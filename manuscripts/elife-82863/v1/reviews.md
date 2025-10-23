# Peer review - Round 1

Editors:
- Ambra Pozzi, https://ror.org/05dq2gs74 Vanderbilt University Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82863.sa0](https://doi.org/10.7554/eLife.82863.sa0)

Your study provides strong and convincing evidence that pYtags enable spatiotemporal measurements of receptor tyrosine kinase signaling in living cells. This is highly significant as it can be used to study in real-time receptor signaling in healthy and diseased cells.


---

# Peer review - Round 1

Editors:
- Ambra Pozzi, https://ror.org/05dq2gs74 Vanderbilt University Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82863.sa1](https://doi.org/10.7554/eLife.82863.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "pYtags enable spatiotemporal measurements of receptor tyrosine kinase signaling in living cells" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jonathan Cooper as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Alex J B Kreutzberger (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Overall, the reviewers found your new approach, using RTK-ITAM fusions and fluorescent Syk or Zap70 SH2 domains to monitor RTK activation, to be exciting and innovative. The approach is explained well, and the experiments are clear and clean. However, as you will see from the original reviews and comments below, there was a divergence in opinion on the interpretation of the data and thus on the likely adoption of this new tool by the research community. During the review consultation, several themes emerged:

1. Use of different cell types makes it difficult to understand the effect of expression level (of RTK fusion and of SH2 reporter) on the kinetics of probe depletion from the cytosol. There are indications that the assay is capable of being very sensitive, but the use of multiple cell types, expression levels and measurement times makes it very difficult to determine the caveats of the system and the types of applications for which this is most useful. We recommend CRISPR/Cas9 insertion of the ITAM tag into the EGFR gene in the same cell type that is used for over-expression. NIH3T3 cells would perhaps make most sense, since they endogenously express ~40K EGFRs, or MCF10A, where many EGFR kinetics and imaging studies have been done.

2. Discrepancy between apparent sensitivity of the approach (ability to detect EGFR activation using the knock-in approach in HEK 293 cells, in which EGFR expression is thought to be very low), with the inability to detect ERBB2 activation by EGF unless EGFR is co-over-expressed. Use of supra-physiological concentrations of ligand (EGF) is also a concern. The sensitivity of the system should be tested with lower EGF concentrations.

3. Lack of calibration of the experiments. The readout of the system (% clearance) is highly dependent on the ratio of tagged receptor to fluorescent probe, the rate of access of the probe, and the number of internal pools and their rate of exchange. RTK activation will also depend on the ratio of the ligand to receptor as well as ligand affinity. However, it is felt that these parameters have not been properly taken into account or controlled.

4. The mathematical model makes use of seemingly arbitrary calibration factors rather than using biophysical quantities that have been previously established for the EGFR system. One reviewer questioned whether the mathematical model for dimerization is indeed needed and whether it enhances the message. If the authors feel that the mathematical model should be included, then the authors should consider cleanly calibrating an experiment to better parameterize the math model. If the math model could be used to extract fundamental numbers for the EGFR system, then the same principles could be applied to other ligand-receptor systems analyzed by the pYtag approach.

5. Since endocytosis of the tagged EGFR seems slower than reported for endogenous EGFRs in this system, controls are needed to show that tagging does not perturb EGFR signaling or internalization. Some type of EGF uptake or degradation assay in the cells with endogenous EGFR plus/min the tagging system would be an appropriate control.

Overall, it is felt that, as written, the manuscript provides a proof-of-concept rather than making a strong case for others to adapt this assay to study their receptors of interest.

Reviewer #1 (Recommendations for the authors):

1. On page 9, the authors state: "Notably, we observed that pYtag-expressing cells stimulated for at least 30 min with EGF contained internalized vesicles that were positive for both total EGFR and ZtSH2 (Figures 2C and 2D). Subsequent treatment with Gefitinib eliminated ZtSH2 from EGFR-positive vesicles within minutes, suggesting that the enrichment of ZtSH2 at vesicles is indicative of signaling from endosomal compartments (Figures 2C and 2D)." To conclude that the accumulation of EGFR and ZtSH2 in punctae that are vesicles/endosomal compartments simultaneous labeling with appropriate markers should be performed (see also below, point 2). The same applies to experiments performed on CRISPR-Cas9 genome-edited HEK 293T cells [page 18: "We also observed rapid and near-complete internalization of endogenous EGFR from the cell membrane, with some internalized vesicles retaining residual ZtSH2 labeling (Figure 6D, right-most panels)."].

2. It would be interesting (and maybe useful to add some novel insights) to follow the receptor routes after it has reached the cell membrane to observe whether the activation also occurs in (or from) specific endocytic compartments (e.g. Rab5 or EEA-1 positive early endosomes, Rab7 or LAMP1 positive late endosomes/lysosomes, Rab11 positive perinuclear/recycling compartment). This set of experiments could be performed by either simultaneously expressing fluorescent protein-tagged endosomal/vesicular markers or staining the corresponding endogenous proteins in cells that were fixed at different time points upon ligand stimulation.

3. The experiments over-expressing the pYtags were mainly performed in NIH3T3 cells, whereas the CRISPR-Cas9 knock-in was done in HEK 293T. It would be useful to check whether the same differences would be also seen in HEK 293T over-expressing the tag. After assessing this, further characterization of the signal emitted by the cell line generated by CRISPR-Cas9 would add some key concepts to RTK activity dynamics (e.g. the localization of the RTK activation signal in the genetically manipulated cells in Figure 6, looks quite different from the signal shown in Figure 1. In Figure 6, it looks more dot-like and less localized in cell-to-cell contacts. Do the authors have an explanation for this?).

4. Some experiments shown in Figures 1 and 2 were repeated only two times. The analysis of at least three independent experiments is in general a well-accepted standard.

Reviewer #2 (Recommendations for the authors):

Instead of using the raw data to test a model of dimerization, it is important to build a model of the reporter system to assist in interpreting the data. See the paper describing the development of KTR reporters by Regot et al. (pmid: 24949979) for an excellent example of how this is done and why it is so useful.

There are several other concerns regarding the technology, especially its apparent lack of sensitivity. Maximal biological response to activated EGFR is typically achieved with only a couple thousand occupied receptors per cell (pmid: 29268862; pmid: 27405981). Is this detectable? The results of the HEK293 experiments suggest that this is the case. However, instead of editing those cells, it would be informative to try MCF10A cells, which have hundreds of thousands of endogenous receptors. This could be a very powerful system, especially considering all the live cell imaging studies that have used those cells for understanding EGFR signal transduction.

The use of FRAP is advised to establish the number of pools for the fluorescent reporters and their exchange rates.

Technical on videos:

1. Titles don't agree with supplementary text

2. Text in videos obscured by QuickTime title bar

Reviewer #3 (Recommendations for the authors):

I have no specific recommendations for these authors. I felt the paper was clearly written, the experiments were well described, and the methods were extremely detailed.

I feel this paper is well-suited for publication and should be accepted in its present form.
