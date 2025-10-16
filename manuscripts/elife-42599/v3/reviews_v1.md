# Peer review - Round 1

Editors:
- Frank Jülicher, Max Planck Institute for the Physics of Complex Systems Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.42599.sa1](https://doi.org/10.7554/eLife.42599.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Length regulation of multiple flagella that self-assemble from a shared pool of components" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The authors perform a theoretical study of the regulation flagellar length in Chlamydomonas based on intraflagellar transport of motors and tubulin subunits that govern assembly and disassembly. A key question is how the length of two flagella can be coordinated by exchange of components. This is an important question. The present paper extends an earlier model by Hendel, Thomson and Marshall. It presents simple analytic expressions for the length dynamics and steady state lengths in several scenarios of components that are shared or separate between cilia. After thorough discussion the reviewers concluded that this work is not a major advance as compared to the earlier work by Hendel et al. It provides an extension of that work which is of interest to specialists but does not represent a fundamental advance.

Reviewer #1:

The authors perform a theoretical study of the regulation flagellar length in Chlamydomonas based on intraflagellar transport of motors and tubulin subunits that govern assembly and disassembly. A key question is how the length of two flagella can be coordinated by exchange of components.

The paper is largely well written and interesting. First a reduced model is presented with several simplifying assumptions such as separation of timescales and simplified kinetic rules. In the context of this reduced model the coordination of two cilia is then discussed. It is shown that if a molecular component is not shared between two cilia then length can be coordinated. If all components are shared then coordination needs to be more subtle. The authors suggest that concentration dependent depolymerization could be responsible for length coordination.

This work is interesting but it also has shortcomings. Reading the Introduction, the paper makes a strong impression. However, when I worked through the main part of the paper weaknesses became apparent and the discussion seemed to be rather superficial. In the end it remains unclear what advance in our understanding the work actually achieves. In its present form I do not think that this work is suitable for publication in eLife.

Major points:

1) The main motivation of the paper is to provide a possible explanation of the cilia severing experiment shown in Figure 1B. This is an important and interesting problem. However, the manuscript fails to really advance this issue. The authors rule out the two independent flagella (Figure 3Bi) because they cannot account for the coordinated behavior of the experiment. It seems that the proposed model of coordinated flagella shown in Figure 4 does also not really capture the key feature of coupled flagella observed in experiments: the flagellum that is not severed shrinks to almost half its original length and then both flagella grow together to their final length. In fact, Figure 4 which is a key figure of the paper is not well presented. In a severing experiment the longer flagellum should start from the steady state length which both flagella reach at long times. Another problem with Figure 4 is that only stochastic simulations are shown. It would be better to show the true average which is obtained by solving the deterministic equations. Then it would be clear if the longer flagellum first reaches a minimum before it again increases its length to reach the steady state. The stochastic simulations can be misleading as the fluctuations conceal this important feature in the behavior or even give the impression of length minima but which arise only from the noise.

2) It is an interesting but not deep insight (given the simplifications of the model), that if all components are shared then only the total length is fixed but individual lengths are independent. As the authors show this feature is a result of the simplifications used. Taking more realistic aspects into account, such as the concentration dependent depolymerization, this degeneracy in the model is removed. However, there are most likely other possibilities that could provide such a lift of the degeneracy. The fact that one mechanism can lift the degeneracy is interesting but does not constitute a strong result given that the model fails to qualitatively account for the experimental data.

3) When discussing the cases where one component (M or T) is not shared but exists in two different pools, it is implicitly assumed that the separate pools (e.g. T1 and T2) are equal. However, this is not stated clearly and it is not clear why they should be equal if they are completely independent.

Reviewer #2:

The authors have analyzed a class of models for length control of the two cilia of Chlamydomonas. The interesting result is that a naive model in which both tubulin and motor pools are shared between the two cilia doesn't work: only the summed ciliary length is determined and the individual lengths are undetermined. To get length control for two cilia, the authors add a length-dependent depolymerization, which can be satisfied by a depolymerase whose concentration increases with length (which happens if anterograde transport of the depolymerase is advective but retrograde transport diffusive).

My main concern is: what is different/new compared to the Hendel et al. (2018) paper? Is this paper wrong, in the sense that their mechanism (which has no length-dependent depolymerase) does not work, contrary to their claims? If this is the case, then then this point must be stressed. If the Hendel et al. paper is correct, then more justification of the novelty of the current work is necessary.

The following points need to be addressed in the manuscript

1) What is the concentration profile of the depolymerase? Please add this in a figure. I assume that it is a linear increasing concentration from the base (as in the Hendel paper) but I would like to see this.

