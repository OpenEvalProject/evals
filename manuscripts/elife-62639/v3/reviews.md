# Peer review - Round 1

Editors:
- Jeffrey C Smith, National Institute of Neurological Disorders and Stroke United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62639.sa1](https://doi.org/10.7554/eLife.62639.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Boeri and colleagues studied the developmental emergence and transformations of electrical activity patterns of embryonic mouse Renshaw neurons in the spinal cord by a novel combination of rigorous electrophysiological and biophysical modeling analyses. Their studies indicate that a dynamic interaction of two prominently expressed sodium and potassium currents in these neurons can produce a variety of electrophysiological activity patterns and account for their transformations during embryonic development. These studies contribute importantly to understanding biophysical mechanisms by which spinal neurons express complex electrophysiological activity patterns including spontaneous activity during embryonic development.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Two voltage-dependent currents can explain the functional diversity of embryonic Renshaw cells" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jeffrey C Smith as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Ryan S Phillips (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers generally thought that your combination of electrophysiological and modeling analyses has the potential to explain the patterns of Renshaw neuron activity in terms of biophysical properties that you characterize. There was also agreement that your analyses provide a more detailed and potentially valuable developmental analysis of neuronal activity patterns than done previously for any mouse spinal neuron type during the developmental window studied. However, after discussion, the reviewers agreed that the present studies have not yet made the advance of convincingly connecting the developmental patterns of Renshaw neuron activity to the developmental patterns of spontaneous neural activity in the spinal cord, which is how the authors are trying to frame the paper.

Reviewer #1:

This very well written manuscript presents an extensive set of experimental observations with rigorous electrophysiological and sophisticated modeling analyses of how dynamically interacting sodium and potassium currents can produce different neuronal firing patterns in Renshaw cells (V1R) during mouse embryonic spinal cord development. The authors analyze firing patterns of V1R during the important developmental period when spontaneous neural activity (SNA) occurs in the mouse embryonic spinal cord (E11.5-E14.5), and during the critical period (E14.5-E16.5) when GABAergic neurotransmission shifts from excitation to inhibition and rhythmic locomotor-like activity emerges. The important finding is that there appear to be five distinct functional classes of V1R transiently present at the onset of SNA, and this functional diversity shifts as development proceeds to the critical period. The authors present substantial evidence from their experimental electrophysiological/pharmacological and biophysical modeling analyses that their observed diversity of firing patterns and the developmental transformations can be attributed largely to the dynamical synergy between two important voltage-dependent currents- the delayed rectifier potassium current and a persistent, TTX-sensitive sodium current- that the authors document from their electrophysiological measurements and can explain from their modeling analyses. These analyses provide a much more detailed view than previous ideas about patterns of emerging activity at a neuron level during embryonic spinal cord development.

1. The authors conclude that a "single mechanism" involving two voltage-gated channels with opposite functions that are ubiquitous in neurons can produce functional diversity between neurons. This is a broad statement that may pertain to the Renshaw cells studied to explain their activity patterns, but it is not at all certain that this explains activity patterns of other spinal cord neurons during development. This conclusion needs to be tempered. The authors do a nice job trying to sort out the potential contributions of IA, IKdr, INaP, and leak currents at experimental and theoretical levels. But there is no mention of calcium currents, for example, that are undoubtedly in the mix developmentally. Mixed-cationic conductances may also be involved. It is not clear that the results of these analyses apply to "many classes of embryonic cells in mammals at an early stage of development" (p. 24, line 560) without studying other embryonic cells.

2. Related to point 1, the description of experimental procedures for the voltage-clamp electrophysiological analyses of contributions of potassium currents seems incomplete. Typically, in voltage-clamp recording analyses to isolate potassium currents, sodium and calcium currents should be blocked pharmacologically. It is not clear from the Methods description that this was the case. This requires further explanation.

3. Also related to point 1, the authors don't offer any ideas about how the transformations in neuronal electrophysiological behavior might be connected to the emergence of rhythmic activity at the endpoint of their developmental analysis even though they place their analysis in this context. There are other spinal interneuron populations involved in the emergence of such activity that may show a different developmental trajectory, such as the maintenance of a relatively high GNaP/GKdr ratio and also involvement of GKleak. This requires some discussion. It is also not clear that the authors provide a reasonable explanation for the results presented in Figure 12 where they attempt to connect the patterns of V1R activity to motoneuron activity to explain SNA. These experiments add more data to an already complex data set and analyses that can probably be eliminated.

Reviewer #2:

In this manuscript, Boeri et al., investigate how the balance of a persistent sodium current (INaP) and a delayed rectifier potassium current (IKdr) shape the diversity of firing patterns in Renshaw cells in embryonic development. This study is a good example of the synergistic use of computational and experimental approaches. The authors identify four distinct types of activity patterns and demonstrate that pharmacological blockade of IKdr transforms firing patterns in a predictable sequence. Furthermore, they find differences in the maximal conductances of INaP and Ikdr which suggest that firing patterns may be determined by the ratio of these two conductances. Finally, they use computational simulations to demonstrate how the balance of INaP and Ikdr can explain the diversity of firing patterns in a model neuron. Overall I am enthusiastic about this work but have some concerns.

1. In Figure 11 C & D it is not clear what the trajectories in the GNaP-Vm plane represent since GNaP is a parameter not a dynamical variable. Does the trajectory represent GNaP*m^3*s? In 11D, is GNaP = 2.5nS as in D?

2. The basic model does a great job capturing and explaining how the GNaP/GKdr can determine the firing firing pattern Figure 10. However, I have some questions about the robustness of the modeling predictions:

i. The RS region in the model is in very good agreement with the experimental data. How sensitive is this fit to changes in INaP and IKdr activation dynamics? For example how would using the INaP activation dynamics reported in Boeri et al., 2018 change the RS region?

ii. For the simulations in Figure 10 the model does not incorporate any slow inactivation of INaP. If inactivation was included would the location of the RS region shift to the right in the GNaP-GKdr plane since a larger GNaP would be required to generate the same current?

iii. In the RS region in Figure 10 it is likely sensitive to the strength of the applied current. In the experimental data the applied current appears to range from 15-50 pA however in the model the RS region is predicted using an applied current of 20pA. Is the fit between the predicted RS region and the data as good with an applied current of 15pA or 50pA?

3. In order to explain the sequential change in V1R activity patterns with progressive block of IKdr the model requires the proportional reduction of Gin and the applied current. The applied current was not varied in any of the example traces presented in Figure 4. Why was it required in the model? Can the model still explain these transitions without reducing the applied current?

4. The explanation of the repetitive plateaus requires inactivation of INaP for the switch from the plateau to the quiescent state. In the model this results in a relatively strong slope during the plateau state and a relatively gradual transition to the quiescent state compared to the example shown in Figure 11A. Inactivation of INaP is still a reasonable explanation, however other burst termination mechanisms could explain these transitions and should be discussed. Also, does the model suggest that only neurons with repetitive plateaus and mixed events have inactivating INaP?

Reviewer #3:

This paper addresses important issues about biophysical mechanisms involved in the generation of spontaneous network activity in the developing spinal cord. Pharmacological and electrophysiological analysis are performed to characterize membrane properties of Renshaw cells during embryonic development in the mouse. The authors demonstrate the existence of heterogeneous firing properties relying on the balance between two opposing voltage-dependent conductances, the persistent sodium current (INaP) and the delayed rectifier potassium current (IKdr). A clear description is provided about how authors classified Renshaw neurons into 4 groups (long-lasting plateau potentials, mixture of spikes and short lasting bursts, repetitive spiking and single spiking) based on biophysical properties. Using both experiments and modeling, the authors show that the balance between INaP and IKdr in Renshaw neurons accounts for functional differences during development. Specifically, cells expressing bistable behaviors have the higher INaP/IKdr ratio, while single spiking cells have the lower INaP/IKdr ratio. Also, an unexpected developmental change in the firing pattern of Renshaw cells is described that switch from repetitive spiking or plateau potential patterns at E11.5-E12.5 to a dominant single-spiking pattern at E13.5-E16.5. The authors suggest that the above-mentioned change may be due to a developmental increase in IKdr. In line with this, when IKdr is decreased by 4-AP most of single spiking neurons recorded at E14.5 switch to an INaP-mediated plateau potential state.

To tackle the physiological meaning of this developmental transition in the firing pattern of Renshaw cells, the authors recorded GABAergic inputs on motoneurons and bath-applied 4-AP in isolated spinal cords at E12.5. The 4-AP-induced increase of GABAergic inputs evoked by a cervical stimulation was attributed to an increase in the excitability of Renshaw cells by favoring the emergence of repetitive firing and plateau potentials. However, we do not have direct evidence of it. These data appear to be over-interpreted insofar as IKdr is not specific to Renshaw cells. In particular, IKdr is also expressed in motoneurons and may thus influence their excitability. Furthermore, the approach of using cervical stimulation to induce GABAergic inputs onto motoneurons rather than recording spontaneous activities is surprising in the context of this study.

Overall, the authors convincingly state that INaP interacts with the IKdr to regulate the firing patterns of Renshaw cells. However, the finding of a balance between inward and outward currents in governing the firing pattern of neurons is not novel. I am afraid that the biological insights afforded by the study on the biophysical mechanisms involved in the generation of spontaneous activities are not strong enough. My opinion is that the work does not make important breakthrough such that deserving to be published in eLife.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for choosing to send your work entitled "Two voltage-dependent currents can explain the functional diversity of embryonic Renshaw cells" for consideration at eLife. Your letter of appeal has been considered by a Senior Editor, and the Reviewing editor in consultation with previous Reviewers, and we are prepared to consider a revised submission incorporating the changes indicated in your letter of appeal with no guarantees of acceptance.

To assist you in preparing your revised submission, we are communicating the following assessment in response to your appeal letter by one of the previous reviewers, who raised important concerns to be addressed in addition to your other proposed revisions.

Essential revisions:

The authors carefully consider most of my concerns. They raise a disagreement with my major concern about the lack of novelty of the main conclusion of the paper, stipulating that a simple mechanism involving two opposite slowly inactivating voltage-gated channels is sufficient to produce functional diversity in neurons. This conclusion appears to me very close to that of previous papers (see references below) where combined experimental and modeling studies show how two opposing currents shape diversity of the firing patterns (silent, spiking, bursting) in a population of neurons. None of these important studies in the field were cited. It would be interesting that the authors discuss these papers in respect to their own data and show how their main conclusion is different, deserving to be published in eLife.

1. Contribution of persistent Na+ current and M-type K+ current to somatic bursting in CA1 pyramidal cells: combined experimental and modeling study. David Golomb 1, Cuiyong Yue, Yoel Yaari J Neurophysiol. 2006 Oct;96(4):1912-26. doi: 10.1152/jn.00205.2006. Epub 2006 Jun 28.

2. Competition between Persistent Na + and Muscarine-Sensitive K + Currents Shapes Perithreshold Resonance and Spike Tuning in CA1 Pyramidal Neurons. Jorge Vera 1, Julio Alcayaga 1, Magdalena Sanhueza. Front Cell Neurosci. 2017 Mar 8;11:61. doi: 10.3389/fncel.2017.00061.

3. Intrinsic bursting activity in the pre-Bötzinger complex: role of persistent sodium and potassium currents. Ilya A Rybak 1, Natalia A Shevtsova, Krzysztof Ptak, Donald R McCrimmon. Biol Cybern 2004 Jan;90(1):59-74. doi: 10.1007/s00422-003-0447-1. Epub 2004 Jan 21.

4. Persistent Sodium Current, Membrane Properties and Bursting Behavior of Pre-Bötzinger Complex Inspiratory Neurons in vitro Christopher A. Del Negro, Naohiro Koshiya*, Robert J. Butera Jr. and Jeffrey C. Smith 01 NOV 2002, https://doi.org/10.1152/jn.00081.2002.
