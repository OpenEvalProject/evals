# Peer review - Round 1

Editors:
- Lynn M Hassman, https://ror.org/01yc7t268 Washington University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74913.sa0](https://doi.org/10.7554/eLife.74913.sa0)

These findings are valuable to ocular immunologists who the study pathophysiologic mechanisms driving inflammation in human uveitis, and for future identification of novel therapeutic targets. The authors convincingly perform high dimensional multi-omic analysis of testing and replication cohorts, followed by characterization of a disease-specific cell type using comparative analysis with previously validated experimental datasets. The analysis will be of particular interest to basic and translational ocular immunologists, as well as dendritic cell biologists.


---

# Peer review - Round 1

Editors:
- Lynn M Hassman, https://ror.org/01yc7t268 Washington University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74913.sa1](https://doi.org/10.7554/eLife.74913.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Whole transcriptome-sequencing and network analysis of CD1c+ human dendritic cells identifies cytokine-secreting subsets linked to type I IFN-negative autoimmunity to the eye" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Betty Diamond as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: James Walsh (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Improved informatics analysis to correct for false discovery and stronger correlation with intra-ocular cDC2s, per reviewer #3

2) Revision of claims to have identified a new type of cDC2, reframed to fit this cell state into the current, more rigorously defined, classification of cDC2 subtypes (authors have already cited key papers). This analysis may also benefit from stronger analysis of the transcriptional profile of intraocular (ie tissue state) CD36/CX3CR1+ cDC2s. Conclusions must be tempered given concerns of reviewers #1 and #2

Also, please correct number of references, it was at times impossible to determine which sources were being cited.

Reviewer #1 (Recommendations for the authors):

It is unclear why the CD14 is plotted vs CD3 in Figure 1F.

Line 166: Repeated word "co-expressed expressed".

Line 247: Run on sentence (and used multiple times).

Line 384: "No minimize bias" needs to be corrected.

Reviewer #2 (Recommendations for the authors):

Specific comments:

An issue is that the cd1c+ cells used for RNAseq were isolated using microbeads which is extremely impure. What other cells contaminated the prep, can the gene expression be reliably de-convoluted? What is the cell purity prior to RNAseq?

5B and D how many patients are displayed? Patient numbers should be shown for each figure throughout the manuscript.

Phenotype of the DCs should be shown in the presence of Notch2 and ADAM10 inhibitor? Is the DC3 reduced? CX3CR1, CD36, ccr2 CD163?

What is the output of the CX3CR1, CD36, ccr2 CD163 DC3 in Notch ligand-conditioing human CD34 HPC derived DCS?

Functional analysis for understanding T cell priming by the new DC3 subsets should be shown. what is the implication of the results for autoimmune Uveitis.

Technical details that should be addressed:

– All versions of the software should be noted in the methods section, for example ConsensusClusterPlus, Deseq2, WGCNA, etc

– For logicleTransform – were the default settings used or were the parameters altered, this needs to be indicated for interpretation of the log linear transformation.

– Heatmap color palettes are not ideal for colorblind readers, would recommend using viridis palettes

– For the differential gene expression and generation of weighted gene co-expression networks, why was the raw p-value used as a cut-off and not adjusted p-value? Was there any controls for possible false positives?

– For the FlowSOM clusters – what are the approximate sizes Cluster 81, 41, 61, and 83? What percent of the peripheral blood? What is the relative proportion of these clusters in Uveitis vs control?

Author should cite Korenfeld at al JCI insight 2017 on page 9

Reviewer #3 (Recommendations for the authors):

