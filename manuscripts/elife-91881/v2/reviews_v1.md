# Peer review - Round 1

Editors:
- Qiang Cui, https://ror.org/05qwgg493 Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91881.sa0](https://doi.org/10.7554/eLife.91881.sa0)

Using extensive atomistic molecular dynamics simulations, the authors analyzed the TCR/pMHC interface with different peptide sequences and protein constructs. The results provide important insights into the catch-bond phenomenon in the context of T-cell activation. In particular, the analysis points to convincing evidence that supports the role of force in further discriminating different peptides during the activation process beyond structural considerations.


---

# Peer review - Round 1

Editors:
- Qiang Cui, https://ror.org/05qwgg493 Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91881.sa1](https://doi.org/10.7554/eLife.91881.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Asymmetric framework motion of TCRαβ controls load-dependent peptide discrimination" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Qiang Cui as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) From a technical point of view, discuss carefully the choice of using a restraining approach vs. applying a steady force, and clarify which better mimics the realistic situation. In addition, the principal component analysis can be done differently to ensure the most meaningful comparison between different cases.

2) In terms of results, discuss more explicitly the specific features that discriminate between catch-bond and slip-bond regimes. It is also valuable to explicitly suggest a set of experimentally testable predictions from the simulation study.

Reviewer #1 (Recommendations for the authors):

1. I suggest that the authors discuss why they chose to restrain the TCR/MHC separation, rather than devise an algorithm to apply a steady force. The issue with the restrained distance is that the forces reported for the different mutants are quite variable, and one might even say, not consistent.

2. Uncertainty should be reported as the forces in some form, or the magnitude of their fluctuation.

3. (Table1) it might be interesting to check whether the integral of the force over the three extensions reported in the table correlates with the TCR/pMHC binding strength, if these data are available.

4. A few simulation observations either appear speculative or are not well illustrated, (e.g. on p5), "short distance between restraints … allows wider transverse motion that in turn generates a shear stress or a bending moment at the interface". Given the complexity of this large biomolecular complex and its dynamics, I suggest making a greater effort to distinguish between what is actually observed and what the implications might be.

5. While there are various analyses of the simulation data, it would strengthen the paper greatly if the authors could provide specific experimentally testable hypotheses, eg., in the form of predicted responses to a mutant peptide, or mutations to the variable chains that could alter the fluctuations (e.g. disulfide crosslinking).

Reviewer #2 (Recommendations for the authors):

In terms of presentation, I found the number and extent of data to be a bit overwhelming. If revising this paper, I hope the authors will consider trying to condense each figure to present a single message and summary panel and move data like how the number of contacts changes with time to the supporting information.

Reviewer #3 (Recommendations for the authors):

The authors have carried out a simulation study of the behavior of the TCR-pMHC complex for different peptides with and without load in the physiological range (10-20 pN). The load is calculated by applying harmonic restraints to the ends of the complex and extending their distances iteratively. The analysis of the complex under load seems to be novel.

Recommendations:

1) While the general conclusions regarding the load (e.g., higher number of contacts) seem to be supported by the simulations with different peptides, the conclusions regarding the different behavior of individual peptides (e.g., modified agonist vs. weak antagonist) are not fully supported as only one MD run was carried out for each peptide sequence and value of load. Multiple independent runs should be carried out for each simulation system, i.e., peptide and low/high load.

2) The definition of low and high load (Table 1) seems somewhat arbitrary as a low load of 13.2 pN and 14.9 pN is defined (from averaging over the 2nd half of the MD trajectory) for the WT peptide (full system and dFG, respectively) and these values are similar/higher than the high load of 13.5 pN of the P6A mutant.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Asymmetric framework motion of TCRαβ controls load-dependent peptide discrimination" for further consideration by eLife. Your revised article has been evaluated by Qiang Cui (Senior Editor) and a Reviewing Editor.

The manuscript has been substantially improved and the reviewers appreciated the revision, but there are some remaining issues that need to be addressed, as outlined below:

A new comment concerns the standard deviations of the forces that have been added. The std are quite variable between the various structures (varying from ~2.5A to ~12A). I wonder whether this variability is interpretable in terms of the proposed catch-bond mechanism.
