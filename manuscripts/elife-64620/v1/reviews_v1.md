# Peer review - Round 1

Editors:
- Margaret L Schlichting, University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64620.sa0](https://doi.org/10.7554/eLife.64620.sa0)

This paper will be of interest to cognitive and behavioral neuroscientists, behavioral economists, and developmental psychologists. The authors provide novel evidence that adolescents, relative to children and young adults, are prone to making risk-averse decisions because they are more attuned to negative outcomes during learning. The paper presents rigorous computational analyses that conclusively support the major claims and advance our understanding of age-related shifts in decision making.


---

# Peer review - Round 1

Editors:
- Margaret L Schlichting, University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64620.sa1](https://doi.org/10.7554/eLife.64620.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Valence biases in reinforcement learning shift across adolescence and modulate subsequent memory" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. All three Reviewers had concerns about the modelling results. Many of these concerns stemmed from the lack of consideration of competing accounts for the data and/or limited justification provided for the choice of models. Please (a) clarify the use of the Pavlovian reinforcement learning model in Experiment 2 (Reviewer 1), (b) relate the current work to the utility model originally presented in the Niv 2012 paper which introduced this behavioural paradigm (Reviewer 3), and (c) add fits of additional competing models. Specifically, with regards to point (c), fitting the subjective value model to account for prospect theory, and the subjective utility model, would be informative.

2. Please account for the effect of forced vs. choice trials in both reinforcement learning and memory. All Reviewers highlighted this as an important consideration, as there is evidence that this distinction could lead to differential learning, attention, and/or memory (as shown previously by this group, e.g., Katzman & Hartley 2020).

3. Please include additional data visualizations that depict the raw data, which will better equip the reader for interpreting the results (e.g., the learning curves per experimental condition, and/or per age group as suggested by Reviewer 2).

4. Please consider the role of attention versus reward prediction error (RPE) in the memory effects. Reviewers pointed out that there may be attentional differences across probabilistic versus deterministic trials that could be driving the effects rather than RPE, which if the source of memory differences would warrant a different conclusion than the current paper. In addition, whether and how attention fits into the relationship between asymmetry index and memory was unclear. The authors may be in a position to address this question by performing additional analyses on the current data (e.g., by assessing whether RPE strength alone is related to encoding within the probabilistic trials, as suggested by Reviewer 2); or more generally (in the absence of data) clarify their position or speculate on these issues.

5. Please improve the integration of Experiment 2 into the paper. More details were needed for understanding the purpose of this sample. In addition, Reviewers noted that the interaction found in Experiment 1 did not entirely replicate in Experiment 2. This warrants more consideration in the paper.

6. Please clarify the task and methods descriptions. For example, it is not clear whether the forced choices were included in the modelling. Moreover, please ensure all details needed to understand the major points of the paper are included in the main text without requiring readers to reference the methods.

7. As highlighted by Reviewer 3, it is unclear whether asymmetry biases are a trait-stable characteristic, or rather would change with age within an individual. Please speak to this point as well as other limitations associated with the cross-sectional nature of this study in the revised Discussion.

8. The Reviewers had several additional thoughtful suggestions for other work the authors might cite. I recommend the authors consider whether these suggestions might enhance the novelty, impact, and/or clarity of their paper.

9. Please provide additional details on the models (e.g., reporting parameter β, age effects, model validation, and/or more information on the recoverability analysis) as appropriate. One specific question raised by reviewers was whether learning rate parameter estimation might be more difficult in participants with more deterministic choices and thus fewer trials with non-zero RPEs. Is this empirically true, i.e., does model parameter recovery (as shown in Table 1 overall) differ across ages/ranges of behavior?

Reviewer #1:

Rosenbaum et al. report an investigation of developmental differences in biases to learn from positive versus negative prediction errors-that is, experiences that are either better (positive) or worse (negative) than expected. One of their key findings is that adolescents show a bias towards negative outcomes in both reinforcement learning and memory, a finding that is somewhat surprising given teens' heightened sensitivity to reward and real-world risk-taking. That is, adolescents (1) showed a general bias to make riskier choices (selecting probabilistic rather than deterministic "machines" of equal average value) and (2) show greater learning from negative than positive prediction errors (i.e., showed a negative asymmetry index [AI]). In addition, individual differences in AI were mirrored by a similar memory advantage, where participants showing greater positive AI likewise showed a bias to remember more surprisingly positive stimuli; whereas those showing a greater negative AI were biased to remember more surprisingly negative stimuli. These individual differences were unrelated to age.

This is a strong paper with an interesting set of results. The authors additionally partially replicated their individual difference findings in a separate dataset (experiment 2; including only adults but a larger sample than the main experiment 1), which is a notable strength and somewhat increases confidence in the findings. I am particularly struck by the surprising finding that adolescents are biased towards negative rather than positive outcomes. As appropriately noted in the paper-and particularly given the adolescents did self-report a relatively higher amount of real-world risk taking than other ages, suggesting that it is not the case that the teens in the study are atypically risk-averse in their everyday lives-the degree to which the reinforcement learning task accurately captures something akin to everyday risk taking warrants further consideration in the field.

In addition to these strengths, the paper has several weaknesses as follows:

1. I am left unsure as to the value added by the reinforcement learning model and whether the asymmetry index reflects something unique about learning as compared with a general bias towards deterministic choices in the adolescent period. That is, if the authors wish to make claims about asymmetry of learning rate specifically (α) it would be important to know if this is dissociable from the choice or sampling bias they observe. Empirically, is it the case that there would be a similar set of findings if one focused on the percent probabilistic choices value per participant (data in Figure 2) rather than the asymmetry index (Figure 3)? If these are somewhat redundant or overlapping metrics, I would encourage the authors to clarify this in the paper and perhaps only focus on one of them in the main text, so as not to imply these are separate findings.

2. Related to my above point, those individuals who make fewer probabilistic choices (disproportionately adolescents) have fewer opportunities to learn from prediction errors that are either positive or negative. That is, in my understanding, there will be no prediction error from the deterministic machines which the adolescents primarily select. Their bias to select deterministic machines seems fairly extreme; it appears as though they shy away from the probabilistic choices across the board, even when the value of the probabilistic choice on average would greatly exceed that of the deterministic choice (e.g., as shown in Figure S2). As such, I am wondering whether theoretically the authors can clarify the relationship between choice and learning rate; and analytically whether the bias towards deterministic choices could impact the model fitting procedures.

3. As an additional interpretive question, I had trouble linking the asymmetry index to the memory performance and understanding how the authors believed these metrics to be related. Is there a general increase in interest or attention or salience when a prediction error aligning with the learner's biases (e.g., a highly positive prediction error if I'm someone who learns best from those types of trials – that is, showing a positive AI) happens, therefore indirectly impacting memory formation in the process? Or, is this thought to be a separate mechanism that occurs (the learning from positive prediction errors vs. "prioritization" in memory of those positively valenced experiences)? It seems to me as though both are related to learning/encoding, and thus this individual difference may not be terribly surprising, but I was unsure about the authors' preferred interpretation.

