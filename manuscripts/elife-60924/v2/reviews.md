# Peer review - Round 1

Editors:
- Christian R Landry, Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60924.sa1](https://doi.org/10.7554/eLife.60924.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

A cell is a very crowded environment that is prone to interaction promiscuity among proteins. Natural selection, therefore, acts to maintain interactions among cognate proteins but also to prevent the ones that may have deleterious consequences. Here, Lite and colleagues examine the contribution of single amino acid substitutions and their combinations to protein-protein interaction specificity using a toxin-antitoxin system. The results provide important insight into how protein-protein interactions evolve and achieve specificity in the context of gene duplication where duplicated proteins initially have the same interaction partners but eventually evolve to have their specific cognate partners.

Decision letter after peer review:

Thank you for submitting your article "The genetic landscape of protein-protein interaction specificity" for consideration by eLife. Your article has been reviewed by Olga Boudker as the Senior Editor, a Reviewing Editor, and three reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

Lite and colleagues examine the contribution of single amino acid substitutions and their combinations to protein-protein interactions using a toxin-antitoxin system. The results provide an important insight into how protein-protein interactions evolve and achieve specificity in the context of gene duplication where duplicated proteins initially have the same interaction partners but eventually evolve to have their specific cognate partners. The reviewers appreciated the quality and importance of the work. They raised several points that would need to be addressed.

1) The novelty of the present study relative to previous work by the same authors and others is not obvious. The context in which the study is anchored could be broader to better demonstrate the implications of the work. Some previous studies that relate to the present work are not discussed.

2) There are some issues regarding the way fitness is estimated across backgrounds and regarding the analysis of epistasis.

3) Many analyses are based on precise cut offs. It would be important to show that the conclusions are robust to the choice of cut off values. A more quantitative assessment of the results rather than one based on cut offs could be used.

4) Issues related to data availability were raised.

5) Protein abundance of the various mutants does not seem to be taken into account and this may be a confounding factor in the measurement of protein-protein interactions. Ideally this would be addressed experimentally but it should at least be discussed if experiments are not easily feasible in the current context or if such data is not already available.

I am leaving the individual reports appended below because they are largely non-redundant and some of the details could be useful for preparing the revisions.

Reviewer #1:

Lite and colleagues describe the contributions of individual residues on protein-protein interaction specificity in the parDE3 toxin-antitoxin system. How interaction specificity arises in PPIs, particularly after gene duplication, is an important problem in evolutionary. They use bulk competition assays, coupled with deep sequencing to quantify the degree to which mutant antitoxins can detoxify the presence of the cognate interaction partner ParE3 and a homologous, orthogonal toxin ParE2. Novel findings include a quantitative exploration of the degeneracy of the cognate parDE3 toxin-antitoxin interface towards change in the targeted residues, an assessment of the relative contributions of each selected residue towards antitoxin binding and selectivity, a structural basis for the interface differences between parDE2 and parDE3 and proof that not all positive elements serve as specificity-determining residues. The data presented in this study should be of interest to biochemists, evolutionary biologists, and geneticists, so is appropriate for eLife's general audience.

Lite et al., characterize the detoxifcation-capabilities of an antitoxin library consisting of 8000 variants, in an approach similar to a previously published study from the same authors (Aarke et al., 2015). While the new library has the advantage of being combinatorically complete, it is smaller than the library from the cited study and 2/3 of the investigated residues in this work were already mutated in the preceding study (albeit with only 13 / 10 of possible amino acids) There is an interesting difference between the previous work, which only used naturally occurring states, whereas this study uses all possible mutations. I think it would be very interesting if the authors could comment on how this might relate to the different results between the studies.

The Results section of this study makes it sound as if the specificity-switching residues were first identified herein. Overall, the similarity to previously published data and experimental setup alongside a decrease in total library size compared to previous studies, that investigate the same model system, make the novelty of this work a little less obvious. Perhaps the authors could emphasize again conceptually (apart from saturation) what new approach this study adds, and why it is crucial for our understanding of specificity.

