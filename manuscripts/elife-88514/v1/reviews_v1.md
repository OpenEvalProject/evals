# Peer review - Round 1

Editors:
- Noah J Cowan, Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88514.3.sa0](https://doi.org/10.7554/eLife.88514.3.sa0)

This study represents a step towards integrating human and non-human primate research towards a broader understanding of the neural control of motor strategies. It could offer valuable insights into how humans and non-human primates (Rhesus monkeys) manage visuomotor tasks, such as stabilizing an unstable virtual system, potentially leading to discoveries in neural behaviour mechanisms. While the evidence is mostly solid, some results, particularly from the binary classification of control strategies for non instructed behaviour, require further validation before it could be conclusively interpreted.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88514.3.sa1](https://doi.org/10.7554/eLife.88514.3.sa1)

The present study examines whether one can identify kinematic signatures of different motor strategies in both humans and non-human primates (NHP). The Critical Stability Task (CST) requires a participant to control a cursor with complex dynamics based on hand motion. The manuscript includes datasets on performance of NHPs collected from a previous study, as well as new data on humans performing the same task. Further human experiments and optimal control models highlight how different strategies lead to different patterns of hand motion. Finally, classifiers were developed to predict which strategy individuals were using on a given trial.

There are several strengths to this manuscript. I think the CST task provides a very useful behavioural task to explore the neural basis of voluntary control. While reaching is an important basic motor skill and commonly studied, there is much to learn by looking at other motor actions to address many fundamental issues on the neural basis of voluntary control.

I also think the comparison between human and NHP performance is important as there is a common concern that NHPs can be overtrained in performing motor tasks leading to differences in their performance as compared to humans. The present study highlights that there are clear similarities in motor strategies of humans and NHPs. While the results are promising, I would suggest that the actual use of these paradigms and techniques likely need some improvement/refinement. Notably, the threshold or technique to identify which strategy an individual is using on a given trial needs to be more stringent given the substantial overlap in hand kinematics between different strategies.

The most important goal of this study is to set up future studies to examine how changes in motor strategies impact neural processing. The revised manuscript has improved the technique for identifying which strategy appears to be performed by the individual. A pivotal assumption is that one can identify control strategies from differences in behaviour. As I'm sure the authors know, this inversion of the control problem is not trivial and so success requires that there are only a few 'reasonable' strategies to solve the control problem, and that these strategies lead to distinct patterns of behavior. Many of the concerns raised by myself and the other reviewers relate to this challenge. The revised manuscript now uses a more strict criteria which is good improvement.

One of the values of this paper is to start to develop the tools and approaches to address neural basis of control. The strength of the present manuscript is that it includes modelling, explicit strategy instructions in humans, and then analysis of free-form performance in humans and non-human primates. Given the novelty of this question and approach, there likely are many ways that the techniques and approaches could be improved, but I think they've done a great start. Their approach is quite clever and provides an important blueprint for future studies.

One weakness at this point is that there is still substantial overlap in behavoural performance predicted between strategies, as some human participants given an explicit strategy were almost equally categorized as reflecting the other strategy. I'm glad to see the addition of the model performance on perturbation trials as this additional figure clearly highlights much greater separation in performance than when observing natural behavior. While it is not reasonable to expand beyond this for the present manuscript, I think it is essential for this group to develop the perturbation paradigm (and potentially other approaches) that can better isolate behavioral signatures of different control strategies. I think future work will be strengthened by having multiple experimental angles to interpret the neural activity.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88514.3.sa2](https://doi.org/10.7554/eLife.88514.3.sa2)

This paper considers a challenging motor control task - the critical stability task (CST) - that can be performed equally well by humans and macaque monkeys. This task is of considerable interest since it is rich enough to potentially yield important novel insights into the neural basis of behavior in more complex tasks that point-to-point reaching. Yet it is also simple enough to allow parallel investigation in humans and monkeys, and is also easily amenable to computational modeling. The paper makes a compelling argument for the importance of this type of parallel investigation and the suitability of the CST for doing so.

Behavior in monkeys and in human subjects suggests that behavior seems to include two qualitatively different kinds of behavior - in some cases, the cursor oscillates about the center of the screen, and in other cases, it drifts more slowly in one direction. The authors argue that these two behavioral regimes can be reliably induced by instructing human participants to either maintain the cursor in the center of the screen (position control objective), or keep the cursor still anywhere in the screen (velocity control objective) - as opposed to the usual 'instruction' to just not let the cursor leave the screen. A computational model based on optimal feedback control can reproduce the different behaviors under these two instructions.

Overall, this is a creative study that leverages experiments in humans and computational modeling to gain insight into the nature of individual differences in behavior across monkeys (and people). The authors convincingly demonstrate that they can infer the control objectives from participants who were instructed how to perform the task to emphasize either position or velocity control, based on the RMS cursor position and RMS cursor velocity. The authors show that, while other behavioral metrics do contain similar information about the control objective, RMS position and velocity are sufficient, and their approach classifies control objectives for simulated data with high accuracy (~95%).

The authors also convincingly show that the range of behaviors observed in the CST task cannot be explained as emerging from variations in effort cost, motor execution noise, or sensorimotor delays.

One significant issue, however relates to framing the range of possible control objectives as a simple dichotomy between 'position' and 'velocity' objectives. The authors do clearly state that this is a deliberate choice made in order to simplify their first attempts at solving this challenging problem. However, I do think that the paper at times gives a false impression that this dichotomous view of the control objectives was something that emerged from the data, rather than resulting from a choice to simplify the modeling/inference problem. For instance, line 115: "An optimal control model was used to simulate different control objectives, through which we identified two different control objectives in the experimental data of humans and monkeys."

In the no-instruction condition - which is the starting point and which the ultimate goal of the paper is to understand - there is a lot of variability in behavior across trials (even within an individual) and generally no clear correspondence to either the position or velocity objective. This variability is largely interpreted as the monkeys (and people) switching between control objectives on a trial-to-trial basis. If the behavior were truly a bimodal mixture of these two different behaviors, this might be a convincing interpretation. However, there are a lot of trials that fall in-between the patterns of behavior expected under the position and velocity control objectives. The authors do mention this issue in the discussion. However, it's not clearly examined whether these are simply fringe trials that are ambiguous (like some trials generated by the model are), or whether they reflect a substantial proportion of trials that require some other explanation (whether that is blended position/velocity control, or something else). The existence of these 'in-between' trials (which possibly amount to more than a third of all trials) makes the switching hypothesis a lot less plausible.

Overall, while I think the paper introduces a promising approach and overall helps to improve our understanding of the behavior in this task, I'm not fully convinced that the core issue of explaining the variability in behavior in the no-instruction condition (in monkeys especially) has been resolved. The main explanation put forward is that the monkeys are switching between control objectives on a trial-by-trial basis, but there is no real evidence in the data for this, and I don't think there is yet a good explanation of what is occurring in the 'in-between' trials that aren't explained well by velocity or position objectives.
