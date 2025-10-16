# Peer review - Round 1

Editors:
- Thorsten Kahnt, Northwestern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57023.sa1](https://doi.org/10.7554/eLife.57023.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This elegant human study examined the effects of retrieval practice on memory performance and neural responses. The results from a set of experiments show that retrieval practice strengthens new memories and reduces intrusions of old memories without suppressing the old memories. Interestingly, this was related to enhanced representations in medial prefrontal cortex, further supporting the idea that this region is important for memory integration and consolidation.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Retrieval practice facilitates reactivation-dependent memory updating" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

As is evident in the individual critiques copied below, the reviewers agreed that your manuscript provides nice and robust evidence for memory updating by means of strengthening the target memories. However, the reviewers felt that given the lack of strong evidence for either competitor suppression or integration, this alone is not novel enough for eLife. In addition, the reviewers agreed that results from the 3-way classifier are difficult to interpret and that two separate 2-way classifiers or an RSA approach would be required to reveal what is reactivated. Finally, there were concerns that the results of experiment 2 were inconclusive.

In light of these concerns, we decided that we cannot move forward with this paper at eLife. However, if you are willing and able to address these issues in full (including new behavioral experiments), you would be able to resubmit a substantially revised version of the manuscript to eLife in the future (if you choose to do this, please refer to this manuscript number and rejection decision in your future submission). However, we understand that you may prefer to submit the manuscript, in its current form, to a more specialized journal.

Reviewer #1:

The authors test the hypothesis that active remembering is an effective means of memory updating when there is proactive interference from outdated information. Participants learn novel associations (A-B) on Day 1, then are asked to replace these memories with overlapping associations (A-C) on Day 2, either by active retrieval practice (RetPrac) or Restudy practice of the new A-C memories. On Day 3 all groups undergo a final memory test. Behaviorally, participants in the RetPrac condition recall the target more often, and experience fewer competitor intrusions, on the Day 3 final test. Multivariate analyses of brain activity patterns suggest that competitors are co-activated on Day 2 in a number of brain regions, but subsequently suppressed and become less accessible on Day 3, again specifically in the RetPrac items. Neural evidence for target and competitor reactivation thus largely tracks the behavioral effects observed.

The manuscript addresses an interesting and timely topic, and the Introduction and Discussion are well written and accessible. The most central behavioral and MVPA findings seem very robust. These findings are largely to be expected based on the existing literature (as appropriately cited in the manuscript), but I do not know of a similar set of coherent results that demonstrates these aspects of memory updating, and therefore I think the manuscript should in principle be considered for publication in eLife. I have a few major concerns, however, regarding the methods, results and conclusions, as outlined in the following.

1) A fundamental technical problem in my view is the use of a 3-class classifier. When such a classifier provides evidence for a target, it is automatically confounded by "anti-evidence" for the competitor and the other, neutral category. The same goes for the competitors: if a 3-class classifier provides strong evidence for competitors being reactivated, this could be due to strong competitor evidence or weak target (and neutral) evidence. The problem is exaggerated by using a normalization where the "neutral" evidence is subtracted from target and competitor evidence. It would be much preferable if the authors used 2-class classifiers with the neutral category as baseline for all analyses trying to separate target and competitor reactivation.

2) During retrieval practice, were subjects significantly more likely to experience an intrusion than an unrelated (other) error? It seems from Figure 1C that they were not, speaking against any strong A-B proactive interference effect, and more for a general learning of the target response over time. This result seems crucial for the central claims of the paper. Similarly, the authors should report in both experiments how the number of Day 2 intrusions on relates to Day 3 performance, and whether this relationship is stronger for intrusions than unrelated errors.

3) The authors make strong claims about competitor suppression throughout the manuscript where the actual evidence appears relatively weak. In the behavioural Experiment 2, if there was a suppression effect, how do the authors explain that they did not find reduced A-B memory for RetPrac than Restudy on Day 3? Is this due to the delay of the final test? Relatedly, the negative correlation between A-B and A-C memory is interpreted as evidence for suppression but can as easily be seen as an associative interference effect. Finally, in Experiment 2, the authors test A-C associations before A-B associations, making it likely that output interference on the A-B items will overshadow potentially more subtle effects of suppression in this experiment.

4) While the most central results seem sound, some of the analyses reported later in the Results section appear less well motivated and somewhat arbitrary in their approaches and selective in the reporting. To avoid the impression of p-hacking, the authors should streamline these sections, and use a more consistent and well-motivated rationale for all of the analyses. To give a few concrete examples,

