# Evaluation of predictions of the stochastic model of organelle production based on exact distributions

## Authors

- C Jeremy Craven<sup>1</sup> †

### Affiliations

1. Department of Molecular Biology and Biotechnology University of Sheffield Sheffield United Kingdom

† Corresponding author

## Abstract

We present a reanalysis of the stochastic model of organelle production and show that the equilibrium distributions for the organelle numbers predicted by this model can be readily calculated in three different scenarios. These three distributions can be identified as standard distributions, and the corresponding exact formulae for their mean and variance can therefore be used in further analysis. This removes the need to rely on stochastic simulations or approximate formulae (derived using the fluctuation dissipation theorem). These calculations allow for further analysis of the predictions of the model. On the basis of this we question the extent to which the model can be used to conclude that peroxisome biogenesis is dominated by de novo production when Saccharomyces cerevisiae cells are grown on glucose medium.

## Introduction

Recently a model was presented in which the variation of numbers of a particular type of organelle (Golgi apparatus, vacuoles or peroxisomes) observed in cells was proposed as a diagnostic indicator of the relative importance of different processes by which organelles can be formed and destroyed (Mukherji and O’Shea, 2014; see Mukherji and O’Shea, 2015 for a correction). Here we re-examine the mathematical analysis of this model and show that further insight can be gained from considering exact calculations of the equilibrium distributions. For conciseness we will refer to the model, and the analysis in the associated paper (Mukherji and O’Shea, 2014), by the abbreviation SMOP (stochastic model of organelle production).

## Analysis

### The SMOP model in the context of “birth and death” models

In the SMOP model, four processes are envisaged for the production and destruction of organelles: de novo synthesis, fission, fusion and decay. These four processes are characterised by one rate constant each, defined in the SMOP paper as kde novo, kfission, kfusion, and γ. Following the definitions in the SMOP paper, the probabilities of each of the four processes occurring in the next small time period δt are given in Table 1. We also include in this table the total rate of each process that would be observed instantaneously in a large population of N cells.

**Table 1.**
 Definition of terms in the SMOP model


<table>
  <thead>
    <tr>
      <th>Process</th>
      <th>Probability of process occurring in next δt in a particular cell containing n organelles1</th>
      <th>Process changes n by</th>
      <th>Rate of process in sample of N cells2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>De novo</td>
      <td>kde novoδt</td>
      <td>1</td>
      <td>kde novofnN</td>
    </tr>
    <tr>
      <td>Fission</td>
      <td>kfissionnδt</td>
      <td>1</td>
      <td>kfissionnfnN</td>
    </tr>
    <tr>
      <td>Decay</td>
      <td>γnδt</td>
      <td>-1</td>
      <td>γnfnN</td>
    </tr>
    <tr>
      <td>Fusion</td>
      <td>kfusionn(n-1)δt</td>
      <td>-1</td>
      <td>kfusionn(n-1)fnN</td>
    </tr>
  </tbody>
</table>

_1For example, if kfission = 0.02 then the probability of a cell with n = 2 organelles undergoing a fission event in the next 0.1 time units = 0.02x2x0.1 = 0.004.2fn is the fraction of cells having n organelles. For example, if 23% of the cells have 2 organelles then f2 = 0.23. If, in a population of 1000 cells, f2 = 0.23 and kfission = 0.02 then the rate of cells changing from having n = 2 to n = 3 organelles at any one moment due to fission would be 0.02x2x0.23x1000 = 9.2 cells per time unit._

Models involving processes of this type are generically termed “birth and death” processes and have a very long history of analysis in the context both of the life sciences (e.g. evolution; Yule, 1924) and in the context of physical processes (e.g. detection of cosmic rays; Furry, 1937). Accessible discussions can be found in several books (Bailey, 1990, which is a reissue of the classic text from 1964; Taylor and Karlin, 1998). In such analyses, the three processes of de novo production, production by fission, and loss by first order decay are often termed immigration, birth and death, respectively. Immigration is used for a process that increases the number of individuals but does not require any other individuals already to be present. Birth is the process by which one individual gives rise to a second individual. Death is a process by which a particular individual is lost from a population with a probability that is independent of any other members of the population. Analyses including a fusion term are much less common.

