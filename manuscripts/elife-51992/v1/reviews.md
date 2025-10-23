# Peer review - Round 1

Editors:
- Anna Akhmanova, Utrecht University Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51992.sa1](https://doi.org/10.7554/eLife.51992.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This carefully executed in vitro reconstitution study resolves some important questions concerning the nature of the cap that stabilizes growing microtubules. The study will be of interest to a broad biological audience interested in cytoskeletal regulation.

Decision letter after peer review:

Thank you for submitting your article "The speed of GTP hydrolysis determines GTP cap size and controls microtubule stability" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Anna Akhmanova as the Senior and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers agreed that this is a rigorously performed study, which addresses important questions about the relationship between the stabilizing cap at growing microtubule ends, the nucleotide state of tubulin and the tubulin state recognized by End Binding proteins. The finding that EB3 specifically recognizes the GTP form of tubulin is an important, though perhaps not entirely surprising contribution to the field. Further, all three reviewers agreed that the description of a gradient of EB binding affinity along the microtubule end is the most novel and interesting part of the paper, but also the part that needs to be worked out better. Specifically, the conformational transition model raised a number of critiques, and these should be addressed by additional experiments and analyses,and possibly also by adjusting the writing of the paper. Since there might be different ways of extending this part of the paper, I include below a summary of the reviewers' discussions and also the full reviews.

The reviewers felt that you should be more clear about what you mean by 'conformation' – do you mean 'expanded/compacted' microtubule lattices, as described by structural work from Nogales lab? Could GTP tubulin exist in either the expanded or the compacted state according to a conformational equilibrium? To begin to address this question, it would be great to get data on whether E254A/D lattices are expanded or compacted. It should be possible to obtain these data without generating a high resolution structure, perhaps by using TPX2 binding experiments or by a 2D cryo-EM analysis.

Further, the conclusions about a conformational gradient are based on a limited set of data, and as, pointed out by the reviewers, alternative explanations of the obtained results are possible. One could consider performing experiments with a monomeric EB3 protein, because they might help to rule out or provide support for the model proposed by reviewer 1. Another idea raised during the consultation between the reviewers was to use as a binding substrate microtubules grown from mixtures of E254A and wild type tubulin at different ratios. Two reviewers questioned the assignment of 'mono exponential' distributions in Figure 4, and this critique should be addressed. Finally, two reviewers found that the split comets deserve some analysis, and the faster growth rate displayed by E254D microtubules requires some attention.

Reviewer #1:

Roostalu et al. have successfully created GTPase-dead and GTP-slow recombinant human tubulin, which is a significant technical breakthrough. They use this new tubulin, along with fluorescent-EB3, to probe the behavior the GTP cap. They make the surprising observation that the dwell time of EB3 molecules changes as you go deeper in the cap. As expected from the Surrey lab, this is a high quality paper addressing a central issue in the microtubule field, namely the role of GTP hydrolysis.

Major comments:

1) The dwell time of EB3 on the microtubule decreases as you move deeper into the cap. The decrease in dwell times is hypothesized to be caused by a gradual "conformational gradient" that reduces EB3 affinity. The visual representation of this idea is the color gradient from red to yellow in the schematic in Figure 4J.

I have an alternative hypothesis for why the dwell times decrease. Consider that EB3 is an "obligatory dimer" (Sen et al., 2013), so its dissociation requires both CH domains to unbind from their respective binding sites. At the very end of the microtubule, EB3 is likely to find two adjacent sites where all of the relevant tubulin dimers are in the GTP state. (The site has 4 dimers, but we can leave aside for the moment the question of their relative relevance.) As you go deeper into the cap, the binding sites will become a mixture of GTP, GDP-Pi, and GDP states. These states have different affinities for EB3. In some cases, a single, high-affinity, GTP site may be adjacent only to GDP sites. In the context of the EB3 dimer, the site mismatch means that one CH domain will bind a GTP site and one can only bind a low-affinity GDP site. EB3 becomes functionally monomeric, hanging on to the microtubule with only one hand. In contrast, EB3 at the very end of the microtubule is holding on with both hands. Note: the EB3 construct they are using appears to be full-length when I trace back through their Materials and methods references.

Can this alternative framework explain the decrease in dwell times with depth inside the cap (Figure 4C)? More specifically: a gradual transition from dimeric to monomeric affinity conditions, driven by the probabilistic availability to two binding sites with different affinities? Are the measurements precise enough to rule out this hypothesis? The visual representation of this idea would NOT be a color gradient but rather an increased "speckling" of red and yellow blocks.

