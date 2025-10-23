# Peer review - Round 1

Editors:
- Sonia Sen, Tata Institute for Genetics and Society India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71238.sa0](https://doi.org/10.7554/eLife.71238.sa0)

Olfactory coding is still an open question in neuroscience. Therefore, this paper is of potential interest to a broad audience of neuroscientists. It undertakes a thorough investigation of how olfactory sensory neurons drive avoidance or attraction in flies and also addresses how combinations of active ORNs can become behaviorally meaningful. It has great potential value for clarifying how animals map sensory input to valence.


---

# Peer review - Round 1

Editors:
- Sonia Sen, Tata Institute for Genetics and Society India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71238.sa1](https://doi.org/10.7554/eLife.71238.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Most primary olfactory neurons have individually neutral effects on behavior" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Piali Sengupta as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Matthew C Smear (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

We appreciated the quality, extent, and importance of this work. While doing so, we had a few concerns that we think the authors should be able to address. They are listed below.

1. Anaesthesia: We were concerned about the short recovery period post cold anesthesia and prior to the behavioural assay. Since cold anesthesia is known to have effects on behaviour, could the authors please demonstrate that a longer duration of recovery doesn't alter their findings of neutral ORN valence?

2. wTSALE: We were concerned that this method of weighting used by the authors may be obscuring real behavioural phenomenon and therefore masking valence. Could the authors please revisit this? Providing more traces of the different response types – attraction, avoidance, weak responses, etc. – would also be helpful.

3. ORN combinations: One of the key points of this manuscript is what it tells us about the rules by which ORN combinations work. While the authors show what their study rules out, we felt that they fall short of discussing what might be occurring instead. So, could the authors please include some discussion around this point?

In this section we also recommend incorporating SupFig8 into the main figure 5. It possible that different ORN pair use different interaction rules and the grouped analysis in figure 5 would mask this. Sup Fig8 is more informative in this regard.

4. Statistics: The statistics in this manuscript are quite involved. We recognise that the authors are promoting the use of Empirical-Bayes methods for statistical inferences. Since this is not commonplace, could the authors please incorporate an intuitive explanation about Empirical Bayes, its assumptions, and why it's better suited to the analysis? We think this will greatly improve accessibility of this manuscript, and therefore its impact.

5. Comparison with the Bell and Wilson study: Could the authors please include the number of ORN pairs tested in the B and W study and their own (28 and 7)? With respect to the stimulation conditions listed in this table (Supp Table 4), we assume that the authors' count of 6 conditions is because they are including with and without airflow for their 3 light intensities. In this case, the B and W study should be listed as 16. Alternatively (indeed preferably), the two studies should be listed as 8 and 3 respectively.

Reviewer #1 (Recommendations for the authors):

Figure 1A I cannot tell the direction of airflow in the corridors. The air port is only shown on one side, does that mean airflow is unidirectional? Where is the exhaust?

I would prefer a more schematic/conceptual drawing of the arena than this quasi-realistic one where the main feature that pops out to me are the flies themselves. I would prefer that the drawing conveys the technical details needed to evaluate what the flies experience in the assay.

Fig1F The y-axis label wTSALE should be swapped for a term with some intrinsic meaning. There isn't even any basic description of what wTSALE means in the Results section, the reader has to go to the Methods. I think it would be helpful for the reader to understand the assay more clearly if the full description is in the Results. It is basically the proportion of time the flies spend outside the light, with the clock starting only after the fly has experienced the light the first time. That's pretty easy to understand and the y-axis label could be % time outside light' or even 'preference light' for positive values and 'preference dark' for negative values without criminally oversimplifying the measurement (IMO).

Also I am not convinced the weighting the authors use (i.e. wTSALE vs TSALE) is really justified. Essentially they are trying to control for shorter sampling periods of the fly's behavior in an extremely simple linear way. That implies that short sampling periods may not be representative – is it fair to simply weight those down so the score goes closer to zero since that actually indicates a lack of preference? Basically since any value on their y-axis carries meaning, it seems unfair to weight some points down simply because sampling wasn't extensive enough. Why not just require some minimal time window for flies to have experienced the light (i.e. know what they are choosing) and look at the overall proportion of time in light vs dark?

P.10 "This result indicates that wind has essentially no impact on ORN-elicited behavior in walking flies" this should read 'single-ORN-elicited behavior' since this is all the authors tested. ORN-elicited behavior could be read as ORN activation in general i.e. odor-based activation, where there is likely an effect of wind at least in some assays.

Figure 5: The authors analyze all ORN pairs together to test whether they summate/max pool/min pool but prior work (Bell and Wilson) showed that some pairs summate while others max pool, which would confound the style of grouped analysis in Figure 5G-I.

Additionally since only 7 combinations were used and only 3 intensity levels, this figure is the weakest part of the paper, which up to this point has been extremely extensive. It also makes the first entry in Table 4 (Number ORNs tested = 45 vs n=8 for Bell and Wilson) unfair since Bell and Wilson actually looked at all combinations among 8 ORNs.

Can the authors discuss more about how the dominant β value can flip as the stimulation intensity increases? How would that work in terms of neural activity in the biological network? Also, what does the diversity of β values imply about biological network, does it potentially correspond to different weights on different downstream targets?

Ending on a negative result is a little disappointing – one positive point the authors could make is that (with one exception) the ORN combinations all transition towarrds more max pooling at higher stimulation rates. This suggests an competitive interaction between channels, which is easy to imagine. Undoubtedly it is complex with different downstream targets having different rules, but this is one fairly consistent trend.

I should say that I found Bell and Wilson more convincing because they examine interactions for each ORN pair over a wider range of spike rates. Here there are just three points for comparison, and when my eyes look at Figure 5C-E it seems that there is not a lot of difference between the three interaction modes.

Finally, the authors should somehow incorporate FigS8 into the main text since I'm sure that the interaction mode depends on the pair of ORNs being examined.

Reviewer #2 (Recommendations for the authors):

– I need to understand the raw data better. What are the flies actually doing here? In 1B, the example fly seems to be walking back and forth at about 0.1 Hz. Is this representative of the population? Do the flies ever not move at all? How is this outcome dealt with? The methods mention that Empirical Bayes has a principled way of excluding outliers. What is that way? When the fly's path enters into the illuminated region, it seems to immediately stop and walk back to the opposite wall, and then on its next two cycles it stops before entering the illuminated region. Is this because the light spreads or does the fly remember where it hit the light before? What happens when the illumination occurs when the fly is already on the illuminated side? The effect of Gr66a>Chr (1F) is much larger than any of the OR effects. What does a weaker avoidance response look like? What does an attraction response look like? The mean +/- 95% CI plots of 1C-E do not answer these questions. More individual animal trajectories and population occupancy heat maps would help a lot. Exclusively compressing the data to the one wTSALE number may well be obscuring worthwhile features of the behavior. With a richer characterization of the behavior, it might be possible to reduce the sample size and simplify the statistics.

– The statistical methods are unusual and seem unnecessarily complicated (at least to me). Further, why these were used instead of something more conventional? Readers (at least this reader) would benefit greatly from clear language giving an intuition for how Empirical Bayes works, what are its assumptions, and why it is superior to more conventional, easier-to-understand methods.

– The distribution of wTSALE in Figure 2 F and G is striking. In these plots, including the controls, there is a large mode at wTSALE=1. This mode is not apparent in the distributions of 1F. Why are control flies so much more attracted to light in these experiments? How does Empirical Bayes deal with non-Gaussian distributions?

– What direction does the wind flow through the chamber? It appears to run perpendicular to the illumination axis. Could this matter? Does wind itself impact the locomotion of the flies? Since only δ-wTSALE is shown, it seems possible that wind may affect the behavior in a way that would obscure an effect. Here again it would be helpful to show more of what the flies are actually doing.

– The authors invoke "complex circuit dynamics" to explain the results of the combined-receptor experiments. I'm not sure what the authors mean here. "Dynamics" implies that time-dependent processes determine valence. If this were the case, these experiments would show no effect, since the stimuli don't recapitulate the dynamics of odor-evoked ORN activity. The discussion in a recent paper by Ron Yu's group (Qiu et al., 2021; Current Biology), deals with the non-labelled-line-ness of the mouse olfactory system in a thoughtful way. A similar discussion would benefit this paper as well.

Reviewer #3 (Recommendations for the authors):

1. The authors use a large array of GAL4 driver lines that they claim cover only the relevant ORN type. However, for most of these lines this was not examined. Although in the past such lines were used for behavior experiments, recent studies are much stricter with the use of driver lines. Many studies have demonstrated that even expression in a single neuron (other than the target neurons) either in the central brain or in the VNC can affect behavioral results. The authors therefore must show that the lines used in this study only label the target neurons either by providing adequate citations or by examining this directly with confocal stacks of both whole brain and VNC.

2. The authors do not show the relevance of their optogenetic activation of ORNs to odor activation of ORNs. Previous studies have shown that optogenetic activation of ORNs generates a firing rate of approximately 30 Hz (Bell and Wilson, 2016; Fox and Nagel, 2021). In contrast, ORNs can reach firing frequencies of up to 250 Hz in response to odors (Hallem and Carlson, 2006). In addition, ORNs show temporal dynamics, whereas I presume that the continuous illumination generates a more uniform response. The authors briefly discuss this in the methods section. They claim that "continuous illumination is a more conservative method (Tumkaya et al., 2019)". However, the same authors claim in their Tumkaya et al., 2019 manuscript that "These results suggest that neither stimulation type is necessarily superior to the other: static- or pulsed-light stimulation can capture more of the native responses than the other in inducing olfactory behavior, depending on the neuronal type". The authors also claim that "We also benchmarked behavioral responses for the Orco neurons against results from a prior study that performed physiological recordings and used a different temporal structure (Bell and Wilson, 2016), finding that the WALISAR protocol has comparable sensitivity (Figure S3)". The fact that both optogenetic activations has similar behavioral results does not imply any relevance to an olfactory cue.

My main concern is that the current optogentic stimulation probably activates ORNs relatively weakly, thus mimicking low odor concentration. As low odor concentrations elicit in many cases only weak behavioral responses it is more than possible that the lack of behavioral effect is just due to "low concentration" and not an indication to the actual role of each ORN.

Taken together, I think the authors should go the extra mileage and show some relevance to olfactory stimuli.

3. The authors own data raises potential problems with their approach. Some of the ORNs that are classified as driving aversion or attraction seem to change valence value they induce with the light intensity. For example, the authors report Or42b to drive attraction in agreement with published literature. However, at the strongest light intensity it is actually neutral. Similarly, the authors report Or85d to drive aversion. However, at the strongest light intensity it is also neutral. So, are these ORs "neutral"?

4. The authors test a number of previously suggested linear models and find that they do not predict how two-ORN odor valence emerges from single-ORN valence. However, linear models were shown to be insufficient to predict odor valence (Badel et al., 2016). It is thus not surprising that these linear models failed.

5. The authors use two databases, one of odor responses (Hallem and Carlson 2006) and one of behavioral responses (Knaden et al., 2012) along with a linear model to try and predict odor valence from ORN activity. However, as mentioned above linear models are not adequate for describing the relation between ORN activity and Odor valence. Furthermore, I think the Knaden et al., database is a wrong database to use in this context. Knaden et al., used a trap assay. In this assay, flies are captured in the trap after a single entrance to the odor source. Thus, exploratory behavior, in which flies examine the odor and then can decide to avoid it, cannot occur, and this assay is expected to be biased towards reporting odors as attractive. Indeed, this was the case in the Knaden et al., database in contrast to other published results. This database was suitable for the claim raised by Knaden et al., that looked only at the most aversive and attractive odors, but it cannot be used to try to predict any odor valence.

6. The authors used cold anesthesia just prior to loading the flies to the chambers and only 30 second acclimation following the cold anesthesia. However, cold anesthesia is known to have effects on behavior, increasing response time, reducing locomotion and reducing overall responses (just a few examples, Barron, 2000; MacMillan et al., 2017, Trannoy et al., 2015). I think most studies today try to avoid cold anesthesia just before the experiment. My concern here is that the lack of effect for most ORNs, may arise from general behavior impairment. Can the authors give a few examples from the neutral ORNs without cold anesthesia?

7. The authors conclude that: 1. "the majority of primary olfactory sensory neurons have neutral behavioral effects individually". This conclusion (as mentioned above) is definitely correct for the optogenetic activation, but its relevance to odor valence is questionable. Furthermore, Badel et al., 2016 already demonstrated with actual odor stimuli that “We find that the behavior is accurately predicted by a model summing normalized glomerular responses, in which each glomerulus contributes a specific, small amount to odor preference.” Thus, the novelty of the current study is not large.

Their second conclusion is that “olfactory sensory neurons…participate in broad, odor-elicited ensembles with potent behavioral effects arising from complex interactions”. I agree with them that olfactory coding is complex. However, they did not show any actual odor responses to support their claim, neither did they provided even one complex mechanism. I think that stating that olfaction is complex is just not enough.

8. To my understanding the order of the β coefficients can affect the interpretation of the data. However, I could not find a reference for this in the methods. Can the authors please elaborate on this?
