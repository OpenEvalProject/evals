# Cell-to-cell infection by HIV contributes over half of virus infection

## Authors

- Shingo Iwami<sup>1</sup> †
- Junko S Takeuchi<sup>4</sup>
- Shinji Nakaoka<sup>5</sup>
- Fabrizio Mammano<sup>6</sup> ([ORCID: 0000-0002-9193-7696](https://orcid.org/0000-0002-9193-7696))
- François Clavel<sup>6</sup>
- Hisashi Inaba<sup>8</sup>
- Tomoko Kobayashi<sup>9</sup>
- Naoko Misawa<sup>4</sup>
- Kazuyuki Aihara<sup>10</sup>
- Yoshio Koyanagi<sup>4</sup>
- Kei Sato<sup>3</sup> †

### Affiliations

1. Mathematical Biology Laboratory, Department of Biology, Faculty of Sciences Kyushu University Fukuoka Japan
2. PRESTO Japan Science and Technology Agency Saitama Japan
3. CREST Japan Science and Technology Agency Saitama Japan
4. Laboratory of Viral Pathogenesis, Institute for Virus Research Kyoto University Kyoto Japan
5. Graduate School of Medicine University of Tokyo Tokyo Japan
6. INSERM-Genetics and Ecology of viruses Hospital Saint Louis Paris France
7. Université Paris Diderot, Sorbonne Paris Cité Paris France
8. Graduate School of Mathematical Sciences University of Tokyo Tokyo Japan
9. Laboratory for Animal Health, Department of Animal Science, Faculty of Agriculture Tokyo University of Agriculture Kanagawa Japan
10. Institute of Industrial Science University of Tokyo Tokyo Japan
11. Graduate School of Information Science and Technology University of Tokyo Tokyo Japan

† Corresponding author

## Abstract

Cell-to-cell viral infection, in which viruses spread through contact of infected cell with surrounding uninfected cells, has been considered as a critical mode of virus infection. However, since it is technically difficult to experimentally discriminate the two modes of viral infection, namely cell-free infection and cell-to-cell infection, the quantitative information that underlies cell-to-cell infection has yet to be elucidated, and its impact on virus spread remains unclear. To address this fundamental question in virology, we quantitatively analyzed the dynamics of cell-to-cell and cell-free human immunodeficiency virus type 1 (HIV-1) infections through experimental-mathematical investigation. Our analyses demonstrated that the cell-to-cell infection mode accounts for approximately 60% of viral infection, and this infection mode shortens the generation time of viruses by 0.9 times and increases the viral fitness by 3.9 times. Our results suggest that even a complete block of the cell-free infection would provide only a limited impact on HIV-1 spread.

## Introduction

In in vitro cell cultures and in infected individuals, viruses may display two types of replication strategies: cell-free infection and cell-to-cell infection (Sattentau, 2008; Martin and Sattentau, 2009; Talbert-Slagle et al., 2014). Both transmission means require the assembly of infectious virus particles (Monel et al., 2012), which are released in the extracellular medium for cell-free transmission, or concentrated in the confined space of cell-to-cell contacts between an infected cell and bystander target cells in the case of cell-to-cell transmission. It has been shown that most enveloped virus species, including human immunodeficiency virus type 1 (HIV-1), a causative agent of AIDS, spread via cell-to-cell infection, and it is considered that the replication efficacy of cell-to-cell infection is much higher than that of cell-free infection (Sattentau, 2008; Martin and Sattentau, 2009; Talbert-Slagle et al., 2014). However, it is technically impossible to let viruses execute only cell-to-cell infection. In addition, since these two infection processes occur in a synergistic (i.e., nonlinear) manner, the additive (i.e., linear) idea that ‘total infection’ minus ‘cell-free infection’ is equal to ‘cell-to-cell infection’ does not hold true universally. Hence, it was difficult to estimate and compare the efficacies of cell-free and cell-to-cell infection, and different reports provided different estimates (Dimitrov et al., 1993; Carr et al., 1999; Chen et al., 2007; Sourisseau et al., 2007; Zhong et al., 2013). Thus, the quantitative information that underlies cell-to-cell infection has yet to be elucidated and its impact on virus spread remains unclear.

In this study, through coupled experimental and mathematical investigation, we demonstrate that the efficacy of cell-to-cell HIV-1 infection is 1.4-fold higher than that of cell-free infection (i.e., cell-to-cell infection accounts for approximately 60% of total infection). We also show that the cell-to-cell infection shortens the generation time of viruses by 0.9 times, and increases the viral fitness by 3.9 times. These findings strongly suggest that the cell-to-cell infection plays a critical role in efficient and rapid spread of viral infection. Furthermore, we discuss the role of the cell-to-cell infection in HIV-1 infected individuals, based on in silico simulation with our estimated parameters.

## Results

### Adaptation of a mathematical model to explicitly consider cell-free and cell-to-cell infection

A static cell culture system (i.e., a conventional cell culture system) allows viruses to perform both cell-free and cell-to-cell infection. On the other hand, Sourisseau et al. have reported that the cell-to-cell infection can be prevented by mildly shaking the cell culture infected with viruses (Sourisseau et al., 2007). Consistent with the previous report (Sourisseau et al., 2007), we verified that shaking did not induce nonspecific consequences on HIV-1 infection (Figure 2—figure supplement 1). To quantitatively estimate the efficacy of the cell-free infection and that of the cell-to-cell infection respectively, we adopted this experimental method (see ‘Materials and methods’). Static cultures of Jurkat cells, an HIV-1-susceptible human CD4+ T-cell line, allow HIV-1 to propagate both by the cell-free and cell-to-cell infection, while under shaking conditions, Jurkat cells allows HIV-1 to replicate only by the cell-free infection (Figure 1A).

![Figure 1.](https://cdn.elifesciences.org/articles/08150/elife-08150-fig1-v1.jpg)

**Figure 1.:** (A) Static and shaking cultures of Jurkat cells. The static and shaking cell cultures allow human immunodeficiency virus type 1 (HIV-1) to perform both cell-free and cell-to-cell infection, and only cell-free infection, respectively. (B) The basic reproduction number, R0, is defined as the number of the secondly infected cells produced from a typical infected cell during its infectious period. In the presence of the cell-to-cell and cell-free infection, the basic reproduction number consists of two sub-reproduction numbers through the cell-free infection, Rcf, and through the cell-to-cell infection, Rcc, respectively.

Previous mathematical models, which have been widely used for data analyses, essentially describe only the cell-free infection (Nowak and May, 2000; Perelson, 2002; Iwami et al., 2012a, 2012b) or implicitly both infection modes (Komarova and Wodarz, 2013; Komarova et al., 2013a, 2013b). Here we used the following revised model including both infection modes explicitly:

$$
\frac{dT(t)}{dt}=gT(t)(1−\frac{T(t)+I(t)}{T_{max}})−\betaT(t)V(t)−\omegaT(t)I(t),
$$



$$
\frac{dI(t)}{dt}=\betaT(t)V(t)+\omegaT(t)I(t)−\deltaI(t),
$$



$$
\frac{dV(t)}{dt}=pI(t)−cV(t),
$$

where T(t) and I(t) are the numbers of uninfected and infected cells per ml of a culture, respectively, and V(t) is the viral load measured by the amount of HIV-1 p24 per ml of culture supernatant. The target cells (we used Jurkat cells) grow at a rate g with the carrying capacity of Tmax (the maximum number of cells in the cell culture flask). The parameters β, δ, p and c represent the cell-free infection rate, the death rate of infected cells, the virus production rate, and the clearance rate of virions, respectively. Note that c, g, and δ include the removal of virus, and of the uninfected and infected cells, due to the experimental samplings. In our earlier works (Iwami et al., 2012a, 2012b; Fukuhara et al., 2013; Kakizoe et al., 2015), we have shown that the approximating punctual removal as a continuous exponential decay has minimal impact on the model parameters and provides an appropriate fit to the experimental data. In addition, we introduce the parameter ω, describing the infection rate via cell-to-cell contacts (Sourisseau et al., 2007; Sattentau, 2008; Sigal et al., 2011). In the shaking cell culture system, we fixed ω = 0 because the shaking inhibits the formation of cell-to-cell contacts completely (Sourisseau et al., 2007). In previous reports, Komarova et al. used a quasi-equilibrium approximation for the number of free virus, and incorporated the dynamics of V(t) into that of I(t) in Komarova and Wodarz (2013), Komarova et al. (2013a), and Komarova et al. (2013b). However, in cell culture system, the clearance of virions usually is not much larger than the death rate of infected cells, like in vivo (see below). This fact does not validate the quasi-equilibrium approximation, and it may affect the quantification of the dynamics of the cell-to-cell and cell-free infection. We introduced the above full model, relying on a carefully designed experiment, to accurately extract the quantitative information that underlies HIV-1 infection. Furthermore, our experimental datasets include all time-series of the number of uninfected, infected cell, and virions. Thus, our coupled experimental and mathematical investigations with a sufficient datasets allowed us to estimate all parameters in Equations 1–3, and to compute the basic reproduction number, generation time, and Malthus coefficient (see below).

### Data fitting to quantify the cell-free and cell-to-cell contribution to HIV spread

Correctly estimated parameter sets with possible variation are required to reproduce model prediction for pure cell-to-cell infection in silico. However, point estimation of the model parameter set by a conventional ordinary least square method does not capture possible variations of kinetic parameters and model prediction. To assess the variability of kinetic parameters and model prediction, we perform Bayesian estimation for the whole dataset using Markov Chain Monte Carlo (MCMC) sampling (see ‘Materials and methods’ and Supplementary file 1), and simultaneously fit Equations 1–3 with ω > 0 and ω = 0 to the concentration of p24-negative and -positive Jurkat cells and the amount of p24 viral protein in the static and shaking cell cultures, respectively. Here we note that g and Tmax were separately estimated and fixed to be 0.47 ± 0.10 for the static culture and 0.54 ± 0.09 for the shaking culture per day, and (1.51 ± 0.02) × 106 and (1.22 ± 0.02) × 106 cells per flask of medium from the cell growth experiments, respectively (see ‘Materials and methods’, Figure 2—figure supplement 2 and Supplementary file 2). In addition, we used c value of 2.3 per day, which is estimated from daily harvesting of viruses (i.e., the amount of p24 have to be reduced by around 90% per day by the daily medium-replacement procedure).

The remaining four common parameters β, ω, δ and p, along with the six initial values for T(0), I(0) and V(0) in the static and the shaking cell cultures, were determined by fitting the model to the data. Experimental measurements, which were below the detection limit, were excluded in the fitting. The estimated parameters of the model and derived quantities are given in Table 1, and the estimated initial values are summarized in Supplementary file 3. The typical behavior of the model using these best-fit parameter estimates is shown together with the data in Figure 2, which reveals that Equations 1–3 describe these in vitro data very well. The shadowed regions correspond to 95% posterior predictive intervals, the dashed lines give the best-fit solution (mean) for Equations 1–3, and the dots show the experimental datasets. This suggests that the parameters that were estimated are representative for the various processes underlying the HIV-1 kinetics including the cell-to-cell and cell-free infection.

**Table 1.**
 Parameters estimated by mathematical-experimental analysis


<table>
  <thead>
    <tr>
      <th>Parameter name</th>
      <th>Symbol</th>
      <th>Unit</th>
      <th>Exp. 1</th>
      <th>Exp. 2</th>
      <th>Exp. 3</th>
      <th>Ave. ± S.D.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="7">Parameters obtained from simultaneous fit to time-course experimental dataset</td>
    </tr>
    <tr>
      <td>Rate constant for cell-free infection</td>
      <td>β</td>
      <td>10−6 × (p24 day)−1</td>
      <td>5.59* (3.54–8.41)†</td>
      <td>3.27 (2.05–5.01)</td>
      <td>‡3.70 (2.28–5.77)</td>
      <td>4.18 ± 1.41</td>
    </tr>
    <tr>
      <td>Rate constant for cell-to-cell infection</td>
      <td>ω</td>
      <td>10−6 × (cell day)−1</td>
      <td>0.88 (0.45–1.39)</td>
      <td>1.25 (0.70–1.97)</td>
      <td>1.13 (0.64–1.79)</td>
      <td>1.09 ± 0.33</td>
    </tr>
    <tr>
      <td>Production rate of total viral protein</td>
      <td>p</td>
      <td>day−1</td>
      <td>0.37 (0.22–0.59)</td>
      <td>0.59 (0.34–0.92)</td>
      <td>0.54 (0.31–0.86)</td>
      <td>0.50 ± 0.16</td>
    </tr>
    <tr>
      <td>Death rate of infected cells</td>
      <td>δ</td>
      <td>day−1</td>
      <td>0.45 (0.32–0.64)</td>
      <td>0.54 (0.38–0.75)</td>
      <td>0.50 (0.36–0.68)</td>
      <td>0.50 ± 0.10</td>
    </tr>
    <tr>
      <td colspan="7">Quantities derived from fitted values</td>
    </tr>
    <tr>
      <td>Basic reproduction number through cell-free infection</td>
      <td>Rcf</td>
      <td>–</td>
      <td>2.88 (2.34–3.53)</td>
      <td>2.27 (1.98–2.66)</td>
      <td>2.43 (2.04–2.95)</td>
      <td>2.44 ± 0.23</td>
    </tr>
    <tr>
      <td>Basic reproduction number through cell-to-cell infection</td>
      <td>Rcc</td>
      <td>–</td>
      <td>2.95 (1.48–4.70)</td>
      <td>3.65 (1.77–6.05)</td>
      <td>3.39 (1.82–5.38)</td>
      <td>3.39 ± 0.91</td>
    </tr>
    <tr>
      <td>Basic reproduction number</td>
      <td>R0</td>
      <td>–</td>
      <td>5.83 (4.20–7.75)</td>
      <td>5.92 (3.99–8.46)</td>
      <td>5.83 (4.21–7.89)</td>
      <td>5.83 ± 0.94</td>
    </tr>
    <tr>
      <td>Contribution of cell-to-cell infection</td>
      <td>RccRcf+Rcc</td>
      <td>–</td>
      <td>0.50 (0.34–0.63)</td>
      <td>0.60 (0.44–0.72)</td>
      <td>0.57 (0.43–0.70)</td>
      <td>0.57 ± 0.07</td>
    </tr>
  </tbody>
</table>

_*Mean value.†95% confidence interval.‡Average and standard deviation of merged values in experiment 1, 2, and 3._

![Figure 2.](https://cdn.elifesciences.org/articles/08150/elife-08150-fig2-v1.jpg)

**Figure 2.:** Jurkat cells were inoculated with HIV-1 (at multiplicity of infection 0.1) in the static and shaking cell cultures. Panels A and B show the time-course of experimental data for the numbers of uninfected cells (top) and infected cells (middle), and the amount of viral protein p24 (bottom) in the static and shaking cell culture systems, respectively. The shadow regions correspond to 95% posterior predictive intervals, the dashed curves give the best-fit solution (mean) for Equations 1–3 to the time-course dataset. All data in each experiment were fitted simultaneously. In panels A and B, the results of three independent experiments are respectively shown.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/08150/elife-08150-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Jurkat cells were infected with HIV-1 (at multiplicity of infection 1) as described in ‘Materials and methods’, and the infected cells were cultured in the static and the shaking condition. By harvesting the cells at 24 and 48 hr postinfection, the cells were analyzed by flow cytometry as described in ‘Materials and methods’. The percentage of the average of p24-positive cells are shown with SD. The assay was performed in triplicate, and the representative result is shown. Note that the ratio of input virus to target cells (multiplicity of infection) of this experiment is 10-fold higher than that of the experiment shown in Figure 2. This is for the clear detection of the infected cells (p24-positive cells) during early time points.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/08150/elife-08150-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Dynamics of Jurkat cell growth in the static and shaking cell cultures. By harvesting the cells for 37 days (A) in the static and (B) in the shaking cell cultures, the growth kinetics of Jurkat cells in these conditions was estimated as described in Materials and methods.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/08150/elife-08150-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** Representative results of flow cytometry (experiment 1). Time-course results of flow cytometry analyses on experiment 1 of static (left) and shaking (right) cultures are respectively shown. The cells positive for p24 antigen is gated in pink, and the number in the bottom right of the gate indicates the percentage of p24-positive cells. The data is available upon request.

Our model (i.e., Equations 1–3) applied to time-course experimental data under static and shaking conditions (i.e., Figure 2A and Figure 2B, respectively) allowed to extract the kinetic parameters in the model (see Table 1), in particular the rate constant for the cell-free infection (β) and the rate constant for the cell-to-cell infection (ω). However, from the estimated values of β and ω, we could not directly compare the efficiency of the two infection modes, because of the different units of measure of these parameters (p24/day for β, and cells/day for ω). To quantify each infection mode and overcome the above difficulty, we derived the basic reproduction number R0 (Perelson and Nelson, 1999; Nowak and May, 2000; Iwami et al., 2012b), an index reflecting the average number of newly infected cells produced from any one infected cell (see mathematical appendix in ‘Materials and methods’). Note that secondly infected cells are produced from both the cell-free and cell-to-cell infection. Interestingly, in spite of nonlinear interaction between the two modes of virus transmission, our derivation of R0 revealed that the secondly infected cells were the sum of the basic reproduction number through the cell-free infection Rcf = βpTmax/δc and the basic reproduction number through the cell-to-cell infection Rcc = ωTmax/δ, (i.e., R0 = Rcf + Rcc) (see Figure 1B). Using all accepted MCMC parameter estimates from the time-course experimental datasets, we calculated that on average the mean of the total basic reproductive number is R0 = 5.83 ± 0.94 (average ± standard deviation), and the mean number of secondly infected cells through the cell-free infection and the cell-to-cell infection are Rcf = 2.44 ± 0.23 and Rcc = 3.39 ± 0.91, respectively (see Table 1). The distributions of calculated R0, Rcf, and Rcc, are shown in Figure 3A–C, respectively. These estimates indicate that the contribution of the cell-to-cell infection is almost 60% on average (i.e., Rcc/(Rcc + Rcf) = 0.57 ± 0.07: Table 1) and this mode of infection is predominant during the HIV-1 spread in Jurkat cells. In Figure 3D, the distributions of calculated ratio are shown. Interestingly, this estimation is consistent with that by Komarova and Wodarz (2013), Komarova et al. (2013a), and Komarova et al. (2013b), although they did not take into account the difference of the death rate in the shaking and static conditions.

![Figure 3.](https://cdn.elifesciences.org/articles/08150/elife-08150-fig3-v1.jpg)

**Figure 3.:** The distribution of the basic reproduction number, R0, the number of secondary infected cells through the cell-free infection, Rcf, and the cell-to-cell infection, Rcc, calculated from all accepted Markov Chain Monte Carlo (MCMC) parameter estimates are shown in A, B, and C, respectively. The contribution of the cell-to-cell infection (i.e., Rcc/(Rcf + Rcc)) is distributed as in D. For each plot, the last 15,000 MCMC samples among the total 50,000 samples are used. a.u., arbitrary unit.

### Advantage of cell-to-cell infection

We also derived the viral generation time, defined as the time it takes for a population of virions to infect cells and reproduce (Perelson and Nelson, 1999), from Equations 1–3 in the static and shaking cell cultures (see mathematical appendix in ‘Materials and methods’). In the presence and absence of the cell-to-cell infection (i.e., for the static and shaking cell cultures, respectively), the mean generation time is calculated as 1/δ + Rcf/cR0 = 2.22 ± 0.32 days and 1/δ + 1/c = 2.47 ± 0.32 days, respectively (see Table 2). Thus, cell-to-cell infection shortens the generation time by on average 0.90 times, and enables HIV-1 to efficiently infect target cells (Sato et al., 1992; Carr et al., 1999). Furthermore, we calculated the Malthus coefficient, defined as the fitness of virus (Nowak and May, 2000; Nowak, 2006) (or the speed of virus infection) (see mathematical appendix in ‘Materials and methods’). In the presence and absence of the cell-to-cell infection, the Malthus coefficient is calculated as 1.86 ± 0.37 and 0.49 ± 0.05 per day, respectively (see Table 2). Thus, cell-to-cell infection increases the HIV-1 fitness by 3.80-fold (corresponding to 944-fold higher viral load 5 days after the infection) and plays an important role in the rapid spread of HIV-1. Thus, the efficient viral spread via the cell-to-cell infection is relevant, especially at the beginning of virus infection.

**Table 2.**
 Generation time and Malthus coefficient of virus infection


<table>
  <thead>
    <tr>
      <th>Cell culture system</th>
      <th>Exp. 1</th>
      <th>Exp. 2</th>
      <th>Exp. 3</th>
      <th>Ave. ± S.D.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5">Generation time of HIV-1</td>
    </tr>
    <tr>
      <td rowspan="2">Static cell culture</td>
      <td>2.51* days</td>
      <td>2.08 days</td>
      <td>2.22 days</td>
      <td>(2.22 ± 0.32)‡ days</td>
    </tr>
    <tr>
      <td>(1.78–3.38) days</td>
      <td>(1.54–2.78) days</td>
      <td>(1.69–2.93) days</td>
      <td>–</td>
    </tr>
    <tr>
      <td rowspan="2">Shaking cell culture</td>
      <td>2.73† days</td>
      <td>2.34 days</td>
      <td>2.47 days</td>
      <td>(2.47 ± 0.32) days</td>
    </tr>
    <tr>
      <td>(1.99–3.59) days</td>
      <td>(1.77–3.06) days</td>
      <td>(1.91–3.18) days</td>
      <td>–</td>
    </tr>
    <tr>
      <td colspan="5">Malthus coefficient of HIV-1</td>
    </tr>
    <tr>
      <td rowspan="2">Static cell culture</td>
      <td>1.61 day−1</td>
      <td>2.03 day−1</td>
      <td>1.86 day−1</td>
      <td>(1.86 ± 0.37) day−1</td>
    </tr>
    <tr>
      <td>(1.10–2.27) day−1</td>
      <td>(1.32–3.01) day−1</td>
      <td>(1.26–2.72) day−1</td>
      <td>–</td>
    </tr>
    <tr>
      <td rowspan="2">Shaking cell culture</td>
      <td>0.57 day−1</td>
      <td>0.46 day−11</td>
      <td>0.49 day−1</td>
      <td>(0.49 ± 0.05) day−1</td>
    </tr>
    <tr>
      <td>(0.47–0.67) day−1</td>
      <td>(0.38–0.56) day−1</td>
      <td>(0.39–0.61) day−1</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

_*Mean value.†95% confidence interval.‡Average and standard deviation of merged values in experiment 1, 2, and 3.HIV-1, human immunodeficiency virus type 1._

### Virtual experiments of cell-to-cell infection in silico

While the shaking culture prevents the cell-to-cell infection, it is technically difficult to completely block the cell-free infection. Here, using our estimated kinetic parameters (Table 1 and Supplementary file 3), we carried out a ‘virtual experiment’ eliminating the contribution of the cell-free infection using all accepted MCMC estimated parameter values, allowing to estimate only the cell-to-cell infection, in silico (see Figure 4). Our simulated mean values (represented by solid lines) of the cell-to-cell infection of HIV-1 are consistently located between the time course of experimental data under the static conditions (closed circles, including both the cell-free and cell to cell infections) and those under the shaking conditions (open circles, reflecting only the cell-free infection). The shadowed regions correspond to 95% posterior predictive intervals. In terms of the dynamics of infected cells and virus production, the simulated values corresponding to cell-to-cell virus propagation, are closer to experimental data from the coupled cell-free and cell-to-cell infection, than to data from the cell-free infection only. This shows that the cell-free infection, which contributes approximately 40% to the whole HIV-1 infection process, plays a limited role on the virus spread. In other words, even if we could completely block the cell-free infection, the cell-to-cell infection would still effectively spread viruses (Sigal et al., 2011). We address this point in ‘Discussion’.

![Figure 4.](https://cdn.elifesciences.org/articles/08150/elife-08150-fig4-v1.jpg)

**Figure 4.:** Using our estimated parameters, the pure cell-to-cell infection is simulated in silico (solid curves). The simulated values are located between the time course of experimental data under the static conditions (closed circles) and those under the shaking conditions (open circles). The shadowed regions correspond to 95% posterior predictive intervals.

## Discussion

Through experimental-mathematical investigation, here we quantitatively elucidated the dynamics of the cell-to-cell and cell-free HIV-1 infection modes (Figure 2 and Table 1). We derived the basic reproduction number, R0, and divided it into the numbers of secondly infected cells through the cell-free infection, Rcf, and the cell-to-cell infection, Rcc, respectively (Figure 1B and mathematical appendix in ‘Materials and methods’). Based on our calculated values of these three indexes, we found that about 60% of the viral infection is attributed to the cell-to-cell infection in the in vitro cell culture system (Table 1), which is consistent with previous estimation by Komarova and Wodarz (2013), Komarova et al. (2013a), and Komarova et al. (2013b). In addition, we revealed that the cell-to-cell infection effectively promotes the virus infection by reducing the generation time (×0.9 times), and by increasing the Malthus coefficient (×3.80 times) (Table 2).

When we consider the significance of the cell-to-cell infection in patients infected with HIV-1, it should be noted that the environment of immune cells including CD4+ T-cells in vivo is radically different from the conditions of in vitro cell cultures. For instance, lymphocytes are closely packed in lymphoid tissues such as lymph nodes, and thereby, the frequency for the infected cell to contact with adjacent uninfected cells in vivo would be much higher than that in in vitro cell cultures. In addition, Murooka et al. have directly demonstrated that HIV-1-infected cells converge to lymph nodes and can be vehicles for viral dissemination in vivo (Murooka et al., 2012). Moreover, certain studies have suggested that cell-to-cell viral spread is resistant to anti-viral immunity such as neutralizing antibodies and cytotoxic T lymphocytes (Martin and Sattentau, 2009). Therefore, these notions strongly suggest that the contribution of the cell-to-cell infection for viral propagation in vivo may be much higher than that estimated from the in vitro cell culture system.

As another significance of cell-to-cell viral spread, Sigal et al. have suggested that the cell-to-cell infection permits viral replication even under the anti-retroviral therapy (Sigal et al., 2011). This is attributed to the fact that the multiplicity of infection per cell is tremendously higher than that reached by an infectious viral particle. However, in the previous report (Sigal et al., 2011), the contribution of the cell-to-cell infection remained unclear. To further understand the role of the cell-to-cell infection, we quantified the contributions of the cell-to-cell and cell-free infection modes (Table 1). Interestingly, we found that the cell-to-cell infection mode is predominant during the infection. Furthermore, our virtual experiments showed that a complete block of the cell-free infection, which is highly susceptible to current antiviral drugs, provides only a limited impact on the whole HIV-1 infection (Figure 3). Taken together, our findings further support that the cell-to-cell infection can be a barrier to prevent the cure of HIV-1 infection, which is discussed in Sigal et al. (2011). However, it should be noted that some papers have shown that cell-to-cell spread cannot overcome the action of most anti-HIV-1 drugs (Titanji et al., 2013; Agosto et al., 2014). To fully elucidate this issue, further investigations will be needed.

In addition to HIV-1, other viruses such as herpes simplex virus, measles virus, and human hepatitis C virus drive their dissemination via cell-to-cell infection (Sattentau, 2008; Talbert-Slagle et al., 2014). Although the impact of cell-to-cell viral spread is a topic of broad interest in virology, it was difficult to explore this issue by conventional virological experiments, because an infected cell is simultaneously capable of achieving cell-to-cell infection along with producing infectious viral particles. By applying mathematical modeling to the experimental data, here we estimated the sole dynamics of cell-free infection in the cell culture system. The synergistic strategy of experiments with mathematical modeling is a powerful approach to quantitatively elucidate the dynamics of virus infection in a way that is inaccessible through conventional experimental approaches.

## Materials and methods

### Cell culture and HIV-1 infection

Jurkat cell line (Watanabe et al., 2012) was cultured in the culture medium: RPMI 1640 (Sigma, St. Louis, MO) containing 2% fetal calf serum and antibiotics. The virus solution was prepared as previously described (Sato et al., 2010, 2013, 2014; Iwami et al., 2012a). Briefly, 30 μg of pNL4-3 plasmid (Adachi et al., 1986) (GenBank accession no. M19921.2) was transfected into 293T cells by the calcium-phosphate method. At 48 hr post-transfection, the culture supernatant was harvested, centrifuged, and then filtered through a 0.45-μm-pore-size filter to produce virus solution. The infectivity of virus solution was titrated as previously described (Iwami et al., 2012a). Briefly, the virus solution obtained was serially diluted and then inoculated onto phytohemagglutinin-stimulated human peripheral blood mononuclear cells in a 96-well plate in triplicate. At 14 days postinfection, the endpoint was determined by using an HIV-1 p24 antigen enzyme-linked immunosorbent assay (ELISA) kit (ZetptoMetrix, Buffalo, NY) according to the manufacture's procedure, and virus infectivity was calculated as the 50% tissue culture infectious doses (TCID50) according to the Reed-Muench method.

For HIV-1 infection, 3 × 105 of Jurkat cells were infected with HIV-1 (multiplicity of infection 0.1) at 37°C for 2 hr. The infected cells were washed three times with the culture medium, and then suspended with 3 ml of culture medium and seeded into a 25-cm2 flask (Nunc, Rochester, NY). For the static infection, the infected cell culture was kept in a 37°C/5% CO2 incubator as usual. For the shaking infection, the infected cell culture was handled as previously described (Sourisseau et al., 2007). Briefly, the cell culture was kept on a Petit rocker Model-2230 (Wakenyaku, Japan) placed in 37°C/5% CO2 incubator, and was gently shaken at 40 movements per min. The amount of virus particles in the culture supernatant and the number of infected cells were routinely measured as follows: a portion (300 μl) of the infected cell culture was routinely harvested, and the amount of released virions in the culture supernatant was quantified by using an HIV-1 p24 antigen ELISA kit (ZetptoMetrix) according to the manufacture's procedure. The cell number was counted by using a Scepter handled automated cell counter (Millipore, Germany) according to the manufacture's protocol. The percentage of infected cells was measured by flow cytometry. Flow cytometry was performed with a FACSCalibur (BD Biosciences, San Jose, CA) as previously described (Sato et al., 2010; Sato et al., 2011, 2013, 2014; Iwami et al., 2012a), and the obtained data were analyzed with CellQuest software (BD Biosciences). For flow cytometry analysis, a fluorescein isothiocyanate-labeled anti-HIV-1 p24 antibody (KC57; Beckman Coulter, Pasadena, CA) was used. The representative dot plots are shown in Figure 2—figure supplement 3. The data is available upon request. The remaining cell culture was centrifuged and then resuspended with 3 ml of fresh culture medium. It should be noted that the procedure for HIV-1 infection was performed at time t = −2 day in the figures. Because there is no viral protein production in the first day after infection, each in vitro experimental quantity was measured daily from t = 0 day (i.e., 2 days after HIV-1 inoculation). The detection threshold of each value are the followings: cell number (cell counting), 3000 cells/ml; % p24-positive cells (flow cytometry), 0.3%; and p24 antigen in culture supernatant (p24 antigen ELISA), 80 pg/ml.

### Parameter estimation

A statistical model adopted in the Bayesian inference assumes measurement error to follow normal distribution with mean zero and unknown variance (error variance). A distribution of error variance is also inferred with the Gamma distribution as its prior distribution. Posterior predictive parameter distribution as an output of MCMC computation represents parameter variability. Distributions of model parameters and initial values were inferred directly by MCMC computations. On the other hand, distributions of the basic reproduction numbers and the other quantities were calculated from the inferred parameter sets (Figure 3 for graphical representation). A set of computations for Equations 1–3 with estimated parameter sets gives a distribution of outputs (virus load and cell density) as model prediction. To investigate variation of model prediction, global sensitivity analyses were performed. The range of possible variation is drawn in Figure 2 as 95% confidence interval. Technical details of MCMC computations are summarized in Supplementary file 1.

### Quantification of Jurkat cell growth

We here estimate the growth kinetics of Jurkat cells, which have been commonly used for HIV-1 studies, under the normal (i.e., mock-infected) condition with the following mathematical model:

$$
\frac{dT(t)}{dt}=gT(t)(1−\frac{T(t)}{T_{max}}),
$$

where the variable T(t) is the number of Jurkat cells at time t and the parameters g and Tmax are the growth rate of the cells (i.e., Log2/g is the doubling time) and the carrying capacity of the cell culture flask, respectively. Nonlinear least-squares regression (FindMinimum package of Mathematica9.0) was performed to fit Equation 4 to the time-course numbers of Jurkat cells in the normal condition. The fitted parameter values are listed in Supplementary file 2 and the model behavior using these best-fit parameter estimates is presented together with the data in Figure 2—figure supplement 2.

### Mathematical appendix

The linearized equation of Equations 1–3 at the virus-free steady state, (Tmax, 0, 0), is given as follows:

$$
\frac{dI(t)}{dt}=\betaT_{max}V(t)+\omegaT_{max}I(t)−\deltaI(t),
$$



$$
\frac{dV(t)}{dt}=pI(t)−cV(t).
$$

Let b(t) be the number of newly produced infected cells in the linear phase:

$$
b(t):=\betaT_{max}V(t)+\omegaT_{max}I(t).
$$

Applying the variation of constants formula to Equations 5, 6, we have

$$
V(t)=V(0)e^{−ct}+\int0te^{−c(t−s)}pI(s)ds,
$$



$$
I(t)=I(0)e^{−\deltat}+\int0te^{−\delta(t−z)}b(z)dz.
$$

Inserting Equation 9 into Equation 8 to exchange the order of integrals, we have

$$
V(t)=g(t)+p\int0t\int0xe^{−c(x−\theta)−\delta\theta}d\thetab(t−x)dx,
$$

where

$$
g(t)∶=V(0)e^{−ct}+\int0te^{−c(t−s)}pI(0)e^{−\deltat}ds.
$$

From Equation 7 and Equations 9, 10, we arrive at the following renewal equation:

$$
b(t)=h(t)+\int0tΨ(x)b(t−x)dx,
$$

where h(t) is given by

$$
h(t)∶=\omegaT_{max}I(0)e^{−\deltat}+\betaT_{max}g(t),
$$

and the kernel Ψ(x) is given by

$$
Ψ(x)∶=\betaT_{max}p\int0xe^{−\delta\theta−c(x−\theta)}d\theta+\omegaT_{max}e^{−\deltax},
$$



$$
=\frac{\betaT_{max}p}{\deltac}(ϕ_{1}∗ϕ_{2})(x)+\frac{\omegaT_{max}}{\delta}ϕ_{1}(x).
$$

In the above expression, ϕj(x) denotes the probability density function given by

$$
ϕ_{1}(x)=\deltae^{−\deltax},   ϕ_{2}(x)=ce^{−cx},
$$

and, ∗ denotes the convolution of functions. From the general theory of the basic reproduction number (Inaba, 2012), R0 for the reproduction of infected cells is given by

$$
R_{0}=\int0∞Ψ(x)dx=\frac{\betaT_{max}p}{\deltac}+\frac{\omegaT_{max}}{\delta}=R_{cf}+R_{cc},
$$

where Rcf and Rcc denote the reproduction numbers for infected cells mediated by the cell-free and cell-to-cell infection, respectively.

Next we consider the reproduction process of viruses. Let ρ(t):= pI(t) be the number of newly produced viruses at time t. From Equations 8, 9, we obtain

$$
ρ(t)=pI(0)e^{−\deltat}+\int0te^{−\delta(t−z)}(\betaT_{max}pV(z)+\omegaT_{max}ρ(z))dz, 
$$

where

$$
V(t)=V(0)e^{−ct}+\int0te^{−c(t−s)}ρ(s)ds.
$$

Inserting Equation 11 into Equation 12, we again arrive at the following renewal equation:

$$
ρ(t)=q(t)+\int0tΨ(x)ρ(t−x)dx,
$$

where q(t) is given by

$$
q(t)∶=pI(0)e^{−\deltat}+\int0te^{−\delta(t−z)}p\betaT_{max}V(0)e^{−cz}dz.
$$

Note that the reproduction kernel Ψ(x) for the virus reproduction is the same as the kernel for the cell reproduction. Thus the probability density function of the virus reproduction is given by

$$
ψ(x)∶=\frac{Ψ(x)}{R_{0}}=\frac{R_{cf}}{R_{0}}(ϕ_{1}∗ϕ_{2})(x)+\frac{R_{cc}}{R_{0}}ϕ_{1}(x).
$$

Then the generation time for the virus reproduction, denoted by G, is calculated as follows:

$$
G∶=\int0∞tψ(t)dt=\frac{R_{cf}}{R_{0}}G_{cf}+\frac{R_{cc}}{R_{0}}G_{cc}\leqG_{cf},
$$

where Gcf : = 1/δ + 1/c and Gcc : = 1/δ are the generation times for virus reproduction mediated by the cell-free and cell-to-cell infection, respectively.

The Malthusian coefficient for the virus reproduction must be given as the dominant real root of the Euler-Lotka equation as

$$
\int0∞e^{−\lambdax}Ψ(x)dx=\frac{\betaT_{max}p}{\deltac}ϕ_{1}^(\lambda)ϕ_{2}^(\lambda)+\frac{\omegaT_{max}}{\delta}ϕ_{1}^(\lambda)=1,
$$

where $ϕ_{j}^$ denotes the Laplace transformation of a function ϕj. That is,

$$
ϕ_{1}^(\lambda)=\int0∞e^{−\lambdax}ϕ_{1}(x)ds=\frac{\delta}{\delta+\lambda}, ϕ_{2}^(\lambda)=\int0∞e^{−\lambdax}ϕ_{2}(x)ds=\frac{c}{c+\lambda}.
$$

Therefore the Euler-Lotka equation can be calculated explicitly as follows:

$$
\frac{\betaT_{max}p}{\deltac}\frac{\deltac}{(\delta+\lambda)(c+\lambda)}+\frac{\omegaT_{max}}{\delta}\frac{\delta}{\delta+\lambda}=1,
$$

which is reduced to a quadratic equation,

$$
\lambda^{2}+\deltac(G_{cc}+(1−R_{cc})(G_{cf}−G_{cc}))\lambda+\deltac(1−R_{0})=0. 
$$

If R0 > 1, Equation 13 has a unique positive root, which is no other than the Malthusian coefficient for the virus reproduction, so it is calculated as,

$$
\lambda=\frac{−\deltac(G_{cc}+(1−R_{cc})(G_{cf}−G_{cc}))+\sqrt{\delta^{2}c^{2}(G_{cc}+(1−R_{cc})(G_{cf}−G_{cc}))^{2}−4\deltac(1−R_{0})}}{2}.
$$
