# Peer review - Round 1

Editors:
- Dominique Soldati-Favre, University of Geneva Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54129.sa1](https://doi.org/10.7554/eLife.54129.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This a welcome and timely study of individual parasite gene expression the asexual phase of several stains of Toxoplasma gondii covering both tachyzoite and bradyzoite development with a SmartSeq2 approach, which represents a significant contribution to the field. It leverages and confirms earlier cell cycle work of others while also nicely informing on biological differences between individual parasites and strains during asexual growth and differentiation. The work also illustrates how new regulatory pathways can be identified and the extent to which they can be conserved over vast evolutionary timescales.

Decision letter after peer review:

Thank you for submitting your article "A single-parasite transcriptional landscape of Toxoplasma gondii reveals novel control of antigen expression" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Dominique Soldati-Favre as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jessica Kissinger (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors have performed rigorous controls and experimental design and made the data freely available in both its raw form and through a user-friendly interface. The discoveries are significant and it is tantalizing to consider what other insights may be gained with additional and deeper exploration of strains with phenotypic differences. Overall this is an outstanding study and an important resource for the community that deserves publication once suggestions/reservations about some aspects of the analysis and the manuscript will have be addressed.

Essential revisions:

1) Several points of clarifications

– As not all individual single-cell experiments were successful, it may make more sense, except when discussing the success rate, to utilize the numbers of parasite datasets (as opposed to parasites) that could actually be compared, e.g. paragraph five of subsection “Hidden heterogeneity in asexually developing Toxoplasma”, since only 1552 datasets could be compared.

– RH genome/gff files that were used represent only 4 Mb of sequence data including and the gff file only contains annotation for the plastid genome sequence. Paragraph two of subsection “Technical validation of single-parasite sorting and sequencing” states that RH reads were mapped to the GT1 genome sequence but this is not reflected in the Materials and methods where only TgME49 and RH are mentioned as reference sequences. The manuscript should more clearly represent exactly which genome sequences and sources were utilized in the methods. See also subsection “Sequencing alignment”.

– It is great that the authors consider the "multiple-mapping problem" and devise a work-around. There is however another issue related to genome misassembly and compressed multi-gene families or recent segmental duplications. This is an issue for most genome sequences and cannot be resolved here but it would be good to acknowledge the effect that missing gene family members may have on the analysis of the results. Specifically, did the genome sequences used contain the "unassembled contigs".

– Subsection “An open-source interactive resource for visualizing single-Toxoplasma atlas” – any thoughts about the longer-term sustainability of the atlas resource? Have the sequence data been deposited in the SRA read archive?

– Discussion paragraph three – why is mRNA concentration affected by the size of the well and reaction volume used? there is still only a single cell in the assay, but the reaction volumes are greater. Saturation was proven to not be a problem with the smaller 384-well format but here, sensitivity to low copy number is favored. Please clarify.

– Figure 1—figure supplement 2, what is panel b really telling us? are differences in genome assembly or annotation skewing the results? Also by ORF do you really mean CDS? how were these obtained? they are not mentioned in the Materials and methods.

2) The authors have chosen some surprising parameters in the mapping:

– The star aligner parameters for max intron and mate gap size is set to 1Mbp, this has been found to lead to some incorrect mapping in other systems and can result in low level misattributed reads; whilst this is not likely to sway the presented analysis in a significant way, it should be checked.

– The choice to include and distribute multiply mapped reads of equivalent quality across different genes is somewhat problematic as it will result in one initial read to be attributed to several genes which is not a true reflection of the underlying signal. The results might be particularly biased in the analysis of the multigene family. Apart from recovering a more important number of genes per cell which is not a valid aim in itself, the authors have not justified why this is needed and not demonstrated that it does not impact their downstream analyses significantly.

3) In the analysis relating the organelle-specific expression clustering, the authors successfully identify correctly and mis-attributed organellar proteins described in the literature. This approach is promising but the further clustering of pseudotime in 3 clusters seems unnecessary, hierarchical clustering of each organellar set ordered in pseudotime may be more informative. Moreover, it could be interesting to compare gene expression patterns and cluster them finely on the whole dataset so as to potentially identify proteins not yet ascribed to any organelle but who share expression patterns with those already described.

4) The bradyzoite diversity observed and the strain specific differences is a significant observation. The authors have not attempted to understand the transcriptomic circuitry that underlies decision to bifurcate to a bradyzoite fate and the strain specific differences associated with that decision. The authors hypothesize that P3 might be a state from which parasites can trifurcate into the cell cycle or either of the two separate bradyzoite clusters. This could be tested and described more granularly by further sub clustering, pseudotime ordering and branching analysis to understand the transcriptomic determinants of bifurcation into these fates.

5) The claim of antigenic switching based on a single cell with a different SRS expression pattern, although an interesting initial observation, seems over-interpreted based on the data presented. It is not clear what the author's hypothesis is with regards to this cell, i.e is it the only cell undergoing switching in the population? Why does it express a sexual stage SRS? Does the SAG1 protein signal disappear completely upon transfection with the AP2? The switching mediated by the AP-2 would need a more single cell measurement of the pattern of antigen expression (e.g. scRNA-seq of sorted parasites with different levels of the AP2), although this would be a big undertaking. The authors should either add more data to complete this observation or alternatively should critically discuss their observations and tone down their conclusions.
