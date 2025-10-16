# Peer review - Round 1

Editors:
- Howard Y Chang, Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59303.sa1](https://doi.org/10.7554/eLife.59303.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Using AHA labeling approach, the authors reported a one-shot approach by combining RNA-seq, Ribo-seq, and LC-MS. The authors provide evidence that this approach helps identification of translatable lncRNAs.

Decision letter after peer review:

Thank you for submitting your article "One-shot analysis of translated mammalian lncRNAs with AHARIBO" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and James Manley as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: John L Rinn (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Minati et al. reported a method called AHARIBO to detect RNAs with active translation. Using L-azidohomoalanine (AHA) to label nascent polypeptides, the authors purified the translation complex via click chemistry followed by high-throughput analysis including RNA-seq. LC-MS, and Ribo-seq. The authors compared translatome between ESC and differentiated neurons (EN) using AHARIBO and found some long non-coding RNAs (lncRNAs) that could encode peptides.

The overall methodology is straightforward and useful. The authors claim that AHARIBO is able to distinguish ribosome-associated lncRNAs and ribosome-translating lncRNAs. This is indeed an important question in the field since a growing body of evidence suggests that a substantial amount of lncRNAs contain functional open reading frames. Although the title, Abstract, and Introduction primarily focus on this topic, the result section did not serve this goal at all. A revision needs to address the key issues below, as well as temper claims and list the potential limitations and interpretations in a revised Discussion.

Essential revisions:

1) AHARIBO detection of nascent peptide vs. mature protein association with RNA.Nascent peptide capture does seem to offer a new approach to measure translation. The core strategy is not adequately validated, however, and so it is not clear that these techniques are capturing proteins and RNAs through nascent-chain labeling. Further, individual applications of this technique for proteomics or sequencing are not subject to incisive tests that clearly distinguish the proposed nascent chain capture mechanism from alternative explanations. It is in fact unclear if there is a straightforward path to address these central concerns.

a) It is clear that the great majority of AHA label is found in completed free proteins rather than in nascent proteins (Figure 1B). Capture of ribosomal proteins (along with a range of other unspecified proteins) in AHA- controls doesn't exclude the possibility that this (Figure 1D) reflects enrichment of new proteins. In addition to labeling of mature proteins, it seems that only 2- to 3-fold enrichment is achieved in comparison with AHA- samples (Figure 1—figure supplement 1D). This means that a large fraction of captured protein, including captured ribosomes/polysomes - is unlabelled background.

b) Likewise, AHA labeling is often used to measure nascent protein synthesis, much like pSILAC labeling. What is the evidence that the concordance in pSILAC and AHARIBO-nP doesn't simply reflect the labeling of fairly new but completely synthesized protein in AHARIBO-nP lysates?

c) If AHARIBO is capturing nascent peptides, certain strong polarity effects are expected: peptides should be strongly enriched near the N-terminus of proteins relative to the C-terminus. Ribosome footprints should be absent from the first 30 – 40 codons, because these proteins should not expose nascent peptide.

2) Evidence for newly detected lncRNA encoded peptides via epitope tagging. Can the authors express a tagged version (even if ectopically) of some of the newly identified peptides. This would be a complimentary validation to the mass spec performed and provide spatial localization information. For example, the lncRNA TUG1 was recently reported in Cell and Genome Biology to encode a peptide and is highly abundant in both cell types. Cell : DOI:https://doi.org/10.1016/j.cell.2019.05.010) and genome biology: in press, currently: https://www.biorxiv.org/content/10.1101/562066v1. Do the authors find TUG1 translated in these cells (the RNA is abundant in both) that would be another validation of a "validated" new peptide that is larger than 100a.a

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "One-shot analysis of translated mammalian lncRNAs with AHARIBO" for further consideration by eLife. Your revised article has been evaluated by James Manley (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) The validation of TUG1 peptide strengthens the original conclusion. Since TUG1 cannot be identified from AHARIBO, it will be highly desirable if the authors could show any newly identified peptides from lncRNA, i.e., translatable lincRNA that has not been reported before. At least, a thorough discussion about this potential is needed.

2) The puromycin treatment resulted in ~15-20% reduction in AHARIBO signal rather than the >80% seen in ribosome profiling experiments, which implies that a substantial fraction of the AHARIBO signal comes from nonspecific background. Please incorporate text to explicitly address this point – should puromycin treatment always be done to confirm AHARIBO screen hits?
