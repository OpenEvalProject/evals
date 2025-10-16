# Author response - Round 1

Authors:
- Austin T Baldwin ([ORCID: 0000-0002-6099-0873](https://orcid.org/0000-0002-6099-0873))
- Juliana H Kim ([ORCID: 0000-0001-6634-4525](https://orcid.org/0000-0001-6634-4525))
- Hyemin Seo
- John B Wallingford ([ORCID: 0000-0002-6280-8625](https://orcid.org/0000-0002-6280-8625))

## Response text

DOI: [10.7554/eLife.66704.sa2](https://doi.org/10.7554/eLife.66704.sa2)

Essential revisions:

1) The authors need to revisit their conclusions, which in places are overextended. For example, it seems too much to conclude that "the primary effect of shroom 3 in the anterior neural plate is …on the coupling of medial actomyosin …with medial N-cadherin accumulation" (p 10, bottom). It is the most obvious change in their current data set, but that data set seems too limited to call it the "primary effect".

Similarly, the manuscript strength is the new analytical approach of molecular and cellular changes at tissue scale rather than in increasing the understanding of neural tube morphogenesis. Therefore, we suggest to better frame the manuscript around this new analytical approach and its capacity to yield data of great richness for understanding morphogenetic processes in vertebrates.

Addressing the points raised below will support the potential of the approach for gaining mechanistic insights and overall strengthen the manuscript.

We have re-written much of the manuscript, focusing on the technical advances here, but also clarifying the distinctions between our findings and our conclusions, which in most cases we have softened.

Furthermore, we have now removed data that we deemed superfluous, thereby shortening and simplifying the manuscript.

2) Estimating molecular concentration: Please clarify and address whether the molecular concentration of analyzed proteins has been corrected for change in size of the analyzed area over time. For example, the medial N-cadherin increases with apical constriction (Figure 6), but is this because the apical surface is getting smaller (i.e. same amount of apical N-cadherin, but now more concentrated) or is there an increase in the total amount of protein in the apical surface?

Yes, we report changes in the mean pixel intensity normalized for area. This has been clarified in the revision on lines 147-149.

3) Clarify the analysis of medial signals: How do the authors correct for noise in their analyses? Lifeact can also bind G-actin and some of the punctate N-cadherin-GFP could potentially be in vesicles rather than at the apical membrane (see also point 5).

To account for "noise" within our data, we have smoothed the data by averaging the data in individual cell tracks over a 7-frame/minute window. We have included a description of this in the main text (lines 149151) and included a diagram in Figure 1 figure supplement 1. As LifeAct cannot strictly distinguish between F-actin and G-actin, we have not distinguished between F-actin and G-actin in the manuscript. We now explicitly describe what we observed and our interpretation thereof. We now also report on the apicobasal position of N-cad relative to actin (lines 197-200, Figure 4) and we discuss the possible mechanisms of action for medial N-cad (Discussion, lines 448-462).

4) The non-junctional distribution of N-cadherin and its dynamic changes during apical constriction represent an exciting result. However, solely using ectopically expressed N-cadherin-GFP to investigate its function is not sufficient, as it may introduce overexpression artifacts. Please provide data corroborating that endogenous N-cadherin behaves similar to the exogenous protein. We appreciate that based on the available reagents (e.g. antibodies) this would likely represent static images. If this proves experimentally not possible, this should at a minimum be addressed in the text.

We agree this is crucial. We therefore examined this issue using immunostaining for endogenous Ncadherin. These experiments, presented in the new Figure 3 figure supplement 1 and lines 194-197 confirm our findings with N-cadherin-GFP.

5) Could the current data be used to assess the trafficking of the N-Cadherin? For instance, can the authors determine if N-cadherin moving from junctional to medial locations, is being trafficked directly to the medial membrane, or being internalized from the medial region, or perhaps some other dynamic behavior. This could help provide more information regarding the mechanistic role of N-cadherin.

We regret that we do not have enough time resolution (1 frame per minute) to resolve the directionality of N-cadherin movement. However, we have shown some new images from our data that provide some insight into the relative apicobasal positioning of actin and N-cadherin (Figure 4), and we discuss the possibility of N-cad endocytosis (lines 197-203 and 448-462).

6) Does medial N-cadherin co-distribute with Myosin II, ppRLC, or Rho-kinase? Based on previous studies of apical constriction in other model systems this is an attractive assumption. This should be tested experimentally to support and mechanistically corroborate the correlation of molecular events and cell shape changed described in this manuscript. For instance, combine N-cadherin with a MyosinII, a GTP-Rho localization sensor (e.g. Bement lab) or the AHPH system (Piekny and Glotzer, 2008) reporter to generate relevant time-series.

We agree that these are interesting experiments, but as the reviewers themselves point out in Point 14 (below), examining these additional markers is extremely daunting given the scale of each experiment here. Thus, we followed the advice in Point 14 and now clearly discuss this limitation of our approach and leave analysis of other markers for a future paper.

7) Given that non-junctional N-cadherin has been associated with diverse cellular functions apart from adhesion, please discuss its possible role in this current context.

The possible roles for medial N-cad are now discussed in lines 448-462 of the discussion.

8) Support the functional inactivation of Shroom3: The sequence analysis provided is compelling but actually demonstrating reduced protein would strengthen the method.

What proportion of indels are 3 bp or multiple of 3, could resulting in-frame deletions or monoallelic indels explain for instance the 2 populations observed for instance in Fig5D, E?

Unfortunately, there are no available antibodies that detect Shroom3 protein in Xenopus (mouse antibodies do not cross-react). We hasten to add, however, that all aspects of the phenotype we observe with shroom3 CRISPR recapitulate known phenotypes not only of shroom3 morphants in Xenopus but also of dominant-negative shroom3 in Xenopus and genetic mutants in mice. This explicitly stated now in the manuscript, and coupled to our sequence analysis, we hope these findings will satisfy the reviewers.

