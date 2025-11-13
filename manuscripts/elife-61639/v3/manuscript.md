# Early life imprints the hierarchy of T cell clone sizes

## Authors

- Mario U Gaimann<sup>1</sup> ([ORCID: 0000-0002-2789-090X](https://orcid.org/0000-0002-2789-090X))
- Maximilian Nguyen<sup>1</sup> ([ORCID: 0000-0002-4378-5050](https://orcid.org/0000-0002-4378-5050))
- Jonathan Desponds<sup>3</sup> ([ORCID: 0000-0001-7112-3217](https://orcid.org/0000-0001-7112-3217))
- Andreas Mayer<sup>1</sup> ([ORCID: 0000-0002-6643-7622](https://orcid.org/0000-0002-6643-7622)) †

### Affiliations

1. Lewis-Sigler Institute for Integrative Genomics, Princeton University Princeton United States
2. Arnold Sommerfeld Center for Theoretical Physics and Center for NanoScience, Department of Physics, Ludwig-Maximilians-Universität München München Germany
3. NSF-Simons Center for Quantitative Biology, Northwestern University Evanston United States

† Corresponding author

## Abstract

The adaptive immune system responds to pathogens by selecting clones of cells with specific receptors. While clonal selection in response to particular antigens has been studied in detail, it is unknown how a lifetime of exposures to many antigens collectively shape the immune repertoire. Here, using mathematical modeling and statistical analyses of T cell receptor sequencing data, we develop a quantitative theory of human T cell dynamics compatible with the statistical laws of repertoire organization. We find that clonal expansions during a perinatal time window leave a long-lasting imprint on the human T cell repertoire, which is only slowly reshaped by fluctuating clonal selection during adult life. Our work provides a mechanism for how early clonal dynamics imprint the hierarchy of T cell clone sizes with implications for pathogen defense and autoimmunity.

## Introduction

The hallmark of adaptive immunity is the generation of diversity through genetic recombination and clonal selection. Their interplay balances the breadth and specificity of the ~1012 T cells in the human body (Figure 1A; Arstila et al., 1999; Farber et al., 2014): The genetic recombination of the T cell receptor (TCR) locus, termed VDJ recombination, generates an enormous potential diversity of receptors ranging from early estimates of ~1015 (Davis and Bjorkman, 1988) to more recent estimates of ~1061 (Mora and Walczak, 2016) different possible receptor TCRαβ heterodimers. Clonal selection expands the number of specific cells during an infection for effector functions, a fraction of which is retained over prolonged periods of time as immune memory (Ahmed and Gray, 1996; Farber et al., 2014).

![Figure 1.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig1-v3.jpg)

**Figure 1.:** (A) T cells with highly diverse receptors are created from progenitor cells through genetic recombination (left), which then undergo clonal selection (middle) together shaping the immune repertoire. The T cell receptor (TCR) locus acts as a natural barcode for clonal lineages, which can be read out by sequencing (right). (B, C) Clone size distributions in two large cohort studies of human blood samples using disparate sequencing protocols display a power-law relationship between the rank and size of the largest clones. Each line shows the size distribution of all T cell clones in an individual in an unsorted blood sample, that is independently of the phenotypes of the cells making up the different clones. Ages are color coded as indicated in the legend. The black line shows a power law with a slope of -1 for visual comparison. Normalized clone sizes were defined as the number of reads of a given receptor’s sequence divided by the total number of reads within a sample and a factor equal to the average fraction of T cells with memory phenotype at different ages to account for variations in sampling depth and in the subset composition of peripheral blood, respectively (Figure 1—figure supplement 3). Only a single individual is displayed per 2-year age bracket to improve visibility. (D) Power-law exponents as a function of the age (legend: linear regression slope and coefficient of determination). Data sources: Britanova et al., 2016, Emerson et al., 2017.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig1-figsupp1-v3.jpg)

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig1-figsupp2-v3.jpg)

**Figure 1—figure supplement 2.:** (A) The naive cell fraction as determined by flow cytometry and the fraction of singletons are closely correlated in the Britanova cohort. To diminish the influence of sampling depth variations, we computationally subsampled all repertoires to an equal sample size of 5 · 105 counts. (B,C) Analysis of unsorted (TCR sequencing from all peripheral blood mononuclear cells), memory (CD3+, CD45+), and naive (CD3+, CD45RA+) blood samples from the same individual (Data source: Chu et al., 2019). (B) Clone size distributions in the different T cell compartments. Filtering naive clones that are also found in the memory compartment removes most large naive clones. (C) Frequency of large clones in the memory sample is shifted upwards relative to their frequency within the unsorted sample. Color represents logarithm of local kernel density estimate in regions with overplotting. The solid lines are guides to the eye (black line represents equal frequency, green line 2.6-fold higher frequency in the memory compartment). (D) The fraction of naive cells decreases with age (Data source: Britanova et al., 2016) starting in early infancy (Data source: Pediatric AIDS Clinical Trials Group et al., 2003). The legend shows the fitted time constant of exponential decay (± SE).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig1-figsupp3-v3.jpg)

**Figure 1—figure supplement 3.:** (A,D) Raw clone size distributions show large variability due to different sample sizes. (B,E) A normalization by sampling depth removes much of this variation. (C,F) A normalization by the fraction of memory cells at different ages further collapses the tails of the clone size distributions.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig1-figsupp4-v3.jpg)

**Figure 1—figure supplement 4.:** (A) Chronic infection with CMV drives large clonal expansions (Lindau et al., 2019; Sylwester et al., 2005). We thus repeated the analysis of Figure 1C separating individuals based on their CMV infection status (fitted lines shown in legend, regression results displayed as offset + slope · (age in years - 40)/10). Overall, CMV-positive individuals have a smaller α than uninfected individuals, which is independent of age. The average exponent in CMV-negative individuals decreases slowly with age, and in old age coincides those of CMV-positive individuals. Combining CMV infection status and age explained a significantly larger proportion of the variance in scaling exponents (17%) than age alone. (B) Many immune determinants differ markedly between the sexes (Klein and Flanagan, 2016). We thus analyzed whether α depends on sex. We find that the dependence on age is similar among the sexes, but men have on average a slightly smaller exponent than women indicating a more skewed repertoire organization. Data source: Emerson et al., 2017.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig1-figsupp5-v3.jpg)

**Figure 1—figure supplement 5.:** Each line shows the distribution in one individual. The black line shows a power law with a slope of -1 for visual comparison. The fitted power-law exponents α = 2.1 ± 0.1 (mean ± SE) are larger than in adult repertoires, but clone sizes are already remarkably broad. Data source: Britanova et al., 2016.

Much progress has been made deciphering the mechanisms of regulation and control of T cell dynamics over the last few decades (Antia et al., 2005; Sallusto et al., 2010; Farber et al., 2014). However, much of that progress has focused on the dynamics of subsets of T cells specific to a particular antigen and has come from experiments in mice. An important open question is how exposures to many antigens over a human lifetime collectively shape our T cell repertoire (Farber et al., 2014; Davis and Brodin, 2018).

High-throughput repertoire sequencing enables direct surveys of the diversity and clonal composition of T cells from human blood or tissue samples and thus promises to provide quantitative answers to this question (Robins et al., 2009; Thomas et al., 2014; Britanova et al., 2016; Emerson et al., 2017; Oakes et al., 2017; Thome et al., 2016; Robins et al., 2010; Qi et al., 2014; Lindau et al., 2019; TRACERx consortium et al., 2019). However, while the TCR locus provides a natural barcode for clonal lineages due to its large diversity, this same diversity also makes inferring past clonal dynamics a challenging inverse problem, in particular given practical limitations on sequencing depth and temporal resolution in longitudinal studies. Mathematical modeling can help address this challenge by solving the forward problem of linking clonal dynamics to emergent statistical patterns (Desponds et al., 2016; Lythe et al., 2016; Dessalles et al., 2019; Altan-Bonnet et al., 2020; de Greef et al., 2020). Comparing patterns to data can provide insights about dynamics from static snapshots of repertoire organization in different individuals. A particularly striking such pattern has been the observation of power-law scaling of clone sizes spanning several orders of magnitude (Robins et al., 2009; Thomas et al., 2014; Britanova et al., 2016; Emerson et al., 2017; Oakes et al., 2017). In a typical sample of T cells from peripheral blood, a large fraction of clones is only seen once within 105–107 sampled sequences, while the most abundant clones account for more than 1% of all sequencing reads. Such power-law scaling of clone sizes has been shown to arise at steady state in models of fluctuating clonal selection driven by different antigen encounters (Desponds et al., 2016). However, it is unclear whether this mechanism alone is sufficient to explain how clone size scaling is established, and more broadly how variable the clonal hierarchy is over time.

Here, we develop a theory of T cell dynamics throughout the human lifespan based on the statistical laws of repertoire organization and dynamics revealed by cohort and longitudinal human TCR repertoire sequencing (Britanova et al., 2016; Emerson et al., 2017; Chu et al., 2019; Lindau et al., 2019). We find that clonal expansions during repertoire formation play an important role in establishing the clone size hierarchy, which is only slowly reshaped by fluctuating clonal selection during adult life.

## Results

### A scaling law of human T cell repertoire organization

An important statistic to summarize repertoire organization is the clone size distribution, which tabulates the number of clones found at different multiplicities within a repertoire or sample. Multiple previous studies have shown that these distributions are heavy-tailed (Robins et al., 2009; Thomas et al., 2014; Britanova et al., 2016; Emerson et al., 2017; Oakes et al., 2017). However, potential confounding by noise introduced during the sequencing process has remain debated (Altan-Bonnet et al., 2020) and systematic analyses of how variable these distributions are across healthy individuals have been lacking. To fill these gaps, we reanalyzed data from two large-scale cohort repertoire sequencing studies of human blood samples, which used fundamentally different sequencing pipelines and thus have different sources of noise (Materials and methods – Experimental data sources). Both studies sequenced the locus coding for the hypervariable TCR CDR3 β-chain from peripheral blood T cells of healthy human volunteers spanning a large range of ages (Figure 1—figure supplement 1). In both studies, T cells were sequenced without regard to their phenotypic characteristics. A clone thus represents the full lineage of cells derived from a common ancestral cell irrespective of differentiation status (see Appendix 5 – Relation between clone size and cellular phenotypes and Figure 1—figure supplement 2 for a phenotypically resolved analysis).

After normalizing clone sizes to account for variations in sampling depth and for the increasing fraction of T cells of memory phenotype with age (Figure 1—figure supplement 3), we found that the tails of the clone size distributions collapsed to the same statistical law across individuals and cohorts (Figure 1B,C): Ranking clones by decreasing size, the rank of the largest clones approximately scales with their size C as a power law,

$$
rank∼C^{-\alpha},
$$

where α is a scaling exponent. To quantify the apparent similarity of the scaling relationship, we determined α for each sample by maximum likelihood estimation. Only a small fraction of all T cells are sampled, which poses a challenge because subsampling a power law leads to deviations from scaling at small clone sizes (Stumpf et al., 2005). To overcome this challenge, we used a trimming procedure and excluded clones smaller than a minimal size from the fitting, which decreases bias arising from subsampling (Appendix 1). Determined in this subsampling-robust manner the fitted power-law exponents agree remarkably well within the range of ages covered by both cohorts (Figure 1D): with α = 1.17 ± 0.03 (mean ± standard error [SE]) and α = 1.18 ± 0.01 in the Britanova cohort and Emerson cohort, respectively. Moreover, the fitted exponents varied little between individuals in both cohorts; with a sample standard deviation of fitted exponents of 0.14 and 0.21, respectively. The agreement of the mean exponents is noteworthy given the different sequencing pipelines and provides strong evidence that the scaling relationship (Equation 1) is a true feature of the clone size distribution and not of the measurement process.

What drives the emergence of a power-law distributed hierarchy of clone sizes? Given the reproducibility of the scaling law across individuals, we might hope for a statistical explanation independent of the precise antigenic history that has driven the expansion of specific cells in an individual. To test hypotheses about mechanisms underlying scaling, we describe repertoire dynamics using a general mathematical framework based on effective stochastic rate equations for the recruitment of new clones, and the proliferation and death of already existing clones within a T cell compartment (Materials and methods – Mathematical framework). In macroecology, where such reductionist approaches have a long history, simple neutral models within this framework have had surprising success in describing species abundance distributions only accounting for demographic stochasticity (Volkov et al., 2003), but this source of variability is insufficient to account for the observed breadth of T cell clone sizes (Desponds et al., 2016; de Greef et al., 2020; for a detailed discussion see Appendix 2). The failure of this null model has prompted a search for other mechanisms that explain scaling.

To constrain this search, we analyzed how fitted exponents varied with age. In particular, based on a finite time solution we derived for a previously proposed model (Desponds et al., 2016) of how power-law scaling can emerge from the cumulative effect of temporal fluctuations in clonal growth rates (Materials and methods – Slow convergence to steady–state scaling), we expected a substantially steeper tail in young individuals. While exponents overall decreased slightly with age, the dependence on age accounted for surprisingly little variation in both cohorts (Figure 1D), including when controlling for sex and cytomegalovirus (CMV) exposure status (Figure 1—figure supplement 4). Notably, scaling is established within the first decade of life, with significant clone size variability existing as early as at birth (Figure 1—figure supplement 5), defying previous model predictions.

### A mechanism for the emergence of scaling during repertoire formation

We hypothesized that scaling might result from clonal expansions during repertoire formation, which would naturally explain the early onset of scaling. Our hypothesis is based on experimental evidence in mice (Le Campion et al., 2002; Min et al., 2003; Haluszczak et al., 2009; Kawabe et al., 2017) and human (Rufer et al., 1999; Schönland et al., 2003) that repertoire formation is driven not only by increased thymic output, but also by large proliferative expansion of some T cell clones. Additionally, multiple studies Hammarlund et al., 2003; Pogorelyy et al., 2017; Tanno et al., 2020 have shown that some T cell clones can persist over multiple decades, which suggests that clonal turnover might be sufficiently slow for transient expansionary dynamics early in life to shape repertoire organization over a prolonged time period (see also Appendix 2 –Relaxation time scale in a neutral model).

To test our hypothesis, we constructed a minimal model of repertoire formation based on known T cell biology (Figure 2A). Following previous work (Bains et al., 2009; Lythe et al., 2016), we assume that T cells proliferate at a rate inversely proportional to the total number of cells N already present in the repertoire. This assumption leads to increased proliferation early in life before the repertoire has reached its homeostatic size, for which there is experimental evidence Le Campion et al., 2002; Min et al., 2003; Haluszczak et al., 2009; Kawabe et al., 2017; Rufer et al., 1999; Schönland et al., 2003. This assumption is also compatible with a simple mechanistic model of T cell competition (Materials and methods – Mechanistic motivation for the competition function). We further assume that cells die at a rate d, and that new clones are recruited at rate θ with an initial size C0. For simplicity, we set C0 equal to one in the following and we assume constant rates d and θ. Importantly, recruitment of new clones and total expansion of already existing clones maintain a constant ratio throughout development under these assumptions in line with findings that the fraction of cells with TCR excision circles, which are diluted during peripheral division, is constant during fetal development (Schönland et al., 2003) and infancy (Douek et al., 2001; Bains et al., 2009).

![Figure 2.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig2-v3.jpg)

**Figure 2.:** (A) Sketch of the stochastic dynamics of recruitment, proliferation, and death of T cells. Proliferation is inversely proportional to total repertoire size, which reflects increased competition as the repertoire grows. (B) Clone size distributions in simulated repertoires display power-law scaling (blue lines), in contrast to steady-state predictions that conform with those of a null model based only on demographic stochasticity (black line, Equation 48). (C) Illustration of the mechanism: early in life rates of proliferation exceed clonal turnover (lower panel). As the total repertoire size increases (gray line, upper panel) the proliferation rate decreases due to increased competition. The dynamics of selected clones after their recruitment marked by a dot is indicated by colored lines (upper panel). The line position shows the cumulative size of all prior clones, while the line width indicates the size of the clone (not to scale). The earlier a clones is recruited the larger it expands during the period of overall repertoire growth. (D) Dependence of the clone size distribution on parameters. Simulated repertoires at 5 years of age were subsampled to 106 cells to mimick the experimental sampling depth (solid lines). The simulated data closely follow predictions from a continuum theory of repertoire formation (dashed lines). Model parameters: (B,D) clonal death rate d = 0.2/year, clonal recruitment rate θ = 106/year, clone size at recruitment C0 = 1; (B) total proliferation rate b0 = 107/year (implying a recruitment to proliferation ratio γ = 0.1), (D) variable b0 as indicated in the legend by the ratio γ.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** Clone size distributions resulting from a variable recruitment size C0 (lognormal with standard deviation as indicated in legend) and repertoire growth (Equation 52). The black line shows a power law with a slope of -2.2 for visual comparison. Parameter: γ = 0.2.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig2-figsupp2-v3.jpg)

**Figure 2—figure supplement 2.:** Influence of a saturation of the proliferation rate, $b=b_{0}/(K+N)$, on the clone size distribution. The saturation induces a change of the scaling behavior at the largest clone sizes. Parameter: b0 = 2 · 104/year, d = 0.2/year, θ = 2 · 103/year (implying γ = 0.1), simulation length 5 years.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig2-figsupp3-v3.jpg)

**Figure 2—figure supplement 3.:** Clone size distributions in a simulated model where clones compete for specific antigens to which they bind with a probability pb. Model parameter: b0 = 104/year, θ = 103/year (implying γ = 0.1), Na = 1000, d = 0.2/year, simulation length 10 years.

We simulated the model starting from an empty repertoire and found that large clones displayed power-law scaling (Figure 2B blue lines). The simulation results contrast with steady-state predictions (Figure 2B black line), where the model effectively reduces to the neutral null model introduced earlier (Materials and methods – Steady-state distribution). The power-law tail persisted over multiple decades of aging, much beyond the timescale of cellular turnover, 1/d = 5 years, assumed in the simulations. A mathematical analysis shows that relative timescales of clonal and cellular turnover are controlled by the control parameter $\gamma=\thetaC_{0}/b_{0}$, which is the ratio of the contribution of recruitment and proliferation to overall compartment maintenance (Appendix 2). The long timescale of clonal turnover emerges because the chosen parameters are in the biological parameter regime $\gamma<1$, where most cell death is balanced by proliferation (den Braber et al., 2012; Macallan et al., 2017). Thus, we find that repertoire formation can produce transient but long-lasting power-law scaling of clone sizes.

To obtain intuitive insight into how scaling is established, we developed a continuum theory of clonal dynamics during repertoire growth (Materials and methods – Continuum theory of clonal growth). We find that the clone size Ci of the i-th clone recruited at time ti follows a subexponential growth law $C_{i}(t)=C_{0}(t/t_{i})^{1/(1+\gamma)}$. Clones recruited early grow large deterministically until competition lowers proliferation rates below the death rate (Figure 2C, lower panel). Different clones are recruited at different times and thus have more or less time to grow (Figure 2C, upper panel), which leads to a clone size distribution that follows power-law scaling with an exponent $\alpha=1+\gamma$. We note that this origin of the power-law scaling is closely related to a well-known generative mechanism for power-laws first studied by Yule, 1924 (for a detailed discussion see Appendix 4 – A unified view on mechanisms generating power laws in different growth processes).

The predicted exponent closely matches simulation results for different values of γ (Figure 2D dashed lines). Intuitively, when recruitment rates are higher, clones founded early have less time to outgrow later competitors, and thus the power law is steeper (α is larger). Importantly, in the biological parameter regime in which proliferation dominates, $\gamma<1$, the exponent is compatible with experiments (Figure 1B–D). We thus find, that the model – without fine tuning of parameters – reproduces the observed scaling exponent.

To expose a basic mechanism capable of producing broad clone size distributions, we have kept the model deliberately simple. More detailed models demonstrate the conditions and limits on the generalizability of this mechanism (Appendix 3). Variable recruitment sizes only affect the distribution of small clones (Figure 2—figure supplement 1); while a saturation of proliferation rates, or competition between subsets of T cells for specific resources maintain distributions at small and intermediate sizes while leading to cutoffs for the largest clones (Figure 2—figure supplement 2 and Figure 2—figure supplement 3, respectively).

### Long-lived incumbency advantage shows early expansions imprint clone size hierarchy

Our proposed theory for the rapid emergence of scaling predicts that large clones have expanded massively during repertoire formation. To test this prediction, we need to trace the dynamics of early founded clones. To this end, we exploit a change in the recombination statistics taking place during fetal development (Feeney, 1991; Rechavi et al., 2015; Park et al., 2020; Figure 3A). While T cells are produced by the thymus from the late first trimester the enzyme terminal deoxynucleotidyl transferase (TdT), which inserts non-templated nucleotides during VDJ recombination, is not expressed until the mid second trimester (Park et al., 2020). Therefore, many more T cells in fetal and neonatal blood have zero insertions than expected from the adult recombination statistics (Rechavi et al., 2015). This enables a statistical dating of individual clones in a repertoire based on their sequence (Sethna et al., 2017; Pogorelyy et al., 2017).

![Figure 3.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig3-v3.jpg)

**Figure 3.:** (A) Genetic recombination of a TCR involves the choice of a V, D, and J region among multiple genomically-encoded templates as well as the deletion and insertion of nucleotides at both the VD and DJ junctions. The enzyme TdT, which is responsible for nucleotide insertions, is not expressed during early fetal development. This allows a statistical dating of clonal ages, as clones with zero insertions at both junctions constitute a much larger fraction of all clones during a fetal and perinatal time window. (B) Fraction (± SE) of clones with zero insertions as a function of age and clone size. Clones are binned by their size into non-overlapping bins (rank 1–500, 501–1000, and so on; upper values are indicated on the x-axis). (C) Same data as in B displayed with a rescaled x-axis using fitted parameters τd = 9.1 ± 0.5 years, r* = 1.2 ± 0.2 ⋅ 104. The data collapses onto a sigmoidal function predicted by theory (Equation 3) with fitted p0,- = 0.074 ± 0.004, p0,+ = 0.0187 ± 0.0005 (black line). Data source: Emerson et al., 2017.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** Sequences with zero insertions code for a particular subset of all possible T cell receptors (TCRs), and some of their enrichment might represent a peripheral selective advantage of this subset of receptors. We thus asked how the enrichment depends on whether the sequence used to define the clone represents a productive or unproductive rearrangement. An unproductive rearrangement, in which the recombination process introduces a frameshift or stop codon, can be rescued by a second productive rearrangement, but is not expressed and thus not selected upon. Under the adult recombination statistics an unproductive zero insertion sequence is likely to be paired with a productive sequence with many insertions, and thus we would not expect to see a similar enrichment for unproductive sequences if a general peripheral selective advantage was causing the enrichment. Data source: Emerson et al., 2017.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** (A) Fraction of clones with TCRs that have exact matches in the VDJdb (Shugay et al., 2018) of known antigen specificities. (B) Fraction of clones with close matches (defined as nearest neighbor sequences in a Levenshtein distance sense, that is sequences with a single amino acid substitution, insertion or deletion). T cells known to be specific to particular antigens are enriched among the most abundant clones. However, there is little change in this enrichment as a function of age. Data source: Emerson et al., 2017.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig3-figsupp3-v3.jpg)

