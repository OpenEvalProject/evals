# Peer review - Round 1

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67516.sa0](https://doi.org/10.7554/eLife.67516.sa0)

This paper will be of interest to scientists who study hematopoiesis. The authors combine single cell RNA-seq with bulk RNA-seq of transcripts from blood cells in the Drosophila larval hematopoietic organ. They present extensive analysis of the datasets, and the pseudotime analyses present a model of how hematopoietic progenitors can differentiate along transitory paths. These datasets reveal cell-type specific isoform expression of Notch pathway regulators, and genetic experiments prove the importance of these factors in development of one lineage. These transcriptomic analyses and subsequent genetic experiences provide strong support for the major claims of the paper.


---

# Peer review - Round 1

Editors:
- Erika A Bach, New York University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67516.sa1](https://doi.org/10.7554/eLife.67516.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review of original submision:

Thank you for submitting your article "Paths and Pathways that Generate Cell-Type Heterogeneity and Developmental Progression in Hematopoiesis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Erika A Bach as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Anna Akhmanova as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Address issues with AUC scores:

a) Define how you established the AUC list.

b) Clarify how you define AUC scores that are statistically significant.

c) Include a zero (0) on the y-axis of all graphs and P values for all graphs.

2) Provide a comparison of the data between the replicates.

3) Provide validation of some of the genes associated with clusters/sub-clusters, including Delta in MZ1, PSC, X and MZ2 clusters, and Ubx in posterior lymph gland lobes, and provide validation to support your model that there is no transition path for IZ to proPL.

4) Demonstrate the potency of RNAi lines, including pnt RNAi.

5) Explain the main differences and similarities between your data set and Jiwon Shim's by addressing specific issues such as Cluster "PH1" (your MZ1, PSC, X and MZ2 clusters) and Cluster X (and include a dot plot representation of Cluster X).

6) Provide additional quantification of CC in "Numb and Musashi in CC determination", additional information on how Numb intensity was quantified, and P values

7) Provide for lymph gland analyses the quantification of CC and MZ indexes and P values.

8) Consider using dot plots instead of box plots.

9) Provide in the main figures a list of the key genes defining each sub-population inside the different clusters.

10) Provide the number of cells in each cluster, including the IZ cluster.

11) Provide a schematic representation of crystal cell specification and maturation involving Notch, Numb and Sima.

12) Make extensive editorial changes, including shortening the manuscript per the reviewers' suggestions and clarifying the narrative so that the introduction covers what is actually being treated in the manuscript. For example, the introduction discusses the IZ but then the manuscript does not provide much insight into this cluster and instead focuses on CCs.

Full Reviews

Reviewer #1/Reviewing Editor:

Girard and colleagues combine bulk RNA-seq and scRNA-seq of FACS sorted blood cells from the larval lymph gland, the hematopoietic organ in Drosophila, to identify cell types and differentiation paths. The lymph gland is comprised of medullary and cortical zones. At least five cell types are found in the lymph gland: niche-like cells (termed the PSC), progenitors (termed prohemocytes) that are found in the MZ, intermediate progenitors (termed IZs) that represent a transition state between prohemocyte and terminally differentiated cells, and terminally-differentiated macrophage-like cells plasmatocytes (PLs) and crystal cells (CCs) found in the CZ. The bulked sorted populations are pure and are enriched for genes known to be expressed in these populations. Analysis of the scRNA-seq data identifies 9 clusters. Some of the clusters correspond to known populations like the PSC, IZ and PL. However, some clusters represent distinct subpopulations of MZ cells (MZ1 and MZ2) and CCs (iCCs and mCCs) and previously unknown clusters proPL and X. The pseudotime analysis identifies three "branch points" and seven "states", and t-SNEs show projected relationships between the states and clusters. Numerous graphs in multiple figures provide transcript levels of genes related to metabolism (Figure 3), pnt (Figure 4), numb (Figure 5), msi (Figure 6 ). The supplements for Figures 2 and 3 provide transcript levels for MZ markers, cluster X markers, IZ markers, CC markers, PL markers and basement membrane genes. Validation of the scRNA-seq are provided for JNK pathway (Figure 3), pnt (Figure 4), numb and sima (Figure 5), msi (Figure 6). The authors extend the transcriptomics through two "case studies". In the first one, the ETS transcription factor Pnt is required for the progression from late MZ to IZ. They also show that Pnt has a later function in PLs in preventing them from becoming CCs. In the second case study, their transcriptomics reveals a specific isoform of sima expressed in mature CCs (i.e., mCCs) that co-localizes with Notch, supporting the Banerjee lab's earlier work. The transcriptomics also reveals that numb transcripts (encoding a Notch inhibitor) are expressed in iCC but the Numb protein is highest in mCC. They author resolve this paradox by showing that the numb translational inhibitor Musashi is expressed robustly in iCCs. The authors also supply analyses comparing their scRNA-seq with one published in 2020. These transcriptomic analyses and subsequent genetic experiences provide strong support for the major claims of the paper.

