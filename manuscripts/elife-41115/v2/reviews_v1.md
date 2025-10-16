# Peer review - Round 1

Editors:
- Bavesh D Kana, University of the Witwatersrand South Africa

Reviewers:
- Bree Aldridge, Tufts University School of Medicine United States

## Review text

DOI: [10.7554/eLife.41115.024](https://doi.org/10.7554/eLife.41115.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "High resolution mapping of fluoroquinolones in tuberculous lesions reveals immune cell type specific distribution" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Wendy Garrett as the Senior Editor. The following individual involved in review of your submission has agreed to reveal her identity: Bree Aldridge (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Effective distribution of drugs to the site of infection is critical to control TB disease, which presents with complex lung pathology, often with heterogeneous lesions at different stages of development. In their submission, Dartois and colleagues attempt to explore tissue distribution of fluoroquinolones (FQs), which are central to the treatment of drug resistant TB. Using imaging mass spectrometry, combined with histological assessment of the same sections, the authors study tissue distribution of FQs in tuberculous lesions from infected rabbits. Previous work demonstrated that FQs distribute into the cellular cuff of necrotic granulomas and in this current submission, the authors further unravel these observations. They also develop and apply interesting statistical analysis algorithms to spatially locate quantify drug distribution.

Key findings:

1) Moxifloxacin (MXF), levofloxacin (LVX) and gatifloxacin (GTX) distribute to a region adjacent to the caseous center of the granuloma.

2) FQs preferentially distribute into foamy macrophages close to the caseum or into less-foamy macrophages in the outer layers of the granuloma.

3) MXF appears to be preferentially taken up by macrophages in the granuloma cuff over other immune cell types. These observations were confirmed in drug uptake assays where FQ uptake was higher in macrophages when compared to other cell types.

4) Preferential accumulation of FQs in foamy macrophages isolated from human PBMCs.

The study is clearly presented and the following should be addressed:

Essential revisions:

1) Mention is made of "same-section" analysis by MALDI and histopathology but the workflow in Figure 1—figure supplement 1 suggests that MALDI is done on one section and histopathology is done on a distinct adjacent section. Adjacent is also mentioned in some figure legends. This becomes confusing again when the legend in Figure 3 mentions "same-section". From the text in the first paragraph of the subsection “Macrophage content and distance from lesion margin drive the penetration of MXF”, it seems clear that the same section was used for MALDI and histopathology, this should be kept consistent throughout the manuscript.

2) The authors report a 1.5 to 2-fold increase in FQ distribution in cellular lesions when compared to uninvolved lung and caseum. This difference seems relatively small. Does it translate to meaningful differences in effective killing concentrations (MICs) in the different components of the lesion? Can statistics be provided for Figure 1—figure supplement 2? What do these differences mean for bacterial clearance in these regions?

3) Better images need to be provided for Figure 2—figure supplement 1H – it's hard to see the bacilli, very fuzzy.

4) Various quantitative analyses were conducted, which are referred to and found under different sections like statistical analysis, correlation analysis and modelling. It is difficult for the reader to follow these different sections and the manuscript would benefit of a re-arrangement of Materials and methods and Results into one section called Statistical analysis where the different types of analysis could have subsections and be presented. It is accepted that some of the statistical analysis have been presented before but as an example, the modeling part is unique to this article. As such, the description of the analysis needs to be somewhat more extensive. A more detailed model development section illustrating the development of the base model and the covariate analysis as well as information about the software used and how model diagnostics were done would be good.

5) The validation step of the analysis is not clear. What does this add? The statement in the manuscript that the validation confirmed the predictive value of the model equation is somewhat questionable. A proper validation step would have required a distinct data set, generated separately from those used to build the model but with a different condition. As an example, this can include comparison of a different dose in PKPD than was used to build the model but still within the covered dose range used for model development. It would be more appropriate if all data in the current manuscript were used for model development and no validation step made. This would also most likely reduce the uncertainty in the model parameters and perhaps change the covariate analysis with respect to statistical power. Please address this.

6) It seems that immune cells in tissues were identified by their morphologic characteristics on H&E which is inaccurate. A more appropriate approach, which may be technically difficult, would be to use specific immune-stains or preferably, flow cytometric separation of cells from tissue homogenates and subsequent measurement of drug levels. Flow cytometry was performed for human blood samples but not for rabbit tissues. Given that these methods were not used, please clearly state in the Abstract and concluding remarks that only H&E staining was used to differentiate cell types in rabbits and that this is a limitation of the study.

7) The significance of the human blood data is unclear. In tissues, the drug distribution is affected by the tissue architecture, fibrosis, etc. but this is not accounted in the blood data. Also explain how this is an advance over Carlier et al. (1990) and Michot et al. (2006). How much drug is protein bound? Are these data simply reflecting drug lipophilicity? Finally, please add a statement regarding IRB approval/exemption.

8) Supplementary figures show the tissue to plasma ratios at several time-points after drug administration. However, except at early time-points (<2 hours), wouldn't these ratios be significantly affected by the plasma clearance (half-lives ~few hours)? The tissue concentration effect noted over time may simply be due to a lower plasma level (denominator) rather than a true, absolute increase in tissue levels. Can the authors address this possibility?
