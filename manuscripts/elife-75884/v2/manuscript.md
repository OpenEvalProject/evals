# Speed variations of bacterial replisomes

## Authors

- Deepak Bhat<sup>1</sup> ([ORCID: 0000-0001-9387-4951](https://orcid.org/0000-0001-9387-4951))
- Samuel Hauf<sup>3</sup> ([ORCID: 0000-0002-3034-8441](https://orcid.org/0000-0002-3034-8441))
- Charles Plessy<sup>4</sup> ([ORCID: 0000-0001-7410-6295](https://orcid.org/0000-0001-7410-6295))
- Yohei Yokobayashi<sup>3</sup> ([ORCID: 0000-0002-2417-1934](https://orcid.org/0000-0002-2417-1934))
- Simone Pigolotti<sup>1</sup> ([ORCID: 0000-0002-6157-6906](https://orcid.org/0000-0002-6157-6906)) †

### Affiliations

1. Biological Complexity Unit, Okinawa Institute of Science and Technology Onna Japan ([ROR:02qg15b79](https://ror.org/02qg15b79))
2. Department of Physics, School of Advanced Sciences, Vellore Institute of Technology Vellore, Tamil Nadu India ([ROR:00qzypv28](https://ror.org/00qzypv28))
3. Nucleic Acid Chemistry and Engineering Unit, Okinawa Institute of Science and Technology Onna Japan ([ROR:02qg15b79](https://ror.org/02qg15b79))
4. Genomics and Regulatory Systems Unit, Okinawa Institute of Science and Technology Onna Japan ([ROR:02qg15b79](https://ror.org/02qg15b79))

† Corresponding author

## Abstract

Replisomes are multi-protein complexes that replicate genomes with remarkable speed and accuracy. Despite their importance, their dynamics is poorly characterized, especially in vivo. In this paper, we present an approach to infer the replisome dynamics from the DNA abundance distribution measured in a growing bacterial population. Our method is sensitive enough to detect subtle variations of the replisome speed along the genome. As an application, we experimentally measured the DNA abundance distribution in Escherichia coli populations growing at different temperatures using deep sequencing. We find that the average replisome speed increases nearly fivefold between 17 °C and 37 °C. Further, we observe wave-like variations of the replisome speed along the genome. These variations correlate with previously observed variations of the mutation rate, suggesting a common dynamical origin. Our approach has the potential to elucidate replication dynamics in E. coli mutants and in other bacterial species.

## Introduction

Every cell must copy its genome in order to reproduce. This task is carried out by large protein complexes called replisomes. Each replisome separates the two DNA strands and synthesizes a complementary copy of each of them, thereby forming a Y–shaped DNA junction called a replication fork. The speed and accuracy of replisomes is impressive (Baker and Bell, 1998). They proceed at several hundreds to one thousand base pairs per second (Pham et al., 2013; Elshenawy et al., 2015), with an inaccuracy of about one mis-incorporated monomer every 10 billion base pairs (Schaaper, 1993). In bacteria, two replisomes initiate replication at a well-defined origin site on the circular genome, progress in opposite directions, and complete replication upon encountering each other in a terminal region.

The initiation and the completion of DNA replication conventionally delimit the three stages of the bacterial cell cycle (Dewachter et al., 2018; Wang and Levin, 2009). The first stage, B, spans the period from cell birth until the initiation of DNA replication. The second stage, C, encompasses the time needed for replication. The last phase, D, begins at the end of DNA replication and concludes with cell division. While it is established that DNA replication and the cell cycle must be coordinated, their precise relation has been a puzzle for decades (Willis and Huang, 2017). A classic study by Cooper and Helmstetter, 1968 finds that, upon modifying the growth rate by changing the nutrient composition in Escherichia coli, the durations of stages C and D remain constant at about 40 min and 20 min, respectively. This means that the replisome speed must be unaffected by the nutrient composition, at least on average. When the cell division time is shorter than one hour, DNA replication is initiated in a previous generation. This implies that, in fast growth conditions, multiple pairs of replisomes simultaneously replicate the same genome (Fossum et al., 2007). Tuning the growth rate by changing the temperature has a radically different effect on bacterial physiology. For example, in vivo (Pierucci, 1972) and in vitro (Yao et al., 2009) studies show that the speed of replisomes is affected in this case.

More precise features of replisome dynamics, such as whether their speed is approximately constant or varies along the genome, are important to determine the location of their encounter point and the distribution of replication errors on the genome (Niccum et al., 2019; Dillon et al., 2018). However, this detailed information is hard to obtain (Pham et al., 2013). One way for inferring it is to measure the DNA abundance distribution, that is the frequency of DNA fragments along the genome in an exponentially growing cell population. In fact, the frequency of these fragments in the population depends on the proportions of synthesizing genomes of different lengths, which in turn depend on the replisome dynamics. Previous studies have used the DNA abundance distribution to understand the functioning of bacterial replication and how different proteins assist completion of DNA replication (Wendel et al., 2014; Wendel et al., 2018; Rudolph et al., 2013; Midgley-Smith et al., 2019; Midgley-Smith et al., 2018). However, these studies focused on qualitative analysis of the observed changes of the DNA distribution in knockout mutants with respect to the wild type, and did not attempt to predict the shape of the distribution using quantitative theoretical models. The DNA abundance distribution has also been used to identify actively growing species in a microbiome (Korem et al., 2015).

In this paper, we introduce a method to infer the replisome dynamics from the DNA abundance distribution. As an application, we experimentally measured the DNA abundance distribution of E. coli growing at different temperatures between $17⁢Co$ and $37⁢Co$ using high-throughput sequencing. Our approach, combined with our experiments, shows that the average speed of replisomes exhibits an Arrhenius dependence on the temperature, with an almost fivefold variation in the range we considered. Moreover, the precision of our experiments reveals that the speed of replisomes varies along the genome in a seemingly periodic and highly repeatable fashion around this average value. We find that this pattern is highly correlated with previously observed wave-like variations of the single base pair mutation rate along the bacterial genome (Niccum et al., 2019; Dillon et al., 2018). We discuss possible common causes for these two patterns.

## Results

### Distribution of genome types

We consider a population of bacteria that grow exponentially in a steady environment. Each cell in the growing population can encompass three types of genomes, see Figure 1a and Figure 1b: (i) one template genome, that is, the genome that the cell inherited at its birth. (ii) incomplete genomes, that is, genomes which are being synthesized. (iii) post-replication genomes that will be passed to new cells and become their templates.

![Figure 1.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig1-v2.jpg)

**Figure 1.:** (a) Cell cycle. In slow growth conditions (top panel), newborn cells contain a template (stage B, red). As the cell cycle progresses, two replisomes synthesize a new genome (stage C, blue) starting from the origin on the template (yellow spot). When replication terminates, cells contain the original template and a post-replication genome (stage D, green). Upon subsequent cell division, the post replication genome becomes the template for the newborn cell. In fast growth conditions (bottom panel), newborn cells acquire a template which is already undergoing synthesis. In subsequent stages, multiple replicating genomes may exist in the same cell. (b) Composition of genomes in an exponentially growing population of cells. Each cell may contain a different number of genomes, depending on its stage in the cell cycle and growth conditions. (c) Dynamics of genome types. Dashed blue arrow represent initiation of replication. The dotted green arrow represents completion of replication. The solid red arrow represents cell division. (d) Replisome dynamics. Two replisomes begin replication at an origin and progress in opposite directions. Their speed may depend, in general, on their genome coordinate. (e) Sketch of the DNA abundance distribution as a function of the genome coordinate. All three types of genomes contribute to the DNA abundance distribution. Because of incomplete genomes, the DNA abundance is largest at the origin and smallest at the terminal region (i.e., towards the periphery). (f) Experimental DNA abundance distribution at different temperatures.

In nutrient-rich conditions, bacteria replicate their genome in parallel, so that the numbers of incomplete genomes and post-replication genomes per cell are variable, see Figure 1b. The classic Cooper-Helmstetter model (Cooper and Helmstetter, 1968) describes the dynamics of these genomes in a given cell through generations. We adopt a different approach and focus on the abundance dynamics of the three types of genomes in the whole population. We call $N_{T}⁢(t)$, $N_{S}⁢(t)$, $N_{P}⁢(t)$ the total number of template genomes, incomplete (synthesizing) genomes, and post-replication genomes, respectively, that are present in the population at time $t$. Our first aim is to quantify the relative fractions of these three types of genomes.

The total number of genomes is $N(T)=N_{T}(t)+N_{S}(t)+N_{P}(t)$. Since each cell contains exactly one template, the total number of cells is equal to $N_{T}(t)$. The total number of genomes evolves as effect of: (a) replication initiation, which creates new synthesizing genomes at a rate $k$; (b) completion of replication, which transforms synthesizing genomes into post-replication ones at rate β; and (c) cell division, which turns post-replication genomes into templates at a rate α, see Figure 1c. This dynamics is described by the set of equations:

$$
\frac{d}{dt}N_{T}(t)=\alphaN_{P}
$$



$$
\frac{d}{d⁢t}⁢N_{S}⁢(t)=k⁢N-\beta⁢N_{S}
$$



$$
\frac{d}{d⁢t}⁢N_{P}⁢(t)=\beta⁢N_{S}-\alpha⁢N_{P}.
$$

It follows from Equations 1–3 that, in steady growth, the total number of genomes grows exponentially at a rate equal to the fork firing rate $k$. In this exponential regime, the fractions of the three genome types are constant:

$$
\frac{N_{T}⁢(t)}{N⁢(t)}=\frac{\alpha⁢\beta}{(k+\beta)⁢(k+\alpha)}
$$



$$
\frac{N_{S}⁢(t)}{N⁢(t)}=\frac{k}{(k+\beta)}
$$



$$
\frac{N_{P}⁢(t)}{N⁢(t)}=\frac{\beta⁢k}{(k+\beta)⁢(k+\alpha)}.
$$

The ratio $N/N_{T}$ can be interpreted as the average number of genomes per cell. Since this ratio is constant, the fork firing rate $k$ can also be identified as the exponential growth rate of the number of cells. For this reason, from now on, we refer to $k$ as the ‘fork firing rate’ or the ‘growth rate’ interchangeably.

In principle, the rates α, β, and $k$ should depend on the ‘age’ of each genome, that is the time spent by the genome in each stage. In Appendix 1, we generalize our model to an age-dependent model to account for this fact. We find that this age-dependent model is equivalent to Equations 1–3 in the exponential growth regime. This result supports the use of our simple model of genome-type dynamics.

We now analyze the incomplete genomes in more detail. We call $x_{1}$ and $x_{2}$ the portions of a given incomplete genome copied by the two replisomes at a given time, with $0\leqx_{1},x_{2}\leqL$, see Figure 1d. Replication initiates at $x_{1}=x_{2}=0$ and completes once the replisomes meet each other, that is, $x_{1}+x_{2}=L$. The replisome dynamics proceeds as follows. Each replisome is characterized by a speed which depends, in principle, on the replisome position (be it $x_{1}$ or $x_{2}$) and by a diffusion coefficient representing random fluctuations of the speed. The coordinates $x_{1},x_{2}$ of the two replisomes evolve according to the stochastic differential equations:

$$
\frac{d}{d⁢t}⁢x_{1}⁢(t)=v⁢(x_{1})+\sqrt{2⁢D}⁢ξ_{1}⁢(t)\frac{d}{d⁢t}⁢x_{2}⁢(t)=v⁢(x_{2})+\sqrt{2⁢D}⁢ξ_{2}⁢(t),
$$

where $ξ_{1}⁢(t)$ and $ξ_{2}⁢(t)$ are white noise variables satisfying $⟨ξ_{1}⁢(t)⟩=⟨ξ_{2}⁢(t)⟩=0$, $⟨ξ_{1}⁢(t)⁢ξ_{1}⁢(t^{′})⟩=⟨ξ_{2}⁢(t)⁢ξ_{2}⁢(t^{′})⟩=\delta⁢(t-t^{′})$, and $⟨ξ_{1}⁢(t)⁢ξ_{2}⁢(t^{′})⟩=0$. Here, $⟨…⟩$ denotes an average over realizations.

Close to thermodynamic equilibrium, the diffusion coefficient $D$ can be estimated by the Stokes-Einstein relation (Hynes, 1977). However, since replisomes are driven far from equilibrium by hydrolysis of dNTPs, their diffusion coefficient could deviate from this estimate. In the absence of fluctuations ($D=0$), each of the two replisomes copies exactly half of the genome, whereas for $D>0$ their meeting point is characterized by a certain degree of uncertainty.

In steady exponential growth, we call $p^{st}⁢(x_{1},x_{2})$ the stationary probability distribution of finding an incomplete genome with copied portions x1 and x2. This probability distribution satisfies the equation:

$$
\nabla→⋅[v→⁢p^{st}]+D⁢\nabla^{2}⁡p^{st}-k⁢p^{st}=0,
$$

where we introduce the vector notation $v→=(v⁢(x_{1}),v⁢(x_{2}))$ and $\nabla→=(\partial/\partial⁡x_{1},\partial/\partial⁡x_{2})$. The last term in the right hand side of Equation 8 is a dilution term that accounts for the exponential increase in newborn cells. We formally derive Equation 8 and discuss its boundary conditions in Methods.

### DNA abundance distribution

The DNA abundance distribution $A(y)$ is the probability that a small DNA fragment randomly picked from the population originates from genome position $y$, see Figure 1e. We define the genome coordinate $y\in[-L/2,L/2]$, where $y=0$ corresponds to the origin of replication and $L$ is the genome length. Templates and post-replication genomes yield a uniform contribution to the distribution $A(y)$ (red and green in Figure 1e). In contrast, incomplete genomes contribute in a way that depends on the replisome positions along the genomes (blue in Figure 1e). Our experiments permit to measure the distribution $A(y)$ with high accuracy, see Figure 1f and Methods.

To express the distribution $A(y)$ in our model, we first introduce the probability $P(y)$ that a randomly chosen genome (either complete or incomplete) in the population includes the genome location $y$. This probability is expressed by

$$
P(y)=\frac{k}{\beta+k}[\int_{|y|}^{L}dx_{1}\int_{0}^{L−x_{1}}dx_{2} p^{st}(x_{1},x_{2})⏞ycopiedby1^{st}replisome+\int_{L−|y|}^{L}dx_{2}\int_{0}^{L−x_{2}}dx_{1} p^{st}(x_{1},x_{2})⏞ycopiedby2^{nd}replisome]+\frac{\beta}{k+\beta}⏞yinacompletegenome .
$$

where the two terms in square brackets reflect the fact that either of the replisomes can in principle have copied position $y$, and we used that a randomly chosen genome is complete with probability $(1-N_{S}/N)=\beta/(k+\beta)$, see Equation 5. The DNA abundance distribution $A(y)$ is proportional to $P(y)$, up to a normalization constant:

$$
A(y)=\frac{P(y)}{\int_{−L/2}^{L/2}P(y^{′})dy^{′}}.
$$

For given choices of $v⁢(x)$, $D$, and $k$, our theory permits to compute the distribution of incomplete genomes $p^{st}⁢(x_{1},x_{2})$ via Equation 8. From this solution, we can also calculate β as the steady rate at which replisomes complete replication (see Methods). This information can be used to compute the DNA abundance distribution $A(y)$ using Equation 10. Therefore, by experimentally measuring the DNA abundance distribution, we can test our hypotheses on the speed function $v⁢(x)$ and the diffusion coefficient $D$.

### Constant speed model

We first consider a scenario in which replisomes progress at a constant speed $v¯$ and without fluctuations, $D=0$. We find that, in this case, the DNA abundance distribution is expressed by

$$
A(y)=\frac{k}{2v¯[1−e^{−kL/2v¯}]}e^{−k|y|/v¯} ,
$$

see Methods. We fit this distribution to the experimental data using maximum likelihood, see Figure 2a. The speed $v¯$ is the only fitting parameter, because we independently measure the exponential growth rate $k$ from the optical density, see Methods.

![Figure 2.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig2-v2.jpg)

**Figure 2.:** (a) DNA abundance distribution for $T=37⁢Co$. Orange circles represent experimental data. The solid black line is the prediction of our model assuming constant speed and $D=0$. Fits are performed using a maximum likelihood method, see Appendix 2 for details. The quality of fits for replicates and other temperatures is comparable, see Figure 2—figure supplement 1, Figure 2—figure supplement 2, and Figure 2—figure supplement 3. In particular, fits of replicates yield similar values of the speed $v¯$. (b) Replisome speed as a function of temperature. Error bars represent sample-to-sample variations. (c) Comparison of the temperature-dependence of speed and growth rate (see Methods for details on the growth rate estimation). The solid curves are fits of Arrhenius laws to the data. The fitted parameters are $A=(2.5\pm5.3)\times10^{8}⁢bp⁢s^{-1}$, $Δ_{R}=(50\pm5)⁢kJmol^{-1}$, $B=(6.0\pm24.9)\times10^{12}⁢hr^{-1}$ and $Δ_{C}=(74\pm10) kJmol^{−1}$. We exclude the data point for $T=17⁢Co$ in both fits. (d) Estimated number of replisomes per complete genome at different temperatures. The red triangles represents the estimate from Equation 19 in which we use the expression of β for the constant speed model, Equation 22. The black circles are the estimates from Equation 20.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** DNA abundance distribution at different temperatures.Bias elimination is carried out using the DNA abundance of the stationary cells grown at temperature $17^{o}⁢C$. Symbols are from experiments, and the solid black lines are predictions of the constant speed model. The DNA abundance distribution presented in Figure 1d, Figure 2a, and Figure 3 corresponds to Sample 1 (top panel).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** DNA abundance distribution at different temperatures. Bias elimination is carried out using the DNA abundance of the stationary cells grown at temperature $27^{o}⁢C$. Symbols are from experiments, and the solid black lines are predictions of the constant speed model.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** DNA abundance distribution at different temperatures. Bias elimination is carried out using the DNA abundance of the stationary cells grown at temperature $37^{o}⁢C$. Symbols represent experimental data. The solid black lines are the predictions of the constant speed model.

We find that the speed increases nearly fivefold with temperature in the range we considered and appears to follow an Arrhenius law, see Figure 2b. This behavior resembles that of the growth rate. The effective activation energy characterizing the cell cycle is larger than that characterizing the replisome speed, see Figure 2c, possibly due to the large number of molecular reactions involved in the cell cycle. The data point at 17°C appears to deviate from the Arrhenius law for both the speed and the growth rate (Roy et al., 2021), see Figure 2c.

As seen in Figure 2c, the replisome speed does not increase as fast as the growth rate at increasing temperature. This observation suggests that the number of replisomes per genome should increase with temperature to compensate for this gap. Indeed, in the temperature range we studied, our model predicts that the average number of replisomes per complete genome increases from two to almost six, see Figure 2d and Methods.

We now focus on the average genome content per cell. Since the model assumes that genomes evolve independently, the average DNA content per cell $C$ is the product of the average genome length $ℓ$ times the average number of genomes per cell $N/N_{T}$. Computing the average genome length in the model (see Methods) and using Equation 4 for the average number of genomes per cell, we obtain that the average DNA content per cell is expressed by

$$
C=\frac{2v¯}{k}\frac{k+\alpha}{\alpha}[e^{kL/(2v¯)}−1].
$$

The classic Cooper-Helmstetter model (Cooper and Helmstetter, 1968) predicts the DNA content per cell assuming constant durations of stages B, C, and D of the cell cycle. Since we assumed constant speed and $D=0$, the duration of the replication cycle $L/(2⁢v¯)$ is constant in our case as well. As a consequence, the prediction of Equation 12 is equivalent to that of the Cooper-Helmstetter model (see Appendix 3).

It is generally believed that the ratio between the average DNA content per cell $C$ and the protein content per cell should be maintained approximately constant at varying physiological conditions. This implies that $C$ should be proportional to the cell size. If the growth rate is varied by changing the nutrient composition, $v¯$ remains constant (Cooper and Helmstetter, 1968). Equation 12 then predicts an approximately exponential growth of $C$ with $k$, which is consistent with observations. In this case, the Schaechter–Maaloe–Kjeldgaard growth law states that the cell size grows exponentially with $k$ (Schaechter et al., 1958), thereby ensuring DNA-protein homeostasis. In the case of varying temperature, we find that $v¯$ and $k$ present a similar dependence on $T$ (see Figure 2c), so that their ratio and thereby $C$ weakly depends on $k$ (see Appendix 3—figure 1). Our result is consistent with observations showing that, at increasing temperature, the cell size remains approximately constant (Shehata and Marr, 1975) or possibly slightly increases (Trueba et al., 1982).

### Oscillating speed model

The assumption of constant speed leads to a rather good fit of our DNA abundance data. However, the precision of our data permits us to appreciate systematic deviations from the model predictions under the constant speed hypothesis, see Figure 3a-e. These deviations appear as regular oscillations as a function of the genome coordinate. They are evident at all the temperatures we studied except for $17⁢Co$, where they are barely visible. They are highly repeatable (see Figure 3—figure supplement 1, Figure 3—figure supplement 2 and Figure 3—figure supplement 3) and approximately symmetric with respect to the origin of replication. We also analyzed previous experimental data from Midgley-Smith et al., 2018. We observed clear oscillations for experiments in nutrient-rich LB medium, but not for experiments in M9 minimal medium, see Figure 3—figure supplement 4. This analysis further supports that this phenomenon is robust, at least in fast growth conditions.

![Figure 3.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig3-v2.jpg)

**Figure 3.:** (a–e) Colored lines: ratios of the experimental DNA abundance over the corresponding prediction assuming constant speed and $D=0$. The solid black lines represent the ratios of the predictions assuming oscillatory speed, Equation 13 and $D\geq0$, over constant speed and $D=0$. Corresponding plots for replicates and other temperatures are presented in Figure 3—figure supplement 1, Figure 3—figure supplement 2 and Figure 3—figure supplement 3. (f–j) Experimental DNA abundance distribution at different temperatures. The solid black lines are the fits of the oscillatory speed model. Tests based on the Akaike information criterion show that the oscillatory speed model should be chosen over the constant speed model for all the replicates and at all temperatures, see Figure 3—figure supplement 5. The fitted parameters are reported in Table 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Ratios of the experimental DNA abundance over the corresponding fit assuming constant speed and $D=0$. The solid black lines represent the ratios of the predictions assuming oscillatory speed over constant speed. The data here is for the stationary temperature $17^{o}⁢C$. The discrepancy ratios presented in Figure 3 are for Sample 1 (topmost panel).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Ratios of the experimental DNA abundance over the corresponding prediction assuming constant speed and $D=0$. The solid black lines represent the ratios of the predictions assuming oscillatory speed over constant speed. The data here is for the stationary temperature $27^{o}⁢C$.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Ratios of the experimental DNA abundance over the corresponding prediction assuming constant speed and $D=0$. The solid black lines represent the ratios of the predictions assuming oscillatory speed over constant speed. The data here is for the stationary temperature $37^{o}⁢C$.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** DNA abundance distribution from the data reported in Midgley-Smith et al., 2018 for E. coli growing in a Luria broth (LB) medium (a) and minimal (M9) medium (b). The solid black line is the prediction from the constant speed model. The reported growth rates are $k=2.15\pm0.18⁢hr^{-1}$ for LB and $k=0.6\pm0.05⁢hr^{-1}$ for M9 (Midgley-Smith et al., 2018). Substituting this value in our model we obtain the average speed $v¯=1306\pm115⁢b⁢p⁢s^{-1}$ for LB and $v¯=837\pm75⁢b⁢p⁢s^{-1}$ for M9. Ratios of the experimental DNA abundance over the prediction of the constant speed model for LB in (c) and M9 in (d). The solid black lines in (c) and (d) represent the ratios of the predictions assuming oscillatory speed over constant speed. The estimated parameters of the oscillatory speed model for LB are, $v¯=1301\pm115⁢b⁢p⁢s^{-1}$, $\delta=0.14\pm0.02$, $\omega=3.2⁢rad⁢Mbp^{-1}$ $ϕ=1.3⁢rad$ and $D=16\pm14⁢k⁢b⁢p^{2}⁢s^{-1}$. Similarly the parameters of the oscillatory speed model for M9 are,$v¯=831\pm75⁢b⁢p⁢s^{-1}$, $\delta=0.07\pm0.01$, $\omega=3.19⁢rad⁢Mbp^{-1}$, $ϕ=2.9⁢rad$ and $D=0$.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** Statistical comparison between the constant speed model and oscillatory model by means of the Akaike information criterion. The Akaike information is defined as $I=2⁢[n_{p}-ln⁡(ℒ_{m})]$, where np is the number of fitted parameters in a model and $ℒ_{m}$ is the maximum likelihood. The constant speed model includes a single free parameters $(n_{p}=1)$ versus five $(n_{p}=5)$ for the oscillatory speed model. The Akaike information criterion prescribes that, given a set of candidate models, one should prefer the one characterized by the minimum Akaike information. The Akaike information for the constant speed model, $I⁢(Con)$, is larger than that for the oscillatory speed model, $I⁢(Osc)$, for all temperatures. The stationary data used for bias elimination correspond to temperatures (a) 17°C, (b) 27°C, and (c) 37°C.

To account for these observations, we introduce a more refined model in which the replisome speed oscillates along the genome:

$$
v⁢(x)=v¯⁢[1+\delta⁢cos⁡(\omega⁢x+ϕ)],
$$

where δ represents the relative amplitude of oscillations; ω their angular frequency along the genome; and $ϕ$ their initial phase. We also take into account random speed fluctuations in this case, $D\geq0$. In this case, we predict the DNA abundance distribution using stochastic simulations, see Methods. By fitting the DNA abundance, we estimate the parameters $v¯$, δ, ω, $ϕ$, and $D$, see Figure 3(f–j) and Table 1.

**Table 1.**
 Parameters of the oscillatory speed model.Temperatures are expressed in $Co$, $v¯$ in $bp⁢s^{-1}$, ω in $rad⁢Mbp^{-1}$, $ϕ$ in $rad$, and $D$ in $kbp^{2}⁢s^{-1}$. Reported values are averages and standard deviations over experimental replicates. The oscillatory and constant speed models yield estimates of the parameter $v¯$ that are consistent with each other, see Appendix 4—table 1.


<table>
  <thead>
    <tr>
      <th>T</th>
      <th>v¯</th>
      <th>δ</th>
      <th>ω</th>
      <th>ϕ</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>17</td>
      <td>246±33</td>
      <td>0.22±0.13</td>
      <td>0.7±0.5</td>
      <td>3.3±1.0</td>
      <td>0.39±0.43</td>
    </tr>
    <tr>
      <td>22</td>
      <td>351±30</td>
      <td>0.20±0.06</td>
      <td>2.7±0.6</td>
      <td>3.4±0.6</td>
      <td>0.81±1.18</td>
    </tr>
    <tr>
      <td>27</td>
      <td>541±30</td>
      <td>0.18±0.03</td>
      <td>4.7±0.1</td>
      <td>2.1±0.1</td>
      <td>0.35±0.49</td>
    </tr>
    <tr>
      <td>32</td>
      <td>821±66</td>
      <td>0.11±0.04</td>
      <td>5.5±0.2</td>
      <td>1.5±0.1</td>
      <td>1.15±1.23</td>
    </tr>
    <tr>
      <td>37</td>
      <td>970±51</td>
      <td>0.17±0.03</td>
      <td>4.3±0.2</td>
      <td>3.0±0.2</td>
      <td>2.90±2.48</td>
    </tr>
  </tbody>
</table>

Our fitted speed oscillations are reminiscent of a previously observed wave-like pattern in the mutation rate along the genome of different bacterial species (Dillon et al., 2018; Niccum et al., 2019). For a quantitative comparison, we analyze this pattern in a mutant E. coli strain lacking DNA mismatch repair (Niccum et al., 2019). We find that the oscillations in mutation rate and speed are highly correlated, see Figure 4a. The mutation rate appears approximately in phase with the speed, meaning that regions where replisomes proceed at higher speed are characterized by a higher mutation rate. This observation leads to the hypothesis that the two phenomena have a common cause.

![Figure 4.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig4-v2.jpg)

**Figure 4.:** (a) Solid lines: relative speeds $v⁢(|y|)/v¯$ along the genome (Red: T = 22°C, sky blue: T = 27°C, brown: T = 32°C, and orange: T = 37°C). We omitted the curve for T = 17°C as the oscillations are less evident in this case (see Figure 4—figure supplement 1). The wave-like pattern of the speed is quantitatively similar to the variations of the mutation rate along the genome (green triangles, from Niccum et al., 2019; Pearson correlation coefficients between speed and mutation rate: $r_{22C}=0.42$; $r_{27C}=0.84;r_{32C}=0.80$ and $r_{37C}=0.69$). The mutation rate is defined as the number of base pair substitutions per generation per kilo base pairs. The solid green line is a fit to the mutation rate data with the same function as in Equation 13. The fit parameters are $v¯=2.4⁢kbp^{-1}⁢gen^{-1}$, $\delta=0.18$, $\omega=4.9⁢rad⁢Mbp^{-1}$ and $ϕ=1.93⁢rad$. (b) Temperature dependence of angular frequency of oscillation ω (squares). (c) phase $ϕ$ (squares). Green triangles in (b) and (c) represent the angular frequency and phase, respectively, from the fit to the mutation rate data with Equation 13. (d) Diffusion coefficient $D$. Circles represent individual fitted values of diffusion coefficients. Blue circles represent cases in which the fitted value of $D$ is either zero or not significant (see SI). This occurs in two out of nine cases for 37°C and three out of nine cases for each of the other temperatures.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Results of the oscillatory speed model. This figure is same as Figure 4a, but with additional curve for $T=17^{o}$ C. Solid lines: relative speeds $v⁢(|y|)/v¯$ along the genome (Pink: $T=17^{o}$ C, Red: $T=22^{o}$ C, sky blue: $T=27^{o}$ C, brown: $T=32^{o}$ C, and orange: $T=37^{o}$ C).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Statistical comparison between the oscillatory model with diffusion ($D>0$) and without diffusion ($D=0$) by means of the Akaike information criterion. The number of parameters is four $(n_{p}=4)$ for $D=0$ and five $(n_{p}=5)$ for $D>0$. Difference between Akaike information $I$ for $D>0$ and $D=0$. If this difference is negative, the model with $D>0$ should be preferred. The stationary data used for bias elimination correspond to temperatures 17°C in (a), 27°C in (b) and 37°C in (c).

We consider two possible explanations for these oscillations. The first is that the oscillations originate from a systematic process related with the cell cycle (Niccum et al., 2019). The second explanation is that the oscillations are caused by competition among replisomes for nucleotides or other molecules required for replication. Assuming approximately constant cell division times, we estimate the cell division time as $\tau=(ln⁡2)/k$. Since $k$ is also equal to the fork firing rate per genome, the time between firing events in a cell is also approximately equal to τ, so that the two hypotheses lead to the same quantitative prediction. If the speed of replisomes was coupled to a factor oscillating with period τ, this would cause spatial oscillation of speed with angular frequency $\omega=2⁢\pi/(v¯⁢\tau)=2⁢\pi⁢k/[(ln⁡2)⁢v¯]$. This prediction qualitatively agrees with our fitted values of ω, see Figure 4b.

If the wave-like pattern were caused by competition among replisomes, one would expect either a minimum of the speed every time a new fork is fired ($ϕ=\pi$) or the speed to start decreasing when a new fork is fired ($ϕ=\pi/2$). Our fitted values of the phase $ϕ$ are also compatible with this range, see Figure 4c.

Our results show that the diffusion coefficient $D$ is quite small. For about one third of our experimental realizations at each temperature, our fitted value of $D$ is not significant according to the Akaike information criterion (see Figure 4d and Figure 4—figure supplement 2). For comparison, we estimate the equilibrium diffusion constant of replisomes in the cytoplasm from the Stokes-Einstein relation as $D_{SE}≈6kbp^{2}s^{−1}$ (see Appendix 5), of the same order of magnitude as our fitted values, see Table 1 and Figure 4. These results suggest that, despite their high average speed, the fluctuations of the replisome position are remarkably similar to the equilibrium case.

The diffusion coefficient determines the uncertainty about the genome site where the two replisomes meet. In the absence of diffusion ($D=0$), replisomes would always meet at the midpoint on the circular genome. For $D>0$, we estimate the typical size $l_{D}$ of the region in which the two replisomes meet as follows. Since the fitted values of δ and $D$ are both small, we approximate the replication time as $\tau_{C}≈L/(2⁢v¯)$. In this time, the accumulated uncertainty due to diffusion is equal to $l_{D}≈2⁢\sqrt{2⁢D⁢\tau_{D}}$. From our estimated diffusion coefficients and average velocities, we obtain values of $l_{D}$ on the order of $100−200kbp$, depending on temperature.

We remark that our bacterial cultures are grown in LB medium. Although the growth curves appear exponential before saturating (see Methods), the nutrient composition can be such that the assumption of steady growth made in our model is not valid. It is therefore important to scrutinize whether the oscillations can be a consequence of this issue. To this aim, we analyzed a version of the model in which the fork firing rate is not steady, but gradually declines with time, see Appendix 7. We find that the discrepancy between the DNA abundance distributions predicted by this model and by the steady-state model is very small compared to the oscillations we observe. This observation supports that a potential lack of steady-state in the LB medium is not a likely cause for the oscillations.

## Discussion

In this paper, we infer the dynamics of replisomes from the DNA abundance distribution in a growing bacterial population. Our theory can be seen as a generalization of the classic Cooper-Helmstetter theory (Cooper and Helmstetter, 1968; Bremer and Churchward, 1977), that permits to estimate the duration of the replication period from the abundance of certain genomic locations in a growing population, see e.g. (Zheng et al., 2016; Si et al., 2017). While the Cooper-Helmstetter theory assumes constant replisome speed, our approach allows for varying speeds. We test our method by measuring the DNA abundance distribution of E. coli populations growing at different temperatures. We thereby accurately estimate the average speed of replisomes in vivo, and their speed variations along the genome.

We find that the dependence of the average replisome speed on the temperature is well described by an Arrhenius law, similar to that governing the population growth rate. This quantitative dependence can be used to deduce other laws governing bacterial physiology at varying temperature. For example, we argue that precise DNA-protein homeostasis requires the cell size to mildly vary with temperature. This prediction is in qualitative agreement with previous observations (Shehata and Marr, 1975; Trueba et al., 1982) and calls for more systematic measurements of cell parameters at varying temperature, similar to what has been done in the case of varying nutrient composition (Si et al., 2017).

Our approach reveals a wave-like oscillation of the replisome speed along the E. coli genome. The relative amplitude of these oscillations ranges from 10% to 20% of the average replisome speed. A quantitatively similar pattern was observed in the bacterial mutation rate along the DNA of an E. coli mutant strain (Niccum et al., 2019) and of other bacterial species (Dillon et al., 2018). This similarity suggests that the two phenomena have a common dynamical origin. In particular, we hypothesize that this correlation could be a manifestation of the trade-off between accuracy and speed that characterizes DNA polymerases (Sartori and Pigolotti, 2013; Banerjee et al., 2017; Fitzsimmons et al., 2018). Because of this trade-off, any mechanism increasing the speed of a polymerase is expected to increase its error rate as well.

Our analysis of the frequency of these oscillations supports that this pattern may originate from a process synchronized with the cell cycle (Dillon et al., 2018), whose activity alters the replisome function. An alternative hypothesis is that the oscillations originate from competition among replisomes for shared resources, such as nucleotides. According to this idea, the firing of new forks can hinder the progression of existing replisomes. The frequency of oscillations is compatible with both explanations. The following additional evidence supports the latter hypothesis. We did not observe appreciable oscillations for our lowest temperature of 17°C, which according to our estimates falls outside the multi-fork replication regime. Further, we found that oscillations disappeared when analyzing previous data from a culture grown in a minimal medium (Midgley-Smith et al., 2018), where multi-fork replication is also not expected. Similarly, oscillations in the mutation rate are also less evident at lower temperature and disappear in minimal medium (Niccum et al., 2019). On one hand, these facts point to competition between multiple replisomes in the same cell as a likely source for the oscillations. On the other hand, given the difficulty of obtaining steady exponential growth in LB medium, further experiments will be important to assess an eventual effect of the growth medium on the DNA abundance shape.

Beside these regular and repeatable variations, our analysis shows that random fluctuations of replisome speed are quite small, leading to an uncertainty of about $100−200kbp$ on the location of the replisome meeting point. In bacteria, the terminal region of replication is flanked by two groups of termination (Ter) sites having opposite orientations. Ter sites are the binding sites for the Tus protein and permit passage of replication forks in one direction only (Elshenawy et al., 2015), so that the two groups effectively trap the two forks in the terminal region (Duggin et al., 2008). Out of the ten Ter sequences in E. coli, only two of them (TerB and TerC) are within $100−200kbp$ of the point diametrically opposite to the origin. These two sequences have the same orientation. Our result therefore implies that most Ter sequences are usually not needed to localize the replisome meeting point. This prediction is consistent with previous observations that the phenotypes of Tus- E. coli mutants (Roecklein et al., 1991) or mutants lacking Ter sequences (Duggin et al., 2008) do not appear distinct from that of the wild type.

Quantitative modeling of the DNA abundance distribution has the potential to shed light on aspects of replisome dynamics beyond those explored in this paper. For example, it was observed that the knockout of proteins involved in the completion of DNA replication leads to either over-expression or under-expression of DNA in the terminal region (Wendel et al., 2014; Wendel et al., 2018; Sinha et al., 2018). Incorporating the role of these proteins into our model will permit to validate possible explanations for these patterns. More in general, our approach is simple and general enough to be readily applied to other bacterial species, to unravel common principles and differences in their DNA replication dynamics.

## Methods

### Cultivation and DNA extraction

E. coli MG1655 was cultured in LB medium supplemented with 50 mM MOPS pH 7.2 and 0.2% glucose. Overnight cultures grown at 37 °C were diluted into fresh medium and grown until reaching an OD600 of about 1.0 at the target temperature. These cultures were used to inoculate 50 ml medium at the desired temperature in 500 ml Erlenmeyer flasks with baffles at a target OD of 0.01. Cultivation was performed with shaking at 250 rpm. OD was determined with a NanoDrop One in cuvette mode.

The growth curves of E. coli were highly repeatable (over three replicate experiments for each temperature), see Figure 5a and Figure 5b. We computed the growth rate at each temperature by fitting a logistic function to individual growth curves, see Figure 5c. When the time was rescaled by the average growth rate, OD of different temperatures collapsed along a single curve. The cultures (1.4 ml) were harvested by centrifugation at 21,000 g for 20 s after reaching an OD of around 0.5 (mid-exponential phase, dashed lines in Figure 5a). Cells were kept growing for at least 45 doubling times (as measured in exponential phase) to reach stationary phase. Samples of 0.2 ml from the stationary phase cultures grown at 17°C, 27°C, and 37°C were harvested for DNA extraction. The pellets were immediately frozen at –80 °C until DNA extraction. DNA was extracted in parallel using Genomic DNA Purification Kit from Thermo Fisher Scientific.

![Figure 5.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig5-v2.jpg)

**Figure 5.:** (a) Optical density (OD) as a function of time at different temperatures. Each curve is averaged over three different replicates at the same temperature. Error bars represent standard deviations. Dashed lines mark the OD window in which the cells are harvested. Solid lines represents the exponential growth curve for each temperature. We computed the growth rate ki for each sample $i=1,2,3$ at a given temperature by fitting the optical density to a logistic function $a_{i}/[1+b_{i}⁢exp⁡(-k_{i}⁢t)]$, where ai and bi are sample-specific constants (Zwietering et al., 1990). The growth rate $k$ for each temperature is the average of the kis. (b) Same data as in (a), but the time in the x-axis is scaled by the growth rate $k$ at each temperature. As a result of this rescaling, the growth curves collapse on each other. (c) Average growth rate as a function of temperature. The solid purple line is an Arrhenius fit to the data (see Figure 2), resulting in $B=(6.0\pm24.9)\times10^{12}⁢hr^{-1}$ and $Δ_{C}=(74\pm10)⁢kJmol^{-1}$. We exclude the data point for $T=17⁢Co$ from the fit.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Growth curves (symbols) for individual samples at each temperature are fitted (solid line) to logistic function, $a_{i}/[1+b_{i}⁢exp⁡(-k_{i}⁢t)]$, where $i=1,2,3$. The fitted parameters are reported in each plot separately. The sample collection time is almost 50 hr for $T=17⁢Co$ and about 5 hr for $T=37⁢Co$.

### Sequencing

We sequenced three samples in the exponential phase from different experimental realizations for each temperature. In addition, we sequenced three stationary samples at three different temperatures. DNA samples were sheared by ultrasound using Covaris AFA technology. Libraries were prepared using the Illumina DNA PCR-Free Library Prep Kit. Sequencing was performed on a Novaseq6000 using paired-end 150 bp reads.

### Alignment and bias elimination

We aligned reads from each sample using Bowtie2 2.3.4.1 (Langmead and Salzberg, 2012), using the MG1655 genome as a reference. We calculated the frequency of reads as a function of the genome coordinate with bin size 10kbp. To attenuate bias, we divided the frequency at each genome coordinate in a sample from the exponential phase by the frequency of the corresponding bin in a stationary sample (Wendel et al., 2014; Midgley-Smith et al., 2018). We alternatively used all of our three stationary samples to correct the bias of each sample in the exponential phase. Therefore, after bias elimination, we effectively have $3\times3=9$ different DNA abundance curves in the exponential phase at each temperature. See Figure 2—figure supplement 1, Figure 2—figure supplement 2 and Figure 2—figure supplement 3 for details.

### Stationary distribution of replisome positions

In this section, we discuss how to compute the stationary distribution of incomplete replisome positions $p^{st}⁢(x_{1},x_{2};t)$. We call $n_{S}⁢(x_{1},x_{2};t)$ the number density of incomplete genomes at time $t$ with replisome positions at x1 and x2. By definition $\int_{0}^{L}dx_{1}\int_{0}^{L−x_{1}}dx_{2}n_{S}(x_{1},x_{2};t)=N_{S}(t)$. It follows from Equation 7 that this number density evolves according to

$$
\frac{\partial}{\partial⁡t}⁢n_{S}⁢(x_{1},x_{2};t)=-\nabla→⋅[v→⁢n_{S}]+D⁢\nabla^{2}⁡n_{s},
$$

where $\nabla→=(\partial/\partial_{x_{1}},\partial/\partial_{x_{2}})$ and $v→=(v⁢(x_{1}),v⁢(x_{2}))$. We now introduce the normalized probability $p⁢(x_{1},x_{2};t)=n_{S}⁢(x_{1},x_{2};t)/N_{S}⁢(t)$. By substituting this definition into Equation 14, we obtain

$$
\frac{\partial}{\partial⁡t}⁢p⁢(x_{1},x_{2};t)=-\nabla→⋅[v→⁢p]+D⁢\nabla^{2}⁡p-k⁢p.
$$

The stationary distribution $p^{st}⁢(x_{1},x_{2})$ is a time-independent solution of Equation 15, see Equation 8.

Because of replication completion, the line $x_{1}+x_{2}=L$ is an absorbing state for the dynamics described by Equation 15. Equation 15 must be consistent with Equation 2, which describes the dynamics of incomplete genomes regardless of the coordinates of their replisomes. This implies that the rate β at which replication completes (see Equation 2) must equal to the probability flux through the absorbing boundary:

$$
\beta=\int_{x_{1}+x_{2}=L}J→⋅n^ dl,
$$

where we introduce the probability current $J→⁢(x_{1},x_{2})=v→⁢p-D⁢\nabla→⁢p$, the unit vector $n^=(1/\sqrt{2},1/\sqrt{2})$, and the infinitesimal line increment $d⁢l$ along the absorbing boundary. Similarly, the probability flux entering the system at $(x_{1},x_{2})=(0,0)$ must match the rate of replication initiation as given by Equation 2.

Given a hypothesis on the speed function $v⁢(x)$ and the diffusion coefficient $D$, we solve Equation 15 at stationarity using the experimentally measured growth rate $k$. From the stationary solution $p^{st}⁢(x_{1},x_{2})$, we obtain β using Equation 16. Our approach does not permit to determine the cell division rate α appearing in Equation 1-Equation 3. However, this rate is not necessary to compute the DNA abundance distribution, which is expressed by Equation 9 and Equation 10 in terms of $p^{st}⁢(x_{1},x_{2})$ and β only.

### Average genome length

To compute the average genome length, we first note that the integral of $P(y)$ is equal to the average genome length $ℓ$ in the population

$$
ℓ=\int_{−L/2}^{L/2}P(y)dy.
$$

Combining Equation 17, Equation 10, and the fact that $P(0)=1$, we obtain a simple relation between the DNA abundance distribution and the average genome length:

$$
ℓ=A(0)^{−1}.
$$

### Average number of replisomes per complete genome

We estimate the average number of replisomes per complete genome $N$ in two alternative ways. On the one hand, using Equation 4-Equation 6 we find that

$$
N=\frac{2N_{S}}{N_{P}+N_{T}}=\frac{2k}{\beta}.
$$

On the other hand, it can be seen in Figure 2d that the fraction of complete genome in the population is equal to the ratio $A(L/2)/A(0)$ between the DNA abundance at the terminal and at the origin. It follows that

$$
N=\frac{2[A(0)−A(L/2)]}{A(L/2)}.
$$

### Constant speed

We focus on the scenario with constant speed and $D=0$. In this case, the steady solution of Equation 15 is given by

$$
p^{st}(x_{1},x_{2})=\frac{ke^{−\frac{k}{2v¯}(x_{1}+x_{2})}}{v¯(1−e^{−kL/(2v¯)})}\delta(x_{1}−x_{2}).
$$

The rate at which replication completes is equal to

$$
\beta=\frac{k⁢e^{-k⁢L/(2⁢v¯)}}{1-e^{-k⁢L/(2⁢v¯)}}.
$$

Substituting Equation 21 and Equation 22 into Equation 9, we obtain.

$$
P(y)=e^{−k|y|/v¯},
$$

from which Equation 11 follows by normalizing, see Equation 10.

We exactly solved Equation 15 also in the case where the speed depends on the genome coordinate, provided that the diffusion coefficient vanishes, see Appendix 6.

### Stochastic simulations

In the case of oscillating speed and $D>0$, we compute the stationary solution of Equation 15 using numerical simulations. To this aim, we interpret Equation 15 as describing a stochastic process subject to stochastic resetting (Evans and Majumdar, 2011). Specifically, we perform stochastic simulations of Equation 7. In addition to the dynamics described by Equation 7, with a stochastic rate equal to the fork firing rate $k$, trajectories are reset to the origin, $x_{1}=x_{2}=0$ (blue trajectory in Figure 6a). Since the boundary $x_{1}+x_{2}=L$ is an absorbing state, trajectories that reach this boundary are also reset to the origin (green trajectory in Figure 6a). The probability distribution associated with this dynamics evolves according to Equation 15. We simulate this stochastic dynamics to estimate the stationary distribution $p^{st}⁢(x_{1},x_{2})$ in a computationally efficient way, see Figure 6b. We estimate from the same simulations the parameter β as the empirical rate at which the absorbing boundary is reached, see Equation 16.

![Figure 6.](https://cdn.elifesciences.org/articles/75884/elife-75884-fig6-v2.jpg)

**Figure 6.:** Replisome dynamics in the $(x_{1},x_{2})$ plane.(a) Two different trajectories demonstrate two different types of resetting events in our simulations. Trajectories are reset to $x_{1}=0,x_{2}=0$ when the two replisomes complete replication (green trajectory) at the absorbing boundary (solid red line). Additionally, trajectories can be reset from any position to the origin at a rate $k$ (sky blue) to take care of the dilution term in Equation 15. (b) Replisome position distribution $p^{st}⁢(x_{1},x_{2})$ in the steady state. In both panels, parameters are $v¯=973⁢b⁢p⁢s^{-1}$, $\delta=0.19$, $\omega=4⁢r⁢a⁢d⁢Mbp^{-1}$, $ϕ=3.1⁢rad$ and $D=55⁢k⁢b⁢p^{2}⁢s^{-1}$. These parameters are on the order of those fitted from experiments (see Table 1), except for $D$ which is chosen to be larger for illustration purposes.
