# Peer review - Round 1

Editors:
- Andrés Jara-Oseguera, https://ror.org/00hj54h04 The University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73645.sa0](https://doi.org/10.7554/eLife.73645.sa0)

This study by Deny Cabezas-Bratesco and collaborators draws from multiple bioinformatics approaches, as well as from published structural and functional data, to uncover a set of highly conserved amino acid sequence features in group I TRP ion channels. These identified features provide insight into the evolution and mechanisms of function of this diverse and important family of ion channel proteins.


---

# Peer review - Round 1

Editors:
- Andrés Jara-Oseguera, https://ror.org/00hj54h04 The University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73645.sa1](https://doi.org/10.7554/eLife.73645.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Sequence conservation and structural features that are common within TRP channels" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Andrés Jara-Oseguera as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Aldrich as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. All three reviewers agreed that the findings in the manuscript are relevant and interesting for a wide audience, and that data has been carefully analyzed. However, they also raised a series of concerns that would need to be addressed. Below is a list of essential revisions agreed upon by all reviewers, together with the individual reviews with additional helpful suggestions.

Essential revisions:

1) The authors should provide additional discussion regarding TRP subfamilies that have been identified more recently in unicellular organisms and invertebrates (TRPVL, TRPS, TRPF/TRPY, TRPL/TRP-γ), and consider them as separate subfamilies in their discussion, or otherwise justify why they chose to group them together with one of the vertebrate subfamilies. The authors should confirm whether sequences from these families were already included in their analysis, and include them if they were not considered initially.

2) The authors should include a cladogram or a similar graphic that allows readers to assess sequences from which organisms were included in the analysis, and whether different groups of organisms are similarly represented within the analyzed sample.

3) The authors should describe how the boundaries of the individual TM domains were determined, and how many structures were used to find these boundaries.

4) Figure 2A is very hard to read and confers limited information. The authors should include a new supplementary figure containing the entire MSA with sufficient resolution to appreciate the amino acid letters in the sequences. I suggest substituting Figure 2A with a different graphic that better highlights the differences in the gaps between subfamilies – perhaps showing histograms of gaps per amino acid position for each family computed from the sequences could be informative.

5) Data presentation in Figure 2 – Supplement 1 should be improved, as it is very hard to read. I suggest the authors show the MSA per subfamily but keeping the lengths of the gaps that arise from the MSA containing all families – this could provide a clearer depiction of the relations between gaps and subfamilies. It is also hard to appreciate the features that group the TRPL and TRP-γ sequences with TRPC channels – I suggest the authors include the sequences of TRPL and TRP-γ in the MSA for the other subfamilies, so that the higher similarity with the TRPC family can be better appreciated.

6) Lines 129-130: "usefulness of these patterns as predictors by looking at Drosophila channels TRPL and TRPgamma that were included in the dataset pulled from Uniprot." Why these particular channels? Also, if they were used in the dataset that generated the results is it fair to use them to test the results? It seems tautological. Is this test really needed?

7) HMM techniques are very well-known – the authors must have considered them along the way: why did the authors chose not to use them in the end? The task of finding conserved residues starting from one or several multiple sequence alignments could benefit from using HMM-based methods. These methods associate to each MSA a "profile", a probabilistic version of a consensus sequence. Different profiles can be compared via HMM-HMM alignments, which gives a pretty good description of the most relevant difference among the starting MSAs. It would be interesting to compute an HMM profile for each TRP family and look at these differences. This will for sure contain and hopefully extend your considerations about the gap "bar code".

8) How different are the trees produced by the maximum likelihood algorithm? I agree with the authors' choice of keeping the tree with the greatest likelihood (provided the MSA is fixed), but at the same time it would be interesting to look at how different the results are, in order to have a rough estimate of the reliability of the method.

9) The authors do not include branch lengths in their trees. This is a fundamental aspect for algorithms only capable of generating binary trees, and could be useful in reinforcing the points the authors make on the clades they find.

