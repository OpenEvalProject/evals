# Peer review - Round 1

Editors:
- Yibing Shan, Antidote Health Foundation United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65824.sa1](https://doi.org/10.7554/eLife.65824.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Using unbiased molecular dynamics simulations and metadynamics simulations, this work characterized the conformational landscapes of the wild-type EGFR kinase and a number of oncogenic mutants. It suggests that the effects and the underlying activation mechanisms of these mutations are varied. In particular, it suggests that the Exon20-deletion mutant tends to adopt a more open conformation, which may be a potentially important finding for drug discovery.

Decision letter after peer review:

Thank you for submitting your article "Structural basis of the effect of activating mutations on the EGF receptor" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jonathan Cooper as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Summary:

The authors present a metadynamics study comparing the free energy landscape of epidermal growth factor receptor (EGFR) and highlight the unique ways by which oncogenic mutations alter EGFR free energy landscape. The work identified a number of intermediate states unique for some of the mutants, which may be exploited in drug discovery. The characterization of one specific mutant, the Exon 20 insertion, is particularly timely, as many EGFR inhibitor drugs are inactive to this mutant, and drug discovery targeting this mutant therefore remains a challenge.

The reviewers raised a number of important concerns that need to be addressed to make this manuscript suitable for publishing in eLife.

Essential Revisions:

1) The authors should compare the kinetics of inactive-active transition for all four mutants and map the lowest energy path from the inactive to active state. If the change in free energy of transition in these mutants correlate to their known fold-change in catalytic activity, this would provide additional support for their model.

2) The observation that the Exon 20 mutants furnish a more open active site is perhaps the most direct and interesting result of this study. This should be further explored. For example, the authors can dock small molecules into a representative conformations of L858R and Exon 19 mutants, and into a representative conformation of a Exon 20 mutant, and hopefully show that the top hits of the former do not fare well in the latter and vice versa. This would be extremely informative to drug discovery.

3) Some of the simulation and analysis details are not described clearly or accurately, notably related to the used important collective variables. The positions of the active and inactive positions in terms of CV space seem to change across different free energy surfaces using the same CVs (See Figure 2-5). The authors need to further describe the CV they chose and explain the rationales behind the choices.

4) Three collective variables (CVs) were defined in the Methods description: CV1 was the difference between two salt-bridge distances, and CV2 and CV3 were distances in the contact map space with respect to the inactive and active conformations, respectively. Were all three CVs used in running the metadynamics simulations? In the figures and related simulation analysis, only CV1 and CV2 were used and appeared to be wrongly labeled. CV2 and CV3 were defined only related to the A-loop in the Sutto and Gervasio 2013, but described differently in this study. They need to be clarified.

5) It would help to plot CVs versus time to examine the simulation convergence and replica exchange rates. They also need to be compared with the unbiased simulation results in Figure 1-S2, which may support the authors statement that "these simulations hinted at slow motions that could not be sampled even by long MD simulations". This can be included in the SI.

6) The free energy surfaces appear noisy. Why were certain energy minima ignored for more detailed characterization, e.g., ~(0.22, 1.8) and ~(0.5, 2.3) in Figure 5 and a number of others with ~3-4 kcal/mol free energy values?

7) In Figures 3 and 4 it is confusing to show two different conformations for one single energy minimum. If they are indeed different low energy states, additional CVs may need to be defined with the corresponding new free energy profiles calculated to characterize these conformations. This need to be discussed and clarified.

8) In Figure 3 for the L858R mutant, why a clear energy minimum was identified in the "active" state in the previous study, but not in the current study.

Reviewer #1:

The authors present a metadynamics study comparing the free energy landscape of four distinct somatic mutations in EGFR and highlight the unique ways by which oncogenic mutations alter EGFR free energy landscape. The conformational landscape of the wild type receptor and EGFR mutants have been extensively studied in previous studies, and while the identification of intermediate states for some of the mutants is interesting, much of what the authors propose mostly validates or reinforces the models already put forward in previous studies.

Reviewer #2:

This study has presented unbiased microsecond molecular dynamics (MD) simulations and advanced parallel tempering metadynamics (PTmetaD) simulations to examine conformational free energy landscapes of the wild-type (WT) and four oncogenic mutants of the EGFR kinase domain. Notably, the authors have applied the same techniques to simulate the same WT and L858R mutant of EGFR in a previous study (Sutto and Gervasio, 2013, PNAS). The main difference in the present study is about simulations of three new mutants: D770-N771insNPG, A763-Y764insFQEA and dΔELREA. However, all the studied mutations generally bias the protein towards the active state, i.e., activating mutations. A number of previous publications as cited by the authors have also provided detailed mechanisms into inactivation of the WT EGFR kinase (Shan et al., 2013) and conformational changes in the activating mutant enzyme (Shan et al., 2012). In this context, the present study even with extensive simulations mostly confirms previous work and the new mechanistic insights to advance our understanding of the protein function are limited.

Strengths:

1. This paper has applied extensive unbiased and advanced enhanced sampling simulations to study the EGFR kinase domain, which is critically important for developing cancer treatments.

2. Free energy profiles can be calculated from particularly the enhanced sampling simulations to characterize conformational dynamics of the WT and mutant EGFR quantitatively.

3. Distinct conformations have been identified from the free energy profiles for the WT and four mutants of EGFR. It's clear that the mutations will bias the protein towards the activation state, which can help explaining the related previous experimental findings.

Weaknesses:

1. The work is not novel in the sense that the same techniques had been applied on the same WT and L858R mutant EGFR, except that another three different mutations are investigated here.

2. Some of the simulation and analysis details are not described clearly or accurately, notably related to the used important collective variables.

3. Apparent discrepancies are found between this study and previous work on the WT and L858R mutant EGFR.

Reviewer #3:

This work expands the group's previous studies that used conformational free-energy calculations to survey the conformational space of EGFR kinase WT and L858R. They apply a more recent force field and show that the observations on L858R are consistent with the previous results, which helps build confidence for this approach. They extend the work to cover Exon 20 insertion EGFR in this study. The quantitative characterization of the conformational landscapes in this work is important. The landscapes of various EGFR mutants together present a rich picture of how seemingly minor mutations can alter the conformational dynamics of EGFR kinase significantly, which is likely the case for many other proteins.

This work is particularly interesting with respect to drug discovery. An often discussed vision of drug discovery is to tailor drug molecules to selectively bind to the target in its minority but unique conformation to achieve specificity and reduce toxicity. This remains conceptual because the minority conformations are typically difficult to capture by crystal structures. MD simulations often capture such conformations but reliable quantification in terms of free energy is needed to choose a conformation to pursue drug discovery and such quantification remains untrusted. This work stands out in presenting a coherent and detailed quantitative survey. One of the more important results of this work is the characterization of exon 20 EGFR, showing that the insertions "open" the kinase and alter the shape of the active site. This explains why developing exon 20 drug remains unaccomplished and suggests a strategy for drug discovery.
