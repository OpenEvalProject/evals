# Peer review - Round 1

Editors:
- Lawrence Cohen, Yale United States

Reviewers:
- Bill Ross, New York Medical College United States
- Leslie M Loew, University of Connecticut School of Medicine United States
- Bradley Baker, Korea Institute of Science and Technology Republic of Korea

## Review text

DOI: [10.7554/eLife.44522.039](https://doi.org/10.7554/eLife.44522.039)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Optical determination of absolute membrane potential" for consideration by eLife. Your article has been reviewed by four peer reviewers and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Bill Ross (Reviewer #1); Leslie M Loew (Reviewer #2); Bradley Baker (Reviewer #3).

We concluded that it was a potentially interesting and useful method and recommend "revise". We ask that you respond to all of the individual reviewers suggestions and criticisms as well as the items below.

We ask that you carry out additional experiments to compare your method with the method published previously by the Leslie Loew laboratory. In one cell type, determine whether your dye and FLIM give a better estimate of membrane potential than ratio imaging and wide-field imaging with the Les Loew dye.

Lastly, we ask that you be more circumspect in advertising the method. The title, "Optical determination of absolute membrane potential", and wording in the text imply that the method will have millivolt accuracy for every cell and every cell type. The results in the paper do not support such a claim. In addition, the limitations of the method should be more explicitly addressed in the Discussion section. Will the method break down for long recordings because the dye gets internalized? There is a claim that the FLIM measurement is sensitive only to membrane potential, but if you would like to state this you would have to test other variables such as temperature, membrane lipid composition, ion concentration, age of cultured cells etc.

Reviewer #1:

This paper describes measurements of membrane potential using FLIM of a class of fluorescent molecules previously shown to respond well to voltage via a PeT mechanism. FLIM of these molecules is much more sensitive to membrane potential changes and more accurately calibrated than similar measurements on GEVIs. The authors show how they calibrate these signals, how they can be used to assay the resting membrane potentials of large numbers of cells, and demonstrate one particular application of this technique to analyze the effect of EGF stimulation of human carcinoma cells. They suggest that this technique could have wide application in situations where it would be helpful to assay slow changes of membrane potential in many cells at the same time.

The measurements appear to be carefully done. I have only a few questions.

1) The paper suggests that all the measurements are made from the surface membrane of the cell, but they do not demonstrate this point. When they calibrate the changes in single cells using voltage clamp, they certainly only record the surface membrane signals. This is partly why the signals are so linear with little difference from cell to cell. But when they look at the resting potential, they cannot be sure there is no signal from internal compartments. They say that, "the vast majority of the fluorescence signal is voltage-sensitive and at the membrane." The confocal images support this claim. But there are no numbers, and confocal images will exaggerate the contribution of surface fluorescence. Since mitochondria and other internal compartments have membranes with different potentials, their contributions must be shown to be small.

2) They claim that the variation from cell to cell is about 20 mV. This appears to be an RMSD evaluation. Figure 1I seems to show that the variation from cell to cell is about 40 mV. These two numbers may be consistent, but in many cases the 40 mV range may the important one to consider. Physiological variations in membrane potential are usually much less than that amount.

Reviewer #2:

Overall, this is a careful and thorough study and could have practical applications for screening membrane potential in cell-based assays.

The novelty of this work is diminished, however, since Adam Cohen's lab has already published 2 papers (Hou, Venkatachalam and Cohen, 2014; Brinks, Klein and Cohen, 2015) showing that absolute membrane potential could be measured via time domain recordings. Some comparisons (subsection “VoltageFluor Fluorescence Lifetime Varies Linearly with Membrane Potential”) are made to CAESR from Brinks et al. (2015), which used 2-photon excited fluorescence lifetime measurements to determine absolute membrane potential with lower accuracy than in the current study.

Hou, Venkatachalam and Cohen (2014) reports on 1-photon time-domain measurements of Arch(D95H) and is not fully considered here. There, they report very little cell to cell variation and a sensitivity of a factor of 2 per 100 mV with accuracy of ~10 mV. These measurements are not of fluorescence lifetimes, but rather of voltage-dependent fast photochemical kinetics. Still, this Cohen paper does also show how time domain measurements can allow determination of absolute membrane potential with good accuracy and little cell to cell variability. So together these 2 older papers diminish the novelty of this report.

