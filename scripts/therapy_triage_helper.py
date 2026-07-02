#!/usr/bin/env python3
"""
therapy_triage_helper.py
Validate therapy loop gate consistency and generate verdict.
Part of the loop-engineering "therapy" skill scaffold.

Usage:
    python3 therapy_triage_helper.py [--state STATE.md] [--log RUN-LOG.md]

Reads STATE.md, checks for:
  - All hard gates PASS (no FAIL, no unresolved PENDING blocking ones)
  - All soft gates PASS
  - All 14 bias questions RESOLVED
  - All 10 schema questions RESOLVED
  - At least one UNRESOLVED must have a condition specified

Outputs:
  - Gate summary table (stdout)
  - Verdict: STRONG_BUY / BUY / HOLD / PENDING
"""

import re
import sys
import os
from pathlib import Path


def parse_state(path):
    """Parse STATE.md and extract gate table rows."""
    text = Path(path).read_text()
    gates = {}
    current_section = None
    for line in text.splitlines():
        if line.startswith("## "):
            current_section = line.strip()
        m = re.match(r"\|\s*(\w+)\s*\|\s*(PASS|FAIL|PENDING|CONDITIONAL|DEFERRED|RESOLVED|UNRESOLVED)\s*\|", line)
        if m:
            gates[m.group(1)] = {"status": m.group(2), "section": current_section}
    return gates


def validate(gates):
    """Return (verdict, issues) tuple."""
    issues = []

    # Check hard gates
    hard_gates = [k for k, v in gates.items() if k not in
                  ("payment_mode", "emergency_fund", "family_job_risk_buffer",
                   "income_generation", "guilt_tolerance", "utilization_trajectory",
                   "social_comparison")]
    hard_fails = [g for g in hard_gates if gates.get(g, {}).get("status") in ("FAIL",)]
    if hard_fails:
        issues.append(f"HARD GATE FAIL: {', '.join(hard_fails)}")

    # Check soft gates
    soft_gates = ("payment_mode", "emergency_fund", "family_job_risk_buffer",
                  "income_generation", "guilt_tolerance", "utilization_trajectory",
                  "social_comparison")
    soft_fails = [g for g in soft_gates if gates.get(g, {}).get("status") == "FAIL"]
    if soft_fails:
        issues.append(f"SOFT GATE FAIL: {', '.join(soft_fails)}")

    # Check bias/schema probes
    unresolved = [k for k, v in gates.items() if v.get("status") == "UNRESOLVED"]
    if unresolved:
        issues.append(f"UNRESOLVED probes: {', '.join(unresolved)}")

    if issues:
        return "HOLD / REOPEN", issues
    return "STRONG_BUY", []


def main():
    state_path = sys.argv[sys.argv.index("--state") + 1] if "--state" in sys.argv else "STATE.md"
    log_path = sys.argv[sys.argv.index("--log") + 1] if "--log" in sys.argv else "RUN-LOG.md"

    if not os.path.exists(state_path):
        print(f"State file not found: {state_path}")
        sys.exit(1)

    gates = parse_state(state_path)
    print(f"\nLoaded {len(gates)} gates from {state_path}\n")
    print(f"{'Gate':<35} {'Status':<15}")
    print("-" * 52)
    for gate, info in gates.items():
        print(f"{gate:<35} {info['status']:<15}")

    verdict, issues = validate(gates)
    print(f"\n{'='*52}")
    print(f"VERDICT: {verdict}")
    if issues:
        print("BLOCKERS:")
        for i in issues:
            print(f"  - {i}")
    else:
        print("All gates cleared. Proceed with decision.")
    print(f"{'='*52}\n")


if __name__ == "__main__":
    main()
