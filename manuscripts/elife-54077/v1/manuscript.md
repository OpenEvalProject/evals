# Mechanics and kinetics of dynamic instability

## Authors

- Thomas CT Michaels<sup>1</sup> ([ORCID: 0000-0001-6931-5041](https://orcid.org/0000-0001-6931-5041))
- Shuo Feng<sup>2</sup> ([ORCID: 0000-0003-0530-8381](https://orcid.org/0000-0003-0530-8381))
- Haiyi Liang<sup>2</sup> ([ORCID: 0000-0001-7458-8036](https://orcid.org/0000-0001-7458-8036)) †
- L Mahadevan<sup>1</sup> ([ORCID: 0000-0002-5114-0519](https://orcid.org/0000-0002-5114-0519)) †

### Affiliations

1. Paulson School of Engineering and Applied Sciences, Harvard University Cambridge United States
2. Department of Modern Mechanics, University of Science and Technology of China Hefei China
3. IAT Chungu Joint Laboratory for Additive Manufacturing, Anhui Chungu 3D Institute of Intelligent Equipment and Industrial Technology Wuhu China
4. Department of Physics, Harvard University Cambridge United States
5. Department of Organismic and Evolutionary Biology, Harvard University Cambridge United States

† Corresponding author

## Abstract

During dynamic instability, self-assembling microtubules (MTs) stochastically alternate between phases of growth and shrinkage. This process is driven by the presence of two distinct states of MT subunits, GTP- and GDP-bound tubulin dimers, that have different structural properties. Here, we use a combination of analysis and computer simulations to study the mechanical and kinetic regulation of dynamic instability in three-dimensional (3D) self-assembling MTs. Our model quantifies how the 3D structure and kinetics of the distinct states of tubulin dimers determine the mechanical stability of MTs. We further show that dynamic instability is influenced by the presence of quenched disorder in the state of the tubulin subunit as reflected in the fraction of non-hydrolysed tubulin. Our results connect the 3D geometry, kinetics and statistical mechanics of these tubular assemblies within a single framework, and may be applicable to other self-assembled systems where these same processes are at play.

## Introduction

Microtubules (MTs) are polar tubular polymers formed by the self-assembly of the protein tubulin. MTs are ubiquitous in eukaryotic cells, where they are a major component of the cellular cytoskeleton, and participate in a number of essential cellular functions, such as cell migration, morphogenesis, transport within cells and cell division (Desai, 1997; Gupta et al., 2015; Huber et al., 2013; Fletcher and Mullins, 2010). They are also involved in regulating the shape and dynamics of axons, cilia and flagella (Mimori-Kiyosue, 2011).

The basic building blocks of MTs are tubulin heterodimers. These are formed by α-tubulin and β-tubulin, two structurally similar globular proteins with mass of about 55 kDa. αβ-tubulin dimers are arranged longitudinally into flexible tubulin filaments called protofilaments (PFs). A number (between 9 and 16, typically 13) of such PFs then assembles by lateral interactions to form the MT lattice (Mandelkow et al., 1986; Chrétien and Wade, 1991; Mitchison, 1993; Tilney et al., 1973). MT growth occurs by the addition of tubulin dimers mainly at the plus end, where $\beta$-tubulin is exposed. Upon hydrolysis of guanosine-tri-phosphate (GTP), tubulin subunits undergo a structural conversion that weakens lateral bonds, destabilises the subunit in the MT lattice and converts the relatively straight tubulin state into a state that is bound to guanosine-di-phosphate (GDP) and is characterised by an increased longitudinal curvature (Wang and Nogales, 2005; Alushin et al., 2014).

MTs are not static assemblies. They can repeatedly and stochastically vary their length by undergoing alternating phases of assembly and disassembly both in vivo and in vitro. This phenomenon is termed ‘dynamic instability’ and it is essential to a number of cellular functions, such as chromosome separation, the remodelling of spatial organisation of the cytoskeleton during mitosis or the exploration of extracellular environment (Mitchison and Kirschner, 1984; Gildersleeve et al., 1992; Cassimeris et al., 1988; Sammak and Borisy, 1988). Understanding the factors that regulate MT dynamic instability is central to cell physiology and disease. Yet a detailed understanding of dynamic instability still remains elusive (Aher and Akhmanova, 2018; Hemmat et al., 2018). This difficulty originates in part from the fact that dynamic instability is the result of several mechanical and kinetic aspects operating at multiple time and length scales (Figure 1).

![Figure 1.](https://cdn.elifesciences.org/articles/54077/elife-54077-fig1-v1.jpg)

**Figure 1.:** MTs are composed of tubulin heterodimers formed of α-tubulin and β-tubulin. Both α-tubulin and β-tubulin are bound to GTP, but only the GTP that is bound to a β-tubulin is hydrolysable (Nogales et al., 1998). When the tubulin dimer is part of the MT lattice, GTP hydrolysis increases the spontaneous longitudinal curvature along the dimer axis. This causes GDP-tubulin dimers to be less tightly bound in the MT lattice (Wang and Nogales, 2005; Alushin et al., 2014). In the scheme, GTP-tubulin dimers are shown in green, while GDP-tubulin dimers are shown in blue; dark color indicates β-tubulin and light colour indicates $\alpha$-tubulin. Tubulin dimers are connected head-to-tail into PFs. Typically, 13 such PFs align laterally to form the MT lattice, which is a long and hollow cylindrical shell with an outer diameter of approximately 25 nm and a thickness of about 5 nm (Mandelkow et al., 1986; Chrétien and Wade, 1991; Mitchison, 1993; Tilney et al., 1973). The mechanical stability/instability of the MT tube structure results from a competition between lateral and longitudinal curvatures. While MTs made of GTP-tubulin are relatively straight (about 5° per subunit), MTs made of GDP-tubulin tend to curve outward longitudinally at the plus end due to the longitudinal spontaneous curvature of GDP-tubulin dimers (about 12° per subunit) (Chrétien et al., 1995). Consequently, MTs consisting of GDP-tubulin (hydrolyzed MTs) tend to be mechanically less stable that their non-hydrolysed counterparts. The images show: (a) Schematic structure of an unhydrolyzed αβ-tubulin dimer with bound nucleotides highlighted in orange (Alushin et al., 2014). (b) EM image showing the characteristic shape of a depolymerising MT plus end, resembling a ram’s horn (VanBuren et al., 2005). (c) Sequence of TIRF microscopy images of a MT end illustrating the switching between phases of polymerisation and depolymerisation during dynamic instability; catastrophe is associated with the loss of the GTP-caps (green fluorescence is from a protein that is believed to associate with the GTP cap). (a) is adapted from Alushin et al. (2014); (b) is reproduced from Austin et al. (2005). (c) is reproduced from Duellberg et al. (2016) under the Creative Commons Attribution License CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/).

As such, dynamic instability of MTs has been the focus of extensive experimental and theoretical work (Mandelkow et al., 1986; Chrétien and Wade, 1991; Mitchison, 1993; Tilney et al., 1973; Mitchison and Kirschner, 1984; Fygenson et al., 1994; Gildersleeve et al., 1992; Cassimeris et al., 1988; Sammak and Borisy, 1988; Hemmat et al., 2018; Aher and Akhmanova, 2018; Dogterom and Leibler, 1993; Brun et al., 2009; Antal et al., 2007; Mahadevan and Mitchison, 2005; Nogales et al., 1998; Wang and Nogales, 2005; Alushin et al., 2014; Zovko et al., 2008; Hoog et al., 2011; Mandelkow et al., 1991; Chrétien et al., 1995; Austin et al., 2005; Gardner et al., 2011; Hunyadi and Jánosi, 2007; Rice et al., 2008; Kueh and Mitchison, 2009; Jánosi et al., 1998; Molodtsov et al., 2005; VanBuren et al., 2005; Zapperi and Mahadevan, 2011; Bertalan et al., 2014b; Wu et al., 2009; Duellberg et al., 2016; Seetapun et al., 2012; Cheng et al., 2012; Cheng and Stevens, 2014; Jain et al., 2015; Aparna et al., 2017; Zakharov et al., 2015). Studies initially invoked a kinetic view capturing MT dynamic instability phenomenologically by different rates of polymerisation and depolymerisation depending on the state of the tubulin-phosphate complex (Dogterom and Leibler, 1993; Brun et al., 2009; Antal et al., 2007). Evidence of changes in the structural properties of MT subunits during hydrolysis later showed how lattice-bound tubulin dimers undergo a structural conformational change that increases their curvature (Wang and Nogales, 2005; Alushin et al., 2014; Mahadevan and Mitchison, 2005), suggesting that outward curving tips of hydrolysed MTs can cause such structures to be mechanically unstable (Zovko et al., 2008; Hoog et al., 2011; Austin et al., 2005; Mandelkow et al., 1991; Chrétien et al., 1995; Gardner et al., 2011; Hunyadi and Jánosi, 2007; Rice et al., 2008; Kueh and Mitchison, 2009). Several coarse-grained computer simulations have since then adopted this structural-mechanical view, considering MT elasticity explicitly, to understand different aspects of dynamic instability, including hydrolysis-driven mechanical deformations near the cap (Jánosi et al., 1998), force generation by shrinking microtubules (Molodtsov et al., 2005), or 3D sheet-like/blunt tips (VanBuren et al., 2005), or stochastic microtubule tip configurations and their relation to catastrophe (Zakharov et al., 2015). Few studies, however, have attempted to capture this mechanical view with the aim of emphasizing the qualitative features necessary for dynamic instability and providing phase diagrams that delineate the zones where dynamic instability is seen. Those that exist, for example (Zapperi and Mahadevan, 2011; Bertalan et al., 2014b), focus on the 1D limit, where MTs are modelled as adsorbed chains: the predictions from these models can be qualitatively different from those that correctly account for the 3D geometry of MTs (see ‘Mechanical stability of 3D MTs in the presence of quenched disorder’).

Here, we use a combination of theory and simulations to establish how the kinetics of polymerization and the mechanics associated with the 3D geometry of MTs act together across multiple scales to regulate dynamic instability. We also establish the role of disordered remnants of GDP-tubulin in determining the statistics of MT rescue. All together, our study provides a set of qualitative phase diagrams that delineate the regions of parameter space where dynamic instability is seen, consistent with previous observations while providing experimentally testable predictions.

## Methods

### Computational model

To complement the theory (see ‘A phase diagram for mechanical stability of 3D MTs’), we developed a minimal coarse-grained computational model of MT mechanics and dynamics. To characterize the tubulin heterodimers, we use two patchy spheres linked together by a flexible hinge. We derive the patchy particles from coarse-grained representations of colloidal particles that are decorated by patches on their surface; the patches represent specific anisotropic interactions that promote binding with patches on other particles. In our model, interactions between dimers are described by patches carrying two types of interactions: longitudinal and lateral contacts (Huisman et al., 2008). Longitudinal contacts link dimers head-to-tail, arranging them into PFs. Lateral contacts connect parallel PFs to form the cylindrical shell of the MT. Each dimer has two longitudinal contacts and four lateral ones, corresponding to three patches per monomer (Figure 2a). Interactions between two patches on monomers $i$ and $j$ are described by the following potential (Feng and Liang, 2012):

$$
V_{patchy}⁢(r,\theta_{i},\theta_{j})=V_{S}⁢(r,\theta_{i},\theta_{j})+V_{B}⁢(r,\theta_{i},\theta_{j})+V_{T}⁢(r,\theta_{i},\theta_{j}).
$$

We see that there are three distinct contributions associated with the stretching ($V_{S}$), bending ($V_{B}$) and twisting ($V_{T}$) modes, and we choose the following forms for these potentials:

$$
V_{S}(r,\theta_{i},\theta_{j})={ϵ[(1−e^{−a(r−r_{0})})^{2}−1]r<r_{m}ϵ[(1−e^{−a(r−r_{0})})^{2}−1]D_{\theta}(\theta_{i})D_{\theta}(\theta_{j})r_{m}\leqr<r_{c}0r\geqr_{c}
$$



$$
V_{B}(r,\theta_{i},\theta_{j})=b(\theta_{i}^{2}+\theta_{j}^{2})D_{r}(r)D_{\theta}(\theta_{i})D_{\theta}(\theta_{j})
$$



$$
V_{T}(r,\theta_{i},\theta_{j})=c(ϕ/r)^{2}D_{r}(r)D_{\theta}(\theta_{i})D_{\theta}(\theta_{j})
$$

where

$$
D_{r}(r)={1−sin^{4}⁡(\frac{\pi}{4}\frac{r−r_{0}}{r_{d}−r_{0}})r<r_{d}0r\geqr_{d}
$$



$$
D_{\theta}(\theta)={1−sin^{4}⁡(\frac{\pi}{4}\frac{\theta}{\theta_{d}})\theta<\theta_{d}0\theta\geq\theta_{d}
$$

Here, $r$ denotes the center-to-center distance between monomers, while the angles $\theta_{i}$ and $\theta_{j}$ describe the spatial directions of the patches (Figure 2b). The Morse potential term $V_{S}$, defined in Equation 2, describes the non-covalent interaction between patches, with $ϵ$ being the depth of the potential well, $r_{0}$ the equilibrium distance between monomers, and $a$ is a parameter that controls the curvature of the potential well and, hence, determines the stretching modulus (see Equation 7). When $r<r_{m}$, where $r_{m}=r_{0}-log⁡(2)/a$, the potential $V_{S}$ behaves as an isotropic repulsive interaction. In the range $r_{m}\leqr<r_{c}$, where $r_{c}=5⁢r_{0}$ is the cutoff for $V_{S}$ ($V_{S}$ is set to zero for $r\geqr_{c}$), $V_{S}$ is modified by multipliers $D_{\theta}⁢(\theta_{i})$ and $D_{\theta}⁢(\theta_{j})$. This yields an anisotropic attractive potential that exists only when the patches are aligned. Indeed, the multipliers $D_{\theta}⁢(\theta_{i})$ and $D_{\theta}⁢(\theta_{j})$, which are defined in Equation 6, weaken the attraction between the patches when these are not aligned (Figure 2c): $D_{\theta}$ reaches its maximum value when $\theta=0$. The cutoff of $D_{\theta}$ is $\theta_{d}=\pi/3$ and limits the influence of the patches within particular range of spatial directions. The potential terms $V_{B}$ and $V_{T}$, defined in Equations 3 and 4, characterise bending and twisting deformations respectively. They are described as classical harmonic potentials with curvature $b$, respectively, $c$, and are modified by the multipliers $D_{r}⁢(r)$, $D_{\theta}⁢(\theta_{i})$ and $D_{\theta}⁢(\theta_{j})$, which are defined in Equations 5 and 6. These multipliers limit the range of $V_{B}$ and $V_{T}$ to specific spatial locations and directions. The cutoff of $D_{r}$ is set as $r_{d}=2.7⁢r_{0}$, which is smaller than $r_{c}$ (the cutoff of $V_{S}$). This choice makes $V_{B}$ and $V_{T}$ shorter-range interactions compared to $V_{S}$.

![Figure 2.](https://cdn.elifesciences.org/articles/54077/elife-54077-fig2-v1.jpg)

**Figure 2.:** (a) The GTP-tubulin subunit ($\alpha⁢\beta$-heterodimer) in our coarse-grained computer model. The blue patches (1 and 2) are longitudinal connecting points, while the pink patches (3 to 6) are lateral ones. This setup allows the dimer to curve inward along the MT longitudinal direction and outward laterally. The positions of the patches allow us to control the longitudinal and lateral curvatures of the subunit, giving a strong curvature (12°) to hydrolysed dimers and a weaker curvature (5°) to non-hydrolysed dimers. (b) The interaction potential $V_{patchy}⁢(r;\theta_{i},\theta_{j})$ between two patchy particles as a function of their centre-to-centre distance $r$ for $\theta_{i}=0$ and increasing $\theta_{j}=\theta$. Inset: the bending angles $\theta_{i}$ and $\theta_{j}$ are defined as the angles between the centre-to-patch line and the centre-to-centre line; the twisting angle $\phi_{i⁢j}$ is defined by the projection of the normals $𝒏_{i}$ and $𝒏_{j}$ on the plane perpendicular to the centre-to-centre line. (c) Our mechanical model describes a MT as a continuous, thin elastic sheet. This is parameterised as a surface of revolution obtained by rotating the function $R⁢(x)=R_{0}+u⁢(x)$ along the MT long axis ($x$-axis), where $R_{0}$ is the natural radius of the MT and $u⁢(x)$ describes the local deformation of the surface away from $R_{0}$. We approximate lateral interaction potentials between tubulin subunits in neighbouring PFs by a set of spring potentials (springs with stiffness $S$). Bending of the PFs in the MT causes the connecting springs to stretch. This competition between bending energy and stretching energy determines the mechanical stability of MTs. Inset: hydrolysed tubulin dimers curve naturally in two directions as described by the longitudinal and lateral spontaneous curvatures $κ$ and $\omega$, respectively.

The parameters in our coarse-grained computational model are linked to the mesoscopic mechanical properties of MTs (see section ’Mechanics’) including the interfilament spring stiffness $S$, the filament bending stiffness $B$ and the filament torsional rigidity $K$ as

$$
S=2⁢a^{2}⁢l⁢ϵ,B=b⁢l,K=\frac{8⁢c}{l},
$$

where $l$ is the length scale of tubulin dimers. $l$ takes different values depending on whether we are calculating longitudinal or lateral properties. In particular, we set $l=2⁢r_{0}=8$ nm when calculating longitudinal properties and set $l=r_{0}=4$ nm for lateral ones (see Appendix 1 and Table 1 for further details on the computer simulation model and a summary of parameter choices). We choose the potential-well parameters in our simulations such that the resulting mesoscopic mechanical parameters Equation 7 are consistent with the experimentally measured values of the mechanical properties of typical MTs (Gittes et al., 1993; Mickey and Howard, 1995; Felgner et al., 1996; Tolomeo and Holley, 1997; de Pablo et al., 2003; Sept and MacKintosh (2010); Deriu et al., 2010). Simulations of this coarse-grained model of MTs were performed using Molecular Dynamics (MD), as described in Appendix 1.

**Table 1.**
 Values of parameters used in our coarse-grained simulations.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Value</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>r0</td>
      <td>4 nm</td>
      <td>Equilibrium distance between tubulin monomers</td>
    </tr>
    <tr>
      <td>ϵ0</td>
      <td>7.665 × 10-20J</td>
      <td>Potential energy depth for longitudinal interactions</td>
    </tr>
    <tr>
      <td>ξ</td>
      <td>5° or 12°</td>
      <td>Angle between α-tubulin and β-tubulin within a GTP- or GDP-dimer</td>
    </tr>
    <tr>
      <td>χc⁢h⁢a⁢i⁢n</td>
      <td>3°</td>
      <td>See Equations 24-29</td>
    </tr>
    <tr>
      <td>χs⁢i⁢d⁢e⁢1</td>
      <td>103.45° or 90°</td>
      <td>See Equations 24-29</td>
    </tr>
    <tr>
      <td>χs⁢i⁢d⁢e⁢2</td>
      <td>13.8°</td>
      <td>See Equations 24-29</td>
    </tr>
    <tr>
      <td>ll⁢o⁢n⁢g</td>
      <td>2r0</td>
      <td>Longitudinal size of tubulin dimers</td>
    </tr>
    <tr>
      <td>ll⁢a⁢t</td>
      <td>r0</td>
      <td>Lateral size of tubulin dimers</td>
    </tr>
    <tr>
      <td>al⁢o⁢n⁢g,al⁢a⁢t</td>
      <td>20/r0</td>
      <td>Parameters that control longitudinal and lateral stretching stiffness</td>
    </tr>
    <tr>
      <td>bl⁢o⁢n⁢g</td>
      <td>20⁢ϵ0</td>
      <td>Parameter that controls longitudinal bending stiffness</td>
    </tr>
    <tr>
      <td>bl⁢a⁢t</td>
      <td>10⁢ϵ0</td>
      <td>Parameter that controls lateral bending stiffness</td>
    </tr>
    <tr>
      <td>cl⁢o⁢n⁢g</td>
      <td>500⁢ϵ0⁢r02</td>
      <td>Parameter controls longitudinal twisting stiffness</td>
    </tr>
    <tr>
      <td>cl⁢a⁢t</td>
      <td>0.5⁢ϵ0⁢r02</td>
      <td>Parameter that controls lateral twisting stiffness</td>
    </tr>
    <tr>
      <td>ϵl⁢o⁢n⁢g</td>
      <td>ϵ0</td>
      <td>Potential energy depth for longitudinal interactions</td>
    </tr>
    <tr>
      <td>ϵl⁢a⁢t</td>
      <td>0.0906ε0</td>
      <td>Potential energy depth for lateral interactions</td>
    </tr>
  </tbody>
</table>

## Results

### A phase diagram for mechanical stability of 3D MTs

Our analytical model to study the mechanical stability of 3D MTs is a function of the underlying parameters describing MT mechanics, MT growth kinetics and subunit hydrolysis, which we first consider in the deterministic limit (see ’A phase diagram for mechanical stability of 3D MTs’). This forms the basis for studying the mechanical stability of MTs when there is heterogeneity in the state of tubulin, that is it could be either GTP or GDP bound (see ‘Mechanical stability of 3D MTs in the presence of quenched disorder’), and allows us to investigate the role of GTP-remnants (containing random fractions of non-hydrolysed subunits) on rescue (see ‘Role of GTP-remnants in rescue’).

The starting point of our mechanical model is that MTs exist as individual polymers with persistence lengths in the O(mm) range, which is much larger than the typical length of MTs (µm range) (Fletcher and Mullins, 2010; Huber et al., 2013). This observation suggests that MTs can be considered to have a well-defined shape that is not affected significantly by thermal fluctuations. Moreover, previous studies indicate that lateral bonds between tubulin dimers are considerably weaker than longitudinal ones (VanBuren et al., 2002; VanBuren et al., 2005; Molodtsov et al., 2005). We model MTs as a set of adherent PFs that have bending stiffness $B$; we approximate lateral interactions between PFs by a series of spring potentials (springs of stiffness $S$) and assume that extending these springs beyond a critical displacement causes MTs to become mechanically unstable and break, potentially leading to dynamic instability.

#### Kinetics

Previous studies (Wang and Nogales, 2005; Alushin et al., 2014) suggest that tubulin dimers that are part of the MT lattice have different mechanical properties depending on their hydrolysis state. In particular, upon hydrolysis the tubulin dimer undergoes a structural transformation from a relatively straight state to a state with finite curvature. In a 3D setting, the tubulin dimer can be curved both in the longitudinal direction and in the lateral direction. Let $κ⁢(0)$ denote the longitudinal curvature of tubulin dimers in their GTP-state and let $κ⁢(∞)$ be the longitudinal curvature in the hydrolysed state. For simplicity, we assume that the hydrolysis reaction affects primarily the longitudinal curvature of the tubulin dimers, such that their curvature $\omega$ in the azimuthal direction can be considered to be constant. This assumption can be relaxed, see Appendix 2. Thus, as a result of GTP-hydrolysis, the longitudinal curvature of tubulin dimers, $κ$, changes with time, which we assume follows first order kinetics so that

$$
\frac{d⁢κ}{d⁢t}=k_{H}⁢(κ⁢(∞)-κ),
$$

where $k_{H}$ is the rate of hydrolysis. While bound tubulin changes its structure, unbound (bound) tubulin can attach (detach) to (from) the free end of the MTs, which we also describe using a minimal first order kinetic law for the evolution of the length of the MT $n⁢(t)$ (expressed in number of subunits) so that

$$
\frac{d⁢n}{d⁢t}=k_{+}⁢[m]-k_{-}=k_{G}.
$$

Here $k_{G}$ is the net growth rate, $k_{+}$ is the elongation rate constant, $k_{-}$ is the dissociation rate constant and, for simplicity, we have assumed a constant subunit concentration $[m]$ in solution.

#### Mechanics

In addition to MT growth and subunit hydrolysis, we also need to account for the elastic deformation of the MTs since the geometric state of the assembly is linked to its mechanical state. Individual PFs can bend, but are also constrained by inter-filament interactions, so that there are two contributions to elastic energy: (i) curvature energy associated with the bending of PFs, (ii) stretching energy of the springs connecting neighbouring PFs. We capture these energy contributions in a continuum picture that describes a MT as a thin elastic surface of revolution obtained by rotating the function $R⁢(x)=R_{0}+u⁢(x)$ along the long MT axis ($x$-axis), where $R⁢(x)$ is the local radius of MT and $R_{0}$ is the natural radius (Figure 2c). In the small gradient approximation, corresponding to $u^{′}≪1$, the total elastic energy can be written as (see Appendix 2 for details):

$$
ℰ_{tot}=\int_{0}^{∞}(\frac{B}{2}⁢[u^{′′}-κ]^{2}+\frac{Σ}{2}⁢[u^{′}]^{2}+\frac{S}{2}⁢u^{2})⁢𝑑x,
$$

where $Σ=B⁢(1+\omega⁢R_{0})^{2}/R_{0}^{2}$ and $=′\partial/\partialx$ denotes derivative with respect to $x$. The first term in Equation 10 is the energy of MT that penalises deviations from its natural curvature $κ⁢(t)$ which itself reflects its state of hydrolysis. The second term is a surface energy term that penalises area increase due to the outward curving of the surface. The third term is the stretching energy of the springs. The minimum energy configuration results from a competition between bending energy, which favours a natural curved MT state, and elastic spring energy, which favours a straight cylindrical MT configuration. The overall shape of the axisymmetric tubule is then obtained by solving the Euler-Lagrange equation associated with Equation 10 (see Appendix 2 for details):

$$
B⁢u^{′′′′}-Σ⁢u^{′′}+S⁢u=0
$$

subject to the boundary conditions $u⁢(∞,t)=u^{′}⁢(∞,t)=0$ (fixed minus end), $u^{′′}⁢(0,t)=κ$ and $u^{′′′}⁢(0,t)=0$ (free plus end), and is coupled to the kinetic Equations 8 and 9.

#### Condition for mechanical stability

There are three natural dimensionless parameters (two mechanical parameters and one kinetic parameter) in our model that read:

$$
\alpha=(\frac{B⁢κ^{2}}{S⁢u_{c}^{2}})^{1/2},\beta=(\frac{Σ⁢u_{c}}{B⁢κ})^{1/2},\gamma=\frac{k_{G}}{k_{H}}.
$$

The first parameter α describes the effect of longitudinal curvature. The second parameter β pertains to lateral curvature. Coupling these mechanical parameters to the kinetics of subunit hydrolysis and MT growth introduces an additional relevant dimensionless parameter $\gamma$, which is the ratio of the rate of hydrolysis of GTP-tubulin dimers to the net rate of addition of GTP-subunits to the MT plus end (see Appendix 2 for details).

These parameters serve as the basis for a phase diagram for the mechanical stability of a 3D MT (Figure 3a). Assuming that a mechanical instability arises when the elastic MT is deformed so that the radial displacement crosses a critical value ($u⁢(0)>u_{c}$), we can solve Equation 11 in terms of the maximal deformation $u⁢(0)$ to yield a condition for when the MT is mechanically unstable. Rewriting this in terms of the scaled longitudinal curvature yields a critical value (see the Appendix 2 for details):

$$
\alpha=\frac{\sqrt{1+\frac{4⁢\beta^{2}}{1-e^{-n/\gamma}}}-1}{2⁢\beta^{2}}.
$$

above which MTs are mechanically unstable (the transition curve in the αβ-plane in Figure 3a). This critical value depends on the lateral curvature parameter β, which is related to MT radius through $\beta≃1/R_{0}$. In particular, the critical value for $\alpha$ is maximal ($\alpha=1$) when $\beta=0$, that is $R_{0}→∞$. This situation corresponds to the limit of a one-dimensional MT (Zapperi and Mahadevan, 2011). The critical value for $\alpha$ then decreases with increasing lateral curvature β, that is decreasing MT radius. Overall, these results suggest that MTs with smaller radius are mechanically less stable than MTs with larger radius, consistent with the intuition that increasing azimuthal curvature increases the mechanical strain on the MT and thus makes it more likely to fracture. Furthermore, increasing the rate of MT growth over hydrolysis acts to stabilise MTs mechanically. In the mechanically stable phase, hydrolysis is slower than the addition of GTP-tubulin at the plus end, leaving a stabilising GTP-cap of size $n$ (see Appendix 2, Video 1). In the mechanically unstable phase, hydrolysis is faster than subunit addition at the plus end. Consequently, the ‘hydrolysis front’ takes over the ‘growth front’, which destabilises MTs. In this case, the PFs curve outward near the plus end, leading to a characteristic morphology of depolymerising MTs that resembles rams’ horns (VanBuren et al., 2005) (see Appendix 2, Video 2). The transition curve separating these fast and slow hydrolysis regimes depends on both the longitudinal and lateral curvatures of the MT.

![Figure 3.](https://cdn.elifesciences.org/articles/54077/elife-54077-fig3-v1.jpg)

**Figure 3.:** (a) Schematic phase diagram for mechanical stability/instability with three axes (two mechanical axes and one kinetic axis): longitudinal curvature parameter $\alpha=(B⁢κ^{2}/S⁢u_{c}^{2})^{1/2}$, lateral curvature parameter $\beta=(Σ⁢u_{c}/B⁢κ)^{1/2}$, and ratio of growth rate to hydrolysis rate $\gamma=\tau_{κ}/\tau_{G}$. (b) 2D phase diagram separating regions of mechanically stable and unstable MTs as a function of $\alpha$ and $\beta$. Data points are from computer simulations and the solid line is the prediction of Equation 13. (c)-(d) Implementation of lateral (c) and longitudinal (d) disorder at the level of the spring stiffness $S$ in our coarse-grained computer model. The data points are simulation results and the solid lines are fits to Equation 16 and Equation 17. The data show that lateral disorder acts to destabilise MTs mechanically (c), while longitudinal disorder strengthens MTs (d). In both cases, disorder was generated using the distribution of spring constants in Equation 14 with $\sigma=0.02⁢⟨S⟩$, that is the disorder parameter was $k=50$. The amount disorder of each tubulin subunit represents the average value of the relative stiffness $S/⟨S⟩$ of its two lateral interactions. See Videos 1–4 for movies illustrating the mechanical stability of a MT with and without quenched disorder (see Videos 1–4).

![Video 1.](https://cdn.elifesciences.org/articles/54077/elife-54077-video1.mp4.jpg)

**Video 1.:** This movie shows the interplay between MT growth kinetics (we focus here only on the addition of GTP-tubulin subunits at the plus end) and the subsequent hydrolysis of the incorporated subunits in the older parts of the MT. The interplay between growth and hydrolysis can be seen in the emergence of a growing front and a hydrolysis front that move with different speed. In this case, the hydrolysis front does not catch up with the growth front at the plus end, yielding a stabilising GTP-cap and a mechanically stable MT configuration for the entire duration of the simulation. The growth rate is $r_{G}=10^{-4}$ steps−1, while the probability of hydrolysis for each dimer is given by $p_{H}=e^{-r_{H}⁢t}$, where $r_{H}=10^{-10}$ steps−1 is the rate of hydrolysis. Note the separation of timescales between MT growth and subunit hydrolysis ($r_{G}≫r_{H}$). To keep the helical structure stable, we use the following parameters $b_{l⁢o⁢n⁢g}=8⁢ϵ_{0}$, $b_{l⁢a⁢t}=4⁢ϵ_{0}$ and $c_{l⁢o⁢n⁢g}=5⁢ϵ_{0}⁢r_{0}^{2}$, while the other mechanical parameters are the same as listed in Table 1.

![Video 2.](https://cdn.elifesciences.org/articles/54077/elife-54077-video2.mp4.jpg)

**Video 2.:** This movie shows the interplay between MT growth and subunit hydrolysis. The rate of hydrolysis is $r_{H}=5\times10^{-6}$ steps−1 while the growth rate is decreasing from $r_{G}=5\times10^{-3}$ steps−1 to $r_{G}=2\times10^{-6}$ steps−1. Hydrolysis destroys the GTP-cap of MT and causes catastrophe. The mechanical parameters are the same as in Video 1.

In Figure 3b, we show that crossing the transition curve given by Equation 13 causes a switch from the mechanically stable phase into the mechanically unstable phase. This could result from variations in either $\alpha$, $\beta$ or $\gamma$. For MTs in the mechanically stable phase, catastrophic failure can still occur via thermal activation. In this regime, the rate of catastrophe follows Arrhenius’ law $r_{c}≃exp⁡(ΔE/k_{B}T)$, where $k_{B}T$ is the thermal energy and $ΔE$ is the energy barrier given by $ΔE∝\alpha−1+\beta^{2}$ is a measure of the ‘distance’ from the transition curve Equation 13 in the phase diagram of Figure 3b; the further away a MT is from this transition curve, the less likely it is to undergo catastrophe. The dependence of the rate of catastrophe on MT radius is through the parameter β, such that $ln⁡r_{c}∝1/R_{0}^{2}$. Thus, at constant temperature and at fixed values of the mechanical parameters, the rate of catastrophe increases with decreasing MT radius or, equivalently, decreasing PF number.

#### Comparison with computer simulations

We used our computer simulations to test the prediction from Equation 13 for how the critical value of $\alpha$ varies with β, which is a function of MT radius $R_{0}$ that is controlled by changing the number $N_{f}$ of PFs in the MT. The results (Figure 3b) show that the critical value for $\alpha$ is maximal when $\beta=0$, and decreases with increasing β, in agreement with the theoretical prediction of Equation 13 (solid line).

### Mechanical stability of 3D MTs in the presence of quenched disorder

Having considered the deterministic limit where growth kinetics, hydrolysis and longitudinal/lateral curvatures characterise the mechanical stability of a 3D MT, we now consider the role of randomness by including a random fraction of GTP-tubulin dimers in their lattice. We can model this situation by introducing quenched disorder in the state of the tubulin subunit. Quenched disorder describes the general situation when certain parameters in the system become random variables; disorder can be considered to be ‘quenched’ when the probability distribution of parameter values either does not vary with time or it varies with time slowly compared to some underlying fast dynamics, and thus cannot be described solely using equilibrium statistical mechanics. In the context of MTs, such a separation of timescales emerges very naturally when comparing fast polymerization/depolymerization kinetics and the comparatively slower GTP turn-over.

Since the primary mode of MT instability is due to the breaking of lateral bonds, a natural parameter for discussing the role of disorder is the spring stiffness $S$. The underlying motivation for this choice is that mechanical forces can influence the rates of chemical reactions. Indeed, mechanical work contributes to the free energy, which in turn determines the rates of a chemical reaction (Howard, 2001). In our context, GDP-tubulins within the MT lattice experience mechanical stresses due to the strong curvature. These mechanical stresses can shift the polymerisation-depolymerisation equilibrium and favour free monomers. This is consistent with the idea that GDP-tubulins are less tightly bound to MTs than GTP-tubulins (Wang and Nogales, 2005; Alushin et al., 2014), even if the chemical bonds are identical.

Thus, instead of having a well-defined spring constant $S$ throughout the MT, we consider a MT with varying $S$. Each lateral interaction is characterised in principle by a different spring constant $S$, which is drawn from a time–independent probability distribution $p⁢(S)$ of spring constants. For convenience, we choose the Gamma-distribution

$$
p⁢(S;k,⟨S⟩)=\frac{k^{k}⁢S^{k-1}⁢exp⁡(-k⁢S/⟨S⟩)}{⟨S⟩^{k}⁢Γ⁢(k)},
$$

where $Γ⁢(x)$ is the Gamma function, $⟨S⟩$ is the average spring stiffness, and the parameter $1/k=\sigma/⟨S⟩$, with $\sigma$ being the standard deviation of the distribution, is the coefficient of variation that describes the degree of disorder in the system. The choice of the Gamma-distribution admits a simple parameterisation in terms of the coefficient of variation that allows us to explore a range of different extreme value statistics. For instance, for $k=1$ the Gamma distribution $p⁢(S;1,⟨S⟩)$ yields the exponential distribution with intensity $\lambda=1/⟨S⟩$, while for $k≫1$ it yields a normal distribution with mean $\mu=k⁢⟨S⟩$ and variance $\sigma^{2}=k⁢⟨S⟩^{2}$. We distinguish two limiting modes for disorder: lateral (Figure 3c) and longitudinal (Figure 3d). Any realisation of disorder can then be decomposed into a combination of these two limiting modes.

#### Lateral disorder

In the presence of disorder in $S$, lateral interactions are characterised by variations in $S$ azimuthally but not longitudinally. In this case, whether the MT undergoes catastrophe depends on the breaking of the weakest lateral bond along the circumference of the MT, resulting in a MT that is ‘cut-open’ along the longitudinal direction (Figure 3c and Appendix 2, Video 3). This situation is fully analogous to what happens when pulling a one-dimensional chain by its ends: the chain will break as soon as its weakest link breaks. The mechanical stability of a MT with lateral disorder is thus equivalent to the mechanical stability of a MT with uniform spring stiffness $⟨S_{min}⟩$, where $⟨S_{min}⟩$ denotes the average value of the weakest spring stiffness along the MT circumference. This replacement maps the study of the mechanical stability of a MT with lateral disorder onto a problem of extreme value statistics (Zapperi and Mahadevan, 2011; Bertalan et al., 2014b): the determination of $⟨S_{min}⟩$ for a system of $N$ independent and identically distributed links with spring constants $S_{1},⋯,S_{N}$. In Appendix 2, we show that $⟨S_{min}⟩$ can be calculated from Equation 14 using extreme-value statistics, yielding:

$$
\frac{⟨S_{min}⟩}{⟨S⟩}=\frac{1}{k}⁢Γ⁢(\frac{k+1}{k})⁢[\frac{Γ⁢(k+1)}{N}]^{1/k}.
$$

The condition for mechanical instability of a MT with lateral disorder in $S$ is thus obtained by replacing $⟨S⟩$ by $⟨S_{min}⟩$ in Equation 13, yielding:

$$
\alpha=\frac{\sqrt{1+\frac{4⁢\beta^{2}}{1-e^{-n/\gamma}}}-1}{2⁢\beta^{2}}⁢\sqrt{\frac{⟨S_{min}⟩}{⟨S⟩}}.
$$

Since $⟨S_{min}⟩<⟨S⟩$, Equation 16 predicts that the transition curve between mechanically stable and unstable MT regions shifts towards the instability region. Thus, lateral disorder weakens MTs.

![Video 3.](https://cdn.elifesciences.org/articles/54077/elife-54077-video3.mp4.jpg)

**Video 3.:** This movie illustrates the stability of a MT in the presence of lateral disorder in the spring stiffness $S$, which describes the strength of lateral contacts between PFs. Note that lateral disorder causes the MT to be mechanically unstable along directions with weakest lateral bonds (the MT ‘cut opens’ along these weak directions). The color code indicates the local value of $S$ for each subunit, which is obtained by averaging over the relative stiffness of its two lateral bonds (drawn from the Gamma-distribution (14) with $k=50$). The simulation parameters are the same as listed in Table 1, except that we set $ξ=5.8^{∘}$ for all tubulin dimers.

#### Longitudinal disorder

A different situation arises when quenched disorder is distributed longitudinally. Here, the strongest lateral bond determines MT stability. In fact, longitudinal disorder leads to the presence of ‘rings’ of particularly strong bonds that prevent the MT from depolymerising completely (Figure 3d and Appendix 2, Video 4). The mechanical stability of a MT with longitudinal disorder is thus equivalent to that of a MT with uniform spring stiffness $⟨S_{max}⟩$, where $⟨S_{max}⟩$ is the expected value of $S$ associated with the strongest lateral bond. Using extreme-value statistics, one finds (see Appendix 2) $⟨S_{max}⟩/⟨S⟩=(\gamma_{e}+log⁡N)/k$, where $\gamma_{e}≈0.5772$ is the Euler-Mascheroni constant (Taloni et al., 2018; Bertalan et al., 2014b; Zapperi and Mahadevan, 2011). Hence, the curve separating mechanically stable and unstable regions in the presence of longitudinal disorder is Zapperi and Mahadevan (2011):

$$
\alpha=\frac{\sqrt{1+\frac{4⁢\beta^{2}}{1-e^{-n/\gamma}}}-1}{2⁢\beta^{2}}⁢\sqrt{\frac{⟨S_{max}⟩}{⟨S⟩}}.
$$

Since $⟨S_{max}⟩>⟨S⟩$, longitudinal disorder in $S$ reinforces MTs.

![Video 4.](https://cdn.elifesciences.org/articles/54077/elife-54077-video4.mp4.jpg)

**Video 4.:** This movie illustrates the stability of a MT in the presence of longitudinal disorder in the spring stiffness $S$. Note that the MT is in this case mechanically more stable than in the presence of lateral disorder. This is because longitudinal disorder leads to the presence of ‘rings’ of strong bonds that prevent the MT from peeling off completely. The simulation parameters are the same as in Video 3.

It is important to note that longitudinal disorder is the only mode of disorder present in a 1D MT (Zapperi and Mahadevan, 2011). Lateral disorder is thus a defining feature of the 3D geometry of MTs. Our results thus reveal a fundamental role of MT dimensionality: while in a 1D setting quenched disorder stabilises MTs mechanically, in a 3D setting it can destabilise MTs.

#### Comparison with computer simulations

We have tested the theoretical predictions of Equation 16 and Equation 17 using our coarse-grained simulations (Figure 3c,d). Quenched disorder was realised using Equation 14 with disorder parameter $k=50$. These simulations confirm that longitudinal quenched disorder increases the mechanical stability of MTs (Figure 3c), whereas the effect of quenched disorder in the lateral direction is to destabilise MTs mechanically (Figure 3d).

### Role of GTP-remnants in rescue

Using our theoretical model of mechanical stability of 3D MTs in the presence of quenched disorder, we are now in the position to investigate the role of remnants of GTP-tubulin in rescue. Rescue refers to the transition from depolymerisation to polymerisation during MT dynamic instability but is still poorly understood (Brouhard, 2015). Experiments indicate that GTP-tubulin addition at the plus end is not critical for rescue (Gardner et al., 2013; Walker et al., 1988), but that the presence of remnants of GTP-tubulin along the MT lattice in so-called ‘GTP-islands’ can lead to MT rescue (Tropini et al., 2012; Dimitrov et al., 2008; Aumeier et al., 2016; Gardner et al., 2013; Vemu et al., 2018). In particular, experiments in vivo have revealed a strong correlation between rescue probability and the presence of remnants of GTP-tubulin in older parts of the MTs, suggesting that these ’GTP-remnants’ can function as rescue sites (Dimitrov et al., 2008). This view was further supported by the observation that the presence of a slowly hydrolyzable analogue of GTP bound to tubulin subunits contributes to MT rescue (Tropini et al., 2012. Aumeier et al., 2016) also demonstrated the possibility to generate GTP-islands along the MT lattice in a controlled manner by means of laser damaging and subsequent repair of the damaged site by incorporation of GTP-tubulin from solution (Schaedel et al., 2015): rescue occurred at laser-damaged sites in the presence of free GTP-tubulin (Aumeier et al., 2016). Separately, recent studies (Vemu et al., 2018; Vemu et al., 2019) reported of a damage-repair mechanism that stabilises MTs mediated by the enzymes spastin and katanin. Overall, these studies suggest that disordered GTP-islands in an otherwise structurally periodic lattice are involved in rescue regulation. Since these GTP-remnants are characterised by a random mixture of different states of tubulin, we ask if our framework might help to quantify these observations.

#### Computer simulations

We first used our coarse-grained simulations to study the role of disordered GTP-remnants in MT rescue. We generated reinforcing islands by inserting, in the middle of a fully hydrolysed, depolymerising MT, a ring consisting of several layers of GTP-tubulin dimers (Figure 4a). We then observed whether the reinforcing GTP-islands were able rescue the depolymerising MTs as a function of two parameters: 1) the length of the GTP-island $N_{rf}$ (defined here as the number of layers in the island) and 2) the fraction $ϕ$ of GTP-tubulin in the island. The results of these simulations (Video 5) are shown in Figure 4b. Note that the parameter $ϕ$ controls the amount of disorder present in the island at the level of GTP-hydrolysis. This mimics both the scenario when rescue islands are formed because not all GTP-tubulin is able to hydrolyse, as suggested in Dimitrov et al. (2008), or when rescue islands result from the incorporation of GTP-tubulin during the repair process of a damaged site, as suggested in Aumeier et al. (2016). If disorder varies slowly over time compared to the characteristic timescale of polymerisation/depolymerisation, we can model slow changes of MT mechanical properties by making the relevant mechanical parameters explicit functions of time. For the parameters in our simulation, we find that when the reinforcing island is one layer long ($N_{rf}=1$), the probability of rescue is close to zero, irrespective of the GTP-fraction in the reinforcing island. Interestingly, when $N_{rf}>1$, we observe that rescue probability $p_{rescue}$ increases with $ϕ$ in a highly nonlinear manner. Specifically, $p_{rescue}$ is either close to zero or close to one for most values of $ϕ$, with a sharp increase in the transition region.

![Figure 4.](https://cdn.elifesciences.org/articles/54077/elife-54077-fig4-v1.jpg)

**Figure 4.:** (a) Schematics showing the rescue of a depolymerising MT reinforced by a disordered GTP-tubulin island. In this example, the length of the reinforcing island is $N_{rf}=3$ and the GTP-island consists of 20 GTP-tubulin dimers, which corresponds to a GTP-fraction of $ϕ=20/(3\times13)≃0.51$ (see Video 5). (b) Simulated rescue probability by GTP-islands as a function of GTP-fraction $ϕ$ and reinforcing island length $N_{rf}$. The rescue probability $p_{rescue}$ was estimated by repeating simulations six to ten times for each pair $ϕ$ and $N_{rf}$. (c) Percolation model for the role of disordered reinforcing GTP-islands on MT rescue. (d) Simulated site percolation on a square lattice with dimensions $N_{rf}\times13$ as a function of GTP-fraction $ϕ$ and island length $N_{rf}$. The probability of percolation was obtained by averaging over 103 realisations for each pair $ϕ$ and $N_{rf}$.

![Video 5.](https://cdn.elifesciences.org/articles/54077/elife-54077-video5.mp4.jpg)

**Video 5.:** This movie illustrates the successful rescue of a depolymerising MT by a disordered GTP-island placed along the MT lattice. The mechanical parameters in this case are the same as in Video 1.

#### Percolation model of rescue

To qualitatively understand the observed nonlinear behaviour of rescue probability with GTP-fraction in the reinforcing island $ϕ$, we propose a site percolation model of rescue (Figure 4c). Site percolation is concerned with the following question: given a random graph, in which each site is (independently) occupied with probability $q$ or empty with probability $1-q$, what is the probability that a connected path of occupied sites exists between the boundaries of the graph? In our percolation model of rescue, each site of the reinforcing island is occupied by a GTP-tubulin dimer with probability $ϕ$, while it is occupied by a GDP-tubulin dimer with probability $1-ϕ$. In Sec. ’Role of quenched disorder in mechanical stability of MTs’, we have shown that the presence of randomly distributed weak lateral bonds (mediated by GDP-tubulin) can destabilise MTs mechanically when disorder is longitudinal. As such, a MT will be mechanically unstable when a connecting path of GDP-tubulins runs longitudinally through the reinforcing island (Figure 4c). The question of whether a reinforcing island with GTP-fraction $ϕ$ is able to rescue a depolymerising MT is thus analogous to site percolation with $q=ϕ$. The rescue probability $p_{rescue}$ thus relates to $1-p_{perc}$, where $p_{perc}$ is the probability of percolation of a longitudinal path of GDP-tubulin subunits through the length of the reinforcing island. Figure 4d shows that the results of site percolation on a square lattice of dimensions $13\timesN_{rf}$ with varying $ϕ$ are in qualitative agreement with simulated rescue probabilities (Figure 4b).

## Discussion

Our multi-scale approach to dynamic instability incorporates the mechanics and 3D geometry of MTs, the kinetics of tubulin addition and GTP-hydrolysis, and quenched disorder in the state of the tubulin subunit. Our results provide a series of phase diagrams for the presence of dynamic instability, revealing the dimensionless mechanical and kinetic parameters controlling the problem. Compared to previous analytic studies of dynamic instability, our results reveal the key role of the 3D geometry of MTs. In particular, we find that the mechanical stability of a MT is strongly affected by its radius (Mahadevan and Mitchison, 2005); a MT with a smaller radius is mechanically less stable than an identical MT with a larger radius.

Since MT radius has been shown to vary because the number $N_{f}$ of PFs composing MTs typically ranges between 9 to 16 (Chrétien et al., 1992; Chalfie and Thomson, 1982; Chaaban and Brouhard, 2017; Cueva et al., 2012; Díaz et al., 1998), our study suggests quantitative experimental tests via measurements of catastrophe rates $r_{c}$ as a function of PF number $N_{f}$ to verify the theoretical prediction for the rate of catastrophe $log⁡(r_{c})∝1/N_{f}^{2}$. Another key prediction from our study is that the rescuing power of GTP-islands displays a sharp drop at intermediate values of GTP-fraction. In particular, the percolation model predicts that there is a critical point for the GTP-fraction, $ϕ=ϕ_{c}$, below which reinforcing islands lose their ability to rescue MT disassembly. The numerical value of the threshold $ϕ_{c}$ depends on the thickness of the reinforcing island as well as on the MT lattice structure. This critical GTP-fraction could be determined experimentally and compared to theory by using non-hydrolyzable analogs of tubulin (Tropini et al., 2012), to control the amount of disorder at the level of the state of tubulin subunit in the island, in combination with super-resolution microscopy (Huang et al., 2009) to establish island length. Finally, we note that our assumption of the form of the quenched disorder in terms of the Gamma distribution is just that - an assumption. Further experimental work will be required to solve the inverse problem of estimating the average GTP-fraction in GTP remnants from rescue probabilities determined experimentally (Dimitrov et al., 2008; Aumeier et al., 2016; Vemu et al., 2018) to see if we might determine both the form of the disorder and the intrinsic parameters characterising it, thus allowing future research to address the question of how to control dynamic instability.
