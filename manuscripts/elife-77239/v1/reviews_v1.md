# Peer review - Round 1

Editors:
- Valerie Horsley, https://ror.org/03v76x132 Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77239.sa0](https://doi.org/10.7554/eLife.77239.sa0)

This manuscript presents an important and useful dataset for understanding cellular and transcriptional dynamics during the estrous cycle in mice. Using single-cell RNA sequencing, the authors' data is compelling, providing new marker genes for different cell types. These data will be useful for understanding ovarian biology and will be of interest to biologists studying other tissues.


---

# Peer review - Round 1

Editors:
- Valerie Horsley, https://ror.org/03v76x132 Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77239.sa1](https://doi.org/10.7554/eLife.77239.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A single cell atlas of the cycling murine ovary" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Marianne Bronner as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The major concerns were regarding some data analysis and a request for further validation of the RNA seq. data.

1. In the Monocle in Figure 5C-D, why are the periovulatory GC that is the visualization look very much like mural GC in a completely different branch than mural GC? I have the impression that either the clusters need to be refined/validated further or the Monocle is not providing meaningful results regarding lineage trajectories. Why would the "periovulatory" GCs be at the end of the CL branch? In addition, the population of periovulatory Runx1+ cells seems rather aspecific. I think the authors could increase the robustness of the data/evidence regarding this cluster. Particularly because they go on comparing periovulatory and antral GCs. Could at least one differentially expressed marker from the volcano plot be validated?

2. The author used tSNE for visualization of the generated scRNA seq dataset, which, according to my knowledge, is outdated for scRNA seq data visualization as its reproducibility has become an issue. Which version of the Seurat package does the author use? And also the other software information should be implemented. Therefore, I suggest the author reanalyze their dataset using an updated Seurat pipeline, and also reanalyze all of their data using UMAP.

3. It does not appear that Figure 2 represents a real "subcluster" analysis. Instead, these cells are from the original clustering performed on all cells. To get a better resolution as to the different cell types, it would be best to perform a subcluster analysis where these cells are first extracted from the total data set and then re-clustered using more relevant principal components (for example, see Niu and Spradling, 2020).

4. For the pseudotime analysis presented in Figure 4 the authors excluded the mitotic and putative atretic granulosa cells. What is the justification for this?

5. The reviewers also have many other suggestions that the authors should likely consider to clarify the manuscript for the broad audience of eLife readers.

Reviewer #1 (Recommendations for the authors):

I think this is a fantastic dataset, but I think it could be better explored. The relation between different stages of estrous/lactating and the histology/validation could have been better explored and the cell types more explicitly named. I am not sure the Monocle analysis is clarifying things, this is tricky to use and I would consider using other comparable methods to determine the trajectories.

I have some points that I would like to see clarified:

– How was it determined that the postpartum 10-day females were lactating or not-lactating?

– Could the authors color the cells per oestrus phase, postlactating, randomly next to Figure 1B? It would be very useful to understand how the different cells in the initial clustering are represented in the different groups, particularly to determine the periovulatory follicles. In that sense, it would be very helpful to have corresponding histology of the ovaries in the respective cycle phase from the beginning. This aspect of the manuscript should be better explored. Also, the ovary from the lactating/nonlactating could be provided.

– Could the authors clarify what cluster corresponds to theca externa? In the text, they mentioned the expression of Mfap5, but in Figure 2 they only mention smooth muscle cells. How are the population for the smooth muscle cells and theca externa connected and or differentiated? This is confusing the text and Figures. In other words: where are the theca externa cells in Figure 2? Perhaps the authors could provide fields with higher magnification, eventually in the Suppl Figure? Could the "smooth muscle cells" simply be the theca externa?

– In Figure 2 is also not clear where are the theca interna cells, although the authors do mention those in the text. This is confusing. Please refer to the theca interna in the text and Figure. Could there be two populations of Theca interna (steroidogenic) and the ones closer to the basement membrane? I don't see any evidence to call this 'immature' theca (see Figure 4C).

– Regarding the atretic granulosa cells: the follicle provided still looks rather healthy. Is there a second marker you could use together with Ghr to confirm that particular cluster corresponds to atretic GC? Or can you colocalise Ghr with a marker of atresia?

