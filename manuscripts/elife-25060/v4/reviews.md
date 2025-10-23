# Peer review - Round 1

Editors:
- Mark McCarthy, Oxford University United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25060.032](https://doi.org/10.7554/eLife.25060.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Genetic Identification of a Common Collagen Disease in Puerto Ricans via Identity-by-Descent Mapping in a Health System" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Mark McCarthy as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision letter to help you prepare a revised submission.

Summary:

The eLife editorial team finds your submitted research paper of considerable interest: it provides an excellent example how a large and clinically well characterised cohort with special population history can provide improved power to find novel rare mutations and haplotypes linked to Mendelian syndromes. Furthermore, the presented analytical strategy improves our understanding of already reported pathogenic mutations by efficiently increasing the number of variant carriers and finessing the resulting clinical picture.

The various contributors to the eLife Editorial team (reviewers, Reviewing Editor, Senior Editor) have raised some questions about aspects of the statistical and methodological approaches, and identified some weaknesses in the methods description, reported sample sizes and in referencing to tables and figures. Furthermore, we felt that some aspects of the work, like IBD detection, need to be explained more effectively to non-expert eLife readers.

Below, we provide a condensed list of Essential Revision actions that we consider need to be addressed in any revised submission.

Essential revisions:

1) Aspects around IBD – Please provide a more thorough description on the IBD methodology used. We'd recommend starting with a more general description of IBD and its role in causal mutation detection – currently the text is drafted in a manner that almost assumes the reader is very familiar with IBD analysis. Please explain specific terms, like "local ancestry".

Second, please justify the use of 3cM in IBD mapping. Third, provide more details in "Materials and methods" on how IBD cliques were identified and QCd.

2) Aspects around Statistical Methods – Currently, the manuscript lacks clarity on exactly which statistical models were applied to the data.

First, be specific about the regression models referred to in paragraph two of subsection “Detecting a Locus Shared Identical-by-Descent Underlying Extreme Short Stature in 172 Puerto Ricans” – have you modelled the zscore as a function of the number of copies (0, 1, or 2) of the haplotype in a specific clique?

Second, the initial analysis of cliques relied on permutation to evaluate significance. Then when restricting analysis to Puerto Rican ancestry subjects (paragraph three of subsection “Detecting a Locus Shared Identical-by-Descent Underlying Extreme Short Stature in 172 Puerto Ricans”) and 480 cliques w/ at least 3 people, are you using significance evaluated from asymptotics? Why the change in methodology? Bonferroni thresholds are mentioned, correcting for how many tests?

Third, the analysis of ICD9 codes vs. genotype at COL27A1.pG697R – we assume you did 416 different logistic regressions, coding each subject as yes/no for a particular ICD9 diagnosis – this could be made more clear. Was any correction done here for 416 tests? While the significance values are impressive, we concerned about inflation due to case-control imbalance.

Fourth, please repeat ICD9 codes vs. genotype at COL27A1.pG697R association testing using Firth test. It appears that many of these dx categories are quite rare, as is the variant. Logistic regression with case-control imbalance results in serious inflation of test statistics, particularly in the case of rare variants (see Ma et al., 2013 Genetic Epidemiology).

3) Power of IBD mapping – First, currently no power calculations are presented to substantiate the claim that the IBD mapping approach outperforms GWAS in terms of power. Please present these calculations as the p-value yielded through 10,000 permutations is only p=0.0018, which is substantially less than a GWAS significance threshold. Second, please clarify if the COL27A1.pG697R variant is imputable with 1000 Genomes reference. In the Materials and methods section, you provide detailed description on imputation. Furthermore in paragraph two of subsection “Fine-mapping Short Stature Locus Reveals Putative Link to Mendelian Syndrome” it states that there was 96.7% concordance between variant genotype and the associated haplotype – so wouldn't the GWAS have identified the association using the variant?

4) Genetic ancestry and COL27A1.pG697R variant – Currently the text is lacking detailed description of the pathogenic variant. Furthermore, more detail is essential to understand how partitioning into ancestry groups was performed.

First, in the functional analysis section (subsection “Functional Investigation of COL27A1.pG697R”). Is the variant predicted damaging by popular annotation tools?- polyphen, sift, cadd, gerp, mutation taster, phyloP etc.

Second, please provide a confidence interval for the dating of the variant, (around 36 generations).

Third, please provide exact criteria how ancestry groups were defined from PCA vectors. Such details are currently missing from the Materials and methods. Furthermore, please provide clear evidence that suggest the populations that are described in subsection “Local Ancestry Estimation” present Native American are not admixed for European ancestry, or at least not significantly so.
