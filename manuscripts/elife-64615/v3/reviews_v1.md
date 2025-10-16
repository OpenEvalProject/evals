# Peer review - Round 1

Editors:
- Jonathan W Pillow, Princeton University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64615.sa1](https://doi.org/10.7554/eLife.64615.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper introduces a new framework for modeling correlated neural population spike responses using multivariate mixtures of Poisson or Conway-Maxwell-Poisson distributions. It describes an algorithm for fitting the model to data using Expectation Maximization (EM), a formula for Fisher information, and a Bayesian decoder that is competitive with other more computationally demanding decoding methods such as artificial neural networks. The authors apply this model to V1 data from awake and anesthetized monkeys, and show that it captures the variability (eg., Fano Factor) and co-variability of population responses better than Poisson models. Finally, the paper shows how the latent variables of the model can provide insight into the structure of population codes. The resulting framework represents a powerful advance for modeling the correlated variability in neural population responses, and promises to be a useful new tool for analyzing large-scale neural recordings. The paper will be of interest to computational neuroscientists studying neural coding, and to system neuroscientists who use descriptive models to characterize the stimulus tuning of correlated spiking activity recorded from large neural populations.

Decision letter after peer review:

Thank you for submitting your article "Modelling the neural code in large populations of correlated neurons" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Kenneth D Harris (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

1) Clarify abstract (and optionally title): see comments from R1.

2) Address R1 comments about claims "C1" and "C2".

3) Compare performance of the proposed models to existing models that capture stimulus encoding by large populations of correlated neurons (see comments from R2).

4) Clarify how users should decide how many mixture components to add. (R3 comment 4).

5) Provide publicly released code.

Reviewer #1 (Recommendations for the authors):

1 – A main suggestion is to rewrite the title and abstract as I outlined in Weakness #1 in the public comments.

2 – Address 2.1-2.3 (under weaknesses), in the public comments or eliminate/tone down the claims C1-C3, in the abstract, intro, discussion or elsewhere.

3 – I found the discussion around Figure 5 hard to follow. To improve this, I suggest that authors provide (already in the Results section) simplified/readable formulas (valid for the "vanilla" Poisson case which is used in this section) for the stimulus dependence of index probabilities (IP) which depends on the mean population response according to

p(k|x) ∝expθK(k) + r(x|k)

where r(x|k) is the average total population spike count in the mixture component k, which I believe is given by the partition function ψN.

4 – As they point out, in their minimal model, the tuning curves (mean response) of neurons are scaled ("gain modulated") versions of the "baseline"-component's tuning curves. Again, I think it would help to write a formula for this in the Results section, and connect the scale factor and the baseline tuning curve with the θNK and θN(x) components, respectively.

5 – I don't think the simple scaling (see previous comment) relationship actually holds in the non-Vanilla CoM case, but they do claim that. If so, the text in lines 189-192 (especially "scaled" in line 191) should be corrected.

6 – As they derive in the Methods part, the population covariance matrix of the CPM has the same form as the covariance matrix in factor analysis: a diagonal "private noise" matrix + low-rank "shared-noise" matrix. I think it would be valuable to point this out and write the corresponding formula in the Results section e.g. around Figure 2. Also point out what happens to the diagonal term in the vanilla vs. CoM cases.

7 – The ground truth exercise of Figure 3 is valuable, but I think more valuable than showing how the model fits one example would be to give an idea of the "sample complexity": give an idea of goodness of fit vs. number of trials in the dataset. (At least clarify in the caption how many trials per stimulus conditions were used.)

8 – Not sure what the exercise described in lines 310-321 shows. Given that the gound truth model is within the fit model family, isn't it given (by classical asymptotic statistics results) that for large enough data the likelihood and therefore the posterior should converge the true posterior?

So is the result really surprising given that the dataset seems pretty large (d_T=10000)?

Again the more relevant thing would be: what is the minimal amount of data needed to find a good posterior approximation… or as a simpler version: how would it do for typical neural dataset sizes (# trials). (c.f. the previous comment).

9 – lines 359-371 – especially line 365-6: The reasoning here (that the shown results establish the information-limiting nature of the noise) are not really complete. Technically, "Information-limiting" means that the Fisher info is not extensive, i.e. does not scale linearly with population size. So they have to argue that the "random shifts" (discussed in line 365) will not go to zero as. Population size goes to infinity.

Reviewer #3 (Recommendations for the authors):

Line 103: Some more introduction to CoM Poisson distributions would be nice. Why are these better than the negative binomial, which is analytically more tractable? Presumably because they can handle underdispersion? Neural data is usually overdispersed, but does the extra dispersion introduced by a mixture model mean one needs to use underdispersed components for the mixture components?

Line 119: "express multivariate Poisson mixtures in an exponential family form". This is misleading: it sounds like you have expressed the marginal distribution of the mixture model in exponential form, which I believe is impossible. In fact, you are expressing each component distribution in exponential form.

Line 150: "vanilla mixtures". Why not call them Poisson mixtures? That's what they are.

Line 159: "optimized model parameters as described in Materials and methods". You mean you used the EM algorithm derived in Materials and methods? Say so explicitly.

Figure 2. Is this cross-validated? From the text it seems not, so no wonder the CoM model, with more parameters, fits better. Also, why does the vanilla model ever produce FFs that are too low? Can't it just add more mixture components to increase dispersion?

Line 180: the "CPM" sounds like a mixture of generalized linear models. If so, "mixture of GLMs" would be more familiar terminology for most readers.

Line 193-227: it is not clear what we really learn from this. If it just is a validation that the EM algorithm can work on simulated ground truth, then shouldn't that go first, before the application to real data? Also comparing to a less sophisticated model would help show the benefits of this one.

Table 1: please state how many cells are in both data sets.

Line 238: "log likelihood". Please specify if this is to base 2 or base e; also give a unit in table 1 (e.g. bits/trial).

Figure 5: it would be nice to see this applied to real data.

Line 466: do you mean ψN = ∑i θN,i? The log partition functions should add, right?

Equation 12: is there a denominator of ∏i ni! missing?

Line 573: how much time does the gradient ascent take? Is it going to be a problem for recordings with large numbers of neurons?