2) Under what conditions can depolymerases regulate a single cilium? Is a limiting tubulin pool necessary? Is a limiting tubulin pool necessary for the case of two cilia? Is a limiting pool of IFT motors necessary? The general point I am raising is that length-dependent depolymerization is a strong assumption and perhaps it is sufficient under very broad conditions. What are they? Then this point needs to be discussed.

3) The stochastic aspect of the work is irrelevant as it is not used and should be removed from the paper (perhaps put into another paper).

Reviewer #3:

The paper describes a very interesting study of the possible models that can account for the simultaneous length control in the flagella of a single-cell organism. The study is illuminating, and shows how simple models can help to shed light on the microscopic processes, simply from the analysis of large-scale dynamics. I have a few comments:

1) How many MT are in each flagellum? How is this number controlled? Is this also a dynamic variable that self-organizes? The implicit assumption is that this is a constant (determined at the base, and therefore not dependent on length?), but should be explained.

2) The authors consider that the ballistic motion of the motors to the growing tip is uninterrupted, is motors and their cargo do not detach from each other or from the MT track until the tip. Is this known to be a good approximation of this system? It certainly simplifies the analysis, as they do not need to solve the spatial distribution of the density of motors, and cargo, along the flagella's length.

I would suggest discussing how this is different from models of the growth and steady-state of actin-based protrusions, where dis-assembly is at the base, and the length is a result of force balance (see Naoz et al., 2008; Orly et al., 2014).

3) The question about the return current of tip-directed motors is also an open issue for myosin motors along actin-filled protrusions. Interesting dynamics and traffic jams have been observed and modeled (see Yochelis et al., 2015; Pinkoviezky and Gov, 2014, 2017), I suggest contrasting with the situation in the flagella.

4) The noise in the reactions that control the growth at the tip should give rise to a term in (1) that has noise multiplied by J and Tf? Would this change the dynamics?

5) MTs undergo catastrophes and recoveries, and the data traces seem to show this. Does this type of dynamics matter for the model? This should be discussed.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Length regulation of multiple flagella that self-assemble from a shared pool of components" for further consideration at eLife. Your revised article has been favorably evaluated by Naama Barkai (Senior Editor), a Reviewing Editor, and two reviewers.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript discusses the length regulation of the pair of flagellae of the green algae Chlamydomonas. The paper builds on earlier work of the Wallace Marshall group which proposed basic concepts of length regulation via tubulin transport along flagellae controlling assembly together with disassembly. Coupling of flagellae can be mediated by shaped molecular pools.

The present paper provides two important results:

i) Detailed theoretical analysis of the shared limiting-pool mechanism, and showing that by itself this mechanism does not lead to length equilibration of the two flagella.

ii) A careful study of a length regulation by length dependent depolymerization, showing that length dependent depolymeriyation together with shared molecular pools can account for the experimental observations.

However, the paper also has some serious weaknesses. In particular:

1) The experimental basis for their proposal of length dependent depolymerization are much weaker than claimed. In fact, Piao et al., 2009 and 2013, do not give evidence for depolymerases at the flagellar tip in steady state.

2) The claim that length dependent depolymerization is the only mechanism to account for the data is an overstatement.

3) The discussion of previous work (Hendel et al.) that did find length regulation as seen in experiments without the need of length dependent depolymerization is discussed only superficially and with a somewhat negative attitude. This previous work should be taken more seriously and discussed more carefully. It does show that length regulation does not require length dependent depolymerization. However, this seems to be resulting from different details and assumptions in the model.

The authors should tone down their claims and more carefully relate their results to previous work. Then this paper could become a very valuable contribution that clarifies subtle but general aspects of length regulation and provides novel insights in the possible role of length dependent depolymerization.

The authors have to revise their manuscript carefully before it could be suitable for publication in eLife.

Essential revisions:

– The authors discuss a mechanism for length dependent depolymerization. However, several arguments are unclear. The authors begin with the assumption in the Introduction: "We will assume for now that the rate-limiting protein is kinesin-2, which is the molecular motor responsible for transport toward the tip of the flagellum". But, then in subsection “Tubulin shared, motors shared and concentration-dependent disassembly” the authors write "although to this point we have assumed the rate-limiting protein is kinesin-2, in fact the model is valid for any rate-limiting IFT protein. Therefore, in what follows we assume that the rate-limiting protein is a depolymerizer having the same motion as kinesin-2, uninterrupted ballistic motion to the tip followed by diffusive motion to the base…"

The authors should clarify if there is a family of kinesins that possess both these properties, namely, anterograde transport of tubulin dimers in a directed manner along a microtubule as well as microtubule depolymerase activity. It seems no such motor is known.

