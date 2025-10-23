# Peer review - Round 1

Editors:
- Richard P Harvey, Victor Chang Cardiac Research Institute Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73325.sa1](https://doi.org/10.7554/eLife.73325.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Personalized Computational Heart Models with T1-Mapped Fibrotic Remodeling Predict Risk of Sudden Death Risk in Patients with Hypertrophic Cardiomyopathy" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Balram Bhargava as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Colleen E Clancy (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please address all of the methodological clarifications addressed by Reviewer 1.

2) Please address all of the conceptual issues raised by Reviewer 2 in the Results/Discussion where appropriate, and more specifically in the Limitations section. Please address the first point in the Recommendations for the Authors section if possible.

Reviewer #2 (Recommendations for the authors):

This is a well written manuscript that describes novel work. However, there are some underlying concerns that should be addressed in a revised manuscript.

1. There is no evidence in the manuscript that the simulated electrical activation and recovery in the models bears any relation to electrical activation and recovery in the patients' hearts. Of course this evidence is difficult to obtain in detail unless the patients undergo electrophysiology study. However, if it were possible to compare some features of a simulated ECG signal with real recordings from the patient group, and demonstrate that the models show features consistent with HCM (changes to Q wave, ST segment and T wave) then this would give confidence in the utility of the model.

2. It is possible that the electrophysiology model is not needed to predict arrhythmia risk, and that it is the distribution of diffuse and focal fibrosis that is important. The authors have addressed this question to some extent in Figure 2, but I suspect that it is the shape and position of diffuse fibrosis that is important, not the total amount present.

3. If this is the case, then it may be that a machine learning approach based on imaging alone may be as good as, and quicker than, the model for risk assessment. The authors should consider this possibility.

4. Although the patient data used in this study will be made available on reasonable request, I would encourage wider availability of the patient specific meshes as well as analysis and simulation codes in line with other groups.

Comments on writing and presentation:

The abstract and introduction are both written using very technical language that may not be appropriate for the more general readership of eLife. Please consider including a more accessible paragraph that sets the scene for the non-expert.

The data shown in Figure 4B are not suitable for linear regression because the number of unique VA morphologies is a categorical not a continuous variable. To make an inference from these data (which may be highly questionable in any case), please choose a more suitable method.

Reviewer #3 (Recommendations for the authors):

The methodology used here is sound and has been well tested by this group. One aspect of this study that should perhaps be highlighted in the Discussion is whether in the absence of a simulated approach as used here, would it be possible to unequivocally link diffuse fibrosis with ventricular arrhythmias based on computational approaches alone?
