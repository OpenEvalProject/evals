# Peer review - Round 1

Editors:
- Robert H Singer, Albert Einstein College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55963.sa1](https://doi.org/10.7554/eLife.55963.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The requirements for nuclear transport can be recapitulated by a simple two-parameter biophysical model that correlates the import flux with the energetics of cargo transport through the nuclear pore complex. Together, the results reveal key molecular determinants of large cargo nuclear import in cells.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Molecular determinants of large cargo transport into the nucleus" for consideration by eLife. Your article has been reviewed by a Reviewing Editor and a Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

While the reviewers felt the work had merit, they had several concerns about the interpretation of the data, the limitations of the experiments and the relevance to living cells. Their concerns might be addressed by further experiments but in its present state we feel the manuscript has too many issues to address within a few months. Hopefully their comments will be helpful in improving your manuscript. When you have addressed the concerns, we could consider it for eLife, as a new manuscript.

Reviewer #1:

Compared with typical/average-sized nuclear transport cargos, there are little data on the transport rates of large cargos by nuclear pore complexes (NPCs). The authors examined the suitability and transport rates of a series of 5 viral particle capsids of different sizes and with different numbers of NLSs. They conclude that 10 or more NLSs are required for import for the cargos examined, and that the number of NLSs per cargo volume is a better variable than NLSs per cargo surface area for predicting the amount of nuclear uptake. While these are interesting and potentially useful quantitative results, there are significant issues with the results, interpretation and details provided, which tempers my enthusiasm.

Of the 5 viral particle capsids described, the authors had technical difficulties with the two largest, and therefore these were not included in the analysis. Thus, their abstract is misleading as they do not report kinetics for the size range of 17-36 nm, but rather 17-27 nm. The problems with the two largest capsids should be moved to a supplementary section so as not to distract from the main work. In addition, the MS2 cargo is so poorly imported that it does not make sense to use it to draw major conclusions. For example, the slope for MS2 in Figure 5A is so flat that it is impossible to reliably conclude a minimum number of NLSs. The remaining cargos are not well behaved in terms of transport kinetics, as described in more detail below.

The NLSs are randomly attached to the capsid surfaces, making the resultant populations heterogeneous. The quantified number of NLSs is an average, and gel analysis is semi-quantitative. Some discussion of their expected errors is warranted.

The only biologically relevant capsid (HBV) – i.e., one that is imported into the nucleus – is not included in their analysis. Physiologically, this capsid disassembles in the nuclear basket. They have deleted the authentic NLS for their experiments. Thus, the biological implications are limited.

In Figure 1D, are the curves actual data or fits? FCS and DLS signals will be dominated by the large particles, yet free dye and/or labeled capsid monomers can significantly influence the import curves – are these responsible for the non-zero ordinate intercepts in Figure 3—figure supplement 1? Can the labeled capsids be separated from monomers and free dye by size exclusion chromatography?

The authors discount the importance of surface properties at numerous locations throughout the text. But they have not actually tested this, and surface properties are in fact surprisingly important, as multiple studies have shown – changing a few residues or adding fluorescent dyes can dramatically change the import properties of cargos. In fact, I would not be surprised if varying the number of dyes on their cargos would alter the slopes of the plots in Figure 5, or some of the scatter in these plots arises from the dye:cargo:NLS ratio. Minimally, they should tone down their discussion arguing against a minimal influence of surface properties.

While the authors limit the fitting "to the first 40 minutes to extract more accurate kinetics", the opposite is in fact true. Accurate fitting of exponential kinetics requires knowing the asymptotic limit, which is not the case for numerous curves in Figure 3 -figure supplement 1. Also, initial time points in these curves vary widely – this is not expected or discussed.

For 80 min time points, the authors should really consider including CAS, RanGAP and RanBP1 to maintain complete recycling of transport factors.

"Normalized nuclear intensity" needs some explanation. Relative to what? Do these correspond to the same scale for different plots. What does an intensity of 1 signify? How does this relate to the intensity in Figure 1D? The efficiency of nuclear uptake of the different cargos varies widely, but this is not discussed.

The energetic discussion in the last paragraph has little meaning without an estimate of the entropic cost of displacing the permeability barrier.

Reviewer #2:

The manuscript by Paci and Lemke describes experiments addressing nuclear accumulation of large NLS-labeled cargoes. The effort is commendable and the use of modified viral capsids is admirably clever. However, I have some serious problems with the interpretation.

The experiments are based on permeabilized cell assays. These are standard in the field, for better or worse, but they suffer a generic problem in that the rest of the cell is washed away. In a live cell, the transport substrate of interest has to compete with the rest of the proteome for attentions of the transport receptors. This can have a dramatic effect on the transport kinetics.

Like most studies of nuclear accumulation, the analysis does not distinguish properly between permeability of the nuclear envelope and the saturating level of nuclear concentration. The latter is recognized as "robust nuclear import" but depends, quite obviously, on the RanGTP system. The assumption that monoexponential (first-order) kinetics measure permeability through the nuclear pores is simply not justified. The observed kinetics reflect the rate-limiting step, which may be Ran recharging with GTP or recycling to the cytoplasm. See Kim and Elbaum, 2013, and much earlier Smith et al., 2002.

Quantitative measurements of nuclear accumulation can be affected in addition by binding to structures within the nucleus, as suggested by the images in Figure 3 for MS2 with high NLS count. Each NLS adds a considerable amount of positive charge. This may well affect binding to nucleic acids when present in such high local concentration on the viral capsid, especially if DNA/RNA binding proteins are lost in the permeabilization.

The text deals with the level of nuclear accumulation ("endpoint" in Figure 5), but the graphs presented show the accumulation kinetics rather than the saturation as a function of #NLS. The time for half-saturation, (I(t) – A)/Imax = 1/2, is actually ln2/k, not ln2/Imax as written in the text (subsection “Image and data analysis”). Looking at the table in Supplementary file 1, the values for T_1/2 are listed equal to 1/2 * ln2/k. This has the correct units but I don't understand the factor of 1/2.

If the aim of the exercise is to study the degree of accumulation, i.e., Imax, then the proper parameter to measure is the saturating nuclear to cytoplasmic ratio N:C. The logarithm of this ratio is the chemical potential difference, which is the essential thermodynamic quantity. As presented, the data do not show the cytoplasmic intensity and the background correction that was applied is not described. Figure 2C shows a single example of the cytoplasmic intensity where the nuclear to cytoplasmic ratio saturates at about 10 (700 / 70 units on the graph).

Since the fluorescence external to the cells coming from titrated cargo substrates should equilibrate with the fluorescence in the cytoplasm, I looked to see if this might be included in the fitting parameter A. It was not clear whether A is the background correction itself or a fit after the correction is applied. In any case A cannot represent the fluorescence from free cargo. According to the text these are introduced at a constant 8 nM concentration, but the values listed in the supplementary file vary widely, even for a given class of cargo. Why should they vary so widely? Presumably these values are corrected by the same factor as Imax for the substrate brightness. If they are not corrected, shouldn't the capsids with fewer NLS appear brighter, so with larger A? In some cases A is a very large fraction of Imax, leaving little dynamic range for the measurement itself. (Compare I53-47 with 15, 18, and 22 NLS.) In principle the black level to subtract is that of the confocal microscope with the laser blocked, and the fluorescence in the surrounding medium should match that measured in the permeabilized cytoplasm. If the cells are auto-fluorescent in the measurement channel then some additional correction will be required, but it should be specified clearly.

A few relatively technical points:

Why was the labeling with fluorescent dye and NLS done both on cysteine? The proteins could have been labeled first on lysine and then with NLS on the cysteine. The problem is that the molecular weight of the dye is almost half that of the peptide. Is a control available to show that the dye labeling really has no effect on the gel mobility? Figure 1—figure supplement 1 shows both Coomassie and fluorescence in the "unsuccessful" labeling of I53-50. For clarity, the main figure should also show the fluorescence in the successful case.

I did not understand the toy model in subsection “Global quantitative analysis of nuclear import in relation to cargo size and #NLSs”. The binding energy of NTRs to the cargo does not assist in directional translocation, nor is it transferred to displacing the FG repeats. That depends on interactions of NTRs with FG motifs. Crowding in the nuclear pore as shown in Figure 5 is interesting and might relate to kinetics, but not to the saturating concentration ("endpoint").

Nuclear export is not just the inverse of import. See Kim and Elbaum, 2013. There is a fundamental difference between exchange of RanGTP, a reversible reaction in "import", and physiologically irreversible GTP hydrolysis, which is coupled to translocation in "export".

The manuscript is long for a short report, about 3500 words in the main text alone.

Hoping to end on a constructive note, I have to apologize for being such an ornery reviewer here. I do quite like the experiment and I believe the data hold some new truths to be discovered. Wherever the work is ultimately published, I would like very much to see the nuclear accumulation presented as the nuclear to cytoplasmic ratio. This will normalize inherently for substrate brightness and avoid potential inconsistencies carried in by numbers from other measurements, imprecise dilutions, protein losses in aggregation, etc. Surely the data are available without requiring any further experiments. I am sure they could be reanalysed easily, avoiding confusion between kinetics and saturation. Plotting the ratio will clarify whether the additional number of NLS indeed influence the kinetics and saturation as suggested. There might be surprises in store.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Molecular determinants of large cargo transport into the nucleus" for consideration by eLife. Your article has been reviewed by the original reviewer, and the evaluation has been overseen by a Reviewing Editor and Suzanne Pfeffer as the Senior Editor. The reviewer has opted to remain anonymous.

The Editors have discussed the review with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

One of the original reviewers feels the manuscript has been improved but has some issues with the interpretation of the data, and the model. Specifically, the reviewer states "Particular attention must be made to predictions of the model, and interpretations in the context of this model." This reviewer has been thorough in the evaluation, so we feel the comments may likely be helpful in improving the manuscript further.

Because the concerns can be answered without additional data, but only require revisions to the manuscript, or explanations for the reviewer, we opt to send it back to you to address these comments.

Reviewer 1:

This revised manuscript has been substantially improved by tightening up the discussion and presentation to focus on the main story, and with the addition of a mathematical model. However, I do have some concerns about the revised manuscript, listed below in order of importance. While some of these points address accuracy and a logical consistency, other portions are intended to promote a more nuanced and informative picture. Particular attention must be made to predictions of the model, and interpretations in the context of this model.

1) Figure 5B – The model impressively explains the values in the graph. However, all of the ∆G values are positive, suggesting that binding to the permeability barrier is unfavorable. Nonetheless, nuclear rimming is clearly seen during the import experiments, indicating that interaction with the pore is favorable – more favorable than being in the cytoplasmic compartment. This indicates that the NPC is a thermodynamic sink. The data thus seem incongruent with the model, which only postulates an energy barrier. The model in Figure 5—figure supplement 4 is reminiscent of the vestibule model of Tu et al., 2013), yet here too, none of the ∆G values are negative (which was the case in Tu et al.,). Please discuss.

