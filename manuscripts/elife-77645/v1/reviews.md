# Peer review - Round 1

Editors:
- Janice L Robertson, https://ror.org/01yc7t268 Washington University in St Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77645.sa0](https://doi.org/10.7554/eLife.77645.sa0)

Activation of NMDA receptors requires two co-agonists: Glutamate that binds to the GluN2 subunit and glycine/D-serine that binds to the GluN1 subunit. In the present manuscript, the authors address the interaction of D-serine, which is a less studied co-agonist than glycine, with the GluN1 and GluN2A subunits using molecular simulations as well as electrophysiology experiments. Surprisingly they find that D-serine interacts with the GluN2 subunit, further expanding our molecular understanding of NMDA receptor structure-function. This paper will be of interest to those who study NMDA receptors and ligand-gated ion channels in general.


---

# Peer review - Round 1

Editors:
- Janice L Robertson, https://ror.org/01yc7t268 Washington University in St Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77645.sa1](https://doi.org/10.7554/eLife.77645.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Excitatory and inhibitory D-serine binding to the NMDA receptor" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Janice L Robertson as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by josé Faraldo-Gómez as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Yun Lyna Luo (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers thought the manuscript was interesting and the research was carefully conducted. In particular, the discovery of D-serine interaction with GluN2A and its inhibitory effect is a novel result that will be of interest to the broader community. However, some questions remained as to the mechanism and the physiological or pharmacological relevance. The following major revisions are required to clarify these questions.

1) It is unclear to us whether D-serine has the capacity to reach such high concentrations in a physiological or pharmacological setting. Please provide more justification for this, or attenuate the conclusions that this provides a possible therapeutic treatment.

2) Extensive analysis is presented about the association of D-serine and its impact on LBD closure or efficacy. However, differences in agonist potency can be due to the differences in binding affinity and/or efficacy. Stabilization of the closed LBD conformation may indicate a change in efficacy, but affinity (KD) will still play a role in the final potency. The question still remains as to whether the binding affinity of D-serine to the two LBDs is stronger or weaker in comparison with glutamate and glycine. The relative strength of binding may be estimated if multiple associations and dissociation events have been captured in the conventional MD simulations. But it is not really clear whether dissociation events have been observed, and this needs to be clearly presented in the revised manuscript. Alternatively, this can be computed using alchemical free energy calculations or PMF calculations. Finally, an experimental KD should be extracted from the experimental competition data to compare to glutamate binding affinity and provide a reference for the computational analysis.

3) It is proposed that guided-diffusion drives serine binding to its site. This would imply that the residues on this path are necessary, and if mutated, would decrease the association rate and the ability for D-serine to compete with glutamate. Additional electrophysiological experiments or direct binding experiments would be useful in understanding the relevance of guided diffusion in the ligand-binding mechanism of NMDARs.

4) Please clarify what is the non-specific association signal in the MD simulations. Perhaps this has already been addressed in a previous study but should be included here. One option is to analyze the current trajectories and calculate the association event probabilities for a residue on the proposed guided path, compared to a similar residue at another interface that does not lead to the binding site. Alternatively, one could compare the current results with a negative control simulation where the ligand was replaced with a similar amino acid or molecule that has been verified as a non-binder for NMDAR.

Reviewer #1 (Recommendations for the authors):

The following changes are suggested for clarification:

1. The supplementary figure labels do not match the text.

Reviewer #2 (Recommendations for the authors):

The 2D-PMF of apo-state GluN2A LBD (Figure 3 C) only shows one minimum, rather than two states (open vs. closed) separated by a free energy barrier. Some clarification would be helpful for readers to better understand this free energy landscape.

On page 9 line 186, "we identified residues critical for stabilizing the agonist in the closed state by analyzing contacts in lowest-energy (<1 kcal/mol) conformers". More information is needed here or in the method section in terms of how the lowest energy was computed.

On page 10 line 217, "In fact, we observed D-serine binding to GluN2A, even in presence of glutamate" in the bulk solution or in the binding site? This is an important point if the LBD could accommodate glutamate and D-serine at the same time. But this somehow contradicts the competitive binding mechanism. If glutamate is present in the bulk solution during D-serine spontaneous binding simulations, do they have the same bulk concentration? Please clarify.

On page 10 line 218, "glutamate bound more frequently than D-serine and with longer residence times in the binding site" While the raw data is available in the Datasets, the number of binding events and residence time (1/Koff) could be briefly mentioned here to give a more quantitative comparison.

On page 17 lines 381-382, Figure S7 should be Figure S6?

Reviewer #3 (Recommendations for the authors):

I have just some general comments:

1. Just a suggestion but for Figures 1 and 2, it might be nice to have each figure panel indicate what it is showing. For example, above Figure 1C one could have a header 'Xi2 face dominates'. Figure 1D: 'Xi1 face of D1 lobe dominates'. Etc. Right now one must look back and forth between the legend/Results section and figure to discern what specifically is being shown. Again this is just a suggestion.

2. Electrophysiological experiments. The effect of D-serine, as noted by the authors, only occurs at fairly high concentrations especially relative to glutamate. The authors conclude that this reflects competition between glutamate and D-serine for GluN2 binding site. Might D-serine or glycine have alternative effects on receptor function? For example, do not these ligands induce receptor desensitization?

3. Given the fairly high concentrations of D-serine especially relative to glutamate, I am not certain that there would be any physiological or even pharmacological (i.e., D-serine as a drug treatment) impact. Either justify these comments more or attenuate them.

4. The N-glycans simulations are interesting and further expand our molecular insight into agonist/binding site interactions. However, many of the results are shown in Supplemental Material. Also, it would be helpful to have a summary figure of these results. Right now the information is buried in the text and it is hard to discern the conclusion of these experiments without reading and rereading to identify the outcome.

Related question. Figure 6C-6E. I see how GluN2A N443-Man5 and GluN1 N491-Man5 show an increased PMF more proximal to the D2 lobe. However, do these interactions impact D1:D2 interactions? Cannot this be assayed using the two-dimensional order parameter (Xi1:Xi2)?