a) The analysis reported in paragraph two of subsection “The LPFC contributed to memory updating under the RetPrac condition” and in Figure S8 is difficult to follow in terms of rationale. The results are also a bit confusing: none of the ROIs shows a pattern where strong competitor reactivation is related to strong LPFC activation, which is surprising given existing literature. Did the authors average competitor evidence across the 3 repetitions? In my mind, the straightforward prediction here is be that strong competitor reactivation on early repetitions, and weak on late repetitions, should be related to effective LPFC-mediated suppression. Therefore, for these analyses it makes more sense to use the slope of competitor reactivation across repetitions, not the average evidence for reactivation

b) The analysis relating caudate activity to competition resolution seems arbitrary for readers not reading the supplements. It is unclear why a different metric is being used here (compared to LPFC) to relate univariate and multivariate effects.

c) The analysis splitting trial into incorrect (IC), first correct (FC) and second/third correct (LC) is not well motivated and difficult to follow.

5) In some instances, interpretations are quite a large step removed from the actual results. For example, why does a difference in LPFC activity between IC/FC and LC (paragraph two subsection “The LPFC contributed to memory updating under the RetPrac condition”) indicate a role in competitor suppression? Such a pattern is more likely driven by target-related processes.

6) The tertile analyses relating competitor reactivation on Day 2 to competitor reactivation (see Figure 5) on Day 3 are not convincing statistically. The interaction with region as a factor seems irrelevant. In IFG and AG the conclusions are based on null results, and in VTC there is a strong positive relationship speaking against reactivation-dependent updating. The only thing left therefore is the U-shaped effect, and this appears like a posthoc observation.

7) For the Day 2 MVPA analyses, the authors never show evidence for target reactivation (or rather, representation given the visual exposure), this result should be included.

Reviewer #2:

In this timely and creative study, the authors investigate in a within-subjects fMRI design with 19 subjects the neural mechanisms and behavioral effects of retrieval practice vs. re-study of A-B, A-C memory updating. In a second within-subjects behavioral study with 28 subjects, the authors probe their postulation that retrieval practice vs. re-study leads to prioritization of C and suppression of B as related to A in memory updating. There are a few drawbacks to the theoretical framing, analytic technique, and conclusions drawn from the data that should be addressed.

1) Theoretical framing:

The authors adopt a research paradigm that is akin to inference/integration/generalization memory work. I was surprised to see this conceptualization of the paradigm downplayed in the Introduction and Discussion, particularly because A-B pairs were overtrained on Day 1. I think that the manuscript would benefit from more explicit characterization of why the adopted paradigm speaks to a suppression account of a B vs. an integration account of a B in memory updating, and how their data adjudicate between these two accounts (e.g., MPFC is often shown as a schema/generalization area).

2) Analytic technique:

a) I was not convinced that the retrieval practice vs. re-study Day 2 design and analyses provided clear support for the idea that B is suppressed and C is prioritized in retrieval practice vs. re-study during memory updating. In fact, the authors do not find evidence of this claim in their follow-up behavioral study designed to address the issue; they have to split data to show that in some subjects you see this pattern but in others you don't. Because the evidence stemming from this follow-up is not clear, the mechanism of retrieval practice in memory updating (suppression vs. integration) is not clear.

b) The critical results of the study are subsection “Retrieval practice enhanced target reactivation and competitor suppression” of the manuscript. I was confused as to why the authors have one classifier analysis for final test performance (Day 3) that doesn't account for retrieval practice/re-study (Day 2), and then another classifier analysis for retrieval practice/re-study (Day 2) that doesn't account for final test performance (Day 3). Why was behavioral performance but not the Day 2 manipulation used in the first analysis, and why was the Day 2 manipulation but not behavioral performance used in the second analysis? I think an analysis that uses both these assays would get at the authors' question most directly.

c) How many trials were used in the fMRI analyses per condition?

d) Greater motivation for the ROI selection parameters for MVPA should be given.

e) Is it possible that shifts in decision criteria would be observed for those trials with retrieval practice on Day 2 vs. those trials with re-study on Day 2? Can the authors rule out a decision criteria account of behavioral findings on Day 3 final test?

3) Conclusions drawn from the data:

a) As noted, I did not think that the critical finding about retrieval practice during memory updating was supported by the data; the authors' own follow-up study did not provide strong behavioral support for this claim. Thus, it is hard to reconcile the lack of a clear mechanism with the fMRI side of the manuscript.

