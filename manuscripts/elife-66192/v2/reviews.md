# Peer review - Round 1

Editors:
- Bruno Lemaître, École Polytechnique Fédérale de Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66192.sa1](https://doi.org/10.7554/eLife.66192.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this manuscript, Kwon et al., describe a single cell sequencing analysis of hemocytes of the malaria mosquito Anopheles gambiae. Their data support the old classification of hemocytes in the three main categories previously defined according to the morphology and phenotype of these cells, but they further reveal subpopulations in the granulocyte and oenocytoid groups. The authors also provide several new markers to define these different populations and subpopulations.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Single-cell analysis of mosquito hemocytes identifies signatures of immune cell sub-types and cell differentiation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered at this stage for publication in eLife. Nevertheless, the reviewers agree that they could consider a revised version of the manuscript that addresses all their points. So you have the opportunity to submit a revised version of this paper to eLife but this revised version will be considered as a new submission (but likely handle by the same reviewers). The editor and reviewers find many merits to your article but one first point is to know what it specifically brings compared to other RNA seq done with hemocytes of mosquitoes. A second point is that your study is rather descriptive. This not a problem by itself if you can provide a solid dataset that can serves of reference for the whole community (see criticisms of reviewer 2 on this point).

Essential revisions:

Reviewer #1:

Mosquito hemocyte biology and function remains poorly understood. However these cells have critical functions for example in immunity and there is a knowledge gap that needs filled. Several subtypes -three in total have been defined in the past but this study goes deeper into the functional characteriusa characterisation based on phagocytic properties, FISH and importantly single cell RNA sequencing. Moreover the importance of Lozenge in differentiation of oenocytoid hemocytes is shown. This is an elegant study relevant to the field. It will certainly impact studies on hemocytes on other mosquitoes and beyond. The introduction is clear and explains the necessity if this study. Methods are described well enough to follow what was done. Data can be accessed in a single cell analysis pipeline which is very useful to end users. I also like that blood fed and non blood fed mosquitoes were used, broadening impact and interest. Overall the manuscript does an excellent job of illustrating expression patters and differences between cells, including lineage analysis and conclude that 7 different types of immune cells, including 4 types of granulocytes. The definition of markers will make it easy for others interested in this topic to translate these findings into different questions, and signficantly expands our understanding of hemocytes in an important disease vector.

The following should be clarified or expanded on:

1) Are the three cell types 1 figure 1A meant to represent the three subtypes or these just three distinct gated populations as separated by FACS- I appreciate that the authors state that the subgroups/clusters realate to these populations but is there a selection into the three main known types? What are the cell types that were not split into these three groups- is there any indication of their identity?

2) Could the authors add information on lozange functions and how it may promoter oenocytoid differentiation? Even expanding on this in the Discussion would be useful for the reader who is not familiar with the topic.

3) Could the sequences of probes for RNA fish be indicated?

4) Line 554: could the authors expand on the question of "suitability" of methods used? This might save others in the field time when analysing similar data.

5) Line 531: "." instead of ".." after Sweden.

6) Line 922: An. Gambiae

7) Immune gene activation is seen in a subset of cells, could the authors speculate on where these may be part of an ongoing immune response to infection; and whether they would expect these genes to be expressed in mosquitoes kept in presence of antibiotics?

Reviewer #2:

Kwon et al. analyse the immune cell diversity of the adult mosquito Anopheles gambiae using single cell sequencing. They bled naïve and blood-fed adult females and sorted the hemocytes using WGA and DRAQ5 as hemocyte markers. Cells were selected from three independent gates defined by the intensity of DRAQ5, and sequenced using SMART-seq2 methodology. 262 cells were sequenced and included in the downstream analysis. The authors found 8 clusters of hemocytes using hierarchical clustering. Cluster 3 seems specific to naïve hemocytes, whereas all other clusters are found in both naïve and blood fed conditions. They dismissed the cluster 1 based on high gene expression, which may be indicative of FACS doublet. Next, the authors described the markers common to all hemocytes and the ones distinguishing the clusters. They identify clusters 2, 3 and 4 as granulocytes, 7 and 8 as oenocytoids and 5 as prohemocyte. Then, they use Monocle 3 to predict the filiation between the clusters based on a limited number of cluster markers.

