# Author response - Round 1

Authors:
- Anahita Bakochi ([ORCID: 0000-0001-8144-8525](https://orcid.org/0000-0001-8144-8525))
- Tirthankar Mohanty
- Paul Theodor Pyl
- Carlos Alberto Gueto-Tettay
- Lars Malmström ([ORCID: 0000-0001-9885-9312](https://orcid.org/0000-0001-9885-9312))
- Adam Linder
- Johan Malmström ([ORCID: 0000-0002-2889-7169](https://orcid.org/0000-0002-2889-7169))

## Response text

DOI: [10.7554/eLife.64159.sa2](https://doi.org/10.7554/eLife.64159.sa2)

Essential Revisions:

1. In some cases the actual pathogens may have left their peptides in CSF. Have the authors tried to detect them by a species wide search? Of course, this may require shotgun data.

We completely agree. In fact, at the onset of this project our main aims were to detect both pathogen-specific and -induced host patterns in the CSF as well as peptides from the infecting pathogen directly in these CSF patient samples to increase predictive power of our analysis. To accomplish this goal, we generated 8 different pathogen assay libraries for the most prevalent pathogens; Escherichia coli, Enterococcus faecalis, Streptococcus pyogenes, Streptococcus agalactiae, Listeria monocytogenes, Pseudomonas aeruginosa, Staphylococcus aureus and Streptococcus pneumoniae. The pathogens were by grown in vitro and analyzed by DDA and DIA to generate the libraries. We have now made the source data and the assay libraries publicly available and deposited to the ProteomeXchange Consortium via the PRIDE partner repository with the dataset identifier PXD024904 as a resource for the community. Description of the bacterial sample preparations and data analysis for the library generation is in the "Materials and methods" section. Unfortunately, the samples in this cohort were sterile filtered, which is a possible explanation why we could not detect the proteomes from the microorganisms in these samples.

2. The authors may want to comment on their proteome coverage in the main text. I understand that this is somewhat delicate for a body fluid, but at least the number of proteins confidently detected would be interesting.

As requested, have added the numbers of confidently detected and quantified proteins in total, as well as for each sample group separately (ABM, BM, VM and controls). This information can be found in the Results section "Changes in the proteome pattern in CSF during meningitis" on rows 129-131.

3. It would be helpful in Figure 2 and 3 if the authors could highlight specific proteins in the volcano plots. For instance where are some of the predictive proteins shown in Figure 4c, such as A1AT, APOE, GELS, TTHY, etc?

The volcano plots in Figure 2 are relatively small, adding individual protein labels would make the figure unreadable and visually disagreeable. Instead, we added a new figure supplement "Figure 4—figure supplement 1" (Visualization of the 18 predictive proteins in volcano plots), where we have reproduced the same volcano plots from Figure 2 in a larger format. In these volcano plots we have included all the protein labels for each of the 18 predictive proteins as requested. We have further mentioned the new "Figure 4—figure supplement 1" in the manuscript in the Results section "Predictive proteomic patterns using LASSO regression modeling" on row number 215.

As for the scatter plots in Figure 4, none of the predictive proteins were found within the limits of the scatter plots, and therefore no alterations have been made to these figures.

4. A brief discussion is warranted regarding whether the CSF protein-pathogen associations found in this work have been previously reported in the literature, or represent entirely novel associations.

We have searched the literature for CSF protein-pathogen associations of the LASSO-generated predictive proteins. For several of these proteins we were unable to find any cross-references that would demonstrate an association between the CSF levels of one of our predictive proteins and meningitis. These proteins include ANT3, CATD, CD14, CFAH, CLUS, DKK3, ENPP2, FCGBP, GELS, HEP2, HPT, ITIH2, PROS, SCG1 and TTHY. For the other predictive proteins (A1AT, A2GL and APOE) we found references that suggest elevated protein levels are found in the CSF during meningitis. This matter is discussed in the Discussion section, on row numbers 295-300.

5. It would be helpful for the authors to perform some type of analysis to depict the localization of the proteins detected (e.g., classically secreted proteins versus membrane versus intracellular). For instance I already see in Figure 4c that ANT3 is mitochondrial. Is there an enrichment of classically secreted proteins in this dataset?

We have now done an analysis of the predicted subcellular compartment of the detected proteins for each sample group (ABM, BM, VM and control). This analysis is presented as grouped bar plots in a new "Figure 2—figure supplement 2". In "Figure 2—figure supplement 2A" we have reported the percentage of proteins belonging to each compartment per sample group, and in "Figure 2—figure supplement 2B" the total average intensity of each proteins belonging to corresponding subcellular compartment. This analysis is now also discussed in the manuscript in the Results section "Changes in the proteome pattern in CSF during meningitis" on rows 134-139.
