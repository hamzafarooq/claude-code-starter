---
name: karpathy-review
description: Review code or a plan against Andrej Karpathy's LLM coding principles — catch over-engineering, silent assumptions, unnecessary abstractions, and scope creep before they ship. Use when the user wants a sanity check on code, a plan, or a feature spec.
---

Review the provided code, plan, or spec against Karpathy's four principles. Credit: guidelines distilled from [Andrej Karpathy's](https://x.com/karpathy) January 2026 observations, adapted by [Forrest Chang](https://github.com/forrestchang/andrej-karpathy-skills).

Ask the user: "Paste the code, plan, or spec you want reviewed."

Then score it against each principle:

---

## Karpathy Review

### 1. Think Before Coding — were assumptions stated?
- Did the solution state its assumptions explicitly, or pick silently between interpretations?
- Are there any unclear requirements that should have triggered a clarifying question?
- **Finding:** PASS / FLAG — [specific observation]

### 2. Simplicity First — is this the minimal solution?
- Does it add features beyond what was asked?
- Are there abstractions written for single-use code?
- Is there "flexibility" or "configurability" that wasn't requested?
- Could this be meaningfully shorter?
- **Finding:** PASS / FLAG — [specific observation, e.g. "This 180-line class could be a 20-line function"]

### 3. Surgical Changes — does it stay in its lane?
- Does it modify adjacent code, formatting, or comments that weren't part of the task?
- Does it refactor things that weren't broken?
- Does it delete pre-existing code that wasn't asked to be removed?
- **Finding:** PASS / FLAG — [specific observation]

### 4. Goal-Driven Execution — is success verifiable?
- Is there a clear success criterion?
- For multi-step work: was a plan stated with checkpoints?
- Is there a way to verify the output without running it?
- **Finding:** PASS / FLAG — [specific observation]

---

### Verdict
| Principle | Result |
|-----------|--------|
| Think before coding | ✅ PASS / ⚠️ FLAG |
| Simplicity first | ✅ PASS / ⚠️ FLAG |
| Surgical changes | ✅ PASS / ⚠️ FLAG |
| Goal-driven execution | ✅ PASS / ⚠️ FLAG |

**One thing to fix:** [If any flags, name the single most important change to make]