– In addition, the periovulatory marker chosen does not seem very specific. I would suggest the authors choose a better marker. Otherwise, the identity of this cluster remains inconclusive. Moreover, what is the evidence that this would be periovulatory follicles? Is this the phase of the cycle? This could be better explained/evidenced, perhaps using histology of ovaries corresponding to the respective stages.

– The 3 clusters of granulosa cells (Figure 3) in the corpus luteum are intriguing. I wonder whether the authors have an explanation for that. What are the oestrous stages the cells were observed in?

– I am not sure the Monocle results (Figure 4A-B) are informative because the theca are not separated in theca interna and externa. Hence to me, it is unclear how the mesenchymal clusters, if they are well determined and reflect biology, relate to each other.

– In the Monocle in Figure 5C-D, I have similar issues – why are the periovulatory GC that is the visualization look very much like mural GC in a completely different branch than mural GC? I have the impression that either the clusters need to be refined/validated further or the Monocle is not providing meaningful results regarding lineage trajectories. Why would the "periovulatory" GCs be at the end of the CL-branch? In addition, the population of periovulatory Runx1+ cells seems rather aspecific. I think the authors could increase the robustness of the data/evidence regarding this cluster. Particularly because they go on comparing periovulatory and antral GCs. Could at least one differentially expressed marker from the volcano plot be validated?

– I am not sure the Monocle analysis is clarifying things, this is tricky to use and I would consider using other comparable methods to determine the trajectories.

– In Figure 4C: if the authors claim that the stroma is more medullary or cortex. In the Results, they do not visualise it. Hence, I would remove the claim from the Results but keep it in the Discussion.

– Results on the OSE should be shown in the Results section, now they are part of the Discussion? Where are those cells? What clusters? Etc. This population is very interesting/elusive and should be given proper attention/validation in the Results. In addition, the authors mention no differences between the estrous states: this should be clearly shown in the Results.

– The Discussion is too long, in particular, the discussion on the biomarkers reads more like a review than a discussion of your results. This should be shortened and made concise.

Reviewer #3 (Recommendations for the authors):

1. The introduction is very brief. It would be improved with a more thorough description of the estrus cycle beyond simply naming the stages. For example, how many days is the estrus cycle in the mouse? This would make the paper more accessible to non-experts.

