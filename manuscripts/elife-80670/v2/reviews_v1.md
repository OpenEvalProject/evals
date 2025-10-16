# Peer review - Round 1

Editors:
- Sonia Sen, https://ror.org/04xf4yw96 Tata Institute for Genetics and Society India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80670.sa0](https://doi.org/10.7554/eLife.80670.sa0)

This article describes cell types in the head of the squid, Loligo vulgaris, through expression patterns of key genes identified in single-cell transcriptomics. This topic is generally of great comparative interest. The data presented here are convincing, and these valuable findings will contribute to a better understanding of the cephalopod nervous and sensory systems, providing a basis for future comparative and evolutionary research.


---

# Peer review - Round 1

Editors:
- Sonia Sen, https://ror.org/04xf4yw96 Tata Institute for Genetics and Society India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80670.sa1](https://doi.org/10.7554/eLife.80670.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Molecular characterization of cell types in the squid Loligo vulgaris" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Sonia Sen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Didier Stainier as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Samuel Reiter (Reviewer #2); Astrid Deryckere (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While appreciating the relevance of this there were a set of common concerns raised by the reviewers that need to be addressed. These are:

1. The reference transcriptome: A high-quality reference transcriptome will be critical for any downstream analysis. Could the authors please provide data for how they validated their reference transcriptome? For example, the authors could report the BUSCO score for assessing the completeness of their assembly, a cumulative density plot of AED scores for annotation quality, and any other metric they choose. Could the authors also report what percent of their single cell reads mapped to the reference?

2. The scRNAseq data: Could the authors please provide data that would allow readers to assess the quality of their single-cell data? At a minimum, could they please provide violin plots depicting the range of UMIs, genes, and mitochondrial genes per cell?

3. Cluster-specific markers: Could the authors please provide dot plots for the top differentially expressed genes for all clusters? In addition to this, the authors have described a set of genes that they did not identify as cell-specific markers (for example, neurotransmission-related ones). Could they please show dot plots for these as well?

4. Trajectory Analysis: Could the authors please explain how they have chosen the cells used in this analysis, the clustering resolution they have used (please provide a dimplot), and which starting point they have selected? In addition to this, could they please analyze the differentially expressed genes along the trajectory to make their claim stronger? Since this data challenges the current state of the field, it would be useful to demonstrate the robustness of their results by verifying it by:

4a. Using different trajectory analysis methods (Monocle or FateID).

4b. Analysing more marker genes (in addition to foxD1) along the differentiation axis.

5. The writing: Could the authors please pay attention to some aspects of the text to help the reader place their work in the broader context of the field? Specifically:

a. There are missing references (see detailed reviews below), including three other recently posted cephalopod scRNAseq preprints. Could the authors please incorporate these references?

b. On occasion, the chronology of the text and figures don't match. There are also some figures that are currently not mentioned in the text. Could the authors please fix this?

c. Many of the methods are not sufficiently well explained. Could the authors please pay attention to this, particularly for bioinformatics? Could the authors motivate this better?

d. The Results section contains many points that would belong better in the Discussion section.

e. Conversely, the discussion as it currently stands, is a summary of the results. Could the authors please revisit their discussion to place their work and findings in the context of the growing field of cephalopod neurobiology?

Review #1 (Recommendations for the authors):

1. I was concerned about the quality of the scRNAseq data for a few reasons:

- The number of genes per cells (200-2000) seems low to me.

- The clusters don't really resolve.

- Many genes that one would have expected to pick up, for example, neurotransmitter-related genes for the neuronal cluster, were not picked up.

So, could the authors please provide the violin plots depicting the range of UMIs, genes, and mitochondrial genes per cell?

2. It was not clear to me how the authors picked the marker genes. Could they provide the top 20 DEGs for each of the clusters?

3. The signal in each of the images could be enhanced. To orient the reader, it would also be useful to have an inset of each of the expression patterns in the whole head. Some of these are really nicely represented in the supplementary information.

4. The authors should refer to the three recent preprints that have used scRNAseq in other cephalopods and, in the discussion, place their work in this context.

5. In general, could the authors elaborate their method sections? Many fairly important aspects are too briefly described – for example, the reference transcriptome and its validation and the selection of marker genes, among others.

Reviewer #2 (Recommendations for the authors):