In subsection “Optical Determination of Resting Membrane Potential Distributions” the authors report ranges of Vmem at rest and in the presence of high K+. They refer to the calculations using the HGK equation to justify these ranges. However, in the Materials and Methods section, the authors acknowledge that they don't know the appropriate parameters needed by the HGK equation for these cells. Instead, they calculate the HGK equations with many combinations of parameters and claim that the resultant calculated range of values spans the measured range of values. But these ranges are so broad that any cell line would probably fit and really don't prove anything about the validity or accuracy of these resting potential estimates. We are also left with the open question of whether these variations are really due to differences in resting transmembrane potential or some other factor that could alter the lifetime, such as the membrane dipole potential. My lab showed many years ago that dual wavelength ratio imaging of electrochromic VSDs could be used to measure resting potential in single cells (Zhang et al., 1998). But there were some cell to cell differences and even differences in ratio within a single cell that could be attributed to membrane dipole potentials (see: Bedlack et al., 1994; Gross, Bedlack Jr and Loew, 1994). Dipole potentials arise from the particular lipid composition of the membrane and therefore can vary from cell line to cell line or along the surface of a differentiated neuron. I don't see any reason that the PeT mechanism used by VF2.1.Cl wouldn't also be sensitive to the electric field produced by the dipole potential. This could all be checked by doing current clamp measurements of resting potential in the same cell that you measure the fluorescence lifetime.

Exposing the cells to high K+ is likely to cause irreversible damage and any assumptions about specific levels of depolarization would be suspect. This might compromise the interpretation of several experiments.

Reviewer #3:

I have reviewed the manuscript, “Optical determination of absolute membrane potential”, where the authors employ fluorescent lifetime measurements (FLIM) to quantify membrane potential using a voltage sensing dye. This report is a major improvement over a previous attempt to use FLIM with a genetically encoded voltage indicator. While the information gained by optically measuring membrane potential in response to treatment with EGF shows the power of this technique, I have several concerns that should be addressed before I can completely support publication.

The last paragraph of the Introduction states that this approach can be used in a range of biological contexts. The most glaring concern is what is not in this report. There are no recordings of membrane potential from excitable cells. Why? I see from Figure 1—figure supplement 1 the temporal time scale is in seconds. Is this the problem with recording from neurons? If so, please state this in the main text. If not, please state why.

The last paragraph of the Introduction states a 20-fold improvement in accuracy over previous optical methods yet there is no direct comparison in the manuscript. Please move the CAESR data from the supplementary material (Figure 1—figure supplement 5) into Figure 1. Subsection “VoltageFluor Fluorescence Lifetime Varies Linearly with Membrane Potential” also compares VF2.1.Cl to the genetically encoded voltage indicator giving another reason to include the CAESR data into Figure 1.

In Figure 1G there is a significant range of lifetime measurements in a single cell for the +40 mV membrane potential but it is uniform at +80 mV. Why is that? Is this a common occurrence? I noticed the same thing in the CAESR paper which I contributed to the probe not really working. Perhaps this is a function of lifetime imaging? Or the binning protocol? I think it would also be helpful to have Scheme 2 be Figure 1 to show how the measurement is made and change current Figure 1 to Figure 2.

In subsection “VoltageFluor Fluorescence Lifetime Varies Linearly with Membrane Potential” the authors state that the fractional change in τ(22.4 +/- 0.4%) is in good agreement with the ∆F/F value of 27%. Am I to infer from this that the ∆F/F value is due primarily to a change in lifetime fluorescence? If so, why not use ∆F/F to quantitate membrane potential?

In subsection “VoltageFluor Fluorescence Lifetime Varies Linearly with Membrane Potential” the resolution of membrane potential for a cell is estimated at 4 mV for intra-cellular measurements and 20 mV between different cells. Figure 1H and I show that the slope is more consistent than the absolute value of Lifetime fluorescence. However, this claim is important and should be demonstrated experimentally. Please add a supplementary figure showing 4 mV steps effect on lifetime measurements.

Subsection “VoltageFluor Fluorescence Lifetime Varies Linearly with Membrane Potential” states a resolution of 390 mV. That number does not make sense. Is it supposed to be 39 mV?

Subsection “Evaluation of VF-FLIM across Cell Lines and Culture Conditions” states that despite the variances shown in Figure 2A, all cell lines' membrane potential can be resolved at or under 5 mV. Please show this for CHO cells since it has the most varied slope and MCF-7 cells which showed the highest variance for 0 mV measurement.

Reviewer #4:

I felt that the paper promises more than was delivered. The paper claims to have developed "a new method for optically quantifying absolute membrane potential in living cells.....with single cell resolution".

Figure 2I shows that the fluorescence is not a measure of the absolute voltage but that each cell has a different FLIM vs. voltage curve. Thus, calibration with an electrode is needed. Furthermore, the cell to cell differences are not the same from one cell type to another; MCF-7 cells displayed greater variability than other cell lines tested (Figure 2B). Thus, calibration for a new cell type will need to include measuring the FLIM vs. voltage response from many cells.

