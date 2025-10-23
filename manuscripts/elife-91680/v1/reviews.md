# Peer review - Round 1

Editors:
- Arvind Murugan, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91680.3.sa0](https://doi.org/10.7554/eLife.91680.3.sa0)

This valuable contribution studies factors that impact molecular exchange between dense and dilute phases of biomolecular condensates through continuum models and coarse-grained simulations. The authors provide convincing evidence that the bouncing of molecules off the interface can lead to interfacial resistance and limit mixing. Results like these can inform how experimental results in the field of biological condensates are interpreted.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91680.3.sa1](https://doi.org/10.7554/eLife.91680.3.sa1)

Summary:

In this paper by Zhang, the authors build a physical framework to probe the mechanisms that underlie exchange of molecules between coexisting dense and dilute liquid-like phases of condensates. They first propose a continuum model, in the context of a FRAP-like experiment where the fluorescently labeled molecules inside the condensate are bleached at t=0 and the recovery of fluorescence is measured. Through this model, they identify how the key timescales of internal molecular mixing, replenishment from dilute phase, and interface transfer contribute to molecular exchange timescale. Motivated by a recent experiment reported by some of the co-authors previously (Brangwynne et al. in 2019) finding strong interfacial resistance in in vitro protein droplets of LAF-1, they seek to understand the microscopic features contributing to the interfacial conductance (inversely proportional to the resistance). To check, they perform coarse-grained MD-simulations of sticker-spacer self-associative polymers and report how conductance varies significantly even across the few explored sequences. Further, by looking at individual trajectories, they postulate the "bouncing" i.e., molecules that approach the interface but are not successfully absorbed is a strong contributor to this mass transfer limitation. Consistent with their predictions, sequences that have more free unbound stickers (i.e., for example through imbalance sequence sticker stoichiometries) have higher conductances and they show a simple linear scaling between number of unbound stickers and conductance. Finally, they predict that an droplet-size dependent transition in recovery time behavior.

Strengths:

(1) This paper is overall well-written and clear to understand.

(2) By combining coarse-grained simulations, continuum modeling, and comparison to published data, the authors provide a solid picture of how their proposed framework relates to molecular exchange mechanisms that are dominated by interface resistance and LAF-1 droplets.

(3) The choice of different ways to estimate conductance from simulation and reported data are thoughtful and convincing on their near-agreement (although a little discussion of why and when they differ would be merited as well).

Updated re-review:

This revised update by Zhang et al. is improved and addresses many of the concerns raised by myself and the other reviewer, especially with the expanded discussion, contextualized text in model description, and the addition of a nice example case-study in revised Fig. 4. I believe the paper provides solid evidence of how "bouncing" may contribute to interfacial resistance/exchange dynamics in biomolecular condensates and is a useful study for the community.

Note: In their response, the authors bring up an important point in references for LAF1 mutant FRAP data. While I found a few papers, for example https://www.pnas.org/doi/abs/10.1073/pnas.2000223117 and https://www.cell.com/biophysj/fulltext/S0006-3495(23)00464-2, these are likely to be not whole droplet bleaches. I wonder whether it may be possible to approximately predict the conductance from other parameters (such as from effective expressions in eq 14) to roughly estimate what the effect maybe since LAF-1 has fairly "known" stickers and spacers. Note that this is not required at all, but I just bring this up in case it may be of interest to authors!
