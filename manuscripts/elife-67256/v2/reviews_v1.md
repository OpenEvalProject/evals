# Peer review - Round 1

Editors:
- Jesse H Goldberg, Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67256.sa0](https://doi.org/10.7554/eLife.67256.sa0)

Motor cortical population activity during reaching exhibits rotational dynamics thought to arise from recurrent connections in cortical circuits. This innovative paper performs an important 'experiment' not currently possible in real biological networks: examine activity and task function before and after deletion of recurrent connections. Surprisingly, trained networks produced rotational dynamics even without internal recurrence, raising the possibility that sensory feedback is a key determinant of motor cortical dynamics. More broadly, this paper leverages the experimental tractability of artificial neural networks to test what conditions and architectures are necessary to produce brain-like signals.


---

# Peer review - Round 1

Editors:
- Jesse H Goldberg, Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67256.sa1](https://doi.org/10.7554/eLife.67256.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Rotational dynamics in motor cortex are consistent with a feedback controller" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Ivry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The NO-REC Network

The point about non-recurrent (NO-REC) networks being able to produce rotational dynamics is critical in showing the key role of feedback in generation of those dynamics. Yet all three reviewers exhibited confusion and concern over exactly how the NO-REC was implemented.

In the Methods, the authors explain how they model a non-recurrent network as follows: "We also examined networks where we removed the recurrent connections from each layer by effectively setting Whh, Woo to zero for the entire simulation and optimization (NO-REC networks)". However, if this is the only modification, it still leaves recurrent elements in the network. For example, if we set Whh to zero, equation 2 will be: ht+1 = (1-a) * ht + a * tanh(Wsh * st + bh) where a is a constant scalar (seems to be equal to 0.5). This is indeed still a recurrent neural network since ht+1 depends on ht. If their explanation in the Methods is accurate, then the current approach restricts the recurrent dynamics to be a specific linear dynamic (i.e. "ht+1 = (1-a) * ht + …") but does not fully remove them. The second layer is also similar (equation 3) and will still have recurrent linear dynamics even if Woo is set to 0. To be able to describe networks as non-recurrent, the first terms in equations 2 and 3 (that is (1-a)*ht and (1-a)*ot) should also be set to 0. This is critical as an important argument in the paper is that non-recurrent networks can also produce rotational dynamics, so the networks supporting that argument must be fully non-recurrent, or the argument should be clarified and restricted to what was actually shown. Perhaps the authors have already done this but just didn't explain it in the Methods, in which case they should clarify the Methods. However, if the current Method description is accurate, they should rerun their NO-REC simulations by also setting the fixed linear recurrent components (that is (1-a)*ht and (1-a)*ot) to zero as explained above to have a truly non-recurrent model.

2) Role of Sensory Feedback

A better discussion and handling of the distinction between recurrent feedback within M1 and recurrent feedback that traverses the whole system is necessary. All reviewers had issues with this, and all reviewers asked for some manipulation of the sensory feedback in the model to shore up the claim of its importance in driving rotations.

2.1 Reviewer 1 recommended deleting the feedback: To fully demonstrate the role of feedback, additional simulations are also needed where the sensory feedback is removed from the brain model. In other words, what would happen if recurrent and non-recurrent brain models are trained to perform the tasks but are not provided with the sensory feedback (only receive task goals)? One would expect the recurrent model to still be able to perform the task and autonomously produce similar rotational dynamics (as has been shown in prior work), but the non-recurrent model to fail in doing the task well and in showing rotational dynamics. I think adding such simulations without the feedback signals would really strengthen the paper and help its message.

2.2 Reviewer 2 additionally suggested tweaking the delays: asking what effect does the feedback delay have on the jPCA frequencies, and to test if increasing the delay leads to slower frequencies and decreasing the delay leads to faster frequencies.

2.3 Reviewer 3 asked if the sensory inputs were the positions and velocities of the two joints in Cartesian coordinates, would we observe similar rotational dynamics?

Full deletion of feedback (2.1) would probably make for the strongest response to this big point, and may also make testable predictions for cortical activity following de-afferentation. Yet we leave it at the author's discretion to choose which of these points to directly take on to bolster the investigation of how feedback affects the system – provided a clear argument in the response to reviewers is provided for why you chose to do what you did.

3. Network Performance Quality

A measure of how well each trained network is able to perform the task should be provided. For example, is the non-recurrent network able to perform the tasks as accurately as the recurrent models? The authors could use an appropriate measure, for example average displacement in the posture task and time-to-target in the center-out task, to objectively quantify task performance for each network. Another performance measure could be the first term of the loss in equation 5. Also, plots of example trials that show the task performance should be provided for the non-recurrent networks (for example by adding to Figure 8), similar to how they are shown for the recurrent models in Figures 2 and 6.

4. Role of Task Structure

