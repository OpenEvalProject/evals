# Peer review - Round 1

Editors:
- Ben Cooper, Mahidol Oxford Tropical Medicine Research Unit Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40977.033](https://doi.org/10.7554/eLife.40977.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Inference and control of the nosocomial transmission of Methicillin-resistant Staphylococcus aureus" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ben Cooper as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Prabhat Jha as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Martin Bootsma (Reviewer #2); Lulla Opatowski (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This work makes both an important methodological contribution to the communicable disease modelling literature, and also an important practical contribution to the study of nosocomial infections. First, the authors develop a novel inference framework allowing inferences from individual based transmission models (overcoming computational problems with existing particle filtering approaches). Second, the methods are applied to make inferences about parameters for a multi-institutional MRSA outbreak across a network of hospitals in Sweden and simulations are used to show how such model-based inferences could translate into improved control measures for MRSA.

Essential revisions:

1) Clarification of exact nature of the MRSA data is needed. Does this only come from clinical infections or was there also screening on asymptomatic carriage?

2) Figure 1B is difficult to read and should be revised. Since only integers (0-5) are plotted, the continuous scale may not be the best choice and makes it difficult to pick out what numbers are being plotted.

3) Enough information needs to be presented to allow an interested reader to repeat this analysis on their own data. In particular, the following aspects of the methods were not clear to any of the reviewers:

i) In Algorithm 1, why is the discount factor raised to the power 2(l-1), rather than just (l-1). Is the 2 arbitrary?

ii) How should the discount factor a be chosen, and how do different values of a influence the algorithm? A value of 0.9 is used, but not explanation is given for this choice.

iii) Algorithm 1 returns the MLE of the parameter vector but makes no attempt to measure the associated uncertainty. Indeed, the variance of the parameter vector ensemble approaches zero as L increases. This is also seen in Appendix 1, Figure 4A. However, distributions for parameters are reported in Figure 3A, and the methods say that "parameter distributions become stable after 5 iterations…which means our choice of L=10 is sufficient". So how are the distributions in Figure 3A derived? Are these just taken from the ensemble of parameter vectors stopping after 10 iterations (implying that if L had been taken as 20 or more, the distributions shown in Figure 3A would have had much lower variance?) Surely it is important to produce not only point estimates, but also appropriate measures of uncertainty associated with these; it is not clear if this is being done and justification of the choice of L=10 in the data analysis (subsection “Inference using the actual diagnostic data”) compared with L=20 in the synthetic tests (subsection “Synthetic tests”) is lacking.

iv) In Algorithm 1 the actual EAKF step is not explained. Given that space is not a limitation (and technical details can be put int he appendix), it would be helpful to provide details of this EAKF step with sufficient detail to enable replication by the interested reader.

4) Clarification of model assumptions is needed. In particular, it is unclear whether the increased decolonization rate μ was only present during treatment, and that afterwards the spontaneous decolonization rate α kicks in, or whether treated patients keep their increased rate μ also after the treatment is stopped. Linked to this, what is the duration of treatment?

5) An explicit unambiguous description of the transmission process within a ward is lacking. Is the process density-dependent or frequency-dependent?

6) Units are missing in Table 1.

7) A table with all parameters estimates is missing.

8) Figure 5A-B legend is confusing as the y-axis doesn't seem to depict a reduction but cumulative incidence. Clarification is needed.

9) Can more formal assessment of model fits with synthetic and real data be provided in addition to the plots in Figure 2 and Figure 3?

10) Figure 5 and associated text: it is unclear whether the model based control measures uses only data/information that would be available at the time point control measures are put in place. If the inference approach instead uses information from the whole course of the epidemic, then this would be an unfair comparison. This needs clarification.

11) Subsection “Statistical test of power-law distribution”: "the significance level of 0.05" Following the recent ASA statement on the use (and misuse of p-values) there is a consensus that we should be striving to move away from such "bright lines". So fine to report the p-value, but we should try to avoid saying that. 049 is significant while. 051 isn't.
