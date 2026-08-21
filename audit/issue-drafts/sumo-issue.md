# Issue draft for the SUMO tracker
**Tracker:** https://github.com/ontologyportal/sumo/issues

**Title**: `desires` / `wants` — the possession-rewrite axiom takes a contested stand on object-desire; commitments audit

Hello — as part of OntoDesire (https://github.com/santos-wesley/ontodesire), we audited how
existing ontologies represent desire. For SUMO's `desires` and `wants`
(Merge.kif, commit `4444031ad0c1643a9fa6808c35e5f47ecd7f1e3a`), we reconstructed:

1. **Content stance**: desires-are-for-states-of-affairs — `desires` is a
   `PropositionalAttitude`, and the axiom
   `(=> (and (wants ?AGENT ?OBJ) (instance ?OBJ Object)) (desires ?AGENT (possesses ?AGENT ?OBJ)))`
   reduces object-directed wanting to a propositional desire about possession.
2. **Essence-level theory**: not attributable — the axioms fix content and
   inferential role, not what desiring essentially is.

One substantive note: the philosophical literature on desire content rejects
the possession disambiguation as a general rule (a want for tea is normally
satisfied by *drinking* soon, not by *possessing*); the rewrite axiom
therefore takes a side on a contested question without flagging it. You may
consider weakening the axiom or documenting the choice.

Full audit, criteria, and quoted evidence: https://github.com/santos-wesley/ontodesire/tree/main/audit/. Responses
will be recorded (confirmed / contested) in the audit's next release.

Note: since v0.3.0 the vocabulary also lets a source declare *neutrality*
in one triple — ex: `sumo:desires odsr:deliberatelyUncommittedOn odsr:FamilyAxis .`
— so 'we take no position' is itself a declarable, queryable outcome.
