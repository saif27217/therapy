# therapy — Decision-Quality Loop

A CBT-informed decision framework for when you have all the facts, the analysis
is clear, and you still can't act.

Not therapy. Structured QC for decisions blocked by bias, fear, and schema —
not by missing information.

## Why It Exists

Standard decision frameworks check: specs, price, capability, structural risk.
They work when the blocker is data. They fail when the blocker is the decider.

This framework adds two layers on top of factual analysis:
- **Bias Mitigation** — 14 questions, 7 cognitive distortions
- **Schema Challenge** — 10 questions, 5 maladaptive belief patterns

Together with factual gates (hard + soft), they form a 4-layer loop that surfaces
and challenges the hidden psychological forces that override rational verdicts.

## The 4-Layer Protocol

```
Layer 1: Hard gates     → structural/spec/financial facts
Layer 2: Soft gates     → payment mode, emergency fund, family risk, utilization
Layer 3: Bias mitigation → 14 questions, 7 distortions
Layer 4: Schema challenge → 10 questions, 5 belief patterns

Verdict: STRONG_BUY / BUY / HOLD
```

## Structure

| Path | Purpose |
|------|---------|
| `LOOP.md` | Cadence, kill gates, exit/entry criteria |
| `STATE.md` | Live gate table and verdict |
| `RUN-LOG.md` | Append-only audit trail |
| `templates/BIAS-MITIGATION.md` | Layer 3 — 14 bias questions |
| `templates/SCHEMA-CHALLENGE.md` | Layer 4 — 10 schema questions |
| `references/theory.md` | Psychological theory reference |
| `scripts/therapy_triage_helper.py` | Validates gate consistency, outputs verdict |

## Use

1. Run Layer 1/2 (hard + soft gates) with `loop-engineering` skill
2. If verdict is blocked by emotional/schema factors → activate this skill
3. Ask all 14 bias questions + all 10 schema questions
4. Score each RESOLVED or UNRESOLVED
5. Any UNRESOLVED → reopen loop, dig deeper
6. All RESOLVED → proceed with clarity

## Integration with Loop Engineering

```
therapy runs AFTER loop-engineering L1 factual analysis.
Sequencing: L1 hard gates → L2 soft gates → L3 bias → L4 schema → verdict.
```

## License

MIT
