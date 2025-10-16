# Peer review - Round 1

Editors:
- David W Hawman, https://ror.org/043z4tv69 National Institute of Allergy and Infectious Diseases United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76071.sa0](https://doi.org/10.7554/eLife.76071.sa0)

The data presented here provide novel insight into the host response to CCHFV infection. These data further our understanding of how CCHFV causes disease in humans and will support the development of therapeutics to address the significant morbidity and mortality caused by this virus.


---

# Peer review - Round 1

Editors:
- David W Hawman, https://ror.org/043z4tv69 National Institute of Allergy and Infectious Diseases United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76071.sa1](https://doi.org/10.7554/eLife.76071.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Multi-omics insights into host-viral response and pathogenesis in Crimean-Congo Hemorrhagic Fever Viruses for novel therapeutic target" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Betty Diamond as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While reviewer 1 has mostly minor comments, reviewer 2 has several suggestions/requests for improving data analysis and conclusions. In particular, authors should address comments 2 and 4 from reviewer 2 along with providing more context on the pathways identified and any potential co-variates identified in the patients.

Reviewer #1:

In the manuscript by Neogi et al., the authors report data on RNAseq of PBMCs from CCHFV infected humans and proteomics analysis on CCHFV-infected cells. Interestingly, authors found that CCHFV-infection caused perturbations to metabolic pathways and also upregulated ISGs, consistent with a viral infection. Importantly, authors discuss their findings in the context of other viral infections to help readers understand how these pathways may influence CCHF pathogenesis. The use of longitudinal samples during acute disease and well after recovery is helpful to account for variability in human populations. These findings are significant as the human host-response to CCHFV is understudied and findings such as those presented here will help researchers using animal models determine the similarities and differences in these systems to human CCHF cases. The manuscript is well written and the extensive discussion helpful to understand the data. A limitation is their cohort had only one patient in the most severe disease group making conclusions on mechanisms that may mediate poor outcome difficult. Cumulatively, these findings add to our knowledge about how the human host responds to CCHFV infection, an area that warrants continued research.

Line 138-140 and 363-368: Do authors have data, e.g. ELISpot data, to show that patients did or did not develop T-cell responses to CCHFV?

Figure 4G: Do authors have cell viability data? Is decrease in CCHFV replication due to general decrease in cell viability?

Line 353 – 354: Authors should clarify that this statement is not based on CCHFV-specific data.

Line 211-212: Why was the extensively mouse passaged 10200 strain used? Would it not make more sense to use a Turkish CCHFV strain?

Line 214: An MOI of 1 via a poisson distribution would infect 63% of cells which would leave few uninfected cells for a second round of infection and little to no cells for a third round.

Line 467: In our experience, SW13s take 3 – 4 days to show cytopathic effect upon infection. Did authors observe CPE by 48 HPI?

Figure 1B: I would recommend authors use colors other than red and green to make figure more accessible to color-blind readers.

Line 403 – 405: What is the feasibility of targeting host metabolism as a host-directed therapy? Have therapies along these lines been evaluated pre-clinically or clinically for viral infections? Would it not be expected that targeting this pathway, an essential component to cell viability, would result in substantial negative effects on the host?

Reviewer #2:

The manuscript by Neogi, U. et al., provides analysis of the circulating immune responses to CCHFV infections in patients. To my knowledge, this is a truly unique dataset as it represents one of the first analysis of the circulating response in patient samples. The authors then further characterize the immune response using in vitro proteomics to isolate pathways associated with glycolysis that could serve as therapeutic targets and provide preliminary evidence that these pathways are important for the virus to replicate in cell lines. Some of the strengths of the manuscript are providing a resource for other to investigate host responses to CCHFV, detailed information on patient samples for further investigation into factors such as sex and age on the host response to CCHFV infections and provides a proof of concept for utilization of the information for potential therapeutics. The paper does rely too heavily on methods, such as WGCNA, whose results can be easily biased in datasets with high variance and low n, such as with patient data. Additionally, more context on the pathways provided beyond their identification is needed. Finally, assessment on how any potential co-variates identified in the patients may bias the results is needed to isolate pathways altered by the host response to the infection.

Specific recommendations that would strengthen the manuscript are listed below.

1. In the Results section on sample collection and clinical data, it would be useful to have a quick note about the clinical severity scores, how they are calculated (is it a standard sheet, is it the same individual scoring all patients, are there any potential biases in the scoring?). It would also be useful to have a visual of the distribution of the clinical severity scores to help put them into context for the reader. Especially since they are utilized so heavily, there was just not a lot of context for these values.

2. The authors use a whole multitude of different p-value cutoffs for significance. There should be a justification for each cutoff being used. For example, on line 144 the authors state that for the metabolite profiling, a adj. p < 0.1 was used but for the DGE an adjust p-value of 0.05 was used. Have the authors done prior work to determine the optimal cutoffs for each of these analysises? If so, that should be included. If not, there needs to be a justification for each set of p-values analyzed.

3. The IFN signature is not surprising and is a common feature in patients that present with severe viral infections. Additionally, this was predicted from NHP data (see Arnold, CE. et al., Scientific Reports 2021). However, the authors could provide a greater context to the IFN and ISG signatures. What percent of the ISGs are attributed to Type I vs. Type II IFN? This is especially important given the NK/Th17 type responses that are detected.

4. WGCNA analysis should always be done with caution when using samples that have high variance (such as patient data) and/or a now n (only 12 samples in this case). Additionally, there is no assessment on co-variate assessment and how factors such as age, sex, clinical score, days since symptom onset, ect. could have affected these results. This is particularly important in-patient data where all of these variables cannot be controlled.

5. For the proteomics data from the cell lines, it would be good to also know what the clustering looks like with the virus removed to help prevent biases caused by differing viral loads.

6. Additionally for the proteomics data, have the authors done an assessment of the viral load? Based on the IF, they are potentially past the exponential growth phase. If this is the case, data collected during the exponential growth phase would be useful to know what pathways are needed for early replication. Growth curve analysis would also help put this into context.

7. For all the UMAP analysis, how many features were used in the UMAP calculation and was a preliminary dimensionality reduction used first?

8. From the sequencing data, it would be great if the authors could perform cellular deconvolution on the samples as well to determine if there is likely changes in cell types causing changes in gene expression. This would be helpful for the NK/Th17 type responses detected but also the reduction in HLA genes.

9. How are the other identified genes sets related to viral load. There was an assessment of ISGs to viral load which showed the expected pattern. It would interesting to know which other gene sets correlate strongly with viral load and particularly ones that seem to not be as linked to viral load. Correlation analysis of gene modules would provide much greater context to the identified gene sets.
