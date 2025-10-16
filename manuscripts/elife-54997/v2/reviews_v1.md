# Peer review - Round 1

Editors:
- Alexander Borst, Max Planck Institute of Neurobiology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54997.sa1](https://doi.org/10.7554/eLife.54997.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In your paper, you apply Bayesian inference to estimate parameters of multi-compartmental models of cone and cone bipolar cells from 2P-glutamate imaging data. You next use the resulting compartmental models to optimize electrical stimulation of the retina for neuroprosthetics.

As a major advantage of the parameter estimation procedure, the result is not just a singular point in parameter space resulting in an optimal fit, but instead a likelihood distribution showing how well each parameter is constrained by the data. I see this as a significant step forward compared to previous model parameter estimation procedures.

Decision letter after peer review:

Thank you for submitting your article "Bayesian inference for biophysical neuron models enables stimulus optimization for retinal neuroprosthetics" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Alexander Borst as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by John Huguenard as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Adrienne L Fairhall (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

In this paper, Oesterle and colleagues apply Bayesian inference to estimate parameters of multi-compartmental models of cone and cone ON and OFF bipolar cells from light stimulation and 2P-glutamate imaging as well as EM reconstructions. The method employed (Sequential Neural Posterior Estimation) makes use of a mixture density network, which is an approach that sounds very promising for work in this domain. Importantly, the resulting model parameters are not only given as points to result in an optimal fit, but are given as a likelihood distribution showing how well a specific parameter is constrained by the data. I see this as a significant step forward compared to previous model parameter estimation procedures.

The authors then extended the work to model the effects of electrical stimulation in view of building a modeling test bed for electrical retinal prostheses. This required data constraints from electrical stimulation and current recording. Using the model, the authors were able to design stimuli that selectively targeted different bipolar cells. This work stands as a useful general contribution as a method and the authors have done a thorough and careful job in their modeling. The extension to predictions for retinal prostheses demonstrates the power of the approach.

Essential revisions:

1) This is a systematic study, primarily aimed to demonstrate the advantage of Bayesian simulation-based inference (BSI) for estimating the biophysical parameters of compartmental models. While BSI is convincingly demonstrated as a powerful tool for this purpose, it is not clear whether it is superior in any way over the present-day most-popular alternative, the Multiple Objective Optimization (MOO) approach (Drukmann et al., 2007) which is presently used for building data-constrained compartmental modelling for a large variety of neuron types, in hundreds of labs. worldwide, including at the Allen Inst. the Blue Brain projects etc. One key missing aspect in the present study is a systematic comparison (at least in the Discussion) between BSI and MOO methods.

2) Another key missing aspect in this work is the lack of biophysical intuitions emerging from the compartmental models built. Specifically, how does the synaptic input from the cones propagate along the ON and the OFF BP cells' model that we see in Figure 1? We actually do not see any signal (synaptic potential) in this work neither its propagation along the different compartments – from the distal dendrites to soma, to axon. Does voltage attenuate significantly along these BP – compartments or are the modeled cell close to isopotentiality? What is the role of active ion channels during signals propagation in these models? What is the synaptic conductances (between Cone and BP cells) in these models (and what is the justification to use such a complicated model for transmitter release with Ca-dependent pool-release, rather than transient (double exponential?) conductance change as synaptic inputs)? What are the key differences between the ON and OFF compt. models that make them respond differentially to extracellular stimulus? The authors write in the Discussion: "Likely, the different density for some ion channels contributed to the differential response of the two BC types". This is clearly an unsounded claim which needs to be shown and discussed. After all – an important usage of compartmental modelling is to gain insights into the interaction between structure/membrane channels and synaptic/input-output properties of the modeled cells and for calibrating the model against experiments. This key aspect is missing in this work and, therefore, it is impossible for the reader to grasp the underlying mechanisms responsible for the emergent properties of the modeled cells in response to light stimulus.

3) Another query is whether the response of the modeled ON and OFF BP cells will not be very different when they are immersed in actual retina circuit, with electrical field generated also by other cell types (AC, GC) when the retina is electrically-stimulated. This point should be discussed.

4) It is essential to provide the readers with Neuron models of the 3-cell types as well as with the respective data that was used to constrain these models

5) While the paper is generally well written and clear, the model exposition (Section entitled "Inference algorithm") leaves considerable room for improvement; ideally the paper should be self-contained. The presentation is a little confusing with respect to the status of p(θ), the "proposal prior" p ~, the posterior p(θ|x) and the "auxiliary" distribution q (which when equated to the posterior is no longer written as a conditional distribution as it appears in the cost function). It would be good to explain the form of the cost function that is minimized-it looks like it is based on a KL divergence but is a bit unclear of what. This exposition could do a much better job of walking pedagogically through the goal of the algorithm and how the goal is achieved by the variables defined and the cost function. Also, one should shorten this part of the paper and shift many of the figures to Appendices – as it is now standing with 10 figures.

6) It is difficult to find a quantitative reporting of the variation between data from the same cell type. I took the method to be applied to fit distributions over parameters for models accounting for each experimental trace separately; and for the (beautiful!) results in Figures 5 and 6 to be from one example cell, but maybe this is not true. Could this be clarified? Are the distributions of 7 over models that fit all the experimental data for that cell type? If not, it would be good to show the measured responses with an error bar, and show variations between models. Understanding the extent of intercellular variability seems important in the design of isolating stimuli.
