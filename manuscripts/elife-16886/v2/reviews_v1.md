# Peer review - Round 1

Editors:
- Antoine M van Oijen, University of Groningen , Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16886.021](https://doi.org/10.7554/eLife.16886.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Complexin induces a conformational change at the C-terminal end of the SNARE complex" for consideration by eLife. Your article has been favorably evaluated by Randy Schekman (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Complexin is thought to be a major regulator of neuroexocytosis and the structural basis for its regulation of SNARE-dependent membrane fusion is of great significance and interest. Choi et al. use single-molecule FRET to show that complexin can be in one of two conformations when bound to the SNARE complex. Importantly, the authors demonstrate that complexin has the capacity to disturb the C-terminal region of the SNARE complex, which potentially provides a structural basis for the "clamping mechanism". Further, the authors show that complexin bound to the ternary SNARE complex can make an intermolecular bridge to the syntaxin-SNAP25 binary complex, which supports the "trans-insertion model" proposed by Rothman and coworkers. Finally, the authors report a method using co-incubation with the C-terminal fragment of synaptobrevin to allow proper SNARE complex assembly of immobilized SNARE complexes.

The reported findings are very important for our current understanding of complexin function in regulating neurotransmission. Complexin clearly has multiple functions that have been localized to distinct domains of the protein, but contradictory models (all with substantial experimental support) have been put forth as the molecular mechanisms for these roles. The current study dramatically extends the molecular picture of the configurations of complexin interacting with the SNARE complex and the authors make convincing arguments about the connections between these configurations and complexin function. These results excitingly bridge several contradictory models, and thus the readers of eLife will receive the current work with broad interest.

However, the manuscript has a number of issues that should be resolved before further consideration.

Essential revisions:

Previous work by Lu et al. (JMB 2010; 396:602) is not cited in the manuscript, but has significant overlap with the results presented in this work. Intriguingly, their results and conclusions are contradictory to those presented in the current manuscript:

1) Lu et al. attached the nitroxides to positions 28, 35, 42 near or in the accessary helix region and investigated with EPR. In that work, Lu et al. did not observe two components that would reflect two different conformations of complexin when bound to the ternary SNARE complex. Although EPR is an ensemble technique, it is highly sensitive to protein conformational changes. Further, the method is fast enough to pick up the type of conformational changes discussed in the current manuscript.

2) In Lu et al.'s JMB paper they labeled the C-terminal positions of synaptobrevin 2. Again, complexin binding to the SNARE complex did not bring about spectral changes that reflects the large conformational change observed with FRET in this study.

Using single-molecule FRET data, the authors derive distances that are then compared to the distances obtained from the crystal structures. Distance information from smFRET experiments is notoriously unreliable; many factors such as local protein interactions and dye conformation play a role in the conversion between FRET values and distance. As is the convention in the field, it is much safer to use FRET values to classify conformational states and draw correlations between these values and different distances observed in crystal structures.

In discussing Figure 3, the authors make statements related to average distances corresponding to the two states in the smFRET experiments being equal to the distance derived from the ensemble-averaged experiments. This argument is mathematically incorrect: in a bulk-averaged FRET experiment one observes the average of two FRET values that each have a highly nonlinear dependence on the distance (1/R6), so that the average FRET value will certainly not be the same as a FRET value calculated using the average of the two distances. Furthermore, comparisons between FRET values derived from these two studies can only be made when the label sites and fluorophores/linkers are identical. This issue is connected to the inaccuracy of FRET experiments reporting on distance: one can only compare FRET values obtained with the exact same proteins and labeling, with conformation being the only difference.

The experiments described in Figure 5 are very insightful and present a nice way to probe the role of complexin in mediating interactions between two different SNARE complexes. In Figure 5B, the authors show a raw trace of acceptor and donor intensity, but surprisingly FRET events correspond to only an increase in the acceptor intensity; the donor intensity remains unchanged. I assume that the 100 nM donor concentration in solution gives rise to a high background, but judging from the signal height and noise levels one should certainly see a drop in the donor signal when FRET occurs. The authors should explain this experiment in much more detail.

One concern with the experiments could be the use of fluorescent labels in the SNARE C-terminal region to probe conformational changes induced by complexin binding near the same region. Direct complexin contacts with the dyes or environmental changes due to close complexin binding could be speculated to impact FRET signals without conformational changes. The authors have taken substantial care to address such potential concerns. In particular, anisotropy studies of the fluorophores at these locations do not show changes with or without complexin (Figure 4—figure supplement 2), and γ factor analysis of FRET pairs Figure 4—figure supplements 3 and 4) also are unchanged with or without complexin. These results suggest dye rotational motion or quantum yields are not significantly altered by complexin binding. In addition, the authors might wish to further emphasize the observation that their measurement of binding kinetics and equilibrium binding constants (Figure 7) for labeled proteins that agree with literature values of unlabeled proteins suggests the fluorophores are not interfering with the biding interfaces. One more point is that the sum of donor and acceptor intensities for the traces shown in Figure 4—figure supplement 1 are all nearly the same in all of the FRET states. This suggests that there is no large Protein Induced Fuorescence Enhancement that is seen in some systems when a protein binds near a fluorophore (Hwang H. and Myong S. "Protein induced fluorescence enhancement (PIFE) for probing protein-nucleic acid interactions" Chem. Soc. Rev. 2014; 43:1221), further suggesting FRET changes are not an artifact.

The concentration dependence of complexin's effect on the C-terminal SNARE complex seems weaker (See Figures 4C and 4E) than the equilibrium binding constant of complexin for the SNARE complex reported in Figure 7 and in the second paragraph of the subsection “Test of the surface tethering method by single molecule binding assay” as 70 nM. Am I misinterpreting the effect in Figure 4C/E, or does this suggest that there is another process beyond simple bimolecular binding involved in this phenomenon of rearranging the SNARE c-terminal? Maybe this point could be emphasized in the paper if the authors agree.

In the subsection “Calculation of distances from FRET efficiency and error estimation”, is the width of a Gaussian FRET peak the best estimate for σ_sub_E? The width of FRET peaks for static conformations is typically dominated by statistical shot noise in the intensity signals. For the estimate of the error in the dye separation R, the uncertainty that is relevant is that in the accuracy of the peak value from the Gaussian fits used as the value E. Maybe this uncertainty in E is hard to determine as it is probably due to systematic variations and the width of the peak is some sort of estimate, but it is not clear how closely they are related. Maybe a cautionary comment is appropriate?
