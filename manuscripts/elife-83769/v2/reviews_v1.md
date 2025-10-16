# Peer review - Round 1

Editors:
- Bernard de Massy, https://ror.org/02feahw73 CNRS UM France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83769.sa0](https://doi.org/10.7554/eLife.83769.sa0)

This paper presents a theoretical model of the evolutionary dynamics of Prdm9-dependent meiotic recombination hotspots. This study provides important insights. It shows that selection acts to limit the number of hotspots and to increase hotspot symmetry. This is consistent with the proposed role of PRDM9 in coordinating DSB formation and repair. Although the authors did not explore all possible scenarios, the conclusions are convincing and open up directions for extending the model and testing some of its predictions.


---

# Peer review - Round 1

Editors:
- Bernard de Massy, https://ror.org/02feahw73 CNRS UM France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83769.sa1](https://doi.org/10.7554/eLife.83769.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Down the Penrose stairs: How selection for fewer recombination hotspots maintains their existence" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Bernard de Massy as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Jessica Tyler as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Sylvain Glemin (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Introduction could be reduced.

2) The objective of each step of the model is not clearly explained and it is left to the reader to understand where the authors want to go. At first read, it is not clear whether the authors present an analysis of the model or simulation results and why they do that. So, the results part deserves rewriting and re-organization to guide the reader.

3) The choice of key parameters is justified except for Prdm9 occupancy, and potential competition between different Prdm9 variants for DSB activity.

4) Developing the specific predictions relative to previous red-queen models, for Prdm9 diversity in human and mice, for gene dosage effects reported in mice.

5) Some more explanation about the difference between the Penrose stair and the Red-queen.

6) Several clarifications on the data presented in the figures are also required.

Reviewer #1 (Recommendations for the authors):

A few specific points also require clarification:

1) In the model, the question of competition is not entirely clear.

There may be different levels of competition:

­– Competition for binding of Prdm9 to its sites (this will depend on affinity and protein level);

Figure 1A indicates that Prdm9 binds its target as a consequence of competition between sites. It is not very clear what this means. Prdm9 will bind and occupy high-affinity sites more frequently than low-affinity sites. This is not a competition. There may be a competition but only if Prdm9 protein is limiting.

The authors write L215. "the corresponding PRDM9 binding sites will always be more likely to be bound in individuals homozygous for the cognate PRDM9 allele relative to heterozygotes": not if Prdm9 protein is not limiting.

In fact, by choosing conditions (L354) where 99% of Prdm9 is bound to weak sites in the absence of hotspots, it seems that the authors define conditions where Prdm9 is limiting. What is the rationale for this?

– Competition between Prdm9 bound and DSB activity (see Diagouraga et al., 2018) (if DSB activity is fixed, then the number of Prdm9 bound may exceed the number of potential DSB, ie 300). This could result in competition between Prdm9 alleles in heterozygotes.

2) Figure 1 represents kon and Koff; the text refers to Ki, thus, even if obvious, it should be mentioned that ki=koff/kon.

3) Figure 3B: the area shaded in red should correspond for the context where the homozygous have lower fitness that the maximal fitness of the heterozygous. Thus, what is the red-shaded area for > 4800 hotspots?

4) Figure 5: The label of the y-axis is missing, please clarify. It would help to describe the figure in the text (L480-484) as way more consistent with the figure itself, and to better explain how the data from Figure 4 was used to derive these hotspot distributions.

I assume the initial and final hotspots correspond to exiting and invading alleles? Is this correct?

"…the distribution is centered close to the optimal number of hotspots.", I guess the authors refer to the invading alleles distribution, please clarify in the text.

5) Estimation of the number of Prdm9 bound sites.

The authors use the value that has been published by Baker et al. Genome Res 24, 724-32 (2014). However, the problem is that this number is questionable.

Baker et al. indicated:

"…we estimated that there are;4700 +/- 400 PRDM9-modified sites in the B6 background in an average meiosis." "For estimating the total number of PRDM9-dependent hotspots per meiosis, an equal volume of MNase-digested input DNA was analyzed alongside the ChIP DNA".

This method is not correct: by using this Mnase-digested input DNA, the amount of DNA is likely underestimated, as most input DNA molecules are not bound by Prdm9, do not have positioned nucleosomes at Prdm9 binding sites, and thus not protected from Mnase (depending on the duration of treatment) as positioned nucleosomes are. This unknown underestimation factor means that the number of sites bound by Prdm9 is overestimated.

The way to address this issue is to design models with different values for pT (from 5000 to 500 for instance). Does it affect the simulations? How?

6) Connections with in vivo data should be made:

