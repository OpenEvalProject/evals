# Author response - Round 1

Authors:
- Malini Rajan ([ORCID: 0000-0002-7653-4223](https://orcid.org/0000-0002-7653-4223))
- Cole P Anderson
- Paul M Rindler
- Steven Joshua Romney
- Maria C Ferreira dos Santos
- Jason Gertz
- Elizabeth A Leibold ([ORCID: 0000-0003-1000-9503](https://orcid.org/0000-0003-1000-9503))

## Response text

DOI: [10.7554/eLife.44674.029](https://doi.org/10.7554/eLife.44674.029)

[Editors’ note: the author responses to the first round of peer review follow.]

All the reviewers found the manuscript to be very interesting, but the lack of rigor or in-depth analysis in many areas makes it unsuitable for publication in its current form. The manuscript could be improved by going more in depth on the metal biology or by strengthening the innate immunity aspects. The diversity of the reviewer's suggestions indicate that the revision will likely take more than two months, the time limit in eLife for revision. This is why the paper was rejected. Nevertheless, the authors could consider re-submitting their article to eLife as a new submission once the reviewer's comments have been addressed in full.

Based on the reviewers’ suggestions and comments, we made substantial changes to the manuscript, including addition of new iron pathogen experiments, reanalysis of RNA-seq data and addition of genetic details, which has resulted in a stronger manuscript.

In this manuscript, we report on the identification of a relatively uncharacterized nuclear receptor-1 (NHR-14) that couples innate immunity with iron sequestration. NHR-14 shares homology with vertebrate HNF4. We identified nhr-14 in a genetic suppressor screen conducted to identify genes that rescues the developmental delay of hif-1 mutants grown under iron limitation. We found that nhr-14 loss of function rescues the hif-1 developmental phenotype through increased expression of the intestinal iron importer SMF-3. Transcriptome studies using nhr-14 mutants revealed enrichment of innate immune response genes, many of which are Class 2 genes reported by Murphy et al. (Nature 2003) to be repressed by DAF-16/FOXO during reduced insulin signaling. More recently, Tepper et al. (Cell 2011) discovered that Class 2 genes were activated by the PQM-1 transcription factor during reduced insulin signaling. Using genetic and biochemical approaches, we showed that smf-3 is a PQM-1 target gene. Given the innate immune response and iron signatures in nhr-14 mutants, we showed that nhr-14 loss of function is required for pathogen resistance and that iron sequestration is a component of the pathogen innate immune response. Several nuclear receptors are known regulators of innate immunity in C. elegans; however, NHR-14 is unique among these receptors in coupling innate immunity with iron sequestration. Our data provide new knowledge into how C. elegans use nuclear receptors to regulate innate immunity and iron availability, and show iron sequestration as an important component of the innate immune response.

We believe that our work is of current interest as several of the genes in nhr-14 mutants have been identified in other stress response pathways in C. elegans. For example, O’Brien et al., 2018, identified PQM-1 as a regulator of transcellular chaperone signaling in neurons and in intestine. Several of the key components of neuronal and intestinal signaling pathways and are upregulated in nhr-14 mutants. Of interest, nhr-14 expression is also enriched in neuronal and intestinal cells, providing further evidence suggesting a role for NHR-14 in these pathways. In another paper, Jiang, et al. (eLife2018) identified a genetic pathway that regulates hypothermia stress, and several of the key genes in this pathway, including a transcription factor and proteases, are upregulated in nhr-14 mutants. It is thus likely that NHR-14 has a function in these pathways.

As NHR-14-PQM-1 represents a new innate immunity pathway, future studies are needed to identify other key components in this pathway and endogenous or exogenous ligands that regulate NHR-14 transcriptional function, and to determine the role of NHR-14 in the stress response pathways described above.

[Editors' note: the author responses to the re-review follow.]

Essential revisions:

1) Transcriptome analysis. A main concern is with the analysis presented in Figure 5. Apart from the fact that DAVID has not been updated (https://david.ncifcrf.gov/helps/update.html), it contains far less information than C. elegans-specific tools such as WormExp. Running their list through WormExp reveals several very significant overlaps with other datasets, including nhr-8 mutants that merit at least discussion if not investigation.

We thank the reviewer for this suggestion.

We compared upregulated and downregulated nhr-14 genes with WormExpv1.0 “mutant” category. We found that 148 upregulated nhr-14 genes out of 568 genes overlapped with genes upregulated in nhr-8 mutants. Also, of interest, 156 upregulated nhr-14 genes overlapped with hyl-2 (encoding ceramide synthase) mutants. Together, these observations suggest a role for nhr-14 in fat metabolism. Iron and lipid metabolism are related and many enzymes involved in lipid metabolism require iron for activity. We added the above gene comparisons to a supplemental table (Figure 6—source data 4).

Using WormExp “tissue” category and Cao et al., 2017 single-cell PCR dataset, we found that downregulated nhr-14 genes are enriched in hypodermis and neurons and nhr-14 upregulated genes are enriched in intestine and neurons. These data are consistent with enriched expression of the NHR-14::GFP::FLAG transgene in intestine and head cells (Figure 3B-D). WormExp “tissue” dataset overlap with upregulated and downregulated nhr-14 genes in reported in Figure 5—source data 1.

Further, the authors write, "Among the 261 downregulated genes, there was enrichment in genes involving cellular organization and body morphogenesis, including sqt-1, noah-1 and sym-1 (Figure 5D and Figure 3—source data 1)".

But what is really striking is the number of genes that normally undergo a sharp drop of expression at the L4 to adult transition, many of them expressed in the epidermis. As can be visualized at https://elegans.mdc-berlin.de/cel_ex.html, this applies, for example, to sqt-1, col-17, rol-8 (the top 3 in Figure 5D), as well as to the heterochronic gene lin-42. There is no comment on this very remarkable pattern, nor the simple experiments that might address the question of how it might be related to the continued nuclear localization of PQM-1 into adulthood.

We examined the developmental expression of the top 50 downregulated nhr-14 genes using MDC-BIMSB. In agreement with this reviewer observations, we found that expression of 42 out of the top 50 downregulated nhr-14 genes were sharply downregulated at the late L4 stage, while only 3 were upregulated. The 3 upregulated genes were enriched in intestine, while downregulated nhr-14 genes were enriched in seam and non-seam hypodermal cells (determined from Cao, et al., 2017 single-cell RNA-seq).

We also examined the developmental expression of the top 50 upregulated nhr-14 genes and found most genes are also downregulated at late L4 (20 genes were unchanged or not in the dataset and 6 were upregulated), but not as sharply as the downregulated nhr-14 genes. Of interest, the 6 genes upregulated at late L4 were DAF-16/FoxO Class II genes (dod-19, dod-21, dod-23, dod-24, oac-14, C32H11.9). qPCR analysis revealed that expression of dod-19, dod-24, oac-14 and clec-41 (dod -21 and C32H11.9 were not assessed) were reduced in nhr-14; pqm-1 (RNAi) mutants, indicating that PQM-1 regulate these genes downstream of nhr-14. These new data are reported in Figure 7. See comment 3B below.

We appreciate the reviewer’s effort in uncovering these interesting observations regarding the developmental expression of nhr-14 genes. We are pursuing how loss of nhr-14 causes the nuclear accumulation of PQM-1 in adults, and how it affects gene expression and aging. However, we prefer not to discuss the developmental expression of upregulated and downregulated nhr-14 genes in this manuscript as it would require inclusion of more datasets as well as experiments. These experiments would require a considerable amount of work to do rigorously. We feel that these experiments are beyond the scope of our manuscript, which is to understand the link between nhr-14 regulation of innate immunity and iron metabolism.

On the same line, the authors write, "Interestingly, we observed less overlap between nhr-14 upregulated genes with Serratia marscens [marcescens] (Wong et al., 2007). The basis for this difference is unknown, but is likely a result of a highly specialized response to S. marscens [marcescens]". If they had used WormExp, they would have seen a very significant overlap with Serratia-induced genes in independent study (Engelmann et al., 2011). And reading that study, there is even the following, "In the current analysis, the results of our previous study of the response to S. marcescens using oligo-arrays [22] stood out. As this was not the case for the results for the response to 2 other bacterial pathogens, and given the underrepresentation in the S. marcescens data set of 'common response genes' [22], this presumably reflects an experimental difference in the strength of the infection for the samples prepared for analysis using oligo-arrays". In other words, the authors' conclusion is unlikely to be correct. And that makes more sense since the screens that used C. elegans to identify S. marcescens virulence factors highlighted a role for iron (see for example the Abstract of PMID: 12660152, and 25070509).

We agree and revised this section. We compared the Engelmann et al., 2011 Serratia dataset with upregulated nhr-14 genes and found that out of 2124 genes in the Engelmann dataset, 237 overlapped with upregulated nhr-14 genes. These data are shown in Figure 6A and listed in Figure 6—source data 1. The Wong et al., 2007 Serratia dataset was deleted.

2) The authors clearly demonstrate that nhr-14 mutants have higher levels of smf-3 transcript, and SMF-3 is a known iron import protein, leading to the hypothesis that this is the critical target gene for the hif-1 rescue. I acknowledge this is a reasonable and even plausible hypothesis. However, the transcriptional analysis of nhr-14 mutant animals demonstrates that hundreds of transcripts are altered, so in principle any one of these changes, or many of these changes in combination might mediate the hif-1 rescue. The critical issue is what additional evidence can test the smf-3 hypothesis. The authors create a smf-3; nhr-14; hif-1 triple mutant and the rescue is lost, in that these triple mutants do not grow in low iron. My concern is that the smf-3 single mutants also do not grow in low iron. So, yes nhr-14 requires smf-3 to rescue hif-1, but this is somewhat different from proving that nhr-14 rescues by increasing smf-3 activity. The authors should acknowledge that because the smf-3 single mutant cannot grow in low iron, there are multiple interpretations for the triple mutant.

We agree and added the sentence:”Given that the smf-3(ok1035) single mutant alone displays a developmental delay under iron limitation, this suggests that other genes in nhr-14(tm1473) mutants might also contribute to the rescue of hif-1(ia4) mutants”.

3) Additional controls:

3A) Figure 3. Results shown in panels B, C, and D lack essential genotype that has to be tested, namely nhr-14,smf-3 double mutant. This genotype is essential to prove that the phenotypes of nhr-14 mutants are mostly mediated by the elevated level of smf-3.

We agree and included iron content of the smf-3(ok1035); nhr-14(tm1473) double mutants (Figure 3B) as well as an image and growth analysis of this mutant on NGM and NGM-BP (low iron) (Figure 3C). We did not include the smf-3; nhr-14 double mutant to the life span analysis in panel D because of its poor growth under iron limitation.

3B) Figure 5E and D. It is nice to see enrichment in PQM-1 binding motif in the promoters of the upregulated genes, but experimentally do these genes really require PQM-1 for their expression? What will be their level of induction in nhr-14, pqm-1 double mutant? I think this experiment is important to prove that pqm-1 regulates these genes downstream of nhr-14.

We agree and used qPCR to measure expression of several upregulated nhr-14 genes in nhr-14(tm1473); pqm-1 (RNAi) and nhr-14(tm1473); Control RNAi worms. qPCR analysis showed reduced expression of Class II genes dod-19, dod-24, clec-41, gst-38 and oac-14 in nhr-14; pqm-1 (RNAi) mutants vs nhr-14; Con (RNAi) worms. The expression of Class II genes ins-7 and lys-2 and Class I genes lys-7 and ftn-1 were not changed in nhr-14; pqm-1 (RNAi) mutants. These data are shown in Figure 7. See response to comment #1.

3C) Figure 6A. This experiment lacks nhr-14, pqm-1 double mutant. Again, this is essential to prove epistatic relations between the two genes.

We agree and measured the survival nhr-14(tm1473); pqm-1 (RNAi) worms after infection with PA14. We found that the nhr-14(tm1473); pqm-1 (RNAi) mutants are more sensitive to PA14 that the nhr-14 single mutant, suggesting that PQM-1 is required for nhr-14(tm1473) resistance. These data are shown in Figure 8A (graph) and Figure 8—source data 1 (survival analysis).
