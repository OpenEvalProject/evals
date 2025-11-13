# Combining mutation and recombination statistics to infer clonal families in antibody repertoires

## Authors

- Natanael Spisak<sup>1</sup> ([ORCID: 0000-0002-6332-047X](https://orcid.org/0000-0002-6332-047X))
- Gabriel Athènes<sup>1</sup> ([ORCID: 0009-0007-4668-884X](https://orcid.org/0009-0007-4668-884X))
- Thomas Dupic<sup>3</sup>
- Thierry Mora<sup>1</sup> ([ORCID: 0000-0002-5456-9361](https://orcid.org/0000-0002-5456-9361)) †
- Aleksandra M Walczak<sup>1</sup> ([ORCID: 0000-0002-2686-5702](https://orcid.org/0000-0002-2686-5702)) †

### Affiliations

1. Laboratoire de physique de l’École normale supérieure, CNRS, PSL University, Sorbonne Université and Université de Paris Paris France ([ROR:013cjyk83](https://ror.org/013cjyk83))
2. Saber Bio SAS, Institut du Cerveau, iPEPS The Healthtech Hub Paris France ([ROR:050gn5214](https://ror.org/050gn5214))
3. Department of Organismic and Evolutionary Biology, Harvard University Cambridge United States ([ROR:03vek6s52](https://ror.org/03vek6s52))

† Corresponding author

## Abstract

B-cell repertoires are characterized by a diverse set of receptors of distinct specificities generated through two processes of somatic diversification: V(D)J recombination and somatic hypermutations. B-cell clonal families stem from the same V(D)J recombination event, but differ in their hypermutations. Clonal families identification is key to understanding B-cell repertoire function, evolution, and dynamics. We present HILARy (high-precision inference of lineages in antibody repertoires), an efficient, fast, and precise method to identify clonal families from single- or paired-chain repertoire sequencing datasets. HILARy combines probabilistic models that capture the receptor generation and selection statistics with adapted clustering methods to achieve consistently high inference accuracy. It automatically leverages the phylogenetic signal of shared mutations in difficult repertoire subsets. Exploiting the high sensitivity of the method, we find the statistics of evolutionary properties such as the site frequency spectrum and dN/dS ratio do not depend on the junction length. We also identify a broad range of selection pressures spanning two orders of magnitude.

## Introduction

B cells play a key role in the adaptive immune response through their diverse repertoire of immunoglobulins (Ig). These proteins recognize foreign pathogens in their membrane-bound form (called B-cell receptor [BCR]), and battle them in their soluble form (antibody). Each B cell expresses a unique BCR that can bind their antigenic targets with high affinity. The set of distinct BCR harbored by the organism is highly diverse (Briney et al., 2019), thanks to two processes of diversification: V(D)J recombination and somatic hypermutation. These stochastic processes ensure that repertoires can match a variety of potential threats, including proteins of bacterial and viral origin that have never been encountered before.

V(D)J recombination takes place during B-cell differentiation (Hozumi and Tonegawa, 1976; Schatz and Swanson, 2011). For each Ig chain, V, D, and J gene segments for the heavy chain, and V and J gene segments for the light chain, are randomly chosen and joined with random non-templated deletions and insertions at the junction, creating a long, hypervariable region, called the complementarity determining region 3 (CDR3) (Figure 1A). Cells are subsequently selected for the binding properties of their receptors and against autoreactivity. At this stage, the repertoire already covers a wide range of specificities. In response to antigenic stimuli, B cells with the relevant specificities are recruited to germinal centers, where they proliferate and their Ig-coding genes undergo somatic hypermutation (Victora and Nussenzweig, 2022) in the process of affinity maturation. Somatic hypermutation consists primarily of point substitutions, as well as insertions and deletions, restricted to Ig-coding genes (Feng et al., 2020). The mutants are selected for high affinity to the particular antigenic target, and the best binders further differentiate into plasma cells and produce high-affinity antibodies. A more diverse pool of variants forms the memory repertoire, leaving an imprint of the immune response that can be recalled upon repeated stimulation.

![Figure 1.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig1-v2.jpg)

**Figure 1.:** Clonal families and $VJl$ classes.(A) Variable region of the immunoglobulin heavy chain (IgH)-coding gene. (B) A clonal family is a lineage of related B cells stemming from the same VDJ recombination event. The partition of the B-cell receptor (BCR) repertoire into clonal families is a refinement of the partition into $VJl$ classes, defined by sequences with the same V and J usage and the same complementarity determining region 3 (CDR3) length $l$. (C–D) Properties of $VJl$ classes in donor 326651 from Briney et al., 2019. (C) Distribution of $VJl$ class sizes exhibits power-law scaling. The total number of pairwise comparisons in the largest $VJl$ classes is $∼10^{5}^{2}=10^{10}$. (D) Distribution of the CDR3 length $l$. The distribution is in yellow for in-frame CDR3 sequences ($l$ multiple of 3), and in gray for out-of-frame sequences.

A clonal family is defined as a collection of cells that stem from a unique V(D)J rearrangement, and has diversified as a result of hypermutation, forming a lineage (Figure 1B). These families are the main building blocks of the repertoire. Since members of the same family usually share their specificities (De Boer et al., 2001), affinity maturation first competes families against each other for antigen binding in the early stages of the reaction, and then selects out the best binders within families in the later stages (Tas et al., 2016; Mesin et al., 2016).

High-throughput sequencing of single receptor chains offers unprecedented insight into the diversity and dynamics of the repertoire. Recent experiments have sampled the repertoires of the immunoglobulin heavy chain (IgH) of healthy individuals at great depth to reveal their structure (Briney et al., 2019). Disease-specific cohorts are now routinely subject to repertoire sequencing studies, which help to quantify and understand the dynamics of the B-cell response (Kreer et al., 2020; Nielsen et al., 2020).

Partitioning BCR repertoire sequence datasets into clonal families is a critical step in understanding the architecture of each sample and interpreting the results. Identifying these lineages allows for quantifying selection (Yaari and Uduman, 2012; Yaari and Kleinstein, 2015; Ruiz Ortega et al., 2023) and for detecting changes in longitudinal measurements (Nielsen et al., 2020; Turner et al., 2020). In recent years, many strategies have been developed that take advantage of CDR3 hypervariability (Abdollahi et al., 2020): it is generally unlikely that the same or a similar CDR3 sequence be generated independently multiple times (Elhanati et al., 2015; Ruiz Ortega et al., 2023). Other approaches make use of the information encoded in the intra-lineage patterns of divergence due to mutations (Briney et al., 2016; Nouri and Kleinstein, 2020). All inference techniques need to balance accuracy and speed. Simpler methods are fast but have low precision (also called positive predictive value) while more complex algorithms have long computation times that do not scale well with the number of sequences. This prohibits the analysis of recent large-scale data such as Briney et al., 2019.

In this work, we propose a new method for inferring clonal families from high-throughput sequencing data that is both fast and accurate. We use probabilistic models of junctional diversity to estimate the level of clonality in repertoire subsets, allowing us to tune the sensitivity threshold a priori to achieve a desired accuracy. We have developed two complementary algorithms. The first one (HILARy-CDR3) uses a very fast CDR3-based approach that avoids pairwise comparisons, while the second one (HILARy-full) additionally exploits information encoded in the phylogenetic signal outside of the junction. We compare our method with state-of-the-art approaches in a benchmark with realistic synthetic data.

## Results

### Analysis of pairwise distances within VJl classes

A common strategy for partitioning a BCR repertoire dataset into clonal families is to go through all pairs of sequences and identify pairs of clonally related sequences. In the following, we call such related pairs positive, and pairs of sequences belonging to different families negative. Then, the partition is built by single-linkage clustering, which consists of recursively grouping all positive pairs. Two characteristics of the repertoire complicate the search for this partition: large total number of pairs and low proportion of positive pairs. In this section we analyze and model the statistics of pairs of sequences in natural repertoires to inform our choice of the clustering method and parameters. In the next section we will leverage that analysis to design an optimized clustering procedure. To help following notations, a summary of their definitions is provided in Table 1.

**Table 1.**
 Summary of notations used throughout the paper.Hats ˆ denote estimates from the fit of the mixture model. Stars ∗ denote estimates after imposing 99% precision. The ‘post’ subscript denotes quantities after applying single-linkage clustering to obtain a partition from positive pairs.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ρ</td>
      <td>Prevalence/fraction of positive pairs</td>
    </tr>
    <tr>
      <td>π</td>
      <td>Precision = TP/(TP+FP)</td>
    </tr>
    <tr>
      <td>s</td>
      <td>Sensitivity = TP/(TP+FN)</td>
    </tr>
    <tr>
      <td>p</td>
      <td>Fallout = FP/(FP+TN)</td>
    </tr>
    <tr>
      <td>t</td>
      <td>Threshold on CDR3 distance</td>
    </tr>
    <tr>
      <td>l</td>
      <td>CDR3 length</td>
    </tr>
    <tr>
      <td>n</td>
      <td>CDR3 Hamming distance of a pair</td>
    </tr>
    <tr>
      <td>x</td>
      <td>Normalized CDR3 Hamming distance=l/n</td>
    </tr>
    <tr>
      <td>x′</td>
      <td>CDR3 Hamming distance, centered and scaled</td>
    </tr>
    <tr>
      <td>y′</td>
      <td>Shared mutations on V segment, centered and scaled</td>
    </tr>
    <tr>
      <td>μ</td>
      <td>Mean x between positive pairs</td>
    </tr>
    <tr>
      <td>PT</td>
      <td>Model distribution for positive pairs</td>
    </tr>
    <tr>
      <td>PF</td>
      <td>Model distribution for negative pairs</td>
    </tr>
  </tbody>
</table>

A pair of related sequences is expected to share the same V and J genes, as well as the same CDR3 length $l$, as determined by alignment to the templates (Figure 1A). The methods developed here begin by partitioning the data into $VJl$ classes, defined as subsets of sequences with the same V and J gene usage, and CDR3 length $l$ (Figure 1B). For a description of the data preprocessing and alignment to the V and J gene templates, see Methods. Clustering will then be performed within each $VJl$ class independently. While this first step severely limits the number of unnecessary comparisons, some $VJl$ classes still exceed 105 sequences in large datasets, leading to the order of 1010 pairs (see Figure 1C for the distribution of the $VJl$ class sizes $N$ for donor 326651 of Briney et al., 2019).

The CDR3 plays an important role in encoding the signature of the VDJ rearrangement. As we will see, the CDR3 length $l$ has a strong impact on the difficulty of clonal family reconstruction. The distribution of CDR3 lengths $l$ observed in the data is shown in Figure 1D. In what follows we restrict our analysis to sequences with CDR3 lengths a multiple of 3 and between 15 and 105, relying on the common approximation that sequences with no frameshift in the CDR3 come from a productive naive ancestor. The number of sequences with length larger than 105 is too small to reach meaningful conclusions, and sequences of length smaller than 15 are likely nonfunctional (as evidenced by the similar number of in-frame and out-of-frame sequences in Figure 1D).

In each $VJl$ class, we call prevalence and denote by $ρ$ the proportion of positive pairs, i.e., the number of positive pairs divided by the total number of pairs. This quantity is unknown in the absence of the ground-truth partition. However, we can estimate it from the statistics of pairwise distances. We compute the Hamming distance $n$ of each pair of CDR3s, defined as the number of positions at which the two nucleotide sequences differ. The distribution of these distances normalized by the CDR3 length, denoted by $x$, shows a clear bimodal structure in data (donor 326651 of Briney et al., 2019), with two identifiable components (Figure 2A): the contribution of positive pairs (of proportion $ρ$) peaks near $x=0$ and decays quickly, whereas the bell-shaped contribution of negative pairs (of proportion $1−ρ$) peaks around $x=1/2$.

![Figure 2.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig2-v2.jpg)

**Figure 2.:** (A) Example distribution of normalized Hamming distances, $x=n/l$, for one $VJl$ class with CDR3 length $l=21$, V gene IGHV3-9 and J gene IGHJ4 (black). We fit the distribution by a mixture of positive pairs (belonging to the same family, in blue) and negative pairs (belonging to different families, in red). See Figure 2—figure supplement 5 for example fit results across different CDR3 lengths. Inset: the prevalence is defined as a fraction of positive pairs and was estimated to $ρ^=3.1%$. Data from donor 326651 of Briney et al., 2019. (B) Distribution of the maximum likelihood estimates of prevalence $ρ^$ across $VJl$ classes in donor 326651. (C–F) The choice of threshold $t$ on the normalized Hamming distance $x$ translates to the following a priori characteristics of inference (illustrated here for arbitrarily chosen $ρ$ and $\mu$). (C) Fallout rate $p^(t)=FP^/(FP^+TN^)$. The null distribution of all negatives (N=FP + TN) is estimated using the soNNia sequence generation software. (D) Sensitivity $s^(t)=TP^/(TP^+FN^)$. (E–F) Precision $\pi^=TP^/(TP^+FP^)$. For the same choice of threshold $t$, a low prevalence of $ρ^=10^{−3}$ (E) leads to lower precision than high prevalence of $ρ^=10^{−1}$ (F). (G) Model distribution $P_{T}(x|\mu)$ of distances between unrelated sequences, for $l=15,30,45,60$, computed by the soNNia software. (H) Precision $\pi^$, computed a priori (i.e. before doing the inference) from the model with $\mu^=0.04$, $ρ^=0.1$, and $l=15,...,81$ (colors as in G), as a function of the threshold $t$. For each $VJl$ class and its own inferred $ρ^$ and $\mu^$, the threshold $t$ is chosen to achieve a desired $\pi^{∗}$. (I) High-precision threshold $t^{∗}$ ensuring $\pi^(t^{∗})=\pi^{∗}=99%$ a priori, as a function of CDR3 length $l$ for different values of the prevalence $ρ^$, and $\mu^=0.04$, as predicted by the model. (J) Sensitivity $s^(t^{∗})$ at the high-precision threshold $t^{∗}$, as a function of CDR3 length $l$ for different values of the prevalence $ρ^$ (colors as in I). Solid lines denote a priori prediction for intermediate mean distance $\mu=4%$, dashed lines denote actual performance of HILARy-CDR3 in a synthetic dataset.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Distribution of the maximum likelihood estimates of mean intra-family distance $\mu$ across $VJl$ classes.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Null distribution $P_{N}(x|l)$ of CDR3 distances between unrelated sequences for $l\in[15,81]$, computed by soNNia software.White line denotes a growing threshold ensuring a fallout rate $p<10^{−4}$ as determined by this distribution.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** $x=n/l$, for largest $VJl$ class for each CDR3 length $l=81$ (black). We fit the distribution by a mixture of positive pairs ($P_{T}(x|\mu)$ in blue), and negative pairs ($PN(x)$, in red). For $l=18$ the estimate $\mu^$ is too large results in large fitting error and for sensitivity computation we used global $\mu=4%$ (in green).

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** Ppost of CDR3 nucleotide sequences computed using soNNia across CDR3 lengths. Short junctions are on average more likely to be generated in VDJ recombination and pass subsequent selection (Isacchini et al., 2021). This makes inference in low-l classes more difficult, a feature reflected by synthetic dataset constructed by sampling unmutated lineage progenitors from the soNNia model.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** Site frequency spectra estimated for families identifed using high-precision CDR3-based inference method (HILARy-CDR3) in the subset of the data where this approach is highly reliable (large-﻿$l$ and large-$ρ^$ regime).The distributions are shown for families of varying family size, $z\in[10,100]$ and averaged over all families of a given size. Together with the exact configuration of sequences carrying a given substitution, synthetic datasets of the sames ignatures of mutations and clonal expansions can be generated.

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig2-figsupp6-v2.jpg)

**Figure 2—figure supplement 6.:** Distribution of normalized Hamming distances $x=n/l$, for $l$ classes, averaging over all $VJl$ classes.We fit the distribution by a mixture of positive pairs using a geometric distribution ($P_{T}(x|\mu)$ in blue), and negative pairs ($P_{N}(x)$, in red). The corresponding prevalence estimates $p^$ are used for small $VJl$ classes for which this parameter cannot be reliably estimated independently.

![Figure 2—figure supplement 7.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig2-figsupp7-v2.jpg)

**Figure 2—figure supplement 7.:** Prevalence and $VJl$ class size.Dependence of prevalence estimates on $VJl$ class size N for largest classes in donor 326651 from Briney et al., 2019. 28% of variation in prevalence estimates can be explained by variation in $VJl$ class sizes.

The prevalence $ρ$ can be formally written as $[Σ_{i}z_{i}(z_{i}−1)/2]/[N(N−1)/2]$, where $z_{i}$ denote the sizes of the clonal families in the $VJl$ class, but we do not know these sizes before the partition into families is found. To overcome this issue, we developed a method to estimate $ρ$ a priori, without knowing the family structure (Methods). We do this by fitting the empirical distribution of $x$ as a mixture model, $P(x)=ρ^P_{T}(x)+(1−ρ^)P_{F}(x)$, where $P_{T}(x)$ and $P_{F}(x)$ are the distributions of distances between positive (T as true) and negative (F as false) pairs (Figure 2C and D), estimated as follows. $P_{F}(x)=P_{F}(x|l)$ is computed for each length $l$ by generating a large number of unrelated, same-length sequences with the soNNia model of recombination and selection (Isacchini et al., 2021), and calculating the distribution of their pairwise distances (Methods). $P_{T}(x)$ is approximated by a Poisson distribution, $P_{T}(x)=(\mul)^{xl}e^{−\mul}/(xl)!$, with adjustable parameter $\mu$, which is proportional to the average hypermutation rate within the clone. The fit of $P(x)$ by the mixture model is performed for each $VJl$ class with an expectation-maximization algorithm which finds maximum likelihood estimates of the prevalence $ρ^$ and mean intra-family distance $\mu^$, the only free parameters of the mixture model.

The results of the fit to real data (donor 326651 of Briney et al., 2019) show that $\mu^$ varies little between $VJl$ classes, around $\mu^≃4%$ (Figure 2—figure supplement 1). In contrast, the prevalence $ρ^$ varies widely across classes, spanning three orders of magnitude (Figure 2B). In addition, when we examine the $VJl$ classes with increasing CDR3 length $l$, we find that the part of the model distribution corresponding to positive pairs, $P_{T}(x)$, varies little, whereas the model distribution over negative pairs $P_{F}(x)$ becomes more and more peaked around 1/2 (Figure 2 and Figure 2—figure supplement 2), making the two categories more easily separable.

### CDR3-based inference method with adaptive threshold

We want to build a classifier between positive and negative pairs using the normalized distance $x$ alone, by setting a threshold $t$ so that pairs are called positive if $x\leqt$, and negative otherwise. Using our model for $P(x)$, for any given $t$ we can evaluate the number of true positives ($TP^$) and false negatives ($FN^$) among all positive pairs ($P^=TP^+FN^$), as well as true negatives ($TN^$) and false positives ($FP^$) among the negative pairs ($N^=TN^+FP^$), as schematized in Figure 2—figure supplement 2C and D.

Our goal is to set a threshold $t$ that ensures a high precision, $\pi^(t)$, defined as a proportion of true positives among all pairs classified as positive (Figure 2E). In a single-linkage clustering approach, we will join two clusters with at least one pair of positive sequences between them. Therefore, it is critical to limit the number of false positives, which can cause the erroneous merger of large clusters. We can write:

$$
\pi^(t)≡\frac{TP^}{TP^+FP^}=\frac{ρ^s^(t)}{ρ^s^(t)+(1−ρ^)p^(t)},
$$



$$
p^(t)≡\frac{FP^}{N^}=\sumx\leqtP_{F}(x),
$$

and $s^(t)$ is the estimated sensitivity (Figure 2D), evaluated from the Poisson fit to $P_{T}$ (Methods):

$$
s^(t)≡\frac{TP^}{P^}=\sumx\leqtP_{T}(x)
$$

Finally, the estimated prevalence $ρ^≡P^/(P^+N^)$ is inferred from the $P(x)$ distribution as explained above.

Figure 2H shows $\pi^(t)$ as a function of $t$ for different CDR3 lengths and a fixed value of $ρ^$. For each $VJl$ class, we define the threshold $t=t^{∗}$ that reaches 99% precision, $\pi^(t^{∗})=\pi^{∗}=99%$, by inverting Equation 1. This adaptive threshold depends on the $VJl$ class through the CDR3 length $l$ and the prevalence $ρ$, and it increases with both (Figure 2I): low clonality (small $ρ$) means few positive pairs and a smaller adaptive threshold, while short CDR3 means less information and a stricter inclusion criterion.

The predicted sensitivity, $s^(t^{∗})$, which tells us how much of the positives we are capturing, is shown in Figure 2J. We conclude that for a wide range of parameters, the method is predicted to achieve both high precision and high sensitivity. However, it is expected to fail when the prevalence and the CDR3 length are both low. At the extreme, for small values $ρ$ and $l$, even joining together identical CDR3s ($t=0$) results in poor precision because of convergent recombination (reflected by $t^{∗}<0$).

The resulting procedure, which we call HILARy-CDR3, can be applied to Ig repertoire data through the following steps: (1) group sequences by $VJl$ class; (2) in each class, fit the mixture model to the distribution of pairwise distance to infer $ρ^$ and $\mu^$; (3) invert Equations 1–3 to find the high-precision threshold $t^{∗}$; (4) classify positive and negative pairs according to that threshold; (5) complete the partition by applying single-linkage clustering to positive pairs.

### Tests on synthetic datasets

So far we have presented a method to set a high-precision threshold with predictable sensitivity, based on estimates from the distribution of distances $P(x)$ only. To verify that these performance predictions hold in a realistic inference task, we designed a method to generate realistic synthetic datasets where the clonal family structure is known. This generative method will also be used in the next sections to create a benchmark for comparing different clustering algorithms.

We first estimated the distribution of clonal family sizes from the data of Briney et al., 2019, by applying HILARy-CDR3 with adaptive threshold as described above to $VJl$ classes for which the inference was highly reliable, i.e. for which the predicted sensitivity was $z\in[10,100]$. In that limit, clusters are clearly separated and the partition should depend only weakly on the choice of clustering method. The resulting distribution of clone sizes follows a power-law with exponent –2.3.

To create a synthetic lineage, we first draw a random progenitor using the soNNia model for IgH generation (Figure 2—figure supplement 4). We then draw the size of the lineage at random, using the power-law distribution above. Mutations are then randomly drawn on each sequence of the lineage in a way that preserves the mutation sharing patterns observed in families of comparable size from the partitioned data (Figure 2—figure supplement 5). We thus generated 104 lineages and 2.5 · 104 sequences. Note that, while that procedure is partially based on real data, in particular the distribution of lineage sizes and mutational co-occurence structure in the lineages, it uses completely random sequences and mutations. In addition, these empirical observables were inferred from $VJl$ classes that were easy to cluster, ensuring that they are not biased by our inference method, and therefore should not give it an unfair advantage. More details about the procedure are given in the Methods.

We applied the HILARy-CDR3 method to this synthetic dataset. The sensitivity achieved at $t^{∗}$ roughly follows and sometimes even outperforms the predicted one $s^(t^{∗})$ across different values of $ρ$ and $l$ (Figure 2J, dashed line), validating the approach and the choice of the adaptive high-precision threshold $t^{∗}$ (the discrepancy is due to the fact that $\mu$ is assumed to be constant in the prediction, while it varies in the dataset). These results also confirm the poor performance of the method at low prevalences and short CDR3s.

### Incorporating phylogenetic signal

To improve the performance of HILARy-CDR3, we set out to include the phylogenetic signal encoded in the mutation spectrum of the templated regions of the sequences. Two sequences belonging to the same lineage are expected to share some part of the mutational histories, and therefore sequences with shared mutations are more likely to be in the same lineage.

We focus on the template-aligned region of the sequence outside of the CDR3, where we can reliably identify substitutions with respect to the germline. We denote the length of this alignment by $L$, so that the total length of the sequence is $l+L$. For each pair of sequences, we define $n_{1},n_{2}$ as the number of mutations along the templated alignment in the two sequences, $n_{0}$ the number of mutations shared by the two, and $n_{L}=n_{1}+n_{2}−2n_{0}$ the number of non-shared mutations. Under the hypothesis of shared ancestry, the $n_{0}$ shared mutations fall on the shared part of the phylogeny, and are expected to be more numerous than under the null hypothesis of independent sequences, where they are a result of random co-occurrence (Figure 3A).

![Figure 3.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig3-v2.jpg)

**Figure 3.:** (A) For a pair of sequences, $n_{1},n_{2}$ denote the numbers of mutations along the templated region (V and J), and $n_{0}$ is the number of shared mutations. For related sequences, $n_{0}$ corresponds to mutations on the initial branch of the tree, and is expected to be larger than for unrelated sequences, where $n_{0}$ corresponds to coincidental mutations. (B) Positive and negative pairs are called mutated if both sequences have mutations $n_{1},n_{2}>0$. Among positive pairs in the synthetic datasets, more than 99% are mutated. (C, D) Distributions of the rescaled variables $x^{′}$ and $y$ (Equation 4), for pairs of synthetic sequences belonging to the same lineage (positive pairs) and sequences belonging to different lineages (negative pairs). The separatrix $x^{′}−y=t^{′}$ marks a high-precision (99%) threshold choice. (E) To limit the number of pairwise comparisons we make use of high-precision and high-sensitivity complementarity determining region 3 (CDR3)-based partitions. High precision corresponds to the choice $t=t^{∗}$. High sensitivity corresponds to a coarser partition where $t$ is set to achieve 90% sensitivity. When the two partitions disagree, mutational information can be used to break the coarse, high-sensitivity partition into smaller clonal families. (F, G) Mutations-based methods achieve high sensitivity across all CDR3 lengths $l$ in the synthetic dataset (G), extending the range of applicability with respect to the CDR3-based method (F).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Red circles represent clusters from the coarse (high-sensitivity) partition, while green clusters represent the fine (high-precision) partition. When the two partitions differ, HILARy-full merges precise clusters inside each sensitive cluster whenever there exists of pair of positive sequences linking them.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Error vs $VJl$ class size.We plot the fitting error of P(x) by the mixture model, for each $VJl$ class in the synthetic dataset, as a function of their sizes. The error is computed as the squared difference between the model and data distributions of distances.

To balance the tradeoff between the information encoded in the templated part of the sequence and the recombination junction, we can compute characteristic scales for the two variables of interest: the number of shared mutations and the CDR3 distance n. Intuitively, in highly mutated sequences, we can expect substantial divergence in the CDR3. At the same time, the number of mutations in the templated regions would increase, possibly leading to more shared mutations. Conversely, sequences with few or no mutations carry no information in the templated region, but we also expect their CDR3 sequences to be nearly identical. To adapt a clustering threshold to the two variables, we compute their expectations under the two assumptions, and define the rescaled variables

$$
x^{′}=\frac{n−⟨n⟩_{T}}{\sigma_{T}(n)},y=\frac{n_{0}−⟨n_{0}⟩_{F}}{\sigma_{F}(n_{0})},
$$

where $⟨n⟩_{T}=l(n_{L}+1)/L$ is the expected value of $n$ under the hypothesis that sequences belong to the same lineage (see Methods), and $⟨n_{0}⟩_{F}=n_{1}n_{2}/L$ is the expected value of $n_{0}$ under the hypothesis that they do not. The standard deviations are likewise defined as $\sigma_{T}(n)=\sqrt{⟨n^{2}⟩_{T}−⟨n⟩_{T}^{2}}=(1/L)\sqrt{l(l+L)(n_{L}+1)}$ and $\sigma_{F}(n_{0})=\sqrt{⟨n_{0}^{2}⟩_{F}−⟨n_{0}⟩_{F}^{2}}=\sqrt{n_{1}n_{2}/L}$ (Methods).

For more than 99% of positive pairs, both sequences are mutated, i.e., $n_{1},n_{2}>0$ (Figure 3B). Without loss of sensitivity, we focus on the mutated part of the dataset, since we cannot use $y$ for non-mutated sequences. The distributions of $x^{′}$ and $y$ for positive and negative pairs (Figure 3C and D) are well separated, with positive pairs characterized by an overrepresentation of shared mutations. By adding the phylogenetic signal $y$ we can identify positive pairs of sequences that have significantly diverged in their CDR3 ($x^{′}>0$) but share significantly more mutations than expected (large $y$).

Computing $y$ for each pair of sequences is computationally expensive. To avoid examining all pairs, we first perform two different nested clusterings of each $VJl$ class using the CDR3-based method: the previously described HILARy-CDR3 ‘fine’ partition with threshold $t^{∗}$ that ensures high precision $\pi^=99%$; and a ‘coarser’ clustering with a high threshold $t=t_{sens}$ that ensures high estimated sensitivity $s^=90%$ (Methods and Figure 3E). When lineages are easily separable (e.g. for sufficiently large prevalence $ρ$ and CDR3 length $l$), these two partitions coincide, and we do not need to compute $y$ at all. When they do not coincide, we can use the phylogenetic signal $y$ to refine the coarse high-sensitivity partition. We only need to compute $y$ for pairs that belong to the same coarse cluster, but not to the same fine cluster: the phylogenetic signal $y$ is used to merge the fine-partition clusters into clonal families (Methods and Figure 3—figure supplement 1). This allows us to considerably reduce the number of pairwise comparisons that we need to make between the templated regions of the sequences.

Using $x^{′}$ and $y$, we classify pairs of sequences as positive (i.e. belonging to the same family) if $y\geqx^{′}−t^{′}$, and as negative otherwise. We can compute the expected sensitivity on the synthetic data, and find that it reaches values ≥90% across the whole range of prevalence $ρ$ and CDR3 lengths $l$, outperforming HILARy-CDR3 in the low-$ρ$, low-$l$ region (Figure 3F and G). This proves that using the phylogenetic signal significantly improves performance over HILARy-CDR3.

The procedure outlined above, which we call HILARy-full, may be summarized as follows: (1) group sequences by $VJl$ class; (2) apply HILARy-CDR3 twice, once with the high-precision threshold as before to get a fine partition, and once with a high-sensitivity threshold to get a coarse partition, thus obtaining two nested partitions; (3) compute $x^{′}$ and $y$ using Equation 4 only for pairs that belong to the same coarse cluster but to different fine clusters; (4) merge all fine clusters with at least one pair with $y\geqx^{′}−t^{′}$.

### Benchmark of the methods on heavy-chain datasets

We compare our approach to state-of-the-art methods. In addition to our two algorithms—HILARy-CDR3 and HILARy-full—our benchmark includes the alignment-free method of Lindenbaum et al., 2021, partis (Ralph and Matsen, 2016), and the spectral clustering method of SCOPer (Nouri and Kleinstein, 2018). The SCOPer method using V and J gene mutations (Nouri and Kleinstein, 2020) was also tested, but gave worse results (Figure 4—figure supplement 1). Details about the used versions and parameters are referenced in the data availability section. We tested all algorithms on two synthetic datasets: a dataset simulated by the partis package and used in Ralph and Matsen, 2022, to benchmark partis against increasing levels of somatic hypermutations, and the synthetic data described above. That dataset is more realistic in the sense that it represents well the statistics of mutation patterns and, perhaps more importantly, the long-tail distribution of clone sizes observed in the data, with its large impact on the diversity of prevalences, which play an important role in the inference. The partis dataset is generated from a population genetics model. It provides a more independent test since it is not based on data used to develop the method and allows to study performance across different mutation rates.

First, we measure the inference time of each algorithm on our synthetic dataset. We find that the inference time is primarily affected by the size of the largest $VJl$ class. Therefore, we measure the inference time using the largest class found in donor 326651 of Briney et al., 2019, with the size of $N=1.2\times10^{5}$ unique sequences. We then apply the methods to a series of subsamples of this class to get the computational time as a function of the subsample size (Figure 4A). We only allowed for runtimes below 1 hr. We find that only three methods achieve satisfactory performance (under an hour): the two methods introduced here, and the alignment-free method. The other two methods, SCOPer and partis, are limited to $VJl$ classes of small size ($<10^{4}$ and $<10^{3}$, respectively).

![Figure 4.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig4-v2.jpg)

**Figure 4.:** (A) Comparison of inference time using subsamples from the largest $VJl$ class found in donor 326651 from Briney et al., 2019. Comparisons were done on a computer with 14 double-threaded 2.60 GHz CPUs (28 threads in total) and 62.7 Gb of RAM. (B) Clustering precision $\pi_{post}$ (post single-linkage clustering of positive pairs), (C) sensitivity $s_{post}$, and (D) variation of information $v$ as a function of complementarity determining region 3 (CDR3) length $l$ in the realistic synthetic dataset generated for this study. Solid lines represent the mean value averaged over five synthetic datasets. (E–G) Same as (B–D) but for the synthetic dataset from Ralph and Matsen, 2022, designed for the development and testing of the partis software. The solid lines represent the mean over the three datasets.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Comparison of inference time using subsamples from the largest $VJl$ class found in donor 326651 from Briney et al., 2019. Comparisons were done on a computer with 14 double-threaded 2.60GHz CPUs (28 threads in total) and 62.7Gb of RAM. (B) Clustering precision $\pi_{post}$ (post single linkage clustering of positive pairs), (C) Sensitivity $s_{post}$, and (D) variation of information υ vs CDR3 length $l$ in the realistic synthetic dataset generated for this study. Solid lines represent the mean value averaged over 5 synthetic datasets.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** We call this method VJCDR3-sim, where sim is the threshold on the normalized similarity between two CDR3s, equal to $1−x$, where $x$ is our normalized Hamming distance. (A) Clustering precision $\pi_{post}$ (post single linkage clustering of positive pairs), (B) sensitivity $s_{post}$, and (C) variation of information υ as a function of CDR3 length $l$ in the realistic synthetic dataset generated for this study. Solid lines represent the mean value averaged over 5 synthetic datasets. (D-F): Same than (A-C) using the synthetic data from Ralph and Matsen, 2022 and across mutation rates.

To compare the five algorithms in finite time, we test the accuracy of the methods using synthetic datasets with different CDR3 lengths, and with fixed mutation rate of 10% for the partis dataset (the mutation rate is not adjustable in our synthetic dataset as it mimics that of the data). We focus on short CDR3s, $l\in[15,45]$, which are the most challenging for lineage inference. Clonal families with longer CDR3s are easy to reconstruct, and simple methods such as single-linkage clustering with a threshold on mutational distance already work very well (Figure 4—figure supplement 2A–C). Each dataset contains 104 unique sequences, so that the dominant $VJl$ class is typically of size ∼103 and can be handled by all five algorithms. We measure performance using three metrics applied to the resulting partition: pairwise sensitivity $s_{post}$ (Figure 4B and E), pairwise precision $\pi_{post}$ (Figure 4C and F), and the variation of information $v$ (Figure 4D and G). Performance measures as a function of mutation rate in the partis dataset are presented in Figure 5. Pairwise sensitivity $s_{post}$ and precision $\pi_{post}$ are a posteriori analogs of the a priori estimates defined before in Equations 1 and 3, now computed after propagating links through the transitivity rule of single-linkage clustering. Their value reflects not only the accuracy of the adaptive threshold but is also affected by the propagation of errors in single-flinkage clustering. Variation of information is a global metric of clustering performance which measures the loss of information from the true partition to the inferred one, and is equal to zero for perfect inference and positive otherwise (Methods).

![Figure 5.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig5-v2.jpg)

**Figure 5.:** (A) Clustering precision $\pi_{post}$ (post single-linkage clustering of positive pairs), (B) sensitivity $s_{post}$, and (C) variation of information $v$ as a function of mutation rate, using the heavy chain only. Solid lines represent the mean value averaged over the three datasets.

Out of the five tested methods, only HILARy-full achieved both high sensitivity and high precision across all CDR3 lengths and for both synthetic datasets. HILARy-full is the only method reaching both high precision and sensitivity for CDR3s shorter than or equal to 30 nucleotides (Figure 4B), which corresponds to ∼10% of a typical repertoire of productive IgGs (Figure 7A, inset).

The HILARy-CDR3 method achieves high precision everywhere by construction, but only reached good sensitivity for CDR3 lengths 24 and above. The alignment-free method also achieves high precision everywhere, but with low sensitivity, meaning that it erroneously breaks up clonal families into smaller subsets. These three methods achieve good precision, thanks to the use of a null model for the negative pairs. On the contrary, SCOPer has excellent sensitivity everywhere but only achieves high precision for large lengths ($l>30$), suggesting that it erroneously merges short-CDR3 clonal families. Likewise, partis has high sensitivity but loses precision for short CDR3 on our realistic dataset, meaning that many clonal families are erroneously merged again. Note that our definition of precision and sensitivity differs from those used in Ralph and Matsen, 2022, which explains the differences between the performance measures reported here and in Ralph and Matsen, 2022. On the synthetic datasets from Ralph and Matsen, 2022, HILARy-full is the only method achieving high precision and sensitivity across mutation rates (Figure 5).

The variation of information offers a useful summary of the performance (Figure 4D and G and Figure 5C). According to that measure, only HILARy-full performs well across CDR3 lengths, mutation rates, and datasets. In particular, HILARy presents a clear advantage for challenging regions of the parameter space, such as CDR3 lengths below 30 nucleotides, and mutation rates of 20% and more.

For a typical repertoire, performance can be summarized into a global score by averaging over all CDR3 lengths in proportion of their abundance (assuming inference is perfect for CDR3 lengths larger than 45 regardless of the method). In this task, HILARy-full achieved 99.9% precision and 98.5% sensitivity; partis 93% and 96.9%; and SCOPer 96.6% and 99.1%. These scores are high because only a minority of lineages are difficult to infer. Nonetheless, HILARy-full provides a substantial gain in precision, while SCOPer presents a slight advantage in sensitivity.

We conclude that HILARy-CDR3 should be chosen for its consistently high sensitivity, specificity, and speed. In the case of the largest datasets, the faster HILARy-CDR3 is a useful alternative for long enough CDR3s in realistic repertoires.

### Extension to heavy- and light-chain paired data

We added an extension of HILARy to infer lineages from paired-chain repertoires, i.e., with paired light- and heavy-chain sequences. To extend HILARy-CDR3, we generalize the $VJl$ class to a  $V_{H}J_{H}V_{L}J_{L}l_{H+L}$ class, using the V and J genes from both the heavy and light chains, and the sum of their CDR3 lengths $l_{H+L}=l_{H}+l_{L}$. We then apply HILARy-CDR3 using the sum of the Hamming distances between the heavy- and light-chain CDR3s, normalized by $l_{H}+l_{L}$, as our new paired-chain $x$. The null distribution used is computed with soNNia using a default generation model for paired heavy and light chains. We incorporate the phylogenetic signal of both chains by concatenating their respective template genes, to obtain the total mutation counts $n_{0}=n_{0,H}+n_{0,L}$, and using $L$ as the sum of the lengths of the $V_{H}$ and $V_{L}$ genes.

In Figure 6A–C we compare our method to SCOPer and partis on the synthetic dataset from Ralph and Matsen, 2022, as a function of CDR3 length, as our method for generating synthetic sequences could not be easily extended to add random light chains. Performance comparison as a function of mutation rate is presented in Figure 6D–F. HILARy performs better than SCOPer and comparably to partis, which was designed and tested against this dataset.

![Figure 6.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig6-v2.jpg)

**Figure 6.:** (A) Clustering precision $\pi_{post}$ (post single-linkage clustering of positive pairs), (B) sensitivity $s_{post}$, and (C) variation of information $v$ as a function of complementarity determining region 3 (CDR3) length $l$, on the synthetic datasets from Ralph and Matsen, 2022, designed for the development and testing of the partis software. (D–F): Same as (A–C) but as a function of mutation rate.

### Inference of clonal families in a healthy repertoire

We next use our method to infer the clonal families of the heavy-chain IgG repertoires of healthy donors from Briney et al., 2019. Figure 7 summarizes key properties of the inferred clonal families of donor 326651. We take advantage of the consistency of our method across CDR3 lengths, as evidenced by the benchmark, to study how the lineage structure changes with the CDR3 length. To this end, we divide the dataset into nine quantiles, each containing ∼10% of the total number of sequences (Figure 7A, inset).

![Figure 7.](https://cdn.elifesciences.org/articles/86181/elife-86181-fig7-v2.jpg)

**Figure 7.:** Inference results for donor 326651 of Briney et al., 2019, are presented for nine quantiles of the CDR3 distribution, each containing between 8% and 12% of the total number of sequences (corresponding to nine colors in the inset of A). (A) Distributions of family size $z$. All CDR3 length quantiles exhibit universal power-law scaling with exponent −2.3. (B) Site frequency spectra estimated for families of sizes $z=100$. Families of larger sizes were subsampled to $z=100$ to subtract the influence of varying family sizes. (C) Distribution of lineage $d_{N}/d_{S}$ ratios computed for polymorphisms in CDR3 regions over all lineages within each nine quantile.

We find that across the nine subsets of the data, the statistics of the lineage structure inferred with the mutations-based method are largely universal. The distribution of the clonal family sizes $z$ (Figure 7A) follows a power law across all CDR3 lengths under study, with no significant differences between different lengths. This results generalizes an earlier observation used above for generating synthetic datasets, but which was restricted to high-$ρ^$, high-$l$ $VJl$ classes, and justifies a posteriori the use of a universal power law in the generative model.

For the largest families, of size $z\geq100$, we compute two intra-lineage summary statistics: the site frequency spectrum, which gives the distribution of frequencies of point mutations within lineages, and the distribution of $d_{N}/d_{S}$ ratios between non-synonymous and synonymous CDR3 polymorphisms within clonal families (estimated by counting). To avoid the bias of the varying family sizes, we subsampled all families to size $z=100$.

Under models of neutral evolution with fixed population size, the distribution of point-mutation frequencies $ν$ goes as $ν^{−1}$. Here, we observe a non-neutral profile of the spectrum, with an upturn at large allele frequencies $ν>0.5$ (Figure 7B). It is a known signature of selection or of rapid clonal expansion (Horns et al., 2019; Nourmohammad et al., 2019). We find that site frequency spectra are universal for all CDR3 lengths, suggesting that the dynamics that give rise to the structure of lineages and the subsequent dynamics that influence the sampling of family members do not depend on the CDR3 length.

The lineage $d_{N}/d_{S}$ ratio is also largely consistent across CDR3 lengths (Figure 7C), while spanning two orders of magnitude, suggesting a wide gamut of selection forces. We could have expected longer loops to be under stronger purifying selection (lower $d_{N}/d_{S}$) to maintain their specificity and folding. Instead, we observe that short CDR3s have more lineages with low $d_{N}/d_{S}$. This may be due to different sequence context and codon composition in short versus long CDR3s. Short junctions are largely templated, whereas long junctions have long, non-templated insertions, and it was shown that templated regions have evolved their codons to minimize the possibility of non-synonymous mutations (Saini and Hershberg, 2015), which would lead to a lower $d_{N}/d_{S}$, regardless of selection.

## Discussion

Clonal families are the building blocks of memory repertoire shaped by VDJ recombination and subsequent somatic hypermutations and selection. Repertoire sequencing datasets enable new approaches to understand these processes. They allow us to model the different sources of diversity and measure the selection pressures involved. To take full advantage of this opportunity, we need to reliably identify independent lineages.

Here, we introduced a general framework for studying the methods for partitioning high-throughput sequencing of BCR repertoire datasets into clonal families. We have identified the main factors that influence the difficulty of this inference task: low clonality levels and short recombination junctions. We quantified the clonality level using the definition of pairwise prevalence $ρ$ and introduced a method to estimate it a priori, without knowing the partition. We found the prevalence levels across $VJl$ classes to span three orders of magnitude (Figure 2B), unraveling the varying degree of complexity.

We leveraged the soNNia model of VDJ recombination to quantify the CDR3 diversity and constructed a null expectation for the divergence of independent recombination products. This null model enabled the design of a CDR3-based clustering method with an adaptive threshold, HILARy-CDR3, that allows us to keep the precision of inference high across prevalences and CDR3 lengths. Owing to the prefix tree representation of the CDR3 sequences, this method is characterized by very short inference times, thanks to avoiding all pairwise comparisons in single-linkage clustering. As expected, we found that the adaptive threshold choice limits the sensitivity of inference in the regime of short junctions and low prevalence (Figure 3F, below the black line).

To remedy the limitations of the CDR3-based approach, we developed a mutation-based method (HILARy-full). We found that including the phylogenetic signal of shared mutations in highly mutated sequences allows us to properly classify them into lineages despite significant CDR3 divergence. We studied the performance of the method using synthetic data and found significant improvement with respect to HILARy-CDR3: we extended the range of high-precision and high-sensitivity performance to cover all values of prevalence and CDR3 lengths observed in productive data (Figure 3G).

We have compared the two methods developed here with state-of-the-art approaches: the partis (Ralph and Matsen, 2016) and SCOPer (Nouri and Kleinstein, 2018) algorithms, and the alignment-free method (Lindenbaum et al., 2021). Compared to these methods, HILARy relies on a probabilistic model of VDJ recombination and selection, which allows it to explicitly control for precision. This is not possible in partis, which relies on likelihood ratio test to merge candidate clusters together to form families. SCOPer also chooses a clustering threshold based on the pairwise distribution of distances, but without a null model. Another innovation of HILARy-full is to use a null expectation for the number of shared mutations. This feature makes the method robust to varying levels of mutation rates across sequences. HILARy achieves optimal efficiency by combining CDR3-based and mutation-based information. Typically, a large part of the dataset doesn’t require the use of the full method, allowing for greatly reduced inference times. HILARy relies on the soNNia model, which is based on a neural network, and benefits from its expressivity to quantify the purifying selection that modifies the VDJ recombination statistics. We found the performance of this model satisfactory when applied to healthy memory repertoires, in agreement with previous findings (Isacchini et al., 2021; Ruiz Ortega et al., 2023). For subsets of the repertoire with less challenging characteristics, such as low mutation rates, long CDR3s, or high pairwise prevalence $ρ$, simpler methods can effectively reconstruct clonal families with high precision and sensitivity. As demonstrated in Balashova et al., 2024, single-linkage clustering outperforms state-of-the-art approaches for simulated samples based on real datasets with mutation rates ranging between 1.3% and 5.5%. As part of our clonal inference package, we provide our own implementation of single-linkage clustering based on mutational distance, which leverages a prefix tree representation method to speed up inference. We found this approach to be comparable to HILARy for long CDRs and low mutation rates (Figure 4—figure supplement 2).

Purifying selection is expected to be more pronounced in datasets of disease-specific cohorts and a default soNNia model may overestimate the diversity (Mayer and Callan, 2022) and lead to underestimation of the fallout rate. The inference framework introduced here could still be applied with more sophisticated models of selection, and take advantage of higher levels of clonality that characterize many disease-specific datasets (Nielsen et al., 2020; Turner et al., 2020).

We applied the mutations-based method to infer lineages in a repertoire of a healthy donor, sequenced at great depth (Briney et al., 2019). We took advantage of the consistency our method exhibits across CDR3 lengths to find that the statistics of lineages, including a heavy-tail distribution of family sizes as well as signatures of selection, are universal and independent of the CDR3 length. This result implies that the dynamics of expansion, mutation, and selection are independent of the CDR3 and suggests they are dictated by the rules of affinity maturation and memory formation rather than BCR specificity. It advocates for the use of RNA sequencing data to quantify these general principles (Mayer and Callan, 2022; Hoehn et al., 2019). Identifying clonal families with high accuracy is paramount in such approaches as it avoids the potential biases of different family sizes and varying levels of clonality.

The algorithm for clonal family identification presented here is a robust inference method that enables a reliable partition of a memory B-cell repertoire into independent lineages. Using synthetic datasets we demonstrated it is distinguished by consistently high precision and high sensitivity across different junction lengths and levels of clonality, while very fast compared to previous methods. It is therefore a useful tool to explore the diversity of the repertoires and improves our ability to interpret repertoire sequencing datasets.

## Methods

### Data preprocessing and alignment

We focus the analysis high-throughput RNA sequencing data of IgH-coding genes (Briney et al., 2019). The sequences were barcoded with unique molecular identifiers (UMIs) to correct for the PCR amplification bias and correct sequencing errors. We aligned raw sequences using presto of the Immcantation pipeline (Vander Heiden et al., 2014) with tools allowing for correcting errors in UMIs and deal with insufficient UMI diversity. Reads were filtered for quality and paired using default presto parameters. We selected only sequences aligned with the IgG primer and therefore the lineage analysis is limited to the IgG subset of the repertoire. Preprocessed data was then aligned to V, D, and J templates from IMGT (Giudicelli et al., 2006) database using IgBlast (Ye et al., 2013). After processing, all UMI count information is discarded and only unique nucleotide sequences are kept for further analysis.

Pairs of sequences stemming from the same VDJ recombination are expected to have the same CDR3 length $l$ and align to the same V and J templates. An exception could be caused by a insertion or deletion within the CDR3 that would alter its length as a result of the somatic hypermutation process. Such indel events are rare and generally selected against (Lupo et al., 2022), therefore in what follows we shall assume the effect of these events is negligible. The inference could also be affected by the misalignment of either V or J templates but we previously found the effect of alignment errors to be insignificant for identifying VJ classes (Spisak et al., 2020) (the alignment of the D template is error-prone and unreliable, hence not used in the inference procedure). Importantly, the two simplifications described here would result in decreased sensitivity of inference but are not expected to affect its precision.

### Modeling junctional diversity

The extraordinary diversity of VDJ rearrangements can be efficiently described and quantified using probabilistic models of the recombination process as well as subsequent purifying selection. Sequence-based models can assign to each receptor sequence $s$, its total probability of generation, $P_{gen}(s)$ (Murugan et al., 2012; Elhanati et al., 2015; Marcou et al., 2018) as well as a selection factor $Q(s)$, inferred so as to match frequencies $P_{data}(s)$ of the sequences with a model-based distribution (Elhanati et al., 2014; Sethna et al., 2020; Isacchini et al., 2021)

$$
P_{post}(s)=Q(s)P_{gen}(s).
$$

The $P_{gen}$ model was inferred using unmutated out-of-frame sequences from Briney et al., 2019, using the IGoR software (Marcou et al., 2018). The selection function $Q$ model was learned using unmutated productive IgM sequences from Briney et al., 2019, using the soNNia software (Isacchini et al., 2021).

The post-selection distribution $P_{post}$ describes the diversity of the CDR3 regions and in doing so provides an expectation of pairwise distances between unrelated, independently generated sequences of same length $l$ (Isacchini et al., 2021). As the soNNia software does not include somatic hypermutations, the underlying assumption is that additional diversity on the CDR3 caused by hypermutations doesn’t affect the distribution of pairwise distances. This assumption is justified by the quality of the fit. We can define

$$
P_{F}(n|l)=⟨\delta_{|s_{1}−s_{2}|,n}⟩_{s_{1},s_{2}∼P_{post}(⋅|l)},
$$

where $|s_{1}−s_{2}|$ stands for (Hamming) distance between sequences $s_{1}$ and $s_{2}$. This definition of the null distribution is a straightforward recipe for its estimation using (Monte Carlo) samples from $P_{post}$.

Should $P_{post}$ differ significantly from the empirical frequencies $P_{data}$ one can resolve to the following alternative

$$
P_{F}^{′}(n|l)=⟨\delta_{|s_{1}−s_{2}|,n}⟩_{s_{1}∼P_{post}(⋅,l),s_{2}∼P_{data}(⋅|l)},
$$

the equivalent of the negation distribution as defined in Lindenbaum et al., 2021, and used in our evaluation of the alignment-free method (Lindenbaum et al., 2021) in the method benchmark analysis.

### Estimation of pairwise prevalence

Pairwise prevalence is defined as the ratio of pairs of related sequences to the total number of pairs of sequences in a given set. Related sequences share an ancestor and have diverged by independent somatic mutations, post-recombination. Low prevalence can be a major difficulty for any inference procedure as any misassignment (or fallout) will result in a drastic loss of sensitivity or precision. It is instrumental to have an a priori estimate of pairwise prevalence before the families are identified.

To estimate the prevalence from the distribution of distances $P(n)$ for a given set of sequences (typically a $VJl$ class or $l$ class), we propose the following expectation-maximization procedure. We stipulate the distribution in question is a mixture distribution of two components, $P_{F}(n)$, the expectation for unrelated sequences defined as above, and $P_{T}(n)$, describing related sequences, modeled using a Poisson distribution

$$
P_{T}(n)=\frac{(\mul)^{n}}{n!}e^{−\mul},
$$

where μ is the mean divergence per base pair. If a particular CDR3 length $l$ is represented by unusually large number of $VJl$ classes, the resultant shape of the positive distribution is often closer to a geometric profile, and is then modeled using $P_{T}(n)=(1−M)M^{n}$, where $M=\frac{1}{1+\mul}$. In sum

$$
P(n)=ρP_{T}(n)+(1−ρ)P_{F}(n).
$$

In a standard fashion, we proceed iteratively by calculating the expected value of the log-likelihood (pairs of sequences indexed by i)

$$
Q(ρ,\mu|ρ_{t},\mu_{t})=\sumiP_{t}(i\inT)log⁡P_{T}(n_{i}|\mu)+P_{t}(i\inF)log⁡P_{F}(n_{i}),
$$

where the membership probabilities are defined as

$$
P_{t}(i\inT)=P(i\inT|n_{i},\mu_{t},ρ_{t})
$$



$$
=\frac{ρ_{t}P_{T}(x|\mu_{t})}{ρ_{t}P_{T}(x|\mu_{t})+(1−ρ_{t})P_{F}(x)}
$$



$$
 P_{t}(i\inF)=P(i\inF|n_{i},\mu_{0},ρ_{0})=1−P_{t}(i\inT).
$$

We then find the maximum

$$
\mu_{t+1},ρ_{t+1}=argmaxQ(ρ,\mu|ρ_{0},\mu_{0})
$$

and iterate the expectation and maximization steps until convergence, $|ρ_{t+1}−ρ_{t}|<ϵ$, to obtain $ρ^=ρ_{t+1}$.

Results for largest $VJl$ class within each $l$ class can be found in Figure 2—figure supplement 3 and results for $l$ classes using a geometric distribution can be found in Figure 2—figure supplement 6. Dependence of maximum likelihood prevalence estimates $ρ^$ on class size $N$ is plotted in Figure 2—figure supplement 7.

### HILARy-CDR3

The standard method for CDR3-based inference of lineages proceeds through single-linkage clustering with a fixed threshold on normalized Hamming distance divergence (fraction of differing nucleotides) (Kepler, 2013; Uduman et al., 2014; Yaari and Kleinstein, 2015; Nourmohammad et al., 2019). This crude method suffers from inaccuracy as it loses precision in the case of highly mutated sequences and junctions of short length (see Figure 4—figure supplement 2). If junctions are stored in a prefix tree data structure (Knuth, 2013) single-linkage clustering can be performed without comparing all pairs and hence is typically orders of magnitude faster than alternatives. The prefix tree is a search tree constructed such that all children of a given node have a common prefix, the root of the tree corresponding to an empty string, and leaves corresponding to unique sequences to be clustered. To find neighbors of a given sequence it suffices to traverse the prefix tree from the corresponding leaf upward and compute the Hamming distance at branchings. This method limits the number of unnecessary comparisons and greatly improves the speed of Hamming distance-based clustering (Boytsov, 2011). We implement the prefix tree structure to accommodate CDR3 sequences. Briefly, all the CDR3 sequences of identical length are stored in the leaves of a prefix tree (Navarro, 2001; Boytsov, 2011), implemented as a quaternary tree where each edge is labeled by a nucleobase (A, T, C, or G). The neighbors of a specific sequence are found by traversing the tree from top to bottom, exploring only the branches that are under a given Hamming distance from the sequence. Clusters are obtained by iterating this procedure and removing all the neighbors from the prefix tree until no sequences remain. The package is coded in C++ with a Python interface and is available independently. The time performance of this method for high-sensitivity and high-specificity partitions is studied as a part of the method benchmark analysis.

We take advantage of the speed of a prefix tree-based clustering to perform single-linkage clustering. Besides the algorithmic speed-up afforded by the prefix tree, the difference with previous methods is that we use an adaptive threshold. For any dataset, we define two CDR3-based partitions, high-sensitivity and high-precision clustering, corresponding to two choices of threshold.

The high-precision partition is obtained by setting the threshold $t$ to $t_{prec}^{∗}$ as the largest $t$ such $\pi^(t)\leq\pi^{∗}$, with $\pi^{∗}=0.99$ (99% precision), where $\pi^(t)$ is given by Equation 1–3. To get the high-sensitivity partition, we set the threshold to $t_{sens}^{∗}$, the smallest $t$ such that $s^(t)\geqs^{∗}$, where $s^{∗}=0.9$ (90% sensitivity), where $s^(t)$ is given by Equation 3.

We apply these thresholds to the single-linkage clustering described above to generate the precise and sensitive partitions, which are then used by the mutations-based method to find an optimal partition that merges the fine clusters within the coarse clusters (Methods and Figure 3—figure supplement 1). We refer to the high-precision partition from the CDR3 alone as HILARy-CDR3, and the mutation-based method as HILARy-full.

Finally, the structure of families leads to propagation of errors that lowers the precision with respect to the a priori estimate $\pi^$. Denoting family size as $z$, one error accounted for in $FP^$ causes, on average, $⟨z⟩^{2}−1$ extra errors by merging two families. If the a priori precision $\pi^$ is high, we can neglect the second order effect of these two families simultaneously affected by other $FP^$ pairs. Therefore the expected precision (Equation 1) of the resulting partition reads

$$
⟨\pi_{post}⟩≃\frac{1}{1+(⟨z⟩^{2}−1)(1−\pi^)}
$$

where we assumed $s^≃1$. For $\pi^=99%$ and $⟨z⟩≃2$ this formula gives $⟨\pi_{post}⟩≃97%$.

### Synthetic data generation

To generate synthetic data we make use of the statistics of tree topologies of the lineages identified in the high-sensitivity and high-precision regime of CDR3-based inference from the data (yellow region above the black line in Figure 3F). We denote the set of these lineages by $L$. We assume that to good approximation the mutational process and the selection forces that shaped the mutational landscape in these lineages do not depend on the CDR3 length.

To test the performance of different inference methods across CDR3 lengths, we build synthetic datasets of fixed length.

In the first step, we choose the number of families $N$. We then draw $N$ independent family sizes from the family size distribution of the form observed in healthy datasets

$$
p(z)=\frac{z^{−\alpha}}{Z_{\alpha}},
$$

where $Z_{\alpha}=\sumz\geq1z^{−\alpha}=ζ(\alpha,1)$. In the next step, we assign a naive progenitor to each lineage by sampling from the $P_{post}$ distribution, selecting sequences with a prescribed length $l$ (Figure 2—figure supplement 4). We then choose a lineage in the set of reconstructed lineages $L$ at random among lineages of size $z$ (or, for large sizes, the lineage of the closest size smaller than $z$). To create a lineage with the same mutation patterns as the real data, we then identify all unique mutations in the lineage from $L$ using standard alignment and tree recontruction methods described in Spisak et al., 2020, and for each mutation denote the labels of members of the lineage that carry it. For each mutation, this defines a configuration of labels, one of $2^{z}−1$ possible. We subsequently loop through observed configurations and choose new positions for all mutations to apply them to the synthetic progenitors of the ancestor, using the position- and context-dependent model of Spisak et al., 2020. The number of mutations assigned to a given configuration is rescaled by a factor $\frac{L+l}{L_{0}}$ where $L$ is the templated length of the synthetic ancestral sequence and $L_{0}$ is the templated length of the model lineage from $L$.

This way a synthetic lineage preserves all properties of the lineages of long CDR3s found in the data, particularly the mutational spectra (Figure 2—figure supplement 5) except for the ancestral sequences and the identity of mutations.

### HILARy-full

We compute the expected distributions of the CDR3 Hamming distance $n$, and the number of shared mutations $n_{0}$, under a uniform mutation rate assumption. In other words, we assume that the probability that a given position was mutated, given a mutation happened somewhere in a sequence of length $L$, equals $L^{−1}$ (we know this not to be true, see, e.g., Spisak et al., 2020, but it allows for simple computations). It follows that the probability that a given position has not mutated once in a series of $n$ mutations is $(1−L^{−1})^{n}$.

#### Expectation of n0 under the null hypothesis

For $n_{0}$ shared mutations, under the null hypothesis (we operate under the null hypothesis here since otherwise to estimate $n_{0}$ we would need to make assumptions about the law that governs B-cell phylogeny topologies), the likelihood reads

$$
P_{F}(n_{0}|n_{1},n_{2},L)=(\frac{L}{n_{0}})p^{n_{0}}(1−p)^{L−n_{0}},
$$

where the probability that the same position independently mutated in series of $n_{1}$ and $n_{2}$ mutations is

$$
p=(1−(1−L^{−1})^{n_{1}})(1−(1−L^{−1})^{n_{2}}).
$$

In the limit of large $L$, we have at leading order

$$
p=\frac{n_{1}n_{2}}{L^{2}},
$$



$$
P_{F}(n_{0}|n_{1},n_{2},L)≃(\frac{L}{n_{0}})(\frac{n_{1}n_{2}}{L^{2}})^{n_{0}}(1−\frac{n_{1}n_{2}}{L^{2}})^{L−n_{0}}≃\frac{(\frac{n_{1}n_{2}}{L})^{n_{0}}}{n_{0}!}e^{−\frac{n_{1}n_{2}}{L}},
$$

where the last approximation assumes $n_{1}n_{2}≪L^{2}$, which holds when mutation rates are small. Therefore, $P_{F}(n_{0}|n_{1},n_{2},L)$ may be approximated by a Poisson distribution of parameter $\frac{n_{1}n_{2}}{L}$, yielding:

$$
⟨n_{0}⟩_{F}≃\frac{n_{1}n_{2}}{L},\sigma_{F}(n_{0})≃\sqrt{\frac{n_{1}n_{2}}{L}}.
$$

#### Expectation of n under the hypothesis of related sequences

The $n$ divergence of two CDR3s is interpreted as divergent mutations under the hypothesis that $s_{1}$ and $s_{2}$ are related. These mutations were harbored in parallel with $n_{L}=n_{1}+n_{2}−2n_{0}$ mutations that occurred in the templated regions ($n_{0}$ mutations arrived before the divergence of the two sequences began).

Under the assumption of a uniform mutation rate, the $n_{L}$ mutations inform the prediction of the number of mutations expected in the CDR3. Indeed, they are related through a hidden variable, the expected number of mutations per base pair, denoted $\mu$. Integrating over this quantity we obtain

$$
P_{T}(n|n_{L},l,L)=\int_{0}^{∞}d\muP_{T}(n|\mu,l)P_{T}(\mu|n_{L},L),
$$

where we convolute the positive distribution (Equation 8),

$$
P_{T}(n|\mu,l)=\frac{(\mul)^{n}}{n!}e^{\mul}
$$

and, using the Bayes rule under uniform prior over $\mu$,

$$
P_{T}(\mu|n_{L},L)=L^{−1}P_{T}(n_{L}|\mu,L)=\frac{(\muL)^{n_{L}}}{n_{L}!L}e^{\muL}.
$$

The result is a negative binomial distribution,

$$
P_{T}(n|n_{L},l,L)=(\frac{L}{l+L})^{n_{L}+1}(\frac{l}{l+L})^{n}(\frac{n+n_{L}}{n}),
$$

with

$$
⟨n⟩_{T}=\frac{l}{L}(n_{L}+1),\sigma_{T}(n)=\frac{1}{L}\sqrt{l(l+L)(n_{L}+1)}.
$$

#### Merging fine-partition clusters

HILARy-full relies on the results (Equation 26) and (Equation 21) to define the rescaled variables (Equation 4)

$$
x^{′}=\frac{n−⟨n⟩_{T}}{\sigma_{T}(n)},y=\frac{n_{0}−⟨n_{0}⟩_{F}}{\sigma_{F}(n_{0})}.
$$

We expect $y≈0$, $x^{′}>0$ for unrelated sequences, and $x^{′}≈0$, $y>0$ for related sequences. So we expect $x^{′}−y>0$ for unrelated sequences, and $x^{′}−y<0$ for related sequences. We use $x^{′}−y$ as a distance for single-linkage clustering, with adaptive threshold to control performance. The threshold $t^{′}$ is chosen to achieve a desired precision of $\pi^{∗}=0.99$ as in HILARy-CDR3. To this end we use soNNia-based estimate of null distribution $P_{F}(n|l)$ (Equation 6), the data-derived distribution of the number of mutations, $P(n_{1})$, and further assume $n_{0}∼\frac{n_{1}n_{2}}{L}$ to compute the null distribution $P_{F}(x^{′}−y|l)$. We can now choose a target $\pi^{∗}$ and compute $t^{′}$ such that $\pi^(t^{′})=\pi^{∗}=0.99$ using Equations 1–3, the prevalence $ρ^$ inferred as explained earlier in the CDR3-based method, and assuming $s^≃1$. As the computation of $t^{′}$ depends on the inferred prevalence, we use this procedure only for $VJl$ classes with enough sequences for a reliable $ρ^$ (Figure 3—figure supplement 2), namely for sizes larger than 100. For smaller sizes the threshold was set to the default value of 0.

To reduce the number of pairwise computations, we do not apply single-linkage clustering directly, but instead merge fine-partition clusters within coarse-partition clusters, where the fine and coarse partitions were previously obtained using the CDR3-based method (see section HILARy-CDR3). Specifically, we compute $x^{′}−y$ for all pairs of sequences that belong to the same coarse cluster, but to different fine clusters. Two fine-partition clusters are then merged if there exist any two sequences belonging to each of the two clusters for which $x^{′}−y<t^{′}$. Note that this is equivalent to performing single-linkage clustering on all sequences using the distance $−∞$ for pairs inside a precise cluster and $x^{′}−y$ otherwise.

### Evaluation methods

In this section, we introduce the variation of information $v$, used for evaluating alternative methods for clonal family inference in the benchmark analysis. It is a useful summary statistic to quantify the performance of inference as it is affected by its precision as well as sensitivity (Brown et al., 2007). Variation of information $v(r,r^{∗})$ measures the information loss from the true partition $r^{∗}$ to the inference result $r$ (Zurek, 1989; Meilă, 2003). To define the variation of information we first introduce the entropy $S(r)$ of a partition $r$ of $N$ sequences into clusters $c$ as

$$
S(r)=−\sumc\inr\frac{n(c)}{N}log⁡\frac{n(c)}{N},
$$

where $n(c)$ denotes the number of sequences in cluster $c$. The mutual information between two partitions $r$ and $r^{∗}$ can then be computed as

$$
I(r,r^{∗})=\sumc\inr\sumc^{∗}\inr^{∗}\frac{n(c,c^{∗})}{N}log⁡\frac{n(c,c^{∗})}{N},
$$

where $n(c,c^{∗})$ denotes the number of overlapping elements between cluster $c$ in partition $r$ and cluster $c^{∗}$ in partition $r^{∗}$. Finally, variation of information is given by

$$
v(r,r^{∗})=S(r)+S(r^{∗})−2I(r,r^{∗}).
$$

Variation of information is a metric in the space of possible partitions since it is non-negative, $v(r,r^{∗})\geq0$, symmetric, $v(r,r^{∗})=v(r^{∗},r)$, and obeys the triangle inequality, $v(r_{1},r_{3})\leqv(r_{1},r_{2})+v(r_{2},r_{3})$ for any three partitions (Zurek, 1989).

### Code and data availability

We used version 1.2.0 for spectral SCOPer, 1.3.0 for SCOper using the V and J mutation presented in Figure 4—figure supplement 1, version 1.2.0 for HILARy, version 0.16.0 for partis, and the code from this repository https://bitbucket.org/kleinstein/projects/src/master/Lindenbaum2020/Example.ipynb for the alignment-free method. The HILARy tool with Python implementations of the CDR3 and mutation-based methods introduced above can be found at https://github.com/statbiophys/HILARy (copy archived at Athènes, 2024). The standalone prefix tree implementation can be found at https://github.com/statbiophys/ATrieGC (copy archived at Dupic, 2024). A complete guide to our benchmark procedure can be found in the README of the folder https://github.com/statbiophys/HILARy/tree/main/data_with_scripts where we make available scripts to infer lineages and reproduce the benchmark figures of this article. We also upload this folder with all input and output data at https://zenodo.org/records/10676371.
