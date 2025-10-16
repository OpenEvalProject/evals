# Peer review - Round 1

Editors:
- Emmanouil T Dermitzakis, University of Geneva Medical School , Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.04729.027](https://doi.org/10.7554/eLife.04729.027)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “The Genetic Architecture of Gene Expression Levels in Wild Baboons” for consideration at eLife. Your article has been favorably evaluated by Aviv Regev (Senior editor), a Reviewing editor, and two reviewers, one of whom, Stephen Montgomery, has agreed reveal his identity.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

Please find below a summary of the comments of the reviewers that we request that you address in your revised manuscript:

Figure 1 and 3 should not be main figures. The pipeline should be moved to the supplement. Also the ASE and eQTL effect sizes is a general technical issue and does not relate specifically to the study of the genetics of gene expression in baboons. The text around these sections is long and generally distracting.

There is a comment regarding the lack of an association between effect size and minor allele frequency compared to Battle et al., 2014. However, Battle et al. had 922 individuals compared to 66 individuals here (among several technical differences). We are not sure that these studies can be easily compared to provide a definitive statement regarding negative selection in baboons here. A caveat regarding study differences might suffice.

The authors bring up the possibility of admixture in the baboon population. This is slightly concerning as it could increase the number of hets and has the potential to increase the length of haplotypes (both observations of the study). It further could explain many of the observations of the study. Three possible suggestions to address this are to test whether: (i) one sees an excess of trans-associations on the same chromosome compared to across chromosomes for cis-eQTL in baboons versus YRI, (ii) apply a surrogate variable or hidden factor correction to eQTL analysis on a single chromosome or (iii), our reviewers’ favorite, test if ASE is correlated over a longer distance (more independent genes) than in humans—in this case, since there is no biological basis for why the locations of causal variants should be further away from the genes they regulate between baboons and humans, the decay of the correlation of ASE measured in proximal genes should be similar. We realize the authors have a model to control for individual relatedness and population structure, but this is derived from the entire genetic data set and does not address local patterns of admixture.

The gene expression data was quantile normalized. Why was a hidden factor correction not applied? Typically, these types of corrections dramatically improve eQTL discovery. Our concern is if there is some structure to the data that is both present and correlated in genotype and gene expression space, the number discoveries will be artificially inflated.

For ASE analyses: (i) the authors assume no recombination, this is not stated, (ii) how is beta in theta∼beta (alpha, beta) estimated, and (iii) detection of ASE correlates with expression level (Figure 3D), this is not a surprise, but given their model we are concerned whether this estimate is more extreme, because ASE has different variances in effect size when it is estimated from a few individuals for very highly expressed genes (2 het individuals with 150 reads = 300 total) compared to lots of estimates from intermediately expressed genes (10 het individuals with 30 reads = 300 total). For robustness, the authors should show whether detection of ASE in their study is independent of the number of input individuals once a testable site has been selected using their criterion.

The authors should discuss the possibility that the negative correlation between conservation and probability of eQTL in a gene in baboons at least may be driven by the technical issue that only coding SNPs were tested and therefore conserved genes will tend to have low MAF and therefore low power.

The authors indicate a large component of expression variability is in trans. Is trans defined as on other chromosomes? In particular, the authors should clarify what goes into the ptrans matrix.
