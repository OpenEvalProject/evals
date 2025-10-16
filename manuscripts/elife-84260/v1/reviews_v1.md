# Peer review - Round 1

Editors:
- David Badre, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84260.sa0](https://doi.org/10.7554/eLife.84260.sa0)

This is an important study that investigates changes in novelty-seeking and uncertainty-directed exploration from childhood to adulthood. A wide age range of participants was tested using a well-suited task and performance was analyzed using a sophisticated model-based approach. The results provide compelling evidence that age-related changes in decision-making are driven by attenuation in uncertainty aversion in the presence of stable novelty-seeking from childhood to adulthood.


---

# Peer review - Round 1

Editors:
- David Badre, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84260.sa1](https://doi.org/10.7554/eLife.84260.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Novelty and uncertainty differentially drive exploration across development" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor, David Badre, and Timothy Behrens as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Charley M. Wu (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Though both reviewers found this to be an important investigation, they identified some points that could be addressed in revision to strengthen the support for the conclusions. Their detailed comments below are clear, so I won't copy them here. But they focus on four issues that would be essential to revise.

1) Modeling – Both reviewers had comments about ways that the modeling could be improved. R1 provided suggestions on how you can clarify and elaborate on the performance of the models. R2 suggested some new modeling, such as incorporating RT, given the sensitivity of decision time.

2) Statistics – R1 had several comments regarding the strength of the statistical evidence that could be clarified.

3) Novelty measure – R1 also raised questions about the definition of novelty. This is important to address, or at least clarify how you are defining it, given the centrality of this construct for your conclusions.

4) Reward uncertainty in children – Related to R2's comments on modeling, R2 also raised comments about the strength of evidence for the conclusion that children do not use reward uncertainty when making their decision when one considers measures like response time. This also seems important to address given its relationship to your conclusions about changes in this factor over development.

Reviewer #1 (Recommendations for the authors):

Nussenbaum, Martin, and colleagues present experimental data and computational modeling results to disentangle the role of uncertainty-directed and novelty-seeking exploration across childhood, adolescence, and adulthood. Their task uses an adapted version of a previously published decision-making task (Cockburn et al., 2022), where they analyze age-related differences in choice behavior (quantified in terms of value, uncertainty, and novelty), reaction times, and with various computational models incorporating different biases.

Overall, I found this work to be clearly written and well-motivated. Some priority claims in the introduction seemed a bit unnecessary though since previous work has also disentangled novelty and uncertainty (Stojić et al., 2020), and two papers already cited in the manuscript have looked at how exploration changes from childhood to adulthood (Giron et al., 2022; Schulz et al., 2019). However, I think this paper is interesting enough and provides a sufficiently new perspective without needing to rely on claims about being first.

The goal of the paper is to disentangle age-related changes in uncertainty-directed and novelty-seeking exploration. I believe that the behavioral and model-based analyses provide some (but perhaps limited) support for the idea that novelty-seeking stays fixed over the lifespan, whereas people become more uncertainty-averse as they get older.

While I greatly appreciate the use of multiple analyses to support their arguments, I have some reservations about the conclusions reached by this paper. These reservations hinge on potential weaknesses in statistical analyses, limited application of the computational models, and potential issues with the quantification of novelty.

Statistics

While the statistics were generally pretty clear, there was heterogeneity across behavioral analyses that seemed to lack justification. Moving from the proportion of optimal choices to total reward earned, it's unclear if the same random effects structure (as in the logistic regression) is applied or if a non-mixed effects model is used instead. If there is a specific reason for changing the statistical framework, it would be helpful to provide some justification.

Additionally, some of the behavioral effects seem rather weak when looking at the plots (e.g., changes in performance over age and age-related differences in choosing more vs. less uncertain options). While likelihood ratio tests are used to show that a model with the predictor is better than one without, the coefficients are not reported, making it difficult to assess whether the effect size is meaningful. Looking at Figure 2B, it wasn't obvious if children performed reliably worse than adults, or if the task is relatively simple such that a ceiling effect is reached. Reporting the regression coefficients (or the Odds Ratio for the logistic regression) and using a consistent mixed-effects structure would greatly help with interpreting these results.

