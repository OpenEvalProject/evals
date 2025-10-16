# Author response - Round 1

Authors:
- Assaf Elazar
- Jonathan Weinstein
- Ido Biran
- Yearit Fridman
- Eitan Bibi
- Sarel Jacob Fleishman ([ORCID: 0000-0002-6831-3770](https://orcid.org/0000-0002-6831-3770))

## Response text

DOI: [10.7554/eLife.12125.019](https://doi.org/10.7554/eLife.12125.019)

The reviewers suggested a number of important revisions that would help strengthen this manuscript. 1) The reviewers pointed out an important caveat for the present analysis: strictly speaking, the results should be considered propensities rather than free energies of membrane insertion and helix-helix association, without calibrating the expression level, or the relative population of the membrane-inserted protein vs the protein in cytosol. We suggest the authors Western Blot the expression levels of a small set (~10) of mutants and hopefully to show small variances in the expression levels. In any event this caveat should be discussed in the revised manuscript.

We agree with this caveat and have addressed it in several ways:

A) We adopted the argument recommended by Reviewer #2 that the free energy derivation depends on the constancy of the cytosolic amounts of protein among the different mutants (subsection “dsTβL: a high-throughput assay for measuring membrane-protein energetics”, last paragraph) and we explicitly mention now the assumption of thermodynamic control of partitioning between the different states. We further state that this assumption is supported by the agreement between the results and biophysical measurements.

B) We verified the behavior of 10 selected mutants by Western blots of membrane preparations (Figure 2—figure supplement 3). The Western blots showed that the proteins express in the membrane, and all run at the expected size, thereby excluding the possibility of cleavage. 6 mutations that target membrane-core positions and one at the amino terminus show the expected trends, including mutations that increase or decrease expression. However, 3 mutants to charges at the amino terminus increased expression levels according to Western blots, but were disruptive according to dsTβL. We propose in the revised manuscript that these results are due to the fact that ampicillin selections probe appropriate integration in the membrane, not just expression levels as in Western blots.

C) The reviewers found it surprising that the screen is so sensitive, even to mild mutations. In the first paragraph of the subsection “Systematic per-position contributions to membrane-protein insertion” we now note that the CLS amino acid sequence is quite polar, suggesting that its membrane-expression levels would be sensitive even to point mutations. To further confirm this sensitivity, for the 10 above-mentioned mutants we carried out plate-viability assays on a clone-by-clone basis, and in 9 saw the same behavior as in the deep sequencing experiments (Figure 2—figure supplement 2), including complete non-viability for some of the mutants.

2) Both reviewers thought the discussion concerning TM topology is a distraction from the main focus. It would be better to remove this discussion from this manuscript and to publish it separately with further development.

Right. We replaced this discussion with the statement: “…the results suggest that the insertion profiles could be used for sequence-based prediction of the locations and orientations of membrane-spanning proteins (A.E., J.W, et al., manuscript in preparation).”

3) The results reported in Figure 2b (Z-dependent energetic profiles) should be analyzed in comparison with bioinformatics results (Senes et al., 2007; Ulmschneider et al. 2005; Ulmschneider et al. 2006; Schramm et al.,

2012).

This now appears in Figure 4 and discussed in the last paragraph of the subsection “Large differences and strong asymmetries in insertion of positively charged residues”. Briefly, we note some similarities but also significant differences with the dsTβL profiles. Most importantly the statistics-based profiles are quite flat by comparison and show minor contributions for hydrophobicity or the positive-inside rule. We discuss these differences with respect to the fact that membrane-protein statistics reflect functional constraints rather than pure energetics. Reviewer #2 noted that our profiles for Tyr and Trp did not match the expectation that these residues are favored at the membrane-water interfaces. We agree with this point and discuss it in the last paragraph of the subsection “Systematic per-position contributions to membrane-protein insertion”, suggesting that these observations may reflect differences between single and multi-span membrane proteins. We also summarized caveats regarding the insertion scales in the Discussion, third paragraph, which we hope will clarify these points and spur future research.

4) The reviewers asked for further description of the present dsTβL system and for a more detailed comparison of the present system with the previously developed Lep system. Why the choice of β

-lactamase instead of the maltose binding protein? What is the precise sequence of L-selectin used in the system? Why the high sensitivity of membrane insertion to even conservative TM mutations? The authors attribute the lower membrane hydrophobicity estimated by previous work (Hessa et al., 2007) to translocon interactions of the Lep system. Please elaborate this point, as the present system also passes through translocons to be embedded in the membrane.

A) We have elaborated our description of the TβL construct (subsection “dsTβL: a high-throughput assay for measuring membrane-protein energetics”). Briefly, there were two reasons for using β-lactamase instead of MBP: 1. Viability on ampicillin is linearly related to β-lactamase expression levels whereas MBP on maltose is not (see refs. provided in the paper); and 2. The TOXCAT-MBP construct requires working with an MBP-null E. coli strain (MM39), which is not amenable to high-throughput genetic transformations, whereas with β-lactamase we could work with the E. cloni high-transformation efficiency strain.

B) As mentioned above in our response 1C, we verified the high sensitivity on a clone-by-clone basis. The reason for this high sensitivity is that the CLS amino acid sequence is quite polar.

C) Regarding our comparison to the Lep system: we have revised our argument in the Discussion. Briefly, the Lep measurements quantified proteins that were either singly or doubly glycosylated, but did not quantify total membrane-protein levels. The observations that the Lep measurements are rank-ordered as in our measurements (and also in published biophysical experiments on an outer-membrane protein), but are fourfold smaller in magnitude, as well as the observation that the atomic-solvation parameter inferred from Lep is smaller by roughly fourfold compared to both dsTβL and previous biophysical work are consistent with a view that Lep was measuring only part of the insertion equilibrium. We have removed the argument that the differences are due to interactions with the translocon.

D) Reviewer #2 was correct in identifying a mistake in the DNA sequence we provided for CLS in the original supplement, which was of the CLS reverse-complement. We corrected this mistake and apologize for the error. The amino acid sequence of CLS is noted at the bottom of Figure 2a.

In addition to the changes above, we corrected, clarified, and reanalyzed our data following the individual reviewer comments, including those that were not mentioned in the summary. With respect to the self-association data we now compare to the Doung et al. data on GpA (Figure 5b) finding high correspondence between their data and ours. We also revised this section to highlight the new findings in dsTβL, including positions, which were not tested in the Lemmon et al. and Doung et al. studies, but are sensitive to mutation, or the few mutations that promote self-association; without a comprehensive analysis it is unlikely to identify the very few beneficial mutations. We further shifted the emphasis from structure prediction to the insertion-association coupling by shortening the structure-prediction paragraph and changing the last sentence in the Abstract and the sub-title of the relevant section. We feel that the self-association section is an important and integral part of this paper because it shows that a single assay can easily provide systematic data on the two primary components of membrane-protein energetics: insertion and association. Furthermore, the fact that we used the insertion data derived from CLS to subtract the insertion contribution in two unrelated systems (GpA and ErbB2) confirms the general usefulness of the insertion scales and should simplify future studies that analyze mutational effects on association or function.
