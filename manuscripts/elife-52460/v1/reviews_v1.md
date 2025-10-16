# Peer review - Round 1

Editors:
- Emilio Salinas, Wake Forest School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52460.sa1](https://doi.org/10.7554/eLife.52460.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study combines multi-neuron recordings from two cortical areas, FEF and LIP, with advanced fitting techniques (GLM modeling) to investigate the underlying neuronal dynamics that unfold during a classic memory-based visuomotor task. The approach is notable because it teases apart the contributions of task events, firing history, and functional coupling across neurons to the evoked spiking activity, doing so in a way that is interpretable. The observed neuronal interactions (magnitudes and timescales) are broadly consistent with those proposed by classic theoretical models of persistent activity and working memory, but the data also reveal intriguing differences and similarities between FEF and LIP that should serve to constrain and refine future models of the frontoparietal attentional network.

Decision letter after peer review:

Thank you for submitting your article "Recurrent circuit dynamics underlie persistent activity in the macaque frontoparietal network" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Emilio Salinas as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Albert Compte (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript analyzes single-neuron activity in the FEF and area LIP during the classic memory-guided saccade task. The novelty here lies in the recording of multiple neurons (5-20 per session) from both areas simultaneously, and in the GLM analyses, which are able to tease apart how task events, firing history, and interneuronal coupling determine the spikes fired by each neuron. The results provide a statistical view of the recurrent interactions between and within these two areas that is of relevance to their functional characterization, and to models of recurrent circuits and working memory in general.

All reviewers agreed that this is fantastic data set and that the analysis is interesting and novel. The general concern was that the methods require more thorough validation in order to put the interpretations on a more solid footing. The suggested revisions will require additional analyses, but not additional experiments. The consensus was that they are important for supporting the conclusions (which could change as a result).

Essential revisions:

1) All reviewers identified potential problems with the analysis/interpretation of the results of the GLM procedure, as can be seen in the individual reviews below. However, as detailed by reviewer 2, many of these concerns could be addressed by testing the GLM methods against synthetic data from the very network models that the results seem to support. This would require substantial work, but is in principle straightforward. This sort of analysis, where the model is tested with designed data sets for which the correct answers are known, would substantially strengthen the credibility of the results and their interpretation.

Some important methodological concerns that could be at least partially addressed in this way are the following:

a) It is not entirely clear why the "exceptionally strong coupling" between neurons contributes in such a subtle way to the predictions of neural activity (i.e., they are not needed to accurately replicate the PSTHs).

b) Verifying the shuffling procedure (null hypothesis) for determining the significance of the coupling terms.

c) It is unclear whether the history-dependent kernels only capture intrinsic neuronal properties, as opposed to influences from other neurons that could be equivalent to history effects.

d) How do the results depend on receptive field overlap? In particular, it is possible that the differences between LIP and FEF are the consequence of different overlap patterns in the two areas.

2) The total coupling strength, which is the net result of adding the positive and negative (inhibitory) kernel weights, is used as a summary measure of coupling between neurons. As elaborated by reviewer 1, this is a potentially misleading quantity, as it does not consider the magnitudes of the excitatory and inhibitory components. The analyses should be run also with alternative measures that take this distinction into account.

3) Consideration of differences across neuronal classes; in particular, whether the results are distinctly different for neurons with significant delay period activity, as mentioned by reviewer 2.

4) There is insufficient validation of the model against traditional analysis techniques, such as cross-correlation analyses.

5) There is insufficient description of some of the analytical procedures (see specific comments below).

Reviewer #1:

This work addresses important problems in oculomotor physiology, is sound, clearly described, and contains many interesting nuggets about the FEF-LIP circuitry. Just to mention one of them, the three interaction kernels provide convincing measures of the time constants of these circuits, confirming long-help ideas based on theory and modeling. Other results, such as the stronger interactions across than within areas, are interesting precisely because they do go a bit against the grain.

I only have one substantial comment. Several analyses are based on the total coupling strength, which is the net result of adding the positive and negative (inhibitory) kernel weights. This leads to the conclusion that "coupling in LIP was greater than FEF, suggesting a greater degree of recurrent connectivity in LIP". But the total strength is a crude measure. If the subtraction of excitation and inhibition gives 1 = 20 – 19 net excitation in one area and 2 = 5 – 3 in the other, is it really fair to say that the coupling is stronger in the latter? Clearly not. Stronger nonlinearities are expected for highly balanced circuits in which both excitation and inhibition are stronger. This intuition is missing in the Discussion paragraphs four and five. In that case, identical excitation in both areas but stronger inhibition in FEF than LIP would be perfectly consistent with stronger winner-take-all dynamics in FEF and more tolerance to spatial ambiguity in LIP, in turn consistent with saccade selection in the former and divided attention in the latter.

