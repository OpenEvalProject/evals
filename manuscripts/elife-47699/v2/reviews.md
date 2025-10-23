# Peer review - Round 1

Editors:
- Julien Vermot, Institut de Génétique et de Biologie Moléculaire et Cellulaire France

Reviewers:
- Andrej Vilfan, Max Planck Institute for Dynamics and Self-Organization Germany
- Martin Blum, Germany

## Review text

DOI: [10.7554/eLife.47699.sa1](https://doi.org/10.7554/eLife.47699.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

How fluid flow and cilia motility modulate robust and reproducible patterning events in the embryo is of great interest to a large audience of scientists, both in developmental biology and more disease oriented disciplines. Cilia motility controls the embryonic cerebrospinal fluid circulating between the brain ventricles and the central canal in the spinal cord, failure of which could lead to congenital disease. This work studying cerebrospinal fluid dynamics in the living zebrafish embryo, exploiting imaging, genetics and modelling approaches, sheds new light on a particular mechanical integration between cilia motility and fluid movements within the cerebrospinal canal. Of particular interest is that deficiency in fluid movement can impairs robust morphogenesis and embryonic growth, raising the possibility that similar defects may compromise similar events in human. The precise effectors of cilia motility and the anatomy of the systems of canal where fluids flow will require future work. This study will certainly stimulate others in the field to build on the authors’ working model.

Decision letter after peer review:

Thank you for submitting your article "Origin of bidirectionality of cerebrospinal fluid flow and impact on long range transport between brain and spinal cord" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Didier Stainier as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Andrej Vilfan (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a highly interesting study of fluid flow in the central canal. The paper first presents in vivo maps of the cilia and the flow, then provides a simple model for the bidirectional velocity distribution, showing that the cilia-induced pressure difference helps maintaining the shape of the canal and discussing the implications of the bi-directional flow for particle transport (which has the properties of enhanced diffusion) and embryogenesis. The study describes an automated workflow of bidirectional CSF flow assessment in the central canal (CC) of the zebrafish spinal cord as well as of CC geometry and cilia localization, which the authors can closely mimic in their modeling attempts. Mutant lines with defects in ciliary motility are analyzed using this workflow, demonstrating a reduced CC diameter (a collapse) in mutants. The manuscript concludes with the description of a novel, so-far overlooked, anatomical feature of the zebrafish central nervous system (Figure 7): while the central canal should run all the way from the ventral diencephalon to the caudal end of the spinal cord and is connected to the diencephalon by a newly discovered funnel cranially, the rhombencephalon extends a novel, much thinner canal dorsally which connects to the CC caudally by another thin canal. If this claim can be substantiated, this finding definitely warrants publication in eLife.

Essential revisions:

1) The existence of the newly described channel, that – if true – needs to be named, has to be proven beyond reasonable doubt, which requires in depth histology, ideally at TEM resolution. The brain anatomy in Figure 7A and Video 8 are not clear, particularly the identity and connection of brain ventricles to CC and the new canal, which is actually not displayed except as a thin line in the scheme in Figure 7A. In other vertebrates (amphibians through mammals), the diencephalon harbors a blind-ending ventral protrusion of the ventricle, which will give rise to the neural part of the hypophysis. Do we see flow in the hypophysis protrusion of the diencephalon in Video 8? Would the hypophysis then be connected to the CC? Why should the rhombencephalon not be connected to the CC, which is what we know from all other vertebrates? This might be an ancestral feature of basal vertebrates, which would be extremely interesting in an evolutionary context, but it needs to be proven. Known canal-like connections in vertebrate embryos include the buccohypophyseal (ventral diencephalon) and neurenteric canals (caudal neural tube/spinal cord). How do the described canals relate to the new one?

2) It is very interesting to see that in ciliary motility mutants the CC collapses and CC flow is abolished. The authors speculate about potential function of CC flow and exosomes transported along the CC. Based on the mutant phenotypes, what specific function of CC flow can be derived? One would really like to learn more about the physiological function of CC flow. A careful analysis/discussion of spinal cord phenotypes in mutants should provide the/an answer.

