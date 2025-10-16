# Peer review - Round 1

Editors:
- Moritz Helmstaedter, Max Planck Institute for Brain Research Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40350.041](https://doi.org/10.7554/eLife.40350.041)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Tetbow: bright multicolor labeling of neuronal circuits with fluorescent proteins and chemical tags" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Moritz Helmstaedter as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor.

Our decision has been reached after consultation between the reviewers.

Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered for publication in eLife at this point. However, if you are able to provide the additional experiments outlined below, we would be willing to consider a revised manuscript. This decision reflects the fact that eLife does not allow reviewers to suggest new experiments that are likely to take longer than 2 months to perform for a revision decision. By instead rejecting these manuscripts, we leave it up to the authors to decide if they think the reviewers are essentially correct, in which case, they may wish to do the requested experiments. If, however, they do not agree with the reviewers, then we would expect authors to send the paper elsewhere. Of course, if you already have the requested experiments in hand, we would be very pleased to have a revised manuscript, incorporating those new data immediately.

Your manuscript reports an approach for bright multicolor labeling of neurons with the goal of deducing neuronal circuitry. While the reviewers see a benefit of this technology over existing techniques, the following points would need to be added to the manuscript to satisfy the consensus concerns of the reviewers (see below for unedited original reviews):

1) While it may seem plausible that an improvement of color distinction and/or brightness of labeling and/or constancy of colors were achieved, a clear application demonstrating the advance over existing techniques is missing. The reviewers suggest either of the following two proof-of-principle reports:

- Quantitative report of long-distance (millimeters) color constancy when labeling axons.

- Automated / efficient reconstruction of single neurons over longer distances, quantification that this reconstruction is performing better with TetBow than with previous techniques.

2) The implications of the technique for circuit reconstruction (connectomics) should be described more cautiously: in local dense networks, the fluorescent labeling of neurons alone does not allow the inference of synaptic connectivity. For long-range labeling, the situation is more benign. We would ask that you amend the text accordingly and discuss this, also in light of the requested proof-of-concept application (see point 1).

Without a proof-of-principle experiment showing clearly the advance of the method over existing technology, the evaluation of the manuscript would be substantially less positive.

Reviewer #1:

The manuscript "Tetbow: bright mutlicolor labeling of neuronal circuits with fluorescent proteins and chemical tags" by Sakaguchi et al. reports the development of a multicolor neuronal labelling toolbox that uses the Tetracyclin-operator system instead of the Cre-loxP system used for the "Brainbow" technology. The main claim of the manuscript is that this different approach increases color variability and provides enhanced color intensity. While an improvement over the "Brainbow" technology for neuron labelling is a relevant endeavour.

I see the following key concerns with the manuscript:

1) The notion of wiring diagram and circuits is mistaken when all that is provided is an intracellular labelling of a presynaptic neuronal population. Wiring diagrams imply synapse detection which this method is currently not providing. This has to be made very clear and care should be taken not to confuse the terminology. Still, intense and long-range labelling of a large number of presynaptic neurons can contribute to circuit analysis and in this sense the method could be valuable.

2) While the manuscript contains many beautiful images, a quantitative documentation of long-range color constancy is missing. In this reviewer's opinion the long-range color constancy is a key prerequisite to use multicolor labelling methods at the light level for circuit inference. While locally the detection of synapses is absolutely required to distinguish an incidental from a synaptic contact, millimeters away from the source neuron, circuit inference can be plausibly done by judging the projection target regions of presynaptic neurons. However, for this the neurons have to stay brightly labelled over millimeters if not centimeters in larger brains. This needs to be documented and quantified for this approach to make a substantial advance.

3) Related to point 2, it would be necessary to show a clear, at least potential improvement in terms of interpretation of such data. Some proof of concept application would be required – at least a hypothetical one. This does not imply that for a methods manuscript a full result has to be documented but at least the notion of what this kind of result could be and why this method in contrast to previous methods will be able to achieve this. Again, I would suggest using the long-range circuit inference as one of these possible key applications.

In summary I think this is an interesting methodological advance that however so far lacks clear quantitative documentation of long-range color constancy. The enhancement of color space is impressive but without a clear application difficult to judge in terms of its impact for neuroscience.

Reviewer #2:

