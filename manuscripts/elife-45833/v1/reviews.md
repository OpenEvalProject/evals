# Peer review - Round 1

Editors:
- Marc Lipsitch, Harvard TH Chan School of Public Health United States

Reviewers:
- Christian Gortazar, Instituto de Investigación en Recursos Cinegéticos IREC Spain

## Review text

DOI: [10.7554/eLife.45833.sa1](https://doi.org/10.7554/eLife.45833.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Combining genomics and epidemiology to analyse bi-directional transmission of Mycobacterium bovis in a multi-host system" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Neil Ferguson as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Christian Gortazar (Reviewer #3).

The reviewers have discussed the reviews with one another, and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This is a population genomics study of the transmission of M. bovis between two nonhuman animal hosts, cattle and badgers, a matter of considerable ecological and practical interest.

Summary:

This is an analysis of the multispecies badger-cattle transmission system using genomic and epidemiological data to characterize the transmission of M. bovis between these species, a matter of considerable interest.

Strengths include the sizable and detailed data set, and the relatively clear exposition of what analyses were done.

Essential revisions:

The major required revision is to place the work in the context of clear hypotheses, predictions of these hypotheses for the results of analyses, and interpretation of the analyses as they inform our judgment on those hypotheses. As currently written, like many pathogen genomics papers, this paper presents analyses and results, but leaves the rationale for the analyses and the interpretation of the results in terms of scientific hypotheses unclear. While this is not atypical for papers in the field, it makes it very hard for an interested non-specialist in the subject matter (ecology of M. bovis) to appreciate the paper. For a general interest journal like eLife, it is problematic because the reader is left with an unclear sense of what has and has not been shown.

It seems that the major hypotheses being tested revolve around the extent to which badgers are a reservoir for cattle M. bovis infection. Put somewhat more precisely, finding that they are a reservoir would mean that badger-badger transmission sustains the infection, that badger-to-cattle transmission is frequent and is the source (immediate or ultimate) of most cattle infections.

There are four main types of analysis in this paper. In a revised version we would expect each of these to be motivated explicitly by "we hypothesized x and tested it using this method and found that results were/were not consistent with x”. This is the main missing item in the paper.

1) Random forest and boosted regressions. The reason for doing both is unclear, and the boosted regressions are not described much at all. The RF method seems perhaps to be testing the plausibility of the idea that genetic distance indicates likely transmission. This seems more or less borne out by the main results where spatial and social proximity have strong explanatory roles (the sign is not stated but I assume that epi distance and genetic distance are positively related). I'm not sure that I'd expect such a relationship to hold over the full scale of distances (beyond some distance I would think there would be no relationship anymore) but this is a detail. The finding that "same host" has no role in the RF is quite weird – usually isolates from the same host would be nearly identical. No explanation is given for why the many different network and spatial measures are used, or which one expects to be positive in such a complex model, especially assuming that this is multivariable, so they are all conditional on the others. Overall, the RF seems maybe to be consistent with the data being of high quality and with transmission being related to short genetic distance, but not to clearly refute or confirm any hypothesis. Please clarify why these analyses were done and what the results mean.

2) Phylogenetic reconstruction. Here most of the clades have high probability of ancestral nodes being in cattle, seemingly inconsistent with the badger-reservoir hypothesis. Please comment on how these results should be interpreted.

3) The epidemiological descriptive data, where badgers seemed to have it long before cattle. Seems consistent with the reservoir hypothesis, though badgers are also much more widely sampled. Please make this explicit (modified if it has been misunderstood).

4) The structured coalescent analyses, in which badger-to-cattle transmissions seem to be much more common than the reverse under nearly all models, including the best-supported ones. One aspect that confuses me is that presumably the different lifespans of the hosts lead to different durations of the infection, so I am not sure if number of transmissions per unit time is the best measure of transmission. But taken at face value this seems consistent with the reservoir hypothesis. Please clarify what you think the interpretation is, and in particular (two reviewers wondered) whether these can be interpreted as the ratio of rates (transmissions per unit time), of basic or effective reproductive numbers (transmissions per infection), or something else that has physical interpretation.

Assuming that the Reviewing Editor, a nonexpert in the substantive field, has understood the above correctly, please modify the discussion to give careful consideration of the contrasting observations (3 and 4 support the hypothesis, 2 argues against it) and how they can be reconciled. If the authors can convincingly do that and answer (even with uncertainty) a clear scientific question, this could become publishable.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Combining genomics and epidemiology to analyse bi-directional transmission of Mycobacterium bovis in a multi-host system" for further consideration at eLife. Your revised article has been favorably evaluated by Neil Ferguson (Senior Editor), a Reviewing Editor, and one reviewer.

This paper has been extensively revised, and the scientific logic is now far clearer. There are some remaining issues that need to be addressed before acceptance, as outlined below:

1) The sampling selected for genetically similar isolates in the two host species, which will (I believe in all cases) increase the estimated transition rates above that which is typical for all strains. For example, any spoligotypes that are not transmitted between the species will not be counted. This is an important caveat to the conclusions about the frequency of interspecies transfer and needs to be explicit in the Discussion.

2) The phylogeny and BASTA analyses document interspecies transfer in both directions. The regression trees seemingly show the relevance of within-species transmission. Neither alone nor together do they answer the question of reservoir – is transmission in either species sufficient on its own for maintenance of the infection and continuing spillover into the other? The Discussion recommends integrated control, and intuitively this seems sensible, but on their own evidence of transmission within each species and between the two does not prove that essentially R_0{ii} >1 for either species, where ii represents transmission from species i to species i, and this is a condition for i to be a reservoir. I believe that the data are formally consistent with the possibility that eradication in either species would eradicate in the other (seems unlikely, as it requires a big role for interspecies transmission) or, more plausibly, that eradication in one species would eliminate it in the other because R0 within that species <1. If this reasoning is wrong, please refute. If it is right, please note this in the discussion and soften the call for integrated control.

3) Is there any way to quantify the ratio of within to between-species transmissions? This is hinted at frequently, but the numbers are never given.

4) The inclusion of a factor in the RF and BRT analyses does not guarantee that it is included in the expected direction. Can the authors report the direction of the effect for each included factor and explain any discrepancies from expectation, e.g. that overlapping lifespan = lower distance?

5) Can the authors explain, in Figure 3 a)what "mean posterior probability of each rate" means (I think it means posterior probability that it is positive) and b) why the ratio of transition counts and ratio of transition rates is so different?

6) No clear answer was given to essential revision 4, which asked in what if any sense these transition rate ratios can be interpreted as reproductive number ratios or something else epidemiological. Please comment on this in the Discussion. Also please edit carefully to use "transition" rather than "transmission" or explain why both these terms appear (as far as I can tell interchangeably) in the text.
