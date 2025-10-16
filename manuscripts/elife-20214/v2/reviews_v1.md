# Peer review - Round 1

Reviewers:
- Joseph S Takahashi, Howard Hughes Medical Institute, University of Texas Southwestern Medical Center , United States

## Review text

DOI: [10.7554/eLife.20214.034](https://doi.org/10.7554/eLife.20214.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Blood transcriptome based biomarkers for human circadian brain pacemaker time" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Pål O Westermark (Reviewer #1); John B Hogenesch (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Laing and co-authors developed an unbiased circadian phase prediction method using partial least squares regression (PLSR) to model the relationship between whole-blood mRNA abundance profiles and their corresponding melatonin phase. Knowing body time is increasingly important for drug development and delivering medicines at optimal times for treatment. In this paper, the authors collected published datasets studying circadian transcription and plasma melatonin levels in human blood samples under different sleep conditions. Using these data, the authors compared published methods to predict body time with transcripts. The authors also developed their own partial least squares regression (PLSR) method to predict body time. Compared with the Molecular timetable and ZeitZeiger methods, PLSR better predicts circadian phase with blood transcripts.

In principle, the topic of the paper is important and the findings are novel and PLSR seems to be an advance; however, there was no statement regarding the availability of the PLSR code or information on what language it was written. Without this, it will be difficult to independently confirm the authors' work, or have the larger research community make use of the method. This reduced the enthusiasm for the paper among the reviewers.

Essential revisions:

1) Because the paper is long and so verbose, the main point of this paper is hard to understand. All of the main texts and figures should be more concise. Many figures are of technical nature and should perhaps be shown in the supplement. In the present manuscript version, the important messages drown in a wealth of material of more technical nature.

2) The SCN phase is not the same as the melatonin phase, the authors describe "predicting the circadian phase of the SCN" throughout the manuscript. As the authors described in Discussion, actual error in SCN phase measurement by melatonin is not known. The authors should use "melatonin phase" instead of "SCN phase". In addition, knowing the melatonin phase is not a panacea for delivering drugs at appropriate times for all diseases (for example, knowing the phase of the liver for a liver-specific disease may be more relevant than knowing the melatonin phase). The authors need to add discussion for this point.

3) The authors should make the code available (e.g. an R package, e.g. ZeitZeiger, or Python or whatever). In addition to making the code available, a more detailed description of PLSR should be included.

4) The authors did a good job of pointing to the primary data. However, they should also document the code/scripts used to run the Molecular timetable method, ZeitZeiger, and PLSR so that others can replicate this analysis.

5) What influence does the size of the training set have on PLSR's accuracy?

6) Can PLSR be used to rule out rhythmicity (ala Molecular timetable and ZeitZeiger)?

7) The Molecular timetable method has also been used with metabolite data. Does PLSR work with metabolite data as well?

8) From Table 1 and Figure 4I, PLSR under-estimates melatonin phase (negative error value). Is this correct?

9) The Agostinelli et al. paper is cited. BIO_CLOCK should be added to the algorithms benchmarked here.

10) This model improves upon previous models, but what advantage does this improved model have over previous models? Or, what advantage does this model have over just measuring melatonin? For example, what disease would benefit from having a model that has 20% error compared to 10% error? Of course, having a more accurate model is better, but it's not clear what problems or challenges that this new model will solve. Or what issues could be addressed that were not addressed by previous models?

11) The SD of the prediction error is on the order of 2-3 hrs. Is this likely to be enough for the method to be practically useful in e.g. clinical applications?

12) Authors should explain why they think only PER1 was identified in both molecular timetable methods (subsection “Molecular Timetable and Zeitzeiger methods”, second paragraph).

13) Authors should explain why they think those particular 4 genes were identified as circadian in all four conditions (subsection “Molecular Timetable and Zeitzeiger methods”, second paragraph). Because other hnRNPs can directly regulate AANAT, the rate-limiting step in melatonin biosynthesis, is it possible that hnRNPDL is also directly regulating AANAT (as opposed to, or in addition to, NRF as the authors suggest in their model)? And could this regulation occur via locally produced melatonin from peripheral blood mononuclear leucocytes?

14) In Figure 2, the cutoff correlation value of 0.3 is slightly arbitrary because there is so much variation in model performance with slightly different correlation values. For example, a cut-off correlation value of 0.4 performs almost as well as 0.3. Authors should discuss about this point.
