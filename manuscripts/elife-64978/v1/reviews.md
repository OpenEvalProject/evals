# Peer review - Round 1

Editors:
- Valentin Wyart, https://ror.org/013cjyk83 École normale supérieure, PSL University, INSERM France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64978.sa0](https://doi.org/10.7554/eLife.64978.sa0)

This manuscript provides a fresh view on the fundamental trade-off between the speed and accuracy of perceptual decision-making. Using computational modeling, the authors establish the important finding that adopting a momentary suboptimal trade-off for maximizing reward rate at the beginning of learning can yield better decisions and larger rewards at later stages. This novel prediction is tested in rodent experiments. The experiments and their detailed analysis provide compelling evidence for the authors' theoretical predictions.


---

# Peer review - Round 1

Editors:
- Valentin Wyart, https://ror.org/013cjyk83 École normale supérieure, PSL University, INSERM France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64978.sa1](https://doi.org/10.7554/eLife.64978.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Strategically managing learning during perceptual decision making" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Valentin Wyart as the Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Konstantinos Tsetsos (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Classical descriptions of the speed-accuracy trade-off during perceptual decision-making assume that agents balance decision speed and accuracy given a fixed level of perceptual sensitivity. These descriptions ignore how agents learn to process the incoming sensory information for the purpose of decision-making. This manuscript develops a theory for how this perceptual learning ought to occur, and tests predictions from the theory using rodent experiments. This theory of perceptual learning leads to a new way of understanding suboptimal slow decisions at the early stages of learning. The manuscript is theoretically and technically sound. Additionally, the experiments are ingeniously designed and rigorously analysed, and their results provide empirical support for the theory proposed by the authors. There are however additional analyses that should be performed to validate the authors' specific claims regarding the strategic adaptation of perceptual sensitivity throughout task execution. Furthermore, the manuscript could be improved for clarity.

A current weakness of the manuscript concerns the preference for a strategic adaptation of perceptual sensitivity throughout learning (iRR-sensitive policy) over a simpler gradual increase in perceptual sensitivity (constant-threshold policy). Indeed, the strategies provide qualitatively similar predictions (see, e.g., Figure 3). Validating the iRR-sensitive policy over the constant-threshold policy is critical to the overall conclusions of the work (namely, that rats are strategically adapting their decision times to promote learning). However, it is currently unclear how the constant-threshold policy (in which rats do not control the speed of their decision but benefit from a gradual improvement in perceptual sensitivity) has been conclusively ruled out.

To rule out the constant-threshold policy, the authors argue first that drift-diffusion model (DDM) fits to the data show both drift rate and decision boundary changes throughout learning (Figure S5). However, it is not clear that a concurrent change in drift rate and decision boundary is the most parsimonious explanation of the data. The authors should establish that indeed both parameters change via comparing different versions of the DDM where a subset of the parameters are allowed to vary while others remain fixed throughout learning. Additionally, it would be interesting to know whether the conclusions remain the same when a more 'complete' version of the DDM is used (including drift-rate variability as a free parameter).

The second argument in support of the iRR-sensitive policy comes from experiment 2, in which the authors convincingly show that the improvement in perceptual sensitivity (or SNR) scales with decision times. It is indeed important to show that longer viewing leads to larger SNR improvements. However, it is currently unclear how this observation rules out the constant-threshold policy. Unless additional analyses are performed to show that the constant-threshold policy does not make this prediction, this observation appears necessary but not sufficient to validate the iRR-sensitive policy.

The third argument in support of the iRR-sensitive policy comes from experiment 3, in which a first group of rats performed a 'learnable' perceptual experiment while a second group performed an experiment with 'unlearnable' (transparent) stimuli. Indeed, this second group showed a reduction in reaction times as the experiment progressed, which (a) is reward-rate optimal, and (b) can be understood as a strategic change of decision boundary, since the SNR in this experiment is theoretically zero. However, it is unclear how rodents behave in this 'unlearnable' context. Presumably, during the first two sessions, the rats may be trying to figure out what the task is (e.g., waiting to see if there are visible stimuli in a subset of trials). In the third session, the rats speed up but it is not clear if they keep speeding up later in the experiment. Are reaction times significantly decreasing beyond the third session? Finally, it is not obvious that the effective SNR in this experiment is zero. In this 'unlearnable' experiment, rats may use some non-sensory information (e.g., choice history information such as their preceding response and whether they got rewarded) as input to their drift rate.

Another weakness comes from the use of recurrent neural networks (RNNs) to model that accumulation of decision-relevant evidence. Indeed, these networks are tuned such that they become equivalent to DDMs. Framed in this way, the connection between RNNs and DDMs appears somewhat trivial, such that the introduction of RNNs does not add anything to the manuscript, and might even be confusing to some readers. The authors should either reframe the specific role of RNNs for supporting their key findings, or possibly remove them if they do not provide unique insights beyond classical drift-diffusion modeling.

