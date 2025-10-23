# Author response - Round 1

Authors:
- Takayuki Tsurumi
- Ayaka Kato ([ORCID: 0000-0002-6306-6600](https://orcid.org/0000-0002-6306-6600))
- Arvind Kumar ([ORCID: 0000-0002-8044-9195](https://orcid.org/0000-0002-8044-9195))
- Kenji Morita ([ORCID: 0000-0003-2192-4248](https://orcid.org/0000-0003-2192-4248))

## Response text

DOI: [10.7554/eLife.104101.4.sa4](https://doi.org/10.7554/eLife.104101.4.sa4)

The following is the authors’ response to the previous reviews.

Reviewer #1 (Public Review):

We thank the reviewer for the positive feedback on the work. The reviewer has raised two weaknesses and in the following we discuss how those can be addressed.

Weaknesses:

The impact of the article is limited by using a network with discrete time- steps, and only a small number of time steps from stimulus to reward. They assume that each time step is on the order of hundreds of ms. They justify this by pointing to some slow intrinsic mechanisms, but they do not implement these slow mechanisms is a network with short time steps, instead they assume without demonstration that these could work as suggested. This is a reasonable first approximation, but its validity should be explicitly tested.

Our goal here was to give a proof of concept that online random feedback is sufficient to train an RNN to estimate value. Indeed, it is important to show that the idea works in a model where the slow mechanisms are explicitly implemented. However, this is a non-trivial task and desired to be addressed in future works.

As the delay between cue and reward increases the performance decreases. This is not surprising given the proposed mechanism, but is still a limitation, especially given that we do not really know what a is the reasonable value of a single time step.

In reply to this comment and the other reviewer's related comment, we have conducted two sets of additional simulations, one for examining incorporation of eligibility traces, and the other for considering (though not mechanistically implementing) behavioral time-scale synaptic plasticity (BTSP). We have added their results to the revised manuscript as Appendix. We think that the results addressed this point to some extent while how longer cue-reward delay can be learnt by elaboration of the model remains as a future issue.

Reviewer #2 (Public Review):

We thank the reviewer for the positive feedback on the work. The reviewer gave comments on our revisions, and here we discuss how those can be addressed.

Comments on revisions: I would still want to see how well the network learns tasks with longer time delays (on the order of 100 or even 1000 timesteps). Previous work has shown that random feedback struggles to encode longer timescales (see Murray 2019, Figure 2), so I would be interested to see how that translates to the RL context in your model.

We would like to note that in Murray et al 2019 the random feedback per se appeared not to be primarily responsible for the difficulty in encoding longer timesclaes. In the Figure 2d (Murray 2019), the author compared his RFLO (random feedback local online) and BPTT with two intermediate algorithms, which incorporated either one of the two approximations made in RFLO: (i) random feedback instead of symmetric feedback, and (ii) omittance of non-local effect (i.e., dependence of the derivative of the loss with respect to a given weight on the other weights). The performance difference between RFLO and BPTT was actually mostly explained by (ii), as the author mentioned "The results show that the local approximation is essentially fully responsible for the performance difference between RFLO and BPTT, while there is no significant loss in performance due to the random feedback alone. (Line 6-8, page 7 of Murray, 2019, eLife)".

Meanwhile, regarding the difference in the performance of the model with random feedback vs the model with symmetric feedback in our settings, actually it appeared (already) in the case with 6 time-steps or less (the biologically constrained model with random feedback performed worse: Fig. 6J, left).

In practice, our model, either with random or symmetric feedback, would not be able to learn the cases with very long delays. This is indeed a limitation of our model. However, our model is critically different from the model of Murray 2019 in that we use RL rather than supervised learning and we use a scalar bootstrapped (TD) reward-prediction-error rather than the true output error. We would think that these differences may be major reasons for the limited learning ability of our model.

Regarding the feasibility of the model when tasks involve longer time delays: Indeed this is a problem and the other reviewers have also raised the same point. Our model can be extended by incorporating either a kind of eligibility trace (similar one to those contained in RFLO and e-prop) or behavioral time-scale synaptic plasticity (BTSP), and we have added the results of simulations incorporating each to the revised manuscript as Appendix. But how longer cue-reward delay can be learnt by elaboration of the model remains as a future issue.

Reviewer #3 (Public Review):

Comments on revisions: Thank you for addressing all my comments in your reply.

We are happy to learn that all concerns raised by the reviewer in the previous round were addressed adequately. We agree with the reviewer that there are several ways the work can be improved.

The various points raised by the reviewers at weaknesses are desired to be taken up in future works.