– In support of their claim, the authors quote the experimental observations of Piao et al. Piao et al. clearly state in their paper that kinesin-13 "was transported by IFT into flagella during flagellar shortening." Further elaborating on this mechanism, Wang et al. (2013) reported that "CrKin13 was barely detectable in the flagella of steady state cells, as shown previously (Piao et al., 2009). However, during rigorous phase of flagellar assembly at 15 and 30 min after deflagellation, CrKin13 was found to be enriched in the flagella and decreased to normal level in fully assembled flagella". Thus, unlike the mechanism proposed by Fai et al. in this paper, experiments indicate very little presence of kinesin-13 depolymerases in the flagella under normal circumstances. Only amputation of one of these trigger a signal that leads to rapid entry of the kinesin-13 into the uncut flagellum for its depolymerization that supplies tubulins for the initial regeneration of the amputated flagellum. Thus, the roles of kinesin-2 and kinesin-13 and their presence or absence in the flagellum should be treated separately and cannot be represented by an all encompassing single motor. The relation to experiments and the required properties of motors should be discussed more carefully (see also next point)).

– Piao et al. demonstrated the depolymerase activity of kinesin-13 family (and not kinesin-8 family) in the microtubule disassembly in cilia. Kinesin-13 diffuses along microtubules to target either end and are not known to transport tubulin. Therefore, the claim of experimental support of the model seems to be a too strong statement.

– Subsection “Tubulin shared, motors shared and concentration-dependent disassembly”, the authors state "Unlike constant disassembly models in which a limiting-pool mechanism is essential for length control,…" This appears to be an incorrect statement. Some constant-disassembly models, e.g., Time-of-flight (TOF) model, which also assumes constant disassembly, does not assume "limiting pool". Instead TOF assumed "differential loading" of IFT particles, as indicated by the experiments of Wren et al.

Therefore, the statement "As we shall see, the constant disassembly models do not result in the rapid length equalization observed experimentally" is an overstatement and oversimplification.

– The key assumptions of Fai et al.'s model seem to be the following: (a) a concentration gradient of the depolymerases along the length of the flagellum and (b) the local depolymerization rate is proportional to the local concentration of the depolymerases. There appears to be an additional implicit assumption: the depolymerase is non-processive in its depolymerase activity (not to be confused with processivity in motility). Otherwise, depolymerases loaded on to the MT plus-end at a location closer to the ciliary tip may continue to depolymerize even when the MT becomes shorter and its plus-end reaches points where the depolymerase concentrations are quite different.

– The possibility of a concentration gradient of the motors arose naturally already in the paper of Hendel et al. (see page 667 of Hendel et al.). However, Hendel et al. did not associate this concentration gradient with that of depolymerases, which seems to be the appropriate picture.

– The authors present "testable predictions". However there are some problems. The experimental results already reported by Piao et al., 2009 and 2013, do not provide evidence for the presence of depolymerases at the tip in steady state. Also based on these experiments the existence of a concentration gradient of the depolymerases in the steady-state (that too, an increasing concentration towards the tip) seems to be unlikely.

The second testable prediction that the authors mention would not be a clear test for validation/refutation of their model. For all those models that depend on a dynamic balance of the rates of polymerization and depolymerization in the steady-state of the flagellum, lowering the entry flux of the IFT particles would lead to overall depolymerization although the local rate of depolymerization of the microtubules at the plus end would remain unchanged.

– The slight difference in the expressions for Lss derived by Hendel et al. and that of Fai et al. arises from difference in the scenarios considered by the two. The two assumptions made by Hendel et al. were clearly stated in their paper. The first assumption of "a constant source of free motor protein at the tip" and the second assumption of "the approximation in which motors that have reached the base immediately transport back to the tip" are exactly the two conditions ("no tubulin depletion" and "instantaneous ballistic motion") that Fai et al. point out in reducing their result to that of Hendel et al. In this sense their derivation is only slightly improved compared to that of Hendel et al.

– I find the claims of the paper that Hendel’s model is somehow incorrect and that the present manuscript solves all open issues unconvincing. Hendel et al. show a scenario where length control works, probably based on different detailed assumptions. This should be more clearly discussed and not superficially mentioned as in the paragraph three of the Discussion.

– The authors discuss the case where molecular components stabilize their levels (Equations 18 and 19) and point out the problem that in steady state such a relaxation to fixed levels breaks length regulation. It remains unclear if that is also a problem for the proposed model based on length dependent depolymerization. Also, it would be important to know what happens when the motors alone are relaxing to a fixed level but the tubulin is limited and fixed. Would that be similar to the results of Hendel et al.?

– The authors seem to miss relevant references: Varga et al. (2009); Klein et al. (2005); Johann et al. (2012).‏ These should be cited and their consequences for this paper should be discussed.
