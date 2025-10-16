# Peer review - Round 1

Editors:
- Martin Taylor, https://ror.org/01nrxwf90 University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67790.sa0](https://doi.org/10.7554/eLife.67790.sa0)

This is an important paper that shows most cancers unavoidably accumulate damaging mutations. Whilst the majority of claims are convincingly supported by the data, evidence that damaging changes are buffered by heat shock pathways is currently incomplete. The insights into selection efficiency are important for the understanding of cancer growth and response to therapy. A broader implication is that high mutation load tumors may use common strategies to tolerate accumulated deleterious mutations, providing a therapeutic target.


---

# Peer review - Round 1

Editors:
- Martin Taylor, https://ror.org/01nrxwf90 University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67790.sa1](https://doi.org/10.7554/eLife.67790.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Most cancers carry a substantial deleterious load due to Hill-Robertson interference" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Martin Taylor as the Reviewing Editor and Reviewer #3, and the evaluation has been overseen by Molly Przeworski as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Elena Kuzmin (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

(1) The authors state that they are excluding tumors with either nonsynonymous(n)=0 or synonymous(s)=0 mutations. Since nonsynonymous and synonymous variants occur in a ratio of about 3:1, this exclusion of tumors would seem to lead to an inflation of the signal of selection in the first (lowest mutation) bins. Additional demonstration is required to show if this distorts the estimate of selection for low mutation burden tumours. For example, by adding pseudo-counts of mutations or by aggregation over tumours in the same mutation load "bin" as was performed for some analyses.

(2) The decline of dN/dS on driver genes is the subject of the supplementary text and we note the efforts taken to disentangle Hill-Robertson interference effects from other possible explanations for dN/dS decay in drivers with increasing tumor mutation burden (TMB). Driver genes can be quite tissue-specific (and thus mus-identified for a tumor) and number of drivers per tumour estimated to span approximately 1 to 10 (Martincorena et al., 2017). Consequently, the fitting of a single set of model parameters and showing they do not match well the observed data (Supplementary note figure) is insufficient to exclude the misidentification of driver genes, or presence of nonsynonymous-neutral mutations in annotated driver genes, as an explanation for the decline in dN/dS with increased TMB. We think it important that a range of justifiable parameters are applied in this modelling, to test if the observed data is robustly outside reasonable parametrisation of the model.

(3) In many figures that show dN/dS as a function of n+s (starting with Figure 2A and extending to Figures S2, 3, 9, 10, 12, 22 and 25), there are no error bars indicated, as opposed to the statement in the figure caption. The error bars/shading should be shown. In Figure 2A, is the observed depletion in the second bin still significant?

Reviewer #1 (Recommendations for the authors):

1. Figure panels should be called out sequentially. For example, Figure 2G is called out before Figure 2D. This happens throughout the text, including main and supplementary figures, and should be corrected.

2. Figure 2G shows that mean gene expression of genes encoding chaperones and the proteasome increases with increasing mutational burden. What about protein abundance? Is this in agreement with gene expression?

3. Figure 2 mentions error bars in the figure legend, but no panel displays error bars. This is also true for Figure S13 and other figures. Authors should display the error bars to which they are referring to make their analysis more convincing.

4. Pg. 9 line 295 describes results of the analysis across genes belonging to different GO terms. However, Figure S13 only shows 3 categories: chromosome segregation, transcription and translation. How were these categories chosen? What about other categories? Such cherry picking doesn't convincingly support the conclusions that no specific GO functions are enriched. Also, translational regulation shows higher dN/dS in low mutation tumors suggesting that there is positive selection for passengers in this category. Authors should discuss in their manuscript why this is the case.

5. Figure S15 shows the attenuation in selection of CNAs across cancer subtypes and broad cancer groups. However, HNSC and kidney cancer appear to be the exceptions. Authors should provide an explanation for these observations in the main text.

6. Generally, copy number variations are considered to be > 50 bp. Is there a rationale as to why authors chose 100 kb to be their cut-off in Figure 2C? If the size of CNA is an important parameter, then authors should explain why that is.

7. Non-allelic recombination and non-homologous recombination mechanisms involving replication accidents that lead to chromosome breakage occur with some frequency in somatic cells. How does the frequency of these events impact the selection efficiency in cancer as it relates to drivers and passengers? Can this also be incorporated in their evolutionary model?

