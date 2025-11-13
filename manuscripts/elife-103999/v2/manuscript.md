# The dominant–egalitarian transition in species-rich communities

## Authors

- David A Kessler<sup>1</sup> ([ORCID: 0000-0002-5279-1655](https://orcid.org/0000-0002-5279-1655)) †
- Nadav M Shnerb<sup>1</sup> ([ORCID: 0000-0003-4418-6284](https://orcid.org/0000-0003-4418-6284)) †

### Affiliations

1. Department of Physics, Bar-Ilan University, Ramat-Gan Ramat-Gan Israel ([ROR:03kgsv495](https://ror.org/03kgsv495))

† Corresponding author

## Abstract

Diverse communities of competing species are generally characterized by substantial niche overlap and strongly stochastic dynamics. Abundance fluctuations are proportional to population size, so the dynamics of rare populations is slower. Hence, once a population becomes rare, its abundance gets stuck at low values. Here, we analyze the effect of this phenomenon on community structure. We identify two distinct phases: a dominance phase, in which a tiny number of species constitute most of the community, and an egalitarian phase, where it takes a finite fraction of all species to constitute most of the community. Using empirical data from microbial, planktonic, and macroorganismal systems, we demonstrate the relevance of this transition and show how demographic stochasticity and immigration critically determine phase behavior. Our results suggest that even slight changes in noise strength or immigration rates can lead to abrupt shifts in community diversity.

## Introduction

Many ecological systems contain numerous competing species, strains, or types (Hutchinson, 1961; Stomp et al., 2011; ter Steege et al., 2013; Connolly et al., 2014; Fierer et al., 2007). In such systems, it can be assumed a priori that the structure of the community essentially reflects resource competition among species (Gause, 2003; Tilman, 1982), with factors such as niche overlap and fitness differences playing a central role in the community assembly (Chesson, 2000; Chesson, 2003). Analyzing these factors and their impact is crucial for understanding the dynamics of these systems, and consequently, for our ability to intervene in these dynamics to achieve desired outcomes – from maintaining biodiversity in a changing world to successfully altering the state of the gut microbiome (David et al., 2014; Grilli, 2020; Eguíluz et al., 2019; Cooper et al., 2024; Callaghan et al., 2021).

Unfortunately, progress in this area has been quite difficult. The coexistence of many species remains largely puzzling, especially given the competitive exclusion principle (Tilman, 1982) and the strict constraints on the stability and feasibility of such complex systems (May, 1972). Moreover, quantifying the relevant parameters in diverse communities is extremely challenging, particularly considering the high level of stochasticity typically present in ecological dynamics. As a result, approaches inspired by statistical physics, which examine generic models through a few summary statistics, have gained significant popularity in recent years (Fisher and Mehta, 2014; Kessler and Shnerb, 2015; Bunin, 2017; Barbier et al., 2018; Grilli, 2020; van Nes et al., 2024).

Broadly speaking, attempts to present a generic analysis of diverse communities can be divided into two main approaches that differ in their interpretation of what determines dominance. In one class of models, the identity of the high-abundance species reflects intrinsic fitness differences (whether through growth rates, competitive advantage, or resource-use efficiency) so that the dominant species are effectively the ‘fittest’ (Fisher and Mehta, 2014; Bunin, 2017; Barbier et al., 2018; Azaele and Maritan, 2023; Marcus et al., 2022). In contrast, an alternative view holds that dominance arises from contingent stochastic dynamics: species happen to be abundant not because they are intrinsically superior, but as a result of random historical trajectories. These trajectories may reflect demographic noise, environmental stochasticity, or even deterministic chaos in systems with complex interactions.

The prototype of this second class of approaches was introduced in the neutral model proposed by Crow and Kimura, 1970 and Hubbell, 2001. In the original neutral models, demographic stochasticity – the inherent randomness in the birth–death process at the individual level – is the sole driver of abundance variations. Analytical solutions to these models are relatively easy to obtain (Volkov et al., 2003; Azaele et al., 2015) and have been quite successful in explaining the observed species abundance distributions (SADs), as well as other static patterns, in both regional and local communities (Rosindell et al., 2011). However, pure demographic stochasticity cannot account for dynamic patterns, whether evolutionary (such as the time to the most recent common ancestor) (Nee, 2005; Ricklefs, 2006) or ecological (such as the dynamics of abundance variation and similarity indices) (Leigh, 2025; Chisholm and O’Dwyer, 2014; Kalyuzhny et al., 2014b; Kalyuzhny et al., 2014a). Demographic stochasticity results in relatively slow and weak abundance variations, whereas observed variability is much stronger and occurs more rapidly (Kalyuzhny et al., 2014b; Chisholm et al., 2014).

The time-averaged neutral model (Kalyuzhny et al., 2015) addresses these limitations by relaxing the assumption of time-independent fitness. In this model, the relative fitness of each species fluctuates over time, but all species share the same mean fitness. The analysis of the time-averaged neutral model is more complex, as environmental stochasticity can facilitate coexistence through the storage effect (Chesson and Warner, 1981). However, the significance of this effect diminishes in highly diverse systems (Dean et al., 2017; Danino and Shnerb, 2018; Pande and Shnerb, 2022; Meyer et al., 2022).

Recent studies have highlighted a notable effect of environmental stochasticity in competitive communities, known as ‘stickiness’ (van Nes et al., 2024) or ‘diffusive trapping’ (Dean and Shnerb, 2020). Under environmental stochasticity, abundance variations are proportional to population size, meaning that the dynamics of rare species is slow, causing them to linger near the extinction point for extended periods. van Nes et al., 2024 suggested that this stickiness enables time-averaged neutral models to produce patterns – such as changes in abundance over time, dominant species turnover, and community egality – that closely resemble those observed in real ecological communities. Similar results were found by Mallmin et al., 2024 in a system of competing species for which the overall dynamics are chaotic. This makes sense, given that the relative fitness of a specific species depends on the abundances of its competitors, so if these abundances fluctuate strongly over time, as they do in the chaotic phase, the community will likely reach a state that resembles time-averaged neutrality.

Our main goal in this article is to identify a previously unrecognized phase transition between dominant and egalitarian communities. To describe this transition, we define the number of dominant species, $S_{1/2}$, as the minimum number of species that must be grouped together at a given moment to account for more than half of the total population. The level of equality in the community is then measured by the egality ratio, $S_{1/2}/S$, where $S$ is the total species richness. We show that in the dominance phase, the growth of $S_{1/2}$ with $S$ is sublinear, so the egality parameter approaches zero as $S→∞$, whereas in the egalitarian phase, $S_{1/2}$ grows linearly with $S$, and the egality parameter converges to a finite value. We demonstrate the existence of these two phases through analysis of empirical data on patterns of commonness and rarity across a wide range of ecological systems, from tropical forest trees to the human microbiome.

During the analysis and comparisons with the empirical data, we also arrived at two important insights.

The dominant–egalitarian phase transition has practical implications. A small decrease in the immigration rate or, alternatively, a small increase in the level of stochasticity can lead to a sharp decline of the diversity within a given community. Moreover, in the section ‘Materials and methods’, we have examined cases in which neutrality is broken, including fitness differences and asymmetry in the competitive interaction matrix. The results of this study demonstrate that the phase transition between the egalitarian and dominance regimes is not an artifact of perfect neutrality, but remains robust over a finite region of parameter space near the neutral point.

## Results

As we have already mentioned, without external immigration, the stickiness will eventually cause the abundance of all species, except one, to drop below any finite threshold, leading the community to a state of monodominance. To avoid disrupting the continuity of the main discussion, we detail and demonstrate this claim in ‘SI A’ (see also the supplement to Figure 1). Therefore, the basic model we study is given by

$$
\frac{dN_{i}}{dt}=\mu+N_{i}(1−\frac{\sumj=1SN_{j}}{K})+r_{i}(t)N_{i}\frac{dr_{i}}{dt}=−\frac{r_{i}}{\tau}+\thetaη_{i}(t),
$$

where $N_{i}$, $i=1,…,S$ is the abundance of the ith species. $K$ sets the overall carrying capacity. The growth rate of the ith species is  $1+r_{i}(t)$, where $r_{i}(t)$ is an independently fluctuating variable, with a correlation time $\tau$, driven by the white noise $η_{i}$. The immigration rates of all species are identical and given by $\mu>0.$ Further details on the model are given in the ‘Materials and methods’ section.

![Figure 1.](https://cdn.elifesciences.org/articles/103999/elife-103999-fig1-v2.jpg)

**Figure 1.:** Red circles: results of a simulation of the process described in Equation 1 with parameters $S=200$, $\mu=0.6$, $K=2⋅10^{6}$, $\sigma~_{e}=0.1$ and $\tau=8$. The values of the extracted parameters for Equation 4 are $c=0.0034$ and $\sigma~_{e}^{2}=0.0131$. The solid line in blue is the expression of Equation 4 with parameters $\alpha=91.2$ and $\beta=1.56$.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/103999/elife-103999-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Species abundances (left), log-abundance (middle), and the egality parameter $S_{1/2}/S$ (right) for the model considered in the main text of van Nes et al., 2024, Parameters are $S=100$, $\sigma~_{e}=0.005$ and $K=100$.The dynamics of Equation SA2 was integrated. The log-abundance of all species performs a random walk (middle), hence, as time goes by, more and more species get stuck at negligible abundances (this is the diffusive trapping, or stickiness of the rare state, left), and only a single species dominates the community and the egality parameter decreases to $1/S$.

is an independently fluctuating variable, with a correlation time $\tau$, driven by the white noise $η_{i}$. The immigration rates of all species are identical and given by $\mu>0.$ Further details on the model are given in the ‘Materials and methods’ section.

### Stickiness and species abundance distribution

Without immigration, the carrying capacity parameter $K$ plays no role in the dynamics. Actually, by defining $N_{i}=Kn_{i}$ one may rescale Equation 1 to $K=1$. When immigration is introduced, the parameter $K/\mu$ expresses the ratio between the carrying capacity and the typical minimum level of population size. The larger this ratio, the stronger the stickiness effect.

On top of that, since stickiness arises from environmental stochasticity, it becomes stronger as $\sigma~_{e}^{2}≡\theta^{2}\tau^{2}$ increases. Dimensional analysis reveals that the dimensionless parameter that governs stickiness is

$$
\gamma≡\frac{K⁢\sigma~_{e}^{2}}{\mu}.
$$

The larger $\gamma$ is, the stronger is the stickiness, and the community approaches monodominance when $\gamma→∞$; for example, when $\mu→0$.

In order to advance in the analysis, we are interested in replacing Equation 1, which provides us with a description of an $S$-dimensional system where each species can affect every other species, with an effective, one-dimensional equation for a focal species, considering all others as a single rival species. In the classical neutral theory, with pure demographic stochasticity, this can be done trivially, as the species identity of a particular individual plays no role in the dynamics. In the time-averaged neutral theory, however, the situation is much more subtle.

The distinction between neutral and time-averaged neutral models – as it arises in the attempt to derive an effective one-species description – was clarified in Danino and Shnerb, 2018 and Steinmetz et al., 2020, and has to do with the difference between the time-averaged growth rate of a given species and the population-averaged growth rate of the community. In Equation 1, the linear growth rate of each species is $1+r(t)$. Since the $r$ process is symmetric around zero, the time-average growth rate of each species is unity. Nevertheless, the instantaneous growth rate of the community is, on average, greater than 1. At any given moment, the fitter species are growing faster, so that on average more than 50% of the individuals belong to instantaneously beneficial species. As a result, the typical value of $\sumjN_{j}>K$, and therefore the dynamics of a single species satisfies the effective one-dimensional stochastic differential equation,

$$
\frac{dN}{dt}=\mu+(\frac{\sigma_{e}^{2}}{2}−c)N+\sigma_{e}η(t)N,
$$

where $c=E[(\sumjN_{j}−K)/K]$. The noise in the net growth rate of the ith species arises from two sources, the first being the direct effect of $η_{i}(t)$, and the second being the fluctuations in the competition term, $−\sumjN_{j}/K$. The two parameters $c$ and $\sigma_{e}$ may be measured, for any given values of $K$, $S$, and $\sigma~_{e}$, from long simulations of Equation 1. Unless we are looking at the most abundant species, the correlations between the competition term and $η_{i}$ are small, and the two contributions are roughly independent. Thus, the overall effect of these two contributions is

$$
\sigma_{e}^{2}≈\sigma~_{e}^{2}+\sigma_{c}^{2}
$$

Here, $\sigma_{c}^{2}$ is the time integral of the two-time correlation function of $c$ and equals $2\tauVar[\sumN_{i}/K]$. For example, for $\sigma~_{e}=0.01$, $S=200$, $K=2⋅10^{6}$, $\mu=0.6$, we have $\sigma_{c}^{2}≐0.0031$ and $\sigma_{e}^{2}≐0.1031$, in line with Equation 3. The Stratonovich term $\sigma_{e}^{2}/2$ expresses the fact that for a population that sometimes grows exponentially and sometimes declines, even if its average growth rate is zero, the arithmetic mean still increases over time. Once this term is introduced, the standard Ito calculus may be applied to Equation 2.

Once the relevant parameters are calibrated, the distribution for $P(N)$ may be extracted from Equation 2, see ‘SI 2’. The resulting distribution is

$$
P(n)=Ae^{−\alpha/n}n^{−\beta},
$$

where $\alpha=2\mu/\sigma_{e}^{2}$, $\beta=1+2c/\sigma_{e}^{2}$ and $A$ is a normalization factor. Figure 1 illustrates the success of the approximation and the validity of Equation 4 in a simulation of a community of $S=200$ interacting species governed by Equation 1.

A similar result was presented a few months ago by Mallmin et al., 2024, who dealt with a system of competing species where the community dynamics is chaotic (but without external stochasticity). In such a case, one can consider, for each focal species, all other species as an effective external environment whose fluctuations generate stochasticity in the instantaneous growth rate of the focal species. A discussion of the similarities and differences between our case and the chaotic model will be presented below.

### The egalitarian transition

The most striking implication of Equation 4 is the sharp shift in the compositional properties of the community at $\beta=2$. When $\beta>2$, abundant species are relatively rare, resulting in an ‘egalitarian’ community. Conversely, when $\beta<2$, the community composition is dominated by a few exceptionally abundant species.

To quantify the egality of the community, one may use the criterion suggested by van Nes et al., 2024, which involves comparing the total number of species, $S$, to the minimal number of species required to make up half of the community, $S_{1/2}$. In a more egalitarian community, the fraction $S_{1/2}/S$ is finite, indicating that the number of dominant species is proportional to the total number of species. In contrast, in a community dominated by only a few species, the ratio $S_{1/2}/S$ approaches zero as $S$ increases, meaning the number of dominant species is sublinear in $S$.

In Appendix C, we provide the relevant mathematical analysis, demonstrating that, as $\beta$ decreases towards 2, $S_{1/2}/S$ monotonically decreases, and in the limit $\beta→2^{+}$,

$$
\frac{S_{1/2}}{S}∼e^{−(ln⁡2)/(\beta−2)}.
$$

Thus, this egality parameter vanishes in a singular manner in that limit, indicating the transition out of the egalitarian phase.

The numerical results presented in Figure 2A illustrate this phenomenon and offer several additional interesting insights. Beyond the positive indication regarding the result in the limit where $S→∞$, Figure 2A shows that the value of $\beta$ depends only weakly on $S$ so it can be considered approximately constant. Moreover, as seen in Figure 2B, for $\beta<2$ the dependence of $S_{1/2}$ on $S$ follows a power law, with an exponent approaching unity from below at the phase transition point $\beta=2$.

![Figure 2.](https://cdn.elifesciences.org/articles/103999/elife-103999-fig2-v2.jpg)

**Figure 2.:** Left panel (A): the egality parameter $S_{1/2}/S$ is plotted against $1/S$, the total number of species, for $\sigma~_{e}=0.015$ (blue) 0.02 (red) 0.04 (orange) and 0.08 (green). For all these simulations $\mu=0.6$, $\tau=8$ and $K=10^{4}$. The values of the parameter $\beta$, as extracted from the simulation, are plotted (again, vs. $1/S$) in the inset. As expected, for $\beta>2$ (blue) the egality parameter $S_{1/2}/S$ extrapolates, at $S→∞$, to a finite value, meaning that the fraction of high-abundance species is finite and the community is egalitarian. This feature is also reflected in the right panel (B), where at large $S$, $S_{1/2}∼0.04S$ for $\sigma~_{e}=0.02$ (red) and $S_{1/2}∼0.08S$ for $\sigma~_{e}=0.015$ (blue). On the other hand, when $\sigma~_{e}=0.08$ (green), the value of $\beta$ approaches 1.8 and is definitely smaller than two. In addition, the egality parameter extrapolates to zero at large $S$, meaning that the community is dominated by a small number of species. The results shown in the right panel suggest $S_{1/2}∼S^{0.3}$. The case $\sigma~_{e}=0.04$ (orange) represents a near marginal case, for which $\beta$ extrapolates to values slightly smaller than 2, and it would appear that $S_{1/2}/S$ is tending toward zero. Indeed, the right panel shows a power law with exponent smaller than unity and decreasing with increasing $\sigma~_{e}$.

Of course, there are other quantities one could employ to quantify the egality. One such possibility is the inverse participation ratio, $I$, defined as $I=[\sumi(N_{i}/K)^{2}]^{−1}$. This varies from 1 in the limit of single species dominance to $S$ for an egalitarian community. Our measurements (not shown) indicate that, similarly to $S_{1/2}$, $I$ increases with $S$, though the exponents controlling the growth are slightly lower. For example, for $\sigma~_{e}=0.08$, $I∼S^{0.26}$, as opposed to $S_{1/2}∼S^{0.29}$, and for $\sigma~_{e}=0.4$, $I∼S^{0.4}$, while $S_{1/2}∼S^{.52}$.

### Comparison with empirical results and the impact of demographic stochasticity

Let us now examine the SAD in several cases of diverse communities, assess their degree of alignment with the results presented above, and attempt to differentiate between dominance and egalitarian communities, linking the results to the fundamental characteristics of each system.

We analyze the community structure in four systems: the human gut microbiome (David et al., 2014), marine prokaryotes (Eguíluz et al., 2019), tropical trees (Cooper et al., 2024), and bird species (Callaghan et al., 2021). All of these communities are hyperdiverse, with thousands of species, making them reflective of the limit where $1/S$ is very close to zero – a limit where the distinction between egalitarian and dominance systems is clearly defined, with the relevant values of $S_{1/2}/S$ being those shown in Figure 2.

Figure 3a shows the excellent agreement between the empirical data for the gut microbiome and our model prediction (Equation 4). In the case of ocean prokaryotes, presented in panel (b), only a pure power law is observed, perhaps because the sampling strength is insufficient. Weak sampling shifts the distribution leftward, thus hiding the true characteristics of the SAD for small abundance populations (Maruvka et al., 2010). In both cases $\beta<2$, indicating that these systems are in the dominant phase, consistent with the very small values of $S_{1/2}/S$ observed in the data.

![Figure 3.](https://cdn.elifesciences.org/articles/103999/elife-103999-fig3-v2.jpg)

**Figure 3.:** The gut microbial community (OTUs of subject A from David et al., 2014) fits our formula Equation 4 quite well. Immigration is extremely weak, but the sampling power is strong enough to reveal some of the effects of the decrease in the number of species at low densities due to immigration. The corresponding distribution for the oceanic prokaryote population Eguíluz et al., 2019 is very close to a pure power law, possibly because the sampling is not deep enough (see text). In both cases, $\beta<2$, indicating that the community is dominated by only a few species. The distributions for the global bird population (Callaghan et al., 2021) and tropical trees in the Amazon Basin (Cooper et al., 2024) show a clear transition between two power-law behaviors. As explained in the text, for these macroorganisms the effect of demographic stochasticity must be taken into account. When this is done (see ‘SI D’), we obtain an excellent fit for the results using the corrected formula. Equation 6. For birds, we find $\beta≈2$, placing them on the margin between egalitarian and dominance communities. For tropical trees in the Amazon Basin, $\beta$ is definitely larger than two, indicating that the community is indeed egalitarian. Note the similarities between the values of $S_{1/2}/S$ in the empirical results and the numerical experiments in Figure 2. For more information, see ‘SI E’.

In contrast, in Figure 3c and d, for birds and Amazon basin trees, respectively, the empirical distribution does not fit Equation 4. Instead, the population size distribution shows a pronounced crossover between two descending power laws, without a maximum point at a finite abundance.

To explain this, we note that trees and birds differ from microorganisms in two important ways. First, since macroorganisms tend to have larger body sizes and longer lifespans, their metabolism buffers them against environmental fluctuations. Additionally, since populations of macroorganisms often span wide geographic ranges, most environmental variations appear uncorrelated across populations. Environmental variation that affects individuals, or small groups within the population, in an uncorrelated manner contributes to demographic stochasticity rather than to environmental stochasticity, which, by definition, affects entire populations coherently. Therefore, for macroorganisms we need to account for demographic stochasticity.

In ‘SI D’, we consider the case of a time-averaged neutral community with demographic stochasticity in addition to the previously considered immigration and environmental stochasticity. The expected distribution for species abundances now takes the form

$$
P(n)=An^{−1+2\mu/\sigma_{d}^{2}}(\frac{\sigma_{d}^{2}}{\sigma_{e}^{2}}+n)^{−2c/\sigma_{e}^{2}−2\mu/\sigma_{d}^{2}},
$$

with $\sigma_{d}$ parameterizing the strength of demographic stochasticity. Equation 6 converges to Equation 4 for values of $n$ satisfying $n≫\sigma_{d}^{2}/\sigma_{e}^{2}$ and predicts a different power-law for smaller values of $n$. With this new formula, one can now successfully fit the empirical data in Figure 3c and d. It is noteworthy that the transition point between the two power-laws happens for values of the abundance which are quite large, reinforcing our above comments about the effect of the large spatial and temporal scales of macroorganisms on reducing $\sigma_{e}$ and increasing $\sigma_{d}$.

Even with the inclusion of demographic stochasticity, the distinction between dominant and egalitarian communities depends solely on the decay of the tail and its corresponding exponent $\beta$, which, for Equation 6, remains as $\beta=−1−2c/\sigma_{e}^{2}$. Figure 3 thus illustrates the three types of behavior demonstrated in the numerical experiments shown in Figure 2: the microorganism communities are in the dominance phase, the tropical tree community is in the egalitarian phase, and the bird community appears to fall in between.

A comparison between the values of the egality parameter in Figure 2 and the values of $S_{1/2}/S$ in van Nes et al., 2024 (for the same range of species richness $S$) also shows that some communities fall within the dominance phase, while others fall within the egalitarian phase. On the other hand, the results for plankton (Ser-Giacomi et al., 2018), in which $\beta\in[1...2]$, appear to suggest that these microorganismal communities are all in the dominance phase.

### Relaxing the assumption of neutrality

So far, we have analyzed the properties of a system that is fully neutral in the deterministic limit – that is, all species have exactly the same fitness. In this section, we aim to explore, or at least provide a glimpse of, the outcomes that arise when this assumption is relaxed; in particular, we assess the robustness of our analysis in the vicinity of the neutral point.

To break perfect neutrality, we introduce heterogeneity into the interaction matrix. Specifically, we replace Equation 1 by

$$
\frac{dN_{i}}{dt}=\mu+N_{i}(1−\frac{N_{i}+\sumj\neqi(1−3ϵ+ϵ\alpha_{i,j})N_{j}}{K})+r_{i}(t)N_{i}\frac{dr_{i}}{dt}=−\frac{r_{i}}{\tau}+\thetaη_{i}(t),
$$

where $\alpha_{i,j}$ are zero-mean, unit-variance Gaussian random numbers, and $\alpha_{i,j}$ is independent of $\alpha_{j,i}$, so the interaction matrix is asymmetric. For $ϵ=0$, this reduces to our original time-averaged neutral model. The additional $−3ϵ$ term ensures that species compete most strongly against themselves, as is commonly assumed in ecological models, since the niche overlap between individuals of the same species is maximal.

The results are presented in Figure 4, which shows $S_{1/2}$ as a function of $ϵ$ for two different values of the environmental stochasticity $\sigma~_{e}$. As $ϵ→0$, the system may reside either in the egalitarian phase (if $\sigma~_{e}$ is small) or in the dominance phase under strong environmental stochasticity. In contrast, for large values of $ϵ$, $S_{1/2}$ becomes independent of $\sigma~_{e}$.

![Figure 4.](https://cdn.elifesciences.org/articles/103999/elife-103999-fig4-v2.jpg)

**Figure 4.:** $S_{1/2}$, as obtained from simulations of Equation 7, is plotted against $ϵ$, for $N=200$, $K=2⋅10^{6}$ and $\mu=0.6$. For $\sigma~_{e}=0.01$ (blue circles), the system is in the egalitarian phase and the main effect of the transition to chaos is an effective enhancement of the strength of stochasticity that makes the system less egalitarian, hence $S_{1/2}$ decreases. The inverse effect is observed for $\sigma_{e}=0.08$ (red squares). For large values of $ϵ$, the effect of $\sigma_{e}$ becomes negligible and the dependence of $S_{1/2}$ on $\sigma_{e}$ weakens significantly. The data was obtained by averaging over at least 20 different realizations of the interaction matrix $\alpha_{i,j}$.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/103999/elife-103999-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Time traces of species abundances for $ϵ=0$ (left panel, time-averaged neutral) and $ϵ=0.05$ (right panel, chaotic), with $S=200$, $K=10^{4}S$, and $\tau=8$.Since $\sigma~_{e}=0.01$, the system is in its egalitarian phase when $ϵ=0$, and the abundance variations span approximately two orders of magnitude. In the chaotic phase (right panel), these variations span the entire range between $K$ and $\mu=0.6$. Another notable feature is the emergence of cliques of high-abundance species in the chaotic phase, whereas in the stochastic phase there is a clear hierarchy of dominance. As a result, the chaotic phase exhibits a characteristic ‘shoulder’ of high-abundance species, as discussed in the main text.

To understand these results, note that in the absence of environmental stochasticity, the heterogeneous and asymmetric interactions lead to chaotic dynamics of the trajectories, as discussed in Arnoulx de Pirey and Bunin, 2024. Illustrations of fluctuation dynamics dominated by stochasticity versus those dominated by deterministic chaos are provided in ‘SI F’. Under chaotic dynamics, the system supports, at any instant of time, a clique of abundant species. This clique is stable in the sense that if all the species within it are placed together in a community, they will reach an equilibrium state in which all of them persist. However, the clique is invadable, meaning that at any given moment, there exist species outside the clique that are capable of invading and reaching high abundance (Kessler and Shnerb, 2025). Such a clique gives rise to a ‘shoulder’ at high abundance values (see Figure 5), since at any given moment there are several species with high abundance. In contrast, the hierarchical structure under pure environmental stochasticity leads to a simple power law, as seen earlier in Figure 1.

![Figure 5.](https://cdn.elifesciences.org/articles/103999/elife-103999-fig5-v2.jpg)

**Figure 5.:** $ln⁡P(n)$ vs.$ln⁡n$ for $ϵ={0 (solid blue line),0.05 (dashed red line)}$, $\sigma~_{e}=0.01$.The distribution for $ϵ=0$ is typical of the egalitarian phase with a large slope for large $n$. The distribution for $ϵ=0.05$, however, has the slower falloff characteristic of the dominance phase. In addition, there is a shoulder for very large $n$, which is due to the existence of multiple sets of several transient quasi-stable species, arising from the chaotic dynamics present in the absence of environmental stochasticity.

As $ϵ$ increases from zero to a finite value, the neutral-stochastic system discussed throughout this article transforms into a system where the dominant factor is deterministic chaos. In the chaotic phase, the dynamics still appears stochastic, but not due to fluctuations in external parameters, but rather as a result of the inherent characteristics of the deterministic dynamics.

Figure 4 demonstrates that the transition to chaos affects $S_{1/2}$ in opposite ways in the two phases. In the egalitarian phase, the main effect of chaos is to increase the effective stochasticity, leading to a decline of $S_{1/2}$. In the dominance phase, by contrast, $S_{1/2}$ increases. This is due to the ‘shoulder’ in the abundance distribution described in Figure 5, that is, because dominance in the chaotic regime is associated with a clique rather than a single species.

## Discussion

Hyperdiverse communities, like those analyzed in this article, are extremely important and frequently occur in nature. However, quantifying their specific parameters is an impossible task. Therefore, the attempt to understand the factors that dictate the community structure in these systems requires the use of models, which should preferably be as generic as possible.

Broadly speaking, there are three generic scenarios for the dynamics of multispecies systems: those involving a stable clique of resident species; those in which the composition of the group of high-abundance species changes over time due to chaotic dynamics; and those assuming neutral dynamics.

In the first case, the set of high-abundance species is determined by their relative fitness (which reflects their intrinsic growth rate and interspecific interactions), which remains fixed over time. In the second, the composition of the dominant cliques varies intermittently over time, but this turnover is governed by deterministic factors, and at any given moment, only a specific set of low-abundance species is capable of exponential growth. Moreover, the system admits a characteristic timescale, the time required for one of these rare species to invade. This timescale depends logarithmically on the migration rate $\mu$.

In the third case, discussed here, the identity of the high-abundance species at any given moment is a random outcome of environmental stochasticity. As in the chaotic case, there is no sharp separation between core species and low-abundance ones, and the fundamental timescale of the system is determined by the stickiness phenomenon described above.

As far as can be judged from the empirical SADs of Figure 2, it appears that they cannot be explained by the first scenario. Two of its main features are a gap between species with abundance of $O(K)$ and those with abundance of $O(\mu)$, and a truncated Gaussian-shaped SAD for the high-abundance species – both of which are not observed in our distributions.

The chaotic case yields SADs that more closely resemble those we have reviewed here: they exhibit no gap and display a power-law behavior. In fact, when attempting to derive an effective equation for a single species, one arrives, as noted above, at the very same equation. As is well known, it is often possible to identify multiple underlying models that give rise to the same abundance distribution. Therefore, matching the SAD is a necessary condition for considering a model a plausible candidate, but leaves open the possibility of alternative explanations.

To tell apart chaos from environmental stochasticity, it may be necessary to focus specifically on the dynamics of the most abundant species. If the noise is intrinsic, originating from chaotic fluctuations, then a species that has reached dominance is expected to exhibit fluctuation patterns that differ markedly from those observed when the same species is rare. In contrast, if the fluctuations stem from external factors such as weather or precipitation, we would expect the statistical properties of abundance fluctuations to be independent of the species’ current abundance level, as has been observed empirically (Kalyuzhny et al., 2014b).

Another test that may help distinguish between a chaotic and a stochastic system relates to the emergence of a fundamental timescale (Arnoulx de Pirey and Bunin, 2024) in chaotic dynamics – one associated with the invasion of rare species. Such a timescale does not appear in systems driven by external stochasticity. Like the previous approach, this too requires one to examine dynamic properties of the system, rather than relying solely on static features such as the abundance distribution.

Whatever the underlying mechanism, the net result, as we have demonstrated herein, is that in the limit of strong interspecies coupling, a transition occurs between an egalitarian phase and a dominance phase. When the immigration rate $\mu$ is reduced, total carrying capacity $K$ increases, or when environmental stochasticity $\sigma_{e}$ increases, the system can suddenly lose a significant amount of diversity at the transition point. The dependence on the total population size $K$ is particularly interesting and has to do with the dispute about the relationships between productivity and species richness (Waide et al., 1999; Kadmon and Benjamini, 2006).

We will now discuss some potential extensions of the model described here and explore their possible implications.

Our model assumed an uncorrelated response of species to environmental variations. This treatment can be easily extended to include correlated responses, using techniques similar to those implemented by Loreau and de Mazancourt, 2008. In general, under correlated responses, the effective number of species in the community decreases.

Another interesting point relates to the interplay between the stickiness mechanism, through which environmental stochasticity causes populations to spend long periods in a state of rarity, and mechanisms such as the storage effect or relative nonlinearity (Chesson, 1982; Chesson, 2000; Ellner et al., 2016; Letten et al., 2018) that allow rare populations to invade due to environmental stochasticity. It is likely that these mechanisms weaken as the number of species increases (for storage, this has been demonstrated in several studies; Chesson and Huntly, 1989; Pande and Shnerb, 2022), and therefore, at least in diverse communities of competing species, the dominant effect will actually be that of stickiness.

The time-averaged neutral dynamic considered here assumes that the differences in average fitness between species are negligible, at least to a first approximation. This assumption is necessary in situations where niche overlap is large; otherwise, fitness differences would cause the extinction of most species. The justification for this can come from processes leading to emergent neutrality (Holt, 2006; Vergnon et al., 2012), or from the fact that environmental stochasticity itself is also a mechanism that ‘neutralizes’ fitness differences (Pande and Shnerb, 2022). Extending our model as we have done above to include weak deviations from time-averaged neutrality, perhaps using the dynamic mean-field approximation (Roy et al., 2019) , is a critical first step, which remains to be explored in more detail.

Species coexistence has long been, and remains, a theoretical puzzle of immense importance for understanding the dynamics of biological systems, with far-reaching practical implications. The research conducted in recent years has provided powerful theoretical tools that allow us to focus the discussion and understand the generic implications of community structure and the nature of species interactions on the range of possible outcomes. We believe that the parameter range we have addressed in this article – (nearly-) neutral dynamics and significant environmental stochasticity – is relevant for a wide variety of ecological systems, and we hope that our work will serve as a foundation for further studies that explain the wide range of diversity levels (for example, between a tropical forest and a tundra, or between different types of microbiome) in relation to the phase transition described here.

## Materials and methods

### Data compilation and analysis

As explained below, the phase transition we analyze in this paper manifests itself in two characteristics: the SAD and the egality parameter $S_{1/2}/S$. Like any phase transition in complex systems, the distinction between the two phases becomes sharper as the system grows larger, so that $S$ increases. To test our predictions, we used several recent large databases on communities with thousands of species: human microbiome (David et al., 2014), marine prokaryotes (Eguíluz et al., 2019), tropical forest trees (Cooper et al., 2024), and birds (worldwide) (Callaghan et al., 2021).

### The (noise-free) neutral model

We consider a community of $S$ populations, with differential responses to environmental variations. $N_{i}$ is the abundance of the ith species, and the carrying capacity parameter is denoted by $K$. With no stochasticity and no immigration, $N_{i}$ satisfies the equation

$$
\frac{dN_{i}}{dt}=N_{i}(1−\frac{\sumj=1SN_{j}}{K}).
$$

As all species admit the same growth rate and interact in a symmetric manner, the model is neutral. In particular, any solution that satisfies $\sumj=1SN_{j}=K$ is a steady state of the system.

### The time-averaged neutral model

To allow for nontrivial dynamics, one would like to add environmental stochasticity and immigration to the process described in Equation 8. The rate of immigration is denoted by $\mu$, and the growth rate of each species fluctuates in time, undergoing an Ornstein–Uhlenbeck process with a correlation time $\tau$. The corresponding set of stochastic differential equations, as set out in Equation 1.

$$
\frac{dN_{i}}{dt}=\mu+N_{i}(1−\frac{\sumj=1SN_{j}}{K})+r_{i}(t)N_{i}\frac{dr_{i}}{dt}=−\frac{r_{i}}{\tau}+\thetaη_{i}(t),
$$

where $η_{i}(t)$ is a white-noise process of unit strength. The index i of $η_{i}$ indicates that each of the $S$ species responds to the environmental variations in an independent manner. The correlation function of $r_{i}$ is

$$
⟨r_{i}(t)r_{j}(t^{′})⟩=\delta_{i,j}\frac{\theta^{2}\tau}{2}e^{−|t−t^{′}|/\tau}.
$$

The equivalent white-noise strength of the environmental stochasticity, twice the diffusion constant of $log⁡N_{i}$, is then given by $\sigma~_{e}^{2}=\theta^{2}\tau^{2}$, the time integral of the $r_{i}$ correlation function.

### Fokker–Planck (FP) equations

The main analytical results presented in this article are based on solving FP equations. To derive these equations, we assumed a relatively short correlation time τ for the environmental stochasticity, which allows the use of a single effective equation for the process described in Equation 8. The relevant considerations are detailed in ‘SI B’.

### Demographic stochasticity

This refers to the intrinsic randomness of the birth–death process at the individual level. This stochasticity also manifests in erratic abundance variations, but the intensity of these fluctuations is weaker (compared to environmental stochasticity) when the population is large, and therefore it was not included in Equation 8 or in the analyses of van Nes et al., 2024 and Mallmin et al., 2024. However, demographic stochasticity is crucially important in small populations and in extinction processes; as we have seen, it must be considered outside the microorganism realm. To include demographic stochasticity in the treatment, one must add a term to the relevant equation that expresses noise whose amplitude scales with the square root of the population size, as opposed to environmental stochasticity, whose amplitude scales linearly with population size. The technical details can be found in ‘SI D.
