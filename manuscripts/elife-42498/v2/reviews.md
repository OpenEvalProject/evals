# Peer review - Round 1

Editors:
- Arup K Chakraborty, Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.42498.031](https://doi.org/10.7554/eLife.42498.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Light-based tuning of ligand half-life supports kinetic proofreading model of T cell activation" for consideration by eLife. Your article has been reviewed by Arup Chakraborty as the Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this system the Lov2 domain binds Zdk1 with a low nM Kd in the dark and a low µM Kd in with intense blue light. Intense blue light will induce rapid conversion to low affinity form and dimmer blue light will induce slower conversion (even when Zdk1 is bound) and some degree of dark recovery of those molecules equilibrate to a concentration of active Lov2 that binds Zdk1 and dissociates with a koff defined by the light intensity. The Lov2 domain is attached to supported lipid bilayer (SLB) with a fluorophore and the Zdk1 domain (a small three helix bundle based on protein A repeat) is expressed as a first gen CAR. The system is cycled between the dark/dim (binding on) or light (binding off) states with the dark/dim periods leading to increased cell spreading. Even in the light state a contact area is maintained, probably by the low affinity interaction of the off Lov2 with Zdk1. As a readout the authors mostly focus on DAG sensor readout as the ZAP-70 readout for CAR itself seems to be recruited in simple proportion to engagement (even in light/off state?). The DAG reporter signal is proportional to kinetics rather that occupation. Suggesting that the step between the ITAM mediated recruitment of ZAP-70 and the LAT dependent recruitment of PLCγ (based on literature) can be involved in kinetic proofreading with a threshold around 10 seconds.

As a technical paper that develops a tool, this is an interesting paper and could be published in the Tools and Resources section. The paper is more relevant to synthetic biology and design of CAR based therapies, but limited relevance to how a TCR works or self/non-self discrimination. We do not think that the paper resolves the latter question, which the authors set out to address. A number of technical points about the method need to be addressed. Furthermore, somewhat disturbingly, the vast literature in the field is cited in a selective manner. Below, we provide guidance on both these important issues.

Essential revisions:

1) The Abstract and Introduction should be reshaped to reflect more of the background of CARs and T cell ligand discrimination and what a simplified signaling model with light based kinetic control could teach us.

2) Many aspects of the system are poorly described- at this point in the technologies they are working with they should provide:

a) Absolute quantification (molecules/cell) of the CAR on the Jurkat cells. This could be done by flow cytometry with 488 or 640 labelled Luv2 (dark) and MESF beads from Bangs labs.

b) The density of the Lov2 domain in the SLB in molecules/µm2 across the range that they are using. This could be done by line scanning FCS (dilute fluorescent version with non-fluorescent version if density is too high.) See PMID: 19254560.

c) The estimate of occupancy will be inaccurate if they don't include a control for exclusion of non-binding Luv2 mutant or similar sized protein in the bilayer with a difference fluorophore. See: PMID: 17911103.

3) It would be useful to see at least diffraction limited higher magnification images of the different signals to establish the correlation between IRM contact, CAR occupancy, the ZAP-70 and C2 domain sensor. It the CAR forming microclusters or is forming larger domains as it appears in the zoomed out views provided.

4) A number of relevant papers need to be cited that are pertinent, and the present results related to these studies. A small sampling of the missing literature are:

a) The work from the Davis lab from several years ago on using caged pMHCs that were sensitive to light, which allowed measurements that described the speed at which signals propagate downstream.

b) The role of rebinding that allows ligands with short half-lives to signal, described by work from eight years ago by Van der Merwe and co-workers (Immunity) and Huseby and co-workers.

c) The role of co-receptors, amount of active Lck and diffusion in kinetic proof reading described by Stepanek et al., (2014).

d) You also ignore the data the Germain lab, and others, have presented showing that the same ab TCR signals differently in DP thymocytes vs. mature cells [in particular, allows meaningful propagation of signals for gene expression in DP with pMHC ligands incapable of electing the same response or biochemical changes in a mature T cell], meaning that intracellular events can control signal propagation separately from occupancy, half-life or mechanosensing.

5) The model for proofreading is a bit strange. Many people have made models that are far more realistic and incorporate feedback, including several papers from the Germain lab (1995; 1997; 2005; 2002), Chakraborty and Palmer, Chakraborty and Weiss, and the more theoretical efforts by Murugan, Huse, and Leibler. These papers should at least be cited and briefly discussed.

