# Peer review - Round 1

Editors:
- Alicia Izquierdo, University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69748.sa0](https://doi.org/10.7554/eLife.69748.sa0)

Following inclusion of new modeling and data presentation, authors have more clearly demonstrated that equivalent performance is seen across males and females in terms of reward rate, yet achieved via different successful strategies. This is an important contribution to the growing literature on sex differences in reinforcement learning.


---

# Peer review - Round 1

Editors:
- Alicia Izquierdo, University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69748.sa1](https://doi.org/10.7554/eLife.69748.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Sex differences in learning from exploration" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Alicia Izquierdo as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kate Wassum as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Chen et al., trained male and female animals on an explore/exploit (2-armed bandit) task. Despite similar levels of accuracy in these animals, authors report higher levels of exploration in male than in female mice. The patterns of exploration were analyzed in fine-grained detail: males are less likely to stop exploring once exploring is initiated, whereas females stop exploring once they learn. Authors find that both learning rate (α) and noise parameter (β) increase in exploration trials in a hidden Markov model (HMM). When reinforcement learning (RL) models were fitted to animal data, they report females had a higher learning rate and over days of testing, suggesting higher meta-learning in females. They also report that of the RL models they fit, the model incorporating a choice kernel updating rule was found to fit both male and female learning. The results suggest one should pay greater attention to the influence of sex in learning and exploration. Another important takeaway from this study is that similar levels of accuracy do not imply similar strategies. There are 2 categories of essential revisions suggested by Reviewers:

1) There was a general concern that reframing of conclusions may be warranted due to the major results possibly reflecting learning more than exploration. Female rats may learn the task better than male rats. For more clarity on this issue, reviewers request that authors present more primary behavioral data (p(reward,obtained) vs time (days), reaction times over time, etc.) to justify their conclusions. It was also unclear how reaction times were calculated and how "steady state" was operationalized.

2) Reviewers also asked for better justification and details for both the hidden Markov model and reinforcement learning parameters. If for example, male rats simply learn the task more poorly and behave more randomly, this would manifest as more exploration in the HMM model. Additional analyses are needed to strengthen authors' claims using the HMM model- the effect of obtained reward on state transitions, and biased exploitations should be further explored as there are presently a number of unjustified assumptions.

Please address these essential concerns (which are detailed in the reviews below), as well as the reviewers other comments.

Reviewer #1 (Recommendations for the authors):

Chen et al., trained male and female animals on an explore/exploit (2-armed bandit) task. Despite similar levels of accuracy in these animals, authors report higher levels of exploration in males than in females. The patterns of exploration were analyzed in fine-grained detail: males are less likely to stop exploring once exploring is initiated, whereas female mice stop exploring once they learn. Authors find that both learning rate (α) and noise parameter (β) increase in exploration trials in a hidden Markov model (HMM). When reinforcement learning (RL) models were fitted to animal data, they report females had a higher learning rate and over days of testing, suggesting higher meta-learning in females. They also report that of the RL models they fit, the model incorporating a choice kernel updating rule was found to fit both male and female learning. The results do suggest one should pay greater attention to the influence of sex in learning and exploration. Another important takeaway from this study is that similar levels of accuracy do not imply similar strategies. I have suggestions for clarity in data presentation and interpretation.

One of the first sections in the Results section dives straight away into the HMM, but in my opinion, authors do not present enough of the primary behavioral data- perhaps I missed this, but can we see p(reward, obtained) over sessions for males and females (more information than Figure 1B)? And the reaction times in Figure 1C, are these reaction times to make a left/right response or reaction times to collect rewards? Can authors show both, as a function over time?

What is the cited rationale for the different RL models and their parameters? If the RLCK is the best fit for both males and females, does this lend support to the idea that though overall learning many not differ between males and females, the strategies are not well captured by RL? Please clarify.

Authors should clarify the difference between learning and "steady state." How was this operationally defined and measured? This was a bit lost in the data presentation.

The lines 430-432 about rodent behavioral tasks are unclear to me: "However, the vast majority of these tasks were not designed with computational models in mind, and as a result, we are unable to assess whether similar latent cognitive variables are influencing behavior in humans and rodents." There are several groups that use touchscreen-response methods paired with computational modeling. Do the authors mean they do not have access to similar databases to compare these latent variables across species? Authors may want to clarify how these experiments uniquely identify latent cognitive variables not previously explored with similar methods.

Reviewer #2 (Recommendations for the authors):

1. How is reaction time computed here? Do you remove outliers (extremely long RTs)? Is there a way to separate exploring from guessing in RT (given that behaviorally they are confounded)?

2. State transitions are not value dependent in the HMM model. Another value independent way of "exploration" is by having a lapse rate in the RL model. I am curious about whether there is a lapse rate difference across sex (and possibly no differences in the temperature term).

3. There is the inset panel (ROC curve) in all density figures except Figure 3D.

4. I like your dynamic landscape illustration of the fitted HMM (Figure 1G).

Reviewer #3 (Recommendations for the authors):

(1) A great proportion of reported results and analysis rely on the extracted latent states from the proposed HMM. While HMM is proposed to provide a model free analysis of behavior, certain choices regarding the HMM model need further justification:

(1.1) Most importantly, authors assume that only most recent state determines the state in the next trial. However, I argue that most recent obtained reward is another determinant of the state in the next trial and should be added to the model. This way instead of using a naïve HMM, and then exploring learning in explore/exploit trials, authors can compare HMM parameters.

(1.2) Proposed HMM model also assumes that exploit states are uniform across the options. Do authors have any evidence supporting this assumption? Side biases are commonly observed in animals and humans. Extracted RL parameters also confirm this. Please comment.

(1.3) Moreover, the model assumes that the mice had to pass through exploration in order to start exploiting a new option. Do authors have any evidence supporting this assumption? What will happen to the results if this assumption is lifted? Please comment.

(2) Page 10, line 252: Please provide a more quantitative comparison of models' choice behavior (and not just RLCK) and the animals' behavior for all sessions. Also, there are no tick-marks on the y-axis.

(3) How much overlap exists between the extracted latent dynamics from HMM and that of previously proposed models mentioned in the methods (Daw et al., 2006; Jepma and Nieuwenhuis, 2011; Pearson et al., 2009)? It would be helpful to show the extent that results from these different methods deviate/overlap with each other.

(4) Do authors see any differences between amount of exploration/exploitation at the beginning vs at the end of a session? How about across days? The fact that meta learning is observed, suggests that even in a single session, changes in the strategy of animals might be expected.
