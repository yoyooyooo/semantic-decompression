# ADR 0001: In-memory first

Status: accepted

The first implementation stores canonical JobRecord values in process memory. Restart persistence is deferred until the lifecycle semantics and acceptance boundary are stable.

This decision permits same-process tests. It does not authorize claims about restart recovery, database durability, or production readiness.