There is a massive amount of data in this study. The data are of high quality, and the manuscript is well written. The results support the main conclusions. This study will be a very valuable resource to the community. I have a few suggestions for possible improvement.

1. On p. 36 (line 906), the authors write that "we surmise that Notch activation is the default pathway for early Hml-expressing cells to become CCs, and that the activation of Pnt acts antagonistically to prevent this process thus favoring instead, the plasmatocyte fate." I don't understand the logic of this. PLs represent 95% of the mature hemocytes, whereas CC represent 5%. Why would most of the differentiating hemocytes have to repress Notch signaling by expressing Pnt. Loss of Pnt from Hml+ cells would very consequential as the animal would not have PLs from the LG. What I am trying to say is that the kind of regulation proposed here is not robust and could be easily disrupted by mutation. Could the authors comment on this.

2. The manuscript is very long (the results section is thirty-five long) and reader attention spans tend to be short. Could the authors please edit the manuscript to reduce its length. For example, I don't think that the entire section about cluster X is needed. The metabolism section could be condensed. Some of the discussion is redundant with the results.

3. Please provide accession numbers the raw data at NCBI and a link to the reviewers.

Reviewer #2:

In this manuscript, Girard et al. analysed the transcriptome of the lymph gland of Drosophila using high throughput sequencing. They fist used genetic markers (Domemeso-GFP and Hml-RFP) to sort the cells from three distinct regions in feeding larvae: the medullary zone (MZ) known to be populated by progenitors, the intermediate zone (IZ) populated by intermediate precursors and the cortical zone (CZ) containing the mature hemocytes. The cells from the CZ were further subdivided into plasmatocytes, immature crystal cells and mature crystal cells with the genetic markers Hml-RFP and Lz-GFP. This subdivision was carried out at later stage to maximise the number of mature hemocytes. A comprehensive molecular signature of each region and cell type was determined with bulk RNAseq. Then, the authors analysed the transcriptome of 21200 cells of the lymph gland using 10x genomics technology. They found 9 clusters of cells displaying distinctive signatures and metabolic properties, including the cells of the Posterior Signaling center (PSC), two types of progenitors in the MZ, the intermediate precursors, the plasmatocytes as well as the immature and mature crystal cells. They predicted the filiation between the clusters using Monocle, indicating a developmental trajectory starting in MZ producing IZ and then plasmatocytes. At last, the authors validated two mechanisms of cell differentiation highlighted by the transcriptome analysis. They showed the context-specific role of the transcription factor Pnt in the differentiation of plasmatocytes. Loss of Pnt in the early progenitors has no effect whereas its loss in the late progenitors prevents the differentiation of intermediate precursors and thus mature plasmatocytes without affecting the differentiation of crystal cells. As a second study case, they showed that the interplay between Notch, Numb, Sima and Musashi is involved in the maturation of crystal cells.

Overall, this manuscript presents a tremendous amount of RNAseq and in vivo data with highly detailed interpretations. It provides very valuable and substantiated information on the molecular mechanisms involved in the development of the hemocyte lineages in the Drosophila lymph gland. The main caveats are (1) the definition of two clusters IZ and proPL, which seem to belong both to the IZ, (2) the fact that most boxplots do not include 0 in the y-axis, which strongly biases the interpretation of the graphs, (3) the definition of mitotic precursors. Finally, shortening would have made the manuscript more easily readable and would have conveyed the message more directly.

1) Most charts presenting expression levels or AUC score across clusters do not include 0 on the y-axis and disclose highly heterogeneous ranges. For example, the ranges of the AUC displayed in Figure 3 are from 37 points in A (y-axis range 0.43 to 0.8) to 3 points in I (y-axis range 0.13 to 0.16). This is highly misleading, and biases the interpretation of the data since the authors describe minor differences the same way than large differences. Few examples are:

– In the legend of Figure 3B-C, the authors write "(B) TCA cycle enzymes are expressed at exceptionally low levels in the PSC compared with the cells of other clusters. (C) Expression of oxidative phosphorylation pathway enzymes is low in the PSC, high in MZ1 and MZ2 and moderate in IZ, proPL, and PL clusters.". In B, exceptionally low level correspond to 0.42 compared to 0.46 in the other clusters. In C, low in the PSC means 0.74 and high in the MZ corresponds to 0.78. Since AUC represent frequencies, I doubt that few point can translate into such high ranges.

