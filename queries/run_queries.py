#!/usr/bin/env python3
"""Run the OntoDesire competency-question queries over the released files
and write queries/RESULTS.txt. Also reports the triple counts cited in the
paper (tool: rdflib; version printed in the output header).

Usage:  python3 queries/run_queries.py   (from the repository root)
"""
import glob
import os
import sys

import rdflib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QDIR = os.path.join(ROOT, "queries")
OUT = os.path.join(QDIR, "RESULTS.txt")

CORE = ["ontodesire-core.ttl", "ontodesire-commitments.ttl"]
AUDIT = "commitments-audit.ttl"


def load(files):
    g = rdflib.Graph()
    for f in files:
        g.parse(os.path.join(ROOT, f), format="turtle")
    return g


def main():
    g_core = load(CORE)
    g_all = load(CORE + [AUDIT])
    # CQ-M4 is computed from the audit file + the commitments module it
    # imports, exemplifying third-party usage; all other CQs run over the
    # full merged graph.
    g_audit = load(["ontodesire-commitments.ttl", AUDIT])

    lines = []
    lines.append(f"# OntoDesire query results (tool: rdflib {rdflib.__version__})")
    lines.append(f"Triples core+commitments: {len(g_core)}")
    lines.append(f"Triples core+commitments+audit: {len(g_all)}")
    lines.append("")

    for qfile in sorted(glob.glob(os.path.join(QDIR, "CQ-*.rq"))):
        name = os.path.basename(qfile)
        graph = g_audit if name.startswith("CQ-M4") else g_all
        with open(qfile, encoding="utf-8") as fh:
            query = fh.read()
        lines.append(f"== queries/{name} ==")
        for row in graph.query(query):
            lines.append(" | ".join("" if v is None else str(v) for v in row))
        lines.append("")

    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines))
    print("\n".join(lines))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    sys.exit(main())
