# Peer review - Round 1

Editors:
- Axel T Brunger, Stanford University Medical Center , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22964.024](https://doi.org/10.7554/eLife.22964.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Dilation of fusion pores by crowding of SNARE proteins" for consideration by eLife. Your article has been favorably evaluated by Randy Schekman (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Josep Rizo (Reviewer #2); Jiajie Diao (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor concluded that major revisions are required before a final decision can be made.

Summary:

This study shows how the number of SNARE complexes affects the formation of fusion pores between discoidal lipid nanoparticles containing VAMP2 (vNPLs) and cells expressing flipped t-SNAREs at the plasma membrane. The approach used in this work is an extension of previous work (Wu et al., 2016) but now with larger (21-27 nm diameter) nanolipoprotein particles (nlp) instead of the smaller nanodiscs used in the previous work (6-18 nm diameter). The larger nlp discs can accommodate more v-SNARE proteins. The electrophysiological approach used by the authors offers better time resolution than optical microscopy approaches used to date to study fusion in reconstituted systems. Their data show how pores form and flicker back and forth for long periods of time. Even relatively large numbers of SNAREs yield pores of limited conductance. However, there are a number of potential concerns that limit the insights into SNARE mediated fusion. Overall, this appears to be more of a methods paper and the conclusions regarding SNARE mediated fusion should be toned down.

Essential revisions:

1) From the example shown in Figure 5D, it appears all fusion pores eventually reseal. Why is that? Could this be a consequence of cellular resealing mechanisms or constraints imposed by the patch clamp? Please test this possibility by using different size clamps.

2) These experiments use flipped t-SNAREs which exhibit considerably slower kinetics than wild type SNAREs (Giraudo et al., 2006): fusion in the presence of synaptotagmin and Ca2+ occurs in several minutes, vs. msec to sec. in reconstituted systems with wildtype SNAREs and synaptotagmin. Thus, use of the flipped t-SNAREs may profoundly alter the kinetics of the fusion pore opening and dilation as well as the number of SNARE complexes required to promote fusion. Moreover, the lipid composition of the outer leaflet of the cell membrane may be quite different from that of the inner leaflet of the plasma membrane (there is little PS in the outer leaflet of the cell membrane). Ideally, the authors should consider experiments to alleviate these concerns, but the minimum, these limitations need to be discussed in detail.

3) Another limitation of this study is that it is focuses on SNAREs only. Prior experiments have been done with a combination of large and small fluorescent probes to measure fusion pore dilation, e.g.: (Lai et al., 2013), and concluded that factors such as synaptotagmin are required for efficient pore expansion. Moreover, with the help of these other proteins, the number of SNARE complexes needed for fusion could be much smaller. The authors do mention accessory proteins at the end of the manuscript, but only in the context of organizing SNARE complexes, as indicated by the term 'accessory' itself, and without considering a direct role in membrane fusion. At the minimum, the authors should tone down every conclusion regarding the number of SNAREs required for neurotransmitter release.

4) Please indicate the percentage of vNLPs that fuse with the cells for the different vNLPs. This is a critical issue when rationalizing the data in terms of how the number of SNAREs influence fusion pore properties because the vNPLs are expected to have a distribution of VAMP copies rather than a single number. If the percentage of vNLPs that is low, the fusion may arise from the population that has much higher VAMP copies than assumed from the average. Describing the percentage of vNPLs that fuse is also important to evaluate this overall approach.

5) The number of fusion pores/min observed with empty NLPs (is what eNLP means?) is low compared to that observed with vNLP8, but not negligible; it appears to be about 8 times smaller in Figure 4C. Does this mean that eNLPs fuse spontaneously with the cells? If this is the case, an acceleration by a factor of 8 suggests that 8 SNARE complexes only provide about 1 kcal/mol to facilitate membrane fusion. If there is no flaw in this argument, the authors should emphasize this point and compare this energetic estimate will all the energetic arguments they make later in the manuscript.

6) Conclusions regarding fusion pore expansion should be taken with caution because the scaffolding protein may impose constraints that would not be present in vivo.

7) A concern is about the possibility of formation of multiple pores. In the third paragraph of the Results, the authors provided an explanation for single pore formation. However, they apparently excluded the possibility of pore formation involving multiple v-SNARE nanolipoprotein particles at the same time. Due to the large size of nanolipoprotein particles (23 nm in diameter), it is possible that there is more than one fusion pore for individual nanolipoprotein particle in the presence of many SNAREs. For example, compared to the large jump from 15 to 30 v-SNAREs, the difference between 8 and 15 v-SNAREs is negligible (Figure 5B). Could this imply the formation of another fusion pore?

8) In the section 'Derivation of best-fit model parameters…', the authors showed how they obtain the parameters in the model by fitting the calculated results of the model (equation 11) to the experimental data. For example, they fit the results in the range of 0.2 nm ≤ rpo ≤ 1.5 nm to obtain the tension of membrane γ and the steric-hydration force length scale λ (0.5 nm ≤ rpo ≤ 2.5nm) to determine a range for epsilon (4 nm ≤ rpo ≤ 4.5nm) to obtain tau. However, in equation 11, the total free energy depends on all the parameters in the full range of rpo, so how can the authors obtain an individual parameter in a different range of rpo?

9) The parameters in the mathematical model (i.e., rpo, h, δ, D, and the twisting angle phi of ApoE proteins) should be explicitly shown in the model in Figure 7.

10) To calculate the second term in equation 7, the authors approximated the pore as a cylinder of radius rpo and height λ = 0.13 nm. It seems that the height of the cylinder is too small, as the neck of the fusion pore can be on the order of ~5 nm in height. Please explain why choosing such a small height for the cylinder is a reasonable approximation.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Dilation of fusion pores by crowding of SNARE proteins" for further consideration at eLife. Your revised article has been favorably evaluated by Randy Schekman (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The manuscript has been improved but there are two remaining issues that need to be addressed before acceptance, as outlined below, using the same bullet numbers used for the points of the decision letter.

2) Some of the arguments offered with regard to lipid composition are reasonable, but saying that 'short PI(4,5)P2 does not have an effect (data not shown)' is not convincing, and the problem still remains that it is difficult to control lipid composition in this system and make it similar to physiological. This is particularly important considering the low percentage of fusion that they now report (point 4). The authors cite Giraudo et al., 2006, but the work in that paper suffers from the same problem. This concern does not invalidate the results from the authors, but they should acknowledge the problem in the manuscript. The fact is that lipids could play key roles in the fusion mechanism and the tendency of SNARE-centric models of membrane fusion to ignore this fact is deleterious to the scientific discussion in the field.

4) The authors again make some good arguments, but they really do not address the heart of the problem. With such low percentage of fusion, it seems very likely that fusion occurs for low populations of nanodiscs with higher copy number of SNAREs than the mean. The authors claim that this is unlikely because 'the fusion rate does not increase for mean copy number greater than 2-4 per NLP side (Figure 5A)'. However, in Figure 5A one can see a tendency for the fusion rate to increase up to vNLP15. Even though the differences may not be statistically significant, one just cannot draw the conclusion written by the authors. Hence, the authors should explicitly acknowledge that the actual numbers of SNAREs underlying fusion may be (in fact that are very likely to be) higher than the mean values described. The same issue applies to measurements of conductance.