4. While I appreciated the inclusion of experiment 2, I felt that it was not particularly well integrated into the paper. For example, why did the authors opt to use data with only adults rather than a developmental sample (and does this constrain interpretation in any way)? In addition, it is important to highlight that the results do not fully replicate the main findings. In particular, there is no difference in the relationship between the magnitude of prediction error and memory among positively valenced trials according to AI, which was observed in the main developmental experiment 1. This discrepancy warrants more attention in the paper. (Could this be about the sample characteristics? Task differences? and so on.)

5. It was not clear at the conceptual level how the Pavlovian reinforcement learning model fit in experiment 2 is different from the main RSTD used in experiment 1, and/or why these paradigms required the use of different models. Additional description on this point would be helpful.

6. I would appreciate more context for the recoverability results. In particular, the ability to recover which model generated the data for simulated participants (RSTD vs. TD) seemed fairly low. I understand the point about low-asymmetry participants generated by the RSTD model being more parsimoniously fit by the simpler TD model, so that direction of error does not bother me so much. However, I am puzzled by the 87% correct for those simulated participants generated by the TD model. This would have to mean, I think, that the simple TD behavior was being incorrectly attributed to the more complex two-alpha model? I was hoping the authors could provide additional context or reassurance that this qualifies as "good" performance.

7. There were some details not sufficiently described in the main paper for the reader to understand without referencing the methods or supplement. For example: How did the forced versus choice trials work? What is "test trial performance" – the test trials are not described until the supplement and it was confusing to me because the only "test" mentioned in the main paper at this point was the memory test. How were the probabilistic vs. deterministic choices incorporated into the mixed-effects modeling?

8. How were the different responses on the memory test considered? There were four choices according to the figure but it is described as though it is simply "old" vs. "new" responses. Please clarify how this was handled in analysis as well as the reason for inclusion of these four options.

