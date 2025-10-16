# Peer review - Round 1

Editors:
- Peter Latham, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.28295.022](https://doi.org/10.7554/eLife.28295.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Predicting non-linear dynamics by stable local learning in a recurrent spiking neural network" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors and the evaluation has been overseen by Timothy Behrens as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper proposes a learning scheme that allows a recurrent network of spiking neurons to predict the dynamics of a non-linear system by training feedforward and recurrent connections. The learning is achieved using a local learning rule. The error signal is fed back by fixed, random connections, with the feedback loop forming an auto-encoder. After learning, which is done via motor "babbling," the network is able to reproduce the output in an open-loop setting without feedback. The authors showcase their training algorithm in a number of linear and non-linear applications, including the dynamics of a two-link arm. In addition, the authors prove analytically under mild assumptions that learning converges if the non-linear dynamics can be realized by the network. The paper is mainly clearly written, and has the potential to be of significant interest to the community.

Essential revisions:

1) The firing rates are far higher than is biologically plausible. It is important that this is fixable, at least in principle. If not, then the scheme has nothing to do with the brain. We hesitate to ask for additional simulations, but we think you need to show that the network can work when firing rates are in a more biologically plausible range, as in less than about 20 Hz on average (still high, but closer to reality).

2) We did not follow a key step. The sixth equation in subsection “Network architecture and parameters” says:

sum_{beta, i} e_{j,beta} d_{beta,i} a_i(sum_alpha e_{i,alpha} epsilon_alpha)

\approx sum_alpha e_{j,alpha} epsilon_alpha

It seems that you effectively rewrote this as

sum_{beta, i} e_{j,beta} d_{beta,i} a_i(I_i) \approx I_i

(see Eq. (13)). Strictly speaking, this holds only if the current (whose ith component is I_i) lies in the low dimensional submanifold spanned by the e_{i,alpha}. However, because of the recurrent dynamic, the network is likely be chaotic, and so the current is likely to live on a high-dimensional manifold.

This seems to indicate a problem with the derivation. Or are we missing something? In any case, this needs to be explained much more clearly.

3) It would be good to have a clear, succinct description of what new feature allowed you to train spiking networks with a local, biologically realistic learning rule, something that others have failed to do. Perhaps it's the auto-encoder? (See next comment.)

4) The auto-encoder is critical for the operation of the network. Can you provide any intuition about why it's there, and what it does? This may not be possible, but it would greatly strengthen the manuscript if you could do it.

5) A potentially important limitation of this paper is that it does not take into account feedback delays during training. This would be a significant limitation if the purpose of this work is to propose how forward models can be learned in the brain: one of the main reasons to have forward models in the first place is being able to deal with feedback delays (see e.g. Wolpert, Ghahramani & Jordan, 1995). Learning that ignores feedback delays is therefore not fully biologically realistic. If this limitation is indeed correct, it needs to be mentioned more prominently in the Discussion section (we only found it buried in the Methods section); if the network can in fact handle feedback delays during training (that are on a similar scale as the target dynamics), it should be demonstrated, as it would make the impact of the paper significantly stronger.

6) An alternative approach to training recurrent networks is to initialize the recurrent weights in some appropriate way and to just train the readout weights during learning (reservoir computing). How much more computationally powerful is the proposed method? A simple way to test this would be to compare the performance of the trained network to that of a network where the recurrent weights have been shuffled after training, the feedback weights set to zero, and the output weights retrained by linear regression. If such a network had comparable computational performance, it would suggest that only the correct recurrent weight distribution is required to learn the task.

7) Does learning still work if the dynamical system has small amounts of stochasticity, or if the error signal is noisy?

8) It's critical to have experimental predictions. Or at least a summary of the implications of this work for what's going on in the brain.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your revised article "Predicting non-linear dynamics by stable local learning in a recurrent spiking neural network" for consideration by eLife. The evaluation has been overseen by a Peter Latham as the Reviewing Editor and Timothy Behrens as the Senior Editor.

I want to congratulate you on a very nice paper, and thank you for your very thorough responses; you addressed almost all the points. The only problem is that in parts the manuscript is still not very clear (at least not to me). Please take a very hard look at the Methods section "Network architecture and parameters", and make sure it's crystal clear.
