# Peer review - Round 1

Editors:
- Dieter Ebert, University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58931.sa1](https://doi.org/10.7554/eLife.58931.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study reports on a phenotypic and genetic polymorphism of DiNVirus in natural populations of Drosophila. The authors present a series of experiments and assessments to understand how the polymorphism evolved and what implication it has for the host and conclude that the observed polymorphism arose multiple times independently and that it is maintained in a polymorphic state. The results are very clear and convincing and provide an excellent example for the power of natural selection in shaping host-parasite interactions.

Decision letter after peer review:

Thank you for submitting your article "Recurrent evolution of two competing haplotypes in an insect DNA virus" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Diethard Tautz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Sebastian Gagneux (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Your manuscript presents an exciting finding of the evolution and biology of a natural viral pathogen of Drosophila. You suggest that two distinct haplotypes of the virus evolved multiple times in isolated host populations. These two haplotypes are characterised by 11 SNPs and associated phenotypic traits (differences in viral titer). The independent evolution of such a complex trait seems rather unusual, making this nice example of evolution of host-parasite interactions.

The three reviewers of this manuscripts have a lot of praise for the study. However, they also raise a number of important points that needs to be addressed. Most important, the substantive technical points raised by reviewer 2 need careful consideration. This includes explaining and resolving the inconsistencies in the analysis and the right choice of the methods. Reviewer 1 pointed out problems with the simulation. Below are the detailed reviews. A final decision will only be possible when the problems in the analysis are solved.

Reviewer #1:

This study reports on a phenotypic and genetic polymorphism of DiNVirus in Drosophila. The study is very appealing as this study system is a natural system (unlike D. melanogaster) with a well understood ecology and biogeography. The authors go through a series of experiments and assessments to understand how the polymorphism evolved and what implication it has for the host. The main conclusion is that the observed polymorphism arose multiple times independently and that it is maintained in a polymorphic state. The mechanism for this maintenance is not entirely clear. A simulation model is used to bring some light into this puzzle. For the most part, the study is solid and well carried out. Below are a number of points that may help the authors to present their material more clearly.

The Introduction is not to the point. The Introduction moves among various aspects of host-parasite interactions without giving the reader an idea where this is going. At various places topics are raised that then later dismissed. For example: the first two paragraphs are about host response to viruses. In the third paragraph it become system specific, but now switches mainly to the DiNV system. It is not clear where one is going here. The Introduction (sixth paragraph) is summed up with a very generic phrase without much perspective on what is going to follow. At this place I still do not know what this paper will be about. A much more targeted Introduction is necessary. What are the questions? What was driving this research? What are the hypotheses?

With 11 SNPs spread across the chromosome and obligate recombination every round of replication, the proportion of viral offspring with sub-optimal multi-SNP-genotypes must be huge. How can the right genotypes be maintained? Discuss.

The authors run computer simulations (called SIR models, but they seem actually to be SI models) to support their ideas about virus evolution. The simulation regarding the accumulation of mutation is fine and gives quantitative support for presented evolutionary scenario.

A second simulation is about the competition of the two viral types. This is by far the weakest part of the manuscript. I am not convinced about the value of this simulation. The outcome can be predicted from the assumptions of the model, several of them are very speculative. Without data on transmission over the course of the infection, the simulations are not very helpful. I suggest to leave this out. It is ok to speculate about this in the Discussion, but it makes the Results part heavy and less strong. Also, the associated figure (Figure 7) is hard to understand.

The authors stress at multiple place that it is likely that the increased virulence of the high type is traded-off against transmission. The evidence for this is much weaker than the strength of these statements suggests. I strongly suggest to tone this down.

Reviewer #2:

This manuscript presents an exciting analysis of the evolution and biology of a natural viral pathogen of Drosophila. In outline: the authors claim that two distinct haplotypes of the virus co-occur in multiple host populations, that these 'evolved' independently (i.e. separate origins) through convergence, and that they have alternative 'life histories' (high titer and virulence, versus low titer and virulence), which may permit their coexistence.

The practical experiments and sequencing data are substantial and appear sound, and the work is likely to be of interest to a very broad host-pathogen audience. However, while some of these headline claims are well-supported, I have a number of serious concerns about the analyses and interpretation of others, and a few key methodological details are missing. The analyses would need substantial revision, or at least additional checks, before I would be convinced by the story.

1) Is there any possibility of circularity in defining the 'high' and 'low' haplotypes?

Two 'types' are defined based on 11 linked SNPs that are described as having 'high' or 'low' titer phenotypes. First, this requires a more robust approach to define 'significance' as (if there is any LD) tests are not independent, and sample sizes relative to predictive SNPs are small. Phenotypes (titers) should be permuted across genotypes (within populations) a thousand times and the analyses re-run for each permutation, then the tails of this distribution used to define significance, as commonly done for e.g. the DGRP. Second, this feels like it is dangerously circular: supposing all 11 SNPs were false positives, and arbitrary haplotypes erroneously defined based on them? Post hoc analysis of the difference between the two haplotypes could still show Figure 1B, because those differences were what drove the (erroneous) detection of the SNPs. So would Figure 1C, since that result necessarily follows from the definition of the haplotypes.

To convince me that the 'two haplotypes' interpretation is real, for each of the randomisation replicates one would need to define a 'high' and a 'low' haplotype based on the any randomisation spurious 'significant' SNPs and re-run the rest of Figure 1 to demonstrate that the separation between the real haplotypes is greater than that between those that result from permutation tests. I appreciate that this will require some computing time, but the authors already have all of the code, so it shouldn't be more than an afternoon of 'hands on' time.

Since the haplotypes overlap in phenotype space (Figure 1B) and not all have all SNPs (Figure 1C), how were intermediate haplotypes (with <11 SNPs) assigned to high or low?

2) Did the haplotypes evolve independently three or four times?

