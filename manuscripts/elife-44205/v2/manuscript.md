# Phylodynamic theory of persistence, extinction and speciation of rapidly adapting pathogens

## Authors

- Le Yan<sup>1</sup> ([ORCID: 0000-0003-1323-0545](https://orcid.org/0000-0003-1323-0545)) †
- Richard A Neher<sup>2</sup> ([ORCID: 0000-0003-2525-1407](https://orcid.org/0000-0003-2525-1407)) †
- Boris I Shraiman<sup>1</sup> ([ORCID: 0000-0003-0886-8990](https://orcid.org/0000-0003-0886-8990)) †

### Affiliations

1. Kavli Institute for Theoretical Physics University of California, Santa Barbara Santa Barbara United States
2. Biozentrum University of Basel, Swiss Institute for Bioinformatics Basel Switzerland

† Corresponding author

## Abstract

Rapidly evolving pathogens like influenza viruses can persist by changing their antigenic properties fast enough to evade the adaptive immunity, yet they rarely split into diverging lineages. By mapping the multi-strain Susceptible-Infected-Recovered model onto the traveling wave model of adapting populations, we demonstrate that persistence of a rapidly evolving, Red-Queen-like state of the pathogen population requires long-ranged cross-immunity and sufficiently large population sizes. This state is unstable and the population goes extinct or ‘speciates’ into two pathogen strains with antigenic divergence beyond the range of cross-inhibition. However, in a certain range of evolutionary parameters, a single cross-inhibiting population can exist for times long compared to the time to the most recent common ancestor (TM⁢R⁢C⁢A) and gives rise to phylogenetic patterns typical of influenza virus. We demonstrate that the rate of speciation is related to fluctuations of TM⁢R⁢C⁢A and construct a ‘phase diagram’ identifying different phylodynamic regimes as a function of evolutionary parameters.

## Introduction

In a host population that develops long-lasting immunity, a pathogen can persist by infecting immunological naive individuals such as children, or through rapid antigenic evolution that enables the pathogen to evade immunity and re-infect individuals. Childhood diseases like measles or chicken pox fall into the former category, while influenza virus adapts rapidly and re-infects most humans multiple times during their lifespan. The continuous adaptation of influenza is facilitated by high mutation rates resulting in diverse populations of co-circulating viral strains. Nevertheless, almost always a single variant eventually outcompetes the others such that diversity within one subtype or lineage remains limited (Petrova and Russell, 2018).

The contrast of rapid evolution while maintaining limited genetic diversity is most pronounced for the influenza virus subtype A/H3N2. Figure 1 shows a phylogenetic tree of HA sequences of type A/H3N2 with the characteristic ‘spindly’ shape. The most recent common ancestor of the population is rarely more than 3–5 years in the past (Rambaut et al., 2008). Other pathogenic RNA viruses that typically do not reinfect the same individual, (measles, mumps, HCV, or HIV) diversify for decades or centuries (Grenfell et al., 2004). Interestingly, influenza B has split into two co-circulating lineages in the 1970s which by now are antigenically distinct (Rota et al., 1990) and maintain intermediate levels of diversity (see Figure 1).

![Figure 1.](https://cdn.elifesciences.org/articles/44205/elife-44205-fig1-v2.jpg)

**Figure 1.:** The top left panel shows a phylogeny of the HA segment of influenza A virus of subtype H3N2 from its emergence in 1968 to 2018. The virus population never accumulates much diversity but is rapidly evolving. The lower left panel shows a phylogeny of the HA segment of influenza B viruses from 1940 to 2018. In the 70s, the population split into two lineages known as Victoria (B/Vic) and Yamagata (B/Yam) in the 1970s. The graphs on the right quantify diversity via the time to the most recent common ancestor $T_{M⁢R⁢C⁢A}$ for different influenza virus lineages. Influenza B viruses harbor more genetic diversity than influenza A viruses. The subtype A/H3N2 in particular coalesces typically in 3y while deeps splits in excess of 5y are rare.

Influenza virus infections elicit lasting immunity rendering most individuals non-susceptible to viruses that circulated during their lifetime (Fonville et al., 2014). The virus population escapes collective human immunity by accumulating amino acid substitutions in its surface glycoproteins (Koel et al., 2013; Wilson and Cox, 1990). Extensive genetic characterizations have shown that within each subtype many HA sequence variants co-circulate (Rambaut et al., 2008; Fitch et al., 1997). These variants differ from each other by ∼10 substitutions and compete for susceptible hosts (Strelkowa and Lässig, 2012). The rapid sequence evolution results in a decay of immune cross-reactivity over ∼10 years (Smith et al., 2004; Bedford et al., 2014; Fonville et al., 2014; Neher et al., 2016).

Epidemiological dynamics of influenza is often modeled using generalizations of the classic Susceptible-Infected-Recovered (SIR) model to multiple antigenically distinct viral strains (Kermack and McKendrick, 1927; Gog and Grenfell, 2002). Such models need to capture (i) how the infection with one strain affects susceptibility to other strains and (ii) how novel strains are generated from existing strains by mutations. A common approach has been to impose a discrete one-dimensional strain space in which new strains are generated by mutation of adjacent strains. Infection results in a reduction of susceptibility in a manner that depends on the distance in this one-dimensional strain space (Andreasen et al., 1996; Gog and Grenfell, 2002). Such models naturally result in ‘traveling waves’ in the sense that the pathogen population moves through strain space by recurrent emergence of antigenically advanced variants produced by mutation from neighboring strains (Lin et al., 2003).

These models of antigenically evolving populations are related to general models of rapid adaptation in which populations form a traveling wave moving towards higher fitness (Tsimring et al., 1996; Rouzine et al., 2003; Desai and Fisher, 2007; Neher et al., 2014), reviewed in Neher (2013a). Recently, Rouzine and Rozhnova (2018) described an explicit mapping between a SIR model in a one-dimensional antigenic space and traveling wave models in fitness.

Traveling wave (TW) models in a one-dimensional antigenic space naturally result in spindly phylogenies: There is only one possible direction for immune escape and the fastest growing most antigenically advanced strain grows drives all other strains extinct. Influenza viruses, however, can escape immunity by mutations at a large number of positions (Wilson and Cox, 1990), suggesting antigenic space is high dimensional (Perelson and Oster, 1979). In many dimensions, different viral strains can escape immunity via different paths and diverge sufficiently from each other until they no longer compete for hosts and thereafter propagate independently evolve. A satisfactory explanation of spindly phylogenies therefore has to describe how evolution in a high dimensional space reduces to an effectively one-dimensional path without persistent branching or rapid extinction. Several computational studies have addressed this question and identified cross-immunity (Bedford et al., 2012; Tria et al., 2005; Koelle et al., 2011; Ferguson et al., 2003; Sasaki and Haraguchi, 2000) as well as deleterious mutations (Koelle and Rasmussen, 2015; Gog and Grenfell, 2002) as critical parameters. We will discuss this earlier work at greater length below.

Our work aims to examine the conditions under which the evolving pathogen can maintain a spindly phylogeny with an approximately constant level of diversity – sufficient to avoid extinction, yet constrained from further branching by cross-inhibition between not too distant strains. We show that long range cross immunity in generic stochastic models of antigenic evolution generates such phylogenies. However, in the long term the viral population either ‘speciates’ into weakly interacting diverging lineages or goes extinct with rates that are controlled by three dimensionless combinations of model parameters. While the relation of these parameters to the known characteristics of influenza epidemiology and evolution is not direct, the general ‘phase diagram’ captured by the parameters of the simple model illustrates the key competing factors governing expected long-term dynamics.

## Results

### Model

A model of an antigenically evolving pathogen population needs to account for cross-immunity between strains and the evolution of antigenically novel strains. We use an extension of the standard multi-strain SIR model (Gog and Grenfell, 2002). The fraction of individuals $I_{a}$ infected with viral strain $a$ changes according to

$$
\frac{d}{d⁢t}⁢I_{a}=\beta⁢S_{a}⁢I_{a}-(ν+\gamma)⁢I_{a}
$$

where $\beta$ is the transmissibility, $S_{a}$ is the population averaged susceptible to strain $a$, $ν$ is the recovery rate, and $\gamma$ is the population turnover rate. The fraction $R_{a}$ of the population recovered from infection with strain $a$ changes according to

$$
\frac{d}{dt}R_{a}=νI_{a}−\gammaR_{a}
$$

Our focus here is on antigenically evolving pathogens that reinfect an individual multiple times during its life-time, we shall ignore population turnover and set $\gamma=0$ right away to simplify presentation.

The dynamics of $I_{a}$ depends on the average susceptibility of the host population $S_{a}=⟨S_{a}⁢(i)⟩_{i}$, while the susceptibility $S_{a}⁢(i)$ of host $i$ depends on the host’s history of previous infections. A plausible representation of the history dependence of susceptibility at the level of individuals has a product form (Wikramaratna et al., 2015)

$$
S_{a}^{(\sigma)}=⟨\prodb(1-K_{a⁢b}⁢\sigma_{b}⁢(i))⟩_{i}
$$

where $\sigma_{b}⁢(i)$ is one or zero depending on whether host $i$ has or has not been previously infected with strain $b$. Matrix $K_{a⁢b}\leq1$ quantifies the cross-immunity to strain $a$ due to prior infection with strain $b$. Thus, Equation 3 expresses the susceptibility $S_{a}$ in terms of a product of attenuation factors each arising from a prior infection by a different strain $b$. A simple, but adequate approximation for the population averaged susceptibility is provided by replacing $\sigma_{b}⁢(i)$ in the product in Equation 3 by the fraction of the population $R_{b}$ that recovered from infection with strain $b$:

$$
S_{a}≈\prodb(1-K_{a⁢b}⁢R_{b})≈e^{-\sum_{b}K_{a⁢b}⁢R_{b}}
$$

This corresponds to the ‘order one independence closure’ by Kryazhimskiy et al. (2007) and is known as Mean-Field approximation in physics (Weiss, 1907; Landau and Lifshitz, 2013). The Mean-Field approximation here corresponds to ignoring correlations between subsequent infection in the individual histories. Approximating the product by the exponential is justified because the total fraction of the host population infected by any single strain in the endemic regime is typically small (Yang et al., 2015). A detailed derivation of Equation 4 and more detailed discussion of approximations is given in Appendix 1. While the original formulation of immunity in Equation 3 is based on the infection history of individuals (Andreasen et al., 1997), the population average over the factorized distribution of histories relates the model to status based formulations (Gog and Grenfell, 2002). While some differences between status and history-based models have been reported (Ballesteros et al., 2009), others have shown that different model types have similar properties (Ferguson and Andreasen, 2002). The differences between these models and approximations are small compared to the crudeness with which these simple mathematical models capture the complex immunity profile of the human population. A model similar to ours has been successfully applied to influenza virus evolution (Luksza and Lässig, 2014).

We note that differentiating Equation 4 with respect to time defines the equation governing the dynamics of population average susceptibility

$$
\frac{d}{d⁢t}⁢S_{a}=-ν⁢S_{a}⁢\sumbK_{a⁢b}⁢I_{b}
$$

which is exactly the same as the dynamics of susceptibility in Gog and Grenfell (2002) and Luksza and Lässig (2014) in the limit of negligible population turnover $\gamma/ν≪1$.

New strains are constantly produced by mutation with rate $m$. The novel strain will differ from its parent at one position in its genome. Following Luksza and Lässig (2014), we assume that cross-immunity decays exponentially with the number of mutations that separate two strains:

$$
K_{a⁢b}=\alpha⁢e^{-\frac{|a-b|}{d}}
$$

where $|a-b|$ denotes the mutational distance between the two strains, $d$ denotes the radius of cross-immunity measured in units of mutations. Antigenic space is thereby assumed to be high dimensional and antigenic distance is proportional to genetic distance in the phylogenetic tree (Neher et al., 2016). The parameter $\alpha\leq1$ quantifies the reduction of susceptibility to reinfection by the same strain and hence the overall strength of protective immunity. We shall set $\alpha=1$ corresponding to perfect protection here for simplicity of presentation. Our analysis below applies equally well to the more realistic case of $\alpha<1$, since in our approximation this parameter can be eliminated by rescaling $R_{a}$ and $I_{a}$ and ultimately merely renormalizes the host population size, which serves as one of the ‘control parameters’ in our analysis.

Cross-immunity and the mutation/diversification process are illustrated in Figure 2. An infection with a particular strain (center of the graph) generates a cross-immunity footprint (shaded circles). Mutation away from the focal strain reduces the effect of existing immunity in the host population, but complete escape requires many mutations. Hence closely related viruses compete against each other for susceptible individuals.

![Figure 2.](https://cdn.elifesciences.org/articles/44205/elife-44205-fig2-v2.jpg)

**Figure 2.:** Via cross-reactivity, the immunity foot-print of ancestral variants (center of the graph) mediates competition between related emerging viral strains and can drive all but one of the competing lineages extinct. At high mutation rates and relatively short range of antigenic cross-reactivity, different viral lineages can escape inhibition and continue to evolve independently.

The above model was formulated in terms of the deterministic Equations 1-4. The actual dynamics, however, is stochastic in two respects: (i) antigenic mutations are generated at random with rate $m$ and (ii) stochasticity of infection and transmission. The latter can be captured by interpreting the terms in Equation 1 as rates of discrete transitions in a total population of $N_{h}$ hosts. This stochasticity is particularly important for novel mutant strains that are rare. Most rare strains are quickly lost by chance even if they have a growth advantage due to antigenic novelty. To account for stochasticity in a computationally efficient way, we employ a clone-based hybrid scheme where mutation and the dynamics of rare mutants are modeled stochastically, while common strains follow deterministic dynamics, see Materials and methods (Clone-based simulations).

We will use the recovery rate $ν$ to set the unit of time, fixing $ν=1$ in rescaled units. The remaining parameters of the model are (1) the transmission rate $\beta$ - in our units the number of transmission events per infection and hence equal to the basic reproduction number $R_{0}$, (2) the mutation rate $m$, (3) the range of cross-immunity $d$ measured as the typical number of mutations needed for an $e$-fold drop of cross-inhibition, and (4) the host population size $N_{h}$.

### Phenomenology

Before proceeding with a quantitative analysis we discuss different behaviors qualitatively. Figure 3A shows several trajectories of prevalence $I_{t⁢o⁢t}=\sum_{a}I_{a}$ (i.e. total actively infected fraction) for several different parameters. Depending on the range of cross-immunity, the pathogen either goes extinct after a single pandemic (red line) or settles into a persistently evolving state, the Red Queen State (RQS) traveling wave (Van Valen, 1973 In large populations the RQS exhibits oscillations in prevalence. As we will discuss further below, the RQS state is transient and either goes extinct after some time or splits into multiple antigenically diverging lineages that propagate independently. To quantitatively understand the dependence on parameters, we will further simplify the model and establish a connection to models of rapid adaptation in population genetics. Figure 3BC shows parameter regimes corresponding to distinct qualitative behaviors. The relevant parameters are three combinations of the population size $N_{h}$, the selection coefficient of novel mutations $s$, the mutation rate $m$, and the radius of cross-immunity $d$. A long-lived but transient RQS regime is flanked be the regime of deterministic extinction (red) and the regime of continuous branching and diversification – the ‘speciation’ regime (blue). The RQS regime itself undergoes a transition from a steady traveling wave (yellow) to a limit cycle oscillation (green) with increasing population size. The location of the boundaries depend on the time scale of observation as the cumulative probability of extinction and speciation increases with time.

![Figure 3.](https://cdn.elifesciences.org/articles/44205/elife-44205-fig3-v2.jpg)

**Figure 3.:** (A) Typical trajectories of infection prevalence in the parameter regimes corresponding to extinction (red), traveling wave RQS (yellow) and oscillatory RQS (green). Panels B and C schematically show parameter regimes corresponding to these qualitatively different behaviors. As explained in the text the boundaries $q_{e⁢x},q_{s⁢p}$ of the RQS regime depend explicitly on the time scale considered (see also Figure 7). Simulation results supporting this diagram are shown in Figure 3—figure supplements 1 and 2. Panel (D) is a schematic illustrating how a novel pandemic strain (red) can settle into an endemic RQS state. As the cumulative number of infected individuals increases, the susceptible fraction decreases, and survival of the strain depends on the emergence of antigenic escape mutations (gray). The top part of the panel illustrates the population composition at a particular time point. Rare pioneering variants are $q$ mutations ahead of the dominant variant and grow with rate $x_{n}$. (Note, that boundaries of the ‘extinction’ regime in (B,C) correspond to $q$ value close to one.) Different lineages are related via their phylogenetic tree embedded in the fitness distribution in the population.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/44205/elife-44205-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** The data points are assigned to phases using the following criteria. The extinction phase (red): $\tau_{ext}<10⁢\tau_{sw}$; The speciation phase (blue): $\tau_{sp}<10⁢\tau_{sw}$; The transient RQS regime (yellow and green): otherwise. Red and blue lines correspond to the extinction boundary $q_{e⁢x⁢t}$ and speciation boundary $q_{s⁢p}$ respectively, defined for $\tau=10⁢\tau_{sw}$. The black solid line corresponds to the onset of spontaneous oscillation $log⁡(N_{h}⁢I¯)=8.3$. Color in the transient phase labels the amplitude of prevalence $var⁢(log⁡I_{t⁢o⁢t})$, increasing from yellow to green. Simulation set $d=50$.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/44205/elife-44205-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Value of $q$ across the ‘Phase diagram’.This figure shows the same data as one with each data point colored by the corresponding value of $q$, which is constant along the straight of different angle.

### Large effect antigenic mutations allow transition from pandemic to seasonal dynamics

A novel virus in a completely susceptible population will initially spread with rate $\beta-1$ and the pandemic peaks when susceptible fraction falls to $\beta^{-1}$. The trajectory of such a pandemic strain in the time-susceptibility plane is indicated in red in Figure 3D. Further infections in the contracting epidemic will then push susceptibility below $\beta^{-1}$ – the propagation threshold for the virus – and without rapid antigenic evolution the pathogen will go extinct after a time $t∼\beta^{-1}⁢log⁡N_{h}$. Such boom-bust epidemics are reminiscent of the recent Zika virus outbreak in French Polynesia and the Americas where in a short time a large fraction of the population was infected and developed protective immunity (O'Reilly et al., 2018).

Persistence and transition to an endemic state is only possible if the pathogen can evade the rapid build-up of immunity via a small number of large effect antigenic mutations. This process is indicated in Figure 3D by horizontal arrows leading to antigenically evolved strains of higher susceptibility and bears similarity to the concept of ‘evolutionary rescue’ in population genetics (Gomulkiewicz, 1995). The parameter range of the idealized SIR model that avoid extinction after a pandemic resulting in persistent endemic disease is relatively small. Yet, various factors like geographic structure, heterogeneity of host adaptation and population turn-over slow down the pandemic and extinction, thereby increasing the chances of sufficient antigenic evolution to enter the endemic, RQS-type, regime. The 2009 pandemic influenza A/H1N1 has undergone such a transition from a pandemic to a seasonal/endemic state. We shall not investigate the transition process in detail here, but will assume that endemic regime has been reached.

### Long-range cross-immunity results in evolving but low diversity pathogen populations

Once the pathogen population has established an endemic circulation through continuous antigenic evolution (green and yellow regimes in Figure 3BC), the average rate of new infections $\beta⁢\sum_{a}I_{a}⁢S_{a}/I_{t⁢o⁢t}$ fluctuates around the rate of recovery $ν=1$ (in our time units). This balance is maintained by the steady decrease in susceptibility due to rising immunity against resident strains and the emergence of antigenically novel strains, see Figure 3D. If the typical mutational distance between strains is small compared to the cross-immunity range $d$, the rate at which susceptibility decreases is similar for all strains. To see this we expand $K_{a⁢b}$ in Equation 5

$$
S_{a}^{-1}⁢\frac{d}{d⁢t}⁢S_{a}⁢(t)=-\sumbe^{-\frac{|a-b|}{d}}⁢I_{b}≈-I_{t⁢o⁢t}+\sumb\frac{|a-b|}{d}⁢I_{b}
$$

where we have used that $|a-b|≪d$ for all pairs of strains with substantial prevalence. In fact it will suffice to keep only the first, leading, term on the right hand side. Close to a steady state, prevalent strains obey $\beta⁢S_{a}≈1$. We can hence define the instantaneous growth rate of strain $x_{a}=(\beta⁢S_{a}-1)≪1$ as its effective fitness. In this limit, the model can be simplified to

$$
\frac{d}{dt}I_{a}=x_{a}I_{a}\frac{d}{dt}x_{a}≈−I_{tot}
$$

The second equation means that effective fitness of all strains $a$ decreases approximately at the same rate since the pathogen population is dominated by antigenically similar strains.

If a new strain $c$ emerged from strain $a$ by a single antigenic mutation, its mutational distance from a strain $b$ is $|c-b|=|a-b|+1$ and $K_{c⁢b}=K_{a⁢b}⁢e^{-d^{-1}}≈K_{a⁢b}⁢(1-d^{-1})$. The population susceptibility of strain $c$ is therefore increased to

$$
S_{c}≈e^{-(1-d^{-1})⁢\sum_{b}K_{a⁢b}⁢R_{b}}≈S_{a}⁢(1-\frac{log⁡S_{a}}{d})
$$

Since the typical susceptibility is of order $\beta^{-1}$, the growth rate of the mutant strain $c$ is $s=d^{-1}⁢log⁡\beta$ higher than that of its parent. The growth rate increment, s, plays the role of a selection coefficient in typical population genetic models and corresponds to the step size of the fitness distribution in Figure 3D. In such models, individuals within a fitness class (bin of the histogram) are equivalent and different classes can be modeled as homogeneous populations which greatly accelerates numerical analysis of the model, see Materials and methods.

Rouzine and Rozhnova (2018) have recently formulated a similar model of antigenic evolution of rapidly adapting pathogens. Analogously to our model, Rouzine and Rozhnova couple strain dynamics to antigenic adaptation through mutations, albeit assuming a one-dimensional antigenic space. In agreement with Rouzine and Rozhnova, we find that selection coefficients of novel mutations are inversely proportional to the cross-immunity rate $d$ and increase with infectivity $\beta$, see Equation 9. Rouzine and Rozhnova, however, do not consider oscillations, extinction, and speciation (see below).

The simplified model in Equation 8, along with the model developed by Rouzine and Rozhnova (2018), is analogous to the traveling wave (TW) models of rapidly adapting asexual populations that have been studied extensively over the past two decades (Tsimring et al., 1996; Desai and Fisher, 2007; Rouzine et al., 2003; Hallatschek, 2011), see Neher (2013a) for a review. These models describe large populations that generate beneficial mutations rapidly enough that many strains co-circulate and compete against each other. The fittest (most antigenically advanced) strains are often multiple mutational steps, $q$, ahead of the most common strains, see Figure 3D. This ‘nose’ of the fitness distributions contains the strains that dominate in the future and the only adaptive mutations that fixate in the population arise in pioneer strains in the nose. Consequently, the rate with which antigenic mutations establish in the population is controlled by the rate at which they arise in the nose (Desai and Fisher, 2007). If the growth rate at the nose of the distribution, $x_{n}$, is much higher than antigenic mutation rate, $x_{n}≫m$, it takes typically

$$
\tau_{a}=\frac{log⁡(x_{n}/m)}{x_{n}}
$$

generations before a novel antigenic mutation arises in a newly arisen pioneer strain that grows exponentially with rate $x_{n}$. The advancement of the nose is balanced rapidly by the increasing population mean fitness.

If beneficial mutations have comparable effects on fitness and population sizes are sufficiently large ($N⁢m≫1$), the fitness distribution has an approximately Gaussian shape with a variance $\sigma^{2}≈2⁢s^{2}⁢log⁡(N⁢s)/log^{2}⁡(x_{n}/m)$. The wave is $\sigma/s$ mutations wide, while the most advanced strains are approximately $q=2⁢log⁡(N⁢s)/log⁡(x_{n}/m)$ ahead of the mean (Desai and Fisher, 2007). Two contemporaneous lineages coalesce on a time scale $\tau_{sw}=s⁢q/\sigma^{2}=s^{-1}⁢log⁡(x_{n}/m)$ and the branching patterns of the tree resemble a Bolthausen-Sznitman coalescent rather than a Kingman coalescent (Desai et al., 2013; Neher and Hallatschek, 2013b).

In circulating influenza viruses, typically around 3–10 adaptive mutations separate pioneer strains from the most common variants (Strelkowa and Lässig, 2012; Neher and Bedford, 2015). While this clearly corresponds to a regime where multiple stains compete, it does not necessarily mean that asymptotic formulae assuming $q≫1$ are accurate. Nevertheless, many qualitative features of TW models have been shown to qualitatively extend into regimes where $q$ takes intermediate values (Neher and Hallatschek, 2013b).

While parameter $N$ in the TW models summarized above is a fixed population size, the corresponding entity in our SIR model is the fluctuating pathogen population size $N_{p}$ which is related to the (fixed) host population size $N_{h}$ by $N_{p}=N_{h}⁢I_{t⁢o⁢t}$. The average $I_{t⁢o⁢t}$ depends on other parameters of the model, scaling in particular with $I¯∼s^{2}$. Hence, it will be convenient for us to use $N_{h}⁢s^{2}$ as one of the relevant ‘control parameters’, replacing $N$ of the standard TW model.

### Stability and fluctuations of the RQS

In contrast to most population genetic models of rapid adaptation, our epidemiological model does not control the total population size directly. Instead, the pathogen population size (or prevalence) depends on the host susceptibility, which in itself is determined by recent antigenic evolution of the pathogen. The coupling of these two different effects results in a rich and complicated dynamics (see Figure 4A for an example trajectory): The first effect is ecological: a bloom of the pathogen depletes susceptible hosts leading to a crash in pathogen population and a tendency of the population size to oscillate London and Yorke, 1973 (blue line in Figure 4A). The second effect is evolutionary: higher nose fitness $x_{n}$ begets faster antigenic evolution and vice versa, resulting in an apparent instability in the advancement of the antigenic pioneer strains (Fisher, 2013) (yellow line and inset in Figure 4A). In our epidemiological model, as we shall show below, fluctuations in the rate of antigenic advance of the pioneer strains couple with a delay of $\tau_{sw}$ to the ecological oscillation.

![Figure 4.](https://cdn.elifesciences.org/articles/44205/elife-44205-fig4-v2.jpg)

**Figure 4.:** (A) An example of the stochastic limit cycle trajectory from the fitness-class simulation. Note the rapid rise and fall of infection prevalence (blue), which causes a drop in nose fitness (yellow) which subsequently recovers (approximately linearly) during the remainder of the cycle. Fluctuations in $I_{t⁢o⁢t}⁢(t)$ and $x_{n}⁢(t)$ from cycle to cycle are caused by the stochasticity of $x_{n}$, that is antigenic evolution in pioneer strains. A particularly large fluctuation about $\tau_{sw}$ prior to the end, caused a large spike in prevalence, followed by the collapse of $x_{n}$ below zero and complete extinction. Inset (red) shows the cross-correlation between $x_{n}$ and $\sigma^{2}$ which peaks with the delay $\tau=\tau_{sw}$ (additional peaks reflect the oscillatory nature of the state and are displaced by integer multiples of mean period). (B) A family of limit cycles in the infection prevalence/mean fitness plane as described by Equation (11) with fixed variance. The variation of $\sigma$ governed by the Equations 11 and 12 (in the deterministic limit) reduces the family to a single limit cycle (red); (C) Trajectories in the infection prevalence/nose fitness generated by the stochastic DD system in the regime above (right panel) and below (left panel) the oscillatory instability of the deterministic DD system.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/44205/elife-44205-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Top: Amplitude of epidemic circulations in logarithm of total prevalence. The amplitude predicted in the fitness class-based (FC) simulation is consistent with the clone-based simulation, bounded from below by the amplitude in the deterministic differential-delay approximation (DDE), which sets on at the spontaneous oscillation threshold $log(N_{h}I¯s)_{o⁢s⁢c}=8.3$, indicated by the dashed line. When the noise is properly considered as in Equation (15), the amplitude can also be predicted from the stochastic differential-delay equations (DDE). Bottom: Period of epidemic oscillation, also bounded below by the limit cycle period of the deterministic DDE.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/44205/elife-44205-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) In our model, the speed of traveling wave varies in time. The instantaneous speeds measured from immune adaptation, Fisher’s theorem, and nose advance could be different at any given moment. (B) But in the phase with steady traveling waves, the time-averaged speeds are consistent for different parameters. (C) The average nose position and (D) the average speed of adaptation (in the clone-based simulation) are consistent with the prediction of the traveling wave theory.

To recognize the ecological aspect of the oscillatory tendency, consider the total prevalence $I_{t⁢o⁢t}$ and the mean fitness of the pathogen $X=\sum_{a}x_{a}⁢I_{a}/I_{t⁢o⁢t}$ 

$$
\frac{d}{d⁢t}⁢I_{t⁢o⁢t}=X⁢I_{t⁢o⁢t};\frac{d}{d⁢t}⁢X=\sigma^{2}-I_{t⁢o⁢t}
$$

which follows directly from Equation (8). Selection on fitness variance $\sigma^{2}$ increases $X$, while prevalence $I_{t⁢o⁢t}$ reduces susceptibility and hence $X$. At fixed variance $\sigma=\sigma¯$ this system is equivalent to a non-linear oscillator describing a family of limit cycles oscillating about $I_{t⁢o⁢t}=\sigma¯^{2}$ and $X=0$ as shown in Figure 4B.

While Equation (11) describes the behavior of common strains, the mutation driven dynamics of the antigenic pioneer strains is governed by the equation for $x_{n}$ that in a continuum limit (suitable for the limit of high mutation rate) reads:

$$
\frac{d}{d⁢t}⁢x_{n}=\tau_{sw}^{-1}⁢x_{n}-I_{t⁢o⁢t}+s⁢ξ⁢(t)
$$

The first term on the right hand side represents the rate at which antigenic pioneer strains enter the population, $\tau_{a}^{-1}$, advancing the nose fitness by an increment $s$ (with $\tau_{a}^{-1}⁢s=\tau_{sw}^{-1}⁢x_{n}$ ). The second term on the right hand side of Equation (12) represents gradual reduction of susceptibility of the host population, and $ξ⁢(t)$ is a random noise variable representing the stochasticity of the establishment of new strains. The Gaussian white noise $ξ⁢(t)$ is defined statistically by its correlation function $⟨ξ⁢(t)⁢ξ⁢(0)⟩=\tau_{a}^{-1}⁢\delta⁢(t)$, see Materials and methods (Stochastic differential-delay simulation).

The first term of Equation (12) captures the apparent instability of the nose: an advance of the nose to higher $x_{n}$ accelerates its rate of advancement. The stabilizing factor is the subsequent increase in $I_{t⁢o⁢t}$, but to see how that comes about we must connect Equation (12) to Equation (11). The connection is provided by $\sigma^{2}$ since it is controlled by the emergence of novel strains, that is the dynamics of the ‘nose’ $x_{n}$, which impacts the bulk of the distribution after a delay $\tau_{sw}$. Based on the analysis detailed in the Appendix 2, we approximate

$$
\sigma^{2}⁢(t)≈\tau_{sw}^{-1}⁢x_{n}⁢(t-\tau_{sw})
$$

relating population dynamics, Equation (11), to antigenic evolution of pioneer strains described by Equation (12). Taken together Equations (11-13) define a Differential Delay (DD) system of equations. Sample simulations of this stochastic DD system are shown in Figure 4 BC. The delay approximation Equation (13) is supported by the cross-correlation of $x_{n}⁢(t)$ and $\sigma^{2}⁢(t^{′})$ measured using fitness-class simulations (see Figure 4A Inset).

The deterministic limit of the DD system (obtained by omitting the noise term in Equation (12)) has a fixed point at $\tau_{sw}^{-1}⁢x¯_{n}=\sigma¯^{2}=2⁢\tau_{sw}^{-2}⁢log⁡(N_{h}⁢I¯)$. Small deviations decay in underdamped oscillations with frequency $\omega=\sigma¯=\tausw-1⁢\sqrt{2⁢log⁡(N_{h}⁢I¯)}$ if $\omega⁢\tau_{sw}<2⁢\pi$. For $\omega⁢\tau_{sw}>2⁢\pi$, the system fails to recover from a deviation of the nose in a single period and the steady state becomes unstable to a limit cycle oscillation. The nonlinearity of Equation (11) implies a longer period with increasing amplitude and the system is stabilized at a limit cycle with the period long enough compared to the feedback delay $\tau_{sw}$. In Appendix 3, we derive the threshold of oscillatory instability to lie at $log⁡(N_{h}⁢I¯_{o⁢s⁢c}⁢s)≈8.3$ (leading to limit cycle period $T≈1.5⁢\tau_{sw}$, see Figure 4—figure supplement 1). We also find that the amplitude of the oscillation $log⁡(I_{m⁢a⁢x}/I¯)$ scales as $log⁡(N_{h}⁢I¯)$ for large values of the later. This transition defines quantitatively the boundary between the TW RQS and the Oscillatory RQS regimes that appear on the phase diagrams in Figure 3 (BC). The validity of the predictions of standard TW theory for our adapting SIR system are explored in Figure 4—figure supplement 2.

The distinction between the TW and Oscillatory RQS is obscured by the stochasticity of antigenic advance, Equation (12), which continuously feeds the underdamped relaxation mode, generating a noisy oscillation with the frequency $\omega$ defined above. The difference between the two regimes is illustrated by Figure 4C: in the TW RQS noisy oscillation is about the fixed point, whereas in the Oscillatory RQS it is about deterministic limit cycle.

Interestingly, the dynamics of the Oscillatory RQS, as shown in Figure 4A, can be understood in terms of a non-linear relaxation oscillator. At relatively low infection prevalence nose fitness $x_{n}$ increases until rising $I_{t⁢o⁢t}$ catches up with it (when $I_{t⁢o⁢t}=\tau_{sw}^{-1}⁢x_{n}$) driving it down rapidly. Once this ‘mini-pandemic’ burns out, the population returns to the low prevalence part of the cycle $I_{t⁢o⁢t}<\tau_{sw}^{-1}⁢x_{n}$, when $x_{n}$ begins to increase again.

### The rate of extinction

While in the deterministic limit the differential-delay system predicts a stable steady TW for $q>q_{e⁢x},I¯<I¯_{o⁢s⁢c}$ and a limit cycle above $I¯_{o⁢s⁢c}$, fluctuations in the establishment of the antigenic pioneer strains (Equation (12)) can lead to stochastic extinction. In fact, both the TW and Oscillatory RQS (see Figure 3BC) are transient, subject to extinction due to a sufficiently large stochastic fluctuation. (Note however the contrast with the ‘extinction’ state in Figure 3BC, where extinction is deterministic and rapid.) The rate of extinction depends on $q$ and $log⁡(N_{h}⁢I¯)$ as shown in Figure 5A. The time to extinction increases dramatically in the range of $q∼1-2$ and more slowly thereafter. Although extinction is fluctuation driven, the mechanism of extinction in the oscillatory state is related closely to the deterministic dynamics, according to which large amplitude excursion in infection prevalence can lead to extinction. A large $x_{n}$ advance leads, after a time $\tau_{sw}$ to a rise in prevalence $I_{t⁢o⁢t}$, followed by the rapid fall in the number of susceptible hosts and hence loss of viral fitness. This turns out to be the main mode of fluctuation driven extinction as illustrated by Figure 4C. One expects extinction to take place when a fluctuation induced deviation $\delta⁢x$ of the fitness of pioneer strains becomes of the order of the mean $x¯_{n}$. New mutations at the nose accumulate with rate $1/\tau_{a}$ such that at short times $t$ we expect $\delta⁢x≈s⁢\sqrt{t/\tau_{a}}$. Hence $\delta⁢x$ becomes of the order of the mean $x¯_{n}$ at times $\tau_{ext}∼q⁢\tau_{sw}$. However the probability of extinction will also depend on the shape of the oscillatory limit cycle (as it depends on the minimum of infection prevalence during the cycle), which in turn depends on $log⁡(N_{h}⁢I¯)$. Numerical simulations, Figure 5B, confirm the dependence of $\tau_{ext}$ on $q$ and $log⁡(N_{h}⁢I¯)$. We note that the rate increase in $\tau_{ext}$ with increasing $q$ slows down in the oscillatory regime and appears to approach a power law dependence $\tau_{ext}/\tau_{sw}∼q^{2.5}$ (albeit over a limited accessible range): presently we do not have an analytic understanding of this specific functional form.

![Figure 5.](https://cdn.elifesciences.org/articles/44205/elife-44205-fig5-v2.jpg)

**Figure 5.:** (A) Simulation results for the average extinction time $\tau_{ext}$ (open symbols) and the average speciation time $\tau_{sp}$ (filled symbols) as a function of pathogen diversity $q$. The life time of the endemic RQS state is limited by the smaller of $\tau_{ext}$ and $\tau_{sp}$. If $\tau_{sp}<\tau_{ext}$, the population tends to speciate and persist, while the population is more likely to go extinct if $\tau_{sp}>\tau_{ext}$. The graph shows $\tau_{sp}$ and $\tau_{ext}$ rescaled with the sweep time $\tau_{sw}$ as a function of genetic diversity measured by the number of mutations $q$. The speciation time $\tau_{sp}$ increases with the range of cross-inhibition ($d$) and decreases with $q$. Note the agreement between the results of the fitness class-based simulation (black line in (A)) and the clone-based simulation (colored squares in (A)). (B) Extinction time over a broad range of parameters, obtained via fitness class-based simulation of population dynamics, confirms its primary dependence on $q$ for large population sizes.

### The rate of speciation

The correspondence of the multi-strain SIR and the TW models discussed above assumes that cross-immunity decays slowly compared to the coalescent time of the population, that is $d/q≫1$. In this case, all members of the population compete against each other for the same susceptible hosts. Conversely, if the viral population were to split into two sub-populations separated by antigenic distance greater than the range of cross-inhibition $d$, these sub-population would no-longer compete for the hosts, becoming effectively distinct viral ‘species’ that propagate (or fail) independently of each other. Such a split has for example occurred among influenza B viruses, see Figure 1.

A ‘speciation’ event corresponds to a deep split in the viral phylogeny, with the $T_{M⁢R⁢C⁢A}$ growing without bounds, see Figure 1 and Figure 6A. This situation contrasts the phylogeny of the single competing population, where $T_{M⁢R⁢C⁢A}$ fluctuates with a characteristic ramp-like structure generated by stochastic extinction of one of the two oldest clades. In each such extinction event the MRCA jumps forward by $\delta⁢T$. Hence the probability of speciation depends on the probability of the two oldest clades to persist without extinction for a time long enough to accumulate antigenic divergence in excess of $d$. The combined carrying capacity of the resulting independent lineages is then twice their original carrying capacity as observed in simulations, see Figure 6B.

![Figure 6.](https://cdn.elifesciences.org/articles/44205/elife-44205-fig6-v2.jpg)

**Figure 6.:** (A) To speciate, two lineage have to diverge enough to substantially reduce cross-reactivity, that is $T$ needs to be comparable to $d$. Inset: Illustration of the definition of time to most recent common ancestor $T$ and the time interval $\delta⁢T$ by which $T$ advances. (B) If such speciation happens, the host capacity - the average number of infected individuals increases two-fold. (C) The probability of such deep divergences decreases exponentially with the ratio $d/q^{*}$, where effective antigenic diversity is $q^{*}=2⁢log⁡(N_{h}⁢s^{2})/log⁡(s/m)$. In the presence of deleterious mutations, the relevant $q$ is not necessarily the total advance of the pioneer strains, but only the antigenic contribution. This antigenic advance $q^{*}$ can be computed as $q^{*}=\sqrt{2⁢log⁡(N_{h}⁢s^{2})⁢\sigma_{a⁢g}^{2}}$ with antigenic variance $\sigma_{a⁢g}^{2}=\sigma^{2}-\sigma_{\beta}^{2}$, where $\sigma_{\beta}^{2}$ is fitness variance due to deleterious mutations. With this correction, speciation times agree with the predicted dependence (colored lines).

To gain better intuition into this process let’s follow two most antigenically advanced ‘pioneer strains’. In the TW approximation one of these will with high probability belong to the backbone giving the rise to the persisting clade, while the other clade will become extinct, unless it persist long enough to diverge antigenically beyond $d$, becoming a speciation event. As their antigenic distance gradually increases, the two clades are evolving to evade immunity built up against the common ancestor. The less advanced of the two clades is growing less rapidly and takes longer to generate antigenic advance mutations, resulting in still slower growth and slower antigenic advance. Deep splits are hence unstable and it is rare for a split to persist long enough for speciation. In Appendix 5, we reformulate this intuition mathematically as a ‘first passage’-type problem which shows that $T_{M⁢R⁢C⁢A}$ distribution has an exponential tail which governs the probability of speciation events. Figure 6C shows that the time to speciation increases approximately exponentially with the ratio $d/q$. More precisely we found that average simulated speciation time behaves as $\tau_{sw}^{*}⁢e^{f⁢(C⁢I/q^{*})}$ with ‘effective’ $\tau_{sw}^{*}=\tau_{sw}/(1+log⁡q/log⁡(s/m))$ and $q^{*}=q⁢(1+log⁡q/log⁡(s/m))$ picking up an additional logarithmic dependence on parameters, the exact origin of which is beyond our current approximations. This correction plausibly suggests rapid speciation, $\tau_{sw}^{*}→0$, when mutation rate become comparable to the selection strength $m/s→1$.

### Red Queen State is transient

We emphasize that the RQS regime in Figure 3BC is only transient. For any given $q$ and $d$, the RQS is likely to persist for a time given by the smaller of $\tau_{ext}$ and $\tau_{sp}$, before undergoing either extinction or speciation. These two processes limit the range of $q$ corresponding to the RQS from both sides in a time-dependent manner. Figure 7 shows the likely state of an RQS system after time $\tau$ as a function of genetic diversity $q$ for the case of $d=50$ and $log⁡(N_{h}⁢I¯)=6.5$.

![Figure 7.](https://cdn.elifesciences.org/articles/44205/elife-44205-fig7-v2.jpg)

**Figure 7.:** This schematic diagram based on Figure 5A defines the ‘boundaries’ of the transient RQS $q_{e⁢x⁢t}⁢(\tau)$ (red line) and $q_{s⁢p}⁢(\tau)$ (blue line). $q_{e⁢x⁢t}⁢(\tau)$ gives the value of $q$ for which the average time to extinction is equal to $\tau$ is defined similarly but for the speciation process. Average times to speciation and extinction become equal at the critical value $q_{c}$ at which RQS persists the longest. For $d=50$, $q_{c}≈2.4$ and this value, along with the RQS lifetime, increases with $d$.

The regime of a single persistent lineage shrinks with increasing $\tau$, for example after $\tau=10⁢\tau_{sw}$ the RQS state likely prevails between $q=1.5$ and $≈4$, while (for $d=50$ and $log⁡(N_{h}⁢I¯)=6.5$) it is unlikely to persist beyond $\tau≈100⁢\tau_{sw}$ for any $q$. Both the maximal RQS lifetime and corresponding critical $q_{c}$, increase with increasing $d$.

## Discussion

The epidemiological and evolutionary dynamics of human RNA viruses show a number of qualitatively distinct patterns (Grenfell et al., 2004; Koelle et al., 2011). Agents of classical childhood diseases like measles or mumps virus show little antigenic evolution, other viruses like dengue- or norovirus exist in distinct serotypes, while seasonal influenza viruses undergo continuous antigenic evolution enabling viruses of the same lineage to reinfect the same individual.

Here, we have integrated classical multi-strain SIR models with stochastic models of adaptation to understand the interplay between the epidemiological dynamics and the accumulation of antigenic novelty. The former is dominated by the most prevalent strains, while the latter depends critically on rare pioneer strains that become dominant at later times. Our model differs from that of Rouzine and Rozhnova (2018) in two aspects that are crucial to questions addressed here: To meaningfully study speciation and diversification, the model needs to allow for an high dimensional antigenic space. Similarly, fluctuations in pathogen population size determine the dynamics of extinction and this aspect can not be studied in models with constant population size. Including these aspects of the epi-evolutionary dynamics allowed to define a ‘phase’ diagram that summarizes qualitatively different behavior as a function of the relevant parameter combinations, see Figure 3B and C.

The phase diagram shows which combinations of key parameters lead to three distinct outcomes: (1) extinction (red), (2) an evolving but low diversity pathogen population (yellow and green), (3) a deeply branching and continuously diversifying pathogen population (blue). The key parameters are the size of the population $log⁡(N_{h}⁢s^{2})$, the ratio of mutational effects to mutation rate $log⁡(s/m)$, and the cross-immunity range $d$. In particular, large $d$ prevents speciation, while rapid mutation and large population sizes facilitate speciation.

In regime (2) of a low diversity but rapidly evolving pathogen population, incidence is determined by the range of cross-immunity $d$ and by the speed of antigenic evolution which itself depends on the pathogen population size, mutation rates, and the fitness effect of novel mutations. A consistent solution of these dependencies shows that average incidence $I_{t⁢o⁢t}$ decreases as $d^{-2}$, while weakly depending on population size and mutation rates (see Equation A2.11), consistent with results by Rouzine and Rozhnova (2018). Typical values of the coalescent time of influenza A (2-4y), an infectious period of 5d, and a human population size $∼10^{10}$ result in an average annual incidence of 3–10%. This number is consistent with previous estimates of the annual attack rate of influenza (Yang et al., 2015) (which typically do not differentiate the different influenza lineages).

Of the different regimes, only extinction (1) and speciation (3) are truly asymptotic. The intermediate regimes of continuously evolving low diversity pathogen population - the Red Queen State (RQS) - are strictly speaking metastable states which eventually either go extinct or undergo branching, but in a certain regime of parameters are very long lived. In our simple model, stability against speciation on the time scale $>10⁢\tau_{sw}$ required $d∼10⁢q$ (while stability against extinction requires $q>2$). These results are consistent with earlier studies that have shown that competition between lineages mediated by long-range cross-immunity can prevent diversification, effectively canalizing the population into a single lineage (Tria et al., 2005; Ferguson et al., 2003).

In practice, the range of cross-immunity required to prevent speciation might be smaller than the idealized model. Our model assumes that the pathogen population can escape immunity via many equivalent mutational path. But in reality, the number of path to escape will be limited and some path more accessible than others, which will reduce the tendency to speciate and the necessity for large $d$. Similarly, other factors such as population turn over and geographic heterogeneity can delay extinction.

Previous studies have shown that the rate of branching in the speciation regime increases with population size and mutation rate consistent with the phase diagram (Sasaki and Haraguchi, 2000; Koelle et al., 2011). Bedford et al. (2012) have used large-scale individual-based simulations to explore structure of influenza viruses phylogenies. Consistent with our results, they found that the speciation rate increases with the mutation rate (lowering $log⁡s/m$ and thereby facilitating speciation) and increasing standard deviation of mutational effects. The latter increases the typical antigenic effect of successful mutations, which decreases the radius of cross-immunity when measured in units of mutations making the population more prone to speciate.

Koelle and Rasmussen (2015) have implicated deleterious mutation load as a cause of spindly phylogenies. Deleterious mutations increase fitness variation, which results in more rapid coalescence and less antigenic diversity, which in turn reduces speciation rates. Our model can readily incorporate deleterious effects of antigenic mutations on transmission $\beta$. Such deleterious mutations reduce the selection coefficient of antigenic mutations, which in turn reduces the fitness variance $\sigma^{2}$, see Appendix 6. After subtracting the contribution of deleterious mutations from the the fitness variance, the times to speciation follow the predicted dependence on $q$ and $d$, see Figure 6C.

Outbreaks of emerging viruses that quickly infect a large fraction of the population, as for example the recent Zika virus outbreak in the Americas, fall into regime (1): In 2–3 years, large fractions of the population were infected and have developed long-lasting immunity. As far as we know, the viral population did not evolve antigenically to escape this build up of herd immunity and the virus population is not expected to continue to circulate in the Americas (O'Reilly et al., 2018).

Different influenza virus lineages, in contrast, persist in the human population, suggesting that they correspond to parameters that fall into the RQS region of the phase diagram. Furthermore, the different subtypes display quantitatively different circulation and diversity patterns that allow for a direct, albeit limited, comparison to theoretical models: subtype A/H1N1 circulated with interruption from 1918 to 2009, A(H2N2) circulated for about 10 years until 1968, A/H3N2 emerged in 1968 and is still circulating today, and the triple reassortant 2009 H1N1 lineage, called A(H1N1pdm), settled into a seasonal pattern following the pandemic in 2009. Influenza B viruses have split into two separate lineages (B/Victoria and B/Yamagata) in the 1970s (Rota et al., 1990). Phylogenetic trees of A/H3N2 and the influenza B lineages are shown in Figure 1.

The influenza B lineages tend to be more genetically diverse than the influenza A lineages with a typical time to the most recent common ancestor of around 6 compared to 3 years, see Figure 1. Influenza A/H3N2 tends to have the lowest diversity and most rapid population turnover. This difference in diversity is consistent with influenza B lineages being more prone to speciation.

The typical diversity of these viruses needs to be compared to their rate of antigenic evolution. Hemagglutination inhibition titers drop by about 0.7–1 log2 per year in A/H3N2 compared to 0.1–0.4 log2 per year for influenza B lineages (Smith et al., 2004; Bedford et al., 2014; Neher et al., 2016). Hence the ratio of the time required to lose immunity and $T_{M⁢R⁢C⁢A}$ is similar for the different lineages, suggesting that the distinct rates of genetic and antigenic evolution can not be used as a straight forward rationalization of the speciation event of Influenza B and the lack of speciation of influenza A lineages. Nor should such an explanation be expected as there is only a single observation of speciation. We note that currently circulating A/H3N2 viruses are exceptionally diverse with a common ancestor that existed about 8 years in the past. Furthermore, the cocirculating 3c.3a and 3c.2a are antigenically distinct and it is conceivable that further antigenic evolution will result in speciation of A/H3N2 viruses.

While we have shown that the natural tendency of SIR models to oscillate couples to the instability of the nose of the pathogen fitness distribution, making a quantitative link to the observed epidemiological dynamics of the flu is difficult on account of seasonal oscillation in transmissivity. The latter confounding factor is widely believed to be the cause behind observed seasonality of the flu. Including explicit temporal variation (in $\beta$) in our model would lock the frequency of the prevalence oscillation to the seasonal cycle, possibly resulting in subharmonic modulation, yet distinguishing such a modulation on top of an already stochastic process is hard. Much remains to be done: finite birth rates, distinct age distributions (as for example is the case for the two influenza B lineages), realistic distribution of antigenic effect sizes, or very long range T-cell-mediated immunity would all be interesting avenues for future work.

## Materials and methods

### Clone-based simulations

We simulate the original model on a genealogical tree by combining the deterministic update of SIR-type equations and the stochastic step introducing mutated strains. In each time step $Δ⁢t<1$, we apply the mid-point method to advance SIR equations Equations (1,2,4). We then generate a random number uniformly sampled between zero and one for each surviving strain with $N_{h}⁢I_{a}\geq1$. If the random number is smaller than $m⁢N_{h}⁢I_{a}⁢Δ⁢t$ for strain $a$, we append a new strain $b$ as a descendent to $a$. The susceptibility to strain $b$ is related to susceptibility to strain $a$ via $S_{b}=(S_{a})^{e^{-1/d}}$. In most of the simulations, the transmissibility of different strains is held constant $\beta$. Otherwise we allow for a strain specific transmissibility that is to its parent: $\beta_{b}=\beta_{a}-\delta⁢\beta$ with $\delta⁢\beta>0$ for the deleterious effect of antigenic mutations and $\beta_{b}=\beta_{max}$ if the mutation is compensatory. The new strain grows deterministically only if $\beta_{b}⁢S_{b}>1$.

This simplified model contains six relevant parameters: transmissibility $\beta$, recovery rate $ν$, mutation rate of the virus $m$, birth/death rate of the hosts $\gamma$, the effective cross-immunity range $d$, and the effective size of the hosts $N_{h}$, whose empirical ranges are summarized in the Table 1. For flu and other asexual systems in RQS, $\beta≳ν≫m,\gamma$, $d≫1$, and $N_{h}≫1$.

**Table 1.**
 Relevant quantities of influenza virus and parameters in multi-strain SIR model.


<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Definition</th>
      <th>Typical values for influenza</th>
      <th>Range in simulations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ia</td>
      <td>Fraction of population infected with strain a</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sa</td>
      <td>Population average susceptibility to strain a</td>
      <td>∼0.5</td>
      <td></td>
    </tr>
    <tr>
      <td>It⁢o⁢t=∑aIi</td>
      <td>Total prevalence</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>I¯</td>
      <td>Average total prevalence</td>
      <td>0.005</td>
      <td></td>
    </tr>
    <tr>
      <td>d</td>
      <td>Cross-immunity range</td>
      <td></td>
      <td>[50, 200]</td>
    </tr>
    <tr>
      <td>β=ν⁢R0</td>
      <td>Transmission rate</td>
      <td>∼0.5/day</td>
      <td>2</td>
    </tr>
    <tr>
      <td>ν</td>
      <td>Recovery rate</td>
      <td>∼0.2/day</td>
      <td>1 (sets unit of time)</td>
    </tr>
    <tr>
      <td>γ</td>
      <td>Host birth/death rate</td>
      <td>∼0.01/year</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Ka⁢b=e-|b-a|/d</td>
      <td>Cross-immunity of strains a, b</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>τsw</td>
      <td>Coalescent time scale/sweep time</td>
      <td>∼2-6 years</td>
      <td></td>
    </tr>
    <tr>
      <td>TM⁢R⁢C⁢A</td>
      <td>Time to most recent common ancestor</td>
      <td>∼2-10 years</td>
      <td></td>
    </tr>
    <tr>
      <td>δ⁢T</td>
      <td>Fluctuations of TM⁢R⁢C⁢A</td>
      <td>∼2-6 years</td>
      <td></td>
    </tr>
    <tr>
      <td>s</td>
      <td>Selection coefficient</td>
      <td>∼0.03/week</td>
      <td>[0.003, 0.05]</td>
    </tr>
    <tr>
      <td>m</td>
      <td>Beneficial mutation rate per genome</td>
      <td>10-3/week</td>
      <td>[10-7,10-3]</td>
    </tr>
    <tr>
      <td>Nh</td>
      <td>Host population</td>
      <td>1010</td>
      <td>[106, 1012]</td>
    </tr>
  </tbody>
</table>

Simulation code and output are available on github in repository FluSpeciation of the neherlab organization (Neher and Yan, 2019; copy archived at https://github.com/elifesciences-publications/FluSpeciation).

### Fitness-class-based simulations

The stability of the RQS and the extinction dynamics is fully captured by the traveling wave Equation (8). We simulate the traveling wave by discretizing the fitness space $x$ into bins of step size $s$ around zero. The number of individuals infected by different strains correspond to integers in each bin $x_{i}$. At each time step, the population in each bin $I_{i}$ updates to a number sampled from the Poisson distribution with parameter $\lambda_{i}=N_{h}⁢I_{i}⁢(1+(x_{i}-x¯)⁢Δ⁢t)$ determined by mean fitness $x_{i}$ and a dynamic mean fitness $x¯$, which increases by $Δ⁢t⁢I_{t⁢o⁢t}$, where $I_{t⁢o⁢t}$ is the total infected fraction summed over all bins. When $x¯$ becomes larger than one bin size $s$, we shift the all populations to left by one bin and reset $x¯$ to , a trick to keep only a finite number of bins in the simulation. At the same time, antigenic mutation is represented by moving the mutated fraction in each bin to the adjacent bin on the right. The fraction is determined by a random number drawn from the Poisson distribution with the mean $m⁢I_{i}⁢Δ⁢t$. The typical ranges of the three parameters $s$, $m$, and $N_{h}$ follow the parameters in the genealogical simulation, as documented also in Table 1.

### Stochastic differential-delay simulation

To simulate the differential delay equations Equations (11-13), we discretize time in increments of $Δ⁢t=\tau_{sw}/k$ and update the dynamical variables $χ_{i}=x_{n}⁢(t_{i})$ and $η_{i}=I_{t⁢o⁢t}⁢(t_{i})$ via the simple Euler scheme:

$$
χ_{i+1}=χ_{i}+Δt(χ_{i}−η_{i})+\frac{χ_{i}}{qs}\sqrt{Δt}ξ_{i};
$$



$$
η_{i+1}=I¯exp⁡(\tau_{sw}χ_{i−k}−\frac{\tau_{sw}^{2}}{k}\sumj=0kjη_{i−j}),
$$

where $ξ_{i}$ is a Gaussian random variable with zero mean and unit variance. Mean prevalence, $I¯$, enters as the control parameter (which defines the time average of $η_{i}$).

### Influenza phylogenies

Influenza virus HA sequences for the subtypes A/H3N2, A/H1N1, A/H1N1pdm, as well as influenza B lineages Victoria and Yamagata were downloaded from fludb.org.

We aligned HA sequences using mafft (Katoh et al., 2002) and reconstructed phylogenies with IQ-Tree (Nguyen et al., 2015). Phylogenies were further processed and time-scaled with the augur (Hadfield et al., 2018) and TreeTime (Sagulenko et al., 2018). The analysis pipeline and scripts are available on github in repository 2019_Yan_flu_analysis of the neherlab organization.
