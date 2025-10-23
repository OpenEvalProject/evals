# Author response - Round 1

Authors:
- Arne Elofsson ([ORCID: 0000-0002-7115-9751](https://orcid.org/0000-0002-7115-9751))
- Ling Han
- Enrica Bianchi ([ORCID: 0000-0001-8124-7328](https://orcid.org/0000-0001-8124-7328))
- Gavin J Wright ([ORCID: 0000-0003-0537-0863](https://orcid.org/0000-0003-0537-0863))
- Luca Jovine ([ORCID: 0000-0002-2679-6946](https://orcid.org/0000-0002-2679-6946))

## Response text

DOI: [10.7554/eLife.93131.3.sa3](https://doi.org/10.7554/eLife.93131.3.sa3)

The following is the authors’ response to the original reviews.

Reviewer #1

The authors should include experiments such as Cryo-EM and genetically modified animals to demonstrate the physiological importance of the TMEM81 complex.

While we intend to pursue cryo-EM studies of the putative complex (or subcomplexes thereof), this is clearly not a straightforward endeavor and goes beyond the scope of the present manuscript. Concerning the generation of genetically modified animals, we would like to underline that the majority of the proteins that we used for AlphaFold-Multimer complex predictions were precisely chosen based on the fact that - as detailed in the publications referenced in the Introduction - ablation of the respective genes caused sex-specific infertility due to defects in gamete fusion (the other criterion used for inclusion being structural similarity to IZUMO1 coupled with expression in the testis (IZUMO2-4 and TMEM81), or evidence from other kinds of experiments in the case of human-specific MAIA). Concerning TMEM81, experimental evidence for a direct involvement in gamete fusion is described in the referenced preprint by Daneke et al., which was submitted to bioRxiv concomitantly with the present work.

Reviewer #2

I believe that the manuscript would benefit from the authors providing more information about the systematic search (Figure 4). For example, by indicating for each pair tested the average pDock score in a 2D plot (or table) and as raw data in the supplementary information.

Figure 4 has been modified to report both the top and the mean ranking scores for every interaction. Furthermore, additional metrics for the systematic search summarized in Figure 4, including pDockQ scores, are provided in this manuscript revision as supplementary Table S1.

A global search, such as including all membrane proteins expressed in eggs or sperm, could not only be more informative but could also allow the reader to understand the pDock score discrimination power for this particular subset.

The possibility of carrying out a global search was evaluated by performing preliminary computational experiments on an extended ensemble of sperm and egg proteins. In order to do so, we compiled a list of sperm membrane proteins by referring to 4 proteomic datasets (PMIDs 36384108, 36896575, 31824947, 24082039) and identifying ~600 proteins that were found in at least two of them; among these, 250 were single-pass type I or type II membrane proteins, or GPI-anchored proteins. Similarly, a list of 160 egg surface membrane proteins, excluding multipass and secreted ones, was obtained by comparing oocyte cDNA library NIH_MGC_257_N (Express Genomics, USA) with 4 proteomic datasets (PMIDs 35809850, 36042231, 29025019, 27215607). As we briefly commented at the beginning of the section “Prediction of interactions between human proteins associated with gamete fusion” of the revised manuscript, the tests carried out using the resulting list of sperm and egg proteins suggested that interpreting the results of a global search would be severely complicated by a relatively large number of putative false positives. Moreover, the tests showed that performing a complete systematic search would be beyond our current access to computing power. Based on these observations, we preferred to maintain the present study limited to proteins that had been previously clearly implicated in gamete fusion and/or matched specific structural features of IZUMO1.

Figure 5 could be improved in clarity by schematically indicating to which cell each protein is anchored.

This has been done in the revised version of the manuscript.

Reviewer #3

Major comments

(1) In Figure 1, how the protein of mouse/human IZUMO1 and JUNO is purified is not mentioned in the main text nor in the Methods. Are the mouse IZUMO1-His and mouse JUNO-His transfected together or separately? Are human JUNO-His and human IZUMO1-Myc transfected together into HEK293 cells? And purified by IMAC?

Transfection information has been included in the Methods section “Protein expression, purification and analysis” (previously “Protein expression and purification”). Concerning the purification procedure, we had already stated in the legend of Figure 1 that human JUNOE-His/IZUMO1E-Myc had been purified by IMAC before SEC, and have now done the same for mouse JUNOE-His and IZUMO1E-His.

(2) It would be easier to understand the figure if the author could run a WB to indicate which band above JUNO is specifically IZUMO1-Myc in Figure 1.

This has been done and reported in a new Figure S1 (with the original Figure S1 having now become Figure S2). Details about the antibodies used for immunoblot have been included in both Methods section “Protein expression, purification and analysis” and the Key Resources Table.

(3) Figure 4: Analysis of more proteins that have been suggested as possible candidates for sperm-egg interaction will help to highlight the following results. Also, providing a score for the possibility of interaction might help in selecting those proteins in Figures 5 and 6.

Please refer to the answer to the first question of Reviewer #2.

(4) Figure 7: The authors take advantage of the latest developments in protein structure and interaction to model protein complex formation. However, some experimental experiments such as Co-IP, pull down to support the prediction to verify some of this predicated interaction is necessary.

We agree with the reviewer; however, for the reasons we discussed during our comparison of the biochemical properties of the JUNO/IZUMO1 interaction between mouse and human, pursuing this line of inquiry will likely necessitate an extensive set of parallel experiments using proteins from different species. This work is being planned and will be the focus of future studies. However, as we mentioned at the end of the Abstract, one should also consider that some of these complexes are likely to be highly transient. Because of this, while they may have important regulated roles in vivo (function at a specific time and place), they could be very challenging to detect using standard approaches in vitro. We thus see this as a significant advance that structural modeling could contribute to the identification of such functionally important but transient interactions.

Minor points

(1) In the abstract, "three sperm (IZUMO1, SPACA6 and TMEM81) "should be "three sperm proteins."

The Abstract has been condensed to fit within the suggested 200-word limit and, as part of this, the sentence has been changed to “complex involving sperm IZUMO1, SPACA6, TMEM81 and egg JUNO, CD9”.

(2) How do the predictions of the binary complex IZUMO1/CD9 (Figure S1B) or IZUMO1/CD81 (Figure S1C) suggest "the two egg tetraspanins are interchangeable"? Was it because they are quite similar? Please provide more explanation for this speculation. Interchangeable by function or for complex formation? To support the conclusion, biochemical data is required. Otherwise, it needs to be toned down.

This is because, in the AlphaFold-Multimer predictions of the pentameric complex, CD9 and CD81 are placed in essentially the same way relative to the other subunits.

We have now clarified this at the end of page 6:

“(...) suggest that the two egg tetraspanins are interchangeable because they are predicted to bind to the same region of IZUMO1; (...)”

(3) It would be more reader-friendly if the author could label the name of each protein in the figure in Figure S1, especially when the name is not written in the figure legend.

This has been done in Figure S2 of the revised manuscript (corresponding to original Figure S1).
