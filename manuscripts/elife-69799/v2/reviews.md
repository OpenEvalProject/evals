# Peer review - Round 1

Editors:
- Adèle L Marston, https://ror.org/01nrxwf90 University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69799.sa0](https://doi.org/10.7554/eLife.69799.sa0)

The authors have developed a framework to quantify rates of chromosomal instability (CIN) in human tumors by fitting karyotype distributions inferred from low-depth DNA-sequencing to in silico models of CIN with karyotype selection pressures, sweeping through parameter space. This is particularly useful for the development of biomarkers for CIN, which is associated with cancer metastasis and drug resistance.


---

# Peer review - Round 1

Editors:
- Adèle L Marston, https://ror.org/01nrxwf90 University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69799.sa1](https://doi.org/10.7554/eLife.69799.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Quantifying chromosomal instability from intratumoral karyotype diversity using agent- based modeling and Bayesian inference" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Trevor A Graham (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Modelling.

Three different models to compute cell fitness based on karyotypic alteration are explored. The construction of all these models feels a little arbitrary, and the assumptions and evolutionary dynamics in each scenario should be more comprehensively explored. Specifically:

a) In the TOE model, fitness is inversely proportional to average ploidy, so it seems higher ploidies are always selected against. Is this a reasonable assumption? Why is it necessary to divide by the average ploidy?

b) In all models, is the simulated population always "out of equilibrium". If the simulations ran for longer would an "optimal karyotype" be established. Relatedly, the dynamics appear to be strongly influenced by the copy number >6 being lethal – chromosomes (in the TOE model) which are beneficial to be gained might tend to increase copy number to 5 whereas deleterious gains reduce copy number to 1 and the population rests on that "precipice". How reasonable are these "boundary conditions" and do the dynamics change significantly if they are relaxed?

c) Gains and losses appear to be treated equivalently – again is this reasonable? Especially in the TOE model where TSG gains and OG losses (and vice versa) have differing consequences. (see also point 8 below).

