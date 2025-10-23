# Peer review - Round 1

Editors:
- Ziyue Gao, University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89096.3.sa0](https://doi.org/10.7554/eLife.89096.3.sa0)

By developing a novel method for detecting genetic variants associated with germline mutation spectrum variation, this important study identifies a new "mutator" locus in a population of inbred mouse strains, although the causal gene(s) and allele(s) within this locus remain uncertain. The authors further demonstrate that this new mutator locus interacts epistatically with a previously identified mutator allele on C>A mutation rate, showcasing the complexity of the genetic basis underlying variation in mutation rate and spectrum. Evidence for major findings in this paper is convincing, and the new method has the potential to be applicable to a variety of experimental systems and natural populations.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89096.3.sa1](https://doi.org/10.7554/eLife.89096.3.sa1)

The mutation rate and spectrum have been found to differ between populations as well as across individuals within the same population. Hypothesizing that some of the observed variation has a genetic basis, the authors of this paper have made important contributions in the past few years in identifying genetic variants that modify mutation rate or spectrum in natural populations. This paper makes one significant step further by developing a new method for mapping genetic variants associated with the mutation spectrum, which reveals new biological insights.

Using traditional quantitative trait locus (QTL) mapping in the BXD mouse recombinant inbred lines (RILs), the authors of this paper previously identified a genetic locus associated with C>A mutation rate. However, this approach has limited power, as it suffers from multiple testing burden as well as noise in the "observed mutation spectrum phenotype" due to rarity and randomness of mutation events. To overcome these limitations, the authors developed a new method that they named "aggregate mutation spectrum distance" (AMSD), which in short measures the difference in the aggregate mutation spectrum between two groups of individuals with distinct genotypes at a specific genomic locus. With this new approach, they recover the previously reported candidate mutator locus (near Mutyh gene) and identify a new candidate locus that modifies the C>A mutation rate on only the mutator allele genetic background at the Mutyh locus. Using more rigorous statistical testing, the authors show convincingly synergistic epistatic effects between the mutator alleles at the two loci.

Overall, the analyses presented are well done and provide convincing evidence for the major findings, including the new candidate mutator locus and its epistatic interaction with the Mutyh locus. The new AMSD method introduced is innovative and outperforms traditional QTL mapping under most conditions, as demonstrated by extensive simulations. I identify no major issues with this paper and think it is very well written.

One of the major advantages of the AMSD method over QTL mapping is alleviation of the multiple testing burden, as one comparison tests for any changes in the mutation spectrum, including simultaneous, small changes in the relative abundance of multiple mutation types. The flip side of this advantage of AMSD is that, when a significant association is detected, it is not immediately clear which mutation type is driving the signal. To narrow the signal to specific candidate mutation type(s), additional analyses are needed, such as testing for differential proportions of each mutation type between individuals with or without the candidate mutator allele. However, such analysis may be less powerful when the mutator allele leads to small changes in the relative abundance of multiple mutation types. This will be an area of improvement for future studies.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89096.3.sa2](https://doi.org/10.7554/eLife.89096.3.sa2)

In this paper Sasani, Quinlan and Harris present a new method for identifying genetic factors affecting germline mutation, which is particularly applicable to genome sequence data from mutation accumulation experiments using recombinant inbred lines. These are experiments where laboratory organisms are crossed and repeatedly inbred for many generations, to build up a substantial number of identifiable germline mutations. The authors apply their method to such data from mice, and identify two genetic factors at two separate genetic loci. Clear evidence of such factors has been difficult to obtain, so this is an important finding. They further show evidence of an epistatic interaction between these factors (meaning that they do not act independently in their effects on the germline mutation process). This is exciting because such interactions are difficult to detect and few if any other examples have been studied.

The authors present a careful comparison of their method to another similar approach, quantitative trait locus (QTL) analysis, and demonstrate that in situations such as the one analysed it has greater power to detect genetic factors with a certain magnitude of effect. They also test the statistical properties of their method using simulated data and permutation tests. Overall the analysis is rigorous and well motivated, and the methods explained clearly.

The main limitation of the approach is that it is difficult to see how it might be applied beyond the context of mutation accumulation experiments using recombinant inbred lines. This is because the signal it detects, and hence its power, is based on the number of extra accumulated mutations linked to (i.e. on the same chromosome as) the mutator allele. In germline mutation studies of wild populations the number of generations involved (and hence the total number of mutations) is typically small, or else the mutator allele becomes unlinked from the mutations it has caused (due to recombination), or is lost from the population altogther (due to chance or perhaps selection against its deleterious consequences).

Nevertheless, accumulation lines are a common and well established experimental approach to studying mutation processes in many organisms, so the new method could have wide application and impact on our understanding of this fundamental biological process.

The evidence presented for an epistatic interaction is convincing, and the authors suggest some plausible potential mechanisms for how this interaction might arise, involving the DNA repair machinery and based on previous studies of the proteins implicated. However as with all such findings, given the higher degree of complexity of the proposed model it needs to be treated with greater caution, perhaps until replicated in a separate dataset or demonstrated in follow-up experiments exploring the pathway itself.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89096.3.sa3](https://doi.org/10.7554/eLife.89096.3.sa3)

Sasani et al. develop and implement a new method for mutator allele discovery in the BXD mouse population. This new method, termed "aggregate mutation spectrum distance" or AMSD, carries several notable strengths, including the ability to aggregate de novo mutations across individuals to reduce data sparsity and to combine mutation rate frequencies across multiple nucleotide contexts into a single estimate. As demonstrated by simulations, this method is better suited to mutator discovery under certain scenarios, as compared to conventional QTL or association mapping. Overall, the theoretical premise of the AMSD method is judged to be both strong and innovative, and the methodology could be extended to other species and populations to enable discovery of additional mutator alleles.

The authors then apply their method to the BXD mouse recombinant inbred mapping population. As proof-of-principle, they first successfully re-identify a known mutator locus in this population on chr4. Next, to assess possible genetic interactions involving this known mutator, Sasani et al. condition on the chr4 mutator genotype and reimplement the AMSD scan. This strategy led them to identify a second locus on chr6 that interacts epistatically with the chr4 locus; mice with "D" alleles at both loci exhibit a significantly increased burden of C>A de novo mutations, even though mice with the D allele at the chr6 locus alone show no appreciable increase in the C>A mutation fraction. This exciting discovery not only adds to the catalog of known mutator alleles, but also reveals key aspects of mutator biology and reinforces the hypothesis that segregating variants in genes associated with DNA repair influence germline mutation spectra.

Despite a high level of overall enthusiasm for this work, there are some limitations to the AMSD method. However, it is my judgement that the authors present a balanced summary of the strengths and weaknesses of their method in the revised manuscript. I also think that the authors' conclusions may actually somewhat undersell the scientific impact of their findings. As the authors note, few mutation rate modifiers have been identified in mammals. This is potentially because large- and moderate-effect modifiers are rapidly selected against due to their deleterious effects, but could also be due to pervasive epistasis wherein modifiers are only expressed on certain "permissive" genetic backgrounds, such as the chr6 locus the authors discover in this paper. The potential background dependence of mutator expression could partially shelter it from the action of selection, allowing the allele persist in populations. This discovery has significant implications for our understanding of mutation rate evolution, but only earns a cursory mention in the paper.
