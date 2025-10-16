# Peer review - Round 1

Editors:
- Pamela J Bjorkman, California Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61393.sa1](https://doi.org/10.7554/eLife.61393.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Biochemical Patterns of Antibody Polyreactivity Revealed Through a Bioinformatics-Based Analysis of CDR Loops" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Satyajit Rath as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Brian Baker (Reviewer #1); Bart Haynes (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below, we suggest substantial revisions. We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The authors present a bioinformatics pipeline to analyze a large aggregate data set of nearly 1,500 antibody sequences, seeking to uncover the biophysical underpinning of antibody polyreactivity – i.e., broad low-affinity binding to diverse epitopes. This is an important topic, relevant not only to Ab therapeutics, but to other assessments of immune repertoires and considerations of protein-protein interaction hubs in general. The unbiased informatics approach that is taken, largely separated from structural considerations, is a distinctive feature of the work, and an attractive aspect of the study. The authors identify two key determinants of polyreactivity: First, the binding interface tends to be neutral, i.e., being neither strongly hydrophobic nor hydrophilic, and lacking significant positive or negative charge. Second, crosstalk (measured by mutual information) between and within CDR loops increases in the heavy chain of polyreactive antibodies. The method of sequence alignment leaves out most structural information (except aligning by the center of each CDR loop) yet retaining the positional context.

The research goal of identifying biophysical properties that allow for promiscuity of a protein selected for strong binding to a particular target is of general interest and biomedical importance, and the approach of combining statistical analyses and information metrics is appealing. The lack of a clear smoking gun is an important finding, as it clearly illustrates the subtleties at play. A classifier is described at the end of the paper, showing promise for sequence-based predictions and applications to therapeutic Abs.

We believe the paper may be suitable for eLife with revisions to address the following concerns.

Essential revisions:

1) The reviewers have concerns about the binary distinction between polyreactive vs. non-polyreactive. The authors essentially sum up this concern in the third paragraph of the subsection “Systematic Determination of the Key Contributions to Polyreactivity”, as well as in the ninth paragraph of the Discussion. The fact that pharma has nonetheless articulated a test for polyreactivity does not make the problem binary, which is clearly recognized by the authors. One way around this would be to repeat the analyses in Figures 1-3 on the more stringently separated (albeit now smaller) dataset used for Figure 4. How do things change? Are there any stronger signals?

Also, this limitation, while articulated well in the Discussion, could be brought up in the Introduction. Forcing a non-binary problem to be binary is by no means unique to this study, but it is a limitation best addressed upfront. As mentioned above, a strength of the paper is the demonstration of the scope of the challenge.

2) A major concern is that, with the biased removal of antibodies that are harder to classify, the true statistics are distorted. This occurs in two places. First, to avoid overfitting of LDA, only input vectors with the largest average differences between the two populations are kept. But this necessarily introduces bias which simplifies the classification problem and distorts the statistical structure in the original data set. Second, upon observing that an intermediate exists between the two classes when applying LDA to a subsampled data set, the authors removed the antibodies that bind a moderate number of select ligands from the analysis. But this continuum of polyreactivity is a real, and likely important, data feature. Since all the subsequent analyses act on the input data, it is necessary to address, with a clear description and supporting evidence, that the main findings remain valid when using the full data set. After this is addressed, direct comparisons – LDA vs. PCA, and with other methods – should be provided to justify the choice of LDA over PCA, and the performance of this newly developed pipeline relative to existing methods.

3) There seems to be a jump from the LDA to mutual information, then back to LDA in the application to therapeutic antibodies. While the physical hints the mutual information gives as mentioned in the Discussion is appreciated, and this can be built on, is this incorporated at all into the analysis of the therapeutic antibodies?

4) Related to point 3, it is not clear why mutual information is a good choice for detecting correlated changes between residues, and there is no comparison to other methods and previous studies. Moreover, mutual information won't be able to distinguish between coevolution and crosstalk between residues. For instance, Direct Coupling Analysis (DCA) indicates that coevolving residues are often in physical proximity. This points to a weakness of lacking the structural information in this work. Thus, it is unclear whether increased mutual information really indicates crosstalk, or instead signals coevolution between residues. This ambiguity undermines the second determinant of polyreactivity.

5) The analysis is finally applied to therapeutic antibodies, which is considered a logical next step. But this is not well motivated – why, in the first place, shall one expect correlations between polyreactivity status of naturally-derived antibodies and the acceptance or discontinuation of a therapeutic antibody? Hence, this section didn't lend validation support to the approach. Perhaps the manuscript could be shortened by deletion of the therapeutic dataset. These antibodies are not natural and it is not clear what approved versus discontinued antibody means.

6) There are other major omissions. First, no performance comparison between this new software and other available methods of antibody sequence analysis is presented (all is said in words, with no supporting figures). Second, it is stated that the approach has been adapted and applied to analyze MHC-like molecules, but no data or references are provided.

7) While in general the manuscript is quite clear, some sections are less so. Is there nothing to be discerned from the identity of the top 10 weights shown in Figure 4? We are only given the identity of three (subsection “Systematic Determination of the Key Contributions to Polyreactivity”, last paragraph), and even then these are only mentioned in a cursory manner. How do these and the other heavily weighted terms relate to the biophysical clues gleaned from the earlier analyses?

8) In the Abstract, the word "offensive" is not defined and would best be "neutral charge" for reader understanding.

9) Introduction, last paragraph, it is not clear in the first sentence if there are 1500 polyreactive abs or a total of 1500 abs studied. It is clarified later but not clear here.

10) The authors use a relatively small panel of antigens to define polyreactivity, whereas a chip type of assay with more proteins may be more precise. This might be mentioned as a way to make the discrimination between PR and non-PR abs more precise.

11) Figure 1 is terrific and very interesting. The fact that VH1-69 in over-represented in the polyreactive group of antibodies is important, both because of the propensity of polyreactive/rheumatoid factor B cells in fetal liver to be VH1-69 and because the polar region (PR)-distal HIV gp41 MPER Abs frequently use VH1-69. Perhaps these associations could be referenced and discussed.

12) In the fifth paragraph of the subsection “A Surface-Level Analysis of Polyreactive Antibody Sequences”, can statistics be applied to determine if any difference between 27% and 17%?

13) Figure 3, were these p values corrected for multiple tests?
