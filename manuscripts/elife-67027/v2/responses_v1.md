# Author response - Round 1

Authors:
- Jordana K Thibado ([ORCID: 0000-0001-7293-5364](https://orcid.org/0000-0001-7293-5364))
- Jean-Yves Tano
- Joon Lee
- Leslie Salas-Estrada
- Davide Provasi ([ORCID: 0000-0002-2868-303X](https://orcid.org/0000-0002-2868-303X))
- Alexa Strauss
- Joao Marcelo Lamim Ribeiro
- Guoqing Xiang
- Johannes Broichhagen ([ORCID: 0000-0003-3084-6595](https://orcid.org/0000-0003-3084-6595))
- Marta Filizola
- Martin J Lohse
- Joshua Levitz ([ORCID: 0000-0002-8169-6323](https://orcid.org/0000-0002-8169-6323))

## Response text

DOI: [10.7554/eLife.67027.sa2](https://doi.org/10.7554/eLife.67027.sa2)

Essential revisions:

In general, the reviewers found this to be an interesting multi-faceted study in which a combination of experiment approaches were used to dissect out the molecular details about transmembrane determinants of mGluR dimerization. While there was enthusiasm for many aspects of this study, some concerns were raised about the structure of the narrative, interpretation of some results and that the concluding model was not well supported.

1. In general, the reviewers found this to be an interesting multi-faceted study in which a combination of experiment approaches were used to dissect out the molecular details about transmembrane determinants of mGluR dimerization. However, there were some concerns that the general narrative of the paper focused on guiding the reader towards the conclusions presented in Figure 8, rather than allow the reader to form their own objective interpretation. Thus, the manuscript should be edited to reduce the proselytizing structure. Furthermore, the model proposed remains hypothetical and is not sufficiently supported by the data presented and so Figure 8 should be removed from the revised manuscript. In addition, the paper needs to be shortened in order to improve readability. This can be achieved by removing sections such as the discussion of the Family A receptor dimerization, and the role of Ala in interfaces, which both do not directly relate to the results in this study.

We thank the reviewers for these suggestions. We have revised the writing in the manuscript to allow readers to form objective interpretations and to streamline the text to improve readability as suggested. Please see highlighted changes throughout the manuscript.

While the model presented in Figure 8 was meant merely as a guide to think about how both dynamic TMD dimerization and interface rearrangement may occur during mGluR activation based on both ours and previously published data from other groups, we appreciate the reviewers’ concern that this strayed too far from the data reported. We have thus removed Figure 8 and toned down the discussion to address the implications of our data and place it in the context of the rest of the literature without explicitly linking this to the framework of a specific state model.

2. Throughout the paper, the observation of different dimerization proportions has been generally interpreted as a change in stability, but this may not be the case. Since the stoichiometry has been captured from cell membranes, it could be that the dimerization proportion is defined during expression and is kinetically trapped. In this case, the results presented indicate a dimerization signal obtained with certain constructs and expression conditions. On the other hand, "stability" inherently implies an equilibrium affinity, and so use of this description should be reserved for occasions when equilibrium binding has been measured, i.e. when the binding isotherm with titration of the protein density in the membrane, with evidence of reversibility. At the very least, if the dimer signal is examined at a a single density, as is the case in these studies, then it must be shown that the dimerization signal arises from a dynamic equilibrium, e.g. with reversibility or competition with un-labelled species. While the studies presented in Figure 6B,D,F indicate dynamic changes, this is not clear for the data presented elsewhere in the paper.

Therefore, where absolute dimer population is reported (throughout, but especially Figure 7), the wording should be changed to remove terms like "stability", "weaker", "stronger", etc.… Instead, it is appropriate to describe this as an increase/decrease in dimerization signal or propensity.

We thank the reviewers for making this important point and their suggestions for improving the clarity of the text and figures to address this. We have revised the manuscript to remove terms like “stability” and “stronger/weaker” and edited where applicable to “increases/decreases in dimerization propensity” (see highlighted text throughout). In addition, we have added a short section to the discussion (p. 26, paragraph 1) to respond to the aforementioned issues regarding the limitations of SiMPull for addressing true differences in stability versus kinetically trapped populations. We’d like to note that while these limitations warrant future in vitro work to gain a deeper biophysical understanding of mGluR dimerization, the relative advantage of our approach is that it captures receptors directly from the plasma membrane of live cells and is, thus, likely to reflect the cellularly-relevant assembly.

We have also modified Figure 1H to reflect the reviewers’ concerns. We believe that the greater than (“>”) symbol (used in Figure 1H and 7L) is appropriate as it reflects the relative differences in propensity observed rather than implying that an equilibrium measurement has been made as was the case in the initial version. We have clarified this in the figure legend as well. We have also modified Figure 7H to make it clear that we are ranking dimerization propensity and not necessarily affinity.

To clarify the interpretation of the dimerization data, please include an explicit description of how the dimerization percentage was calculated in the methods. Specifically address whether this calculation includes a consideration of changes of the expression or does it assume it to be constant? Finally, show the expression data alongside the dimerization data in the main paper, instead of the supplement. This is essential to the interpretation of the results, and is analogous to showing loading control data in western blot figures. Finally, for the expression data, please add error bars and statistical tests.

To clarify the interpretation of dimerization data, we have added a description of how the dimerization percentage was calculated to the “Single-molecule pulldown and subunit counting” section of the methods section (page 33). The description is as follows:

“Single molecule fluorescence time traces were manually classified as having 1, 2, 3 or 4 bleaching steps or were discarded if no clear bleaching steps were identified. […] This calculation makes no correction for expression level.

%dimerization=((Observedvalue)−Minvalue)*100Maxvalue−Minvalue”

We have also added expression data alongside the dimerization data in the main and supplemental figures wherever relevant (see Figure 1E, G; Figure 2D, F, H; Figure 2—figure supplement 4C; Figure 2—figure supplement 5C, G; Figure 2—figure supplement 6E; Figure 3—figure supplement 2B, C; Figure 5C; Figure 5—figure supplement 1B, C; Figure 6B, E, H, Figure 7C, F, I, K). All expression plots show individual points, error bars, and statistical tests (unpaired t-tests for 2 conditions or one-way ANOVA plus Tukey-Kramer) are described in the associated figure legends and relevant source files. Note that for 2-color experiments in Figure 7 we now report data on the ratio of expression level of the CLIP-tagged (i.e. prey) and SNAP-tagged (i.e. bait) construct as this is the key parameter for determining the potential effect of expression differences on relative pulldown efficiency. In all cases there are no significant differences in expression ratios between conditions.

3) The computational studies are set up in a rigorous manner, with many replicate systems and extended simulation times (the amount of work presented could fill its own paper). However, the connection between the computational analysis and the rest of the paper is a little unclear. For example, many interfaces are identified in the analysis, but the focus remains on TMD4 and TMD6 with the additional interfaces generally ignored. The presentation of the logic between the results from these studies and the rest of the paper should be improved. In addition, the relegation of this work to the supplement has perhaps led to the omission of key details that are important for interpreting the results. Analysis of the sampling achieved, and convergence of results must be included. In the case of the trajectories used for the Markov state analysis, does the protein sample multiple conformations in the same trajectory, or is the sampling of states achieved by the many parallel simulations? A discussion of the lag time analysis was stated, but should be shown. Furthermore, for the free energy estimates from the steered MD, how was convergence over the 30 runs assessed? All of these analyses should be provided even if the data is not presented in the main figures.

We thank the reviewers for this critique and acknowledgement of the rigorous manner in which the computational study was conducted. Indeed, placing this work in the supplement led to the accidental omission of a few key details, which we have now included in the revised manuscript. We have also moved the description of the CG MD simulations of isolated TMDs into the first section of the results to complement the key initial finding that the mGluR2 TMD shows a higher dimerization propensity than mGluR3. We then revisit the different TMD interfaces in the full-length context in the second part of the Results section to complement our sequence analysis of TM4. We have added the following information:

– A table (Figure 1—supplemental table 1) showing that while most individual trajectories used for the Markov state analysis only sampled one dimeric macrostate, several trajectories sampled more than one dimeric configuration.

– A plot (Figure 1—figure supplement 5) showing the implied timescales as a function of lag time. See accompanying text describing this on page 9, paragraph 1.

– A table (Figure 1—supplemental table 2) showing further information regarding the TM helices involved in the most frequent interfaces associated with each assigned microstate used for the reactive flux analysis.

– Plots (Figure 2—figure supplement 2) illustrating convergence of the free energy differences between representative full-length dimeric configurations of highly populated macrostates.

The contribution of the computational studies stems from their revelation that inter-TMD interactions are highly complex and dynamic with many underlying microstates. However, grouping these microstates into macrostates according to both a >40% helix probability of being at an interface and the largest number of contacts formed by each helix, draws attention to TM1, TM4, and TM5 in the case of mGluR2 or TM3 and TM7 in the case of mGluR3 based on calculated macrostate probabilities larger than 10%. Although these helices are involved in highly probable macrostates in the two receptors, this probability is tuned in the context of a full-length receptor, which favors symmetric TM4 interfaces in mGluR2 over other highly probable ones such as symmetric interfaces involving TM1. We have clarified these observations in the discussion (p. 26, 28), admitting that a complete validation of the computational predictions will require further investigation.
