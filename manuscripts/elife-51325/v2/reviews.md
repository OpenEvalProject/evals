# Peer review - Round 1

Editors:
- Marianne E Bronner, California Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51325.sa1](https://doi.org/10.7554/eLife.51325.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this interesting paper, the authors identify a set of zebrafish periderm enhancer candidates and use the same methods to identify enhancer candidates in mouse palate epithelium and human oral epithelium cell lines, and then trained a machine learning program (gkm-SVM) on these data sets to identify likely OFC-associated SNPs near the KRT18 gene, which they functionally tested in reporter assays. The results reveal many important periderm enhancer as well as useful methods for enhance validation.

Decision letter after peer review:

Thank you for submitting your article "Analysis of zebrafish periderm enhancers facilitates the identification of a regulatory variant near human KRT18" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Marianne Bronner as the Senior and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alice Goodwin (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Essential revisions:

The reviewers are overall positive but I ask you to discuss the points raised in the individual reviews below, If you are unable to perform the experiments proposed in point 1 of reviewer 2, please discuss whether the snp is expected to alter the binding of a transcription factors. As to the reviewer's second major point, please respond to the point raised.

Reviewer #2:

The data is extensive and the authors do a nice job of integrating their data, including with other data sources. The work on defining periderm enhancers is impressive and very useful for the field. Certainly, parts of this paper confirm previous findings, but it also points to potential new regulators of periderm. The paper does identify a new disease-related SNP in a periderm-related disease. Overall, the paper makes a significant enough advancement.

1) The overall logic is that the definition of zebrafish periderm enhancers is useful for identifying functional SNPs in human periderm-related disease. This is possible despite the limited enhancer conservation from zebrafish to humans because the key transcription factors and overall regulatory logic is better conserved than overall enhancer sequence and because SNPs in regulatory regions disrupt binding of these key transcription factors. In the paper, the authors identify SNP2 near the keratin 18 gene as functional. The approach would be better supported if there was some analysis of which transcription factor(s) might be binding or not binding to SNP2. Also, the prediction would be that this human regulatory region would mediate periderm expression in zebrafish and that this expression was sensitive to the disease variant of SNP2. Was this tested?

2) Given that the machine learning algorithm trained on zebrafish data had a very high false positive rate for predicting periderm enhancers, it seems surprising to me that using that data then for analysis of human enhancers would be very useful. This is compounded by the fact there is no enhancer data on human periderm, leading the authors to use data from cells and cell lines from diverse sources to validate their approach. My worry here is that with the multiple cell lines, some with limited relevance, the authors can show pretty much what they like to show. The authors try to address this by linking the 0.1% top bin scoring tiles with gene expression from mouse periderm, but while the p-value may make a significance cutoff, this does not seem entirely convincing. Of note, the IRF6 enhancer element selected for study by the authors does not make it into the 0.1% top bin scoring tiles. Because of these concerns and the concerns in #1, the generality of the authors' approach for identifying functional disease SNPs in humans is not entirely convincing.

Reviewer #3:

I believe this work is of interest in that it proposes a high throughput method to identify potential functional OFC-associated SNPs. The focus of this article was training on periderm tissue, however, the methods may also be applied to other tissues involved in craniofacial development.
