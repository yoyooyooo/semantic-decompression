# Synthetic Security Plan

This fixture describes a proposed design, not a deployed or verified system.

The threat model includes a signed-in user trying to export another project's records. The trust boundary is between an authenticated request and authority to act on a specific project's data. Authentication identifies the requester; it does not by itself grant export permission.

The gateway authenticates the request. A policy service checks project membership and export permission, then issues a project-scoped grant that expires after ten minutes. A worker checks the grant's scope and expiry before executing an export. This is the plan's least privilege mechanism: the grant does not authorize other projects or other actions.

The audit store records the decision and job outcome, not the exported records or credentials. An invalid or expired grant stops that job. Each worker job has a separate temporary directory, intended to limit the blast radius of a job failure. Runtime isolation and crash recovery have not been tested. The plan does not define retry policy or prove that partial exports are rolled back.
