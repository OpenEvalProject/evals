# Peer review - Round 1

Reviewers:
- Nir Ben-Tal, Tel Aviv University , Israel

## Review text

DOI: [10.7554/eLife.20718.029](https://doi.org/10.7554/eLife.20718.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Assembling the Tat protein translocase" for consideration by eLife. Your article has been favorably evaluated by John Kuriyan (Senior Editor) and two reviewers, one of whom, [Nir Ben-Tal (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: William M Clemons (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The Tat protein complex mediates the transport of folded proteins across the cytoplasmic membrane in bacteria and the thylakoid membranes of plant chloroplasts. The complex is assembled from multiple copies of each of the following three proteins: TatA, TatB, and TatC. The manuscript describes the use of evolutionary data (mostly coevolution), molecular simulations, and various experimental assays to suggest a structure model of the interaction between the 3 subunits in the complex based on the structures of the individual components. It further suggests a model of Tat activation and conformational changes upon interaction with the signal peptide of the transported protein.

In particular, it explores a hypothesis generated from co-evolution analysis that TatA and TatB both bind to the conserved patch of hydrophilic residues on TM5 and TM6 of TatC. The work convincingly demonstrates that the paralogs TatA and TatB evolved from a common TatA family member. The divergence resulted in TatB occupying the binding state during the resting channel. Binding of substrate would displace TatB, resulting in TatA occupying this site. Additionally, TatA is demonstrated to have a second binding site in the resting translocase. The result is a reasonably convincing model of the TatB/C complex that is substantiated by molecular dynamics.

This is a very interesting and carefully conducted study, where predicted contacts between amino acid pairs are examined experimentally, e.g., using disulfide crosslinks. The results are nicely presented within the context of existing knowledge on Tat.

Essential revisions:

The model structures (in PDB format) should be made readily accessible to the public. Maybe as Supplementary data?

1) How dependent is the phylogenetic tree of Figure 2 on the method used to generate it? CLUSTAW might not always give the most reliable trees. More accurate tools, such as MAFFT-LINSI and PRANK should be used.

2) The charged residue in the central pocket isn't discussed at all. Based on the phylogeny determined, is there anything that can be gleaned from TatC homologs that only have a polar residue?

3) Introduction, fifth paragraph: 'direct methods' isn't a clear term. Perhaps 'standard structural methods'?

4) Subsection “Evolutionary contacts between TatA family proteins and TatC”, second paragraph: 'precision score' is used without context. Considering the general audience it might be helpful to provide some context for what the scores actually mean. Is 0.5 a reasonable cut-off? High/low. One can only infer from the figure but there should be a way to explain the score in a sentence or two.

5) Subsection “Exploring evolutionary contacts for different TatA paralogs”, second paragraph: some numbers would be interesting to cite. 'Almost all' means what? How prevalent are TatB?

6) Subsection “Exploring evolutionary contacts for different TatA paralogs”, end of second paragraph: what is meant by 'partners' in this context? Does it have to have a TatC?

7) Subsection “Exploring evolutionary contacts for different TatA paralogs”, fourth paragraph: TatA and TatA family are used interchangeably at times. It makes it unclear as TatA becomes defined. Here it should say 'TatA family subsets' for clarity.

8) Subsection “Exploring evolutionary contacts for different TatA paralogs”, fourth paragraph: perhaps change the two motifs to be F-G-X and X-G-P to make it easier to relate.

9) Subsection “Exploring evolutionary contacts for different TatA paralogs”, fourth paragraph: seems odd that E8 isn't discussed here.

10) Subsection “Evolutionary co-evolution analysis identifies additional inter-subunit contact sites within the TatBC complex”, last paragraph: can't really see the flexible regions of the periplasmic cap loops.

11) Subsection “Evolutionary co-evolution analysis identifies additional inter-subunit contact sites within the TatBC complex”, last paragraph: the rationale for filling with lipids or water should be discussed. Was anything learned here? It seems there should be some substantial differences. (I realize there are space constraints).

12) Figure 2B: in the logo plot the length is constrained. How were differences in length accounted for in this presentation.
