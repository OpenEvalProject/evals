# Wild worm embryogenesis harbors ubiquitous polygenic modifier variation

## Authors

- Annalise B Paaby<sup>1</sup> †
- Amelia G White<sup>1</sup>
- David D Riccardi<sup>1</sup>
- Kristin C Gunsalus<sup>1</sup>
- Fabio Piano<sup>1</sup>
- Matthew V Rockman<sup>1</sup> †

### Affiliations

1. Department of Biology and Center for Genomics and Systems Biology New York University New York United States
2. New York University Abu Dhabi Abu Dhabi United Arab Emirates

† Corresponding author

## Abstract

Embryogenesis is an essential and stereotypic process that nevertheless evolves among species. Its essentiality may favor the accumulation of cryptic genetic variation (CGV) that has no effect in the wild-type but that enhances or suppresses the effects of rare disruptions to gene function. Here, we adapted a classical modifier screen to interrogate the alleles segregating in natural populations of Caenorhabditis elegans: we induced gene knockdowns and used quantitative genetic methodology to examine how segregating variants modify the penetrance of embryonic lethality. Each perturbation revealed CGV, indicating that wild-type genomes harbor myriad genetic modifiers that may have little effect individually but which in aggregate can dramatically influence penetrance. Phenotypes were mediated by many modifiers, indicating high polygenicity, but the alleles tend to act very specifically, indicating low pleiotropy. Our findings demonstrate the extent of conditional functionality in complex trait architecture.

## Introduction

The effect of gene disruption on an organism depends on a combination of the gene's function and the genetic background in which it resides (Chandler et al., 2013; Chari and Dworkin, 2013; Vu et al., 2015). The average human genome contains loss-of-function alleles for 100 or more genes, some of which cause known genetic diseases (Abecasis et al., 2010; MacArthur et al., 2012); disease expression depends on exposure of the disease allele, such as by homozygosity, but also on variants elsewhere in the genome that act as penetrance modifiers (Hamilton and Yu, 2012). When looked for, such modifier variation is routinely observed; in model organisms, this phenomenon is recognized as genetic background effects (Chandler et al., 2013).

Genetic background effects are an example of cryptic genetic variation (CGV), the class of mutations that affect phenotype under rare conditions (Gibson and Dworkin, 2004; Paaby and Rockman, 2014). Unlike mutations that are always silent with respect to phenotype, or mutations that always affect phenotype, CGV is invisible until a perturbation changes the molecular, cellular, or developmental processes that govern its phenotypic expression. In addition to genetic perturbations, CGV may be ‘released’ by environmental exposure, like the modern changes to diet that have been hypothesized to underlie the emergence of complex metabolic diseases in humans (Gibson, 2009). The concept of CGV has been of longstanding interest to evolutionary theorists because it explains how populations might store alleles that enable adaptation when conditions change (Dobzhansky, 1941; Waddington, 1956; McGuigan et al., 2011), but its extent, architecture, and role in nature is largely unknown. Most of our empirical knowledge of CGV arises from studies that inhibited the heat shock chaperone protein HSP90 to reveal previously-silent mutational effects across many taxa, which probably represents a general mechanism that buffers genome-wide functional variation (Queitsch et al., 2002; Yeyati et al., 2007; Jarosz and Lindquist, 2010; Chen and Wagner, 2012; Rohner et al., 2013).

In this study, we aimed to systematically uncover and characterize genome-wide variation affecting a major metazoan process. C. elegans embryogenesis is both complex and typically invariant, which may favor the accumulation of mutations that act in a conditionally-functional manner (Gibson and Dworkin, 2004; Paaby and Rockman, 2014). We revealed these alleles by perturbing known embryonic genes and measuring differences in penetrance across multiple wild-derived strains.

## Results

To uncover the nature and extent of natural genetic modifiers in C. elegans embryogenesis, we individually targeted 29 maternal-effect genes in each of 55 wild strains from around the globe (Figure 1). Worms were grown in liquid culture in 96-well plates, and RNAi was delivered by feeding the parental generation Escherichia coli expressing dsRNA against the target genes (Cipriani and Piano, 2011). Each combination of strain and targeted gene was replicated in at least eight wells, and within each well an average of 10 adult worms contributed hundreds of offspring that were screened as dead or alive. Estimates of embryonic lethality were extracted by the image analysis algorithm DevStaR, which was developed to recognize C. elegans developmental stages for this specific application (White et al., 2013). We then modeled the probability that an embryo would fail to develop as a function of targeted gene, worm strain, strain-by-gene interaction, and several experimental variables (see ‘Materials and methods’).

