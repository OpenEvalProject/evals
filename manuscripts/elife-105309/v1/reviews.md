# Peer review - Round 1

Editors:
- Rosana Collepardo, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.105309.3.sa0](https://doi.org/10.7554/eLife.105309.3.sa0)

This valuable study presents an analysis of evolutionary conservation in intrinsically disordered regions, identified as key drivers of phase separation, leveraging a protein language model. The strength of evidence presented is convincing overall, though the theoretical grounding could benefit from further development.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105309.3.sa1](https://doi.org/10.7554/eLife.105309.3.sa1)

The manuscript by Zhang et al describes the use of a protein language model (pLM) to analyse disordered regions in proteins, with a focus on those that may be important in biological phase separation. This is an interesting study that supports, complements and extends previous related analyses on the conservation and mutational tolerance of disordered regions, with a particular focus on disordered regions in proteins that are found in condensates.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105309.3.sa2](https://doi.org/10.7554/eLife.105309.3.sa2)

This manuscript uses the ESM2 language model to map the evolutionary fitness landscape of intrinsically disordered regions (IDRs). The central idea is that mutational preferences predicted by these models could be useful in understanding eventual IDR-related behavior, such as disruption of otherwise stable phases. While ESM2-type models have been applied to analyze such mutational effects in folded proteins, they have not been used or verified for studying IDRs. Here, the authors use ESM2 to study membraneless organelle formation and the related fitness landscape of IDRs.

Through this, their key finding in this work is the identification of a subset of amino acids that exhibit mutation resistance. Their findings reveal a strong correlation between ESM2 scores and conservation scores, which if true, could be useful for understanding IDRs in general. Through their ESM2-based calculations, the authors conclude that IDRs crucial for phase separation frequently contain conserved sequence motifs composed of both so-called sticker and spacer residues. The authors note that many such motifs have been experimentally validated as essential for phase separation.

Comments on revisions:

Unfortunately my concerns about lack of theoretical grounding and validation (especially critical in lack of theoretical grounding) persist. The argument about correlation between ESM2 scores and MSA conservation is circular. Protein language models already encode residue‑level conservation, so agreement with conservation does not establish new predictive power. For IDRs, conservation is a poor surrogate for function because many functions are mediated by short, degenerate SLiMs that are frequently gained and lost. Sequence‑only predictions therefore need orthogonal (preferably experimental or at the least in silico) tests. Finally, without a family‑level holdout (e.g., cluster de‑duplication at low identity) and prospective tests, overlap with known motifs cannot rule out training‑data memorization/near‑duplicates.