My suggestion is to quantify the excitatory and inhibitory interactions separately. For instance, by computing the total excitatory coupling on one hand, and the total inhibitory coupling on the other. If both terms and the net result are stronger in LIP than FEF, then that would credibly verify the current conclusion ("greater coupling in LIP than FEF"). But I suspect (from Figure 3B) that the situation is a bit more nuanced. For instance, stronger inhibitory coupling in FEF would be consistent with stronger motor competition and/or narrower visual tuning. Likewise, one could argue that the relevant indicator of stronger or more reliable delay-period activity is not the net coupling (excitation minus inhibition) but the total absolute coupling (i.e., the total summed magnitude of the coupling weights). I think that, in general, consideration of these alternatives beyond the net coupling would provide a broader and more substantial view of the data, and a more nuanced basis for their functional interpretation, without any alterations to the GLM model.

Reviewer #2:

This manuscript provides evidence that recurrent mechanisms in LIP, FEF and between these two areas are engaged during persistent activity in a delayed response task. This is supported by fitting neuronal spiking data simultaneously recorded in these areas with a population encoding model. A GLM fitting procedure estimates parameters for visual and motor dependencies, neuronal history dependence, and coupling kernels between simultaneously recorded neurons. The coupling kernels are reported strong in comparison to history kernels, and contain time scales consistent with excitatory and inhibitory mechanisms typically included in attractor models of working memory.

The manuscript is a valuable and significant contribution to the research on the mechanisms of working memory. For this classic task, a population-level analysis of simultaneous recordings in two cortical areas has not yet been presented, and provides important insights into the relative importance of different mechanisms that have been proposed to support persistent activity: intrinsic mechanisms, local circuit recurrence, and recurrent interactions between areas. The methods applied are aimed at testing this with advanced statistical methods.

My major concerns regarding the conclusions drawn from these analyses are:

1) There is an inconsistency in the manuscript in that, on the one hand, interneuronal couplings do not improve PSTH predictions (Figure 3D) and yet various analyses (Figure 3A, Figure 4C) are interpreted as demonstrating "exceptionally strong coupling", "exceptionally strong recurrent interactions" or that "network dynamics play a more vital role than intrinsic dynamics". If recurrent interactions are removed from an attractor model persistent activity collapses, and PSTHs are profoundly affected. At face value, the findings thus do not seem to represent a direct support of these models. The fact that exceptionally strong couplings do not have an impact in the PSTH should be better explained.

2) I am concerned about the "null hypothesis" in Figure 3A: if trials are shuffled for each neuron before the fit, then neural activity is modeled with spiking data of other neurons obtained in trials with different delay duration, so not aligned to the stimulus and saccade predictors used in the model. Since these events are typically associated with an increase in firing rate, interneuronal couplings will be reduced in this model because of these misalignments. The reading of "strong recurrence" that now emanates from the comparison with this "null hypothesis" might instead result from this misalignment. Maybe a more direct assessment of how strong is the contribution of couplings to the network would be to evaluate what fraction they represent in the sum of all predictor terms in the model.

3) The manuscript emphasizes the role of recurrent interactions in generating persistent activity. However, not all neurons recorded in LIP and FEF show persistent activity in this task. In particular, Figure 2 shows that neurons with robust persistent activity show sustained history kernels, which supposedly affect just a minority of neurons in the database (Figure 4C). Some of the conclusions may change if one considers separately neurons with strong persistent activity from other neurons. For instance, if neurons with persistent activity mostly populate the right cloud of dots in Figure 4C the interpretation of this panel's results would be very different. Example neurons shown in Figure 1 could be explicitly identified in Figure 4C and other panels with individual neuron data. If the question is how persistent activity is generated, then it should be relevant to consider separately neurons with and without persistent activity.

4) The interpretations in the manuscript jump very easily between the statistical description contained in the fitted kernels and biophysical mechanisms, and this should be more carefully considered. Any "temporal integration above and beyond that explained by the external task elements" (Park et al., 2014) and the spike times of the few simultaneously recorded neurons in that session will be attributed to history kernels, which would therefore be inappropriate to attribute to intrinsic cellular mechanisms. In general, authors should be cautious with the possible confusion in using "intrinsic" to refer to the history kernel. The history kernel might include traces of other network dynamics not captured by the few neurons recorded simultaneously in the session.