The modelling assumes exponential growth to a relatively small number of cells (4500) and then randomly kills half the cells to reinitiate exponential growth from 2500 cells. This regime will influence the evolutionary dynamics of the system: the random killing will cause emerging clones to often go extinct and could exacerbate the influence of drift in the system. It also effects the influence of selection, (see for example: https://www.nature.com/articles/ng.3214). Alternative growth dynamics could be implemented – such as a Wright Fisher type model of either constant or growing populations (for the construction of a growing WF see: https://pubmed.ncbi.nlm.nih.gov/25665006/) and the influence of the growth dynamics on karyotypic heterogeneity robustly assessed.

The modelling assumes only whole chromosome missegregations (and the bioinformatics data analysis averages over sub-chromsomal sized events). The authors could consider extending their analysis to handle part-chromosome events to better represent the biological data.

2. Bayesian inference.

It is a concern that unusual prior distributions are used in the ABC inference and this effects the reliability of the inference. Figure 5F and 6C show smoothed density plots for the prior distributions – which confusingly show density for S<0 – and the true priors might instead be a series of point masses at a handful of S values. This should be clarified.

It is likely that the posterior the alteration rate and S are interrelated (high S inferred when the alteration rate is high and vice versa) – so joint posteriors should be shown. Because of the interrelationship between the parameters, it is a concern that the current parameter estimates are inaccurate – currently the prior for S has zero mass for many S values, and the inferred value of the alteration rate will depend on which values of S are explored form the prior distribution. The inference should be repeated using continuous distribution over S, a uniform distribution is suggested.

When real data is analysed, only the hybrid model is compared to data, but their Figure 3 shows the diversity depends on the underlying model of selection. The authors should implement a model selection routine (one is available with the ABC-sysbio package: https://pubmed.ncbi.nlm.nih.gov/20591907/) to test which selection paradigm (if any) best represents the data. They could also consider comparing what is arguably the "null hypothesis" of neutral evolution (S=0) to a case with selection as part of this model selection, to quantitatively determine the evidence of selection in the data.

A single threshold for acceptance in the ABC algorithm (epsilon=0.05). The authors should show this is sufficiently small: a straightforward way is to plot the mean and variance of the posteriors as a function of epsilon.

Above, the possibility of temporal effects in the model are mentioned – how do temporal ("out of equilibrium" evolutionary dynamics) affect the inference?

When public data are analysed, the growth dynamics of the breast tissue, or colorectal organoid is very unlikely to match the exponential growth assumption that is assumed by the authors. These growth dynamics likely strongly determine the pattern of observed heterogeneity (exponential growth leads to large founder effects in the extant population) and so the influence of alterative growth models needs to be explored. This can also be done within a model selection framework.

The initial state of the model used to fit to public dataset is not specified and needs to be. The authors might also consider the influence of spatial sampling confounders (the breast dataset in particular in not a well-mixed population).

3. Single cell data analysis. The data are presented as if only whole chromosomal alterations occur (e.g. figure 5B). Is this actually the case? (certainly the assumption is false in breast and colon organoid datasets) Could relative read counts in say 1MB bins for each cell be provided in the appendix to reassure the reader that the types of genetic alterations occurring in their single cell data mirror the assumptions of the modelling.

As noted above, the authors should consider modelling part-chromosome alterations. They should be able to determine in their simulations how their assumption of only whole chromosome missegregation events, despite their being part-chromosomal copy number alterations in the data, affects the accuracy of the inferred chromosomal missegregation rate.

4. The presented framework is lacking expanded characterization and validation of selection models that are biologically relevant. The current framework simply applies a scalar exponent to already published fitness models for selection. It is unclear what this exponent mirrors biologically, beyond amplifying the selection pressures already explored in existing gene abundance and driver density models.

5. Related to point (4)., how is the CIN ON-OFF model in which CIN is turned off after so many cell divisions relevant biologically? Typically, CIN is a considered a trait that evolves later in cancer progression, that once tolerated, is ongoing and facilitates development of metastasis and drug resistance. A more relevant model to explore would be that of the effect of a whole genome duplication (WGD) event on population evolution, which is thought to facilitate tolerance of ensuing missegregation events (because reduce risk of nullisomy).

5. The authors utilize two models of karyotype fitness – a gene abundance model and driver density model – to evaluate impact of specific karyotypes on cellular fitness. They also include a hybrid model whose fitness effects are simply the average of these two models, which adds little value as only a weighted average. In silico results shows inferred missegregation rates are extremely disparate across the two primary models. And while a description of these differences is provided, the presented analyses do not make clear the most important question – which of these models is more clinically relevant? Toward this, in Figure 2F, the authors claim the three models approach a triploid state – which is unsupported by the in silico results. Clearly the driver model approaches a triploid state, as previously reported. But the abundance model does not and hybrid only slightly so, given that it is simply a weighted average of these two approaches. Because the authors have developed a Bayesian strategy for inferring which model parameters best fit observed data, it would be very useful to see which model best recapitulates karyotypes observed in cancer cell lines or patient materials.

6. Topological features of phylogenetic trees, while discriminatory, are largely dependent on accurate phylogenetic tree reconstruction. The latter requires more careful consideration of cell linkages beyond computing pairwise Euclidean distances and performing complete-linkage clustering. For example, a WGD event, would appear very far from its nearest cell ancestor in Euclidean space.

7. Experimental validation of the added selection exponential factor is imperative. Works have already shown models of karyotypic evolution without additional selection exponential coefficient can accurately recover rates of missegregation observed in human cell lines and cancers by fluorescent microscopy. Incorporation of this additional weight on selection pressure has not been demonstrated or validated experimentally. This would require experimental sampling of karyotypes longitudinally and is a critical piece of this manuscript's novelty.

8. It seems like this model treats chromosome gains and losses equivalently. Is this appropriate? Chromosome loss events are much more toxic than chromosome gain events – as evidenced by the fact that haploinsufficiency is widespread, and all autosomal monosomies are embryonically-lethal while many trisomies are compatible with birth and development. Can the authors consider a model in which losses exert a more significant fitness penalty that chromosome gains? (see also point 1c above).

9. Chromosomes do not missegregate at the same rate (PMID: 29898405). This point should be discussed, and, if feasible, incorporated into the authors' models.

10. Can the authors clarify their use of live cell imaging (e.g., in Figure 6G)? Certain apparent errors that are visible by live-cell imaging (like a lagging chromosome) can be resolved correctly and result in proper segregation. Is it appropriate to directly interfer missegregation rates as is done in this paper?

11. The authors should discuss in greater detail earlier mathematical models of CIN, including PMID: 26212324, 30204765, and 12446840. How does their approach improve on this prior work?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Quantifying chromosomal instability from intratumoral karyotype diversity using agent- based modeling and Bayesian inference" for further consideration by eLife. Your revised article has been evaluated by Anna Akhmanova (Senior Editor), Reviewing Editors and two of the original reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. The reviewers are concerned about the choice of statistics used for the ABC analysis. While these summary statistics indeed must contain some statistical signal on the rate of chromosomal instability, the current method of "phylogenetic reconstruction" which based on euclidian distances of chromosomal copy number variation is very indirect. The reviewers are not convinced that this is an optimal way to extract relevant information from the distribution of chromosomal copy number across cells. At least they are not clearly rooted in models of clonal evolution.

Why this particular set of summary statistics was chosen, how it relates to the quantity of interest (rate of chromosomal instability), how it compares to other possible ways to capture relevant information must be properly justified. The choice of these statistics should be explored in much more details in the manuscript with clear rationale given and caveats with this choice clearly stated.

2. Related to point 1 – The phylogenetic reconstruction is an unusual way to summarise the statistical data and has not been rigorously assessed. The authors should elaborate on the consequences of the possibly low accuracy of the tree reconstruction itself.

3. The manuscript is difficult to follow. For example, there is a lengthy part on validating simulations that doesn't have a very specific message and could be reduced quite a lot. Please also ensure that the manuscript narrative is accessible to the general readership of eLife, including defining specialist concepts, referring to figures (and figure supplements) in the order they appear in the text. Please also consider adding additional labels to the figures themselves to aid the reader and avoid over-simplification e.g. "Tet" "Dip" could be written in full, Figure 2D is missing a key etc.

4. More details are required on the ABC analysis, please address the additional comments of reviewer #3 below.

Reviewer #3 (Recommendations for the authors):

I focused my attention at looking at the revised ABC analysis.

I found the new analysis a little hard to follow.

It is not clear to me precisely what the "step windows" and sliding/expanding timesteps are in Fig6-S1&2. I couldn't see this explicitly explained in the methods. (I can see that the authors are trying to optimise the simulated number of cell divisions, I presume some kind of adaptive search was done)

I couldn't understand the rationale for only considering the mutation rate in these optimisations. I think that because stronger selection suppresses diversity, the strength of selection should inversely correlate with the time needed to evolve the diversity observed in the organoids.

I'm concerned about the posterior distributions shown in Figure 6-S3. In most cases the mass in the posteriors is at the extremes of the prior, which suggests that the true parameter values lie outside of the range of the prior (i.e. that the priors were too narrow). This problem appears always the case for the selection coefficient and appears to be a problem for the mutation rate in some cases too (at least it seems that the mutation rate cannot be distinguished from the boundary of 0). Possibly the same issue of a to narrow a prior applies to Figure 5F (taxol treated cell lines). The concern is that the data could be much better explained by a set of parameters located outside of the parameter space considered, which would mean that the conclusions could be incorrect.

Calculating posterior predictive distributions (analagous to Figure 6-S4&5) would help to convince the goodness of fit.

Line 479 says that a large-ish value of the acceptance threshold (epsilon=0.05) was used to retain prior data. This seems an incorrect statement: epsilon determines how many simulations are rejected but all prior data is always used. Smaller epsilons should give greater accuracy but at the cost of more computation.
