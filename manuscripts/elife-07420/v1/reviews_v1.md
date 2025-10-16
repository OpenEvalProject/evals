# Peer review - Round 1

Editors:
- Irwin Davidson, Institut de Génétique et de Biologie Moléculaire et Cellulaire , France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07420.002](https://doi.org/10.7554/eLife.07420.002)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “Registered report: Oncometabolite 2-Hydroxyglutarate Is a Competitive Inhibitor of α-Ketoglutarate-Dependent Dioxygenases” for peer review at eLife. Your submission has been favorably evaluated by Michael Marletta (Senior editor), Irwin Davidson (Reviewing editor), and four reviewers.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission. The reviewers of this paper have raised several issues and we would ask you to specifically take into account the comments concerning the statistical analyses.

Summary:

The article outlines the detailed protocol to reproduce a report published in Cancer Cell linking mutations in IDH1/2 to cellular levels of Ketoglutarate and changes in histone and DNA methylation. This initial work had a major impact on linking metabolites to chromatin, but also raised a number of questions that justify a rigorous replication.

Overall, the proposed study covers the major aspects with the required detail and rigour.

Specific points to address are:

1) The referees suggest that the authors consider using mass spectrometry to measure 5hmC in addition to immune dot-blot. Mass spectrometry is a more quantitative measure and while it would go beyond replicating the published findings it might give a clearer answer.

2) In protocol 1 a 2-way ANOVA is proposed, however as 2 quantitative variables are measured and there is only one qualitative factor (with three possible values) influencing these measures, an MANOVA would be more suited.

3) There may be confusion between groups and variables in setting the degrees of freedom for ANOVA analyses. In protocol 1, how was (2, 6) obtained? The same question applies to protocols 3, 4 and 5.

4) In addition to t-tests for the comparison of means where both variances are equal, F-tests should be added when variances are significantly different.

5) Referees raised concerns about null variances that appear in the power calculation tables. Although these values are not always available, variance values can change the conclusion of the tests. When variances are not available, preliminary experiments in order to estimate them are proposed. More generally, variance values used in this paper are estimated from published figures using a low number of replicates, so they are not robust. A way to increase robustness would be to increase measured values by a pre-determined factor and then relax the expected power if too many replicates are required.

Also, non-rounded computed sample sizes are requested to have an idea of how close we are to the theoretical value after rounding.

6) For protocol 2, in subsection “Confirmatory analysis plan”, a MANOVA is proposed, whereas a one-way ANOVA is suggested for the same protocol in subsection “Test family”. Please correct this inconsistency.

7) Protocol 5: a mean across several groups is compared with the mean of a single group. This should not be done with a simple t-test to take into account the fact that the number of measures is different in the two groups being compared.
