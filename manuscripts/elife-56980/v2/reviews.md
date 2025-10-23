# Peer review - Round 1

Editors:
- Valerie Horsley, Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56980.sa1](https://doi.org/10.7554/eLife.56980.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Overall, this manuscript provides informative data sets of m6A profiles and clear-cut evidence showing the consequences of m6A loss in skin epidermal progenitors. This study highlights the imperative role of m6A modification in modulating fate decision of skin epidermal progenitors.

Decision letter after peer review:

Thank you for submitting your article "m6A impacts fate choices during skin morphogenesis" for consideration by eLife. Your article has been reviewed by Marianne Bronner as the Senior Editor, a Reviewing Editor, and two reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Rui Yi (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this manuscript, Xi et al., studied m6A RNA modification and its role in embryonic skin development. They first profiled m6A modification in epithelial progenitors and investigated the correlation between m6A modification and translation efficiency as well as mRNA stability. By conditionally deleting Mettl3, a critical writer for m6A, in epithelial cells during skin development, they examined the physiological impact of Mettl3/m6A modification and observed compromised hair follicle morphogenesis.

Essential revisions:

1) The correlation between m6A and translation efficiency (TE) seems weak, and the way they show this in Figure 1E is confusing. In the Materials and methods section, I couldn't find the definition of "Relative TE" and the cut-off for "high", "med" and "low" m6A modification. As it's shown in Figure 1E, ~50% of "high" m6A mRNA have relative TE greater than 0 and ~50% less than 0. This doesn't support "high" m6A enhances TE. Even in the CDS panel, "med" and "low" m6A transcripts show only very mild reduction of overall TE. They should fully define the parameters used in this analysis; use non-modified transcripts as control; calculate the statistical significance of each comparison e.g. "high" vs "med", "med" vs "low" and all against non-modified transcripts. To truly support the claim that m6A enhances TE, they should perform ribosome profiling in WT and mettl3 ko epithelial cells and calculate the differential TE. And for a few examples, they should quantify protein levels by Western blotting and/or staining to support the increased TE indeed leads to a higher concentration of protein or the reduced protein levels in cKO.

2) They relied heavily on gene ontology analysis to identify pathways that are preferentially affected by m6A. However, this analysis is confusing. They stated they "ranked the mRNAs carrying the modification according to the sum of normalized-to-input uTPM at each m6A site within the coding sequence, and divided by CDS length" (subsection “Skin transcripts most highly modified by m6A are involved in hair follicle 129 morphogenesis”). However, I'm not sure if they used the ranking system at all when they searched for enriched KEGG pathways. It seems that they simply identified pathways with most transcripts with m6A but not necessarily highly modified. They need to show (1) which pathways the most highly m6A modified mRNAs are enriched in? (2) whether the top enriched pathways contain many highly m6A modified mRNAs? In addition, they should apply their TE analysis to these enriched pathways. Can they find reduced TE in these highly modified mRNAs that belong to the top KEGG pathways such as BCC and hedgehog signaling?

3) The phenotypical analysis should be strengthened by more careful analysis of cell proliferation such as colony formation in addition to EdU and Ki67 staining and cell adhesion analysis. The demonstrated phenotypes also seem similar to Dicer1 KO, when all miRNAs are depleted, including neonatal lethality due to the lack of weight gain, degenerated hair follicles and diminished filiform papillae formation.

4) They mentioned that WNT and SHH pathways surfaced in multiple pathways in their miCLIP data and suggested that m6A might function in hair follicle fate through these pathways. However, the authors did not show how these pathways behaved in WT vs cKO mice. Such analysis will strengthen their claims. Aberrant LEF and SHH signaling was associated with failure to form tight dermal condensates. With this data, they concluded that WNT signaling has been altered by m6A modification. However, there were not mechanistic studies to prove that WNT has been altered. The authors can do qPCR analysis of transcripts that are under WNT regulation to further show altered WNT signaling (e.g. axin) or IHC imaging of β-catenin etc. to future strengthen their conclusion.

5) They performed single-cell RNA-seq to measure the changed transcriptome and cellular state. However, their cell clustering analysis should be performed by using control and cKO samples together, rather than clustering separately and relying on marker genes to identify each population in control and cKO (Figure 5—figure supplement 1D, F). Are all corresponding cell populations in control and cKO clustered together? If not, they should explore the underlying reasons. The pseudotime analysis in Figure 4B should be strengthened by statistical analysis rather than eyeballing the population/lineage differences between Ctrl and cKO. They also should keep in mind they only have 1 pair of biological samples, which may reduce the robustness of the analysis. For differential gene analysis, they should independently confirm each data (Figure 4C, Figure 5D etc.) by qPCR or bulk RNA-seq from more sample pairs.

6) Based on ribosome profiling analysis, they suggest that m6A enhances translation. Based on RNA-seq, they suggest that m6A reduces mRNA stability. Globally, these are two opposite effects on mRNA's potential to make protein. It's important to distinguish (1) whether these two opposite effects of m6A are on different mRNAs? (2) if the same mRNAs are under the control of both effects, what is the net effect on protein synthesis? Are they cancelled out or one effect is more dominant than the other? How does this explain/correlate with the phenotypes?

7) The observation of prematurely detached basal cells is interesting. Are they the direct consequence of reduced cell-cell adhesion and/or cell-bm adhesion?

8) The reviewers were not sure about the point of OPP experiments. OPP label may be too low resolution to show any changes in Mettl3 cKO.

9) Figure 3E-F: it is clear that in the grafted skin Mettl3 cKO HFs underwent HF degeneration in accompany with sebocyte differentiation. However, it is not clear if this fate switch only occurred in Mettl3 cKO HFs upon wounding (grafting in this case). Oil red O staining with P6 ungrafted skin sections will partially address this question. If this fate switch only happens upon wounding, authors should discuss the effects of m6A loss in the differential circumstance as well as speculate the effect of wounding in m6A-mediated regulation.

10) Subsection “Conditional ablation of Mettl3 in epidermal progenitors results in a marked defect in HF morphogenesis”: "the engrafted cKO epidermis was hyperthickened, a feature which had also been evident in ungrafted cKO epidermis." To this reviewer, the hyperthicken epidermis could NOT be appreciated in ungrafted cKO epidermis based on the H&E staining shown in Figure 2G. The quantification in the thickness of ungrafted and grafted epidermis will be essential. In line with point #2, this hyperthicken epidermis in grafted cKO skin might be caused by wounding if hyperthickness is not detected in ungrafted Mettl3 cKO epidermis.

11) Figure 5E: Authors stated that MYC expression was elevated within Mettl3 cKO epidermal progenitors (subsection “A cohort of highly m6A-decorated mRNAs whose levels rise upon removal of their modification”). It is not clear to this reviewer how the quantification of MYC expression was done. Which cell markers did authors use to define "epidermal progenitors" (e.g. integrin α6 or K14…)? Did authors also include P-cad+ WNY-hi, WNT-lo HF cells, and epidermal suprabasal cells? Please clarify this by adding information in the figure legend as well as Materials and methods.

12) Figure 3—figure supplement 1: It is interesting to see high levels of PCAD expression in the basal layer of grafted Mettl3 cKO epidermis. Did authors also find this striking pattern in ungrafted Mettl3 cKO epidermis (e.g. P6 ungrafted skin)? What could be the explanation of this significant upregulation of P-Cadherin in the Mettl3 cKO epidermal basal cells, e.g. alteration in cell junction? Confusion in fate specification? It will be helpful if authors can check on ungrafted skin and speculate the possibilities.
