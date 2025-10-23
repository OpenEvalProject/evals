# Peer review - Round 1

Editors:
- Donald Hamelberg, Georgia State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70362.sa1](https://doi.org/10.7554/eLife.70362.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper describes a vital step in the infection cycle of the Covid-19 virus, providing useful insights into how the virus enters the cell and the importance of the modification to viral proteins with glycans. Despite the use of a simplified model to describe the system, this study provides a thorough examination of the conformational changes of the Covid-19 Spike protein, knowledge that could be exploited for drug design purposes and would otherwise have been impossible to obtain with a more detailed model.

Decision letter after peer review:

Thank you for submitting your article "Sterically-Connned Rearrangements of SARS-CoV-2 Spike Protein Control Cell Invasion" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Kei-ichi OKAZAKI (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) For data reproducibility, both pre-fusion and post-fusion structure models should be provided as coordinate files in the SI files. Based on limited available information, authors made complete structure models, which itself has considerable values for subsequent studies.

(1a) Related to this, it is not explicitly stated that the structure drawn in Figure 1C is the post-fusion model the authors used in this work. If not, the post-fusion structure must be provided for example alongside Figure S1.

(1b) In the structure in Figure 1C, 3 TMs look asymmetric. Since TMs are not included in the original PDB model, authors modeled it. How this particular asymmetric configuration appeared?

(2) In the simulation, TMs are restrained to the implicitly-assumed membrane plane, which is reasonable. However, in the snapshots in Figures 2 and 4, the tilt angle of TMs does not seem to be restrained. Is it possible that this slant TMs may affect the overall orientation of the spike proteins and thus could affect the dFP? Can author comment on it?

(3) In the analysis of Figure 5, once one FP captures the host membrane, this must anchor the FP subsequently. This anchoring must affect the dynamics of the rest of spike protein including the other FPs. Therefore, in reality, there must have higher probabilities of multiple FP captures (2FP and 3FP). Can authors conduct some simple simulations in which FP is anchored once it reaches the host cell membrane.

(4) In the description of all-atom structure-based model, The meanings of "1-3 dihedral potentials" and "6-12 interactions" are not clearly understood.

(5) It was difficult to understand the viral membrane potential described in Equation S1. What does "*" mean in the upper equation and does K take a positive or negative value? It might help to include a plot of the potential along z.

(6) It would be useful to have a detailed Discussion section on caveats of the model/potential alternate mechanisms as well as possible predictions which can be tested which include the following facts/questions. The alternate mechanisms need not be simulated. They can be speculations based on the present model. The indicated citations are just suggestions and may not represent the latest results. The authors should check for those.

(6a) The starting prefusion structure for the simulations is a hypothetical structure of what the spike would look like post cleavage. This should be emphasized. Does the frustration analysis indicate that some regions will already be unfolded pre-cleavage? For instance HR2 could already be unfolded before cleavage and then will it be able to partially cage some part of the spike? And what would this do to the mechanism?

(6b) What changes in mechanism could occur if this were a dual structure-based model instead of a single structure-based one? Do any of these seem physically reasonable?

(6c) Does the importance of glycosylation decrease if HR1 folds faster than the timescale of uncaging of HG without the glycosylation? What increase in contact (or dihedral) strengths or contact to dihedral ratios would be required for this to happen? Are these increases physically reasonable?

(6d) The TM helices are pinned into a trimeric conformation. What would happen if they are not and can move away from each other? See for instance: https://www.biorxiv.org/content/10.1101/2021.06.07.447334v1

(6e) Some percentage of spikes are naturally in the post-fusion conformation. See for instance: https://science.sciencemag.org/content/369/6511/1586 How does that fit into the simulation results?

(6f) Please look through current literature (since this is a fast moving field) for the role of spike sugars in fusion. See for instance https://elifesciences.org/articles/61552 Are there experimental results which support the present model or can the authors suggest experiments which can test the model specifically in the context of sugar placement?

(7) Throughout: Viral membrane envelopes are not called "capsids".

(8) Lines 52-57: These sentences imply an order to the cleavage/ACE2 binding events (ACE2 binding happens after cleavage). Has this been proven? If yes, please give a reference. If not, please reword.

(9) Figure 1: Please also give PDB IDs for the structures right here.

(10) Lines 153 onwards: Since at least some model justification depends on frustrated contacts, it would be useful to explain frustrated contacts in some detail and bring the supplementary figure into the main paper (if no page limit constraints exist).

(11) Figure 5B: Please state if this figure is for a glycosylated protein.

(12) Line 290: Please remove the word dramatic. It's not a quantifiable amount.

(13) Lines 301-305: I don't understand what happens when FPs transition to a post-fusion conformation without engaging the host membrane. What does this mean in the context of the present model? And what happens in hemagglutinin? It would be useful to have a clarification of these sentences and a detailed explanation.

Reviewer #1:

Authors performed all-atom structure-based molecular dynamics simulation of the conformational change process of SARS-CoV-2 spike protein from its pre-fusion form to the post-fusion form, with and without glycans bound to the spike protein. Authors found that the bound glycans provide considerable steric barrier in the transition, which prolongs the transition compared to the case without the bound glycan. Interestingly, this intermediate configuration, called caged state, has high probability to extend its fusion peptide towards the host cell membrane. Thus the bound glycan enhances the probability for the spike protein to capture the host cell membrane.

Using a simplified energy function, i.e. the structure-based model, authors could simulate extremely large-scale conformational change numerous times, which robustly shows the role of the bound glycans., which strengthens their finding.

On the other hand, any attraction interactions of glycans with protein amino acids are completely ignored in this simplified energy function, which is a clear limitation of the current study. These interaction, if included, could give much longer pause in the caged intermediate. Thus, real effect of the bound glycans may be even stronger.

Reviewer #2:

Dodero-Rojas et al. investigated a large-scale conformational change of the SARS-Cov-2 Spike protein involved in membrane fusion to its host cell. They used a structure-based all-atom model to simulate the large-scale conformational transition between prefusion and post-fusion conformations, which is impossible to simulate with conventional simulation methods. From extensive simulations, they identified the "caged" intermediate, which is realized through steric interactions of glycans. It was clearly shown from various control simulations that the caged intermediate has a much shorter lifetime without glycans, and glycans attached to the head group (HG) are mainly responsible for the stable intermediate. Furthermore, they showed that the caged intermediate facilitates capturing of the host membrane by extending the fusion peptides (FP) in the perpendicular direction to the membrane. The probability of capturing the host membrane by FP is higher with the stable caged intermediate in the presence of glycans for the virus-host inter-membrane distance of 30 nm, consistent with the cryotomography observations. Overall, the author's claims and conclusions are justified by their data. The strength of this work is that they simulated the unprecedently large conformational transition thousands of times. The weakness is that they used a simplified model that might miss physical interactions like electrostatic interactions. However, this work can establish a foundation for more detailed simulations with precise physicochemical interactions.

Reviewer #3:

The conformational transition of the SARS-CoV2 spike protein from its prefusion state to its post-fusion state helps the viral envelope fuse with the host membrane and eject the viral RNA into the host cell. This conformational transition is difficult to study in its entirety using either experimental techniques or standard simulation methods. Here, the authors use starting structures modelled on the prefusion structure and a potential energy function encoding the post-fusion structure to characterize the spike conformational transition using molecular dynamics (MD) simulations. Such structure-based models simplify the potential energy function and are able to simulate timescales many orders of magnitude longer than those seen in standard atomistic MD simulations. The spike simulations show that a helical region (HR2) C-terminal to the spike head (HG) which links HG to the transmembrane segment (TM; embedded in the viral membrane) unfolds and cages HG close to the viral membrane. Glycosylation increases the size and roughens the surface of HG allowing it to be caged for longer by HR2. This allows the helical region (HR1) N-terminal to HG to fold into a long helical trimer and potentially reach out to and latch onto the host membrane more effectively suggesting that glycosylation enables efficient fusion.

Structure-based models encode the protein structure in the potential energy function simplifying it. They also do not encode interactions which are not present in the structure. In the model used here, this implies that not all interactions present in the starting prefusion structure are stabilizing. The viral membrane is encoded implicitly while the host membrane is excluded and the sugars are included using connected beads which incorporate the sugar structure but ignore any further attractive interactions. However, such simplified models have a grounding in protein folding theory. Additionally, it is such simplifications which allow the model to simulate the spike conformational transition. Finally, similar models have previously been successfully used to understand the conformational transitions of large molecular machines such as the ribosome.

The authors have successfully simulated the spike conformational transition, shown a likely order of events that occur during this conformational transition and illustrated the potential importance of spike glycosylation to SARS-CoV-2 fusion.
