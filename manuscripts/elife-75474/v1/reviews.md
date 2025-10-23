# Peer review - Round 1

Editors:
- Catherine Hartley, https://ror.org/0190ak572 New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75474.sa0](https://doi.org/10.7554/eLife.75474.sa0)

This study adopts a within-participant approach to address two important questions in the field of human reinforcement learning: to what extent do estimated computational model parameters generalize across different tasks and can their meaning be interpreted in the same way in different task contexts? The authors find that inferred parameters show moderate to little generalizability across tasks, and that their interpretation strongly depends on task context.


---

# Peer review - Round 1

Editors:
- Catherine Hartley, https://ror.org/0190ak572 New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75474.sa1](https://doi.org/10.7554/eLife.75474.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Learning Rates Are Not All the Same: The Interpretation of Computational Model Parameters Depends on the Context" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Angela Radulescu (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The authors should carefully consider whether model misspecification may play a role in the observed results. More information should be provided on the set of models compared to validate the claim that the models presented are the best-fitting models and to establish whether each best-fitting model provides a comparably good fit to its respective task. For example, might models that incorporate various different forms of memory processes provide a better fit to the data for Tasks A and B? Moreover, to what degree are the claims in the current paper dependent on the precise specification of the model for each task? If a common set of parameters are included in each model specification, do the same claims hold?

2) While it may be beyond the scope of the current data, it would be helpful to include some discussion of test-retest reliability of the current tasks, and of RL tasks more generally, and how these measures relate to expectations about generalizability.

3) Was there a reason that the authors used PCA rather than factor analysis to extract common components across task parameters/behavioral indices?

4) The finding that both the positive learning rate and inverse temperature generalized across tasks is an important result that is not given the same weight in the exposition of the results as those parameters that exhibit generalization failures. The abstract and title could be edited to provide a more balanced reflection of these findings and to eliminate the somewhat "straw man"-ish implication that the field expects that the absolute values of learning rates should be the same across tasks.

5) To determine what might be a reasonably expected ceiling on the degree of generalizability, as suggested by the reviewer, the authors could simulate data from agents using the same generative parameters across the three tasks and report the correlations between the resulting parameters estimates.

6) Descriptions of the tasks that capture their distinguishing features through the lens of Markov Decision Process theory might be valuable to contextualize the current results within a broader reinforcement learning literature.

The reviewers also made a number of concrete suggestions for ways in which the manuscript might be improved that the authors should consider carefully.

Reviewer #1 (Recommendations for the authors):

I hope that the above three points will be discussed in the Discussion section or in the relevant part of the Method section. In the following, I will discuss some minor points.

p 4, Line 87

The citations for clinical research areas [15-18] seem to be mostly review articles in computational psychiatry, and I am not sure if the literature explicitly addressing the inconsistencies discussed here is properly cited. For example, a review of the lack of agreement between studies on whether the association with depression appears in learning rates or temperature parameters (Robinson and Chase, 2017, Computational Psychiatry, 1, 208-233) and the literature cited there may also be included.

p.14

The symbol '$' in Table 4 needs to be explained.

p.25

Figure 5: Is 'B' the correct label for 'Panel C'?

Reviewer #2 (Recommendations for the authors):

With regard to obtaining a ceiling on correlations that indicate relative generalizability, it might be possible to get an answer to this w/o collecting new data by simulating behavior of the *same N agents* (with uniformly sampled params, or params sampled from prior group distribution used in the hierarchical fit, or params sampled from distributions centered around ideal observer values). If we then re-run model fitting on these simulated datasets, what is the max correlation between LRs estimated from different tasks? And can we bootstrap to obtain some CIs around this ceiling? In general, the authors consider the tasks to be fairly similar, but I'm not sure that is actually the case -- even A and C, which share the most similarities, differ markedly in the reward function (probabilistic vs. deterministic).

With regard to clarifying the interaction between memory parameters and LR/exploration, have authors specifically determined the degree to which memory-related parameters F and/or K interact with α_+/β, e.g. by plotting likelihood function surfaces as a function of pairs of parameters? I also couldn't find the pairwise correlation between F (Task A) and F( Task C) in this section, were these reported? I'm guessing these were not significant based on the results in 2.1.4 showing F in A does not predict F in B, but it would be helpful to include them for completeness.

The current study was not designed for systematically varying different aspects of the MDP to see how this affects inferred parameter generalizability and interpretability, which is okay. But perhaps one step the paper can make in this direction of theoretical consistency is to explicitly name the features of each task from an MDP theory standpoint, or at least additionally include this as a table or additional panel in Figure 1. e.g. size of state and action space (+ mapping to "set size" jargon), reward function, etc. Authors do this at several points in the paper (including the appendix), and this can only help as a practice that allows the RL community to think about tasks in a common way. In the present study, this convention can illuminate why the tasks presented here are actually quite different from one another. Task A: 4 states (1 per trial), 2 actions (visible on screen), stable stochastic reward function; Task B: stateless, 2 actions, reversal in stochastic reward function; Task C: RL-WM task: 2-5 states (1 per trial), 3 actions (not visible on screen), stable deterministic reward function.

With regard to model selection:

– For the section describing the computational models for the first time, it would be helpful to summarize info about parameters in a table, emphasizing those parameters common across best-fitting models. For example, just from a rhetorical standpoint, it seemed strange that Tasks A and C are not both best fit by a model that allows LR- to vary freely, even though both tasks are taken as similar in the paper's taxonomy.

– It would be helpful to show upfront in a figure that each best-fitting model explains data in its respective task as well as models in the other tasks. i.e. can we say that each model explains about the same number of choices in every task? This is important because incomplete models are the reason we might see "contamination" whereby variance explained by one parameter in a task is explained by a different parameter in a second task.

– I did wonder here to what extent some of the inconsistencies can be explained by the fact that authors only instantiated a model that formalizes explicit memory demands only for Task C. We know from past work (e.g. by Bornstein and colleagues) that even in stateless bandit tasks such as Task B, explicit memory of outcomes stretching back tens of trials ago impact decisions. Task A is also potentially solvable by a WM module that keeps track of explicit state-action associations, bearing similarity to Task C. Is the forgetting parameter F enough to capture all the memory processes that might *also* be present in Task A? And would a RL-WM model with a fixed set size do better at explaining behavior on Task A? The lack of specificity in the noise/exploration parameter for Task A (evidenced by the fact that it was correlated with different parameters in other tasks, including working memory weight from C), strongly supports this possibility, as this parameter is known to absorb unexplained variance.

Finally, I think it is important to provide a bit more detail upfront about the training and instructions protocol for each task, and, to the extent that it is possible, provide evidence that instruction comprehension is not related to parameter differences. One simple analysis here would be to examine the "lose-stay" distribution in Tasks B and C and look for any evidence of bimodality that can be traced to how instructions were presented. I would also be curious if this distribution varies with age, potentially explaining the striking divergence in age trajectories for LR- in Tasks B and C.
