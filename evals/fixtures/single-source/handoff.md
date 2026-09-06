# Synthetic Handoff Notes

Snapshot: 2026-09-01. These notes are the supplied design description, not evidence that the referenced code or tests were inspected.

A request enters POST /jobs. The API validates the payload and writes a Pending job to the jobs table. A worker reads Pending jobs and changes a selected job to Running. It performs the requested transformation, stores the result reference, and changes the job to Completed. A validation failure returns an error before a job is created. A transformation failure changes the job to Failed and records a reason.

The jobs table is the authoritative job state. Notifications only prompt the UI to refresh that state. A lost notification does not itself change a job's status; the UI polls the jobs endpoint every five seconds as a fallback.

Maintenance entry points named by the notes are api/jobs.ts for input handling, worker/execute.ts for execution, and db/jobs.ts for state changes. The API team owns validation, and the worker team owns execution. These paths are illustrative and are not additional supplied files.

The notes do not define how concurrent workers claim jobs, how a Running job is recovered after a crash, or whether retries are safe. No claim of exactly-once execution is made. Investigate those questions before promising automatic recovery. For the current task, no code or runtime tests are available.
