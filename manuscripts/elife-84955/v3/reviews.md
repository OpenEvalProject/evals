# Peer review - Round 1

Editors:
- Birte U Forstmann, https://ror.org/04dkp9463 University of Amsterdam Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84955.sa0](https://doi.org/10.7554/eLife.84955.sa0)

This valuable paper presents findings showing that different brain regions were best described by a distinct accumulation model, which all differed from the model that best described the rat's choices. These findings are solid because the authors present a very strong methodological approach. This work will be of interest to a wide neuroscientific audience.


---

# Peer review - Round 1

Editors:
- Birte U Forstmann, https://ror.org/04dkp9463 University of Amsterdam Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84955.sa1](https://doi.org/10.7554/eLife.84955.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Neural population dynamics underlying evidence accumulation in multiple rat brain regions" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Brandon Turner (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions (for the authors):

1. I found some of the decisions about the model development to be somewhat unusual, and I wondered whether the results hinged on these assumptions. To be clear, I am fine with unusual, but I was not clear how the authors came to the decisions they made. I think it would be better to describe why some decisions were made. For example, Equation 1 uses both the sum and difference of the evidence directly in the accumulation dynamics, but I wonder why the authors used this expression and not the standard DDM. It was also unclear why leakage was added in this way (where λ can be negative) for a model that uses a two-boundary setup (i.e., a non-racing accumulator structure). Other unusual things were the step function combined with a contaminant process (lapse) to relate to a probability of choice and a softplus function for the neural activity (Equations 2 and 3). Because these were choices I was unfamiliar with, I wondered where they were from and whether their incorporation had any impact on the results.

2. I also felt that the paper was lacking some connection to other joint modeling efforts that use trial-by-trial parameters to link neural and behavioral data. These are not quite the same as the authors' approach, but it could be good to link to those many lines of research to leave some 'breadcrumbs' for other researchers who are interested in modeling brain-behavior links.

3. Why are there two absorbing bounds, one for a(t) and one for the choice criterion? Evidence accumulation models typically impose an absorbing bound for (an analogue of) a(t), and assume a choice is made when that bound is reached. Can the authors clarify the purpose of deviating from this assumption?

4. Page 13: Reference to Figure 4A might mean 4B.

5. Equations 10-11: I'm wondering to what extent there might be a collinearity issue here. These models allow firing rates to vary over time as a function of two mechanisms: \theta_{n}a_t, which is time-varying because a varies over time; and \theta_{n,t}^{0}, which is time-varying by itself through equation 11. I was wondering: If firing rates indeed covary with a, then doesn't the model have two options to model this: both via \theta_{n} and via \theta_{n,t}^0?

This point is especially relevant for the section on the independent noise accumulator models, where \theta_{y} is fit for every neuron individually, and as such, these parameters are informed by relatively little information which might increase the uncertainty on these parameters. Are the results shown in Figure 4B not potentially an overfitting issue? A related question here pertains to the cross-validation procedure: How exactly are the data partitioned? If the parameters fit on the individual neuron level, then the split between train and test data should only split trials of the same neurons (under the independent noise model, \theta_{1,T} cannot be expected to predict \theta_{2,T}, as these are different neurons, I would think? Or am I missing something?).

6. Page 39: were the bounds of optimization ever reached?

7. Null joint model: This is related to the point above, but I'm not sure if Figure S9B (referred to on page 42) actually shows the results of this model. I was indeed wondering how well this model cross-validates, in light of the potential collinearity issue raised in point 3 above.

8. Figure S9A: I don't see '+'-symbols.

9. Typos.

Page 21, Figure S1C title: "Example recovered parameters" (missing e in parameters).

Page 36: "The transition matrix M(θa, δt) it is determined using methods established in Brunton (2013)". "it" should probably be removed.

10. Code availability:

The authors state they will make the code publicly accessible upon publication. It would be useful to include a persistent link (to e.g. osf or github) in the manuscript to facilitate finding the manuscript after it has been published. The code itself could still remain under embargo as long as the review lasts, should the authors prefer this.
