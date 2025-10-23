# Peer review - Round 1

Editors:
- Sacha B Nelson, https://ror.org/05abbep66 Brandeis University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84333.sa0](https://doi.org/10.7554/eLife.84333.sa0)

The authors use detailed simulations to convincingly demonstrate that the temporal properties of synaptic transmission from retina to thalamus help to prevent short timescale correlations from hijacking the activity-dependent refinement of these circuits. These correlations are shown to be "parasitic" because although they can readily drive neural plasticity, they have little information about visual topography during the relevant period of refinement. This is an important point since it informs our understanding of activity-dependent development of neural circuits. The present study shows that it is not enough to simply posit that "neurons that wire together fire together," since some types of correlated firing are actually detrimental.


---

# Peer review - Round 1

Editors:
- Sacha B Nelson, https://ror.org/05abbep66 Brandeis University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84333.sa1](https://doi.org/10.7554/eLife.84333.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Synaptic and circuit mechanisms prevent detrimentally precise correlation in developing visual system" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Sacha B Nelson as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Andrew King as the Senior Editor. The following individual involved in the review of your submission have agreed to reveal their identity: Matthias H Hennig (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) All of the reviewers felt that the manuscript needed to be revised to improve the clarity of the presentation so that it is more accessible to a non-specialized audience. Please see the individual reviews below.

2) The reviewers felt that the present manuscript failed to provide sufficient insight into how decorrelation was achieved in the simulations. There was confusion about the following interrelated issues:

a) are NMDA receptors in the model simply performing a low-pass filtering operation?

b) what is the precise origin of the high-frequency or "fast" correlations that are being removed?

c) in what sense, more precisely, are these "parasitic?" (the term, if retained, should be better defined, but perhaps it would be better to choose a more neutral term). One of the reviewers suggested that the problem with "referring to precise correlations as parasitic [is that] what is bad or good depends on the needs of the circuit."

d) Is it really correlations over different timescales or simply the magnitude of the correlation at a fixed window--to address this, the correlation over a broader range of different time lags should be computed.

e) Are other factors, such as the heterogeneity of the model neurons or the broad and imprecise connectivity also contributing? The contribution of at least some of these assumed circuit features should be addressed in additional simulations.

3) The paper should propose some experimental predictions of the model.

Reviewer #1 (Recommendations for the authors):

My major suggestion for improvement is to extensively rework the presentation to make it more accessible to non-specialists. Many of the key ideas are referred to throughout the paper but are only explained in the discussion. These need to be explained intuitively much earlier in the paper and then supported by the results of the simulations. In addition, there are many fine points that are difficult for all but the most specialized reader to follow.

Specific suggestions are below.

Title: In keeping with eLife policy, add a reference to "mammalian".

48 "Correlation below such timescales is likely to be damaging as it has the potential to induce synaptic plasticity based on non-informative activation."

This core point needs more explanation when it is introduced as this point will not be immediately obvious to most readers.

50 "the long timescales of development" is ambiguous. I think you mean the longer timescales of correlations present in the developing visual system, as opposed to the developmental timescale of days to weeks (mouse) or weeks to months (human).

51 For more foundational references on this issue, recognized much earlier than 2014, see references contained in Nelson and Sur 1992, https://doi.org/10.1016/0959-4388(92)90184-M

61-62: A key piece of the argument could be made a little more explicitly: Rapid timescale correlations are present due to visual stimulation and for these to accurately drive refinement, the refinement must not have already occurred before eye-opening. Either, the refinement must be gated, or the correlations which would otherwise drive it must have been prevented in some way.

