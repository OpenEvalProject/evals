# Peer review - Round 1

Editors:
- Hannes Neuweiler, University of Würzburg Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55286.sa1](https://doi.org/10.7554/eLife.55286.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Value assessment: Binding of ligands to cellular membrane receptors is fundamental to processes like cell-cell communication, signaling, and initiation of biochemical cascades. Methods that can detect and quantify such interactions are scarce. This "Tools and Resources" contribution introduces a fast variant of line-scanning fluorescence correlation spectroscopy that facilitates detection and quantification of binding of fluorescently modified ligands to their target receptors on cell membranes.

Decision letter after peer review:

Thank you for submitting your article "Precise quantification of ligand-cell surface receptor interactions using axial line-scanning FCS" for consideration by eLife. Your article has been seen by three peer reviewers, including Hannes Neuweiler as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Thorsten Wohland (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Major concerns include the novelty of the proposed methodology, estimation of equilibrium dissociation constants, additional controls, and details on data processing and analysis.

Reviewer #1:

The manuscript "Precise quantification of ligand-cell surface receptor interactions using axial line-scanning FCS" by Eckert et al. reports a modification of existing line-scanning fluorescence correlation spectroscopy (lsFCS) for improved detection and quantification of binding strengths of protein-ligand interactions on cell surfaces with live cell applicability. Eckert et al. implement a tuneable acoustic gradient index of refraction (TAG) lens in a multi-colour lsFCS setup that facilitates microsecond scanning of biological samples in axial direction. The axial scan is reported to be two orders of magnitude faster than existing lateral scanning techniques, thus alleviating complications arising from cell membrane dynamics and poor photophysical properties of fluorescent tags. The authors demonstrate the capabilities of their technique through quantitative analysis of inhibition of Wnt signalling using fluorescently modified DKK1 and DKK2 ligands that bind the Wnt co-receptor LRP6 in human lung cancer and human embryonic kidney cells. Eckert et al. test three different methods of LRP6 expression in their assays. Axial lsFCS is finally applied to investigate ternary interactions of DKK1 with the co-receptor Kremen2 and LRP6.

The elucidation of pathways of cellular signalling is a current challenge in molecular biophysics. It requires methods that can detect and quantify protein-ligand interactions in membrane receptors. Temporal analysis of fluorescence fluctuations of modified proteins involving modern multi-colour fluorescence microscopy is a promising approach. Fluorescent background, dynamics of cell membranes and changes in cell morphology, however, complicate a reliable analysis within a cellular environment. The new tool reported by Eckert et al. extends existing lsFCS to overcome such complications by rapidly scanning samples in axial direction thereby improving time resolution in correlation analysis and shortening the overall measurement time. Eckert et al. report clean binding isotherms and the associated equilibrium dissociation constants, measured by their technique, of interactions of DKK1 and DKK2 with the membrane receptors LRP6 and Kremen2. The study involves different fluorescent fusion proteins as tags and different transfection/expression techniques, testifying general applicability. The manuscript is well written. Technique, experimental data together with their analysis are clearly presented and discussed. The advantage of the axial scanning mode in live cell applications appears convincing.

However, the following points should be addressed before publication.

1) The authors report that the Kd of DKK1/LRP6 increases with increasing expression level of LRP6 (subsection “DKK1 and DKK2 binding to LRP6-mCherry”). Eckert et al. rationalize the effect by a reduced affinity of the LRP6 receptor due to packing of LRP6 in the membrane (Discussion paragraph four). But an alternative explanation would be that a significant fraction of DKK1, which is applied at nM concentrations in conditioned medium, binds to over-expressed LRP6 located at cellular sites beyond lsFCS detection. Such undetected binding events can lead to "lost" ligand and would consequently result in artificially high Kds in titration experiments.

2) The authors find similar Kds of DKK1 interactions using mCherry and tdTomato as fluorescent fusions on LRP6 and argue that the change of fluorescent reporters proves reliable and tag-independent measurement of Kds. An important additional control would be to change the tag on the ligand DKK1. eGFP fused to DKK1 may also perturb binding.

3) The authors find that overexpression of unlabelled LRP6 leads to an increase of affinity of DKK1-eGFP. The observation may report on a perturbation of DKK1 binding caused by the fluorescent fusion on LRP6. The possibility of a probe-induced artefact should be discussed.

4) Figure 3—figure supplement 1: the authors detect a decrease of time constant of DKK1-eGFP binding to HEK cells with increasing concentration of DKK1-eGFP. It would be interesting to see if the observed rate constants of binding increase linearly with increasing DKK1-eGFP concentration. This is expected for a bi-molecular reaction in solution. A linear fit to the observed concentration-dependent rate constants yields a microscopic rate constant of DKK1 binding. The microscopic rate constant of ligand-binding to a cellular receptor is interesting because such quantities are usually inferred from in-vitro kinetic experiments on isolated proteins that may not reflect the in-vivo situation.

Reviewer #2:

Nienhaus et al. present a tool for improving fluorescence correlation spectroscopy by axial line scanning using a TAG lens. In large parts the study shows systematic and rigorous experimental work with several proteins interrogated at different densities.

