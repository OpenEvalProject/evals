# Peer review - Round 1

Editors:
- Thomas O'Brien, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.42463.026](https://doi.org/10.7554/eLife.42463.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Broad Impact of Interferon Lambda 4 on Hepatitis C Virus Diversity" for consideration by eLife. Your article has been reviewed by four peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wenhui Li as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Previously, Ansari et al. reported results of a genome-to-genome study of 542 individuals who were chronically infected with HCV (predominantly viral genotype (VGT) 3, but also VGT 2; Ansari et al., 2017). Genotype for the IFNL4 rs12979860 SNP marker associated with 11 amino acid polymorphisms on the HCV polyprotein (60, 109 [C]; 500, 501, 576d, 578, 741 [E2]; 2414 [NS5A]; 2570, 2576, 2991 [NS5B]) based on a 5% false discovery rate (FDR). The strongest association was for 2570 in NS5B; residue 2414 in NS5A associated with HCV RNA levels amongst patients infected with VGT 3a. The present paper, which is restricted to the 485 subjects who were infected with VGT 3a, contains important new data, but the analytical approach used to arrive at these conclusions is complicated and often confusing. A more focused and unified presentation of the results is needed.

Essential revisions:

Ansari et al. have now imputed genotype for IFNL4 rs368234815, which controls generation of the IFN-λ4 protein, and IFNL4 rs117648444, a non-synonymous polymorphism that defines a structural variant of the IFN-λ4 protein. Haplotypes comprised of these variants generate different versions of the IFN-λ4 protein. The authors report that variation in the HCV genome and HCV RNA levels associate with these different haplotypes, consistent with previous associations between these functional IFNL4 haplotypes and HCV clearance. This finding is novel and potentially important, as it would provide additional support that the IFN activity of IFNL4 affects the observed phenotype.

This finding raises some additional questions:

Re: the effect of the IFNL4 loci on viral load, does that translate directly to a lower level of viral replication in patients with IFNL4 P70? Might this be investigated from the diversity of the viral quasi-species found in the patient?

Re: the coupling between IFNL4 P70 and S2414 in the HCV genome, is IFNL4 P70 driving selection of a specific amino acid at this position?

In the Nature Genetics paper, IFNL4 rs12979860 associated with 11 amino acid polymorphisms, but now, in a smaller cohort, that SNP apparently associates with 42 sites (both based on a 5% FDR). The authors should explain the reason for that striking difference and comment more generally about how findings from the current paper differ from the previous publication. Similarly, the paper should be clearer on which data and results are original to this paper with previously published data referenced to the Nature Genetics paper.

The value of including the Expanded Access Programme (EAP) subjects is unclear. EAP contributes only ~15% of the total subjects and differs from the BOSON group regarding important demographic and clinical characteristics (sex, prevalence of cirrhosis, HCV RNA levels), as well as genotype frequencies of rs12979860. If EAP subjects are retained in the revised paper, these differences should be considered in the analysis and addressed in the Discussion.

The reviewers have many questions and concerns about the statistical methods and the analyses.

Multiple testing: FDRs of either 5% or 20%, as well as Bonferroni correction are employed. Unless there are compelling reasons for these different approaches (which should be stated), a uniform approach to multiple testing adjustment should be used. The Abstract states rs12979860 genotype associated with 4% of viral amino acid sites across the HCV polyprotein. Based on the discussion (that finding does not appear in the results), this result is based on a 20% FDR, whereas findings presented in the Results (and the previous paper) are based on a 5% FDR. A 20% FDR seems very high and needs to be justified.