In this article the authors present a useful variation of Brainbow strategy for stochastic multicolor labeling of neurons. Their method, which they called Tetbow, combines the Tet-Off system with the Brainbow approach. They show that they can generate multicolor labeling using plasmids for XFPs or chemical tags as well as with viral tools. These reagents will be a useful addition to the already available recombinase based or transgenic toolkit for multicolor labeling. However, the authors' major claim that the expression levels of FPs using this approach is much higher, therefore this strategy 'should facilitate neuronal circuit reconstruction at higher densities and resolutions' compared to the current -best of class- Brainbow approaches is not supported by the data presented. Labeling many neurons in a brain and labeling individual neurons bright enough for complete reconstructions is a challenging problem. But it is not clear from the data presented that the approach presented in this manuscript solves this problem.

Specific comments:

1) The conditions for induction of the Tet-Off system need to be described in the Materials and methods section.

2) It is not clear from the description why the 0.25µg/µl was chosen for the in utero electroporations. Were multiple concentrations tried? Was the chosen concentration arrived at after examining spread (colors) or by looking at ternary plots as in Figure 2D.

3) Subsection “Image processing and quantification”, subsection “Modeling”, subsection “Imaging data”, include code and data location.

4) Figure 2 panel D – the ternary plot could be separated out for the three conditions for clarity.

5) Figure 1—figure supplement 1 seems unnecessary – addresses a special case of Brainbow.

6) Figure 2—figure supplement 1 and Figure 2—figure supplement 2 can be condensed together; the plasmid cartoons again could be condensed. Similarly, for the other plasmid and vector maps.

7) Figure 2—figure supplement 3 – Brainbow 3.0 experiment is uninformative.

Reviewer #3:

In this manuscript, Sakaguchi et al., present a toolbox for multicolor neuronal labeling termed "Tetbow". Their approach relies on mixing three distinct vectors that express different colors of fluorescent protein (cyan, yellow or red) with the Tet-Off system. Each fluorescent protein gene is under the control of a tetracycline response element (TRE), activated by a transactivator (tTA2) encoded by a fourth vector. The authors show that this strategy enables multicolor labeling of mouse neurons by in utero electroporation, and provide evidence that higher expression and more color contrast can be achieved with Tet-Off transactivation compared with direct expression of the fluorescent proteins from a CAG promoter. They also present a variation of their technique in which protein tags (SNAP, Halo and CLIP) are used to label neurons with combinations of synthetic fluorochromes resistant to tissue clearing procedures. Finally, they present a version of Tetbow based on AAV vectors, which also achieves multicolor labeling of neurons in injected brain areas.

The tools presented in the manuscript may be of interest for the neuroscience community and several convincing images are provided that support their effectiveness. I have however several general concerns about the manuscript:

First, most of the concepts used in the paper are not new. For instance, multicolor labeling with mixtures of vectors expressing distinct XFPs has been introduced several years ago (Weber et al., 2011), as has been the usage of AAV vectors (Cai et al., 2013) or electroporation (Loulier et al., 2014) to achieve multicolor neuronal labeling, and the modeling of the relation between copy number and color combinations (Kobiler et al., 2010).

Second, beyond the images presented in the article, there is no demonstration of a usage of the Tetbow approach to trace connectivity. An application of these strategies to study some aspects of brain circuitry is essential to evaluate their usefulness. In particular it appears uncertain that labeled neuronal processes can be followed in their entirety in neural tissue samples.

Third, due to incomplete description or inappropriate evaluation procedures, the actual improvement brought by Tetbow appears uncertain. For instance, it is unclear if the number of samples analyzed in Figure 1 is sufficient to minimize discrepancies among the different brains analyzed, and between different sections of a given brain. The authors also claim that their scheme is simpler that Brainbow, but in practice this is hardly the case: with Tetbow, a total of 4 plasmids or AAV vectors must be introduced in neurons of interest, while with Brainbow two plasmids (Brainbow et al., 2014) or 2 AAVs (AAV no. 1 and no. 2, Cai et al., 2013) are sufficient. In addition, with Tetbow, careful titration of the different color vectors needs to be performed for each fresh vector preparation, while expression of different XFPs is intrinsically balanced in Brainbow transgenes, making them inherently more reproducible. Concerning the strategy based on protein tags (Figure 5), one cannot assess how deep synthetic fluorochromes labels diffuse within tissue sections: does this scheme really enable to label more than just the first few 10th of micrometers of tissue samples? Finally, are Tetbow protein tags (Figure 5) and AAVs (Figure 6) more efficient in terms of expression level and color contrast than standard vectors? It seems that most cells in Figure 5 and Figure 6 coexpress all three XFPs and that the color contrast in these samples is low.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Tetbow: bright multicolor labeling of neuronal circuits with fluorescent proteins and chemical tags" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