In general, figure panels should be made larger; several -- particularly in Figure 3 -- have panels that are nearly unreadable even when printed at full-page scale.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Transcriptome network analysis of human CD1c+ dendritic cells identifies an inflammatory cytokine-secreting subpopulation within the CD14+ DC3s that accumulates locally in type I IFN-negative autoimmunity to the eye" for further consideration by eLife. Your revised article has been evaluated by Betty Diamond (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The authors utilized deep transcriptional profiling of isolated CD1c+ peripheral blood cells to identify a peripheral blood biomarker of uveitis, followed by flow cytometric analysis of protein expression to test the hypothesis that a subset of CD1c+ cells are reduced in uveitis patients. Identification of peripheral blood biomarkers of uveitis is important and their study is based on analysis of a reasonable number of study subjects with active disease, therefore the data supporting the first conclusion that a differential gene expression profile exists in uveitis is well-supported and convincing. The subsequent analysis which attempts to define and new cell type based on comparison with published expression datasets, while hypothesis-generating, is inadequate, as sufficient phenotypic and functional analyses were not performed to reach their conclusions. Similarly, the comparison with genes expressed by ocular CD1c+ cells from a separate dataset is not sufficient to conclude that the peripheral blood CD1c+ cells migrate into the eye.

Reviewer #1 (Recommendations for the authors):

The authors have addressed many of the concerns in the original reviews, and while the discovery of a subpopulation of blood-derived DCs that are changed in uveitis would be interesting the revision does not leave me convinced that this is truly a unique population of cells. Specifically the flow cytometry data in Figure 5/supplement suggests that the CD14 population is derived from a population that is bisected by the original gate, rather than from a population of CD1c+ DCs limiting functional analysis, and the scRNA seq does not show that the cells expressing black module genes are distinct from those that don't.

Reviewer #2 (Recommendations for the authors):

The authors set out to utilize advance informatics techniques to advance our understanding of a cell type previously shown to play a role in uveitis, type 2 conventional dendritic cells (previously termed mDC1). They accumulated a valuable set of samples from untreated, active disease and employed a testing and validation cohort which reproduced a core set of genes differentially expressed within the CD1c+ dendritic cells in the peripheral blood of patients with uveitis. Importantly these cells appear altered regardless of the subtype of uveitis. They then astutely question whether the transcriptional signature simply represents different proportions of cell subtypes or states and test this hypothesis using flow cytometry.

They also attempt to probe the mechanism driving this particular cell type/state by cleverly drawing on published data sets, however these hypothesis-generating experiments are not validated experimentally in a uveitis system.

They utilize in vitro analysis of similar cells isolated from human patients and show that the cells can be induced to make a specific set of cytokines which is different from a related dendritic cell type, however the lack of concordance with published activated DC2s, or the transcriptional signature in their own ex vivo activated DC2s raises more questions than it answers.

The manuscript was difficult to read, largely because it is trying to accomplish too many goals, but also because the informatics techniques and external data sets were not described sufficiently for an average reader to readily evaluate the method and conclusions, and the conclusions were overstated throughout the paper. Overall, too many hypotheses were tested, alternative hypotheses were not considered/discussed. The data should probably be divided into at least 2 papers, one which explores the peripheral blood subsets more concretely, and one which attempts to elucidate a mechanisms by which low RUNX3 expression is associated with the genes expressed more highly in DC2s in the peripheral blood of uveitis patients.

1. The rationale for depleting CD14 in the validation cohort is not clear and justified. CD14 expression on dendritic cells has been established in the literature (ex Duterte Immunity 2019). This reviewer wonders if a better flow of data would be to start with the current second cohort, CD14 depleted, ID the black module, realize that some genes discovered have been associated with CD14+DC3, then utilize a second cohort that includes CD14+CD1c+ cells to validate and expand the original gene set.

2. Experiments probing the transcriptional regulation of the uveitis-enriched gene set are not definitive, but hypothesis-generating, and left in this story, are distracting from the primary observation of a cell type differentially present in the blood of uveitis patients.

3. The authors claim to have found an inflammatory cell type, but the gene expression profile does not recapitulate inflammation-induced DC2 gene expression profile. Figure 3 attempts to shed mechanistic light but only opens more questions, like if viral infection in mice (figure 3A lower panel) and multiple inflammatory stimuli (figure 3C) induce a transcriptional program opposite what they are finding in these cells in the peripheral blood of uveitis patients, how are the cells identified in this paper likely relevant to eye inflammation?

