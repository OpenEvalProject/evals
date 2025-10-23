# Peer review - Round 1

Editors:
- Juan Alvaro Gallego, Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101325.3.sa0](https://doi.org/10.7554/eLife.101325.3.sa0)

This study characterises motor and somatosensory cortex neural activity during naturalistic eating and drinking tongue movement in nonhuman primates. The data, which include electrophysiology, three-dimensional tracking of tongue movements, and nerve block manipulations, are valuable to neuroscientists and neural engineers interested in tongue use. Although the current analyses provide a solid description of single neuron activity in these areas, both the population level analyses and the characterisation of activity changes following nerve block could be improved.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101325.3.sa1](https://doi.org/10.7554/eLife.101325.3.sa1)

Summary:

Hosack and Arce-McShane investigate how the 3D movement direction of the tongue is represented in the orofacial part of the sensory-motor cortex and how this representation changes with the loss of oral sensation. They examine the firing patterns of neurons in the orofacial parts of the primary motor cortex (MIo) and somatosensory cortex (SIo) in non-human primates (NHPs) during drinking and feeding tasks. While recording neural activity, they also tracked the kinematics of tongue movement using biplanar video-radiography of markers implanted in the tongue. Their findings indicate that many units in both MIo and SIo are directionally tuned during the drinking task. However, during the feeding task, directional turning was more frequent in MIo units and less prominent in SIo units. Additionally, in some recording sessions, they blocked sensory feedback using bilateral nerve block injections, which seemed to result in fewer directionally tuned units and changes in the overall distribution of the preferred direction of the units.

Strengths:

The most significant strength of this paper lies in its unique combination of experimental tools. The author utilized a video-radiography method to capture 3D kinematics of the tongue movement during two behavioral tasks while simultaneously recording activity from two brain areas. This specific dataset and experimental setup hold great potential for future research on the understudied orofacial segment of the sensory-motor area.

Weaknesses:

A substantial portion of the paper is dedicated to establishing directional tuning in individual neurons, followed by an analysis of how this tuning changes when sensory feedback is blocked. While such characterizations are valuable, particularly in less-studied motor cortical areas and behaviors, the discrepancies in tuning changes across the two NHPs, coupled with the overall exploratory nature of the study, render the interpretation of these subtle differences somewhat speculative. At the population level, both decoding analyses and state space trajectories from factor analysis indicate that movement direction (or spout location) is robustly represented. However, as with the single-cell findings, the nuanced differences in neural trajectories across reach directions and between baseline and sensory-block conditions remain largely descriptive. To move beyond this, model-based or hypothesis-driven approaches are needed to uncover mechanistic links between neural state space dynamics and behavior.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101325.3.sa2](https://doi.org/10.7554/eLife.101325.3.sa2)

Summary:

This manuscript by Hosack and Arce-McShane examines the directional tuning of neurons in macaque primary motor (MIo) and somatosensory (SIo) cortex. The neural basis of tongue control is far less studied than, for example, forelimb movements, partly because the tongue's kinematics and kinetics are difficult to measure. A major technical advantage of this study is using biplanar video-radiography, processed with modern motion tracking analysis software, to track the movement of the tongue inside the oral cavity. Compared to prior work, the behaviors are more naturalistic behaviors (feeding and licking water from one of three spouts), although the animals were still head-fixed.

The study's main findings are that:

• A majority of neurons in MIo and a (somewhat smaller) percentage of SIo modulated their firing rates during tongue movements, with different modulation depending on the direction of movement (i.e., exhibited directional tuning). Examining the statistics of tuning across neurons, there was anisotropy (e.g., more neurons preferring anterior movement) and a lateral bias in which tongue direction neurons preferred that was consistent with the innervation patterns of tongue control muscles (although with some inconsistency between monkeys).

• Consistent with this encoding, tongue position could be decoded with moderate accuracy even from small ensembles of ~28 neurons.

• There were differences observed in the proportion and extent of directional tuning between the feeding and licking behaviors, with stronger tuning overall during licking. This potentially suggests behavioral context-dependent encoding.

• The authors then went one step further and used a bilateral nerve block to the sensory inputs (trigeminal nerve) from the tongue. This impaired the precision of tongue movements and resulted in an apparent reduction and change in neural tuning in MIo and SIo.

Strengths:

The data are difficult to obtain and appear to have been rigorously measured, and provide a valuable contribution to this under-explored subfield of sensorimotor neuroscience. The analyses adopt well-established methods especially from the arm motor control literature, and represent a natural starting point for characterizing tongue 3D direction tuning.

Weaknesses:

There are alternative explanations from some of the interpretations, but those interpretations are described in a way that clearly distinguishes results from interpretations, and readers can make their own assessments. Some of these limitations are described in more detail below.

One weakness of the current study is that there is substantial variability in some of the results between monkeys, including the tuning characteristics of primary somatosensory cortex neurons during drinking, and the effect of nerve block on tongue movements and the associated changes in single neuron tuning.

This study focuses on describing directional tuning using the preferred direction (PD) / cosine tuning model popularized by Georgopoulous and colleagues for understanding neural control of arm reaching in the 1980s. This is a reasonable starting point and a decent first order description of neural tuning. However, the arm motor control field has moved far past that viewpoint, and in some ways an over-fixation on static representational encoding models and PDs held that field back for many years. The manuscript benefit from drawing the readers' attention (perhaps in their Discussion) that PDs are a very simple starting point for characterizing how cortical activity relates to kinematics, but that there is likely much richer population-level dynamical structure and that a more mechanistic, control-focused analytical framework may be fruitful. A good review of this evolution in the arm field can be found in Vyas S, Golub MD, Sussillo D, Shenoy K. 2020. Computation Through Neural Population Dynamics. Annual Review of Neuroscience. 43(1):249-75. A revised version of the manuscript incorporates more population-level analyses, but with inconsistent use of quantifications/statistics and without sufficient contextualization of what the reader is to make of these results.

The described changes in tuning after nerve block could also be explained by changes in kinematics between these conditions, which temper the interpretation of these interesting results.

I am not convinced of the claim that tongue directional encoding fundamentally changes between drinking and feeding given the dramatically different kinematics and the involvement of other body parts like the jaw (e.g., the reference to Laurence-Chasen et al. 2023 just shows that there is tongue information independent of jaw kinematics, not that jaw movements don't affect these neurons' activities). I also find the nerve block results inconsistent (more tuning in one monkey, less in the other?) and difficult to really learn something fundamental from, besides that neural activity and behavior both change - in various ways - after nerve block (not at all surprising but still good to see measurements of).

The manuscript states that "Our results suggest that the somatosensory cortex may be less involved than the motor areas during feeding, possibly because it is a more ingrained and stereotyped behavior as opposed to tongue protrusion or drinking tasks". An alternative explanation be more statistical/technical in nature: that during feeding, there will be more variability in exactly what somatosensation afferent signals are being received from trial to trial (because slight differences in kinematics can have large differences in exactly where the tongue is and the where/when/how of what parts of it are touching other parts of the oral cavity)? This variability could "smear out" the apparent tuning using these types of trial-averaged analyses. Given how important proprioception and somatosensation are for not biting the tongue or choking, the speculation that somatosensory cortical activity is suppressed during feedback is very counter-intuitive to this reviewer. In the revised manuscript the authors note these potential confounds and other limitations in the Discussion.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101325.3.sa3](https://doi.org/10.7554/eLife.101325.3.sa3)

Summary

In this study, the authors aim to uncover how 3D tongue direction is represented in the Motor (M1o) and Somatosensory (S1o) cortex. In non-human primates implanted with chronic electrode arrays, they use X-ray based imaging to track the kinematics of the tongue and jaw as the animal is either chewing food or licking from a spout. They then correlate the tongue kinematics with the recorded neural activity. They perform both single-unit and population level analyses during feeding and licking. Then, they recharacterize the tuning properties after bilateral lidocaine injections in the two sensory branches of the trigeminal nerve. They report that their nerve block causes a reorganization of the tuning properties and population trajectories. Overall, this paper concludes that M1o and S1o both contain representations of the tongue direction, but their numbers, their tuning properties and susceptibility to perturbed sensory input are different.

Strengths

The major strengths of this paper are in the state-of-the-art experimental methods employed to collect the electrophysiological and kinematic data. In the revision, the single-unit analyses of tuning direction are robustly characterized. The differences in neural correlations across behaviors, regions and perturbations are robust. In addition to the substantial amount of largely descriptive analyses, this paper makes two convincing arguments (1) The single-neuron correlates for feeding and licking in OSMCx are different - and can't be simply explained by different kinematics and (2) Blocking sensory input alters the neural processing during orofacial behaviors. The evidence for these claims is solid.

Weaknesses

The main weakness of this paper is in providing an account for these differences to get some insight into neural mechanisms. For example, while the authors show changes in neural tuning and different 'neural trajectory' shapes during feeding and drinking - their analyses of these differences are descriptive and provide limited insight for the underlying neural computations.
