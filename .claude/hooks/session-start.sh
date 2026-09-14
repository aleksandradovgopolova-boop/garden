#!/bin/bash
# AI OPS kit — SessionStart hook.
# Prepares the environment so the documentation and site-build quality gates
# can run during a session. Idempotent and non-interactive.
set -euo pipefail

PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
REQ="$PROJECT_DIR/scripts/requirements.txt"

# check_docs.py uses only the standard library. build_site.py needs the
# packages in scripts/requirements.txt; install them best-effort so the site
# preview and the full gate runner work without blocking session start.
if [ -f "$REQ" ]; then
  python3 -m pip install --quiet --disable-pip-version-check -r "$REQ" \
    || echo "AI OPS kit: could not install scripts/requirements.txt (offline?); the documentation gate still runs without it." >&2
fi

echo "AI OPS kit ready. Run 'python scripts/quality_gates.py' before proposing changes."