4. Pro-inflammatory CD14+DC3 increased in blood in SLE patients, but according to authors interpretation, they find a similar cell type is decreased in peripheral blood in uveitis. The authors adhere to a possible explanation that these cells are trafficking to the eye, but by the same logic, SLE patients should have an even more significant reduction, not increase in their peripheral DC3 counts. This is not discussed.

5. Even more importantly, the Chen et al. papers which are cited generally by the authors, showed the opposite- that CD1c+ DCs are increased in the blood of patients with uveitis, and correlate with disease activity. No attempt is made by the authors to compare their data with this data derived from a larger number of patients, or discuss the difference. The authors have essentially ignored this key discrepancy with previously published data.

6. Despite changing some text around the hypothesis that this cell type is reduced in the blood because it migrates to the eye (numerically impossible as pointed out by prior reviewer #1), this notion is reiterated several other places in the paper and should be removed, and frankly, reconsidered. It is also possible that the change in peripheral blood cell type/state frequency results from cytokine-induced precursor emigration/differentiation. Perhaps there is actually a fraction of DC2-type cells that are increased in the blood in uveitis (as Chen found) but express the transcriptional program identified in the paper because they are pre-activated cells?

7. The analysis of ocular DC2s which concludes that the current cell type, CD14+DC3s with black module gene expression, are present in the eye is not convincing. The methods are not clearly explained, however it appears that rather than utilizing unbiased cluster analysis and performing differential gene expression analysis between the patients with non-infectious uveitis, and the control (endophthalmitis), or using another technique like GSEA which they used in previous figures to correlate the black module genes with the genes expressed by the ocular DC2s, the authors appear to have selected individual cells that expressed the black modules genes, then compared the expression of black module genes to the cells that did not express black module genes.

8. The authors state in their response to reviewer #1 comments "we profiled available eye fluid biopsies and paired plasma by Olink proteomics to measure immune mediators from patients and controls from this study (and several additional samples, including aqueous humor from non-inflammatory cataract controls – see revised Figure 5 panel D). This analysis shows that cytokines produced by CD36+CX3CR1+ DCs such as TNF-α and IL-6 are specifically increased in eye tissue of patients, but not in blood."-Neither this data, or discussion of it are included in the revised manuscript.

Finally, a concern is that the title is a gross overstatement of their findings:

1. They have not demonstrated that the cells in this paper induce inflammation, and especially not in the context of uveitis- only that similar cells from healthy patients produce a different set of cytokines when stimulated in vitro compared to another cell type.

2. They have not demonstrated that these very cells migrate to the eye, only that similar genes are present in a possibly similar ocular cell type in another data set.

3. They do not demonstrate type I IFN-negative autoimmunity in the eye. This was a huge stretch, presumably from prior assumptions about the mechanisms driving uveitis along with the finding that their cell type does not share a transcriptional program with murine DC2s activated in a viral infection.

In regard to addressing the Previous Editor Concerns:

1. The informatics analysis for most of the paper is likely sufficient, however the methods are not communicated succinctly and clearly such that non-informatics experts can understand the rationale and method for each analysis. The analysis of the intraocular DCs was not clear and from the details provided, did appear appropriate.

2. Revision of claim to have identified a new type of cDC2- This is still not satisfactory as:

a. authors have not ruled out the possibility that the cells are monocyte-derived by transcriptional analysis, protein expression or functional analysis. The use of CD14-deplete cells to recapitulate the gene expression profile is not sufficient to determine that the cells in this paper are not monocyte-derived, as CD14-expression is demonstrated on cells confirmed by FLT3L response to be dendritic cells in Duterte et al. Immunity 2019.

b. To be defined as a new subset of the previously defined DC3 subset, one would need to exactly replicate the marker expression and then show that the new markers subset that subset further, the current manuscript may simple be focusing on different genes/proteins expressed by one or more previously described subsets.

c. As this paper is useful for describing a cell type or state that differentiates uveitis from healthy patients, these experiments do not need to be done to publish this paper, but the naming of the cell type should be tempered to simply describe the markers that were expressed and suggest how they fit into the Duterte/Villani schema of DC2/DC3 classification. In actuality, the discrimination of cDC2 from monocyte-derived DC2-like cells has proven difficult in many papers, thus the authors are advised to stay out of the mud, so-to-speak.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Transcriptome network analysis implicates CX3CR1-positive type 3 dendritic cells in non-infectious uveitis" for further consideration by eLife. Your revised article has been evaluated by Betty Diamond (Senior Editor) and a Reviewing Editor.

Summary:

CD1c+ dendritic cells have been found in the peripheral blood and eyes of patients with active uveitis. The authors set out to characterize CD1c+ dendritic cells in uveitis. They establish that the CD1c+ population varies between uveitis and healthy controls in both gene expression and the frequency of a subset of CD1c+ DCs, recently termed DC3s. Finally, the authors utilize a previously published dataset to show that cells with similar gene expression can be found in the eye during active uveitis.

Review:

The authors compare sorted CD1c+ DCs from patients with non-infectious uveitis and healthy controls and find a gene expression signature associated with uveitis, regardless of anatomic subtype or severity, that includes expression of the chemokine receptor CX3CR1. They corroborate this finding with a second cohort of CD1c+CD14+ cells, which strengthens the uveitis-specific CD1c+ DC signature.

The authors then compare the genes enriched in these uveitis CD1c+ DCs with previously published datasets analyzing murine CD1c+ DCs. They found more overlap between uveitis patient CD1c+ DC genes and murine RUNX3/NOTCH2 KO CD1c+ DCs than with murine viral-infected cells. While the data suggests that IFN signaling may be less relevant in these cells, the authors' conclusion that the genes differentially expressed by peripheral blood CD1c+ DCs in uveitis are not mediated by type I IFNs is overstated and alternative explanations should also be considered.

Next, the authors used flow cytometry to show that blood CD36+CX3CR1+CD1c+ DCs (thus labeled DC3s) were diminished in uveitis vs healthy controls, suggesting that the difference in CD1c+ gene expression between uveitis and healthy controls may actually be due to differential presence of CD1c+ subsets. The difference is small, but statistically significant, although the observation could have been strengthened by quantifying this cell type longitudinally in the same patients during active and inactive disease.

Next the authors found that LTA-stimulated CX3CR1+ DC3s from healthy controls secrete higher levels of uveitis-relevant inflammatory cytokines, including TNF-α, compared to CX3CR1- DC3s. This experiment was performed on a small number of healthy controls and not compared with cytokine production by DC3s from uveitis patients, which could have further supported the authors conclusion that the differential gene expression identified in Figure 1 was due to reduced proportions of CX3CR1+ DC3 cells in uveitis patients vs healthy controls, rather than qualitative differences between uveitis and healthy DC3s.

Finally, the authors find expression of CD36 and CX3CR1 on CLEC10A+ (which they use as a proxy for CD1C) cells by aqueous dendritic cells from a previously published dataset, suggesting that DC3s similar to those found at reduced frequency in the peripheral blood are present in aqueous inflammation, supporting their relevance in uveitis.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Specifically, there are errors in the methods, results, and legends that must be corrected.

Reviewer #1 (Recommendations for the authors):

In the revised paper entitled "Transcriptome network analysis implicates CX3CR1-positive type 3 dendritic cells in non-infectious uveitis," Hiddingh, Vandit, Verhagen et al. explore the gene expression of PBMCs in non-infectious uveitis patients and demonstrate a CX3CR1-positive Cd1c+ gene signature that is altered in non-infectious uveitis. They show that this population is decreased in the peripheral blood, could be regulated by notch signaling, expresses proinflammatory cytokines upon stimulation with LTA, and are present in the eye during uveitis.

The hypothesis that a cD1c+ population of DCs that could be related to uveitis in humans is intriguing and deserves further study. Their use of multiple methods to explore this population and the use of multiple cohorts are a strength of the manuscript, and it raises many intriguing questions that are potentially interesting, such as if this population is expressing inflammatory cytokines upon stimulation, why are they decreased in uveitis?

There are still areas where the manuscript is hard to follow and there are some concerns with the experimental methodology. The difficulty following the author's story is partially due to errors in cross-referencing statements in the text with their figures that support the data and understanding the experiments from the figure legends. For instance, in lines 313-315, the authors state "Furthermore, in CD1c+ DCs from healthy human donors, IFN-α did not induce downregulation of RUNX3 as observed CD1c+ DCs from non-infectious uveitis patients. Figure 2 – Figure 2 supplement 1". Data to support this statement is not found in Figure 2 or Figure 2 supplements (only healthy control data). The Figure 2 Supplement 1 legend references "the notch-negative condition in d" with a d in that figure.

Methodologically, the backgating for the manual gating of CD11c/CD1c suggests that the CD36+CX3CR1+ population is really part of a larger population of CD11c+ cells, raising the question of if this population is too poorly defined in this experimental context. This concern is slightly ameliorated by the appearance of a CD36hiCX3CR1hiCD1c+ population in the unsupervised clustering.

Despite these weaknesses, there is enough strength in using multiple methods and replication with multiple patient cohorts to overcome these concerns and to utilize it as a basis to further explore the functions of this population in uveitis pathogenesis.

Reviewer #4 (Recommendations for the authors):

The authors have responded to most of the previous reviews and have generated a more clear and cohesive manuscript.

Additional recommendations:

Figure 1

The text rationale for CD14 separation is confusing, consider omitting it.

A better methodology would have been to repeat analysis with new cohort I followed by validation using new cohort II rather than simply comparing the cohorts, but this reads more clearly and logically than the prior version and the overall conclusions seem valid.

Figure 1 Sup 1 not needed, emphasized the odd methodology sorting "cohort II" for CD14- recommend omitting this from the final version, or using instead Figure 3- Supplement 2 could be moved to the supplement for Figure 1 to explain why black module (from the CD14-sorted cohort) is stronger than then enriched modules from cohort I.

CD14+ CD1c+CD11c+CD36+CXCR3+ DC3s seem to be a subset of CD1c+CD11c+CD36+CXCR3+ DC3s, which may be why there is a stronger gene expression signature black module from cohort II vs the blue and green modules from cohort 1.

The supplemental experimental data shows that sorted DC3s from healthy peripheral blood treated with a variety of inflammatory stimuli upregulate RUNX3. One alternative explanation not discussed by the authors is that peripheral blood DC3s are in a precursor or pre-activation state.

Text: in CD1c+ DCs from healthy human donors, IFN-α did not induce downregulation of RUNX3 as observed in CD1c+ DCs from non-infectious uveitis patients, however supplemental figure 2 only tests CD1c DCs from healthy patients. CD1c+ DCs from uveitis patients were never stimulated with IFN to test whether they downregulate RUNX3 after this stimuli. This textual discussion of the experimental data is misleading.

Sup figure 3 final panel should be G, not H.

Aqueous scRNA samples are listed as obtained from Utrecht in the methods section and should cite the previous dataset.

Data used from prior sources should be more clearly detailed in legends and text. As the paper reads, it appears that the authors did the murine BMDC on the OP9 culture experiment detailed in Sup Figure 2.

Figure 5 image is very misleading – "purify tissue CD1c+ DCs" suggests that cells were purified resulting in the displayed UMAP. CLEC10A and C5AR should both be shown and the label should not state CD1c+ if this expression was not assessed- this is misleading.