Another point that is unclear here is why these finer timescale correlations are absent from retinal waves, i.e. do not convey information about the retinal position. I'm sure this has a reasonable explanation, but it's not going to be obvious to most readers. (added after reading further: I see part of the explanation is in Figure 5, perhaps it would be helpful to anticipate this result in the introduction-but even here the explanation is in terms of mutual information between wave and synaptic transmission as a function of synaptic transmission properties but does not explain the issue of what is or is not encoded in the waves. I haven't gone back and reviewed the Butts papers, but what most who have read them are likely to remember is that there is some information about topography in the waves, not the precise spatiotemporal point at which this information falls off – e.g. fact given in line 333 probably needs to be given earlier and more frequently and given some more intuitive motivation as to why it is true mechanistically).

If I am not understanding this correctly, that is further evidence that the precise argument here is not completely clear.

102: can you motivate why existing recordings were not sufficient?

139-151: The significance of the fact that the parameter distributions are not multimodal is not clear. It is also unclear how this leads to the conclusion "Thus we conclude that our database is a valid representation"… Is the fact that these models are nearby in parameter space just a validation of the fact that (a) the neurons are compact and (b) a reasonably orthogonal set of channels was chosen? I'm struggling to understand the point.

Figure 1 legend: most of the description in B should probably move to the methods (e.g. which algorithm was used, which Python library etc.).

184-202: because the homeostatic convergence is pretty critical to the endpoint synaptic weights you are looking at, this assumption could probably use a bit more justification and introduction. Even just the basic concept "Instead of setting the synaptic conductance into some specific value…" could be expanded a bit. Remember you are trying to communicate this to general readers rather than just to computational neuroscientists.

211-13: same point: explain for a more general audience why low correlation is unexpected and why it should be sensitive to convergence. Maybe just move this point (the unexpectedness) until after the contrast with 2B-AMPA only results.

293: to visual → to visualize.

Figure 5. This could use some intuitive motivation.

424-426 The definition of parasitic correlations comes very late. Consider using a more neutral term and defining it earlier to help motivate the study.

451-453 Similarly, the explanation of why waves lack short time scale correlation information about topography would benefit most readers if presented earlier.

505 "provide testable predictions" It would be helpful to say here or earlier what these predictions are and explicitly label them as such.

511-563. I do not find this section very helpful. It reads like a historical account of the process of performing the study, not like a discussion of the results.

General: the term "state-of-the-art" is overused.

Reviewer #2 (Recommendations for the authors):

There are my main "big picture" concerns:

1. The notion of correlation timescales (or precision) vs amplitude (or level).

The authors describe their approach for computing correlations on line 202, based on a previous study from the same lab: but the Mexican-hat-like kernel they use (difference of a 20 ms Gaussian and an 80 ms Gaussian) is already setting the timescale of the correlations, hence the only aspect that they compute and vary is the level of the correlation and not the timescale.

To provide any kind of quantification of the timescale of the correlations, the authors need to: a. Consider different timescales of the kernel, including very narrow ones, b. Consider also the correlations as a function of time lag. Note: people use a different word for this, what I mean is the cross-correlation, normalized to -1 and 1 by subtracting the mean and dividing by the standard deviation, where the typical Pearson correlation coefficient would just be the value at zero time lag.

It seems as if the authors are only measuring the correlation amplitude (level) at zero lag, which conveys information only about a single timescale (the one in their fixed kernel), and hence they cannot make claims about the connectivity convergence factor (or anything else) changing correlation timescales if they don't actually look at those correlation timescales. Basically, every measurement of correlation, e.g. Figure 2, 3, 5, etc. currently is about amplitudes at a fixed timescale, not about timescales. I would suggest that the analysis is actually repeated for correlations over different timescales.

(More minor but related comment is: It is also unclear why they need to have the negative part of the kernel, i.e. why a Mexican hat and not just a single Gaussian.)

If they just want to compare their results to those of Colonnese et al. 2017, where the same method of computing correlations is used, that's fine! But then the claims in the paper should be changed, it should be about amplitude or levels of correlations at the fixed timescales being determined by the kernel matching the data, and not about timescales of correlations.

2. The need to use a biophysical model of the thalamus.

The claim that broad and imprecise connectivity (which refers to spatial connectivity) causes correlations over millisecond timescales because of locally homogeneous synaptic currents is unwarranted. Locally homogeneous synaptic currents do not follow from the broad and precise connectivity. They follow if one assumes uniform neuronal properties. The current paper solves this by fitting biophysical thalamic neurons to data and hence generates neuronal diversity. This is an interesting result on its own, but it's an entirely different reason for the differences in synaptic currents than the broadness and precision of connectivity. What would happen if simpler neurons were used but with diverse currents?

If the main result is the presence of NMDA currents and lack of recurrent connectivity, could the same hold if simpler (single compartment, leaky IaF, or even exponential IaF) models were used for the thalamic cells? I see the value in building these databases using real data, but just to ask about synchronization and timescales of activity and plasticity, maybe a single-compartment model is enough?

Related to this: Are precise correlations generated because of the heterogeneous neurons, or because of the levels of convergence? If the claim is the latter, then is it still there for homogeneous neurons? How important is the heterogeneity among the neurons?

Along those lines: I would tone down the statement in line 92. To really claim that the authors should indeed provide evidence that not including all the detail fails to model spike correlations in the developing thalamus. Synchronization can be avoided not just by heterogeneous neurons, but also due to randomness in input drive and balanced excitation-inhibition as is the case of the classical balanced E/I networks (e.g. classical papers by van Vreeswijk and Sompolinsky and many others).

3. This may appear like a minor issue but it's actually pretty important. The authors should reconsider using the word "parasitic" when they refer to detrimental i.e. bad correlations. Parasitic means feeding someone else, but this is not the case here.

4. For the models in Figures 3 and 4, the setup is unclear. How many new neurons were added? How many TRN neurons, how many cortical neurons (or I guess synapses, not neurons)? Was there heterogeneity here?

5. What about cortically generated activity, e.g. H events as described by Siegel and Lohmann 2012? Especially for the model in the last section where external spike trains beyond the LGN input are not modeled.

6. In addition to the Butts papers, they should also discuss and cite: Gjorgjieva et al. PLoS CB 2009 which actually used real retinal waves and compared the STDP vs BTDP rule proposed by Butts 2007 to demonstrate that the timescales of development and plasticity need to be matched (both slow).

Other papers that they should also consider citing:

- Wosniack et al. 2021 eLife presents a similar feedforward model between the thalamus and cortex and proposes a way to decorrelate activity as a function of development.

- An alternative way to decorrelate activity via emerging inhibition is proposed by Chini et al. 2022 eLife and Rahmati et al. Sci Reports 2017.

- Jia et al. Communications Biology 2022 for short-term plasticity in development which could also influence correlations as it changes E/I balance (especially as the authors assume STP to operate at their synapses)

Reviewer #3 (Recommendations for the authors):

My main suggestion is to try to address the question of how NMDA receptors actually prevent parasitic correlations. As mentioned in the public review, perhaps the slow time constant is responsible. If this is the case, then a graded reduction of NMDA conductances (and homeostatic compensation to maintain the average firing rates) should increase their strength. So perhaps the single-cell NMDA/AMPA ratio is related to the strength of parasitic correlations? This could be an experimentally testable prediction of this work. More generally, I would find it useful if testable experimental predictions could be as specific as possible, e.g. effects of blocking (knocking out) NMDARs (subunits).
