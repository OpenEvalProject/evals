# Lotka-Volterra pairwise modeling fails to capture diverse pairwise microbial interactions

## Authors

- Babak Momeni<sup>1</sup> ([ORCID: 0000-0003-1271-5196](https://orcid.org/0000-0003-1271-5196)) †
- Li Xie<sup>2</sup> ([ORCID: 0000-0003-3397-2407](https://orcid.org/0000-0003-3397-2407))
- Wenying Shou<sup>2</sup> ([ORCID: 0000-0001-5693-381X](https://orcid.org/0000-0001-5693-381X)) †

### Affiliations

1. Department of Biology Boston College Chestnut Hill United States
2. Division of Basic Sciences Fred Hutchinson Cancer Research Center Seattle United States

† Corresponding author

## Abstract

10.7554/eLife.25051.001 Pairwise models are commonly used to describe many-species communities. In these models, an individual receives additive fitness effects from pairwise interactions with each species in the community ('additivity assumption'). All pairwise interactions are typically represented by a single equation where parameters reflect signs and strengths of fitness effects ('universality assumption'). Here, we show that a single equation fails to qualitatively capture diverse pairwise microbial interactions. We build mechanistic reference models for two microbial species engaging in commonly-found chemical-mediated interactions, and attempt to derive pairwise models. Different equations are appropriate depending on whether a mediator is consumable or reusable, whether an interaction is mediated by one or more mediators, and sometimes even on quantitative details of the community (e.g. relative fitness of the two species, initial conditions). Our results, combined with potential violation of the additivity assumption in many-species communities, suggest that pairwise modeling will often fail to predict microbial dynamics. DOI: http://dx.doi.org/10.7554/eLife.25051.001

## Introduction

Multispecies microbial communities are ubiquitous. Microbial communities are important for industrial applications such as cheese and wine fermentation (van Hijum et al., 2013) and municipal waste treatment (Seghezzo et al., 1998). Microbial communities are also important for human health: they can modulate immune responses and food digestion (Round and Mazmanian, 2009; Kau et al., 2011) during health and disease. Properties of the entire community (‘community properties’, e.g. species dynamics, ability to survive internal or external perturbations, and biochemical activities of the entire community) are influenced by interactions wherein individuals alter the physiology of other individuals (Widder et al., 2016). To understand and predict community properties, choosing the appropriate mathematical model to describe species interactions is critical.

A mathematical model ideally focuses only on details that are essential to community properties of interest. However, it is often unclear

![Figure 1.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig1-v3.jpg)

**Figure 1.:** (A) The mechanistic model (left) considers a bipartite network of species and chemical interaction mediators. A species can produce or consume chemicals (open arrowheads pointing towards and away from the chemical, respectively). A chemical mediator can positively or negatively influence the fitness of its target species (filled arrowhead and bar, respectively). The corresponding L-V pairwise model (right) includes only the fitness effects of species interactions, which can be positive (filled arrowhead), negative (bar), or zero (line terminus). (B) In the example here, species S releases chemical 1C, and 1C is consumed by species 1S and promotes 2S’s fitness. In the mechanistic model, the three equations respectively state that (1) 2S grows exponentially at a rate 1, (2) r10C is released by 1S at a rate 1 and consumed by βC1S1S with saturable kinetics (maximal consumption rate 2 and half-saturation constant αC1S2), and (3) KC1S2S’s growth (basal fitness 2) is influenced by r20C in a saturable fashion. In the pairwise model here, the first equation is identical to that of the mechanistic model. The second equation is similar to the last equation of the mechanistic model except that 1 and r21 together reflect how the density of K21S (1) affects the fitness of S1S in a saturable fashion. For all parameters with double subscripts, the first subscript denotes the focal species or chemical, and the second subscript denotes the influencer. Note that unlike in mechanistic models, we have omitted ‘2’ from subscripts in pairwise models (e.g. S instead of r21) for simplicity. In this example, both rS2S1 and r21 are positive.rS2S1DOI: http://dx.doi.org/10.7554/eLife.25051.003

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** (A) In a pairwise model of prey-predation proposed by Lotka and Volterra, predator reduces the fitness of prey, while prey stimulates the fitness of predator. Such dynamics can be easily simulated (Green and Shou, 2014). (B) Assuming random encounter between prey and predator, the pairwise model predicts oscillations in the prey and predator population sizes. (C) Similar oscillations have been qualitatively observed in natural populations of lynx (predator) and hare (prey), providing support for the usefulness of pairwise models. Picture is adapted from https://biologyeoc.wikispaces.com/PopulationChanges (BiologyEOC, 2016).DOI: http://dx.doi.org/10.7554/eLife.25051.004

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig1-figsupp2-v3.jpg)

**Figure 1—figure supplement 2.:** (A) Analytically deriving a pairwise model from a mechanistic model allows us to uncover approximations required for such a transformation (top). Alternatively (bottom), within a ‘training window’ of the mechanistic model population dynamics, we can numerically derive parameters for a pre-selected pairwise model such that it best fits the mechanistic model. We then quantify how well such a pairwise model matches the mechanistic model under conditions different from those of the training window. (B) A mechanistic model of three species interacting via two chemicals (left) can be translated into a pairwise model of three interacting species (center). S inhibits 1S and promotes 1S (via 2C). 1S promotes 2S and 2S (via 3C) as well as 2S (via removal of 1C). 1S promotes 3S (via removal of 1C) and inhibits 1S (via removal of 2C). Take interactions between 2S and 2S for example: the saturable L-V pairwise model will require estimating ten parameters (colored, right), some of which (e.g. 3 in this case) may be zero. (r33C) In the numerical method, the six monoculture parameters (, ri0, and rii, Kii = 2, 3; green and red) are first estimated from training window i (within a dilution cycle) of monoculture mechanistic models (top and middle). Subsequently, the four interaction parameters ( and T, , olive) can be estimated from the training window Kij of the T coculture mechanistic model (bottom). Parameter definitions are described in S +2S3Figure 1. Often in this work, pairwise model parameters that can be directly obtained from the mechanistic model (e.g. species basal fitness; ) are directly obtained from the mechanistic model (instead of being estimated). To estimate parameters, we use an optimization routine to minimize , the fold-difference (hatched area) between dynamics from a pairwise model (dotted lines) and the mechanistic model (solid lines) averaged over D¯ and species number T: N. Here D¯=1N∑i=1N[1T∫TDi(t)dt]=1N∑i=1N[1T∫T|log10(Si,pair(t)/Si,mech(t))|dt] and Si,pair are Si,mech calculated using pairwise and mechanistic models, respectively. Since species with densities below a set extinction limit, Si, are assumed to have gone extinct in the model, we set all densities below the extinction limit to Sext in calculating Sext to avoid singularities. D¯ outside the training window can be used to quantify how well the best-matching pairwise model predicts the mechanistic model. Unless otherwise stated, in all simulations to ensure that resources not involved in interactions are never limiting, a community is diluted back to its inoculation density whenever total population increases to a high-density threshold, mimicking turbidostat experiments. Too frequent dilutions will allow only small changes in population dynamics within a dilution cycle or time D¯, which is not suitable for estimating pairwise model parameters. Dilutions can sometimes violate conditions for convergence to reference dynamics (TFigure 3—figure supplement 4). Under most cases we have tested, small variations in dilution frequency do not affect our conclusions. See Methods-Summary of simulation files for relevant Matlab codes.DOI: http://dx.doi.org/10.7554/eLife.25051.005

L-V pairwise models are popular. L-V pairwise modeling has successfully explained the oscillatory dynamics of hare and its predator lynx (Figure 1—figure supplement 1) (Volterra, 1926; Wangersky, 1978; BiologyEOC, 2016). Pairwise models have also been instrumental in delineating conditions for multiple carnivores to coexist when competing for herbivores (MacArthur, 1970; Chesson, 1990). In both cases, mechanistic models and pairwise models happen to be mathematically equivalent for the following reasons. In the hare-lynx example, both species are also interaction mediators, and therefore pairwise and mechanistic models are identical. In the second example, if herbivores (mediators of competitive interactions between carnivores) rapidly reach steady state, herbivores can be mathematically eliminated from the mechanistic model to yield a pairwise model of competing carnivores (MacArthur, 1970; Chesson, 1990). Pairwise models are often used to predict how perturbations to steady-state species composition exacerbate or decline over time (May, 1972; Thébault and Fontaine, 2010; Mougi and Kondoh, 2012; Allesina and Tang, 2012; Suweis et al., 2013; Coyte et al., 2015). Although most work are motivated by contact-dependent prey-predation (e.g. hare-lynx) or mutualisms (e.g. plant-pollinator) where L-V models could be identical to mechanistic models, these work do not explicitly exclude chemical-mediated interactions where species are distinct from interaction mediators.

The temptation of using pairwise models is indeed high, including in microbial communities where many interactions are mediated by chemicals (Mounier et al., 2008; Faust and Raes, 2012; Stein et al., 2013; Marino et al., 2014; Coyte et al., 2015). Even though pairwise models do not capture the dynamics of chemical mediators, predicting species dynamics is still highly desirable in, for example, forecasting species diversity and compositional stability. For chemical-mediated interactions, L-V pairwise models are far easier to construct than mechanistic models for the following reasons. Mechanistic models would require knowledge of chemical mediators, which are often challenging to identify. Since chemical mediators are explicitly modeled, mechanistic models require more equations and parameters than their cognate pairwise models (Figure 1, Table). Pairwise model parameters are relatively easy to estimate using community dynamics or dynamics of monocultures and pairwise cocultures (Mounier et al., 2008; Stein et al., 2013; Guo and Boedicker, 2016). Consequently, pairwise modeling has been liberally applied to microbial communities.

L-V pairwise models have been criticized when applied to communities of more than two species (referred to as ‘multispecies communities’) (Levine, 1976; Tilman, 1987; Wootton, 1993, 2002; Werner and Peacor, 2003; Stanton, 2003; Schmitz et al., 2004). This is because a third species can influence interactions between a species pair (‘indirect interactions’), which sometimes violates the additivity assumption of pairwise models. For example, a carnivore can indirectly increase the density of a plant by decreasing the density of an herbivore (‘interaction chain’; ‘density-mediated indirect interactions’). A carnivore can also decrease how often an herbivore forages plants (‘interaction modification’, ‘trait-mediated indirect interactions’, or ‘higher order interactions’) (Vandermeer, 1969; Wootton, 1994; Billick and Case, 1994; Wootton, 2002). In interaction modification, foraging per herbivore decreases, whereas in interaction chain, the density of herbivores decreases. Interaction modification (but not interaction chain) violates the additivity assumption (Methods-Interaction modification but not interaction chain violates the additivity assumption) (Tilman, 1987; Wootton, 1994; Schmitz et al., 2004) and can cause the pairwise model to generate qualitatively wrong predictions. Indeed, pairwise models largely failed to predict biomass and species coexistence in three-species and seven-species plant communities (Dormann and Roxburgh, 2005), although reported failures of pairwise models could be due to limitations in data collection and analysis (Case and Bender, 1981; Billick and Case, 1994).

Here, we examine the universality assumption of pairwise models when applied to microbial communities (or any community that employs diverse chemical-mediated interactions). Microbes often influence other microbes in a myriad of fashions, via consumable metabolites, reusable signaling molecules, or a combination of chemicals (

![Figure 2.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig2-v3.jpg)

**Figure 2.:** Interactions can be intra- or inter-population. Examples are meant to be illustrative instead of comprehensive.DOI: http://dx.doi.org/10.7554/eLife.25051.006

Instead of investigating natural communities where interaction mechanisms can be difficult to identify, we use in silico communities. In these communities, two species interact via mechanisms commonly encountered in microbial communities, including growth-promoting and growth-inhibiting interactions mediated by reusable and consumable compounds (Figure 2) (Stams, 1994; Czárán et al., 2002; Duan et al., 2009). We construct mechanistic models for these two-species communities and attempt to derive from them pairwise models. A mechanistic reference model offers several advantages: community dynamics is deterministically known; deriving a pairwise model is not limited by inaccuracy of experimental methods; and the flexibility in creating different reference models allows us to explore a variety of interaction mechanisms. We demonstrate that a single pairwise equation form often fails for commonly-encountered diverse pairwise microbial interactions. We conclude by discussing when pairwise models might or might not be useful, in light of our findings.

## Results

Throughout this work, we consider communities grown in a well-mixed environment where all individuals interact with each other with an equal chance. A well-mixed environment can be found in industrial fermenters. Moreover, at a sufficiently small spatial scale, a spatially-structured environment can be approximated as a well-mixed environment, as chemicals are uniformly-distributed locally. Motile organisms also reduce the degree of spatial structure. A well-mixed environment allows us to use ordinary differential equations (ODEs), which are more tractable than partial differential equations demanded by a spatially-structured environment. This in turn allows us to sometimes analytically demonstrate failures of pairwise models.

## Mechanistic model versus pairwise model

A mechanistic model describes how species release or consume chemicals and how chemicals stimulate or inhibit species growth (Figure 1A left). In contrast, in pairwise models, interation mediators are not explicitly considered (Figure 1A right). Instead, the growth rate of an individual of species Si is the sum of its basal fitness (ri0, net growth rate of the individual in the absence of any intra-species or inter-species interactions) and fitness effects from intra-species and inter-species interactions. The fitness effect from species Sj to species Si is represented by fij(Sj), where Sj is the density of species Sj. fij(Sj) is a linear or nonlinear function of only Sj and not of another species. When j=i, fii(Si) represents density-dependent fitness effect within Si (e.g. density-dependent growth inhibition or stimulation).

In a multi-species pairwise model, a single form of fij is used for all pairwise species interactions. For example, the most popular L-V model is linear L-V:(1)dSidt=[ ri0+∑jrijSj ]Si

Here, ri0 is the basal fitness of an individual of Si, and can be positive, negative, or zero; rij is the fitness effect per Sj individual on Si. Positive, negative, or zero rij represents growth stimulation, inhibition, or no effect, respectively. An example of linear L-V is the logistic L-V pairwise model traditionally used for competitive communities:(2)dSidt=ri0[ 1−∑jSjΛij ]Si

Here, nonnegative ri0 is the basal fitness of Si; positive Λij is the carrying capacity imposed by limiting shared resource (e.g. space or carbon source) such that a single Si individual will have a zero net growth rate when competing with a total of Λij individuals of Sj.

Alternative forms of fitness effect fij (Wangersky, 1978) include L-V with delayed influence, where the fitness influence of one species on another may lag in time (Gopalsamy, 1992), or saturable L-V (Thébault and Fontaine, 2010) where(3)dSidt=[ ri0+∑jrijSjKij+Sj ]Si

Here, ri0 is the basal fitness of an individual of Si, rij is the maximal fitness effect species Sj can exert on Si, and Kij (>0) is the Sj at which half maximal fitness effect on Si is achieved. ri0 and rij can be positive, negative, or zero. Note that at a low concentration of influencer, the saturable form can be converted to a linear form.

Our goal is to test whether a single equation form of pairwise model can qualitatively predict dynamics of species pairs engaging in various types of interactions commonly found in microbial communities (e.g. Figure 2). To do so, we use a combination of analytical and numerical approaches (Figure 1—figure supplement 2). Analytically deriving a pairwise model from a mechanistic model not only reveals assumptions required to generate the pairwise model, but also alleviates any concern that we may have failed to identify the optimal pairwise model parameters. When interactions become more complex (e.g. involving multiple mediators), we take the numerical approach, which is typically used to infer pairwise models from experimental results (Pascual and Kareiva, 1996). In the numerical approach, we mimic experimentalists by first deciding on a pairwise model to be used, and then employing a nonlinear least squares routine to numerically identify model parameters that minimize the average difference D¯ between pairwise and mechanistic model dynamics within a training time window T (Figure 1—figure supplement 2; Methods-Summary of simulation files). To evaluate how well a pairwise model predicts long-term mechanistic model dynamics, we ‘buy time’ by introducing 'dilutions' in numerical simulations of both models and quantify their difference D¯.

## Reusable versus consumable mediators require different pairwise models

In this section, we analytically derive pairwise models from mechanistic models of two-species communities where one species affects the other species through a single mediator. The mediator is either reusable such as signaling molecules in quorum sensing (Duan et al., 2009; Jakubovics, 2010) or consumable such as metabolites (Stams, 1994; Freilich et al., 2011) (Figure 2). We show that a single pairwise model may not encompass these different interaction mechanisms and that for consumable mediator, the choice of pairwise model also depends on details such as the relative fitness and initial densities of the two species.

Consider a commensal community where species

![Figure 3.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig3-v3.jpg)

**Figure 3.:** S stimulates the growth of 1S via a reusable (2A) or a consumable (B) chemical C. In mechanistic models of the two cases (i), equations for 1 and S1 are identical but equations for S2 are different. In (C1A),  can be solved to yield C1, assuming zero initial C1=(βC1S1/r10)S10exp⁡(r10t)−(βC1S1/r10)S10=(βC1S1/r10)S1−(βC1S1/r10)S10. Here, C1 is S10 at time zero. We have approximated S1 by omitting the second term (valid after the initial transient response has passed so that C1 has become proportional to C1). This approximation allows an exact match between the mechanistic model and the saturable L-V pairwise model (S1ii). In (B), depending on the relative growth rates of the two species, and if additional requirements are satisfied (Methods; Figure 3—figure supplement 2; Figure 3—figure supplement 3; Figure 3—figure supplement 4; Figure 3—figure supplement 5), either saturable L-V or alternative pairwise model should be used.DOI: http://dx.doi.org/10.7554/eLife.25051.00710.7554/eLife.25051.008Figure 3—source data 1.Figure 3—figure supplement 1.DOI: http://dx.doi.org/10.7554/eLife.25051.00810.7554/eLife.25051.009Figure 3—source data 2.Figure 3—figure supplement 2 on interactions through a consumable mediator.DOI: http://dx.doi.org/10.7554/eLife.25051.00910.7554/eLife.25051.010Figure 3—source data 3.Figure 3—figure supplement 3 on conditions required for convergence of the alternative pairwise model.DOI: http://dx.doi.org/10.7554/eLife.25051.01010.7554/eLife.25051.011Figure 3—source data 4.Figure 3—figure supplement 4 on how dilution might affect the convergence of a pairwise model.DOI: http://dx.doi.org/10.7554/eLife.25051.011

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** (A) We use the mechanistic model for a reusable mediator to generate reference dynamics of , , and over 150 generations of community growth. Note that population fractions (instead of population densities) are plotted, which fluctuate less than the mediator concentration during dilutions. After an initial period of time, becomes proportional to (inset). The basal fitness of S and 1S in pairwise models are identical to those in mechanistic models, and here and (= 1, 2) are irrelevant due to the lack of intra-population interactions. We use every 10 community doublings (within a dilution cycle) of reference dynamics as training windows to numerically estimate best-matching saturable L-V pairwise model parameters and . Dashed and solid rectangles represent a training window before and after acclimation, respectively. (2B) Pairwise model parameters estimated after acclimation (e.g. solid rectangle) match their analytically-derived counterparts (black dotted lines) better than those estimated before acclimation (e.g. dashed rectangle). (C) A pairwise model generated from population dynamics before acclimation (top) predicts future reference dynamics less accurately than that generated after acclimation (bottom). (D) Quantification of the difference between pairwise and mechanistic models before (dashed) or after (solid) acclimation. All parameters are listed in Figure 3—source data 1.DOI: http://dx.doi.org/10.7554/eLife.25051.012

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** S releases a consumable metabolite 1C which stimulates 1S growth. In all panels, brown circles indicate the 2 and C1 (RS) of a community, and are separated by 1/4 of community doubling time. In the vicinity of the =S2/S1-zero-isocline (f) (blue line), can be eliminated to yield a pairwise model. (f=0A–D) When  (Methods-Deriving a pairwise model for interactions mediated by a single consumable mediator, Case II), a steady state (green circle) exists. Let us scale and against their respective steady state values to obtain rS2C1>r10−r20>0 and R^S. The C^1-zero-isocline (blue) and the steady state f (vertical solid line) divide the phase portrait into four regions (① to ④). (C^1=1A) The directions of movement are marked by grey arrowheads. According to the top portion of Equation 11,the right-hand side of Equation 14 is zero when . Since C^1=1 is an increasing function of C^1/(C^1+K^S2C1)=1/(1+K^S2C1/C^1), when C^1, C^1>1 > 0 (up arrows), and when dR^S/dt<1, C^1<0 (down arrows). From dR^S/dtEquation 15, above the -zero-isocline, f<0 (left arrows), while below the dC^1/dt-zero-isocline, f>0 (right arrows). Thus, the community moves toward the dC^1/dt-zero-isocline, and then moves slowly alongside (but not superimposing) the f-zero-isocline before reaching the steady state. fA–C respectively describe community dynamics trajectories from when  is large and when S10 (Case II-2), R^S(t=0)≈1 (Case II-1), or R^S(t=0)≫max(1,K^S2C1−1) (Case II-3). (R^S(t=0)≪1/(1+K^C1S2)D)  but R^S(t=0)≈1 is much smaller than that in S10A. In this case, instead of approaching the -zero-isocline quickly as in fA, the trajectory plunges sharply before moving toward the -zero-isocline. The black dotted line marks f, the asymptotic value of R^S=1/(1+K^C1S2)-zero-isocline. (fE–H) When  (Methods-Deriving a pairwise model for interactions mediated by a single consumable mediator, Case III), there is no steady state. r10−r20<0 approaches infinity and RS approaches 0. The black dotted line marks C1, the asymptotic value of RS=βC1S1/αC1S2-zero-isocline. fE, F, and G respectively describe community dynamics trajectories from  when C1=0 is large and when S10, RS(0)≈βC1S1/αC1S2 (Case III-1), and RS(0)≫βC1S1/αC1S2 (Case III-2). (RS(0)≪βC1S1/αC1S2H)  but RS(0)≫βC1S1/αC1S2 is much smaller than that in S10F. Note different axis scales in different figure panels. All parameters are listed in Figure 3—source data 2.DOI: http://dx.doi.org/10.7554/eLife.25051.013

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig3-figsupp3-v3.jpg)

**Figure 3—figure supplement 3.:** Here are the phase portraits of Equation 43. The olive vertical dotted lines correspond to , a singularity point when RS=−ω/ψ. (ω<0A) Case II (), rS2C1>r10−r20>0, ω=0.5. Regardless of initial , the solution converges to steady state (in agreement with the mechanistic model). (ψ=0.25B) Case II, , ω=−1. When ψ=1 (to the left of olive line), the alternative pairwise model falsely predicts extinction of RS(t=0)<−ω/ψS. (2C) Case III (), r10<r20, ω=0.8. Regardless of initial , the model predicts extinction of ψ=0.1S (in agreement with the mechanistic model). (1D) Case III (), r10<r20, ω=−9. When ψ=5 (to the left of olive line), the alternative pairwise model falsely predicts steady state coexistence of the two species. All parameters are listed in RS(t=0)<−ω/ψFigure 3—source data 3.DOI: http://dx.doi.org/10.7554/eLife.25051.014

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig3-figsupp4-v3.jpg)

**Figure 3—figure supplement 4.:** We consider commensalism through a consumable mediator, where the producer and the consumer could reach a steady state (Methods-Deriving a pairwise model for interactions mediated by a single consumable mediator, Case II). We choose a low consumption rate such that starting from equal proportions of producers and consumers, consumption can be neglected. (A) When the initial total population density is low (2 × 105 total cells/ml, and periodic 10x dilution maintains this low density), the community cannot approach the blue -zero-isocline in a reasonable time frame (brown trajectory in the phase space of  and C^1, the mediator concentration and the consumer-to-producer ratio normalized to their potential steady state values, respectively). As a result, growth and dilution lead to an alternate sustained cycle for the community (inset). (R^SB) In this case, accumulates proportionally to within each dilution cycle, and the ratio of to reaches a constant value (inset). (C) Since behaves as a reusable mediator and since the community remains far from the -zero-isocline, the use of the alternative pairwise model (dashed) is not justified. Instead, the saturable L-V pairwise model (dotted) provides a better approximation. (D) The same community at a higher initial total density (2 × 108 total cells/ml) approaches the blue -zero-isocline (brown trajectory in the phase space) after a few dilutions. (E) In the vicinity of the -zero-isocline, reaches its steady state value within each dilution cycle. (F) In this case, the alternative model produces a better approximation to the mechanistic model compared to a saturable L-V model. In (C) and (F), the saturable L-V model is fitted into dynamics of the reference model after 50 generations, whereas analytical formulas are used for the alternative pairwise model. All parameters are listed in Figure 3—source data 4.DOI: http://dx.doi.org/10.7554/eLife.25051.015

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig3-figsupp5-v3.jpg)

**Figure 3—figure supplement 5.:** S affects 1S via a single consumable mediator 2C where 1.C1(0)=0For details, see Methods. Here, . RS=S2/S1, S1(0), S2(0), and C1(0) are the initial values of the respective variables. (RS(0)A) The initial condition requirement for a pairwise model to converge to the mechanistic model. (B) The time scale required for convergence. Conditions on  are sufficient, but may not be necessary.S1(0)DOI: http://dx.doi.org/10.7554/eLife.25051.016

When C1 is reusable, the mechanistic model (Figure 3A,i) can be transformed into a saturable L-V pairwise model (compare Figure 3A,ii with Equation 3), especially after the concentration of the mediator (which is initially zero) has acclimated to be proportional to the producer population size (Figure 3A legend; Figure 3—figure supplement 1). This saturable L-V pairwise model is valid regardless of whether the producer coexists with the consumer, outcompetes the consumer, or is outcompeted by the consumer.

If C1 is consumable, different scenarios are possible (Figure 3B; Methods).

Case I: When supplier

![Figure 4.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig4-v3.jpg)

**Figure 4.:** Consider a commensal community with a consumable mediator C. (1A) The mediator accumulates without reaching a steady state within each dilution cycle as the consumer S gradually goes extinct (2Figure 3B, Case I). After a few tens of generations,  becomes proportional to its producer density C1 (inset in left panel). In this case, a saturable L-V (dotted) but not the alternative pairwise model (dashed) is suitable. All parameters are listed in S1Figure 4—source data 1. (B) The consumable mediator reaches a non-zero steady state within each dilution cycle (Figure 3B, Case II). From mechanistic dynamics where initial species ratio is 1, we use two training windows to derive saturable L-V (dotted) and alternative (dashed) pairwise models. We then use these pairwise models to predict dynamics of communities starting at two different ratios. The alternative model but not the saturable L-V predicts the mechanistic model dynamics. All parameters are listed in Figure 4—source data 2. Note that in all figures, population fractions (instead of population densities) are plotted, which fluctuate less during dilutions compared to mediator concentration.DOI: http://dx.doi.org/10.7554/eLife.25051.01710.7554/eLife.25051.018Figure 4—source data 1.Figure 4 on an interaction through a reusable mediator.DOI: http://dx.doi.org/10.7554/eLife.25051.01810.7554/eLife.25051.019Figure 4—source data 2.Figure 4 on an interaction through a consumable mediator.DOI: http://dx.doi.org/10.7554/eLife.25051.019

Case II: When S1 and S2 can coexist (the basal fitness of S1 is higher than the basal fitness of S2 but less than the maximal fitness of S2), a steady state solution for C1 and species ratio RS=S2/S1 exists (Figure 4B; Methods-Deriving a pairwise model for interactions mediated by a single consumable mediator Case II, Equation 11). To arrive at a pairwise model, we will need to eliminate C1 which is mathematically possible (i.e. after community dynamics converges to the ‘f-zero-isocline’ on the phase plane of mediator C1 and species ratio RS, as depicted by blue lines in Figure 3—figure supplement 2A–D). However, the derived pairwise model differs from the saturable L-V model:(4)dS2dt=r20S2+rS2C1S1ωS1+ψS2S2

where constants r20, rS2C1, and ω=1−KS2C1/KC1S2 can be positive, negative, or zero, and ψ =(KS2C1αC1S2)/(KC1S2βC1S1) is positive (see Figure 1 table for parameter definitions and see Equation 13 in Methods). We will refer to this equation as ‘alternative pairwise model’, although the fitness influence term is a function of both S1 and S2 instead of the influencer S1 alone as defined in the traditional L-V pairwise model.

Case III: When supplier S1 always grows slower than consumer S2, i.e. when the basal fitness of S1 (r10) is less than the basal fitness of S2 (r20), consumable C1 declines to zero concentration. This is because C1 is consumed by S2 whose relative abundance over S1 eventually exponentially increases at a rate of r20−r10. Similar to Case II, under certain conditions (i.e. after community dynamics converges to the f-zero-isocline as seen in Figure 3—figure supplement 2E–H), the alternative pairwise model (Equation 4) can be derived (Methods-Deriving a pairwise model for interactions mediated by a single consumable mediator, Case III).

For both Case II and Case III, we analytically demonstrate that in the absence of dilutions, alternative pairwise model dynamics can converge to mechanistic model dynamics (see Figure 3—figure supplements 3 and 5 for initial condition requirement and time scale of convergence). However, if initial S1 and S2 are such that the time scale of convergence is long compared to the duration of one dilution cycle (e.g. Figure 3—figure supplement 2C and G), then we will have to perform dilutions and the saturable L-V model can sometimes be more appropriate than the alternative model (Figure 3—figure supplement 4). Thus in these cases, whether a saturable L-V or an alternative model is more appropriate also depends on initial conditions.

The alternative model (Equation 4) can be further simplified to(5)dS2/dt=(r20+ρS1/S2)S2

if additionally, the half-saturation constant K for C1 consumption (KC1S2) is identical to that for C1’s influence on the growth of consumer (KS2C1), and if S2 has not gone extinct. This equation form has precedence in the literature (e.g. [Mougi and Kondoh, 2012]), where the interaction strength r21 reflects the fact that the consumable mediator from S1 is divided among consumer S2. Thus, we can regard the alternative model (Equation 4) or its simplified version (Equation 5) as a ‘divided influence’ model.

The saturable L-V model and the alternative model are not interchangeable (Figure 4). When a consumable mediator accumulates without reaching a steady state within each dilution cycle (Figure 4A left; inset: C1 eventually becomes proportional to S1), the saturable L-V model is predictive of community dynamics (Figure 4A right, compare dotted and solid lines). In contrast, predictions from the alternative pairwise model are qualitatively wrong (Figure 4A right, compare dashed and solid lines). When a consumable mediator eventually reaches a non-zero steady state within each dilution cycle (Figure 4B, black), could a saturable L-V model still work? The saturable L-V model derived from training window i (initial 10 generations) fails to predict species coexistence regardless of initial species ratios (Figure 4B left magenta box, compare solid with dotted). In comparison, the saturable L-V model derived from training window ii (at steady-state species ratio) performs better, especially if the starting species ratio is identical to that of the training dynamics (Figure 4B, top panel in right magenta box). However, at a different starting species ratio, the saturable L-V model fails to predict which species dominates the community (Figure 4B, bottom panel in right magenta box). In contrast, community dynamics can be described by the alternative pairwise model derived from either window i or ii (Figure 4B, compare dashed and solid lines in left and right magenta boxes).

We have shown here that even when one species affects another species via a single mediator, either a saturable L-V model or an alternative pairwise model may be appropriate. The appropriate model depends on whether the mediator is reusable or consumable, how fitness of the two species compare, and initial species densities (Figure 3; Figure 3—figure supplements 2–5). Choosing the wrong pairwise model generates qualitatively flawed predictions (Figure 4). Considering that reusable and consumable mediators are both common in microbial interactions, our results call for revisiting the universality assumption of pairwise modeling.

## Two-mediator interactions require pairwise models different from single-mediator interactions

A species often affects another species via multiple mediators (

![Figure 5.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig5-v3.jpg)

**Figure 5.:** (A) One species can affect another species via two reusable mediators, each with a different potency  where KCi is KCi (Methods-Conditions under which a saturable L-V pairwise model can represent one species influencing another via two reusable mediators). A low KS2Cir10/βCiS1 indicates a strong potency (e.g. high release of KCiC by iS or low 1 required to achieve half-maximal influence on CiS). (2B) Under what conditions can an interaction via two reusable mediators with saturable effects on recipients be approximated by a saturable L-V pairwise model? (C) A community where the success or failure of a saturable L-V pairwise model depends on initial conditions. Here, = 10KC13 cells/ml and = 10KC25 cells/ml. Community dynamics starting at low  (solid) can be predicted if the saturable L-V pairwise model is derived from reference dynamics starting at low (dotted). However, if we use a saturable L-V pairwise model derived from a community with high initial S1, prediction is qualitatively wrong (dash dot line). See S1Figure 5—figure supplement 1D for an explanation why a saturable L-V pairwise model estimated at one community density may not be applicable to another community density. Simulation parameters are listed in Figure 5—source data 1 .DOI: http://dx.doi.org/10.7554/eLife.25051.02010.7554/eLife.25051.021Figure 5—source data 1.Figure 5 on an interaction through two concurrent mediators.DOI: http://dx.doi.org/10.7554/eLife.25051.02110.7554/eLife.25051.022Figure 5—source data 2.Figure 5—figure supplement 1 on an interaction through two concurrent mediators, assessed at high versus low cell densities.DOI: http://dx.doi.org/10.7554/eLife.25051.022

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** (A) Consider the interaction in Figure 5. The fitness effect of S on 1S via 2C and 1C is 2. (rS2,C1C2=rS2C1S1S1+KS2C1r10/βC1S1+rS2C2S1S1+KS2C2r10/βC2S1=rS2C1S1S1+KC1+rS2C2S1S1+KC2B–C) Under special conditions the fitness effect  (magenta line) can be approximated using a single saturable L-V model (grey dash-dot line) at all densities. These special conditions include when the potencies of two mediators,rS2,C1C2  and KC1, are similar (KC2B) or the potency of one mediator is orders of magnitude stronger than the other (C). Otherwise, saturable L-V pairwise models derived from a low-density community and from a high-density community can have qualitatively different parameters (D). Let’s first consider the low-density case (left black and blue bars corresponding to low total density and therefore low , respectively). When  (magenta line) is above the (rS2,C1C2) line (grey dashed line), the fitness of r10−r20S (2) will be higher than the fitness of rS2,C1C2+r20S. Thus, even though 1S grows at its basal fitness during a dilution cycle, 1S fraction will decrease. Thus 1 will decrease at the next dilution cycle when total density is reset to a pre-fixed level (arrow pointing towards lower S1). In contrast, when S1, rS2,C1C2<r10−r20S population fraction and 1 will increase at the next dilution cycle (arrow pointing towards higher S1). Thus, the dynamics will converge to a steady state ratio (filled dot). Interaction coefficient of a saturable L-V (grey dash-dot line) is estimated to be a positive value ( =+0.039). In contrast, in the high-density case (right black and blue bars), S1, and r10>rS2,C1C2+r20S goes extinct. Interaction coefficient of a saturable L-V (grey dash-dot line) is estimated to be a negative value ( = −0.010). As a result, a saturable L-V pairwise model with parameters estimated at high densities cannot predict communities at low densities (2Figure 5). All parameters are listed in Figure 5—source data 2.DOI: http://dx.doi.org/10.7554/eLife.25051.023

We assume that fitness effects from different chemical mediators on a focal species are additive. Not making this assumption will likely violate the additivity assumption essential to pairwise models. Additive fitness effects have been observed for certain ‘homologous’ metabolites. For example, in multi-substrate carbon-limited chemostats of E. coli, the fitness effects from glucose and galactose were additive (Lendenmann and Egli, 1998). ‘Heterologous’ metabolites such as carbon and nitrogen sources likely affect cell fitness in a multiplicative fashion. However, if WC and WN, the fitness influences of released carbon and nitrogen with respect to those already in the environment, are both small (i.e. WC, WN< < 1), the additional relative fitness influence will be additive: (1+WC)(1+WN)−1≈WC+WN. However, we need to keep in mind that even among homologous metabolites, fitness effects may not be additive (Hermsen et al., 2015). ‘Sequential’ metabolites (e.g. diauxic shift) provide another example of non-additivity. Similar to the previous section, we assume that all abiotic resources are unlimited.

For the two reusable mediators, depending on their relative ‘potency’ (defined in Figure 5A legend), their combined effect generally cannot be modeled as a single mediator except under special conditions (Methods-Conditions under which a saturable L-V pairwise model can represent one species influencing another via two reusable mediators). These special conditions include: (1) mediators share similar potency (Figure 5—figure supplement 1B), or (2) one mediator dominates the interaction (Figure 5—figure supplement 1C). If these conditions are not satisfied, we can easily find examples where saturable L-V pairwise models derived from a low-density community and from a high-density community have qualitatively different parameters (Figure 5—figure supplement 1D). Consequently, the future dynamics of a low-density community can be predicted by a saturable L-V model derived from a low-density community but not by a model derived from a high-density community (Figure 5C). Thus, even though each mediator can be modeled by saturable L-V, their joint effects may or may not be modeled by saturable L-V depending on the relative potencies of the two mediators and sometimes even on initial conditions (high or low initial S1).

Similarly, when both mediators are consumable and do not accumulate (as in Cases II and III of Figure 3B), the fitness effect term becomes rS2C1S1ωC1S1+ψC1S2+rS2C2S1ωC2S1+ψC2S2. Except under special conditions (e.g. when ωC1 and ωC2 are zero, or when ωC1/ωC2=ψC1/ψC2, or when one mediator dominates the interaction), the two mediators may not be regarded as one. By the same token, when one mediator is a steady-state consumable and the other is reusable, they generally may not be regarded as a single mediator and would require yet a different pairwise model (i.e. with the fitness effect term rS2C1S1ωC1S1+ψC1S2+rS2C2S1S1+KS2C2r10/βC2S1).

In summary, when S1 influences S2 through multiple mediators, rarely can we approximate them as a single mediator. Sometimes, a pairwise model derived from one community may not apply to communities initiated at different densities (Figure 5C; Figure 5—figure supplement 1D). This casts further doubt on the usefulness of a single pairwise model for all pairwise microbial interactions.

## L-V competition model can fail if two competing species engage in an additional interaction

So far, by assuming that abiotic resources are always present in excess (e.g. in turbidostats), we have not considered species competition for abiotic resources. In this section, we consider a competitive commensal community in a batch environment where

![Figure 6.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig6-v3.jpg)

**Figure 6.:** (A) Left: Two species S and 1S compete for shared resource 2C. Additionally, 1S produces 1C that promotes the growth of 2S upon consumption. Right: An L-V pairwise model captures the intra- and inter-species competition as well as the commensal interaction between the two species. (2B,C) Examples where L-V pairwise models predict the mechanistic reference dynamics well. (D) An example where the L-V pairwise model fails to predict the dynamics qualitatively (note the much longer time range). Here, population fractions fluctuate due to changes in relative concentration of C compared to 1C. In all cases, the pairwise model is derived from the population dynamics in the initial stages of growth (150 hr in all cases). Simulation parameters are listed in 2Figure 6—source data 1.DOI: http://dx.doi.org/10.7554/eLife.25051.02410.7554/eLife.25051.025Figure 6—source data 1.Figure 6 on an interaction through a consumable mediator, for species consuming a shared abiotic resource.DOI: http://dx.doi.org/10.7554/eLife.25051.025

In our mechanistic model (Methods-Competitive commensal interaction, Equation 47), the fitness of S2 is multiplicatively affected by C1 and C2 (Mankad and Bungay, 1988). We choose parameters such that the effect from C2 to S2 is far from saturation (e.g. linear with respect to C2 and S1) to simplify the problem. In our L-V pairwise model (Figure 6A, right; Methods-Competitive commensal interaction, Equation 48), intra- and inter-species competition is represented by the traditional logistic L-V model (Equation 2; Gause, 1934; Thébault and Fontaine, 2010; Mougi and Kondoh, 2012). We then introduce a linear term (r21S1) to describe the fitness effect of commensal interaction.

We tested various sets of mechanistic model parameters where the two species coexist in a steady fashion (Figure 6B), or one species goes extinct (Figure 6C), or species composition fluctuates (Figure 6D). L-V pairwise models deduced from a fixed period of training time could predict future dynamics in the first two cases, but failed to do so in the third case. Thus, depending on dynamic details of communities, a pairwise model sometimes works and sometimes fails.

To summarize our work, even for pairwise microbial interactions, depending on interaction mechanisms (reusable versus consumable mediator, single mediator versus multiple mediators), we will need to use a plethora of pairwise models to avoid qualitative failures in predicting which species dominates a community or whether species coexist (

![Figure 7.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig7-v3.jpg)

**Figure 7.:** We examine three-species communities engaging in indirect interactions. Each species pair is representable by a two-species pairwise model (saturable L-V or alternative pairwise model, purple in the right columns of B, D, and F). We then use these two-species pairwise models to construct a three-species pairwise model, and test how well it predicts the dynamics known from the mechanistic model. In B, D, and F, left panels show dynamics from the mechanistic models (solid lines) and three-species pairwise models (dotted lines). Right panels show the difference metric . (D¯A–B) Interaction chain: S affects 1S, and 2S affects 2S. The two interactions employ independent mediators 3C and 1C, and both interactions can be represented by the saturable L-V pairwise model. The three-species pairwise model matches the mechanistic model in this case. Simulation parameters are provided in 2Figure 7—source data 1. (C–F) Interaction modification. In both cases, the three-species pairwise model fails to predict reference dynamics even though the dynamics of each species pair can be represented by a pairwise model. (C–D) S consumes 3C, a mediator by which 1S stimulates 1S. Parameters are listed in 2Figure 7—source data 2. Here, S changes the nature of interaction between 1S and 2S and 3: S2S do not interact in the absence of 3S, but 1S inhibits 3S in the presence of 2S. The three-species pairwise model makes qualitatively wrong prediction about species coexistence. As expected, if 1S does not remove 3C, the three-species pairwise model works (1Figure 7—figure supplement 1A–B). (E–F) S and 1S both supply 3C which stimulates 1S. Here, no species changes ‘the nature of interactions’ between any other two species: both 2S and 1S contribute reusable 3C to stimulate 1S promotes 2. S1S regardless of 2S promotes 3; S3S regardless of 2S and 1; S1S do not interact regardless of 3S. However, a multispecies pairwise model assumes that the fitness effects from the two producers on 2S will be additive, whereas in reality, the fitness effect on 2S saturates at high . As a result, the three-species pairwise model qualitatively fails to capture relative species abundance. As expected, if 2C affects 1S in a linear fashion, the community dynamics is accurately captured in the multispecies pairwise model (2Figure 7—figure supplement 1C–D). Simulation parameters are listed in Figure 7—source data 3.DOI: http://dx.doi.org/10.7554/eLife.25051.02610.7554/eLife.25051.027Figure 7—source data 1.Figure 7B on interaction between three species in a chain.DOI: http://dx.doi.org/10.7554/eLife.25051.02710.7554/eLife.25051.028Figure 7—source data 2.Figure 7D on interaction modification through consumption of a shared mediator by a third species.DOI: http://dx.doi.org/10.7554/eLife.25051.02810.7554/eLife.25051.029Figure 7—source data 3.Figure 7F on interaction modification through production of a shared mediator by a third species.DOI: http://dx.doi.org/10.7554/eLife.25051.02910.7554/eLife.25051.030Figure 7—source data 4.Figure 7—figure supplement 1B on an interaction between three species through a shared reusable mediator affecting multiple species.DOI: http://dx.doi.org/10.7554/eLife.25051.03010.7554/eLife.25051.031Figure 7—source data 5.Figure 7—figure supplement 1D on an interaction between three species through a shared reusable mediator produced by multiple species.DOI: http://dx.doi.org/10.7554/eLife.25051.031

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig7-figsupp1-v3.jpg)

**Figure 7—figure supplement 1.:** (A–B) As a control for Figure 7C, if S does not remove the mediator of interaction between 3S and 1S, a three-species pairwise model accurately matches the mechanistic model. Simulation parameters are provided in 2Figure 7—source data 4. (C–D) As a control for Figure 7E, we ensured that fitness effects from multiple species are additive. In this case, a three-species pairwise model can represent the mechanistic model. To ensure the linearity and additivity of fitness effects, we have used a larger value of half saturation concentration (=10KS2C13 μM, instead of 10−1 μM in Figure 7E–F). We have adjusted the interaction coefficients accordingly such that the overall interaction strength exerted by S and 1 on S3S is comparable to that in 2Figure 7E–F (as evident by comparable population compositions). Since the interaction influences under these conditions remain in the linear range, the three-species pairwise model accurately predicts the reference dynamics. Simulation parameters are provided in Figure 7—source data 5.DOI: http://dx.doi.org/10.7554/eLife.25051.032

## Discussions

Multispecies pairwise models are widely used in theoretical ecology due to their simplicity. These models assume that all pairwise species interactions can be captured by a single pairwise model regardless of interaction mechanisms or quantitative details of a community (universality assumption). This assumption may be satisfied if, for example, interaction mediators are always species themselves (e.g. prey-predation in a food web) so that pairwise models are equivalent to mechanistic models. However, interactions in microbial communities are diverse and often mediated by chemicals (Figure 2). Here, we consider the validity of universality assumption of pairwise models in well-mixed, two-species microbial communities. We have focused on various types of chemical-mediated interactions commonly encountered in microbial communities (Figure 2) (Kato et al., 2005; Gause, 1934; Ghuysen, 1991; Jakubovics et al., 2008; Chen et al., 2004; D'Onofrio et al., 2010; Johnson et al., 1982; Hamilton and Ng, 1983). For each type of species interaction, we construct a mechanistic model to generate reference community dynamics (akin to experimental results). We then attempt to derive the best-matching pairwise model and ask how predictive it is.

We first consider cases where abiotic resources are in excess. When one species affects another species via a single chemical mediator, either the saturable L-V or the alternative pairwise model is appropriate, depending on the interaction mechanism (consumable versus reusable mediator), relative fitness of the two species, and initial conditions (Figure 3; Figure 3—figure supplement 2 to Figure 3—figure supplement 5). These two models are not interchangeable (Figure 4). If one species influences another species through multiple mediators, then in general, these mediators may not be regarded as a single mediator nor representable by a single pairwise model. For example, for two reusable mediators, unless their potencies are similar or one mediator is much more potent than the other, saturable L-V model parameters can qualitatively differ depending on initial community density (Figure 5—figure supplement 1D). Consequently, a pairwise model derived from a high-density community generates false predictions for low-density communities (Figure 5C), limiting the usefulness of pairwise models. We then consider a community where two species compete for a shared resource while engaging in commensalism via a single chemical mediator. We find that the best-fitting L-V pairwise model can predict future dynamics in some but not all communities, depending on parameters used in the mechanistic model (Figure 6). Thus, although a single equation form can work in many cases, it generates qualitatively wrong predictions in many other cases.

In communities of more than two microbial species, indirect interactions via a third species can occur. When indirect interactions take the form of interaction chains, if each chain segment of two species engages in an independent interaction and can be represented by a pairwise model, then multispecies pairwise models can work (Figure 7A-B). However, as discussed above, pairwise equation forms may vary among chain segments depending on interaction mechanisms and quantitative details of a community. When indirect interactions take the form of interaction modification, even if each species pair can be accurately represented by a pairwise model, a multispecies pairwise model may fail (Figure 7C–F, ). Interaction modification includes trait modification (Wootton, 2002; Werner and Peacor, 2003; Schmitz et al., 2004), or, in our cases, mediator modification. Mediator modification is very common in microbial communities. For example, antibiotic released by one species to inhibit another species may be inactivated by a third species, and this type of indirect interactions can stabilize microbial communities (Kelsic et al., 2015; Bairey et al., 2016). As another example, interaction mediators are often generated by and shared among multiple species. For example in oral biofilms, organic acids such as lactic acid are generated from carbohydrate fermentation by many species (Bradshaw et al., 1994; Marsh and Bradshaw, 1997; Kuramitsu et al., 2007). Such by-products are also consumed by multiple species (Kolenbrander, 2000).

One can argue that an extended pairwise model (e.g. dS2dt=r20S2+rS2CS1ς+ωS1+ψS2S2) embodying both the saturable form and the alternative form can serve as a general-purpose model at least for pairwise interactions via a single mediator. In fact, even the effects of indirect interactions may be quantified and included in the model by incorporating higher-order interaction terms (Case and Bender, 1981; Worthen and Moore, 1991), although with many challenges (Wootton, 2002). In the end, although these strategies may lead to a sufficiently accurate phenomenological model especially within the training window, they may fail to predict future dynamics.

When might a pairwise model be useful? First, pairwise models have been instrumental in understanding ecological phenomena such as prey-predator oscillatory dynamics and coexistence of competing predator species (Volterra, 1926; MacArthur, 1970; Case and Casten, 1979; Chesson, 1990). In these cases, mechanistic models are either identical to pairwise models or can be transformed into pairwise models under simplifying assumptions. Second, pairwise models of pairwise species interactions can provide a bird’s-eye view of strong or weak stimulatory or inhibitory interactions in a community. For example, Vetsigian et al., 2011 found that interactions between soil-isolated Streptomyces strains are enriched for reciprocity – if A inhibits or promotes B, it is likely that B also inhibits or promotes A (Vetsigian et al., 2011). Third, pairwise models have been useful in qualitatively understanding species assembly rules in small communities (Friedman et al., 2017). That is, qualitative information regarding species survival in competitions among a small number of species may be used to predict survival in more diverse communities within a similar time window. Fourth, a pairwise model can serve as a starting point for generating hypotheses on species interactions (e.g. Li et al., 2015). Note that when applied to microbial communities (Mounier et al., 2008; Stein et al., 2013; Marino et al., 2014), a fitting pairwise model means that the training dynamics of the community under investigation can be approximated by a theoretical community where species interactions satisfy the additivity and universality assumptions of pairwise models. Even though the theoretical community is likely different from the real community, hypothesis formulation can still be valuable. Finally, pairwise models can be useful in making predictions of limited scales. For example, Stein et al. used 2/3 of community dynamics data as a training set to derive a multispecies pairwise model, and in the best-case scenario, the model generated reasonable predictions on the remaining 1/3 of data (Stein et al., 2013). However, as we have shown, pairwise models can generate qualitatively wrong predictions (Figures 4–7), especially if interaction mechanisms are diverse such as in microbial communities. Not surprisingly, predicting qualitative consequences of species removal or addition using a pairwise model has encountered difficulties, especially in communities of more than three species (Mounier et al., 2008; Friedman et al., 2017).

An alternative to a pairwise model is a mechanistic model. How much information about interaction mechanisms do we need to construct a mechanistic model? That is, what is the proper level of abstraction which captures the phenomena of interest, yet avoids unnecessary details (

![Figure 8.](https://cdn.elifesciences.org/articles/25051/elife-25051-fig8-v3.jpg)

**Figure 8.:** How one species (S) may influence another (1S) can be mechanistically modeled at different levels of abstraction. For simplicity, here we assume that interaction strength scales in a linear (instead of saturable) fashion with respect to mediator concentration or species density. The basal fitness of 2S is zero. (2A) In the simplest form, S stimulates 1S in an L-V pairwise model. (2B) In a mechanistic model, we may realize that S stimulates 1S via a mediator 2C which is consumed by S. The corresponding mechanistic model is given. (2C) Upon probing more deeply, it may become clear that S stimulates 1S via an enzyme 2E, where E degrades an abundant precursor (such as cellulose) to generate mediator C (such as glucose). In the corresponding mechanistic model, we may assume that E is released by S at a rate 1 and that ζES1E liberates C at a rate . (ηCED) If instead E is anchored on the cell surface (e.g. cellulosome), then  is proportional to E. If we substitute S1E into the second equation, then (B) and (D) become equivalent. Thus, when enzyme is anchored on cell surface but not when enzyme is released, the mechanistic knowledge of enzyme can be neglected.DOI: http://dx.doi.org/10.7554/eLife.25051.033

In summary, under certain circumstances, we may already know that microbial interaction mechanisms fall within the domain of validity for a particular pairwise model. In these cases, a pairwise model provides the appropriate level of abstraction, and constructing such a pairwise model is much easier than a mechanistic model (Figure 1). However, if we do not know whether a pairwise model is valid, we will need to be cautious since pairwise models can fail to even qualitatively capture pairwise microbial interactions. We need to be equally careful when extrapolating and generalizing conclusions obtained from pairwise models, especially for communities where species interaction mechanisms are diverse. Considering recent advances in identifying and quantifying interactions, we advocate a transition to models that incorporate interaction mechanisms at the appropriate level of abstraction.

## Materials and methods

## Interaction modification but not interaction chain violates the additivity assumption

In a pairwise model, the fitness of a focal species Si is the sum of its ‘basal fitness’ (ri0, the net growth rate of a single Si individual in the absence of any intra-species or inter-species interactions) and the additive fitness effects exerted by pairwise interactions with other members of the community. Mathematically, an N-species pairwise model is often formulated as(6)dSidt=(ri0+∑j=1Nfij(Sj))Si

Here, fij(Sj) describes how Sj, the density of species Sj, positively or negatively affects the fitness of Si, and is a linear or nonlinear function of only Sj.

Indirect interactions via a third species fall under two categories (Wootton, 1993). The first type is known as ‘interaction chain’ or ‘density-mediated indirect interactions’. For example, the consumption of plant S1 by herbivore S2 is reduced when the density of herbivore is reduced by carnivore S3. In this case, the three-species pairwise model(7){dS1dt=(r10−f12(S2))S1dS2dt=(r20+f21(S1)−f23(S3))S2dS3dt=(r30+f32(S2))S3

does not violate the additivity assumption (compare with Equation 6 (Case and Bender, 1981; Wootton, 1994).

The second type of indirect interactions is known as ‘interaction modification’ or ‘trait-mediated indirect interactions’ or ‘higher order interactions’ (Vandermeer, 1969; Wootton, 1994; Billick and Case, 1994; Wootton, 2002), where a third species modifies the ‘nature of interaction’ from one species to another (Wootton, 2002; Werner and Peacor, 2003; Schmitz et al., 2004). For example, when carnivore is present, herbivore will spend less time foraging and consequently plant density increases. In this case, f12 in Equation 7 is a function of both S2 and S3, violating the additivity assumption.

## Summary of simulation files

Simulations are based on Matlab and executed on an ordinary PC. Steps are:

Step 1: Identify monoculture parameters ri0, rii, and Kii (Figure 1—figure supplement 2C, Row 1 and Row 2).

Step 2: Identify interaction parameters rij, rji, Kij, and Kji where i≠j (Figure 1—figure supplement 2C, Row 3).

Step 3: Calculate distance D¯ between population dynamics of the reference mechanistic model and the approximate pairwise model over a period of time outside of the training window to assess if the pairwise model is predictive.

Fitting is performed using nonlinear least squares (lsqnonlin routine) with default optimization parameters. The following list describes the m-files used for different steps of the analysis:

File name Function FitCost_BasalFitnessSource code 1 Calculates the cost function for monocultures (i.e. the difference between the target mechanisticmodel dynamics and the dynamics obtained from the pairwise model)FitCost_BFSatLV.mSource code 2 Calculates the cost function for communities (i.e. the difference between the target mechanisticmodel dynamics and the dynamics obtained from the saturable L-V pairwise model)FitCost_BFSatLV_Dp.mSource code 3 Calculates the cost function for communities (i.e. the difference between the target mechanistic modeldynamics and the dynamics obtained from the alternative pairwise model)DynamicsMM_WM_MonocultureDpMM.mSource code 4 Returns growth dynamics for monocultures, based on the mechanistic modelDynamicsMMSS_WM_NetworkDpMM.mSource code 5 Returns growth dynamics for communities of multiple species, based on the mechanistic modelDynamicsWM_NetworkBFSatLV.mSource code 6 Returns growth dynamics for communities of multiple species, based on the saturable L-V pairwisemodelDynamicsWM_NetworkBFSatLV_Dp.mSource code 7 Returns growth dynamics for communities of multiple species, based on the alternative pairwise modelDeriveBasalFitnessMM_WM_DpMM.mSource code 8 Estimates monoculture parameters of pairwise model (Step 1)DeriveBFSatLVMMSS_WM_DpMM.mSource code 9 Estimates saturable L-V pairwise model interaction parameters (Step 2)DeriveBFSatLVMMSS_WM_DpMM_Dp.mSource code 10 Estimates alternative pairwise model interaction parameters (Step 2)DeriveBFSatLVMMSS_WM_DpMM_r21.mSource code 11 Estimates saturable L-V pairwise model interaction parameters (r21 and K21) in cases where we knowthat S2 is only affected by S1, to accelerate optimizationDeriveBFSatLVMM_WM_DpMM_Dp_r21.mSource code 12 Estimates alternative pairwise model interaction parameter (r21) in cases where we know that S2 is only affected by S1 and that KS2C1=KC1S2 to accelerate optimizationDynamicsWM_NetworkBFLogLV_DI.mSource code 13 Returns growth dynamics for communities of two species competing for an environmental resourcewhile engaging in an additional interaction, based on the logistic L-V pairwise model (Figure 6)C2Sp2_ARCLi_NoSatDp_FitBFLogLV_DI.mSource code 14 Estimates logistic L-V pairwise model interaction parameters for communities of two speciescompeting for an environmental resource while engaging in an additional interaction, andcompares community dynamics from pairwise and mechanistic models (Figure 6)Dynamics_WM_NetworkDpMM_ODE23.mSource code 15 Defines differential equations when using Matlab’s ODE23 solver to calculate community dynamicsCase_C1Sp2_CmnsDp_ODE23.mSource code 16 Example of using Matlab ODE23 solver for calculating community dynamics

## Deriving a pairwise model for interactions mediated by a single consumable mediator

To facilitate mathematical analysis, we assume that requirements calculated below are eventually satisfied within each dilution cycle (see Figure 3—figure supplement 4 for an example where dilution cycles necessitated by long convergence time violate requirements for a pairwise model to converge to the mechanistic model). We further assume that r10>0 and r20>0 so that species cannot go extinct in the absence of dilution. See Figure 3—figure supplement 5 for a summary of this section.

When S1 releases a consumable mediator which stimulates the growth of S2, the mechanistic model as per Figure 3B, is(8){dS1dt=r10S1dS2dt=r20S2+rS2C1C1C1+KS2C1S2dC1dt=βC1S1S1−αC1S2C1C1+KC1S2S2=(βC1S1−αC1S2C1C1+KC1S2S2S1)S1

Let C1(t=0)=C10=0; S1(t=0)=S10; and S2(t=0)=S20. Note that the initial condition C10=0 can be easily imposed experimentally by pre-washing cells. Under which conditions can we eliminate C1 so that we can obtain a pairwise model of S1 and S2?

Define RS=S2/S1 as the ratio of the two populations.(9)dRSdt=dS2dtS1−S2dS1dtS12=(r20+rS2C1C1C1+KS2C1)S2S1−S2S12r10S1=(r20+rS2C1C1C1+KS2C1−r10)RS

## Case I: r10−r20>rS2C1

Since producer S1 always grows faster than consumer S2, RS→0 as t→∞. Define C~1=C1/S1 (‘~' indicating scaling against a function).(10)dC1~dt=d(C1/S1)dt=dC1dtS1−C1dS1dtS12=(βC1S1S1−αC1S2C1C1+KC1S2S2)S1−C1r10S1S12=βC1S1−r10C1~−αC1S2C~1C~1+KC1S2exp⁡(−r10t)/S10RS

Since RS declines exponentially with a rate faster than | r20+rS2C1−r10 |, we can ignore the third term of the right hand side of Equation 10 if it is much smaller than the first term. That is,αC1S2C~1C~1+KC1S2exp⁡(−r10t)/S10RS<αC1S2RS≤αC1S2RS(0)exp⁡(−|r20+rS2C1−r10|t)≪βC1S1.

Thus for t≫ln⁡(αC1S2RS(0)βC1S1)/|r20+rS2C1−r10|, dC~1dt≈βC1S1−r10C~1. When initial C1~ is 0, this equation can be solved to yield: C1~≈βC1S1(1−exp⁡(−r10t))/r10. After time of the order of 1/r10, the second term can be neglected. Thus, C1~≈βC1S1/r10 after time of the order of max(ln⁡(αC1S2RS(0)βC1S1)/|r20+rS2C1−r10|,1/r10). Then C1 can be replaced by (βC1S1/r10)S1 in Equation 8, and a saturable L-V pairwise model can be derived.

## Case II: rS2C1>r10−r20>0

For Equation 8, we find that a steady state solution for C1 and RS, denoted respectively as C1∗ and RS∗, exist. They can be easily found by setting the growth rates of S1 and S2 to be equal, and dC1/dt to zero.(11){C1∗=r10−r20r20+rS2C1−r10KS2C1RS∗=βC1S1αC1S2(1+KC1S2C1∗)

However, if C1 has not yet reached steady state, imposing steady state assumption would falsely predict RS at steady state and thus remaining at its initial value (Figure 4Bii , dotted lines). Since dC1/dt in Equation 8 is the difference between two exponentially growing terms, we factor out the exponential term S1 to obtain(12)dC1dt=(βC1S1−αC1S2C1C1+KC1S2S2S1)S1=βC1S1f(C1,RS)S1

where f(C1,RS)=1−αC1S2βC1S1C1C1+KC1S2RS. When f≈0, we can eliminate C1 and obtain an alternative pairwise model(13)dS2dt=r20S2+rS2C1βC1S1KC1S2S1βC1S1(KC1S2−KS2C1)S1+αC1S2KS2C1S2S2

Or(4)dS2dt=r20S2+rS2C1S1ωS1+ψS2S2

where ω and ψ are constants (Figure 3Bii).

For certain conditions (which will be discussed at the end of this section, Figure 3—figure supplement 5A), this alternative model can make reasonable predictions of community dynamics even before the community reaches the steady state (Figure 4Bii , compare dashed and solid lines). Below we discuss the general properties of community dynamics and show that there exists a time scale tf after which it is reasonable to assume f≈0 and the alternative model can be derived. We also estimate tf for several scenarios.

We first make C1 and RS dimensionless by defining C^1=C1/C1∗ and R^S=RS/RS∗ (‘ ^ ' indicating scaling against steady state values). Equation 9 can then be rewritten as(14)dR^Sdt=(r20+rS2C1C^1C^1+K^S2C1−r10)R^S

where K^S2C1=KS2C1/C1∗.

From Equations 8 and 11, we obtaindC1C1∗dt=1C1∗(βC1S1−αC1S2C1C1+KC1S2RSRS∗RS∗)S1=1C1∗(βC1S1−αC1S2C1C1+KC1S2R^SRS∗)S1=1C1∗(βC1S1−αC1S2C1/C1∗C1/C1∗+KC1S2/C1∗R^SβC1S1αC1S2(1+KC1S2C1∗))S1=1C1∗βC1S1(1−C^1(1+K^C1S2)C^1+K^C1S2R^S)S1

or(15)dC^1dt=β^C1S1[1−C^1(1+K^C1S2)C^1+K^C1S2R^S]S1

where β^C1S1=βC1S1/C1∗ and K^C1S2=KC1S2/C1∗.

Using these scaled variables, f (i.e. the square bracket in Equation 15) can be rewritten as(16)f(C^1,R^S)=1−C^1(1+K^C1S2)C^1+K^C1S2R^S

and(17)dC^1dt=β^C1S1f(C^1,R^S)S1

Equations 14 and 17 allow us to construct a phase portrait where the x axis is C^1 and the y axis is R^S (Figure 3—figure supplement 2A–D). Note that at steady state, (C^1,\ R^S)=(1,1). Setting Equation 16 to zero:(18)R^S=(1+K^C1S2/C^1)/(1+K^C1S2)or C^1=K^C1S2/[R^S(1+K^C1S2)−1]

defines the f-zero-isocline on the C^1−R^s phase plane (i.e. values of (C^1,\ R^S) at which f(C^1,R^S)=0 and thus C^1 can be eliminated to obtain a pairwise model; Figure 3—figure supplement 2A–D blue lines). As shown in Figure 3—figure supplement 2A, the phase portrait is divided into four regions by the f-zero-isocline (blue) and the steady state C^1=1 (vertical solid line), and grey arrows dictate the direction of the community dynamics trajectory (C^1, R^S). Starting from 'initial state' (C^1(t=0)=0, R^S(t=0)), the trajectory moves downward right (brown circles and orange lines in Figure 3—figure supplement 2A–D) until it hits C^1=1. Then, it moves upward right and eventually hits the f-zero-isocline. Afterward, the trajectory moves toward the steady state (green circles) very closely along (and not superimposing) the f-zero-isocline during which the alternative pairwise model can be derived (Figure 3—figure supplement 2A–D).

It is difficult to solve Equations 14 and 15 analytically because the detailed community dynamics depends on the parameters and the initial species composition in a complicated way. However, under certain initial conditions, we can estimate tf, the time scale for the community to approach the f-zero-isocline. Note that tf is not a precise value. Instead it estimates the acclimation time scale after which a pairwise model can be derived.

One assumption used when estimating all tf is that S10 is sufficiently high (Figure 3—figure supplement 5B) to avoid the long lag phase that is otherwise required for the mediator to accumulate to a high enough concentration.

From Equation 18, the asymptotic value for the f-zero-isocline is(19)R^S(C^1→∞)=1/(1+K^C1S2)

This is plotted as a black dotted line in Figure 3—figure supplement 2A–D.

Below we consider three different initial conditions for R^S(t=0):

## Case II-1. R^S(t=0)≫max(1,K^S2C1−1)

From Equation 11, this becomes RS(0)/RS∗≫max(1,r10−r20r20+rS2C1−r10).

A typical trajectory of the system is shown in Figure 3—figure supplement 2B: at time t=0, using Equations 14 and 15, the community dynamics trajectory (orange solid line in Figure 3—figure supplement 2B inset) has a slope of(20)dR^SdC^1|C^1(0)=0=dR^S/dtdC^1/dt|t=0=(r20−r10)R^S(0)β^C1S1S1(0)

From Equation 18, the slope of the f-zero-isocline (blue line in Figure 3—figure supplement 2B inset) at R^S=R^S(0) is(21)dR^SdC^1|R^S=R^S(0)=d[(1+K^C1S2/C^1)/(1+K^C1S2)]dC^1|R^S=R^S(0)=−11+K^C1S2K^C1S2C^12|R^S=R^S(0)=−K^C1S21+K^C1S2(R^S(0)(1+K^C1S2)−1K^C1S2)2=−[(1+K^C1S2)R^S(0)−1]2(1+K^C1S2)K^C1S2≈−(1+K^C1S2)R^S(0)2K^C1S2

The approximation in the last step is due to the very definition of Case II-1: R^S(t=0)≫1. The initial steepness of the community dynamics trajectory (Equation 20) will be much smaller than that of the f-zero-isocline (Equation 21) if(22)S1(0)≫K^C1S2(r10−r20)β^C1S1(1+K^C1S2)R^S(0)

If we do not scale, together with Equation 11, this becomes:(23)S1(0)≫(KC1S2/C1*)(r10−r20)(βC1S1/C1*)(1+KC1S2/C1*)RS(0)/RS*=KC1S2(r10−r20)RS(0)αC1S2

In this case, the community dynamics trajectory before getting close to the f-zero-isocline can be approximated as a straight line (the orange dotted line) and the change in R^S can be approximated by the green segment in the inset of Figure 3—figure supplement 2B. Since the green segment, the orange dotted line and the red dashed line form a right angle triangle, the length of green segment can be calculated once we find the length of the red dashed line ΔC^1, which is the horizontal distance between (C^1(0), R^S(0)) and the f-zero-isocline and can be calculated from Equation 16:1−ΔC^1(1+K^C1S2)ΔC^1+K^C1S2R^S(0)=0

which yields(24)ΔC^1=K^C1S2R^S(0)(1+K^C1S2)−1≈K^C1S2R^S(0)(1+K^C1S2)

The green segment ΔR^S is then the length of red dashed line (ΔC^1, Equation 24 ) multiplied with dR^SdC^1|C^1(0)=0 (Equation 20), or(25)ΔR^S=(r20−r10)K^C1S2β^C1S1S1(0)(1+K^C1S2)

Note that if Equation 22 is satisfied, |ΔR^S|≪R^S(0). What is the time scale tf for the community to traverse the orange dotted line to be close to the f-zero-isocline? Since from Equation 14 dR^Sdt=(r20+rS2C1C^1C^1+K^S2C1−r10)R^S≈(r20−r10)R^S. In Equation 14, the second term in the parenthese can be dropped if|rS2C1r20−r10C^1C^1+K^S2C1|≪1.

In case II-1, before the system reaches the f-zero-isocline, from Equation 24, C^1≤ΔC^1<1/R^S(0) thus|rS2C1r20−r10C^1C^1+K^S2C1|<|rS2C1r20−r10ΔC^1ΔC^1+K^S2C1|<|rS2C1r20−r1011+R^S(0)K^S2C1|.

From the top portion of Equation 11,rS2C1r10−r20=K^S2C1+1

thus|rS2C1r20−r10C^1C^1+K^S2C1|<(K^S2C1+1)11+R^S(0)K^S2C1.

According to the condition, R̂S(0)≫ max(1,K̂S2C1−1). If K̂S2C1−1>1, then R̂S(0)≫K̂S2C1−1, R̂S(0)K̂S2C1≫1 and K^S2C1<1.|rS2C1r20−r10C^1C^1+K^S2C1|<(K^S2C1+1)11+R^S(0)K^S2C1<21+R^S(0)K^S2C1≪1

If K^S2C1−1<1, then R^S(0)≫1|rS2C1r20−r10C^1C^1+K^S2C1|<(K^S2C1+1)11+R^S(0)K^S2C1=(1+K^S2C1−1)1K^S2C1−1+R^S(0)<2R^S(0)≪1

Thus, the above approximation of Equation 14 is valid, and we obtain

tf≈ln⁡(R^S(0)+ΔR^SR^S(0))/(r20−r10).

Since here ΔR^S≪R^S(0) and ln⁡(1+x)∼x for small x, together with Equation 25, we have(26)tf≈K^C1S2β^C1S1S1(0)(1+K^C1S2)R^S(0)

If unscaled, using Equation 11, this becomestf≈KC1S2/C1*βC1S1/C1*(1+KC1S2/C1*)S1(0)RS(0)/RS*=KC1S2αC1S2S2(0)

## Case II-2. R^S(t=0) is comparable to 1

That is, RS(t=0)≈RS*. If S10 is low, a typical example is shown in Figure 3—figure supplement 2D. Here, because it takes a while for C1 to accumulate, during this lagging phase R^S(t)≈R^S(0)exp⁡(−|r10−r20|t) and there is a sharp plunge in R^S before the trajectory levels off and climbs up. Although the trajectory eventually hits the f-zero-isocline where the alternative pairwise model can be derived, estimating tf is more complicated. Here we consider a simpler case where S10 is large enough so that the trajectory levels off immediately after t=0, and R^S≈1 before the trajectory hits the f-zero-isocline (Figure 3—figure supplement 2A). Since R^S decreases until C^1=1 and from Equation 20, and similar to the reasoning in Case II-1, if|ΔR^S|=|dR^SdC^1|C^1(0)=0|×1=|(r20−r10)R^S(0)β^C1S1S1(0)|≪R^S(0)

or if(28)S1(0)≫(r10−r20)β^C1S1

a typical trajectory moves toward the f-zero-isocline almost horizontally (Figure 3—figure supplement 2A). The unscaled form of Equation 28 is(29)S1(0)≫(r10−r20)β^C1S1=(r10−r20)C1∗βC1S1=(r10−r20)2KS2C1βC1S1(r20+rS2C1−r10)

To calculate the time it takes for the trajectory to reach the f-zero-isocline, let ΔsC^1=C^1−1 and ΔsR^S=R^S−1 at any time point t respectively represent deviation of (C^1(t), R^S(t)) away from their steady state values of (1, 1). We can thus linearize Equation 14 and Equation 15 around the steady state. Note that since at the steady state f= 0, thus Δsf=f.

Rewrite Equation 14 as

dR^Sdt=(r20+rS2C1C^1C^1+K^S2C1−r10)R^S=h(C^1,R^S).

We linearize this equation around the steady state C^1=1,  R^S=1

d(1+ΔsR^S)dt=h(1+ΔsC^1,1+ΔsR^S)≈h(1,1)+ΔsC^1∂h∂C^1||(C^1=1,R^S=1)+ΔsR^S∂h∂R^S|(C^1=1,R^S=1).

At steady state, dR^Sdt=h(1,1)=0. Thus, r20+rS2C11+K^S2C1−r10=0.dΔsR^Sdt=ΔsC^1R^SrS2C1(C^1+K^S2C1)−C^1(C^1+K^S2C1)2|(C^1=1,R^S=1)+ΔsR^S(r20+rS2C1C^1C^1+K^S2C1−r10)|(C^1=1,R^S=1)=ΔsC^1rS2C1K^S2C1(1+K^S2C1)2+ΔsR^S(r20+rS2C11+K^S2C1−r10)=ΔsC^1rS2C1K^S2C1(1+K^S2C1)2.

Thus,(30)dΔsR^Sdt=ΔsC^1rS2C1K^S2C1(1+K^S2C1)2

Recall Equations 15 and 17 as

dC^1dt=β^C1S1(1−C^1(1+K^C1S2)C^1+K^C1S2R^S)S1=β^C1S1f(C^1,R^S)S1.

Linearize around the steady state C^1=1,R^S=1 (note f(1,1)=0):d(1+ΔsC^1)dt=β^C1S1S1(ΔsC^1∂f∂C^1|(C^1=1,R^S=1)+ΔsR^S∂f∂R^S|(C^1=1,R^S=1))=−β^C1S1S1(ΔsC^1((1+K^C1S2)(C^1+K^C1S2)−C^1(1+K^C1S2)(C^1+K^C1S2)2R^S)|(C^1=1,R^S=1)+ΔsR^SC^1(1+K^C1S2)C^1+K^C1S2|(C^1=1,R^S=1))=−β^C1S1S1(ΔsC^1K^C1S21+K^C1S2+ΔsR^S).

Thus,(31)dΔsC^1dt=−β^C1S1(ΔsC^1K^C1S21+K^C1S2+ΔsR^S)S1

Similar to the above calculation, we expand f (Equation 16) around steady state 0,(32)Δsf=f−0=ΔsC^1∂f∂C^1|(C^1=1,R^S=1)+ΔsR^S∂f∂R^S|(C^1=1,R^S=1)=−ΔsC^1K^C1S21+K^C1S2−ΔsR^S

Utilizing Equation 30, Equation 31, and Equation 32,(33)dΔsfdt=dfdt=−ddt(ΔsC^1K^C1S21+K^C1S2+ΔsR^S)=K^C1S2β^C1S11+K^C1S2(ΔsC^1K^C1S21+K^C1S2+ΔsR^S)S1−ΔsC^1rS2C1K^S2C1(1+K^S2C1)2=−K^C1S2β^C1S1S11+K^C1S2f−ΔsC^1rS2C1K^S2C1(1+K^S2C1)2

Taking the derivative of both sides, and using Equation 31 and Equation 32, we have

d2fdt2=−K^C1S2β^C1S11+K^C1S2d(S1f)dt+rS2C1K^S2C1(1+K^S2C1)2β^C1S1(ΔsC^1K^C1S21+K^C1S2+ΔsR^S)S1=−K^C1S2β^C1S11+K^C1S2d(S1f)dt−β^C1S1rS2C1K^S2C1(1+K^S2C1)2fS1.

The solution to the above equation is:f=exp⁡(−b2r10er10t−r10t2)⋅(D1M(12+abr10,0,er10tbr10)+D2W(12+abr10,0,er10tbr10))

where a=rS2C1K^S2C1β^C1S1S10/(1+K^S2C1)2 and b=β^C1S1K^C1S2S10/(1+K^C1S2) are two positive constants. D1 and D2 are two constants that can be determined from the initial conditions of R^S and C^1. M(κ,μ,z) and W(κ,μ,z) are Whittaker functions with argument z. As z→∞ (http://dlmf.nist.gov/13.14.E20 and http://dlmf.nist.gov/13.14.E21)

M(κ,μ,z)∼exp⁡(z/2)z−κW(κ,μ,z)∼exp⁡(−z/2)zκ.

Thus when er10tb/r10≫1,

f∼D1exp⁡[−b2r10er10t−r10t2+er10tb2r10](er10tbr10)−(12+abr10)+D2exp⁡[−b2r10er10t−r10t2−er10tb2r10](er10tbr10)(12+abr10)=(br10)−(12+abr10)D1exp⁡(−(r10+ab)t)+(br10)(12+abr10)D2exp⁡(−br10er10t+abt).

The second term approaches zero much faster compared to the first term due to the negative exponent with an exponential term. Thus,(34)f∝exp⁡(−(r10+ab)t)=exp⁡(−(r10+rS2C1K^S2C1β^C1S1S10/(1+K^S2C1)2β^C1S1K^C1S2S10/(1+K^C1S2))t)=exp⁡(−(r10+rS2C1K^S2C1(1+K^C1S2)K^C1S2(1+K^S2C1)2)t )

Thus, when er10tb/r10≫1, Δsf =f approaches zero at a rate of r10+rS2C1K^S2C1(1+K^C1S2)K^C1S2(1+K^S2C1)2. Therefore, as a conservative estimation, for (35)t≫r10−1

the community is sufficiently close to f-zero-isocline.

## Case II-3. R^S(t=0)≪1/(1+K^C1S2) or RS(0)≪βC1S1/αC1S2

Similar to Case II-2, if Equation 28 is satisfied, a typical trajectory is illustrated in Figure 3—figure supplement 2C where the trajectory decreases slightly until C^1=1. C^1then increases to much greater than one before the system reaches the f-zero-isocline. tf can then be estimated from tf1, the time it takes for C^1 to reach 1 and tf2 , the time takes for R^S to increase to 1/(1+K^C1S2). Using Equation 15, since R^S decreases very little, and R^S(t=0)≪1/(1+K^C1S2),dC^1dt≈β^C1S1S1=β^C1S1S10exp⁡(r10t)

Therefore, C^1≈β^C1S1S1(0)r10(er10t−1).

During tf1, C^1 increases from 0 to 1. Thus, 1≈β^C1S1S1(0)r10(er10tf1−1). tf1≈ln⁡(r10/(β^C1S1S10)+1)/r10.

If(36)S1(0)≫r10β^C1S1

tf1≈(β^C1S1S10)−1≪r10−1.

Using Equation 14 and since C^1 is very large,

dR^Sdt=(r20+rS2C1C^1C^1+K^S2C1−r10)R^S≈(r20+rS2C1−r10)R^S.

This yields

tf2≈ln⁡(1R^S(0)(1+K^C1S2))/(r20+rS2C1−r10),

and a conservative estimation of tf is(37)tf≈1/r10+ln⁡(1R^S(0)(1+K^C1S2))/(r20+rS2C1−r10)

In the unscaled form, this becomes:(38)tf≈1r10+ln⁡((1+KC1S2C1∗)RS(0)RS∗)/(r10−r20−rS2C1)=1r10+ln⁡((1+KC1S2C1∗)RS(0)βC1S1αC1S2(1+KC1S2C1∗ ))/(r10−r20−rS2C1)=1r10+ln⁡(αC1S2RS(0)βC1S1)(r10−r20−rS2C1)

## Case III: r10<r20

In this case, supplier S1 always grows slower than S2. As t→∞, RS=S2/S1→∞ and C1→0. The phase portrait is separated into two parts by the f-zero-isocline (Figure 3—figure supplement 2E), where, as in Equation 12,

f(C1,RS)=1−αC1S2βC1S1C1C1+KC1S2RS=0 or RS=βC1S1αC1S2(1+KC1S2C1).

Note that the asymptotic value of RS (black dotted line, Figure 3—figure supplement 2E–H) is(39)RS(C1→∞)=βC1S1/αC1S2

From Equation 9, dRS/dt>0. From Equation 8, below the f-zero-isocline, dC1/dt>0 and above the f-zero-isocline, dC1/dt<0. Thus if the system starts from (0,RS(0)), the phase portrait dictates that it moves with a positive slope until a time of a scale tf when it hits the f-zero-isocline, after which it moves upward to the left closely along the f-zero-isocline (Figure 3—figure supplement 2E). After tf, the alternative pairwise model can be derived. Although tf is difficult to estimate in general, it is possible for the following cases.

## Case III-1. RS(0)≫βC1S1/αC1S2

Similar to Case II-2, if S10 is small, there is a lagging phase during which the trajectory rises steeply before leveling off (Figure 3—figure supplement 2H). Although the alternative pairwise model can be derived once the trajectory hits the f-zero-isocline, tf takes a complicated form. Here we consider two cases where S10 is large enough so that we can approximate the trajectory as a straight line going through (0,Rs(t=0)) (Figure 3—figure supplement 2F). Graphically, S10 is large enough so that the green segment in Figure 3—figure supplement 2F, whose length is ΔRS, is much smaller than RS(0). In other words,ΔRS=dRSd(C1/KC1S2)|C1(0)=0×Δ(C1/KC1S2)≪RS(0).

From Equations 8 and 9

dRSd(C1/KC1S2)|C1(0)=0=dRS/dtdC1/dt|t=0KC1S2=(r20−r10)RS(0)KC1S2βC1S1S1(0).

Δ(C1/KC1S2), the red segment in Figure 3—figure supplement 2F, is the horizontal distance between (0,RS(0)) and the f-zero-isocline andΔC1KC1S2=βC1S1RS(0)αC1S2−βC1S1.

Thus, ifΔRS=(r20−r10)RS(0)KC1S2βC1S1S1(0)βC1S1RS(0)αC1S2−βC1S1≈(r20−r10)KC1S2S1(0)αC1S2≪RS(0),

orS1(0)≫(r20−r10)KC1S2αC1S2RS(0)

then from Equation 9 and r20>r10, the upper bound of tf can be calculated as(41)tf≈ln⁡(RS(0)+ΔRSRS(0))/(r20−r10)≈ΔRSRS(0)(r20−r10)≈KC1S2RS(0)S1(0)αC1S2=KC1S2S2(0)αC1S2

## Case III-2. RS(0)≪βC1S1/αC1S2

A typical example is displayed in Figure 3—figure supplement 2G. The trajectory moves with a small positive slope so that the intersection of the community dynamics trajectory with the f-zero-isocline is near the black dotted line βC1S1/αC1S2 (Equation 39) where C1/KC1S2 is large. The upper bound of tf can thus be estimated from Equation 9:dRSdt=(r20+rS2C1C1/KS2C1C1/KS2C1+1−r10)RS≥(r20−r10)RS

which yields a conservative estimate of (42)tf≈ln⁡(βC1S1αC1S2RS(0))/(r20−r10)

## Conditions for the alternative pairwise model to approximate the mechanistic model

Cases II and III showed that population dynamics of the mechanistic model could be described by the alternative pairwise model. However, since the initial condition for C1 cannot be specified in pairwise model, problems could occur. To illustrate, we examine the phase portrait of the pairwise equation(13)dS2dt=r20S2+rS2C1S1ωS1+ψS2S2

where ω=1−KS2C1KC1S2, ψ=αC1S2KS2C1βC1S1KC1S2. From Equations 8 and 13,(43)dRSdt=d(S2S1)dt=(r20+rS2C1S1ωS1+ψS2)S2S1−S2r10S1S12=(r20+rS2C1ω+ψRS−r10)RS

Below, we plot Equation 43 under different parameters (Figure 3—figure supplement 3) to reveal conditions for convergence between mechanistic and pairwise models.

If ω=1−KS2C1/KC1S2≥0 (Figure 3—figure supplement 3A): When RS<RS∗, dRS/dt is positive. When RS>RS∗, dRS/dt is negative. Thus, wherever the initial RS, it will always converge toward the only steady state RS∗ of the mechanistic model.

If ω<0 (Figure 3—figure supplement 3B): ω+ψRS=0 or RS=−ω/ψ creates singularity. Pairwise model RS will only converge toward the mechanistic model steady state if(44)RS(0)>−ω/ψ

If ω≥0 (Figure 3—figure supplement 3C): Equation 43 dRSdt=(r20+rS2C1ω+ψRS−r10)RS>0. Thus, Equation 43, which is based on alternative pairwise model, also predicts that RS will eventually increase exponentially at a rate of r20−r10, similar to the mechanistic model.

If ω<0 (Figure 3—figure supplement 3D): RS(0)>−ω/ψ (Equation 44) is required for unbounded increase in RS (similar to the mechanistic model). Otherwise, RS converges to an erroneous value instead.

## Conditions under which a saturable L-V pairwise model can represent one species influencing another via two reusable mediators

Here, we examine a simple case where S1 releases reusable C1 and C2, and C1 and C2 additively affect the growth of S2 (see example in Figure 5). Similar to Figure 3A, the mechanistic model is:(45){S1=S10exp⁡(r10t)dS2dt=(r20+rS2C1S1S1+KS2C1r10/βC1S1+rS2C2S1S1+KS2C2r10/βC2S1)S2

Now the question is whether the saturable L-V pairwise model{S1=S10exp⁡(r10t)dS2dt=(r20+r21S1S1+K21)S2

can be a good approximation.

For simplicity, let’s define KC1=KS2C1r10/βC1S1 and KC2=KS2C2r10/βC2S1. Small KCi means large potency (e.g. small KC2 can be caused by small KS2C2 which means low C2 required to achieve half maximal effect on S2, and/or large synthesis rate βC2S1). Since S1 from pairwise and mechanistic models are identical, we have(46)D¯=12T∫T|log10⁡(S2,pair)−log10⁡(S2,mech)|dt=12Tln⁡(10)∫T|ln⁡(S2,pair)−ln⁡(S2,mech)|dt=12Tln⁡(10)∫T|∫t|(r20+r21S1S1+K21)dτ−∫t(r20+rS2C1S1S1+KC1+rS2C2S1S1+KC2)dτ|dt=12Tln⁡(10)∫T|∫t[r21S1S1+K21−(rS2C1S1S1+KC1+rS2C2S1S1+KC2)]dτ|dt

D¯ can be close to zero when (i) KC1≈KC2 or (ii) rS2C1S1S1+KC1 and rS2C2S1S1+KC2(effects of C1 and C2 on S2) differ dramatically in magnitude. For (ii), without loss of generality, suppose that the effect of C2 on S2 can be neglected. This can be achieved if (iia) rS2C2 is much smaller than rS2C1, or (iib) KC2 is large compared to S1.

## Competitive commensal interaction

For the community in Figure 6A, our mechanistic model is:(47)dS1dt=(r10+rS1C1C1C1+KS1C1)S1dS2dt=[r20+rS2C1,2(C1/KS2C1)(C2/KS2C2)C1/KS2C1+C2/KS2C2(1C1/KS2C1+1+1C2/KS2C2+1)]S2dC1dt=β0−αC1S1rS1C1C1C1+KS1C1S1−αC1S2rS2C1,2C1KS2C1C2KS2C2C1KS2C1+C2KS2C2(1C1KS2C1+1+1C2KS2C2+1)S2dC2dt=βC2S1S1−αC2S2rS2C1,2(C1/KS2C1)(C2/KS2C2)C1/KS2C1+C2/KS2C2(1C1/KS2C1+1+1C2/KS2C2+1)S2

Here, S1 and S2 are the densities of the two species; ri0 is the basal net growth rate of Si (negative, representing death in the absence of the essential shared resource C1); C1 is supplied at a constant rate β0; βC2S1is the production rate of C2 by S1; αCiSj is the amount of resource Ci consumed to produce a new Sj cell.

The growth of S2 is controlled by C1 and C2. When C1 is limiting (C1/KS2C1≪C2/KS2C2), the fitness influence of the two chemicals on S2 becomes:rS2C1,2(C1/KS2C1)(C2/KS2C2)C1/KS2C1+C2/KS2C2(1C1/KS2C1+1+1C2/KS2C2+1)≈rS2C1,2(C1/KS2C1)(C2/KS2C2)C2/KS2C2(1C1/KS2C1+1)=rS2C1,2C1/KS2C1C1/KS2C1+1=rS2C1,2C1C1+KS2C1

which is the standard Monod equation. A similar argument holds for limiting C2. We have intentionally chosen very large KS2C2 to ensure that the fitness effect of C2 on S2 is linear with respect to C2. This way, we minimize the number of pairwise model parameters that need to be estimated.

For our L-V pairwise model, to capture intra-species competition, we usedSidt=bi0(1−Siκi)Si−diSi

where non-negative bi0 represents the maximal birth rate of Si at nearly zero population density (no competition), and non-negative di represents the constant death rate of Si. Positive κi is the ‘carrying capacity’ imposed by the limiting resource, and is the Si at which birth rate becomes zero. This equation can be simplified to:dSidt=(bi0−di)[1−Siκi(1−di/bi0)]Si=ri0[1−SiΛi]Si.

When Λi>0 (i.e. when bi0>di), this resembles standard L-V model traditionally used for competitive interactions (compare to Equation 2; Gause, 1934; Thébault and Fontaine, 2010; Mougi and Kondoh, 2012).

Thus, for the competitive commensal community, we have:(48)dS1dt=b10(1−S1Λ11−S2Λ12)S1−d1S1dS2dt=(b20+r21S1)(1−S1Λ21−S2Λ22)S2−d2S2

Here, birth rate of each species is reduced by competition from the two species, and Λij is the carrying capacity such that a single Si individual will have a zero birth rate when encountering a total of Λij individuals of Sj. For S2, We used (b20+r21S1)(1−S1Λ21−S2Λ22)S2 instead of b20(1−S1Λ21−S2Λ22)S2+r21S1S2 so that when the shared resource is exhausted (i.e. 1−S1Λ21−S2Λ22=0), S2 does not keep growing due to the presence of S1.
