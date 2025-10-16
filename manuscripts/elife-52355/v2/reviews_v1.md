# Peer review - Round 1

Editors:
- Pekka Lappalainen, University of Helsinki Finland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52355.sa1](https://doi.org/10.7554/eLife.52355.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Coordinated polymerization of actin filaments provides forces for plasma membrane deformation during endocytosis. However, the dynamics of individual actin molecules and actin-associated proteins within endocytic sites have not been reported, and thus the precise mechanism by which actin dynamics produces force for membrane deformation in endocytosis is incompletely understood. Here, Lacy et al. applied single-molecule speckle tracking to analyze the turnover of actin and actin-associated proteins in endocytic patches of fission yeast. They revealed very rapid turnover of molecules within the endocytic actin network, and heterogeneous behaviors of these proteins at the molecular level. Together, these results provide important new insights into the mechanism by which actin dynamics contributes to clathrin-mediated endocytosis.

Decision letter after peer review:

Thank you for submitting your work entitled "Single-molecule turnover dynamics of actin and membrane coat proteins in clathrin-mediated endocytosis" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Actin dynamics provides forces for plasma membrane deformation during endocytosis. Here, Lacy et al. applied single-molecule speckle tracking to analyze the turnover of actin and actin-associated proteins in endocytic patches of fission yeast. The revealed very rapid turnover of molecules within the endocytic actin network, and heterogeneous behaviors of these proteins at the molecular level. Thus, the authors suggest that the forces produced through actin polymerization in endocytic patches may be higher than previously estimated.

All reviewers concurred that the findings presented are potentially important. However, they stated that certain experiments lacked necessary controls, and the modelling part was inadequately described in the manuscript. Moreover, the experimental part of the manuscript is entirely based on single-molecule speckle tracking and some key results require confirmation by another experimental approach. Overall, an extensive amount of additional work would be required to address these points. Because of the policy of eLife to invite revisions only if they can be completed within 2-3 months, we cannot offer to consider this paper for further consideration.

Reviewers, however, provide several suggestions for how to improve the manuscript. Thus, if you can address these issues by performing additional experiments and by providing much better description of the models, we would be glad to consider a new submission on this topic for publication in eLife. In this case, the new submission would be evaluated by the three original reviewers.

Reviewer #1:

This manuscript reports a single-molecule speckle analysis of actin and selected other proteins in clathrin-mediated endocytosis in fission yeast. The authors provide evidence that these proteins display short residence times and rapid dynamics in endocytic patches. Analysis of single-molecule trajectories reveals that the motions of these proteins display differences that correlate with their functions in endocytosis.

The data presented in the manuscript appear of very good technical quality, and the study provides interesting insights into the molecular mechanisms of clathrin-mediated endocytosis. My main concern is that the data are somewhat redundant with the earlier FRAP analysis of endocytic components. For example, the studies by Kaksonen et al., (2003 and 2005) demonstrated (by using a Sla2del strain) that continuous actin polymerization occurs at the membrane of endocytosis structures in budding yeast with a comparable rate to the one determined in the present manuscript. This was also confirmed with another approach by Michelot et al., 2013. Thus, it is unclear for this reviewer, why the authors state several times in the manuscript that the 'common interpretation of the previous data is that the entire actin meshwork assembles and disassembles once during the total lifetime of the endocytic patch'. Moreover, the rapid turnover of clathrin was earlier demonstrated by FRAP analysis (Avionam et al., 2015). To merit publication in eLife, the authors should much better describe what it really novel in this study compared to earlier FRAP etc. experiments, and explain what fundamentally new information this work provides about the mechanisms of endocytosis. Otherwise, the manuscript is better suited for publication in a more specialized journal.

Moreover, the conclusions of the present study are entirely based on one method. Thus, the authors should use an alternative approach to confirm the main findings. They could e.g. carry out FRAP experiments on mEGFP-fusions of at least one actin filament binding protein and one nucleation promoting factor. If these proteins indeed display very short residence times in endocytic patches, this should be evident also form photobleaching experiments.

Reviewer #2:

In this manuscript, Lacy et al. aim to distinguish different mechanisms of molecule residence lifetimes using a combination of modeling and experiments. From the experimental standpoint, the authors provide quantitative measurements using a method they developed previously (Lacy et al., 2017) and I have no complaints with that. However, they use the model to identify possible mechanisms and here is where things get difficult.

1) What are they modeling? I read their Materials and methods, downloaded their MATLAB files, and tried to make sense of Figure 1. Given the sparse details in the Model simulations sections, I cannot make any sense of the model, the justification for the many assumptions and choice of parameters.

2) Then I downloaded the MATLAB file and tried to read it. At first glance, there is no documentation in the file, so I can't understand what's going on. After an inordinate amount of time spent on this. m file, I found the function simulator. It is a series of random and sorting functions! How do these functions represent the schematics in Figure 1A and B? Because the MATLAB file does not contain any representation of binding and unbinding events as mentioned in the Introduction, based on the information provided to me, the modeling component is not rigorous nor representative of the process they study.

