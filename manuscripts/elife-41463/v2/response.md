# Author response - Round 1

Authors:
- Patpicha Arunsan
- Wannaporn Ittiprasert ([ORCID: 0000-0001-9411-8883](https://orcid.org/0000-0001-9411-8883))
- Michael J Smout ([ORCID: 0000-0001-6937-0112](https://orcid.org/0000-0001-6937-0112))
- Christina J Cochran
- Victoria H Mann
- Sujittra Chaiyadet
- Shannon E Karinshak ([ORCID: 0000-0002-2079-0973](https://orcid.org/0000-0002-2079-0973))
- Banchob Sripa
- Neil David Young ([ORCID: 0000-0001-8756-229X](https://orcid.org/0000-0001-8756-229X))
- Javier Sotillo ([ORCID: 0000-0002-1443-7233](https://orcid.org/0000-0002-1443-7233))
- Alex Loukas
- Paul J Brindley ([ORCID: 0000-0003-1765-0002](https://orcid.org/0000-0003-1765-0002))
- Thewarach Laha

## Response text

DOI: [10.7554/eLife.41463.019](https://doi.org/10.7554/eLife.41463.019)

Essential revisions:

With regard to point 1 in the summary, provide an assessment of the deep sequencing approach as an informative estimate of mutation frequency compared with possible alternative methods that would yield an estimation of the frequency of mutations in the target on a worm-for-worm basis. Comments on how the low mutation frequencies obtained by the deep sequencing approach can be reconciled with the dramatic decrements in Ov-grn-1 transcripts and protein and in the virulence of the parasites would also greatly improve the paper. As suggested by reviewer 1 (and by all of us in consultation) a discussion of the site of Ov-grn-1 expression within the worms as it relates to efficiency of transduction with CRISPR elements would also be helpful.

We have addressed the issue in the revised Discussion, second paragraph, as follows”

“Although the findings demonstrated programmed gene editing of the Ov-grn-1 locus, the somatic mutation rate in the adult developmental stage was generally <5% of the genomes recovered from these multicellular parasites. […] If so, this may explain the marked reduction of expression and secretion of Ov-GRN-1 in tandem with a limited rate of mutation estimated in genomic DNA pooled from the gene-edited flukes.”

With regard to point 2 in the summary, the segment on "Longevity of programmed mutation at Ov-grn-1" was somewhat confusing to all three reviewers before and during our consultation. It is essential to clarify this section along lines specified by reviewers 1 and 3.

We revised the relevant sections in the Results and Materials and methods, extensively, including a revised heading in the Results and an additional figure (Figure 5) to provide the findings of a NGS/CRISPResso analysis of Illumina sequence reads of pools of genomic DNAs from the L, M and H groups in Figure 4. In the Materials and methods, we now include more thorough descriptions of the two approaches employed to quantify the outcome of programmed gene editing, 1) tri-primer qPCR and 2) targeted amplicon library NGS with analysis using the CRISPResso algorithm and software program; and to comparatively describe their attributes and limitations.

We anticipate that the revised text, including the new findings/Figure 5, will clarify the results and clarify our interpretation of the findings.

Results

“Gene editing efficiency negatively correlated with granulin expression during infection

Bile ducts parasitized by the gene-edited worms displayed a broad range of fibrosis from minimal to marked, as established by staining both with Sirius Red and with antibody specific for alpha-smooth muscle actin. […] Lastly, these findings also demonstrated the longevity of the programmed mutation at Ov-grn-1; mutations were retained in the parasite for at least 60 days during active infection of the mammalian host.”

Materials and methods

“Targeted amplicon libraries, Illumina-based sequencing

Several Illumina NGS libraries were constructed. First, for analysis of programmed editing of adult flukes that were subjected to gene editing manipulation and subsequently cultured in vitro, genomic DNAs were extracted from the Ov-grn-1 gene-edited adult liver flukes at each of 7, 14 and 21 days after transfection. […] However, the latter approach provides more detailed characterization of the events including the types and frequencies of the INDELS, and is more accurate (Schmittgen and Livak, 2008).”

With regard to point 3 in the summary, the three reviewers concurred that a control in which Cas9 was expressed without a functional gRNA would have added to the rigor of the study. There was difference of opinion about the advisability of including in such a control a nonfunctional gRNA (i.e. one that contained a scaffold with no seed sequence or that contained a scaffold with a seed sequence having no homology in the O. viverrini genome). All this is to say that since this paper is likely to constitute a prototype for future studies, some discussion of what constitutes a rigorous control in experiments of this kind is warranted.

To address the concern, the revised Discussion includes a new paragraph addressing the reviewers/editors’ advice on additional controls including a non-functional gRNA:

Discussion

“The rigor of future gene editing investigations might be enhanced with the inclusion of additional controls including parasites transfected with an otherwise functional vector that lacks target-specific gRNA and/or a gRNA with a scaffold but without seed sequence and/or containing a seed sequence without homology in the genome of O. viverrini. […] Characterizing by immunolocalization the site of expression in the parasite from hamsters infected with gene-edited NEJ and/or the location of the gene editing plasmid after transfection of the liver fluke should be instructive.”

Reviewer #1:

[…] It would have been helpful to discuss where granulin is expressed in the worm as this can help inform the tissue-specific efficiency of the transfection methods used.

We thank the reviewer for the useful suggestion – see response to point 1 above.

The efficiency of transfection data was provided for the directly transfected adults and yet the biology was performed on adults derived from transfected of NEJs – it's unclear why the transfection data were not generated for the juvenile flukes OR from adults of transfected NEJs.

Please see our response above to essential revision point 2.

Mutation frequencies are provided for adult fluke with low, medium and high levels of target gene transcript expression. It's not clear if the data for the pooled samples from each group are based on an n=1 or multiple pools of each type. Either way, this needs to be clarified and, if multiple pools were used, the range or SE values included with all the relevant data in the manuscript..

We have clarified this issue with the inclusion of the following statement in the Materials and methods section:

“The data for the pooled samples from each group are based on a single Illumina run, i.e. n = 1 sample for each of the L, M and H genomic DNA pools.”

The ranges used to assign to define the H, M and L groups appear to differ between the Results (subsection “Longevity of programmed mutation at Ov-grn-1”) and Materials and methods (subsection “Extraction of nucleic acids”).

Text revised to resolve the inconsistency, as follows:

Results section

“[…] adult flukes at necropsy were assigned to one of three groups based on Ov-grn-1mRNA expression levels, as follows: (i) ≥ 100% relative to WT mean, i.e., low (L) efficiency of programmed gene editing; group was termed LΔOv-grn-1; (ii) > 10 to < 100% relative to WT mean, i.e., moderate (M) level efficiency of programmed gene editing; termed MΔOv-grn-1; and (iii) ≤ 10% relative to WT mean, i.e., high (H) level efficiency of programmed gene editing; termed HΔOv-grn-1.”

Materials and methods section

”To assess the performance of the gene editing approach, following necropsy of hamsters and recovery of the liver flukes, the adult worms were assigned to one of three phenotypes based on the levels of Ov-grn-1 transcript knockdown, low (L), moderate (M) or high (H), as follows: L, ≥100% relative to WT mean (low efficiency of programmed genome editing), group termed LΔOv-grn-1; M, > 10 to < 100% relative to WT mean, group termed MΔOv-grn-1; and H, ≤ 10% relative to WT mean, group termed HΔOv-grn-1.”

In the subsection “Programmed mutation of growth factor secreted by carcinogenic liver fluke”, the three outcomes of transfection (insertion, deletion, substitution) totaled 27640 against the total number of NHEJ reads of 27616 – but why these differ is not stated.

Text revised to resolve the inconsistency, as follows: “The CRISPResso pipeline was used to quantify gene-editing outcomes and efficiency (Canver et al., 2018; Pinello et al., 2016); among > 2 million reads aligned against the reference sequence, 27,640 sequence reads exhibited non-homologous end joining (NHEJ) mutations, including 170 reads with insertions (0.6%), 193 reads with deletions (0.7%) and 27,277 reads with substitutions (98.7%).”

Subsection “Attenuated infection-induced hyperplasia of the biliary tract”, last sentence is incomplete and needs rewriting.

Rewritten as:

“At 60 days after infection, significant differences in biliary hyperplasia remained between hamsters infected with WT (216%) and ΔOv-grn-1 (162%) flukes (P ≤ 0.05), although this was less marked than during acute infection at day 14 (Figure 3G).”

Materials and methods – Wrt transfection of mature adult fluke, the authors need to state if the 20 worms were transfected individually (1 per cuvette) or otherwise?

Clarified in the revised version, as follows:

“Pools of 20 mature adult flukes were simultaneously subjected to transfection with 10 µg pCas-Ov-grn-1plasmid DNA in ~500 µl RPMI-1640 (Σ) by electroporation; all 20 flukes were included in the same cuvette.”

Reviewer #3:

1) If I understand the narrative under "Longevity of programmed mutation at Ov-grn-1" it suggests that individual flukes were subjected to quantitative RT-PCR to determine levels of expression, classed according to three levels of expression: low, medium and high, and then their gDNA pooled for deep sequencing to determine mutation rates. Is it not possible to genotype individual flukes, or does mosaicism tend to render mutant genomes in these worms practically undetectable?

First, please see our response above (essential revision point 2). Second, we did directly genotype individual flukes using the tri-primer qPCR approach (Figure 5). Second, it is technically feasible also to genotype individual worms using the targeted amplicon library-NGS-CRISPResso computational algorithm-based analysis, and whereas this approach will provide more information including the NHEJ profile of% insertions,% deletions, and% substitutions, it is technically more challenging, more time consuming, and more expensive.

If possible to obtain, an estimate of the percentage of worms in a sample population that showed any mutation might be easier to reconcile with the very large reductions you see in Ov-grn-1 protein and the large changes in the parameters relating to hepatobiliary disease that you see.

We have now addressed this issue experimentally following the reviewers’ recommendation; please see Figure 5 and related text. Also, we addressed the issue in our responses above to the essential revisions, points 1 and 2.

2) The control groups (subsection “Transfection of liver flukes with pCas-Ov-grn-1”) in this study appear to have been WT parasites and "mock transected" parasites that were electroporated in complete medium lacking plasmid DNA. Wouldn't a more rigorous control be parasites electroporated with a vector containing all functionalities except that the target-specific gRNA was replaced with either a gRNA with a scaffold but no seed sequence, or, better yet, a gRNA containing a seed sequence with no homology in the O. viverrini genome? This would control for any non-specific effects of Cas9 expression on parasite fitness. Such effects have been noted in other systems, notably in C. elegans lines that express Cas9 constitutively.

See our response to point 3 above.