Model results

One of the strengths of the paper is in using multiple analyses (e.g., choices, RTs, and models) to probe the main question. However, I felt that the model results were a bit underwhelming. It's clear a lot of work has gone into them, but we are given a relatively sparse account of how well they perform. Showing age-related changes to the parameters governing novelty and uncertainty bias would be very helpful in supporting the behavioral analyses in justifying the current conclusions. Currently, it's not reported if children's novelty bias differs from adolescents or adults or if novelty bias changes as a function of age. Second, beyond the rather 1-dimensional comparison provided in Figure 5, would you expect the models to also reproduce key behavioral signatures (e.g., in Figure 2 and Figure 3?)? It's also fine if this is out of the current scope, but a demonstration that age-related changes in uncertainty bias but not novelty is necessary to reproduce key aspects of behavior would provide the strongest support for the current claims. Lastly, the recovery results suggest potential misspecification with the winning model also accounting for a lot of the variance from other models. It would be very helpful to also report the inversion matrix (Wilson and Collins, 2019).

Measuring novelty

I found the quantification of stimulus novelty to be sensible but somewhat limited. It captures a uni-dimensional account of how often one has interacted with a given stimulus. But it doesn't capture how accustomed we are to other stimuli and how genuinely novel new stimuli may be. For example, for a naïve learner in the task, any new locations may be equally novel. However, over the course of learning, one gains familiarity with existing stimuli, such that new locations might be more surprising or unexpected. This familiarity effect would predict that novel stimuli in early blocks should differ from later blocks.

Perhaps a more holistic account of stimulus novelty could use a Dirichlet distribution over the n different hiding locations, where the concentration parameter α_i is updated for each experience of stimuli i. This would capture how expectations over all stimuli can inform novelty judgements about a particular new stimulus. I should clarify that this is a rather speculative suggestion, and I'm definitely not going to insist that you adopt it. Perhaps you've already looked into the effect of novelty over blocks and have already falsified this prediction. However, I am personally curious about how this would influence other downstream analyses. And since the forgetting mechanisms of the Bayesian learner can be applied to uncertainty but not to the current implementation of novelty, swapping to a Dirichlet distribution would also let you apply an equivalent decay process to the concentration parameters.

References:

Barr, D. J., Levy, R., Scheepers, C., and Tily, H. J. (2013). Random effects structure for confirmatory hypothesis testing: Keep it maximal. Journal of Memory and Language, 68(3). https://doi.org/10.1016/j.jml.2012.11.001

Giron, A. P., Ciranka, S. K., Schulz, E., van den Bos, W., Ruggeri, A., Meder, B., and Wu, C. M. (2022). Developmental changes resemble stochastic optimization. https://doi.org/10.31234/osf.io/9f4k3

Schulz, E., Wu, C. M., Ruggeri, A., and Meder, B. (2019). Searching for Rewards Like a Child Means Less Generalization and More Directed Exploration. Psychological Science, 30(11), 1561-1572.

Stojić, H., Schulz, E., P Analytis, P., and Speekenbrink, M. (2020). It's new, but is it good? How generalization and uncertainty guide the exploration of novel options. Journal of Experimental Psychology. General, 149(10), 1878-1907.

Wilson, R. C., and Collins, A. G. (2019). Ten simple rules for the computational modeling of behavioral data. eLife, 8. https://doi.org/10.7554/eLife.49547

Reviewer #2 (Recommendations for the authors):

