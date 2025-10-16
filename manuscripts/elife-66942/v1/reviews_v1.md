# Peer review - Round 1

Editors:
- Roger J Davis, University of Massachusetts Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66942.sa1](https://doi.org/10.7554/eLife.66942.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study demonstrates that AKT-mediated IRS1/2 protein phosphorylation provides a mechanism for negative feed-back regulation of insulin receptor signaling. Comprehensive analysis using computational modeling and experimental analysis provides convincing evidence to support the authors' conclusions.

Decision letter after peer review:

Thank you for submitting your article "Akt phosphorylates insulin receptor substrate (IRS) to limit PI3K-mediated PI(3,4,5)P3 synthesis" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Jonathan Cooper as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Model results were obtained by computational simulation, with parameters determined from fitting to experimental data for certain nodes in the signaling network. Comparing the simulated results for the different alternative models permitted inferences about which assumed feedback mechanisms were more versus less consistent with the experimental data. This integrated framework is a very powerful approach for helping dissect the complex system being examined.

a) Can the authors provide information with respect to parameter identifiability and uncertainty? Without this information being described concretely in the text – and perhaps in appropriate figure panels – it is difficult for a reader to know what degree of confidence can be given to the comparisons among mechanisms.

b) When a quantitative assessment of "fit" is illustrated (e.g., Figure 2B), in terms of the objective function – which is an aggregate overall time as well as all variables – what are the associated effects on qualitative behavior of the dynamics? Given that a key point being investigated here is the interesting qualitative behavior of a feedback system, seeing how that relates to an aggregate numerical fit metric would be quite helpful.

c) When modeling the molecular validation experiments, how are the parameters altered by a given perturbation? For instance, are inhibitory perturbations assumed to be complete and exclusively precise (neither of which generally guaranteed experimentally)? A note on this point for each perturbation should be provided, again to buttress confidence in the model / experiment integration.

d) The code used for modeling should be made available.

2. An important open question that is not resolved by the study is the mechanism by which the IRS proteins interact with the plasma membrane prior to insulin stimulation. This is fundamental to the model proposed in the manuscript. However, in the model shown in Figure 7 only the interaction of the IRS proteins with the IR after insulin stimulation is shown and the receptor-independent interactions are not included. This issue should be noted. Any insight that can be provided into this outstanding question would strengthen the impact of the study.

3. The levels of plasma membrane associated IRS1 and IRS2 rapidly decrease almost immediately upon stimulation with insulin. However, PI3K and AKT activity are sustained over a longer time course. Do the IRS proteins stay associated with the HDM or LDM fractions for a longer period of time? This analysis is shown for the IR but not the IRS proteins.

4. Stimulation with EGF causes a decrease in PM associated IRS1 and IRS2. Is this AKT-dependent? Does EGF stimulation inhibit subsequent insulin-dependent PI3K activation?

5. The data shown in Figure 6 indicate that IRS1 and IRS2 S to A mutants increase interactions with the PM upon stimulation with insulin. Is this an increase in the interaction of these adaptors with the IR or is this a receptor-independent interaction as observed under basal conditions. In other words, is the phosphorylation of the IRS proteins disrupting receptor interactions or receptor-independent interactions at the PM?

6. The discussion could address the following topics:

a) The position and number of S/T phospho-sites mediate the feedback regulation should be discussed. How heterologous kinases co-opt this mechanism to mediate inflammatory or ER stress during metabolic stress should also be discussed.

b) In addition to negative feedback, the authors might address the possibility that separation of IRS from the PM/InsR might facilitate translocation of the IRS signaling complex to another cellular site, which could be important for signal propagation.

c) Can the authors discuss how the mechanism might provide a rationale for the evolution of IRS as an obligate intermediate between the InsR and PI3K.

d) The overshoot is most apparent at 1 nM and less obvious at 100 nM insulin. How does the concentration of the principle signaling components (insulin, IR, IRS) modulates the strength of the AKT-mediated modulation of downstream signaling?

e) The authors might mention that other sites modulate tyrosine phosphorylation of IRS1 (PMID: 24652289), and whether these other sites might have a similar mechanism as offered by this manuscript.

f) Additional discussion about the physiological role of the correction of acute AKT activation "overshoot" that is observed would also be helpful for communicating the overall significance of the study.

Reviewer 1:

This is an interesting study that examines negative feedback regulation of IRS signaling to PI-3K/AKT. The foundation for the analysis is the knowledge that there is a rapid overshoot of the recruitment of AKT to the plasma membrane at low insulin concentrations. A theoretical framework is presented and experimentally tested. The authors conclude that AKT-mediated phosphorylation of IRS proteins mediates rapid negative regulation by depleting the pool of plasma membrane-associated IRS proteins. Strong evidence is provided showing that two sites of AKT phosphorylation on IRS2 are important. It is suggested that IRS1 is regulated by a similar mechanism, but it is less clear which sites are of key importance because of the number of sites and potential redundancy (or functional cooperation). Overall, this is a strong study (with data that supports the authors conclusions) that advances our understanding of insulin signaling.

Reviewer 2:

