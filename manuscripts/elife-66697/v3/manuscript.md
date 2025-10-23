# Polygenic adaptation after a sudden change in environment

## Authors

- Laura Katharine Hayward<sup>1</sup> ([ORCID: 0000-0003-4445-8067](https://orcid.org/0000-0003-4445-8067)) †
- Guy Sella<sup>3</sup> ([ORCID: 0000-0002-5239-7930](https://orcid.org/0000-0002-5239-7930)) †

### Affiliations

1. https://ror.org/00hj8s172 Department of Mathematics, Columbia University New York United States
2. https://ror.org/03gnh5541 Institute of Science and Technology Maria Gugging Austria
3. https://ror.org/00hj8s172 Department of Biological Sciences, Columbia University New York United States
4. https://ror.org/00hj8s172 Program for Mathematical Genomics, Columbia University New York United States

† Corresponding author

## Abstract

Polygenic adaptation is thought to be ubiquitous, yet remains poorly understood. Here, we model this process analytically, in the plausible setting of a highly polygenic, quantitative trait that experiences a sudden shift in the fitness optimum. We show how the mean phenotype changes over time, depending on the effect sizes of loci that contribute to variance in the trait, and characterize the allele dynamics at these loci. Notably, we describe the two phases of the allele dynamics: The first is a rapid phase, in which directional selection introduces small frequency differences between alleles whose effects are aligned with or opposed to the shift, ultimately leading to small differences in their probability of fixation during a second, longer phase, governed by stabilizing selection. As we discuss, key results should hold in more general settings and have important implications for efforts to identify the genetic basis of adaptation in humans and other species.

## Introduction

Many traits under natural selection are quantitative, highly heritable, and genetically complex, meaning that they take on continuous values, that a substantial fraction of the population variation in their values arises from genetic differences among individuals, and that this variation arises from small contributions at many segregating loci. It therefore stands to reason that the responses to changing selective pressures often involve adaptive changes in such traits, accomplished through changes to allele frequencies at the many loci that affect them. In other words, we should expect polygenic adaptation in complex, quantitative traits to be ubiquitous. This view traces back to the dawn of population and quantitative genetics (Wright, 1931; Fisher, 1958) and is supported by many lines of evidence (Walsh and Lynch, 2018; Sella and Barton, 2019).

Notably, it is supported by studies of the response to directional, artificial selection on many traits in plants and animals in agriculture and in evolution experiments (Walsh and Lynch, 2018; Sella and Barton, 2019). In these settings, selected traits typically exhibit amazingly rapid and sustained adaptive changes (Weber and Diggins, 1990; Barton and Keightley, 2002; Hill, 2016), which are readily explained by models in which the change is driven by small shifts in allele frequencies at numerous loci (Weber and Diggins, 1990; Hill and Kirkpatrick, 2010), and inconsistent with models with few alleles of large effect (Barton and Keightley, 2002; Zhang and Hill, 2005). The potential importance of polygenic adaptation has also been highlighted by more recent efforts to elucidate the genetic basis of adaptation in humans. In the first decade after genome-wide polymorphism datasets became available, this quest was largely predicated on the monogenic model of a hard selective sweep (Voight et al., 2006), in which adaptation proceeds by the fixation of new or initially rare beneficial mutations of large effect (e.g. Smith and Haigh, 1974; Kaplan et al., 1989). Subsequent analyses, however, echoed studies of artificial selection in indicating that hard sweeps were rare, at least over the past ∼500,000 years of human evolution (Coop et al., 2009; Hernandez et al., 2011). Yet humans plausibly adapted in myriad ways during this time period, and they definitely experienced substantial changes in selection pressures, notably during more recent expansions across the globe. These considerations refocused the quest for the genetic basis of human adaptation on polygenic adaptation (Pritchard et al., 2010; Pritchard and Di Rienzo, 2010).

Findings from genome wide association studies (GWASs) in humans have been central to this research program. Statistical analyses of GWASs indicate that in humans, heritable variation in complex traits is highly polygenic (Loh et al., 2015; Shi et al., 2016; Boyle et al., 2017). For example, for many traits, estimates of the heritability contributed by chromosomes are approximately proportional to their length (Shi et al., 2016), suggesting that the contributing variants are numerous and roughly uniformly distributed across the genome. Such findings reinforced the view that adaptive changes to quantitative traits are likely to often be highly polygenic, but also implied that their identification would be difficult, as the changes to allele frequencies at individual loci may be minute. To overcome this limitation, recent studies pooled signatures of frequency changes over the hundreds to thousands of alleles that were found to be associated with an increase (or decrease) in a given trait (Turchin et al., 2012; Berg and Coop, 2014; Robinson et al., 2015; Field et al., 2016; Berg et al., 2019b; Edge and Coop, 2019; Speidel et al., 2019). Initial studies suggest that polygenic adaptation has affected multiple human traits, but these conclusions have been called into question with the realization that the results are highly sensitive to systematic biases in GWASs, most notably due to population structure confounding (Berg et al., 2019a; Sohail et al., 2019).

Given that polygenic adaptation is plausibly ubiquitous, yet likely hard to identify, there is a clear need for a deep understanding of its behavior in populations and footprints in data. To date, theoretical work has primarily focused on two scenarios. The first is motivated by the observed responses to sustained artificial selection, modeled either as truncation selection (Robertson, 1960) or as stabilizing selection, with the optimal phenotype moving at a constant rate in a given direction (e.g. Bürger and Lynch, 1995; Bürger, 1999; Kopp and Hermisson, 2009; Matuszewski et al., 2015; Jain and Devi, 2018). In natural populations, however, quantitative traits are unlikely to be subject to long-term continuous change in one direction. Instead, considerable evidence indicates that they are often subject to long-term stabilizing selection (Sella and Barton, 2019), with intermittent shifts of the optimum in different directions. The second scenario therefore assumes that a sudden change in the environment induces an instantaneous shift in the optimum of a trait under stabilizing selection (Lande, 1976; Barton and de Vladar, 2009; de Vladar and Barton, 2014; Jain and Stephan, 2015; Bod’ová et al., 2016; Jain and Stephan, 2017b; Stetter et al., 2018; Thornton, 2019). Although more elaborate scenarios (where, for example, the optimum and/or strength of stabilizing selection vary frequently) are also possible, this simple scenario provides a sensible starting point for thinking about polygenic adaptation in nature, and is our focus here.

Although there has been considerable work on the adaptive response to an instantaneous change in optimal phenotype, our understanding of this process is still limited. Seminal work by Lande, 1976 described the change in the phenotypic mean assuming that phenotypes are normally distributed in the population and that the phenotypic variance remains constant over time. Barton and Turelli, 1986b derived recursions for the expected change to higher moments of the phenotypic distribution, and showed that when phenotypic variation arises from alleles with large effect sizes, which are strongly selected and rare, the response to selection introduces skew in the phenotypic distribution that can substantially affect the change in the phenotypic mean. Their recursions, however, are not generally tractable, and their analyses do not extend to the phenotypic response in more realistic cases, in which phenotypic variation arises from alleles with a wide range of effect sizes. Moreover, with GWASs now enabling us, at least in principle, to learn about the genetic basis of the phenotypic response, we would like to understand the allele dynamics that underlie it.

Several studies have tackled this problem using simulations (e.g. Stetter et al., 2018; Thornton, 2019). Although illustrative of the dynamics, it is unclear how to generalize their results, given (necessarily) arbitrary choices about multiple parameters and the complexity of these dynamics. In turn, elegant analytical work by de Vladar and Barton, 2014 and extensions by Jain and Stephan, 2017a; Jain and Stephan, 2017b afford a general understanding of the allele dynamics in models with an infinite population size. These dynamics, however, are shaped by features of mutation-selection balance that are specific to infinite populations. Notably, they strongly depend on the frequency of alleles prior to the shift in optimum following deterministically from their effect size, and on the critical effect size at which this frequency transitions from being dominated by selection to being dominated by mutation. In real (finite) populations, the frequencies of alleles whose selection effects are sufficiently small to be dominated by mutation will be shaped by genetic drift; more generally, variation in allele frequencies due to genetic drift will crucially affect the allele response to selection (see below). Thus, we still lack a solid understanding of the allele dynamic underlying polygenic adaptation in natural populations, notably in humans.

Here, we follow previous work in considering the phenotypic and allelic responses of highly polygenic traits after a sudden change in optimal phenotype, but we do so in finite populations and employ a combination of analytic and simulation approaches to characterize how the responses vary across a broad range of evolutionary parameters.

## Model

We build upon the standard model for the evolution of a highly polygenic, quantitative trait subject to stabilizing selection (Wright, 1935b; Robertson, 1956b; Turelli, 1984; Keightley and Hill, 1988; Johnson and Barton, 2005; Simons et al., 2018; Sella and Barton, 2019). An individual’s phenotype is represented by the value of a continuous trait, which follows from its genotype by the standard additive model (Falconer, 1996; Lynch and Walsh, 1998). Namely, we assume that the number of genomic sites affecting the trait (i.e. the target size) is very large, 



L
≫
1



, and that an individual’s phenotype is given by
(1)


z
=

∑

l
=
1


L


(

a

l


+

a

l


′


)
+
ϵ
,

where the first term is the genetic contribution, with a

l
 and 


a
l
′


 denoting the phenotypic effects of the alleles inherited from the parents at site 

l

, and 



ϵ

∼

N
(
0
,

V

E


)



 is the environmental contribution.

Stabilizing selection is introduced by assuming that fitness declines with distance from the optimal trait value positioned at the origin (



z
=
0



). Specifically, we assume a Gaussian fitness function:
(2)


W
(
z
)
=

Exp


[

−

z

2



/

(
2

V

S


)

]



,

where 


V
S

-
1



 measures the strength of selection. The specific form of the fitness function is unlikely to affect our results under parameter ranges of interest (see below), however. Additionally, since the additive environmental contribution to the phenotype can be absorbed into 


V
S


 (by replacing it by 




V

S


′


=

V

S


+

V

E





; e.g., Turelli, 1984; Bürger, 2000), we consider only the genetic contribution.

The population dynamics follow the standard model of a diploid, panmictic population of constant size 

N

, with non-overlapping generations. In each generation, parents are randomly chosen to reproduce with probabilities proportional to their fitness (i.e. Wright-Fisher sampling with fertility selection), followed by mutation, free recombination (i.e. no linkage) and Mendelian segregation. We assume that the mutational input per site per generation is sufficiently small such that segregating sites are rarely more than bi-allelic (i.e. that 



θ
=
4
N
u
≪
1



, where 

u

 is the mutation rate per site per generation). We therefore employ the infinite sites approximation, in which the number of mutations per gamete per generation follows a Poisson distribution with mean 


U
=

L
⁢
u



. The effect sizes of mutations, 


±
a


, are drawn from a symmetric distribution, that is, with equal probability of increasing or decreasing the trait value; we therefore specify this distribution in terms of the distribution of allele magnitudes, 


g
⁢

(
a
)



. Appendix 1—table 1 provides a summary of our notation.

## Evolutionary scenario and parameter ranges

We consider that at the outset (i.e. before the shift in optimal phenotype), the population has attained mutation-selection-drift balance. We follow previous work modeling this balance in making several plausible assumptions about parameter ranges (e.g. Simons et al., 2018), which ensure that genetic variation in the trait is highly polygenic, and subject to effective but not catastrophically strong selection. First, we assume that the per generation, population scaled mutational input is sufficiently large to guarantee high polygenicity (specifically, that 




2
N
U

≫
1



). Second, we assume that the expected number of mutations affecting the trait per generation, per gamete, is small (specifically, that 


U
=

L
⁢
u

≤
0.02


), such that the loss in mean population fitness (i.e. the genetic load) is not too large. As an example, for this assumption to be violated in humans, the mutational target size, 

L

, would have to exceed ∼1.5 Mb (assuming that 



u
≈
1.25
⋅

10

−
8





 per bp per generation; Kong et al., 2012; Besenbacher et al., 2016). We note that we expect our results to hold for substantially greater values of 

U

 in extensions of our model in which genetic variation in the trait under consideration has pleiotropic effects on other selected traits. Third, we make the standard assumption that the selection coefficients of all alleles satisfy 


s
≪
1


, which implies that 



s
e

=


a
2

/

V
S


≪
1


 (subscript 

e

 for equilibrium; see below and Wright, 1931; Wright, 1935a; Turelli, 1984). Fourth, we assume that a substantial proportion of mutations are not effectively neutral, i.e., have 



S
=
2
N

s

e


⪆
1



 (by "



⪆



"/"



⪅



" we mean greater/smaller than or on the same order as). This last assumption is supported by empirical estimates of persistence time of mutations contributing to quantitative genetic variation for a variety of traits and taxa (Walsh and Lynch, 2018; Sella and Barton, 2019) and by inferences based on human GWASs (Simons et al., 2018; Zeng et al., 2018; O’Connor et al., 2019; Zeng et al., 2021), which indicate that quantitative genetic variation is not predominantly neutral. Under these assumptions, the phenotypic distribution at mutation-selection-drift balance is symmetric and tightly centered on the optimal phenotype (Figure 1). Specifically, the mean phenotype exhibits tiny, rapid fluctuations around the optimal phenotype with variance 



δ
2

=


V
S

/

(

2
⁢
N

)




 (Simons et al., 2018); the phenotypic standard deviation is considerably greater than these fluctuations, i.e., 





V

A



≫
δ



 (Section 3.2 of Appendix 3), but it is substantially smaller than the width of the fitness function, that is, 




V

S


≫

V

A





 (Simons et al., 2018 and Section 3.2 of Appendix 3).

![Figure 1.](https://cdn.elifesciences.org/articles/66697/elife-66697-fig1-v3.jpg)

**Figure 1.:** Before the shift in optimum, phenotypes are distributed symmetrically, with a mean that is very close to the old optimum and a standard deviation that is substantially smaller than the width of the fitness function (

). We consider the response to an instantaneous shift in optimum, for the case where the magnitude of the shift is smaller than the width of the fitness function (







V


A
(
0
)
≪


V


S

). See text for further details.



Λ
⪅




V
S

We then consider the response to an instantaneous shift of 

Λ

 in optimal phenotype at time 


t
=
0


 (Figure 1), ensuring that the shift is substantial yet not immensely large when compared to the genetic variance in the trait and in terms of the reduction in mean population fitness. To these ends, we first assume that the shift in optimum is greater than the equilibrium fluctuations in mean phenotype, i.e., that 



Λ
>
δ



. Second, we assume that the shift is smaller than, or on the order of, the width of the fitness function (



Λ
⪅


V

S






) and that the vast majority of mutations move the phenotype by much less than the distance over which fitness declines, 



V
S



 (i.e. that 



a
≪


V

S






). These two assumptions guarantee that the maximal directional selection coefficient of alleles, attained immediately after the shift, satisfies 




s

d


=
2
⋅
(
Λ
⋅
a
)

/


V

S


≪
1



 (see below and Wright, 1931; Barton and Turelli, 1986b). Our current condition on the magnitudes of mutations (i.e. that 



a
≪


V

S






) is stronger than our earlier one at equilibrium (i.e., that 




s

e


=

a

2



/


V

S


≪
1



), but is still not particularly restrictive, as it allows for the selection coefficients of alleles at equilibrium, 




s
e




, to be as large as 1%. As a concrete example, with a population size of 


N
=

10
4



, both this condition and the condition that a substantial proportion of mutations not be effectively neutral (


S
=

2
⁢
N
⁢

s
e


⪆
1


) are satisfied if selection coefficients of alleles at equilibrium are exponentially distributed with mean between 


10

-
5



 and 


10

-
3



. Third, we assume that adaptation to the new optimum requires only a small average frequency change per segregating site, which translates into the requirement that 



Λ

/



V

A


(
0
)

⪅
1

/

2
⋅

2
N
U




 (see Section 3.2 of Appendix 3). Both this and the previous bound on the shift size (that 



Λ
⪅


V

S






) are again not particularly restrictive, in that they allow for shifts of several equilibrium phenotypic standard deviations (given that 




2
⁢
N
⁢
U


≫
1


 and 



V
S

≫


V
A

⁢

(
0
)




 for this and the former bounds, respectively). Our assumptions on parameter values are summarized in Appendix 1—table 2.

## Choice of units

When we study the allelic response, we use units based on the dynamics at mutation-selection-drift balance (i.e. before the shift in optimum). Using arbitrary units, and denoting corresponding parameter values with tildes, the population-scaled selection coefficient at mutation-selection-drift balance is 



S
=
2
N

s

e


=
2
N



a
~



2



/




V
~



S


=



a
~



2



/




δ
~



2





. We measure the trait in units of 

δ

, the typical deviation of the population mean from the optimum. In these units, the magnitude of effect size 


a
=

S



, the stabilizing selection parameter 



V
S

=

2
⁢
N



, and the contribution of a segregating allele to variance is 




v
*

⁢

(
a
,
x
)


=

2
⁢

a
2

⁢
x
⁢

(

1
-
x

)




. As shown below, stating our results in these terms makes their form invariant with respect to the population size, 

N

, and the strength of stabilizing selection, 


V
S

-
1



.

## Simulations and resources

We compare our analytical results to three kinds of simulations, which differ in their simplifying assumptions and computational tractability (see Section 2 of Appendix 3 for further detail). The first realizes the full model described above; it is run for a burn-in period of 


10
⁢
N


 generations before the shift and for a period of 


12
⁢
N


 generations after, to attain equilibrium both before and after. The second traces all alleles rather than individuals, assuming linkage equilibrium (rather than free recombination). Changes to allele frequencies every generation are modeled according to the Wright-Fisher process. These second simulations are also run with a burn-in period of 



10
N



 generations before the shift, then for 


12
⁢
N


 generations after. The third kind of simulation traces the trajectory of a single allele segregating at the time of the shift. To that end: (i) given the effect size of the allele, we sample initial minor allele frequencies from the closed form, equilibrium distributions (Equation A3-27 in Appendix 3), using importance sampling based on the density of variance contributed by different minor allele frequencies (Section 3.1 of Appendix 3); and (ii) the trajectory of the mean phenotype of the population over time, on which the allele dynamics depend, is given as input, based on either an analytical approximation (see below) or on an average over simulations of the second kind. The single allele simulation is run until the focal allele fixes or goes extinct. Documented code for simulations can be found at https://github.com/sellalab/PolygenicAdaptation1D (copy archived at swh:1:rev:35d0857272a3929bad9fad0856e90c24e032b5ff; Hayward and Sella, 2022).

In the main text, we use the simulations that afford the highest resolution in comparisons with analytical predictions, whereas in Section 2.2 of Appendix 3 we validate our main results against simulations that realize the full model (at a lower resolution). Specifically, we compare most of the predictions about the allele dynamics with the results of single allele simulations, running 250,000 replicas for any given allele effect size and optimum shift size (see parameter choices below). The single allele simulations do not describe phenotypic change or the trajectories of mutations that arise after the shift in optimum, however. We therefore compare the predictions for these processes with the results of the all alleles simulations; in these simulations, we run 2500 replicas with any given set of parameters.

The simulations used in the main text correspond to the two qualitative phenotypic responses described below, which we refer to as the Lande and non-Lande (see Results). Specifically, we use the following simulation parameter values:

## Results

## Phenotypic response

We first consider how the population’s mean phenotype approaches the new optimum. In Section 1.2 of Appendix 3, we express the mean distance from the new optimum, 


D
⁢

(
t
)



, as a sum over alleles’ contributions. We show that under our assumptions, the expected, per generation change in this distance is well approximated by
(3)


E

(

Δ
D
(
t
)

)

≈
−

V

A


(
t
)

/


V

S


⋅
D
(
t
)
+
(
1
−

D

2


(
t
)

/


V

S


)
⋅

μ

3


(
t
)

/

(
2

V

S


)
,

where 



V
A

⁢

(
t
)



 and 



μ
3

⁢

(
t
)



 denote the 2nd and 3rd central moments of the phenotypic distribution. The 1st term on the right-hand side reflects selection to reduce the distance between the mean phenotype and the new optimum, which is proportional to this distance and to the additive genetic variance (Lande, 1976). The 2nd term reflects the effect of stabilizing selection on an asymmetric (skewed) phenotypic distribution. In particular, when the mean phenotype is near the optimum (and this 2nd term is approximately 




μ
3

⁢

(
t
)


/

(

2
⁢

V
S


)



), stabilizing selection pushes the mean phenotype in the direction opposite to the thicker tail of the phenotype distribution (see Section 1.2 of Appendix 3 for further discussion of Equation 3). Similar expressions were derived by Barton and Turelli, 1986b under the rare-alleles approximation and by Bürger, 1991 under the assumption of a parabolic fitness function.

We rely on Equation 3 to describe the phenotypic response to selection. This response takes a simple form in the infinitesimal limit (Fisher, 1918) in which genetic variation at equilibrium arises from infinitely many segregating alleles with infinitesimally small effect sizes (see Section 8 of Appendix 3 for details). In this limit, the equilibrium phenotypic distribution is Normal and it remains Normal with the same variance after the shift, because the change in mean phenotype is achieved by infinitesimally small changes to allele frequencies at infinitely many loci, with no change to the frequency distribution (Lande, 1976, and Section 8 of Appendix 3). Under these assumptions, Equation 3 reduces to
(4)


E

(

Δ
D
(
t
)

)

=
−

V

A


(
0
)

/


V

S


⋅
D
(
t
)
,

which (in continuous time) is solved by
(5)



D

L


(
t
)
=
Λ
⋅

Exp


[

−

V

A


(
0
)

/


V

S


⋅
t

]



.

This solution was first derived by Lande, 1976, and in what follows, we refer to it as Lande’s solution or approximation. When genetic variance is dominated by loci with small and intermediate effect sizes (as defined below), the trait is highly polygenic, and the shift in optimum is not too large relative to the phenotypic standard deviation, changes to the 2nd and 3rd central moments of the phenotypic distribution are small and the expected phenotypic response is well approximated by Lande’s solution (Figure 2A and Appendix 3—figures 26 and 27).

![Figure 2.](https://cdn.elifesciences.org/articles/66697/elife-66697-fig2-v3.jpg)

**Figure 2.:** (
A) Cartoon of the two kinds of phenotypic response: (i) the Lande approximation, in which the mean approaches the new optimum exponentially with time and the phenotypic distribution maintains its shape; (ii) substantial deviations from Lande’s approximation, in which the mean approaches the new optimum rapidly at first, but during this time the phenotypic distribution becomes skewed, causing the mean’s approach to slow down dramatically, to a rate that is dictated by the decay of the 3rd central moment. (B) In both the Lande and non-Lande cases, the mean phenotype initially approaches the new optimum rapidly. This approach is described by Lande’s approximation, and is thus almost identical in the two cases (which is why only the Lande curve is visible). The simulation results were generated using the all alleles simulation with a shift of 
, as detailed in 



Λ
=


4
⋅






V
A
⁢


(
0
)
Simulations and resources. For each quantity described in B-D, we show the simulations’ mean ±1.96 SE (solid lines and shaded regions, respectively). (C) In the non-Lande case, the phenotypic variance and skewness increase during the rapid phase and then take a very long time to decay to their values at equilibrium. (D) Over the longer-term, the approach to the optimum in the non-Lande case almost grinds to a halt, where its rate can be described by the quasi-static approximation (Equation 6). While the non-Lande response differs from Lande’s approximation, the difference is small: the maximal deviation in mean phenotype is 
, the variance increases by ∼ 10% and the maximal skewness is tiny (less than 0.01).




∼


0.06
⋅






V
A
⁢


(
0
)

More generally, given our assumptions that polygenicity is high and that the shift is not too large (see Section 6 of Appendix 3), the deviations from Lande’s approximation are usually small and their magnitude is determined by the distribution of allele effect sizes (see section on The allelic response in the equilibration phase and Section 6 of Appendix 3). Specifically, changes to the 2nd and 3rd central moments of the phenotypic distribution are greater when alleles with large effects contribute markedly to genetic variance (Figure 2C, Appendix 3—figures 26 and 27, and Barton and Turelli, 1986b). For some intuition, consider a pair of minor alleles with the same initial frequency and magnitude of effect, where the effect of one is aligned with the shift and the effect of the other opposes it. After the shift, directional selection increases the frequency of the aligned allele relative to that of the opposing one. The frequency increase of the aligned allele increases variance more than the frequency decrease of the opposing allele decreases it, resulting in a net increase to variance (Figure 2C; Barton and Turelli, 1986b; de Vladar and Barton, 2014; Jain and Stephan, 2017a). The relative changes in frequency and thus the net increase in variance are greater for alleles with larger effects. Next consider the 3rd central moment. At equilibrium, the contributions of alleles with opposing effects to the 3rd central moment cancel out. After the shift, the frequency increase of aligned alleles relative to opposing ones introduces a non-zero 3rd central moment (Figure 2C). Large effect alleles contribute substantially more to this 3rd central moment, plausibly because their individual contribution to the 3rd central moment at equilibrium is greater (see Section 3.3 of Appendix 3 and Appendix 3—figure 7B) and because they exhibit larger relative changes in frequency after the shift (see section on The allelic response in the rapid phase and Section 4 of Appendix 3). The same reasoning suggests that very large shifts in optima or low polygenicity could also lead to substantial changes to the 2nd and 3rd central moments of the phenotypic distribution (Section 6 of Appendix 3 and Barton and Turelli, 1986b), but these cases violate our assumptions and are beyond the scope of this manuscript.

The increase in 2nd and 3rd central moments after the shift result in a phenotypic dynamic with two distinct phases. First, immediately after the shift, the mean phenotype rapidly approaches the new optimum, akin to the exponential approach in Lande’s approximation. In this case, however, genetic variance increases and thus the exponential rate of approach may increase, making the expected approach even faster (Equation 3). Shortly thereafter, when the mean phenotype nears the optimum, the decreasing distance and increasing 3rd central moment reach the point at which
(6)




D
⁢

(
t
)


≈



μ
3

⁢

(
t
)


/

(

2
⁢

V
A

⁢

(
t
)


)



.

The two terms on the right-hand side of Equation 3 then approximately cancel out, and the dynamic enters a second, prolonged phase, in which the approach to the optimum nearly grinds to a halt (Figure 2D). During this phase, the expected change in mean phenotype can be described in terms of a quasi-static approximation given by Equation 6 (Figure 2D and Appendix 3—figure 25). The rate of approaching the optimum is then largely determined by the rate at which the 3rd central moment decays. This roughly corresponds to the rate at which the allele frequency distribution equilibrates and mutation-selection-drift balance is restored around the new optimum (see section on Other properties of the equilibration process).

## Allele dynamics

We now turn to the allele dynamics that underlie the phenotypic response. These dynamics can be described in terms of the first two moments of change in frequency in a single generation (Ewens, 2004, Chapter 4). For an allele with effect size 



±
a



 and frequency 



x



, we calculate the moments by averaging the fitness of the three genotypes over genetic backgrounds (Section 1 of Appendix 3). Under our assumptions, the moments are well approximated by
(7)



E
⁢

(

Δ
⁢
x

)


≈




(

±



a
⋅
D

⁢

(
t
)


/

V
S



)

⋅
x

⁢

(

1
-
x

)


-



(


a
2

/

V
S


)

⋅

(

1
-



D
2

⁢

(
t
)


/

V
S



)

⋅
x

⁢

(

1
-
x

)

⁢

(


1
/
2

-
x

)

and
(8)


V
(
Δ
x
)
≈
x
(
1
−
x
)

/

(
2
N
)
,

which is the standard drift term. Similar expressions for the first moment trace back to Wright, 1935b and have been used previously to study the response to selection on quantitative traits (Barton, 1986a; Bürger, 1991; Charlesworth, 2013; de Vladar and Barton, 2014).

The two terms in the first moment reflect different modes of selection: directional and stabilizing, respectively. The first term arises from directional selection on the trait and takes a semi-dominant (additive) form with selection coefficient 



s
d

=

±




2
⁢
a

⋅
D

⁢

(
t
)


/

V
S





. Its effect is to increase the frequency of alleles whose effects are aligned with the shift (and vice versa) and its strength weakens as the distance to the new optimum, 

D

, decreases. The second term arises from stabilizing selection on the trait and takes an under-dominant form with selection coefficient 



s
e

=



a
2

/

V
S


⋅

(

1
-



D
2

⁢

(
t
)


/

V
S



)




. Its effect is to decrease an allele’s contribution to phenotypic variance, 


2
⁢

a
2

⁢
x
⁢

(

1
-
x

)



, by reducing minor allele frequency (MAF); it becomes weaker as the MAF approaches 1/2.

The relative importance of the two modes of selection varies as the mean distance to the new optimum, 

D

, decreases. We therefore divide the allelic response into two phases: a rapid phase, immediately after the shift, in which the mean distance to the new optimum is substantial and changes rapidly, and a subsequent, prolonged equilibration phase, in which the mean distance is small and changes slowly (Jain and Stephan, 2017a). We define the end of the rapid phase as the time, 




t
1




, at which Lande’s approximation for the distance to the optimum 



D
L

⁢

(

t
1

)



 equals the typical deviation of the population mean from the optimum at equilibrium 



δ
=


V

S



/

2
N




, i.e.,
(9)



t

1


≡

(


V

S



/


V

A


(
0
)

)

⋅

L
n


[

Λ

/

δ

]

∼

(

1

/

U

)

⋅

L
n


[

Λ

/

δ

]

(in Section 3.2 of Appendix 3 we show that 





V
S

/

V
A


⁢

(
0
)


∼

1
/
U



). This definition is somewhat arbitrary, as the transition between phases is gradual, but it roughly captures the change in allele dynamics (Appendix 3—figure 25). Moreover, our analysis is insensitive to this particular choice (we only use it in comparing analytic and simulation results for the rapid phase).

The change in mean phenotype during the rapid phase is driven by the differential effect of directional selection on minor alleles whose effects are aligned and opposed to the shift in optimum (Figure 3). Considering a pair of minor alleles with opposing effects of the same magnitude and the same initial frequency, selection increases the frequency of the aligned allele relative to the opposing one. By the end of the rapid phase, the frequency differences across all aligned and opposing alleles drive the mean phenotype close to the new optimum (Figure 2A). Deviations from Lande’s approximation manifest as prolonged, weak directional selection during the equilibration phase, which further increases the expected frequency difference between aligned and opposing alleles. However, given that we are considering a highly polygenic trait, the expected frequency difference between a pair of opposing alleles will be small. This small difference causes aligned alleles to have a slightly greater probability of eventually fixing during the equilibration phase (Figure 3). Over a period on the order of 


2
⁢
N


 generations (see below), the frequency differences between aligned and opposing alleles are replaced by a slight excess of fixed differences between them, and the equilibrium genetic architecture is restored around the new optimum. In the following sections, we describe these processes quantitatively: Specifically, we ask how the relative contribution of alleles to phenotypic change during the two phases depends on their effect size and initial frequency.

![Figure 3.](https://cdn.elifesciences.org/articles/66697/elife-66697-fig3-v3.jpg)

**Figure 3.:** We divide the allele dynamics into rapid and equilibration phases, based on the rate of phenotypic change, and consider the trajectories of alleles with opposing effects of the same magnitude, which start at the same initial minor frequency. During the rapid phase, alleles whose effects align with the shift slightly increase in frequency relative to those with opposing effects. During the equilibration phase, this frequency difference can increase further and eventually leads aligned alleles to fix with slightly greater probabilities than opposing ones.

## The allelic response in the rapid phase

We can describe changes to allele frequencies during the rapid phase with a simple deterministic approximation. The duration of the rapid phase is much shorter than the time scale over which genetic drift has a substantial effect (



t
1

∼

1
/
U

≪

2
⁢
N



 generations; see Equation 9), allowing us to rely only on the first moment of change in allele frequency (Equation 7). Additionally, deviations of the distance 


D
⁢

(
t
)



 from Lande’s approximation during this phase have negligible effects (Figure 2B and Appendix 3—figure 8D–F), allowing us to assume that 



D
(
t
)
=

D

L


(
t
)



 (Equation 5). Lastly, when relative frequency changes are small, we can substitute the frequency in the first moment by its initial value. With these simplifications, we can integrate the first moment over time to obtain an explicit linear approximation for frequency changes.

Consider a pair of minor alleles with opposing effects of size 



±
a



 and initial frequency 




x
0




 before the shift in optimum. Using our linear approximation, we find that the frequency difference between them at the end of the rapid phase is
(10)





Δ

x


t

1




∗


(
a
,

x

0


)


=


x


t

1




(
a
,

x

0


)
−

x


t

1




(
−
a
,

x

0


)
≈
2
⋅
(
a

/


V

S


)
⋅

x

0


(
1
−

x

0


)

∫

0



t

1





D

L


(
t
)
d
t






=
(
Λ
−

D

L


(

t

1


)
)
⋅
2
a

x

0


(
1
−

x

0


)

/


V

A


(
0
)
.

The contribution of the pair to the change in mean phenotype is (11)


Δ

z


t

1




∗


(
a
,

x

0


)
=
2
a
⋅
Δ

x


t

1




∗


(
a
,

x

0


)
≈
(
Λ
−

D

L


(

t

1


)
)
⋅
2
⋅

v

∗


(
a
,

x

0


)

/


V

A


(
0
)
,

where 




v
*

⁢

(
a
,

x
0

)


=

2
⁢

a
2

⁢

x
0

⁢

(

1
-

x
0


)




 is the contribution to variance of an allele with magnitude 

a

 and frequency 




x
0




. Thus, the pair’s contribution to phenotypic change is proportional to its contribution to phenotypic variance before the shift in optimum.

The expected contribution of alleles with a given magnitude and initial frequency is therefore proportional to their expected contribution to phenotypic variance at equilibrium, before the shift occurs. We focus on the contribution of alleles divided by the mutation rate at which they are introduced into the population, that is the ‘contribution per unit mutational input’. To this end, we measure the trait value in units of 



δ
=


V

S



/

(
2
N
)




 and express allele magnitudes in terms of the scaled selection coefficients at equilibrium (when 


D
=
0


); in these units 


S
=

2
⁢
N
⁢

s
e


=

a
2



 (see Choice of units). Expressing our results in this form makes them invariant with respect to changing the population size, 

N

, stabilizing selection parameter, 


V
S


, mutational input per generation, 


2
⁢
N
⁢
U


, and distribution of magnitudes, 


g
⁢

(
a
)



. In these terms, the expected contribution of alleles with given magnitude and initial MAF to phenotypic change is
(12)




Δ
⁢

z

t
1


⁢

(
a
,

x
0

)


≈





(

Λ
-


D
L

⁢

(

t
1

)



)

⋅
v

⁢

(
a
,

x
0

)


/

V
A


⁢

(
0
)



,

and the marginal contribution of alleles with a given magnitude is
(13)



Δ

z


t

1




(
a
)
=

∫

0


1

/

2


Δ

z


t

1




(
a
,
x
)
d
x
≈
(
Λ
−

D

L


(

t

1


)
)
⋅
v
(
a
)

/


V

A


(
0
)
,

where 



v
(
a
,

x

0


)
≈
4

a

2


⋅

Exp


[

−

a

2



x

0


(
1
−

x

0


)

]




 and 



v
(
a
)
≈
4

a

2


⋅

∫

0


1

/

2



Exp


[

−

a

2


x
(
1
−
x
)

]

d
x
=
4
a
⋅

D

+



(

a

/

2

)




 are the corresponding densities of variance per unit mutational input at equilibrium, and 


D
+


 is the Dawson function (Section 3.2 of Appendix 3). The expected absolute contributions follow from multiplying these expressions by the mutational input per generation, 




2
⁢
N
⁢
U

⋅
g

⁢

(
a
)



. Specifically, as we would expect, the total change in mean phenotype during the rapid phase is 



2
N
U
⋅
Δ

z


t

1




=
2
N
U
⋅

∫

0


∞


Δ

z


t

1




(
a
)
⋅
g
(
a
)
d
a
≈
Λ
−

D

L


(

t

1


)



, as 




V

A


(
0
)
=
2
N
U
⋅

∫

0


∞


v
(
a
)
⋅
g
(
a
)
d
a



.

The relative contribution of alleles with a given magnitude and initial MAF to phenotypic change follows from their expected contribution to variance at equilibrium (Equations 12 and 13, and Figure 4). The properties of 


v
⁢

(
a
)



 imply that (Figure 4A): (i) the relative contribution of alleles with small effect sizes (



a
2

≪
1


) scale linearly with 


S
=

a
2



 (



v
(
a
)
≈
2

a

2





, measured in units of 


δ
2


); (ii) the contribution of alleles with moderate and large effect sizes (roughly 



S
=

a

2


>
3



) are much greater, and fairly insensitive to the effect size (with 



v
⁢

(
a
)


≈
4


); and (iii) the contribution is maximized for 



a
2

≈
10


 (



v
(

10

)
≈
5.2



) (see Simons et al., 2018, for intuition about these properties). While large and moderate effect alleles make similar contributions to phenotypic change, MAFs of large effect alleles before the shift are much lower than MAFs of moderate ones (Figure 4B), because they are subject to stronger stabilizing selection. The expected frequency difference between pairs of opposing alleles is greatest for moderate effect sizes (Figure 4C), because it is proportional to 



E
⁢

(

2
⁢
a
⁢

x
0

⁢

(

1
-

x
0


)


)


∝


v
⁢

(
a
)


/
a



 (Equation 10), and 


v
⁢

(
a
)



 is similar for moderate and large effect sizes. Additional properties of the allelic response during the rapid phase are presented in Section 4 of Appendix 3.

![Figure 4.](https://cdn.elifesciences.org/articles/66697/elife-66697-fig4-v3.jpg)

**Figure 4.:** (
A) Alleles with moderate and large magnitudes make the greatest contribution to phenotypic change (per unit mutational input). The results of our linear approximation (derived in the main text) are compared with a more accurate nonlinear one (derived in Section 4.1.2 of Appendix 3) and with simulations. (B) The average MAF of aligned and opposing alleles at the end of the rapid phase decreases with effect size squared. (C) The expected frequency difference between pairs of opposing alleles is greatest for moderate effect sizes. In B and C, the results of the nonlinear approximation are compared with simulations. The simulation results in all panels were were generated using the single allele simulation, as detailed in Simulations and resources; error bars are not visible because they are smaller than the points.

When the polygenicity is low and/or the shift in optimum or effect sizes are large our linear approximation becomes less accurate (Figure 4A). Specifically, minor alleles exhibit large relative changes in frequency such that substituting the initial MAF for the frequency in Equation 7 for the 1st moment is inaccurate. In Section 4.1.2 of Appendix 3 we derive a nonlinear approximation that is more accurate in these cases (Figure 4A and Appendix 3—figures 9 and 10). Nonetheless, the qualitative behaviors we outlined remain intact.

## The allelic response in the equilibration phase

Over the long run, the small frequency differences between opposite alleles that accrue during the rapid phase translate into small differences in their fixation probabilities (Figure 3). In the non-Lande case, prolonged weak directional selection during the equilibration phase amplifies these differences in fixation probabilities. We approximate fixation probabilities in two steps. First, we model the effect of directional selection on frequency as an instantaneous, deterministic pulse. Second, we apply the diffusion approximation for the fixation probability (Ewens, 2004, Chapter 4), assuming stationary stabilizing selection (


D
=
0


), genetic drift, and the initial frequency after the pulse. We further assume that the relative changes in allele frequencies due to directional selection are small, such that we can use approximations that are linear in this change; but in Section 5 of Appendix 3, we derive nonlinear approximations that relax this assumption.

## The Lande case

When Lande’s approximation is accurate, directional selection is non-negligible only briefly after the shift. This justifies approximating its effects as if they were caused by an instantaneous pulse. It also suggests that mutations that arise after the shift in optimum contribute negligibly to phenotypic change, because when directional selection is non-negligible, few of them arise and their fixation probabilities are tiny (given that they start from an initial frequency of 



1
/
2

⁢
N


).

Consider a pair of opposite minor alleles, with magnitude 

a

 and initial frequency 




x
0




. Analogously to our derivations for the rapid phase (Equations 10, 11 and 12) by modeling the effects of directional selection on their frequencies as an instantaneous pulse, and assuming that these effects are small, we find that the resulting frequency differences between them is approximated by
(14)





Δ

x

d


∗


(
a
,

x

0


)


≡


x

d


(
a
,

x

0


)
−

x

d


(
−
a
,

x

0


)
≈
2
a

x

0


(
1
−

x

0


)
⋅

∫

0


∞


(

D

L


(
τ
)

/


V

S


)
d
τ






=
2
a

x

0


(
1
−

x

0


)
⋅
Λ

/


V

A


(
0
)
.

Consequently, the pair’s expected contribution to phenotypic change is approximated by
(15)


Δ

z

d


∗


(
a
,

x

0


)
≡
2
a
⋅
Δ

x

d


∗


(
a
,

x

0


)
≈
2
Λ
⋅

v

∗


(
a
,
x
)

/


V

A


t
(
0
)
,

and the contribution of such pairs per unit mutational input is approximated by
(16)


Δ

z

d


L


(
a
,

x

0


)
≈
Λ
⋅
v
(
a
,
x
)

/


V

A


(
0
)
,

where, as before, 




v
*

⁢

(
a
,
x
)


=

2
⁢

a
2

⁢
x
⁢

(

1
-
x

)




 is an allele’s contribution to genetic variance and 


v
⁢

(
a
,
x
)



 is the density of variance per unit mutational input at equilibrium, and we use the superscript 

L

 to denote that this applies to the Lande case.

We approximate a pair’s expected long-term, fixed contribution to phenotypic change by calculating the difference in fixation probabilities of the opposite alleles given their frequency after the pulse, again assuming that the effects of the pulse are small. Namely,
(17)





Δ

z

∞


∗


(
a
,

x

0


)


≈
2
a

(

π
(
a
,

x

d


(
a
,

x

0


)
)
−
π
(
a
,

x

d


(
−
a
,

x

0


)
)

)






≈
2
a
⋅


∂
π


∂
x


(
a
,

x

0


)
⋅
Δ

x

d


∗


(
a
,

x

0


)
=


∂
π


∂
x


(
a
,

x

0


)
⋅
Δ

z

d


∗


(
a
,

x

0


)
.

where 


π
⁢

(
a
,
x
)



 denotes the fixation probability of an allele with magnitude 

a

 and initial frequency 

x

 under stationary stabilizing selection and drift. In Section 3 of Appendix 3 we derive the diffusion approximation for 


π
⁢

(
a
,
x
)



 and show that
(18)




∂
π


∂
x


(
a
,

x

0


)
=
2
f
(
a
)

/

v
(
a
,

x

0


)
,

where 



f
(
a
)
≡
2

a

3


⋅

Exp


[

−

a

2



/

4

]


/


(


π

⋅

E
r
f


[

a

/

2

]


)




. From Equation 14-18, we find that the expected fixed contribution per unit mutational input of pairs of alleles is
(19)


Δ

z

∞


L


(
a
,

x

0


)
≈


∂
π


∂
x


(
a
,

x

0


)
⋅
Δ

z

d


L


(
a
,

x

0


)
≈
2
Λ
⋅
f
(
a
)

/


V

A


(
0
)
.

Note that this expression does not depend on the initial frequency! The expected marginal contribution of alleles with a given magnitude follows and is
(20)



Δ

z

∞


L


(
a
)
=

∫

0


1

/

2


Δ

z

∞


(
a
,
x
)
d
x
≈
Λ
⋅
f
(
a
)

/


V

A


(
0
)
.

Hence, the function 

f

 approximates how the relative long-term contribution of alleles depends on their magnitudes (Figure 5A).

![Figure 5.](https://cdn.elifesciences.org/articles/66697/elife-66697-fig5-v3.jpg)

**Figure 5.:** We show the relative contribution of alleles as a function of effect size squared, based on the linear approximations and on simulations with the two shift sizes specified in the caption. (
A) The Lande case. The theoretical prediction is described by the function 
 (



f
⁢


(
a
)
Equations 13 and 20), and simulation results were generated using the single allele simulation, as detailed in Simulations and resources; error bars are not visible because they are smaller than the points. Our prediction for the long-term contribution (corresponding to 
) is always below the prediction for the rapid phase (corresponding to 



f
⁢


(
a
)

). The difference becomes substantial for 



v
⁢


(
a
)

, implying that the linear Lande approximation underestimates the fixed contribution when large effect alleles contribute markedly to the genetic variance at equilibrium. (





a
2
⪆
4
B) The non-Lande case. Here, we assume an exponential distribution of effect sizes squared with 
, which yields an amplification factor of 





E
⁢


(


a
2
)
=
16

 (





1
+
C
≈
2.2
Equation 22). The theoretical prediction for the joint contribution of standing variation and new mutations is described by the function 
 (





(
1
+
C
)
⋅
f
(
a
)
Λ


/


V


A
(
0
)
Equation 28). Simulation results were generated using the all alleles simulation for the non-Lande case (see section on Simulations and resources). Specifically, we calculated the relative contribution of alleles in each effect size bin (between the gray gridlines), by dividing the contribution of all fixations in the bin by the mutation rate per generation corresponding to that bin. In both Lande and non-Lande cases, long-term stabilizing selection diminishes the contribution of alleles with large effects (red arrows). In the non-Lande case, long-term, weak directional selection greatly amplifies the contribution of alleles with small and moderate effects (blue arrow). See Appendix 3—figures 12–19 for other attributes of the long-term allelic response and for the nonlinear approximations.

We expect the total long-term allelic contribution to equal the shift in optimum, 

Λ

. In our linear Lande approximation, the total contribution is
(21)






2
N
U
⋅
Δ

z

∞


L




=

2
N
U
⋅

∫

0


∞


Δ

z

∞


L


(
a
)
⋅
g
(
a
)
d
a
≈
Λ
⋅


2
N
U
⋅

∫

0


∞


f
(
a
)
⋅
g
(
a
)
d
a



V

A


(
0
)








=

Λ
⋅



∫

0


∞


f
(
a
)
⋅
g
(
a
)
d
a



∫

0


∞


v
(
a
)
⋅
g
(
a
)
d
a


=

Λ

1
+
C


,

where we use the fact that 




V

A


(
0
)
=
2
N
U
⋅

∫

0


∞


v
(
a
)
⋅
g
(
a
)
d
a



 and define
(22)



C
≡



∫

0


∞



v
(
a
)
⋅
g
(
a
)
d
a




∫

0


∞



f
(
a
)
⋅
g
(
a
)
d
a



−
1.

C

 measures the extent to which our approximation underestimates the long-term phenotypic change. We note that 



C
>
0



 for any distribution of allele magnitudes, because 



v
(
a
)
>
f
(
a
)



 for any magnitude 

a

 (Figure 5A), and further that 


C
≪
1


 is a necessary condition for our approximation to be accurate. Given that 


v
⁢

(
a
)



 is appreciably greater than 


f
⁢

(
a
)



 only for 



a
2

⪆
4


 (Figure 5A), this condition implies that for our approximation to be accurate, the vast majority of the genetic variance at equilibrium must arise from alleles with 




a

2


<
4



.

When alleles with larger effects contribute substantially to the variance at equilibrium (and 

C

 is appreciable), Lande’s approximation becomes inaccurate. The prevalence of large effect alleles leads to a quasi-static decay of the mean distance from the new optimum, 

D

, during the equilibration phase (Figure 2D and the section on the Phenotypic response). For the distance during the equilibration phase, and therefore for the deviations from Lande’s phenotypic approximation to be substantial, would require that 


C
≫
1


 (see Section 6 of Appendix 3), which implies that the vast majority (e.g. > 90%) of the genetic variance at equilibrium arises from alleles with large effect sizes, say with 




a

2


≫
4



 (see Figure 5A and Equation 22). Even a small distance 

D

 during the equilibration phase, however, would result in prolonged, weak directional selection that could markedly amplify the difference in fixation probabilities between opposite alleles. Our linear Lande approximation does not account for this amplification, and it could therefore greatly underestimate the total long-term allelic contribution.

## The non-Lande case

We can, however, extend our approximation to account for the amplification in the non-Lande case. To this end, we modify our instantaneous pulse approximation for a pair of opposite alleles (Equation 14) to
(23)


Δ

x

d


∗


(
a
,

x

0


)
≡

x

d


(
a
,

x

0


)
−

x

d


(
−
a
,

x

0


)
≈
2
a

x

0



(

1
−

x

0



)

⋅
(
1
+
A
)
⋅
Λ

/


V

A


(
0
)
,

where the factor 



A
>
0



 accounts for the greater effect of directional selection relative to the Lande case (with the caveat that the justification for the instantaneous pulse approximation is less obvious in the non-Lande case, given prolonged, weak directional selection; see Section 5.2 of Appendix 3). Following the same steps as taken in the Lande case, we then find that the expected long-term (fixed) contribution per unit mutational input of pairs of alleles with a given magnitude and initial MAF is
(24)


Δ

z

∞



(

a
,

x

0



)

≈
2
⋅
(
1
+
A
)
⋅
Λ
⋅
f
(
a
)

/


V

A


(
0
)

and that their expected marginal contribution for a given magnitude is
(25)




Δ
⁢

z
∞
v

⁢

(
a
)


≈





(

1
+
A

)

⋅
Λ
⋅
f

⁢

(
a
)


/

V
A


⁢

(
0
)



,

where the superscript 

v

 denotes that these contributions originate from variation that segregated before the shift in optimum.

In the non-Lande case, the fixation of mutations that arise after the shift in optimum can also contribute substantially (Appendix 3—figure 21B), because prolonged, weak directional selection can produce a substantial difference in the numbers of fixations of mutations with opposite effects. In Section 5.2.2 of Appendix 3, we follow the same approach that applied for standing variation to show that the relative long-term contribution of new mutations with a given magnitude can be approximated by
(26)




Δ
⁢

z
∞
m

⁢

(
a
)


≈




B
⋅
Λ
⋅
f

⁢

(
a
)


/

V
A


⁢

(
0
)



,

where the factor 



B
>
0



 does not dependent on the magnitude (Section 5.2.2 of Appendix 3). Thus, similar to what we found in the Lande case, the function 

f

 approximates how the relative long-term contribution of alleles depends on their magnitudes, but here it applies to both standing variation and new mutations (Figure 5B).

To gain further understanding of the non-Lande case, we consider the joint contribution of standing variation and new mutations. Equating the total contribution with the shift in optimum we find that
(27)


2
N
U
⋅
Δ

z

∞


=

2
N
U
⋅

(

Δ

z

∞


v


+
Δ

z

∞


m



)

≈


1
+
A
+
B


1
+
C


⋅
Λ
=
Λ
,

with 

C

 defined in Equation 22. This implies that 



A
+
B

=
C


 and that the proportional contributions of standing variation and new mutations are 



(

1
+
A

)

/

(

1
+
C

)



 and 


B
/

(

1
+
C

)



, respectively. It also implies that the contribution per unit mutational input of alleles with a given magnitude 

a

 is
(28)




Δ
⁢

z
∞

⁢

(
a
)


=


Δ
⁢

z
∞
v

⁢

(
a
)


+

Δ
⁢

z
∞
m

⁢

(
a
)



≈



(

1
+
C

)

⋅
Δ

⁢

z
∞
L

⁢

(
a
)


=





(

1
+
C

)

⋅
Λ
⋅
f

⁢

(
a
)


/

V
A


⁢

(
0
)



.

Thus, in the linear non-Lande approximation, prolonged weak directional selection amplifies the relative contribution of alleles of any given magnitude by the same factor of 


(

1
+
C

)


 (Figure 5B and Appendix 3—figure 19). 

C

 is therefore an allelic measure of the deviation from Lande’s approximation (see Appendix 3—figures 20 and 21), and, intriguingly, it depends only on the distribution of mutation magnitudes (Equation 22).

In Section 5 of Appendix 3, we show that the linear approximations are accurate when 



a
⋅
(
1
+
A
)
⋅
Λ

/


V

A


(
0
)
≪
1



 (with 


A
=
0


 in the Lande case) and we derive nonlinear approximations that are more accurate when this condition is violated (Figure 4A and Appendix 3—figures 13 and 16). When polygenicity is low, the shift in optimum is large, or effect sizes are large, directional selection causes large relative changes in MAFs, such that the use of the initial MAF in the instantaneous pulse approximation (i.e. in Equations 14 and 23) and the Taylor approximation of fixation probabilities (Equation 17) become inaccurate. Even in these cases, however, the linear approximations capture the salient features of the long-term allelic contribution to phenotypic adaptation (Figure 5 and Appendix 3—figures 13–19).

## Turnover in the genetic basis of adaptation

Notably, our linear approximations capture the dramatic turnover in the genetic basis of adaptation during the equilibration phase (Figure 6). In the long run, the short-term contribution of large effect alleles (


S
=

a
2

⪆
30


) is almost entirely wiped out, and is supplanted by the contribution of moderate effect alleles (



a
2

≈
5


) (Figure 6A and Appendix 3—figures 15 and 19). Moreover, for any given magnitude, the proportional long-term contribution of minor alleles that segregated at low frequencies before the shift is diminished relative to their short-term contribution, all the more so for large effect sizes (Figure 6B and Appendix 3—figure 14). For instance, for an effect size 



a
2

=
35


, minor alleles with initial frequencies below 0.05 account for more than 99% of the short-term contribution but for only ∼10% of the (much smaller) long-term contribution (Figure 6B and Appendix 3—figure 14).

![Figure 6.](https://cdn.elifesciences.org/articles/66697/elife-66697-fig6-v3.jpg)

**Figure 6.:** (
A) The short-term contribution of large effect alleles is supplanted by the contribution of moderate effect alleles. As an illustration, we show the results of the linear approximation for the non-Lande case in Figure 5B (Equations 13 and 28). Specifically, we weight the short- and long-term relative contributions by the density of effect size squared (given 
) and use a linear (rather than log) scale for the effect sizes squared. This way we can see that the decrease in the contribution of large effect alleles (shaded dark gray area) equals the increase in the contribution of moderate effect alleles (shaded blue area). (





E
⁢


(


a
2
)
=
16
B) The proportional long-term contribution of alleles that segregated at low MAFs before the shift is diminished relative to their short-term contribution, an effect most pronounced for large effect sizes. As an illustration, we show the linear approximations for the contribution of alleles with a given effect size as a function of their initial MAF (Equations 12, 19 and 24) for the same non-Lande case as in A, with a shift of 
. To this end, we estimate the amplification factor for standing variation (



Λ
=


2
⁢






V
A
⁢


(
0
)

) using 



1
+
A
all alleles simulations for the non-Lande case (see section on Simulations and resources and Section 5.2 of Appendix 3). In both the Lande and non-Lande cases, long-term stabilizing selection diminishes the contribution of alleles with lower initial MAF and amplifies the contribution of alleles with higher initial MAF (red arrows). In the non-Lande case, prolonged, weak directional selection amplifies the contribution of alleles, regardless of their initial MAF (blue arrow).

We can understand this turnover by considering the effects of stabilizing selection during the equilibration phase (Appendix 2—figure 2). As noted, stabilizing selection on the trait induces selection against minor alleles, which weakens as MAF increases and vanishes at MAF 



=

1
/
2



. Now consider how it affects a pair of alleles with opposite, moderate or large effect. If their initial frequencies are very low, both alleles will have low MAFs at the end of the rapid phase. Consequently, they will both be strongly selected against during the equilibration phase and will almost certainly go extinct (Appendix 2—figure 2). In the long run, their expected contribution to phenotypic adaptation is therefore diminished. In contrast, if the alleles’ initial MAF is sufficiently high, the relative increase in the aligned allele’s frequency by the end of the rapid phase causes it to be subject to substantially weaker selection than is the opposing allele. In the extreme in which the aligned allele has exceeded frequency 


1
/
2


, the direction of selection on it is even reversed (Appendix 2—figure 2). In such cases, the pair’s expected contribution to phenotypic adaptation will be amplified. This reasoning suggests that, for a given magnitude, there is a critical initial MAF such that the long-term contribution of alleles that start above it is amplified and the contribution of those that start below it is diminished (Figure 6B and Appendix 2—figure 3). This critical frequency is lower in the non-Lande case, because prolonged, weak directional selection amplifies the long-term contribution from alleles with any initial MAF.

The turnover among alleles with different magnitudes can be explained in similar terms. Alleles with large magnitudes almost always start from low MAF, because they are subject to strong stabilizing selection before the shift (Figure 4B). Consequently, they are highly unlikely to exceed the critical initial frequency and their expected long-term contribution to phenotypic adaptation is diminished (Figures 5A and 6A). However, changes to the frequencies of these alleles skew the phenotypic distribution, leading to prolonged, weak directional selection that amplifies the long-term contribution of small and moderate effect alleles (Figure 6B). In our linear approximation, this amplification will occur for allele magnitudes that satisfy 





(

1
+
C

)

⋅
f

⁢

(
a
)


⪆

v
⁢

(
a
)




 (Figure 5B). These considerations explain why the contributions of alleles with small and moderate effects supplant those of alleles with large effects (Figures 5A and 6A). They also highlight that deviations from Lande’s approximation are critical to understanding the allelic response, even when they have small phenotypic effects.

## Other properties of the equilibration process

While long-term phenotypic adaptation arises from an excess in fixations of aligned relative to opposing alleles, this excess and the increase in the total number of fixations are typically small relative to the number of fixations at equilibrium (Figure 7). The relative excess of aligned fixations (defined as 



(


π
⁢

(
a
)


-

π
⁢

(

-
a

)



)

/

(


π
⁢

(
a
)


+

π
⁢

(

-
a

)



)



) and the relative increase in total fixations (compared to the expected number at equilibrium) both decrease with increased polygenicity and increase with the shift in optimum and allele magnitude (Figure 7B and C). For sufficiently large effect sizes, practically all fixations are caused by the shift and are of aligned alleles (Figure 7B and C). However, with the exception of extreme cases in which the contribution of alleles of small and moderate effects to genetic variance is negligible, the number of fixations of such large effect alleles and their contribution to phenotypic change will be small (Figures 5 and 7). Typically, most fixations and contribution to phenotypic change will arise from alleles with small and moderate effects (Figures 5 and 7), for which the proportional excess of aligned and total fixations is modest (Figure 7B and C).

![Figure 7.](https://cdn.elifesciences.org/articles/66697/elife-66697-fig7-v3.jpg)

**Figure 7.:** (
A) The fixation probabilities of aligned and opposing alleles segregating before the shift, as a function of their effect size squared. Simulation results were generated using the single alleles simulation, as detailed in Simulations and resources; error bars are not visible because they are smaller than the points. Analytic predictions in all panels were calculated using the nonlinear Lande approximation derived in Section 5.3 of Appendix 3. For large effect sizes, the fixation probabilities become vanishingly small, whereas for small and moderate effect sizes, the difference in the fixation probabilities of alleles with opposing effects is small. (B) The relative excess of fixations of aligned alleles as a function of effect size squared. (C) Polygenic adaptation typically adds a small number of fixations relative to the number at equilibrium. For large effect sizes, the relative increase in number is large, but their absolute number and the corresponding contribution to phenotypic adaptation are extremely small.

In the long run, these fixations move the mean phenotype all the way to the new optimum, and genetic variation around the new optimum returns to equilibrium. A proxy for the approach to equilibrium is the ‘fixed distance from the optimum’, defined as the phenotypic distance of an individual that is homozygous for the ancestral allele at every segregating site; at equilibrium, we expect the fixed distance to be 

0

. Our simulations suggest that, under a broad range of parameter values, the change in fixed distance after the shift is well approximated by an exponential decay with a rate of 


1
/

(

2
⁢
N

)



 per generation (Figure 8 and Appendix 3—figure 28). This approximation is remarkably accurate in the Lande case. In the non-Lande case, the decay is initially slower than the approximation suggests, possibly because the long-term contribution of new mutations (as opposed to standing variation) takes longer to amass. In both cases, the return to equilibrium occurs on a time scale of 


2
⁢
N


 generations after the shift (Figure 8 and Appendix 3—figure 28).

![Figure 8.](https://cdn.elifesciences.org/articles/66697/elife-66697-fig8-v3.jpg)

**Figure 8.:** generations after the shift.



2
⁢
N
The change in fixed distance after the shift estimated using 
all alleles simulations for the Lande and non-Lande cases (see section on Simulations and resources) is compared with an exponential decay with a rate of 
 per generation. See 



1
/


(


2
⁢
N
)
Appendix 3—figure 28 for similar comparisons using a broad range of model parameter values.

## Discussion

Here, we investigated the phenotypic and genetic adaptive response to selection on a highly polygenic quantitative trait in a simple yet highly relevant setting, in which a sudden change in environment shifts the trait’s optimal value. The phenotypic response to selection was previously studied by Lande, 1976. Assuming that phenotypes are normally distributed in the population, he predicted that after the shift the population’s mean phenotype will approach the new optimum exponentially, at a rate that is proportional to the additive genetic variance in the trait. The Normality assumption, however, was only shown to hold in an infinitesimal limit, in which the effect sizes of individual loci are infinitesimally small (see Turelli, 2017 and Section 8 of Appendix 3). We found that when the trait is sufficiently polygenic and the shift in optimum is not too large (relative to genetic variance in the trait), Lande’s prediction is accurate so long as the genetic variance is dominated by loci with small and moderate effect sizes, which are defined based on the selection acting on them before the shift. When these conditions are violated, most notably when loci with large effects contribute markedly to genetic variance, the initial, rapid change in mean phenotype is followed by a pronounced quasi-static phase, governed by changes to the 3rd central moment of the phenotypic distribution, in which the mean phenotype takes much longer to catch up to the new optimum.

We also characterized the genetic basis of these adaptive phenotypic changes. The closest previous work assumed an infinite population size (de Vladar and Barton, 2014; Jain and Stephan, 2015; Jain and Stephan, 2017a; Jain and Stephan, 2017b). As we show, relaxing this assumption leads to entirely different behavior. In infinite populations, small effect alleles, whose equilibrium frequencies are dominated by mutation and are held at 


1
/
2


 before the shift, make the greatest contribution to phenotypic change after the shift (see Introduction). In contrast, in most if not all real (finite) populations (with 



N
e

≪

1
/
u



, where 

u

 is the mutation rate per site per generation), the frequencies of such small effect alleles are dominated by genetic drift rather than mutation. More generally, variation in allele frequencies due to genetic drift, which is absent in infinite populations, critically affects the allelic response to selection.

To study the allelic response, we divided it into two periods: a rapid phase, immediately after the shift, and a subsequent, prolonged equilibration phase. During the rapid phase, the population’s mean distance to the optimum is substantial and changes rapidly. Directional selection on the trait increases the frequency of minor alleles whose effects are aligned with the shift relative to minor alleles with opposing effects (given the same magnitude and initial frequency). By the end of the rapid phase, the cumulative effect of these frequency differences pushes the mean phenotype close to the new optimum, but because this effect is spread over myriad alleles, the frequency difference between any individual pair of opposing alleles is fairly small. Specifically, we found that an allele’s contribution to phenotypic change is proportional to its contribution to phenotypic variance before the shift, implying that alleles with moderate and large effect sizes make the greatest per site contributions to phenotypic change, while alleles with moderate effect sizes experience the greatest frequency changes. The expected frequency differences between opposing alleles is amplified by prolonged, weak directional selection during the subsequent equilibration phase, and this amplification is pronounced when the phenotypic approach to the new optimum deviates markedly from Lande’s approximation.

Over the long run, stabilizing selection on the trait and genetic drift transform these small frequency differences into a small excess of fixed aligned alleles relative to opposing ones, and cumulatively this excess moves the population mean all the way to the new optimum. This transformation process involves a massive turnover in the properties of the contributing alleles. Notably, the transient contributions of large effect alleles are supplanted by contributions of fixed moderate, and to a lesser extent, small effect alleles. In the non-Lande cases, the fixation of mutations that arise after the shift in optimum can also contribute substantially to long-term phenotypic adaptation. These processes take on the order of 


2
⁢

N
e



 generations, after which the equilibrium architecture of genetic variation around the new optimum is restored.

Our finding that large effect alleles almost never sweep to fixation appears at odds with the results of previous studies of similar models. These discrepancies are largely explained by earlier papers considering settings that violate our assumptions, notably about evolutionary parameter ranges. For instance, some studies assume that large effect alleles segregate at high frequencies before the shift in optimum (e.g. Christodoulaki et al., 2019), which is presumably uncommon in natural populations and in any case, violates our assumption that the population is at mutation-selection-drift equilibrium before the shift. Other models implicitly consider quantitative traits of intermediate genetic complexity; while such traits likely exist, there are to our knowledge few well-established examples. Notably, Thornton, 2019 observes sweeps in cases in which the trait is not highly polygenic (violating our assumption that 




2
⁢
N
⁢
U


≫
1


). Relatedly, Chevin and Hospital, 2008 observe sweeps in cases in which a rare mutation of large effect contributes substantially to genetic variance, which violates our assumptions that genetic variation is highly polygenic and is not predominantly effectively neutral (i.e. that alleles with 


S
⪆
1


 contribute substantially). Although it remains to be seen, we believe that this architecture is much less common, given mounting evidence, reviewed in the Introduction, which suggests that traits are often highly polygenic, and other considerations, notably estimates of persistence time (Walsh and Lynch, 2018; Sella and Barton, 2019) and inferences based on human GWASs (Simons et al., 2018; Zeng et al., 2018), which indicate that quantitative genetic variation is not predominantly neutral.

Lastly, Stetter et al., 2018 considered a huge shift in the optimal trait value (e.g. of ∼90 phenotypic standard deviations), resulting in a massive drop in fitness (violating our assumption that 


Λ
⪅


V
S




)—although shifts in optimum need not be that large to result in the fixations of some large effect alleles. While there are many examples of rapid and large environmental fluctuations, e.g., seasonal fluctuations or shifting weather systems, they occur on a much shorter time scale than fixation (although they might have some effect on genetic architecture; see below). In turn, little is known about the magnitude of shifts in optimal trait values over the time scales of large effect, beneficial fixations. While it seems plausible that moderate shifts, which fall within our assumed parameter ranges, are common, we cannot rule out that larger shifts are common as well. The response to such larger shifts is not covered by our analysis and clearly warrants further study.

Other factors that we have not considered may also affect polygenic adaptation. Most notable among them is pleiotropy. Given that quantitative genetic variation affecting one trait often affects many other traits (Bulik-Sullivan et al., 2015; Pickrell et al., 2016; Boyle et al., 2017; Liu et al., 2019; Sella and Barton, 2019), alleles that would have been positively selected because of their effect on the trait under directional selection may be selected against because of their adverse effects on other traits. Moreover, pleiotropy is known to affect the genetic architecture of a given trait at equilibrium (Simons et al., 2018), which we have shown to shape the allelic response to selection on that trait. Pleiotropy is therefore likely to affect which alleles contribute to phenotypic change at the different phases of polygenic adaptation (see Otto, 2004, for related considerations for genetically simple traits). Linkage disequilibrium (LD) may have an effect as well, perhaps most notably for minor alleles with large effects, which start at low frequencies and experience strong directional selection during the rapid phase. Before the shift, large effect alleles located in genomic regions with low recombination and high functional density are more likely to be in LD with, for example, alleles with countervailing effects on the focal trait (Lande, 1975) or deleterious effects on other traits. If this were the case, then directional selection during the rapid phase might be effectively weaker, because it would act on extended haplotypes rather than on individual alleles.

In addition, the demography of a population, notably its size, and the selection pressures on quantitative traits are likely to change over a shorter time scale than it takes the genetic architecture of complex traits to equilibrate. When these changes occur over the 



∼

2
⁢

N
e




 generations preceding a shift in optimal trait value, they may affect the genetic architecture of the trait and consequently its response to selection. Changes in population size influence the number of segregating sites affecting a trait and the distribution of their frequencies and contributions to variance, with more recent population sizes affecting strongly selected variation more than weakly selected variation (Lohmueller, 2014; Simons et al., 2014; Simons and Sella, 2016; Sella and Barton, 2019). The effects of varying selection will depend on the attributes of this variation in ways that await further study.

While the effects of all of these factors on the response to a shift in optimum warrant investigation, we expect the response to follow from the principles we outlined. Notably, we expect the short-term contribution of alleles to phenotypic change to be proportional to their contribution to variance before the shift, and their long-term contribution to arise from differences between the fixation probabilities of alleles with opposite effects, caused by the opposing effects of directional selection on their frequencies. Thus, while all these factors are likely to affect the response, we expect the main features of the dynamics we portrayed to remain largely intact. These features include the role of the 3rd central moment of the phenotypic distribution in slowing down phenotypic adaptation near the new optimum; the transient contribution of large effect alleles to phenotypic adaptation; and the long-term importance of alleles with moderate effects.

As polygenic adaptation in quantitative traits is likely ubiquitous, our conclusions have potentially important implications. One is that, contrary to adaptation mediated by selective sweeps of initially rare, large effect, beneficial alleles (Smith and Haigh, 1974; Kaplan et al., 1989; Braverman et al., 1995; Hermisson and Pennings, 2005; Coop and Ralph, 2012; Berg and Coop, 2015), polygenic adaptation might have minor effects on patterns of neutral diversity at any given point in time (but may affect temporal diversity patterns; Buffalo and Coop, 2019; Buffalo and Coop, 2020). The effects of selected alleles on neutral diversity at linked loci follow from their trajectories (Barton, 2000). Our results indicate that directional selection on a highly polygenic trait introduces only small changes to allele frequencies at individual loci, which amount to minor perturbations to the allele trajectories expected under stabilizing selection at equilibrium (also see Chevin and Hospital, 2008; Thornton, 2019). Indeed, alleles with large effects exhibit only small, transient changes. For those with more moderate effects, there is a modest, long-term excess of fixations of those alleles whose effects are aligned with the shift relative to those whose effects are opposed, accompanied by a small increase in the total number of fixations (Figure 7). The trajectories of the alleles that fix are largely driven by weak stabilizing selection and tend to be drawn out (Figure 8). Thus, our results indicate that the effects of polygenic adaptation on neutral diversity should be minor (other than perhaps for massive shifts in optimal trait values, as noted above).

In contrast, long-term stabilizing selection on quantitative traits likely has substantial effects on neutral diversity patterns. Specifically, selection against minor alleles induced by stabilizing selection may well be a major source of background selection and is expected to affect neutral diversity patterns in ways that are similar to those of background (purifying) selection from other selective origins (Charlesworth et al., 1993; Hudson and Kaplan, 1995; Santiago and Caballero, 1998; McVean and Charlesworth, 2000).

Another implication of our results pertains to the search for the genetic basis of human adaptation, as well as adaptation in other species. Efforts to uncover the identity of individual adaptive genetic changes on the human lineage were guided by the notion that their identity would offer insight into what ‘made us human’. Under the plausible assumption that many adaptive changes on the human lineage arose from selection on complex, quantitative traits, this approach may not be as informative as it appears (Pritchard et al., 2010; Boyle et al., 2017). Our results indicate that after a shift in the optimal trait value, the number of fixations of alleles whose effects are aligned with the shift are typically nearly equal to the number of alleles that are opposed (Figure 7A). Moreover, the alleles that fix are a largely random draw from the vastly greater number of alleles that affect the trait, both in the sense of being those that happened to segregate at high MAFs at the onset of selection and because of the stochasticity of fixation. Thus, in this plausible scenario, it becomes meaningless to say that any given fixation was adaptive, and arguably uninteresting to focus on the particular subset of alleles that happened to reach fixation. In contrast, identifying the traits that experienced adaptive changes promises to provide important insights. Recent efforts to do so pool the signatures of frequency changes over many loci that were found to be associated with a given trait in GWAS (Turchin et al., 2012; Berg and Coop, 2014; Robinson et al., 2015; Field et al., 2016; Berg et al., 2019b; Edge and Coop, 2019; Speidel et al., 2019), an exciting approach that has also proven to be technically challenging (Berg et al., 2019a; Sohail et al., 2019). A better understanding of the process of polygenic adaptation should help to guide such efforts.
