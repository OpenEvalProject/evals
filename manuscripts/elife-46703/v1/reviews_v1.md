# Peer review - Round 1

Editors:
- Oliver Hobert, Howard Hughes Medical Institute, Columbia University United States

Reviewers:
- John Isaac Murray, University of Pennsylvania United States

## Review text

DOI: [10.7554/eLife.46703.048](https://doi.org/10.7554/eLife.46703.048)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A Myt1 family transcription factor defines neuronal fate by repressing non-neuronal genes" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Marianne Bronner as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: John Murray (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper reports that a member of the Myt1 family of zinc finger transcription factors functions in C. elegans drives neurogenic fate while simultaneously blocking epidermal traits. This finding is exciting because Myt1 is routinely used to induce trans-differentiation of mammalian skin cells into neuroblasts. Remarkably, this work shows that ZTF-11, the sole Myt1 homolog in C. elegans, is also sufficient to transform epidermal precursors into neurons. Moreover, Lee et al. show that ZTF-11 drives an epidermal to neuronal trans-differentiation event that occurs during normal C. elegans development. These findings indicate that ZTF-11/Myt1 function is likely evolutionarily conserved and thus investigations that exploit the experimental tractability of C. elegans can effectively advance our understanding of the mechanism Myt1 function in mammals. The work deploys powerful experimental tools including a clever strategy for a conditional knockout of the ZTF-11/Myt1 locus that monitors an intrinsic GFP signal to detect cell-specific knockdown. In a first for any metazoan, the cell specific and temporal expression of ZTF-11 throughout embryonic development is defined by time-lapse imaging. Genetic methods also place ztf-11 in a transcriptional cascade involving the proneural transcription factor genes lin-22/Hairy and lin-32/Achaete-Scute and demonstrate physical interaction with the conserved MuvB co-repressor complex.

Essential revisions:

Generally, the authors need to be commended for this very rigorous analysis. However, a number of loose ends were identified that the authors should tie up:

1) The ability of ztf-11 to induce neuronal fates in V1-4 (in a lin-32-dependent manner) is a little unexpected given that ztf-11 is a target of lin-32 in V5. The authors need to test whether ztf-11 and lin-32 cross-regulate, i.e. (a) is the ability of ztf-11 to induce neuronal fates in V1-4 accompanied by turning on lin-32 expression and (b) in the V5 lineage, does lin-32 also depend on ztf-11 (feedback loop; in Figure 4Aztf-11 expression appears to commence before lin-32, so the regulation of ztf-11 by lin-32 is perhaps the feedback). This is trivial thing to test and given the genetic lin-32-dependence such feedback almost has to exist.

2) An alternative explanation should be considered for results reported in Figure 6, in which pan neuronal marker gene is fully expressed in embryos homozygous for a ztf-11 null allele. The authors conclude from this result that ztf-11 is not necessary for differentiation of embryonic neurons. The problem with this interpretation is that it overlooks the more likely explanation of a maternal effect. The ztf-11(0) allele used for this experiment is lethal at the first larval stage and therefore must be maintained with a balancer chromosome. Thus, embryos that are homozygous for the ztf-11 null allele will have maternal ztf-11 mRNA that could be sufficient to sustain neuronal fate in the embryo but not for later stages that depend on zygotic expression. The authors should (a) use global ztf-11 RNAi (see Figure 8) to knockdown maternal ztf-11 mRNA in the balanced ztf-11 strain; or alternatively, (b) in which the rescue the ztf-11 null phenotype with a non-complex ztf-11 array (e.g. fosmid), mark the array with a marker that labels P1 descendant (say myo-3), find animals with dorsal/ventral bwm loss (= P2 loss = loss in germline), then score their non-transgenic offspring (larvally arrested animals).

3) While the analysis of several postembryonic neuronal fates is very elegantly and well done, it is quite restricted. Plus, the analysis of neuronal identity in the embryo is not quite up to par to the quality of the analysis of postembryonic fates. The authors’ work hints at an extremely intriguing possibility that is mentioned by the authors but not very well carved out and broadly enough probed: is ztf-11 function in neurogenesis restricted to those cases where the ectoblast from which the neuron is derived already is a somewhat differentiated cell? That's indeed obvious in the Y to PDA transdifferentiation event. But it's also the case of the V cells – which are also polarized differentiated skin cells which essentially "transdifferentiate" to generate things like the postdeirid. In such cases a gene like ztf-11 is apparently required to "wipe out" the non-neuronal state. But is this really true for all postembryonically generated neurons that come from such a differentiated epidermal state? In contrast, in the embryo, neural precursors don't go through such a differentiated state – and indeed ztf-11 does not appear to have much of a role in embryonic neurogenesis. The authors do of course recognize this, but could word this issue more crisply. For example, they say: "these results indicate that ztf-11 is particularly important for neurons that are generated from an established epidermal lineage". "established" is not very clear – they should say that these are cells that have fully differentiated by a number of different criteria.

Anyway, that's potentially the most exciting point of the manuscript but the authors need to take a closer look at this potential dichotomy with a few more markers for embryonic and postembryonic neurons. Specifically:

Postembryonic: are really all neurons that are generated from differentiated ectoblasts affected? Currently the authors only look at V cell descendants and Y cells, using nifty Cre/Lox approaches. I suggest that they use the plain null to assess whether a few other lineages are affected as well. As markers, they could use specific transcription factor reporters that come on in the L1, right after the respective neuron is generated. Either the reporter will be off (i.e. case proven) or it's still on, but then the authors could look at the characteristic speckled morphology of neurons:

– T cell descendant PHC and Q cell descendants with unc-86(ot893) (a mNG tagged allele)

– K descendant DVB with lim-6 fosmid integrant wgIs387 (perhaps oxIs12 will also work, see below)

– G1 descendant RMH with sem-2 fosmid reporter otIs313.

Embryonic (assuming that maternal rescue is not occurring, as discussed above): The authors state that the embryonically generated head neurons cannot be counted well (with a panneuronal marker in an L1-arrested animals). But actually, this can be done quite easily using the Fiji cell-counter plugins. Alternatively, and perhaps more clearly, to provide more insight on how extensive is the role of ztf-11 on embryonically born neurons, the authors should look a little more systematcally in head neurons. I would simply suggest to use the 4 main neurotransmitter systems, assayed with eat-4 (Glu), cho-1 (ACh), oxIs12 (GABA) and cat-1 (aminergic). This covers most neurons. There's probably little need for precise cell ID here because the expectation is that there will be little if any change, i.e. simply a count of reporter-positive neuron in the head of L1-arrested ztf-1 nulls should suffice.

This is all very simple marker analysis which will allow the authors to support the interesting case of a transcription factor that controls a specific type of neurogenic events.
