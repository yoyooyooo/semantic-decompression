export type CandidateJob = Readonly<{
  id: string
  expectedRevision: number
  output: string
}>

export type JobRecord = Readonly<{
  id: string
  revision: number
  output: string
}>

export class JobOwner {
  private readonly records = new Map<string, JobRecord>()

  accept(candidate: CandidateJob): JobRecord {
    const current = this.records.get(candidate.id)
    const revision = current?.revision ?? 0
    if (candidate.expectedRevision !== revision) {
      throw new Error("stale revision")
    }
    const record = {
      id: candidate.id,
      revision: revision + 1,
      output: candidate.output,
    }
    this.records.set(candidate.id, record)
    return record
  }
}
