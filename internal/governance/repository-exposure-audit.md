---
title: "Repository Exposure Audit — P0"
status: accepted
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: false
---

# Repository Exposure Audit — P0

## Access remediation evidence

The owner initially chose private visibility, then restored public visibility after GitHub rejected private-repository branch protection on the current plan. The historical private interval was confirmed by authenticated API and an unauthenticated repository 404; it is not the current access boundary. The repository and all tracked source files are now publicly readable. Pages configuration was deleted and the legacy deployment workflow disabled. The proposed quality workflow builds without deployment or artifact publication; its CI logs are public.

## Targeted historical credential check

The scan covered 221 historical Git blobs reachable from the cloned main history and 306 archive members. It tested high-confidence private-key headers, GitHub token formats and AWS access-key formats. Zero pattern matches were found. Only safe aggregate counts were emitted; no candidate credential content was logged.

This check does not establish that there is no personal data, credential in another format, remote fork, cache or leaked copy. Archived research documents remain historical sources; raw participant data must be stored outside Git under appropriate controls. No history rewriting or credential rotation was performed because no credential was identified by this check. The scan alone does not certify every archived document as appropriate for public release; any subsequently identified confidential material must be removed from the public source under a separately reviewed cleanup.

## Future handling

A verified sensitive-data finding must be addressed in the owning system before any cleanup of Git history. Folder names are not an access boundary. Confidential material must remain outside this public repository under separate access controls. Reopening public publication requires the owner-approved process in [Publication Policy](PUBLICATION_POLICY.md).
