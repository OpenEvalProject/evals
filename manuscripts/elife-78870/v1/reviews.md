# Peer review - Round 1

Editors:
- Julie M Overbaugh, https://ror.org/007ps6h72 Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78870.sa0](https://doi.org/10.7554/eLife.78870.sa0)

This study applies a new novel method of single cell detection to biologically relevant systems to try to understand whether glycans on the surface of CD4+ T cells impact HIV susceptibility. They find that cells expressing higher levels of fucose and sialic acid are more likely to be infected with HIV than those with low levels. The findings point to glycans as biomarkers and potential determinants for cellular susceptibility to HIV, and open the door to new avenues for studying the interplay between cell surface glycans and viral infections.


---

# Peer review - Round 1

Editors:
- Julie M Overbaugh, https://ror.org/007ps6h72 Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78870.sa1](https://doi.org/10.7554/eLife.78870.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "CyTOF-Lec: Single-cell glycomics analysis reveals glycan features defining cells differentially susceptible to HIV" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Satyajit Rath as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Julie M Overbaugh (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

These suggested revisions are mostly meant for clarity.

Ma et al. take a novel approach to an important problem of host cell susceptibility to HIV. They tackle an understudied area of glycan effects on HIV infection using a new method they developed called CyTOF-lec. This method allows single cell detection of infected cells when using a reporter virus for infection. Importantly, the authors go to considerable trouble to use biologically relevant systems, including a transmitted virus and tonsil, endometrial and peripheral T cells. They find that cells expressing higher levels of fucose and sialic acid are more likely to be infected with to HIV than those with low levels. The studies presented here suggest, although didn't fully resolve, that sialic acid itself may be important for infection in CD4, CCR5 positive cells, although they can't really rule out that sialic acid is simply a biomarker for other cell features, such as activation state and entry receptor levels, which are known to impact susceptibility to HIV. Nonetheless, the findings point to glycans as a biomarker and potential determinant for HIV cells susceptibility and open the door to new avenues for studies the interplay between cell surface glycans and viral infections.

Histograms and dot plots in Figure 1 and S1 show broad unimodal distributions of lectin staining. How much overall information is being gained from these lectin stains? As part of the validation and general description of staining, Figure S1 would benefit from tSNE plots of total CD45 tonsil cells colored by intensities of each of the lectins (perhaps annotated by major subsets). This would be useful to provide a sense of how much the staining with each of these lectins varies and co-varies across broad cell subsets. Along similar lines, some representative histograms for lectin staining would be good to add for key figures showing differences in lectin staining (e.g., differences plotted in Figure 3). Also, for Figure 4, please show how high vs. low staining cells were gated.

It's confusing that both signal intensity (MSI) and gating are used to analyze data in Figures3-5

Did the authors perform replicates and quantify changes caused by Sialidase treatment? Please indicate the number of replicates

It is surprising how variable the scales are across tissues and this raises concerns about the possibility of technical reason for this. For instance, that tonsil cells have 10-old lower AOL binding than PBMCs (in several figures including Figure 4C). Were these tissue samples stained and run in parallel in order to test for these differences? Could there be difference in the way that the cells were collected or processed that might be behind this? Conclusions from the section ending on line 262 are not clear.

The tSNE plots provided throughout are poorly annotated in terms general features of the different regions of the plot. Where possible, some effort to better annotate major populations within these plots would be appreciated. It would also be appreciated if the authors limited the number of unique tSNE embedding used. For instance, was tSNE run in parallel the plots shown in Figure 5? If not, if possible it would be great if different tissues could be merged unless batch effects a major issue for these analyses? A general trend in high dimensional analysis has been towards the use of UMAP, which are often more intuitive and easier to annotate. Did the authors consider using UMAP instead of tSNE?

tSNE plots colored by AOL and WGA staining in Figure 4C, 5C are difficult to read. Larger dot size and font sizes for scale labels would be helpful.

The weakest data in Figure 6 J, where increasing removal of sialic acid has just a 2-fold effect on the number of infected cells. Some information in the results of repeat experiments would be helpful as would perhaps studies with higher MOI or more sailadase. If not, the limitations of these findings should be noted.

Related to the point above, why is the effect of sialidase in Figure 1 so modest? A quick explanation there may help explain the limits of the Figure 6 experiment.

For Figure 6, while maybe not inconsistent with the premise of the paper, is it possible that WGA staining is working as a partial proxy for memory phenotype? Tm cells were used as a control but no significant difference between Tm and WGAhigh cells in terms of infection rate is reported in this experiment. While maybe not necessary, the authors could have sorted WGAhigh vs. low cells from within Tm cells to more specifically control for memory status. Similarly, perhaps the analysis in Figure 4D-H could be performed just on non-naïve cells to see if lectin staining differentiates subpopulations of non-naïve cells?

It is good to see the use of corrections for multiple comparisons. They make the findings more robust and impressive.
