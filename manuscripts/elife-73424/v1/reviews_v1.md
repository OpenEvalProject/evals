# Peer review - Round 1

Editors:
- Muriel Thoby-Brisson, https://ror.org/057qpr032 CNRS Université de Bordeaux France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73424.sa0](https://doi.org/10.7554/eLife.73424.sa0)

This article will interest neuroscientists who study how spinal circuits control locomotion. While the role of spinal interneurons in control of left–right and flexor–extensor alternations has been studied extensively, their role in hind–forelimb coordination has not been sufficiently studied. Zhang et al. study interlimb coordination by combining experimental data and computer simulation to shed light on how a population of spinal neurons may coordinate hind and fore limbs during locomotion at different speeds.


---

# Peer review - Round 1

Editors:
- Muriel Thoby-Brisson, https://ror.org/057qpr032 CNRS Université de Bordeaux France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73424.sa1](https://doi.org/10.7554/eLife.73424.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "The role of V3 neurons in speed-dependent interlimb coordination during locomotion in mice" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Tuan V Bui (Reviewer #1); Avihu Klar (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The present study aims at identifying a sub-population of V3 neurons that would be involved in coordinating hindlimb and forelimb movements, thus influencing locomotor speed and gait adaptation. These long-projecting V3 neurons (LPNs) would be excitatory, express the transcription factor Sim1, are located at the lumber level, are ascending with contralateral cervical projections. Their experimental silencing changes speed/gait adaptation. Experimental data can be replicated using an already existing computational model of the locomotor circuitry incremented with the newly identified V3 aLPN neurons. Despite the fact that the data presented here are addressing the role of spinal interneurons in hind/forelimb coordination, which has been only insufficiently examined so far, the study suffers from several problems that should be addressed before the paper can be judged suitable for publication in eLife.

The major concerns are as follows:

1) The methodological approaches are not always targeting specifically the neurons of interest. For instance, the retrograde labeling method used to label V3 aLPN neurons is not specific enough (see reviewers' comments). We recommend at least that the author amend their diagram in Figure 1A1 to show that they could also be staining en passant axons and that they state this in the text as a source of uncertainty. Also the blockade of glutamatergic signaling at the lumbar level as it is performed blocks all connections and not only those involving V3 aLPN neurons. It is right that the stimulation is specific but no direct conclusions can be reached from these experiments on the exclusive role of V3 aLPN neurons specifically. Connections of these neurons with all other ones located at the same level will also be affected. Conclusions here must be made cautiously and limitations addressed in the discussion.

2) A lack of description of the connections between the neurons of interest (V3 aLPN) and the other sub-population of V3 neurons identified in previous studies (namely the commissural V3), and also with interneurons known to be involved in the control of gaiting and locomotor speed. In the same vain, it is not clear whether the kinetics' of the recordings points to monosynaptic or polysynaptic connectivity. Therefore, it is imperative to demonstrate at least that the lumbar aV3 are either pre-cervical-MN, or innervate the pre-cervical-MN, as indicated in Figure 7. We are aware that demonstrating the anatomy of the lumbar aV3 is not straightforward due to the transient expression of Sim1 at embryonic stages and the amount of work it represents. Therefore, we are willing to comprise on obtaining the anatomy data, if more accurate electrophysiology data are obtained even if it requires the traditional "old-fashioned" electrophysiology to support the authors' model.

3) It appears incorrect to use data obtained on the V3OFF mice (in which all V3 neuronal subtypes are targeted) to conclude on the specific role of V3 aLPN neurons. For example some models can account for the phenotype of the locomotion following deletion of vGlut2 in V3 neurons. Maybe the cervical V3 neurons receive inputs from other lumbar interneurons? Hence, impairing their activity may result in similar gait impairments. We think that manipulating the lumbar aV3, or at least, the entire lumbar V3 is imperative for substantiating the model. The authors should find ways to eliminate only V3 aLPN neurons as suggested by reviewers (or at least to strongly moderate their conclusions).

4) In the present study, the computational model replicates quite well data observed in vitro. This is a powerful tool to develop new hypothesis. But the main interest is then to subsequently test at least some of these hypothesis. Here a long part of the paper is dedicated to describe the model (which is now quite complex) and to establish that it does what the modeler wants, but it would strengthen the paper if at least one of the prediction could be tested here. Additional experiments are required here, as suggested by the reviewers.

5) In a general manner, figures are very loaded and complicated to understand at a first sight. It would be useful for the readers to be guided towards what are the important panels. For example on Figures 4 and 11 could you highlight one way or another the panels on which the readers should focus on. Also data presented in Figure 1b requires details. Indeed traces are small and presented with an inappropriate time scale: the coordination between lumbar/cervical, and left/right is not visible. Could you add samples at a different time scale? And quantification of the intensity of activity before, during and after the light stimulation should be provided (see comments of reviewers).