6) The estimate of 3 proofreading steps is undoubtedly wrong. The various steps do not have the same time scales and there are feedback loops. These effects make the model's fit to obtain n very difficult to interpret. This part needs to be deleted.

7) The comments about ZAP70 not being subject to kinetic proof reading in the Introduction need to be made with great care. Two points to note in this regard: a] There are data suggesting that partial phosphorylation of ITAMs is at least correlated if not connected to antagonism. b] in vivo, ZAP that is bound to TCR is not phosphorylated. Also note that in vivo the T cells are constantly stimulated by self ligands (see recent paper by Weiss, Chakraborty and co-workers in MCB).

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Light-based tuning of ligand half-life supports kinetic proofreading model of T cell signaling" for further consideration at eLife. Your revised article has been favorably evaluated by Arup Chakraborty (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The reviewing editor has asked that you address one point prior to a final decision. Please describe the steps in optimisation of the adhesion system and the specific requirement for the system chosen. Also, the implications of this adhesion system for kinetic proofreading – aka kinetic segregation model – should be discussed. For example, could the lack of kinetic proofreading in TCR proximal signaling be due to the presence of the adhesion system, which takes care of CD45 exclusion and makes signaling a matter of occupancy? If the light dependent kinetics were in control of CD45 segregation, would this step show a sensitivity to kinetics?

Recent relevant papers include:

Chang.et al., 2016.

Cai.et al., 2018.

The editor is not asking for additional experiments, just a transparent discussion of the results of the adhesion system, why anti-β2m, and if this is actually required for the signaling by the light inactivated CAR.

Reviewer #1:

The study continues to struggle with proving "kinetic proofreading" (KP) due to the issue that the light dependent acceleration of dissociation of the LOV2 domain from Zdk1 doesn't impact the dark reversion rate (on rate) so the affinity is decreased by blue light. This is a similar limitation faced by people working with mutation-based systems for TCR or CARs. The mass action equation makes it very hard to change the half-life while maintaining a constant affinity and occupation. They partly compensate for this by doing the experiments at different densities of the LOV2 domain to have matched receptor occupancy at all light intensities. These densities are now specified, but there is a surprise there. This is partly successful as they do see a better correlation of DAG to kinetics rather than occupation, but it’s expected that this system fires fully at low occupancy, so this lack of linear relationship to occupation is expected. Thus, the proof of KP is not advanced that much in practice, but the potential is there. Additional innovations seem necessary to fully exploit it.

Essential Revisions:

The authors have added a synthetic adhesion system, which was only mentioned in the methods and some legends. They use a biotinylated mAb to β2m, which should pull the cells very close to the substrate, perhaps less than 10 nm. I assume this will exclude CD45 at least partially if not quite robustly (the authors should check this) so all they need to do to trigger the CAR is pull them into these close contacts. This changes everything as they are not making the LOV2-Zdk1 interaction achieve KP through "kinetic-segregation". This is thought by many to be a critical process that needs to be mediated by the ITAM bearing receptor to initiate signalling in many contexts. So, this adhesion system and its implications need to be described in the experimental design and schematics in figures as its likely critical to interpretation. Can the system work at all without this synthetic adhesion system? This may explain why they see no kinetic proofreading at the level of ZAP-70- as its recruitment is taken care of by the adhesion system and then bringing the CAR into the close contacts.

The other surprise is that the binding of the LOV2 domain displays significant positive cooperativity in binding to the SLB, suggesting that it oligomerises. How does this impact the measurements and interpretation?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Light-based tuning of ligand half-life supports kinetic proofreading model of T cell signaling" for consideration by eLife. Your revised article and response to our request has been reviewed by a Reviewing Editor and Arup Chakraborty as the Senior Editor.

Unfortunately, your response has not addressed the only issue that needs to be resolved. When the question about adhesion first came up, we asked about low affinity interaction in the off state that might support residual adhesion. You noted that this was not a relevant question because the adhesion system was added to make the system independent of the CAR interactions with the ligand to keep the cells in place over many cycles. Now you say the adhesion system is not needed and in fact you did not use it for the studies looking at ZAP-70's role in kinetic proofreading. Given this, unfortunately, we need to ask again if this indicates that there is a low affinity interaction in the 100% "off" state that could mediate some residual adhesion, but without signaling. If the cells remain attached in the presence of the most intense blue light that would completely turn off the interaction, then it seems there would be support for the presence of such an interaction. Can you acknowledge this, or do you have another explanation for the system working with or without the parallel adhesion system?