– In figure 3D and E, the authors mention the levels of Zw and Idh in the clusters. They explain that both are highly enriched in PSC compared to MZ. Zw presents an expression level of 1.1 in PSC, around 1.2 fold higher than in MZ and Idh presents an expression level of ~ 7 in PSC around 2 fold higher than in MZ. The difference in level of expression and fold enrichment cannot be appreciated properly due to the heterogeneous y-axes. In addition, the authors described the two enzymes in the same terms while Idh is expressed 7 time higher than Zw.

– For Pnt (Figure 4AB), the authors describe "a very low level of Pnt" in the PSC and MZ and a significant increase in the MZ2-3. The level in PSC is around 5.2, which is much higher than most genes described in this study and the significant increase is going from 5.2 in MZ2-2 to 5.5 in the MZ2-3. The significance of this increase need to be documented with a p-value and the biological relevance of this difference seem far-fetched.

2) A better explanation should be provided for the AUC scores. The authors rightly say that AUC are reflective of co-regulation however the keys to interpret the score are not described. In addition, while a difference from 0.80 to 0.60 (Figure 3A) seems plausible and sufficient to call for an enrichment of glycolytic genes in the PSC, the biological relevance of differences from 0.74 to 0.78 (Figure 3C) or from 0.08 to 0.09 (Figure 2—figure supplement 5) seems far-fetched without further explanations/justifications.

3) The distinction between the cluster IZ and proPL needs to be clarified. The enrichments of the IZ AUC and individual IZ markers are not striking (Figure 2—figure supplement 3A-H). In addition, can the authors explain why only 6 of the 9 IZ specific genes were taken to estimate the AUC score? The strong similarities between the two clusters, in terms of markers and developmental trajectories, seem to indicate that the two clusters represent transient conditions that each cell goes through on its way towards full differentiation. Indeed, the single cell analysis has been performed in feeding larvae, when cells are actively differentiating, not in a steady state condition. Longitudinal/spatial analyses in the developing lymph gland might help in the interpretation, but this is not the scope of the present manuscript.

4) The authors assess the impact of Pnt in the MZ cells using the drivers domemeso-Gal4 and Tep4-Gal4. The authors showed that domemeso>pntRNAi prevent the progression of MZ cells toward IZ cells. Some quantification would be welcome to appreciate the penetrance of the phenotype. In addition, the authors say that Tep4>pntRNAi has no observable phenotype, while the comparison between Figure 4E and Figure 4F seem to indicate that the lobe is smaller and with less Tep4 positive cells. Such difference could arise from slight stage differences. Could the authors indicate how they staged the animals, the number of samples...? At last, the potency of the pntRNAi construct should be documented.

5) In the section "Numb and Musashi in CC determination", the authors mention that Notch-ACT raises Numb levels and Notch-RNAi decreases Numb levels in the crystal cell. This interpretation should be clarified. Since N activity is modulated using a CC specific driver and the number of lz>GFP also changes upon N modulation, the observed results may arise from regulation of Numb expression and/or from regulation of CC number. CC quantification will help sustaining their statement on the role of N. In the third paragraph linked to Figure 5—figure supplement 3H-N and Figure 5O-R', the authors describe a clear reduction of Sima puncta, PPO2 expression and number of mCC. P-values should document these observations. Also, does the expression of the type II targets decrease upon Numb RNAi? At last, Figure 6H-M, the authors indicate that msi-RNAi enhance the level of Numb in crystal cells without providing information on the procedure followed to measure Numb intensity. What does Numb intensity represent in Figures 6J and 6M? Is it the average level per cell or the level in the whole lobe?

6) The authors carried out the single cell sequencing in triplicate. It would strengthen considerably the data to provide a comparison between the replicates.

7) The paper would gain from shortening. The introduction is broad and exhaustive, the results section describes the different the clusters and states as well as two study cases, the discussion elaborates on the mode of differentiation and put forward interesting models such as the gradual rather than stepwise transitions between groups of cells. Since this is a resource paper, the validation of all the single cell data is out of the scope, hence a thorough discussion of all those data could be shorten and used in subsequent studies. Furthermore, many data are already discussed in the results section, diluting the important and novel messages that the paper conveys.

