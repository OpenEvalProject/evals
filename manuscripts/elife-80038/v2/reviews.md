# Peer review - Round 1

Editors:
- Rohit V Pappu, https://ror.org/01yc7t268 Washington University in St. Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80038.sa0](https://doi.org/10.7554/eLife.80038.sa0)

In this work, the authors introduce and develop upon a computational model to investigate and quantify the effect of protein conformations and valence of interaction sites as organizers of structure within biomolecular condensates. The authors integrate their findings with new and emerging concepts regarding the coupling between phase separation and percolation as a determinant of driving forces and internal organization of condensates. The key insight that emerges from the current work pertains to the structure that prevails across length scales.


---

# Peer review - Round 1

Editors:
- Rohit V Pappu, https://ror.org/01yc7t268 Washington University in St. Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80038.sa1](https://doi.org/10.7554/eLife.80038.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Protein compactness and interaction valency define the architecture of a biomolecular condensate across scales" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Rohit Pappu as Reviewing Editor and José Faraldo-Gómez as Senior Editor. The reviewers have opted to remain anonymous.

The Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Many of the experimental details need careful scrutiny. Both reviewers raise specific concerns and make specific requests. Please respond with all the details that the reviewers are requesting.

2) Both reviewers are concerned about the rather sweeping generalizations and statements made that do not square with the state of the art. First and foremost, it is now clear that the phase transitions in question are not purely segregative LLPS type phenomena. That the field has overused this term and done so without a care is not a good enough reason to perpetuate the false notion of a pure LLPS type behavior. One of the earlier studies demonstrating the coupling of segregative transitions viz., phase separation, and associative transitions, viz., percolation, was published in eLife and elsewhere. Please see: https://elifesciences.org/articles/30294 and http://iopscience.iop.org/article/10.1088/1367-2630/aab8d9. Given the considerable progress made by several labs, and especially those of Mittag and Pappu on the topic of IDR phase transitions, it is imperative that the motivation for the current work not be that LLPS is "poorly understood" (see comments by Reviewer 2).

3) Please provide a coherent motivation/justification for co-opting concepts such as the fractal analysis from colloidal chemistry for the analysis of the simulations. Please note that this is not the first time fractal analyses have been brought to bear in studying phase separating IDRs. They've been previously deployed in studies of ultra-coarse grained simulations of mimics of the exon 1 encoded region of huntingtin (http://www.sciencedirect.com/science/article/pii/S0006349514007371).

4) The issues of convergence, statistical robustness, and finite size effects need careful consideration. How do the images interact with one another in the dilute and dense phase simulations. For simple liquids, even the earliest simulations deployed ca. 100 molecules for querying properties of neat liquids. How then does one justify the use of 24 copies for a complex fluid? In lattice-based simulations, the effects of finite size were systematically analyzed, the inference was that one needs at least 100+ molecules to get to coherent descriptions of two coexisting phases. The current work does not simulate coexisting phases but approaches each phase separately. So, fewer molecules are reasonable, but it must still be the case that a reasonably rigorous assessment of finite size effects is provided.

5) Regarding the differences between Arg and Lys, the sources of differences are intrinsic and context dependent. As Reviewer 2 notes, this is not as enigmatic as the authors note. Please see recent contributions that have demonstrated clear differences of Arg vs. Lys as drivers of speckle formation (https://doi.org/10.1016/j.molcel.2020.01.025), the realization that Arg and Lys are very different in terms of their intrinsic free energies of hydration (https://pubs.acs.org/doi/abs/10.1021/acs.jpcb.1c01073), and that these differences contribute directly to the cation-specificity of IDP conformational ensembles (https://www.pnas.org/doi/full/10.1073/pnas.2200559119). These physical principles and the distinction of Arg being sticky vs. Lys being non-sticky appear to also contribute to relative abundance and amino acid compositions of IDRs (https://doi.org/10.1016/j.jmb.2019.08.008).

6) The size and shape analyses (please see comments of Reviewer 1) need a lot of work and thought. It would help to probe these effects at higher resolution and greater precision.

7) Finally, the asymmetry between interactions that determine single chain dimensions vs. collective phase behavior is puzzling, as noted by Reviewer 2. Please see why this is physically unexpected for simple systems (https://www.sciencedirect.com/science/article/pii/S0006349520304884) and how an asymmetry can arise as discussed recently for prion-like low complexity domains (https://doi.org/10.1038/s41557-021-00840-w). Are the principles uncovered by Bremer et al., operative with the specific IDR studied here? If not, how is the symmetry broken?

Reviewer #1 (Recommendations for the authors):

– The manuscript will be strengthened by improving the experimental part. The phase diagrams are not "phase diagrams" in a true sense, they are solubility diagrams or state diagrams of the protein. Phase diagrams are characterized by binodal and tie-lines, which were not measured here. Please see the measured phase diagrams reported in Martin et al. (ref # 18). doi:10.1126/science.aaw8653.

– The use of BF microscopy to distinguish the "morphology" of the condensed phase provides shallow insight into the morphology and dynamics of these assemblies.

– The phase-separated condensates are considered network fluids where percolation and phase separation goes hand-in-hand. A discussion on this should be included in the current manuscript and should include how different variants that the authors studied show distinct percolation behavior. Please see https://doi.org/10.1016/j.molcel.2022.05.018.

– The idea that comes across from reading this manuscript is that IDPs/IDRs are the main driver of phase separation of proteins. This may not be true. It is fine to study an isolated IDR and its phase behavior, but one needs to acknowledge the full-length protein may display a more nuanced behavior through a combination of its IDR and other domains.

– The colloidal cluster formalism, while interesting, should be compared with experimentally determined observables, as the authors point out. Without such data, I am unsure how one can conclude that this formalism provides "a potentially universal foundation" in studying the phase separation of proteins.

– Interactions and solubility of "stickers" and "spacers" have been recently studied by Mittag, Pappu, and co-workers. Such discussions would be helpful to include here since the authors focus on a similar set of residues (R, G, Y, K). Please see https://www.nature.com/articles/s41557-021-00840-w