This work represents a c database of hemocyte subtypes in mosquitoes and has the potential to highlight strong markers for each subpopulation. However, the experimental design is not explained properly and the authors mostly described their data without deep interpretation. Moreover, the definition of each subtype is not convincing. For these reasons, I believe that the work does not warrant publication in eLife in principle.

1) The number of sequenced cells seems rather low, which may bias the overall interpretation of the data.

2) The authors should provide the rational to look at naïve versus blood fed hemocytes. In addition, merging the two sets of data may again bias their interpretation. Typically, cluster 3 is only present in naïve hemocytes and cluster 2 is overrepresented in blood-fed hemocytes.

3) The biological meaning of the gating strategy for the FACS is not interpreted nor justified. What is the meaning of Clusters 3, 4 and 6 being excluded from gate 1?

4) What is DRAQ5? There is no description nor reference to the use of DRAQ5 to label hemocytes.

5) The justification for removing Cluster 1 from the analysis is not convincing: "we dismissed this cell cluster from further analysis as likely cell doublets of mixed cell origins as the result of FACS cell isolation or as dividing cells". If these cells were indeed doublets of mixed cells, they should not cluster together and if they were dividing cells, markers of division should be present. The authors should provide more evidence to remove cluster 1 or include it in the downstream analysis. As a matter of fact, the transcriptional profile suggests that these cells may represent pluripotent precursors for granulocytes and oenocytoid cells.

6) Cluster 5 is defined as prohemocyte based on the absence of Cyclin G2. Most hemocyte markers are also absent from this cluster (Figure 2C,D). What are the evidence that this cluster is indeed populated by hemocytes? Did the authors search for mitotic markers?

7) Most markers presented across the different figures are expressed in several clusters. The author should provide a figure or table displaying the markers expressed in a single cluster. Such table can be generated using the Seurat toolkit with the FindAllMarkers program (https://satijalab.org/seurat/). Figure 2A shows the level of expression of different genes and the percentage of cells expressing them. This is a more correct representation of the sc RNA data compared to that in the following panels (2 C-E), where there is no information as to the number of cells within the cluster expressing a given gene. Based on Figure 2A, the identification of different clusters does not seem to rely on robust criteria. For example, Cluster 2 to 4 seem very similar. Altogether, very few markers are taken into consideration.

8) Lines 190-200: the authors state that "PPO1, PPO3, and PPO8 are enriched in putative oenocytoids, while PPO2, PPO4, PPO5, PPO6, and PPO9 are most abundant in putative granulocyte populations (Figure 2E)", in contrast to previous suggestions that PPOs are expressed in a subset of hemocytes. This sentence is not in agreement with the data, Figure 2E highlights three main clusters expressing distinct pattern of PPOs, suggesting that indeed, distinct subsets of hemocytes express specific PPOs. But again, this panel does not show the percentage of cells expressing the different genes. We only get this information for PPO1, which is by the way only expressed in 25% of the cluster 8 cells.

9) The data shown in several supplementary figures do not seem to add much information, as such.

10) What is the evidence for cluster 4 producing cluster 2 and 3 (which is also specifically present in one condition)?

11) Figure 2A,C and 5A: lozenge ID is changing from 002506 in A to 002825 in C. In addition, the expression profiles are not concordant between the two graphs. In A, we observe a strong expression in clusters 5, 7 and 8, while in C we only see expression in cluster 8. Additionally, the expression of Lz shown in Figure 5A (histogram on log normalized count) suggest more cells strongly expressing Lz in cluster 8 and 4 compared to cluster 5, which is again different from the observation in Figure 2A.

12) Monocle 3 analysis. On which basis was done the selection of the genes for the Monocle 3 analysis (Figure S14)? The Dot plot indicates that most genes are strongly expressed across several clusters. How is it possible to infer filiation based on ubiquitously expressed genes? In addition, the number of genes seems extremely low. Can the analysis be done on the whole expression matrix?

