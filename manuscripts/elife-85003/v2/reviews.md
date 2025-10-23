# Peer review - Round 1

Editors:
- Christian R Landry, https://ror.org/04sjchr03 Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85003.sa0](https://doi.org/10.7554/eLife.85003.sa0)

This manuscript reports valuable findings regarding the evolution of nitrogenases through ancestral sequence reconstruction and resurrection. The results are convincing and support the conclusions of the study, and highlight the historical constraints that have been acting on this enzyme. The findings will be of interest to people interested in enzyme evolution in general and particularly to those interested in the evolution of nitrogenases.


---

# Peer review - Round 1

Editors:
- Christian R Landry, https://ror.org/04sjchr03 Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85003.sa1](https://doi.org/10.7554/eLife.85003.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Nitrogenase resurrection and the evolution of a singular enzymatic mechanism" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Landry as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Matilda Newton (Reviewer #2); Christian B Macdonald (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

– The reviewers raised questions about the impact of horizontal gene transfers on phylogenetic reconstructions. Further discussions led to the conclusion that this is probably not a major issue but it would be important to address this point in the paper.

– Reviewer 1 raised the issue that two distinct phylogenies were obtained with the same dataset as well as issues with the reconstruction methods implemented in the computational tools used. These would be important points to verify and clarify as needed.

Reviewer #1 (Recommendations for the authors):

I would strongly suggest the RaxML issue is explained in the methods. As a community, we should make sure that rigorous methods are used, especially since there is virtually no significant computational cost to the full algorithm anymore. As the Kacar lab is one of the leading groups in this field, it would be great to be clear about this.

If I misunderstood, and the authors' version of RaxML did in fact use the correct algorithm, this part of my public review should be deleted. It would still raise the question as to why the PAML and RaxML reconstructions differ, which would still need to be explained in the methods.

I did not understand exactly what the language model analysis shows. It is only mentioned in one sentence in the paper that does not explain the meaning of this analysis.

Reviewer #2 (Recommendations for the authors):

• Include a caveat that the reconstructed enzymes can only ever be hypotheses.

• I appreciated the insertion of the gene into the genome as opposed to plasmid-based expression

• ASR can only ever reconstruct the ancestor to extant enzymes, we can't rule out that there were other N2 fixation strategies competing pre-LUCA but they have left no trace.

• Why did you choose to use maximum likelihood inference instead of Bayesian?

• Figure 3A – please show the y-axis in the log.

• Could you please represent catalysis in units for kcat and KM? This would make the kinetics easier to compare to other enzymes, both extant and reconstructed.

• 4C please include WT.

• In light of the conclusion about a highly conserved mechanism, I would like to see more nuanced mechanistic studies. Pre-steady state kinetics; MD; pH studies.

• Please infer the age of the hypothetical ancestors expressing anc1 and anc2.

• Is there a notable difference between how the all-anc complexes (Anc1B) interact as opposed to the hybrids (Anc1A, Anc2)? Is there a notable difference in melting temperature or oligomeric state? This is discussed to a degree in the paragraph beginning line 323, but many of the statements are general and do not posit molecular explanations. What do the authors mean by "historical" amino acid substitutions?

• The discussion notes the surprising conservation of inhibition by H+ despite "substantial residue-level changes to the peripheral nitrogenase structure, as well as a handful within relatively conserved, active-site or protein-interface regions within the enzyme complex" Please elaborate on this, with specific attention to the active site. Are the residues involved/mechanisms known? Specify the mutations, how chemically conserved are they?

• I would be interested to see a discussion of potential ancestral promoters and expression levels. Expression levels are mentioned briefly in the results. I know this experiment must be compatible with the biological system used for the experiment (i.e. it would be impractical to also reconstruct ancestral promoters), but do the authors speculate that an ancestral nitrogenase would have been overexpressed to compensate for lower efficiency or that N2 fixation would merely have been rate-limited?

• For the uninitiated, please clearly introduce the evolution of metal ion dependence in nitrogenases.

• How do your results compare to enzyme reconstructions of a similar "age"?

• I find these results unsurprising. There is sufficient ASR literature to predict that a reconstructed enzyme will have comparable activity to the one or two extant enzymes it is compared to. When using a clade of conserved enzymes using a conserved mechanism, it is not surprising the ancestor conforms. What have we learned? It would be more interesting to probe these reconstructions for promiscuous activities or additional inhibitors. Are they easier to evolve than extant enzymes? If you reconstruct the whole pathway, does it behave differently? Does it act inefficiently and leak metabolites? Are other methods of fixation conceivable?

Reviewer #3 (Recommendations for the authors):

I have several questions and suggestions for the phylogenetic analysis that I do not believe will alter any of the results but may help with presentation or for a better understanding of the uncertainty with them.

• Why were these particular nodes picked for reconstruction? Are they the highest confidence reconstructions?

• Why was LG+G+F used? Was any model testing done?

• What tool was used to align the sequences?

• Why was ASR performed with RAxML and PAML both?

• What is the difference between the forak023 and forak013-14 files in the github repository? The topology of tree_forak013-14_branchsupport.tre seems to be the one in the manuscript, but there are no branch support values in that file.

As mentioned in the public comments, I worry whether HGT may cause issues during tree inference. I believe the simplest way to find out would be to reconstruct a gene tree for each individual nif gene and see how the trees differ. It could also be worth examining whether these or the tree in the manuscript agree with bacterial phylogenies.

The randomly-selected codon (de)optimization process is a nice inclusion. I was a little unsure about how it was performed, though – were codons swapped randomly until some metric was reached, or a fixed number, or some other procedure? Given the other controls, I do not expect this to change any results, but it would be a nice method for other groups to potentially use.

Given that the WT and ancestral sequences are 83% identical or higher (roughly akin to humans and mice), is the result that function is conserved surprising? Is it possible that these results say more about sequence (and functional) conservation, rather than a constraint? The UMAP embedding is an interesting approach, but makes this point in a different way, as the ancestral and WT sequences are extremely close in UMAP space. I believe some discussion of sequence.