Reviewer #1:

In this study, the authors sought to describe the role of a set of spinal neurons named V3 interneurons in the coordination of hindlimbs and forelimbs in locomotor control in mice.

The authors first mapped how these neurons in the lumbar section of the spinal cord, involved in the control of the hindlimbs, were connected to cervical section controlling the forelimbs. They then analyzed stimulating or removing these neurons affected locomotor output using optogenetics and transgenic silencing. Finally, the authors used computational modelling to infer possible connections between these neurons with other spinal neurons in the forelimb and hindlimb segments of the spinal cord that could explain the results that were observed during their experiments.

The major strengths of the study was the rigorous analysis of locomotor deficits in animals lacking the V3 neurons. The replication of these phenotypes in the computational models generates testable hypotheses about the connectivity of the V3 neurons with the rest of the spinal cord.

While the experimental and computational methodology is rigorous, an analysis of the phase relationship of cells, between cells controlling limb coordination involving ascending V3s would provide greater insights into the operation of the spinal locomotor circuits.

The experimental and the simulation results support the role of ascending V3 interneurons in the control of left-right coordination across forelimb and hindlimbs.

The computational models build upon previous models from the authors. They are useful tools for the community to study the operation of spinal circuits to control the many parameters of locomotor control.

Suggestions:

1. Can you go into more details regarding the rationale of the diagonal aV3 populations? I would suggest moving the section Circuit interactions mediated by V3 subpopulations before describing the model connectivity because it provides a rationale for the connectivity of these neurons in the model.

2. Please describe the rationale for modelling a descending drive to aV3s.

3. I don't fully agree that the increase in activity in the V3 population seen in the model would be reflected in the increased cFos expression, which is a proxy for the number of neurons that are activated. From the model, it looks like the population is fully active at lower speeds but their firing frequency increases with speed.

4. I agree that the model qualitatively replicates the experimental results with the V3OFF mice. In addition, can you describe where the model differs from experimental results for the V3OFF data?

5. Could you generate phase plots to show how the relationship between the activity of relevant cell populations shift at different speeds and without aV3s?

6. In the analysis of the computer simulations, how was the minimal burst amplitude determined? Were there bursts that could have just been due to noise in RG activity?

Reviewer #2:

The Zhang et al., study addresses the role of lumbar to cervical ascending V3 interneurons in controlling intralimb coordination. The role of spinal interneurons in control of left/right and flexor/extensor alternations has been studied extensively, while their role in hind/forelimb coordination is yet insufficiently studied. In this respect, revealing the role of lumbar-cervical V3-aLPN is essential and timely. The authors are using retrograde labeling and physiological recording to demonstrate the lumbar to cervical connectivity of V3, kinematic analysis of V3off mice in which the vGlut2 was conditionally removed in all V3 neurons, and present an updated model. Based on computationally testing their theoretical model, the authors also hypothesize the outcome of silencing only the V3-aLPN subpopulation. There are two main concerns that question the validity of the findings: 1) the data that supports the lumbar-to-brachial connectivity are not sufficiently convincing, 2) the conclusion about the role of V3 in intralimb coordination is based on the silencing of the entire V3 populations not the V3-aLPN subpopulation.

1) The data in figure 1 demonstrate the lumbar-cervical connectivity of V3 neurons. The authors are using retrograde labeling attained by cervical injection of CTB. However, CTB may also label transneuronal processes (passing by axons). Two previous papers cited extensively throughout this manuscript mapped the descending cervical-to-lumbar connectome of spinal interneurons (Ruder et al., 2016 and Flynn et al., 2017). In these papers, the researchers use more reliable retrograde labeling methods: Rabies and Fluorogold. Since the central issue of the manuscript relies on the lumbar-cervical circuit, more data should be provided. For example, 1) The distribution of V3-lumbar synapses in the cervical level. 2) Labeling the lumbar aLPN by using alternative retrograde labeling methods.

The experiment presented in 1B is supposed to provide physiological verification to the lumbar-cervical connectivity. The authors present one representative trace of rectified ENG recordings following single light activation of the lumbar V3 neurons. Quantification of the excitation level before-during-after blue light emission in several (at list 10) episodes should be included. By observing figure B1, I am not convinced that Left C8 is activated at all.

2) The paper's main conclusion is: "The proposed V3 aLPN connections support diagonal synchronization necessary for trot whereas the local V3 CIN connections support left-right synchronization necessary for gallop and bound". The theoretical model supports the following hypothesis: "selective deletion of only V3 aLPNs in the model allowed for stable coordination of limb activities at high speeds, i.e., during gallop and bound, whereas trot was completely lost and the model transitioned from walk directly to gallop and bound". The suggested experiment is imperative to prove this hypothesis, and the authors have the means to perform this experiment.
