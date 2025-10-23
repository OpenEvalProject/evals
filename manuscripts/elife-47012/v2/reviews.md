# Peer review - Round 1

Editors:
- Stephanie Palmer, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.47012.sa1](https://doi.org/10.7554/eLife.47012.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper provides a bridge between traditional phenomenological models of neuronal spiking and more biophysically realistic models, by supplying a method to infer excitatory and inhibitory conductances directly from spiking data. This manuscript describes this new model, a conductance-based encoding model (CBEM), and adds a crucial stage in testing this type of biophysical modeling by direct comparison with intracellular data. The CBEM model is validated with spiking and conductance data measured in retinal ganglion cells. Excitatory and inhibitory conductances in both midget and parasol cells from the primate retina can be inferred reliably. The method has potential applications to other cell types beyond the retina and can provide more mechanistic insights into what drives spiking in the brain.

Decision letter after peer review:

Thank you for submitting your work entitled "Inferring synaptic inputs from spikes with a conductance-based neural encoding model" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

All reviewers found this to be an interesting new model, and thought it is a useful tool for the computational neuroscience community to have. The manuscript was well-written and clear, but some major concerns about the broader impacts and applicability of the model were raised, as detailed below in the three individual reviews.

Reviewer #1:

This paper provides a bridge between traditional phenomenological LNP models and more biophysically realistic models, by supplying a method to infer excitatory and inhibitory conductances from spiking data. It is a well-reasoned and well-written account of this new model (CBEM) for computational neuroscience. The CBEM model is validated with a comparison to spiking and conductance data measured in retinal ganglion cells, and compares reasonably well to an LN model fit directly to the conductance data.

1) The biggest concern the current manuscript raises is: what important features of RGC encoding does the current model capture that a GLM cannot? Put another way, the new model explains more of the response variance of RGC cells, but what does that extra variance encode about the stimulus? What does this extra fitting power allow one to explain in terms of RGC computation? Can simulations be added that explore what aspects of stimulus encoding the full CBEM captures better than a GLM?

2) For the checkerboard stimuli (Figure 9), the GLM and CBEM models seem to have fairly comparable fits to the data. If these are the more interesting data to fit, how should one interpret the weaker additional explanatory power of the CBEM?

3) Some more discussion of the results of the model simulations of center-surround stimuli is needed. How do the observed spike rates compare to known RGC responses? The full CBEM model clearly makes different predictions about the spiking response to spatially correlated stimuli (particularly the inhibition of the sustained response). What aspects of RGC computation are captured by the full CBEM model compared to the excitation only CBEM or GLM for these kind of stimuli?

4) Some variations (dynamic gain adaptation, cascade nonlinearities) on LN models for RGC data can explain more of the observed spiking response to natural image sequences, but still fail to predict the majority of response variance. Several groups have shown that deep or recurrent neural nets can be fit to retinal data and explain about 30% more of this variance. How does a CBEM compare? It could potentially have a serious advantage over these NN models, both in the number of parameters and in interpretability. The absence of a fit to more complex stimuli, where LN models are known to fail spectacularly, stands out as a large hole in the current manuscript. Of course the points brought up in comment 1 apply here as well.

Reviewer #2:

This paper introduces a new point-process model applied to retinal ganglion cell data, which is based on model components that infer excitatory and inhibitory conductances to predict spikes. It uses a smorgasbord of data to demonstrate difference successes of this model (better performance over linear models, ability to explain some aspects of contrast adaptation), and has a number of mathematical derivations and some simulations to demonstrate how it works.

Overall, it is a mixture of what appears to be solid methods with some interesting results from combining them. However, I found this paper scattered, flipping between mathematical derivations, modeling results, and findings specific to the retina. This has the effect of not clearly tying down any element convincingly, nor clearly demonstrating novelty – or at least the need for the advances suggested in this paper.

1) If main purpose is to demonstrate a better way to model neurons (or perhaps just retinal ganglion cells), one would want to understand its generality, as well as how it compares to models of similar ilk, particularly phenomenological models of excitation/inhibition such as the Butts, 2011, 2016. There is a lot of overhead in computing the integration-properties of this model, and not clear what is gained over a more phenomenological LNLN cascade model. I see that it is possible there could be a lot to be gained from the CBEM, but the current manuscript does not make this clear.

Furthermore, what is the scope of this model. Do the authors expect this to be a more generally applicable method, or simply a means to model retinal ganglion cell responses? Under what conditions?