**Figure 3—figure supplement 3.:** Fraction of clones with T cell receptor (TCR) sequences $\sigma$ with a probability of generation $P_{g⁢e⁢n}⁢(\sigma)$ higher than 10-9. The probability of generation was calculated based on the nucleotide sequence using a probabilistic model of recombination with default parameters for human TCR sequences (Sethna et al., 2019). To remove confounding by the early expansionary dynamics, we excluded zero insertion clones as most of these clones also have high probability of generation. We find that clones with high $P_{g⁢e⁢n}$ are moderately more likely to be large. In comparison to the zero insertion clones, there is little change in their enrichment as a function of age. Data source: Emerson et al., 2017.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig3-figsupp4-v3.jpg)

**Figure 3—figure supplement 4.:** In CMV positive individuals zero insertion clones are less enriched among the largest clones. Data source: Emerson et al., 2017.

If our model is correct, we expect abundant clones to be more likely to have zero insertions than smaller clones. Analyzing data from the Emerson cohort, we find that zero insertion clones are indeed highly enriched within the most abundant clones (Figure 3B). This generalizes a previous report of such an enrichment within the naive compartment (Pogorelyy et al., 2017). The large cohort size allows us to perform a fine-grained analysis of how the fraction of zero-insertion clones depends on clonal abundance and age. We find that enrichment is particularly pronounced in the young and decreases with age at different speeds depending on clone size. Among the largest clones many more still have zero insertions than expected from the adult recombination statistics even multiple decades after repertoire formation. This suggests that the incumbent large clones created during repertoire formation are only slowly replaced by clones expanding later in life, similarly to what has been observed in mice (Gossel et al., 2017; Hogan et al., 2019).