3) The final issue is that the authors propose to distinguish different mechanisms from their data on the basis of this model. But since I don't understand the model, I cannot comment on the accuracy of the remainder of the work and therefore the scientific conclusions.

Reviewer #3:

Using single molecule labeling and imaging methods, Lacy et al. report that the lifetime of actin molecules and many of their regulators in actin patches is very short, on the order of seconds. This is much shorter than anticipated time based on the ~ 20 sec lifetime of actin patches. It is consistent with other studies in animal cells using similar methods that supported local turnover of dendritic actin structures. As yeast is a model organism for the study of actin cytoskeleton, this results will be noticed and important to the broad cytoskeleton field. I have however a few questions that I feel need to be addressed, mostly regarding the controls for accurate detection of such short-lived events.

1) Effect of photobleaching. In subsection “Single-molecule residence times of endocytic proteins are short” it is stated that photobleaching occurs over ~ 1 min so photobleaching is not important on the fast times scales of order 1 sec where actin turnover occurs. However this statement is not so obvious to me. In panel A of Figure 3—figure supplement 1 as well as Video 2 it's clear that photobleaching is significant over 5-10 sec, a time that could severely influence the calculated fraction of longer-lived spots (that would stay in the patch for a longer time and thus represent a bigger fraction of actin the patch). Further, given that in panel A the spots renew themselves by new monomers coming into the plane of focus, the photobleaching in the plane of focus could be even higher.

A control experiment on fixed cells is presented in panel C of Figure 3—figure supplement 1 where the spot lifetime is 15 sec on average (which is less than a min but longer than 1 sec). It is stated that the same imaging conditions were used as for live cells, 0.5 W/cm^2, but it's not clear of the frame acquisition rate and exposure were also kept the same. The binning of the histogram in panel C suggests that they were not and that the spot lifetime was about 10 exposures, corresponding to ~ 1 sec with the acquisition rate in live cells (panel B of Figure 3—figure supplement 1).

Can the authors address these apparent discrepancies?

2) Detection of spot lifetime in images. To address the difficulty of large number of spots in noisy images, the authors used a combination of automated and manual tracking of spot lifetime. However the spots are near the threshold of detection and in the provided videos and montages of Figure 1C and D it's hard to tell when the spot signal started and ended and whether blinking occurs. Providing examples of spot intensity versus time could help the readers evaluate the ability to detect and measure single molecule lifetimes, including addressing blinking effects and tracking errors. The effect of blinking could also be address nicely in fixed cells. The spot intensity should decrease rather abruptly in a depolymerization event and not slowly as might occur when the spot moves slowly out of focus.

3) How did the authors distinguish spots in patches at the cell middle that internalize away from the plane of focus versus spots in patches at the cell tip that could move parallel to the plane of focus? Does this effect influence the movement statistics in Figures 4-6?

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Single-molecule turnover dynamics of actin and membrane coat proteins in clathrin-mediated endocytosis" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors and the evaluation has been overseen by Vivek Malhotra as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All three reviewers found the manuscript significantly improved. They stated that the study provides important new information on the dynamics of actin and actin-associated proteins at the sites of clathrin-mediated endocytosis, and thus elucidates the mechanism of actin-based force generation in endocytosis. However, reviewers #2 and #3 raised few relatively minor points that should be addressed before publication.

Reviewer #2:

1) For completeness and making a more convincing case, I suggest that the authors provide one example of a video (single cells may be sufficient) for all tagged proteins and especially actin, for live and fixed cells as relevant.

2) Since, the authors work really at the limit of spot detection, providing examples of the filtered version of the video(s) that were used for measuring spot lifetime can also make the study more convincing. For non experts, it may be hard to see how lifetime measurement is feasible in the provided example of Acp1.

Reviewer #3:

1) In the Introduction, the authors state that, "As has been shown in other actin systems, continuous turnover of filaments allows a network to convert a larger amount of energy from ATP hydrolysis of actin polymerization into mechanical work over the meshwork's lifetime." And, " Based on these results, we suggest that the amount of force produced by the endocytic actin meshwork might be higher than has been previously estimated." These statements are not accompanied by any references. Given that this is a major finding, these statements should be supported by literature.

2) In light of point 1 above, some estimates of force production with and without actin turnover considerations would shed greater light on the impact of the work and make the manuscript more broadly accessible.

3) The modeling part of the work is now clearly explained, in that different models can give rise to the similar behavior (Figure 1). But now I'm wondering how does this contribute to the paper? The experiments and their discussions by themselves seem more solid and it seems that the modeling aspect really doesn't identify hypotheses or bring significant value to the interpretation of the data. It is true that's multiple mathematical mechanisms can give rise to similar looking functions but unless one is able to distinguish one mechanism from the other with a large degree of certainty, it's best to leave this portion out.
