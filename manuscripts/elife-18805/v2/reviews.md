# Peer review - Round 1

Editors:
- Jan-Marino Ramirez, Seattle Children's Research Institute and University of Washington , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18805.028](https://doi.org/10.7554/eLife.18805.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Lognormal firing rate distribution reveals prominent fluctuation-driven regime in spinal motor networks" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Jan-Marino Ramirez (Reviewer #1), is a member of our Board of Reviewing Editors and the evaluation has been overseen by Eve Marder as the Senior Editor. The other two reviewers involved in the review of your submission have agreed to reveal their identity: Mark Humphries (Reviewer #2) and Alexander Roxin (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study characterizes the firing rate distribution of neurons within spinal motor networks. The authors have beautifully combined intracellular and large-scale extracellular recordings to reveal the wide-spread existence of "fluctuation-driven" activity in spinal motor networks. These neurons (50% or more) discharge in a "subthreshold" manner. The authors suggest that the existence of these neurons is a strategy to increase stability and sensitivity in the locomotor network. The return map ratio as used here is a metric that has the potential for wide application in a variety of networks. Indeed, the authors nicely discuss their work in the context of a variety of networks. The study elegantly links spiking dynamics to subthreshold activity and therefore shows that the fluctuation-driven versus mean-driven regimes as described in theoretical work appears to be consistent with real networks. The strength of the study is the use of electrophysiology to test a theoretical framework on neuronal dynamics. There are not many studies, specially in spinal circuits that explore this in great detail. Another strength is the use of the turtle model, which allows the characterization of neuronal discharge in a relatively intact animal.

Essential revisions:

1) The manuscript requires serious editorial revisions to more clearly describe the results. This will be critical to make the text more interesting for a general readership.

– The discussion is of broad interest and compares the data obtained in the turtle spinal cord with data obtained in numerous networks. However, the Introduction is too specialized, and does not provide a general perspective. The reader is immediately confronted with the fluctuation/mean-driven regimes, without an explanation why this is interesting in a general context. It is not clear what the authors mean e.g. with networks being in unresponsive quiescence and saturation. A thorough revision of the Introduction is critical. There is a body of literature on "fluctuation-driven regimes in which excitatory and inhibitory inputs are balanced (e.g. van Vreeswijk and Sompolinsky, Science 1996), and recent in-vivo electrophysiology in cortical circuits supports this idea, e.g. Renart et al. Science 2010. The Introduction fails to make this general point, and also fails to discuss how this study is different from the more "traditional way" to study spinal circuits.

As also indicated by one of the reviewers: "The writing obscures the logic of the work".

– The same need for editorial revision applies to the Results section. Careful proof-reading is needed: see e.g. the first paragraph of the Results makes little sense; Figure 3—figure supplement 2 legend; Figure 3 legend confusing the grey and green histograms; and so on. Most seriously: An entire sub-section of the results is missing, explaining and describing Figure 4A-G

Present the data in a logical manner.i) Establish necessary and sufficient conditions for the existence of "fluctuation-driven" regime:a) Is the subthreshold input approximately Gaussian? [Figure 5]b) Do the neurons have supralinear input-output functions in the subthreshold regime? [Figure 3]ii) How often are neurons in the fluctuation-driven regime? [Figure 6]iii) Does the mode of operation (fluctuation- vs mean-driven) depend on E/I balance? [Figure 4]iv) Can the fluctuation-driven regime be detected across the spinal motor networks? [Figure 2]v) Is it stable between animals and behaviors? [Figure 2]vi) How often and how much of the population is in the fluctuation-driven regime? [Figure 7]

2) Following this logic one notes that a key analysis step is missing. Figure 7 uses the duration of time spent in high irregularity (CV2 > CVcrit) to detect the fluctuation-driven regime, as a proxy for the direct measurements of threshold possible in the intracellular data (Figure 6). In some respects, this is their main result – that 50% of the neurons spend more than 50% of their time in this regime. To show that using CV2 can detect this regime, the authors should apply this same analysis of CV2 to their intracellular data: they need to show it is indeed a proxy for the fluctuation-driven regime.

The authors note that there is different irregularity of firing between the intracellular and extracellular recordings (Consequently, it is not possible to specifically validate the CV2 threshold chosen for the extracellular data. Nonetheless, the authors need to show that in principle this CV2 analysis can recover the fluctuation-driven regime in the intracellular data.

3) In the theoretical work on networks, the network state is considered to be stationary. This means that measures of the spiking activity such as firing rate distributions and CVs of inter-spike-intervals represent very long-time averages and, in fact, in a simulation will converge to the theoretical predictions if ever-longer time intervals are used to evaluate them. In short, there is a proper self-consistent network state for which such statistical measures can be estimated. In the case of the present work the activity is highly non-stationary. It seems the authors take advantage of a sort of separation of time scales in that the bursts, which drive the scratching behavior, as shown in Figure 1D and E for example, are long compared to the inter-spike interval within the burst. However, it seems this non-stationarity should introduce additional variability to any measures of spiking or subthreshold activity beyond the effects of a pure ‘fluctuation-driven' or ‘mean-driven' regime. The authors should find a way to better characterize (quantify) this, since it is one of the important messages of the paper.

