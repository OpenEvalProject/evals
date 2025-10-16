# Peer review - Round 1

Editors:
- Mani Ramaswami, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.43924.031](https://doi.org/10.7554/eLife.43924.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "optoPAD: a closed-loop optogenetics system to study the circuit basis of feeding behaviors" for consideration by eLife. Your article has been reviewed by K VijayRaghavan as the Senior Editor, Mani Ramaswami as the Reviewing Editor, and three reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors recently published a paper describing the use of an automated food choice assay flyPAD to study yeast taste neurons and their effects on yeast feeding. The current manuscript serves as a technical follow-up in which Moreira et al. develop and validate a closed-loop optogenetics system, optoPAD, built on top of the previously described flyPAD. OptoPAD produces light stimulation time-locked to the feeding onset detected by flyPAD, allowing for temporally precise and dynamic manipulation of targeted neuron populations. Using Bonsai data stream processing, they first extract active periods when fly is interacting with the food source. This information is then used to control high power LEDs in different wavelengths at precise time points and durations to optogenetically activate specific classes of neurons. The authors demonstrate the efficacy of their system by stimulating sugar feeding by activating sugar taste neurons or reducing yeast feeding by inhibiting taste peg neurons. Next, they also perform a dynamic task to change the acceptance of a food source in a two-choice assay by pairing one source with bitter taste neuron activation. These experiments show that close loop optoPAD system can change the value of a food source in real time by means of optogenetic activation of the avoidance pathways in the periphery. Thus, this system is shown to be useful and effective in creating virtual taste realities while individual flies are freely feeding on a define food medium. Overall, the work establishes that optoPAD system has a potential to contribute to the understanding of sensory responses and reinforcement learning in flies.

In general, the manuscript is well organized and clearly explained. However, the authors do not fully exploit the system to demonstrate its potential utility for a broad range of Drosophila applications that would greatly expand the interest and impact of this paper.

Essential revisions:

To be acceptable for publication, the manuscript must be revised with new data to: (a) show that optoPAD's utility is not limited to peripheral neurons and that can be useful for identifying/manipulating central neurons, and (b) include options that allow optoPAD to be flexible enough to allow optogenetic stimulations at times other than the onset of feeding.

1) In Figure 1, authors describe the real-time detection of food interactions in flyPAD. What is the false positive and false negative rate of this real-time data analysis? How reliable is the thresholding to detect food interactions? It would be good to show confidence rates of the system by annotating files by a human observer and comparing it with the machine annotations.

2) Authors measure the latency of the optoPAD to trigger the LED illumination and found this delay is 50-120ms. Could they mention why the delay has a 70ms range? What causes the variability? They also mention average sip duration is 130ms. Would this mean if the bout length is lower than 50-120ms, there will be a chance LED would not be activated before the sip ends? How would this impact fly's behavior? Although 10ms delay probably would not directly impact behavior, it may influence the action potentials in neurons that regulate the behavior in time periods smaller than 10ms. Could authors discuss these possibilities in their Discussion rather than claiming the delay will not impact behavior without actually testing it?

3) All of the transgenic fly strains tested in the optoPAD experiments mainly label taste sensory neurons that stimulate or inhibit feeding. Does optoPAD work for central feeding circuits to modulate feeding behavior? Testing activation of NPF or sNPF neurons that are shown to regulate food responses can demonstrate functionality of this system in neurons of the central nervous system rather than periphery. Would optoPAD work with a restricted driver that label few neurons? What are the limits of this system?

4) On the same lines, a potential advantage of the optoPAD system is to allow the design of operant conditioning experiments to study "pleasure circuits", which is challenging in flies. To do this, it would be ideal to be able to trigger optogenetic stimulation in response to touching the food or licking the food. It has previously been shown that activation of NPF neurons is in itself rewarding (Shohat-Ophir et al., 2012). Thus, it would be interesting to test whether manipulating NPF neuron activity can support operant conditioning paradigms using the optoPAD system.

5) In addition to showing that the system can modulate central neurons, can the authors determine if the system is suited for the dynamic regulation of more complex neural modules that control the microstructures of fly feeding responses to various food?

6) In Figure 4, authors try an elegant experiment to change the value of a food source by activating bitter taste neurons in a two-choice assay. They see no difference between two sides in the first 10 minutes of the experiment even though one side is paired with punishment (bitter neuron activation). Can authors explain the 10-minute delay in the results further? In this period of time are the flies interacting with the food at all?

7) To expand the versatility of optoPAD, it would be useful to add an "open-loop" mode in the setup, where light stimulation can be controlled at will and does not need to follow feeding onset. This will allow users to take full advantage of the high temporal resolution of both flyPAD and optogenetics to study feeding related modalities before ingestion happens, such as tasting and feeding initiation.

8) To allow for more diverse experimental designs, it would be useful if one could choose to deliver the stimulations at the end of a feeding bout. For example, a researcher might be particularly interested in the inter-meal interval. In this case, stimulation placed at the end of an activity bout will help to evaluate whether circuit manipulation affects the latency to start next feeding bout since the cessation of the last one.

9) It would also be useful to be able to control the number of optogenetic stimuli delivered to the fly, for example, if one wanted to have a maximum number of activations for the targeted neural circuit.
