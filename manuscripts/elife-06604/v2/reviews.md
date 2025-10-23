# Peer review - Round 1

Editors:
- Timothy Behrens, Oxford University , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.06604.007](https://doi.org/10.7554/eLife.06604.007)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Visual processing of informative multipoint correlations arises primarily in V2” for consideration at eLife. Your article has been favorably evaluated by Timothy Behrens (Senior editor and Reviewing editor) and three reviewers, one of whom, Michael Landy, has agreed to share his identity.

The editor and the reviewers discussed their comments before we reached this decision, and the editor has assembled the following comments to help you prepare a revised submission.

The editor and reviewers agree that the finding of neural correlates of multipoint correlations reflects an important advance over your previous behavioural findings and are enthusiastic about the potential publication of this Research Advance.

For example:

This paper takes the previous work of this group on which 2-, 3- and 4-point correlations are visually salient and to which the visual system is sensitive, and shows that some differential responses to these correlations arise first in area V2. As the authors are aware, I'm pretty familiar with this line of work (having reviewed several of the earlier papers in the series). Tying this story to the physiology is certainly a logical and useful next step.

In the current manuscript Yu et al. add to previously published findings that human observes are more sensitive to more informative multi-point correlations in images. Here they provide a candidate for the neural substrate of this sensitivity: supragranular layers of V2. I think the manuscript is an interesting addition to the previous paper.

Overall, this Research Advance is clearly written and nicely complements the founding article by providing neuronal correlates for multipoint correlation stimuli that have theoretical significance and perceptual relevance.

However, there were several questions that the review panel would like addressed before we could consider publication of the study.

During discussion the panel agreed that the most critical issue to address before the paper can be published is the issue of the scaling of the stimuli.

Since receptive fields are larger in V2 and you are adjusting the stimulus to the receptive field size, aren't you effectively presenting two different stimulus ensembles to the V1 and the V2 population, respectively? Could that explain the differential response between V1 and V2? Do you have control data, where you, instead of upscaling the 16x16 patch, simply increased the number of pixels to match the receptive field size? Alternatively, you could drive the V1 population with the upscaled stimuli for the V2 neurons and see whether your results change. If you do not have such data readily to hand, do you have other means of ruling out that the stimulus scaling confounds the results? For example, are there recorded V1 cells whose receptive field completely overlapped with that of a V2 cell? In that case, you would have responses to the same stimulus ensemble, but from two different areas. The review panel agreed that this issue should be rigorously addressed.

If such data do not exist, then the review panel asks you to remove the claim of a distinction between V1 and V2 from the paper since the data does not really support a comparison, and to explicitly mention that V1 and V2 are stimulated with differently scaled stimuli and explain the reasoning behind it.

A related question about the relationship between V1 and V2 coding was also raised:

Figure 2A shows that at least 75% of V1 cells have no selectivity for multipoint correlation stimuli, yet the mean MCDI of all cells is ∼0.05. This implies that V1 has a small population of V1 cells that have an MCDI of 0.2 or more. How do the response properties of these “special” V1 neurons compare to a “typical” V2 neuron? With the current presentation, it's hard to tell whether V2's representation of multipoint correlations is new or enhances a representation already present in a small subpopulation of V1. As such, the first sentence of the Discussion, which says “arises primarily in V2” seems imprecise. This distinction is also relevant to the authors' Discussion hypothesis that higher-order correlation specificity might emerge from a two-stage cascade from V1 to V2.

The reviewers were also concerned about the illusory contour figure:

At present, the connections between higher-order correlations and previously hypothesized roles for V2 seem tenuous and insufficiently detailed to warrant a full figure in the main text.

For example:

The authors use Figure 3 to argue that V2's selectivity to multipoint correlations helps explain its involvement in the detection of illusory contours and the discrimination of figure and ground. I have two comments. First, in panel a, the “even and odd” correlation structure picks out the corners of the black bars. As such, the association of this correlation with the illusory contour is a consequence of the fact that the bars are spaced by the same distance that defined the “even and odd” correlation structure. Can the authors say anything about whether there is an association between the spatial scales of illusory contour detection and the “even and odd” correlation structure? For example, do humans perceive illusory contours over the same length scales that “even and odd” correlation structures are informative for natural images? Has V2 previously been shown to be sensitive to illusory contours on the spatial scale that the authors use in the “even and odd” correlation structure? Second, the “white and black triangle” correlation structure is the only correlation structure that can distinguish between the two stimuli in panel b because it's the only odd-ordered correlation. This is why I earlier alluded to the point that it would have been helpful to include an uninformative third-order correlation stimulus. Also, in the specific example shown, couldn't one just use the mean (i.e. a first-order structure) to discriminate between the stimuli? I wonder if there might be a better choice of stimuli for this panel.

The reviewers also had several questions that we believe can be addressed by changes to the manuscript text.

In Hermundstad et al. 2014 the second order stimuli (beta) are more informative than the fourth order stimuli (alpha), which are more informative than the third order stimuli (theta). However, the authors only present data for alpha and theta stimuli (that were less informative in the Hermundstad paper) while not presenting the beta stimuli (that were more informative in the Hermundstad paper). I would like to know whether the authors (i) performed experiments with beta stimuli, (ii) if so why they did not report them, or (iii) why they did not consider them. I am sure the authors had a good reason which should be mentioned in the paper.

It would be nice if you could mention more explicitly how the rank order of the MCDI relate to the sensitivity order found in the psychophysical experiments of the previous paper.

I was interested by the finding that the MCDI was unassociated with mappable receptive fields and would be interested in hearing some thoughts from the authors in their Discussion section.

Can the authors clarify how they determined the p-value threshold in Figure 4D? Since the authors declare significance “if any of these p-values” falls below the FDR threshold, is the Benjamini-Hochberg correction equivalent to a Bonferroni correction? If so, then 40 comparisons would lead to a p-value correction less than that displayed. Or do the authors somehow correct for fact that their temporal smoothing effectively leads to fewer than 40 comparisons?

There were also questions about the underlying assumptions in the model. We understand that these comments pertain equally to the already-published paper, but we nevertheless hope that you will be able to deal with them in a few sentences, which we felt would help the current manuscript.

What justifies the authors to assume the regime of sampling limitation rather than transmission limitation? You write that your results fit into the efficient coding framework if sampling an image is the main limitation. What is the empirical evidence that justifies this assumption as opposed to the transmission limited regime many other studies are based on?

If I understand correctly, the fact that humans/neurons should be more sensitive to more variable features is derived using a linear model with Gaussian input and channel noise. However, the mapping from images to multi-point correlations does not seem to be linear. How do you know that this result still holds in the non-linear case, in particular if the sampling regime is characterized by dominating input noise (which would get nonlinearly transformed)?

How do you justify that more variable features contain more information? In the discrete case, I can see that. However, in the limit of infinitely many images, the multi-point correlations become continuous. In that case I could transform all features by a pointwise monotonic transformation (histogram equalization) that would not change the information content but make all features equally variable.
