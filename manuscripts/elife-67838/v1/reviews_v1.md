# Peer review - Round 1

Editors:
- Jonas Obleser, University of Lübeck Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67838.sa1](https://doi.org/10.7554/eLife.67838.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Stephani et al., address the question of how ongoing fluctuations in neuronal excitability, as well as stimulus strength, impact the perception of above-threshold tactile stimuli and the subsequent stimulus-evoked brain activity. The study builds up on very high quality data as well as analysis approaches and, alongside a decent sample size and a host of additional peripheral measures and a simulation study, allows the authors to challenge common interpretations of brain potential magnitudes in stimulus-intensity encoding.

Decision letter after peer review:

Thank you for submitting your article "Neural excitability and sensory input determine intensity perception with opposing directions in initial cortical responses" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Floris de Lange as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Richard Gao (Reviewer #1); Nathan Weisz (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The main weaknesses of the manuscript become most apparent with respect to the stated impact that "The widespread belief that a larger brain response corresponds to a stronger percept of a stimulus may need to be revisited.". We are not sure that there are many cognitive neuroscientists who would subscribe to such a simplistic relationship between evoked responses and perception and that temporal differentiation (early vs late responses) and the biasing influence of prestimulus activity patterns are becoming increasingly recognized. So rather than actually changing a dominant paradigm, this work is an (excellent) contribution to a paradigm shift that is already taking place. Unneccesary claims of controiversiality and novelty thus should be toned down. See many specific hints to this in the two individual reviews below.

2) A main technical concern lies in the choice of decomposition filter for SEP and α oscillations, and the conclusions the authors draw from that. Specifically, a CCA spatial filter is optimized here for the N20 component, which is then identically applied to isolate for α sources, with the logic being that this procedure extracts the α oscillation from the same sources (e.g., L359). If our understanding of the authors' intent is correct, then the majority of us does not agree with the logic that using the same filter will isolate for α as well. The prestimulus α oscillation can have arbitrary source configurations that are different from the SEP sources, which may hypothetically have a different association with the behavioral responses when it's optimally isolated. In other words, just because one uses the same spatial filter, it does not imply that one is isolating α from the same source as the SEP, but rather simply projecting down to the same subspace – looking at a shadow on the same wall, if you will.

To show that they are from the same sources, α should be isolated independently of the SEP (using CCA, ICA, or other methods), and compared against the SEP topology. If the topology is similar, then it would strengthen the authors' current claims, but ideally the same analyses (e.g., using the 1st and 5th quintile of α amplitude to partition the responses) is repeated using α derived from this procedure. Also, have the authors considered using individualized α filters given that α frequency vary across individuals? Why or why not?

3) It should be considered that with regards to the analysis approach using CCA, the claims are mainly restricted to BA3b: The authors should refrain from overinterpreting the results in a very generalized manner. The authors do include some "thalamus" and "late" evoked response patterns as well, however that presentation of the results is somewhat changed now as compared to the N20 (e.g. using LMEs rather than comparison of extremes; not using SEMs). The readablity of results and especially the comparison of effects would profit from a more coherent approach.

4) Concerns arose whether the relationship between large α power and more negative N20s could be driven by more trivial factors rather than the model explanations the authors develop in the discussion. Put in concrete terms, the question is whether phase locking of large α power along with >30 Hz high pass filtering could produce a similar finding as shown e.g. in Figure 2c. This is an important issue, as prestimulus α influences the N20 amplitudes as well as the perceptual reports. See also our point #1 above.

5) At multiple points, the authors comment that the covariation of N20 and α amplitude in the same direction is counterintuitive (e.g., L123-125). It is being explained later in the manuscript that lower α amplitude and higher SEP amplitude are associated with excitability, and hence should have the opposite directions. This should be explicitly stated earlier in the introduction, as well as the expected relationship between α amplitude and behavior.

Reviewer #1 (Recommendations for the authors):

General comments for improving clarity and other discussion points

– Figure 1 is a really nice schematic of the study. Personally, it would have been extremely helpful to have an additional panel that shows the quintile analysis, and perhaps a visual representation of the quantities extracted (i.e., sensitivity and criterion). A slightly adapted version of a generic SDT schematic would be sufficient for the naive reader such as myself (as I had to Google around a bit), but could be unnecessary given the target audience of the paper

