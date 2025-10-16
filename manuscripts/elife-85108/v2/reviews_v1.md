# Peer review - Round 1

Editors:
- Björn Herrmann, Baycrest Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85108.sa0](https://doi.org/10.7554/eLife.85108.sa0)

This fundamental work uses deep neural networks to simulate activity evoked by a wide range of stimuli and demonstrates systematic differences in latent population representations between hearing-impaired and normal-hearing animals that are consistent with impaired representations of speech in noise. The evidence supporting the conclusions is compelling, and the neural-network approach is novel with potential future applications. The research will be of interest to auditory neuroscientists and computational scientists.


---

# Peer review - Round 1

Editors:
- Björn Herrmann, Baycrest Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85108.sa1](https://doi.org/10.7554/eLife.85108.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Distorted neural signal dynamics create hypersensitivity to background noise after hearing loss" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Barbara Shinn-Cunningham as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Stephen V David (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The reviewers raised concerns about the generalizability of the study's approach. The approach hinges on the deep neural network getting things right, such that it generalizes across sounds. The study's claims would be substantially more convincing if the authors included data that validates their model's predictions about coding of speech in noise, tones in noise, and SAM noise in NH vs. HL animals. It appears that they have data in hand for speech and speech-in-noise from the same animals that they could analyze using methods already in the manuscript. If they are unable to validate any of these predictions, the authors should revise the manuscript to emphasize that they remain predictions until they can be validated with additional data in a different study.

2) Several labs have studied changes in inferior colliculus and cortex, but their work is not acknowledged in this manuscript. For example, the work by the Sanes lab at NYU and Polley lab at Harvard have advanced theories around decreased inhibition to accommodate reduced peripheral input. This work has also implicated deficits in temporal processing that do not at the surface appear consistent with the current study (e.g., see Sanes and Yao eLife 2018). The authors would want to place their work in the context of these and other works more clearly.

3) Details about some statistical tests were hard to find (e.g., only in Table S1), but it also appears that the authors still make important statements without statistical justification, for example, related to NH/HL+noise vs. NH/HL+quiet (Figures 6 vs. Figures 7). There are several other cases where conclusions, e.g., about dimensionality, are not supported by a statistical test. The authors would want to make sure that all their conclusions are supported quantitatively.

4) The authors would also want to flesh out the argument for why the same effects would not be present in the nerve.

Reviewer #1 (Recommendations for the authors):

Suggestions for authors:

-at the end of intro, I think you could make it a little more explicit that the DNN is being trained to predict PC responses from sound.

For people who will not be familiar with the practical constraints that necessitate a design with separate groups of normal-hearing and hearing-impaired gerbils, you might state explicitly early on that you are comparing separate groups of NH and HI gerbils.

Figure 1 caption – why are there two sample sizes given in the last sentence?

Line 83 – you might give some flavor as to the noise types that were used

Figure 2A is really well done -- you made a pretty complicated list of comparisons quite straightforward to follow

Line 111 and Figure 2 – I must be missing something, but I don't see how you can approach 100% explained signal variance given the way that I think it is calculated. Doesn't the noise variance show up in the denominator?

Line 130 – I suggest motivating/justifying the additional linear transformation for the reader

Figure 3 – can anything be said about how the left panel of Figure 3d looks pretty different from Figure 2i?

I don't understand what constitutes a "recorded unit". The methods refer to multi-unit activity. Is a unit just an electrode from the array of 512? Or is there spike sorting being performed? How is any non-stationarity in the recordings dealt with (e.g. if neurons die, or the brain moves a little w.r.t. the electrode array)?

Line 177 – I found myself wondering how the results would compare to a more conventional model with a STRF for each neuron. I suspect lots of people will wonder how the DNN compares to something like that.

Lines 183-185 – give numbers for the similarity, to be parallel to earlier sections

Lines 219-220 – the "clustering of dynamics" referred to here was not all that evident to this reviewer from eyeballing the figure – please make what you mean more explicit, and clarify how this is different from refs 18 and 19

Lines 232-233 – I recommend making the RDMs more conventional and just having more of them in the figure – I think people will find the asymmetry confusing when they page through the paper

Line 241 – are the numbers mean and SD? Please specify.

Line 246 – I didn't completely understand what would constitute a distortion to the "overall structure of the dynamics" – could you give an example?

Multiple figures – I don't think the asterisks are defined clearly, and I believe the mean different things in different figures. Please label more explicitly, and/or mention in each caption.

Line 287 – I found myself wondering about the possible effect of phase shifts or increases in response latency, which one might imagine could occur with hearing loss. I think the analysis would be highly vulnerable to this, especially given that the encoding of modulation is partly synchrony-based. The fact that the modulation analysis shows pretty similar results for NH and HI suggests there is not much of this, but some readers may wonder about this.