This is an interesting and rigorous paper that provides new information on a mechanism of feedback signaling/regulation that modulates downstream insulin signaling activated through the PI3K→AKT signaling cascade. Feedback inhibition at the insulin receptor substrates is important to understand because it can contribute to the progression of type 2 diabetes during hyperinsulinemia owing to nutrient overload. The authors report rigorous analysis of PI3K→IRS→AKT association at the PM, and how AKT promotes dissociation of IRS from the PM. The dissociation provide a mechanism to explain results from many published report over the past 20 years. The methods and approach are very powerful and will be used in the future to investigate signaling at the PM. By fitting theoretical models to experimental results, the authors conclude that dissociation of IRS from the PM is mediated by S/T-phosphorylation of IRS. Direct measures of S/T-phosphorylation are limited to inferences from mutations and two MS identifications in IRS2. How S/T-phosphorylation promotes dissociation is not clear, and whether it involves specific interactions with the InsR or other PM components, or nonspecific electrostatic effects is not resolved.The conclusions are generally consistent with previous results that IRS tyrosine phosphorylation is inhibited by PI3K◊AKT mediated IRS S/T-phosphorylation (For example PMID: 24652289). Indeed, previous studies show that LIRKO mice show a loss of insulin stimulated IRS1 S/T phosphorylation in the liver but not in the muscle (PMID: 26846849), suggesting that insulin signaling itself is the major mediator of IRS S/T-phosphorylation; however, except for 2 sites in IRS2, the AKT sites involved in IRS1 were not resolved in this report.

This manuscript provides evidence to support and solidify the hypothesis that AKT-mediated S/T-phosphorylation of IRS drives the IRS-PI3K complex away from the PM/InsR to explain the feedback inhibition, including reduced PIP3 production and target recruitment. While evidence of IRS S/T-phosphorylation is generally indirect (or theoretically validated), this feedback mechanism and especially the role for AKT is consistent with previous results showing that AKT inhibitors along with inhibitors of other kinases in the cascade can have a positive effect upon the steady state IRS1 tyrosine phosphorylation. Increased Tyr phosphorylation would be expected for an IRS complex that lingers at the PM/InsR, and inclusion of such results might be helpful.

Although MS analysis of putative AKT phosphorylation sites in both IRS1 and IRS2 was difficult to achieve, mutation of six predicted AKT sites in IRS1 or 5 AKT sites in IRS2 enhanced PM association of IRS, AKT and PDPK1, which is consistent with increased IRS signaling (and presumably Tyr phosphorylation). A measure of Tyr phosphorylation in this case would be a worthwhile addition.

Mutation of AKT sites individually did not disrupt the AKT-mediated feedback inhibition, which was taken as evidence that multisite phosphorylation is key for feedback regulation, as previous suggested (PMID: 24652289).

Only in the case of IRS2 were combined mutations at two validated AKT sites (S306A and S577A) found to disrupt IRS2 dissociation and negative feedback through AKT. The interpretation of this result is reasonable to support the idea that multisite S/T-phosphorylation (rather than any single specific site) mediates dissociation of IRS from the PM/InsR; however, it seems surprising that two sites are so much more effective than one if the mechanism relies upon a nonspecific electrostatic repulsion; however, as a similar mechanism for IRS1 was not supported by the data, the authors might consider other AKT targets might be involved in the feedback mechanism at the PM.Reviewer 3:

The focus of this study is to examine the feedback regulation of the PI3K/AKT signaling network in response to insulin stimulation. Insulin signaling is under tight control and many feedback regulatory pathways control the intensity and longevity of these signals. The IRS proteins have been shown in many studies to play an important role in the feedback regulation of insulin signaling through their phosphorylation on multiple Ser/Thr residues that impact receptor interactions, effector interactions and degradation of the proteins. A number of different kinases have been implicated in this feedback, including AKT for IRS1. The novelty of the current study is that a specific role for AKT-dependent phosphorylation of IRS1 and IRS2 in an early, acute regulation of PI3K/AKT signaling is identified. Specifically, the rapid spike that occurs immediately after stimulation is reduced partially and then a steady state level of activity is observed, and the decline in activity is regulated by AKT-dependent phosphorylation. Specific phosphorylation sites on IRS2 are identified that mediate this acute decrease in IRS/PI3K/AKT signaling.Overall the study is nicely done and the data presented are clear and convincing. Computational modeling is validated by experimental conditions and a role for AKT in feedback regulation through the IRS proteins is demonstrated. The importance of this signaling pathway and its regulation for normal metabolic homeostasis and pathological conditions such as Type 2 diabetes and cancer makes the study significant and relevant for a broad audience.

An important open question that is not resolved by the study is the mechanism by which the IRS proteins interact with the plasma membrane prior to insulin stimulation. This is fundamental to the model proposed in the manuscript. However, in the model shown in Figure 7 only the interaction of the IRS proteins with the IR after insulin stimulation is shown and the receptor-independent interactions are not included.Reviewer 4:

I will restrict my comments to the mathematical modeling aspect of the study.The goal of the mathematical modeling aspect of the study was to put into explicit and quantitative terms key assumptions and hypotheses concerning the biochemical processes under consideration. Different, alternative models were formulated, and numerical results from each were simulated, in order to permit comparison of predictions arising from diverse postulates representing dynamic signaling pathway mechanisms, in particular feedback influences.

To the extent that I can assess from the manuscript, the modeling work appears to have been soundly performed.
