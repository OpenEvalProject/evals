# Peer review - Round 1

Editors:
- Emmanouil T Dermitzakis, University of Geneva Medical School , Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.00299.014](https://doi.org/10.7554/eLife.00299.014)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for choosing to send your work entitled “Integrative genomic analysis of the human immune response to influenza vaccination” for consideration at eLife. Your article has been evaluated by a Senior editor and 2 reviewers, one of whom, Manolis Dermitzakis, is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewer discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments based on the reviewers' reports.

The manuscript describes a project that aims to integrate genetic, gene expression, and vaccination data, together with immunological traits. The design is innovative and promises interesting discoveries, some of which are described in the submission. Some key concerns were raised that need to be addressed before a final decision can be made:

1) The eQTL discovery was performed in a cohort comprised of males only and the replication was performed in a cohort comprised of females only. What was the purpose of this design? The authors do not address the issue that discovery and replication are confounded by sex.

2) We suspect that an interaction term in the models would actually be more efficient in detecting genetic effects modified by the time point after vaccination. Why was this not used (instead a simple comparison among time points was made)?

3) The fact that there is enrichment in the QQ plots on Figure 6A does not provide evidence about causality of SNPs to vaccine response but simply of correlation among the two effects. More complex models need to be implemented to show causality.

4) The study design used two different array versions: Illumina HT-12v3 and HT-12v4. The authors should describe how they combined data from these arrays, particularly for transcripts where the probe sequence differs between versions.

5) The expression data processing should be described in more detail to make it clear how normalization, and so on, was performed given the different time points, array versions, and discovery/replication cohorts.

6) The authors mention that the person effect within their model would account for differences in cell populations among individuals, given that these are stable within individuals during the sampling timeframe. No data or references are provided to support this claim. Immune cell relative proportions can change rapidly.

7) The authors use the delta r2 metric to identify eQTLs that differ between time points or in response to the vaccination. It seems that the authors could have performed the analysis using the delta of transcription(time point x)−transcription(baseline) as a trait. This normalizes to each individual's starting point. Furthermore, a difference of r2 between time points can have multiple causes (as the authors point out). It seems to us that what they are most concerned with is cases where the effect size (beta) of a given eQTL differs between time points, or where the actual response (transcription time point x−transcription baseline) differs between individuals. The authors reasoning behind these choices should be made clearer.

8) For the trans-eQTL analysis, the authors consider as genome-wide significant any SNP-transcript pair with p<5×10-8. Indeed for a GWAS of common variation, this may be appropriate for a single trait, but the authors should account for testing nearly 10K transcripts.

[After resubmission, the editors also asked for the following comments to be addressed prior to acceptance.]

A) The revision is not satisfactory for point 7, above, on the delta r2. The case is still not convincing because only 146 of the 541 cases were validated. It is not clear why the difference in r2 is necessarily interpreted as a significant change when only 30% of the cases are validated.

B) The modelling as previously discussed in point 3 is somewhat weak and causality is not as well demonstrated, as the authors want to claim. The fact that the association with the residuals is lower than with the original values is not direct but indirect evidence that there are casual relationships. Also, how were the “random” SNPs chosen? Establishing a relevant null is important here. Also, direct causal models would help in establishing the relationships rather than the indirect approach the authors use.
