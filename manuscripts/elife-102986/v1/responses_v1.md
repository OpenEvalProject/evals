# Author response - Round 1

Authors:
- Gaqi Tu ([ORCID: 0000-0001-5807-0798](https://orcid.org/0000-0001-5807-0798))
- Peiying Wen
- Adel Halawa
- Kaori Takehara-Nishiuchi ([ORCID: 0000-0002-7282-7838](https://orcid.org/0000-0002-7282-7838))

## Response text

DOI: [10.7554/eLife.102986.2.sa4](https://doi.org/10.7554/eLife.102986.2.sa4)

(1) We do not know that the mechanism mediating the behavioral changes observed involves acetylcholine at all. (Reviewer 1)

The reviewer rightly pointed out the co-release of acetylcholine (ACh) and GABA from cholinergic terminals. We believe that the detected behavioral changes are because of the augmentation of this innate mixed chemical signal. We agree that identifying the receptor specificity is an essential next step; however, addressing this point requires a currently unavailable research tool to block cholinergic receptors for a few hundred milliseconds. This temporal specificity is vital because acetylcholine is released in the medial prefrontal cortex (mPFC) on two distinct timescales, the slow release over tens of minutes from the task onset and the fast release time-locked to salient stimuli (TelesGrilo Ruivo et al., 2017). Moreover, the former slow signal is far more robust than the latter phasic signal. The pharmacological experiments suggested by the reviewer will suppress both the tonic and phasic signals, making it difficult to interpret the results. Given the rapid technological advancement in this field, we hope to investigate the underlying mechanisms in detail in the future.

(2) It is unclear whether mPFC cells are signaling predictions versus prediction errors. (Reviewer 2)

As the reviewer pointed out, mPFC cells signal the prediction of imminent outcomes (Baeg et al., 2001; Mulder et al., 2003; Takehara-Nishiuchi and McNaughton, 2008; Kyriazi et al., 2020).

However, the key difference between prediction signals and prediction error signals is their time course. The prediction signals begin to arise before the actual outcome occurs, whereas the prediction error signals are emitted after subjects experience the presence or absence of the expected outcome. In all our analyses, cell activity was normalized by the activity during the 1-second window before the threat site entry (i.e., the reveal of actual outcome; Lines 655-659). Also, all the statistical comparisons were made on the normalized activity during the 500-msec window, starting from the threat site entry (Lines 669670). Because this approach isolated the change in cell activity after the actual outcome, we interpret the data in Figure 4C as prediction error signals.

(3) The task does not fully dissociate place field coding. (Reviewer 2)

The present analysis included several strategies to dissociate outcome selectivity from location selectivity (Figure 4). First, we collapsed cell activity on two threat sites to suppress the difference in cell activity between the sites. Second, our analysis compared how cell activity at the same location differed depending on whether outcomes were expected or surprising (Figure 4C). Nevertheless, we can use the present data to investigate the spatial tuning of mPFC cells. Indeed, an earlier version of this manuscript included some characterizations of spatial tuning. However, these data were deemed irrelevant and distracting when this manuscript was reviewed for publication in a different journal. As such, these data were removed from the current version. We are in the process of publishing another paper focusing on the spatial tuning of mPFC cells and their learning-dependent changes.

(4) The basic effects of cholinergic terminal stimulation on mPFC cell activity are unclear. (Reviewers 1, 3)

We acknowledge the lack of characterization of the optogenetic manipulation of cholinergic terminals on mPFC cell activity outside the task context. As outlined in the discussion section (Lines 309-321), cholinergic modulation of mPFC cell activity is highly complex and most likely varies depending on behavioral states. In addition, because we intended to augment naturally occurring threatevoked cholinergic terminal responses (Tu et al., 2022), our optogenetic stimulation parameters were 3-5 times weaker than those used to evoke behavioral changes solely by the optogenetic stimulation of cholinergic terminals (Gritton et al., 2016). Based on these points, we validated the optogenetic stimulation based on its effects on air-puff-evoked cell activity during the task (Figure 2C, 2D).

(5) Some choices of statistical analyses are questionable (Reviewers 1, 3)

We used the Kolmogorov-Smirnov (KS) test to investigate whether the distribution of cell responses differed between the two groups (Figure 2D) or changed with learning (Figure 3Ac, 3Bc). As seen in Figure 3Aa, some mPFC cells increased calcium activity in response to air-puffs, while others decreased. We expected that the manipulation or learning would alter these responses. If they are strengthened, the increased responses will become more positive, while the decreased responses will become more negative. If they are weakened, both responses will become closer to 0. Under such conditions, the shape of the distribution of cell response will change but not the median. The KS test can detect this, but not other tests sensitive to the difference in medians, such as Wilcoxon rank-sum tests. In Figure 2D, KS tests were applied to the independently sampled data from the control and ChrimsonRexpressing mice. In Figure 3Ac and 3Bc, we used all cells imaged in the first and fifth sessions. Considering that ~50% of them were longitudinally registered on both days, we acknowledge the violation in the assumption of independent sampling. In Figure 1D, we detected significant interaction between the group and sessions. Several approaches are appropriate to demonstrate the source of this interaction. We chose to conduct one-way ANOVA separately in each group to demonstrate the significant change in % adaptive choice across the sessions in the control group but not the ChrimsonR group. The cutoff for significance was adjusted with the Bonferroni correction in follow-up paired t-tests used in Figure 1F.
