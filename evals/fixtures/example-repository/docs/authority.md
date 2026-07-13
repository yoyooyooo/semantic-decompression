# Job Authority

`CandidateJob` is a proposed job result. It is not canonical and may be rejected or superseded.

The `JobOwner` is the only component allowed to accept a CandidateJob against the current revision.

An accepted proposal becomes a canonical `JobRecord`. Canonical means accepted by the declared owner for this repository. It does not mean persisted across restart or delivered through a product UI.

A projection may display a JobRecord, but projection does not create or change canonical facts.
