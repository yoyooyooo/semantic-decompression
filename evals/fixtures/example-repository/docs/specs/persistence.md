# Persistence Spec

Status: draft

Target behavior:

1. Commit accepted JobRecord values to a durable store.
2. Reload them after a clean or unclean process restart.
3. Preserve owner revision and reject stale CandidateJob submissions.

No implementation or evidence is attached to this draft.