2) Relatedly, one wonders how important it is to model the conductances explicitly, versus membrane potential. Comparisons to membrane potential has been explored in several previous modeling approaches requiring only LN modeling (since there will not be two separate terms), including work of Priebe (Mohanty, 2012) in V1 and Demb (Zaghloul, 2005) in retina. More could be said about motivation for wanting to infer conductances past fitting data better. If the motivation is simply to fit data better, see #1 above.

3) The ability to explain adaptation to contrast as total-conductance changes seems interesting, but is only presented to the level of validating the model, and not explored. It is thus difficult to evaluate based on the extensive literature studying this in the retina.

4) Relatedly, the Cui et al., 2016 paper that was cited in this manuscript also posits excitation and inhibition, models recorded synaptic currents and spikes, and offers an explanation for contrast adaptation, but with a different model form. It seems worth more of a discussion here commenting on it. Could their proposed model explain these results? (and/or vice versa). Can one distinguish between their proposed circuit (presynaptic inhibition being dominant) and normal inhibition proposed here? Likewise, although not matching in content as much, Ozuysal and Baccus also model intracellular recordings and contrast adaptation, using yet another model form.

5) The derivations in the subsection “Background: Poisson GLM with spike history”, motivating the modeling, do not make a clear argument that the model goes beyond the phenomenological, given its overly restrictive assumptions (e.g., that E=-I). As soon as the GLM-based biophysical model is derived making explicit assumptions, it seems to say that these assumptions do not hold and defines the CBEM without them. Later data in the paper (and in previous papers) seem to invalidate these assumptions as well. If these assumptions do not hold, what is the purpose of deriving the model in this context?

6) It was very unclear the components of the various models and how they are fit to data, and I could not make sense until poring through the Materials and methods section. This was in part complicated by the use of different models in different figures (fit to different experiments), without a clear overarching structure. It might also be useful to compare and contrast the derived model forms to simpler phenomenological models of excitation/inhibition (see #1 above).

7) The subsection “Capturing spike responses to spatially varying stimuli” based on simulation had very confusing motivation and conclusions, and could be much better fit into the logical structure of the rest of the paper.

Reviewer #3:

The manuscript by Latimer et al., proposes a new model for analyzing single neurons under sensory stimulation. The model framework, here termed conductance-base encoding model (CBEM) is similar in spirit to the widely used generalized linear model (GLM), applying filters to integrate a sensory stimulus and a stochastic process to generate spikes. Also similar to the GLM approach, model parameters can be obtained from experimentally recorded spike trains by a maximum-likelihood approach. A conceptual advance of the CBEM, however, is that the model incorporates separate filters for excitatory and inhibitory inputs and that these inputs are treated as conductance changes of the neuron, providing an additional level of biological realism. The authors validate their approach by analyzing previously published data from parasol retinal ganglion cells recorded in primate retina. They show that the inferred conductances match intracellularly recorded conductances, and they show that their model improves predictions of spike trains to new data as compared to a GLM.

The manuscript presents an interesting and thought-provoking approach. The possibility of inferring features of excitatory and inhibitory input from recorded spike trains may be a great tool for investigating sensory processing. Also, the mathematical connections to the GLM, which are nicely drawn out in the manuscript, provide a good background for understanding how this model framework functions. In the present form, however, one concern is that it remains a bit unclear how directly applicable the model is to other systems or what sort of insights it may provide. I would imagine that a more general discussion of the applicability, limitations, and interpretation of the model, potentially supported by some additional example from data or simulations, would considerably strengthen the manuscript.

Essential revisions:

The successful inference of excitatory and inhibitory inputs is only shown for parasol cells under full-field stimulation. Here, the excitatory and inhibitory filters are nearly inverted with respect to each other, similar to the specific case discussed in the text where the conductance model can be mapped onto a GLM. Therefore, one wonders how the model performs when excitation and inhibition are correlated instead of anti-correlated or when their filters are (nearly) orthogonal to each other. Are correlated components of the inhibition as well recovered as uncorrelated (orthogonal) components, or will there be some bias?

The match of the inferred and measured conductance is impressive and suggests that this should work as a general technique to assess inhibitory input. However, it is not clear to me how the model would treat inhibitory signals that are not direct conductance inputs into the analyzed neuron. In the retina, for example, many circuits are also influenced by presynaptic inhibition, which acts on bipolar cell terminals. Should one expect that such inhibition is captures by the inhibition filter (because it is likely filtered differently than the direct excitatory pathway) or by the excitation filter (because it affects the excitatory conductance)?