An important observation is that rotational dynamics also exist in the sensory signals about the limb state. This may imply that the task structure that dictates the limb state and thus the associated sensory feedback may play an important role in the rotations without the recurrent connections. While the present study will be a valuable addition regardless of what the answer is, What is the role of the task structure in producing rotational dynamics? In both the posture task and the center-out task, the task instruction instructs subjects to return to the initial movement 'state' by the end of the trial: in the posture task the simulated arm needs to return to the original posture upon disturbance, and in the center out task the arm needs to start from zero velocity and settle at the target with zero velocity. Is this structure what's causing the rotational dynamics? This is an important question both for this paper and for the field and the authors have a great simulation setup to explore it. For example, what happens if the task instructions u* instruct the arm to follow a random trajectory continuously, instead of stopping at some targets? With a simulated tracking task like this, one could eliminate obvious cases of return-to-original-state from the task. Would the network still produce rotational dynamics? We do not expect the authors to collect experimental monkey data for such new tasks, rather to just change the task instructions in their numerical simulations to explore the dependence of observed rotational dynamics on the task structure. this will help the message of the paper and can be very useful for the field. If the authors choose not to address this point, there should be at least clear text in the discussion allowing for the possibility that their results might not generalize to other tasks, even though such a caveat might weaken the paper's argument.

Reviewer #2 (Recommendations for the authors):

I feel the study overloads the differences between recurrence and feedback. I am sure the authors do not mean to say that there is no recurrent processing in motor cortex! For instance, in the abstract the authors say:

Recent studies hypothesize that motor cortical (MC) dynamics are generated largely through its recurrent connections based on observations that MC activity exhibits rotational structure.

I think this claim is an overinterpretation of the Churchland 2012 and Sussillo 2015 articles from the Shenoy lab. The point is actually that when you apply jPCA to MC data, a surprising amount of it is rotational structure and one source of it can be local recurrence and that a lot of it can be described by autonomous dynamics. This past output could come through short low latency pathways within motor cortex. As these authors and Sussillo et al. 2015 argue, longer time constant pathways that involve the limb, and the joint muscles could be the cause of these rotations. Together, they all collaborate and result in the rotational structure in these brain areas.

I recognize the authors removed recurrent connections from the RNN and then show that a model without recurrence can replicate the rotational structure. I think this is somewhat imprecise because there is pseudo recurrence in the system except not in the traditional local synaptic sense but through a filtered version that comes through feedback from the output. In my mind what the authors have built is a sophisticated two-step albeit nonlinear autoregressive process which will show slow oscillations. To verify my idea, I developed a simple AR process simulation in MATLAB and observed that you can get oscillatory structure in the output even with an AR(2) and AR(4) process. The time scale of dt is ~10 ms and the time constant is 20 ms, and finally the feedback delay is ~50 ms which means this is essentially an AR(5) process which should lead to slow time scale changes in the network activity (please see attached code which simulates a 4th order AR process).

Let me try to make the point clearer. I feel the authors could really contribute by saying rotational structure in dynamical systems comes comes from past output affecting future output. In simple LDSes

dx/dt = Ax + U.

If A has complex eigen values, then you get rotational structure.

Now assume A = 0. Now somehow, if U contains a component which is some nonlinear form of x. Then you basically have a new equation which is

dx/dt = Af(x) + U'.

Now you have basically created another LDS which depends on the previous state. If A has complex eigen values you essentially have rotations again.

Related, what effect does the feedback delay have on the jPCA frequencies? It would be interesting to understand if increasing the delay leads to slower frequencies, and decreasing the delay leads to faster frequencies. This would further bolster the manuscript.

I think the discussion is very muddled and generic and is not as compelling as one would like it to be. In my mind, it seems weird to say recurrence has no role and also to think of MC as some sort of independent system divorced from the rest of the brain and the world. The way I formulate it is that the activity at the next time step in these motor related areas is a combination of local recurrent contribution, input from another cortical area, and feedback from the external world, which in itself is from another cortical area. All of these ultimately contribute to the rotational structure observed in motor cortex. This is the challenge for the field to understand all the constituent components. At best, this paper shows that just observing rotations means that any or all three of these components could be the cause. A better synthesis of their findings would improve the impact.

Reviewer #3 (Recommendations for the authors):

This work could be further strengthened with additional analyses of the trained RNNs that elucidate the conditions under which sensory inputs induce rotational dynamics in the MC.

1. The authors suggest that sensory inputs are likely the source of the rotational dynamics observed in the trained RNNs.

However, this is only weakly substantiated by linear fits of the activity in the top 2 jPCA planes to the sensory inputs.

Would any sensory inputs that are themselves rotational induce such phenomenon?

For example, if the sensory inputs were the positions and velocities of the two joints in Cartesian coordinates, would we observe similar rotational dynamics?

What if the feedback signals were not rotational at all (e.g., if we only provide the muscle activity as feedback signals)?

2. How does rotational dynamics in the trained RNNs depend on the length of the sensory delay? For example, would we expect a comparable delay to the onset of rotation dynamics in the RNN?

3. The authors showed that trained feedforward networks also exhibited rotational dynamics. Do trained recurrent connections converge to this solution? More generally, how strong is the internal activity of the trained RNNs as measured by for example the norm of the recurrent weights? Do the internal dynamics of the RNNs need to be weak for sensory inputs to induce rotational dynamics in the RNNs?

4. The authors seem to take for granted (perhaps rightfully so) that continuous feedback signals are necessary for performing the posture perturbation task. While this makes sense intuitively, it would help convince the readers to see evidence of this fact. More specifically, I assume RNNs trained with continuous feedback signals are likely able to generalize to perturbations that are not in the training set. On the other hand, RNNs trained without continuous feedback signals (but provided with the initial perturbed state of the arm) would not be able to generalize to novel perturbations.

5. The trained RNNs include an input layer and an output layer. Is this necessary? Would a single layer suffice?