The assay employed in this work is not capable of discriminating good antitoxins from great antitoxins (as discussed in subsection “Specificity arises from the discrimination between cognate and non-cognate partners”). To address this, the authors measure the contributions to specificity of all single amino acid changes in all possible genetic backgrounds. Such a background-independent analysis leverages the completeness of the library (and I think was first employed here, Salinas and Ranganathan, 2018) to get an average effect for each mutation, though I am a little unsure I understand that it is appropriate in this case. The authors conclude that the naturally occurring specificity-determining residues are "optimal with respect to promoting the insulation" (Introduction). It seems to me that the authors compare the fitness of each mutation in the context of all genetic backgrounds to the wild-type state in its wild-type context and not in the context of all genetic backgrounds. It is thus to be expected that the apparent fitness of antitoxins that retain the cognate amino acid in a given position (e.g. ParD3 retains a D in position 1) is <1 if they are analyzed in a background-dependent manner (e.g. DXX). This is because many of the backgrounds will contain deleterious states. So the comparison of a background averaged fitness to the fitness of the WT state in a single background seems inappropriate to me to show that the WT sequence is optimal.

Reviewer #2:

In this work, Li et al., perform an exceptionally comprehensive assessment of how individual mutations contribute to recognition specificity amongst paralogous complexes. The authors take a bacterial anti-toxin, ParD3, and construct a combinatorial saturation mutagenesis library of three positions that physically interface with the toxin, ParE3. They then measure the effects of these mutations on: (1) binding of the cognate partner, ParE3 and (2) binding of a non-cognate partner, the paralog ParE2. The authors also compare the interactions at these three positions in the crystal structures of the ParE3/ParD3 complex (previously published) and the ParE2/ParD2 (which they solved in this work).

The central result of the paper is that individual positions can act as both positive and negative elements for interaction specificity, and that "positive and negative contributions are neither inherently coupled nor mutually exclusive". That is, rather than using distinct sets of positions to either enhance cognate interactions or discourage non-cognate binding, specificity can be (but is not always) encoded in an overlapping set of residues. This has implications for both the engineering and evolution of protein interactions. The experiments appear to be of high technical quality, and we expect the results will be of interest to a diverse scientific audience in biophysics, structural biology, protein engineering and molecular evolution. We recommend publication in eLife.

Essential revisions:

1) In Figure 1B, the authors lay out two different models of how positions at a physical interface contribute to the formation of a specific protein-protein interaction. Their data demonstrate that both models apply within a single protein. Much of the impact of the paper seems to depend on how surprising (or not) this finding is, and what the consequences of this finding might be both for evolving and engineering complexes. Thus, it is necessary for the authors to provide more context that can help the reader clearly assess the impact of this work. Specifically, can more be said about why and when one model would be favored over another? What is the evolutionary implication for individual residues in a protein to have negative and/or positive roles in identifying cognate interactions? Why is it surprising that residues can carry out dual roles in recognition and discrimination in a binding partner?

2) The linear model (Figure 3—figure supplement 1, Figure 4—figure supplement 2) indicates that the effects of mutations at the anti-toxin/toxin interface can be considered near-independently. This suggests that there is little epistasis (or coupling) between positions. However, can the authors perform a more thorough analysis of second and third order epistasis? Do they see that epistasis is centered at zero for the average interaction between mutations across a pair of sites? Given that the authors have all of the data, a thorough analysis of epistasis would further support their linear model and show that the contributions of each position studied in ParD3 are independent from each other. This seems especially interesting given the spatial proximity of positions 61 and 64.

3) As the authors point out, the in vivo assays rely on induced expression of toxins and antitoxins in a heterologous host. They claim that "the relative behavior of ParD3 variants measured here is likely to apply in whatever context they arise". Can the authors show that the induction conditions do not strongly affect their measurements? One way to demonstrate this is to take a small panel of ~10-20 ParD3 mutants that have a broad range of effects on growth rate across both ParE3 and ParE2 backgrounds. The growth rate effects of mutants in this "sub-library" can then be measured across varying concentrations of IPTG (for induction of ParD3) and arabinose (induction of ParE2/E3). Does the rank ordering of the mutant growth rates effects change with induction level, or are the results indeed qualitatively similar?

Reviewer #3:

This is an interesting study that uses a combinatorially complete deep mutagenesis strategy to identify determinants of the specificity of protein-protein interactions between bacterial toxins and antitoxins using a paralogy pair as a model system. I enjoyed the manuscript: it addresses a general and important question with a good experimental design and using an elegant model system. The clarification of negative and positive contributions to specificity is conceptually interesting.

Essential revisions:

