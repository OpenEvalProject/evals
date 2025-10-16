# Peer review - Round 1

Editors:
- Qiang Cui, https://ror.org/05qwgg493 Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81547.sa0](https://doi.org/10.7554/eLife.81547.sa0)

By integrating a range of computational techniques, the authors made an important contribution by generating a structural model for the AT3 domain, which is predicted to adopt a new fold. The key features of the structural model are consistent with the activity of the enzyme as an acyltransferase, with a transmembrane channel that can accommodate an acyl-CoA donor, and an outer cavity formed with a second domain that can accommodate a nascent LPS molecule as substrate. Overall, the study is valuable as it will help stimulate specific experimental analyses that will further evaluate and improve the model for better mechanistic understanding of this class of enzymes.


---

# Peer review - Round 1

Editors:
- Qiang Cui, https://ror.org/05qwgg493 Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81547.sa1](https://doi.org/10.7554/eLife.81547.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A novel fold for acyltransferase-3 (AT3) proteins provides a framework for transmembrane acyl-group transfer" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of Our Board of Reviewing Editors, and the evaluation has been overseen by Volker Dötsch as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Josh V Vermaas (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Clarity of the presentation can be improved, and some results (e.g., open/close mechanism) can be made more robust with alternative simulation or analysis.

2) Interaction energies reported need to be placed into the proper context, so that the mechanistic implications can be made clear.

For details see the individual comments of the reviewers.

Reviewer #1 (Recommendations for the authors):

The combination of a broad range of computational models in the study is appropriate and powerful. The only comment/question I have concerns the quantum mechanical calculations, which revealed a very large (-1035.943 kcal/mol) interaction energy. While I understand that this represents interaction energy rather than binding (free) energy, and that there are several charged groups involved, the magnitude is rather large. Is this due in part to the fact that calculations were conducted in vacuum?

Reviewer #2 (Recommendations for the authors):

I would have benefitted from a reaction diagram detailing the chemistry this enzyme is thought to facilitate. The broad eLife readership is unlikely to know what exactly MurNAc is, or what part gets acetylated. I think, based on the extensive introduction, that the best guess right now is that this enzyme, or related enzymes, add the acetyl group onto the glucosamine nitrogen (?). These are thought to be cytoplasmic reactions, however, so I am very confused as to where this fits into polysaccharide synthesis overall.

Roughly how big is the dataset that is helping RaptorX with coevolutionary analysis? For fun, I ran this through alphafold, and indeed, the only pdb templates AlphaFold picks up on are for the soluble domain. This suggests to me that RaptorX and AlphaFold are basing the structure almost exclusively based on sequence alignments. How many sequences are close enough that the black box structural methods use them as inputs?

I would love to see some context around the quantum calculations. -1000kcal/mol sounds impressive, but is completely irrelevant to the actual binding affinity, and the way the discussion is phrased would be highly misleading to a non-computational audience.

The SI should have the sequence alignment. You clearly have computed one to know what the offset is between the current protein and other points of comparison listed in the text, but for the reader this is hard to grok the first time through, since we are naturally far less familiar with the protein sequences than you are.

Figure S2C is… unfortunate? I know that this is a VMD default visualization using Timeline, but I think we can all agree that it isn't the most professional looking representation for the data. It also argues against the highlighting in S2B, since in S2C I count 13 helical regions, not 11.

If you do an analysis that you comment on in the main text, the results should be shown. From page 15: "Principal component analysis (PCA) of the backbone atoms was used to extract the first 2 major motions (accounting for 77% or more of the variance) of the protein in the four equilibrium replicates." What is the sampled spread along these PCA dimensions? Are these even meaningful? In short simulations, this protein cannot really change its conformation, so all the PCA is measuring are the jiggles around the initial structure. The animations, while visually appealing, don't actually quantify the motions claimed in the paper. If this were framed in a more speculative fashion, I think it would be more appropriate, since the simulations are just nowhere close to exhaustive enough to prove or disprove this hypothesis.

Page 16, where can I see the occupancies, other than the selected occupancies enumerated in the text? It is not hard to tabulate this similar to what is done in Table 2.
