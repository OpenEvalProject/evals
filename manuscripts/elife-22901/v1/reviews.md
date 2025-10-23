# Peer review - Round 1

Editors:
- Peter Latham, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22901.026](https://doi.org/10.7554/eLife.22901.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Deep learning with segregated dendrites" for consideration by eLife. Your article has been evaluated by a Senior Editor and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation among the reviewers. Based on these discussions, which are summarized below together with the individual reviews, we regret to inform you that your work will not be considered further for publication in eLife.

Reviewing Editor's summary:

This was a tough one: reviewers 2 and 3 were very positive, and even reviewer 1, who was negative about the clarity of the paper, was very positive about its content and importance. The problem was the writing: the reviewers felt that in its present form, the paper would be understandable only by deep learning experts. I'm sure it would be possible to fix this, but the reviewers also felt that this would be a major undertaking, and might even take a couple of rounds. It is eLife's policy to reject papers in that situation.

I'm very sorry; I would love to see work like this in eLife. Unfortunately, I'm not sure how useful the reviews will be – the most negative reviewer was #1, but there were only a small number of concrete suggestions, mainly because s/he was very lost. Perhaps it would be helpful to find a theoretical neuroscientist who is not an expert in deep networks – presumably your target audience – and see where s/he has trouble understanding the paper.

Reviewer #1:

This paper touches on a very important topic: biologically plausible deep learning. However, this particular version is not suitable for eLife. In fact, it's not clear it's suitable at all: after several hours staring at the paper, I remained thoroughly confused. Please don't get me wrong; I'm guessing the paper is correct; I think the problem is mainly the exposition relative to my level of knowledge.

A few examples:

1) It was never clear from the notation (and often the text) whether they were referring to scalars, vectors or matrices – something that does not help when one is trying to make sense of the math.

2) Above Equation (1) the authors talk about target firing rates. But, except for the output units, it's not clear at all what those are.

3) In Equation (1), I don't know what the target burst, α^t, is. I thought the apical dendrite (presumably what α is referring to) is cut off in the target phase.

4) Why should Equation (1) be the target rate?

5) L^0 is actually |α^t-α^f|^2. Why not say so?

At this point I turned to Materials and methods, in the hopes that the equations would clarify things. They didn't.

6) Equations (5)-(8) are standard, but are written in a very complicated a form. There may be a reason for that, but it's confusing for your run of the mill computational neuroscientist.

7) As far as I could tell, neither Equations (7) nor (8) include the feedback from the apical dendrite. And I couldn't figure out from anywhere in Materials and methods how that was implemented.

8) Equation (17) seems inconsistent with Equations (19) and (20).

And at that point I gave up.…

Reviewer #2:

This paper takes on the valiant task of making artificial deep neural networks more biologically relevant by implementing multi-compartmental neurons. In particular, the segregation of feed-forward from feedback information processing streams within the single cell is a welcome addition for biologists to see in computational models. The authors use details about the anatomical and physiological properties of cortical pyramidal neurons to implement backprop training. They establish that these biologically-inspired features can be accommodated without significant loss of performance. We believe this paper would be a welcome early step in the direction of bringing deep artificial network and neurophysiology thinking together, but requires conceptual explanation in a few key areas, especially for biologists not familiar with the details of deep networks.

What is the conceptual reason that feedforward and feedback streams need to be separated? Is it because the error signal is computed as the difference between the forward phase and the "correct" answer imposed by the teaching signal on the output neurons in the target phase? Conceptually, it seems that the separation of the signals allows for an error to be computed, and therefore for the appropriate change in weights to be arrived at. This is in contrast to how some often think about the relationship between feedforward and feedback in the brain where the main function of the feedforward/feedback integration is to actively and directly create downstream activity (as opposed to here where it is to change the weights of synapses).

What is the purpose of the random sampling of bursts? Why not just a fixed time? Would asynchronous bursting still be effective? Is the synchronous nature of the bursting in order to coordinate with the feedback from the teaching signal?

