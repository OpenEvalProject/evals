# Peer review - Round 1

Editors:
- Magnus Nordborg, Austrian Academy of Sciences Austria

Reviewers:
- Matthew V Rockman, New York University United States
- John Kelly, University of Kansas United States

## Review text

DOI: [10.7554/eLife.42014.048](https://doi.org/10.7554/eLife.42014.048)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "An integrative genomic analysis of the Longshanks selection experiment for longer limbs in mice" for consideration by eLife. Your article has been reviewed by Patricia Wittkopp as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Matthew V Rockman (Reviewer #2); John Kelly (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper uses a combination of theoretical and empirical population genetics, functional genomics, and developmental genetics to elucidate the molecular basis for the response in a long-term selection experiment for mice with longer limbs. The authors demonstrate the contribution of major loci (one of which, Nkx3-2, is identified) as well as a polygenic background, providing one of the most detailed analyses of a selection response to date.

Essential revisions:

Standard eLife practice is to provide a condensed decision letter instead of individual reviews, but because the reviews in this case are very well written and in perfect agreement (not to mention positive!), doing so would be a disservice to the authors. Thus, we attach the full reviews and simply list the essential revisions here.

First, it must be made clearer which data are new, and which were previously published (presumably in Marchini et al., 2014).

Second, although the polygenic analysis is an important part of this paper, we noted that no formal comparison with a simpler QTL model is included. How much of the selection response was due to each? Either add some analysis along these (perhaps test how adding more loci improves cross-replicate prediction?), or tone down the language.

Reviewer #1:

The manuscript by Castro et al., dissects the genomic signatures underlying the phenotypic response to artificial selection in the Longshank experiment. The authors find that the response to selection is a composite of subtle allele frequency changes across the whole genome (polygenic response) and major allele frequency changes in some individual loci. Interestingly, they find that only two of such "major effect" loci are found in both replicates, with rest of them being unique to each replicate line. They focus on one of the major effect loci, and dissect it down to three SNPs that result in a de-repression of bone growth.

This is a well written and easy to read manuscript, with a very interesting and rigorously explored dataset. I particularly like the way the authors push the story from a "signature of selection" perspective to explore the relative importance of polygenic vs major-effect-loci underlying rapid response to selection. The array of assays and datasets used across the paper were very well integrated. In particular, I find that the use of TADs to define candidate regions added more meaning to such definition than the traditionally-used LD blocks. I think the evolutionary community, in general, will be interested in this manuscript.

1) This study is based on the selection experiment by Marchini et al., (2014). However, in the text it is never clear which data are new and which are from Marchini, 2014 (e.g. there they explore mice up to the thirteenth generation). The only hint is in the Introduction. The way the text is currently written suggests the Lonshank experiment is a new contribution of this manuscript.

2) The authors claim that an infinitesimal model with linkage "best fits the observed data" (subsection “Sequencing the Longshanks mice reveals genomic signatures of selection”). However, it is not clear from the text or the supplement which other models (e.g. few genes of major effect, or a combination of polygenic and major effect loci), besides the infinitesimal model, were tested. The simulations regarding selection coefficients and LD are clear, but I couldn't find any other model regarding the general architecture of the trait.

3) The paper highlights the importance of standing genetic variation in rapid adaptive responses, and the validation of the candidate SNPs exemplifies this beautifully. However, nothing is mentioned about de novo mutations and the role they could play. A discussion about the relative importance of these two factors, or at least the mention of how many de novo SNPs were found in F17 is warranted. I acknowledge that it is not possible to test whether de novo SNPs increased in frequency in the population given that only F0 and F17 were sequenced.

4) The results are very interesting but poorly discussed. The Discussion section is focused more on highlighting the results than in actually discussing the findings in the context of previous selection studies. I would like to see the data discussed in the framework of what we expect or have seen before regarding e.g. the role of standing variation vs de novo mutations, polygenic vs major-loci signatures of selection, coding vs non-coding changes, etc. These are current (and old) debates in evolutionary biology that will benefit a lot from the results of this paper. Also, the fact that only two loci are replicated between LS1 and LS2, and that everything else, including other major-effect loci are unique to each line is mentioned in pass in the results but never discussed.

