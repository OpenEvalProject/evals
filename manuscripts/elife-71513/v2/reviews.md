# Peer review - Round 1

Editors:
- Jeffrey Ross-Ibarra, University of California, Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71513.sa1](https://doi.org/10.7554/eLife.71513.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Mutation saturation for fitness effects at human CpG sites" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. All three reviewers were very enthusiastic about the manuscript, and with some revision it will clearly be suitable for publication in eLife.

The main revision reviewers agreed would be important to incorporate is the issue of multiple testing (highlighted by Reviewer #2).

While all the reviewers were enthusiastic about the manuscript as written, and none felt that additional analyses were necessary, there were a number of additional analyses suggested that reviewers felt could strengthen the paper if they were relatively straightforward to incorporate. These included:

1) Comparison of the nonsynonymous genome-wide DFE from smaller samples to the 780K, perhaps only focusing on methylated nonsynomous sites.

2) Comparison of overlap between these invariant sites and Clinvar or databases of patients with known developmental disorders.

3) Comparison of results under a different parameterization of human demography.

Reviewers had a number of additional suggestions that we felt would improve the manuscript. Perhaps first among these was a general feeling of "to be continued" in the discussion with multiple citations to another manuscript in prep. While reviewers were not against this strategy by any means, efforts to address the novelty of the current paper in the discussion (rather than simply hinting at exciting results in the forthcoming work) would be worthwhile.

Please do review and respond to the individual reviewer comments as well.

Reviewer #1:

Agarwal and Przeworski have performed a very timely and interesting study of the distribution of fitness effects (DFE) of new mutations. This study is timely because modern human population genetic datasets have finally achieved sample sizes for which a certain class of nucleotide sites, i.e. methylated CpG sites, when neutrally evolving, should approach near complete polymorphism saturation. If every neutral site is expected to carry at least one variant, the classic problem of distinguishing sites that are monomorphic due to chance (no mutation) versus sites that are monomorphic due to selective constraint (removed mutations) is greatly simplified. The point at which population genomic datasets are saturated with polymorphisms should represent a major advance in understanding the DFE at individual sites and is what immediately piqued my interest.

Overall, this manuscript is a thorough and thoughtful examination of this topic; to my enjoyment there were several times where a question came to mind that was addressed shortly later in the paper. I believe the authors have made a compelling case for why methylated CpG sites provide an entry point for understanding the site-specific DFE. I found the section "Interpreting monomorphic and polymorphic sites in current reference databases" particularly insightful as a guide to thinking about future datasets; similarly, I thought the comparison with CADD scores (Figure S9) provided important food for thought regarding confounders to maps of constraint generated from vast numbers of species using modern genomic datasets.

While the study is addressing an interesting topic, I also felt this manuscript was limited in novel findings to take away. Certainly the study clearly shows that substitution saturation is achieved at synonymous CpG sites. However, subsequent main analyses do not really show anything new: the depletion of segregating sites in functional versus neutral categories (Figure 2) has been extensively shown in the literature and polymorphism saturation is not a necessary condition for observing this pattern. Similarly, the diminishing returns on sampling new variable sites has been shown in previous studies, for example the first "large" human datasets ca. 2012 (e.g. Figure 2 in Nelson et al., 2012, Science) have similar depictions as Figure 3B although with smaller sample sizes and different approaches (projection vs simulation in this study). There are some simulations presented in Figure 4, but this is more of a hypothetical representation of the site-specific DFE under simulation conditions roughly approximating human demography than formal inference on single sites. Again, these all describe the state of the field quite well, but I was disappointed by the lack of a novel finding derived from exploiting the mutation saturation properties at methylated CpG sites.

Similarly, I felt the authors posed a very important point about limitations of DFE inference methods in the Introduction but ended up not really providing any new insights into this problem. The authors argue (rightly so) that currently available DFE estimates are limited by both the sparsity of polymorphisms and limited flexibility in parametric forms of the DFE. However, the nonsynonymous human DFE estimates in the literature appear to be surprisingly robust to sample size: older estimates (Eyre-Walker et al., 2006 Genetics, Boyko et al., 2008 PLOS Genetics) seem to at least be somewhat consistent with newer estimates (assuming the same mutation rate) from samples that are orders of magnitude larger (Kim et al., 2017 Genetics). Whether a DFE inferred under polymorphism saturation conditions with different methods is different, and how it is different, is an issue of broad and immediate relevance to all those conducting population genomic simulations involving purifying selection. The analyses presented as Figure 4A and 4B kind of show this, but they are more a demonstration of what information one might have at 1M+ sample sizes rather than an analysis of whether genome-wide nonsynonymous DFE estimates are accurate. In other words, this manuscript makes it clear that a problem exists, that it is a fundamental and important problem in population genetics, and that with modern datasets we are now poised to start addressing this problem with some types of sites, but all of this is already very well-appreciated except for perhaps the last point.

At least a crude analysis to directly compare the nonsynonymous genome-wide DFE from smaller samples to the 780K sample would be helpful, but it should be noted that these kinds of analyses could be well beyond the scope of the current manuscript. For example, if methylated nonsynonymous CpG sites are under a different level of constraint than other nonsynonymous sites (Figure S14) then comparing results to a genome-wide nonsynonymous DFE might not make sense and any new analysis would have to try and infer a DFE independently from synonymous/nonsynonymous methylated CpG sites.

Abstract: where it says "Here, we focus on putatively-neutral, synonymous CpG sites…" I thought the phrase "putatively-neutral, synonymous" could be clearer to the reader if moved to "… not seeing a polymorphism [at putatively-neutral, synonymous sites] is indicative of strong…".