2) They cite four references for the initial flux equation (2, 33-35). I cannot find the equation they use in these references. In fact, two of them describe flux in terms of a constant multiplied by a concentration difference, which seems inconsistent with their equation. More discussion is necessary to elucidate where the model comes from.

3) If I understand the methods correctly, the NLSs and dyes were simultaneously mixed with the capsids. They discuss tuning the NLS/capsid ratio, and this is ultimately determined via a gel shift assay. But what about the number of dyes per capsid? It seems like they have brightness data from FCS experiments, and this should be reported. Do the number of dyes vary inversely with the number of NLSs? They continue to minimize the role of surface properties, yet a few extra dye molecules were shown by Tu et al., to dramatically affect the permeability properties of the cargo. I do not consider it safe to assume that the number of dye molecules does not influence the particle's interaction strength with the NPC. Moreover, they state that F(R) scales with the radius, yet the values for F(R) that they obtain are all essentially the same, which would be consistent with different surface properties of the different diameter capsids. Stating this does not diminish their results.

4) The epsilon values are surprisingly small. For the cargo of Tu et al., this would predict a very small interaction strength of the fully decorated cargo, and even smaller for a single NTR-bound cargo, which nonetheless still clearly binds to the pore. Note that the size (volume occupied) of β-galactosidase is less than MS2(S37P) by a similar ratio that the MS2(S37P) size is less than I53-47. It would be quite surprising indeed if the substantial behavioral differences of the β-galactosidase and MS2(S37P) cargos can be ascribed to the size and shape differences alone. It seems that surface properties must at least somewhat contribute to the observed differences.

