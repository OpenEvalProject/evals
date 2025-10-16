# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.04745.021](https://doi.org/10.7554/eLife.04745.021)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “RNA chaperones buffer deleterious mutations in E. coli” for consideration at eLife. Your article has been favorably evaluated by Detlef Weigel (Senior editor), a Reviewing editor, and two reviewers.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments.

The conclusion of the paper is highly interesting: that RNA chaperones may buffer mutations that could impact on mRNA folding. The possible implication is that this way hidden genetic variability can be maintained in the genome and become effecting under certain (e.g. stress) conditions by compensating the function of RNA chaperones, e.g. by over-loading their functions. This role of chaperone was previously reported and extensively discussed in the context of protein mutations, but not in the context of RNA mutation.

Stronger evidence that this is indeed the case, however, is required. The main issue raised is that the mutations described were not characterized in the context of RNA stability. Therefore, it is difficult to interpret the experiment. If you decide to submit a substantially revised version of the manuscript, a minimal set of experiments required to better support your conjecture has to include: (1) the identification of at least one mutation in the original strain predicted to affect RNA stability (using computational tools), (2) the demonstration that it has a detrimental effect on fitness when in isolation, and (3) evidence that it is being buffered by RNA chaperones.

Additional comments:

1) Given the overall conclusion of the work, that overexpression of RNA chaperone proteins confers a fitness benefit by assisting with RNA folding or structural rearrangements in the mutated strains, it seems important to evaluate whether any of the mutations in known or suspected structured RNAs. This question is especially intriguing for the ΔmutH because it has such a small number of mutations, and all of the SNPs are in coding sequence. This could be done computationally.

2) The data presentation does not allow a direct comparison, but the impression upon comparing parts B and C of Figure 1 is that, upon over-expression of some DBRHs , the evolved 40k strain grows faster than the ancestral strain (RhlB and CsdA; or the latter and SrmB, in Figure 2). Is that the case? If so, how can this be accounted for?

3) Fitness was determined by competitions: cultures were grown for 24 hours, as default. It's unclear to which growth phase the fitness effects relate to: is it most exponential growth, or stationary phase as well. Further, given the different growth rates of the different strains, it could may well be that some were subjected to growth only and other to growth + stationary phase survival. Many, I'd say, most mutations have conflicting effects on growth vs. survival in stationary phase. It could therefore be that the actual buffering effects would be different, possibly much larger, if competitions were perfumed under a defined phase—exponential growth on one hand, and survival at stationary phase on the other. This should be clarified by performing competition experiment in well-defined conditions (e.g. maintaining cells in log phase).

4) “Relative fitness was calculated as the ratio of the competitors' growth rates during competition.” The method relates to counting the ratio of CFUs on tetrazolium plates, so how would growth rates be derived from that; especially, when no data is available as number of generations within the 24 hours growth (or growth phase, see above)?

5) “The arabinose-utilization marker, which is neutral under the conditions utilized”. Was this tested, or assumed? Many markers do affect growth rates.

6) An empty vector control is missing.

7) The supplementary tables listing the mutations are not very informative. The genes and positions of the mutations should be specified.

8) The expression levels of the RNA chaperones are not reported. It is interesting that overexpression of CspA restores fitness to the same level as overexpression of the ATP-dependent DEAD-box proteins, but this result cannot be fully evaluated without knowing whether the different proteins were expressed at comparable levels.

9) The sentence: “RNA chaperones can promote orderly structural transitions towards and subsequently stabilize the native fold or—as exemplified by classic work on the Neurospora crassa CYT-19 protein—facilitate the re-folding of misfolded species (reviewed in Bogumil, 2010).” This reference seems to be incorrect here.

10) In the subsection headed “Mutant proteins”, the sentence: “Here, we used DBRH mutants in which the central glutamic acid residue has been recoded to yield lysine, a change known to abolish RhlB helicase activity (Vanzo, 1998).” In Vanzo, 1998, helicase activity was not measured. Instead, it was shown that RNaseE-dependent ATPase activity is compromised for this mutant. It is certainly expected that the mutation will also result in a loss of helicase activity, which depends on ATPase activity, but the connections to previous work should be clarified.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “RNA chaperones buffer deleterious mutations in E. coli” for further consideration at eLife. Your revised article has been favorably evaluated by Detlef Weigel (Senior editor), a Reviewing editor, and two reviewers. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

As you can see from the reviews, both reviewers appreciated the additional data and discussion provided in the revised manuscript and agreed that the paper is improved. There is also an agreement that you nicely illustrated the core finding—that the slow growth phenotypes of these strains can be rescued with overexpression of DEAD-box proteins, known RNA-dependent ATPases (and one RNA-binding protein that lacks ATPase activity)—and that this finding is interesting.

However, both reviewers also agreed that the mechanism(s) of rescue is not at all understood, and that you haven't convincingly proved that it has to do with buffering mRNA stability.

What we would like to ask you is to relate to these points specifically in the manuscript. Currently, the Discussion is very short, and it can easily be extended to a real section where you can discuss and relate to the all the points raised by the reviewers (in particular the points raised by reviewer #1).

It may also be interesting (but not necessary) to relate to protein chaperones. Would you expect mutations that would also be buffered this way at the protein level? What do you think would be more important?

Reviewer #1:

The authors have done a significant amount of work, and provided new data. The overall picture remains, however, enigmatic, and possibly even more confusing than it had been prior to the addition of these new data. Specifically, there is still no clear indication that the mutations in the evolved lines relate to RNA stability/folding, and are thereby buffered by RNA chaperones.

The puzzling points that cast doubt on this interpretation are several:

1) There is not even a single overlapping mutation between the two evolved lines. This may suggest a non-specific buffering mechanism, but then on the other hand, as with protein chaperones, RNA chaperones are likely to have some obligatory 'clients', and other RNAs that are highly dependent on chaperone action. However, none of the identified mutations is in known structural RNAs.

2) Making isogenic strains is probably the most rigorous test possible, and the authors took this avenue. Sadly, however, the results are not supporting the hypothesis. Only one out 7 mutations tested (in lamB) exhibited both reduced fitness and evidence for buffering. But this mutation involves an amino acid exchange.

3) The synonymous mutation in rplS is more convincing, as it was shown to be deleterious and compensated by DRBH over-expresssion. However, then authors' assumption that fitness effects of synonymous mutations indicate the presence of selective constraints beyond the protein level is wrong. Synonymous mutations have been shown to affect the rate and outcome of protein folding, and thus the yield of soluble, function protein.

Overall, as I said, I'm sorry to say that the additional data cast in my view more doubts on the paper's main conclusion.

Reviewer #2:

The authors have addressed my major concerns. The work demonstrates that mutations in the evolved strains are reduced in growth and this reduction can be 'buffered' by overexpression of proteins that function as ATP-dependent or ATP-independent RNA chaperones. It is interesting that both mutations that confer fitness defects individually are in coding regions. While one is a missense mutation, the other one is synonymous, suggesting a role of the chaperone proteins in regulating the lifetime or translatability of the mRNA. The work raises very interesting questions on the roles of RNA chaperones in the functions of mRNAs, which will presumably spur future work.
