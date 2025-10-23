# Peer review - Round 1

Editors:
- Hugo Merchant, https://ror.org/01tmp8f25 National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76489.sa0](https://doi.org/10.7554/eLife.76489.sa0)

This article will be of interest to scientists studying the contribution of motoneuron behaviour to motor control as well as anyone interested in the relation between neuron morphology, intrinsic properties, and neuron behaviour. The authors have distilled decades of research on motoneuron properties into a set of mathematical relationships that can guide both experimentalists and modellers interested in developing realistic models of populations of motoneurons. In fact, Caillet et al. present a data-driven regression analysis to infer the relationships between morphological and electrophysiological measures from spinal motor neurons in different animal species. Finally, the authors emphasize the value of this approach, but also carefully consider its limitations, including inter-study variability and limited sample sizes in the experimental datasets used to derive the relationships between multiple intrinsic properties.


---

# Peer review - Round 1

Editors:
- Hugo Merchant, https://ror.org/01tmp8f25 National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76489.sa1](https://doi.org/10.7554/eLife.76489.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Mathematical Relationships between Spinal Motoneuron Properties" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Barbara Shinn-Cunningham as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Randall K Powers (Reviewer #2); Leonardo Abdala Elias (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The format of the paper should follow the structure of eLife. The legend of Figure 1 should describe very explicitly the steps used to create the final size-related datasets, maybe giving an example. The circles and symbols in Figure 2 should be larger.

2. The Introduction should be more inclusive and respectful with previous studies. It is unfair to state that some inferences are "speculative" since some authors provide linear regression curves (Eccles et al., 1958, for instance) while others consider the theoretical analysis by Rall. Also, when mentioning computational models, since the present study is focused on motor neurons, consider citing the extensive literature on models of motor neurons (see p. 3, l. 51 and 52).

3. In both Intro and Discussion, the authors should be careful when declaring the relevance of the current study. Several statements cannot be supported by analysis, for example, the comments that the method "can accelerate future research in the behaviour of individual MNs" and that mathematical equations can be scaled "to estimate the MN property values that cannot be measured in humans in vivo". How can you scale the equations without prior information on human motor neuron electrophysiology and morphology?

4. The methods section could be expanded to explain some of the measured electrophysiological properties in more detail. Most of the direct measurements (ACV, AHP duration, RN, Ith) are fairly straightforward, with the possible exception of time constant (see comments in Public Review). However, the derived measurements need to be explained in the Methods section. Both estimates of specific membrane resistivity (Rm) and whole cell capacitance (C) can be estimated using an equivalent cable model of the motoneuron along with an estimate of electrotonic length, and the formulas for these should be stated (see Ulfhake and Kellerth, Brain Res, 1984 equations 2 and 3 and Gustafsson and Pinter, JPhysiol, 1984a, equation 1). It should be mentioned in Methods that whole cell capacitance can be used as an estimate of cell surface area by assuming a value for specific capacitance of 1 microF/cm2 and that these area estimates are roughly in line with direct measurements although they tend to be a bit high (see Figure 6 of Gustafsson and Pinter 1984a).

5. Data used in the analysis are both from in vivo and in vitro recordings, not exclusively from in vivo experiments as declared in several parts of the manuscript (e.g., Abstract). Morphometric data cannot be recorded in vivo.

6. The authors should revise their method to include some information on data variability. A simple way is to provide the confidence interval of the regression. In this case, all parameters of the mathematical equations will have a range (95% confidence interval). The values provided in the current manuscript are only average values.

7. It is not clear why the authors used a 70-30% scheme for crossvalidation and why only 5 validations were performed. A larger set of validations are probably needed and at least another training-testing proportion should be carried out.

8. Tables 4, 5 and 7 could be moved to the Supplementary material section.

9. In the merged data sets shown in Figure 4 it would be useful to use different symbols for each data set (i.e., different symbols for {AHP;Smn}1 and {AHP;Smn}2).

10. There is no oval box with fc(C) in Figure 1. Please, revise. Also, consider changing Figure 1 with a pseudo-code of the algorithm to improve clarity.

11. Ith was estimated using different approaches in the selected studies. Some studies have used triangular-shaped currents, while others used step currents. How would different methods for estimating similar parameters influence your analysis (inter-study variability)?

12. Some relations are not unexpected. The proportional relation between cell capacitance and cell size is obvious. Again, you should consider previous theoretical studies based on Rall's theory.

13. The authors should provide more clear evidence on how the proposed method should be translated to future studies on synaptic integration. Since the analysis did not consider any active property, I am not confident that the mathematical relations can help a more comprehensive computer simulation study.

14. Please use ACV or CV, not a mixture of both abbreviations.

15. The section on specific resistance (starting on Line 536) should be expanded to consider the fact that specific resistance may be different in different parts of the neuron (see Public review comments). This is important for modelers who want to explicitly represent dendrites in their motoneuron models (either as a separate compartment, an equivalent cable or completely reconstructed trees).

16. The Discussion section on relevance for modelers contains the following statement: "This supports the conclusions that the relative voltage threshold is constant within the MN pool and that Ohms law is followed in MNs". This is not strictly correct. Gustafsson and Pinter (1984b) showed that voltage threshold tended to be lower in low input conductance cells with long AHPs (see their Figure 4C and D). Also, the voltage threshold predicted by Ohms Law from the product of the measured rheobase and input resistance Vth = Ith*R tended to be lower than the measured voltage threshold, suggesting the activation of an inward conductance near threshold. This requires a variant of Ohm's Law in which the effective resistance is voltage-dependent: Vth=Ith*R(v).

17. Finally, although the vast majority of readers will know that correlation does not imply causation, it is worth stating explicitly in the Discussion section on limitations.

18. p. 33, l. 721: Actually, you should consider that in some experimental conditions, large (high-threshold) MNs attain lower firing rates than small (low-threshold) MNs. Maybe you have to explain in what conditions large MNs attain high firing rates.