2. Data availability- The authors have deposited the count matrix of the combined inDROP scRNA-seq dataset at Open Science Framework. However, for this dataset to serve as a useful resource for the wider community, the processed data should be uploaded to the Broad Institute Single Cell Portal (https://singlecell.broadinstitute.org).

3. The abstract indicates that in addition to ovaries isolated from the four stages of estrus, scRNA-seq was also performed on ovaries isolated from lactating or non-lactating 10 days postpartum mice, and from randomly cycling mice. However, cells from these later samples were never presented or discussed. It is therefore not clear what cells were used in the analysis. To make this clear, Figure 1 (or a supplemental figure) should include a tSNE plot where the cells are color-coded based on their sample origin (i.e. like Figure 5A).

4. Figure 1 – Given that this is the first figure, it would be good to show a tSNE plot that identifies which cells are from which library.

5. Figure 2 – It does not appear that Figure 2 represents a real "subcluster" analysis. Instead, these cells are from the original clustering performed on all cells. To get a better resolution as to the different cell types, it would be best to perform a subcluster analysis where these cells are first extracted from the total data set and then re-clustered using more relevant principal components (for example, see Niu and Spradling, 2020).

6. For the data presented in Figure 2, it is not entirely clear what is novel and what is already known. There are no references to the genes used to identify the cell sub-types types. References that are cited in the tables are not listed in the reference list. These references should, at a minimum, be listed in a supplemental text and it should be made clear in the text what genes are novel.

7. In addition to the markers chosen for specificity (e.g. Mafap5), it would be nice to see representative UMAPS (or dot plots) showing standard cell-type markers (e.g. Tcf21, Dcn, Notch3, Cxcl12). This could be a supplemental figure.

8. The description of the mesenchyme cell subpopulations is confusing as the authors do not use consistent terminology. A more concise definition of theca interna, theca externa, mature theca and immature theca as it relates to theca 1 and 2, stroma 1 and 2, smooth muscle would make the paper more accessible to the non-expert.

9. Line 196: Text refers to "dividing mesenchyme (8%) as seen in Figure 2A" but this population is not labeled. Which subcluster of cells is this referring to?

10. Line 204: Confusing to use theca externa when Figure 2C is labeled smooth muscle. Defining theca interna vs. theca externa, as mentioned above, would help.

11. Line 206: "…whereas Hhip was expressed in theca interna and immature theca (Figure S2A, B)." What is the difference between theca 1 and immature theca? Are these the same?

12. Figure 2 FigSup2: hard to see Acta2-Mfap5 overlap in Figure S2B. A higher magnification image would be helpful. It looks like there are two distinct cell layers, not the same cells. Also, Hhip expressing cells appear to be located outside of the Acta2-expressing cells, but Hhip is referred to as marking theca interna while Acta2 is said to mark theca externa. This needs to be explained.

13. Figure 2C – To make interpretation of the expression patterns more accessible to the non-expert, I suggest labeling some structures in these figure panels (e.g. oocyte, granulosa cells, cortical, medullary).

14. What cell type are the mitotic granulosa cells most similar to? Antral/mural or preantral/cumulus? Or are they an intermediate between these two? Subcluster analysis, as mentioned above, may help to better define their relationship.

15. Line 228: What is the justification for identifying these as atretic? What is the significance of Ghr to atresia? References would help.

16. Fan et al., used the following gene expression signatures to distinguish cumulus from mural GC's: cumulus GC (VCANhigh/FSThigh/IGFBP2high/HTRA1high/INHBBhigh/IHHhigh); mural GC (WT1low/EGR4low/KRT18high/CITED2high/LIHPhigh/AKIRIN1high). However, in Table S5 Fst and Inhbb are listed as markers for mural, not cumulus cells. This should be explained.

17. For the pseudotime analysis presented in Figure 4 the authors excluded the mitotic and putative atretic granulosa cells. What is the justification for this?

18. Figure 4D and E – Why are the preovulatory cells at the terminus of the pseudotime with CL2, while CL1 and CL3 cells positioned along the root. This does not match expectations. The discussion suggests that the developmental progression is PO>CL2>CL1>CL3, but this is not supported by the trajectory analysis. This calls into question the usefulness of the pseudotime analysis. It is mentioned in the discussion that instead of the different CL clusters representing a developmental progression, they are instead distinct cell types within a CL. This could be resolved with double RNA in situ hybridization using CL cluster-specific genes.

19. Figure 5A – It would be nice to show 4 separate plots for each of the stages. Hard to see this on a single plot. Perhaps 4 smaller panels next to A. It would also be helpful to label the different cell sub-types so the reader does not need to refer back to Figure 3.

20. Figure 5B – It would be helpful to label this panel "Proestrus-Estrus," following that in Figure S5.

21. Line 270 – reference to Figure S5D should be Figures 5E.

22. Figure S5D – This figure panel is not mentioned in the text.

23. Line 270: "…involved in wound repair during ovulation." This needs a reference.

24. It is stated that the motivation for identifying stage-specific secreted biomarkers was to identify markers that would be useful for staging in assisted reproduction and other applications in reproductive medicine. This begs the question if Prss35, Nppc and Tinagl1 are also expressed in human ovaries? Was this part of the reason they were selected?

25. Figure 6B: I think panel B should be first since it is from the scRNA-seq data set and then A is validation. I would also add Lhcgr and Pgr to the dot plot in B. Also, it makes more sense to put Inhba next to Nppc.

26. Figure 6A: The graphs in A are somewhat randomly organized, which makes it unnecessarily complicated. These should be reorganized to group factors high in P vs. E together and those high in E vs. P together.

27. Figure 6C: Follicle stages should be labeled. Mural vs. Cumulus cell should be labeled. Would be best to show both follicles that are labeled and ones that are not labeled to emphasize that this is a stage-specific expression. I cannot see Nppc expression. Might be helpful to have a higher magnification or arrows pointing to expressing cells.

28. Line 234: Run-on sentence: "Early pre-antral follicles…"

29. Line 384- Fan et al., reference should be deleted here.