2) I have some technical questions about the "spatially-resolved EB3 dwell time distributions". They divide the microtubules into bins based on distance from the plus-end. The bin size is approximately 0.6 μm for the E254D microtubules (see legend to Figure 4C, see Figure 4—figure supplement 2) and 0.2 μm for the wildtype microtubules (Figure 4—figure supplement 2). These bins are relatively small when you consider that: (1) the microtubule end-position is not determined with sub-pixel accuracy, but is determined rather using the "traced end position" from a manual-tracing of a kymograph, which they state has 0.2 μm accuracy, (2) there is error in the single-molecule localization of the EB3 of 30 nm, and (3) the microtubule is growing at 70 nm/s, which means that an EB3 molecule could start its residence time in one bin and yet end it in another. The first two points make me uncertain whether the molecules are being correctly placed into their bins. The 3rd point is more conceptual: what is the best way to treat a molecule whose bin changes beneath it?

3) How mono-exponential are the spatially-resolved dwell time distributions (Figure 4C)? They appear to start off linear but then deviate from linearity at, e.g., t = 4 s for the 1.47 μm bin.

The central argument of the paper hinges on the fact that Figure 4B is not mono-exponential but Figure 4C is mono-exponential. Are the fits really strong enough to support this? The distributions are described as "strikingly mono-exponential". What does strikingly mean in terms of goodness of fit?

4) The split-comet phenomenon is mentioned briefly, along with their "curved appearance" – but there is very little quantification of the behavior. How often are they observed? How bright are the split comets compared to a full comet, etc.

5) The tubulin that they use retains an internal His tag on the α subunit. That's fine; the Roll-Mecak lab uses similar constructs. The Materials and methods are clear about the retention of the internal His tag but the main text is not. I think it's important to be clear throughout.

A suggestion:

The E254A and E254D microtubules are characterized in terms of their EB3 affinities. Perhaps the authors could explore the binding preference of TPX2, as it would report on the expansion/compaction state of these lattices? Alternatively, in the concluding paragraph, the authors say that high-resolution structures are on the way. But one doesn't necessarily need a 3.4 A structure to answer the most important question: are these lattices expanded or compacted?

Notes on the writing:

– The hypothesis that a nucleotide gradient "might translate into a conformational stability gradient" comes out of nowhere. What motivates this hypothesis? Are there data, structures, kinetic measurements, conceptual arguments, etc, that would motivate this idea?

– The concluding paragraph suggests that the "normal" GTP hydrolysis rate might be under evolutionary pressure. Are there measurements of the GTPase activity with non-human proteins that would provide support for this idea?

Reviewer #2:

This is an interesting and well-executed paper that addresses interesting questions about the microtubule's stabilizing cap, how it relates to nucleotide state, and what is the preferred state that EB proteins recognize. The approach was to purify site-directed recombinant human α/β-tubulins with mutations at a putative GTPase residue. The experiments are performed rigorously and for the most part described clearly, and the work has been done to a high technical standard.

The main findings of the paper are: (i) that abolishing (or at least substantially slowing; E254A) GTPase results in very stable microtubules akin to GMPCPP microtubules, (ii) that moderately slowing (E254D) GTPase results in microtubules with longer EB comets that are also more stable, and (iii) that in these longer comets (and also wild-type comets), there appears to be a gradient of EB binding affinity, with the highest affinity being closest to the growing end. Although it has not been shown directly before using a mutant, I did not find it all surprising that reducing GTPase rate increased microtubule stability, but it is nice to see this in the way that it is shown here. The findings involving EB binding are more interesting: they provide some of the most direct support for the idea of an adaptable microtubule lattice, and they raise questions about what states commonly used GTP analogs are giving.

Major comments:

– I wonder if the balance of the manuscript should change somewhat if to be published in eLife. I think the site-specific EB analysis is probably the most interesting and mechanistic part of the manuscript, and the authors might want to place a little more emphasis there (and place less emphasis on some of the obvious-sounding claims). I don't think new experiments are required, but they may want to go deeper into some of the analysis of the EB binding.

– The authors observe that EB3 does not bind to recombinant GMPCPP microtubules, even though in other ways GMPCPP has been taken to be a good GTP analog. The authors did not mention that GMPCPP generally gives 14 protofilament microtubules. Could the authors commend on whether they think the switch in protofilament number or the different conformation of tubulin (or both) account for the lack of EB3 binding?