Page 3 – "DNM" and "FET" were not defined before the first usage of the acronyms.

Page 7 – "That synonymous sites are close to saturation…": Here, wouldn't the expected length of the genealogy such that 1 mutation is expected per synonymous CpG site be a pretty drastic underestimate of the length of the genealogy such that saturation is observed (99% of synonymous CpG sites w/mutation)? Wouldn't a more precise estimate be something like 39 million generations, [1-Pois(0|1.17e-7*39e6)] ~ 99% of sites?

Reviewer #2:

This manuscript presents a simple and elegant argument that neutrally evolving CpG sites are now mutationally saturated, with each having a 99% probability of containing variation in modern datasets containing hundreds of thousands of exomes. The authors make a compelling argument that for CpG sites where mutations would create genic stop codons or impair DNA binding, about 20% of such mutations are strongly deleterious (likely impairing fitness by 5% or more). Although it is not especially novel to make such statements about the selective constraint acting on large classes of sites, the more novel aspect of this work is the strong site-by-site prediction it makes that most individual sites without variation in UK Biobank are likely to be under strong selection.

The authors rightly point out that since 99% of neutrally evolving CpG sites contain variation in the data they are looking at, a CpG site without variation is likely evolving under constraint with a p value significance of 0.01. However, a weakness of their argument is that they do not discuss the associated multiple testing problem-in other words, how likely is it that a given non synonymous CpG site is devoid of variation but actually not under strong selection? Since one of the most novel and useful deliverables of this paper is single-base-pair-resolution predictions about which sites are under selection, such a multiple testing correction would provide important "error bars" for evaluating how likely it is that an individual CpG site is actually constrained, not just the proportion of constrained sites within a particular functional category.

The paper provides a comparison of their functional predictions to CADD scores, an older machine-learning-based attempt at identifying site by site constraint at single base pair resolution. While this section is useful and informative, I would have liked to see a discussion of the degree to which the comparison might be circular due to CADD's reliance on information about which sites are and are not variable. I had trouble assessing this for myself given that CADD appears to have used genetic variation data available a few years ago, but obviously did not use the biobank scale datasets that were not available when that work was published.

Reading this paper left me excited about the possibility of examining individual invariant CpG sites and deducing how many of them are already associated with known disease phenotypes. I believe the paper does not mention how many of these invariant sites appear in Clinvar or in databases of patients with known developmental disorders, and I wondered how close to saturation disease gene databases might be given that individuals with developmental disorders are much more likely to have their exomes sequenced compared to healthy individuals. One could imagine some such analyses being relatively low hanging fruit that could strengthen the current paper, but the authors also make several reference to a companion paper in preparation that deals more directly with the problem of assessing clinical variant significance. This is a reasonable strategy, but it does give the Discussion section of the paper somewhat of a "to be continued" feel.

I think the paper could be strengthened by calculating the proportion of non-variable CpG sites in teach category are likely to be truly under constraint, making use of some kind of multiple testing correction. This would build upon the intuition that a non-variable CpG is likely functional with a non-corrected p value of 0.01.

My point about the possible circularity of comparison to CADD could be addressed with further discussion of the degree to which CADD is informed by patterns of human genetic variation and how incorporation of genetic variation into CADD scores might affect the conclusions of this section. As an additional point in the CADD section, it's not totally clear whether the statement "Mean transition rates at methylated CpGs are similar across CADD deciles" is based on de novo mutation data or some other data source.

Another addition that would add a lot to the paper, though is not strictly necessary, would be to comment on the overlap between sites identified as under selection by the current paper and sites where mutations are already annotated as clinically relevant or suspected to be so based on their occurrence in a disease cohort.

Reviewer #3:

Agarwal et al., combine a few well-known ideas in population genetics – diminishing returns in sampling new alleles with increasing sample size and the enrichment of invariant sites for sites under strong purifying selection – and point out the exciting result that sample sizes of modern human data sets are sufficiently large that, for highly mutable sites, saturation mutation has been reached. This is my favorite kind of result – one that is strikingly obvious in retrospect but that I had never considered (and probably wouldn't have). The manuscript is well written, and a number of my concerns or questions while reading were resolved directly by the authors later on. I have no major concerns, but a few potential suggestions that might strengthen the presentation.

The authors emphasize several times how important an accurate demographic model is. While we may be close to a solid demographic model for humans, this is certainly not the case for many other organisms. Yet we are not far off from sufficient sample sizes in a number of species to begin to reach saturation. I found myself wondering how different the results/inference would be under a different model of human demographic history. Though likely the results would be supplemental, it would be nice in the main text to be able to say something about whether results are qualitatively different under a somewhat different published model.

On a similar note, while a fixed hs simplifies much of the analysis, I wondered how results would differ for (1) completely recessive mutations and (2) under a distribution of dominance coefficients, especially one in which the most deleterious alleles were more recessive. Again, though I think it would strengthen the manuscript by no means do I feel this is a necessary addition, though some discussion of variation in dominance would be an easy and helpful add.

There's some discussion of population structure, but I also found myself wondering about GxE. That is, another reason a variant might be segregating is that it's conditionally neutral in some populations and only deleterious in a subset. I think no analysis to be done here, but perhaps some discussion?

Maybe I missed it, but I don't think the acronym DNM is explained anywhere. While it was fairly self-explanatory, I did have a moment of wondering whether it was methylation or mutation and can't hurt to be explicit.
