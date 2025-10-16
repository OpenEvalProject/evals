# Peer review - Round 1

Editors:
- Inna Slutsky, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59247.sa1](https://doi.org/10.7554/eLife.59247.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work uncovers the role of two distinct cortico-fugal pathways in the learning and the performance of a visual detection task. It demonstrates that visual cortex neurons that project to the striatum enhance learning speed, while visual cortex neurons that project to the superior colliculus enhance detection sensitivity. This study contributes to our understanding of the function of visual cortex during the learning and execution of a visual task.

Decision letter after peer review:

Thank you for submitting your article "Distinct cortico-fugal neurons in visual cortex enhance learning speed and detection sensitivity" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Andrew King as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Summary:

In this manuscript the authors investigate the different roles of two different subclasses of projection neurons in visual cortex during a simple stimulus detection task. The functional role of each subclass is assessed by targeting them for selective ablation based on their projection target. One cell type, projecting to the striatum, is vital for acquisition of the task but is dispensable for performance after acquisition. The second cell type, projecting to the superior colliculus, is not required for the mice to learn the task, but has a modulatory role during performance – activity in these cells enhances behavioural sensitivity moment-to-moment.

The findings are important and should be of great interest to the behavioural neuroscience community. The results are presented clearly, logically and succinctly. The reviewers have some concerns which can be addressed with editorial changes, further analysis and/or discussion. Some comments call for more histology which is hopefully possible. Other comments could be addressed by new experiments (relating to 1P stimulation), but these experiments should be considered optional.

Essential revisions:

1) The core of the story is learning; task acquisition and task performance. It is therefore quite surprising that behavioural performance seems so poor – there is a very high false alarm rate even in learned animals (86% probability of lick in the absence of a stimulus, Figure 1 far right example. Note the example in Figure 4 is much better). Could the authors please discuss this issue? While this does not challenge the results in the paper, it does raise some concern over the “expertness” of the animals, i.e. how well they have actually learned. This should be mentioned as a caveat and discussed. What could the possible reasons for the high false alarm rate be? The stimulus duration is quite long at 4 seconds; perhaps with a shorter stimulus (and thus shorter blank period and/or shorter response window) the performance would improve.

2) Further to the previous comment, the authors write “learning was considered complete by 14 days” but it does not appear as though the FA rate has stopped dropping by this time, i.e. the animals are still learning. While the performance in this simple task is not exactly exemplary, it is clear the mice are trying; the concern is how do these results depend on actual task performance, or “expertness”?

3) Wording of main claim: The authors stress throughout the manuscript that they have shown how Str neurons "enhance learning speed" while CT neurons "improve detection sensitivity". Instead what they have shown is that lesioning Str neurons slows down learning and lesioning CT neurons decreases sensitivity. The reversal of interpretation currently used is not justified, since if you claim Str neurons enhance learning speed, it begs the question, enhanced compared to what? We can only make such relative statements from the known rate of learning in an intact animal as a reference, and the correct conclusion is thus an impairment on lesioning. "Impairs the rate of learning", "is required for normal learning rates", etc are alternatives that the authors could use instead.

Importantly, the current phrasing leads the reader to assume that the authors have performed a manipulation that actually speeds up learning compared to controls, which is what the Abstract currently implies. I would advise the authors change all phrasing of this kind throughout the entire manuscript, including title and Abstract.

4) Statistics: There are a number problems with the statistics throughout the paper which must be corrected in order to justify the claims.

– In Figure 1 it is unclear what statistics have been done to compare the learning rates across conditions. The text only mentions slope, SEM, and n.s. No further information is available in the Materials and methods. This needs to be clarified. What exact test has been done to determine that the slopes in two linear regressions are significantly different? Have the authors calculated the confidence intervals of the slope using bootstrapping? Or have they performed linear regression analysis and measured the significance of an interaction term between session number and lesion condition?

– A serious concern is that in Figure 1E, the cortico-striatal lesion condition has been statistically tested against the cortico-tectal, rather than control mice. This does not support the claims made either in text or in the figure, where the control mice plots are overlaid on the same panel.

