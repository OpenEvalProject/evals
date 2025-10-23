# Peer review - Round 1

Editors:
- Karla Kirkegaard, Stanford University School of Medicine United States

Reviewers:
- Jesse D Bloom, Fred Hutchinson Cancer Research Center United States

## Review text

DOI: [10.7554/eLife.46339.026](https://doi.org/10.7554/eLife.46339.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "HSV-1 single cell analysis reveals anti-viral and developmental programs activation in distinct sub-populations" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in review of your submission have agreed to reveal their identity: Jesse D Bloom (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Single cell analyses provide the unprecedented opportunity to study virus-host interactions while exploring and capturing the heterogeneity of cell responses. Although these studies have focused mainly on RNA viruses, the present paper focuses on the Herpex simplex virus 1 (HSV-1) DNA virus. They find that there is substantial heterogeneity among cells, the expression of interferon-stimulated genes is rare, and infection induces a developmental program in the cells. The study is interesting and well done, and the paper is well written.

Essential revisions:

1) All reviewers had questions about the population of uninfected cells and the discussion thereof.

- Subsection “Viral infection dynamics varies among individual cells”, first paragraph: how was the MOI titered? Only 50% of cells become ICP4-positive at a MOI of 2. This is extremely far off Poisson statistics, which would suggest that 1 – exp(-2) = 84% should be ICP4-positive. The aforementioned paragraph just shows that infection isn't Poisson suggesting some cells might be refractory to infection. This should be more explicitly discussed at this point.

- Subsection “Viral infection dynamics varies among individual cells”, third paragraph and Figure 1C: Clarity of the wording is important: cells can be exposed but not infected (the virus entered); cells can be abortively infected, i.e. the virus entered but cannot successfully replicate and cells can undergo productive infection. Thus, being ICP4- during imaging analysis does not allow discriminating between abortive and non-infected yet. In this context, I would rather write "of 1,814 cells exposed to HSV-1, […]".

- In Figure 1, only ICP4+ cells are shown and it is not clearly stated what criteria were used to distinguish ICP4+ and ICP4- cells, nor is the distribution for ICP4- cells ever shown. Please provide the intensity of the 818 ICP4- cells as well as their number. Then, after the scRNA-Seq, please include your interpretation that these data indicate that the majority of cells are expressing some% of viral transcripts and thus are bona fide abortive infections rather than non-infected cells (as only apparently a minor fraction of cells display 0% viral transcripts),

2) Provision of data and methods:

-The authors should add a figure supplement that shows some basic statistics on read depth per cell (and its distribution) for each sample. This is critical for evaluating single-cell RNA-seq, and doesn't appear possible to find now short of going to the raw data.

- The Materials and methods say that the scripts for data analysis are "available upon request." This is not adequate for a paper that relies so heavily on computational analyses. The authors need to provide the computer code, which is currently not contained as part of the paper. The scripts should be made available (eLife allows GitHub repos linked to papers), and the paper should not be accepted until these scripts along with some sort of reasonable README describing their use are available for examination. In addition, some further details (such as how the differential gene expression was done) should be added to the Materials and methods.

3) The very interesting idea of the role of the cell cycle in infection and signaling should be further developed rather than just mentioned as a possibility, given the richness of the data at hand. The scRNA-seq should allow the testing of correlation between viral phenotype and cell cycle. In the subsection “The cell-cycle affects HSV-1 gene expression” and Figure 2—figure supplement 1, please provide more details and results regarding the cell cycle score and how the outregression was performed (gene list used for the G2/M score and outregression).

Major comments:

1) Please include references to relevant papers such as Zhu and Jones, 2018, which shows that HSV1 viral production is inhibited upon treatment with iCRT14. It would be good also to cite other scRNA-seq papers on the sparsity of IFN induction in virus-infected cells, such as DOI 10.1128/JVI.01778-18 and DOI 10.1101/437277.

2) The expression of ISGs like IFIT1 and Mx2 which are produced in response to IFN-receptor signaling are most frequently analyzed. IRF3 activation is also examined and it would be helpful if the authors would discuss whether that was indicative of the cell-autonomous response, as one might conclude. This would help shed light on whether cells are detecting infection or just responding to signaling.

3) The argument that ISG expression is higher among low-virus expressing cells infected by deltaICP0 is not entirely convincing. It is true that in Figure 3D, all of the cells expressing ISGs are in clusters 1-3 (except two IFIT1-expressing cells in cluster 4 which are not accurately described in the text which says that no cluster 4 cells express ISGs). However, cluster 4 has many fewer cells, so maybe there just aren’t ISG expressing cells in that cluster by chance. Some statistics should be applied here. Also, Figure 2A, B, C appears to show a IFIT2 expressing cells with high viral expression. Please show additional data to strengthen the conclusions if available or obtainable. It is not clear whether the cell clustering analysis was performed taking into account viral transcripts or not. Could you please compare cell clustering with mock cells performed in parallel?
