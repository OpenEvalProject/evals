# Author response - Round 1

Authors:
- Akiko Satake ([ORCID: 0000-0002-0831-8617](https://orcid.org/0000-0002-0831-8617))
- Ryosuke Imai
- Takeshi Fujino
- Sou Tomimoto ([ORCID: 0009-0005-8376-7104](https://orcid.org/0009-0005-8376-7104))
- Kayoko Ohta
- Mohammad Na'iem
- Sapto Indrioko
- Widiyatno Widiyatno
- Susilo Purnomo
- Almudena Molla Morales
- Viktoria Nizhynska
- Naoki Tani
- Yoshihisa Suyama
- Eriko Sasaki ([ORCID: 0000-0002-0878-364X](https://orcid.org/0000-0002-0878-364X))
- Masahiro Kasahara

## Response text

DOI: [10.7554/eLife.88456.3.sa4](https://doi.org/10.7554/eLife.88456.3.sa4)

The following is the authors’ response to the original reviews.

Reviewer #1

1. Here are a few sentences that could potentially benefit from further discussion, particularly in the context of the plant developmental framework of an effective germline. It is important to note that the idea of an effective germline is supported by many, but not all, scientists. Nevertheless, as long as this concept remains relevant, a discussion based on it may be appropriate.

The early establishment of germlines during development is crucial in addressing the impact of somatic mutation on the next generation. To emphasize this aspect, we have included an additional sentence addressing this point in ll. 242–244.

1. Lines 161-163: The suggestion that long-lived tropical trees do not necessarily suppress somatic mutation rates to the same extent as their temperate counterparts might warrant additional examination.

We have revised our statement to present a more balanced perspective, and we have also included a sentence to emphasize the importance of conducting further studies in future.

1. Lines 200-202: The observation of potential influences of GC-biased gene conversion during meiosis or biased purifying selection for C>T inter-individual nucleotide substitutions could be further elaborated upon.

Our data does not provide enough information to delve into a more detailed discussion regarding GC-biased gene conversion during meiosis or biased purifying selection for C>T substitution. However, future studies that obtain genome sequences from somatic cells, male or female gametophytes, and offspring (such as seeds or seedlings) would offer opportunities to assess these phenomena.

1. Line 245: The statement "somatic mutations can be transmitted to seeds" might be correct, but it would be helpful to explore the extent to which this occurs.

In response to the comment from Reviewer 1 (#4) and 2 (#16), we have decided to remove the discussion about the heritability of somatic mutations in next generation. We have completely rewritten the final paragraph to discuss the possibility of a disparity in the relationship between lifespan and somatic mutation rates between plants and animals.

Reviewer #2

1. l. 108- 115: The authors seem to have made a really great work at assembling and annotating two reference genomes. Even if this does not represent the main result of the manuscript, these genomic resources are a plus for the community, especially given that reference genomes from tropical trees are known to be underrepresented in the literature (e.g. Plomion et al. 2016). The authors have made the particular effort of generating two high-quality reference genome assemblies for two species of the same genus, including one with an excellent contiguity. Even if they do not explicitly indicate the divergence time between the two species, it is clear that the cheapest solution would have been to map the reads of the two species against a single assembly, but this could have generated some biases. So by generating two de novo assemblies, the authors have used here the best design possible to control for some potential biases for the detection of somatic mutations. However, given the interests these two assemblies represent by themselves, I consider that a couple of additional investigations could have been made on local synteny and orthologous genes in particular. Thanks to whole-genome alignments and orthology (e.g. Lovell et al. 2022), they could have generated more general information regarding the two assembles and investigated additional questions regarding mutations, e.g. mutations in collinear / non-collinear (if any) segments, intensity of purifying selection (or neutral evolution) at single vs. multiple copies or between shared vs. private genes, etc.

To address the comment by Reviewer 2, we performed synteny analysis using the MCScanX in TBtools-II and added Supplementary Figure 3 to illustrate conserved synteny relationship between S. laevis and S. leprosula. Detecting selection in the genome will be a future study as our current data are not sufficient for the aim because of limited number of individuals (n = 2 for each species).

1. l. 123-124. Here, the authors indicate that they have "validated" 93.9% of the mutations. It would be more accurate to indicate that they have "validated" 31/33 mutations (94%), 22/24 mutations on S1 and 9/9 on S2 (Table S5). Can the authors indicate why no somatic mutations from the F1 and F2 were tested? According to me, the use of the word "validation" is not totally accurate (see also Schmitt et al. 2022), since amplicon sequencing can be viewed as a kind of validation but it doesn't represent a complete validation since it represents new sequencing data that are mapped against the same reference assembly, in such a way that we could always imagine that the same biases are at play, leading to a similarly false positive call. Reciprocally, a "non-validated" mutation could be associated to a mutation that is at a too low allele frequency, at least after amplification, in such a way that the call is not heterozygous despite the fact that the mutation is real. I think that another terminology than "validated" could be used, plus one or two sentences explaining this degree of complexity.

To improve the clarity of the statement, we have modified the sentence as follows: We conducted an independent evaluation of a subset of the inferred single nucleotide variants (SNVs) using amplicon sequencing. Our analysis demonstrated accurate annotation for 31 out of 33 mutations (94% overall), with 22 out of 24 mutations on S1 and all 9 mutations on S2 (Supplementary Table 5).”

While we did not conduct additional assessments using F1 and F2, we anticipate a similar high level of agreement between the somatic SNV calls and amplicon sequencing in these trees. We have included sentences in the Materials and Methods section to elucidate the challenges involved in validating true somatic mutations.

1. l. 135-137 the reasoning appears to be quite circular to me. As indicated by the authors in the line just before, an incongruent pattern could also be explained biologically, in such a way that the overall congruency between the phylogenetic tree and the tree architecture cannot be considered as a way to prove the reliability of the detection. In some species, it seems clear that the phylogenetic tree do not seem to follow the plant architecture (Zahradnikova et al. 2020) in such a way that we should argue to not consider the plant architecture in the design and not consider this represents either a way to validate mutations or a way to validate the methodological framework. I suggest removing this sentence.

We have removed the sentence as suggested by Reviewer 2.

1. l. 150. It seems that the differences in length and diameter between the two species come from two different studies and therefore that no statistical test has been performed to test its significance.

We agree with Reviewer 2. To clarify this point, we have replaced “significantly” with “substantially” in the revised text.

1. l. 156-159: the same sentence is repeated twice.

We have removed the repeated sentence.

1. l. 159-161: Comparing somatic mutation rates between studies is difficult. It is too sensitive to the methodology used, here again see Schmitt et al. 2022. I propose to remove these two sentences. It represents an interesting working hypothesis but would require a better design, or at least, to reanalyze all the data with the same pipeline.

We have toned down our statement, and added a sentence that additional studies are required to compare somatic mutation rates among trees in tropical, temperate, and boreal regions, employing standardized methodologies.

1. l. 171-175: Here I am wondering if the authors could provide more information regarding the enrichment at CpG sites? I suggest first estimating the proportion of CpG sites thanks to the two genome assemblies and then using this information as a way to weight the results and therefore to estimate the level of enrichment of mutations at CpG sites.

In response to the comment by Reviewer 2, we first determined the proportion of CpG sites as 0.030 and 0.028 for S. laevis and S. leprosula, respectively, based on the triplet matrix using the reference genome of each species. Subsequently, we estimated the proportion of somatic mutations at CpG sites. The results revealed a 4.54-fold and 3.53-fold increase in somatic mutations at CpG sites for S1 and S2, and a 3.38-fold and 2.56-fold increase for F1 and F2, respectively. We have incorporated this finding into ll. 172–175.

1. l. 176-187. Interesting comparison and insights. You could also indicate that SBS5 is also detected in all human cancers too. So the detection of SBS1 and SBS5 signatures indeed suggest some shared mutation biases. Note that in humans, a specific signature of UV is associated to TCG -> TTG mutations (Martincorena & Campbell, 2015). It seems that there is a substantial difference in the mutation spectra between the two trees for this specific category, note sure if this difference could be associated to UV.

We slightly modified the sentence to indicate that SBS5 is also detected in all human cancers. We are very interested in the potential impact of UV on somatic mutations in tropical trees, considering the high levels of UVR in the tropics. Conducting a comparative analysis of the mutational spectrum among trees inhabiting diverse UVR environments would provide valuable insights to substantiate this hypothesis.

1. l. 206: I rather suggest "the somatic mutation rate per year is roughly the same, suggesting that somatic mutations rates are independent of growth rate".

In response to the suggestion from Reviewer 2, we have revised the sentence as follows: "The somatic mutation rate per year remains largely consistent, indicating that somatic mutation rates are independent of the growth rate."

1. l. 207-232: Here, It is the section looks a mixture between a result and a discussion. I guess the authors consider here that it remains a verbal model at this stage and it therefore represents more a discussion. If so, I agree but it could be good to discuss more this part, in particular to know how this model could be improved and empirically tested.

The argument based on the model will be more accurate when the cell cycle duration can be directly estimated for each tree. We have added this explanation in the revised text.

1. l. 238-239: The parallel drawn with the molecular clock is interesting but according to me, it remains a working hypothesis at this stage, since it is not validated outside the two focal species. I encourage the readers to continue to work on this question and to investigate also some annual plants for instance in the future (assuming that they have a higher α) in order to be able to derive a global model. In addition, even if I consider that the authors use and interpret this parallel wisely, I consider that the use of this terminology could be misleading for some readers. That's why I also suggest removing "molecular clock" from the title and using a more explicit one, e.g. "Somatic mutation rates scale with time not growth rate in dipterocarp trees".

We agree with Reviewer 2. We have changed the title to “Somatic mutation rates scale with time not growth rate in long-lived tropical trees.”

1. l. 245-249: The results rather suggest that (i) there is little diversity due to somatic mutations and that (ii) most heritable non-synonymous mutations are deleterious and therefore purged from the population. So rather than this last section of this discussion that has little interest and could be quite debatable, I consider that the authors could extend their discussion, e.g. the differences with somatic mutations in mammals (recently, Cagan and coauthors (2022) demonstrated that somatic mutation rates are inversely correlated with lifespan in mammals) or the overall low rate of molecular evolution in trees could be some directions. But there are many others.

We have completely rewritten the final paragraph to propose the possibility of a disparity in the relationship between lifespan and somatic mutation rates between plants and animals, rather than discussing the heritability of somatic mutation in next generation.

1. l. 570-571: I guess, the reader should understand here "fixed at the heterozygous state"

To avoid confusion, we have modified the text as follows: “If the alternative allele was present or absent in all eight branches in the amplicon sequence, the site was determined as fixed within an individual tree.” We have also removed “heterozygote” in Supplementary Figure 5.

1. Fig. 4d. the y-axis would be easier to interpret by writing "Delta Inter-individual vs. Somatic SNPs" and/or by adding arrows on the right margin of the plot to indicate the directions with some short sentences such as "more somatic mutations observed than expected assuming the inter-individual comparison", "less somatic mutation than expected". According to me, some statistical tests are lacking here. Are the differences in the mutation spectra significant given the relatively limited amount of somatic mutations detected?

We have added short sentences explaining the directions.

1. Supplementary Tables (excel file): please correct the typos. There are many on these supplementary tables.

We carefully checked supplementary tables and corrected the typos.

Reviewer #3

1. To estimate false negative rates, the authors might consider using mutation insertion tools such as Bamsurgeon (https://github.com/adamewing/bamsurgeon) to create simulated mutations. Alternatively, one could assess the calling rate of high-confidence SNPs that differ between individuals of the same species to get at the FNR.

We agree with Reviewer 3. To calibrate our pipeline, we previously performed simulation to estimate the false negative and positive rates in different tree species (Betula platyphylla) using wgsim v0.1.11 (https://github.com/lh3/wgsim). Based on our simulations, we found that the false negative and false positive rates were very low, averaging at 0.050 and 0.046, respectively. It is important to note that the estimated false positive rate obtained from the simulation data was substantially lower than the proportion of potential false positive SNVs (as shown in Supplementary Fig. 5). This observation suggests that simulation-based evaluation of the false positive rate is not reliable, at least for the tree species we studied. Similarly, the same argument could be applied to the false negative rate. Therefore, we conclude that the simulation-based analysis for estimating false positive and false negative rates is not informative for our study.

The rate of true-positive or false-negative mutation calls can be estimated only when the true mutational status is known, but the data are not currently available. However, under the assumption that the final set of SNVs represents true somatic mutations, we were able to calculate the potential false negative rate. Our findings indicate that this rate is low, specifically less than 10%, when using less stringent filtering thresholds such as BQ20 and MQ20. While these estimated values may not precisely represent the true false negative rate, we included them as potential false negative rates in Supplementary Figure 7 of the revised manuscript. This information provides additional insights into the performance of our pipeline under different filtering thresholds and contributes to the overall assessment of our study.

1. It may be interesting to examine the mutation trees for constancy (or not) in mutation rate per meter. Examining Figure 1, it appears that the number of mutations near the crown "4" node is consistently higher than in nearby nodes (3-1 and 3-2).

We calculated the branch-level increment of SNVs per meter by dividing the number of single nucleotide variations (SNVs) by the physical distance. Our analysis revealed a slight increase in the number of SNVs per meter as the branch position became higher in S. laevis, as shown in Author response table 1. However, this trend was not clearly observed in S. leprosula. We found this observation in S. laevis intriguing, particularly because our recent analysis (Tomimoto et al., in preparation) demonstrated that genetic distance increases in branch pairs located in the upper part of a tree. This was elucidated through a mathematical model that describes the dynamics of the stem cell population during elongation and branching. We opted not to delve further into the findings in the current manuscript, as this topic will be extensively investigated in a future study.

1. Line 150: Use of "significantly different" is confusing as the phrase is usually reserved for statistical significance. Consider replacing with "substantially different."

We have replaced “significantly” with “substantially” in the revised text.

1. In the Discussion, a clearer explanation of the assumptions that underlie the authors' reasoning would be welcome: e.g., constancy in mutation rate per meter within an individual tree. In particular, the authors assume that mutations that are seen in one leaf and not in another cannot have predated the most recent common meristematic node linking the two leaves. Is this a reasonable assumption? Since the meristem is multicellular, is it possible for a mutation to have arisen earlier in development and "assorted" into one cell lineage but not another?

We greatly appreciate an important comment. It is true that when the meristem is multicellular, and the stem cell lines are retained during mutation accumulation (e.g. a structured meristem analyzed in Tomimoto and Satake 2023), it is possible for a mutation to have arisen earlier before the bifurcation. Using a mathematical model, we have proved that the intercept and slope of the linear regression between the pairwise genetic distance and physical distance are influenced by the type of a meristem (strength of somatic genetic drift in a meristem) as well as the branching architecture of the tree. We have included an explanation of this point in the revised manuscript (ll. 244–249).

1. Supplementary Data 7: Column J should be "2_2"

We corrected the typo.
