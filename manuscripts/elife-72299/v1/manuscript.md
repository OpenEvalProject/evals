# A unified framework for measuring selection on cellular lineages and traits

## Authors

- Shunpei Yamauchi<sup>1</sup> ([ORCID: 0000-0002-8530-4147](https://orcid.org/0000-0002-8530-4147))
- Takashi Nozoe<sup>1</sup> ([ORCID: 0000-0003-2556-6484](https://orcid.org/0000-0003-2556-6484))
- Reiko Okura<sup>1</sup>
- Edo Kussell<sup>2</sup> ([ORCID: 0000-0003-0590-4036](https://orcid.org/0000-0003-0590-4036))
- Yuichi Wakamoto<sup>1</sup> ([ORCID: 0000-0002-6233-0844](https://orcid.org/0000-0002-6233-0844)) †

### Affiliations

1. Department of Basic Science, Graduate School of Arts and Sciences, The University of Tokyo Tokyo Japan ([ROR:057zh3y96](https://ror.org/057zh3y96))
2. Department of Biology, New York University New York United States ([ROR:0190ak572](https://ror.org/0190ak572))
3. Department of Physics, New York University New York United States ([ROR:0190ak572](https://ror.org/0190ak572))
4. Research Center for Complex Systems Biology, The University of Tokyo Tokyo Japan ([ROR:057zh3y96](https://ror.org/057zh3y96))
5. Universal Biology Institute, The University of Tokyo Tokyo Japan ([ROR:057zh3y96](https://ror.org/057zh3y96))

† Corresponding author

## Abstract

Intracellular states probed by gene expression profiles and metabolic activities are intrinsically noisy, causing phenotypic variations among cellular lineages. Understanding the adaptive and evolutionary roles of such variations requires clarifying their linkage to population growth rates. Extending a cell lineage statistics framework, here we show that a population’s growth rate can be expanded by the cumulants of a fitness landscape that characterize how fitness distributes in a population. The expansion enables quantifying the contribution of each cumulant, such as variance and skewness, to population growth. We introduce a function that contains all the essential information of cell lineage statistics, including mean lineage fitness and selection strength. We reveal a relation between fitness heterogeneity and population growth rate response to perturbation. We apply the framework to experimental cell lineage data from bacteria to mammalian cells, revealing distinct levels of growth rate gain from fitness heterogeneity across environments and organisms. Furthermore, third or higher order cumulants’ contributions are negligible under constant growth conditions but could be significant in regrowing processes from growth-arrested conditions. We identify cellular populations in which selection leads to an increase of fitness variance among lineages in retrospective statistics compared to chronological statistics. The framework assumes no particular growth models or environmental conditions, and is thus applicable to various biological phenomena for which phenotypic heterogeneity and cellular proliferation are important.

## Introduction

Growth rates of cellular populations are physiological quantities directly linked to the fitness of cellular organisms. To understand the roles of biological processes and reactions within cells, including modulation of gene expression and metabolic states, one must characterize how they are eventually channeled into an increase or maintenance of population growth rates.

As documented by many single-cell studies, phenotypic states of individual cells in cellular populations are heterogeneous and often correlate with fitness variations among cellular lineages (Balázsi et al., 2011; Elowitz et al., 2002; Kelly and Rahn, 1932; Powell, 1956; Wakamoto et al., 2005; Wang et al., 2010; Cerulus et al., 2016; Susman et al., 2018). Fitness heterogeneity within a population causes a statistical bias on ancestral cells’ contributions to the number of descendants, which is broadly referred to as ‘selection’ (Leibler and Kussell, 2010). Such bias from growth heterogeneity makes the relations between cellular lineages and populations nontrivial. For example, an intriguing consequence of intra-population selection is a growth rate gain, a phenomenon that cell population’s growth rate becomes greater than the mean division rate of isolated single-cell lineages (Powell, 1956; Hashimoto et al., 2016; Rochman et al., 2018). Recent progress of single-cell measurements has enabled high-throughput acquisitions of cellular lineage trees and historical dynamics in each lineage (Stewart et al., 2005; Wang et al., 2010; Hashimoto et al., 2016). However, establishing the theory and method of cellular lineage statistics to quantify fitness differences among different phenotypic states and intrapopulation selection is still in progress (Nozoe et al., 2017; García-García et al., 2019; Levien et al., 2020; Genthon and Lacoste, 2020; Genthon and Lacoste, 2021).

Growth of cellular populations can be described using the ensemble of individual cells’ growth histories (Leibler and Kussell, 2010). A theoretical approach that regards a cell lineage (history) as a basic unit of analysis has offered illuminating insights into population dynamics. For example, it has provided the formula for untangling selection from responses (Leibler and Kussell, 2010), population response to age-specific changes in mortality and fecundity (Wakamoto et al., 2012), fluctuation relations of fitness (Kobayashi and Sughiyama, 2015; Genthon and Lacoste, 2020), and relations between cell size growth rate and population growth rate (Thomas, 2007; Lin and Amir, 2017).

Employing this cell history-based formulation of population dynamics, we have previously proposed a method of cellular lineage statistics that allows quantification of fitness landscapes and selection strength for any traits of cellular lineages (Nozoe et al., 2017). Here, we extend this statistical framework and show that population growth rates can be expanded by the cumulants that represent various properties of fitness distributions, such as variance and skewness, in a population. We apply the framework to experimental single-cell lineage data of bacteria, yeast, and mammalian cells to quantify their condition-dependent growth heterogeneity and its contribution to population growth rate. We also apply this framework to measuring the fitness landscapes for a growth-regulating sigma factor in E. coli and identify the conditions where its continuum and non-genetic expression heterogeneity correlates with lineage fitness in cellular populations.

### Examples of biological questions

Before detailing the theoretical and experimental results, we first present several biological questions for which cell lineage statistics could provide essential insights.

### Growth rate gain

Growth of individual cells is heterogeneous in a cellular population even under constant environmental conditions (Stewart et al., 2005; Wakamoto et al., 2005; Wang et al., 2010; Hashimoto et al., 2016). Whether genetic or non-genetic, such growth heterogeneity inevitably enables selection within a cellular population. Growth heterogeneity can increase the rate of a population’s growth compared to the mean replication (division) rate of individual cells, known as ‘growth rate gain’ (Hashimoto et al., 2016). Since population growth rate is one of the critical quantities that determine long-term evolutionary success, it is interesting to ask to what extent growth heterogeneity contributes to population growth rate and how the contributions change depending on cellular phenotypes, genotypes (e.g. species), and environmental conditions. Answering this question may uncover strategies of each organism regarding how it exploits inherent stochasticity for population growth.

As we detail below, a measure of selection strength, $S_{KL}^{(1)}⁢[D]$, can quantify the growth rate gain from growth heterogeneity. Furthermore, we show that one can quantitatively decompose $S_{KL}^{(1)}⁢[D]$ into the contributions of distinct characteristics of growth heterogeneity, such as variance and skewness of fitness distributions. In this study, we apply the cell lineage statistics framework to single-cell lineage data and unravel how the growth rate gain changes across environments and organisms.

### Selection in changing environments

When a population of cells faces environmental changes, response of individual cells can be uniform and heterogeneous (Lambert et al., 2014; Julou et al., 2020). In one scenario, individual cells might respond to an environmental change uniformly and contribute to the future population nearly equally with respect to the number of descendants. In another scenario, only a tiny fraction of the cell population could respond to an environmental change, and the descendants of the responders might dominate the entire future population. In this case, the selection within a population is intense, and the nature of a population’s response exclusively depends on these rare cell lineages. Typically, the responses of real cell populations would fall between these two extremes; it is therefore critical to ask how strongly selection occurs within cellular populations in response to environmental changes to understand their response and adaptation strategies.

The framework enables such quantification by evaluating the selection strength $S_{KL}^{(1)}⁢[D]$ of responding cell populations. Importantly, quantifying the selection strength $S_{KL}^{(1)}⁢[D]$ requires only the information of division counts in cellular lineages. Hence, the selection strength is measurable even for complex processes where clarifying the transitions of environmental conditions around cells is technically challenging. We indeed analyze cellular populations of E. coli regrowing from an early or late stationary phase and characterize distinct levels of selection depending on the duration of stationary phase.

### Correlations between cellular lineage traits and fitness

Since various traits of individual cells, such as expression levels of particular genes (Elowitz et al., 2002), are heterogeneous in cellular populations, it is natural to ask how strongly trait heterogeneity correlates with the fitness of individual cell lineages. Quantifying such correlations will allow us to understand which traits are under strong selection and potentially crucial for long-term evolution.

The cell lineage statistics framework quantifies relationships between traits and fitness using fitness landscapes $h⁢(x)$. Additionally, the overall correlation between the heterogeneity of traits and that of fitness can be quantified by the relative selection strength $S_{rel}⁢[X]$. In this study, we measure $h⁢(x)$ and $S_{rel}⁢[X]$ for a growth-regulation sigma factor in E. coli to unravel whether its continuum expression level heterogeneity is correlated with the fitness heterogeneity of single cell lineages.

Clarifying trait and fitness correlations based on individual-cell-based analyses is difficult when growth and traits fluctuate rapidly over time and when the traits affect growth with delays. In such circumstances, instantaneous correlations between traits and growth might not report their relations correctly. On the other hand, the cell-lineage-based analysis of this framework can take the whole dynamics of traits in cell lineages into account. For example, if we expect that absolute expression levels are important for fitness, the expression level averaged in each cell lineage can be employed as the lineage trait, and its fitness landscape and selection strength are measurable. If large fluctuations affect cell fates and contribute to diversification of cell lineage fitness within a cellular population (Purvis and Lahav, 2013), the variances of expression levels can be taken as lineage traits, and one can evaluate their fitness landscape $h⁢(x)$ and relative selection strength $S_{rel}⁢[X]$. Therefore, the assumption of a cell lineage as a unit of selection can significantly extend the choice of traits, including time-dependent properties, and can provide insights into cellular dynamics that cannot be gained without the lineage-based formulation of fitness and selection.

### Theoretical background

First, we briefly review the analytical framework of cell lineage statistics introduced in Nozoe et al., 2017. This framework allows us to quantitatively infer fitness differences associated with distinct states of cellular lineage traits and selection within a growing cell population from empirical single-cell lineage tree data. Time-lapse single-cell measurements provide cellular growth and division information in the form of lineage trees (Figure 1, Stewart et al., 2005). We regard a lineage $\sigma$ as a cell history traceable back from a descendant cell at the final time point $t=\tau$ (Figure 1B). For the case of cellular growth shown in Figure 1A, 22 cell lineages exist in the trees.

![Figure 1.](https://cdn.elifesciences.org/articles/72299/elife-72299-fig1-v1.jpg)

**Figure 1.:** (A) Time-lapse images of a growing microcolony of Escherichia coli expressing green fluorescent protein (GFP) from plasmids. Scale bars, 5 μm. (B) Cellular lineage trees for the microcolony in A. Bifurcations in the trees represent cell divisions. $\sigma$ denotes cell lineage labels. $D⁢(\sigma)$ shows the number of cell divisions in each lineage. $P_{cl}⁢(\sigma)$ and $P_{rs}⁢(\sigma)$ are chronological and retrospective probabilities defined in the main text.

We assign two types of probability weight to cellular lineages. One is retrospective probability, in which we assign equal weight $P_{rs}(\sigma):=1/N_{\tau}$ to all lineages, where $N_{\tau}$ is the number of cells at the final time point $t=\tau.P_{rs}(\sigma)$ represents the probability of selecting the history of a cell present at the endpoints of lineage trees. Another is chronological probability, in which we assign the weight $P_{cl}(\sigma):=2^{−D(\sigma)}/N_{0}$ to the lineages, where $D⁢(\sigma)$ is the number of cell divisions on lineage $\sigma$ and N0 is the initial number of cells at $t=\tau.P_{cl}(\sigma)$ represents the probability of choosing lineage $\sigma$ descending the tree from one of the ancestor cells at $t=0$ and selecting one branch with the probability $1/2$ at every cell division. $P_{rs}⁢(\sigma)$ and $P_{cl}⁢(\sigma)$ can be different in general when the number of cell divisions are variable among the cell lineages, as shown in Figure 1B.

We define retrospective and chronological probabilities for a lineage trait $X$ as $Q_{rs}(x):=\sum\sigma:X(\sigma)=xP_{rs}(\sigma)$ and $Q_{cl}(x):=\sum\sigma:X(\sigma)=xP_{cl}(\sigma)$, where $X⁢(\sigma)$ is the value of trait $X$ for lineage $\sigma$. Here, we regard any measurable quantity associated with cellular lineages as a lineage trait $X$. For example, time-averaged expression levels and production rates of a drug-resistance protein were analyzed as lineage traits in the experiments of Nozoe et al., 2017. Intuitively, $Q_{cl}⁢(x)$ and $Q_{rs}⁢(x)$ represent the probabilities of finding the lineage trait value $X=x$ before and after selection, respectively.

Using these retrospective and chronological distributions, we define the fitness landscape for lineage trait $X$ as

$$
h(x):=\tauΛ+ln⁡\frac{Q_{rs}(x)}{Q_{cl}(x)},
$$

where $Λ:=\frac{1}{\tau}ln⁡\frac{N_{\tau}}{N_{0}}$ is the population growth rate. This definition relates the relative difference of the retrospective probability from the chronological probability to fitness. $h⁢(x)$ becomes greater than $\tau⁢Λ$ if the lineage trait state $X=x$ is overrepresented in the retrospective probability relative to chronological probability and vice versa. Furthermore, if none of the states of lineage trait $X$ are overrepresented nor underrepresented, $h⁢(x)$ becomes constant across the states and equals $\tau⁢Λ$ for all $x$. The fitness landscape $h⁢(x)$ thus represents fitness differences mapped on the lineage trait space of $X$ (see Figure 2 and Box 1).

![Figure 2.](https://cdn.elifesciences.org/articles/72299/elife-72299-fig2-v1.jpg)

**Figure 2.:** (A) Non-uniform fitness landscape and broad trait distribution. The gray distribution represents a chronological distribution of lineage trait $x$; the cyan distribution represents a retrospective distribution of lineage trait $x$; and the black dashed line represents a fitness landscape. Due to the non-uniform fitness landscape and the broad chronological distribution, there is trait fitness heterogeneity for selection to act on. The retrospective distribution therefore shifts significantly from the chronological distribution, and the selection strength is large ($S[X]>0$). (B) Non-uniform fitness landscape and narrow trait distribution. Due to the lack of trait heterogeneity, there is little fitness heterogeneity for selection to act on. The retrospective distribution shifts only slightly from the chronological distribution, and the selection strength is small ($S⁢[X]≈0$). (C) Uniform fitness landscape. When the fitness landscape is constant ($=\tau⁢Λ$) across the lineage trait state $x$, there can be no trait fitness heterogeneity regardless of whether the trait distribution itself is narrow or broad. The selection strength is therefore zero ($S⁢[X]=0$).

One can also define ‘selection strength’ using $Q_{rs}⁢(x)$ and $Q_{cl}⁢(x)$ as

$$
S_{JF}[X]:=J[Q_{cl}(X),Q_{rs}(X)]=⟨h(X)⟩_{rs}−⟨h(X)⟩_{cl},
$$

where $J[Q_{cl}(X),Q_{rs}(X)]:=\sumx(Q_{cl}(x)−Q_{rs}(x))ln⁡\frac{Q_{cl}(x)}{Q_{rs}(x)}$ is Jeffreys divergence, and $⟨h(X)⟩_{rs}:=\sumxh(x)Q_{rs}(x)$ and $⟨h(X)⟩_{cl}:=\sumxh(x)Q_{cl}(x)$ are the retrospective and chronological mean fitness for lineage trait $X$. Jeffreys divergence measures dissimilarity between two probability distributions. Therefore, $S_{JF}⁢[X]$ measures dissimilarity between the chronological and retrospective distributions caused by selection. Notably, one can link this dissimilarity to the difference in the mean fitness, as shown in Equation 2. Since Jeffreys divergence is non-negative, the retrospective mean fitness (mean fitness after selection) is equal to or greater than the chronological mean fitness (mean fitness before selection).

This measure of selection strength quantifies how strongly differences in the states of lineage trait $X$ correlate with the differences in lineage fitness. Therefore, one can unravel which traits correlate with lineage fitness strongly by evaluating this for traits of interest.

Likewise, we can define two alternative selection strength measures:

$$
S_{KL}^{(1)}[X]:=D_{KL}[Q_{cl}(X)||Q_{rs}(X)]=\tauΛ−⟨h(X)⟩_{cl},
$$



$$
S_{KL}^{(2)}[X]:=D_{KL}[Q_{rs}(X)||Q_{cl}(X)]=⟨h(X)⟩_{rs}−\tauΛ,
$$

where $D_{KL}[Q_{cl}(X)||Q_{rs}(X)]:=\sumxQ_{cl}(X)ln⁡\frac{Q_{cl}(X)}{Q_{rs}(X)}$ and $D_{KL}[Q_{rs}(X)||Q_{cl}(X)]:=\sumxQ_{rs}(X)ln⁡\frac{Q_{rs}(X)}{Q_{cl}(X)}$ are the Kullback-Leibler divergence of the two distributions. Note that $S_{KL}^{(1)}⁢[X]+S_{KL}^{(2)}⁢[X]=S_{JF}⁢[X]$.

These three types of selection strength measures share identical properties in common: they are always non-negative and report the overall correlations between trait states and fitness. We exclusively used $S_{JF}⁢[X]$ as the selection strength measure in our previous study (Nozoe et al., 2017). However, $S_{KL}^{(1)}⁢[X]$, $S_{KL}^{(2)}⁢[X]$, and their difference $S_{KL}^{(2)}⁢[X]-S_{KL}^{(1)}⁢[X]$ possess their own unique biological meanings, as we detail in Results. We indeed evaluate both $S_{KL}^{(1)}⁢[X]$ and $S_{KL}^{(2)}⁢[X]$ for the empirical lineage data of various organisms and use them to unravel distinct effects of selection on fitness variances. Such meanings and roles of the different selection strength measures are clarified in this study.

Importantly, division count $D$ is also a lineage trait, and its selection strength sets the maximum bound for the selection strength of any lineage trait irrespectively of a choice of the selection strength measures as discussed in Appendix 3. Therefore, the selection strength relative to that of $D$ is bounded between 0 and 1 and evaluates how strongly the heterogeneity of $X$ correlates with the division count heterogeneity in a given cellular population. This relative measure is useful when comparing relative strength of correlations between lineage traits and fitness across conditions. In this study, we define relative selection strength as

$$
S_{rel}[X]:=\frac{S_{KL}^{(1)}[X]}{S_{KL}^{(1)}[D]},
$$

and use it in the analysis.

All of the quantities introduced above are measurable without relying on any growth models. Thus, this cell lineage statistics framework is applicable to a wide range of single-cell lineage data.

## Results

### Growth rate gain and cumulant expansion of population growth rate

To quantify contributions of growth heterogeneity to population growth, we first rewrite the definition of the selection strength $S_{KL}^{(1)}⁢[X]$ (Equation 3) as follows:

$$
\tau⁢Λ=⟨h⁢(X)⟩_{cl}+S_{KL}^{(1)}⁢[X].
$$

This shows that population growth rates can be decomposed into chronological mean fitness and selection strength. In particular, when we take division count $D$ as a lineage trait, its fitness landscape is $h~⁢(d)=d⁢ln⁡2$ (Appendix 3), and $⟨h~⁢(D)⟩_{cl}/\tau$ represents the mean division rate of cellular lineages without selection. $S_{KL}^{(1)}⁢[D]/\tau$, thus, represents growth rate gain caused by the growth heterogeneity among the cellular lineages in a cellular population. Therefore, evaluating $S_{KL}^{(1)}⁢[D]/\tau⁢Λ$ from single-cell lineage data provides information on the contribution of growth heterogeneity to population growth.

To further examine the connections between the disparate selection measures and elucidate their meaning, we define a function of a variable $ξ$ as

$$
K_{X}(ξ):=ln⁡⟨e^{ξh(X)}⟩_{cl}=ln⁡\sumxe^{ξh(x)}Q_{cl}(x).
$$

This is the cumulant generating function (cgf) of $h⁢(x)$ with respect to the chronological distribution $Q_{cl}$. We have $K_{X}⁢(0)=0$, and from the definition of fitness landscape $h⁢(x)$ (Equation 1), we find

$$
K_{X}⁢(1)=\tau⁢Λ.
$$

When the radius of convergence of the Taylor expansion of $K_{X}⁢(ξ)$ around $ξ=0$ is at least 1, $K_{X}⁢(1)$ can be expressed as the series using the cumulants of a fitness landscape as

$$
K_{X}(1)=\sumn=1∞\frac{κ_{n}^{(X)}}{n!},
$$

where $κ_{n}^{(X)}:=\frac{d^{n}K_{X}(ξ)}{dξ^{n}}|_{ξ=0}$ is the $n$-th order cumulant, satisfying $κ_{1}^{(X)}=⟨h⁢(X)⟩_{cl}$, and $κ_{2}^{(X)}=Var⁢[h⁢(X)]_{cl}=⟨h⁢(X)^{2}⟩_{cl}-⟨h⁢(X)⟩_{cl}^{2}$. Hence,

$$
\tauΛ=\sumn=1∞\frac{κ_{n}^{(X)}}{n!},
$$

which shows that population growth rates can be expanded by the cumulants of a fitness landscape for any lineage trait $X$. Additionally, since $κ_{1}^{(X)}=⟨h⁢(X)⟩_{cl}$, comparing (Equation 8) and (Equation 12) yields

$$
S_{KL}^{(1)}[X]=\sumn=2∞\frac{κ_{n}^{(X)}}{n!}.
$$

Therefore, $S_{KL}^{(1)}⁢[X]$ represents the total contribution of second and higher order cumulants to population growth.

The cumulant expansion allows us to quantify the relative contributions of various statistical features of fitness distributions to population growth, such as mean, variance, and skewness. We define the cumulative contribution up to the $n$-th order cumulant as

$$
W_{n}^{(X)}:=\frac{1}{\tauΛ}\sumk=1n\frac{κ_{k}^{(X)}}{k!},
$$

and note that $W_{n}^{(X)}$ converges to 1 as $n→∞$. In particular, $W_{1}^{(X)}=\frac{⟨h⁢(x)⟩_{cl}}{\tau⁢Λ}$ and $W_{2}^{(X)}=\frac{1}{\tau⁢Λ}⁢(⟨h⁢(X)⟩_{cl}+\frac{1}{2}⁢Var⁢[h⁢(X)]_{cl})$. We will indeed measure $W_{n}^{(D)}$ for various cellular species under steady and non-steady environments in the experimental sections below.

The function $K_{X}⁢(ξ)$ defined in (Equation 9) is useful as it provides various forms of fitness and selection measures by simple algebraic calculation, as shown in Table 1. In general, evaluating $K_{X}⁢(ξ)$ and its derivatives at $ξ=0$ and $ξ=1$ gives the information of chronological and retrospective statistics, respectively (Appendix 3). Therefore, $K_{X}⁢(ξ)$ contains complete information on the fitness distributions in both chronological and retrospective statistics.

**Table 1.**
 Relationships between $K_{X}⁢(ξ)$ and quantities in cellular lineage statistics.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Quantities in lineage statistics</th>
      <th>Symbol</th>
      <th>Correspondence to KX⁢(ξ)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Fitness</td>
      <td>Population growth</td>
      <td>τ⁢Λ</td>
      <td>KX⁢(1)</td>
    </tr>
    <tr>
      <td></td>
      <td>Chronological mean fitness</td>
      <td>⟨h⁢(X)⟩cl</td>
      <td>KX′⁢(0)</td>
    </tr>
    <tr>
      <td></td>
      <td>Retrospective mean fitness</td>
      <td>⟨h⁢(X)⟩rs</td>
      <td>KX′⁢(1)</td>
    </tr>
    <tr>
      <td></td>
      <td>Chronological fitness variance</td>
      <td>Var⁢[h⁢(X)]cl</td>
      <td>KX′′⁢(0)</td>
    </tr>
    <tr>
      <td></td>
      <td>Retrospective fitness variance</td>
      <td>Var⁢[h⁢(X)]rs</td>
      <td>KX′′⁢(1)</td>
    </tr>
    <tr>
      <td>Selection strength</td>
      <td>Jeffreys divergence bet. Qcl⁢(X) and Qrs⁢(X)</td>
      <td>SJF⁢[X]</td>
      <td>KX′⁢(1)-KX′⁢(0)</td>
    </tr>
    <tr>
      <td></td>
      <td>KL divergence of Qcl(X) from Qrs(X)</td>
      <td>SKL(1)⁢[X]</td>
      <td>KX⁢(1)-KX′⁢(0)</td>
    </tr>
    <tr>
      <td></td>
      <td>KL divergence of Qrs(X) from Qcl(X)</td>
      <td>SKL(2)⁢[X]</td>
      <td>KX′⁢(1)-KX⁢(1)</td>
    </tr>
    <tr>
      <td>Growth rate gain/loss</td>
      <td>Growth rate gain</td>
      <td>SKL(1)[D]/τΛ</td>
      <td>1-KD′⁢(0)/KD⁢(1)</td>
    </tr>
    <tr>
      <td></td>
      <td>Additional growth rate loss upon perturbation</td>
      <td>-SKL(2)⁢[D]/τ⁢Λ</td>
      <td>1-KD′⁢(1)/KD⁢(1)</td>
    </tr>
  </tbody>
</table>

### Difference in the selection strength measures reveals the effect of selection on fitness variance

The difference between the two selection strength measures $S_{KL}^{(1)}⁢[X]$ and $S_{KL}^{(2)}⁢[X]$ is determined by the higher order cumulants by the relation

$$
S_{KL}^{(2)}[X]−S_{KL}^{(1)}[X]=\sumn=3∞\frac{κ_{n}^{(X)}}{n!}(n−2)
$$

(Appendix 3). When fourth or higher order cumulants are negligible, the third-order fitness cumulant $κ_{3}^{(X)}$, that is the skewness of fitness distribution, determines which selection strength measure is greater.

The relations among the fitness and selection strength measures can be graphically depicted by plotting $K_{X}^{′}⁢(ξ)$ in the interval $0\leqξ\leq1$ (Figure 3A). $S_{KL}^{(1)}⁢[X]$ corresponds to the area between $y=⟨h⁢(X)⟩_{cl}$ and $y=K_{X}^{′}⁢(ξ)$; and $S_{KL}^{(2)}⁢[X]$ corresponds to the area between $y=K_{X}^{′}⁢(ξ)$ and $y=⟨h⁢(X)⟩_{rs}$ (Figure 3A). Therefore, the skewness of fitness distribution primarily determines the convexity of $K_{X}^{′}⁢(ξ)$ (Figure 3B–G).

![Figure 3.](https://cdn.elifesciences.org/articles/72299/elife-72299-fig3-v1.jpg)

**Figure 3.:** (A) Graphical representation of various fitness and selection strength measures by $K_{X}^{′}⁢(ξ)$-plot. Blue curve represents $K_{X}^{′}⁢(ξ)$. The area between the horizontal axis and $K_{X}^{′}⁢(ξ)$ in the interval $0\leqξ\leq1$ outlined in red corresponds to population growth $\tau⁢Λ$. The gray and hatched regions correspond to $⟨h⁢(X)⟩_{cl}$ and $S_{KL}^{(1)}⁢[X]$, respectively. The area between $K_{X}^{′}⁢(ξ)$ and $y=⟨h⁢(X)⟩_{rs}$ corresponds to $S_{KL}^{(2)}⁢[X]$. (B-D) Representative shapes of $K_{X}^{′}⁢(ξ)$ depending on $κ_{3}^{(X)}$. Assuming that the contributions from fourth or higher-order cumulants are negligible, $K_{X}^{′}⁢(ξ)$ becomes convex downward when $κ_{3}^{(X)}>0$ (B); a straight line when $κ_{3}^{(X)}=0$ (C); and convex upward when $κ_{3}^{(X)}<0$ (D). (E-G) Relationships between third-order fitness cumulant and skewness of chronological distribution $Q_{cl}⁢(h)$.

The difference between the two selection strength measures can reveal the effect of selection on fitness variances. The slope of the tangent lines to $K_{X}^{′}⁢(ξ)$ at $ξ=0$ and 1 corresponds to the chronological and retrospective fitness variances, respectively (Table 1). Therefore, when $K_{X}^{′}⁢(ξ)$ is convex upward in the interval $0\leqξ\leq1$ ($κ_{3}^{(X)}<0$, i.e., $S_{KL}^{(1)}[X]>S_{KL}^{(2)}[X]$, as in Figure 3D), the effect of selection is to decrease the lineage fitness variance in the retrospective distribution relative to the chronological distribution, whereas if $K_{X}^{′}⁢(ξ)$ is convex downward ($κ_{3}^{(X)}>0$, i.e., $S_{KL}^{(1)}[X]<S_{KL}^{(2)}[X]$, as in Figure 3B), selection increases the fitness variance. We indeed find cases of both kinds of behavior in the experimental lineage data, as will be seen below. Therefore, one can probe the effect of selection on fitness variances by comparing the two selection strength measures $S_{KL}^{(1)}⁢[X]$ and $S_{KL}^{(2)}⁢[X]$.

Significant differences between $S_{KL}^{(1)}⁢[X]$ and $S_{KL}^{(2)}⁢[X]$ indicate non-negligible contributions of higher-order cumulants. In such circumstances, the fitness distributions are far from Gaussian with significant skews or multiple peaks. Therefore, higher-order cumulants can also be used to probe the existence of sub-populations in cellular populations.

### Population growth rate under fitness perturbations

We mentioned above that the selection strength measure $S_{KL}^{(1)}⁢[D]$ represents growth rate gain caused by fitness heterogeneity. Likewise, another selection strength measure $S_{KL}^{(2)}⁢[D]$ represents a different consequence of fitness heterogeneity, that is, additional loss of growth rate under fitness perturbations.

From (Equation 1), and taking division count as a lineage trait, one can express population growth rate as

$$
Λ=\frac{1}{\tau}ln⁡\sumde^{h~(d)}Q_{cl}(d).
$$

We now consider the response of population growth rate to perturbations that cause lineage fitness to change from $D⁢(\sigma)⁢ln⁡2$ to $(1-ϵ)⁢D⁢(\sigma)⁢ln⁡2$, and rewrite the population growth rate as

$$
Λ(ϵ):=\frac{1}{\tau}ln⁡\sumde^{(1−ϵ)h~(d)}Q_{cl}(d).
$$

We have $Λ⁢(0)=Λ$, and note that $Λ⁢(ϵ)=\frac{1}{\tau}⁢K_{D}⁢(1-ϵ)$ from (Equation 9). Differentiating $Λ⁢(ϵ)$ with respect to $ϵ$, and evaluating at $ϵ=0$, we find

$$
\frac{d⁢Λ⁢(ϵ)}{d⁢ϵ}|_{ϵ=0}=-\frac{⟨h~⁢(D)⟩_{rs}}{\tau}
$$

(see Appendix 3). This relation shows that the change of population growth rate for small $ϵ$ is proportional to the retrospective mean fitness of the unperturbed population. Since $⟨h~⁢(D)⟩_{rs}=\tau⁢Λ+S_{KL}^{(2)}⁢[D]$ (Equation 4), the relative change of population growth rate is

$$
\frac{1}{Λ}⁢\frac{d⁢Λ⁢(ϵ)}{d⁢ϵ}|_{ϵ=0}=-(1+\frac{S_{KL}^{(2)}⁢[D]}{\tau⁢Λ}).
$$

Therefore, a population with higher selection strength will exhibit a greater change in population growth rate upon perturbation. The selection strength measure $S_{KL}^{(2)}⁢[D]$ represents additional loss of population growth rate due to division count heterogeneity before perturbation.

As we see below, one manifestation of $ϵ$ occurs via a cell removal operation. Consider the removal of a branch in the genealogical tree just after each cell division with the probability of $1-2^{-ϵ}$ ($ϵ>0$) (Figure 4A). In this case, the probability that a cell remains in the population after a cell division is $2^{-ϵ}$, and the growth of cell lineages that originally divided $d$ times will be effectively reduced by the factor $(2^{-ϵ})^{d}$. Consequently, the number of cell lineages that reach the end time point will also be effectively reduced from $N_{0}⁢(\sum_{d}2^{d}⁢Q_{cl}⁢(d))$ to $N_{0}⁢(\sum_{d}2^{(1-ϵ)⁢d}⁢Q_{cl}⁢(d))$. Therefore, the population growth rate under this branch removal operation is given by (Equation 17), and the relative change of population growth rate is

$$
\frac{ΔΛ}{Λ}:=\frac{Λ(ϵ)−Λ}{Λ}=−(1+\frac{S_{KL}^{(2)}[D]}{\tauΛ})ϵ+O(ϵ^{2}).
$$

![Figure 4.](https://cdn.elifesciences.org/articles/72299/elife-72299-fig4-v1.jpg)

**Figure 4.:** (A) Scheme of random cell removal. Here, we consider the situation where cells were removed probabilistically after each cell division. Red crosses represent cell removal positions in the tree. The lineages after cell removal points disappear from the tree. Consequently, the number of cells at the end time point decreases. (B) Generation time distributions used in the simulation. We assumed that cellular generation time follows gamma distributions in the simulation. We set the shape parameter to either 1 ($g_{1}⁢(x)$), 2 ($g_{2}⁢(x)$), or 5 ($g_{3}⁢(x)$). (C-E) Population growth rate changes by cell removal perturbation. Gray points show the relative changes in population growth rate $ΔΛ/Λ:=(Λ(ϵ)−Λ(0))/Λ(0)$. Cell removal probability was set to $1-2^{-ϵ}$ in each condition of perturbation strength $ϵ$. Broken red lines represent the theoretical prediction $Δ⁢Λ/Λ≈-\frac{⟨h~⁢(D)⟩_{rs}}{\tau⁢Λ}⁢ϵ=-(1+\frac{S_{KL}^{(2)}⁢[D]}{\tau⁢Λ})⁢ϵ$. The lines of $Δ⁢Λ/Λ=-ϵ$ (blue) and $-\frac{⟨h~⁢(D)⟩_{cl}}{\tau⁢Λ}⁢ϵ$ (green) are shown for reference. The generation time distributions used in the simulation are $g_{1}⁢(x)$ for C, $g_{2}⁢(x)$ for D, and $g_{3}⁢(x)$ for E.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/72299/elife-72299-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** We conducted the simulations of cell population growth with positive mother-daughter correlations (Gray points). We considered the generation time distribution that follows a gamma distribution with shape parameter 2 ($g_{2}⁢(x)$ in Figure 4B). We generated correlated generation time of individual cells based on the mother cell’s value with the algorithm in Materials and methods. We randomly removed the individual cells from the population with the probability $1-2^{-ϵ}$ after each cell division. The broken red lines represent the theoretical prediction of the changes $Δ⁢Λ/Λ=-\frac{⟨h~⁢(D)⟩_{rs}}{\tau⁢Λ}⁢ϵ$. The lines of $Δ⁢Λ/Λ=-ϵ$ (blue) and $Δ⁢Λ/Λ=-\frac{⟨h~⁢(D)⟩_{cl}}{\tau⁢Λ}⁢ϵ$ (green) were also shown for reference. (A) The result with no mother-daughter correlation of generation time ($r_{md}=0$). (B) $r_{md}=0.2$. (C) $r_{md}=0.4$. (D) $r_{md}=0.6$.

We validated this relation by simulating population growth with and without the cell removal operation (Figure 4B–E and Figure 4—figure supplement 1). The result confirmed that the relative changes of population growth rates by the probabilistic removal of cells followed $-(1+\frac{S_{KL}^{(2)}⁢[D]}{\tau⁢Λ})⁢ϵ$ in all the conditions (Figure 4C–E). We also tested this relation for cell populations with positive mother-daughter correlations of division intervals, which are often found for eukaryotic cells (Nozoe and Kussell, 2020; Seita et al., 2021; Mosheiff et al., 2018; Kuchen et al., 2020). We confirmed that the response relation was valid irrespectively of the strength of mother-daughter correlations (Figure 4—figure supplement 1), which shows that the relation is general and independent of the specific dynamics of the cell division process.

### Applications to models

In Appendices 1 and 2, we calculate the exact form of $K_{D}⁢(ξ)$ for analytically-tractable models. We derive chronological and retrospective mean fitness, selection strength, and the cumulants of fitness landscapes from $K_{D}⁢(ξ)$ to observe how the framework works. In particular, we show the analytical calculation for a cellular population in which cells divide with gamma-distributed uncorrelated interdivision times in Appendix 2 to understand the effect of inherent stochasticity on population growth. This analysis yields two conclusions: (1) Unlike the central limit theorem, the contribution of higher-order cumulants to population growth remains even in the long-term limit, and (2) the shape of the generation time distribution influences the cell population’s long-term growth rate by constantly introducing selection within the population. Therefore, the details of inherent stochasticity of interdivision times are essential for the long-term population growth rate.

### Experimental evaluation of contributions of growth heterogeneity to population growth

Next, we apply this framework of cell lineage statistics to experimental single-cell lineage data of various organisms. The list includes bacterial cells (Escherichia coli and Mycobacterium smegmatis), unicellular eukaryotic cells (Schizosaccharomyces pombe), and mammalian cancer cells (L1210 mouse leukemia cells). This analysis aims to unravel whether the extent of growth rate gain from growth heterogeneity depends on the organisms and environments under constant growth conditions. As summarized in Tables 2 and 3, we used cellular lineage data newly obtained in this study as well as other existing datasets (Nozoe et al., 2017; Wakamoto et al., 2013; Nakaoka and Wakamoto, 2017; Seita et al., 2021). The E. coli and S. pombe data include several culture conditions to compare cumulants’ contributions to population growth across environments. The E. coli data were obtained using either agarose pad or the microchamber array microfluidic device, yielding genealogical tree information such as the one shown in Figure 1. The S. pombe and L1210 cell data were obtained with mother machine microfluidic devices (Wang et al., 2010), which provide isolated cell lineage information but discard tree information due to its cell exclusion scheme. We assumed that these isolated cell lineages would follow chronological statistics and evaluated chronological distributions and selection strength according to the method described in Materials and methods. All the data analyzed in this section were taken from cell populations growing at approximately constant rates.

**Table 2.**
 Summary of cellular species, culture conditions, and observation setup used in the experiments in Figure 5.


<table>
  <thead>
    <tr>
      <th>Species</th>
      <th>Label</th>
      <th>Strain</th>
      <th>Medium</th>
      <th>Temperature (°C)</th>
      <th>Device</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>E. coli</td>
      <td>rpoS-mcherry glucose_30°C</td>
      <td>MG1655 F3 rpoS-mcherry /pUA66-PrpsL-gfp</td>
      <td>M9 minimal medium +0.2%(w/v) glucose +1/2 MEM amino acids solution (Sigma)</td>
      <td>30</td>
      <td>Microchamber array</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>rpoS-mcherry glucose_37°C</td>
      <td>MG1655 F3 rpoS-mcherry /pUA66-PrpsL-gfp</td>
      <td>M9 minimal medium +0.2%(w/v) glucose +1/2 MEM amino acids solution (Sigma)</td>
      <td>37</td>
      <td>Microchamber array</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>rpoS-mcherry glycerol_37°C</td>
      <td>MG1655 F3 rpoS-mcherry /pUA66-PrpsL-gfp</td>
      <td>M9 minimal medium +0.1%(v/v) glycerol +1/2 MEM amino acids solution (Sigma)</td>
      <td>37</td>
      <td>Microchamber array</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>f3nw -sm</td>
      <td>F3NW</td>
      <td>M9 minimal medium +0.2%(w/v) glucose +1/2 MEM amino acids solution (Sigma)+0.1mM Isopropyl β-D-1 thiogalactopyranoside (IPTG)</td>
      <td>37</td>
      <td>Agar pad</td>
      <td>Nozoe et al., 2017</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>f3nw +sm</td>
      <td>F3NW</td>
      <td>M9 minimal medium +0.2%(w/v) glucose +1/2 MEM amino acids solution (Sigma)+0.1 mM Isopropylβ-D-1 thiogalactopyranoside (IPTG)+100 μg/ml streptomycin</td>
      <td>37</td>
      <td>Agar pad</td>
      <td>Nozoe et al., 2017</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>f3ptn001 -sm</td>
      <td>F3/pTN001</td>
      <td>M9 minimal medium +0.2%(w/v) glucose +1/2 MEM amino acids solution (Sigma)+0.1 mM Isopropylβ-D-1 thiogalactopyranoside (IPTG)</td>
      <td>37</td>
      <td>Agar pad</td>
      <td>Nozoe et al., 2017</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>f3ptn001+sm</td>
      <td>F3/pTN001</td>
      <td>M9 minimal medium +0.2%(w/v) glucose +1/2 MEM amino acids solution (Sigma)+0.1 mM Isopropylβ-D-1 thiogalactopyranoside (IPTG)+200μg/ml streptomycin</td>
      <td>37</td>
      <td>Agar pad</td>
      <td>Nozoe et al., 2017</td>
    </tr>
    <tr>
      <td>M. smegmatis</td>
      <td>mc2155 7H9</td>
      <td>mc2155</td>
      <td>Middlebrook 7H9 medium +0.5% albumin +0.2% glucose +0.085% NaCl+0.5% glycerol +0.05% Tween-80</td>
      <td>37</td>
      <td>Membrane cover</td>
      <td>Wakamoto et al., 2013</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>EMM28</td>
      <td>HN0025</td>
      <td>Edinburgh minimal medium +2% (w/v) glucose</td>
      <td>28</td>
      <td>Mother machine</td>
      <td>Nakaoka and Wakamoto, 2017</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>EMM30</td>
      <td>HN0025</td>
      <td>Edinburgh minimal medium +2%(w/v) glucose</td>
      <td>30</td>
      <td>Mother machine</td>
      <td>Nakaoka and Wakamoto, 2017</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>EMM32</td>
      <td>HN0025</td>
      <td>Edinburgh minimal medium +2%(w/v) glucose</td>
      <td>32</td>
      <td>Mother machine</td>
      <td>Nakaoka and Wakamoto, 2017</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>EMM34</td>
      <td>HN0025</td>
      <td>Edinburgh minimal medium +2%(w/v) glucose</td>
      <td>34</td>
      <td>Mother machine</td>
      <td>Nakaoka and Wakamoto, 2017</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>YE28</td>
      <td>HN0025</td>
      <td>Yeast extract medium +3%(w/v) glucose</td>
      <td>28</td>
      <td>Mother machine</td>
      <td>Nakaoka and Wakamoto, 2017</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>YE30</td>
      <td>HN0025</td>
      <td>Yeast extract medium +3%(w/v) glucose</td>
      <td>30</td>
      <td>Mother machine</td>
      <td>Nakaoka and Wakamoto, 2017</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>YE34</td>
      <td>HN0025</td>
      <td>Yeast extract medium +3%(w/v) glucose</td>
      <td>34</td>
      <td>Mother machine</td>
      <td>Nakaoka and Wakamoto, 2017</td>
    </tr>
    <tr>
      <td>L1210 mouse leukemia cell</td>
      <td>L1210 RPMI-1640</td>
      <td>L1210 (ATCC CCL-219)</td>
      <td>RPMI-1640 medium (Wako)+10% fetal bovine serum (Biosera) under 5% CO2 atmosphere</td>
      <td>37</td>
      <td>Mother machine</td>
      <td>Seita et al., 2021</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Summary of the data used in the analysis in Figure 5.tstart and tend are the start and end times for the analysis time window $\tau$.


<table>
  <thead>
    <tr>
      <th>Species</th>
      <th>label</th>
      <th>τ(hr)</th>
      <th>tstart(hr)</th>
      <th>tend(hr)</th>
      <th>N0</th>
      <th>Nτ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>E. coli</td>
      <td>rpoS-mcherry glucose_37°C</td>
      <td>5</td>
      <td>0.95</td>
      <td>5.95</td>
      <td>163</td>
      <td>3989</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>rpoS-mcherry glucose_30°C</td>
      <td>8</td>
      <td>0.95</td>
      <td>8.95</td>
      <td>197</td>
      <td>6173</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>rpoS-mcherry glycerol_37°C</td>
      <td>6.5</td>
      <td>0.95</td>
      <td>7.45</td>
      <td>253</td>
      <td>5825</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>f3nw-sm</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>305</td>
      <td>4343</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>f3nw +sm</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>291</td>
      <td>3164</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>f3ptn001-sm</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>984</td>
      <td>9229</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>f3ptn001+sm</td>
      <td>5</td>
      <td>0</td>
      <td>5</td>
      <td>977</td>
      <td>7429</td>
    </tr>
    <tr>
      <td>M. smegmatis</td>
      <td>mc2155 7H9</td>
      <td>10</td>
      <td>1.75</td>
      <td>11.75</td>
      <td>39</td>
      <td>311</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>EMM28</td>
      <td>167</td>
      <td>0</td>
      <td>167</td>
      <td>1148</td>
      <td>-</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>EMM30</td>
      <td>131</td>
      <td>0</td>
      <td>131</td>
      <td>963</td>
      <td>-</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>EMM32</td>
      <td>123.5</td>
      <td>0</td>
      <td>123.5</td>
      <td>883</td>
      <td>-</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>EMM34</td>
      <td>152</td>
      <td>0</td>
      <td>152</td>
      <td>1078</td>
      <td>-</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>YE28</td>
      <td>108</td>
      <td>0</td>
      <td>108</td>
      <td>1177</td>
      <td>-</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>YE30</td>
      <td>90</td>
      <td>0</td>
      <td>90</td>
      <td>866</td>
      <td>-</td>
    </tr>
    <tr>
      <td>S. pombe</td>
      <td>YE34</td>
      <td>78</td>
      <td>0</td>
      <td>78</td>
      <td>863</td>
      <td>-</td>
    </tr>
    <tr>
      <td>L1210 mouse leukemia cell</td>
      <td>L1210 RPMI-1640</td>
      <td>60</td>
      <td>0</td>
      <td>60</td>
      <td>474</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

First, we evaluated the first-order cumulants’ contributions $W_{1}^{(D)}=\frac{κ_{1}^{(D)}}{\tau⁢Λ}=\frac{⟨h~⁢(D)⟩_{cl}}{\tau⁢Λ}$ (Equation 14), finding that $W_{1}^{(D)}<1$ for all the samples and conditions (Figure 5A). This result confirms that the chronological mean fitness cannot fully account for the population growth rates. This means that the division count heterogeneity present even in constant environments contributes to increasing the population growth rate. However, the extent of the contributions was different: $W_{1}^{(D)}$ for S. pombe was consistently closer to 1 than those for the other cell types except one condition (EMM, 34 °C), suggesting that S. pombe’s growth is less heterogeneous under most culture conditions.

![Figure 5.](https://cdn.elifesciences.org/articles/72299/elife-72299-fig5-v1.jpg)

**Figure 5.:** (A) Contributions of the cumulants of a fitness landscape to population growth. $W_{1}^{(D)}$ and $W_{2}^{(D)}$ were evaluated for the experimental cell lineage data from E. coli (red), M. smegmatis (blue), S. pombe (green), and L1210 mouse leukemia cells (yellow). The E. coli rpoS-mcherry data were newly obtained in this study (see Materials and methods). The other data were taken from literature: E. coli f3nw and f3ptn001 from Nozoe et al., 2017; M. smegmatis from Wakamoto et al., 2013; S. pombe from Nakaoka and Wakamoto, 2017; and L1210 from Seita et al., 2021. Circles and triangles represent $W_{1}^{(D)}$ and $W_{2}^{(D)}$, respectively. Error bars represent the two standard deviation ranges estimated by resampling the cellular lineages (see Materials and methods). (B) Relationship between $S_{KL}^{(1)}⁢[D]/\tau⁢Λ$ and $S_{KL}^{(2)}⁢[D]/\tau⁢Λ$. Colors correspond to the cellular species as in A. The S. pombe data were further categorized into two groups: Circles for the EMM conditions; and triangles for the YE conditions. (C-E) Representative chronological distributions of division count, $Q_{cl}⁢(D)$. (F-H) Graphical representation of $K_{D}^{′}⁢(ξ)$. F for S. pombe EMM30; G for L1210 RMPI-1640; and H for E. coli f3nw-sm.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/72299/elife-72299-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** Chronological distributions of division count, $Q_{cl}⁢(D)$.(A-G) E. coli. (H). M. smegmatis. (I-O) S. pombe. P. L1210 mouse leukemia cells.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/72299/elife-72299-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** Graphical representation of $K_{D}^{′}⁢(ξ)$.A-G. E. coli. H. M. smegmatis. I-O. S. pombe. P. L1210 mouse leukemia cells.

We next evaluated $W_{2}^{(D)}=\frac{κ_{1}^{(D)}+κ_{2}^{(D)}/2}{\tau⁢Λ}$, finding that $W_{2}^{(D)}≈1$ for most of the conditions (Figure 5A). This result indicates small contributions of the third or higher-order cumulants to population growth. Consistent with this result, $S_{KL}^{(1)}⁢[D]$ and $S_{KL}^{(2)}⁢[D]$ were almost identical in most conditions (Figure 5B). Note that $S_{KL}^{(2)}⁢[D]-S_{KL}^{(1)}⁢[D]$ depends only on the third or higher order cumulants (Equation 15). The chronological distributions $Q_{cl}⁢(D)$ of these samples were nearly symmetric in most cases; however, under the conditions where the deviations of $W_{2}^{(D)}$ from 1 are larger, such as S. pombe in EMM medium and L1210, the distributions were skewed slightly (Figure 5C–E and Figure 5—figure supplement 1). Such distribution skew was reflected in the convexity directions of $K_{D}^{′}⁢(ξ)$-plots (Figure 5F–H and Figure 5—figure supplement 2). These results imply that cellular populations of S. pombe in EMM medium and of L1210 contain small subpopulations that follow distinct division statistics. In fact, it was previously demonstrated that the L1210 cell populations contain slow-cycling cell lineages that can survive for longer durations under exposure to an anticancer drug (Seita et al., 2021). Therefore, this analysis confirms that the differences in the two strength measures can be used for detecting subpopulations in cellular populations.

In S. pombe EMM medium conditions, $K_{D}^{′}⁢(ξ)$ was convex downward in the interval $0\leqξ\leq1$ except for EMM 34°C (Figure 5F and Figure 5—figure supplement 2). Therefore, under certain conditions selection can increase fitness variance in the retrospective distributions relative to chronological distributions among cellular lineages.

### The contributions of higher order cumulants become significant in the regrowth from a late stationary phase

We further applied the framework to the cell lineage data of E. coli populations regrowing from an early or late stationary phase. This analysis aims to uncover how strongly selection occurs upon environmental changes and whether the selection strength can differ under identical conditions depending on the conditions before regrowth. To conduct time-lapse observations of regrowing cell populations, we used a microfluidic device equipped with microchambers etched on a glass coverslip. We sampled E. coli cells either from an early or late stationary phase batch culture and enclosed the cells into the microchambers by a semipermeable membrane (Inoue et al., 2001; Hashimoto et al., 2016). We switched flowing media from stationary-phase conditioned medium to fresh medium at the start of time-lapse measurements and recorded the growth and division of individual cells (Figure 6A, see Materials and Methods).

![Figure 6.](https://cdn.elifesciences.org/articles/72299/elife-72299-fig6-v1.jpg)

**Figure 6.:** (A) Time-lapse images. Cellular regrowing dynamics from early and late stationary phases were observed by time-lapse microscopy. Cells were enclosed in the microchambers etched on coverslips. The top three images show representative images of the cells from an early stationary phase. The bottom three images show the cells from a late stationary phase. Scale bar, 5 μm. (B) Population dynamics. The number of cells at each time point normalized by the initial cell number ($N⁢(t)/N⁢(0)$) was plotted against time $t$ was 307 for the early stationary sample and 295 for the late stationary sample. (C, D) Representative cellular lineage trees in the regrowing kineics from the early stationary phase (C) and the late stationary phase (D). The trees correspond to the time-lapse images in A. (E) Cumulative contributions of the cumulants of the fitness landscape $h⁢(D)$ to population growth. Error bars represent the two standard deviation ranges estimated by resampling the cellular lineages (see Materials and methods). (F) Chronological distributions of division count $Q_{cl}⁢(D)$. (G) Relationships between $S_{KL}^{(1)}⁢[D]$ and $S_{KL}^{(2)}⁢[D]$. The blue and black points show the results for the early stationary phase sample and the late stationary phase sample, respectively. Gray points represent the results for the cell populations growing at approximately constant growth rates shown in Figure 5B.

The growth curves reconstructed by counting the number of cells at each time point showed lags in regrowth (Figure 6B). The lag time was shorter for the populations from the early stationary phase. The lineage tree structures in the cell populations were markedly different between the conditions (Figure 6C and D). The tree structures were more uniform for the early stationary phase sample with multiple divisions in most cell lineages (Figure 6C), whereas those for the late stationary phase sample were more heterogeneous, with 90% of cells showing no divisions within the observation time (Figure 6D).

We analyzed these data and found $W_{1}^{(D)}=0.95\pm0.02$ for the population from the early stationary phase and $W_{1}^{(D)}=0.27\pm0.04$ for the population from the late stationary phase (Figure 6E). Therefore, the chronological mean fitness, $⟨h~⁢(D)⟩_{cl}$, explains only 27% of the growth rate of the population regrowing from the late stationary phase. In other words, significantly strong selection occurred in the regrowth from the late stationary phase. We also found that $W_{2}^{(D)}≈1$ for the population from the early stationary phase, as observed for the E. coli populations growing at constant rates. In constrast, $W_{2}^{(D)}$ for the population from the late stationary phase was $0.61\pm0.04$, and $W_{n}^{(D)}$ converged to 1 only after taking the cumulants up to approximately 10th-order into account (Figure 6E). This indicates a skew of the fitness distribution and validates the existence of subpopulations following distinct division statistics in the population from the late stationary phase in this time scale of regrowth (Figure 6F). Reflecting the extreme skew to the right of the chronological distributions $Q_{cl}⁢(D)$ (Figure 6F), $S_{KL}^{(2)}⁢[D]$ was significantly greater than $S_{KL}^{(1)}⁢[D]$ for the late stationary phase sample (Figure 6G).

These results indicate that the levels of selection in the regrowing processes strongly depend on the durations under stationary phase conditions. Therefore, the ability to quickly resume growth under favorable conditions is gradually lost in most cells in the stationary phase; only a fraction of cells in the population can contribute to the future cell population. However, we also remark that preserving such non-growing cell lineages can be beneficial when cell populations are exposed to harsh environments in unpredictable manners (Kussell and Leibler, 2005).

### Lineage statistics reveal condition-dependent fitness landscapes and selection strength for a growth-regulating sigma factor

RpoS is a sigma factor that controls the transcription of a large set of genes (10% of the genome) in E. coli (Battesti et al., 2011). High RpoS expression usually correlates with growth suppression; RpoS is induced when cells enter stationary phases or encounter stress conditions, such as starvation, low pH, oxidative stress, high temperature, or osmotic stress. Elevated RpoS expression provokes the intracellular programs to shut down growth and resist the stress (Battesti et al., 2011). However, it remains poorly understood how the continuum heterogeneity of RpoS expression levels is linked to the lineage fitness and selection in exponentially growing cellular populations. We therefore applied the lineage statistics framework to the single-cell time-lapse data of an E. coli strain expressing an RpoS-mCherry fusion protein from the native chromosomal locus and green fluorescent protein (GFP) from a low copy plasmid.

We quantified the time-scaled fitness landscapes $h⁢(X)/\tau$ and relative selection strength $S_{rel}⁢[X]$ (Equation 5) under three growth conditions, taking the time-averaged mean fluorescent intensity of RpoS-mCherry or GFP along each cell lineage (proxies of time-averaged intracellular concentrations) as $X$ (Figure 7). Since fluorescent intensity is a trait that takes continuous values, we binned the intensity values with the bin sizes around which selection strength values are relatively stable (Materials and methods). Furthermore, since the calculation of relative selection strength from empirical data always gives positive values, we compared the relative selection strength values with those calculated from the data in which the correspondences between division counts and trait values were randomized to confirm the confidence levels (Figure 7—figure supplement 1).

![Figure 7.](https://cdn.elifesciences.org/articles/72299/elife-72299-fig7-v1.jpg)

**Figure 7.:** (A) Fitness landscapes for the time-averaged concentration (mean fluorescent intensity) for RpoS-mCherry. The time-averaged mean fluorescent intensity of RpoS-mCherry was adoped as a lineage trait $X$ and changes in fitness were plotted against the trait values $x$. Fitness landscapes were scaled by the lineage length (observation duration) $\tau$. Error bars represent the two standard deviation ranges estimated by resampling the cellular lineages. (B) Fitness landscapes for the time-averaged concentration for GFP. The time-averaged mean fluorescent intensity of GFP was adoped as a lineage trait $X$ and changes in fitness were plotted against the trait values $x$. (C) Relative selection strength for the time-averaged concentrations of RpoS-mCherry (red) and GFP (green). (D, E) Chronological distributions $Q_{cl}⁢(x)$ for the time-averaged concentrations of RpoS-mCherry (D) and GFP (E). (F-H) Cumulative contributions of fitness cumulants to population growth, $W_{n}^{(X)}$, assuming that $X$ is either time-averaged concentration of RpoS-mCherry (red) or time-averaged concentration of GFP (green). Error bars represent the two standard deviation ranges estimated by resampling the cellular lineages. Panel F is for the Glucose-37°C condition; Panel G for the Glucose-30°C condition; and Panel H for the Glycerol-37°C condition.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/72299/elife-72299-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** The blue histograms show the distributions of the relative selection strength values calculated from the lineage data in which the correspondences between division counts and trait values are shuffled. The vertical lines indicate the relative selection strength values for the experimental data. A. GFP under the Glucose-37°C condition. B. RpoS-mCherry under the Glucose-37°C condition. C. GFP under the Glucose-30°C condition. D. RpoS-mCherry under the Glucose-30°C condition. E. GFP under the Glycerol-37°C condition. F. RpoS-mCherry under the Glycerol-37°C condition.

The result shows that the fitness landscapes and selection strength of RpoS expression level differ significantly among the growth conditions (Figure 7). Under the glucose-37°C condition, the fitness landscapes of RpoS-mCherry and GFP expression were both decreasing functions (Figure 7A and B). Thus, high expression of RpoS-expression and GFP in an exponentially growing population are both linked with lower lineage fitness. However, while the fitness landscape of GFP expression were nearly constant and showed significant decrease of fitness only at high expression levels, the fitness landscape of RpoS-mCherry decreased steadily in the observed expression range (Figure 7A and B). Consequently, the relative selection strength for RpoS-mCherry was 2.6-fold larger than that for GFP (Figure 7C).

Under the glucose-30°C and glycerol-37°C conditions, the fitness landscapes for RpoS-mCherry level were also decreasing functions and close to each other but significantly downshifted from that for the glucose-37°C condition (Figure 7A). This result reveals that cells could have different fitness for the same expression levels of RpoS, depending on the growth conditions. The selection strength for RpoS-mCherry was larger than that for GFP under the glucose-37°C and glucose-30°C conditions (Figure 7C), which proves that the heterogeneity of RpoS expression in a population correlates with the lineage fitness more strongly than that of GFP under those conditions. On the other hand, the relative selection strength of RpoS-mCherry under the glycerol-37°C condition was the smallest among the three conditions and not significantly different from that of GFP (Figure 7C). This is due to the relatively flat fitness landscapes in the central ranges of the distributions $Q_{cl}⁢(x)$ (Figure 7A and B) and the smaller variations of $x$ in the population (Figure 7D and E). These results reveal that the continuum heterogeneity of RpoS expression level in a population does correlate with the lineage fitness, but its contribution to selection depends on growth conditions. In other words, the heterogeneity in the RpoS-mCherry expression levels can barely correlate with fitness heterogeneity under some conditions.

We also evaluated the contributions of fitness cumulants for RpoS-mCherry expression to the population growth rate. Under all the conditions, $W_{1}^{(X)}$ was lower than 1 (Figure 7F–H). Therefore, the contributions of the higher-order fitness cumulants are non-negligible. However, the deviation of $W_{1}^{(X)}$ from 1 for RpoS-mCherry under the glycerol-37°C condition was small (Figure 7H). Hence, in this growth condition, RpoS-mCherry expression barely correlated with fitness heterogeneity in the population.

Importantly, this analysis can simultaneously reveal the changes in fitness landscapes (Figure 7A) and chronological distributions (Figure 7D). Interestingly, the distributions of the RpoS-mCherry expression levels are close between the Glucose-37°C and the Glycerol-37°C conditions, but the fitness landscapes are close between the Glucose-30°C and the Glycerol-37°C conditions. These results imply that the distributions and the fitness landscapes may vary independently in different conditions. Therefore, cells can potentially modulate the selection strength in each environment either by changing the fitness landscape or by changing the distribution of expression levels.

## Discussion

Growth and division of individual cells are intrinsically variable, which causes division count heterogeneity among cellular lineages in a population. Such heterogeneity is ubiquitous across prokaryotic and eukaryotic cells, and its statistical properties could depend on the mechanisms and regulations determining cell division timings. Notably, division count heterogeneity influences population growth rate and, consequently, a population’s survival and evolutionary success. Therefore, understanding what statistical features are produced among cellular lineages and how these features contribute to population growth is essential for unraveling each organism’s survival and evolutionary strategy.

This report presents a cell lineage statistics framework to uncover the linkage between fitness distributions and population growth rate. We reveal that a population’s growth rate can be expanded by the cumulants of a fitness landscape for any lineage trait. The cumulant expansion allows us to quantify the contribution of each fitness cumulant, such as variance and skewness, to population growth rate. Applying this framework to the experimental cell lineage data revealed the cumulants’ contributions to population growth for various organisms and environmental conditions. In particular, higher-order cumulants became significant in the regrowth of E. coli from a late stationary phase. We remark that the cumulant expansion of population growth rate is valid only when all the cumulants are finite and when the Taylor expansion of $K_{X}⁢(ξ)$ around $ξ=0$ also converges at $ξ=1$. However, all the experimental data examined in this study exhibited stable convergence, including in the regrowth condition from the late stationary phase.

An advantage of this framework is its independence from any growth and division models. The mechanisms driving the growth and division of individual cells are diverse among organisms. For example, the properties of cellular growth and division, such as whether a cell’s size increases exponentially or linearly and whether cell size regulation follows sizer or adder models, could depend on cell types, organisms, and environmental conditions (Jun et al., 2018; Kohram et al., 2021). Therefore, any model assumptions restrict applicability and necessitate model validation before application. The model independence of the framework presented here comes from the definitions of two essential quantities: the chronological and retrospective probabilities. Quantifying these probabilities requires only the information of the numbers of cells at initial and end time points and of division counts on each cellular lineage. Consequently, this formalism can be applied even to non-stationary conditions without modifications. However, we also remark that this independence from the details other than cell lineage structures imposes a limitation on the framework because it cannot report any potential influences from factors such as heterogeneous environments around cells and non-quantified traits. Furthermore, the fitness landscape $h⁢(x)$ and the relative selection strength $S_{rel}⁢[X]$ evaluate only the correlations between the trait and fitness, not causal relationships. However, causal traits should have large selection strength values, and this framework helps narrow down the candidates for essential traits. Most importantly, division statistics is the focal information that connects molecular details underlying cellular growth and division to population growth. Regulatory mechanisms can influence population growth only by modulating the division statistics in a cellular population.

Growth heterogeneity in a cellular population plays a critical role in its adaptation and survival against stressful conditions. In antibiotic persistence, bacterial cell populations often harbor small populations of non-growing or slow-growing cells which can survive under antibiotic exposures (Balaban et al., 2004). Such structures of growth heterogeneity can be investigated in a unified manner by the selection strength measures introduced here. For example, the differences in $S_{KL}^{(1)}⁢[D]/\tau⁢Λ$ among organisms can reveal the distinct levels of the overall growth heterogeneity of these organisms. Furthermore, the differences between $S_{KL}^{(1)}⁢[D]$ and $S_{KL}^{(2)}⁢[D]$ characterize the structure of growth heterogeneity: If $S_{KL}^{(1)}[D]>S_{KL}^{(2)}[D]$, the distribution of lineage fitness is skewed negatively, and the cell population harbors small subpopulations of slow-growing cell lineages; on the contrary, if $S_{KL}^{(1)}[D]<S_{KL}^{(2)}[D]$, the population harbors small populations of fast-growing cell lineages. Untangling the linkage between the structures of growth heterogeneity and their adaptability would help us understand the adaptive strategies of various organisms.

In general, heredity is also crucial for the growth and evolution of a population. The role of the heredity of a particular trait might be unravelled by taking the correlation length as a lineage trait $X$ and quantifying its selection strength. Since the modes of heredity can also be important targets of natural selection (Rivoire and Leibler, 2014), such measurements might provide insights into the evolution of heredity.

We remark that the distribution of interdivision time (generation time) influences the long-term growth rate, as demonstrated by the analytical model in Appendix 2. Therefore, statistical properties of generation time, such as distribution shapes and transgenerational correlations, can contribute to organisms’ evolutionary success by constantly introducing selection within a population. Unlike the central limit theorem, the contributions of higher-order cumulants can remain even in the long-term limit. Importantly, even when cell division processes seem purely stochastic, different states in some traits might underlie these variations in generation times. In such cases, $h⁢(x)$ and $S_{rel}⁢[X]$ for these traits can still unravel the correlations between the trait values and fitness.

This framework is applicable even to cell populations growing under non-constant environmental conditions. We indeed utilized this framework to analyze the regrowth of growth-arrested cells from the stationary phase conditions. The selection strength contributions to population growth, $S_{KL}^{(1)}⁢[D]/\tau⁢Λ$, were below 10% in most cases under constant growth conditions. Nevertheless, it became over 70% in the regrowth of E. coli from the late stationary phase. While increased selection in non-constant environments may not be surprising itself, it is intriguing to ask how its contribution changes quantitatively depending on the conditions of environmental changes, such as nutrient upshift and downshift. The selection strength contribution in the regrowth from the early stationary phase was only 5%. This result clearly shows that how strongly selection acts in regrowing processes depends on stationary phase incubation durations. However, we also remark that the differences in the selection strength values depend on the time window and might be valid only in this time scale. Clarifying the differences in the selection strength in longer time scales requires the detail of their lag time distributions, which we did not measure in this study.

We identified the cellular populations in which selection acts to increase fitness variance in the retrospective statistics compared with the chronological statistics (Figures 5F and 6G and Figure 5—figure supplement 2). When a decrease in fitness variance by selection is mentioned in evolutionary biology, an upper bound and inheritance of fitness across the generations of individuals are usually assumed. In such circumstances, selection drives the fitness distribution toward the maximum value, and the selection eventually causes fitness variance to decrease. However, even in this process, a decrease is not assured for every step; whether selection reduces fitness variance at each step depends on the fitness distribution at that time. Likewise, whether the fitness variance increases or decreases in the retrospective distribution depends on the shape of the fitness distribution before selection, that is, chronological distribution. Such conditions are graphically recognized by the downward convexity of $K_{D}^{′}⁢(ξ)$ (Figure 3). When the fourth or higher order fitness cumulants are negligible, the convexity of $K_{D}^{′}⁢(ξ)$ is determined primarily by the skewness of $Q_{cl}⁢(d)$; positive skew of $Q_{cl}⁢(d)$ with a long right tail makes $K_{D}^{′}⁢(ξ)$ convex downward and $Var⁢[h~⁢(D)]_{rs}$ greater than $Var⁢[h~⁢(D)]_{cl}$. This consequence is intuitively understandable since the right tail of $Q_{cl}⁢(d)$ is accentuated in proportion to $e^{D}$ by selection, which leads to greater variance of $Q_{rs}⁢(d)$. On the other hand, when the skew is negative with the long left tail, the effect of applying $e^{D}$ is to diminish the tail and compress the distribution toward the fittest lineages. It is of note that greater fitness variance in the retrospective statistics is possible even in the long-term limit, as demonstrated by the model in Appendix 2.

We showed that division count heterogeneity among cellular lineages has dual facets: increasing population growth rate while sensitizing populations to perturbations. These two effects are quantitatively represented by $S_{KL}^{(1)}⁢[D]/\tau⁢Λ$ and $S_{KL}^{(2)}⁢[D]/\tau⁢Λ$, respectively. Therefore, the difference between these selection strength measures gauges which aspect of growth heterogeneity is more significant in the population. Even though $S_{KL}^{(1)}⁢[X]$ and $S_{KL}^{(2)}⁢[X]$ are different in general, the analysis revealed that they were nearly identical in most of the cellular populations growing at constant rates (Figure 5). This result might suggest that, from a practical viewpoint, the contribution of higher-order cumulants becomes negligible under steady growth conditions, and the significant difference between $S_{KL}^{(1)}[X]$ and $S_{KL}^{(2)}⁢[X]$ could be used as a probe for the non-stationarity of the population growth. This speculation must be examined experimentally using various organisms and cell types across diverse environmental conditions.

This framework is premised on complete lineage tree information. However, many methods of single-cell measurements continuously exclude cells from observation areas and provide only a part of the tree information. Therefore, extending this framework so that one can infer both chronological and retrospective probabilities from incomplete tree information is an essential future research direction. In this study, we calculated the fitness landscapes and selection strength measures for the cell lineage data obtained with the mother machine devices, assuming that these cell lineages would follow the chronological statistics. Such a simple approach is not yet available for larger scale lineage tree data obtainable with the other single-cell measurement devices such as dynamics cytometer (Hashimoto et al., 2016) and chemoflux (Lambert et al., 2014). Furthermore, it has been shown that the inference precision of population growth rate has non-monotonic dependence on the length of cell lineages obtained with mother machine devices (Levien et al., 2020). Even though the difficulties to overcome are present, a comprehensive framework may permit a unified treatment of cellular lineage data obtained using various single-cell measurement methods.

Phenotypic heterogeneity is widely observed in diverse cellular systems, including both prokaryotic and eukaryotic cells. It is often considered that phenotypic heterogeneity allows bet-hedging against unpredictable environments and promotes the survival of cellular population (Kussell and Leibler, 2005). However, quantitative evaluation of correlations between the traits of interest and fitness is usually an intricate problem. The cell lineage statistical framework described in this study offers a straightforward procedure applicable to any cellular genealogical data, which are now becoming increasingly available for various biological phenomena, including cancer metastasis (Quinn et al., 2021) and stem cell differentiation (Filipczyk et al., 2015; Frieda et al., 2017; Chow et al., 2021). Another important advantage of this framework is that it allows decomposing a population growth rate into chronological fitness and selection strength. It is thus intriguing to apply this framework to long-term evolutionary dynamics and quantify how the contributions of chronological mean fitness and selection underlie the transitions of population growth rate. Such analysis might clarify the crucial roles of phenotypic heterogeneity in facilitating evolution.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pUA66-PrpsL-gfp (plasmid)</td>
      <td>Zaslaver et al., 2006</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>MG1655 F3</td>
      <td>Wakamoto lab</td>
      <td></td>
      <td>MG1655ΔfliCΔfimAΔflu</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>MG1655 F3 rpoS-mcherry /pUA66-P rplS-gfp</td>
      <td>Wakamoto lab</td>
      <td></td>
      <td>MG1655ΔfliCΔfimAΔflu rpoS-mcherry /pUA66-PrplS-gfp</td>
    </tr>
  </tbody>
</table>

### Microfabrication of microchamber array

We constructed and used a microchamber array for conducting single-cell time-lapse observation under controlled environmental conditions. A microchamber is a well etched on a glass coverslip. We used two types of microchamber array. One is an array of microchamber, whose dimension is 70 μm (w) × 55 μm (h) × 1 μm (d). This microchamber has a 21-μm×7-μm pillar for supporting the membrane in the middle. We used this microchamber array for the exponential-phase experiment of E. coli. Another is an array of microchamber, whose dimension is 40 μm (w) × 30 μm (h) × 1 μm (d). We used this type of microchamber array for the stationary-phase-regrowth experiment in Figure 6. We fabricated these microchamber arrays following similar procedures described in Hashimoto et al., 2016; Inoue et al., 2001.

The photomasks for the microchamber array were created by laser drawing (DDB-201-TW, Neoark) on mask blanks (CBL4006Du-AZP, CLEAN SURFACE TECHNOLOGY). The photoresist on mask blanks was developed in NMD-3 (Tokyo Ohka Kogyo). The uncovered chromium (Cr)-layer was removed in MPM-E30 (DNP Fine Chemicals), and the remaining photoresist was removed by acetone. Lastly, the slide was rinsed in MilliQ water and air-dried.

The microchamber array was created in glass coverslips by chemical etching. First, we coated a 1,000-angstrom Cr-layer on a clean coverslip (NEO Micro glass, No. 1., 24 mm × 60 mm, Matsunami) by evaporative deposition and AZP1350 (AZ Electronic Materials) by spin-coating on the Cr-layer. We transferred the photomask patterns using a mask aligner (MA-20, Mikasa). After developing the photoresist in NMD-3 and the Cr-layer in MPM-E30, the coverslip was soaked in buffered hydrofluoric acid solution (110-BHF, Morita Kagaku Kogyo) for 14 minutes 20 seconds at 23°C for glass etching. The etching reaction was stopped by soaking the coverslip in milliQ water. The remaining photoresist and the Cr-layer were removed by acetone and MPM-E30, respectively.

### Fabrication of PDMS pad

We used a polydimethylsiloxane (PDMS) pad to flow culture medium and control the environmental conditions around the cells in the microchamber array. The PDMS pad was designed to have a square bubble-trap groove, which prevents interference with bright-field microscopic imaging by air bubbles in flowing media.

To create a mold for the bubble-trap groove, we spin-coated SU-8 3050 (Kayaku Advanced Materials) on a silicon wafer (ID 447, $ϕ$ = 76.2 mm, University Wafer) and baked it at 95°C for 2 hr on a hot plate. The SU-8 layer was exposed to UV light on a mask aligner using a photomask and postbaked at 95°C for 2 hr. After cooled down to room temperature, the SU-8 photoresist was developed in the SU-8 developer (Kayaku Advanced Materials) and rinsed with isopropanol (Wako).

Part A and Part B of PDMS resin (SYLGARD 184 Silicone Elastomer Kit, DOW SILICONES) were mixed at 10:1 and poured onto the SU-8 mold. The air bubbles were removed under a decreased pressure for 30 min. The PDMS was cured at 65°C for 1 hour, and 20 mm × 20 mm square PDMS pad was cut out using a blade. We punched out two holes ($ϕ$ = 2 mm) in the PDMS pad for the inlet and outlet, and 10-cm silicone tubes (SR-1554, Tigers Polymer Corp., outer $ϕ$ = 2 mm, inner $ϕ$ = 1 mm) were inserted into the holes. The tubes were fixed to the holes by gluing a small amount of PDMS around the tubes at the holes. This PDMS pad was washed in isopropanol by sonication and autoclaved for the single-cell measurements.

### Chemical decoration of coverslip and cellulose membrane

We washed the microfabricated coverslips by sonication in contaminon (Wako), ethanol (Wako), and 0.1 M NaOH solution (Wako). The washed coverslips were rinsed in milliQ water by sonication and dried at 140°C for 30 min. The washed coverslip was soaked in 1% (v/v) 3-(2-aminoethylaminopropyl)trimethoxysilane solution (Shinetsu Kagaku Kogyo) for 30 min and incubated at 140°C for 30 min to create an amino group on the glass surface. The treated coverslip was washed in milliQ water for 15 min and dried at 140°C for 30 min. 1 mg NHS-LC-LC-Biotin (Funakoshi) was dissolved in 25 μl dimethyl sulfoxide and dispersed in 1 ml phosphate buffer (0.1 mM, pH8.0). A total of 200 μl of this biotin solution was placed on the coverslip and incubated at room temperature for 4 hr. The biotin solution was removed by soaking the coverslip in milliQ water.

We prepared a streptavidin-decorated cellulose membrane to enclose cells in the microchamber array while retaining a flexible environmental control. First, a 3 cm × 3 cm square cellulose membrane (Spectra/Por7 Pre-treated RC Tubing MWCO:25kD) was cut out and washed in milliQ water for 10 min. The membrane was incubated in a 0.1 M NaIO4 solution with gentle shaking for 4 hr at 25°C. After the wash in milliQ water, the treated membrane was incubated in a 500-μl solution of streptavidin hydrazide (Funakoshi) (10 μg/ml, dissolved in 0.1 mM phosphate buffer (pH7.0)) with gentle shaking for 14 hr at 25°C. The membrane was again washed in milliQ water and stored at 4°C.

### E. coli strains

We used two E. coli strains: MG1655 and MG1655 F3 rpoS-mcherry (MG1655 ΔfliCΔfimAΔflu rpoS-mcherry/pUA66-PrplS-gfp). MG1655 was used in the regrowth experiment from the stationary phases (Figure 6). MG1655 F3 rpoS-mcherry was used for analyzing the growth in constant environments (Figures 5 and 7). In MG1655 F3 rpoS-mcherry, the three genes, fliC, fimA, and flu, were deleted, and mcherry gene was inserted downstream of rpoS gene to express RpoS-mCherry translational fusion protein. This strain also expresses green fluorescent protein (GFP) from a low-copy plasmid, pUA66-PrplS-gfp, taken from a comprehensive library of fluorescent transcriptional reporters (Zaslaver et al., 2006).

### Culture conditions and sample preparation (exponential growth)

We used MG1655 F3 rpoS-mcherry E. coli strain and cultured the cells in M9 minimal medium (Difco) supplemented with 1/2 MEM amino acids solution (SIGMA) and 0.2% (w/v) glucose or glycerol as a carbon source. We set the cultivation temperature either at 37°C or 30°C.

To prepare E. coli cells for single-cell observation, we first inoculated a glycerol stock into a 3-ml culture medium and incubated it with shaking overnight under the same conditions of culture medium and temperature as those used in the time-lapse measurement. 30 μl of the overnight culture was inoculated in a 3-ml fresh medium and incubated with shaking until the optical density at $\lambda$ = 600 nm reaches 0.1-0.3. This exponential-phase culture was diluted to OD600 = 0.05, and 0.5 μl of the diluted cell suspension was spotted on the microchamber array on a biotin-decorated coverslip. A 5-mm × 5-mm streptavidin-decorated cellulose membrane was placed gently on the cell suspension on the coverslip, and an excess cell suspension was removed by a clean filter paper. A small piece of agar pad made with the culture medium and 1.5% (w/v) agar was placed on the cellulose membrane to maintain the culture conditions around the cells until tight streptavidin-biotin bonding was formed between the coverslip and the membrane. After 5-min incubation, the agar pad was removed, and the PDMS pad for medium perfusion was attached on the coverslip via a square-frame two-sided seal (Frame-Seal Incubation Chambers, Bio-rad). We immediately filled the device with the fresh medium and connected it to a syringe pump on the microscope stage.

### Culture conditions and sample preparation (regrowth from stationary phases)

We used E. coli MG1655 strain and cultured the cells in Luria-Bertani (LB) medium at 37°C. To prepare the cells for the time-lapse experiment, a glycerol stock of this strain was inoculated into a 2 ml LB medium and cultured with shaking for 15 hours. The cell culture was diluted in 50 ml fresh LB medium to OD600 = 0.005 and again cultured with shaking as a pre-culture. For preparing the early-stationary-phase conditioned medium, 7 ml pre-culture cell suspension at 8 hr (OD600 ≈ 4.3) was spun down at 2600 G for 12 min. The supernatant was filtered through a 0.22-μm filter. For preparing cells for time-lapse observation, a 10-μl pre-culture cell suspension at 8 hr was mixed with 240 μl early-stationary-phase conditioned medium. One μl of this diluted cell suspension was placed on the microchamber array on a biotin-decorated glass coverslip. A 5-mm × 5-mm streptavidin-decorated cellulose membrane was placed gently on the cell suspension on the coverslip, and an excess cell suspension was removed by a clean filter paper. A small piece of a conditioned medium agar pad made with 1.5% (w/v) agar was placed on a cellulose membrane to maintain the early stationary phase condition during the incubation. After 5-min incubation, the conditioned medium agar pad was removed, and the PDMS pad for medium perfusion was attached on the coverslip via a square-frame two-sided seal. We immediately filled the device with the conditioned medium and connected it to a syringe pump. We maintained the chamber filled with the conditioned medium until we started the time-lapse observation. The conditioned medium was flushed away immediately before starting the time-lapse measurement by flowing fresh LB medium. After flowing 2 ml fresh LB medium at 32 ml/hr, the flow rate was decreased and maintained at 2 ml/hr throughout the time-lapse measurement.

We followed the same procedures for the late stationary phase sample except that we sampled the cells and prepared the conditioned medium from a 24-hr pre-culture cell suspension (OD600 ≈ 3.0).

### Time-lapse measurements and image analysis

We used Nikon Ti-E inverted microscope equipped with Plan Apo $\lambda$ 100× phase contrast objective (NA1.45), ORCA-R2 cooled CCD camera (Hamamatsu Photonics), Thermobox chamber (Tokai hit, TIZHB), and LED excitation light source (Thorlabs, DC2100). The microscope was controlled by Micromanager (Edelstein et al., 2014). In the exponential phase experiments, we monitored 25-30 microchambers in parallel in one measurement and acquired the phase-contrast, RpoS-mCherry fluorescence, and GFP fluorescence images from each position with a 3-min interval. We repeated the time-lapse measurement for each culture condition three times. In the regrowth experiment from the stationary phases, we monitored 150-250 microchambers in parallel with a 3-min interval and acquired only phase-contrast images.

We analyzed the time-lapse images by ImageJ (Schneider et al., 2012). We extracted the information of cell size (projected cell area), RpoS-mCherry fluorescence mean intensity, and GFP fluorescence mean intensity of individual cells along with division timings on each cell lineage for the exponential phase experiment. We extracted only division timings on each cellular lineage for the regrowth experiments from the stationary phases and used this information for further analysis.

### Data analysis

#### Distributions and selection strength measures for division count

We calculated the distributions and selection strength measures of $D$ as follows. With the list of division counts ${D}$ for each lineage $\sigma$, the chronological and retrospective probabilities were evaluated as $P_{cl}⁢(\sigma)=2^{-D⁢(\sigma)}/N_{0}$ and $P_{rs}⁢(\sigma)=1/N_{\tau}$, respectively, where N0 is the number of cells at $t=0$ and $N_{\tau}$ is that at $t=\tau$. From these probabilities, the chronological and retrospective distributions of $D$ were obtained by summing the lineage probabilities for each division count, that is,

$$
Q_{cl}(d)=\sum\sigma:D(\sigma)=dP_{cl}(\sigma),
$$



$$
Q_{rs}(d)=\sum\sigma:D(\sigma)=dP_{rs}(\sigma).
$$

The selection strength measures, $S_{KL}^{(1)}⁢[D]$ and $S_{KL}^{(2)}⁢[D]$, were calculated as

$$
S_{KL}^{(1)}[D]=\sumd\inD_{supp}Q_{cl}(d)ln⁡\frac{Q_{cl}(d)}{Q_{rs}(d)},
$$



$$
S_{KL}^{(2)}[D]=\sumd\inD_{supp}Q_{rs}(d)ln⁡\frac{Q_{rs}(d)}{Q_{cl}(d)},
$$

where $D_{supp}$ is the support of both chronological and retrospective probabilities with respect to $D$, which is common between the two probabilities.

#### Distributions and selection strength measures for time-averaged fluorescence intensity of RpoS-mCherry and GFP

We obtained the mean fluorescence intensity of RpoS-mCherry and GFP along with the genealogical trees in the time-lapse measurements of E. coli MG1655 F3 rpoS-mcherry strain. We analyzed the time-averaged fluorescence intensity of RpoS-mCherry and GFP as a lineage trait $X$ and evaluated their distributions, fitness landscapes, and selection strength measures (Figure 7). For each cell lineage, the time-averaged fluorescence intensity was calculated as

$$
X(\sigma)=\frac{1}{N+1}\sumi=0Nx_{\sigma}(t_{i}),
$$

where $t_{i}=t_{start}+i⁢Δ⁢t$ min (tstart is the start time of the cell lineage; $Δ⁢t=3$ min is the time-lapse interval), and $x_{\sigma}⁢(t_{i})$ is the mean fluorescence intensity at time ti.

Generally, bin sizes for the fluorescence intensity affect the selection strength values. However, one can usually find the ranges of bin sizes where the results are relatively insensitive to the choice (Nozoe et al., 2017). Following an empirical rule, we set the bin width $Δ⁢X$ to

$$
Δ⁢X=0.4*IQR⁢({X}),
$$

where $IQR(X)$ is the interquartile range of the set of $X⁢(\sigma)$ from all the cell lineages. Then, the interval was defined as $I_{x,ΔX}=[x−\frac{ΔX}{2},x+\frac{ΔX}{2}]$ for $x=min⁢({X}),min⁢({X})+Δ⁢X,⋯,min⁢({X})+(L-1)⁢Δ⁢X$, where $L$ is the number of total bins given by $L=⌊\frac{max⁢({X})-min⁢({X})}{Δ⁢X}⌋+2$.

We calculated the chronological and retrospective probability distributions of $X$ by

$$
Q_{cl}(x)=\sum\sigma:X(\sigma)\inI_{x,ΔX}\frac{2^{−D(\sigma)}}{N_{0}},
$$



$$
Q_{rs}(x)=\sum\sigma:X(\sigma)\inI_{x,ΔX}\frac{1}{N_{\tau}}.
$$

$h⁢(x)$ The fitness landscape was evaluated by

$$
h⁢(x)=ln⁡\frac{N_{\tau}}{N_{0}}⁢\frac{Q_{rs}⁢(x)}{Q_{cl}⁢(x)}.
$$

The selection strength measures were evaluated by

$$
S_{KL}^{(1)}[X]=\suml=0L−1Q_{cl}(min(X)+lΔX)ln⁡\frac{Q_{cl}(min(X)+lΔX)}{Q_{rs}(min(X)+lΔX)},
$$



$$
S_{KL}^{(2)}[X]=\suml=0L−1Q_{rs}(min(X)+lΔX)ln⁡\frac{Q_{rs}(min(X)+lΔX)}{Q_{cl}(min(X)+lΔX)}.
$$

#### Cumulant generating functions and cumulants

To plot the differential of the cumulant generating functions in Figure 5F-H, we evaluated $K_{D}^{′}(ξ)=\frac{\sumd\inD_{supp}(dln⁡2)2^{ξd}Q_{cl}(d)}{\sumd\inD_{supp}2^{ξd}Q_{cl}(d)}$ by changing $ξ$ from 0 to 1 with the step size 0.01.

We calculated the cumulative contributions of fitness cumulants to the population growth $W_{n}^{(X)}$ (Figures 5A—7F-H) using a julia package, JuliaDiff/TaylorSeries.jl (Benet and Sanders, 2019; Benet and Sanders, 2021).

#### Error estimations by resampling method

To evaluate the error ranges of the quantities calculated in the analysis, we created 20,000 randomly resampled datasets for each condition and reported the means and two standard deviation ranges in the results.

For the datasets of colony growth (E. coli and M. smegmatis), $N_{\tau}$ lineages were randomly sampled with replacement according to the probability weight $P_{rs}⁢(\sigma)$ for each resampled dataset. In each resampled dataset, the initial number of cells was estimated as $N^_{0}=\sum_{\sigma\in{\sigma}_{resampled}}2^{-D⁢(\sigma)}$.

For the datasets taken using the mother machines (S. pombe and L1210), we randomly sampled N0 lineages with an equal weight, which corresponds to the chronological probability in this setting. $N_{\tau}$ was estimated as $N^_{\tau}=\sum_{\sigma\in{\sigma}_{resampled}}2^{D⁢(\sigma)}$.

#### Simulating the effect of cell removal on population growth rates

We simulated cell population growth with cell removal using a custom C script. The gamma distributions were adopted as generation time distributions. We assigned the shape parameter to $k=$ 1, 2, or 5 and the scale parameter to $\theta=2^{1/k}-1$. The perturbation strength $ϵ$ was changed from 0 to 0.2 with the interval 0.01.

As a pre-run, we started a simulation from a newborn cell and assigned its generation time randomly according to a pre-defined gamma probability distribution. We assumed that this cell divided into two daughter cells at the end of the generation. Each daughter cell was removed with probability $1-2^{-ϵ}$ and assigned with generation time from the same pre-defined probability distribution if it escaped removal. Repeating this procedure, we let the population grow until all of the remaining cell lineages in the population exceed the maximum duration $T_{max}=8.0$. The time to the next division of each cell lineage at $T_{max}$ was exported as the first division time in the main simulation. This pre-run was repeated 1000 cycles to export a sufficiently sizable list of first division times.

In the main simulation, we started from a progenitor cell with its division time randomly assigned from the first division time list exported in the pre-rum. For the daughter cells born from the first divisions and their descendants, the assignment of generation time and the cell removal were done as in the pre-run. We stopped further production of daughter cells in each lineage if it exceeded $T_{max}=8.0$. We repeated this main simulation 1,000 cycles starting from different progenitor cells. The number of cell divisions in each cell lineage until $T_{max}$ was exported for analysis.

We calculated the population growth rate at each perturbation strength as

$$
Λ⁢(ϵ)=\frac{1}{T_{max}}⁢ln⁡\frac{N⁢(T_{max},ϵ)}{1000},
$$

where $N⁢(T_{max},ϵ)$ is the number of cell lineages at $T_{max}$ when the perturbation strength was $ϵ$. The chronological and retrospective mean fitness of division count without cell removal was calculated as

$$
⟨h~(D)⟩_{cl}=\sum\sigma=1N(T_{max},0)\frac{(D(\sigma)ln⁡2)2^{−D(\sigma)}}{1000},
$$



$$
⟨h~(D)⟩_{rs}=\sum\sigma=1N(T_{max},0)\frac{D(\sigma)ln⁡2}{N(T_{max},0)}.
$$

When simulating the cell population with mother-daughter correlation time, we randomly assigned the generation time from the gamma probability distribution with its shape parameter $\frac{r⁢\tau_{m}/\theta+k⁢(1-r)}{1-r^{2}}$ and scale parameter $(1-r^{2})⁢\theta$, where $\tau_{m}$ is the generation time of the mother cell, $r$ is the correlation coefficient of generation time between neighboring generations. The stationary distribution of this transition probability approximates the gamma distribution with shape parameter $k$ and scale parameter $\theta$ to good precision with identical first and second-order moments irrespective of the parameters $k$, $\theta$, and $r$. In Figure 4—figure supplement 1, we fixed $k=2$ and $\theta=\sqrt{2}-1$ and set $r$ to 0, 0.2, 0.4, or 0.6.

#### Data and code availability

The raw data obtained in this study, the Matlab codes for data analysis, and the C code for simulation have been deposited in Github repositories (https://github.com/Wakamoto-lab/LineageAnalysis, (copy archived at swh:1:rev:1865d167f1c24625c98d3c493a9a180b1aa2035d; Yamauchi, 2021), https://github.com/Wakamoto-lab/LineageAnalysis-Julia, (copy archived at swh:1:rev:e22fbce8a713582a18fbe2bcc57dc9078090f121; Nozoe and Wakamoto, 2021) and https://github.com/Wakamoto-lab/LineageSimulation, (copy archived at swh:1:rev:ef1166620396835168ca9061851898993a091976; Wakamoto, 2021).