3) The authors argue that 30 hpf is the ideal time point for their analysis. With the improved automated workflow at hand, the descriptive part of this work would gain a lot by relating this stage to earlier and later time points, particularly with respect to the novel canal.

4) Is it possible to know more about the few motile dorsal cilia: how many are they? Are they polarized, i.e. would they contribute to bi-directional flow? Where are they found along the cranial-caudal axis?

5) Figure 2B, Figure 2—figure supplement 1:

The zig-zag pattern of some cilia in Figure 2—figure supplement 1A illustrates some challenges when inferring the ciliary beating frequency from a single pixel intensity, which is a highly non-linear function of the cilium's phase. In the middle of the zig-zag line, the principal peak in the power spectrum will likely correspond to the second harmonic of the beating frequency. Aliasing can be an additional problem (the 2nd harmonic of a cilium beating with 40 Hz appears at 20 Hz when sampled with 100 fps). The description in Materials and methods is unclear on how these problems were dealt with.

6) Equation (4): the force density fvchanged its sign between Equations (2) and (4).

7) Equation (5): The zero flux condition (5) must have been taken into account in the derivation of Equations (3) and (4), which always give v=0 at y=d/2. Yet it is only introduced afterwards.

In the subsequent text, the value of α is given, but not that of the viscosity mu. The pressure gradient, which is half the value of fv, is presented as a numerical result, rather than a basic symmetry property of the model.

8) "Counterintuitively, this model predicts that vortices may originate not from cilia dynamics, but rather from the local absence of motile cilia in the ventral side on a distance larger than d."

What is the basis for this statement? What is meant by "cilia dynamics"? It is clear that cilia and gaps between them are both needed to get recirculation.

Moreover, the solution shows an interesting mirror symmetry about the center of the channel, which is not discussed. But it is easy to understand, considering that the velocity profile remains unchanged if any force profile f(y,z)=f(z) (i.e., independent of y) is added to the channel. The force distribution in Figure 3 can therefore always be made antisymmetric with respect to the channel center.

9) Figure 7: the funnel and the loop through RV are very difficult to see – it would be helpful to redesign the figure and make a magnification of the relevant region.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Origin and role of the cerebrospinal fluid bidirectional flow in the central canal" for further consideration by eLife. Your revised article has been evaluated by Didier Stainier (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The key point is to solve the general issue of the presumed canal system, especially given its transient nature. Some guidelines are provided below to address this issue.

Reviewer #2:

I like to repeat myself and state again that this manuscript by Wyart, Gallaire and colleagues is mainly technical and descriptive in nature (it lacks a hypothesis). It describes a novel, transient canal system in the embryonic zebrafish CNS; an automated workflow of bidirectional CSF flow assessment in the central canal (CC) of the zebrafish spinal cord as well as of CC geometry and cilia localization, which the authors can closely mimic in their modeling attempts. Several of the features of CC flow described here have been previously reported (by the same authors), though not at the resolution achieved here.

The novelty that qualifies this manuscript for eLife lies primarily in the description of the presumed novel channel system in the embryonic CNS. The revised manuscript contains a limited set of additional histological data that should prove the existence of these canals. Unfortunately, rather than being convinced, I now have doubts as to their existence.