5) Related to the above point. In the Discussion section the effect size of the major loci is mentioned to be 10%, is this a high, low? Expected? There's no discussion about the effect sizes in terms of what other studies might have found. If 10% is the effect of a single locus how much is attributed to the polygenic component? Is there something else left to be explained? If modelling uses only standing-variation, is there a role for de novo mutations?

Reviewer #2:

I think this is really beautiful work at several levels, and in particular the very careful analysis of expectations under polygeny is exceptional. The clear demonstration that polygenic adaptation would leave almost no signature in data of this type is terrific.

My one substantive concern is that the authors conclude that polygeny played an important role in the evolution of their focal trait (e.g., line 188-190, and in the abstract), but it's not actually clear to me how much evidence there is to support that conclusion. Most of the genome is similar to their polygenic null expectation, but not all: they detected eight genome-wide significant loci, and they show an excess of signal below that threshold (e.g., Figure 2—figure supplement 2, maybe Figure 3A, maybe Figure 6A). Further, there's not obviously a test that compares their results to a qtls-but-no-polygenes null. I'd like to see more explicit accounting of *how much* variation is explained by polygenic effects.

A second very modest concern has to do with the circular mating scheme, which is mentioned only deep in the supplementary methods. I'd like to see this explained more. As I understand it, each mouse mates only once, yielding a single brood. In that case, circular mating involves lots of obligate first-cousin matings, preserving F-sub-B at the expense of F-sub-W. The higher frequency of autozygosity under this scheme will slightly reduce effective recombination relative to the genetic map. I *think* that the simulations account for this as they use the actual pedigree, but that should be stated more clearly. The increased autozygosity also changes the potential role of dominance in the estimation of the selection coefficient for Nkx3-2, although I'm sure it's a very slight effect.

Reviewer #3:

In this paper, Castro et al., analyze genomic data from a selection of mice. Two replicate populations were selected for long legs for 20 generations and compared to a single control population. There was a moderate response to selection, parallel in both replicates at the phenotype scale. Castro et al., follow-up on one major locus with functional genetic experiments. These provide evidence for the involvement of the gene Nkx3-2 in the response to selection. The dissection of the QTL down to 6 candidate quantitative trait nucleotides (QTNs) is a noteworthy advance for this kind of work in mice.

As a model for nature, the results apply only to very small populations. Perhaps this is the intention as these would be under greatest conservation threat. The result that parallel evolution was limited to loci of largest effect is entirely expected given the small population size. As population size increases, selection would become increasingly deterministic and parallel change more likely.

A strong feature of the experiment is that the full pedigree of the population is known. This allows the simulation modeling based directly on the pedigree of the population. However, several things here need to be further developed or clarified. Regarding the pedigree, why not use this to test for a change in the additive variance over the course of the experiment. The most important practical effect of having large effect loci for quantitative traits is that additive (co)variances change on the same time scale as means with selection. Figure 1B,C does suggest a slowing of response in the latter half of experiment. Can this be attributed to a reduction in the additive variance? If estimated, can the change be explained in terms of the allele frequency shifts at the 'major' loci?

Related to this, the text in subsection “Linking molecular mechanisms to evolutionary consequence” suggests that 1569 mice were genotyped at the major locus. The authors look at allele frequency change. However, the paper suggests that they also have individual phenotypes for each of these same mice. If so, the authors can estimate QTL effect on phenotype directly. An estimate for the average effect could be coupled with the known strength of selection on the phenotype to produce an independent prediction for allele frequency change. This procedure would not be associated with the "winner's curse" problem (effect overestimation of outliers) that the authors correctly note about the cumulative δ p estimate.