Of the 11 SNPs defining the haplotype, three are non-synonymous, five are in the UTRs of known virulence genes, and three are intergenic SNPs. Is it really credible that a specific base change has arisen and been selected for independently in each of four populations, at each of the 11 sites? i.e. always A->C being beneficial at a site, but never A->G at that site? Even for the non-coding ones? This is an extraordinary claim that would require extraordinary evidence, for which the rates of recombination and gene conversion seem at the heart of the argument.

In some places the authors appear to assume (or assert) that recombination is frequent, while in others they assume it is completely absent, and nowhere do they explicitly test for it. If it is common, then none of the tree-based analyses can be used. If it is absent, then it is very hard to explain the patterns of diversity or LD in Figure 1—figure supplement 3, and some of the simulations may be inappropriate.

The tree-based analyses seem to be the basis of the major claim that these haplotypes arose independently multiple times, and that the order of the mutations arising was similar. Any tree analysis absolutely requires the absence of recombination or gene conversion, and this needs to be explicitly tested for here (e.g. using GARD, or possibly if diversity is low by inferring the ARG using tsinfer). The failure of LD to decay with distance hints that recombination is absent, but gene conversion over very short distances could still shuffle mutations between haplotypes. However, assuming its branch lengths are in mutations, the shape of the tree in Figure 6A (many short tips below large crowns) shouts 'recombination' to me. Where did this tree come from? It is not ultrametric, so if it was inferred with BEAST this is not standard output.

If the authors do have evidence that recombination is absent, can they confirm that the other analyses (population size history from the SFS; simulations) also assumed zero recombination? Although zero recombination would make me worry even more about the p-values in the GWAS discovery of the SNPs that define the haplotypes – but permutation tests would help deal with that.

I am really confused about their view of recombination, because a couple of times they imply recombination may be common, for example by noting that recombination is required in Nudivirus replication – but then this would invalidate the tree-based analyses? Plus, mechanistic recombination is irrelevant without coinfection infection, since recombination only between identical haplotypes does not have any effect. The observation that no co-infections occur suggests recombination should be very rare – but that's not what the tree looks like. The sixth paragraph of the Discussion suggests that not enough thought has been given to the likelihood, or implications, of recombination.

