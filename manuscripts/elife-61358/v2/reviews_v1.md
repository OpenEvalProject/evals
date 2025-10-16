# Peer review - Round 1

Editors:
- Ingmar Riedel-Kruse, The University of Arizona United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61358.sa1](https://doi.org/10.7554/eLife.61358.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper represents a step forward in combining quantitative experiments and modeling in order to explain the mechanism behind complex dynamic phenomena in a terms of the underlying molecular and genetic interactions.

Decision letter after peer review:

Thank you for submitting your article "From local resynchronization to global pattern recovery in the zebrafish segmentation clock" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Didier Stainier as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

All three reviewers agreed that this work makes a valuable contribution to the field and should be published with revisions.

The paper presents an elegant yet complex mathematical and computational model for this embryo segment formation that quantitatively reproduces phenotypes observed after pharmacological inhibition of Notch signaling in Zebrafish embryos. The zebrafish segmentation provides an important research paradigm for developmental processes where tissue patterning and growth are tightly coupled. Intriguingly, the model integrates many different parameters at different levels of organization, i.e. from local cell-cell coupling to tissue level parameters, such as shrinking rate of the presomitic mesoderm. The agreement between simulations and experiments is excellent. This multi-scale model allows the authors to make several non-intuitive predictions, which can also guide future experiments.

In particular, the authors find evidence for vortices formed by the synchronizing genetic oscillators under certain conditions, leading to a large-scale and semi-persistence perturbation of the natural traveling-wave front pattern. Understanding such collective patterns is important to properly interpret mutant phenotypes, furthermore, to understand the critical parameter choices required to stably produce the desired outcome under WT conditions. This work will likely help understanding error correction and robustness in many developmental / multicellular contexts.

The reviewers find the paper overall well written and the videos especially helpful to visualize the dynamics. Each of the reviewers has some suggestions that will help to improve this paper further.

The main points summarized are (see full points below):

• The Abstract and Discussions should be sharpened. The authors should re-evaluate how they summarize the main insights of this paper, also to make this message more obviously relevant to researchers in related fields. Some of the writing should be improved to make the paper more accessible especially to non-specialists in the field.

• Overall the paper should be highlighted as a primarily theoretical contribution (with some experimental support) – as otherwise readers will wonder why many suggestive experiments have not been carried out. At various points it is also not directly obvious whether the authors talk about experimental or theoretical results.

• Do the authors have any additional evidence (in their own lab / unpublished by other groups / from the literature) that such vortices actually occur?

• The reason and potential impact on results for some of the model assumptions (simplifications) have not been explicitly addressed, such as changes in segment size, time delays, or the role of left-right communication. And how does the model exactly compare to already published models?

• The authors should evaluate whether additional, more direct insights can be derived from the model (see suggestions). For example, can we more directly understand what accounts for changes in vortex size? Can we quantitatively understand such features in a more direct, intuitive way – beyond "it comes out of a complex simulation"?

Reviewer #1:

The zebrafish segmentation provides an important research paradigm for developmental processes where tissue patterning and growth are tightly coupled. This paper combines quantitative experimental and novel theoretical approaches, which promises quantitative and deeper insights into this system. In particular, the authors find evidence for vortices formed by the synchronizing genetic oscillators under certain conditions, leading to a large-scale and semi-persistence perturbation of the natural traveling-wave front pattern. Understanding such collective patterns is important to properly interpret mutant phenotypes, furthermore, to understand the critical parameter choices required to stably produce the desired outcome under WT conditions. The results are likely of high relevance for understanding error correction and robustness in many developmental / multicellular contexts.

I recommend sharpening some of the discussions, furthermore, to evaluate whether additional, more direct insights can be derived from the model. This provides the opportunity to be more helpful to a wider readership.

Reviewer #2:

In this manuscript a theoretical model for embryo segment formation is presented that quantitatively reproduces phenotypes observed after pharmacological inhibition of Notch signaling in Zebrafish embryos. Intriguingly, the model integrates many different parameters at different levels of organization, i.e. from local cell-cell coupling to tissue level parameters, such as shrinking rate of the presomitic mesoderm. This multi-scale model allows the authors to make several non-intuitive predictions, which can guide future experiments. I see here a great value of this theoretical work.

Points to discuss:

1) I think one point of criticism that likely will be raised is the fact that several (most?) of these predictions are not tested experimentally, also because there is no straightforward way to tune parameters such as tissue growth, cell motility with the specificity needed.

