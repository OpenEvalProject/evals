# Eco-evolutionary dynamics of clonal multicellular life cycles

## Authors

- Vanessa Ress<sup>1</sup>
- Arne Traulsen<sup>1</sup> ([ORCID: 0000-0002-0669-5267](https://orcid.org/0000-0002-0669-5267))
- Yuriy Pichugin<sup>1</sup> ([ORCID: 0000-0003-3078-2499](https://orcid.org/0000-0003-3078-2499)) †

### Affiliations

1. Max Planck Institute for Evolutionary Biology Plön Germany ([ROR:0534re684](https://ror.org/0534re684))
2. Hamburg Center for Health Economics, University of Hamburg Hamburg Germany ([ROR:00g30e956](https://ror.org/00g30e956))
3. Department of Ecology and Evolutionary Biology, Princeton University Princeton United States ([ROR:00hx57361](https://ror.org/00hx57361))

† Corresponding author

## Abstract

The evolution of multicellular life cycles is a central process in the course of the emergence of multicellularity. The simplest multicellular life cycle is comprised of the growth of the propagule into a colony and its fragmentation to give rise to new propagules. The majority of theoretical models assume selection among life cycles to be driven by internal properties of multicellular groups, resulting in growth competition. At the same time, the influence of interactions between groups on the evolution of life cycles is rarely even considered. Here, we present a model of colonial life cycle evolution taking into account group interactions. Our work shows that the outcome of evolution could be coexistence between multiple life cycles or that the outcome may depend on the initial state of the population – scenarios impossible without group interactions. At the same time, we found that some results of these simpler models remain relevant: evolutionary stable strategies in our model are restricted to binary fragmentation – the same class of life cycles that contains all evolutionarily optimal life cycles in the model without interactions. Our results demonstrate that while models neglecting interactions can capture short-term dynamics, they fall short in predicting the population-scale picture of evolution.

## Introduction

Multicellular organisms are found everywhere. In all major branches of complex multicellularity (animals, plants, fungi, red and brown algae), organisms are formed by cells staying together after cell division – unlike unicellular species, in which cells part their ways before the next division occurs (Márquez-Zacarías et al., 2021; Herron et al., 2022). However, organisms have to reproduce as otherwise their species will eventually go extinct. For a multicellular organism, this means that some cells must depart in order to develop into an offspring individual. The combination of organism growth and reproduction constitutes a clonal life cycle. Emergence of clonal multicellular life cycles was the central innovation in the earlier stages of the evolution of multicellularity. There, traits, which do not even exist for unicellular species, become crucial for long-term success of even the most primitive colony of cells (Maynard Smith and Szathmáry, 1995, Michod, 2007). These include the number of cells in the colony, how often cells depart to give rise to new colonies, how large the released propagules are, and how many of them are produced. As the reproduction and, consequently, fitness of simple cell colonies are dependent on these traits, they immediately become subjected to natural selection, favoring some life cycles over others. Since complex multicellular life descends from those loose cell colonies, the understanding of the prior evolution of primitive life cycles is essential to our understanding of the later evolution of complex traits (Ratcliff et al., 2012; De Monte and Rainey, 2014; Hammerschmidt et al., 2014; Doulcier et al., 2020).

There are several theoretical approaches to the modeling of the evolution of multicellular life cycles. The mechanistically simplest class of models assumes that natural selection operates by means of growth competition. Colonies are born small, but due to cell divisions they increase in size and, eventually, fragment, so the number of colonies in the population increases. The life cycle maximizing the population growth rate has a selective advantage as it outgrows all competitors (Roze and Michod, 2001; Libby et al., 2014; Pichugin et al., 2017; Pichugin et al., 2019; Staps et al., 2019; Gao et al., 2019; Pichugin and Traulsen, 2020; Gao et al., 2021; Pichugin, 2022; Pichugin and Traulsen, 2022). For groups made of identical cells, growth competition models of evolution predict that some life cycles cannot be the winners of this growth competition under any conditions. For instance, if the fragmentation event is instantaneous and its execution does not cost anything to the group, only fragmentation into two pieces can evolve (Pichugin et al., 2017; Pichugin and Traulsen, 2020). And indeed, the division into two pieces is, by a large margin, the most common reproductive strategy among microscopic life forms.

However, these models, due to their conceptual simplicity, assume unconstrained (exponential) growth of the population, which cannot be sustained for a prolonged period of time, because resources and space are limited. Other models consider density-dependent growth (Rossetti et al., 2011; Tarnita et al., 2013; van Gestel and Nowak, 2016; Doulcier et al., 2020, Henriques et al., 2021), where the population growth decreases with the number of groups. A similar approach is the Moran birth–death process on the group level, where whenever a new group emerges, one other group dies (Traulsen and Nowak, 2006; Matias Rodrigues et al., 2012; Simon et al., 2013; Luo, 2014; Kaveh et al., 2016; Olejarz et al., 2018; Cooney, 2019; Cooney, 2020). While the population dynamics of density-dependent population growth is vastly different from the exponential explosion found in models of unconstrained growth, these two approaches lead to identical results for life cycle evolution: as shown in Pichugin and Traulsen, 2020, the dynamics of the fraction of a given life cycle in a population are identical in models with unconstrained and density-dependent growth. Therefore, even in models with density-dependent growth, the evolutionary success of the life cycle is still fully determined by the population growth rates.

Nevertheless, density-dependent growth is also a simplification as different groups may differ in their competitiveness. For instance, large-cell colonies are able to block single cells from access to vital resources (Rainey and Travisano, 1998; Rainey and Rainey, 2003; Hammerschmidt et al., 2014), which may even lead to a complete extinction of solitary cells. Thus, the population dynamics of multicellular life cycles is not necessarily density dependent, but could be frequency dependent – the impact of resource limitation on the population growth depends on both the size and the composition of the population.

Hence, the evolution of multicellular life cycles cannot always be reduced to growth competition, but may arise from eco-evolutionary dynamics.

From a broader empirical perspective, frequency-dependent dynamics is found to be common among microbial populations (Levin, 1988; Ribeck and Lenski, 2015; Healey et al., 2016; Friedman et al., 2017). From the perspective of the theoretical ecology, frequency-dependent evolutionary dynamics arising from interactions between diverse population members has also been considered in detail (May, 1972; Wangersky, 1978; Bomze, 1983; Huang et al., 2015; Huang et al., 2017; Bunin, 2017; Barbier et al., 2018; Kotil and Vetsigian, 2018; Tarnita, 2018; Farahpour et al., 2018; Park et al., 2019; Park et al., 2020). The impact of interactions between individuals is recognized in the context of the emergence of aggregative multicellularity, where cells come together to form collectives (Garcia and De Monte, 2013; De Monte and Rainey, 2014; Garcia et al., 2015; Miele and De Monte, 2021). However, both empirical and theoretical ecology approaches tend to overlook frequency dependence in the context of clonal life cycles, where the organism’s growth in the course of the life cycle may cause a change in its role in interactions (but see an example in Tverskoi and Gavrilets, 2022 modeling evolution of germ–soma differentiation).

In this article, we developed a model of the evolution of clonal life cycles under frequency-dependent dynamics, implemented in the form of frequency-dependent colony death rate. We focus on three questions:

We first address these questions in the context of simpler models with unconstrained growth. In these models, a population performing any life cycle grows exponentially, the competition between life cycles always results in a single one outcompeting all others (which life cycle will be the winner depends only on the growth/death rates but not on the initial composition of population), and finally, the winner always comes from a limited subset of life cycles (in the simplest version of the model with costless fragmentation – it must be a fragmentation mode producing exactly two offspring). We found that including frequency-dependent interactions between organisms performing different life cycles and thus constraining the total population size changes the answers to these questions. First, the population dynamics leads to a stationary state with a finite population size. Second, we found that interactions between groups allow for situations with bistability or coexistence of multiple life cycles – scenarios impossible in the unconstrained growth model. Third, evolutionary stable strategies in our present model always belong to a limited subset of life cycles – the same one containing possible winners of growth competition in models without group interactions. Thus, we found that despite the fundamental differences between our present model and simpler models with unconstrained growth, some of their results have a direct analogy in a much more general eco-evolutionary context considered here.

## Model

### Population dynamics of a single life cycle

We consider a population consisting of cell groups that grow in size and fragment, giving rise to new groups. Cells within a group of size $i$ divide at rate $b_{i}$, thus a group of size $i$ grows at rate $i⁢b_{i}$. Groups also die due to both external environmental factors and within-population competition for resources or space. The death rate of groups of size $i$ due to external factors is $d_{i}$. Frequency-dependent competition is modeled as the death of groups of size $i$ upon encounter with groups of size $j$ at rate $K_{i,j}$ (see Figure 1A).

![Figure 1.](https://cdn.elifesciences.org/articles/78822/elife-78822-fig1-v1.jpg)

**Figure 1.:** (A) There are four processes occurring in the model: groups grow by cell division, which occurs with rates $b_{i}$, groups spontaneously die with rates $d_{i}$, groups fragment immediately upon exceeding maturity size $m$ (3 in this example), according to predefined fragmentation pattern $κ$ (1 + 1 + 1 + 1 here), and groups of size $i$ die due to the competition with groups of size $j$ at rates $K_{i⁢j}$. (B) Together, group growth and fragmentation constitute a life cycle, in which initially small groups grow in size and eventually fragment, giving rise to more small groups. Colors represent group sizes: red, solitary cells; green, bicellular groups; blue, tricellular groups.

Whenever a group of maturity size $m$ grows to $m+1$ cells, it immediately fragments. The fragmentation always occurs by the same pattern and determines the life cycle of a population. We represent a fragmentation pattern by $κ$ – a partition of a number $m+1$. For example, the fragmentation pattern of the unicellular life cycle, in which two daughter cells always go apart, is $κ=1+1$ (see Figure 1B). Other fragmentation patterns correspond to multicellular life cycles. The simplest of them are the life cycles in which groups grow up to two cells, but fragment upon reaching size three. Such a fragmentation can be performed in two ways: either detachment of a single cell, leading to the fragmentation pattern $κ=2+1$, or fission into three solitary cells, $κ=1+1+1$ (see Figure 1B). For simplicity, we assume that the cell number does not change during fragmentation (no cell loss), the sum of a fragmentation pattern $κ$ is equal to $m+1$.

If we denote the abundance of cell groups containing $i$ cells as $x_{i}$, then the dynamics of population is described by a system of differential equations

$$
\frac{dx_{1}}{dt}=−b_{1}x_{1}−d_{1}x_{1}+mb_{m}\pi_{1}(κ)x_{m}−x_{1}\sumj=1mk_{1,j}x_{j},\frac{dx_{i}}{dt}|_{i>1}=(i−1)b_{i−1}x_{i−1}−ib_{i}x_{i}−d_{i}x_{i}+mb_{m}\pi_{i}(κ)x_{m}−x_{i}\sumj=1mk_{1,j}x_{j},
$$

where the first two terms $(i−1)b_{i−1}x_{i−1}−ib_{i}x_{i}$ describe the growth of groups – the positive term represents growth from size $i-1$ to $i$ and the negative term represents growth from $i$ to $i+1$. The third term $-d_{i}⁢x_{i}$ is the environmentally caused death. The term $m⁢b_{m}⁢\pi_{i}⁢(κ)⁢x_{m}$ describes the birth of new groups of size $i$ via fragmentation of larger groups, where $\pi_{i}⁢(κ)$ is the number of groups of size $i$ produced in the result of that fragmentation. Finally, $-x_{i}⁢\sum_{j=1}^{m}K_{i,j}⁢x_{j}$ is the death of groups due to the competition between groups.

Summarizing the dynamics into matrix notation, the system (1) can be written as

$$
\frac{dx}{dt}=Ax−diag⁡(Kx)x.
$$

Here, $x$ is the column vector of group abundances

$$
x=(x_{1},x_{2},x_{3},…,x_{m})^{T}.
$$

The linear term $Ax$ represents the processes of group growth, fragmentation, and frequency-independent death. The matrix $A$ of size $m\timesm$ is called a population projection matrix in the field of formal demography – in the sense of the projection of the current state into the future state. For an arbitrary life cycle, matrix $A$ is given by

$$
A=(-b_{1}-d_{1}00…0m⁢b_{m}⁢\pi_{1}⁢(κ)b_{1}-2⁢b_{2}-d_{2}0…0m⁢b_{m}⁢\pi_{2}⁢(κ)02⁢b_{2}-3⁢b_{3}-d_{3}…0m⁢b_{m}⁢\pi_{3}⁢(κ)003⁢b_{3}⋱0m⁢b_{m}⁢\pi_{4}⁢(κ)⋮⋮⋮⋱⋱⋮000…(m-1)⁢b_{m-1}m⁢b_{m}⁢\pi_{m}⁢(κ)-m⁢b_{m}-d_{m}).
$$

The elements of the population projection matrix $A_{i,j}$ represent changes to number of groups of size $i$ due to processes occurring with groups of size $j$ (but not due to interactions). Hence, the population projection matrix has nonzero elements only on the main diagonal (group death and growth of groups to larger sizes), lower subdiagonal (growth of smaller groups), and rightmost column (fragmentation at the end of the life cycle). The elements of the competition matrix $K$ are given by $K_{i,j}$ for $i,j=1,…,m$. The operation $diag⁡(⋅)$ takes an input vector of length $m$ and transforms it into a diagonal matrix of size $m\timesm$ with the entries of the input vector on the main diagonal.

### Population dynamics of multiple life cycles

To investigate the eco-evolutionary dynamics of clonal life cycles, we consider a composition of subpopulations executing various life cycles: $κ^{(1)},κ^{(2)},…κ^{(r)}$. In this composite population, the cell growth ($b_{i}$), environmentally caused (constant) group death ($d_{i}$), and group fragmentation ($\pi_{i}(κ)$) occur independently in each subpopulation. However, frequency-dependent death due to competition entangles the dynamics of the subpopulations as groups with different life cycles growing together have to compete with each other. If we denote with $x_{i}^{(j)}$ the number of groups containing i cells in a subpopulation executing the life cycle $κ^{(j)}$, the dynamics of the composite population is described by the differential equations

$$
\frac{dx_{1}^{(j)}}{dt}=−b_{1}x_{1}^{(j)}−d_{1}x_{1}^{(j)}+m^{(j)}b_{m^{(j)}}\pi_{1}(κ^{(j)})x_{m^{(j)}}^{(j)}−x_{1}^{(j)}\sump=1r\sumk=1nK_{1,k}x_{k}^{(p)},\frac{dx_{i}^{(j)}}{dt}|_{i>1}=(i−1)b_{i−1}x_{i−1}^{(j)}−ib_{i}x_{i}^{(j)}−d_{i}x_{i}^{(j)}+m^{(j)}b_{m^{(j)}}\pi_{i}(κ^{(j)})x_{m^{(j)}}^{(j)}−x_{i}^{(j)}\sump=1r\sumk=1nK_{i,k}x_{k}^{(p)},
$$

where $m^{(j)}$ is the maturity size of the life cycle $κ^{(j)}$, and $n=max⁡(m^{(1)},m^{(2)},…,m^{(r)})$ is the maximal maturity size in the composite population. The difference between the one life cycle system (1) and the system of multiple life cycles (5) is in the last term, where groups from every competing subpopulation contribute to frequency-dependent death.

In vector form, the state of the composite population is described by a concatenation of vector states of each subpopulation:

$$
x~=(x^{(1)^{T}},x^{(2)^{T}},…,x^{(r)^{T}})^{T}=(x_{1}^{(1)},…,x_{n}^{(1)},x_{1}^{(2)},…,x_{n}^{(2)},…,x_{1}^{(r)},…,x_{n}^{(r)})^{T},
$$

where $x~$ is the column vector describing the state of the composite population, $x^{(j)}$ is the column vector describing $j$th subpopulation in a form (3). Note that the last entries of any $x^{(j)^{T}}$ will be zero if $m^{(j)}<n$. The dynamics of the composite population in Equation (5) can be represented in the vectorized form, similar to Equation (2):

$$
\frac{dx~}{dt}=A~x~−diag⁡(K~x~)x~.
$$

Here, the composite population projection matrix representing the cell growth, environmentally caused (constant) group death, and group fragmentation is a diagonal block matrix

$$
A~=(A^{(1)}00…00A^{(2)}0…000A^{(3)}…0⋮⋮⋮⋱⋮000…A^{(r)}),
$$

where $A^{(i)}$ is the population projection matrix of the life cycle $κ^{(i)}$ extended to size $n\timesn$ ($n$ is the maximal maturity size across all competing life cycles). If the maturity size of the life cycle $i$ is $m^{(i)}=n$, this matrix has a form exactly as in Equation (4). If the maturity size is smaller, $m^{(i)}<n$, then the top-left $m^{(i)}\timesm^{(i)}$ has the form (4), while the remaining elements are nonzero at the main diagonal and the lower subdiagonal, as dictated by Equation (5).

The composite competition matrix $K~$ is constructed as

$$
K~=(KKK…KKKK…KKKK…K⋮⋮⋮⋱⋮KKK…K),
$$

where each block $K$ is a competition matrix.

### Invasions from rare

In the general case, the investigation of the composite population dynamics given by Equation (7) is a very complex problem without a general solution. Hence, in our study we consider a specific class of initial conditions – invasion from rare, where the composite population contains only two subpopulations: the abundant ‘resident’ executing life cycle $κ^{(R)}$ and rare ‘invader’ executing different life cycle $κ^{(I)}$. This scenario represents an emergence of a mutant in previously stable population of the resident. The population changes if this mutant is capable of invading the resident – otherwise, the mutant goes extinct and the resident population remains the same.

In this scenario, the composite dynamics in Equation (7) can be disentangled into resident and invader components. Since the invader population is small, its contribution to frequency-dependent competition is negligible. The members of the resident population compete predominantly between themselves, so the resident dynamics is effectively a single-species scenario,

$$
\frac{dx^{(R)}}{dt}≈[A^{(R)}−diag⁡(Kx^{(R)})]x^{(R)}=0=A^{(R,R)}x^{(R)∗},
$$

where the vector $x^{(R)}$ represents the composition of the resident population, $A^{(R)}$ is the population projection matrix of the resident, $x^{(R)⁣*}$ is the equilibrium composition, and we introduced the self-invasion population projection matrix $A^{(R,R)}=A^{(R)}-diag⁡(Kx^{(R)⁣*})$. Since the resident is assumed to be at a stable equilibrium in the absence of invaders, the self-invasion matrix $A^{(R,R)}$ has an eigenvalue that is zero, and the equilibrium population composition $x^{(R)}$ is given by the corresponding eigenvector. The resident population dynamics can be obtained by solving the nonlinear Equation (10), which in the general case can be performed only numerically.

The rare invader population also competes primarily with the resident and self-competition is negligible. Thus, its dynamics is given by

$$
\frac{dx^{(I)}}{dt}≈[A^{(I)}−diag⁡(Kx^{(R)∗})]x^{(I)}=A^{(I,R)}x^{(I)},
$$

where vector $x^{(I)}$ represents the composition of the invader population, and we introduced the invasion matrix

$$
A^{(I,R)}=A^{(I)}−diag⁡(Kx^{(R)∗}).
$$

Unlike the resident dynamics, the dynamics of the invader population is linear – the invasion population projection matrix $A^{(I,R)}$ is independent from the invader population state $x^{(I)}$. The linear dynamics of clonal life cycles has been extensively studied in previous work (Pichugin et al., 2017). If the largest eigenvalue of the invasion matrix $A^{(I,R)}$ is positive, then the invader population will increase in numbers, independently of its initial demography. Otherwise, the invader population goes extinct.

The assumption of a negligible impact of the invader population on competition limits the analysis to the early stages of invasion, when the invader population is small. Nevertheless, this makes it possible to investigate the stability of resident life cycles with respect to invasions.

## Results

We first briefly recap the population dynamics and evolution under a more basic model with unconstrained growth ($K_{i⁢j}=0$) (Pichugin et al., 2017; Pichugin and Traulsen, 2020). This model has three main features. First, a population executing a single life cycle grows exponentially in the long run. The population growth rate is given by the leading eigenvalue of the population projection matrix ($A$) and the demographic composition is given by the associated eigenvector. Second, selection always finds a single winner. In a composite population, where different subpopulations execute different life cycles, only one life cycle survives in the long run – the one that has the largest growth rate. This outcome is independent of the initial state of the population. Third, some life cycles cannot be optimal under any combination of cell division rates ($b_{i}$) and group death rates ($d_{i}$). In the simplest case of instant and costless group fragmentation, life cycles with more than two offspring cannot win the growth competition.

Next, we consider how these features transfer to a system taking into account competition between groups. We begin with the dynamics of a single life cycle (section ‘Dynamics of a single life cycle’) in a system with a population size constraint, which is very different from exponential growth. Then, we consider how the competition proceeds in our model: for two (section ‘Competition between pairs of life cycles may result in coexistence or bistability’) and multiple life cycles (section ‘Competition between multiple life cycles’), where a rich spectrum of possible stationary states is found. After that, we outline the restrictions imposed on evolutionary stable strategies (section ‘The set of possible evolutionary stable strategies is restricted’). We conclude with presenting scenarios of a special interest: interactions with killer and victim kernels, where the evolutionary dynamics is reduced to the competition for growth rate and carrying capacity respectively (section ‘Killer and victim kernels guarantee a dominance of a single life cycle’), and investigate the competition between unicellular and multicellular life cycles (section ‘Conditions promoting the evolution of multicellular life cycles’).

### Dynamics of a single life cycle

For the simplest unicellular life cycle ($κ=1+1$), where population is composed only of solitary cells, the dynamics of our model given by Equation (2) reduces to logistic growth,

$$
\frac{dx_{1}}{dt}=(b_{1}−d_{1})x_{1}−K_{1,1}x_{1}^{2},
$$

where the net growth rate is equal to $b_{1}-d_{1}$ and the carrying capacity is $(b_{1}-d_{1})/K_{1,1}$. The characteristic feature of logistic growth is that the population approaches the carrying capacity with time, starting from either high or low populations size (see Figure 2A). The population dynamics of more complex life cycles also bears similarity to the logistic growth of the unicellular life cycle. If a population is small, the competition term is small, so the population grows exponentially. While population size increases, so does the competition term – group mortality rises and the overall population growth slows down. The growth stops when the population reaches a stationary state $x^{*}$, where

$$
\frac{dx^{∗}}{dt}=Ax^{∗}−diag⁡(Kx^{∗})x^{∗}=0.
$$

![Figure 2.](https://cdn.elifesciences.org/articles/78822/elife-78822-fig2-v1.jpg)

**Figure 2.:** (A) For a unicellular life cycle $1+1$, our model is equivalent to logistic growth. There, the number of solitary cells (red) approaches the carrying capacity from any initial state. (B, C) For multicellular life cycles (2 + 1 depicted), the population also approaches such a stationary state from any initial state. (B) shows the dynamics of solitary cells (red) and bicellular groups (green) with time. (C) shows the trajectories of the population composition, the dot marks the stationary state. (B) and (C) show the same dataset.

Numerical simulations show that a population executing a single life cycle always comes to the same stationary state $x^{*}$ from any initial distribution of group sizes (see Figure 2B and C).

### Competition between pairs of life cycles may result in coexistence or bistability

A composite population containing several subpopulations executing different life cycles also reaches a stationary state. In the simplest case, only one life cycle survives, while others go extinct. However, we found that the stationary state may contain more than one life cycle (coexistence). Also, the stationary state may depend on the initial state of the population (multistability). Neither of these can occur in the linear model without competition.

To illustrate these effects, we focus on a pair of life cycles ($κ^{(1)},κ^{(2)}$) with the special initial conditions, where one of these life cycles is abundant, while the other one is rare. The life cycle $κ^{(1)}$ can invade from rare into the abundant $κ^{(2)}$ if the largest eigenvalue of the invasion matrix $A^{(1,2)}$ is positive; see Equation (12). Otherwise, the rare life cycle $κ^{(1)}$ goes extinct. For a pair of life cycles, there are four possible scenarios of invasion from rare (see the outline in Table 1 and corresponding dynamics in Figure 3).

**Table 1.**
 Competitive interactions in a pair of life cycles can lead to the dominance of either life cycle, their coexistence, or bistability.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2">λ(A(1,2))&lt;0κ(1) cannot invade into κ(2)</th>
      <th rowspan="2">λ(A(1,2))&gt;0κ(1) can invade into κ(2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>λ(A(2,1))&lt;0 κ(2) cannot invade into κ(1)</td>
      <td>Bistability between κ(1) and κ(2)</td>
      <td>Dominance of κ(1)</td>
    </tr>
    <tr>
      <td>λ(A(2,1))&gt;0 κ(2) cannot invade into κ(1)</td>
      <td>Dominance of</td>
      <td>Coexistence of κ(1) and κ(2)</td>
    </tr>
  </tbody>
</table>

![Figure 3.](https://cdn.elifesciences.org/articles/78822/elife-78822-fig3-v1.jpg)

**Figure 3.:** Each panel shows the evolutionary trajectories of populations with various initial abundances of the life cycles 1 + 1 and 2 + 1 (lines) and all final states (dots). In (A), colors indicate to which of two stationary states the trajectory converges. Birth and death rates are $b=(1,0.5)$ and $d=(0,0)$; they favor the unicellular life cycle 1 + 1 in the absence of competition. Simulations performed on each panel only differ in the competition matrix K shown in panels.

Life cycle $κ^{(1)}$ dominates life cycle $κ^{(2)}$ if $κ^{(1)}$ spreads from rare, but $κ^{(2)}$ does not. This is equivalent to the leading eigenvalue of the invasion matrix $A^{(1,2)}$ being positive, while the leading eigenvalue of $A^{(2,1)}$ is negative. Then, independently of the initial conditions, only the life cycle $κ^{(1)}$ survives in the long run (see Figure 3B). The opposite signs result in the dominance of $κ^{(2)}$ over $κ^{(1)}$ (see Figure 3C).

Beyond a dominance of one life cycle over another, it is possible that each life cycle is able to spread in the abundance of another. This happens when the leading eigenvalues of both invasion matrices $A^{(1,2)}$ and $A^{(2,1)}$ are positive. There, the result of interactions between life cycles is a coexistence of both – an outcome impossible in the model without competition (see Figure 3D).

Finally, the leading eigenvalues of both invasion matrices could be negative – then neither of the life cycles can invade into another. Then, the result is a bistability between life cycles, where the outcome of interactions depends on the initial conditions – another result impossible in the model without competition (see Figure 3A).

The competition between groups plays a major role in determining which of the four invasion patterns occurs. For instance, it is possible that a life cycle having an advantage in the raw growth rate (i.e., dominating in the unconstrained growth model) is dominated by the result of the competition (see Figure 3C), where the life cycle 1 + 1 has a faster growth but 2 + 1 still dominates due to the advantage of multicellular groups in competition.

### Competition between multiple life cycles

Extending our analysis beyond just a pair of life cycles, we considered the evolutionary dynamics in a population with multiple of them. We numerically investigated the evolutionary dynamics in a population containing all life cycles in which groups do not exceed a size of three cells. There are seven such life cycles: unicellular (1 + 1), two with bicellular groups (2 + 1 and 1 + 1 + 1), and four with groups of three cells (3 + 1, 2 + 2, 2 + 1 + 1, and 1 + 1 + 1 + 1) (see Figure 4A). We generated a set of 13,000 randomly drawn combinations of growth and competition rates from an exponential distribution with unit rate parameter. For each set, we simulated 100 independent replicates of population dynamics that differ in the initial conditions (abundances and demographic composition of each of the seven life cycles).

![Figure 4.](https://cdn.elifesciences.org/articles/78822/elife-78822-fig4-v1.jpg)

**Figure 4.:** (A) The schematics of the life cycles taking part in evolution. Groups colored according to the number of cells. (B) The frequencies of various classes of outcomes. A single life cycle (yellow) is the most common. Coexistence of life cycles (red) and bistability between them (blue) are less common. More complex composite configurations (gray) are also possible, but found rarely.

These runs were classified by the state of population at the end of simulation (see Figure 4B and Table 2). The majority of simulations (about 75%) resulted in the survival of a single life cycle across all 100 replicates. The next most common outcome is a coexistence between two or more life cycles – found in about 17% of simulations. Also, a multistability between two or three life cycles was observed in about 6.5% of simulations. Here, coexistence describes a situation where the stationary state of the population is composed of the same set of at least two life cycles in every replicate. Multistability describes a situation, where in every replicate the stationary state contained only a single life cycle, but there were different stationary states among the replicates. More complex outcomes were also observed – these were the compositions of multistability and coexistences, which contributed to only about 1.5% of simulations. The most common of these composite situations is a minimal combination of bistability and coexistence: there are two possible stationary states, one is a single life cycle and another is a coexistence of two other life cycles (0.7% of simulations).

**Table 2.**
 Observation frequencies of different kinds of evolutionary outcomes in a population with multiple competing life cycles.


<table>
  <thead>
    <tr>
      <th colspan="2">Outcome</th>
      <th>Frequency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">Single life cycle</td>
      <td>0.751</td>
    </tr>
    <tr>
      <td rowspan="3">Coexistence of</td>
      <td>Two life cycles</td>
      <td>0.121</td>
    </tr>
    <tr>
      <td>Three life cycles</td>
      <td>0.044</td>
    </tr>
    <tr>
      <td>Four or more life cycles</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td rowspan="3">Multistability between</td>
      <td>Two life cycles</td>
      <td>0.065</td>
    </tr>
    <tr>
      <td>Three life cycles</td>
      <td>0.002</td>
    </tr>
    <tr>
      <td>Four or more life cycles</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="2">Composite configurations</td>
      <td>Bistability with a coexisting pair</td>
      <td>0.007</td>
    </tr>
    <tr>
      <td>Other configurations</td>
      <td>0.007</td>
    </tr>
  </tbody>
</table>

The numerical investigation of evolutionary dynamics of multiple life cycles revealed that a diverse range of outcomes are possible, including multistability and coexistence of life cycles, as well as their combinations. At the same time, the most common result is still the dominance of a single life cycle.

### The set of possible evolutionary stable strategies is restricted

Between simple dominance and multistability, about 80% of evolutionary simulations ended with the survival of a single life cycle. This happens if a life cycle is an evolutionary stable strategy (ESS), for example, if it is abundant, it cannot be invaded by any other life cycle. In the basic model without competition, the life cycle with the maximal growth rate also satisfies the definition of an ESS. Here, we found that the set of evolutionary stable strategies is similarly restricted – it also contains only fragmentations into exactly two pieces.

To show this restriction, we consider a triplet of life cycles $κ^{(1)}$, $κ^{(2)}$, $κ^{(3)}$. If the life cycle $κ^{(1)}$ is a resident, there are four variants of its stability against invasions: (i) either it is stable against invasions from both $κ^{(2)}$ and $κ^{(3)}$ (then $κ^{(1)}$ is an ESS), or (ii) stable against only $κ^{(2)}$, or (iii) stable against only $κ^{(3)}$, or (iv) both $κ^{(2)}$ and $κ^{(3)}$ can invade. Similar four variants exist for the two other life cycles. As a result, for the whole triplet, there are $4^{3}=64$ possible pairwise invasion patterns, which could feature 0, 1, 2, or 3 evolutionary stable strategies.

Numerical simulations show that all 64 patterns can be expressed for the same triplet of life cycles for some combination of cell birth, group death, and competition rates (see Figure 5A). We generated a set of 40,000 randomly drawn combinations of these rates from an exponential distribution with unit rate parameter and analyzed the pairwise invasion patterns for each. The six most frequent patterns, comprising 77% of the generated dataset, feature a hierarchical dominance, where the life cycles can be ordered in a way that higher-order life cycle dominates (always invade) lower-order life cycles. These six patterns are all possible hierarchical dominance triplets as there are exactly six ways how three items can be placed in order. If we use the same analysis for the basic, linear model with unrestricted growth, we will only observe hierarchical dominance as larger growth rate results in domination there. On the opposite side of the frequency spectrum, the two most rare patterns feature cyclic dominance, together comprising only 0.015% of the dataset. There, in any pair of life cycles one dominates another but the whole triplet follows a ‘rock–paper–scissors’ dynamics with no evolutionary stable strategies present (cf. Park et al., 2020).

![Figure 5.](https://cdn.elifesciences.org/articles/78822/elife-78822-fig5-v1.jpg)

**Figure 5.:** (A) For a combination of three life cycles, there are $223=64$ pairwise invasion patterns possible. For the triplet $κ^{(1)}=5+3,κ^{(2)}=4+4,κ^{(3)}=4+2+2$, the rates of all processes ($b_{i},d_{i},K_{i,j}$) were randomly sampled from an exponential distribution with unit rate parameter. Then the pairwise invasion pattern was identified. All 64 possible patterns were observed in these simulations. (B) In a similar investigation for the triplet $κ^{(C⁢1)}=2+2,κ^{(C⁢2)}=4+4,κ^{(M)}=4+2+2$, in which $κ^{(C⁢1)}$ and $κ^{(C⁢2)}$ constrain $κ^{(M)}$, only eight patterns were found; see the main text for a discussion.

While an arbitrary triplet of life cycles may demonstrate up to 64 invasion patterns, some triplets, which we will call ‘constrained,’ feature much smaller diversity of patterns. A triplet is constrained if the fragmentation rule of one (constrained) life cycle $κ^{(M)}$ can be represented as a combination of fragmentation rules of two other (constraining) life cycles $κ^{(C⁢1)}$ and $κ^{(C⁢2)}$. The simplest example is the triplet $κ^{(C⁢1)}=2+1$, $κ^{(C⁢2)}=1+1$, $κ^{(M)}=1+1+1$, where the fragmentation of a three-celled group into three solitary cells ($3→1+1+1$) can be presented as a combination of the detachment of a single cell ($3→2+1$) immediately followed by the dissolution of the two-cell group ($2→1+1$). A lot of constrained triplets can be constructed, for example, in our illustrations we use the triplet $κ^{(C⁢1)}=2+2,κ^{(C⁢2)}=4+4,κ^{(M)}=4+2+2$. Originally, constrained triplets emerged in the model with unconstrained growth (Pichugin et al., 2017), where the growth rate of the constrained life cycle $κ^{(M)}$ was found to be always between growth rates of the constraining life cycles $κ^{(C⁢1)}$ and $κ^{(C⁢2)}$. It follows that in the present model with competition ($K_{i⁢j}\neq0$), each of two constraining life cycles ($κ^{(C⁢1)}$ and $κ^{(C⁢2)}$) must be either stable against two others or unstable against both. The constrained life cycle $κ^{(M)}$ in turn is always invaded by one of constraining life cycles and is stable against the other (see Appendix 1). Hence, the number of possible pairwise invasion patterns for such a triplet is limited to $2⋅2⋅2=8$ (see Figure 5B). Among these eight patterns, two feature hierarchical dominance, where the life cycles can be ordered in a way that a higher-order life cycle dominates the lower-order life cycles (with the constrained life cycle $κ^{(M)}$ always being in the middle of hierarchy) (see Figure 6A). In a larger dataset (66,000 entries) with random birth, death, and competition rates, hierarchical dominance was observed in about 78% of entries. Two patterns feature bistability between constraining life cycles $κ^{(C⁢1)}$ and $κ^{(C⁢2)}$ (see Figure 6B). These patterns appear in about 11% of the dataset. Two more patterns feature a coexistence between all three life cycles (see Figure 6C). Note that unlike a pair of life cycles with unique coexistence equilibrium considered in section ‘Competition between pairs of life cycles may result in coexistence or bistability,’ the triplet features a range of stable coexistence states. The coexistence pattern is similarly frequent, observed in 11% of the dataset. Finally, the least frequent two patterns are non-hierarchical dominance, where one constraining life cycle dominates another, but in the abundance of the constrained life cycle, the invasion pattern is inverse (see Figure 6D). They appear with three orders of magnitude lower frequency, smaller than 0.01% of cases.

![Figure 6.](https://cdn.elifesciences.org/articles/78822/elife-78822-fig6-v1.jpg)

**Figure 6.:** Four patterns are shown here and four more are symmetric to them. Blue lines are population dynamics trajectories with different initial composition of the population. Red points are final states. Black arrows show directions of invasion from rare. (A) In a hierarchical dominance, one of the constraining life cycles outcompetes the two others from any initial condition. (B) In a bistability situation, each of the two constraining life cycles is able to outcompete the third life cycle. Which of them will survive depends on the initial conditions. Trajectories converging to different stationary states are highlighted with different colors. (C) In a coexistence, all three life cycles survive to a stationary state. (D) In a non-hierarchical dominance, one of the constraining life cycles outcompetes another; however, in the abundance of the constrained life cycle, the dominance is reversed. The parameters used to produce these figures are presented in Appendix 5.

The fundamental feature of constrained triplets is that any constrained life cycle ($κ^{(M)}$) can always be invaded by exactly one constraining life cycles ($κ^{(C⁢1)}$ and $κ^{(C⁢2)}$). Hence, any life cycle, which can be constrained by two others, cannot be an ESS. We found that any life cycle with more than two offspring can be constrained (see Appendix 1 for the proof). As a result, only binary fragmentation life cycles can be evolutionary stable strategies.

### Killer and victim kernels guarantee a dominance of a single life cycle

As shown above, the evolutionary dynamics of interacting life cycles can be quite complex. In this context, a special interest attracts these cases, where the complexity of dynamics is limited. In this section, we present two forms of interaction matrices ($K$), which guarantee that the evolutionary outcome is a straightforward domination of a single life cycle.

The first special case is the killer kernel, defined as

$$
K_{ij}=k_{j}.
$$

There, the probability of a group to die in an encounter depends only on the size of the opponent group ($j$), hence the name.

For an arbitrary killer kernel, a single life cycle has the same demographic composition in the stationary state as it has in the no-interactions model ($K_{i⁢j}=0$) (see Appendix 2 for the proof).

This feature of the demography leads to the result that the outcome of evolution under a killer kernel is also the same as in the no-interaction model. To show that, consider a composite population containing multiple life cycles; its dynamics is described by Equation (7) and depends on the composite projection ($A~$) and competition ($K~$) matrices. If the competition matrix $K$ is a killer kernel, the composite competition matrix $K~$ defined in Equation (9) is a killer kernel as well. Since the population dynamics of both single and multiple life cycles are governed by equations with the same structure (Equation (2) and (7), respectively), the results of Appendix 2 carry over to a composite population. Specifically, the stationary state of the composite population is proportional to the eigenvector of the composite population projection matrix $A~$ corresponding to its leading eigenvalue. The composite population projection matrix $A~$ defined in Equation (8) is a block diagonal matrix, composed of population projection matrices of the life cycles constituting the composite population. Thus, the leading eigenvalue of $A~$ is the largest among the eigenvalues of all population projection matrices comprising $A~$. Additionally, the corresponding eigenvector has nonzero components only at the positions in $x~$ associated with the block having the maximal leading eigenvalue – that is, only that life cycle constitutes the stationary state. This rule is equivalent to the choice of the fastest growing life cycle in the linear model. Thus, the evolution of life cycles competing by a killer kernel ($K_{i⁢j}=k_{j}$) can be reduced to growth competition, which results in the survival of only one life cycle.

Another special case is the victim kernel defined as

$$
K_{ij}=k_{i}.
$$

There, the chance of a group to die depends only on the size of that group ($i$). For an arbitrary victim kernel, the carrying capacity of a single life cycle can be explicitly found. The total number of groups at the stationary state $N^{*}=\sum_{i}x_{i}^{*}$ is equal to the growth rate of this life cycle in the no-interaction model ($K_{i⁢j}=0$) with modified cell division rates $b_{i}^{′}=b_{i}/k_{i}$ and group death rates $d_{i}^{′}=d_{i}/k_{i}$ (see Appendix 3 for the proof).

We found that in the composite population with many life cycles interacting by a victim kernel, only one survives in the long run (see the proof in Appendix 3). In such a scenario, each life cycle grows in numbers if the total population size is smaller than the carrying capacity of that life cycle (derived in Appendix 3). If the whole population size exceeds this value, the life cycle gradually dies out. Hence, selection favors the life cycle with the largest carrying capacity because it can grow in a dense population, when all other life cycles die from intense competition.

In both killer and victim kernels, the evolutionary dynamics is reduced to optimization of a single trait: growth rate for the killer kernel and carrying capacity for the victim kernel. Thus, the result of selection in these scenarios is a dominance of a single life cycle over all suboptimal competitors.

### Conditions promoting the evolution of multicellular life cycles

We conclude our findings with one of the most biologically interesting cases – the evolution of multicellular life cycles in a population dominated by unicellular organisms. This is also one of the simplest scenarios as it deals with the simplest, unicellular life cycle 1 + 1.

If a unicellular population is abundant in the system, its stationary state can be explicitly found (see Appendix 4). Hence, for an arbitrary invading multicellular life cycle $κ^{(M)}$, its invasion matrix ($A^{(M,1)}$) can be found explicitly. As a result, a multicellular invader can spread from rare in a population of unicellular residents if this life cycle has a positive growth rate in a model with unconstrained growth with modified group death rates,

$$
d_{i}^{′}=d_{i}+\frac{b_{1}−d_{1}}{K_{1,1}}K_{i,1}.
$$

The successful multicellular invader drives the unicellular life cycle to extinction if the unicellular life cycle cannot invade from rare. If the unicellular life cycle is an invader, its invasion matrix ($A^{(1,M)}$) has size $1\times1$ and the invasion rate is just equal to its only element. The unicellular life cycle cannot invade into a multicellular resident life cycle if

$$
b_{1}−d_{1}−\sumi=1m^{(M)}K_{1,i}x_{i}^{(M)∗}<0,
$$

where $m^{(M)}$ is the maximal group size in the life cycle $κ^{(M)}$, and $x_{i}^{(M)⁣*}$ is the composition of the population when $κ^{(M)}$ is abundant. Derivations of both conditions are presented in Appendix 4.

## Discussion

In this article, we have added an ecological dimension to the problem of life cycle evolution. Specifically, we are interested in three aspects of the eco-evolutionary dynamics: (i) What is a population dynamics of a single life cycle? (ii) What is the evolutionary dynamics of multiple life cycles? (iii) What are the possible constraints on the outcomes of that evolution? All three questions has been extensively studied for the model with unconstrained growth (Pichugin et al., 2017), and it is natural to contrast our current findings with these results.

First, the introduction of group competition completely changes the population dynamics of the life cycle growth. Instead of the exponential explosion of the population size occurring in the model with unconstrained population size, the growth in our current model slows down with the population size. Eventually, the population approaches a stationary state with the limited population size and constant composition (see Figure 2B).

Second, frequency-dependent selection arising from competition allows diverse outcomes of evolution: the stationary state can feature a coexistence of multiple life cycles or multistability between several possible end states, as shown in Figure 3. By contrast, evolution in the model with unconstrained growth always results in a survival of a single life cycle, independently of the initial conditions.

Third, despite all the differences in the population and evolutionary dynamics, the restrictions on the possible evolutionary stable strategies are exactly the same in the models with and without population size constraints (see section ‘The set of possible evolutionary stable strategies is restricted’). In both models, an ESS may only feature a fragmentation into exactly two pieces. Any life cycle producing more than two offspring can always be invaded by another life cycle with a smaller number of offspring.

Beyond the scope of our model, life cycles with fragmentation into multiple pieces may become evolutionary stable strategies if fragmentation is costly (e.g., imposes a risk of cell loss). There, binary fragmentation is no longer special as a fragmentation into multiple pieces can win growth rate competition. Nevertheless, constrained triplets of life cycles still exist under a costly fragmentation scenario but the constraining condition is different from the one presented here. There, a life cycle containing two different subsets of offspring with the same combined size is constrained between two life cycles, which use either of these subsets twice (Pichugin and Traulsen, 2020). For instance, $κ^{(M)}=2+1+1$ is constrained as it has different offspring subsets 2 and $1+1$ with the same combined size. This life cycle is constrained between life cycles $κ^{(C⁢1)}=2+2$ and $κ^{(C⁢2)}=1+1+1+1$, which use one of these subsets twice. Since the scenario of costly fragmentation still contains constrained triplets, life cycles satisfying the rule above, such as 2 + 1 + 1, cannot be evolutionary stable strategies there. Note that this rule works in the present model too (so there are actually two ways to construct constraining triplets), but it is a weaker condition than the rule presented in section ‘The set of possible evolutionary stable strategies is restricted’ and does not allow to construct any additional constraining triplets.

In the broad context of the eco-evolutionary dynamics, our dynamical Equations (2) and (7) bear a similarity with the generalized Lotka–Volterra (GLV) equations widely used in ecology: both contain a linear growth term and a nonlinear competition term (typically of the second order) balancing out the linear growth. However, our equations are not equivalent to the GLV. In the GLV, individuals corresponding to different elements of the population vector reproduce independently, that is, in our terms, the population projection matrix $A$ is diagonal. In our model, however, an individual group changes its state in the course of the life cycle and the population projection matrix $A$ is not diagonal. Of course, if the population projection matrix $A$ can be diagonalized, we can perform a linear transformation $x→Cy$ ($C$ is a matrix) to make the linear term in our model diagonal as in GLV. However, in this case, the interaction term will lose the GLV form of the modification of the growth rate ($-x_{i}⁢\sum_{j}K_{i⁢j}⁢x_{j}$, see Equation (1)) and will become a general second-order term instead ($-\sum_{j⁢k}K_{i⁢j}⁢x_{j}⁢x_{k}$). Given that our system is not a GLV in disguise, it is surprising how much of the analysis presented here has been performed using the approaches designed to analyze GLV systems.

In this article, we found that the competition plays a major role in the evolution of multicellular life cycles. Our choice of the competition matrix values was driven by theoretical aspects of this article: we either use randomly drawn values for numerical simulations or choose specific forms leading to analytical results. Yet, competition in natural populations is neither random nor fine-tuned to mathematically beautiful outcomes. What might empirical competition matrices in a stage-structured population look like? Unfortunately, the demographics of simple multicellular species is not sufficiently studied experimentally. Still, we can consider an example of emergence of Pseudomonas fluorescens colonies, where a competition plays a major role in the population dynamics and evolution (Rainey and Travisano, 1998; Rainey and Rainey, 2003; Hammerschmidt et al., 2014). In a still liquid media, these initially unicellular bacteria evolve a ‘glue’ production, which causes formation of multicellular aggregates. These aggregates float atop the media, gaining an exclusive access to oxygen. Once the entire surface is covered by continuous bacterial biofilm, the unicellular phenotype living in the body of the media is completely denied the oxygen access and dies out. In the framework of our study, the competition matrix $K$ is determined by the capability to block oxygen and surface area access. Naturally, the more cells there are in the group, the more stress they apply to others and, at the same time, the more resistant to competition they are. In the limit of small population size, single cells have almost no impact on others ($K_{i,1}≪1$) and are the most susceptible to oxygen denial ($K_{1,i}≫1$). In opposite limit, an established mat of millions of cells just drives everything else to extinction ($K_{i,j≫1}≫1$). For arbitrary competitors size, the terms $K_{i⁢j}$ should increase with the size of an opponent group ($K_{ij}<K_{i,j+1}$) but decrease with the size of the focal group ($K_{ij}>K_{i+1,j}$). Similar competition matrices should arise in scenarios where being bigger is better.