Additional analyses rule out other potential explanations for the relation between insertion statistics and clonal abundance. First, sequences with zero insertions are similarly enriched among the largest clones in productive and unproductive sequences (Figure 3—figure supplement 1) demonstrating that convergent selection pressures during adult life are not a primary source of the higher abundance of these clones. Second, while abundant clones are also enriched for sequences with known antigen specificity (Figure 3—figure supplement 2) and sequences likely to be convergently recombined (Figure 3—figure supplement 3), these enrichments do not show the same striking dependence on age. Furthermore, we find that zero insertion clones are consistently less enriched in individuals infected by CMV (Figure 3—figure supplement 4), in contrast to the hypothesis that this infection might drive their expansion (Pogorelyy et al., 2017). Taken together, these analyses support the conclusion that dynamics during the perinatal time window of repertoire formation leave a long-lasting imprint on the T cell clonal hierarchy well into adulthood.

### Longitudinal clone size fluctuations predict the dynamics of the clone size hierarchy with aging

Building on this successful validation of a core prediction of our theory, we asked whether we could leverage the detailed pattern of enrichments at different ranks and ages to quantify how much being part of the wave of early expansions determines the fate of a clone relative to other sources of clone size variability. To this end, we extended our model beyond repertoire formation and allowed clonal proliferation rates to fluctuate over time to model the net effect of clonal selection by changing antigenic stimuli during adult life (Desponds et al., 2016). Specifically, we added a stochastic term to the growth rate of each clone to provide an effective Langevin description of the long-term dynamics induced by fast-changing antigen stimuli,

