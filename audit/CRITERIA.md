# Audit reconstruction criteria (v0.3.0)

This document states the coding criteria under which the commitments in
`commitments-audit.ttl` were reconstructed, and the outcome vocabulary. It
exists so that the audit is falsifiable: anyone can re-apply the criteria to
the quoted evidence and check the coding.

## Unit of analysis

One *term* (class or predicate) per source that represents desire or the
closest cognate conative state, identified by searching the source's labels
and definitions for "desire", "want", and cognates. For each term, three
independent axes are coded.

## Criteria

**C1 — Theory family** (`odsr:commitsToFamily`). Attributable **only if** the
source's definition or axioms *identify desire itself* with the
characteristic mark of one family — a definitional identification or
equivalence ("to desire p is to …", an equivalence axiom, or a genus that IS
the mark). The following do **not** license family attribution:

- descriptions of desire's *functional role* in an architecture (input to
  deliberation, driver of decision-making) — compatible with several
  essence-level theories;
- representation of an *associated state* (e.g. the feeling of desire) rather
  than desire itself — a scope decision;
- subclass structure that merely *suggests* a reading without a definitional
  identification.

**C2 — Content stance** (`odsr:commitsToContentStance`). Attributable only if
the source's axioms or definitions fix the content kind of the term (e.g. a
domain/range axiom typing the object as a Formula/state of affairs, or a
definition quantifying over states of affairs).

**C3 — Categorial stance** (`odsr:commitsToCategorialStance`). Attributable
only if the term's placement in the source's own taxonomy, or its explicit
definition, fixes an ontological category (e.g. subclass of *mental process*,
*affective representation*, characterization as a causal-functional state).

**Referent scoping (C2/C3).** When the audited term represents a
desire-*cognate* rather than desire itself (e.g. MFOEM's *feeling of desire*,
MF's *wanting*), C2/C3 attributions code the content kind and category the
source fixes **for that term's referent** — not a thesis about desire in
general. Only C1 concerns desire's own essence, which is why an
associated-state or role representation blocks C1 but not C2/C3. The stance
labels ("desire as …") name positions in desire's theory space; in audit use
they are read referent-scoped (this is stated in the vocabulary's
`skos:definition`s and in each entry's note).

## Outcomes

Per axis, exactly one of — **each machine-readable**:

| Outcome | Meaning | Machine-readable form |
|---|---|---|
| `attributable` | The criterion is met; the coding is asserted with quoted evidence. | a `commitsTo*` triple |
| `not attributable` | The published text/axioms underdetermine the axis (any *suggested but unattributable* reading goes in the note). | `odsr:noAttributableCommitmentOn <axis>` |
| `declared-by-source` | The source itself states and argues the commitment. | `odsr:declaredBySourceOn <axis>` alongside the `commitsTo*` triple |

A source can also *declare its own neutrality* on an axis in one triple:
`ex:Term odsr:deliberatelyUncommittedOn odsr:FamilyAxis` — OntoDesire's own
`Desire` class does exactly this for the essence-level axis. Underdetermination
is therefore a queryable outcome (see CQ-M4), not prose-only.

Findings *outside* the C1–C3 axes (e.g. BDI's `isMotivatedBy some Belief`
formation axiom) do not receive codings, but are recorded in the entry's
`commitmentNote` for the maintainers' attention.

**"Not attributable" is a first-class finding.** That a published definition
does not even determine which theory of desire the resource presupposes is
the sharpest form of the transparency gap OntoDesire addresses.

## Evidence discipline

- Every attribution carries a verbatim quotation (`odsr:commitmentEvidence`).
- Sources are pinned: OBO releases by version IRI date, GitHub sources by
  commit hash, and all retrieved files by SHA-256
  (`audit/retrieve-sources.sh` records them).
- File-audited entries use the source's own IRIs; paper-based entries use
  proxy IRIs in the OntoDesire namespace (`odsr:proxy-<source>-<Term>`).

## Validation status and maintainer engagement

The coding was performed by the resource author, so it carries the bias of a
single interpreter. As external validation, each reconstruction is being
filed with the source project's issue tracker (texts in
`audit/issue-drafts/`); maintainer responses (confirmed / contested / no
response) will be recorded in `odsr:commitmentNote` in subsequent releases.
Until those responses arrive, every coding here should be read as a
documented reconstruction open to correction, not as a settled attribution.

## v0.2.0 → v0.3.0 recoding log

| Term | v0.2.0 coding | v0.3.0 coding | Reason |
|---|---|---|---|
| MFOEM:000220 | PleasureBasedFamily + OccurrentFeelingCategory + StateOfAffairsContent | StateOfAffairsContent + OccurrentAffectiveEpisodeCategory; family **not attributable** | C1: definition characterizes the *feeling of* desire, not desire; category corrected to occurrent episode (the term is a feeling, not a disposition to feelings). |
| MF:0000045 | MentalProcessCategory + StateOfAffairsContent | unchanged (+ explicit "essence undetermined by circularity") | Already conforming. |
| sumo:desires | StateOfAffairsContent | unchanged (+ explicit "essence not attributable") | Already conforming. |
| bdi:Desire | ActionBasedFamily + CausalRoleStateCategory | CausalRoleStateCategory; family **not attributable** | C1: motivational-role description does not identify desire with disposition-to-act. |
| UFO-C Desire | StateOfAffairsContent + MentalMomentCategory (minted `w3id.org/ufo-c/Desire`) | unchanged coding; subject moved to `odsr:proxy-UFOC-Desire` | Provenance convention: no IRIs minted in namespaces we do not control. |