Several important studies in the analysis of Prdm9 hybrid incompatibility have reported dosage effects (ie Mihola et al. Science 323, 373-5 (2009); Flachs, P. et al. PLoS Genet 8, e1003044 (2012)).

These studies must be cited and discussed. Specifically, it is important to link the model presented to these studies, as they provide a potential assay to validate the model (in particular Flachs, P. et al. PLoS Genet 8, e1003044 (2012) where both the removal of an allele or increased gene dosage can improve the fertility of B6xSTUS hybrid). Although the in vivo parameters are not known in the hybrids that have been analyzed, the authors may be able to approximate some conditions that are simulated, and the model may propose an interpretation for these observations.

Also, the context of C57BL/6 mice seems a good example of a context where Prdm9 binding becomes limiting as seen in the B6 +/- mice (Baker, C.L. et al. Multimer Formation Explains Allelic Suppression of PRDM9 Recombination Hotspots. PLoS Genet 11, e1005512 (2015)). This seems to indicate that B6 sites have been strongly eroded.

In the discussion, the authors refer to the number of DSBs per meiosis (L701). If DSBs are indeed lower in B6 compared to PWD, it would suggest that the impact is global rather than specific to symmetric/asymmetric site balance (unless an additional hypothesis of co-evolution is invoked).

In addition to the reduction of DSB activity (at symmetric sites and maybe also at asymmetric sites), it has been shown in this context and other contexts (hybrids) that default sites are used. Even if not integrated into the model, this aspect should be discussed. At some point, during Prdm9 evolution, default sites are able to take over, thus this is a very important feature that needs to be taken into consideration/discussed, even if it does not directly impact the present study and model.

Reviewer #2 (Recommendations for the authors):

1) The introduction is a bit long but it is maybe necessary as the topic is complex. The authors did a very good job to explain such complexity but maybe so parts could be a bit reduced. For example, between l55-62 could be removed as it is not really discussed later on.

2) As explained above there are several points that should be clarified to help the reader

– In the two first results parts there is no direct result about the evolutionary dynamics per se but some logical predictions based on the fitness landscapes, similar to an invasion analysis (for example, under which conditions a new allele can invade? are there fixed points and which ones?). This step is fully justified but the objective should be explained clearly.

– In figures 2 and 3 it would be good to explain from which equations the figures come. For example, in figure 2 it is not clear whether it corresponds to fitness and probability of binding at an individual or population scale and what is the composition of the population.

– In figure 3 the composition of the population is not clear either: one resident PRDM9 allele? Several? So, "homozygote vs heterozygote genotypes" is not clear (as in Figure 3). We globally understand the rationale but then we need to guess to reconstruct the puzzle from the different pieces of equations.

– l. 310. "These last two assumptions are key, as can be understood by considering how fitness would change over time without them, under the simplest possible scenario, in which all individuals are homozygous for a single PRDM9 allele and all binding sites have the same binding affinity." This statement is rather implicit and the reader may think that the answer is in the sentence (however one must read the next paragraph to fully understand). Maybe rephrase a more explicit explanation.

– In the third part, mutations on PRDM9 are introduced but not before. This should be explained in the model part that the mutation dynamics of PRDM9 are not considered first for the fitness analysis. Otherwise, it leaves the reader with unanswered questions about it until l426. We also only understand when reading this part that the diversity of PRDM9 will be followed. So, this should be explained earlier also.

3) Choice of parameters

– The number of hotspots associated with a new PRDM9 allele is drawn in a uniform distribution between 1 and 5000. This is a bit surprising. Is there any justification for this choice? Instead, we might have expected a unimodal distribution centered for example on the average number of sequences we can find at random in a genome for a motif. A few additional simulations with another distribution could be helpful to check whether the results are not dependent too much on this assumption.

– It is also justified to explore only the case of two heats and the assumptions of many weak sites seem reasonable, but it is not justified. Is the underlying justification that for a given motif of k nucleotides there is 3^k possible one-step mutant motif (so many more) that should only bind weakly (because of one mutant site)? – Among other choices of parameters, the authors decided to consider only two heats (and discussed this choice). However, we can consider that there are only two heats per PRDM9 alleles but that they have different heats, especially the hottest one. If possible, a complementary set of simulations would be to fix n2 and k2 as the authors did but then instead of fixing k1 and considering that each new PRDM9 allele has a different n1, doing the reverse: fixing n1 and drawing k1 in a distribution.

4) Discussion

A possible suggestion would be to summarize observations to explain in a table in parallel with predictions of this model and those of previous red-queen models to clearly show what is better explained, what is not that different, and what could be tested further.