8) According to the authors, Cluster X represents mitotic states of several distinct cell types, including the CZ that carries differentiated cells. This intriguing finding indicating the presence of dividing cells throughout the lymph gland deserves some clarifications. Does it imply that none of the other clusters identified by the RNAseq analysis contains cells in mitosis? Does it mean that plasmatocytes and cells of the medullary zones have similar mitotic potential? Is there any difference in the type/levels of genes associated to cell division between the cells of the cluster that express MZ markers vs. those that express the Pl markers? I understand that the spatial analysis of the cluster X cells in the lymph gland, which would help clarifying these issues, goes beyond the scope of the manuscript. It would be nevertheless useful to compare the RNAseq data with those from the laboratory of Jiwon Shim, who also identified the clusters of mitotic cells in the lymph gland. Also, a dot plot representation of the genes associated with cell division in the different cells of the cluster X (MZ, Tr, Pl) might help identifying features specific to the different subclusters.

Reviewer #3:

Using a combination of bulk RNA-Seq of FACS-sorted cells and single cell RNA-seq, the authors identify various blood cell subpopulations that compose the Drosophila hematopoietic organ called the lymph gland. This study has been performed at one developmental time point, mid third instar larvae. The authors perform a pseudo time analysis and propose a developmental trajectory with multiple paths to mature blood cells types. RNAseq data suggest that different blood cell types express genes involved in various metabolisc processes. They establish that Pointed has different roles during lymph gland hematopoiesis. Finally, they identify that Numb and Musahi are involved in a Sima dependent Notch non canonical pathway in mature crystal cells.

This analysis is of interest, however in the current version, it is too preliminary.

1. The list of the main genes defining each sub-population inside the different clusters, as well as their expression in all the other sub clusters, has to be provided in the main figures.

2. No validation of RNA seq data is provided: A spatial reconstruction in vivo by profiling the expression of a subset of genes identified by RNA seq is necessary.

3. To support the developmental progression of lymph gland cells proposed in Figure 7,

lineage tracing experiments are required.

4. Comparison between RNA seq data obtained by (Cho et al 2020) has to be given in the main text. Furthermore, discrepancies between these 2 studies have to be clarified. How the AUC list has been established? This is a key point. For example, the PH1 cluster identified by Cho et al is spread out in MZ1, PSC, X and MZ2 cluster in this study. Why are the results so different? Delta is a marker of PH1, which is validated by analyzing its in vivo expression profile. What about delta expression in the scRNA seq performed here?

5. There is a discrepancy between the introduction and the main results of this paper. In the introduction the authors focus our attention on the IZ, but in fine we don't learn much about IZ cells from this analysis. Instead of deciphering IZ identity and fate by in vivo profiling, most functional analyses performed concern crystal cell maturation. This part is developed via 2 main figures among 7, plus 5 sup figures. From my point of view, this study represents an ideal opportunity to better characterise IZ cell identity, lineage and function. Unfortunately these data are missing in the current version of the manuscript but could be added instead of the data concerning crystal cell maturation, which is somewhat out of the scope of this manuscript and could be published in a separate paper.

6. This manuscript has to be focused on the novelty given by the RNAseq data. The data concerning crystal cell maturation, which is somewhat out of the scope of this manuscript, could be published in a separate paper.

7. There are 7 main figures and 16 sup figures + 1 additional file. All these Sup figures give information and make suggestions that unfortunately are not validated by additional experiments. Overall the reader is left with a lot of observations that are not further validated and in fine one cannot rely on. Data presented in this manuscript have to be focused to avoid overloading the reader with too many side observations, which in turn lead to losing the thread of the message of this study.

8. I have concerns about the single cell RNA seq data, since essential information is missing.

– What about the cell numbers in each cluster? The IZ cluster (Dome-GFP+ and Hml+) represents a small subset of lymph gland cells based on the CHIZ expression profile (see Figure 3K); however, it corresponds surprisingly to a quite large lymph gland cell subset, as illustrated in Figure 1J. How can one explain this?

– To identify subpopulations in clusters, the authors performed sub clustering on isolated clusters for PL and CC. Why was this not done in the same way for the other 3 main clusters (MZ2, IZ and proPL)?

– For the IZ sub-cluster: The plot in Figure 2 sup 3I is very misleading, since it suggests that genes expressed in the IZ are specific to this cluster. For example, "state 3" is present both in the MZ and proPL (Figure 2), but in Figure 2 sup 3l it is only represented in the IZ and not in the MZ and proPL clusters. The same remark holds for states 4, 5 and 7. Furthermore, as I mentioned above, the list of the main genes defining each sub-population inside clusters, as well as their expression in the other sub-clusters, has to be provided in the main figures. Furthermore, a spatial reconstruction in vivo by profiling the expression of a subset of genes identified in sub populations is mandatory to validate the RNAseq data.