Regarding the proportions of indels and their relationship to phenotypes, we have no way of exploring this possibility. That said, as we now clarify in the revision on lines 236-239 and in Figure 5 figure supplement 1A, our sgRNA targets amino acid ~28 of the ~3000 amino acid Shroom3 protein, making it unlikely that distinct change-of-function mutations could be introduced. We therefore feel it more appropriate not to speculate on the issue.

Moreover, please clarify which particular domain is targeted by the Shroom3 gRNA employed in this study? How is it expected to impair its function, e.g. complete loss of function, deletion of a specific functional domain? If the latter, could a truncated protein exert partial functions? How would this effect interactions with actin or N-cadherin and relate to the specific phenotypes observed?

As noted in point 8, above, the sgRNA targets amino acid ~28 of the ~3000 amino acid Shroom3 protein. This is substantially N-terminal to all defined domains in the protein. This is now stated on lines 236-239 and diagrammed in Figure 5 figure supplement 1A.

9) Shroom3 spatial expression: How is Shroom3 expressed throughout the extent of the anteroposterior neural epithelium, given that it seems to exert different effects in the anterior and posterior parts? Likewise, would be important to see the Shroom3 subcellular distribution in the neural plate to determine if there is a population of Shroom3 in medial positions analogous to N-cadherin.

Xenopus shroom3 is expressed along the entire length of the closing Xenopus neural plate (Haigo et al., Current Biology 2003), as we now indicate on lines 86-88.

As for the protein localization, unfortunately no antibodies that detect Xenopus Shroom3 are available. Compounding this problem, ectopic expression of wild-type Shroom3 causes a severe gain-of-function phenotype in early embryos, eliciting strong apical constriction of blastomeres that precludes analysis of Shroom3-GFP localization at neural plate stages.

That said, ectopically expressed, tagged Shroom3 clearly decorates the entire apical surface in diverse epithelial cell types (see Haigo, 2003; Lee et al., 2009), and this point is now made on lines 204-208 of the revision.

Finally, in a more direct attempt to attempt to address this concern, we took a cue from previous work on Drosophila Shroom, and we expressed a C-terminal (Rok-binding domain) truncation of Xenopus Shroom3.

We found his construct co-accumulates with both medial and junctional actin in the closing neural plate. These data are now discussed on lines 208-214 and shown in Figure 4 figure supplement 1.

10) Clarification of sample numbers and data integration of different samples: The samples included in this study and presented in Methods Appendix2 display apparent differences, therefore additional information is required for the number of samples that contribute to each analysis and how data were compared and/or integrated. For instance, the anterior samples show differences in cell size and asymmetries within the tissue. Please explain the reason for this and how is this accounted for when comparing quantifications between samples. This should include how staging between samples was achieved, and the related registration allowing comparison of resulting cell behaviors.

Differences in cell size and fluorescent intensity arise from many sources: (a) staging, (b) natural variation, (c) variation arising from microinjection of mRNAs, etc. As such, we have focused not so much raw values of size and intensity, but rather in the changes in these values over time. Thanks to our cell tracking paradigm, we are able to mean-center and scale cell size and fluorescence parameters per individual cell track and convert measures of area and fluorescence (i.e. microns and arbitrary units) to standard deviations. Thus both within and between embryos, each cell is analyzed individually for relative changes in parameters over time and then integrated into the overall dataset. We have clarified this in the text on lines 157-164 and is additionally diagrammed in Figure 1 figure supplement 1.

Related to this, there seem to be only two posterior samples containing Shroom3 crispant cells, please describe the variability between samples, similar to above. If only two samples were interrogated, a third sample needs to be included. In general, the sample number per experiment should be greater than two.

We have now included additional videos and analysis.

11) Describing the data analysis. Please introduce in the Results a few sentences that explain the "standardization" approach that are used to present the data. While this is in the Methods and Appendix, the approach is not one commonly seen, and it would be good to orient readers less familiar with the approach.

As described above in response to Point 10, we have improved the description of this method on lines 157164 of the main text and diagrammed the standardization in Figure 1 figure supplement 1.

12) Facilitating the interpretation of some the 2D density plots in figure 10. Consider an alternative way or simplification of the graphs without breaking the data out into several additional graphs. If difficult, a more detailed description in the methods should be helpful to the reader and included.

We have broken out a large part of the data in Figure 10 (now Figure 11) to Figure 11 figure supplement 1 to aid with legibility. These data are now described in more detail and the original plots have now been annotated to guide the reader (Figure 11C, cyan ellipses). In addition, histograms have been extracted from different regions of the plots (Figure 11H) to provide more granular view of specific results.

13) The 2D density plots in figure 6D and E have such sharp edges; they look artificial. Please check and address whether this is just an issue with the PDF, thresholding, or some other technical issue.

This was a technical issue with a background layer on the plots. This background layer has been removed in all density plots in the manuscript.

14) Discuss limitations inherent to the approach, including: (i) a relatively limited number of molecular parameters are interrogated (F-actin and N-cadherin). It is possible, for example, that changes in contractility which drive junctional shortening (relevant for the analysis in Figure 10) are due to changes in actin organization (that may not be readily captured by overall measures of quantity) or activity of Myosin II (which is not measured here). Given the scale of the experiments that are involved, it would be technically challenging to interrogate more molecular players at the same time, representing a potential limitation.

(ii) the dynamics are relatively coarse-grained. For example, changes in cadherin levels that occur over hours may not capture changes in molecular turnover.

Limitation of the approach are now discussed on lines 463-477.
