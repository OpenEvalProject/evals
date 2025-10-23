# Peer review - Round 1

Editors:
- Peter Latham, University College London , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23978.018](https://doi.org/10.7554/eLife.23978.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Attentional modulation of neuronal variability in circuit models of cortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Ruben Coen-Cagli (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All three reviewers found the paper interesting and potentially important. Of particular note is the demonstration that a single source of attentional modulation in an E-I network can explain both increases in firing rate and decreases in noise covariance, without the need to postulate separate effects. In addition, the modelling is solid and convincing, and the result is an important advance in our understanding of attentional effects.

However, there are a couple if issues that need to be addressed:

1) Robustness to network parameters and assumptions needs to be explored.

2) The rank-1 covariance needs to be better quantified.

3) Information was about contrast, whereas the experiment was about orientation change detection. This is important because the rank 1 covariance matrix is unlikely to have much effect on information about orientation.

It won't be completely trivial to address these issues, but we believe they are addressable.

It is eLife's policy to provide a summary of essential revisions. That's hard to do for these reviews, as they were all relatively extensive. I am, though, going to give it a shot. The exposition will be a little uneven, as I combined the reviews, without trying to edit for uniformity.

1) A big issue is robustness to parameters. Essentially what we want to know is: what are the constraints on parameter space for the results to hold qualitatively? It's probably hard to fully answer this, but it should be possible to provide answers for some of the more important parameters. Following are some more specific points.

First is a long comment about two of the modelling assumptions:

- The weights scale as 1/N.

- Perfect balance (JEE = JIE = JE and JII = JEI = JI).

This 1/N scaling is different from the usual one, which is 1Nand in that regime perfect balance is problematic. Granted, the 1Nscaling is probably too large, but 1/N is probably too small. At the very least, the authors need to comment on this scaling – after all, the last author just published a paper on correlations which was based on 1Nscaling. We're not suggesting that the analysis be redone, but it would be good to know whether the analysis really does apply to biologically plausible connectivity.

Now, a couple of technical comments relating to these points.

The first one is mainly a suggestion. The authors use the 1/N scaling to argue that the first term in Equation 3 of SM (the full-rank component of the covariance matrix) is O(1/N). But this may not be necessary. An instructive case is completely homogeneous coupling, in which Jij depends only on the type (E versus I) of neurons i and j, the probability of connection is 1. In this case, if the scaling is 1Na back of the envelope calculations indicates that the first term in Equation 3 of SM scales as 1/N. I believe that if iid noise is added to the weight matrix (while retaining the 1Nscaling), the first term in Equation 3 of SM would still scale as 1/N, but I'm not sure. This should probably be checked: if it one turns out to be correct, it would go a long way toward dispelling doubts about the 1/N scaling.

Second, in Equation 7 the authors derive an expression for the variance over long time windows. This was derived under the perfect balance assumption. If that assumption is dropped, there's an additional term in the denominator that scales as LE LI -Det(J) (where J is the 2x2 matrix of weights). If the components of J are large – as they probably are in realistic networks -- this can have a large effect. Is it possible to estimate its effect for realistic networks? How would that change the results?

A couple semi-minor points on robustness:

a) Equation 7 depends on σE – σI. That's taken to be negative (Table 1). How much do the results change if it's positive?

b) In real networks, an increase in drive (which is how top down attention is modelled) would probably lead to an increase in noise (because variance scales with spike count). I think it would be important to estimate how large an increase in noise could be tolerated without an increase in covariance with attention.

2) The rank-1 covariance

a) The authors tell us that the modulation matrix is close to being rank one, but they tell us nothing about the vector of modulation gains defining this rank one matrix. I would like to see answers to basic questions such as: What is the distribution of gs? Are they correlated with as (firing rate modulations) and/or with baseline firing rates? Or with the vectors obtained using low-rank approximation of the covariance matrix itself? The model must make specific predictions about the answers to all these questions, and it would be nice to see these predictions tested.

b) It is unclear why the authors used their method for low rank approximation, as opposed to more standard methods based on SVD (that naturally provides a quantification of the quality of a general low rank approximation based on singular values). I think it would be useful to check what they get using alternate methods, to check the robustness of their results.

c) The data in Figure 1D show a broad range of effects of attention on noise covariance, but the model addresses only the overall reduction in the mean, not any other property of the distribution (including the fact that there are a substantial minority of cases with increased covariance under attention). Isn't is possible to study the distribution across the network model, at least in simulations? And again, the structure of the covariance (and tuning) is important to determine information.

d) A separate, smaller issue is the assumption that attention acts as a low-rank modulation of noise covariance. The opening statement in the Results, subsection “Attention as a low-rank modulation of noise covariance” is that "we need to first understand the dimension of attentional modulation", as if a model-comparison of some sort was going to be performed between low-rank and full-rank modulations. Instead, there is only a quantification that the low-rank assumption works reasonably well, but no comparison to a higher-rank description. Also, why is the assumption of a multiplicative effect better than e.g. additive modulation? This could be quantified.

3) Fisher information: contrast versus orientation.

My main concern is that I see a disconnect between the modeling and the data/experimental paradigm that motivate the modeling.

I am not convinced about the generality of the conclusions on the effects of attentional modulation on population coding in the model. The experiment is about orientation-change detection, but in the modeling the stimulus dependence is more like contrast (all neurons are identically modulated by the stimulus intensity) than like orientation (where a change in stimulus value would drive some neurons up, and others down). This is acknowledged in the closing paragraphs, and suggested as future work, but I wonder if it should instead be done as part of this paper. I am no expert in EI networks, I don't know how long it would take, but here is concretely what I would like to see and why. Add the stimulus drive in the actual network, not just in the mean field solutions. And while doing that, assume heterogeneity (and possibly nonlinearity) of tuning. If the stimulus acts like contrast, then doing the information analysis on the mean field is fine; but otherwise the mean field solution is effectively a suboptimal decoder (weight all neurons equally), and the conclusions about information may be only valid for that decoder, not for the optimal decoder. The rank-one external noise by itself does not limit information for orientation-like stimulus dimensions (unless you modify it to exactly align it with the signal) (e.g. Moreno-Bote et al., 2014), so some other source of differential correlations needs to be considered if you want the attentional modulation to have any chance of improving information.

We'll admit that this may be a hard one to address rigorously. But the authors should provide an extended discussion of this issue. And an attempt should be made to provide approximate calculations and/or estimates.
