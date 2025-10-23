# Peer review - Round 1

Editors:
- Patricia Bassereau, Institut Curie France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29213.031](https://doi.org/10.7554/eLife.29213.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Detection of human disease conditions by single-cell morpho-rheological phenotyping of whole blood" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ivan Dikic as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Dennis Discher (Reviewer #1); Amy C Rowat (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. The editors and reviewers agree that this work is interesting and potentially quite useful however, as your effort is directed at the development of a new technique rather than a discovery with novel conclusions, we feel it will be more appropriately published as a Tools and Resources paper rather than as a Research Article.

Summary:

Blood cell numbers, sizes, and deformability have been quantified for many decades at the single cell level under normal and numerous diseased conditions for 2-3 decades or more, although throughput for deformation measures is more limited. This manuscript describes a microfluidic approach to the above quantitation, called MORE (cell-by-cell morpho-rheological) analysis, capable of treating around 1000 blood cells/s, from 10 µL drop of blood only, adding deformation information for each cell type. The principle of the method is based on image acquisition by high-speed video-microscopy and post-acquisition image analysis. The method correctly phenotypes different blood cells using both their typical projected area in the constriction as well as their compactness or their deformation. Adding a third parameter for classification represented by the "brightness" of the cells, the authors are successfully able to reproduce most of the classical and simple hematological phenotyping present on the market of automated blood counts without any staining steps. Moreover, the authors provide a comprehensive set of examples from leukemia patients, or malaria infection, bacterial and viral infections as well as donor samples with anti-coagulants.

Overall, this manuscript is well written, interesting and timely. Its strength is clearly the technology, with an impressive collection of data validating expectations, and only a few key concerns temper enthusiasm. We have the following suggestions to improve the manuscript.

Essential revisions:

1) The authors over-use the acronym MORE, in particular in the captions. They should replace these with text that highlights the new biological finding or concept that is learned. Moreover, the authors should highlight what is scientifically new for the well-established field of hemorheology.

2) Statistical significance and confidence should be clarified at different places.

- Figure 3D the number of EBV cells is not provided. Also, authors define n as number of independent experiments, does this reflect the number of patients or the same patient cells measured over independent experiments? It would be helpful to show single cell distributions for EBV given the focus of the paper.

- The authors need to comment on the utility and statistical significance of deformation measurements in Figure 4D for the 4-6 patients with AML or ALL, since the deformation data adds little to nothing beyond cell size measurements.

- Given that Figure 4E-H is a time series generated from just one patient, it is at least important to provide measures of statistical significance and confidence. Each datapoint is the median for a given day, and so error bars should be added for each day. An asterisk could be added to each datapoint that differs from the first, or some other scheme. More important, given that this is a new method, some type of daily standard (i.e. normal control) should have been run and shown in parallel with the patient measurements. Knowledge of how this data compare to conventional biomarkers/existing methods for analysis following treatment would be helpful to benchmark RTDC.

3) Figure 2D,E shows control vs exposed but then data shown in Figure 2F also includes infected. The difference and disease relevance of exposed vs infected populations should be clarified for the reader.

The authors claim the greater deformation reduction of infected cells vs entire exposed population (Figure 2F), which may be explained by clearance of stiff cells by the spleen. But if stiffer cells are filtered out by the spleen, this would result in a lower deformation reduction.

It is unclear why the 2BP and PA treatments were performed. It would be helpful for the reader to clarify the motivation for these treatments as they relate to pf infection.

4) Subsection “MORE analysis of leukocytes” what is the timepoint of mechanical measurements of activated neutrophils published in the older reports? If measurements were performed at different time points, with different methods that deform cells on vastly different timescales, it does not seem to be a conflict.

Neutrophils were less deformable after fMLP treatment, but became more deformable and larger at longer time points. Given that 'larger cells of identical stiffness should deform more in RTDC' (subsection “MORE analysis of malignant transformed blood cells”), how can these results show that fMLP cells, which are bigger, are less deformable? If larger cells are deforming more in RTDC (and when deformed by inertial flows as in Gossett et al.), then it is difficult to compare to previous methods.
