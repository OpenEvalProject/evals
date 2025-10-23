# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40919.030](https://doi.org/10.7554/eLife.40919.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The proneural wave in the Drosophila optic lobe is driven by an excitable reaction-diffusion mechanism" for consideration by eLife. Your article has been reviewed by two reviewers and the evaluation has been overseen by Naama Barkai as the Reviewing and Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

It is uniformly agreed that the system is interesting and the theoretical work valid. There are several issues, however, that will need to be addressed.

1) Motivating the study: given that the system was previously studied (Sato paper), it may be necessary to better define why a new model is 'needed', and what new biological insights it can bring to the table. For example, what are the mysteries that are still not understood and can be better explained by a more in-depth quantitative study? This is discussed in Appendix 3 but should be explained also in the main text.

2) Related to point 1, not all statements in Appendix 3 are supported – e.g. the statement that the Sato model is not robust. Also, the new model may not be fundamentally different from the Sato model, but rather extends it: models clearly make useful simplifications. The current work may 'open' some 'black-box' and by this provide deeper insights. This does not reduce the significance of the study. Please address that.

3) The analysis of Appendix 5 is interesting and should be part of the main text. The lack of lateral inhibition in this case presents a key biological insight that distinguishes the present study. The experimental test proposed by reviewer #1 below is therefore important.

4) Please explain all assumptions, interactions and parameters, as requested below.

Finally, please address all comments and suggestions in the detailed reviews below.

Reviewer #1:

This paper describes a model to explain the progression of a wave of differentiation that crosses a neuroepithelium to generate a brain structure in the optic lobes of Drosophila. This type of wave has been described (and modeled) quite extensively, in particular the morphogenetic furrow that patterns the Drosophila eye. In this case, we are dealing with the neurogenic wave that transforms epithelial cells into neural stem cells (neuroblasts) and produces one of the optic lobe structures. In fact, a recent paper had also modeled the same wave of differentiation and this paper is discussed here.

This type of patterning mechanisms is likely to be fairly common in biology and it is thus quite important to understand its fundamental aspects, which means that a comparison with the morphogenetic furrow is important to emphasize the common points and points of divergence. This will therefore be an important paper for physicists and for more theoretically oriented biologists who want to understand the rules of patterning.

This being said, as a biologist, I do not feel completely qualified to comment on the mathematics of the model. Yet, I think that the authors should have made more efforts to make more accessible the aspects of the model in which a biologist might be interested and might want to use for his/her own research. For example, it is quite difficult to find a clear description in one place of all the interactions (positive and negative) between pathway components that are actually used in the model. Figure 2D comes closest to doing so but, as with other parts of the paper, it refers to an appendix that is disconnected from the main text. The authors should therefore explain in much more precise terms the exact interactions and must justify why each arrow exists, and or why some of them (which have also been described as important for the process) have been excluded.

In particular:

- What is the evidence to support Notch promotion of EGFR signaling?

- Why isn't proneural promotion of Dl expression included?

- Is Notch repression of cell fate conversion necessary on top of the Notch inhibition of proneural factors?

- The authors do not even mention the data on JAK/STAT and Hippo affecting proneural wave progression. Why do they ignore this?

Some of these justifications have been relegated to appendices and it would make the paper much more important to the biologists if much of Appendix 3 (and similarly for Appendix 5) were to be part of the main text. The authors must do this.

There are several comparisons with the recent paper from the Sato lab, with assertions that the current model makes more accurate predictions. However, both papers use relatively crude assessments of phenotype: acceleration or retardation of the proneural wave. From the model simulations in Figure 3, the authors show that there are many 'flavors' to proneural acceleration (or retardation), i.e. different parameters can produce similar outcomes. If the authors really want to say their model is more accurate or better, then they should test model predictions appropriately (i.e. look at EGFR activity and Notch and Dl levels, in addition to Dpn and/or L'sc for the experimental conditions detailed in Figure 3. All of this should be quite easy and would add significant validation to the model.

Furthermore, the authors should also explain why their model of proneural wave progression adds to previous similar models of wave progression, in particular the morphogenetic furrow in the eye disc, also in Drosophila. One key feature that is distinct with the proneural wave is the lack of Notch-mediated lateral inhibition. As this was a puzzling question, the explanation that this is due to basal low levels of Notch in the neuroepithelium is very attractive. A prediction of the model (Appendix 5, Figure 1B) is that reducing Notch levels in the neuroepithelium should result in a salt-and-pepper pattern typical of lateral inhibition. This would be a key result that can very easily be tested experimentally by using a neuroepithelial driver to knock down to different extents Notch using RNAi. This would provide a qualitatively different prediction from just acceleration or retardation of the wave and would convince the biologist that the model is useful to address this point.

Reviewer #2:

The presented article proposes a mathematical model for a pro-neural wave in the Drosophila optical lobe as driven by an excitable reaction diffusion mechanism, that explains observed data and predicts a new experiment. The biochemical nature of the wave is due to a complex process, involving interaction of EGFR and Delta-Notch signaling pathways. Their interplay establishes a transition zone, that travels over the tissue and triggers a differentiation wave.

Although a phenomenological model of this process exists, the authors propose a new approach. This is justified as it helps to analyze at greater depth how this biochemical process, with interaction between multiple components, results in the wave. As such the article is an example for how mainly model driven approaches may help refining the view on a developmentally relevant, but poorly understood process.

The structure of the article is well developed. The appendix, in particular for the explanation of traveling front and pulse models, is didactically useful for a readership that has a background in life sciences.

Possible improvements:

In general, the theory is compared to data at a qualitative level. If possible, it would help to develop a more quantitative interface to experiments. For example, Figure 2E discusses a transient activation of notch signaling that is mentioned to also occur in the optic lobe. The model predicts a striking spatial profile, that may be contrasted to a similar profile of data for a few of the genes involved.

Further, Figure 3 shows a comparison of model simulations on a 2D lattice to experiment. One of the striking differences is that the simulation is based on an ordered hexagonal lattice, while data looks like a strongly disordered array. Order may be less important in case of strong effects such as shown in panels A,B,D. It remains unclear however, how the underlying lattice order will affect the more subtle effects shown in the cell state variable for panels C,E,F.

In Appendix 3, the authors explain the concrete realization that H0 is not important to capture the qualitative features of the model. However, in the spirit of the well-developed didactic tone in the preceding appendices, the model might become more transparent to a broader audience, if key features of H0 are further developed. The mathematics is clear, but additional graphics and a brief discussion would help to guide the intuition of this aspect.

The following Appendix 4 presents a valuable in-depth analysis about robustness against fluctuations. However, it is difficult to find a more detailed discussion about choice of parameters presented in Appendix 3—Table 1. Are these parameters chosen in a physiologically relevant regime? What's the effect of changes to the model? For future experimentalists aiming to test this model, it may be good to provide a range of possible parameter values in which the presented features will be valid. For example, is there a microscopic motivation for the choice of the Hill coefficient n = 3?

This is an exciting model, and it would be very helpful for future development if the model could provide additional predictions that are potentially difficult to test using current technology. For example, could the model be used to predict what sets the speed of the wave? This point is not essential to support the major conclusions of the article. But in the interest of theory motivating new experiments, such an addition might be helpful.
