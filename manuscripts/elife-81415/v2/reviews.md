# Peer review - Round 1

Editors:
- Yogesh K Gupta, https://ror.org/02f6dcw23 The University of Texas Health Science Center at San Antonio United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81415.sa0](https://doi.org/10.7554/eLife.81415.sa0)

This valuable paper is methodologically solid as it describes the first molecular dynamics (MD) simulation of the full-length membrane-bound Thyroid Stimulating Hormone Receptor (TSHR). This paper will be of interest to researchers working on thyroid biology and autoimmune disorders. This important set of new results also highlights dynamic conformational changes in the linker region (LR) and its interaction with the leucine-rich domain (LRD). While most claims are convincingly supported by the data and advance the understanding of TSHR, the experimental validation is currently incomplete.


---

# Peer review - Round 1

Editors:
- Yogesh K Gupta, https://ror.org/02f6dcw23 The University of Texas Health Science Center at San Antonio United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81415.sa1](https://doi.org/10.7554/eLife.81415.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Computational model of the full-length TSH receptor" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Carlos Isales as the Senior Editor. The reviewers have opted to remain anonymous.

Essential revisions:

Reviewers' comments are appended. Please address all comments raised by the reviewers.

Reviewer #1 (Recommendations for the authors):

Major weaknesses:

– Page 29 line 508: The authors claim that this is the first model of full-length TSHR, but citation 39 appears to be a full-length TSHR homology model (with noted differences in LR conformation). This manuscript does appear to be the first simulation of full-length TSHR, however. The manuscript would benefit from stating more clearly what is in this model that previous models are lacking and why that is significant.

– Page 7 line 88: This paragraph describes the choice of orientation for the starting model. This model was selected first by rotating the LRD-LR around the z-axis and selecting an orientation that minimizes the volume of the box necessary for running the simulation and maximizes the number of contacts between LR and TMD (which the authors acknowledge as inexact). While this choice of starting model is computationally efficient, it is not sufficiently rigorous. The initial model appears to contain the interdomain hydrogen bonds that the authors track in Figure 7, and it is unclear that these bonds would be found and maintained if the starting conformation of the model were different. It is also unclear whether the TSHR-TSH interactions reported in Figure 10 would hold with a different starting conformation. To address this concern, the paper would benefit from another set of calculations where this arbitrary orientation is changed to be outside of the 45{degree sign} window that is presented to validate that these results are not dependent on initial orientation. It may also be valuable to report the orientation that AF2 produces (see next comment).

– The authors used AF2 to determine the structure of the whole protein except for the Transmembrane domain (TMD), for which they had generated a model previously. How similar was the AF2 model of the whole protein to their model of two AF2 domains with the TMD? What does the TRIO model of the TMD give that an AF2 model of the TMD doesn't? AF2 has been shown to produce reasonable models of membrane bound proteins (Diego del Alamo, Davide Sala, Hassane S Mchaourab, Jens Meiler (2022) Sampling alternative conformational states of transporters and receptors with AlphaFold2 eLife 11:e75751); it would be an important addition if the authors could describe how/why AF2 cannot be used for this entire structure.

– It would be helpful if the authors could expand on the signaling mechanism mentioned in the last line of the discussion. This result and its mechanistic implications may be important in further studies (both computational and experimental) but it is barely discussed here.

– Page 8 line 106: MD parameters necessary to run the six-step equilibration protocol and production run should be reported.

– Page 10 line 156: This paragraph notes that many atoms clash and that the model requires further development. However, there is no mention of what was done to further develop the model. Any steps that were taken to further develop should be reported.

– Page 7 line 92: The authors should provide a rigorous definition of "mutually proximal". A distance threshold would be sufficient.

– Page 9 line 135: the X-Y distance is below what threshold for hydrogen bonds?

Reviewer #2 (Recommendations for the authors):

1. The authors should put more effort to provide clear, properly labeled and good quality figures.

a. There is no labeling of figures like N-, C- terminal of the protein in Figure 2.

b. In Figure 4a, its very difficult to read the color codes below the figure.

c. For fig6, I can hardly read the labels on y-axis.

d. There is typo in line 364. it should be 284 and not 384.

2. In Figure 1, the authors showed the enlarged LR showing various epitopes. What is the purpose of this?

3. The authors have used the pdb code 4AY9 for the structural analysis. They should also use sequence based analysis and find out whether the LR of TSHR and FSHR have anything in common. since this may give an explanation why the authors find that TSH makes contact with LR based on MD simulation but based on the FSH crystal data, no/weaker interaction exists.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Computational model of the full-length TSH receptor" for further consideration by eLife. Your revised article has been evaluated by previous reviewers, Carlos Isales (Senior Editor), and a Reviewing Editor.

The manuscript has been improved, but some remaining issues, as pointed out by Reviewer #2 need to be addressed, as outlined below:

1. While the authors did address many of my comments, I still think that the fact LR is disordered does not provide obvious mechanistic insights, and the simulations with the bound ligand are too preliminary to make solid conclusions. This was my #1 criticism, and the authors did not address it in their response; I didn't see it addressed in the manuscript either. To me, this is a fundamental oversight because readers will want to know the significance of these simulations. In my opinion, this significance is not spelled out clearly.