$$
b_{i}⁢(t)=b_{0}/N+\sqrt{2}⁢\sigma⁢η_{i}⁢(t),
$$

where $⟨η_{i}⁢(t)⁢η_{j}⁢(t^{′})⟩=\delta_{i⁢j}⁢\delta⁢(t-t^{′})$.

To determine a biologically plausible fluctuation strength $\sigma$, we analyzed the variability of clone sizes over time in a longitudinal repertoire sequencing study (Chu et al., 2019). We first analyzed how much recently expanded clones contribute to the tail of the clone sizes, and found that only a small fraction of the largest clones in any sample were not already large at the earliest time point (Figure 4A and Figure 4—figure supplement 1). To minimize confounding by transient dynamics affecting these clones, we excluded them from further analysis. We found that large clones had remarkably stable abundances over time, which we quantified by calculating the variance of log-foldchanges in clone size between the second and every subsequent time point (Figure 4B and Figure 4—figure supplement 2). The variability of clone sizes increased linearly over time as expected theoretically, from which we determined a magnitude of net growth rate fluctuations $\sigma$ compatible with the slope of increase (Materials and methods – Modeling long-term repertoire dynamics with fluctuating clonal growth rates).

![Figure 4.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig4-v3.jpg)

**Figure 4.:** (A,B) Longitudinal clonal dynamics in a healthy adult over a one year time span. (A) Fraction of the 1000 largest clones that fall within a specific clone size rank bin at the earliest time point. A small number of clones was not detected at all at the first time point (ND) likely representing recently expanded clones. All other clones were already among the largest clones initially. (B) Variance of log-foldchanges in clone size as a function of time difference for the 250 largest clones. (C) Fraction of clones with zero insertions as a function of age and clone size in a simulated cohort using a magnitude of clonal growth rate fluctuations inferred from the longitudinal data. Data source: Chu et al., 2019.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** Longitudinal analysis of the origin of the 1000 largest clones at each time point (indicated by arrows) in three healthy adults over a 1-year time frame. For each clone, we determined whether it was also sampled at the earliest time point, and if so at what clone size. The plot displays the fraction of clones that fall within a specific clone size rank bin at the first time point. At all times, a majority of clones was already large initially. A small fraction was not detected at all at the first time point (ND) likely representing recently expanded clones. (Supplement to Figure 4A which corresponds to panel C.) Data source: Chu et al., 2019.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** Dynamics of the 250 largest clones from second time point onwards excluding those not sampled at the first time point. (A-C) Fraction of the repertoire represented by these clones (sum of their normalized clone sizes); (D-F) mean and (G-I) variance of the log-foldchanges of their normalized clone sizes relative to time point 2. (Supplement to Figure 4B which corresponds to panel I.) Data source: Chu et al., 2019.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig4-figsupp3-v3.jpg)

**Figure 4—figure supplement 3.:** Same data as in Figure 3F displayed with a rescaled x-axis using fitted parameters $\tau_{d}=10.2\pm0.4⁢years,r^{⋆}=1.19\pm0.08⋅10^{4}$. The data collapses onto a sigmoidal function predicted by theory (Equation 3) with fitted $p_{0,-}=0.0695\pm0.0012$, $p_{0,+}=0.0198\pm0.0003$ (black line).

Using the fitted fluctuation strength, we constructed an in silico cohort of individuals of different ages according to the extended model (Materials and methods – Simulated cohort). In short, we computationally assigned each newly recruited clone to have zero insertions in a way that mimics the change in fetal recombination statistics, and we simulated memory repertoire dynamics based on the combined effect of early expansion and fluctuating clonal selection (Equation 2). The enrichment of zero insertion clones in the simulated cohort (Figure 4C) closely recapitulated the empirical findings using plausible parameter values. Notably, the longer lasting enrichment of zero insertion clones among the very largest clones is also found in the simulated cohort, and the timescales over which the enrichment decays agree remarkably well.

To obtain analytical insight into the enrichment dynamics, we studied how fluctuating growth rates reorder the clone size hierarchy established during repertoire formation (Materials and methods – Relaxation of the zero insertion distribution). The early clone size hierarchy in our model is dominated by the time of recruitment, which leads to a steep gradient in the zero insertion probabilities as a function of rank in the first decade of life (Figure 4C). We thus calculated how the zero insertion probabilities $P_{0}⁢(r,t)$ for clones of rank r at time t change due to fluctuating clonal growth starting from an idealized initial condition resembling the early clone size hierarchy, in which the clone sizes follow power-law scaling and the $r^{⋆}$ largest clones have a zero insertion probability $p_{0,-}$ and all others a probability $p_{0,+}$. We find that the probability of zero insertion clones then follows a sigmoidal shape as a function of log clone size rank, which changes with age as follows,

$$
P_{0}(r,t)=\frac{Δp_{0}}{2}erfc(\frac{log⁡(r/r^{⋆})+t/\tau_{d}}{2\sqrt{t/\tau_{d}}})+p_{0,+},
$$

where $Δ⁢p_{0}=p_{0,-}-p_{0,+}$ is the difference of zero insertion probabilities, $\tau_{d}$ a characteristic timescale, and $erfc(x)$ the complementary error function. These analytical results suggest a two-parameter rescaling of the enrichment of zero insertion clones as a general test of our theory. To demonstrate the feasibility of fitting these parameters from the enrichment dynamics, we determined them from the simulated data using weighted least squares fits setting r and t in Equation 3 to the mid-value of each bin. Rescaling the data with the fitted $r^{⋆}$ and $\tau_{d}$ lead to a collapse of all simulated datapoints onto the predicted sigmoidal curve (Figure 4—figure supplement 3). We then applied the same fitting and rescaling procedure to the experimental data, and found that it also leads to a remarkably good data collapse (Figure 3C).

The fitted parameters quantify key features of long-term repertoire dynamics, with $\tau_{d}$ characterizing the timescale over which fluctuations change the clone size hierarchy, and $r^{⋆}$ being related to the number of clones recruited during early repertoire growth. In line with the long-lived enrichment of zero insertion clones, the fitting reveals a remarkably slow timescale of about a decade over which the clone size hierarchy is reordered during healthy aging. The fitted $r^{⋆}$ indicates that early repertoire formation involves the expansion of a large number of different clones. Overall, the agreement between theory and data demonstrates that our model quantitatively captures how early expansions and ongoing fluctuating selection together shape the clone size hierarchy.

## Discussion

The evolution of the adaptive immune system has endowed vertebrates with the ability to adapt to pathogens that evolve on a timescale faster than host reproduction (Mayer et al., 2016). However, this ability comes with a cost: every generation needs to rebuild immune memory anew. As the organism first comes into contact with the outside world, it quickly needs to train its adaptive immune system to tolerate innocuous antigens and build up immune memory against pathogens. Here, we have shown that this process of rapid adaptation leaves a long-lasting imprint on the organization of the human T cell repertoire. More broadly, we propose a theory of repertoire dynamics that quantitatively describes how early expansions during repertoire formation combine with a lifetime of exposures to cumulatively shape the T cell hierarchy. Notably, we find that the T cell repertoire is remarkably stable over time in adult individuals outside of the punctuated expansions and contractions of specific clones in acute responses. Our study demonstrates that despite its vast complexity, repertoire dynamics is partially predictable by quantitative models. The model predictions can help guide future longitudinal studies, which in turn will allow refinements of modeling assumptions. The current work thus provides a stepping stone toward a detailed quantitative understanding of T cell dynamics that we hope will ultimately power the rational development of immunodiagnostics and therapeutics.

