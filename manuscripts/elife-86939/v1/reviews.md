# Peer review - Round 1

Editors:
- David Ron, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86939.3.sa0](https://doi.org/10.7554/eLife.86939.3.sa0)

The authors investigate the mechanism of amyloid nucleation in a cellular system using novel ratiometric measurements, providing fundamental insight into the role of polyglutamine length and the sequence features of glutamine-rich regions in amyloid formation. The problem addressed by this study is very significant and the ability to assess nucleation in cells is of considerable value. The data, as presented and analyzed, are mostly convincing.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.86939.3.sa1](https://doi.org/10.7554/eLife.86939.3.sa1)

Numerous neurodegenerative diseases are thought to be driven by the aggregation of proteins into insoluble filaments known as "amyloids". Despite decades of research, the mechanism by which proteins convert from the soluble to insoluble state is poorly understood. In particular, the initial nucleation step is has proven especially elusive to both experiments and simulation. This is because the critical nucleus is thermodynamically unstable, and therefore, occurs too infrequently to directly observe. Furthermore, after nucleation much faster processes like growth and secondary nucleation dominate the kinetics, which makes it difficult to isolate the effects of the initial nucleation event. In this work Kandola et al. attempt to surmount these obstacles using individual yeast cells as microscopic reaction vessels. The large number of cells, and their small size, provides the statistics to separate the cells into pre- and post-nucleation populations, allowing them to obtain nucleation rates under physiological conditions. By systematically introducing mutations into the amyloid-forming polyglutamine core of huntingtin protein, they deduce the probable structure of the amyloid nucleus. This work shows that, despite the complexity of the cellular environment, the seemingly random effects of mutations can be understood with a relatively simple physical model. Furthermore, their model shows how amyloid nucleation and growth differ in significant ways, which provides testable hypotheses for probing how different steps in the aggregation pathway may lead to neurotoxicity.

In this study Kandola et al. probe the nucleation barrier by observing a bimodal distribution of cells that contain aggregates; the cells containing aggregates have had a stochastic fluctuation allowing the proteins to surmount the barrier, while those without aggregates have yet to have a fluctuation of suitable size. The authors confirm this interpretation with the selective manipulation of the PIN gene, which provides an amyloid template that allows the system to skip the nucleation event.

In simple systems lacking internal degrees of freedom (i.e., colloids or rigid molecules) the nucleation barrier comes from a significant entropic cost that comes from bringing molecules together. In large aggregates this entropic cost is balanced by attractive interactions between the particles, but small clusters are unable to form the extensive network of stabilizing contacts present in the larger aggregates. Therefore, the initial steps in nucleation incur an entropic cost without compensating attractive interactions (this imbalance can be described as a surface tension). When internal degrees of freedom are present, such as the conformational states of a polypeptide chain, there is an additional contribution to the barrier coming from the loss of conformational entropy required to the adopt aggregation-prone state(s). In such systems the clustering and conformational processes do not necessarily coincide, and a major challenge studying nucleation is to separate out these two contributions to the free energy barrier. Surprisingly, Kandola et al. find that the critical nucleus occurs within a single molecule. This means that the largest contribution to the barrier comes from the conformational entropy cost of adopting the beta-sheet state. Once this state is attained, additional molecules can be recruited with a much lower free energy barrier.

There are several considerations in interpreting this result. First, the height of the nucleation barrier(s) comes from the relative strength of the entropic costs compared to the binding affinities. This balance determines how large a nascent nucleus must grow before it can form interactions comparable to a mature aggregate. In amyloid nuclei the first three beta strands form immature contacts consisting of either side chain or backbone contacts, whereas the fourth strand is the first that is able to form both kinds of contacts (as in a mature fibril). This study used relatively long polypeptides of 60 amino acids. This is greater than the 20-40 amino acids found in amyloid-forming molecules like ABeta or IAPP. As a result, Kandola et al.'s molecules are able to fold enough times to create four beta strands and generate mature contacts intramolecularly. This authors make the plausible claim that these intramolecular folds explain the well-known length threshold (L~35) observed in polyQ diseases. The intramolecular folds reduce the importance of clustering multiple molecules together and increase the importance of the conformational states. Similarly, manipulating the sequence or molecular concentrations will be expected to manipulate the relative magnitude of the binding affinities and the clustering entropy, which will shift the relative heights of the entropic barriers.

The authors make an important point that the structure of the nucleus does not necessarily resemble that of the mature fibril. They find that the critical nucleus has a serpentine structure that is required by the need to form four beta strands to get the first mature contacts. However, this structure comes at a cost because residues in the hairpins cannot form strong backbone or zipper interactions. Mature fibrils offer a beta sheet template that allows incoming molecules to form mature contacts immediately. Thus, it is expected that the role of the serpentine nucleus is to template a more extended beta sheet structure that is found in mature fibrils.

A second point of consideration is the striking homogeneity of the nucleus structure they describe. This homogeneity is likely to be somewhat illusory. Homopolymers, like polyglutamine, have a discrete translational symmetry, which implies that the hairpins needed to form multiple beta sheets can occur at many places along the sequence. The asparagine residues introduced by the authors place limitations on where the hairpins can occur, and should be expected to increase structural homogeneity. Furthermore, the authors demonstrate that polyglutamine chains close to the minimum length of ~35 will have strict limitations on where the folds must occur in order to attain the required four beta strands.

A novel result of this work is the observation of multiple concentration regimes in the nucleation rate. Specifically, they report a plateau-like regime at intermediate regimes in which the nucleation rate is insensitive to protein concentration. The authors attribute this effect to the "self-poisoning" phenomenon observed in growth of some crystals. This is a valid comparison because the homogeneity observed in NMR and crystallography structures of mature fibrils resemble a one-dimensional crystal. Furthermore, the typical elongation rate of amyloid fibrils (on the order of one molecule per second) is many orders of magnitude slower than the molecular collision rate (by factors of 10^6 or more), implying that the search for the beta-sheet state is very slow. This slow conformational search implies the presence of deep kinetic traps that would be prone to poisoning phenomena. However, the observation of poisoning in nucleation during nucleation is striking, particularly in consideration of the expected disorder and concentration sensitivity of the nucleus. Kandola et al.'s structural model of an ordered, intramolecular nucleus explains why the internal states responsible for poisoning are relevant in nucleation.

To achieve these results the authors used a novel approach involving a systematic series of simple sequences. This is significant because, while individual experiments showed seemingly random behavior, the randomness resolved into clear trends with the systematic approach. These trends provided clues to build a model and guide further experiments.

There has been discussion in the review process about whether a monomeric nucleus is consistent with established properties of huntingtin aggregation. I do not see a problem with an energetically unfavorable conformational state preceding a concentration-dependent growth step. The authors make the case for this sequence using a schematic free energy landscape (Fig 6) that has many similarities to a free energy landscape derived from models of polyQ nucleation (Phan et al. 2022, see Fig. 6). The theory does not consider molecules large enough to form the conformational state described by Kandola et al., but the transition state is otherwise very similar.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.86939.3.sa2](https://doi.org/10.7554/eLife.86939.3.sa2)

Kandola et al. explore the important and difficult question regarding the initiating event that triggers (nucleates) amyloid fibril growth in glutamine-rich domains. The researchers use a fluorescence technique that they developed, dAMFRET, in a yeast system where they can manipulate the expression level over several orders of magnitude, and they can control the length of the polyglutamine domain as well as the insertion of interfering non-glutamine residues. Using flow cytometry, they can interrogate each of these yeast 'reactors' to test for self-assembly.

In the introduction, the authors provide a fairly thorough yet succinct review of the relevant literature into the mechanisms of polyglutamine-mediated aggregation over the last two decades, as well as a fairly clear description of the experimental techniques they developed.

Their assay shows that the fraction of cells with AmFRET signal increases strongly with an increase in polyQ length, with a threshold around 35-40 glutamines. This roughly correlates with the Q-length dependence of disease. The experiments in which asparagine or other amino acids are inserted at variable positions in the glutamine repeat are creative and thorough, and the data along with the simulations provide compelling support for the proposed Q zipper model. The experiments are strongly supportive of a model where formation of the beta-sheet nucleus is within a monomer. This is a potentially important result, as there are conflicting data in the literature as to whether the nucleus in polyQ is monomer.

The authors present convincing data that there are differences in the structural stability of their "QU" versus "QB" aggregates. However, the conclusion that "QB" must have multilamellar architecture versus "QU" was feasible but less compelling.

The authors present intriguing data showing that amyloid formation does not monotonically increase with increasing concentration, and their conclusion that high concentrations of polyQ can 'self-poison' amyloid growth is supported by the experimental data. The discussion surrounding the mechanism by which 'self-poisoning' occurs is confusing. The authors variously discuss that soluble oligomers must be the inhibitory species, that dead-end products of Q zipper nuclei are the inhibitory species, or that self-poisoning occurs because conformational conversion at the templating surface is slow relative to the rate of arrival of new molecules to the surface. The data seem consistent with an argument that, at high concentrations, non-structured polyQ oligomers form which interfere with elongation into structured amyloid assemblies - but it is not clear why such oligomers would be zippers.

Overall, this is a very valuable and thorough exploration of the fundamental question as to the nature and identity of the nucleating species in polyglutamine aggregation.
