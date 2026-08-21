# Issue draft for the FOSSR BDI Ontology tracker
**Tracker:** see the project links at https://w3id.org/fossr/ontology/bdi

**Title**: Theoretical commitments of `Desire` — external audit, request for confirmation

Hello — as part of OntoDesire (https://github.com/santos-wesley/ontodesire), we audited how
existing ontologies represent desire. For the BDI Ontology's `Desire` class
(v0.5), we reconstructed:

1. **Categorial stance**: desire as a state type occupying a causal role —
   grounded in "The Desire class represents a motivational mental state of an
   agent [...] unlike intentions, they do not imply a commitment to act.
   Desires serve as the driving force behind an agent's decision-making
   process."
2. **Essence-level theory**: we coded this **not attributable**: the
   definition describes desire's functional role in the agent architecture
   (Bratman-style), which is compatible with several rival accounts of what
   desiring essentially is (action-based, holistic, and others).

One further observation, outside our coding axes but possibly of interest:
the axiom `Desire subClassOf isMotivatedBy some Belief` makes every desire
belief-motivated — a substantive formation-level commitment (contestable for
basic/instinctual desires) that you may wish to document; and the separate
`Desire` / `DesireProcess` state–process split corroborates our causal-role
state coding.

Questions:
- Do you confirm that the ontology intends only the architectural/functional
  characterization, with no position on desire's essence?
- Would you consider declaring this explicitly (one annotation triple with
  the OntoDesire commitments vocabulary, or prose documentation)?

Full audit, criteria, and quoted evidence: https://github.com/santos-wesley/ontodesire/tree/main/audit/. Responses
will be recorded (confirmed / contested) in the audit's next release.

Note: since v0.3.0 the vocabulary also lets a source declare *neutrality*
in one triple — ex: `bdi:Desire odsr:deliberatelyUncommittedOn odsr:FamilyAxis .`
— so 'we take no position' is itself a declarable, queryable outcome.
