# Peer review - Round 1

Editors:
- Sarah Cobey, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26255.043](https://doi.org/10.7554/eLife.26255.043)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Genome-wide identification of lineage and locus specific variation associated with pneumococcal carriage duration" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Daniel Wilson.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers agree that this is an interesting and novel analysis of an impressive data set. The study sheds light on an important problem in clinical microbiology, the genetic determinants of carriage duration in pneumococcus, and the work should thus appeal to modelers in bacterial genomics and epidemiology. The reviewers find the conclusions fairly convincing and note that the association between carriage duration and the presence of prophage is an especially intriguing result that could inspire future investigations.

The reviewers note, however, the statistical challenges inherent in this type of study. They provide several suggestions for how the statistics could be improved or clarified to carefully delineate the support for different conclusions. An overriding concern is that the limitations of the statistics, and especially the inability of associations to demonstrate causality, be accurately communicated. The reviewers also recommend discussing the potential biology of the phage association in more depth.

Essential revisions and major points:

1) Exploring the inclusion of some components (e.g. serotype, resistance, lineage), but not all components of genetic variation (i.e. the rest of the genome) on phenotype using a Lasso is fairly ad hoc, making it difficult to have confidence in the conclusions. Besides the uncertainty in distinguishing the effects of these loci from others not included, there is also the problem that unmeasured, heritable confounders may influence results, because population stratification may not be adequately controlled. Lasso can make arbitrary choices between approximately equally good variables even if all loci were included, making it good for predicting phenotype, but bad for identifying candidate causal loci. It would be appropriate to mention that in the Lasso analysis, there is less robustness to potential confounding with unmeasured variables that may be associated with the significant regressors. Inferences of causality (e.g. subsection “Serotype and drug resistance explain part of the narrow-sense heritability”, seventh paragraph) are therefore likely to be overstated. For more robust inference, I would suggest testing the significance of these explanatory variables over and above what is explained by, e.g. the top 30 PCs or (better) in a lineage mixed model. If these analyses do not support the same conclusions, that is important to highlight.

2) The authors need to be more careful/speculative in their description of their findings, especially in the Abstract. For example, with respect to the role of host factors, this was far from exhaustive in this study, and there are many more host features, that were the data available could have accounted for more of the phenotype variation, so I believe it is more accurate to state "We estimated that pneumococcal genomic variation accounted for 63% of the phenotype variation, whereas the host traits considered here accounted for less than 5%." (Clearly, the inclusion of epidemiological metadata, if any are available, would enrich the story.)

The second statement in the Abstract that is overstated is 'A pan-genome-wide association study identified prophage sequences as significantly decreasing carriage duration independent of serotype.' Whereas without any evidence of causation, I believe they can only state that they have "identified prophage sequences that significantly associated with decreasing carriage duration independent of serotype." The same idea holds for the association of erithromycin resistance and carriage – the causality is not straightforward. Under the theory of Lehtinen et al. (2017), long durations drive resistance due to the sensitivity of strains with long carriage durations to the fitness effects of antibiotic use, not the other way around.

3) The association of the polymorphic phage with carriage is intriguing and deserves more treatment. Phages likely affect the strain in very different ways, some potentially extending carriage duration with other others decreasing it. Can phages in the database be partitioned into categories based on predicted phenotypic impact and the association retested? What was the genetic polymorphism in the phage genes that associated with carriage duration? How many strains was this in, i.e., was it a large effect in a small number of samples or a small affect in a large number? What was the mean carriage duration for strains with and without it (similar to that shown for serotype in Table 2). Phage often encode specific virulence or immune evasion factors, does this phage carry these? (Ideally a lab-based assay could be performed on the clinical strains to provide some functional information about its potential effect, or a second collection of isolates could be used to validate the finding, but neither is required.)
