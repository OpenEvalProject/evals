# Peer review - Round 1

Editors:
- Melanie Blokesch, Ecole Polytechnique Fédérale de Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70597.sa1](https://doi.org/10.7554/eLife.70597.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This manuscript presents the development and validation of a new tool for the characterization of peptidoglycan (PG), the essential cell wall polymer of bacteria. PG is a single large macromolecule that protects almost all bacterial cells. The newly developed open access tool will greatly facilitate comparative quantitative analyses and the determination of compositional diversity of PG, which might ultimately contribute to the development of new antibacterials that target this essential cell wall component.

Decision letter after peer review:

Thank you for submitting your article "PGfinder, a novel analysis pipeline for the consistent, reproducible and high-resolution structural analysis of bacterial peptidoglycans" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Gisela Storz as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Seemay Chou (Reviewer #2); Anthony Clarke (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The authors are encouraged to revise their manuscript by properly stating two weaknesses of their tool (as it stands in its current form):

1) The lack of important PG modifications in the mass spectrometry-based library of the muropeptides such as O-acetylation; inclusion of such modification would be required for the broader application of the analysis tool (e.g., as those modifications are frequently encountered in pathogenic Gram-positive bacteria);

2) The emphasis on comparative analyses between different samples (e.g., from the same species/strain but grown under different conditions) versus absolute quantification using MS, which might be more challenging. Future users are therefore encouraged to include appropriate controls.

Reviewer #1 (Recommendations for the authors):

Lines 285-288 say, "The present study confirmed that the complexity of bacterial PGs was greatly underestimated until now. Our unbiased search identified >106 masses matching E. coli muropeptide structures representing a number strikingly larger than previously reported (Kuhner, et al., 2014)." This may be an overestimate of the increase in complexity revealed by the new method of analysis. While older methods certainly identified fewer muropeptides, I think it was understood that the range of modifications and crosslinked dimers and trimers was greater than what was identified, and that many low-abundance muropeptides were present. Many of these could be predicted. This does not diminish the importance of this tool for allowing the rapid identification and quantification of many of these assumed muropeptides, but the actual increased demonstration of complexity should not be overstated.

Lines 298-301: The authors describe the advantages of muropeptide quantification using XIC, such as resolving overlapping peaks. There should also be a discussion of challenges of quantitative analysis using MS data, such as potential differences in ionization efficiency between muropeptides with significantly different peptide side chains, with possible lower detection of larger muropeptides due to lessor ionization, or differences of in-source fragmentation. Older methods using UV absorbance quantification were likely more accurate for quantification across the diversity of identified muropeptides, but missed low abundance muropeptides.

Lines 305-306: I agree that this represents a powerful tool for qualitative and reproducible PG analyses. The demonstration of absolute quantification is not clear. Yes, quantitative differences between the C. difficile strains is very clear, and the reproducibility of differences between the measured E. coli average cross-linking between this method and published values is clear, but whether the lower cross-linking determined by this method are more accurate is not clear. Is this due to greater detection of minor muropeptides or more accurate quantification of all muropeptides species? Or is the difference due to lessor detection of ions for the cross-linked muropeptides?

Lines 369-370 say, "Samples were diluted to contain 150mAU/μl of the major monomer. Based on the dry weight of the PG sample, we estimated that this corresponded to approximately 50μg of material" It is not clear what this 50 µg is. Does this dilution produce a suspension of 50 µg/µl? Does the resulting 10 µl injected for UHPLC contain 50 µg?

Reviewer #2 (Recommendations for the authors):

Below are several comments/questions on the paper as a whole but also on some specific sections.

1. The workflow was explained in detail in the text and also through the use of helpful schematics

2. Automating the analysis of MS cell wall data is a major advance in the field, especially through the use of open-source software.

3. Line 147, do you think the remaining 52-59% of total ion intensity is noise? If so, why so much? Or do you think there is some real signal that you are missing? If so, what could be improved to capture that?

4. Lines 149, what stereoisomers are you referring to? How do they form? Do you think these form in living cells?

5. Lines 158, 165, and 169, the authors found some discrepancies between current knowledge on E. coli PG and their data.

a. They stated in the text that further biochemical and molecular biology studies would be required to validate their findings.

6. Line 236, why did you increase the mass tolerance here to 25ppm? What was the problem if you used 10ppm as you did for the previous analysis?

7. The authors established the application of an alternative open-source deconvolution software.

a. They showed that it works as well as the commercial counterparts.

b. Lines 244-246, they described variability issues with the deconvolution step – what could be done to improve the software used here? This could help with the application of your approach across more datasets.

8. The authors provided multiple schematics that are helpful to visualize their workflow.

9. Their previous study and this one demonstrate the capacity for discovery when this type of unbiased approach was applied.

a. Especially regarding their novel findings for E. coli and C. difficile PG composition.

10. Their approach has advantages such as open-access and availability as a Jupyter notebook that would make it broadly available in the community. However, they also describe issues that need to be addressed.

a. One such issue is the ability to analyze MS/MS data.

11. The paper establishes high standards for other studies relying on MS data but also in general for other cell wall papers relying on chromatographic techniques

a. Biological replicates, list of searched muropeptides, and general data reporting

12. Some of the methods rely too heavily on previously published protocols. Could you provide brief details on the steps you followed in this study?

a. Lines 354, 361, and 395.

13. Check spellings of meso-diaminopimelic acid – it varies across the paper.

14. Correct g-D-Glutamate to γ-D-Glutamate – several instances across the paper.

Reviewer #3 (Recommendations for the authors):

1. Lines 125-126: Why did the authors limit the modifications to PG in their Library 3 to only those listed on these lines. Importantly, given that all pathogenic Gram-positive bacteria, and many Gram-negative bacteria produce O-acetylated PG, this reviewer is surprised that this modification was not (apparently) included, especially since reference is made to it on line included in Line 332 of the Discussion. This addition would be necessary for the analysis of the PG from these bacteria given the levels of O-acetylation which would greatly influence % compositional analyses of the various muropeptides.

2. Throughout the manuscript, including main and supplemental figures and tables, the authors have used J as their one-letter code abbreviation for diaminopimelic acid. Unfortunately, the IUPAC-IUB Joint Commission on Biochemical Nomenclature define J as the one-letter code for the combination of either isoleucine or leucine (I/L) ; please see, e.g., http://www.insdc.org/documents/feature_table.html#7.4.3.

All letters of the Latin alphabet are already used, and the Joint Commission states Dpm as the abbreviation for diaminopimelic acid. Using J as the (defined) abbreviation may have been acceptable with its isolated use, but it is very problematic when combined with the conventional code for the other amino acids. Clearly, using the three-letter abbreviation in combination with the one-letter code is awkward (particularly when convention usually requires the use of one or the other, not their combination) but in this instance, maybe the only option. Unless, the authors want to consider introducing another unconventional approach and move to eg., Greek and use delta for Dpm. This maybe going too far, but I can't think of any other alternative.