1) Major concern about novelty: The idea of axial scanning to improve the data quality in membrane FCS studies is not new (https://arxiv.org/pdf/1806.00070.pdf) or the work by Jonas Ries (DOI: 10.1039/b718132a). The (only) difference here is that the authors use an ultra-fast TAG lens. Unfortunately, the Introduction is misleading and makes the reader believe that axial scanning FCS is an invention by Nienhaus et al. Moreover, the impact compared to previously reported studies remains unclear.

2) Major concern about data interpretation/processing: One major concern is that it remains unclear how the authors reach the precision reported. How exactly are the data processed and how is the outcome generated? How was the FCS data analyzed? What software program was used? If self-written, why is the source code/ compiled version not provided with example data and manual?

Reviewer #3:

The article by Eckert et al. introduces a new scanning fluorescence correlation spectroscopy (FCS) modality to quantitatively measure molecular affinities of ligand-receptor systems on cell membranes. The authors perform scanning along the optical axis using a tunable lens. This preserves the advantages of lateral scanning, namely the removal of sample movement artefacts, but is much faster as axial scanning by the tunable lens can be performed at higher frequencies than the galvano-scanner based lateral scan systems, reducing measurement time. The authors demonstrate the capability of axial line-scanning FCS by measuring the interaction of various proteins of the Wnt signaling pathway, including DKK1, LRP6, xKremn2, showing that DKK1-LRP6 and Kremen-LRP6 interactions stabilize the trimeric protein complex with a weaker contribution by DKK1-xKremen2 interactions. The article introduces a new method that corrects for many possible artefacts in previous FCS approaches and provides biologically interesting and quantitative Kd values with small errors. The article is well written and convincing but needs to address some concerns:

1) The authors show almost no experimental correlation curves. Especially on cells there is only one set of curves shown in the supplement. But these curves are noisy. At this correlation function quality, how well are the fractions of the different components determined (Equations 8 and 9)? It would also be instructive to see a set of curves at different ligand concentrations.

2) Can the authors either include a positive and negative control?

3) The dissociation constants determined are very strong, below the nanomolar range. Thus the interaction is quite easy to measure and experiments can be performed at low concentrations. Nevertheless, as remarked under point 1 the curves are quite noisy and this will likely get worse at higher concentrations to measure higher Kds. It would be therefore useful if the authors could provide an estimated concentration and Kd range they think they can measure.

4) Subsection “Analysis of fast axial lsFCS on live cells”: The background signal seems to follow the intensity and is not constant as one would assume. Is this an overcorrection or do the authors assume that the background is also bleaching?

5) The authors bleach-correct their time traces. But the correction needs to conserve the variance of the signal, otherwise the amplitudes are changed by the correction. As their correction function is itself a function of time it is not evident whether their transformation fulfills this condition.

In addition, why do the autocorrelations require an extra scaling factor if the intensity traces have already been rescaled to the initial intensity I'(0)? For the cross-correlation they acknowledge that there is no re-scaling necessary. There is no explanation why the cross- should be different from the auto-correlation.

6) The authors state that as the intensities were already corrected, any correction factors would cancel. But overall with bleaching the interacting particles will decrease and that cannot be taken account of in that format. So bleaching will still decrease the cross-correlation amplitude and thus also the determined Kd. Authors might want to discuss this point.

7) The authors use pulsed laser excitation and thus can unambiguously assign photons removing cross-talk. This should result in completely flat cross-correlation functions for a negative control. However, they still have cross-talk from a red label into the green channel when excited with a green dye? This is quite surprising. Thus, a negative control to document this would be very useful.

8) As the background is different for the different wavelength channels, it will lead to different corrections in amplitude for the different correlation functions. This in general will not lead to cancellation effects. While in the authors situation the effect might have been sufficiently small it should not be neglected if axial-line scanning FCS is to be used in general. This point should be elaborated and if the authors think they can neglect background effects, then this should be shown (also note that the shift in Kd is 4 times higher than the error claimed so is not completely negligible).

9) The authors treat non-fluorescent proteins and endogenous proteins the same way. But this is not entirely correct. Cells will have a certain level of endogenous proteins. Depending on the amount of recombinant labeled protein expressed this endogenous protein will have a stronger or weaker influence. If, e.g., 80% of a fluorescent protein are fluorescent, then the measured value of non-fluorescent proteins (parameter β) will be influenced by endogenous proteins. At a high recombinant protein concentration, endogenous proteins play little role and one recovers 80% of fluorescent proteins. But at lower recombinant protein concentrations, the endogenous proteins play a much larger role and values <80% will be recovered for fluorescent proteins. Thus, β is not a constant if one measures on different cells with different recombinant protein expression levels.

10) Increase of Kd with receptor density. This could also be a result of background issues or bleaching, or of the issue with β just mentioned. A positive control at different concentrations would help clarifying the issue.

11) The simplifications constrain the technique. The authors should report how much these assumptions change their actual experimental estimates for the Kd. e.g. the assumption that GFP is 100% fluorescent is not really borne out by recent experiments that rather report 80%. Also the assumption that there are no non-fluorescent tdTomato in the dimers is not entirely justified. Reports on red fluorescent proteins being fluorescent vary between 20 to maximally 60%. Even in the best case this still would lead to 16% non-fluorescent proteins. Furthermore, tdTomato with one or two fluorophores contribute very differently to the correlation functions as the contribution depends not linearly on the brightness. So I agree that the simplifications make the data more easily treatable. But the authors should at least show once the full solution and compare the results of it to the approximation.