The general mechanism we describe for imprinting in the adaptive immune system provides a unified lens through which to view a number of converging lines of evidence about how a developmental time window shapes adaptive immunity (Guerau-de-Arellano et al., 2009; Farber et al., 2014; Gostic et al., 2016; Constantinides et al., 2019; Li et al., 2019; Davenport et al., 2020; Hong et al., 2020). In our model, overall repertoire growth early in life amplifies the effect of any early exposures, as the responding clones continue to proliferate as memory cells and thus are much larger than memory produced from similar exposures after the homeostatic repertoire size is reached. We thus expect early pathogen exposures to be particularly potent, as has been observed in influenza, where disease severity across age cohorts for different strains depends on the first exposure (Gostic et al., 2016). Conversely, we expect the presence of tolerizing factors early in life to be particularly crucial during repertoire formation to avoid autoimmunity, as has been observed for the autoimmune regulator gene AIRE, for which expression is only essential during a perinatal time window (Guerau-de-Arellano et al., 2009).

A limitation of datasets used in this study is that they do not provide direct information about the phenotypic characteristics of cells belonging to different clones. Repertoire sequencing of phenotypically sorted blood samples shows that the largest clones predominantly consist of cells with memory phenotype (Appendix 5). This indirectly suggests that the clonal expansions during repertoire formation produce memory cells as we have assumed in our simulated cohort (Figure 4C). Supporting this interpretation, a substantial number of memory cells circulate in the blood quickly following birth (Pediatric AIDS Clinical Trials Group et al., 2003) and recent evidence suggests that memory-like T cells are already generated in particular tissue sites such as the intestine even before birth (Zhang et al., 2014; Li et al., 2019). However alternatively, early expansions could also set up a broad distribution of naive T cell clone sizes (de Greef et al., 2020), whose hierarchy would then need to be roughly maintained during the transition into memory to be compatible with the observed impact of early expansions on the hierarchy of the most abundant clones. Advances in repertoire sequencing of T cells sorted with increasing granularity using cell surface markers (Oakes et al., 2017; Soto et al., 2020) along with advances in single-cell technologies linking TCR sequencing and cellular phenotyping could help differentiate between these scenarios in the future.

An important question raised by our work is which antigens drive the expansion of early T cell clones. To address this question, it will be necessary to determine the exposures that imprint the abundance of these clones, as has been done recently for mucosal-associated invariant T cells (Constantinides et al., 2019), a subset of non-conventional T cells. Going forward, the highly abundant clones with sequences close to the genetically inherited gene templates resulting from the absence of TdT expression during early fetal development are a particularly interesting target of study. They might constitute an evolutionarily controlled set of innate-like defenses within the adaptive immune system. Determining what imprints their abundances will help resolve the question of whether their large abundances are simply a byproduct of rapid repertoire formation or whether these clones serve particular functions.

## Materials and methods

### Experimental data sources

We analyzed T cell repertoire sequencing data from two large published cohort studies of healthy human volunteers by Britanova et al., 2016 and Emerson et al., 2017 and from a longitudinal study by Chu et al., 2019, detailed descriptions of which we provide in the following.

In short, Britanova et al., 2016 sequenced reverse transcribed mRNA with added unique molecular identifiers (UMIs), while Emerson et al., 2017 and Chu et al., 2019 sequenced genomic DNA coding for this region without the addition of UMIs. These approaches have complementary strengths: The addition of UMIs allows to correct for stochasticity during PCR amplification and sequencing artifacts, while DNA sequencing removes the influence of cell-to-cell gene expression heterogeneity.

The Britanova cohort comprises 71 individuals spanning ages 6–103 years, as well as eight cord blood samples. The Emerson cohort spans ages 1–74 years and consists of a training and validation set of 666 and 120 individuals, respectively. From the training set, we excluded 111 samples with missing age information and 62 samples with a conflicting data format. We used only samples from the training set to analyze how the scaling law of repertoire organization changes with age (Figure 1). For the zero insertion enrichment analyses (Figure 3B,C), we combined both the training and validation set together with separately published repertoire sequencing data from eight elderly individuals Lindau et al., 2019 generated using the same experimental pipeline (immunoSEQ, Adaptive Biotechnologies, Seattle) to achieve the broadest possible coverage of all age groups.

The longitudinal study by Chu et al., 2019 performed repertoire sequencing of peripheral blood from three healthy female volunteers (using the immunoSEQ pipeline) over eight time points spanning a ~1 year time frame. One individual in the study was in mid-adulthood (24–45 years, Subject 3 in the original study), while two were in early adulthood (18–24 years, Subjects 1 and 2 in the original study). In Figure 4A,B, we display data from the older individual as we expect dynamics of large clones to be masked less by measurement noise as the large clones increase in relative abundance with age.

All studies from which we analyzed data sequenced the locus coding for the TCR CDR3 β-chain only, and we thus define clones as collections of cells sharing the same CDR3 β-chain. Clone sizes are defined as the number of distinct unique molecular identifiers (UMIs) sequenced (Britanova cohort), or based on sequencing reads (Emerson cohort). The definition of a clone solely based on the CDR3 β-chain neglects convergent recombination of the most easily produced receptors with different CDR3 α-chains, but we expect convergent recombination to be sufficiently rare overall for this distinction not to qualitatively affect clone size distributions.

For all studies we used data, which was preprocessed as described in the original study. This data is publicly available using the links provided in Table 1.

**Table 1.**
 Repertoire sequencing data used in this study.


<table>
  <thead>
    <tr>
      <th>Study</th>
      <th>Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Britanova et al., 2016</td>
      <td>https://doi.org/10.5281/zenodo.826447</td>
    </tr>
    <tr>
      <td>Emerson et al., 2017</td>
      <td>https://doi.org/10.21417/B7001Z</td>
    </tr>
    <tr>
      <td>Lindau et al., 2019</td>
      <td>https://doi.org/10.21417/PL2018JI</td>
    </tr>
    <tr>
      <td>Chu et al., 2019</td>
      <td>https://doi.org/10.21417/B7J01X</td>
    </tr>
  </tbody>
</table>

