# Peer review - Round 1

Editors:
- Leendert Van Maanen, University of Amsterdam Netherlands

Reviewers:
- Leendert Van Maanen, University of Amsterdam Netherlands

## Review text

DOI: [10.7554/eLife.42607.024](https://doi.org/10.7554/eLife.42607.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Leave-One-Trial-Out (LOTO): A general approach to link single-trial parameters of cognitive models to neural data" for consideration by eLife. Your article has been reviewed by Michael Frank as the Senior Editor, a Reviewing Editor, and two reviewers.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Both of the reviewers appreciate the importance of readily available methods to estimate single-trial values of computational model parameters. We feel that there is much to like about the current approach, but there are some concerns, that I have compressed into a single list of points below.

Summary:

The authors discuss a leave-one-out method to estimate trial-by-trial variability in parameters of computational models (LOTO). The rationale is that the deviation between a model parameter that is estimated using all data and a model parameter that is estimated using all data minus one data point, reflects the influence of that one data point. The authors demonstrate that LOTO is relatively easy to implement and faster with respect to previous approaches, and importantly it can be easily demonstrated via simulations whether the adopted approach is falsifiable.

Essential revisions:

1) An important issue with the current version of the paper is that in subsection “Comparison of LOTO with related approaches”, a comparison with the more complex, but presumably superior method of joint modeling (Turner et al.) is not performed. It would be good to see how much information about the single trial parameter estimates is really lost when not accounting for the covariance structure as Turner proposes.

2) A substantial concern about the utility of the approach and the interpretation of the results obtained by LOTO comes from the fact that recent evidence indicates that a good proportion of trial to trial fluctuations comes from inference processes of the incoming signals or subsequent computations (for emerging evidence see e.g., Drugowitsch et al., 2016; Findling et al., 2018; Polania et al., 2018). This suggests, that for instance, in the case of the HD example given by the authors, fluctuations can come directly from encoding di or xi or even from performing the computation (xi /(1+κ*di)) but not necessarily from κ.. This means that variability in behavior can be misattributed to a given parameter (and therefore misattributed to a brain region when applied to neural data), but the sources of fluctuations may potentially come from encoding/decoding processes of input-signals/computations as indicated by recent research. Is there a way that the authors can rule out or study this possibility? For the case of the HD model, I assume that this might be difficult as the denominator in Equation 6 contains κ*di, but it could be that this is dissociable as uj does not depend on κ (at least in some way as this implies d=0). Is there a way that the authors can come up with a paradigm, experiment or analyses to resolve this issue? If this is the case, this is an approach that could significantly advance the current state of the art in the field. The authors would need to convincingly demonstrate that this is the case.

3) The "toy" example based on the binomial model can be illustrative, it can also be confusing if some clarifications are not done from the beginning. From the moment the authors started to argue that LOTO can be used to detect trial to trial fluctuations on θ, it was clear to me that it was impossible to dissociate trial to trial fluctuations in k and θ. The explanation that this is the case comes only in the last paragraph of the subsection. I am not exactly sure what would be the best way to deal with this, but perhaps this issue about LOTO can be mentioned before the authors dive into applying LOTO to this example. Moreover, this is an issue that the authors might want to emphasize in the Discussion by explicitly describing what is or what is not possible with LOTO and giving some recommendations in this respect.

4) The usual approach when modelling trial-to-trial fluctuations for a given parameter is to assume some parametrization (e.g. uniform distribution for the starting evidence or Gaussian distribution for drift rate, or sometimes a Gamma distribution for precision parameters). While the correlations between LOTO recovered and true values is rather high in general, it would be interesting to see whether the distribution of the parameters recovered by LOTO match the shape of the generating distribution. If yes, great; if not, why not?

5) In subsection “An example of using LOTO for model-based fMRI”, the authors argue that the neuroimaging effects were "even stronger than those reported in the original publication". These statements have to be backed up via quantitative analyses. Given that the authors are performing their analysis based on the SPM framework, a direct way to test this is via the Bayesian model comparison module. In this way one could understand how much stronger a given activation pattern is better explained by one model or the other. Please provide the statistical maps of these analyses.

6) In the LOTO analyses for subsection “An example of using LOTO for model-based fMRI” (reported in Appendix D), σ could have been included as a potential source of trial-to-trial fluctuations. Why was this not the case? If σ does not change from trial to trial, then one should see this from the null distribution analyses on potential improvement of deviance. If this is the case, then how are the neuroimaging results affected?
