# Author response - Round 1

Authors:
- My-Tra Le
- Wojciech K Kasprzak
- Taejin Kim
- Feng Gao
- Megan YL Young
- Xuefeng Yuan
- Bruce A Shapiro
- Joonil Seog
- Anne E Simon ([ORCID: 0000-0001-6121-0704](https://orcid.org/0000-0001-6121-0704))

## Response text

DOI: [10.7554/eLife.22883.019](https://doi.org/10.7554/eLife.22883.019)

Essential revisions:

1) Subsection “5A is implicated in RdRp binding to a 3’ end fragment”, first paragraph: It seems surprising that a loss of binding of the RDRP to m74 would only reduce transcription by 3.6-fold. Perhaps the authors could address this better. Were there differences in the salt or Mg2+ concentrations between the transcription reactions and the binding studies?

The transcription reactions contained 100 mM potassium glutamate, which was not present in the binding reactions. Other salt and magnesium concentrations were identical. It is known that the 3’ terminal hairpin in conjunction with upstream hairpin H4 is sufficient to confer a low level of transcription by the RdRp. The following sentence was added to this section and the new reference was added to references:

“The ability of the RdRp to continue transcribing low levels of complementary strands in the absence of 5A binding is likely due to the presence of the 3’ terminal Pr hairpin, which in combination with upstream hairpin H4 can promote a low level of transcription (Sun and Simon, 2006).”

2) Many of the figures and labels on the figures are too small to easily read.

We have enlarged the fonts in most of the figures.

3) It is unfortunate that all the SMD simulations were done in the absence of Mg2+ when their data clearly shows that Mg2+ plays an important role.

As we stated in the Molecular Dynamics section (perhaps not sufficiently clearly) we cannot perform reliable MD or SMD simulations including Mg2+ ions because we have no experimental data on Mg2+ ion placement in TCV TSS. Ab initio prediction of proper Magnesium ions placement and determination of their influence on the TCV TSS structure is not a feasible alternative because it is currently impossible to perform microsecond time scale simulations that would be necessary to achieve proper Mg2+ coordination.

We can only speculate, partly based on the observed impact of extended persistence of tertiary interactions involving H4b in some SMD simulations (as described in MD simulations of TSS unfolding section and in the Supplementary Information), that Psi2-Mg2+ interactions could alter the order of TSS building blocks opening, perhaps leading to the H4b/Psi2 and H5 opening in parallel, coupled by magnesium-mediated tertiary interactions (that would be observed as one OT rip), while the Mg-strengthened H4a/Psi3 could still offer proportionally more resistance to pulling and open last.

4) The authors propose a model where by the RDRP binds to the 5A and downstream regions which disrupts the PK3 and this is what leads to unfolding of the rest of the TSS element. However, addition of an oligo to H4a/PK3 was unable to bind due to the stability of the RNA structure. The question arises as to how the RDRP is binding to this short region that is presumably in accessible to disrupt H4a/PK3, since the authors suggest that some of the adenosines interact with the major groove of PK3.

Binding of an oligonucleotide requires formation of particular hydrogen bonds that are not necessarily the hydrogen bonds (and ionic bonds) that are involved in protein binding. Furthermore, the RdRp may be recognizing the adenylates within the structure of H4a/Psi3, which would be very different from accessibility to unpaired (or breathing) nucleotides that are required for the oligonucleotide.
