# Mechanisms of chromosome biorientation and bipolar spindle assembly analyzed by computational modeling

## Authors

- Christopher Edelmaier<sup>1</sup> ([ORCID: 0000-0002-3673-1310](https://orcid.org/0000-0002-3673-1310))
- Adam R Lamson<sup>1</sup>
- Zachary R Gergely<sup>1</sup>
- Saad Ansari<sup>1</sup>
- Robert Blackwell<sup>1</sup>
- J Richard McIntosh<sup>2</sup>
- Matthew A Glaser<sup>1</sup>
- Meredith D Betterton<sup>1</sup> ([ORCID: 0000-0002-5430-5518](https://orcid.org/0000-0002-5430-5518)) †

### Affiliations

1. Department of Physics, University of Colorado Boulder Boulder United States
2. Department of Molecular, Cellular, and Developmental Biology, University of Colorado Boulder Boulder United States

† Corresponding author

## Abstract

The essential functions required for mitotic spindle assembly and chromosome biorientation and segregation are not fully understood, despite extensive study. To illuminate the combinations of ingredients most important to align and segregate chromosomes and simultaneously assemble a bipolar spindle, we developed a computational model of fission-yeast mitosis. Robust chromosome biorientation requires progressive restriction of attachment geometry, destabilization of misaligned attachments, and attachment force dependence. Large spindle length fluctuations can occur when the kinetochore-microtubule attachment lifetime is long. The primary spindle force generators are kinesin-5 motors and crosslinkers in early mitosis, while interkinetochore stretch becomes important after biorientation. The same mechanisms that contribute to persistent biorientation lead to segregation of chromosomes to the poles after anaphase onset. This model therefore provides a framework to interrogate key requirements for robust chromosome biorientation, spindle length regulation, and force generation in the spindle.

## Introduction

Cell biology seeks to understand how nanometer-scale molecules organize micron-scale cells, a question well-suited to theory and modeling (Marshall, 2017). As quantitative cell biology has grown, modeling has expanded in scope (Mogilner et al., 2006). Theory and simulation can now predict cellular phenomena across length and time scales, giving new insight into cellular self-organization. In the cytoskeleton, an important challenge is understanding how a relatively small number of building blocks can produce diverse structures and machines. Quantitative modeling has contributed to our understanding of cytoskeletal functions including mitosis (Mogilner and Craig, 2010; Civelekoglu-Scholey and Cimini, 2014), cytokinesis (Akamatsu et al., 2014; Stachowiak et al., 2014), and cell motility (Allard and Mogilner, 2013; Barnhart et al., 2017).

Chromosome segregation in eukaryotes is performed by the mitotic spindle, a self-organized microtubule (MT)-based machine (Bray, 2000; McIntosh et al., 2012). Dynamic spindle MTs are typically organized with their plus-ends toward the center of the spindle, forming a bipolar array as the spindle poles move apart (Figure 1; Taylor, 1959; McIntosh et al., 2012). Motor proteins and crosslinkers that bundle and slide MTs create, extend, and stabilize MT bundles (Figure 1A,B; Mann and Wadsworth, 2019; Pidoux et al., 1996; Chen et al., 2012; Hepperla et al., 2014; Hueschen et al., 2019; Yamashita et al., 2005; Janson et al., 2007; Braun et al., 2011; Lansky et al., 2015). As the spindle assembles, MTs attach to duplicated chromosomes at kinetochores and align them at the spindle midzone (Figure 1A–C; Musacchio and Desai, 2017; Hinshaw and Harrison, 2018; Hamilton et al., 2019). Biorientation occurs when sister kinetochores are attached to sister poles, but is often preceded by erroneous attachment (Figure 1D; Cimini et al., 2001; Salmon et al., 2005; Rumpf et al., 2010; Gregan et al., 2011; Lampson and Grishchuk, 2017). Kinetochores therefore perform multiple functions: they link chromosomes to MTs, maintain attachment to MT ends under force and as MTs grow and shrink, sense MT attachment and tension between sisters, and regulate correction of attachment errors and the spindle-assembly checkpoint (Sacristan and Kops, 2015; Musacchio and Desai, 2017).

![Figure 1.](https://cdn.elifesciences.org/articles/48787/elife-48787-fig1-v2.jpg)

**Figure 1.:** (A) Schematic of initial condition, showing adjacent spindle-pole bodies (blue) embedded in the nuclear envelope (gray dashed), proximal chromosomes (gray with green plate and blue springs), short microtubules (pink), and motor proteins and crosslinkers (red, blue, and black). (B) Schematic of bipolar spindle and a bioriented chromosome. (C) Schematic of chromosome and kinetochore model showing sister chromatids (gray), one kinetochore on each chromatid (green plates), the pericentric chromatin spring (blue springs), and kinetochore-MT attachment factor (blue line). (D) Schematic of chromosome attachment states, showing amphitelic, merotelic, monotelic, syntelic, and lost chromosomes. (E) Schematic of progressive restriction, showing that the angular range of kinetochore-MT attachment is restricted after attachment. (F) Schematic of misaligned destabilization of attachment, showing that misaligned attachments are destabilized. (G) Schematic of force stabilization of attachment, showing that end-on attachment to depolymerizing MTs has increased lifetime. (H) Image sequence of spindle assembly and chromosome biorientation rendered from a three-dimensional simulation. Initially, spindle-pole bodies (SPBs) are adjacent (blue disks), MTs are short spherocylinders (green and purple when unattached to kinetochores, yellow and magenta when attached), and chromosomes (cyan, yellow, magenta) are near SPBs. Motors and crosslinkers are dispersed spots (red, blue, and black) within the nucleus (gray boundary). Time shown in minutes:seconds. Lower: a zoomed view of each chromosome with attachment state labeled.

It is not fully understood how kinetochores, microtubules, and associated proteins robustly assemble a bipolar spindle and align chromosomes. In particular, it is unclear which kinetochore functions are most important for error correction and proper chromosome segregation (Lampson and Grishchuk, 2017; Sacristan and Kops, 2015). Error correction is affected by kinetochore geometry (Gregan et al., 2007; Paul et al., 2009; Rumpf et al., 2010; Magidson et al., 2015; Zaytsev and Grishchuk, 2015) and attachment/tension sensing (Sacristan and Kops, 2015; Musacchio, 2015; Musacchio and Desai, 2017; Salmon and Bloom, 2017), although the relative contribution of different effects is not established (Nannas and Murray, 2014; Tauchman et al., 2015; Kuhn and Dumont, 2017; Yoo et al., 2018). Destabilization of incorrect attachments by Aurora B kinase appears to be particularly important for high-fidelity chromosome segregation (Cheeseman et al., 2002; Cimini et al., 2006; Liu et al., 2009; Liu et al., 2010a). Therefore, further insight into the minimal mechanisms required for spindle assembly and chromosome biorientation could be gained from a computational model.

Once the spindle assembles and attaches to chromosomes, it achieves a consistent length (Dumont and Mitchison, 2009; Goshima and Scholey, 2010; Nannas et al., 2014; Rizk et al., 2014; Lacroix et al., 2018). The force-balance model proposes that outward-directed forces from plus-end directed sliding motors separate spindle poles, while inward-directed forces from minus-end directed sliding motors and chromosomes pull the poles together (Saunders and Hoyt, 1992). This model helps explain perturbations that alter spindle length (Syrovatkina et al., 2013; Hepperla et al., 2014; Chacón et al., 2014; Nannas et al., 2014). However, a change in spindle length may occur from a direct change in force production or from indirect effects such as alteration in MT dynamics or alignment (Hepperla et al., 2014; Gergely et al., 2016). In addition, the steady-state force-balance model requires extension to address spindle length fluctuations, in which the bipolar spindle assembles, but then undergoes large, dynamic length changes (Bratman and Chang, 2007; Griffiths et al., 2008; Choi et al., 2009; Hsu and Toda, 2011; Masuda et al., 2013; Wälde and King, 2014; Syrovatkina et al., 2013; Gergely et al., 2016). Computational modeling can be a valuable tool to dissect force generation and spindle length changes.

To better understand the key mechanistic requirements for chromosome biorientation and how kinetochore number and attachment affect spindle length stability, we developed a computational model of fission-yeast mitosis. Schizosaccharomyces pombe cells are amenable to genetic manipulation and quantitative experiments (Ward et al., 2015; Mary et al., 2015; Klemm et al., 2018; Blackwell et al., 2017b; Blackwell et al., 2017a) and the spindles are small enough that full 3D simulations are computationally tractable (Glunčić et al., 2015; Ward et al., 2015; Blackwell et al., 2017a; Lamson et al., 2019). We were motivated by previous work modeling spindle function and chromosome segregation (Mogilner and Craig, 2010; Civelekoglu-Scholey and Cimini, 2014). Because we study de novo spindle assembly and chromosome alignment, we could not use previous models that started with an already-bipolar structure and/or chromosomes attached to the spindle. Therefore, we extended a previous model of spindle assembly in the absence of chromosomes and kinetochore-microtubule attachments (Blackwell et al., 2017a; Rincon et al., 2017; Lamson et al., 2019) to include chromosomes and kinetochores.

Our model successfully accomplishes spindle assembly and chromosome biorientation. The results give insight into key requirements for error correction and long-lived biorientation, emphasizing the importance of progressive restriction of attachment, destabilization of misaligned attachments, and force-dependent attachment lifetime. The turnover of kinetochore-MT attachments affects spindle mechanics, because models with larger attachment lifetime exhibit larger fluctuations in spindle length. The spindle components which contribute most to force generation change over time: initial spindle -pole separation is due to the outward force from kinesin-5 motors overcoming the passive crosslinker braking force, while interkinetochore stretch is the main inward force after biorientation. Finally, properly constructed metaphase spindles are able to robustly segregate chromosomes in the model.

## Materials and methods

Computational modeling has been used previously to study the mitotic spindle (Mogilner and Craig, 2010; Vladimirou et al., 2011; Civelekoglu-Scholey and Cimini, 2014). Recent work on spindle and MT organization includes studies of spindle elongation and force balance (Brust-Mascher et al., 2015; Ward et al., 2015), the formation and maintenance of antiparallel MT overlaps (Johann et al., 2015; Johann et al., 2016), MT bundling and sliding (Hepperla et al., 2014), spindle movements and positioning (Ma et al., 2014; Garzon-Coral et al., 2016), spindle length and shape (Brugués and Needleman, 2014; Chacón et al., 2014; Hepperla et al., 2014; Gergely et al., 2016; Novak et al., 2018), MT organization (Redemann et al., 2017), and spindle assembly from a bipolar initial condition (Magidson et al., 2015; Winters et al., 2019). Models of kinetochore-MT attachment and biorientation have examined capture of lost kinetochores (Kalinina et al., 2013; Blackwell et al., 2017b), chromosome reorientation after MT attachment (Paul et al., 2009), attachment error correction (Zaytsev and Grishchuk, 2015; Tubman et al., 2017; Yoo et al., 2018; Trivedi et al., 2019), and chromosome movement on the spindle (Armond et al., 2015; Banigan et al., 2015; Gergely et al., 2016; Vukušić et al., 2017; Klemm et al., 2018). Most spindle models have started with a bipolar structure or separated spindle poles, and most previous chromosome models have begun with chromosomes attached to the spindle or near a pre-formed spindle. Because we seek to model simultaneous spindle assembly and chromosome alignment with few imposed constraints, we developed a new model, building on previous work on spindle assembly in the absence of chromosomes and kinetochore-microtubule attachments (Blackwell et al., 2017a; Rincon et al., 2017; Lamson et al., 2019).

In developing the model, we used three-dimensional geometry and an initial condition with side-by-side centrosomes (spindle-pole bodies, or SPBs) that mimics the biological configuration at the onset of mitosis. Because stochastic binding kinetics and turnover of motor proteins, crosslinkers, and kinetochore-MT attachments are important in spindle assembly and chromosome alignment, we developed methods to rapidly compute the statistical mechanics of protein binding and unbinding (Gao et al., 2015b; Gao et al., 2015a; Blackwell et al., 2016; Blackwell et al., 2017a). The binding and unbinding of motors, crosslinkers, and kinetochore-MT attachments is microscopically reversible and force-dependent. Motor proteins move with force-dependent velocity, which can be important for force generation by crosslinking motors (Blackwell et al., 2016; Blackwell et al., 2017a). We represent steric interactions between molecules (such as microtubules) with a hard-core short-range repulsive interaction, rather than soft repulsion. The simulations are based on Brownian dynamics, and state changes (such as motor binding/unbinding and an MT switching from growing to shrinking) are modeled using kinetic Monte Carlo sampling (Blackwell et al., 2017a; Blackwell et al., 2017b; Rincon et al., 2017; Lamson et al., 2019; Appendix 1, Table 1; Table 2; Table 3). We seek quantitative agreement between results from the simulation model and experiments, and so fix poorly constrained model parameters by direct comparison to data (Blackwell et al., 2017a; Rincon et al., 2017).

**Table 1.**
 Simulation, SPB, and MT parameters.


<table>
  <thead>
    <tr>
      <th>Simulation parameter</th>
      <th>Symbol</th>
      <th>Value</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Time step</td>
      <td>δ⁢t</td>
      <td>8.9 ×10-6 s</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Nuclear envelope radius</td>
      <td>R</td>
      <td>1.375 μm</td>
      <td>Kalinina et al., 2013</td>
    </tr>
    <tr>
      <td colspan="4">Spindle pole bodies</td>
    </tr>
    <tr>
      <td>Diameter</td>
      <td>σSPB</td>
      <td>0.1625 μm</td>
      <td>Ding et al., 1993</td>
    </tr>
    <tr>
      <td>Bridge size</td>
      <td></td>
      <td>75 nm</td>
      <td>Ding et al., 1993</td>
    </tr>
    <tr>
      <td>Tether length</td>
      <td>R0</td>
      <td>50 nm</td>
      <td>Flory et al., 2002; Muller et al., 2005</td>
    </tr>
    <tr>
      <td>Tether spring constant</td>
      <td>K0</td>
      <td>0.6625 pN nm-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Translational diffusion coefficient</td>
      <td>Dt</td>
      <td>4.5 × 10-4 μm2 s-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Rotational diffusion coefficient</td>
      <td>Dθ,spb</td>
      <td>0.0170 s-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Linkage time</td>
      <td>τl⁢i⁢n⁢k</td>
      <td>5 s</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td colspan="4">Microtubules</td>
    </tr>
    <tr>
      <td>Diameter</td>
      <td>σM⁢T</td>
      <td>25 nm</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Angular diffusion coefficient</td>
      <td>Dθ</td>
      <td>Depends on MT length</td>
      <td>Blackwell et al., 2017a; Kalinina et al., 2013</td>
    </tr>
    <tr>
      <td>Force-induced catastrophe constant</td>
      <td>αc</td>
      <td>0.5 pN-1</td>
      <td>Blackwell et al., 2017a; Janson et al., 2003; Dogterom and Yurke, 1997</td>
    </tr>
    <tr>
      <td>Growth speed</td>
      <td>vp,0</td>
      <td>4.1 μm min-1</td>
      <td>Blackwell et al., 2017a; Blackwell et al., 2017b</td>
    </tr>
    <tr>
      <td>Shrinking speed</td>
      <td>vs,0</td>
      <td>6.7 μm min-1</td>
      <td>Blackwell et al., 2017a; Blackwell et al., 2017b</td>
    </tr>
    <tr>
      <td>Catastrophe frequency</td>
      <td>fc,0</td>
      <td>3.994 min-1</td>
      <td>Blackwell et al., 2017a; Blackwell et al., 2017b</td>
    </tr>
    <tr>
      <td>Rescue frequency</td>
      <td>fr,0</td>
      <td>0.157 min-1</td>
      <td>Blackwell et al., 2017a; Blackwell et al., 2017b</td>
    </tr>
    <tr>
      <td>Growth speed stabilization</td>
      <td>sv⁢g</td>
      <td>1.54</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Shrinking speed stabilization</td>
      <td>sv⁢s</td>
      <td>0.094</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Catastrophe frequency stabilization</td>
      <td>sf⁢c</td>
      <td>0.098</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Rescue frequency stabilization</td>
      <td>sf⁢r</td>
      <td>18</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Stabilization length</td>
      <td>sℓ</td>
      <td>16 nm</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Minimum MT length</td>
      <td>Lmin</td>
      <td>75 nm</td>
      <td>Optimized</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Soft nuclear envelope model parameters.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Symbol</th>
      <th>Value</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Translational mobility</td>
      <td>μSPBt⁢b</td>
      <td>(0.050000.110000.11)μms−1pN−1</td>
      <td>Calculated</td>
    </tr>
    <tr>
      <td>Rotational mobility</td>
      <td>μSPBr⁢b</td>
      <td>(16.60000.1660000.166)μm−1s−1pN−1</td>
      <td>Calculated</td>
    </tr>
    <tr>
      <td>Membrane tube radius</td>
      <td>ftube</td>
      <td>87.7 nm</td>
      <td>Derényi et al., 2002; Lim et al., 2007; Lamson et al., 2019</td>
    </tr>
    <tr>
      <td>MT asymptotic wall force</td>
      <td>fMT,w</td>
      <td>2.5 pN</td>
      <td>Derényi et al., 2002; Lim et al., 2007; Lamson et al., 2019</td>
    </tr>
    <tr>
      <td>SPB asymptotic wall force</td>
      <td>fSPB,w</td>
      <td>17 pN</td>
      <td>Derényi et al., 2002; Lim et al., 2007; Lamson et al., 2019</td>
    </tr>
    <tr>
      <td>Tether spring constant</td>
      <td>K0</td>
      <td>6.625 pN nm-1</td>
      <td>Optimized</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Motor and crosslinker parameters.


<table>
  <thead>
    <tr>
      <th>Simulation parameter</th>
      <th>Symbol</th>
      <th>Value</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4">Kinesin-5</td>
    </tr>
    <tr>
      <td>Number</td>
      <td>NK⁢5</td>
      <td>174</td>
      <td>Optimized (Carpy et al., 2014)</td>
    </tr>
    <tr>
      <td>Association constant per site</td>
      <td>Ka</td>
      <td>90.9 μM-1 site-1</td>
      <td>Cochran et al., 2004</td>
    </tr>
    <tr>
      <td>One-dimensional effective concentration</td>
      <td>c2</td>
      <td>0.4 nm-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Spring constant</td>
      <td>K</td>
      <td>0.3⁢pN⁢nm-1</td>
      <td>Kawaguchi and Ishiwata, 2001</td>
    </tr>
    <tr>
      <td>Singly-bound velocity</td>
      <td>v0</td>
      <td>-100⁢nm⁢s-1</td>
      <td>Roostalu et al., 2011</td>
    </tr>
    <tr>
      <td>Polar aligned velocity</td>
      <td>v0,P</td>
      <td>-50⁢nm⁢s-1</td>
      <td>Gerson-Gurwitz et al., 2011</td>
    </tr>
    <tr>
      <td>Anti-polar aligned velocity</td>
      <td>v0,A⁢P</td>
      <td>8⁢nm⁢s-1</td>
      <td>Gerson-Gurwitz et al., 2011</td>
    </tr>
    <tr>
      <td>Singly bound off-rate</td>
      <td>k1</td>
      <td>0.11 s-1</td>
      <td>Roostalu et al., 2011</td>
    </tr>
    <tr>
      <td>Doubly bound off-rate (single head)</td>
      <td>k2</td>
      <td>0.055 s-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Tether length</td>
      <td>R0</td>
      <td>53 nm</td>
      <td>Kashlna et al., 1996</td>
    </tr>
    <tr>
      <td>Stall force</td>
      <td>Fs</td>
      <td>5 pN</td>
      <td>Valentine et al., 2006</td>
    </tr>
    <tr>
      <td>Characteristic distance</td>
      <td>xc</td>
      <td>1.5 nm</td>
      <td>Optimized (Arpağ et al., 2014</td>
    </tr>
    <tr>
      <td>Diffusion constant (solution)</td>
      <td>Dfree</td>
      <td>4.5 μ⁢m2⁢s-1</td>
      <td>Bancaud et al., 2009</td>
    </tr>
    <tr>
      <td colspan="4">Kinesin-14</td>
    </tr>
    <tr>
      <td>Number</td>
      <td>NK⁢14</td>
      <td>230</td>
      <td>Optimized (Carpy et al., 2014)</td>
    </tr>
    <tr>
      <td>Association constant (motor head)</td>
      <td>Ka,m</td>
      <td>22.727 μM-1 site-1</td>
      <td>Chen et al., 2012</td>
    </tr>
    <tr>
      <td>Association constant (passive head)</td>
      <td>Ka,d</td>
      <td>22.727 μM-1 site-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>1D effective concentration (motor head)</td>
      <td>c2⁢m</td>
      <td>0.1 nm-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>1D effective concentration (passive head)</td>
      <td>c2⁢d</td>
      <td>0.1 nm-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Spring constant</td>
      <td>K</td>
      <td>0.3⁢pN⁢nm-1</td>
      <td>Kawaguchi and Ishiwata, 2001</td>
    </tr>
    <tr>
      <td>Singly bound velocity (motor head)</td>
      <td>v0⁢m</td>
      <td>-50⁢nm⁢s-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Diffusion constant (bound, diffusing head)</td>
      <td>Dd</td>
      <td>0.1 μm2 s-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Singly bound off-rate (motor head)</td>
      <td>k1⁢m</td>
      <td>0.11 s-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Singly bound off-rate (passive head)</td>
      <td>k1⁢d</td>
      <td>0.1 s-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Doubly bound off-rate (motor head)</td>
      <td>k2⁢m</td>
      <td>0.055 s-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Doubly bound off-rate (passive head)</td>
      <td>k2⁢d</td>
      <td>0.05 s-1</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Tether length</td>
      <td>R0</td>
      <td>53 nm</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Stall force</td>
      <td>Fs</td>
      <td>5.0 pN</td>
      <td>Blackwell et al., 2017a</td>
    </tr>
    <tr>
      <td>Characteristic distance</td>
      <td>xc</td>
      <td>4.8 nm</td>
      <td>Optimized (Arpağ et al., 2014)</td>
    </tr>
    <tr>
      <td>Adjusted characteristic distance</td>
      <td>xc′</td>
      <td>1.5 nm</td>
      <td>Figure 2—figure supplement 1C</td>
    </tr>
    <tr>
      <td colspan="4">Crosslinker</td>
    </tr>
    <tr>
      <td>Number</td>
      <td>NX⁢L</td>
      <td>657</td>
      <td>Optimized (Carpy et al., 2014)</td>
    </tr>
    <tr>
      <td>Association constant</td>
      <td>Ka</td>
      <td>90.9 μM-1 site-1</td>
      <td>Cochran et al., 2004</td>
    </tr>
    <tr>
      <td>One-dimensional effective concentration</td>
      <td>c2</td>
      <td>0.4 nm-1</td>
      <td>Lansky et al., 2015</td>
    </tr>
    <tr>
      <td>Spring constant</td>
      <td>K</td>
      <td>0.207 pN nm-1</td>
      <td>Lansky et al., 2015</td>
    </tr>
    <tr>
      <td>Diffusion constant (solution)</td>
      <td>Dfree</td>
      <td>4.5 μ⁢m2⁢s-1</td>
      <td>Bancaud et al., 2009</td>
    </tr>
    <tr>
      <td>Singly bound diffusion constant</td>
      <td>Dsb</td>
      <td>0.1 μm2 s−1</td>
      <td>Lansky et al., 2015</td>
    </tr>
    <tr>
      <td>Doubly bound diffusion constant</td>
      <td>Ddb</td>
      <td>6.7×10−3μm2 s−1</td>
      <td>Lansky et al., 2015</td>
    </tr>
    <tr>
      <td>Singly bound off-rate</td>
      <td>k1</td>
      <td>0.1 s-1</td>
      <td>Kapitein et al., 2008</td>
    </tr>
    <tr>
      <td>Doubly bound off-rate</td>
      <td>k2</td>
      <td>0.05 s-1</td>
      <td>Lansky et al., 2015</td>
    </tr>
    <tr>
      <td>Parallel-to-antiparallel bindng ratio</td>
      <td>Paff</td>
      <td>0.33</td>
      <td>Kapitein et al., 2008; Rincon et al., 2017; Lamson et al., 2019</td>
    </tr>
    <tr>
      <td>Characteristic distance</td>
      <td>xc</td>
      <td>2.1 nm</td>
      <td>Optimized (Arpağ et al., 2014)</td>
    </tr>
    <tr>
      <td>Tether length</td>
      <td>R0</td>
      <td>53 nm</td>
      <td>Lansky et al., 2015; Lamson et al., 2019</td>
    </tr>
  </tbody>
</table>

### Geometry, microtubules, motors, and crosslinkers

The simulation takes place within a sphere that represents the fission-yeast nucleus. Two SPBs are embedded in the nuclear envelope but free to move on the surface of the sphere (although we also consider effects of allowing SPBs to move radially due to a soft nuclear envelope in one variant of the model, as discussed below). Each SPB nucleates 14 MTs, with their minus-ends tethered to the SPBs by a spring and which undergo dynamic instability at their plus-ends. Steric interactions are mediated by short-range hard repulsion between MTs, SPBs, and the nuclear envelope (Figure 1A,B, Appendix 1).

Three classes of motors and crosslinkers assemble the spindle (Figure 1A,B). Kinesin-5 motors (representing Cut7) move bidirectionally on MTs (Edamatsu, 2014; Edamatsu, 2016; Britto et al., 2016; Singh et al., 2018), with plus-end directed movement on antiparallel MTs exerting force to slide apart the SPBs. Kinesin-14 motors (representing Pkl1 and Klp2) crosslink MTs and one head walks toward the MT minus-ends, aligning MTs and exerting force that shortens the spindle (Pidoux et al., 1996; Troxell et al., 2001; Chen et al., 2012; Olmsted et al., 2014; Hepperla et al., 2014; Yukawa et al., 2015; Yukawa et al., 2018). Crosslinkers (representing Ase1) preferentially bind antiparallel MTs (Yamashita et al., 2005; Loïodice et al., 2005; Janson et al., 2007; Kapitein et al., 2008; Courtheoux et al., 2009; Fu et al., 2009) and stabilize MT overlaps when crosslinking near the end of an MT, an effect which mimics the recruitment of stabilizing proteins such as CLASP (Bratman and Chang, 2007) to MT ends.

### Chromosomes and kinetochores

We represent the multiple outer kinetochore proteins involved in MT binding (Sacristan and Kops, 2015; Musacchio and Desai, 2017) by a single attachment factor that can be bound or unbound to an MT. Because fission-yeast kinetochores can bind up to 3 MTs (Ding et al., 1993), each kinetochore has three attachment factors in the model separated by 40 nm along the kinetochore plate (Figure 1C, Appendix 1—figure 1). Attachments are constrained so that no more than one attachment factor can bind to the same MT plus-end. The attachment factor is a 54-nm-long spring that exerts force on the MT and kinetochore when stretched or compressed (Tables 4 and 5). Attachment factors can make both lateral and end-on attachments to MTs, with different binding kinetics that favor end-on attachment. Importantly, the model includes tip tracking: a tip-bound attachment factor tracks MT ends by maintaining end-on attachment during MT growth and shrinking. The attachment factor also includes a plus-end-directed kinetochore motor, representing the measured contribution of kinetochore-localized dimeric Cut7 to chromosome alignment (Akera et al., 2015). End-on attachment alters MT dynamic instability and is force-dependent, as measured previously (Akiyoshi et al., 2010; Miller et al., 2016).

**Table 4.**
 Chromosome and kinetochore parameters.


<table>
  <thead>
    <tr>
      <th>Simulation parameter</th>
      <th>Symbol</th>
      <th>Value</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4">Kinetochore kinematics</td>
    </tr>
    <tr>
      <td>Diameter</td>
      <td>σK⁢C</td>
      <td>200 nm</td>
      <td>Blackwell et al., 2017a; Kalinina et al., 2013</td>
    </tr>
    <tr>
      <td>Length</td>
      <td>LK⁢C,0</td>
      <td>150 nm</td>
      <td>Ding et al., 1993</td>
    </tr>
    <tr>
      <td>Width</td>
      <td>LK⁢C,1</td>
      <td>50 nm</td>
      <td>Ding et al., 1993</td>
    </tr>
    <tr>
      <td>Thickness</td>
      <td>dKC</td>
      <td>0 nm</td>
      <td>Chosen</td>
    </tr>
    <tr>
      <td>Diffusion coefficient</td>
      <td>DK⁢C</td>
      <td>5.9 × 10-4µm2 s-1</td>
      <td>Gergely et al., 2016; Blackwell et al., 2017a; Kalinina et al., 2013</td>
    </tr>
    <tr>
      <td>Translational drag</td>
      <td>γK⁢C,t</td>
      <td>3.51 pN µm-1 s</td>
      <td>Computed</td>
    </tr>
    <tr>
      <td>Rotational drag</td>
      <td>γK⁢C,r</td>
      <td>0.165 pN µm s</td>
      <td>Computed</td>
    </tr>
    <tr>
      <td>Catastrophe enhancement</td>
      <td>sKC-cen,fc</td>
      <td>0.5 pN-1</td>
      <td>Matches NE factor</td>
    </tr>
    <tr>
      <td>MT tip length</td>
      <td>lcen,tip</td>
      <td>25 nm</td>
      <td>Chosen</td>
    </tr>
    <tr>
      <td colspan="4">Interkinetochore spring</td>
    </tr>
    <tr>
      <td>Tether length</td>
      <td>RC,0</td>
      <td>100 nm</td>
      <td>Stephens et al., 2013; Gergely et al., 2016; Gay et al., 2012</td>
    </tr>
    <tr>
      <td>Linear spring constant</td>
      <td>κC</td>
      <td>39 pN µm-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Rotational spring constant</td>
      <td>κC,u</td>
      <td>1850 pN nm rad-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Alignment spring constant</td>
      <td>κC,v</td>
      <td>1850 pN nm rad-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td colspan="4">Pericentric chromatin</td>
    </tr>
    <tr>
      <td>Pericentric chromatin length</td>
      <td>rcentromere</td>
      <td>200 nm</td>
      <td>Chosen</td>
    </tr>
    <tr>
      <td>Pericentric chromatin diameter</td>
      <td>dcentromere</td>
      <td>75 nm</td>
      <td>Chosen</td>
    </tr>
    <tr>
      <td>Kinetochore-centromere offset</td>
      <td>rKC-cen</td>
      <td>37.5 nm</td>
      <td>Chosen</td>
    </tr>
    <tr>
      <td>Chromatin-MT repulsion amplitude</td>
      <td>ACMT</td>
      <td>1 pN nm</td>
      <td>Optimized</td>
    </tr>
  </tbody>
</table>

**Table 5.**
 Attachment factor parameters.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Symbol</th>
      <th>Value</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Number</td>
      <td>NA⁢F</td>
      <td>3</td>
      <td>Ding et al., 1993</td>
    </tr>
    <tr>
      <td>Attachment-site separation on kinetochore</td>
      <td>rA⁢F,e⁢x</td>
      <td>40 nm</td>
      <td>Ding et al., 1993</td>
    </tr>
    <tr>
      <td>Linear spring constant</td>
      <td>κA⁢F,m</td>
      <td>0.088 pN nm-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Angular spring constant, 0 to 1</td>
      <td>κA⁢F,r,0</td>
      <td>4.1 pN nm</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Angular spring constant, 1 to 2</td>
      <td>κA⁢F,r,1</td>
      <td>41 pN nm</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Angular spring constant, 2 to 3</td>
      <td>κA⁢F,r,2</td>
      <td>410 pN nm</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Angular spring constant, 3 to 3</td>
      <td>κA⁢F,r,3</td>
      <td>410 pN nm</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Tether length</td>
      <td>rA⁢F,0</td>
      <td>54 nm</td>
      <td>Ciferri et al., 2007</td>
    </tr>
    <tr>
      <td>kMC steps</td>
      <td>Nk⁢m⁢c</td>
      <td>10</td>
      <td>Chosen</td>
    </tr>
    <tr>
      <td>MT tip length</td>
      <td>lA⁢F,t⁢i⁢p</td>
      <td>25 nm</td>
      <td>Chosen</td>
    </tr>
    <tr>
      <td>MT tip crowding</td>
      <td>bA⁢F,t⁢i⁢p</td>
      <td>True</td>
      <td>Ding et al., 1993</td>
    </tr>
    <tr>
      <td>Tip concentration</td>
      <td>cA⁢F,t⁢i⁢p</td>
      <td>40 nm-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Side concentration</td>
      <td>cA⁢F,s⁢i⁢d⁢e</td>
      <td>0.4 nm-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Tip rate assembling</td>
      <td>kA⁢F,t⁢i⁢p,a</td>
      <td>0.0001 s-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Tip rate disassembling</td>
      <td>kA⁢F,t⁢i⁢p,d</td>
      <td>0.03 s-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Side rate</td>
      <td>kA⁢F,s⁢i⁢d⁢e</td>
      <td>0.03 s-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Tip characteristic distance assembling</td>
      <td>xc,t,a</td>
      <td>1 nm</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Tip characteristic distance disassembling</td>
      <td>xc,t,d</td>
      <td>−3.9 nm</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Side characteristic distance</td>
      <td>xc,s</td>
      <td>−0.37 nm</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Angular characteristic factor</td>
      <td>χc</td>
      <td>0.013</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Speed</td>
      <td>vA⁢F</td>
      <td>50 nm s-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Stall force</td>
      <td>fA⁢F,s⁢t⁢a⁢l⁢l</td>
      <td>5 pN</td>
      <td>Kinesin-5 (Blackwell et al., 2017a; Akera et al., 2015)</td>
    </tr>
    <tr>
      <td>Tip diffusion</td>
      <td>Dt⁢i⁢p</td>
      <td>0.0012 μm2 s-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Side diffusion</td>
      <td>Ds⁢i⁢d⁢e</td>
      <td>0.018 μm2 s-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Tip tracking</td>
      <td>fA⁢F,t⁢r⁢a⁢c⁢k</td>
      <td>0.25</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Tip-enhanced catastrophe</td>
      <td>sf⁢c,d⁢a⁢m⁢1</td>
      <td>4</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Misaligned destabilization</td>
      <td>sk,A⁢B⁢K</td>
      <td>70</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Polymerization force factor</td>
      <td>FA⁢F,v⁢g</td>
      <td>8.4 pN</td>
      <td>Akiyoshi et al., 2010; Gergely et al., 2016</td>
    </tr>
    <tr>
      <td>Depolymerization force factor</td>
      <td>FA⁢F,v⁢s</td>
      <td>−3.0 pN</td>
      <td>Akiyoshi et al., 2010; Gergely et al., 2016</td>
    </tr>
    <tr>
      <td>Catastrophe force factor</td>
      <td>FA⁢F,f⁢c</td>
      <td>−2.3 pN</td>
      <td>Akiyoshi et al., 2010; Gergely et al., 2016</td>
    </tr>
    <tr>
      <td>Rescue force factor</td>
      <td>FA⁢F,f⁢r</td>
      <td>6.4 pN</td>
      <td>Akiyoshi et al., 2010; Gergely et al., 2016</td>
    </tr>
    <tr>
      <td>Maximum polymerization speed</td>
      <td>vA⁢F,M⁢T,m⁢a⁢x</td>
      <td>30 μm min-1</td>
      <td>Gergely et al., 2016</td>
    </tr>
  </tbody>
</table>

Physically each kinetochore is a rectangular plate of length 150 nm, width 50 nm, and zero thickness (Figure 1C; Ding et al., 1993) with a steric repulsion with MTs. Sister kinetochores are linked via springs that resist stretching and rotation, to maintain the distance and alignment of the kinetochores (Figure 1C, Appendix 1—figure 1; Mary et al., 2015; Smith et al., 2016). The pericentric DNA is modeled as a spherocylinder of length 200 nm and diameter 75 nm, which has a soft repulsion with MTs that allows MT-chromatin overlap with an energy penalty (Appendix 1).

With these ingredients, the model can achieve both correct and erroneous kinetochore-MT attachment states (Figure 1D). To achieve error correction and persistent biorientation, we found three key model ingredients were required: progressive restriction of attachment (Figure 1E), destabilization of misaligned attachment (Figure 1F), and stabilization of attachment by force (Figure 1G, Appendix 1). With these mechanisms, the model exhibits both spindle assembly and chromosome biorientation (Figure 1H, Video 1).

![Video 1.](https://cdn.elifesciences.org/articles/48787/elife-48787-video1.mp4.jpg)

**Video 1.:** Initially, short MTs begin to grow at the start of the simulation and interact with nearby kinetochores. A bipolar spindle forms as the chromosomes begin to biorient. Finally, a metaphase spindle is established with bioriented chromosomes that move along the spindle and breathe. The insets are zoomed views of each chromosome, showing attachment turnover and interkinetochore stretch.

### Comparison to experimental results

To constrain model parameters, we developed multiple tests of simulation performance based on live-cell imaging, electron microscopy, and biorientation. First, we quantified the dynamics of spindle length and kinetochore position by confocal fluorescence light microscopy (Figure 2; Gergely et al., 2016; Blackwell et al., 2017a). Cells with low-level labeling of MTs with mCherry-atb2 (Yamagishi et al., 2012; Blackwell et al., 2017a) and the cen2-GFP marker on the centromeric DNA of chromosome 2 (Yamamoto and Hiraoka, 2003) allowed imaging of spindle length and centromere position (Appendix 1). The Cen2 marker is displaced only 125 nm on average from the kinetochore (Gay et al., 2012), allowing quantification of the position of a single pair of sister kinetochores. We measured spindle length and kinetochore position by fitting Gaussian spots and lines to detect features, and then tracked spindle length and kinetochore position over time using previous methods (Appendix 1; Jaqaman et al., 2008). Second, we used previously published electron tomographic reconstructions of fission yeast spindles (Grishchuk and McIntosh, 2006; McIntosh et al., 2013) to measure spindle structure (Blackwell et al., 2017a). Third, we quantified how successfully the models biorient chromosomes, measured by the fraction of simulation time during which all the chromosomes are bioriented and the average number of end-on attachments.

![Figure 2.](https://cdn.elifesciences.org/articles/48787/elife-48787-fig2-v2.jpg)

**Figure 2.:** (A–D) Experimental results. (A) Maximum-intensity-projected smoothed images from time-lapse confocal fluorescence microscopy of fission yeast with mCherry-atb2 labeling MTs (red) and cen2-GFP labeling the centromere of chromosome 2 (green). Time shown in minutes:seconds. (B) Spindle length, (C) spindle pole body-kinetochore distance, and (D) interkinetochore distance versus time for the experiment shown in (A). (E–K) Simulation results. (E) Simulated fluorescence microscopy images with MTs (red) and a single kinetochore pair (green). (F) Spindle length, (G) spindle pole body-kinetochore distance, and (H) interkinetochore distance versus time from the simulation shown in (E), sampled at a rate comparable to the experimental data in (A–D). Note that the rigid nucleus in our model sets an upper limit on spindle length of 2.75 μm, as shown by the dashed line in F. (I) Spindle length versus time for 12 simulations of the reference model. (J) Spindle length versus time for 12 simulations in a model lacking kinesin-5. (K) Spindle length versus time for 12 simulations in a model lacking crosslink-mediated microtubule stabilization. (L) Fraction of simultaneous biorientation for the reference, kinesin-5 delete, and no-stabilization models (N = 12 simulations per data point).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/48787/elife-48787-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Simulated spindles form and biorient chromosomes in the absence of kinesin-14 motors if kinesin-5 and crosslinker number are increased. (B) Simulated spindles have difficulty forming in the absence of crosslinkers, and do not properly biorient chromosomes. (C) Lowering the characteristic distance of force-dependent unbinding of kinesin-14 to that of kinesin-5 (which makes kinesin-14 motors less sensitive to force-induced unbinding) causes longer spindles to form that are capable of biorienting chromosomes. (D) Spindle length as a function of wall force for a model of a soft nuclear envelope for which the SPBs are not fixed on the surface of the sphere. The reference model contains 174 kinesin-5 motors, 230 kinesin-14 motors, and 657 crosslinkers. (N = 12 simulations per data point.).

We combined these measures of simulation performance in a fitness function which quantifies the overall success of each simulation run with a set of model parameters. We then varied poorly constrained model parameters to maximize the fitness function. The optimized parameters defined the reference model (Appendix 1).

## Results

### A computational model can assemble a bipolar spindle and biorient chromosomes

To understand the mechanisms most important for proper chromosome alignment on the spindle, we developed a computational model of fission-yeast mitosis (Figure 1) that includes spindle MTs nucleated from SPBs, crosslinking motors, passive crosslinkers, pericentric chromatin, and kinetochores, all contained within a spherical nucleus (Materials and methods, Figure 1A,B). Kinetochore-MT binding occurs via attachment factors that represent MT-binding kinetochore proteins (Figure 1C), which can form both correct and erroneous MT-kinetochore attachments (Figure 1D). Kinetochore-MT attachments progressively restrict in angle as MTs bind (Figure 1E), a mechanism motivated by previous work on kinetochore geometry and chromosome rotation in error correction (Gregan et al., 2007; Rumpf et al., 2010; Paul et al., 2009; Magidson et al., 2015; Zaytsev and Grishchuk, 2015). In particular, work on the S. pombe monopolin complex has proposed that monopolin acts as a site-clamp that co-orients MTs bound to the same kinetochore (Gregan et al., 2007). To correct attachment errors, we included destabilization of improper attachments and tip-enhanced catastrophe (Figure 1F), mimicking the effectsof Aurora B kinase (DeLuca et al., 2006; Cimini et al., 2006; Gay et al., 2012) and recapture of lost kinetochores by MT depolymerization (Grishchuk and McIntosh, 2006; Franco et al., 2007; Gachet et al., 2008; Gao et al., 2010; Gergely et al., 2016). To maintain biorientation, we implemented force-dependent kinetochore-MT attachment kinetics (Figure 1G), based on previous work that demonstrated an increase in attachment lifetime with tension when kinetochores are attached to depolymerizing MTs (Akiyoshi et al., 2010; Miller et al., 2016). For further details of the construction of the model, see Materials and methods and Appendix 1. With these ingredients, the model is able to spontaneously assemble a bipolar spindle starting with side-by-side SPBs, form MT-kinetochore attachments, correct attachment errors, and biorient the chromosomes (Figure 1H, Video 1).

To refine and test the model, we measured spindle assembly and chromosome alignment in fission yeast (Figure 2, Materials and methods, Appendix 1). We quantified spindle length, SPB-kinetochore separation, and interkinetochore stretch from the onset of mitosis until chromosome segregation (Figure 2A–D) and used these data to adjust model parameters (Materials and methods, Appendix 1). After refinement, simulations of the reference model showed dynamics of SPB separation, kinetochore movement along the spindle, and interkinetochore stretch similar to the experimental data (Figure 2E–H, Video 2). As occurs in cells, the dynamics varied from simulation to simulation, but were similar on average (Figure 2I, Appendix 1—figure 2).

![Video 2.](https://cdn.elifesciences.org/articles/48787/elife-48787-video2.mp4.jpg)

**Video 2.:** The simulated fluorescence images are rotated so that the spindle is vertical. Lower: simulation of models mimicking genetic perturbation. Lower left: Model lacking kinesin-5 motors. The SPBs never separate and the spindle remains monopolar. Chromosomes do not biorient. Lower right: Model lacking crosslinker-mediated stabilization of MT dynamics. SPBs separate only slightly, forming a short spindle that is nearly indistinguishable from a monopolar spindle. Chromosomes do not biorient.

### Single model perturbations recapitulate the requirement for kinesin-5 motors and CLASP

After developing the reference model, we verified that single model perturbations recapitulate results from fission-yeast genetics. Kinesin-5 motors are essential for spindle assembly in S. pombe, and temperature-sensitive mutants of the kinesin-5/Cut7 fail to separate spindle-pole bodies (Hagan and Yanagida, 1990; Hagan and Yanagida, 1992; Yukawa et al., 2018; Toda et al., 2018). Consistent with this, when we remove kinesin-5 from the model, SPBs do not separate (Figure 2J). Similarly, the microtubule-associated protein CLASP is essential for spindle assembly in fission yeast, where it is recruited to MT antiparallel overlaps by Ase1 and stabilizes MT dynamics (Bratman and Chang, 2007). When the stabilization of dynamics of crosslinked MTs is turned off in the model, SPBs do not separate (Figure 2K). Chromosome biorientation is abolished in models where the SPBs do not separate (Figure 2L, Video 2).

We further studied combined perturbations (Figure 2—figure supplement 1) by varying kinesin-5 and crosslinker number in the absence of kinesin-14 (Figure 2—figure supplement 1A) and by varying kinesin-5 and −14 number in the absence of crosslinkers (Figure 2—figure supplement 1B). Kinesin-14 in our models combines the functions of fission-yeast Pkl1 and Klp2, neglecting the anchoring of MT minus-ends to SPBs by Pkl1 previously measured (Olmsted et al., 2014; Syrovatkina and Tran, 2015; Yukawa et al., 2015; Yukawa et al., 2018). Experimentally, cells lacking Klp2 or both Pkl1 and Klp2 do not show altered average spindle length (Syrovatkina et al., 2013; Troxell et al., 2001). Consistent with this, model spindles formed and bioriented chromosomes in the absence of kinesin-14, and spindle length depended on the ratio of kinesin-5 to crosslinkers.

In fission yeast, Ase1 deletion cells assemble spindles (Yamashita et al., 2005; Syrovatkina et al., 2013; Yukawa et al., 2019). To test if our model correctly reproduced these results, we removed the crosslinker from the model and varied the number of kinesin-5 and kinesin-14 molecules present (Figure 2—figure supplement 1B). Removing crosslinkers in the reference model abolished spindle assembly because spindles cannot maintain robust antiparallel MT overlaps. However, in the reference model the kinesin-14 motors are highly sensitive to force-dependent unbinding: the characteristic distance that quantifies this is 3.2 times larger for kinesin-14 motors than kinesin-5 motors. This leads to kinesin-14 motors that unbind relatively easily under force, and they fail to maintain microtubule antiparallel overlaps necessary for bipolar spindle assembly. When we model the kinesin-14 motors with the same force sensitivity to unbinding as for the kinesin-5 motors, spindle formation and chromosome biorientation are rescued (Figure 2—figure supplement 1C).

Most of our simulations represent the nuclear envelope as a rigid sphere with the SPBs constrained to move on the surface of this sphere. However, constraining SPBs to a fixed radius alters force balance on the spindle and may alter spindle length. Therefore, we tested a model of a soft nuclear envelope by allowing the SPBs to move radially in a potential that mimics the energy required to deform the nuclear envelope (Rincon et al., 2017; Lamson et al., 2019) (Materials and methods, Appendix 1). The results show that a soft nuclear envelope leads to slightly longer spindles (Figure 2—figure supplement 1D, Video 3), but for a physically realistic nuclear envelope force of around 17 pN, spindle length remains near 3 μm, as measured experimentally.

![Video 3.](https://cdn.elifesciences.org/articles/48787/elife-48787-video3.mp4.jpg)

**Video 3.:** SPBs are able to move away from their preferred radius from the center of the nucleus. The spindle reaches a bounded length, and chromosomes are able to biorient. Spindle length larger than the nuclear envelope radius is reached by the balance of force from motors, crosslinkers, chromosomes.

### Chromosome biorientation during spindle assembly requires three basic kinetochore properties

Our simulations start in a state mimicking early mitosis with monotelic chromosomes, then spontaneously assemble a bipolar spindle and biorient chromosomes. Biorientation requires the model to correct attachment errors and maintain correct attachments. This occurs in the simulations primarily through progressive restriction of attachment angle, misaligned destabilization, and force-dependent kinetochore-MT attachment.

### Kinetochores can avoid merotelic attachments by progressive restriction of microtubule binding

To facilitate correct initial attachment of MTs to kinetochores, the model progressively restricts the angle at which binding can occur as more MTs bind (Figure 1E). This is motivated by previous work demonstrating that kinetochore geometry and chromosome rotation play an important role in promoting correct kinetochore-MT attachment and correcting errors (Gregan et al., 2007; Rumpf et al., 2010; Paul et al., 2009; Magidson et al., 2015; Zaytsev and Grishchuk, 2015). We have extended previous work to include both multiple MT binding sites per kinetochore and changes in kinetochore geometry upon binding. In our model, unattached kinetochores have a wide angular range over which attachments can form (modeled as an angular spring constant for binding, represented by the three wide cones in Figure 1E left). Each attachment formed narrows the angle allowed for the subsequent attachment, favoring attachment to MTs that are more perpendicular to the kinetochore plate (represented by the narrower cones in Figure 1E right). Attachments exert an alignment force/torque on kinetochores and MTs based on the stiffness of this angular spring.

To illustrate the importance of progressive restriction, we removed it, making the angular range identical for all three kinetochore-MT attachment events (Figure 3A, Video 4). Doing this nearly abolishes biorientation in the model: the fraction of simulation time for which all three chromosomes are bioriented is below 10%, independent the value of the angular spring constant from 1 $k_{B}⁢T$ (almost any angle of attachment is allowed) to 100 $k_{B}⁢T$ (attachment is highly restricted in angle). These failures occur for different reasons as the angular spring constant varies. When attachment angle is most permissive, merotelic attachments form and are not corrected sufficiently rapidly to biorient the chromosomes. When the attachment angle is highly restricted, attachments are unlikely to form at all. Overall, this result shows that in our model progressive restriction of attachment is essential for biorientation.

![Figure 3.](https://cdn.elifesciences.org/articles/48787/elife-48787-fig3-v2.jpg)

**Figure 3.:** (A) Fraction simultaneous biorientation versus angular spring stiffness in models lacking progressive restriction of attachment. (B) Fraction simultaneous biorientation versus the first angular spring stiffness in the model with progressive restriction. (C) Fraction simultaneous biorientation versus the third angular spring stiffness in the model with progressive restriction. (D) Fraction simultaneous biorientation versus the misaligned destabilization factor. (E) Effects of force-dependent error correction. Top, schematic of stabilization of kinetochore-MT attachments as a function of interkinetochore force. Left, Stabilization as a function of interkinetochore tension for a characteristic force of 1.67 pN. When the interkinetochore force is the characteristic force, attachment turnover is reduced by a factor of two, as shown by the red dashed lines. Right, fraction simultaneous biorientation versus the characteristic force. (F) Fraction simultaneous biorientation for different types of force-dependent kinetics (N = 12 simulations per data point).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/48787/elife-48787-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Angular spring stiffness for the middle value chosen in progressive restriction did not affect chromosome biorientation fidelity. In these models, the first and third angular spring stiffnesses were fixed at 1 $k_{B}⁢T$ and 100 $k_{B}⁢T$, respectively. (B) Varying the number of microtubule attachment sites per kinetochore does not significantly alter biorientation in the model. We varied the angular spring stiffnesses are varied with the number of attachments shown as (1: [1 $k_{B}⁢T$, 1 $k_{B}⁢T$], 2: [1 $k_{B}⁢T$, 10 $k_{B}⁢T$, 10 $k_{B}⁢T$], 3: Reference model, 4–6: [1 $k_{B}⁢T$, 10 $k_{B}⁢T$, 100 $k_{B}⁢T$, 100 $k_{B}⁢T$, … 100 $k_{B}⁢T$]) (N = 12 simulations per data point).

![Video 4.](https://cdn.elifesciences.org/articles/48787/elife-48787-video4.mp4.jpg)

**Video 4.:** Top left: Model lacking progressive restriction, with a common angular spring stiffnesses of 1 $k_{B}⁢T$ for all attachments. A short bipolar spindle forms, but chromosomes are typically merotelically attached and do not biorient. Top middle: Model lacking progressive restriction, with a common angular spring stiffnesses of 100 $k_{B}⁢T$ for all attachments. A long bipolar spindle forms, kinetochore-MT attachments are transient, and chromosomes do not generate significant inward force on the spindle. Top right: Model including progressive restriction with an angular spring stiffness of 20 $k_{B}⁢T$ for the first binding event, leading to restricted attachments. A long bipolar spindle forms, and kinetochore-MT attachments are transient. Lower left: model including progressive restriction but with an angular spring stiffness of 20 $k_{B}⁢T$ for the third binding event, leading to permissive attachments. Error correction is impaired, and chromosomes are typically merotelically attached. Lower middle: Model lacking misaligned destabilization. Error correction is impaired. Lower right: Model with force-independent attachment kinetics. Kinetochore-MT attachments are not stabilized under tension from depolymerizing microtubules, leading to short-lived biorientation.

The progressive restriction model requires that the first binding event be relatively permissive in angle, the second more restricted, and the third highly restricted. To study this, we varied the angular spring constant of each attachment independently (Figure 3B,C, Figure 3—figure supplement 1, Video 4). The model achieves a high fraction of simultaneous biorientation around 70% when the first attachment is maximally permissive (spring constant is 1 $k_{B}⁢T$); an increase in this spring constant restricts the angle and decreases simultaneous biorientation to below 20% (Figure 3B). This means that for the first attachment, promoting kinetochore binding to any MT is important: initial attachments should be established easily, even if erroneous. By contrast, biorientation is increased when the third (final) binding event is highly restricted (Figure 3C): chromosomes are bioriented in the model <10% of the time when the third attachment is most permissive, but the fraction of simultaneous biorientation increases with the angular stiffness of the third binding site. The second value of the angular potential for progressive restriction was less important (Figure 3—figure supplement 1A): varying it did not significantly change the fraction of simultaneous biorientation.

Because of the importance of progressive restriction in our model, we additionally examined whether varying the number of allowed kinetochore-MT attachments might affect how easily biorientation is achieved, but found no significant effect (Figure 3—figure supplement 1B). In these simulations, we chose how to vary the angular spring stiffness as the number of attachment sites varies. For fewer attachment sites, we chose the lower values of angular spring stiffnesses for progressive restriction that matched the reference stiffness. For increased number of attachments, the later attachments were fixed at an upper limit of 100 $k_{B}⁢T$. In all cases, chromosome biorientation was not compromised.

### Error correction occurs through the destabilization of improper attachments

Progressive restriction of attachment reduces but does not eliminate erroneous kinetochore-MT attachments. Previous experimental work has shown that merotelic attachments are common in early mitosis and are corrected over time (Cimini et al., 2003) due to increased turnover of kinetochore MTs from the activity of Aurora B kinase (DeLuca et al., 2006; Cimini et al., 2006; Gay et al., 2012). To study this, we considered two different error correction models: biorientation-dependent stabilization and force-dependent stabilization. First, we implemented the rule-based model of misaligned destabilization by accelerating the detachment of kinetochore-MT attachments that are not amphitelic (Figure 1F). Because experimental work has demonstrated a decrease in kinetochore MT turnover by up to a factor of 65 in the presence of Aurora B inhibitors (Cimini et al., 2006), we varied the misaligned destabilization factor in the model, which quantifies the increased turnover of incorrect attachments, over a similar range from 1 to 100 (Figure 3D, Video 4). Consistent with experimental results, biorientation is nearly eliminated in the absence of misaligned destabilization. Biorientation time in the model is maximum when the misaligned destabilization factor is 70, comparable to the experimental value. This demonstrates the importance of error correction in the model.

The biorientation-dependent model has the disadvantage that it cannot test any mechanisms by which incorrect attachments are destabilized. We therefore additionally tested a force-dependent error correction model, based on previous results that kinetochore-MT attachments are stabilized by force (Nicklas and Koch, 1969; Cane et al., 2013). We modeled the kinetics of kinetochore-MT attachments as a function of interkinetochore tension, with the rates decreasing with force (Figure 3E, Video 5), controlled by a a characteristic force for significant stabilization.

![Video 5.](https://cdn.elifesciences.org/articles/48787/elife-48787-video5.mp4.jpg)

**Video 5.:** The spindle forms in a few minutes, and chromosomes form stable, bioriented attachments. Zoomed views of chromosomes shows them forming load-bearing attachments to the tips of MTs. The interkinetochore characteristic force is 1.67 pN.

The force-stabilization model of error correction that we implemented experiences the initial problem of biorientation (IPBO): a bioriented attachment that has just formed is not under tension, and therefore is not stable (Zhang et al., 2013; Kalantzaki et al., 2015; Tubman et al., 2017). Consistent with this, we found implementing force-dependent stabilization alone did not lead to biorientation. Recent work has suggested that the IPBO may be solved by initial syntelic-like attachments that are end-on between the kinetochore face near a pole, and lateral to the kinetochore farther from that same pole (Kuhn and Dumont, 2017). Therefore, we varied parameters in the model that might facilitate tension generation before biorientation, including the angular spring constants of the interkinetochore spring, the characteristic angular factor for binding high angles to the kinetochore plate, the effective concentration for binding laterally, and the number of kinesin-5 motors, which affect overall spindle force generation. We were able to achieve long-lived biorientation in the force-dependent error correction model with model parameters that favored end-on over lateral attachments, inhibited attachments at high angle, and allowed sister kinetochores to more easily reorient (Table 6).

**Table 6.**
 Force-dependent error correction model parameters.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Symbol</th>
      <th>Value</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Inter-kinetochore stabilization force</td>
      <td>FEC,0</td>
      <td>1.67 pN</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Rotational spring constant</td>
      <td>κC,u</td>
      <td>925 pN nm rad-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Alignment spring constant</td>
      <td>κC,v</td>
      <td>925 pN nm rad-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Angular characteristic factor</td>
      <td>χc</td>
      <td>0.08</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Side concentration</td>
      <td>cAF,side</td>
      <td>0.32 nm-1</td>
      <td>Optimized</td>
    </tr>
    <tr>
      <td>Kinesin-5 number</td>
      <td>NK5</td>
      <td>200</td>
      <td>Optimized</td>
    </tr>
  </tbody>
</table>

In this version of the model, we then varied the characteristic force that controls how much attachments are stabilized by force (Figure 3E, Video 5). The characteristic force is the value of the interkinetochore force at which attachments are stabilized by a factor of two, so a small value reflects rapid variation of attachment stability with force, while an infinite value means that attachments are force independent. We found that the model is sensitive to the value of this characteristic force, with best performance of the model at a characteristic force of 1.67 pN. Higher or lower values decrease cumulative biorientation by up to a factor of two.

### Persistent biorientation is achieved through force-dependent kinetochore-microtubule attachment

Once amphitelic kinetochore-MT attachments are formed, they must be maintained for biorientation to persist. Attachments between single MTs and purified budding-yeast kinetochores were altered by force applied to the kinetochore, even in the absence of Aurora kinase (Akiyoshi et al., 2010; Miller et al., 2016). In particular, the kinetochore-MT attachment lifetime increased with tension when kinetochores were attached to depolymerizing MTs, an effect dependent on a TOG protein (Akiyoshi et al., 2010; Miller et al., 2016). Consistent with this, we implemented force dependence of attachments in the model (Figure 1G). This effect is required to maintain biorientation: if we eliminate the force dependence of attachment kinetics, biorientation is nearly abolished in the model (Figure 3F, Video 4). To understand which force-dependent rate is most important for this effect, we added them back to the model one at a time. The increase in attachment lifetime of a kinetochore bound to a shrinking MT is the key force-dependent rate, because making this the only force-dependent lifetime in the model restores nearly all biorientation compared to the model with all rates force-dependent (Figure 3F). This demonstrates that maintenance of biorientation requires kinetochore-MT attachments to persist during MT depolymerization.

### Slow turnover of kinetochore-microtubule attachments can cause spindle length fluctuations

Spindle length regulation (Dumont and Mitchison, 2009; Goshima and Scholey, 2010; Syrovatkina et al., 2013; Hepperla et al., 2014; Nannas et al., 2014; Rizk et al., 2014) can be understood using the force-balance model of Saunders and Hoyt in which plus-end directed sliding motors produce outward force, and minus-end directed sliding motors and chromosomes produce inward force (Saunders and Hoyt, 1992; Nabeshima et al., 1998; Goshima et al., 1999; Severin et al., 2001; Tolić-Nørrelykke et al., 2004; Bouck and Bloom, 2007; Stephens et al., 2013; Syrovatkina et al., 2013; Costa et al., 2014; Zheng et al., 2014; van Heesbeen et al., 2014; Syrovatkina and Tran, 2015). The force-balance model has been used in mathematical models of spindles in yeast (Gardner et al., 2005; Gardner et al., 2008; Chacón et al., 2014; Hepperla et al., 2014; Ward et al., 2015; Blackwell et al., 2017a; Rincon et al., 2017; Lamson et al., 2019), and Drosophila (Cytrynbaum et al., 2003; Cytrynbaum et al., 2005; Wollman et al., 2008; Civelekoglu-Scholey and Scholey, 2010) cells. This work has focused on spindle length at steady state, not dynamic changes. However, some fission-yeast mutants exhibit large fluctuations in spindle length in which the bipolar spindle assembles, but then shortens or falls apart, known as spindle collapse (Bratman and Chang, 2007; Griffiths et al., 2008; Choi et al., 2009; Hsu and Toda, 2011; Masuda et al., 2013; Wälde and King, 2014; Syrovatkina et al., 2013; Gergely et al., 2016). Remarkably, fission-yeast double mutants can have wild-type average metaphase spindle length, but much larger fluctuations than wild-type (Syrovatkina et al., 2013). The underlying mechanisms of large spindle length fluctuations have remained unclear, in part because apparently contradictory changes can cause it. For example, deletion of proteins known either to stabilize (Bratman and Chang, 2007) or destabilize MTs (Gergely et al., 2016) can both lead to large spindle length fluctuations. In recent work we examined how deletion of the kinesin-8 motor proteins could contribute to large spindle length fluctuations in fission yeast (Gergely et al., 2016), but a general understanding of this phenomenon is lacking. Therefore, we sought to understand what mechanisms might lead to large length fluctuations.

One key determinant of the magnitude of spindle length fluctuations is the lifetime of kinetochore-MT attachments (Figure 4, Video 6). We quantified the magnitude of length fluctuations by determining the standard deviation in spindle length over time after spindle elongation for each individual simulation of the model, then averaging that standard deviation over multiple model runs with the same parameters. This measure of length fluctuations increases with kinetochore-MT attachment lifetime: the longer the lifetime, the larger the fluctuations (Figure 4A–D).

![Figure 4.](https://cdn.elifesciences.org/articles/48787/elife-48787-fig4-v2.jpg)

**Figure 4.:** (A–C) Spindle length versus time for 24 simulations of the same model, with (A) short (1/4 the reference value), (B) intermediate (1/2 the reference value), and (C) long (twice the reference value) kinetochore-MT attachment lifetime. (D) Length fluctuation magnitude versus measured kinetochore-MT attachment lifetime and average interkinetochore stretch (color) for bioplar spindles (corresponding to simulation time >10 min.). (E) Length fluctuation magnitude versus measured kinetochore-MT attachment lifetime and average interkinetochore stretch (color) for the reference, restricted, and weak rescue models (N = 24 simulations per data point).

![Video 6.](https://cdn.elifesciences.org/articles/48787/elife-48787-video6.mp4.jpg)

**Video 6.:** Left: Model with short attachment lifetime in which the kinetochore-MT binding and unbinding rates are 4 times larger than in the reference model. Biorientation is somewhat compromised. Middle: Model with intermediate attachment lifetime in which the kinetochore-MT binding and unbinding rates are 2 times larger than in the reference model. Right: Model with long attachment lifetime in which the kinetochore-MT binding and unbinding rates are 2 times smaller than in the reference model. Biorientation is preserved and the spindle undergoes large length fluctuations.

To understand this result, note that for long-lived attachment, the force exerted by a stretched kinetochore can grow over time to a larger value: long-lived attachment allows multiple MTs to bind per kinetochore, exert greater force, and stretch apart the sisters. This allows larger inward force to be exerted on the spindle by attached kinetochores. Indeed, the average interkinetochore distance increases with kinetochore-MT attachment lifetime (Figure 4D). Thus, slow cycles of attachment and detachment lead to slowly varying force on the spindle that causes its length to fluctuate. In the opposite limit, short-lived kinetochore-MT attachment causes relatively quick turnover, limiting interkinetochore stretch, inward force, and variation in inward force.

Alteration in kinetochore-MT attachment lifetime could occur through multiple molecular mechanisms. To illustrate how this could occur, we considered two perturbations to the model that have downstream effects on both lifetime and length fluctuations (Figure 4E). The first perturbation is a restricted attachment model, in which the angular spring constant of attachment discussed above (Figure 3A) is set to 100 $k_{B}⁢T$ for all attachments. In this case, attachments rarely form and when formed, their lifetime is short ($<0.05$ min on average). As a result, the force produced by interkinetochore stretch is small and does not vary much, leading to small length fluctuations in the model ($<0.01\mu$ μm on average). The opposite limit can occur in a model in which the force-dependent rescue of kinetochore MTs is greatly reduced, by increasing the force constant from 6.4 pN to 12.8 pN (this reduces the force sensitivity of rescue, see Appendix 1). This causes kinetochore MTs to depolymerize for longer time, and because kinetochore-MT attachments are stabilized during depolymerization, this change dramatically increases the attachment lifetime to 0.2 min. As a result, interkinetochore stretch can increase, and length fluctuations correspondingly increase (0.3 μm).

This analysis suggests that altered kinetochore-MT attachment lifetime could be a downstream effect that may result from the diverse mutations observed to cause spindle length fluctuations in S. pombe. We note that the effect of lifetime may not be the only source of spindle length fluctuations: other mutations that lead to slow changes in force exerted on the spindle could have similar effects.

### Force generation in the spindle varies during spindle elongation

The force-balance model can explain why multiple perturbations alter steady-state spindle length, including mutation of motors and microtubule-associated proteins (Syrovatkina et al., 2013; Hepperla et al., 2014), and chromosome/kinetochore number and chromatin stiffness (Chacón et al., 2014; Nannas et al., 2014). However, it can be challenging to distinguish direct from indirect effects of altering force balance. For example, the force-balance model posits that minus-end-directed kinesin-14 motors contribute inward force that shortens the spindle, so their deletion would be expected to lead to longer spindles. However, in budding yeast, kinesin-14 deletion instead leads to shorter spindles, because kinesin-14 helps bundle spindle MTs, allowing kinesin-5 motors to generate greater outward force when kinesin-14 is present (Hepperla et al., 2014). Similarly, kinesin-8 deletion in fission yeast leads to longer spindles, but this is likely due to effects of this motor on MT dynamics rather than direct inward force generation by kinesin-8 (Syrovatkina et al., 2013; Gergely et al., 2016).

To better understand direct and indirect changes in spindle length, we examined the force produced by spindle molecules as the spindle elongates, averaged over many simulation runs (Figure 5, Video 7). In this analysis, we considered each half-spindle separately, and calculated the total force exerted along the spindle axis produced by separate force-generating elements: outward force by kinesin-5 motors, and inward force by kinesin-14 motors, passive crosslinkers, and kinetochore-MT attachments (Figure 5A). We computed spindle length as a function of time (Figure 5B,E,H), force as a function of time (Figure 5C,F,I) and spindle length (Figure 5D,G,J) in the reference, restricted attachment, and weak rescue models.

![Figure 5.](https://cdn.elifesciences.org/articles/48787/elife-48787-fig5-v2.jpg)

**Figure 5.:** (A) Schematic of force generation along the spindle axis, showing kinesin-5 motors exerting outward force (red) and kinesin-14 (dark blue), crosslinkers (black), and kinetochore-MT attachment to stretched chromosomes (light blue) exerting inward force. (B, E, H) Spindle length versus time, (C, F, I) average spindle axis force versus time, and (D, G, J) average spindle axis force versus spindle length for three different models: (B–D) the reference model, (E–G) the restricted attachment model, and (H–J) the weak rescue model (N = 24 simulations per data point).

![Video 7.](https://cdn.elifesciences.org/articles/48787/elife-48787-video7.mp4.jpg)

**Video 7.:** Left: The reference model shows typical spindle length fluctuations. Middle: The restricted attachment model shows minimal length fluctuations, because transient kinetochore-MT attachments lead to low inward force on the spindle from chromosomes. Right: The weak rescue model shows large spindle length fluctuations, because kinetochore MTs remain attached while depolymerizing, leading to high and fluctuating inward force on the spindle from chromosomes.

### The early bipolar spindle forms due to motors and crosslinkers, not chromosomes

Force generation by kinesin-5 motors, kinesin-14 motors, crosslinkers, and chromosomes changes significantly as the bipolar spindle assembles. For early time (up to 5 min) when spindles are short (up to 1 μm), motors and crosslinkers exert force that slowly increases in magnitude up to a few tens of pN, but chromosomes exert almost no force (Figure 5C,F,I, Video 7). Because chromosomes are not bioriented on the spindle during initial SPB separation, they do not exert significant inward force. This result is consistent with our previous work, which demonstrated that initial bipolar spindle assembly can occur in a model lacking chromosomes (Blackwell et al., 2017a; Rincon et al., 2017; Lamson et al., 2019).

The outward sliding force produced by kinesin-5 motors increases approximately linearly with spindle length, as the length of antiparallel MT overlaps increases during spindle assembly (Figure 5D,G,J). This agrees with the experimental result that the sliding force generated by kinesin-5 motors is proportional to overlap length (Shimamoto et al., 2015). The inward force generated by kinesin-14 motors is small, as in previous work that has shown that kinesin-14 is less effective at force generation that kinesin-5 (Hentrich and Surrey, 2010) and that in the spindle kinesin-14 may be more important to align spindle MTs than to generate force directly (Hepperla et al., 2014).

During initial spindle assembly, crosslinkers play the primary role of maintaining antiparallel MT overlaps in opposition to the sliding activity of kinesin-5. Remarkably, we find that the inward force generated by passive crosslinkers initially increases with spindle length to approximately 25 pN when the spindle is 0.75 μm long. Beyond this point, the crosslinker force steadily decreases, dropping to near zero within a few minutes (Figure 5C,F,I). This is consistent with previous results on force generation by the crosslinker Ase1, which found large force for small overlaps that drops significantly as overlaps become larger (Lansky et al., 2015). Therefore, our results support a picture of early spindle assembly in which high braking force by crosslinkers on short antiparallel MT overlaps oppose the outward force generated by kinesin-5. This highlights the key role of crosslinkers in early spindle assembly suggested previously (Blackwell et al., 2017a; Rincon et al., 2017; Lamson et al., 2019).

### Metaphase spindle length is determined primarily by interkinetochore stretch and kinesin-5 motors

Once the spindle elongates sufficiently to separate SPBs by 1 μm, there is a transition in the primary contributer to spindle force. In this regime, chromosomes biorient and the inward force from interkinetochore stretch becomes significant, balancing outward force from kinesin-5 motors (Figure 5C,F,I). This balance is crucial to setting metaphase spindle length.

To perturb this force balance, we considered two additional models discussed above (Figure 4E) with restricted attachment and weak rescue. When attachment is restricted, chromosomes rarely biorient and the inward force from chromosomes is small for spindles of all length. This leads to unbalanced force from kinesin-5 motors and long spindles (Figure 5E–G, Video 7). When MT rescue is reduced, interkinetochore stretch is larger and the inward force from stretched sister kinetochores increases (Figure 5H–J, Video 7). This leads to shorter metaphase spindle length and a corresponding increase in force from stretched kinetochores.

### Chromosome segregation can occur via the same mechanisms that assemble the spindle

After developing the model of spindle assembly and chromosome biorientation, we examined what additional mechanisms were required for the model to segregate chromosomes to the poles. Relatively few changes are required for robust chromosome segregation, suggesting that significant new mechanisms are not required in anaphase for chromosome segregation. The rules added to the model for anaphase A include severing the chromatin spring between kinetochores (based on cumulative time the chromosomes are bioriented), stabilization of kinetochore-MT attachment, and depolymerization of MTs (Table 7). With these additions to the model, simulations consistently segregate chromosomes to the poles (Figure 6A–D, Video 8). We compared our simulations to experimental measurements of chromosome segregation, and found similar speed of chromosome movement to the poles and separation of sisters (Figure 6E–G), as expected from the choice of MT depolymerization speed in the anaphase model.

**Table 7.**
 Anaphase parameters.


<table>
  <thead>
    <tr>
      <th>Anaphase</th>
      <th>Symbol</th>
      <th>Value</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Integrated simultaneous biorientation time</td>
      <td>τSAC</td>
      <td>4.45 min</td>
      <td>Chosen</td>
    </tr>
    <tr>
      <td>Anaphase attachment rate</td>
      <td>kAF,anaphase</td>
      <td>0.00007 s-1</td>
      <td>Chosen</td>
    </tr>
    <tr>
      <td>Anaphase MT depoly speed</td>
      <td>vanaphase,s,0</td>
      <td>2.2 µm min-1</td>
      <td>Chosen</td>
    </tr>
  </tbody>
</table>

![Figure 6.](https://cdn.elifesciences.org/articles/48787/elife-48787-fig6-v2.jpg)

**Figure 6.:** (A) Image sequence of simulation of chromosome segregation after anaphase is triggered, rendered from a three-dimensional simulation. Anaphase begins immediately after the first image. Lower, schematic showing kinetochore position along the spindle. Time shown in minutes:seconds. (B–D) Simulation results. (B) Simulated fluorescence microscopy images with MTs (red) and a single kinetochore pair (green). Time shown in minutes:seconds. (C) Spindle pole body-kinetochore distance, and (D) interkinetochore distance versus time from the simulation shown in (B), sampled at a rate comparable to the experimental data in (E–G). (E–G) Experimental results. Maximum-intensity projected smoothed images from time-lapse confocal fluorescence microscopy of fission yeast with mCherry-atb2 labeling MTs (red) and cen2-GFP labeling the centromere of chromosome 2 (green). Time shown in minutes:seconds. (E) Spindle length, (F) spindle pole body-kinetochore distance, and (G) interkinetochore distance versus time from the experiment shown in (E).

![Video 8.](https://cdn.elifesciences.org/articles/48787/elife-48787-video8.mp4.jpg)

**Video 8.:** Top: Simulation video showing that separation of the sister chromatids occurs after 4.45 min of the simultaneous biorientation of all three chromosomes. The zoomed views show the chromosomes achieving biorientation before segregating to the spindle poles. Lower: Simulation video (left) and simulated fluorescence microscopy images (right), with red MTs and green kinetochore (scale bar 1 μm). The simulated fluorescence images are rotated so that the spindle is vertical. Anaphase occurs at 7:09.

## Discussion

The computational model of mitosis presented here can biorient chromosomes as the spindle assembles. This framework allows us to examine which functions are most important to assemble a bipolar spindle, attach kinetochores to spindle MTs, biorient chromosomes, and segregate them to the poles (Figure 1; Video 1). Our model was refined with experimental data on spindle structure, spindle elongation, and chromosome movements in fission yeast, leading to quantitative agreement with the data (Figure 2; Video 2). The reference model results match previous genetics that found that kinesin-5 motors and CLASP are essential for bipolar spindle assembly (Hagan and Yanagida, 1990; Hagan and Yanagida, 1992; Bratman and Chang, 2007; Blackwell et al., 2017a), which suggests that the model captures key features needed to provide insight into mitotic mechanism.

Three ingredients are required for long-lived biorientation in the model (Figure 3; Video 4). Kinetochores shield themselves from merotely by progressive restriction of attachment. Inclusion of this effect in the model was motivated by recent work on the monopolin complex in fission yeast (Gregan et al., 2007) and attachment-driven compaction of mammalian kinetochores (Magidson et al., 2015). Progressive restriction has two key effects: it promotes proper attachment by favoring binding of microtubules from the same pole that is already attached to the kinetochore, and simultaneously creates a torque that helps to reorient the kinetochore on the spindle. In previous work, the monopolin complex components Pcs1/Mde4 were found not to be essential in fission yeast (Gregan et al., 2007), but in our model completely removing progressive restriction abolishes biorientation (Figure 3). This suggests the possibility that in fission yeast, other molecules may contribute to progressive restriction in addition to monopolin.

Mimicking the effects of Aurora B kinase by including destabilization of misaligned attachments allows the model to achieve robust error correction. Destabilization by approximately a factor of 70 gives the highest degree of biorientation the model. This is similar to the degree of destabilization previously estimated to occur due to Aurora B (Cimini et al., 2006), further suggesting that the model produces biologically relevant results.

To maintain long-lived biorientation in the model, kinetochore-MT attachment lifetime must increase with tension during microtubule depolymerization. This catch-bond behavior has been previously measured for purified budding-yeast kinetochores attached to single microtubules (Akiyoshi et al., 2010; Miller et al., 2016). Without this force dependence, kinetochores frequently detach from depolymerizing MTs and lose biorientation. Our model achieves biorientation for the longest time with an increased force-sensitivity of attachment compared to experimental measurements, a difference that would be of interest to explore in future work.

The timing of spindle assembly and biorientation in the model were consistent with those quantified experimentally. A current difference between the model and experiment is that we find ongoing turnover of kinetochore-MT attachments, so that biorientation can be lost once established. This is in contrast to previous experimental work, which suggests that for metaphase spindles, once biorientation is established it is rarely lost (Waters et al., 1996; Nicklas, 1997; Yoo et al., 2018). The mechanisms underlying this difference are an open question.

Using our model, we studied the origins of large spindle length fluctuations (Figure 4; Video 6). While previous work has examined regulation of spindle length (Syrovatkina et al., 2013; Hepperla et al., 2014; Nannas et al., 2014; Rizk et al., 2014), what mechanisms might drive large fluctuations in spindle length over time have been less well-studied. We identified the lifetime of kinetochore-MT attachment as a determinant of the degree of spindle length fluctuations. Long attachment lifetime allows bioriented chromosomes to become more stretched, leading to large, slowly varying inward force on the spindle. Our results suggest why large spindle length fluctuations have not been seen in larger spindles in vertebrate cells: in S. pombe, a relatively small number of kinetochores and MTs contribute to spindle length, and therefore the changing force on the three chromosomes can have a significant effect on the spindle. In vertebrate spindles with tens of thousands of MTs, changes in force on a small number of kinetochores contribute only a small fractional change to overall force on the spindle, leading to smaller fluctuations.

To understand how force generation changes as the spindle assembles, we quantified the force generated by different classes of spindle molecule (Figure 5; Video 7). The early spindle has almost no force generation from interkinetochore stretch because chromosomes are rarely bioriented at this stage. Instead, the early spindle is characterized by outward force from kinesin-5 motors that is resisted by crosslinkers. Consistent with earlier work (Lansky et al., 2015), the force from crosslinkers is highest when MT antiparallel overlaps are short and drops as the spindle elongates. Once the bipolar spindle is formed and chromosomes are bioriented, attached chromosomes provide significant inward force that opposes the outward force of kinesin-5 motors. These results suggest that the many mutations that alter spindle length in fission yeast (Syrovatkina et al., 2013) might act indirectly by altering kinesin-5 force generation or interkinetochore stretch.

Remarkably, the model is able to transition to anaphase A and robustly segregate chromosomes to the poles with a small number of additional rules (Figure 6; Video 8). Overall, our work provides a powerful framework for testing spindle assembly mechanisms that can inform future experimental studies.
