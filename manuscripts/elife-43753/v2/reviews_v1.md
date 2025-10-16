# Peer review - Round 1

Editors:
- Peter Latham, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.43753.019](https://doi.org/10.7554/eLife.43753.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Complementary congruent and opposite neurons achieve concurrent multisensory integration and segregation" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

It is often the case that the brain receives more than one cue about a quantity of interest. Not surprising, in multisensory areas many neurons have similar tuning to the two cues. Slightly more surprising, some neurons have opposite tuning to the two cues. So far we do not have a clear and unified explanation for the opposite tuning; this paper provides one. The authors extended their previous work (Zhang et al., 2016), and show that the opposite tuned neurons can be used to determine whether or not the two cues are really providing information about the same quantity. They also provided plausible neural circuitry, consisting of a decentralized attractor network, for doing this. This is an important result, and although the material is a bit dense, overall the manuscript is clearly written.

Essential revisions:

We have only one major comment: Despite claims by the authors that their model performs Bayesian inference (e.g.: "Equation 4 is the result of Bayesian optimal integration"), we believe that it doesn't. To perform Bayesian inference, it's necessary to have a prior that allows the two cues to be either the same or different; something like

p(s1, s2|x1, x2) ∝ p(x1, x2|s1, s2) p(s1, s2)

= p(x1|s1) p(x2|s2) [p0δ(s2-s1) + (1-p0) p(s2-s1)]

where δ(…) is the Dirac δ function. (It's actually a bit more complicated, since it's possible that only one cue is present, and in general the cues should have different amounts of reliability, but an extension to that wouldn't be too hard.) To make contact with the paper, one can integrate over s2, yielding

p(s1|x1, x2) = ∫p(s1, s2|x1, x2) ds2 ∝ p0 p(x1|s1) p(x2|s1) + (1-p0) ∫p(s2-s1)p(x1|s1)p(x2|s2)ds2

= p0 p(x1|s1) p(x2|s1) + (1-p0) ∫p(z)p(x1|s1)p(x2|s1+z)dz

If p(z) = δ(z-pi), then

p(s1|x1, x2) ∝ p0 p(x1|s1) p(x2|s1) + (1-p0) p(x1|s1) p(x2|s1 + pi).

In this case, one recovers the two terms in the paper: the first term corresponds to Equation 3; the second to Equation 6 (both under a flat prior).

However, it's not the case that p(z) = δ(z-pi); instead, p(z) is, we believe, more or less uniform. In that case the integral over z is probably tractable, although we admit that we haven't checked.

Given the above analysis, we see two possibilities:

1) Admit that this model is reasonable, but it doesn't do Bayesian inference for the cue integration problem.

2) Show that the above analysis, or something like it, does lead (at least approximately) to the network that the authors end up constructing.

Option 2 would be preferable, and we have the feeling that it would be possible, but we would be happy with 1 as well.

Other points:

1) We assume that the preferred direction used in the population vector decoding is the preferred heading of the neuron's major input. We didn't see that stated explicitly (although we may have missed it). It would be worth noting that, for example in the legend in Figure 6 or in Equation 22.

2) Abstract, last sentence: We don't see results that support 'rapid' decision making (compared with what?). Concurrent does not always mean rapid. We would suggest either emphasizing this less, or providing supporting evidence.

3) Introduction paragraph three: We think the concerns about losing information about individual cues during integration is exaggerated. Primary sensory cortices along with working memory may maintain the information, especially if segregation can be done rapidly.

4) Discussion paragraph seven: Neurons responding to center and surround differently may not be good examples. Here, cues are motions in different spatial locations (center vs. surround). In the problem of multisensory integration, different cues encode the same variable (e.g., heading).

5) Discussion paragraph three: Suggested experiments don't seem to test the network structure proposed here. Can you come up with experiments that dissect the network structure? For example, how does activity change in other areas when one area is inactivated? Would you expect to see negative correlations in spiking activity between opposite neurons in the two areas and positive correlations between congruent ones? How about optogenetic inactivation experiments (even if the technique is not fully established in monkeys) that show characteristic rebound activity, as shown in Guo et al., 2017 Nature paper from Svoboda lab?

6) Subsection “Neural encoding model”: In the network, distribution of preferences is uniform. However, the distribution of visual or vestibular preference is bimodal with more neurons preferring lateral headings (Gu et al, 2006). Are the results still consistent in that situation?

7) We're somewhat curious whether there are computational benefits of a decentralized network versus a centralized one. If the authors have some thoughts on this, they would be worth mentioning. But it's not necessary.
