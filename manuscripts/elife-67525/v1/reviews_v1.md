# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67525.sa1](https://doi.org/10.7554/eLife.67525.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This article introduces a new experimental method that enables the direct measurements of weak interactions between proteins. It is based on densely attaching one type of protein (antigen) to a ferromagnetic microsphere, which can then bind to another protein that has been attached to a flat surface, and applying an external, rotating magnetic field to force the particle to roll across the surface, where its motion is slowed by binding and unbinding of antigens. The sensitivity of the method suggests that it may prove useful in the study of weak protein-protein interactions.

Decision letter after peer review:

Thank you for sending your article entitled "Mechanically Transduced Immunosorbent Assay To Measure Protein-Protein Interactions" for peer review at eLife. Your article is being evaluated by 2 peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Cynthia Wolberger as the Senior Editor. The following individual involved in reviewer of your submission has agreed to reveal their identity: Erika Eiser (Reviewer #3).

As you can see from the reviews below, the reviewers agree that the method you have described has interesting potential, particularly in the small amount of material needed for the assay. However, there are concerns about the fact that the method itself has been published already some time ago, lessening the novelty of the publication. Focusing on the applications of the method would in principle be acceptable, but the concerns about the dynamic range of the method, and the important need for validation need to be addressed (perhaps requiring new experiments to do so) before we can reach a decision on your paper.

Reviewer #1:

The authors are seeking to develop a method for measuring the binding affinities between biomolecules using low amounts of material. The method described in this manuscript uses a magnetic field to cause a ferromagnetic particle to roll along a surface. When the particle is modified with one biomolecule and the surface is modified with another, there is an increase in friction if the two molecules interact. The degree of interaction is proportional to the amount of friction.

Strengths

– The method requires a minimal amount of material.

– The rolling parameter can be measured for many ferromagnetic particles simultaneously, leading to robust statistical analyses.

Weaknesses

– The method itself has already been described in a paper published by one of the corresponding authors in 2014.

– Insufficient detail is provided on the method and output. Raw data showing that the rolling particle is displaced in the presence of a binding partner on the surface is missing.

– The Kd cannot be directly obtained from the rolling parameter.

– Unlike methods such as surface plasmon resonance and biolayer interferometry, which use a comparably low amount of material, this method requires both binding partners to be affinity-tagged. The tags and the immobilization could obscure native interactions.

– Biomolecular interactions have a wide range of affinities that span over 15 orders of magnitude (1 M to 10-15 M). Yet, the dynamic range of the rolling parameter is only one order of magnitude (0.081 for Kd of 1 M and 0.918 for Kd of 10-15M). As a result, the rolling parameter values cluster together when correlated with Kds on a logarithmic scale. Subtle differences in binding affinity can therefore be lost.

– For any given system, the Kd must be measured using an orthogonal technique in order to establish binding affinities that can be correlated with the measured rolling parameter. More specifically, the rolling parameter values are not generalizable from system to system.

– The schemes presented in Figure 1 are difficult to interpret. Perhaps it would be better show a video of the particles rolling along a surface with no binding partner and another video when there is a binding partner. In the absence of these raw data for each system, the binding measurements are not compelling.

– The authors spend a great deal of time comparing their method to NMR, why? Other measurements such as SPR and BLI would be more appropriate comparisons.

– In general, I found the way in which the manuscript was written to be very misleading. After reading the Intro, I was expecting the rest of the paper would focus on the development of the method. Then, in lines 184-185 on page 6, it becomes clear that the method was already published 7 years ago by one of the corresponding authors. Thus, the paper is less about the method and more about the application.

– Please remove sentences like "It is difficult to overstate how transformative this will be for the study of PPIs." The method is not a direct measurement of binding affinity. The dynamic range of the measurement does not correlate with the range of biomolecular binding affinities. Multiple affinity tags must be used and orthogonal binding measurements must be made in order to interpret the rolling parameter values.

Reviewer #3:

In this article the authors introduce a new experimental method, named mechanically transduced immunosorbent (METRIS) assay, enabling the direct measurements of weak interactions between proteins. Such protein-protein interactions (PPT) are typically very weak (on the order of a fraction of the thermal energy, kBT). This new technique is based on densely attaching one type of protein (antigen) to a ferromagnetic micron bead, which can then bind to another protein, that has been attached to a flat surface. By applying an external, rotating magnetic field, the probe particles will be driven to perform a rolling motion on the flat surface. In order to see any displacement of the probe particle the antigens need to detach on one side and bind on the opposing side in the direction of the motion induced by the magnetic field. This apparent friction informs us on the strength of the PPT. The authors have tested a number of important PPT's – the non-covalent Interactions between Ubiquitin-like Domains and Ube2D1 is one example.

An important strength of the new technique the authors introduce is the sensitivity of their new method – it exceeds that of common methods by far, as they were able to measure protein-protein interactions at much lower concentrations (2 orders of magnitude) than is typically done. This allows a systematic determination of many interaction potentials between the complex configurations of proteins as function of solvent parameters and I guess also as function of temperature, which could be interesting new the denaturation region. In addition, the affinity or attractive interactions between specific proteins or RNA and proteins may change as function of concentration: As the reaction constant or KD value depends directly on the total concentration in the system the up- and down regulation processes of proteins may be better understood. The authors demonstrate that they can achieve such a sensitivity, which is well explained in the results and discussion.

The only point that needs to be addressed is the interpretation of the data. While the systems and references are very well presented and researched it would be helpful to the reader to explain in more detail the actual measurements and in particular their interpretation and relation between the displacements measured and the KD and Gibbs free energy differences.

My main suggestions are of technical nature concerning the interpretation of the results and the underlying theory.

In the present description (line 1567) the authors relate the displacement of the probe bead to a parameter they introduce as rolling parameter RP: zeta = δ x/(pi times the diameter of the bead times the frequency of the oscillating magnetic field). First I would call RP = zeta, or only RP unless I have not understood the difference. However, my main questions is how did the authors derive this expression in equation 1. It is clear that zeta must be dimensionless, hence it is presented as displacement divided a velocity that is multiplied with the actuation time. This velocity is the rolling velocity = angular velocity times the radius of the probe colloid. It is confusing what π is doing there. The authors should double check the equation and also explain to the reader why you introduce this parameter. Moreover, the radius of the colloids sured here should be given.

If I understand right, this zeta or rolling parameter is at the same time normalised against the streptavidin-biotin binding, which is known to be the strongest non-covalent binding in the system. If the probe particle is brought in contact and assuming that there is full coverage of avidin and biotin on the opposing surfaces, the effective contact area will depend on the size of the particle, and the binding strength with be more than 100 kBT. This means there is full traction and now slip or friction between the probe particle and the support surface. But with such strong binding energies, this means the fields applied must be very large and as the particle roller over the surface the biotin or avidin on one of the surfaces must be ripped off. Such behaviour was observed previously in AFM contact experiments, e.g. by the group of Herman Gaup in the 90's. First, the authors need to give details about the reproducibility of these reference measurements, in particular, the applied Forces (e.g. Magnetic field) grafting density and effective number of bonds in the contact area (which also may be influenced by the roughness of the colloidal bead surface) need to be detailed. Secondly, the authors do not discuss or present any calibration of the friction or rolling parameter. It is not necessarily a linear function between zero (no interaction and thus no friction) and one (full sticking/traction like when riding a bicycle).

In this context, it is important to look also into the displacement velocity. In these measurements the friction relies on the fact whether the protein-protein interactions are easily pealed off on one side and possibly re-established on the front of the rolling motion. But this will depend on how fast the rolling motion is. Again, AFM work by Gaup and in particular by Evan Evans (Annu. Rev. Biophys. Biomol. Struct. 2001. 30:105-28 – which should be referenced) showed that the force or interactions measured depend on how fast one pulls on the protein-protein link. Hence, the authors should give much more experimental detail and relation to known measurements. The numbers presented here for the Binding energies and their relation to the rolling parameters must be clarified as well, so that it would be possible for others to reproduce these measurements.

To summarise, the technique and the measured parameters need better elucidation and validation to be useful to others. In Particular friction is not necessarily the right terminology used in these measurements.
