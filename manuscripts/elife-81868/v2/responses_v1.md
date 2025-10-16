# Author response - Round 1

Authors:
- Jordan L Pauli ([ORCID: 0000-0001-6276-3407](https://orcid.org/0000-0001-6276-3407))
- Jane Y Chen ([ORCID: 0000-0002-3986-8785](https://orcid.org/0000-0002-3986-8785))
- Marcus L Basiri ([ORCID: 0000-0002-4829-7187](https://orcid.org/0000-0002-4829-7187))
- Sekun Park
- Matthew E Carter ([ORCID: 0000-0003-1802-090X](https://orcid.org/0000-0003-1802-090X))
- Elisenda Sanz ([ORCID: 0000-0002-7932-8556](https://orcid.org/0000-0002-7932-8556))
- G Stanley McKnight
- Garret D Stuber ([ORCID: 0000-0003-1730-4855](https://orcid.org/0000-0003-1730-4855))
- Richard D Palmiter ([ORCID: 0000-0001-6587-0582](https://orcid.org/0000-0001-6587-0582))

## Response text

DOI: [10.7554/eLife.81868.sa2](https://doi.org/10.7554/eLife.81868.sa2)

Essential revisions:

1. Although both males and females were used, the authors state that "no formal comparisons were done between sex". Many of the peptides and receptors identified here exhibit sexual dimorphism. Information on potential sex differences would be valuable, and the authors should comment on this.

We added the sex of mice used in these studies to Methods and the following sentence to the Discussion (caveat section): Mice of both sexes were pooled for scRNA-Seq experiment and the Hi-Plex experiment did not have enough mice of each sex to make any formal comparison, so future studies should consider this variable.

2. Geerling and collaborators (PMC9119955) have recently published a catalog of cell populations in PB, focusing primarily, but not exclusively, on Atoh1 and Lmx1. The present authors have cited this paper more than once in this manuscript. However, it might be useful for the readers to relate the conclusions of the present manuscript to those presented by Geerling's group.

We added a sentence to Results. Karthik et al. (2022) have shown that the two major clades represented by Atoh1 decedents and Lmx1 descendants are largely non-overlapping populations; they have distinct axonal projections patterns, with the Atoh1 clade following a central tegmental tract to the forebrain and the Lmx1 clade following a ventral pathway.

3. In the abstract, the authors describe the PBN as being involved in pain sensation. Many people in the pain field would cringe at this description since they feel that pain is a percept that occurs in the cortex. Please consider an alternative description such as pain behaviors, pain responses, or nociceptive responses.

We changed text to read “nocifensive responses”

4. In Figure 3, table supplement 1, two genes have superscripts that are colored red for reasons that are unclear and look peculiar.

Color has been removed

5. In the discussion, the authors state: "We obtained ~100,000 reads per neuron which is close to the number of mRNA molecules/cell. A higher number of reads is necessary to capture rare transcripts since a single transcript can maintain ~10,000 proteins with a half-life of 1 day, which may be enough for many regulatory proteins." Please provide citations or at least some indication of how you arrived at these estimates.

A new section ‘Estimating mRNA and protein abundance per cell’ has been added to the Materials and methods to illustrate how the estimate was derived

6. The abbreviations associated with the PBN and its efferent targets make this paper somewhat challenging to read. Please consider adding a table of abbreviations.

We added a list of abbreviations

7. In the results, the authors state that "This (Phox2b) line showed a unique projection to the SH, which likely originated from cells in the PBlc and PBls rather than PBmm because we did not see the same SH projection from the Tac1 cells in the PBmm" What is the SH? I could not figure this out, nor could I see evidence for this claim in the main or supplementary figures.

We changed the sentence in the Discussion. It now reads: This line showed a projection to the septohippocampal nucleus (SH), which likely originated from cells in PBls rather than PBmm because we did not see the same SH projection from the Tac1 injection that heavily expressed in the PBmm (compare Phox2b and Tac1 whole brain expression available on Zenodo, DOI: 10.5281/zenodo.6707404).

8. There are two undefined yet significant clusters (without any assigned color codes) – one in the center and the other at the bottom of the UMAP space (Figure 2A). The molecular identity of the two clusters should be described in the figure and main text.

We added a sentence to Methods and a note of Figure legend.

“Within the neurons, two subclusters were unable to be mapped to any specific features and were excluded from the analysis (Figure 2A, gray).”

9. The authors conclude that neuronal populations located in the dorsal PBN mainly innervate brain regions associated with the Central Tegmental Tract (CTT), whereas neuronal populations found in the PBle mainly innervate the brain regions associated with the Ventral Pathway (VP). However, there is significant overlap in the brain regions innervated by both PBN populations (Figure 7B). Thus, the axon projection summary diagram (Figure 7A) may be misleading. Can this be discussed and the overlap of these two pathways more clearly indicated?

This is a good point. We added the following paragraph to Discussion.

“There is overlap of axonal projections to both pathways that probably occurs because none of the neuronal subclusters are restricted one sub-domain of the PBN. Cre-driver lines that mainly have expression in the dorsal PBN regions (Pdyn, Tacr1, Brs3, Cbln4, Ptger3) have axons that tend to travel through and target ventral brain regions such as the VTA, LHA, DMH, PVH, and MEPO. Lines that are categorized into the dorsal group often have fewer cells and weaker projections as a result. Some lines also have expression in PBle (Tacr1, Ptger3) which results in weak innervation of areas along the CTT as well. Some Cre-driver lines have strong cellular expression across most of the lateral PBN. For lines like this (Adcyap1, Adcyap1r1, Oprm1, Crh), there is robust expression of the AAV-driven fluorescent proteins in areas associated with the CTT such as the BNST/CEA and areas associated with the VP such as the MEPO. Overall, their projections are a combination of areas seen in the other groups.”

Reviewer #2 (Recommendations for the authors):

1) Related to concern 2) in the public review: Considering the variability of the expression level of different Cre-driver lines and efficiency of AAV virus injections, quantifying the relative density of axonal projections within each population could be more meaningful and potentially better support the authors' conclusion.

Quantifying the density of projections is not worth the effort. Readers can decide for themselves by looking at primary data. We can discuss under “caveats”

Reviewer #3 (Recommendations for the authors):

1. In the abstract, the authors describe the PBN as being involved in pain sensation. Many people in the pain field would cringe at this description since they feel that pain is a percept that occurs in the cortex. Please consider an alternative description such as pain behaviors, pain responses, or nociceptive responses instead.

This comment was addressed under Essential Revisions

2. In Figure 3, table supplement 1, two genes have superscripts that are colored red for reasons that are unclear and look peculiar.

This comment was addressed under Essential Revisions

3. In the discussion, the authors state "We obtained ~100,000 reads per neuron which is close to the number of mRNA molecules/cell. A higher number of reads is necessary to capture rare transcripts since a single transcript can maintain ~10,000 proteins with a half-life of 1 day, which may be enough for many regulatory proteins." Please provide citations or at least some indication of how you arrived at these estimates.

This comment was addressed under Essential Revisions

4. The abbreviations associated with the PBN and its efferent targets make this paper somewhat challenging to read. Please consider adding a table of abbreviations.

5. In the results, the authors state that "This (Phox2b) line showed a unique projection to the SH, which likely originated from cells in the PBlc and PBls rather than PBmm because we did not see the same SH projection from the Tac1 cells in the PBmm" What is the SH? I could not figure this out, nor could I see evidence for this claim in the main or supplementary figures.

This comment was addressed under Essential Revisions
