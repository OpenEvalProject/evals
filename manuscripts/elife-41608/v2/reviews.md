# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- Robert L Moritz, Institute for Systems Biology United States

## Review text

DOI: [10.7554/eLife.41608.040](https://doi.org/10.7554/eLife.41608.040)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "In-depth human plasma proteome analysis captures tissue proteins and transfer of protein variants across the placenta" for peer review at eLife. Your article has been evaluated by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Harry Dietz as the Senior Editor.

Summary:

The paper provides new avenues to deep human plasma profiling, and applies this multi-dimensional fractionation technology to the analysis of plasma proteins crossing the placenta of pregnant women. The paper provides practical guides to the capabilities of high-resolution isoelectric focusing gel strips to mass spectrometry to drill deep into the plasma proteome to a level of 1888 proteins per sample and 3053 proteins in total. The technical aspects are well discussed and compared to public databases to provide a context of the protein depth. The analysis of both mother and fetus derived proteins by the notion of identifying peptides harboring SAAV's from non-synonymous SNP differences is a key feature of this work to unequivocally identify proteins that will have to have transferred across the placenta and entered into each other's circulation.

Opinion:

This work provides a valuable advancement for mass spectrometry based proteomic analysis of the plasma proteome in terms of sensitivity and depth of coverage. In addition it could be an important resource to the field. However, major issues, described below, should be carefully dealt with prior publication.

Essential revisions:

1) Novelty compared to the state of the art: There are several prior reports on use of the method for plasma analysis dating back to Heller et al., 2005, and the authors own work published in 2014 in Nature Methods provides much of the detail off-line HiRIEF separations. The first step of using abundant protein depletion to gain depth in the plasma proteome is commonly used and common knowledge. One new aspect reported relative to the authors prior published work is that broad range IEF strips outperform narrow-range IEF strips with respect to the numbers of peptides and proteins identified. This result contradicts the author's own prior results obtained with cell and tissue samples. This important difference between the behavior of cells/tissues and plasma should be described and further explored as it represents an interesting and potentially novel finding.

- The section on exploring the proteome demonstrates that the HiRIEF method can replicate already known finding about the differences in the plasma proteome between males and females.

- The section on protein enriched during pregnancy and enriched in cord blood is interesting, but largely describes what is already known from other blood analysis papers. Perhaps most interesting, although again simply descriptive, is the finding of fetal hemoglobin in maternal blood of some of the subjects. No mechanistic or biological implications for this are presented.

- Variant observation – it is well known that MS-based proteogenomics can do this (see authors own work in 2014; and, for example, Bing Zhang Nature 2014; Mertins Nature 2016; Hui Zhang Cell 2016). The fact that one can do this in blood and show correlation to the genome is therefore fully expected.

2) Method analyses 72 fractions from the HiRIEF separation and uses ca. 89 hours of MS instrument time to acquire the data. The number of proteins reported is ca. 1/3 of what has been achieved with slightly greater instrument use time (Branca et al., 2014 and Keshishian et al., 2016). The HiRIEF method does yield some proteins not detected by other approaches, but overall the depth is limited in comparison to the Keshishian method which makes it somewhat less relevant for biomarker discovery or to inform biology.

3) Importantly, the method appears to not be particularly reproducible as many of the supposedly confidently identified proteins must only be being observed in one or a small number of analyses: "When applying the HiRIEF methodology we identified on average 1505 proteins (per sample)…."; "In total 3053 proteins (across at least 16 experiments, perhaps more…hard to tell) were identified in the different experiments.' The fact that this aggregate number approaches the 3509 proteins from the most recent version of the human plasma atlas is, therefore, not of much use from the perspective of what the method can do on an individual sample basis for biology or biomarker discovery. What matters is what can be confidently and repeatedly detected across multiple patient/subject samples.

4) Importantly, the number of proteins confidently identified by the authors appears to be overstated. From 1/4 to 1/2 of the proteins claimed to be identified are identified on the basis of a single peptide according to Supplementary file 1. It is standard practice in proteomics to only claim confident identification of a protein when 2 or more unique peptides from that protein are identified. Therefore, the large number of proteins claimed (ca. 3000 across multiple experiments) is likely highly inflated as it appears to include "one-hit wonders". It also appears that these numbers derive from analysis of the same plasma pool rather than plasma from different subjects – this needs to be clearly stated in the text.

5) The PSA spike experiment is interesting, but simply replicates what is already known: that if you know the fraction that peptide(s) from a protein of interest elute in, you can get significantly higher sensitivity by focusing experiments on those selected fractions. In this case the authors changed to selected fractions a single narrow pI range. This is similar in concept to the PRISM method developed at PNNL by the Smith group.

