# Peer review - Round 1

Editors:
- Hayriye Cagnan, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84135.sa0](https://doi.org/10.7554/eLife.84135.sa0)

This important study advances our understanding of Parkinson's by identifying micro and macro scale signatures linked to critical symptoms (e.g., tremor and slowness of movement), and effective motor control. The evidence supporting the conclusions is solid, and leverages a rich dataset obtained during naturalistic movement. The work will be of interest to neuroscientists, neurologists, and biomedical engineers.


---

# Peer review - Round 1

Editors:
- Hayriye Cagnan, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84135.sa1](https://doi.org/10.7554/eLife.84135.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Concurrent Decoding of Distinct Neurophysiological Fingerprints of Tremor and Bradykinesia in Parkinson's Disease" for consideration by eLife. Your article has been reviewed by 3 peer , one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Tamar Makin as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Wolf-Julian Neumann (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Reviewers all agree that the work is interesting and beneficial, however, there are several aspects that the authors should address:

1) Clarifying how behavioural measures (tremor, slowness) were derived, and how these relate to clinical scores. The authors should also support their analysis choices such as normalisation of cursor speed and derivation of effective motor control;

2) Analysing sub-thalamic and cortical recordings together to explore connectivity and coupling measures;

3) Clarifying how multiple recordings from each subject have been dealt with for decoding and using R2 as a performance metric.

Reviewer #1 (Recommendations for the authors):

I enjoyed reading this manuscript and think it will be a valuable contribution to a number of research fields following a revision.

1) The manuscript would significantly improve if the authors provided additional information regarding their methods and reorganised their results.

A) How did the authors compute tremor amplitude probability densities in age-matched controls and patients who did not exhibit tremors? Panels 1B and C linked to tremor analysis are difficult to read – did most patients and controls have no tremor and therefore the density functions are decaying from 0 or is there a low amplitude peak?

B) What was the motivation for normalising cursor speed to its minimum and maximum and what are the implications of this normalisation when comparing speed within and across participants?

C) I am not entirely sure how useful age-matched control behaviours are to understanding the main results of the paper – the authors could consider removing these to streamline the Results section.

D) Could authors further clarify the analysis using FWHM to delineate periods of time where metrics were sustained above control levels?

E) the authors start referring to effective motor control in figure 2 but the description appears later in the paper; re-organising figures 2 and 3 would improve readability.

2) If ECOG and STN recordings were acquired simultaneously, how did signals in both structures co-vary? Would considering envelope – envelope, phase – phase, envelope – phase information improve decoding beyond what can be achieved from a single recording site?

3) In the discussion, the authors state that their model supports "tremor related oscillations originating in the STN and propagating to cortex" – what is the evidence for this in the manuscript?

4) Could the authors further discuss how their full spectrum decoder may be implemented in the future for DBS control taking into account device and real-time processing constraints?

5) Could the authors further discuss how tremor/slowness/effective movement decoding from micro-electrode recordings reflect overall activity levels of units (in particular those linked to higher frequencies (γ high and hfo)) (Figures 3 and 4)?

Reviewer #2 (Recommendations for the authors):

Thank you for inviting me to review this interesting study. This is an amazing paper, that I read with enthusiasm. I am not sure why the authors have chosen to neglect all brain signal decoding papers in the field of deep brain stimulation, perhaps they were afraid that this would diminish the novelty. I personally think that the paper and results are sufficiently novel and the paper would have further gained from a thorough discussion of the current field (for review from our group see Merk et al., Exp Neurol 2022; https://doi.org/10.1016/j.expneurol.2022.113993 ; I do not aim to get this paper cited, just want to provide some inspiration).

Reviewer #3 (Recommendations for the authors):

There are a few questions and suggestions that would strengthen the overall conclusions of the manuscript.

The approach they use to obtain high-density recordings of the STN involves first driving the microelectrode to the bottom of the STN, and then in an automated fashion and based on the length of the recording track, incrementally and automatically moving the microelectrode dorsally, interleaving experimental sessions at each increment, until the top of the STN is reached. This is a nice approach for mapping the entire STN. However, there are two questions. First, as far as I understand, the microelectrodes used will have a larger macro electrode contact 3mm dorsal to the microelectrode tip. This means that any tissue that lies 3mm to the most ventral aspect of the recording will be damaged by the larger macro contact. If the recording span of the STN is larger than 3mm, then some microelectrode recordings will be in this damaged region. How do the authors account for this, and would it make sense to discard data that is obtained >3mm dorsal to the dental STN border? Second, different recording tracks may have different lengths and spans. Which recording track is used for this process? As they note, not all the electrodes, therefore, recorded data from the STN, and so the question is whether it would make sense to discard these non-STN recordings.

Tremor amplitude is quantified as the magnitude of the 3-10 Hz filtered signal. How is this converted to a tremor score that is then used for effective motor control? In addition, effective motor control appears to be simply the average of the (effective) tremor and slowness scores. However, the simple average may be misleading as a very good score in one domain could potentially compensate for a poor score in the other. Had the authors instead considered using an effective motor control score that is the minimum of either the tremor or slowness effective scores (1 – their value)? On a related note, the authors convert cursor speed to slowness by normalizing within the session. But should they instead normalize within subjects?

Figure 2 could be presented more clearly. For example, there are no scale bars in 2A, and panels B, C, and D are all different sizes for example.

For figure 3, the authors use decoding models to compare the decoding of tremor to the decoding of slowness to determine which spectral features can distinguish between the two categories and between each category and effective motor control. This is a nice analysis. Interestingly, there is a difference in these features between micro and macro recordings, and the macro electrode features appear somewhat similar to the motor cortex ECoG recordings. Is there a reason this should differ from the micro features? More interestingly, is there a possible link between the macro STN recordings and the ECoG recordings? Have the authors investigated any measures of coupling or connectivity between the two regions?

There are multiple experiments performed at different depths throughout the STN in each subject. It is not clear to me, and I am sure the authors have addressed this point, but when constructing the LLMs, there is included a factor for the subject. However, are all experiments or trials recorded within the same subject considered as independent samples? Could one subject's data be driving these significant regression coefficients?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Concurrent Decoding of Distinct Neurophysiological Fingerprints of Tremor and Bradykinesia in Parkinson's Disease" for further consideration by eLife. Your revised article has been evaluated by Tamar Makin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1) Could the authors please (a) clarify patients' and control subjects' limb position/posture during the behavioural task; (b) indicate that Louis et al. 2001 observed a relation between Parkinson's rest and action tremor when the UPDRS rest tremor sub-scores and the Washington Heights-Inwood Genetic Study of Essential Tremor Rating Scale were correlated; and (c) discuss why in this study there is a deviation between UPDRS rest tremor sub-score and tremor severity on task vs UPDRS kinetic tremor sub-score despite the previously reported relationship between the two (Louis et al. 2001).
