# Peer review - Round 1

Editors:
- Richard A Neher, Max Planck Institute for Developmental Biology , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16965.028](https://doi.org/10.7554/eLife.16965.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Adaptation in protein fitness landscapes is facilitated by indirect paths" for consideration by eLife. Your article has been favorably evaluated by Diethard Tautz as the Senior editor and three reviewers, including Joachim Krug (Reviewer #2) and a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Wu et al. report fitness measurements of all possible of combinations of amino acid substitutions at 4 positions in the protein GB1. Properties of fitness or folding landscapes of proteins are fundamental determinants of evolution since they determine which mutations are permissible on which genetic background. The major contribution of this manuscript is that it for the first time measures all combinations of all amino acids at multiple (four) sites. Using this data, the authors demonstrate that indirect path often enable ascend to the global fitness maximum, even when direct path a blocked by fitness valleys.

Essential revisions:

All reviews agreed that the results reported are a significant step forward in understanding the landscapes governing evolution of proteins. Before we can recommend publication, we would like to see the following points addressed.

1) A more thorough discussion of the generality of the results. The sites were chosen to be as epistatic as possible. Hence it is not clear how representative the properties of the 4 site landscape are. Along the same lines, we would like know how the wild type genotype compares to the ensemble of possible genotypes. Where does the wild type fall in the distribution of all fitness measurements? It would be informative to have Figure 1C not only for WT and the average sequence, but also the top and bottom 5% or similar.

2) Quantification of ruggedness and the importance of higher order coefficients. Figure 3A quantifies the accuracy of the approximation of the fitness landscapes (2 allele subspaces) after inclusion of 1st, 2nd, and 3rd order effects. This is important and useful, but can be improved. Instead of plotting the correlation coefficient, plot the fraction of variance explained by each order (that is the power spectrum of the Fourier decomposition, see Neher and Shraiman, RMP, 2011 or Neidhart et al., JTB 2013). Furthermore, a distribution of the 1st, 2nd, and 3rd order variance would be easier to parse than the current overlay of many lines. Along similar lines, can one quantify whether higher-order epistasis makes the landscape more or less rugged on average? If all higher order coefficients are set to 0, does the number of accessible path go up or down?

3) Your simulations allow transitions from every amino acid to any other amino acid and hence ignore the constraints imposed by the encoding as codons. It does not seem to be a big complication to restrict transitions to those that can be achieved by single nucleotide substitutions. Does this reduction in connectivity reduce the effects of indirect path substantially?

4) Missing literature and inaccurate statements. Even if there are only two amino acids (or more generally two alleles) per site, there can still be indirect paths with mutational reversions. The statements in the second paragraph of the Main text are not accurate. The mechanisms of bypass and conversion have been discussed previously (and have not been "discovered" by the authors; Main text, fifth paragraph). Gavrilets (1997) discusses extra-dimensional bypass. Several recent papers have theoretically studied the effect of reversions on evolutionary accessibility in diallelic sequence spaces:

Julien Berestycki, Eric Brunet, Zhan Shi. http://arxiv.org/abs/1401.6894

Anders Martinsson. http://arxiv.org/abs/1501.0220

Li Li. http://arxiv.org/abs/1502.07642

The adaptation schemes referred to by the authors as 'Greedy model', 'Correlated Fixation Model' and 'Equal Fixation Model' should be placed into their proper population-genetic context. Key references are:

H. Allen Orr. Evolution, 56(7), 2002, pp. 1317-1330

H. Allen Orr. J. theor. Biol. (2003) 220, 241-247

which discuss the performance of the three types of 'adaptive walks' in the uncorrelated random 'mutational landscape' model and show, in particular, that greedy walks are much shorter than 'correlated fixation' walks which in turn are shorter than 'equal fixation' walks. This is expected to be a fairly general pattern that also appears in the results shown in Figure 4D.

5) One take home message of the manuscript is that even in the most rugged place of a protein fitness landscape, the multitude of possible mutations makes most places accessible (via detours at times). This could be a way to reconcile the seemingly contradictory observations that (i) there is a lot of epistasis/ruggedness and (ii) that amino acid preferences are preserved (work by Bloom et al) and that viruses like HIV extensively revert to a putatively optimal fitness peak after immune evasion. In high dimensions, fitness landscapes seem to be locally rugged and accessible at the same time. A more thorough discussion of the potentially wider implications of indirect path could place these results into a broader context.
