# Trade-offs in modeling context dependency in complex trait genetics

## Authors

- Eric Weine<sup>1</sup> ([ORCID: 0009-0001-7809-1649](https://orcid.org/0009-0001-7809-1649))
- Samuel Pattillo Smith<sup>1</sup> ([ORCID: 0000-0002-6269-0276](https://orcid.org/0000-0002-6269-0276))
- Rebecca Kathryn Knowlton<sup>4</sup>
- Arbel Harpak<sup>1</sup> ([ORCID: 0000-0002-3655-748X](https://orcid.org/0000-0002-3655-748X)) †

### Affiliations

1. Department of Integrative Biology, The University of Texas at Austin Austin United States ([ROR:00hj54h04](https://ror.org/00hj54h04))
2. Department of Population Health, The University of Texas at Austin Austin United States ([ROR:00hj54h04](https://ror.org/00hj54h04))
3. Department of Human Genetics, University of Chicago Chicago United States ([ROR:024mw5h28](https://ror.org/024mw5h28))
4. Department of Statistics and Data Sciences, The University of Texas at Austin Austin United States ([ROR:00hj54h04](https://ror.org/00hj54h04))

† Corresponding author

## Abstract

Genetic effects on complex traits may depend on context, such as age, sex, environmental exposures, or social settings. However, it remains often unclear if the extent of context dependency, or gene-by-environment interaction (GxE), merits more involved models than the additive model typically used to analyze data from genome-wide association studies (GWAS). Here, we suggest considering the utility of GxE models in GWAS as a trade-off between bias and variance parameters. In particular, we derive a decision rule for choosing between competing models for the estimation of allelic effects. The rule weighs the increased estimation noise when context is considered against the potential bias when context dependency is ignored. In the empirical example of GxSex in human physiology, the increased noise of context-specific estimation often outweighs the bias reduction, rendering GxE models less useful when variants are considered independently. However, for complex traits, we argue that the joint consideration of context dependency across many variants mitigates both noise and bias. As a result, polygenic GxE models can improve both estimation and trait prediction. Finally, we exemplify (using GxDiet effects on longevity in fruit flies) how analyses based on independently ascertained ‘top hits’ alone can be misleading, and that considering polygenic patterns of GxE can improve interpretation.

## Introduction

In organisms and study systems where the environment can be tractably manipulated, gene-by-environment interactions (GxE) are the rule, not the exception (El Soda et al., 2014; Vieira et al., 2000; Des Marais et al., 2013; Smith and Kruglyak, 2008; Paaby and Rockman, 2014). Yet, in complex (polygenic) human traits, there are but a few cases in which models that incorporate GxE explain data—such as genome-wide association study (GWAS) data—better than parsimonious models that assume additive contributions of genetic and environmental factors (Munafò et al., 2014; Kraft and Aschard, 2015; Sella and Barton, 2019). This is true for both physical environments but also for other definitions of ‘E’, broadly construed to be any context that modifies genetic effects, such as age, sex, or social setting (Zhu et al., 2023; Schwaba et al., 2023; Elgart et al., 2022; Duncan and Keller, 2011; Gibson and Lacek, 2020; Brown et al., 2016; Ge et al., 2017; Balliu et al., 2021). GWAS commonly estimate marginal additive effects of an allele on a trait. The estimand here can be thought of as the average effect of the allele over a distribution of multidimensional contexts (Veller et al., 2023). With this view, some differences in allelic effects across contexts are likely omnipresent, but may very well be small, such that the cost of including additional parameters (for context-specific effects) outweighs the benefit of measuring heterogeneous effects. Here, we consider this problem and its connection to the currently underwhelming utility of GxE models in GWAS. First, we rigorously describe the statistical trade-off involved in estimating context specificity at the level of a single variant. Then, we highlight ways in which this trade-off might change as we consider GxE in complex traits, involving numerous genetic variants simultaneously. We begin by framing the problem of estimating context specificity at an individual variant as a bias-variance trade-off. For example, consider the estimation of an allelic effect on lung cancer risk that depends on smoking status. When the allelic effect is estimated from a sample without considering smoking status, the estimate would be biased with respect to the true effect in smokers. We can estimate the effect separately in smokers and non-smokers to eliminate the bias, but the consideration of the additional parameters—smoking status-specific effects—has an associated cost of increasing the estimation variance, compared to an estimator that ignores smoking status. This bias-variance trade-off is closely related to the ‘signal-to-noise’ ratio, where the signal of interest is the true difference in context-specific allelic effects. To demonstrate this trade-off in real data, we consider sex-specific effects on physiological traits in humans. We show that for the majority of traits, it is typically unhelpful to model sex dependency for individual sites since the increase in noise vastly outweighs the signal. We then consider the extension to GxE in complex traits. Complex trait variation is primarily due to numerous genetic variants of small effects distributed throughout the genome (Fisher, 1930; Falconer and Mackay, 1996; Yengo et al., 2022; Zwick et al., 2000). Simultaneously considering GxE across multiple variants may decrease estimation noise if the extent and mode of context specificity is similar across numerous variants. This would tilt the scale in favor of context-dependent estimation. In addition, we show how conventional approaches for detecting and characterizing GxE, which focus on the most significant associations, may lead to erroneous conclusions. Finally, we discuss implications for complex trait prediction (with polygenic scores). We suggest a future focus on prediction methods that empirically learn the extent and nature of context dependency by simultaneously considering GxE across many variants.

## Results and discussion

### Modeling context-dependent effect estimation as a bias-variance trade-off

#### The problem setup

We consider a sample of $n+m$ individuals characterized as being in one of two contexts, A or B of the individuals are in context A with the remaining $m$ individuals in context B. We measure a continuous trait for each individual, denoted by

$$
y_{1},…,y_{n}⏞A,y_{n+1},…,y_{n+m}⏞B.
$$

We begin by considering the estimation of the effect of a single variant on the continuous trait. We assume a generative model of the form

$$
y_{i}∼{N(\alpha_{A}+\beta_{A}g_{i},\sigma_{A}^{2})if i\in{1,…,n}N(\alpha_{B}+\beta_{B}g_{i},\sigma_{B}^{2})if i\in{n+1,…,n+m},
$$

where $\beta_{A}$ and $\beta_{B}$ are fixed, context-specific effects of a reference allele at a biallelic, autosomal variant $i$, $g_{i}\in{0,1,2}$ is the observed reference allele count. $\alpha_{A}$ and $\alpha_{B}$ are the context-specific intercepts, corresponding to the mean trait for individuals with zero reference alleles in context $A$ and $B$, respectively. $\sigma_{A}^{2}$ and $\sigma_{B}^{2}$ are context-specific observation variances. We would like to estimate the allelic effects $\beta_{A}$ and $\beta_{B}$.

#### Estimation approaches

We compare two approaches to this estimation problem. The first approach, which we refer to as GxE estimation, is to stratify the sample by context and separately perform an ordinary least squares (OLS) regression in each sample. This approach yields two estimates, $\beta^_{A}$ and $\beta^_{B}$, the OLS estimates of $\beta_{A}$ and $\beta_{B}$ of the generative model in Equation 1, respectively. This estimation model is equivalent to a linear model with a term for the interaction between context and reference allele count, in the sense that context-specific allelic effect estimators have the same maximum likelihood estimators in the two models (see Appendix 1). The second approach, which we refer to as additive estimation, is to perform an OLS regression on the entire sample and use the allelic effect estimate to estimate both $\beta_{A}$ and $\beta_{B}$. We denote this estimator as $\beta^_{A∪B}$, to emphasize that the regression is run on all individuals from context $A$ and context $B$. This estimation model posits that for $i=1,…,n+m$,

$$
y_{i}∼N(\alpha_{A∪B}+\beta_{A∪B}g_{i},\sigma_{A∪B}^{2}),
$$

where $\alpha_{A∪B}$ is the mean trait value for an individual with zero reference alleles, $\beta_{A∪B}$ is the additive allelic effect and $\sigma_{A∪B}^{2}$ is the observation variance which is independent of context. Notably, this model differs from the generative model assumed above: $\beta_{A∪B}$ may not equal $\beta_{A}$ and $\beta_{B}$; in addition, this model ignores heteroskedasticity across contexts.

#### Error analysis

We focus on the mean squared error (MSE) of the additive and GxE estimators for the allelic effect in context $A$. The estimator minimizing the MSE may differ between contexts A and B, but the analysis for context $B$ is analogous. When selecting between these two estimation approaches, a bias-variance decomposition of the MSE is useful. Based on OLS theory (Casella and Berger, 2021, Theorem 11.3.3), under the model specified above, we have

$$
\beta^_{A}∼N(\beta_{A},V_{A}),
$$

where $V_{A}=\frac{\sigma_{A}^{2}}{\sumi=1n(g_{i}−g¯_{A})^{2}}$ and $g¯_{A}$ is the mean genotype of individuals in context $A$. The unbiasedness of the GxE estimator implies

$$
MSE(\beta^_{A},\beta_{A})=V_{A},
$$

where $MSE(\beta^_{A},\beta_{A})$ is the mean squared error of estimating $\beta_{A}$ with $\beta^_{A}$. The case of the additive estimator, $\beta^_{A∪B}$, is a bit more involved. As we show in the Methods section, we can write

$$
\beta^_{A∪B}=\omega_{A}\beta^_{A}+\omega_{B}\beta^_{B}
$$

for non-negative weights $\omega_{A}$ and $\omega_{B}$ (that need not sum to 1). Further, we show in Equation 7 of the Methods section that $\omega_{A}∝nH_{A}$ and $\omega_{B}∝mH_{B}$, where $H_{A}$ and $H_{B}$ are the sample heterozygosities in contexts $A$ and $B$, respectively. Using Equation 3, we may write

$$
MSE(\beta^_{A∪B},\beta_{A})=Bias^{2}(\beta^_{A∪B},\beta_{A})+Var(\beta^_{A∪B})=((\omega_{A}−1)\beta_{A}+\omega_{B}\beta_{B})^{2}+\omega_{A}^{2}V_{A}+\omega_{B}^{2}V_{B},
$$

where $V_{B}$ is defined analogously to $V_{A}$. Thus, with MSE as our metric for comparison, we prefer the GxE estimator in context $A$ when

$$
MSE(\beta^_{A∪B},\beta_{A})>MSE(\beta^_{A},\beta_{A}),
$$

or, if and only if

$$
((\omega_{A}−1)\beta_{A}+\omega_{B}\beta_{B})^{2}+\omega_{A}^{2}V_{A}+\omega_{B}^{2}V_{B}>V_{A}.
$$

We refer to Equation 4 as the ‘decision rule’, since it guides us on the more accurate estimator; to minimize the MSE, we will use the context-specific estimator if and only if the inequality is satisfied. To gain some intuition about the important parameters here, we first consider the case of equal allele frequencies (and hence equal heterozygosities) in both contexts and equal estimation variance in both contexts. In this case, the GxE estimator is advantaged by larger context specificity (larger $|\beta_{A}−\beta_{B}|$) and disadvantaged by larger estimation noise (larger $V_{A}=V_{B}$) (Figure 1). In fact, the decision boundary (i.e. the point at which the two models have equal MSE) can be written as a linear combination of $|\beta_{A}−\beta_{B}|$ and $\sqrt{V_{A}}$ (Figure 1C). In this special case, we show in the Methods section that Equation 4 is an equality when

$$
\sqrt{\frac{m}{2n}}|\beta_{A}−\beta_{B}|−\sqrt{V_{A}}=0.
$$

![Figure 1.](https://cdn.elifesciences.org/articles/99210/elife-99210-fig1-v1.jpg)

**Figure 1.:** The x-axis shows the difference in context-specific effects, while the y-axis shows the standard deviation of the context-specific estimators—both in raw measurement units. The color on the plot indicates the difference between the additive and gene-by-environment interaction (GxE) estimators in bias (A), variance (B), or mean squared error (MSE) (C). (A) Only the additive estimator is potentially biased. The bias is proportional to the difference in context-specific effects and independent of the estimation noise. (B) The difference in variance is proportional to context-specific estimation noise and independent of the difference of context-specific effects. (C) The decision boundary is linear in both the estimation noise and the difference between context-specific effects.

More generally, in the case where $H_{A}=H_{B}$ but $V_{A}\neqV_{B}$, we show in the Methods section that we can write Equation 4 as

$$
\frac{(\beta_{A}−\beta_{B})^{2}}{V_{A}}>\frac{1+\omega_{A}}{1−\omega_{A}}−\frac{V_{B}}{V_{A}}.
$$

This dimensionless re-parameterization of the decision rule makes explicit its dependence on three factors. $\frac{(\beta_{A}−\beta_{B})^{2}}{V_{A}}$ can be viewed as the ‘signal-to-noise’ ratio: it captures the degree of context specificity (the signal) relative to the estimation noise in the focal context, A $\frac{1+\omega_{A}}{1−\omega_{A}}$ is the relative contribution to heterozygosity, which equals the relative contribution to variance in the independent variable of the OLS regression of Equation 2. $\frac{V_{B}}{V_{A}}$ is the ratio of context-specific estimation noises. In Appendix 1, we extend the decision rule for the case of a continuous context variable. For a given trait and context, we can consider the behavior of the decision rule across variants with variable allele frequencies and allelic effects. The ratio of estimation noises, $r:=\frac{V_{A}}{V_{B}}$, will not be constant. However, in some cases, considering a fixed $r$ across variants is a good approximation. In GWAS of complex traits, each variant often explains a small fraction of trait variance. As a result, the estimation noise is effectively a matter of trait variance and heterozygosity alone. If per-site heterozygosity is similar in strata $A$ and $B$, as it is, for example, for autosomal variants in biological males and females, $r$ is approximately fixed across variants (Zhu et al., 2023). Figure 2 illustrates the linearity of the decision boundary under the assumption that $r$ is fixed across variants. It also shows that the slope of the decision boundary changes as a function of $r$. Intuitively, we are less likely to prefer GxE estimation for the noisier context. In fact, for sufficiently small values of $r$ (e.g. $r<\frac{1}{3}$ for $\omega_{A}=\frac{1}{2}$), $\frac{1+\omega_{A}}{1−\omega_{A}}−\frac{V_{B}}{V_{A}}$ will be negative. This corresponds to the situation where $V_{A}≪V_{B}$, in which case the additive estimator is never preferable to the GxE estimator in estimating $\beta_{A}$, as the signal-to-noise ratio is always non-negative. Typically, this will also imply that the additive estimator is greatly preferable for estimating $\beta_{B}$, as $\beta^_{B}$ will be extremely noisy.

![Figure 2.](https://cdn.elifesciences.org/articles/99210/elife-99210-fig2-v1.jpg)

**Figure 2.:** In all panels, the heterozygosity of the variant is assumed to be equal across contexts. The x and y axes are the same as in Figure 1. (A) Estimation noise in the focal context, $A$, is half that of the other context, $B$. (B) Estimation noise is equal in both contexts. (C) Estimation noise in focal context is double that of the other context.

It is natural to ask where the decision rule of Equation 4 falls with respect to empirical GWAS data. We considered the example of biological sex as the context (GxSex), and examined sex-stratified GWAS data across 27 continuous physiological traits in the UK Biobank (Bycroft et al., 2018; Zhu et al., 2023). For each of 9 million variants, we estimated the difference in sex-specific effects and the variance of each marginal effect estimator in males. Then, using an estimate of the ratio of sex-specific trait variances as a proxy for the ratio of estimation variances of males and females, we approximated the linear decision boundary between the additive and GxE estimators (Figure 3A and B; Appendix 1—figure 2, Appendix 1—figure 3). To demonstrate the accuracy of our decision rule, we employed a data-splitting technique where we estimate the MSE difference between estimators in a training set and evaluate the accuracy in a holdout set (Appendix 1—figure 1). For almost all traits examined, very few allelic effects in males are expected to be more accurately estimated using the male-specific estimator (usually between 0% and 0.1%). Notable exceptions to this rule are testosterone, sex hormone binding globulin (SHBG), and waist-to-hip ratio adjusted for body mass index, for which roughly 0.5% of allelic effects are expected to be better estimated with the GxE model (Figure 3B). However, when considering only SNPs that are genome-wide significant in males (marginal p-value $<5\times10^{−8}$ in males), many traits show a much larger proportion of effects that would be better estimated by the GxE model. At an extreme, for testosterone, all genome-wide significant SNPs are expected to be better estimated by the GxE model. In addition, a large fraction of genome-wide significant effects are better estimated with the GxE model for creatinine (62%), arm fat-free mass (24%), waist-to-hip ratio (19%), and SHBG (18%) as well (Figure 3D).

![Figure 3.](https://cdn.elifesciences.org/articles/99210/elife-99210-fig3-v1.jpg)

**Figure 3.:** (A, B) The x-axis shows the estimated absolute difference between the effect of variants in males and females. The y-axis shows the measured standard error for each variant in males, the focal context here. The dashed line shows the decision boundary for effect estimation in males. The difference in mean squared error (MSE) between estimation methods increases linearly with distance from the dashed line, as in Figure 2. If a variant falls above (below) the line, the additive (gene-by-environment interaction [GxE]) estimator has a lower MSE. (A) shows a random sample of 15K single nucleotide variants whereas (B) shows only variants with a marginal p-value less than $5\times10^{−8}$ in males. (C, D) The percent of effects in males which would be better estimated by the GxE estimator, across continuous physiological traits. (Note the difference in scale between the two panels.) To estimate these percentages, one single nucleotide variant is sampled from each of 1700 approximately independent autosomal linkage blocks, and this procedure is repeated 10 times. Shown are average percentages across the 10 iterations.

The decision rule we derived could potentially guide more accurate allelic effect estimation approaches. However, the consideration of GxE pattern sharing across many variants (polygenic GxE) can alter both bias and variance and therefore the trade-off. In our discussion of complex traits that follows, we therefore expand on the rule through qualitative consequences of polygenic GxE, and no longer stick to the analytical single variant rule.

### Context dependency in complex traits

At the single variant level, and specifically when variants are considered independently from one another, we have discussed how the accurate estimation of allelic effects can be boiled down to a bias-variance trade-off. For complex traits, genetic variance is often dominated by the contribution of numerous variants of small effects that are best understood when analyzed jointly (Sella and Barton, 2019; Sinnott-Armstrong et al., 2021; Shi et al., 2016; Boyle et al., 2017; Liu et al., 2019; Wray et al., 2018; Yengo et al., 2022). It stands to reason that to evaluate context dependence in complex traits, we would also want to jointly consider polygenic patterns, rather than just the patterns at the loci most strongly associated with a trait (Urbut et al., 2019; Gibson and Lacek, 2020; Zhang et al., 2021; Paaby and Gibson, 2016; Aschard et al., 2017; Des Marais et al., 2013). Motivated by this rationale, we recently inferred polygenic GxSex patterns in human physiology (Zhu et al., 2023). One pattern that emerged as a common mode of GxSex across complex physiological traits is ‘amplification’: a systematic difference in the magnitude of genetic effects between the sexes. Moving beyond sex and considering any context, amplification can happen if, for example, many variants regulate a shared pathway that is moderated by a factor—and that factor varies in its distribution among contexts. Amplification is but one possible mode of polygenic GxE, but can serve as a guiding example for ways in which GxE may be pervasive but difficult to characterize with existing approaches (Zhu et al., 2023; Gibson and Dworkin, 2004; Miao et al., 2022; Balliu et al., 2021). In what follows, we will therefore use the example of pervasive amplification (across causal effects) to illustrate the interpretive advantage of considering context dependency across variants jointly, rather than independently.

#### A focus on ‘top hits’ may lead to mischaracterization of polygenic GxE

A common approach to the analysis of context dependency involves two steps. First, categorization of context dependency (or lack thereof) is performed for each variant independently. Second, variants falling under each category are counted and annotated across the genome. Some recent examples of this approach toward the characterization of GxE in complex traits include studies of GxSex effects on flight performance in Drosophila (Spierer et al., 2021), GxSex effects on various traits in humans (Traglia et al., 2022; Bernabeu et al., 2021), and GxDietxAge effects on body weight in mice (Wright et al., 2022). Characterizing polygenic trends by summarizing many independent hypothesis tests may miss GxE signals that are subtle and statistically undetectable at each individual variant, yet pervasive and substantial cumulatively across the genome. To characterize polygenic GxE based on just the ‘top hits’ may lead to ascertainment biases, with respect to both the pervasiveness and the mode of GxE across the genome. Much like the heritability of complex traits is thought to be due to the contribution of many small (typically sub-significant) effects (Boyle et al., 2017; Sinnott-Armstrong et al., 2021), when GxE is pervasive we may expect that the sum of many small differences in context-specific effects accounts for the majority of GxE variation. For concreteness, we consider in more depth one recent study characterizing GxDiet effects on longevity in Drosophila melanogaster (Pallares et al., 2023). In this study, Pallares et al. tracked caged fly populations given one of two diets: a ‘control’ diet and a ‘high-sugar’ diet. Across 271K single nucleotide variants, the authors tested for association between alleles and their survival to a sampling point (thought of as a proxy for ‘lifespan’ or ‘longevity’) under each diet independently. Then, they classified variants according to whether or not their associations with survivorship were significant under each diet as follows:

This authors’ choice of four categories a variant may fall into may be motivated by the wish to test for the presence of ‘cryptic genetic variation’—genetic variation that is maintained in a context where it is functionally neutral but carries large effects in a new or stressful context (Gibson and Dworkin, 2004; Paaby and Rockman, 2014; Young et al., 2016; Des Marais et al., 2013). Indeed, of the variants Pallares et al. classified as having an effect (one-hundredth of variants tested), approximately 31% were high-sugar specific, while the remaining 69% of the variants were shared. Fewer than 1% were labeled as having control-specific effects. They concluded that high-sugar-specific effects on longevity are pervasive, compatible with the hypothesis of widespread cryptic genetic variation for longevity. This characterization of GxE, based on ‘top hits’, places an emphasis on the context(s) in which trait associations are statistically significant, rather than on estimating how the context-specific effects covary. In addition, this particular classification system also does not cover all possible ways in which context-specific effects may differ. In Appendix 1, we discuss these interpretation difficulties further.

We next show that a generative model that differs qualitatively from the cryptic genetic variation model yields results that are highly similar to those observed by Pallares et al. We simulated data under pervasive amplification. Specifically, we sampled from a mixture of 40% of variants having no effect under either diet and 60% of variants having an effect under both diets—but exactly 1.4× larger under a high-sugar diet. We then simulated the noisy estimation of these effects and employed the classification approach of Pallares et al. to the simulated data (Methods). The patterns of allelic effects in the control compared to high-sugar contexts were qualitatively similar in the experimental data and our pervasive amplification simulation. This is true both genome-wide (Figure 4A compared to Figure 4B) and for the set of variants classified as significant with their classification approach (Figure 4C compared to Figure 4D). The similarity of ascertained variants further highlights caveats of interpretation based on the classification of ‘top hits’: despite the fact that we did not simulate any variants that only have an effect under the high-sugar diet, approximately 36% of significant variants were classified as specific to the high-sugar diet (green points in Figure 4D), comparable to the 31% of variants classified as high-sugar specific in the experimental data (Figure 4C). These variants simply have sub-significant associations in the control group and significant associations in the high-sugar group. In addition, every variant in the shared category (blue points in Figure 4D) in fact has a larger effect in the high-sugar diet than in the control diet, which cannot be captured by the classification system itself but represents the only mode of GxE in our simulation.

![Figure 4.](https://cdn.elifesciences.org/articles/99210/elife-99210-fig4-v1.jpg)

**Figure 4.:** (A) Data from an experiment measuring allelic effects on longevity in caged flies given one of two diets, ‘control’ and ‘high sugar’. Shown are allelic effect estimates under each diet for a random sample of approximately 12K variants. (B) Simulated data where all true allelic effects are exactly 1.4 times larger under a high-sugar diet. The effects are estimated with sampling noise mimicking the Pallares et al. data. (C) Allelic effect estimates of variants ascertained as significant and classified as ‘diet-specific’ or ‘shared’ by Pallares et al. (D) Simulated effects ascertained as significant and classified using a similar procedure to that applied in (C). While the generative mode of GxE we used in our simulations was not considered by Pallares et al., the simulation results (left panels) closely match the patterns observed in their data (right panels) across all effects (top panels) and as reflected via their classification approach (bottom panels).

To recap, we simulated a mode of GxE that is not considered in Pallares et al. (i.e. pervasive amplification) and that is at odds with their conclusions about evidence for a large discrete class of SNPs with diet-specific effects (i.e. cryptic genetic variation). The close match of our simulation to the empirical results of Pallares et al. therefore illustrates that the characterization of GxE via hypothesis testing and classification at each variant independently may lead to erroneous interpretation when applied to empirical complex trait data as well. In Appendix 1, we show that a reanalysis of the Pallares et al. data that is based on estimating the covariance of allelic effects is directly consistent with pervasive amplification as well (Appendix 1—figure 4). In conclusion, the classification of ‘top hits’ alone may not be representative of the extent of GxE nor of the most pervasive modes of GxE.

#### The utility of modeling GxE for complex trait prediction

Modeling context dependency of genetic effects may hold the potential for constructing polygenic scores that are more accurate or improve their portability across contexts (Patel et al., 2022; Miao et al., 2022; Turley et al., 2018; Spence et al., 2022; Wang et al., 2024; Smith et al., 2025). Evidence for the utility of GxE models in polygenic score prediction, however, has been underwhelming and GxE models are still rarely applied (Zhu et al., 2023; Schwaba et al., 2023). A key reason behind this apparent discrepancy is the bias-variance trade-off for individual variants discussed above. If context-specific effects are similar—a likely possibility for highly polygenic traits with the majority of heritability owing to small causal effects—then additive models will tend to outperform (Fisher, 1930; Falconer and Mackay, 1996; Hill et al., 2008; Young, 2019). This is because the unbiasedness of GxE estimation does not make up for the cost of additional estimator variance, resulting from sample stratification by context or the addition of explicit interaction terms (Schwaba et al., 2023). We exemplify the relative importance of variance compared to bias in polygenic scoring using simulations. We continue with the generative model of pervasive amplification as an example. Namely, we simulated a GWAS of a continuous trait with independent effects in 2500 variants (50% of variants included in the GWAS). Effects were either the same in two contexts, $A$ and $B$, or $1.4$ times larger in context $B$. The GWAS is conducted with either a small sample size or a large sample size, conferring low or high statistical power, respectively. We then constructed polygenic scores using 833 variants (corresponding to one-third of the causal variants), which were ascertained as most significantly associated with the trait according to either the additive model (orange and red in Figure 5) in or context-specific hypothesis tests (green and blue in Figure 5).

![Figure 5.](https://cdn.elifesciences.org/articles/99210/elife-99210-fig5-v1.jpg)

**Figure 5.:** In each simulation, a genome-wide association study (GWAS) is performed on 5000 biallelic variants, half of which have no effect in either context. Of the other half, some percent of the variants (indicated on the x-axis) had effects 1.4× larger in one of contexts and the remaining SNPs had equal effects in both contexts. The broad sense heritability was set to $0.4$ in all simulations. The y-axis shows the average, over $11,000$ simulations, of the out-of-sample Pearson correlation between polygenic score and trait value. (A) Results with a GWAS sample size of 1000 individuals. (B) Results with a GWAS size of $50,000$ individuals.

Even in settings with pervasive GxE, additive polygenic scores (red lines in Figure 5) outperformed context-specific scores (green lines in Figure 5). The advantage of the additive model is manifested in two ways: more accurate estimation, as discussed above, but also better identification of true associations with the trait. We considered the two advantages separately. It is sometimes better to ascertain variants using the lower variance approach and estimate effects using the lower-bias approach. In our simulations, this strategy (orange lines in Figure 5) was preferable to using the GxE model for both ascertainment and estimation (green line). It was not preferable to using the additive model (red line) for both approaches, but it was the preferable strategy under a slightly different parametric regime, corresponding to more GxE (Appendix 1—figure 5). Finally, we considered a polygenic GxE approach, as implemented in ‘multivariate adaptive shrinkage’ (mash) (Urbut et al., 2019), a method to estimate context-specific effects by leveraging common patterns of effect covariance between contexts observed across the genome. mash models the underlying distribution of effects in all contexts as a mixture of zero-centered multivariate normal distributions with different covariance structures (as well as the null matrix, to induce additional shrinkage). After estimating this distribution via maximum likelihood, mash uses it as a prior to obtain posterior effect estimates for each variant in each context. As a result, posterior effect estimates across contexts regress toward commonly observed patterns of covariance of allelic effects across contexts. In our simulations, in the presence of substantial amplification, the polygenic adaptive shrinkage approach outperformed all other methods as long as the study was adequately powered (Figure 5B). This is thanks to the unique ability (compared to the three other approaches) to leverage the sharing of signals across variants, including the extent and nature of context dependency. With low power, however, the additive model performed best (Figure 5A). We attribute this to the variance cost associated with the polygenic adaptive shrinkage approach—driven by the estimation of additional parameters for capturing the genome-wide covariance relationships.

### Conclusion

When genetic variants are considered independently, the estimation of their effects in different contexts can be boiled down to a bias-variance trade-off. For complex traits, we show through example that further considering polygenic patterns of GxE can be key for understanding context-dependent genetic architecture and to aid in prediction. The notion that complex trait analyses should combine observations at top associated loci alongside polygenic trends has gained traction with additive models of trait variation; it may be similarly important in our understanding of context dependency.

## Methods

### Expressing the additive estimator as a linear combination of GxE estimators

In this section, we prove the result of Equation 3, stating that

$$
\beta^_{A∪B}=\omega_{A}\beta^_{A}+\omega_{B}\beta^_{B}
$$

for some non-negative weights $\omega_{A}$ and $\omega_{B}$. To do this, we will need some additional notation. Let $g¯_{A}$ denote the average number of effect alleles in individuals in context $A$, and let $g¯_{A∪B}$ denote the average effect allele count across all individuals. Similarly, let $y¯_{A}$ denote the average trait value in context $A$, and let $y¯_{A∪B}$ denote the average trait value across all individuals. As an OLS estimator, the context-specific estimator is defined as

$$
\beta^_{A}=\frac{\sumi=1n(g_{i}−g¯_{A})(y_{i}−y¯_{A})}{\sumi=1n(g_{i}−g¯_{A})^{2}}=\frac{\sumi=1n(g_{i}−g¯_{A})y_{i}−\sumi=1n(g_{i}−g¯_{A})y¯_{A}}{\sumi=1n(g_{i}−g¯_{A})^{2}}=\frac{\sumi=1n(g_{i}−g¯_{A})y_{i}−y¯_{A}\sumi=1n(g_{i}−g¯_{A})}{\sumi=1n(g_{i}−g¯_{A})^{2}}=\frac{\sumi=1n(g_{i}−g¯_{A})y_{i}}{\sumi=1n(g_{i}−g¯_{A})^{2}}, since \sumi=1n(g_{i}−g¯_{A})=0.
$$

Similarly, the additive estimator can be written as

$$
\beta^_{A∪B}=\frac{\sumi=1n+m(g_{i}−g¯_{A∪B})(y_{i}−y¯_{A∪B})}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}=\frac{\sumi=1n+m(g_{i}−g¯_{A∪B})y_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}} (by the same logic as above)=\frac{\sumi=1n(g_{i}−g¯_{A∪B})y_{i}+\sumi=n+1n+m(g_{i}−g¯_{A∪B})y_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}.
$$

We will show that the weights in Equation 3 depend on the effect allele frequency in the two contexts, $f_{A}$ and $f_{B}$. We will assume mean-centered traits, such that $\sumi=1ny_{i}=0$ and $\sumi=n+1n+my_{i}=0$. We note that mean-centering is inconsequential for effect estimation. We can then write

$$
\beta^_{A∪B}=\frac{\sumi=1n(g_{i}−g¯_{A∪B})y_{i}+\sumi=n+1n+m(g_{i}−g¯_{A∪B})y_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}=\frac{\sumi=1n(g_{i}−g¯_{A∪B})y_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}+\frac{\sumi=n+1n+m(g_{i}−g¯_{A∪B})y_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}=\frac{\sumi=1n(g_{i}−g¯_{A}+(g¯_{A}−g¯_{A∪B}))y_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}+\frac{\sumi=n+1n+m(g_{i}−g¯_{B}+(g¯_{B}−g¯_{A∪B}))y_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}=\frac{\sumi=1n(g_{i}−g¯_{A})y_{i}+\sumi=1n(g¯_{A}−g¯_{A∪B})y_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}+\frac{\sumi=n+1n+m(g_{i}−g¯_{B})y_{i}+\sumi=n+1n+m(g¯_{B}−g¯_{A∪B})y_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}=\frac{\sumi=1n(g_{i}−g¯_{A})y_{i}+(g¯_{A}−g¯_{A∪B})\sumi=1ny_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}+\frac{\sumi=n+1n+m(g_{i}−g¯_{B})y_{i}+(g¯_{B}−g¯_{A∪B})\sumi=n+1n+my_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}=\frac{\sumi=1n(g_{i}−g¯_{A})y_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}+\frac{\sumi=n+1n+m(g_{i}−g¯_{B})y_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}} (by our assumption of mean centered traits)=\frac{\sumi=1n(g_{i}−g¯_{A})y_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}⋅\frac{\sumi=1n(g_{i}−g¯_{A})^{2}}{\sumi=1n(g_{i}−g¯_{A})^{2}}+\frac{\sumi=n+1n+m(g_{i}−g¯_{B})y_{i}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}⋅\frac{\sumi=n+1n+m(g_{i}−g¯_{B})^{2}}{\sumi=n+1n+m(g_{i}−g¯_{B})^{2}}=\frac{\sumi=1n(g_{i}−g¯_{A})y_{i}}{\sumi=1n(g_{i}−g¯_{A})^{2}}⋅\frac{\sumi=1n(g_{i}−g¯_{A})^{2}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}+\frac{\sumi=n+1n+m(g_{i}−g¯_{B})y_{i}}{\sumi=n+1n+m(g_{i}−g¯_{B})^{2}}⋅\frac{\sumi=n+1n+m(g_{i}−g¯_{B})^{2}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}=\frac{\sumi=1n(g_{i}−g¯_{A})^{2}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}\beta^_{A}+\frac{\sumi=n+1n+m(g_{i}−g¯_{B})^{2}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}\beta^_{B}.
$$

Thus, $\omega_{A}=\frac{\sumi=1n(g_{i}−g¯_{A})^{2}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}$ and $\omega_{B}=\frac{\sumi=n+1n+m(g_{i}−g¯_{B})^{2}}{\sumi=1n+m(g_{i}−g¯_{A∪B})^{2}}$ in Equation 3. We note that the numerator of $\omega_{A}$ is $n$ times the sample heterozygosity in context A, and the numerator of $\omega_{B}$ is $m$ times the sample heterozygosity in context B. Thus, we have shown that

$$
\omega_{A}∝nH_{A} and \omega_{B}∝mH_{B},
$$

where $H_{A}$ and $H_{B}$ are the sample heterozygosities in context A and B, respectively. And, in the special case where $f_{A}=f_{B}$, because this implies that the sample heterozygosities will be approximately equal across contexts, we have that

$$
\omega_{A}∝nH_{A} and \omega_{B}∝mH_{B}.
$$

### Linearity of the decision rule

In Equation 5, under the assumption that $V_{A}=V_{B}$ and $H_{A}=H_{B}$, the decision boundary is expressed as a linear function of $|\beta_{A}−\beta_{B}|$ and $\sqrt{V_{A}}$ as

$$
\sqrt{\frac{m}{2n}}|\beta_{A}−\beta_{B}|>\sqrt{V_{A}}.
$$

Here, we prove that the linearity of the decision rule holds in the more general case where $\frac{V_{A}}{V_{B}}=r$ for some fixed value of $r$. Equation 5 then follows as a special case of this fact when $r=1$. Starting from Equation 4, we prefer the GxE estimator to the additive estimator when estimating $\beta_{A}$ if

$$
V_{A}<\omega_{A}^{2}V_{A}+\omega_{B}^{2}V_{B}+((\omega_{A}−1)\beta_{A}+\omega_{B}\beta_{B})^{2}⟺V_{A}<\omega_{A}^{2}V_{A}+\frac{\omega_{B}^{2}}{r}V_{A}+((\omega_{A}−1)\beta_{A}+\omega_{B}\beta_{B})^{2}⟺V_{A}−\omega_{A}^{2}V_{A}−\frac{\omega_{B}^{2}}{r}V_{A}<((\omega_{A}−1)\beta_{A}+\omega_{B}\beta_{B})^{2}⟺(1−\omega_{A}^{2}−\frac{\omega_{B}^{2}}{r})V_{A}<((\omega_{A}−1)\beta_{A}+\omega_{B}\beta_{B})^{2}⟺V_{A}<\frac{((\omega_{A}−1)\beta_{A}+\omega_{B}\beta_{B})^{2}}{1−\omega_{A}^{2}−\frac{\omega_{B}^{2}}{r}} (assuming 1−\omega_{A}^{2}−\frac{\omega_{B}^{2}}{r}>0)⟺\sqrt{V_{A}}<\frac{|(\omega_{A}−1)\beta_{A}+\omega_{B}\beta_{B}|}{\sqrt{1−\omega_{A}^{2}−\frac{\omega_{B}^{2}}{r}}} (again assuming 1−\omega_{A}^{2}−\frac{\omega_{B}^{2}}{r}>0)
$$

If our assumption that $1−\omega_{A}^{2}−\frac{\omega_{B}^{2}}{r}>0$ does not hold, we note that the GxE model is always preferable and technically speaking there exists no decision rule between the two models. Now, when heterozygosities (and thus minor allele frequencies) are equal across contexts, then Equation 8 implies $\omega_{A}+\omega_{B}=1$. Therefore, we may write the decision rule as

$$
\sqrt{V_{A}}<\frac{|(1−\omega_{B}−1)\beta_{A}+\omega_{B}\beta_{B}|}{\sqrt{1−\omega_{A}^{2}−\frac{\omega_{B}^{2}}{r}}}⟺\sqrt{V_{A}}<\frac{|\omega_{B}(\beta_{B}−\beta_{A})|}{\sqrt{1−\omega_{A}^{2}−\frac{\omega_{B}^{2}}{r}}}⟺\sqrt{V_{A}}<\frac{\omega_{B}}{\sqrt{1−\omega_{A}^{2}−\frac{\omega_{B}^{2}}{r}}}|\beta_{A}−\beta_{B}| (by properties of the absolute value)⟺\sqrt{V_{A}}<\frac{1−\omega_{A}}{\sqrt{1−\omega_{A}^{2}−\frac{(1−\omega_{A})^{2}}{r}}}|\beta_{A}−\beta_{B}|.
$$

Here, we see that for any fixed $r$ the decision rule is linear with a slope determined by $r$ (Figure 2). Now, in the special case where $r=1$, we have

$$
\sqrt{V_{A}}<\frac{1−\omega_{A}}{\sqrt{1−\omega_{A}^{2}−(1−\omega_{A})^{2}}}|\beta_{A}−\beta_{B}|⟺\sqrt{V_{A}}<\frac{1−\omega_{A}}{\sqrt{1−\omega_{A}^{2}−1−\omega_{A}^{2}+2\omega_{A}}}|\beta_{A}−\beta_{B}|⟺\sqrt{V_{A}}<\frac{1−\omega_{A}}{\sqrt{2\omega_{A}(1−\omega_{A})}}|\beta_{A}−\beta_{B}|⟺\sqrt{V_{A}}<\sqrt{\frac{1−\omega_{A}}{2\omega_{A}}}|\beta_{A}−\beta_{B}|
$$

Now, substituting the definitions of $\omega_{A}$ and $\omega_{B}$ in the case of equal minor allele frequencies given in Equation 8, we can write

$$
\sqrt{V_{A}}<\sqrt{\frac{1}{2}}\sqrt{\frac{1−\frac{n}{n+m}}{\frac{n}{n+m}}}|\beta_{A}−\beta_{B}|⟺\sqrt{V_{A}}<\sqrt{\frac{1}{2}}\sqrt{\frac{\frac{m}{n+m}}{\frac{n}{n+m}}}|\beta_{A}−\beta_{B}|⟺\sqrt{V_{A}}<\sqrt{\frac{m}{2n}}|\beta_{A}−\beta_{B}|.
$$

This inequality is instead an equality under the conditions stated in Equation 5. Finally, again using the definition of $\omega_{A}$ and $\omega_{B}$ given in Equation 8, we note that our assumption that $1−\omega_{A}^{2}−\frac{\omega_{B}^{2}}{r}>0$ will always hold in the case of equal minor allele frequencies and $r=1$, as

$$
1−\omega_{A}^{2}−\frac{\omega_{B}^{2}}{r}=1−\frac{n^{2}}{(n+m)^{2}}−\frac{m^{2}}{(n+m)^{2}}=\frac{(n+m)^{2}−n^{2}−m^{2}}{(n+m)^{2}}=\frac{2nm}{(n+m)^{2}},
$$

which is strictly positive.

### Re-parameterized decision rule in terms of unitless quantities

In Equation 6, under the assumption that $H_{A}=H_{B}$, we re-state the decision rule in terms of the signal-to-noise ratio. Here, we prove this result. From Equation 4, we have that we should select the GxE model to estimate $\beta_{A}$ if and only if

$$
V_{A}<\omega_{A}^{2}V_{A}+\omega_{B}^{2}V_{B}+((\omega_{A}−1)\beta_{A}+\omega_{B}\beta_{B})^{2}⟺1<\omega_{A}^{2}+\omega_{B}^{2}\frac{V_{B}}{V_{A}}+\frac{((\omega_{A}−1)\beta_{A}+\omega_{B}\beta_{B})^{2}}{V_{A}}⟺1−\omega_{A}^{2}<\omega_{B}^{2}\frac{V_{B}}{V_{A}}+\frac{((\omega_{A}−1)\beta_{A}+\omega_{B}\beta_{B})^{2}}{V_{A}}.
$$

Now, because $H_{A}=H_{B}$, we know by Equation 8 that $\omega_{A}+\omega_{B}=1$. Then, we may write the decision rule as

$$
1−\omega_{A}^{2}<\omega_{B}^{2}\frac{V_{B}}{V_{A}}+\frac{((1−\omega_{B}−1)\beta_{A}+\omega_{B}\beta_{B})^{2}}{V_{A}}⟺1−\omega_{A}^{2}<\omega_{B}^{2}\frac{V_{B}}{V_{A}}+\frac{(\omega_{B}(\beta_{B}−\beta_{A}))^{2}}{V_{A}}⟺1−\omega_{A}^{2}<\omega_{B}^{2}\frac{V_{B}}{V_{A}}+\omega_{B}^{2}\frac{(\beta_{A}−\beta_{B})^{2}}{V_{A}}⟺\frac{1−\omega_{A}^{2}}{\omega_{B}^{2}}<\frac{V_{B}}{V_{A}}+\frac{(\beta_{A}−\beta_{B})^{2}}{V_{A}}⟺\frac{1−\omega_{A}^{2}}{(1−\omega_{A})^{2}}<\frac{V_{B}}{V_{A}}+\frac{(\beta_{A}−\beta_{B})^{2}}{V_{A}}⟺\frac{1−\omega_{A}^{2}}{(1−\omega_{A})^{2}}−\frac{V_{B}}{V_{A}}<\frac{(\beta_{A}−\beta_{B})^{2}}{V_{A}}⟺\frac{(1−\omega_{A})(1+\omega_{A})}{(1−\omega_{A})^{2}}−\frac{V_{B}}{V_{A}}<\frac{(\beta_{A}−\beta_{B})^{2}}{V_{A}}⟺\frac{1+\omega_{A}}{1−\omega_{A}}−\frac{V_{B}}{V_{A}}<\frac{(\beta_{A}−\beta_{B})^{2}}{V_{A}}
$$

as is stated in Equation 6.

### Simulation of GxDiet effects on longevity in Drosophila

In Figure 4, we compare the effect estimates of Pallares et al. to ones we got in simulations of pervasive amplification. Here, we detail the simulation approach. We first generated true effects under each diet. For variants $j=1,…,50,000$, we sampled a true effect under the high-sugar diet ($\beta_{h_{j}}$) and under the control diet ($\beta_{c_{j}}$). A random 60% of variants were set to have no effect under either diet, with the effects of the remaining 40% of variants sampled as

$$
[\beta_{c_{j}}\beta_{h_{j}}]∼N([−0.125−0.15],0.01⋅[11.41.41.96]).
$$

This corresponds to a systematic amplification of $1.4\times$ in the high-sugar compared to the control diet. We selected these parameters based on inspection of the resulting distribution of effects and their correspondence to the Pallares et al. data. We then simulated the effect estimation. For each variant, the effect estimate was simulated as normally distributed with mean equal to the true effect and standard deviation equal to a randomly sampled (with replacement) standard error from the effect estimates of Pallares et al. That is, given the simulated values of the true effect estimates $\beta_{c_{j}}$ and $\beta_{h_{j}}$, we simulated effect estimates as

$$
[\beta^_{c_{j}}\beta^_{h_{j}}]∼N([\beta_{c_{j}}\beta_{h_{j}}],[s^_{c_{k}}^{2}00s^_{h_{k}}^{2}]),
$$

where $k$ represents the index of a randomly selected variant from the empirical data of Pallares et al. and $s^_{c_{k}}$ and $s^_{h_{k}}$ are the corresponding estimated standard errors for the effect estimates in the control and high-sugar groups, respectively. This process yielded vectors of estimated effects in the high-sugar group and control group, $\beta^_{h}$ and $\beta^_{c}$, respectively, and vectors of estimated standard errors in the high-sugar group and control group, $s^_{h}$ and $s^_{c}$, respectively. We then performed a Z-test for each variant under each diet, yielding two vectors of p-values, $p_{h}$ and $p_{c}$, corresponding to the high-sugar and control diets, respectively. Using these p-values, we followed a similar approach to Pallares et al. to classify the variants (Figure 4D). First, as in Pallares et al., we computed q-values separately for each diet (Storey, 2003), yielding $q_{h}$ and $q_{c}$, corresponding to the q-values of non-zero effects in the high-sugar and control diets, respectively. Then, we employed the following classification scheme for each variant $j=1,…,50,000$:

We note that p-value and q-value cutoffs used are nominally different than those used in the Pallares et al. study.

### Polygenic score simulations

In Figure 5, we show the results of multiple simulations where we compute polygenic scores in each of two contexts under amplification. Here, we detail the generation of data in the simulations and the methods for constructing polygenic scores. As in Results and discussion, we assumed that we have $n+m$ observations of a continuous trait, where the first $n$ individuals are observed in context $A$ and the final $m$ are observed in context $B$. For convenience, in this case we assumed $n=m$. Now, for variants $j=1,…,p$ we generated true effects in contexts $A$ and $B$ independently from the mixture model

$$
[\beta_{A_{j}}\beta_{B_{j}}]∼\pi_{0}\delta_{0}+(1−\pi_{0})(\alphaN([00],[1111]))+(1−\alpha)N([00],[\frac{3}{2}11\frac{2}{3}])),
$$

where $\pi_{0}$ (which we set to $0.5$) represents the proportion of SNPs with null effects in both contexts, $\alpha$ represents the proportion of non-null SNPs which have exactly equal effects in both contexts, and $1−\alpha$ is the proportion of non-null SNPs which are generated as perfectly correlated but with $1.5\times$ the standard deviation in context A. Let $\beta→_{A}$ and $\beta→_{B}$ represent the resulting p-vectors of true effects for contexts $A$ and $B$, respectively. Next, we generated genotype counts for each of the $n+m$ individuals at all $p$ variants. Specifically, we independently generated genotypes as

$$
f_{j}∼\frac{1}{2}Beta(s_{1},s_{2}) for j=1,…,p
$$



$$
g_{ij}∼Binomial(2,f_{j}) for i=1,…,n+m,
$$

where $f_{j}$ is the minor allele frequency at variant $j$ in the population, $s_{1}$ and $s_{2}$ are parameters controlling the distribution of minor allele frequencies in the population, and $g_{ij}$ is the observed genotype for individual $i$ at variant $j$. Here, we set $s_{1}=1$ and $s_{2}=5$. Let $G_{A}$ and $G_{B}$ represent the generated $n\timesp$ matrices of genotypes in contexts A and B, respectively. Finally, we generated the observed continuous traits for context A ($y→_{A}$) and context B ($y→_{B}$) as $y→_{A}∼N(G_{A}\beta→_{A},\sigma_{A}^{2}I_{n})$$y→_{B}∼N(G_{B}\beta→_{B},\sigma_{B}^{2}I_{m}),$

$$
y→A∼N(G_{A}\beta→_{A},\sigma_{A}^{2}I_{n})y→B∼N(G_{B}\beta→_{B},\sigma_{B}^{2}I_{m}),
$$

where $\sigma_{A}^{2}$ and $\sigma_{B}^{2}$ are the observation variances in contexts A and B, respectively, and $I_{w}$ is the $w\timesw$ identity matrix. In our simulations, we set $\sigma_{A}^{2}$ and $\sigma_{B}^{2}$ such that the narrow sense heritability is 40% in each context. So that we may later test the accuracy of our polygenic scores, we generated both a training set (consisting of $n$ individuals in each context, where n=1000 in the low power simulation and $n=50,000$ in the high power simulation) for effect estimation and a test set (consisting of 3000 individuals in each context) using the above distributions. Figure 5 compares four distinct approaches for constructing polygenic scores, derived from three allelic effect estimation approaches: additive estimation with shrinkage, GxE estimation with shrinkage, and mash. First, the additive and GxE estimates are derived independently for each variant as described in Results and discussion. Let $\beta^_{A}$ and $\beta^_{B}$ be the p-vectors of GxE estimates of effects in context $A$ and $B$, respectively. Similarly, let $s^_{A}$ and $s^_{B}$ be the p-vectors of the standard errors of GxE estimates of effects in context A and B, respectively. Finally, let $\beta^_{A∪B}$ be the p-vector of estimated effects from the additive model and $s^_{A∪B}$ be the p-vector of standard errors of estimated effects from the additive model. Using the GxE estimates, we also constructed estimates of the effects in each context using mash. Specifically, we ran mash on the $n\times2$ matrices $[\beta^_{A}\beta^_{B}]$ (of effects) and $[s^_{A}s^_{B}]$ (of standard errors). mash then yields $p(\beta→_{A}|\beta^_{A},s^_{A})$ and $p(\beta→_{B}|\beta^_{B},s^_{B})$, the posterior distributions of the effects in contexts $A$ and $B$, respectively. To construct each polygenic score, we made two choices. First, a choice between the three sets of p-values (or pseudo p-values, see below) for thresholding—we include the 833 (corresponding to one-third of the causal variants) most significant variants in the polygenic score. The second choice was between the three sets of effect estimates to be used as weights in the polygenic score (Figure 5). For instance, when the GxE model was used for ascertainment, we selected the set of variants $Ω_{A}⊂{1,…,p}$ consisting of the variants with the 833 smallest p-values and $Ω_{B}⊂{1,…,p}$ consisting of the variants with the 833 smallest p-values (derived from $\beta^_{B}$ and $s^_{B}$). Then, we predicted trait values (out of sample) by multiplying the effect estimates of our chosen ‘estimation method’ (for mash we use the posterior mean) by the effect allele count at each of the selected variants for the individual in question.
