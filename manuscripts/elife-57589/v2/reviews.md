# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, National Heart, Lung and Blood Institute, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57589.sa1](https://doi.org/10.7554/eLife.57589.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The value of this manuscript resides in its rigorous analysis and clear presentation of non-trivial methodological issues that are of relevance to all molecular simulation studies. It is anticipated that this work will serve a reference for the growing community of scientists using these types of computational methods.

Decision letter after peer review:

Thank you for submitting your article "On the importance of statistics in molecular simulations: thermodynamics, kinetics and simulation box size" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alan Grossfield (Reviewer #3).

The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission. In the interest of full transparency, the Senior Editor has decided to provide you with the reviewers' reports as received. As you will see, the reviewers have judged that your manuscript is of interest and potentially suitable for eLife. However, they also conclude that additional data and revisions to the text will be required before the manuscript can be accepted for publication.

Given this decision, I would like to draw your attention to the changes in the eLife revision policy that were made in response to the COVID-19 crisis (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option.

Reviewer #1:

The work by Gapsys and de Groot addresses the critical issues of adequate sampling and proper statistical analysis in molecular simulations, which are essential to provide a rigorous assessment and interpretation of the simulation results. Molecular simulations are necessarily performed on limited-size systems confined in a simulation box, typically under periodic boundaries and it is legitimate to investigate the implications of such finite-size approximation in conventional simulation setups.

In this work the authors analyze the effect of the simulation box size in different types of simulations and bimolecular systems, ranging from small test systems to more realistic biological molecules (i.e. hemoglobin), exemplifying in each case the possible shortcomings arising from sampling and statistical inaccuracies. In the case of hemoglobin, the authors propose rigorous statistical analysis to evaluate the trend of the transition times from T to R protein conformations as a function of the box size for different simulations repeats. This work report an extensive set of examples, is well written and appear very well done from the technical standpoint. Nonetheless in my opinion the manuscript requires a few revisions to improve the clarity of the presentation and to provide a better and more comprehensive fit with the current literature.

One of the main conclusions of this work is that beyond a reasonable threshold the box size does not affect the simulation outcome. While this has been clearly proven for the systems and observables investigated in this study, to provide a broader perspective it is important to mention clear-cut examples in which the effect of the finite box size must be taken into consideration to provide meaningful results and in some case could also lead to artifacts.

For the case of the alchemical calculations reported in the manuscript the authors should mention and discuss documented cases of inhomogeneous systems (e.g. when charges are generated) in which the periodic boundaries could lead to shifts in the calculated free energy unless a proper setup is utilized (Lin et al., 2014). One example of artifact that could be induced by the periodic boundaries is also reported in a previous study by one of the authors of this work (Hub et al., 2014). Another example is the significant system size dependence of the lateral diffusion of lipids (Klauda et al., 2006). Lastly, even for homogenous systems a box size dependence of the rotational diffusion of biomolecules has been recently reported (Linke et al., 2018).

A general question that I have pertains to the examples of Figure 1C and Figure 5C, in which the authors illustrate the anecdotal trends that could be obtained with limited statistics. It could be instructive in these cases to report additional controls that could be taken for assessing lack of statistics. In Figure 1C for example block analysis within each single repeat could already indicate that the reported trends as a function of the box size are not significant. In the case of Figure 5C autocorrelation analysis and/or block analysis could be used to assess the presence of correlations between the repeats (i.e. each single repeat is not equilibrated). Another possibility is to compare the results with a Markov Model analysis, such as TRAM (Wu et al., PNAS June 7, 2016 113 (23) E3221-E3230) or DHAM (Stelzl et al., J Chem Theory Comput. 2017 Dec 12;13(12):6328-6342) that should better handle non equilibrated samples.

I report below more specific clarifications/improvements that need to be addressed.

In the application to the Gb protein the authors compare their results to the work of Asthagiri and Tomar. Here the explicit comparison must be clarified; Asthagiri and Tomar also report a thermodynamic integration calculation to estimate the charging free energy of Gb which is (consistently with this work) box size independent. The box size dependence emerges when using the quasi chemical theory (e.g. to analyze the specific components). Additionally, the charging free energy reported by Asthagiri and Tomar doesn't seem consistent with the values reported in this work.

The Discussion section is more a result section about water diffusion, my suggestion is to move this section in the results and provide an actual discussion, e.g. expanding the Conclusions by including the considerations reported above.

Reviewer #2:

General assessment:

This paper aims to present a methodical demonstration of the importance of obtaining complete sampling statistics from MD simulations for the purpose of estimating thermodynamic or kinetic quantities. As a test case, the authors apply this demonstration to the hypothesis that solvent periodic box size affects the simulation-derived thermodynamics and kinetics of biomolecules. This work is statistically rigorous and provides a clear comparison between results obtained with insufficient sampling and those derived from more extensive sampling. This paper can serve as a good reference for future scientists employing MD simulations who want to make sure their sampling is adequate based on proper statistical methods.

Major comments:

1) The authors show that increased simulation time per window (50 ns instead of 2.5 ns) along the dihydrofolate reductase M20 loop motion reaction coordinate results in indistinguishable PMF profiles by box size. The authors attribute the discrepancies observed when using 2.5-ns sampling times to insufficient equilibration away from the initial structure, as 2.5 ns is not sufficiently greater than the autocorrelation time of the loop motion. While this is a very plausible explanation, the conclusion would be strengthened by explicit calculation of the reaction coordinate autocorrelation time. This is particularly important to include as an example to other scientists who would like to estimate how long their independent simulations need to be to avoid biased estimates that are caused by using the same initial structure.

2) For the kinetics analysis it would be helpful to include more information, including equations or a reference to the appropriate equations, to show how the rate constants and uncertainty were calculated in detail using the frequentist approach. In particular, it is not clear how the trials that did not exhibit any transitions for hemoglobin were accounted for in the calculation of the T state halflife.

