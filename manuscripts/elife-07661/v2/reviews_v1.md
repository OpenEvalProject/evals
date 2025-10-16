# Peer review - Round 1

Editors:
- Arup K Chakraborty, Massachusetts Institute of Technology , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07661.031](https://doi.org/10.7554/eLife.07661.031)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “An open-source computational and data resource to analyze digital maps of immunopeptidomes” for peer review at eLife. Your submission has been favorably evaluated by Tadatsugu Taniguchi (Senior editor), Arup K Chakraborty (Reviewing editor), and two reviewers.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript describes the use of the SWATH-MS methodology for identification and cataloging of HLA peptide repertoires – viz., 'the Immunopeptidome'. The manuscript is based on an international collaboration between a few laboratories specializing in HLA immunopeptidome analysis and the laboratory of Dr. Aebersold, who developed the SWATH_MS methodology. In the past, HLA peptides were mostly identified by shotgun proteomics, which is based on the selection of peptides from purified pools of peptides for fragmentation in the mass spectrometer during the LC-MS-MS analysis. The SWATH_MS approach does not select specific peptides for fragmentation, but instead scans repetitively incremental mass windows of about 25 mass units, every time fragmenting all the peptides that are present in each of these mass windows. The method allows fragmenting all the peptides which have the mass divided by charge of the mass region being scanned more than once. The advantage of this approach is the better reproducibility of the data while the disadvantage is the lower sensitivity and the need to establish beforehand a library of spectra of the individual peptides that will be used for identification by the SWATH-MS approach. The use of the peptide preparations and the LC-MS-MS data from the different collaborating labs resulted in successful establishment of a large repository of peptides and their spectra libraries in a format that will be made public and will serve a large community of researchers, enabling better collaborations.

Overall, the work reported in this paper could be a significant resource for the community. But, the following issues need to be addressed to further establish the robustness of the method.

Major points:

1) In the Introduction, it is suggested that Data-Dependent Acquisition (DDA) used for such analyses of MHC peptidomes results in less reproducible results. This is a well-known fact, but it would be good to show the reproducibility of the results of the same three raw data files when analyzed by the SWATH-MS method and a figure with parallel Venn diagrams indicating how many peptides are identified in each analysis in total, and how many are shared between the runs.

2) Peptide presentation by HLA C is ignored because it is claimed that they are expressed in low amounts. In Schittenhelm et al. (Tissue Antigens, 2014, 83, 174-179, 2014), an HLA immunopeptidome of HLA C is reported using the C1R cell line. Since the same cell line is used in the present study, ignoring peptide presentation by HLA C seems to be inappropriate. This point needs clarification or inclusion of HLA C in the analysis.

3) Several search engines (Comet, MS-GF+, X!Tandem) were used to identify peptide sequences from the mass spectrometry data. As can be seen from Figure 1—figure supplement 2, different engines identify quite different numbers of potential peptides. How should these results be interpreted? Should the union or intersection of these peptide sets be used?

4) The HLA annotation score, based on the predicted IC50 binding affinities from NetMHC server, is used to associate peptides with particular HLA alleles. In a similar server, Immune Epitope Database (IEDB), sometimes the values of experimentally measured and predicted values of IC50 can differ by a factor of 10 or more. Using the NetMHC server are the results more robust, thus allowing use of cutoff of value of 3 for the HLA annotation score?

Minor points:

1) In the first paragraph of Results and Discussion, the comment “no reference computational framework is currently available to facilitate the analysis of such datasets” is not entirely correct, since software tools, such as MaxQuant, Perseus, or X-PRESIDENT can handle HLA-peptidome data without effort (for example: see the second reference cited, Bassani-Sternberg et al. 2015).

2) In the second paragraph of Results and Discussion: “of all identified peptides to their respective HLA allele” is an overstatement, since significant parts of the identified peptides are not annotated to their respective HLA allele.

3) In the third paragraph of Results and Discussion: “Three synthetic EBV-derived peptides were also used to build the HLA-A02 and -B07 library. How can three peptide by useful for building two libraries? Some clarification is required.

4) In the fourth paragraph of Results and Discussion: “Class I peptide precursors fall within the range of 400-700 Th” – this is not correct, since many peptides fall outside this range. We suggest clarifying the percentage of the peptides which fall within this range, and indicating if the loss of these peptides compensate for the additional 17% gained by use of this narrow range. Also, why was the 400-650 mass range selected?

5) In the subsection headed “Isolation of HLA peptides”: We suggest adding the reference by Hunt et al. 1992 to the references for the method of affinity purification and LC-MS-MS analysis of MHC peptidome.

6) In the subsection “Generation of HLA allele-specific peptide spectral and assay libraries”: Please clarify that the parameters are used for Spectrast, and explain what they mean for readers that do not use Spectrast.
