# Peer review - Round 1

Editors:
- Richard A Neher, University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32035.034](https://doi.org/10.7554/eLife.32035.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "CRISPR-based herd immunity limits phage epidemics in bacterial populations" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom Richard A Neher is a member of our Board of Reviewing Editors and the evaluation has been overseen by and Arup Chakraborty as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Timothy Cooper (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript presents a mathematical model and a set of experiments examining how CRISPR-Cas mediated immunity to phage infection can result in herd immunity preventing the spread of the pathogen. The experiments are performed both in well-mixed liquid culture as well as in structured environments on agar. The critical herd immunity thresholds and the plaque radii follow model predictions as the parameters of the system as varied. All reviewers appreciated the elegant combination of experiments and theory, but we would like the authors to address the following points:

Essential revisions:

1) The system is set up such that resistant cells don't grow once infected. We would like to see the importance of this assumption discussed. How would model predictions change if cells kept growing? How important is rapid degradation of phage by resistant cells?

2) We would like to encourage the authors to move some derivations presented in Materials and methods section to the Results section. While detailed algebra is better kept in the Materials and methods section, additional mathematical details would help readers appreciate the theoretical results without having to jump back and forth to the Materials and methods section.

3) The experiments are started with a small inoccula which result in a broad crossover at the herd immunity threshold. Is the observed stochasticity consistent with that expected from a small founder population? Or are there additional sources of stochasticity? Would the transition in Figure 4C be sharper if larger inoccula had been used? What is the nature of the error bars in Figure 3 and Figure 4C? Do they quantify uncertainty in the parameter measurements or the stochasticity of the dynamics?

4) There is a sophisticated body of theory on pathogen spreading with long range jumps (e.g. Hallatschek and Fisher, 2014). Can you provide some intuition/discussion how the spreading and herd immunity thresholds change as dispersal goes from 2D diffusion to occasional long-range jumps ultimately to the well-mixed case?

5) It is mentioned in the Abstract that herd immunity might facilitate coexistence between susceptible and resistant variants. This possibility is mentioned again in the discussion in one sentence but not elaborated on. While it seems obvious that selection for resistant variants is reduced when the pathogen can no longer spread due to herd immunity, it is not obvious that this herd immunity results in stable coexistence. Resistant variants would still sweep to high frequencies in areas with high pathogen load. How would a cost of resistance change the model behavior?

The quantitative model the authors parameterized with experiments could be used to investigate many of these points in greater detail. If the model for example predicted the width of the cross-over at the herd immunity threshold correctly, such comparisons would increase confidence in both the model and the experimental system. Furthermore, the model could be used to assess robustness to assumptions like growth arrest and rapid phage degradation.