– Why is the plot shown in Figure 1J different from the plot shown in Figure 2 sup 5 I? The t-SNE graphic representation does not give any indications concerning whether clusters are related or not.

– Why are there discrepancies between gene expression levels and their representation on the corresponding plot? Please see for example the case of CG30090 in Figure 2 sup 3B and the corresponding plot in C. CG30090 is expressed at a similar level in proPL and PL, but its expression in proPL is lacking in the plot. Why ?

– Concerning IZ markers, among the 6 identified by bulk RNA seq, only 4 of them have been analysed in single cell experiments. What about the 2 others?

– In Figure 7, the model of developmental progression of blood cells proposes that there is no transition path between IZ and proPL. This proposition does not fit with the data. Indeed, in the pseudo time analysis there is a clear overlap between IZ and proPL, indicating that they are connected (see states 4 and 5 in Figure 2 O-P). Genes highly expressed in IZ are also highly expressed in proPL. This is observed for all the IZ markers analysed in this manuscript (please see Figure 2 sup 3B, D, G, H). Determining whether there is a transition path between IZ and proPL has to be validated by in vivo experiments.

– Figure 7: Regarding the translational link between PL7 and iCC7 (Figure 2 sup4), again this proposition has to be validated in vivo. Furthermore, how can iCC7 (more engaged in maturation) give rise to iCC6 (less engaged in differentiation). This also needs to be validated.

– Concerning the MZ1 cluster, Ubx is expressed in these cells. Ubx is specifically expressed in lymph gland posterior lobes that are composed of hematopoietic progenitors expressing markers of MZ cells (Rodrigues et al., 2021). Altogether these data strongly suggest that MZ1 cells correspond to posterior lobe hemocytes. This has to be clarified.

– For cluster X, since DNA damage markers are expressed, this strongly suggests that this cluster might correspond to unhealthy cells damaged during the experiment. What about their ribosomal content (a criteria commonly used to check for cell health)? Is the molecular signature of cluster X found in bulk RNA seq and in the Cho et al., 2020 paper?

– What is the unit given for the Y axis in Figure 3? Why is the scale different from one graph to another and does not start always at zero? For all graphs in this manuscript the p value is missing, so the reader cannot not figure out whether the differences are statistically significant or not. Concerning the AUC analysis, how is the list of genes taken into account for a signalling pathway or a function that has been established? What kind of conclusion can be drawn from analyses regarding metabolism? In other words, considering the PSC as an example of a group of cells where glycolysis genes are highly expressed, what is the impact of this on PSC function, and how does potential glycolysis in the PSC help us to understand PSC function?

– Figure 3K: the authors need to define what CHIZ is. Since there is no staining overlap between MMP1 and CHIZ-GFP, the authors cannot conclude that MMP1 is expressed in the IZ. Furthermore, MMP1 transcripts are detected at high levels not only in the IZ but also in the MZ2, proPL and PL (Figure 3J). How can these results be reconciled with the expression profile of MMP1 shown in Figure 3K?

–Figure 4: Quantifications are missing. Crystal cell and MZ indexes have to be given.

– Figure 4G and H: That tep4 is expressed in a subset of MZ progenitors defined by dome>GFP is not new, this has been established previously. Please see Benmimoun et al. 2015, and Oyallon et al 2016.

– What about the Pnt expression profile in the LG? Figure 4C-D: DomeMESO>pnt RNAi , in addition to a defect in blood cell differentiation, this leads to a smaller LG compared to the control. This defect in size has to be mentioned and quantified. Since the role of pnt in the MZ has been previously reported by Dragojlovic-Munther M et al , 2013, this paper has to be cited. Furthermore, the Dragojlovic-Munther M et al. study indicates that in addition to preventing hemocyte differentiation, pnt RNAi in the MZ leads to lamellocyte differentiation. Do lamellocytes differentiate when pnt is knocked down using domemeso, tep4 , CHIZ and hml gal4 drivers? In Figure 4F :Tep4>GFP>pntRNAi , GFP levels are decreased compared to the control. Does Pnt control the expression of the Tep4-gal4 driver? In the text, p35 line 886 "Pnt loss in MZ2.3" is an over interpretation, since no gal4 driver specific for this group of cells has been used to perform the lof experiment. p35 lines 903 "plasmatocytes to be converted into crystal cells" is erroneous, since hml-Gal4 expression is not restricted to mature plasmatocytes but is expressed both in plasmatocyte and crystal cell precursors. p35, lines 905-910 should be in the discussion, not in the result 'section.

– Figure 5: Numb and crystal cells

The paper Cho et al 2020 has to be mentioned in the text, since it established previously by immunostaining that Numb is expressed in crystal cells.

