# Effects of dopamine on reinforcement learning and consolidation in Parkinson’s disease

## Authors

- John P Grogan<sup>1</sup> ([ORCID: 0000-0002-0463-8904](https://orcid.org/0000-0002-0463-8904)) †
- Demitra Tsivos<sup>2</sup>
- Laura Smith<sup>1</sup>
- Brogan E Knight<sup>2</sup>
- Rafal Bogacz<sup>3</sup>
- Alan Whone<sup>1</sup>
- Elizabeth J Coulthard<sup>1</sup> †

### Affiliations

1. Institute of Clinical Neurosciences, School of Clinical Sciences University of Bristol Bristol United Kingdom
2. Clinical Neurosciences North Bristol NHS Trust Bristol United Kingdom
3. MRC Brain Network Dynamics Unit, Nuffield Department of Clinical Neurosciences University of Oxford Oxford United Kingdom

† Corresponding author

## Abstract

10.7554/eLife.26801.001 Emerging evidence suggests that dopamine may modulate learning and memory with important implications for understanding the neurobiology of memory and future therapeutic targeting. An influential hypothesis posits that dopamine biases reinforcement learning. More recent data also suggest an influence during both consolidation and retrieval. Eighteen Parkinson’s disease patients learned through feedback ON or OFF medication, with memory tested 24 hr later ON or OFF medication (4 conditions, within-subjects design with matched healthy control group). Patients OFF medication during learning decreased in memory accuracy over the following 24 hr. In contrast to previous studies, however, dopaminergic medication during learning and testing did not affect expression of positive or negative reinforcement. Two further experiments were run without the 24 hr delay, but they too failed to reproduce effects of dopaminergic medication on reinforcement learning. While supportive of a dopaminergic role in consolidation, this study failed to replicate previous findings on reinforcement learning. DOI: http://dx.doi.org/10.7554/eLife.26801.001

## Introduction

Phasic changes in dopamine level are believed to encode the reward prediction error (RPE), which measures the difference between the reward expected after an action, and the reward actually received (Schultz et al., 1993, Schultz et al., 1997). In turn the RPE guides reinforcement learning (RL) such that behaviour is adapted to changing surroundings. Several studies have taken advantage of the dopaminergic depletion in Parkinson’s disease (PD) in the substantia nigra pars compacta and ventral tegmental area (Agid et al., 1989; Shulman et al., 2011). PD patients are frequently treated with dopamine replacement therapy (levodopa and dopamine agonists), and thus by comparing patients in ON and OFF medication states the effects of dopamine depletion can be investigated.

One influential study using such a procedure found that dopaminergic state modulated RL from positive and negative feedback (

![Figure 1.](https://cdn.elifesciences.org/articles/26801/elife-26801-fig1-v2.jpg)

**Figure 1.:** In each pair one card is more likely to be rewarded (shown ‘Correct’ feedback) than the other, with card A in pair AB rewarded 80% of trials, and card B on 20% of trials. For pairs CD and EF, the probabilities are 70–30% and 60–40%.DOI: http://dx.doi.org/10.7554/eLife.26801.003

PD patients chose A more and avoided B less when ON medication, and vice versa for OFF medication (Frank et al., 2004). This suggested better learning from positive reinforcement and poorer negative reinforcement ON medication, while patients OFF showed the opposite pattern. Importantly, patients OFF medication were better at negative reinforcement than healthy age-matched controls (HC), suggesting that PD actually improved some aspect of RL. The explanation for these effects was provided with a model of the basal ganglia. In the Go-NoGo model, the two main pathways from the striatum are proposed to underlie positive and negative reinforcement. The direct pathway, which is mainly activated by striatal neurons containing dopamine D1 receptors and therefore is activated by a dopamine increase during a positive RPE, underlies positive reinforcement. The indirect pathway which is inhibited by D2 receptors, and therefore activated when a dopamine decrease signals a negative RPE, allows negative reinforcement. When PD patients are ON medication, the higher dopamine levels activate D1 receptors and inhibit D2 receptors, thus biasing towards the direct pathway, improving positive reinforcement. When OFF medication, the lower dopamine levels mean less D1 activation, and less D2 inhibition, thus increasing indirect pathway activity, and improving negative reinforcement.

While this view is persuasive, some more recent studies have cast doubts on the extent to which dopamine is involved in the learning part of RL, and how much is the expression of that learning. In Frank et al. (2004) study, the RL test was given immediately after learning, and it was only in this test that the effects were seen. However, as patients were ON for both learning and testing, or OFF for both, it meant that the dopaminergic effects could have occurred at either point. One study attempted to correct for this by adding a one hour delay between learning and testing, allowing PD patients to learn OFF medication, then be tested ON medication (along with ON-ON and OFF-OFF conditions) (Shiner et al., 2012). It was found that being ON medication at the time of testing produced greater expression of positive reinforcement than being OFF, while it had no effect during learning. Additionally, RPE signals in the striatum during learning were not affected by medication state, but ventromedial PFC and nucleus accumbens signals in the test phase only tracked the value of the stimuli when patients were ON medication. This suggests that dopamine may not play as much of a role in learning, but instead influence the choices made after the expected rewards have been learnt. Other studies have also shown dopaminergic D2 receptor effects mainly on the expression rather than learning (Eisenegger et al., 2014; Pessiglione et al., 2006).

The direct link between dopamine and RL, as opposed to expression of information, was further questioned by another study, which found that dopaminergic effects could be shown even when rewards were not actually given during learning (Smittenaar et al., 2012). Participants received one of two shapes, probabilistically, after selecting a stimulus, and only after the learning trials were they told that one shape corresponded to winning money, and one to losing money. Thus, the reward/monetary associations were created separately to the stimulus-outcome associations. However, they still found that PD patients ON medication during testing (after finding out about the money), showed higher accuracy on the most rewarded stimulus, and lower accuracy on the most punished stimulus. This shows that it is possible to generate this effect without any reinforcement learning actually taking place, suggesting dopamine influences value-based decision making.

A recent extension to standard RL models offers a mechanism by which dopamine may influence expression of learning. The OpAL model (Collins and Frank, 2014) has separate learning rates and choice parameters for the direct and indirect pathways, which learn from positive and negative reinforcement, respectively. By allowing dopamine to affect the choice parameter, it can bias towards choosing the stimulus that learned mainly from the direct pathway, or from the indirect pathway, thus lending more weight to the positive or negative reinforcement the stimulus received.

In addition to evidence of dopamine affecting expression of learned values, there is also evidence of it affecting consolidation. PD patients ON medication showed an increase in accuracy on an RL task after a 20 min delay, while those OFF medication showed a large decrease (Coulthard et al., 2012). This was despite all PD patients showing the same behaviour during the learning trials. It is still possible that this is a retrieval effect, and that it was simply not seen during the learning trials as the values were still being updated, but it is also possible that the dopaminergic medication preserved the synaptic weight changes induced during learning, thus improving memory for the learned items.

This explanation ties in nicely with models of synaptic consolidation based on the synaptic tagging and capture hypothesis (Clopath et al., 2008; Frey and Morris, 1998; Redondo and Morris, 2011). In these models, early synaptic changes are induced during learning, but decay away unless actively prolonged, which is achieved by the changes setting a ‘tag’ which plasticity-related proteins (PRPs) must act on to make the changes permanent. Dopamine is hypothesised to set the threshold for the synthesis of these PRPs, so that higher levels of dopamine mean a lower threshold. Thus, PD patients OFF medication would have a higher PRP threshold, and therefore lower consolidation of early synaptic changes, leading to a delayed impairment of memory, as seen in Coulthard et al. (2012).

Here, we sought to investigate the hypotheses that:

These hypotheses were tested in experiment 1 where surprisingly we did not show the expected effects of dopamine on novel pairs choices. We undertook a further two experiments to investigate the effects of dopamine and delays on RL, and the effects of procedural changes to the PST.

## Results

## Experiment 1

## Learning

Eighteen PD patients and 18 HC learned a modified version of the PST (2 pairs, different probabilities of reward, smiling or frowning faces as feedback, see Figure 7), and were tested immediately, 30 min and 24 hr later. PD patients were ON or OFF their dopaminergic medication on day 1 during learning, and ON or OFF on day 2 for testing (4 conditions; within-subject design). No data were excluded, but the final learning blocks were missing from two conditions for the same participant due to experimenter and computer error.

Participants were able to learn the task, with final mean accuracies of 78.60% (SEM = 3.84) ON medication, 77.71% (4.16) OFF medication and 79.03% (4.67) for HC. No effects of medication (p=0.882, ηp2 =0.001), or disease (p=0.846, ηp2 =0.0004) were seen on the learning trials. We also examined win-stay lose-shift behaviour on the learning trials, but found no significant differences between groups (p>0.2; see Appendix 1 for details).

We fit variations of the Q-learning model to the participants’ data, with and without different learning rates for the different PD medication states during learning (see Appendix 2 for details). A dual learning rate Q-learning model where the learning rates did not differ by medication state provided the best fit, further suggesting that dopaminergic medication did not affect learning.

## Memory

The memory tests presented the same pairs as the learning trials, but without any feedback. The 30 min memory test data were missing from two conditions for the same patient due to experimenter and computer error.

We looked at the difference between immediate and 30 min delayed memory blocks, and between 30 min and 24 hr blocks.

![Figure 2.](https://cdn.elifesciences.org/articles/26801/elife-26801-fig2-v2.jpg)

**Figure 2.:** ON-OFF had significantly greater increases in memory score over this time than OFF-OFF (* = p=0.0106) and indeed both day 1 ON conditions (blue bars) had a mean increase in accuracy while both day 1 OFF conditions (red bars) and HC (black bars) had a decrease. Error bars are SEM. Figure 2—source data 1 shows the summary statistics.DOI: http://dx.doi.org/10.7554/eLife.26801.00410.7554/eLife.26801.005Figure 2—source data 1.Figure 2, the difference in memory scores between 30 min and 24 hr tests for each condition.DOI: http://dx.doi.org/10.7554/eLife.26801.005

## Novel pairs

The novel pairs task was given 24 hr after learning on day 2. Each possible combination of the cards was shown six times, without feedback, in a random order. The percentage of times participants chose the most rewarded card (A) and avoided the least rewarded card (B) were used as measures of expression of positive and negative reinforcement, respectively. One block of novel pairs data were missing due to computer error.

The overall accuracy on the novel pairs test showed a positive correlation with the accuracy in the final learning block (r = 0.4365, p<0.0001), which is not surprising as participants who learned the task well would be expected to perform better on the test.

A between-subjects multivariate ANOVA was run to compare PD patients against HC (

![Figure 3.](https://cdn.elifesciences.org/articles/26801/elife-26801-fig3-v2.jpg)

**Figure 3.:** There were no significant effects of day 1 or day 2 medication state (p>0.28). Error bars are SEM. Figure 3—figure supplement 1 shows the data when filtered by performance on the 80–20% pair for day 1 conditions, and Figure 3—figure supplement 2 shows the filtered day 2 conditions. Figure 3—source data 1 shows the summary statistics.DOI: http://dx.doi.org/10.7554/eLife.26801.00610.7554/eLife.26801.007Figure 3—source data 1.Figure 3, the percentages of choose-A and avoid-B selections in the experiment 1 novel pairs test.DOI: http://dx.doi.org/10.7554/eLife.26801.007

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/26801/elife-26801-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** As the filtering removed data from different participants, paired samples statistics were no longer suitable. Independent-samples t-tests showed no significant effects of day 1 medication state (df = 57, p=0.975, d = 0.0956; p=0.265, d = 0.2010), nor an effect of disease state (df = 72, p=0.315, d = 0.1269; p=0.939, 0.1169) on choose-A or avoid-B. Error bars are SEM.DOI: http://dx.doi.org/10.7554/eLife.26801.00810.7554/eLife.26801.009Figure 3—figure supplement 1—source data 1.Figure 3—figure supplement 1, percentages of choose-A and avoid-B behaviours for experiment 1 split by Day 1 condition, after data filtering.DOI: http://dx.doi.org/10.7554/eLife.26801.009

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/26801/elife-26801-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Between-subjects t-tests showed no effect of day 2 medication state (df = 57, p=0.151, d = 0.1780; p=0.928, d = 0.0061). Error bars are SEM.DOI: http://dx.doi.org/10.7554/eLife.26801.01010.7554/eLife.26801.011Figure 3—figure supplement 2—source data 1.Figure 3—figure supplement 2, percentages of choose-A and avoid-B behaviours for experiment 1 split by day 2 condition, after data filtering.DOI: http://dx.doi.org/10.7554/eLife.26801.011

We found no effects of dopaminergic state during day 1 or day 2 on expression of positive and negative reinforcement. A repeated measures ANOVA (choice * day 1 * day 2) on the PD patients’ data showed a significant effect of choice (F (1, 16)=4.692, p=0.046, ηp2 = 0.227), with avoid-B higher than choose-A overall. There were no significant effects of day 1 or day 2 medication state, or any interactions (p>0.12). This suggests that overall PD patients were better at expressing negative reinforcement, but that medication on day 1 or day 2 had no effect.

There were also no significant effects when examining individual conditions with paired t-tests for choose-A (p>0.08, α = 0.0125) or avoid-B selections (p>0.2). This suggests that neither day 1 nor day 2 medication state affected choose-A or avoid-B performance.

The data filtering used by Frank et al. (2004) was applied to the data here also. Any participants who failed the easiest choice (A vs B) on 50% or more of the novel pairs trials were assumed to not have learned the task properly, and that condition’s novel pairs data were excluded. The other conditions from the same participant could still be included if they passed the filtering. This lead to 4/18 ON-ON blocks excluded, 2/17 OFF-OFF blocks, and 3/18 for all other conditions. No significant effects of choice or medication state were seen on the filtered data (p>0.1; Figure 3—figure supplements 1 and 2).

Overall, there were no significant effects of medication or disease state, suggesting that PD and dopaminergic medication did not affect novel pairs performance on the modified PST when tested 24 hr later. As experiment 1 failed to show the expected effects of dopamine on RL, experiment 2 was run without the 24 hr delay to attempt to replicate effects of dopamine on RL when tested immediately after learning.

## Experiment 2

## Learning

Eighteen PD patients and 20 HC completed the modified PST with the novel pairs test immediately after learning. There were no memory blocks. PD patients were ON or OFF medications for both learning and testing. Participants again reached over 70% accuracy on the learning trials on average (ON: 77.01% (SEM = 3.67), OFF: 78.06% (4.04), HC: 74.69% (4.43)), and there were no effects of medication (p=0.806, ηp2 = 0.004) or disease (p=0.563, ηp2 = 0.006).

## Novel pairs

Overall accuracy in the novel pairs tests correlated positively with accuracy in the final learning block (r = 0.6686, p<0.0001). A multivariate ANOVA comparing PD patients and HC showed no effects of disease state on choose-A (p=0.285,

![Figure 4.](https://cdn.elifesciences.org/articles/26801/elife-26801-fig4-v2.jpg)

**Figure 4.:** There were no significant effects of disease state or medication condition on either selection in either experiment 2 (p>0.2) or experiment 3 (p>0.3). Error bars are SEM. Figure 4—figure supplement 1 shows the data after filtering was applied to experiment 2, and Figure 4—figure supplement 2 shows the filtered data for experiment 3. Figure 4—source data 1 shows the summary statistics.DOI: http://dx.doi.org/10.7554/eLife.26801.01210.7554/eLife.26801.013Figure 4—source data 1.Figure 4, the percentages of choose-A and avoid-B selections in experiments 2 and 3 novel pairs tests.DOI: http://dx.doi.org/10.7554/eLife.26801.013

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/26801/elife-26801-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Independent-samples t-tests showed no significant effects on choose-A or avoid-B for disease state (df = 47, p=0.361, d = 0.2768; p=0.126, d = 0.4681) or medication state (df = 30, p=0.473, d = 0.2575; p=0.825, d = 0.0792). Error bars are SEM.DOI: http://dx.doi.org/10.7554/eLife.26801.01410.7554/eLife.26801.015Figure 4—figure supplement 1—source data 1.Figure 4—figure supplement 1, percentages of choose-A and avoid-B behaviours for experiment 3, after data filtering.DOI: http://dx.doi.org/10.7554/eLife.26801.015

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/26801/elife-26801-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Independent-samples t-tests showed no effects of disease state (df = 31, p=0.509, d = 0.2465; p=0.926, d = 0.0345) or medication state (df = 20, p=0.579, d = 0.2415; p=0.555, d = 0.25658). Error bars are SEM.DOI: http://dx.doi.org/10.7554/eLife.26801.01610.7554/eLife.26801.017Figure 4—figure supplement 2—source data 1.Figure 4—figure supplement 2, percentages of choose-A and avoid-B behaviours for experiment 2, after data filtering.DOI: http://dx.doi.org/10.7554/eLife.26801.017

## Experiment 3

As experiment 2 did not replicate the findings of Frank et al. (2004), an exact replication was run to ensure we observed the well-described effect of dopamine enhancing positive reinforcement or impairing negative reinforcement.

## Learning

Eighteen PD patients and 18 HC completed the original PST (Frank et al., 2004). PD patients were ON or OFF for both learning and novel pairs test. Neither PD nor medication state significantly affected the number of blocks completed (ON: 4.78 (0.59), OFF: 5.28 (0.50), HC: 5.94 (0.42); PD: p=0.145, ηp2 = 0.040; medications: p=0.477, ηp2 = 0.030) or the final learning accuracy (ON: 61.94% (3.35), OFF: 61.67% (3.26), HC: 57.22% (3.97); PD: p=0.291, ηp2 = 0.021; medications: p=0.950, ηp2 = 0.0002). Note that the final learning accuracies were lower than in experiments 1 and 2.

## Novel pairs

Again, overall accuracy in the novel pairs test correlated positively with the accuracy in the final learning block (r = 0.4680, p=0.0004). PD patients did not differ from HC on either choice (p=0.940, ηp2 = 0.0001; p=0.577, ηp2 = 0.006). Paired-samples t-tests showed no significant differences in choose-A (p=0.363, d = 0.2573) or avoid-B selections for the two medication conditions (p=0.968, d = 0.0132), meaning dopaminergic medication state didn’t affect positive or negative reinforcement in PD patients (Figure 4b). Data filtering excluded 8/18 ON blocks, 6/18 OFF blocks and 7/18 HC blocks, and no significant effects of disease or medication were seen in the remaining data (p>0.5; Figure 4—figure supplement 2).

It should be noted that participants were only just above chance performance on the novel pairs task in experiment 3, with mean percentage of choices between 49% and 57% for all groups. This is lower than in experiments 1 and 2, suggesting that the original PST was harder for participants to learn.

## General results

## Learning

As each experiment provided related statistics of learning, they were analysed together to get the full picture. A univariate analysis was run on the final learning block accuracies for each experiment (

![Figure 5.](https://cdn.elifesciences.org/articles/26801/elife-26801-fig5-v2.jpg)

**Figure 5.:** Experiment 3’s final accuracy was significantly lower than experiments 1 and 2’s (p<0.000001). Error bars are SEM. Figure 5—source data 1 shows the summary statistics.DOI: http://dx.doi.org/10.7554/eLife.26801.01810.7554/eLife.26801.019Figure 5—source data 1.Figure 5, the mean final learning block accuracies across the three experiments.DOI: http://dx.doi.org/10.7554/eLife.26801.019

## Novel pairs

A multivariate ANOVA was run on choose-A and avoid-B from each experiment. ON and OFF in experiments 2 and 3 were treated the same as ON-ON and OFF-OFF from experiment 1. There were no significant effects of condition on either choice (p=0.609,  ηp2 = 0.014; p=0.583, ηp2 = 0.015), but were significant effects of experiment on avoid-B (F (2, 188)=16.069, p<0.000001, ηp2 = 0.146). Bonferroni-corrected post-hoc tests showed that experiment 3 had lower avoid-B than experiments 1 (p=0.000005) and 2 (p=0.000013), while experiments 1 and 2 did not differ (p=1). There was no effect of experiment on choose-A performance (p=0.327, ηp2 = 0.012), and no interaction of experiment and condition for either choice (p=0.556, ηp2 = 0.016; p=0.749, ηp2 = 0.010).

This means that experiment 3 had poorer final learning accuracy (despite passing the accuracy thresholds) and less avoid-B choices on the novel pairs test, than experiments 1 and 2 which used the modified-PST. Interestingly, this was because experiments 1 and 2 had avoid-B scores higher than choose-A, while experiment 3 had about the same scores.

## Discussion

These experiments found that dopaminergic medication during learning prevented a decrease in memory for RL over 24 hr. However, dopamine did not affect expression of positive or negative reinforcement either during learning or testing, when tested immediately or 24 hr after learning. PD patients did not differ from HC in any of the experiments. Finally, experiment 3, using the original PST, had much lower accuracy in the learning trials, and lower avoid-B scores than experiments 1 and 2 which used the modified-PST.

## Effects of dopamine on consolidation

Dopaminergic medication seemed to affect memory performance on the PST. When patients were OFF medication on day 2, being ON medication the day before (during learning) prevented a decrease in their memory over the 24 delay. Interestingly, both day 1 ON conditions had a pattern of a slight increase in memory scores (albeit non-significantly different to zero), while both day 1 OFF conditions (and HC) showed a decrease on average. As this score was the difference between 30 min and 24 hr delay tests, it suggests that day 1 dopamine improved consolidation of the learned values sometime after 30 min, preventing a decay in the memory. This is in line with a previous study showing a benefit of dopamine at the time of learning on memory testing 20 min later (Coulthard et al., 2012), although it was only seen at longer delays here.

All PD patients went back ON medication immediately after the day 1 session regardless of day 2 condition, so all patients were in an ON state for the hours after learning (see

![Figure 6.](https://cdn.elifesciences.org/articles/26801/elife-26801-fig6-v2.jpg)

**Figure 6.:** Blue is when patients were ON medication, red hatched bars when they were OFF, and yellow bars the PST phases. In order for patients to be fully OFF medication during testing, they were withdrawn from their dopaminergic medications a minimum of 15 hr prior to testing (>24 hr for long-lasting medications). Note that in all conditions, patients were ON medication for a few hours after the day 1 session, to minimise the time spent OFF medication.DOI: http://dx.doi.org/10.7554/eLife.26801.020

This finding fits with the wider literature implicating dopamine in memory and consolidation mechanisms (Lisman et al., 2011; Shohamy and Adcock, 2010). Dopamine given before or after learning can improve consolidation (Bernabeu et al., 1997; de Lima et al., 2011; Furini et al., 2014; Péczely et al., 2016; Rossato et al., 2009), although there is still debate on the time course of its effects. Synaptic tagging and capture models suggest dopaminergic effects would take place within a few hours of learning (Clopath et al., 2008; Redondo and Morris, 2011), and consolidation effects on RL have been reported over shorter times before (Coulthard et al., 2012). Synaptic tagging has mainly been studied in hippocampal circuits, and may relate to the binding of separate experiences within a time window of hours or days (Shohamy and Adcock, 2010). However, the PST is assumed to rely on basal ganglia functioning, at least when there are short delays between action and feedback as there were here (Foerde and Shohamy, 2011). Combining computational synaptic tagging and capture models with basal ganglia RL models would show whether such an explanation could explain this effect. Further behavioural work fractioning the time window after learning where dopamine impacts on consolidation of RL could also be illuminating.

Consolidation has not often been the focus in RL studies, rather learning or testing effects, but a few studies have shown that RL consolidation is affected by dopamine or sleep. Three studies have found that sleep affects performance on the Weather Prediction Task (Barsky et al., 2015; Djonlagic et al., 2009; Lerner et al., 2016). While this task is different to the PST, it is not unreasonable to expect sleep to also affect other RL tasks similarly. Dopamine has also been shown to affect sleep consolidation for reward-related memory (Feld et al., 2014), and while reward-related memory is partly a declarative memory process, it relies on the same reward-processing brain regions that underlie RL (Wittmann et al., 2005).

An alternate explanation is that dopamine state during the 30 min memory block affected reconsolidation of the RL values, allowing the values to be reconsolidated properly and recalled accurately the next day. Dopamine has been implicated in reconsolidation (Rossato et al., 2015), although it has not been investigated in the RL domain.

## Effects of dopamine on learning from positive and negative feedback

Experiment 1 sought to separate the effects of dopamine during learning and during testing on positively and negatively reinforced information, but found no effects of either. PD patients also did not differ from HC. If our study were simply underpowered we might expect the results to at least be in the direction predicted by previous studies. Interestingly, the direction of effect was opposite to the expected effect, with the day 1 ON conditions having the highest amount of avoid-B selections. The classic view is that dopamine improves positive reinforcement, at the cost of impaired negative reinforcement, so it is unclear why the condition in which patients have the most dopamine would show greatest expression of negative reinforcement.

Due to this unexpected pattern, another experiment was run without the 24 hr delay between learning and testing, to try to replicate the expected pattern of behaviour. Experiment 2 used the same modified PST as experiment 1, but with testing immediately after learning. Again, PD patients did not differ from HC, and showed no effect of medication. This is in contradiction to previous studies which found that PD patients had greater expression of positive reinforcement when ON medication, and greater expression of negative reinforcement when OFF medication (Frank et al., 2004; Shiner et al., 2012).

It is surprising that we were unable to replicate the findings of dopamine affecting positive and negative reinforcement, especially in experiment 3 which was designed to be an exact replication of the original study (Frank et al., 2004). We now look at the possible differences between the studies. The main results reported here were on unfiltered data, but when the data filtering used in previous studies was applied, it made little difference to the results.

The average accuracy on novel pairs in experiment 3 was much lower than reported in Frank et al. (2004), where the patients ON medications achieved 78% accuracy in choosing A and patients OFF medications achieved 82% accuracy in avoiding B. By contrast the corresponding accuracies in our experiment were very close to chance (53% and 51%, respectively; 54.5% and 46.7% for filtered data). So, since the patients were unable to well express any learned preferences, it is not surprising that there was no difference in expression preference learned from positive and negative feedback.

One important thing to consider is whether there were sample differences that could explain the disparity between our results and previous studies (e.g. Frank et al., 2004). Our samples were very closely matched in age, gender and disease severity to the PD patients tested ON medication in Frank et al. (2004). T-tests on the Frank et al. (2004) PD sample and our experiment 3 sample showed no significant differences in ages or Hoehn and Yahr stages, and χ2 tests showed no significant difference in gender distributions between PD and HC (p>0.1). The PD patients (p<0.001) and HC (p=0.046) in experiment 3 had fewer years of education on average than those in Frank et al. (2004), which could have contributed to the failure to learn this task, although our experiment 1 sample also had fewer years of education (p<0.001) and they could learn the modified PST. Given that other studies have found effects of dopamine on RL tasks when using different samples, the differences here are unlikely to be dependent on demographic characteristics.

Many studies have used the PST (or variations), and while the findings are not always exactly the same, the general pattern of higher dopamine levels either improving expression of positive reinforcement (Rutledge et al., 2009; Shiner et al., 2012; Smittenaar et al., 2012; Voon et al., 2010), impairing negative reinforcement (Cools et al., 2006; Frank et al., 2007b; Mathar et al., 2017), or both (Bódi et al., 2009; Maril et al., 2013; Palminteri et al., 2009; Piray et al., 2014; Wittmann et al., 2005; Voon et al., 2010) has been seen multiple times. Likewise, low dopamine conditions have shown either worse positive reinforcement (Eisenegger et al., 2014; Jocham et al., 2011; Kobza et al., 2012), better negative reinforcement (Bódi et al., 2009; Cox et al., 2015; Frank et al., 2004; Voon et al., 2010), or both (Palminteri et al., 2009; Piray et al., 2014).

However, not all PST studies have agreed with these findings. One study found that while PD patients with greater left hemisphere pathology showed dopaminergic medication modulated reward and punishment learning, patients with greater right hemisphere pathology showed no such effects (Maril et al., 2013). They also pointed out that left-hemisphere patients are more common, so are likely to be over-represented in study samples unless specifically balanced. We found no effects of laterality of symptoms in our data.

Additionally, the PST was found to have low test-retest reliability when retested 7–8 weeks later (Baker et al., 2013); as well as low correlation between performance at different time points, participants initially classed as ‘positive learners’ or ‘negative learners’ were labelled differently when retested. The study also failed to find any effects of several dopaminergic genes on RL, in contradiction to previous genetic studies (Doll et al., 2011; Frank and Hutchison, 2009; Frank et al., 2007a). This study questions the idea that dopamine improves positive reinforcement and/or impairs negative reinforcement, and raises doubts about the reliability of the PST.

A recent study has shown that performance on the PST depends on the discriminability of the stimuli used, with the difference in discriminability of stimuli A vs B, and stimuli C vs D affecting whether healthy participants showed choose-A or avoid-B biases (Schutte et al., 2017). While the majority of the studies (ours included) using the PST counterbalanced which specific stimuli were A and B (etc.), it is still possible that differences in discriminability between the stimuli within and across experiments may have affected results.

There are many variations of the PST, including using different stimuli (Waltz et al., 2007) smiling and frowning faces as feedback (Aberg et al., 2015, 2016; Gold et al., 2013; Jocham et al., 2011), using money as feedback (Kunisato et al., 2012; Rustemeier et al., 2012), changing the number of pairs (Doll et al., 2014), the probabilities of reward (Doll et al., 2014; Evans and Hampson, 2015), the number of trials (Cicero et al., 2014; Evans and Hampson, 2015), and the filtering criterion (Evans and Hampson, 2015; Waltz et al., 2007). Small changes such as changes to the stimuli used, or changing the delay between action and feedback can have large effects on how this task works (Foerde and Shohamy, 2011; Schutte et al., 2017). Care should be taken when comparing across such procedures, as we, and others, have shown that small modifications to RL task procedure can have large effects on behaviour.

Some studies are now using simpler RL tasks that require learning to predict the outcome associated with one stimulus shown, rather than picking from two simultaneously shown stimuli (Bódi et al., 2009; Herzallah et al., 2013; Mattfeld et al., 2011; Simon and Gluck, 2013; Tomer et al., 2014). Tasks including punishments as well as rewards are frequently used, and often have a simpler probabilistic structure with the same probability for pairs used for the reward and punishment pairs (Eisenegger et al., 2014; Naef et al., 2017; Palminteri et al., 2009; Pessiglione et al., 2006). These simpler tasks may make it easier for participants to learn, and have lesser effects of stimulus discriminability. However, discriminability effects have not been tested for in these tasks, and to date only the Weather Prediction Task has published test-retest reliability data (Aron et al., 2006). So whether other RL tasks are actually better than the PST or have the same issues remains to be seen. It would be useful if reliability and validation data were included in publications for tasks such as these in future.

It is interesting to consider what the implication of our results are for the theories of basal ganglia function. In particular, how our results can be reconciled with the observations that dopaminergic neurons activate striatal D1 neurons, which are believed to be involved in activating movements, while they inhibit the D2 neurons, which are thought to be involved in movement inhibition (Kravitz et al., 2010). It has been recently proposed that these neurons encode not only the expected value of an action in the difference of their activity, but also the variance of the reward in the sum of their activity (Mikhael and Bogacz, 2016). In PST, the stimuli with reward probability closer to 50% have a high variance of reward, because on some trials they result in positive and on some trials in negative feedback. In the simulations of the PST these stimuli strongly activated both D1 and D2 neurons (Mikhael and Bogacz, 2016). Thus on the simulated novel-pair trials with such stimuli and the stimulus A, the D1 neurons selective for both options were activated, and hence increasing the level of dopamine had little affect the accuracy in choose-A (or even decreased it for some variants of the model). These simulations show that the level of dopamine may little influence the accuracy the PST even if the dopaminergic modulation differentially affects the striatal D1 and D2 neurons.

## Conclusion

Dopamine and PD did not affect expression of positive or negative reinforcement when tested immediately or 24 hr after learning. Dopamine during learning improved the consolidation of RL memories over 24 hr. The original PST had very low accuracy, and the modifications made to the PST had large effects, increasing learning and novel pairs accuracy, and increasing the amount of avoid-B selections participants made. This highlights the effects that can be induced by small changes to these types of tasks. These experiments failed to replicate the previously reported effects of dopamine and PD on RL, suggesting the effect may be weak.

## Materials and methods

## Experiment 1

Ethical approval was obtained from the NHS Research Ethics Committee at Frenchay, Bristol. All participants gave written consent, in accordance with the Declaration of Helsinki.

## Participants

The three experiments reported here all tested PD patients and HC. Demographic data are shown in Table 1. PD patients had a diagnosis of idiopathic PD, were stable on their medications for at least 3 months, and were recruited through the general neurology and movement disorders clinic in Frenchay and Southmead Hospitals, Bristol. Patients were on levodopa and/or dopamine agonists, were not taking mono-amine oxidase inhibitors and did not have a Deep Brain Stimulator implanted. When coming OFF medication, patients were withdrawn from standard-release medication a minimum of 15 hr prior to testing, and from prolonged-release medication a minimum of 24 hr prior to testing. For the OFF-OFF condition patients went back ON medication for a short while after the day 1 session, to minimise time spent OFF medication and the risk of neuroleptic malignant syndrome (Keyser and Rodnitzky, 1991).10.7554/eLife.26801.021Table 1.The means and SEM for each experiment for PD patients and HC on all measures taken. Within each experiment, one-way ANOVAs were run between PD patients and HC (χ2 for the genders), and paired t-tests for the comparisons between patients ON and OFF medication for the UPDRS. MMSE scores from experiment 1 were converted to MoCA scores for comparison. *p<0.05, **p<0.01, ***p<0.001.DOI: http://dx.doi.org/10.7554/eLife.26801.021Experiment123MeasurePD patientsHCPD patientsHCPD patientsHCNumber181818201818Gender (M/F)15/3**7/1116/2***5/1511/711/7Age71.56 (2.06)71.19 (2.52)67.39 (2.10)66.05 (2.05)69.11 (1.44)71.61 (2.05)Years Education13.50 (0.66)12.93 (0.89)14.83 (0.91)13.75 (0.56)11.94 (0.52)*14.72 (0.65)MoCA29.44 (0.12)29.63 (0.13)28.72 (0.50)*26.85 (0.53)27.61 (0.54)26.78 (0.56)DASS21.71 (2.85)*12.19 (2.76)15.39 (2.54)20.05 (5.50)29.13 (4.53)**10.44 (2.29) Depression6.35 (0.81)**2.88 (0.87)4.94 (1.13)5.55 (1.958)7.13 (1.71)***2.78 (0.75) Anxiety7.88 (1.27)**3.25 (0.88)5.67 (0.84)5.50 (1.80)10.33 (1.58)***2.61 (0.69) Stress7.47 (1.41)6.06 (1.32)4.78 (1.09)9.00 (2.02)11.67 (1.73)**5.06 (1.25)BIS14.94 (2.36)15.31 (3.07)53.50 (2.47)51.90 (2.35)53.56 (2.70)51.00 (1.88)LARS−20.22 (1.36)***−27.44 (1.24)−23.50 (1.71)*−30.00 (1.58)−22.44 (2.06)*−27.06 (1.16)UPDRS ON18.67 (2.69)18.78 (2.85)26.50 (2.73)UPDRS OFF24.56 (3.41)***23.28 (2.97)30.44 (2.52)***Years since diagnosis4.44 (1.21)4.39 (0.90)5.00 (1.02)Years since symptoms5.18 (1.28)4.78 (0.86)6.44 (1.10)LDE (mg)566.41 (61.18)543.70 (67.36)653.00 (93.96)# levodopa/ dopamine agonists/both12/1/510/2/610/0/8# on XL meds3109MoCA=Montreal Cognitive Assessment, DASS=Depression, Anxiety and Stress Scale, BIS=Barratt Impulsivity Scale, LARS=Lille Apathy Rating Scale, UPDRS=Unified Parkinson’s Disease Rating Scale, LDE=Levodopa Dose Equivalence.

HC were recruited from the ReMemBr Group’s healthy volunteer database.

Experiment 1 tested 18 PD patients and 18 HC. PD patients were tested in a within-subjects manner, with all patients tested in all medication conditions.

## Procedure

PD patients were tested over two days, with learning taking place on day 1, and testing on day 2. Patients could be ON or OFF for each of these days, giving four conditions (ON-ON, ON-OFF, OFF-ON, OFF-OFF; see Figure 6) tested in a randomised, counterbalanced order. All patients completed all four conditions. HC completed one pair of days.

Presentation software (Version 18.0, Neurobehavioural Systems, Inc., RRID:

![Figure 7.](https://cdn.elifesciences.org/articles/26801/elife-26801-fig7-v2.jpg)

**Figure 7.:** Participants saw two symbols on the screen, and selected one with a button press. If no response was made within 2 s, they were shown a ‘GO’ prompt. Feedback was determined probabilistically, was shown for 2 s, and was either the smiling or frowning face.DOI: http://dx.doi.org/10.7554/eLife.26801.022

After 40 practice trials (different stimuli), and 240 learning trials (three blocks of 80), there was a block of 40 ‘memory trials’ which were the same as the learning trials but without the feedback. This measured the participants’ memory on the learning pairs, and is analogous to the delayed memory trials from Coulthard et al. (2012). Another memory block was given 30 min later.

On day 2, 24 hr after learning, a third memory block was given, and then the novel pairs block. This consisted of all the possible pair combinations of the cards (AB, AC, AD, BC, BD, CD) shown without feedback, as in Frank et al. (2004). Each was shown 15 times for a total of 90 trials. From this, the percentage of times that card A was shown and chosen (choose-A) was taken as a measure of positive reinforcement, and the percentage of times that card B was shown and avoided (avoid-B) was taken as a measure of negative reinforcement.

In addition to the PST, several other tasks were administered including the HVLT-R, UPDRS, MMSE, DASS, LARS, BIS and SMHSQ.

## Experiment 2

As experiment 1 failed to show predicted effects of medication or disease state, further experiments were run. As we had made some modification to the PST based on our pilot data, we designed experiment 2 to test whether performance using our modified PST was as predicted from previous work (e.g. Frank et al., 2004) with no delay between learning and testing.

## Participants

Eighteen PD patients and 20 HC were tested in experiment 2. Demographic data are shown in Table 1. Six of the PD patients were previously tested in experiment 1, however excluding these from the analysis did not change the direction of effects, and did not materially affect statistical outputs, so these participants were included in the analysis.

Ten PD patients were given the MMSE while the others, and all HC, were given the MoCA. MMSE scores were converted to MoCA scores using the PD conversion from Waltz et al. (2007).

## Procedure

The modified PST described above was used again, but this time without any memory blocks, and without any delay between the learning and novel pairs blocks. Therefore, participants completed 40 practice trials (different stimuli), then three blocks of 80 learning trials (240 total), followed immediately by the block of 90 novel pairs trials.

As learning and testing was on the same day, PD patients were ON for both, or OFF for both, meaning there were only two testing sessions, and only two conditions for patients. All patients completed both conditions. Again, condition order and task stimuli were randomised and counterbalanced. HC were tested once.

## Experiment 3

## Participants

Eighteen PD patients and 18 HC were tested, demographic data are shown in Table 1. None of these participants had taken part in experiments 1 or 2. PD patients were tested once ON and once OFF (randomised order) and HC were tested once.

## Procedure

The original PST (Figure 1) was run, with three pairs (80–20%, 70–30%, 60–30%), which gave written ‘Correct’ or ‘Incorrect’ feedback. Maximum trial duration was 4000 ms, after which if no response was made, ‘No response detected’ was printed in red and the next trial began. The feedback was shown for 2000 ms.

Forty practice trials (different stimuli) were given, followed by the learning trials. The learning trials ran in blocks of 60 trials (20 of each pair), and participants had to pass accuracy thresholds in order to exit the training. Within one block, participants had to score above 65% accuracy on the 80–20% pair, 60% accuracy on the 70–30% pair and 50% accuracy on the 60–40% pair. If they did not reach these thresholds by the end of the 7th block, they exited the training anyway (in the original study there were only 6 blocks).

The novel pairs test still had all possible combinations (15), although now each was presented only six times to give a total of 90 trials.

Task stimuli were randomised and counterbalanced.

## Data analysis

In all trials, selections of the cards with the highest probability of reward were taken as the ‘optimal’ choice, regardless of what feedback they produced on that specific trial. In the novel pairs block, the learning pairs (AB and CD) were excluded from the analysis as in previous studies (Frank et al., 2004). Between-subjects ANOVAs were used to compare PD patients to HC, and paired sample t-tests to compare the PD medication conditions (with Bonferroni corrections for multiple comparisons). Cohen’s d and ηp2 effect sizes are given for significant results from t-tests and ANOVAs, respectively.

Additional analyses were conducted after data filtering; if a participant scored 50% or lower on the AB choice in the novel pairs task, they were assumed to have not learnt the task properly and that data were excluded. Each condition was checked separately, so one medication condition’s data could be excluded while all other remain. This filtering was only applied to the novel pairs data and analysis.

Some data were missing from the analysis, due to experimenter error or computer errors. Two final learning blocks, two 30 min memory blocks and one novel pairs block were missing from experiment 1.

All error bars in the figures are standard error of the mean (SEM). MATLAB (RRID:SCR_001622) was used for data processing (code available at https://github.com/johnPGrogan/Effects-of-dopamine-on-RL-consolidation-in-PD/releases/tag/v1.0; Grogan, 2017), and SPSS (RRID:SCR_002865) for statistical tests. A copy of the code is available at https://github.com/elifesciences-publications/Effects-of-dopamine-on-RL-consolidation-in-PD.

## Data availability

We did not obtain consent from participants to share individual data from this study, thus only summary statistics are presented in the figures, tables and text. Individual data are not provided in the source data files, although the summary statistics are.
