# Peer review - Round 1

Editors:
- Nahum Sonenberg, McGill University , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.01179.025](https://doi.org/10.7554/eLife.01179.025)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Ribosome profiling reveals pervasive and regulated stop codon readthrough in Drosophila melanogaster” for consideration at eLife. Your article has been favorably evaluated by a Senior editor and 3 reviewers, one of whom, Nahum Sonenberg, is a member of our Board of Reviewing Editors.

The consensus opinion of the reviewers is that this study is a thorough, compelling analysis that describes the development of a ribosome profiling assay for Drosophila melanogaster and provides the first genome-wide experimental analysis of stop codon readthrough. The data support most of your conclusions.

The important conclusions are that:

A) Readthrough is more pervasive than expected, and the majority of readthrough events observed were not predicted phylogenetically.

B) The C-terminal protein extensions show evidence of selection, contain functional subcellular localization signals, and their readthrough is regulated, arguing for their importance.

C) The readthrough might regulate gene expression and protein function, and to add plasticity to the proteome during evolution.

However, the reviewers raised several concerns and questions as described below.

1) You note that the locations of ribosome-protected footprint fragments from yeast and human ribosome profiling datasets exhibit 3-nucleotide periodicity from which reading frames can be deduced. Does the fly data provide enough resolution to also show such periodicity? If not, why?

2) The reviewers agree that you need to indicate more clearly the mean level of readthrough you observe with the predicted and novel extensions. You could have discussed this in a couple of places, but you didn't seize upon those opportunities. For example, Figure 5F appears to show that the mean readthrough rates observed range from 1-3%. However, only a couple of rather cryptic references that addressed this point are in the text. In the Results section you state that the human, yeast and fly samples cover similar ranges of efficiency. In the Discussion, you state that the readthrough rates range beyond 10%, while the baseline readthrough is much lower (0.0-1.4%). You need to address the mean level of readthrough more directly in the text since the level of readthrough you observe directly relates to your functional significance arguments in the Discussion. Have you tried to show that one of the newly discovered endogenous proteins has a longer isoform than the predicted size encoded by its corresponding coding region? If not, this needs to be noted.

3) Recent studies have shown that dedicated recycling factors (Rli1 in yeast and ABCE1 in mammals) are required for efficient ribosome release following translation termination. A key concern related to your predicted and novel extensions is whether the ribosomes distal to the stop codon represent translating ribosomes, or simply ribosomes that may not have properly released from the mRNA following termination at the stop codon. In a recent Cell paper (Guttman et al, 2013), a parameter called the Ribosome Release Score (RRS) was used to discriminate between translated protein-coding regions and non-coding transcripts with similar ribosome densities. Could you apply that parameter to the stop codons of the predicted and novel extensions to provide further confidence that you truly represent translated extensions, rather than 3´-UTRs that simply don't release ribosomes? The Guttman paper should be cited.

4) Discussion: You state that readthrough is pervasive, biologically regulated, and functionally consequential, and thus provides an important mechanism to regulate gene expression and function. In light of my concern about the level of readthrough you are generally observing (1-3%), the reviewers think this is somewhat overstating your results. Until you have eliminated one or more of these C-terminal extensions and shown that it results in an adverse phenotype, you cannot say that these extensions are “functionally consequential”.

5) The evolutionary analysis presented near the end of the paper is problematic.

You partitioned the observed examples of readthrough into those that had been predicted by Lin et al. to have signatures of coding conservation (predicted readthrough) and those that didn't (novel readthrough). Then you use three pieces of data to argue that the novel readthroughs are under purifying selection to maintain their coding capacity, and that they are of recent evolutionary origin.

First, you used PhyloCSF to score the novel readthrough, finding that few score positively and that you have the same distribution of scores as non read-through 3'UTRs. You posit that there are only two possible explanations for this - that the novel readthrough are selectively neutral, or that you are of too recent origin to leave a detectable phylogenetic signature. But it is also possible that you have a signature, but it is simply too weak to detect with the model used by PhyloCSF. We come back to this point below.

Next, you compared predicted and novel readthrough, UTRs from non read-through genes, and coding sequence using an algorithm that separates coding and non-coding sequence using nucleotide frequencies, finding that novel readthrough were somewhere in between coding and predicted readthrough on the one hand and non-coding sequence on the other. You note that this is consistent with an “evolutionary trajectory” from non-coding to coding. However, it is also consistent with sequences that simply have weak coding propensity.

Finally, you look at D. melanogaster SNPs to evaluate whether there is a preference for synonymous relative to non-synonymous SNPs in novel vs predicted read-through, finding that there is a weak preference for synonymous SNPs, less than found in predicted SNPs, and say this is consistent with “mild or recently-imposed selection”. This might not be correct. If you have two read-through events – one which evolved at the base of the genus Drosophila, and one along the lineage that separates D. melanogaster from D. simulans/D. sechellia – and posit that these read-through events are under identical selective pressure, then you would expect both to have identical preference for synonymous substitutions, regardless of when you evolved. There is good reason to assume that recently evolved sequences would be under any different strength of selection. If this novel hypothesis were correct, you would probably expect some, if not most, of the novel events to be polymorphic within the population, with some of these in the middle of selective sweeps. But, this would produce a different synonymous vs non-synonymous pattern (with an excess of non-synonymous SNPs perhaps).

It is odd to argue that the majority of read-through events are novel and under selection – something that you'd only expect to find if readthrough events had very short evolutionary half-lives or if there were some reason to have specifically evolved functional read-through events in D. melanogaster.

The data are equally, if not more, consistent with the novel readthrough being subject to weak selection, with their origins unknown. One simple way to resolve this might be to run the Z-score program on orthologous UTRs of read-through and non-read-through genes across the genus. If these are novel to D. melanogaster, their scores should be significantly higher in D. melanogaster.