9. I apologized if I missed this point in the paper: I understand that the models were fit to individual data and most participants were better fit by RSTD than TD. However, the authors also discuss the RSTD model winning overall and all subsequent analyses on the individual differences require the two separate α values. So, I am confused as to whether (a) all participants were ultimately fit with the RSTD so all could be included in the analysis, despite some being better fit by TD or (b) only participants who were best fit by RSTD were included in subsequent analyses (or of course (c) something else)? I think this would be OK because my assumption would be that the participants would simply have two α values (positive and negative) that would be similar if their behavior is better explained by the TD model, but I just wanted to clarify.

Reviewer #2:

The authors investigate valence biases in reinforcement learning (RL) and memory, and how they change across adolescence. In a medium size developmental study where outcomes are learned rather than instructed (n = 62, ages 8-27), the results show a surprising choice pattern: adolescents have a stronger bias to select a choice with a deterministic 40 outcome, over a probabilistic 80/0 (50%), compared to younger and older participants. The authors interpret this as a more risk-averse performance, and operationalize it as a difference in RL learning rate. Memory test phase results show that individual images observed with a high absolute reward prediction error (RPE) are more likely to be recalled, and that individuals' valence biases predict a valence asymmetry of this RPE effect. The latter result is partially replicated in a reanalysis of a previously published, non-developmental study.

This is a well-written, easy to read article, that adds a new data point to the complex and contradictory literature on valence, risk, and adolescence, without resolving it. The strengths of the article are (1) its interesting experimental protocol and pure behavioral results (2) the existence of a replication of the complex memory finding.

There are also a number of weaknesses.

First the behavioral results are presented in a very processed manner, limiting the ability to re-interpret the results.

Second, the computational modeling is fairly limited and lacking in competing accounts, which also limits the interpretation of the results. As such, it seems that at this point, the results do not fully support the conclusions – in particular, it is not clear that the interpretation in terms of asymmetric learning rates is warranted yet.

Comments for the authors:

1. Presentation of the results. All figures presented are quite removed from the raw data. It would be helpful to provide more unprocessed results – for example, the learning curves per experimental condition, and/or per age group. This would also provide a more sensitive target for model validation than the ones currently presented in Figure S4. It is much harder for the reader to interpret the results when only very processed data is shown.

This is a well-written, easy to read article, that adds a new data point to the complex and contradictory literature on valence, risk, and adolescence, without resolving it. I see a number of issues with the presentation of the results, the modeling and interpretation of the results.

2. Modeling. The authors use two very simple RL models to capture the performance (a classic δ rule model, and the same with two learning rates). There are a few relevant aspects to the modeling that are either not considered or not reported, but that are important for interpreting the results.

a. Please indicate Q-value initialization and reward rescaling as part of the model description, rather than as part of the model fitting procedure. The initialization has theoretical impacts, so should be part of the model.

b. Prospect theory indicates that a value of 80 is subjectively worth less that 2* the subjective value of 40. As such, the claim that "expected value" and "risk" are controlled for is debatable: if a true 40 feels like a 50 in comparison to an 80, then the two "same objective expected value stimuli" have different subjective expected values, without a need to invoke risk. The authors should test a competing model where the learning rate is fixed, but the obtained reward is modified according to prospect theory (i.e. subjective reward = 80*((reward/80)^p), where p is a free parameter). This model should also be able to capture the presented processed results (existence of an apparent "risk-aversion"), but should have slightly different temporal dynamics, and would lead to a completely different interpretation of the results.

c. Please report parameter β, age effects. Also provide more model validation.

d. Have the author investigated the effect of forced vs. free choice trials, both on RL and memory? There is evidence that this leads to differential learning processes, and potentially differential attention, which could impact both the learning and memory findings.

3. Memory findings:

a. Can the authors comment on the role of attention? Presumably, the participants pay more attention to the outcome of probabilistic than deterministic choices. Could this be a factor in encoding the image, instead of the actual RPE strength? Is there some analysis in probabilistic trials that could be done to show convincingly that the actual size of the RPE matters? In the current analysis, it seems confounded with condition.

b. While the overall statistical pattern is replicated (Figure 4 and 6A), the realization of the triple interaction looks different in the two experiments (Figure 4 and 6B). In the replication, the asymmetry seems to not matter for positive RPEs, and to have a stronger effect for negative RPEs. For the new study, the patterns seem symmetrical between positive and negative RPEs. Can the authors comment on this?

Reviewer #3:

This work provides novel insights about how good and bad feedback differentially influence risky decision making with age from childhood to young adulthood. Further the authors examine how valenced learning biases (updating from positive or negative feedback) influence subsequent memory. The authors tested individuals age 8 to 27 using a risk-sensitive learning task. The task design allowed for the authors to measure learning asymmetries following choices with equivalent expected value but different levels of risk. Learning feedback was accompanied by trial unique images, which allowed for an examination of how learning biases modulate memory. They found that adolescents made more risk-averse decisions, and they over-weighted negative prediction errors during learning. Memory analyses revealed that individual differences in asymmetry bias influenced subsequent memory, an effect that was replicated in an independent sample. The results strongly support the conclusions put forth in this paper. These findings provide timely contributions to both developmental cognitive neuroscience and contemporary research in memory and decision making. The current work provides important revisions to theoretical models in both fields.

Strengths

Prevailing theories of cognitive development posit that adolescents are uniquely attuned to rewards. Yet, little research has investigated developmental differences in sensitivity to negative feedback. The present study advances our understanding of how valence asymmetries (learning from positive vs. negative feedback) during learning bias decision making and subsequent memory across development. The authors use an experimental paradigm that assesses risk-sensitive reinforcement learning. This approach is well-suited to identify individual biases in using positive and negative feedback to guide decision making. The results provide novel, yet surprising, evidence that adolescents are more risk-averse due to enhanced sensitivity to negative feedback. These findings offer an important revision to the current theoretical models of adolescent behavior.

The subsequent memory findings advance our understanding of how prediction errors during learning modulate memory encoding. Prior work has produced mixed results as to whether the valence or magnitude of prediction error influences memory. Here, the authors illustrate that individual differences in learning biases can account for when outcome valence modulates memory. The authors report that asymmetric biases in updating from positive vs. negative prediction errors during learning modulate subsequent memory. However, this effect depends on individual differences in learning asymmetries. Therefore, reward enhances subsequent memory for individuals who are more sensitive to positive prediction errors, however punishment enhances subsequent memory in individuals who are more sensitive to negative prediction errors. A major strength of this paper is that the authors reproduce this memory finding by conducting novel analyses in an existing dataset that was collected in an adult sample.

A major strength of this paper is the analytical approach. The authors implement rigorous computational modeling procedures. They test multiple models of learning and run formal model comparisons to identify the best fitting model. The authors also run simulations and present parameter and model recovery. To test age-related differences, the authors fit both linear and nonlinear age terms. Moreover, to confirm the strength of nonlinear effects, they conducted break-point analyses using segmented regression, as recommended by the Simohnson two-line approach.

Weaknesses

This paper presents data from a cross-sectional sample. This raises questions as to whether learning asymmetries are a stable individual characteristic, or whether these biases exhibit within-person changes with age. Nonetheless, the results of this paper provide important advances to our understanding of age-related differences in learning, decision making, and memory that can form the basis of future longitudinal studies.

Comments for the authors:

This manuscript is exceptionally well-written, and the authors present the methods and findings very clearly. I commend the authors approach to computational modeling and nonlinear age analyses. The present findings provide exciting and novel insights about how adolescents approach risky decision making, which in turn has consequences for memory formation. This is a strong paper, and I believe that the current conclusions warrant publication in eLife. However, I also believe that the inclusion of some additional analyses and clarifications, which I offer below, will further strengthen this manuscript.

In the introduction, the authors explain how prior research in developmental samples cannot disentangle learning asymmetries because performance in prior tasks improved if individuals relied upon updating from positive prediction errors. To clarify this point, and to emphasize the novelty of the current study, it would be helpful if the authors provide a more detailed explanation as to how the present design differs from the paradigm used in Van den Bos 2012.

In the present paper, the authors run model comparison for a basic TD model and a risk-sensitive reinforcement learning model. However, risk sensitivity may be influenced by nonlinear utility functions. It would be informative if the authors also discussed the utility model, as presented in the Niv 2012 paper, which first introduced the present behavioral paradigm. If the authors did not fit this model, please provide an explanation as to why this model was not tested in the current sample.

Prior work from this group has shown that choice and agency can influence memory (e.g. Katzman & Hartley 2020). Therefore, for the memory data, it would be helpful if the authors accounted for the different trial types (choice trials vs. forced trials) in the analyses.

Due to the cross-sectional nature of the sample, it is unclear if asymmetry biases are a trait-stable characteristic, or whether this bias changes with age within an individual. It would be helpful for the authors to address this in the discussion.