– A previous study done in Banerjee's lab, reports on the role of Sima and Notch in crystal cell survival by preventing their dissociation (Mukherjee et al., 2011). In the present manuscript, no data and comments refer to crystal cell survival depending on Numb. Thus in the current version of the manuscript, it remains unclear as to what is the role of Numb in crystal cells. Does it control iCC to mCC, or is it required for survival of mature crystal cells? The confusion is sustained by sentences such as: "depletion of Numb prevents the maturation of iCC to the mCC state", please see p 39, lines 1000. Since Numb is detected at high levels in mCC and not in iCC, the function of Numb should be in mCC once they have matured. Furthermore, it has been previously published that Sima is required for crystal cell survival. A decrease in Sima levels is observed in Lz>numbRNAi conditions, supporting the proposition that CC depleted from Numb should disrupt since they lack Sima . In conclusion, the role of Numb in either crystal cell maturation (i. e., going from iCC to mcCC) or mCC survival has to be clarified.

– Figure 5 sup2 : Quantification is missing. p 38 lines 979-981. The authors need to clarify whether there are talking about an increase in Numb levels per crystal cell, or an increase in Numb levels per LG, which in this case reflects an increase in the number of cell expressing Numb.

– Numb subcellular localisation is different from one picture to another. In Figure 5M, Figure 5 sup2 , Figure 6A-c and 6 H-L', Numb is mainly localised at the periphery of the cell at the plasma membrane, whereas in Figure 5 sup 3A-B and sup 3F-G, Numb is detected as cytoplasmic punctate dots without staining at the plasma membrane. This is confusing and clarification is necessary.

– Figure 5 sup 3: PPO2 staining shown in Figure 5 sup 3 K-L is not in agreement with the quantification given in M. p values are missing in M and N. There are also discrepancies between these figures and the text p 39: "numb RNAi expressed in crystal cells causes ...with a concomitant increase in the iCC population". Figure 5 sup 3N: Quantification of crystal cell numbers is not convincing. Since there is a lot of variation among LGs, quantification of PPO+ cells has to be given as an index (i.e., a ratio between the total number of PPO+ cells/ per total number of LG cells). In N, 6 LGs maximum per genotype have been analysed, which is far too few. Defining whether the number of crystal cells is affected in lz>numbRNAi is essential to determine whether Numb is required to allow iCC to mature into mCC, or whether it controls mCC disruption. The MM section has to be completed; it should indicate how quantifications of cell numbers and fluorescent intensity were performed.