Importantly, many of these concerns could be directly addressed by analyzing spike trains from a few neurons selected from attractor network simulations (many of which freely available) to verify if their GLM approach is able to extract the biophysically-based parameters of the model, as currently argued. My intuition is that model neurons without any specific intrinsic mechanism with long time course would show a long-lasting history dependence (self excitation) when modeled against the activity of just a handful of their close neighbors. The number of neurons used as predictors, or the similarity of their memory fields, could also conceivably have an impact in the decay time of history and coupling kernels, and thus contribute to possible differences between FEF and LIP in this analysis. These computational models are freely available (for instance https://neuronaldynamics-exercises.readthedocs.io/en/latest/) and the model data can be generated easily and analyzed with the authors' methods.

Reviewer #3:

The paper uses a novel analytical technique to infer functional connectivity among FEF and LIP cells during a memory guided saccade task. The analysis takes a GLM-based approach and fits spike trains of simultaneously recorded FEF and LIP cells as weighted combinations of kernels related to (1) target location, (2) saccade direction, (3) coupling filters modeling interactions among cells and (4) history filter modeling within-neuron autocorrelations. The main conclusions are that FEF and LIP neurons show strong coupling both within and across areas, and that LIP shows stronger coupling and longer intrinsic timescales than FEF.

While the approach is interesting and potentially useful, I am afraid it is not sufficiently justified in the present version of the manuscript. The level of detail provided is simply not sufficient to support the claims based on this novel analysis technique. I see two main problems with the manuscript as it is now:

1) There is insufficient control for potentially differential sampling of neurons in FEF and LIP: Could the apparent stronger coupling in LIP vs. FEF be due to different neural sampling in the two areas? For instance, if the RF of the recorded cells had more overlap in LIP relative to FEF, that may produce stronger apparent coupling in two different ways. Stronger coupling may arise if the model mis-attributes shared stimulus/saccade related activity to the coupling weights. The authors emphasize that their model identified coupling above and beyond any stimulus-related response, but they provide little evidence to substantiate this assertion. Stronger coupling may also arise if the model correctly attributes variance but the neurons are in fact more coupled by virtue of being more functionally similar. In that case, the areal differences are only artefacts of the neurons the authors happened to sample. We need much more thorough analyses of the similarity in RF profiles and temporal response profiles of the recorded cells to rule out a sampling confound.

2) There is insufficient validation of the model against traditional analysis techniques. The field has several traditional, established measures of neural coupling or connectivity, including noise correlations and joint PSTHs or autocorrelograms. The authors dismiss those analyses off hand with little justification except for saying that they do not adequately remove stimulus-evoked activity. But there are actually many ways for them to get around confounds with these methods. Comparing their model results to these traditional analyses is essential to validate their results.

3) There is insufficient description of the analytical procedures:

– How were the neurons combined across recording days? Clearly, the neurons that were simultaneously recorded each day could be fit using the described method. But the authors say that they simultaneously fit the entire data set – including neurons recorded on different days. How precisely did they set this up and how did this affect the results?

– What were the kernels that the authors used in the model fits? How were those kernels selected? What properties must the kernels have to make the model work? Are the conclusions robust over reasonable changes in kernel shape?

– Goodness of fit and model comparisons: The authors should provide a complete description of the type of models they compared.

– Individual monkey results: How many cells were recorded in each monkey? Did the critical results hold in both monkeys?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for re-submitting your article "Recurrent circuit dynamics underlie persistent activity in the macaque frontoparietal network" for consideration by eLife. Your article has been reviewed by two peer reviewers, including Emilio Salinas as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Timothy Behrens as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors have been very responsive to the comments made in the original reviews, and have thoroughly revised the manuscript. The methods are clearer and the conclusions and rationale for the model more robust. Importantly, the GLM approach has now been validated by applying it to simulated data, and the new results are largely consistent with the original intuition provided by the authors.

However, several implementation details that can potentially affect the results were still unclear and require more thorough explanation.

Essential revisions:

1) What exactly is the uncoupled model?

2) How exactly is the shuffling across trials performed?

3) More careful analyses of the activity during fixation and early delay.

4) Clarification of the dependence on overall firing rate (separate from the variations in connectivity).

These points are discussed at length by reviewer 2 below.

Reviewer #2:

The revised manuscript contains significant improvements over the previous version, notably the new computational model data that provides support to the methods applied. However, I still maintain some relevant concerns on the controls required to support the interpretations of their analyses as couplings between neurons. This concerns primarily the shuffle approach and the control of firing rate confounds as detailed below.

1) Related to previous Major concern 1.

I realize that part of the confusion here is that the “uncoupled model” is never fully described. I understood that this was the full fitted model, to which couplings were set to zero. From this model I would expect PSTHs to differ largely from measured PSTHs, if couplings are contributing significantly to the GLM. Instead, I gather from Pillow et al. (2008) that the uncoupled model is a reduced model refitted to the data, and then I understand that the fit may be good even if couplings for the full model are strong contributors to the fit. I urge the authors to explain clearly what their uncoupled model is. In fact, in the current revision this is further confused in the Materials and methods (“Unsurprisingly,…”), where the “uncoupled method” is commented in the middle of the description of the shuffle approach. These two separate controls should be clearly distinguished and specified so the reader understands their separate implications. Now this is very confusing.

