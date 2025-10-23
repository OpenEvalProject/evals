# Author response - Round 1

Authors:
- Srivastav Ranganathan
- Eugene I Shakhnovich ([ORCID: 0000-0002-4769-2265](https://orcid.org/0000-0002-4769-2265))

## Response text

DOI: [10.7554/eLife.56159.sa2](https://doi.org/10.7554/eLife.56159.sa2)

Essential revisions:

The major revisions requested are:

a) Please moderate the rather extreme pronouncements about the irrelevance of the equilibrium picture.

We appreciate the concerns raised by the reviewers with regards to the lack of acknowledgment of the importance of equilibrium theories. In the revised manuscript, at several places in the Introduction as well as the Discussion, we highlight how the process of phase-separation by multi-valent polymers is driven by the underlying thermodynamic landscape. In the revised manuscript, we emphasize that the current study focuses on potential role of dynamics in hindering the progression of a multi-droplet system to the equilibrium two-state system. We also provide examples from literature supporting the observation of droplet coalescence in support of the equilibrium predictions. The current study sheds light on the importance of dynamics of cluster growth, complementing the existing equilibrium understanding of the phenomenon.

b) Please analyze density as well as percolation transitions.

We thank the reviewer for this suggestion. In the revised manuscript, we introduce a second order parameter to analyze the intracluster density of polymers (normalized by the bulk density). This quantity is analogous to the order parameter “ρ” used to analyze density transitions by Harmon et al1. In Figure 1A of the revised manuscript, we plot the intracluster densities and cluster sizes as a function of total monomer concentration (Cmono). As observed in case of equilibrium lattice simulations by Harmon et al1, the density transition shows a non-monotonic behavior as a function of concentration, with large concentrations resulting in system-spanning networks with low densities. In a narrow range of concentrations, we do observe dense clusters. Further, in Figure 5, we show how intracluster density depends on the properties of the linker. In Figure 5B and Figure 5—figure supplement 2, we show how inter-linker interactions can tune the density of polymers within the clusters.

c) Please replace the usage of gelation with bond percolation.

We thank the reviewers for this suggestion. In the revised manuscript, we refer to large clusters with system-spanning networks as a “macrophase” (characterized by low density within the macro cluster), and to a system of coexisting clusters (Sclus << Ntot) as a metastable “micro-phase”. We refrain from using the term gelation in the revised manuscript.

We define these terms in the first subsection of the Results titled “Terminology and Notations used in this study”.

d) Please streamline the narrative to use a small number of necessary jargon terms and define these up front.

We now introduce the conventions and terminology used in the article in the first subsection of the Results titled “Terminology and Notations used in this study”. We also introduce a table listing the physical interpretation and the definition of all variables and order parameters used in the current study.

e) Please redo the LD simulations with reversible crosslinks to obtain a comparative assessment of the pictures that emerge with irreversible vs. reversible crosslinks.

To test whether the early time-scale behavior changes in the presence of reversible interactions, we introduced breakable functional bonds in our model. A comparative assessment of the single largest cluster sizes as well as the distributions for reversible and irreversible crosslinks is now presented in Figure 2B and C. As with the irreversible interaction simulations, even in the presence of breakable interactions, Lclus << Ntot (Figure 2B) indicating the existence of long-living metastable microphase droplets except for large Cmono when we observe a system-spanning network. Critically, we find a coexistence of intermediate cluster sizes with small and large clusters suggesting an increased diversity in cluster sizes at the early stages of droplet assembly even upon introduction of breakable interactions (Figure 2C). However, a more detailed study of impact of bond formation and breakage dynamics on cluster growth is the subject of future work.

The implementation of reversible functional interactions is explained in the “Modeling Specific Interactions” subsection under Materials and methods.

f) Please reconsider the assertions being made about solid-phases since the results cannot be used to make these assertions.

The usage of “solid-like” and “liquid-like” phases in the original manuscript was in reference to the rate at which monomers get exchanged between the condensate and the free medium in our kMC simulations (referred to as exchange times in the manuscript). We do not perform any other detailed assessment of the material properties of these assemblies. We therefore do not use these terms in the revised manuscript. Instead, we call these refer to these phases as slow- or fast-exchange phases in the revised manuscript , based on their mean exchange times in kMC simulations.

g) Please note that Ostwald ripening has been observed in vitro and there are numerous examples, especially from the Brangwynne and Hyman labs showing that a large single droplet will form and coexist with a dispersed dilute phase.

Thanks for pointing this out. In the Introduction section of the revised manuscript, we now include references supporting the in vitro observation of droplet growth via Ostwald ripening and coalescence.

h) Please include citations to the work of Chiu Fan Lee, Boeynaems et al. and Roberts et al. https://www.nature.com/articles/s41563-018-0182-6

In the Introduction and Discussion sections, we now broaden the discussion to include the potential role of active mechanisms as well as the rigidity of the scaffold in promoting/stabilizing a multi-droplet system. We cite the suggested references in the relevant context within the revised text.

i) Please revisit the description and usage of the reptation model, correct the mathematical description to ensure that what emerges has units of time, and ensure that usage of this model is indeed appropriate / accurate.

We agree with the reviewer’s comments about the validity of the reptation based mathematical description of the dimer reorganization timescale. Indeed, a classical reptation model predicts scaling of N3 while our formula predicts Rouse-type scaling of N2. Extra power of N in reptation model comes from slowing down diffusion in entangled dense polymer solution (melt) which does not play a role in our estimate of time scale of valency saturation in a polymer dimer in solution. However, we feel that this interesting question warrants a separate study. We removed this equation and accompanying discussion from revised manuscript since it is not central to our message here. We plan to return in the near future to careful study of polymer physics of valency exhaustion in dilute solution and report findings in a separate manuscript.

We also cite the sticky-reptation model described by Semenov and Rubinstein in the Discussion section of the revised version. While relevant, it explores somewhat different model of a dense solution while our focus here is on dynamic processes leading to formation of metastable microdroplets from initially dilute solution.

j) Please provide a more accessible treatment and an illustrative example of the KMC formalism (details that enable reproducibility are important).

We now provide additional details of the kMC simulation, and the details of cluster size computations in the Materials and methods section of the revised manuscript. The reactions modeled in the kMC simulations are schematically described in Figure 6. The simulation code for the lattice-kMC simulations will also be deposited in a software repository and will be accessible to the readers.

k) Please provide a summary of the main conclusions, please minimize some of the overstatements and casting aside of previous work, cite the seminal work of Semenov & Rubinstein, and touch base with the work of Huan-Xiang Zhou, especially the recent publication in PNAS.

The summary of the main conclusions is presented in the form of a succinct illustration (Figure 10) as well as the “Testable Predictions” section. We believe that a separate additional conclusions section will lengthen the paper even further and duplicate already existing pictorial conclusion. The work by Semenov and Rubinstein is now discussed in the context of exhausted valencies within clusters in the Discussion section. We also discuss the patchy particle model by Huan-Xiang Zhou’s group in the Introduction section while referring to existing computational studies related to LLPS. We thank the reviewers for bringing these important works to our attention.

Overall, we modified three figures in the main text (Figure 2, Figure 4 and Figure 5) and included a new subsection introducing the key terminology and order parameters used in this study. We include a new subsection in the Materials and methods section, discussing the implementation of breakable interactions. Under Introduction and Discussion in the revised manuscript, we also provide a more elaborate context emphasizing the importance of the existing thermodynamic understanding. Also, to provide a broader view of existing literature, we incorporate references to the possible role of active mechanisms in shaping droplet size distributions and compare predictions from both mechanisms.