Reviewer #3:

I think this is a timely, important, and well-executed study that will be a valuable resource to the community. Insufficient sampling has been the bane of bimolecular simulation since its inception 40 years ago, and this paper is largely framed as a rebuke to a recent, high-profile example.

My biggest complaint with the paper as it stands is not with the work, which is excellent, but with the lack of details in the presentation. As I see it, the real value in this manuscript isn't beating up on a bad paper, the authors already accomplished that, but in teaching the community how to do things better. The paper covers a truly enormous scope, arguably, 3-4 paper's worth, and as a consequence doesn't include all of the details needed to understand their arguments. Most of the information is available in the references, or in the code they distribute (another excellent choice on their part), but to really maximize the didactic value of the paper I think more of the explanation has to be in the main body of the paper. For example:

1) They never said what enhanced sampling method was used in the DHFR calculations, or what the collective variable was. It sounds like umbrella sampling, but they weren't explicit.

2) Figures 8-10 on the kinetics of hemoglobin. There's no real explanation of what they did to generate any of these figures. The error bars in Figure 8 aren't defined, nor is how they were calculated. I'm assuming they did bootstrapping, with different sample sizes, but it should be stated explicitly. It's interesting that the standard errors in Figure 8B are larger for the smaller box, but the authors don't comment on why.

3) Figure 9: there are 2 curves in each panel, presumably one for each prior, but which is which is not stated. In the top right panel, there's only 1 curve, with no explanation. Given that the paper is mostly intended as a teaching tool, I think a brief summary of the Ensign and Pande theory would be helpful, as would an explanation for why you would use to two different priors.

4) Figure 10: You have to read pretty far into the caption before you realize the data which shows 2 distributions is artificial, to prove a point. No details are given to explain how this was done, in the caption or the body of the paper. The authors should either leave it out or provide those details.

5) Very few details are given about the alanine dipeptide calculations.

6) When discussing the protein solvation calculations, the final conclusion (that the appropriate approach to eliminate box-size dependence in vacuum is to use no cutoff at all) is very reasonable, but the data should be shown.

Despite my somewhat lengthy list of complaints, I want to re-emphasize that I think this is an outstanding paper.