At several points throughout the paper, I found myself wondering about the effects of compression. I would have been greatly interested to see an analysis that separately manipulated compression (e.g., turning it off), to see how much benefit it produces on restoring normal-like responses. I also would have liked to see some discussion of its effects.

Line 344 – for this analysis, I was hoping to have chance levels explicitly stated, and ideally labeled on the graph.

Figure 7d – this panel is pretty confusing, partly because the SPL numbers are inside particular plots, so it is not completely clear what they apply to, and partly because the little numbers in the plots are not labeled or defined anywhere.

Line 404-406 – how does this jive with the findings of distorted tonotopy from the Heinz lab?

Line 408 and onwards – the text refers to CCs but the figure is labeled as PCs

Line 438 – why is this coherence rather than correlation?

Line 457-459 – these lines state the conclusions of the paper, but I think they could be more explicitly linked to the results that come earlier. Explain why the distortions are nonlinear, and explain why the effects involve cross-frequency interactions.

Lines 472-473 – the statement here (and the earlier one on line 33) seems a little too strong given the widespread prevalence of noise reduction, and the widespread use of speech in noise diagnostics in audiometric evaluations

Line 484 and earlier – can the clustering be explained merely by audibility (e.g., all the stimuli that are inaudible cluster together, for the uninteresting reason that they do not evoke a response)?

Line 496 – the claim here needs a reference

Line 511 – I wanted to know more about the absence of evidence of clustering in nerve responses. This seems critical.

Line 586 and onwards – I think the conclusions/suggestions here should be tempered given that there are almost surely going to be limits to how well DNN models trained in this way will generalize to arbitrary stimuli. And you might acknowledge some of these limitations.

Line 606 – I think it might be helpful to specify what a material transfer agreement would involve – does this just mean someone agrees not to share it with anyone else?

Line 691 – why is "/ 0.6745" here? Is this a typo?

Line 697 – what is a "unit"?

Line 768 – I wondered whether setting values to 0 without any windowing might induce artifacts…

Line 784 – it seems plausible that the hearing aid settings are suboptimal. In particular, the extent of compression is based on some informal optimization in humans. Could this partly explain the less than complete restoration of normal responses?

Line 810 – it would help to link this to the weights that are described in the Results section. It took me a couple reads to make the connection.

Overall, the statistical tests and quantitative comparisons are somewhat buried. There are a lot of statistical comparisons via color map (i.e., Figures 2H-I and 3D) where a scatter or bar plot with error bars might be more helpful.

Reviewer #2 (Recommendations for the authors):

1. While there are many open questions around central deficits following hearing loss, several labs have studied changes in IC and cortex, but their work is not acknowledged in this manuscript. In particular the Sanes lab at NYU and Polley lab at Harvard have advanced theories around decreased inhibitory tone to accommodate diminished bottom-up drive. Relevant to the current study, this work has implicated deficits in temporal processing that do not at the surface appear consistent with the current study (eg, see Sanes and Yao eLife 2018). Hearing loss and the neural coding of sound are complex, so the concern is not about the validity of the current results as much as how they fit in with the existing literature. Currently, the manuscript reads as if this previous work was never completed, and that issue should be addressed.

2. In general, the results of fairly sophisticated analyses are presented clearly, which is great. After some hunting, it was possible to find important details about some statistics in Table S1, but it appears that the authors still make important statements without statistical justification. Of particular importance to the main conclusions, the increased dissimilarity for NH/HL+noise vs. NH/HL+quiet (Figure 6 vs. Figure 7) needs to be demonstrated by a quantitative comparison between them. Table S1 doesn't appear to contain anything about comparisons between data in the different figures. Please provide quantitative support for the statement that "… neither was sufficient to bring the similarity close to normal levels" (Line 379). There are several other cases where conclusions, eg, about dimensionality, are not supported by a statistical test. The authors should make sure that all their conclusions are supported quantitatively. It would also

3. The performance of the DNN is impressive, providing a reasonable motivation for the subsequent analysis of "bottleneck PCs" for activity simulated by the model. However, one worries that since the models were not fit to stimuli tested in the simulation, that the results may not actually be reciprocated in actual neural activity. One contrast, in particular (speech in quiet vs. speech in noise), was actually collected experimentally, and it seems like the authors could validate their decoding analysis with the actual neural data. Can't the neural responses be projected back into the bottleneck space and be used to decode the same way as the DNN simulations? Such an analysis would substantially strengthen the study. Alternatively, the authors should include a caveat in the Discussion that the DNN simulations may not actually generalize to actual neural activity. The authors may wish to argue that this is a small concern, but the finding of such low-dimensional PC bottleneck is quite surprising, and it's not clear if dimensionality would be as small if the actual stimuli (pure tones, SAM noise) were included in the fit set.
