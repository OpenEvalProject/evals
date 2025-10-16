# Peer review - Round 1

Editors:
- Volker Dötsch, https://ror.org/04cvxnb49 Goethe University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80942.sa0](https://doi.org/10.7554/eLife.80942.sa0)

The authors describe with the newly developed software, ProteInfer, an important new tool that analyses protein sequences to predict their functions. It is based on a single convolutional neural network scan for all known domains in parallel. This software provides a convincing approach for all computational scientists as well as experimentalists working near the interface of machine learning and molecular biology.


---

# Peer review - Round 1

Editors:
- Volker Dötsch, https://ror.org/04cvxnb49 Goethe University Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80942.sa1](https://doi.org/10.7554/eLife.80942.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Deep neural networks for protein functional inference" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Volker Dötsch as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Max Staller (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Outline a better method for setting up a validation set. This should be using the experimental evidence codes: http://geneontology.org/docs/guide-go-evidence-codes/ in some fashion, as those are the proteins for which the function is known. They can enrich the pool by adding close homologs.

2) Separate GO-based analyses to the different GO aspects: MFO, BPO, and CCO.

3) Figure 3: Add baseline methods (BLAST and Naive) to all analyses.

4) The difference between the single ProteInfer CNN and the ensemble ProteinInfer CNNs is unclear. Which one is being used on the website?

5) In addition, please provide more guidance on how to use the "ProteinInfer CNN scaled by Blast Score" model. Are there heuristics for when the scaling is worth the extra effort?

6) Figure S7 shows that combining Blast results with the CNN-Ensemble model was sometimes the best performing model, but it is unclear how the user could use the joint functionality.

7) It would be helpful to add a short paragraph explaining how a wet lab biologist might most efficiently combine ProteinInfer, BLAST, and ProtCNN. For which problems is each best suited? This discussion might be beyond the scope of this work.

8) How does this work differs from existing methods that seem very similar? This should be shown more clearly.

9) Recommendation: report results on highly similar (e.g. >70% identical sequences between validation and training set) and less similar (<70% identity between training and validation) sequences.

10) Recommendation: further integrate ProteInfer with Pfam-N (the ProtCNN model). It would be amazing to have both run in parallel with integrated results.

11) Recommendation: I would suggest moving the comparison of precision vs recall for CNN vs BLASTp from the supplemental material to the main text, as this is a crucial aspect of the study. It would be useful to also discuss or hypothesize why CNN has higher precision at lower recall values, whereas BLAST has higher recall at lower precision values (and especially why precision plateaus if you decrease recall in BLAST).

In the same vein, it would help to motivate the conceptual utility of the high-dimensional embedding for protein sequences, for example by providing functional or phylogenetic insight into a sub-category of enzymes.
