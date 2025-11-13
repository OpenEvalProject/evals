# The success of artificial selection for collective composition hinges on initial and target values

## Authors

- Juhee Lee<sup>1</sup> ([ORCID: 0000-0003-3318-6377](https://orcid.org/0000-0003-3318-6377))
- Wenying Shou<sup>3</sup> ([ORCID: 0000-0001-5693-381X](https://orcid.org/0000-0001-5693-381X)) †
- Hye Jin Park<sup>1</sup> ([ORCID: 0000-0003-3552-6275](https://orcid.org/0000-0003-3552-6275)) †

### Affiliations

1. Department of Physics, Inha University Incheon Republic of Korea ([ROR:01easw929](https://ror.org/01easw929))
2. Asia Pacific Center for Theoretical Physics Pohang Republic of Korea ([ROR:011hxwn54](https://ror.org/011hxwn54))
3. Centre for Life’s Origins and Evolution, Department of Genetics, Evolution and Environment, University College London London United Kingdom ([ROR:001mm6w73](https://ror.org/001mm6w73))

† Corresponding author

## Abstract

Microbial collectives can perform functions beyond the capability of individual members. Enhancing collective functions through artificial selection is, however, challenging. Here, we explore the ‘rafting-a-waterfall’ metaphor where achieving a target population composition depends on both target and initial compositions. Specifically, collectives comprising fast-growing (F) and slow-growing (S) individuals were grown for ‘maturation’ time, and the collective with S-frequency closest to the target value is chosen to ‘reproduce’ via inoculating offspring collectives. During collective maturation, intra-collective selection acts like a waterfall, relentlessly driving the S-frequency to lower values, while during collective reproduction, inter-collective selection resembles a rafter striving to reach the target frequency. Using simulations and analytical calculations, we show that intermediate target S frequencies are the most challenging, akin to a target within the vertical drop of a waterfall, rather than above or below it. This arises because intra-collective selection is the strongest at intermediate S-frequencies, which can overpower inter-collective selection. While achieving a low target S frequencies is consistently feasible, attaining high target S-frequencies requires an initially high S-frequency — much like a raft that can descend but not ascend a waterfall. As Newborn size increases, the region of achievable target frequency is reduced until no frequency is achievable. In contrast, the number of collectives under selection plays a less critical role. In scenarios involving more than two populations, the evolutionary trajectory must navigate entirely away from the metaphorical ‘waterfall drop.’ Our findings illustrate that the strength of intra-collective evolution is frequency-dependent, with implications in experimental planning.

## Introduction

Microbial collectives can carry out functions that arise from interactions among member species. These functions, such as waste degradation (Woo et al., 2020; Sun et al., 2022), probiotics (Bober et al., 2018), and vitamin production (Wang et al., 2016), can be useful for human health and biotechnology. To improve collective functions, one can perform artificial selection (directed evolution) on collectives (see Figure 1): Low-density ‘Newborn’ collectives are allowed to ‘mature’ during which cells proliferate and possibly mutate, and community function develops. ‘Adult’ collectives with high functions are then chosen to reproduce, each seeding multiple offspring Newborns. Artificial selection of collectives have been attempted both in experiments (Goodnight, 1990; Swenson et al., 2000b; Swenson et al., 2000a; Blouin et al., 2015; Panke-Buisse et al., 2015; Panke-Buisse et al., 2017; Jochum et al., 2019; Wright et al., 2019; Raynaud et al., 2019; Arora et al., 2020; Chang et al., 2020; Mueller et al., 2021; Jacquiod et al., 2022; Raynaud et al., 2022; Arias-Sánchez et al., 2024) and in simulations (Penn, 2003; Penn and Harvey, 2004; Williams and Lenton, 2007; Xie et al., 2019; Doulcier et al., 2020; Xie and Shou, 2021; Chang et al., 2021; Fraboul et al., 2023; Lalejini et al., 2022; Zaccaria et al., 2023; Vessman et al., 2023), often with unimpressive outcomes.

![Figure 1.](https://cdn.elifesciences.org/articles/97461/elife-97461-fig1-v1.jpg)

**Figure 1.:** Each selection cycle begins with a total of $g$ Newborn collectives, each with $N_{0}$ total cells of slow-growing S population (light gray dots) and fast-growing F population (dark gray dots). During maturation (over time $\tau$), S and F cells divide at rates $r_{S}$ and $r_{S}+\omega$ ($\omega>0$), respectively, and S mutates to F at rate $\mu$. During inter-collective selection, the Adult collective with F frequency $f$ closest to the target composition $f^$ is chosen to reproduce $g$ Newborns for the next cycle. Newborns are sampled from the chosen Adult (yellow star) with $N_{0}$ cells per Newborn. The selection cycle is then repeated until the F frequency reaches a steady state, which may or may not be the target composition. To denote a variable $x$ of $i$-th collective in cycle $k$ at time $t$ ($0\leqt\leq\tau$), we use notation $x_{k,t}^{(i)}$ where $x\in{S,F,s, f}$. Note that time $t=0$ is for Newborns and $t=\tau$ is for Adults.

One of the major challenges in selecting collectives is to ensure the inheritance of a collective function (Xie et al., 2023; Thomas et al., 2024). Inheritance from a parent collective to offspring collectives can be compromised by changes in genotype and species compositions. During maturation of a collective, genotype compositions within each species can change due to intra-collective selection favoring fast-growing individuals (Figure 1, ‘intra-collective’ selection), while species compositions can change due to ecological interactions. Furthermore, during the reproduction of a collective, genotype and species compositions of offspring can vary stochastically from those of the parent (Figure 1, ‘genetic drift’).

Here, we consider the selection of collectives comprising two or three populations with different growth rates, and our goal is to achieve a target composition in the Adult collective. This is a common quest: whenever a collective function depends on both populations, the collective function is maximized, by definition, at an intermediate frequency (e.g. too little of either population will hamper function; Xie et al., 2019). Earlier work has demonstrated that nearly any target species composition can be achieved when selecting communities of two competing species with unequal growth rates (Doulcier et al., 2020; Rainey, 2023), so long as the shared resource is depleted during collective maturation (Doulcier et al., 2020). In this case, initially, both species evolved to grow faster, and the slower-growing species was preserved due to stochastic fluctuations in species composition during collective reproduction. Eventually, both species evolved to grow sufficiently fast to deplete the shared resource during collective maturation, and evolution in competition coefficients then acted to stabilize the species ratio to the target value (Doulcier et al., 2020). Regardless, earlier studies are often limited to numerical explorations, with prohibitive costs for a full characterization of the parameter space for such nested populations (population of collectives, and populations of variants within a collective).

We mathematically examine the selection of composition in collectives consisting of populations growing at different rates. We made simplifying assumptions so that we can analytically examine the evolutionary tipping point between intra-collective and inter-collective selection. We show that this tipping point creates a ‘waterfall’ effect which restricts not only which target compositions are achievable, but also the initial composition required to achieve the target. We also investigate how the range of achievable target composition is affected by the total population size in Newborns and the total number of collectives under selection. Finally, we show that the waterfall phenomenon extends to systems with more than 2 populations.

## Results and discussion

To enable the derivation of an analytical expression, we have made the following simplifying assumptions. First, growth is always exponential, without complications such as resource limitation, ecological interactions between the two populations, or density-dependent growth. Thus, the exponential growth equation can be used. Second, we initially consider only two populations (genotypes or species): the fast-growing F population with size $F$ and the slow-growing S population with size $S$. We do not consider a spectrum of mutants or species, since with more than two populations, an analytical solution becomes very difficult. Finally, the single top-functioning community is chosen to reproduce, which allows us to employ the simplest version of the extreme value theory (see section below for further justification).

Our goal is to select for collective composition in terms of F frequency $f=F/(S+F)$, or equivalently, S frequency $s=1−f$. More precisely, we want collectives such that after maturation time $\tau$, $f(\tau)$ is as close to the target value $f^$ as possible (Figure 1). Note that even if the target frequency has been achieved, since F frequency will always increase during maturation, inter-collective selection is required in each cycle to maintain the target frequency.

We will start with a complete model where S mutates to F at a nonzero mutation rate $\mu$. We made this choice because it is more challenging to attain or maintain the target frequency when the abundance of fast-growing F is further increased via mutations. This scenario is encountered in biotechnology: an engineered pathway will slow down cell growth, and breaking the pathway (and thus faster growth) is much easier than the other way around. When the mutation rate is set to zero, the same model can be used to capture collectives of two species with different growth rates. We show that intermediate F frequencies or equivalently, intermediate S frequencies, are the hardest targets to achieve. We then show using simulations that similar conclusions hold when selecting for a target composition in collectives of three populations.

### Model structure

A selection cycle (Figure 1; Table 1) starts with a total of $g$ Newborn collectives. At the beginning of cycle $k$ ($t=0$), each Newborn collective has a fixed total cell number $N_{0}=S_{k,0}^{(i)}+F_{k,0}^{(i)}$ where $S_{k,t}^{(i)}$ and $F_{k,t}^{(i)}$ denote the numbers of S and F cells in collective $i$ ($1\leqi\leqg$) at time $t$ ($0\leqt\leq\tau$) of cycle $k$. The average F frequency among the $g$ Newborn collectives in cycle $k$ is $f¯_{k,0}$, such that the initial F cell number in each Newborn is drawn from the binomial distribution $Binom(N_{0},f¯_{k,0})$.

**Table 1.**
 Nomenclature.


<table>
  <thead>
    <tr>
      <th>Variables</th>
      <th>Representing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>S\begin{document}$S$\end{document}</td>
      <td>Number of slower-growing (S) cells</td>
    </tr>
    <tr>
      <td>F\begin{document}$ F$\end{document}</td>
      <td>Number of faster-growing (F) cells</td>
    </tr>
    <tr>
      <td>N\begin{document}$ N$\end{document}</td>
      <td>Total cell numbers in a collective, N=S+F\begin{document}$N=S+F$\end{document}</td>
    </tr>
    <tr>
      <td>s\begin{document}$  s$\end{document}</td>
      <td>Frequency of S cells, s=S/(S+F)\begin{document}$s = S/(S + F)$\end{document}</td>
    </tr>
    <tr>
      <td>f\begin{document}$f$\end{document}</td>
      <td>Frequency of F cells, f=F/(S+F)=1−s\begin{document}$f=F/(S+F)=1-s$\end{document}</td>
    </tr>
    <tr>
      <td>f∗\begin{document}$ f^{*}$\end{document}</td>
      <td>F frequency of the selected collective in a cycle</td>
    </tr>
    <tr>
      <td>Parameters</td>
      <td>Representing</td>
    </tr>
    <tr>
      <td>rS\begin{document}$ r_{S}$\end{document}</td>
      <td>Growth rate of S</td>
    </tr>
    <tr>
      <td>ω&gt;0\begin{document}$\omega \gt 0$\end{document}</td>
      <td>Growth rate advantage of F over S</td>
    </tr>
    <tr>
      <td>μ\begin{document}$  \mu$\end{document}</td>
      <td>Mutation rate from S to F</td>
    </tr>
    <tr>
      <td>g\begin{document}$ g$\end{document}</td>
      <td>Total number of collectives</td>
    </tr>
    <tr>
      <td>τ\begin{document}$\tau$\end{document}</td>
      <td>Maturation time</td>
    </tr>
    <tr>
      <td>N0\begin{document}$N_{0}$\end{document}</td>
      <td>Total number of cells in Newborn, or Newborn size</td>
    </tr>
    <tr>
      <td></td>
      <td>Target frequency in s\begin{document}$s$\end{document} or f\begin{document}$f$\end{document}.</td>
    </tr>
    <tr>
      <td>fL,fH\begin{document}$f^{L},f^H$\end{document}</td>
      <td>Low and High thresholds of inaccessible f^\begin{document}$\hat{f}$\end{document}</td>
    </tr>
    <tr>
      <td>Rτ\begin{document}$ R_{\tau}$\end{document}</td>
      <td>Fold-growth of S cells over time τ\begin{document}$\tau$\end{document}, Rτ=erSτ\begin{document}$R_{\tau}=e^{r_{S}\tau}$\end{document}</td>
    </tr>
    <tr>
      <td>Wτ\begin{document}$ W_{\tau}$\end{document}</td>
      <td>Fold ratio change of F cells over S cells over time τ\begin{document}$\tau$\end{document}, Wτ=eωτ\begin{document}$W_{\tau}=e^{\omega\tau}$\end{document}</td>
    </tr>
  </tbody>
</table>

Collectives are allowed to grow for time $\tau$ (‘Maturation’ in Figure 1). During maturation, S and F grow at rates $r_{S}$ and $r_{S}+\omega$ ($\omega>0$), respectively. If maturation time $\tau$ is too small, a matured collective (‘Adult’) does not have enough cells to reproduce $g$ Newborn collectives with $N_{0}$ cells. On the other hand, if maturation time $\tau$ is too long, fast-growing F will take over. Hence, we set the maturation time $\tau=ln⁡(g+1)/r_{S}$, which guarantees sufficient cells to produce $g$ Newborn collectives from a single Adult collective. At the end of a cycle, a single Adult with the highest function (with F frequency $f$ closest to the target frequency $f^$) is chosen to reproduce $g$ Newborn collectives, each with $N_{0}$ cells (‘Selection’ and ’Reproduction’ in Figure 1). Note that even though S and F do not compete for nutrients, they compete for space: because the total number of cells transferred to the next cycle is fixed, an overabundance of one population will reduce the likelihood of the other being propagated.

Collective function is dictated by the Adult’s F frequency $f$. Among all Adult collectives, the selected Adult is the one whose F frequency is closest to the target value, $f^$. In contrast with findings from an earlier study (Xie et al., 2019), choosing top 1 is more effective than the less stringent ‘choosing top 5%.’ In the earlier study, variation in the collective trait is partly due to nonheritable factors such as random fluctuations in Newborn biomass. In that context, a less stringent selection criterion proved more effective, as it helped retain collectives with favorable genotypes that might have exhibited suboptimal collective traits due to unfavorable non-heritable factors. However, since this study excludes non-heritable variations in collective traits, selecting the top 1 collective is more effective than selecting the top 5% (see Appendix 7—figure 1).

The selected Adult, with F frequency denoted as $f^{∗}$, is then used to reproduce $g$ offspring collectives, each with $N_{0}$ total cells. The number of F cells in a newborn follows a binomial distribution $B(N_{0},f^{∗})$. By repeating the selection cycle, we aim to achieve and maintain the target composition $f^$.

Overall, our model considers mutational stochasticity, as well as demographic stochasticity in terms of stochastic birth and stochastic sampling of a parent collective by offspring collectives. Other types of stochasticity, such as environmental stochasticity and measurement noise, are not considered and require future research.

### The success of collective selection is constrained by the target composition, and sometimes also by the initial composition

Since intra-collective selection favors F, we expect that a higher target $f^$ (a lower target $s^$) is easier to achieve. By ‘achieve,’ we mean that the absolute error $d$ between the target frequency $f^$ and the selected frequency averaged among independent simulations $⟨f^{∗}⟩$ is smaller than 0.05 (i.e.$d=|⟨f^{∗}⟩−f^|\leq0.05$).

We fixed $N_{0},$ the total population size of a Newborn to 1000, and obtained selection dynamics for various initial and target F frequencies by implementing stochastic simulations (Appendix 1). If the target $f^$ is high (e.g. 0.9, Figure 2a magenta), selection is successful (computed absolute errors Appendix 1—figure 4): regardless of the initial frequency, $f^{∗}$ of the chosen collective eventually converges to the target $f^$ and stays around it. In contrast, without collective-level selection (e.g. choosing a random collective to reproduce), F frequency increases until F reaches fixation (Supplementary information Appendix 1—figure 3b).

![Figure 2.](https://cdn.elifesciences.org/articles/97461/elife-97461-fig2-v1.jpg)

**Figure 2.:** (a–c) F frequency of the selected Adult collective ($f^{∗}$) over cycles at different target $f^$ values (long dashed lines). $f^$ between $f^{L}$ and $f^{H}$ (orange dotted and solid line segments) is inaccessible where selection will fail. (a) A high target F frequency (e.g.$f^=0.9>f^{H}$; magenta) can be achieved from any initial frequency (black dots). (b) An intermediate target frequency (e.g.$f^{L}<f^=0.5<f^{H}$; green) is never achievable, as all initial conditions converge to  $f^{H}$. (c) A low target frequency (e.g. $f^=0.1<f^{L}$; dark blue) is achievable, but only from initial frequencies below $f^{L}$. For initial frequencies at $f^{L}$, stochastic outcomes (gray curves) are observed: while some replicates reached the target frequency, others reached $f^{H}$. For parameters, we used S growth rate $r_{S}=0.5$, F growth advantage $\omega=0.03$, mutation rate $\mu=0.0001$, maturation time $\tau≈4.8$, and $N_{0}=1000$. The number of collectives $g=10$. Each black line is averaged from independent 300 realizations. (d) Inter-collective selection opposes intra-collective selection. We plot probability density distributions of F frequency $f$ during two consecutive cycles when selection is successful. Data correspond to cycles 31 and 32 from the second lowest initial point in c. $Δf$ is the selection progress within a cycle (see Box 1). Black triangle: median. (e) Two accessible regions (gold). Either high $f^$ ($f^>f^{H}$; region 2) or low $f^$ starting from low initial $f$ ($f^<f^{L}$ and $f¯_{1,0}<f^{L}$; region 1) can be achieved. We theoretically predict (by numerically integrating Equation 1) $f^{H}$ (orange solid line) and $f^{L}$ (orange dotted line), which agree with simulation results (gold regions). (f) Example trajectories from initial compositions (black dots) to the target compositions (dashed lines). The gold areas indicate the region of initial frequencies where the target frequency can be achieved. (g) The tension between intra-collective selection and inter-collective selection creates a ‘waterfall’ phenomenon. See the main text for details.

In contrast, an intermediate target frequency (e.g. $f^=0.5$; Figure 2b green) is never achievable. High initial F frequencies (e.g. 0.95) decline toward the target but stabilize at the ‘high-threshold’ $f^{H}$ (∼ 0.7, solid orange line segment in Figure 2a-c) above the target. Low initial F frequencies (e.g. 0) increase toward the target, but then overshoot and stabilize at the $f^{H}$ value.

If the target frequency is low (e.g. $f^=0.1$; Figure 2c dark blue), artificial selection succeeds when the initial frequency is below the ‘lower-threshold’ $f^{L}$ (dotted orange line segment in Figure 2a-c). Initial F frequencies above $f^{L}$ (e.g. 0.45 and 0.95) converge to $f^{H}$ instead. Initial F frequencies near $f^{L}$ display stochastic trajectories, converging to either $f^{H}$ or $f^$.

To achieve target $f^$, inter-collective selection must overcome intra-collective selection. We can visualize the distributions of $f$ over two consecutive cycles (bottom to top, Figure 2d) where $f$ started above target $f^$. When newborns matured into adults, the distribution of $f$ up-shifted due to intra-collective selection. The distribution of $f$ was then down-shifted toward the target due to inter-collective selection. If the magnitude of down-shift exceeded that of up-shift, progress toward the target was made. During reproduction of collectives, the distribution of $f$ retained the same mean but became broader due to stochastic sampling by the Newborns from their parent.

In summary, two regions of target frequencies are ‘accessible’ (gold in Figure 2e, f; Box 1): (1) target frequencies above $f^{H}$ ($f^>f^{H}$) or (2) target frequencies below $f^{L}$ ($f^<f^{L}$) and starting at an average frequency below $f^{L}$ ($f¯_{1,0}<f^{L}$).

### Intra-collective evolution is the fastest at intermediate F frequencies, creating the ‘waterfall’ phenomenon

To understand what gives rise to the two accessible regions, we calculated $△f$, the selection progress in F frequency over two consecutive cycles (Box 1, Equation 2). The solution (Figure 3a, green) has the same shape as results from numerically integrating Equation 1 (Figure 3a, orange) and from stochastic simulations (Figure 3a, blue).

![Figure 3.](https://cdn.elifesciences.org/articles/97461/elife-97461-fig3-v1.jpg)

**Figure 3.:** (a) The change in F frequency over one cycle. When $f_{k}^{∗}$ is sufficiently low or high, inter-collective selection can lower the F frequency to below $f_{k}^{∗}$ ($Δf<0$). The points where $Δf=0$ (in the orange line) are denoted as $f^{L}$ and $f^{H}$, corresponding to the boundaries in Figure 2. (b) The distributions of frequency differences obtained by 1000 numerical simulations. The cyan, purple, and black box plots respectively indicate the changes in F frequency after intra-collective selection (the mean frequency among the 100 Adults minus the mean frequency among the 100 Newborns during maturation), after inter-collective selection (the frequency of the 1 selected Adult minus the mean frequency among the 100 Adults), and over one selection cycle (the frequency of the selected Adult of one cycle minus that of the previous cycle). The box ranges from 25% to 75% of the distribution, and the median is indicated by a line across the box. The upper and lower whiskers indicate maximum and minimum values of the distribution. ***p<0.001  in an unpaired $t$-test.

If $△f$ is negative, then inter-collective selection will succeed in countering intra-collective selection and reducing $f$ toward the target. $△f$ is negative if the selected $f_{k}^{∗}$ is low or high, but not if it is intermediate between $f^{L}$ and $f^{H}$ (Figure 3a). This is because the increase in $f$ during maturation is the most drastic when Newborn $f$ is intermediate (Figure 3b), for intuitive reasons: when Newborn $f$ is low, the increase in $f$ will be minor; when Newborn $f$ is high, the fitness advantage of F over the population average is small and hence the increase is also minor. Thus, when Newborn F frequency is intermediate, intra-collective selection is the strongest and may overwhelm inter-collective selection (Figure 3b and Appendix 2—figure 2a). Not surprisingly, similar conclusions are derived where S and F are slow-growing and fast-growing species which cannot be converted through mutations (Appendix 4 and Appendix 4—figure 1).

Thus, inter-collective selection is akin to a raftman rowing the raft to a target, while intra-collective selection is akin to a waterfall. This metaphor is best understood in terms of S frequency $s=1−f$. The lower-threshold $f^{L}$ corresponds to higher-threshold in $s^{H}=1−f^{L}$. Intra-collective selection is akin to a waterfall, driving the S frequency $s$ from high to low (Figure 2g). Intra-collective selection acts the strongest when $s$ is intermediate ($s^{L}<s<s^{H}$), similar to the vertical drop of the fall. Intra-collective selection acts weakly at high ($>s^{H}$) or low ($<s^{L}$) $s$ , similar to the gentle sloped upper and lower pools of the fall (regions 1 and 2 of Figure 2e and g). Thus, an intermediate target frequency can be impossible to achieve: a raft starting from the upper pool will be flushed down to $s^{L}$ ($f^{H}$), while a raft starting from the lower pool cannot go beyond $s^{L}$ ($f^{H}$). In contrast, a low target S frequency (in the lower pool) is always achievable. Finally, a high target S frequency (in the upper pool) can only be achieved if starting from the upper pool (as the raft cannot jump to the upper pool if starting from below).

### Manipulating experimental setups to expand the achievable target region

In Equation 2; Box 1, selection progress $△f$ depends on the total number of collectives under selection ($g$). $△f$ also depends on the mean and the standard deviation of Adult F frequency — $f¯(\tau)$ and $\sigma_{f}(\tau)$. Equations 3 and 4 of Box 1 provide simplified expressions of $f¯(\tau)$ and $\sigma_{f}(\tau)$ when mutation rate $\mu$ has been set to 0. When the mutation rate $\mu$ is not zero (Equations 48 and 49 in Appendix 2), selection progress is additionally influenced by $\frac{\mu}{\omega}$ (mutation rate $\mu$ scaled with fitness difference $\omega$).

Our goal is to make $△f$ as negative as possible so that any increase in $f$ during collective maturation may be reduced. From Equation 2 in Box 1, a small $f¯(\tau)$ will facilitate collective-level selection. Additionally, a large $\sigma_{f}(\tau)$ will also facilitate collective-level selection due to negative $Φ^{−1}(\frac{ln⁡2}{g})$. Note that since $\frac{ln⁡2}{g}$<0.5 for $g\geq2$, $Φ^{−1}(\frac{ln⁡2}{g})$ — corresponding to the number $y$ such that the probability of a standard normal random variable being less than or equal to $y$ is $\frac{ln⁡2}{g}$ — is negative.

From Equation 4 in Box 1, $\sigma_{f}(\tau)$ will be large if Newborn size $N_{0}$ is small. Indeed, as Newborn size $N_{0}$ declines, the region of achievable target frequency expands (gold area in Figure 4a). If the Newborn size $N_{0}$ is sufficiently small (e.g. ≤ 700 in our parameter regime), any target frequency can be reached. An analytical approximation of the maximal Newborn size permissible for all target frequencies is given in Appendix 3.

![Figure 4.](https://cdn.elifesciences.org/articles/97461/elife-97461-fig4-v1.jpg)

**Figure 4.:** (a) Reducing the population size in Newborn $N_{0}$ expands the region of success. In the gold area, the probability that $f_{k+1}^{∗}$ becomes smaller than $f_{k}^{∗}$ in a cycle is more than 50%. We used $g=10$ and $\tau≈4.8$. Figures 2–3 correspond to $N˘_{0}=1000$ in this graph. Black dotted line indicates the critical Newborn size below which all target frequencies can be achieved. (b) Increasing the total number of collectives $g$ also expands the region of success, although only slightly. We used a fixed Newborn size $N_{0}=1000$. The maturation time $\tau=log⁡(100)/r_{S}≈9.2$ is set to be long enough so that an Adult can generate at least 100 Newborns. (c) Increasing the maturation time shrinks the region of success. We used a fixed Newborn size $N_{0}=1000$ and number of collectives $g=10$.

From Equations 3 and 4 in Box 1, maturation time $\tau$ affects $f¯(\tau)$ and $\sigma_{f}(\tau)$ through $W_{\tau}=e^{\omega\tau}$ (the fold change in F/S over $\tau$), and affects $\sigma_{f}(\tau)$ additionally through $R_{\tau}=e^{r_{S}\tau}$ (fold-growth of S over $\tau$). Longer $\tau$ increases $f¯(\tau)$ and is thus detrimental to selection progress. The relationship between $\sigma_{f}(\tau)$ and $\tau$ is not monotonic (Appendix 2—figure 2c), meaning that an intermediate value of $\tau$ is the best for achieving large $\sigma_{f}(\tau)$. However, the effect of $f¯(\tau)$ dominates that of $\sigma_{f}(\tau)$ and therefore, the region of success monotonically reduces with longer maturation time (Figure 4c). Similarly, $f¯(\tau)$ will be small if $\omega$ (fitness advantage of F over S) is small. Indeed, as $\omega$ becomes larger, the region of success becomes smaller (Appendix 5—figure 1).

$g$, the number of collectives under selection, also affects selection outcomes. As $g$ increases, the value of $Φ^{−1}(\frac{ln⁡2}{g})$ becomes more negative, and so does $△f$ — meaning collective-level selection will be more effective. Intuitively, with more collectives, the chance of finding a $f$ closer to the target is more likely. Thus, a larger number of collectives broadens the region of success (Figure 4b). However, the effect of $g$ is not dramatic. To see why, we note that the only place that $g$ appears is Equation 2 in $Φ^{−1}(\frac{1}{g})$. When $g$ becomes large, $Φ^{−1}(\frac{1}{g})$ is asymptotically expressed as $Φ^{−1}(\frac{1}{g})≈−\sqrt{2ln⁡g−ln⁡[ln⁡g]+⋯}$ (Appendix 2) (Phllip, 1960), and thus does not change dramatically as $g$ varies.

### The waterfall phenomenon in a higher dimension

To examine the waterfall effect in a higher dimension, we investigate a three-population system where a faster-growing population (FF) grows faster than the fast-growing population (F) which grows faster than the slow-growing population (S) (Figure 5a and Appendix 8—figure 1). In the three-population case, the evolutionary trajectory travels in a two-dimensional plane. A target population composition can be achieved if inter-collective selection can sufficiently reduce the frequencies of F as well as FF (accessible regions, gold in Figure 5b).

![Figure 5.](https://cdn.elifesciences.org/articles/97461/elife-97461-fig5-v1.jpg)

**Figure 5.:** (a) During collective maturation, a slow-growing population (S) (with growth rate $r_{S}$; light gray) can mutate to a fast-growing population (F) (with growth rate $r_{S}+\omega$; medium gray), which can mutate further into a faster-growing population (FF) (with growth rate $r_{S}+2\omega$; dark gray). Here, the rates of both mutational steps are $\mu$, and $\omega>0$. (b) Evolutionary trajectories from various initial compositions (open circles) to various targets (filled triangles). Intra-collective evolution favors FF over F (vertical blue arrow) over S (horizontal blue arrow). The accessible regions are marked gold (see Appendix 1). We obtain final compositions starting from several initial compositions while aiming for different target compositions in i, ii, and iii. The evolutionary trajectories are shown in dots with color gradients from initial time (light grey) to final time (dark grey). (i) A target composition with a high FF frequency is always achievable. (ii) A target composition with intermediate FF frequency is never achievable. (iii) A target composition with low FF frequency is achievable only if starting from an appropriate initial composition such that the entire trajectory never meanders away from the accessible region. The figures are drawn using the mpltern package (Ikeda et al., 2019). (c) The accessible region in the three-population problem is interpreted as an extension of the two-population problem. First, the accessible region between FF and S+F is given, and then the S+F region is stretched into S and F.

From numerical simulations, we identified two accessible regions: a small region near FF and a band region spanning from S to F (gold in Figure 5b i). Intuitively, the rate at which FF grows faster than S+F is greater than the rate at which F grows faster than S (see Appendix 8). Thus, the problem can initially be reduced to a two-population problem (i.e. FF versus F+S; Figure 5c left), and then expanded to a three-population problem (Figure 5c right).

Similar to the two-population case, targets in the inaccessible region are never achievable (Figure 5b ii), while those in the FF region are always achievable (Figure 5b i). Strikingly, a target composition in an accessible region may not be achievable even when the initial composition is within the same region: once the composition escapes the accessible region, the trajectory cannot return back to the accessible region (Figure 5biii, the leftmost initial condition). However, if the initial position is closer to the target in the accessible region, the target becomes achievable (Figure 5b iii, initial condition near the bottom). Note that here, the selection outcome is path-dependent in the sense of being sensitive to initial conditions. This phenomenon is distinct from hysteresis, where path-dependence results from whether a tuning parameter is increased or decreased.

In conclusion, we have investigated the evolutionary trajectories of population compositions in collectives under selection, which are governed by intra-collective selection (which favors fast-growing populations) and inter-collective selection (which, in our case, strives to counter fast-growing populations). Intra-collective selection has the strongest effect at intermediate frequencies of faster-growing populations, potentially creating an inaccessible region of target frequency analogous to the vertical drop of a waterfall. High and low target frequencies are both accessible, analogous to the lower and the upper pools of a waterfall, respectively. A less challenging target (high $f^$; low $s^$) is achievable from any initial position. In contrast, a more challenging target (low $f^$; high $s^$) is only achievable if the entire trajectory is contained within the region, similar to a raft striving to reach a point in the upper pool must start at and remain in the upper pool. Our work suggests that the strength of intra-collective selection is not constant, and that strategically choosing an appropriate starting point can be essential for successful collective selection.

## Materials and methods

### Stochastic simulations

A selection cycle is composed of three steps: maturation, selection, and reproduction. At the beginning of the cycle $k$, a collective $i$ has $S_{k,0}^{(i)}$ slow-growing cells and $F_{k,0}^{(i)}$ fast-growing cells. At the first cycle, the mean F frequency of collectives is set to be $f¯_{1,0}. F_{1,0}^{(i)}$ is sampled from the binomial distribution with mean $N_{0}f¯_{1,0}$. Then, $S_{1,0}^{(i)}(=N_{0}−F_{1,0}^{(i)})$ S cells are in the collective $i$. In the maturation step, we calculate $S_{k,\tau}^{(i)}$ and $F_{k,\tau}^{(i)}$ by using stochastic simulation. We can simulate the division and mutation of each individual cell stochastically by using the tau-leaping algorithm (Gillespie, 2001; Cao et al., 2006; see Appendix 1—figure 3). However, individual-based simulations require a long computing time. Instead, we randomly sample $S_{k,\tau}^{(i)}$ and $F_{k,\tau}^{(i)}$ from the joint probability density distribution $P(S_{k,\tau}^{(i)},F_{k,\tau}^{(i)})$. To obtain $P(S_{k,\tau}^{(i)},F_{k,\tau}^{(i)})$, we solve the master equation which describes the time evolution of the probability distribution $P(S_{k,t}^{(i)},F_{k,t}^{(i)})$ under the random processes (see Appendix 1). We assumed that $S_{k,\tau}^{(i)} and F_{k,\tau}^{(i)}$ are independent (as S and F populations grow independently without ecological interactions), and thus $P(S_{k,\tau}^{(i)},F_{k,\tau}^{(i)})$ is product of two probability density functions $P(S_{k,\tau}^{(i)}) and P(F_{k,\tau}^{(i)})$. Each distribution follows a Gaussian distribution, with the mean and variance numerically obtained from ordinary differential equations derived from the master equation (see Appendix 1). We choose the collective with the closest frequency to the target $f^$ to generates $g$ Newborns. The number of F cells is sampled from the binomial distribution with the mean of $N_{0}f_{k}^{∗}$. We start a new cycle with those Newborn collectives. Then, the number of S cells in a collective $i$ is $S_{k+1,0}^{(i)}=N_{0}−F_{k+1,0}^{(i)}$.

### Analytical approach to the conditional probability

The conditional probability distribution $Ψ(f_{k+1}^{∗}|f_{k}^{∗})$ of observing $f_{k+1}^{∗}$ at a given $f_{k}^{∗}$ is calculated by the following procedure. Given the selected collective in cycle $k$ with $f_{k}^{∗}$, the collective-level reproduction proceeds by sampling $g$ Newborn collectives with $N_{0}$ cells in cycle $k+1$. Each Newborn collective contains certain F numbers $F_{k+1,0}^{(1)},⋯,F_{k+1,0}^{(g)}$ at the beginning of the cycle $k+1$, which can be mapped into $f_{k+1,0}^{(1)},⋯,f_{k+1,0}^{(g)}$ with the constraint of $N_{0}$ cells. If the number of cells in the selected collective is large enough, the joint conditional distribution function $P(f_{k+1,0}^{(1)},⋯,f_{k+1,0}^{(g)}|f_{k}^{∗})$ is well described by the product of $g$ independent and identical Gaussian distribution $N(\mu,\sigma^{2})$. So we consider the frequencies of $g$ Newborn collectives as $g$ identical copies of the Gaussian random variable $f_{k+1,0}$. The mean and variance of $f_{k+1,0}$ are given by $m=f_{k}^{∗}$ and $\sigma^{2}=f_{k}^{∗}(1−f_{k}^{∗})/N_{0}$. Then, the conditional probability distribution function of $f_{k+1,0}$ being $ζ$ is given by

$$
P_{f_{k+1,0}}(ζ|f_{k}^{∗})=\frac{1}{\sqrt{2\pi}}exp⁡(−\frac{(ζ−m)^{2}}{2\sigma^{2}}).
$$

After the reproduction step, the Newborn collectives grow for time $\tau$. The frequency is changed from the given frequency $ζ$ to $f$ by division and mutation processes. We assume that the frequency $f$ of an Adult is also approximated by a Gaussian random variable $N(f¯(\tau),\sigma_{f}^{2}(\tau))$. The mean $f¯(\tau)$ and variance $\sigma_{f}^{2}(\tau)$ are calculated by using means and variances of $S$ and $F$ (see Appendix 2). Since $f¯(\tau)$ and $\sigma_{f}^{2}(\tau)$ also depend on $ζ$, the conditional probability distribution function of $f_{k+1,\tau}$ being $f$ is given by

$$
P_{f_{k+1,\tau}}(f|ζ)=\frac{1}{\sqrt{2\pi}}exp⁡(−\frac{(f−f¯(\tau))^{2}}{2\sigma_{f}^{2}(\tau)}).
$$

The conditional probability distribution of an Adult collective in cycle $k+1$ ($f_{k+1,\tau}$) to have frequency $f$ at a given $f_{k}^{∗}$ is calculated by multiplying two Gaussian distribution functions and integrating overall $ζ$ values, which is given by

$$
P_{f_{k+1,\tau}}(f|f_{k}^{∗})=\int_{0}^{1}dζ P_{f_{k+1,\tau}}(f|ζ) P_{f_{k+1,0}}(ζ|f_{k}^{∗}).
$$

Since we select the minimum frequency $f_{k+1}^{min}$ among $g$ identical copies of $f_{k+1,\tau}$, the conditional probability distribution function of $f_{k+1}^{min}$ follows a minimum value distribution, which is given in Equation 1. Here, for the case of $f^<f_{k}^{∗}$, the selected frequency $f_{k+1,0}$ is the minimum frequency $f_{k+1}^{min}$. So we have $Ψ(f_{k+1}^{∗}|f_{k}^{∗})$ by replacing $f_{k+1}^{min}$ with $f_{k+1}^{∗}$.

We assume that the conditional probability distribution in Equation 7 follows a normal distribution, whose mean and variances are described by Equation 48 and Equation 49. Then, the extreme value theory (Gumbel, 1958) estimates the median of the selected Adult by

$$
Median(f_{k+1}^{∗})=f¯(\tau)+[Φ^{−1}(\frac{ln⁡2}{g})]\sigma_{f}(\tau).
$$

The selection progress $Δf$ in Equation 2 is obtained by subtracting $f_{k}^{∗}$ from Equation 8.
