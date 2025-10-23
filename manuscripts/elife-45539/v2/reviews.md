# Peer review - Round 1

Editors:
- Antonis Rokas, Vanderbilt University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.45539.sa1](https://doi.org/10.7554/eLife.45539.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

oskar is a master regulatory gene involved in insect early development that is only found in holometabolan insects. The gene's functions are well studied but its origins remain unknown. This study provides convincing phylogenetic evidence that the OSK domain of the protein encoded by the oskar gene appears to have been originally acquired from a bacterium. The study sheds significant light on the origin of a gene that is uniquely present in holometabolan insects and that plays a major role in insect early development.

Decision letter after peer review:

Thank you for submitting your article "Bacterial contribution to genesis of the novel germ line determinant oskar" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Eve Gazave (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this short report submitted to ELife, Blondel and collaborators aim at understanding the evolutionary history of a crucial gene for reproduction in some insects, oskar. This gene, not found outside this group of organisms, plays a sufficient and mandatory role for germ line determination. So far, the evolutionary history of this enigmatic gene was unknown. In this study, the authors conduct a suite of molecular evolutionary and bioinformatic analyses to unravel the origin of this important gene. They notably performed parametric and phylogenetic methods to detect potential HGT that has been suggested to be at the origin of Oskar. Based on these analyses and findings, they argue:

i) That one of the two domains of the Oskar protein, OSK, is more related to bacterial sequences while the other one, LOTUS, is clustering with eukaryotic sequences.

ii) That LOTUS is related to eukaryotes and that OSK clusters within bacterial sequences, more specifically with GDSL-like hydrolases, thanks to phylogenetic analyses of the two domains separately, as well as topology-constraint tests.

iii) That sequence characteristics, notably the GC3 content and the codon use, through the cosine distance analysis, are very different from the LOTUS and OSK domains which is consistent with the hypothesis of distinct origins for the two domains composing the Oskar gene.

Essential revisions:

The essential revisions fall into two major categories: concerns about the phylogenetic analyses and concerns about the codon usage analyses. The concerns about the codon usage analyses are quite substantial. Here, the authors have two options – one would be to remove completely this part from the manuscript (given that the HGT inference can stand on its own). The other would be to address the reviewers' concerns, which may reveal additional interesting biology.

Concerns about codon usage analyses:

Main text, twelfth paragraph: The reviewers were surprised that you were able to detect codon usage differences for HGT events that occurred that far back in time (e.g., third position synonymous sites are saturated between D. melanogaster and D. pseudoobscura). Thus, explanations of any differences between LOTUS and OSK parts of the oskar gene should be carefully scrutinized. In particular:

1) If we understand the methods correctly, the process used to calculate codon usage is somewhat unorthodox. By calculating the frequency of all 64 codons, rather than usage of alternate synonymous codons, this metric of similarity will be influenced by amino acid composition. Thus, genes where the 5' and 3' ends look quite different in their codon usage could result from very different amino acid composition between the two halves, rather than differences in synonymous codon usage. This raises the possibility that the large differences in codon usage between the LOTUS and OSK domains could be driven by differences in amino acid composition. Do either of these domains (especially OSK) have a particularly unusual or distinctive amino acid composition, relative to other arthropod genes?

2) We recommend that you conduct this analysis using a metric of codon usage that is independent of amino acid composition, such as the codon adaptation index or relative synonymous codon usage.

3) There are many other possible explanations for why the coding sequences of two domains in a protein may exhibit different codon usage that may have to do with domain folding, translational selection, etc. that would be worth considering as alternative explanations.

4) If the oskar gene is cut in half following the procedure used for the genes in the 17 genomes, rather than comparing just the LOTUS and OSK domains, are the 5' and 3' halves still significantly discordant for AT3/GC3/codon usage?

5) The manuscript states: "if evolutionary time had not completely erased the original GC3 content and codon use signatures from the putative bacterially donated sequence (OSK), we might detect some differences in these parameters both from the LOTUS domain, and from the host genome." All of the analyses presented appear to address the first issue (OSK vs. LOTUS), but I did not see any analyses addressing the second question, whether these parameters systematically differ between the OSK domain and the rest of the host genome. If some of the analyses in the paper do bear on this question, this connection should be made more explicit. This seems like an important question, and would help to inform whether the observed differences between the LOTUS and OSK domains are in fact due to unusual features of the OSK domain specifically.

6) In Figure 3—figure supplement 1, why is the correlation for AT3 between the 5' and 3' ends of genes positive, but negative for GC3? This seems counter-intuitive to me.

7) We don't understand this sentence: "Thus, we sampled each codon at least twice, preserving the coding frame." Why does cutting each gene in half at a randomly chosen location sample each codon twice (or more)?

