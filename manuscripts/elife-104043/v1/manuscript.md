# Toward stable replication of genomic information in pools of RNA molecules

## Authors

- Ludwig Burger<sup>1</sup> ([ORCID: 0009-0000-0699-6302](https://orcid.org/0009-0000-0699-6302))
- Ulrich Gerland<sup>1</sup> ([ORCID: 0000-0002-0859-6422](https://orcid.org/0000-0002-0859-6422)) †

### Affiliations

1. Physics of Complex Biosystems, Department of Bioscience, School of Natural Sciences, Technical University of Munich Garching Germany ([ROR:02kkvpp62](https://ror.org/02kkvpp62))

† Corresponding author

## Abstract

The transition from prebiotic chemistry to living systems requires the emergence of a scheme for enzyme-free genetic replication. Here, we analyze a recently proposed prebiotic replication scenario, the so-called Virtual Circular Genome (VCG) [Zhou et al., RNA 27, 1-11 (2021)]: Replication takes place in a pool of oligomers, where each oligomer contains a subsequence of a circular genome, such that the oligomers encode the full genome collectively. While the sequence of the circular genome may be reconstructed based on long oligomers, monomers and short oligomers merely act as replication feedstock. We observe a competition between the predominantly error-free ligation of a feedstock molecule to a long oligomer and the predominantly erroneous ligation of two long oligomers. Increasing the length of long oligomers and reducing their concentration decreases the fraction of erroneous ligations, enabling high-fidelity replication in the VCG. Alternatively, the formation of erroneous products can be suppressed if each ligation involves at least one monomer, while ligations between two long oligomers are effectively prevented. This kinetic discrimination (favoring monomer incorporation over oligomer–oligomer ligation) may be an intrinsic property of the activation chemistry, or can be externally imposed by selectively activating only monomers in the pool. Surprisingly, under these conditions, shorter oligomers are extended by monomers more quickly than long oligomers, a phenomenon that has already been observed experimentally [Ding et al., JACS 145, 7504-7515 (2023)]. Our work provides a theoretical explanation for this behavior and predicts its dependence on system parameters such as the concentration of long oligomers. Taken together, the VCG constitutes a promising scenario of prebiotic information replication: It could mitigate challenges in non-enzymatic copying via template-directed polymerization, such as short lengths of copied products and high error rates.

## Introduction

In order to delineate possible pathways toward the emergence of life, it is necessary to understand how a chemical reaction network capable of storing and replicating genetic information might arise from prebiotic chemistry. RNA is commonly assumed to play a central role on this path, as it can store information in its sequence and catalyze its own replication (Higgs and Lehman, 2015; Joyce, 1989; Robertson and Joyce, 2012). While ribozymes capable of replicating strands of their own length have been demonstrated in the laboratory (Attwater et al., 2013), it remains elusive how enzyme-free self-replication might have worked before the emergence of such complex ribozymes.

One possible mechanism is template-directed primer extension (Ding et al., 2022; Kervio et al., 2016; Leveau et al., 2022; Walton and Szostak, 2016; Welsch et al., 2023). In this process, a primer hybridizes to a template and is extended by short oligonucleotides, thereby forming a (complementary) copy of the template strand. Considerable progress has been made in optimizing template-directed primer extension, but challenges remain: (i) The produced copies are likely to be incomplete. So far, at most 12 nt have been successfully added to an existing primer (Leveau et al., 2022). Moreover, as the pool of primer strands needs to emerge via random polymerization, the primer is likely to hybridize to the template at various positions, and not only to its 3′-end, leaving part of the 3′-end of the template uncopied (Szostak, 2011). (ii) Errors in enzyme-free copying are frequent due to the limited thermodynamic discrimination between correct Watson-Crick pairing and mismatches (Kervio et al., 2010; Leu et al., 2013; Leu et al., 2011). While some activation chemistries (relying on bridged dinucleotides) have been shown to exhibit improved fidelity (Duzdevich et al., 2021), the error probability still constrains the length of the genome that can be reliably replicated.

The issue of insufficient thermodynamic discrimination can, in principle, be mitigated by making use of kinetic stalling after the incorporation of a mismatch (Leu et al., 2013; Rajamani et al., 2010). By introducing a competition between the reduced polymerization rate and a characteristic timescale of the non-equilibrium environment, it is possible to filter correct sequences from incorrect ones (Göppel et al., 2021). To address the challenge of incomplete copies, Zhou et al. propose a new scenario of replication, the so-called Virtual Circular Genome (VCG) (Zhou et al., 2021). In this scenario, genetic information is stored in a pool of oligomers that are shorter than the circular genome they collectively encode: Each oligomer bears a subsequence of the circular genome, such that the collection of all oligomers encodes the full circular genome virtually. Within the pool, each oligomer can act as a template or primer (Zhou et al., 2021). The oligomers hybridize to each other and form complexes that allow for templated ligation of two oligomers, or for the extension of an oligomer by a monomer. Because the sequences of the ligated strands and the template are part of the genome, most of the products should also retain the sequence of the genome. That way, long oligomers encoding the circular genome can be produced at the expense of short oligomers (Zhou et al., 2021). The long strands, in turn, can assemble into catalytically active ribozymes. With a continuous influx of short oligomers, the VCG might allow for continuous replication of the virtually encoded circular genome. Importantly, replication in the VCG is expected to avoid the issue of incomplete copies. Since the genome is circular, it does not matter which part of the genome an oligomer encodes, as long as the sequence is compatible with the genome sequence. An additional feature of the VCG scenario is that replication should be achievable without the need of adding many nucleotides to a primer: Provided the concentration of oligomers decreases exponentially with their length, the concentration of each oligomer in the pool can be doubled by extending each oligomer only by a few nucleotides (Zhou et al., 2021). The extension of an oligomer by a few nucleotides in a VCG pool has already been demonstrated experimentally (Ding et al., 2023).

A recent computational study points out that the VCG scenario is prone to loss of genetic information via ‘sequence scrambling’ (Chamanian and Higgs, 2022). If the genome contains identical sequence motifs at multiple different loci, replication in the VCG will mix the sequences of these loci, thus destroying the initially defined genome. It is currently unclear which conditions could prevent this genome instability of VCGs, such that their genetic information is retained. Length distribution, sequence composition, oligonucleotide concentration, and environmental conditions, such as temperature, all affect the stability of complexes and thus the replication dynamics of the VCG pool. Here, we characterize the replication fidelity and yield of VCG pools using a kinetic model, which explicitly incorporates association and dissociation of RNA strands as well as templated ligation. We study a broad spectrum of prebiotically plausible and experimentally accessible oligomer pools, from pools containing only monomers and long oligomers of a single length to pools including a range of long oligomers with uniform or exponential concentration profile. The length of the included oligomers as well as their concentration is a free parameter of our model.

We find that, regardless of the pool composition, three competing types of template-directed ligation reactions emerge: (i) ligations between two short oligomers (or monomers), producing products too short to specify a unique genomic locus, (ii) ligations between a short and a long oligomer, typically generating longer products compatible with the genome sequence, and (iii) ligations between two long oligomers, which often yield sequences incompatible with the genome. These erroneous ligations of type (iii) are a key driver of sequence scrambling, as they covalently link oligomers originating from non-adjacent genomic loci, effectively ‘mixing’ distant regions of the genome. Fidelity is primarily determined by the competition between the correct extension of a long oligomer and the erroneous ligation of two long oligomers. The likelihood of the latter can be reduced by decreasing the relative abundance of long oligomers, even though this increases the frequency of unproductive ligations between short oligomers. As a result, fidelity can be improved at the cost of reduced yield. The efficiency, meaning the yield attainable at a fixed high fidelity, thus depends on the length distribution of the oligomers in the pool.

Alternatively, the issue of erroneous ligations is mitigated if ligations of long oligomers are kinetically suppressed, such that each ligation incorporates only one monomer at a time, as in the experimental study by Ding et al., 2023. In this case, the VCG concentration can be chosen arbitrarily large without compromising fidelity. Interestingly, our model predicts an unexpected feature: In the limit of high VCG concentrations, short oligomers are more likely to be extended than long oligomers, even though, intuitively, complexes containing longer oligomers are expected to be more stable and thus more productive. The same behavior was indeed observed experimentally (Ding et al., 2023). We provide an explanation for this feature and discuss its dependence on system parameters such as the length and the concentration of long oligomers in the pool.

## Results

### Modelling approach

In the VCG scenario, a circular genome is stored in a pool of oligomers, with each oligomer shorter than the genome it helps encode. Each oligomer bears a subsequence of the circular genome, such that, collectively, the oligomers encode the full genome (Figure 1A). As the spontaneous emergence of such VCG pools is expected to be rare (Chamanian and Higgs, 2022), our study focuses on the conditions under which an existing VCG pool can reliably replicate. We therefore begin with a known genome and an associated VCG pool, without addressing the question of origin. To set up our model of VCG dynamics, we specify (i) the circular genome used, (ii) the procedure by which the genome is mapped to a set of oligomers, and (iii) the chemical reactions governing the system’s evolution.

![Figure 1.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig1-v1.jpg)

**Figure 1.:** (A) In the Virtual Circular Genome (VCG) scenario, a circular genome (depicted in green) as well as its sequence complement are encoded in a pool of oligomers (depicted in blue and orange). Collectively, the pool of oligomers encodes the whole sequence of the circular genome. Depending on their length, two types of oligomers can be distinguished: Long VCG oligomers specify a unique locus on the genome, while feedstock molecules (monomers or short oligomers) are too short to do so. (B) The length distribution of oligomers included in the VCG pool is assumed to be exponential. The concentration of feedstock and VCG oligomers as well as their respective length scales of exponential decay $κ_{F}^{−1}$ and $κ_{V}^{−1}$ can be varied independently. The set of included oligomer lengths can be restricted via $L_{F}^{min}$, $L_{F}^{max}$ and $L_{V}^{min}$, $L_{V}^{max}$. (C) The hybridization energy of complexes is computed using a simplified nearest-neighbor model: Each full block comprised of two base pairs (depicted in pink) contributes $\gamma$, while dangling end blocks (depicted in blue) contribute $\gamma/2$. (D) Oligomers form complexes via hybridization reactions, or dehybridize from an existing complex. The ratio of hybridization and dehybridization rate is governed by the hybridization energy (Equation 1). If two oligomers are adjacent to each other in a complex, they can undergo templated ligation. (E) Based on the length of the reacting oligomers, we distinguish three types of templated ligation: Ligation of two feedstock molecules (F+F), ligation of a feedstock molecule to a VCG oligomer (F+V) and ligation of two VCG oligomers (V+V).

#### Circular genomes

For a given genome length, $L_{G}$, there are $4^{L_{G}}/2L_{G}$ distinct circular genomes (the factor $1/2L_{G}$ accounts for the freedom to select the starting position and to choose the Watson or the Crick strand as reference sequence). A key property of the genome is its unique motif length, $L_{U}$, defined as the shortest length such that all possible subsequences of length $L\geqL_{U}$ appear at most once in the genome. In other words, all subsequences of length $L\geqL_{U}$ specify a unique locus on the genome. In addition, each circular genome has another length scale, corresponding to the maximal motif length, up to which all possible motifs are contained in the genome. We refer to this length as the exhaustive coverage length, $L_{E}$. We typically analyze unbiased genomes in which all possible subsequences of length $L\leqL_{E}$ are contained at equal frequency.

#### Construction of VCG pools

To specify a VCG pool that encodes a genomic sequence, one must select which subsequences are included in the pool at which concentrations. We consider unbiased pools, where the concentration of subsequences, $c(L)$, depends only on their length, $L$, that is all subsequences of a given length are included at equal concentration. We refer to the length-dependent concentration profile as the length distribution of the pool. Depending on their length, oligomers fall into two categories (Figure 1B): (i) short feedstock molecules (monomers and oligomers) and (ii) long VCG oligomers. Feedstock oligomers are oligomers that are shorter than the unique motif length $L_{U}$. Since their sequence appears multiple times on the genome, they do not encode a specific position on the genome. Thus, they serve as feedstock for the elongation of VCG oligomers rather than as information storage. Conversely, VCG oligomers, which are longer than the unique motif length $L_{U}$, have a unique locus on the circular genome. Collectively, the VCG oligomers enable the reconstruction of the full genome. The full-length distribution, $c(L)$, can be decomposed into the contributions of feedstock and VCG oligomers,

$$
c(L)=c_{F}(L)+c_{V}(L).
$$

We assume that both $c_{F}$ and $c_{V}$ follow an exponential length distribution. In our model, the concentration of VCG oligomers can be varied independently of the concentration of feedstock, and the length scales for the exponential decay ($κ_{F}^{−1}$ vs. $κ_{V}^{−1}$) may differ between feedstock and VCG oligomers. Additionally, we can restrict the set of oligomer lengths included in the pool by setting minimal and maximal lengths for feedstock and VCG oligomers individually,

$$
c_{F}(L)=c^_{F}exp⁡(−κ_{F}L)if L_{F}^{min}\leqL\leqL_{F}^{max},c_{V}(L)=c^_{V}exp⁡(−κ_{V}L)if L_{V}^{min}\leqL\leqL_{V}^{max}.
$$

For any other oligomer length, the concentrations equal zero. This parameterization includes uniform length distributions as a special case ($κ_{F}=0$ and $κ_{V}=0$), and also allows for concentration profiles that are peaked. Peaked length distributions can emerge from the interplay of templated ligation, (de)hybridization, and outflux in open systems (Rosenberger et al., 2021). We define the total concentration of feedstock, $c_{F}^{tot}=\sumLc_{F}(L)$, as well as the total concentration of VCG oligomers, $c_{V}^{tot}=\sumLc_{V}(L)$. Their ratio will turn out to be an important determinant of the VCG dynamics.

#### (De)hybridization kinetics

Oligomers can hybridize to each other to form double-stranded complexes, or dehybridize from an existing complex. For simplicity, we do not include self-folding within a strand, which is a reasonable assumption for short oligomers. The stability of a complex is determined by its hybridization energy, with lower hybridization energy indicating greater stability. We use a simplified nearest-neighbor energy model to compute the hybridization energy (Göppel et al., 2022; Laurent et al., 2024; Rosenberger et al., 2021): The total energy equals the sum of the energy contributions of all nearest-neighbor blocks in a given complex (Figure 1C). The energy contribution associated with a block of two Watson-Crick base pairs (matches) is denoted $\gamma<0$, and dangling end blocks involving one Watson-Crick pair and one free base contribute $\gamma/2$. Nearest-neighbor blocks with mismatches increase the hybridization energy by $\gamma_{MM}>0$ per block, thus reducing the stability of the complex. The rate constants of hybridization and dehybridization are related via

$$
\frac{k_{off}}{k_{on}}=c^{∘}exp(\betaΔG),
$$

where $c^{∘}=1M$ is the standard concentration, $\beta=(k_{B}T)^{−1}$ is the Boltzmann factor, and $ΔG$ is the free energy of hybridization. The association rate constant $k_{on}$ is proportional to the encounter rate constant, $k_{enc}=1/(c^{∘}t_{0})$. The encounter timescale $t_{0}$ serves as the elementary time unit of the kinetic model, with all reaction timescales measured relative to it.

#### Templated ligation

Two oligomers A and B that are hybridized adjacently to each other on a third oligomer C can produce a new oligomer A-B via templated ligation (Figure 1D). Depending on the length of A and B, we distinguish three types of ligation reactions (Figure 1E): (i) F+F ligations, in which two feedstock molecules ligate, (ii) F+V ligations, where a VCG oligomer is extended by a feedstock molecule, and (iii) V+V ligations involving two VCG oligomers. The formation of a covalent bond via templated ligation is not spontaneous but requires the presence of an activation reaction. Usually, these reactions add a leaving group to the 5′-end of the nucleotide, which is cleaved during bond formation (Kervio et al., 2016; Walton and Szostak, 2016). We assume that the concentration of activating agent is sufficiently high for the activation to be far quicker than the formation of the covalent bond, such that activation and covalent bond formation can be treated as a single effective reaction. When not otherwise stated, we assume that all possible templated ligation reactions occur with the same rate constant $k_{lig}$.

#### Observables

Templated ligation in the pool forms longer oligomers at the expense of shorter oligomers and monomers. While the product of an F+V ligation (or V+V ligation) is always a VCG oligomer, F+F ligations can produce feedstock or VCG oligomers. In both cases, a produced VCG oligomer can be correct (compatible with the genome) or incorrect (incompatible). We quantify these processes by measuring extension fluxes in units of nucleotides ligated to an existing strand (counting the length of the shorter ligated strand as the number of incorporated bases). In particular, we define the fidelity $f$ as the extension flux resulting in correct VCG oligomers relative to the flux resulting in any VCG oligomer,

$$
f=\frac{#nucleotides incorporated in correct VCG oligomers}{# nucleotides incorporated in VCG oligomers}.
$$

In addition, we introduce the yield $y$ as the proportion of total extension flux that produces VCG oligomers,

$$
y=\frac{# nucleotides incorporated in VCG oligomers}{# incorporated nucleotides}.
$$

Efficient replication of the VCG requires both high fidelity and high yield. Hence, we introduce the efficiency of replication $η$ as the product of fidelity and yield,

$$
η=f⋅y=\frac{# nucleotides incorporated in correct VCG oligomers}{# incorporated nucleotides}.
$$

Moreover, we define the ligation share $s$ of a ligation type, which allows us to discern the contributions of different types of templated ligations (F+F, F+V, V+V) to fidelity, yield, and efficiency,

$$
s(type)=\frac{# nucleotides incorporated via ligation type}{# incorporated nucleotides}.
$$

### Replication efficiency reaches a maximum at intermediate concentrations of VCG oligomers

We begin our analysis of the dynamics of VCG pools with an exemplary genome of length $L_{G}=16 nt$,

This genome contains all possible monomers and dimers with equal frequency, ensuring that all motifs up to $L_{E}=2 nt$ are represented. Identifying a unique address on this genome requires at least three nucleotides. Therefore, the unique motif length is $L_{U}=3 nt$, and VCG oligomers need to be at least 3 nt long. Further below, we also explore genomes of different lengths $L_{G}$, as well as varying characteristic sequence length scales $L_{E}$ and $L_{U}$ (genome construction detailed in the Methods section).

Based on the genome, we construct the initial oligomer pool. As a first step, we focus on a simple scenario in which the pool contains only monomers (serving as feedstock) and VCG oligomers of a single, defined length. The VCG pools are evolved in time using a stochastic simulation based on the Gillespie algorithm (Göppel et al., 2022; Laurent et al., 2024; Rosenberger et al., 2021). Since the Gillespie algorithm operates on the level of counts of molecules instead of concentrations, we must assign a volume to each system (in the range $1\mum^{3}$ to $10000μm^{3}$, see Methods). Besides the volume, we also need to choose the reaction rate constants appropriately: (i) The association time $t_{0}$ is the fundamental time unit in our kinetic model, and all other times are expressed relative to $t_{0}$. Experimentally determined association rate constants are typically around $10^{6}−10^{7}M^{−1}s^{−1}$(Ashwood et al., 2023; Braunlin and Bloomfield, 1991; Todisco et al., 2024a; Wetmur and Davidson, 1968). For the purpose of estimating absolute timescales, we therefore assume a constant association timescale of $t_{0}=(k_{on}c^{∘})^{−1}≈1μs$ in the following. (ii) The timescale of dehybridization is computed via Equation 1 using the energy contribution $\gamma=−2.5 k_{B}T$ for a matching nearest-neighbor block and $\gamma_{MM}=25.0 k_{B}T$ in case of mismatches. The high energy penalty of nearest-neighbor blocks involving mismatches, $\gamma_{MM}$, is chosen to suppress the formation of mismatches, while the value of $\gamma$ roughly matches the average energy of all matching nearest-neighbor blocks given by the Turner energy model of RNA hybridization (Mathews et al., 2004). (iii) For templated ligation, we select a reaction rate constant of $k_{lig}=10^{−12} t_{0}^{−1}$. This choice of $k_{lig}$ is consistent with ligation rates measured in enzyme-free template-directed primer extension experiments, which range from around $10^{−6}s^{−1}$ $(10^{−12} t_{0}^{−1})$ (Leveau et al., 2022; Sosson et al., 2019) to roughly $10^{−4}s^{−1}$ $(10^{−10} t_{0}^{−1})$ (Walton and Szostak, 2017), depending on the underlying activation chemistry. This indicates that, for sufficiently short oligomers (up to about 11 nt long), hybridization and dehybridization occur much faster than ligation, so binding equilibrates before ligation takes place.

Based on the ligation events observed in the simulation, we compute the observables introduced above. Due to the small ligation rate constant, it is computationally unfeasible to simulate the time evolution for more than a few ligation time units. Consequently, ligation events are scarce, which leads to high variances in the computed observables. We mitigate this issue by calculating the observables based on the concentration of complexes that are in a productive configuration, even if they do not undergo templated ligation within the time window of the simulation (Methods).

The observable $y$ (yield) quantifies the fraction of this total flux directed to producing VCG oligomers. Figure 2B shows how the yield depends on the concentration of VCG oligomers, $c_{V}^{tot}$, at a fixed total monomer concentration, $c_{F}^{tot}=0.1mM$. Here, the data points (with error bars) represent the simulation results with the different colors corresponding to different choices of initial VCG oligomer length, $L_{V}$. We observe that the yield increases monotonically with the concentration of VCG oligomers and approaches 100% for high $c_{V}^{tot}$. The concentration at which the pool reaches a yield of 50% depends on the oligomer length $L_{V}$: Shorter VCG oligomers require higher concentrations for high yield. The concentration dependence of the yield can be rationalized by the types of templated ligations that are involved. For low VCG concentration, most templated ligation reactions are dimerizations (1+1) with the VCG oligomers merely acting as templates (Figure 2C). As dimers are shorter than the unique motif length $L_{U}$, their formation does not contribute to the yield, which explains the low yield in the limit of small $c_{V}^{tot}$. Conversely, for high VCG concentration, most of the templated ligations are F+V or V+V ligations, which produce oligomers of length $L\geqL_{U}$, implying high yield.

![Figure 2.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig2-v1.jpg)

**Figure 2.:** (A) The pool contains a fixed concentration of monomers, $c_{F}^{tot}=0.1mM$, as well as VCG oligomers of a single length, $L_{V}$, at variable concentration $c_{V}^{tot}$ (the VCG oligomers cover all possible subsequences of the genome and its complement at equal concentration). (B) The yield increases as a function of $c_{V}^{tot}/c_{F}^{tot}$, because dimerizations become increasingly unlikely for high VCG concentrations. (C) The ligation share of different ligation types depends on the total VCG concentration: In the low concentration limit, dimerization (F+F) dominates; for intermediate concentrations, F+V ligations reach their maximum, while, for high concentrations, a substantial fraction of reactions are V+V ligations. The panel depicts the behavior for $L_{V}=6 nt$. (D) Replication efficiency is limited by the small yield for small $c_{V}^{tot}/c_{F}^{tot}$. In the limit of high $c_{V}^{tot}/c_{F}^{tot}$, replication efficiency decreases due to the growing number of error-prone V+V ligations. Maximal replication efficiency is reached at intermediate VCG concentration. (E) V+V ligations are prone to the formation of incorrect products due to the short overlap between educt strand and template. In general, the probability of correct product formation, $p_{corr}$, depends on the choice of circular genome and as well as its mapping to the VCG pool. The probabilities listed here refer to a VCG pool with $L_{G}=16 nt$, $L_{E}=2nt$ and $L_{U}=3nt$. (F) The optimal equilibrium concentration ratio of free VCG strands to free feedstock strands, which maximizes replication efficiency, decays as a function of length (continuous line). The analytical scaling law (dashed line, Equation 2) captures this behavior. The window of close-to-optimal replication, within which efficiency deviates no more than 1% from its optimum (shaded areas), increases with $L_{V}$ facilitating reliable replication without fine-tuning to match the optimal concentration ratio. (G) Maximal replication efficiency, which is attained at the optimal VCG concentration depicted in panel E, increases as a function of $L_{V}$ and approaches a plateau of 100%. For high efficiency, Equation 3 provides a good approximation of the length-dependence of $η_{max}$ (dashed lines). The oligomer length at which replication efficiency equals 95% is determined using Equation 3 (vertical dotted lines). (H) The unique motif length, $L_{U}^{min}$ increases logarithmically with the length of the genome, $L_{G}$. The length of VCG oligomers, $L_{V}$ at which the optimal replication efficiency reaches 95% (computed using Equation 3) exhibits the same logarithmic dependence on $L_{G}$.

Figure 2C also shows that the relative contribution of V+V ligations increases with increasing $c_{V}^{tot}$, with a large fraction of them producing incorrect products (denoted V+V,f). This reduces the fidelity of replication, $f$, and leads to a trade-off between fidelity and yield, which causes replication efficiency, $η=f⋅y$, to reach a maximum at intermediate VCG concentrations (Figure 2D). Using hexamers as an example, Figure 2E illustrates why V+V ligations are prone to forming incorrect oligomers: In order to ensure that two oligomers only ligate if their sequences are adjacent to each other in the true circular genome, both oligomers need to share an overlap of at least $L_{U}$ nucleotides with the template oligomer. Otherwise, the hybridization region is too short to identify the locus of the oligomer uniquely, and two oligomers from non-adjacent loci might ligate. The probability of forming incorrect products is a consequence of the combinatorics of possible subsequences in the VCG. Specifically, for a genome with $L_{G}=16 nt$, there are 32 different hexamers. For example, if the left educt hexamer only has one nucleotide of overlap with the template, there are $1/4⋅32=8$ possible educt oligomers. However, only one out of those eight hexamers is the correct partner for the right educt hexamer, implying an error probability of $1−1/8=7/8$ (first example in Figure 2E).

Characterizing replication efficiency via full simulations is computationally expensive. Depending on parameters, obtaining a single data point in Figure 2B-D can require hundreds of simulations, each lasting several days. To explore a broad parameter space more easily, we introduce an approximate adiabatic method that (i) assumes ligation is much slower than any hybridization or dehybridization event, and (ii) relies on a coarse-grained sequence-independent representation of oligomers. Details are provided in the Methods section. In brief, because ligation is rare, we first compute the equilibrium distribution of free and bound oligomers. Oligomers of the same length share a common concentration, and complex concentrations are determined via the mass action law using length-dependent dissociation constants. Combining the mass action law with a mass conservation constraint for each oligomer length allows us to compute the equilibrium concentrations of free VCG and feedstock strands, $c_{V}^{eq}$ and $c_{F}^{eq}$, given total concentrations $c_{V}^{tot}$ and $c_{F}^{tot}$. With these equilibrium values, we determine the concentrations of productive complexes and thus obtain the desired ligation‐based observables without running full stochastic simulations.

The results of the adiabatic approach agree well with the simulation data (Figure 2B-D), supporting that the replication efficiency depends non-monotonously on the concentration of VCG oligomers, with a maximum at intermediate concentration. While the available simulation data only allows for a qualitative characterization of this trend, the adiabatic approach enables a quantitative analysis. For instance, we use the adiabatic approach to determine the equilibrium concentration ratio at which replication efficiency is maximal as a function of the VCG oligomer length $L_{V}$ (solid lines in Figure 2F). As expected from the qualitative trend observed in the simulation, pools containing longer oligomers reach their maximum for lower concentration of VCG oligomers. The shaded area indicates the range of VCG concentrations within which the pool’s efficiency deviates by no more than one percent from its optimum. We observe that this range of close-to-optimal VCG concentrations increases with $L_{V}$. Thus, pools containing longer oligomers require less fine-tuning of the VCG concentration for replication with high efficiency.

In addition to the numerical results, we utilize the adiabatic approach to study the optimal equilibrium VCG concentration analytically (Appendix 1). We find that, for any choice of $L_{V}$, replication efficiency reaches its maximum when the fractions of dimerization (1+1) reactions and erroneous V+V ligations are equal (Figure 2C for $L_{V}=6 nt$). This criterion can be used to derive a scaling law for the optimal equilibrium concentration ratio $c_{V}^{eq}/c_{F}^{eq}$ as a function of the oligomer length $L_{V}$,

$$
\frac{c_{V}^{eq}}{c_{F}^{eq}}|_{opt}∼\sqrt{\frac{1}{Λ_{F+F}}−\frac{1}{L_{V}}}exp⁡(−\frac{|\gamma|L_{V}}{2}),
$$

which is shown as dashed lines in Figure 2F (the length-scale $Λ_{F+F}$ is defined in Appendix 1). The optimal equilibrium concentration ratio decreases exponentially with $L_{V}$, while the hybridization energy $\gamma/2$ sets the inverse length scale of the exponential decay. Analytical estimate and numerical solution agree well, as long as the hybridization is weak and oligomers are sufficiently short. For strong binding and long oligomers, complexes involving more than three strands play a non-negligible role, but such complexes are neglected in the analytical approximation.

Figure 2G shows how the maximal replication efficiency depends on the VCG oligomer length. Consistent with the qualitative trend observed in Figure 2D, longer oligomers enable higher maxima in replication efficiency. Regardless of the choice of $\gamma$, replication efficiency reaches 100% if $L_{V}$ is sufficiently high. Starting from Equation 2, we find the following approximation for the maximal replication efficiency attainable at a given oligomer length (dashed lines in Figure 2G),

$$
η_{max}≈1−η^{∘}\sqrt{\frac{1}{Λ_{F+F}}−\frac{1}{L_{V}}}L_{V}exp⁡(−\frac{|\gamma|L_{V}}{2}),
$$

where $η^{∘}$ is a genome-dependent constant (Appendix 1). This equation can provide guidance for the construction of VCG pools with high replication efficiency: Given a target efficiency, the necessary oligomer length and hybridization energy, that is temperature, can be calculated. In Figure 2G, we determine the oligomer length necessary to achieve $η_{max}=95%$ for varying hybridization energies $\gamma$. At higher temperatures (weaker binding), VCG pools require longer oligomers to replicate with high efficiency.

Equation 3 is not restricted to the specific example genome of length $L_{G}=16 nt$, but applies more generally to genomes of arbitrary length. Any genome of length $L_{G}$ can contain at most $2L_{G}$ distinct motifs. Consequently, the minimum length required to specify a unique address on the genome equals $L_{U}^{min}=⌈\frac{ln⁡(2L_{G})}{ln⁡4}⌉$. By the same logic, the longest motif length for which all $4^{L}$ possible sequences can be exhaustively represented within the genome is $L_{E}^{max}=⌊\frac{ln⁡(2L_{G})}{ln⁡4}⌋$. Both of these characteristic lengths scale logarithmically with genome size. For genomes where $L_{E}$ is taken to be maximal and $L_{U}$ minimal, we find that the characteristic VCG oligomer length $L_{V}^{⋆}$ required for replication with high efficiency ($η_{max}=95%$) also scales logarithmically with genome length (Figure 2H). Across genome lengths, the offset between $L_{U}$ and $L_{V}^{⋆}$ is roughly constant.

In genomes with different choices of $L_{E}$ and $L_{U}$ $(L_{E}<L_{E}^{max}andL_{U}>L_{U}^{min})$, the characteristic VCG oligomer length required for efficient replication, $L_{V}^{⋆}$, is primarily determined by the unique motif length $L_{U}$. Specifically, the length of VCG oligomers, $L_{V}$, must exceed $L_{U}$, regardless of the value of $L_{E}$. This is shown for genomes of length $L_{G}=64nt$ in Appendix 2, where we generate genomes with specified length scales $L_{E}$ and $L_{U}$ using a Metropolis–Hastings algorithm and analyze their replication efficiency. Intuitively, the required VCG oligomer length $L_{V}^{⋆}$ is set by $L_{U}$, because $L_{U}$ defines the minimal hybridization region needed to ensure correct ligation via sequence-specific recognition. The precise offset between $L_{U}$ and $L_{V}^{⋆}$ depends on genome-specific features, such as the frequency distribution of motifs with lengths between and $L_{U}$. If this distribution is nearly uniform (noting that at least one motif must repeat, or else it would constitute a unique address), then $L_{V}^{⋆}$ will be close to $L_{U}$ (Appendix 2—figure 1B). In contrast, strongly biased motif distributions require larger $L_{V}^{⋆}$ to achieve reliable replication (Appendix 2—figure 1A), though even in this case, $L_{V}^{⋆}$ typically exceeds by only a few nucleotides.

### Replication in multi-length VCG pools is dominated by the longest oligomers

In the previous section, we characterized the behavior of pools containing VCG oligomers of a single length. We observed that V+V ligations are error-prone due to insufficient overlap between the educt strands and the template, whereas F+V ligations extend the VCG oligomers with high efficiency. The F+V ligations will gradually broaden the length distribution of the VCG pool, raising the question of how this broadening affects the replication behavior. In principle, introducing multiple oligomer lengths into the VCG pool might even improve the fidelity of V+V ligations, since a long VCG oligomer could serve as a template for the correct ligation of two shorter VCG oligomers.

To analyze this question quantitatively, we first consider the simple case of a VCG pool that only contains monomers, tetramers, and octamers. The concentration of monomers is set to $c(1)=0.1mM$, while the concentrations of the VCG oligomers are varied independently (Figure 3A). Replication efficiency reaches its maximum at $c(8)≈0.1μM$ and very low tetramer concentration, $c(4)≈7.4pM$, effectively resembling a single-length VCG pool containing only octamers. As shown in Figure 3B, the maximal efficiency is surrounded by a plateau of close-to-optimal efficiency. The octamer concentration can be varied by more than one order of magnitude without significant change in efficiency. Similarly, adding tetramers does not affect efficiency as long as the tetramer concentration does not exceed the octamer concentration. Figure 3C illustrates that the plateau of close-to-optimal efficiency coincides with the concentration regime where the ligation of a monomer to an octamer with another octamer acting as template, $\frac{1|8}{8}$, is the dominant ligation reaction. For high tetramer concentration and intermediate octamer concentration, templated ligation of tetramers on octamer templates, $\frac{4|4}{8}$, surpasses the contribution of $\frac{1|8}{8}$ ligations (green shaded area in Figure 3C). The $\frac{4|4}{8}$ reactions give rise to a ridge of increased efficiency, which, however, is small compared to the plateau of close-to-optimal efficiency (Figure 3B). Even though reactions of the type $\frac{4|4}{8}$ produce correct products in most cases, they compete with error-prone ligations like $\frac{4|8}{8}$ or $\frac{4|4}{4}$, which reduce fidelity. Increasing the binding affinity, that is lowering $\gamma$, enhances the contribution of $\frac{4|4}{8}$ ligations at the expense of $\frac{4|8}{8}$ ligations, resulting in an increased local maximum in replication efficiency (Figure 3—figure supplement 1). However, very strong hybridization energy, $\gamma=−5.0 k_{B}T$, is necessary for $\frac{4|4}{8}$ ligations to give rise to similar efficiency as $\frac{1|8}{8}$ ligations. Thus, in this example, high efficiency replication facilitated by the ligation of short VCG oligomers on long VCG oligomers is in theory possible, but requires unrealistically strong binding affinity. Moreover, this mechanism is only effective if educts and template differ significantly with respect to their length. If the involved VCG oligomers are too similar in size, templated ligation of two short oligomers tends to be error-prone, irrespective of the choice of binding affinity (Figure 3—figure supplement 2 and Figure 3—figure supplement 3). In that case, F+V ligations remain the most reliable replication mechanism.

![Figure 3.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig3-v1.jpg)

**Figure 3.:** (A) The pool contains a fixed concentration of monomers, $c_{F}^{tot}=0.1mM$, as well as tetramers and octamers at variable concentration. The hybridization energy per nearest-neighbor block is $\gamma=−2.5 k_{B}T$. (B) Replication efficiency reaches its maximum for $c(8)≈0.1\muM$ and significantly lower tetramer concentration, $c(4)≈7.4 pM$. Efficiency remains close to maximal on a plateau around the maximum spanning almost two orders of magnitude in tetramer and octamer concentration. In addition, efficiency exhibits a ridge of increased efficiency for high tetramer concentration and intermediate octamer concentration. (C) Complexes that facilitate templated ligation are grouped by the length of the template and the educts, $\frac{L_{educt,1}|L_{educt,2}}{L_{template}}$. We distinguish complexes producing correct (labeled ‘c’) and false products (labeled ‘f’). For each relevant type of complex, we highlight the region in the concentration plane where it contributes most significantly, that is at least 20% of the total ligation flux. The plateau of high efficiency is dominated by the ligation of monomers to octamers, whereas the ridge of increased efficiency is due to the correct ligation of two tetramers templated by an octamer.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Replication performance in pools containing tetramers and octamers for strong binding affinity, $\gamma=−5.0k_{B}T$.Replication efficiency reaches its maximum in the concentration regime that supports templated ligation of tetramers on octamer templates.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** Replication performance in pools containing heptamers and octamers for weak binding affinity, $\gamma=−2.5k_{B}T$.Replication efficiency reaches its maximum in the concentration regime dominated by the addition of monomers to the VCG oligomers.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** Replication performance in pools containing heptamers and octamers for strong binding affinity, $\gamma=−5.0k_{B}T$.Replication efficiency reaches its maximum in the concentration regime dominated by the addition of monomers to the VCG oligomers.

We observe similar behavior in VCG pools containing a range of oligomer lengths from $L_{V}^{min}$ to $L_{V}^{max}$, rather than just tetramers and octamers. For a uniform VCG concentration profile (Figure 4A, dark gray), the maximal replication efficiency (at the optimal VCG concentration) is attained when F+V ligations involving long VCG oligomers dominate the templated ligation (see Figure 4D showing the contribution of different ligation types in pools with varying $L_{V}^{min}$ at fixed $L_{V}^{max}=10nt$). Importantly, the maximal replication efficiency is always bounded by the efficiency of the longest VCG oligomer in the pool, independent of the presence or length of shorter oligomers (blue curve in Figure 4B; identical to the orange curve in Figure 2G). Including short VCG oligomers has minimal effect on the dominant ligation types and only slightly increases the proportion of unproductive F+F ligations. Consequently, reducing $L_{V}^{min}$ while keeping $L_{V}^{max}$ fixed leads to only a modest decline in maximal efficiency. In contrast, decreasing $L_{V}^{max}$ while holding $L_{V}^{min}$ constant causes a substantial reduction in efficiency (Figure 4B), because the longest oligomer in the pool sets an upper bound on replication efficiency. Moreover, at low $L_{V}^{max}$, short and long oligomers become more similar in length, giving rise to a spectrum of erroneous V+V ligations that compete with the productive F+V ligations (Figure 4E).

![Figure 4.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig4-v1.jpg)

**Figure 4.:** (A) The pool contains a fixed concentration of monomers, $c_{F}^{tot }=0.1mM$, as well as long oligomers in the range $L_{V}^{min}\leqL_{V}\leqL_{V}^{max}$ at variable concentration $c_{V}^{tot}$. The length dependence of the concentration profile is assumed to be uniform (for panels B, D, and E) or exponential (for panel C); its steepness is set by the parameter $κ_{V}$. (B) If the length distribution is uniform, reducing $L_{V}^{min}$ decreases the maximal efficiency, whereas increasing $L_{V}^{max}$ increases it. Pools containing a range of oligomer lengths are always outperformed by single-length VCGs (blue curve). (C) Assuming an exponential length distribution of VCG oligomers allows us to tune from a poorly-performing regime (dominated by oligomers of length $L_{V}^{min}$) to a well-performing regime (dominated by oligomers of length $L_{V}^{max}$). In the limit $κ_{V}→∞$, $η_{max}$ approaches the replication efficiency of single-length pools containing only oligomers of length $L_{V}^{min}$ (dashed lines). (D) For high $L_{V}^{max}$, replication is dominated by primer extension of the long oligomers in the VCG (here $L_{V}^{max}=10nt$). In this limit, addition of shorter oligomers leaves the dominant F+V ligations almost unchanged. (E) Reducing $L_{V}^{max}$ for fixed $L_{V}^{min}=3 nt$ increases the fraction of unproductive (i.e. dimerization) or erroneous ligation reactions.

In a realistic prebiotic scenario, the concentration profile of the VCG pool would not be uniform. Depending on the mechanism producing the pool and its coupling to the non-equilibrium environment, it might have a concentration profile that decreases or increases exponentially with length. We use the parameter $κ_{V}$ to control this exponential length dependence (Figure 4A): For negative $κ_{V}$, the concentration increases as a function of length, while exponentially decaying length distributions have positive $κ_{V}$. We find that replication efficiency is high if the concentration of long VCG oligomers exceeds or at least matches the concentration of short VCG oligomers ($κ_{V}\leq0$ in Figure 4C). In that case, replication efficiency is dominated by the long oligomers in the pool, since these form the most stable complexes. As the concentration of long oligomers is decreased further ($κ_{V}>0$), the higher stability of complexes formed by longer oligomers is eventually insufficient to compensate for the reduced concentration of long oligomers. Replication efficiency is then governed by short VCG oligomers, which exhibit lower replication efficiency. In the limit $κ_{V}→∞$, replication efficiency approaches the replication efficiency of a single-length VCG pool containing only oligomers of length $L_{V}^{min}$ (Figure 4C and Figure 2G).

### Adding dinucleotides to the feedstock decreases replication efficiency

So far, we focused on ensembles that contain solely monomers as feedstock. However, examining the influence of dimers on replication in VCG pools is of interest, since dinucleotides have proven to be interesting candidates for enzyme-free RNA copying (Leveau et al., 2022; Sosson et al., 2019; Walton and Szostak, 2016). For this reason, we study oligomer pools like those illustrated in Figure 5A: The ensemble contains monomers, dimers, and VCG oligomers of a single length, $L_{V}$. As our default scenario, the dimer concentration is set to 10% of the monomer concentration, corresponding to $κ_{F}=2.3$, but this ratio can be modified by changing $κ_{F}$.

![Figure 5.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig5-v1.jpg)

**Figure 5.:** (A) The pool contains a fixed total concentration of feedstock, $c_{F}^{tot}=0.1mM$, partitioned into monomers and dimers, as well as VCG oligomers of a single length, $L_{V}$. The proportion of monomers and dimers can be adjusted via $κ_{F}$, and the concentration of the VCG oligomers is a free parameter, $c_{V}^{tot}$. (B) Replication efficiency exhibits a maximum at intermediate VCG concentration in systems with (dashed blue curve) and without dimers (solid blue curve). The presence of dimers reduces replication efficiency significantly, as they enhance the ligation share of incorrect F+V ligations (dashed green curve). The panel depicts the behavior for $L_{V}=7 nt$ and $κ_{F}=2.3$. (C) Optimal replication efficiency increases as a function of oligomer length, $L_{V}$, and asymptotically approaches a plateau (dashed lines, Equation 4). The value of this plateau, $η_{max}^{∞}$, is determined by the competition between correct and false 2+V reactions, both of which grow exponentially with $L_{V}$. Thus, $η_{max}^{∞}$ depends on the relative concentration of the dimers in the pool: the more dimers are included, the lower is $η_{max}^{∞}$. (D) Erroneous 1+V ligations are possible if the educt oligomer has a short overlap region with the template. The hybridization energy for such configurations is small and independent of the length of the VCG oligomers (left). While 2+V ligations may produce incorrect products via the same mechanism (middle), incorrect product can also be caused by complexes in which two VCG oligomers hybridize perfectly to each other, but the dimer has a dangling end. The stability of these complexes increases exponentially with oligomer length (right).

Figure 5B compares the replication efficiency of a pool with ($L_{F}^{max}=2nt$) and without dimers ($L_{F}^{max}=1nt$). In both cases, pools that are rich in VCG oligomers exhibit low efficiency of replication. As erroneous V+V ligations are the dominant type of reaction in this limit, all pools achieve the same efficiency regardless of the presence of dimers. In contrast, when the pool is rich in feedstock (small $c_{V}^{tot}/c_{F}^{tot}$), pools with and without dimers behave differently: If only monomers are included, the efficiency approaches zero, as dimerizing monomers do not contribute to the yield, and thus not to the efficiency. However, the presence of dimers enables the ligation of monomers and dimers to form trimers and tetramers, which lead to a non-zero yield. Given the low VCG concentration, the ligations are likely to proceed using dimers as template. As a consequence, educt oligomers can only hybridize to the template with a single-nucleotide-long hybridization region, leading to frequent formation of incorrect products and, consequently, low efficiency.

Replication efficiency reaches its maximum at intermediate VCG concentrations, where replication is dominated by F+V ligations. Notably, the maximal attainable efficiency is significantly lower for pools with dimers than without, as dimers increase the number and the stability of complex configurations that can form incorrect products (Figure 5C). Without dimers, ligation products are only incorrect if the overlap between the VCG educt oligomer and template is shorter than the unique motif length, ﻿$L_{U}$. With dimers, however, dangling end dimers can cause incorrect products even in case of long overlap of educt oligomer and template (right column in Figure 5D). The stability of the latter complexes depends on the length of the VCG oligomers, $L_{V}$, whereas the stability of complexes facilitating incorrect monomer addition is independent of oligomer length (Figure 5D).

In the presence of dimers, the length-dependent stability of complexes allowing for correct and incorrect F+V ligations causes a competition, which sets an upper bound on the efficiency of replication (Appendix 3),

$$
η_{max}\leq\frac{K_{1+V,c}^{a,∘}+0.5 K_{2+V,c}^{a,∘} e^{−κ_{F}}}{K_{1+V,c}^{a,∘}+0.5 (K_{2+V,c}^{a,∘}+K_{2+V,f}^{a,∘}) e^{−κ_{F}}}.
$$

Here, we introduced effective association constants $K^{a}$, which depend differently on the VCG oligomer length, $L_{V}$. While the effective association constant $K_{1+V,f}^{a}$ of complexes enabling incorrect 1+V ligations is length-independent, the effective association constant for incorrect 2+V ligations, $K_{2+V,f}^{a}$, scales exponentially with $L_{V}$,

$$
K_{2+V,f}^{a}=K_{2+V,f}^{a,∘}exp(|\gamma|L_{V})
$$

The effective association constants for correct 1+V and 2+V ligations also scale exponentially with the oligomer length (Appendix 3—figure 1).

In systems without dimers, that is $κ_{F}→∞$, $η_{max}$ approaches 100%, which is consistent with the behavior observed in the previous sections. Conversely, in systems containing dimers, the maximal efficiency remains at a value below 100%, which depends on the concentration of dimers in the feedstock. Figure 5C shows the dependence of maximal replication efficiency on the length of VCG oligomers in pools containing monomers, dimers, and VCG oligomers. As $L_{V}$ increases, $η_{max}$ converges towards the upper bound defined in Equation 4 (dashed line in Figure 5C).

### Error-prone ligation of VCG oligomers can be kinetically suppressed

In all scenarios considered so far, the efficiency of replication is limited by a common mechanism, regardless of the specifics of the VCG pool: Ligations involving two oligomers that hybridize to the template over a region shorter than $L_{U}$ are prone to generate incorrect products. In previous sections, we minimized these erroneous ligations by fine-tuning the concentration and length of VCG oligomers. However, such control may become unnecessary if the typically error-prone ligation of two oligomers (V+V) is kinetically suppressed. Kinetic suppression can be an intrinsic property of the activation chemistry: Templated ligation of two oligomers can be several orders of magnitude slower than the extension of an oligomer by a single monomer (Ding et al., 2022; Prywes et al., 2016). As a result, V+V ligations are disfavored purely by their slower kinetics. In addition, it is conceivable that only monomers are chemically activated while longer oligomers remain inactive, which would further reduce the likelihood of erroneous ligations. This scenario has already been explored experimentally (Ding et al., 2023). In natural environments, it could occur, for instance, when activated monomers are produced externally and then diffuse into compartments containing the VCG but lacking internal activation pathways (Kriebisch et al., 2024; Toparlak et al., 2023).

Within our model, we capture the kinetic suppression by introducing two different rates of ligation, $k_{lig,1}$ for ligations involving a monomer and $k_{lig,>1}$ for ligations involving no monomer, allowing for kinetic discrimination between these processes. We explore the resulting replication efficiency in the limit of perfect kinetic discrimination ($k_{lig,>1}/k_{lig,1}→0$) where only monomers are reactive for ligation. We first consider a pool where the reactive monomers are mixed with VCG oligomers of a single length as well as non-reactive dimers (Figure 6A). We vary the concentration of VCG oligomers, but keep the feedstock concentrations constant. For small VCG concentrations, we observe low efficiencies (Figure 6B), as the ligation of two monomers, or one monomer and one dimer, is most likely. Conversely, high $c_{V}^{tot}$ facilitates the formation of complexes in which VCG oligomers are extended by monomers, which implies high efficiency (Figure 6B). Note that, unlike in systems where all oligomers are reactive, replication efficiency does not decrease for high VCG concentration, as erroneous V+V ligations are impossible. Instead, perfect replication efficiency (100%) is reached for sufficiently high $L_{V}$.

![Figure 6.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig6-v1.jpg)

**Figure 6.:** (A) The pool contains reactive monomers alongside non-reactive dimers and VCG oligomers of a single length. The concentrations of monomers and dimers are fixed, $c(1)=0.091mM$ and $c(2)=9.1\muM$, adding up to a total feedstock concentration of $c_{V}^{tot}=0.1mM$, while the concentration of VCG oligomers, $c_{V}^{tot}$, is varied. (B) Unlike in pools in which all ligation processes occur, replication efficiency does not decrease at high VCG concentration if ligations that do not involve monomers are kinetically suppressed. Instead, replication efficiency approaches an asymptotic value of 100%, as erroneous V+V ligations are impossible. (C) The fraction of oligomers that are in a monomer-extension-competent state depends on the total concentration of VCG oligomers. At low VCG concentration, most oligomers are single-stranded, and extension of oligomers by monomers is scarce. At high VCG concentration, $r_{1+V}$ approaches the asymptotic value $r_{1+V}^{∞}$ (grey dashed line, Figure 7.). In this limit, almost all oligomers form duplexes, which facilitate monomer addition upon hybridization of a monomer. Thus, the asymptotic fraction of oligomers that gets extended by monomers is not determined by the oligomer length, but by the binding affinity of monomers to existing duplexes. Conversely, the threshold concentration at which $r_{1+V}=r_{1+V}^{∞}/2$ depends on oligomer length (colored dashed lines): Longer oligomers reach higher $r_{1+V}$ at lower VCG concentration.

While replication efficiency characterizes the relative amount of nucleotides used for the correct elongation of VCG oligomers, it is also interesting to analyze which fraction of VCG oligomers is in a monomer-extension-competent state,

$$
r_{1+V}=c_{1+V}^{eq}/c_{V}^{tot}.
$$

Here, $c_{1+V}^{eq}$ denotes the equilibrium concentration of all complexes enabling the addition of a monomer to any VCG oligomer. We find that $r_{1+V}$ depends on the VCG concentration qualitatively in the same way as the efficiency: $r_{1+V}$ is small for small VCG concentration but approaches a value $r_{1+V}^{∞}$ asymptotically for high VCG concentration (Figure 6C). In this limit, almost all VCG oligomers are part of a duplex. Monomers can bind to these duplexes to form complexes allowing for 1+V ligations. Since almost all VCG oligomers are already part of a duplex, increasing $c_{V}^{tot}$ further does not increase the fraction of VCG oligomers that can be extended by monomers. Instead, the asymptotic value is determined by the concentration of monomers and their binding affinity $K_{d}(1)$ to an existing duplex (Appendix 4),

$$
r_{1+V}^{∞}≈\frac{1}{6}(\frac{c^{∘}}{K_{d}(1)}+1−\frac{2K_{d}(1)}{3c^{∘}})\frac{c(1)}{c^{∘}}.
$$

While the asymptotic value $r_{1+V}^{∞}$ does not depend on the length of the VCG oligomers, the threshold VCG concentration at which $r_{1+V}=r_{1+V}^{∞}/2$ scales exponentially with $L_{V}$ (Appendix 4),

$$
c_{V}^{tot}∼exp⁡(−L_{V}|\gamma|).
$$

This scaling implies that longer oligomers require exponentially lower VCG concentration to achieve a given ratio $r_{1+V}$ (Figure 6C), as their greater length allows them to form more stable complexes. This observation implies that pools with longer oligomers will always be more productive than pools with shorter oligomers (at equal VCG concentration).

The behavior becomes more complex in pools containing VCG oligomers of multiple lengths, due to the competitive binding within such heterogeneous pools. To illustrate this, we examine an ensemble containing VCG oligomers ranging from $L_{V}^{min}=3 nt$ to $L_{V}^{max}=9 nt$, along with the same feedstock as previously (reactive monomers and non-reactive dimers, see Figure 7A). For simplicity, we assume that the length distribution of VCG oligomers is uniform. We study the fraction of oligomers in a monomer-extension-competent state as a function of oligomer length,

$$
r_{1+V}(L)=c_{1+V}^{eq}(L)/c(L),
$$

![Figure 7.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig7-v1.jpg)

**Figure 7.:** (A) The pool contains reactive monomers as well as non-reactive dimers and VCG oligomers. The concentrations of monomers and dimers are fixed, $c(1)=0.091mM$ and $c(2)=9.1\muM$, adding up to a total feedstock concentration of $c_{V}^{tot}=0.1mM$, while the total concentration of VCG oligomers, $c_{V}^{tot}$, is varied. All VCG oligomers are assumed to have the same concentration. (B) At low VCG concentration, long oligomers are more likely in a monomer-extension-competent state than short oligomers, whereas at high VCG concentration, the trend reverses and short oligomers are more likely to be extended by monomers (‘productivity inversion’). The threshold concentration at which a short oligomer starts to outperform a longer oligomer depends on the lengths of the compared oligomers (dashed lines). (C) The mechanism underlying productivity inversion can be understood based on the pair-wise competition of different VCG oligomers, for example 8-mers vs. 9-mers. Over the entire range of VCG concentrations, complexes with 8-mer templates have a lower relative equilibrium concentration than complexes with 9-mer templates (bottom two curves vs. top two curves). As the concentration of VCG oligomers is increased, ligations of type $\frac{1|8}{9}$ exceed ligations of type $\frac{1|9}{9}$, that is the fraction of 8-mers that are extended by monomers using a 9-mer as a template exceeds the fraction of extended 9-mers. (D) The equilibrium concentration of free oligomer decreases with increasing $c_{V}^{tot}$. For longer oligomers, the equilibrium fraction of free oligomers is lower, as they can form more stable complexes with longer hybridization sites. (E) Complexes in which 8-mers serve as template are less stable than complexes with 9-mer templates, explaining why complexes with 8-mer templates are more abundant than complexes with 9-mer templates (see panel C). Complexes with 9-mer template have similar stability regardless of the length of the educt oligomer, that is $\frac{1|8}{9}$ and $\frac{1|9}{9}$ are similarly stable. This similar stability, together with the higher concentration of free 8-mers compared to 9-mers (see panel D), is the reason why the fraction of monomer-extended 8-mers exceeds the one of 9-mers (see panel C).

where $c_{1+V}^{eq}(L)$ denotes the equilibrium concentration of all complexes that allow monomer-extension of VCG oligomers of length $L$. At low VCG concentration, longer oligomers are more likely to be extended by monomers than shorter ones (Figure 7B). This behavior is intuitive, as longer oligomers tend to form more stable complexes, which lead to higher productivity. Surprisingly, increasing the VCG concentration reverses the length-dependence of the productivity, such that short oligomers are more likely to be extended by monomers than long ones (note the three crossings of the curves in Figure 7B). For example, 8-mers are more likely to undergo primer extension than 9-mers once the VCG concentration exceeds $≈0.5μM$. We derived a semi-analytical expression for the threshold VCG concentrations at which oligomers of two different lengths have equal productivity (dashed lines in Figure 7B, Appendix 5 and Appendix 6).

To understand the mechanism underlying this inversion of productivity, we analyze how different complex types contribute to $r_{1+V}(L)$. We introduce

$$
r_{1+V}(\frac{1|L_{E}}{L_{T}})=c_{1+V}^{eq}(\frac{1|L_{E}}{L_{T}})/c(L_{E}),
$$

which denotes the fraction of oligomers of length $L_{E}$ that are in a monomer-extension-competent complex configuration that uses an oligomer of length $L_{T}$ as template. The term $c_{1+V}^{eq}(\frac{1|L_{E}}{L_{T}})$ includes the sum over all possible configurations of complexes with the given lengths. Focusing on 8-mers and 9-mers as an example, we observe that complexes utilizing the 9-mer as template are responsible for the inversion of productivity (top two curves in Figure 7C): As the VCG concentration increases, the fraction of monomer-extendable 8-mers eventually surpasses the fraction of monomer-extendable 9-mers, that is $r_{1+V}(\frac{1|8}{9})>r_{1+V}(\frac{1|9}{9})$ (Figure 7C). Two factors give rise to this feature: (i) Ternary complexes of type $\frac{1|8}{9}$ and $\frac{1|9}{9}$ have similar stability (Figure 7E), and (ii) the equilibrium concentration of free 8-mers is higher than that of 9-mers (Figure 7D). As a result, 8-mers are more likely than 9-mers to hybridize to an existing duplex $\frac{1}{9}$, and, given the stability of the complex $\frac{1|8}{9}$, 8-mers remain bound almost as stably as 9-mers. In summary, short oligomers sequester long oligomers as templates to enhance their monomer-extension rate, while long oligomers cannot make use of short oligomers as templates due to the relative instability of the corresponding complexes.

It is noteworthy that Ding et al. have already observed productivity inversion experimentally (Ding et al., 2023). In their study, they included activated monomers, activated imidazolium-bridged dinucleotides and oligomers up to a length of 12 nt and observed that the primer extension rate for short primers is higher than the extension rate of long primers. Even though our model differs from their setup in some aspects (e.g. different circular genome, no bridged dinucleotides), evaluating our model using parameters similar to those of the experimentally studied system predicts productivity inversion that qualitatively agrees with the experimental findings (Appendix 7). We therefore assume that the mechanism underlying productivity inversion described here also applies to the experimental observations.

## Discussion

While significant progress has been made in understanding the prebiotic formation of ribonucleotides (Becker et al., 2016; Benner et al., 2012; Kim et al., 2011; Powner et al., 2009) and characterizing ribozymes that might play a role in an RNA world (Attwater et al., 2018; Mutschler et al., 2015; Pressman et al., 2019; Tjhung et al., 2020), a convincing scenario bridging the gap between prebiotic chemistry and ribozyme-catalyzed replication is still missing. Here, we studied a scenario proposed by Zhou et al., 2021 (the ‘Virtual Circular Genome’, VCG) using theoretical and computational approaches. We analyzed the process whereby template-directed ligation replicates the genomic information that is collectively stored in the VCG oligomers. Our analysis revealed a trade-off between the fidelity and the yield of this process: At low concentration of VCG oligomers, most of the ligations produce oligomers that are too short to specify a unique locus on the genome, resulting in a low yield of replication (Figure 2B-C). At high VCG concentration, erroneous templated ligations cause sequence scrambling and consequently limit the fidelity of replication (Figure 2C-D). We considered two solutions to these issues: (i) a VCG pool composition that optimizes its replication behavior within the bounds of the fidelity-yield trade-off, and (ii) breaking the fidelity-yield trade-off given that error-prone ligations can be kinetically suppressed.

The first solution maximizes the yield of replication for fixed fidelity. In pools containing only monomers and VCG oligomers of a single length, replication efficiency can be maximized by increasing the length of VCG oligomers and decreasing their concentration (Figure 2F-G). This reduces the likelihood of error-prone templated ligation of long oligomers. When the pool contains VCG oligomers of multiple lengths, replication efficiency is typically governed by the longest oligomer in the pool (Figure 4D). Including dimers as feedstock for the replication increases the error fraction (Figure 5B-C), as dimers that bind to a template with a dangling end are prone to form an incorrect product (Figure 5D).

The second solution eliminates the error-prone templated ligation of two VCG oligomers by suppressing them kinetically, for example by assuring that only monomers are chemically activated. This enables both fidelity and yield to remain high at high VCG concentrations (Figure 6B), effectively breaking the fidelity-yield trade-off. Longer VCG oligomers are then more likely to be extended than shorter oligomers at equal concentration (Figure 6C). However, this is only true for pools with VCG oligomers of a single length — once multiple VCG oligomer lengths compete with each other, shorter oligomers can be more productive than longer ones (Figure 7B). This feature, which has also been observed experimentally (Ding et al., 2023), is caused by an asymmetry in the productive interaction between short and long oligomers (Figure 7C): While short oligomers can sequester longer oligomers as templates for their extension by a monomer, short oligomers are unlikely to serve as templates for longer oligomers (Figure 7D-E).

As we intended to study the pathways responsible for sequence scrambling and to explore possible mitigation strategies, we based our analysis on a coarse-grained model that neglects some experimental details. First, we assumed that a complex instantaneously dehybridizes if it contains a non-complementary base pair, whereas in reality, short duplexes can tolerate a limited number of mismatches (Todisco et al., 2024a). While such mismatches can facilitate incorrect hybridization and introduce additional replication errors, we expect this effect to be moderate: Mismatches preferentially occur near the ends of the hybridized region, where their destabilizing effect on binding is weakest (Todisco et al., 2024a). However, such terminal mismatches have also been shown to significantly reduce ligation rates (Rajamani et al., 2010 Leu et al., 2013), which in turn limits the likelihood of forming incorrect products.

Second, we simplified the hybridization dynamics by assuming that all oligomers bind to each other at equal rates, and that dehybridization rates are determined by the hybridization energy computed via a nearest-neighbor model. However, recent work has shown that hybridization to a gap flanked by two oligomers proceeds more slowly than binding to an unoccupied template. Moreover, the resulting nicked complexes (two oligomers hybridized adjacently on a template) are more stable than predicted by standard nearest-neighbor models due to enhanced stacking interactions at the nick site (Todisco et al., 2024b). While this added stability is not expected to affect overall replication efficiency of the VCG (since all productive complexes, correct or incorrect, contain a nick), it can impact the kinetics of the system. In particular, the extended lifetime of such complexes may challenge the adiabatic approximation used in much of our analysis, which assumes ligation is always slower than hybridization and dehybridization.

Third, we do not model the activation chemistry explicitly, but instead assume that all monomers (and, depending on the scenario, also oligomers) are always reactive. As a result, some activated intermediates that are known to form in experiments, such as imidazolium-bridged dinucleotides (Walton and Szostak, 2016), are not modeled. Nonetheless, we include aspects of activation chemistry in a coarse-grained manner. Specifically, to capture the experimentally observed difference in reactivity between monomer incorporation and templated ligation of oligomers under amino-imidazolium activation, we introduce two distinct ligation rate constants. With this approach, we describe the experimental setup well enough to qualitatively reproduce features observed in experiments, for example, the preferential extension of shorter oligomers by monomers in pools containing VCG oligomers of varying lengths (Ding et al., 2023).

The VCG scenario was proposed to close the gap between prebiotic chemistry and ribozyme-catalyzed replication. To this end, VCG pools need to be capable of replicating (parts of) ribozymes that play a role in the emergence of life. While there are cases of small ribozymes (Pressman et al., 2019) or ribozymes with small active sites (e.g. the Hammerhead ribozyme Scott, 2013), ribozymes obtained experimentally via in vitro evolution are often more than a hundred nucleotides long (Attwater et al., 2013; Johnston et al., 2001; Müller and Bartel, 2008; Wochner et al., 2011). Remarkably, our model suggests that the VCG scenario enables high-fidelity replication of long genomes, even in pools containing relatively short VCG oligomers. For a genome of length $L_{G}$, a sequence of at least $L_{U}^{min}=⌈\frac{ln⁡(2L_{G})}{ln⁡4}⌉$ nucleotides is required to uniquely specify a position within the genome. If the oligomers in the pool exceed this length by about three nucleotides, accurate replication becomes feasible (Figure 2H). For example, genomes of length $L_{G}=1000nt$ ($L_{U}^{min}=6,nt$) can be replicated in VCG pools containing $10nt$ oligomers. However, $L_{U}$ equals $L_{U}^{min}$ only for a restricted set of genome sequences; more generally, $L_{U}>L_{U}^{min}$. In such cases, reliable replication requires correspondingly longer oligomers. While the precise margin between oligomer length and $L_{U}$ depends on genome-specific features (particularly the motif distribution at sub-$L_{U}$ scales), it typically amounts to only a few additional nucleotides (Appendix 2).

It is noteworthy that replication in the VCG scenario imposes a selection pressure on prebiotic genomes to reduce their unique motif length, $L_{U}$. A circular genome requiring many nucleotides to specify a unique locus (high $L_{U}$) replicates less efficiently than one with a shorter $L_{U}$, assuming all other properties of the VCG pool (particularly the oligomer length distribution) remain identical. This length distribution arises from the interplay between the chemical kinetics and molecular transport governed by the physical environment. For instance, templated ligation in an open system with continuous oligomer influx and outflux can produce a non-monotonic length distribution, with a concentration peak at a characteristic oligomer length $L_{c}$, determined by the interplay between dehybridization and outflux (Rosenberger et al., 2021). Through this emergent length scale, the environment shapes replication in the VCG scenario. If the environment facilitates long oligomers ($L_{c}>L_{U}$), replication proceeds efficiently. Conversely, in environments with a small $L_{c}$, repeating motifs longer than $L_{c}$ are selected against. In such cases, mutational errors may replace long repeated motifs with functionally equivalent sequences composed of shorter unique motifs, thereby increasing replication efficiency.

Given the broad range of prebiotically plausible non-equilibrium environments (Ianeselli et al., 2023), it is reasonable to expect that some environments provide the required conditions for efficient replication. The constraints formulated in this work can help to guide the search for self-replicating oligomer pools, in the vast space of possible concentration profiles and non-equilibrium environments.

## Methods

### Constructing circular genomes

In the Virtual Circular Genome (VCG) scenario, genomes are encoded in a pool of oligomers. The encoded genomes are assumed to be circular sequences of length $L_{G}$, containing both the original sequence and its reverse complement. Each genome is characterized by two fundamental length scales that reflect different aspects of motif distribution along the sequence. The minimal unique motif length, $L_{U}$, is defined as the shortest subsequence length for which all motifs of length $L\geqL_{U}$ appear at most once in the genome. In contrast, the exhaustive coverage length, $L_{E}$, denotes the largest motif length for which all $4^{L_{E}}$ possible motifs are present within the genome. Since only $2L_{G}$ distinct motifs can be encoded in a genome (including its complement), $L_{E}$ cannot exceed

$$
L_{E}^{max}=⌊\frac{ln⁡(2L_{G})}{ln⁡4}⌋.
$$

Similarly, for a motif to be uniquely addressable on the genome, its length must be at least

$$
L_{U}^{min}=⌈\frac{ln⁡(2L_{G})}{ln⁡4}⌉.
$$

We note that $L_{E}^{max}$ and $L_{U}^{min}$ are essentially the same length scale (differing by at most one nucleotide).

The characteristic length scales $L_{E}$ and $L_{U}$ impose constraints on how motifs are distributed. For example, when $L=L_{U}$, all motifs of length $L$ must appear at most once, while at least one motif of length $L−1$ must occur more than once. To quantify the motif distribution, we introduce the motif entropy,

$$
S(L)=−\sumi=14^{L}f_{i}lnf_{i},
$$

where $f_{i}$ denotes the relative frequency of motif $i$ across the genome and its reverse complement. Motif entropy ranges from zero (a homogeneous sequence with only one motif) to a maximum value that depends on the subsequence length,

$$
S^{max}(L)={LifL\leqL_{G},\frac{ln⁡(2L_{G})}{ln⁡4}ifL>L_{G}.
$$

For motif length $L$ to qualify as the unique motif length $L_{U}$, its entropy must be maximal, $S(L)=S^{max}(L)$, while $S(L−1)$ must be smaller than its respective maximum, $S(L−1)<S^{max}(L−1)$.

The correspondence between characteristic length scales and motif entropies provides a way to construct genome sequences with specified motif characteristics. By treating the entropy function as an effective ‘Hamiltonian’ $H$, we can generate genome sequences through Metropolis–Hastings sampling. In our implementation, each update step in the Metropolis-Hastings algorithm involves either a single-nucleotide mutation or a cut-and-paste operation that relocates a segment of the genome to a new position (the cut-and-paste operation is 10 times more likely than the single nucleotide mutation). The acceptance criterion follows the standard Metropolis rule: modifications that reduce the Hamiltonian are always accepted, while increases in ‘energy’ are accepted with probability $exp⁡[−\beta(E_{old}−E_{new})]$. Here, $\beta^{−1}$ is an effective temperature chosen to be small compared to the typical energy to ensure convergence to the minimum. Simulations are either run until a predefined entropy target is reached or until the energy converges to a plateau.

To generate genomes with $L_{E}=L_{E}^{max}$ and $L_{U}=L_{U}^{min}$, we minimize the Hamiltonian

$$
H=−S(L_{E})−S(L_{U})
$$

Starting from a random sequence, we perform 10,000 Metropolis–Hastings steps at an inverse temperature $\beta=10^{−5}$ to construct genome sequences of lengths $L_{G}=16nt$ (listed in Results) and $L_{G}=64nt$ (listed in Supplementary file 1). To explore genomes with $L_{E}<L_{E}^{max}$ and $L_{U}>L_{U}^{min}$, we initialize the algorithm from the maximally diverse genomes ($L_{E}=L_{E}^{max}$, $L_{U}=L_{U}^{min}$) and then reduce entropy across the range $L_{E}<L<L_{U}$. This is done by minimizing the Hamiltonian

$$
H=\sumL=L_{E}L_{U}S(L),
$$

via two different sampling protocols. In the first protocol, the simulation is terminated as soon as the genome reaches the desired values of $L_{E}$ and $L_{U}$. The resulting motif distributions on the intermediate length scales ($L_{E}<L<L_{U}$) remain close to uniform, with only minor biases sufficient to enforce the length-scale constraints. In the second protocol, entropy minimization continues beyond the point at which the target values are achieved, leading to more strongly biased motif distributions on intermediate length scales. These construction strategies allow us to systematically tune genome complexity and motif structure, enabling controlled investigations of how the characteristic length scales influence replication dynamics (see Appendix 2 for details).

### Computing replication observables based on the kinetic simulation

We simulate the dynamics of VCG pools using a kinetic simulation that is based on the Gillespie algorithm. In the simulation, oligomers can hybridize to each other to form complexes or dehybridize from an existing complex. Moreover, two oligomers can undergo templated ligation if they are hybridized adjacent to each other on a third oligomer. At each time $t$, the state of the system is determined by a list of all single-stranded oligomers and complexes as well as their respective copy number. We refer to the state of the system at the time $t$ as the ensemble of compounds $E_{t}$. Given the copy numbers, the rates $r_{i}$ of all possible chemical reactions $i\inI$ can be computed. To evolve the system in time, we need to perform two steps: (i) We sample the waiting time until the next reaction, $\tau$, from an exponential distribution with mean $(\sumi\inIr_{i})^{−1}$, and update the simulation time, $t→t+\tau$. (ii) We pick which reaction to perform by sampling from a categorical distribution. Here, the probability to pick reaction $i$ equals $r_{i}/(\sumi\inIr_{i})$. The copy numbers are updated according to the sampled reaction, yielding $E_{t+\tau}$. Steps (i) and (ii) are repeated until the simulation time $t$ reaches the desired final time, $t_{final}$. A more detailed explanation of the kinetic simulation is presented in Göppel et al., 2022; Rosenberger et al., 2021.

Our goal is to compute observables characterizing replication in the VCG scenario based on the full kinetic simulation. In the following derivation, we focus on one particular observable (yield) for clarity. The results for other observables are stated directly, as their derivations follow analogously. Recall the definition of the yield introduced in the Results section,

$$
y=\frac{#nucleotidesincorporatedinVCGoligomersuntil\tau_{lig}}{#incorporatednucleotidesuntil\tau_{lig}}.
$$

As we are interested in the initial replication performance of the VCG, we compute the yield based on the ligation events that take place until the characteristic timescale of ligations $\tau_{lig}=k_{lig}^{−1}≈10^{12} t_{0}$. In principle, we would like to compute the yield based on the templated ligation events that we observe in the simulation. Unfortunately, for reasonable system parameters, it is impossible to simulate the system long enough to observe sufficiently many ligation events to compute $y$ to reasonable accuracy. For example, for a VCG pool containing monomers at a total concentration of $c_{F}^{tot }=0.1mM$ and VCG oligomers of length $L=8nt$ at a total concentration of $c_{V}^{tot}=1μM$, it would take about 1700 hr of simulation time to reach $t=5⋅10^{12}t_{0}$ (Figure 8). Multiple such runs would be needed to estimate the mean and the variance of the observables of interest, rendering this approach unfeasible.

![Figure 8.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig8-v1.jpg)

**Figure 8.:** Simulation runtime of the full kinetic simulation for a VCG pool that includes monomers and VCG oligomers of length $L=8$.The total concentration of feedstock monomers equals $c_{F}^{tot}=0.1mM$, while the total concentration of VCG oligomers is $c_{V}^{tot}=1\muM$. The energy contribution per matching nearest-neighbor block is set to $\gamma=−2.5 k_{B}T$. The volume of the system is varied, and the time evolution is simulated until $t=5.0⋅10^{7}t_{0}$. The runtime of the simulation scales linearly with the volume of the system.

Instead, we compute the replication observables based on the copy number of complexes that could potentially perform a templated ligation, that is complexes in which two strands are hybridized adjacent to each other, such that they could form a covalent bond. We can show analytically that the number of productive complexes is a good approximation for the number of incorporated nucleotides: The number of incorporated nucleotides can be computed as the integral over the ligation flux, weighted by the number of nucleotides that are added in each templated ligation reaction,

$$
(#incorporatednucleotidesuntil \tau_{lig})=\int_{0}^{\tau_{lig}}dt \sumC\inE_{t}N(C)min(L_{e,1},L_{e,2})1(C allows templated ligation).
$$

Here, $N(C)$ denotes the copy number of the complex C in the pool $E_{t}$. $L_{e,1}$ and $L_{e,2}$ denote the lengths of the oligomers that undergo ligation, and $1$ is an indicator function which enforces that only complexes in a ligation-competent configuration contribute to the reaction flux. As only a few ligation events are expected to happen until $\tau_{lig}$, it is reasonable to assume that the ensembles $E_{t}$ do not change significantly during $t\in[0,\tau_{lig}]$. Therefore, the integration over time may be interpreted as a multiplication by $\tau_{lig}$,

$$
(#incorporatednucleotidesuntil \tau_{lig})≈\tau_{lig}⟨\sumC\inEN(C)min(L_{e,1},L_{e,2})1(C allows templated ligation)⟩,
$$

where $⟨…⟩$ denotes the average over realizations of the ensembles $E_{t}$ within the time interval $t\in[\tau_{eq},\tau_{lig}]$. This average corresponds to the average number of complexes in a ligation-competent configuration. Note that, at this point, we made the additional assumption that no templated ligations are taking place between $[0,\tau_{eq}]$. This assumption is reasonable, as (i) the equilibration process is very short compared to the characteristic timescale of ligation, and (ii) the number of complexes that might allow for templated ligation during equilibration is lower than in equilibrium (we start the simulation with an ensemble of single-stranded oligomers). Both aspects imply that the rate of templated ligation is negligible during the interval $[0,\tau_{eq}]$.

In order to compute the average over different realizations of ensembles $E$ (as required in Equation 6), we need to sample a set of uncorrelated ensembles that have reached the hybridization equilibrium, which can be done using the full kinetic simulation. The simulation starts with a pool containing only single-stranded oligomers and reaches the (de)hybridization equilibrium after a time $\tau_{eq}$. We identify this timescale of equilibration by fitting an exponential function to the total hybridization energy of all complexes in the system, $ΔG_{tot}$ (Figure 9A). In the set of ensembles used to evaluate the average in Equation 6, we only include ensembles for time $t>\tau_{eq}$ to ensure that the ensembles have reached (de)hybridization equilibrium. To ensure that the ensembles are uncorrelated, we require that the time between two ensembles that contribute to the average is at least $\tau_{corr}$. The correlation time, $\tau_{corr}$, is determined via an exponential fit to the autocorrelation function of $ΔG_{tot}$ (Figure 9B). Besides computing the expectation value (Equation 6), we are also interested in the ‘uncertainty’ of this expectation value, that is in the standard deviation of the sample mean $\sigma_{⟨X⟩}$. (We use $X$ as a short-hand notation for $\sumC\inEN(C)min(L_{e,1},L_{e,2})1(Callowstemplatedligation)$). The standard deviation of the sample mean, $\sigma_{⟨X⟩}$, is related to the standard deviation of $X$, $\sigma_{X}$, by the number of samples, $\sigma_{⟨X⟩}=(N_{s})^{−1/2}\sigma_{X}$. Moreover, based on the van-Kampen system size expansion, we expect the standard deviation of $X$ to be proportional to $V^{−1/2}$, such that $\sigma_{⟨X⟩}∝(N_{s}V)^{−1/2}$.

![Figure 9.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig9-v1.jpg)

**Figure 9.:** (A) The equilibration timescale is determined based on the total hybridization energy of all strands in the pool, $ΔG_{tot}$. By fitting an exponential function to $ΔG_{tot}$, we obtain a characteristic timescale $\tau^{∗}$ (vertical dotted line), which is then used to calculate the equilibration time as $\tau_{eq}=5\tau^{∗}$ (vertical dashed line). The horizontal dashed line shows the total hybridization energy expected in (de)hybridization equilibrium according to the coarse-grained adiabatic approach (Methods). (B) The correlation timescale is determined based on the autocorrelation of $ΔG_{tot}$. We obtain $\tau_{corr}$ (vertical dashed line) by fitting an exponential function to the autocorrelation. In both panels, we show simulation data obtained for a VCG pool containing monomers and VCG oligomers with a concentration of $c_{F}^{tot}=0.1mM$ as well as oligomers of length $L=8 nt$ with a concentration of $c_{V}^{tot}=1\muM$.

Using Equation 6 (as well as an analogous expression for the number of nucleotides that are incorporated in VCG oligomers), the yield can be expressed as

$$
y=\frac{⟨\sumC\inEN(C)min(L_{e,1},L_{e,2})1(Callowstemplatedligation)1(L_{e,1}+L_{e,2}\geqL_{U})⟩}{⟨\sumC\inEN(C)min(L_{e,1},L_{e,2})1(Callowstemplatedligation)⟩}.
$$

The additional condition $1(L_{e,1}+L_{e,2}\geqL_{U})$ in the numerator ensures that the product oligomer is long enough to be counted as a VCG oligomer, that is at least $L_{U}$ nucleotides long. Analogously, the expression for the fidelity of replication reads

$$
f=\frac{⟨\sumC\inEN(C)min(L_{e,1},L_{e,2})1(C allows templated ligation)1(L_{e,1}+L_{e,2}\geqL_{U})1(product correct)⟩}{⟨\sumC\inEN(C)min(L_{e,1},L_{e,2})1(C allows templated ligation)1(L_{e,1}+L_{e,2}\geqL_{U})⟩}.
$$

Multiplying fidelity and yield results in the efficiency of replication,

$$
η=\frac{⟨\sumC\inEN(C)min(L_{e,1},L_{e,2})1(Callowstemplatedligation)1(L_{e,1}+L_{e,2}\geqL_{U})1(product correct)⟩}{⟨\sumC\inEN(C)min(L_{e,1},L_{e,2})1(Callowstemplatedligation)⟩}.
$$

The ligation share of a particular type of templated ligation $s(type)$, that is, the relative contribution of this templated-ligation type to the nucleotide extension flux, can be represented in a similar form as the other observables,

$$
s(type)=\frac{⟨\sumC\inEN(C)min(L_{e,1},L_{e,2})1(C allows templated ligation of given type)⟩}{⟨\sumC\inEN(C)min(L_{e,1},L_{e,2})1(C allows templated ligation)⟩}.
$$

As all observables are expressed as the ratio of two expectation values, $Z=⟨X⟩/⟨Y⟩$, we can compute the uncertainty of the observables via Gaussian error propagation,

$$
\sigma_{Z}=\sqrt{\frac{\sigma_{⟨X⟩}^{2}}{⟨Y⟩^{2}}+\frac{⟨X⟩^{2} \sigma_{⟨Y⟩}^{2}}{⟨Y⟩^{4}}−\frac{2⟨X⟩ \sigma_{⟨X⟩,⟨Y⟩}^{2}}{⟨Y⟩^{3}} }.
$$

Since the variances, $\sigma_{⟨X⟩}^{2}$ and $\sigma_{⟨Y⟩}^{2}$, as well as the covariance, $\sigma_{⟨X⟩,⟨Y⟩}^{2}$, are proportional to $(N_{s}V)^{−1}$, the standard deviation of the observable mean, $\sigma_{Z}$, scales with the inverse square root of the number of samples and the system volume, that is $\sigma_{Z}∝(N_{s}V)^{−1/2}$. Therefore, the variance of the computed observable can be reduced by either increasing the system volume or increasing the number of samples used for averaging. Both approaches incur the same computational cost: (i) Increasing the number of samples, $N_{s}$, requires running the simulation for a longer duration, with the additional runtime scaling linearly with the number of samples. (ii) Similarly, the additional runtime needed due to increased system volume, $V$, also scales linearly with $V$ (Figure 8). One update step in the simulation always takes roughly the same amount of runtime, but the change in simulation time per update step depends on the total rate of all reactions in the system. The total rate is dominated by the association reactions, and their rate is proportional to the volume. Therefore, the change in simulation time per update step is proportional to $V^{−1}$. The runtime, which is necessary to reach the same simulation time in a system with volume $V$ as in a system with volume 1, is a factor of $V$ longer in the larger system. With this in mind, it makes no difference whether the variance is reduced by increasing the volume or the number of samples. For practical reasons (post-processing of the simulations is less memory- and time-consuming), we opt to choose a moderate number of samples, but slightly higher system volumes to compute the observables of interest. The simulation parameters (length of oligomers, concentrations, hybridization energy, volume, number of samples, characteristic timescales) used to obtain the results presented in Figure 2 are summarized in Table 1.

**Table 1.**
 Input parameters and resulting observables (yield and efficiency) from the full kinetic simulation of replication in pools containing monomers and VCG oligomers of a single length $L_{V}$ . The observables (yield and efficiency) listed in this table are shown in Figure 2.


<table>
  <thead>
    <tr>
      <th>VCG oligo. length</th>
      <th>conc. ratio cVtot/cFtot\begin{document}$c^{\rm tot}_{\rm V} / c^{\rm tot}_{\rm F}$\end{document}</th>
      <th>volume</th>
      <th>equilibration time</th>
      <th>correlation time</th>
      <th>number of samples</th>
      <th>yield y\begin{document}$y$\end{document}</th>
      <th>efficiency η\begin{document}$\eta$\end{document}</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>6</td>
      <td>1.0 ⋅ 10−4</td>
      <td>5.0 ⋅ 104</td>
      <td>3.4 ⋅ 106</td>
      <td>1.9 ⋅ 106</td>
      <td>3805</td>
      <td>0.04 ± 0.01</td>
      <td>0.04 ± 0.01</td>
    </tr>
    <tr>
      <td>6</td>
      <td>1.0 ⋅ 10−3</td>
      <td>5.0 ⋅ 103</td>
      <td>1.2 ⋅ 107</td>
      <td>2.6 ⋅ 106</td>
      <td>3264</td>
      <td>0.38 ± 0.02</td>
      <td>0.36 ± 0.02</td>
    </tr>
    <tr>
      <td>6</td>
      <td>3.3 ⋅ 10−3</td>
      <td>8.0 ⋅ 102</td>
      <td>1.3 ⋅ 107</td>
      <td>2.7 ⋅ 106</td>
      <td>5400</td>
      <td>0.68 ± 0.02</td>
      <td>0.64 ± 0.02</td>
    </tr>
    <tr>
      <td>6</td>
      <td>1.0 ⋅ 10−2</td>
      <td>9.1 ⋅ 101</td>
      <td>1.4 ⋅ 107</td>
      <td>2.7 ⋅ 106</td>
      <td>5440</td>
      <td>0.87 ± 0.01</td>
      <td>0.77 ± 0.03</td>
    </tr>
    <tr>
      <td>6</td>
      <td>3.3 ⋅ 10−2</td>
      <td>9.1 ⋅ 100</td>
      <td>1.3 ⋅ 107</td>
      <td>2.4 ⋅ 106</td>
      <td>6170</td>
      <td>0.96 ± 0.01</td>
      <td>0.63 ± 0.03</td>
    </tr>
    <tr>
      <td>7</td>
      <td>1.0 ⋅ 10−4</td>
      <td>3.9 ⋅ 104</td>
      <td>1.7 ⋅ 108</td>
      <td>2.6 ⋅ 107</td>
      <td>784</td>
      <td>0.33 ± 0.05</td>
      <td>0.33 ± 0.05</td>
    </tr>
    <tr>
      <td>7</td>
      <td>1.0 ⋅ 10−3</td>
      <td>7.6 ⋅ 102</td>
      <td>1.9 ⋅ 108</td>
      <td>4.0 ⋅ 107</td>
      <td>2041</td>
      <td>0.87 ± 0.02</td>
      <td>0.81 ± 0.05</td>
    </tr>
    <tr>
      <td>7</td>
      <td>3.3 ⋅ 10−3</td>
      <td>7.7 ⋅ 101</td>
      <td>1.9 ⋅ 108</td>
      <td>3.3 ⋅ 107</td>
      <td>2980</td>
      <td>0.95 ± 0.01</td>
      <td>0.87 ± 0.04</td>
    </tr>
    <tr>
      <td>7</td>
      <td>1.0 ⋅ 10−2</td>
      <td>1.1 ⋅ 101</td>
      <td>1.9 ⋅ 108</td>
      <td>2.6 ⋅ 107</td>
      <td>3465</td>
      <td>0.99 ± 0.01</td>
      <td>0.81 ± 0.05</td>
    </tr>
    <tr>
      <td>7</td>
      <td>3.3 ⋅ 10−2</td>
      <td>1.7 ⋅ 100</td>
      <td>1.9 ⋅ 108</td>
      <td>3.1 ⋅ 107</td>
      <td>3235</td>
      <td>0.99 ± 0.04</td>
      <td>0.73 ± 0.05</td>
    </tr>
    <tr>
      <td>8</td>
      <td>1.0 ⋅ 10−4</td>
      <td>6.3 ⋅ 103</td>
      <td>2.5 ⋅ 109</td>
      <td>1.1 ⋅ 108</td>
      <td>466</td>
      <td>0.81 ± 0.05</td>
      <td>0.81 ± 0.05</td>
    </tr>
    <tr>
      <td>8</td>
      <td>1.0 ⋅ 10−3</td>
      <td>9.9 ⋅ 101</td>
      <td>1.9 ⋅ 109</td>
      <td>3.6 ⋅ 108</td>
      <td>615</td>
      <td>0.99 ± 0.01</td>
      <td>0.99 ± 0.01</td>
    </tr>
    <tr>
      <td>8</td>
      <td>3.3 . 10-3</td>
      <td>1.6 ⋅ 101</td>
      <td>1.0 ⋅ 109</td>
      <td>2.2 ⋅ 108</td>
      <td>1100</td>
      <td>0.95 ± 0.03</td>
      <td>0.95 ± 0.03</td>
    </tr>
    <tr>
      <td>8</td>
      <td>1.0 . 10-2</td>
      <td>3.8 ⋅ 100</td>
      <td>5.6 ⋅ 108</td>
      <td>1.4 ⋅ 108</td>
      <td>1700</td>
      <td>1.00 ± 0.01</td>
      <td>0.93 ± 0.05</td>
    </tr>
    <tr>
      <td>8</td>
      <td>3.3 . 10-2</td>
      <td>0.9 ⋅ 100</td>
      <td>4.9 ⋅ 108</td>
      <td>7.4 ⋅ 107</td>
      <td>3195</td>
      <td>1.00 ± 0.03</td>
      <td>0.82 ± 0.05</td>
    </tr>
  </tbody>
</table>

### Coarse-grained representation of complexes in the adiabatic approach

To characterize the replication performance of VCG pools across a broad range of system parameters, we developed an adiabatic approach that enables faster computation of replication observables than full kinetic simulations. In this method, we compute the equilibrium concentrations of complexes in productive configurations under the assumption that templated ligation is much slower than (de)hybridization. The approach relies on a coarse-grained representation of the oligomers in the pool, which we introduce in this section.

#### Single strands

In the coarse-grained description, oligomers of identical length are assumed to have equal concentration, irrespective of their sequence. This assumption is justified for two reasons: (i) We initialize the VCG pool without sequence bias, that is all oligomers compatible with the genome sequence are included at equal concentration. (ii) Hybridization energy in our simplified energy model (and therefore also the stability of complexes) only depends on the length of the hybridization site, not on its sequence, such that oligomers of equal length have similar probabilities of being free or bound in complexes. Under this assumption, each coarse-grained oligomer is uniquely identified by its length $L$, and it represents a group of oligomers with $C(L)$ distinct sequences. We refer to the number $C(L)$ as the combinatorial multiplicity of the coarse-grained oligomer. The value of $C(L)$ depends on the choice of the encoded genome. We assume that by construction, all possible oligomer sequences of length $L\leqL_{E}^{max}$ are included in the genome (see Methods for the definition of $L_{E}^{max}$ and $L_{U}^{min}$). For $L\geqL_{U}^{min}=L_{E}^{max}+1$, only a subset of all possible $4^{L}$ sequences is included, but no sequence is repeated multiple times across the genome. Therefore, the combinatorial multiplicity equals

$$
C(L)={4^{L}if L<L_{U}^{min},2L_{G}if L\geqL_{U}^{min}.
$$

#### Duplexes

Two strands can form a duplex by hybridizing to each other. We refer to the bottom oligomer as ‘Crick’ strand C and to the top oligomer as ‘Watson’ strand W. A duplex is uniquely characterized by the lengths of the oligomers, $L_{C}$ and $L_{W}$, as well as their relative alignment (Figure 10A). The alignment index $i$ denotes the position of the Watson strand with respect to the Crick strand. As there needs to be at least one nucleotide of overlap between the strands for a duplex to exist, the alignment index needs to be in the interval $i\in[−(L_{W}−1),L_{C}−1]$. Using the alignment index, we can also determine if the duplex has a left (or right) dangling end. The corresponding indicator variables are called $d_{l}$ (or $d_{r}$),

$$
d_{l}={1ifi=0,0otherwise,d_{r}={1ifi+L_{W}=L_{C},0otherwise.
$$

![Figure 10.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig10-v1.jpg)

**Figure 10.:** (A) A duplex is comprised of two strands, which we refer to as W (Watson) and C (Crick) strands. The relative position of the strands is characterized by the alignment index $i$; for the depicted duplex, $i=−2$. The length of the hybridization region is called $L_{o}$. (B) A ternary complex contains three strands. By convention, we denote the two strands that are on the same ‘side’' of the complex as W1 and W2, and the complementary strand as C. The alignment indices $i$ and $j$ denote the positions of W1 and W2 relative to C. For the depicted complex, $i=−2$ and $j=3$. The length of the hybridization regions is called $L_{o,1}$ and $L_{o,2}$.

Moreover, the length of the hybridization region $L_{o}$ can be computed via

$$
L_{o}=min(L_{C},i+L_{W})−max(i,0).
$$

The hybridization energy of the duplex depends on the length of the hybridization region as well as on the existence/absence of dangling ends. For a hybridization site of length $L_{o}$, there are $L_{o}−1$ nearest-neighbor energy blocks each of which contributes $\gamma$ to the energy. Moreover, each dangling end contributes $\frac{\gamma}{2}$ to the energy,

$$
E=\gamma(L_{o}−1)+\frac{\gamma}{2}(d_{l}+d_{r}).
$$

To compute the combinatorial multiplicity for a duplex with fixed $L_{C}$, $L_{W}$ and alignment index $i$, we need to multiply the combinatorial multiplicity of the Crick strand by the number of possible hybridization partners. We assume that a hybridization partner is possible if its sequence is perfectly complementary to the lower strand within the hybridization region, whereas hybridization partners with mismatches are not accounted for. This is sensible as long as the energetic penalty for mismatches in the full kinetic simulation is sufficiently large to suppress mismatches. The number of possible hybridization partners is determined by the length of the overlap region $L_{o}$: If $L_{o}\geqL_{U}^{min}$, the pool contains only one oligomer sequence that can act as hybridization partner by construction of the genome. For shorter hybridization regions, multiple hybridization partners might be possible. Their number is set by the combinatorial multiplicity of the Watson oligomer divided by the combinatorial multiplicity of the hybridization region,

$$
C(L_{C},L_{W},i)={\frac{C(L_{C})C(L_{W})}{4^{L_{o}}}  if L_{o}<L_{U}^{min},C(L_{C})if L_{o}\geqL_{U}^{min}.
$$

To avoid double-counting, we only account for complexes in which the Crick strand is at least as long as the Watson strand, $L_{C}\geqL_{W}$, and multiply $C(L_{W},L_{C},i)$ by $1/2$ if $L_{W}=L_{C}$.

#### Ternary complexes

Ternary complexes, that is complexes comprised of three strands, are uniquely characterized by the length of the three oligomers, $L_{C},L_{W,1},L_{W,2}$, as well as their respective alignment (Figure 10B). The alignment index $i$ denotes the position of strand W1 relative to strand C. Analogously, $j$ denotes the relative position of W2 relative to oligomer C. Two strands that are hybridized to each other need to have a hybridization region of at least one nucleotide. Moreover, the strands W1 and W2 must not occupy the same position on the template strand C. Taking both requirements together, the alignment indices fall within the intervals,

$$
i\in[−(L_{W,1}−1), L_{C}−L_{W,1}−1],   and   j\in[i+L_{W,1}, L_{C}−1].
$$

A ternary complex may have a dangling end not only on its left or right end, but also in the gap between strands W1 and W2. Three boolean variables are necessary to denote the presence/absence of the respective dangling ends,

$$
d_{l}={0if i=0,1otherwise,d_{m}={0if i+L_{W,1}=j,1otherwise,d_{r}={0if j+L_{W,2}=L_{C},1otherwise.
$$

The length of the two hybridization regions is given by

$$
L_{o,1}=i+L_{W,1}−max(i,0),   and   L_{o,2}=min(j+L_{W,2},L_{C})−j.
$$

The hybridization energy depends on the length of the overlap regions as well as on the existence of dangling ends: As in the duplex, each overlap region of length $L_{o,1}$ (or $L_{o,2}$) comprises $L_{o,1}−1$ (or $L_{o,2}−1$) nearest neighbor blocks, each of which contributes $\gamma$ to the total energy. Moreover, every dangling end contributes $\gamma/2$. Note that the presence of a gap between strands W1 and W2, that is $d_{m}=1$, implies that there are two dangling ends, one for W1 and another for W2. Gaps in between two complexes contribute $\gamma/2$ per each dangling end, adding up to $\gamma$. If there is no gap between the strands, that is $d_{m}=0$, there are no dangling end contributions, but a new full nearest neighbor block emerges, which contributes $\gamma$ to the energy. Therefore, the total energy reads,

$$
E=\gamma(L_{o,1}+L_{o,2}−2)+\frac{\gamma}{2}(d_{l}+d_{r}+2d_{m})+\gamma(1−d_{m}).
$$

The combinatorial multiplicity of a ternary complex is computed in the same way as for the duplex: The combinatorial multiplicity of the strand C is multiplied by the number of possible hybridization partners W1 and W2. Again, the number of possible partners is set by the length of the hybridization regions,

$$
C(L_{C},L_{W,1},L_{W,2},i,j)=C(L_{C})\times[\frac{C(L_{W,1})}{4^{L_{o,1}}}1(L_{o,1}<L_{U}^{min})+1(L_{o,1}\geqL_{U}^{min})]\times[\frac{C(L_{W,2})}{4^{L_{o,2}}}1(L_{o,2}<L_{U}^{min})+1(L_{o,2}\geqL_{U}^{min})].
$$

We use $1$ to denote the indicator function which returns 1 in case the condition in the bracket is fulfilled and zero otherwise. As all ternary complexes are asymmetric, there is no need to introduce a symmetry correction factor.

#### Quaternary complexes

The largest complexes to be accounted for in our coarse-grained adiabatic approach are quaternary complexes, that is complexes comprised of four strands. We need to distinguish three types of such complexes: (i) 3-1 quaternary complexes, (ii) left-tilted 2-2 quaternary complexes, and (iii) right-tilted 2-2 quaternary complexes. In 3-1 quaternary complexes, three Watson strands are hybridized to one Crick strand (Figure 11), whereas in 2-2 quaternary complexes, two Watson strands are hybridized to two Crick strands (Figure 12 and Figure 13).

![Figure 11.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig11-v1.jpg)

**Figure 11.:** Three strands (referred to as Watson strands W1, W2, and W3) hybridize to a single template strand (Crick strand C). The positions relative to the left end of the C strand are given by the alignment indices $i,j$, and $k$; here, $i=−2,j=2,k=5$. The length of the overlap regions is denoted as $L_{o,1},L_{o,2}$, and $L_{o,3}$.

![Figure 12.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig12-v1.jpg)

**Figure 12.:** (A) Two Watson strands (W1 and W2) are hybridized to two Crick strands (C1 and C2). Both Watson strands are hybridized to the left Crick strand C1, whereas only W2 is hybridized to the right Crick strand C2. The alignment indices $i,j$ and $k$ denote the position of the strands relative to the left end of C1; here, $i=−2$, $j=3$ and $k=6$. The length of the hybridization regions is called $L_{o,1}$, $L_{o,2}$, and $L_{o,3}$. (B) Rotating the schematic representation of a left-tilted 2-2 quaternary complex by $180^{∘}$ produces an alternative representation of the same complex, which is again a left-tilted 2-2 complex. The panel depicts the rotated complex representation (variables with superscript ‘rot’) as well as the non-rotated representation (variables without superscript). There is a unique linear mapping between non-rotated and rotated representation, for example C2 after rotation always corresponds to W1 before rotation.

![Figure 13.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig13-v1.jpg)

**Figure 13.:** (A) Two Watson strands (W1 and W2) are hybridized to two Crick strands (C1 and C2). Unlike in the left-tilted 2-2 quaternary complex, both Watson strands are hybridized to the right Crick strand C2, whereas only W1 is hybridized to the left Crick strand C1. The alignment indices $i,j$, and $k$ denote the positions of the strands relative to C1; here, $i=1$, $k=3$, and $j=6$. The length of the overlap regions is called $L_{o,1},L_{o,2}$ and $L_{o,3}$. (B) Rotating the schematic representation of a right-tilted 2-2 quaternary complex by $180^{∘}$ produces an alternative representation of the same complex, which is again a right-tilted 2–2 complex. The panel depicts the rotated complex representation (variables with superscript ‘rot’) as well as the non-rotated representation (variables without superscript). There is a unique linear mapping between non-rotated and rotated representation, for example C2 after rotation always corresponds to W1 before rotation. The mapping is identical for left- and right-tilted 2–2 quaternary complexes.

##### 3-1 Quaternary complexes

Figure 11 depicts a typical 3-1 quaternary complex. Such a complex is uniquely characterized by the length of its oligomers, $L_{C},L_{W,1},L_{W,2},L_{W,3}$, as well as their relative position to each other denoted by the alignment indices $i,j$, and $k$. All positions within the ternary complex are measured relative to the left end of the C strand. Any W strand needs to have at least one nucleotide of overlap with the C strand, but two W strands must never occupy the same position on the C strand. Consequently, the alignment indices fall within the intervals,

$$
i\in[−(L_{W,1}−1),L_{C}−L_{W,1}−L_{W,2}−1],    j\in[i+L_{W,1},L_{C}−L_{W,2}−1],   and   k\in[j+L_{W,2},L_{C}−1].
$$

There are two dangling ends (left and right) and potentially two gaps between the W strands: one gap between W1 and W2 and another one between W2 and W3. The following boolean variables indicate the presence/absence of the respective dangling ends,

$$
d_{l}={0if i=0,1otherwise,   d_{m1}={0if i+L_{W,1}=j,1otherwise,d_{m2}={0if i+L_{W,2}=k,1otherwise,  d_{r}={0if k+L_{W,3}=L_{C},1otherwise.
$$

The length of the hybridization regions is given by

$$
L_{o,1}=i+L_{W,1}−max(i,0),    L_{o,2}=L_{W,2},   and   L_{o,3}=min(L_{C},k+L_{W,3})−k.
$$

Following the same reasoning as in the case of ternary complexes, the energy equals

$$
E=\gamma(L_{o,1}+L_{o,2}+L_{o,3}−3)+\gamma(1−d_{m1})+\gamma(1−d_{m2})+\frac{\gamma}{2}(d_{l}+d_{r}+2d_{m1}+2d_{m2}).
$$

Similarly, the combinatorial multiplicity of 3-1 quaternary complexes is constructed using the same reasoning as in the case of ternary complexes,

$$
C(L_{C},L_{W,1},L_{W,2},L_{W,3},i,j,k)=C(L_{C})\times[\frac{C(L_{W,1})}{4^{L_{o,1}}}1(L_{o,1}<L_{U}^{min})+1(L_{o,1}\geqL_{U}^{min})]\times[\frac{C(L_{W,2})}{4^{L_{o,2}}}1(L_{o,2}<L_{U}^{min})+1(L_{o,2}\geqL_{U}^{min})]\times[\frac{C(L_{W,3})}{4^{L_{o,3}}}1(L_{o,3}<L_{U}^{min})+1(L_{o,3}\geqL_{U}^{min})].
$$

As 3-1 quaternary complexes are not symmetric under rotation, no symmetry correction of the combinatorial multiplicity is necessary.

##### Left-tilted 2-2 quaternary complexes

A 2-2 quaternary complex is comprised of two C strands and two W strands. We call a 2-2 complex left-tilted if strand W1 is connected to strand W2 via strand C1 (Figure 12A). The lengths of the oligomers are called $L_{W,1},L_{W,2},L_{C,1}$, and $L_{C,2}$. The positions of the strands relative to each other are governed by the alignment indices. All positions are measured relative to the position of the left end of strand C1. The alignment indices may take on the following values,

$$
i\in[−(L_{W,1}−1),L_{C,1}−L_{W,1}−1],    j\in[i+L_{W,1},L_{C,1}],   and   k\in[L_{C,2},j+L_{W,2}−1].
$$

The complex can have dangling ends on the right and on the left end of the complex; the presence of these dangling ends is indicated by the boolean variables $d_{l}$ and $d_{r}$. Moreover, two gaps are possible: There might be a gap between strands W1 and W2, or a gap between C1 and C2. The respective boolean variables read

$$
d_{l}={0if i=0,1otherwise,d_{m1}={0if i+L_{W,1}=j,1otherwise,d_{m2}={0if L_{C,1}=k,1otherwise,d_{r}={0if j+L_{W,2}=k+L_{C,2},1otherwise.
$$

We refer to the hybridization region of strand W1 and C1 as overlap region 1, to the hybridization region of strand W2 and C1 as overlap region 2 and to the hybridization region of strand W2 and C2 as overlap region 3. The length of these hybridization regions is computed via

$$
L_{o,1}=i+L_{W,1}−max(i,0),    L_{o,2}=L_{C,1}−j,   and   L_{o,3}=min(j+L_{W,2},k+L_{C,2})−k.
$$

Given the length of the hybridization region as well as the presence/absence of dangling ends, we can compute the hybridization energy,

$$
E=\gamma(L_{o,1}+L_{o,2}+L_{o,3}−3)+\gamma(1−d_{m1})+\gamma(1−d_{m2})+\frac{\gamma}{2}(d_{l}+d_{r}+2d_{m1}+2d_{m2}).
$$

The combinatorial multiplicity of a left-tilted 2-2 quaternary complex is constructed using the same reasoning as in the case of a 3-1 complex,

$$
C(L_{C,1},L_{C,2},L_{W,1},L_{W,2},i,j,k)=C(L_{C})\times[\frac{C(L_{W,1})}{4^{L_{o,1}}}1(L_{o,1}<L_{U}^{min})+1(L_{o,1}\geqL_{U}^{min})]\times[\frac{C(L_{W,2})}{4^{L_{o,2}}}1(L_{o,2}<L_{U}^{min})+1(L_{o,2}\geqL_{U}^{min})]\times[\frac{C(L_{C,1})}{4^{L_{o,3}}}1(L_{o,3}<L_{U}^{min})+1(L_{o,3}\geqL_{U}^{min})].
$$

To prevent double-counting the same quaternary complex, we include either the complex or its rotated representation in the container of possible complexes, but not both. If the complex is symmetric under rotation, we multiply the combinatorial multiplicity by $1/2$. Given a left-tilted 2-2 quaternary complex $(L_{C,1},L_{C,2},L_{W,1},L_{W,2},i,j,k)$, we can compute the corresponding rotated complex $(L_{C,1}^{rot},L_{C,2}^{rot},L_{W,1}^{rot},L_{W,2}^{rot},i^{rot},j^{rot},^{rot})$ by applying a linear map. The mapping of the oligomer lengths is illustrated in Figure 12B. We see that strand C2 after rotation corresponds to strand W1 before rotation, implying that $L_{C,2}^{rot}=L_{W,1}$. The same reasoning can be applied to all strands leading to the map,

$$
L_{C,1}^{rot}=L_{W,2},    L_{C,2}^{rot}=L_{W,1},    L_{W,1}^{rot}=L_{C,2},   and   L_{W,2}^{rot}=L_{C,1}.
$$

In order to compute the map of the alignment indices under rotation, we need to express the relative positions of the strands with respect to the position of strand C1 after rotation, which corresponded to W2 before rotation. For example, $|i^{rot}|$ corresponds to the number of nucleotides by which strand C2 (before rotation) protrudes beyond strand W2 (before rotation). Expressed in terms of variables before rotation, this distance may be written as $k+L_{C,2}−jL_{W,2}$. Analogous relations can be derived for all alignment indices,

$$
i^{rot}=j−k+L_{W,2}−L_{C,2},    j^{rot}=j+L_{W,2}−L_{C,1},   and   k^{rot}=j−i+L_{W,1}−L_{W,2}.
$$

##### Right-tilted 2-2 quaternary complexes

A 2-2 quaternary complex is called right-tilted if strand W1 is connected to strand W2 via strand C2 (Figure 13). As in the case of the left-tilted 2-2 complex, the oligomer lengths are again called $L_{W,1},L_{W,2},L_{C,1}$ and $L_{C,2}$, but the values of the alignment indices that are possible for the right-tilted quaternary complex differ from the ones of the left-tilted complex,

$$
i\in[L_{C,1}−L_{W,1}−1,L_{C,1}−1],    j\in[L_{C,1},i+L_{W,1}−1],   and   k\in[i+L_{W,1},k+L_{C,2}−1].
$$

Note that the range of $i$ is chosen such that at least one nucleotide of strand W1 always extends to the right beyond the end of strand C1, allowing for a hybridization region between strand C2 and W1. The boolean variables denoting the presence/absence of dangling ends read

$$
d_{l}={0if i=0,1otherwise,d_{m1}={0if i+L_{W,1}=j,1otherwise,d_{m2}={0if L_{C,1}=k,1otherwise,d_{r}={0if j+L_{W,2}=k+L_{C,2},1otherwise.
$$

The length of the overlap regions is given by

$$
L_{o,1}=L_{C,1}−max(i,0),    L_{o,2}=i+L_{W,1}−k,   and   L_{o,3}=min(k+L_{C,2},j+L_{W,2})−j.
$$

Like in the case of left-tilted 2-2 quaternary complexes, the total hybridization energy is computed via

$$
E=\gamma(L_{o,1}+L_{o,2}+L_{o,3}−3)+\gamma(1−d_{m1})+\gamma(1−d_{m2})+\frac{\gamma}{2}(d_{l}+d_{r}+2d_{m1}+2d_{m2}),
$$

and the combinatorial multiplicity via

$$
C(L_{C,1},L_{C,2},L_{W,1},L_{W,2},i,j,k)=C(L_{C})\times[\frac{C(L_{W,1})}{4^{L_{o,1}}}1(L_{o,1}<L_{U}^{min})+1(L_{o,1}\geqL_{U}^{min})]\times[\frac{C(L_{W,2})}{4^{L_{o,2}}}1(L_{o,2}<L_{U}^{min})+1(L_{o,2}\geqL_{U}^{min})]\times[\frac{C(L_{C,1})}{4^{L_{o,3}}}1(L_{o,3}<L_{U}^{min})+1(L_{o,3}\geqL_{U}^{min})].
$$

We include either the quaternary complex or its rotated representation in the list of possible complexes to avoid double-counting. Moreover, the combinatorial multiplicity is divided by 2 if the complex is symmetric under rotation. It turns out that the rotation map for the right-tilted 2-2 quaternary complex is identical to the one of the left-tilted 2-2 complex,

$$
L_{C,1}^{rot}=L_{W,2},    L_{C,2}^{rot}=L_{W,1},    L_{W,1}^{rot}=L_{C,2},    L_{W,2}^{rot}=L_{C,1},i^{rot}=j−k+L_{W,2}−L_{C,2},    j^{rot}=j+L_{W,2}−L_{C,1},   and   k^{rot}=j−i+L_{W,1}−L_{W,2}.
$$

### Numerical solution of the (De)hybridization equilibrium in the adiabatic approach

Based on the list of complexes constructed in the previous section, we can compute the equilibrium concentration of strands and complexes reached in the (de)hybridization equilibrium. In the following, we denote the concentration of a coarse-grained oligomer with length $L$ as $c(L)$, and the concentration of an oligomer with length $L$ and known sequence as $c_{s}(L)$. Recall that we assumed that all sequences of a given length that are compatible with the circular genome are equally likely in the pool. Thus, the concentration of the coarse-grained oligomer and the concentration of an oligomer with specified sequence are related by the combinatorial multiplicity,

$$
c(L)=C(L)c_{s}(L).
$$

In order to compute the concentration of a complex based on the concentration of single strands, we make use of the law of mass action. The concentration of a specific sequence realization of a complex is computed as the product of concentrations of the strands forming the complex divided by the dissociation constant $K_{d}$,

$$
c_{s}(L→,i→)=\frac{1}{K_{d}(L→,i→)}\prodjc_{s}(L_{j}).
$$

Here, $L→$ is the vector denoting the lengths of the strands comprising the complex, and $i→$ are the alignment indices. The dissociation constant is set by the hybridization energy, $ΔG$, of the complex,

$$
K_{d}(L→,i→)=(c^{∘})^{n−1}exp⁡(\betaΔG),
$$

where $c^{∘}=1M$ is the standard concentration. Just as in the case of single strands, the concentration of the sequence-independent coarse-grained complex is related to the concentration of a complex with specific sequence realization via the combinatorial prefactor,

$$
c(L→,i→)=C(L→,i→)c_{s}(L→,i→).
$$

It can be useful to combine the combinatorial multiplicity and the dissociation constant into a single effective association constant,

$$
K_{a}(L→,i→)=\frac{C(L→,i→)}{K_{d}(L→,i→)}.
$$

Note that the effective association constant including the combinatorial multiplicity is denoted by $K_{a}$ (in curly font), while the association constant without combinatorial multiplicity is denoted $K_{a}=K_{d}^{−1}$ (in regular font).

In the adiabatic approach, we study the behavior of the system on timescales that are long enough for the system to reach the (de)hybridization equilibrium, but too short for templated ligation events to take place. Therefore, the length of the oligomers is expected not to change throughout the equilibration process, and we need to introduce a separate mass conservation law for each coarse-grained oligomer, that is each oligomer length, that is included in the pool. For each length, the concentration of single-stranded coarse-grained oligomers of length $L$ and the concentration of coarse-grained oligomers of length $L$ bound in a complex need to add up to their total concentration $c(L)$ set by the initial condition,

$$
c^{eq}(L)+\sum(L→,i→)|∃js.t.L→_{j}=Lc^{eq}(L→,i→)=c^{tot}(L).
$$

In this equation, $(L→,i→)|∃js.t.L→_{j}=L$ denotes the summation over all complexes that contain at least one strand of length $L$. Note that we referred to the total concentration of oligomers of length $L$ as $c(L)$ in the main text, but for clarity, we use $c^{tot}(L)$ in the following.

Combining the mass conservation requirement with the mass action law gives a set of coupled polynomial equations. The number of equations equals the number of distinct oligomer lengths included in the pool. The polynomial equations are of degree 4, as quaternary complexes are the largest complexes to be accounted for and their concentrations equal the product of the four strands comprising the complex. We determine the equilibrium concentrations by finding the root of this set of fourth-degree polynomial equations using the Levenberg-Marquardt algorithm.

### Computing replication observables based on the adiabatic approach

As we are not modeling templated ligation events explicitly in the adiabatic approach, we compute replication observables based on the equilibrium concentration of complexes that are in a configuration which allows for a templated ligation reaction to happen. Templated ligations are possible if two strands in the complex are adjacent to each other, that is there is no gap in between two oligomers that are hybridized to the same template strand (Figure 14). Recall that the absence of a gap between two oligomers in the complex implies that the dangling end indicator variable $d_{m}=0$. The length of the product strand P is equal to the sum of the lengths of the two educt strands E1 and E2, $L_{p}=L_{e,1}+L_{e,2}$. We can use the information about the length of the product strand to compute the yield of replication. By definition, the yield equals the fraction of nucleotides used to form VCG oligomers, that is strands that are at least $L_{U}$ long,

$$
y=\frac{#nucleotidesincorporatedinVCGoligomers}{#incorporatednucleotides}.
$$

![Figure 14.](https://cdn.elifesciences.org/articles/104043/elife-104043-fig14-v1.jpg)

**Figure 14.:** The strands E1 and E2 are adjacent to each other, such that a covalent bond can form between their ends. The length of the product strand, $L_{p}$, is set by the length of the educt strands, $L_{e,1}$ and $L_{e,2}$. The likelihood for the complex to form a product oligomer whose sequence is compatible with the true circular genome, $p_{corr}$, is determined by the length of the educts and the length of their hybridization region with the template. The parts of the complex shown with hatching do not affect $p_{corr}$.

We can express this quantity in terms of the equilibrium concentration of complexes facilitating templated ligation,

$$
y=\frac{\sum(L→,i→)|(d_{m}=0∧L_{e,1}+L_{e,2}\geqL_{U}^{min}) min(L_{e,1},L_{e,2})c^{eq}(L→,i→)}{\sum(L→,i→)|d_{m}=0 min(L_{e,1},L_{e,2})c^{eq}(L→,i→)}.
$$

$(L→,i→)|(d_{m}=0∧L_{e,1}+L_{e,2}\geqL_{U}^{min})$ denotes the summation over all complexes, in which (i) the strands E1 and E2 are adjacent to each other, that is $d_{m}=0$, and (ii) the length of the product $L_{e,1}+L_{e,2}\geqL_{U}^{min}$. We multiply the equilibrium concentration by the length of the shorter educt strand to account for the number of incorporated nucleotides in line with the definition of the yield (Equation 7).

In order to compute the fidelity of replication, we need to distinguish between product oligomer sequences that are compatible with the genomes (correct sequences) and sequences that are incompatible with the genome (false sequences). As we do not know about the details of the sequences due to the coarse-grained representation of the complexes, we need to invoke a combinatorial argument to determine the fraction of correct products. To this end, we compare the number of product sequences that might be produced in a complex of given oligomer lengths and alignment indices to the number of correct products associated with the same complex configuration. The combinatorial multiplicity of the products that could be produced by a complex of given configuration is set by the combinatorial multiplicity of the possible templates, $C(L_{o,1}+L_{o,2})$, multiplied by the multiplicity of the educt strands hybridizing to the template with given lengths of the hybridization regions, $L_{o,1}$ and $L_{o,2}$,

$$
C(possible products)=C(L_{o,1}+L_{o,2})\frac{C(L_{e,1})}{C(L_{o,1})}\frac{C(L_{e,2})}{C(L_{o,2})}.
$$

The multiplicity of correct products equals the combinatorial multiplicity of strands that have the same length as the product,

$$
C(correct products)=C(L_{e,1}+L_{e,2}).
$$

This implies that the probability for a complex of given shape $(L→,i→)$ to form a correct product is given by

$$
p_{corr}(L→,i→)=\frac{C(correct products)}{C(possible products)}=\frac{C(L_{e,1}+L_{e,2})C(L_{o,1})C(L_{o,2})}{C(L_{o,1}+L_{o,2})C(L_{e,1})C(L_{e,2})}.
$$

Using this probability, we can compute the fidelity of replication,

$$
f=\frac{\sum(L→,i→)|(d_{m}=0∧L_{e,1}+L_{e,2}\geqL_{U}^{min}) p_{corr}(L→,i→)min(L_{e,1},L_{e,2})c^{eq}(L→,i→)}{\sum(L→,i→)|(d_{m}=0∧L_{e,1}+L_{e,2}\geqL_{U}^{min}) min(L_{e,1},L_{e,2})c^{eq}(L→,i→)}
$$

as well as the replication efficiency,

$$
η=\frac{\sum(L→,i→)|(d_{m}=0∧L_{e,1}+L_{e,2}\geqL_{U}^{min}) p_{corr}(L→,i→)min(L_{e,1},L_{e,2})c^{eq}(L→,i→)}{\sum(L→,i→)|d_{m}=0 min(L_{e,1},L_{e,2})c^{eq}(L→,i→)}.
$$
