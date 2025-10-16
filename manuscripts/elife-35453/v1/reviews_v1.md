# Peer review - Round 1

Editors:
- Richard A Neher, University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35453.044](https://doi.org/10.7554/eLife.35453.044)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: the authors were asked to provide a plan for revisions before the editors issued a final decision. What follows is the editors’ letter requesting such plan.]

Thank you for sending your article entitled "Long read sequencing reveals poxvirus evolution through rapid homogenization of gene arrays" for peer review at eLife. Your article is being evaluated by three peer reviewers, and the evaluation is being overseen by Richard Neher as the Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers discussed your manuscript at length and one critical issue came up.

Sasani and colleagues use long read nanopore sequencing to characterize pox virus populations from cell culture evolution experiments. In these experiments, poxviruses adapt initially by amplification of the target gene or by a point mutation. The central claim of the paper is that the point mutation subsequently spreads among amplified gene arrays via a gene-conversion like mechanism. This is an intriguing possibility and long read sequencing seems in principle well suited to characterize this complex evolutionary dynamics. However, the evidence presented is also compatible with the following more parsimonious explanation:

The initial response of the virus population is gene amplification and the rise of single copy mutant genes. Once the latter are common, it becomes likely that they undergo gene amplification as well resulting in multi-copy mutant arrays. These homogeneous mutant arrays than gradually replace the WT arrays. This mechanism explains the homogeneity of the arrays and their late dominance via processes we already know to be common in this system without the need to invoke gene conversion. We failed to identify evidence in the data you presented that favors gene conversion over this simpler mechanism, especially given the high error rate of nanopore sequencing.

Given this critical issue, the editors and reviewers invite you to respond within the next two weeks either with existing data/explanations in favor of gene conversion, or suggestions for experiments/analyses that would decisively answer this question. We plan to share your responses with the reviewers and then issue a binding recommendation.

[Editors’ note: formal revisions were requested, following approval of the authors’ plan of action.]

Thank you for submitting your article "Long read sequencing reveals poxvirus evolution through rapid homogenization of gene arrays" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Richard A Neher as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Sasani and colleagues use long read nanopore sequencing to characterize pox virus populations from cell culture evolution experiments. The central claim of the paper is that pox virus achieves immune evasion initially by either amplification of the target gene or a point mutation. Subsequently, the point mutation spreads among amplified gene arrays via a gene-conversion like mechanism. This is an intriguing possibility and long read sequencing is well suited to characterize these complex evolutionary dynamics.

Essential revisions:

Sasani et al., have already responded to our most serious concern, an alternative mechanism via amplification of mutant alleles, and their additional analyses provide convincing evidence that this simple mechanism can be ruled out. We would like these analyses to be included in the manuscript and have a number of additional essential points that need to be addressed:

1) Statistics on the arrangements of alleles in multi-copy arrays. How often are different patterns AAAAA, AABAA, ABBAB, etc. observed? Do identical alleles tend to be neighbors or are they randomly distributed? Are specific subpatterns over-represented across 3,4,5 copy arrays? These statistics should be used to explicitly discuss the plausibility of different scenarios and ideally quantitatively model the dynamics across time. Simply showing examples/pictures and stating that this result is "compatible" with your hypothesis is not enough. For follow-up analysis, it would be useful to provide alignments of 1, 2, 3, 4, 5, copy arrays such that readers don't have to go back to the FASTQ files (maybe after stripping non-reference insertions that are likely ONT errors).

2) Recombination and MOI: Viral titer will increase dramatically during the 48h experiments and there is, therefore, no single MOI for any experiment. Furthermore, even experiments started at low MOI likely have high MOI towards the end. Subsection “Recombination and selection drive patterns of K3LHis47Arg homogenization” should explain these caveats and discuss carefully the degree to which inter-genomic recombination can be ruled out. Statistical signatures of WT/mutant patterns in the multicopy arrays might help to differentiate such patterns (cross-over recombination might result in mutant copies being preferentially at the 3' or 5' end of the array).

Qin and Evans, 2014 provide careful estimates of pox virus recombination rates. In particular, they find short recombination tract length (that look like gene conversion) and frequent recombination even though experiments start at MOI 0.02. This further calls into question your assumption that little inter-genomic recombination is happening.

If inter-genomic recombination is common, the observed patterns could be explained by non-allelic homologous recombination that results in frequent deletion, concatentation, and replacements of arrays or parts thereof.

3) ONT error rates. A detailed analysis of sequencing errors needs to be part of the manuscript. It would be useful to indicate the ONT error threshold in Figure Figure 2B. How does one reconcile the fact that ONT finds 10% mutant alleles in P5 while these are not detected in Illumina reads?

4) An effort should be made to clarify the logic of the manuscript. The reviews below highlight problems and provide a number of concrete suggestions to improve the manuscript.

5) "Homology" is used incorrectly: homology is a binary quality. Two sequences either share a common ancestor (are homologous) or they don't. You use homology as a synonym for similarity, which it is not (see https://www.ncbi.nlm.nih.gov/books/NBK20255/).

6) Better graphs: bar graphs are a sub-optimal way to present data in many cases. In Figure 1A/D, for example, please show all data points and the median, there is no need for the bars. Figure Figure 1—figure supplement 1 is even worse - all the relevant differences happen within 10% of the figure. Figure 2C might be better as line graph with copy number as x-axis and one line per passage. We would like to see graphs and statistics that explicitly show the WT/mutant arrangements in multi-copy arrays with more information than the current Figure 3 and Figure 4. Overall, quantitative analysis and presentation of the data should be improved.

Finally, you need to be careful not to overstate your case: Evidence for gene conversion remains indirect (experiments with mixtures of viruses recoded at synonymous positions might provide more direct evidence), the importance of this process in the real-world pox-virus infections remains speculative, and other mechanisms to homogenize the array can't be ruled out.
