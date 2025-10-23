# Peer review - Round 1

Editors:
- Alan M Moses, University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91415.3.sa0](https://doi.org/10.7554/eLife.91415.3.sa0)

This important study addresses the problem of detecting weak similarity between protein sequences, a procedure commonly used to infer homology or assign putative functions to uncharacterized proteins. The authors present a convincing approach that combines recently developed protein language models with well-established methods. The benchmarks provided show that the proposed tool is fast and accurate for remote homology detection, making this paper of general interest to all researchers working in the fields of protein evolution and genome annotation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91415.3.sa1](https://doi.org/10.7554/eLife.91415.3.sa1)

This paper describes a new method for sequence-based remote homology detection. Such methods are essential for the annotation of uncharacterized proteins and for studies of protein evolution.

The main strength and novelty of the proposed approach lies in the idea of combining state-of-the-art sequence-based (HHpred and HMMER) and structure-based (Foldseek) homology detection methods with protein language models (the ESM2 model was used). The authors show that high-dimensional, information-rich representations extracted from the ESM2 model can be efficiently combined with the aforementioned tools.

The benchmarking of the new approach is convincing and shows that it is suitable for homology detection at very low sequence similarity. The method is also fast because it does not require the computation of multiple sequence alignments for profile calculation or structure prediction.

Overall, this is an interesting and useful paper that proposes an alternative direction for the problem of distant homology detection.