10) The functional significance of the aromatic core is not convincingly determined beyond that it might provide stability to the protein. The bulk of the functional studies actually suggest that mutating these residues only rarely abolishes coupling of ligand binding to gating, as proposed. The authors should more clearly discuss the potential relevance that the hydrophobic core might have on channel function – it would strengthen the manuscript if the authors provided a set of predictions or experimentally testable hypothesis for the functional relevance of this core. The authors should perform a thorough search of the literature for perturbations introduced in that region to test whether the published results are consistent with their hypothesis, and discuss their findings accordingly. The finding of a conserved interaction between residues on the TM4 and TM5 (W549 and F589) is significant, but there is no functional data for F589 or structural comparison analysis of the two sites in the apo and bound states – the authors should provide additional information from the literature if available.

11) Early on it is noted that the pre-S1 is functionally important, but findings for this region were not reported. The authors should include a brief note on those regions that are functionally important but yielded no highly conserved residues.

12) The authors should add labels for the transmembrane helices in Figure 3 and Figure 3 – Supplement 2. Without the labels, it is very hard to follow the discussion about the role of lipids in bridging regions with co-evolving residues. Have lipids been observed in structures specifically at those positions? The authors should discuss this more clearly.

13) The authors should provide stronger support for the conservation of signature residues in non-TRP channels. This could be done by including a sequence alignment for those channels or structural data such as that in Figure 3 – Supplement 1.

14) Structure-based sequence alignments are publicly available from the work by Huffer et al., (eLife, 2020) that is cited by the authors. The authors should analyze or at least discuss whether the signature residues they identify in their MSA also align in the structure-based alignments. This would provide stronger support for the structural conservation of the signature residues.

15) Figure 3 – Supplement 2 is inadequate to show changes in connectivity in the signature residues. The authors should introduce this topic with more nuance regarding the uncertainties in interpreting structural differences in single residues when the functional states that are represented by the structures are not known, and when the conformational differences that can be observed between a pair of aligned structures strongly depend on which regions of the protein were chosen for the alignment – the entire tetramer vs a single subunit vs just the pore- or the S1-S4-domains. The authors should analyze the structural data in a more systematic way, including data from more than one representative from each subfamily.

16) Figure 1: denote what UC stands for in the caption.

17) Line 172: please specify what TPCN stands for.

18) Figure 4: please clarify if the violet asterisk is between subfamilies? Rather than within. What does “AC” stand for?

19) Line 288: define VGIC.

20) In Figure 6 is it unclear whether the position of the markers for each evolutionary event has any significance, and if it does, what support is there for it. Perhaps reducing the size of the phylogenetic tree and including similar structural schemes for each group I TRP channel subfamily, as done for the outliers, could make the figure more informative.

Reviewer #1 (Recommendations for the authors):

1) The authors should include a cladogram or a similar graphic that allows readers to assess the diversity and balance between organisms from which sequences were analyzed.

2) Figure 2A is very hard to read and confers limited information. The authors should include a new supplementary figure ontainning the entire MSA with sufficient resolution to appreciate the amino acid letters in the sequences. I suggest substituting Figure 2A with a different graphic that better highlights the differences in the gaps between subfamilies – perhaps showing histograms of gaps per amino acid position for each family computed from the sequences could be informative.

3) Figure 2 – Supplement 1 is also very hard to read. I suggest the authors show the MSA per subfamily but keeping the lengths of the gaps that arise from the MSA containing all families – this would provide a better illustration of the relations between gaps and subfamilies. It is also hard to appreciate the features that group the TRPL and TRP-γ sequences with TRPC channels – I suggest the authors include the sequences of TRPL and TRP-γ in the MSA for the other subfamilies, so that the contrast can be better appreciated. This aspect of the manuscript could be strengthened if the authors provided data showing that the patterns of sequence gaps allow a clustering algorithm to correctly segregate channel ‘barcodes’ into their correct subfamilies.

4) The authors should add labels for the transmembrane helices in Figure 3 and Figure 3 – Supplement 2. Without the labels, it is very hard to follow the discussion about the role of lipids in bridging regions with co-evolving residues. Have lipids been observed in structures specifically at those positions? The authors should discuss this more clearly.

