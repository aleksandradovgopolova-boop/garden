"""Regression cases for previously green-but-incomplete repository checks."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

DOCS, SITE = module('check_docs'), module('check_site')

class DocsChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for directory in ('public', 'internal', 'templates', '.github', 'archive'):
            shutil.copytree(ROOT / directory, self.root / directory)
        for file in [*ROOT.glob('*.md'), ROOT / 'MANIFEST.json']:
            shutil.copy(file, self.root)
    def tearDown(self):
        self.temp.cleanup()
    def errors(self):
        return '\n'.join(DOCS.check(self.root)[0])
    def test_current_docs_pass(self):
        self.assertEqual(self.errors(), '')
    def test_yaml_parse_error_fails(self):
        p = self.root / 'README.md'
        p.write_text(p.read_text().replace('owner: "aleksandradovgopolova-boop"', 'owner: [broken'))
        self.assertIn('Invalid frontmatter', self.errors())
    def test_duplicate_metadata_fails(self):
        p = self.root / 'README.md'
        p.write_text(p.read_text().replace('status: accepted', 'status: accepted\nstatus: proposed'))
        self.assertIn('duplicate YAML key', self.errors())
    def test_unknown_status_fails(self):
        p = self.root / 'README.md'
        p.write_text(p.read_text().replace('status: accepted', 'status: shipped'))
        self.assertIn('Unknown status', self.errors())
    def test_broken_related_link_fails(self):
        p = self.root / 'internal/product/ai/ai-runtime-requirements.md'
        p.write_text(p.read_text().replace('../../engineering/', '../../04_ENGINEERING/'))
        self.assertIn('Broken link', self.errors())
    def test_missing_nested_public_section_fails(self):
        p = self.root / 'public/wowrepo.yml'
        p.write_text(p.read_text().replace('  - label: Основополагающие исследования\n    path: 06-research/foundational\n', ''))
        self.assertIn('Public page not ingested', self.errors())
    def test_public_link_to_team_fails(self):
        p = self.root / 'public/README.md'
        p.write_text(p.read_text() + '\n[team](../internal/README.md)\n')
        self.assertIn('Public link leaves public/', self.errors())
    def test_compilation_does_not_grant_embedded_approval(self):
        p = self.root / 'internal/decisions/registry.json'
        data = json.loads(p.read_text())
        next(r for r in data['records'] if r['id'] == 'GDR-008')['status'] = 'accepted'
        p.write_text(json.dumps(data))
        self.assertIn('GDR registry status conflict: GDR-008', self.errors())
    def test_missing_decision_fails(self):
        p = self.root / 'internal/decisions/registry.json'
        data = json.loads(p.read_text())
        data['records'] = [r for r in data['records'] if r['id'] != 'ADR-004']
        p.write_text(json.dumps(data))
        self.assertIn('Decision registry coverage mismatch', self.errors())
    def test_body_status_conflict_fails(self):
        p = self.root / 'internal/product/ai/ai-product-contract.md'
        p.write_text(p.read_text().replace('status: proposed', 'status: accepted', 1))
        self.assertIn('Body/frontmatter status conflict', self.errors())
    def test_navigation_traversal_fails(self):
        p = self.root / 'public/wowrepo.yml'
        p.write_text(p.read_text() + '\n')
        text = p.read_text().replace('path: 01-introduction', 'path: ../internal')
        p.write_text(text)
        self.assertIn('Invalid public navigation path', self.errors())

class ArtifactChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.public, self.out = self.root / 'public', self.root / 'dist'
        self.public.mkdir(); self.out.mkdir()
        (self.public / 'README.md').write_text('# Garden')
        (self.public / 'research').mkdir()
        (self.public / 'research/report.md').write_text('# Report')
        (self.out / 'research/report').mkdir(parents=True)
        (self.out / 'index.html').write_text('<a href="/garden/research/report/">report</a>')
        (self.out / 'research/report/index.html').write_text('<main id="report">Report</main>')
    def tearDown(self):
        self.temp.cleanup()
    def errors(self):
        return '\n'.join(SITE.check(self.out, self.public))
    def test_complete_artifact_passes(self):
        self.assertEqual(self.errors(), '')
    def test_missing_report_fails(self):
        (self.out / 'research/report/index.html').unlink()
        self.assertIn('Public page missing', self.errors())
    def test_broken_asset_and_anchor_fail(self):
        (self.out / 'index.html').write_text('<img src="/garden/missing.png"><a href="/garden/research/report/#missing">report</a>')
        self.assertIn('Broken artifact link', self.errors())
        self.assertIn('Broken artifact anchor', self.errors())
    def test_private_artifact_fails(self):
        (self.out / 'internal').mkdir()
        (self.out / 'internal/secret.html').write_text('Team document')
        self.assertIn('Non-public source artifact', self.errors())
        self.assertIn('Unexpected HTML page', self.errors())
    def test_base_path_error_fails(self):
        (self.out / 'index.html').write_text('<a href="/research/report/">report</a>')
        self.assertIn('Local link leaves deployment base', self.errors())
    def test_external_links_are_not_fetched(self):
        (self.out / 'index.html').write_text('<a href="https://example.invalid/report">external</a>')
        self.assertEqual(self.errors(), '')

class WorkflowBoundary(unittest.TestCase):
    def test_quality_workflow_has_no_publication(self):
        data = DOCS.load_yaml((ROOT / '.github/workflows/quality.yml').read_text())
        # PyYAML YAML 1.1 treats "on" as bool; the checks below concern jobs/permissions.
        self.assertEqual(data['permissions'], {'contents': 'read'})
        self.assertNotIn('deploy', data['jobs'])
        self.assertEqual(data['jobs']['build']['needs'], 'docs')
        for job in data['jobs'].values():
            for step in job.get('steps', []):
                if 'uses' in step:
                    self.assertRegex(step['uses'], r'@[0-9a-f]{40}$')
        self.assertRegex(data['env']['WOWREPO_ENGINE_REF'], r'^[0-9a-f]{40}$')
        self.assertNotIn('upload-pages-artifact', (ROOT / '.github/workflows/quality.yml').read_text())

if __name__ == '__main__':
    unittest.main()
