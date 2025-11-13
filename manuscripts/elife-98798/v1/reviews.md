# Peer review - Round 1

Editors:
- Bin Zhang, Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98798.3.sa0](https://doi.org/10.7554/eLife.98798.3.sa0)

A combination of molecular dynamics simulation and state-of-the-art statistical post-processing techniques provided valuable insight into GPCR-ligand dynamics. This manuscript provides solid evidence for differences in the binding/unbinding of classical cannabinoid drugs from new psychoactive substances. The results could aid in mitigating the public health threat these drugs pose.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98798.3.sa1](https://doi.org/10.7554/eLife.98798.3.sa1)

This manuscript presents insights into biased signaling in GPCRs, namely cannabinoid receptors. Biased signaling is of broad interest in general, and cannabinoid signaling is particular relevant for understanding the impact of new drugs that target this receptor. Mechanistic insight from work like this could enable new approaches to mitigate the public health impact of new psychoactive drugs. Towards that end, this manuscript seeks to understand how new psychoactive substances (NPS, e.g. MDMB-FUBINACA) elicit more signaling through β-arrestin than classical cannabinoids (e.g. HU-210). The authors use an interesting combination of simulations and machine learning.

The caption for Figure 3 doesn't explain the color scheme, so its not obvious what the start and end states of the ligand are.

For the metadynamics simulations were multiple Gaussian heights/widths tried to see what, if any, impact that has on the unbinding pathway? That would be useful to help ensure all the relevant pathways were explored.

It would be nice to acknowledge previous applications of metadynamics+MSMs and (separately) TRAM, such as Simulation of spontaneous G protein activation... (Sun et al. eLife 2018) and Estimation of binding rates and affinities... (Ge and Voelz JCP 2022).

What is KL divergence analysis between macrostates? I know KL divergence compares probability distributions, but its not clear what distributions are being compared.

I suggest being more careful with the language of universality. It can be "supported" but "showing" or "proving" its universal would require looking at all possible chemicals in the class.

Comments on revisions:

The authors provided appropriate responses to the comments above.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98798.3.sa2](https://doi.org/10.7554/eLife.98798.3.sa2)

Summary:

The investigation provides a computational as well as biochemical insights into the (un)binding mechanisms of a pair of psychoactive substances into cannabinoid receptors. A combination of molecular dynamics simulation and a set of state-of-the art statistical post-processing techniques were employed to exploit GPCR-ligand dynamics.

Strengths:

The strength of the manuscript lies in usage and comparison of TRAM as well as Markov state modelling (MSM) for investigating ligand binding kinetics and thermodynamics. Usually MSMs have been more commonly used for this purpose. But as the authors have pointed out, implicit in the usage of MSMs lie the assumption of detailed balance, which would not hold true for many cases especially those with skewed binding affinities. In this regard, the author's usage of TRAM which harnesses both biased and unbiased simulations for extracting the same, provides a more appropriate way-out.

Weaknesses:

(1) While the authors have used TRAM (by citing MSM to be inadequate in these cases), the thermodynamic comparisons of both techniques provide similar values. In this case, one would wonder what advantage TRAM would hold in this particular case.

(2) The initiation of unbiased simulations from previously run biased metadynamics simulations would almost surely introduce hysteresis in the analysis. The authors need to address these issues.

(3) The choice of ligands in the current work seems very forced and none of the results compare directly with any experimental data. An ideal case would have been to use the seminal D.E. Shaw research paper on GPCR/ligand binding as a benchmark and then show how TRAM, using much lesser biased simulation times, would fare against the experimental kinetics or even unbiased simulated kinetics of the previous report

(4) The method section of the manuscript seems to suggest all the simulations were started from a docked structure. This casts doubt on the reliability of the kinetics derived from these simulations that were spawned from docked structure, instead of any crystallographic pose. Ideally, the authors should have been more careful in choosing the ligands in this work based on the availability of the crystallographic structures.

(5) The last part of using a machine learning-based approach to analyse allosteric interaction seems to be very much forced, as there are numerous distance-based more traditional precedent analyses that do a fair job of identifying an allosteric job.

(6) While getting busy with the methodological details of TRAM vs MSM, the manuscript fails to share with sufficient clairty what the distinctive features of two ligand binding mechanisms are.

Comments on revisions:

The authors have addressed most of the queries of the reviewer in an adequate manner. However, The current code availability section just provides the link to Python files to generate the plots. It is not very useful in its current form. The code availability section should provide a proper GitHub page that shows the usage of TRAM for the readers to execute. While Pyemma has been cited for TRAM, a python note book to reproduce the TRAM would be very instructive.
