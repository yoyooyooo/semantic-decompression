# Current Architecture

The current runtime contains one `JobOwner` and an in-memory map of accepted `JobRecord` values.

The owner checks the expected revision before accepting a CandidateJob. On success it writes the record to the map and returns the new revision.

There is no database adapter, restart loader, real provider adapter, browser transport, or deployment configuration in the current snapshot.
