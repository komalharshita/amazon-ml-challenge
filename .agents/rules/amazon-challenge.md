# Amazon ML Challenge Development Rules

## Core Principle

This project must be built incrementally with manual verification after every
major stage.

NEVER implement multiple major pipeline stages in a single task unless
explicitly instructed.

## Human Verification Gate

After completing the requested task:

1. Run relevant tests/checks.
2. Show exactly which files changed.
3. Explain what was implemented.
4. Show important outputs/metrics.
5. STOP.
6. Do not continue to the next pipeline stage.
7. Wait for explicit human approval.

Never assume that a passing Python execution means the implementation is
correct.

## Challenge Constraints

- Use only the provided challenge data.
- Do not use external databases.
- Do not use external APIs.
- Do not use geocoding.
- Source 1 is the entity-resolution anchor.
- Source 2 and Source 3 contain candidate entities.
- A Source 1 entity can have zero, one, or many matches.
- Blocking is candidate generation, not final matching.
- Optimize for the challenge's macro F0.5 metric.
- False merges are particularly costly.
- Do not assume a 0.50 probability threshold.
- Preserve the exact submission schema provided by the organizers.

## Coding Rules

- Prefer simple, readable Python.
- Use type hints where useful.
- Avoid unnecessary dependencies.
- Do not modify unrelated files.
- Do not silently change existing behavior.
- Do not fabricate dataset columns.
- Inspect the actual dataset before writing dataset-specific logic.
- Add tests for every transformation that materially affects matching.

## Verification

Every stage must have:
- automated checks
- manual verification instructions
- expected result
- actual result

Do not proceed until the human explicitly approves the stage.