Would all of this be mathematically equivalent to a separate set of neurons that deal primarily with teaching signals in feedback pathways, and whose interaction with the "normal" feedforward network be regulated through some disinhibitory mechanism? To say this another way, is there anything special about the single cells and the nonlinearity α used, or could a similar setup be created by separating the different compartments into single neurons and connecting them with normal synapses?

What is the explanation for why weak apical attenuation disrupts learning? Is it because it forces an underestimation of the error by having the difference in activity between forward and target phases become eroded?

Local here means local in space. However, in order to compute weight updates, differences in activity still need to be taken over time. More specifically, the activity in the bursts between forward and target phases (equation 2). What is the biologically plausible mechanism for such non-temporally aligned computation?

Is there any explanation for why sparse feedback weights improve the network?

In general it would useful to have conceptual explanations for many of the issues discussed above.

Reviewer #3:

I think this is a very valuable manuscript that makes a link between deep learning and a possible biological implementation. As this link is of high scientific relevance topic and of broad interest, I consider the manuscript suited for a good journal as eLife, even if there is still a large gap between the performance of deep learning for artificial neuronal network and the suggest biological implementation (that only considers 2 layers with relatively humble performance). But the authors well recognize this and the manuscript represents a first step towards future research in this important field.

There is one main issue that should be addressed more thoroughly.

1) The proof of Theorem 1 assumes that the matrix product (J_β) (J_γ) is close to the identity mapping in the readout space. In the cited work by Lee et al. (Difference Propagation, 2015) this is the case because the forward and backward weights are adapted such that they get aligned. In the present case the alignment only becomes indirectly apparent by simulations showing that the error vector in the hidden layer eventually falls within 90 degrees of the true backpropagation error.

As I understand, the top-down weight matrix Y is fixed (e.g. randomly chosen). From a theoretical perspective, one may choose Y to be the pseudo-inverse of the forward weight matrix W^1. In fact, in that case a much simpler proof for Theorem 1 exists (a few lines only). But if Y is random, then the whole idea boils down to the random feedback idea (Lillicrap et al., Nature communication 2016) and this link should be emphasized more. While in the Supplementary Information of that paper a proof is outlined for linear transfer functions, it remains unclear how for nonlinear transfer functions this alignment is achieved obtained.

If J is chosen to be the transposed of W^1 as it is the case in backprop (and in part of the simulations), then nothing has to be proven. But if Y is random, then the big issue is to prove that the mapping γ(y) is approximatively an inversion of the mapping β(x). If this were proven, Theorem 1 in the manuscript could be cited as Theorem 2 in Lee et al. (Diff prop, 2015). But in the current form, Theorem 1 replicates the idea of Lee et al. (as it is also stated by the authors) without proving the basic assumption shown to be true in the case of Lee et al.. Of course, for the reader's convenience the proof of the Diff-Prop Theorem can still be reproduced.

In my view the core idea for the theory in the paper is (1) with random top-down connections the forward weights align as shown by Lillicrap et al. (2) Given the alignment, the idea of difference propagation with the proof given in Lee et al. can be applied. Once this theoretical fundament is introduced in this form (and simply referred to these papers), the idea of using segregated dendrites to implement the random feedback idea can be stressed.

A bit less fundamental, but still more than minor:

2) In view of the rather deep mathematical issues related to the feedback alignment, I would suggest to defer Lemma 1 to some Supplementary Information. The approximation of PSP signaling by instantaneous Poisson rates when the rate is small as compared to the PSP duration is standard in theoretical neuroscience. But the 3-page proof is still nicely done and may be helpful for a non-specialist who wishes to go into the details.

3) At the end of the subsection “A network architecture with segregated dendritic compartments” (Results) some critical issues are raised about the biological plausibility. In this context it should also be stressed that the alternation between two phases, each of which again subdivided into two further phases (Figure 1C), is not so easy to match to the biology. The phases need a memory that is tagged with the phase information and plasticity that is only turned on in a specific phase, checking out the memory from a previous phase.

