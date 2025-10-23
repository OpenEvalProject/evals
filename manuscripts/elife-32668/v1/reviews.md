# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32668.021](https://doi.org/10.7554/eLife.32668.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Linking time series of single-molecule experiments with molecular dynamics simulations by machine learning" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Arup Chakraborty as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: John Straub (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript describes a novel approach based on hidden Markov models to connect single-molecular FRET measurements with MD simulations, and application to the folding of formin-binding protein WW domain. The manuscript address two key issues in improving the validity of Markov state models used in protein folding studies, namely, 1) the construction of the discrete states, and 2) the construction of the continuous time Markov transition matrix T(\tau). Initially, discrete conformational states were obtained by clustering trajectory snapshots, and transition rates were then estimated from trajectories. To correct potential bias due to problems in the force field, the authors then used a hidden Markov model to model smFRET time series measurement and a) modified the discrete states and b) estimated the T(\tau) values between the discrete states so the smFRET is better explained. Indeed, the refined Markov state model can better account for the single-molecule time-series data: The improvement in reproducing the smFRET histogram of 50 uS as shown in Figure 3 is dramatic. It further revealed a different folding pathway of the WW-domain, as well as a different transition state ensemble.

The approach of using MD-derived MSM as basis and initial input for likelihood optimization with respect to smFRET data is very interesting and novel, and the calculations and uncertainty analysis were conducted carefully. The insight into the folding mechanism is very interesting. However, quite a few outstanding issues, including some serious concerns, remain to be addressed to assess whether publication is warranted.

Essential revisions:

1) An overall question about the current practice of Markov state models in MD-based protein folding studies. Assuming both simulation and experimental studies are under the same conditions (salt, dye, temperature, etc.), they are probing the same underlying physical process. Therefore, they should reflect the same ground-truth reality. As MD can provide atomistic details within the time scale of simulation, MD studies should provide far more details than smFRET. However, this is not the case. Rather, MD simulation cannot stand on its own, and needs to be corrected by smFRET. As described by the authors, the MSM is shifted before and after incorporating smFRET data. The authors showed that the discrete states are very different when smFRET data are brought into consideration. While it is not explicitly stated (please clarify), it seems that the refined Markov states are derived from the original Markov states by clustering of MD trajectories, but updated with new equilibrium probability (hence different bubble areas in Figure 2) and new transition rates. How can the ground truth, for example, equilibrium probabilities of the Markov states, change if it is examined one way (by MD) or another way (MD+smFRET)? This would suggest there is no objective ground truth that is accessible by current MD simulations.

Lending support to this conclusion, is the discussion you provided, that in other studies prior to this manuscript, the number of discrete states and the nature of these states are all malleable, depending on which metric one examines (RMSD or contact map). This would again suggest that there is no objective truth in determining what constitutes a set of discrete states that are Markovian and what their transition rates are. Rather, all depends on which metric and/or which additional experimental data one chooses to examine.

One cannot help but speculate: would one expect some other alternative discrete Markovian states different from the currently reported ones to emerge, when other types of experimental time series data other than \epsilon is incorporated. Is it likely that yet more different Markovian states, different dynamics of transition rates, different folding dynamics, and different transition state ensembles will be identified, all for the same WW-domain under the same condition (dye, pH, salt, temperature, if well controlled)?

This aspect of shifting ground truth in MD simulation and Markov state modeling is rather unsettling. A pessimistic, but not unreasonable, view is that without a principled approach in defining true reaction coordinates for protein folding one has to make do with rather ad hoc and heuristic approaches in defining the discrete states with unexamined consequences, and hence this unsettling aspect may be with us for a long while and the truth may be elusive.

Here is a suggestion in this respect: The authors employ Equation 5 for a model of FRET efficiency, however, more detailed models exist such as http://aip.scitation.org/doi/pdf/10.1063/1.3230974

The authors could evaluate their approach and determine if a more detailed model might be justified or needed in making contact with experimental measurements.

