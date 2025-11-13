# Physical constraints and biological regulations underlie universal osmoresponses

## Authors

- Yiyang Ye<sup>1</sup> ([ORCID: 0000-0002-2411-5297](https://orcid.org/0000-0002-2411-5297))
- Qirun Wang<sup>1</sup> ([ORCID: 0000-0001-8845-1997](https://orcid.org/0000-0001-8845-1997))
- Jie Lin<sup>1</sup> ([ORCID: 0000-0002-2027-4661](https://orcid.org/0000-0002-2027-4661)) †

### Affiliations

1. Center for Quantitative Biology, Academy for Advanced Interdisciplinary Sudies, Peking University Beijing China ([ROR:02v51f717](https://ror.org/02v51f717))
2. Peking-Tsinghua Center for Life Sciences, Academy for Advanced Interdisciplinary Sudies, Peking University Beijing China ([ROR:02v51f717](https://ror.org/02v51f717))

† Corresponding author

## Abstract

Microorganisms constantly transition between environments with dramatically different external osmolarities. However, theories of microbial osmoresponse integrating physical constraints and biological regulations are lacking. Here, we propose such a theory, utilizing the separation of timescales for passive responses and active regulations. We demonstrate that regulations of osmolyte production and cell-wall synthesis assist cells in coping with intracellular crowding effects and adapting to a broad range of external osmolarity. Furthermore, we predict a threshold value above which cells cannot grow, ubiquitous across bacteria and yeast. Intriguingly, the theory predicts a dramatic speedup of cell growth after an abrupt decrease in external osmolarity due to cell-wall synthesis regulation. Our theory rationalizes the unusually fast growth observed in fission yeast after an oscillatory osmotic perturbation, and the predicted growth rate peaks match quantitatively with experimental measurements. Our study reveals the physical basis of osmoresponse, yielding far-reaching implications for microbial physiology.

## Introduction

Microbes constantly transition between environments with dramatically different osmolarities, a hallmark of microbial life (Csonka, 1989; Muzzey et al., 2009; Wood, 2015; Bremer and Krämer, 2019). One of the most essential features of walled microbial cells is the turgor pressure – the elastic stress stretching the cell wall due to osmotic imbalance. Upon a hypoosmotic shock (i.e. a sudden decrease of the external osmolarity), the turgor pressure increases immediately due to the sudden water influx. To relax the turgor pressure, the cell upregulates the cell-wall synthesis rate, adds more materials to the peptidoglycan network, and eventually adapts to the lower external osmolarity (Typas et al., 2010). Upon a hyperosmotic shock (i.e. a sudden increase of the external osmolarity), the cell volume of a microbial cell shrinks within milliseconds due to water efflux, leading to a decreased turgor pressure (Rojas and Huang, 2018; Cadart et al., 2019). To increase the internal osmotic pressure, microorganisms increase their intracellular solute pool by amassing osmolyte molecules (i.e. osmoregulation), e.g., through de novo synthesis (Kempf and Bremer, 1998). The cell volume then restores progressively over time, and eventually, the cell adapts to the higher osmolarity. Intracellular crowding may act as a cell volume sensor to trigger osmoregulation (Burg, 2000; van den Berg et al., 2017; Model et al., 2021). Meanwhile, intracellular crowding due to volume reduction inevitably affects the cellular physiology globally, e.g., slowing down protein diffusion (Dix and Verkman, 2008; Dill et al., 2011; Miermont et al., 2013; Mika et al., 2014; Munder et al., 2016; Joyner et al., 2016; Molines et al., 2022) and reducing the elongation speed of translating ribosomes (Dai et al., 2018; Chen et al., 2023). Despite extensive knowledge regarding the molecular details of osmotic response pathways (Bremer and Krämer, 2019), how intracellular crowding interferes with gene expression regulation and affects osmotic adaptation remains an open question.

Interestingly, many features of microbial osmoresponses appear general across different organisms, suggesting a universal underlying mechanism. For example, it is widely observed that microbial cells can adapt to a broad range of external osmolarity, with the external osmotic pressure varying over an order of magnitude (Cayley et al., 1991; Dai et al., 2018; Rojas et al., 2014; Rojas et al., 2017). Furthermore, the growth rate in the steady state decreases as the external osmolarity increases, and a complete arrest of cell growth occurs above a critical osmolarity (Scott, 1953; Christian and Scott, 1953; Christian, 1955; Rojas et al., 2014; Rojas et al., 2017; Dai et al., 2018). Moreover, upon an osmotic shock, the growth rate usually does not approach the new steady-state value monotonically, e.g., an overshoot of growth rate often occurs upon a hypoosmotic shock (Rojas et al., 2017), and a damped oscillation of growth rate can happen after a hyperosmotic shock (Rojas et al., 2014). In recent experiments of Schizosaccharomyces pombe by Knapp et al., 2019, an oscillatory osmotic shock was applied to cells, during which cell volume growth was dramatically slowed down while biomass was still actively produced. Surprisingly, a supergrowth phase happened after removing the oscillatory osmotic shock, during which cells grew much faster than the steady state before the shocks.

In this work, we unify all these phenomena by a theory capturing the essential elements of osmoresponses: physical constraints (e.g. the crowding effects and osmotic imbalance) and biological regulation, including osmoregulation (i.e. regulation of the osmolyte-producing protein) and cell-wall synthesis regulation. Our model assumes the following phenomenological rules: (1) the change in free water volume within the cell is driven by osmotic imbalance (Cadart et al., 2019; Rollin et al., 2023), while the remaining volume changes in proportion to protein production; (2) osmoregulation influences the production of osmolyte-producing protein, governed by intracellular protein density; (3) cell-wall synthesis is regulated through a feedback mechanism, wherein turgor pressure modulates the efficiency of cell-wall synthesis, enabling the cell to maintain a relatively stable turgor pressure; and (4) intracellular crowding slows down biochemical reactions as the protein density increases, with reactions ceasing entirely when the protein density reaches a critical threshold. Upon a hyperosmotic shock, cell volume reduction due to water efflux increases the protein density, inducing the upregulation of osmolyte-producing protein but slowing down the translation speed due to crowding. Upon a hypoosmotic shock, the dramatic water influx stretches the cell wall, and the increased turgor pressure induces cell-wall synthesis (Typas et al., 2010; Jiang and Sun, 2010; Amir and Nelson, 2012).

We remark that our model is coarse-grained, without including detailed molecular mechanisms, and is therefore applicable across diverse microbial species. Notably, the predicted steady-state growth rate as a function of internal osmotic pressure from our model aligns well with experimental data from diverse organisms. This alignment allows us to quantify the sensitivities of translation speed and regulation of osmolyte-producing protein in response to intracellular density. Additionally, we demonstrate that osmoregulation and cell-wall synthesis regulation enable cells to adapt to a wide range of external osmolarities and prevent plasmolysis. Our model also predicts a non-monotonic time dependence of growth rate and protein density as they approach steady-state values following a constant osmotic shock, in concert with experimental observations (Rojas et al., 2014; Rojas et al., 2017). Moreover, we show that a supergrowth phase can arise following a sudden decrease in external osmolarity, driven by cell-wall synthesis regulation, either through the direct application of a hypoosmotic shock or the withdrawal of an oscillatory stimulus. Remarkably, the predicted amplitudes of supergrowth (i.e. growth rate peaks) quantitatively agree with multiple independent experimental measurements (Knapp et al., 2019).

In the following Results section, we begin by outlining the primary assumptions and equations of our model in the subsection Model description, which includes four parts, each addressing one of the four phenomenological rules. Additional details can be found in Materials and methods. We then proceed to the subsection Steady states in constant environments, where we employ our theoretical framework to analyze steady-state growth and examine how the growth rate varies with external osmolarity. In the subsection Transient dynamics after a constant osmotic shock, we investigate the time-dependent osmoresponse after a constant hyperosmotic and hypoosmotic shock. Finally, in Comparison with experiments: supergrowth phenomena after osmotic oscillation, we address the supergrowth phenomena observed in S. pombe, utilizing our model to elucidate these experimental observations.

## Results

### Model description

#### Cell growth

In the limit of an extreme hyperosmotic shock, the remaining cytoplasmic volume is comparable to the volume of expelled water (Cayley et al., 1991; Scott Cayley et al., 2000; Miermont et al., 2013). Thus, the total cytoplasmic volume must be divided into a free volume and a bound volume (Whatmore and Reed, 1990; Cayley and Record, 2003; Lemière and Chang, 2023; Zhou et al., 2009; Rollin et al., 2023):

$$
V=V_{f}+V_{b}.
$$

The free volume comes from the free water that is osmotically active, and the bound volume includes the bound water $V_{bw}$ (i.e. water of macromolecular hydration) and the volume of dry mass $V_{bd}$ (Figure 1A). Because the fraction of protein mass in the total dry mass is typically constant and the volume of bound water is proportional to the dry mass (Cayley et al., 1991), the bound volume is proportional to the total protein mass $m_{p}$ through $V_{b}=\alpham_{p}$. Here, $\alpha$ is a constant, and its values for some model organisms are included in Table 1, and its detailed calculations from experimental data are in Section B of Appendix 1.

![Figure 1.](https://cdn.elifesciences.org/articles/102858/elife-102858-fig1-v1.jpg)

**Figure 1.:** (A) The total cytoplasmic volume includes the free and bound volumes. The free volume sets the internal osmotic pressure $Π_{in}=k_{B}TN_{a}/V_{f}$, where $V_{f}$ is the free volume and $N_{a}$ is the number of osmolyte molecules. The bound volume $V_{b}$ comprises the dry mass $V_{bd}$ and bound water $V_{bw}$, i.e., $V_{b}=V_{bd}+V_{bw}$, all proportional to the total protein mass. (B) We model osmoregulation through the change of ribosome translation strategy. When the protein density increases, the fraction of ribosomes translating the osmolyte-producing protein $χ_{a}$ is upregulated, leading to the subsequent increase in the mass fraction of the osmolyte-producing protein $ϕ_{a}$. Here, $\mu_{r}$ denotes the dry-mass growth rate. (C) The cell-wall synthesis process is controlled by the turgor pressure $\sigma$, which is proportional to the cell-wall strain $ϵ=(V−V_{cw})/V_{cw}$. Here, $V$ is the cytoplasmic volume, and $V_{cw}$ is the relaxed cell-wall volume.

**Table 1.**
 Model parameters for different species in their corresponding reference growth media.


<table>
  <thead>
    <tr>
      <th>E. coli</th>
      <th>Value</th>
      <th colspan="3">Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>σc\begin{document}$\sigma_{c}$\end{document}</td>
      <td>1 [atm]</td>
      <td colspan="3">Rojas and Huang, 2018</td>
    </tr>
    <tr>
      <td>α\begin{document}$\alpha$\end{document}</td>
      <td>1.68 [ml/g]</td>
      <td colspan="3">Deduce from Scott Cayley et al., 2000</td>
    </tr>
    <tr>
      <td></td>
      <td>MBM (Cayley et al., 1991)</td>
      <td>MOPS+fructose (Dai et al., 2018)</td>
      <td>MOPS+glucose (Dai et al., 2018)</td>
      <td>LB (Rojas et al., 2014)</td>
    </tr>
    <tr>
      <td>krmaxχr\begin{document}$k_{r}^{\max}\chi_{r}$\end{document}</td>
      <td>0.743 [1/hr]</td>
      <td>0.776 [1/hr]</td>
      <td>1.14 [1/hr]</td>
      <td>2.05 [1/hr]</td>
    </tr>
    <tr>
      <td>Πin,c\begin{document}$\Pi_{in,c}$\end{document}</td>
      <td>1.54 [Osm]</td>
      <td>1.49 [Osm]</td>
      <td>1.61 [Osm]</td>
      <td>2.18 [Osm]</td>
    </tr>
    <tr>
      <td>Hr/(Ha+1)\begin{document}$H_{r}/(H_{a}+1)$\end{document}</td>
      <td>1.68</td>
      <td>1.30</td>
      <td>1.18</td>
      <td>2.72</td>
    </tr>
    <tr>
      <td>Bacillus subtilis (LB)</td>
      <td>Value</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>σc\begin{document}$\sigma_{c}$\end{document}</td>
      <td>19 [atm]</td>
      <td>Whatmore and Reed, 1990</td>
    </tr>
    <tr>
      <td></td>
      <td>2.52 [1/hr]</td>
      <td rowspan="3">Fit to Rojas et al., 2017</td>
    </tr>
    <tr>
      <td>Hr/(Ha+1)\begin{document}$H_{r}/(H_{a}+1)$\end{document}</td>
      <td>2.18</td>
    </tr>
    <tr>
      <td>Πin,c\begin{document}$\Pi_{in,c}$\end{document}</td>
      <td>3.09 [Osm]</td>
    </tr>
    <tr>
      <td>S. pombe (YE5S)</td>
      <td>Value</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>Πout\begin{document}$\Pi_{out}$\end{document}</td>
      <td>0.2 [Osm]</td>
      <td>Atilgan et al., 2015</td>
    </tr>
    <tr>
      <td>σc\begin{document}$\sigma_{c}$\end{document}</td>
      <td>10 [atm]</td>
      <td>Lemière and Chang, 2023</td>
    </tr>
    <tr>
      <td>ρ^d\begin{document}$\hat{\rho}_{d}$\end{document}</td>
      <td>0.282 [g/ml]</td>
      <td>Odermatt et al., 2021</td>
    </tr>
    <tr>
      <td>ρp\begin{document}$\rho_{p}$\end{document}</td>
      <td>0.104 [g/ml]</td>
      <td>See Section B of Appendix 1</td>
    </tr>
    <tr>
      <td>μ</td>
      <td>0.35 [1/hr]</td>
      <td>Knapp et al., 2019</td>
    </tr>
    <tr>
      <td>f\begin{document}$  f$\end{document}</td>
      <td>0.788</td>
      <td>Fit to Molines et al., 2022 (Section B of Appendix 1)</td>
    </tr>
    <tr>
      <td>ϵ\begin{document}$  \epsilon$\end{document}</td>
      <td>0.584</td>
      <td>Atilgan et al., 2015</td>
    </tr>
    <tr>
      <td>α\begin{document}$\alpha$\end{document}</td>
      <td>2.60 [ml/g]</td>
      <td>See Section B of Appendix 1</td>
    </tr>
    <tr>
      <td>G\begin{document}$G$\end{document}</td>
      <td>17.1 [atm]</td>
      <td>G=σ/ϵ\begin{document}$G=\sigma/\epsilon$\end{document}</td>
    </tr>
    <tr>
      <td>Πout,c\begin{document}$\Pi_{out,c}$\end{document}</td>
      <td>3.5 [Osm]</td>
      <td></td>
    </tr>
    <tr>
      <td>kw\begin{document}$k_{w}$\end{document}</td>
      <td>100 [1/(min atm)]</td>
      <td></td>
    </tr>
    <tr>
      <td>ρc\begin{document}$\rho_{c}$\end{document}</td>
      <td>0.267 [g/ml]</td>
      <td>Deduce from Molines et al., 2022 (Section B of Appendix 1)</td>
    </tr>
    <tr>
      <td>Hr\begin{document}$H_{r}$\end{document}</td>
      <td>3.03</td>
      <td>Copied from S. cerevisiae in YPD</td>
    </tr>
    <tr>
      <td>Ha\begin{document}$H_{a}$\end{document}</td>
      <td>0.974</td>
      <td>Set according to Πin/Πin,c=(ρp/ρc)Ha\begin{document}$  \Pi_{in}/\Pi_{in,c}=\left(\rho_{p}/\rho_{c}\right)^{H_{a}}$\end{document}</td>
    </tr>
    <tr>
      <td>krmaxχr\begin{document}$k_{r}^{\max}\chi_{r}$\end{document}</td>
      <td>0.371 [1/hr]</td>
      <td>Set according to μr=krmaxχr(1−(ρp/ρc)Hr)\begin{document}$\mu_{r}=k_{r}^{\max}\chi_{r}\left(1-\left(\rho_{p}/\rho_{c}\right)^{H_{r}}\right)$\end{document}</td>
    </tr>
    <tr>
      <td>kBTkamaxχamax\begin{document}$k_{B}Tk_{a}^{\max}\chi_{a}^{\max}$\end{document}</td>
      <td>2.25 [(atm ml)/(g min)]</td>
      <td>Set according to kBTkamaxχamaxηaρp=krmaxχrΠin\begin{document}$k_{B}Tk_{a}^{\max}\chi_{a}^{\max}\eta_{a}\rho_{p}=k_{r}^{\max}\chi_{r}\Pi_{in}$\end{document}</td>
    </tr>
    <tr>
      <td>τcw−\begin{document}$\tau_{cw}^{-}$\end{document}</td>
      <td>0.1 [min]</td>
      <td></td>
    </tr>
    <tr>
      <td>τcw+\begin{document}$  \tau_{cw}^{+}$\end{document}</td>
      <td>12.5 [min]</td>
      <td rowspan="2">Fit to Knapp et al., 2019</td>
    </tr>
    <tr>
      <td>Hcw\begin{document}$H_{cw}$\end{document}</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td>S. cerevisiae (YPD)</td>
      <td>Value</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>Πout\begin{document}$\Pi_{out}$\end{document}</td>
      <td>0.26 [Osm]</td>
      <td></td>
    </tr>
    <tr>
      <td>σc\begin{document}$\sigma_{c}$\end{document}</td>
      <td>3.1 [atm]</td>
      <td>Lemière and Chang, 2023</td>
    </tr>
    <tr>
      <td>ρ^d\begin{document}$\hat{\rho}_{d}$\end{document}</td>
      <td>0.295 [g/ml]</td>
      <td>Feijó Delgado et al., 2013</td>
    </tr>
    <tr>
      <td>μ</td>
      <td>0.448 [1/hr]</td>
      <td>Our experiment</td>
    </tr>
    <tr>
      <td>f\begin{document}$f$\end{document}</td>
      <td>0.6</td>
      <td>Miermont et al., 2013</td>
    </tr>
    <tr>
      <td>ρp\begin{document}$\rho_{p}$\end{document}</td>
      <td>0.155 [g/ml]</td>
      <td>See Section B of Appendix 1</td>
    </tr>
    <tr>
      <td>ρc\begin{document}$\rho_{c}$\end{document}</td>
      <td>0.994 [g/ml]</td>
      <td>See Section B of Appendix 1</td>
    </tr>
    <tr>
      <td>α\begin{document}$\alpha$\end{document}</td>
      <td>4.29 [ml/g]</td>
      <td>See Section B of Appendix 1</td>
    </tr>
    <tr>
      <td>krmaxχr\begin{document}$k_{r}^{\max}\chi_{r}$\end{document}</td>
      <td>0.450 [1/hr]</td>
      <td rowspan="3">Fit to our data</td>
    </tr>
    <tr>
      <td>Πin,c\begin{document}$\Pi_{in,c}$\end{document}</td>
      <td>3.52 [Osm]</td>
    </tr>
    <tr>
      <td>Hr/(Ha+1)\begin{document}$H_{r}/(H_{a}+1)$\end{document}</td>
      <td>2.54</td>
    </tr>
    <tr>
      <td>Hr\begin{document}$H_{r}$\end{document}</td>
      <td>3.03</td>
      <td>Set according to 1−(ρp/ρc)Hr=μ/(krmaxχr)\begin{document}$1-(\rho_{p}/\rho_{c})^{H_{r}}=\mu/(k_{r}^{\max}\chi_{r})$\end{document}</td>
    </tr>
  </tbody>
</table>

The free volume changes due to osmotic imbalance, and the growth rate of the free volume follows

$$
\mu_{f}≡\frac{V_{f}˙}{V_{f}}=k_{w}(Π_{in}−Π_{out}−\sigma),
$$

where $Π_{in}$, $Π_{out}$ are the internal (i.e. cytoplasmic) and external osmotic pressures, respectively (Cadart et al., 2019). $Π_{in}$ is proportional to the concentration of osmolyte molecules in the free volume: $Π_{in}=k_{B}TN_{a}/V_{f}$, where $N_{a}$ is the number of osmolyte molecules, $k_{B}$ is the Boltzmann constant, and $T$ is the temperature. For simplicity, we assume that the production speed of osmolyte molecules is proportional to the mass of osmolyte-producing protein (Materials and methods). Here, we have replaced the difference of the hydrostatic pressures across the cell membrane with the turgor pressure $\sigma$, assuming that mechanical equilibrium is always satisfied. $k_{w}$ is the filtration coefficient quantifying the water permeability of the cell membrane (Solenov et al., 2017).

The species of osmolytes involved in osmoregulation are diverse across different microorganisms and conditions; nevertheless, they are primarily small organic molecules (Kempf and Bremer, 1998; Empadinhas and da Costa, 2008). In this work, we simplify the problem by considering a single species of osmolyte that dominates the internal osmotic pressure, e.g., glycerol in Saccharomyces cerevisiae (Reed et al., 1987; Hohmann et al., 2007; Blomberg, 2022) and glycine betaine in Escherichia coli (Wood, 2015), with the production speed proportional to the mass of the osmolyte-producing protein (Figure 1A and Materials and methods).

To model gene expression regulation, we introduce $χ_{a}$ and $χ_{r}$ as the fractions of ribosomes translating the osmolyte-producing protein and ribosomal proteins (Figure 1B and Materials and methods). In steady states, $χ_{a}$ and $χ_{r}$ are equal to the mass fractions of osmolyte-producing protein and ribosomal proteins in the total proteome, $ϕ_{a}=m_{p,a}/m_{p}$ and $ϕ_{r}=m_{p,r}/m_{p}$, respectively (Scott et al., 2010; Wang and Lin, 2022). In this work, we assume that the dry-mass growth rate is proportional to the fraction of ribosomal proteins within the total proteome for simplicity, $\mu_{r}=k_{r}m_{p,r}/m_{p}=k_{r}ϕ_{r}$. This assumption leverages the fact that ribosomes are responsible for producing all proteins. The proportionality coefficient $k_{r}$ encapsulates the efficiency of ribosomal activity, being proportional to the elongation speed of the ribosome. We remark that $k_{r}$ is influenced by the crowding effect, which we address later. The growth rate of the cytoplasmic volume, $\mu=V˙/V$, is a weighted average of the free-volume growth rate $\mu_{f}$ and the dry-mass growth rate $\mu_{r}$:

$$
\mu=f\mu_{f}+(1−f)\mu_{r}.
$$

Here, $f$ is the free volume fraction in the total cytoplasmic volume: $f=V_{f}/V$. In this work, we refer to the growth rate as the growth rate of cytoplasmic volume μ unless otherwise mentioned.

#### Osmoregulation

Dai et al., 2018, found that the reduction of growth rate as the external osmolarity increases is dominated by the reduction of the translation speed $k_{r}$ instead of the ribosomal fraction $ϕ_{r}$. Therefore, we assume that the fraction of ribosomes translating themselves $χ_{r}$ is constant for simplicity. To model osmoregulation, we introduce a coupling between the fraction of ribosomes translating the osmolyte-producing protein $χ_{a}$ and the degree of intracellular crowding. We quantify the crowding effects by the protein density, defined as $ρ_{p}=m_{p}/V_{f}$, which serves as a good proxy for the dry-mass density measured in the experiments (Feijó Delgado et al., 2013; Odermatt et al., 2021) (see Table 1 and the detailed discussion on the relations between the two densities in Section A of Appendix 1) and propose the following relation:

$$
χ_{a}=χ_{a}^{max}(\frac{ρ_{p}}{ρ_{c}})^{H_{a}}.
$$

Here, the parameter $H_{a}$ quantifies the sensitivity of osmoregulation to intracellular crowding. $ρ_{c}$ is the critical protein density above which intracellular processes are frozen, which we introduce later in Equation 8. Therefore, $χ_{a}^{max}$ represents the largest possible $ϕ_{a}$ since all intracellular dynamics is frozen when $ρ_{p}>ρ_{c}$. We remark that our model can be directly generalized to cases where osmolyte molecules are extracted from the environment. One only needs to change the interpretation of the parameter $k_{a}$ in Equation 17 from the synthesis rate to the uptake rate, and all the results are the same.

#### Cell-wall synthesis regulation

In this work, the cell wall is regarded as a linear elastic material, where the turgor pressure is proportional to the elastic strain of the cell wall by a constant modulus $G$ such that

$$
\sigma=Gϵ=G(\frac{V}{V_{cw}}−1).
$$

Here, $V_{cw}$ is the relaxed cell-wall volume (Figure 1C). When plasmolysis happens, the cell membrane detaches from the cell wall ($V<V_{cw}$), and the turgor pressure is zero. We introduce the growth rate of the relaxed cell-wall volume as $\mu_{cw}=V˙_{cw}/V_{cw}$. Given that in the steady states of cell growth, $\mu_{r}=\mu_{cw}$, we write $\mu_{cw}$ in the following form without losing generality,

$$
\mu_{cw}=\mu_{r}η_{cw}.
$$

Here, $η_{cw}$ is a coarse-grained parameter modeling the active regulation of cell-wall synthesis, which we refer to as the cell-wall synthesis efficiency in the following.

Experiments suggested that turgor pressure induces cell-wall synthesis, e.g., through mechanosensors on cell membrane in S. pombe (Dupres et al., 2009; Neeli-Venkata et al., 2021), by increasing the pore size of the peptidoglycan network (Typas et al., 2010) and by accelerating the moving velocity of the cell-wall synthesis machinery in E. coli (Amir and Nelson, 2012). Guided by these ideas, we model the effects of turgor pressure on the time dependence of the cell-wall synthesis efficiency as

$$
η˙_{cw}=\frac{1}{\tau_{cw}^{\pm}}[(\frac{\sigma}{\sigma_{c}})^{H_{cw}}−η_{cw}].
$$

Here, $\sigma_{c}$ is a characteristic scale of turgor pressure depending on species. $\tau_{cw}^{+}$ ($\tau_{cw}^{−}$) is the relaxation timescale when the current $η_{cw}$ is below (above) its target value $η_{cw}^{st}=(\sigma/\sigma_{c})^{H_{cw}}$. The former (latter) happens immediately after the cell is subject to a hypoosmotic (hyperosmotic) shock. In the extreme case of plasmolysis, the insertion of newly synthesized cell-wall materials is interrupted immediately due to the separation of the cell membrane and cell wall. Meanwhile, the upregulation of cell-wall synthesis rate presumably takes a longer time. For example, in fungi, where polarized growth is generally adopted, the upregulation of the cell-wall synthesis rate involves reorienting the polarisome complex to the growing tip, directing actin polarization, and delivering cell-wall synthesis machinery (Kono et al., 2012; Haupt et al., 2018). Therefore, we set $\tau_{cw}^{+}≫\tau_{cw}^{−}$ in this work (see details of parameter values in Table 1).

#### Intracellular crowding

Multiple experiments suggested the cytoplasm of bacteria, yeast, and mammalian cells resemble crowded colloidal suspensions in which the mobilities of biomolecules are significantly reduced compared with dilute solutions (Miermont et al., 2013; Parry et al., 2014; Mika et al., 2014; Nishizawa et al., 2017; Ebata et al., 2023), a signature of glass transition (Hunter and Weeks, 2012). Intracellular crowding affects biochemical processes globally, e.g., slowing down translation and intracellular signaling by suppressing protein diffusion (Miermont et al., 2013; Parry et al., 2014; Mika et al., 2014; Dai et al., 2018; Molines et al., 2022). Therefore, we assume that the speed of osmolyte production, translational elongation, and cell-wall synthesis are all slowed down by the same crowding factor:

$$
η_{r}=1−(\frac{ρ_{p}}{ρ_{c}})^{H_{r}}.
$$

Here, $ρ_{c}$ is the critical protein density, and $H_{r}$ is a parameter to quantify the sensitivity of biochemical reactions to the intracellular density. For example, the translational elongation speed is suppressed by intracellular crowding through $k_{r}=k_{r}^{max}η_{r}$. Therefore, the dry-mass growth rate becomes $\mu_{r}=\mu_{r}^{max}η_{r}$, where we introduce $\mu_{r}^{max}=k_{r}^{max}ϕ_{r}$.

The details of our model are summarized in Materials and methods, with five independent variables: the protein density $ρ_{p}$, the mass fraction of osmolyte-producing protein $ϕ_{a}$, the internal osmotic pressure $Π_{in}$, the cell-wall strain $ϵ$, and the cell-wall synthesis efficiency $η_{cw}$. For convenience, Appendix 1—table 3 provides a comprehensive list of all symbols used in the main text along with their meanings.

### Steady states in constant environments

When cell growth reaches a steady state, the proportions of all components, including free water volume, cell mass, and cell-wall volume, must be constant relative to the total cell volume to ensure homeostasis. Therefore, all growth rates in steady states of cell growth must be the same: $\mu_{f}=\mu_{r}=\mu_{cw}$. The consequence of cell-wall synthesis regulation can be seen directly from $\mu_{cw}=\mu_{r}$: the turgor pressure at steady states is constant, $\sigma=\sigma_{c}$. Experimentally, the cell-wall strain was measured by applying an acute hyperosmotic shock to induce plasmolysis, and it is approximately constant as the external osmolarity increases (Misra et al., 2013; Rojas et al., 2014), suggesting a constant turgor pressure independent of external osmolarity, in concert with our model assumptions. The internal osmotic pressure at steady states is related to the external osmotic pressure through Equation 2,

$$
Π_{in}=Π_{out}+\sigma.
$$

Here, we have neglected the term $\mu_{f}/k_{w}$. Boer et al., 2011, show that an abrupt water flux occurs within hundreds of milliseconds after an osmotic shock, from which we can estimate the water permeability as $k_{w}∼100min^{−1}atm^{−1}$ considering an osmotic shock with an amplitude $ΔΠ_{out}=1$ atm. Because the typical doubling times of microorganisms are from about 20 min to several hours, we estimate $\mu_{f}/k_{w}∼10−100$ Pa (Ye and Verkman, 1989; Boer et al., 2011), negligible compared with the typical cytoplasmic osmotic pressures, which can be several atmospheric pressures.

In steady states, the internal osmotic pressure is independent of time. Combining Equation 4 and the dynamics of the internal osmotic pressure, Equation 18c, we find the relationships between the protein density, the internal osmotic pressure, and the growth rate in the steady states:

$$
\frac{Π_{in}}{ρ_{p}^{H_{a}+1}}=const,
$$



$$
\frac{\mu_{r}}{\mu_{r}^{max}}=1−(\frac{Π_{in}}{Π_{in,c}})^{\frac{H_{r}}{H_{a}+1}}.
$$

The right-hand side of Equation 10a is a constant independent of external osmolarity (see its detailed expression in Section C of Appendix 1). In deriving Equation 10b, we have replaced $ρ_{p}$ by $Π_{in}$ in Equation 8 using Equation 10a with the critical internal osmotic pressure $Π_{in,c}$ proportional to $ρ_{c}$. Intriguingly, the relationship between the normalized growth rate ($\mu_{r}/\mu_{r}^{max}$) and the normalized cytoplasmic osmotic pressure ($Π_{in}/Π_{in,c}$), which we refer to as the growth curve in the following, has only one parameter $H_{r}/(H_{a}+1)$. Therefore, the growth curves of different organisms can be unified by a single formula, Equation 10b, and different organisms may have different values of $H_{r}/(H_{a}+1)$. Furthermore, Equation 10b predicts a critical external osmolarity $Π_{out,c}=Π_{in,c}−\sigma_{c}$, beyond which cell growth is completely inhibited.

We test the validity of Equation 10b by fitting it to the experimental growth curves (Figure 2A). To do this, we calculate the internal osmotic pressure using Equation 9 given the values of the external osmotic pressure and the turgor pressure (Table 1). Intriguingly, the growth curves of multiple species can be well fitted by Equation 10b, from which we infer the parameters $H_{r}/(H_{a}+1)$ and $Π_{in,c}$ (Table 1). We find that budding yeast cells exhibit notable resilience to high external osmolarities: their $Π_{in,c}$ value is higher than those of Gram-positive bacteria, B. subtilis, and Gram-negative bacteria, E. coli. Further, budding yeast cells demonstrate a higher value of $H_{r}/(H_{a}+1)$, indicating a reduced susceptibility to growth rate reduction when exposed to mild increases in the external osmolarity. Meanwhile, the osmoadaptation capability of E. coli depends on the growth media, presumably arising from variations in metabolic fluxes and gene expressions (Cayley et al., 1991; Dai et al., 2018; Rojas et al., 2014).

![Figure 2.](https://cdn.elifesciences.org/articles/102858/elife-102858-fig2-v1.jpg)

**Figure 2.:** (A) Normalized growth rate vs. normalized internal osmotic pressure of different species under various culture media. The experiment data (scatter markers) are fitted by our theoretical prediction Equation 10b. The data of E. coli are from Cayley et al., 1991; Dai et al., 2018; Rojas et al., 2014, the data of B. subtilis is from Rojas et al., 2017, and the data of S. cerevisiae is from our own experiments, where sorbitol is added to increase the external osmolarity. (B) Growth curves of wild-type (WT) cells, mutant cells without osmoregulation ($H_{a}=0$), and mutant cells without cell-wall synthesis regulation ($H_{cw}=0$). The dotted line indicates the region where plasmolysis occurs for the mutant cells with $H_{cw}=0$. (C) Mutant cells without cell-wall synthesis regulation cannot maintain a stable turgor pressure in a hypertonic environment, while WT cells can maintain a constant turgor pressure. The mutant cells reach plasmolysis at a threshold of external osmolarity. In (B) and (C), the parameters for WT cells are chosen as the values for S. pombe, and the mutant values are set such that they have the same growth rate as the WT cells in the reference medium (Appendix 1—table 2).

To further reveal the functions of biological regulations, we study the steady-state properties of mutant cells in which either osmoregulation or cell-wall synthesis regulation is depleted. For mutant cells without osmoregulation, $H_{a}=0$ in Equation 4. In this case, the fraction of osmolyte-producing protein is constant with time, i.e., $ϕ_{a}=χ_{a}^{max}$. Comparing the dynamics of osmolyte and total protein mass, $N_{a}˙=k_{a}ϕ_{a}m_{p}$ and $m_{p}˙=k_{r}ϕ_{r}m_{p}$, one finds that the ratio of the number of osmolyte molecules and the total protein mass remains constant over time, irrespective of variations in external osmolarity (see the detailed derivation in Section C of Appendix 1). As the external osmolarity increases, the protein density of mutant cells quickly reaches the critical value $ρ_{c}$ according to Equation 10a with $H_{a}=0$. Therefore, the steady-state growth curve of the mutant cells terminates at an external osmolarity much smaller than wild-type (WT) cells (Figure 2B), in agreement with previous experiments (Brewster et al., 1993).

For mutant cells without the cell-wall synthesis regulation, $H_{cw}=0$; therefore, the cell-wall synthesis efficiency $η_{cw}$ equals 1 independent of time. Thus, the growth rate of the relaxed cell-wall volume is always equal to the growth rate of total protein mass (Equation 6 and Equation 7). Interestingly, in this case, the turgor pressure at steady states decreases with the increase of external osmolarity (Figure 2C and see the detailed proof in Section C of Appendix 1). The decreased turgor pressure lowers the internal osmotic pressure given the same $Π_{out}$ according to Equation 9, leading to a lower protein density of mutant cells than WT cells according to Equation 10a. Therefore, mutant cells grow faster than WT cells under the same external osmolarity (Figure 2B). Nevertheless, the mutant cells are prone to plasmolysis at a threshold external osmolarity where the WT cells can maintain constant turgor pressure (see the vertical line in Figure 2C around 2 M extra external osmolarity). Reduced turgor pressure is detrimental to multiple biological processes, e.g., cytokinesis in fission yeast requires the participation of turgor pressure (Proctor et al., 2012).

To summarize, osmoregulation allows cells to grow in a wide range of external osmolarity conditions with a mild change in protein density. The cell-wall synthesis regulation allows cells to maintain a stable turgor pressure and avoid plasmolysis. Both regulatory mechanisms expand the range of external osmolarities that cells can adapt to.

### Transient dynamics after a constant osmotic shock

Next, we study the dynamical behaviors of cellular properties in response to a constant osmotic shock: the external osmolarity changes abruptly and keeps its value for an infinitely long time. Intriguingly, we find that the dynamics of osmoresponse can be split into shock and adaptation periods (see insets of Figure 3C and D). The immediate water flow due to osmotic imbalance occurs in the shock period, during which the mass and osmolyte productions are negligible. Therefore, the ratio of the internal osmotic pressure and the protein density is invariant right before and after a shock period: $Π_{in}^{i}/ρ_{p}^{i}=Π_{in}^{f}/ρ_{p}^{f}$, where the upper index $i$ ($f$) means the state right before (after) the shock period. Given this condition, we introduce the normalized protein density $ρ~_{p}$ as

$$
ρ~_{p}=\frac{ρ_{p}}{ρ¯_{p}},
$$

![Figure 3.](https://cdn.elifesciences.org/articles/102858/elife-102858-fig3-v1.jpg)

**Figure 3.:** (A) Numerical simulations of cells undergoing a constant 500 mM hyperosmotic shock. The dotted lines represent the steady-state values for the reference growth medium (green) and the medium after perturbation (yellow). (B) Numerical simulations of cells undergoing a constant 500 mM hypoosmotic shock. The purple circle in the third panel marks the growth rate peak during the supergrowth phase. (C) The dynamics of the internal state of a cell characterized by ($ρ~_{p},η_{a}$). The dotted curve represents the constraint on the steady-state solution $ρ~_{p},η_{a}=1$, and the solid trajectory is from numerical simulations. The triangles indicate the steady-state solution before the perturbation and the steady-state solution after the perturbation for a long enough time. The yellow open circle represents the immediate steady-state solution after applying the hyperosmotic shock. (D) The same analysis as (C) but for a constant 500 mM hypoosmotic shock. (E) The growth rate peak in the supergrowth phase (yellow) and the immediate value of turgor pressure after the hypoosmotic shock 𝜎𝑓 (green) vs. the amplitude of the hypoosmotic shock.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/102858/elife-102858-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Simulation of a cell undergoing a constant 500 mM hypoosmotic shock, the same simulation as Figure 3B. Here, we show the time dependence of the internal osmotic pressure,$Π_{in}$ the turgor pressure, $\sigma$ the free volume fraction $f$, and the dry-mass growth rate $\mu_{r}$. All these quantities relax to their steady-state values (dotted lines) on the timescale set by the doubling time.

where the normalization factor $ρ¯_{p}∝Π_{in}$ (see its detailed expression in Materials and methods) so that $ρ~_{p}$ changes continuously across the shock period. Interestingly, we find that osmoresponse is governed by a two-dimensional dynamical system composed of $ρ~_{p}$ and $η_{a}≡ϕ_{a}/χ_{a}^{max}$ (Materials and methods):

$$
\frac{ρ~˙_{p}}{ρ~_{p}}=\mu_{r}^{max}η_{r}(1−ρ~_{p}η_{a}).
$$



$$
η˙_{a}=\mu_{r}^{max}η_{r}[(\frac{ρ~_{p}}{ρ~_{c}})^{H_{a}}−η_{a}],
$$

Here, $ρ~_{c}=ρ_{c}/ρ¯_{p}$ is the normalized critical protein density, and $η_{a}$ denotes the efficiency of osmoregulation. From the above equations, it is clear that the timescale of osmoregulation is set by the doubling time: it takes about the doubling time for the protein density and the fraction of osmolyte-producing protein to adapt to the new steady-state values. For walled cells, $ρ~_{c}$ and $ρ¯_{p}$ depend on time since $Π_{in}=Π_{out}+\sigma$ and the turgor pressure $\sigma$ is time-dependent during osmoresponse processes (Figure 3A and B). For unwalled cells, such as mammalian cells and microbial cells with cell walls removed (i.e. protoplasts), $ρ~_{c}$ is constant in a fixed environment (see detailed discussion on the transient dynamics of unwalled cells in Section D of Appendix 1).

Upon a constant hyperosmotic shock, the immediate water efflux leads to an instantaneous drop in turgor pressure and a rise in protein density (Figure 3A). The internal state of the cell, ($ρ~_{p}$, $η_{a}$), evolves toward the new equilibrium point, $(ρ~_{c}^{H_{a}/(H_{a}+1)},ρ~_{c}^{−H_{a}/(H_{a}+1)})$. One should note that the equilibrium point is time-dependent initially but eventually becomes fixed as the turgor pressure relaxes to the steady-state value (Figure 3C and Figure 3—video 1). Interestingly, the protein density increases initially and then decreases after the shock (Figure 3A). The decrease in protein density is because of the osmoregulation process, which is set by the doubling time (Equation 12a and Equation 12b). Meanwhile, we find that the initial increase of protein density is because of the suppressed growth of the relaxed cell-wall volume due to the low turgor pressure. Indeed, for unwalled cells, the protein density $ρ_{p}$ decreases immediately after the shock (Appendix 1—figure 2B). We note that the growth rate approaches the new steady-state value non-monotonically (Figure 3A) because of the spiral trajectory in the space of the internal state (Figure 3C), consistent with experimental observations from Rojas et al., 2014.

The phenomena are essentially the opposite for a constant hypoosmotic shock (Figure 3B and D, Figure 3—video 2). However, we find extremely fast cell growth after the hypoosmotic shock, with a growth rate peak occurring about 25 min after applying the shock, which we call the supergrowth phase (Knapp et al., 2019). One should note that 25 min is much shorter than the doubling time (about 2 hr) but comparable to the timescale of cell-wall synthesis regulation, which we set as $\tau_{cw}^{+}=12.5$ min in the simulations in Figure 3 (we will explain why we choose $\tau_{cw}^{+}=12.5$ min in the next section). Furthermore, applying a hypoosmotic shock to an unwalled cell does not induce a significant supergrowth phase compared with walled cells (Appendix 1—figure 2D).

We propose that supergrowth comes from the high turgor pressure caused by the hypoosmotic shock, which leads to fast cell-wall synthesis according to Equation 7. Rapid insertion of materials into the cell wall relaxes the turgor pressure and allows the cells to grow faster (Equation 2 and Equation 3). This idea is consistent with the observation that the growth rate and the growth rate of the relaxed cell-wall volume $\mu_{cw}$ reach their peaks simultaneously (Figure 3B). This observation also suggests that the timescale of supergrowth, i.e., the timing of growth rate peak, is set by the timescale of cell-wall synthesis regulation ($\tau_{cw}^{+}$ in Equation 7). Notably, in the initial stage of the adaptation period, $\mu_{cw}$ approaches its target from below and reaches its target value at the growth rate peak (i.e. $\mu_{r}(\sigma/\sigma_{c})^{H_{cw}}$) (the third panel of Figure 3B), after which $\mu_{cw}$ sticks to its target value and decreases accordingly because of the short relaxation time $\tau_{cw}^{−}$ (Equation 7). For comparison, we also show $\mu_{cw}$ and $\mu_{r}(\sigma/\sigma_{c})^{H_{cw}}$ for the hyperosmotic shock in the third panel of Figure 3A. A detailed proof of the conditions for supergrowth, including the necessity of a cell wall and the regulation of cell-wall synthesis, is provided in Section E of Appendix 1.

Following the discussion above, we obtain an analytical expression of the growth rate peak after a hypoosmotic shock (see the detailed derivations in Section F of Appendix 1)

$$
\mu^{sg}=\mu_{r}{1+\frac{f}{f+\frac{Π_{in}}{\sigma+G}}\times[(\frac{\sigma}{\sigma_{c}})^{H_{cw}}−1]}.
$$

Here, all the variables on the right side are at the growth rate peak. Because the timescale of the osmoresponse process, which is around hours (Figure 3B), is much longer than the timescale of the supergrowth phase, which is about 20 min for S. pombe (Knapp et al., 2019), the turgor pressure at the growth rate peak can be well approximated by its immediate value after the shock. Therefore, the growth rate peak must increase as the amplitude of the hypoosmotic shock increases, which we confirm numerically in Figure 3E.

### Comparison with experiments: supergrowth phenomena after osmotic oscillation

Next, we quantitatively compare our theoretical predictions regarding the supergrowth phase with experimental data. Knapp et al., 2019, applied an osmotic oscillation to fission yeast S. pombe during which the external osmolarity alternated between two values. They found cell growth was almost inhibited during the perturbation, while the protein and dry-mass densities increased. Surprisingly, cells grew unusually fast after the osmotic oscillation was removed and reached their maximum growth rate about 20 min after the end of the osmotic oscillation. The maximum growth rate can be twice the growth rate in the reference growth medium, and the elevation in growth rate can persist for two to three cell cycles. These observations are very similar to our results for a constant hypoosmotic shock (Figure 3B).

To test if our osmoresponse model captures the supergrowth phase for a periodic perturbation, we simulate WT S. pombe cells with the same protocols as the experiments (see details of simulations in Materials and methods). Intriguingly, our model successfully recapitulates the supergrowth phase and the gradually increasing protein density and dry-mass density during the perturbation (Figure 4). We confirm that cell-wall synthesis regulation is crucial for the emergence of the supergrowth phase since unwalled cells do not exhibit supergrowth after periodic perturbation (Appendix 1—figure 3). Interestingly, we find that an infinitely long periodic osmotic shock can be equivalently mapped to a constant osmotic shock (see the detailed discussions and proof in Section D of Appendix 1), which means that they have the same time-averaged growth rate and protein density in the steady states (Appendix 1—figure 2F).

![Figure 4.](https://cdn.elifesciences.org/articles/102858/elife-102858-fig4-v1.jpg)

**Figure 4.:** (A) Numerical simulations of wild-type (WT) S. pombe undergo 24 cycles of 500 mM osmotic oscillations with a 10 min period. We show a 30 min window average in the third panel of growth rate. (B–D) Quantitative agreement between simulations and experiments for the growth rate peak $\mu^{sg}$ vs. different oscillation parameters, including (B) amplitude, (C) period length, and (D) number of periods. The red lines in (B, C) are predictions, and the blue line in (D) is fitting from which we infer the values of $H_{cw}$ and $\tau_{cw}^{+}$. Green dots with error bars are experimental data from Knapp et al., 2019. (E) In the case of osmotic oscillation with a single period, the hyperosmotic period persists for 120 min before reverting to the reference medium. The vertical dotted blue line represents the minimal amplitude to induce cytoplasm jamming during the hyperosmotic period. The excess turgor pressure $\sigma^{f}−\sigma_{c}$ upon exiting the hyperosmotic period is approximately equal to the recovered turgor pressure $\delta\sigma$ during the hyperosmotic period. (F) The growth rate peak $\mu^{sg}$ at different $H_{r}$ vs. the amplitude of a single oscillation. $H_{r}=3.031$ is the value of the WT S. pombe. Parameters of WT S. pombe are used in this figure unless otherwise mentioned (Table 1).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/102858/elife-102858-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Simulation of a wild-type cell undergoing 24 cycles of 500 mM osmotic oscillation with a 10 min period, the same simulation as Figure 4A. We plot the cell-wall synthesis efficiency $η_{cw}$ and the dry-mass density $ρ^_{d}$ for better comparison with experimental data (Knapp et al., 2019).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/102858/elife-102858-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** The non-monotonic relationship between $\mu^{sg}$ and amplitude.Growth rate peak vs. oscillation amplitude under different numbers of oscillation periods. The total duration of the oscillation stimulus is fixed.

Knapp et al., 2019, measured the growth rate peaks vs. three different parameters of the osmotic oscillations: amplitude, period length, and number of periods. We first fit the growth rate peaks vs. the amplitudes (Figure 4D), from which we obtain $H_{cw}=1.7$, the sensitivity of the cell-wall synthesis efficiency to turgor pressure (Equation 7), and $\tau_{cw}^{+}=12.5$ min, the timescale in the upregulation of cell-wall synthesis efficiency (which is why we set $\tau_{cw}^{+}=12.5$ min in the previous section). Other model parameters are inferred from independent steady-state measurements, and we set the timescale in the downregulation of cell-wall synthesis efficiency as $\tau_{cw}^{−}=0.1$ min for simplicity (Table 1). We next fix the values of $H_{cw}$ and $\tau_{cw}^{+}$ and plot the predicted growth rate peaks vs. the period length (Figure 4B) and number of periods (Figure 4C). As a strong support of our model, our predictions quantitatively match the experimental data without any further fitting.

Two interesting features of the curve $\mu^{sg}$ vs. amplitude catch our attention: the non-monotonic behavior and the kink point at which the derivative is discontinuous (Figure 4D), which are conserved regardless of the number of periods (Figure 4—figure supplement 2). Therefore, we study the case of a single oscillation for simplicity, which is equivalent to a hyperosmotic shock of finite duration. For a mild hyperosmotic shock, during the period of hyperosmotic shock, the turgor pressure has almost recovered to the steady-state value $\sigma_{c}$ (Figure 3A). Therefore, switching from a long hyperosmotic period to the reference growth medium is equivalent to a constant hypoosmotic shock, where we have shown that the growth rate peak increases with the amplitude (Figure 3E). However, the crowding effect becomes more pronounced as the amplitude increases. Beyond the critical amplitude at the kink point, the cytoplasm is completely jammed during the hyperosmotic shock such that the cell states are precisely the same before and after the hyperosmotic shock, which means no supergrowth phase beyond this critical amplitude. Therefore, the curve $\mu^{sg}$ vs. amplitude must be non-monotonic (Figure 4E). Notably, for a very large $H_{r}$, cells can feel the crowding effect only when the cytoplasm is close enough to the critical protein density, shown as the abrupt decline of $\mu^{sg}$ (Figure 4F).

Finally, we remark that the significance of supergrowth is intimately related to the amount of recovered turgor pressure during the hyperosmotic shock $\delta\sigma$. We prove that the overshoot of turgor pressure after the removal of hyperosmotic shock ($\sigma^{f}−\sigma_{c}$), which sets the growth rate peak, is mainly set by the recovered turgor pressure during the hyperosmotic shock (see the detailed discussions in Section G of Appendix 1). Indeed, $\mu^{sg}$, $\sigma^{f}−\sigma_{c}$, and $\delta\sigma$ are highly correlated as we change the amplitude (Figure 4E).

## Discussion

This study presents a theory of microbial osmoresponses based on a physical foundation and simplified biological regulation strategies. Our theory captures the steady-state properties of constant turgor pressure and reduced growth rate with increasing external osmolarity. We remark that the growth rate reduction is due to the loss of free water and subsequent intracellular crowding as the external osmolarity increases. In particular, we predict a critical external osmolarity above which cell growth is completely inhibited and a universal relationship between the normalized growth rate and the normalized internal osmotic pressure, fitting the data of bacteria and yeast. We also demonstrate the biological functions of osmoregulation and cell-wall synthesis regulation. Cells defective in osmoregulation cannot grow even if the external osmolarity is only mildly higher than the reference value. Cells defective in cell-wall synthesis regulation cannot maintain turgor pressure as the external osmolarity increases, even though they grow faster than WT cells (Figure 2B), which will be a strong support of our theory if confirmed by experiments.

Regarding dynamic behaviors, our model predicts a non-monotonic time dependence of protein density after a constant hyperosmotic shock. We also unveil the supergrowth phase after a hypoosmotic shock, initially discovered in fission yeast after an osmotic oscillation (Knapp et al., 2019). As a strong support of our theory, the predicted growth rate peaks quantitatively agree with the experimental data without additional fitting. We demonstrate the critical role of cell-wall synthesis regulation in the supergrowth phenomenon (Section E of Appendix 1). Knapp et al., 2019, observed the rapid repolarization of the cell-wall glucan synthase Bgs4 to the cell tip following the removal of osmotic oscillations in fission yeast, in agreement with the dynamics of the cell-wall synthesis efficiency predicted from our model (compare Figure 4—figure supplement 1 in this work and Figure S4H in Knapp et al., 2019). To test our theory, we propose applying a hyperosmotic shock with a finite duration and measuring the growth rate after removing the hyperosmotic shock. We predict that the growth rate peak during the supergrowth phase is a non-monotonic function of shock amplitude, initially rising because of the increased excess turgor pressure and later declining because the protein density reaches the critical value $ρ_{c}$ during the shock (Figure 4E).

We remark that our model is intrinsically a coarse-grained model with many molecular details regarding gene expression regulation neglected, which allows us to gain more analytical insights. Shen et al., 2023, studied the responses to osmotic stress in glucose-limited environments and found that cells exhibited stronger osmotic gene expression response under glucose-limited conditions than under glucose-rich conditions. Using a computational model based on molecular mechanisms combined with experimental measurements, the authors demonstrated that in a glucose-limited environment, glycolysis intermediates were limited, which required cells to express more glycerol-production enzymes for stress adaptation. In the current version of our model, we do not account for the interaction between cell growth and osmolyte production; instead, we assume a constant fraction of ribosomes dedicated to translating ribosomal proteins. Our model can be further generalized to include the more complex interactions, including the coupling between biomass and osmolyte production, e.g., by allowing the fraction of ribosomes translating ribosomal proteins ($χ_{r}$) to depend on the translation strategy of the osmolyte-producing enzyme ($χ_{a}$).

Rojas et al., 2014, showed that the expansion of E. coli cell wall is not directly regulated by turgor pressure, and this scenario is also included in our model as the case of $H_{cw}=0$. According to our model, the supergrowth phase is absent if $H_{cw}=0$ (Appendix 1—figure 8), consistent with the absence of a growth rate peak after a hypoosmotic shock in the experiments of E. coli (Rojas et al., 2014). Meanwhile, our predictions are consistent with the growth rate peak after a hypoosmotic shock observed for B. subtilis (Rojas et al., 2017).

We remark on several limitations of our current coarse-grained model. First, the high membrane tension that inhibits transmembrane flux of peptidoglycan precursors, leading to a growth inhibition before the supergrowth peak (Rojas et al., 2017), is beyond our model. Second, in our current framework, osmoregulation and cell-wall synthesis regulation rely on the instantaneous cellular states. However, microorganisms can exhibit memory effects to external stimuli by adapting to their temporal order of appearance (Mitchell et al., 2009). Notably, in the osmoregulation of yeast, a short-term memory, facilitated by posttranslational regulation of the trehalose metabolism pathway, and a long-term memory, orchestrated by transcription factors and mRNP granules, have been identified by Jiang et al., 2020. Besides, our model does not account for the role of osmolyte export in osmoregulation (Tamás et al., 1999) and the interaction between biomass and osmolyte production (Shen et al., 2023). Extending our model to include more realistic biological processes will be interesting.

In this work, we construct a systems-level and coarse-grained model capable of elucidating the complex processes underlying microbial osmoresponse. By leveraging the separation of timescales associated with mechanical equilibrium, cell-wall synthesis regulation, and osmoregulation, our model facilitates in-depth analytical and numerical analysis of how these various processes interact during cellular adaptation. In particular, we demonstrate the key physiological functions of osmoregulation and cell-wall synthesis regulation. We then apply this model to interpret the unusual phenomenon of supergrowth observed in fission yeast. This application addresses an essential challenge in experimental studies: exclusive knockout experiments can be difficult, and mechanistic interpretations of experimental observations are often lacking. Our theoretical framework offers a valuable tool for understanding such phenomena, contributing to the fundamental knowledge of microbial physiology and developing predictive models for microbial behaviors under osmotic stress.

## Materials and methods

### Details of the osmoresponse model

We define the fractions of osmolyte-producing protein and ribosomal proteins in the total proteome as $ϕ_{a}=m_{p,a}/m_{p}$ and $ϕ_{r}=m_{p,r}/m_{p}$, respectively. To model gene expression regulation, we introduce $χ_{a}$ and $χ_{r}$ as the fractions of ribosomes translating the osmolyte-producing protein and ribosomal proteins such that

$$
m˙_{p,r}=k_{r}χ_{r}m_{p,r}⇒ϕ˙_{r}=k_{r}ϕ_{r}(χ_{r}−ϕ_{r}),
$$



$$
m˙_{p,a}=k_{r}χ_{a}m_{p,a}⇒ϕ˙_{a}=k_{r}ϕ_{a}(χ_{a}−ϕ_{a}),
$$



$$
m˙_{p}=k_{r}m_{p,r}⇒\mu_{r}=k_{r}ϕ_{r}.
$$

Here, $k_{r}$ is proportional to the elongation speed of ribosomes on mRNAs divided by the protein mass of a single ribosome, which is affected by the global crowding effect as $k_{r}=k_{r}^{max}η_{r}$. Here, $\mu_{r}$ is the growth rate of total protein mass, which is also the growth rate of dry mass and bound volume in our model since they are all proportional. The osmolyte molecules are produced by the osmolyte-producing protein, with the rate given by

$$
N˙_{a}=k_{a}m_{p,a},
$$

where $k_{a}=k_{a}^{max}η_{r}$ is the osmolyte production rate, including the crowding factor, and $m_{p,a}$ is the mass of osmolyte-producing protein. We summarize the dynamical equations involved in the osmoresponse model:

$$
ρ˙_{p}=(\mu_{r}−\mu_{f})ρ_{p}
$$



$$
η˙_{a}=\mu_{r}[(\frac{ρ_{p}}{ρ_{c}})^{H_{a}}−η_{a}]
$$



$$
Π˙_{in}=k_{B}Tk_{a}^{max}η_{r}ϕ_{a}ρ_{p}−\mu_{f}Π_{in}
$$



$$
ϵ˙=(\mu−\mu_{cw})(ϵ+1)
$$



$$
η˙_{cw}=\frac{1}{\tau_{cw}^{\pm}}[(\frac{\sigma}{\sigma_{c}})^{H_{cw}}−η_{cw}].
$$

To describe the osmoregulation process using a two-dimensional dynamical system, we introduce the normalized protein density as

$$
ρ~_{p}=\frac{k_{B}Tk_{a}^{max}χ_{a}^{max}}{\mu_{r}^{max}}\frac{ρ_{p}}{Π_{in}}≡\frac{ρ_{p}}{ρ¯_{p}},
$$

Combining Equation 11 and Equation 18a, we obtain the dynamical equation for $ρ~_{p}$ as

$$
\frac{ρ~˙_{p}}{ρ~_{p}}=\mu_{r}^{max}η_{r}(1−ρ~_{p}η_{a}).
$$

Using Equation 15, we obtain the equation for $η_{a}=ϕ_{a}/χ_{a}^{max}$ as

$$
η˙_{a}=\mu_{r}^{max}η_{r}[(\frac{ρ~_{p}}{ρ~_{c}})^{H_{a}}−η_{a}],
$$

where $ρ~_{c}=ρ_{c}/ρ¯_{p}$. The unique equilibrium point for the internal state is

$$
(ρ~_{p}^{eq},η_{a}^{eq})=(ρ~_{c}^{\frac{H_{a}}{H_{a}+1}},ρ~_{c}^{−\frac{H_{a}}{H_{a}+1}}).
$$

### Details of numerical simulations

We employ the LSODA algorithm with automatic stiffness detection and switching (Petzold, 1983), implemented in SciPy (Virtanen et al., 2020), to solve Equation 18a–e. The parameters used for numerical simulations of walled cells are listed in Table 1.