Beside mentioning this in the Results, it should also be taken up in a further paragraph in the Discussion. One should mention that synaptic eligibility traces could help out here and that this helps to bridge information across the phases. Moreover, the phases could be implemented by exploiting global (I guess γ) oscillations that are shown to be present in various cognitive states. Discussing the link of learning and γ oscillations may be of general interest in this context.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Towards deep learning with segregated dendrites" for further consideration at eLife. Your article has been favorably evaluated by Andrew King (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

This paper is much improved. However, it still has a way to go before it's ready for a neuroscience audience. Given that this has been reviewed several times now and remains in an unacceptable form, we are prepared to offer only one more opportunity to provide an acceptable version of the manuscript.

The easy thing to fix is notation and writing: we believe that, even in its improved form, it would be very hard for a neuroscientist, even a computational one who is used to thinking about circuits, to read, and the main ideas would be difficult to extract. More on that below.

The potentially harder thing to fix is biological plausibility. If we understand things correctly, the neuron must estimate the average PSPs during the feedforward sweep of activity, when only the input is active, estimate them again during the training phase, when the correct output is active as well, and then subtract the two. These signals are separated in time, which means the synapses have to store one signal, wait a few tens of ms, store another, and take the difference. In addition, the difference is computed in the apical dendrite, but it must be transferred to the proximal dendrites. And finally, a global signal is required to tell a synapse in which phase it is so that the estimate can be endowed with the correct sign. All seem nontrivial for neurons and synapses to compute.

Lack of biological plausibility should not rule out a theory – synapses and neurons are, after all, complicated. However, two things are needed. First, you need to provide a mechanism for implementing the learning rule that's not inconsistent with what's known about neurons and synapses. Second, you need to provide suggest experiments to test these predictions. Of these, the first is probably harder.

Now for the exposition. It may seem like we're micromanaging (and we are), but if this paper is to have an impact on the neuroscience community – a prerequisite for publication in eLife – it has to be cast into familiar notation.

1) The model was much simpler, and more standard, than first impressions would imply. It can be written in the very familiar form

dV^m_i/dt = -g_L V^m_i

+ sum_n g_n (b^n_i + sum_j W^mn_ij s^n_j(t) – V^m_i)

+ g^m_iE(t) (E_E – V_i^m) + g^m_iI(t) (E_I – V_i^m)

where the s^n_j(t) are filtered spike trains,

s^n_j(t) = sum_k kappa(t-t^n_jk),

t^n_jk is the k^th spike on neuron j of type n, and spikes were generated via a Poisson process based on the voltage. (Please note: errors are possible, but the equations look something like what we wrote.)

In this form it is immediately clear to a neuroscientist what kind of network this is. If nothing else, that will save a huge amount of time for the reader – it took hours of going back and forth over the equations in the paper before it became clear that the model was very standard, something that most readers would not have the patience for.

In addition, as written above, it makes it clear exactly how the dendrites are implemented: by varying the g_n. In real dendrites they vary with voltage on the dendrite; in this model they simply vary with time.

And finally, the notation with the A's and B's used in the paper is not helpful to neuroscientists, who are very used to seeing V, or maybe U, for voltage.

2) Along the same lines, a better figure showing the circuit needs to be included. The circuit with multiple hidden layers needs a similar drawing, as we were not able to figure out exactly what it looked like. (We're guessing there was sufficient information in the paper, but the amount of work it would take to extract it seemed high.)

3) The cost function, L^1, seemed somewhat arbitrary. According to Equation 7,

L^1 \propto \sum_i (<σ(U_i)>^t – σ(<U_i>^f))^2

where the angle brackets represent a time average and the superscripts t and f refer to the target and feedforward phases, respectively (basically, the overline was replaced with angle brackets, mainly because we're using plain text). Why was the average taken outside the sigmoid in the target phase and inside the sigmoid in the feedforward phase?

4) A similar question applies to L^0, which is written

L^0 = sum_i (λ_max(<σ(C_i)>^f – σ(<C_i>^f) + α_i^t – α_i^f)^2

As far as we can tell, the first two terms are included to make the update rules work out, and they are eventually set equal to each other. But is there any reason to think that L^0 should be minimized? It seemed unmotivated.

5) In Equations 19 and 22, why are there no terms involving the derivatives of the sigmoid in the target phase?
