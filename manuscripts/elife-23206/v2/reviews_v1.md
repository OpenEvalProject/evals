# Peer review - Round 1

Editors:
- K VijayRaghavan, National Centre for Biological Sciences, Tata Institute of Fundamental Research , India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23206.020](https://doi.org/10.7554/eLife.23206.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The role of PDF neurons in setting preferred temperature before dawn in Drosophila" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by K VijayRaghavan as the Senior Editor and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal his identity: Todd Holmes (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This works follows excellent work from the same lab on Drosophila's temperature preference rhythm (TPR), which produces a daily rhythm in body temperature. The fact that ectotherms behaviorally produce such daily rhythms in body temperature suggest that such rhythms are a fundamental adaptation among animals to a rhythmic environment. Previous work had identified the DN2 class of clock neurons as the critical clock node for TPR and implicated DH31 modulation of these neurons through the Pigment Dispersing Factor Receptor PDFR as an important signaling mechanism for the normal switch to cooler preferred temperatures at night. Remarkably, the PDF peptide did not appear to be necessary for this switch but mutants lacking PDF preferred significantly lower temperatures than wild-type flies late at night. The manuscript under consideration investigates the network mechanisms by which PDF sets late night temperature preference. The manuscript provides evidence for a network, consisting of heat sensitive AC neurons modulating the s-LNvs, which form excitatory synapses on the DN2s, that governs late night temperature preference. Establishment of such a network would be a significant contribution to the field.

Essential revisions:

There are several technical issues that dampen our enthusiasm for this study as currently presented. Yet, addressing these concerns would significantly increase the confidence with which several central results could be interpreted and these concerns are addressable.

One major technical concern is the genetic drivers used to differentially express transgenes within the DN2s and s-LNvs for the GRASP and Kir2.1 experiments. Ideally these experiments would employ completely independent GAL4 and LexA drivers, one expressing strongly in the DN2s and the other in the LNvs. Of course, life is never this easy. The GAL4 driver used here for the DN2s (Clk9M-Gal4) is also, unfortunately, expressed in the s-LNvs, thus requiring the need for Pdf-GAL80 to turn-off GAL4/UAS-mediated expression in the s-LNvs. As designed, the experiments in the study essentially require Pdf-GAL80 silencing of UAS expression to be perfectly complete. Unfortunately, there is no evidence that this is true. This leads to serious concerns about the GRASP signal seen this study and the effects of Kir2.1 expression driven by Clk9M-Gal4/Pdf-GAL80, both of which may simply reflect persistent GAL4 expression in the s-LNvs.

DN2/s-LNv GRASP: The authors describe GRASP located in the dorsal protocerebrum that is with a synaptic connection between the s-LNvs and the DN2s. Maximal putative GRASP signal between s-LNvs and DN2s corresponded exactly to the previously established time of maximal spread of the s-LNv dorsal projection. Given the possibility of some GAL4 driven expression in the s-LNvs (i.e., incomplete silencing by Pdf-GAL80), we are worried that the authors are simply visualizing GFP reconstitution in the axoplasm of s-LNvs. How sure are they that Pdf-GAL80 has completely silenced UAS driven spGFP1-10 expression in the s-LNvs? One way to reassure the reader (and the authors) that this isn't the case, is to show a complete lack of GRASP signal outside of the dorsal protocerebrum. It would be very reassuring, for example, to see no GFP fluorescence in the s-LNv cell bodies or the first 1/2 of their dorsal projections. We did not see this possibility addressed clearly in the Results section or the figures.

P2X2: Though the data presented for a physiological connection between s-LNvs and DN2s does support the presence of such a connection, critical negative controls for this experiment are not shown. Though the authors state that preparations in which P2X2 was not driven in the s-LNvs, displayed no responses to ATP, the details of this control were not described and data are not shown. It is critical to show the ATP responses of Clk9M-Gal4/UAS-GCaMP/LexAop-P2X2 flies, using the same LexAop-P2X2 element used in the experimental fly. Unfortunately, leaky P2X2 expression is always a possibility and must be controlled for. We think the authors should show these control experiments to fully control for this important observation.

Kir2.1 inhibition of DN2s: Isn't it possible, given the concern about incomplete silencing of UAS expression by Pdf-GAL80, that this is simply phenocopying Pdf-GAL4/UAS-Kir2.1 because there is enough Kir2.1 expression in the s-LNvs to result in inhibition? This is especially worrisome in this case, as it appears that there are two copies of the Clk9M-Gal4 present in these experimental flies.

AC/s-LNv connection. This would be a major finding with big implications for how temperature input makes its way into the circadian system. It is very nice to see that the GRASP signal between these two neuron types persists even when the more specific AC driver (NP0002-Gal4) is used. GRASP alone is not compelling evidence that the AC neurons form synapses on or modulatory connections with the s-LNvs. The two neurons may simply rest in close apposition (the dorsal protocerebrum is a busy place) or, if there is a connection, the PDF neurons could be modulating the AC neurons. Without evidence for a physiological connection between AC neurons and s-LNvs it is impossible to interpret the GRASP results. We are curious why the authors did not try to confirm the presence of a connection with P2X2, as this technique is used to make the case for the s-LNv to DN2 connection earlier in the paper. Existing sensors are quite likely to be sensitive enough to detect even an inhibitory or modulatory connection between the AC neurons and the s-LNvs.

In summary this is a promising and interesting study that would be significantly strengthened by an increase in technical rigor. Further, we recommend they add citation of a recent publication Barber et al., 2016, Genes & Dev, that supports their use of the pre-synaptic P2X2/post-synaptic GCaMP assay for functional connectivity.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The role of PDF neurons in setting preferred temperature before dawn in Drosophila" for further consideration at eLife. Your revised article has been favorably evaluated by K VijayRaghavan as the Senior Editor and Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

In particular, please see the concerns of reviewer 2, which needs to be well-addressed. Also, are the experiments that you suggest (re reviewer 1's) being done/done. It will not hurt to have them in place too.

Reviewer #1:

The authors have addressed my concern regarding the effectiveness of the Pdf-GAL80 element in the GRASP experiments. The absence of fluorescence in the soma and initial axonal segments of the s-LNvs gives the reader confidence that the GRASP was not attained intracellularly.

The authors have also nicely addressed my technical concerns surrounding the P2X2 experiments uncovering excitatory connections between PDF expressing neurons and the DN2s. This is now a fully controlled experiment that meets the standards in the field.

There is still no direct evidence for a functional serotonergic connection between the AC neurons and the s-LNvs. But I concede that the circumstantial evidence for the modulatory connection is compelling. It's unfortunate that the authors did not push this further (they outline a reasonable set of experiments to do so in their response to the review) as it would have made this very nice study even stronger.

This is a solid contribution to the field that sheds light on the connections mediating temperature preference rhythms in Drosophila, a unique area of field in which the PI continues to make excellent progress.

Reviewer #2:

Overall, I am satisfied with the revised manuscript. However, the authors have not entirely addressed the concern of one of the reviewers about the physiological certainty of the functional connections between the AC neurons and the sLNv. Thus, I think it is in everyone's best interest if the authors revise the tone of their claims to reflect this significant qualification. At present, the language in the text is too assertive in my opinion.
