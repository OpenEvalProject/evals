# Peer review - Round 1

Editors:
- Ramon Grima

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69324.sa1](https://doi.org/10.7554/eLife.69324.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The revisions have substantially improved the manuscript. In particular the authors have clarified the connection of the present work to previous work and shown that their method's accuracy in identifying noise sources does not depend on the details of the gene expression model used. The novel method is based on multiple generic reporters from the same biochemical pathways. Since now it is possible to do simultaneous measurements of transcripts and proteins in single cells, this method offers a viable alternative to the standard dual reporter method, as a means to infer the magnitudes of intrinsic and extrinsic transcriptional noise.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Pathway dynamics can delineate the sources of transcriptional noise in gene expression" for consideration at eLife. Your article has been reviewed by 3 reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. Although the work is of interest, we are not convinced that the findings presented have the potential significance that we require for publication in eLife.

Specifically, some of the main critical comments overlapping between one or more reviews are: the need for experimental confirmation of the approach, major issues with the model assumptions and potential overlap with previously published works. Several recommendations have been made by the referees and we hope you find these useful. However it appears that the changes needed are considerable and the paper would need to be rewritten, hence the decision to reject the paper in its current form.

Reviewer #1:

Ham et al. present a manuscript that attempts to answer two main questions:

(i) Is it possible to identify the relative sources of population heterogeneity from

the measured transcript abundance distribution alone?

(ii) Can one develop a method that can reliably estimate the strength of intrinsic and extrinsic noise and that does not require identical and independent pairs of

gene reporters?

In the context of this paper, extrinsic noise is assumed to be variations in parameters across cells; these variations are static and do not depend on time. The authors then proceed to answer question (i) by writing the observed distribution of transcripts as a compound distribution given by Equation 2 which takes as input the distribution of the telegraph model (that is analytically known in closed-form) – the underlying dynamics – and the distribution of parameters across a cellular population – the population heterogeneity. As summarized in Table I, they find that there are various different choices of these 2 distributions that can lead to the same compound (observed) distribution, thus highlighting the issue of non-identifiability if one only has available transcription abundance distributions. I note that the issue of non-identifiability is already known and described in the literature, however the authors identify some cases that were previously unknown. This framework is useful and the results are interesting; however the present formalism does not take into account some of the most important and ubiquitous sources of noise, namely those due to cell division (binomial partitioning of products upon division) and the cell-cycle (replication and cell-cycle length variability) because the authors use the conventional telegraph model that does not account for these phenomena – see Ref 38 where it is shown that these sources of noise can easily mimic that due to transcriptional bursting.

In the second part of the paper, the authors address question (ii). The dual reporter method of Swain et al. (Ref 4) is the standard method to decompose noise into its intrinsic and extrinsic contributions by using two independent reporter genes integrated into the same cell. The assumption that the reporters have identical dynamics is a strong one and presents difficulties in interpreting the results. Ham et al. present an alternative method which does not need dual reporters, rather makes use of 2 pieces of data (for e.g. mRNA and protein) belonging to the same biochemical pathway. The result is based on the decomposition of the covariance of any two variables according to the law of total covariance. This "pathway-reporter method" is shown to be accurate provided there is a small correlation between the reporter pairs – this is a strong assumption, in my view, and it is difficult to make a strong case for it generally. Also when carrying out verification of the method using synthetic data, the correlations between reporter pairs may strongly depend on the details of the model used. For e.g. nascent mRNA maturation to mRNA is in the present paper modeled via a one-step first-order process but more biologically faithful models (see for example PMID: 27667861 and 33976195) model this via a reaction step with a fixed time delay (modelling elongation + termination). The correlations calculated using the latter are likely stronger than the former because the former assumes exponentially distributed times. My main concern however is that the method presented is similar to another one described in the paper PMID: 22529351 which also uses the law of total covariance to understand how the variation in a species is determined by other species in the same pathway. There is also no comparison of the present method with another common one whereby the extrinsic noise is estimated as the part of the expression for the coefficient of variation that is not dependent on the mean molecule numbers; see for e.g. Ref 38 and Ref. 55 (Figure 2B).

Reviewer #1:

I found this paper very interesting to read and I think there is ample scope for the development of new methods in this field. Hence I am generally supportive of this paper.

My main concerns that I would like the authors to address, in order of importance, are:

(i) Novelty – is their method different than PMID: 22529351? They seem to be based on similar mathematical formalisms.

(ii) Nascent mRNA is more faithfully modeled using a delay step rather than a first-order step. Using the latter is approximative at best but will certainly decrease the correlations and maybe making your method perform pathway-reporter better than it would otherwise. The issue might be that the inclusion of such a delay step will lead to a non-Markovian model in which case I am not sure that the same mathematical steps follow

(iii) Cell-cycle and cell division effects are strong sources of noise and it would be ideal that these are at least discussed extensively; even better if they can be integrated into a modified telegraph model and then one can ask the same questions about what one can identify from a compound distribution based on Equation 2.

(iv) Discussion of their method vs the other method of obtaining the extrinsic noise from plots of the coefficient of variation squared versus molecule numbers.

(iv) The manuscript should be checked carefully as I found a number of grammatical mistakes scattered throughout.

Reviewer #2:

The paper deals, theoretically, with the question of decomposing noise into intrinsic and extrinsic components. This has previously been done primarily using the dual reporter method. Here, the authors suggest alternative methods that could in principle bypass the need for using two reporters.

I do not find the results very relevant from the biological perspective. The authors only verify their methods on stochastic simulations, where the model assumptions are specified by hand and thus fit perfectly into their theoretical framework. But how the proposed protocols would perform on experimental data remains unclear. The authors also seem unaware of recent work where essentially the same problem is addressed (Lin and Amir, PRL 2021) – inferring extrinsic vs. intrinsic noise from data – and a method not relying on dual reporters is tested on two existing experimental datasets. Related to the above, it was unclear to me precisely what sort of data would be needed in practice to implement their pathway-reporter method – and whether such data are currently available.

Another example of the potential discrepancy between mathematics and working with actual data is the authors' discussion of the identifiability problem. It seems to me that in reality distributions are always subject to noise (e.g. due to sampling errors) and it is unclear to me whether the sort of rigorous analysis they perform in the paper (that shows whether or not identifiability is possible or not in principle, assuming a perfectly measured distribution) is relevant at all to real data. (e.g.. even if two distributions are mathematically different, would it be possible to distinguish them in practice?)

It seems to me that the paper in its current format is a much better fit for specialized journals in biophysics/mathematics such as the biophysical journal or physical review.

Reviewer #3:

It is now well-known that single-cell expression data exhibits significant cell-to-cell heterogeneity, which can stem from both "extrinsic" factors (e.g. enzyme concentrations, energy content, cellular environment etc.) or "intrinsic" noise (e.g. firing of reactions). Ham et al. rigorously show how extrinsic factors can cause non-identifiability of a model from single time-point gene-expression data, and also lead to incorrect conclusions about the underlying process if they are excluded from the model. Then they propose a novel pathway reporter (PR) approach for quantifying the contributions of the extrinsic and the intrinsic factors to the overall cell-to-cell heterogeneity. These results are illustrated with examples based on the telegraph gene-expression model which includes both nascent and mature mRNA. While the developed results are interesting and mathematically accurate, they come with many caveats, and they do not present a significant advance over existing works on this topic. My reasons for this assessment are mentioned below:

1. Non-identifiability results: The observations regarding non-identifiability of the dynamic parameters from the compound distribution model are not surprising and even though specific examples in Table 1 are nicely worked out, I do not see how they contribute substantially to the existing knowledge on the subject. Essentially non-identifiability will hold for nearly all choices of tilde{p} and f, and identifiability, if it exists, is an exception rather than the norm. This is consistent with what the authors observed in the simulation study outlined at the end of page 10.

2. The Pathway Reporter (PR) scheme: The PR scheme is presented as an alternative to the dual reporter (DR) scheme. However PR also suffers from issues similar to the DR scheme:

– DR assumes conditional independence of reporters. Likewise, PR also requires that such an independence (at least at the level of covariance) in order to argue that the intrinsic noise contribution is zero in the reporter covariance. The paper establishes this approximately for certain parameter regimes by using analytical expressions for the steady-state covariances. However generally such neat expressions are not readily available. It is unclear how one can check that this expected covariance is small. Of course if a fully identified model is available, then one can check it with simulations, but then one can simply compute the extrinsic noise directly.

– Another critical assumption of the PR scheme is that the conditional expectation for the reporters given the extrinsic factors Z, should nicely separate into a function of the common parameters and a function of independent parameters. Even though this works for the specific linear gene-expression model considered in the paper, it is unclear if this would work more generally. Moreover having such a splitting is (up to an additional scaling factor) is not much more general than having identical conditional expectations, as needed by the DR approach.

3. Applicability to experimental studies: As the authors mention in the paper, it is difficult to experimentally construct reporters satisfying the conditions of the DR scheme. However the paper does not discuss how for unknown experimental systems one can identify/construct reporters that satisfy the conditions of the PR scheme. In light of my previous comment, this seems to be as challenging as the DR approach, if one does not have a well-characterized mathematical model.

4. Lack of a meaningful connection: There is very little connection between the two parts of the paper (non-identifiability and PR scheme). A more substantial connection is expected, as in the abstract it is said that: "Here we mathematically formalize this non-identifiability; but we also use this to identify how new experimental set-ups coupled to statistical noise decomposition can resolve this non-identifiability."

An example showing how noise decomposition helped turn a non-identifiable system into an identifiable one is lacking. Moreover, it is unclear how quantification of the extrinsic noise enables resolution of the challenging non-identifiability issue in the compound model.

5. All the results are presented for a specific gene-expression model and its derivatives. As the paper claims to provide a general approach for analyzing noise sources, more examples need to be provided, for a clearer evaluation of the PR method and comparison with the dual reporter method.

6. The paper only considers single time-point snapshot data measured at steady-state. What happens if multiple time-points, including the transience, is also taken into account. Certainly model identifiability would improve and the PR scheme should still work. The authors should consider such examples in the paper.

7. The description of the dual reporter method is misleading – at several places the paper says that the dual reporter method requires "independent gene-reporters". However only conditional independence is required by the method. If there is full independence, then the covariance (extrinsic noise) would always be zero.

8. On page 21, first paragraph it is mentioned that "For nascent-protein reporters, the normalized intrinsic contribution to the covariance is satisfactorily small (less than 0.05) for (a) high values of δp in unison with (b) low values of λ (less than 1, though lower values are acceptable if δp is small)". However based on the discussion prior/post this statement and also Figure 5, it seems that λ values should be high (not low!) for the normalized intrinsic contribution to the covariance to be small.
