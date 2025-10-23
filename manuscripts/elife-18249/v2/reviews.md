# Peer review - Round 1

Reviewers:
- Volker Dötsch, Goethe University , Germany

## Review text

DOI: [10.7554/eLife.18249.014](https://doi.org/10.7554/eLife.18249.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Allosteric Activation of SENP1 by SUMO1 β-Grasp Domain Involves a Dock-and-Coalesce Mechanism" for consideration by eLife. Your article has been favorably evaluated by John Kuriyan (Senior Editor) and three reviewers, one of whom, Volker Dötsch, is a member of our Board of Reviewing Editors..

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors report molecular dynamics simulations to study the mechanism of allosteric activation of SENP1 by SUMO1 β-Grasp domain. The design of the simulations was motivated in part by previous NMR studies and in part by previous simulation study by the authors of a different system (PIN1). The mechanism that emerged from the simulations, referred to as a "dock-and-coalesce" mechanism, suggests that the binding of SUMO1 quenches fast (nanosecond) dynamics while stimulates slow (microsecond-millisecond) collective motions that couple distal regions together. In particular, the collective motion may facilitate structural rearrangements in the active site, therefore impacting the catalytic efficiency of SENP1.

Overall, the study is well motivated by a problem (allostery) of general significance. The proposed mechanism is qualitatively consistent with reported experimental data (distinct effects on fast and slow dynamics), and it provides novel physical insights into the allosteric activation of SENP1 and related systems (e.g., DUB). The mechanism also provides new clues to the design of small molecules that target SENP1 activation.

Essential revisions:

1) It is now becoming relatively easy to reach microsecond time scales in MD simulations, even for relatively large systems, and one should make an argument for why 200 ns were deemed appropriate to address the questions posed here since modern computational resources would allow simulations in excess of what is presented here.

2) It is also now common practice to reach statistical redundancy by running replicate simulations. To obtain statistical significance of the results a replication of the simulation would be important.

3) The figure caption of Figure 2 should mention that 2C maps the sampling onto the principal components. Otherwise, the figure is confusing.

4) It would help to indicate in Figure 2A where exactly the cleft distance was measured.

5) The comparison with the experimental chemical shift perturbations validates the simulations but doesn't quite help with the mechanistic picture. It would be useful to discuss a mechanistic model that explains the observed effects. In particular, how does triggering slow motions lead to reorganization of the active site that favors catalysis. Additional discussion that further clarifies this important aspect of activation would be beneficial to the clarity of the proposed mechanism.
