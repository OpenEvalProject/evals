# Peer review - Round 1

Editors:
- Richard A Neher, https://ror.org/02s6k3f65 University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82516.sa0](https://doi.org/10.7554/eLife.82516.sa0)

Neverov and colleagues analyze patterns of correlated changes of amino acids in the SARS-CoV-2 spike protein to identify networks of interacting positions using an improved version of the previously validated method. Identifying such patterns of co-evolution is important for a better understanding of spike-protein evolution. The evidence for the identified co-evolving pairs is convincing, though the degree of certainty varies among the different identified groups of potentially interacting positions.


---

# Peer review - Round 1

Editors:
- Richard A Neher, https://ror.org/02s6k3f65 University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82516.sa1](https://doi.org/10.7554/eLife.82516.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Evidence for coordinated evolution at amino acid sites of SARS-CoV-2 spike" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Richard A Neher as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Neil Ferguson as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All reviewers agreed that you have presented a sensible and intuitive investigation of epistasis in SARS-CoV-2 Spike evolution that uncovered or confirmed epistatically interacting networks of positions. This is a valuable addition to the literature. The main points raised during the review and the ensuing discussion are

1) Please make an effort to explain your method better. All reviewers struggled with some aspects (see reviews).

2) Please extend the discussion of limitations, for example, errors in phylogenetic reconstruction.

Reviewer #1 (Recommendations for the authors):

– Are these networks specific to SARS-CoV-2? Or even specific variants of SARS-CoV-2? Or are homologous sites also co-evolving in the broader group of sarbeco-viruses? Do these networks also feature in the work by Rodriguez-Rivas?

– We are currently seeing very rapid convergent evolution in multiple lineages (mutations at positions 346, 444, 460). How does convergent evolution driven by consistent selection pressure affect the specificity to detect epistatic groups? A more extensive discussion of this would be useful.

Reviewer #2 (Recommendations for the authors):

1. Although the method has been published before, I appreciated that the authors included a description here. But I found it a bit hard to follow in places. For example, I'm not sure why the authors chose the simulations they did to set the thresholds. I think the simulations mostly involved compensatory substitutions, but wouldn't SARS-CoV-2 epistatic evolution probably mostly involve positive substitutions that then potentiate new positive substitutions that were deleterious on the old background (so skirting valleys rather than crossing them)? I also wasn't sure what was going on with the simulation results, e.g., are the false positives clustered with the true positives or disjoint? What features distinguish true positives from false negatives? (Is it just how much they evolved?)

2. I'm not sure I totally understand the distinction between concordant and discordant evolution. I thought that it was concordant evolution when the derived alleles at both sites tended to be found in the same parts of the phylogeny and discordant when they tended to be on different branches, but the authors say that A653V and S982A occurring mostly on the D614G background is an example of discordant evolution.

3. The authors say that the epistasis inferences are robust to errors in the phylogeny, but the results actually seem fairly different between the two reconstructed phylogenies. Maybe reframe this?

4. I really appreciated Figures 3-5 (the example trees), which helped visualize what these signals actually look like. But I didn't totally understand them. Are all those pale blue and red dots included or excluded from the analysis? They look like they're on terminal branches, but they're unlikely to be errors, right?

5. I would be careful not to push the "enrichment VOC-defining mutations among the interacting sites" story too hard, given that they show that this is in large part because the data from the VOCs (except Omicron) is used to find the interactions

Reviewer #3 (Recommendations for the authors):

Comments and questions:

1. From paragraph at line 99 and Methods, it isn't clear – are concurrent changes (two mutations reconstructed to occur on the same branch) included in the analysis? (My instinct from the description is that they're not.) It seems like SARS-CoV-2 evolution might quickly fix epistatically coupled mutational pairs such that they appear coincidental on the tree (e.g. Omicron emergence, where we don't have mutational intermediates), and I would expect these to be an important source of signal for epistatic couplings.

2. For the simulation studies, is it clear why the revised method doesn't have false positives in the non-epistatic control simulations but does have some falsely identified pairs in the epistatic simulation?

3. Phylogeny figures: it would be very helpful if the main text or figure legend had more of a "narrative" description of how to interpret these figures besides the visual legend. Maybe I'm misinterpreting (it's a hard phylogeny to visually parse), but it seems like the dashed lines reflective of VOC annotation in Figure 3 are very far away from being monophyletic. This is surprising, it seems like at the very least a reliable phylogeny for this analysis needs to be getting those highest-level taxonomic groupings of VOCs correct. But, maybe I'm not interpreting the phylogeny correctly (which suggests some more care might need to be taken in visualization). Upon thinking further, it may be that because so many other sequences outside of Α are collapsed into the triangles, the polyatomic representation here is all of "Α" and "Α-like" things (that are just not annotated as Α?) surrounding the basal Α emergence and my initial impression is not as concerning as it appeared.

4. It would be interesting to add more context and speculation about the sets of sites that are seen to evolve concordantly and disconcordantly. For example, discussion and citations illustrate that cluster (I) of concordant sites are within an important class of antibody epitope. Double-check this, but does cluster (III) map to the NTD "antigenic supersite"? I also really liked the discussion of the signal of disconcordance between 501 and 675/677 in the Discussion. I think aspects of these types of interpretations could be included more proximal to the initial results themselves, too, to make it more clear to the reader what the relevance is of some of these pairs.

5. The observation in line 358 and Figure 5 made me jump to the reversion bias issue that is later discussed and clearly aware to the authors given discussion at line 374. I then came to understand that the many double mutations that appear on terminal branches on the phylogeny in Figure 5 are the light color indicating that they are excluded from analysis, which was my initial suggestion before I understood that these were already excluded. Rather than have a secondary color indicating excluded mutations that don't contribute to the epistatic pair discovery algorithm (assuming I understand correctly that terminal branches are not included in the algorithm), it might be more straightforward to just exclude these mutations from visualization entirely (and more clearly state that only internal branches are queried in the algorithm).

6. It is not entirely clear to me why the other epistatic mutations described in the cited paper on RBD mutations (Starr et al. 2022) are not seen in the phylogenetic signal. For example, in Figure 3E of that reference, substitutions are tabulated as singular occurrences on the phylogeny similar to the approach here, and suggests there is more signal between 501 and 449 than just the one 449H occurrence suggested in the discussion (e.g. mutations Y449H, D, N all contribute). Could this be related to point 1. above – are co-occurring substitutions being counted in the current algorithm, or is that potentially important signal being discarded? Or different sequence/phylogeny sources?

7. I want to thank the authors for continuing their important work and their outspoken statements during these difficult political times. We're all sending positive thoughts for peace in Ukraine.