![Figure 1.](https://cdn.elifesciences.org/articles/09178/elife-09178-fig1-v3.jpg)

**Figure 1.:** (A) Under ordinary conditions, wild-type Caenorhabditis elegans embryos hatch into larvae. (B) We targeted maternally-expressed genes by RNAi to induce embryonic lethality that varied in penetrance across strains. (C) L1 larvae in the parental generation were fed Escherichia coli expressing dsRNA against target genes, in 96-well plates in liquid media. 5 days later, wells were imaged to capture the penetrance of embryonic lethality in the next generation. (D, E) Raw images were evaluated using DevStaR (White et al., 2013), which identified objects as larvae (blue), dead embryos (green), or adults (red).

The experiments revealed extensive variation in embryonic lethality caused by genetic differences among strains (Figure 2). We observed substantial variation among strains, with some strains exhibiting more embryonic lethality across all targeted genes than other strains, but also significant gene-specific among-strain variation, where particular combinations of gene and strain exhibited surprisingly high or low lethality (Table 1). These two classes of variation represent two general mechanisms of modifier action. Informational modifiers (such as suppressors of nonsense mutations in classical screens [e.g., Hodgkin et al., 1989], and modifiers of germline RNAi sensitivity in this experiment) alter the effect of the initial perturbation in a non-gene-specific manner, while gene-specific modifiers reveal functional features of the targeted locus. By screening for modifiers of many different perturbations, we are able to quantitatively partition the effects of these mechanisms. Of the variation attributable to heritable modifier variation among worms, half is explained by non-gene-specific informational modifiers and half by gene-specific modifier effects (Table 1).

![Figure 2.](https://cdn.elifesciences.org/articles/09178/elife-09178-fig2-v3.jpg)

**Figure 2.:** Each cell represents the embryonic hatching success for a strain and targeted gene, averaged from at least eight replicate wells. The rows and columns are ordered by average hatching, and boxplots illustrate hatching phenotypes for each strain (across all targeted genes) and for each gene (across all strains).

**Table 1.**
 Factorial analysis of deviance of lethality phenotypes for 55 wild-type strains in 29 perturbations of germline-expressed genes


<table>
  <thead>
    <tr>
      <th></th>
      <th>DF</th>
      <th>Deviance</th>
      <th>Resid. DF</th>
      <th>Resid. Dev</th>
      <th>F</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>NULL</td>
      <td>–</td>
      <td>–</td>
      <td>17,855</td>
      <td>2,201,873</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Strain</td>
      <td>54</td>
      <td>338,618</td>
      <td>17,801</td>
      <td>1,863,255</td>
      <td>334.697</td>
      <td>&lt;10−15</td>
    </tr>
    <tr>
      <td>Targeted gene</td>
      <td>28</td>
      <td>1,152,310</td>
      <td>17,773</td>
      <td>710,945</td>
      <td>2196.584</td>
      <td>&lt;10−15</td>
    </tr>
    <tr>
      <td>Adults per well</td>
      <td>1</td>
      <td>35,318</td>
      <td>17,772</td>
      <td>675,627</td>
      <td>1885.113</td>
      <td>&lt;10−15</td>
    </tr>
    <tr>
      <td>Date</td>
      <td>1</td>
      <td>2406</td>
      <td>17,771</td>
      <td>673,221</td>
      <td>128.416</td>
      <td>&lt;10−15</td>
    </tr>
    <tr>
      <td>Strain × gene</td>
      <td>1512</td>
      <td>349,415</td>
      <td>16,259</td>
      <td>323,806</td>
      <td>12.334</td>
      <td>&lt;10−15</td>
    </tr>
    <tr>
      <td>Strain × adults per well</td>
      <td>54</td>
      <td>6715</td>
      <td>16,205</td>
      <td>317,091</td>
      <td>6.637</td>
      <td>&lt;10−15</td>
    </tr>
    <tr>
      <td>Gene × adults per well</td>
      <td>28</td>
      <td>7358</td>
      <td>16,177</td>
      <td>309,732</td>
      <td>14.026</td>
      <td>&lt;10−15</td>
    </tr>
  </tbody>
</table>

_The table rows report information associated with each term in our statistical model (see ‘Materials and methods’), which represent distinct sources for the variation we observed in embryonic lethality. All terms were highly significant, including the strain-by-gene interaction, which represents variation attributable to cryptic genetic modifiers that act gene-specifically. This term and the strain term, which represents variation attributable to informational modifiers affecting germline RNAi, explain similar amounts of variation, and together account for 31% of the total deviance._

The variation in embryonic lethality attributable to informational modifiers, represented by genetic strain effect in our statistical model, provides an estimate of each strain's sensitivity to exogenous germline RNAi. We observed dramatic variation in sensitivity. Most strains exhibited moderately reduced lethality penetrance relative to the RNAi-sensitive laboratory strain N2, but two strains, the germline RNAi-insensitive strain CB4856 (Tijsterman et al., 2002) and the genetically divergent strain QX1211, showed consistently weak penetrance across the targeted genes (Figure 2). CB4856 harbors a ppw-1 loss-of-function mutation that confers resistance to germline RNAi (Tijsterman et al., 2002), but sequencing shows that QX1211 and other strains with intermediate sensitivity do not. We found that a ppw-1 mutation in the N2 background was more sensitive than CB4856, showing high lethality on mex-3 and pos-1 (Figure 2), indicating that some of the difference between N2 and CB4856 is ppw-1-independent. These results demonstrate that insensitivity to germline RNAi is genetically complex and that wild C. elegans populations harbor many alleles affecting germline RNAi (Elvin et al., 2011; Pollard and Rockman, 2013).

Genetic modifiers of RNAi efficacy in our experiment may affect uptake of dsRNA, general RNAi machinery, or tissue-specific RNAi requirements. To distinguish among these, we targeted tubulin (tba-2), which is expressed ubiquitously. Among wild-type strains, all but four (KR314, JU396, CB4852 and ED3040) showed complete sensitivity to somatic RNAi, indicated by developmental arrest of P0 animals on tba-2, which demonstrates that most wild-type strains take up dsRNA and are capable of RNAi. An rrf-1 deletion mutant, which is sensitive to RNAi against genes expressed in the germline but resistant to RNAi in most somatic tissues (Yigit et al., 2006; Kumsta and Hansen, 2012), grew to adulthood but laid dead embryos, suggesting that germline RNAi successfully silenced maternal tba-2 required for embryonic development. The four somatically-resistant wild strains also exhibited embryonic lethality on tba-2 and other germline-expressed genes, confirming that the modifier variability acts tissue-specifically.

Gene-specific modifiers explain as much of the total variation as the informational modifiers, as estimated by the strain-by-gene interaction term in our model (Table 1), and represent cryptic genetic variation in developmental processes. The modifiers could act via network bypasses, where loss of the targeted gene reveals variation among strains in developmental network structure (e.g., Zhang and Emmons, 2000). Gene-specific modifiers could also act on the extent of the knockdown at a gene-specific level, in a manner akin to intragenic suppressors, resulting in variable residual activity of the targeted gene. This latter class potentially includes gene-specific variation in RNAi sensitivity, perhaps due to heritable variation in transcriptional licensing (Shirayama et al., 2012; Seth et al., 2013), and variation in wild-type expression level of the targeted gene, due to cis- or trans-acting regulatory variation.

Each of the 29 genes we targeted showed significant strain-by-gene interaction coefficients, indicating that genetic modifiers of embryonic gene perturbations are pervasive in natural populations. The coefficients, which are statistical estimates of the gene-specific cryptic phenotypes (see ‘Materials and methods’), exhibit low correlations between gene perturbations known to share function: 36 gene pairs have known physical or genetic interactions, but these did not show significantly elevated phenotypic correlations (χ2 = 2.30, df = 1, p = 0.13). For example, despite high interaction within the par network, which underlies polarization of the zygote, the average pairwise par gene correlation was no higher than the average correlation across all genes (Supplementary file 1). Coefficients for par-3 and par-6 were correlated (correlation = 0.40, p = 0.003), but not for par-3 and pkc-3 (correlation = −0.17, p = 0.24) or par-6 and pkc-3 (correlation = 0.12, p = 0.41), even though their proteins together comprise the anterior polarity complex (Munro et al., 2004). This indicates that the cryptic genetic modifiers have low developmental pleiotropy (Paaby and Rockman, 2013). That is, variation at these loci must influence a very restricted suite of developmental events, since only specific perturbations uncover evidence of their phenotypic effects. For those associated with polarization of the zygote, this may be explained by the high degree of redundancy observed in the process (Beatty et al., 2010; Fievet et al., 2013; Motegi and Seydoux, 2013), as redundancy allows shared function of some factors and specificity of others. Exceptions to the overall trend of low correlation between gene perturbations are discussed below, in the context of genome-wide associations. The low pleiotropy of cryptic alleles may be a result of purifying selection, which over evolutionary time should deplete populations of pleiotropic alleles as they may be more likely to be deleterious (Stern, 2000).

Our quantitative-genetic approach is uniquely able to discern modifier effects that depend simultaneously on variants at many loci. In order to evaluate the polygenicity of the gene-specific variation we observed, and to ask whether cryptic alleles are rare or common in populations, we assessed whether genome-wide genetic similarity among strains explained patterns of phenotypic similarity (Kang et al., 2008). Specifically, we estimated the genomic heritability of the strain-by-gene coefficients. This approach estimates the proportion of gene-specific modifier effects caused by alleles of intermediate frequency at many loci, as these are best captured in estimates of strain relatedness.

We found that for most of the perturbations, variation in lethality penetrance is due to common alleles at many contributing cryptic loci. Of the 29 genes we targeted, 12 exhibited gene-specific modifier variation with genomic heritability estimates greater than 0.80; for 19 genes, estimates were greater than 0.60 (Table 2). However, genotypic similarity failed to explain phenotypic similarity for perturbations of emb-30, mel-32, mex-3, mom-5, par-3 and sur-6 (Table 2). Because these genes exhibit nonzero variance in their associated strain-by-gene interaction coefficients, the strains necessarily harbor cryptic genetic differences affecting lethality under these perturbations. Thus, the genetic architecture of the cryptic variation associated with these genes is likely comprised of few loci, rarer alleles, or both.

**Table 2.**
 Genome heritability estimates for CGV phenotypes associated with 29 targeted genes


<table>
  <thead>
    <tr>
      <th>Targeted gene</th>
      <th>Heritability estimate</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>aph-1</td>
      <td>0.6747</td>
      <td>0.16</td>
    </tr>
    <tr>
      <td>car-1</td>
      <td>0.9149</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>cdc-37</td>
      <td>0.7308</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>cdc-42</td>
      <td>0.3639</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>emb-30</td>
      <td>0.0000</td>
      <td>0.46</td>
    </tr>
    <tr>
      <td>fat-2</td>
      <td>0.3548</td>
      <td>0.32</td>
    </tr>
    <tr>
      <td>lag-1</td>
      <td>0.9075</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>lsy-22</td>
      <td>0.1270</td>
      <td>0.43</td>
    </tr>
    <tr>
      <td>mel-26</td>
      <td>0.8245</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>mel-28</td>
      <td>0.8410</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>mel-32</td>
      <td>0.0000</td>
      <td>0.47</td>
    </tr>
    <tr>
      <td>mex-3</td>
      <td>0.0000</td>
      <td>0.76</td>
    </tr>
    <tr>
      <td>mom-2</td>
      <td>0.7485</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>mom-5</td>
      <td>0.0000</td>
      <td>0.46</td>
    </tr>
    <tr>
      <td>nmy-2</td>
      <td>0.4841</td>
      <td>0.26</td>
    </tr>
    <tr>
      <td>par-1</td>
      <td>0.7871</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td>par-2</td>
      <td>0.9719</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>par-3</td>
      <td>0.0000</td>
      <td>0.77</td>
    </tr>
    <tr>
      <td>par-4</td>
      <td>0.9032</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>par-5</td>
      <td>0.6640</td>
      <td>0.15</td>
    </tr>
    <tr>
      <td>par-6</td>
      <td>0.9258</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>pkc-3</td>
      <td>0.8136</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td>pos-1</td>
      <td>0.7307</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>rfc-3</td>
      <td>0.6958</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td>rpn-9</td>
      <td>0.8715</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>rpn-10</td>
      <td>0.8397</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>skn-1</td>
      <td>0.8599</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>skr-2</td>
      <td>0.8961</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>sur-6</td>
      <td>0.0000</td>
      <td>0.47</td>
    </tr>
  </tbody>
</table>

To locate genome regions harboring gene-specific modifiers, we performed genome-wide association (GWA) mapping using the strain-by-gene interaction coefficients as phenotypes. GWA in C. elegans benefits from high linkage disequilibrium in this species, which reduces the number of tests required to scan the genome, and from high biological replication, which reduces the number of required genotypes relative to human GWA (Rockman and Kruglyak, 2009; Andersen et al., 2012). Nine of the 29 analyses identified at least one single nucleotide polymorphism (SNP) associated with phenotype under a strict Bonferroni-corrected threshold for significance (Supplementary file 2). Across all tests, a total of 19 SNPs or SNP haplotype blocks, defined by SNPs in high linkage disequilibrium (R2 > 0.9), exhibited significant associations at that threshold (Supplementary file 2), while many additional variants exhibit suggestive associations (p < 0.001).

To validate the GWA findings, we introgressed a segment of chromosome II from strain N2 into the genome of wild isolate EG4348. Gene-specific modifier phenotypes for lsy-22 and pkc-3 both have suggestive associations with SNPs on the right arm of chromosome II (the SNPs for lsy-22 are independent of those for pkc-3 [R2 = 0.03], which reside approximately a megabase away, implicating distinct cryptic modifiers). N2 exhibits low lethality when lsy-22 is targeted but high lethality on pkc-3, and EG4348 shows the opposite pattern; in both comparisons, the introgression rescued the original N2 phenotype (Figure 3). These results demonstrate that cryptic variants within the introgression modify the effects of lsy-22 and pkc-3 perturbations.

![Figure 3.](https://cdn.elifesciences.org/articles/09178/elife-09178-fig3-v3.jpg)

**Figure 3.:** Introgression of part of chromosome II from strain N2 (yellow) into strain EG4348 (blue) rescues the N2 phenotype on lsy-22 (F = 12.15, DF = 2, p = 0.001) and pkc-3 (F = 55.87, DF = 2, p < 0.001); genome-wide analyses found associations between this region and hatching phenotypes for both lsy-22 and pkc-3.

To distinguish between intragenic and extragenic modifiers, we considered the list of 129 associated SNPs (in 27 haplotype blocks) with p-values less than 10−4 (Supplementary file 2), all of which exceed the significance of the validated lsy-22 and pkc-3 modifiers. These associations were spread across 15 targeted-gene phenotypes. No SNPs lie within or near the locus of the targeted gene, with the exception of one SNP within the mel-28 locus that associates with the mel-28 phenotype. The mel-28 phenotype is also associated with multiple other SNPs elsewhere in the genome. Thus, most of the CGV detectable by GWA is caused by extragenic modifiers.

Extragenic modifiers may work by affecting, in trans, the expression level of the targeted gene. Recent work shows that differences in severity of RNAi phenotype, for four C. elegans strains perturbed at electron transport chain genes, are associated with differences in expression level of the targeted gene (Vu et al., 2015). However, we find no evidence for the reported pattern of lower expression explaining more severe phenotypes. We examined published transcript abundances for our 29 target genes measured in 4-cell embryos (Grishkevich et al., 2012) under standard conditions in five strains. Five of the genes exhibited significant variation in expression among the strains. In contrast, RNAi against 28 induced significant gene-specific variation in embryonic lethality among the five strains. Overall, both for genes with significant variation and for the whole set, lower expression of the target gene was usually correlated with less severe RNAi phenotypes (20 of 29 genes, p = 0.06), though the correlations are weak. Although undetectable differences in transcript level may nevertheless contribute to embryonic survival, these results suggest that much of the gene-specific modifier effect we observe depends on variation beyond the target gene.

Our GWA mapping identified few SNPs associated with more than one phenotype. For example, lethality phenotypes for 4 of the 7 targeted polarity genes (par-2, -4, -6 and pkc-3) were associated with SNPs, but none were shared. The discrete nature of the genotype–phenotype associations further implies low developmental pleiotropy of the cryptic alleles; variants with effects under one perturbation have no detectable effects under another.

However, the rare instances of multiple associations for individual SNPs implicate a relationship between the targeted genes (Supplementary file 2). The co-association of SNPs in a haplotype block on chromosome IV with lethality phenotypes for rpn-9 and rpn-10 support a known relationship, as rpn-9 and rpn-10 both encode non-ATPase regulatory subunits of the proteasome and are predicted to interact with each other (Zhong and Sternberg, 2006; Lee et al., 2008). The haplotype, which spans approximately 10 kb, was also significantly associated with lethality phenotypes for car-1, mom-5, and skn-1; skn-1 has a role in proteasome-mediated protein homeostasis (Li et al., 2011). Separately, modifier phenotypes for pkc-3, involved in anterior-posterior polarity in the early embryo, and rfc-3, which shows homology to DNA replication factors C and effects on cell cycle synchrony (Piano et al., 2002), are associated with SNPs on both chromosome III and X. Because the co-associations occur twice, with unlinked SNPs (R2 = 0.26), they implicate the presence of at least two interacting cryptic alleles and provide independent lines of evidence for a relationship between pkc-3 and rfc-3, genes with no reported interactions or shared functions.

## Discussion

We have uncovered pervasive CGV that modifies the probability that an embryo will survive a gene perturbation. By evaluating the effects of naturally-occurring mutations on gene knockdowns, we explored a genotypic space that is distinct from that accessible to conventional screens. Our findings provide complementary insight, including discovery of modifier activity that may be detectable only when effects are moderate (Fievet et al., 2013) or polygenic (Mackay, 2014).

We describe the variation we uncovered as ‘cryptic’ because its effect on embryonic survival is dramatically magnified under perturbed conditions. Without gene perturbation, our strains exhibit little embryonic lethality. However, under ordinary conditions the strains vary in gene expression and other cellular or developmental phenotypes (Grishkevich et al., 2012; Farhadifar et al., 2015), which may be the mechanisms by which the cryptic alleles influence the penetrance of the primary perturbation. Previously, we and others have described such differences as variation in ‘intermediate’ phenotypes (Félix and Wagner, 2008; Paaby and Rockman, 2014); whether a genetic variant is cryptic requires definition of the focal phenotype, since even at the morphological level an allele can be cryptic in one trait but penetrant in another (Duveau and Félix, 2012).

Exploration of CGV is not new: CGV has been demonstrated following perturbation of candidate genes (Gibson and Hogness, 1996; Dworkin et al., 2003; Cassidy et al., 2013; Chandler et al., 2013; Chari and Dworkin, 2013); its potential role in adaptive evolution has been considered in diverse systems (Dobzhansky, 1941; Waddington, 1953; Masel, 2006; Ledon-Rettig et al., 2010; McGuigan et al., 2011; Duveau and Félix, 2012; Rohner et al., 2013); and most extensively, it has been characterized following inhibition of HSP90 (Rutherford and Lindquist, 1998; Queitsch et al., 2002; Yeyati et al., 2007; Jarosz and Lindquist, 2010). Here, we show by systematic evaluation that the phenomenon of conditionally functional variation pervades even the highly stereotyped and controlled process of embryogenesis.

We found that gene-specific cryptic variation affects every targeted gene, implying that wild populations harbor many enhancers and suppressors of critical embryonic genes. In humans, such penetrance modifiers may mediate expression of genetic diseases arising from loss-of-function mutations (Abecasis et al., 2010; Hamilton and Yu, 2012; MacArthur et al., 2012), and if their crypsis is environmentally influenced they may also explain modern disease susceptibility (Gibson, 2009). Our screen also revealed dramatic variation among wild-type strains in their responses to exogenous RNAi in the germline. Somatic RNAi response has been shown to influence C. elegans susceptibility to viral infection; variation in germline RNAi may affect vertical viral transmissibility (Félix et al., 2011) as well as transposon activity (Sijen and Plasterk, 2003; Vastenhouw and Plasterk, 2004). The variation we describe illustrates how conditionally-functional relationships between genes may pervade the variation on which natural selection acts, affecting how complex traits evolve (True and Haag, 2001; Félix, 2007; Wang and Sommer, 2011; Verster et al., 2014) and the nature of their genetic architecture (Mackay, 2014). Moreover, this variation has major implications for model system biologists that work with a single genetic strain.

## Materials and methods

### C. elegans strains

We evaluated laboratory strain N2, originally derived from Bristol, England, and 54 wild-type strains derived from populations around the world. The wild-type strains were chosen with reference to genotype data (Rockman and Kruglyak, 2009; Andersen et al., 2012); we avoided haplotype-identical isolates, which can occur even across disparate sampling locations, and included the most diverged genotypes at the population level. The wild-type strains were: AB1, AB2 (Adelaide, Australia), CB3197, PS2025 (Altadena, CA, USA), CB3198 (Pasadena, CA, USA), CB4852 (Rothamsted, England), CB4856 (Hawaii, USA), CB4857 (Claremont, CA, USA), CB4932 (Taunton, England), ED3010, ED3017, ED3021 (Edinburgh, Scotland), ED3040 (Johannesburg, South Africa), ED3042, ED3046 (Western Cape, South Africa), ED3073 (Limuru, Kenya), EG4347, EG4348, EG4945, EG4951 (Salt Lake City, UT, USA), EG4724 (Amares, Portugal), JU1088 (Japan), JU1171, JU1172 (Chile), JU258 (Madeira, Portugal), JU301 (LeBlanc, France), JU319, JU347 (Merlet, France), JU362, JU366, JU371, JU694 (Franconville, France), JU396, JU398, JU399, JU406 (Hermanville, France), JU440 (Beauchene, France), JU533 (Primel, France), JU563 (Sainte Barbe, France), JU642 (Le Perreux, France), KR314 (Vancouver, Canada), LKC34 (Madagascar), MY1 (Lingen, Germany), MY14, MY15, MY16 (Mecklenbeck, Germany), MY18, MY21 (Roxel, Germany), PB303 (isolated from an isopod from Ward's Biological Supply), PB306 (isolated from an isopod from Connecticut Valley Biological Supply), PX174 (Lincoln City, OR, USA), PX179 (Eugene, OR, USA), QX1211 (San Francisco, CA, USA), and QX1218 (Berkeley, CA, USA). Isolates were acquired from the Caenorhabditis Genetics Center or kindly shared by members in the worm community. We also assayed N2 mutants NL2557, which carries a deletion at ppw-1 (pk1425) that confers resistance to RNAi in the germline (Tijsterman et al., 2002), and NL2098, which carries a deletion at rrf-1 (pk1417) that confers resistance to RNAi in most somatic tissues (Yigit et al., 2006; Kumsta and Hansen, 2012). These were provided by the Caenorhabditis Genetics Center, which is funded by NIH Office of Research Infrastructure Programs (P40 OD010440).

### Phenotyping embryonic lethality in liquid culture

Worms were grown to large numbers on agarose-media plates, and healthy embryos at least two generations past starvation or thawing were collected using standard bleaching techniques. For each strain, ∼10,000 embryos were plated onto a 15 cm agarose-media plate densely seeded with E. coli OP50. Worms were reared at 20°C with food until gravid, then bleached and the embryos synchronized to the arrested L1 larval stage by rocking in M9 buffer overnight at 20°C. Following the methodology for growing and imaging worms in 96-well plates described in ref. 27, larvae were washed and diluted to 10 worms per 20 μl of S buffer with additives. Worms were dispensed with a peristaltic pump (Matrix Wellmate) in 20 μl volumes into wells of flat-bottomed 96-well plates (in rows, 8 strains per plate) already containing 30 μl of the appropriate RNAi feeding bacteria. Each plate was replicated eight times, and N2 was dispensed on every plate. After dispensing, plates were stored at 20°C in sealed humid chambers for 5 days. Three sets of eight worm strains were dispensed per experimental cycle; we performed a total of three cycles over 3 months.

### RNAi vectors

In our initial survey, we targeted 41 germline-expressed genes and one somatic gene (tba-2). The germline-expressed genes were chosen following exploratory examination of a larger set of embryonic genes for which observations of embryonic lethality phenotypes were reported on wormbase.org. The final set of 41 were selected by eliminating genes with effects on post-embryonic development or sterility, by including genes with a range of lethality penetrance in N2, and by including the seven core members of the par pathway. We targeted the genes by feeding the worms HT115 E. coli bacteria expressing dsRNA for their targets. Bacteria had been transformed with pL4440-derived RNAi feeding vectors into which target DNA had been cloned (Timmons et al., 2001) and which carry genes for ampicillin and tetracycline resistance. We also included E. coli carrying the empty pL4440 vector, for a total of 43 RNAi vectors in the survey. The majority of the RNAi vectors we used were obtained from the Ahringer feeding library (Kamath and Ahringer, 2003). These included: aph-1 (VF36H2L.1), car-1 (Y18D10A.17), cdc-37 (W08F4.8), cdc-42 (R07G3.1), ceh-18 (ZC64.3), cyb-2.1 (Y43E12A.1), emb-30 (F54C8.3), fat-2 (W02A2.1), gad-1 (T05H4.14), lag-1 (K08B4.1), lin-5 (T09A5.10), lsy-22 (F27D4.2), mel-26 (ZK858.4), mel-28 (C38D4.3), mel-32 (C05D11.11), mes-1 (F54F7.5), mex-3 (F53G12.5), mom-2 (F38E1.7), mom-5 (T23D8.1), nmy-2 (F20G4.3), nos-3 (Y53C12B.3), ooc-3 (B0334.11), par-1 (H39E23.1), par-2 (F58B6.3), par-3 (F54E7.3), par-5 (M117.2), par-6 (T26E3.3), pkc-3 (F09E5.1), pos-1 (F52E1.1), rfc-3 (C39E9.13), rpn-10 (B0205.3), rpn-12 (ZK20.5), rpn-9 (T06D8.8), skn-1 (T19E7.2), skr-2 (F46A9.4), spat-1 (F57C2.6), spat-2 (Y48A6B.13), sur-6 (F26E4.1), tba-2 (C47B2.3), and ztf-1 (F54F2.5). We also used two feeding vectors created and kindly shared by M. Mana, for genes gpb-1 (F13D12.7) and par-4 (Y59A8B.14).

We constructed a frozen RNAi bacterial feeding library in 96-well plates with 20% glycerol. The bacteria were distributed across the plates in columns (12 vectors per plate); the mom-2 vector was included on every plate. Using a 96-pin replicator, bacterial colonies were transferred from the frozen libraries and grown on LB agar plates (100 μg/ml ampicillin, 12 μg/ml tetracyclin). LB broth (50 μg/ml ampicillin) in 96-deep-well plates was inoculated from the solid cultures using the pin replicator and grown overnight in a 37°C shaker. Cultures were induced with 1 mM IPTG for two hours and dispensed into 96-well flat-bottom plates using a Tecan Aquarius robot.

### Excluding genes from the analysis

Although we evaluated 41 genes in our experiment, in our final analysis we included results only for 29. Perturbing gpb-1 and lin-5 induced growth defects in multiple strains such that the parental generation of worms failed to develop to reproductive maturity, indicating that these genes have effects outside of embryogenesis. We also identified ten genes (ceh-18, cyb-2.1, gad-1, mes-1, ooc-3, nos-3, rpn-12, spat-1, spat-2 and ztf-1) that induced no or extremely low embryonic lethality. As they were indistinguishable from the empty vector negative control, we excluded them from analysis.

### Image acquisition and data extraction

5 days after the experimental cycle was initiated, the L1 larvae had developed into egg-laying adults and consumed the RNAi bacteria so that the wells were optically clear. Wells were photographed at the point at which viable embryos had hatched but not developed past early larval stages. We captured single images of each well using a DFC340 FX camera and a Z16 dissecting microscope (Leica Microsystems, Inc., Buffalo Grove, IL), a Bio-precision motorized stage with adaptors for the 96-well plates and stage fittings (Ludl, Inc., Hawthorne, NY), and Surveyor software from Media Cybernetics, Inc. (Warrendale, PA). We used a 1.2 ms exposure at 17.3× magnification.

Data were extracted from the images using the automated image analysis system DevStaR (White et al., 2013). DevStaR is an object recognition machine that classifies each object in the image as an adult, larva or embryo using a support vector machine and global shape recognition. Embryonic lethality estimates were derived from the proportion of embryos in each well relative to all progeny (embryos plus larvae). During the development of DevStaR, each of the approximately 30,000 images in this experiment were manually evaluated and assigned qualitative scores for the number of embryos and the number of larvae, and exact counts were determined for the adults in each well. These data provided independent phenotype estimates and demonstrate that DevStaR is accurate and reliable (White et al., 2013), and we used the manually-collected adult count data in our analyses evaluating the number of adults in each well.

### Statistical analyses

The counts of dead embryos and living larvae from each experimental well were bound together as a single response variable and modeled using a generalized linear model with a quasi-binomial error structure. In the central analysis, in which we evaluated 55 strains and 29 genes, the model included main effects of strain, targeted gene, number of adult worms per well, and experimental date; and interaction terms for strain-by-gene, strain-by-adults and gene-by-adults, in the form:

$$
E(Y)=g^{−1}(\beta_{0}+\beta_{Strain}X_{Strain}+\beta_{Gene}X_{Gene}+\beta_{Adults}X_{Adults}+\beta_{Date}X_{Date}+\beta_{Strain*Gene}X_{Strain}X_{Gene}+\beta_{Strain*Adults}X_{Strain}X_{Adults}+\beta_{Gene*Adults}X_{Gene}X_{Adults})
$$

where g−1 represents a logit link function. The analysis was conducted using the glm function in R Development Core Team (2010) and model fit was examined with the deviance statistic.

Coefficients from the strain-by-gene interaction term in this model were used as estimates of gene-specific CGV, as they provide quantitative measures of probability of embryonic lethality associated with each perturbation after accounting for contributions from the general degree of lethality of the perturbation, the strain effect associated with variation in informational modifiers affecting germline RNAi, and other experimental variables. The significance of each coefficient was computed by assessing the coefficient ratio against the t-distribution using the summary.glm function. We also performed a mixed-model analysis using the glmer function in the R package lme4 (Bates, 2010) with a logit link function and a binomial error structure, in which all effects except the number of adults were specified as random. Results from this analysis were consistent with the fixed-effects analysis, including tight correlation between the fixed-effect coefficients and the mixed-effect estimates and between the downstream GWAS results; we only report results from the fixed-effects analysis. Other analyses, including those exploring confounding effects of experimental design, fitted models with additional terms for well position and bacterial source to subsets of the data. To identify best-fitting models, terms were sequentially reduced from the full model and model comparison was achieved with the F statistic.

Correlations among gene perturbations were estimated using the Spearman Rank method in R. The coefficients, extracted from the generalized linear model, for each strain on each targeted gene were compared for each pairwise combination of genes. Evidence for known interactions among pairs of genes was collated from wormbase.org (February 2015) and includes physical and genetic interactions. We tested whether gene pairs with known interactions had higher phenotypic correlations using the Kruskal–Wallis method in R.

### Experimental replication and controls

Because we arranged worm strains in fixed rows and RNAi vectors in fixed columns across the 96-well experimental plates, well position was a potentially confounding source of variation in the data. The source of each bacterial culture was also potentially confounding, as each culture was grown independently for each strain on a plate. To estimate the contribution of these variables to the lethality phenotypes, we examined hatching variation for strain N2 on targeted gene mom-2, which we included in every plate. The dataset includes counts of dead and alive offspring from 285 experimental wells. Independent cultures of E. coli bacteria expressing dsRNA against mom-2 only weakly affected hatching (F = 3.12, DF = 2, p = 0.046) (Table 3), and whether a well was on the edge, near the edge, or in the center of the plate had no effect on phenotype (F = 1.39, DF = 2, p = 0.251).

**Table 3.**
 Factorial analysis of deviance of strain N2 lethality on targeted gene mom-2


<table>
  <thead>
    <tr>
      <th></th>
      <th>Df</th>
      <th>Deviance</th>
      <th>Resid. Df</th>
      <th>Resid. Dev</th>
      <th>F</th>
      <th>Pr (&gt;F)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>NULL</td>
      <td>–</td>
      <td>–</td>
      <td>284</td>
      <td>9191.7</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Date</td>
      <td>1</td>
      <td>1060.26</td>
      <td>283</td>
      <td>8131.4</td>
      <td>38.397</td>
      <td>2.0 × 10—09</td>
    </tr>
    <tr>
      <td>Bacterial source</td>
      <td>2</td>
      <td>172.47</td>
      <td>281</td>
      <td>7958.9</td>
      <td>3.123</td>
      <td>0.04556</td>
    </tr>
  </tbody>
</table>

With the exception of N2, strains were assayed in one of three date batches. To evaluate the relative importance of date, we examined the N2 lethality phenotypes for all 29 lethality-inducing genes across the three dates. While the date effect was statistically significant, it explained only 1.9% of the deviance; the gene effect explained 86.6% of the deviance (Table 4). The model that best fits the data also includes main and interaction terms for the number of adults per well, but their effects are similarly negligible.

**Table 4.**
 Factorial analysis of deviance of strain N2 lethality phenotypes across 29 targeted genes


<table>
  <thead>
    <tr>
      <th></th>
      <th>Df</th>
      <th>Deviance</th>
      <th>Resid. Df</th>
      <th>Resid. Dev</th>
      <th>F</th>
      <th>Pr (&gt;F)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>NULL</td>
      <td>–</td>
      <td>–</td>
      <td>2254</td>
      <td>280,706</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Silenced gene</td>
      <td>28</td>
      <td>221,081</td>
      <td>2226</td>
      <td>59,624</td>
      <td>378.3275</td>
      <td>&lt;2 × 10—16</td>
    </tr>
    <tr>
      <td>Date</td>
      <td>1</td>
      <td>6090</td>
      <td>2225</td>
      <td>53,534</td>
      <td>291.8186</td>
      <td>&lt;2 × 10—16</td>
    </tr>
    <tr>
      <td>Adults per well</td>
      <td>1</td>
      <td>249</td>
      <td>2224</td>
      <td>53,285</td>
      <td>11.9248</td>
      <td>0.00056</td>
    </tr>
    <tr>
      <td>Silenced gene × date</td>
      <td>28</td>
      <td>5265</td>
      <td>2196</td>
      <td>48,020</td>
      <td>9.0099</td>
      <td>&lt;2 × 10−16</td>
    </tr>
    <tr>
      <td>Silenced gene × adults per well</td>
      <td>28</td>
      <td>2423</td>
      <td>2168</td>
      <td>45,597</td>
      <td>4.1467</td>
      <td>2.7 × 10—12</td>
    </tr>
  </tbody>
</table>

### Genome-wide association tests

Association analyses of the gene-specific embryonic lethality phenotypes were implemented with the emma.ML.LRT function in the R package emma, which controls for population structure using a kinship matrix and performs efficient mixed-model association using maximum likelihood (Kang et al., 2008). The kinship matrix was determined from a total of 41,188 SNPs across 53 strains; we excluded strains CB4856 and QX1211, as they are essentially insensitive to RNAi in the germline. The SNP genotypes are as described in Andersen et al. (2012) and were downloaded from the website of E Andersen (http://groups.molbiosci.northwestern.edu/andersen/Data.html). We assayed six wild isolates not fully genotyped by that study; see our imputation method below. The phenotype values were the coefficients estimated from the strain-by-gene interaction by the generalized linear model, as they include strain contributions to lethality minus the strain effect, the date effect, and other effects of experimental design. We evaluated SNPs with minor allele counts of 6 or more, which allowed us to interrogate 9362 SNPs. Of these, 3057 exhibit unique genotype identities across the 53 strains, and the strict threshold for significance, following Bonferroni correction for multiple tests, was determined at 0.05/3,057, or 1.6 × 10−5. Genomic heritability estimates for each of the cryptic phenotypes represented by the strain-by-gene coefficients was determined from the genetic and residual error variance components estimated by restricted maximum likelihood, using the function emma.REMLE. Significance was tested by 1000 permutations of strain phenotypes.

### Genotype imputation

Six wild isolates in our study were not fully genotyped using the RAD-seq method by Andersen et al. (2012), and we used the following procedure to impute genotypes at the full set of SNPs. If the strain was identical at the 1454 SNPs assayed by Rockman and Kruglyak (2009) to a strain genotyped by RAD-seq, we used the RAD-seq data of the matching strain. This allowed us to use genotype data of CB4854 for CB3197; JU310 for JU301; JU311 for JU319; JU367 for JU371, and MY10 for MY21. In each of these cases, multiple RAD-sequenced strains collapse into groups of strains that are also identical at the 1454 SNPs, suggesting that this procedure is reliable. Only in the case of JU366 do we encounter uncertainty. At the 1454 SNP markers, this strain is identical to JU360, JU363, and JU368 (and three others not RAD-sequenced). JU360 and JU368 have identical RAD-seq haplotypes, but JU363 is different at 224 sites (of which 164 were tested for association with phenotype). We substituted both JU360 and JU363 as proxies for JU366 and ran the full GWAS pipeline twice; the differences in outcome were negligible, with extremely tight correlation among SNP p-values across all tests and no differences in the set of statistically significant SNPs.

### Validation of CGV by introgression

We created the strain QG611, which carries two markers (mIs12, expressing GFP in the pharynx, and juIs76, expressing GFP in the motor neurons) in the N2 wild-type background. The markers are positioned at the approximate middle and right end of chromosome II, respectively (precise locations are unknown), which flank the region for which lsy-22 and pkc-3 phenotypes were associated. We crossed QG611 to wild-type strain EG4348 and then backcrossed to EG4348 for 20 generations, retaining the N2 introgression by selecting for the double markers. The introgression strain, QG1438, carries the N2 haplotype from approximately II 3,174,000 to the right of II 14,430,751. To test the effect of the introgression on lsy-22 and pkc-3 perturbations, RNAi was induced by feeding on agarose plates following standard protocols (wormbook.org): test worms were singled onto plates, 6 replicates each, at the L4 stage following bleaching and developmental synchronization; worms were transferred daily for 3 days and the number of dead embryos and hatched larvae were counted 24 hr after transfer. Test strains included QG611 (the GFP constructs in QG611 have no effect on phenotype relative to N2, data not shown), EG4348, and QG1438. The data were analyzed using a generalized linear model with a quasi-binomial error structure to test the effect of strain on embryonic lethality.

### Genome sequencing and off-target predictions

Seventeen strains (AB1, AB2, CB3198, CB4852, CB4856, EG4347, EG4348, JU319, JU371, JU1088, JU1171, MY1, MY16, MY18, PB306, PX174, PX179) were examined for sequence variation at the RNAi target sites. Sequences were derived from 100-bp paired-end reads run on an Illumina HiSeq 2500 that were mapped to the N2 reference (ce10) using stampy (Lunter and Goodson, 2011) and variant-called with samtools (Li et al., 2009). We observed nucleotide variation in these genes, but zero mutations in the exons targeted by the RNAi clones we used. Thus, we exclude RNAi mismatch via target locus sequence variation as a source of the phenotypic variation we observed. Off-target predictions for our RNAi clones were generated from a sliding window analysis of matching 21-mers between the RNAi reagent and the C. elegans reference genome (ce10). We predicted no off-target sequence matches for the 29 clones used in our final analysis.

### Comparison of gene expression and embryonic lethality data

To test whether native gene expression of our target genes correlates with the embryonic lethality phenotypes, we downloaded microarray transcriptome data published by Grishkevich et al. (2012). These data were collected on 4-cell embryos, which retain the maternally-inherited mRNA transcripts that were the targets of our study, and include three replicate values (following quantile normalization and log10 transformation) determined from three pools of 50 embryos each. We examined gene expression values for the 29 targeted genes, collected under control conditions, for five strains: AB2, CB4856, CB4857, N2, and RC301 (identical to PX174, which we tested in our study). We tested for the genotypic effect of strain with an ANOVA and for correlations between the transcriptome data and our estimates of gene-specific CGV using the Spearman Rank method. For each gene, we looked for correlation between the average gene expression value for each of the five strains and the strain coefficients from the strain-by-gene interaction term in our statistical analysis. We used the same generalized linear model structure as described above; in this analysis, we included 29 genes and five strains. We used a two-tailed binomial sign test to assess whether the 29 correlations were disproportionately positive or negative.
