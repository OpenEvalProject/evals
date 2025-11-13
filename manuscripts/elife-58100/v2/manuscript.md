# Structural insight into toxin secretion by contact-dependent growth inhibition transporters

## Authors

- Jeremy Guerin<sup>1</sup> ([ORCID: 0000-0003-2622-040X](https://orcid.org/0000-0003-2622-040X))
- Istvan Botos<sup>1</sup>
- Zijian Zhang<sup>2</sup>
- Karl Lundquist<sup>2</sup>
- James C Gumbart<sup>2</sup> ([ORCID: 0000-0002-1510-7842](https://orcid.org/0000-0002-1510-7842))
- Susan K Buchanan<sup>1</sup> ([ORCID: 0000-0001-9657-7119](https://orcid.org/0000-0001-9657-7119)) †

### Affiliations

1. Laboratory of Molecular Biology, NIDDK, NIH Bethesda United States
2. School of Physics, Georgia Institute of Technology Atlanta Georgia

† Corresponding author

## Abstract

Bacterial contact-dependent growth inhibition (CDI) systems use a type Vb secretion mechanism to export large CdiA toxins across the outer membrane by dedicated outer membrane transporters called CdiB. Here, we report the first crystal structures of two CdiB transporters from Acinetobacter baumannii and Escherichia coli. CdiB transporters adopt a TpsB fold, containing a 16-stranded transmembrane β-barrel connected to two periplasmic domains. The lumen of the CdiB pore is occluded by an N-terminal α-helix and the conserved extracellular loop 6; these two elements adopt different conformations in the structures. We identified a conserved DxxG motif located on strand β1 that connects loop 6 through different networks of interactions. Structural modifications of DxxG induce rearrangement of extracellular loops and alter interactions with the N-terminal α-helix, preparing the system for α-helix ejection. Using structural biology, functional assays, and molecular dynamics simulations, we show how the barrel pore is primed for CdiA toxin secretion.

## Introduction

In bacterial ecosystems, competition for limited nutrients can be a life or death battle. To fight for resources, some Gram-negative bacteria employ direct toxin exchange through a process known as Contact-Dependent growth Inhibition (CDI). This process was first described in Escherichia coli EC93, where a two-partner secretion system consisting of a CdiA toxin and a CdiB transporter was shown to inhibit other E. coli strains (Aoki et al., 2005). CdiB is an outer membrane transporter that releases its CdiA toxin to the cell surface. Once contact occurs, a toxin domain at the CdiA C-terminus is cleaved and imported into the target bacterium to inhibit growth. To prevent self-destruction, CDI systems also express an immunity protein, CdiI, which protects against CdiA toxins delivered from neighboring cells (Figure 1—figure supplement 3; Aoki et al., 2005; Ruhe et al., 2018; Ruhe et al., 2017).

CdiA and CdiB belong to the Two-Partner Secretion family of proteins (TPS; Type Vb secretion system). The core of a TPS system consists of two proteins called TpsA for the secreted proteins, and TpsB for their cognate transporters (Guérin et al., 2017). Like TpsA, CdiA toxins are predicted to fold into a β-helix, forming an elongated filament that extends several hundred angstroms from CdiB transporters (Clantin et al., 2004; Ruhe et al., 2018). CdiA proteins are synthesized in the cytoplasm and contain two N-terminal domains directing their secretion: a signal peptide and a TPS domain (Figure 1—figure supplement 3). After inner membrane translocation and signal peptide removal by the SEC machinery, the CdiA TPS domain interacts with the periplasmic domains of its cognate CdiB transporter (Baud et al., 2014; Clantin et al., 2004; Delattre et al., 2011; Hodak et al., 2006). At this point, translocation across the outer membrane is initiated and the rest of the protein is folded at the surface of the bacterium. Domain organization and folding during secretion are still poorly understood, however a study using electron cryo-tomography suggests that secretion occurs in two distinct steps (Ruhe et al., 2018). In this model, the CdiA N-terminal half of the protein, including the TPS and FHA-1 domains, is secreted first and forms a 330 Å filament exposing the receptor-binding domain (RBD). The RBD recognizes a specific membrane receptor on the surface of a neighboring cell, triggering the second secretion step (Ruhe et al., 2018; Ruhe et al., 2017). The CdiA C-terminal half of the protein, which was still in the periplasm, is now released and exported to the cell surface. A short tyrosine- and proline-rich region and a second filamentous hemagglutinin domain (FHA-2) fold and then associate with the outer membrane of the target bacterium to deliver the C-terminal toxin. The toxin domain is cleaved from the rest of the CdiA protein by an unknown mechanism, and then released into the target cell.

CdiB proteins are members of the Omp85 superfamily. There are two functionally distinct protein classes in the Omp85 superfamily: BamA/TamA proteins that insert newly synthesized outer membrane proteins into the outer membrane, and TpsB proteins that secrete cognate protein substrates to the extracellular surface (Figure 1—figure supplement 3; Gentle et al., 2004; Guérin et al., 2017; Heinz and Lithgow, 2014). While there are several BamA, TamA, and BAM complex structures (Bakelar et al., 2016; Gruss et al., 2013; Gu et al., 2016; Noinaj et al., 2013), only one TpsB structure has been characterized: Bordetella pertussis FhaC (Clantin et al., 2007; Maier et al., 2015). This TpsB transporter secretes a major adhesin called filamentous haemagglutinin (FHA). BamA/TamA and TpsB proteins share a common fold with distinct features enabling either insertion into the membrane, or secretion across it. The two protein classes use a 16-stranded β-barrel to span the outer membrane, connected to a series of N-terminal periplasmic interaction modules called polypeptide-transport-associated (POTRA) domains. Inside the β-barrel lumen, extracellular loop 6 (L6) forms a ‘lid-lock’ through interactions between two essential signature motifs: (V/I)RG(Y/F) at the tip of L6 and (F/G)xDxG on strand β13 (Gruss et al., 2013; Maier et al., 2015; Noinaj et al., 2013). Mutagenesis experiments have shown that L6 is essential for activity but its precise function is unclear (Guérin et al., 2015; Höhr et al., 2018; Leonard-Rivera and Misra, 2012; Rigel et al., 2013). In addition, TpsB proteins contain an N-terminal α-helix (H1) inserted into the barrel pore that is not found in BamA/TamA proteins. H1 is connected to the first POTRA domain by a short periplasmic polypeptide; this linker has been shown to be essential for secretion in the FhaC/FHA system. Since H1 blocks the barrel pore in the resting conformation, it must be removed for secretion to occur (Figure 1—figure supplement 3; Baud et al., 2014; Guérin et al., 2014; Maier et al., 2015).

Here we report the first crystal structures of CdiB transporters from A. baumannii (ACICU) and E. coli (EC93). Two distinct conformations for H1 are observed within the β-barrel lumen. Using structure-based sequence alignment, we identified a conserved DxxG motif on strand β1 that is found in all TpsB transporters but not in BamA/TamA proteins. We show that the role of DxxG is to increase the flexibility of strand β1, which in turn affects the β1–β16 interface. We developed a secretion assay to show that CdiB transporters specifically secrete their cognate CdiA proteins and used this assay to analyze the functions of individual amino acids in CdiA secretion. Molecular dynamics simulations illustrate ejection of H1 from β-barrel lumen. Our results highlight conformational changes in the β-barrel domain that facilitate pore opening and secretion of the substrate.

## Results

### Two CdiB transporter structures

We determined two full-length crystal structures of CdiB transporters from Acinetobacter baumannii (strain ACICU) and E. coli (strain EC93), which will be referred to as CdiBAb and CdiBEc. CdiBAb and CdiBEc structures were built and refined to final resolutions of 2.4 Å and 2.6 Å, respectively (Table 1). Despite low sequence similarity (21% sequence identity), both structures adopt a common fold: an N-terminal α-helix (H1) is inserted into the lumen of the β-barrel and is connected by a ~ 20 residue linker to two periplasmic POTRA domains. The POTRA domains have a conserved βααββ fold and extend away from the β-barrel (Figure 1). The C-terminal β-barrel consists of 16 antiparallel β-strands organized as an oblique cylinder with cross-sectional dimensions of 35 Å x 25 Å. The longest β-strands (β5 to β8) form an extended β-sheet that may serve to anchor the CdiA substrate to initialize its folding (Baud et al., 2014; Figure 1 and Supplementary file 1).

![Figure 1.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig1-v2.jpg)

**Figure 1.:** Membrane view (upper panel) and periplasmic view (lower panel) of (A) CdiB from Acinetobacter baumannii (CdiBAb) in light teal and, (B) CdiB from Escherichia coli (CdiBEc) in pale yellow. The first POTRA domain is indicated by P1, and the second POTRA domain, closer to the β-barrel, by P2. Inside the β-barrel, the N-terminal helix H1 is shown in blue and Loop 6 (L6) in magenta. The linker connecting H1 to P1 is also colored blue. The first and last β-strands from the β-barrel are shown in yellow, with the DxxG motif in orange. In the lower panels, selected sidechains from DxxG and L6 are shown as sticks, with the interacting loop 6 residue highlighted.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Extracellular loops 1, 2, and 5 from CdiBEc structure are colored in orange (indicated by L1, L2, and L5). (A) Extracellular view of the network of interaction (dashed lines) between helix H1 (blue), loop 6 (magenta) and loop 1. Lysine 440 from loop 6 stabilizes N211, the second residue of the conserved DxxG motif. The long extracellular loop 5 is stabilized by interactions with loop 6 and β8 from the β-barrel (pale yellow). (B) zoomed view of loop 1-helix H1-loop 6 interactions where Q214 forms hydrogen bonds with two residues from helix H1 (R10 and Q14), while R10 also interacts with K440 from loop 6. The loop 1 conformation is secured by an interaction between S245 on β3 and T217-G218 on loop 1. As seen in the sequence alignment (Supplementary file 1), the glycine of the DxxG motif, and T217-G218 residues are conserved, and the CdiBEc structure displays their spatial proximity. The conserved glycines complete the turn made by loop 1, where one amine group interacts with the carbonyl group of T217. (C) side view of loop 5 showing three hydrophobic residues (M370, W372, F373) that extend outside the β-barrel toward the outer membrane, potentially interacting with the membrane bilayer.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** View of the periplasmic region for (A) CdiBAb and, (B) CdiBEc. The α-helix proximal to the β-barrel lumen is labeled α4, where a conserved glutamate forms a salt bridge with an arginine and a lysine present on β6 and β7 from the β-barrel in both structures. On the same face of α4, a polar residue connects the N-terminal region of the linker (colored in blue). A zoomed view of this region is shown in the inset. The C-terminal region of the linker shows greater variation between the CdiB structures, where the linker in CdiBAb makes multiple interactions along the α2 helix of POTRA1. In both structures, the conserved cysteines (colored in red) form a disulfide bond that connects the linker to POTRA1. The two residues missing in the CdiBEc linker are represented by dashed lines.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** In the cytoplasm, the CDI operon synthetizes CdiB and CdiA as preproteins. The N-terminal signal peptide (represented by a yellow box) is cleaved by the SEC complex (yellow) during inner membrane translocation. In the periplasm, CdiB and CdiA follow two different pathways (aided by periplasmic chaperones; not shown). As a TpsB transporter, CdiB interacts with the BAM complex, which folds and inserts CdiB into the outer membrane. BamA (brown), the central element of the BAM complex, and TpsB transporters are part of the same Omp85 superfamily sharing structural homologies (loop 6 and periplasmic POTRA domains (P) are indicated). CdiAs are large multi-domains proteins: the signaling domains TPS and RBD are represented in light green, FHA-1 and FHA-2 domains in dark green, and C-terminal toxin domain in red. In the periplasm, the N-terminal TPS domain recognizes and interacts with CdiB POTRA domains to initiate outer membrane translocation. At the surface of the cell, CdiA forms a filament folded as a β-helix that presents the RBD and toxin domains to neighboring bacteria. To prevent fratricide and auto-inhibition, the CDI operon produces a cytoplasmic immunity protein (CdiI). The boundaries of CdiB, CdiA, and BamA proteins are indicated by ‘N-ter’ and ‘C-ter’.

**Table 1.**
 Data collection and refinement statistics for CdiBAb and CdiBEc.


<table>
  <thead>
    <tr>
      <th></th>
      <th>CdiB Ab (Se)</th>
      <th>CdiB Ab</th>
      <th>CdiB Ec</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4">Data collection</td>
    </tr>
    <tr>
      <td>λ (Å)</td>
      <td>0.979415</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P1</td>
      <td>P1</td>
      <td>P21212</td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>47 49.3 86.8</td>
      <td>46.9 49.3 86.8</td>
      <td>45.3 112.9 183.4</td>
    </tr>
    <tr>
      <td>α, β, γ (°)</td>
      <td>100.7 90.6 109.9</td>
      <td>100.8 90.4 109.9</td>
      <td>90 90 90</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>50–2.6</td>
      <td>50–2.4</td>
      <td>50–2.6</td>
    </tr>
    <tr>
      <td>Rsym/Rmerge†*</td>
      <td>0.1 (1.4)</td>
      <td>0.1 (1.3)</td>
      <td>0.1 (1.3)</td>
    </tr>
    <tr>
      <td>I / σ (I)*</td>
      <td>13.6 (1.4)</td>
      <td>10.1 (1.3)</td>
      <td>13.9 (2.0)</td>
    </tr>
    <tr>
      <td>CC (1/2) (%)*</td>
      <td>0.998 (0.688)</td>
      <td>0.99 (0.619)</td>
      <td>0.99 (0.9)</td>
    </tr>
    <tr>
      <td>Completeness (%)*</td>
      <td>90.8 (90.0)</td>
      <td>97.0 (82.4)</td>
      <td>99.9 (100)</td>
    </tr>
    <tr>
      <td>Ano Completeness (%)*</td>
      <td>90.1 (89.5)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Redundancy*</td>
      <td>7.7 (7.7)</td>
      <td>5.8 (5.6)</td>
      <td>13 (13.5)</td>
    </tr>
    <tr>
      <td colspan="4">Refinement</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td></td>
      <td>44–2.4</td>
      <td>44–2.6</td>
    </tr>
    <tr>
      <td>No. reflections</td>
      <td></td>
      <td>27153</td>
      <td>29889</td>
    </tr>
    <tr>
      <td>Rwork§/Rfree¶</td>
      <td></td>
      <td>0.20/0.25</td>
      <td>0.24/0.26</td>
    </tr>
    <tr>
      <td colspan="4">r.m.s. deviations</td>
    </tr>
    <tr>
      <td>Bonds (Å)</td>
      <td></td>
      <td>0.003</td>
      <td>0.002</td>
    </tr>
    <tr>
      <td>Angles (°)</td>
      <td></td>
      <td>0.61</td>
      <td>0.58</td>
    </tr>
    <tr>
      <td>No. Protein atoms</td>
      <td></td>
      <td>4256</td>
      <td>4130</td>
    </tr>
    <tr>
      <td>No. Ligand atoms</td>
      <td></td>
      <td>52</td>
      <td>90</td>
    </tr>
    <tr>
      <td>No. Waters</td>
      <td></td>
      <td>55</td>
      <td>13</td>
    </tr>
    <tr>
      <td colspan="4">B-factors (Å2)</td>
    </tr>
    <tr>
      <td>Wilson B</td>
      <td></td>
      <td>53.20</td>
      <td>68.29</td>
    </tr>
    <tr>
      <td>Protein</td>
      <td></td>
      <td>59.6</td>
      <td>79.1</td>
    </tr>
    <tr>
      <td>Ligands</td>
      <td></td>
      <td>69.1</td>
      <td>81.2</td>
    </tr>
    <tr>
      <td>Waters</td>
      <td></td>
      <td>54.4</td>
      <td>58.5</td>
    </tr>
    <tr>
      <td colspan="4">Ramachandran Analysis</td>
    </tr>
    <tr>
      <td>Favored (%)</td>
      <td></td>
      <td>98.3</td>
      <td>97.18</td>
    </tr>
    <tr>
      <td>Allowed (%)</td>
      <td></td>
      <td>1.7</td>
      <td>2.82</td>
    </tr>
    <tr>
      <td>Outliers (%)</td>
      <td></td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td></td>
      <td>6WIL</td>
      <td>6WIM</td>
      <td>PDB code</td>
    </tr>
  </tbody>
</table>

_†Rsym = Σhkl,j (|Ihkl-<Ihkl > |) / Σhkl,j Ihkl, where < Ihkl > is the average intensity for a set of j symmetry-related reflections and Ihkl is the value of the intensity for a single reflection within a set of symmetry-related reflections.§R factor = Σhkl (||Fo| - |Fc||) / Σhkl|Fo| where Fo is the observed structure factor amplitude and Fc is the calculated structure factor amplitude.¶Rfree = Σhkl,T (||Fo| - |Fc||) / Σhkl,T|Fo|, where a test set, T (5% of the data), is omitted from the refinement.* Statistics for highest resolution shell shown in parentheses._

The extracellular surface of the β-barrel is composed of long loops in mostly extended conformations that allow access to the barrel pore and would facilitate CdiA secretion. In TpsB/CdiB proteins, extracellular loop 5 is usually longer than other extracellular loops; the entire loop 5 can be traced in CdiBEc but electron density is missing for CdiBAb (residues 389–411) and FhaC (residues 381–399; PDB: 4QKY). In CdiBEc, loop 5 is stabilized by contacts with loop 6 (R421) and two residues from strand β8 (R340 and T343) (Figure 1—figure supplement 1). Interestingly, this loop contains three hydrophobic residues (M370, W372, F373) that extend outward from the β-barrel toward the membrane, with sidechains potentially interacting with the bilayer lipopolysaccharides.

On the periplasmic side of the outer membrane, the two POTRA domains exhibit the conserved βααββ fold characteristic of Omp85 proteins (Figure 1—figure supplement 2). A network of interactions connects β-barrel-POTRA2 and the linker through conserved charged residues. A glutamate from helix α4 of POTRA2 (E179 in CdiBAb and E168 in CdiBEc) forms a salt bridge with an arginine and a lysine present on strands β6 and β7, respectively (R325-K330 in CdiBAb and R309-K314 in CdiBEc), while the N-terminal region of the linker (Y35 in CdiBAb and S34-A35 in CdiBEc) is also stabilized by side chains from α4 (D175 for CdiBAb, and R161-E164 for CdiBEc). Some of these interactions are also seen in the FhaC structure, and biochemical experiments have shown that the interactions between POTRA2 and the linker are essential for substrate recognition and secretion (Baud et al., 2014; Delattre et al., 2011; Maier et al., 2015). These conserved interactions emphasize the importance of the POTRA domains for TpsB function.

The linker connecting H1 to POTRA1 is well defined in the electron density maps. In CdiBAb, the linker is stabilized by a network of interactions with helices α2 and α4 from POTRA1 and POTRA2, respectively (Figure 1—figure supplement 2). In both CdiB structures, the C-terminal part of the linker is attached to POTRA1 by a disulfide bond between two cysteines, an interaction that is conserved in all CdiB transporters (and some TpsB transporters). While a network of interactions stabilizes the N-terminal linker region near the β-barrel lumen, the middle region of the linker appears more flexible, sharing fewer surface interactions with POTRA1 (especially for CdiBEc where residues 42–43 are missing in the electron density). This position differs slightly between CdiBAb and CdiBEc, confirming the biochemical and biophysical studies that have shown multiple linker conformations in the resting state (Guérin et al., 2014; Maier et al., 2015; Figure 1, Figure 1—figure supplement 2).

### Structural differences in helix H1

Both CdiB structures adopt the same overall architecture, with H1 and L6 occluding the interior of the β-barrel. However, H1 is positioned very differently in CdiBAb and CdiBEc (Figure 2, Video 1): the angle between H1 and the β-barrel is about 10° for CdiBAb, versus 25° for CdiBEc. In addition, H1 sits higher in the barrel pore in CdiBAb, positioning its N-terminus closer to the extracellular surface. In this orientation, H1 interacts with the inner barrel wall using 12 H-bonds and three salt bridges, with no interactions to loop 6, for a total buried surface area of 1263 Å2 (Figure 2, Figure 2—source data 1). In CdiBEc, H1 in sits 4.8 Å lower in the barrel pore, allowing it to form 5 H-bonds with loop 6, and 8 H-bonds with the barrel wall, for a total buried surface of 1385 Å2.

![Figure 2.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig2-v2.jpg)

**Figure 2.:** (A) Membrane view of a superposition of CdiBAb (light teal) and CdiBEc (pale yellow) that illustrates conformational differences of helix H1 inside the β-barrel. To better visualize helix H1, β-strands from the front of the barrel are transparent. (B) Molecular surface cross-section of CdiBAb (light teal) and CdiBEc (pale yellow) where helix H1 and linker are shown in blue.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Root-Mean-Square Deviation (RMSD) of the position of helix H1 for the two CdiB models generated by Targeted Molecular Dynamics (TMD) simulations. Top panels, CdiBAb structure where the helix H1 is moved from its initial position toward the position of the CdiBEc helix H1. Bottom panels, CdiBEc structure where the helix H1 is moved from its initial position toward the position of the CdiBAb helix H1. TMD was run for 30 ns, followed by 30 ns of H1 restrained to the new position, and then 120 ns of free equilibration. (A) CdiBAb H1 RMSD comparison with the initial frame (CdiBAb crystal structure). (B) CdiBAb H1 RMSD comparison with the targeted model (CdiBEc H1 position). (C) CdiBEc H1 RMSD comparison with the initial frame (CdiBEc crystal structure). (D) CdiBEc H1 RMSD comparison with the targeted model (CdiBAb H1 position).

![Video 1.](https://cdn.elifesciences.org/articles/58100/elife-58100-video1.mp4.jpg)

**Video 1.:** Linear interpolation morph of CdiBAb and CdiBEc crystal structures highlights the conformational differences observed. Helix H1 adopts a different angle and is positioned at a different height in the two structures. β1 twists inward, whereas loop 2 is oriented outward. The POTRA domains are relatively rigid. We note that although the length of the small α-helix in POTRA 1 differs between CdiBAb and CdiBEc, the mobility detected in the morph movie is probably an artefact due to the length.

To better understand the orientation of H1 in the β-barrel lumen, we generated two models using the targeted molecular dynamics method (TMD). The first model is based on the structure of CdiBAb, where the helix H1 is moved from its initial position toward the position of the CdiBEc helix H1. The second model is based on the structure of CdiBEc, where the helix H1 is moved from its initial position toward the position of CdiBAb helix H1. TMD was run for 30 ns, followed by 30 ns of H1 restrained to the new position, and then 120 ns of free equilibration (Video 2). For both models, analysis of RMSD during free equilibration reveal that H1 is stable in the new position and does not revert to the initial state (Figure 2—figure supplement 1, Video 2). This result suggests that H1 can adopt either orientation in both systems.

![Video 2.](https://cdn.elifesciences.org/articles/58100/elife-58100-video2.mp4.jpg)

**Video 2.:** From the initial state: X-ray structures of CdiBAb (left) or CdiBEc (right), the helix H1 is displaced toward the position of the helix from CdiBEc helix (left) or CdiBAb (right).

Our results on the position of H1 in CdiB agree with previous studies that have reported high flexibility for H1 in the TpsB transporter FhaC. Acting as a plug domain, H1 exists in different states in the resting conformation and can undergo a large conformational change to fully open the β-barrel pore during secretion (Baud et al., 2014; Guérin et al., 2014). The structural variations observed in our CdiB structures illustrate at least two conformations that include different interactions with the interior of the β-barrel, loop 6 and extracellular loops.

### Extracellular loop 6 and the DxxG motif on strand β1

Like H1, L6 sits in the interior of the β-barrel and partially occludes it. This conformation is maintained by a conserved salt bridge between an arginine on the tip of L6 (from the (V/I)RG(F/Y) motif) and an aspartate on strand β13 ((F/G)xDxG motif), an interaction observed in all Omp85 structures (Gruss et al., 2013; Gu et al., 2016; Maier et al., 2015; Noinaj et al., 2013). In addition, in the CdiBAb and CdiBEc structures, the arginine is also stabilized by a glutamate from β12 (E483 and E455 respectively) (Figure 3A and B). This position inside the β-barrel lumen allows loop 6 sidechains to point toward the β1–β16 interface. Loop 6 uses different interactions with β1 to stabilize alternate conformations in CdiBAb and CdiBEc involving the β1–β16 interface and extracellular loops 1 and 2 (Figure 3C and D, Video 1).

![Figure 3.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig3-v2.jpg)

**Figure 3.:** Zoomed view of loop 6 (L6, magenta) in the lumen of the β-barrel of (A) CdiBAb (light teal) and, (B) CdiBEc (pale yellow). Sidechains involved in the network of interactions between L6 (VRGF/Y motif), β12 and β13 (F/GxDxG motif) and the DxxG motif (orange) are indicated by black dashed lines. β1 and β16 are colored in yellow, and extracellular loops 1 and 2 are indicated by ‘L1' and ‘L2', respectively. A conformational difference is shown between CdiB structures: in CdiBAb, R460, located before the VRG(F/Y) motif, interacts with the first and third residues of the DxxG motif, while In CdiBEc, K440 located after VRG(F/Y), interacts with the second residue of DxxG. Membrane view of the β-barrel of (C) CdiBAb and, (D) CdiBEc where β2–4 are highlighted in light teal and pale yellow respectively. β1 and β16 are highlighted in yellow, and DxxG motif in orange with important residues numbered. At the β1–β16 interface, mainchain interactions are shown as black dashed lines, and sidechain interactions as red dashed lines. In CdiBEc the two sidechains from L6 pointing toward β1–β16 are shown.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Superposition of CdiBEc (pale yellow) and FhaC (blue, PDB: 4QKY). Helix H1 lies at the same angle inside the barrel and the β1–β16 interface is shorter, where the second residue of DxxG (N219) stabilizes β16 and starts loop 1. Loop 1 is flexible and twisted inward, whereas loop 2 is oriented outward. (A) Membrane view illustrates conformational similarities between the CdiBEc (pale yellow) and FhaC (blue) structures. N-terminal helix H1, loop 1, loop 2, loop 6, and the first β-strand are indicated by H1, L1, L2, L6, and β1, respectively. For clarity, the front of the β-barrel is transparent. (B) Membrane view of the β-barrel of FhaC for comparison with Figure 3D. Helix H1 and strands β2 - β4 are highlighted in blue. β1 and β16 are highlighted in yellow, with the DxxG motif in orange. Interactions between β1 and β16 are shown by black dashed lines. (C) Extracellular view of DxxG-H1-L6 in FhaC structure. R17 from helix H1 (blue) forms a network of interactions between E446 on loop 6 (pink) and the conserved aspartate D218 from the DxxG motif (orange).

Structure-based sequence alignment of TpsB transporters allowed us to identify a conserved sequence, the DxxG motif, where ‘x’ corresponds to polar residues (Supplementary file 1). This region is located on β1, interacts with loop 6, and dictates features of the β1–β16 interface on the extracellular surface of the protein. DxxG can either fully fold as a β-strand or adopt an extended conformation that tilts inward as shown by CdiBAb and CdiBEc, respectively (Figure 3). In CdiBAb, the DxxG motif accounts for four residues on the 12-residue β1 strand, allowing β1 to form an extended β-sheet with β2, β3, and β16 (Figure 3C). The sidechains of the first and third residues (D224 and S226) interact with R460 from loop 6 (Figure 3A), while the mainchain interacts with strand β2. In this structure, the second and fourth residues of the DxxG motif (D225 and G227) form H-bonds with β16. As a result, the β-barrel is in a fully zipped conformation, stabilized by 10 H-bonds between strands β1 and β16 (Figure 3C). Extracellular loops 1–2 are short, with loop 2 curved inward and partially blocking the top of the channel (Figure 3C). In CdiBEc, the DxxG motif is in an extended conformation and initiates loop 1. As a result, strand β1 is shorter, containing only eight residues. The β-sheet formed by β16 and β1-β3 is also shorter (Figure 3D). In this structure, the β1–β16 interface is stabilized by only 6 H-bonds, although the sidechain from the second residue (N211) of the DxxG motif contributes to additional interactions with β16 that further stabilize the interface (Figure 3D). By increasing the length and flexibility of loop 1, the DxxG motif creates an inward tilting of the loop, allowing it to fold against β2-β3 and interact directly with H1 (Figure 1—figure supplement 1A and B). In this position, loop 1 pushes loop 2 away from the lumen of the barrel. In CdiBEc, the conserved glycine from the DxxG motif is also involved in a large conformational change by completing the turn made by loop 1 (Figure 3D). From our structural analysis, we propose that the role of this region is to increase the flexibility of strand β1, and to facilitate the conformational changes of loop 1 and loop 2.

A comparison of CdiBAb and CdiBEc with TpsB transporter FhaC shows that the structures of FhaC and CdiBEc are virtually identical (Figure 3—figure supplement 1), whereas CdiBAb shows an alternate conformation. The high structural similarity observed between FhaC and CdiB transporters suggests that the large body of research pertaining to FhaC is also relevant to CDI secretion.

### Secretion of CdiA by CdiB is specific

To probe the specificity of CDI systems, we generated an in-vivo functional assay by co-expressing full-length cdiB genes with truncated versions of cdiA genes, to produce only the N-terminal domain of the toxin: CdiA-Nt (containing TPS and part of FHA-1) (Figure 1—figure supplement 3). After induction, the bacterial pellet was separated from the culture supernatant and production of CdiB and CdiA-Nt were detected by Western blotting. As expected, when CdiBAb and CdiA-NtAb are co-expressed, CdiBAb is detected in the pellet, and CdiA-NtAb in the supernatant (Figure 4A). As a control, when only CdiBAb is expressed, no CdiAAb secretion is detected, since the protein is not produced. When only CdiA-NtAb is expressed, neither CdiBAb nor CdiA-NtAb are detected, since no CdiBAb transporter is available to secrete CdiA-NtAb. These results show that the secretion of CdiA-Nt is CdiB dependent. We next asked whether CDI systems are specific. No secretion of CdiA occurs when a different CdiB species is used, despite 50% sequence similarity between the two CdiA-Nt constructs. These results show that CDI toxins and transporters are not interchangeable (Figure 4A). As a control, CdiA-NtEc is detected in the culture supernatant when CdiBEc is expressed. Unfortunately, a small amount of CdiBEc is also detected in the supernatant, indicating that overexpression of CdiBEc can increase bacterial lysis. Therefore, we used only CdiBAb/CdiA-NtAb for subsequent functional analyses.

![Figure 4.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig4-v2.jpg)

**Figure 4.:** Immunoblot analyses of Escherichia coli C41 cultures co-expressing CdiB and CdiA-Nt. (A) After induction, cell pellets ‘P’ and culture supernatants ‘S’ are separated and analyzed to detect the presence of CdiB and CdiA-Nt from Acinetobacter baumannii ACICU ‘Ab’ or E. coli EC93 ‘Ec’, respectively. Dash indicates that cdi genes are present on the plasmid but not induced. CdiA-NtAb 74-472 and CdiA-NtEc 29-416 are only detected in the supernatant when their respective CdiB transporters are present. (B) CdiB variants where helix H1 ‘ΔH1’ and Linker ‘ΔLink’ are genetically deleted and co-expressed with their cognate CdiA-Nt substrates from CDI systems of A. baumannii ‘Ab’ and E. coli ‘Ec’. CdiB and CdiA-Nt wildtype proteins detected in immunoblot are indicated by B and A for A. baumannii ACICU and B* and A* for E. coli. Detection of CdiBΔH1 and CdiBΔH1ΔLink variants are indicated respectively, by a black square and a black circle for A. baumannii; and a white square and a white circle for E. coli. Protein ladder bands indicate 62, 49, 38 kDa respectively.

### Helix H1 and linker influence CdiB stability

To probe the functions of H1 and the linker connecting it to POTRA1, we constructed CdiB variants lacking H1 or lacking both H1 and the linker. The latter construct removes structural elements found in TpsB/CdiB proteins, but not in BamA/TamA proteins, such that only the two POTRA domains and β-barrel are present (Figure 1—figure supplement 3). When just the helix is deleted, there is less CdiB in the pellet fraction, especially for CdiBAb, and correspondingly, a smaller amount of CdiA-Nt is secreted (Figure 4B). This suggests that H1 is important for folding, membrane insertion, and/or stability of CdiB. However, when both the helix and linker are deleted, CdiB is present and secretion of CdiA-Nt occurs (Figure 4B). These results show that the helix and linker are not essential for CdiA-Nt secretion but must be important for CdiB stability. In comparison, the linker was found to be essential for substrate secretion in FhaC and helps to stabilize the POTRA domains (Delattre et al., 2011; Jacob-Dubuisson et al., 2009). However, the precise function of the linker and why its presence alone drastically affects CdiBAb, are unclear. One obvious function of H1 is to plug the β-barrel lumen when substrate is absent, preventing entry/exit of unwanted molecules (Clantin et al., 2007).

### Flexibility of the β1–β16 interface is essential for secretion

In CdiBAb, the DxxG motif increases the length of the first β-strand to 12 residues, rigidifying the β1–β16 interface, but this region appears more flexible in CdiBEc and FhaC structures (Figure 3, Figure 5C, Video 1, Figure 3—figure supplement 1). To understand whether the flexibility of DxxG is important for activity, we engineered paired cysteine variants between β1 and β16 to stabilize the conformation of CdiBAb. The CdiBAb cysteine variants were then tested for their ability to secrete CdiA-NtAb in the absence or presence of the reducing agent TCEP. Disulfide bond formation was analyzed by Western blot (Figure 5). Clear disulfide bond formation was observed for all mutants positioned in the middle of the β-sheet. When β1 and β16 are cross-linked, substrate secretion is greatly impaired, however reduction of the disulfide rescues secretion (Figure 5A). To confirm that crosslinking β1–β16 does not impair CdiBAb biogenesis, we monitored expression of CdiB D224C/S555C and secretion of CdiA-Nt over time (Figure 5B). CdiBAb was detected in the pellet from 20 to 100 min after induction, in the presence or absence of TCEP. In comparison, the secretion of CdiA-Nt is greatly increased only when the β1–β16 disulfide is reduced with TCEP. To confirm that the disulfide mutants are correctly targeted to the outer membrane, we isolated and solubilized membranes from the D225C/F554C mutant. The oxidized form was detected in membranes and could be solubilized with detergent (Figure 5—figure supplement 1A). As a control, we confirmed disulfide formation in a strain lacking the periplasmic oxidoreductase, DsbA (Figure 5—figure supplement 1B). Altogether, these results show that secretion of CdiA is inhibited when strands β1 and β16 are tethered, and correspondingly, flexibility of β1 and the DxxG motif facilitate secretion.

![Figure 5.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig5-v2.jpg)

**Figure 5.:** (A) CdiBAb cysteine variants are co-expressed with CdiA-Nt substrate from Acinetobacter baumannii in presence + or absence - of reducing agent ‘TCEP’ in the culture. After induction, pellet ‘P’ and supernatant ‘S’ are separated and analyzed by western blot to detect the presence of CdiA-Nt ‘A’ and, CdiB without cross-linking ‘red’, or CdiB with β1–β16 crosslinked ‘ox’. Protein ladder bands indicate 70, 50, 40 kDa, respectively. (B) After induction (t0) the secretion of CdiA-Nt and the production of CdiBAb double cysteine D224C-S555C are monitored at 10 min intervals. Samples from culture supernatant and bacterial pellet are separated, analyzed by western blot, and the bands corresponding to CdiA-Nt (left) and CdiBAb (right) displayed. For comparison, reducing agent was added to the pellet fraction t100 (‘+DTT’) or incubated with the culture at t0 (‘+TCEP’). (C) Mainchain representation of β1–β16 of CdiB from A. baumannii (left) and E. coli (right) colored in yellow, or orange for the DxxG motif. Adjacent sidechains oriented in the same direction are indicated by dashed lines, where * indicate sidechains involved in H-bonding in the crystal structure. Black circles with white numbers indicate engineered disulfides.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Western blot of isolated membrane fraction from CdiB D225C/F554C double cysteine variant (represented by bold letters A to E). Fraction A, bacterial pellet fraction (‘P ‘lane from Figure 5A). Fraction B, bacterial lysate fraction homogenized three times. Fraction C, supernatant fraction after centrifugation at 7000 g (where inclusion bodies and unlysed cells are removed). Fraction D, pellet from ultracentrifugation at 160,000 g to isolate membrane fractions after a 2% Triton wash (which removes soluble and inner membrane proteins). Membrane fractions are resuspended in 50 mM Tris-HCl, pH7.4, 200 mM NaCl, and solubilized by constant stirring in 5% Elugent. Fraction E, supernatant of a second ultracentrifugation at 220,000 g containing solubilized membrane proteins. As seen in Figure 5, β1–β16 are mostly crosslinked in the D225C-F554C mutant where ‘ox’ and ‘red’ indicate the oxidized and reduced form, respectively. Protein ladder bands indicate 70 and 50 kDa. (B) Western blot analysis of bacterial pellet from CdiBAb D225C/F554C variant expressed in MC4100 E. coli parent cell (dsbA ‘+’) and MC4100 E. coli dsbA:ChloroR strain (dsbA ‘-‘), in absence (second lane) or presence of TCEP (‘+TCEP’).

### Loop 2 and the DxxG motif influence secretion

Based on conformational differences in the CdiB crystal structures, we probed residues that might be important for CdiA secretion. We monitored CdiA secretion over 130 min (Figure 6A, left). We controlled the system so that production does not increase cell lysis, and we monitored the expression levels of CdiB in the bacterial pellet (Figure 6A, right; Figure 6—figure supplement 1A). For all mutants, CdiB was detected after 20 min and levels increased over time. In contrast, levels of secreted wildtype CdiA-Nt are first detected after 60 min. Removing H1 and the linker (WTΔH1ΔLink) slightly improves secretion, with the toxin first detected after 50 min. This result reconfirms that H1 is not essential for TpsB function (Méli et al., 2006; Figure 4B).

![Figure 6.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig6-v2.jpg)

**Figure 6.:** (A) Secretion of CdiA-NtAb 74-472 and expression of CdiBAb are monitored after induction (t0) up to 130 mins. Samples from culture supernatant and bacterial pellet were separated by centrifugation, analyzed by western blot, and the bands corresponding to CdiA-Nt (left) and CdiBAb variants (right) displayed. A gray dashed line at 60 min after induction indicates the reference point for the W.T where enough CdiA-Nt is present in the culture supernatant for immunoblot detection. (B), (C) Secretion activity was assessed by the levels of CdiA-NtAb 74-472 detected in culture supernatants normalized to the wildtype at t130 min (100%), repeated three times independently where error bars represent the standard error of the mean. (B), Secretion activity comparison from 20 to 130 min for CdiBAb wildtype (WT, ●), CdiB where H1 and Linker are genetically deleted (WTΔH1ΔLinker, Δ), Loop 2 substitutions GGAG (L2GGAG,♦) and single substitution variants D224G (, gray), S226G (□, light gray). (C), Secretion activity comparison from 50 to 130 min between CdiBAb wildtype (WT, ●), single substitution S226E (○), S226E without H1 and Linker (S226EΔH1ΔLinker, Δ gray), and double substitution S226E+R460G (□).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Western blot detection of GroEL and MBP from culture supernatant and bacterial pellet over 130 min after induction of CdiA-NtAb with CdiBAb wild type (A) or CdiBAb L2GGAG variant (B). Protein ladder bands indicate 180, 130, 100, 70, 55, 40, 35 and 25 kDa.

Loop 2 adopts very different conformations in our two CdiB structures. Whereas deletion of this loop prevents expression of CdiB, the 4-residue substitution of DDFH to GGAG is tolerated and does not increase cell lysis (Figure 6—figure supplement 1B). Removal of the sidechains can prevent loop 2 interaction with the rest of the protein while increasing loop 2 flexibility. The GGAG mutant results in measurable impact on the secretion, where CdiA is detected after just 30 min and continues to increase over time. This result suggests that increasing loop 2 flexibility enhances secretion activity and may promote the active conformation of the β-barrel. As a comparison, when loop 2 adopts an inward conformation in the CdiBAb X-ray structure, the sidechains point in the direction of H1 and loop 6, and the β-barrel lumen is partially capped (Figure 1, Figure 3, and Video 1).

Our structural and functional analysis reveal that β1 can be fully folded as a β-strand stabilized by β16 or adopt a more flexible extended secondary structure and be folded inward as part of loop 1. Our hypothesis is that the conserved DxxG motif can facilitate a conformational change that promotes the active conformation. To explore the role of the interaction between DxxG and the conserved loop 6 inside the β-barrel, we made point mutants in the D224-S226-R460 interaction network. Mutations to glycine do not lower the rate of CdiA secretion, indicating no essential role for these residues in producing an active CdiB conformation and/or substrate interaction (Figure 6A and B). However, the CdiBAb structure predicts that mutation of S226 to glutamate would allow formation of a salt bridge with R460, further stabilizing the DxxG-L6 network. In fact, S226E delays secretion and results in lower amounts of CdiA secreted over time. Combining S226E with R460G or with the H1-linker deletion (S226EΔH1ΔLink) improves secretion and restores CdiA levels to near wildtype (Figure 6A and C). These results show that interactions between DxxG and loop 6 affect CdiA secretion and that flexibility in this region is essential.

### Link between DxxG conformation and position of H1 helix

The main conformational differences observed between CdiBAb and CdiBEc are at the β1–β16 interface at the DxxG motif, and inside the barrel with H1. Based on structural analysis of CdiBEc, the rearrangement of loop 1 created by DxxG forms a network of interactions between loop 1, H1, and loop 6 (Q214-R10-K440-N211; Figure 1—figure supplement 1). Interestingly, in the FhaC structure, there is a similar network of interactions between β1, H1, and L6, where R17 from H1 interacts with the conserved aspartate from DxxG (Figure 3—figure supplement 1). In both CdiBEc and FhaC structures, the inward tilting of DxxG in β1 promotes the rearrangement of loop 1 and loop 2 while presenting a new interaction surface for H1. However, due to the weak sequence conservation of H1 in TpsB transporters (Supplementary file 1), it is difficult to predict whether particular residues either stabilize the helix in the barrel pore or induce its exit in the active conformation. Since the position of H1 in our CdiB structures vary, we wanted to understand whether β1–β16 and DxxG remain flexible. Using molecular dynamics, we ran three 500-ns equilibrium simulations of each CdiB structure in a species-specific outer membrane (Video 3, Figure 7—figure supplement 1; Phillips et al., 2005). Although the position of H1 remains stable in the β-barrel lumen, we observed rupture of several H-bonds between β1 and β16 in the CdiBAb simulations. Part of the DxxG motif can convert from a β-strand to a loop, whereas the β1–β16 interface can fluctuate from a short to a long β-sheet affecting the size of the β16-β1-β2-β3 sheet. During the simulations we observe that water molecules penetrate into the membrane slightly to keep the DxxG motif solvated (Figure 7—figure supplement 1C). This environment may facilitate the interconversion of secondary structure. In comparison, during CdiBEc simulations, the DxxG motif tilts inward, toward the lumen, and the CdiBEc conformation is much more stable, with no H-bond disruption detected between β1 and β16. This result shows that DxxG can exist in two different conformational states: fully folded as a β-strand or in a more flexible, extended conformation. The equilibrium simulations demonstrate that CdiBAb interconverts between the two conformations, while CdiBEc stabilizes only the unfolded conformation. However, the importance of these structural differences to CdiA secretion remains to be determined.

![Video 3.](https://cdn.elifesciences.org/articles/58100/elife-58100-video3.mp4.jpg)

**Video 3.:** 500 ns equilibrium simulations of three CdiBAb (light teal) and three CdiBEc (pale yellow) molecules. Full length CdiB proteins are inserted into their respective species-specific outer membranes (shown in Figure 7—figure supplement 1). Strands β1 and β16 are highlighted in yellow, and helix H1 in blue. The H-bonds between G227-T552 and I229-V534 are indicated for CdiBAb and CdiBEc, respectively. The POTRA domains and linker were present for the simulations but not shown in the final movies.

### Extraction of helix H1 from β-barrel lumen

To secrete substrates across the outer membrane, TpsB/CdiB transporters must cycle through multiple conformational states, from the resting conformation with H1 inserted into the β-barrel lumen, to the active form when H1 resides in the periplasm (Figure 1—figure supplement 3; Baud et al., 2014; Guérin et al., 2014). To understand these conformational changes, we induced the exit of H1 by steered molecular dynamics (SMD) to measure the force needed to extract it from the pore and observe its exit path (Video 4, Video 5; Sotomayor and Schulten, 2007). H1 was pulled in the direction of the periplasm at a constant speed of 0.29 Å/ns over 150–200 ns. In these experiments, we wanted to mimic a hypothetical periplasmic force that could cause the helix to exit the pore as might be expected when substrate is present and/or when large conformational changes in the linker and POTRA domains occur. During the simulations, H1 is free to move or rotate as force is applied to the center of mass of the helix. We tracked the position of H1 and measured the force required. We also used the SMD trajectories to seed potential of mean force (PMF) calculations to determine the free energy required to extract H1 from CdiBAb and CdiBEc β-barrels (Figure 7, Figure 7—figure supplement 2A; Sugita et al., 2000). Since the exit pathway of H1 is not known, we ran four independent simulations (two per species) to assess the role of sampling during SMD simulations and PMF calculations. In the case of CdiBAb, both independently determined PMF profiles show a continuous rise in energy as the helix is extracted from the barrel. With large energetic barriers measured at 90kcal/mol and 32kcal/mol, respectively, the exit of H1 appears to be energetically expensive (Figure 7—figure supplement 2A). Similarly, the first PMF determined for H1 extraction from CdiBEc suggests 35 kcal/mol is required to extract H1. However, the second run for CdiBEc found a significantly lower energy path on a similar time scale as the other PMF calculations (35–60 ns/window, or 1.7–2.6 μs in total) (Figure 7). Therefore, we extended this PMF calculation to 235 ns/window (10.1 μs in total). From this PMF, we discovered a new minimum, one even lower in energy than the crystal structure minimum, at a point of intermediate extraction. In this PMF, the second minimum is separated from the crystal-structure conformation by 7.5 kcal/mol and a barrier of 13 kcal/mol; the fully extracted state is 7.5 kcal/mol higher than the second minimum and almost identical to the crystal-structure conformation. The existence of an intermediate state during helix extraction from the barrel is supported by earlier experimental data where Pulsed-electron double-resonance (PELDOR) spectroscopy revealed distinct peaks in the distance distribution on a related two-partner-secretion transporter, FhaC, even in the absence of any substrate (Guérin et al., 2014). We note that for computational efficiency, the POTRA domains were not present in the PMF calculations; along with the substrate, they may shift the relative energies of the fully embedded, partially embedded, and fully extracted H1 conformations. Also, the different PMFs obtained for different starting conditions illustrates the systematic uncertainty present in these calculations when run for moderate lengths (1–2 μs in total), complicated further by the unknown end-state structure.

![Figure 7.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig7-v2.jpg)

**Figure 7.:** Plot of the potential of mean force (PMF) measured as a function of the distance between the centers-of-mass of the α-helix H1 and β-barrel of CdiBEc. Three images of CdiBEc have been added to the plot representing different states, from the left to right: resting conformation, intermediate extraction, and H1 out of the pore.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) CdiBAb was inserted into a bilayer that mimics the A. baumannii outer membrane. The outer leaflet is composed of type 1 and type 2 Lipid A with a ratio of 1:1 and the R1 core. (B) CdiBEc was inserted into an asymmetric bilayer that mimics the E. coli outer membrane. The outer leaflet is composed of type1 Lipid A with the R1 core. The inner leaflets of both membranes are composed of PPPE, PVPG and PVCL with a ratio of 15:4:1. The protein-membrane systems are surrounded by TIP3P water. The system size for the E. coli simulation is 110 × 115×125 Å3 and ~170,000 atoms, while the system size for the A. baumannii simulation is 115 × 125×125 Å3 and ~200,000 atoms. (C) Zoomed-in view of the DxxG motif from CdiBAb inserted into the outer membrane bilayer. Water molecules (in red and white) penetrate into the membrane to keep DxxG solvated.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** (A) Plots of the results of four independent PMF calculations measured as a function of the distance between helix H1 and β-barrel of CdiBEc (top panels) and CdiBAb (lower panels). Statistical error (+ / - 1 standard deviation) is represented as a red dashed line. CdiBEc run two is also presented in Figure 7. (B) Force vs. position plots of the steered molecular dynamics simulations for H1 extraction from CdiBEc and CdiBAb structures (wt), from CdiBAb where Loop 2 is in-silico deleted (Ab ΔL2), and from CdiBAb double cysteine variants (Ab β1–β16). For each system, three independent replicas are presented (blue, orange, green). The main differences observed between the CdiBAb replicas is due to the formation of an ion-bridged interaction between H1 and D224 (DxxG) and D261 (loop 2). D261 is removed in the ΔL2 mutant, although we still see an ion-bridged interaction between H1 and E469 (loop 6) in one out of the three trajectories.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/58100/elife-58100-fig7-figsupp3-v2.jpg)

**Figure 7—figure supplement 3.:** Left and middle images are taken from CdiBAb WT trajectories and show interactions between E4 and D224 (DxxG) and E4 and D261 (loop 2), respectively. The image on the right is taken from simulation of CdiBAb ΔL2 and shows an interaction between E4 and E469 (loop 6).

![Video 4.](https://cdn.elifesciences.org/articles/58100/elife-58100-video4.mp4.jpg)

**Video 4.:** SMD simulations of CdiBAb (light teal) where helix H1 is pulled toward the direction of the periplasm at a constant speed (0.29 Å/ns).

![Video 5.](https://cdn.elifesciences.org/articles/58100/elife-58100-video5.mp4.jpg)

**Video 5.:** SMD simulations of CdiBEc (pale yellow) where helix H1 is pulled toward the direction of the periplasm at a constant speed (0.29 Å/ns).

To better understand the exit pathway and investigate any conformational differences between CdiBAb and CdiBEc, we ran several additional SMD simulations. Using the X-ray structures as an initial model, we pulled the H1 helix to the periplasm and quantified the force as a function of the position during extraction for three replicas (Figure 7—figure supplement 2B). The force plots for CdiBEc and CdiBAb display distinct features, while on average CdiBEc requires less work to extract H1, especially from −25 to −35 Å. Upon further examination, we observed a strong electrostatic interaction between H1 and the DxxG motif or loop 2 in CdiBAb that require a large force to disrupt (Figure 7—figure supplement 3). This ion-bridged interaction is not observed for CdiBEc, probably because loop 2 is oriented outward and does not interact with H1. Based on the CdiBAb functional data (Figure 5, Figure 6) we built and simulated two CdiBAb mutants. The force plot of CdiBAb in which loop 2 is deleted shows that less force is required to extract H1 on average. In comparison, the force plots from the disulfide-bonded β1–β16 mutant display features similar to the wildtype CdiBAb, with multiple peaks observed in the −10 to −35 Å range (Figure 7—figure supplement 2B). These results show that by stabilizing H1 in the barrel lumen through electrostatic interactions, some structural elements (such as loop 2 and the DxxG motif) influence the energetic barrier needed to open the β-barrel pore.

Altogether our simulations indicate that the exit of H1 must follow a pathway inside the β-barrel lumen to be correctly extracted. As an alternative, conformational changes from the β-barrel itselft (rearrangement of extracellular loops, flexibility of DxxG motif) decrease the energy required to eject H1 while probably preparing the active conformation.

## Discussion

By releasing large exoproteins at the surface of the cell, type Vb secretion systems play an essential role in pathogenesis and survival of Gram-negative bacteria. Genome databases have reported hundreds of TpsA proteins that come in different sizes and domain organizations, where CdiA toxins represent a special subgroup. An increasing number of studies have reported multifunctional roles for CdiA proteins, apparently independent of toxin activity. CdiA promotes adhesion on epithelial cells in A. baumannii, plays a major role in intracellular survival and intracellular escape in Neisseria meningitidis, increases the virulence of Pseudomonas aeruginosa in infection models, and controls biofilm establishment in human pathogens (Melvin et al., 2017; Mercy et al., 2016; Pérez et al., 2016; Roussin et al., 2019; Talà et al., 2008). Both CDI systems investigated in our study have been shown to be constitutively active, and a secretome analysis of Acinetobacter spp. revealed that CdiA is one of the most abundantly secreted proteins (Aoki et al., 2005; Harding et al., 2017).

During the secretion cycle, the TpsB β-barrel must adopt multiple conformational states favoring ejection of the N-terminal helix H1, entry and movement of substrate into the β-barrel lumen, folding of substrate in the extracellular space and then re-entry of H1 into the lumen. All steps happen in an environment where no hydrolysable energy or electrochemical gradient sources are available to power conformational changes. The limited space inside the β-barrel lumen and the multiple tertiary interactions with H1 increase the energetic barrier needed to eject the internal α-helix. As a result, additional conformational changes are likely required to obtain the active conformation, such as potential rearrangement of the β-barrel itself. These changes may be induced by the presence of the substrate CdiA, the binding of which to the POTRA domains could provide the additional 7.5 kcal/mol necessary to fully extract the helix (Figure 7).

The flexibility of the β1–β16 interface mediated by the DxxG motif plays an essential role in the transport mechanism, where conformational changes in loop 1 display different interacting surfaces for H1 and possibly for the toxin substrate. At the β1–β16 interface, sidechains from the conserved loop 6 interact with the DxxG motif, helping to stabilize different conformations. Our structures also reveal two different conformations for loop 2 that affect CdiA secretion and H1 ejection. Similar results have been observed for FhaC, where deletion of this loop does not affect the active conformation, whereas insertion of several residues reduces the channel conductance and prevents substrate secretion (Baud et al., 2014; Méli et al., 2006). These results suggest a common and conserved role of loop 2 in the TpsB transporter family, where the inward state can stabilize the resting conformation, and the outward state facilitate the active conformation.

H1 and the DxxG motif are both present in CdiB/TpsB transporters, but absent in BamA/TamA proteins. We hypothesize that they contribute to unidirectional secretion where the lumen of the β-barrel is accessible or inaccessible at different stages of the secretion cycle. The position of loop 6 and interactions with β13 are conserved in all Omp85 proteins, suggesting a common function. In addition to possibly interacting with the substrate upon entering the β-barrel lumen, our results suggest that loop 6 can also stabilize different conformational states of the β-barrel at the β1–β16 interface.

## Materials and methods

### Cloning and purification of CdiB proteins

cdiBAb from A. baumannii strain ACICU (locus tag ACICU_01912, protein id WP_000956371) and cdiBEc from E. coli strain EC93 (locus DQ100454, protein id AAZ57197.1) were codon-optimized, synthesized (Genscript) and cloned using ligation- independent cloning into pET9 vector, a derivative of pET20b (EMD Millipore). Signal sequence positions 1–23 for CdiBAb and 1–52 for CdiBEc were replaced by the pelB signal sequence followed by a 10-Histidine tag and a TEV site (ENLYFQSM) added to the N-terminus of mature proteins. Expression was performed in BL21(DE3) cells in 12 liters of TB media supplemented with 25 μg/mL kanamycin during 3 days at 20°C without induction (leaky expression of pET9 vector). Cells were collected by centrifugation (7500 g for 15 min), and resuspended in lysis buffer (50 mM Tris-HCl, pH7.4, 200 mM NaCl, 1 mM MgCl2, 10 mg/mL DNase I, and 100 mg/mL 4-(2-aminoethyl)benzenesulphonyl fluoride (AEBSF)). Cells were broken by three passages through an Emulsiflex C3 (Avestin) homogenizer at 4°C, and unlysed cells removed by centrifugation (7500 g for 15 min). The membrane fraction was harvested by ultracentrifugation (160,000 g for 60 min), and the pellet was resuspended in 50 mM Tris-HCl, pH7.4, 200 mM NaCl, 20 mM imidazole and solubilized by constant stirring in 5% Elugent (EMD Millipore) for 16 hr at 4°C. Solubilized membranes were harvested by a second ultracentrifugation step (220,000 g for 60 min) and the supernatant containing CdiB proteins was applied to a 15 mL Ni-NTA column (Qiagen) and eluted with 50 mM Tris-HCl, pH7.4, 200 mM NaCl, 0.8% Elugent and 250 mM imidazole. To remove the N-terminal 10-His Tag, peak fractions were pooled and incubated with 2 mg of TEV protease, in the presence of 2 mM DTT and 1 mM EDTA at 4°C under gentle agitation for 12 hr. The mixture was diluted into 50 mM Tris-HCl, pH8, 0.8% elugent and applied to an anion exchange chromatography column (Q sepharose GE Healthcare) for detergent exchange, eluted using a NaCl gradient into 50 mM Tris-HCl, pH8, and 1% C8E4 (Anatrace). To remove uncleaved protein from the TEV digestion, the peak fractions from ion-exchange were applied to a second Ni-NTA purification on gravity column using 2 mL of resin. The flow through containing TEV-digested CdiB proteins was concentrated to 4 mL and applied to a HiLoad 16/600 Superdex 200 size exclusion column (GE Healthcare) using 25 mM NaPi pH6.6, 100 mM NaCl, 1% C8E4. For Selenomethionine-substituted CdiBAb proteins, expression was performed in B834 E. coli cells (Novagen). Cultures were started in 12 L of TB media, then when OD600 reached 0.8, cells were harvested and washed two times in SelenoMet minimal media (Molecular Dimensions) supplemented with L-methionine at 60 mg/L. The final round was resuspended in 1 liter of SelenoMet media to inoculate 12 liters of SelenoMet supplemented with L-methionine at 60 mg.L−1 and 50 µg.mL−1 kanamycin. When OD600 reached 0.7, SeMet derivatized CdiBAb proteins were induced by addition of 1 mM Isopropyl‐thio β‐D‐1‐thiogalactopyranoside (IPTG) and grown 16 hr at 30°C. The final OD600 was ~2.5, cells were harvested by centrifugation and CdiB proteins purified as described above. The incorporation of selenium into CdiBAb proteins was analyzed by mass spectrometry (data not shown; Taplin – Harvard).

### Crystallization and data collection

For crystallization, samples were concentrated to ~10 mg/mL and sparse matrix screening was performed using a TTP Labtech Mosquito crystallization robot using hanging drop vapor diffusion with plates incubated at 21°C. The best native crystals for CdiBAb were grown from 100 mM Tris-HCl pH 8.4, 200 mM lithium sulfate, 10% PEG400, and 23% ethylene glycol. Selenomethionine-substituted crystals of CdiBAb were crystallized using similar conditions to native: 100 mM Tris-HCl pH 8, 200 mM lithium sulfate, 11% PEG400, and 23% ethylene glycol. The best crystals for CdiBEc were grown from Morpheus II condition C10 (Molecular Dimensions): 100 mM Gly-Gly, AMPD pH8.5, 4 mM Alkalis (1 mM Rubidium chloride, 1 mM Strontium acetate, 1 mM Cesium acetate, 1 mM Barium acetate), 12.5% PEG4000% and 20% 1,2,6-Hexanetriol. Crystals were collected directly from the crystallization drops and native data were collected at SER-CAT (ID22) and the GM/CA-CAT (ID23-D) beamlines of the Advanced Photon Source of the Argonne National Laboratory. Data collection for selenium-single-wavelength anomalous dispersion (Se-SAD) phasing of CdiBAb was performed at the BL12-2 beamline of the Stanford Synchrotron Radiation Lightsource from the SLAC National Accelerator Laboratory, during the Rapidata practical course. A summary of the data collection statistics can be found in Table 1.

### Structure determination

Molecular replacement on CdiBAb native data using the FhaC structures (PDB 4QKY and 3NJT) was unsuccessful. We phased the CdiBAb structure by collecting one data set on selenomethionine substituted CdiBAb crystal at the wavelength 0.979 Å. The data were processed in space group P1 to a final resolution of 2.6 Å and selenium sites located using SHELX (Sheldrick, 2010). A phase-extended density-modified electron density map was produced with AutoSol (PHENIX) (Adams et al., 2010) and used for iterative model building (COOT [Emsley and Cowtan, 2004]) and refinement (PHENIX). This model was then used as a search model to solve the selenomethionine derivative CdiBAb and native CdiBEc structures by molecular replacement using Phaser-MR (Adams et al., 2010). The CdiBAb structure was refined in space group P1 to 2.4 Å resolution with R/Rfree values of 0.20/0.25 and CdiBEc in space group P21212 to 2.6 Å resolution with R/Rfree values of 0.24/0.26. Figures were made with UCSF Chimera (Pettersen et al., 2004).

Coordinates and structure factors for the CdiBAb and CdiBEc structures have been deposited in the Protein Data Bank (PDB accession codes 6WIL and 6WIM).

### Sequence alignments

Starting after the predicted signal sequence, sequence alignments included representative Type Vb transporters where eight are involved in the CDI mechanism (6 CdiB: WP_000956371, AAZ57197.1, WP_046042815, ACI07001.1, WP_002210394.1, NP_273542, WP_126867950. 2 BcpB: WP_011402463, WP_011851264) and nine representative TpsB transporters, not involved in the CDI mechanism (WP_010930614, VDH07240, BAA21096, WP_136264517, AAA50322, AAA87060.1, AAX13508.1, WP_011191836, WP_010895677). Alignments were performed with T-coffee (Notredame et al., 2000) and edited with Jalview (Waterhouse et al., 2009) to take into consideration the secondary structure from available structural data. The final result was presented with ESPript (Robert and Gouet, 2014). Sequence identity percentage was calculated using Blastp suite (NCBI).

### Secretion assays

To test secretion activity, two plasmids were used to co-produce CdiB and CdiA-NT proteins in E. coli C41 (DE3) cells. cdiB genes were cloned into the pBAD plasmid under the control of the arabinose promoter, where the signal sequences (1–23 for CdiBAb and 1–52 for CdiBEc) were replaced by a pelB signal sequence, and 6-Histidine tags inserted into extracellular loop7 (located between residues 510–511 for CdiAAb, and between residues 486–487 for CdiAAc). The 5’ region of cdiA genes from the related CDI operons was codon-optimized and synthesized (Genscript) to produce region 74–472 for CdiAAb (WP_001039234.1) and region 29–460 for CdiAEc (AAZ57198.1) containing the TPS domain and part of the FHA-1 domain. cdiA-NT genes were cloned into a pCDF plasmid under the control of a T7 promoter with lac operator, and the native signal sequence (1–73 and 1–28) was replaced by the pelB signal sequence, and a 6-Histidine tag added at the C-termini of the proteins. Cloning and CdiB deletion variants (denoted Δ in the text) were engineered using the Gibson assembly method (NEB) and amino acids substituted using Q5 Site-Directed Mutagenesis (NEB). α-helix H1 deletion constructs were built by removing the first 26 (IEDVSLPSQVLQDQRLKELNQQLQDQ) and 29 (AMLSPGDRSAIQQQQQQLLDENQRQRDAL) N-terminal residues from CdiBAb and CdiBEc, respectively. Constructs with α-helix H1 and linker deleted start at the first conserved cysteine indicated in Supplementary file 1 (end of the linker). For secretion assay E. coli C41(DE3) cells were co-transformed using pBAD-cdiB and pCDF-cdiA-NT constructs and selected with 25 μg/mL kanamycin and 20 μg/mL streptomycin on LB (LB K/S). Cultures for secretion assays were incubated by shaking at 37°C 20 mL culture LB K/S in 125 mL flasks. When cultures reached OD600 = 0.8, 0.1% arabinose and 400 μM IPTG were added for exactly 2h30 min and standardized at the end of the induction period using the final OD600, 100 μL containing 4 × 107 bacteria were harvested by centrifugation at 7000 g for 10 min. For kinetic experiments, 0.1% arabinose and 400 μM IPTG are added at OD600 = 0.8 (t0), then after 20 min every 10 mins (for 100–130 mins) 100 μL from each culture were harvested by centrifugation to separate culture supernatant and bacterial pellet at 7000 g for 10 min. For double cysteine variants, 5 mM TCEP was added during the induction period (TCEP ‘+’). 1X SDS-loading buffer was added into the culture supernatants and heated at 95°C. The whole cells (pellet) were washed and resuspended in 100 μL of 50 mM Tris-HCl pH7.4, 200 mM NaCl 1X SDS-loading buffer, heated at 95°C for 10 min at 1400 rpm shaking. 10 μL fractions from supernatant and whole cells were analyzed on NuPAGE 4–12% gels (Invitrogen) with 1X MES SDS-PAGE running buffer for 35 min at 200 V (constant) and transferred to polyvinylidenedifluoride (PVDF) membrane via the iBlot system (Invitrogen). Anti-HIS-HRP, Anti-GroEL, Anti-mouse and rabbit IgG-HRP (Sigma) and Anti-MBP (NEB) antibodies were used for western blot analysis and imaged using an ImageQuant LAS 4000 imaging system (GE Healthcare). The respective amounts, and estimation of the secretion efficiency were determined by scanning densitometry of the CdiA-NT and CdiB protein bands using the ImageQuantTL software (GE Healthcare). For kinetic experiments, the secretion efficiency of CdiA-NT wild type is arbitrarily set to 100% at t130 min and compared with the secretion efficiency of CdiA-NT variants. For the DsbA experiment, MC4100 dsbA+ parent cells and MC4100 dsbA- cells (dsbA::cm) were transformed using pBAD-cdiBAb D225C/F554C. All experiments were independently repeated at least three times from fresh transformations, and data were analyzed and presented using Prism 8 (GraphPad).

### Equilibration Molecular dynamics (MD) simulations

CHARMM-GUI membrane builder (Jo et al., 2008; Wu et al., 2014) was used to generate simulation systems. One copy of CdiB from E. coli or A. baumannii (referred to as CdiBEc or CdiBAb, respectively) was inserted into its respective species-specific outer membrane. The outer leaflet of the E. coli membrane was composed of type 1 Lipid A and R1 core (Wu et al., 2013). The outer leaflet of the A. baumannii membrane was composed of type 1 and type 2 Lipid A in a 1:1 ratio and R1 core (Fregolino et al., 2010). The inner leaflets of both membranes were composed of PPPE, PVPG and PVCL with a ratio of 15:4:1 (Vance and Vance, 2002). All systems were solvated with TIP3P water (Jorgensen et al., 1983). The E. coli system size is 110 × 115×125 Å3 and ~170000 atoms, while the A. baumannii system size is 115 × 125×125 Å3 and ~200000 atoms. Visual Molecular Dynamics (VMD) was used to construct both systems (Humphrey et al., 1996). We ran six equilibrium simulations, three for CdiBAb and three for CdiBEc, with NAMD for 500 ns each (Phillips et al., 2005). The lipid placement was the same for each replica. The force field used for all simulations is CHARMM36m (Huang et al., 2017). Langevin dynamics (damping constant ɣ = 1.0 ps−1) was used to keep the temperature (310 K = 37°C) constant and an anisotropic Langevin piston barostat was adopted for constant pressure (one atm) (Martyna et al., 1994). The time step of the simulations is two fs. Bonded interactions and short-range (below the 12 Å cutoff) nonbonded interactions were updated at every time step. The Particle-mesh Ewald (PME) method (Darden et al., 1993) was used for long-range interactions, calculated every other time step.

The potential of mean force (PMF) for extraction of the helix H1 from CdiBAb and CdiBEc β-barrels was calculated using replica-exchange umbrella sampling (REUS) (Sugita et al., 2000) and the weighted histogram analysis method (WHAM) (Grossfield, 2017; Kumar et al., 1992). A collective variable defining the distance between the Cɑ atoms of the helix and those of the barrel projected onto the membrane axis was constructed using the colvars module of NAMD (Fiorin et al., 2013). Steered molecular dynamics (SMD) (Sotomayor and Schulten, 2007) was used to generate starting states for each window. A total of 43–50 windows were used, covering a range from +2 to −40 Å (positive values are on the extracellular side and negative values on the periplasmic side compared to the crystal structure at 0 Å). For the four PMF calculations (two for CdiBAb and two for CdiBEc), we ran 35–235 ns/window (1.7–10.1 μs per PMF). Exchange rates between the windows were between 0.1 and 0.5. A particularly difficult region to sample was around −4 to −12 Å for CdiBAb. To improve sampling in this region, we ran 16 additional windows, spaced every 0.5 Å, with a larger restraint for 10 ns each. While these windows helped with WHAM, it should be noted that they do not benefit from accelerated convergence intrinsic to REUS. Bootstrap error estimates were calculated using WHAM. Correlation times for each window, a necessary input for the error estimate, were determined from the integral of the normalized autocorrelation function (ACF), cut-off at the first time it reaches 0. These ACFs were determined using ACFCalculator (Gaalswyk et al., 2016) with inputs from additional 2-ns highly restrained (force constant of 10 kcal/mol⋅Å2) simulations. The correlation time ranged from 20 ps to 140 ps and were smoothed using a three-point running average (Hub et al., 2010). PMFs are plotted in Figure 7—figure supplement 2 with + / - 1 standard deviation.

To quantify H1’s removal from the CdiB β-barrel, we ran SMD simulations. Because interactions with the linker region and POTRA domains are unpredictable in a non-equilibrium simulation, we deleted them prior to running SMD for both CdiBAb and CdiBEc. In the SMD simulations, force was applied to the center of mass of H1 and its secondary structure was restrained to obtain the force profile of extraction under the assumption that H1 maintains its α-helical structure. H1 was pulled toward the periplasm at a constant speed (0.29 Å/ns) in all SMD simulations, which were 150–200 ns in length. Loop 2 (Leu260 to Ser266) was deleted in the ‘ΔL2’ system. Gly227 (β1) and Thr552 (β16) were substituted by cysteines to form a disulfide bond in the ‘β1–β16’ system. Three SMD replicas were run for each of these CdiBAb variants at the same speed and length as for the WT systems.

To explore the different positions of H1 observed in each species’ β-barrel, Targeted Molecular Dynamic (TMD) simulations were run. In the first TMD simulation starting from the crystal structure of CdiBAb, H1 was forced to adopt the same position relative to the β-barrel as that of CdiBEc H1. In the second TMD simulation, the same procedure was applied to CdiBEc, matching its H1 to the position of that in the CdiBAb structure. TMD was run for 30 ns, followed by 30 ns in which H1 was restrained to its new position, and finally 120 ns of free equilibration.