2) While concern 1 is more general, there is another question more specific to connecting MD and the smFRET measurements. It will be necessary for the authors to show how well the HMM learned T(\tau) conform with MD simulation generated T(\tau) after the refined discrete states are obtained, in a statistically significant way. For example, the authors should compare the HMM rates and the MD rates for the subsets of state-state transitions with the highest and relevant lowest rates among the 87x87 parameters. In addition, the flux and pathway analysis should also be carried out using MD-derived rates after the refined states are obtained by the HMM model, for key paths carrying most of the flux, and compared with the analysis using HMM rates. The authors may have already done some of these in the transition state ensemble analysis, and may already have all necessary data.

This is important for validating the connection between the sm-FRET (HMM modeling) time series and the MD trajectories the authors are proposing. It would be fantastic if all works out, as this would naturally suggest that in the future one no longer needs to do MD simulation. Rather, one could use smFRET to fit dynamic rates, as long as the discrete states can be obtained, for example, by some other means. However, one should be cautious about being overly optimistic here, as there are significant problems in the enormous search space of very high dimension. It will be very interesting if the authors can show that the HMM rates and MD rates after refinement are the same.

3) Potential over-fitting remains a concern, as there is a large number (87x87 = 7,569) parameters that need to be fitted. While the authors qualitatively compared results using each half of the data through plotting, it would be necessary to do some cross-validation tests, which are standard in machine learning. Specifically, the authors could use (n-1)/n balanced smFRET and MD data (e.g. similar number of folding trajectories) to identify refined states, and estimating \tau values, then test whether the remaining 1/n data falls within these defined states, and whether the unseen epsilon histograms can be reproduced accurately.

4) In Equation 5, the average values are used in calculating \epsilon. It seems that kappa has little difference at different regions of Q. Is the difference along the dimension of \epsilon that is used for clustering due to difference in distances r(si)? It will be helpful to also show both mean and variance of r(si) for each of the major discrete states, and justify whether the degree of in-cluster and between-cluster heterogeneity/homogeneity conforms to the Markovian assumption of each discrete state. This relates to the issue of validating the defined discrete states.

5) The calculations of FRET efficiencies from MD trajectories need to be stated explicitly. Furthermore, the estimation of FRET efficiencies from experimentally measured photon sequences also needs to be presently clearly. The latter in fact is a long-standing issue in the single-molecule community, for example, the time binning convention and the information-base binning by Haw Yang.

6) It is not obvious how the folding pathways were decomposed into individual pathways for both MSM models. How this procedure was conducted would critically impact the interpretation of results. This part thus needs careful and clear explanation.

7) Certain key references of interring dynamics from smFRET trajectories were missed in the context of this work, such as Haas et al., 2013.

8) Obtaining a solution of similar likelihood value starting from a random matrix is a bit worrisome. Can the authors elaborate more on how this model was ruled out? Furthermore, the convergence of likelihood optimization should also be discussed to reveal the robustness of this approach.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Linking time series of single-molecule experiments with molecular dynamics simulations by machine learning" for further consideration at eLife. Your revised article has been favorably evaluated by Arup Chakraborty (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Overview:

The unsettling aspects of shifting ground truth, or rather, the lack of ground truth remains. This is, however, an issue the community of protein folding simulations has to deal with.

Using Q as an adequate reaction coordinate is similarly problematic and inadequate, as Q is no substitute to reaction coordinates in the strict sense of earlier classic studies of Chandler and Dinner. But this again is a community problem, and we do not wish to specifically penalize the authors of the current work. Therefore, we accept the authors' arguments, although at least one of the reviewers had some fundamental concerns about the entire set of approaches in this area.

Specific points to address:

1) There is one issue that the authors did not provide answers to but they can easily do, namely, regarding the question of providing details of the 87x87 rates from the Hidden Markov model and the corresponding rates from MD simulation. It will be necessary to make first a general statement on how similar/different these two sets of matched/paired rates are, and second, provide details, e.g., in the Appendix, with side-by-side or overlaid histograms. If these two distributions are similar, it would be a comforting result. However, even if these two distributions do not agree, it will be important for readers to know this fact so they can directly draw their own inferences. This can be easily done with existing data.

2) A grammar and expression overhaul is highly recommended to enhance the readability of the work.