8) Barplots in Figure 3A and B: it would be more informative to see the full distribution of correlations for all non-oskar genes. It would also be useful to see the points for the LOTUS and OSK domains highlighted in Figure 3—figure supplement 1. In general, Figure 3—figure supplement 1 appears to be more informative than Figure 3.

9) Figure 3C: we expect there are many points within the "intra-gene" set that are not displayed? If this is true, it would be more transparent to allow the boxplot whiskers to extend to the full range of the data.

10) Figure 3D is hard to understand – those two boxplots show two null distributions, but we don't see where the differences between the LOTUS and OSK domains are indicated.

Concerns about phylogenetic analyses/results:

11) Although the reviewers appreciate that the MUSCLE sequence alignment program is one of the state-of-the-art software for this type of analyses, it is fair to say that the use of different alignment programs can sometimes generate considerable variation in phylogenetic inference (e.g., https://academic.oup.com/mbe/article/30/3/642/1038709). We request that the authors use at least a couple of additional programs for sequence alignment (e.g., PRANK and T-Coffee) and rebuild the trees for the two domains. This should provide a sanity check that the key conclusions of their work are not sensitive to method/alignment software.

12) Main text, seventh paragraph: to really claim that the dipteran LOTUS domain sequences do not group together with the LOTUS domain sequences from other insects, you should do a topology constraint analysis (like you've done for the HGT). Is the ML topology where these two groups of sequences are forced into monophyly significantly different from the unconstrained ML topology? The reviewers think you need to show that these two topologies are significantly different to be able to claim that this is not simply an artifact of doing phylogenetic analyses using a short sequence alignment. Also note that your statement, "the phylogenetic interrelationships of these [LOTUS] sequences is largely consistent with the current species or family level trees for the corresponding insects", contradicts your findings/arguments in the aforementioned paragraph.

13) It is not clear how the two domains fused and when (approximately) they did so. I think it would be useful for the readers if the authors speculated in a small paragraph their hypothesis (based on their knowledge of the distribution of these two domains in insects) when the fused oskar gene originated.

Other broad comments:

14) Main text, fourth paragraph: why are you using two different thresholds for your blast searches of the protein versus the two domains?

15) The discussion and cited studies on HGT were too narrow and well known examples of bacterial to insect HGT not cited (e.g., Husnik et al., 2013; Sloan et al., 2014; Acuna et al., 2012, to mention just a few).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Bacterial contribution to genesis of the novel germ line determinant oskar" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Patricia Wittkopp as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Eve Gazave (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The study by Blondel et al. provides phylogenetic evidence that the OSK domain of the key developmental gene oskar appears to have been originally acquired from a bacterium. oskar is a key developmental gene and its functions are well studied but its origins remain unknown. This study sheds significant light on its origin and believe will be of interest not just to evo-devo afficionados, but more broadly to developmental biologists and evolutionary biologists. The manuscript is overall clearly written and straightforward to understand.

Essential revisions:

While the reviewers appreciated the authors' additional analyses on codon usage between the two domains of the oskar gene, they raised numerous concerns about the statistical analyses performed as well as for the inference that the observed patterns of codon usage may stem from the HGT event (see detailed comments below). The reviewers thought that the argument that the observed patterns are remnants of the HGT event is highly unlikely and hard to reconcile with everything that we know about the (fast) rate with which codon bias evolves. The reviewers also raised several remaining issues in the calculations of the codon usage statistics, which are substantial and would require additional, extensive analyses.

