# Peer review - Round 1

Editors:
- Harel Z Shouval, University of Texas Medical School at Houston United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55714.sa1](https://doi.org/10.7554/eLife.55714.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This is a very ambitious project, that models many of the different molecular interactions that can affect synaptic plasticity. The inclusion of neuromodulators is important, novel and can account for recent data about the role of neuromodulators. The statistical model of AMPA receptors is interesting novel and practical. It is approximation that should be validated experimentally. The authors take seriously the role of data. Due to the models high dimensionality and complexity it is hard to currently validate many assumptions. The significance of this paper is not necessarily the specific assumptions being made, rather it is that many pathway previously ignored are now included, and are shown to significantly contribute.

Decision letter after peer review:

Thank you for submitting your article "A unified computational model for cortical post-synaptic plasticity" for consideration by eLife. Your article has been reviewed by two peer reviewers, including Harel Z Shouval as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is 'in revision at eLife'. Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This is a very ambitious project, that models many of the different molecular interactions that can affect synaptic plasticity. The inclusion of neuromodulators is important and relatively novel. The statistical model of AMPA receptors is interesting, novel and practical. The authors take seriously the role of data. It is quite a heroic effort, but on the other hand the model is hard to verify, it is hard to extract more general principles, and the predictions of the model are limited. This limits the overall impact of the work.

The model is very complex, and almost none of the reaction coefficients are known. There are so many parameter combinations that can yield the same results. What do we actually learn from this? This is an essential part of this model, not much can be done to address this.

Spine model should be used in all simulations of plasticity protocol. It is not clear and how the magnitude of the calcium currents through the NMDAR, and of efflux through diffusion and pumps are calibrated.

It is not clear if all initial conditions are at the fixed points.

The dynamics of the neuromodulators are odd and sometimes unclear. They should be justified, explained better or corrected if these dynamics cannot be justified. Does the application of neuromodulator to the bath on its own change the efficacies?

Essential revisions:

1) All simulations of plasticity protocols should use the spine model, and it should be explained how the NMDA currents in the spine model are calibrated.

2) All simulations should start from a fixed point of the model.

3) The neuromodulator dynamics should be better explained and justified. Does it make sense to have square neuromodulator pulses? What are the neuromodulator dynamics in the STDP experiments? Especially must take into account that in the Seol et al., 2007 paper neuromodulators are bath applied. Does bath application of neuromodulators, alone, without stimulation change the efficacies?

Reviewer #1:

This is a very ambitious project, almost heroic. The attempt is to carry out true quantitative modeling of many of the signal transduction pathways involved in LTP/LTD in neocortex. The work here is very detailed and extensive, and there are many interesting and novel components to this work. However, I am not yet convinced that this goal is feasible. The model is very complex, there is a huge number of unknown parameters and I am not sure that I understand all of the methods and therefore do not know if they are appropriate.

The good:

1) The inclusion of neuromodulators is important and relatively novel.

2) The statistical model of AMPA receptors is interesting novel and practical.

3) The authors take seriously the role of data.

The bad:

1) The model is very complex, and almost none of the reaction coefficients are known. There are so many parameter combinations that can yield the same results. What do we actually learn from this?

2) All simulation of plasticity including LFS and HFS should be carried out on the basis if the spine model in Neuron. It is not clear to me though how that was calibrated.

3) The neuromodulator dynamics, which are pulses for every Ca pulse, are problematic, and not justified. It is unclear to me what the NM dynamics are in the subsection “Paired-pulse stimulus protocol induces PKA- and PKC-dependent spike-timing-dependent plasticity (STDP) in GluR1-GluR2-balanced synapses”

Detailed points – Major:

The good:

4) The inclusion of neuromodulators and their effects on the PKC and PKA pathways is important. Most previous models have ignored these effects, but results in adult neocortical slices have proven that these pathways are essential for LTP and LTD.

Most previous models have ignored the role of the different subunits in the AMPA receptor heteromers. Modeling of these receptors directly as independent species in a mass action approach is nearly impossible due to the huge number of possible combinations. The statistical model proposed is a novel idea that has significant practical advantages. There are assumptions that go into this, which the authors acknowledge. Nevertheless, it is a novel and sensible approach. I think a separate work could simply be based on this model and the statistical testing of its validity.

These authors take seriously the role of data and test the model (with different parameters) against many different experimental results.

The major problems:

5) This is a very complex model with 140 reactions and 47 types of elementary molecules which could be in many states. A tiny fraction of the reaction coefficients have been measured, even if they have it might not be relevant for in vivo conditions. The determination of these coefficients in the paper does not seem to depend on measured coefficients, but instead seems to depend on these coefficients being appropriate for matching experimental results. As we know, and as is shown for example in Figure 7, there is a very large space of parameter combinations that can produce very similar experimental results. What do we actually learn from all of this then? This problem is actually made clear in Figure 7, what are the authors trying to clarify in this very complex figure?

6) The real complete model is the one that uses the Calcium transients from a Neuron simulation, subsection “Paired-pulse stimulus protocol induces PKA- and PKC-dependent spike-timing-dependent plasticity (STDP) in GluR1-GluR2-balanced synapses” and Figure 6. Only here there is a possibility that realistic calcium transients are used, and in principle this should have been used from all comparisons to data. Not only STDP protocols have real synapses, HFS and LFS stimuli also use real synapses. However, it is not clear to me how this synapse model was calibrated. Peak Ca influx rate here is much larger than for the other cases, more than an order of magnitude larger than in Figure 3 and much larger than in Figures 4, 5 as well. How was this calibrated? Was this based on the number of NMDAR and this influx through each? If so, what are these numbers? An alternative way of calibrating the spine model is to use estimates of calcium influx from Ca imaging, for example from Sabatini and Svoboda, 2002. A third option is to use whatever works, however then even this elementary component of the model is not based on biophysical realism. Several details and references are given in the subsection “Modelling the Ca2+ inputs and neuromodulatory inputs”, but this is still not clear to me. It would also be useful to see what the spine voltages are and how they affect the Mg block. Why is there more calcium influx at -30 ms vs. only presynaptic stimulation? Is the -30 ms measured from the first or last spike in the 4-spike train? What is it about a spike that occurred 30 ms prior to the presynaptic stimulus that affects calcium influx?

7) Neuromodulator dynamics. It is important that neuromodulators have been included here. However, the assumptions about their dynamics do not make sense to me. In several sections neuromodulators pulses are assumed to follow the Ca pulses? What is the logic here, that stimulation of axons also causes neuromodulator release? This clearly does not seem to match experiments like Seol et al., 2007, where neuromodulators are bath applied and should just be at a constant level. Is there any evidence that in other slice experiments neuromodulators are indeed release at every pulse? What about the culture experiments? It is also not clear to me what is done with neuromodulators in the subsection “Paired-pulse stimulus protocol induces PKA- and PKC-dependent spike-timing-dependent plasticity (STDP) in GluR1-GluR2-balanced synapses”, where Ca transients were taken from the spine model. Here it is clear to me that constant Neuromodulator levels should be used as in the experiment.

8) Are initial conditions steady at steady state for each parameter combination? It is not clear to me if all plasticity simulations are started at the steady levels of the system for the given parameter set? Are they?

Reviewer #2:

1) The authors develop a complicated model of the biochemical pathways underlying LTP and LTD. It is quite a heroic effort, but on the other hand the model is hard to verify, it is hard to extract more general principles, and the predictions of the model are limited. This limits the overall impact of the work.

2) Some of the design decisions are hard to follow.

For instance, why was the CaM activation made steeper?

3) I also did not understand how the model fitting was done by changing initial concentrations (Materials and methods). Changing the reaction rates would be a more conventional way. I wonder how these concentrations develop in the absence of stimulation. Do they stay the same, or do they have to be clamped to certain values? Yet in the subsection “The model flexibly reproduces data from various cortical LTP/LTD experiments” other variables are changed to fit the data (what are 'factors for the protein concentrations'?).

4) The model's complexity make it difficult to understand it's properties. For instance, does CaMKII act as a switch, and is the expression essentially binary (O'Connor and Wang)? Does it fit the observations of Nevian and Sakmann?

5) The STDP curves look odd, with no below baseline LTD for short negative intervals.

6) Does the last sentence of the subsection “High-frequency stimulation causes LTP and low-frequency stimulation causes LTD in GluR1-GluR2-balanced synapses” really imply a causal relation, so that GuR2 endocytosis leads to potentiation or depression? If so, the mechanism was not clear to me.

7) The y-axis labels on the plots are odd. In Figure 2 they put the quantity as the plot label, and the units as axis label. The authors do it correctly on the x-axis.

In other figures other conventions are followed.
