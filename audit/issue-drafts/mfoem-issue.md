# Issue draft for the Emotion Ontology (MFOEM) tracker
**Tracker:** https://github.com/jannahastings/emotion-ontology/issues

**Title**: Theoretical commitments of `feeling of desire` (MFOEM:000220) — external audit, request for confirmation

Hello. As part of OntoDesire (https://github.com/santos-wesley/ontodesire), a resource for
declaring theoretical commitments about desire, we audited how existing
ontologies represent desire and cognate states. We reconstructed the
following for MFOEM:000220 (*feeling of desire*), version 2025-07-31, and
would value your confirmation or correction:

1. **Content stance**: desires-are-for-states-of-affairs, grounded in the
   definition "A subjective affective feeling that involves attraction to an
   imagined state of affairs."
2. **Categorial stance**: occurrent affective episode, since the term is itself a
   feeling.
3. **Essence-level theory**: we coded this **not attributable**: the
   definition characterizes the *feeling of* desire rather than desire, which
   we read as a scope decision of an emotion ontology. The anticipated
   pleasure / anticipated relief subclass split (MFOEM:000221/000222)
   *suggests* a pleasure-based reading of desire, but does not assert one.

Questions:
- Do you confirm the "scope decision" reading, i.e. MFOEM intends no position
  on what desire essentially is?
- Would you consider declaring this explicitly (one annotation triple using
  the OntoDesire commitments vocabulary, or prose in the term's editor note)?

The full audit, criteria, and quoted evidence:
https://github.com/santos-wesley/ontodesire/blob/main/audit/CRITERIA.md and commitments-audit.ttl. Responses will
be recorded (confirmed / contested) in the audit's next release.

Note: since v0.3.0 the vocabulary also lets a source declare *neutrality*
in one triple: `obo:MFOEM_000220 odsr:deliberatelyUncommittedOn odsr:FamilyAxis .`
So 'we take no position' is itself a declarable, queryable outcome.
