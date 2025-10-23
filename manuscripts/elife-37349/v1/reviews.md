# Peer review - Round 1

Editors:
- Inna Slutsky, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37349.031](https://doi.org/10.7554/eLife.37349.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Sparse recurrent excitatory connectivity in the microcircuit of the adult mouse and human cortex" for consideration by eLife. Your article has been reviewed by Eve Marder as the Senior Editor, a Reviewing Editor, and three reviewers.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. We understand that this manuscript represents a good deal of work, but also feel that requires significant editorial attention to make it self-consistent and transparent.

Summary:

Seeman et al., have explored visual cortex excitatory connectivity across multiple layers and cell types using acute slices, patch-clamp recordings, 2-photon optogenetic activation, and computer simulations. The authors explore both mouse and human connectivity, although only specifically visual cortex in the rodent, not human. Human tissue was resected from different brain regions of patients with epilepsy or tumours. The authors find that connectivity is higher and short-term depression lower in supragranular layers. The authors also find that connective strength in human tissue is stronger, as previously shown.

The manuscript is well written and the figures are largely quite clear. The novelty of these results lies in the combination of studying several cortical layers simultaneously in mouse as well as human tissue. The authors should address all the major concerns raised by the reviewers by either extending and strengthening the weaker sections or by removing the weakest data, and then fairly and completely discussing the methodology for what remains. We remind you that eLife also publishes Research Advances that would, in principle, allow you to follow this study with one that strengthens the weaker aspects of what is now here, should you wish to remove them, as might be advisable.

Essential revisions:

1) Developing a standardized pipeline for analyzing the synaptic connectivity of the cortex and other brain regions would represent an advance in the field. However, in many places, the authors do not justify their choices for their experimental procedures. How slices are cut may affect connectivity rates. For example, studies in slices from older mice have used an NMDG-based solution, different from the one used in the current study (Jiang et al., 2015) as well as common alternatives including kynurenic acid- and sucrose-based solutions (see, for example, Galaretta and Hestrin, 2002 (2-7 months old); Crandall et al., 2017). When developing this standardized pipeline, what was the justification for adopting the experimental procedures for preparing the mouse and human slices? Were comparisons made among different approaches including comparisons of slice thickness, slice orientation, depth of recording, and so on that may affect connectivity rates? These variables should be assessed before settling on a standardized pipeline. Furthermore, the authors do not include enough experimental detail to enable the reader to evaluate the standardized pipeline and compare it to prior studies (see below).

2) This finding in L6 PCs that connectivity is low is not so strange given the prior literature, e.g. Velez-Fort et al., 2014. The authors genetically target the less connected form of L6 PC and then report that they cannot find many connections, but this is expected when targeting CT L6 neurons. The most rigorous way to address this would probably be to additionally target and record from L6 PCs other than the ones that express Ntsr1. Alternatively, it would be possible to take out all data on L6, because it is presently quite limited anyway.

3) Technically our major concern lies with the composition of the whole-cell recording solution used. The authors use an internal containing 0.3 mM EGTA. Previous work on unitary excitatory output of layer 2/3 pyramidal neurons has demonstrated that this concentration has a major influence on uEPSP amplitude and dynamics in a target specific manner (Rozov et al., 2001) – decreasing use-dependent facilitation. It is possible that the use of EGTA in the internal solution has flattened the disparity between the use-dependent dynamics of in each layer, and also may have implications for comparison across species. This is a major problem that requires addressing.

4) It has been shown that connectivity depends on the pre- and post-synaptic cell type (see, for example, Brown and Hestrin. 2009). However, here the authors are likely mixing synapse types in their analyses. Cre is expressed in more than one cell type in the Ntsr1-Cre line (Chevée et al., 2018, Tasic et al., 2016) and the Tlx3-Cre line (Tasic et a.l, 2017). Layer 2/3 includes more than one cell type (see, for example, Yamashita et al., 2013; Yamashita et al., 2018; Tasic et al., 2016; Tasic et al., 2017). Thus, the connectivity rates and the average synaptic properties shown here may not represent connectivity rates among specific cell types but rather represent mixtures of synapse types within a layer.

5) The machine learning approach is basically a form of advanced template matching that looks for an event with the right properties. But at no stage can we see that the machine-learning algorithm knows exactly where the presynaptic spike is. Detection should explicitly model the fact that the time of the action potential is known, since it would strengthen its performance, in turn affecting estimates.

6) Figure 4EF data set is small, and the resulting connectivity rate in panel F is low compared to the prior literature (e.g. Perin, Berger and Markram, 2011). Either this n should be increased, or maybe simply remove panels E-F?

7) What about bidirectional connections? Both Song, 2005 and Lefort, 2009 make a big deal of those, it would seem strange not to mention them.

8) E.g. albino animals are known to have different connectivity patterns, so if some of these transgenic lines (Materials and methods section, etc.) were created on an albino background, then please discuss. Differences attributed to layers could in reality be due to the transgenic mouse line used.
