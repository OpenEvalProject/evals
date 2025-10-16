# Peer review - Round 1

Editors:
- Saskia Haegens, Columbia University College of Physicians and Surgeons United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66761.sa0](https://doi.org/10.7554/eLife.66761.sa0)

The authors used a clever design, in which adolescents and adults learned to juggle, to study the impact of sleep and associated oscillations on the consolidation of motor memory across age groups. Overall, the topic and the results of the present study are interesting and timely, and extends previous findings in the declarative memory domain to the motor memory domain.


---

# Peer review - Round 1

Editors:
- Saskia Haegens, Columbia University College of Physicians and Surgeons United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66761.sa1](https://doi.org/10.7554/eLife.66761.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Slow oscillation-spindle coupling strength predicts real-life gross-motor learning in adolescents and adults" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Overall, the topic and the results of the present study are interesting and timely, and we appreciate the use of a more ecologically valid paradigm. However, several aspects of the analyses need further clarification, and critically, a question was raised as to whether this is a sleep story or a circadian rhythm story.

Essential revisions:

1. The results may first and foremost tell a circadian (rather than sleep) story. Examining the data in Figure 2A and 2B, it appears that every AM learning period has a higher learning curve (slope) than every PM period. While this could, of course, be due to having just slept, the main story gleaned from such a result is not a sleep effect on retention, which has been the emphasis in motor memory consolidation research in the last couple of decades, but on new learning. The fact that this effect appears present in the first session (juggling blocks 1-3 in adolescents and blocks 1-5 in adults) makes this seem the more likely story here, since it has less to do with "preparing one to re-learn" and more to do with just learning and when that learning is optimal. But even if it does not reach statistical significance in the first session alone, it remains a concern and should be considered a focus in the manuscript unless the authors can devise a reason to definitively rule it out. The authors should include all sessions from all subjects into a mixed effect model, predicting the slope of the learning curve with time of day and age group as fixed effects and subjects as random effects:

learning curve slope ~ AM/PM [AM (0) or PM (1)] + age [adolescent (0) or adult (1)] + (1|subject)

…or something similar with other regressors of interest. If this is significant for AM/PM status, they should re-try the analysis using only the first session. If this is significant, then a sleep-centric story cannot be defended here.

2. Related: The sleep data of all participants (thus from both sleep first and wake first) were used to determine the features of SO-spindle coupling in adolescents and adults. Were there any differences between groups (sleep first vs. wake first)? This might be interesting in general but especially because only data of the sleep first group entered the subsequent correlational analyses.

3a. Supporting and extending previous work of the authors (Hahn et al., 2020), SO-spindle coupling over centro-parietal areas was stronger in adults as compared to adolescents. Despite these differences in the EEG results the authors collapsed the data of adults and adolescents for their correlational analyses (Figure 4a and 4b). Why would the authors think that this procedure is viable (also given the fact that different EEG systems were used to record the data)?

3b. If the authors believe it is justified to combine these groups, Figure 3 and 4 should be combined and some current figure panels in Figure 3 should be removed or moved to the supplementary information.

4. The authors might want to explicitly show that the reported correlations (with regards to both learning curve and task proficiency change) are not driven by any outliers. It would be useful to know if the relationship is significant with Pearson correlations when robust regression is applied.

5. With only a single night of recording data, it is impossible to disentangle possible trait-based sleep characteristics (e.g., Subject 1 has high SO-spindle coupling in general and retains motor memories well, but these are independent of each other) from a specific, state-based account (e.g., Subject 1's high SO-spindle coupling on night 1 specifically led to their improved retention or change in learning, etc., and this is unrelated to their general SO-spindle coupling or motor performance abilities). Clearly, many studies face this limitation, but this should be acknowledged.

6. The authors used a partial correlation analysis to rule out that age drove the relationship between coupling strength, learning curve and task proficiency. It seems like this analysis was done specifically for electrode C4, after having already established that coupling strength at electrode C4 correlates in general with changes in the learning curve and task proficiency. The claim that results were not driven by age as confounding factor would be stronger if the authors used a cluster-corrected partial correlation in the first place (just as in the main analysis).

7. To allow a more comprehensive assessment of the underlying data information with regards to general sleep descriptives (minutes, per cent of time spent in different sleep stages, overall sleep time etc.) as well as related to SOs, spindles and coupled events (e.g. number, density etc.) would be needed.

8. The authors state that "To ensure the simultaneous presence of the two interacting sleep oscillations in the signal, we restricted our analyses to NREM3 sleep given the higher co-occurrence rate." We do not understand this reasoning. The utilized procedure of specifically isolating sleep spindles that are followed or preceded by slow oscillations already ensures the presence of SOs and sleep spindles in the data. Hence, why not take coupled events from sleep stage N2 into account? Or do the authors think that light sleep SO-spindle events are qualitatively different from SWS SO-spindle complexes (and if so does the present data support such a notion)?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Slow oscillation-spindle coupling strength predicts real-life gross-motor learning in adolescents and adults" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The authors have done an impressive job with this revision. It is meticulously organized, thorough, and clearly stated. That is all to their major credit. However, I still cannot come to agree that their data supports much of the story they are telling.

First, part of the issue may be the change from their original story and the new one following the revision. Making major revisions can obviously be tricky, especially when a revision requires as many changes as theirs did (and I again commend them on the overhaul). But there is still something unclear in their primary claims. They say in their cover letter, "Collectively, our results suggest that SO-spindle coupling indexes the integrity of memory pathways (as reviewed in detail recently: Helfrich et al., 2021); thus, reflects a trait-specific (in contrast to a state-specific) correlate of learning capacity." However, this story does not come through clearly in the new paper. In fact, reading the new paper, it seems this is nodded to only here in the Discussion – "Thus, our results primarily suggest that strength of SO-spindle coupling correlates with the ability to learn (trait), but does not solely convey 534 the recently learned information. This set of findings is in line with recent ideas that strong coupling indexes individuals with highly efficient subcortical-cortical network communication (Helfrich et al., 2021)." Much of the paper instead talks about active systems consolidation theory, which I believe is not supported in their data, and the authors do seem to agree. If the authors indeed want to make this more of a memory pathway integrity story, it seems more unpacking of the ideas in their recent review is warranted, as does perhaps some evidence in the literature linking sleep measures to integrity in some neural pathways (e.g., Mander et al., 2017).

Second, they concede in various locations that the circadian story cannot be ruled out, which I also commend, but then the paper still largely revolves around active sleep consolidation theory. I invite the authors to imagine convincing a hypothetical researcher who thought the brain just shuts off entirely during sleep ("sleep does nothing") and that people have different abilities based on the time of day. (Believe it or not, this is not my belief.) How would the authors convince this person based on these behavioral data that sleep is actually doing something? I do not know whether they could, given the mixed-effects model findings.

Of course, they could point to the prior literature. The prior literature on sleep and motor learning has shown, in the case of the Morita juggling studies cited, that there should be better overall performance after sleep (vs equivalent wake periods). And in the case of countless finger-tapping studies, even though the major story has changed from one of absolute improvement (e.g., Walker et al., 2002) to stabilization (e.g., Brawn et al., 2010) after sleep, there seem to be sleep (vs wake) benefits on overall performance (analogous to task proficiency here). This, however, is not what the authors find with their learning curve findings here, as performance seems, if anything, worse on the first few trials after sleep (though this may not be significant) and then catches up more quickly. So, it is hard to know whether the prior literature would necessarily help them convince this researcher about their own findings.

This researcher may also say that the inclusion of a PVT is great, and the null results across sessions is more helpful than not to their story. But this researcher may add that a null PVT difference does not exclude all possible circadian effects. There are certainly circadian effects on cognition – including the very recent publication of Tandoc et al., (2021) and even on motor learning (Keisler et al., 2007) – and indeed the authors do find such an effect here in their mixed-effects model analysis. Therefore, the null PVT results are not conclusive, especially in counteracting an effect that they actually found in their paper.

One could then point this researcher to the SO-spindle coupling results as evidence that sleep is playing a strong role here. However, given that these are trait- vs. state-based results, it is unclear why stronger SO-spindle coupling for some individuals – which may be having an impact on neural integrity over a long timescale – would prime their nervous systems for more learning right after sleep than at some other time during the day. The researcher may say, okay, SO-spindle coupling results do not prove sleep does anything, they merely correlate with the observed behavioral result, and moreover, they constitute a trait (vs post-learning sleep state) effect. They may add that it is also unclear why, if stronger SO-spindle coupling is doing something, it could not alternatively reflect some other individual trait that could even lead to the observed circadian effects that learning curves are higher in the morning.

One analysis that could possibly work to disentangle circadian vs. active sleep effects would be to include a different factor in the mixed-effects model that could tease apart time of day from sleep-after-learning effects. In addition to including “Time of day”, where all mornings = 1 and all evenings = 0, the authors could include the conjunction of “Time of day + after learning”, where mornings on the 2nd and 3rd sessions = 1 and mornings on the 1st session and all evenings = 0. This would capture the idea that post-learning mornings show differential improvement because post-learning sleep sort of “prepared” the networks to re-learn within a short time span, and this preparation was not operative before the 1st session. I say it could “possibly” work above because the two factors would still be quite correlated (identical except for the first morning session), which could hurt their statistical power to independently produce effects. Nevertheless, if BOTH factors end up being significant, I think the authors could make the claim that both are contributing (that is, time of day + after learning is actually independently contributing above and beyond what time of day could do alone). If only one is significant, then the story is clean, but may have to change. If neither are significant, then it may be difficult to know what to do, and the authors may have to fall back on the original time-of-day analysis and keep things closer to as is but acknowledge more of the uncertainty surrounding the effects. If nothing changes upon a second revision in this regard, I do expect the authors to incorporate circadian possibilities more thoroughly in their paper, such as in their abstract and with more citations of this literature.

I realize this may seem a lot for a second round of revisions, and the authors have clearly done an impressive amount of work on the paper, but I feel that the authors can still strengthen it, either with this last analysis or by refocusing on the stories that can and cannot be supported here. There is something here that lacks clarity in translating from the data to the story about them, and, as a result, it remains difficult to confidently find the main takeaway from the manuscript.
