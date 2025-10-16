# Peer review - Round 1

Editors:
- Mani Ramaswami, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74172.sa0](https://doi.org/10.7554/eLife.74172.sa0)

Drosophila Kenyon cells dendrites in the mushroom body calyx receive inputs from the projection neurons (PNs) in the antennal lobe. This work shows that potential variability of olfactory responses in Kenyon cell post synapses is reduced by the activity of a widely arborizing inhibitory interneuron named APL. APL also receives inputs from PNs and provides local scaled GABAergic feedback to PN-Kenyon cell synapses to normalize postsynaptic responses in the calyx.


---

# Peer review - Round 1

Editors:
- Mani Ramaswami, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74172.sa1](https://doi.org/10.7554/eLife.74172.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The anterior paired lateral neuron normalizes odour-evoked activity in the Drosophila mushroom body calyx" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Mani Ramaswami as Reviewing Editor and K VijayRaghavan as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please revise the manuscript as requested in the "Recommendations for the authors". As you will see, almost all these can be addressed by including additional qualifications, information or methods of analyses without need for new experiments. Please endeavour to respond to constructively to all of them, unless you have good reasons not to follow one or other specific suggestion.

Recommendations for the authors.

1. The data seem to support the authors conclusions that stronger odor responses in PNs/KCs correlates with stronger APL response and thereby stronger GABAergic feedback. Do correlations seen from comparison of APL response magnitudes for MCH and Oct (Figure 2 and Figure 3) hold true for other odor pair comparisons? If such (APL vs PN/KC) comparisons cannot be made, then the fact that studies of additional odorants are needed for more definitive conclusions should at least be discussed.

2. The main conclusion of the manuscript rests on the findings that in one condition (PN boutons, or KC claws with APL blocked), OCT>MCH, but in another condition (KC claws in wildtype), OCT=MCH. Currently this is shown using p<0.05 vs. p>0.05, but it needs to be shown with either an interaction in a 2-way ANOVA, or directly comparing the difference (Oct-MCH) between the conditions (as they did in comparing the differences Oct-dDL vs. Oct-MCH in Figure 2G vs. 2D) (see Nieuwenhuis et al., Nat Neurosci 2011).

3. Early figures (Figure 1A-C) need some labeling to orient nonspecialist readers, particularly directional markers (anterior/poterior, medial/lateral), similar to figure 5. Scale bars should also be included on these anatomical figures throughout.

4. The spatial analysis was done for 5 anterior-posterior zones (Z1-Z5), selected as horizontal slices through the calyx. This seems to make sense for most of the PN terminal fields, but what about the other two axes (medial-lateral, dorsal-ventral)? For instance, some PNs (e.g., the PA-responsive one) traverse more than one A-P slice and have terminal fields in multiple dorsoventral layers.

5. In figure 5, an analysis directly comparing the spatial patterns of APL with PN/KC responses would bolster the evidence for local inhibition in shaping the responses. 5. Does silencing APL alter the regionally-specific responses in KCs? Providing an experimental test would bolster the evidence for a local role of APL modulating these spatial patterns.

6. The authors quantify PN bouton and KC claw responses by selecting only ROIs that responded to the odor. (line 303-4: "calculated per calyx the average peak response among the boutons showing calcium transients") However, sometimes they refer to "average bouton response" or "average microglomerular postsynaptic response" which could reasonably be interpreted to mean the average including non-responsive boutons/claws. This point should be clarified either by changing the phrasing or adding more explanations of the quantification. It's also not clear if the responses in Figure 3B, 3F, 4B are quantified for the same ROIs across both odors, or if for each odor, only the ROIs responsive to that particular odor were used. Could the authors be more explicit about their quantification methods? In the Methods section, they should explain how they identified bouton/claw ROIs (e.g., manually, automated thresholding, etc) and how they selected the responsive ROIs (this last point is relevant for the "limit of detection" referred to in line 563). Clarifying the quantification methods is important because it could help to explain the contrast between the results in this manuscript and previous findings that stronger odors elicit bigger responses in KCs in the calyx (Apostolopoulou and Lin, 2020 – Figure S16), where responses were quantified by averaging over all pixels in the calyx.

7. Figure 5C This is a clever way to show that APL odor responses are localized to the part of the calyx innervated by the PNs responding to that odor. The graph is persuasive, but the statistical analysis may not be appropriate. Perhaps the authors do not intend to state that the black curve is significantly different from the blue curve (that would mean only that PA is more strongly activating than FA and MP), but rather that the slope of the black curve is steeper than the slope of the blue curve? This should be tested using the linear regression analysis tool (for example using a feature in Prism: "Test whether slopes and intercepts are significantly different"). Ideally, the analysis should include a ratio for PA/FA and MP/FA.

8. Figure supp 3E (labelled 3F) – APL response vs. predicted PN response from Hallem and Carlson 2006 data passed through equation from Olsen et al. 2010. Do the odor concentrations match? The authors here use dDL and EtOH at 1:100 and ethyl acetate and pentyl acetate at 1:1000. That's a factor of 10 difference. But Hallem and Carlson only tested odors at factors of 100 difference (10-2, 10-4, 10-6, etc.), so it's not clear how the odors used here correspond to the Hallem and Carlson data. Perhaps an alternative approach is simply to plot the APL response vs. PN response for dDL, MCH and Oct using the data from Figure 2 and Figure supp 3A-D.

9. Figure 3F vs. 4B – why is the KC claw response in the APL ON control in Figure 4B only half the amplitude as in the wildtype response in Figure 3F?

10. Figure supp 2C – For identifying synapses as being on claws vs. being on the dendritic branch, the authors write in the Methods, "The localization of the synapses (e.g., on PN bouton or not) was addressed manually by two separate users in a blind manner" – can they clarify what criteria they used for this manual classification?

11. Line 564-570. The argument against option (ii) (that more MGs respond when APL is blocked because more KCs have back-propagating action potentials) is not convincing. The data indicate only a slight increase in the number of responsive MGs when APL is blocked, which is perfectly consistent with a small number of MGs having a large enough fraction of their 13 KC claws getting extra back-propagating action potentials that their odor response becomes detectable. Perhaps both options should remain on the table.

12. Line 528 "the average strength of postsynaptic responses in KC dendritic claws is homogenous among MGs" – but the histograms show that the response strengths are clearly heterogeneous among MGs as there is wide variation between MGs. Consider deleting the words "among MGs and".

13. Line 646 "incomplete silencing might increase KCs' output without affecting sparseness" – this is indeed the case – shown in Lin et al. 2014 Nat Neurosci, Figure 8.

14. Line 555-557 draws an implicit contrast between "the input gain control normalization executed by GABAergic interneurons in the AL (Olsen and Wilson 2008)" vs. "the high-pass filter function performed by inhibitory iPNs at the lateral horn (Parnas et al. 2013)." Actually, these are both the same mechanism – Parnas et al. 2013 notes: "We call this form of inhibition a 'high-pass filter' because it allows high-frequency spike trains to pass (Abbott and Regehr, 2004). Similar phenomena have also been termed input gain control (Olsen et al., 2010) or input division (Mysore and Knudsen, 2012)." Indeed, at the cellular level, both occur by pre-synaptic inhibition.

15. The finding that APL responds more strongly to stronger odors (Figure 2) should be placed in the context of a similar finding in Papadopoulou et al. 2011 (Figure S9).

16. The findings that blocking APL makes the amplitudes of odor responses in KC claws sensitive to stimulus strength (Figure 4) should be placed in the context of similar findings in KC lobes/calyx (Mittal et al. 2020 Nat Comm – Supp Figure 9, Apostolopoulou and Lin 2020 PNAS – Figure S3, S16, Lin et al. 2014 Nat Neurosci – Supp Figure 5), while making note of the different quantification methods.
