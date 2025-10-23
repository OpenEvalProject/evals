# Peer review - Round 1

Editors:
- Richard A Neher, University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72516.sa0](https://doi.org/10.7554/eLife.72516.sa0)

This paper presents a systematic analysis of the fitness landscape of the influenza virus protein neuraminidase (NA). The authors generate 864 different combinations of amino acids at seven positions in six genetic backgrounds sampled 10 years apart and measure the fitness of the resulting virus. This fitness landscape is characterized by strong epistatic interactions, including a strong tendency to maintain the local charge of the protein. Such systematic characterizations of important proteins of viral pathogens are crucial to develop principled models to understand and predict their evolution.


---

# Peer review - Round 1

Editors:
- Richard A Neher, University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72516.sa1](https://doi.org/10.7554/eLife.72516.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Antigenic evolution of human influenza H3N2 neuraminidase is constrained by charge balancing" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Richard A Neher as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Betty Diamond as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Christopher J R Illingworth (Reviewer #2); Claus O Wilke (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The primary conclusion from your work is that evolution of NA is heavily constraint by charge balancing and that this constraint could potentially be used to predict evolution. It would be great if this could be quantified. How does the realized trajectory compare to an ensemble of possible ones? How many of the past substitutions could have been predicted? Are similar constraints seen in homologous regions of A/H1N1 of B? Some additional exploration of this would strengthen the paper.

2) The structural interpretation of the results could potentially be strengthened by analyzing side-chain positions rather than C-α positions. Comparisons of structures with different local charge might also be informative.

3) The variation among the estimates of additive effects is surprising. Is this variation smaller between similar backgrounds (10 years apart) compared to distant backgrounds? How well does an "additive only" model fit the data and how variable are the inferred effects? Some additional discussion of this would help.

4) The experiments presented here are different from most DMS experiments: All possible combinations of a subset of mutations are analyzed, rather than all possible point mutations. It would be good to highlight this difference and possibly use a different term.

The reviews below contain a number of other suggestions that we encourage you to consider.

Reviewer #1 (Recommendations for the authors):

– I have trouble interpreting the result that additive fitness effects are all over the place when comparing backgrounds, while pairwise effects are conserved. How much does this depend on the model choice? You could also use un-ambiguous Fourier transformation on subsets of binary hypercubes. And fit a model with only addititive coefficients. How much would the coefficients vary in that case? How much less variance is captured? Is there a sense that additive fitness effects are more strongly correlated with comparing backgrounds 10y appart then 20, 30, 40y apart?

– The part on analyzing natural variation in charge and prediction could be expanded and explored a little more. Net charge of the regions tends to be either -1,0, or +1, but it is not apriori clear that the realized trajectory is much more narrow in its charge distribution than random permutations of the mutations of the last 50 years are. From the experimental data, a charge of -2 seems better than +1, but +1 has been dominant in the last few years, while -2 is only sporadically observed. There is of course only one realization with a long correlation time. To strengthen the case for predictive power, would it be feasible to repeat this analysis on homologous residues in H1N1 (and maybe B and the H1N1pdm)?

Reviewer #2 (Recommendations for the authors):

1. The authors note that the region studied is subject to antigenic evolution. To what extent do the authors believe that charge balancing imposes a negative constraint upon evolution, as opposed to epistasis driving compensating changes in NA under positive selection following an immunologically driven change in the virus that coincidentally impacts residue charge? This is not to nullify the finding, but of the substiutions observed in this region over time, how many could have been predicted in advance on the basis of fitness landscapes derived here (accounting for their charge or non-charge effects)? Can the authors predict likely changes in this region that are likely to be observed next?

2. With this in mind, I found Figure 5a hard to understand or interpret. Would it be possible to show the data in a way that highlights the frequency of haplotypes by charge against time? I would find this easier to follow.

3. A small amount of work has been done looking at the consequences of charge for the local structure, though sidechain positions might be a little stochastic between crystal structures. Are there any consistent changes in structure arising from changes in local charge? That is, if multiple structures with different charge distributions are locally aligned (e.g. using VMD to perform local structural alignment on backbone atoms and RMSD to assess differences), are any changes in local conformation evident?

4. I am perhaps not sufficiently familiar with the terminology to understand what exactly was done in the virus rescue experiment. Could more details be provided?

5. Is it possible, potentially via a more superficial analysis, to suggest whether the region of charge conservation in NA might be preserved beyond the region under study? I am happy if the authors don't want to go down this route, though I wonder whether a figure along the lines of a revised Figure 5A would show possible routes for future exploration.

Reviewer #3 (Recommendations for the authors):

I think you need to be absolutely clear about whether you performed six experiments of 864 variants or 864 deep mutational scanning experiments of every possible mutation in NA. I think you did the former, but in many places the manuscript reads as if you did the latter. If you did six experiments of 864 variants, I believe you shouldn't use the term "deep mutational scanning" at all.

Neuraminidase has almost 400 residues, so a deep mutational scan of one NA variation would require almost 8000 mutations, ten times more than one of your experiment did (assuming you did only six experiments).

I also would like to emphasize that one of the main strong points of your study (if I understand correctly what you did) is that you systematically explored all possible combinations of a set of mutations. This is very different from deep mutational scanning, which usually only looks at single mutations and maybe sometimes at mutation pairs. By emphasizing deep mutational scanning, you are drawing attention away from this aspect of your study, even though that's the primary selling point of your study in my opinion.

Additionally, redoing the analysis of Figure 4 with side-chain distances should be straightforward. You could use either the smallest distance among all heavy atoms or the distance between the geometric center of the sidechain atoms, whichever is easier for you to calculate. Both should give you approximately the same results.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Antigenic evolution of human influenza H3N2 neuraminidase is constrained by charge balancing" for further consideration by eLife. Your revised article has been evaluated by Betty Diamond (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Thank you very much for submitting the revision. I still think this study is elegant and important (as did my co-reviewers). Unfortunately, the additional analyses you have done did not provide strong support for the claim that charge conversation can be used to predict influenza evolution, while the central claim of charge being an important constraint remains convincing. I therefore think some parts of the manuscript need to be toned down. The last two sentences of abstract, for example, seem too strong:

"In addition, we show that residue coevolution in this antigenic region can be predicted by charge states and pairwise epistasis. Overall, this study demonstrates the importance of quantifying epistasis and the underlying biophysical constraints for building a predictive model of influenza evolution."

The main evidence that charge constrains natural evolution is the concordance of co-evolution scores and pairwise epistasis. I think it should be better explained what can and what can not be concluded from this and in what sense this is predictive.

The definition of the score is also somewhat confusing and I think there are some problems around lines 470 and 471. Why is si summed over when si is an argument to \delta f? The text below doesn't help to resolve the matter.

It would be nice if you made it a bit easier for the reader to piece together what exactly happened in natural H3N2 populations in the past 50y. Figure 1c shows the trajectories, but it is at times tough to link colors with amino acids and the associated changes in charge. Highlighting which events change charge would be helpful. These events underlie Figure 5a and ultimately Figure 5c. It should be possible to show more explicitly how these are connected, maybe by combining only charge changing frequency trajectories into one graph or by increasing panel 5a and annotating the curves with the underlying changes in genotype.
