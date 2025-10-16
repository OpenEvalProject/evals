# Peer review - Round 1

Editors:
- Gary L Westbrook, Vollum Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31755.026](https://doi.org/10.7554/eLife.31755.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Pre-post synaptic alignment through neuroligin tunes synaptic transmission efficiency" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Gary Westbrook as the Senior Editor.

The reviewers have opted to remain anonymous. The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission.

As you will see some of the comments will require additional experiments concerning:

1) The validation of the culture results using slice recording;

2) The inclusion of evoked responses in addition to the mEPSC analysis;

3) Additional simulation to address the comments of both reviewers; and

4) Editing to avoid overinterpreting the results.

The original non-overlapping comments of the reviewers are below.

Reviewer #1:

The paper by Haas et al. examines the role of neuroligin in aligning postsynaptic receptor nanodomains to presynaptic active zones and the functional consequences of this alignment for synaptic transmission. To address these questions, the authors use imaging methods (dSTORM), electrophysiology, and modeling. The main findings are:

- Super resolution imaging reveals a strong spatial colocalization between AMPA receptors and neuroligin-1;

- Truncation of the C terminus of neuroligin-1 disrupts this colocalization and shifts the release machinery away from AMPA receptor clusters;

- Electrophysiological analysis and modeling suggest that this physical shift markedly decreases the efficiency of synaptic transmission.

Based on these results, the authors conclude that the alignment of pre- and postsynaptic components plays a critical role to ensure the efficiency of synaptic transmission. Overall, I found this a potentially interesting paper. The combination of high-resolution imaging, electrophysiology, and MCell modeling is nice and provides new insights into the mechanisms of synaptic transmission. However, it is also clear that parts of the paper are preliminary, and major revision is required to address these weaknesses.

1) NLG1 and NLG1 deltaC were mostly expressed on wild-type background. This is a complication, because endogenously and exogenously expressed NLG1 mix. The necessary KO control data come only very late in the manuscript, when functional properties of synaptic transmission are assessed.

2) The conclusions stand and fall with the validity of the culture systems used. The authors should make an attempt to validate the results in acute slice preparations.

3) The functional characterization of synaptic transmission is rudimentary. A lot can go wrong in the analysis of miniature synaptic events, and evoked and miniature release may not even be mediated by the same postsynaptic receptors. Thorough analysis of evoked EPSCs seems required to support the conclusions.

4) The diffusion coefficient of glutamate in the synaptic cleft seems an important parameter. However, the value used is unclear (it is just briefly mentioned in the legend of Figure 6), and how its exact value would affect the conclusions remains open. This point should be addressed in systematic simulations. Furthermore, the synaptic cleft height may affect the conclusions. Why was it assumed 20 nm if the authors have the full reconstruction of the extracellular space?

5) The presentation of the results requires improvement. The functional significance of the NLG1-mediated alignment seems sometimes overstated. The relation between receptor alignment and previously reported receptor mobility should be better discussed (otherwise an apparent contradiction may remain for naive readers).

Reviewer #2:

This is a nice work dealing with an important and timely issue, which refers us to the basic mechanisms of synaptic transmission and its efficacy control. The authors employ some cutting-edge super-resolution techniques and electrophysiology in cultured neurons to find that the neuroligin NGL1 plays a key role in the clustering of postsynaptic AMPA receptors in front of the presynaptic glutamate release sites. This finding provides novel and important insights into the molecular machinery underpinning the functioning of brain circuits.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Pre-post synaptic alignment through neuroligin tunes synaptic transmission efficiency" to eLife. Your revised article has been evaluated by Gary Westbrook (Senior Editor), a Reviewing Editor, and two reviewers.

Both editors and reviewers think that the manuscript has been improved and has the potential to be an important paper. However, we think the functional aspects of the work have not reached acceptability. Specifically the discussion among reviewers and editors concluded that additional data requested in the first reviews should be pursued to fully support the conclusions the authors would like to make. We realize that this reflects additional work for the authors, but in our opinion this work would substantially increase the merits of the work. We hope you will be able to address these concerns in a revised manuscript.

Major points:

1) Regarding further experiments for slice recordings, the authors' contention that fast manipulation is not possible with this system is not compelling. It is indeed possible that viral expression generates expression at a sufficiently fast time scale, before structural changes are initiated. Before the authors have tried, it cannot be claimed that it does not work.

2) Regarding the criticisms concerning the evoked EPSCs, the authors now provide analysis of EPSCs evoked in strontium. However, issues with these data remain. First, strontium is a rather artificial approach to study evoked synaptic transmission. Second, the slow rise time of the evoked EPSCs is 2 ms (Figure 4—figure supplement 2D), which indicates technical problems with these recordings. How the authors can study the functional effects of nanoscale alignment under these recording conditions remains unclear. Finally, the authors try to argue that evoked EPSCs are difficult to interpret, because overlaying effects of receptor alignment and synapse number are difficult to dissect. However, a pessimistic view on the new data shown in the figure for reviewers would be that the central hypothesis is challenged. The authors could perform nonstationary fluctuation analysis of evoked EPSCs to distinguish between changes in N and q. In any case, additional experiments are needed to address the reviewers’ concerns.

3) Regarding the adjustment of rate constants in the AMPAR model (subsection “Synaptic efficiency critically depends on the AMPAR nanodomains to glutamate release sites distance”), it is unclear how microscopic reversibility can be maintained with these changes. Calculating the products of rates for the two cycles in clockwise and anti-clockwise direction in the modified model, they do not match, suggesting that microscopic reversibility is violated. Furthermore, the authors refer to Figure 5, but the relevant numbers are in the legend of Figure 6.