5) Discussion section – I do not understand these surface coverage calculations. For maximum NLSs of 38, 35, and 98 for MS2(S37P), I53-47, and MS2, I get 84%, 42%, and 85% surface coverage assuming 20 nm2/β. This does not include Importin α. How much do the diameters increase assuming a full coat of Importins α and β? This is expected to be significant. How does this increased diameter compare with the size of the channel? Is there any experimental evidence that all NLSs on the capsids are bound to NTRs? Taking into account that concentrations and the Kd (~40 nM, α for NLS) are similar, the NLSs on the MS2 capsid are only about 90% occupied, implying 77% surface coverage. While these changes may not materially change their interpretation, a more detailed discussion is necessary to build an accurate picture and to build confidence in the conclusions. Other potential complications: (1) is it possible geometrically for all NTRs on a capsid to be bound to FG repeats? Figure 5A suggests that this may not be possible; and (2) can multiple capsids simultaneously bind to a single pore? Excess cargo, slow import and nuclear rimming suggest this possibility. Would this affect interpretation?

6) It is unclear whether there is any meaning behind the A values. These are highly variable, and I don't know what to make of them. In principle, A could reflect the accumulation of the cargos on the nuclear envelope, but as this arises from an extrapolation to zero time, it seems like this should in fact be zero, or at least some reasonably explained value. One possibility is that import rate could be dependent on the amount of accumulated cargo at the pores, i.e., a release rate, as entrance into the NPCs appears really fast.

