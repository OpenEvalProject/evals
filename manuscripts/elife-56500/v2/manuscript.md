# Stochastic bond dynamics facilitates alignment of malaria parasite at erythrocyte membrane upon invasion

## Authors

- Sebastian Hillringhaus<sup>1</sup> ([ORCID: 0000-0003-0100-9368](https://orcid.org/0000-0003-0100-9368))
- Anil K Dasanna<sup>1</sup> ([ORCID: 0000-0001-5960-4579](https://orcid.org/0000-0001-5960-4579))
- Gerhard Gompper<sup>1</sup> ([ORCID: 0000-0002-8904-0986](https://orcid.org/0000-0002-8904-0986)) †
- Dmitry A Fedosov<sup>1</sup> ([ORCID: 0000-0001-7469-9844](https://orcid.org/0000-0001-7469-9844)) †

### Affiliations

1. Theoretical Physics of Living Matter, Institute of Biological Information Processing and Institute for Advanced Simulation, Forschungszentrum Jülich Jülich Germany

† Corresponding author

## Abstract

Malaria parasites invade healthy red blood cells (RBCs) during the blood stage of the disease. Even though parasites initially adhere to RBCs with a random orientation, they need to align their apex toward the membrane in order to start the invasion process. Using hydrodynamic simulations of a RBC and parasite, where both interact through discrete stochastic bonds, we show that parasite alignment is governed by the combination of RBC membrane deformability and dynamics of adhesion bonds. The stochastic nature of bond-based interactions facilitates a diffusive-like re-orientation of the parasite at the RBC membrane, while RBC deformation aids in the establishment of apex-membrane contact through partial parasite wrapping by the membrane. This bond-based model for parasite adhesion quantitatively captures alignment times measured experimentally and demonstrates that alignment times increase drastically with increasing rigidity of the RBC membrane. Our results suggest that the alignment process is mediated simply by passive parasite adhesion.

## Introduction

Malaria is a dangerous mosquito-borne disease which kills nearly 0.5 million of people every year (World Health Organisation, 2018). It is caused by a protozoan parasite of the genus Plasmodium and proceeds in several stages (Miller et al., 2002; Cowman et al., 2012; White et al., 2014). After about 10 days from the initial infection through a mosquito bite, an infected liver releases a large number of merozoites, egg-shaped parasites with a typical size of $1−2\mum$ (Bannister et al., 1986; Dasgupta et al., 2014), into the blood stream. The blood stage of malaria infection is a clinically relevant stage, where merozoites invade healthy red blood cells (RBCs) and multiply inside by utilizing the RBC internal resources. This intra-erythrocytic development is essential for merozoites to be hidden from the immune system and avoid clearance. After about 48 hours post RBC invasion, infected RBCs are ruptured and new merozoites are released into the blood stream to repeat this reproduction cycle. Thus, RBC invasion by merozoites is crucial not only for parasite survival, but also for further multiplication.

RBC invasion by merozoites is preceded by three key events: (i) initial attachment, (ii) re-orientation or alignment of the parasite such that its apex is facing the RBC membrane, and (iii) formation of a tight junction (Koch and Baum, 2016). The apex contains all required machinery to invade RBCs after the tight junction is formed (Cowman and Crabb, 2006). At physiological hematocrit levels with a volume fraction of RBCs close to 40%, initial attachment of merozoites can be considered almost immediate after their egress from infected RBCs. However, the initial attachment has a random parasite orientation, which rarely provides direct alignment of the apex toward the membrane required to start the invasion. This implies that the parasite alignment is an extremely crucial step for successful invasion, which needs to be completed within a couple of minutes, as after this time period merozoites generally lose their ability to invade RBCs (Crick et al., 2014). To facilitate parasite alignment, merozoites contain a surface coat of proteins, mainly GPI-anchored, which can bind to the RBC membrane (Bannister et al., 1986; Gilson et al., 2006; Beeson et al., 2016). However, one of the main difficulties in the investigation of RBC-parasite interactions is that exact receptor-ligand bindings remain largely unknown. Electron microscopy images (Bannister et al., 1986) of merozoites adhered to a RBC suggest that along with short bonds of length $≃20nm$, connecting the two cells, there exist much longer bonds of lengths up to $150⁢nm$, which may play an important role in early stages of merozoite adhesion to the RBC membrane. Furthermore, these long bonds have a much lower density than short bonds. Even though adhesion kinetics of such bonds remain unknown, recent optical tweezers experiments (Crick et al., 2014) indicate the adhesion force of spent merozoites to the RBC membrane to be within the range of 10 to 40pN.

Another important aspect during merozoite alignment is the deformation of the RBC membrane. Dynamic membrane deformations of various magnitudes are often observed (Dvorak et al., 1975; Gilson and Crabb, 2009; Glushakova et al., 2005; Crick et al., 2013) and are thought to aid in the alignment process (Weiss et al., 2015; Hillringhaus et al., 2019). Recent live-cell imaging experiments show a positive correlation between RBC deformations and eventual merozoite alignment (Weiss et al., 2015). Most merozoites that successfully invade RBCs induce considerable membrane deformations, while the invasion success is much less frequent without preceding RBC deformations. Furthermore, these experiments lead to an estimate of an average alignment time of about $16⁢s$ (Weiss et al., 2015). A recent simulation study by Hillringhaus et al., 2019, with RBC-parasite adhesion modeled by a homogeneous interaction potential, has confirmed the importance of membrane deformations, which facilitate parasite alignment through its partial wrapping by the membrane. However, this model shows static (not dynamic) membrane deformations and leads to average alignment times of less than $1⁢s$, indicating that an essential aspect of the alignment process has not been captured. Another speculation is that dynamic membrane deformations are induced actively by merozoites through changing locally the concentration of Ca+ ions (Lew and Tiffert, 2007; McCallum-Deighton and Holder, 1992). This proposition has been confronted by recent experiments (Introini et al., 2018), which show that calcium release by parasite starts only at the invasion stage. Therefore, RBC membrane deformations are potentially induced by a passive mechanism, such as parasite adhesion.

In this paper, we focus on the passive compliance hypothesis (Introini et al., 2018) which assumes that RBC deformations and parasite alignment result from parasite adhesion interactions rather than from some active mechanism. Thus, our central question is whether parasite alignment can be explained purely by the passive compliance hypothesis. In contrast to the recent simulation study by Hillringhaus et al., 2019, where RBC-parasite interactions are represented by a laterally smooth potential, the adhesion model presented here is based on discrete stochastic bonds between parasite and RBC membrane. This is a key step toward a realistic description of RBC-merozoite adhesion, since it eliminates the major shortcomings of the previous potential-based model such as unrealistically fast alignment times and the absence of dynamic membrane deformations. Even though receptor-ligand interactions which determine parasite alignment are largely not known, our bond-based interaction model still incorporates a few experimental details such as the range of adhesion interactions and density of different agonists (Bannister et al., 1986). In particular, bonds of different lengths, that is long and short two-state bond interactions, are employed in the model. The bond-based parasite adhesion model generates an erratic motion of the parasite at the RBC membrane, visually similar to that observed experimentally (Weiss et al., 2015). Furthermore, it results in alignment times which agree quantitatively with those measured in experiments (Weiss et al., 2015; Yahata et al., 2012) and confirms the importance of membrane deformations for successful parasite alignment. The model is also used to investigate the effect of various adhesion parameters, such as bond extensional rigidities and kinetic rates, and ligand densities, on the parasite alignment process. Future investigations with this model can consider more realistic scenarios such as parasite adhesion and alignment under blood flow conditions.

The article is organized as follows. First, we introduce and calibrate our hydrodynamic model, where simulation parameters are tuned to quantitatively match several characteristics of the parasite motion at the RBC membrane from available experimental data by Weiss et al., 2015. Then, RBC membrane deformations and alignment times are investigated for this reference parameter set and several cases of altered bond kinetics and rigidities, and ligand densities. Finally, the effect of membrane stiffness on alignment times is studied.

## Results

The RBC membrane is modeled as a network of $N_{rbc}=3000$ vertices that are distributed uniformly on the membrane surface and connected by $N_{s}$ springs (Gompper and Kroll, 2004; Fedosov et al., 2010a; Fedosov et al., 2010b; Fedosov et al., 2014). Our RBC membrane model incorporates elastic and bending resistance, and its biconcave shape is obtained by constraining the total surface area and enclosed volume of the membrane. Similar to the RBC, a parasite is modeled by $N_{para}=1230$ vertices distributed homogeneously on its surface. The egg-like shape of a merozoite (see Figure 1a) is approximated as (Dasgupta et al., 2014; Hillringhaus et al., 2019)

$$
(r_{x}^{2}+r_{y}^{2}+r_{z}^{2})^{2}=(R_{a}-R_{b})⁢r_{x}⁢(r_{y}^{2}+r_{z}^{2})+R_{a}⁢r_{x}^{3},
$$

where $R_{a}=1.5\mum$ and $R_{b}=1.05\mum$ are diameters along the major and minor axes of the parasite, respectively. The parasite is much less deformable than the RBC, as no deformations of parasite body are visible in experiments (Weiss et al., 2015; Crick et al., 2014). Therefore, the merozoite is considered to be a rigid body, whose dynamics can be described by equations involving force and torque on the parasite’s center of mass and directional vector (Heard, 2006).

![Figure 1.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig1-v2.jpg)

**Figure 1.:** (a) Two-dimensional sketch of a parasite with a directional vector $𝐧$ from the parasite’s back at $r_{x}=1.5\mum$ to its apex at $r_{x}=0$. (b) Three-dimensional triangulated surfaces of a RBC (red) and a parasite (blue). Bonds between the parasite and RBC can form within the contact zone which is illustrated by a magnified view, where discrete receptor-ligand interactions (or bonds) are sketched. A bond can form with a constant on-rate $k_{on}$ and break with a constant off-rate $k_{off}$.

Both RBC and parasite are immersed in a fluid and the hydrodynamic interactions are modeled by the dissipative particle dynamics (DPD) method (Hoogerbrugge and Koelman, 1992; Español and Warren, 1995). The interaction of parasite and RBC membrane has two components. The first component corresponds to an excluded-volume repulsion to prevent an overlap between the two cells, which is modeled by the repulsive part of the Lennard-Jones (LJ) potential with a minimum possible distance $\sigma=0.2\mum$. The distance $\sigma$ can be considered as an effective membrane thickness of a surface constructed from overlapping spheres with a diameter $\sigma$. Generally, $\sigma$ depends on the resolution length of both the RBC membrane and parasite (about $0.2\mum$ in our models) and is chosen large enough to guarantee no artificial membrane intersection or overlap between the cells. The effect of the precise value of $\sigma$ on simulation results is expected to be small and will be discussed later. The second interaction component represents adhesion which is modeled by discrete dynamic bonds between RBC and parasite vertices. Each parasite vertex represents one of the two different types of ligands: (i) long ligands with an effective binding range $ℓ_{eff}^{long}=100nm$ and (ii) short ligands with an effective binding range $ℓ_{eff}^{short}=20nm$. Both ligand types are distributed randomly at the parasite surface with fixed ligand densities $ρ_{long}$ and $ρ_{short}$, such that their sum $ρ_{long}+ρ_{short}$ is equal to the parasite vertex density $ρ_{para}$. Receptors for ligand binding are modeled by RBC vertices, each of which can bind only a single ligand, irrespective of its type. Due to the effective membrane thickness characterized by $\sigma$, long and short bonds can be formed by bound long and short ligands if the distance between RBC and parasite vertices is smaller than $ℓ_{0}+ℓ_{eff}^{long}$ and $ℓ_{0}+ℓ_{eff}^{short}$, respectively, where $ℓ_{0}=2^{1/6}\sigma$ is the equilibrium spring length that corresponds to the cutoff of repulsive interactions. Note that existing bonds are allowed to stretch beyond their effective binding ranges, see section ‘Methods and models’ for more details.

To relate simulation units to physical units, a basic length scale is defined as the effective RBC diameter $D_{0}=\sqrt{A_{0}/\pi}$ ($A_{0}$ is the membrane area), an energy scale as $k_{B}⁢T$, and a time scale as RBC membrane relaxation time $\tau=η⁢D_{0}^{3}/κ$, where $η$ is the fluid viscosity and $κ$ is the bending rigidity of the membrane. All simulation parameters in model and physical units are given in Tables 1 and 2. Average properties of a healthy RBC correspond to $D_{0}≃6.5\mum$ with $A_{0}=133.5\mum^{2}$ (Evans and Skalak, 1980) and $\tau≈0.92s$ for $κ=3\times10^{−19}J$ (Evans, 1983; Fedosov et al., 2010a) and $η=1mPas$.

**Table 1.**
 Simulation parameters given in both model and physical units.The effective RBC diameter $D_{0}=\sqrt{A_{0}/\pi}$ sets a basic length, the thermal energy $k_{B}⁢T$ defines an energy scale, and RBC relaxation time $\tau=η⁢D_{0}^{3}/κ$ sets a time scale in the simulated system, where $A_{0}$ is the RBC surface area, $κ$ is the bending rigidity, and $η$ is the fluid dynamic viscosity. The values of bending rigidity $κ$, 2D shear µ and Young’s $Y$ moduli are chosen such that they correspond to average properties of a healthy RBC. Parameters $\sigma$ and $ϵ$ correspond to RBC-parasite excluded-volume interactions represented by the purely repulsive LJ potential in Equation 11.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Simulation value</th>
      <th>Physical value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A0</td>
      <td>133.5</td>
      <td>133.5μm2</td>
    </tr>
    <tr>
      <td>D0</td>
      <td>A0/π=6.5</td>
      <td>6.5μm</td>
    </tr>
    <tr>
      <td>kB⁢T</td>
      <td>0.01</td>
      <td>4.282×10-21⁢J</td>
    </tr>
    <tr>
      <td>τ</td>
      <td>η⁢D03/κ=725.8</td>
      <td>0.92 s</td>
    </tr>
    <tr>
      <td>η</td>
      <td>1.85</td>
      <td>1×10−3Pas</td>
    </tr>
    <tr>
      <td>κ</td>
      <td>70⁢kB⁢T</td>
      <td>3.0×10-19⁢J</td>
    </tr>
    <tr>
      <td>µ</td>
      <td>4.6×104kBT/D02</td>
      <td>4.8μN/m</td>
    </tr>
    <tr>
      <td>Y</td>
      <td>1.82×105kBT/D02</td>
      <td>18.9μN/m</td>
    </tr>
    <tr>
      <td>Npara</td>
      <td>1230</td>
      <td></td>
    </tr>
    <tr>
      <td>Nrbc</td>
      <td>3000</td>
      <td></td>
    </tr>
    <tr>
      <td>σ</td>
      <td>0.031⁢D0</td>
      <td>0.2μm</td>
    </tr>
    <tr>
      <td>ϵ</td>
      <td>1000⁢kB⁢T</td>
      <td>4.282×10-18⁢J</td>
    </tr>
  </tbody>
</table>

To better understand the effect of various adhesion properties on parasite alignment, several parameters such as bond formation and rupture rates, bond rigidity, and ligand densities are varied. For each fixed parameter set, a number of simulations are performed and the results are combined and/or averaged, which is necessary due to the stochastic nature of bond-based interaction as well as thermal fluctuation effects within the fluid. Note that each simulation is performed for a different random choice of parasite vertices which represent long and short ligands, while their densities remain fixed, see section ‘Methods and models’.

### Calibration of RBC-parasite interactions

A parasite adhered to the RBC membrane exhibits visually an irregular diffusive-like motion observed experimentally (Weiss et al., 2015), which is controlled by the ligand densities $ρ_{long}$ and $ρ_{short}$, bond rigidities $\lambda_{long}$ and $\lambda_{short}$, and the bond formation ($k_{on}^{long}$, $k_{on}^{short}$) and rupture ($k_{off}$) rates that are currently not known. Nevertheless, available experiments (Bannister et al., 1986) suggest that the number of short bonds in RBC-merozoite interaction is lager than the number of long bonds, which is reflected in the ligand densities $ρ_{long}$ and $ρ_{short}$ assumed for our parasite model (see Table 2). To calibrate RBC-parasite interactions, parasite dynamics at the RBC membrane (see Video 1) is quantified by its fixed-time displacement, which is measured by tracking the distance $Δ⁢d$ traveled by the parasite at fixed intervals of time $Δ⁢t$, see Figure 2a. Particle tracking is employed to measure $Δ⁢d$ from available experiments (Weiss et al., 2015), where $Δ⁢t$ is selected to be $1⁢s$, which is the time resolution of the experimental videos. Only time ranges, within which parasites remain visible and the RBC is not moving much, are included in the analysis.

![Figure 2.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig2-v2.jpg)

**Figure 2.:** (a) A time instance of parasite motion at RBC membrane from an experimental video (Weiss et al., 2015) (top) and simulation (bottom), see also Video 1. To obtain the distribution of merozoite fixed-time displacements, the marked parasite (red circle) is tracked over the course of its interaction with the RBC membrane. (b) Comparison between experimental (20 samples) and simulated (100 samples) fixed-time displacements ($Δ⁢d$) of the parasite at RBC membrane, which is normalized by the effective RBC diameter $D_{0}=\sqrt{A_{0}/\pi}$ calculated from the membrane area $A_{0}$. By adapting the interaction parameters, the displacement distribution in simulations is calibrated against the experimental distribution. The resulting reference parameters for our model can be found in Table 2. (c) Mean squared displacement (MSD) of a parasite from simulations as a function of time. The black solid line marks a diffusive regime with $MSD∼t$. Note the subdiffusive dynamics for short times, less than about $1⁢s$.

![Video 1.](https://cdn.elifesciences.org/articles/56500/elife-56500-video1.mp4.jpg)

**Video 1.:** $k_{off}/k_{on}^{long}=2$. See Figure 2a.

**Table 2.**
 List of bond parameters that are used to calibrate displacement of the parasite at the RBC membrane in simulations (see Video 1) against available experimental data (Weiss et al., 2015), as shown in Figure 2b.The parameter values in simulations are given in terms of the length scale $D_{0}$, energy scale $k_{B}⁢T$, and timescale $\tau=η⁢D_{0}^{3}/κ$. The densities of long and short ligands are given in terms of parasite vertex density $ρ_{para}≃270\mum^{−2}$. Note that $ρ_{long}+ρ_{short}=ρ_{para}$ in all simulations.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Simulation value</th>
      <th>Physical value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ℓefflong</td>
      <td>0.0154⁢D0</td>
      <td>100⁢nm</td>
    </tr>
    <tr>
      <td>ℓeffshort</td>
      <td>0.0031⁢D0</td>
      <td>20⁢nm</td>
    </tr>
    <tr>
      <td>ρlong</td>
      <td>0.4 ρpara</td>
      <td>107μm−2</td>
    </tr>
    <tr>
      <td>ρshort</td>
      <td>0.6 ρpara</td>
      <td>161μm−2</td>
    </tr>
    <tr>
      <td>konlong</td>
      <td>36.3⁢τ-1</td>
      <td>39.6s−1</td>
    </tr>
    <tr>
      <td>konshort</td>
      <td>290.3⁢τ-1</td>
      <td>317.0s−1</td>
    </tr>
    <tr>
      <td>koff</td>
      <td>72.58⁢τ-1</td>
      <td>79.2s−1</td>
    </tr>
    <tr>
      <td>λlong</td>
      <td>25.3×105kBT/D02</td>
      <td>0.264⁢pN/nm</td>
    </tr>
    <tr>
      <td>λshort</td>
      <td>8.45×105kBT/D02</td>
      <td>0.0882⁢pN/nm</td>
    </tr>
  </tbody>
</table>

Figure 2b compares experimental and simulated characteristics of fixed-time displacements for the interaction parameters given in Table 2. This set of parameters (further referred to as reference case) is obtained by varying $ρ_{long}$, $ρ_{short}$, $\lambda_{long}$, $\lambda_{short}$, $k_{on}^{short}$, $k_{on}^{long}$, and $k_{off}$ until a good agreement between experimental and simulated parasite displacements is reached. However, the effective binding ranges of long and short ligands remain fixed at $ℓ_{eff}^{long}=100nm$ and $ℓ_{eff}^{short}=20nm$ in this calibration procedure. The variance of experimental displacements in Figure 2b is larger than that in simulations due to a limited sample size of experimental data (20 samples). Note that this set of parameters is likely not unique, and other combinations of the parameters, which result in statistically similar parasite-displacement characteristics, can probably be found.

To further characterize the parasite motion on the RBC membrane, the mean-squared displacement (MSD) of the parasite’s center of mass is computed in simulations and shown in Figure 2c. At long enough times $t≳3$ s, the parasite exhibits diffusive-like motion, indicated by a linear increase of the MSD curve with time. For shorter timescales, the MSD of parasite motion shows a transient anomalous subdiffusion, which may occur, for instance, in the case of sticky particle dynamics with alterations between sticking (i.e., stopping its motion for some time) and diffusing states (Saxton, 2007; Höfling and Franosch, 2013). The transient sticky dynamics is an appropriate description for an adhered parasite, where sticking periods correspond to time intervals within which no bonds are formed or ruptured. The diffusive-like dynamics is governed by the number of bonds $n_{b}$ and their on- and off-rates, as an adhered particle becomes slower and eventually gets arrested when $n_{b}$ is increased and the rates are decreased (Jana and Mognetti, 2019).

### Parasite alignment

Recent experiments suggest that a successful RBC invasion strongly correlates not only with the distance between parasite apex and RBC membrane, but also with a perpendicular alignment of the merozoite toward the cell membrane (Koch and Baum, 2016). Furthermore, the junctional (invasion initiating) interaction range $r_{junc}$ of the parasite’s apex is known to be around $10⁢nm$ (Bannister et al., 1986). Based on these observations, we define two quantities, (i) the apex distance $d_{apex}$ from the RBC membrane, and (ii) the alignment angle $\theta$ that characterizes parasite orientation, both sketched in Figure 3a. Here, $d_{apex}$ is defined as the distance between the parasite apex and the nearest membrane vertex,

$$
d_{apex}=mini(|r_{apex}−r_{i}|),
$$

the alignment angle $\theta$ as the angle between the parasite’s directional vector $𝐧$ and the normal $𝐧^{face}$ of a triangular face whose center is closest to the apex,

$$
\theta=arccos⁡(n⋅n^{face}).
$$

![Figure 3.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig3-v2.jpg)

**Figure 3.:** (a) Sketch of apex distance $d_{apex}$ and alignment angle $\theta$. The apex distance $d_{apex}$ is defined as a distance (magenta line) between the parasite’s apex and the closest vertex of RBC membrane. The alignment angle $\theta$ corresponds to the angle between the parasite’s directional vector (black arrow) and the normal vector $𝐧^{face}$ (green arrow) of a triangular face whose center is closest to the apex. Note that the angle $\pi-\theta$ is drawn in the plot. (b and c) Probability distributions of the apex distance $d_{apex}/D_{0}$ and the alignment angle $\theta/\pi$. Data are obtained for parameters shown in Table 2, and accumulated starting from an initial adhesion contact (i.e., formation of a few bonds). The dashed line in the apex distance distribution indicates the cutoff $2^{1/6}\sigma$ of repulsive LJ interactions. Note that a good parasite alignment requires small values of $d_{apex}/D_{0}$ and values of $\theta/\pi$ close to unity.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Probability distributions of (a) the apex distance $d_{apex}/D_{0}$, and (b) the alignment angle $\theta/\pi$. The dashed line in the apex distance distribution indicates the cutoff $2^{1/6}\sigma$ of repulsive LJ interactions.

Figure 3b,c shows distributions of apex distance $d_{apex}$ and alignment angle $\theta$ for the calibrated RBC-parasite interactions. Both characteristics are represented by distributions as the merozoite is very dynamic at the membrane surface. Minimum values of $d_{apex}$ in Figure 3b correspond to the parasite’s apex being very close to the membrane (i.e., $d_{apex}≈\sigma$), whereas maximum values generally represent a configuration where the parasite is adhered sideways to the RBC. Furthermore, low values of $\theta$ in Figure 3c characterize the sideways adhesion orientation, while large values of $\theta$ represent a good alignment configuration. Note that an ideal merozoite alignment would be achieved if $d_{apex}$ is less than $\sigma+r_{junc}$ ($r_{junc}=10nm$) and the alignment angle is $\theta≈\pi$. Due to a discrete representation of the membrane, perfect alignment is unlikely, which requires to slightly relax these conditions. Therefore, we define a successful parasite alignment by the criteria

$$
d_{apex}\leq2^{1/6}\sigma+r_{junc}&\theta\geq0.8\pi.
$$

The choice of $0.8⁢\pi$ in Equation 4 is also partially driven by the RBC discretization length of about $0.2\mum$. Half circumference of the parasite corresponds to $\piR_{a}/2=2.36\mum$, which is about twelve RBC discretization lengths. This means that our resolution in determining angle $\theta$ is close to $0.1⁢\pi$, so that the window of $0.2⁢\pi$ in the alignment criteria is large enough to avoid strong discretization effects.

In experiments, merozoite alignment times are measured as time intervals between initial parasite adhesion and the beginning of invasion (Weiss et al., 2015). Similarly, alignment time in simulations is calculated as the time required for the parasite to meet the alignment criteria in Equation 4 starting from an initial adhesion contact (i.e., formation of a few bonds). Figure 4b presents a distribution of alignment times from 86 statistically independent DPD simulations for the reference RBC-parasite interactions in Table 2. The alignment times range between $1⁢s$ and $26⁢s$ with an average value of $9.53⁢s$. For comparison, the average alignment time was reported to be $16⁢s$ by Weiss et al., 2015, and the range of alignment times between $7⁢s$ and $44⁢s$ was found by Yahata et al., 2012, which agree reasonably well with our model predictions. Differences in alignment times between simulations and experiments are possibly due to a limited experimental statistics (e.g. only 10 samples in the study by Yahata et al., 2012) and/or selected model parameters, as the distribution of alignment times in our model can be altered by changing RBC-parasite interactions. Therefore, further experiments and possible model improvements are needed to clarify the source of existing differences.

![Figure 4.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig4-v2.jpg)

**Figure 4.:** (a) Two-dimensional probability map as a function of $d_{apex}$ and $\theta$. Each bin represents a single alignment state and the color corresponds to probability of that state. The dark green area ($d_{apex}/D_{0}\leq0.036$ and $\theta/\pi\geq0.8$, compare with Equation 4) represents the criteria for a successful alignment. The black dashed line corresponds to the cutoff $2^{1/6}\sigma$ of repulsive LJ interactions. (b) Distribution of alignment times $t_{a}$ obtained from 86 statistically independent DPD simulations. $t_{a}$ is defined as a time interval starting from an initial adhesive contact (i.e., formation of a few bonds) to the instance when the alignment criteria for $d_{apex}$ and $\theta$ in Equation 4 are met. The average alignment time is equal to $⟨t_{a}⟩≃9.53 s$. (c) Alignment time distribution from MC sampling using the probability map in (a). The alignment time is defined as a number of MC steps needed to satisfy the alignment criteria, as the MC procedure does not have an inherit timescale. Note that the sample size in MC modeling (8000 trajectories) is much larger than that in (b).

Note that the sample size (about 100) in simulations is limited by the computational cost. A single simulation, corresponding to a total physical time of about $26⁢s$, requires approximately 168 core hours on the supercomputer JURECA (Jülich Supercomputing Centre, 2018) at Forschungszentrum Jülich. Therefore, a direct brute-force approach for the investigation of the effect of various parameters on the parasite alignment time is not feasible. To overcome this problem, Monte-Carlo (MC) sampling (see section ‘Methods and models’ for details), which is based on a two-dimensional probability map of parasite alignment characteristics ($d_{apex}$, $\theta$) illustrated in Figure 4a, is employed to determine the differences in alignment times for various parameter sets. Such a probability map is computed from several direct DPD simulations of RBC-parasite adhesive interactions. Then, the MC procedure is used to model stochastic jumps between neighboring alignment states ($d_{apex}^{i}$, $\theta^{j}$) within the probability map, starting from a randomly selected initial state and continuing until the alignment criteria in Equation 4 are met, and the number of MC steps represents the alignment time. Distribution of alignment times $t_{n}$ from the MC sampling is shown in Figure 4c for the reference parameter set. Clearly, the distributions obtained by direct (Figure 4b) and MC (Figure 4c) simulations are very similar, verifying the reliability of the MC approach. Note that alignment times $t_{n}$ from MC sampling are measured in terms of MC steps, since MC simulations do not have an intrinsic timescale. The average alignment time for the reference parameter set is denoted as $⟨t_{n,ref}⟩$ and assumed to be equivalent to $9.53⁢s$, the average alignment time from direct DPD simulations of RBC-parasite adhesion. This implies that 104 MC steps correspond to about $15⁢s$.

### Membrane deformation and parasite dynamics

A recent simulation study by Hillringhaus et al., 2019 with a laterally homogeneous adhesion potential has demonstrated that the deformation of RBC membrane is crucial for a successful parasite alignment. Further, we show that ligand density, bond rigidity and kinetics not only control the parasite motion at the membrane surface, but also directly affect membrane deformation. To quantify the strength of membrane deformations, a change in total energy between the deformed state and the equilibrium state of the RBC membrane is computed as (Hillringhaus et al., 2019)

$$
Δ⁢E_{rbc}=E_{rbc}^{deform}-E_{rbc}^{equil}.
$$

Figure 5 shows temporal changes in deformation energy, number of bonds, head distance, and alignment angle for the reference case. Two major contributions to the deformation energy (i.e. elastic stretching $Δ⁢E_{sp}$ and bending $Δ⁢E_{bend}$ energies) indicate that membrane deformation is very dynamic and has a strong variability in its intensity. This is due to the dynamic formation and dissociation of long and short bonds between the merozoite and RBC membrane.

![Figure 5.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig5-v2.jpg)

**Figure 5.:** Variations in stretching $Δ⁢E_{sp}$ and bending $Δ⁢E_{bend}$ energies, the number of bonds $n_{b}$, the head distance $d_{apex}$, and the alignment angle $\theta$ as a function of time for the default parameter set given in Table 2.Temporal changes in the number of bonds are shown for both long and short bond types. The dashed lines in the bottom plot correspond to the alignment criteria in Equation 4. For all quantities, the corresponding averages and variances represented by box plots are depicted on the right.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (a) Average total number of bonds between the merozoite and RBC as a function of the distance $d_{cm}$ between their centers of mass. (b) Illustration of parasite adhesion at the RBC rim (marked by I) and in the dimple (II). The parasite forms more bonds in the dimples (position II) than at the RBC rim (position I).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Different alignment characteristics, including (a) deformation energy, (b) number of bonds, (c) apex distance, (d) alignment angle, and (e) fixed-time displacement, for several values of parameter $\sigma$ which determines the effective membrane thickness.

An interesting observation is that the head distance and alignment angle in Figure 5 fluctuate around some average values, indicating that the parasite has a preferred orientation, which is consistent with a peak in the probability map in Figure 4a. To assess whether the most likely values of $d_{apex}$ and $\theta$ are mainly determined by the egg-like parasite shape, or also depend on the mechanical properties of the membrane, $d_{apex}$ and $\theta$ distributions in Figure 3 for a deformable RBC are compared with those for the parasite adhered to a rigidified membrane (see section ‘Effect of RBC rigidity’) in Figure 3—figure supplement 1. Clearly, in the case of a rigid membrane, the preferred $d_{apex}$ and $\theta$ values are determined by the egg-like parasite shape, corresponding to a configuration with maximum adhesion area. In comparison to the deformable membrane (Figure 3), the peak in $d_{apex}$ for the rigid RBC (see Figure 3—figure supplement 1) is shifted further away from zero. This indicates that the degree of wrapping has a significant effect on the preferred values of $d_{apex}$ and $\theta$. Therefore, in addition to the egg-like parasite shape, RBC membrane properties, such as bending rigidity, shear elasticity, and local curvature, affect the most probable values of $d_{apex}$ and $\theta$. Furthermore, the fluctuations of $d_{apex}$ and $\theta$ from their average values in Figure 5 represent parasite motion toward its apex or bottom due to stochastic bond dynamics. Thus, the parasite dynamics at the membrane can be described as a superposition of the rolling motion around its directional vector with a preferred orientation and intermediate fluctuations of parasite orientation toward its apex or the bottom. The rotational motion around the directional vector is preferred because it is not associated with a significant energy cost, while fluctuations in the orientation toward the merozoite’s apex or bottom have an energy penalty.

A further noteworthy result from simulations is that a successful alignment occurs more frequently in the concave areas of RBC dimples than at the convex rim of the membrane. This is due to the fact that the cell dimples have a favorable local curvature or a lower energy penalty for membrane wrapping (Agudo-Canalejo and Lipowsky, 2015; Yu et al., 2018), which leads to a stronger parasite wrapping by the membrane, and thus a larger probability for successful alignment. Figure 5—figure supplement 1 shows that the merozoite forms more bonds in the dimples than at the RBC rim, confirming the position-dependent differences in membrane wrapping. Furthermore, our simulations show that merozoites move frequently into the dimple areas, starting from the initial rim contact, and remain there for the majority of simulation time. This behavior is again due to a more energetically favorable adhesion position within RBC dimples in comparison to the RBC rim. Energetically favorable parasite wrapping within the RBC dimples might be also advantageous for the subsequent entry into the cell.

The dynamic adhesive behavior of the parasite in the current stochastic bond-based model is in striking contrast to the previous adhesion model (Hillringhaus et al., 2019) based on a homogeneous interaction potential between the two cells, where no dynamic deformations were observed. A qualitative correspondence between these two models can be understood by considering a ratio $k_{on}/k_{off}=exp⁡(Δ⁢U_{b}/k_{B}⁢T)$, where $Δ⁢U_{b}$ is the binding energy of a single bond (Bell, 1978; Schwarz and Safran, 2013). Thus, the ratio $k_{on}/k_{off}$ directly controls the average number of bonds $⟨n_{b}⟩$ and the strength of adhesion (see section ‘Effect of bond properties on parasite alignment’), which are correlated with RBC deformation energy $Δ⁢E_{rbc}$. Similarly, in the parasite adhesion model with a homogeneous interaction potential (Hillringhaus et al., 2019), the strength of adhesion potential controls membrane deformations. Even though average membrane deformations can be compared for these two models, the stochastic bond-based adhesion model results in a very different diffusive-like dynamics of the parasite, which is governed by $n_{b}$ and the off-rate $k_{off}$ (Jana and Mognetti, 2019). A significant increase of $n_{b}$ and/or a decrease of $k_{off}$ would lead eventually to parasite arrest (see section ‘Effect of bond properties on parasite alignment’), which can be compared well with the model based on a homogeneous interaction potential (Hillringhaus et al., 2019).

There exist three different timescales which might be relevant for the parasite alignment: (i) bond lifetime $\tau_{b}≃1/k_{off}$, (ii) membrane deformation time on the scale of parasite size $\tau_{p}≃η⁢R_{a}^{3}/κ$, and (iii) rotational diffusion time of the parasite $\tau_{r}≃8⁢\pi⁢η⁢R_{a}^{3}/k_{B}⁢T$. These characteristic times are $\tau_{b}≈0.013s$, $\tau_{p}≈0.011s$, and $\tau_{r}≈20s$ computed from the model parameters given in Tables 1 and 2. There is a clear separation of timescales between $\tau_{r}$ and both $\tau_{b}$ and $\tau_{p}$, indicating that the rotational diffusion of the parasite is too slow to have a significant effect on merozoite alignment. Furthermore, $\tau_{b}$ and $\tau_{p}$ are comparable in magnitude, suggesting that both bond dynamics and membrane deformations are important for the alignment process. It is also interesting to note that the ratio $\tau_{p}/\tau_{r}=k_{B}⁢T/(8⁢\pi⁢κ)≈6\times10^{-4}$ depends only on the bending rigidity $κ$. This means that membrane deformation will always represent a dominating timescale over the rotational diffusion of the parasite, independently of the parasite size and the viscosity of suspending medium.

After the detailed analysis of parasite alignment, let us consider a possible influence of the effective membrane thickness, characterized by $\sigma$, on merozoite alignment. Figure 5—figure supplement 2 presents various alignment characteristics for $\sigma=0.15\mum$ and $\sigma=0.3\mum$ in comparison with the original choice of $\sigma=0.2\mum$. The simulation results indicate that the $\sigma$ value may affect the number of bonds between the RBC and parasite, and thus the degree of membrane wrapping. This result is not entirely surprising, as $\sigma$ also affects the binding range defined as $2^{1/6}\sigma+ℓ_{eff}^{long}$ and $2^{1/6}\sigma+ℓ_{eff}^{short}$ for long and short ligands, respectively. However, differences in alignment results are rather small for $\sigma=0.15\mum$ and $\sigma=0.2\mum$, indicating that the choice for small enough $\sigma$ we made is appropriate. The case with $\sigma=0.3\mum$ exhibits a larger number of bonds and stronger membrane deformations than for $\sigma=0.2\mum$. Finally, note that fixed-time displacement characteristics of the parasite in Figure 5—figure supplement 2 remain nearly unaffected by the $\sigma$ value, because dynamical properties of the merozoite are mainly determined by the bond off-rate, see the next section.

### Effect of bond properties on parasite alignment

To better understand the dependence of merozoite alignment on bond kinetics, the off-rate $k_{off}$ is varied for two ratios $k_{on}^{short}/k_{on}^{long}$ of short and long bond on-rates. Figure 6 presents the parasite’s fixed-time displacement, deformation energy, and average alignment times as a function of $k_{off}/k_{on}^{long}$. A lower ratio of $k_{off}/k_{on}^{long}$ (i.e. a lower $k_{off}$) leads to stronger adhesion and thereby stronger membrane deformations (see Figure 6b and Video 2), consistently with the number of bonds shown in Figure 6—figure supplement 1. For small $k_{off}/k_{on}^{long}$ values, membrane deformation energies can reach up to $2000k_{B}T$, whereas large values of $k_{off}$ result in $ΔE_{rbc}≈100k_{B}T$. The main reason is that low values of $k_{off}$ lead to a significant increase in the lifetime of individual bonds, allowing the parasite to form more bonds and thereby increase its adhesion energy and induce larger membrane deformations. Similarly, large values of $k_{off}$ decrease the bond lifetime, resulting in a decrease in the adhesion energy. For instance, in case of $k_{off}/k_{on}^{long}=0.5$, the parasite forms on average about 200 bonds, whereas for $k_{off}/k_{on}^{long}=4$, the average number of bonds is approximately 15 (see Figure 6—figure supplement 1). Furthermore, a larger on-rate for the short bonds yields a slight increase in the strength of membrane deformations in comparison to a smaller $k_{on}^{short}$.

![Figure 6.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig6-v2.jpg)

**Figure 6.:** Effect of the off-rate $k_{off}$ on (a) the parasite’s fixed-time displacement, (b) RBC deformation energy, and (c) alignment time.Since the off-rate controls the lifetime of bonds, a smaller off-rate results in a stronger adhesion, a lower parasite displacement, and a faster alignment time.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Effect of the off-rate $k_{off}$ on (a) the apex distance, (b) alignment angle, and (c) the number of bonds.

![Video 2.](https://cdn.elifesciences.org/articles/56500/elife-56500-video2.mp4.jpg)

**Video 2.:** Parasite adhesion and dynamics on a deformable RBC for a reduced off-rate $k_{off}$.$k_{off}/k_{on}^{long}=1$.

Figure 6b,c shows that there is a clear correlation between the level of membrane deformations and average alignment time. For example, for off-rates $k_{off}/k_{on}^{long}\leq2$, the alignment times are comparable with those for the reference parameter case, while for off-rates $k_{off}/k_{on}^{long}>2$, there is a strong increase in alignment times, which is correlated with insignificant membrane deformations. A shorter alignment time for $k_{off}/k_{on}^{long}\leq2$ is due to the partial wrapping of the parasite by the RBC membrane, which is consistent with the previous study by Hillringhaus et al., 2019 that demonstrates the importance of membrane deformation for merozoite alignment. Note that the fixed-time displacement $Δ⁢d$ in Figure 6a significantly increases with $k_{off}$ due to a weaker adhesion. This seems to imply that the parasite alignment may proceed faster for $k_{off}/k_{on}^{long}>2$. However, as it is evident from Figure 6c, this simple expectation is not applicable here, indicating that a faster motion of the parasite at the RBC surface may not necessarily result in a faster alignment. Alignment times for $k_{on}^{short}/k_{on}^{long}=8$ are generally shorter than for $k_{on}^{short}/k_{on}^{long}=4$ because of a slightly stronger parasite wrapping by the membrane. A seemingly opposite result for $k_{off}/k_{on}^{long}=0.5$ in Figure 6c is likely due to insufficient statistics in the probability maps used for MC sampling, as they are constructed based on several direct simulations. Accurate resolution of small differences in alignment times is challenging, as it requires a large number of direct simulations.

Another bond parameter, which may affect parasite alignment, is the extensional rigidities of both bond types. Figure 7 presents RBC deformation energy and the number of bonds for five times softer and stiffer bonds than those in the reference case. Bonds with a larger rigidity lead to the formation of a larger number of bonds, more membrane wrapping, and a larger RBC deformation energy in comparison to soft bonds. The physical mechanism is that stiffer bonds facilitate a smaller distance between the membrane and the parasite at the edge of adhesion area between them, which favors further wrapping by the formation of additional bonds. Therefore, the spring rigidity in our model can mediate distance-limited bond formation at the edge of adhesion area between the parasite and the membrane, which affects merozoite alignment (see Figure 7—figure supplement 1), and is connected to membrane bending rigidity and the degree of wrapping. Consistently, simulations of the merozoite on a rigid RBC show no effect of the bond extensional rigidities on parasite alignment, because no significant membrane deformations are induced by parasite adhesion.

![Figure 7.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig7-v2.jpg)

**Figure 7.:** (a) RBC deformation energy and (b) the number of short and long bonds as a function of $\lambda/\lambda_{ref}$. $\lambda_{r⁢e⁢f}$ corresponds to the reference case with parameters given in Table 2. Note that both $\lambda_{long}$ and $\lambda_{short}$ are changed by the same factor with respect to their $\lambda_{r⁢e⁢f}$ values. Here, the bond kinetic rates are $k_{on}^{short}=290.3⁢\tau^{-1}$, $k_{on}^{long}=36.3⁢\tau^{-1}$, and $k_{off}=72.6⁢\tau^{-1}$.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig7-figsupp1-v2.jpg)

Furthermore, we consider effect of the density of long ligands $ρ_{long}$ on parasite alignment. For the reference parameter set, $ρ_{long}$ is chosen to be $ρ_{long}/ρ_{para}=0.4$, so that $ρ_{short}/ρ_{para}=0.6$. Figure 8 presents the number of short and long bonds as well as parasite alignment times as a function of $ρ_{long}/ρ_{para}$. Interestingly, the number of short bonds increases with increasing $ρ_{long}$, even though the density of short ligands $ρ_{short}$ decreases. This occurs due to the fact that more long bonds further stabilize parasite adhesion, allowing the formation of more short bonds. Note that for the density $ρ_{long}/ρ_{para}=0.1$ in Figure 8b, the value of $⟨t_{n}⟩$ is omitted, as the alignment criteria in Equation 4 have not successfully been met during the entire course of direct simulations, yielding the probability of parasite alignment in MC sampling to be zero. For ligand densities $ρ_{long}/ρ_{para}\geq0.3$, both bond numbers and alignment times remain nearly independent of $ρ_{long}$. However, the average alignment time for $ρ_{long}/ρ_{para}=0.2$ is about $30⁢s$ which is roughly three times longer than for the reference case. Note that $30⁢s$ is longer than the total length ($≈26s$) of direct simulations. Nevertheless, parasite alignment has occurred in some of these simulations, resulting in a small non-zero probability of merozoite alignment and a relatively long $⟨t_{n}⟩$ calculated through the MC sampling. The fact that $⟨t_{n}⟩$ for $ρ_{long}/ρ_{para}=0.2$ is longer than the total time of direct simulations means that the probability of parasite alignment is likely overestimated, indicating that the average alignment time should be even longer than $30⁢s$. An increase of $⟨t_{n}⟩$ with decreasing values of $ρ_{long}$ is consistent with a significant decrease in membrane deformations (see Figure 8—figure supplement 1). For off-rates $k_{off}<72.6⁢\tau^{-1}$, the trends illustrated in Figure 8 remain qualitatively the same.

![Figure 8.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig8-v2.jpg)

**Figure 8.:** Effect of the density of long ligands $ρ_{long}$ on parasite alignment.(a) Number of short and long bonds and (b) parasite alignment times as a function of $ρ_{long}/ρ_{para}$. Note that $ρ_{long}+ρ_{short}=ρ_{para}$ remains constant in all simulations. Here, the bond kinetic rates are $k_{on}^{short}=290.3⁢\tau^{-1}$, $k_{on}^{long}=36.3⁢\tau^{-1}$, and $k_{off}=72.6⁢\tau^{-1}$. In case of $ρ_{long}/ρ_{para}=0.1$, parasite alignment time could not be computed through the MC sampling, since merozoite alignment has never occurred in direct simulations.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** Effect of the density of long ligands $ρ_{long}$ on (a) deformation energy, (b) fixed-time displacement, (c) apex distance, and (d) alignment angle.

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig8-figsupp2-v2.jpg)

**Figure 8—figure supplement 2.:** Alignment results of simulations with only long ligands, i.e. for $ρ_{long}/ρ_{para}=1$.(a) Deformation energy, (b) the number of bonds, (c) apex distance, (d) alignment angle, and (e) fixed-time displacement of the merozoite for the three cases: (1) $ρ_{long}/ρ_{para}=1$ and $k_{off}/k_{on}^{long}=2$, (2) $ρ_{long}/ρ_{para}=0.4$ and $k_{off}/k_{on}^{long}=2$ (the reference case), (3) $ρ_{long}/ρ_{para}=1$ and $k_{off}/k_{on}^{long}=0.25$.

The importance of different ligand densities discussed above triggers the question whether both ligand types are necessary. Simulations performed with only short ligands (i.e., $ρ_{short}/ρ_{para}=1$) for several different $k_{off}$ rates show that the parasite is not able to achieve significant wrapping by the membrane, because such ligands are too short to facilitate progressive membrane attachment over a curved parasite surface. This limitation is directly connected to the density of available receptors on the RBC surface, which is determined in our model by the membrane resolution. For the same reason, parasite mobility is impaired, as it is largely mediated by bond formation/dissociation at the edge of adhesion area between the parasite and the membrane. Therefore, the model with only short ligands does not reproduce proper parasite alignment. Simulations performed with only long ligands (i.e., $ρ_{long}/ρ_{para}=1$) show that the parasite mobility and alignment can be well reproduced, see Figure 8—figure supplement 2. Thus, the presence of long bonds aids in the stabilization of merozoite adhesion and the enhancement of parasite motion, such that long bonds serve as some sort of effective leverages. Theoretically, a model with only long ligands would be sufficient to reproduce the proper parasite alignment; however, current biomolecular knowledge about parasite coating does not support the presence of many bonds with a length of about $100⁢nm$. We speculate that short bonds are necessary (i) to stabilize parasite adhesion, as the density of long ligands is likely low, and (ii) to bring the two cells in sufficiently close contact (about $10⁢nm$) to facilitate the formation of a tight junction required for invasion. Thus, the presence of both ligand types is likely necessary for a successful invasion.

### Effect of RBC rigidity

To investigate the effect of RBC rigidity on the alignment of a merozoite, we consider a nearly rigid cell membrane by increasing both bending rigidity and Young’s modulus by two orders of magnitude in comparison to a healthy RBC. Such a rigid RBC shows no significant membrane deformations for the reference interaction parameters given in Table 2, see Video 3. Comparison of parasite fixed-time displacements and alignment times for flexible and rigid membranes is shown in Figure 9 for two different values of $k_{off}$. Clearly, larger RBC rigidity leads to much longer parasite alignment times (see Figure 9b), emphasizing again the importance of membrane deformations for merozoite alignment. For off-rates $k_{off}/k_{on}^{long}<2$, parasite alignment at the surface of a rigid RBC is not achieved within the course of the simulation. As the off-rate increases, alignment time at the rigid membrane becomes comparable with that for the flexible membrane, because large enough $k_{off}$ values do not result in strong membrane deformations even for the flexible RBC. Thus, for large off-rates, the parasite’s alignment solely relies on its rotational dynamics controlled by the bond kinetic rates.

![Figure 9.](https://cdn.elifesciences.org/articles/56500/elife-56500-fig9-v2.jpg)

**Figure 9.:** Effect of RBC membrane rigidity on (a) alignment time and (b) parasite fixed-time displacement for different off-rates $k_{off}$.Note that for a rigid RBC with $k_{off}/k_{on}^{long}=1$, parasite alignment time could not be computed through the MC sampling, as the alignment criteria have never been met in direct simulations.

![Video 3.](https://cdn.elifesciences.org/articles/56500/elife-56500-video3.mp4.jpg)

**Video 3.:** $k_{off}/k_{on}^{long}=2$.

Figure 9a presents a comparison of parasite fixed-time displacements at the flexible and rigid membranes. In both cases, parasite displacements increase with increasing $k_{off}$, as expected. However, the displacement at the rigid membrane is larger than at the flexible membrane (for visual comparison, see Videos 1 and 3), because the merozoite forms less bonds at the rigid surface. For the same reason, the variance of parasite displacements is larger for the rigid RBC than for the flexible RBC. Note that an increase in $k_{off}$ results in an increase of fixed-time displacement and a decrease of alignment time for the rigid membrane, whereas for flexible RBC, an increase in off-rate leads to an elevation of both fixed-time displacement and alignment time. This implies that for a rigid RBC, fast kinetics or weak adhesion are favorable for a quick alignment. In contrast, for a flexible RBC, slow kinetics or strong adhesion are advantageous for fast alignment, since the parasite employs RBC deformation for efficient alignment by partial membrane wrapping.

## Discussion and conclusions

We have investigated the alignment of a merozoite at RBC membrane using a realistic two-state bond-dynamics model for parasite adhesion. Motivated by experiments (Bannister et al., 1986), parasite adhesion is modeled by two bond types, with long and short binding ranges. Since RBC-parasite interactions and the corresponding bond properties are experimentally not yet well characterized, the calibration of bond parameters is based on parasite fixed-time displacement at the membrane from existing experiments (Weiss et al., 2015), which is in the range of $0.3−0.8\mum$. The presented model is able to reproduce quantitatively experimentally measured alignment times. Simulated alignment times are in the range between a few seconds and $26⁢s$, while the analysis of experimental videos by Weiss et al., 2015 yields an average alignment time of $16⁢s$. Another independent experimental study by Yahata et al., 2012 reports alignment times in the range between 7 and $44⁢s$, which agree relatively well with our simulation predictions. In addition to the good agreement between simulated and experimental alignment times, our model reproduces well dynamic RBC membrane deformations frequently observed in experiments (Dvorak et al., 1975; Gilson and Crabb, 2009; Crick et al., 2013).

Our main result is that parasite alignment is mediated by RBC membrane deformations and a diffusive-like dynamics due to the stochastic nature of parasite-membrane interactions. Average number of bonds $⟨n_{b}⟩$ between the parasite and the membrane is governed by the ratio $k_{on}/k_{off}=exp⁡(Δ⁢U_{b}/k_{B}⁢T)$ that is connected to the binding energy $Δ⁢U_{b}$ of a single bond and determines the strength of membrane deformations. Our results show that membrane deformations speed up the alignment through partial wrapping of the parasite, facilitating a contact between the parasite apex and the membrane. This conclusion is consistent with the previous simulation study (Hillringhaus et al., 2019), where merozoite adhesion has been modeled by a laterally homogeneous interaction potential whose strength controls RBC deformations. The importance of membrane deformation is also corroborated by simulations of parasite alignment at a rigid RBC, which show a drastic increase in alignment times. For a rigid membrane, the parasite alignment depends mainly on bond lifetime (i.e., $\tau_{b}≃1/k_{off}$), indicating that a low $k_{off}$ or large bond lifetime may significantly decelerate the parasite’s rotational motion, and hence, increase its alignment time drastically. This conclusion agrees well with a recent simulation study (Jana and Mognetti, 2019) on the dynamics of two adhered colloids, whose effective rotational diffusion is governed not only by $⟨n_{b}⟩$ but also by $\tau_{b}$. Clearly, $\tau_{b}$ is also important for parasite dynamics at a deformable RBC, in addition to the membrane relaxation time $\tau_{p}$ on the scale of parasite size. The poor alignment of the merozoite at a stiff membrane can be a contributing factor, limiting parasite invasion. For example, infected RBCs in malaria become significantly stiffer than healthy cells (Suresh et al., 2005; Fedosov et al., 2011), limiting secondary invasion events. Furthermore, an increased RBC membrane stiffness is relevant in many other diseases, such as sickle cell anemia (Barabino et al., 2010), thalassemia (Peters et al., 2011), and stomatocytosis (Caulier et al., 2018), whose carriers are generally less susceptible to malaria infection.

For large values of $k_{off}$, the parasite is not able to induce strong deformations even at a flexible membrane, so that the alignment times at rigid and deformable RBCs become comparable, and the alignment is governed solely by a diffusive-like rotational dynamics. The diffusive-like motion of the parasite at the membrane surface is facilitated by stochastic formation/dissociation of bonds between the two cell surfaces, and leads occasionally to a successful alignment. Therefore, our model is also able to explain the possibility of RBC invasion by a merozoite without preceding membrane deformations, which is observed much less frequently than the invasion preceded by significant RBC deformations (Weiss et al., 2015). Note that the RBC-parasite adhesion model based on a laterally homogeneous interaction potential (Hillringhaus et al., 2019) predicts the complete failure of parasite alignment without significant membrane deformations, because it does not capture a diffusive-like rotational dynamics of the parasite. Thus, the bond-based model is more appropriate for the representation of RBC-parasite interactions.

Even though the bond parameters in Table 2 were calibrated by the parasite fixed-time displacement obtained from experiments (Weiss et al., 2015), such a choice is likely not unique as some other set of parameters (e.g., receptor and ligand densities, bond rigidities and kinetic rates) may lead to statistically similar displacement characteristics. Nevertheless, it is important to emphasize that the discrete bonds in simulations should be thought of as ‘effective’ bonds, which likely represent a small cluster of real molecular bindings. Furthermore, since the parasite displacement is mainly controlled by the bond kinetics, this calibration procedure is rather robust in identifying an appropriate range of bond properties. Another important aspect of this model is the necessity of sufficiently long ligands and bonds to facilitate dynamic motion of the parasite at RBC surface. Simulations with only short ligands show that the parasite fails to induce significant wrapping by the membrane, leading to very little alignment success. Therefore, the long bonds serve as leverages for stable parasite adhesion and its motion at the membrane. Even though simulations with only long ligands indicate that a proper alignment can be achieved in this case, the existence of a dense population of long bonds has currently no support experimentally. Furthermore, we hypothesize that short enough bonds are necessary to enable the formation of a tight junction for parasite invasion, which requires a contact distance of about $10⁢nm$ between the two cells. Thus, our simulations suggest that both ligand types are likely necessary.

Electron microscopy images of adhered parasites (Bannister et al., 1986) suggest that the density of long bonds can be as low as 5 - 10%. However, the density of long ligands and bonds in our simulations is limited by the resolution of both the RBC and parasite to be larger than about 20%. A much finer membrane model would alleviate this limitation, but it would be prohibitively expensive computationally. Note that such heterogeneous receptor-ligand interactions exist in other biological systems as well. For example, during leukocyte binding in the microvasculature, both selectin and integrin molecules participate in adhesion and work synergistically, even though they have distinct functions (Ley et al., 2007). Furthermore, infected RBCs in malaria adhere to endothelial cells via two distinct receptors, ICAM-1 and CD-36, where binding with ICAM-1 exhibits a catch-like bond, while the interaction with CD-36 is a slip-like bond (Lim et al., 2017).

Several studies (Cowman et al., 2012; Dasgupta et al., 2014; Singh et al., 2010) about RBC-parasite interactions hypothesize the existence of an adhesion gradient along the parasite body, which is expected to facilitate alignment. Based on the RBC-parasite adhesion model with a laterally homogeneous interaction potential (Hillringhaus et al., 2019), it was shown that an adhesion gradient, where the potential strength increases toward the apex of a merozoite, generally accelerates parasite alignment. No definite conclusions about possible gradients can be made in the context of that model, because even in the case of no adhesion gradients, it predicts very short alignment times of about two orders of magnitude smaller than measured experimentally. An introduction of adhesion gradients in our bond-based interaction model leads qualitatively to the following conclusions: (i) Weak adhesion gradients do not significantly disturb the irregular motion of a parasite at RBC membrane, and have a negligible effect on the alignment. (ii) Strong adhesion gradients often result in a controlled direct re-orientation of the parasite toward its apex, suppressing the irregular motion observed experimentally. These preliminary results do not permit a definite conclusion about the possible existence of adhesion gradients, as moderate adhesion gradients may exist and aid partially in the alignment process. Nevertheless, our model shows that adhesion gradients are not necessary, since the main parasite properties, such as dynamic motion and realistic alignment times, can be reproduced well by the bond-based model without adhesion gradients.

In conclusion, our model suggests that the parasite alignment can be explained by the passive compliance hypothesis (Introini et al., 2018; Hillringhaus et al., 2019), such that no additional active mechanisms or processes are necessary. Of course, this does not eliminate the possible existence of some active mechanisms, which may participate in the alignment process. Another limitation of many studies is that the parasite alignment is investigated under static (no flow) conditions, whereas in vivo, parasite alignment and invasion occur under a variety of blood flow conditions, including different flow stresses and flow-induced RBC deformations (Lanotte et al., 2016). Further experiments are needed to investigate RBC-parasite interactions for realistic blood-flow scenarios. The bond-based model proposed here is expected to be useful for the quantification of such experimental studies and for a better understanding of RBC-parasite adhesion under blood flow conditions.

## Model and methods

### Red blood cell model

The total potential energy of the RBC model is given by Fedosov et al., 2010a; Fedosov et al., 2010b

$$
U_{rbc}=U_{sp}+U_{bend}+U_{area}+U_{vol}.
$$

Here, the term $U_{sp}$ represents the elasticity of spectrin network, which is attached to the back side of the lipid membrane. $U_{bend}$ models the resistance of the lipid bilayer to bending. $U_{area}$ and $U_{vol}$ constrain the area and volume of RBC membrane, mimicking incompressibility of the lipid bilayer and the cytosol, respectively.

The elastic energy term $U_{sp}$ is given by

$$
U_{sp}=\sumi=1N_{s}\frac{k_{B}⁢T⁢ℓ_{i}^{max}⁢(3⁢x_{i}^{2}-2⁢x_{i}^{3})}{4⁢p_{i}⁢(1-x_{i})}+\frac{\lambda_{i}}{ℓ_{i}},
$$

where the first term is the attractive worm-like chain potential, while the second term corresponds to a repulsive potential with a strength $\lambda_{i}$. Furthermore, $ℓ_{i}$ is the length of the i-th spring, $p_{i}$ is the persistence length, $ℓ_{i}^{max}$ is the maximum extension, and $x_{i}=ℓ_{i}/ℓ_{i}^{max}$. The stress-free state of the elastic network is considered to be a biconcave RBC shape, such that initial lengths in the triangulation of this shape define equilibrium spring lengths $l_{i}^{0}$. For a regular hexagonal network, its two-dimensional (2D) shear modulus µ can be derived in terms of model parameters as (Fedosov et al., 2010a; Fedosov et al., 2010b)

$$
\mu=\frac{\sqrt{3}⁢k_{B}⁢T}{4⁢p_{i}⁢ℓ_{i}^{0}}⁢(\frac{x¯}{2⁢(1-x¯)^{3}}-\frac{1}{4⁢(1-x¯)^{2}}+\frac{1}{4})+\frac{3⁢\sqrt{3}⁢\lambda_{i}}{4⁢(ℓ_{i}^{0})^{3}},
$$

where $x¯=ℓ_{i}^{0}/ℓ_{i}^{max}$ is a constant for all $i$. Thus, for given values of µ, $x¯$, and $ℓ_{i}^{0}$, individual spring parameters $p_{i}$ and $\lambda_{i}$ are calculated by using Equation 8 and the force balance $∂U_{sp}/∂l_{i}|_{l_{i}^{0}}=0$ for each spring.

The bending energy of the membrane is expressed as (Gompper and Kroll, 1996; Gompper and Kroll, 2004)

$$
U_{bend}=\frac{κ}{2}⁢\sumi=1N_{rbc}\frac{1}{\sigma_{i}}⁢[𝐧_{i}^{rbc}⋅(\sumj⁢(i)\frac{\sigma_{i⁢j}}{r_{i⁢j}}⁢𝐫_{i⁢j})]^{2}
$$

where $κ$ is the bending modulus, $𝐧_{i}^{rbc}$ is a unit normal of the membrane at vertex $i$, $\sigma_{i}=(\sum_{j⁢(i)}\sigma_{i⁢j}⁢r_{i⁢j})/4$ is the area of dual cell of vertex $i$, and $\sigma_{i⁢j}=r_{i⁢j}⁢[cot⁡(\theta_{1})+cot⁡(\theta_{2})]/2$ is the length of the bond in dual lattice, with the two angles $\theta_{1}$ and $\theta_{2}$ opposite to the shared bond $𝐫_{i⁢j}$.

The last two terms in Equation 6,

$$
U_{area}=\frac{k_{a}(A−A_{0})^{2}}{2A_{0}}+\sumi=1N_{t}\frac{k_{ℓ}(A_{i}−A_{i}^{0})^{2}}{2A_{i}^{0}},U_{vol}=\frac{k_{v}(V−V_{0})^{2}}{2V_{0}},
$$

constrain surface area and volume of the RBC (Fedosov et al., 2010a; Fedosov et al., 2010b), where $k_{a}$ and $k_{ℓ}$ control the total surface area $A$ and local areas $A_{i}$ of each triangle to be close to desired total area $A_{0}$ and local areas $A_{i}^{0}$, respectively. The coefficient $k_{v}$ controls the total volume $V$ of the cell. The values of these coefficients are chosen large enough such that the area and volume fluctuate within 1% of the desired values.

The elasticity of a healthy RBC is characterized by the 2D shear modulus $\mu≈4.8\muNm^{−1}$, which corresponds to the 2D Young’s modulus $Y≈18.9\muNm^{−1}$ for a nearly incompressible membrane (Suresh et al., 2005; Fedosov et al., 2010a). These values are employed in all simulations unless stated otherwise. The described membrane model has been shown to accurately capture RBC mechanics (Fedosov et al., 2010a; Fedosov et al., 2010b) and membrane fluctuations (Turlier et al., 2016).

### RBC-parasite adhesion interaction

Interaction between parasite and RBC membrane has two components. The first part imposes excluded-volume interactions between the RBC and merozoite (i.e. no overlap between them), using the purely repulsive part of the Lennard-Jones (LJ) potential

$$
U_{rep}(r)=4ϵ[(\frac{\sigma}{r})^{12}−(\frac{\sigma}{r})^{6}],r\leq2^{1/6}\sigma.
$$

This potential acts between every pair of RBC and parasite vertices separated by a distance $r=|𝐫_{rbc}-𝐫_{para}|$ that is smaller than $2^{1/6}\sigma$. Here, $ϵ$ represents the strength of interaction and $\sigma$ is the characteristic length scale of repulsion. The distance $\sigma$ can be thought of as an effective membrane thickness (imagine a surface constructed from overlapping spheres with a diameter $\sigma$). Normally, $\sigma$ should be selected as small as possible for a given resolution length of both the RBC membrane and parasite, which is about 0.2 μm in our models. Therefore, $\sigma=0.2\mum$ is chosen, such that no overlap between the cells is guaranteed and the interacting surface is smooth enough.

The attractive part of RBC-parasite interaction is modeled by a reversible two-state bond model. Bonds can form between RBC membrane vertices representing receptors and merozoite vertices corresponding to ligands, while existing bonds can also dissociate. These bonds represent RBC-parasite adhesion through existing agonists at the surface of these cells and can be formed by two different types of ligands:

which is motivated by electron microscopy observations of RBC-merozoite adhesion (Bannister et al., 1986). Long ligands result in long bonds, while short ligands lead to short bonds. Both bond types are modeled by harmonic springs with the potential energy given by

$$
U_{ad}⁢(ℓ)=\frac{\lambda_{type}}{2}⁢(ℓ-ℓ_{0})^{2},
$$

where $\lambda_{type}$ is the spring extensional rigidity of either long or short bond type and $ℓ_{0}$ is the equilibrium bond length. To model the dynamic two-state interaction, constant (i.e. length independent) on- and off-rates ($k_{on}^{short}$, $k_{on}^{long}$, and $k_{off}$) are chosen, in order to simplify the model and reduce the number of parameters. Furthermore, the off-rate for both bond types is selected to be same. Note that this model can easily be extended to length-dependent rates.

To implement the different bond types, each vertex at the parasite surface represents either a long or a short ligand. The choice of vertices that correspond to long or short ligands is made randomly for fixed ligand densities $ρ_{long}$ and $ρ_{short}$. To avoid possible artifacts of a single discrete ligand distribution, each independent simulation assumes a different random choice of ligands with their respective densities kept constant. Bonds between the vertices at the RBC and parasite surfaces can form if the distance between two vertices is smaller than the corresponding cut-off distances $ℓ_{0}+ℓ_{eff}^{long}$ and $ℓ_{0}+ℓ_{eff}^{short}$, which remain the same in all simulations. Here, $ℓ_{0}=2^{1/6}\sigma$ corresponds to the length of the excluded-volume LJ interactions between the vertices of RBC and parasite, whose choice is defined by a characteristic discretization length of the RBC membrane. Only a single bond is allowed at each vertex for the both ligand types. Note that existing bonds can stretch beyond their effective binding ranges $ℓ_{eff}^{long}$ and $ℓ_{eff}^{short}$.

### Hydrodynamic interactions

Hydrodynamic interactions are modeled using the dissipative particle dynamics (DPD) method (Hoogerbrugge and Koelman, 1992; Español and Warren, 1995), where fluid is represented by a collection of particles interacting through three types of pairwise forces: conservative $𝐅_{i⁢j}^{C}$, dissipative $𝐅_{i⁢j}^{D}$, and random $𝐅_{i⁢j}^{R}$ forces. The total force between particles $i$ and $j$ is given by

$$
𝐅_{i⁢j}=𝐅_{i⁢j}^{C}+𝐅_{i⁢j}^{D}+𝐅_{i⁢j}^{R}.
$$

The conservative force models fluid compressibility, whereas the dissipative and random forces maintain a desired temperature of the system. The dissipative force also gives rise to fluid viscosity, which is generally measured in DPD by simulating a reversible-Poiseuille flow (Backer et al., 2005; Fedosov et al., 2010c). The DPD interactions are implemented only between the pairs of fluid-fluid, fluid-RBC, and fluid-parasite particles. DPD interaction parameters are selected such that they impose no-slip boundary condition at RBC and parasite surfaces (Fedosov et al., 2010a; Hillringhaus et al., 2019).

### Simulation setup

Simulation domain with a size of $7.7⁢D_{0}\times3.1⁢D_{0}\times3.1⁢D_{0}$ contains both RBC and parasite suspended in a DPD fluid, where $D_{0}=\sqrt{A_{0}/\pi}$ is the effective RBC diameter. Periodic boundary conditions are imposed in all directions. Initially, the parasite is placed close enough to the RBC membrane, so that the interaction between them is immediately possible. The initial parasite orientation is with its apex directed away from the membrane to mimic least favorable attachment configuration.

The main simulation parameters are shown in Table 1, both in simulation and physical units. To compare simulation units to physical units, a basic length scale is defined as the effective RBC diameter $D_{0}$, an energy scale as $k_{B}⁢T$, and a time scale as RBC membrane relaxation time $\tau=η⁢D_{0}^{3}/κ$. For average properties of a healthy RBC, the effective diameter is $D_{0}≃6.5\mum$ with $A_{0}=133.5\mum^{2}$ (Evans and Skalak, 1980) and the relaxation time becomes $\tau≈0.92s$ for the bending modulus $κ=3\times10^{−19}J$ (Evans, 1983; Fedosov et al., 2010a) and plasma viscosity $η=1mPas$. All simulations are performed on the supercomputer JURECA Jülich Supercomputing Centre, 2018 at the Jülich Supercomputing Centre, Forschungszentrum Jülich.

### Monte-Carlo sampling of alignment times

One of the main foci of our study is to obtain distributions of parasite alignment times for various conditions, which requires a large number of simulations of merozoite alignment. In order to significantly reduce the computational effort, Monte-Carlo (MC) sampling of alignment times, which is guided by direct DPD simulations of RBC-parasite adhesion, is employed. The MC sampling is based on a two-dimensional probability map (see e.g. Figure 4a), which characterizes parasite orientation at the membrane surface through the distance $d_{apex}$ between the parasite apex and membrane and merozoite alignment angle $\theta$ (see Figure 3a for definitions of $d_{apex}$ and $\theta$). To construct such a probability map, possible $d_{apex}$ and $\theta$ values are binned into a number of orientation states $(i,j)=(d_{apex}^{i},\theta^{j})$, and the probability $P(i,j)$ of each state is computed from at least 10 long DPD simulations of RBC-parasite adhesion. We have verified that 10 independent DPD simulations are enough to reliably compute a probability map through its convergence with the number of DPD simulations. In the MC algorithm, changes in parasite orientation are modeled by transitions between different states, using the Metropolis algorithm. Thus, the transition from a state $(i,j)$ to one of the neighboring states $(i+1,j)$, $(i−1,j)$, $(i,j+1)$ or $(i,j−1)$ is selected randomly with a probability of $1/4$, and this move is accepted if $ξ<P(newstate)/P(i,j)$, where $ξ$ is a random number drawn from a uniform distribution in the interval $[0,1]$. In summary, the MC sampling algorithm is performed as follows:

Note that the MC sampling algorithm fulfills detailed balance, but does not account for hydrodynamic interactions. The fulfillment of detailed balance for the Metropolis algorithm in equilibrium means that changes between different states $(i,j)$ and $(i^{′},j^{′})$ (with energies $E_{(i,j)}$ and $E_{(i^{′},j^{′})}$, respectively) are performed according to transition rates proportional to $exp⁡[−(E_{(i,j)}−E_{(i^{′},j^{′})})/(k_{B}T)]$, which are directly connected to probabilities of different states. Noteworthy, the MC sampling is a fast and efficient way to sample the distribution of parasite alignment times.