– For Hnt staining in lz>numbRNAi, there is a discrepancy between Figure 5 sup 3 l-l" and Figure 5 sup 3 L-L". In I-I" no difference in Hnt levels compared to control (H-H) is observed, whereas in L-L" a strong decrease is observed (K-K").

– The enlargements shown in Figure 5O-R have been taken from pictures shown in Figure 5 sup 3K-L. It would be better to show independent immunostainings. This remark is even more relevant in this case because the staining in Figure 5 sup 3 L is not convincing.

– Figure 5 sup 3 H-I: lz >numb RNAi there is a decrease in Sima staining. Is it due to a decrease in sima transcription and/or Sima protein stability and/or Sima subcellular localisation?

– Figure 6 J and M ; is "the Numb intensity" referring to the intensity of Numb per cell or the total amount of Numb intensity measured per LG? This has to be clarified in the figure, in the text (p 40) and mentioned in the MM. What about the crystal cell index in lz>msi RNAi and Hml>msRNAi?

– A schematic representation of crystal cell maturation involving N (both the canonical and non-canonical signalling), Numb and Sima would be very helpful.

– In MM p 74 lines 1888 "data was corrected for batch effects between samples". The information concerning the method used has to be provided.

9. Modifications in the text are required

– Lines 1093 "the equilibrium signal from proPl". Functional data supporting this conclusion are lacking.

– Lines 1088 "JNK signalling ... is a specific property if IZ cells". Neither JNK expression nor its function has been analysed in this study.

Reviewer comments after revision

Decision letter 2

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Paths and Pathways that Generate Cell-Type Heterogeneity and Developmental Progression in Hematopoiesis" for further consideration by eLife. Your revised article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Anna Akhmanova as the Senior Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Essential revisions:

1. The authors should temper some conclusions because the conversion of AUC scores to z-scores can obscure the actual level of enrichment. Specifically, the authors should:

a. Soften the conclusion that proPL generates the equilibrium signal and that the IZ alone activates the JNK pathway as this is based on a low number of genes (lines 959-960). Please rephrase this statement.

b. Point out in the text that JNK activation is enriched in but not specific to the IZ.

c. Clarify the in vivo definition of the IZ and the ProPL cells with respect to the Hml delta QF driver. The authors use it to specifically label the IZ but the driver's expression domain is broader than IZ cells.

2. The authors should indicate in Figure 3—figure supplement 3, 1D which AUC terms encompass "glycerolipid remodelling genes" (line 592)

3. The authors should rephrase "pnt transcript is expressed at low levels in the PSC (Figure 4A)". (Line 664). One interpretation of Figure 4A is that pnt is expressed at the same levels across the different clusters but in a smaller number of cells in the PSC (hence the smaller circle).

4. The authors should provide publications for the enhancers in Figure 5—figure supplement 1 B,C,G or explain how they defined the enhancers.

5. The authors should remove the comma in line 795 ("we find, is").

6. The authors should avoid the term de-enriched/de-enrichment (lines 525, 549, 562, 836, 135, 1136, 1159, 1435, 1437, 1438) to indicate a change in the levels of expression.

7. The authors should modify their conclusion (line 652) "establishing the IPs as MMP1 producing cells". The diffused MMP1 staining in Figure 3D-D' is not convincing.

8. The authors should address how they conclude (line 696) that "Pnt is required for exit from the IZ" since there is no defect in CC differentiation in CHIZ >pnt RNAi (Figure 4l-M). They should also comment on Pnt's role in plasmatocyte differentiation.

9. The authors should modify the introduction so that it includes a statement about the cardiac tube acting as a niche to control lymph gland hematopoiesis and supporting references.

10. The authors should add a sentence/short paragraph in the discussion saying that the proposed model/definition of states awaits functional confirmation, at least in some cases.

11. In the dot plots, the authors should indicate what is meant by 'mean' and 'non-zero percent'.

12. In Figure 2H,I, the authors should show the whole lobe and indicate the IZ and the proPL with arrowheads.

Suggested revisions:

1. It is suggested but not required that the authors provide a volcano plot to illustrate the differences between proPL and IZ.

2. It is suggested but not required that the authors provide the single table that must have been generated to produce the figures of the first submission and used to calculate the z-scores.

Detailed Reviews

Reviewer #1/Reviewing Editor:

I have read the response to authors and the revised manuscript. The authors have addressed all of the essential revisions and all of the reviewers' comments satisfactorily. They have overhauled the manuscript, making extensive changes to the figures and the text, thereby improving their study and its conclusions. The manuscript is now easy to read, follow the logic and the data support the conclusions in the text. I recommend its publication in eLife.

Reviewer #2:

The revised manuscript from Utpal Banerjee and collaborators involves substantial editing of the text, additional experiments and significant changes in the presentation of the data. The RNAseq data provide a useful resource to the community and the validations already help understanding the mechanisms controlling lymph gland development. Altogether, the revision allows a much smoother reading and answers many questions asked by the reviewers. I have few comments that do not call for additional experiments but need to be addressed.

The authors converted the AUC-scores in normalised z-scores to enhance the contrast on the heatmaps. This representation does indeed ease the interpretation of the AUC score but hides completely their actual levels of enrichment, which leads to strong conclusions based on minor differences. Here below indicative examples.

In the discussion (line 959-960), the authors state "proPL (but not IZ) generates the equilibrium signal, whereas the IZ alone activates the JNK pathway". While this statement could be deduced from the heatmaps (Figure 2—figure supplement 2A,B for the AUC Equilibrium signal and Figure3B and Figure 3—figure supplement 2B for the JNK pathway), it is far from being conclusive (compared to the initial representation of the 1st submission, old Figure 2—figure supplement 5 for the AUC Equilibrium signal and old Figure 3I,J for the JNK pathway).

In the previous representation, Mmp1 expression levels and AP-1 targets are enriched in IZ but overlap between the IZ and the proPL, suggesting that JNK activation is enriched but not specific to IZ.

Concerning the equilibrium signal, Figure 2—figure supplement 2B indicates a strong enrichment in the proPL but the IZ also present a mild enrichment. In addition, the AUC equilibrium signal displays low variability across the different clusters (old Figure 2—figure supplement 5: highest ~0.475 for pPL-4 and lowest 0.445 for PL-7). The AUC score represents the number of genes associated with the term. Thus, the score of AUC comprising low gene number should provide stronger contrast than the AUC with high gene number since the genes are less likely to be among the top 25% of genes (threshold set up by the authors). The AUC Equilibrium signal comprise 6 genes with a single one (Pvr) enriched in proPL. With such low gene number, the scores 0.475 and 0.445 both represent less than 3 genes and no striking differences across the two clusters. Therefore, it seems overstating to say that "proPL (but not IZ) generates the equilibrium signal".

To avoid any mis-interpretation and provide the reader with all the data to interpret the heatmap, I would recommend the authors to join the matrix of the AUC scores used in the manuscript across all clusters. I would also strongly recommend to rephrase the sentence line 959-960.

A clarification is appreciated on the in vivo definition of the IZ and the ProPL cells. The authors use the Hml delta QF line and CHIZ Gal4, a split Ga4 line relying on the domemeso and Hml delta enhancers that allows the identification of the IZ cells (page 16-18). The Hml delta Ga4 driver is expressed in the cortical zone and in the intermediate zone (Spratford 2020). The Hml delta QF is derived from this line and has an identical profile of expression (line 428). Yet, with no further explanation, this very line is used to label ProPL cells and distinguish them from the IZ, in combination with CHIZ-Gal4 (Figure 2H,I).

Altogether, the use of AUC and cell states adds a new dimension to the single cell analysis and can identify transient populations that appear during development, however, the manuscript largely over-emphasizes this concept and subdivides the developing lymph gland into numerous cell subpopulations in some cases without strong evidence. Beyond the fact that the analysis concerns a single time point, does not provide spatial resolution and does not sufficiently validate the described states (three issues that are anyway beyond the scope of the manuscript), an unweighted analysis can lead to over interpretations. After all, AUC are relative definitions, as detailed in the rebuttal letter. To distinguish cell groups through AUC, qualitative and quantitative information should to be somehow taken into account: the number of cells, the number of genes in each AUC, that of the members of the AUC showing differential expression, the absolute levels of gene expression, the levels of differential expression, as well as the relative 'significance' of genes in the AUC. Typically, transcription factors that control the expression of many genes or key enzymes in a biochemical pathway may have a different weight compared to other genes. Some of this information is not available in the figures, some is present in supplemental materials/can be extrapolated from other figures (whereas each figure should be self-explanatory). The lack of granularity necessary to firmly define a cell group (state, cluster...) by no mean affects the quality of the manuscript as the validation of all the cell groups in the lymph gland can await further studies. The authors should nevertheless be more cautious in the interpretations and avoid strong statements. This will overall strengthen and further simplify the message provided by the manuscript.

Reviewer #3:

The revised version of the manuscript answers my main requests. The extensive editorial changes in the text and modification of figures make the manuscript much easier to read and allow one to understand the novelty of this study.

I still have two concerns:

1. Figure 3D-D': That MMP1 staining corresponds to diffused MMP1 is not convincing. If IZ cells synthetized MMP1, why is there no MMP1 staining in these cells? Furthermore, MMP1 is expressed in plasmatocytes; thus in Figure 3E-F'(Chiz>mihep and CHIZ>hepACT) what about plamatocyte differentiation in these two conditions? The modification in MMP1 expression in these 2 genetic contexts might reflect a change in plasmatocyte differentiation and thus might explain the difference in MMP1 expression. In conclusion, data supporting that MMP1 is produced by IZ cells are missing, and the sentence on line 652 "establish that IP as MMP1 producing cells" has to be modified.

2. Line 696 :"Pnt is required for exit from the IZ " How do the authors arrive at such a conclusion since CHIZ >pnt RNAi (Figure 4l-M) shows no defect in crystal cell differentiation? What about plasmatocyte differentiation?

Additional corrections:

1. The introduction should be updated, including that the cardiac tube acts as a niche to control lymph gland hematopoiesis. This has to be added.

2. Figure 2 Sup 3 : Zscore is -3 to +3. Is it OK?

Decision letter 3; after second revision:

Dear Dr Banerjee,

Congratulations, we are pleased to inform you that your article, "Paths and Pathways that Generate Cell-Type Heterogeneity and Developmental Progression in Hematopoiesis", has been accepted for publication in eLife.

Editor's evaluation:

This paper will be of interest to scientists who study hematopoiesis. The authors combine single cell RNA-seq with bulk RNA-seq of transcripts from blood cells in the Drosophila larval hematopoietic organ. They present extensive analysis of the datasets, and the pseudotime analyses present a model of how hematopoietic progenitors can differentiate along transitory paths. These datasets reveal cell-type specific isoform expression of Notch pathway regulators, and genetic experiments prove the importance of these factors in development of one lineage. These transcriptomic analyses and subsequent genetic experiences provide strong support for the major claims of the paper.

Please take note of the points below and we hope you will continue to support eLife.

Best wishes,

Erika Bach

Reviewing Editor

Anna Akhmanova

Senior Editor
