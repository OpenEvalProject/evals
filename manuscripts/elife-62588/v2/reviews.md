# Peer review - Round 1

Editors:
- Sacha B Nelson, Brandeis University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62588.sa1](https://doi.org/10.7554/eLife.62588.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Release probability increases towards distal dendrites boosting high-frequency signal transfer" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Sacha B Nelson as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by John Huguenard as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Prior work has established that neuronal sensitivity to released transmitter scales with distance from the axon so as to mitigate limitations of integrating more distal synapses. Here, the authors show for the first time that presynaptic release of glutamate is also "scaled" with distance. This is an important finding that potentially changes how we think about synaptic integration in these well studied hippocampal neurons, but reviewers raise concerns over aspects of the analyses that need to be addressed. Acceptability of the manuscript will be assessed after it is clearer whether or not the reanalysis supports the central claims of the paper.

Title: It is eLife policy that the title should make clear the biological system under investigation. This could be accomplished by including reference to "…the mammalian hippocampus" or at least "hippocampus" or "hippocampal neurons."

Essential revisions:

The full reviews are included below to help clarify the concerns. Each of the concerns raised should be addressed, however many of these require simply textual clarifications. Key additional analyses required are:

1) The reanalysis suggested by reviewer #3.

2) An analysis of baseline noise distributions and of how apparent Ca+ and iGluSnFR "failure" signals vary with the site and intensity of stimulation, coupled to a more detailed quantitative argument as to why spillover affects the latter, but not the former measurements.

Reviewer #1:

The authors use optical quantal analysis and iGluSnFR measurements of glutamate release at CA3-CA1 synapses to convincingly demonstrate a gradient in release probability that favors distal synapses, matching in many respects, the distance-dependent scaling demonstrated postsynaptically by Magee and others. This is an elegant study that reveals a new feature of hippocampal synaptic physiology. Although the net effect is modest (~15%) the authors also use a realistic biophysical model to demonstrate that the observed gradient improves information transfer to CA1 neurons.

Figure 1: why are 1/3 of the synapses in C. missing in D. Were these synapses for which a second response was not clearly visible? Is this presumed due to saturation? Some brief description of the reason for exclusion should be provided.

Reviewer #2:

In this study, Jensen and colleagues use optical imaging of synaptic calcium signals and glutamate release and report that presynaptic release probability increases in CA1 pyramidal cell dendrites where more distal synapses have a higher release probability. These results complement earlier observations on the increase in postsynaptic efficacy in distal dendrites. While the findings presented in this manuscript address a fundamental question in synapse biology and are potentially important, further documentation is needed to ensure validity of these results and realize their full impact.

1) The findings presented here contradict an earlier thorough study by Magee and colleagues that addressed the same question and reached opposite conclusions. I think the authors should discuss this work (Smith et al., 2003) and address the potential discrepancy.

2) It is important to document baseline noise distributions for calcium indicator as well as glutamate probe measurements. It is critical to demonstrate the reliability of success/failure classification in individual recordings. What is the variation in response amplitudes? How do they compare to baseline fluorescence fluctuations in the same trace?

3) As the senior author and colleagues proposed 14 years ago PPR can be release-independent (Volynski et al., 2006) and therefore makes a poor predictor of release probability. Given the authors have near single synapse resolution, it is surprising that they heavily rely on PPR measure for their arguments. While paired pulse stimulation is a good tool to reduce the bias towards potential high Pr synapses, failure analysis (first response success probability) should be more emphasized over paired pulse ratios. It is worrisome that iGluSnFR experiments solely rely on PPR measure. The authors indicate that they cannot detect failures due to spill over contribution to their measurements. Wouldn't spill-over be more of a concern for calcium signals as they rely on NMDA receptors? Given this group's track record in the field, I would have expected more insight into this issue. I think the authors should at least make sure that this is not a simple technical issue (e.g. location and intensity of stimulation etc.).

Reviewer #3:

I am not able to assess the manuscript in its current form, as I have doubts about the extraction of quantal parameters from the fluorescence traces. The description in the methods does not seem to match the examples provided. I suggest re-analysis of the data (not just of the example traces!).

In the Materials and methods, P2 is defined as "the sum of responses to the second stimulus + responses to both stimuli/total number of trials". There are 4 possible outcomes of paired pulse stimulation: double failure (0,0), single responses (1,0 and 0,1) and double responses (1,1). The author's definition sounds like P2 = [(0,1) + (1,1)] / [(0,0) + (1,0) + (0,1) + (1,1)], which makes sense.

Looking at the example traces shown in Figure 1B and Figure 1—figure supplement 1C, however, the given values of P2 correspond to [(1,0) + (0,1) + (1,1)] / [(0,0) + (1,0) + (0,1) + (1,1)], which is actually a different quantity, (P1+P2). The resulting calculated PPRs are thus not correct.