Many images show blobs (Figure 1E and F, Figure 2C, Figure 3, Figure 4, Figure 5B). Sometimes the blobs seem voltage dependent, sometimes not. I would presume that the blobs are the result of non-specific staining. This subject was not discussed. Were the presented images selected for relatively good membrane staining?

In Figure 4A and Figure 5B different parts of the cell membrane appear to have different voltage responses and these response differences do not seem to be stochastic. This result does not fit with expected membrane voltage uniformity for small cells.

Drawbacks of the method are not discussed. The time resolution seems relatively slow. Will the method will be applicable to preparations with substantial light scattering? How will it work in three dimensional preparations? The differences from cell type to cell type will require calibration for each cell type and perhaps for each developmental age of each cell type.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Optical estimation of absolute membrane potential using fluorescence lifetime imaging" for further consideration at eLife. Your revised article has been favorably evaluated by Richard Aldrich (Senior Editor), and Lawrence Cohen (Reviewing Editor), and three other reviewers. The following reviewer has agreed to share their identity: Leslie M Loew (Reviewer #2).

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Reviewer #1:

I am satisfied with the revision.

Reviewer #2:

The authors have significantly revised and thereby strengthened the paper. In particular, they did scale back on some of the over-enthusiastic claims for their method. They also did a good job comparing their method to previous lifetime-based and dual wavelength ratio-based approaches. The new method with the VF dyes is indeed more sensitive and seems to have less cell to cell variability for estimating absolute Vmem. I appreciate the clearer explanation of how the GHK equation was used to understand the high K+ experiments. I still would have preferred some current clamp electrophysiology experiments to validate the resting potential determinations, but this is not essential. There are still 2 areas related to my own previous work where there is need for some clarification:

1) In comparing the ratiometric electrochromic dyes in the Introduction, they state: "Although they benefit from simpler loading procedures, signals from electrochromic styryl dyes display a strong dependence on local membrane properties other than transmembrane potential, reducing the accuracy of Vmem determinations (Gross et al., 1994; Montana et al., 1989; Zhang et al., 1998)". This is correct when examining different cell lines or cells in different states of differentiation, where the lipid composition, for example, can affect the ratio. But saying this in the Introduction appears to suggest that the new method that is about to be described does not have this problem; it likely does and even shows differences within the same cell line. And, actually, examination of Figure 2 in Zhang et al. (1998) shows that the cell to cell variation for the normalized ratiometric approach is remarkably small for the 40 cells examined. Figure 4 in Zhang et al. (1998) shows remarkably little variation in Vrest for undifferentiated neuroblastoma cells; the small variation in Vrest for differentiated cells, may be attributed to different degrees of differentiation.

2) In discussing the influence of membrane dipole potential, the authors misunderstand some of the studies from my lab, subsection “Resolution of VF-FLIM: Voltage, Space, and Time”:

"Relative to di-8-ANEPPS, where this effect was documented (Gross et al., 1994; Zhang et al., 1998), VF-FLIM displays less cell to cell variability, suggesting reduced dependence on the membrane dipole potential. The reason for this is unclear, as both sensors putatively detect Vmem from within the plasma membrane (Loew et al., 1979; Miller et al., 2012)." Our studies deliberately sought to establish the sensitivity of d-8-ANEPPS to dipole potential by systematically measuring ratios with different lipid compositions in lipid vesicles and by adding or depleting cholesterol in cell membranes. As a side benefit, these studies showed that membrane composition had to be considered when using dual wavelength ratio measurements to determine absolute Vmem. Until the authors do a deliberate investigation of this effect on FLIM of their probes, I don't think they can say that FLIM of the VF dyes is less sensitive to membrane composition.

Reviewer #3:

No further major comments.

Reviewer #4:

The revision is greatly improved. However, there are several areas where the paper remains overstated.

In the Abstract add the words "in culture" after the words "single cell resolution".

The first paragraph of the Introduction leads the reader to think that the paper is about signals that can be measured rapidly and can be measured in complex tissues even though the reported measurements have a time resolution that is ~four orders of magnitude slower than presently available from other methods and the measurements are only from single cells in culture. This needs toning down. The timing issue would be clearer for the reader if the table in subsection "Acquisition Time and Effective Pixel Size in Lifetime Data”" was in the main body of the paper.

A discussion of the difficulties of applying this method to other applications should be added to the Discussion section.

The Discussion section notes that faster apparatus is available. How much faster? One order?

Please discuss the possible explanations for "between regions" in the following sentence in the Discussion section: "Intriguingly, there are differences in lifetime within some cells in VF-FLIM images, both at the pixel to pixel level and between regions of the cell membrane."
