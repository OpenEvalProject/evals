# Peer review - Round 1

Editors:
- Muireann Irish, University of Sydney Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62520.sa1](https://doi.org/10.7554/eLife.62520.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This is an interesting and timely study exploring the relationship between objective and subjective indices of recollection to provide novel insights into the mechanisms underlying memory-guided decision-making. Using an innovative experimental paradigm comprising a memory phase and decision phase, the authors provide an elegant behavioural dissociation between two conditions; A-A' condition in which the diagnostic features of stimuli are prioritised thus promoting higher levels of objective accuracy, versus the A-B' condition in which a global appraisal of the target stimulus instantiates a stronger sense of subjective recollection. Results suggest that participants' behaviour is derived from subjective global appraisal, rather than fine-grained consideration of objective features.

Decision letter after peer review:

Thank you for submitting your article "Distinct Neural Mechanisms Underlie Subjective and Objective Recollection and Guide Memory-based Decision Making" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This fMRI study of young healthy adults explores potential dissociations between subjective recollection and objective episodic memory accuracy within the posterior parietal cortex and PFC. Using a 2AFC object-memory task, the authors reveal clear behavioural dissociations between two conditions; A-A' condition in which the diagnostic features of stimuli are prioritised thus promoting higher levels of objective accuracy, versus the A-B' condition in which a global appraisal of the target stimulus instantiates a stronger sense of subjective recollection. The study further explores metacognitive appraisals of this process, by having participants make judgements about keeping or discarding recollection trials towards an overall score. Taken together, the behavioural and neural dissociations are interesting and timely, and this study should make a useful contribution to the literature.

Essential revisions:

1) The authors need to provide a much more thorough overview of the extant literature. For example, several studies exist that have already examined this dissociation, some cited here (Richter et al., 2016), others not cited or discussed in this way (Duarte, Henson, Graham, Cerebral Cortex 2008; Mark and Rugg, 1998) as well as PPC lesion studies (Davidson et al., Neuropsychologia 2008; Hower et al., Neuropsychologia 2014; Simons et al., 2010; Ciaramelli et al., Cortex 2017). The authors need to clearly articulate how their study builds on and extends previous work, as well as delineating precisely the novel contribution that their study makes.

2) Related to the above point, a substantial body of work exploring the contribution of posterior parietal regions to episodic recollection has not been discussed (e.g. Kuhl and Chun, J.Neuroscience 2014; Favila et al., J. Neuroscience 2018; Frithsen and Miller., Neuropsychologia 2014; Ramanan S. et al., The Neuroscientist, 2018). It would be important to integrate this prior work to appreciate how the current results fit within the broader memory literature.

3) It is not clear how the distinction between subjective and objective recollection maps on to the distinction made between "local" and "global" processing. The authors should clearly explain what they mean by "global assessment" (provide a definition) and why exactly this process might give rise to a stronger sense of subjective recollection (e.g. as proposed in the Introduction). Similarly, the authors should clarify why this "global assessment" would also come alongside a situation where "salient retrieval output will be more likely to serve as a basis for response".

4) While it is acceptable to have an active baseline to reduce the probability of negative BOLD memory effects, due to greater activity at rest, it seems highly unlikely that the baseline task ("press a number") would prevent participants from remembering their previous memory decision just a few seconds earlier. Given that the decision phase task asks participants to keep or trash their prior memory decision, it is not clear how this would be an effective distractor task, as subjects knew they needed to make this decision based on their first memory choice. Furthermore, it is stated in the decision phase results that the authors wanted to determine if patterns of activity in the memory phase persisted in the decision phase, which of course, many did. While the decision phase may provide some behavioural support for the authors' predictions about the two task conditions, it is not clear what the decision vs. memory phase neural comparison is intended to show. Presumably, the authors could compare BOLD responses during the memory phase for select and discard trials and see similar results, though peaks and significance values may vary somewhat.

5) The precise instructions and conditions of the decision phase of the experiment warrant further explanation. Under what circumstances would a participant “trash” their responses? What were the specific instructions provided to participants? Were participants instructed explicitly on how their score was calculated? Did they think their score simply reflected the correct versus incorrect retrievals? It is not clear from the manuscript whether participants thought their score was calculated based purely on objective retrieval accuracy or whether it also related to their "remember vs. very familiar vs. somewhat familiar" judgements. This is a subtle point but one with serious implications for the interpretation of the behavioural and neural data.

6) Related to the neural predictions on the decision phase, there is no discussion of the differences between retrospective and prospective metacognitive monitoring within the PFC (e.g. Fleming and Dolan, Phil. Trans. Royal Society. 2012). Metacognitive monitoring is treated as a unitary construct here.

7) Please detail how the sample size was determined – was a power analysis conducted? Was this sample a convenience sample or determined based on available resources? What was the stopping rule for data collection? Additionally, was the study pre-registered? Which hypotheses and tests were a-priori, and which were conducted after the data had been examined? Ideally, this should be specified throughout.

8) Further details are required regarding the data analysis strategy. For example, for the mixed-effects modelling approach, was there a reason why only intercepts were allowed to vary by participant but not random slopes? There are good theoretical and empirical reasons to expect that the coefficients for the key effects would also vary by participant, not only the intercepts. Some justification of the modelling decisions is warranted here.

9) Similarly, the reader would benefit from more detail about where the reported results are drawn from – in the mixed effects framework, for instance, where are the p values derived? Did you use a package like "lmerTest" with Satterthwaite's method, or did you do some kind of model selection (comparing between models with/ without focal variables)? As far as I know, lme4 does not, by default, provide p-values.

10) The plots lack the overlaid raw data, making inferences difficult. The authors should overlay the raw datapoints on top of the bar charts so that readers can see for themselves what the distributions look like. Similarly, there are no plotted logistic regression functions, meaning the plots for the behavioural data do not match up with the analytical tools used for the inferential statistics and reported in text – perhaps this needs at least to be explained in the figure legend?

11) A point worthy of discussion is the possibility that the motivation to do well on this task may not necessarily be financial, but could have been socially driven, in that participants' scores were displayed. Thus, motivation to perform well may not reflect "reward" as per previous incentive-compatible confidence studies, but potentially both social reward and punishment (e.g. embarrassment at poor performance). Aspects of the Abstract and Discussion should be re-phrased because the decision task was not incentivized with tangible rewards – instead, it could also contain the motivation to avoid a penalty like embarrassment.

12) I would like to see some consideration of the laterality of the parietal regions that were recruited during the memory phase, given that it was the right supramarginal gyrus that emerged in the analyses. For example, I was surprised that the angular gyrus did not emerge as a key region during the memory phase and I wonder if the authors could comment on the lack of AG involvement in the current study (e.g. see work by Preston Thakral; Siddharth Ramanan, Heidi Bonnici). It would help the reader to place some of these findings in context and comment on how the paradigms etc. potentially give rise to these differences across studies.
