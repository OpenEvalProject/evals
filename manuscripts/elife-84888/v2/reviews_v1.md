# Peer review - Round 1

Editors:
- Thorsten Kahnt, National Institute on Drug Abuse Intramural Research Program United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84888.sa0](https://doi.org/10.7554/eLife.84888.sa0)

This study provides convincing evidence that the fidelity of neural representations of task states is associated with assigning credit to these states. The topic is timely and the results are important for understanding the neural mechanisms of reinforcement learning. The manuscript will be highly relevant for readers interested in cognitive and decision neuroscience, as well as reinforcement learning.


---

# Peer review - Round 1

Editors:
- Thorsten Kahnt, National Institute on Drug Abuse Intramural Research Program United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84888.sa1](https://doi.org/10.7554/eLife.84888.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Prefrontal cortex state representations shape human credit assignment" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Christian Büchel as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Rui Ponte Costa (Reviewer #2).

Apologies for the long delay in getting back to you. The reviewers have now discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

As you can see, both reviewers agreed that your manuscript addressed an important and timely topic. However, they also identified key weaknesses that should be addressed with substantial text revisions, new analysis, and/or data.

The list below highlights two key concerns, but please also consider the points raised in the individual critiques.

1. Potential stimulus confounds (reviewer 1 public review, point 1). Ideally, you would address this with new data showing that the results hold when the stimuli between the social and non-social tasks are matched. Alternatively, you could change the language about social vs. non-social to complex vs. simple in most of the manuscript, and refer to the potential role of social vs non-social stimuli in the discussion.

2. Are effects driven by the strength of neural representations rather than learning signals (reviewer 2 public review, point 3)? Please address this concern through additional analysis as it is central to your main conclusions.

Reviewer #1 (Recommendations for the authors):

This study uses fMRI and computational modeling to examine the relationship between credit assignment and neural stimulus representations, and compare this relationship between yoked social and non-social reinforcement learning tasks. The authors find that credit assignment is more accurate in the social task and that this is mirrored in the strength of neural stimulus representations in the PFC. They also report evidence for overlapping neural representations between the choice and feedback phases.

The question addressed in this study is timely and interesting, and the manuscript is well-written. However, there are several shortcomings in the experimental design and analytic approach that limit what can be concluded from these results.

1. A focus of the study are differences between social and non-social tasks. The key distinction between these tasks is the stimulus set: the social task uses faces as stimuli whereas the non-social task uses a bandit symbol in different colors. This potentially confounds the social vs non-social learning domain with the salience, complexity, etc. of the stimuli used. Thus, it is unclear whether the behavioral and neural results reflect credit assignment in social vs. non-social domains or the well-known effects of stimulus features on learning.

2. The authors use computational modeling to compare different mechanisms of learning (working memory vs credit assignment). However, although these two mechanisms are not mutually exclusive and there is no attempt to capture both mechanisms within the same model.

3. The authors use the term 'state' when referring to different stimuli within each task. This is misleading because 'states' are typically conceptualized to be abstract and not tied to specific stimuli. The analyses presented in the manuscript do not dissociate state identity from stimulus identity, and so it would be more accurate to refer to 'stimulus identity' rather than 'state identity' in the context of the current manuscript.

4. My biggest concern is related to potential stimulus confounds in the social vs non-social tasks. Faces are more complex, salient, and meaningful than the colored bandits. We know from decades of learning and memory research that such stimulus features determine the rate of learning and so any differences between conditions may have nothing to do with social vs non-social but are entirely driven by these features.

Relatedly, given the choice-related RSA results reflect representations of stimulus identity, any differences between the two conditions could be driven entirely by better decoding of more complex stimuli.

There are two solutions to this issue. Either you do additional experiments and show that a reasonable set of features does not explain differences between the two tasks, or you revise the manuscript to remove all language about social vs non-social and acknowledge that the differences between the tasks could be entirely driven by differences in stimulus features.

5. Your modeling approach is designed to test (among other things) whether working memory or credit assignment mechanisms better account for the behavioral data. Given that these mechanisms are not mutually exclusive, it would be important to include a model that captures both mechanisms.

6. I think using the term 'state' when referring to 'stimulus' is misleading. States are generally thought to be abstract and not tied to specific stimulus configurations. To dissociate states and stimuli, you'd need an experiment where the same state is evoked by different stimuli. Your design actually allows you to do that if you assume that faces and corresponding bandits evoke the same state.

7. I may be wrong here, but if I understand your description of the cross-timepoint RSA in the method section correctly, I wonder whether this analysis could still be confounded by the temporal proximity of choice and feedback phase. As far as I understand, you computed the similarity of choice and feedback phases within odd trials and separately within even trials. Then you computed the matrix product between the odd and even trial neural RDMs. Couldn't any signals (including those driven by vascular effects or noise) that linger from the choice phase into the feedback phase explain the cross-phase similarity within the odd and even trials? It seems it would be better to compute two neural RDMs such that the choice phase comes from odd trials and the feedback phase comes from even trials (and vice versa), and then average the two RDMs. This way, the similarity between the choice and feedback phase is less likely to result from autocorrelations

8. How were the ROIs selected? I assume there were more areas that represented stimulus identity, no?

Reviewer #2 (Recommendations for the authors):

In this manuscript the authors use a combination of reinforcement learning modelling and fMRI to study the fidelity of state representations in the frontal cortex and whether these representations predict the ability of (individual) participants for credit assignment.

Strengths:

1. This study provides a nice combination of reinforcement learning modelling and fMRI studies, which enabled the authors to link computational principles with neuronal representations.

3. The experimental paradigm is also interesting, contrasting social and non-social tasks. It suggests very interesting differences between the two in terms of investment, but also in terms of neural representations.

4. Finally, this study might make substantial advances in our understanding of individual differences in terms of credit assignment, a critical part of learning and adaptability. However, this is not entirely clear (see below).

Weaknesses:

1. The manuscript could present some of the results in a more gradual way, that makes it accessible to a general reader. I also find that there are generally long relatively complex sentences that make it hard to follow. For example: "We leverage these potential differences to evaluate whether the brain adaptively adjusts the fidelity of state representations across contexts to mediate the selectivity of causal learning.".

2. There is in my view a need to clarify what is meant by credit assignment (CA). For example, the way the models are described in the main text make it seem that some models perform credit assignment whereas others do not. From what I can see all these models have to perform some form of credit assignment, as they all atribute credit to model parameters/states, which I think would also make model 1 a CA model.

3. One of the key points made by the authors is that individual differences are driven by the strength of neural representations, and not by the magnitude of learning signals. Unfortunately, I fail to see how this conclusion is supported by the analysis of the data. I believe that this is interpretation builds on their correlation analysis between the representations and the model fits (Figure 5D and 6C). However, the model itself contains an explicit learning signal (δ: prediction error), so it is not clear to me how can the authors disentangle the neuronal representations from the learning signal using this analysis.

4. The model and some of the methods are not described in enough detail. For example, it is not stated what some of the parameters are. Although the models used appear to be standard in the field, no links/citations to classical RL models are made.

Claims:

Several claims are supported by the data/analysis, but it is not clear to me if one of the central claims is (see one of the weakness points above).

1. One of the potentially very interesting points made by the authors is about what causes individual differences in terms of CA. However, I fail to see how they can use the CA fit without implicitly also considering learning signals -- learning signals are an implicit part of their model (i.e. there is a δ = prediction error). Not sure how this can be addressed, but maybe there is something I'm missing and this is not a problem at all? On a related point, I failed to see a discussion on this very important part of the manuscript, discussing what would be the key contribution of the paper.

2. The text could be improved by making more smoother/gradual descriptions of the results/ideas. For example, I find that there is a lot of information in the final part of the section "Although these outcomes should not inform choices on the current trial given the generative task structure…" (until the end). To make it more accessible to the general reader I suggest that you present this information more gradually and provide intermediate (brief) summaries of what it means.

3. So I think it would be better to clarify that these are all different variants of CA models. This does not change your interpretation in any way but would make the story more clear. Also, to follow the modelling more easily I would suggest giving specific names to each model like you already do for the v-CA model. I note that this is done in Figure S2, but should also be included in the main text, and in the methods when referring to the methods, for clarity. This would also make the link with Figure 3 easier to follow. For example, at the moment it's unclear exactly to which model Figure 3b and c refer.

4. On page 7 and Figure 3 you use the term "spread" again, but this was only referred to very early on, so at this point appears out of place. Would be important to highlight what this means and how the models capture this spread. Also, in Figure 3 the spread is contrasted with CA precision, given that these two elements are critical for understanding Figure 3, it would be important to clearly define them in the main text before introducing the results of Figure 3. Also, in Figure 3 are the credit matrices obtained by running the models? If so, how? Clarify.

5. One possible prediction for the neuronal representations of PE found in PFC is that they should weaken over learning if they underlie the learning signal. As this form a critical component of any credit assignment/learning model, it would be interesting/important to explore this. I imagine this could be easily tested with your data by analysing how the PE-specific representations change over learning.

6. There is some lack of clarity in the description of the model/analysis: (i) The baseline RL model, seems to be exactly the Rescorla-Wagner rule. If so please refer to it as so. (ii) The AIC is usually given by: AIC = – 2ln(L) + 2k, not AIC = – 2ln(L) – 2k, as given in the methods. Please clarify. (iii) What is the prior in the decay model? It does not appear to be given. (iv) The Q variable is usually reserved for Q-learning in RL, which models explicitly the value of state-action pairs, but this does not appear to be the case here. Instead, to be consistent with the literature, I suggest that you use the variable V. It's important that the authors ensure that all the details are given, and parameters described.
