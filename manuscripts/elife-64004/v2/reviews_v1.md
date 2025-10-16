# Peer review - Round 1

Editors:
- Donald Hamelberg, Georgia State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64004.sa1](https://doi.org/10.7554/eLife.64004.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The driving forces behind the formation of membrane-less organelles within cells have been of significant interest. The results of this article suggest that non-specific electrostatic interactions primarily control phase separation of RNA/protein condensation in a cytoplasmic-like environment. The results suggest that phase separation occurs readily in simulations, and the simulations reproduce experimental results of binary mixtures of proteins and RNA. The predictions made by a theory developed by the authors to explain the experimental results are in good agreement with the simulation data. The combination of the different techniques is commendable, and it is anticipated that the results presented will stimulate additional studies.

Decision letter after peer review:

Thank you for submitting your article "Charge-Driven Phase Condensation of RNA and Proteins Suggests Broad Role of Phase Separation in Cytoplasmic Environments" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Donald Hamelberg as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The manuscript by Dutagaci et al., describes a combination of coarse-grained (CG) simulations, theory, and experiment to examine the possibility for phase separation to occur in mixed protein-RNA systems that are intended to mimic cytoplasmic conditions. The authors develop a theory to predict and explain experimental results of binary systems. The authors find that phase separation occurs readily in simulations in which cytoplasmic components are modeled as spheres, and they then show that the same simulation models do a reasonable job of reproducing experimental microscopy results obtained for simple binary mixtures of proteins and RNA. Especially encouraging is that good qualitative correspondence is obtained between simulation and experiment with regard to which proteins form condensates with a model small RNA (J345); the predictions made by the theory are also shown to be in quite good agreement with the simulation data. However, it is not completely clear to the reviewers how much the condensates maintain a liquid character. The paper is well written, the results are interesting, and the attempt to combine different techniques is commendable.

The work will be of interest to many in the field. The results would stimulate additional studies and experiments by the authors and others. Below are recommended revisions to improve the manuscript and strengthen the conclusions of the work.

Essential revisions:

1) It is very clear from the beautiful simulation snapshots shown in Figure 1 that phase separation occurs in the CG simulations of the authors' cytoplasm model. There is no question that this is a very interesting and arresting result. What is less convincing, however, is how strong the evidence is in support of the statement that the separated phases seen in the simulations are "liquid condensates". The nice movie provided by the authors gives an impression of two gel phases rather than two liquid phases; gel-like behavior would also seem to be a likely outcome given the absence of hydrodynamic interactions in the simulations. In support of liquid-like behavior, the authors mention that the macromolecular concentrations are consistent with liquid estimates and that, for the tRNA-dominated condensate at least, the RDF has few clear peaks (Figure 1—figure supplement 3); the latter feature, however, could be caused by small displacements of many tRNAs about nearly-fixed positions within the condensates. The authors also argue that their measured translational diffusion coefficients (Dtr) indicate liquid-like behavior. But these are obtained from fits to MSD data with lag times of only up to 20 ns, and it is clear from the plots that the lines are deviating from linearity as the lag time increases up to 50 ns. If the authors were to instead measure Dtr with a series of much longer lag times (e.g. up to 1 us: very feasible given the 1 ms simulation time and the number of molecules in each condensate) then I think that they might find that their Dtr estimates would drop lower and lower as the lag time increases. If so, wouldn't that indicate that the condensates are gels rather than liquids? The phase separation observed by the authors is a sufficiently interesting result to report, without needing to go one step further and say that the observed phases are liquid-like. If the authors really want to argue that the phases they observe are liquid then they need to provide stronger evidence; if not, wouldn't it would be better to just say "phase separation" throughout the manuscript and leave it at that?

2) Related to the point above, the experiments undoubtedly confirm the formation of condensates between RNA and positively charge proteins. However, the nature of the condensates is ambiguous for majority of the RNA/protein systems studied. Surprisingly, it appears that only one of these condensates possibly maintained a liquid character, contrary to simulation results of the multicomponent systems. In general, are two component systems capable of forming liquid phase condensates? What is known?

3) The simulated cytoplasm model is a reduced representation of an atomistic model previously reported by the authors in this journal. The trade-off made here is that the reduced representation allows much longer timescales to be simulated and this may well be the key to the interesting behavior uncovered by the authors. The model itself, however, is very reminiscent of cytoplasm models previously reported in the literature by other groups: starting with seminal work by Bicout and Field, (1996), but continuing with works by Ridgway et al., (2008), McGuffee and Elcock, (2010), Ando and Skolnick, (2010), Qang and Cheung, (2012), Xu et al., (2013), Hasnain etr al., (2014), Trovato and Tozzini, (2014) and probably others. Of these studies, only the Ando and Skolnick paper is cited here. Some of those earlier studies use models *very* similar to that used here, while others employ models that are much more structurally detailed (though not having the explicit solvent used in the authors' previous atomistic MD simulations). While the present study is exciting in both its timescale and its findings, omitting references to those other papers does readers a disservice and makes the authors look ungenerous to others working in the field. A paragraph should be added to the Introduction and Discussion section that cites and acknowledges the good simulation work done by others that came before this study.

4) Given the potential implications for "real life" in vivo, the authors should also provide some deeper discussion of the potential shortcomings of their CG cytoplasm model, e.g. with regard to: (a) components that are only very roughly treated (e.g. the "mRNA" is 6 copies of a 100-nucleotide RNA, which isn't enough to code for anything interesting), (b) components that might be important but that have been left out (DNA? metabolites?), and/or (c) components for which a sphere might not be a particularly good model (see mRNA above).

5) The authors account for bound counterions by modifying the effective charge on each sphere using Equation 5 or Equation 6. It is unclear where these equations came from. Were they made up by the authors (e.g. Equation 6?) or where they obtained from another source?

6) The algorithm used in the simulations should be clarified. As written, it sounds like conventional molecular dynamics (MD) was used, which would be an odd choice since it would mean that the macromolecules would move ballistically between collisions. But in the Materials and methods section we are told that a Langevin thermostat was used in the simulations, which would make them stochastic dynamics (SD) simulations instead.

7) Additional text would be helpful for the legend to Figure 3 and/or Materials and methods section outlining how each of the data points on the phase diagrams in panels A-D were obtained: after multiple readings of this section of the paper it is reasonably clear about where the fit-lines come from, but it is unclear on the much more basic issue of how the actual data points were obtained.

8) In fitting their theory to their simulation data, the authors note that "Mathematically possible solutions include cases where the volume fractions in the cluster exceed what is physically realistic". They therefore restrict their solutions to ones in which the total macromolecular volume is less than 30%. This doesn't seem unreasonable, but the 30% number is somewhat arbitrary. The authors should say how many of their final solutions ended up with a volume of 29.999% as this would tell whether the theory really wanted to settle on a quite different answer than the one ultimately accepted by the authors.

9) It may be worth elaborating on the "… highly ordered arrangement in the RP condensates." It was recently shown that a balance of homotypic and heterotypic interactions might lead to structured condensates (10.1093/nar/gkaa1099).
