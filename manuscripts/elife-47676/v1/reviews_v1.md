# Peer review - Round 1

Editors:
- Antonis Rokas, Vanderbilt University United States

Reviewers:
- Rama Ranganathan, University of Chicago United States
- Itamar Sela, National Institute of Health United States
- Luke Wheeler, University of Colorado Boulder United States

## Review text

DOI: [10.7554/eLife.47676.026](https://doi.org/10.7554/eLife.47676.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "ASPEN: A methodology for reconstructing protein evolution with improved accuracy using ensemble models" for consideration by eLife. Your article has been reviewed by peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Rama Ranganathan (Reviewer #1); Itamar Sela (Reviewer #2); Luke Wheeler (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The study by Sloutsky and Neagle addresses the important problem of how to make good models of the evolutionary history of a protein family given extant sequences. This is a topical, important, and interesting problem, especially given the growing use of sequence databases for understanding the function and evolution of proteins. Protein sequences diverge through two processes that must be distinguished in making an accurate model of their history: speciation events which lead to orthologous sequences and duplication/divergence events that lead to paralogous sequences. The manuscript presents a meta-algorithm, ASPEN, that improves phylogenetic inference of protein families by subsampling sequences and constructing a topology which is supported by subsampled trees. Sampling alignment columns is a common practice which is used to assign bootstrap support values to phylogenetic trees splits, however, in this work the sampling is performed over rows (i.e. sequences). Notably, there is a correlation between "accuracy" (inferred topology quality) and "precision" (statistical support of inferred topology), as defined in the manuscript. Subsampled topologies are incorporated into a subtle branch-to-bound procedure, to construct topology that is statistically supported by many subsamples, rather than a single all-sequence alignment. The resulting constructed topology is shown to be more accurate than all-sequence based topology using a simulated dataset. The developed meta-algorithm will be of considerable interest for scientists that study evolution of protein/gene families and represents an advance in the effort to improve phylogenetic reconstruction by accounting for uncertainties in inference algorithms.

Essential revisions:

1) A key general point here is the real difficulty of actually inferring the true specific sequence of mutational events that underlie branches in an evolutionary tree. A very important and insightful concept that is partially expressed in this paper is to question the relevance of wanting to know that information from a point of view of deducing any principles of molecular evolution. The idea that the most invariant aspects of the tree reconstruction are simultaneously the most accurate is interesting and sensible, but isn't what is being proposed here that they are also the most relevant? If so, then this should be discussed and defended in more detail in the conclusions. In this same theme, what do these results mean for the whole community using ancestral reconstruction to infer epistasis along branches of the inferred trees and using such studies to extract principles of protein evolution? And for the interesting claims to having "resurrected" true ancestral states from all-sequence tree reconstructions? More generally, some discussion of what can be claimed and what cannot in reconstruction-based studies given the advances presented here about accuracy and precision in the process of these reconstructions would be valuable to guide the scientific community.

2) Analyses summarized in Figure 2 (and is also related to Figure 5). Figure 2A suggests that low accuracy topologies result from poor alignments, and are not due to failure of the tree reconstruction algorithm to retrieve the optimal topology for the given alignment. This can be tested directly by analysis of alignments quality. Moreover, since the quality of the inferred tree depends to a large extent on the quality of the alignment, such an analysis can provide a simple explanation for the observed correlation between accuracy and precision. We suggest that you compare the agreement of all-sequence and true alignments in several accuracy bins, as well as perform comparisons of subsampled alignments between themselves and to all-sequence and true alignments.

A plausible explanation for the accuracy-precision correlation is that different accuracy bins represent different levels of alignment problems complexities. Low complexity alignments are robust with respect to subsampling and are therefore associated with high precision. Complex alignment problems might produce very different subsampled alignments that result in different inferred topologies and low precision. Analysis of the alignments quality can directly support or disprove this hypothesis and better isolate the source of low accuracy (poor alignment or poor topology inference given the alignment).

Questions about how different scenarios might affect the efficacy of the ASPEN approach.

3) As noted in the paper, the simulated trees have a fixed number of paralogs. There are no new gene duplications that occur from the oldest ancestral state to the end-state used for reconstruction. How will variability in this feature in real biological trees effect the ASPEN reconstructions? What is the minimum number of "high confidence nodes" that one needs to make this work?

4) We wonder about using JTT model (or another similar amino acid substitution matrix) to conduct the simulated evolution, because it assumes independent evolution of each site/column. Real proteins will have epistatic interactions due to physical and functional constraints. Does this added complexity change the relationship between precision and accuracy or have some other effect on the efficacy of ASPEN? For example, will there be a deviation in the precision vs. accuracy curve for real proteins (like LacI in this study) relative to simulated proteins, that wouldn't be detectable without knowing the true model?

Question about software.

5) We were pleased with the availability of data and materials used in the paper via online repositories. One thing that would be very beneficial, though not necessary for publication of this article, is a thorough documentation of the ASPEN software that the authors have implemented. It will be difficult for any would-be users to dissect how the software functions without documentation. What are the authors' plans regarding providing documentation for the software?
