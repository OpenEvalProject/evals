# Peer review - Round 1

Editors:
- Akhilesh Pandey, Mayo Clinic United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58783.sa1](https://doi.org/10.7554/eLife.58783.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

While large-scale identification of post-translational modifications by mass spectrometry has become trivial, determining the extent of these modifications remains a challenge. FLEXIQuant-LF permits an assessment of the extent of PTMs without the use of heavy labeled standards and should be especially useful in large-scale experiments involving cellular dynamics or perturbation experiments.

Decision letter after peer review:

Thank you for submitting your article "FLEXIQuant-LF: Robust Regression to Quantify Protein Modification Extent in Label-Free Proteomics Data" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Philip Cole as the Senior Editor. The reviewers have opted to remain anonymous. The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The manuscript describes a method for quantifying modifications of peptides through analysis of intensity of unmodified peptides. The authors highlight that it is capable of large-scale identification and quantification of differentially modified peptides without any prior knowledge of the type of modification. The method was applied to DIA data from an experiment designed to study APC/C complex to benchmark and to identify differentially modified peptides in a time course setting. The obvious advantage of this method is that it does not rely on heavy isotope-labeled proteins/peptides. The manuscript describes a novel method, which is likely to be impactful for the field and could be a good fit as an eLife Tools and Resources paper. However, the way the manuscript is currently written is quite confusing in several places. The authors are advised to submit a revised manuscript that addresses the following issues:

Essential revisions:

1) Modifying the text and the Materials and methods section to emphasize that changes are measured in unmodified peptides and that the modification is not directly measured at all. Perhaps, the authors could consider including a graphic to illustrate this.

2) The authors assume that the number of molecules of each unique peptide derived from a protein will be equal. Because in routine proteomic analyses, this is not always true possibly due to the different degree of digestions at different proteolytic sites. The authors should address this issue.

3) Since many peptides often contain multiple potential sites of modifications (e.g. several phosphorylation sites on the same peptide), it is not possible to accurately measure the phosphorylation dynamics for each site. The authors should modify their claims and discuss this important caveat.

4) Although the authors state that FLEXIQuant-LF allows quantification of the modification extent without prior knowledge of the type of modification, they should explicitly state that after this analysis, the exact type of modification is still large unknown.

5) The authors should carry out an artificial positive control experiment using synthetic peptides to provide better understanding to readers of how well the algorithm works.

6) The authors should apply FLEXIQuant-LF to one of publicly available label-free phosphoproteome datasets with known answers regarding the extent of phosphorylation? If the authors can do this and obtain similar conclusions, then it can indeed be presented as a powerful strategy that can be applied in many studies.
