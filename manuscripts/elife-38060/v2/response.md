# Author response - Round 1

Authors:
- Yu Zhou ([ORCID: 0000-0002-1623-7948](https://orcid.org/0000-0002-1623-7948))
- Xiao-Ming Xia
- Christopher J Lingle

## Response text

DOI: [10.7554/eLife.38060.012](https://doi.org/10.7554/eLife.38060.012)

Reviewer #1:

[…] There are two areas that the manuscript/study need to be revised.

First, throughout the study, the authors need to specify how many observations contributed to the results presented. When appropriate, the authors need to specify what each error/variability number represents (e.g., SD, SEM, confidence interval).

The number of experiments for each data point is added to corresponding plots. Information about variability of measurement and uncertainty of curve fitting is added to the Materials and methods subsection “Data analysis”.

Second, the authors should incorporate the VSD activation mechanism information from the previous work on Kv channels. The sequence alignment indicates mSlo1 D133, D147, and D153 are equivalent to E183, E220, and D226 in Kv1.2/2.1 of Long et al. (2017). The activated and (hypothetical) closed conformations of the Kv1.2/2.1 VSD in Long et al. (2017) are quite similar to those presented in Figure 6A. Some discussions about the conserved VSD mechanisms are appropriate. Further, Hoshi and Armstrong (PDBID 22802655) suggested, based on gating and ionic current measurements, that some divalent and trivalent cations may interact with E226 in Kv1.2/2.1 (mSlo1 D153) (albeit the GV shift is considerably smaller than that presented here). Similar mechanisms may be involved in the effect of divalent cations in Kv channels and H+ in Slo1.

We added a new paragraph in the subsection “Relation to previous studies and structural implications” to discuss the relationship between previous studies on the VSD activation mechanism and our work on pH inhibition of BK channels based on this comment.

• Introduction, first paragraph. Perhaps, insert "potentially" into "[…] or even in various organelles”

Done.

• "Extracellular". Somehow qualify that the normally extracellular side is the luminal side early on.

We added several sentences in the Introduction to make it clear that the normally extracellular side is the luminal side in some organelles.

• Figure 1D. pH 4 data. Instead of scaling to the observed maximal value, it might be better to scale to the Boltzmann-fit estimated maximal value? In the current form, the max fit value is >1 and the graph probably underestimates the Vh shift.

We fit the data in Figure 1D with Gmax allowed to vary at each pHO and updated Figure 1D and its legend with the new fitting result. The new estimations of Vh and z are almost identical to the original values.

• Figure 2C. It is better not to connect the data points with straight lines.

The data points are now connected with cubic spline line.

• Results, section ‘BK channel activation is strongly inhibited at pHO lower than 5’: "[…] not the reduction in single-channel conductance." If illustrative opening records are available, the authors should show them.

Representative single channel recordings at pHO 7 and 4 are included in Figure 1—figure supplement 1.

• Results, section ‘A change in the C-O equilibrium only accounts for a small portion of the gating shift induced by extracellular H+’: "about 2-fold with" and " reduced by 2-fold are" The results seem to show that the single-channel nPo decreased by 3-fold?

Now these two sentences are changed to “L of BK channels at pHO 4 was about 1/3 of that at pHO 7” and “with L0 scaled to 1/3 of the control value” respectively.

Reviewer #2:

[…] I have only some concerns with the presentation of some of the data, plus a more moderate concern on the experiments regarding C-O equilibrium.

In Figure 1C: It's not clear how the single-channel i-V data, which is on an absolute scale, is related to the model-generated plot of fractional current. Plotting the data in this way seems to suggest that if the model were correct, then the model-generated curve should superimpose on the data, but this is not the case. One possible remedy would be to plot the experimental data as fractional current to compare it to the curve.

We put a fractional single channel current-voltage plot and corresponding Woodhull model fit in Figure 1C and provided sample traces of BK single channel current and i-V plot in Figure. 1—figure supplement 1.

For measurements aimed at quantifying the effect of pHo on C-O equilibrium:

1) In the interest of transparency, the authors should list the actual parameter values used to generate the simulated curves in Figure 2B (there are three sets of parameters listed in Horrigan and Aldrich 2002).

The parameters used for simulation are added to Figure 2 legend.

2) It is a moderate concern that the estimates of C-O equilibrium are from channel activity with 10 µM Ca at the cytosolic side of the patch, at -100 mV. Under these conditions it is very unlikely that the C-O step has been isolated from effects of voltage sensor movement. These experiments should ideally be performed in that negative Vm range with nominally 0 Ca at the cytosolic side of the patch (also, currents should be measured over a range of negative voltages to confirm that voltage sensor activation is not contributing to gating).

We attempted to measure BK limiting nPO at pHO 4 with 0 [Ca2+]in. But the openings under such conditions were too brief for us reliably determine nPO. Two previous studies (Horrigan and Aldrich, 2002; Carrasquel-Ursulaez et al., 2015) show that there is little BK VSD movement at voltages negative to -100 mV even with 70 to 100 μm [Ca2+]in. Therefore, BK VSDs should largely be in resting states at -100 mV with 10 μm [Ca2+]in. We repeated nPO measurement at three negative potentials (-100, -120 and -140 mV) with 10 μm [Ca2+]in and found that the change of nPO induced by extracellular acidification was not significantly different at these voltages. The new result is included as a new panel in Figure 2 (Figure 2B).

Introduction, "[…] whether BK channels is sensitive" should read "whether BK channels are sensitive"

Corrected.

Also "Given the possible presence of BK channels […]" should probably read "Given the presence of BK channels", unless the authors have reason to doubt their presence at these loci. Same for "Given the possibility that BK channels may be expressed".

Even though we have no direct evidence to argue against the presence of BK channels at these loci, our result does indicate that the activity of BK channels should be highly suppressed due to the extremely low extracellular pH at these loci. Therefore, we want to be cautious with these statements. Furthermore, there may be still some doubt about whether BK channels are really present in such membranes. For example, extensive proteomics of mitochondria have failed to reveal any Slo1 protein.

Reviewer #3:

[…] I do, however, have some questions and a suggestion for a point of discussion. While the apparent IC50 of inhibition at pH 3.8 does implicate acidic residues, the pH-dependence is very shallow with a hill coefficient of 0.41, such that shifts in activation are observed even at pH 7 or 6 (relative to pH 9). The mechanism underlying this shallow pH-dependence is not addressed, but is interesting because it makes the effect potentially relevant to physiological or pathophysiological pH conditions other than the extreme example of lysosomes. The shallow pH-dependence would seem to suggest either that (1) the 3 aspartic acids identified may have very different pKa's or (2) or a high pKa sensor was missed. Therefore, some relevant questions are: Do acidic residue mutations reduce the response to pH 6 as well as pH 4 (suggesting they account for the effects near physiological pH)? and, was the effect of mutating the only external histidine in hSlo (H254) tested?

Even if none of these experiments were done, I think it may be worth discussing that the broad pH-dependence could arise from D133, D147, D153 having different pKa, since this fits into the existing discussion. It is well known that the pKa of acidic residues can be altered depending on aqueous exposure and interaction with other charged residues, which the authors show are different for D133, D147, D153, and may change with voltage-sensor activation. In addition, there is previous evidence to suggest that D133 and/or D153 might have an unusually high pKa (at least in the resting state) because the effect of Cu2+ reported by Ma et al. 2008 and referenced in the discussion, was dependent on D133 and D153, but not H254, and yet exhibited a relatively high apparent pKa of 6.0.

Yes, the unusually shallow slope of the pH-dependent gating shift curve is an interesting observation, and as reviewer #3 pointed out, deserves further investigation to deepen our understanding of BK regulation by extracellular pH. For the current study, we added a new paragraph at the end of the subsection “Relation to previous studies and structural implications” to discuss the implication of such shallow slope based on reviewer #3’s comments.
