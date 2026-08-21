# OntoDesire

A reference ontology for **declaring theoretical commitments about desire**.

Desire is a theoretically contested concept: philosophy of mind offers at least
six rival families of accounts of what desiring essentially is. Ontologies that
represent desire do not say which account they presuppose — and, as our audit
shows, their published definitions often do not even determine one. OntoDesire
inverts the usual strategy: the class `odsr:Desire` is deliberately
underdetermined (a minimal structural skeleton), the rival **theories are
reified as first-class individuals** — linked to the characteristic marks they
privilege, the objections they face, and the ontological category each implies
for desire — and the **residual commitments the core retains are self-declared
with the resource's own vocabulary** (dogfooding: OntoDesire passes the audit
standard it applies to others).

Namespace: `https://w3id.org/ontodesire#` (prefix `odsr:`). Registration of the
w3id redirect is pending; until it resolves, the ontology is served from this
repository and its documentation site.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22037194.svg)](https://doi.org/10.5281/zenodo.22037194)

## Artifacts

| File | IRI / purpose |
|---|---|
| `ontodesire-core.ttl` | `https://w3id.org/ontodesire` — full model: 8 marks, 12 reified theories, 9 objections, 4 partitions of desire, categorial layer (10 stances defined, 9 of them used across the 12 theories), 5 evidence-backed self-declarations + machine-readable essence-level neutrality, individual-distinctness axioms, worked example. |
| `ontodesire-commitments.ttl` | `https://w3id.org/ontodesire/commitments` — **lightweight module asserting no axioms over host terms.** Import this alone to declare commitments. Generic `commitsTo` + four axis-specific subproperties + three audit-outcome properties (`noAttributableCommitmentOn`, `deliberatelyUncommittedOn`, `declaredBySourceOn`). |
| `commitments-audit.ttl` | `https://w3id.org/ontodesire/audit` — criteria-governed reconstructed commitments of MFOEM, MF, SUMO and the FOSSR BDI ontology (+ UFO-C, paper-based, via proxy IRI), with quoted evidence. |
| `audit/CRITERIA.md` | Reconstruction criteria (C1–C3), outcome vocabulary, and the v0.2.0 → v0.3.0 recoding log. |
| `audit/issue-drafts/` | Issue texts for the four audited projects, inviting confirmation or correction of each reconstruction. |
| `audit/retrieve-sources.sh` | Re-retrieves audited sources and records SHA-256 hashes. |
| `shapes/ontodesire-shapes.ttl` | SHACL shapes: closed-world structural validation + axis-correct commitment declarations. |
| `queries/` | Six competency-question queries (`CQ-M1`…`CQ-D1`) + `run_queries.py` + `RESULTS.txt`. |
| `tests/` | Provocation-test suite (`run_tests.py` + `RESULTS.txt`): 5 HermiT tests + 4 SHACL tests. |

## Declaring a commitment (one triple per axis)

```turtle
@prefix odsr: <https://w3id.org/ontodesire#> .

ex:MyDesireClass
    odsr:commitsToFamily  odsr:PleasureBasedFamily ;
    odsr:commitmentEvidence "…quote the definition that grounds this…" .
```

`odsr:commitsTo` and its axis-specific subproperties (`commitsToFamily`,
`commitsToContentStance`, `commitsToCategorialStance`,
`commitsToStructuralStance`) are OWL **annotation** properties, and the module
asserts no logical axioms over host terms: importing it never changes the DL
profile or entailments over your ontology's terms. Declaring **neutrality** is
also one triple: `ex:MyDesireClass odsr:deliberatelyUncommittedOn
odsr:FamilyAxis .` The SHACL shapes validate that each declaration targets an
enumerated individual of the right axis and carries quoted evidence.

## Verification (all runnable locally)

```bash
python3 queries/run_queries.py   # CQ answers + triple counts -> queries/RESULTS.txt
python3 tests/run_tests.py      # HermiT + SHACL provocation tests -> tests/RESULTS.txt
```

- **1043** triples (core + commitments); **1075** with the audit file (rdflib 7.6.0).
- Consistent under **HermiT 1.4.3** (via Owlready2 0.51).
- Provocation tests: a "monofactorial" theory with two distinct marks, a
  desire with two bearers, and an occurrent+standing desire are each detected
  as **inconsistent**; a theory with three distinct marks is **classified as
  holistic by inference**; SHACL flags missing content, axis-mismatched
  declarations, and evidence-less self-declarations. All 9 tests pass, and the
  harness is **hermetic** (strips `owl:imports`; no network access), so results
  are deterministic regardless of w3id registration status.
- Third-party audited sources are **not redistributed**; retrieve them with
  `audit/retrieve-sources.sh` (records hashes to `audit/SOURCES.sha256`).

## Contributing

The primary intended contribution is extending the audit to further resources:
a new axis-specific commitment assertion with quoted evidence, coded under the
criteria in `audit/CRITERIA.md`. Corrections to existing reconstructions are
equally welcome — particularly from maintainers of the audited ontologies.
Please open an issue or a pull request.

## Citation

See `CITATION.cff`. An accompanying manuscript describing the resource is in
preparation.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see `LICENSE`.