Given the SNR of the (best) examples, it seems very risky to try to distinguish between (1,0) and (1,1). My recommendation would be to define P2 = (0,1) / [(0,0) + (0,1)], which can be reliably extracted. Unfortunately, this requires complete re-analysis of all raw data and may change results and conclusions.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Release probability increases towards distal dendrites boosting high-frequency signal transfer in the rodent hippocampus" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Sacha Nelson as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by John Huguenard as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The authors perform sophisticated optical measurements of spine calcium and extracellular glutamate in hippocampal tissue to investigate synaptic properties on the long apical dendrite of CA pyramidal cells. They report that synapses close to the soma displayed pronounced paired-pulse facilitation and lower release probabilities compared to distal synapses. The correlations of these properties with synaptic location are statistically significant, but very weak, indicating that the major causes of variability are still not understood. Interesting for researchers in the field, exactly the opposite gradient of synaptic properties was recently reported for the basal dendrites of the same cell type.

Summary:

After receiving clarifications of the analysis methods in the initial round of revision, reviewer 3 has raised some additional concerns. Other points raised by reviewers 1 and 2 have been adequately addressed. Specific revisions are suggested below. The full text of review #3 is also included for clarity.

Essential revisions:

1) Reviewer 3 correctly points out that the effect size for the central observation is small. This does not necessarily preclude publication, but this point should be made clearer to the reader both by including the correlation coefficients in the figures and adding consideration of this issue to the Discussion.

2) The analysis of the burst experiments should be revised along the lines suggested below, or these experiments should be removed or the concern raised adequately rebutted.

3) Whether or not the average Pr and facilitation were kept constant for the different modeling scenarios should be clarified. If this is not the case, it will be necessary to revise the modeling portion of the study, or to make a convincing argument as to why this is not required in order to demonstrate the functional significance of the observed trend.

Reviewer #3:

Jensen et al., use calcium- and glutamate-imaging to assess the properties of presynaptic terminals impinging on the dendrites of CA1 pyramidal cells at different distances from the soma. They find a trend towards higher release probabilities and less facilitation at distal synapses. Synapses that are close together (< 40 um) had similar release probabilities. It is reassuring to see a similar distance-dependent decrease of paired-pulse ratios using two very different parameters, single spine calcium and local glutamate (pooled from several synapses). Opposite gradients have been described for synapses on the proximal dendrites of CA1 neurons (Grillo, 2018), which makes this study interesting and controversial. The authors then use a Neuron model to compare synaptic inputs with uniform properties to inputs that reflect the detected trend to higher Pr at distal inputs. Higher frequencies are indeed better transmitted in the model with a gradient in Pr. This seems to be a good way to test the intuition about the impact of the scaling effect, but I have some questions about the simulated scenarios (below).

While the spine calcium imaging experiments are performed with a local stimulation electrode positioned close to each responding spine, the glutamate experiments use a single stimulation electrode position in stratum radiatum, but read-out in different layers. Although GluSnFR expression is punctate, the optical measurements represent bulk extracellular glutamate and not individual synapses. Therefore, the distance from the simulation electrode is likely the key parameter determining max df/f at different positions. The paired pulse ratio is the only parameter that can be extracted from the glu imaging experiments.

1) The discussion of correlations is focused on their p-values (which indicate that the slope of a linear regression is not zero). Biologically more interesting are the correlation coefficients, which indicate (after squaring) that only a small part of the total variability in Pr is determined by synapse position. Correlations with R squared = 0.18 (Figure 1C) or 0.14 (Figure 2A) are considered "very weak", which is not necessarily what you expect given the title of the manuscript. As all data points are shown, readers will form their own opinion and realize that synapse position has only a weak impact on presynaptic properties. Still, I recommend showing the numerical value of r (or r squared) on all panels with linear fits (and relegate "n" to the figure legends).

2) Figure 3C shows strong facilitation at proximal synapses, linear behavior at distal synapses, which the authors take as supporting evidence that Pr is higher at distal synapses. However, the first pulse amplitude is similar (Figure 3D, averaging failures and successes), which the authors explain away by saying these measurements average glutamate from at least 60 synapses, some of which might not be stimulated. In other words, given the position of the stimulation electrode distal from the cell body layer, the fraction of activated axons is likely higher at distal ROIs, compensating for their lower Pr. This argument (from the authors!) renders the burst experiments moot (Figure 3—figure supplement 1), as the read-out is df/f (measured in large ROIs), which is mainly a function of the density of active axons. Thus, the burst response slope is expected to be steepest close to the tip of the stimulation electrode. Indeed, ROIs close to the cell body layer (80-100 μm from soma layer) showed no response at all in these experiments (Figure 3—figure supplement 1C)! The burst experiments should therefore be removed unless there is a possibility to normalize the data to the 1st pulse responses (as in PPR analysis).

3) Modeling (subsection “A realistic biophysical model explains the role of the release probability trend”), "with the Pr values distributed in accord with our data (Figure 1C)". According to the Materials and methods, you used the slope of the linear fit, which is not the same as the distribution of the measured Pr values (which are much more variable). This has to be clear in the text. In Figure 1C, some synapses have distances > 300 um, but the most distal synapses in the model seem to be just 150 μm from the soma. Is there a reason why you did not place synapses on the distal apical dendrite of the model? Given you put only proximal synapses in your model, was the average release probability and the PPR in the "Pr trend" simulation identical to the average from the measurements? The comparison of the different model scenarios only makes sense if the average Pr and facilitation was identical in all scenarios. Please show the distribution of synaptic properties for all scenarios. If the gradients really matter, I would also expect a comparison of the frequency response to proximal vs distal inputs (as in Grillo, 2018).
