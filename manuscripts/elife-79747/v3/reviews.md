# Peer review - Round 1

Editors:
- Qiang Cui, https://ror.org/05qwgg493 Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79747.sa0](https://doi.org/10.7554/eLife.79747.sa0)

This study employs extensive MD simulations to probe the effect of phosphorylation of a tyrosine residue on the conformational ensemble of Ras GTPase. The insights form the basis for a screen of small molecule(s) that disrupt interaction with its target Raf kinase, and predictions are tested experimentally. Overall, the integrated approach is of interest to a wide range of biochemists and protein scientists and could potentially be used to modulate the activities of other proteins.


---

# Peer review - Round 1

Editors:
- Qiang Cui, https://ror.org/05qwgg493 Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79747.sa1](https://doi.org/10.7554/eLife.79747.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Inhibition of mutant RAS-RAF interaction by mimicking structural and dynamic properties of phosphorylated RAS" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and Jonathan Cooper as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Yuji Sugita (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The most essential revisions that the reviewers have suggested concern statistical error analysis of the simulation results, and correction of the computed free energy profile in Figure 9. Essentially all reviewers expressed major concerns about the correctness of the computed PMF, in terms of both the qualitative trend and quantitative values.

Reviewer #1 (Recommendations for the authors):

Overall, I think the simulations have been conducted properly and analyzed carefully. However, I have two major questions.

1. Foremost, the results in Figure 9 are potentially very confusing. The free energy scale here is several hundreds of kcal/mol, which is clearly not physical for the conformational rearrangement of the SwI motif. Second, even at a qualitative level, the PMF is downhill in nature without any obvious barrier. This is also largely unexpected. Finally, the downhill nature is less clear with the bound ligand, which doesn't readily explain how the ligand facilitates the conformational rearrangement in SwI as the authors claim. I think the PSP method is interesting but needs to be explained and discussed much more carefully, in terms of both qualitative features and quantitative values of the results.

2. On Pg6, the authors commented on the level of hydration of the γ phosphate in various protein variants, and suggested that a higher level of hydration can explain the higher level of intrinsic GTPase activity. This correlation is not immediately obvious to me, as the enzymatic activity is often inversely correlated with the level of active site hydration since a higher hydration level likely leads to higher reorganization energy and therefore a higher activation free energy barrier.

Reviewer #2 (Recommendations for the authors):

As I pointed out in the public review, I recommended the authors repeat the simulations a few times for improving the statistical significance and adding the errors. Also, I have several requests about the data presentations.

(1) In the distributions they showed in Figures (such as Figures 4C, 4D, 5A, 5B, and 5C), the curves are very smooth, lacking any noise. It seems to be unusual for me in MD simulations. I recommend the authors show the original data without smoothing, which is more natural for me (and readers).

(2) Clarification of structural figures is required. For instance, we can't see the green characters embedded in Figures 2E and 3B. Although the key residues are annotated in Figure 1A, I suggest the authors annotate key residues in other structural figures as well.

(3) PMF should be computed with enhanced sampling, such as umbrella sampling or metadynamics.

(4) More technical details are required in the Methods. Program package of MD simulation (Gromacs?) should be mentioned. I don't know which force field (AMBER of CHARMM, and which version) is used in the simulation.

Reviewer #3 (Recommendations for the authors):

The authors need to address the issues given in the public review by:

• Increasing their data range (at least five independent simulations in total) and/or proving convincingly that the data they collected is robust and the observed structural and dynamical effects are real. The most convincing way to do so is to include ensemble means and respective error bars in all distribution plots.

• Clearly stating which system (WT; pY32; G12D) has been simulated and how often for how much time.

• Showing data on the convergence of their results, e.g., RMSD plots of the protein backbone over time for the simulations.

• Either remove the PMF data completely or search for the pathways present in the data set (see the given article Jäger et al., J. Chem. Mol. Model. 2022) and analyze trajectories according to pathways. Additionally: how many independent pulling simulations did the authors perform? How long were these simulations?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Inhibition of mutant RAS-RAF interaction by mimicking structural and dynamic properties of phosphorylated RAS" for further consideration by eLife. Your revised article has been evaluated by Jonathan Cooper (Senior Editor) and a Reviewing Editor.

The manuscript has been substantially improved but there are some remaining issues that need to be addressed. In particular, as Reviewer #3 highlighted, it is important to clarify several technical details, especially concerning the PMF calculations.

Reviewer #1 (Recommendations for the authors):

The authors significantly expanded the scope of the sampling in their simulations, especially the steered MD simulations. The results are more sound and generally support the mechanistic picture that emerged from the study of the effect of phosphorylation. I think the revision is appropriate for publication.

Reviewer #2 (Recommendations for the authors):

In the revised manuscript, the authors addressed almost all the issues that I had been concerned about in the original one. In particular, a very large free-energy barrier in figure 9 was a big problem in the original manuscript. To resolve this, the authors added more "pulling simulations" to get converged the PMF as shown in the revised manuscript. Although this is a different approach than I suggested, the results are now reasonable and fine for me. I expect that this has involved their significant computations in additional molecular dynamics simulations and I appreciate their effort in the revisions.

I also suggested the authors to improve the methods section for telling the technical points more clearly. According to the modified sentences (highlighted in yellow), it looks now fine.

Overall, the revised manuscript has been improved greatly compared to the original submission. The authors satisfactorily addressed the questions and comments by reviewers.

Reviewer #3 (Recommendations for the authors):

While the authors have addressed some of my concerns, not all points have been sufficiently addressed and need additional revisions:

• The distributions in Figures 2a,b; 3a; 4c,d; 5; 7 and most of the histograms in the SI still are missing error bars. Please do the following: Calculate distributions of distances or angles for each simulation separately. Then calculate the mean distributions as a function of distance/angle, as well as the respective standard error of the mean. Display the mean distributions as lines, and the standard error of the mean as a shaded area.

• Steered pulling: The PMF in Figure 9 looks much better now – too good for my experience, actually, as only 70 simulations were used as input for a 2nd cumulant expansion of the Jarzynski identity. And especially the error bars are incredibly small. I do not understand how the block averaging procedure mentioned in the text should work here. Usually, error estimation with the 2nd cumulant approximation is performed based on Jackknifing or bootstrapping – what do the respective errors look like when using this approach? What are the pulling rates employed? How was the "pathway analysis" performed? On what criteria were trajectories kept or discarded? And: The insight that different paths cause erroneous free energy estimates is not "well known", as is currently described in the text, but rather new insight – please cite, e.g., Bray et al., J. Chem. Inf. Model. 2022, 62, 4591-4604. In general, I agree here with reviewer #2 who requested Umbrella Sampling calculations instead of the steered MD results given here.

• PCA: I do not find the answer to my question why only the first three eigenvectors were used convincingly. If the authors want to leave out the remaining eigenvectors that contribute the remaining 30% of cumulative eigenvalues, they need to provide evidence of why this is applicable. They could, e.g., plot free energies calculated from the simulation data along the eigenvectors and show for which eigenvectors the distributions are non-trivial, i.e., not following a normal distribution.