b) The lack of neuroimaging effects for AG and Hipp was striking, particularly given recent work finding reactivation effects in parietal cortex (Jonker, Ranganath, 2019, PNAS; Lee, Kuhl, 2019, Cerebral Cortex). These papers should be cited in text and discussion should be given as to the discrepancies.

Reviewer #3:

In this paper, the authors tested the hypothesis that retrieval facilitates memory updating through stronger suppression of competing memory. Using a word-picture association paradigm with fMRI, the authors found that brain regions, including mPFC, showed greater reactivation of new memory at the final test, but greater reactivation of old memory during practice in the test condition, compare with the restudy condition. In addition, LPFC showed stronger activity during retrieval practice than during restudy. Overall, this is a very interesting study addressing how memory retrieval interact with proactive memory interference. The paper is easy to read and the design and method are clearly described. However, some of our enthusiasm was dampened by significant questions and concerns regarding the novelty and central arguments in the paper. These areas of significant concern are detailed below:

1) This is a very interesting and fruitful set of results, but the framing does not seem to fit with the work that is reported. The logic of the paper is that neural changes in response to repeated retrievals reflect memory updating and suppression of old memory, but a priori this did not seem like an obvious prediction. It is possible that any differences (both in behavioral performance and neural activity) between the test and the restudy condition simply reflect superior learning during testing. In other words, without a no interference or weaker interference condition, it is hard to conclude that brain activity during retrieval practice supports memory updating/suppression.

2) From the Introduction, it is unclear how this study is different from prior studies examining neural mechanisms underlying retrieval induced forgetting using a similar paradigm, e.g. Wimber et al., 2015.

3) The authors capture many previous findings about activity in mPFC and LPFC, however, the hypothesis they form following this literature is too vague to be clearly falsifiable or to adjudicate between potentially contradictory findings. For instance, rather than reflecting suppression, stronger reactivation of competing memory during retrieval practice has also been associated with retrieval induced facilitation (e.g. Jonker et al., 2018). Moreover, the authors examine brain activity in 4 ROIs but did not present a rationale for including AG, IFG, VTC.

4) It is laudable the authors report a follow-up behavioral experiment examining the relationship between memory for new memory vs. old memory. However, the negative correlation could be driven by output interference, especially given that subjects recalled A-C pairs first. It is likely that better A-C recall produced stronger output interference to A-B pairs.

5) It is unclear in the analyses of retrieval practice reactivation, whether the authors included all test trials or only correct test trials. If all trials were included, all the results reported in these sections would not be surprising because subjects wrongly recalled a large portion old targets during retrieval practice. This also explains why restudy trials showed larger reactivation of new memory because new information was always directly presented.

6) A number of ad hoc hypotheses are given for results that are inconsistent with the prediction. For example, the authors claim that the null results for correct or incorrect trials are due to a small number of trials. However, there should be at lease 70 correct trials in the test condition and 50 correct trials in the restudy condition. Moreover, decreased update in the restudy condition is explained by the repetition suppression effect; null results of correlations between competitor reactivation and behavioral performance are explained by the claim that behavioral measure is not sensitive; chance level classification performance in the hippocampus is thought to reflect "technical limitations". These ad hoc explanations of conflicting results, which lack justification, suggest strong confirmation bias.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Retrieval practice facilitates memory updating by enhancing and differentiating medial prefrontal cortex representations" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

All reviewers agreed that the authors have done a very thorough job addressing the initial comments, and that, as a result, the paper is much improved. Reviewers also identified a few remaining issues that should be addressed with new analysis and re-writing.

Revisions:

1) The authors analyzed the behavioral data with a "test order (A-C first, A-B first) by memory test type (Recall A-C, Recall A-B) by update method (RetPrac, Restudy) by response type (Target, Competitor, Other) four-way mixed design ANOVA". Either the choice or the description of the analysis is incorrect. Given that the performance of A-C test and A-B test, absolute ratios of Target, Competitor and Others are not comparable, response type and memory test type should not be used as independent variables (factors). Rather, separate ANOVAs should be conducted, with appropriate multiple comparison correction, to examine target ratio and competitor ratio in each test.

2) Given the above reason, the authors cannot rule out the potential order confounding by just showing there was no significant effect of test order or interaction effect with test order in this four-way ANOVA. Rather, the authors need to directly compare A-B performance between when A-B was tested first vs. when A-B was tested after A-C. However, even if the correct analysis was done, non-significant difference between different orders cannot rule out the confounding of order either. A stronger test would be only examining A-B performance with subjects start with A-B test, and vice versa for A-C test.
