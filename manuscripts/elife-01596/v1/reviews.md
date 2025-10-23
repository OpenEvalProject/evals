# Peer review - Round 1

Editors:
- Randy Schekman, Howard Hughes Medical Institute, University of California, Berkeley , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.01596.020](https://doi.org/10.7554/eLife.01596.020)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled ”Intrinsic and Extrinsic Control of Dynein-Based Cargo Transport Revealed by a Novel In Vitro Assay for mRNP Motility” for consideration at eLife. Your article has been favorably evaluated by the Editor-in-Chief Randy Schekman and 3 peer reviewers.

The Editor-in-Chief and the reviewers discussed their comments before we reached this decision, and the Editor-in-Chief has assembled the following comments to help you prepare a revised submission.

Understanding how microtubule-based cargos move bidirectionally along their tracks and achieve distinct patterns of spatial organization is an important problem. Here, Soundararajan and Bullock tackle this problem by first developing an improved in vitro motility assay for analyzing microtubule-based RNP motility. Their method relies on purifying native motor complexes from Drosophila extracts via their interaction with in vitro transcribed RNAs (hairy). Previous work from the Bullock lab has shown that dynein is recruited to these RNAs along with dynactin, Lis1, BicD and Egl. These RNP complexes exhibit a combination of unidirectional movement towards the minus end of the microtubule and bi-directional movement; no unidirectional plus end-directed motility was observed. This work then goes on to characterize these unidirectional and bidirectional types of motility.

Summary recommendations:

The nature of the bidirectional motion can be sorted out in a revision by a) improved MSD analysis, b) higher spatial resolution data of the bidirectional motion, c) analysis of other nucleotide states besides ATP (e.g., ADP/ATP-vanadate or perhaps ADP) and d) most definitive (but perhaps optional) optical trapping to see if the plus end direction is associated with force.

Detailed major concerns:

1) A great deal of this paper involves the analysis and dissection of bidirectional transport, and it seems to me that the interpretation requires an understanding of the principle mechanism of bidirectional motion. The primary question is what is causing motion to the plus end of the microtubule? There is some mention of this issue only at the very end of the discussion section, but it makes it confusing to read along the way and to interpret at the end. Addressing this issue is important for making conclusions such as a ”tug of war” between opposing motors. There are three possibilities:

1) That there is a kinesin moving toward the plus end. This is what most people would assume when “plus end motion or tug of war” is discussed. However, there is no evidence for this in the Results, and in the Discussion, the authors think that this is not the case.

2) That dynein itself is a plus end directed motor, i.e., that it uses ATP energy to execute a prolonged sequence of plus end direct steps (for example a 500 nm run would be about 60 x 8 nm steps).

3) That dynein binds weakly to the microtubule and that the bidirectional motion is thermally driven (perhaps with some mild bias toward the minus end).

This is an important issue and I think that the authors need to confront it in a head-on and convincing way for publication in eLife. There are some papers in the literature that suggest model 2 (dynein can either be minus or plus end-directed motor, and perhaps can convert between the two states). This would be a significant discovery if true, but convincing evidence is needed to advance the field. It is important to rule out diffusion as a mechanism; an MSD plot for one run can be misleading since a single run with limited events can produce a deviation for diffusion which could look like “active transport”. Thus, this is not an easy question to answer in a convincing way. Simulation of 1-D diffusion (to see how often if produces apparent unidirectional runs) might be helpful. But better data would be most helpful. Looking at stepping behavior directly at higher resolution might be helpful. The 6 GFP RNPs should be pretty good for analyzing stepping behavior of the RNPs (how unidirectional is the motion when one gets down to <10 nm resolution?). It might also be possible to attach the RNP to a Q dot. Second, is the motion in the plus end direction associated with significant force production? This could be done by attaching the RNP to a 1μm bead. Is the plus end direction associated with a ∼6 pN force (this might be suggestive of a kinesin, but would not rule out a dynein or multiple dyneins; it would rule out diffusion)? Even a 1-2 pN force (what has been reported for a single dynein) might rule that out diffusion. It would also be powerful to show that the plus end force (like the unidirectional minus end) scales with copy number of dynein. However, if there is little force, then this would suggest a diffusive model. Although less informative than the two prior suggestions, it could be interesting to add ATP-vanadate to kill unidirectional minus end movement and see what happens to the “bidirectional” RNPs – is the plus end direction affected? If not, then this might be diffusional. The authors might have other ideas on how to address this issue as well. The bottom line is that the authors need to better support their explanation of an active plus end-directed motor activity. This might reveal that bidirectional motion is due to a switching behavior of the dynein motor itself. If shown convincingly, this would be very interesting and would increase the interest in the paper considerably. It could then be featured in the abstract for sure.

It is clear from the shown data that two types of runs are observed – unidirectional runs and runs where frequent switching of direction takes place. A lot of the conclusions are based on the MSD analysis of individual runs shown in Figure 1–figure supplement 1. This analysis is thus of crucial importance for the interpretation of the rest of the data in this paper and should therefore be moved, together with the kymographs, to the main figures.

