# Peer review - Round 1

Editors:
- Andrew P Morris, University of Liverpool United Kingdom

Reviewers:
- Andrew P Morris, University of Liverpool United Kingdom
- Seongwon Cha

## Review text

DOI: [10.7554/eLife.49898.sa1](https://doi.org/10.7554/eLife.49898.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The reviewers appreciated the presentation of results of the meta-analysis of genome-wide association studies (GWAS) of 3D facial phenotypes in large sample sizes across cohorts of European ancestry, with replication in an additional three cohorts of diverse ancestry. The reviewers felt the detailed modelling of the facial phenotypes was a particular strength of the study. The authors identified 24 loci at stud-wide significance, 17 of which had not been previously reported: of these 10 loci were replicated (including six of the novel loci). Subsequent integration of these GWAS results with epigenomic data generated in cranial neural crest cells highlighted enrichment in cis-regulatory elements across the identified loci, and luciferase reporter assays demonstrated enhancer activity of several associated variants. Taken together, the reviewers felt that these data have substantially advanced the understanding of the genetic contribution to facial phenotypes, and have pinpointed potential causal genes and molecular mechanisms underlying facial variation that warrant further functional investigation.

Decision letter after peer review:

Thank you for submitting your article "Novel genetic loci affecting facial shape variation in humans" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Andrew P Morris as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Mark McCarthy as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Seongwon Cha (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Xiong et al. present results of meta-analysis of genome-wide association studies (GWAS) of facial phenotypes across cohorts of European ancestry, with replication in an additional three cohorts of diverse ancestry. The authors identified 24 loci at genome-wide significance, 17 of which had not been previously reported: of these 13 loci were replicated (including 9 of the novel loci). Integration of GWAS results with epigenomic data generated in cranial neural crest cells highlighted enrichment in cis-regulatory elements across the identified loci, and luciferase reporter assays demonstrated enhancer activity of variants in linkage disequilibrium with lead SNPs at three loci.

Essential revisions:

1) Genome-wide significance and replication. Given that 78 traits are tested here, using the traditional genome-wide significance threshold of 5x10-8 seems anti-conservative – some adjustment for multiple traits should be considered. This is even more essential as the replication is not ideal – only one of the three replication studies has exactly the same traits as discovery, and for the other two replication studies, a composite p-value for association with any facial trait is reported. The replication stage also does not take account of multiple testing of 24 SNPs. Only the composite p-value should be reported in replication. The authors could consider a meta-analysis of the p-value across the three replication studies using Fishers' method to give an overall assessment of replication evidence.

2) Elsewhere in the manuscript, "significant" is used, without any report of the threshold for significance (in the Results or the Materials and methods) or appropriate justification: "nominally significant" association with facial phenotypes; "significant" multi-tissue eQTL effects; no justification for p<0.05 in subsection “Preferential expression of face-associated genetic loci in embryonic cranial neural crest cells” and “Cis-regulatory signals in face-associated genetic loci”.

3) Signals of selection. More details of these findings should be reported in the Results section (and shorter comments in the Discussion). Since Fst and iHS are not well powered to detect selection, overlap with singleton density score (SDS) results in Europeans should be reported (Field et al., 2016).

4) Selection of "candidate regulatory SNPs" is not clear. The authors highlight SNPs that are in LD with the lead SNP at some loci. However, tag SNPs with r2 of 0.3 with the lead SNP do not seem to be in strong LD, and they may not actually show a strong association with the facial trait for that locus – as a result, the fact that the authors demonstrate enhancer activity for this SNP is irrelevant, as it will not be a good candidate to be driving the association signal. It also wasn't clear where the 5 SNPs came from, since 7 are reported in the preceding text. A better approach would be to define 99% credible sets of variants at each locus, which account for 99% of the probability of driving the association, and then assess the evidence for regulatory activity for these.

5) Multivariable modelling of phenotypes. The authors have considered all SNPs at genome-wide significance, and then LD pruned to a set of independent SNPs (r2<0.5). This does not define SNPs with independent effects on the phenotypes. The authors would be better to actually condition out the effects of the 24 lead SNPs by including them as covariates in the model, and then identify SNPs that remain at genome-wide significance. This could be done in exactly in RS, or could be done through approximate conditional analysis implemented in GCTA.
