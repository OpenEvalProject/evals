# Peer review - Round 1

Editors:
- Agnese Seminara, https://ror.org/0107c5v14 University of Genoa Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72415.sa0](https://doi.org/10.7554/eLife.72415.sa0)

This article by Jayaram and colleagues uses computational modeling approaches to examine how temporal filtering of an odor signal contributes to navigation success in different odor environments. The article advances the literature in considering how different algorithms may be optimal for different environments. The provided evidence suggests an intriguing trade-off between frequency and ‘intermittency’ sensing.


---

# Peer review - Round 1

Editors:
- Agnese Seminara, https://ror.org/0107c5v14 University of Genoa Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72415.sa1](https://doi.org/10.7554/eLife.72415.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Navigating a diversity of turbulent plumes is enhanced by sensing complementary temporal features of odor signals" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jeff Riffell (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Discuss the role of odor intensity, for example as suggested by referee 1.

2. Test the performance of the algorithm to more realistic conditions either in vitro or in vivo (see suggestions referee 1).

3. Include a Figure like 2C and 2F for the simulated odor plumes considered in the second half of the paper.

4. Better justify the use of expression (6) for example as suggested by referee 2.

5. Show results for a logical 'or' combination of inputs and consider other alternatives, as suggested by referee 2.

6. Compare results to a null model that surges in response to any signal above threshold with no frequency filtering, and analyse performance as a function of the filtering cutoffs.

7. Discuss what you expect the frequency content of natural plumes to be.

Reviewer #1 (Recommendations for the authors):

I am enthusiastic about the authors past work in this domain, but I have a few suggestions on the current work.

1. Incorporating odor intensity into the simulated model. Presumably, the authors have related information on this topic from their previous work. I'm curious whether the interaction between "rate" and "intermittency" is related to the flux of the odor experienced by the navigating fly (or agent).

2. The authors simulate only two different plumes, but in nature, these plumes are dynamic and could be a combination based on the turbulent air conditions. Under a range of intermittency/rate conditions, how do the model results hold up? And how about then the plume dynamically changes between the two environments?

3. Alternately, empirical testing using fruit flies in an arena like their previous study, but stimulating the flies with odor pulses that simulated the model intermittent and rate plumes, would strengthen the authors' results.

Reviewer #2 (Recommendations for the authors):

I have three suggestions for the authors:

1. It would be very helpful to have a Figure like 2C and 2F for the simulated odor plumes considered in the second half of the paper in oredr to make a comparison.

2. The expression (6) while sensible does not have a strong justification. The authors should clarify if there is any indication that the neural system of flies is actually combining the output of two different signal processing units, one for intermittency and one for frequency, through a simple perceptron as they do in (6). It would also be interesting to know if there are ways to test this hypothesis.

3. Related to 2, a different and possibly more compelling way to express the combination of inputs is to use a simple perceptron that implements an OR function instead of (6). Indeed, this appears the most natural choice to obtain high upwind turning probabilities with high intermittency or high frequency. The authors are warmly encouraged to show results for this other choice, and possibly other "logical" ANNs as well.

Reviewer #3 (Recommendations for the authors):

line 283: setting sensor gains to zero. Can this be compensated by increasing the gain of the other sensor?

~line 334: what is the molecular diffusivity of air how does this compare to the values modeled here?

Figure 4, E and F: it might be helpful to explore a finer range of gains close to 1 here.