13) Monocle 3 interpretation. In Figure 4B, cluster 7 is split into two cell groups, one joined with the prohemocyte cluster 5 and the other with cluster 8. Thus, the group joined with cluster 5 could constitute the progenitors of cluster 8 independently from cluster 5. What are the evidence of the link between cluster 5 and cluster 7?

Reviewer #3:

In this manuscript, Kwon et al. describe a single cell sequencing analysis of hemocytes of the malaria mosquito Anopheles gambiae. Their data support the old classification of hemocytes in the three main categories previously defined according to the morphology and phenotype of these cells, but they further reveal subpopulations in the granulocyte and oenocyte groups. The authors also provide several new markers to define these different populations and subpopulations. Of note, two additional scRNAseq studies on A. gambiae/coluzzii hemocytes are available: Severo et al., PNAS 2018, and Raddi et al., BioRxiv 2020. Still, while overlapping to some extend (especially Kwon and Raddi), I believe that the three papers reinforce each other, each of them bringing a different perspective.

Compared to Severo 2018, Kwon et al. selected a larger diversity of hemocytes as they did not restrict themselves to PPO6 expressing hemocytes, and thus, they were able to get more diverse transcriptomic clusters covering most hemocyte types. Of note, they sequenced ~10x more cells than Severo et al., however the coverage was much lower with a smaller reads (56 vs 100 bases) and a relatively low cutoff for minimal read number (10 000 reads per cell while Severo et al. had several millions reads per cell). Still, this lower coverage did not affect their cell classification, but likely restricted it to highly expressed genes.

Raddi et al. sequenced an even larger number of cells (~20x more compared to Kwon et al), which allowed them to identify some additional subpopulations, and especially one, the megacytes that was not at all described in Kwon et al. While Raddi et al. focused on hemocyte changes after Plasmodium infection, Kwon et al. characterised the phagocytic properties of their different subpopulations.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Single-cell analysis of mosquito hemocytes identifies signatures of immune cell sub-types and cell differentiation" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Utpal Banerjee as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Angela Giangrande (Reviewer #1); Stéphanie Blandin (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. The reviewers have the feeling that you can addressed the revisions without further experiments. Thus the revisions requested below only address clarity and presentation.

Summary:

In this manuscript, Kwon et al., describe a single cell sequencing analysis of hemocytes of the malaria mosquito Anopheles gambiae. Their data support the old classification of hemocytes in the three main categories previously defined according to the morphology and phenotype of these cells, but they further reveal subpopulations in the granulocyte and oenocytoid groups. The authors also provide several new markers to define these different populations and subpopulations.

Essential revisions:

1) The reasons given for removing cluster 1 from subsequent analyses are not acceptable.

The authors bring the following arguments: (i) "Cluster 1 does not express specific marker and express markers also present in other clusters." From the presented figure, it appears that Cluster 1 expresses at least three specific markers (CDC42, 005742 and 004634 in Figure 2A) that are completely absent from the other clusters. (ii) "Cluster 1 is an outlier in the t-SNE analysis." The distance between dots in the t-SNE analysis depends on the projection that was done and is merely indicative of the distance between the clusters. The hierarchical clustering provided by the authors in Figure 1B is more quantitative in terms of homology between clusters and clearly shows the proximity of Cluster 1 with Clusters 2 to 4. Moreover, the distance between Cluster 1 and 2-4 is shorter than the distance between 7 and 8 that are both oenocytoids. (iii) "Cluster 1 presents a high median of gene number." Figure 1D shows that the number of genes is in the same range than Cluster 8. (iv) Based on the above statements, the authors believe that Cluster 1 represents cell doublets. However, an efficient gating strategy on the FACS should remove doublets. In addition, we would expect at least a higher DRAQ5 signal for doublets (higher DNA content), but Cluster 1 is also found among cells gated with gate 2 and gate 3. At last, if these cells were doublets, their specific markers should be present in other clusters as well (e.g. CDC42, 005742 and 004634). (v) The authors exclude the possibility that these cells are transdifferentiating by the lack of mitotic markers. However, transdifferentiation does not necessarily involve cell division and the two processes are independent in Drosophila for both crystal cells and lamellocytes. (vi) The authors exclude the possibility that these cells represent megacytes based on the expression of two markers. Raddi et al., (2020) provide a list of 102 markers for megacytes. The authors should at least provide the data for all the markers (in the form of a Dotplot for example).