5) The authors should provide stronger support for the conservation of signature residues in non-TRP channels. This could be done by including a sequence alignment for those channels or structural data such as that in Figure 3 – Supplement 1.

6) Structure-based sequence alignments are publicly available from the work by Huffer et al., (eLife, 2020) that is cited by the authors. The authors should analyze or at least discuss whether the signature residues they identify in their MSA also align in the structure-based alignments. This would provide stronger support for the structural conservation of the signature residues.

7) Figure 3 – Supplement 2 is inadequate to show changes in connectivity in the signature residues. The authors should introduce this topic with more nuance regarding the uncertainties in interpreting structural differences, and discuss more at length their specific choices of structures for the analysis, and the implications of excluding certain structures and channel subtypes.

8) In Figure 6 is it unclear whether the position of the markers for each evolutionary event has any significance, and if it does, what support is there for it. Perhaps reducing the size of the phylogenetic tree and including similar structural schemes for each group I TRP channel subfamily, as done for the outliers, could make the figure more informative.

9) "a sidechain associated to channel response to both agonist and pH in different TRPs channels" – there are different mechanisms by which pH modulates TRP channels, and protons function as agonists for some of them. I suggest making this statement more specific.

10) "certain ligands might have the ability to modulate the conformation of the selectivity filter and by extension the extracellular linkers- without the need of an open gate conformation." – the significance of this statement is unclear.

Reviewer #2 (Recommendations for the authors):

Suggesting that you have determined the "phylogenetic position of unicellular TRP channels" yet excluding TRPVL and TRPS channels to me makes this analysis less compelling. TRPF/TRPY were included but this was not mentioned anywhere except the methods. Given this, it cannot be determined whether these novel channels are associated with known TRP subfamilies.

The functional significance of the aromatic core is not convincingly determined beyond that it might provide stability to the protein. The bulk of the functional studies actually suggest that mutating these residues only rarely abolishes coupling of ligand binding to gating, as proposed. Comparisons of the apo and ligand-bound state suggest it does not move upon channel opening. I also am not convinced that a similar set of non-rotating residues does not exist in other channels just because they are not at these exact sites.

Can you compare the locations of the TM4 and TM5 residues in the apo and ligand bound structures? This finding is compelling and could be easily checked with the data already included.

It was not described how the boundaries of the individual TM domains were determined, how many structures were used to find these boundaries.

Early on it is noted that the pre-S1 is functionally important, but findings for this region were not reported.

To make this more of interest to a broad audience, more detail about the medical and biological significance of TRP channels might be appropriate in the introduction.

Reviewer #3 (Recommendations for the authors):

I thank the authors for their very meticulous work for organizing the existent sources and pieces of knowledge regarding TRP proteins.

The original numerical contribution is also interesting. The bioinformatics techniques used are very standard, but they are used carefully. I have a few questions:

– The task of finding conserved residues starting from one or several multiple sequence alignments could benefit from using HMM-based methods. These methods associate to each MSA a "profile", a probabilistic version of a consensus sequence. Different profiles can be compared via HMM-HMM alignments, which gives a pretty good description of the most relevant difference among the starting MSAs. It would be interesting to compute an HMM profile for each TRP family and look at these differences. This will for sure contain and hopefully extend your considerations about the gap "bar code". HMM techniques are very well-known, thus I guess the authors must have considered them along the way: why did the authors chose not to use them in the end?

– How different are the trees produced by the maximum likelihood algorithm? I agree with the authors' choice of keeping the tree with the greatest likelihood (provided the MSA is fixed), but at the same time it would be interesting to look at how different the results are, in order to have a rough estimate of the reliability of the method.

– Also, the authors do not include branch lengths in their trees. This is a fundamental aspect for algorithms only capable of generating binary trees, and could be useful in reinforcing the points the authors make on the clades they find.

– As the authors point out, several PDB structures of TRP exist. This is a very precious resource: have the authors considered any online resource for their structural comparison?

– The authors perform a coevolution analysis, but the results are not mentioned in the Results section. Could they expand on this aspect?