6) Authors state that the "method" is reproducible. As noted above, based on the ability to confidently and repeatedly detect proteins appears to be rather low. Exactly which parts are reproducible (i.e., depletion, IEF fractionation, LC-MS/MS, identifications, etc.) is not entirely clear. The data used to support this statement are TMT intensity ratios obtained in a set of 4 x TMT 10-plex experiments, and focuses on a subset of ca. 1000 proteins found to be in common across the experiments. What is not demonstrated well (or at all) is the ability to confidently determine differences in protein abundance between samples. It would be much more convincing to show the reproducibility of the relative abundance differences of proteins from different patient samples and which cover the detection range from high to low abundance. Data plotted appear to be just for the pooled plasma sample in each of the 4 TMT plexes where no differences in abundance are expected across samples for the same protein. Perhaps more importantly, the actual method used for analysis of subject plasma samples does not use TMT labeling, so the reproducibility of the label-free proteomics approach has not being directly evaluated.

7) Keshishian et al. report a TMT1- method that provides ca. 600 proteins/sample in ca. 5h of analysis time (Keshishian et al., 2016). This paper should be cited and your results compared.

8) Please provide tables: of proteins which are purported to be newly discovered in plasma (n=611); protein affinity assay to provide the identity of the 751 protein assays that are not in the HiRIEF or PeptideAtlas lists, and of whom they are available from; CancerSEEK fingerprint used so readers do not have to go to the original paper to find out this information.

9) The figures are a little on the small size of acceptable quality and care should be taken to provide legible axis and text within the figure. If they can be made larger, it would benefit the paper immensely.

10) For the identification of new proteins, full identification data provided as tables should provide the MS spectral details of each of the new plasma proteins identified, the MS spectra of peptides with SAAV's, and provide the genomic data used to construct the SAAV databases for proteomics search algorithms.

11) Choosing a single amino acid variation (SAAV) as the strategy to distinguish between mother and fetus proteins might hold a weakness. Since the mass difference between the WT peptide and the variant peptide is relatively low (based on one amino acid substitution) it may be explained by additional post-translational modifications (PTMs) from ones that were already mentioned and may not necessarily be explained by SAAV. For example, in Supplementary file 9: peptide 2 (T>S) – the mass difference equals Methylation, peptides 7,25,26,30,32 (V>I/L) – mass difference equal Methylation, peptide 13,15 (E>D) – mass difference equal Methylation, peptide 1,18,19 (P>L) – mass difference almost equals oxidation. We would suggest to closely review the peptide spectra to validate that the source of the different mother-fetus peptides is due to genomic variance and not PTM. This should be addressed or discussed in the manuscript and it may limit the interpretation of transfer.

12) When analyzing the inter-individual variability of the plasma proteome (Figure 2B) the authors identified HLA proteins in their top 20 list. This may be due to the highly polymorphic nature of HLA causing individual's peptides to not be properly assigned to the reference sequence. This is worth considering or mentioning.

13) The authors should clarify what they mean by 'load'. Is this the amount of protein loaded onto the MARS14 column or onto the isoelectric focusing strips. If the latter, did it require multiple depletions of the same sample to reach the amount of total protein?

14) In the Methods section they list two types of data processing tools (MS-GF+ and MaxQuant). It is not clear why did they use two different tools and for which samples did they use each tool?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "In-depth human plasma proteome analysis captures tissue proteins and transfer of protein variants across the placenta" for further consideration at eLife. Your revised article has been favorably evaluated by Harry Dietz as the Senior Editor, a Reviewing Editor, and two reviewers.

The manuscript has been substantially improved but there are some remaining issues that need to be addressed before final acceptance, as outlined below.

1) Figure 3B – it is unclear if the colored dots obscure one another – is there a way to statistically strengthen this statement? Perhaps it would be useful to calculate the average abundance of each of the four groups and compare them? It seems that the statement is not supported statistically.

2) Overall, the authors have improved the manuscript substantially and the paper is almost ready for acceptance with the new information provided. However, the revised manuscript could have been better with tables that have the required information contained in them as requested, as well as the individual peptide spectral files from all of the novel identifications purported and provided to be more extensive and user-friendly than the current revised tables included. If done, many readers can take the information provided in this paper and perform their own analysis and corroborate the findings described within. For example, the review asked for tables of identification and spectral information of each novel peptide to describe the new protein lists in both the plasma identifications as well as the variant peptides that were found with this work, yet a simplistic table of ensemble identifiers (Supplementary file 4) was only provided for the novel plasma proteins even though the full spectral information was provided for the variant peptides. Given the scrutiny that the work presented in this manuscript will come under from the research community interested in plasma protein analysis, it is beholden to the authors to defend the work to the best of their capabilities as it stands if the work is to be published in a quality journal. The tables of new identifications would encompass all the technical details of the proteins discovered including web-linked accession number to not only ensemble but also to neXtProt and PeptideAtlas given this was one of the databases referred to, how many peptides for each novel protein were found, their individual score and probabilities, as well as any other quality factors used for their positive identification. The PSM MS spectrum plots were not provided as requested for the 611 newly discovered plasma proteins, however, these were supplied for the mother/baby variant peptides identified in the demonstration project of this paper. To complete the resubmission, please provide this updated table (Supplementary file 4) also identifying which files in the raw data repository of this work the novel identifications were made from so readers can quickly get at the data if needed.
