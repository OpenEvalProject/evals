# Age and diet shape the genetic architecture of body weight in diversity outbred mice

## Authors

- Kevin M Wright<sup>1</sup> ([ORCID: 0000-0001-8772-2687](https://orcid.org/0000-0001-8772-2687))
- Andrew G Deighan<sup>2</sup>
- Andrea Di Francesco<sup>1</sup> ([ORCID: 0000-0001-6867-8203](https://orcid.org/0000-0001-6867-8203))
- Adam Freund<sup>1</sup> ([ORCID: 0000-0002-7956-5332](https://orcid.org/0000-0002-7956-5332))
- Vladimir Jojic<sup>1</sup>
- Gary A Churchill<sup>2</sup> ([ORCID: 0000-0001-9190-9284](https://orcid.org/0000-0001-9190-9284)) †
- Anil Raj<sup>1</sup> ([ORCID: 0000-0003-4412-0883](https://orcid.org/0000-0003-4412-0883)) †

### Affiliations

1. Calico Life Sciences LLC South San Francisco United States
2. The Jackson Laboratory Bar Harbor United States ([ROR:021sy4w91](https://ror.org/021sy4w91))

† Corresponding author

## Abstract

Understanding how genetic variation shapes a complex trait relies on accurately quantifying both the additive genetic and genotype–environment interaction effects in an age-dependent manner. We used a linear mixed model to quantify diet-dependent genetic contributions to body weight measured through adulthood in diversity outbred female mice under five diets. We observed that heritability of body weight declined with age under all diets, except the 40% calorie restriction diet. We identified 14 loci with age-dependent associations and 19 loci with age- and diet-dependent associations, with many diet-dependent loci previously linked to neurological function and behavior in mice or humans. We found their allelic effects to be dynamic with respect to genomic background, age, and diet, identifying several loci where distinct alleles affect body weight at different ages. These results enable us to more fully understand and predict the effectiveness of dietary intervention on overall health throughout age in distinct genetic backgrounds.

## Introduction

Quantifying the contributions of genetic and environmental factors to population variation in an age-dependent phenotype is critical to understanding how phenotypes change over time and in response to external perturbations. The identification of genetic loci that are associated with a complex trait in an age- and environment-dependent manner allows us to elucidate the dynamics and context dependence of the genetic architecture of the trait and facilitates trait prediction. For health-related traits, these genetic loci may also facilitate greater understanding and prediction of age-related disease etiology, which is an important step to genetically or pharmacologically manipulating these traits to improve health.

Standard approaches used to identify genetic loci associated with quantitative traits can be confounded by nonadditive genetic effects such as genotype–environment (G×E) and genotype–age (G×A) interactions (Robinson et al., 2017), contributing to the ‘missing heritability’ of quantitative traits (Sul et al., 2016). The linear statistical models routinely used in genetic mapping analyses do not account for variation in population structure between environments and polygenicity in G×E interactions. Population structure can substantially increase the false-positive rate when testing for G×E associations (Moore et al., 2019). Furthermore, not accounting for polygenic G×E interactions has the potential to incorrectly estimate the heritability of quantitative traits in the context of specific environments (Sul et al., 2016). To address these limitations, recent efforts have generalized standard linear mixed models (LMMs) with multiple variance components that allow for polygenic G×E interactions and environment-dependent residual variation (Sul et al., 2016; Runcie and Crawford, 2019; Moore et al., 2019; Dahl et al., 2020). Moreover, these LMMs substantially increase the power to discover genomic loci that are associated with phenotype in both an environment-independent and environment-dependent manner.

In this study, we used an LMM to investigate the classic quantitative trait, body weight, in a large population of diversity outbred (DO) mice. Body weight was measured longitudinally from early development to late adulthood, before and after the imposition of dietary intervention at 6 months of age. We expect diet and age to be important factors affecting body weight and growth rate; however, it remains to be determined how these factors will interact with genetic variation to shape growth. Two early studies found significant genetic correlations for body weight and growth rate during the first 10 weeks of mouse development, which supported the hypothesis that growth rates during early and late development were affected by pleiotropic loci (Cheverud et al., 1996; Riska et al., 1984). Subsequent experiments found that the heritability of body weight increased monotonically with age throughout development: from 29.3% to 76.1% between 1 and 10 weeks of age (Cheverud et al., 1996), from 6% to 24% between 1 and 16 weeks of age (Gray et al., 2015), and from 9% to 32% between 5 and 13 weeks of age (Parker et al., 2016). The heritability of growth rate also varied with age, but exhibited a peak of 24% at 3 weeks of age and then declined to nearly 4% at 16 weeks of age (Gray et al., 2015). The strength of association and effect size of QTLs for body weight and growth rate were specific to early or late ages and were inconsistent with the hypothesis that pleiotropic alleles affect animal size at early and late developmental stages (Cheverud et al., 1996; Gray et al., 2015). While these results are well supported, their interpretation is somewhat limited because body weight measurements ceased at young ages and significant QTLs encompassed fairly large chromosomal regions. Given these limitations, we were motivated to ask two questions: Will fine-mapping to greater resolution reveal single genes that function at either early or late developmental stages, or reveal multiple genes in tight linkage with variable age-specific effects? How will the effect of these loci change at later ages and under different diets?

We expect the interaction of dietary interventions, such as calorie restriction (CR) or intermittent fasting (IF), with genetics to greatly impact the body weight trajectories of mice. Researchers have observed genotype-dependent reductions in body weight in the 7–50 weeks after imposing a 40% CR diet, and variation in heritability of this trait with age from 42% to 54% (Rikke et al., 2006). A second study subjected a large genetic-mapping population to dietary intervention and identified multiple loci with significant genetic and genotype–diet interaction effects on body weight at 2–6 months of age (Vorobyev et al., 2019). These studies identified substantial diet- and age-dependent genetic variance for body weight in mice, similar to what has been found in humans (Robinson et al., 2017; Couto Alves et al., 2019; Wang et al., 2019). It, however, remains to be determined how the contribution of specific genetic loci to body weight changes in response to different dietary interventions and whether the effects observed in younger mice are indicative of the maintenance of body weight in adult mice.

In order to address these questions, we measured the body weight of multiple cohorts of genetically diverse mice from the DO population (Svenson et al., 2012) from 60 to 660 days of age (Figure 1A). At 180 days of age, we randomized mice by body weight and assigned each mouse to one of five dietary regimes – ad libitum (AL), 20% and 40% daily CR, and 1 or 2 days per week IF. Longitudinal measurements of body weight in these DO mice allowed us to discover the age-dependent genetic determinants of body weight and growth rate in the context of different dietary interventions.

![Figure 1.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig1-v1.jpg)

**Figure 1.:** (A) Outline of study design. (B) Median (interquartile range) body weight in grams and (C) median (interquartile range) growth rate in grams per day for five dietary treatments from 60 to 660 days of age. Vertical gray dotted line denotes the onset of dietary intervention at 180 days of age.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Body weight and growth rate trends as a function of age. Mice in this study also underwent an array of phenotyping procedures; the age range for metabolic cage phenotyping is highlighted in pink, the age range for blood draws is highlighted in blue, and the age range for a battery of challenge-based phenotyping procedures is highlighted in green.

In the following sections, we first describe the study design and collection of the genetic and body weight measurements. Second, we motivate the use of the gene–environment mixed model (G×EMM) (Dahl et al., 2020) to model genetic associations in these data and give an overview of our analyses. We next use this model to identify genetic loci having additive or genotype–diet interaction effects on body weight. We fine-map candidate loci and determine the scope of pleiotropy for age- and diet-specific effects. We find many, but not all, loci are associated with body weight in a narrow age range and localize to small genomic regions, in some cases to single genes. We utilize the full genome sequence of the DO founders and external chromatin accessibility data to further narrow the genomic regions to a small number of candidate variants at each locus. Interestingly, many diet-specific body weight loci localize genes implicated in neurological function and behavior in mice or humans.

## Results and discussion

### Study design and measurements

The DO house mouse (Mus musculus) population was derived from eight inbred founder strains and is maintained at Jackson Labs as an outbred heterozygous population (Svenson et al., 2012). This study contains 960 female DO mice, sampled at generations: 22–24 and 26–28. There were two cohorts per generation for a total of 12 cohorts and 80 animals per cohort. Enrollment occurred in successive quarterly waves starting in March 2016 and continuing through November 2017.

A single female mouse per litter was enrolled into the study after wean age (3 weeks old), so that no mice in the study were siblings and maximum genetic diversity was achieved. Mice were housed in pressurized, individually ventilated cages at a density of eight animals per cage (cage assignments were random). Mice were subject to a 12 hr:12 hr light:dark cycle beginning at 06:00 hr. Animals exit the study upon death. All animal procedures were approved by the Animal Care and Use Committee at The Jackson Laboratory.

From enrollment until 6 months of age, all mice were on an AL diet of standard rodent chow 5KOG from LabDiet. At 6 months of age, each cage of eight animals was randomly assigned to one of five dietary treatments, with each cohort equally split between the five groups (N = 192/group): AL, 20% CR (20), 40% CR (40), 1 day per week fast (1D), and 2 days per week fast (2D) (see Figure 1A). In a previous internal study at the Jackson Laboratory, the average food consumption of female DO mice was estimated to be 3.43 g/day. Based on this observation, mice on 20% CR diet were given 2.75 g/mouse/day and those on 40% CR diet were given 2.06 g/mouse/day. Food was weighed out for an entire cage of eight. Observation of the animals indicated that the distribution of food consumed was roughly equal among all mice in a cage across diet groups.

Mice on AL diet had unlimited food access; they were fed when the cage was changed once a week. In rare instances when the AL mice consumed all food before the end of the week, the grain was topped off midweek. Mice on 20% and 40% CR diets were fed daily. We gave them a triple feeding on Friday afternoon to last till Monday afternoon. As the number of these mice in each cage decreased over time, the amount of food given to each cage was adjusted to reflect the number of mice in that cage. Fasting was imposed weekly from Wednesday noon to Thursday noon for mice on 1D diet and Wednesday noon to Friday noon for mice on 2D diet. Mice on 1D and 2D diets have unlimited food access (similar to AL mice) on their nonfasting days.

From enrollment until 660 days of age, each animal underwent a number of phenotypic assays to assess a wide range of physiological health parameters. These included two 7-day stints in Sable Systems Promethion metabolic cages at 120 and 390 days of age, two blood draws at 160 and 480 days of age, and one of each of the following challenge-based assays at 300–330 days of age: 3-day stint in a cage with wheel, rotarod, grip strength, dual-energy X-ray absorptiometry, echocardiogram, Y-maze spontaneous alternation, and acoustic startle.

#### Body weight measurements

Body weight was measured once every week for each mouse throughout its life. The body weight measurements for this analysis were collated on February 1, 2020, at which point 941 mice (98%) had measurements at 180 days, 890 (93%) at 365 days, 813 (85%) at 550 days, and 719 (75%) at 660 days. For these analyses, we included all body weight measures for each mouse up to 660 days of age. We smoothed out measurement noise, either due to errors in measurement or swaps in assigning measurements to mice, using an $ℓ_{1}$ trend filtering algorithm (Kim et al., 2009), which calculates a piecewise linear trend line for body weight for each mouse over its measurement span. The degree of smoothing was learned by minimizing the error between the predicted fit and measurements at randomly held-out ages across all mice. In the rest of this article, body weight and growth rate refer to the predicted fits from $ℓ_{1}$ trend filtering.

We present the average trends in body weight and growth rate, stratified by dietary intervention, in Figure 1B and C, respectively. The body weight and growth rate trends without $ℓ_{1}$ trend filtering are presented in Figure 1—figure supplement 1. The most prominent observation from these trends is that dietary intervention contributes the most to variation in body weight in this mouse population. After accounting for this source of variation, there remain substantial and different quantities of variation in body weight trends within the different dietary interventions, suggesting the existence of heteroscedastic noise or plausible G×D interaction effects on body weight trajectories.

#### Genotype measurements

We collected tail clippings and extracted DNA from 954 animals (http://agingmice.jax.org/protocols). Samples were genotyped using the 143,259-probe GigaMUGA array from the Illumina Infinium II platform (Morgan et al., 2015) by NeoGen Corp. (genomics.neogen.com/). We evaluated genotype quality using the R package: qtl2 (Broman et al., 2019). We processed all raw genotype data with a corrected physical map of the GigaMUGA array probes (https://kbroman.org/MUGAarrays/muga_annotations.html). After filtering genetic markers for uniquely mapped probes, genotype quality, and a 20% genotype missingness threshold, our dataset contained 110,807 markers.

We next examined the genotype quality of individual animals. We found seven pairs of animals with identical genotypes, which suggested that one of each pair was mislabeled. We identified and removed a single mislabeled animal per pair by referencing the genetic data against coat color. Next, we removed a single sample with missingness in excess of 20%. The final quality assurance analysis found that all samples exhibited high consistency between tightly linked markers: log odds ratio error scores were less than 2.0 for all samples (Lincoln and Lander, 1992). The final set of genetic data consisted of 946 mice.

For each mouse, starting with its genotypes at the 110,807 markers and the genotypes of the 8 founder strains at the same markers, we inferred the founders-of-origin for each of the alleles at each marker using the R package: qtl2 (Broman et al., 2019). This allowed us to test directly for association between founder-of-origin and phenotype (rather than allele dosage and phenotype, as is commonly done in QTL mapping) at all genotyped markers. Using the founder-of-origin of consecutive typed markers and the genotypes of untyped variants in the founder strains, we then imputed the genotypes of all untyped variants (34.5 million) in all 946 mice. Targeted association testing at imputed variants allowed us to fine-map QTLs to a resolution of 1–10 genes.

### Motivating models for environment-dependent genetic architecture

Genome-wide QTL analyses in model organisms over the last decade have predominantly employed linear mixed models (e.g., EMMA Kang et al., 2008), FastLMM [Lippert et al., 2011], GREML [Yang et al., 2011], GEMMA [Zhou and Stephens, 2012], and LDSC [Bulik-Sullivan et al., 2015], expanding on the heuristic that samples sharing more of their genome have more correlated phenotypes than genetically independent samples. We found that the distributions of covariances in body weight, measured at 500 days of age, between animal pairs within the AL treatment were nearly indistinguishable when we partition pairs into high-kinship (>0.2) and low-kinship groups (Figure 2, no significant separation between solid and dashed red lines). However, animal pairs in the 40% CR treatment exhibited significantly lower covariance in body weight in the low-kinship group compared to the high-kinship group (Figure 2, significant separation between solid and dashed orange lines). This observation suggests that the genetic contribution to body weight is different in distinct dietary environments. This observation also motivates the use of recently developed generalized linear mixed models to conduct genome-wide QTL analysis because they more fully account for environment-dependent genetic variances, reduce false-positive rates, and increase statistical power (Yang et al., 2011; Sul et al., 2016; Runcie and Crawford, 2019; Moore et al., 2019; Dahl et al., 2020).

![Figure 2.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig2-v1.jpg)

**Figure 2.:** Phenotypic divergence between animal pairs is quantified by the covariance in body weight at 500 days of age. We plot the cumulative density of body weight covariance for all pairs of animals in the ad libitum (AL) and 40% calorie restriction (CR) dietary treatments, partitioned into high-kinship (>0.2) or low-kinship groups. We test for separability between the high- and low-kinship distributions using the Mann–Whitney U test, and report p-values from this test. The reported area under the curve (AUC) is a standard transformation of the Mann-Whitney U test statistic.

### Simulations

To evaluate the accuracy of G×EMM and compare it against standard linear mixed models like EMMA (Kang et al., 2008), we simulated phenotypic variation under a broad range of values for proportion of phenotypic variance explained by genetics (PVE) in each of two environments. For all simulations, we fixed the total sample size to $N=946$ and used the observed kinship matrix for the 946 DO mice in this study. For these simulations, the environment-specific genetic contribution $PVE_{e}$, environment-specific noise $\sigma_{e}^{2}$, and the relative distribution of samples between environments are the tunable parameters. In order to explore how the two models behaved under a wide range of conditions, we varied $PVE_{e}\in{0.05,0.10,…,0.95}$, fixed $\sigma_{e⁢1}^{2}=\sigma_{e⁢2}^{2}=1.0$, and assigned samples to environments either at a 1:1 ratio or a 4:1 ratio (i.e., a total of 114 parameter values). For each setting of the tunable parameter values, we ran 50 replicate simulations and in each simulation, we randomly assigned samples to one of the two environments. Given the environment assignments, kinship matrix, and the set of tunable parameter values for each simulation, we computed the environment-specific genetic variance using Equation 13, Equation 14, and Equation 15. Next, we generated the vector of phenotypes from a multivariate normal distribution with zero mean and covariance structure dependent upon the observed kinship matrix, environment assignments, tunable parameter settings, and the environment-specific genetic variance for each environment. Using the simulated phenotypes, we computed estimates of $PVE_{t⁢o⁢t}$ under both the EMMA and G×EMM models and estimates of $PVE_{e}$ under the G×EMM model.

We first evaluated the accuracy of $PVE_{t⁢o⁢t}$ estimated from the two models and found that the G×EMM model estimated total PVE with little bias and lower variance compared to EMMA in nearly all simulations across the suite of parameter combinations that we investigated (Figure 3A and B). In particular, we found that EMMA substantially underestimated the total PVE in comparison to G×EMM when samples were equally distributed between environments and there was substantial difference in PVE or noise between environments. This is because $PVE_{e}$ will have a greater impact on $PVE_{t⁢o⁢t}$ when both environments are more equally represented in the study sample.

![Figure 3.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig3-v1.jpg)

**Figure 3.:** (A). Comparison of true $PVE_{t⁢o⁢t}$ to that estimated from EMMA (left panel) and G×EMM (right panel). Simulations were run with an equal number of samples in each environment ($N_{e⁢1}=N_{e⁢2}$) and with the same value for the environment-specific error terms ($\sigma_{e⁢1}^{2}=\sigma_{e⁢2}^{2}=1$). (B). Same as (A) but with a 4:1 ratio of samples between environments ($N_{e⁢1}=4\timesN_{e⁢2}$). (C). Plot of the true $PVE_{e⁢2}$ vs. the G×EMM estimate of $PVE_{e⁢2}$. Gray points are the results of individual simulations, orange lines denote the median and 95% interquartile range (IQR). The three panels differ in the true proportion of phenotypic variance explained by genetics (PVE) specific to environment 1, $PVE_{e⁢1}\in{0.2,0.5,0.8}$. Simulations were run with an equal number of samples in each environment ($N_{e⁢1}=N_{e⁢2}$) and with the same value for the environment-specific error terms ($\sigma_{e⁢1}^{2}=\sigma_{e⁢2}^{2}=1$). (D). Same as (C) but with a 4:1 ratio of samples between environments ($N_{e⁢1}=4\timesN_{e⁢2}$).

Next, we examined the sensitivity and specificity of the G×EMM model to quantify environment-specific genetic contribution to phenotypic variance. We found that when samples were equally distributed between environments, G×EMM accurately estimates $PVE_{e}$ under a wide range of parameter values (Figure 3C). When there was a skew in the number of samples between environments, the $PVE_{e}$ estimate for the environment with the larger sample size was as accurate as when there was no skew in sample size (similar to Figure 3C, result not shown). In contrast, the $PVE_{e}$ estimate for the environment with the smaller sample size was more variable and the median $PVE_{e}$ estimates were consistently lower than the true $PVE_{e}$ (Figure 3D). Finally, we observed that increasing the environment-specific noise terms, $\sigma_{e⁢1}^{2}$ and $\sigma_{e⁢2}^{2}$, increased the variance of our estimates of $PVE_{e}$ but introduced little bias (results not shown).

Overall, the G×EMM model outperforms the EMMA model in estimating total PVE and shows little bias in estimating environment-specific PVE across a broad range of scenarios relevant to our study.

### Overview of analyses

Starting with body weight measurements in 959 mice from 30 to 660 days of age, and founder-of-origin alleles inferred at 110,807 markers in 946 mice, we first quantified how the heritability of body weight and growth rate changes with age and between dietary contexts. We used the G×EMM model (described in detail in ‘Materials and methods’) to account for both additive environment-dependent fixed effects and polygenic gene–environment interactions. We considered two different types of environments: diet and generation. The five diet groups were applied from 180 to 660 days and the 12 generations were applied from 30 to 660 days. Next, we performed genome-wide QTL mapping for body weight at each age independently, testing for association between body weight and the inferred founder-of-origin at each genotyped marker. For ages 180–660 days, we additionally tested for association between body weight and the interaction of diet and founder-of-origin at each marker. We computed p-values using a sequential permutation procedure (Besag and Clifford, 1991; Shim and Stephens, 2015) at each variant for each of the additive and interaction tests and used these to assign significance (Abney, 2015). Finally, for each significant locus, we performed fine-mapping to identify the putative causal variants and founder alleles driving body weight and underlying functional elements (genes and regulatory elements) to ascertain the possible mechanisms by which these variants act.

### PVE of body weight across age and diet

First, we quantified the overall contribution of genetics to variation in body weight and, importantly, how this contribution changed with age. We applied both EMMA and G×EMM to body weight estimated every 10 days. Since the mice from each generation cohort were measured at the same time every week, we used generation as a proxy for the shared environment that mice are exposed to as part of the study design. We accounted for generation-specific fixed effects (α in Equation 1) in both models and genotype-generation random effects (γ) in G×EMM. For ages after dietary intervention ($\geq180$ days), we additionally accounted for diet-specific fixed effects in both models and genotype-diet random effects in G×EMM. We estimated the variance components in the model at each age independently and computed the total and diet-dependent PVE using Equation 7 and Equation 13.

In Figure 4A, we observed that the PVE of body weight steadily increased during early adulthood and up to 180 days of age, when dietary intervention was imposed. The G×EMM model estimates a higher PVE than the EMMA model during this age interval because the former model specifically accounts for polygenic genotype-generation effects. Following dietary intervention, PVE decreased in four of the five dietary groups; the one exception was the 40% CR group, which maintained a high PVE ($PVE_{40}≈0.8$) (Figure 4A) and low total phenotypic variance (Figure 4—figure supplement 3A, top-right panel) from 180 to 660 days of age. In contrast, the AL group had the lowest PVE and greatest total phenotypic variance in the same age range. Notably, $ℓ_{1}$ trend filtering of the raw measurements proved useful in quantifying smoothly varying trends in the PVE of body weight and growth rate, and improving our estimates of the PVE of growth rate by reducing the effect of measurement noise (Figure 4—figure supplement 1). Moreover, these results were robust to variation in the genetic data used to calculate the kinship matrix and to survival bias at 660 days of age.

![Figure 4.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig4-v1.jpg)

**Figure 4.:** (A) Body weight proportion of phenotypic variance explained by genetics (PVE) (± SE) for 30–660 days of age. Total PVE estimates are derived from the EMMA (light gray) and gene–environment mixed mode (G×EMM) (dark gray) models. Diet-dependent PVE values were derived from the G×EMM model. Dotted vertical line at 180 days depicts the time at which all animals were switched to their assigned diets. (B) Growth rate PVE; details the same as (A).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** PVE (±SE) of (A) Body weight and (B) growth rate, estimated using raw body weight measurements.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** PVE (± SE) of (A) Body weight and (B) growth rate, overlayed with the timing of bouts of phenotyping.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** (A) PVE (± SE) (left column) and expected phenotypic variance (±SE) (right column) estimated using kinship calculated from founder-of-origin allele probabilities (top row) and biallelic genotypes (bottom row). (B) PVE (±SE) estimated using kinship calculated from founder-of-origin allele probabilities (left column) and biallelic genotypes (right column), after randomly permuting body weight trajectories across mice, within each dietary intervention. (C) PVE (±SE) estimated using all mice in the study (left column) and mice that survived to 660 days of age (right column).

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig4-figsupp4-v1.jpg)

**Figure 4—figure supplement 4.:** PVE (±SE) of body weight was estimated without imposing any non-negativity constraints on the variance components in the gene–environment mixed mode (G×EMM) model.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig4-figsupp5-v1.jpg)

**Figure 4—figure supplement 5.:** Proportion of phenotypic variance explained by genetics (PVE) comparing full and diagonal $Ω$.PVE (± SE) of body weight was estimated with and without a diagonal constraint on $Ω$.

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig4-figsupp6-v1.jpg)

**Figure 4—figure supplement 6.:** Decomposing the total and diet-dependent PVE into contributions from diet terms (diamonds) and contributions from generation terms (x-markers).

The kinship matrix used for estimating these PVE values was computed based on the founder-of-origin of marker variants (Aylor et al., 2011). When using kinship estimated using biallelic marker genotypes (as is commonly done in genome-wide association studies [GWAS]), we observed largely similar trends in PVE; however, differences in PVE between diets after 400 days were harder to discern due to much larger standard errors for the estimates (Figure 4—figure supplement 3A, left panels). To test for bias or calibration errors in our PVE estimates, we randomly permuted the body weight trends between mice in the same diet group and recalculated the total and diet-dependent PVE values. Consistent with our expectations, PVE dropped to nearly zero for the permuted dataset (Figure 4—figure supplement 3B, left panel), indicating that the PVE estimates are well-calibrated. Finally, to evaluate the contribution of survival bias to our estimates, we recomputed PVE at all ages after restricting the dataset to mice that were alive at 660 days. We observed PVE estimates largely similar to those computed from the full dataset, suggesting very little contribution of survival bias to our estimates (Figure 4—figure supplement 3C).

When using kinship computed from genotypes, we note that the PVE in the permuted dataset does not drop to zero, suggesting that genotype-based kinship includes some background relatedness that can explain some of the phenotypic variation even after permuting the labels (Figure 4—figure supplement 3B, right panel). The genotype-based kinship includes two components: the genetic sharing between the founder strains and the genetic sharing arising from the breeding strategy used to develop the DO panel. Randomly permuting the phenotype labels breaks the link between phenotypic similarity and the latter component of genotype-based kinship, but does not effectively break the link with the former component. Kinship computed using the founder allele probabilities explicitly includes only the latter component; this component explains little phenotypic variation once the phenotype labels are randomly permuted.

Next, we quantified the age-dependent contribution of genetics to variation in growth rate, enabled by the dense temporal measurement of body weight. As before, we applied EMMA and G×EMM to growth rate estimated every 10 days. In Figure 4B, we observed that PVE of growth rate increases rapidly during early adulthood, and then decreases to negligible values around 240 days of age. In contrast to body weight, PVE of growth rate is substantially lower at all ages, and there is little divergence in PVE across diet groups for most ages. Notably, the decrease and subsequent increase in growth rate PVE coincide with specific metabolic, hematological, and physiological phenotyping procedures that these mice underwent at specific ages as part of the study (Figure 1—figure supplement 1). Due to lower values and greater variance in PVE of growth rate with age, we focus on body weight throughout the rest of the article.

In summary, the 40% CR intervention produced the greatest reduction in average body weight and maintained a high PVE after dietary intervention. This is because the genetic variance in body weight remained relatively high and the environmental variance remained relatively low throughout this interval. In contrast, body weight PVE steadily decreased with age in each of the four less restrictive diets, which was due to a steady increase in noise (nongenetic variance) and not a decrease in the genetic variance of body weight (Figure 4—figure supplement 3A). Even though the genetic variance in body weight is nearly constant across diets from 180 to 660 days of age, the effect of specific variants may change with age.

### Genome-wide QTL analysis of body weight across age and diet

We sought to identify loci significantly associated with body weight in a diet-dependent and age-dependent manner. To this end, we tested for association between the inferred founder-of-origin of each typed variant and body weight at each age independently. We note that body weight measurements taken at different ages are not independent; that is, we may detect a locus at a specific age if it has small effects on body weight acting over a long period of time or a large effect on body weight, resulting in rapid bursts in growth. Thus, a locus identified as significant at a specific age indicates its cumulative contribution to body weight at that age.

We identified 29 loci significantly associated with body weight at any age in the additive or interaction models using a genome-wide Bonferroni-corrected $p\leq10^{−4}$ threshold for both the additive and the genotype–diet interaction tests (Figure 5—figure supplement 1). Additionally, we report suggestive genotype–diet interaction QTLs using a weaker threshold of $p\leq10^{−3}$. The Bonferroni correction was computed based on the expected number of linkage-disequilibrium (LD) blocks in our dataset; as a proxy for the number of LD blocks, we used the number of top eigenvalues of the LD matrix between genotyped variants that explained at least 90% of the variance across markers. This threshold also corresponds to a 10% variant-level expected false discovery rate, using the Benjamini–Hochberg method (Benjamini and Hochberg, 1995). In order to focus on highly significant associations, we also used the number of eigenvalues explaining 99.5% of the variance across markers (Gao et al., 2010), resulting in a more stringent threshold of $p\leq1.1\times10^{−5}$ (see Table 1). Notably, these thresholds hold for the interaction tests as well because we have only one test per marker. Using all biallelic variants imputed from the complete genome sequences of the eight DO founder strains (Keane et al., 2011), we retested the genetic association for the 29 candidate loci with the additive and interaction models. Specifically, we tested for association between all imputed genotype variants and body weight, accounting for kinship estimated using founder-of-origin inferred at genotyped variants as before (see file “emma_vs_gxemm.xlsx” in Data Release: Results for a comparison of the number of significant loci with those obtained using the EMMA model).

**Table 1.**
 Candidate diet-independent and diet-dependent body weight loci.For each locus, we identified the variant with the lowest p-value at any age, the founder allele pattern (FAP) of this variant, the number of significant variants that comprise this lead FAP, the genomic positions spanning these significant FAP variants, and all ages for which at least one FAP variant is associated with body weight. For loci in which the lead FAP is comprised of fewer than 10 significant variants, we also present results for the second FAP. We list candidate genes for loci where the FAP spans three or fewer genes. Highly significant associations ($p\leq1.1\times10^{−5}$) are denoted with ***, significant associations ($p\leq10^{−4}$) with **, and suggestive associations ($p\leq10^{−3}$) with *.


<table>
  <thead>
    <tr>
      <th colspan="5"></th>
      <th colspan="2">FAP position (Mb)</th>
      <th colspan="2">Significant variants</th>
      <th rowspan="2">Significant age range (days)</th>
      <th rowspan="2">Age-dependent nonlinearity</th>
      <th rowspan="2">Lead candidate genes (if ≤3)</th>
    </tr>
    <tr>
      <th>Chrm</th>
      <th>Founder Allele Pattern (FAP)</th>
      <th>FAP rank</th>
      <th colspan="2">p-Value</th>
      <th>Start</th>
      <th>End</th>
      <th>Total</th>
      <th>Open chromatin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="12">Diet-independent</td>
    </tr>
    <tr>
      <td rowspan="2">1</td>
      <td>AJ/NOD</td>
      <td>1</td>
      <td>3.24E-05</td>
      <td>**</td>
      <td>152.046626</td>
      <td>152.046626</td>
      <td>1</td>
      <td>1</td>
      <td>60</td>
      <td rowspan="2">1.44E-05</td>
      <td>Trmt1l, Edem3</td>
    </tr>
    <tr>
      <td>AJ/NOD/129</td>
      <td>2</td>
      <td>3.05E-05</td>
      <td>**</td>
      <td>151.473677</td>
      <td>152.280212</td>
      <td>58</td>
      <td>10</td>
      <td>60</td>
      <td>—</td>
    </tr>
    <tr>
      <td>2</td>
      <td>129/CAST/PWK</td>
      <td>1</td>
      <td>2.17E-05</td>
      <td>**</td>
      <td>77.154962</td>
      <td>77.357295</td>
      <td>80</td>
      <td>8</td>
      <td>120–360</td>
      <td>2.83E-09</td>
      <td>Ccdc141, Sestd1</td>
    </tr>
    <tr>
      <td>3</td>
      <td>AJ/NOD/NZO/CAST</td>
      <td>1</td>
      <td>1.89E-05</td>
      <td>**</td>
      <td>50.533599</td>
      <td>50.595073</td>
      <td>55</td>
      <td>—</td>
      <td>200–260</td>
      <td>5.03E-12</td>
      <td>Slc7a11</td>
    </tr>
    <tr>
      <td rowspan="2">4</td>
      <td>AJ</td>
      <td>1</td>
      <td>6.81E-06</td>
      <td>***</td>
      <td>58.950364</td>
      <td>60.267128</td>
      <td>5</td>
      <td>2</td>
      <td>260–360</td>
      <td rowspan="2">3.82E-19</td>
      <td>Ugcg</td>
    </tr>
    <tr>
      <td>PWK/WSB</td>
      <td>2</td>
      <td>2.80E-05</td>
      <td>**</td>
      <td>59.461248</td>
      <td>59.981846</td>
      <td>39</td>
      <td>3</td>
      <td>100–300</td>
      <td>—</td>
    </tr>
    <tr>
      <td>6</td>
      <td>AJ/NOD</td>
      <td>1</td>
      <td>2.75E-07</td>
      <td>***</td>
      <td>53.61761</td>
      <td>55.555977</td>
      <td>89</td>
      <td>2</td>
      <td>60–200</td>
      <td>1.55E-26</td>
      <td>Creb5</td>
    </tr>
    <tr>
      <td>7</td>
      <td>B6/CAST</td>
      <td>1</td>
      <td>4.20E-06</td>
      <td>***</td>
      <td>71.375007</td>
      <td>72.786849</td>
      <td>47</td>
      <td>1</td>
      <td>80–160</td>
      <td>2.48E-11</td>
      <td>Mctp2</td>
    </tr>
    <tr>
      <td>7</td>
      <td>AJ/129/NZO/PWK</td>
      <td>1</td>
      <td>5.70E-06</td>
      <td>***</td>
      <td>134.08785</td>
      <td>134.704465</td>
      <td>20</td>
      <td>2</td>
      <td>80–200</td>
      <td>9.17E-10</td>
      <td>Adam12</td>
    </tr>
    <tr>
      <td rowspan="2">10</td>
      <td>129/NZO/PWK/WSB</td>
      <td>1</td>
      <td>4.99E-06</td>
      <td>***</td>
      <td>9.078054</td>
      <td>9.078054</td>
      <td>1</td>
      <td>—</td>
      <td>540–660</td>
      <td rowspan="2">9.52E-06</td>
      <td>Samd5</td>
    </tr>
    <tr>
      <td>129/NZO/WSB</td>
      <td>2</td>
      <td>2.25E-05</td>
      <td>**</td>
      <td>8.903387</td>
      <td>9.092694</td>
      <td>10</td>
      <td>2</td>
      <td>540</td>
      <td>Sash1, Samd5</td>
    </tr>
    <tr>
      <td>10</td>
      <td>CAST/PWK</td>
      <td>1</td>
      <td>5.98E-06</td>
      <td>***</td>
      <td>91.163191</td>
      <td>91.905287</td>
      <td>2,779</td>
      <td>81</td>
      <td>120–660</td>
      <td>4.09E-10</td>
      <td>Anks1b, Apaf1</td>
    </tr>
    <tr>
      <td rowspan="2">11</td>
      <td>AJ/NZO/PWK/CAST</td>
      <td>1</td>
      <td>5.89E-05</td>
      <td>**</td>
      <td>58.155424</td>
      <td>58.155424</td>
      <td>1</td>
      <td>—</td>
      <td>80</td>
      <td rowspan="2">2.35E-05</td>
      <td>—</td>
    </tr>
    <tr>
      <td>B6/CAST</td>
      <td>2</td>
      <td>4.91E-05</td>
      <td>**</td>
      <td>56.985645</td>
      <td>59.035309</td>
      <td>603</td>
      <td>70</td>
      <td>80–100</td>
      <td>—</td>
    </tr>
    <tr>
      <td>12</td>
      <td>NZO/CAST</td>
      <td>1</td>
      <td>6.47E-05</td>
      <td>**</td>
      <td>99.520559</td>
      <td>99.907182</td>
      <td>43</td>
      <td>3</td>
      <td>160–260</td>
      <td>3.83E-12</td>
      <td>Foxn3</td>
    </tr>
    <tr>
      <td>15</td>
      <td>B6/129/NZO</td>
      <td>1</td>
      <td>4.77E-07</td>
      <td>***</td>
      <td>99.390603</td>
      <td>99.65295</td>
      <td>92</td>
      <td>20</td>
      <td>260–600</td>
      <td>1.50E-13</td>
      <td>Aqp2, Aqp5, Aqp6</td>
    </tr>
    <tr>
      <td>17</td>
      <td>AJ/NOD/WSB</td>
      <td>1</td>
      <td>8.56E-06</td>
      <td>***</td>
      <td>6.753277</td>
      <td>8.85311</td>
      <td>149</td>
      <td>11</td>
      <td>60–420</td>
      <td>1.23E-10</td>
      <td>Pde10a</td>
    </tr>
    <tr>
      <td>19</td>
      <td>AJ/129/NZO/PWK</td>
      <td>1</td>
      <td>7.90E-05</td>
      <td>**</td>
      <td>23.025043</td>
      <td>23.17612</td>
      <td>58</td>
      <td>14</td>
      <td>80–120</td>
      <td>4.46E-09</td>
      <td>Trpm3, Klf9</td>
    </tr>
    <tr>
      <td colspan="12">Diet-dependent</td>
    </tr>
    <tr>
      <td>1</td>
      <td>NOD/CAST</td>
      <td>1</td>
      <td>4.89E-04</td>
      <td>*</td>
      <td>151.032114</td>
      <td>153.716837</td>
      <td>28</td>
      <td>3</td>
      <td>360–660</td>
      <td>3.32E-04</td>
      <td>—</td>
    </tr>
    <tr>
      <td>2</td>
      <td>AJ/CAST/PWK/WSB</td>
      <td>1</td>
      <td>7.74E-04</td>
      <td>*</td>
      <td>22.192222</td>
      <td>22.78664</td>
      <td>86</td>
      <td>8</td>
      <td>480</td>
      <td>1.32E-04</td>
      <td>—</td>
    </tr>
    <tr>
      <td>2</td>
      <td>PWK</td>
      <td>1</td>
      <td>3.34E-04</td>
      <td>*</td>
      <td>73.590142</td>
      <td>75.371564</td>
      <td>1,672</td>
      <td>44</td>
      <td>280–300</td>
      <td>4.62E-03</td>
      <td>—</td>
    </tr>
    <tr>
      <td>3</td>
      <td>NOD/CAST/PWK/WSB</td>
      <td>1</td>
      <td>3.87E-05</td>
      <td>**</td>
      <td>50.184746</td>
      <td>50.419821</td>
      <td>5</td>
      <td>—</td>
      <td>420–660</td>
      <td>7.90E-04</td>
      <td>Slc7a11</td>
    </tr>
    <tr>
      <td rowspan="2">3</td>
      <td>B6/PWK</td>
      <td>1</td>
      <td>8.29E-05</td>
      <td>**</td>
      <td>156.74554</td>
      <td>156.74554</td>
      <td>1</td>
      <td>—</td>
      <td>660</td>
      <td rowspan="2">1.60E-05</td>
      <td>Negr1</td>
    </tr>
    <tr>
      <td>129/CAST/WSB</td>
      <td>2</td>
      <td>7.33E-04</td>
      <td>*</td>
      <td>156.133466</td>
      <td>156.387825</td>
      <td>170</td>
      <td>8</td>
      <td>660</td>
      <td>—</td>
    </tr>
    <tr>
      <td rowspan="2">4</td>
      <td>129/NOD/PWK</td>
      <td>1</td>
      <td>9.61E-04</td>
      <td>*</td>
      <td>57.696301</td>
      <td>57.84652</td>
      <td>10</td>
      <td>1</td>
      <td>200</td>
      <td rowspan="2">5.10E-07</td>
      <td>Palm2, Pakap, Akap2</td>
    </tr>
    <tr>
      <td>NOD</td>
      <td>2</td>
      <td>9.76E-04</td>
      <td>*</td>
      <td>57.669827</td>
      <td>57.669827</td>
      <td>1</td>
      <td>—</td>
      <td>200</td>
      <td>—</td>
    </tr>
    <tr>
      <td>5</td>
      <td>NOD</td>
      <td>1</td>
      <td>3.88E-05</td>
      <td>**</td>
      <td>19.213904</td>
      <td>21.57007</td>
      <td>153</td>
      <td>16</td>
      <td>420–660</td>
      <td>2.26E-03</td>
      <td>Magi2, Ptpn12</td>
    </tr>
    <tr>
      <td>5</td>
      <td>PWK</td>
      <td>1</td>
      <td>5.84E-04</td>
      <td>*</td>
      <td>68.986655</td>
      <td>70.490341</td>
      <td>277</td>
      <td>—</td>
      <td>360–480</td>
      <td>2.28E-03</td>
      <td>Kctd8</td>
    </tr>
    <tr>
      <td rowspan="2">5</td>
      <td>AJ/129/NOD/WSB</td>
      <td>1</td>
      <td>4.00E-05</td>
      <td>**</td>
      <td>117.543498</td>
      <td>118.050453</td>
      <td>7</td>
      <td>—</td>
      <td>480–540</td>
      <td rowspan="2">1.55E-03</td>
      <td>—</td>
    </tr>
    <tr>
      <td>B6/CAST/PWK</td>
      <td>2</td>
      <td>1.04E-04</td>
      <td>*</td>
      <td>116.797769</td>
      <td>118.270745</td>
      <td>69</td>
      <td>10</td>
      <td>360–600</td>
      <td>—</td>
    </tr>
    <tr>
      <td>6</td>
      <td>B6/CAST/PWK</td>
      <td>1</td>
      <td>1.04E-04</td>
      <td>*</td>
      <td>54.146132</td>
      <td>55.452827</td>
      <td>507</td>
      <td>101</td>
      <td>540–660</td>
      <td>7.51E-04</td>
      <td>Ghrhr</td>
    </tr>
    <tr>
      <td>6</td>
      <td>B6/CAST</td>
      <td>1</td>
      <td>1.68E-05</td>
      <td>**</td>
      <td>139.190506</td>
      <td>140.141694</td>
      <td>111</td>
      <td>5</td>
      <td>240–420</td>
      <td>9.63E-03</td>
      <td>Pik3c2g</td>
    </tr>
    <tr>
      <td>7</td>
      <td>NZO/PWK</td>
      <td>1</td>
      <td>9.60E-04</td>
      <td>*</td>
      <td>133.838117</td>
      <td>133.924023</td>
      <td>218</td>
      <td>3</td>
      <td>420</td>
      <td>3.19E-07</td>
      <td>Adam12</td>
    </tr>
    <tr>
      <td rowspan="2">12</td>
      <td>AJ/B6</td>
      <td>1</td>
      <td>6.29E-04</td>
      <td>*</td>
      <td>78.06102</td>
      <td>79.734912</td>
      <td>10</td>
      <td>2</td>
      <td>420–540</td>
      <td rowspan="2">4.23E-04</td>
      <td>Gphn</td>
    </tr>
    <tr>
      <td>WSB</td>
      <td>2</td>
      <td>9.84E-04</td>
      <td>*</td>
      <td>78.107988</td>
      <td>78.932842</td>
      <td>122</td>
      <td>8</td>
      <td>360–420</td>
      <td>Gphn</td>
    </tr>
    <tr>
      <td>12</td>
      <td>AJ/CAST/PWK/WSB</td>
      <td>1</td>
      <td>3.53E-04</td>
      <td>*</td>
      <td>102.447268</td>
      <td>102.56532</td>
      <td>43</td>
      <td>4</td>
      <td>420–480</td>
      <td>2.59E-05</td>
      <td>—</td>
    </tr>
    <tr>
      <td>13</td>
      <td>NZO/WSB</td>
      <td>1</td>
      <td>1.00E-04</td>
      <td>**</td>
      <td>117.100864</td>
      <td>118.777463</td>
      <td>99</td>
      <td>1</td>
      <td>200–300</td>
      <td>1.14E-03</td>
      <td>Fgf10</td>
    </tr>
    <tr>
      <td>15</td>
      <td>AJ/129/NOD</td>
      <td>1</td>
      <td>3.52E-04</td>
      <td>*</td>
      <td>10.738034</td>
      <td>12.040137</td>
      <td>53</td>
      <td>4</td>
      <td>240–300</td>
      <td>1.27E-04</td>
      <td>—</td>
    </tr>
    <tr>
      <td>17</td>
      <td>B6/129/NZO</td>
      <td>1</td>
      <td>7.52E-04</td>
      <td>*</td>
      <td>6.755865</td>
      <td>7.598818</td>
      <td>26</td>
      <td>3</td>
      <td>300–360</td>
      <td>3.23E-03</td>
      <td>—</td>
    </tr>
    <tr>
      <td>18</td>
      <td>129/CAST</td>
      <td>1</td>
      <td>3.86E-04</td>
      <td>*</td>
      <td>71.36087</td>
      <td>71.58844</td>
      <td>16</td>
      <td>1</td>
      <td>480–540</td>
      <td>6.92E-03</td>
      <td>Dcc</td>
    </tr>
    <tr>
      <td>19</td>
      <td>AJ/B6/WSB</td>
      <td>1</td>
      <td>1.24E-04</td>
      <td>*</td>
      <td>21.806665</td>
      <td>22.051277</td>
      <td>32</td>
      <td>1</td>
      <td>220–300</td>
      <td>3.54E-03</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

Our fine-mapping analysis confirmed 24 candidate loci: 5 loci unique to the additive model, 10 loci unique to the interaction model, and 9 loci significant in both models (Table 1). We identified body weight associations with age-dependent effects from early adulthood to adulthood: four diet-independent loci were associated with body weight exclusively during early adulthood (ages 60–160 days) and three were associated exclusively during adulthood (ages 200–660 days); the remaining seven loci were associated prior to the imposition of dietary restriction at day 180 and continued to be associated into adulthood (Table 1). The majority of diet-dependent loci (12 of 19) had a detectable effect on body weight at least 240 days after dietary intervention (ages 420–660 days; Table 1). For each candidate body weight locus, we sought to determine the likely set of causal variants and estimate the effect of the eight founder alleles in a diet- and age-dependent manner.

### Improved mapping resolution with founder allele patterns

In order to facilitate characterization and interpretation of the genetic associations at each locus, we sought to represent these associations in terms of the effects of founder haplotypes (Zhang et al., 2022). First, we determined the founder-of-origin for each allele at every variant that was significant in at least one age. This allowed us to assign a founder allele pattern (FAP) to each significant variant in the locus. For example, if a variant with alleles A/G had allele A in founders AJ, NZO, and PWK and the allele G in the other five founders, then we assign A to be the minor allele of this variant and define the FAP of the variant to be AJ/NZO/PWK. Next, we grouped variants based on FAP and define the logarithm of the odds (LOD) score of the FAP group to be the largest LOD score among its constituent variants. (Note that, by definition, no variant can be a member of more than one FAP group.) By focusing on the FAP groups with the largest LOD scores, we significantly reduced the number of putative causal variants (Table 1, see file all_significant_snps.csv in Data Release: Results), while representing the age- and diet-dependent effects of these loci in terms of the effects of its top FAP groups. We further narrowed the number of candidates by intersecting the variants in top FAP groups with functional annotations (e.g., gene annotations, regulatory elements, tissue-specific regulatory activity, etc.). For many loci, this procedure identified candidate regions containing 1–3 genes (Table 1), and we provide the full list of all genes within candidate regions in the file all_significant_genes.csv in Data Release: Results. In order to demonstrate the utility of this approach, we first examined a single locus on chromosome 6 strongly associated under the additive model.

We used this approach to examine a diet-independent locus on chromosome 6 significantly associated with body weight during early adulthood (Figure 5A). Interestingly, this same locus was nominally associated with body weight in certain dietary treatments at later ages. We hypothesized that the functional variant(s) responsible for the diet-dependent body weight association at this locus are among the variants in the respective lead FAP groups because they exhibit the strongest statistical association and it is unlikely any additional variants are segregating in this genomic interval beyond those identified in the full genome sequences of the eight founder strains. For the diet-independent locus, at age 120, we identified 87 significantly associated variants; of these, 79 could be assigned to the lead FAP group and shared a similarly high LOD score (Figure 5B). All of these variants are single-nucleotide polymorphisms (SNPs located in the gene Creb5, 78 are intronic and 1 a synonymous exon variant). For the diet-dependent locus, at age 600 days, we identified 617 variants as significant; of these, 507 could be assigned to the lead FAP and shared a similarly high LOD score (Figure 5D). Also, 2 of the 507 variants were intergenic structural variants; of the remaining SNPs, 5 were noncoding exon variants, 167 were intronic, and the remainder were intergenic. Given that all candidate variants were noncoding, we next sought to determine whether they were located in regulatory elements across a number of tissues, identified as regions of open chromatin measured using ATAC-seq (Cusanovich et al., 2018) or DNase-seq (Gorkin et al., 2020) (see file "chromatin_accessibility_celltypes.xlsx" in Data Release: Results for a description of the cell types for each of the assays, and their grouping into tissues). For the diet-independent and diet-dependent loci, we found 2 and 101 variants, respectively, that were located in regions of open chromatin (Figure 5C and E). Notably, both variants with diet-independent effects lay within the same muscle-specific regulatory element located within Creb5, suggesting that these variants likely affected body weight by regulating gene expression in muscle cells.

![Figure 5.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig5-v1.jpg)

**Figure 5.:** (A) Manhattan plots of additive genetic associations and genotype–diet associations on chromosome 6 at multiple ages. (B, D) Fine-mapping loci associated with body weight: diet-independent association at 120 days of age and diet-dependent association at 600 days of age. Solid circles indicate significant variants. Colors denote variants with shared FAPs; ranks 1, 2, and 3 by logarithm of the odds (LOD) score are colored red, orange, and yellow, respectively. (C, E) Significant variants, colored by their FAP group, along with the gene models (shown in blue) and the tissue-specific activity of regulatory elements near these variants (shown in gray). Significant variants that lie within regulatory elements are highlighted as diamonds, and regulatory elements that contain a significant variant are highlighted in black.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** Genetic loci associated with body weight, using G×EMM, at different ages identified under the additive genetic model (subpanels on the left) and genotype–diet interaction model (subpanels on the right). Each circle is a genotyped marker, significant markers are in red.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** Genetic loci associated with body weight, using EMMA, at different ages identified under the additive genetic model (subpanels on the left) and genotype–diet interaction model (subpanels on the right). Each circle is a genotyped marker, significant markers are in red.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** (A) Fine-mapping a locus on chromosome 1 associated with body weight under the additive model (left column) and genotype–diet interaction model (right column). Each circle is a biallelic variant, both imputed and genotyped, and solid circles denote significantly associated variants. Variants are colored according to their founder allele pattern (FAP); FAPs of ranks 1, 2, and 3 (based on logarithm of the odds [LOD] score) are colored red, orange, and yellow, respectively. Panels (B–F) are the same as (A) for loci on chromosomes 2, 4, 12, 17, and 19.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig5-figsupp4-v1.jpg)

**Figure 5—figure supplement 4.:** (A) Fine-mapping a locus on chromosome 3 associated with body weight under the additive model (left column) and genotype–diet interaction model (right column). Each circle is a biallelic variant, both imputed and genotyped, and solid circles denote significantly associated variants. Variants are colored according to their FAP; FAP with ranks 1, 2, and 3 are colored red, orange, and yellow, respectively. (B) Founder allele effect as a function of age for the lead FAP variant from (A) for the diet-independent association (left column) and the diet-dependent association (right column). Panels (C) and (D) are the same as (A) and (B) for a locus on chromosome 7.

Next, we identified a locus on chromosome 12 with strong diet-dependent effects on body weight from 300 to 420 days of age (Table 1; Figure 6). Upon fine-mapping the locus with the strongest association, at 420 days of age, we identified 77 significant variants partitioning into two distinct lead FAP groups, with similarly high LOD scores and centered at the same gene (Figure 6A and B). The rank 1 FAP group contained variants with the minor allele specific to AJ and B6, whereas the rank 2 FAP group contained variants with the minor allele specific to WSB (Figure 6A). We found that the minor allele of the lead imputed variant in the AJ/B6 FAP group was associated with increased body weight in the 2D fasting diet, but had little effect on the other four diets (Figure 6C). In contrast, the minor allele of the lead imputed variant from the WSB-specific FAP group had the largest positive effect on body weight in the AL and 1D fast diet and largest negative effect on body weight in the 40% CR diet (Figure 6C). The striking difference in diet-specific effects for WSB and AJ/B6 alleles suggests that there are multiple functional variants affecting body weight at this locus (e.g., allelic heterogeneity; Singh, 2013). Of the 77 variants, the AJ/B6 FAP group contained six intergenic SNPs and four intronic SNPs spanning three genes: Gphn (gephyrin), Plekhh1, and Rad51b (Figure 6A). One of these 10 variants is located in a regulatory element active specifically in adipose tissue. The remaining 67 significant variants all belonged to the WSB-specific FAP group; of these, 23 SNPs were intergenic and 44 were intronic and centered at the gephyrin gene. Also, 4 of these 67 variants were located in regulatory elements active in adipose tissue as well as other tissues relevant to metabolism (Figure 6D).

![Figure 6.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig6-v1.jpg)

**Figure 6.:** (A) Fine-mapping loci, under the interaction model, at 420 days of age. Significant variants are marked as solid circles. Colors denote variants with shared FAPs; ranks 1, 2, and 3 by logarithm of the odds (LOD) score are colored red, orange, and yellow, respectively. (B) Log odds ratio as a function of age, for a single variant that exhibits the strongest association from each of the top three FAPs. (C) Age and diet-dependent effect size of variants with the strongest associations specific to either the WSB minor allele or AJ/B6 minor allele. (D) Significant variants, colored by their FAP, along with the gene models (shown in blue) and the tissue-specific activity of regulatory elements near these variants (shown in gray). Significant variants that lie within regulatory elements are highlighted as diamonds and regulatory elements that contain a significant variant are highlighted in black.

### No evidence for pleiotropic alleles affecting diet-independent and dependent effects

We identified a diet-independent locus on chromosome 6 significantly associated with body weight during early adulthood and nominally associated with body weight in certain dietary treatments at later ages (Figure 5A). One explanation for this result is a single pleiotropic allele affecting body weight at two distinct stages of life: early adulthood and mid-late adulthood. Alternatively, this result could be explained by multiple alleles at a single locus (perhaps similar to the allelic heterogeneity observed in Figure 6) or multiple loci in tight LD. Fine-mapping this locus using the additive model, we identified the variant with the highest LOD score to be at 53.6 Mb. The minor allele at this lead variant was common to the AJ and NOD founders, while the remaining six founders possessed the alternate allele; this defined the lead diet-independent FAP at this locus to be AJ/NOD (Figure 5B). Separately, we fine-mapped this locus using the interaction model, identified the lead variant at 55.1 Mb, and determined the lead FAP to be B6/CAST/PWK (Figure 5D). These results do not support the pleiotropy hypothesis and were consistent with the hypothesis that distinct body weight alleles derived from different DO founders were responsible for the diet-dependent and diet-independent body weight associations.

We next fine-mapped other QTLs that had diet-dependent and diet-independent associations located in adjacent genomic regions to assess whether the associations were due to a single pleiotropic allele or, as we found on chromosome 6 (Figure 5B and D), the additive and interaction effects were due to distinct alleles. Of the eight additional diet-dependent and diet-independent associations that colocalized to the same genomic region (Table 1), all of them were consistent with the hypothesis that distinct FAPs rather than a single pleiotropic allele were responsible for diet-dependent and diet-independent associations. The first six loci were located in adjacent genomic regions (Figure 5—figure supplement 3). The remaining two loci were composed of similar (although, not identical) FAP groups located in overlapping genomic regions (Figure 5—figure supplement 4). At one of these loci, on chromosome 3, the FAP driving the diet-dependent association was NOD/CAST/PWK/WSB, whereas the diet-independent association was due to AJ/NOD/NZO/CAST (Figure 5—figure supplement 4A). The diet-dependent and diet-independent chromosome 7 loci are due to differential effects between NZO/PWK and AJ/129/NZO/PWK, respectively (Figure 5—figure supplement 2D). In summary, we identified multiple instances of diet-dependent and diet-independent associations that mapped to the same genomic region and for all of these loci we determined that distinct FAPs were responsible for diet-dependent or diet-independent effects on body weight.

### Nonlinear changes in genetic effects with age

We found that the relationship between model LOD score and age was similar for each of the three lead FAPs at the diet-independent and diet-dependent loci on chromosome 6 (Figure 7A and B). The minor allele of the lead variant at the diet-independent locus was associated with increased body weight at young ages (Figure 7C), whereas the minor allele for the lead diet-dependent variant had a positive effect on body weight under the 20% CR diet, a nearly neutral effect under the 40% CR, and a negative effect under the AL diet (Figure 7D). We next measured the effect of each founder allele at the lead diet-independent genotyped marker and, consistent with the lead FAP group for the diet-independent association, the AJ and NOD alleles had large positive effects at young ages (Figure 7E). For the diet-dependent association, B6, CAST, and PWK alleles were associated with decreased body weight in the AL diet and increase in body weight in the 20% CR diet (Figure 7F), consistent with their role in defining the lead diet-dependent FAP group. This example clearly demonstrates the insight gained by focusing on lead FAP variants to link specific founder alleles to variation in body weight and narrow the number of potential functional variants underlying body weight.

![Figure 7.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig7-v1.jpg)

**Figure 7.:** (A) Log odds ratio of additive body weight association as a function of age for the lead variant from each founder allele pattern (FAP) group. Red, orange, and yellow colors denote lead variant for rank 1, 2, and 3 FAPs. (B) Same as (A) for interaction body weight association on chromosome 6. (C, D) Estimated mean (SE) effect on body weight (grams) of the minor allele for the lead imputed variant. For the diet-dependent locus (D), effects are shown for each diet treatment. (E) Estimated mean effect (±SE) on body weight of each founder allele for the genotyped marker with the highest logarithm of the odds (LOD) score from the additive model. (F) Estimated effect (±SE) on body weight of each founder allele under the ad libitum (AL) and 20% calorie restriction (CR) diets.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** (A) Manhattan plots of additive genetic associations and genotype–diet associations on chromosome 5 at multiple ages. (B) Fine-mapping a locus associated with body weight in diet-dependent manner at 660 days of age. Each circle is a biallelic variant, both imputed and genotyped and solid circles denote significantly associated variants. Variants are colored according to their founder allele pattern (FAP); FAPs of ranks 1, 2, and 3 (by logarithm of the odds [LOD] score) are colored red, orange, and yellow, respectively. (C) Significant variants, colored by their FAP, along with the gene models (shown in green) and the tissue-specific activity of regulatory elements near these variants (shown in gray). Significant variants that lie within regulatory elements are highlighted as diamonds, and regulatory elements that contain a significant variant are highlighted in black. (D) Log odds ratio as a function of age, for a single variant that exhibits the strongest association from each of the top three FAPs. (E) Diet-dependent effect size of the minor allele as a function of age, for the variant with the strongest association. (F) Estimated effect of each founder allele in three diets (ad libitum [AL], 20, 40), at the genotyped variant with the strongest diet-dependent association.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/64329/elife-64329-fig7-figsupp2-v1.jpg)

**Figure 7—figure supplement 2.:** For each fine-mapped locus (A-G), we note the location of the variant with the strongest association and the ages at which the genetic association is significant and plot the estimated effect (SE) of this variant as a function of age, under different diets.

Given high temporal resolution in the measurements of body weight, we tested for nonlinearity in the trends of effect size with age for all significant loci in Table 1. Specifically, for each diet-independent locus, we tested for nonlinearity in the effect size trend with age in at least one founder allele of the lead variant, and for each diet-dependent locus, we tested for nonlinearity in at least one (founder, diet) pair at the lead variant (referred to as ‘age-dependent nonlinearity’). In addition to diet-dependent nonlinearity, we also observed age-dependent nonlinearity at the diet-independent locus on chromosome 6 (Figure 7C; $p=1.35\times10^{−13}$). Surprisingly, the nonlinearity at this locus appears to be largely driven by the AJ founder background (Figure 7E; AL, yellow trace, $p=1.55\times10^{−26}$ vs. NOD, navy trace, $p=6.5\times10^{−6}$), indicating that the effects of different founder alleles on body weight can have substantially different trends with age. Overall, we observed age-dependent nonlinearity to be predominant, with all 14 diet-independent loci exhibiting nonlinear trends with at least one founder allele (Table 1). In contrast, we observed nonlinear trends with age for diet-dependent effects to be less common, with only 4 of 19 diet-dependent loci exhibiting nonlinear trends with age in the effects of at least one founder allele under one diet. Additionally, nonlinearity was often specific to a subset of founder strains that are driving the associations at each locus, suggesting that the genetic background plays an important role when interpreting the dynamics of the genetic architecture of body weight in DO mice. Notably, such age-dependent nonlinearity often cannot be discerned even with large cross-sectional data that are typical of modern GWAS in humans.

### Nonlinear changes in diet-specific genetic effects

The diet-dependent locus on chromosome 6 illustrated a rather counterintuitive result; while we observed an approximately linear reduction in median body weight between the AL, 20% CR, and 40% CR diets in response to a linear reduction in calories (Figure 1B), the effects of this locus on body weight were nonlinear in the context of each diet (Figure 7D). We defined diet-dependent effects to have a nonlinear trend with respect to diet (referred to as ‘diet-dependent nonlinearity’) if the genetic effects in the context of either the 20% CR or 1D fast treatments deviated substantially from the average of the genetic effects in the context of AL and 40% CR diets or AL and 2D fast diets, respectively. We observed a second instance of diet-dependent nonlinearity at a locus we mapped to chromosome 5. This locus had the strongest diet-dependent association observed in the genome. The lead FAP group, containing variants with an allele private to the NOD strain, was associated with large positive effect on body weight in the 20% CR diet, a small positive effect in the 1D fast diet, and nearly neutral effects in the 40% CR, 2D fast, and AL diets (Figure 7—figure supplement 1). In total, we found this pattern to be quite common, with 9 of the 19 significant loci identified under the interaction model exhibiting diet-dependent nonlinearity (Figure 7—figure supplement 2).

### Candidate body weight genes linked to neurological and metabolic processes

Of the 24 significant loci from the additive and interaction models, we identified 14 loci with lead FAP groups spanning 1–3 genes (Table 1). Many of these genes implicated in modulating body weight are also known to affect neurological and metabolic processes.

One example is the neuronal growth regulator 1 (Negr1) gene, a candidate linked to body weight in mid-late adulthood via the lead 129/CAST/WSB FAP group within a diet-dependent locus on chromosome 3. This gene is highly expressed in the cerebral cortex and hippocampus in the rat brain (Miyata et al., 2003) and is known to regulate synapse formation of hippocampal neurons and promote neurite outgrowth of cortical neurons (Hashimoto et al., 2008; Sanz et al., 2015). Negr1 has also been implicated in obesity (Lee et al., 2012), autistic behavior, memory deficits, and increased susceptibility to seizures (Singh et al., 2018) in mice, and body mass index (Speliotes et al., 2010), and major depressive disorder (Hyde et al., 2016) in humans. Another example is the gephyrin gene (Gphn) implicated by two distinct FAP groups in the diet-dependent locus on chromosome 12 (Figure 6A). Gephyrin is a key structural protein at neuronal synapses that ensures proper localization of postsynaptic inhibitory receptors. Gephyrin is also known to physically interact with mTOR and is required for mTOR signaling (Sabatini et al., 1999), suggesting two plausible pathways for influencing body weight. On chromosome 1, murine Trmt1l (Trmt1-like), a gene with sequence similarity to orthologous tRNA methyltransferases in other species, was linked to body weight during early adulthood (Figure 5—figure supplement 3A). Mice deficient in this gene, while viable, have been found to exhibit altered motor coordination and abnormal exploratory behavior (Vauti et al., 2007), suggesting that the association at this locus is possibly mediated through modulating exploratory behavior. The association of these three candidates with mouse body weight is consistent with human body mass index and obesity GWAS that found an enrichment of genes active in the central nervous system (Locke et al., 2015; Yengo et al., 2018; Schlauch et al., 2020).

Among candidates that affect metabolic processes, Creb5, a gene linked to diet-independent effects on body weight (Figure 5B), has previously been reported to be linked to metabolic phenotypes in humans, with differential DNA methylation detected between individuals with large differences in waist circumference, hypercholesterolemia, and metabolic syndrome (Salas-Pérez et al., 2019). Another gene important for metabolic control in the liver, Pik3c2g was linked to diet-dependent effects on body weight in mid-adulthood. Pik3c2g-deficient mice are known to exhibit reduced liver accumulation of glycogen and develop hyperlipidemia, adiposity, and insulin resistance with age (Braccini et al., 2015). Edem3, another candidate gene at the locus on chromosome 1 linked to body weight in early adulthood (Figure 5—figure supplement 3A), has previously been linked to short stature in humans based on family-based exome sequencing and differential expression in chondrocytes (Hauer et al., 2019). Possibly sharing a similar mechanism, Adam12, a candidate gene in both a diet-independent and diet-dependent locus on chromosome 7, is known to play an important role in the differentiation, proliferation, and maturation of chondrocytes (Horita et al., 2019).

### Future considerations

To summarize, we found that the effects of age and diet on body weight differ substantially with respect to the genetic background and type of dietary intervention imposed. These results highlight that with knowledge of these environment-dependent effects, we can generate more accurate predictions of body weight trajectories than would be possible from knowledge of genotype, age, or diet alone. Moreover, with the elucidation of specific candidate genes and variants underlying these effects, we are not limited to predicting how this complex quantitative trait changes with age, but can also identify specific targets for genetic or pharmacological manipulation in an effort to improve organismal health.

One important limitation to our study is the lack of direct measurements of food consumption and feeding behaviors for each mouse in the population; this makes it difficult to ascertain how much variation in body weight can be ascribed to variation in such behaviors. Additionally, CR was imposed based on the average food consumed by a typical DO mouse rather than a per-mouse baseline of food consumption. Furthermore, CR interventions were imposed on a per-cage basis, not a per-mouse basis, because all animals were housed in groups of eight. Therefore, the social hierarchy within each cage likely contributed to additional variation in body weight (Baud et al., 2017). Additionally, we note that over the course of this study each animal underwent a number of phenotypic assays (Figure 1—figure supplement 1) that would further contribute to study-specific variation in body weight. Accounting for these sources of variation will be a promising avenue for future research, helping interpret many of the associations identified in our study.

A second important consideration for this study is the potential for survival bias to lead to inflated PVE values and false-positive associations at later ages. To evaluate the presence of survival bias, we computed PVE at all ages restricting to animals that survived to 660 days of age (75% of animals in our study). We observed similar PVE values to those from the full dataset, across the full age range, suggesting that survival bias has very little effect on the results presented in this paper (Figure 4—figure supplement 3C, top-left panel). However, as these animals age and the survival bias of the population increases, genetic analyses of body weight at ages past 660 days will need to explicitly account for this effect.

In this study, we have elucidated the dynamics and context dependence of the genetic architecture of body weight from 60 to 660 days of age. By 660 days of age, nearly all surviving animals have realized their maximum adult body weight and the majority of animals have yet to experience appreciable loss of body weight indicative of late-age physiological decline. Under AL diet, reduced body weight has been associated with greater longevity, whereas under 40% CR conditions, greater longevity is associated with the maintenance of high body weight (Liao et al., 2011). Our future research will assess whether we observe a similar result in this DO population and determine whether alleles at body weight loci are predictive of life span in a diet-dependent manner.

## Materials and methods

### Polygenic models for gene × environment interactions

G×EMM (Dahl et al., 2020) is a generalization of the standard linear mixed model that allows for polygenic G×E effects. Under this model, the phenotype is written in terms of genetic effects as follows:

$$
Y=\alpha_{0}+\sume=1EZ_{e}\alpha_{e}+\sumv=1VG_{v}\beta_{v}+\sume=1E\sumv=1VG_{v}Z_{e}\gamma_{ve}+\epsilon,
$$

where $Y\inR^{N}$ is the vector of phenotypes over $N$ samples, $G_{v},v=1,…,V$ are genotypes of $V$ biallelic SNPs, $Z_{e},e=1,…,E$ are binary vectors over $E$ environments, and $\epsilon$ denotes the residual vector.

In our application, $Y$ is the vector of $ℓ_{1}$ trend filtered body weights at a specific age; we do not standardize the body weights so that the estimated effects are interpretable and comparable across ages. When testing for association with the founder-of-origin of markers, $G_{n⁢v}\in[0,1]^{8};∥G_{n⁢v}∥_{1}=1$ is a vector denoting the probability that the two alleles of the marker came from each of the eight founder lines from which the DO population is derived. $∥⋅∥_{1}$ denotes the $L⁢1$-norm of a vector. Alternatively, when testing for association with the allele dosage of a variant, $G_{n⁢v}\in[0,2]$ is the expected allele count at variant $v$. Finally, $Z_{n⁢e}=1$ denotes that sample $n$ is subject to environment $e$. Prior to dietary intervention, the environments in our model are the 12 generations over which the DO samples span (i.e., $E=12$). After dietary intervention, the environments further include the five diet groups (i.e., $E=17$).

The effects of covariates, $\alpha$, are modeled as fixed while the genetic effects, $\beta$, and genotype–environment effects, $\gamma$, are modeled as random. Assuming heteroscedastic noise, $\epsilon∼N(0,Θ)$, a normal prior on the random genetic effects, $\beta_{v}∼N(0,ϱ^{2}/V)$, and a normal prior on the random G×E effects, $\gamma_{v⋅}∼N(0,\frac{1}{V}Ω)$, we get $Y∼N(\mu,Λ)$, where $\mu=\alpha_{0}+\sum_{e}Z_{e}⁢\alpha_{e}$ and $Λ=Θ+ϱ^{2}K+\sume,e^{′}Ω_{ee^{′}}(K∘(Z_{e}Z_{e^{′}}^{T}))$ is a diagonal matrix with entries specified as $Θ_{n⁢n}=\sum_{e}Z_{n⁢e}^{2}⁢\sigma_{e}^{2}$, $K$ is the kinship matrix with entries defined as $K_{mn}=\frac{1}{V}\sumvG_{mv}^{T}G_{nv}$, $ϱ^{2}$ is the variance of environment-independent genetic effects, $Ω\inℝ^{E\timesE}$ is the variance–covariance matrix representing the co-variation in environment-dependent genetic effects between pairs of environments, and $A∘B$ denotes the Hadamard product of matrices $A$ and $B$. We do not include an environment-independent noise term since it is nonidentifiable.

Off-diagonal elements of Ω quantify the covariance in the interaction effect sizes between pairs of environments; thus, a diagonal Ω assumes that the interaction effect sizes between pairs of environments are uncorrelated. This assumption of diagonal Ω could lead to some bias in the estimates of the variance components, although bias in PVE estimates are expected to be minimal. We computed PVE estimates using a full Ω and a diagonal Ω and observed little difference (Figure 4—figure supplement 5). For the sake of computational simplicity, we assumed all off-diagonal elements of Ω to be zero in this study. Note that each of the above parameters and data vectors in the model may be distinct at different ages.

Recent work has shown that non-negativity constraints on the variance components are both important in order to obtain unbiased estimates and unnecessary to achieve valid estimates of heritability (Steinsaltz et al., 2020). Nevertheless, we constrained the variance components to be non-negative since they are more interpretable in the context of our study. While it is likely that this constraint contributes to the small bias observed in our simulations (Figure 3), we observed almost no bias in heritability estimates for body weight due to the constraint, likely because of strong signals in the data (Figure 4—figure supplement 4). We have also included a flag in our published code to relax this constraint when estimating the variance components.

### Proportion of phenotypic variance explained by genetics

Decomposing the phenotype into genetic and nongenetic effects, $Y=Y_{G}+Y_{\epsilon}$, the expected proportion of phenotypic variance explained by genetic effects is approximately given as

$$
PVE=E⁢[\frac{V⁢[Y_{G}]}{V⁢[Y]}]≈\frac{E⁢[V⁢[Y_{G}]]}{E⁢[V⁢[Y]]}≔\frac{Var_{G}}{Var_{Y}},
$$

where $V⁢[⋅]$ denotes the sample variance. The expected sample phenotypic variance conditional on environment $e$ can be written as

$$
E⁢[V⁢[Y|e]]=\frac{E⁢[\sum_{n}Y_{n}^{2}⁢Z_{n⁢e}]}{N_{e}}-\frac{E⁢[(\sum_{n}Y_{n}⁢Z_{n⁢e})^{2}]}{N_{e}^{2}},
$$

where $Z_{n⁢e}$ is an indicator variable denoting whether sample $n$ belongs to environment $e$, and $N_{e}=\sum_{n}Z_{n⁢e}$ is the number of samples in environment $e$. Under the G×EMM model, starting from Equation 1 and integrating out the random effects, we can write the numerator of the first term in the expectation as

$$
E⁢[\sum_{n}Y_{n}^{2}⁢Z_{n⁢e}]=\sum_{n}\mu_{n}^{2}⁢Z_{n⁢e}+\frac{ϱ^{2}}{V}⁢\sum_{n,v}G_{n⁢v}^{2}⁢Z_{n⁢e}+\sum_{e^{′},e^{′′}}\frac{Ω_{e^{′}⁢e^{′′}}}{V}⁢\sum_{n,v}G_{n⁢v}^{2}⁢Z_{n⁢e}⁢Z_{n⁢e^{′}}⁢Z_{n⁢e^{′′}}+\sum_{n}Θ_{n⁢n}⁢Z_{n⁢e},
$$

and the numerator of the second term in the expectation as

$$
E⁢[(\sum_{n}Y_{n}⁢Z_{n⁢e})^{2}]=(\sum_{n}\mu_{n}⁢Z_{n⁢e})^{2}+\frac{ϱ^{2}}{V}⁢\sum_{v}\sum_{n,n^{′}}G_{n⁢v}⁢G_{n^{′}⁢v}⁢Z_{n⁢e}⁢Z_{n^{′}⁢e}+\sum_{e^{′},e^{′′}}\frac{Ω_{e^{′}⁢e^{′′}}}{V}⁢\sum_{v}\sum_{n,n^{′}}G_{n⁢v}⁢G_{n^{′}⁢v}⁢Z_{n,e^{′}}⁢Z_{n^{′}⁢e^{′′}}⁢Z_{n⁢e}⁢Z_{n^{′}⁢e}+\sum_{n}Θ_{n⁢n}⁢Z_{n⁢e},
$$

where $e^{′}$ and $e^{′′}$ iterate over all environments and $n^{′}$ and $n^{′′}$ iterate over all samples. Therefore, the expected sample phenotypic variance can be decomposed as follows:

$$
E[V[Y|e]]=(\frac{\sumn\mu_{n}^{2}Z_{ne}}{N_{e}}−\frac{(\sumn\mu_{n}Z_{ne})^{2}}{N_{e}^{2}})+ϱ^{2}(\frac{tr(K∘W_{e})}{N_{e}}−\frac{sum(K∘W_{e})}{N_{e}^{2}})+\sume^{′}Ω_{e^{′}e^{′}}(\frac{tr(K∘W_{e}∘W_{e^{′}})}{N_{e}}−\frac{sum(K∘W_{e}∘W_{e^{′}})}{N_{e}^{2}})+tr(Θ∘W_{e})(\frac{N_{e}−1}{N_{e}^{2}}),
$$

where $W_{e}=Z_{e}⁢Z_{e}^{T}$, $tr⁢(⋅)$ denotes that trace of a matrix, $sum⁢(⋅)$ denotes the sum of all entries of the matrix, and $A∘B$ denotes the Hadamard product of matrices $A$ and $B$. The first term quantifies the phenotypic variance explained by fixed effects, the second and third terms together quantify the phenotypic variance explained by genetic effects $(E⁢[V⁢[Y_{G}|e]])$, and the fourth term quantifies the residual (unexplained) phenotypic variance. The total proportion of variance explained by genetics in the entire sample can now be computed using Equation 2.

$$
PVE_{t⁢o⁢t}=\frac{Var_{G}}{Var_{Y}},
$$



$$
Var_{G}=ϱ^{2}(\frac{tr(K)}{N}−\frac{sum(K)}{N^{2}})+\sumeΩ_{ee}(\frac{tr(K∘W_{e})}{N}−\frac{sum(K∘W_{e})}{N^{2}}),
$$



$$
Var_{Y}=Var_{G}+(\frac{(\sum_{n}\mu_{n}^{2})}{N}-\frac{(\sum_{n}\mu_{n})^{2}}{N^{2}})+tr⁢(Θ)⁢(\frac{N-1}{N^{2}}).
$$

The two terms in $Var_{G}$ are genetic contributions to phenotypic variation that are shared across environments and specific to environments, respectively. The second and third terms in $Var_{Y}$ are phenotypic variation explained by fixed effects and unexplained residual phenotypic variation, respectively.

The expected total sample phenotypic variance (across all environments) again has two terms, as in Equation 3; the numerator of the first term is written as

$$
E⁢[\sum_{n}Y_{n}^{2}]=\sum_{n}\mu_{n}^{2}+\frac{ϱ^{2}}{V}⁢\sum_{n}\sum_{v}G_{n⁢v}^{2}+\sum_{e,e^{′}}\frac{Ω_{e⁢e^{′}}}{V}⁢\sum_{n}\sum_{v}G_{n⁢v}^{2}⁢Z_{n⁢e}⁢Z_{n⁢e^{′}}+\sum_{n}Θ_{n⁢n},
$$

and the numerator of the second term is written as

$$
E⁢[(\sum_{n}Y_{n})^{2}]=(\sum_{n}\mu_{n})^{2}+\frac{ϱ^{2}}{V}⁢\sum_{v}\sum_{n,n^{′}}G_{n⁢v}⁢G_{n^{′}⁢v}+\sum_{e,e^{′}}\frac{Ω_{e⁢e^{′}}}{V}⁢\sum_{v}\sum_{n,n^{′}}G_{n⁢v}⁢G_{n^{′}⁢v}⁢Z_{n⁢e}⁢Z_{n^{′}⁢e^{′}}+\sum_{n}Θ_{n⁢n}.
$$

The expected total sample phenotypic variance can be decomposed as follows:

$$
E[V[Y]]=(\frac{\sumn\mu_{n}^{2}}{N}−\frac{(\sumn\mu_{n})^{2}}{N^{2}})+ϱ^{2}(\frac{tr(K)}{N}−\frac{sum(K)}{N^{2}})+\sumeΩ_{ee}(\frac{tr(K∘W_{e})}{N}−\frac{sum(K∘W_{e})}{N^{2}})+tr(Θ)(\frac{N−1}{N^{2}}).
$$

The proportion of variance explained by genetics conditional on environment can be computed by substituting the above in Equation 2.

$$
PVE_{e}=\frac{Var_{G|e}}{Var_{Y|e}},
$$



$$
Var_{G|e}=ϱ^{2}(\frac{tr(K∘W_{e})}{N_{e}}−\frac{sum(K∘W_{e})}{N_{e}^{2}})+\sume^{′}Ω_{e^{′}e^{′}}(\frac{tr(K∘W_{e}∘W_{e^{′}})}{N_{e}}−\frac{sum(K∘W_{e}∘W_{e^{′}})}{N_{e}^{2}}),
$$



$$
Var_{Y|e}=Var_{G|e}+(\frac{(\sum_{n}\mu_{n}^{2}⁢Z_{n⁢e})}{N_{e}}-\frac{(\sum_{n}\mu_{n}⁢Z_{n⁢e})^{2}}{N_{e}^{2}})+tr⁢(Θ∘W_{e})⁢(\frac{N_{e}-1}{N_{e}^{2}}).
$$

The proportion of phenotypic variance explained by genetic effects is equivalent to narrow-sense heritability, once variation due to additive effects of environment, batch, and other study design artifacts have been removed. In this work, we use the more general term, proportion of variance explained, to accommodate variation due to effects of diet and environment.

Under the EMMA model, the expected total sample phenotypic variance simplifies to

$$
E[V[Y]]=(\frac{\sumn\mu_{n}^{2}}{N}−\frac{(\sumn\mu_{n})^{2}}{N^{2}})+ϱ^{2}(\frac{tr(K)}{N}−\frac{sum(K)}{N^{2}})+\theta^{2}(\frac{N−1}{N^{2}}),
$$

where $\theta$ denotes the homoscedastic noise. The first component quantifies the phenotypic variance explained by fixed effects, the second component quantifies the phenotypic variance explained by genetic effects $(E⁢[V⁢[Y_{G}]])$, and the third component quantifies the residual (unexplained) phenotypic variance. Substituting these into Equation 2 gives us the proportion of variance explained by genetics under the EMMA model.

### Genome-wide association mapping

#### Additive genetic effects

To test for additive effect of a genetic variant on the phenotype, we include the focal variant among the fixed effects in the model while treating all other variants to have random effects.

$$
Y=\sumcX_{c}⁢\alpha_{c}+ϕ_{s}⁢G_{s}+\sumv\neqsG_{v}⁢\beta_{v}+\sumv,eG_{v}⁢Z_{e}⁢\gamma_{v⁢e}+\epsilon
$$

Applying the priors described above for $\beta_{v}$, $\gamma_{v}$, and $\epsilon$, we can derive the corresponding mixed-effects model is as follows:

$$
Y∼N(\sumcX_{c}\alpha_{c}+ϕ_{s}G_{s},Λ_{s}),
$$

where $Λ_{s}=Θ+ϱ^{2}K_{s}+\sumeΩ_{ee}(K_{s}∘W_{e})$ and $K_{s}$ is the kinship matrix after excluding the entire chromosome containing the variant $s$ (leave-one-chromosome-out [LOCO] kinship). Leaving out the focal chromosome when computing kinship increases our power to detect associations at the focal variant (Lippert et al., 2011). The test statistic is the log likelihood ratio $Φ^{a}⁢(Y,G_{s})$ comparing the alternate model $ℋ:ϕ_{s}\neq0$ to the null model $ℋ_{0}:ϕ_{s}=0$.

$$
Φ^{a}⁢(Y,G_{s})=log⁡\frac{max⁡ℒ⁢(ϕ_{s},\alpha,\sigma,ϱ,Ω)}{max⁡ℒ⁢(ϕ_{s}=0,\alpha,\sigma,ϱ,Ω)}
$$

#### Genotype–environment effects

To test for effects of interaction between genotype and environment on the phenotype, we include a fixed effect for the focal variant and its interactions with the set of all environments of interest ($ℰ$) while treating all other variants to have random effects for their additive and interaction contributions:

$$
Y=\sumcX_{c}⁢\alpha_{c}+ϕ_{s}⁢G_{s}+\sume\inℰχ_{s⁢e}⁢G_{s}⁢Z_{e}+\sumv\neqsG_{v}⁢\beta_{v}+\sumv\neqs,eG_{v}⁢Z_{e}⁢\gamma_{v⁢e}+\epsilon.
$$

The corresponding mixed-effects model is

$$
Y∼N(\sumc\alpha_{c}X_{c}+ϕ_{s}G_{s}+\sume\inEχ_{se}G_{s}Z_{e},Λ_{s}),
$$

and the test statistic is:

$$
Φ^{i}(Y,G_{s})=log⁡\frac{maxL(χ_{s⋅},ϕ_{s},\alpha,\sigma,ϱ,Ω)}{maxL(χ_{s⋅}=0,ϕ_{s},\alpha,\sigma,ϱ,Ω)},
$$

where $X_{s⁣⋅}$ is a vector notation for all $χ_{s⁢e}$. Note that this statistic tests for the presence of interaction effects between the focal variant and any of the environments of interest.

### Likelihood and gradients for G×EMM model

Under the full G×EMM model, the phenotype $Y$ depends on fixed and random effects as follows:

$$
Y∼N(\mu,Λ),
$$

where $\mu=\alpha_{0}+\sum_{e}Z_{e}⁢\alpha_{e}$ captures all fixed effects and $Λ=Θ+ϱ^{2}K+\sumeΩ_{ee}K∘(Z_{e}Z_{e}^{T})$ captures the covariance after integrating out the random effects. The parameters to be estimated in this model are $\alpha$, $\sigma$, $ϱ$, and $Ω$. The complete log likelihood can be written as

$$
ℒ=-\frac{N}{2}⁢log⁡(2⁢\pi)-\frac{1}{2}⁢log⁢det⁡Λ-\frac{1}{2}⁢(Y-X⁢\alpha)^{T}⁢Λ^{-1}⁢(Y-X⁢\alpha).
$$

Maximizing the log likelihood over $\alpha$ gives us

$$
\alpha^=arg⁡max\alpha⁡ℒ=(X^{T}⁢Λ^{-1}⁢X)^{-1}⁢(X^{T}⁢Λ^{-1}⁢Y).
$$

Substituting this into the log likelihood, we get

$$
L_{\alpha^}=−\frac{N}{2}log⁡(2\pi)−\frac{1}{2}log⁡detΛ−\frac{1}{2}Y^{T}PY,
$$

where $P=Λ^{−1}−Λ^{−1}X(X^{T}Λ^{−1}X)^{−1}X^{T}Λ^{−1}$.

Computing the gradient of $ℒ_{\alpha^}$ involves evaluating the following gradients:

$$
\frac{∂Λ}{∂\sigma_{e}^{2}}=I_{Z_{e}}
$$



$$
\frac{∂Λ}{∂ϱ^{2}}=K
$$



$$
\frac{∂Λ}{∂Ω_{ee}}=K∘(Z_{e}Z_{e}^{T})
$$



$$
∂log⁡detΛ=tr(Λ^{−1}∂Λ)
$$



$$
∂Λ^{−1}=−Λ^{−1}∂ΛΛ^{−1}
$$



$$
∂P=−P∂ΛP,
$$

where $ℐ_{Z_{e}}$ is a diagonal matrix with elements of the vector $Z_{e}$ on the diagonal. Thus,

$$
\frac{∂L_{\alpha^}}{∂\sigma_{e}^{2}}=−\frac{1}{2}tr(Λ^{−1}I_{Z_{e}})+\frac{1}{2}Y^{T}PI_{Z_{e}}PY
$$



$$
\frac{∂L_{\alpha^}}{∂ϱ^{2}}=−\frac{1}{2}tr(Λ^{−1}K)+\frac{1}{2}Y^{T}PKPY
$$



$$
\frac{∂L_{\alpha^}}{∂Ω_{ee}}=−\frac{1}{2}tr(Λ^{−1}K^{e})+\frac{1}{2}Y^{T}PK^{e}PY,
$$

where $K^{e}=K∘(Z_{e}Z_{e}^{T})$.

### Permutations

Since the assumptions underlying the G×EMM model are unlikely to hold exactly in practice, we used permutations to assess the significance of the observed values of $Φ^{a}$ and $Φ^{i}$. Specifically, for each variant $s$, we generated $M$ independent random permutations $\mu_{1},…,\mu_{M}$ of $(1,…,N)$ and computed test statistics $Φ_{m}^{a/i}≔Φ^{a/i}⁢(\mu_{m}⁢(Y),G_{s})$ for each permutation $\mu_{m}$. The p-value associated with $Φ^{a}$ and $Φ^{i}$ is then given as

$$
p^{a/i}=\frac{#{m:Φ_{m}^{a/i}\geqΦ^{a/i}}+1}{M+1}
$$

We used a sequential procedure (Besag and Clifford, 1991; Shim and Stephens, 2015) to compute the p-value that helps avoid large numbers of permutations for nonsignificant results, substantially speeding up computation. Specifically, instead of a fixed large number of permutations $M$, we performed $M_{s}$ permutations for each variant $s$ until $C_{s}^{a/i}≔#⁢{m:Λ_{m}^{a/i}\geqΛ^{a/i}}=10$ or $M_{s}=10^{8}$. The p-value for the sth variant is then a random sample from the interval $[\frac{C_{s}}{M_{s}},\frac{C_{s}+1}{M_{s}+1}]$. This scheme allows us to estimate p-value quickly without carrying out large numbers of permutations at every marker. Although the precision of this estimate is lower for markers that are not significant (i.e., most of the genome), precision increases as the significance of association increases.

### Tests for nonlinearity in trends of effect size with age

We test for nonlinear dependence between effect size and age by comparing two models: a null model that only allows for linear dependence between age and effect size and an alternate model that allows for dependence between effect size and higher-order powers of age. While this test can be applied to evaluate nonlinear effect-size trends for any covariate (e.g., dietary intervention, genotype, etc.), we focus our attention to tests for nonlinear trends in the effect sizes of the founder alleles and the effect sizes of the interaction between founder alleles and diet.

Specifically, the estimated effects $ϕ^_{s⁢t}$ and their standard errors $ψ^_{s⁢t}$ can be modeled as

$$
ϕ^_{st}∼N(ϕ_{st},ψ^_{st});t\in{40,50,…,660}
$$

and the two models of the effect size trends are

$$
H_{nℓ}:ϕ_{st}=\phi_{0}+\phi_{1}t+\phi_{2}t^{2}+\phi_{3}t^{3}H_{ℓ}:ϕ_{st}=\phi_{0}+\phi_{1}t,
$$

where $t$ denotes the ages (in days) at which we test for association between a genetic variant and body weight and $ϕ_{s⁢t}$ the unobserved effect sizes at these ages. We used a likelihood ratio test statistic ($ℵ$) to compare the two models and quantify the evidence for nonlinearity in effect size trends with age and assessed significance using p-values computed using a chi-squared distribution with degree-of-freedom 2.

$$
ℵ=2ln⁡\frac{maxL(\phi)}{maxL(\phi;\phi_{2}=\phi_{3}=0)},
$$

where $ℒ⁢(\phi)$ is the likelihood under the model in Equation 37.

We apply this test for each of the founder effects in each of the 14 diet-independent loci (112 tests) and each of the 19 founder-x-diet interaction effects in each of the diet-dependent loci (760 tests). We assign a diet-independent trend as significantly nonlinear if we observe a $p<10^{−4}$ and assign a diet-dependent trend as significantly nonlinear if we observe a $p<10^{−5}$ (Bonferroni-corrected p-value thresholds).

### Data and software release

Data used in this study, and significant QTLs, can be downloaded from the following links:

Our Python implementation of the EMMA and G×EMM models can be downloaded from https://github.com/calico/do_qtl; (Raj, 2021; copy archived at swh:1:rev:3d23d3fbd7768b74b0bba6183de1570a65a2d93d).
