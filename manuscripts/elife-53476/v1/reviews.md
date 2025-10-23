# Peer review - Round 1

Editors:
- Sarel Jacob Fleishman, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53476.sa1](https://doi.org/10.7554/eLife.53476.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors combined mutational scanning with structural and biochemical analysis of DHFR against different genetic backgrounds and show how these backgrounds can change the tolerance to mutations. The work provides several important mechanistic insights on the relationship between cellular proteostasis, protein structure and evolution.

Decision letter after peer review:

Thank you for submitting your article "Modulating the cellular context broadly reshapes the mutational landscape of a model enzyme" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Sarel Jacob Fleishman as the Reviewing Editor, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Thompson et al. used deep mutational scanning of E. coli DHFR to evaluate how the constraints imposed by the cellular environment modulate the mutational tolerance of the enzyme. To this end, selection coefficients of every possible DHFR amino acid substitution were determined in the absence and presence of Lon protease. The authors demonstrate that Lon dramatically transforms the mutational landscape of DHFR. A particularly interesting finding is that Lon largely suppresses the advantageous mutations that, in the absence of Lon, constitute over 23% of all single point mutations. It is suggested that the observed phenomenon can be explained by extensive activity-stability trade-offs, whereby advantageous mutations increase the DHFR activity, but this improvement in activity comes at the expense of reduced thermodynamic stability that renders the mutants sensitive to Lon degradation. The manuscript is clearly written and interesting and nicely adds to our understanding of the relationship between cellular proteostasis and evolution.

Essential revisions:

1) Bacterial fitness depends on the product of the catalytic proficiency (kcat/KM) and intracellular abundance of an essential enzyme (Dykhuzien, Dean and Hartl, 1987). This dependence was also specifically demonstrated for DHFR in E. coli (Bershtein et al., 2015) but isn't discussed in this paper. In the manuscript, the activity of the DHFR mutants is measured as initial velocity at a particular concentration of DHF. However, the comparison between DHFR mutants using this type of measurement is meaningless for mutants that vary substantially in their Km(DHF) values. For example, the reported Km value of L54F is 0.7 μm and that of F31Y is 168 μm – 240 fold higher (Figure 1—source data 3). This means that when the initial velocity for both mutants is measured at 20 μm DHF, the L54F variant operates at a rate close to Vmax, whereas the rate of F31Y is measured way below its Km and, therefore, is far away from its Vmax value. Since the changes in kcat and KM amongst DHFR mutants are not necessarily correlated (e.g., the kcat of variant F31V is close to that of wt but its KM is 2 orders of magnitude higher, Figure 1—source data 3), the differences in the initial velocities at a given concentration of DHF will be sometimes driven by kcat and sometimes by KM. The interpretation of these measurements with respect to bacterial fitness is further muddled by the fact that 1) the intracellular concentrations of the mutants are not known, and 2) the intracellular amounts of DHF can rise as a result of low DHFR abundance and/or activity (Kwon et al., 2008), thus affecting the relative importance of Km. Indeed, roughly half of analyzed adaptive mutations appear to have initial velocities lower than that of wt (Figure 4C and Figure 4—figure supplement 3), although the authors claim that the initial velocities are expected to be correlated with selection coefficients (as shown in Figure 1C for a small subset of mutants). Thus, the way the activity of DHFR mutants is measured does not adequately explain the observed distribution of selection coefficients.

For proper interpretation of the selection coefficients, it is therefore important to measure the intracellular abundance of a selection of DHFR mutants on Lon+/- backgrounds and to measure kcat and KM parameters for a subset of advantageous DHFR mutants.

2) Related to point (1) above, the mechanism invoked by the authors to explain why destabilization may increase activity through increased dynamics at the active site is interesting but other mechanisms related to cellular abundance have not been taken into consideration. In particular, DHFR destabilization is known to turn DHFR into a chaperonin client and this interaction may increase cellular levels. As argued in point (1) above, more detailed measurements of cellular abundance and kcat,KM determination are needed to produce a consistent interpretation of the results.

3) Results – the authors show that their DMS results are nicely reproducible. However, I don't think that they correlate the DMS results with individually measured selection coefficients (it's not totally clear whether the data shown in Figure 1C is from individual measurements or the DMS). They should do this to establish that the DMS accurately recapitulates individual measurements both in E. coli and for purified protein.

4) The selection system is beautifully designed to allow highly sensitive selection conditions, including the identification of better-than-wt DHFR mutants. The experimental conditions in the paper, however, are likely to be different from those that a wild type strain would face. First, the endogenous promoter of folA regulates the DHFR expression via a negative feedback loop: A drop in DHFR activity/abundance results in the upregulation of its expression (Bershtein, et al., 2015). An interesting question is how the distribution of fitness effects of DHFR mutations will be shaped by the presence of such a regulatory expression element. Second, it was demonstrated that the endogenous DHFR levels in E. coli strain carrying the chromosomal folA gene are very close to the optimal level, as the increase in activity or abundance of DHFR does not increase fitness (Bhattacharyya et al., 2016). The fact that over 23% of single point DHFR mutations increase bacterial fitness suggests that the intracellular DHFR levels in the selection system are far away from the optimum. Third, there is no difference in the DHFR sequence between naturally occurring E. coli B and K-12 strains, even though according to the authors' conclusions, the lack of Lon protease in B strains should have driven the adaptive evolution of DHFR in this strain. It would be helpful if the authors discussed these caveats in the manuscript.
