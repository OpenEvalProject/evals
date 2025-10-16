# Peer review - Round 1

Editors:
- Lucie Delemotte, KTH Royal Institute of Technology Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56518.sa1](https://doi.org/10.7554/eLife.56518.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Computer simulations are increasingly used in structural biology as a means to integrate different kinds of experimental biophysical data, so as to facilitate a coherent and physically realistic molecular-level interpretation. This paper reports a structural refinement strategy of a previously determined NMR structure of a lipid nanodisc using orthogonal scattering data and advanced MD simulations. The elegant integrative simulation/experimental Ansatz leads to the insightful conclusion that the nanodisc undergoes elliptical structural fluctuations. Such elliptic fluctuations are "averaged out" in the NMR signal, but not in the scattering experiments data, thus resolving the apparent discrepancy between the different experimental methods.

Decision letter after peer review:

Thank you for submitting your article "Structure and dynamics of a nanodisc by integrating NMR, SAXS and SANS experiments with molecular dynamics simulations" for consideration by eLife. Your article has been reviewed by four peer reviewers, including Lucie Delemotte as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Franz Hagn (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The present manuscript builds up on previous work by the same authors (e.g. Skar-Gislinge, 2010, Midtgaard, 2015) towards the goal of understanding the structure and dynamics of MSP1D1-ΔH5 and MSP1D1-ΔH4H5 nanodiscs and their membrane mimicking capabilities. In particular, small angle X-ray and neutron scattering experiments are performed and used together with previously determined NMR distance restraints (Bibow et al., 2017)) and molecular dynamics simulations to obtain additional information on the structural properties of a lipid nanodisc particle in solution.

In essence, this paper reports on a structural refinement strategy of a previously determined NMR structure of a lipid nanodisc using orthogonal scattering data and advanced MD simulations. According to a procedure established by the Lindorff-Larsen lab, the conformational clusters obtained in the simulations are re-weighted to obtain a better fit to the experimental data.

A key question addressed by the authors is whether the NDs are circular, as suggested by the previous NMR experiments, or slightly elliptical, as suggested by the scattering experiments carried out by the authors. The elegant integrative simulation/experimental Ansatz leads to the insightful conclusion that the ND undergoes elliptical structural fluctuations, with the major axes changing direction and being largely orthogonal to each other. Such elliptic fluctuations are "averaged out" in the NOEs from NMR, but not in the SAXS data, thus resolving the apparent discrepancy between the different experimental methods.

Essential revisions:

1) The reviewers agreed unanimously that the work was methodologically rigorous, technically well done, and the scientific conclusions fully supported by the data. They also agreed that this manuscript was clearly written, and that the presentation of the data was thorough and well organized. However, it was not entirely clear what aspects of this manuscript were novel. SAXS and SANS on MSP1D1 nanodiscs, lipid melting transition temperature dependence probed by SAXS on MSP1D1 and MSP1E3D1, analysis of lipid properties in MSP1 nanodiscs, broadening of gel-liquid phase transition in MSP1D1-ΔH5, size-dependent increase of the transition enthalpy in MSP1D1 and MSP1E3D1 had been reported beforehand. The MD methodology as well as SAXS/SANS model building and fitting has been previously published by the authors.

It thus appeared to the reviewers that the novel aspect of this paper was the combination of various structural data and simulations to obtain better structures of challenging systems. Thus, while this paper provided a valuable protocol for dealing with structural data of various sources, this was not entirely clear from the paper in the present form.

Additionally the relevance of an oval nanodisc shape for their membrane mimicking properties was not entirely clear, since the shape might change in presence of a membrane protein. It was also unclear whether the conclusions around ellipticity could be generalized for all nanodiscs.

The reviewers thus recommended that the paper be rewritten to reflect the novel aspects of the work and to highlight its strengths while clarifying which aspects were already tackled by previous work.

2) In addition to the circular NMR structure from Bibow et al., 2017, a circular nanodisc structure was solved in a cryo-electron microscopy study by Frauenfeld et al., 2011. How would the authors compare their results to this single particle cryo-electron microscopy structure? It would be interesting to use also these restraints into the MD simulation. Could the oval shape of an empty nanodisc also be seen in (cryo-)electron microscopy single particle data (before class averaging)?

3) The work by Bibow et al. also includes PRE distance restraints and EPR distance restraints (and for the latter also a size distribution) which are of medium range and thus on almost a similar level of information as the SAXS and SANS data. These restraints should also be used in the reweighing procedure and discussed.

4) The authors show the good fit between SAXS and SANS data towards an elliptical model. The authors should illustrate how a circular model would fit with the data as well as different elliptical models to access the request for an elliptical model.

5) The major problem of any bulk studies is the potential presence of a heterogenous sample likely to be the case for nanodiscs because they may contain a distinct number of lipids. While the authors state that a single SEC peak is present that of course is not sufficient evidence for a single entity. First, this potential issue must be stated. Second, it is suggested to calculate the SAXS and SANS curves for a heterogenous sample with several cyclic nanodiscs having a distinct radius. Third, some argumentation may be put forward that indicate that the heterogeneity is of dynamic nature (such as a single set of NMR peaks, the dynamics of the MD simulation).

6) What do the authors mean with "membrane mimicking capabilities"? Just physical properties of lipids in nanodiscs as compared to liposomes?

7) It is not clearly described how SAXS and SANS data have been scaled for data fitting. Is it just a hardware-dependent correction or does it have an underlying physical meaning? This requires a short explanation.

8) For comparing the NMR structure with the simulation results, have the authors considered the entire NMR structural bundle (10 structures) or just a single structure? This might have a marked impact on the chi-square value for the NMR structure.

9) Correlation of MD with amide NOES (subsection “Integrating experiments and simulations”): The authors might want to add here that the amide-amide NOEs report on the α-helical secondary structure of the individual MSPs and are not quite sensitive to slight changes in the shape of the overall MSP belt. Thus, a good correlation with these restraints is very much expected.

10) Subsection “Integrating experiments and simulations”, seventh paragraph: it seems like the square root(C) value for the NMR/EPR structure is missing.

11) Order parameters (Figure 4B): What C-H moieties in DMPC have been used to calculate the numbers plotted in the figure? Also, it seems counter-intuitive that lipids in the rim region are more mobile than lipids in the core.

12) It is very good that the authors make their MD data publicly available on GitHub. It would be nice if the refined ensemble (or some number of representative frames) could be made available to the scientific community also via a database, such as PDB-dev.

13) The clustering step of the MD simulations seems quite important for the rest of the paper, and the choice of methods and parameters is not rationalized. Were other methods/parameters tested and why did the authors settle on this specific choice?

14) Additionally, the reviewers had the following suggestion, but did not strictly require additional experiments to be performed: Have the authors tried to perform SANS contrast matching experiments to obtain scattering data of the protein belt and the lipid patch only, respectively? Since the NMR structure does not contain lipids, such experiments would be helpful to validate the "lipid-free" structure.
