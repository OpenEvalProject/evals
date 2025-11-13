# Coupling adaptive molecular evolution to phylodynamics using fitness-dependent birth-death models

## Authors

- David A Rasmussen<sup>1</sup> ([ORCID: 0000-0001-9457-7561](https://orcid.org/0000-0001-9457-7561)) †
- Tanja Stadler<sup>3</sup>

### Affiliations

1. Department of Entomology and Plant Pathology North Carolina State University Raleigh United States
2. Bioinformatics Research Center North Carolina State University Raleigh United States
3. Department of Biosystems Science and Engineering ETH Zürich Basel Switzerland
4. Swiss Institute of Bioinformatics Lausanne Switzerland

† Corresponding author

## Abstract

Beneficial and deleterious mutations cause the fitness of lineages to vary across a phylogeny and thereby shape its branching structure. While standard phylogenetic models do not allow mutations to feedback and shape trees, birth-death models can account for this feedback by letting the fitness of lineages depend on their type. To date, these multi-type birth-death models have only been applied to cases where a lineage’s fitness is determined by a single character state. We extend these models to track sequence evolution at multiple sites. This approach remains computationally tractable by tracking the genotype and fitness of lineages probabilistically in an approximate manner. Although approximate, we show that we can accurately estimate the fitness of lineages and site-specific mutational fitness effects from phylogenies. We apply this approach to estimate the population-level fitness effects of mutations in Ebola and influenza virus, and compare our estimates with in vitro fitness measurements for these mutations.

## Introduction

The fitness effects of new mutations is a key determinant of a population’s evolutionary potential to adapt over time. Studies exploring the distribution of fitness effects (DFE) in a wide range of organisms have revealed that, while many mutations are neutral, a smaller but significant fraction have substantial effects on fitness (Sanjuán et al., 2004; Eyre-Walker and Keightley, 2007; Visher et al., 2016). These findings have spurred interest in molecular evolutionary models that consider how non-neutral mutations shape sequence evolution and patterns of genetic diversity. Such models range in complexity from simple models assuming that selection operates uniformly across all sites (Muse and Gaut, 1994; Goldman and Yang, 1994; Yang and Nielsen, 2008) to parameter rich models with site-specific fitness effects (Halpern and Bruno, 1998; Lartillot and Philippe, 2004; Rodrigue et al., 2010; Hilton and Bloom, 2018). While all of these models assume sequences evolve along an underlying phylogenetic tree representing their shared common ancestry, all also assume that the mutation process driving sequence evolution is independent of the other evolutionary processes giving rise to the tree. This independence assumption implies that mutations do not feedback and affect the fitness of lineages in the tree, such that lineages carrying highly beneficial mutations are just as likely to survive and produce sampled descendants as lineages riddled with deleterious mutations (Figure 1A).

![Figure 1.](https://cdn.elifesciences.org/articles/45562/elife-45562-fig1-v3.jpg)

**Figure 1.:** (A) Standard phylogenetic models assume that there is an underlying process by which individuals replicate and give rise to a phylogeny. Mutations occur along the lineages of the tree, generating the sequence data observed at the tips. The mutation process is assumed to be independent of tree generating process, such that mutations do not impact the branching structure of the tree. (B) The MFBD allows us to relax this assumption, such that mutations at multiple sites feedback and shape both the tree and sequence data. (C) Under the original multi-type birth-death model we track $D_{n,i}⁢(t)$, the probability density that a lineage $n$ at time $t$ in state $i$ produces the subtree descending from $n$ and the observed tip states. We also track $E_{i}$, the probability that a lineage produces no sampled descendants and is therefore unobserved. (D) In the MFBD model we instead track $D_{n,k,i}⁢(t)$, the probability that a lineage $n$ in state $i$ at site $k$ produces the subtree and the observed tip states at site $k$. Because the fitness of a lineage $f_{n}$ will depend on its genotype at all sites, we use the marginal site probabilities $\omega$ to compute the probability that a lineage has a certain genotype, such as ACT (Approximation 1). We can then marginalize over the fitness of each genotype weighted by its approximate genotype probability to compute the fitness $f_{n}$ of a lineage (Approximation 2). Finally, we need to know the probability $E_{n}$ that a lineage left no other sampled descendants, which we approximate using the probability $E_{u}$ that a lineage with same expected fitness $u$ leaves no sampled descendants (Approximation 3). The schematic in A was reproduced from the original figure by Louis du Plessis (https://github.com/Taming-the-BEAST/TechnicalLectureSources/tree/master/BeastIntro2018) with permission under a Creative Commons license.

While questionable in terms of biological realism, independence between the tree generating process and the mutation process allows for tractable statistical models. Assuming independence, the joint likelihood of a phylogenetic tree $𝒯$ and the sequence data $𝒮$ at the tips of the tree having evolved as observed can be factored into two distinct components:

$$
L⁢(𝒮,𝒯|\mu,\theta)=L⁢(𝒮|𝒯,\mu)⁢p⁢(𝒯|\theta).
$$

The likelihood of the sequence data $L⁢(𝒮|𝒯,\mu)$ conditional on the tree and the mutational parameters $\mu$ can be computed efficiently for most continuous-time Markov models of sequence evolution (Felsenstein, 1981). The probability density $p⁢(𝒯|\theta)$ of the tree $𝒯$ given the parameters generating the tree $\theta$ can likewise be computed under widely used coalescent (Griffiths and Tavaré, 1994; Pybus et al., 2000) or birth-death models (Rannala and Yang, 1996; Stadler, 2009). In Bayesian phylogenetics, $p⁢(𝒯|\theta)$ is normally thought of as the prior distribution over trees rather than a likelihood, because the tree itself is inferred from the sequence data.

The assumption of independence between the mutation and tree generating processes may be unproblematic in certain scenarios, such as if mutations are truly neutral or do not contribute to substantial fitness differences among lineages. A common argument invoked in defense of ignoring non-neutral mutations is that macroevolutionary tree generating processes like speciation and extinction play out on longer timescales than the substitution process fixing or removing mutations within a population (Bustamante, 2005). In this case, fitness variation drives the substitution process within a population but does not ultimately drive the formation of a phylogeny at the species level. But such separation-of-timescales arguments do not hold when segregating mutations contribute to substantial fitness variation between lineages in a phylogeny, such as for rapidly evolving microbes where several different mutant strains can co-circulate. In these cases, the tree generating and mutation processes occur on the same timescale, and the fitness effects of mutations can feedback and shape the branching structure of a phylogeny (Kaplan et al., 1988; Nicolaisen and Desai, 2012; Neher and Hallatschek, 2013). Ignoring non-neutral evolution in this case may introduce biases into phylogenetic inference. But perhaps more importantly, fitness differences among lineages can be correlated with ancestral genotypes, providing information about the molecular basis of adaptive evolution we would otherwise ignore.

We therefore explore an approach that couples molecular sequence evolution to the tree-generating process using multi-type birth-death (MTBD) models. Under this approach, mutations can directly impact the fitness of a lineage in the phylogeny by altering its birth or death rate (Figure 1B). For a single evolving site or other character state, the joint likelihood of the phylogeny together with the observed tip states can be computed exactly under the MTBD model (Maddison et al., 2007; Stadler and Bonhoeffer, 2013; Kühnert et al., 2016). However, this approach is impractical for more than a few non-neutrally evolving sites due to the need to track all possible genotypes as separate types in the state space of the model. We therefore explore an approximate birth-death model that considers how mutations at multiple sites contribute to a lineage’s overall fitness, without the need to track all possible genotypes in sequence space. This approach allows us to infer the fitness effects of individual mutations and the fitness of any particular lineage at any time (based on its inferred ancestral genotype) from the branching structure of a phylogeny. Because our approach is particularly relevant to rapidly adapting microbial pathogens, we apply it to Ebola and influenza virus sequence data in order to quantify the fitness effects of naturally occurring amino acid substitutions.

## Materials and methods

### The MTBD at a single evolving site

At a single evolving site, the multi-type birth-death (MTBD) model of Stadler and Bonhoeffer (2013) can be used to compute the joint likelihood $L⁢(S,𝒯|\mu,\theta)$ of the sequence or character state data $𝒮$ and phylogenetic tree $𝒯$ in a way that couples the mutation process with changes in fitness along a lineage. Let $D_{n}⁢(t)$ represent the probability density (i.e. the likelihood) that the subtree descending from lineage $n$ evolved between time $t$ and the present exactly as observed (Figure 1C). Further, let $D_{n,i}⁢(t)$ represent this probability density conditional on lineage $n$ being in state $i$ out of $M$ possible states at time $t$. Here the state of a lineage refers to a particular allele or character state (e.g. nucleotide or amino acid) at a single site. We reserve the term genotype to refer to a particular configuration of states across multiple sites in a sequence.

The density $D_{n,i}⁢(t)$ can be computed going backwards in time from the present ($t=0$) to time $t$ along a lineage by numerically solving a system of ordinary differential equations:

$$
\frac{d}{dt}D_{n,i}(t)=−(\lambda_{i}+\sumj=1M\gamma_{i,j}+d_{i})D_{n,i}(t)(a)noevent+2\lambda_{i}E_{i}(t)D_{n,i}(t)(b)birthoflineagewithnosampledescendants+\sumj=1M\gamma_{i,j}D_{n,j}(t)(c) mutation from i to j
$$

Here, $\lambda_{i}$ is the birth rate and $d_{i}$ is the death rate of lineages in state $i$, and thus reflect a lineage’s fitness. Mutations between states $i$ and $j$ occur at a rate $\gamma_{i,j}$, independently of birth events. Each term in (Equation 2) describes how $D_{n,i}$ changes through time by accounting for all of the different events that could have occurred along the lineage. The first term (a) considers the change in probability density given that no birth, death or mutation event occurred. The second term (b) considers the probability of a birth event that went unobserved because one of the child lineages produced no sampled descendants (this event has probability $E_{i}⁢(t)$, see below). The third term (c) reflects the probability that the lineage mutated from state $i$ to $j$.

$E_{i}⁢(t)$ represents the probability that a lineage in state $i$ is not sampled and has no sampled descendants. This probability can be computed at any time $t$ by solving a second set of ODEs:

$$
\frac{d}{dt}E_{i}(t)=(1−s_{i})d_{i}(a)deathwithoutsampling−(\lambda_{i}+\sumj=1M\gamma_{i,j}+d_{i})E_{i}(t)(b)noevent+\lambda_{i}E_{i}(t)^{2}(c)birth,neitherchildhassampleleddescendants+\sumj=1M\gamma_{i,j}E_{j}(t).(d)mutationfromitoj
$$

The first term (a) reflects the probability that a lineage dies and is not sampled, where $s_{i}$ is the probability that a lineage in state $i$ is sampled upon dying. Terms b-d have similar interpretations as in (Equation 2).

At a tip lineage $n$, we initialize $D_{n,i}⁢(t)=d_{i}⁢s_{i}$ if the lineage was sampled upon death at time $t$. Alternatively, if $n$ was sampled at the present time $t=0$ before dying, then $D_{n,i}⁢(t)=ρ_{i}$, where $ρ_{i}$ is the probability that an individual in state $i$ was sampled at present. At a branching event, the probability density $D_{a,i}$ of the parent lineage $a$ in state $i$ giving rise to two descendent lineages $n$ and $m$ is updated as:

$$
D_{a,i}=2⁢\lambda_{i}⁢D_{m,i}⁢(t)⁢D_{n,i}⁢(t).
$$

The factor of two enters because either lineage $m$ or $n$ could have given birth and we must consider both possible events.

At the root, we can compute the probability density of the entire tree by summing over all possible root states:

$$
D_{n}=\sumi=1Mq_{i}⁢\frac{D_{n,i}⁢(t_{r⁢o⁢o⁢t})}{1-E_{i}⁢(t_{r⁢o⁢o⁢t})},
$$

where $q_{i}$ is the prior probability that the root is in state $i$ at time $t_{r⁢o⁢o⁢t}$. Including the term $1-E_{i}⁢(t_{r⁢o⁢o⁢t})$ in the denominator conditions the birth-death process on giving rise to at least one sampled individual. $D_{n}$ represents the probability that the entire tree and the tip states $𝒮$ evolved as exactly as observed. It is therefore equivalent to the joint likelihood $L⁢(𝒮,𝒯|\mu,\theta)$ we seek where $\mu={\gamma}$ and $\theta={\lambda,d,s}$.

In theory, this approach could be extended to evolution at any number of sites as long as we track $D_{n,i}⁢(t)$ for all possible genotypes $i$. Unfortunately, this approach has limited utility because the number of possible genotypes in sequence space scales exponentially with the number of sites $L$ (i.e. $4^{L}$ possible genotypes for nucleotide sequences), making the MTBD model impractical for modeling evolution at more than a few sites.

### The marginal fitness birth-death model

While the fitness of a lineage will generally depend on its genotype across multiple sites, tracking evolution in the space of all possible genotypes is, as just discussed, computationally infeasible. We therefore seek an approach that considers how mutations at multiple sites determine the fitness of a lineage without the need to track $D_{n,i}$ for all possible genotypes. In the approach described below and outlined in Figure 1D, we therefore track molecular evolution at each site, computing the probability that each site occupies each state, and then approximate the probability of a lineage being in any particular genotype based on these site probabilities. To compute the expected fitness of a lineage, we can then sum, or marginalize, over the fitness of each genotype weighted by its approximate probability. We therefore refer to this approach as the marginal fitness birth-death (MFBD) model.

First, in order to couple a lineage’s fitness with the birth-death process, we will assume that the birth rate $\lambda_{n}$ of any lineage $n$ scales according to the fitness $f_{g}$ of its genotype:

$$
\lambda_{n}=f_{g}⁢\lambda_{0},
$$

where $\lambda_{0}$ is the base birth rate assigned to a particular reference genotype (e.g. the wildtype). A lineage’s death rate can also be coupled to its fitness, but for simplicity we will assume a lineage’s fitness is reflected only in its birth rate $\lambda_{n}$.

Let $𝒢$ be the set of all possible genotypes in sequence space and $g_{k}$ be the state of genotype $g$ at site $k$. To make it clear when we are considering evolution in genotype space rather than at a particular site, we will write the probability density $D_{n,i}$ as $D_{n,g}$ when $i$ refers to a particular genotype. Furthermore, let $D_{n,k,i}$ be the probability density of the subtree descending from lineage $n$ given that site $k$ is in state $i$. By definition,

$$
D_{n,k,i}=\sum{g\in𝒢:g_{k}=i}D_{n,g},
$$

where the sum is over all genotypes in $𝒢$ with site $k$ in state $i$.

We can derive a difference equation for $D_{n,k,i}$ from $D_{n,g}$ in a straightforward manner:

$$
D_{n,k,i}(t+Δt)=\sum{g\in𝒢:g_{k}=i}D_{n,g}(t+Δt)=\sum{g\in𝒢:g_{k}=i}[(1−(f_{g}\lambda_{0}+\sumj=1M\sum{g^{′}\in𝒢:g_{k}^{′}=j}\gamma_{g,g^{′}}+d))D_{n,g}(t)Δt=+2f_{g}\lambda_{0}E_{n,g}(t)D_{n,g}(t)Δt=+\sumj=1M\sum{g^{′}\in𝒢:g_{k}^{′}=j}\gamma_{g,g^{′}}D_{n,g^{′}}(t)Δt].
$$

Taking the limit as $Δ⁢t→0$, we get a new system of differential equations for $D_{n,k,i}⁢(t)$:

$$
\frac{d}{dt}D_{n,k,i}(t)=\sum{g\in𝒢:g_{k}=i}[−(f_{g}\lambda_{0}+\sumj=1M\sum{g^{′}\in𝒢:g_{k}^{′}=j}\gamma_{g,g^{′}}+d)D_{n,g}(t)+2f_{g}\lambda_{0}E_{n,g}(t)D_{n,g}(t)+\sumj=1M\sum{g^{′}\in𝒢:g_{k}^{′}=j}\gamma_{g,g^{′}}D_{n,g^{′}}(t)]
$$

Unfortunately, (Equation 9) would still require us to track $D_{n,g}⁢(t)$ for all possible genotypes, precisely what we wish not to do. We show below that, if we can approximate $f_{g}$ and $E_{n,g}$ for any given lineage, we can write (Equation 9) in terms of only $D_{n,k,i}$ (see (Equation 19)) and therefore do not need to track each genotype.

### Approximating the fitness of a lineage

We begin by approximating the fitness $f_{n}$ of a lineage $n$. Even if we do not know the exact genotype of a lineage at a particular time, we can compute the lineage’s expected fitness by summing over the fitness of each genotype $f_{g}$ weighted by the probability $\omega_{n,g}$ that lineage $n$ is in genotype $g$:

$$
𝔼⁢(f_{n})=\sumg\in𝒢f_{g}⁢\omega_{n,g}.
$$

The same logic can be extended to compute the expected marginal fitness $𝔼⁢(f_{n,k,i})$ of a lineage $n$ that at site $k$ is in state $i$:

$$
𝔼⁢(f_{n,k,i})=\sum{g\in𝒢:g_{k}=i}f_{g}⁢\omega_{n,g}.
$$

Computing $𝔼⁢(f_{n,k,i})$ using (Equation 11) requires knowledge of the genotype probabilities $\omega_{n,g}$, which would again require us to track evolution in genotype space. We therefore introduce our major assumption: that we can approximate genotype probabilities using only the marginal site probabilities $\omega_{n,k,i}$ that site $k$ is in state $i$. We describe how we compute $\omega_{n,k,i}$ below. For now, we make the approximation that

$$
\omega^_{n,g}=\frac{\prod_{k=1}^{L}\omega_{n,k,g_{k}}}{\sum_{g\in𝒢}\prod_{k=1}^{L}\omega_{n,k,g_{k}}}.
$$

This approximation assumes that all sites evolve independently of one another, which is not generally true because mutations at different sites are linked together in genotypes with shared ancestral histories, creating correlations among sites that we ignore.

Using the approximate genotype probabilities $\omega^_{n,g}$, we can in turn approximate the expected marginal fitness of a lineage:

$$
f^_{n,k,i}=\sum{g\in𝒢:g_{k}=i}f_{g}⁢\omega^_{n,g}.
$$

If the fitness effects of each site act multiplicatively to determine the overall fitness of a lineage, we can compute $f^_{n,k,i}$ as:

$$
f^_{n,k,i}=\sigma_{k⁢i}⁢\prodl=1,l\neqkL\sumj=1M\sigma_{l⁢j}⁢\omega_{n,l,j},
$$

where $\sigma_{k⁢i}$ is the fitness effect of site $k$ being in state $i$. This formulation of $f^_{n,k,i}$ is useful if the number of sites $L$ is large and the number of genotypes we need to sum over in (Equation 13) is therefore also extremely large.

### Approximating the probability of no sampled descendants

The $E_{n,g}⁢(t)$ term in (Equation 9) represents the probability that a lineage $n$ alive at time $t$ in the past is not sampled and leaves behind no sampled descendants. $E_{n,g}⁢(t)$ therefore necessarily depends on the fitness of unobserved lineages descending from $n$ and how fitness along these lineages evolves through changes in their genotype. Because it is often easier track evolution in one dimensional fitness space rather than high-dimensional sequence space (Kepler and Perelson, 1993; Tsimring et al., 1996), we simplify this problem by tracking a proxy for $E_{n,g}⁢(t)$ though fitness space.

Let $E_{u}$ be the probability that a lineage with expected fitness $u$ leaves no sampled descendants. While fitness can take on a continuous range of values, we track these probabilities only for a discrete set of points $𝒱$ in fitness space. We can track $E_{u}$ for $u\in𝒱$ by modifying (Equation 3) to obtain:

$$
\frac{d}{d⁢t}⁢E_{u}⁢(t)=(1-s_{u})⁢d_{u}-(\lambda_{u}+\sumv\in𝒱\gamma_{u,v}+d_{u})⁢E_{u}⁢(t)+\lambda_{u}⁢E_{u}⁢(t)^{2}+\sumv\in𝒱\gamma_{u,v}⁢E_{v}⁢(t).
$$

We can then substitute $E_{n,g}⁢(t)$ in (Equation 9) with $E_{u}$ for the fitness value $u$ closest to $f_{g}$ or $f^_{n,k,i}$ in fitness space.

Tracking evolution in fitness space requires us to specify rates $\gamma_{u,v}$ for how lineages transition between fitness classes $u$ and $v$. Let $𝒢_{u}$ be the set of genotypes with expected fitness closest to $u$ out of all fitness values in $𝒱$. We approximate $\gamma_{u,v}$ as:

$$
\gamma_{u,v}=\frac{1}{|𝒢_{u}|}⁢\sumi\in𝒢_{u}\sumj\in𝒢_{v}\mu_{i⁢j},
$$

where $\mu_{i⁢j}$ is the mutation rate between genotypes $i$ and $j$. In other words, we compute the average rate of transitions out of fitness class $u$ into $v$ by summing over all possible transitions between genotypes contained within each fitness class. Note that if each genotype falls in a unique fitness class such that $|𝒢_{u}|=1$ for all $u\in𝒱$, then $E_{u}$ is computed exactly. In the Results, we compare using the approximate transition rates above to compute $E_{u}$ versus an even simpler approximation where we assume no transitions between fitness classes along unobserved lineages, which has been assumed in earlier multi-type birth-death models (Rabosky et al., 2014; Barido-Sottani et al., 2018).

### Computing the marginal site densities Dn,k,i

Recall that (Equation 9) provided an exact way to track the marginal site densities $D_{n,k,i}$ based on the genotype densities $D_{n,g}$. To efficiently evaluate $D_{n,k,i}$ without the need to track $D_{n,g}$ for all genotypes, we apply the three approximations made above. First, we approximate the genotype probabilities $\omega^_{n,g}$ based on the marginal site probabilities. Second, we marginalize over the fitness of each genotype (weighted by its genotype probability) to compute $f^_{n,k,i}$ and then substitute $f^_{n,k,i}$ for $f_{g}$ for all genotypes where $g_{k}=i$ below. Third, we approximate $E_{n,g}$ by $E_{u}$ for a single fitness value $u$ closest to $f^_{n,k,i}$. Making these approximations in (Equation 9) leads to:

$$
\frac{d}{dt}D_{n,k,i}(t)=\sum{g\in𝒢:g_{k}=i}[−(f^_{n,k,i}\lambda_{0}+\sumj=1M\sum{g^{′}\in𝒢:g_{k}^{′}=j}\gamma_{g,g^{′}}+d)D_{n,g}(t)+2f^_{n,k,i}\lambda_{0}E_{u}(t)D_{n,g}(t)+\sumj=1M\sum{g^{′}\in𝒢:g_{k}^{′}=j}\gamma_{g,g^{′}}D_{n,g^{′}}(t)]
$$

Assuming that the mutation rate from $i$ to $j$ at site $k$ does not depend on the genetic background, we can substitute $\sum_{j=1}^{M}\sum_{{g^{′}\in𝒢:g_{k}^{′}=j}}\gamma_{g,g^{′}}$ with $\sum_{j=1}^{M}\gamma_{i,j}$, where $\gamma_{i,j}$ is the per site mutation rate. We can likewise substitute $\sum_{j=1}^{M}\sum_{{g^{′}\in𝒢:g_{k}^{′}=j}}\gamma_{g,g^{′}}⁢D_{n,g^{′}}⁢(t)$ with $\sum_{j=1}^{M}\gamma_{i,j}⁢\sum_{{g^{′}\in𝒢:g_{k}^{′}=j}}D_{n,g^{′}}⁢(t)$. Making these substitutions and rearranging the sums in (Equation 17), we have:

$$
\frac{d}{dt}D_{n,k,i}(t)=−(f^_{n,k,i}\lambda_{0}+\sumj=1M\gamma_{i,j}+d)\sum{g\in𝒢:g_{k}=i}D_{n,g}(t)+2f^_{n,k,i}\lambda_{0}E_{u}(t)\sum{g\in𝒢:g_{k}=i}D_{n,g}(t)+\sumj=1M\gamma_{i,j}\sum{g^{′}\in𝒢:g_{k}^{′}=j}D_{n,g^{′}}
$$

Recalling that $D_{n,k,i}=\sum_{{g\in𝒢:g_{k}=i}}D_{n,g}$ (and by extension $D_{n,k,j}=\sum_{{g\in𝒢:g_{k}=j}}D_{n,g}$), we have:

$$
\frac{d}{dt}D_{n,k,i}(t)=−(f^_{n,k,i}\lambda_{0}+\sumj=1M\gamma_{i,j}+d)D_{n,k,i}(t)+2f^_{n,k,i}\lambda_{0}E_{u}(t)D_{n,k,i}(t)+\sumj=1M\gamma_{i,j}D_{n,k,j}(t).
$$

The significance of (Equation 19) is twofold. First, we can track sequence evolution at each site individually without tracking all genotypes. Second, given $f^_{n,k,i}$, we can track the overall fitness of a lineage by marginalizing over the fitness effects of all possible mutations at other sites. We can therefore track sequence evolution at each site while simultaneously taking into account the coupled fitness effects of mutations at all other sites on a lineage’s fitness.

Computing $f^_{n,k,i}$ still requires us to approximate the genotype probabilities using (Equation 12), which in turn requires the marginal site probabilities $\omega_{n,k,i}$. In our notation, $\omega_{n,k,i}$ represents the conditional probability $p⁢(i|𝒯_{n},𝒮_{n})$ that lineage $n$ is in particular state $i$, where $𝒯_{n}$ represents the subtree descending from $n$ with tip sequences $𝒮_{n}$ represents the inverse conditional probability density $p⁢(𝒯_{n},𝒮_{n}|i)$. We can therefore apply Bayes theorem to compute $\omega_{n,k,i}$ given $D_{n,k,i}$:

$$
\omega_{n,k,i}=p⁢(i|𝒯_{n},𝒮_{n})=\frac{p⁢(𝒯_{n},𝒮_{n}|i)⁢q⁢(i)}{\sum_{i}^{M}p⁢(𝒯_{n},𝒮_{n}|i)⁢q⁢(i)}=\frac{D_{n,k,i}⁢q⁢(i)}{\sum_{i}^{M}D_{n,k,i}⁢q⁢(i)}.
$$

The $q⁢(i)$ terms represent the prior probability that the lineage is in state $i$. Here we make a simplification in assuming that the tree ancestral and sister to lineage $n$ has no information regarding $\omega_{n,k,i}$, and thus assume a uniform prior on $q⁢(i)=1/M$. The $q⁢(i)$ terms therefore cancel above.

Because the fitness of a lineage depends on the state of all sites, we must solve (Equation 19) for all sites simultaneously as one coupled system of differential equations. This requires updating $D_{n,k,i}$ at each time step, which suggests the following iterative procedure.

At a tip $n$ observed to be in genotype $g$, we initialize $f^_{n,k,i}$ as $f_{g}$ if $g_{k}=i$ or else $f^_{n,k,i}=0$, $D^_{n,k,i}=d⁢s$ or $ρ$, and $\omega_{n,k,i}=1$ if $g_{k}=i$, else $\omega_{n,k,i}=0$. Then at each time step backwards through time from time $t$ to time $t+Δ⁢t$, for each site and state we:

### Computing the full joint likelihood

We can now compute the joint likelihood of the tree and sequence data if we track $D_{n,k,i}$ at each site back to the root. At the root, $D_{n,k,i}⁢(t_{r⁢o⁢o⁢t})$ represents $p⁢(𝒯,𝒮_{k}|\mu,\theta,i)$, the probability density of the entire tree $𝒯$ and the observed sequence data $𝒮_{k}$ as site $k$, conditional on site $k$ being in state $i$ at the root. To be precise, $D_{n,k,i}$ only approximates $p⁢(𝒯,𝒮_{k}|\mu,\theta,i)$ because we computed $D_{n,k,i}$ using the expected marginal fitness of a lineage $f^_{n,k,i}$ based on approximate genotype probabilities. We therefore introduce an additional auxiliary variable $ℱ$ representing the entire set of expected fitness values $f^_{n,k,i}$ computed over all lineages, sites and states. Using this notation, $D_{n,k,i}⁢(t_{r⁢o⁢o⁢t})=p⁢(𝒯,𝒮_{k}|\mu,\theta,ℱ,i)$. By summing over all possible root states at site $k$ (and conditioning on survival), we can then compute:

$$
p⁢(𝒯,𝒮_{k}|\mu,\theta,ℱ)=\sumi=1Mq⁢(i)⁢\frac{p⁢(𝒯,𝒮_{k}|\mu,\theta,ℱ,i)}{1-E_{u}⁢(t_{r⁢o⁢o⁢t})}=\sumi=1Mq⁢(i)⁢\frac{D_{n,k,i}⁢(t_{r⁢o⁢o⁢t})}{1-E_{n,k,i}⁢(t_{r⁢o⁢o⁢t})}.
$$

Likewise, we can compute the conditional probability density $p⁢(𝒮_{k}|𝒯,\mu,\theta,ℱ)$ of the sequence data at site $k$ given the tree:

$$
p⁢(𝒮_{k}|𝒯,\mu,\theta,ℱ)=\frac{p⁢(𝒯,𝒮_{k}|\mu,\theta,ℱ)}{p⁢(𝒯|\mu,\theta,ℱ)}.
$$

We already know $p⁢(𝒯,𝒮_{k}|\mu,\theta,ℱ)$ from above but now need the tree density $p⁢(𝒯|\mu,\theta,ℱ)$. This can easily be computed using a birth-death process where the birth rate of each lineage at any time $t$ is always rescaled by its expected fitness $f^_{n}⁢(t)$ contained within $ℱ$.

We can now compute the joint density $p⁢(𝒯,𝒮_{1:L}|\mu,\theta)$ for all sites. Because each site is conditionally independent of all other sites given $ℱ$, we can factor $p⁢(𝒯,𝒮_{1:L}|\mu,\theta,ℱ)$ into a product of densities for $𝒮_{k}$ at each site and the density of the entire tree $𝒯$:

$$
p⁢(𝒯,𝒮_{1:L}|\mu,\theta,ℱ)=p⁢(𝒯|\mu,\theta,ℱ)⁢\prodk=1Lp⁢(𝒮_{k}|𝒯,\mu,\theta,ℱ).
$$

We can thus approximate the joint likelihood of the sequence data and the phylogeny $p⁢(𝒯,𝒮_{1:L}|\mu,\theta)$ as $p⁢(𝒯,𝒮_{1:L}|\mu,\theta,ℱ)$. This allows us to consider how selection shapes sequence evolution at each site while simultaneously considering how the fitness effects of mutations at multiple sites act together to shape the phylogeny. As (Equation 23) makes clear though, the goodness of our approximation depends on how well the fitness values in $ℱ$ are approximated, which in turn depends on how well we can approximate genotypes based on the marginal site probabilities. We explore the goodness of these approximations in the Results section.

### Implementation

We first implemented the marginal fitness birth-death (MFBD) model in Matlab version R2017b. The Matlab implementation was used to test how well the MFBD model can approximate likelihoods and genotype probabilities relative to the exact multi-type birth death model tracking all possible genotypes for a simple model with only four genotypes. For statistical inference, the MFBD was implemented as an add-on package for BEAST 2 (Bouckaert et al., 2014) named Lumière, which extends the existing BDMM package for multi-type birth-death models (Kühnert et al., 2016). BEAST two is a general software platform that allows a wide range of evolutionary models including birth-death models to be fit to phylogenetic trees while jointly inferring the phylogeny using Bayesian MCMC sampling. The BEAST 2 implementation of Lumière therefore allows the joint posterior distribution of all parameters in the MFBD model and the phylogeny to be estimated from sequence data. Source code for Lumière and the Matlab implementation are freely available at https://github.com/davidrasm/Lumiere.

### Simulations

To test the statistical performance of our approach, mock phylogenies and sequence data were simulated under a birth-death-mutation-sampling process using a variant of the Gillespie stochastic simulation algorithm (Gillespie, 2007) that recorded the ancestry of all individuals in the population. A binary sequence was associated with each lineage and allowed to mutate with a constant per-site mutation rate $\gamma$. Mutations could alter the fitness of a lineage by either increasing or decreasing its birth rate according to site-specific fitness effects. At death events, lineages were sampled with probability $s$, in which case they were included in the mock phylogeny. Code for these simulations is available at https://github.com/davidrasm/Lumiere/tree/master/sim (Rasmussen, 2019; copy archived at https://github.com/elifesciences-publications/Lumiere).

### Ebola analysis

We used the Lumière implementation of the MFBD model to estimate the fitness effects of amino acid mutations previously identified to increase the infectivity of Ebola virus in human cell lines (Diehl et al., 2016; Urbanowicz et al., 2016). We reanalyzed a set of 1610 whole genome EBOV sequences sampled from Guinea, Sierra Leone and Liberia in 2014 to 2016. The sequence alignment along with the time-calibrated molecular phylogeny we used for our analysis were downloaded from https://github.com/ebov/space-time/tree/master/Data.

(Urbanowicz et al., 2016) measured the fitness effects of 17 viral genotypes carrying 18 different amino acid mutations in either single, double or triple mutant backgrounds relative to the Makona genotype first sampled at the beginning of the epidemic. Because our methods cannot estimate fitness effects of mutations at very low frequencies, we only analyzed 9 of these mutations that were present in at least 10 of the 1610 viral samples. Preliminary analysis revealed that these mutations fall within eight unique genetic backgrounds because of the way mutations are nested within other single or double mutant lineages in the phylogeny. Because the data of Urbanowicz et al. (2016) strongly suggest that epistatic interactions between mutations affect viral fitness, we estimated the genotypic fitness $f_{g}$ of these eight major genotypes rather than site-specific fitness effects $\sigma$. We therefore used the MFBD to track sequence evolution at each site, but used (Equation 13) to marginalize over these genotypes when approximating the fitness of a lineage.

We estimated the fitness of each genotype relative to the Makona genotype, assuming a uniform $[0,2]$ prior distribution on these fitness values. For the other parameters in the model, we assumed a fixed death or removal rate $d$ of 0.1667 per day based on earlier estimates (Gire et al., 2014; Stadler et al., 2014). Sampling was modeled as occurring upon removal, with the sampling proportion $s$ set to zero before March 2014, when the first sample was collected. After March 2014, we assumed a fixed sampling proportion of 0.056, reflecting the fact that the dataset included samples from 1610 individuals out of the 28,652 probable cases reported by the WHO (WHO, 2016). Lastly, we assumed a constant amino acid mutation rate over all sites with an exponential prior on both the forward and backward mutation rate with a mean rate of 2 × 10−3 per site per year. We also ran a second analysis where we included the geographic locations of lineages (Guinea, Sierra Leone and Liberia) as an additional evolving character state in our model. In this analysis, we estimated the effect of geographic location on transmission rates in Sierra Leone and Liberia relative to the base transmission rate in Guinea. Both analyses can be reproduced in Lumière with the XML input files available at https://github.com/davidrasm/Lumiere/tree/master/ebola.

### Influenza H3N2 analysis

We used the Lumière implementation of the MFBD model to estimate the fitness effects of amino acid mutations in the hemagglutinin (HA) protein of human influenza virus subtype H3N2. In order to ensure our fitness estimates were directly comparable to the mutational fitness effects previously estimated by Lee et al. (2018), we focused our analysis on viral samples in the same antigenic cluster as the A/Perth/16/2009 strain studied by Lee et al. for two reasons. First, Lee et al. (2018) showed that the fitness effects of amino acid mutations in HA vary depending on the genetic background, with greater fitness differences between more divergent strains. We therefore only considered strains with low genetic divergence from A/Perth/16/2009. Second, the deep mutational scanning experiments were performed in cell culture, and therefore do not reflect the antigenic component of viral fitness in the human population. Only considering a single antigenic cluster therefore minimizes the effect of antigenic mutations.

To further minimize additional background variation in fitness due to geography, we only considered samples collected in the United States from January 2009 to the end of 2012. Overall, we downloaded 2150 sequences from the Influenza Research Database (https://www.fludb.org/) that met these criteria. Nucleotide sequences of the HA segment were aligned in Muscle (Edgar, 2004) and a maximum likelihood phylogenetic tree was estimated in RAxML (Stamatakis, 2014) using a GTR + Gamma substitution model. To get a time-calibrated phylogeny, branch lengths in the ML tree were converted into units of real calendar time with Least Squares Dating v0.3 (To et al., 2016) using a previously estimated molecular clock rate for the HA segment of H3N2 of 5.72 x 10−3 substitutions per site per year (Rambaut et al., 2008).

In our first analysis, we estimated mutational fitness effects from the H3N2 phylogeny under the MFBD model assuming that fitness effects are multiplicative across sites, as in (Equation 14). Because of the large number of naturally occurring mutations in the HA sequences, we limited our analyses to the 17 most abundant amino acid mutations that were present in more than 10% of the sampled sequences. To compare our estimates of population-level fitness effects to fitness effects measured in vitro, we converted the relative amino acid preferences at each site from the deep mutational scanning experiments to mutational fitness effects:

$$
\theta_{k}=l⁢o⁢g_{2}⁢\frac{\pi_{k,i}}{\pi_{k,l}},
$$

where $\pi_{k,i}$ is the relative preference for amino acid $i$ at site $k$. To compute these fitness effects, we used the averaged relative amino acid preferences reported in Dataset S3 of Lee et al. (2018).

In our second analysis, we used the relative preference data from the deep mutational scanning experiments to predict the population-level fitness of viral lineages. For this analysis, we considered all naturally occurring mutations in the HA protein that were present in at least 10 samples. In all, the fitness effects of 67 mutations distributed across 56 sites were included. To map relative amino acid preferences across multiple sites to population-level fitness, we assume that the mutational fitness effects computed from the relative amino acid preferences are additive on a log2 scale, such that the fitness $f_{n}$ of a lineage is:

$$
f_{n}=(1+\alpha⁢\sumkLl⁢o⁢g_{2}⁢\frac{\pi_{k,i}}{\pi_{k,l}})^{κ}.
$$

Here, $\alpha$ is a linear scaling term that allows us to calibrate population-level fitness in terms of the sum of the site-specific fitness effects. We also include the scaling exponent $κ$ to account for curvature in the fitness landscape, as might be expected to arise if mutations interact globally through synergistic ($κ>1$) or antagonistic ($κ<1$) epistatic effects across sites (Elena et al., 2010). A complete list of the HA mutations considered, their fitness effects predicted by DMS and the XML input file needed to reproduce our analysis are available at https://github.com/davidrasm/Lumiere/tree/master/influenzaH3N2.

## Results

### The four genotype model

We first consider a simple model of molecular evolution in order to compare the marginal fitness birth-death (MFBD) model against the exact multi-type birth-death (MTBD) model tracking all genotypes. Specifically, we consider a binary evolving sequence of length $L=2$ where all mutations are deleterious and carry a selective fitness cost $\sigma$. Fitness effects of individual mutations act multiplicatively, such that the double mutant has fitness $(1-\sigma)^{2}$. With this simple model, it is therefore possible to track the evolutionary dynamics of all four genotypes ($𝒢={00,01,10,11}$) under both models.

Figure 2A shows a phylogeny simulated under the four genotype model, colored according to the genotype of each lineage. We computed the joint likelihood that this tree and observed tip genotypes evolved under a range of different fitness values $\sigma$ for both the exact MTBD and approximate MFBD models (Figure 2B). The likelihood profiles under both models peak around the true value of $\sigma$ and closely match at lower values of $\sigma$, but begin to diverge at higher values. The probability of a single hypothetical lineage being in each genotype approximated under the MFBD model is also shown against the exact genotype probabilities computed under the MTBD in (Figure 2C).

![Figure 2.](https://cdn.elifesciences.org/articles/45562/elife-45562-fig2-v3.jpg)

**Figure 2.:** (A) Simulated phylogeny showing the genotype of each lineage through time. (B) Joint likelihood of the phylogeny and tip genotypes under different values of $\sigma$ using the the approximate MFBD (solid line) or the exact MTBD model (dotted line). The vertical blue line marks the true parameter value. (C) The normalized probability of a single hypothetical lineage being in each genotype back through time based on the MFBD approximation (solid line) versus the exact MTBD model (dotted line) with $\sigma=0.5$. Note that the probabilities for genotypes 10 and 01 are identical. All parameters besides $\sigma$ were fixed at $\lambda=0.25$, $d=0.05$, $s=0.05$. The mutation rate $\gamma$ was symmetric between forward and backwards mutations and fixed at 0.05.

Because the MFBD approximates the probability of a lineage being in each genotype based on the marginal sites probabilities, we also compared how well the MFBD model approximates the genotype probability densities $D_{n,g}$ relative to the exact multi-type birth-death model. Recall that $D_{n,g}$ provides the probability that the subtree descending from a lineage $n$ has evolved exactly as observed, and therefore forms the foundation of all likelihood calculations under our model. Averaged over all genotypes, the error introduced by approximating $D_{n,g}$ under the MFBD model is greatest at intermediate mutation rates (Figure 3A). When there is no selection ($\sigma=0$), the MFBD introduces no error, but the error increases as the strength of selection increases (Figure 3B). We can also consider a variant of the four genotype model where each of the single mutant genotypes is neutral with $\sigma=0$ but an epistatic interaction between the two sites causes the double mutant to be deleterious with some fitness cost $ϵ$. Again, the error introduced by the MFBD grows as the strength of the epistatic fitness effect increases (Figure 3C).

![Figure 3.](https://cdn.elifesciences.org/articles/45562/elife-45562-fig3-v3.jpg)

**Figure 3.:** (A–C) The error introduced by approximating the genotype probability densities $D_{n,g}$ based on the marginal sites probabilities under the MFBD model for different mutation rates (A), strengths of selection (B), and epistatic fitness effects (C). The solid line represents the MFBD approximation with fitness effects coupled across sites whereas the dashed line represents a more naive approximation that ignores the fitness effects of other sites entirely. The mean error represents the time-integrated average over all genotypes. (D–F) Normalized $D_{n,g}$ probabilities for a single hypothetical lineage being in each genotype back through time based on the MFBD approximation (solid line) versus the exact MTBD model (dotted line). Each plot shows the dynamics of $D_{n,g}$ for the parameter values marked by asterisks in the plots immediately above. Other parameters are fixed at $\lambda=0.25$, $d=0.05$, $s=0.05$.

Taken together, these results suggest that the MFBD model introduces error in $D_{n,g}$ by ignoring correlations among sites due to the fact that selection acts at the level of genotypes, especially when epistasis is strong. The additional correlations between sites induced by selection then causes the genotype probabilities to deviate from those expected based on the marginal site probabilities. Conversely, at very high mutation rates, correlations between sites quickly break down so that sites evolve effectively independently of one another, such that the error introduced by the MFBD also decreases as the mutation rate becomes very high.

Overall, the magnitude of the error introduced by approximating the genotype probabilities is small, especially when we can compare the MFBD model against a more naive approximation that tracks sequence evolution at each site completely independent of all other sites by setting the expected marginal fitness $f^_{n,k,i}=\sigma$ instead of using (Equation 14). This approximation completely ignores how the fitness of a lineage depends on mutations at other sites, and the error in $D_{n,g}$ is generally considerably greater than under the MFBD model (Figure 3A–C; dashed lines). Moreover, even when the error introduced by the MFBD model is relatively large, the model still tracks the dynamics of $D_{n,g}$ backwards through time along a lineage well (Figure 3D–F; for parameter values marked by the black asterisks in A-C).

The MFBD model also approximates $E_{n}$, the probability that a lineage has no sampled descendants, using a discretized fitness space and is therefore another source of potential error. Mirroring the results for $D_{n,g}$, the error introduced by this approximation peaks at intermediate mutation rates while it increases monotonically with the strength of selection and epistatic fitness effects (Figure 4A–C). Interestingly, tracking how lineages transition between fitness classes in fitness space does not improve the approximation relative to simply ignoring changes in fitness along unobserved lineages (Figure 4A–C; dashed lines). The overall magnitude of error introduced by approximating $E_{n}$ is also small, although using a discretized fitness space does lead to some jaggedness in the dynamics of $E_{n}$ (Figure 4D–F). However, only when selection is very strong ($\sigma>0.8$) does tracking $E_{n}$ in fitness space result in significant errors, and then only in the more distant past (Figure 4E). In this case, a lineage’s fitness in the distant past may be a poor predictor of its probability of leaving sampled descendants at a time point in the distant future because the fitness of the lineage and its descendants may greatly change over time in a way that is difficult to predict without considering the exact mutational pathways through which a lineage can move in sequence space.

![Figure 4.](https://cdn.elifesciences.org/articles/45562/elife-45562-fig4-v3.jpg)

**Figure 4.:** (A–C) The error introduced by approximating $E_{n}$ in a discretized fitness space under the MFBD model for different mutation rates (A), strengths of selection (B), and epistatic fitness effects (C). The solid line represents the approximation where lineages are allowed to transition between fitness classes whereas the dashed line represents the assumption that fitness does not change along unobserved lineages. To obtain a single $E_{n}$ value comparable across both models, we summed $E_{n}$ over all genotypes weighted by the exact probability of the lineage being in each genotype and then took the time-integrated average to compute the mean error. (D–F) The dynamics of $E_{n}$ for a single hypothetical lineage back through time based on the MFBD approximation (solid line) versus the exact MTBD model (dotted line). Each plot shows the dynamics of $E_{n}$ for the parameter values marked by asterisks in the plots immediately above.

### Estimating site-specific fitness effects

Next, we simulated phylogenies under a model where the fitness effect of the mutant allele at each site is drawn independently from a distribution of fitness effects (DFE) in order to test how well we can estimate site-specific fitness effects. Because there can be considerable uncertainty surrounding these fitness effects, we now estimate the posterior distribution of fitness effects using Bayesian MCMC. The accuracy and precision of the estimated fitness effects varies considerably across sites, as shown for a representative phylogeny with five evolving sites in Figure 5.

![Figure 5.](https://cdn.elifesciences.org/articles/45562/elife-45562-fig5-v3.jpg)

**Figure 5.:** (A) A phylogeny simulated under a model with five evolving sites each with a random fitness effect. The lineages are colored according to the number of mutations they carry (blue = 0; yellow = 5). The distribution of fitness effects was assumed to be LogNormal with a mean of 0.85 and a standard deviation of 0.32. (B) Site-specific fitness effects estimated using the marginal fitness BD model. Red lines indicate the posterior median and 95% credible intervals. Blue lines mark the true fitness effect at each site.

In order to better understand this variability, we simulated 100 phylogenies with randomly drawn fitness effects at either 2, 5 or 10 evolving sites. Overall, the estimated posterior median fitness effects are well correlated with their true values, although the strength of this correlation decreases as the number of sites increases (Figure 6A–C). Coverage of the 95% credible intervals on the other hand increased from 71.0 to 72.8% to 77.4%.

![Figure 6.](https://cdn.elifesciences.org/articles/45562/elife-45562-fig6-v3.jpg)

**Figure 6.:** (A–C) Correlation between the true and estimated posterior median fitness effects for phylogenies simulated with 2, 5 or 10 evolving sites. Results are aggregated over 100 simulated phylogenies, with each point representing an estimate for a single site and phylogeny. The points are colored according to the frequency of the mutant allele among sampled individuals in the phylogeny. (D) Fitness effects estimated under the exact MTBD model tracking all four possible genotypes for the same two site simulations as in A. (E) Correlation between the site-specific fitness effects estimated under the approximate MFBD and exact MTBD for the two site simulations. (F) Error and uncertainty in estimated site-specific fitness effects across all 2, 5, and 10 site simulations. Error was calculated as the posterior median estimate minus the true fitness effect. Uncertainty was calculated as the standard deviation of the posterior values sampled via MCMC. In all simulations, sites where the Effective Sample Size of the MCMC samples was below 100 (less than 5% of all sites across simulations) were discarded. The death rate was fixed at $d=0.05$ but the birth, mutation and sampling rates were randomly drawn for each simulation from a prior distribution: $\lambda∽$ Uniform(0.1,0.2); $\gamma∽$ Exponential(0.01); $s∽$ Uniform(0,1). Only the birth rate was jointly inferred with the site-specific fitness effects.

While there is no systematic directional bias, fitness effects are underestimated for sites at which the mutant allele is at low frequency among sampled individuals and overestimated for sites where the mutant allele is at high frequencies. This however appears to be an intrinsic feature of estimating fitness effects from the branching structure of a phylogeny, as the same phenomena is observed under the exact MTBD model with two sites and four genotypes (Figure 6D), and the estimates made under the approximate MFBD model are highly correlated with estimates made under the exact MTBD model (Figure 6E).

Across all sites and simulations, accuracy decreased when the mutant allele at a given site was at low or high frequencies, and there was considerably more uncertainty for sites where the mutant allele was at very low frequencies (Figure 6F). Thus, while the MFBD model generally performs well at estimating site-specific fitness effects, the accuracy and precision of these estimates varies greatly depending on the frequency of a given mutation in a phylogeny.

### Ebola virus adaptation to humans

The Ebola virus glycoprotein (GP) binds to cells during viral cell entry and is therefore thought to be a key determinant of viral fitness in different hosts. Previously, (Urbanowicz et al., 2016) analyzed a large set of naturally occurring amino acid mutations in the GP isolated from patients during the 2013–16 epidemic in Western Africa. The effect of these GP mutations on fitness were then experimentally determined using infectivity assays in cell culture. Several mutant genotypes dramatically increased viral infectivity relative to the Makona genotype isolated during the earliest stages of the epidemic. However, the effect of these mutations on viral transmission and fitness at the host population level have not yet been determined. We therefore applied the MFBD model to a large dataset of 1610 Ebola virus (EBOV) genomes sampled during the 2013–16 epidemic to infer the population-level fitness effects of these GP mutations.

We analyzed 9 out of the 18 amino acid mutations analyzed by Urbanowicz et al. (2016) that were present in at least 10 of the 1610 viral samples. These nine mutations fall in eight different genetic backgrounds or genotypes (Figure 7). Because Urbanowicz et al. (2016) found evidence for epistatic interactions between several of these mutations, we estimated the fitness of these eight genotypes rather than site-specific mutational fitness effects. Table 1 shows the relative fitness of these genotypes estimated at the population-level versus their fitness in cell culture.

**Table 1.**
 Estimated posterior median fitness and 95% CI for the Ebola GP mutants relative to the Makona genotype


<table>
  <thead>
    <tr>
      <th>Genotype</th>
      <th>Sample freq</th>
      <th>Base model</th>
      <th>Model + geo effects</th>
      <th>Effect in cell culture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Makona</td>
      <td>0.036</td>
      <td>1.00</td>
      <td>1.00</td>
      <td>Reference genotype</td>
    </tr>
    <tr>
      <td>A82V</td>
      <td>0.720</td>
      <td>1.05 (1.04–1.07)</td>
      <td>1.26 (1.19–1.35)</td>
      <td>Increases infectivity 2X</td>
    </tr>
    <tr>
      <td>P330S</td>
      <td>0.002</td>
      <td>0.98 (0.82–1.14)</td>
      <td>1.11 (0.96–1.24)</td>
      <td>Decreases infectivity</td>
    </tr>
    <tr>
      <td>P330S+N107D+G480D</td>
      <td>0.037</td>
      <td>1.04 (0.98–1.12)</td>
      <td>1.27 (1.16–1.39)</td>
      <td>Increases infectivity &gt; 2X</td>
    </tr>
    <tr>
      <td>A82V+R410S</td>
      <td>0.044</td>
      <td>1.09 (1.00–1.18)</td>
      <td>1.31 (1.17–1.45)</td>
      <td>No or small effect</td>
    </tr>
    <tr>
      <td>A82V+R410S+K439E</td>
      <td>0.035</td>
      <td>1.14 (1.01–1.26)</td>
      <td>1.36 (1.20–1.54)</td>
      <td>Increases infectivity 2-3X</td>
    </tr>
    <tr>
      <td>A82V+R29K</td>
      <td>0.019</td>
      <td>1.06 (0.93–1.19)</td>
      <td>1.27 (1.10–1.45)</td>
      <td>Increases infectivity 2-3X</td>
    </tr>
    <tr>
      <td>A82V+T230A</td>
      <td>0.026</td>
      <td>1.03 (0.93–1.11)</td>
      <td>1.23 (1.10–1.37)</td>
      <td>Increases infectivity 2-3X</td>
    </tr>
    <tr>
      <td>A82V+I371V</td>
      <td>0.067</td>
      <td>1.03 (0.98–1.09)</td>
      <td>1.24 (1.14–1.35)</td>
      <td>Increases infectivity 2-3X</td>
    </tr>
  </tbody>
</table>

![Figure 7.](https://cdn.elifesciences.org/articles/45562/elife-45562-fig7-v3.jpg)

**Figure 7.:** Ancestral fitness values were reconstructed by first finding the probability of a lineage being in each possible genotype based on the marginal site probabilities computed using (Equation 20). Ancestral fitness values were then computed by averaging the posterior median fitness of each genotype, weighted by the probability that the lineage was in each genotype. Fitness values are given relative to the Makona genotype isolated at the start of the epidemic. Clades are labeled according to their most probable genotype.

Mapping the genotypes and fitness of lineages inferred under the MFBD model onto the phylogeny allows us to reconstruct the series of events by which EBOV adapted to humans (Figure 7). Shortly after the epidemic started in 2013, the A82V mutation occurred and gave rise to lineage B, which then spread to Sierra Leone, Liberia and Mali. (Urbanowicz et al., 2016) found that the A82V mutation increases infectivity by 2–3 fold in cell culture. At the population-level, this mutation appears to have a less dramatic effect, increasing transmissibility by only 5% relative to the Makona genotype. The P330S mutation appears to have temporarily decreased the fitness of the main surviving clade in lineage A, although mutations N107D and G480D later rescue the fitness of this lineage, consistent with the findings of Urbanowicz et al. (2016). Meanwhile, the R410S mutation occurred within lineage B but did not have an immediate effect on fitness. However, R410S appears to epistatically interact with mutation K439E, which occurs twice along the same lineage carrying the R410S mutation and in this genetic background increases infectivity 2–3 fold in cell culture. We estimate that the A82V+R410S+K439E genotype had the highest population-level fitness, but only increased fitness by 14% relative to the Makona genotype. Three other mutations, R29K, T230A and I371V, also occurred in the A82V genetic background, but were not estimated to have further increased the fitness of the A82V genotype.

Because the A82V mutation occurred along a lineage that spread from Guinea to Sierra Leone and several of the genotypes we considered were also geographically restricted, we performed a second analysis to check whether our estimates of genotype fitness were confounded by geographic differences in transmission rates. In this model, we accounted for geographic effects by including location (Guinea, Sierra Leone or Liberia) as an additional evolving character state or ‘site’ in the model. We found no evidence that transmission rates differed by location; relative transmission rates were 1.01 (95% CI: 0.97–1.05) in Sierra Leone and 0.99 (95% CI: 0.94–1.04) in Liberia compared with Guinea. All mutant genotypes had higher estimated fitness relative to the Makona genotype under the model with geographic effects due to a lower estimated fitness of the Makona genotype. However, the rank order of genotypic fitness values is consistent across models (Table 1). Overall, the population level fitness of all eight genotypes agree with their fitness in cell culture in terms of the sign or direction of their effects, but these genotypes had much greater fitness relative to the Makona genotype in cell culture than at the population level.

### Influenza H3N2 fitness variation

We also applied the MFBD model to estimate the fitness effects of mutations in the hemagglutinin (HA) protein of human influenza virus subtype H3N2. Lee et al. (2018) recently estimated the relative preference for each amino acid residue at all sites in the HA protein in cell culture using a reverse genetics approach known as deep mutational scanning (DMS). The fitness effect of mutating one amino acid to another is expected to correlate strongly with the relative preference for each amino acid in these experiments. We therefore sought to compare the population-level fitness effects of naturally occurring mutations estimated under the MFBD model with their fitness measured in vitro by DMS.

To minimize the effect of antigenic mutations, which would not be reflected in the DMS experiments, we limited our analysis to viral lineages in the same antigenic cluster as the A/Perth/16/2009 strain studied by Lee et al. (2018). We first estimated the fitness effects of the 17 most abundant mutations that reached a frequency of 10% or greater among viruses sampled in the United States between 2009 and 2012. We found no apparent relationship between the estimated population-level fitness effects of these mutations and their in vitro effects, although there is agreement that most of these mutations are nearly neutral (Figure 8A). Although the 95% credible intervals on our estimates are narrow, these results need to be interpreted with extreme caution because our MCMC algorithm never converged on a stable posterior distribution for several mutations (Effective Sample Size < 10) due to strong correlations between mutations in their estimated fitness effects. This is likely due to the fact that many of these mutations occur only once in the phylogeny and share the same ancestry and therefore genetic background as other mutations in the phylogeny (Figure 8B).

![Figure 8.](https://cdn.elifesciences.org/articles/45562/elife-45562-fig8-v3.jpg)

**Figure 8.:** (A) The fitness effects of mutations estimated in vitro using deep mutational scanning versus their estimated population-level effects. In vitro fitness effects were quantified as the relative preference for the mutant versus the consensus amino acid residue in the deep mutational scanning experiments, given on a log2 scale. Population-level fitness effects were estimated using the MFBD model assuming multiplicative effects across sites. Error bars show the 95% credible intervals on the estimated population-level fitness effects. (B) Coancestry matrix showing the fraction of ancestry shared between each pair of mutations in the H3N2 phylogeny. The coancestry value represents the fraction of branches in the phylogeny that share both mutations based on a maximum parsimony reconstruction. The diagonal gives the fraction of all branches in the phylogeny with each individual mutation.

While our population-level estimates did not correlate with the in vitro data, the fitness effects predicted by DMS correlate strongly with the maximum frequency that naturally occurring mutations reach in the human population (Lee et al., 2018). We therefore sought to test whether using the DMS experimental data to inform the MFBD model about the fitness effects of mutations, rather than estimating them independently from the phylogeny, would result in a better fit of the model to the H3N2 phylogeny and sequence data. Doing so requires a fitness model that aggregates mutational fitness effects across sites and then maps this combined fitness to the population-level fitness of a lineage. In our model, we sum the mutational fitness effects predicted by the relative amino acid preferences across all sites to get a composite predictor of fitness: $\theta_{D⁢M⁢S}=\sum_{k}^{L}l⁢o⁢g_{2}⁢\frac{\pi_{k,i}}{\pi_{k,l}}$. We then use (Equation 25) to map $\theta_{D⁢M⁢S}$ to overall population-level fitness.

Fitting our model to the H3N2 phylogeny allows us to calibrate how the mutational fitness effects based on relative preferences scale to population-level fitness. Overall, large changes in $\theta_{D⁢M⁢S}$, resulting from mutations to more or less preferred amino acid residues, have a relatively small impact on population-level fitness. Population-level fitness grows slowly and roughly linearly with mutations to more preferred amino acids (Figure 9; inset). Nevertheless, when mutational fitness effects are aggregated across all sites, there are substantial fitness differences between lineages (Figure 9). Relative to a hypothetical lineage bearing the consensus sequence, fitness ranges from 0.84 to 1.04 across lineages with many lineages having a relative fitness less than one, indicating a slightly deleterious mutation load. Accounting for these fitness differences results in the MFBD model informed by the DMS data fitting the H3N2 phylogeny substantially better (Log likelihood: −4184) than a model assuming all mutations are neutral (Log likelihood: −7510). As would be expected, lineages predicted to be more fit also tend to persist between influenza seasons. Most notably, a lineage with higher than average fitness circulates in 2009 and 2010 during the H1N1 pandemic. This lineages carries the T228A mutation, which is predicted to have a large beneficial effect in the DMS experiments. It is therefore tempting to speculate that this mutation may have conferred an advantage that helped seasonal H3N2 compete with the pandemic H1N1 virus.

![Figure 9.](https://cdn.elifesciences.org/articles/45562/elife-45562-fig9-v3.jpg)

**Figure 9.:** Fitness values were reconstructed based on a fitness model that maps mutational fitness effects predicted based on deep mutational scanning experiments to population level fitness. The inset shows this fitness mapping for the model parameters with the highest posterior probability: $\alpha=0.0098$ and $κ=0.964$. Uncertainty in ancestral amino acid sequences was taken into account by first computing the marginal site probability at each site. Ancestral fitness values were then reconstructed by marginalizing over all possible ancestral sequences using the marginal site probabilities.

## Discussion

Many assumptions are made in phylogenetics to model molecular evolution in a statistically tractable way. Historically, one of the most pervasive yet biologically questionable of these assumptions has been that sequences evolve neutrally along lineages, such the mutations do not feedback and alter the branching process shaping the phylogeny. Our marginal fitness birth-death (MFBD) model allows us to relax this core assumption in order to consider how non-neutral evolution at multiple sites affects sequence evolution, the fitness of lineages, and the overall branching structure of a phylogeny. While our approach is not exact in that it approximates genotype probabilities by assuming sites evolve independently when computing the marginal fitness of a lineage, we have shown that this approximation generally works well and only produces significant errors in rather extreme situations, such as the four genotype model with very strong selection or epistasis. While an earlier approach based on birth-death models allowed for lineage-specific fitness values to be inferred from the branching pattern of a phylogeny (Neher et al., 2014), this approach did not connect fitness back to the mutational process nor allow for the fitness effects of individual mutations or genotypes to be estimated. Using our approach, we demonstrated that the fitness effects of specific mutations can be estimated from simulated phylogenies under the MFBD with accuracy comparable to an exact multi-type birth death model. The MFBD model therefore provides a new, statistically powerful way of incorporating adaptive molecular evolution into phylodynamics.

The MFBD model allows us to exploit phylogenetic information about adaptive evolution that most methods for inferring selection from patterns in sequence data ignore. Currently, codon-substation models (Goldman and Yang, 1994; Muse and Gaut, 1994) and the related class of mutation-selection models (Yang and Nielsen, 2008) are by far the most widely used approach for inferring selection. These approaches rely on comparing sequence substitution patterns such as the dN/dS ratio of non-synonymous to synonymous substitutions across sites. These approaches can be very powerful when sequences from highly divergent taxa are compared, such that enough time has elapsed for multiple substitutions at a single site to have accumulated between lineages. But on the shorter timescales relevant to evolution within a population, substitution patterns like the dN/dS ratio are relatively insensitive to selection pressures and may produce misleading inferences of selection (Kryazhimskiy and Plotkin, 2008). For example, a highly beneficial non-synonymous mutation that occurs in a single lineage and then spreads through a population may produce a very low dN/dS ratio, indicative of purifying selection rather than adaptive evolution. In contrast, comparing the evolutionary dynamics of lineages with and without the mutation allows us to infer if that mutation confers a competitive advantage. Thus, considering the branching pattern of phylogenies provides additional information about molecular evolution not visible from substitution patterns in sequence data alone.

While new technologies increasingly allow researchers to quantify mutational fitness effects in vitro or even in vivo (Zanini and Neher, 2013; Thyagarajan and Bloom, 2014), how fitness measured in the lab translates to fitness in nature is largely unknown. This is especially pertinent for emerging pathogens whose epidemic potential often depends on new adaptive mutations (Antia et al., 2003; Longdon et al., 2014). Phylodynamic approaches like the MFBD model that can quantify fitness at the host population level are therefore greatly needed, as they offer a means to assess the epidemiological significance of mutant lineages. Extrapolating from our experience with Ebola, where the population-level fitness effects of each mutant genotype we considered matched the sign of their effect in cell culture, we suspect that fitness measured in the lab will generally agree with fitness in nature. This seems reasonable, as mutations that increase replication or cellular infectivity within hosts should generally promote transmissibility between hosts (e.g. Quinn et al., 2000; Fraser et al., 2007). But at the same time, there is no reason to believe that transmission rates will increase linearly or even monotonically with increasing within-host growth rates. We therefore expect that the magnitude of fitness effects might often greatly differ across scales, as we found for the A82V glycoprotein mutation in Ebola. While A82V doubles infectivity in cell culture, we estimated that it only increases transmissibility at the population level by 5% (95% CI: 4–7%). Interestingly, (Diehl et al., 2016) found that A82V only slightly increases viral titers in Ebola patients, which is likely a much better proxy for transmissibility than cellular infectivity, lending support to our more moderate estimates at the population level.

For influenza, we were unable to reliably estimate the fitness effects of individual mutations from the H3N2 phylogeny. We believe that these inference problems likely stem from the fact that many of these mutations occur only once in the phylogeny and in the same genetic background as other mutations in the HA protein. The shared phylogenetic ancestry of mutations creates an identifiability problem akin to the problem of collinearity in more standard regression-type models. In either case, the individual effects of highly correlated variables are difficult or impossible to infer. Nevertheless, including the mutational fitness effects predicted by deep mutational scanning experiments improved the fit of the MFBD model to the H3N2 phylogeny by thousands of log likelihood units. Accounting for these fitness effects in the MFBD model also revealed substantial variation in population-level fitness among viral lineages within a single antigenic cluster. Most lineages were reconstructed to have a slightly deleterious mutation load, consistent with earlier reports that background variation in fitness arising from deleterious mutations, not just antigenic mutations, plays a large role in determining which H3N2 lineages ultimately persist (Illingworth and Mustonen, 2012; Luksza and Lässig, 2014; Koelle and Rasmussen, 2015). Moreover, the fitness variation uncovered by our analysis likely represents only the ‘tip of the iceberg’, since there are likely mutations in other genomic segments besides HA with large fitness effects (Raghwani et al., 2017), which we did not consider.

The influenza analysis highlights some of the inevitable difficulties encountered when inferring mutational fitness effects from phylogenies. Increasing the number of sites under consideration also increases the complexity of the genetic background in which mutations occur due to the increased probability of mutations being linked to other mutations rather than occurring in isolation. This leads to strong correlations between the fitness effects of different sites in an increasingly high dimensional parameter space, making statistical inference challenging, especially using MCMC methods. Spurious correlations may also arise due to additional, unmodeled sources of fitness variation. For example, if a mutation occurs coincidently with another beneficial mutation or the mutation occurs by chance along a lineage spreading through a higher fitness environment, it will likely be inferred to increase fitness even if it is actually neutral. In the future, the MFBD should therefore be extended to account for unmodeled sources of fitness variation. For example, each lineage could be assigned a random fitness effect representing the unmodeled components of fitness variation. These random effects could then be modeled as a continuous trait evolving along lineages, such that more closely related lineages would be expected to have similar fitness and overly large changes between closely related lineages would be penalized. Such a model would then allow us to say whether a fitness effect attributed to a particular mutation could be equally well explained by random effects arising from unmodeled fitness variation. Until such a principled approach is implemented, the fitness effects of individual mutations need to be interpreted carefully unless they occur in multiple genetic backgrounds and confounding sources of fitness variation can be accounted for, as we tried to do for Ebola by including potentially confounding geographic fitness effects.

In spite of these shortcomings, we believe the MFBD model offers a powerful means to explore many questions not previously possible with strictly neutral phylodynamic models. Even if the fitness effects of individual mutations are not identifiable, it may still be possible to infer the distribution of fitness effects across sites, a key determinant of adaptive evolution that has only been explored in a few systems (Eyre-Walker and Keightley, 2007). The MFBD model can also be used to compare the fitness of a mutation or lineage across different environments, such as in different hosts of a pathogen. Finally, the MFBD is not limited to exploring sequence evolution, as the model is generalizable to any discrete character state, including phenotypic, geographic or environmental characters. Thus, more generally, our model can be thought of as a multi-trait, multi-type birth-death model that can be used to explore how different molecular and non-molecular characters interact to shape the overall fitness of lineages in a phylogeny.
