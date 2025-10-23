# Peer review - Round 1

Editors:
- Anthony G Vecchiarelli, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69676.sa1](https://doi.org/10.7554/eLife.69676.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Bacterial ParB partition proteins have the novel property that they employ an unusual nucleotide cofactor for complex assembly at their specific DNA binding site, parS. The impact of this study is on our general understanding of this novel class of nucleotide-dependent processes, and the role that nucleotide-protein interactions play in DNA binding and bacterial physiology.

Decision letter after peer review:

Thank you for submitting your article "A CTP-dependent gating mechanism enables ParB spreading on DNA" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Anthony G Vecchiarelli as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Gisela Storz as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All three reviewers agree that the work is exciting, high quality, will be of broad interest, and should be published in eLife. However, in the "Recommendations to the Authors" there are two control experiments that all three reviewers agree are simple to perform and required. Also, all three reviewers had concerns regarding the ChIP-seq data that need to be addressed prior to publication.

1) From Reviewer 1: A control experiment where the authors pre-treat ParB with cross-linker before addition of DNA substrate to show that premature and irreversible closing of the ring prevents interactions with parS as well as spreading/sliding. The pre-crosslinking might alter protein conformation in other ways (besides closing a gate) that might destroy the DNA binding site (so there are caveats). Nevertheless if crosslinking did not prevent DNA binding, that would affect the overall story.

2) From Reviewer 2: A linearized plasmid control. The authors use the binding to circular DNA as evidence that ParB is topologically constrained, compared to a 22 bp linear DNA substrate. But the latter might just be too short to make a stable (non-clamped) complex. The experiment is consistent with a clamped complex but does not formally show it. Or perhaps instead of Benzonase treatment, treat the complex with a restriction enzyme after the fact and show it disassembles. This data can be added as a supplemental figure so the authors don't need to repeat the original and redraw the figure. If not performed, then the language should reflect that the experiment does not prove topological constraints.

3) More critically, reviewers agree that the single MAJOR issue is the ChIP-seq data in Figure 8A. We all expected an expanded profile around parS sites with ParB[E102A] and that is clearly not happening. Also, the authors highlight the upstream extended signal that is amplified in the mutant and largely absent in WT, but this could just be a confounding interaction with the par operon or expression from the parB gene itself. All three reviewers appreciate the authors trying to bring their in vitro findings back into the cell, but it did not seem to work out as described in the text. Of note, the Gruber lab currently has a similar story on BioRxiv and their ChIP-seq data for their CTP-trap mutant of B.sub ParB shows an expansion of signal around the parS sites. As noted in our independent reviews, the authors need to re-interpret their ChIP-seq data, provide a better and more detailed explanation of these findings, and possibly tamper their claims.

Finally, please see the "Recommendations to the Authors" section from all three reviewers for suggestions to improve clarity and presentation before resubmission.

Reviewer #1 (Recommendations for the authors):

Ln 302-304 and Figure 8

The description and interpretation of the [E102A] ChIP-seq data, as having a more "extended profile", is not an entirely accurate. Figure 8A clearly shows that spread is only in one direction (upstream), and there is a massive signal around the parAB operon (particularly over the ParB gene) with [E102A] that is largely absent from the WT ChIP seq. This strong [E102A] signal over the parAB operon dissipates in both directions, and the spread from this specific location is described by the authors as [E102A]'s "extended profile". This result is striking but not discussed by the authors. The authors need to expand their description and interpretation of the ChIP data as it relates to this region, and speculate as to what they think this upstream signal around the parAB operon may represent.

Ln 316-317 and Figure 9

Given the flexibility of the N-terminal domain, do the authors think it possible that this domain flexibility plays a role in ParB's ability to not only close the ring, but also associate with other ParB dimers and/or with ParA? Given that the ParA interaction interface is on this flexible domain, I think the data here interfaces quite nicely with the BioRxiv preprint from the Mizuuchi group (already cited in the paper) that was also recently reviewed by eLife: https://www.biorxiv.org/content/10.1101/2021.01.24.427996v1. In particular: They find ParB can bind to ParA either using the two protomers of a single dimer or two protomers from distinct dimers. The former occurs in the absence of ligands, the latter upon addition of either CTP or parS, thus presumably corresponding to the state of ParB found in the cells near a parS site. The discussion would benefit from the authors putting their findings in the context of other ParB interactions shown to be required for chromosome segregation – ParA interaction and ParB dimer oligomerization.

Reviewer #2 (Recommendations for the authors):

1. The crosslinking at L224 supports the idea that DNA has left the DNA binding domain after clamp closure, consistent with the structural clashes observed. Where is L224 in the DNA binding region? The cartoon in Figure 5 places it at the C-terminal side of the DBD but it would help if the position of L224 was indicated on one of the structures, eg Figure 1B, in addition to the cartoons. Why is there a helix 10 in the structure (Figure 1) but not in the secondary structure of Figure 2-supp2? By my estimation L224 is in helix 10 but this is confusing.

2. Figure 8: The ChIPseq profile of E102A is confusing and warrants more explanation. The authors state it is "notably more extended than the profile of" wild-type ParB. The shaded area to which they refer does not center on a parS site. What is the explanation for this pattern? That the profile is more extended also predicts that the other parS peaks would be more extended, which does not appear to be the case. Why? If the peaks were normalized to the same height, would E102A peaks look broader?

3. I like the alanine scanning approach to target the residues that interact with CTP, in part because it is a more comprehensive survey of the CTP binding site, which is poorly understood compared to sites that bind ATP or GTP. This allowed them to identify E102A as a mutation that created a CTP dependent clamp with diminished dissociation rate because it could not hydrolyze CTP. But the analysis also created two other classes of mutants (pg 8). Although the authors would likely argue that their analysis is beyond the scope of the current study, it would add important insight to the story if the authors discussed or proposed explanations for the behavior of each class in the Discussion. For example, why do class II, which bind but do not hydrolyse CTP, behave differently than E102A? Based on their location could they be permanently closed?

4. Figure 5: There should be a linearized plasmid control. The authors use the binding to circular DNA as evidence that ParB is topologically constrained, compared to a 22 bp linear DNA substrate. But the latter might just be too short to make a stable (non-clamped) complex. The experiment is consistent with a clamped complex but does not formally show it. Or perhaps instead of Benzonase treatment, treat the complex with a restriction enzyme after the fact and show it disassembles.

Reviewer #3 (Recommendations for the authors):

The data on the recycling mechanism upon CTP hydrolysis presented in Figure 8A are not sufficiently convincing to conclude that without CTP hydrolysis (variant E102A) the clamped-ParB diffuse longer away from parS than wt ParB. Especially, the most important signal, which strongly extend the ParB signature over DNA on the left side, seems independent of parS loading; indeed, the peak is away from the first and weak parS site. It rather corresponds to the location of the parB gene, which suggests that the signal detected here does not correspond to sliding but rather to ParB synthesis. Therefore, this is against the author's conclusion that preventing CTP hydrolysis extend ParB sliding. In addition, the signal over the parB gene is increased 4-5 fold compare to wt while the parS-specific signals are decreased about 3-fold. This may prevent a direct comparison of the "spreading" signature. Also, if ParB (E102A) is trapped longer on DNA, one would expect that the ParB signal should be higher in between parS sites that are close together such as in between parS3-4-5-6. The authors should comment on this lack of increase, and discuss these in regard of the sliding model relatively to other assembly model.