Given that the manuscript is a short communication and that the codon bias analyses are not mentioned in the title or Abstract (so their removal does not impact the manuscript's key result and discovery), our recommendation is that the authors remove all analyses associated with codon usage. If the authors can do so, there is broad agreement that the rest of this manuscript would be suitable for publication and would be accepted without the need for additional revisions (everyone concurred that the phylogenetic aspects of the manuscript are well done and will be interesting to a broad audience). Alternatively, if the authors feel strongly that they wish to keep the codon usage analyses in their manuscript, our recommendation is that the manuscript should be rejected. We sincerely hope that you decide to implement the reviewers' suggestions so that your manuscript can be accepted for publication at eLife.

Specific comments about codon usage analyses:

The reviewers appreciate the additional analyses that the authors have included regarding the differences in codon useage between the LOTUS and OSK domains of oskar. However, some of the changes are not presented clearly, and the rest appear to undermine the authors' claim that codon useage in oskar reflects its HGT hybrid origin.

First, there are some ambiguities and contradictions within the manuscript about the new analyses. The legend to Figure 3A states "Scatter plot representing the full distribution of correlations from Pearson correlation analysis for AT3 use in 3' and 5' halves". However, what is shown in Figure 3A is a bivariate plot – unless we misunderstand, calculating the correlation coefficient between the AT3 content for the 5' and 3' halves of each gene should yield a univariate distribution (one correlation coefficient for each gene) – and according to the axis labels, what is shown are the residuals (?) or Z-score (are these the same thing?) of AT3 for each 5' and 3' half of each gene. We are similarly confused about this statement: "The Z score ranges of correlations for the oskar domains are within the distribution for all genes in the genome, although correlations of use across the gene are lower for oskar than for non-oskar genes".

It is stated in the main text and in the Materials and methods that the residuals/Z-scores are calculated for each insect genome separately: "Pooling the residuals together revealed that the GC3 content was significantly different between the LOTUS and OSK domains, compared to what would be expected within an average gene in that genome"; "Then, Z scores for each sequence from the Intra-Gene, OSK or LOTUS domain sequences were calculated against the corresponding genome frequency distribution." But if this were the case, wouldn't the plots in Figure 3—figure supplements 1 and 2 be centered on (0,0)? At least Figure 3—figure supplement 1 looks as if the Z-scores were calculated from the combined distributions of AT3 pooled across all 17 genomes, which we do not think is appropriate, since genomes differ in AT/GC content. For this reason, we also think Figure 3A should be changed to Z-scores calculated for each genome separately.

Second, comparing the correlation in AT3/GC3 between the LOTUS and OSKAR domains with the average intra-gene correlation (either within a genome or across all genomes) does not seem to be a good indication of whether the correlation for oskar is unusual – as suggested by Figure 3A, many genes have correlations well above or below the mean for that genome, and likely have a lower correlation than observed for oskar. If even some genes in these genomes have AT3/GC3 correlations between their 5' and 3' halves that are as low or lower than oskar's (are some even negative?), and presumably this is not due to the same hybrid evolutionary origin as hypothesized for oskar , then how confident can we be that this low correlation reflects the HGT origin for oskar? We apologize for not raising this issue in the first round of review, but we did not quite understand what was represented in Figure 3C, D, E.

Third, we still think that the methods used to compare codon usage between the 5' and 3' ends of non-oskar genes are not fully comparable to comparing codon usage between the LOTUS and OSK domains. The OSK domain comprises the 3' 33% of oskar while the LOTUS domain comprises 16% of the protein, from 23-39% of the length from the 5' end. So the LOTUS domain makes up a smaller fraction of oskar than the methods used to sample the 5' halves of other genes, which could generate a more biased usage in the LOTUS domain. Probably more importantly, assuming that the LOTUS and OSKAR domains are functional, coherent units within the oskar protein, we might expect their amino acid composition to be unrepresentative of simply the 5' or 3' halves of genes, if most of those halves include multiple protein domains and/or truncate protein domains. It's hard to know what the perfect control set is here, but it would be informative to at least compare codon usage across two different discrete protein domains within a number of genes as was done for oskar.

Fourth, as the revised manuscript states, and as is clearly shown in Figures 3A, B (our questions about those figures notwithstanding), Figure 3—figure supplement 2, and Figure 3—figure supplement 6: codon useage in oskar genes is actually not unusual relative to their host genomes, or when it is unusual, this is true for both OSKAR and LOTUS domains (Figure 3—figure supplement 6A). Drawing the alternate conclusion in the face of these results confuses the manuscript.

Finally, we reiterate that we have difficulty believing, a priori, that "evolutionary time had not completely erased the original GC3 content and codon use signatures from the putative bacterially donated sequence (OSK)". Codon usage evolves over very rapid evolutionary timescales, (for example Akashi 1996, Genetics 144:1297), and can diverge genome-wide within a genus (see the 12 Drosophila genomes paper: Clark et al. 2007, Nature 450: 203-218, Figure 5). There is still much we do not understand about the evolution of synonymous codon usage (for example https://doi.org/10.1534/genetics.119.302542). Nonetheless, everything we do know suggests that either neutral or selective pressures should have long ago erased any codon usage signatures retained from a bacterial origin of the OSKAR domain. If the difference in AT3/GC3/codon useage is indeed unusual between the OSKAR and LOTUS domains of oskar (a conclusion that the manuscript has yet to convincingly demonstrate), then we insist that this is much more likely to be due to some unknown feature of oskar function that constrains its codon usage, than it is to reflect its evolutionary origin. As the authors mention in the revised manuscript, given that oskar mRNA is localized in the oocyte, this provides an entirely plausible constraint on the mRNA sequence independent of its coding role. We note that FlyBase also has annotated a lncRNA that almost entirely overlaps with the oskar mRNA in D. melanogaster; we don't know what evidence supports this annotation, but if true, this could indicate additional constraints that could shape codon usage. But in the end, we think such speculation is of limited value to the manuscript if the reader is not convinced that the codon usage is indeed unusually different between the two domains in oskar.