The theory on fluctuation-driven versus mean-driven network states does not take into account variable or adaptive thresholds. The authors should also discuss how this might affect such states, e.g. make fluctuation-driven more robust, or less robust? Specifically, a strongly variable threshold would create the appearance of a fluctuation-driven regime, even given approximately constant input (because the timing of ISIs then depends on the noise in the threshold, not the noise in the input). To solve this, the authors could perhaps estimate the degree of non-stationarity by estimating the local variance in the threshold within the burst e.g. computing Var(threshold) in overlapping windows of 10 ISIs. In that way, they could determine if there is only strong variation at the start and end of the bursts (as suggested in some of the example figures), and so would little affect their conclusions.

4) Unfortunately, the authors have not differentiated between interneurons and motoneurons. Yet, they talk about the implications for the rhythm-generating network. Without identifying whether these neurons were either interneurons or motoneurons we don't know whether the difference in the mean/fluctuation driven neuron population is explained by the different types of neurons. The authors should discuss this caveat or even better show for a subset of interneurons (identified for example by staining) that the different types of discharge patterns are present among these neurons. From the data presented here, we don't know whether e.g. the spike distribution characterized here is only representative for motoneurons.

5) The Gaussian distribution of synaptic inputs is not directly demonstrated by actually characterizing the distribution of synaptic events, which is a caveat. The authors deduce this from the somatic membrane potential (Vm = RI) which has a Gaussian distribution – and they show that it does [Figure 3 panels E-G; and Figure 3—figure supplement 2]. Given that this is such an important aspect the authors shouldn't show this key result as an inset of panel A of Figure 3—figure supplement 2. This should be a main figure to illustrate that all neurons have an approximately symmetrical distribution of membrane potentials between spikes (as the skewness is close to 0). And the caveat should be clearly stated that the authors did not perform a characterization of synaptic inputs.

6) Similarly hidden is the definition of the threshold, which is another key point. The authors define the threshold at the maximum slope of dVm/Vm when dVm > 0 [Figure 4—figure supplement 1, panel C], but do not explain it well. The authors need to make this clearer.

Also, in Figure 4—figure supplement 1G, the authors show that the threshold increases for increasing firing rate. In Figure 4A on the other hand, the dashed lines seem to indicate that the threshold is constant during the duration of the burst, despite the fact that the firing rate is clearly changing in time. This apparent discrepancy should be addressed.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Lognormal firing rate distribution reveals prominent fluctuation-driven regime in spinal motor networks" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior editor), and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers noted considerable improvement, in both prose and organisation of the content. In terms of the prose, the Introduction now does a much better job of laying out the issues in understanding the dynamical regimes of neuronal networks; and the Discussion nicely links the findings to a range of issues. In particular, with the new results on the physical distribution of the "fluctuating" regime neurons, the Discussion now makes clear the biggest contribution of this study: that we have to think of all neuronal networks, even spinal ones, as acting en masse to generate dynamics, not as a collection of arbitrarily labelled individuals.

The Reviewing editor notes however, there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) Please consider changing the flow of the Abstract:

"When spinal circuits generate rhythmic movements it is important that the neuronal activity remains within stable bounds to avoid saturation and to preserve responsiveness. Here, we simultaneously record from hundreds of neurons in lumbar spinal circuits and establish the neuronal fraction that operates within either a ‘mean-driven’ or a ‘fluctuation-driven’ regime. Fluctuation-driven neurons have a ‘supralinear’ input-output curve, which enhances sensitivity, whereas the mean-driven regime reduces sensitivity. We find…”.

2) Introduction:

The Introduction has greatly improved! I have some minor comments, though:

2a) In "Which is generated by large circuits primarily in the spinal cord…” replace large circuits with "neuronal network". (Recent studies indicate that locomotion is generated by coupled "microcircuits" – hence the term "large circuits" is very misleading). State "in the spinal cord and medulla" too, since you refer to breathing, which is generated in the medulla.

2b) In the Introduction I would also like to see reference and discussion of the concept that different speeds of locomotion seem to be generated by different microcircuits (see studies by El Manira, Fetcho, etc.). And then differentiate your work from this concept by stating that there must also be a control of different intensities… and then go to your concept of a pool of mean-driven neurons, etc.