The detailed description of the models is currently hidden in the Methods section, even though it is essential for understanding their learning dynamics. In particular, the authors assume two sources of noise in the model: one on the input, and one on the accumulator. Learning is achieved by re-scaling the input by an 'input weight'. Increasing the input weight boosts the input signal compared to the accumulation noise, such that the latter can be effectively suppressed by making the input weight large enough. By contrast, the input noise cannot be suppressed by such re-scaling, such that it is this noise that ultimately limits asymptotic performance, and determines the asymptotic SNR. This important constraint is currently not clear after reading the manuscript. The authors should reframe the manuscript to highlight and discuss the model variables that affect the SNR, including the input weight. This would clarify what the authors mean by 'learning' in their theory. The authors initialize the model with a low input weight to reflect that the agent has not yet learned how to interpret the sensory information for the purpose of decision-making. Thus, the input weight is not something that would have a direct mechanistic implementation in the brain. Instead, it is an abstract quantity that describes how well a decision-maker can turn sensory information into a perceptual decision. Once this interpretation of input weight is stated clearly in the manuscript (which it is not in the current version), starting the task with a low input weight makes sense.

Finally, a few choices made by the authors are critical for their findings, but are not sufficiently described in the main text. First, the observed reaction time (RT) is composed of a non-decision time (T0) and a decision time (DT). Experiments allow to measure RT, but the theory makes predictions about DT, which requires inferring T0. The magnitude of T0 impacts the results, but how it is inferred is currently buried in the Methods section. Second, the rodents sometimes choose to not immediately initiate a new trial (the "voluntary inter-trial interval"). The authors assume that rodents ignore this interval when maximizing reward rate, and find near-optimal reward rates under this assumption. Importantly, including this voluntary inter-trial interval makes reward rates drop significantly. However, these details are again buried in the Methods section, and are not mentioned nor discussed in the main text.

– The main conclusions hinge upon concurrent changes in both drift rate and decision boundary throughout learning. This change is assessed via fitting HDDM models. It is important that the authors fit and compare the following 3 DDM variants: (a) drift rate changes throughout learning but decision boundary remains fixed, (b) decision boundary changes throughout learning but drift rate remains fixed, (c) both drift rate and decision boundary change throughout learning.

– The HDDM fitting procedure is not fully described. In particular, it is not clear what parameters, asides the drift rate, the decision boundary and the non-decision time, varied. For instance, was the drift rate variability a free parameter? It is important to report more precisely the details of the model fits and, if simple variants of the DDM were used, to fit the data using more complex DDMs that include drift rate variability as a free parameter. Additionally, please report in Figure S5 all parameter estimates during learning and not just the drift rate and the decision boundary. Details around Equation (40) should also be in the main text. Furthermore, except for the internal noise, the setup looks very similar to that of Drugowitsch et al. (2019), and the relationship should be discussed somewhere in the main text.

– Currently the evolution of the mean RT during learning is examined. Plotting the change in the RT distribution (averaged/vincentised across participants) can be more informative about changes in the strategy being used than plotting the mean RT alone.

– The results of experiment 3 are interesting, but at the same time the behaviour in the transparent group requires more scrutiny. How do rats behave in this condition? It appears that random choice in combination with heuristic strategies (e.g. win-stay lose-switch) are viable possibilities. The argument that the SNR is intrinsically zero in this task. However, the signal in this experiment may contain non-zero, irrelevant information (such as choice history or feedback information). Plotting the RT distributions as a function of learning could provide insight in this regard, because boundary changes and SNR changes manifest differently in the shapes of RT distributions.

– The use of RNNs is not sufficiently supported beyond classical drift-diffusion modeling. The authors should either reframe the specific role of RNNs for supporting their key findings, or possibly remove them if they do not provide unique insights beyond classical drift-diffusion modeling.

– The authors should clarify early on in the manuscript what "learning" means in their model and theory, and why it makes sense to start with a low input weight (after describing the meaning of the input weight). The authors should also explain what T0 and D_RSI are, how they are determined (and the choices made to determine them), and how these parameters impact the results (also related to Figure S13). In particular the relationship between RT and DT is already required to understand Figure 1c, and many plots thereafter.

– Box 1 provides some details of the model, but leaves out others – e.g., the different sources of noise in the model. From Box 1 alone, it is unclear how the asymptotic SNR or the iRR-sensitive threshold are computed. It is indeed nice that it is possible to derive Equation (3), but the equation itself is not particularly informative for the exposition of the main findings, and so it could be moved to the Methods section.