Regarding the improvement of response predictions over the GLM, I'm wondering whether the differences in the applied nonlinearities play any role here. While the soft-threshold nonlinearities of the CBEM are backed up nicely by analyses, the exponential nonlinearity of the GLM could create problems in the quantitative predictions, especially for strong activation as is likely the case under full-field stimulation.

To emphasize the significance of the work, maybe the authors could point out more clearly how the method could be used for providing new insight into the investigated neurons. Is there a specific finding regarding the inputs into parasol cells derived from the present analysis that could serve as an example? Or maybe the authors could point out questions where the model framework might provide answers.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Inferring synaptic inputs from spikes with a conductance-based neural encoding model" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

Essential revisions:

The reviews on this version of the manuscript were mixed, with some definite enthusiasm for the inclusion of the new midget cell data, but some remaining skepticism and questions about the presentation and generality of the current results. Several points need to be fully addressed for this manuscript to be accepted:

1) For the section on interpreting the GLM as a conductance-based model, and the biophysical motivation for the paper:

The model is set up to make some mathematical manipulations in order to remove the voltage dependence of the currents. That wasn't super clear on a first or second pass and should be made more accessible to the reader.

Other points to address for clarity and scholarship:a) There exists a common quasi-biophysical interpretation of the GLM, wherein the output of the linear stage is thought of as an approximation of the intracellular input or voltage. This interpretation requires (1) that E and I inputs are thought of as currents and sum linearly. Near threshold, this approximation might be decent for modeling spiking, as the voltage is ~constant. (2) the integration time of the neuron must be short enough that the response is mostly a function of the inputs, not on its own voltage history. With these constraints presumed satisfied, many previous studies over the years have assumed that the generating function of the GLM has a quasi-biophysical basis. Can this more standard derivation/interpretation be addressed in this manuscript? Does the explicit integration in the "biophysical" GLM detailed in this work (which addresses assumption 2 above) help in fitting neuronal spiking as compared to a standard GLM? No explicit comparisons are made in the manuscript, and should be added.

b) The derivations seem overly long to simply notice that ge(V-Ee) – gi(V-Ei) will have no voltage dependence if ge and gi cancel. This derivation might be difficult to follow for the broad readership of this journal and should be explained more clearly.

c) This should be reorganized so that it doesn't distract from subsequent results. It could be made more clear that the E = -I assumption is made only to connect this to the GLM-like model class, to motivate the model setup, and is relaxed in the subsequent CBEM inference scheme.

2) For the CBEM model setup, justification, and background:a) The GLM derivation is what is used to motivate the CBEM, and excitation and inhibition are rectified (Equation 10 compared with Equation 9). While the motivation for such rectification is that conductances must be non-negative, this seems somewhat misleading. In the retina, rectification of excitation and inhibition (where it exists) often comes from other sources, most notably non-linear synaptic release from bipolar cells (see Schwartz et al., 2012, Turner and Rieke, 2016, and Freeman, 2015), as well as the effect of amacrine cell processing, which often preserve or extend non-linear effects. While conductances cannot be negative (as the authors assert), the rectification in Equation 10 probably has other sources. This issue raises concerns about the motivation for the CBEM and should be addressed and clarified.

b) The model in its current form cannot capture any cell for which either excitation or inhibition is a non-monotonic function of contrast (i.e. any cell with ON-OFF excitation or ON-OFF inhibition). This applies to many other RGC types, and likely most visual neurons downstream in the brain. Please discuss this limitation more fully and argue for the generality of the model. How does this limit the general utility of this approach outside the retina? Can this model be used to infer a larger class of different contrast-response function shapes? That would certainly be impressive, but doesn't appear to be within the reach of the current model.

c) The advances of the CBEM over previous work on models with separate LN components for excitatory and inhibitory inputs needs to be more thoroughly reviewed, placing the CBEM in the context of this work and arguing for its particular advances.

d) Rectification of the inputs (Equation 10) is the basis of the LNLN cascade model used in many papers over the years, starting with the work of Shapley and Victor and Korenberg and Sakai (in 1970s and 80s). It has been explicitly incorporated in likelihood-based models of the retina and LGN in more recent years (Butts et al., 2011) and most recently in (Maheswaranathan et al., 2018). This includes models that explicitly model excitation and inhibition in the retina using nearly equivalent mathematical forms as used in the current manuscript.