The most parsimonious explanation for these canals would be that they represent aspects of the ventricle in contact with the floor plate ('tel- and diencephalospinal canals') and roof plate ('rhombencephalospinal canal') of the developing brain and spinal cord, with a temporal occlusion in between due to lateral walls getting in close contact (explaining why there is no fluid flow). In the chick embryo, Gary Schoenwolf has studied such a temporal occlusion back in the 1980s already. A wealth of published histological sections in various vertebrate embryos attest that brain ventricle walls as well as lateral walls of the spinal cord approach each other temporarily during development (cf. examples below). The transversal sections shown in the new Figure 7B2 and B4 can be interpreted in exactly that way. Zooming in on the DSC – or perhaps ventricle close to the floor plate – the tear-drop (with flattened bottom) shape of the presumed canal actually argues that this structure is not closed dorsally, which is visible in the ZO-1 stained specimen in B4, in which staining is continuous from the ventral-most aspect (DSC/FP) all along the lateral walls into the wide lumen of the rhombencephalon. The 'similar geometry' of Reissner's fiber and the ventral canal in addition argues that this canal represents the ventral most part of the ventricle next to the floor plate.

Because this issue is of central importance for the main message of this (descriptive) manuscript, it needs to be addressed beyond reasonable doubt: we have to be one hundred percent certain as to the nature of the described items. I think this is feasible without much effort and would include conventional histology, immunofluorescence staining and the analysis of some marker genes. I would suggest to stain WT specimens for mRNA expression of floor and roof plate marker genes (shh, BMP4, etc.) as well as for genes that highlight the dorso-ventral pattering of the brain and neural tube (pax6, nkx2.2 or the like). Stained specimens should be analyzed by conventional histology through transversal sections, such as in Figure 7B4. IF-staining for basal lamina-specific markers should be applied in addition to prove or disprove the existence of these canals.

If it turned out that the canals represented indeed merely the continuation of the ventricle lumen next to floor and roof plate, the manuscript would need to be rewritten. Whether or not it would still qualify for eLife is hard to judge at this point; it would need another round of thorough reviewing.

Example 1: from G. Halasi et al., Developmental Biology 365 (2012) 118-132;

Figure 1. Neural tube of WT chick embryo. Lumina at floor and roof plate are reminiscent of presumed canals in zebrafish.

Figure 2. Temporal progression of CC development, demonstrating the temporal nature of separate lumina at floor and roof plate.

Example 2: from Chen et al., Toxicol. Pathol. 45, 705-744, 2017. Figure 9. Representative images of the transient neural lumen occlusion of the spinal cord in the E11.5 mouse embryo.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Origin and role of the cerebrospinal fluid bidirectional flow in the central canal" for further consideration by eLife. Your revised article has been evaluated by Didier Stainier (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below. The critical issues have been adequately addressed and the reviewers believe the work will receive considerable attention in the field. They however identified a few remaining points where simple text revisions will be required before acceptance, as outlined below. Overall, the authors are asked to eliminate the term canal and explain that further work is needed to clarify its geometry.

Reviewer #2:

Nature of the report:

As stated by the authors: we disagree on this point. Although the authors use state-of-the-art technology to visualize and model cilia and CSF flow in the developing zebrafish ventricular system, the main character of the study is descriptive; it lacks a conceptual advance, i.e. it remains unclear what the physiological meaning of bi-directionality is and how the specific pattern of flow relates to any ciliopathies.

Anatomy in question:

Unfortunately, the revised manuscript still lacks clarity. It now seems obvious that the structures the authors report – "conduction paths" (termed "canals" in the former versions of the manuscript, a term that persists in the revised manuscript as well) – represent the dorsal and ventral aspects of the developing ventricular system. This should be clearly stated in the manuscript, not only given as a possible explanation in the Discussion. Canals and conduction paths are confusing and imprecise; in addition, such terms tend to stick, which would be inappropriate. The cited paper by the Sive lab shows a parasagittal section, which does not resolve whether or not these structures are part of the ventricle and provides no proof for the existence of novel conduction paths. In addition, the Ribeiro et al. paper nicely shows that during transition of the neural tube primitive lumen into the central canal, the lumen becomes very narrow, but remains continuous between its dorsal and ventral aspects. If the authors insisted that their conduction paths and canals were independent entities, 3D imaging or morphing of histological sections and segmentation of the ventricular system would be required.
