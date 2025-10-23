# Peer review - Round 1

Editors:
- Valentin Wyart, Inserm France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86892.3.sa0](https://doi.org/10.7554/eLife.86892.3.sa0)

This study investigates how humans make decisions on the difficulty of perceptual categorization tasks. The study finds that such judgments are best described by an evidence-accumulation model that includes a dynamic comparison of difficulty-related evidence, which terminates when the difference in evidence between two tasks reaches a predetermined bound - a valuable finding for research in perceptual decision-making. The paper provides compelling behavioral evidence for the proposed model through: 1/ quantitative model selection/validation procedures, and 2/ qualitative analyses of the relation between the optimal model of the task and the human data (and the proposed model).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.86892.3.sa1](https://doi.org/10.7554/eLife.86892.3.sa1)

Meta-cognition, and difficulty judgments specifically, is an important part of daily decision-making. When facing two competing tasks, individuals often need to make quick judgments on which task they should approach (whether their goal is to complete an easy or a difficult task).

In the study, subjects face two perceptual tasks on the same screen. Each task is a cloud of dots with a dominating color (yellow or blue), with a varying degree of domination - so each cloud (as a representation of a task where the subject has to judge which color is dominant) can be seen an easy or a difficult task. Observing both, the subject has to decide which one is easier.

It is well-known that choices and response times in each separate task can be described by a drift-diffusion model, where the decision maker accumulates evidence toward one of the decisions ("blue" or "yellow") over time, making a choice when the accumulated evidence reaches a predetermined bound. However, we do not know what happens when an individual has to make two such judgments at the same time, without actually making a choice, but simply deciding which task would have stronger evidence toward one of the options (so would be easier to solve).

It is clear that the degree of color dominance ("color strength" in the study's terms) of both clouds should affect the decision on which task is easier, as well as the total decision time. Experiment 1 clearly shows that color strength has a simple cumulative effect on choice: cloud 1 is more likely to be chosen if it is easier and cloud 2 is harder. Response times, however, show a more complex interactive pattern: when cloud 2 is hard, easier cloud 1 produces faster decisions. When cloud 2 is easy, easier cloud 1 produces slower decisions.

The study explores several models that explain this effect. The best-fitting model (the Difference model is the paper's terminology) assumes that the decision-maker accumulates evidence in both clouds simultaneously and makes a difficulty judgment as soon as the difference between the values of these decision variables reaches a certain threshold. Another potential model that provides a slightly worse fit to the data is a two-step model. First, the decision maker evaluates the dominant color of each cloud, then judges the difficulty based on this information.

Importantly, the study explores an optimal model based on the Markov decision processes approach. This model shows a very similar qualitative pattern in RT predictions but is too complex to fit to the real data. Possibly, the fact that simple approaches such as the Difference model fit the data best could suggest the existence of some cognitive constraints that play a role in difficulty judgments and could be explored in future research.

The Difference model produces a well-defined qualitative prediction: if the dominant color of both clouds is known to the decision maker, the overall RT effect (hard-hard trials are slower than easy-easy trials) should disappear. Essentially, that turns the model into the second stage of the two-stage model, where the decision maker learns the dominant colors first. The data from Experiment 2 impressively confirms that prediction and provides a good demonstration of how the model can explain the data out-of-sample with a predicted change in context.

Overall, the study provides a very coherent and clean set of predictions and analyses that advance our understanding of meta-cognition. The field would benefit from further exploration of differences between the models presented and new competing predictions (for instance, exploring how the sequential presentation of stimuli or attentional behavior can impact such judgments). Finally, the study provides a solid foundation for future neuroimaging investigations.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.86892.3.sa2](https://doi.org/10.7554/eLife.86892.3.sa2)

Starting from the observation that difficulty estimation lies at the core of human cognition, the authors acknowledge that despite extensive work focusing on the computational mechanisms of decision-making, little is known about how subjective judgments of task difficulty are made. Instantiating the question with a perceptual decision-making task, the authors found that how humans pick the easiest of two stimuli, and how quickly these difficulty judgments are made, are best described by a simple evidence accumulation model. In this model, perceptual evidence of concurrent stimuli is accumulated and difficulty is determined by the difference between the absolute values of decision variables corresponding to each stimulus, combined with a threshold crossing mechanism. Altogether, these results strengthen the success of evidence accumulation models in describing human decision-making, now extending it to judgments of difficulty.

The manuscript addresses a timely question and is very well written, with its goals, methods and findings clearly explained and directly relating to each other. The authors are specialists of evidence accumulation tasks and models. Their modelling of human behaviour within this framework is state-of-the-art. In particular, their model comparison is guided by qualitative signatures which are diagnostic to tease apart different models (e.g., the RT criss-cross pattern). Human behaviour is then inspected for these signatures, instead of relying exclusively on quantitative comparison of goodness-of-fit metrics.

The study has potential limitations well flagged by the authors after the revision process. The main limitation pertains to the (dis)similarity between the behavioural task used in the study and difficulty judgments people actually do in real world (and which are well illustrated in the introduction). First, difficulty judgments made in the task never impact the participant (a new trial simply follows) while difficulty judgments in the wild often determine whether to pursue or quit the corresponding task, which can have consequences years after the difficulty estimation (e.g., deciding to engage in a particular academic path as a function of the estimated difficulty). Second, while trial-by-trial feedback is delivered in the task, difficulty estimation in the wild has to be made with partial information and feedback is either absent or delayed. How much these differences are key in providing an accurate computational description of human difficulty judgments will likely require further research.

Another limitation is the absence of models based on computational principles other than evidence accumulation. Although there are good reasons to favour evidence accumulation models in these settings (as mentioned by the authors in their manuscript), showing that evidence accumulation models would have won against competitors would have further strengthened the authors' claim that difficulty judgment about perceptual information are firmly anchored in the principles of evidence accumulation.

These limitations should not distract the reader from the impact of the present work, which will likely be wide, spanning the whole field of decision-making, and this across species. It will echo in particular with the many other seminal studies that have relied on a similar theoretical account of behaviour and brain activity (evidence accumulation). In addition, this study will hopefully inspire novel task designs aiming at addressing difficulty judgment estimations in controlled lab experiments, possibly with features closer to real world difficulty estimation (e.g., long-term consequences of difficulty estimation and absence of feedback).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.86892.3.sa3](https://doi.org/10.7554/eLife.86892.3.sa3)

The manuscript presents novel findings regarding the judgment of difficulty of perceptual decisions. In the main task (Experiment 1), participants accumulated evidence over time about two tasks, patches of random dot motion, and were asked to report for which patch it would be easier to make a decision about its dominant color, while not explicitly making such decision(s). By fitting several alternative models, authors demonstrated that while accuracy changes as a function of the difference between stimulus strengths, reaction times of such decisions are not solely governed by the difference in stimulus strength, but (also) by the difference in absolute accumulated evidence for color judgment of the two stimuli ('Difference model'). Predictions from the best fitted model were then tested with a new set of conditions and participants (Experiment 2). Here, authors eliminated part of the uncertainty by informing participants about the dominant color of the two stimuli ('known color' condition) and showing that reaction times were faster compared to the 'unknown color' task, and only depended on the difference between stimulus strengths.

The paper deals with a valuable question about a metacognitive aspect of perceptual decision making, which was only sparsely addressed before. The paper is very well written, figures and illustrations clearly accompanied the text, and methods and modeling are rigor. The authors also address the concern that a difficulty judgment might be a confidence estimation, another metacognitive judgment of perceptual decisions, by fitting a Confidence model to the 'known color' condition in Experiment 2 and showing that this model performs worse compared to the Difference model. This is an important control analysis, given the possibility that humans might make an implicit decision about the dominant color of each patch, and then report their level of confidence.

This work is likely to be of great interest in the field of behavioral modeling of perceptual decision making, and might encourage further investigations of how judging the difficulty of a task affects subsequent decisions about the same task.
