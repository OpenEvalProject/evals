# Peer review - Round 1

Editors:
- Ariel Amir, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.107214.3.sa0](https://doi.org/10.7554/eLife.107214.3.sa0)

This work provides high-precision single-cell data on the relationship between DnaA activity and cell size, offering important insights for the field of cell cycle control. These findings motivate a novel and intriguing hypothesis for DNA replication initiation -the "extrusion model"- in which DNA-binding proteins modulate free DnaA availability in response to biomass-DNA imbalance. While the current indirect evidence does not fully establish the model, an experimental perturbation involving H-NS offers convincing support for its plausibility, laying the groundwork for future investigation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.107214.3.sa1](https://doi.org/10.7554/eLife.107214.3.sa1)

Summary:

The study by Li and coworkers addresses the important and fundamental question of replication initiation in Escherichia coli, which remains open despite of many classic and recent works. It leverages single-cell mRNA-FISH experiments in strains with titratable DnaA and novel DnaA activity reporters to monitor DNA activity peaks versus size. The authors find oscillations in DnaA activity and show that their peaks correlate well with the estimated population-average replication initiation volume across conditions and imposed dnaA transcription levels. The study also proposes a novel and interesting extrusion model where DNA-binding proteins regulate free DnaA availability in response to biomass-DNA imbalance. Experimental perturbations of H-NS support the model validity, addressing key gaps in current replication control frameworks.

Strengths:

I find the study interesting and well conducted, and I think its main strong points are (i) the novel reporters obtained with systematic synthetic biology methods, and combined with a titratable dnaA strain, (ii) the interesting perturbations (titration, production arrest and H-NS) and (iii) the use of single-cell mRNA FISH to monitor transcripts directly. The proposed extrusion model is also interesting, though not fully validated, and I think it will contribute positively to the future debate.

Weaknesses and Limitations

A relevant limitation in novelty is that DnaA activity and concentration oscillations have been reported by the cited Iuliani and coworkers previously by dynamic microscopy, and to a smaller extent by the other cited study by Pountain and coworkers using mRNA FISH.

An important limitation is that the study is not dynamic. While monitoring mRNA is interesting and relevant, the current study is based on concentrations and not time variations (or nascent mRNA). Conversely, the study by Iuliani and coworkers, while having the drawback of monitoring proteins it can access directly production rates. It would be interesting for future studies to monitor the strains and reporters dynamically, as well as using (as a control) the technique of this study on the chromosomal reporters used by Iuliani et al.

While the implemented code is made available and the parameter values are given in the text, important details are missing regarding the mathematical models (mathematical definitions, clear discussions of ingredients and main assumptions, and choices made in the deployment of such models, which are presented briefly in the Methods section). The reader is not given sufficient tools to understand the predictions of different models and no analytical estimates are used and the falsification procedures are not clear. More transparency and depth in the analysis would be needed to use the models as more than a heuristic tool for qualitative arguments. The Berger model for example has many parameters and many regimes and behaviors. When models are compared to data (e.g. in fig. 2G) it is not clear how parameters were fixed, and whether and how the model prediction depends on adjustable parameters.

Importantly, the statement about tight correlations of peak volumes and average estimated initiation volume does not establish coincidence. Crucially, the data rely on average initiation volumes, and the estimate procedure relies on assumptions that could lead to systematic biases and uncertainties added to the population variability (in any case error bars are not provided).

The delays observed by the authors (in both directions) between the peaks of DnaA-activity conditional averages with respect to volume and the average estimated initiation volumes are not incompatible with those observed dynamically by Iuliani and coworkers. The direct experiment to prove the authors' point would be to use a direct proxy of replication initiation such as SeqA or DnaN and monitor initiations and quantify DnaA activity peaks jointly, with dynamic measurements.

While not being an expert I had the doubt that the fact that the reporters are on plasmid (despite a normalization control that seems very sensible) might affect the measurements. The approach is different from the aforementioned previous study, which used a chromosomal reporter placed symmetrically, at the same distance from the origin of replication as the original dnaA promoter.

Overall Appraisal:

In summary, this appears to me as a very interesting study providing valuable high-precision data and a novel testable hypothesis, the extrusion model, supported by relevant perturbation experiments and open to future explorations.

Comments on revisions:

I am happy with the replies and the revisions.

The main outstanding point remains that reconstructing the mathematical model details from the text (and having to rely on the code) is not optimal for a reader. However, I do understand that the authors intend to use the models as a heuristic tool only and possibly plan a theoretical study where they explore the models more systematically.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.107214.3.sa2](https://doi.org/10.7554/eLife.107214.3.sa2)

Summary:

The authors show that in E. coli the initiator protein DnaA oscillates post-translationally: its activity rises and peaks exactly when DNA replication begins, even if dnaA transcription is held constant. To explain this, they propose an "extrusion" mechanism in which nucleoid-associated proteins such as H-NS, whose amount grows with cell volume, dislodge DnaA from chromosomal binding sites; modelling and H-NS perturbations reproduce the observed drop in initiation mass and extra initiations seen after dnaA shut-down. Together, the data and model link biomass growth to replication timing through chromosome-driven, post-translational control of DnaA, filling gaps left by classic titration and ATP/ADP-switch models.

Strengths:

(1) Introduces an "extrusion" model that adds a new post-translational layer to replication control and explains data unexplained by classic titration or ATP/ADP-switch frameworks.

(2) A major asset of the study is that it bridges the longstanding gap between DnaA oscillations and DNA-replication initiation, providing direct single-cell evidence that pulses of DnaA activity peak exactly at the moment of initiation across multiple growth conditions and genetic perturbations.

(3) A tunable dnaA strain and targeted H-NS manipulations shift initiation mass exactly as the model predicts, giving model-driven validation across growth conditions.

(4) A purpose-built Psyn66 reporter combined with mRNA-FISH captures DnaA-activity pulses with cell-cycle resolution, providing direct, compelling data.

Weaknesses:

(1) What happens to the (C+D) period and initiation time as the dnaA mRNA level changes? This is not discussed in the text or figure and should be addressed.

(2) It is unclear what is meant by "relative dnaA mRNA level." Relative to what? Wild-type expression? Maximum expression? This should be explicitly defined.

(3) It would be helpful to provide some intuition for why an increase in dnaA mRNA level leads to a decrease in initiation mass per ori and an increase in oriC copy number.

(4) The titration and switch models do not explicitly include dnaA mRNA in the dynamics of DnaA protein. Yet, in Figure 2G, initiation mass is shown to decrease linearly with dnaA mRNA level in these models. How was dnaA mRNA level represented or approximated in these simulations?

(5) Is Schaechter's law (i.e., exponential scaling of average cell size with growth rate) still valid under the different dnaA mRNA expression conditions tested?

(6) The manuscript should explain more explicitly how the extrusion model implements post-translational control of DnaA and, in particular, how this yields the nonlinear drop in relative initiation mass versus dnaA mRNA seen in Fig. 6E. Please provide the governing equation that links total DnaA, the volume-dependent "extruder" pool, and the threshold of free DnaA at initiation, and show-briefly but quantitatively-how this equation produces the observed concave curve.

(7) Does this Extrusion model give well well-known adder per origin, i.e., initiation to initiation is an adder.

(8) DnaA protein or activity is never measured; mRNA is treated as a linear proxy. Yet the authors' own narrative stresses post-translational (not transcriptional) control of DnaA. Without parallel immunoblots or activity readouts, it is impossible to know whether a six-fold mRNA increase truly yields a proportional rise in active DnaA.

(9) Figure 2 infers both initiation mass and oriC copy number from bulk measurements (OD₆₀₀ per cell and rifampicin-cephalexin run-out) instead of measuring them directly in single cells. Any DnaA-dependent changes in cell size, shape, or antibiotic permeability could skew these bulk proxies, so the plotted relationships may not accurately reflect true initiation events.

Comments on revisions:

The authors have addressed all of my previous concerns, questions, and suggestions sufficiently.
