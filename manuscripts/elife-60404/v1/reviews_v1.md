# Peer review - Round 1

Editors:
- Sebastian Deindl, Uppsala University Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60404.sa1](https://doi.org/10.7554/eLife.60404.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

DeepFRET, a new deep learning-based platform for standardized, automated, and unbiased single-molecule FRET data analysis, has great potential to lower the threshold for smFRET expertise, allowing for a greater number of scientists to take advantage of this powerful technique.

Decision letter after peer review:

Thank you for submitting your article "DeepFRET: Rapid and automated single molecule FRET data classification using deep learning" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Sebastian Deindl as the Reviewing Editor and Suzanne Pfeffer as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Shixin Liu (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

A major bottleneck in many single-molecule FRET experiments is the need to sort through and classify the single-molecule time traces in order to separate the good traces in an experiment from ones that contain artifacts. In this work, Thomsen et al. describe a new platform for standardized, automated, and unbiased single-molecule FRET data analysis. The software is based on deep learning and is intended to act as the sole tool required to go from smFRET data acquisition all the way to quantitative analyses and publication-quality figure production. Rapid and automated analysis is enabled following a single user-input parameter (quality threshold), ensuring minimal user intervention in the data analysis process. A user-friendly GUI is provided to further simplify analysis. Importantly, the platform is open source written in Python, so users may adjust the code for their specific needs.

If successful, this platform could lower the threshold for smFRET expertise, allowing for a greater number of scientists to take advantage of this powerful tool. However, in its current form the manuscript could benefit from important clarifications to convince the readers of the novelty and superiority of this platform compared to the numerous previously published smFRET data analysis software packages. One weakness of the validation is that it was done only on a single real data set from one experiment performed by their lab.

Essential revisions:

1) It is unclear how pre-training the model can account for the infinite possible FRET states/lifetimes/occupancies/transition pathways/noise etc. How can this not bias the results to look for traces that are similar SNR etc. to the training data? For example, the 0.2 max probability of transition between states in the training dataset could bias analysis toward long-lived FRET states. The authors should comment on this.

2) Comparison of DeepFRET to human accuracy in picking "clean traces" does not seem to be an appropriate comparison (and is obviously faster). Manual trace selection is generally no longer a standard means to analyze smFRET data given the freely available open-source automated alternatives (e.g. HAMMY, ebFRET, SPARTAN, etc.). The comparison to other available software packages is important to convince users of the superior or at least equivalent performance of DeepFRET in automated trace selection. The authors should include such a comparison in the revised version of the manuscript.

3) Along the same lines, a better way to prove DeepFRET's trace analysis power is to take several datasets and compare analyses from HAMMY, ebFRET etc. vs. DeepFRET. The authors should include such comparative analyses on more than one dataset in the revised version of the manuscript.

4) It would be helpful if, in the Discussion section, the authors could provide a discussion of the tool's limitations. A discussion that talks about cases where their tool might fail would be useful for researchers who want to use their tool or build upon it. For example, in the discussion, the Materials and methods section notes that photophysical effects that are sometimes observed in smFRET experiments can be problematic for the method (it seems like the tool would likely classify these as non-useful traces even though they might reflect the "true" signal from the experiment [e.g. observation of PIFE in work from TJ Ha's group]).