7) The data on negatively charged linkers is inconclusive at best, as they are highly scattered. Their conclusions should be toned down.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Molecular determinants of large cargo transport into the nucleus" for further consideration by eLife. Your revised article has been evaluated by Suzanne Pfeffer (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

One reviewer feels the manuscript is substantially improved but there remains an outstanding issue that has not been corrected in the revision. The reviewer feels that Figure 5—figure supplement 4 needs to be clarified as described below. Additional minor comments directed at improving the manuscript are included as well. Please send a revised manuscript that addresses these comments sufficiently that it may not need to go back to this reviewer.

This revised manuscript has been substantially improved, with a much more balanced and informed discussion. All of my major concerns have been adequately addressed, with the exception of one item, the model in Figure 5—figure supplement 4. The figure itself is confusing/unclear, and I do not understand the basis behind building the model the way they did. Specific concerns for this figure are as follows:

1) What is the y-axis in the top panel of 'A'? This should be marked. My guess is that this is some measure of 'FG-Nup density' – are there any relevant units?

2) The dimensions of L1 and L0 do not reflect the values in the caption. Consequently, the diagram is misleading. The Greek letter is inconsistent with the caption. The vestibule region is not marked.

3) It is unclear why a transition region (L1) is included between the vestibule and L0. Comparing the top and bottom panels in A, it appears that the vestibule is equivalent to the cytoplasm. This does not make sense.

4) For L1 = 30 nm and L0 = 5 nm, the first impression is that the barrier gate is biased toward the nucleoplasmic side. Is this the intention? Such a model would be consistent with the nucleoplasmic gate hypothesized by the Weis group, and, if so, should be mentioned. Alternatively, are both the cytoplasmic and nucleoplasmic L1 regions both 30 nm? This would place the barrier in the center, but very narrow. It doesn't make much sense for a 'transition region' to be 6 times the width of the main barrier, so some discussion is needed here.

5) It is unclear why the ΔG for the L1 region changes substantially for the different viral particles, yet the ΔG for the L0 region changes minimally. It seems that the ΔG for the more dense FG nup environment would be more sensitive to particle size. An older hypothesis suggested dense clouds on the nucleoplasmic and cytoplasmic sides, but significantly lower density within the center. Is this being considered here?

6) The authors are correct in their rebuttal that only a portion of the NPC needs to contain a region where the interaction free energy is negative, in order to be consistent with the experimental observation of rimming. However, none of the regions illustrated in Figure 5—figure supplement 4 have negative ΔG. There is a dashed region that is apparently of negative free energy, but what this is remains unclear (point 3), and it is not clear if this energy is included in any way in their fit to the data.

7) In the lower panel of B, the green curve fit approximates the data very poorly, but does much better in the upper panel. Something seems amiss here.
