# Current Architecture

Snapshot: 2026-07-10

A relay attempt can produce a Candidate. The conversation owner may accept that Candidate and commit it as the canonical message. In this runtime scope, accepted means committed to the canonical conversation history.

Persistence interfaces and an in-memory replay fixture exist. The durable storage adapter is a scaffold. End-to-end replay after a process restart has not been verified for the current snapshot.
