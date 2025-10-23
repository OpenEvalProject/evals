# Author response - Round 1

Authors:
- Benny Borremans ([ORCID: 0000-0002-7779-4107](https://orcid.org/0000-0002-7779-4107))
- Amandine Gamble
- KC Prager ([ORCID: 0000-0003-0669-0754](https://orcid.org/0000-0003-0669-0754))
- Sarah K Helman
- Abby M McClain ([ORCID: 0000-0001-5000-4198](https://orcid.org/0000-0001-5000-4198))
- Caitlin Cox
- Van Savage
- James O Lloyd-Smith ([ORCID: 0000-0001-7941-502X](https://orcid.org/0000-0001-7941-502X))

## Response text

DOI: [10.7554/eLife.60122.sa2](https://doi.org/10.7554/eLife.60122.sa2)

Essential revisions:

1) Reporting of the review component: This paper is missing some reporting elements that are usual in reviews of the literature and required for full transparency. Please provide: a) the full electronic search strategy for at least one database in appendix, with search terms used; b) a flowchart of the study selection process, with inclusions and exclusions; c) a summary table of all included studies, providing an overview of their main characteristics (ex. assay, antigen, countries, age range of participants, sample sizes, and maximum follow-up times) ; d) the full list of citations of all included studies. While this paper is not a formal systematic review, some guidance on how to present the elements listed above can be found in the PRISMA guidelines.

We agree that more information about the selection process would be valuable, and have added all information as suggested (subsection “Estimating the distribution of seroconversion times”). We have also added a flowchart (Figure 5) and a table listing the key features of the selected articles (Figure 5—source data 1).

2) Chain convergence: Looking at the plots in the supplementary information, the MCMC chains have not converged. This means that the results on the fitting of antibody levels cannot be reliably interpreted and casts doubt on the validity of estimates from these analyses. There are several individuals for which we observe very poor fits. Perhaps visualizing the uncertainty in the model estimates of antibody levels would clarify. The chains need to be run again. Calculation of the Gelman-Rubin convergence statistic would provide evidence of chain convergence. The reviewers recommend running the chains for longer and re-tuning the proposal distributions in order to achieve chain convergence.

We fully agree, and have re-done all MCMC fitting using a better method (JAGS instead of R Metropolis-Hastings MCMC).

Chains for all parameters now converge nicely, with clean posterior distributions.

Additionally, the much improved model fits have motivated us to improve parameter estimation by implementing individual growth rates (as opposed to one population-level growth rate previously).

These improvements did not change any qualitative results, and now allowed all statistical comparisons of model parameters to be done fully based on posterior distributions that take into account parameter uncertainty.

These changes resulted in the following edits in the main text and supplementary information:

– Updated description of MCMC model fitting in the main text.

– Updated antibody kinetics results in the main text

– Updated MCMC results in Figure 3—figure supplements 1-10.

Unfortunately a bug was found in the code in the process of improving the models, which previously resulted in wrong subsetting of IgM results of mild cases.

As a result, we now find a marginally significant difference in IgM antibody level growth rates and peak level timing between mild and severe cases.

This did not have a major impact on the overall conclusions however, as the difference was not large, and seroconversion as well as antibody detection patterns that are based on much larger datasets do not provide evidence for a general effect of disease severity on antibody patterns.

We edited the relevant section in the Discussion accordingly: "Here, we did not detect any significant effects of disease severity on antibody patterns, with the single exception that we estimated a lower rate of IgM increase in severe/critical cases relative to mild/moderate cases", and "Our findings do not support the idea that severe cases seroconvert faster. Indeed, the only significant effect of severity in our analyses is that the inferred growth rate of IgM levels is slower for severe/critical cases. It is not clear whether this reflects a relevant biological difference, considering that all other parameters do not differ among disease severity categories. The consensus patterns from our meta-analysis suggest that any interaction between disease severity and antibody response must be subtle and sensitive to other sources of variation, explaining the inconsistencies seen across studies".