3) "This view was essentially predicted much earlier in random walk models [Gerstein and Mandelbrot, 1964]". Follow with a statement like: "However, this concept has been forgotten in explaining locomotion. Yet, it has been adapted to explain cortical processing". Please state something along these lines. I believe it is important to emphasize that this paper tries to apply lessons and approaches that are now commonly used in the cortex to better understand locomotion. In other words, the paper should further crystalize the novelty approach for the field of locomotion, and the opportunities by using approaches that are now commonly used for understanding neuronal circuits in areas other than the spinal cord and brainstem.

4) Small typo: third sentence down in subsection "Normally distributed synaptic input": "in fluctuation-driven regime" should be "in the fluctuation-driven regime".

5) Section "Normally distributed synaptic input": the key definition of fluctuation-driven neurons is here – you go on to relate everything else to this RMR-based definition. But, it is not clear; nor is it said anywhere how many neurons are defined as such. Clearer would be: "…and this forms the basis for selecting neurons in our analysis. An RMR close to 0.5 has fluctuation-driven spiking whereas a value close to 1 has mean-driven spiking (Figure 3—figure supplement 1A,B). Therefore, we defined a neuron as fluctuation-driven if its RMR < 0.7; in our sample of intracellular recordings we found x/68 neurons in this regime."

6) Section "Mean Vm across the population is normally distributed". Three issues here:i) You make use of the threshold here; but do not define it until a few pages later. Is this the same definition of threshold? If so, note it here.ii) "The IO-curve has approximately the same non-linearity across all neurons (Figure 3E)". Figure 3E doesn't address the IO-curve; was this meant to refer to the theoretical scheme (i.e. Figure 1)?iii) Is this analysis only for the fluctuation-driven neurons, or all 68 neurons?

7) Section "Neuronal response-function in subthreshold domain is nonlinear". Again: is this analysis for only the fluctuation-driven neurons, or all 68 neurons?

8) Section "CV2 as an indicator of spiking regime". Reported here is no linear correlation between the time spent below threshold, and the mean CV2 of a neuron. This would seem to be an issue with later using CV2 to diagnose regimes in the population recording. A clear explanation of why this is not an issue would be good – I think the authors are saying that the time below threshold need have no linear relationship with CV2, because different neurons, all in the fluctuation-driven regime, will have different relationships between their CV2 and time below threshold (because of their specific AHP behavior, etc.). But still, Figure 2C implies there should be some relationship between CV2 and time-below-threshold.

That is, we should still be able to see the two broad classes of fluctuating/mean-driven neurons. One wonders if the issue is the same as in Figure 3—figure supplement 1F: the data are not particularly suited for linear correlation. In that figure, correlating LTBT versus RMR, a linear correlation is poor because most of the data-points are clustered close to LTBT=1, and so points inside that cluster dominate the correlation, obscuring any relationship over the whole range of LTBT. So presumably LTBT vs CV2 has the same issue. Perhaps try estimating the distribution of RMR (or CV2) values per LTBT bin e.g. for the bin of, say, LTBT in [0.8 0.9], take the median RMR (or CV2) value. That way, you can correlate (or regress) the medians of the distribution per bin, estimating the relationship between the LTBT and the centre of mass of the values of RMR and CV2.

9) Section "Noisy threshold has no effect". It is stated that "not random, but rather due to a gradual inactivation of Na+-channels throughout the burst." How do we know this is the mechanism?

10) Section "Skewness preserved across behaviours". It is stated that "the ipsilateral behaviour had a slightly higher Gini-coefficient". In Figure 9I can only see 2 out of the 5 animals for which the ipsilateral behaviour has a higher Gini coefficient?

11) Figure 4. Two issues:

i) I think the Results text and/or Figure legend needs a simple explanation for how a firing rate output (y-axis) is derived from the ratio of two histograms (Figure 4A) [as some of the details are already in the Methods]. I understand that this is essentially P(spike) transformed into a firing rate?

ii) Define more carefully what you mean by "sub threshold": Figure 4B shows that "sub threshold Vm" far exceeds the threshold (star)! I think you mean that all these neurons are fluctuation-driven neurons, and so spend the majority of their time sub-threshold.

12) Discussion:

"In neuronal networks, spikes are generated in either in the mean- or the…” (omit "in").

13) "An intrinsic property, which is commonly believed to be involved in rhythm-generation, is the pacemaker property that can autonomously generate neuronal bursting in the absence of synaptic input [Brocard et al., 2010]". This paper is a good example. Since the authors also discuss their paper in the context of breathing it would be appropriate to also cite: Ramirez et al. 2011, PMID: 22654176 and Ramirez et al. 2004: Pacemaker neurons and neuronal networks: an integrative view (Curr Opin Neurobiol). The authors may also want to discuss Carroll and Ramirez 2013, a paper which discusses the role of pacemaker neurons, and discharge pattern in respiratory rhythm generation using a population approach as similarly applied here for the locomotor network.