– Further, lesion of full visual cortex are compared with striatal lesion and a non-significant difference is reported. Clearly the correct test is to compare VC lesion with the VC controls (which the authors have done when comparing spontaneous lick rates).

– Spontaneous lick rates have been compared in some, but not other cases. This measure is particularly important for the striatal lesion case (see below). Could the authors specify what time periods are included in “spontaneous” and provide comparisons of spontaneous lick rate consistently.

– In a number of cases throughout the manuscript, statistics have been performed on N sessions, which includes multiple sessions from the same animals (e.g. 9 sessions from 6 mice). This is incorrect since multiple sessions from the same mouse are not independent samples. While errors of this kind are unfortunately common in the field at the moment, it is important to avoid it in general, and in particular in this study given that behaviour is highly correlated within individuals. One way to deal with data of this nature is to perform tests with fixed and random effects (e.g. as described in Aarts et al. Nat Neurosci 2014). Another option is to average sessions for each animal.

– Figure 5B: A key claim of this study is that CT lesions reduce sensitivity. However, we only found a comparison of the effect of optogenetic silencing vs. no silencing, but no test between the non-silenced pre vs. post CT lesion. Although the figure legend says “Note reduction in rightward shift of the contrast threshold after CT lesion“ this is not actually compared. This seems like a key comparison to support the main claim of the study.

5) Gross behavioural changes: Measures of gross behavioural changes should be measured with and without lesions in order to rule out the role of these changes in learning rates and sensitivity curves. Importantly, non-stimulus period lick rate should be compared between controls and visual cortex/cortico-striatal lesions, since a reduction in overall lick rate may account for the lower rate of learning.

– The number of trials was limited to 250 per training session: Could the authors clarify if all mice always reached 250 trials in each session, and if not, report the average and range of trials actually performed by the mice in each group. With this information, could the authors rule out that any differences in rates of learning were due to different numbers of trials performed in some days by lesioned mice.

6) Latency of first licks on blank trials: In the behavioural paradigm used here, latency from blank trials onset is not really a latency, since the mouse experiences a continuous blank screen even though the software might have transitioned from the delay to the “blank” stimulus. This point should be made clear to the reader in the Results and Materials and methods sections, especially when presenting plots like Figure 1B where histograms of lick latencies on blank trials are presented.

7) The Introduction is heavily focused on cross species comparisons and evolutionary arguments, and appears more appropriate for a cross species comparative study. In particular, it seems to set up a comparison between mammals, with expanded cortico-fugal pathways, and non-mammals without this expansion. While this is an entirely subjective judgement, this study would benefit from an Introduction more suited to the questions addressed.

8) Throughout the manuscript, emphases such as the following occur along with essentially each result presented:

– "the visual specificity of the licking behavior increased much slower"

– "learning progressed much slower and.… was far from complete."

– "… strongly reduced the impact"

The authors should either substantiate what “much slower”, “far from complete” etc means, or rephrase as much as possible.

9) It's not immediately clear what the timing of the task is. The schematic in Figure 1A should be extended so as to indicate the timing of the task. The Materials and methods state the stimulus duration is "up to 4 seconds". Why up to? What about the time between trials? What was the actual ITI? Was the no-lick requirement invalidated often for these mice? (do the mice lick constantly or have they learnt to withhold the licking mostly but the 4 second blank is just too long in addition?)

10) The authors use a metric that is unconventional – aROC of lick latencies. This reaction time metric does make sense and appears convincing from the example in Figure 1. While I like the metric, it is not standard in the field. Therefore it would be nice to more fully compare it to other standard metrics for this type of behaviour – i.e. P(Lick) and d-prime. These comparisons are indirectly available, but It would be better to directly compare a sessions P(Lick) and/or dprime with that session's aROC.