To address this criticism, I would recommend to label and present the work more explicitly as theoretical work and hence I would move the key parts of the theory to the main text, rather than (mis-?) placing these in the Materials and methods section… The theoretical model is a key result that should be presented as such. In addition, I would be explicit about the fact that several predictions are not tested within this paper but rather, this work serves to guide follow up studies, in different systems. I suggest, in order to make this very accessible, to prepare a list of predictions and detail whether or not these have been tested already, it will serve as guide for future experimentation which than refer back to this original theoretical work.

2) One central prediction is the occurrence of vortices (phase vortices) during the re-synchronization process. While, as pointed out, vortices occur in a wide range of oscillatory systems and hence per se not might be diagnostic, the demonstration would obviously be crucial to support the validity of the presented model. Given that the authors of this manuscript have access to refined imaging setup to quantify oscillations in zebrafish embryos, I would have expected a more decisive answer. To state this data should "soon" be available sounds a bit vague (what means soon?), have these vortices be observed after DAPT washout, has it been attempted?

3) Similarly, as indeed phase vortex can arise in many systems and as the authors predict that "these structures [vortices] will form also in mammalian PSM tissue culture systems" the obvious question is whether indeed there is experimental evidence for the presence of vortices during synchronization in mouse embryo re-synchronization experiments, or stem cells systems (mouse/human, gastruloids). In all these, oscillation dynamics have been quantified in real-time. Have the authors reached out to those groups to query the data? I think this would be in the spirit of this work, i.e. make theoretical progress first and then query the experimental data available in the field.

4) The rationale underlying some model assumptions is not evident:

a) for instance, in the case of shrinking PSM, the authors assume that segment size remains constant. To achieve this in their model, they reduce advection speed to compensate for boundary Xa movement. However, experimental evidence has recently been published using Zebrafish embryos providing evidence that while PSM size is reduced, segment size do not remain of constant size but rather, show a scaling behaviour (Simsek et al., 2018). Can the authors address this point in their model to relate to previous findings?

b) In their model, they do not include time-delays for intercellular communication, while stating that these "play important roles in setting the period of collective rhythms and synchronization". How does the exclusion of this key feature affect the conclusions?

Reviewer #3:

The manuscript by Uriu and colleagues addresses the process of resynchronization and segment recovery in somitogenesis in zebrafish embryos. On the one hand, it shows that recovery after early washout of DAPT drives the intermingling of defective and normal segments in zebrafish embryos. On the other hand, it presents an elegant yet complex mathematical and computational model to propose how this intermingling arises. The agreement between simulations and experiments is excellent. The manuscript is very well written, all data is very clear and the conclusions are very well supported. Videos are especially helpful to visualize the dynamics. I believe this is an excellent and elegant work that deserves publication in eLife.

A major comments to improve the manuscript is:

In the simulations, normal segments arise when the most posterior part of the tailbud spontaneously becomes synchronized. It is then when waves propagate from posterior to anterior, symmetrically on left and right sides, without any spiral. If I am correct, it is the geometry of the PSM and tailbud (two cylinders connected by a toroidal shape), together with the gradient of frequencies, what enables that "wave initiation" becomes ultimately localized within the wide region at the posterior end of the tailbud. During intermingling, wave initiation starts at other locations, more locally, within the PSM. I would suggest to discuss on the relevance of the overall geometry of the PSM+tailbud, that involves left-right symmetry, to reach re-synchronization. In the absence of left-right communication (e.g. in simulations where there is only one tubular shape with no toroidal mimicking the tailbud, for instance) I would expect that recovery of normal segmentation would take much longer, if it happens, and intermingling will be affected.