Genomic inflation factor for IFNL4 rs12979860 and 500 SNPs with similar frequencies: The genome inflation factor (represented by λ) is used to examine assumptions re: cryptic relatedness when a large set of SNP markers are tested for association with a dichotomous trait in a GWAS (https://www.ncbi.nlm.nih.gov/pubmed/11315092 https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0019416), but it is unclear what is being analyzed here – association of viral variants with a trait (yes or no host SNP)? Are the assumptions about the distribution of viral variants the same as for distribution of host germline variants, for which this approach was developed? This is not a standard approach to test for unaccounted population structure or other biases and the logic for doing this is unclear. Can the authors provide a reference to support use of this method?

A λ value of 2.16 is extremely high and indicates cryptic relatedness, but in this case that statistic is impossible to interpret it because the approach is not described adequately.

Principal component analysis: What is used for PCA in the host? There is no explanation and the plot differs from those used for GWAS, where study samples are plotted in relation to reference populations.

Which viral PCs were included? Were the PCs used as continuous variables in any models? (Note: "principal" is spelled as "principle" in several places.)

Assessment of Confounding, Interaction and Mediation: Assessment as to whether adjustment for potential confounders (e.g. sex, age, study [EAP or BOSON], cirrhosis) is needed. Were genotypes associated with any patient characteristics? E.g. age or cirrhosis status?

Stratified analyses should be performed to identify possible interactions for those variables, especially sex (interaction between IFNL4 genotype and sex has been reported for associations with hepatic fibrosis).

The association of IFNL4 genotype with the frequency of HCV polymorphisms could reflect an effect of IFNL4 on viral replication rates. To assess that possibility, the investigators should compare the results of two logistic regression models: one that does and one that does not include HCV RNA as an additional covariate to IFNL4. Otherwise these paired models should include identical adjustments.

Other comments re: statistical analyses

Subsection “IFNL4 SNP has a widespread impact on the viral amino acids” first paragraph: how was the "expected median" computed?

Subsection “IFNL4 SNP has a widespread impact on the viral amino acids” second paragraph: was does "frequency matched" mean? With the same MAF?

Subsection “Subsection “IFNL4 SNP has a widespread impact on the viral amino acids” first paragraph”, third paragraph: please state outcome variable for the logistic regression models.

Subsection “IFNL4 SNP has a widespread impact on the viral amino acids”, third paragraph: please define FDR and give reference.

Subsection “Statistical analysis”, third paragraph: please state clearly that the SNP was the outcome for the logistic models.

Subsection “Statistical analysis”, eleventh paragraph: To obtain maximum likelihood estimates one needs to assume a normal distribution for log10(viral load) transformed data. IN my experience this assumption is not true for log10(viral load) transformed data. However, least squares estimates do not require this assumption.

Subsection “Statistical analysis”, eleventh paragraph: when a line was fit through the log(OR) estimates, how were the standard deviations of the log(ORs) used? That uncertainty needs to be accommodated.

Other general comments:

The presentation is hard to follow with most data presented as minimally annotated supplementary materials with limited legends provided separately. Providing more detailed legends next to corresponding figures and tables should make it easier to follow.

In the Discussion, the limitations of the study should be explored.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Interferon lambda 4 impacts on the genetic diversity of hepatitis C virus" for further consideration at eLife. Your revised article has been favorably evaluated by Wendy Garrett as the Senior Editor and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Overall, the authors were responsive to reviewer comments and the paper is much improved. The analytical approach remains complicated and the paper is still challenging to read. The authors should consider and address the following comments.

Multiple testing: The authors eliminated use of the Bonferroni correction and a false discovery rate (FDR) of 20%. The paper still presents two different FDR thresholds (5% and 10%) for many analyses and the reason for doing so is unclear. It would be simpler to report a single set of results based on a 5% FDR, the threshold used in the previous publication from this group.

Normality of viral load data: It is not clear from a visual inspection of the Q-Q plot that these data are normally distributed. A P-value for fit would be a more objective measure.

Second paragraph of the Introduction “substitutes a proline for a serine […]”: Terczyńska-Dyla et. al state, “an amino-acid substitution in the IFNλ4 protein changing a proline at position 70 to a serine (P70S) […]”. To this reader, that means a serine is substituted for a proline. Alternatively, the authors might use the language of Terczyńska-Dyla et. al to describe this variant.

Subsection “Host and virus genetic structures”: Without any explanation, it is unclear how to interpret the Bayes factors of 249 and 1.1.

How the patients are divided into IFNL4-null, S70 and P70 groupings could be clearer. Supplementary file 7 would present that information if the groups were arranged together and labeled.

Subsection “Host and virus genetic structures”, ninth paragraph – The co-submission by Chaturvedi et al. has been accepted for publication and might be referenced here.
