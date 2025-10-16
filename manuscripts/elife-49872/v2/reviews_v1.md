# Peer review - Round 1

Editors:
- Marlene Bartos, University of Freiburg Germany

Reviewers:
- Cheng-Chang Lien, National Yang-Ming University Taiwan
- Jean Christophe Poncer, INSERM, Sorbonne University France

## Review text

DOI: [10.7554/eLife.49872.024](https://doi.org/10.7554/eLife.49872.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Acceptance summary:

This study provides evidence that dendritic NMDA receptors underlie supralinear integration of excitatory feedback inputs from local principal cells onto CA1 PV-expressing fast-spiking interneurons. By using computational neuronal network models, this work further demonstrates that NMDA receptors in PV-interneurons support their cooperative recruitment and strengthening of principal cell assemblies.

Decision letter after peer review:

Thank you for submitting your article "Dendritic NMDA receptors in parvalbumin neurons enable strong and stable neuronal assemblies" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Gary Westbrook as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Cheng-Chang Lien (Reviewer #2); Jean Christophe Poncer (Reviewer #3). The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript provides a computational explanation on the potential role of NMDAR-mediated currents in PV interneurons in neuronal representation of given information. They show that dendrites receiving feedback excitation from local CA1 principal cells (PCS) show supralinear summation of EPSPs generated in close proximity at a dendritic compartment using glutamate uncaging. The data are reproduced by ChR2-mediated excitation of PC inputs. The authors apply a computational model consisting of PV cells and PCs and show that clustered synchronized excitatory inputs recruit PV cells if NMDAR-mediated EPSPs are induced. In contrast, randomized non-synchronized excitatory inputs do not reliably activate PV cells. By using neural network simulations, the authors provide evidence suggesting NMDAR enrichment may influence the properties of neuronal ensembles by promoting output/input fidelity and the stability of cell assemblies.

Essential revisions:

All three reviewers judge the work as high-quality, which provides new insights on the synaptic integration of excitatory inputs along the dendrites of parvalbumin (PV)-expressing interneurons. However, all reviewers formulated major criticisms, which need to be addressed by the authors.

1) The reviewers agree that the supralinear summation of uEPSPs evoked in PV+ interneuron dendrites in stratum oriens but not in stratum radiatum is central to the study, including the modeling part, but requires further investigation. Particularly, it is important to test the spatial constraints for supralinearity: how does spacing between simultaneously active inputs influence their summation and what happens when uEPSCs are evoked onto 2 distinct, same order sister dendrites? How does the number and duration of individual uncage locations influence the summation of EPSPs?

2) Figure 3—figure supplement 1 is important as it addresses whether the properties of GluA2-lacking AMPARs in PV+ cells influence synaptic cooperativity. It would be perhaps more explicit to represent these data as in Figure 3D-E and include the appropriate statistics.

3) State clearly that uncaging of glutamate does not necessarily activate synaptic receptors. See statement of reviewer #3 point 2 for details.

4) Figure 5—figure supplement 2 is important, as it describes the effect of NMDAR enrichment on the sharpness of the network response to a clustered burst of input activity. However, in its present form it is only descriptive. Can these simulation data be tested for statistically significant difference? Moreover, explain on what ground they chose the first and last 75 ms of network simulation, as it is not clear from Figure 5D that networks dynamics evolve much over time. It would be useful if the authors could include a panel similar to the middle panel in Figure 5D for the case of no NMDARs.

5) Excitatory inputs: the authors model external inputs to pyramidal neurons using a Poisson process. Although this is often done for modeling cortical networks, the reviewer is unsure whether this is most adapted to area CA1 of the hippocampus. It would perhaps be more informative to use Gaussian-modulated theta-frequency input. This would also let the authors test how/whether γ-band firing of PV cells is modulated by theta-modulated inputs. Moreover, supralinearity of excitatory inputs in this study is dependent on spatial clustering of glutamatergic inputs. Please discuss on what published information is available on the spatial distribution of co-active inputs onto CA1-PV interneuron dendrites in vivo.

6) There is always a concern about 'tuning' models to fit the desired output. Most modeling studies therefore perform a sensitivity analysis of the various parameters that were fixed for the simulations (see Marder and Taylor 2011 Nat Neuroscience; Rathour and Narayanan 2014 PNAS). Was such an analysis conducted within this study to ensure that no bias was generated in the network output due to the choice of various parametric values? Comment on this point in the manuscript.

7) AAV-ChR2 was injected in the dorsal hippocampus. Please comment on what part of the hippocampus has been used for in vitro whole-cell recordings in the study.
