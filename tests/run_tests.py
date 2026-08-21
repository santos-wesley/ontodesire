#!/usr/bin/env python3
"""OntoDesire provocation-test suite (v0.3.0).

Positive check: the released ontology is consistent under HermiT.
Provocation checks: deliberately ill-formed additions must be DETECTED --
either as OWL inconsistency (HermiT, via Owlready2) or as SHACL
non-conformance (pySHACL). A consistency claim is only informative if the
axioms can in principle be violated; this suite demonstrates that they can.

Usage:  python3 tests/run_tests.py     (from the repository root)
Requires: rdflib, owlready2 (bundles HermiT; needs Java), pyshacl.
Writes tests/RESULTS.txt.
"""
import os
import sys
import tempfile

import rdflib
import owlready2
from pyshacl import validate

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "tests", "RESULTS.txt")
ODSR = "https://w3id.org/ontodesire#"

BASE_FILES = ["ontodesire-core.ttl", "ontodesire-commitments.ttl"]

PREFIXES = """
@prefix odsr: <https://w3id.org/ontodesire#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
"""

# --- OWL provocations: each block is (name, expectation, extra turtle) ---
OWL_TESTS = [
    ("T1 base ontology", "consistent", ""),
    ("T2 monofactorial theory with two distinct marks", "INCONSISTENT", PREFIXES + """
odsr:testRogueMono a odsr:MonofactorialTheory , owl:NamedIndividual ;
    odsr:identifiesDesireWith odsr:ActionDisposition , odsr:PleasureDisposition .
"""),
    ("T3 desire with two distinct bearers", "INCONSISTENT", PREFIXES + """
odsr:testBearerA a odsr:Human , owl:NamedIndividual .
odsr:testBearerB a odsr:Human , owl:NamedIndividual .
odsr:testBearerA owl:differentFrom odsr:testBearerB .
odsr:testGreedyDesire a odsr:Desire , owl:NamedIndividual ;
    odsr:hasBearer odsr:testBearerA , odsr:testBearerB .
"""),
    ("T4 desire both occurrent and standing", "INCONSISTENT", PREFIXES + """
odsr:testJanusDesire a odsr:OccurrentDesire , odsr:StandingDesire , owl:NamedIndividual .
"""),
    ("T5 unlabelled theory with three distinct marks classified holistic", "INFERRED holistic", PREFIXES + """
odsr:testAnonymousTheory a odsr:TheoryOfDesire , owl:NamedIndividual ;
    odsr:identifiesDesireWith odsr:ActionDisposition , odsr:PleasureDisposition , odsr:ReasonsAttention .
"""),
]

# --- SHACL provocations: (name, extra turtle, expect_conforms) ---
SHACL_TESTS = [
    ("S1 released files", "", True),
    ("S2 desire with no asserted content", PREFIXES + """
odsr:testMuteDesire a odsr:Desire , owl:NamedIndividual ;
    odsr:hasBearer odsr:Nora .
""", False),
    ("S3 commitsToFamily targeting a categorial stance", PREFIXES + """
odsr:testConfusedTerm odsr:commitsToFamily odsr:DispositionCategory ;
    odsr:commitmentEvidence "test" .
""", False),
    ("S4 structural-stance self-declaration without evidence", PREFIXES + """
odsr:testShyDeclarer odsr:commitsToStructuralStance odsr:SingleBearer .
""", False),
]


def merged_graph(extra_ttl=""):
    g = rdflib.Graph()
    for f in BASE_FILES:
        g.parse(os.path.join(ROOT, f), format="turtle")
    if extra_ttl:
        g.parse(data=extra_ttl, format="turtle")
    # The suite is hermetic: both modules are already merged locally, so the
    # owl:imports triple must go. Otherwise owlready2 may (depending on
    # serialization order) try to HTTP-resolve the w3id IRI -- a network
    # dependency that made results nondeterministic and, once the redirect is
    # registered, would silently mix the published module with the local one.
    from rdflib.namespace import OWL
    g.remove((None, OWL.imports, None))
    return g


def run_owl_test(name, expectation, extra_ttl):
    g = merged_graph(extra_ttl)
    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, "merged.owl")
        g.serialize(destination=path, format="xml")
        world = owlready2.World()
        onto = world.get_ontology("file://" + path.replace(os.sep, "/")).load()
        try:
            with onto:
                owlready2.sync_reasoner(world, debug=0)
        except owlready2.base.OwlReadyInconsistentOntologyError:
            return "INCONSISTENT"
        if expectation.startswith("INFERRED"):
            ind = world[ODSR + "testAnonymousTheory"]
            holistic = world[ODSR + "HolisticTheory"]
            if ind is not None and holistic in ind.is_a:
                return "INFERRED holistic"
            return "not inferred"
        return "consistent"


def main():
    lines = [f"# OntoDesire provocation tests (owlready2 {owlready2.VERSION}, HermiT bundled)"]
    ok = True
    for name, expectation, extra in OWL_TESTS:
        result = run_owl_test(name, expectation, extra)
        passed = result == expectation
        ok &= passed
        lines.append(f"[{'PASS' if passed else 'FAIL'}] {name}: expected {expectation}, got {result}")

    shapes = rdflib.Graph().parse(os.path.join(ROOT, "shapes", "ontodesire-shapes.ttl"), format="turtle")
    for name, extra, expect_conforms in SHACL_TESTS:
        g = merged_graph(extra)
        g.parse(os.path.join(ROOT, "commitments-audit.ttl"), format="turtle")
        conforms, _, _ = validate(g, shacl_graph=shapes, inference="none")
        passed = conforms == expect_conforms
        ok &= passed
        lines.append(f"[{'PASS' if passed else 'FAIL'}] {name}: expected conforms={expect_conforms}, got {conforms}")

    lines.append("ALL PASS" if ok else "FAILURES PRESENT")
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
