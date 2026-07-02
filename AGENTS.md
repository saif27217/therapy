# therapy-repo

Decision-quality loop — CBT-informed bias and schema mitigation for high-stakes decisions.

## What This Is

When you have all the facts, the math is clear, and you still can't decide — the
blocker is not information. It's the decider.

This repo supplies a 4-layer gate protocol:
1. Hard gates (factual)
2. Soft gates (financial/situational)
3. Bias mitigation (14 questions, 7 distortions)
4. Schema challenge (10 questions, 5 maladaptive patterns)

Ported from a real first-person decision session and formalized for reuse.

## Repo Contents

| File | Purpose |
|------|---------|
| `LOOP.md` | Cadence, kill gates, exit/entry criteria |
| `STATE.md` | Live gate table and verdict |
| `RUN-LOG.md` | Append-only audit trail |
| `templates/BIAS-MITIGATION.md` | Layer 3 — 14 bias questions |
| `templates/SCHEMA-CHALLENGE.md` | Layer 4 — 10 schema questions |
| `references/theory.md` | Psychological theory reference |
| `scripts/therapy_triage_helper.py` | Validates gate consistency |

## Usage

```bash
git clone <url>
cd therapy-repo
cp templates/BIAS-MITIGATION.md .   # and SCHEMA-CHALLENGE.md
# edit STATE.md with your decision gates and answers
python3 scripts/therapy_triage_helper.py --state STATE.md --log RUN-LOG.md
```

## Integration with loop-engineering

```
therapy is the L2/L3/L4 layer on top of loop-engineering L1 factual analysis.
```

## License

MIT