8. Authors mentioned that haploinsufficiency was not used in the model. What about loss of heterozygosity which is extensive in cancer genomes? Can this parameter be included in the evolutionary model and how would it impact the results?

Reviewer #2 (Recommendations for the authors):

1. The authors have taken great care to study single-nucleotide variants and large CNAs. It would be great if they could confirm their findings by also showing the effect on small insertions and deletions.

2. Figure S5 is showing a bias in the determination of dN/dS from simulation results and the correlation between mutation rate and n+s. I am not sure I understand why dN/dS under a neutral simulation would be biased. Also, the low median correlation between n+s and the mutation rate (<0.4) is quite surprising. I would have expected these to be almost perfectly correlated. Likewise, I do not understand the formula after l. 631. It states that this is the joint density of the two Poisson random variables that denote nonsynonymous and synonymous mutation count, yet there is an additional unexplained factor in the denominator, which corresponds to the probability of s>0. If the simulation that underlies Figure S5 was also used in the ABC-based parameter inference, this would raise a serious cause for concern.

3. The simulation starts when the first mutation with positive selective effect initiates population growth, which can be very late in a patient's life. How does the assumption that up to 100 years can pass after this affect the parameter estimates?

4. To which extent does the inferred distribution of selection effects depend on the allowable parameter range? For example, s_passengers extends beyond the initially allowable range after the fit (Figure 3C).

5. It is not entirely clear to me how the partitioning of the likelihood between Muller's ratchet and hitchhiking vs other effects can be made and how robust these inferences are with respect to variation of the modeling assumptions (e.g. about initial population size or mode of selection). Is the necessity of inclusion of selected synonymous variants on driver genes a robust result or not, taking into account the discussion on p. 26f.?

6. In Figure S4, the authors report the correlation of n+s with other measures of tumor mutation load. Given the relative sizes of the different regions that are displayed, i.e. whole genome:intergenic:intronic:exonic:protein-coding, of roughly 100:60:40:2:1, the displayed numbers do not make sense, as their ratios are 100:100:100:1:0.001.

7. I am not sure I understood well how CNAs were analyzed. Based on the description in l. 669ff., it appears that putative cancer driver genes were identified from the CNA data based on recurrence. Were the same data then analyzed for CNAs falling into said putative cancer driver gene regions to infer selection? This would appear a bit circular.

8. I do not understand the formula shown after li. 738. It appears it is showing the fraction of genes that intersect a CNA boundary, summed over all tumors in a given n+s bin. Each CNA can be counted twice if both of its boundaries fall into a gene. Why is the mean value of this 1?

9. In all figures that show dN/dS as a function of n+s (starting with Figure 2A and extending to Figures S2, 3, 9, 10, 12, 22 and 25), there are no error bars indicated, as opposed to the statement in the figure caption. In Figure 2A, is the observed depletion in the second bin still significant?

10. In l. 290, I understand that the authors argue that differential dominance effects between heterozygous early- and late-arising mutations could be affecting the efficacy of selection on subclonal variants compared to clonal variants. I do not see this claim well motivated or corroborated.

11. In Figure 2D, the caption states that mutations have been separated into two groups by their clonality, yet the figure shows three curves. What do they correspond to? Are the results still significant given the partitioning of the mutation data into smaller subsets?

12. Figure 3 does not have a panel G.

Reviewer #3 (Recommendations for the authors):

I enjoyed reading the manuscript, it was well written, generally clear figures and very through provoking.

Only a small number of specific points to address:

Line 60.- The description of dN and dS here along with the interpretation of dN/dS=1 as neutral implies that you are just counting non-synonymous and synonymous mutations and dividing one by the other. This of course is not the case. Perhaps dN and dS could be described as rates or dN/dS as the dN:dS odds ratio which is how it's calculated for your permutation metric.

Line 112 – 40% of what, benefit of ~130% of what. This becomes apparent later into the manuscript but not clear how to interpret when reading at this point for the first time.

Line 188 – Mutational burden <= 3 (what units).

Line 189 – "We observed little negative selection in passengers" be clear what passengers (previous identified passenger genes).

Line 252 – Panel G, y-axis, what units? Why are "all" genes uniformly at approximately -0.2? Assuming this is fold-change or log-fold-change I'd expect 1 or zero respectively.

Line 275 – Figure 2G, shaded error bars are not visible.
