# Peer review - Round 1

Editors:
- Volker Dötsch, https://ror.org/04cvxnb49 Goethe University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82556.sa0](https://doi.org/10.7554/eLife.82556.sa0)

This study applies AlphaFold to the CHESS selection of transcripts with the goal of generating predicted 3D protein structures and a quality measure of folding, the pLDDT score. From these data, the authors build a database for result exploration, documented by several examples, including proteins, where the authors propose the pLDDT score as a measure of presumed superior biological functionality over other isoforms. These results will be highly relevant for anyone working with proteins that occur in different isoforms.


---

# Peer review - Round 1

Editors:
- Volker Dötsch, https://ror.org/04cvxnb49 Goethe University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82556.sa1](https://doi.org/10.7554/eLife.82556.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Structure-guided isoform identification for the human transcriptome" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Volker Dötsch as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Anna Poetsch (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Using the representative isoform from the MANE database the authors provide 5 exemplar genes whose MANE representative isoform when translated yields a protein structure with a lower pLDDT score than a non-representative isoform, suggesting that the protein stability of the representative isoform is suspect. The authors clearly explain that not all isoforms encode a well folded functional protein. Thus, it would be helpful for the authors to provide a clearer indication of how common the non-exemplar representative isoforms in the MANE database may have a lower pLDDT score. Armed with this a false positive and negative estimate could be provided.

2) The authors evaluate the single representative isoform selected for each human protein coding gene in the MANE database. In addition, the authors provide a list of isoforms with the highest pLDDT score for each human gene. However, it would be useful for the authors to provide a section that speaks to the confounding conditions and sequence features are understood to be confounding in evaluating the use of pLDDT scores. For example, since evolutionary conservation and synteny considerations of isoform sequences are an important consideration in evaluating the potential utility of an isoform, what would the authors recommend if the pLDDT scores are elevated but one or more of the other considerations are less than ideal?

3) The study is based on the elegant idea to aid genome annotation through 3D structure prediction. This is a very powerful approach that allows large-scale data generation for functional interpretation. This approach appears technically sound and well executed (although I may miss details not being a protein expert). However, in my opinion, the authors could make more use of the potential of their approach. From the big-data start, they seem to directly restrict themselves to interesting examples. I am missing a global analysis that shows the bigger picture of their results. Given that they have generated structures from 90,415 isoforms, each associated with a pLDDT score, conservation scores, length, expression levels and other quantifiable data listed on page 18. I would wish for a comprehensive analysis of these data and their potential before applying the focus on a few (admittedly very nice) examples.

4) One of the weak spots of such an analysis is the relationship between foldability and functional relevance. Disordered regions would imply reduced relevance due to poor pLDDT scores, which may be a misleading conclusion. While this may be a problem difficult to solve with this approach, it still needs to be addressed and discussed throughout the paper and particularly as part of the global analysis, not just in the context of examples.

Reviewer #1 (Recommendations for the authors):

The manuscript is well written and speaks to an important and timely issue concerning the number how to annotate and evaluate isoforms for each gene. As the number of isoforms for a genome continues to increase it will be helpful to provide some logic to distinguish among the isoforms.

Using the representative isoform from the MANE database the authors provide 5 exemplar genes whose MANE representative isoform when translated yields a protein structure with a lower pLDDT score than a non-representative isoform, suggesting that the protein stability of the representative isoform is suspect. The authors clearly explain that not all isoforms encode a well folded functional protein. Thus, it would be helpful for the authors to provide a clearer indication of how common the non-exemplar representative isoforms in the MANE database may have a lower pLDDT score. Armed with this a false positive and negative estimate could be provided.

The authors evaluate the single representative isoform selected for each human protein coding gene in the MANE database. In addition, the authors provide a list of isoforms with the highest pLDDT score for each human gene. However, it would be useful for the authors to provide a section that speaks to the confounding conditions and sequence features are understood to be confounding in evaluating the use of pLDDT scores. For example, since evolutionary conservation and synteny considerations of isoform sequences are important consideration in evaluating the potential utility of an isoform, what would the authors recommend if the pLDDT scores are elevated but one or more of the other considerations are less than ideal?

Finally, the authors are encouraged to provide readers with a reasoned argument that the addition of structure-guided isoform considerations is more than an incremental advancement in the annotation of the human transcriptome.
