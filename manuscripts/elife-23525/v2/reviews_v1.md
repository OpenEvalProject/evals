# Peer review - Round 1

Editors:
- Christian Rosenmund, Charité-Universitätsmedizin Berlin , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23525.014](https://doi.org/10.7554/eLife.23525.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Fluorescence Lifetime Imaging Microscopy reveals rerouting of SNARE trafficking driving dendritic cell activation" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The manuscript by Verboogen et al. utilizes FRET-FLIM to study SNARE complex formation in dendritic cells and the role of VAMP3 and syntaxin 4 in LPS induced IL-6 release. Dynamic complexes formed between VAMP3 and Stx4 or Stx3 at the cell surface and VAMP8 complexes at intracellular sites are revealed. Finally the study concludes that LPS activation causes a switch to preferential formation of Stx4-VAMP3 complexes at the cell surface, which in turn support secretion of the IL-6 cytokine. This conclusion is novel in dendritic cells, in keeping with the functions of SNAREs in other immune cell types, but here it is reached on the basis of a single approach – albeit very elegant FLIM-FRET. The method that allows quantitative visualization of SNARE complexes with subcellular resolution is an important step forward. Overall the manuscript is interesting and the text well written. The figures are well presented and establish the approach (Figures 1–4) before addressing IL-6 exocytosis (Figure 5). There are several concerns that preclude publication in its current stage:

Figure 1. Authors state that there is decreased lifetime at the plasma membrane but do not attempt to quantify the difference. To make this statement (subsection 2SNAREs interactions in live cells visualized by FLIM”, second paragraph) they would need to quantify the lifetime at both the plasma membrane and the appropriate internal compartments across multiple examples.

In Figure 1 the authors note that Stx3-mCitrine localised to the plasma membrane and intracellular compartments. VAMP3-mCherry also located to the plasma membrane and predominantly in intracellular compartments. However, Stx3-mCitrine-mCherry appeared on the plasma membrane (mCitrine channel) and intracellular compartments (mCherry channel). Two concerns were raised. First, is the apparent localization of the VAMP down to the mCherry fusion? For example, all images in the mCherry channel in the manuscript show this accumulation. Second, numerous papers have used C-terminal fusions to VAMP proteins (e.g. pHlourins) and noted significant accumulation on the plasma membrane not observed for endogenous unfused VAMP. How does this mis-targetting impact the conclusions of the manuscript for example preferential pairing in the plasma membrane?

Figure 1C – The authors point out that the tandem dimer of mCitrine and mCherry does not 100% co-localize. They suggest that there might be differences in maturation. Another explanation is that the experimental design is not appropriate to measure FLIM at internal compartments such as lysosomes. As Vamp8-Syntaxin interaction is most likely at the late endosome/lysosome there will be a significant amount of quenching/degradation of mCitrine as compared to the relatively stable mCherry fluorophore that survives in the lysosomal compartment.

In Figure 2 FLIM is used by fitting a single decay to the entire image. The authors should show actual photon count numbers rather than normalized to 100%. This provides a clearer interpretation of this data for the reader. As shown in Figure 1C FRET lifetime is non-uniform in the cell. The authors should therefore use either a pixel by pixel fitting for all data with a bi-exponential decay or at least a bi-exponential fit to the whole cell data. The example data in Figure 2—figure supplement 1 shows that the fit is deviating at short lifetimes in the residuals.

Also, the authors note the large spread of lifetimes observed. Excluding the fitting issue above this is most likely due to the proportion of pixels reporting lifetime at the periphery versus the intracellular space. How was the imaging plane in the cell standardized? The authors suggest expression level as a potential issue, however, the number of plotted points in Figure 2D/2F does not match the number of points in 2C. If concentration is the answer this would be better proved by using all data in 2C and examining correlation or using bi-exponential fits and examining amplitudes and lifetimes (preferably without fixing the short lifetime as it may not be the same as the positive control state).

Figures 4 and 5 state that cells were used from 'at least 4 donors' or '3 donors' (were these donor numbers used as 'n' values for statistical purposes?). However, the cells appear to have been pooled to conduct the experiments instead of cells from each donor being measured separately. This would simply be a single mixed population rather than providing statistical replicates. If the authors have the separate data from each donor they need to include this and reassess their results.

In the text associated with Figure 4B the authors state "The interaction between Stx3-mCitrine and VAMP3-mCherry was stronger than for all other tested SNARE pairs". By stronger I presume they mean a shorter mean lifetime. However, this is misleading. The FRET energy transfer reported by the mono-exponential whole cell fit is a conflation of proportion of interacting molecules, proximity and dipole orientation averaged over the whole cell. The only conclusion that can be drawn is that the lifetime has changed. This issue also impacts on the subsection “Comparison of different SNAREs involved in exocytosis”, the Discussion and Abstract wherever the lifetime value is interpreted as a specific change in strength/number of interactions.

Figure 5: Given that FLIM is best suited to live cell imaging, Could the authors not show changes in FLIM in the same cell post LPS? This would give greater confidence in the observed changes pre- and post-LPS. In fact, it is not clear whether the study has used live or fixed cells, this needs to be stipulated in the methods.

Is Figure 5—figure supplement 1B endogenous or expressed isoform expression levels? There are no MW markers or text to indicate either way. Methods do not state if cells were transfected. As the experiment it controls for is examining over-expressed proteins this should be looking at over-expression level.

6) The IL-6 secretion data in Figure 5D is not very convincing in its current format. The experimental details need to be clarified (is this a 16 hour treatment with LPS followed by collection times of 4-24 hours (with or without LPS?) Secondly, the cytokine levels are currently expressed as percent of maximum. This is unconventional and does not convey direct information about the amount of cytokine secretion over the time course. Since the ELISA assay gives direct cytokine amounts, this is how the data should be conveyed (e.g. ng/ml) and ideally for each of the 3 donor cell lines +/- VAMP3.