11) The bulk of this paper makes use of selective ablation of neurons based on their projection target, via a combination of retroAAV-Cre in the target area and AAV-Caspase3 in the source area. There are no references to existing literature regarding this method: could the authors please add some? It would also strengthen the manuscript if authors could also demonstrate the specificity of this method in at least one of two ways:

a) First, how specific is the cell death in the source location? Could the authors provide histology showing that other neurons are indeed spared? What are the consequences of the local death of a good many cells? Is the function and connectivity of other cells unaffected? (perhaps the literature could provide a hint, these new experiments would be a considerable undertaking. At the least, the potential effects should be discussed). When the authors describe the “lesion” of CT and CSt, is it a lesion in the same sense as the VC lesions? Perhaps “ablation” is a better word and does more justice to the method. It would be good to see Caspase-only (no Cre) controls, in addition to the Cre-only controls. Does VC remain healthy? Note the concentrations of the virus used are not described in the Materials and methods.

b) Second, how accurate are the target site injections? It would be good practice to provide histology confirming accurate targeting of the SC and dmStriatum. I.e. please confirm that CT cells are projecting to the superior colliculus and the CSt cell are indeed projecting to the striatum.

12) Regarding the silencing result in Figure 5B, it seems as though the CT lesion has affected baseline performance, which seems at odds with the previous Figure 3. Or is the performance at 100% contrast the same? Can the authors test this? The authors suggest that removal of the CT neurons “strongly reduces the impact of VC”. Could the authors put the stats test into the figure here? A paired comparison of all the detection thresholds? Or perhaps copy the curves from 5A into 5B (but dashed)? There is still a reduction in aROC with VC silencing post CT lesion at all datapoints, and this is particularly strong at 100% contrast, where previously there was no effect of silencing. What could the reasons for that be? I think this figure needs to be more clearly explained in the text, it is not as straightforward as it is currently described.

13) The question of what causes this additional reduction leads to the next comment. The 1P silencing was only performed in the context of CT neurons, which raises the question of whether this modulation or sensitivity-enhancement is specific to only this cell type. 1P silencing of the entire VC also shows a similar behavioural effect – is that thought to be predominantly through the action of CT cells? It would be very intriguing to see what the impact of transient silencing does when there are no CSt cells for example.

14) The authors describe the visual stimulus as circular sinusoidal drifting grating displayed on the monitor to capture 30 degrees of the mouse visual field. In the Results section, they write that "a computer monitor was placed to the left visual field of the animal". Yet, it is unclear where exactly the stimulus is in the visual field of the mouse, and whether it is presented only in the left visual field. This needs to be clearly specified as it looks like (although not stated) the viral injections are done unilaterally, and therefore effects on visual performance may vary in the two halves of the visual field (right vs. left). Importantly: where exactly are the cortico-fugal neurons located? The authors state they were mostly found in L5 but do not provide information on exact cortical area (V1 only, other cortices?). Do cortical lesions via viral injections always affect the entire cortical area that corresponds to the retinotopic location of the visual stimulus?

Moreover, the authors use a full field drifting grating stimulus for the experiment depicted in Figure 5 (I assume same is true for Figure 6, although not stated in the Materials and methods). They do not describe the size of the stimulus (in visual degrees) and its exact location in the mouse visual field, and whether it spreads both the left and the right fields. This information can affect the interpretation of the results.

15) Please flesh out the discussion of the roles of the striatum and the superior colliculus, to provide a bit more context, on what is already known of these structures and why they are important to consider in this task. Having these brief discussions will also allow the reader to appreciate the findings a bit more clearly. I.e. it is obviously not novel that the striatum is required for learning (nor is this what the authors claim), so therefore it is not surprising that projections to the striatum are also required for learning. What we learn from this study is that VC provides the most valuable information to striatum, even though it could have come from other sources. Likewise, it is known that SC can subserve a visual task in the absence of V1, though not completely. However, this study suggests that the major influence of VC in this task is mediated through the SC. (though see previous comments on this). In sum, please provide brief summaries with appropriate references to allow readers to position and appreciate these new findings in the existing literature.