It is unfortunate that each MSD plot is obtained from just a single event. In such cases, the calculated values at higher time lags become increasingly inaccurate, because they are obtained by averaging much less displacements than at shorter time lags. In these cases, it is recommended (and common practice) to only analyse the MSD trace until the time lag that corresponds to one quarter of the total trace length. (see Saxton, Biophys J 72, 1744-1753, 1997). Therefore, the ranges that were used to fit the MSD curves seem inappropriate, as is the interpretation of the inset shown in Figure 1–figure supplement 1D.

In addition, rather than analysing just single events to obtain an MSD trace, it is common practice to analyse many more events and analyse the data in some statistically correct manner. Since many proteins have been observed to perform diffusive motility along microtubules (e.g., MCAK, Eg5, Ase1, PRC1), several procedures have been firmly established for this.

The authors observe back-and-forth movements along microtubules. The essential question is whether this motility is active, i.e., driven by ATP-dependent molecular motors, or passive, i.e., driven by thermal excitation. The apyrase experiment does not solve this question, as it could lock the motor into a tightly bound state. Additional experiments should include the use of ADP.

The authors state that: “MSD analysis of individual bidirectional RNPs suggested that there was both a diffusive and a deterministic component to their movement in each direction along the microtubule. These observations imply that individual bidirectional RNA–motor complexes undergo directed transport interspersed with diffusive motion.” These conclusions were based on analyzing the complete MSD trace of an individual trajectory, which is incorrect. In addition, the reasoning suggests that any quadratic dependence somewhere in the MSD trace is evidence for deterministic motion (as reported in Figure 1–figure supplement 1D). This also seems incorrect. In the case of unidirectional motility, one would indeed expect a quadratic dependence of MSD on time lag, as shown in Figure 1–figure supplement 1A. However, for bidirectional motility, there are three different options:

a) Passive, ATP-independent, one-dimensional diffusion on the MT lattice: In this case, one would expect a linear dependence of MSD on time lag for all times with in the range appropriate for analysis (up to one quarter of the total time, when individual traces are analyzed).

b) Active, ATP-dependent bidirectional motility occurring as short bursts of directional motion of average duration “tburst” followed by reversal of directionality. In this case, the MSD traces would appear quadratic/ballistic/deterministic for time lags shorter than “tburst”, and linear for times greater than tburst. In Figure 2, the authors report bursts of ∼500 nm at 1.5 μm/s, suggesting that tburst is approximately 0.3 seconds. Therefore, MSD curves should only be quadratic for times below 0.3 seconds and linear above this.

c) Passive, ATP-independent, one-dimensional diffusion interspersed with occasional (short) runs in the minus end direction every x seconds. In this case, the MSD trace would appear linear up to t = x seconds and become more quadratic at longer times due to the bias introduced by the occasional unidirectional runs. However, also in this case MSD traces from individual trajectories are only reliable up to one quarter of the total time.

Finally, in the description of the plots, the authors state that the red curves represent the deterministic contribution (v2t2) and the black lines the diffusive contribution (2Dt) of the fit to the data (open circles), but this description seems incorrect given that the sum of both contributions is much higher than the real data.

Given these concerns, it is still unclear if bidirectional motility is driven by ATP-dependent motor activity. Even for pure diffusion, the design of subsequent data analysis for Figure 2 will result in separation of the trajectories in apparent persistent runs. Therefore, as it stands, none of these data can be properly interpreted. However, the extreme similarity between plus and minus end 'runs' could be evidence for passive diffusion in both cases.

MSD analysis must therefore be strongly improved.

a) Much more traces should be analyzed and the analysis should be corrected. One should either just average squared trajectories without internal averaging (such as in Helenius et al. Nature 2005) or average MSD traces obtained by internal averaging until one quarter of the total trajectory time.

b) In the case of bidirectional trajectories, testing for a quadratic dependence for MSD(t) as evidence for ATP-driven directional bursts should only be done in the range from 0 to 0.3 seconds. Plotting the MSD(t) on a log-log scale would be helpful for such a test.

c) Nucleotide dependence should also be tested by using ADP instead of ATP.

2) What is the relative amount of dynein/dynactin recruited to HLE compared to hwt, hΔLE, hSL1x3? This information seems essential for interpreting the experiments in Figure 5. Overall, I found the HLE experiments confusing. Are Egl and BicD present on HLE? What is the basis for dynein/dynactin recruitment to HLE RNA?

Perhaps one could examine the effect of transport of RNPs by changing the copy number of the HLE (e.g., a HLE-short oligo-HLE-short oligo-HLE). Looking at the data, the HLE seems to be a cleaner recruiter of active minus end-directed dynein and could be good for looking for effects of what happens with increasing number of active dyneins. The whole hairy mRNA is more physiological but it seems to recruit some “unidirectional and bidirectional” dyneins, which might complicate the interpretation of how increasing copy number affects motor properties. At minimum, it would be interesting to have compare 1x and 3x HLE and see if the same conclusions (e.g., processivity, velocity, mean run time, reversals, etc) are true as for 1x and 3x hairy mRNA.
