# Evolutionary dynamics of incubation periods

## Authors

- Bertrand Ottino-Loffler<sup>1</sup> ([ORCID: 0000-0001-6839-5510](https://orcid.org/0000-0001-6839-5510))
- Jacob G Scott<sup>2</sup> ([ORCID: 0000-0003-2971-7673](https://orcid.org/0000-0003-2971-7673))
- Steven H Strogatz<sup>1</sup> ([ORCID: 0000-0003-2923-3118](https://orcid.org/0000-0003-2923-3118)) †

### Affiliations

1. Center for Applied Mathematics Cornell University Ithaca United States
2. Department of Translational Hematology and Oncology Research Cleveland Clinic Cleveland United States
3. Department of Radiation Oncology Cleveland Clinic Cleveland United States

† Corresponding author

## Abstract

The incubation period for typhoid, polio, measles, leukemia and many other diseases follows a right-skewed, approximately lognormal distribution. Although this pattern was discovered more than sixty years ago, it remains an open question to explain its ubiquity. Here, we propose an explanation based on evolutionary dynamics on graphs. For simple models of a mutant or pathogen invading a network-structured population of healthy cells, we show that skewed distributions of incubation periods emerge for a wide range of assumptions about invader fitness, competition dynamics, and network structure. The skewness stems from stochastic mechanisms associated with two classic problems in probability theory: the coupon collector and the random walk. Unlike previous explanations that rely crucially on heterogeneity, our results hold even for homogeneous populations. Thus, we predict that two equally healthy individuals subjected to equal doses of equally pathogenic agents may, by chance alone, show remarkably different time courses of disease.

## Introduction

The discovery that incubation periods tend to follow right-skewed distributions originally came from epidemiological investigations of incidents in which many people were simultaneously and inadvertently exposed to a pathogen. For example, at a church dinner in Hanford, California on March 17, 1914, ninety-three individuals became infected with typhoid fever after eating contaminated spaghetti prepared by an asymptomatic carrier known to posterity as Mrs. X. Using the known time of exposure and onset of symptoms for the 93 cases, Sawyer, 1914 found that the incubation periods ranged from 3 to 29 days, with a mode of only 6 days and a distribution that was strongly skewed to the right. Similar results were later found for other infectious diseases. Surveying the literature in 1950, Sartwell noted a striking pattern: the incubation periods of diseases as diverse as streptococcal sore throat (Sartwell, 1950) (Figure 1a), measles (Stillerman and Thalhimer, 1944), polio, malaria, chicken pox, and the common cold were all, to a good approximation, lognormally distributed (Sartwell, 1950). On a time scale of years instead of days, the incubation periods for bladder cancer (Goldblatt, 1949) (Figure 1b), skin cancer, radiation-induced leukemia, and other cancers were also found to be approximately lognormally distributed (Armenian and Lilienfeld, 1974).

![Figure 1.](https://cdn.elifesciences.org/articles/30212/elife-30212-fig1-v1.jpg)

**Figure 1.:** Data redrawn from historic examples. Dashed red curves are noncentral lognormal distributions. Solid blue curves are Gumbel distributions, predicted by the theory developed here. Both sets of curves were fitted via the method of moments. (a) Data from an outbreak of food-borne streptococcal sore throat, reported in 1950 (Sartwell, 1950). Time is measured in units of days. (b) Data from a 1949 study of bladder tumors among workers following occupational exposure to a carcinogen in a dye plant (Goldblatt, 1949). Time is measured in units of years.

Two natural questions arise: Why should incubation periods be distributed at all, and why should they be distributed in the same way for different diseases? Previous explanations rest on the presumed heterogeneity of the host, the pathogen, or the dose (Sartwell, 1950; Nishiura, 2007; Horner and Samsa, 1992). To see how this works, return to the typhoid outbreak at the Hanford church dinner (Sawyer, 1914). Every person who ate that spaghetti presumably had a different level of overall health and immune function, and every plate of spaghetti was likely contaminated with a different dose and possibly even strain of typhoid.

Suppose the typhoid bacteria proliferated exponentially fast within the hosts and triggered symptoms when they reached a fixed threshold. Then, if the bacterial dose, growth rate, or triggering threshold were normally distributed across the hosts, one can show that the resulting distribution of incubation periods would have been either exactly or approximately lognormal (see Results, ‘Influence of heterogeneity’). On the other hand, there is counter-evidence that lognormal distributions can occur even if some of these sources of heterogeneity are lacking. For example, Sartwell, 1950 reanalyzed data from a study (Bodian et al., 1949) in which identical doses and strains of polio virus were injected into the brains of hundreds of rhesus monkeys. The incubation period, defined as the time from inoculation to the onset of paralysis, was still found to be approximately lognormally distributed, even though the route of infection and the viral dose and strain were held constant. Moreover, the lognormal distributions commonly observed for human diseases have a particular shape, with a dispersion factor (Sartwell, 1950) around $1.1-1.5$, which previous models cannot explain without special parameter tuning. (See Box 1 for the definition of dispersion factors.)

Here, we propose a new explanation for the skewed distribution of incubation periods. Instead of heterogeneity, it relies on the stochastic dynamics of the incubation process, as the pathogen invades, multiplies, and competes with itself and the cells of the host in a structured network topology. The theory predicts that under a broad range of circumstances, incubation periods should follow a right-skewed distribution that resembles a lognormal, but is actually a Gumbel, one of the universal extreme value distributions (Kotz and Nadarajah, 2000). Heterogeneity is not required, but it is allowed; it does not qualitatively alter our results when included.

## Results

### Mathematical Model

We model the incubation process using the formalism of evolutionary graph theory (Lieberman et al., 2005; Nowak, 2006; Ohtsuki et al., 2006; Ashcroft et al., 2015). A network of $N≫1$ nodes is used to represent an environment within a host where a pathogenic agent, such as a harmful bacterium or a cancer cell, is invading and reproducing. The network could represent several plausible biological scenarios, for example the intestinal microbiome, where harmful typhoid bacteria are competing against a benign resident population of gut flora in a mixing system (modeled as a complete graph); or it could represent mutated leukemic stem-cells vying for space against healthy hematopoietic stem cells within the well-organized three-dimensional bone marrow space (modeled as a 3D lattice); or a flat epithelial sheet with an early squamous cancer compromising and invading nearby healthy cells (modeled as a 2D lattice). For the sake of generality, we will refer to the two types of agents as healthy residents and harmful invaders.

While Sartwell’s law has been applied to many different types of diseases with diverse etiologies, the model we propose makes the most sense for asexually reproducing invaders, like cancer cells or bacteria. Viruses, on the other hand, often reproduce with a ‘one-to-many’ dynamic, which is not faithfully captured in this model. So, while the general phenomenon of network invasion seems to apply to viruses as well, the model in its present form is not well suited to describe their dynamics.

Considering asexually reproducing and competing invaders, then, we choose to model the invasion dynamics as a Moran process (Moran, 1958; Williams and Bjerknes, 1972; Lieberman et al., 2005; Nowak, 2006). Invaders are assigned a relative fitness $r$ (suggestively called the carcinogenic advantage by Williams and Bjerknes, 1972). The fitness of residents is normalized to 1. We consider two versions of the Moran process. In the Birth-death (Bd) version (Figure 2a), a random node is chosen, with probability proportional to its fitness. It gives birth to a single offspring. Then, one of its neighbors is chosen uniformly at random to die and is replaced by the offspring (Figure 2b). We also consider Death-birth (Db) updates (Figure 2c,d). In this version of the model, a node is randomly selected for death, with probability proportional to $1/r$; then a copy of a uniformly random neighbor replaces it. To test the robustness of our results, we study both versions of the Moran model on various networks: complete graphs, star graphs, Erdős-Rényi random graphs, one-, two-, and three-dimensional lattices, and small-world, scale-free, and $k$-regular networks. We also vary the invader fitness $r$ and the model criterion for the onset of symptoms. These extensions are presented in the Materials and methods, Figures 5, 6. Box 2 discusses other variants of the Moran model. Here we focus on the simplest cases to elucidate the basic mechanisms.

![Figure 2.](https://cdn.elifesciences.org/articles/30212/elife-30212-fig2-v1.jpg)

**Figure 2.:** (a) In the Birth-death (Bd) update rule, a node anywhere in the network is selected at random, with probability proportional to its fitness, and one of its neighbors is selected at random, uniformly. (b) The neighbor takes on the type of the first node. In biological terms, one can interpret this rule in two ways: either the first node transforms the second; or it gives birth to an identical offspring that replaces the second. (c) In the Death-birth (Db) update rule, a node is selected at random to die, with probability inversely proportional to its fitness, and one of its neighbors is selected at random, uniformly, to give birth to one offspring. (d) The first node is replaced by the offspring of the second.

Our simulations start with a single invader placed at a random node in a network of otherwise healthy residents. The update rule is applied at discrete time steps. In the long run, either the invaders replace all the residents, or vice versa. If symptoms are triggered when the entire network has been taken over by invaders, then the incubation period is the number of time steps between the introduction of the invader and its fixation. On the other hand, if the invaders die out and the healthy cells take over, then the process is stopped and no observable symptoms manifest. Later, in the paper, we consider a generalization from complete to partial takeovers, but for now the incubation period will refer to a complete takeover.

Our notion of time in this model is linked directly to the biology of invasion of a reproducing asexual pathogen that divides and replaces other cells sequentially. Instead of considering divisions as a rate, and therefore linking the dynamics to real time, we consider time steps to be individual division events. This is more akin to the standard methods of modeling chemical interactions, as in the Gillespie algorithm (Gillespie, 1977). This focus on the biology of the individual pathogen (or cancer cell) also provides a simple explanation for how diseases with very different natural histories can have the same analytic distribution of incubation time. As each different disease would have a different characteristic mean doubling time, while the shape of the distributions might be the same, the physical time taken would scale with the characteristic proliferation time. Future iterations of this model could consider deriving an exact scaling between physical time and this biological event-based updating of time.

### Infinitely fit invaders

First, consider what happens if the invaders have infinite fitness ($r→∞$) in the Birth-death model. While an exaggeration, this case is instructive and is a reasonable approximation for aggressive cancers and infections. In this limit, the dynamics simplify enormously: only the invaders reproduce. But because they give birth and replace their neighbors blindly, they waste time whenever they compete between themselves and one invader replaces another. These random self-replacements slow down the incubation process, and make it highly variable. In fact, the level of in-fighting is what determines the incubation period in this case. Beyond fitness, the topology of the network matters too. For low-dimensional networks, exemplified by a two-dimensional lattice (Figure 3a , red circles), the growth rate of the invader population remains roughly constant as takeover occurs. This leads to a normal distribution of incubation periods (Figure 3a, red circles; and see Methods and Materials, ‘Birth-death, other solvable networks’). However, on very high-dimensional networks like the complete graph (Figure 3a, blue circles), the distribution becomes right skewed. Intuitively, this happens because every invader now has a chance of replacing any healthy node or any other invader. It is as if at every time step a candidate node for replacement gets blindly drawn from a bag, relabeled as an invader, and returned to the bag. At the start of the incubation process, almost every draw adds another invader to the population and the infection progresses rapidly. But near the end, it will take many, many draws to blindly fish out the last remaining healthy node, as needed to terminate the incubation period. This slowing-down phenomenon near the end should feel familiar to anyone who has tried to complete a collection of baseball cards, stamps, or coupons, since they are all manifestations of the coupon collector's problem, a well-studied concept in probability theory (Pósfai, 2010; Feller, 1968; Erdős and Rényi, 1961). Because of those frustratingly long waits to collect the final healthy node, the incubation period distribution gets skewed to the right. In the infinite-$N$ limit (see Methods and Materials, ‘Birth-death, complete graph’), the coupon collector’s process returns a Gumbel distribution, which resembles a lognormal and can be mistaken for it (Read, 1998). Indeed, when a Gumbel and a lognormal are fit to the same real data, as in Figure 1, it is hard to tell them apart. All this analysis can easily be repeated for the Death-birth model with minimal changes.

![Figure 3.](https://cdn.elifesciences.org/articles/30212/elife-30212-fig3-v1.jpg)

**Figure 3.:** Plots show simulated distributions of incubation periods, defined here as invader fixation times. Starting from a single invader at a random node, the state of the network was updated by Birth-death dynamics on both a complete graph and a two-dimensional (2D) lattice. Results for the Death-birth update rule (not shown) are identical. All distributions are normalized to have zero mean and unit variance. (a) Infinitely fit invader. For invader fitness $r→∞$, the distribution is right-skewed for a complete graph (blue symbols). It approaches a Gumbel distribution as $N→∞$, where $N$ is the number of nodes in the network. In contrast, for a 2D lattice (red symbols) the incubation periods are normally distributed. The difference is that a coupon collection mechanism operates in the complete graph and in lattices of sufficiently high dimension $d\geq3$; this mechanism causes the right skew. Simulations used $10^{6}$ repetitions on a complete graph of $N=150$ nodes, and $10^{5}$ repetitions for a 2D lattice of $N=30^{2}$ nodes. (b) Neutrally fit invader. Distributions of incubation periods are shown for invader fitness $r=1$, using $10^{6}$ repetitions on a complete graph of $N=50$ nodes (blue symbols), and $10^{5}$ repetitions for a 2D lattice of $N=7^{2}$ nodes (red symbols). Similar right-skewed distributions occur for both networks, caused by a conditioned random walk mechanism.

### Neutrally fit invaders

At the other extreme, suppose the invaders have no selective advantage ($r=1$). Then a different stochastic mechanism skews the distribution of incubation periods to the right (Figure 3b and Methods and Materials, ‘Random Walk Skewness’). For many networks, the dynamics reduce to an unbiased random walk on the number of invaders, with waiting times at each population level. There are two absorbing states, corresponding to both $0$0 and $N$ invaders for the two kinds of fixation. However, we only care about random walks that successfully hit $N$, as these represent disease processes that manifest symptoms, so we must always condition on its success. This demands that the invader experience early success and growth, pushing it away from probable extinction. This conditioning introduces a bias that makes short incubation times probable, but long walks may still occasionally occur, driving the mean time above the median. In short, a conditioned random walk will introduce a right skew in the distribution of incubation periods. This effect holds for both high- and low-dimensional networks (Figure 3b), and for Birth-death and Death-birth dynamics.

### Testing robustness to update rule and truncation

Right-skewed distributions typically persist in the face of various perturbations to the model, but some perturbations can turn them into normal distributions. For example, suppose we allow symptoms to occur when invaders take over only a fraction $f$ of the whole network. This is a reasonable consideration as leukemic cells need not take over all the bone marrow before leukemia becomes evident, nor does typhoid need to overwhelm all the cells in the microbiome before causing fever; indeed it is likely far fewer in both cases. Figure 4 contrasts what happens for Birth-death and Death-birth dynamics under these assumptions. When $r=∞$, the Gumbel distribution of Figure 3a persists for $f=1$ (Figure 4a), but turns into a normal distribution (Baum and Billingsley, 1965) when $f=0.9$ (Figure 4b) or $f=0.1$ (Figure 4c). Yet under Death-birth dynamics, the distribution stays Gumbel for all nonzero values of $f$ (Figure 4d,e,f). The fact that birth-death dynamics returns a normal for $0<f<1$ whereas Death-birth still returns a Gumbel can be rationalized via various convergence theorems (Baum and Billingsley, 1965; Ottino-Löffler et al., 2017; Pósfai, 2010). However, the fact that similar update rules behave so differently under a reasonable perturbation should caution us to be mindful of our choice of models.

![Figure 4.](https://cdn.elifesciences.org/articles/30212/elife-30212-fig4-v1.jpg)

**Figure 4.:** The plots show how the distribution of incubation periods does or does not change when we modify the assumed update rules and criterion for the onset of symptoms. Both Birth-death (Bd) and Death-birth (Db) dynamics were simulated on a complete graph of $N=5000$ nodes, using a infinite invader fitness. Incubation periods are now defined as times needed for invaders to take over a fraction $f$ of the whole network. All distributions are normalized to have zero mean and unit variance. Data points are color-coded according to the nature of the distribution: blue indicates a Gumbel distribution, and red indicates a normal distribution. (a) The distribution of times till invader fixation ($f=1$) under Birth-death dynamics. The Gumbel distribution of Figure 3a persists. (b) When $f$ is reduced to 0.9, the incubation periods under Birth-death dynamics become normally distributed instead of skewed. (c) When $f$ is reduced to 0.1, the incubation period distribution remains normally distributed. By contrast, Death-birth dynamics are insensitive to this modification: the Gumbel distribution persists not only for (d) $f=1$ but even for (e) $f=0.9$ and (f) $f=0.1$. The difference in sensitivity between the two types of dynamics can be explained intuitively by when the slowest part of the coupon collection process occurs. For Death-birth dynamics, it occurs near the beginning of the invasion, when it takes a long time to randomly select one of the few available invaders to give birth. Since the slow part of coupon collection occurs near the beginning, it is insensitive to the end-condition $f<1$. In contrast, the slow part occurs near the end of the invasion for Birth-death dynamics (when residents are scarce), and hence gets truncated when $f<1$, giving rise to a normal instead of a right-skewed distribution.

### Influence of heterogeneity

Historically, the distribution of incubation periods has been ascribed to heterogeneity (Sartwell, 1950; Nishiura, 2007; Horner and Samsa, 1992) in the fitness (growth rate, say) or dose of the pathogen, or in host factors like immune response. To see how these potential sources of heterogeneity could account for the skewed and approximately lognormal distribution of incubation periods, consider a pathogen growing exponentially with rate $r$ from an initial population $N_{0}$, so that its population at time $t$ is given by $N⁢(t)=N_{0}⁢e^{r⁢t}$. If an immune response or other detectable symptoms are triggered when $N$ reaches a threshold population $\theta$, then the incubation time $T$ satisfies $N⁢(T)=N_{0}⁢e^{r⁢T}=\theta$. Solving for $T$ yields

$$
T=\frac{1}{r}⁢(log⁡\theta-log⁡N_{0}).
$$

So if either the threshold $\theta$ or the inoculum $N_{0}$ are normally distributed across the host population, the incubation period $T$ will be lognormally distributed. Likewise, but in a more qualitative sense, a normal distribution of pathogen growth rates $r$ will also produce a skewed distribution that resembles a lognormal (Nishiura, 2007). However, if there is no randomness in any of those sources, this model predicts a single deterministic value of $T$ for the incubation period.

In contrast, the stochastic model proposed here does not need these sources of heterogeneity to produce right-skewed distributions. But if they happen to be present, as they likely are for many real diseases, our model can accommodate them. Indeed, when any of the three sources of heterogeneity are included in our model, they only serve to make the predicted distributions even more right-skewed, as we now show.

First, to emulate the heterogeneity of the strength of the pathogen, we assume heterogeneity in the parameter $r$ (which, in our model, governs the fitness of the invading cells relative to those of the host). In particular we randomly draw a different $r>0$ in each simulation, to simulate different hosts being infected with different pathogenic strains. The resulting distribution of invader fixation times depends on the distribution of the $r$’s, but our investigations demonstrate they consistently produce right-skewed distributions (Figure 5a).

![Figure 5.](https://cdn.elifesciences.org/articles/30212/elife-30212-fig5-v1.jpg)

**Figure 5.:** Simulated, fitted, and normalized distributions of incubation periods for birth-death dynamics on a complete graph of $N=500$ nodes. Unless stated otherwise, each simulation used an invader fitness of $r=10$, measured times till complete takeover ($f=1$), and started from an initial dose of 1 invader. Runs where the dosage was not smaller than the truncation point were rejected. The blue curves indicate noncentral lognormals fitted via the method of moments. (a) Heterogeneous fitness of invader. Every run used a different $r$ selected from a Gamma distribution with a shape parameter of 10. (b) Heterogeneity of host response. Instead of waiting until all $N$ residents had been replaced by invaders, every run used a different truncation point uniformly selected from ${2,3,…⁢N}$. (c) Heterogeneity of dosage. Every run had a different starting population drawn from a Poisson of mean 10 and a shift of 1. (d) Heterogeneity of invader fitness, host response, and dosage. Every run used an $r$ drawn from Gamma(10), a truncation point $f$ drawn from Uniform(0,1), and a dosage drawn from Poisson(10)+1.

Second, to emulate the heterogeneity of host factors like immune response, we allow variability in the parameter $f$, which quantifies the fraction of the network that needs to be invaded before symptoms appear. Let $T_{f}$ denote the time it takes for $N⋅f$ of the original resident nodes to be replaced by invaders. If we draw $f$ randomly from some distribution, then essentially each host has a different threshold at which symptoms appear. In contrast to Figure 4b, where we saw that repeated simulations for a host population with a single, fixed, deterministic $f$ can cause skewed distributions to turn into normal distributions, that is no longer the case when heterogeneity is included, as Figure 5b indicates. In fact, the heterogeneity actually causes even more right-skew than before.

Third, emulating variable doses is also straightforward. Instead of always starting with a single invader cell, we choose the initial number of invaders according to some distribution. Again, this modification does not remove the right-skewed behavior established in the Moran model (Figure 5c).

Finally, we can apply all these sources of heterogeneity at once, and remain with a right-skewed distribution (Figure 5d). In summary, although our main results were obtained by analyzing stochastic models of homogeneous host and pathogen populations, allowing for heterogeneity makes the predicted right-skewed distributions more, not less, prominent.

## Discussion

The evolutionary dynamical model presented here is intended to mimic the within-host development of certain cancers and bacterial infections. It is not well suited to the dynamics of viruses. Thus, explaining why Sartwell's law also holds for so many viral diseases remains an open question.

Our model suggests two basic mechanisms underlie the observed right-skewed, approximately lognormal distributions of incubation periods. When the fitness of the pathogen is high, the skew comes from coupon collection; when the pathogen fitness is neutral or low, the skew comes from conditioned random walks; and at intermediate fitnesses, a combination of the two creates skew. Neither of these effects demand any heterogeneity from the invader or the host. However, the model can accommodate such heterogeneity, either by having the invader fitness $r$ be randomly drawn, or by having symptoms occur when a random fraction $f$ of the host network has been invaded. Our simulations show that both sources of heterogeneity only exaggerate the level of right-skewness we would have seen without them (See Results,‘Influence of heterogeneity’, Figure 5).

Beyond accounting qualitatively for the distributions of incubation periods, our model accounts for a quantitative feature that has never been explained before. As shown in Methods and Materials, Table 1, the distributions generated by highly fit pathogens and mutants are predicted to have dispersion factors (also known as geometric standard deviations; see Box 1) of about $1.1-1.4$, close to the actual values of $1.1-1.5$ observed for various infectious diseases (Sartwell, 1950;Sartwell, 1966;Nishiura, 2007). Moreover, the model also helps to explain why so few infectious diseases yield dispersion factors greater than 1.5. Such high dispersion factors arise only for $r≈1$, corresponding to pathogens or mutants that are only slightly more fit than the resident populations against which they are competing.

**Table 1.**
 Model dispersion factors.Dispersion factors (geometric standard deviations, see Box 1) for the simulated distributions of incubation periods shown in Figures 6,7,8 , for different networks and invader fitness levels $r$. Errors represent 95% confidence intervals. Due to finite size effects, the dispersion factors exceed 1 for 1D and 2D lattices with $r=∞$ (they should approach one as $N→∞$). Dispersion factors for the $r=1$ case are larger than for the $r=∞$ case, but are more uniform for different network topologies.


<table>
  <thead>
    <tr>
      <th>Network</th>
      <th>r=∞</th>
      <th>r=1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.2386±0.0004</td>
      <td>1.6629±0.0012</td>
      <td>Complete</td>
    </tr>
    <tr>
      <td>1.3463±0.0006</td>
      <td>1.6875±0.0012</td>
      <td>Star</td>
    </tr>
    <tr>
      <td>1.1418±0.0002</td>
      <td>1.7907±0.0014</td>
      <td>1D Lattice</td>
    </tr>
    <tr>
      <td>1.0731±0.0003</td>
      <td>1.6799±0.0012</td>
      <td>2D Lattice</td>
    </tr>
    <tr>
      <td>1.1289±0.0006</td>
      <td>1.6659±0.0012</td>
      <td>3D Lattice</td>
    </tr>
    <tr>
      <td>1.2586±0.0004</td>
      <td>1.6900±0.0012</td>
      <td>Erdős-Rényi</td>
    </tr>
    <tr>
      <td>1.2604±0.0004</td>
      <td>1.7693±0.0014</td>
      <td>Small-World</td>
    </tr>
    <tr>
      <td>1.2125±0.0003</td>
      <td>1.7229±0.0013</td>
      <td>k-Regular</td>
    </tr>
    <tr>
      <td>1.4189±0.0007</td>
      <td>1.7399±0.0013</td>
      <td>Scale-Free</td>
    </tr>
  </tbody>
</table>

On the other hand, it is tempting to speculate that this regime of nearly neutral fitness may be more relevant to cancer development. While it is likely that tumor cells late in the disease process have much higher fitness than healthy cells secondary to continued selection (Scott and Marusyk, 2017), there is ample evidence that most cancers have long latency periods, for example in genetic data from pancreatic cancers (Yachida et al., 2010). One could speculate that during this early period, which accounts for the majority of the cancer’s time in the patient, the fitness is nearly neutral. For the cancer data reviewed by (Armenian and Lilienfeld, 1974), the observed distributions typically had dispersion factors around $1.4-1.9$. In our model, these high dispersion factors tend to arise when the invader is only slightly more fit than residents. This is also consistent with the suggestion of (Williams and Bjerknes, 1972); the shape of tumors in the model most closely resembled that of real tumors when the fitness of the invaders was only slightly above neutral.

In 1546, Fracastorii, 1930 described the incubation of rabies after a bite from an rabid dog as ‘stealthy, slow, and gradual.’ Today, nearly five centuries later, the dynamics of incubation processes remain stealthy and slow to yield their secrets. We have tried to shed light on their patterns of variability with the help of a new conceptual tool, evolutionary graph theory. This approach provides a possible solution to the longstanding question of why so many disparate diseases show such similarly-shaped distributions of incubation periods. What remains is to quantify the dynamics of incubation processes experimentally with high-resolution measurements in time and space.

Aside from their possible application to incubation processes, our results also shed light on a broader theoretical question in evolutionary dynamics: when a mutant invades a structured population of residents, how does the distribution of mutant fixation times depend on the network structure of the population? Early work in evolutionary graph theory (Lieberman et al., 2005; Nowak, 2006; Ohtsuki et al., 2006) concentrated on the network’s impact on the probability of mutant fixation and the mean time to fixation. More recent studies have gone beyond the mean time to consider the full distribution of fixation times (Ashcroft et al., 2015), as we have also done here. We hope that our exact results for disparate topologies and dynamics will stimulate further investigations of these important questions in evolutionary biology.

## Materials and methods

Here we describe the model and our analytical and numerical results in further detail. We also test the robustness of our claims with respect to relaxation of the various assumptions in the model. See the Appendix for complete proofs of analytical results.

### Birth-death, complete graph

The population of cells is represented by a network of $N$ nodes. Edges between nodes indicate which cells can potentially interact with each other. There are two types of cells: harmful invaders with fitness $r$, and healthy residents with fitness 1. All simulations are initialized with a single invader placed at a random node.

The Moran Birth-death (Bd) update rule has two steps. First, a node is randomly selected out of the total population, with probability proportional to its fitness. Second, a neighbor of the first node is chosen, uniformly at random, and takes on the type of the first node.

In a complete graph, all nodes are adjacent. Therefore, the probability of adding a new invader, given there are currently $m$ invaders, is

$$
p_{m}:=P⁢(Choose an invader)⋅P⁢(Neighbor is resident)=\frac{m⁢r}{m⁢r+(N-m)}⋅\frac{N-m}{N-1}.
$$

In the limit of infinite fitness, $(r→∞)$, the first term approaches one and we get

$$
p_{m}:=\frac{N-m}{N-1},
$$

and the probability of the invader population ever decreasing is 0. So the time $T$ to invader fixation is sum of all the transition times $m→m+1$ for $m=1,2,…,N-1$. These transition times can be calculated as follows. For the population to take $t$ steps to go from $m$ to $m+1$ invaders, nothing must have happened for $t-1$ steps before advancing on the $t$’th step. The probability of this happening is exactly

$$
p_{m}⁢(1-p_{m})^{t-1}.
$$

In other words, the time to add a new invader is exactly a geometric random variable. Therefore, the total fixation time is just

$$
T=\summ=1N-1Geo⁢(p_{m})=\sumk=1N-1Geo⁢(\frac{k}{N-1}).
$$

This random variable $T$ describes a process identical to that of the coupon collector’s problem (Pósfai, 2010; Feller, 1968). In both, we have a collection of $N-1$ nodes, and draw a random one with replacement at each time step. If we pick a healthy node, we relabel it and toss it back, and repeat until there are no healthy nodes left. By adapting classic results (Erdős and Rényi, 1961; Baum and Billingsley, 1965), we show in the Appendix that it is straightforward to find the asymptotic distribution of $T$ as $N$ gets large. To normalize this distribution, note that its mean is $\mu=\sum_{m}p_{m}^{-1}≈N⁢log⁡(N)+N⁢\gamma$. Then we find

$$
\frac{T-\mu}{N}→𝑑Gumbel⁢(-\gamma,1).
$$

Here $\gamma≈0.5772$ is the Euler-Mascheroni constant, $→𝑑$ denotes convergence in distribution, and a Gumbel($\alpha,\beta$) random variable has a density given by

$$
h⁢(x)=\beta^{-1}⁢e^{-(x-\alpha)/\beta}⁢exp⁡(-e^{-(x-\alpha)/\beta}).
$$

This prediction for the normalized distribution of the incubation period $T$ agrees with simulations on large networks (Figure 6a).

![Figure 6.](https://cdn.elifesciences.org/articles/30212/elife-30212-fig6-v1.jpg)

**Figure 6.:** Distributions of invader fixation times, normalized to have zero mean and unit variance, are shown for infinite-$r$ Birth-death dynamics on various networks. Open circles show simulation results. Curves show analytical predictions: blue curves are Gumbels, red are normals, and pink is an intermediate distribution. Insets show schematics of networks. (a) The distribution of fixation times for a complete graph on $N=150$ nodes, for $10^{6}$ runs. Distribution normalized according to analytically calculated mean and standard deviation. Curve shows a Gumbel distribution. (b) The Gumbel distribution of fixation times for a star graph with $N=75$ spokes, for $10^{6}$ runs. Distribution normalized according to analytically calculated mean and standard deviation. (c) Normal distribution of fixation times for a 1D ring on $N=75$ nodes, for $10^{6}$ runs. Distribution normalized according to analytically calculated mean and standard deviation. (d) Normal distribution of fixation times for a 2D lattice of $N=60\times60$ nodes, for $10^{5}$ runs. Distribution normalized according to empirically calculated mean and standard deviation. (e) The distribution of fixation times for a 3D lattice of $N=11^{3}$ nodes, for $10^{5}$ runs. Distribution normalized according to empirically calculated mean and standard deviation. The predicted distribution is the result of an approximating sum of exponential random variables under $10^{6}$ repetitions. (f) The distribution of fixation times for an Erdős-Rényi random graph on $N=115$ nodes with an edge probability of $ρ=0.5$. Distribution normalized according to empirically calculated mean and standard deviation.

A Gumbel distribution of incubation periods has previously been obtained for a variant of this model. Instead of working with the large-$N$ limit of a complete graph, it assumed a continuous-time birth-death model of an invading microbial population whose dynamics were governed by differential equations (Williams, 1965).

### Birth-death, other solvable networks

The analysis of the finite-$N$ complete graph sets up an important framework that can be applied to more complicated networks. For example, in the Appendix we prove that the distribution of fixation times $T$ for a star network also converges to a Gumbel for $N≫1$, specifically:

$$
\frac{T-N^{2}⁢log⁡(N)-(\gamma-1)⁢N^{2}}{N^{2}}→𝑑Gumbel⁢(-\gamma,1).
$$

This prediction matches simulations (Figure 6b).

The same framework also applies to a one-dimensional (1D) ring lattice, but instead of using the coupon-collector framework, we need to cite the Lindeberg-Feller central limit theorem (Durrett, 1991). As shown in the Appendix, this gives us

$$
\frac{T-(N^{2}-N)/2}{(2⁢N^{3}-3⁢N^{2}+N)/6}→𝑑Normal⁢(0,1).
$$

This prediction agrees with simulations (Figure 6c).

For a two-dimensional square lattice, it is more difficult to produce analytical results that are both rigorous and exact. But by making an approximation based on the geometry of the lattice, and using the fact that the population growth rate is proportional to its surface area (see the Appendix, ”Normally distributed fixation times for 2D lattice’), we can make a non-rigorous analytical guess about the distribution of the fixation times $T$. Via these arguments, and given $\mu=E⁢[T]$ and $\sigma^{2}=Var⁢(T)$, we predict

$$
\frac{T-\mu}{\sigma}→𝑑Normal⁢(0,1).
$$

Despite the approximation, this prediction works well (Figure 6d).

By similar arguments, we predict that lattices of dimension $d\geq3$ have right-skewed asymptotic distributions of fixation times. Specifically, given $η:=1-1/d$, we predict

$$
Skew⁢(T):=\frac{E⁢[(T-\mu)^{3}]}{\sigma^{3}}=\frac{2⁢ζ⁢(3⁢η)}{ζ⁢(2⁢η)^{3/2}},
$$

where $ζ$ is the Riemann zeta function. The methods used to derive that can also be used to create approximate finite-size distributions for the lattices (Figure 6e).

In particular, we predict positive skew for all $d\geq3$ and for the skew to increase monotonically with dimension (see the Appendix). Meanwhile, both 1D and 2D lattices have normal asymptotic distributions, and therefore no skew. This establishes $d=2$ as a critical dimension in these dynamics, transitioning from zero skew to positive skew.

Incidentally, these arguments also suggest that appropriate infinite-dimensional networks will asymptotically have a Gumbel distribution. This is numerically true for the Erdős-Rényi random graph (Figure 6f).

For more complex networks, such as the Watts-Strogatz small-world network, the $k$-regular random graph, and the Barabasi-Albert scale-free network, we currently lack theory to predict the asymptotic distributions analytically. However, numerical simulations produce simulations that are all well-approximated by a noncentral lognormal, obeying Sartwell’s law (Sartwell, 1950) (Figure 7a,c,e).

![Figure 7.](https://cdn.elifesciences.org/articles/30212/elife-30212-fig7-v1.jpg)

**Figure 7.:** Simulated and fitted distributions of invader fixation times for Birth-death dynamics on small-world, scale-free, and $k$-regular networks. All distributions were normalized to have mean zero and unit variance. The curves indicate non-central lognormals fitted to the first three moments of the data. All distributions are the result of $10^{6}$ simulations. The figures in the top row ((a), (b), (c)) used invader fitness $r=∞$, whereas the figures in the bottom row ((d), (e), (f)) used neutral fitness $r=1$. (a) Newman-Watts-Strogatz small-world ring network with shortcut probability of $ρ=0.25$ on $N=75$. (b) Random 3-regular graph on $N=100$ nodes. (c) Barabasi-Albert scale-free network with a minimum degree of 3 and $N=100$ nodes. (d) Newman-Watts-Strogatz small-world ring network with shortcut probability of $ρ=0.25$ on $N=25$ nodes. (e) Random 3-regular graph on $N=22$ nodes. (f) Barabasi-Albert scale-free network with a minimum degree of 3 and $N=22$ nodes.

Table 1 shows that geometric standard deviations of the incubation period distributions for all of these networks fall around $1.1-1.4$, in agreement with the dispersion factors of $1.1-1.5$ observed for many infectious diseases (Sartwell, 1950; Horner and Samsa, 1992).

### Random walk skewness

So far we have focused on infinitely fit invaders ($r→∞$). Now we consider the opposite extreme, where invaders have nearly neutral fitness ($r≈1$) relative to the residents. We will show that right-skewed distributions of incubation periods occur in this limit as well, but for a completely different reason than coupon collection.

The analysis is again simplest for the complete graph, so we return to that case. As before, the probability of an invader replacing a resident in the next time step is

$$
p_{m}^{+}:=\frac{m⁢r}{m⁢r+(N-m)}⋅\frac{N-m}{N-1}.
$$

Similarly, the probability of an invader being replaced by a resident in the next time step is

$$
p_{m}^{-}:=\frac{N-m}{m⁢r+(N-m)}⋅\frac{m}{N-1}.
$$

So the probability of the next replacement adding a new invader is

$$
q:=\frac{p_{m}^{+}}{p_{m}^{+}+p_{m}^{-}}=\frac{r}{r+1}.
$$

This defines a random walk with drift $q$ on the invader population.

Only a special subset of these walks are relevant to the computation of the incubation period distribution. For the incubation period to be well-defined, the invader population must not go extinct. Therefore, we need to condition on the fact that the invader population $m$ hits $N$ before it ever hits 0. For the limiting case $r=1$, corresponding to a perfectly neutral invader, we can show with martingale methods that the resulting distribution of incubation periods will be strongly skewed to the right as $N$ gets large (see the Appendix). This is to be expected: there are only a few ways to walk from one to $N$ quickly, while there are many ways to have a long, meandering excursion before finally getting there.

The variance from this conditioned random walk process tends to drown out the effects of network topology. The distribution of incubation periods ends up looking similar for diverse networks (Figure 8), including complex networks (Figure 7b,d,f). So even though no coupon collection happens at low finesses $r≈1$, the effect of the conditioned random walk is more than enough to generate right-skewed distributions of incubation periods. In fact, this conditioned random walk mechanism at low $r$ produces an even higher dispersion factor ($≈1.7$) than coupon collection does at high $r$ (see Table 1).

![Figure 8.](https://cdn.elifesciences.org/articles/30212/elife-30212-fig8-v1.jpg)

**Figure 8.:** Neutrally fit invader $(r=1)$.Simulated and fitted distributions of invader fixation times are shown for Birth-death dynamics on various networks. All distributions were normalized to have mean zero and unit variance. The curves indicate noncentral lognormals fitted via the method of moments. (a) Complete graph on $N=50$ nodes, for $10^{6}$ runs. (b) Star graph with $N=25$ spokes, for $10^{6}$ runs. (c) One-dimensional ring on $N=50$ nodes, for $10^{6}$ runs. (d) Two-dimensional lattice on $N=7\times7$ nodes, for $10^{6}$ runs. (e) Three-dimensional lattice on $N=4^{3}$ nodes for $10^{6}$ runs. (f) Erdős-Rényi random graph on $N=25$ nodes with an edge probability of $ρ=0.5$.

### Influence of non-static population

In many diseases, it is unlikely that the total network size would remain constant in time. For example, targeted radiation and chemotherapy leads to a loss of mass in both the tumor and the substrate tissue. Depending on the specific physical case, the population levels of invaders and residents can have many nontrivial time dependencies. As a first-order examination of the effects of time-varying populations, three simple cases were considered on the complete graph for the intermediate fitness of $r=10$. As a baseline, the distribution for a constant population was measured in Figure 9a.

![Figure 9.](https://cdn.elifesciences.org/articles/30212/elife-30212-fig9-v1.jpg)

**Figure 9.:** Simulated, fitted, and normalized distributions of incubation periods for Birth-death dynamics on a complete graph that initially has $N=500$ nodes. Invader fitness is set at $r=10$. The blue curves indicate noncentral lognormals fitted via the method of moments. (a) Constant total population. (b) Growing population. At every time step, there is a constant 1/$N$chance that a new resident node will appear. The new node is adjacent to all preexisting nodes. (c) Shrinking population. At every time step, there is a constant 1/$N$chance that a random resident node will be removed. (d) Randomly varying population. At every time step, a resident node is either added or removed from the population, both events occurring with probability 1/2.

We considered a case when the resident population was growing. At every time step, a new resident node was added with probability $1/N$, which was chosen so that takeover would happen in finite time. Even still, the majority of the run will be spent when the resident population is small, with takeovers and new additions occurring at a roughly even pace. This led to an accentuated level of right skew in Figure 9b.

We then considered a case where the resident population was constantly shrinking. Again, the probability of change was $1/N$ every time step, but this time it decreased the resident population by 1. While there is still a visible right skew in Figure 9c, it was somewhat lessened due to the global shrinkage speeding up the coupon collecting process.

Finally, we considered a randomly varying resident population. Here, the resident population increases or decreases by one every time step, each with probability 1/2. This random-walking population level also leads to an extreme level of skew in Figure 9d.
