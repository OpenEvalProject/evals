# A widespread family of serine/threonine protein phosphatases shares a common regulatory switch with proteasomal proteases

## Authors

- Niels Bradshaw<sup>1</sup> ([ORCID: 0000-0002-6845-4717](https://orcid.org/0000-0002-6845-4717))
- Vladimir M Levdikov<sup>2</sup>
- Christina M Zimanyi<sup>1</sup> ([ORCID: 0000-0002-6782-507X](https://orcid.org/0000-0002-6782-507X))
- Rachelle Gaudet<sup>1</sup> ([ORCID: 0000-0002-9177-054X](https://orcid.org/0000-0002-9177-054X))
- Anthony J Wilkinson<sup>2</sup> ([ORCID: 0000-0003-4577-9479](https://orcid.org/0000-0003-4577-9479))
- Richard Losick<sup>1</sup> ([ORCID: 0000-0002-5130-6582](https://orcid.org/0000-0002-5130-6582)) †

### Affiliations

1. Department of Molecular and Cellular Biology Harvard University Cambridge United States
2. Structural Biology Laboratory, Department of Chemistry University of York York United Kingdom

† Corresponding author

## Abstract

PP2C phosphatases control biological processes including stress responses, development, and cell division in all kingdoms of life. Diverse regulatory domains adapt PP2C phosphatases to specific functions, but how these domains control phosphatase activity was unknown. We present structures representing active and inactive states of the PP2C phosphatase SpoIIE from Bacillus subtilis. Based on structural analyses and genetic and biochemical experiments, we identify an α-helical switch that shifts a carbonyl oxygen into the active site to coordinate a metal cofactor. Our analysis indicates that this switch is widely conserved among PP2C family members, serving as a platform to control phosphatase activity in response to diverse inputs. Remarkably, the switch is shared with proteasomal proteases, which we identify as evolutionary and structural relatives of PP2C phosphatases. Although these proteases use an unrelated catalytic mechanism, rotation of equivalent helices controls protease activity by movement of the equivalent carbonyl oxygen into the active site.

## Introduction

Reversible protein phosphorylation is widely used in biological systems to control the activity of enzymes or the association of proteins with other proteins. Kinases and phosphatases control the phosphorylation state of target proteins in response to specific cellular or environmental cues, making reversible phosphorylation a flexible mechanism to control diverse biological systems (Huse and Kuriyan, 2002; Shi, 2009; Taylor and Kornev, 2011). Here we address the question of how members of the PP2C family of serine/threonine phosphatases are regulated to control processes such as cell growth and death, development, and responses to stress in all kingdoms of life (Kerk et al., 2015; Lammers and Lavi, 2007; Shi, 2009). Among serine/threonine phosphatases, a distinctive feature of the PP2C family is that the activity of a conserved catalytic domain is controlled by diverse regulatory domains that are often linked in cis to the catalytic domain (Shi, 2009; Zhang and Shi, 2004). We investigated the PP2C family member SpoIIE, which controls the activation of the cell-specific transcription factor σF during the developmental process of sporulation in the bacterium Bacillus subtilis.

Sporulation involves the formation of an asymmetrically-positioned septum that divides the developing cell into large and small cellular compartments (Stragier and Losick, 1996). SpoIIE is the most upstream member of a three-protein pathway that activates σF in the small cell (Figure 1A). It does so by dephosphorylating the phosphoprotein SpoIIAA-P (Duncan et al., 1995). Dephosphorylated SpoIIAA, in turn, displaces σF from the anti-sigma factor SpoIIAB to release the free and active transcription factor (Figure 1A) (Diederich et al., 1994). A long-standing mystery is how SpoIIE is regulated to generate dephosphorylated SpoIIAA selectively in the small cell. Recent work indicates that SpoIIE initially associates with the asymmetrically-positioned cytokinetic ring and then during cytokinesis is handed off to the adjacent cell pole, which will become the small cell (Bradshaw and Losick, 2015). Cell-specific activation is mediated by the self-association of SpoIIE molecules in the small cell, which protects the protein from proteolysis and activates the phosphatase (Bradshaw and Losick, 2015). Here we focus on the molecular mechanism of phosphatase activation.

![Figure 1.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig1-v2.jpg)

**Figure 1.:** A is a diagram of the three-protein pathway controlling σF. B is a schematic diagram of the SpoIIE primary structure with its N-terminal cytoplasmic degradation tag in black, the 10 transmembrane segments in dark grey, the regulatory domain in blue, and the PP2C phosphatase domain shown in light grey. Also shown are the switch helices in orange and the metal-coordinating residues within the active site in red. The black box identifies the SpoIIE457-827  fragment that was crystallized. C is a ribbon diagram of a single molecule of SpoIIE457-827 with front and side views using the same color scheme as the diagram in panel B. The inset shows the putative metal coordinating sidechains of the active site (from top to bottom: D795, D746, and D628) and the backbone carbonyl of G629. Figure 1—figure supplement 1 shows the 2Fo-Fc electron density map and a stereo representation of the SpoIIE457-827 structure. D shows the dimer observed in the crystal structure of SpoIIE457-827 (chains A and B) with the two protomers in darker and lighter shades (buried surface area 1500–2000 Å2 per monomer). The two and a half dimers in the asymmetric unit are shown in Figure 1—figure supplement 2.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** A shows the long α-helix from the regulatory domain of chain A from the SpoIIE457–827 structure. The 2Fo–Fc electron density map is shown with a 4 Å carve radius around the α-helix in grey mesh contoured to 1.0 σ, and the anomalous difference map from seleno-methionine derivatized crystals is shown in yellow mesh contoured to 4.0 σ. B shows a stereo representation of chain A from the SpoIIE457–827 structure with the 2Fo–Fc electron density map shown in grey mesh contoured to 1.5 σ with a 2.5 Å carve radius around chain A. C shows a stereo representation of chain A from the SpoIIE457–827 structure.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Each panel shows the asymmetric unit from the crystals of SpoIIE457–827 on the left with a single dimer circled in red and presented in isolation on the right. The chains are labeled as in the PDB file with the exception of Esym, which is a crystallographic symmetry mate of chain E.

Like other PP2C family phosphatases, the catalytic center of SpoIIE uses two divalent cations (manganese in the case of SpoIIE) to deprotonate a water molecule that serves as the nucleophile for dephosphorylation (Arigoni et al., 1996; Schroeter et al., 1999). This active site is embedded in the conserved fold of the PP2C domain, which is shared by all PP2C family members (Shi, 2009). The PP2C domain is paired with diverse regulatory modules (over 1500 unique domain architectures have been identified in the InterPro database) (Mitchell et al., 2015), but how these regulatory modules control phosphatase activity was not understood. Here we identify a pair of α-helices at the heart of the regulatory mechanism that rotate to position a carbonyl oxygen to bind an active site Mn2+ ion and activate SpoIIE. We present evidence that this mechanism is widely conserved among PP2C family members. Remarkably, rotation of equivalent α-helices is also used to control an unrelated catalytic mechanism in the structurally similar family of enzymes that form the catalytic core of the proteasome (Arciniega et al., 2014; Ruschak and Kay, 2012; Shi and Kay, 2014; Sousa et al., 2000). This raises the possibility that PP2C phosphatases and proteasome proteases have a common evolutionary history that is linked by a shared regulatory mechanism.

## Results

### Overview

To investigate how PP2C phosphatase activity is regulated, we sought to determine X-ray crystal structures of SpoIIE with the phosphatase in the active and inactive states. We present a structure of a fragment that includes the entire PP2C phosphatase domain and a portion of the adjacent regulatory domain. This structure shows that the regulatory domain mediates the formation of dimers between SpoIIE molecules, and evidence indicates that dimerization is needed to activate the phosphatase. We also present a structure of the phosphatase domain alone. A comparison of the structures reveals that dimerization rotates two α-helices of the PP2C fold (α1 and α2 of the conserved PP2C fold) (Das et al., 1996) relative to the phosphatase core. We refer to these helices as switch helices and present evidence that this shift in position switches the phosphatase from the inactive to active state.

### Structure of the phosphatase domain with a portion of the adjacent regulatory domain

To determine how SpoIIE is regulated, we first sought to determine the structure of the molecule in an active, self-associated state. The entire, 270-residue-long regulatory domain mediated the formation of heterogeneous multimers that were refractory to crystallization (Bradshaw and Losick, 2015). Using bioinformatic analysis, we devised a construct (SpoIIE457–827) that included the C-terminal half of the regulatory domain and the PP2C phosphatase domain (Figure 1B; information on the design of the construct is presented in the Materials and methods). This construct produced monodisperse protein that yielded crystals. Despite limited (3.9 Å) resolution of the diffraction data, the overall secondary structure elements were well-defined in electron density maps for both the regulatory and the phosphatase domains (Figure 1, Figure 1—figure supplement 1, and Table 1). The most striking feature of the regulatory domain was an N-terminal 45-residue long α-helix (residues 473–518) that makes intramolecular contacts with the switch helices (α1 and α2) of the phosphatase domain (Figure 1C).

**Table 1.**
 Data collection and refinement statistics.


<table>
  <thead>
    <tr>
      <th></th>
      <th>SpoIIE457-827 (5UCG)</th>
      <th>SpoIIE590-827 (5MQH)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data collection</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Beam source</td>
      <td>APS 24-ID-C</td>
      <td>Diamond, I02</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>0.9792</td>
      <td>0.97950</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P43212</td>
      <td>C2221</td>
    </tr>
    <tr>
      <td>Cell dimensions</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>125.62, 125.62, 330.70</td>
      <td>56.29, 122.51, 81.62</td>
    </tr>
    <tr>
      <td>α, β, γ (°)</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
    </tr>
    <tr>
      <td>Resolution (Å)*</td>
      <td>60–3.9 (3.97–3.9)</td>
      <td>61.34–2.44 (2.48–2.44)</td>
    </tr>
    <tr>
      <td>Total reflections*</td>
      <td>284918 (8031)</td>
      <td>60359 (4228)</td>
    </tr>
    <tr>
      <td>Unique reflections*</td>
      <td>24917 (1181)</td>
      <td>10961 (681)</td>
    </tr>
    <tr>
      <td>Rsym†*</td>
      <td>0.102 (1.448)</td>
      <td>0.057 (0.631)</td>
    </tr>
    <tr>
      <td>CC1/2</td>
      <td>0.999 (0.847)</td>
      <td>0.999 (0.874)</td>
    </tr>
    <tr>
      <td>CC*</td>
      <td>1.00 (0.958)</td>
      <td>-</td>
    </tr>
    <tr>
      <td>I / σI*</td>
      <td>24.7 (0.8)</td>
      <td>20.1 (2.8)</td>
    </tr>
    <tr>
      <td>Completeness (%)*</td>
      <td>99.7 (97.4)</td>
      <td>99.7 (99.8)</td>
    </tr>
    <tr>
      <td>Redundancy*</td>
      <td>11.4 (6.8)</td>
      <td>6.3 (6.2)</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resolution (Å)*</td>
      <td>50–3.9 (4.1–3.9)</td>
      <td>50–2.45 (2.51–2.45)</td>
    </tr>
    <tr>
      <td>No. reflections</td>
      <td>21558</td>
      <td>10187</td>
    </tr>
    <tr>
      <td>Rwork / Rfree‡*</td>
      <td>0.28/0.32</td>
      <td>0.21/0.28</td>
    </tr>
    <tr>
      <td>No. atoms</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>13166</td>
      <td>1783</td>
    </tr>
    <tr>
      <td>B-factors</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>93.0</td>
      <td>68.0</td>
    </tr>
    <tr>
      <td>R.m.s. deviations</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bond lengths (Å)</td>
      <td>0.002</td>
      <td>0.010</td>
    </tr>
    <tr>
      <td>Bond angles (°)</td>
      <td>0.525</td>
      <td>1.545</td>
    </tr>
    <tr>
      <td>Ramachandran plot</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Favored (%)</td>
      <td>92.48</td>
      <td>96.9</td>
    </tr>
    <tr>
      <td>Allowed (%)</td>
      <td>7.40</td>
      <td>3.1</td>
    </tr>
    <tr>
      <td>Outliers (%)</td>
      <td>0.12</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Rotamer outliers (%)</td>
      <td>6.44</td>
      <td>15.4</td>
    </tr>
  </tbody>
</table>

_*Values in parentheses are for highest-resolution shell.†Rsym = ∑hkl∑i|Ii - <I> |/∑hkl∑i <I> where Ii is the intensity of the ith measurement of a reflection with indexes hkl and <I> is the statistically weighted average reflection intensity.‡Rwork = ∑||Fo| - |Fc||/∑|Fo| where Fo and Fc are the observed and calculated structure factor amplitudes, respectively. Rfree is the R-factor calculated with 5% of the reflections chosen at random and omitted from refinement._

The five molecules of SpoIIE457-827 in the asymmetric unit were paired in similar dimers; two dimers were formed within the asymmetric unit and the fifth molecule dimerized across a crystallographic two-fold axis (Figure 1D, Figure 1—figure supplement 2). The core of the dimer interface (1500–2000 Å2 buried surface per monomer) was formed from antiparallel contacts between the long α-helices from the regulatory domains of adjacent molecules. Additionally, the switch helices at the base of each phosphatase domain contact each other across the dimer interface (Figure 1, Figure 2A and B, shown in orange).

![Figure 2.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig2-v2.jpg)

**Figure 2.:** A is a surface representation of the SpoIIE457–827 dimer with the phosphatase domain, the switch, and the regulatory domain color coded as indicated in the associated schematic. Chain A is colored with darker shades and Chain B is colored with lighter shades. B is an open-book view of the SpoIIE457–827 dimer with the interface (defined as residues within 4.5 Å of the adjacent molecule) outlined in black. Red circles mark positions of amino-acid substitutions that blocked stabilization, localization, and activation (V480K, L484K, V487K, M491K, F494K, I498K, L646K, I650K, and T663K), whereas white circles mark positions of substitutions that blocked activation (as judged by σF activity) but not stabilization and localization (E639K, E642K, and I667K). Figure 2—figure supplement 1 presents the analysis of the behavior of the SpoIIE mutants in vivo. C is a surface representation of Chain A of SpoIIE457-827 rotated approximately 180° relative to the dimeric view in A. White circles indicate positions of substitutions that led to defects in activation (but not localization) of SpoIIE in vivo (Q483A, G486K, V490K, and E497K). The box outlines the section of the long α-helix of the regulatory domain that is represented as a helical wheel in D. Figure 2—figure supplement 1 presents the analysis of the behavior of the SpoIIE mutants in vivo. D is a helical wheel representation of residues 480 to 498 from the long α-helix of the regulatory domain. Positions at which substitutions led to defects in σF activation are indicated by circles colored as in B and C. Black text (A481K, S488K, D493K, and S495K) indicates positions where substitutions did not lead to a phenotype, grey text represents positions that were not tested. Figure 2—figure supplement 1 presents the analysis of the behavior of the SpoIIE mutants in vivo.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** A shows the intracellular localization of the SpoIIE mutants described in Figure 2. Images of SpoIIE-YFP fluorescence from representative sporulating cells that had completed asymmetric division are shown for wild-type SpoIIE (top center), the mis-localized mutant SpoIIEV480K (left), and the forespore-localized mutant SpoIIEQ483A (right). Average fluorescence intensity profiles of SpoIIE-YFP are plotted for each mutant. Plots from mutants with defects in localization and activation of σF are in red (left), and plots from variants that are defective only in σF activation are in white (right). The blue bar at the right indicates substituted residues that reside in the long α-helix of the regulatory domain, whereas the orange bar marks substitutions in the PP2C phosphatase domain switch region. Each trace represents an average intensity profile normalized to the membrane dye FM4-64 from hundreds of asymmetrically divided cells aligned at the forespore pole. A reference plot from wild-type SpoIIE is in grey, and the dashed line represents the approximate position of the asymmetric septum. After σF activation, SpoIIE is recruited back to the forespore face of the asymmetric septum and then moves along with the engulfing membrane to encompass the forespore. Thus, mutants with the most severe defects in σF activation haves fluorescence profiles that are slightly shifted towards the forespore pole relative to that of wild-type cells. B-D are immunoblots showing the levels of SpoIIE-YFP, and CFP produced from a σF dependent promoter (detected using an α-GFP antibody) for the mutants in panel A. B shows immunoblots for the mutants that exhibited reduced SpoIIE levels and abnormal localization (red). C shows immunoblots for the mutants shown in panel B in which the FtsH degradation tag of SpoIIE had been removed to stabilize SpoIIE protein (the immunoblot for intact SpoIIE is shown in the left lane). D shows immunoblots for the properly localized mutants (white). The colored bars and mutant labels are color coded as in panel A.

### Amino acid substitutions in the dimer interface block function

To investigate the role of dimerization in stabilization, localization and phosphatase activation, we systematically created substitutions of residues that make up the dimer interface and investigated the ability of these mutants to function during sporulation. We substituted the native amino-acids with lysine because the positive charge and the long side chain would be expected to impair dimerization. The effect of these substitutions on stabilization and subcellular localization was investigated by use of a SpoIIE-YFP fusion and the effect on phosphatase activity was judged by use of a σF-dependent reporter (Figure 2B, red circles, Figure 2—figure supplement 1A,B and C). The results revealed that a continuous region of the dimer interface (marked with red circles in Figure 2B) composed of six residues from the long α-helix of the regulatory domain (V480, L484, V487, M491, F494, and I498) and three residues from the switch helices (L646, I650, and T663) were needed for all three aspects of SpoIIE function. These findings are consistent with the hypothesis that the dimers observed in our structure represent the active state of the phosphatase.

### Structure of the phosphatase domain

To investigate how dimerization activates phosphatase activity, we sought to compare the active dimeric structure of SpoIIE457–827 to inactive SpoIIE. Previously, we determined the structure of SpoIIE590–827, a fragment that included the PP2C phosphatase domain but lacked the adjacent regulatory domain (Levdikov et al., 2012). We hypothesized that this structure represented the inactive state because it lacked the dimeric interface of the SpoIIE457–827 structure. Although monomeric in solution under physiological conditions, SpoIIE590–827 had undergone a domain-swap dimerization during crystallization (Levdikov et al., 2012). Here, we solved an additional structure for SpoIIE590–827 (with an amino acid substitution A624I that was designed to block domain swapping) that was in a different crystal form and was not domain-swapped (Figure 3A). Importantly, the only significant differences between the two SpoIIE590–827 structures were at the site of the domain-swap (Figure 3—figure supplement 1). Also, contacts between the phosphatase domains observed in the SpoIIE457–827 dimer were not present in either of the SpoIIE590–827 structures.

![Figure 3.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig3-v2.jpg)

**Figure 3.:** A is a ribbon diagram of the structure of SpoIIE590–827, which is the phosphatase domain of SpoIIE lacking the regulatory domain. The region of the protein that was crystallized is diagramed above. The switch region and Mn2+-coordinating residues are color-coded as in Figure 1A. Figure 3—figure supplement 1 shows a comparison with the previously published domain swapped SpoIIE590–827 structure. B compares the conformations of the phosphatase domain in the dimeric SpoIIE457–827 structure (switch helices in dark orange) and the isolated phosphatase domain of SpoIIE590–827 (switch helices in light orange). The structures were aligned based on the core of the phosphatase domain excluding the switch region (residues 590–628 and 678–827) with an RMSD = 0.952 Å (970 to 970 atoms). The major conformational change upon dimerization corresponds to a rotation and upward movement of the switch helices. Figure 3—figure supplement 2 shows how gain of function mutants may promote the conformational change. C is a model for how rotation of the switch helices leads to phosphatase activation. In the inactive state (left) G629 is not positioned to coordinate the M2 metal. We propose that dimerization (right) leads to rotation of the switch helices (orange), which repositions G629 to recruit manganese and complete the active site. We note that an additional glycine of RsbX (G47), corresponding to G631 of SpoIIE, also coordinates M2. Thus, it is possible that G631 also coordinates M2 in place of the lower right-hand water molecule depicted in the schematic diagram (Teh et al., 2015). Figure 3—figure supplement 3 shows details of the active site in the SpoIIE457–827 structure.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** A shows the domain swapped structure of SpoIIE590–827 (PDB ID 3T91). The PP2C domain of Chain B is grey and the switch helices are colored orange and Chain A is colored blue. B shows an overlay of the unswapped SpoIIE590–827 structure (light shades), and the domain swapped SpoIIE 590–827 (colored as in panel A). The overlay was done using residues 678–800 (RMSD 0.72 Å).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** A shows the side-chains that surround V697 (green) in the inactive (SpoIIE590–827 left, switch helices in light orange) and active (SpoIIE457–827 right, switch helices in orange) conformations. Residues depicted as sticks are L647, I661, I664, N665, L668, I676, L680, L695, L718, F726, and V728. B is a head-on ribbon representation of SpoIIE457–827 as in Figure 1 with spheres indicating the position of residues substituted in gain-of-function mutants that were isolated as suppressors of the spoIIE48 mutation. The residues are in three clusters: those that contact the switch helices from the PP2C phosphatase domain (I684, L695, V697, and V728), those on the switch helices that make contacts across the dimer interface (K649 and I650), and those that point up towards the switch helix from the long α-helix of the regulatory domain (L479).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** A shows an anomalous difference map calculated from an X-ray dataset collected from manganese-soaked crystals overlaid on the ribbon diagram of SpoIIE457–827 as in Figure 1. The side view of the SpoIIE457–827 structure is shown for chain A, and the inset panels show the active site regions with the putative metal-coordinating side-chains for each of the five chains in the asymmetric unit. The purple spheres represent the manganese ions from superimposed RsbX (PDB ID 3W43, see panel C below), displayed here for reference. The maps are shown with a 4 Å carve radius around the indicated chain and are contoured at 4.0 σ for chains A and B and 3.5 σ for chains C, D, and E. B shows the 2Fo–Fc electron density map from the X-ray data in grey mesh contoured to 1.0 σ with a 2.5 Å carve radius around the active site loop residues 628–635 of SpoIIE457–827. Residues 628–635 are shown as sticks. C shows an overlay of SpoIIE457–827 and RsbX (PDB ID 3W43) aligned based on residues 590–628. SpoIIE457–827 is shown as a darker shade, and RsbX is shown as a lighter shade, and the putative metal-coordinating side-chains of the active sites are shown as sticks. The purple spheres represent the manganese ions from the RsbX structure.

Comparison of the SpoIIE590–827 structures with SpoIIE457–827 revealed that dimerization rotated the switch helices (α1 and α2 of the PP2C fold, corresponding to SpoIIE residues 630–678) approximately 45° as a rigid body relative to the phosphatase core (Figure 3B, Video 1). We hypothesized that this conformational change of the switch helices is responsible for activation of the SpoIIE phosphatase.

![Video 1.](https://cdn.elifesciences.org/articles/26111/elife-26111-media1.mp4.jpg)

**Video 1.:** Shown is the PP2C phosphatase domain of SpoIIE (switch helices in orange) morphing from the structure of SpoIIE590–827 to the structure of SpoIIE457–827. The structures were aligned based on the core of the phosphatase domain excluding the switch region (residues 590–628 and 678–827) as in Figure 3B.

### Repositioning the switch region is necessary for phosphatase activation

To evaluate whether repositioning of the switch region is responsible for phosphatase activation, we returned to our genetic analysis of the contacts made in the SpoIIE457–827 structure. In the dimer, the switch helices are held in position by intramolecular contacts with the long α-helix of the regulatory domain and intermolecular contacts between switch helices across the dimer interface (Figures 1D, 2B and C). We found that single-amino acid substitutions at either of these contact sites blocked phosphatase activity but not stabilization or localization to the small cell. Phosphatase activity was assessed by σF-directed gene expression and stabilization and localization by use of a SpoIIE-YFP fusion (white circles in Figure 2C and D and Figure 2—figure supplement 1A and D). This result defines two roles for the long α-helix: one face of the helix mediates dimerization and is required for all three aspects of SpoIIE function (stabilization, localization and phosphatase activity) (Figure 2B and D red circles), and the other face, which makes intramolecular contacts with the switch region, is specifically required for phosphatase activity (Figure 2B–D white circles). Additionally, these results are consistent with the idea that dimerization stimulates phosphatase activity by repositioning the switch helices.

### Evidence from gain-of-function mutants that repositioning the switch helices is sufficient for phosphatase activation

Replacement of valine at position 697 with alanine causes a gain-of-function mutant phenotype in which σF is activated constitutively (Carniol et al., 2004; Hilbert and Piggot, 2003). The V697A substitution also enhanced phosphatase activity as measured in vitro (Bradshaw and Losick, 2015). But how this substitution acts had been unclear. Our structure of SpoIIE590–827 reveals that in the monomeric state, V697 packs in a hydrophobic pocket between the β strands at the base of the PP2C domain and the switch (Figure 3—figure supplement 2A). In contrast, N665 from the switch packs near V697 in the structure of SpoIIE457–827 in the dimeric state. We therefore hypothesize that in the wild type, V697 stabilizes the conformation of the switch helices in the inactive monomeric state and that truncating V697 to alanine stabilizes the active conformation by promoting solvation of the polar residue N665 (Figure 3—figure supplement 2A). Thus, and according to our hypothesis, replacing V697 with alanine destabilizes the inactive state by removing hydrophobic contacts and favors the active conformation by eliminating a repulsive interaction. Reinforcing this hypothesis, substitution of V697 with a bulky hydrophobic residue (phenylalanine), which could similarly destabilize the inactive conformation, also causes constitutive activity (Bradshaw and Losick, 2015).

Other gain-of-function mutants that stimulate phosphatase activity in the context of a loss-of-function mutant support this hypothesis (Carniol et al., 2004). The amino acid substitutions in these mutants (L479F, K649T, I650L, I684V, L695W, and V728M) were all located at positions in the structure that could contribute to positioning the switch helices (Figure 3—figure supplement 2B). I684 and L695 project down from the β-strands at the base of the phosphatase domain to contact the switch. K649 and I650 are themselves part of the switch helices and project across the dimer interface. V728 projects towards the switch from the loop implicated in substrate binding in other PP2C phosphatases. Finally, L479 projects up towards the switch from the long α-helix of the regulatory domain. We conclude that, like V697A, these amino-acid substitutions bias the phosphatase domain to the active conformation of the switch region.

### The switch helices move a conserved manganese-coordinating residue into the active site

How does repositioning the switch region activate phosphatase activity? All PP2C phosphatases coordinate 2–3 divalent metals (usually manganese) in their active sites (Das et al., 1996; Shi, 2009). The two core metal ions, known as M1 and M2, directly participate in catalysis by deprotonating a water molecule that serves as the nucleophile for hydrolysis (Das et al., 1996). Based on the universally conserved architecture of the catalytic center, the M2 metal of SpoIIE is predicted to be coordinated by the side-chain of D628 and the carbonyl oxygen of G629 (Schroeter et al., 1999) (Figure 1C and Figure 3C). G629 is at the junction between the switch helices and the β strands at the base of the phosphatase domain, such that movement of the switch helices could be coupled with bringing G629 into position to recruit M2.

In support of this idea, G629 is not in position to coordinate M2 in our isolated phosphatase domain structures, which we thus conclude represent an inactive state. This is supported by the fact that although our previously published structures included manganese in the crystallization conditions, the M2 site was unoccupied and the active site contained only a single manganese (Levdikov et al., 2012). While soaking SpoIIE457–827 crystals with manganese degraded the diffraction, an anomalous difference map provided evidence that manganese was bound in the active site (Figure 3—figure supplement 3A and Table 2). Due to the low (5.4 Å) resolution of the data for the manganese-soaked crystals, the number of bound metal ions and their position in the active site could not be established. In the dimeric SpoIIE457–827 structure and in contrast to the SpoIIE590–827 structure, the loop connecting the switch helices to G629 was ordered (Figure 3—figure supplement 3B) and overlaid well with M2-containing structures of closely related phosphatases such as B. subtilis RsbX (Teh et al., 2015), M. tuberculosis Rv1364c (King-Scott et al., 2011), and S. thermophilus Sthe_0969 (Nocek et al., 2010) (Figure 3—figure supplement 3C). We propose that the shift of the switch helices activates the phosphatase by repositioning G629 to recruit M2 and complete the active site (Figure 3C).

**Table 2.**
 Data collection statistics for anomalous datasets.


<table>
  <thead>
    <tr>
      <th></th>
      <th>SpoIIE457-827 Mn</th>
      <th>SpoIIE457-827 SeMet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data collection</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Beam source</td>
      <td>APS 24-ID-C</td>
      <td>APS 24-ID-E</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P43212</td>
      <td>P43212</td>
    </tr>
    <tr>
      <td>Cell dimensions</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>124.783, 124.783, 329.787</td>
      <td>123.081, 123.081, 329.556</td>
    </tr>
    <tr>
      <td>α, β, γ (°)</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
    </tr>
    <tr>
      <td></td>
      <td>Inflection</td>
      <td>Inflection</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>1.89350</td>
      <td>0.97920</td>
    </tr>
    <tr>
      <td>Resolution (Å)*</td>
      <td>50–5.4 (5.49 — 5.4)</td>
      <td>50–5.7 (5.8–5.7)</td>
    </tr>
    <tr>
      <td>Total reflections*</td>
      <td>40325 (318)</td>
      <td>51233 (4024)</td>
    </tr>
    <tr>
      <td>Unique reflections*</td>
      <td>8598 (187)</td>
      <td>8071 (706)</td>
    </tr>
    <tr>
      <td>Rsym*</td>
      <td>0.145 (0.535)</td>
      <td>0.175 (1.475)</td>
    </tr>
    <tr>
      <td>CC1/2*</td>
      <td>0.99 (0.75)</td>
      <td>0.996 (0.459)</td>
    </tr>
    <tr>
      <td>CC* *</td>
      <td>0.997 (0.926)</td>
      <td>0.999 (0.793)</td>
    </tr>
    <tr>
      <td>Mean I / σI*</td>
      <td>9.14 (1.00)</td>
      <td>7.86 (1.13)</td>
    </tr>
    <tr>
      <td>Completeness (%)*</td>
      <td>90.1 (41.6)</td>
      <td>99.0 (97.4)</td>
    </tr>
    <tr>
      <td>Redundancy*</td>
      <td>4.7 (1.7)</td>
      <td>6.3 (5.7)</td>
    </tr>
  </tbody>
</table>

_*Values in parentheses are for highest-resolution shell._

### Mn2+ stimulates dimerization and phosphatase activity

A prediction of the hypothesis that movement of the helices allows recruitment of M2 is that binding of metal to the active site of SpoIIE should be coupled to dimerization and activation. Whereas in cells, cues in the forespore promote self-association of SpoIIE to induce phosphatase activity (Bradshaw and Losick, 2015), we reasoned that in vitro, in the absence of cellular cues, addition of high concentrations of manganese should drive dimerization and activation by mass action (Figure 4A). We used size exclusion chromatography coupled to multi angle laser light scattering (SEC-MALLS) to monitor SpoIIE dimerization over a range of manganese concentrations. In the absence of manganese, SpoIIE457–827 eluted as a single monodisperse peak with a calculated molecular weight of 42 kDa, consistent with the calculated molecular weight of a monomer (Figure 4B). Addition of 250 µM and 1 mM MnCl2 induced dimerization of SpoIIE457–827, shifting and broadening the peak in concert with an increase in molecular mass (Figure 4B). In support of the idea that this dimerization uses the interface found in the SpoIIE457–827 structure, substitution of a residue from the interface (L484) with lysine blocked dimerization even after addition of 1 mM MnCl2 (Figure 2, Figure 4—figure supplement 1). Additionally, substitution of the M2 coordinating residue D628 with alanine partially impaired dimerization in the presence of 1 mM MnCl2, suggesting that manganese binding in the active site promoted dimerization (Figure 4—figure supplement 1).

![Figure 4.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig4-v2.jpg)

**Figure 4.:** A is a model for phosphatase activation. During sporulation, cellular cues induce dimerization of SpoIIE molecules, rotating the switch helices and leading to Mn2+ binding in the active site. A prediction of this model is that high concentrations of Mn2+ would drive SpoIIE to become activated and form dimers. B shows SEC-MALLS (size exclusion chromatography coupled to multi angle laser light scattering) results for the SpoIIE457-827 fragment to assess complex formation at various concentrations of Mn2+. The top plot shows molecular weights calculated from light scattering and the bottom plot shows the corresponding UV absorbance traces for both wild-type SpoIIE (left-hand side) and the gain-of-function mutant SpoIIEV697A (right). The experiments were performed in the absence of Mn2+ (grey), with 0.25 mM MnCl2 (light purple), and at 1 mM MnCl2 (purple). All experiments were performed in triplicate and data from representative runs are shown. Figure 4—figure supplement 1 shows size exclusion chromatography analysis of additional SpoIIE mutants. The source data are included as Figure 4—source data 1. C is a plot of phosphatase activity (initial rates, vobs) for the wild-type (black) and V697A mutant (purple) SpoIIE457–827 fragments as a function of MnCl2 concentration using SpoIIAA-P as the substrate. The data were fit with the equation vobs=Vmax*[MnCl2]h/(K+[MnCl2]h) where h is the Hill coefficient calculated from the inset panel [Vmax = 4.15 ± 0.04 min–1 (2.28 ± 0.04 min–1 for SpoIIEV697A) and K = 0.32 ± 0.02 mM (0.020 ± 0.002 mM for SpoIIEV697A)]. The K1/2 values reported in the text were calculated from this equation and represent the concentration of MnCl2 at which SpoIIE has half maximal activity. Inset is a Hill plot for data points representing 10–90% activity. Lines are linear fits to the data using the equation log(vobs/(Vmax–vobs))=h*log[MnCl2]–logK [h = 2.0 ± 0.1 (1.92 ± 0.1 for SpoIIEV697A) and K = 0.31 ± 0.04 mM (0.022 ± 0.008 mM for SpoIIEV697A)]. The reported error is the error of the fit to the data. Experiments were repeated at least three times and data from a representative experiment are shown. The source data are included as Figure 4—source data 1.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Shown is size exclusion chromatography analysis in the absence of manganese (grey) or in the presence of 1 mM MnCl2 (purple) for 200 µM wild type (Panel A), SpoIIED628A (Panel B), and SpoIIEL484K (Panel C). The fact that some dimerization still occurs for the D628A variant was not unexpected because the other metal-coordinating residues are still present (including G629) and high concentrations of protein and MnCl2 were used in the experiment.

To test whether manganese-induced dimerization correlated with phosphatase activation, we measured the dependence of phosphatase activity on manganese concentration using an assay for dephosphorylation of SpoIIAA-P, the native substrate of SpoIIE. By varying the manganese concentration in the presence of saturating substrate, we determined that SpoIIE was cooperatively activated (h = 2.0) with a K1/2 for manganese of 0.56 mM (Figure 4C). This correlates well with the manganese dependence of dimerization (Figure 4B left panel). Additionally, cooperative activation with a Hill coefficient of two indicates that at least two manganese ions bind in the active site of SpoIIE, consistent with the proposed catalytic mechanism (Figure 3C).

Our hypothesis also predicts that the V697A substitution would reduce the manganese concentration required for dimerization and phosphatase activity by favoring the active conformation of the switch. Indeed, the K1/2 for manganese was reduced from 0.56 mM to 0.13 mM for SpoIIEV697A (Figure 4C), and SEC-MALLS revealed that the V697A substitution similarly reduced the concentrations of manganese required to promote dimer formation (Figure 4B right panel). Together these experiments provide biochemical evidence that SpoIIE dimerization is coupled to phosphatase activity by rotation of the switch region and coordination of manganese in the active site.

## Discussion

We have presented the structures of the active and inactive state of the PP2C phosphatase SpoIIE from B. subtilis. Based on these structures, analysis of the function of SpoIIE mutants in vivo, and biochemical experiments, we propose that the movement of two helices at the base of the phosphatase domain, forming the switch region, activates the phosphatase by positioning the carbonyl oxygen of a conserved glycine to coordinate manganese in the active site. Importantly, and as we will explain, structural and functional data additionally suggest that the switch mechanism is broadly conserved among PP2C phosphatases. Unexpectedly, and underscoring the flexibility and conservation of the switch, our analysis also reveals that a similar module controls the activity of proteases that form the catalytic core of the proteasome. This raises the possibility that the switch helices are a shared, and possibly evolutionarily conserved, feature of at least two families of enzymes that use unrelated catalytic mechanisms.

### The SpoIIE regulatory switch is broadly conserved among PP2C phosphatases

The following illustrative examples highlight the conservation and adaptability of the allosteric regulatory mechanism among PP2C phosphatases (Figure 5):

![Figure 5.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig5-v2.jpg)

**Figure 5.:** The structure of the active SpoIIE457–827 phosphatase domain is shown in the center. The SpoIIE dimerization interface that mediates activation is indicated with an orange arc. Similarly, additional arcs indicate regions where regulatory inputs impinge on the PP2C phosphatase domain for RsbP (brown, Figure 5—figure supplement 1), Pdp1 (phosphorylation is shown in red, and lipoyl binding is shown in teal, Figure 5—figure supplement 2), Fem-2 (blue, Figure 5—figure supplement 3), Hab1 (grey, Figure 5—figure supplement 4), and RssB (green, Figure 5—figure supplement 5). The diagram is based on structures illustrated in Figure 5—figure supplements 1–5.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** A shows the regulatory cascade in which the PP2C phosphatase RsbP activates the transcription factor σB. In response to energy stress RsbP is activated as a phosphatase and dephosphorylates RsbV-P, which binds to the anti-sigma factor RsbW and displaces σB, which then is competent to activate transcription. B shows the position of bypass suppressor substitutions that activate RsbP in the absence of RsbQ, the stress-responsive activator of RsbP. The positions of these substitutions are mapped onto the structure of RssB (PDB ID 3F7A) by homology (no structure of RsbP is available) and are indicated with spheres in green. Residues shown are RsbP 173, 181, 211, 230, 233, 241, 242, 244, and 246 (corresponding to RssB residues 159, 166, 199, 215, 218, 228, 229, 231, and 233). The α-helix corresponding to the predicted α0 helix of the RsbP regulatory domain is blue, and the switch helices are orange.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** A diagrams how the PP2C phosphatase pyruvate dehydrogenase phosphatase (Pdp1) promotes flux through the TCA cycle by activating pyruvate dehydrogenase. B is a ribbon diagram of Pdp1 (PDB ID 2PNQ). The PP2C phosphatase domain is in grey with tyrosine-94, which is phosphorylated to inhibit the activity of Pdp1, in red sticks, and the switch helices in orange. The metal-coordinating residues of the active site are shown in stick representation. A Pdp1-specific insertion, colored in blue, contains the predicted activating binding site for lipoyl groups from the E2 subunit of pyruvate dehydrogenase, as indicated.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** A diagrams how the PP2C phosphatase Fem-2, together with FEM-1 and FEM-3, promotes sex determination in C. elegans. B is a ribbon diagram of FEM-2 (PDB ID 4JND). The PP2C phosphatase domain is grey, the switch helices are orange, and the N-terminal domain that binds FEM-1 and FEM-3 is blue. The metal-coordinating sidechains of the active site are shown as sticks, and the magnesium ions are shown as green spheres.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** A diagrams how the PP2C phosphatase Hab1 promotes drought tolerance in plants. B shows a ribbon diagram of Hab1 (PDB ID 3UJG). The PP2C phosphatase domain is grey, the switch helices are orange, and the ‘flap’ region is blue. The metal-coordinating sidechains of the active site are shown, and the magnesium ions are shown as spheres. C shows a surface representation of Hab1 as in panel B. The contact surface with the kinase SnRK2 (defined as residues within 4 Å) is indicated with a black outline and the ‘lock’ residue W385, which is critical for binding of Hab1 to both its substrate and to the PYR/PYL/RCAR family of abscisic acid binding receptors that inhibit Hab1 activity, is indicated with a red circle. D is an overlay of the structures of dimeric SpoIIE457–827 (switch helices colored dark orange) and monomeric SpoIIE590–827 (switch helices colored light orange) as in Figure 3. The ‘flap’ region of SpoIIE is blue (SpoIIE457–827) or light blue (SpoIIE590–827).

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig5-figsupp5-v2.jpg)

**Figure 5—figure supplement 5.:** A diagrams how the pseudo-PP2C phosphatase RssB destabilizes σS by acting as an adapter protein for ClpXP proteolysis. B is a ribbon diagram of RssB (PDB ID 3F7A). The PP2C phosphatase domain is grey, the switch helices are orange, and the regulatory region is blue. The positions of bypass suppressor amino acid substitutions (residues 149, 156, 160, 164, 220, 222, 224, 227, 228, 260, 261, and 263 from P. aeruginosa corresponding to residues 146, 150, 154, 158, 214, 216, 218, 221, 222, 254, 255, and 257 from E. coli) that render RssB active in the absence of stress are indicated with spheres. C shows a comparison of the RssB dimer (above) and the SpoIIE457-827 dimer (below). The structures are colored as in panel A.

#### RsbP

The phosphatase RsbP from B. subtilis is activated in response to energy stress by binding to its partner (RsbQ) to activate the transcription factor σB (Vijay et al., 2000) (Figure 5—figure supplement 1A). Gain-of-function mutants of RsbP that constitutively activate σB in the absence of RsbQ identified two elements in RsbP that control PP2C phosphatase activity (Brody et al., 2009). One element corresponds to one of the two switch helices we identified for SpoIIE (α1). The other element (designated as α0 by Brody et al.) was from the RsbP regulatory domain, and comparison with the structure of a closely related phosphatase (Levchenko et al., 2009) (RssB; the structure of RsbP itself has not been solved) suggests that this helix contacts the switch (Figure 5—figure supplement 1B). This suggests that RsbP and related phosphatases use the α0 helix as a regulatory module to position the switch to control phosphatase activity. This supports the broad conservation of the switch mechanism and suggests that the switch is controlled by docking varied input domains with the switch helices.

#### Pdp1

Pyruvate dehydrogenase phosphatase (Pdp1) dephosphorylates pyruvate dehydrogenase to promote respiratory metabolism (Vassylyev and Symersky, 2007) (Figure 5—figure supplement 2A). Human Pdp1 activity is inhibited by phosphorylation at a site distant from the active site (Y94), and phosphorylation at Y94 is commonly observed in human cancer cells and contributes to the Warburg effect (Shan et al., 2014). In the Pdp1 structure Y94 contacts a structural motif unique to Pdp1 (Vassylyev and Symersky, 2007) that packs against a pair of α-helices structurally homologous to the SpoIIE switch helices (Figure 5—figure supplement 2B). We hypothesize that phosphorylation of Y94 would displace this structural element, shifting the position of the switch helices and inhibiting Pdp1 activity through a mechanism similar to that for SpoIIE regulation. Additionally, Pdp1 is activated by binding to the lipoyl moiety on the E2 subunit of the pyruvate dehydrogenase complex, and the proposed lipoic acid binding site is contained in the same structural element that is contacted by Y94 and packs against the switch helices (Vassylyev and Symersky, 2007) (Figure 5—figure supplement 2B). Thus, our model for PP2C regulation may explain how Pdp1 integrates both positive and negative regulatory signals to control phosphatase activity.

#### Fem-2

The C. elegans Fem-2 phosphatase regulates sex determination in complex with its regulatory partners Fem-1 and Fem-3 (Chin-Sang and Spence, 1996) (Figure 5—figure supplement 3A). Additionally, the mammalian homologue of Fem-2 promotes caspase-dependent apoptosis by antagonizing Ca2+/calmodulin-dependent protein kinase (Tan et al., 2001). Fem-2 has a specific N-terminal regulatory domain that is the scaffold for binding Fem-1 and Fem-3 to form the active complex (Zhang et al., 2013). In the Fem-2 structure this regulatory domain packs against the equivalent of the switch helices (Zhang et al., 2013) (Figure 5—figure supplement 3B). How Fem-2 phosphatase activity is regulated is not clear, but the direct contact between the Fem-2 regulatory domain and the switch helices is consistent with our proposed model for regulation of phosphatase activity through the switch helices.

#### Hab1

The PP2C phosphatase Hab1 is a member of a sub-family of related phosphatases that regulate drought tolerance in response to abscisic acid in plants (Ma et al., 2009; Park et al., 2009) (Figure 5—figure supplement 4A). It is the only PP2C phosphatase for which a structure bound to its protein substrate (the kinase SnRK2) is available (Soon et al., 2012). Hab1 contacts SnRK2 primarily through a sub-domain (termed the ‘flap’ [Pullen et al., 2004]) that is variable in PP2C phosphatases and that packs against the switch helices (blue in Figure 5—figure supplement 4B and C) (Soon et al., 2012). In the presence of abscisic acid, the PYR/PYL/RCAR family of abscisic-acid-binding proteins inhibit Hab1 by binding to a site that overlaps with the binding site for SnRK2, suggesting that the switch could be influenced both by substrate and regulator binding. This could be a more general feature of PP2C phosphatases; the corresponding substrate-binding domain in SpoIIE changed conformation upon SpoIIE dimerization and activation (Figure 5—figure supplement 4D), suggesting that the conformational change of the switch could couple regulatory inputs to substrate binding. Additionally, coupling between substrate binding and the active conformation of the switch helices would provide a conserved mechanism to achieve the known high substrate specificity of PP2C phosphatases.

#### RssB

RssB activates the general stress response in E. coli, P. aeruginosa, and certain other gamma proteobacteria (Battesti et al., 2011). Although RssB is closely related to PP2C phosphatases, its primary role is not as a phosphatase (and does not require phosphatase activity), but rather as an adapter protein, delivering the transcription factor σS for degradation by ClpXP in the absence of stress (Figure 5—figure supplement 5A). Structural and genetic studies revealed that adapter activity is regulated by contacts between the RssB regulatory domain and the switch helices that are mediated by dimerization, similar to our observations for SpoIIE (Battesti et al., 2013; Levchenko et al., 2009) (Figure 5—figure supplement 5B and C). Because the primary function of an adapter protein is to mediate protein-protein interactions, we hypothesize that for RssB the switch couples regulatory inputs to substrate binding (rather than to phosphatase activity) through a mechanism such as proposed above for Hab1. Thus, the switch mechanism may not only provide a flexible platform for adapting phosphatase activity to various inputs but also to control different outputs. We note that there are other pseudo-PP2C phosphatases including Tab1, which mediates caspase dependent apoptosis (Lu et al., 2007) and which may have similarly repurposed the switch mechanism.

Based on these examples, we conclude that the SpoIIE regulatory switch is broadly used to control diverse PP2C phosphatases via regulatory domains that dock on the switch to couple phosphatase activity to regulatory inputs (Figure 5).

### The PP2C switch is shared with the proteasome proteases

One of the most striking discoveries of our investigation is that the PP2C regulatory switch strongly resembles the allosteric switch that regulates the family of proteases that form the catalytic core of the proteasome (Arciniega et al., 2014; Ruschak and Kay, 2012; Shi and Kay, 2014; Sousa et al., 2000). These proteases are the most structurally similar family to PP2C phosphatases as revealed using the DALI server (Holm and Rosenström, 2010) and the ECOD database (Cheng et al., 2014), and like PP2C phosphatases their catalytic activity is subject to allosteric regulation. Specifically, the proteasome proteases and PP2C phosphatases have a conserved core fold (Figure 6A and B), which includes the switch helices, and the active sites are positioned in the same overall part of the structure. Although the proteases use different functional groups to mediate catalysis, the carbonyl oxygen of a conserved glycine (G629 of SpoIIE) at the junction of the core domain and the switch helices is used by both enzyme families for catalytic activity (Sousa et al., 2000).

![Figure 6.](https://cdn.elifesciences.org/articles/26111/elife-26111-fig6-v2.jpg)

**Figure 6.:** A is a secondary structure topology diagram for SpoIIE (left) and for HslV (the E. coli homolog of the proteasome protease; right). β strands are shown as arrows pointing from N to C terminus and α-helices as circles in cross section. Conserved features are dark grey, whereas variable features are light grey. The conserved glycine that moves to activate each protein is indicated with a red circle. The switch helices of SpoIIE and the corresponding α-helices of HslV are colored orange. B shows ribbon diagrams of SpoIIE and HslV (PDB ID 1G3I) colored as in A. The position of the conserved regulatory glycine (G649 in SpoIIE, and G69 in HslV) is shown with a red sphere and the insertions specific to each protein are indicated by brackets. C is a schematic of how the regulatory particle (blue) activates the proteasome proteases (grey). D shows an overlay of the active (PDB ID 1G3I) and inactive (PDB ID 1G3K) states of HslV following superimposition of the regions in grey. The switch helices are color-coded orange and light orange for the active and inactive states, respectively. The active site residues T1, K33, and the carbonyl oxygen of G69 are shown.

Association with the regulatory cap activates the proteases, ensuring that the proteolytic active sites are sequestered prior to activation (Seol et al., 1997) (Figure 6C). Early studies on HslV, the E. coli homologue of the proteasome proteases, revealed that allosteric activation by the HslU cap takes place by rotation of the switch helices to position the active site glycine (Figure 6D) (Sousa et al., 2000). This mechanism is remarkably similar to the regulatory mechanism we proposed for PP2C phosphatases; docking of a regulatory module repositions the structurally homologous region in the same way to position the same functional group to achieve catalytic activity (Video 2).

![Video 2.](https://cdn.elifesciences.org/articles/26111/elife-26111-media2.mp4.jpg)

**Video 2.:** Shown are side-by-side displays of SpoIIE and HslV morphing from the inactive to active states. Shown on the left is the PP2C phosphatase domain of SpoIIE morphing from SpoIIE590–827 (inactive, PDB ID 5MQH) to SpoIIE457–827 (active, PDB ID 5UCG) as in Figure 3B. Shown on the right is HslV morphing from the HslU free structure (inactive, PDB ID 1G3K) to the HslU bound structure (active, PDB ID 1G3I) as in Figure 6D. The switch helices are colored orange and the active site residues of each protein are shown.

This mechanism is also conserved for the archaeal proteasome, which like the eukaryotic proteasome includes an additional layer of related, but catalytically inactive α subunits; docking of the cap displaces the switch helices of the α subunits, which directly contact and reposition the switch helices of the catalytic β subunits (Ruschak and Kay, 2012). Several lines of evidence suggest that this mechanism is conserved for the eukaryotic proteasome (Arciniega et al., 2014) and is additionally used by chaperones that promote proteasome maturation (Wani et al., 2015). Finally, comparative studies of the constitutive proteasome and the immune proteasome suggested that differences in the conformational flexibility of the switch underlies their differences in activity (Arciniega et al., 2014).

Thus, our identification of the PP2C switch demonstrates that PP2C phosphatases and the proteasome use the same allosteric regulatory module, revealing an unexpected link between two fundamental signaling systems – reversible phosphorylation and regulated proteolysis. Independent analysis of structural and sequence similarity suggest that this is a result of common evolutionary ancestry. Structural comparison by the ECOD database, which classifies the evolutionary relationships of protein folds places PP2C phosphatases and the proteasome proteases in the same ‘X-group’, which is consistent with homology (Cheng et al., 2014). Independently, sequence-based searches using HHPRED (Söding et al., 2005) detected weak sequence similarity between phosphatases and the broad family of NTN-hydrolases that includes the proteasome proteases. For example, using the SpoIIE phosphatase domain sequence to search hidden Markov model alignments for B. subtilis proteins identified weak sequence similarity to D-fructose-6-phosphate amidotransferase, an NTN hydrolase. Notably, the region of possible sequence similarity maps to the switch helices and the β strands that follow and pack with the switch (although it is not known whether the switch helices play a regulatory role in amidotransferases).

### Allostery as a potential driver of evolutionary innovation

What evolutionary path might connect proteasomal proteases and PP2C phosphatases? Acquisition of a new catalytic mechanism requires that the ancestral protein retain function while acquiring the changes necessary for the new catalytic mechanism. However, conversion between the catalytic mechanisms of the proteasomal proteases and PP2C phosphatases would require multiple changes that would individually inactivate both activities (including circular permutation of the enzyme, loss/gain of metal binding, and charge swaps of residues at essential positions for catalysis). The conservation of the allosteric regulatory switch suggests a possible solution to this dilemma: namely, that the intermediate was a noncatalytic pseudoenzyme that retained the allosteric regulatory switch. RssB is an example of this sort of hypothetical pseudoenzyme; RssB uses the PP2C switch to regulate protease adapter function without functioning as a phosphatase (Battesti et al., 2013). An RssB-like intermediate would provide evolutionary pressure to preserve the regulatory mechanism, while creating a condition of neutrality to other mutations that would allow the new chemistry to evolve. Indeed, E. coli RssB lacks the C-terminal β strand of PP2C phosphatases that is substituted by the N-terminus of the proteases (Figure 6A), suggesting a pathway for how a gene fusion event could produce the topological change required to evolve protease activity.

Allosteric regulatory modules have facilitated the evolutionary diversification of enzyme families to respond to new regulatory inputs, and the regulatory mechanism we have described for PP2C phosphatases may have similarly facilitated phosphatase diversification. A recent investigation of the evolution of ligand specificity in PDZ domains proposed that allostery produces conformational flexibility and thus may arise as a consequence of evolutionary history (Raman et al., 2016). Here we propose a mechanism whereby pre-existing allosteric regulatory modules such as we have identified for PP2C phosphatases facilitated the evolution of new enzymatic activities by transition through a pseudoenzyme intermediate that is pre-programmed for regulation. Pseudoenzymes are abundant (for example, 10% of kinase family members are pseudoenzymes) (Leslie, 2013) and thus may be important for their evolutionary potential in addition to their current biological functions.

## Materials and methods

### Construct design

The SpoIIE457–827 construct was designed based on a putative sub-domain immediately N-terminal to the conserved PP2C phosphatase domain that we identified using HHPRED RRID:SCR_010276 (Söding et al., 2005). This region exhibited weak similarity to several proteins including another sporulation protein SpoIIIAH. Analysis of the regulatory domain (the newly determined portion of the structure) using the DALI server RRID:SCR_013433 (Holm and Rosenström, 2010) identified similarity to GpsL, a component of the type II secretion system, and structural alignment of the regulatory domain with SpoIIIAH matched the alignment predicted by HHPRED (Söding et al., 2005).

### Protein expression and purification

The SpoIIE457–827 coding sequence was inserted into pET47b vector that had been digested with XmaI and XhoI using isothermal assembly. SpoIIE amino acid residue substitutions were introduced to this construct by Quikchange site directed mutagenesis. These constructs were introduced to E. coli BL21 (DE3) cells for protein expression. Cells were grown at room temperature to an OD600 of 0.4, then were shifted to 14°C and expression was induced for 14–18 hr with 1 mM IPTG. Cells were harvested and pellets were resuspended in 5 ml/L of cell culture of 50 mM K•HEPES pH 8, 200 mM NaCl, 20 mM Imidazole, 10% Glycerol, 0.5 mM DTT, and 1 mM PMSF. Cells were lysed using a cell disruptor in one-shot mode (Constant Systems, Daventry, United Kingdom) and lysates were clarified by spinning for 30 min at 16,000 RPM in a Sorvall SS-34 rotor at 4°C. Lysates were loaded to a HisTrap-HP column on an AKTA FPLC and eluted with a gradient of imidazole to 200 mM. The 6His tag was cleaved overnight with PreScission protease during dialysis to 50 mM K•HEPES pH 8, 200 mM NaCl, 20 mM Imidazole, 10% Glycerol, 0.5 mM DTT at 4°C. The PreScission protease was removed by flowing the dialyzed protein over a Ni-NTA resin, and the flowthrough was loaded to a Resource Q column that had been pre-equilibrated in 50 mM K•HEPES pH 8, 100 mM NaCl, 2 mM EDTA, 2 mM DTT. Protein was eluted using a gradient to 500 mM NaCl. Fractions containing SpoIIE were concentrated on Amicon Ultra centrifugal filters and loaded to a Superdex 200 column equilibrated with 20 mM K•HEPES pH 8, 50 mM NaCl, 2 mM DTT. Fractions containing SpoIIE were concentrated and immediately used to set up crystallization trials or were flash frozen in liquid nitrogen after addition of 10% glycerol.

Seleno-Methionine derivatized SpoIIE457–827 protein was grown in fully supplemented M9 media. Fifteen minutes before induction, 100 mg/L L-Phenylalanine, 50 mg/L L-Isoleucine, 100 mg/L L-Lysine, 50 mg/L L-Leucine, 100 mg/L L-Threonine, 50 mg/L L-Valine, and 60 mg/L L-Selenomethionine were added. Otherwise induction and purification were identical to the un-derivatized protein.

Recombinant SpoIIE590–827 (with an amino acid substitution A624I that was designed to block domain swapping) was overproduced from E. coli BL21 (DE3) harboring a pET-YSBLIC derivative plasmid. Cultures were grown at 37°C and induced at OD600 = 0.6–0.7 by addition of IPTG to 1 mM followed by overnight growth at 16°C. Cells were harvested and the pellets resuspended in 20 mM sodium phosphate (pH 7.5), 0.5 M NaCl, 20 mM imidazole (Buffer A). The supernatant was loaded onto a HiTrap Ni-NTA column equilibrated with buffer A and eluted with a 20–500 mM imidazole gradient in buffer A. Fractions containing SpoIIE were concentrated before loading on to a Superdex S200 column equilibrated with 20 mM Tris pH 8.5, 150 mM NaCl.

### X-ray structure determination

SpoIIE457–827 crystals were grown in sitting drops using Swissci 3 well 96 well plates (Hampton, Aliso Viejo, CA) with 40 µl well solution (0.5 mM LiSO4, 8% PEG8000, 0.05 mM NaF, 6% glycerol). SpoIIE457–827 (11 mg/mL) in 20 mM K•HEPES pH 8, 50 mM NaCl, 2 mM DTT was supplemented with 0.05 mM NaF and mixed at a 2:1 ratio with well solution in 300 nL drops using an NT8 robot (Formulatrix, Bedford, MA). Crystals grew over two weeks at room temperature. Crystals were cryoprotected by serial transfer to well solution supplemented with 10% and then 15% glycerol and plunged in liquid nitrogen. Data were collected at the Advanced Photon Source at Argonne National Laboratory on NE-CAT beamlines 24ID-C and 24ID-E.

Data were processed using HKL-2000 (Otwinowski and Minor, 1997) and initial phases were determined by molecular replacement using MR-PHASER RRID:SCR_014219 (McCoy et al., 2007) and an unswapped model from the published structure of SpoIIE590–827 as the search model (Levdikov et al., 2012). Iterative model building and refinement was done in COOT RRID:SCR_014222 (Emsley et al., 2010) and refinement in PHENIX RRID:SCR_014224 (Adams et al., 2010). Non-crystallographic symmetry was initially enforced for the five chains in the asymmetric unit, then released first for chain B and finally for all chains. In later stages of refinement NCS was again imposed on regions where the chains differed by less than 4 Å. Model restraints were used based on the structure of SpoIIE590–827 published here during an intermediate stage of refinement.

The model for SpoIIE457–827 was additionally validated using anomalous signal from crystals grown with seleno-methionine derivatized protein (Table 2). With the exception of M557, signals were observed for all methionines at the expected sites in the anomalous difference map (an example is shown in Figure 1—figure supplement 1A).

Crystallization experiments with SpoIIE590–827 consistently led to crystals of the domain-swapped dimeric form of the protein, even though SEC-MALLS analysis showed that SpoIIE590–827 is predominantly monomeric (Levdikov et al., 2012). To stabilize the PP2C domain and slow down/prevent domain-swapping during crystallization, we introduced residue substitutions to reinforce the interface involved in domain-swapping. One such SpoIIE590–827 mutant, A624I, constructed by Quikchange mutagenesis (changing the GCA codon to ATA), led to the crystallization of SpoIIE590–827 without domain swapping. Residues with bulkier aliphatic side-chains (L, I, V or M) are found at the position corresponding to A624 in many SpoIIE orthologues.

Crystals of SpoIIE590–827(A624I) were grown from hanging drops formed by mixing 1 µl of 38 mg/mL protein with 1 µL of 2 M sodium formate, 100 mM sodium acetate, pH 4.6. The crystals were cryo-protected in mother liquor containing 4 M sodium formate for X-ray data collection on beamline I02 at the DIAMOND Light Source. Data extending to 2.44 Å spacing were collected and processed using HKL-2000 (Otwinowski and Minor, 1997). Initial phases were determined by molecular replacement using MOLREP (Vagin and Teplyakov, 2010), and a coordinate set derived from PDB ID 3T91 as the search model. The structure was rebuilt and refined using iterative cycles of COOT RRID:SCR_014222 (Emsley et al., 2010) and REFMAC RRID:SCR_014225 (Murshudov et al., 1997) respectively. Data collection and refinement statistics are given in Table 1.

### SEC-MALLS

SEC-MALLS was performed by loading 100 µL of 200 µM SpoIIE457–827 to a Wyatt WTC-030S5 column using an Agilent HPLC in line with Wyatt DAWN-HELIOS and Optilab rEX detectors. Before running SpoIIE457–827 was exchanged to 25 mM K•HEPES pH 8, 100 mM NaCl using a Superdex 200 column. The SEC-MALLS instrument was equilibrated in 25 mM K•HEPES pH 8, 100 mM NaCl, supplemented with MnCl2 as appropriate. SpoIIE457–827 samples were supplemented with MnCl2 shortly before running on the SEC-MALLS. Analysis was conducted using the ASTRA software. All SEC-MALLS samples were run in at least triplicate. SEC experiments shown in Figure 4—figure supplement 1 were conducted similarly, loading 200 µL of 200 µM SpoIIE457–827 on a 20 mL Superdex 200 column on an AKTA FPLC.

### Phosphatase assays

Phosphatase assays were performed as reported in Bradshaw and Losick, 2015. SpoIIAA, SpoIIAA-P, and SpoIIAB were produced and purified as described previously. SpoIIAA-P was produced by overexpression of 6H-SpoIIAA in an E. coli strain that also expressed SpoIIAB (Levdikov et al., 2012). To produce 32P labeled SpoIIAA-P, 75 µM SpoIIAA, 5 µM SpoIIAB and 50 µCi of γ-32P ATP were incubated overnight in 50 mM K•HEPES pH 7.5, 50 mM KCl, 750 µM MgCl2, 2 mM DTT. The protein was exchanged to 20 mM K•HEPES pH 7.5, 200 mM NaCl, 2 mM DTT over a Zeba spin column (Pierce) to remove unincorporated nucleotide and then flowed over Q sepharose resin to remove SpoIIAB. Phosphatase assays were performed in 25 mM K•HEPES pH 8, 100 mM NaCl, 100 µg/ml BSA (supplemented with MnCl2 as appropriate) with 2.5 µM SpoIIE and 200 µM SpoIIAA-P. Reactions were started by adding SpoIIE to a mixture containing SpoIIAA-P and MnCl2. Reactions were stopped in 1 M KPO4 pH 3.3, 2% Triton X-100 and run on PEI-Cellulose TLC plates developed in 1 M LiCl2, 0.8 M Acetic Acid, and imaged on a Typhoon (GE Life Sciences, Pittsburgh, PA). Phosphatase assays were performed more than three independent times as separate experiments.

### B. subtilis strains and analysis

B. subtilis strains were constructed using standard molecular genetic techniques (Harwood and Cutting, 2010) in the PY79 strain background (Youngman et al., 1984; Zeigler et al., 2008) and were validated to contain the correct constructs by double-crossover recombination at the correct insertion site. All strains used in this study are described in Table 3. For imaging, cells were grown at 37°C in 25% LB to OD 0.6, resuspended in minimal sporulation resuspension medium, and grown for 2.5 hr. Cells were immobilized on 2.5% agarose pads made with the sporulation resuspension medium and imaged on an Olympus BX-61 upright microscope with a 100X objective. Cells were segmented using SuperSegger (Stylianidou et al., 2016) and analyzed with custom MatLab scripts (Bradshaw and Losick, 2015). Samples were taken from the same cultures for western blot analysis; cells were lysed using a FastPrep (MP-BIO, Santa Ana, CA) and blots were probed with polyclonal α-GFP antibody.

**Table 3.**
 Table of strains. B. subtilis strains (all strains are in the background of PY79-RL3).


<table>
  <thead>
    <tr>
      <th>Strain #</th>
      <th>Genotype</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RL3</td>
      <td>prototrophic</td>
      <td>Youngman et al., 1984</td>
    </tr>
    <tr>
      <td>RL5874</td>
      <td>spoIIE::kan yxiD::spoIIE-yfp spc amyE::PspoIIE-cfp cm</td>
      <td>Bradshaw and Losick, 2015</td>
    </tr>
    <tr>
      <td>RL5902</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp L646K spc</td>
      <td>Bradshaw and Losick, 2015</td>
    </tr>
    <tr>
      <td>RL5904</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp Q483A spc</td>
      <td>Bradshaw and Losick, 2015</td>
    </tr>
    <tr>
      <td>RL5905</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp G486K spc</td>
      <td>Bradshaw and Losick, 2015</td>
    </tr>
    <tr>
      <td>RL5907</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp E639K spc</td>
      <td>Bradshaw and Losick, 2015</td>
    </tr>
    <tr>
      <td>RL6198</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp V480K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6199</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp A481K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6200</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp L484K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6201</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp V487K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6202</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp S488K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6203</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp V490K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6204</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp M491K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6205</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp D493K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6206</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp F494K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6207</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp S495K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6208</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp E497K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6209</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp I498K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6210</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp E642K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6211</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp I650K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6212</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp T663K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6213</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-yfp I667K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL5915</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-∆tag-yfp L646K spc</td>
      <td>Bradshaw and Losick, 2015</td>
    </tr>
    <tr>
      <td>RL6246</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-∆tag-yfp V480K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6247</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-∆tag-yfp L484K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6248</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-∆tag-yfp V487K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6249</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-∆tag-yfp F494K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6250</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-∆tag-yfp I498K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6251</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-∆tag-yfp I650K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6252</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-∆tag-yfp T663K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6253</td>
      <td>spoIIE::kan yhdGH::PspoIIQ-cfp tet amyE::spoIIE-∆tag-yfp M491K spc</td>
      <td>this study</td>
    </tr>
    <tr>
      <td colspan="3">E. coli strains</td>
    </tr>
    <tr>
      <td>RL6214</td>
      <td>BL21 (DE3) pET47b H6-3C-spoIIE 457–827</td>
      <td>This study</td>
    </tr>
    <tr>
      <td>RL6215</td>
      <td>BL21 (DE3) pET47b H6-3C-spoIIE 457–827 V697A</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6216</td>
      <td>BL21 (DE3) pET47b H6-3C-spoIIE 457–827 D628A</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6217</td>
      <td>BL21 (DE3) pET47b H6-3C-spoIIE 457–827 L484K</td>
      <td>this study</td>
    </tr>
    <tr>
      <td>RL6218</td>
      <td>BL21 (DE3) pET23a H6-sumo-spoIIAA</td>
      <td>Bradshaw and Losick, 2015</td>
    </tr>
    <tr>
      <td>RL6219</td>
      <td>BL21 (DE3) pET23a H6-sumo-spoIIAB</td>
      <td>Bradshaw and Losick, 2015</td>
    </tr>
    <tr>
      <td>AW2001</td>
      <td>BL21 (DE3) pET-YSBLIC H6-3C-spoIIE 590–827 A624I</td>
      <td>Levdikov et al., 2012</td>
    </tr>
    <tr>
      <td>AW2002</td>
      <td>BL21 (DE3) pET-YSBLIC H6-3C-spoIIAA spoIIAB</td>
      <td>Levdikov et al., 2012</td>
    </tr>
  </tbody>
</table>