Finally, if there is no recombination, then 'fully derived' haplotypes (those with all 11 SNPs) can only be as old as the youngest of the 11 SNPs, unless the SNPs arose multiple time within populations as well. Is that compatible with the patterns of diversity and the timescale? One check would be to mask those 11, re-infer the tree, and check that the clades are still monophyletic. If these arose by re-current mutations due to strong selection, they could be warping the tree – this might be akin to the problem of recurrent drug or MHC selected mutations in HIV trees, where the known sites are excluded before analysis.

If we believe the two haplotypes are real, a much more credible 'story' to me would be two distinct and potentially old haplotypes maintained by selection in the face of a low level of ongoing gene conversion (or recombination). Is there some aspect of the data that this does not fit? This seems just as good a 'story', just as interesting, and just as publishable.

3) The MK-like analyses

Although a relatively minor part of the story, the MK analysis is extremely unclear. In part this is because it doesn't appear in the Materials and methods.

i) What software was used? The supporting data implies VCFtools can do this (which surprised me) but the method it uses was not explained. Was SNIpre fitted with the original code? The text seem to imply that raw counts were used, which would not be suitable unless Ks was <0.3

ii) Although divergence is required, we're not told how (or from what species) it was estimated. If Ks>0.3, then something more than raw counts should certainly be used. If Ks>0.8, I would strongly advise against doing any sort of MK analysis.

iii) Figure 4 gives 'difference from background'. What is meant by difference from background? But if the background is a signal of strong constraint, could a positive signal here mean relaxed constraint rather than positive selection. What is the evidence that it's positive selection rather than relaxed constraint?

iv) In Figure 4—figure supplement 1 the populations are presented separately, and differences among them are interpreted as differences in positive selection. But surely the divergence number must be massive, larger than the polymorphism number, so almost all of this variation is due to differences in constraint affecting the Pn/Ps ratio. Or is the method one that uses high frequency derived SNPs as evidence of positive selection? If so, how was ancestral state identified? This is probably not possible to do reliably if Ks>0.3. We need to see some raw numbers, and a lot more detail on the methods.

Reviewer #3:

This is an interesting piece of work on the co-evolution of the Drosophilainnubila Nudivirus (DiNV) and its host. The authors analyzed several natural populations of D. innubila, some of which were partially infected with DiNV, and simultaneously characterized both the host and the infecting viral pathogen using a combination of DNA and RNA sequencing and various complementary analytical approaches. Using a GWAS approach, they discovered a viral variant with high virulence (High Type) that differed by 11 strongly linked SNPs from low virulence variants. They demonstrate that the High Type associates with a higher viral titer and increased host mortality, and also validate these findings using experimental infection assays. Using a transcriptomic approach, they show that the High Type overexpresses genes known to be linked to viral virulence, and this correlated with the under expression of host genes involved in antiviral immunity, indicating that the increased virulence of the High Type is at least partially due to the inhibition of host defense mechanisms. They further show that loci associated with differences in virulence were under strong selection for adaptation, particularly genes involved in the viral envelope and virulence proteins. Based on their reconstruction of the most likely evolutionary histories of the High Type in the different host populations, they further conclude that the High Type emerged multiple times independently, and yet, the High Type did not outcompete the Low virulence variants in these populations. This might indicate varying trade-offs between virulence and transmission in the High and Low Types that vary across these populations. Finally, they show that the same phenomenon for High Type evolution of DiNV can also be observed in other Drosophila species. I have just a few comments:

1) Throughout the manuscript, the authors switch back and forth between the present and past tense, which seems awkward from a stylistic point of, I'd suggest to stick to the past tense through-out.

2) The fact that the exact same 11 SNPs evolve multiple times independently in mostly the same order is interesting. The authors note that an expected alternative could be different SNPs emerging in the same genes, but they don't discuss the potential mechanism, by which the exact same SNPs seem to be preferred instead.

3) The authors found little evidence of mixed infection with both the High and Low Types and conclude potential in-compatibility. Please expand on the potential mechanisms of this.

4) Related to the above comment, the authors observe no "hybrids" of High and Low Types again, suggesting "incompatibility". Please discuss the difference between this genetic/genomic versus ecological incompatibility referred to above, as well as the potential link between these two types of incompatibilities.

5) Please rephrase the first sentence of the Discussion (what is the deference between "to better infect" and "optimizing the infection"?).