The fact that previous models use spike trains to infer excitation and inhibition does seem to detract a bit from the novelty of the CBEM, if the manuscript does not demonstrate why the CBEM's particular form leads to better inference (certainly the validation with intracellular data here is key to drawing these conclusions and is understood as the main innovation in the paper). Answering the following questions would also provide more biological insight into the success of the CBEM: Is the CBEM's ability to match measured excitatory and inhibitory conductances a result of the integration of currents? The rectification of inputs? The difference between conductance and current?

e) What does the restriction that the conductances are non-noisy do to the CBEM in terms of the types of cellular computations it can and cannot reproduce? Are there particular biophysical effects (e.g. stim-dependent spiking noise) that will be missed via this constraint?

3) For a reader interested in applying the method, it will likely be important to get a better feeling for the applicability and interpretability of the data, in particular when no intracellular data are available for comparison.

a) Important questions are, for example, whether the method also works for non-white-noise stimuli and what may be limitations for the applicability of the method, or the interpretation of the obtained filters as corresponding to actual excitatory or inhibitory conductances. If no data are available, simulations and/or thoughtful discussion could help address these concerns.

b) As a specific example, Figure 10 shows that the inhibitory component can capture surround effects, at least for OFF parasol cells. But is it clear that this actually corresponds to inhibition received by the ganglion cell and not a representation of presynaptic inhibition that nonlinearly interacts with excitatory signals? (Presynaptic effects appear to form a major part of the surround in parasol cells, see, e.g., discussion in Turner, Schwartz and Rieke, 2018.)

c) The method currently uses an explicit model and parameters of the output nonlinearity that are obtained from intracellular data. For pure extracellular data, these parameters (or the shape of the nonlinearity) will not be known a priori. How does that affect the model fitting? Can the parameters of the output nonlinearity be included in the fitting procedure?

4) The results concerning contrast adaptation could be shortened or omitted. The CBEM does a bit better than a GLM, but really, both fail at contrast adaptation because one needs to model it explicitly, as has been done in many previous models, including papers cited in this manuscript from the Baccus group.

5) Existing approaches for inferring excitation and inhibition from spike trains are incorrectly labeled in the Introduction as LN modeling, and only briefly mentioned as alternative to the CBEM in the third paragraph of the discussion. This should be corrected, and the CBEM should be presented in this fuller context.

[Editors’ note: further revisions were suggested before acceptance.]

Thank you for resubmitting your work entitled "Inferring synaptic inputs from spikes with a conductance-based neural encoding model" for further consideration at eLife. Your revised article has been favorably evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) To clarify a bit first: The main model comparison that was sought after by the reviewers had the following aim: Explain how the inference of conductances here (i.e. the biophysical basis of the CBEM) is the key ingredient in successfully predicting the E/I values, as opposed to LNLN models, which have more general nonlinearities (as compared to the GLM's). The reviewers agree with you that the goal here is not to outperform other models per se, in terms of fitting performance or whatnot, but to add interpretable knowledge about the underlying biophysics. The prompt, then, from the reviewers is this: show more clearly and directly how the biophysical assumptions in the CBEM are crucial for getting this E/I estimation right, which allows for the proper interpretation of the model results; show that it's not just the fact that the CBEM (like LNLN models) has a more generalized form of nonlinearity built into it. Essentially, that one needs to model the biophysics in this more correct way to get the right interpretation out.

Here's the concern spelled out more explicitly:

If the CBEM is no better (at predicting the E/I inputs to a cell) than other LNLN models that simply have voltage-like, LN approximations of excitatory and inhibitory inputs, this means that the biophysics presented here is somewhat misleading (at least in the sense that it has to do with considering conductances), which is the current basis of the paper.

Additionally, any more-flexible LNLN models (with many subunits) -- now several in the literature – would actually outperform the CBEM because they can include multiple subunits, and model more general nonlinearities.

It is very possible that the more explicit model of the biophysics in the CBEM would do better and its particular structure is therefore an advance – but the manuscript does not show or address this directly.

There were certainly some things said about this in the response to reviewers, and more of that should be entered into the paper as well.

2) You had a question in the response to reviewers about references for the "quasi-biophysical interpretation of the GLM". The Gerstner references are certainly great here, but please also cite (and if appropriate, discuss) Pillow et al., 2004 and 2005 (where the output of the linear term is explicitly treated as a voltage) and perhaps one of the more recent papers comparing GLM fits to intracellular data.

3) Please add a few more lines to the Discussion section outlining why you expect this model to be of broad utility beyond the retina. Specifically: what sorts of heuristics can a future user of the method employ to decide if the model's assumptions are appropriate for their data? Here, just saying a bit more to justify the breadth of the expected applicability of the model would be sufficient.
