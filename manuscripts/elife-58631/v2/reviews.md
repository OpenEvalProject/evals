# Peer review - Round 1

Editors:
- Arduino A Mangoni, Flinders Medical Centre Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58631.sa1](https://doi.org/10.7554/eLife.58631.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your work provide useful insights regarding potential safety issues to be considered in studies investigating the role of chloroquine and hydroxychloroquine in several disease states, particularly COVID-19.

Decision letter after peer review:

Thank you for submitting your article "Concentration-dependent mortality of chloroquine in overdose" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Matthias Barton, MD, as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Nick Holford (Reviewer #1); Karen Barnes (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper describes a modelling and simulation project which utilises a mixture of data-sets to predict the likely concentrations (total blood) from the currently recommended hydroxychloroquine (HCQ) (chloroquine (CQ)) dose regimens for COVID-19.

Essential revisions:

The NONMEM simulation code could not be found in the list of contents of the GitHub site. When searching for NONMEM in the Rmd file it does not appear. Please provide full details on how to access the PK modelling used.

Subsection “Pharmacodynamic modelling”: Please describe the model used to simulate the PK profile in order to obtain peak concentrations.

As not all regimens could be tested in the model, it would be highly informative to have the loading, maintenance and duration of dose used in the ~90 registered clinical trials summarised in a supplementary table. This would clarify how the wide range of chloroquine dosages currently being used relate to dosages modelled in terms of predicted exposure and mortality risk. This is needed to support the Impact statement that "Most chloroquine regimens trialled for the treatment of COVID19 will not result in life-threatening cardiovascular toxicity".

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Concentration-dependent mortality of chloroquine in overdose" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Essential revisions:

– Introduction: The term "weak" is used again but without an explanation of what it means. The authors should state as they have in the response to my original comment, that antiviral effects are expected to be small because predicted unbound concentrations of CQ in vivo are lower than those than the C50 reported for in vitro cell culture anti-viral effects.

– You continue to describe volumes as enormous without any reference to support these assertions. As I have pointed out it is not possible to reliably estimate such large volumes and long terminal half lives. The volumes of distribution in the 2 models you have used for whole blood (Vcentral 468 L/52 kg and Vperipheral of 1600 L/52 kg) and for plasma (Vcentral 2020 L/61.9 kg, Vshallow 6740 L/61.9 kg and Vdeep 3270 L/61.9kg are not 200-300 L/kg as you state in your response. These commonly cited 100s of L/kg values in the literature has been uncritically repeated by others and you should not make the same mistake. You have 2 adequate PK models which you can use to give more reasonable estimates of volumes and terminal half-life.

– Note that it is not helpful to standardize these 2 models to different weights (52 kg, 61.9 kg). The fit of the data is not affected by using a common standard weight e.g. 70 kg (1). Using a standard weight allows different studies to be compared much more easily (2).

– Response to my comments about peak concentrations. It is still not clear to me how you claim to estimate peak concentrations using a latent variable. You say you did not a published PK model so what PK model did you use?

– Please also answer my question about why you did not use the observed concentrations for a logistic regression or time to event analysis. That would avoid the problem of trying to predict a peak concentration.

– The description of the two NM-TRAN code files refers to a QRS model but these files only describe CQ concentrations and not QRS. The descriptions of these files should be changed or provide files which include CQ and QRS code.

– The comments for $Σ in the two NM-TRAN code files should be corrected.

– Hoglund_wholeblood_CQ_mod, Line 101 says simulation is without residual error but $Σ is not zero. However, it is close to zero and thus the residual error will be small.

$Σ 0.00001 ;Simulation without residual error.

– Pukrittayakarnee_plasma_CQ.mod, Line 118 says simulation is without residual error but $Σ is not zero (SD=0.64 mg/L) so there will be residual error in the predicted concentration. $Σ 0.0806 ;Simulating without residual error.
