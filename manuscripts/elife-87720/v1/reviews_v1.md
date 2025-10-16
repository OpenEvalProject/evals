# Peer review - Round 1

Editors:
- Claire M Gillan, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87720.4.sa0](https://doi.org/10.7554/eLife.87720.4.sa0)

This is a valuable paper demonstrating the validity of a novel task that could advance the field of reinforcement learning to better incorporate threat processing in approach-avoidance-conflict. A compelling methodology includes the use of online samples and computational modelling, psychometrics, discovery/replication and pre-registration. This work provides a foundation for future work, which is required to establish this task as relevant to psychopathology and treatment.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87720.4.sa1](https://doi.org/10.7554/eLife.87720.4.sa1)

This paper describes the development and initial validation of an approach-avoidance task and its relationship to anxiety. The task is a two-armed bandit where one choice is 'safer' - has no probability of punishment, delivered as an aversive sound, but also lower probability of reward - and the other choice involves a reward-punishment conflict. The authors fit a computational model of reinforcement learning to this task and found that self-reported state anxiety during the task was related to a greater likelihood of choosing the safe stimulus when the other (conflict) stimulus had a higher likelihood of punishment. Computationally, this was represented by a smaller value for the ratio of reward to punishment sensitivity in people with higher task-induced anxiety. They replicated this finding, but not another finding that this behavior was related to a measure of psychopathology (experiential avoidance), in a second sample. They also tested test-retest reliability in a sub-sample tested twice, one week apart and found that some aspects of task behavior had acceptable levels of reliability. The introduction makes a strong appeal to back-translation and computational validity. The task design is clever and most methods are solid - it is encouraging to see attempts to validate tasks as they are developed. The lack of replicated effects with psychopathology may mean that this task is better suited to assess state anxiety, or to serve as a foundation for additional task development.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87720.4.sa2](https://doi.org/10.7554/eLife.87720.4.sa2)

Summary:

The authors develop a computational approach-avoidance-conflict (AAC) task, designed to overcome the limitations of existing offer based AAC tasks. The task incorporated likelihoods of receiving rewards/ punishments that would be learned by the participants to ensure computational validity and estimated model parameters related to reward/punishment and task induced anxiety. Two independent samples of online participants were tested. In both samples participants who experienced greater task induced anxiety avoided choices associated with greater probability of punishment. Computational modelling revealed that this effect was explained by greater individual sensitivities to punishment relative to rewards.

Strengths:

Large internet-based samples, with discovery sample (n = 369), pre-registered replication sample (n = 629) and test-retest sub group (n = 57). Extensive compliance measures (e.g. audio checks) seek to improve adherence.

There is a great need for RL tasks that model threatening outcomes rather than simply loss of reward. The main model parameters show strong effects and the additional indices with task based anxiety are a useful extension. Associations were broadly replicated across samples. Fair to excellent reliability of model parameters is encouraging and badly needed for behavioral tasks of threat sensitivity.

The task seems to have lower approach bias than some other AAC tasks in the literature.

Appraisal and impact:

Overall this is a very strong paper, describing a novel task that could help move the field of RL forward to take account of threat processing more fully. The large sample size with discovery, replication and test-retest gives confidence in the findings. The task has good ecological validity and associations with task-based anxiety and clinical self-report demonstrate clinical relevance. Test-retest of the punishment learning parameter is the only real concern. Overall this task provides an exciting new probe of reward/threat that could be used in mechanistic disease models.

Additional context:

The sex differences between the samples are interesting as effects of sex are commonly found in AAC tasks. It would be interesting to look at the main model comparison with sex included as a covariate.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87720.4.sa3](https://doi.org/10.7554/eLife.87720.4.sa3)

This study investigated cognitive mechanisms underlying approach-avoidance behavior using a novel reinforcement learning task and computational modelling. Participants could select a risky "conflict" option (latent, fluctuating probabilities of monetary reward and/or unpleasant sound [punishment]) or a safe option (separate, generally lower probability of reward). Overall, participant choices were skewed towards more rewarded options, but were also repelled by increasing probability of punishment. Individual patterns of behavior were well-captured by a reinforcement learning model that included parameters for reward and punishment sensitivity, and learning rates for reward and punishment. This is a nice replication of existing findings suggesting reward and punishment have opposing effects on behavior through dissociated sensitivity to reward versus punishment.

Interestingly, avoidance of the conflict option was predicted by self-reported task-induced anxiety. Importantly, when a subset of participants were retested over 1 week later, most behavioral tendencies and model parameters were recapitulated, suggesting the task may capture stable traits relevant to approach-avoidance decision-making.

The revised paper commendably adds important additional information and analyses to support these claims. The initial concern that not accounting for participant control over punisher intensity confounded interpretation of effects has been largely addressed in follow-up analyses and discussion.

This study complements and sits within a broad translational literature investigating interactions between reward/punishers and psychological processes in approach-avoidance decisions.