The core of this study is the analysis of scRNAseq data. Here the authors assembled a transcriptome de novo. I wonder about the quality of this assembly, as it will affect all downstream analysis. The other 3 studies (Styfhals et al. bioRxiv 2022.01.24.477459; doi: https://doi.org/10.1101/2022.01.24.477459; Songco-Casey et al. bioRxiv 2022.06.11.495763; doi: https://doi.org/10.1101/2022.06.11.495763; Gavriouchkina et al., bioRxiv 2022.05.26.490366; doi: https://doi.org/10.1101/2022.05.26.490366) all refer to the necessity of a high-quality reference genome for a high-quality transcriptome. If this is not the case here, it would be useful to quantify this.

I found the analysis of stem cells and progenitors quite interesting. The authors profile specific markers for cell types, map these cell types onto interesting anatomical regions, and analyze developmental trajectories defined transcriptomically.

In other parts of the paper, I was surprised that many cell types could not be defined based on certain marker genes/small combinations of genes. Figure 2b, for example, shows that clusters have a great deal of overlapping expression among 'marker' genes. This would deviate quite a bit from the other scRNAseq studies I am familiar with. I could see a few possible explanations: (1) This is a product of low-quality transcriptome assembly/single-cell data (2) This is a product of the immature developmental stage of the animal, and (3) This reflects a cephalopod-specific transcriptomic signature.

I doubt possibility 3, as the other 3 cephalopod scRNAseq papers describe cell types well differentiated (eg. By neurotransmitter expression, Figure 2 in Songco-Casey et al. 2022, Figure 3 in Gavriouchkina et al. 2022). The fact that specific neurotransmitters are often not well localized to specific cell types here calls for an explanation. Similarly, the lack of differentiation of neural types even when analyzed separately from other cell types (Figure 2c). Many phototransduction genes are expressed in Cluster 32, and these genes are expressed, specifically in the retina. They could potentially be used as a sanity test for the scRNAseq: Are these genes only found in cluster 32?

The lack of specific marker genes makes some of the FISH experiments in this manuscript less informative than others. Many plots show anatomical localization of a gene broadly expressed in many cell types, meaning we cannot conclude how transcriptomically identified clusters map spatially. In other cases, FISH is used to mark individual cell types. In some cases, it is not clear which situation we are looking at. It would be useful to have a quantification of how specifically the marker genes used in FISH experiments mark individual clusters.

The authors observe a similar anatomical expression of fmrf and reflectin-8 in the olfactory organ. Because these have been linked to chromatophore and iridiophore control, they argue that this suggests that chromatophores and iridiophores are modulated through the olfactory organs. I find this plausible but the logic questionable. FMRF has many functions unrelated to chromatophore modulation, so just observing its presence seems insufficient to make statements about the neural control of chromatophores. Reflectin-8 is shown later in the manuscript to be broadly expressed in the epidermis and brain (Figure 5c).

I was not clear why the expression of elav-like 1 in the epidermal lines 'informs on their potential mechanosensory function'. With elav-like 1 expressed very broadly across cell types and anatomical locations.

The expression of the cilia-associated protein, rab3 and synaptogyrin-1, and other cilia/flagella markers in cluster 27 suggested that this corresponds to a mechanosensory population. To test whether this is neural, the authors take the subset of cells in the dataset expressing amyloid β- binding-like (a neural marker) and see whether a subset of these also expresses the collection of sensory markers. This seems round about to me. Why not look directly at whether the cells in cluster 27 express amyloid β- binding-like? If the probability of co-expression is high, then concluding that these cells are neurons seems warranted. If the probability is lower, then the conclusion does not seem warranted. The author's existing analysis does not address the possibility that non-neurons (those not expressing amyloid β- binding-like) express the collection of sensory markers.

Line 63: 'Coleoid cephalopods, which have internalized or lost their shell over evolutionary time 64 were able to swim more easily and could exploit other niches.'

Not clear what 'other' refers to. The niches of ammonoids? Not clear whether it was the loss of shell that led to niche exploitation or the other way.

Line 93 "… as a first step to understanding cephalopod evolution". I'm not clear why a molecular comparison would be a first step to understanding cephalopod evolution. What then is the non-molecular evolutionary story given earlier in the introduction?

Figure 2 Are the Umap plots in 2c re-estimated on the subset of data in A? If so, I don't see a description of this in the methods section, and I am surprised at the lack of cell type differentiation among neurons.

Figure 4D is described as 'feature plots'. Is this UMAP? How are the plots on the right-hand side generated?

The developmental trajectory analysis using slingshot could be better explained in text/methods/figure legend and not easily interpretable from Figure 3e if one is not familiar with the technique

'Additionally, the cephalopod-specific chromatophores, which are colored or iridescent, have been suggested to be modulated by the nervous system'. Maybe I am misunderstanding the sentence, but as I read it this is an understatement of what we know. Over 50 years of work have profiled the neural control of chromatophores in detail.

Some of the supplementary figures are quite dark. Why not increase the brightness of the images? Others like Figure 4 supplement 1 are beautiful.

Reviewer #3 (Recommendations for the authors):

First of all, I would like to congratulate the authors on the extensive expression analysis study performed in this manuscript. However, I believe that this dataset offers so many more opportunities to better understand cell types in cephalopods, and in general, the data could be analysed and interpreted in more detail.

Since the field of scRNAseq is moving incredibly fast, the authors should be careful with claims of being first (e.g. Abstract line 34). Preprints of scRNAseq data in the nervous system of other cephalopods have been recently published (Styfhals 2022, Gavriouchkina 2022, Songco-Casey 2022).

The manuscript is missing key citations to support the results and to provide a comparative view of gene expression in other cephalopods. For example, the expression patterns of Elav, SoxB1, Asc have been reported during the development of octopus, squid, and cuttlefish, and could enhance the interpretation of the results observed in Loligo.

In general, the reader needs to be proficient in the brain areas of cephalopods in order to follow the results. Therefore, the manuscript would benefit from a short introduction of the main brain lobes in cephalopods to be accessible to a wider audience, either in the introduction or in the results in Figure 1C.

Please make sure to refer to the figures and figure panels chronologically. Multiple figure panels are not referred to throughout the text (e.g. the first figure described is Figure 1B and there is no notion to Figure 1A, similar to Figure 2, …).

The authors distinguish 33 cell clusters when using 25 pca's and a resolution of 2. The UMAP, however, shows most cells in one single, central blob. This is striking knowing how different connective tissue is from neurons. Did the authors try other methods for clustering and dimensionality reduction, or change the parameters in the current algorithm to try to resolve the data better? It would also be helpful to specify the filtering parameters for filtering out low-quality cells in the methods section.

In the first section of the results, the authors list a handful of enriched genes used to differentiate the major cell type categories. However, little explanation is given to why these genes were chosen and a comprehensive overview supporting the claims is missing. It would help the reader if they would add a plot (e.g. a DotPlot) to support these data. In addition, a UMAP plot with cells colored according to cell cycle could clearly show where the progenitor cells are located on the UMAP.

To avoid going back and forth between cell type categories in the first results paragraph, it would be helpful to describe Cl 27 (lines 202 onwards) and Cl 32 (lines 207 onwards) with the other nervous system cells, and Cl 29 (lines 213 onwards) with the epidermis section.

In order to interpret HCR expression patterns, the authors should add axis labels to the figures. In addition, I understand that the figure panels are small to add annotation of the brain regions, but since we are looking at different levels through the brain, either a schematic with the figure or annotation would really help.

The authors should explain the analysis performed to obtain the UMAP(?) plots in Figure 2C. Which cells were selected? Were they re-clustered? What do the clusters look like?

Did the authors perform image manipulation e.g. Figure 2C and 2D for the DAPI channel? Why is DAPI absent from the neurons in the tetraspanin-8 HCR, or the serotonin transporter staining?

In Figure 3B, it would be helpful to add some genes involved in proliferation, as exemplified in the text.

The authors claim that neural stem cells undergo neuronal differentiation and then migrate to the nervous system. However, evidence is missing as the authors do not show where progenitor cells stop dividing and start to differentiate.

The use of the marker foxD1 for differentiation neurons is not well supported. Additional marker analysis is required before this can be claimed.

The authors need to explain which clusters were used for trajectory analysis using Slingshot and how the data were reclustered. Were non-neuronal stem cells included? This might skew the analysis. Importantly, the method was not described in the methods section. It is critical for the readers to know which endpoints were selected in the slingshot algorithm. Off note, the slingshot is very dependent on clustering resolution and will try to connect all clusters. Have the authors tried a different pseudotime analysis method such as Monocle or FateID? Additionally, can the authors elaborate on which transcription factors are steering this differentiation? In the current state, the analysis is preliminary and contradicts present data on the origin and trajectory of neurons in the cephalopod brain (see comment below; Koenig et al. 2016, Deryckere et al. 2021).

With the current interpretation of the data, the authors claim that foxd1 cells are an intermediate developmental state of neurons. This would be very striking since the cortex of the optic lobe has been described as being the inner retina. Additionally, it is contradicting the expression of amyloid β-binding like in the optic lobe cortex, which the authors say is only expressed in differentiated neurons. Is amyloid β-binding-like expressed in clusters 15, 19, and 20? How about other markers for differentiated neurons? What would all those intermediate cells do there? Do the authors think they migrate into the medulla or even the central brain? This is contradicting existing literature on the origin of neurons in the cephalopod brain (Koenig 2016, Deryckere 2021) and requires in-depth discussion.

The authors prepared beautiful summary diagrams in Figures 3 and 4. However, they should be referred to in the main text.

After performing extensive HCR expression studies, can the authors go back to their scRNAseq data and better annotate the different clusters?

In order to better understand neuronal diversity and neural cell types (as the authors claim), the dataset has to be analyzed in more depth. 33 clusters/cell types seem low given the number of cells that were sequenced and the different tissues that were sampled. Can the authors identify the different brain regions when subclustering the neurons? Can they identify and annotate different neural cell types?

The authors present several striking findings. However, at the moment, the Discussion section explains the results obtained in the paper, but does not place the acquired data within the current state-of-the-art. Parts of the results should be moved to the discussion and the discussion should be elaborated on.

Specific comments:

Line 76: "by the use its specialized iridescent cells" misses an of

Line 97: it would be helpful for the readers to add the "pre-hatchling stage" to stage 28, as was done in the Results section for the audience to have a better idea of what stage was studied.

Throughout the text (starting line 219) please write "HCR ISH" instead of just "HCR". The chain reaction method is not specific to in situ hybridization and can also be used in immunohistochemistry and others.

Line 101: "in all animals" please be more specific; not all animals have neurons.

Line 110: "marking distinct stages of neural development", neural differentiation would be more appropriate.

Line 126: Add a reference to Figure 1A to show what the head region is.

Line 133 says 34 cell clusters were identified, but Figure 1B shows 33.

Line 145: "smooth muscle-like cells (Cl26)" should be Cl25.

Line 156-159: add a reference for this statement, maybe a specific example.

Line 167-171: "a gene whose function is homologous to …" and " exact function … is not known". This is contradictory. Do you mean that the gene's sequence is homologous?

Line 199-201: with the comments below on SoxB1 and Ascl1, this sentence needs to be revisited.

Line 239-240 and also further in the text: "in the medial portion of the optic lobes" do the authors mean the medulla (in contrast to the cortex (inner and outer granular layer))? Medial portion is not clearly defined and the cortex also stretches quite medially. (also line 278, 540).

Lines 263 and 271: please rearrange the supplementary figure so you can refer to panels A-D first. In general, please refer to figures chronologically.

Line 298 with Figure 2D: please switch panels of LIM and serotonin, so they follow the text.

Line 326: this part covers more than stem cells and progenitors (line 375 and onwards).

Line 327: please add an introductory sentence to this new paragraph; rephrase the first sentence (grammatically incorrect).

Line 338-340: this is an overstatement. What identity are the authors referring to? Genes involved in proliferation etc do not give identity to stem cells and Cl02 and Cl14 are also actively cycling. Do the authors suggest only Cl10 and Cl17 are stem cells? Can the authors show more evidence?

Lines 350-359: I would suggest moving this part to the discussion and incorporating the following comments:

Lines 347-352: The expression of Asc is not as well conserved as the authors suggest. Indeed, it has some proneuronal role, but the level of differentiation in the cell it is expressed is very different across the animal tree. In Drosophila as in other non-insect arthropods, Asc is expressed in quiescent ectodermal cells to drive them into the neural lineage (formation of a neural progenitor cell) (e.g. Cabrera et al., 1987; Skeath and Carroll, 1992). In contrast, in vertebrates and also in spiralia such as capitella teleta, Ascl1 is expressed in neural progenitor cells to drive them into differentiation (e.g. Bertrand 2002; Sur 2020). Ascl1 expression has been studied in octopus and seems to have a similar function as in capitella, not Drosophila (Deryckere 2021). This scRNAseq dataset has the power to test this hypothesis and figure out whether, in cephalopods, as is expressed in proliferating and not quiescent cells.

Lines 354-355: this conclusion does not reflect the data shown. The authors are showing proliferating stem cells, not the location of differentiation. In octopus, differentiation seems to happen in the transition zones (NeuroD cells, Deryckere 2021). It would be interesting to locate those cells in your dataset.

Lines 356-359: Again here, one needs to be careful to extrapolate the functionality of a gene in one species to other species. In invertebrates, SoxB1 is also expressed in differentiated neurons (e.g. Le Gouar et al., 2004; Semmler et al., 2010). Additionally, expression of SoxB1 has been described in Sepia (Focareta and Cole, 2016) and octopus (Deryckere 2021), indicating expression in neurons (with some interesting discrepancies). Furthermore, be careful with the use of the word "neuroblast" because it refers to different types of cells in different animals.

Line 361: "Interestingly" it seems a general theme for cephalopods, and maybe invertebrates in general (see comment above).

Line 367: Data are missing to show where the neural progenitor cells differentiate.

Line 370-374: in line with this, SoxB1 expression is also found in sensory epithelia of sepia and octopus (e.g. suckers and statocyst; Baratte, S. and Bonnaud 2009; Deryckere 2021).

Line 376-378: add a reference and elaborate. Regulators of development is a very general process. In addition "for this reason, these cells were presumed to be differentiating cells": this is an overstatement and needs additional gene expression patterns to support this presumption.

Line 382-385: optic lobe cortex = inner and outer granular layers, please adjust and rephrase. From Figure 3C upper panel, it seems that Foxg1 is also expressed in the medulla. Or is this all cortex? Annotation would be helpful here.

Line 386: this is an overstatement. Most neurons in the brain express elav1 and the function of foxD1 is very broad. Additional markers (like for example NeuroD) are required to support this claim.

Lines 394-400: Figure 3D is not mentioned in the text and seems substantial. The authors might also want to revise it with the comments above and in public review.

Lines 408-411: please add references to support these statements.

Lines 419-421: Why did the authors choose to map the expression of Pax9? Koenig et al. studied the eye in Doryteuthis and mapped the expression of several genes important for eye development. A reference to this work would be appropriate here. Pax9 is not an eye gene in vertebrates and invertebrates (in contrast to Pax2/6). In which clusters is it expressed (again here, a dotplot of the genes under study would be helpful)? The level of the image in Figure 4A for Pax9 is also different than the others, why is this? In which cells of the eye is Pax9 expressed?

Line 448: Figure 5B should be Figure 4B I think.

Line 457: can the authors verify that they selected cells with expression level >3? From the legend in Figure 4D, the expression level of 3 seems present in a lot of cells (it looks more like the selected level was 5). In addition, the authors should explain how they obtained the graphs on the right. It looks like they underwent an extra transformation? Or are they just distorted?

Line 459, and together with the comment above: It would be helpful to be able to check the cluster numbers. For example, are cilia-associated protein cells from Cl27? A dotplot or heatmap might be more convincing to support these statements.

In addition, please add a reference to Figure 4D here.

Line 468-470: egf-like does not seem to be expressed in Cl03 and 31 from Figure 5A as suggested in the text.

Lines 471-493: please add the discussed genes to the dotplot in Figure 5A or supplement.

Line 541: It seems that cells in Cl27 do express neuronal markers. Please revise.

Line 545 and onwards: please not only discuss the results obtained but place the discussion in the state-of-the-art literature. Several statements have already been proposed in other papers which deserve to be referenced (e.g. lines 559, 568). Multiple genes mapped with HCR in this manuscript have been described in other cephalopods and assigned a preliminary function (e.g. Buresi 2013, 2014; Shigeno 2015; Koenig 2016; Focareta 2016; Deryckere 2021 and others). Please acknowledge their presence in appropriate sections, and, if the authors which, they might add a paragraph describing consistency or differences in expression.

Line 562: in line with previous comments in the results, please revise. This is based on the functionality of asc in Drosophila, but not other animals. Additionally, in the opinion of the authors, what are the asc+ e2f3- cells?

Line 713: please add the parameters used to filter low-quality cells.

Line 722: please add additional information on how cells were subclustered (and re-clustered?). Please add a description of the slingshot analysis.

Figures:

In general, please rearrange so each panel comes chronologically in the Results section. Make sure to mention each panel in the text.

Add axes to the confocal images and consider annotation.

Figure 1:

A) Is this the ventral view instead of the dorsal view? The funnel is visible?

Please arrange the abbreviations alphabetically. Ibl and sbl are missing.

Figure 2:

Line 790: UMAP with clusters.

C) Add legend to the 1→6 expression? Bar. It is not clear how these featureplots were calculated. Which clusters were selected? Were they re-calculated? Please show the dimplot with cluster annotation. What is on the x- and y-axes? UMAP? t-SNE?

D) Please rephrase 'that were not represented in the scRNAseq data': do the authors mean not differentially expressed? Were the genes absent from the reference transcriptome?

Figure 3:

A) Why are Cl2 and Cl14 encircled?

C) Explain what the red encircled areas are.

Figure 4:

D) Double check that 3 is the threshold. The curly bracket is confusing (it reads like the right panels feed into the left). What are the x- and y-axes? Similar comment to Figure 2C.
