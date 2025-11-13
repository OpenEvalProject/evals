# Catalytic growth in a shared enzyme pool ensures robust control of centrosome size

## Authors

- Deb Sankar Banerjee<sup>1</sup> ([ORCID: 0000-0003-4452-7982](https://orcid.org/0000-0003-4452-7982))
- Shiladitya Banerjee<sup>1</sup> ([ORCID: 0000-0001-8000-2556](https://orcid.org/0000-0001-8000-2556)) †

### Affiliations

1. Department of Physics, Carnegie Mellon University Pittsburgh United States ([ROR:05x2bcf33](https://ror.org/05x2bcf33))
2. James Franck Institute, University of Chicago Chicago United States ([ROR:024mw5h28](https://ror.org/024mw5h28))
3. School of Physics, Georgia Institute of Technology Atlanta United States ([ROR:01zkghx44](https://ror.org/01zkghx44))

† Corresponding author

## Abstract

Accurate regulation of centrosome size is essential for ensuring error-free cell division, and dysregulation of centrosome size has been linked to various pathologies, including developmental defects and cancer. While a universally accepted model for centrosome size regulation is lacking, prior theoretical and experimental works suggest a centrosome growth model involving autocatalytic assembly of the pericentriolar material. Here, we show that the autocatalytic assembly model fails to explain the attainment of equal centrosome sizes, which is crucial for error-free cell division. Incorporating latest experimental findings into the molecular mechanisms governing centrosome assembly, we introduce a new quantitative theory for centrosome growth involving catalytic assembly within a shared pool of enzymes. Our model successfully achieves robust size equality between maturing centrosome pairs, mirroring cooperative growth dynamics observed in experiments. To validate our theoretical predictions, we compare them with available experimental data and demonstrate the broad applicability of the catalytic growth model across different organisms, which exhibit distinct growth dynamics and size scaling characteristics.

## Introduction

Centrosomes are membraneless organelles that act as microtubule organizing centers during mitotic spindle formation (Gould and Borisy, 1977). Prior to cell division, centrosomes grow many folds in size by accumulating various types of proteins including microtubule nucleators, in a process known as centrosome maturation (Palazzo, 1999). Tight control of centrosome size is functionally important for the cell as aberrations in centrosome growth and size can lead to errors in chromosome segregation (Krämer et al., 2002). This may result in aneuploidy, which is associated with a range of problems, including birth defects, developmental abnormalities, and cancer (Basto et al., 2008; D’Assoro et al., 2002; Levine et al., 2017). Previous works have suggested that centrosomes grow cooperatively and regulate their size through a coordinated assembly of the pericentriolar material, mediated by complex signaling pathways and regulatory proteins (Alvarez Rodrigo et al., 2019; Conduit et al., 2014b; Zwicker et al., 2014). Despite the significant progress on uncovering the molecular components regulating centrosome assembly (Conduit et al., 2015b), a quantitative model connecting the molecular mechanisms of growth to centrosome size regulation is lacking.

Centrosomes are composed of a porous scaffold-like structure (Schnackenberg et al., 1998; Feng et al., 2017) known as the pericentriolar material (PCM), organized around a pair of centrioles at the core (Figure 1A). An individual cell starts with a single centrosome in the G1 phase, undergoes centriole duplication in the S phase, followed by the formation of two centrosomes in the G2/M phase (Figure 1A). During centrosome maturation, the two spatially separated centrosomes grow in size by adding material to their PCMs from a cytoplasmic pool of building blocks (Decker et al., 2011; Woodruff et al., 2014; Kemp et al., 2004; Pelletier et al., 2004; Conduit et al., 2014b), while the centrioles themselves do not grow. Following maturation, the two centrosomes achieve equal sizes (Decker et al., 2011; Zwicker et al., 2014; Alvarez Rodrigo et al., 2019), which is deemed essential in the establishment of a symmetric bipolar spindle (Conduit et al., 2015b). This size equality is vital for ensuring error-free cellular division, as spindle size is directly proportional to centrosome sizes (Greenan et al., 2010). However, the mechanisms by which centrosomes within a cell achieve equal size remain poorly understood.

![Figure 1.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig1-v1.jpg)

**Figure 1.:** (A) Schematic showing the dynamics of centrosomes during the cell cycle. In the G1 phase, there is a single centrosome with mother (M) and daughter (D) centrioles at the core, surrounded by the pericentriolar material (PCM). The two new centriole pairs with the old mother (oM) and the new mother (nM) separate into two centrosomes in the G2/M phase after centriole duplication. The spatially separated centrosomes then grow via a process called centrosome maturation (red arrow), prior to cell division. (B) Schematic of the autocatalytic growth model for centrosomes, where the assembly rate increases with increasing centrosome size. (C) Autocatalytic growth of centrosomes captures the sigmoidal size dynamics for a single and a pair of centrosomes, but is unable to ensure size equality of a centrosome pair. See Table 1 for a list of parameter values.

**Table 1.**
 Parameter Values.


<table>
  <thead>
    <tr>
      <th>Figure</th>
      <th>Parameter Values</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Figure 1C</td>
      <td>ρ0(=N/Vc)=0.033μM, k0+ = 600μM−1s−1, k1+ = 0.6μM−1s−1, k− = 0.005s−1</td>
      <td>based on Zwicker et al., 2014</td>
    </tr>
    <tr>
      <td>Figure 2A</td>
      <td>ρ0=0.033μM, k− = 0.005s−1</td>
      <td>based on Zwicker et al., 2014</td>
    </tr>
    <tr>
      <td>Figure 2D</td>
      <td>k+ = 1000μM−1s−1, ρ0=0.1μM</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 3C</td>
      <td>ρ0= 1μM, [E] = 0.1μM, k+=1μM−1s−1, k∗=1000μM−1s−1, kE∗=5s−1, k1∗=1μM−1s−1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 3D</td>
      <td>ρ0 = 0.05μM, [E] = 0.1μM, k+=1μM−1s−1, k∗=2000μM−1s−1, kE∗=10s−1, k1*=100⁢μ⁢M-1⁢s-1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 3E</td>
      <td>ρ0 = 0.02μM, [E] = 0.09μM, k+=1μM−1s−1, k∗=8×104μM−1s−1, kE∗=4.25s−1, k1*=0.1⁢μ⁢M-1⁢s-1</td>
      <td>From fitting experimental data</td>
    </tr>
    <tr>
      <td>Figure 3F</td>
      <td>ρ0 = 1μM, k∗=1000μM−1s−1, kE∗=5s−1, k1∗=10μM−1s−1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 3G &amp; H</td>
      <td>ρ0 = 0.15μM, [E] = 0.085μM, k+=1μM−1s−1, k∗=1000μM−1s−1, kE∗=1s−1, k1∗=5μM−1s−1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 4A</td>
      <td>Same as Figure 3E</td>
      <td>From fitting experimental data</td>
    </tr>
    <tr>
      <td>Figure 4B</td>
      <td>ρ0 = 0.1μM, [E] = 0.05μM, k+=100μM−1s−1, k∗=2000μM−1s−1, kE∗=10s−1, k1∗=100μM−1s−1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 4D</td>
      <td>ρ0 = 0.02μM, [Es⁢s*] = 0.01μM, k1∗=0.1μM−1s−1, Vc=25000μm3</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 5B &amp; D</td>
      <td>ρ0 = 0.5μM, [E] = 0.1μM, k+=60⁢μ⁢M-1⁢s-1, k∗=2000μM−1s−1, kE*=10⁢s-1, k1∗=100μM−1s−1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 5C &amp; E</td>
      <td>ρ0=0.033μM, k0+ = 60μM−1s−1, k1+ = 0.6μM−1s−1, k- = 0.005s−1</td>
      <td>based on Zwicker et al., 2014</td>
    </tr>
    <tr>
      <td>Figure 6B</td>
      <td>[ρa] = 0.25μM, [ρb] = 0.35μM, [ρE] = 0.015μM, other parameters are same as below</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Figure 6C &amp; D</td>
      <td>[ρa] = 0.25μM, [ρb] = 0.5μM, [ρE] = 0.01μM, ka+=10⁢μ⁢M-1⁢s-1, kb0+=0.5μM−1s−1, kb⁢0-=0.01⁢s-1,</td>
      <td>-</td>
    </tr>
    <tr>
      <td></td>
      <td>kaE+=5×103μM−1s−1, kE⁢b+=103⁢μ⁢M-1⁢s-1, kb⁢1+=104⁢μ⁢M-1⁢s-1, kb⁢1-=5×10-3⁢s-1, ka-=5×10-3⁢s-1</td>
      <td></td>
    </tr>
    <tr>
      <td>Fixed parameters</td>
      <td>δ⁢v=2×10-4⁢μ⁢m3, V0=5×10-3⁢μ⁢m3, k-=5×10-3⁢s-1, Vc=5000⁢μ⁢m3</td>
      <td>estimates &amp; Zwicker et al., 2014</td>
    </tr>
  </tbody>
</table>

A variety of qualitative and quantitative models of centrosome size regulation have emerged in recent years. These include the limiting pool theory (Decker et al., 2011; Goehring and Hyman, 2012), liquid-liquid phase separation model for PCM assembly (Zwicker et al., 2014), reaction-diffusion models (Mahen et al., 2011; Mahen and Venkitaraman, 2012), and centriole-driven assembly of PCM (Conduit et al., 2010a, Conduit et al., 2014b; Alvarez Rodrigo et al., 2019; Kirkham et al., 2003; Banerjee and Banerjee, 2022). While there is no universally accepted model for centrosome size regulation, all these models indicate a positive feedback mechanism underlying centrosome assembly. For instance, Zwicker et al., 2014 described PCM assembly in C. elegans as an autocatalytic process, assembled from a single limiting component undergoing active phase segregation through centriole activity. The authors suggested that a modified version of this model may also apply to centrosome maturation in Drosophila. While this model captures sigmoidal growth dynamics observed experimentally and the scaling of centrosome size with cell size, autocatalytic growth of centrosome pairs can induce significant discrepancies in size. We discuss how small initial differences in centrosome size could be amplified during the process of autocatalytic growth, as the larger centrosome would incorporate more material, thereby outcompeting the smaller one.

Another category of models, based on a large body of recent experimental works on Drosophila (Conduit et al., 2010a, Conduit et al., 2014b; Alvarez Rodrigo et al., 2019; Raff, 2019), suggests that PCM assembly occurs locally around the centriole, driven by a positive feedback loop between the scaffold-former PCM components such as Centrosomin (Cnn) and Spindle defective-2 (Spd-2) facilitated by enzymes like Polo or Polo-like-kinase (Plks; Alvarez Rodrigo et al., 2019) and this mechanism of growth appears to remain conserved across different organisms enacted by functionally homologous proteins for example SPD-5 and SPD-2 in worms (Alvarez Rodrigo et al., 2019; Raff, 2019; Aljiboury and Hehnly, 2023).

In a recent study, we employed quantitative modeling to demonstrate that localized assembly around the centriole, accompanied by distributed turnover within the PCM, can ensure centrosome size equality (Banerjee and Banerjee, 2022). However, this model did not take into account positive feedback between PCM components, and was thus unable to capture the cooperative nature of growth dynamics. Thus, none of the existing quantitative models can account for robustness in centrosome size equality in the presence of positive feedback. Furthermore, intracellular noise and the distinct nature of centrioles within the two centrosomes (old mother centriole and new mother centriole, depicted in Figure 1A) can give rise to fluctuations in centrosome size and introduce initial disparities in size during the maturation process. Consequently, a robust size regulation mechanism is required to achieve centrosome size parity, despite the presence of noise in growth and initial size differences.

Here, we present a quantitative theory for size regulation of a centrosome pair via catalytic assembly of the PCM from a cytoplasmic pool of enzymes and molecular components. We first establish that autocatalytic growth of centrosomes in a shared subunit pool results in amplification of initial size differences, leading to significant size inequality after maturation. Then we propose a new model of catalytic growth of centrosomes in a shared pool of building blocks and enzymes. Our theory is based on recent experiments uncovering the interactions of the molecular components of centrosome assembly, that is Polo-dependent positive feedback between Cnn and Spd-2 in Drosophila (Conduit et al., 2010a, Conduit et al., 2014b; Alvarez Rodrigo et al., 2019), and conserved functionally similar proteins that may constitute a similar pathway in other organisms like C. elegans, Xenopus, Zebrafish, and Human (Raff, 2019; Aljiboury and Hehnly, 2023). We show that this model ensures robust size control of centrosomes while capturing several key features of centrosome growth observed experimentally, including the growth of two stable centrosomes of equal size after maturation observed in Drosophila (Conduit et al., 2015b) and C. elegans (Zwicker et al., 2014), sigmoidal growth dynamics (Zwicker et al., 2014; Decker et al., 2011) and tunable scaling of centrosome size with cell size and centrosome number observed in C. elegans (Decker et al., 2011) and Drosophila (Wong et al., 2022), and the ability to robustly create centrosomes of different size from differences in centriole activity as observed in Drosophila male germ line stem cells (Conduit and Raff, 2010b) and larval neuroblasts (Januschke et al., 2013). We show that our model can explain seemingly different growth behaviours seen in worms and flies by comparing theoretical results with experimentally observed trends from these different organisms demonstrating the potential applicability of our model across different species. We further develop a two-component model of catalytic growth to explicitly show that without the sharing of the enzyme pool, centrosome size regulation is not robust when accounting for the experimentally observed enzyme-mediated positive feedback between the two components (Alvarez Rodrigo et al., 2019).

## Results

### Autocatalytic feedback in centrosome growth drives centrosome size inequality

Previous quantitative modeling of centrosome growth in C. elegans has suggested that centrosomes are autocatalytic droplets growing via phase separation in a limited pool of building blocks (Zwicker et al., 2014; Decker et al., 2011). Autocatalytic growth arises if the centrosome assembly rate increases with centrosome size, creating a size-dependent positive feedback (Figure 1B). To investigate if autocatalytic growth can ensure size equality of centrosomes, we considered a reaction-limited model of centrosome growth via stochastic assembly and disassembly of its subunits. Theoretical estimates indicate that the timescale of diffusion is much faster than the timescales of reactions observed in experiments. For instance, the scaffold formers diffuse over 5 – 10 μm in about 1 s while they have turnover timescale of ∼ 100 s (see Materials and methods section for more details). Although there are multiple essential components involved in PCM assembly (Dobbelaere et al., 2008; Conduit et al., 2010a, Conduit et al., 2014b), we first examined a one-component centrosome model to illustrate the role of autocatalytic growth on size control. The deterministic description for the growth of a centrosome pair is given by

$$
\frac{dn_{i}}{dt}=(k_{0}^{+}+k_{1}^{+}n_{i}(t))ρ(t)−k^{−}n_{i}(t),
$$

where $n_{i}(t)$ is the number of subunits in $i^{th}$ centrosome ($i=1,2$), $k_{0}^{+}$ and $k_{1}^{+}$ are the rate constants for non-cooperative and cooperative assembly, respectively, and $k^{−}$ is the disassembly rate constant. Equation 1 can be derived from the phase segregation model for centrosome assembly studied by Zwicker et al., 2014 (see Appendix), with $k_{0}^{+}$ and $k_{1}^{+}$ representing centriole activity and the strength of autocatalytic interaction, respectively. In Equation 1, $ρ(t)$ is the cytoplasmic concentration of centrosomal subunits, given by $ρ(t)=(N−n_{1}(t)−n_{2}(t))/V_{c}$ where $V_{c}$ is cell volume and N is the total amount of subunits in the cell. Centrosome volume is given by $V_{i}(t)=n_{i}(t)\deltav$, where $\deltav$ is the effective volume occupied by a single subunit. As shown before (Zwicker et al., 2014), this model can capture the essential quantitative features of the growth of a single centrosome (Figure 1C), including sigmoidal growth curve, temporal control of size and scaling of centrosome size with cell size. However, this model is unable to ensure the size equality of two identical centrosomes growing from a shared subunit pool. Stochastic simulation of this model, using the Gillespie algorithm (see Materials and methods), shows a significant difference in steady-state size even with a small initial size difference (Figure 1C).

It is instructive to first compare two opposite limits of the model, $k_{0}^{+}=0$ (purely autocatalytic growth) and $k_{1}^{+}=0$ (non-cooperative growth). For $k_{0}^{+}=0$, Equation 1 can be interpreted as assembly and disassembly occurring throughout the PCM volume, with the assembly rate scaling with centrosome size. As a result, the centrosome with a larger initial size would end up growing to a larger steady-state size. Stochastic simulations of this model show that the ensemble-averaged absolute difference in centrosome size ($|\deltaV|=|V_{1}−V_{2}|$) increases with the initial centrosome size difference $(\deltaV_{0})$, indicating lack of robustness in size regulation (see Appendix 1 and Figure 2—figure supplement 1). On the other hand, the limit $k_{1}^{+}=0$ corresponds to a model where the assembly rate is size-independent, and material turnover is distributed throughout the PCM volume. This model guarantees size equality of a centrosome pair competing for a limiting subunit pool (see Appendix 1 and Figure 2—figure supplement 2), even in the presence of large initial size differences (Figure 2D), with the steady-state size given by $V=k^{+}N\deltav/(k^{−}+2k^{+})$. However, the resulting growth curve is non-sigmoidal, thus fails to capture experimental data in C. elegans (Decker et al., 2011; Zwicker et al., 2014).

![Figure 2.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig2-v1.jpg)

**Figure 2.:** (A) The relative difference in centrosome size, $|\delta⁢V|/⟨V⟩$, as a function of the growth rate constants $k_{0}^{+}$ and $k_{1}^{+}$, with an initial size difference of $0.1⁢\mu⁢m^{3}$. The light gray and dashed black lines represent the lines $|\delta⁢V|/⟨V⟩=0.2$ and $|\delta⁢V|/⟨V⟩=1.0$. (B,C) Size dynamics of a pair centrosomes for (B) weakly cooperative ($k_{0}^{+}=100$, $k_{1}^{+}=0.001$) and (C) strongly cooperative ($k_{0}^{+}=0.1$, $k_{1}^{+}=0.001$) growth regimes. (D) Dynamics of centrosome size for a single centrosome and a pair of centrosomes simulated using the non-cooperative growth model. Inset: Schematic of centrosome growth via centriole-localized assembly and disassembly distributed throughout the PCM. The $|\delta⁢V|/⟨V⟩$ values in (A) represent an average over 1000 ensembles. The values of $k_{0}^{+}$ and $k_{1}^{+}$ are in the units of $\times600⁢\mu⁢M^{-1}⁢s^{-1}$. See Table 1 for a list of parameter values. Parameter values for panel D were chosen to obtain typical steady-state centrosome size (∼ 5 μm3) and timescale of growth (∼ 500 s).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) A model of autocatalytic growth of a single centrosome from a limited pool of subunits exhibits robust size control and sigmoidal growth. For a pair of centrosomes, this model leads to size inequality of the two centrosomes. (B) Phase portrait analysis shows completely overlapping nullclines (in thick gray and dotted black lines), creating a line attractor on which every point is a valid solution for the ODE system. The orange and green trajectories, obtained from stochastic growth simulations, show the extent of size inequality. The black dot indicates the equal size point ($V_{1}=V_{2}$, but not a fixed point here). (C) Size difference between the two centrosomes ($|\delta⁢V|$) increases with increasing initial size difference $\delta⁢V_{0}$ (i.e. two centrosomes have initial sizes $V_{0}+\delta⁢V_{0}$ and $V_{0}$). The result presented in terms of the relative quantities $\frac{|\delta⁢V|}{⟨V⟩}$ and $\frac{\delta⁢V_{0}}{V_{0}}$, shows lack of robustness in size regulation. The parameters for purely autocatalytic growth are: $k^{+}=2⁢\mu⁢M^{-1}⁢s^{-1}$, $ρ_{0}=0.0108⁢\mu⁢M$. All other parameters are the same as the fixed parameters listed in Table 1.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A–B) Size dynamics for a centrosome pair shows strong suppression of initial size difference and robust control of centrosome size. (inset) The dynamics of $\delta⁢V$ shows monotonic decay towards small $\delta⁢V$ value. (C) Size dynamics plotted on the phase portrait, obtained from an equivalent deterministic description, shows the corresponding evolution of the two cases presented in panels A (orange) and B (green), respectively. The black and red lines indicate the nullclines $V˙_{1}=0$ and $V˙_{2}=0$, respectively. Probability distribution of size deviation from the mean size $V-⟨V⟩$. (inset) Probability distribution of size $P⁢(V_{1})$ and $P⁢(V_{2})$. These quantities demonstrate that $\delta⁢V$ in this case originates from the stochasticity in the size dynamics and it is independent of the initial size difference. Parameters: $k^{+}=1000⁢\mu⁢M^{-1}⁢s^{-1}$, $ρ_{0}=0.1⁢\mu⁢M$. All other parameters are the same as the fixed parameters listed in Table 1.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** (A–F) Phase portrait from deterministic growth description and growth dynamics from stochastic simulations show the resulting centrosome size inequality during autocatalytic growth. (A,C,E) The phase portrait plot shows the nullclines $V˙_{1}=0$ and $V˙_{2}=0$ in thick gray and black dotted lines, respectively, and the growth trajectory from stochastic simulation is shown in orange. (B,D,F) The size dynamics from stochastic simulations show decreasing size inequality and decreasing sigmoidal growth with increasing non-cooperative growth rate $k_{0}^{+}$. (G–I) Relative size inequality measured by $|\delta⁢V|/⟨V⟩$ as a function of the non-cooperative growth rate ($k_{0}^{+}$) and the cooperative growth rate ($k_{1}^{+}$). The parameter values for $k_{0}^{+}$ and $k_{1}^{+}$ are expressed in the units of $\times600⁢\mu⁢M^{-1}⁢s^{-1}$. Here $ρ_{0}=0.033⁢\mu⁢M$ and all other parameters are the same as the fixed parameters listed in Table 1.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig2-figsupp4-v1.jpg)

**Figure 2—figure supplement 4.:** (A) Schematic of reaction-diffusion simulation showing the two centrosomes that are $\delta⁢R$ distance apart in the 3D simulation volume. (B) Centrosome volume during autocatalytic growth for two different diffusion constant values. Solid and dashed lines indicate the volume curves for the centrosome pair. (C) Centrosome size inequality, $\frac{|\delta⁢V|}{⟨V⟩}$, increases with increasing separation ($\delta⁢R$) for different diffusion constants (indicated in different colours). The dashed line indicates 2% inequality, that is $\frac{|\delta⁢V|}{⟨V⟩}=0.02$. (D) Centrosome size inequality as a function of separation distance $\delta⁢R$. Size inequality increases with increasing initial size difference (indicated in different colours). The parameter values are $k_{0}^{+}=10^{-3}⁢\mu⁢M^{-1}⁢s^{-1}$ and $k_{1}^{+}=10^{-1}⁢\mu⁢M^{-1}⁢s^{-1}$, $ρ_{0}=0.017⁢\mu⁢M$, $V_{c}=729⁢\mu⁢m^{3}$ and all other parameters are the same as the fixed parameters listed in Table 1. We have chosen a smaller system size and a smaller pool size to reduce the computational cost.

To quantify the robustness of size control, we measured the relative difference in steady-state centrosome size, $|\deltaV|/⟨V⟩$, starting with an initial size difference $\deltaV_{0}∼0.01⟨V⟩$, where $|...|$ denotes the absolute value and $⟨V⟩$ is the ensemble average of centrosome size at steady-state. For a robust size regulation mechanism, the final size difference is expected to be independent of the initial size difference. The resulting size inequality is controlled by the rate constants  $k_{0}^{+}$, $k_{1}^{+}$, $k^{−}$ and the pool size N. Our analysis shows that there is a relatively small region of the parameter space where the strength of the autocatalytic feedback is low enough to ensure a small difference in centrosome size (Figure 2A). Through linearization of the rate equations, we derive the analytical condition for size equality to be $2k_{0}^{+}+k^{−}V_{c}>k_{1}^{+}N$ (see Appendix 3 for details). However, in this range of parameter values, the growth is essentially non-cooperative and the growth curve is not sigmoidal (Figure 2B). Larger size inequality is associated with higher values of $k_{1}^{+}$, when the growth dynamics is sigmoidal in nature (Figure 2C). For a detailed study of the lack of robustness in size regulation, please refer to Appendix 1 and Figure 2—figure supplement 3.

While our theoretical estimates suggest that centrosome growth is primarily reaction-limited, the increasing distance between centrosomes during maturation — especially in certain organisms or depending on cell size—could lead to a diffusion-limited growth scenario. To investigate how diffusion affects centrosome size regulation, we extended our model to include subunit diffusion (see Appendix 4). Our results indicate that diffusion does not qualitatively alter centrosome size regulation. Size inequality can be reduced when the diffusion constant is low or when centrosomes are far apart, though in this regime, the growth curves lose their characteristic sigmoidal shape (see Appendix 4 and Figure 2—figure supplement 4). Crucially, the presence of diffusion does not resolve the issue of robustness in size control; the size difference between centrosomes still increases with larger initial size disparities (Figure 2—figure supplement 4).

### Catalytic growth in a shared enzyme pool ensures centrosome size equality and cooperative growth

#### Model motivation and assumptions

Centrosome growth during maturation occurs through the expansion of a scaffold-like structure and subsequent recruitment of PCM proteins on the scaffold. While multiple proteins are involved in the scaffold assembly, Spd-2 and centrosomin (Cnn) are two essential scaffold-forming proteins identified in Drosophila, in the absence of which centrosome growth is almost entirely diminished (Conduit et al., 2014a). The kinase Polo interacts with both Spd-2 and Cnn to promote the assembly of a stable scaffold. In particular, Spd-2 recruits Cnn with the help of Polo and Cnn in turn strengthens the Spd-2 scaffold without directly recruiting additional Spd-2 proteins. Without the Polo kinase, the Cnn scaffold fails to grow (Alvarez Rodrigo et al., 2019). Similar molecular pathways exist in other organsisms like C. elegans, involving homologous proteins (Raff, 2019). These findings suggest a model for catalytic assembly of centrosomes based on positive feedback between scaffold-forming proteins and an enzyme. Moreover, Fluorescent Recovery After Photobleaching (FRAP) data reveal that the turnover rate of the enzyme Polo kinase within PCM is much faster (∼ 1 min) compared to the Spd-2 and Cnn (∼ 10 min; Alvarez Rodrigo et al., 2019; Wong et al., 2022). Consequently, owing to the enzyme’s pronounced diffusivity, there is a strong likelihood that the active enzyme pool is shared between the two centrosomes.

To determine whether a shared catalytic growth model can yield size parity in a pair of centrosomes, we initially formulated a single-component model for PCM growth, catalyzed by an enzyme (Figure 3A). This model takes into account a shared limiting pool of enzyme and PCM subunits. The assumption of a limiting subunit pool is supported by prior research on C. elegans, which displayed centrosome size scaling with centrosome number (Decker et al., 2011). While the presence of such a limited subunit pool has not been established in other systems, we will subsequently demonstrate that even in cases where centrosome size scaling is not pronounced, the subunit pool can still be finite. Consequently, we implement a model with a limiting pool for both subunits and enzymes. We later relax this assumption by exploring the implications of an infinite enzyme pool.

![Figure 3.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig3-v1.jpg)

**Figure 3.:** (A) Schematic of centrosome growth via catalytic activity of an enzyme that is activated by PCM proteins at a rate proportional to PCM size. (B) Reactions describing centrosome growth via catalytic activity of enzyme $E$. The centrosome ($S_{n}$) can activate the enzyme in a state $E^{*}$, which in turn creates an activated subunit ($S_{1}^{*}$) that binds the PCM. (C) Size dynamics of a centrosome pair (blue, red curves) growing via catalytic assembly and the dynamics of the activated enzyme ([$E^{*}$]) in time (blue curve). (D) The ensemble average of relative absolute size difference $|\delta⁢V|/⟨V⟩$ is insensitive to change in relative initial size difference $\delta⁢V_{0}/V_{0}$. Inset: Probability distribution of $\delta⁢V$ for two different values of initial size difference ($\delta⁢V_{0}/V_{0}=0.1$ and $\delta⁢V_{0}/V_{0}=0.4$). (E) Centrosome growth curves obtained from the catalytic growth model (lines) fitted to experimental growth curves (points) measured at different stages of C. elegans development. (F) Degree of sigmoidal growth, measured by Hill coefficient $\alpha$, as a function of the growth rate constant $k^{+}$ and the total enzyme concentration [$E$]. (G) Model of shared catalysis considering a constant concentration of inactive enzyme ($E$) throughout the growth period. Inset: Schematic of the reactions showing the steady state cycle between $S_{1}$, $S_{1}^{*}$ and $S_{n}$. (H) Centrosome pair growth in the presence of unlimited inactive enzyme pool exhibits size equality as well as cooperative growth dynamics. Inset: Dynamics of $S_{1}$ and $S_{1}^{*}$ concentrations. See Table 1 for a list of parameter values. Parameters were chosen to match typical steady-state centrosome size (∼ 5 μm3) and the timescale of growth (∼ 500 S). Parameters for panel E were obtained by fitting the enzyme kinetics.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Dynamics of $S_{1}^{*}$ and $E^{*}$ show the decay of $E^{*}$ pulse in the wake of the $S_{1}^{*}$ production from $E^{*}$ and $S_{1}$. (B–C) The features of the active enzyme pulse ($E^{*}$ dynamics) can be modulated by changing the rates of enzyme activation ($k_{E}^{*}$) and subunit activation ($k_{1}^{*}$). (C) The centrosome growth rate (deduced from $S_{n}⁢(t)$) changes with parameters regulating the pulse dynamics. The growth rate is reduced for a weaker pulse with a smaller amplitude and larger time period. The parameter values are the same as in Figure 3C and $k_{E}^{*}/k_{1}^{*}$ values are obtained by changing $k_{E}^{*}$ values.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (A–B) Centrosome size inequality ($\frac{|\deltaV|}{⟨V⟩}$) as a function of the initial size difference ($\frac{\deltaV_{0}}{V_{0}}$), for different concentrations of the subunit pool. $\frac{|\deltaV|}{⟨V⟩}$ does not change with the increasing subunit pool size in autocatalytic growth model (A), while it decreases in the catalytic growth model (B). (C) Centrosome size difference ($\delta⁢V$) in the autocatalytic growth model is positively correlated with the initial size difference ($\delta⁢V_{0}$), with a Pearson correlation coefficient $R=0.45$. (D) Centrosome size difference ($\delta⁢V$) in the catalytic growth model is uncorrelated with the initial size difference ($\delta⁢V_{0}$) with Pearson correlation coefficient $R∼0$. The dashed lines in the panels C and D are obtained by linear fit as a guide to the eye. The parameter values for panels A and C are the same as in Figure 2C and the parameter values for panels B and D are the same as in Figure 3D.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** (A) Size dynamics of centrosome pairs (dashed and solid lines) in the catalytic growth for different values of subunit diffusion constant (indicated by colour). The distance between the centrosomes is taken to be fixed at $\deltaR=2\mum$. (B) Size dynamics of centrosome pairs (dashed and solid lines) in the catalytic growth model for different values of centrosome separation distance (indicated by colour). The subunit diffusion constant is taken to be fixed at $10\mum^{2}/s$. (C) Centrosome growth curves with different values of initial size difference shows no significant effect on the final size difference. The parameter values used are $ρ_{0}=0.016\muM$, $[E]=0.006\muM$, $V_{c}=729\mum^{3}$ and $k^{+}=1\muM^{−1}s^{−1}$ and other parameters are the same as in Figure 3B.

#### Model description

In the single-component model for PCM growth, PCM is composed of a single type of subunit that can either take an inactive form ($S_{1}$), or an enzyme-dependent active form ($S_{1}^{∗}$), with $S_{n}$ representing a centrosome with $n$ subunits. The single coarse-grained subunit ($S_{1}$) represents a composite of the scaffold-forming proteins (e.g. Spd-2 and Cnn in Drosophila), and the enzyme ($E$) represents the kinase (e.g. Polo in Drosophila). The inactive subunit can slowly bind and unbind from the PCM, while the enzyme-activated form can assemble faster (reactions 1 and 2 in Figure 3B). The subunit activation is carried out by the active form of the enzyme ($E^{∗}$). Enzyme activation occurs in the PCM, and is thus centrosome size-dependent (reactions 3 and 4 in Figure 3B). A centrosome with a larger PCM thus produces active enzymes at a faster rate, and an increased amount of activated enzymes enhance centrosome growth. Thus, size-dependent enzyme activation generates a positive feedback in growth, which is shared between the centrosomes as the enzymes activated by each centrosome become part of the shared enzyme pool. This is in contrast to the autocatalytic growth model where the size-dependent positive feedback was exclusive to each centrosome.

A deterministic description for the growth of a single centrosome in a cell of volume $V_{c}$ is given by the coupled dynamics of centrosome size ($S_{n}$, number of incorporated subunits), the abundance of available active subunits ($S_{1}^{∗}$) and the abundance of activated enzymes ($E^{∗}$):

$$
\frac{dS_{n}}{dt}=\frac{k^{+}}{V_{c}}S_{1}+\frac{k^{∗}}{V_{c}}S_{1}^{∗}−k^{−}S_{n},
$$



$$
\frac{dS_{1}^{∗}}{dt}=\frac{k_{1}^{∗}}{V_{c}}S_{1}E^{∗}−\frac{k^{∗}}{V_{c}}S_{1}^{∗},
$$



$$
\frac{dE^{∗}}{dt}=\frac{k_{E}^{∗}}{V_{c}}S_{n}E−\frac{k_{1}^{∗}}{V_{c}}S_{1}E^{∗},
$$

where $k^{+}$ and $k^{∗}$ are the assembly rates for inactive and active form of the subunit, and $k^{-}$ is the disassembly rate. Here, $k^{+}$ represents the centriolar activity that can be different for the two centrosomes. The rates for PCM-dependent enzyme activation and enzyme-dependent subunit activation are given by $k_{E}^{∗}$ and $k_{1}^{∗}$ (Figure 3B). The condition for limiting component pool is imposed by substituting $S_{1}$ and $E$ with the constraints: $S_{1}=N−S_{n}−S_{1}^{∗}$, $E=N_{E}−E^{∗}−S_{1}^{∗}$, where $N$ and $N_{E}$ are the total amounts of subunits and enzymes, respectively.

#### Model results and predictions

Using the above-described dynamics (Equations 2–4 and Figure 3B), we performed stochastic simulations of a pair of centrosomes growing from a shared pool of enzymes and subunits. The resulting growth dynamics is sigmoidal, and lead to equally sized centrosomes (Figure 3C). Interestingly, the dynamics of the activated enzyme show an activation pulse at the onset of growth (Figure 3C). This pulse in the cytoplasmic concentration of active enzymes arises from the dynamics of enzyme activation by the PCM scaffold and its subsequent consumption by PCM subunits. The amplitude and the lifetime of the pulse depend on the difference in the timescales of enzyme activation and consumption (Figure 3—figure supplement 1). Notably, a pulse of centriolar Polo kinase density has been observed to initiate centrosome assembly in Drosophila (Wong et al., 2022). However, as we discuss later, further experiments are required to draw a direct correspondence between the centriolar Polo pulse and the pulse we observe here in the cytosolic active enzyme concentration. The experimentally observed Polo pulse is regulated by the abundance of the centriolar protein Ana1 (Wong et al., 2022), which controls the enzyme activation rate ($k_{E}^{∗}$ in our model). Exploring the effect of the enzyme activation rate $k_{E}^{∗}$, we observe increased pulse period and decreased pulse amplitude with decreasing enzyme activation rate (Figure 3—figure supplement 1). These results are similar to the experimentally observed effect of reduced Ana1, which reduces the overall rate of Polo activation in the centrosome (Wong et al., 2022).

Importantly, this model ensures robustness in centrosome size equality, with a negligible difference in steady-state size (∼ 2% of mean size) that is independent of the initial size difference (Figure 3D). A linear stability analysis of the growth equations shows that the size difference between centrosomes decays exponentially, independent of the dynamics of subunit activation and enzyme activation (see Appendix 3 for details). The difference in steady-state size is a result of the fluctuations in the individual centrosome size dynamics, as evident from the distribution of the size difference (Figure 3D - inset). To further quantify the robustness in size regulation, we performed a statistical test by evaluating the Pearson correlation constant between the initial size difference and the final size difference and find them to be uncorrelated (Figure 3—figure supplement 2). We find that the centrosome growth dynamics predicted by this model match really well with the experimental growth curves in C. elegans (Decker et al., 2011; Figure 3E).

Although centrosome growth in C. elegans is found to be sigmoidal, it has been suggested that centrosomes in Drosophila grow in a non-sigmoidal fashion (Zwicker et al., 2014). Although we could not find any direct quantitative measurement of centrosome size dynamics in Drosophila or other organisms, analysis of PCM assembly dynamics using fluorescence reporters show varying degrees of cooperativity during Drosophila development (Wong et al., 2022). We therefore sought to explore whether our catalytic growth model can also describe non-sigmoidal growth. To this end, we characterized the sigmoidal nature of the growth by fitting the dynamics of centrosome volume $V(t)$ to a Hill function of the form $At^{\alpha}/(B^{\alpha}+t^{\alpha})$, where the coefficient α represents the strength of cooperativity. Our results show that the cooperative nature of growth depends on the interplay between the growth rate constant $k^{+}$ and the total enzyme concentration [$E$], such that growth is sigmoidal ($\alpha\geq2$) for larger [$E$] and smaller $k^{+}$, and non-sigmoidal otherwise (Figure 3F).

While our model of shared catalysis considers a limiting pool of enzymes, a finite enzyme pool is not required for robust size control. To show this, we considered an unlimited pool of inactive enzymes ($E$), such that the cytoplasmic concentration of $E$ does not change over time (Figure 3G). The unlimited pool of inactive enzymes keeps producing activated enzymes via the centrosomes. The centrosome size reaches a steady-state when the subunit activation (via $E^{*}$) and subsequent growth is balanced by subunit disassembly from the centrosome (Figure 3G - inset). The size equality and cooperativity of growth remain intact in the presence of constant [$E$] (Figure 3H). The prevalence of activated enzyme almost entirely depletes the inactive subunit pool and the centrosomes are in chemical equilibrium with the active subunit pool in the steady state (Figure 3H - inset).

Distinguishing between the autocatalytic and catalytic growth models from experimental data is not trivial as the qualitative features of growth and size scaling behaviors for a single centrosome are the same in both models. We find that the two models can be differentiated by measuring the correlation of the initial size difference with the final size difference of centrosome pairs. They are strongly correlated in the autocatalytic growth model with the sigmoidal growth curve but uncorrelated in the catalytic growth model (Figure 3—figure supplement 2C-D). The final size difference increases with decreasing the subunit pool size in catalytic growth model while no such relation was found in autocatalytic growth model (Figure 3—figure supplement 2A-B).

Finally, we extended our analysis beyond reaction-limited growth to examine how subunit diffusion affects catalytic centrosome growth, utilizing our spatially extended model. Our findings indicate that centrosome size equality, as predicted by the catalytic growth model, remains largely unaffected by variations in the diffusion constant or the separation distance between centrosomes (Figure 3—figure supplement 3).

### Cytoplasmic pool depletion regulates centrosome size scaling with cell size

Since our model for centrosome growth is limited by a finite amount of subunits, it is capable of capturing centrosome size scaling with cell size (Figure 4A), in excellent agreement with experimental data (Decker et al., 2011; Zwicker et al., 2014). However, the extent of organelle size scaling with cell size depends on the assembly rate and becomes negligible when the assembly rate is not significantly higher compared to the disassembly rate (Figure 4B). In particular, centrosome size scaling is connected to the extent of subunit pool depletion, such that the steady-state cytoplasmic fraction of the subunits is low when centrosome size scales with the cell size and higher otherwise (Figure 4C).

![Figure 4.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig4-v1.jpg)

**Figure 4.:** (A) Scaling of centrosome size with cell size obtained from the catalytic growth model (line) fitted to experimental data (points) in C. elegans embryo (Zwicker et al., 2014). (B) Centrosome size does not scale with cell size when the assembly rates are much lower compared to disassembly rate (i.e., $k^{∗},k^{+}≲k^{−}V_{c}$). (C) Dynamics of the cytoplasmic fraction of subunits ($S_{1}$ and $S_{1}^{*}$ combined) reveal significantly higher pool depletion in the size scaling regimes. The two curves correspond to the growth curves shown in panels A (blue) and B (black). The dashed lines are theoretical results obtained from the deterministic model. (D) An analytically obtained phase diagram of centrosome size scaling as functions of enzyme-dependent and enzyme-independent assembly rate constants. The color indicates the strength of size scaling (measured by $d⁢V/d⁢V_{c}$). The dashed gray line indicates the contour $d⁢V/d⁢V_{c}=0.1$. Here the slope values are shown in $\delta⁢v$ units. Insets: Characteristic size scaling behaviours. See Table 1 for a list of parameter values. Parameters for panel B were obtained by tuning enzyme-dependent assembly rate and parameters for panel D were similar to panel A.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) A phase diagram of centrosome size scaling, measured by the slope $d⁢V/d⁢V_{c}$, as functions of assembly rate $k^{*}$ and cell (system) size $V_{c}$. The phase diagrams shows weaker size scaling for smaller assembly rate and larger system size. The values of the slope are expressed in units of $\delta⁢v$. (B) A phase diagram of subunit pool depletion, measured by the cytoplasmic fraction of subunits ($f_{c}$), as functionsof $k^{+}$ and.$k^{*}$ (C–D) Model predictions for cytoplasmic fraction of subunits, as functons of $V_{c}$ and $M$ (organelle number), for parameters corresponding to C. elegans and Drosophila. The black arrows indicate the direction of embryonic development. Inset: Centrosome size scaling with centrosome number as the development progresses. The parameter values for A&B are same as used in main text Figure 4D with $k^{+}=1⁢\mu⁢M^{-1}⁢s^{-1}$ in A. Parameter values for C are:,$ρ_{0}=0.01⁢\mu⁢M$,$E^{*}=0.01⁢\mu⁢M$,$k^{+}=1⁢\mu⁢M^{-1}⁢s^{-1}$ $k^{*}=5000⁢\mu⁢M^{-1}⁢s^{-1}$ and.$k_{1}^{*}=100⁢\mu⁢M^{-1}⁢s^{-1}$ Parameter values for D are same as C except $ρ_{0}=0.03⁢\mu⁢M$ and.$k^{*}=100⁢\mu⁢M^{-1}⁢s^{-1}$ The inset results in C and D are obtained at cell volume $V_{c}=20000⁢\mu⁢m^{3}$ and $V_{c}=10^{6}⁢\mu⁢m^{3}$ respectively. All other parameters are the same as the fixed parameters listed in Table 1.

To understand how size scaling is regulated by the growth parameters, we derived a simplified analytical form (see Appendix 2) for the steady-state centrosome size given by

$$
V=\frac{(E^{∗}k_{1}^{∗}+k^{+})k^{∗}ρ_{0}V_{c}\deltav}{k^{∗}(k^{+}+k^{−}V_{c})+E^{∗}k_{1}^{∗}(k^{∗}+k^{−}V_{c})},
$$

where $\delta⁢v$ is the volume occupied by a centrosome subunit, $ρ_{0}$ is the total subunit density, and the enzymes are assumed to reach their steady-state abundance $E^{*}$ very fast. From the above expression, we can see that centrosome size $V$ will strongly scale with cell size $V_{c}$ when $k^{+},k^{*}≫k^{-}⁢V_{c}$. This result is reflected in the phase diagram of size scaling (measured as the slope $∼d⁢V/d⁢V_{c}$), which shows stronger size scaling with increasing assembly rates (Figure 4D). The subunit pool depletion also increases with the assembly rates, reaching a state of almost complete depletion (i.e. $V→ρ_{0}⁢V_{c}⁢\delta⁢v$) as we approach the regime of strong size scaling (see Figure 4—figure supplement 1).

It is important to note here that size scaling with cell size reported here is different from the linear size scaling predicted by the canonical limiting pool model (Decker et al., 2011; Goehring and Hyman, 2012). Robust size control for multiple centrosomes requires size-dependent negative feedback and with this feedback, the size scaling with cell size becomes a feature achieved in a range of cell volumes by tuning growth rates. Interestingly, strong size scaling has been observed in C. elegans embryos (Decker et al., 2011), which are smaller in size ($∼10^{4}⁢\mu⁢m^{3}$) than Drosophila embryos ($∼10^{6}⁢\mu⁢m^{3}$) that do not exhibit size scaling with centrosome number (inferred from intensity data in Wong et al., 2022). This feature can be explained by our model in the regime of weaker size scaling, which is expected for larger system sizes (see Appendix 2 and Figure 4—figure supplement 1). Thus, the parameters of our model can be tuned to capture both sigmoidal and non-sigmoidal growth and strong or weak size scaling, without changing the nature of the molecular interactions that are largely conserved across organisms (Raff, 2019).

### Control of centrosome size asymmetry through differential growth

An essential aspect of centrosome size regulation is the modulation of centrosome size by centriole activity. In particular, it has been shown that the centrosome associated with a more active centriole will grow larger, resulting in centrosomes of unequal size (Januschke et al., 2013; Conduit and Raff, 2010b). Control of centriole activity-driven centrosome size asymmetry is important as this size asymmetry may play a crucial role in stem cell division as observed in Drosophila neuroblasts (Conduit and Raff, 2010b). We test the effectiveness of size regulation by studying the growth of a centrosome pair with different centriole activities, controlled by the values of the growth rate constants $k_{0}^{+}$ and $k^{+}$ for the autocatalytic (Equation 1) and the catalytic (Figure 3B) growth models, respectively (Figure 5A). For both the models, we bias the initial size of the centrosomes by assigning a smaller initial size ($V_{0}-\delta⁢V_{0}$) to the centrosome with a higher centriole activity (i.e., $k_{0}^{+(1)}=k_{0}^{+}+\delta⁢k_{0}^{+}$ or $k^{+(1)}=k^{+}+\delta⁢k^{+}$). We then simulate the growth of $N_{tot}$ centrosome pairs and quantify the efficiency ($\epsilon$) of size control as the ratio of the number of cases ($N^{+}$) where the centrosome with higher growth rate ($k_{0}^{+}+\delta⁢k_{0}^{+}$ or $k^{+}+\delta⁢k^{+}$) becomes larger, to the total number of simulated pairs, $\epsilon=N^{+}/N_{tot}$.

![Figure 5.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig5-v1.jpg)

**Figure 5.:** (A) Schematic illustrating asymmetric size regulation via differential growth in the (top) catalytic growth model and (bottom) autocatalytic growth model. (B,C) Ten representative trajectories showing the dynamics of centrosome size difference ($V_{1}-V_{2}$) for (B) catalytic growth model ($\delta⁢k^{+}/k^{+}=0.2$), and (C) autocatalytic growth model ($\delta⁢k_{0}^{+}/k_{0}^{+}=0.2$). The two centrosomes are initially of the same size. (D) Efficiency growth-rate-dependent control of centrosome size asymmetry ($\epsilon=N^{+}/N_{tot}$) as a function of (normalized) initial size difference ($\delta⁢V_{0}/V_{0}$) and (normalized) growth rate difference ($\delta⁢k^{+}/k^{+}$), in the catalytic growth model. (E) Efficiency of growth-rate-dependent control of centrosome size asymmetry as a function of (normalized) initial size difference ($\delta⁢V_{0}/V_{0}$) and (normalized) growth rate difference ($\delta⁢k_{0}^{+}/k_{0}^{+}$), in the autocatalytic growth model. See Table 1 for a list of model parameters. Parameter values for panels B and D were chosen to obtain typical steady-state centrosome size (∼ 5 μm3) and timescale of growth (∼ 500 S).

In the absence of any initial size difference ($\deltaV_{0}=0$), the catalytic growth model shows better control of differential growth-induced size asymmetry (Figure 5B), while the autocatalytic growth model shows wide variations in centrosome size difference (Figure 5C). We find that the catalytic growth model ensures that the centrosome with a larger $k^{+}$ (higher centriole activity) end up being larger, irrespective of the initial size difference (Figure 5D). This illustrates robust control of centrosome size asymmetry by controlling differences in centriole activity. By contrast, in the autocatalytic growth model, the efficiency of size control monotonically decreases with increasing initial size difference, reflecting the lack of robustness in size control (Figure 5E).

### Multi-component centrosome model reveals the utility of shared catalysis on centrosome size control

One major postulate of the one-component PCM model was that the enzyme pool was shared between the two centrosomes rather than being localized to each. Here, we support this assumption using a more realistic multi-component centrosome model that allows us to model the specific interactions between the enzyme and the centrosome components, making it possible to study the relative dynamics of the two main scaffold formers. While we draw parallels between this model and the interactions observed in Drosophila, the model should be relevant to other organisms where similar pathways are in action via functionally similar proteins.

Based on recent studies (Alvarez Rodrigo et al., 2019; Conduit et al., 2015b), we model the centrosomes with two essential scaffold-forming proteins, $a$ and $b$, whose assembly into the PCM scaffold is regulated by the kinase $E$. The total size of the PCM scaffold, $S$, and the centrosome volume $V$ are given by $S=S⁢(a)+S⁢(b)$ and $V=V_{a}+V_{b}$, where $S⁢(a)$ ($S⁢(b)$) and $V_{a}$ ($V_{b}$) denote the contribution to the scaffold size (in number of subunits) and the centrosome volume by the component $a$ ($b$). The molecular identities of these key components are listed in Table 2 for different organisms. In particular, for Drosophila, $a$ and $b$ can be identified as the scaffold forming proteins Spd-2 and Cnn, while $E$ represents the kinase Polo. It has been observed that Spd-2 and Cnn cooperatively form the PCM scaffold to recruit almost all other proteins involved in centrosome maturation (Conduit et al., 2014b). To effectively coordinate cooperative growth of the scaffold, Spd-2 proteins recruit the kinase Polo, which in turn phosphorylates Cnn at the centrosome (Alvarez Rodrigo et al., 2019). In the absence of Polo, Cnn proteins can bind to the scaffold but fall off rapidly, leading to diminished centrosome maturation (Alvarez Rodrigo et al., 2019; Woodruff et al., 2015).

**Table 2.**
 Two-component growth model across organisms.


<table>
  <thead>
    <tr>
      <th>Organism</th>
      <th>Component a</th>
      <th>Component b</th>
      <th>Enzyme E</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Fly</td>
      <td>DSpd-2/Spd-2</td>
      <td>Cnn</td>
      <td>Polo</td>
      <td>Conduit et al., 2014b; Feng et al., 2017</td>
    </tr>
    <tr>
      <td>Worm</td>
      <td>SPD-2</td>
      <td>SPD-5</td>
      <td>PLK-1</td>
      <td>Woodruff et al., 2015; Wueseke et al., 2016</td>
    </tr>
    <tr>
      <td>Xenopus, Zebrafish and Mammals</td>
      <td>Cep192 or Pericentrin</td>
      <td>Cdk5Rap2/Cep215</td>
      <td>Plk1</td>
      <td>Gomez-Ferreria et al., 2007; Fong et al., 2008; Lane and Nigg, 1996; Lee and Rhee, 2011; Doxsey et al., 1994; Aljiboury and Hehnly, 2023</td>
    </tr>
  </tbody>
</table>

We incorporated these experimental observations in our multi-component model as described in Figure 6A. We then test two different models for enzyme spatial distribution: (i) enzyme $E$ (Polo) is activated at each centrosome by the scaffold component $a$ (Spd-2), which then assembles the second component $b$ (Cnn) into the scaffold of that particular centrosome (for details see Appendix 5), and (ii) enzyme $E$ activated by the scaffold component $a$ is released in the cytoplasmic pool, promoting assembly of the $b$-scaffold at both centrosomes (for details see Appendix 5). In the first case, localized enzyme interaction exclusively enhances the growth of the individual centrosomes, creating an autocatalytic feedback that leads to size inequality of centrosomes (Figure 6B). Similar to model (Equation 1), the steady-state size difference between the two centrosomes increases with the increasing initial size difference, resulting in a failure of robust size control (Figure 6—figure supplement 1).

![Figure 6.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig6-v1.jpg)

**Figure 6.:** (A) Schematic of centrosome growth model driven by two scaffold components $a$ and $b$, and enzyme E. $a$ can bind the existing PCM independent of $b$ or the enzyme $E$. The enzyme is activated by $a$ in the scaffold, then released in the cytoplasm as $E^{*}$. The other scaffold former $b$ binds to PCM in $a$-dependent manner in an intermediate form $b_{i}$ which can undergo rapid disassembly. The intermediate form $b_{i}$ can get incorporated in the $b$-scaffold by the active enzyme $E^{*}$ via forming an activated subunit form $E^{*}⁢b_{i}$. The red arrows indicate the size-dependent positive feedback and the green arrow indicates the catalytic activity of the enzyme. (B) Centrosome size ($V_{1},V_{2}$) dynamics for growth with localized enzyme. (C) Centrosome size ($V_{1},V_{2}$) dynamics for growth with shared enzyme pool (black and red curve) and the pulse-like dynamics of activated enzyme concentration ([$E^{*}$], blue curve). (D) Radial spread of the two scaffold former components $a$ and $b$ corresponding to the centrosome growth shown in panel-C. See Table 1 for a list of parameter values. Parameter values for panel B & D were chosen to obtain typical steady-state centrosome size (∼ 5 μm3) and timescale of growth (∼ 500 s).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (A) The panel lists all the reactions used to simulate the growth of centrosomes consisting of two scaffolds $S_{n}⁢(a)$ and $S_{n}⁢(b)$. The $a$-scaffold grows independently of $b$ and $E$ with centriole-dependent assembly and disassembly throughout the PCM volume (Reaction. 1). The second scaffold former $b$ can bind to the $a$-scaffold in a size-dependent manner to form an intermediate $b_{i}$ (Reaction. 2) that can disassemble fast from the scaffold ($k_{b⁢0}^{-}≫k_{b⁢0}^{+}$). The enzyme gets activated by the $a$-scaffold and can activate the intermediate form $b_{i}$, which can then assemble into the $b$-scaffold and increase the amount of $S_{n}⁢(b)$ (Reaction. 3 – 5). The $b$-scaffold can disassemble at a rate $k_{b⁢1}^{-}$ (Reaction. 6). The reactions above describe the growth of centrosome-1 as it is indicated as $S_{n}^{i}⁢(a)$ with i = 1. A similar set of reactions will govern the other centrosome too with all the rate constants being the same. (B) Time evolution of centrosome size dynamics and active enzyme dynamics. (C) The relative size inequality $|\delta⁢V|/⟨V⟩$ is a monotonically increasing function of the initial size difference $\delta⁢V_{0}/V_{0}$, indicating loss of robust size regulation. See Table 3 and Table 1 for a list of model parameters.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/92203/elife-92203-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** (A) The panel lists all the reactions used to simulate the growth of centrosomes of two scaffolds $S_{n}⁢(a)$ and $S_{n}⁢(b)$, where they share the activated enzyme $E^{*}$. The reactions are the ame as the localized enzyme model, except Reaction. 3 – 4. Here the activated enzyme $E^{*}$ is released in a shared pool rather than being specific to a particular centrosoe. This active enzyme can activate the second scaffold former intermediate $b_{i}$ in any of the two centrosomes. (B) Centrosome size dynamics and active enzyme dynamics show insignificant size inequality but clear sigmoidal trend in growth. The active enzyme concentration exhibits pulse-like dynamics at the beginning of centrosome growth. (C) The relative size inequality $|\delta⁢V|/⟨V⟩$ is very small in value and independent of the initial size difference $\delta⁢V_{0}/V_{0}$, indicating robust regulation of size. (D) Total enzyme concentration [$E$] can effectively control the steady-state size of the centrosome, with increasing [$E$] leading to larger centrosome size. (E) Enzyme kinetics can signal the start and end of centrosome maturation and a continuous activity of enzyme is required to maintain the grown centrosome. We turned the enzyme activity on or off by making $k_{E⁢b}^{+}$ non-zero (zero) to see the effect of enzyme on centrosome growth. See Table 3 and Table 1 for a list of model parameters.

**Table 3.**
 Parameter values for two component growth via enzyme activity.


<table>
  <thead>
    <tr>
      <th>[ρb]=0.25μM</th>
      <th>[ρb]=0.5μM</th>
      <th>[ρb]=0.01μM</th>
      <th>ka+=10μM−1s−1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>kb0+=0.5μM−1s−1</td>
      <td>kb0−=0.01s−1</td>
      <td>kaE+=5×103μM−1s−1</td>
      <td>kEb+=103μM−1s−1</td>
    </tr>
    <tr>
      <td>kb1+=104μM−1s−1</td>
      <td>kb1−=5×10−3s−1</td>
      <td>ka−=5×10−3s−1</td>
      <td></td>
    </tr>
  </tbody>
</table>

We then considered the second case where the enzyme-mediated catalysis is shared between the growing centrosome pair. Experimental observations suggest a dynamic enzyme population around the centrosomes (Mahen et al., 2011; Kishi et al., 2009), with a turnover timescale much smaller than the scaffold forming proteins (Conduit et al., 2014b; Conduit et al., 2015a). These findings point towards the possibility that the enzyme is transiently localized in the centrosome during activation and the active enzyme is then released in the cytoplasmic pool that can enhance the growth of both the centrosomes (Figure 6A). We incorporate this shared catalysis mechanism in the second model where $a$ activates the enzyme to $E^{*}$ which then gets released in the cytoplasm, facilitating $b$-scaffold expansion in both the centrosomes (see Appendix 5 for details). This growth mechanism is able to robustly control centrosome size equality (Figure 6—figure supplement 2), giving rise to the characteristic sigmoidal growth dynamics (Figure 6C), where the first scaffold former $a$ is smaller in amount than the second, enzyme-aided component $b$. This difference in the abundances of $a$ and $b$ proteins, when translated into their respective radial spread from the centrosome center ($R∝V^{1/3}$), bears close resemblance with the relative spread in Spd-2 and Cnn observed in the experiments, where the Cnn spread is twice as large as Spd-2 (Conduit et al., 2014b; Alvarez Rodrigo et al., 2019; Figure 6D). The active enzyme dynamics also resembles the observed pulse in Polo dynamics at the beginning of centrosome maturation (Wong et al., 2022; Figure 6C). Overall, the two-component model provides crucial insights into the role of shared catalytic growth on centrosome size control and lays the theoretical foundation for further investigations into the molecular processes that govern centrosome assembly.

## Discussion

### Autocatalytic feedback drives centrosome size inequality

In this article, we examined quantitative models for centrosome growth via assembly and disassembly of its constituent building blocks to understand how centrosome size is regulated during maturation. Although there is no generally accepted model for centrosome size regulation, previous studies Conduit et al., 2014b; Zwicker et al., 2014; Conduit et al., 2014a; Alvarez Rodrigo et al., 2019; Woodruff et al., 2015; Conduit et al., 2015b have suggested that centrosome assembly is cooperative and driven by a positive feedback mechanism. It has been quantitatively shown that an autocatalytic growth model (Zwicker et al., 2014) captures the cooperative growth dynamics of individual centrosomes as well as their size scaling features. However, as we showed here, autocatalytic growth does not guarantee the size equality of two centrosomes growing from a shared subunit pool. The resultant size inequality increases with the initial size difference between the centrosomes, indicating a lack of robustness in size control. This observation remains valid even within models where autocatalysis is not explicitly invoked, but emerges from positive feedback between PCM components (Alvarez Rodrigo et al., 2019). For instance, the positive feedback between Spd-2 and Cnn within Drosophila centrosomes results in the accumulation of more Cnn where Spd-2 is abundant. This, in turn, amplifies the retention of Spd-2 and binding of Cnn, culminating in a size-dependent positive feedback (akin to autocatalytic feedback) in PCM assembly. Given the current molecular understanding, it remains an open question whether localized assembly around the centriole, driven by autocatalytic feedback, is sufficient to furnish a robust mechanism for centrosome size regulation. It is important to note that the results shown in Zwicker et al., 2014 indicate that the Ostwald ripening can be suppressed by the catalytic activity of the centriole, therefore stabilizing the centrosomes against coarsening by Ostwald ripening. However, if size discrepancy arises from the growth process (e.g. due to autocatalysis) the timescale of relaxation for such discrepancy is unclear from the above-mentioned result. We show that for any appreciable amount of positive feedback, the system cannot achieve equal size in a physiologically relevant timescale (Figure 2—figure supplement 3).

### Model of centrosome pair growth via shared catalysis

Following recent experiments on the molecular mechanisms governing centrosome assembly, we constructed an enzyme-mediated catalytic growth model that not only describes cooperative growth behavior but also ensures robustness in size equality of the two maturing centrosomes. The enzyme Polo-like kinase (PLK1) that coordinates centrosome growth (Conduit et al., 2014a; Woodruff et al., 2015; Ohta et al., 2021; Alvarez Rodrigo et al., 2019), gets phosphorylated in the centrosome and has a much faster turnover rate than the centrosome scaffold forming proteins Spd-2 and Cnn (Conduit et al., 2014b). Experiments (∼ 5 μm2 s-1 Mahen et al., 2011) and theoretical estimates (see Materials and methods) indicate high PLK1 diffusivity such that PLK1 transfer between the centrosome pair (assuming at a distance of ∼ 5 – 10 μm) may occur within a few seconds which is much faster than the timescale of centrosome growth (∼ 1000 s). This indicates that the kinase dynamics is not diffusion-limited, consistent with recent studies reporting negligible gradient in cytoplasmic Polo in C. elegans embryo (Barbieri et al., 2022). These insights led us to hypothesize that the kinase, once activated at the centrosome, could be released into the cytoplasm, becoming part of a shared pool of enzymes. This pool would then catalyze the growth of both centrosomes without any inherent bias. While we theoretically demonstrated that this mechanism of shared catalysis can robustly regulate centrosome size, it is important to acknowledge that the specific predictions concerning enzyme dynamics can only be validated through further experiments.

### Localized catalysis leads to centrosome size disparity

To further explore the role of enzymes in mediating centrosome growth and predict the consequence of an enzyme pool that is not shared equally by the two centrosomes, we extended our single-component model of catalytic growth to a multi-component model. This extended model incorporates the interactions PCM scaffold-forming proteins (Spd-2 and Cnn in Drosophila) and the enzyme Polo kinase. Using this model, we showed that localized catalysis by the enzyme—indicative of an unshared pool—leads to significqnt size differences in the centrosomes. While direct experimental validation of a shared enzyme pool remains outstanding, it is intriguing to consider the findings that a centrosome-anchored Plk1 construct (Plk1-AKAP) induces anomalous centrosome maturation and defective spindle formation (Kishi et al., 2009).

### Enzyme-mediated size control

Our findings reveal that centrosome size increases with increasing enzyme concentration and that centrosome growth is inhibited in the absence of the enzyme (Figure 6—figure supplement 2). Since the activity of the Polo kinase is cell-cycle dependent (Hamanaka et al., 1995; Uchiumi et al., 1997), we further explored the dynamics of centrosome growth with a time-dependent dynamics of the enzyme. We found that centrosome growth can be triggered by switching on the enzyme dynamics and centrosome size was reduced when the enzyme was switched off (Figure 6—figure supplement 2). Importantly, it supported the experimental observation that a continuous Polo activity is required to maintain the PCM scaffold (Mahen et al., 2011; Cabral et al., 2019). Many key features of centrosome growth such as the sigmoidal growth curve and size scaling behavior can be modulated in our model by changing the growth rate constants and enzyme concentration, while conserving the underlying molecular mechanisms for assembly. This opens up the possibility that the catalytic growth model may be broadly relevant to other organisms where homologous proteins (Table 2) play similar functional roles in regulating centrosome growth (Conduit et al., 2015b).

### Testable model predictions

Aside from capturing the existing data on the dynamics of centrosome growth, our catalytic growth model makes specific predictions that can be tested in future experiments. Firstly, our model posits the sharing of the enzyme between the two centrosomes. This can potentially be experimentally tested through immunofluorescent staining of the kinase or by constructing FRET reporter of PLK1 activity (Allen and Zhang, 2006), where it can be studied if the active form of the PLK1 is found in the cytoplasm around the centrosomes indicating a shared pool of active enzyme. Another possible future experiment can be performed based on photoactivated localization microscopy (PALM; Sillibourne et al., 2011) where fluorescently tagged enzyme can be selectively photoactivated in one centrosome and intensity can be measured at the other centrosome to find the extent of enzyme sharing between the centrosomes. It is important to to acknowledge that while we exclusively focused on Polo kinase as the sole enzyme, this shared catalytic activity might also involve other molecular players that interact with Polo, such as cyclin B/Cdk1 (Kishi et al., 2009). Moreover, our model provides explicit predictions regarding the enzyme’s role in influencing centrosome size and growth. These predictions encompass the anticipated increase in centrosome size with increasing enzyme concentration, the ability to modify the shape of the sigmoidal growth curve, and the manipulation of centrosome size scaling patterns by perturbing growth rate constants or enzyme concentrations. Additionally, the model suggests inducing a shift from strong size scaling to weak size scaling through the reduction of PCM assembly rate or via cytoplasmic subunit pool depletion.

Secondly, an implication of our model is the robust regulation of centrosome size through catalytic PCM assembly during maturation. One direct avenue for testing this result is to observe the dynamics of two initially unequal-sized centrosomes during the early maturation phase. The catalytic growth model predicts that the final size difference of the centrosomes is uncorrelated to their initial size disparity while they are strongly correlated according to the autocatalytic growth model (Figure 3—figure supplement 2). The catalytic model also predicts the final size inequality will increase with decreasing subunit pool size. These predictions can be experimentally examined by inducing varying centrosome sizes at the early stage of maturation for different expression levels of the scaffold former proteins. It is important to note here that the initial size difference has to be induced while keeping the centrioles unaffected otherwise it may create size difference due to differences in centriole activity (Januschke et al., 2013; Conduit and Raff, 2010b; Zwicker et al., 2014). Experimentally validating these predictions will play a pivotal role in building a quantitative understanding of centrosome size regulation during mitosis and in clearly distinguishing the catalytic growth mechanism from the autocatalytic growth.

## Materials and methods

### Stochastic growth simulations

We use the Gillespie, 1977 algorithm to simulate the stochastic growth of one or multiple structures from a common pool of subunits. At any time $t$ the Gillespie algorithm uses two random variables drawn from an uniform distribution ($r_{1},r_{2}\in𝒰⁢(0,1)$), and the instantaneous propensities for all of the possible reactions to update the system in time according to the defined growth law. The propensities of the relevant reactions, that is the assembly and disassembly rates of the ith structure are given by $K_{i}^{on}$ and $k_{i}^{off}$, respectively. For example, for the autocatalytic growth model described in Equation 1, these propensities are functions of subunit pool size (N) and structure size (ni),

$$
K_{i}^{on}=(k_{0}^{+}+k_{1}^{+}n_{i})(\frac{N−\sumi=1Mn_{i}}{V}),
$$



$$
K_{i}^{off}=k^{−},
$$

where we are considering growth of M structures from a shared pool. The Gillespie algorithm computes the time for the next reaction at $t+\tau$ given the current state of the system (i.e. the propensities for all reactions) at time $t$ where $\tau$ is given by-

$$
\tau=\frac{1}{\sum_{i=1}^{C}ℛ_{i}}⁢log⁡(\frac{1}{r_{1}}),
$$

where $ℛ_{i}$ is the propensity of $i^{t⁢h}$ reaction and $C$ is the total number of all possible reactions. The second random variable $r_{2}$ is used to select the particular reaction ($j^{t⁢h}$ reaction) that will occur at $t+\tau$ time such that

$$
\frac{\sum_{i=1}^{j-1}ℛ_{i}}{\sum_{i=1}^{C}ℛ_{i}}\leqr_{2}<\frac{\sum_{i=1}^{j}ℛ_{i}}{\sum_{i=1}^{C}ℛ_{i}}.
$$

The condition for the first reaction ($j=1$) is $0\leqr_{2}<\frac{ℛ_{1}}{\sum_{i=1}^{C}ℛ_{i}}$. The two steps defined by Equation 8 and Equation 9 are used recursively to compute the growth dynamics in time.

We used the Gillespie algorithm to find the stochastic trajectories of the above discussed deterministic (mass action kinetics) dynamics of the autocatalytic growth model and its various limits. See Catalytic growth in a shared enzyme pool ensures robust control of centrosome size for the corresponding chemical master equations. Similarly for the catalytic growth and two-component model, we find the stochastic trajectories via the Gillespie algorithm from the reactions given in Figures 3B and 6A.

### Subunit size estimation

Although we use single subunit and two subunit models of growth, we have used same value for the volume occupied by the subunit $\delta⁢v$. We estimate the value of $\delta⁢v$ from the molecular weight of SPD-5 which is 135 kDa (Hamill et al., 2002). Taking the protein mass density to be $1.4⁢gcc^{-1}$(Fischer et al., 2004) and the PCM volume fraction to be ∼ 0.1 (Mahen et al., 2011), we estimate the volume occupied by SPD-5 in PCM to be $0.1\times162\times10^{-7}⁢\mu⁢m^{3}∼2\times10^{-4}⁢\mu⁢m^{3}$.

### Timescale of diffusion

We assume reaction-limited dynamics for centrosome maturation, meaning that the cytosolic diffusion of scaffold-forming proteins and the enzyme is much faster than their reaction rates. Here, we quantitatively discuss the timescales of protein diffusion and reaction based on their mass and fluorescent recovery after photobleaching (FRAP) data. The scaffold-forming proteins have a mass range of 100–150 kDa, while the enzyme mass is approximately 50–70 kDa. Using the Stokes-Einstein relation, which predicts that the diffusion constant scales inversely with protein radius (R), that is D ∼ R-1 ∼ M-1/3 where M is the protein mass, we estimate their diffusion constants. Based on the cytosolic diffusion constant of 30 μm2s-1 for GFP (mass 30 kDa; Milo et al., 2010), we estimate diffusion constants of 17–20 μm2s-1 for the scaffold-forming proteins and about 24 μm2s-1 for the enzyme.

The separation distance between centrosomes (d) during maturation depends on the developmental stage of C. elegans and Drosophila embryos, but in later stages, it ranges between 5 and 10 μm (Decker et al., 2011; Alvarez Rodrigo et al., 2019). Using the diffusion timescale $\tau_{D}=\frac{L^{2}}{6D}$, we estimate diffusion times of about 1 s for scaffold-forming proteins and 0.1–0.5 s for the enzyme. These diffusion times are significantly shorter than the turnover times observed in FRAP experiments, which are around 100 s for scaffold-forming proteins and 10 s for the enzyme in Drosophila (Conduit et al., 2014b; Conduit and Raff, 2010b) and C. elegans (Woodruff et al., 2017). This discrepancy suggests that diffusion of the relevant proteins and enzyme is considerably faster than their reaction rates, supporting the use of a reaction-limited model for studying the self-assembly of the PCM during centrosome maturation. Further experiments to directly measure diffusion constants of these proteins are necessary for a more detailed understanding of the role of diffusion in centrosome size regulation.
