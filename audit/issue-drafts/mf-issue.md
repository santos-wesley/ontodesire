# Issue draft for the Mental Functioning Ontology (MF) tracker
**Tracker:** https://github.com/jannahastings/mental-functioning-ontology/issues

**Title**: `wanting` (MF:0000045) is defined via "desire", but MF has no desire class — circularity report + commitments audit

Hello — as part of OntoDesire (https://github.com/santos-wesley/ontodesire), we audited how
existing ontologies represent desire and cognate states. For MF:0000045
(*wanting*), version 2025-07-08, we found:

1. **Circularity**: the definition — "A mental process that involves thinking
   about a state of affairs that is not yet the case together with a desire
   for that state of affairs to come about" — defines *wanting* in terms of
   *desire*, but MF contains no class labelled "desire". The essence-level
   commitment is left undetermined by the circularity.
2. **Categorial stance** (reconstructed): mental process — silently made by
   the genus.
3. **Content stance** (reconstructed): desires-are-for-states-of-affairs.

Suggestions:
- Either add a `desire` class the definition can refer to, or reword the
  definition to break the circle;
- Consider declaring the categorial commitment explicitly (one annotation
  triple with the OntoDesire commitments vocabulary, or an editor note).

Full audit, criteria, and quoted evidence: https://github.com/santos-wesley/ontodesire/tree/main/audit/. Responses
will be recorded (confirmed / contested) in the audit's next release.

Note: since v0.3.0 the vocabulary also lets a source declare *neutrality*
in one triple — ex: `obo:MF_0000045 odsr:deliberatelyUncommittedOn odsr:FamilyAxis .`
— so 'we take no position' is itself a declarable, queryable outcome.