Cluster 1 should be included in all graphical representation of Figure 2 as well as in the lineage analysis of Figure 4. Browsing through the web application of the authors, one can notice notably that Cluster 1 is enriched for LRIM15 and thus could be considered as another cluster of phagocytes?

2) The definition of Cluster 5 as prohemocytes still relies exclusively on the absence of markers (Figure S10).

Raddi et al., (2020) defined two populations of prohemocytes. The authors should at least show the comparison of the markers for cluster and the prohemocytes markers indicated in Raddi et al., report. Also, the presence of Clusters 5 and 7 could reflect the presence of two prohemocyte populations, resembling the situation observed in Drosophila (see the work of L Waltzer). At this, point, the interpretation of the data should be more cautious.

3) Blood-fed vs. naïve conditions.

It would help to analyze the data in either naïve or in blood-fed conditions, rather than merging the data from the two conditions. As shown in Figure S3, the eight clusters are represented in very different manner in the two conditions, from 0% Cluster 3 to almost 50% Cluster 2 in blood-fed animals.

The interpretation of the impact of blood feeding on the hemocytes (cluster 2 and 4) should be described in the result section, possibly with a figure displaying the differentially expressed genes (present in Table S2).

Of note, only Cluster 2 hemocytes are enriched in cell cycle gene: how many genes, in how many cells of the cluster? Can they be preferentially ascribed to a food regimen? Is it possible to compare Cluster 2 to the proliferative cluster observed in Raddi et al.?

4) A resource manuscript should provide useful information to the community. This manuscript would gain from a more systematic comparison with the data already available in the literature. For example, Raddi et al., define PPO 4 and 9 as being characteristic of oenocytoids.

5) Could the authors explain why there are no cells from the blood-fed condition in Gate 4?

6) On DRAQ5 labelling used for the FACS sorting step, in Figure 1A, several levels of DRAQ5 are observed in the dot plots. Other publications mention the use of DRAQ5 to estimate the ploidy of the cells. Is this what we observe on the dotplots in Figure 1A, the first three gates separating cells based their ploidy? Is this known for mosquitoes' hemocytes? How do the authors interpret this, since cluster 8 is exclusively found in gate 1?

7) line 1048: "higher levels".

8) Figure 2E: "Ninjurin" is Ninjirin in the text.

9) Figure S14: Are the data normalised by column or are these expression levels? The unit of the colour gradient should be mentioned (z-score, expression levels?).

10) I would appreciate a somehow more detailed comparison of their hemocyte categories (including cluster 1) with those from Raddi et al., This could be proposed as a supplementary figure for instance. Is there a 1 to 1 correlation between the categories? Also, please indicate discrepancies when relevant, e.g. PPO4 is used as a marker for oenocytoids in Raddi et al. while this gene seems to be expressed in all hemocyte subgroups, and especially in granulocytes, in Kwon et al.

11) The discussion paragraph where the authors compare their work with the two other scRNAseq reports (l519-544) is somehow awkward. While I do understand the need to provide an overview of the three studies, I would rather insist there (1) on the reason why they managed to recover as many clusters as Raddi et al., despite sequencing fewer cells (strategies not compared in the text), (2) on a more precise comparison of the hemocyte clusters from the 3 studies (see previous point), and (3) summarising current knowledge on the functional characterisation of the different hemocyte categories.

12) Changes in cluster populations upon blood feeding (e.g. disappearance of all hemocytes from cluster 3): this could be due to rewiring/changes in gene expression in some specific cells as suggested by the authors. Another explanation could be a change in adherence: if certain cells become sessile after blood feeding, they will not be recovered during mosquito perfusion. Of note, it is unclear why there are no hemocytes identified in gate 4 after blood feeding. As this gating is not selective, one would have expected to recover cells there in both sugar fed and blood fed conditions.

13) Figure S1: the cluster color code is different from that of Figure 1. Please use the same for all figures.