– What is the rationale for choosing the top and bottom 20% of α / SEP amplitude for partitioning? Is this just an arbitrary choice? If so, is the result robust to using, say, quartiles?

– α amplitude was higher in general when response was "weak", but SEP amplitude was larger for all stronger stimuli, and only larger when response was "weak" conditioned on the stimulus strength. In fact, it looks like the SEP effect is really driven by a difference within the strong stimuli (Figure 2d). I may have missed this, but a comment on this and why it might be would be great.

– I'm not sure if this was by design to emphasize the counterintuitiveness of the findings, but at multiple points in the manuscript, the description of the α and SEP effects are reversed with double negatives. For example, L100-102 says α amplitude was higher when participants rated the stim to be "weaker", while L140-141 says SEP was smaller when participants rated the stim to be "stronger". If I'm not mistaken, these mean the same thing, especially considering that N20 negativity is also intuitively an amplitude, in which case, both amplitude measures correlate with a bias towards "weaker" ratings. Same with the arrangement of figure 2b and 2e, where it would be natural to put higher amplitude (i.e., more negative N20) on the right. Unless this was done very intentionally, I think it would improve the clarity of the manuscript to make those descriptions and figures the same.

– Which is SEM1? Is that represented in Figure 4? I don't think this is labeled anywhere, and in the table SEM1 is just "original model"

– I might have misunderstood something here, but it was very surprising that the thalamic component does not vary as a function of stimulus intensity? Is there an explanation for this?

– Just to reiterate the earlier point on α, L312-317 is a really nice explanation of the model the authors have in mind, though I had a totally different one reading through the paper, that basically α amp and SEP amp have a shared origin, and hence both reflect synchronous neuronal activity, potentially of the same population. My reading of the author's interpretation is that α is a readout of excitability, and the lower the α amp the higher the excitability, which leads to more depolarized neurons and hence smaller EPSCs in a different (population). If this is correct, my suggestion would be to hint at this earlier on, so people don't go down the same rabbit hole as I did (though I am unfamiliar with this literature)

– Related to the above, I had to really wrap my head around the fact that the N20 is both a function of the true stimulus intensity (i.e. post-stim readout), as well as a marker for prestim (or ongoing) neural excitability (i.e., pre-stim readout). I know this is the whole point of the paper, but a sentence explicitly stating that very early on might help the naive reader to orient themselves to the subsequent findings.

– L328-330: nice emphasis on the significance, would do the same earlier as well if not already.

– I think a brief discussion on how the brain then uses the information represented by the SEP downstream to "perform the perceptual rating" would be great, i.e., does it account for the ongoing fluctuation in excitability?

– L351-355: CNAP (sensory readout) variability did not influence perceptual decision, but CMAP (muscle output) variability does – both are within the first 10ms, so there must be another loop from the motor reaction / reflex readout to the brain, and when does the brain / subject make the decision? Does the motor percept also feed back into the N20?

– I was looking for an explanation as to why criterion might be affected here but not sensitivity, maybe a brief discussion speculating on this point would be appropriate?

Again, great paper – it was a joy to read!

Reviewer #2 (Recommendations for the authors):

Overall I found the manuscript very interesting and my recommendations pretty much concern the discussed weaknesses.

– The authors should reflect more clearly the impact of the study along the lines mentioned above. I pretty much have the impression that the results are not a "game changer" in the field but fits well with increasingly dominant views in the field.

– I would strongly advise to check the possibility whether the α-N20-link could be caused by high-pass-filtering of phase locked α responses. Along these lines a time frequency depiction of results in figure 1a would be helpful (i.e. showing low to high frequencies of non-high pass filtered data). Also since the link between N20 and perception appears "counterintuitive", it may be also useful to test the relationship within α bins (i.e. high-low N20 responses stratified for α power) and see whether the relationship still holds.

– Furthermore, it would improve readability if the authors used a streamlined statistical approach also for the "thalamic" and "late" evoked responses.

– The authors convincingly show that evoked peripheral responses are not linked to N20 amplitude. It would be interesting to know whether variability in ongoing peripheral activity is linked to ongoing α activity (i.e. in prestimulus period).

– At the moment the value of the physiological model developed in the discussion is not really clear (see previous comments). It also seems to be particularly geared to the N20 results and leaves open the question whether it also encompasses the "thalamus" and "late" results.