As there are a considerable number of possible combinations of the four processes that might be active, we will use a notation here to define a model by listing in curly brackets the active production processes, followed by the active destruction processes, separated by a semi-colon. Any process that is not mentioned has a rate constant of zero. Thus the model with de novo, fission and decay terms would be denoted {de novo, fission; decay}.

During single cell simulations based upon the equations in Table 1 the number of organelles will fluctuate (Figure 1A) and one can ask what fraction of time, fn, does a cell spend having n = 0, n = 1, n = 2, etc. organelles. This is equivalent to asking what fraction of a large ensemble of cells have n = 0, n = 1, n = 2, etc. organelles at one moment in time. In treatments of stochastic systems, the values of fn would normally be described as the probability distribution for a cell having n organelles. In terms of a population of cells it can be described as a population distribution.

![Figure 1.](https://cdn.elifesciences.org/articles/10167/elife-10167-fig1-v1.jpg)

**Figure 1.:** (A) The traces show simulations run with the parameters {kde novo = 2.0, kfission = 0.9; γ = 1.0, kfusion = 0.02}, starting from n = 0 (black trace) and n = 50 (green trace). Both simulations “settle down” to stochastic fluctuations about a mean value of <n> = 7.1 (B) Schematic representation of a set of cells that are all initialised to n = 1 at time t = 0, and are observed at a time t = τ. (C) Distributions calculated with the same parameters as in (A) for a set of 1000 cells as in (B), calculated for τ = 0.2 (magenta), 0.4 (yellow), 1.0 (green), 2.0 (blue), 5.0 (black), 10.0 (cyan), 15.0 (red). The curves for τ = 10.0 and τ = 15.0 become very similar as they approach the limiting distribution. These two curves match closely the result (filled black circles) of applying the recurrence relation (Equation 2; Appendix 2). (D) The red trace is a time course for parameters {kde novo = 2.0, kfission = 1.1; γ = 1.0, kfusion = 0}. Since kfission > γ, and kfusion = 0, then n diverges; in such a case there is no limiting distribution.

The simulations in Figure 1A illustrate the important point that a simulation is always started from some arbitrary starting point, and that a period of time must elapse before the simulations can be considered to be independent of this starting point. If the distribution fn is evaluated at different times after the starting point of simulations (Figure 1C) then different distributions are obtained; hence the distribution is “time dependent”. As the probability (or population) distribution varies in time (and since the system can in principle be started from any state) then it is not strictly possible to talk of “the distribution” for a stochastic system. However in many birth and death models the system will settle down to a limiting distribution, independent of the starting states of the cell(s) as in the cyan and red curves in Figure 1C. Such a situation corresponds to a state of dynamic equilibrium that is familiar from chemical kinetics. Thus the terms limiting, equilibrium (or steady state) distributions can be used in this context interchangeably. The conditions for the models studied here to have limiting distributions is discussed further below; an example of a set of parameters for which a SMOP model does not yield a limiting distribution is shown in Figure 1D.

Assuming that a limiting probability distribution does exist there are two basic sampling methods by which it can be measured, irrespective of whether one is making experimental observations or performing simulations. One method is to note n at a set of time points for a single cell (such as points drawn from the trajectories in Figure 1A), and the other is to take a large number of cells at one point in time, and measure n across this ensemble of cells (Figure 1B,C). The former would require a time dependent set of observations that may be difficult to obtain experimentally. The latter approach is equivalent to making experimental observations on a large field of view of cells, or of making repeated simulations. However there is a large caveat that when the measurements are made one must be convinced that the cells have had “long enough to reach equilibrium” since the last significant perturbation to the system. If this is not the case then the distribution measured will be contaminated with contributions from non-equilibrium distributions (such as from the magenta, yellow, green and blue curves in Figure 1C). Perturbations include the choice of an arbitrary starting point in simulations, and effects such as cell division and change of growth conditions in experimental data.

### Does the SMOP analysis imply equilibrium distributions?

It is implicitly assumed in the SMOP paper that the populations are to be considered to be at equilibrium (or that the probability distributions are in their limiting form) for all three cases of the analysis via simulations, from experimental data, or via the fluctuation dissipation theorem; a comment has been added to the original articles to clarify this assumption for the simulations (see the comment dated November 23, 2015 on Mukherji and O'Shea, 2014). For the experimental data this seems a reasonable assumption, although dynamic population data are really required to fully settle this issue. The fluctuation dissipation theorem method implicitly assumes a steady state (Paulsson, 2005).

### Derivation of recurrence relation for the distribution of organelles in the {de novo, fission; decay, fusion} model

By applying an equilibrium condition it is straightforward to derive precise relations for the distributions in the three scenarios considered in the original SMOP paper, and hence avoid the approximations introduced by the use of the fluctuation dissipation theorem.

At equilibrium, the rate at which the population gains cells with n + 1 organelles due to cells with n organelles gaining one organelle must equal the rate at which the cells with n + 1 organelles lose one organelle. The reasoning is the same as for standard treatments of dynamic equilibrium between two states (as in a chemical reaction), and the complete justification of this when there are multiple states (i.e. cells with n = 0, n = 1, n = 2, etc., organelles) is given in Appendix 1.

Thus at equilibrium

$$
(k_{de novo}+ k_{fission}n)f_{n}N = (\gamma+ k_{fusion}n)(n + 1)f_{n+1}N
$$

which gives

$$
f_{n+1} = \frac{(k_{de novo}+ k_{fission}n)}{(\gamma+ k_{fusion}n)n+ 1}f_{n}
$$

From Equation 2 the exact distribution of organelle numbers at equilibrium can be calculated for a model involving any combination of the four processes, without recourse to random number based simulations and the attendant issues of ensuring adequate sampling precision.

An explicit numerical example of the use of Equation 2 to generate a distribution is given in Appendix 2. Briefly, an arbitrary value for f0 is chosen; f1 is then calculated from f0; f2 is calculated from f1; f3 is calculated from f2; etc. Finally the entire distribution is normalised, which removes any dependence on the initial choice for f0. Equation 2 is often termed a recurrence relation (or sometimes recursion relation or difference equation) as it allows successive terms in a distribution to be calculated from earlier terms.

### Application of recurrence method to Golgi and vacuole models

The recurrence relation readily allows the derivation of precise distributions for the case of the model applied to Golgi ({de novo; decay}, Appendix 3) and vacuoles ({fission; fusion}, Appendix 4). For the Golgi, a Poisson distribution is obtained as the limiting distribution in accord with the SMOP analysis. However for vacuoles a truncated Poisson distribution is obtained, and not the shifted Poisson distribution that is reported in the SMOP analysis. Although the difference between these distributions is quite subtle (Appendix 4), the variation of Fano factor with <n> is significantly different: the Fano factor for the truncated Poisson approaches 1 much more rapidly (Figure 2, green curve) than for the shifted Poisson (Figure 2, black curve).

![Figure 2.](https://cdn.elifesciences.org/articles/10167/elife-10167-fig2-v1.jpg)

**Figure 2.:** Three data points quoted in the SMOP paper are plotted: □ Haploid (glucose); ○ Diploid (glucose); ∆ Haploid (oleate). The solid black curve is the expectation from the shifted Poisson distribution (which is the incorrect distribution given the {fission; fusion} model) and the solid green curve is the expectation from the truncated Poisson distribution (which is the correct distribution given the model). The dashed line is for a Fano factor of 1. The solid curves were constructed by calculating a family of distributions and evaluating the mean and Fano factor.

In Figure 2, it can be seen that the experimental values quoted in the SMOP analysis are in excellent agreement with the incorrect prediction, whilst the agreement with the corrected theoretical prediction is much less good. This greatly weakens the argument that the SMOP model makes “quantitatively accurate predictions” or that it therefore correctly accounts for the behaviour of the vacuole population.

### Application of recurrence method to peroxisome models

Having established the value of analysing the SMOP model with the recurrence method, we move on to the case of peroxisomes.

#### Recurrence relation demonstrates that {de novo, fission; decay} yields a negative binomial distribution

For peroxisomes, the primary model discussed in the SMOP analysis is a model in which peroxisomes can potentially form both de novo and by fission, and fusion is considered to be negligible. We show in Appendix 5 that such a {de novo, fission; decay} model has a limiting distribution that is a negative binomial distribution.

As a result, exact expressions (for all parameter values) are readily obtained (Appendix 5) for the mean and Fano factor for this model,

$$
n = \frac{k_{de novo}}{\gamma−k_{fission}}
$$

$$
\frac{\sigma^{2}}{n} = \frac{\gamma}{\gamma−k_{fission}}
$$

Combining Equations 3,4 gives an alternative form for the Fano factor

$$
\frac{\sigma^{2}}{n} = 1+\frac{k_{fission}n}{k_{de novo}}
$$

This latter equation is the form given in the SMOP analysis as the kfusion = 0 limit of the approximate Equation 1 of the SMOP paper. By explicitly applying the equilibrium assumption we have therefore shown that this expression is exact in this case for all values of the parameters.

#### Evaluation of Fano factor for the boundary marking equal de novo and fission rates

An attractive claim made for the SMOP analysis is that the value for the Fano factor can be used to distinguish between different modes of organelle production.

In Figure 3D of the original SMOP paper, a green dashed line was placed at σ2/n=1 and stated as “marking the boundary between de novo synthesis and fission dominated organelle production”. Thus, as presented in Figure 3D of the original version of the SMOP paper, the Fano factor for cells grown on oleate (σ2/n=2.4±0.2) appears to lie significantly above the line where the rates are equal, and thus terms such as “fission dominated biogenesis” are used widely in the SMOP paper.

![Figure 3.](https://cdn.elifesciences.org/articles/10167/elife-10167-fig3-v1.jpg)

**Figure 3.:** For each value of the Fano factor shown, a bar is drawn to represent the total production rate. The filled part of the bar represents the contribution from de novo production inferred from the model and the open part of the bar represents the inferred rate from fission. Bars are shown for Fano factors of: 1.0 (100% de novo); 1.1 (experimentally observed for glucose growth (G) in SMOP paper; 9% de novo, 91% fission); 2.0 (boundary value, where de novo and fission contributions are equal); 2.4 (experimentally reported value for oleate growth (O) in SMOP paper; 42% de novo, 58% fission); 3.0 (value required for fission rate to be double the de novo rate). The total production rate from de novo processes is simply kde novo. The total rate from fission processes is kfission<n>. The relative proportions of the two processes were calculated using Equation 5.

However, according to Equation 5 the correct value with equal contributions from the two processes is $\sigma^{2}/n=2$. A correction to this effect has now been issued. The value of $\sigma^{2}/n=1$ corresponds to the extreme case of zero fission and production solely by de novo production (Figure 3). In the corrected version of Figure 3D in the SMOP paper it is clear that the inferred fission rate for growth on oleate is only barely greater than the de novo synthesis rate and the term “dominance” does not seem to be appropriate. It is clear from Figure 3 that the inferred contribution from fission grows only rather slowly as the Fano factor increases above a value of two. In other words, for fission to be truly dominant a Fano factor would have to be observed that was far greater than any reported in the SMOP paper.

#### Restrictions on the relationships between parameters in order for limiting distributions to exist

Since it is inherent in the SMOP analysis that the distributions are limiting/equilibrium distributions, it is important to consider whether a limiting distribution will ever be reached.

In the case of the peroxisome model, {de novo, fission; decay}, for the system to have a limiting or equilibrium distribution there is a strong restriction on parameters, namely that kfission < γ. To see why this restriction exists, consider first the more simple {de novo; decay} model. Considering a single cell, the number of organelles will be limited by the fact that as n grows larger then the decay process (whose rate increases proportionally to n) will become increasingly more likely than the de novo formation process (which is independent of n). If the fission process is introduced then there is now a production term that also increases proportionally to n. If kfission exceeds γ then the fission process will always exceed the decay process and the number of organelles will grow without limit.

The behaviour as kfission becomes similar to γ can also be seen from Equations 3,4 since if kfission is increased from zero until it becomes equal to γ then <n> and $\sigma^{2}/n$ both diverge. Thus at first sight there appear to be two different ways in which the Fano factor can become very large. One way, as extensively discussed in the SMOP analysis and above, is if the mean rate kfission<n> becomes large compared to the mean rate kde novo. The other way, that becomes clear from our analysis, is if the rate constant kfission becomes similar to the rate constant γ. The connection between these two relations is that <n> is a function of all three rate constants. This emphasises the hidden complexity of the interplay of the parameters in this model.

## Discussion

Our motivation for this in depth analysis of the SMOP method was sparked by the claim that it could differentiate between fission and fusion dominated mechanisms of peroxisome biogenesis. That the distribution of numbers of organelles can give a clue to the mechanisms by which organelles are formed is a very elegant idea, and the SMOP analysis combines this idea with a very simple kinetic model. As we explored the system further we realised that the fluctuation dissipation theorem result was not necessary for analysis of the system, and that enforcing the equilibrium condition, that was implicit in the work already, greatly simplified the analysis.

There are a number of factors that cause us to question the utility of the SMOP model. A main piece of evidence for the correctness of the model was the agreement of the experimentally observed Fano factors for the vacuole data with those from the model. We have shown this agreement to be much less perfect than originally demonstrated. We have also shown that there is a strong interplay between different parameters in the model. This means that the agreement of experimental data with the model is not as compelling as originally presented and that the interpretation of experimental observations back to mechanistic conclusions is open to question. We hope that our analysis will stimulate discussion as to whether, for instance, the SMOP model captures the key features of the underlying processes and is just lacking some details; or whether the model fundamentally lacks key aspects of feedback. The assumption that observations of cells grown in batch culture faithfully report equilibrium distributions also requires further verification.

A key conclusion of the SMOP analysis is that the contribution of fission to peroxisome biogenesis is negligible (<10%) when yeast cells are grown on glucose, but "dominant" when they are grown on oleate. This is an area of some contention (Hoepfner et al, 2005; Motley and Hettema, 2007), and a recent model relied on fission of peroxisomes during organelle inheritance as the proliferation mechanism (Knoblach et al, 2013). Our analysis has shown that the term “dominant” is misleading, and that the data reported for haploid cells grown on oleate indicates approximately equal contributions from the two processes.

Nevertheless the model does suggest that the proportion of production by fission increases by about a factor of five on switching to oleate growth. Supporting evidence for this was provided by the observation of the reduction in the inferred fission contribution in cells grown on oleate in which the fission factors Vps1 or Dnm1 (or Fis1, an accessory factor of Dnm1) were deleted. On the other hand, no data were shown for glucose grown cells harbouring the same deletions. On glucose the Fano factor is reported in the SMOP analysis as 1.1, with <n> = 3, and from Equations 3,4 one obtains kde novo = 2.7γ and kfission = 0.1γ. The model then implies that on deletion of the fission pathway (i.e. setting kfission = 0) then <n> would only drop by 10%. Peroxisome count data has been reported recently (Fig S4, Motley et al., 2015), with values of <n> = 4.9 in WT cells, <n> = 1.5 in vps1Δ cells and <n> = 1.2 in vps1Δdnm1Δ cells. The drops in peroxisome numbers in vps1Δ and vps1Δdnm1Δ cells are much greater than the 10% estimated above from the SMOP model. There is also peroxisome count data in Kuravi et al. (2006), which gives <n> = 1.6 (WT), <n> = 1.2 (vps1Δ), <n> = 1.7 (dnm1Δ), <n> = 0.9 (dnm1Δvps1Δ). The drop in <n> for the dnm1Δvps1Δ again conflicts with the idea that fission is such a small contributor to the biogenesis process. The discrepancies between these various data possibly arise from difficulties in quantifying peroxisome numbers, especially when cells contain a large number of small (and therefore low fluorescence) peroxisomes as may be the case when fission is a strong contributor to biogenesis. The problem of peroxisome counts depending on the brightness of fluorescent markers has been commented on by Jung et al. (2010).

There is a continuing push for cell biology to become more quantitative, and to be subject to the use of rigorous models as are common in the physical sciences. Such a push raises significant challenges not only in terms of developing tractable models and justifying the underlying assumptions, but also in terms of the application of the model to complex experimental data. In particular this work highlights the need for greater accounting for detection limits and intensity distributions, as well of time dependent issues, in the reporting and analysis of organelle count data, if these are to be used to infer details of organelle biogenesis mechanisms.

## Materials and methods

All calculations were performed in python 2.7, running either via Cygwin under Windows 8.1, or Linux Mint 17.0. The code used for running stochastic simulations and for calculating distributions via Equation 2 is given in Source code 1,2. Time units are arbitrary. The time step for the simulations in Figure 1 was 0.0001 units. Equation 2 can be reformulated in terms of three parameters, e.g. kde novo/γ, kfission/γ, kfusion/γ; thus for example the parameters {kde novo = 2.0, kfission = 0.9; γ = 1.0, kfusion = 0.02} and any uniformly scaled set of parameters (e.g. {kde novo = 4.0, kfission = 1.8; γ = 2.0, kfusion = 0.04}) yield the same limiting distribution. As in the SMOP paper, the Fano factor is defined here as $\frac{\sigma^{2}}{n}$.
