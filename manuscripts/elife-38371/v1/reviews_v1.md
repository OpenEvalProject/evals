# Peer review - Round 1

Editors:
- David Lentink, Stanford University United States

Reviewers:
- Andrew Biewener, Harvard United States
- Greg Sawicki, NC State University United States

## Review text

DOI: [10.7554/eLife.38371.022](https://doi.org/10.7554/eLife.38371.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Step-to-step variations in human running reveal how humans run without falling" for consideration by eLife. Your article has been reviewed by Andrew King as the Senior Editor, a Reviewing Editor, and two reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Andrew Biewener (Reviewer #1) and Greg Sawicki (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

How do humans stabilize themselves while running? This study of human running exploits the information contained in the natural step-to-step variability of the movement of the center of mass of the body as well as the ground reaction forces under the foot to 'reverse-engineer' the control algorithm. Using well-designed experiments and mathematical modelling, the authors provide key insights into how changes in foot placement and ground reaction force are modulated to deal with noise and perturbations to run stably. Interestingly, humans make these adjustments side-to-side within a stride, while fore-aft adjustments are made over several strides. Previous studies explained the role of elastic storage in the legs to run efficiently, the present findings shed new light on the central role of active muscle control to run stably. This finding is of broad interest to roboticists, engineers, and biomechanists interested in human and animal locomotion over terrain. The new information on how humans control their gait may be used to develop better controllers for powered exoskeletons and prostheses as well as humanoid robots.

Essential revisions:

1A) The authors tend to overstate the novelty of their findings in suggesting that past work based on a passive spring-mass running model cannot account for stable running. Past work based on spring-mass running mechanics was developed to argue for how passive-elastic properties may reduce the work of muscles needed to control leg and body movement. But these past studies do not claim that muscle work per se is unnecessary. As the author's own work (Srinivasan, 2011) and earlier papers (Alexander, 1997; Ruina et al., 2005) have noted (in addition to others – e.g. Biewener and Daley, 2007), spring-like leg behavior can result from an inelastic limb, in which muscle negative work is performed followed by equal positive work. The authors should revise to more accurately represent that understanding and approach of past workers on running dynamics in relation to their own work. We understand that some of these earlier studies may have overstated their implications towards dynamic stability during running. However, we encourage the authors to focus on their new data and model and let that speak towards the contribution of their study. Examples are listed below:

1B) The majority of those who have modeled steady running as a spring-mass system with spring-like leg dynamics do not suggest that this passive model is an accurate representation of how running is controlled, or that it would necessarily result in stable periodic motion following a perturbation. The authors' telescoping or single knee joint muscle-controlled leg model which shows net leg work (either negative or positive) is unsurprising in this regard and an expected result. Please better reflect that past workers who analyze running as spring-mass dynamics implicitly or explicitly recognize that some muscle work must be done to control the time-varying motions of a runner's CoM state for stable periodic motion.

1C) Introduction "Here, in contrast, we eschew spring-mass-like assumptions and characterize the control in terms of how humans modulate their leg force magnitude and direction." This is somewhat misleading in that spring-mass assumptions previously made by other workers were to explore the extent to which running (trotting, hopping) can be explained by passive dynamics, while recognizing that some amount of muscle work to stabilize running (or to go uphill/downhill, change direction) is necessary. The majority of prior workers do not claim that running is purely passive and does not require muscle work for control and stability. Please reflect the understanding and work in the field more accurately here.

1D) Subsection “Human-derived controller stabilizes a minimal model of bipedal running”: "Running stably cannot be purely passive and involves active leg work." Please revise so this does not overstate the significance of the authors' modeling and findings.

1E) Discussion section: The pseudo-elastic behavior of a runner's leg, which in fact could be entirely based on actuation (negative work followed by equivalent positive work) – as citations to Ruina et al., 2005 and Alexander, 1997 demonstrate, as well as the author's own past work (Srinivasan, 2011).

2) There is a large literature dedicated to understanding variability in gait (e.g., Dingwell's GEM; Chang's UCM; Hausdorff's long-term noise correlations; Laquaniti's principle components analysis etc.). These approached are predominantly based on characterizing the variability in kinematic measures as a way to assess 'stability', but they cannot say much about the underlying control and this has limited their impact on understanding control of gait mechanics more fundamentally. The approach presented here is a long-overdue, a more formal linear systems ID framework grounded in Newton-Euler mechanics. It may be worth acknowledging this and comparing/contrasting the utility of these two approaches (e.g., diagnosis vs. prediction) without overly criticizing previous approaches. E.g. by focusing one or a couple of sentences in the discussion on the key new abilities that add to previous approaches and how they could be used together in future studies.

3) The modeling approach taken here is framed in the form of a linear system ID, which is OK for small perturbations, in this case step to step variation around an average behavior. Figure 8 starts to address this in simulation, but how well does the approach hold for more explicit, larger perturbations at different phases of the gait where non-linearities might become more important? What is the plan to deal with this? Please clarify this, or the underlying limitations, in the discussion.

4) Please discuss the potential physiological mechanisms underlying the extracted controller, and suggest experiments that could be done to elucidate them if you have a new perspective on this. E.g., the authors mention a combination of feedforward and feedback processes but do not elaborate much on how vision, vestibular, proprioception, and cerebellar internal model may contribute.

5) Can this approach be applied to smaller data sets from single individuals as well? How variable is the controller across people and how much data is necessary to extract a good model?

6) Introduction "Numerous running robots have demonstrated stable periodic running, using a variety of control schemes (Raibert, 1986; Chevallereau et al., 2005; Tajima et al., 2009)." If robots are moving stably and periodically, as stated here, why then isn't human running and other animal running not stable and periodic as per the authors' lead statement (Introduction)? The earlier statement is made to argue the importance of muscle actuation for control to achieve truly stable periodic motion. Clearly both animals and robots need to do some muscle work to control movement. This inconsistency in phrasing needs to be addressed.

7) The regressions for equations 1and 2 should be shown (at least in supplemental materials).

8) Subsection “Impulse control is achieved by phase-dependent force modulations”: "compute the phase-dependent sensitivity of the GRFs to…" Exactly how are these phase-dependent sensitivities computed? (The y-axis label for these needs to be defined/explained more clearly.) This is explained in part (subsection “Linear regressions between the outputs and the inputs”) but could be made more clear and explicit when showing and referring to these patterns in Figure 4.

9) Figure 5: Swing-foot reposition and CoM state predictability of foot position – how these are determined/calculated needs to be made clear. Results are stated but their basis is not shown.

10) Figure 6: The force-velocity and force-length relations shown and implemented in the authors' model may be overly simple. F-V is an inverse hyperbolic not linear relationship and the lengthening side of F-V is much more skewed than the authors' model. (Also consider Zajac, 1989). How would a more realistic F-V relationship (inverse hyperbolic for shortening and a more steep and rapid leveling off of force in relation to lengthening) affect the authors' model?
