# Nomadic-colonial life strategies enable paradoxical survival and growth despite habitat destruction

## Authors

- Zhi Xuan Tan<sup>1</sup>
- Kang Hao Cheong<sup>2</sup> ([ORCID: 0000-0002-4475-5451](https://orcid.org/0000-0002-4475-5451)) †

### Affiliations

1. Yale University New Haven United States
2. Engineering Cluster Singapore Institute of Technology Singapore

† Corresponding author

## Abstract

10.7554/eLife.21673.001 Organisms often exhibit behavioral or phenotypic diversity to improve population fitness in the face of environmental variability. When each behavior or phenotype is individually maladaptive, alternating between these losing strategies can counter-intuitively result in population persistence–an outcome similar to the Parrondo’s paradox. Instead of the capital or history dependence that characterize traditional Parrondo games, most ecological models which exhibit such paradoxical behavior depend on the presence of exogenous environmental variation. Here we present a population model that exhibits Parrondo’s paradox through capital and history-dependent dynamics. Two sub-populations comprise our model: nomads, who live independently without competition or cooperation, and colonists, who engage in competition, cooperation, and long-term habitat destruction. Nomads and colonists may alternate behaviors in response to changes in the colonial habitat. Even when nomadism and colonialism individually lead to extinction, switching between these strategies at the appropriate moments can paradoxically enable both population persistence and long-term growth. DOI: http://dx.doi.org/10.7554/eLife.21673.001

## Introduction

Behavioral adaptation and phenotypic diversity are evolutionary meta-strategies that can improve a population’s fitness in the presence of environmental variability. When behaviors or phenotypes are sufficiently distinct, a population can be understood as consisting of multiple sub-populations, each following its own strategy. Counter-intuitively, even when each sub-population follows a losing strategy that will cause it to go extinct in the long-run, alternating or reallocating organisms between these losing strategies under certain conditions can result in meta-population persistence, and hence, an overall strategy that wins (Williams and Hastings, 2011). Some examples include random phase variation (RPV) in bacteria across multiple losing phenotypes (Wolf et al., 2005; Kussell and Leibler, 2005; Acar et al., 2008), as well as the persistence of populations that migrate among sink habitats only (Jansen and Yoshimura, 1998; Roy et al., 2005; Benaïm and Schreiber, 2009).

These counter-intuitive phenomena are reminiscent of Parrondo’s paradox, which states that there are losing games of chance which can be combined to produce a winning strategy (Harmer and Abbott, 1999). The existence of a winning combination relies on the fact that at least one of the losing Parrondo games exhibits either capital-dependence (dependence upon the current amount of capital, an ecological analog of which is population size) or history-dependence (dependence upon the past history of wins or losses, or in an ecological context, growth and decline) (Parrondo et al., 2000; Harmer and Abbott, 2002). There have been many studies exploring the paradox (Cheong and Soo, 2013; Soo and Cheong, 2013, 2014; Abbott, 2010; Flitney and Abbott, 2003; Harmer et al., 2001), including a multi-agent Parrondo’s model based on complex networks (Ye et al., 2016) and also implications to evolutionary biology (Cheong et al., 2016; Reed, 2007; Wolf et al., 2005; Williams and Hastings, 2011). However, many biological studies which have drawn a connection to Parrondo games do not necessarily utilize capital-dependence or history-dependence in their models (Williams and Hastings, 2011). Furthermore, models of reversal behavior in ecological settings generally rely upon the presence of exogenous environmental variation (Jansen and Yoshimura, 1998; Roy et al., 2005; Benaïm and Schreiber, 2009; Wolf et al., 2005; Kussell and Leibler, 2005; Acar et al., 2008; Levine and Rees, 2004). Without exogenous variation, the paradoxes do not occur. The broader applicability of Parrondo’s paradox to ecological systems thus remains under-explored.

This lacuna remains despite the abundance of biological examples that exhibit history-dependent dynamics. The fitness of alleles may depend on the presence of genetic factors and epigenetic factors in previous generations (Reed, 2007). More generally, the fitness of any one gene can depend on the composition of other genes already present in a population, enabling the evolution of complex adaptations like multicellularity through ratcheting mechanisms (Libby and Ratcliff, 2014). Such mechanisms have recently been shown to help stabilize these complex adaptations (Libby et al., 2016). In ecological contexts, the storage effect can ensure that gains previously made in good years can promote persistence in less favorable times (Warner and Chesson, 1985; Levine and Rees, 2004). Species-induced habitat destruction or resource production can also have time-delayed effects on population growth, resulting in non-linear phenomena like punctuated evolution (Yukalov et al., 2009, 2014).

In this paper, we present a biologically feasible population model which exhibits counter-intuitive reversal behavior due to the presence of history-dependent and capital-dependent dynamics. Unlike most other studies, these dynamics do not rely upon the assumption of exogenous environmental variation. In our model, we consider a population that exists in two behaviorally distinct forms: as nomads, and as colonists. Numerous organisms exhibit analogous behavioral diversity, from slime moulds (amoeba vs. plasmodia) (Baldauf and Doolittle, 1997) and dimorphic fungi (yeast vs. hyphae) (Bastidas and Heitman, 2009) to jellyfish (medusae vs. polyps) (Lucas et al., 2012) and human beings. One model organism which exhibits this sort of behavior, to which our study might apply, is the amoeba Dictyostelium discoideum (Annesley and Fisher, 2009).

Nomads live relatively independently, and thus are unaffected by either competition or co-operation. Under poor environmental conditions, they are subject to steady extinction. Colonists live in close proximity, and are thus subject to both competitive and co-operative effects. They may also deplete the resources of the habitat they reside in over time, resulting in long-term death. However, if these organisms are endowed with sensors that inform them of both population density and the state of the colonial habitat, they can use this information to switch from one behavior to another. Significantly, we find that an appropriate switching strategy paradoxically enables both population persistence and long-term growth – an ecological Parrondo’s paradox.

## Population model

Two sub-populations comprise our model: the nomadic organisms, and the colonial ones. In a similar vein to habitat-patch models, organisms that exist in multiple sub-populations can be modelled as follows:(1)d⁢nid⁢t=gi⁢(ni)+∑jsi⁢j⁢nj-∑jsj⁢i⁢ni

where ni is the size of sub-population i, gi is the function describing the growth rate of ni in isolation, and si⁢j is the rate of switching to sub-population i from sub-population j. Population sizes are assumed to be large enough that Equation 1 adequately approximates the underlying stochasticity.

## Nomadism

Let n1 be the nomadic population size. In the absence of behavioral switching, the nomadic growth rate is given by(2)g1⁢(n1)=-r1⁢n1

where r1 is the nomadic growth constant. Nomadism is modelled as a losing strategy by setting −r1 < 0, such that n1 decays with time. In the context of Parrondo’s paradox, nomadism corresponds to the ‘agitating’ strategy, or Game A. Importantly, competition among nomads, as well as between nomads and colonists, is taken to be insignificant, due to the independence of a nomadic lifestyle.

## Colonialism

Colonial population dynamics will be modelled by the well-known logistic equation, with carrying capacity K, but with two important modifications.

Firstly, the Allee effect is taken into account. This serves two roles: it captures the cooperative effects that occur among colonial organisms, and it ensures that the growth rate is negative when the population falls below a critical capacity A. Let n2 be the colonial population size. In the absence of behavioral switching, the colonial growth rate is given by(3)g2(n2)=r2n2(n2min(A,K)−1)(1−n2K)

where r2 is the colonial growth constant. Setting r2>0, we have a positive growth rate when A<n2<K, and a negative growth rate otherwise. The min(A,K) term ensures that when K<A, g2 is always zero or negative, as would be expected.

Secondly, the carrying capacity K changes at a rate dependent upon the colonial population size, n2, accounting for the destruction of environmental resources over the long run.

The rate of change of K with respect to t is given by(4)d⁢Kd⁢t=α-β⁢n2

where α>0 is the default growth rate of K, and β>0 is the per-organism rate of habitat destruction. An alternative interpretation of this equation is that K, the short-term carrying capacity, is dependent on some essential nutrient in the environment, and that this nutrient is slowly depleted over time at a rate proportional to β⁢n2.

Let n*=αβ, the critical population level at which no habitat destruction occurs. d⁢Kd⁢t is zero when n2=n*, positive when n2<n∗, and negative when n2>n∗. n∗ can thus also be interpreted as the long-term carrying capacity. Clearly, if the long-term carrying capacity n*<A, the only stable point of the system becomes n2=0. Under this condition, colonialism is a losing strategy as well.

Note that g2 increases as K increases, and that K increases more quickly as n2 decreases. In the context of Parrondo’s paradox, colonialism can thus serve as a ‘ratcheting’ strategy, or Game B, because the rate of growth is implicitly dependent upon the colonial population in the past. Another way of understanding the ‘ratcheting’ behavior is through the lens of positive reactivity (Williams and Hastings, 2011; Hastings, 2001, 2004). In the short-term, n2=A is a positively reactive equilibrium, because small upwards perturbations of n2 away from A will result in rapid growth towards K before a slow decrease back down towards A.

## Behavioral switching

Organisms are able to detect the amount of environmental resources available to them, and by proxy, the carrying capacity of the population. Thus, they can undergo behavioral changes in response to the current carrying capacity.

Here, we model organisms that switch to nomadic behavior from colonial behavior when the carrying capacity is low (K < L1), and switch to colonial behavior from nomadic behavior when the carrying capacity is high (K > L2), where L1≤L2 are the switching levels. Let rs > 0 be the switching constant. Using the notation from Equation 1, switching rates can then be expressed as follows:(5)s12={rsif K < L10otherwises21={rsif K > L20otherwise

A variety of mechanisms might trigger this switching behavior in biological systems. For example, since the nomadic organisms are highly mobile, they could frequently re-enter their original colonial habitat after leaving it, and thus be able to detect whether resource levels are high enough for recolonization. It should also be noted that the decision to switch need not always be ‘rational’ (i.e. result in a higher growth rate) for each individual. Switching behavior could be genetically programmed, such that ‘involuntary’ individual sacrifice ends up promoting the long-term survival of the species.

## Reduced parameters

Without loss of generality, we scale all parameters such that α=β=1. Equation 4 thus becomes:(6)d⁢Kd⁢t=1-n2

Hence, n*=αβ=1. All other population sizes and capacities can then be understood as ratios with respect to this critical population size. Additionally, since β=1, r1, r2 and rs can be understood as ratios to the rate of habitat destruction. For example, if r2≫1, this means that colonial growth occurs much faster than habitat destruction. Time-scale separation between the population growth dynamics and the habitat change dynamics can thus be achieved by setting r1,r2≫1. Similarly, the separation between the behavioral switching dynamics and the population growth dynamics can be achieved by setting rs≫r1,r2.

## Results

Simulation results revealed population dynamics that could be categorized into the following regimes:

Importantly, there were conditions under which both sub-populations would go extinct in the absence of behavioral switching (regime 1a), but collectively survive if behavioral switching was allowed (regime 2b), thereby exhibiting Parrondo’s paradox. The following sections describe the listed regimes in greater detail, with a focus upon the regimes involved in the paradox. Figures generated via numerical simulation are provided as examples of behavior within each regime.

## Extinction in the absence of switching

As described earlier, both nomadic and colonial behaviors can be modelled as losing strategies given the appropriate parameters. Simulations across a range of parameters elucidated the conditions which resulted in extinction for both strategies.

![Figure 1.](https://cdn.elifesciences.org/articles/21673/elife-21673-fig1-v3.jpg)

**Figure 1.:** a) eventual extinction for both strategies vs (b) survival for the colonial strategy.Initial conditions for both are , n1=2, n2=2. Shared parameters are K=5, rs=0, r1=1. For (r2=10a), . For (A=1.001b), .A=0.5DOI: http://dx.doi.org/10.7554/eLife.21673.003

It is clear from Equation 2 that the growth rate of the nomadic population n1 is always negative, because of the restriction that r1 > 0. Hence, nomadism is always a losing strategy.

However, the conditions under which colonial behavior is a losing strategy are more complicated. Complex dynamics occur when the critical capacity A is just below 1 that can result in either survival or extinction. Nonetheless, it can be shown that when A > 1, extinction occurs (as in Figure 1a, and that survival is only possible when A is significantly less than 1 (as in Figure 1b). That is:(7)A>1(colonial extinction guaranteed)(8)A<1(colonial survival possible )

The intuition behind this is straightforward. Suppose that initially, A < n2 < K, so that the growth rate is positive. When A < 1, the colonial population n2 increases until it reaches the carrying capacity K, following which they converge in tandem until stabilizing at the critical population size, n2=K=1. However, when A > 1, n2=K=1 is no longer a stable equilibrium, since dn2/dt < 0 when n2 < A, resulting in the eventual extinction of the population. For a formal proof, refer to Theorem A.3.

## Survival through periodic alternation

We now restrict our analysis to the case where A > 1. Under this condition, both nomadism (Game A) and colonialism (Game B) are losing strategies when played individually. Paradoxically, it is possible to combine these two strategies through behavioral switching such that population survival is ensured, thereby producing an overall strategy that wins.

Simulation results over a range of parameters have predicted this paradoxical behavior, and also elucidated the conditions under which it occurs.

![Figure 2.](https://cdn.elifesciences.org/articles/21673/elife-21673-fig2-v3.jpg)

**Figure 2.:** a) extinction vs (b) survival.Initial conditions for both are , n1=2, n2=2. Shared parameters are K=5, rs=1000, r1=1. For (r2=10a), , L1=3. For (L2=4.5b), , L1=3.L2=4DOI: http://dx.doi.org/10.7554/eLife.21673.004

Conceptually, this paradoxical survival is possible because the colonial strategy, or Game B, is history-dependent. In particular, the colonial growth rate d⁢n2/d⁢t is dependent upon the carrying capacity K, which in turn is dependent upon previous levels of n2. Behavioral switching to a nomadic strategy decreases the colonial population size, allowing the resources in the colonial environment, represented by K, to recover. Switching back to a colonial strategy then allows the population to take advantage of the newly generated resources. Because switching occurs periodically, as can be seen in Figure 2b, it should be noted that the organisms need not even detect the amount of resources present in the environment to implement this strategy. A biological clock would be sufficient to trigger switching behavior.

The exact process by which survival is ensured can be understood by analysing the simulation results in detail. In the nomadic phase, the colonial population n2 is close to zero, the nomadic population n1 undergoes slow exponential decay, and the carrying capacity K undergoes slow linear growth. K increases until it reaches L2, which triggers the switch to colonial behavior.

The population thus enters the colonial phase. If the colonial population n2 exceeds the critical capacity A at this point, then n2 will grow until it slightly exceeds the carrying capacity K. Subsequently, n2 decreases in the tandem with K until K drops to L1, triggering the switch back to the nomadic phase. However, if n2 < A when the colonial phase begins, the colonial population goes extinct, as can be seen in Figure 2a. Hence, a basic condition for survival is that n2≥A at the start of each colonial phase.

This implies that, by the end of the nomadic phase, n1 needs to be greater by a certain amount than A as well. Otherwise, there will be insufficient nomads to form a colony which can overcome the Allee effect. Under the reasonable assumption that the rate of behavioral switching is much faster than either colonial or nomadic growth (rs≫r1,r2), it can be shown more precisely that at the end of the nomadic phase, n1 needs to be greater than a critical level B, which is related to A by the equation:(9)A=B−(1−B)W0(B1−BexpB1−B)

A full derivation is provided in the Appendix (Theorem A.4). Here, W0⁢(x) is the principal branch of the Lambert W function. Qualitatively speaking, B is a function of A on the interval (1,∞) that increases in an exponential-like manner, and that approaches 1 when A does as well. Thus, B≥A, as expected.

The greater the difference between the switching levels, the longer the nomadic phase will last, because it takes more time for K to increase to the requisite value for switching, L2. And the longer the nomadic phase lasts, the more n1 will decay. If, at the end of the nomadic phase, the value that n1 decays to happens to be less than B, then the population will fail to survive. It follows that there should be some constraint on the difference between the switching levels L1 and L2.

Under the same assumption that rs≫r1,r2, such a constraint can be derived:(10)L2 < L1+1r1ln⁡L1+W0(−L1e−L1)B

Survival is ensured given the following additional condition:(11)There exists t∗≥t0:n2(t∗)=K(t∗)≥L1

where t0 marks the start of an arbitrary colonial phase, and t* marks the time of intersection between n2 and K during that phase. In other words, n2 has to grow sufficiently quickly during the colonial phase such that it exceeds both K and L1 before switching begins. This can be seen occurring in Figure 2b. In accordance with intuition, numerical simulations predict that this occurs when the colonial growth constant is sufficiently large (r2≫r1), as can be seen in the Figures. (The Figures also show that r1 close to 1, but this is not strictly necessary.) Collectively, Equations 10–11 are sufficient conditions for population survival. Mathematical details are provided in the Appendix (Theorems A.5 and A.6).

Note that Equation 10 contains an implicit lower bound on L1. Since L2≥L1 by stipulation, we must have ln⁡[L1+W0(−L1e−L1)] > ln⁡ B for survival. The following bound is thus obtained:(12)L1 > BeBeB−1

On the other hand, under the assumptions made, there is no upper bound for L1, and hence no absolute upper bound for L2 either. This suggests that given a sufficiently well-designed switching rule, K can grow larger over time while ensuring population survival. Such a rule is investigated in the following section.

## Long-term growth through strategic alternation

Suppose that, in addition to being able to detect the colonial carrying capacity, nomads and colonists are able to detect or estimate their current population size. This might happen by proxy, by communication, or by built-in estimation of the time required for growth or decay to a certain population level. The following switching rule then becomes possible:(13)When n2=K, dn2/dt > 0, set L1=K, L2=∞When n1=B, dn1/dt < 0, set L2=K

That is, L1 is set to the carrying capacity K whenever n2 rises to K, resulting immediately in a switch to nomadic behavior, and that L2 is in turn set to K whenever n1 falls to B, resulting in an immediate switch to colonial behavior.

This switching rule is optimal according to several criteria. Firstly, by switching to nomadic behavior just as n2 reaches K, it ensures that d⁢n2/d⁢t≥0 for the entirety of the colonial phase. As such, it avoids the later portion of the colonial phase where K and n2 decrease in tandem, and maximizes the ending value n2. Consequently, it also maximizes the value of n1 at the start of each nomadic phase.

Furthermore, by switching to colonial behavior right when n1 decays to B, the rule maximizes the duration of the nomadic phase while ensuring survival. This in turn means that the growth of K is maximized, since the longer the nomadic phase, the longer that K is allowed to grow.

In fact, this switching rule is a paradigmatic example of how Parrondo’s paradox can be achieved. It plays Game A, the nomadic strategy, for as long as possible, in order to maximize K and hence the returns from Game B. And then it switches to Game B, the colonial strategy, only for as long as the returns are positive (dn2/dt > 0), thereby using it as a kind of ratchet.

Suppose that

![Figure 3.](https://cdn.elifesciences.org/articles/21673/elife-21673-fig3-v3.jpg)

**Figure 3.:** Initial conditions are , n1=0, n2=2. Parameters are K=5, A=1.001, L1=3, L2=4, rs=1000, r1=1.r2=10DOI: http://dx.doi.org/10.7554/eLife.21673.005

In the cases shown, long-term growth is achieved because K indeed grows more during each nomadic phase than it falls during the subsequent colonial phase. As can be seen from Figure 3a, this is, in turn, because the nomadic phase lasts much longer than the colonial phase, such that the amount of environmental destruction due to colonialism is limited. Simulation results predict that this generally occurs as long as the colonial growth rate is sufficiently large (r2≫r1).

An interesting phenomenon that can be observed from Figure 3b is how the nomadic population size n1, which peaks at the start of each nomadic phase, eventually exceeds the carrying capacity K, and then continues doing so by increasing amounts at each peak. This is, in fact, a natural consequence of the population model. When n2 grows large, the assumption that switching is much faster than colonial growth starts to break down. This occurs even though rs≫r2, due to the increasing contribution of the (n2A-1) factor in Equation 3.

The result is that when a large colonial population begins switching to nomadism, a significant number of colonial offspring are simultaneously being produced. These offspring also end up switching to a nomadic strategy, resulting in more nomadic organisms than there were colonial organisms before. A particularly pronounced example of this is shown in

![Figure 4.](https://cdn.elifesciences.org/articles/21673/elife-21673-fig4-v3.jpg)

**Figure 4.:** Figure 5 that shows the mechanism behind the spikes in .n1When  is large, switching takes longer, causing a drop in n2, and a large increase in K.n1DOI: http://dx.doi.org/10.7554/eLife.21673.006

![Figure 5.](https://cdn.elifesciences.org/articles/21673/elife-21673-fig5-v3.jpg)

**Figure 5.:** .t=10Initial conditions are , n1=0, n2=2. Parameters are K=5, A=1.001, rs=1000, r1=1.r2=10DOI: http://dx.doi.org/10.7554/eLife.21673.007

However, this same phenomenon also introduces a limiting behavior to the pattern of long-term growth. As Figure 5 shows, when the same simulation as in Figure 3a and b is continued to t=1000, peak levels of n1, n2 and K eventually plateau around t=650.

This occurs because sufficiently high levels of n2 cause a qualitative change in the dynamics of behavioral switching. Normally, switching to nomadic behavior starts when K falls below L1, and ends when K rises above it again. K rises towards the end of the switch, when n2 levels fall below the critical level of n*=1. But when n2 is sufficiently large, the faster production of colonial offspring drags out the duration of switching, as seen in Figure 4. The higher levels of n2, combined with the longer switching duration, causes an overall drop in K by the end of the switching period. Because the increase in K during the subsequent nomadic phase is unable to overcome this drop, K stops increasing in the long-run.

Nonetheless, it is clear that significant long-term gains can be achieved via the optimal switching rule. Under the conditions of fast colonial growth and even faster switching (rs≫r2≫r1≃1, as in Figures 3a–5), these gains are several orders of magnitude larger than the initial population levels, a huge departure from the long-term extinction that occurs in purely colonial or nomadic populations. Limiting behavior eventually emerges, but this is to be expected in any realistic biological system.

## Survival and growth under additional constraints

Our proposed model is convenient for the functional understanding of growth and survival, and can be easily modified for a variety of applications. Additional constraints can be imposed under which survival and long-term growth are still observed. For example, in many biological systems, the dynamics of habitat change might occur on a slower timescale than both colonial and nomadic growth (i.e.

![Figure 6.](https://cdn.elifesciences.org/articles/21673/elife-21673-fig6-v3.jpg)

**Figure 6.:** Parameters for (a) are , rs=10000, r1=10, r2=100,L1=3. For (L2=3.083b), , rs=100000, r1=100, r2=1000,L1=3. Shared parameters are L2=3.008, Kmax=20.A=1.001DOI: http://dx.doi.org/10.7554/eLife.21673.008

Another practical constraint that can be imposed is limiting the growth of the carrying capacity to some maximal value Kmax, capturing the fact that the resources in any one habitat do not grow infinitely large. This can be achieved by modifying Equation 6 as follows:(14)dKdt=(1−n2)(1−KKmax)

![Figure 7.](https://cdn.elifesciences.org/articles/21673/elife-21673-fig7-v3.jpg)

**Figure 7.:** Initial conditions are , n1=0, n2=2, shared parameters are K=5. For (A=1.001a), , Kmax=20, rs=1000, r1=1 (fast habitat change). For (r2=10b), , Kmax=7.5, rs=10000, r1=10 (slow habitat change).r2=100DOI: http://dx.doi.org/10.7554/eLife.21673.009

## Discussion

The results presented in this study demonstrate the theoretical possibility of Parrondo’s paradox in an ecological context. Many evolutionary strategies correspond to the strategies that we have termed here as ‘nomadism’ and ‘colonialism’. In particular, any growth model that is devoid of competitive or collaborative effects is readily captured by Equation 2 (nomadism), while any logistic growth model which includes both the Allee effect and habitat destruction can be described using Equations 3 and 4 (colonialism). Many organisms also exhibit behavioral change or phenotypic switching in response to changing environmental conditions. By incorporating this into our model, we have demonstrated that nomadic-colonial alternation can ensure the survival of a species, even when nomadism or colonialism alone would lead to extinction. Furthermore, it has been demonstrated that an optimal switching rule can lead to long-term population growth.

The switching rules which lead to survival and long-term growth are analogous to the periodic alternation between games that produces a winning expectation in Parrondo’s paradox. If one views the carrying capacity K as the capital of the population, then it is clear that Equation 5 is a capital-dependent switching rule. By setting the appropriate amounts of capital at which switching should occur, survival and growth can be achieved. Survival is achieved by ensuring that Game A, or nomadism, is never played beyond the point where extinction is inevitable, that is, the point where n1 falls below the critical level B. Long-term growth is additionally achieved by ensuring that Game B, or colonialism, is only played in the region where gains are positive, that is, when A < n2 < K such that dn2/dt > 0. The history-dependent dynamics of Game B are thus optimally exploited.

Several limitations of the present study should be noted. Firstly, the study only focuses on cases where nomadism and colonialism are individually losing strategies, despite the abundance of similar strategies that do not lose in the real world. This is because assuming individually losing strategies in fact leads to a stronger result – if losing variants of nomadism and colonialism can be combined into a winning strategy, it follows that non-losing variants can be combined in a similar way too (see Theorem A.7 in the Appendix).

Secondly, the population model does not encompass all variants of qualitatively similar behavior. For example, many other equations can be used to model the Allee effect (Boukal and Berec, 2002). Nonetheless, our proposed model is general enough that it can be adapted for use with other equations and be expected to produce similar results. Even the presence of the Allee effect is not strictly necessary, since the colonial population might die off at low levels because of stochastic fluctuations, rather than because of the effect. Theorem A.7 in the Appendix also demonstrates that paradoxical behavior can occur even without the Allee effect causing long-term death of the colonial population.

Thirdly, though it is trivially the case that pure nomadism and pure colonialism cannot out-compete a behaviorally-switching population, a more complex analysis of the evolutionary stability of behavioral switching is beyond the scope of this paper. Finally, spatial dynamics are not accounted for in this study. Exploring such dynamics is a goal for future work.

## Materials and methods

Numerical simulations were performed using code written in MATLAB (Source code 1) that relied on the ode23 ordinary differential equation (ODE) solver. ode23 is an implementation of an explicit Runge-Kutta (2,3) pair of Bogacki and Shampine. Simulations were performed with both behavioral switching turned off (rs=0) and turned on (rs > 0). The accuracy of the simulation was continually checked by repeating all results with more stringent tolerance levels, ensuring that the final simulated parameters did not change significantly (by less than 1%). Both the relative error tolerance and absolute error tolerance were determined to be 10-9.

In the case of complex switching rules like Equation 13 that required modifying differential equation parameters at specific time points, the Events option of MATLAB’s ODE solvers was used to detect when these points occurred. After each detection, the parameters were automatically modified as per the switching rule, and the simulation continued with the new parameters.

Broad regimes of model behavior were observed by running simulations across a wide range of parameters and initial conditions. General trends and conditions observed within each regime were formalized analytically, the details of which can be found in the Appendix. In these derivations, reasonable assumptions were made in order to make the model analytically tractable. In particular, it was assumed that the rate of behavioral switching was much faster than the rates of either colonial or nomadic growth (rs≫r1,r2), and that colonial growth rates were in turn much faster than the rate of habitat destruction (r2≫1). Initial conditions corresponding to unstable equilibria (e.g. n2=K=1 < A) were avoided as unrealistic.

## Conclusion

Our comprehensive model captures both capital and history-dependent dynamics within a realistic ecological setting, thereby exhibiting Parrondo's paradox without the need for exogenous environmental influences. The possibility of an ecological Parrondo’s paradox has wide-ranging applications across the fields of ecology and population biology. Not only could it provide evolutionary insight into strategies analogous to nomadism, colonialism, and behavioral diversification, it potentially also explains why environmentally destructive species, such as Homo sapiens, can thrive and grow despite limited environmental resources. By providing a theoretical model under which such paradoxes occur, our approach may enable new insights into the evolution of cooperative colonies, as well as the conditions required for sustainable population growth.
