# Peer review - Round 1

Editors:
- Matthew A Quinn, Wake Forest School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78540.sa0](https://doi.org/10.7554/eLife.78540.sa0)

The Hippo signaling pathway is essential for multiple physiological processes, most notably the regulation of cell proliferation and survival during wound healing. Wehling et al. provide a molecular framework for an alternative mechanism by which the Hippo effector molecule YAP's sub-cellular localization is regulated by cell compartment-specific phosphorylation. Specifically, the authors demonstrate dynamic regulation of shuttling of YAP both in vitro and in vivo during drug-induced liver injury. Given the importance and developmental conserveness of the Hippo pathway, the work is of broad interest to the field of developmental and regenerative biology.


---

# Peer review - Round 1

Editors:
- Matthew A Quinn, Wake Forest School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78540.sa1](https://doi.org/10.7554/eLife.78540.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Spatial modeling reveals nuclear phosphorylation and subcellular shuttling of YAP upon drug-induced liver injury" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Matthew A Quinn as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Mone Zaidi as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Dirk Fey (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The model features very different diffusion rates for the canonical and alternative model, but is not explained why. For the estimation, different parameter ranges were specified for the canonical and alternative model, also for other parameters to be estimated, e.g. phosphorylation and dephosphorylation rates. This also lacks an explanation. What is the rationale behind this? Please update the discussion and/or methods to clarify this issue.

2) 200 parametrizations were obtained. Is the simulation result similar? Maybe include a panel in figure S2 in the supplement about this. Also, include a table with all fitted parameters.

3) Although of a dynamic nature, the model was not analyzed for the time-dependency of its simulations nor compared to time-course data, and the manuscript would benefit from a brief discussion, in particular with respect to the time-dependent biphasic response.

4) In Figures 2B and 2D, please highlight the boundary between nucleus and cytoplasm in the pictures, as the main difference between the two modeling results is the direction of gradient around the nucleus-cytoplasm boundary. In addition to the modeling result confined by the parameter space, please also provide an intuitive explanation of why the canonical model cannot account for the discrepancies between experiment and simulation.

5) Figure 3 on APAP regulation of YAP phosphorylation: As APAP generally induces toxicity, it makes sense to quantify cell death in the culture and limit the measurement to live cells. If possible, it will be nice to monitor the same cell population over the course of APAP or control treatment, and see how the nuclear/cytoplasmic ratio of YAP and TAZ change as a function of a cell's local environment. Also, did the proposed YAP phosphorylation in early APAP treatment (<6h) lead to YAP shuttling inside the nuclei?

6) The western immunoblot bands are hard to be interpreted by eye except when showing a binary result. Please add quantification for the plots in Figure 3C and Figure 4A, C, D, E, and F.

Reviewer #1 (Recommendations for the authors):

This is an interesting and thorough investigation of the regulation of Yap localization via its nuclear phosphorylation. While this is a novel concept and well-supported by the data provided, there are several unanswered questions that need to be resolved either by additional experiments or by an enhanced discussion as detailed below:

1) In figure 2, the authors demonstrate kinases able to phosphorylate Yap (LATS1/2) display a nuclear localization under low cell seeding conditions. However, is this localization of LATS1/2 dependent on cell density? Does a LATS1/2 knockdown or overexpression affect Yap phosphorylation and shuttling? Does APAP affect LATS1/2 localization? Answering these questions experimentally will give more credence to the claim that Yap regulatory machinery is located in the nucleus and affords functional consequences to those regulatory proteins.

2) Figure 4 shows the quantification of duolink particles for various proteins under control and APAP groups. However, the APAP treated group is not displayed. A representative image of the APAP duolink is needed.

3) From a mechanistic perspective the authors utilize an Akt inhibitor and show dephosphorylation of YAP. They also show that Akt inhibitors block APAP-induced phosphorylation. However, the authors do not determine the effects of the downstream sub-cellular localization of Yap. Determining if Akt inhibitors affect Yap localization during APAP treatment is needed to make a mechanistic link between APAP/Akt/Yap translocation.

4) The authors show APAP induces Yap translocation in vivo during DILI. While this demonstrates in vivo relevance to their in vitro findings, it does not convey any functional relevance in the modulation of the regenerative response. Does Akt inhibition affect hepatic Yap translocation and downstream survival or regeneration? Performing additional in vivo experiments modulating the Akt/ROS/Yap pathway is essential in order to draw conclusions on whether this is a viable therapeutic target in vivo during DILI.

Reviewer #2 (Recommendations for the authors):

1) The model features very different diffusion rates for the canonical and alternative model, but is not explained why. For the estimation, different parameter ranges were specified for the canonical and alternative model, also for other parameters to be estimated, e.g. phosphorylation and dephosphorylation rates. This also lacks an explanation. What is the rationale behind this?

2) 200 parametrizations were obtained. Is the simulation result similar? Maybe include a panel in figure S2 in the supplement about this. Also, include a table with all fitted parameters.

3) Although of a dynamic nature, the model was not analyzed for the time-dependency of its simulations nor compared to time-course data, and the manuscript would benefit from a brief discussion, in particular with respect to the time-dependent biphasic response.

Reviewer #3 (Recommendations for the authors):

I believe the conclusions are mostly supported by the result. My comments are mostly on data presentation and interpretation:

1. In Figures 2B and 2D, please highlight the boundary between nucleus and cytoplasm in the pictures, as the main difference between the two modeling results is the direction of gradient around the nucleus-cytoplasm boundary. In addition to the modeling result confined by the parameter space, please also provide an intuitive explanation of why the canonical model cannot account for the discrepancies between experiment and simulation.

2. Figure 3 on APAP regulation of YAP phosphorylation: As APAP generally induces toxicity, it makes sense to quantify cell death in the culture and limit the measurement to live cells. If possible, it will be nice to monitor the same cell population over the course of APAP or control treatment, and see how the nuclear/cytoplasmic ratio of YAP and TAZ change as a function of a cell's local environment. Also, did the proposed YAP phosphorylation in early APAP treatment (<6h) lead to YAP shuttling inside the nuclei?

3. The western immunoblot bands are hard to be interpreted by eye except when showing a binary result. Please add quantification for the plots in Figure 3C and Figure 4A, C, D, E, and F.

Finally, it would be nice if the authors could discuss (1) the role of nuclear phosphorylation in cell proliferation, tissue damage, and regeneration – i.e. whether the YAP/TAZ localization is the cause or consequence of cell density change, and (2) the biological implication of context-dependent effect of APAP in early and late treatment.
