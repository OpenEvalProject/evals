# Peer review - Round 1

Editors:
- Edward D Janus, University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66921.sa1](https://doi.org/10.7554/eLife.66921.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper will be of considerable interest to researchers studying the interactions between metabolic responses in myocardial infarction. Ultimately this increased understanding of these metabolic responses could lead to exploration of new avenues of treatment.

Decision letter after peer review:

Thank you for submitting your article "Integrative transcriptomic analysis of tissue-specific metabolic crosstalk after myocardial infarction" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Edward D Janus as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tunahan Cakir (Reviewer #2).

The reviewers and Editors have discussed their reviews with one another, and this letter is to help you prepare a revised submission.

Essential revisions:

1. RMetD2 formulation in the reference paper is complex/ difficult to follow. It seems RMetD2 predicts flux ranges rather than fluxes. If so, the definition in the paper is a bit oversimplification, and a more detailed definition should be made. Given that RMetD2 also uses differentially expressed genes to extract the model, it is actually not surprising that the results would match. So I still don't consider it to be an independent validation. RMetD2 in my opinion suffers from various drawbacks because it only uses differentially expressed genes to extract the network. Further, it also seems to strongly rely on fluxes rather than the structure of the genome-scale network. Whether fluxes correlate with expression, is still a hotly debated topic; especially for mammalian cells. Also, it appears that RMetD2 isn't published in any journal but only on biorxiv.

2. Sham operation – Could the authors please detail in the methods section what sham operation entails?

3. Could the authors show the coefficients of the first two principal components – to get an idea of how the gene space changes?

4. The colorbars are not clear throughout the manuscript.

5. The authors are making a model and predicting fluxes. Then, they performed a qualitative validation. Does the output in the section warrant all the effort going into building multi-tissue model? Its possible other computational methods could have done the job much easily. Could the authors show the necessity for building the multi-tissue model?

6. It is not clear to me what is purpose of the model? Models are built to capture the complexity of the problem. While the authors found a number of genes, it is not clear how these genes are producing complexity. The networks that the authors are using aren't clearly explained or delineated or benchmarked. Could the authors do some benchmarking and highlight the complexity of this network?

7. A lot of the analyses in the later part of the manuscript comes across as circular. The authors found some candidate genes implicated in this conditions using transcriptomics data, then they used transcriptomic data to find these DEGs? The validation was done the same way the initial part of the study was conducted. Isn't this biasing the study somehow? Typically, the data types used for validations are different than those for constructing the list of candidates. For e.g. when validating metabolic models of cells built using transcriptomic data, CRISPR-Cas9 essentiality screens are used. Here, they basically repeated the same analyses on the same transcriptome from a different experiment. What is the novel systems biology being learnt here?

8. "Functional analysis reveals widespread" seems problematic in terms of English.
