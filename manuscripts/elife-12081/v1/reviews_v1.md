# Peer review - Round 1

Reviewers:
- Magnus Nordborg, Vienna Biocenter , Austria

## Review text

DOI: [10.7554/eLife.12081.036](https://doi.org/10.7554/eLife.12081.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "The genetic basis for ecological adaptation revealed by genome sequencing of the Atlantic herring" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Nick Barton and Magnus Nordborg, who is a member of our Board of Reviewing Editors. The evaluation was overseen by Diethard Tautz as the Senior Editor. Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that this manuscript cannot be considered further for publication in eLife. However, we would consider a completely reworked resubmission which addresses the concerns of the reviewers, and in particular goes much further in distinguishing between causal from non-causal alleles.

The consensus opinion of the reviewers is that this is a really interesting study in an excellent study system, but that the analysis is insufficient and several of the conclusions not supported. In particular, the reviewers were not convinced that you can actually identify the causal sites, and several conclusions rest on this. However, exploring the limits of what may be concluded is also of great interest, especially given the quality of the data.

In essence, the analysis does not do the data justice.

Reviewer #1:

This is a substantial piece of work addressing an important question using a beautiful and promising system. It is certainly the case that identifying loci that show evidence having been under selection is much easier in gigantic population with little population structure, as appears to be the case for herring.

Unfortunately, the paper suffers from several conceptual/logical flaws and I do not think the major conclusions are supported.

The confusion begins in the first sentence of the abstract, where it is stated that "Ecological adaptation is of major relevance…, but the underlying genetic factors are typically hard to study in natural populations due to confounding between population structure and signatures of selection".

It is indeed true that population structure makes it hard to identify signatures of selection, but who says that genes involved in ecological adaptation will exhibit such signatures? Generally, such signals arise as a consequence of strong selection on individual genes. For a quantitative trait, is not clear that there will be any such genes, and is also not clear that any such genes found will explain much of the variation. Furthermore, there is no phenotype in the present study, nor any heritability. Thus the comparison with human height (Discussion section) does not make sense. You have no idea how much of the variation for fitness your SNPs explain. Indeed it is formally possibly that all your SNPs are associated with defense against a parasite with a life-cycle that depends on salinity. I obviously don't believe this, but the point remains that in order to discuss the genetic architecture of adaptation, there needs to be genetics in the study. For example, a reciprocal transplant study that quantified the fitness effects of the identified loci.

Speaking of associations, I don't understand how the threshold for calling frequency differences significant was set (Figure 1—figure supplement 1). This is not explained ("used a QQ-plot" is not an explanation).

It is also stated that the presence of haplotype blocks was striking. Why? Presumably these are simply the consequence of selection? Are they longer than you would expect? Why? What is the evidence that they contain multiple causal sites as opposed to being the result of linkage drag?

Regardless of why they are there, the existence of these blocks mandate extreme caution when trying to decide which sites are causal. It is by now clear that local haplotype structure, especially when coupled with allelic heterogeneity causes large number of local spurious associations, and that, as a consequence, the most strongly associated SNP is NOT likely to be the causal one: it is likely to be an intermediate-frequency SNP that happens to tag the underlying variants well…

A consequence of this is that most of the conclusions about what kinds of SNPs do what (Subsection “Genomic distribution of causal variants”) are not supported. You find few significantly associated non-synonymous substitutions, but this could simply be because they are all rare, and can only be found by proxy.

It does make sense to compare different kinds of regions, as you do, but everything has to be controlled for allele frequency.

On a more population genetics level, I was struck by your low nucleotide diversity coupled with a rapid decay of linkage disequilibrium. Unless mutation- and recombination rates are very different from other organisms, they make no sense. My guess is that your nucleotide diversity is underestimated because you are detecting heterozygotes in single individuals, and that your rate of linkage disequilibrium decay is overestimated because of bad SNPs.

Third paragraph subsection “Genetic basis underlying timing of reproduction”: This something not right about this argument. Why would rare SNPs affect nucleotide diversity one way or another?

Subsection “Genomic distribution of causal variants”: "Some of these will be false positives due to close linkage to true positives but many will be true positives" I discuss this above, but it would be important to realise that, without assumptions about the meaning of "some" and "many", it is not possible to conclude any of what you conclude further down.

Same section: "Enrichment" compared to what?

Reviewer #2:

This paper uses whole-genome sequencing from 20 population pools, supported by SNP genotyping of ~360 individuals, to identify variants associated with differences between Baltic and Atlantic, and between autumn and spring spawning herring. This is an impressive set of data, and as the authors argue, the recent divergence, large population size and low differentiation makes herring exceptionally well suited to identifying genes responsible for adaptation. Thus, the study could in principle be a very nice contribution to eLife. However, the interpretation of the results seems quite naive: more detailed and rigorous argument is needed to be convincing.

SNP and structural variants associated with divergence are clustered into haplotype blocks that may span multiple genes, and up to 200kb. It seems to be assumed that all (or at least, many) of the variants within each block are causal, on the grounds that within the Atlantic population, LD decays very rapidly, over a hundred bp or so. This would be very interesting, implying that complex adaptive alleles build up as a result of successive substitutions in the same region. However, careful arguments are needed to exclude the more obvious alternative, that selection has raised specific haplotypes to high frequency. Suppose that the original population was indeed at linkage equilibrium. Under selection in a new environment, many alleles might increase at the same locus – either from standing variation or from new mutations. Such "soft sweeps" might not be detected in these data. However, at a subset of loci, one or a few haplotypes might increase, and their size would reflect the time since adaptation – presumably a few thousand generations, corresponding to perhaps 10-100kb. Even if two or three successive causal alleles were involved, the great majority of SNPs would still be neutral. Seeing LE within the base population does not address this issue; and the ascertainment bias means that only more or less hard sweeps can be detected.

Paragraph six subsection “Genetic adaptation to a new niche environment”: There needs to be a proper test of whether it is surprising that significant variants cover genes in certain functional classes – I have no idea how many genes may be involved in osmoregulation, for example. This is especially an issue because haplotype blocks may cover multiple genes. A proper permutation test is needed here.

Subsection “Genomic distribution of causal variants”: The section on genomic distribution of causal variants was confused. It should be possible to make a rigorous statistical estimate of the fraction of markers that are likely to be causal from the extent of enrichment, but this needs to be done carefully.

Reviewer #3:

This is a comprehensive and nice study and well-written paper, with possible implications for inference on ecological adaptation of species other than the Atlantic herring.

My major comment is that I was surprised by how the paper was written with respect to the literature. After reading Lamichhaney et al. 2012 from the same group it is clear that the current study is a kind of (nice) follow-up from that. Yet the authors only refer to Lamichhaney et al. 2012 once in the Introduction and once in the Results and not at all in the Discussion. In my opinion, the authors should be upfront of what they found in L2012, how this study goes well beyond that, and how the current results confirms or contradicts previously reported results.

My quick reading of Lamichhaney et al. 2012 is that the authors reported: (i) low level population differentiation, (ii) evidence for local adaptation (salinity), (iii) evidence for selection on haplotype blocks, (iv) candidate genes under natural selection (salinity) and (v) evidence of natural selection of reproduction (spawning season).

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your work entitled "The genetic basis for ecological adaptation of the Atlantic herring revealed by genome sequencing" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Nick Barton and Magnus Nordborg, who is a member of our Board of Reviewing Editors, and the evaluation has been overseen Diethard Tautz as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

As emphasized in the decision letter encouraging you to resubmit this manuscript, the reviewers unanimously agree that this is one of the best data sets in existence for addressing questions about the architecture of local adaptation. The resubmitted version is greatly improved, but is still somewhat frustrating in that it was felt that much more could be done with the data. However, it was recognized that this would take the analysis well beyond the current state of the art, and that it would not be constructive to demand this. We actually do not yet have the intellectual framework for thinking about these kinds of data. It says on page 5 that "the results provide a comprehensive and detailed view on the genetic architecture underlying ecological adaptation". So what is the answer? How far can we go without reciprocal transplant studies?

Better then to publish, and be clear about what has and has not been demonstrated.

Essential revisions:

The distinction between causal and non-causal SNPs needs to be more clearly spelled out. The paper identifies a very large number of SNPs that differ significantly between groups. These tend to be clustered on the genome, and also enriched for certain functional types. Some clusters may arise by chance, whilst others may include one or more causal alleles, which tend to be in candidate loci. The enrichment analysis shows the clearest evidence for selection, but it seems to us that this could be consistent with multiple causal alleles at ~ 20 loci, rather than the "thousands" of SNPs cited in the abstract. It should be possible to estimate the minimum number of causal loci consistent with the observed clustering and enrichment, at least roughly.

The existence of long haplotypes distinguishing the different population is emphasized, but it is not clear whether these are in any sense unusual given the low effective population (surprisingly low given the vast census sizes in this species). It should be possible to use standard coalescent simulation to at least test whether the observed haplotype lengths are long compared to neutral expectations under the estimated demography and a range of plausible values for the recombination rate.
