# Peer review - Round 1

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37124.016](https://doi.org/10.7554/eLife.37124.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Learning recurrent dynamics in spiking networks" for consideration by eLife. Your article has been reviewed by Timothy Behrens as the Senior Editor and two reviewers, one of whom is the Reviewing Editor. One of the reviewers, Brian DePasquale, has agreed to reveal his identity.

The Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The focus of most (maybe all?) research on RNNs has been on output: how do you train recurrent networks to produce a low dimensional (compared to the dimensionality of the network) target function? This paper asks a different question: how do you train recurrent networks so that neurons within the network produce their own target function? Here the target can be either firing rate or synaptic drive. What's interesting about this paper is that the authors give the conditions under which training is possible. These rules provide insight into the limits of performance of spiking RNNs, something that has, I believe, been lacking in the field.

Essential revisions:

Reviewers A and B's full reviews, along with the subsequent discussion are included below. You should focus on making A happy (which is pretty easy, since he/she had only minor comments). However, when you revise the paper, you probably should keep B's review in mind – his/her interpretation of your paper may be shared by others.

Reviewer A comments:

The focus of most (maybe all?) research on RNNs has been on output: how do you train recurrent networks to produce a low dimensional (compared to the dimensionality of the network) target function? This paper asks a different question: how do you train recurrent networks so that neurons within the network produce their own target function? Here the target can be either firing rate or synaptic drive.

What's interesting about this paper is that the authors give the conditions under which training is possible:

- The target functions have to be sufficiently diverse..

- A sufficiently large number of neurons have to be associated with targets.

- The synaptic time constant can't be too long compared to the timescale of the target functions.

- the synaptic time constant can't be too short compared to 1/N (N is the number of neurons in the network).

- The training period can't be too long compared to N.

These rules provide insight into the limits of performance of spiking RNNs, something that has, I believe, been lacking in the field. [Minor comments not shown.]

Reviewer B comments:

The authors present an interesting study examining the capability of recurrent networks of QIF neurons for learning various types of signals. They apply a RLS learning rule so that the network produces various periodic functions, filtered noise, the activity of chaotic networks, and experimental data. They present evidence to support their contention that two key conditions need be met for learning: (1) including a sufficiently rich set of target functions; (2) appropriately matched synaptic time-scale relative to the target dynamics. Additionally, a mean field analysis was performed and shown to be consistent with dynamics after learning.

While a handful of curious findings are presented, for the following two reasons I do not believe the work, as presented, is suitable for publication in this journal.

First, the examples, learning conditions and supporting experiments do not constitute a significant advance over previous work. While I cannot refer to prior work that has studied the ability to produce the specific signals presented, the authors do not properly motivate the importance of these particular signals. Prior publications that train RNNs (spiking too) typically focus on constructing networks that can perform tasks, where the motivation for the signals they construct is obvious: they use signals necessary for performing computations. For three of the examples (rate chaos, OU noise and spiking chaos) it's not clear what computation these networks might perform after learning (in fact, the primary motivation for stabilizing rate chaos, e.g. in FORCE learning, was so that the network COULD produce a computation after learning). In the case of the work of Laje and Buonomano (which the authors claim to extend to spiking networks), they sought to stabilize chaotic rate trajectories as a model for understanding timing tasks; here the authors do not present any use for these dynamical patterns, just that they can be learned.

Second, the presented work is simultaneously too technical (and therefore too specific) and too vague to be of significant interest to the general neuroscience community. The mean field analysis is interesting and stands out when compared to other published works, which have not extensively studied how analytic solutions compare to simulations in trained networks. Nevertheless, this is a minor, technical point, not likely to be interesting to most neuroscientists (unless the authors can explain why this is interesting).

While the question of universal computation is of general interest, the presented results are not sufficiently rigorous to match the claims. While they claim that previous work has been impressive but not sufficient to showcase the full richness of what can be expressed by spiking RNNs, the authors claim to learn "arbitrary" and "near universal" dynamics but only show examples (as previous work has) from a rather small set of potential dynamics. If this paper were to be published, the authors would need to clarify what they mean by this to accurately reflect the presented results or include a proof of the universality they are claiming to show. Another question of general interest is what constitutes a "sufficient basis" for learning but here again the authors only provide a few examples that are not shown to extend beyond the direct application studied. This approach is inferior to previous methods, since no prescription is offered for establishing sufficiency other than generating additional random signals; in previous work where specific computations were examined, the only signals required were those necessary for performing the computation and these could be "bootstrapped" by exploiting knowledge about the train-ability of firing rate networks. The authors offer a bold claim (identifying the sufficiency of a rich basis) with pretty weak support (just keep adding random signals).

I conclude by highlighting the most interesting and promising result: training with neural data. That the training required auxiliary dynamics is interesting and provides a prediction of a set of dynamical patterns that should exist in the brain in order for the network to perform the task it did. Expounding on these results would yield a very interesting finding, albeit beyond the scope of a simple revision to the present work.

A's response to B's comments (during discussion phase):

My main feeling is that they are looking at a very different problem than anybody else: they're training every single neuron (or a large fraction of neurons) to produce target functions, with different target functions (but similar timescales) for each neuron. This is, in my opinion, completely unrealistic – it's much more realistic to train networks to produce relatively low dimensional output patterns. But what I thought was interesting was that the paper gave bounds on performance in general in terms of timescales of the network and the target output of each neuron. If you can't produce target functions with a particular timescale when you can train each neuron individually, I would think that you certainly can't train the network as a whole to produce target functions with that timescale. Which is a point they might have emphasized more, but that would be easy to fix. But maybe I'm interested simply because it was something I always wondered about.

With this view, your first objection, which is that they didn't consider interesting functions, becomes, I think, moot. Your second objection is that the work is too technical and too vague. I agree the mean field analysis is very technical, and will be followed by only a handful of people. But it doesn't seem to be an integral part of the paper. And I think the rest is pretty easy to follow. Not sure what you meant by too vague – could you expand?

You also say that their results are not sufficiently rigorous. However, if they can make the arguments rigorous, would you be satisfied, at least about the rigorousness (but not necessarily about the first two points)?

B's response to A:

I disagree with you that they are looking at a different problem than anybody else. However, none of this works addresses the conditions for learning, I agree with you there.

I agree with you that understanding the limits of learning in RNNs is interesting and lacking, but to me, their results related to that point only account for a fraction of the full paper. As written, that point is embedded within a range of other findings that are unmotivated (e.g. the various other signals they train networks to perform that do not support their results about the limits of learning), incomplete (using data to train networks, as I wrote in my review) and that do not ultimately support the point about learnability. However, if they were to remove these other results, the point on learnability alone would not constitute a full paper.

In my view, they introduce two main conditions for learning: that the synaptic timescale should roughly match the targets and that the targets should be "suffciently rich". The second condition highlights my concerns about the vagueness and rigorness of the results. They illustrate the need for sufficient richness by removing targets from some of the training sets they used and show that these network cannot learn (Figure 3). While this is anecdotally interesting, I do not believe that illustrating that this is true in a handful of cases is sufficient to say anything general about the conditions necessary for learning. At best, this is good enough to make some pretty hand-waving arguments about the need for an overcomplete basis, which is precisely what they do in Section 2. Again, it's not that I don't find this interesting, I just don't seem much substance there.

Their first condition for learning is definitely much more rigorously addressed (the simulations and calculations of Figure 6 are nice) but I find this neither surprising or groundbreaking (you can't learn slow signals without slow synapses, or fast signals without fast synapses....) I think this point could be stated much more simply without the need for the various training targets they used (chaotic rate models and stochastic noise) which again, strengthens my resolve that much of what they do feels unmotivated. Even though Figure 6 being nicely done, 1 figure is not enough for a paper.

Finally, I think the tasks they are learning are perfectly "interesting", just unmotivated.