This study deploys a modified value-guided decision-making task (adopted from Cockburn et al., 2022) to examine factors contributing to the commonly observed developmental shift toward exploitation. The paradigm permits a dissociation between sensory stimulus novelty and reward uncertainty, allowing the authors to investigate the effects of both factors on choice behavior across a large population of participants ranging from eight to 27 years. The authors apply a combination of linear mixed-effect modeling and reinforcement learning to examine age-related differences in the influence of novelty and reward uncertainty on choices and reaction times (RTs). Both types of analyses yield the same age-related differences: the choice behavior of adults is best captured by both sensory novelty (novelty-seeking) and reward uncertainty (uncertainty aversion), whereas the choice behavior of children is best captured by novelty, not uncertainty. Nevertheless, children's RTs are partly influenced by reward uncertainty. The authors conclude that the developmental shift toward exploitation may reflect an age-related increase in the aversion to reward uncertainty (as opposed to alterations in novelty-seeking) and that children do not factor uncertainty into their decision-making.

Strengths

The study deployed a well-suited paradigm (Cockburn et al., 2022) to examine age-related changes in decision-making behavior. The experiment enables a clean dissociation between (sensory) stimulus novelty and reward uncertainty and is amenable to both statistical and computational modeling of participant behavior. Notably, the authors took great care in adapting the paradigm for children and ensuring that all participants understood instructions involving the experimental manipulation (e.g., that the reward uncertainty resets every block while some stimuli might occur more often).

Another strength of this article is its multi-methodical approach to examining the core hypothesis that age-related changes in exploratory behavior are driven by how novelty and reward uncertainty influence choice evaluation. The statistical analyses appear sound and replicate prior findings. Moreover, the statistical analyses comport the results from a formal comparison of different reinforcement learning models (each implementing a different hypothesis). Notably, the authors demonstrate the validity of the comparison by showcasing model recovery on synthetic data.

Weaknesses

The only critical weakness I could identify pertains to the conclusion that children did not use reward uncertainty "to guide their decisions." This argument rests on the observation that children's choices were unaffected by reward uncertainty. However, the authors observed that RTs were affected by reward uncertainty, leading them to conclude that children may be aware of the reward uncertainty but don't factor it into the decision-making process. If RTs were regarded as a more sensitive measure than choices, then reward uncertainty might arguably still affect the decision process. This hypothesis may be better tested by fitting a drift-diffusion model to both choices and RTs and examining the effect of reward uncertainty on the rate of evidence accumulation. The advantages of this method would be that the model is fit using more information (choices and RTs) and that it allows dissociating mechanisms for biasing the decision process (e.g., rate of evidence accumulation) from mechanisms for delaying the decision process (response threshold).

Impact

From a conceptual point of view, the study contributes novel insights into developmental changes in decision-making behavior while, at the same time, offering a valuable replication of previous findings (Cockburn et al., 2022).

From a technical point of view, the adopted paradigm and modeling effort provide a valuable tool for other researchers to examine the distinctive contributions of novelty and reward uncertainty to human decision-making. Therefore, I applaud the authors for making their data, analysis, and code available on OSF.

1. Developmental shift in aversion to uncertainty. Is it the case that adults become more uncertainty-averse or that children are more uncertainty-seeking to begin with or both? Figure 3B suggests the former, although Figure 5 suggests the latter so it might be worth further (statistical) examination.

2. Effects of uncertainty on choices versus RTs in children. The manuscript argues that children "were able to track uncertainty, despite not using it to guide their decisions." This argument seems to rest on the observation that uncertainty did not affect choices but RTs. However, RTs are also impacted by the decision-making process and could be regarded as a more sensitive measure. Thus, I wonder if it is fair to argue that uncertainty did not influence children's choices. A cleaner examination of this question might involve fitting a drift-diffusion model (e.g., with the HDDM package) to both children's choices and RTs. An effect of uncertainty on the rate of evidence accumulation would indicate that uncertainty influences the decision-making process. In contrast, an effect on threshold would suggest that the decision is not biased based on uncertainty but generally slowed.

3. Perhaps I am missing something, but I wondered why the authors did not consider fitting a mixture RL model in which the interaction term (bias x novelty) was weighted depending on age (in addition to the main terms). The advantage of such an approach may be that, if hierarchically fitted, the weight could be directly examined.
