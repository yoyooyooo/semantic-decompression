import { strict as assert } from "node:assert"
import { JobOwner } from "../src/runtime"

const owner = new JobOwner()
const record = owner.accept({ id: "job-1", expectedRevision: 0, output: "ok" })

assert.equal(record.revision, 1)
assert.equal(record.output, "ok")

// This test does not restart the process or use a database, provider, or browser.