– Some of the language suggests there is a 1:1 correspondance between nucleotide state and lattice state, but their results indicate the opposite. I think this should be made more clear.

– It seems E254D microtubules grow ~twice as fast as wild-type. This is unexpected, and the authors really don't say much about it.

– In Figure 4D, the authors fit the EB dwell time decay as a function of distance from the tip. This is what they measured, of course. Since they know the growth rates, is there anything interesting to learn from plotting the decay against time (or just transforming to get the time dependence)? It seems that even speculatively they might be able to get a little more specific about the likely mix of GTP/GDP at different distances from the tip, and/or say something more quantitative about what the GTPase rate must be.

– The spatially resolved EB binding analysis was a strength of the paper for me. I think it also has the potential to be confusing to people, because the language/fits imply a series of discrete 'states' but it seems these states would have to be heterogenous in terms of nucleotide state. A few more sentences about this might be useful.

– The supplemental discussion felt looser than the rest of the paper. In particular, while the authors ascribe various deficiencies to nucleotide analogs, they do not seem to consider the possibility that the mutation(s) they made might also perturb the structure. This criticism applies to the main text also. Some version of the discussion of induced fit should probably be incorporated into the main text.

Reviewer #3:

The study by Roostalu et al. addresses the fundamental question of how GTP-tubulin at the growing tip of a microtubule can be detected by other proteins. The present study examines the binding of the major plus end tip tracking protein, EB3, and its ability to specifically recognize the GTP form of tubulin. In recent years, it has been controversial as to whether tip trackers are recognizing GTP or possibly another nucleotide/conformational state, such as GDP-Pi-tubulin. Here, it is shown, using tubulin mutants that either fail to hydrolyze or hydrolyze slowly, that EB3 specifically recognizes the GTP form of tubulin. This is an important finding for the field, one that is achieved through elegant experimental studies of mutant tubulin and careful quantitative analysis, for which the authors are to be commended. However, in the final analysis, the authors invoke a GDP-Pi intermediate state, without strong evidence to justify it. Rather, it seems possible that a simpler alternative explanation that only assumes GTP and GDP states, as suggested by their data, is not ruled out. Thus, I am concerned that the study, while making an important contribution to the field, may be misleading in its final interpretation.

Major comments:

1) Conclusion of a GDP-Pi state based on non-exponentially distributed dwell times is problematic.

a) Figure 4C. The spatially resolved dwell time is interesting, but the two positions that are farther away from the tip appear that they may be bi-exponential. It seems the non-exponential distribution might be expected as the koff jumps when the hydrolysis occurs, which would give spatially varying dwell times and nonexponential distributions as the hydrolysis can occur at random (Poisson process) during the observation time. So it still seems that the data could be consistent with a simple GTP-GDP model, with no need for an additional third state of GDP-Pi.

b) Figure 4J is unconvincing as the simpler model of only two nucleotide states (GTP and GDP) has not been ruled out. To rule this out it will be necessary to do model-convolution to make it convincing that the analysis method is not yielding spurious results. Even then, the EB binding could be dependent on the local neighborhood of nucleotide state (see Seetapun et al., Figure 2—figure supplement 1 for conformational spread modeling), which seems reasonable since the binding site is at the interface between tubulins. Overall, model-convolution on the microtubule addition-loss-hydrolysis and EB binding-unbinding to assess the model is needed to rule out the simpler GTP-GDP model. Even then the argument for a GDP-Pi state is not compelling.

2) The values for KDs of 8 nM and 40 nM for EB3 binding to GTP- and GDP-tubulin, respectively, seem very strong compared to Seetapun et al. values of 3.8 µM and 55 µM, respectively, in vivo. Why is this, and are the in vitro results informative of the tip tracking in living cells?

3) How big is the cap with wildtype tubulin in vitro? Note: "cap size" is in the title, but it is not estimated, despite a lot of nice quantitation. Previous estimates put it at ~40 in vitro (at 5 µM wildtype tubulin) and ~750 in vivo (Schek et al., 2006; Seetapun et al., 2012), a disparity that is largely explained by the relative disparity in the net growth rates under these two conditions. These papers should be cited, as previous estimates of cap size. (Note: need to account for tubulin concentration, e.g. 19 µM wildtype tubulin in Figure 3J vs. 5 µM in Schek et al. and 7 µM in. Seetapun et al.).