We also used flow cytometry data on the fraction of naive cells from Britanova et al., 2014 (available at https://doi.org/10.1371/journal.pcbi.1005572.s016) and from Pediatric AIDS Clinical Trials Group et al., 2003.

### Data analysis

#### Fitting power-law exponents

We estimate the power-law exponent from sampled clone sizes ${C_{i}}$, $i=1,…,M$, which exceed a minimal size $C_{m⁢i⁢n}$ by numerically maximizing the log-likelihood of the data (Clauset et al., 2009),

$$
ℒ=-M⁢ln⁡ζ⁢(1+\alpha,C_{m⁢i⁢n})-(1+\alpha)⁢\sumi=1Mln⁡C_{i},
$$

where $ζ⁢(x,k)$ is the incomplete Riemann zeta function. We use $C_{m⁢i⁢n}=16$ for both cohorts, which provides a balance between minimizing bias of the estimated exponents induced by subsampling while not overly increasing the variance of the estimator by excluding most of the data (see Appendix 1—figure 2).

#### Fitting the zero insertion profiles

To fit the zero insertion fractions to the theory prediction (Equation 3) we determine the values for $r^{⋆}$ and $\tau_{d}$ by a weighted least squares fit. We set r and t to the mid-value of each bin for the data. We weight each value by the sum of its empirical standard error and a fixed model specification error of $2⋅10^{-3}$ chosen based on fits to the simulated cohort (Figure 4—figure supplement 3). To demonstrate the feasibility of the parameter inference, we reinferred the parameters from the simulated data and recovered those used as parameter values for the simulation. We also fitted the values of $p_{0,-}$ and $p_{0,+}$, but we note that they are not used in the rescaling and are only needed to display the theoretical curve (Equation 3).

#### Normalization of clone sizes

Variations in sampling depth can confound comparisons of clone sizes (Appendix 1). Intuitively, if we sample more cells overall we also expect to sample proportionally more cells belonging to each given clone. This suggests to use the frequency with which cells are sampled from a given clone as a more robust measure, which can be empirically estimated by normalizing each clone size by the total sample size. We further normalize clone sizes by the fraction of memory T cells found in people of different ages to account for the increase in memory cell fraction in peripheral blood with age (Appendix 5). Together these two normalization steps lead to a large degree of data collapse as compared to unnormalized clone sizes (Figure 1—figure supplement 3).

#### Regression analyses

We determine 95% confidence intervals on regression lines by bootstrapping using case resampling (Efron and Hastie, 2016).

### Mathematical framework

We describe T cell dynamics using the following general set of stochastic rate equations. The class of models we consider are known in the mathematical literature as birth-death-immigration models. The number of cells $C_{i}$, $i=1,…,M$ of each of the M clones in the repertoire changes according to

$$
proliferation:C_{i}→b_{i}(C,X,t)C_{i}C_{i}+1,
$$



$$
death:C_{i}→d_{i}(C,X,t)C_{i}C_{i}−1,
$$

where the rate of proliferation $b_{i}⁢(𝑪,𝑿,t)$ or cell death $d_{i}⁢(𝑪,𝑿,t)$ generally can depend on the repertoire composition $𝑪$, on the time t, and on the state of the environment $𝑿⁢(t)$ representing for example the levels of different antigens and cytokines in the organism at a given time. We furthermore consider that new clones are added at rate $\theta⁢(𝑿,t)$ at a size C0,

$$
recruitment:→\theta(X,t)C_{M+1}=C_{0}.
$$

This recruitment represents thymic output and antigen-driven differentiation of naive cells for the naive and memory compartment, respectively.

$$
b_{i}(C,X,t)=b_{0}/N,d_{i}(C,X,t)=d,\theta(X,t)=\theta
$$

where $N⁢(t)=\sum_{j=1}^{M⁢(t)}C_{j}⁢(t)$ is the total repertoire size. In the results section 'Long-lived incumbency advantage shows early expansions imprint clone size hierarchy' w modify this model by adding a noise term that describes the effective influence of environmental variations $𝑿⁢(t)$ on clonal proliferation,

$$
b_{i}⁢(𝑪,𝑿,t)=b_{0}/N+\sqrt{2}⁢\sigma⁢η_{i}⁢(t),
$$

where $⟨η_{i}⁢(t)⁢η_{j}⁢(t^{′})⟩=\delta_{i⁢j}⁢\delta⁢(t-t^{′})$.

### Modeling repertoire formation

#### Mechanistic motivation for the competition function

We consider a population of N T cells that proliferate at a rate proportional to the concentration S of a set of stimuli (stimulatory cytokines), $b∝S$. We assume that the cytokines are produced by other cells at some fixed rate p and degraded at a basal rate q. We further assume that competition between T cells is mediated by their consumption of cytokines. The dynamics of S is then described by

$$
\frac{d⁢S}{d⁢t}=p-q⁢S-k⁢S⁢N,
$$

where $-k⁢S⁢N$ is a mass action term describing how T cells lower cytokine levels. Assuming a separation of timescales in which cytokine concentrations change quickly we obtain the quasi steady state approximation

$$
S=\frac{p}{q+k⁢N}.
$$

When the consumption term dominates relative to basal decay, $k⁢N≫q$, we obtain $b∝S∝1/N$.

#### Mean-field competition approximation

We simplify the full stochastic model (Equation 5–Equation 7) using a mean-field approximation for the competition, which decouples the dynamics of individual clones while retaining the full stochasticity on the clonal level. This approximation replaces the dependence of the proliferation rate on N by a dependence on its continuum theory average given by Equation 14. We exactly simulated a system of reduced size to validate the mean-field approximation. The distributions of the exact and mean-field simulations agree to within stochasticity (Figure 5), with the exception of the largest clone, which is larger in the exact simulations as has been discussed elsewhere (Dodds et al., 2017).

![Figure 5.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig5-v3.jpg)

**Figure 5.:** Comparison of full stochastic simulations and simulations using mean-field competition. Parameter: $b_{0}=2⋅10^{4}$/year, $d=0.2$/year, $\theta=2⋅10^{3}$/year (implying $\gamma$ = 0.1), simulation length 5 years.

#### Continuum theory of clonal growth

To obtain insight into why the model produces power-law scaling we present a simple continuum theory of early clonal dynamics. We approximate the clone size dynamics of the i-th clone $C_{i}$ as

$$
\frac{d⁢C_{i}}{d⁢t}=(\frac{b_{0}}{N⁢(t)}-d)⁢C_{i},
$$

with $C_{i}⁢(t_{i})=C_{0}$ at the time of recruitment ti. The total repertoire size $N=\sum_{i}C_{i}$ evolves according to

$$
\frac{d⁢N}{d⁢t}=b_{0}-d⁢N+\theta⁢C_{0},
$$

whose solution is given by

$$
N⁢(t)=(b_{0}+\theta⁢C_{0})⁢(1-e^{-d⁢t})/d.
$$

For times large compared to $1/d$ the total repertoire size given in Equation 14 reaches a steady-state,

$$
N_{∞}=(b_{0}+\theta⁢C_{0})/d,
$$

because competition for proliferation signals acts as a homeostatic regulator. By combining Equation 14 and Equation 12 we derive the clonal growth law

$$
C_{i}(t)=C_{0}(\frac{e^{dt}−1}{e^{dt_{i}}−1})^{1/(1+\gamma)}e^{−d(t−t_{i})},
$$

where $\gamma$ as in Appendix 2 is the recruitment to proliferation ratio which in this model is given by $\gamma=\theta⁢C_{0}/b_{0}$. To simplify we expand the growth law at leading order for small times, $t_{i}<t≪1/d$, to obtain

$$
C_{i}⁢(t)=C_{0}⁢(\frac{t}{t_{i}})^{1/(1+\gamma)}.
$$

This expression can also be derived directly by noting that early repertoire growth is linear $N⁢(t)≈(b_{0}+\theta⁢C_{0})⁢t$, and that the early dynamics is dominated by proliferation and not death such that

$$
\frac{d⁢C_{i}}{d⁢t}=\frac{1}{(1+\gamma)⁢t}⁢C_{i},
$$

which is solved by Equation 17. Given the constant recruitment of new clones the distribution of the ti’s is uniform, which with Equation 17 implies a clone size distribution

$$
P⁢(C)=P⁢(t_{i}⁢(C))⁢|\frac{d⁢t_{i}}{d⁢C}|∝C^{-2-\gamma}
$$

that follows power-law scaling with an adjustable exponent that depends on $\gamma$. Note that the exponent for $P⁢(C)$ differs by one from the exponent for the rank (Clauset et al., 2009), which is a complementary cumulative distribution, and thus $\alpha=1+\gamma$.

#### Steady-state distribution

To derive the power-law scaling, we have expanded the total repertoire size for small times (or death rates). How does the clone size distribution change later in life? At large times, the division rate $b_{0}/N⁢(t)$ falls below the constant death rate d as the steady-state repertoire size $N_{∞}$ is approached following Equation 14. In this model this happens at a time $t^{⋆}≃log⁡(1+1/\gamma)/d$, after which the large clones experience a deterministic force toward extinction. For times $t≫t^{⋆}$ the model effectively reduces to the neutral birth-death dynamics considered in Appendix 2. (The growth rate fluctuations produced by variations of the total population size around steady state asymptotically vanish for large $N_{∞}$.) We thus expect the steady-state clone size distribution to be equivalent to that of the neutral model (Equation 48). Indeed this distribution accurately describes the distribution of small clones in old age (Figure 2B). The neutral distribution is not compatible with data as discussed before. However, the timescale over which large early founded clones vanish is long (Appendix 2) such that a tail of large clones resulting from the early growth dynamics can be maintained much beyond $t^{⋆}$ until $t≫\tau_{c}$ (see also Appendix 2 –Relaxation time scale in a neutral model).

### Modeling long-term repertoire dynamics with fluctuating clonal growth rates

#### Slow convergence to steady-state scaling

Multiplicative stochastic processes are a classical generative mechanisms for heavy-tailed distributions (Sornette and Cont, 1997; Gabaix, 1999; Newman, 2005). In the context of lymphocyte dynamics this mechanism has first been proposed by Desponds et al., 2016, who argued that fluctuations in antigen availability can lead to multiplicative stochastic dynamics producing power-law scaling at steady state. Here, we expand on this earlier work by analyzing a simple fluctuating fitness model out-of-steady-state. Our analytical results show that the emergence of scaling can be slow when the fluctuation amplitude is small.

We opted to treat proliferation rate fluctuations as temporally uncorrelated for computational tractability (Equation 2). Correlations in proliferation rate fluctuations are clearly an important feature of short-term dynamics – for example to describe the quick expansion and contraction during and following acute infection over a timescales of days and weeks, respectively (Mayer et al., 2019). However, given finite correlation times we expect to be able to capture dynamics over the long timescales which we are interested in here, with uncorrelated noise with an effective net fluctuation strength that averages over the short-term dynamics.

In this limit clone sizes follow a geometric Brownian motion, that is $x=log⁡C/C_{0}$ follows the Langevin equation

$$
\frac{d⁢x_{i}}{d⁢t}=f_{0}+\sqrt{2}⁢\sigma⁢η_{i},
$$

with initial condition $x⁢(t_{i})=0$, where $\sigma$ sets the fluctuation strength and where $⟨η_{i}⁢(t)⁢η_{j}⁢(t^{′})⟩=\delta_{i⁢j}⁢\delta⁢(t-t^{′})$. A negative mean fitness $f_{0}<0$ balances the recruitment of new clones and the net expansion induced by the fluctuating term. In general, we might want to include also demographic noise and the extinction of clones as an absorbing boundary condition (Desponds et al., 2016), but here for simplicity we will neglect those effects. Equation 20 is a diffusion equation for the logarithmic clone size x and has the well-known Green’s function

$$
G(x,y,t)=\frac{1}{\sqrt{4\pi\sigma^{2}t}}e^{−\frac{(x−y−f_{0}t)^{2}}{4\sigma^{2}t}},
$$

which describes how the distribution spreads out from an initial $\delta$-distribution centered at size y. The clone size distribution at time T is given by

$$
P⁢(x,T)=\int_{0}^{T}dt⁢P⁢(t)⁢G⁢(x,0,t),
$$

where t is the clonal age. For a constant immigration rate t is uniformly distributed and we obtain by integration

$$
P(x,T)=\frac{e^{\frac{f_{0}x(1−\theta(x))}{\sigma^{2}}}erfc(\frac{|x|−f_{0}T}{\sqrt{4T\sigma^{2}}})−e^{\frac{f_{0}x\theta(x)}{\sigma^{2}}}erfc(\frac{|x|+f_{0}T}{\sqrt{4T\sigma^{2}}})}{2f_{0}T},
$$

where $\theta⁢(x)$ is the Heaviside step function, $\theta⁢(x)=0$ for $x<0$ and $\theta⁢(x)=1$ otherwise. For large T and $x>0$ this reduces to

$$
P⁢(x)→e^{\frac{f_{0}⁢x}{\sigma^{2}}}/(-f_{0}⁢T),
$$

which implies

$$
P⁢(C)∼C^{-(1+\alpha)} with⁢\alpha=-f_{0}/\sigma^{2},
$$

recovering the steady-state result from Desponds et al., 2016.

Setting $f_{0}=-\alpha⁢\sigma^{2}$ and rescaling age as $\tau=T⁢\sigma^{2}$, we can rewrite the finite time solution as

$$
P(x,\tau)=\frac{e^{−\alphax\theta(x)}erfc(\frac{|x|+\tau\alpha}{\sqrt{4\tau}})−e^{−\alphax(1−\theta(x))}erfc(\frac{|x|−\alpha\tau}{\sqrt{4\tau}})}{2\alpha\tau}.
$$

Plotting the cumulative distribution of clone sizes at different effective ages (Figure 6) we observe that the convergence of clone size distributions is slow when $\sigma^{2}$ is small. Based on estimates for the fluctuation strength from longitudinal data (Figure 4B), we would expect significant deviations from the steady state power-law scaling that persist into adulthood. Thus, this mechanism alone is unable to account for the observed power-law scaling in data.

![Figure 6.](https://cdn.elifesciences.org/articles/61639/elife-61639-fig6-v3.jpg)

**Figure 6.:** Analytical predictions for the clone size distributions in a geometric Brownian motion fluctuating fitness model (Integral of Equation 26) as a function of effective age $\tau=T⁢\sigma^{2}$. The black line shows the asymptotic prediction for the steady-state scaling. Parameter: $\alpha=1.2$.

#### A note on the scaling exponent

A minimal requirement for the existence of a steady state is $f_{0}<0$ ensuring that clones eventually die to balance the recruitment of new clones. This condition still allows such multiplicative processes to produce power-laws with arbitrary exponents as noted before (Desponds et al., 2016). Here, we propose that the parameters should fulfill a stronger condition. In particular, it seems reasonable to require that the large clones do not deterministically take up a larger fraction of the overall repertoire, or equivalently that their expected change in clone size should not exceed one. The mean of the lognormal distribution of clone size change is given by $e^{f_{0}+\sigma^{2}}$, and thus we find the stronger condition

$$
-f_{0}<\sigma^{2}.
$$

Importantly, it follows that exponents in the vicinity of $\alpha=-1$ arise without fine-tuning as long as the timescale of expected net clonal decay is large compared to the diffusion timescale.

Another perspective on the parameterization is provided by noting that the Langevin equation for C (not $x=log⁡C$) in the Stratonovich convention includes an extra drift term $-\sigma^{2}$, to keep $⟨Δ⁢C⟩$ independent of the choice of $\sigma$. Alternatively, in the Ito convention the extra drift term arises by Ito’s lemma when transforming the equation from C to x.

#### Predictions for longitudinal fluctuations in clone sizes

To quantify longitudinal fluctuations, we calculate the mean and variance of log-clonesize changes with respect to a reference time t0. From the model we, according to Equation 21, expect

$$
⟨x(t)−x(t_{0})⟩=f_{0}t
$$



$$
⟨(x(t)−x(t_{0})−⟨x(t)−x(t_{0})⟩)^{2}⟩=2\sigma^{2}t.
$$

The variance of log-clonesize changes in empirical data involves an additional term $\sigma_{S}^{2}$ accounting for sample-to-sample variability. This term is expected not to depend on the time difference, and we can thus determine $\sigma^{2}$ by linear regression with an intercept that captures the sampling variability $\sigma_{S}^{2}$ (Figure 4B).

We note that a similar approach has been independently proposed in unpublished work by Ferri, 2018.

#### Relaxation of the zero insertion distribution

Here, we solve for the relaxation dynamics of the zero insertion distribution in a simplified setting. Throughout we use log clone sizes $x=log⁡C$ for notational convenience. We posit that at time 0 the power-law distribution $P⁢(x,0)=\alpha⁢e^{-\alpha⁢x}$ is already established and we further assume that the $r^{⋆}$ largest clones have zero insertion probability $p_{0,-}$ and all smaller or later added clones have probability $p_{0,+}$. Then the probability that a clone of a given size x has zero insertions is given by

$$
P_{0}⁢(x,t)=Δ⁢p_{0}⁢f_{e⁢a⁢r⁢l⁢y}⁢(x,t)+p_{0,+}
$$

where $Δ⁢p_{0}=p_{0,-}-p_{0,+}$ and $f_{e⁢a⁢r⁢l⁢y}⁢(x,t)$ is the fraction of clones of size x and time t that derive from the $r^{⋆}$ largest clones at time 0.

In the following, we determine an analytical formula for $f_{e⁢a⁢r⁢l⁢y}⁢(x,t)$ under the assumption that the dynamics leaves the distribution unchanged $P⁢(x,t)=P⁢(x,0)$. We then have

$$
f_{early}(x,t)=\frac{\int_{x_{min}}^{∞}dye^{−\alphay}G(x,y,t)}{e^{−\alphax}},
$$

where $G⁢(x,y,t)$ as before is the Green’s function of the fluctuating proliferation rate dynamics and $x_{m⁢i⁢n}$ is defined such that the total number of clones times $P(x>x_{m⁢i⁢n})$ equals $r^{⋆}$. By integration one obtains

$$
f_{early}(x,t)=\frac{1}{2}e^{\alphat(f_{0}+\alpha\sigma^{2})}erfc(\frac{x_{min}−x+t(f_{0}+2\alpha\sigma^{2})}{\sqrt{4\sigma^{2}t}}),
$$

which after setting $f_{0}=-\alpha⁢\sigma^{2}$ reduces to

$$
f_{early}(x,t)=\frac{1}{2}erfc(\frac{x_{min}−x+\alpha\sigma^{2}t}{\sqrt{4\sigma^{2}t}}).
$$

To convert clone size into ranks, we note that $rank∼e^{-\alpha⁢x}$ and thus $x_{m⁢i⁢n}-x∼\frac{1}{\alpha}⁢log⁡(\frac{r}{r^{⋆}})$. In combination with Equation 33 and Equation 30 we thus obtain

$$
P_{0}(r,t)=\frac{Δp_{0}}{2}erfc(\frac{\frac{1}{\alpha}log⁡(r/r^{⋆})+\alpha\sigma^{2}t}{\sqrt{4\sigma^{2}t}})+p_{0,+}.
$$

Defining a characteristic timescale for the diffusive dynamics as $\tau_{d}=1/(\alpha⁢\sigma)^{2}$, we can simplify this expression to

$$
P_{0}(r,t)=\frac{Δp_{0}}{2}erfc(\frac{log⁡(r/r^{⋆})+t/\tau_{d}}{2\sqrt{t/\tau_{d}}})+p_{0,+}.
$$

### Simulation procedures

#### Repertoire formation

To simulate the model efficiently at large scales, we use a mean-field competition approximation (Materials and methods – Mean–field competition approximation). We verified the validity of the mean-field assumption by comparing them to full stochastic simulations of the coupled birth-death-immigration equations, which we simulated using the Gillespie algorithm (Press et al., 2007; Figure 5). In the mean-field approximation, the proliferation rate is time-dependent, which requires a specific procedure for sampling event times. The time interval until the next event depends on the total rate for all possible processes $\lambda⁢(t)=\theta+b⁢(t)+d.$ To sample an interval of time $Δ⁢t$ between two events from an inhomogeneous Poisson process of rate $\lambda⁢(t)$ one can sample from a Poisson process with a rate function $\lambda^{⋆}⁢(t)$ fulfilling the majoration condition $\lambda^{⋆}\geq\lambda⁢(t)⁢∀t$ and then reject a proposed time interval $Δ⁢t^{⋆}$ with a probability of $1-\lambda⁢(t+Δ⁢t^{⋆})/\lambda^{⋆}⁢(t+Δ⁢t^{⋆})$ (Lewis and Shedler, 1979). The thinned set of event times follows the statistics of the Poisson process with rate $\lambda⁢(t)$. Here, because competition is increasing with time, $\lambda⁢(t)$ decreases monotonically. Therefore, the homogeneous Poisson process with a constant rate function $\lambda^{⋆}⁢(t)=\lambda⁢(t_{0})$, satisfies the majoration condition. Using this thinning technique, we are able to efficiently sample the next event time while accounting for the time-dependence of the proliferation rate. The source code that allows reproduction of the statistical analyses and numerical results reported in the manuscript is published (Gaimann et al., 2020).

#### Simulated cohort

As empirical evidence shows that the tail of the clone size distribution is almost exclusively driven by cells with memory phenotype (Appendix 5), we focused on the clone size dynamics within the memory compartment. We assumed that the recruitment size for memory cells is independent of the prior naive cell dynamics, and we thus did not explicitly model the clone size dynamics within the naive compartment. Within the memory compartment, we modeled clone size dynamics under the combined effect of early deterministic expansions during repertoire formation and fluctuating clonal growth rates according to Equation 2. Given the large sizes of memory clones, we expect demographic stochasticity to be negligible relative to clone size variability introduced by fluctuating selection. For tractability, we thus ignored demographic fluctuations, which allowed us to combine the continuum solution to the deterministic clonal growth (Equation 16) with the stochastic propagator for the fluctuating dynamics (Equation 21) to efficiently simulate the dynamics. To study the enrichment of zero insertion clones in silico, we assigned newly recruited memory clones as having zero insertions with a probability equal to the fraction $p_{0}⁢(t)$ of zero insertion clones within the naive compartment. We assumed $p_{0}⁢(t)=p_{0,-}$ before TdT expression turn-on at time $t^{†}$ and $p_{0}⁢(t)=p_{0,-}⁢t/t^{†}+p_{0,+}⁢(1-t/t^{†})$ for $t>t^{†}$, where $t/t^{†}$ is the fraction of naive clones produced since the switch to the adult recombination statistics. Taken together, these simplifications lead to the following direct sampling scheme:

where $d,\gamma,\sigma^{2}$ are model parameters and $y∼N⁢(\mu,\sigma^{2})$ indicates x being drawn from a normal distribution of mean µ and variance $\sigma^{2}$.

where $x∼Pois(\lambda)$ indicates x being drawn from a Poisson distribution of parameter $\lambda$.

#### Parameter choices

In the following, we summarize the parameters we used to simulate repertoire dynamics and provide additional motivation for our parameter choices.

Lifetimes of several years and several months have been measured by deuterium labeling for naive and memory T cells, respectively (De Boer and Perelson, 2013; Borghans et al., 2018). Clonal turnover can be substantially slower than cellular turnover when proliferation balances most death (Appendix 2). This has been shown to be the case for the maintenance of naive cells in human (Zhang et al., 2014), where the aging-associated decline of the fraction of T cells with TCR excision circles (TRECs) suggests $\gamma∼0.1$. Similarly, memory T cell numbers decline much more slowly overall than suggested by the deuterium labeling literature, which is thought to be driven by homeostatic proliferation in the absence of reinfection (Macallan et al., 2017). For example, T cell memory has been observed to decline with half-lives of 8–15 years by following titers after small pox vaccination (Hammarlund et al., 2003). Additionally, the relatively short average lifetime of memory T cells likely masks substantial heterogeneity with a subset of more long-lived cells also contributing to the slower long-term decline of memory cells (Akondy et al., 2017). Another line of direct evidence for long clonal persistence has come from two studies of identical twins (Pogorelyy et al., 2017; Tanno et al., 2020), which have shown an excess sharing of identical clones decades after in utero blood exchange in monochorionic twins.

To simulate repertoire formation (Figure 2B), we used a set of parameters summarized in Table 2. In choosing these parameters, we were not trying to reproduce exact values of any particular T cell subset, but rather illustrate a plausible biological parameter regime that characterizes T cell dynamics. We note that qualitatively the scaling presented in Figure 2B only depends on $\gamma$ as shown by our theoretical analysis, in a way that is shown in Figure 2D. For the recruitment rate $\theta$, we used a rate intermediate between those suggested by estimates of thymic output and the rate of recruitment of memory clones suggested by estimates of the diversity of the memory compartment (see below). We note that under mean-field competition the rate of recruitment $\theta$ only determines the overall number of clones, but does not influence the dynamics of individual clones. While $\theta$ decreases during adulthood for both the naive compartment (as thymic production wanes with age) and the memory compartment (as new primary responses are rarer at advanced age), we used a constant $\theta$ for simplicity. We expect this simplifying assumption not to qualitatively affect the results in Figure 2 due to a separation of timescales: The clone size scaling emerging from the expansionary dynamics only depends on the rate $\theta$ during infancy and not on slower changes in $\theta$ happening during adulthood. We chose a recruitment size of one to numerically investigate potential deviations from the continuum theory predictions due to demographic stochasticity. The number of recruited clones is of course much larger in practice in the memory compartment, and even naive cells undergo a few rounds of division before thymic export and thus have $C_{0}>1$. Assuming a larger C0 will further decrease the small effects of demographic stochasticity relative to the continuum theory.

**Table 2.**
 Parameters of the minimal model of repertoire formation (Figure 2B).


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Explanation</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>d</td>
      <td>death rate</td>
      <td>0.2/year</td>
    </tr>
    <tr>
      <td>γ</td>
      <td>recruitment to proliferation ratio</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>θ</td>
      <td>recruitment rate</td>
      <td>106/year</td>
    </tr>
    <tr>
      <td>C0</td>
      <td>recruitment size</td>
      <td>1</td>
    </tr>
  </tbody>
</table>

To study the enrichment of zero insertion clones in a simulated cohort (Figure 4C), we used the same recruitment to proliferation ratio and death rate as in the previous simulation of repertoire formation. To determine the absolute number of large clones that have zero insertions in these simulations, the choice of the recruitment rate $\theta$ is important. Based on order-of-magnitude estimates of the clonal diversity of the memory compartment (Robins et al., 2009; Qi et al., 2014), we chose a value of $\theta=10^{5}$/year. Additionally, we chose a fraction of zero insertion clones within the early naive compartment of $p_{0,-}=0.07$ (roughly equal to their overall fraction in cord blood [Pogorelyy et al., 2017]) and in the late naive compartment equal to $p_{0,+}=0.02$ (roughly equal to their overall fraction in adult blood). Finally, we used $t^{†}=0.05$ years for the time of the recombination switch, which together with the choice of $\theta$ produces ~104 excess zero insertion clones recruited during repertoire formation in line with the empirical enrichment data in the <10 years age group (Figure 3B). All parameters are summarized in Table 3.

**Table 3.**
 Parameters of the simulated cohort (Figure 3C).


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Explanation</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>σ2</td>
      <td>Magnitude of clone size fluctuations</td>
      <td>0.08/year</td>
    </tr>
    <tr>
      <td>d</td>
      <td>Death rate</td>
      <td>0.2/year</td>
    </tr>
    <tr>
      <td>γ</td>
      <td>Recruitment to proliferation ratio</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>θ</td>
      <td>Recruitment rate</td>
      <td>105/year</td>
    </tr>
    <tr>
      <td>p0,-</td>
      <td>Zero insertion fraction early in life</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>p0,+</td>
      <td>Adult zero insertion fraction</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>t†</td>
      <td>Time of recombination statistics switch</td>
      <td>0.05 years</td>
    </tr>
    <tr>
      <td>Ns⁢a⁢m⁢p⁢l⁢e</td>
      <td>Simulated sample size</td>
      <td>5 ⋅ 105</td>
    </tr>
  </tbody>
</table>
