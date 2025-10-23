# Author response - Round 1

Authors:
- Kathryn M Tabor ([ORCID: 0000-0003-3696-4584](https://orcid.org/0000-0003-3696-4584))
- Gregory D Marquart ([ORCID: 0000-0001-9811-5372](https://orcid.org/0000-0001-9811-5372))
- Christopher Hurt
- Trevor S Smith
- Alexandra K Geoca
- Ashwin A Bhandiwad
- Abhignya Subedi
- Jennifer L Sinclair
- Hannah M Rose
- Nicholas F Polys
- Harold A Burgess ([ORCID: 0000-0003-1966-7801](https://orcid.org/0000-0003-1966-7801))

## Response text

DOI: [10.7554/eLife.42687.019](https://doi.org/10.7554/eLife.42687.019)

Major comments [concatenated and reordered, from all reviewers]:

1) [Related to Essential revision 1] Throughout the manuscript, the words, "cellular resolution", "single cell resolution", and "intersectional targeting" are used multiple times. With these words, readers would expect the following experiments: searching for Cre and Gal4 lines in the database, finding small numbers of neurons in which Cre and Gal4 expression overlap, and expressing reporter/effecter genes in these neurons. Nowhere in the manuscript, however, are examples of such experiments are provided. Thus, it is not clear whether targeting expression of reporter genes with cellular resolution is possible with the combination of Cre and Gal4. There are several potential concerns for the intersectional targeting of small numbers of neurons. These include stochastic activity at target loxP sites for Cre, and variable expression and silencing for Gal4. The authors cite the Current Biology paper (Tabor et al., 2018) as an example of intersectional targeting, but the Cre lines used in that study are broad expression lines (Cre expression in particular rhombomeres). So, the study does not serve as an example of intersectional targeting at cellular resolution. There is one place in the paper where the authors mention UAS:Switch expression experiments (in Discussion). However, it is written in a negative context: "Occasionally, we have observed UAS:Switch expression in neurons outside the domain of Cre expression in the ZBB2 atlas". In any case, the authors need to show clear examples of intersectional targeting in small numbers of neurons where Cre and Gal4 expression overlap in the ZBB2database.

In the manuscript we have generally used the phrases like 'cellular resolution' to refer to the level of detail observable in the database rather than the level of resolution that we think can be usually obtained by intersectional targeting with transgenic reagents. Rather, our vision is that Cre lines with relatively broad expression can be used to select out sub-domains within Gal4 expression patterns. To achieve true single cell resolution, a third intersectional reagent is generally necessary (for example, the B3 recombinase that we used in Tabor et al., 2018).

However, the reviewers correctly observe, in Tabor et al., we performed intersectional targeting using Gal4 and Cre lines with relatively broad expression. We also agree that UAS lines (including the UAS:Switch) tend to silence and show variable expression. Therefore in the revised manuscript we have added:

A) A new Figure 5 which illustrates examples where Gal4 and Cre intersectionally drive expression in a small groups of neurons. In the accompanying text, we explicitly acknowledge the confound of variable expression.

B) A short description to the Materials and methods section describing the protocol that we use to minimize transgene silencing.

2) [Related to Essential revision 2] While I do not request more experiments to the authors, I think an in-depth analysis of the distribution of interneurons types based on neurotransmitter and neuromodulator expressions per brain area, which seems amenable to the authors based on the data acquired, would provide more relevant information to the reader and the field. In particular, it would be useful to take it a step further and analyze out of the ~92 000 neurons in the brain the putative distribution as a function of neurotransmitter, neuromodulator and/or neuropeptide types. This effort would constitute a critical resource for the field and seems possible to estimate with ZBB2 and the collection of transgenic lines mapped in the 6 dpf zebrafish larval brain.

As requested, we provide new supplementary information (Supplementary files 4 and 5) that describe the density of neurotransmitter/neuromodulator expression in different brain regions. For this, we have used both manually curated anatomical masks from Z-Brain, and second set of computational defined spatially smaller masks recently described by our group (Gupta et al., 2018). However, we cannot reliably extend this to a neuron-level description (if we understand the idea correctly) due to biological variability. Almost all brain regions contain multiple cell types that are intermingled, and – with the possible exception of the Mauthner neuron – specific cells are not precisely located at the same coordinates in different individuals.

3) [Related to Essential revision 2] Related to Figure 3: Seeing images of the lines or 3D views online is very nice qualitatively. Naive question here: I wonder if we could take it one step further to reach a quantitative representation of the expression over the entire brain space of the larva. Do the authors have a simple way to converge on a physical 3D map indexed in a matrix with absolute coordinates that we could refer to in publications from different labs?

The ZBB reference volume constitutes a 3D map with an absolute coordinate system in microns. We modified the code for the downloadable version so that irrespective of user-selected downscaling values, slices are now labeled by their position in ZBB reference space. The online version already displays the absolute coordinates of the selected voxel. This position can be reported in publications.

4) [Related to Essential revision 2] In order to locate with absolute coordinates the expression of transgenes better than by eye on the atlas: could the authors come up with a matrix of ~1000 bins (containing on average 10 neurons) for which each index corresponds to a graded value of expression on a 0-1 scale?

This is a great idea – thank you. We have added new Supplementary file 3 that provides coordinates for 1804 bins (20 µm side volumes) and the density of transgene expression in each. Using the bin coordinates, users can quickly navigate to the selected region in the atlas.