2) Related to previous Major concern 2.

I am still not convinced about the shuffle approach on which the "extraordinarily strong coupling" result is based. If I understand it correctly, the structure of the data is as schematically depicted in Decision letter image 1, with simultaneous spike trains recorded (here 10 neurons in 10 lines per panel) for separate trials (here 8 trials in 8 panels), where in each trial the stimulus is presented in different locations (here different colors of the simulus and response shadings) and delay durations are also different from trial to trial. Neurons respond with spiking activity depending on whether the stimulus falls within their receptive field or not.

The GLM for the neuron on the gray background would then model spikes based on its specific stimulus and response events for each different trial, on its previous spikes in the corresponding trial, and on the previous spikes of all other neurons in the corresponding trials. Crucially the spikes for these other same-trial neurons are collected based on the same stimulus location, response and delay duration.If I understand correctly the shuffle condition applied in Figure 3, the GLM now models the gray-background neuron based on its specific stimulus and response events for each different trial and on its previous spikes in the corresponding trial, exactly as before, but now the spikes of other neurons are taken from randomly picked trials. This is represented in the schematic in Decision letter image 2 (notice the first lines of each panel are the same for both schematics). If this is the case, then now the spikes for these other shuffled neurons were not collected based on the same stimulus location, response and delay duration as the modeled neuron. As a result, the consistency of stimulus activation of neuron 9 and neuron 7 shown in Decision letter image 1 (they are both active or inactive in response to stimuli in all trials), and the consistency of the timing of response events, are broken with the shuffle in Decision letter image 2. This will lead to a radical change in the cross-correlations between these two neurons, even if these spike trains were totally independently generated.

I have run this simulation. Data for these spike trains were independently generated for each neuron (so with no coupling between them), only keeping the consistency of stimulus, response and delay within trials. As shown in the histograms in Decision letter image 3, the mean cross-correlations (as a proxy of the couplings obtained with the GLM) were radically affected by the shuffling procedure. This does not demonstrate any functional coupling between the neurons, but the fact that task events that elicited neural responses were misaligned by the shuffling procedure.

In my view, this effect could explain the extraordinary changes in shuffle histograms in Figure 3. To clarify this, the shuffle should be performed only between trials with equal stimulus location and delay duration, or else apply other commonly used resampling procedures to estimate cross- correlations (Fujisawa et al., 2008; Katsuki et al., 2014), such as within-trial jitter correction methods (Amarasingham et al., J Neurophysiol 2012).3) The section on “Interneuronal coupling is dynamic across behavioral epochs” is very confusing and is not really addressing the point that they are formulating. The fact that there are not very marked changes between couplings measured in the fixation and delay periods is taken as evidence of dynamical working memory without much justification. Later on the comparison of early and late delay periods yields stronger couplings as delay progresses. In my view, this attempt to contribute to the debate on dynamic delay activity, or even activity-silent working memory (Stokes et al., 2015) is overambitious and needs more specific analyses (consider for instance possible traces of the stimuli in the couplings after the response period, by comparing in and out conditions in the baseline period where there is no confound of firing rate for in/out conditions, e.g. Spaak et al., SfN 2017 #339.14; Barbosa et al., Biorxiv, 2019, doi:10.1101/763938). Further, in the interpretations of this paragraph it is disclosed that their measure of coupling is confounded by changes in firing rate (“This finding highlights the potential role of nuanced changes in the dynamics of the network rather than an overall increase in population activity”). This should be declared early on, as this confound may affect many of the interpretations. Any interpretations of difference in coupling strengths should be cautious in previously demonstrating no difference in firing rates, or else in applying more stringent rate-correcting methods such as jitter correction (Fujisawa et al., 2008). Currently, the manuscript does not parallel each of the coupling comparisons (FEF-LIP, fixation-delay, etc.) with corresponding comparisons of mean firing rates, or rate-correcting measures, to support these conclusions.

4) The computational model is a nice demonstration of their methods, in particular of the retrieval of the correct time scale of the interactions between neurons (the AMPA and NMDA current time courses). However, in terms of the strengths of the couplings, the model may also be confounded by changes in firing rate. It will be useful to plot the mean firing rate of model neurons as recurrent connectivity is increased. If this mean firing rate is increasing too, then some compensatory change may be introduced to maintain rates constant as recurrent connectivity increases in order to resolve this concern. The stimulus kernels derived from the model in Figure 7D, left panel, do not seem to correspond to the simulation results: stimuli in receptive fields should generate increase in rates, and stimuli outside the receptive field a suppression of rates.

5) Because of the possible rate confound that affects the coupling measure, the manuscript should provide a mean firing rate description of the various areas and task periods, for instance through average PSTHs.
