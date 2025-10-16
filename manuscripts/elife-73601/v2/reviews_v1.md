# Peer review - Round 1

Editors:
- Rina Rosenzweig, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73601.sa0](https://doi.org/10.7554/eLife.73601.sa0)

This paper presents an elegant and multidisciplinary study combining state-of-the-art NMR with computational modeling methods, to characterize the effects of mutations on the structure and allosteric communication within the CRISPR-Cas9 system. In revealing the link between the allosteric network in the protein and the increase in CRISPR-Cas9 specificity, this study carries important implications for the design of new gene editing tools.


---

# Peer review - Round 1

Editors:
- Rina Rosenzweig, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73601.sa1](https://doi.org/10.7554/eLife.73601.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Enhanced Specificity Mutations Perturb Allosteric Signaling in CRISPR-Cas9" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Rina Rosenzweig as Reviewing Editor and José Faraldo-Gómez as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Ivaylo Ivanov (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) One significant concern raised by several reviewers is the lack of a direct comparison between the NMR studies and the MD simulations. This should be addressed in the revised manuscript.

2) The authors performed relaxation measurements for fast dynamics, however, they did not calculate the order parameters for the protein backbone. These should therefore be calculated and the authors should clearly indicate how the order parameters and heteronuclear NOEs compare to the calculated values from the MD trajectories.

3) There is no mention of figures 4B and 4C in the manuscript. The results presented in these figures should be discussed, and protein regions showing slow and fast timescale dynamics should be clearly indicated.

4) CPMG data were collected at multiple fields and the data analyzed, yet the analysis of these results was not presented. The authors should provide the kex and pbs obtained for these data, as well as indicate the changes between the wild type and mutant proteins. Do all the mutants populate the same excited state (as gauged from δ omegas)? How does this fit with the MD?

5) The effect of the mutants on the micro-to-millisecond timescale dynamics should be discussed. Additionally, it is unclear how the dynamics or structural perturbations caused by these selected mutants are converted into the enzyme's increased or decreased specificity.

6) The authors state that the differences in the relaxation dispersion profiles are less than 1.5 Hz, indicating small changes in dynamics. A Plot showing the differences in the relaxation dispersion profiles (ΔRex) should be provided for all the proteins (WT and mutants) to support this claim.

7) The authors have chosen to use Grubmuller's generalized correlation to compute the weights on the nodes of the protein network. Grubmuller's generalized correlation captures both linear and non-linear correlations. Indeed, you could run the linearized version to distinguish the non-linear from linear correlations. Would the results have been different if Pearson correlation was used? Conversely, would there be key allosteric residues picked up by generalized correlation and not by linear correlation?

8) When using the Girvan-Newman method to partition the network graph into communities, it is possible that the different simulation ensembles for the K855A, K810A and K484A mutants could result in different numbers of residues per community. In that case, it becomes difficult to compare the changes in betweenness for the mutants as there is also an accompanying shift in residues between communities. Could the authors please confirm that this is not the case and that each community contains the exact same number of residues for the K855A, K810A and K484A mutants.

9) Did the authors employ a modularity cutoff for the Girvan-Newman method to control community subdivision? And if so, was the cutoff the same for each of the three mutant cases?

10) In the discussion, the authors refer to the synchronous motions that may be responsible for specificity. How did they deduce that the motions are synchronous? From MD simulations or the global fitting of the CPMG curves? Do motions need to be synchronous for effective allosteric communications?

11) The authors state that mutations can target sites identified in this study (hotspots) to improve CRISP-Cas9 function. Can the authors elaborate more on this point? How do they envision the mutations could tune the function of the complex?

12) Generally, there appear to be a number of grammatical and stylistic issues with the manuscript. Revisiting the writing could serve to improve the readability of the article.

Reviewer #1 (Recommendations for the authors):

My area of expertise is molecular modeling. Therefore, I will constrain my comments mostly to the molecular modeling and computational aspects of the manuscript. I would appreciate if the authors address the following points in the revised version:

1. The authors have chosen to use Grubmuller's generalized correlation to compute the weights on the nodes of the protein network. Grubmuller's generalized correlation captures both linear and non-linear correlations. Indeed, you could run the linearized version to distinguish the non-linear from linear correlations. Would the results have been different if Pearson correlation was used? Conversely, would there be key allosteric residues picked up by generalized correlation and not by linear correlation?

2. When using the Girvan-Newman method to partition the network graph into communities, it is possible that the different simulation ensembles for the K855A, K810A and K484A mutants could results in different numbers of residues per community. In that case, it becomes difficult to compare the changes in betweenness for the mutants as there is also an accompanying shift in residues between communities. Could the authors please confirm that this is not the case and that each community contains the exact same number of residues for the K855A, K810A and K484A mutants.

3. Did the authors employ a modularity cutoff for the Girvan-Newman method to control community subdivision? And if so, was the cutoff the same for each of the three mutant cases?

Reviewer #2 (Recommendations for the authors):

The paper would benefit from clarifying the importance of the structural dynamics to the specificity of the CRISP-Cas9 function. Specifically, the authors should explain whether changes in the intra- and inter-molecular communication are linked to a defined step of the nuclease (i.e., substrate recognition? chemical step? On and off rates?).

Reviewer #3 (Recommendations for the authors):

Figure 4B and 4C are never mentioned in the article, which I believe speaks to a bigger issue with the manuscript – a lot of NMR data has been collected, but it is not being utilized; its main role is to support the MD, but it is doing so only superficially. What are supposed to learn from the R1R2 product? There does not seem to be the expected increase in R1R2 values corresponding to residues that exhibit exchange. A line depicting the average or better the expected value of R1R2 would be informative, as the reader could then be able to pick out regions with slow and fast timescale dynamics. How do the order parameters or heteronuclear NOE compare with the MD? These timescales are definitely covered by the length of the simulation and may be more informative of the allosteric network than the CPMG data.

CPMG data were collected at multiple fields and data analyzed, yet nothing about these results are presented; what were the kex and pbs for these data? Do all the mutants populate the same excited state (as gauged from δ omegas)? How does this fit with the MD? I'm not convinced that "the allosteric signaling is preserved" in the mutants, and pointing to the shape and number of curves as evidence is not sufficient (i.e., lines 179-182). It's not clear that the dynamics measured by CPMG are on the same timescale as those measured by MD, even with a 3.6 us simulation. Fast pico-to-nanosecond timescale dynamics may be more informative (see above). Nevertheless, the mutants are clearly altering the micro-to-millisecond timescale dynamics (e.g., K782, E827, E873). Again, this is hardly discussed. Only a short acknowledgement is made about the larger R2,inf for K855A. What is the case for this?

The overall conclusion of the MD analysis seems at odds. The mutants maintain the same allosteric network but alter the network somehow to affect specificity. The network analysis shows a loss in communication between two allosteric communities, what does this mean exactly (line 223)? How does this loss disrupt allosteric cross-talk between RuvC and REC2 (line225)? The mutants increase communication between non-allosteric sites; is the loss or gain of communication observed in the NMR relaxation data?
