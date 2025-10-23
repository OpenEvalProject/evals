# Author response - Round 1

Authors:
- Eugenio Manassero
- Giulia Concina
- Maria Clarissa Chantal Caraig
- Pietro Sarasso
- Adriana Salatino ([ORCID: 0000-0002-2471-7212](https://orcid.org/0000-0002-2471-7212))
- Raffaella Ricci
- Benedetto Sacchetti ([ORCID: 0000-0002-8695-8310](https://orcid.org/0000-0002-8695-8310))

## Response text

DOI: [10.7554/eLife.85951.sa2](https://doi.org/10.7554/eLife.85951.sa2)

Essential revisions (for the authors):

Reviewer #1 (Recommendations for the authors):The suggestions that I'd like to present here build on the concerns I have raised in the public review, along with some further suggestions to generally strengthen the manuscript.

– Pre-processing should be in line with accepted standards in the fear conditioning field: Start out to range correct each individual SCR datapoint (and clarify what exact value (e.g., average, maximum) of the US during acquisition is used to do so). Differences scores with a preconditioning phase are very uncommon, and also not necessary when a comparison with the acquisition data is being made in the main analyses. No matter what, only as a final step, should the data be square root transformed.

We would like to thank the Reviewer for raising this important point. To align our data analysis with the accepted standards in the fear conditioning field, we re-analyzed our data starting by range-correcting each participant’s SCR raw data point, dividing it by the same participant’s average US response during the conditioning phase. We finally applied a square-root transformation of each scaled data point (see Methods section).

As usefully suggested, we have also analyzed the responses elicited by the CS during the conditioning phase and we then processed them in the same manner. In line with previous studies in the same field (Raij et al., 2018), the trials in which the US shock was delivered (12 out of 15 trials) were excluded to avoid artifacts/confounds induced by the electric shock itself. Therefore, the remaining 3 out of 15 trials were analyzed. The data we obtained (with a sample of n = 21 participants) were not normally distributed, preventing us from running the suggested omnibus ANOVA analysis. Thus, we reasoned to perform a new power analysis and repeat the experiments to reach a sample width of n = 30 (for the aPFC ) Throughout the manuscript, we have changed the denomination of the medial prefrontal cortex (mPFC) with the term “medial anterior prefrontal cortex” (aPFC, anatomically corresponding to the medial portion of the Brodmann area 10, BA10) in accordance with the suggestion of the Reviewer 2., sham, OC, and dlPFC groups. With this sample width, we reached a normal distribution of the data and we were able to perform the suggested analyses.

– The main analyses should incorporate a within-subject factor of Time (pre and post intervention), possibly also with the within-subject factor Trial Number (e.g., the last 4 trials of acquisition and the four test trials) such that an omnibus test can be performed to assess whether there is an interaction with Time and Group (and or Trial Number). If so, this can be followed-up with relevant planned contrasts investigating whether fear is significantly reduced in the mPFC group, and whether the DIFFERENCE in fear reduction is higher in the mPFC group as compared to such difference scores in the other groups.

Thank you for this useful suggestion. After preprocessing the data as indicated in the previous point, we ran omnibus 2 × 2 mixed ANOVAs by incorporating a within-subject factor of Time/Phase (pre- and post-intervention) both in the case of the test (i.e., conditioning vs test) and the follow-up (i.e., conditioning vs follow-up). Therefore, we included in the omnibus analysis the averaged SCRs level evoked by the CS during these phases. These analyses allowed us to assess whether there was an interaction with Time/Phase and Group, and to run relevant planned contrasts accordingly. By singularly comparing the aPFC group with all the other conditions (sham, OC, and dlPFC) we were able to observe that the CS-elicited fear was significantly reduced in the aPFC group (both in the test and the follow-up phases) relative to the conditioning phase. This dampening effect from the acquisition phase was selective for this region and thus was not observed in all the other groups.

– The generalization analyses should consist of the within subject factor Stimulus Type (CS, NS1, NS2) and between subject factor Group. Again, only in the case of a significant omnibus test, these should be followed up by relevant planned comparisons.

Thank you for this indication. We performed the suggested analysis by running 2 × 3 mixed ANOVAs with a within-subject factor of Stimulus Type/Tone (CS, NS1, and NS2) and a between-subject factor of Group (aPFC vs sham, aPFC vs OC, and aPFC vs dlPFC). This approach led to the confirmation of the previous findings that, during the test session, rTMS over the aPFC significantly decreased the defensive responses to all the stimuli (CS, NS1, and NS2) relative to the sham condition (we found a significant main effect of Group and no Group × Tone interaction effect), supporting a dampening effect of threat generalization processes. Finally, we confirmed the previous finding that the difference between the aPFC group and the dlPFC group pertaining to rTMS effects was selective for the CS, and no between-group differences were observed for defensive reactions to the NSs.

– Very important: to increase transparency and credibility, ideally, the paper should adopt a complete open science approach: the raw data along with the code to arrive at results should be openly accessible. The acquisition data should also be presented in graphs, both with all trials and the relevant averages that are chosen to compare for the pre-post intervention effect.

We agree with the Reviewer about the importance of transparency. To this aim, the raw data of this study have been uploaded along with the manuscript files. The methodological procedures to arrive at results have been detailed in the Methods section (“Psychophysiological recording and analysis” and “Statistical analyses” subsections).

– Generally, the factors and their levels of performed ANOVAs should always be reported.

As suggested, we always reported the factors and levels of performed ANOVAs in the Results section.

– Pay attention to using consistent numbers after the comma's, this currently varies widely.

Thank you for this advice. We have corrected the values throughout the manuscript, to uniform them with three numbers after the commas.

– For transparency, always report the exact p-value (so not p>0.05)

Thank you also for signaling this point. As recommended, we reported the exact p-value throughout the manuscript, also for the non-significant cases.

– To strengthen the theoretical framework of the paper, the rationale to include the explicit memory tests as well as a substantiation of the hypotheses should be included in the introduction. Also, a clear and substantial reasoning behind the inclusion of the generalization tests is required. It is now after the fact, but preregistration of the hypotheses and analytical approach would have been a major plus. Currently is seems a bit as if the study was actually set-up as some sort-of reconsolidation intervention. I am saying this because the introduction is oblivious as to per what mechanism could mediate the long-term effects of the intervention, if not extinction of reconsolidation. So a clear reasoning why the long-term test was implemented and why the authors hypothesize what they hypothesize should be added. For future studies, preregistration is highly recommended.

Thank you for these useful indications. As suggested, in the Introduction section we added the rationale to include the explicit memory test and a generalization test, the reasons to implement the long-term test, and the experimental hypotheses.

– The discussion (which is currently already interesting) could reflect more on what mechanisms may be behind the long-term effect, and how the absence of any effects of the explicit memory tests should be interpreted. A critical reflection on what exact theoretical constructs these tests represent is also required.

Also in this case, we added in the Discussion section a reasoning about the potential mechanisms mediating the long-term effect, the absence of any effects on the explicit memory, and the theoretical constructs that these tests represent (see also the Methods section).

Reviewer #2 (Recommendations for the authors):

– Labeling all areas in the midline of the prefrontal cortex 'medial prefrontal cortex' might not be wrong, but lumping those very different regions together as a homogeneous functional entity can be a bit off-putting to those who consider anatomy important. Perhaps the authors can be more precise in their nomenclature throughout the manuscript.

The Reviewer is completely right about this point. To more precisely denominate the prefrontal target of our rTMS procedure, throughout the manuscript, we corrected “medial prefrontal cortex” (mPFC) with “medial anterior prefrontal cortex” (aPFC). Indeed, the coil placement that we adopted (i.e. over Fpz according to the international 10‒20 EEG coordinate system) directly focused on the medial portion of the BA 10.

– I would suggest to plot the SCR timeseries in addition to the deviation from baseline. That would also give insight into the amount of change caused by the TMS protocol.

Giving insights into the amount of change caused by the rTMS protocol is certainly of great importance. To this purpose, we have now added within-group comparisons (through 2 × 2 mixed ANOVAs) that show, for each group, the amount of change in CS-evoked SCRs from the conditioning phase to the test phase, as well as from the conditioning phase to the follow-up phase. Furthermore, to directly and simply depict these changes, in addition to dot plots, we have also represented them with line charts (Figures 2C, 2H, 4C, 4H, 5C, 5H).

– The sentence starting at lines 32-33: "in this scenario…" is quite difficult to understand, perhaps consider revising it.

Thank you. We have removed this unnecessary sentence.

– Lines 93-95 is quite confusing, for a moment I thought the authors were going to assess the potential distal effects of TMS, which did not happen. Consider keeping this for the discussion

Thank you. We have moved this part to the Discussion section.

– On several instances the authors equate a non-significant effect to effects being the same e.g. line 109-110: "there the CS evoked similarly strong autonomous reactions (P > 0.05) (Figure 2A)." That is not really what you can conclude from such an analysis as you do not test how similar these effects are. Additionally, it would be good to give the exact p-value and t-statistics for readers to judge how not different these effects are.

Thank you for this revision. We have corrected all the sentences like the one above-mentioned, and we have reported the exact p-value and statistics for non-significant comparisons throughout the manuscript.

– Consider adding simulations of the TMS effects on the neural tissue. That will make it easier for non-experts in TMS to judge the success of your manipulation.

Thank you for this interesting suggestion. We have performed simulations of the rTMS effects on the neural tissue of the medial anterior prefrontal cortex, the left occipital cortex, and the left dorsolateral prefrontal cortex. The simulations have been performed with SimNIBS 4.0 software, and they have been included in the main figures (Figure 2A, Figure 4A, and Figure 5A).

– It is not clear to me why the authors shift back to context A in their third session, is there a rationale for that?

The rationale behind the context shift between the second session (context B) and the third session (context A) consisted of testing potential renewal effects. Indeed, a return of fear following extinction training is often caused by a change of context, due to the fact that extinction learning is context-dependent (Vervliet et al., 2013). Therefore, we sought to test whether rTMS (delivered in context B) may induce enduring effects, observable even during a re-exposition to the original threatening environment (context A). To better clarify this point, we have included more explanations in the Introduction section, the Results section, and the Discussion section.

– Why is the time for the peak-to-trough deflection different for US2 as compared to the CS and US?

The reason why the time for peak-to-through deflection is different for the US2 compared to that of the other stimuli (CS, NSs) relies on the different duration of the selected stimuli (6s for the CS/NSs and 4s for the US2). Since we considered as event-related the SCRs in which the trough-to-peak deflection started at least 1s from the onset and before the offset of each stimulus, then the time window in which an event-related deflection had to begin was 1–6s (for the CS and the NSs) or 1–4s (for the US2) after the stimulus onset.

[Editors’ note: what follows is the authors’ response to the second round of review.]

The manuscript has been improved and the addition of control experiments has many of the concerns raised by reviewer 2 who has no further comments. However, there are some remaining issues related to the SCR data handling and reporting that need to be addressed. Reviewer 1 provides valuable concrete suggestions for analyses (analysing SCR data from all acquisition trials, bonferroni correction where appropriate) and reporting (discussing limitations related to efficacy of threat conditioning, the lack of a control stimulus CS-, failing generalisation manipulation that makes it unwarranted to claim that the intervention targeted generalization). An important possibility that needs to be discussed is that the effects reflect a general dampening effect on seeing any kind of stimulus (that is not aversive in itself).

Reviewer #1 (Recommendations for the authors):

The authors have revised the manuscript substantially, and the result certainly has improved. The revised version is clear, nuanced, and the contribution of the manuscript to the literature is evident. Some final considerations and concerns to reflect on to further improve the manuscript.

We would like to thank the Reviewer for the time and effort spent in carefully evaluating the revised version of the manuscript, and we are happy to read this recognition of our work. Thank you also for these useful considerations that you provided, which have been all addressed as follows:

- In the intro it would be good to add a clear and explicit rationale for the inclusion of the explicit memory test and the generalization test.

As suggested, we added in the Introduction (lines 38-41) a rationale for including the explicit memory test as well as the generalization test.

– Please also analyse the SCR data from ALL acquisition trials and add its graph on a trial-by-trial basis, this is the best way to assess any possible pre-existing learning differences for the groups.

Thank you for this important suggestion. As requested, we have analyzed the CS-related SCR data during the acquisition phase on a trial-by-trial basis ‒including both the 15 trials of the conditioning procedure separately as well as their average in the graphs (see Figure 2-S1, Figure 4-S1, and Figure 5-S1). Collectively, we found no differences in how the aPFC group responded relative to the sham, the OC, and the dlPFC groups, allowing us to exclude potential pre-existing learning differences between groups. These analyses have been included in the Results section, highlighted in yellow.

– One concern I have is the lack of a control stimulus (CS-) during acquisition: as such it is challenging to reveal whether conditioning was effective in the first place. In this light it is also concerning that the SCR values seem very low.

We thank the Reviewer for raising this important point. As we mentioned in the Results section (lines 101-102), we chose to adopt a single-cue conditioning protocol ‒instead of a differential conditioning procedure‒ because it more ecologically reflects real-life traumatic experiences. It is true that the consequent lack of a control stimulus (CS-) make it more challenging to reveal the efficacy and precision of the conditioning. However, one possibility to observe the efficacy of fear learning may consist of comparing the CS-evoked SCRs of the sham control group before the conditioning (preconditioning phase), during the conditioning, and after the conditioning (implicit test). In this way, it has been possible to observe a progressive enhancement of the magnitude of the autonomic responses through these three experimental phases. With the same logic, the aPFC group showed an enhancement of SCRs from the preconditioning to the conditioning phase, but a following decrease of SCRs after the rTMS procedure (during the implicit test) which restored the magnitude of CS-related responses to preconditioning levels.

– Please confirm that the shock electrodes were attached during the test phases and indicate so in the manuscript.

We confirm that the shock electrodes were attached during all the test and follow-up phases, and we have added this specification also for the US2 test and the perceptual test in the Methods section (lines 521-522 and 550), which were previously missing.

– It is unclear what tests were Bonferroni corrected and which ones were not (and why), this should be done consistently.

We confirm that we had performed Bonferroni-corrected tests throughout the manuscript, and now we have included this specification for all the post-hoc comparisons in the Results section. We apologize for the previous omission.

– The unit of SCR on some of the y-axes is lacking. On some other graphs it is the root of mS. The unit applied should be consistent across all graphs. In the graphs, also the relevant planned comparisons that are NS should be indicated.

We thank the Reviewer for bringing this issue to our attention. As requested, we have corrected the y-axes of the graphs and now the unit is consistent across all graphs. In the supplementary figures (Figure 2-S1, Figure 4-S1, and Figure 5-S1) we have also corrected the analysis of the CS-preconditioning (panel A) by processing the raw SCR data in the same way as all the other SCR data of the manuscript (in the previous version they were only square-rooted). The corrected analyses have been highlighted in yellow in the Results section. Furthermore, we have indicated also the relevant non-significant planned comparisons in the main figures.

– The lack of a main effect of tone in the generalization phase indicates that the generalisation manipulation itself did not work. This needs to be flagged in the relevant analyses and critically discussed in the Discussion section. For one thing, it does not allow the conclusion that the intervention targeted generalization. Consequently, one may wonder whether the effect (at least the immediate one, the follow-up test is another story) is mediated by memory at all, or whether it involves a more general dampening effect on seeing any kind of stimulus (that is not aversive in itself).

The Reviewer is absolutely right in raising this important point. Autonomic reactions that we observed towards the new tones in the aPFC group relative to the sham control group did not allow the conclusion that the rTMS intervention targeted threat generalization, leaving open the question of the specificity of rTMS effects (mediated by memory or more general dampening effect). However, the lack of between-group differences that we observed in the autonomic responses to the US2 seems to suggest that the observed effect may be memory-related and not due to a general dampening of autonomic reactivity. We added this reasoning in the Discussion section (lines 340-344).
