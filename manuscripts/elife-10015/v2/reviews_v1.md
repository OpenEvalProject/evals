# Peer review - Round 1

Editors:
- Timothy Behrens, Oxford University , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10015.022](https://doi.org/10.7554/eLife.10015.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Internal models for interpreting neural population activity during sensorimotor control" for peer review at eLife. Your submission has been favorably evaluated by Timothy Behrens (Senior editor), and two reviewers.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper describes a novel statistical analysis of population neural activity in M1 during brain-machine interface (BMI) control. It reports that errors in BMI control can be understood in terms of a mismatch between a true control model and an "internal" control model assumed by the animal. It shows that population activity accurately takes account of the time-lag in visual feedback, and compensates for a perturbation of the true model by a corresponding perturbation of the internal model.

The paper is well written, interesting and highly original, and is likely to be of broad interest to the BMI community as well as to the broader community of neuroscientists interested in issues of population coding, dimensionality reduction, and motor control.

Essential revisions:

1) First, I admit I am struggling a little bit to understand why I shouldn't adopt the conclusion offered in the Discussion that "it might be tempting to view an extracted internal model as simply the BMI mapping that should have been identified during calibration." The authors give several arguments here but sometimes I don't entirely follow them. The true model here is linear difference equation. The (fitted) internal model also takes the form of a linear difference equation, and accounts for a substantial fraction of the errors. This indicates (if I understand the claims correctly) that if the experimenters had used the learned internal model instead of the "true" model to drive cursor position, the BMI performance would have been much better. So I'm puzzled about why the authors don't feel that this is the straightforward conclusion of the paper. (Couldn't this be considered a positive result, i.e., a finding that suggests a much better way to improve BMI training? I suppose a drawback to this framing is that if the paper were pitched as a better way to train BMIs, we would presumably expect to see that it actually works, i.e., show some data where the estimated internal model is used to drive behavior and achieves much lower error).

2) A related concern: the paper asserts that the good performance of the estimated internal model shows that the limits to performance are the observer's inaccurate estimates of the model, as opposed to noise in the neural activity. I'd like to suggest a third possibility: could it possible that it's not noise, but rather systematic problems in producing neural activity patterns needed to optimally drive the BMI? For example, suppose the animal could only produce activity patterns corresponding to motion in the 4 cardinal directions. Then it would to alternate between producing these patterns in order to drive a diagonal cursor movement. Or (more realistically), suppose there were only certain fixed points in neural activity space that M1 can easily visit. These fixed points might be systematically misaligned with the directions needed to optimally drive the controller. Re-estimating the internal model allows the best linear mapping from these allowed neural activity patterns to those that can drive the cursor as needed during the experiment.

I raise this possibility in part because it seems like this was the conclusion of the Yu & Batista groups' nature paper last year, showing that control within an intrinsic manifold (as defined by the state space explored by the network prior to BMI activity) is much easier than outside this manifold. I realize it is likely that the "intuitive" training procedure would latch on to "out of manifold" patterns, since it tries to use activity during training to define the controller. But it would still be nice to rule out this kind of effect – could it be that rather than insufficient knowledge of the controller, the difference results from differences in the ease with which certain network states can be visited?

3) Result one is that compensation for feedback delay indicates the existence of an internal model. My confusion is that, because equation 1 includes cursor velocity as an input, couldn't it be doing this extrapolation all by itself? How does extrapolation provide evidence of an internal model if the external model could be doing it? Don't you need to show that the internal model is doing a better job of extrapolation that equation 1 possibly could?

4) The second issue is whether it is justified to call equation 2 an approximation of an internal model. The authors discuss reasons why equation 1 and 2 are not identical, that is, why the internal and external models don't match. Let me provide a simplified analogy. Suppose a single scalar were being extracted from u by x = Bu (in other words, ignore A and b for the moment). In the initial "intuitive BMI mapping" B is defined by a procedure that is not well explained. Suppose that, on each trial u = u0 + s, where u0 would give perfect performance and s is noise. Clearly Bu0 = x (the correct x), but has B been chosen to minimize the effects of noise? That is, has Bs been minimized? If the noise is correlated, this can be done. What if B~ is simply more orthogonal to the major PCs of s than B? Wouldn't this explain the effect? Even if the parameters of equation 1 are optimal with respect to noise, how do we know that the correlation structure of s has not changed by the time the model of equation 2 was constructed?

In summary, the paper would be strengthened by a more convincing case that evidence for an internal model has been obtained and that equation 2 can be interpreted as an approximation for this internal model.