While the reviewers were very positive about the extensive revision, they concluded after extended discussion that they would strongly recommend to address the following remaining issues. These will likely not require an additional consultation with the reviewers after submission of the final revision.

- The text needs substantial revision along the suggestions of reviewers 2 and 3, especially to properly reference the literature and remove ambiguous statements.

- We recommend describing the quality of terminal axonal branch labeling, since this is considered a key benchmark of this set of methods.

Reviewer #1:

This manuscript is a revision of an earlier submission. The authors have taken serious steps to address the issues raised before and have in my view substantially improved the manuscript. The case for Tetbow being a significant step forward for multi-color neuronal labeling has been made more clearly.

In particular, I think the added analyses of color assessment, comparison of fluorescence intensity to Brainbow; and importantly the analysis of color constancy over long distances (Figure 8 and associated supplements) are valuable and relevant.

Reviewer #2:

The revised manuscript, Tetbow: bright mutlicolor labeling of neuronal circuits with fluorescent proteins and chemical tags" by Sakaguchi et al., addresses some of the points raised by the reviewers in the previous submission however, one significant concern remains.

This methods paper adds to the existing toolkit for multicolor labeling of neurons. The tTA-TRE based reagents described in this manuscript appear to have improved brightness over the traditional Brainbow methods. While such a color palette would certainly be useful for answering certain neuroanatomical questions the revised manuscript still fails to address the primary concern that was raised in the original submission – whether such a multicolor labeling approach would be useful for complete neuronal reconstructions. Will the use of multicolor labeling permit reconstruction of entire neurons at higher densities as the authors suggest, i.e. is it an improvement over existing methods that simply use sparse and bright neuronal labeling with a limited color-set.

Figure 8 and Figure 8—figure supplement 2 in this revised submission address this question. The data presented clearly show that the trajectories of the main axon of multiple M/T neurons can be traced. This might be useful if the goal was to identify the primary brain areas targeted by these neurons. But it is not at all clear from the data shown whether complete reconstructions of neurons would be feasible and therefore prompts the question if Tetbow labeling is bright enough to trace axonal arbors in entirety. Reconstructions that aim to trace out only the main axon and the first order collaterals are already possible even in Thy1-GFP transgenic animals (see for instance Guo et al., (2017)). The authors would have definitely compared their traced neurons to the Mitral/Tufted cell reconstructions presented in Igarashi, 2012 or Ghosh, 2011 (both articles are cited in the manuscript). Is it possible to get similar level of completeness using the Tetbow approach?

Reviewer #3:

Sakaguchi et al., present a revised version of their article on the development of an enhanced multicolor neuronal labeling toolbox termed "Tetbow". They have significantly strengthened their study, with the addition of: (1) a theoretical analysis of the color discriminability expected with their labeling scheme; (2) a more precise characterization of the effects of plasmid and AAV concentrations and ratios on color labels; (3) examples of axon tracing over long distances in mitral cells labeled with AAV mixtures. This latter point constituted the main insufficiency of the initial draft of the article, and is addressed in a relatively convincing manner, although an evaluation of the applicability of chemical tags for tracing is still lacking. The tools presented in the manuscript and the efforts made at characterizing optimal labeling conditions will be of interest for the neuroscience community.

My main comment about this new version of the article concerns the presentation of the results, which requires significant revision of the text for the following reasons:

- Several concepts presented in the article are not novel per se and are simply improved and more deeply explored than in the studies that introduced them. The true interest of the article lies in these improvements and optimizations, which will undoubtedly be useful to the community, not in the rediscovery of previous ideas. This is for instance the case of multicolor labeling with mixtures of distinct single-color viral vectors (Chan et al., 2017; Weber et al., 2011) or plasmids (Siddiqi et al., 2014), modeling of the relationship between copy number and color (Kobiler et al., 2010), usage of the Tet-Off system to amplify expression in a multicolor context (Chan et al., 2017 and other studies)…When introducing these concepts, the text should state this explicitly and refer to the related articles. It is with respect to these recent studies that the new tools should be judged, not only relative to former Cre-dependent Brainbow approaches.

- The discussion should also include a section on the drawbacks of Tetbow and possible difficulties of this approach, such as the necessity to carefully titrate the different RGB vectors to equilibrate their concentration, batch-to-batch variations, and whether it is compatible with strategies to sparsen expression e.g. as in Chan et al., 2017.

-Some statements are repeated unnecessarily throughout the paper (e.g. the known fact that Cre recombination is not required for combinatorial labeling).

- Several sentences are quite imprecise, some conclusions are overstated and there are also many typos that need to be corrected.
