# Peer review - Round 1

Editors:
- Andreea Oliviana Diaconescu, University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.103734.3.sa0](https://doi.org/10.7554/eLife.103734.3.sa0)

This study makes an important contribution by showing that humans adapt learning rates rationally to environmental volatility yet systematically misattribute noise as volatility, demonstrating approximate rationality with simplified internal models. The evidence is compelling, encompassing a cleverly designed volatility-versus-noise paradigm, innovative lesion-based comparisons between reinforcement-learning and degraded Bayesian Observer Models, and convergent behavioural and pupillometric data. Expanding formal model comparisons (e.g., BIC/AIC) and directly contrasting RL and Bayesian fits to physiological markers would further enhance the work, but these are minor limitations that do not detract from the core findings.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103734.3.sa1](https://doi.org/10.7554/eLife.103734.3.sa1)

Summary:

The authors present an interesting study using RL and Bayesian modelling to examine differences in learning rate adaptation in conditions of high and low volatility and noise respectively. Through "lesioning" an optimal Bayesian model, they reveal that apparently suboptimal adaptation of learning rates results from incorrectly detecting volatility in the environment when it is not in fact present.

Strengths:

The experimental task used is cleverly designed and does a good job of manipulating both volatility and noise. The modelling approach takes an interesting and creative approach to understand the source of apparently suboptimal adaptation of learning rates to noise, through carefully "lesioning" and optimal Bayesian model to determine which components are responsible for this behaviour.

Weaknesses:

The model space could be more extensive, although the authors have covered the most relevant models for the question at hand.

Comments on revisions: I have no further recommendations for the authors, they have addressed my previous comments very well.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103734.3.sa2](https://doi.org/10.7554/eLife.103734.3.sa2)

Summary:

In this study, the authors aimed to investigate how humans learn and adapt their behavior in dynamic environments characterized by two distinct types of uncertainty: volatility (systematic changes in outcomes) and noise (random variability in outcomes). Specifically, they sought to understand how participants adjust their learning rates in response to changes in these forms of uncertainty.

To achieve this, the authors employed a two-step approach:

Reinforcement Learning (RL) Model:

They first used an RL model to fit participants' behavior, revealing that the learning rate was context-dependent-it varied based on the levels of volatility and noise. However, the RL model showed that participants misattributed noise as volatility, leading to higher learning rates in noisy conditions, where the optimal strategy would be to be less sensitive to random fluctuations.

Bayesian Observer Model (BOM):

To better account for this context dependency, they introduced a Bayesian Observer Model (BOM), which models how an ideal Bayesian learner would update their beliefs about environmental uncertainty. They found that a degraded version of the BOM, where the agent had a coarser representation of noise compared to volatility, best fit the participants' behavior. This suggested that participants were not fully distinguishing between noise and volatility, instead treating noise as volatility and adjusting their learning rates accordingly.

The authors also aimed to use pupillometry data (measuring pupil dilation) as a physiological marker to arbitrate between models and understand how participants' internal representations of uncertainty influenced both their behavior and physiological responses. Their objective was to explore whether the BOM could explain not just behavioral choices but also these physiological responses, thereby providing stronger evidence for the model's validity.

Overall, the study sought to reconcile approximate rationality in human learning by showing that participants still follow a Bayesian-like learning process, but with simplified internal models that lead to suboptimal decisions in noisy environments.

Strengths:

The generative model presented in the study is both innovative and insightful. The authors first employ a Reinforcement Learning (RL) model to fit participants' behavior, revealing that the learning rate is context-dependent-specifically, it varies based on the levels of volatility and noise in the task. They then introduce a Bayesian Observer Model (BOM) to account for this context dependency, ultimately finding that a degraded BOM-in which the agent has a coarser representation of noise compared to volatility-provides the best fit to the participants' behavior. This suggests that participants are not fully distinguishing between noise and volatility, leading to misattribution of noise as volatility. Consequently, participants adopt higher learning rates even in noisy contexts, where an optimal strategy would involve being less sensitive to new information (i.e., using lower learning rates). This finding highlights a rational but approximate learning process, as described in the paper.

Weaknesses:

While the RL and Bayesian models both successfully predict behavior, it remains unclear how to fully reconcile the two approaches. The RL model captures behavior in terms of a fixed or context-dependent learning rate, while the BOM provides a more nuanced account with dynamic updates based on volatility and noise. Both models can predict actions when fit appropriately, but the pupillometry data offers a promising avenue to arbitrate between the models. However, the current study does not provide a direct comparison between the RL framework and the Bayesian model in terms of how well they explain the pupillometry data. It would be valuable to see whether the RL model can also account for physiological markers of learning, such as pupil responses, or if the BOM offers a unique advantage in this regard. A comparison of the two models using pupillometry data could strengthen the argument for the BOM's superiority, as currently, the possibility that RL models could explain the physiological data remains unexplored.

The model comparison between the Bayesian Observer Model and the self-defined degraded internal model could be further enhanced. Since different assumptions about the internal model's structure lead to varying levels of model complexity, using a formal criterion such as Bayesian Information Criterion (BIC) or Akaike Information Criterion (AIC) would allow for a more rigorous comparison of model fit. Including such comparisons would ensure that the degraded BOM is not simply favored due to its flexibility or higher complexity, but rather because it genuinely captures the participants' behavioral and physiological data better than alternative models. This would also help address concerns about overfitting and provide a clearer justification for using the degraded BOM over other potential models.

Comments on revisions:

The authors have addressed all my questions. Congratulations on the impressive work accomplished by the authors!
