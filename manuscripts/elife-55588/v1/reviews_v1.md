# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55588.sa1](https://doi.org/10.7554/eLife.55588.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The study proposes a compact self-organization model for formation of whisker barrels in the absence of pre-defined centers for the barrels. Further, the authors have come up with a biologically plausible rule for competition and conservation of axonal density.

Decision letter after peer review:

Thank you for submitting your article "Modelling the emergence of whisker barrels" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Bard Ermentrout (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is 'in revision at eLife'. Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This compact paper proposes a self-organization model for formation of whisker barrels. The key idea is that reaction-diffusion dynamics can lead to the observed topology, in the absence of pre-defined centers for the barrels.

Essential revisions:

1) How do the authors obtain 41 pairs of γ values (Results, third paragraph)? Are these parameters or were they inferred from experiments? This must be better motivated.

2) The competition term χi requires renormalization, which seems biologically implausible. The authors may wish to try a form such asXai∇1N−1∑j≠iajwhich does not need renormalization. Several other points about this competition term are unclear as mentioned in the reviewer comments.

3) There should be more exploration of the model: some parameter exploration and sensitivity analysis, and some more predictions.

Reviewer #1:

This compact paper proposes a self-organization model for formation of whisker barrels. The key idea is that reaction-diffusion dynamics can lead to the observed topology, in the absence of pre-defined centers for the barrels.

The model is well presented and the motivation of mathematical choices is mostly clear. It may be worth expanding on the motivation for competition for axonal branching (Equations 3 and 4).

It is a little unclear how the misexpression experiment (Shimogori and Grove, 2005) in Figure 1E was done. The simulation approach and outcome for this section is described very tersely.

The authors also mention another easily modeled experiment, in which capybara brains lack barrels because they are big. It should be a simple matter to do this run.

Overall I feel this study presents an attractive and compact model for the formation of whisker barrels, which has good biological motivation, and does a good job of reducing assumptions and molecular guidance cues.

Reviewer #2:

This is an interesting paper that with a few assumptions shows that an old model for areal formation in cortex is sufficient to quantitatively reproduce the patterns of barrels observed in mouse S1. It would appear from the model that the key is the parameters γij that are presumably (hypothesized) to be assigned at the level of the thalamus. I have a few questions about the paper.

1) Does the same model work with respect to projections from the brain stem (barrelettes) to the thalamus (barreloids)? This would be a good way to check the ideas. Related to this, is it true that the barrelettes (barreloids) precede the development of the barreloids (barrels)? It would seem to be necessary? Or perhaps, starting with a double gradient in the thalamus and cortex and a prepattern in the barelettes, would the correct patterns emerge simultaneously?

2) There seems to be a strong prediction in this concerning the development of the patterns over time. Figure 1C indicates that early on there are large distortions in the shape of the barrels particularly in Figure 1D, E rows. is this known to occur?

3) It seems to me that without the chi, then possible connections plus axons are conserved which is reasonable. But with the necessary competition, there seems to be a flaw in the model if they have to renormalize at each point. If axons make connections should they not be lost from the pool forever (this is the -dci/dt the model). For example, since the gradient has no flux in the original K&E model, there is conservation of the total number of connections and axons of a given type (int ai+ci dx = constant). This principle seems to make sense to me. However, the competition term χi seems to disrupt this. Is there a way to introduce the axonal competition in a way the prevents the unrealistic (or biologically implausible, at least) renormalization at each step? I'd be more comfortable with the model if there were a more physiological way to renormalize. For example, I don’t know if the authors considered something like an additional flux of the form:Xai∇1N−1∑j≠iaj

This makes the axons of type i move away from type j while at the same time enforcing conservation without recourse to some sort of post normalization.

Reviewer #3:

The manuscript studies a theoretical model within the framework of reaction-diffusion equations coupled to signalling gradients to possibly explain the emergence of whisker barrels in the cortex.

1) The model considered by the authors is identical to the one studied by Karbowski and Ermentrout, 2004. The only new features are the extension of the original 1D model to 2D and the addition of an extra term to represent competition in axonal branching.

2) The authors consider 2 guiding fields. What are their explicit spatial profiles? Notice that since these fields essentially guide the emergent pattern and hence their profiles, in relation to the geometry of the 2D domain, are crucial. A different profile would certainly lead to a different pattern. I feel that it is not enough to say '…linear signalling gradients aligned with the anterior-posterior and medial-lateral axes….' since the domain is 2D and of non-rectangular shape.

3) The justification for the introduction of the extra term for competition amongst axons (Equation 3) is missing. Why that form? What is the reasoning for introducing axonal competition? What essential features of the resultant patterns are missed out if this term is absent? Or has a different form? In the Discussion section, the authors mention, without any justification, that the conservation of branch density in each projection is a key requirement for the emergence of barrel patterns. This is totally unclear.

4) Related to the above point, the authors mention that the axonal branch density is bounded by their dynamics. I presume that the integrations on the RHS of Equation 4 are spatial integrals over the domain. Then how come a spatial index survives in the LHS of this equation? How did the authors arrive at this equation? Is there a continuous-time version of this equation (like a conservation law), i.e., one that does not make a reference to the discrete time-stepping dynamics?

5) A typical mathematical modelling study should explore the space of relevant parameters to demonstrate the possible range of behaviours that the model can exhibit. This is usually presented as a phase-diagram. The authors do not explore the parameter space (or the possible spatial profiles of the guiding fields) in their study.

6) Throughout, the authors emphasize the spatial-locality of their mathematical model and conclude 'Hence the simulations demonstrate how a self-organizing system…'. A mathematical model with spatial-locality alone does not imply self-organized dynamics. With a sufficiently large number of spatio-temporal fields (N=42), and the concomitant parameters, and non-autonomous guiding fields, it is possible to reproduce any desired pattern. As such, it is crucial in the mathematical modelling of living systems to delineate the essential requirements from the incidental.
