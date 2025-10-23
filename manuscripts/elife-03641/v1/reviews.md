# Peer review - Round 1

Editors:
- Chi Van Dang, University of Pennsylvania , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.03641.022](https://doi.org/10.7554/eLife.03641.022)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Phenotype-based cell-specific metabolic modeling reveals metabolic liabilities of cancer” for consideration at eLife. Your article has been evaluated by Charles Sawyers (Senior editor) and 4 reviewers, one of whom, Chi Dang, is a member of our Board of Reviewing Editors. Our opinion is favorable but there are a number of major concerns that you will need to address before we can consider the paper for acceptance at eLife.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The authors present a novel method termed PRIME for building cell-specific Genome Scale Models and apply this technique for the reconstruction of metabolic models of normal and cancer cells. The work is interesting as it addresses development of technique that is able to predict metabolic phenotype, a problem currently lacking conclusive answers. However, because of its highly specialized nature, whether the paper would be useful to cancer biologists is unclear. Even if the authors computationally predicted 1 target that slows the growth of some cancer cell lines, would this represent a significant advance? How many targets would need to be validated to provide a false discovery rate or the true utility of the approach? In the absence of convincing biologic data, the computational methods become less relevant.

In this regard, additional experimental data should be provided. Specifically, the authors use siRNA to knockdown of MLYCD without providing any assays to determine if the knockdown was effective other than showing a modest suppression in total mRNA content that results in a modest suppression in cell growth. The authors need to assay the cells MLYCD activity, de novo fatty acid synthesis and fatty acid oxidation. The authors instead use steady-state metabolomics, which can be very misleading. For example, they go on to suggest that the mechanism of the selective toxicity results from a redox imbalance for which the argument (and data) are extremely weak. Furthermore, in humans, mutations in MLYCD cause malonic and methylmalonic aciduria (OMIM#248360) therefore the selective toxicity may be a cell culture artifact.

Another major concern is the lack of accompanying models or at least the base code of the method, which would facilitate easier dissemination. The authors can submit their code as supplementary documentation. It would also be great, if at all possible, to make the cell-specific GSMMs available for download, either from the journal's website, from a group resource, or from public repositories.

The Methods section entitled “The PRIME algorithm”, while overall well-written and presenting the basics of PRIME effectively, seems to have mixed up notation, because the text alternates between using i,j and t,p for reaction and sample sets, respectively. This can be particularly confusing since the i,j combination was used for the metabolite, reaction sets just in the previous section. Perhaps the authors were trying to fix that exact discrepancy, but the symbols were only replaced in part of the text. This should be made consistent throughout.

Not an absolute requirement, but rather a suggestion: the PRIME method presented here makes heavy use of MOMA. Since the authors take the time and space to briefly present and explain the FBA formulation, perhaps a similar short section on MOMA would be useful for the reader.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Phenotype-based cell-specific metabolic modeling reveals metabolic liabilities of cancer” for further consideration at eLife. Your revised article has been favorably evaluated by Charles Sawyers (Senior editor), a Reviewing editor, and the other three original reviewers. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) It's improper when one presents only one or a few metabolite isotopologues (mass-isotopomers). Only whole metabolite mass-isotopomer distribution (MID) ranging from m+0 to m+n (where n- number of C atoms in the molecule) makes sense. Please completely describe your observed MID for TCA cycle intermediates and palmitate isotopologues (Figure 5 and Figure 5—figure supplement 5) or at least describe that other mass-isotopomers were not observable.

2) It is not clear why m+1/m+2 isotopologue ratios for pyruvate and lactate are different; assuming that lactate dehydrogenase usually operates at near equilibrium condition. Please clarify.
