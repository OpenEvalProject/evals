# Author response - Round 1

Authors:
- Andrew K Lawton ([ORCID: 0000-0001-8633-6637](https://orcid.org/0000-0001-8633-6637))
- Tyler Engstrom
- Daniel Rohrbach
- Masaaki Omura
- Daniel H Turnbull
- Jonathan Mamou
- Teng Zhang
- J M Schwarz
- Alexandra L Joyner ([ORCID: 0000-0001-7090-9605](https://orcid.org/0000-0001-7090-9605))

## Response text

DOI: [10.7554/eLife.45019.022](https://doi.org/10.7554/eLife.45019.022)

Essential revisions:

One of the reviewers is concerned that in the model the missing two parameters mμ/kr are constrained to scale linearly in time. There must be a second constraint to fix two parameters. The motivation behind linear scaling and the full choice of parameters should be more transparent.

We thank the reviewer for their comment on the parameterization of the model as it gives us a chance to clarify our approach. In the modeling community, it is quickly becoming the norm to reformulate a model in terms of dimensionless quantities, i.e. nondimensionalization. To do so, one works with dimensionless ratios of the parameters, thereby reducing the number of parameters to uncover a smaller set of quantities that the system depends on. In the manuscript, we also work with a nondimensionalized form of the model (i.e., we work in units where r0=1), and so only 5 dimensionless parameters are required to completely specify the model. These may be chosen as μ/kr, kr/kt, At/r0, t0/r0, and q, as discussed in the Materials and methods section entitled “Details of Multi-phase model […]”. Thus, the quantity μ/kr should not be thought of as a ratio of two independent parameters, but rather a single dimensionless parameter. We indeed should have been more transparent about using the nondimensionalized version of the model, and we thank the reviewer for pointing out this oversight. The revised manuscript has language added to the section "Details of multi-phase model […]" to state explicitly that the nondimensionalized model is used to make the plots in Figure 6B-C as follows:

“Because we are primarily interested in shape changes, rather than size changes, a nondimensionalized model solution was used, i.e., we chose units where r0=1. This reduces the total number of parameters specifying the model to five dimensionless parameters.”

In re-reading this section, we also noticed a typo that may have been the source of some of the confusion. The fifth paragraph said "Figure 5F" where it should say "Figure 6B-C". We apologize for this typo, we have fixed it in the revised manuscript, and hope this clarifies how the parameters in Figure 6B-C are chosen.

Regarding time-dependence, the model parameter μ/kr should be increasing over time because kr is decreasing over time, which we suggest in the Discussion can be attributed to the radial glia transitioning to Bergmann glia (see, e.g., Discussion, third paragraph). We assume linear scaling, because that is the simplest possible kind of scaling. That this is an assumption stated in both the legend to Figure 6 and in the section "Details of multi-phase model […]". Having said that, Figure 6C illustrates that this assumption is not too unreasonable, at least concerning the agreement of the experimental and theoretical shape index.
