# Peer review - Round 1

Editors:
- John Kuriyan, Howard Hughes Medical Institute, University of California , , Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.09410.013](https://doi.org/10.7554/eLife.09410.013)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "A vocabulary of ancient peptides at the origin of folded proteins" for peer review at eLife. Your submission has been favorably evaluated by John Kuriyan (Senior editor) and three reviewers.

The following individual responsible for the peer review of your submission has agreed to reveal his identity: Rob Russell (peer reviewer).

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Review:

In this most interesting study, Lupas and colleagues hypothesize that modern protein domains arose from ancestral peptides. This is not a new idea; however, the current work is a systematic study of many proteins, while previous work focused on individual fold families. The authors have systematically revisited the original "antecedent domain segment" notion for protein structure, published some 15 years ago, by now using a systematic interrogation of structure and sequence. The authors identify 40 short 3D-structural motifs (they call them "fragments") that are most likely to be some of the ancestral primordial peptides that gave rise to the present-day protein world. These are subdomain-size segments found by sequence profile similarity and validated by 3D structure similarity. They typically lack a well-defined hydrophobic core and are complemented to form complete domains in several different and likely evolutionarily independent ways.

This work stems from a hypothesis that proteins originated by fusion of ancestral peptides. These peptides likely functioned in complex with RNA. The crux of the authors' argument is that subdomain sequence similarity between different domains indicates deep homology for the subdomain. Because the containing domains are not homologous, they argue that the homology at the subdomain level indicates an ancestral peptide shared by the domains. They further argue that this sequence similarity does not arise from structural constraints on sequence, as similar subdomain structures with apparently unrelated sequences can be found. The authors' arguments are mostly clear. They also do not overstate their conclusion that these peptides are ancestral, which necessarily remains somewhat speculative.

This study is made possible by the development of the HHsearch algorithm to find statistically supported similarity between sequence profiles. While some of the HHsearch hits represent false positives, most are predictive of 3D structure, as has been validated in many CASP experiments. It is indeed most likely that if the HHsearch sequence-based alignment is nearly the same as the 3D structure-based alignment then the two segments are homologous. This is the main assumption of this work.

Some of these fragments have been detected before and studied, e.g. in the SISYPHUS database and various publications (e.g. about HHH motifs), but this manuscript provides the first principled and comprehensive approach to find them all and therefore deserves attention. Interestingly, no example of multiple different peptides in any fold was found, which goes slightly against the original idea, though multiplication/repetition of fragments seems definitely to have been a theme in the evolution of the folds.

In summary, the elaboration presented in this paper of the idea that short sub-structure motifs might have arisen through primordial interactions with RNA will be of general interest to the readership of eLife, and the paper is potentially suitable for publication provided that the authors can address the following issues raised by the referees.

Important issues to address:

1) There is concern about the argument that the sequence correlation between these motifs must arise from history rather than convergence. This argument – the core argument in the paper – hinges on the idea that the sequence space compatible with the subdomain motif is too vast to lead to chance convergence. The authors do not, however, provide any estimate for the number of sequences compatible with a given subdomain motif. Their median fragment length is 24 residues. How many different amino acids can be tolerated at each site in the fragment? With what probability? If only a few amino acids can be tolerated at each position, the space associated with a 24 residue fragment could be quite small, potentially leading to a spurious signal of homology.

The reviewers wonder whether it would be feasible to compute more of a significance of the overall observation (i.e. considering whether such a distribution of sequence similarities might be expected by chance) than just what seems to be a rather lenient sequence similarity measure. The reviewers are concerned that the authors support the lack of convergence with anecdotal rather than statistical analysis.

As an aside, the reviewers recognize that a compelling point is that these ancient peptide candidates are associated with ancient functions, and perhaps this isn't emphasized enough in the paper.

2) One thing that is missing is more discussion of the fragments that were common, but not significant in terms of sequence. For instance, the point about there being no single fold containing two fragments leads to the question of just how many there were that satisfied only stringent structural criteria. The reviewers realise that this is considerable work, but wonder if the authors have these data lying around anyway. For example, of the most popular folds, how many have two common fragments or more, even if HMMsearch doesn't give a significance? This would lend some insight into the really ancient, no-longer-detectable, but still related relationships.

3) Some discussion of some old favorites is also missing. The two halves of the Immunoglobulin fold or Rossmann fold, etc. – that is the cases that most structurally-obsessed readers will have in their minds, could also, if fitting, do with some discussion in the same light.

Other issues to address:

1) The authors can reference more relevant publications (e.g. SISYPHUS and those dedicated to individual motifs, like HHH).

2) The description of your methods to establish the statistical cutoffs for sequence and structural similarity took multiple reads to understand (both in the text, Results and discussion, and in the graphic and legend of Figure 2). Highlighting the fragments on Figure 2 might help.

3) "domains might not constitute the evolutionary unit of protein structure" might better be stated as "domains might not constitute the only evolutionary unit of protein structure"