1) Many of the analyses use an arbitrary cut-off of interaction vs no interaction (W>0.5). Whilst this simplifies communication and analyses, it is important to: (1) demonstrate that the conclusions are robust to the choice of this arbitrary cut-off; and (2) to stress that this reduction in fitness is huge and in natural populations much smaller changes in fitness are likely to be selected against, especially in microbes with large effective population sizes. How does imposing a much higher fitness cut-off alter the authors' conclusions?

2) In general, and related to point [1], I would prefer to see a more quantitative treatment of the data. Defining proteins as interacting or not interacting is a bit clunky given that binding is actually a fully quantitative trait and the data here is, at least by design, also quantitative. Many of the questions addressed could be answered quantitatively rather than by using a binary categorisation of binding vs non-binding.

3) What about protein abundance? The authors don't quantify the effects of the combinatorial mutations on protein abundance, so some of the non-specific effects on binding are likely to be due to changes in concentration of the protein not the binding affinity.

4) Relationship to conclusions in previous publications from the same group: previous manuscripts from the same lab have focussed on the finding that mutational effects in protein interaction interfaces change in the presence of additional mutations in the same protein (Podgornaia and Laub, 2015 i.e. the importance of pairwise and higher order epistasis). How, quantitatively, does the current dataset compare to this previous dataset on a different system and also to previous toxin-anti toxin mutagenesis datasets? Are mutational effects less background dependent in the toxin-anti-toxin system or similarly so?

5) "Although a purely additive model of residue contributions was highly predictive of variant fitness (R2 = 0.89, SD between folds + 0.003; Figure 3—figure supplement 1B), the model was weakest for the most fit variants, likely due to diminishing returns for highly favorable residues." This is fully expected- mutations should have effects that are additive for free energy changes (ddG binding) but not for changes in protein concentration because of the non-linear relationship between the amount of protein bound to an interaction partner and the free energy of binding (dG).

6) Data processing / quality control. We tried to download the raw sequencing data from SRA using the referee token to perform some basic quality control, but it seems only possible to obtain the summary tables not the actual sequence reads (this may be an issue in general with private SRA entries). Would it be possible to get access to the raw data e.g. by making the entry fully public prior to publication for reviewing purposes?

We have noticed major issues with quite a few deep mutational scanning data analyses, including in published papers. These include inappropriate filtering such that the analysed datasets consist partly (or in some cases, largely) of sequencing errors not real variants which can seriously alter conclusions. A second issue is underestimating sampling errors due to over-sequencing. For the design of the library used here and the filtering applied, this seem unlikely to be the case. But it would still be good to run some basic checks prior to publication.

7) Introduction/ citation of prior work. An obvious missing citation given the similarity of questions, strategy, title and journal is: Diss et al., 2018. In addition, there have now been quite a few papers published that use a similar combinatorially complete deep mutagenesis design published on different molecules (proteins, RNAs) and molecular processes and very few of them are cited here. Also, the statement in the introduction that 'prior work has not used combinatorially complete libraries to systematically dissect interface residues' is a bit misleading given previous work from the Laub lab.

8) It would be useful to more explicitly state in the text the (rational for the) previous ParD mutagenesis library design in the previous publication by the same lab.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Uncovering the basis of protein-protein interaction specificity with a combinatorially complete library" for further consideration by eLife. Your revised article has been evaluated by Olga Boudker (Senior Editor), a Reviewing Editor and one of the original reviewers.

The manuscript has been improved but there are some minor remaining issues that need to be addressed before formal acceptance, as outlined below:

I would include some of the panels from Figure 2—figure supplement 2 in the main figure – as the interaction strength increases, the degeneracy of the interface decreases. I think this is an interesting point.

Figure 4C, D. It looks like, if the changes in mutational effects across genetic backgrounds are significant, that there is more sign epistasis (switches from beneficial to detrimental mutational effects) for interaction with the non-cognate partner. Is this true? Any ideas why this might be?

Figure 3—figure supplement 1D. There is a (weak) sigmoidal relationship between the fitness scores predicted by the linear model and the actual fitness scores which suggests there is global (non-specific) epistasis in this system. This may be because there is a non-linear relationship between changes in free energy and the phenotype being measured (=~binding), as may be expected from thermodynamics. And/or perhaps because of an upper or lower bound on the measurement range.
