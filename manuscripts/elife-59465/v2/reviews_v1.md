# Peer review - Round 1

Editors:
- Nima Sharifi, Cleveland Clinic United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59465.sa1](https://doi.org/10.7554/eLife.59465.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your article identifies distinct luminal epithelial and periurethral populations of the adult mouse prostate using a single-cell sequencing approach. Furthermore, you identify the human prostate counterparts to these distinct populations of mouse prostate cells, which together advances the our understanding of the relationship between human and mouse prostate populations.

Decision letter after peer review:

Thank you for submitting your article "A single-cell atlas of the mouse and human prostate reveals heterogeneity and conservation of epithelial progenitors" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Nima Sharifi as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard White as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Mark Rubin (Reviewer #2); Justin D Lathia (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This study is a well-done single-cell comparative atlas of the mouse and human prostate. Their studies were from two whole mouse prostates, 4 samples corresponding to each of the lobes and 3 independent sets of human prostate for comparison. Altogether, they identify lobe-specific luminal epithelial populations (LumA, LumD, LumL, and LumV) in the distal region and the proximally-enriched luminal population (LumP) that is not specific to any lobe and a periurethral population (PrU) that has both basal and luminal features. Organoid studies suggest that LumP and PrU cells are multipotent progenitors. Comparisons to the human prostate suggest that the mouse lateral prostate is most like the human peripheral zone – from which the majority of prostate cancers arise. Altogether, this is generally a well done study. The nature of the study is fundamental, the paper is generally well written and the studies themselves generally well-described. All three reviewers concur about the importance of this body of work.

Essential revisions:

Most of the comments pertain to optimizing the clarity of presentation and data accessibility. Please see the specific reviewer comments below.

1) Title. A title referencing the work as an atlas should make the atlas more publicly accessible and reproducible than an expression matrix. Either remove atlas from the title/text or consider making this group of work more accessible to the community so that it can be utilized as an atlas. One way to do this would be to place these data into a shiny app or some other sort of online single cell viewing portal (UCSC cell browser, or the broad institute single cell portal). This is especially important because you use Randomly and many people will place this data directly into other pipelines such as Seurat and the clustering will be different so people may not be able to query your exact populations without further information from your group. Following this the entirety of the code should be published with this manuscript since a newer method clustering is used and there is no single package that this data is being ran through.

2 Subsection “Distinct luminal epithelial populations in the mouse prostate” – please refer how the samples were dissociated for single cell seq here as this is important for future studies.

3) Subsection “Distinct luminal epithelial populations in the mouse prostate” – The Randomly package is explained and referenced but then in the Materials and methods section there are almost 3 pages about Randomly and the equations used. I believe it is enough to say at which steps you implemented the use of this published package and then move on from here. Additionally, please briefly mention that batch effect correction was done and how. I know this is in the Materials and methods but in general one should be able to read in 2-3 sentences the sequencing depth, method of data alignment, batch correction, use of randomly, and then downstream analysis. Extra detail about each of these steps and the exact settings used if not default settings can be added into the Materials and methods.

4) Subsection “Distinct luminal epithelial populations in the mouse prostate” – – it's my belief that these tSNE plots should be UMAPs to show your clusters better. For example, Figure 1A has intermixing of luminal A and D but viewing this as a tSNE I don't know if these clusters are mixed because they are similar and there is a population of LumD that appear more similar to LumA. There is also a PrU cell that appears in the center of the plot away from the rest of the PrU cells. I think these should be re-graphed as UMAP plots for the whole paper. At the very least they should be in the supplement as UMAPs but I suspect they will represent your data better and you may want to swap them once they are graphed.

5) The description and biology of the cellular constituents of the mouse prostate and comparison to human anatomy are well done. In human, the normal prostate anatomic origin of prostate cancer is well worked out. This group has pioneer several different mouse prostate cancer models. Given the profiling in the current paper, can they comment or show data on the cellular origin of mouse prostate cancer? The genetic models may have divergent origins and may be multifocal; however, one wonders if they bear some resemblance to LumP or PrU cells, at least more so compared to the other cell and anatomic types.

6) Subsection “Spatial localization and morphology of epithelial populations” – "suitable antibodies" is vague and needs to be expanded on what makes them suitable.

7) Subsection “Spatial localization and morphology of epithelial populations” – "specificity" for their markers also should be expanded on, without knockdown and knockout mice you can't prove the antibody is specific. It is simply enough to say that we utilized and stained with these antibodies and demonstrated that there was little or no background on the secondary only controls.

8).Subsection “Functional analysis of epithelial populations” – Figure 3C is unclear what these flow plots actually represent? What was the starting population or flow and what gates preceded these representative panels. Include this in the text and figure legend.

9) Discussion, first paragraph – function properties are noted and it would be nice to see differential gene expression showed for the groups and the significantly expressed differences between groups should be published as supplementary tables.

10) Subsection “Data availability”. Utilizing new methods of single cell analysis and calling the data an atlas and identifying new cell types necessitates that this data be available in a better format than GEO. The entirety of the code along with metadata showing which cells are in which clusters need to be made available. An added bonus would be uploading it to a portal so people can query their own genes with the cell clusters you identified but at the very minimum the above criteria should be met.

11) Referencing/novelty – There are several single cell studies in this general area, but are not referenced, and they should be (PMIDs: 31317052, 30566875, 29233929). It is acknowledged that this study is clear different, but the reader should be made aware of the current state of the field.
