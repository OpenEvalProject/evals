# Structural and thermodynamic analyses of the β-to-α transformation in RfaH reveal principles of fold-switching proteins

## Authors

- Philipp K Zuber<sup>1</sup> ([ORCID: 0000-0001-5139-3930](https://orcid.org/0000-0001-5139-3930))
- Tina Daviter<sup>2</sup> ([ORCID: 0000-0003-2636-5959](https://orcid.org/0000-0003-2636-5959))
- Ramona Heißmann<sup>1</sup>
- Ulrike Persau<sup>1</sup>
- Kristian Schweimer<sup>1</sup> ([ORCID: 0000-0002-3837-8442](https://orcid.org/0000-0002-3837-8442))
- Stefan H Knauer<sup>1</sup> ([ORCID: 0000-0002-4143-0694](https://orcid.org/0000-0002-4143-0694)) †

### Affiliations

1. Biochemistry IV – Biophysical Chemistry, University of Bayreuth Bayreuth Germany ([ROR:0234wmv40](https://ror.org/0234wmv40))
2. Birkbeck, University of London, Malet Street, Bloomsbury London United Kingdom ([ROR:04cw6st05](https://ror.org/04cw6st05))

† Corresponding author

## Abstract

The two-domain protein RfaH, a paralog of the universally conserved NusG/Spt5 transcription factors, is regulated by autoinhibition coupled to the reversible conformational switch of its 60-residue C-terminal Kyrpides, Ouzounis, Woese (KOW) domain between an α-hairpin and a β-barrel. In contrast, NusG/Spt5-KOW domains only occur in the β-barrel state. To understand the principles underlying the drastic fold switch in RfaH, we elucidated the thermodynamic stability and the structural dynamics of two RfaH- and four NusG/Spt5-KOW domains by combining biophysical and structural biology methods. We find that the RfaH-KOW β-barrel is thermodynamically less stable than that of most NusG/Spt5-KOWs and we show that it is in equilibrium with a globally unfolded species, which, strikingly, contains two helical regions that prime the transition toward the α-hairpin. Our results suggest that transiently structured elements in the unfolded conformation might drive the global folding transition in metamorphic proteins in general.

## Introduction

Fundamental understanding of how proteins fold has ever been one of the most important questions in structural biology and it is still not answered, despite recent progress in protein structure prediction (Jumper et al., 2021; Tunyasuvunakool et al., 2021). Since the formulation of the ‘thermodynamic hypothesis of protein folding’ by Anfinsen (Epstein et al., 1963), it has been generally accepted that the amino acid sequence of a protein determines its three-dimensional structure and that a protein adopts only a single folded conformation, which is referred to as physiological state and which corresponds to its global energy minimum. This conformation, in turn, fulfills one distinct function. While this ‘one sequence–one structure–one function’ dogma holds true for most well-folded (globular) proteins, it has been challenged by several discoveries over the past decades. Among those are, for instance, (i) moonlighting proteins, which fulfill two completely unrelated functions (Jeffery, 2014; Jeffery, 1999), (ii) intrinsically disordered proteins (IDPs), which do not adopt a defined secondary or tertiary structure at all, but sample an ensemble of sterically allowed conformations instead (van der Lee et al., 2014), and (iii), most strikingly, metamorphic proteins (also referred to as fold-switching proteins), which can reversibly interconvert between at least two well-defined conformations, sometimes in response to a molecular signal (Murzin, 2008).

The free energy landscape of globular, well-folded proteins is often portrayed as a rugged funnel, with the ‘rim’ corresponding to the multitude of random coil structures of the ‘unfolded state’ (U state) and the deepest point (global minimum in Gibbs free energy, G), representing the ‘native’ or ‘physiological’ state (N state). IDPs, in contrast, exhibit a rather flat energy landscape and no specific conformation is favored, that is, significantly populated. Fold-switching proteins are thought to reside in-between these two scenarios, i.e. their energy landscape may be funnel-like, but it shows at least two major minima, each representing a distinct, well-folded conformation. The various conformations of a fold-switching protein may differ in the following aspects: (i) the type of secondary structure (α-helices, β-strands, turns, random coil), (ii) the extent of secondary structure elements, and (iii) the tertiary structure, usually in combination with (i) and/or (ii) (Dishman and Volkman, 2018; Kim and Porter, 2021). Additionally, these states often exhibit different quaternary structures, for example, monomeric in one state versus multimeric in another state.

A particularly intriguing example of fold-switching proteins is the transcription factor RfaH from Escherichia coli (EcRfaH), a member of the universally conserved family of NusG (bacteria)/Spt5 (archaea and eukaryotes) proteins (Werner, 2012). NusG/Spt5 proteins exhibit a modular structure with several domains. Bacterial NusG consists of at least an N-terminal domain and a C-terminal Kyrpides, Ouzounis, Woese (KOW) domain connected by a flexible linker (Werner, 2012). Spt5 proteins contain a NusG-like N-terminal (NGN) domain and one (archaea) or several (eukaryotes) KOW domains (Werner, 2012). All structurally characterized NusG/Spt5-KOW domains adopt a five-stranded β-barrel structure (Figure 1A; see e.g. Klein et al., 2011; Meyer et al., 2015; Mooney et al., 2009; Zuber et al., 2018).

![Figure 1.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig1-v2.jpg)

**Figure 1.:** (A) Cartoon representation of EcRfaH in the closed, autoinhibited state (left; protein data bank identifier (PDB-ID): 5OND) and in the open, active conformation (right; PDB-ID all-β EcRfaH-KOW: 2LCL) as well as of EcNusG-KOW (boxed; PDB-ID: 2JVV). Unstructured regions are shown as dashed lines, termini are labeled. (B) Secondary structures of EcRfaH-KOW in the all-α and the all-β state. Tubes indicate α-helical elements, arrows represent β-strands. The amino acid sequence is shown above. (C) Secondary chemical shift of VcRfaH. The plots show the difference between the observed chemical shift and the corresponding predicted random coil value of 13Cα (top) and 13CO (bottom). Positive values indicate helical, negative values elongated (β-sheet) structures, and values close to zero are observed for random coil-like structures. The secondary structure elements inferred from the analysis are shown above the graphs (code for secondary structure elements as in (B)). The position of the identified disulfide bridge (see also Figure 1—figure supplement 1A, B) is indicated. (D) Left: Ribbon representation of the 20 lowest energy structures of VcRfaH-KOW (PDB-ID: 6TF4). Right: Cartoon representation of the lowest energy structure. β-Strands and termini are labeled.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Strips of the HNCACB experiment corresponding to VcRfaH residues C34 and C102, respectively. Signals arising from the cystein’s Cα and Cβ carbons (indicative of a cysteine in a disulfide bridge) are labeled. (B) [1H, 15N]-HSQC spectra of [2H, 13C, 15N]-VcRfaH in the absence (black) or presence (red) of 20 mM DTT. Signals of the two disulfide bridge forming residues, C34 and C102, and their sequential neighbors are labeled. (C) Refolding of VcRfaH under reducing conditions. [1H, 15N]-heteronuclear single quantum coherence (HSQC) spectra of 150 µM 15N-VcRfaH (black), 39 µM 15N-VcRfaH after incubation in the presence of 8 M urea for 24 hr (red), and 40 µM 15N-VcRfaH upon refolding (cyan).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Structure-based sequence alignment of the KOW constructs used in this study. Highly conserved residues are highlighted in green, residues that differ among NusG-KOW/Spt5-KOW and RfaH-KOW domains are colored red. (B) Structures of the six KOW domains shown in cartoon representation. N- and C-termini are labeled. PDB-IDs: 2JVV (EcNusG-KOW), 2MI6 (MtNusG-KOW), 4ZN3 (MjSpt5-KOW), 2E70 (hSpt5-KOW5), 2LCL (EcRfaH-KOW), 6TF4 (VcRfaH-KOW). (C) Structural alignment of the six KOW domains. The proteins are shown as ribbons. Orientation and colors as in (B).

EcRfaH is an operon-specific paralog of E. coli NusG (EcNusG) and – just like EcNusG – consists of an NGN domain that is loosely connected to a KOW domain via a flexible 15 amino acid long linker. However, in free EcRfaH EcRfaH-KOW folds as an α-helical hairpin (all-α state) that interacts with the EcRfaH-NGN domain. Thus, the binding site for RNA polymerase (RNAP) at the domain interface on EcRfaH-NGN is masked and EcRfaH is locked in an autoinhibited state (Belogurov et al., 2007). Upon recruitment to a transcription elongation complex pausing at an operon polarity suppressor (ops) site, EcRfaH is activated (Artsimovitch and Landick, 2002; Zuber et al., 2019): the domains dissociate and the liberated EcRfaH-KOW refolds into a NusG-KOW-like β-barrel (all-β state; Figure 1A and B; Burmann et al., 2012; Zuber et al., 2019).

The refolding occurs spontaneously as soon as the domains are separated and EcRfaH-KOW, when produced as an isolated domain, also adopts the all-β state, implying that the all-α fold is only stable in the presence of EcRfaH-NGN (Burmann et al., 2012; Tomar et al., 2013). Each of the EcRfaH-KOW states has a specific function: the all-α state prevents off-target recruitment of EcRfaH and competition with the general transcription factor NusG (Belogurov et al., 2007), whereas the all-β EcRfaH-KOW serves as recruitment platform for ribosomes to activate translation (Burmann et al., 2012; Zuber et al., 2019). Upon release from RNAP EcRfaH is transformed back into its autoinhibited state, that is, the structural switch of EcRfaH-KOW is fully reversible (Zuber et al., 2019). EcRfaH was not only considered a fold-switching protein, but termed a ‘transformer protein’ to emphasize, that a complete domain cycles reversibly between two states with radically different stable secondary/tertiary structure and with each state performing a distinct function (Knauer et al., 2012).

The fine-tuned mechanism used by EcRfaH to control its functions may be widespread in nature (Porter and Looger, 2018) and a recent study predicts that 24% of the bacterial NusG family members might exhibit similar reversible α-to-β transitions (Porter et al., 2022). However, the molecular principles underlying the fold-switching process are only poorly understood. Here, we present a comprehensive thermodynamic and structural analysis of six KOW domains from NusG/Spt5/RfaH proteins from all domains of life. We combine circular dichroism (CD) spectroscopy, differential scanning calorimetry (DSC), and solution-state nuclear magnetic resonance (NMR) spectroscopy to gain insight into the mechanism and the dynamics of fold-switching within the RfaH family on a molecular level and provide a rationale for the mechanism of fold-switching proteins in general.

## Results

### Evolutionary conservation of fold-switching within the RfaH family

To date, three-dimensional structures and comprehensive evidence for fold-switching are available only for EcRfaH (Belogurov et al., 2007; Burmann et al., 2012; Zuber et al., 2019), although other RfaH orthologs seem to employ a similar mechanism to carry out their function (Carter et al., 2004; Porter et al., 2022). Thus, we first asked whether this ability might be a general feature of RfaH proteins. We chose RfaH from Vibrio cholerae (VcRfaH) for a structural analysis by solution-state NMR spectroscopy as it is evolutionarily remote from EcRfaH (sequence identity Ec/VcRfaH: 43.6% [full-length] or 35.8% [KOW domain], respectively). We first identified the secondary structure elements of the full-length protein by performing an NMR backbone assignment and calculating the secondary chemical shift for each 13Cα and 13CO atom, which depends on the main chain geometry (Figure 1C). In full-length VcRfaH, the KOW domain exhibits two stretches with helical structure that are separated by about four residues and the overall pattern of secondary structure elements perfectly matches the one of autoinhibited EcRfaH (Burmann et al., 2012), suggesting similar tertiary structures for EcRfaH and VcRfaH (compare Figure 1A), but with helix α3* being 1.5 turns longer in VcRfaH. Interestingly, the Cα and Cβ atoms of C34 and C102 exhibit chemical shifts typical for cystines (Sharma and Rajarathnam, 2000, Figure 1—figure supplement 1A). These residues are located at the end of helix α3* and in strand β3*, respectively, and are, most probably, in close proximity, as indicated by the structure of EcRfaH. The addition of a reducing agent to [2H, 15N, 13C]-VcRfaH led to drastic changes of the chemical shifts of C34 and C102 as well as residues in spatial proximity in a [1H, 15N]-heteronuclear single quantum coherence (HSQC) spectrum (Figure 1—figure supplement 1B). From this we conclude that C34 and C102 form a disulfide bridge, that covalently tethers the α3*-helix to the core of VcRfaH-NGN, a feature absent in EcRfaH. However, upon refolding from a solution containing 8 M urea and reducing agent, 15N-VcRfaH adopted the same conformation as before denaturation (Figure 1—figure supplement 1C), suggesting that the disulfide bridge is not required for VcRfaH to fold into the autoinhibited state.

Next, we determined the solution structure of the isolated VcRfaH-KOW domain by NMR spectroscopy. VcRfaH-KOW also shows the five-stranded β-barrel topology typical for NusG/Spt5-KOW domains (Figure 1D and Table 1), with a Cα root mean square deviation (rmsd) of 1.4 Å as compared to isolated EcRfaH-KOW.

**Table 1.**
 Solution structure statistics for VcRfaH-KOW.


<table>
  <thead>
    <tr>
      <th>Experimental derived restraints</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Distance restraints</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>NOEs unique (total)</td>
      <td>630 (734)</td>
    </tr>
    <tr>
      <td></td>
      <td>Intraresidual</td>
      <td>59</td>
    </tr>
    <tr>
      <td></td>
      <td>Sequential</td>
      <td>187</td>
    </tr>
    <tr>
      <td></td>
      <td>Medium range</td>
      <td>89</td>
    </tr>
    <tr>
      <td></td>
      <td>Long range</td>
      <td>295</td>
    </tr>
    <tr>
      <td></td>
      <td>Hydrogen bonds</td>
      <td>2 · 18</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Dihedral restraints</td>
      <td></td>
      <td>76</td>
    </tr>
    <tr>
      <td>Restraint violation</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Average distance restraint violation (Å)</td>
      <td></td>
      <td>0.002584±0.000700</td>
    </tr>
    <tr>
      <td>Maximum distance restraint violation (Å)</td>
      <td></td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>Average dihedral restraint violation (°)</td>
      <td></td>
      <td>0.0654±0.0265</td>
    </tr>
    <tr>
      <td>Maximum dihedral restraint violation (°)</td>
      <td></td>
      <td>0.71</td>
    </tr>
    <tr>
      <td>Deviation from ideal geometry</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bond length (Å)</td>
      <td></td>
      <td>0.000544±0.000039</td>
    </tr>
    <tr>
      <td>Bond angle (Å)</td>
      <td></td>
      <td>0.1096±0.0056</td>
    </tr>
    <tr>
      <td>Coordinate precision*,†</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Backbone heavy atoms (Å)</td>
      <td></td>
      <td>0.32</td>
    </tr>
    <tr>
      <td>All heavy atoms (Å)</td>
      <td></td>
      <td>0.90</td>
    </tr>
    <tr>
      <td>Ramachandran plot statistics‡ (%)</td>
      <td></td>
      <td>91.8/7.9/0.2/0.1</td>
    </tr>
  </tbody>
</table>

_*The precision of the coordinates is defined as the average atomic root mean square difference between the accepted simulated annealing structures and the corresponding mean structure calculated for the given sequence region.†Calculated for residues 116–165.‡Ramachandran plot statistics are determined by PROCHECK and noted by most favored/ additionally allowed/generously allowed/disallowed._

Although we do not present functional data on VcRfaH here, these results strongly suggest that VcRfaH-KOW can also switch between an all-α and an all-β state and that VcRfaH thus is, most probably, also a transformer protein.

### The model systems

The sequence of NusG/Spt5-KOW domains has been evolutionarily optimized to fold in only one defined conformation. Consequently, in the case of RfaH-KOW, the ability to switch between the all-α and the all-β state must be encoded within the primary structure, whereas the ‘decision’ which state to adopt solely depends on the availability of RfaH-NGN (Tomar et al., 2013). Sequence alignments and bioinformatical approaches (Balasco et al., 2015; Bernhardt and Hansmann, 2018; Gc et al., 2014; Joseph et al., 2019; Li et al., 2014; Shi et al., 2017; Xiong and Liu, 2015) gave first hints why RfaH, in contrast to NusG, is a metamorphic protein and how the structural switch might proceed. Yet, experimental evidence is still scarce. Thus, we analyzed isolated KOW domains of six NusG/Spt5 or RfaH proteins to identify characteristic properties of fold-switching proteins and to understand the molecular mechanisms underlying the refolding mechanism of RfaH-KOW. Due to the fact that NusG proteins are universally conserved, we chose NusG-KOWs from E. coli and Mycobacterium tuberculosis (Ec/MtNusG-KOW), the Spt5-KOW from the hyperthermophilic archaeon Methanocaldococcus jannaschii (MjSpt5-KOW) and the fifth KOW domain from human Spt5 (hSpt5-KOW5) as representative NusG-/Spt5-KOWs and the Ec/VcRfaH-KOWs as representatives for RfaH proteins. The constructs used are about 65 residues in length and contain the structured region and parts of the neighboring linker(s) (Figure 1—figure supplement 2A). In isolation all six domains exhibit the typical β-barrel topology (Figure 1—figure supplement 2B) with major differences only in the loops or turns connecting the β-strands (Figure 1—figure supplement 2C).

### Thermal and chemical stability of the KOW domains

Metamorphic proteins that switch between two stable conformations are expected to show two main minima in their energy landscape, each corresponding to one of these states (Dishman and Volkman, 2018). This implicates that (i) in order to control the structural interconversion, one of the conformations has to be (de)stabilized according to a molecular signal, and (ii) the energy minima cannot be as deep as the global minimum of a protein with a single, stable conformation to avoid permanent trapping of one state. Consequently, the all-β RfaH-KOW should show a limited thermodynamic stability to allow facile refolding to the all-α state when RfaH-NGN is available after transcription termination. To test this hypothesis, we analyzed the thermal stability of the six KOW domains by CD-based thermal denaturation experiments (Figure 2A) and by DSC (Figure 2B) at pH 4 and pH 7. At pH 7 unfolding was reversible for all KOW domains except for hSpt5-KOW5, which showed aggregation; the opposite effect was observed at pH 4 (Figure 2—figure supplement 1). All observed unfolding transitions were analyzed with a two-state model to determine the melting temperature, Tm, the enthalpy of unfolding at Tm, ΔHu(Tm), and, in case of the DSC thermograms, the temperature-dependent difference in heat capacity between the N and U states, ΔCp(T) (Figure 2C and D and Table 2).

![Figure 2.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig2-v2.jpg)

**Figure 2.:** (A) Thermal unfolding monitored via change in the circular dichroism (CD) signal with a temperature gradient from 20°C to 95°C. The line corresponds to the best fit to a two-state unfolding model. Measurements were carried out with proteins in 10 mM K-acetate (pH 4.0) buffer for hSpt5-KOW5 and in 10 mM K-phosphate (pH 7.0) buffer for all other domains. The wavelength for monitoring the transition was chosen based on the largest difference between the spectra of the folded and unfolded protein (for details, see Materials and methods). Data for EcNusG-KOW was not fitted due to the lack of the baseline of the unfolded state. MjSpt5-KOW could not be denatured at all. (B) Thermograms obtained from differential scanning calorimetry (DSC) measurements. All profiles are normalized to one molar of protein. The lines correspond to best fits to a two-state unfolding model that includes a T-dependent ΔCp change. Buffers are as in (A). (C,D) Tm (C) and ΔHu(Tm) (D) values derived from thermal unfolding experiments monitored by CD and DSC. Error bars result from data fitting.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** The graphs show circular dichroism (CD) spectra of the six Kyrpides, Ouzounis, Woese (KOW) domains at 25°C (blue) and at 95°C (red) together with the change in ellipticity, Δθ, during heating from 25°C to 95°C (filled black circles) and subsequent cooling to the initial temperature (filled gray circles), each at pH 4.0 (left) and pH 7.0 (right). When aggregation was already apparent from the CD spectra acquired at 95°C (i.e. the shape of the spectrum did not correspond to that of an unfolded protein), no thermal unfolding/refolding curves were recorded (n.a.). Due to its hyperthermophilic source organism, MjSpt5-KOW could not be denatured at either pH. The wavelength for monitoring the transition was chosen based on the largest difference between the spectra of the folded and unfolded state (for details see Materials and methods).

**Table 2.**
 Selected thermodynamic parameters of the six Kyrpides, Ouzounis, Woese (KOW) domains.The values were derived from thermal denaturations monitored by differential scanning calorimetry (DSC) and circular dichroism (CD) spectroscopy. Standard deviations result from data fitting.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>EcNusG-KOW</th>
      <th>MtNusG-KOW</th>
      <th>MjSpt5-KOW</th>
      <th>hSpt5-KOW5</th>
      <th>EcRfaH-KOW</th>
      <th>VcRfaH-KOW</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="7">Tm (°C) pH 7/pH 4</td>
    </tr>
    <tr>
      <td>CD</td>
      <td>–*/–</td>
      <td>76.6±0.874/–</td>
      <td>–†/–†</td>
      <td>–/60.5±0.771</td>
      <td>50.3±0.388/–</td>
      <td>65.2±1.78/–</td>
    </tr>
    <tr>
      <td>DSC</td>
      <td>87.0±0.0485/–</td>
      <td>77.0±0.0885/–</td>
      <td>111±0.0326/–</td>
      <td>–/58.0±0.162</td>
      <td>47.3±0.143/–</td>
      <td>70.2±0.379/–</td>
    </tr>
    <tr>
      <td colspan="7">ΔHu (Tm) (kJ/mol) pH 7/pH 4</td>
    </tr>
    <tr>
      <td>CD</td>
      <td>–*/–</td>
      <td>193±11.3/–</td>
      <td>–†–/–†</td>
      <td>–/140±12.4</td>
      <td>121±5.15/–</td>
      <td>162±2.91/–</td>
    </tr>
    <tr>
      <td>DSC</td>
      <td>222±0.339/–</td>
      <td>192±0.417/–</td>
      <td>293±0.345/–</td>
      <td>–/117±0.735</td>
      <td>129±0.432/–</td>
      <td>169±1.56/–</td>
    </tr>
    <tr>
      <td>ΔCp (Tm)(kJ/(K mol)) pH 7/pH 4</td>
      <td>0.800/–</td>
      <td>0.346/–</td>
      <td>–*/–</td>
      <td>–/2.27</td>
      <td>2.18/–</td>
      <td>0.148/–</td>
    </tr>
  </tbody>
</table>

_*Data was not fitted due to the lack of the baseline of the unfolded state.†No denaturation._

Due to the fact that the KOW domains are β-barrels the precision of the thermodynamic parameters determined by CD spectroscopy is not as high as for proteins with helical elements. Nevertheless, the results obtained by DSC and CD spectroscopy are in good agreement showing that EcNusG-KOW, MtNusG-KOW, and MjSpt5-KOW have much higher Tm values (87°C, 77°C, and 111°C, respectively) than hSpt5-KOW5 (58–60°C), EcRfaH-KOW (47–50°C), and VcRfaH-KOW (65–70°C). The same trend was observed for ΔHu(Tm) values. Consequently, this data indicates that EcNusG-KOW, MtNusG-KOW, and MjSpt5-KOW have a higher thermodynamic stability than Spt5-KOW5, EcRfaH-KOW, and VcRfaH-KOW.

To corroborate and complement the previous findings, we next performed far-UV CD-based chemical unfolding experiments at pH 4 and pH 7 using urea as denaturant (Figure 3A–F, left).

![Figure 3.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig3-v2.jpg)

**Figure 3.:** (A–F) Change in ΘMRW of the indicated protein domain upon over-night incubation with increasing concentrations of (left) urea in 10 mM K-acetate (pH 4.0; red circles) or 10 mM K-phosphate (pH 7.0; dark blue circles), respectively, and (right) GdmCl in 10 mM K-phosphate (pH 7.0; light blue circles). The detection wavelength is indicated and chosen based on the maximum difference between the spectra of the folded and unfolded state (for details see Materials and methods). The lines correspond to the best fits to a two-state unfolding model, except for EcRfaH-KOW, which exhibits a three-state unfolding behavior. (G, H) Comparison of [denat]1/2 values (G) and ΔGu(H2O) values (H) of the KOW domains derived from the chemical denaturation experiments shown in (A–E). Error bars result from data fitting.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A), (B) The curves show the normalized Trp fluorescence change at 380 nm of VcRfaH-KOW, obtained after over-night incubation of the protein in the presence of increasing concentrations of (A) urea at pH 4.0 (filled blue circles) or pH 7.0 (filled red circles) or (B) GdmCl at pH 7.0 (filled light blue circles). The lines represent fits to a two-state unfolding model.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Circular dichroism (CD) spectra of the six protein domains acquired at the indicated denaturant concentration and buffer. In order to check the reversibility, two spectra at identical denaturant concentration were obtained by adding the native protein from a solution containing no denaturant to the desired denaturant concentration (N → X), or by adding the unfolded protein from a solution containing 10 M urea/8 M GdmCl to a solution containing the desired denaturant concentration (U → X). The color code is indicated.

EcNusG-KOW, MtNusG-KOW, hSpt5-KOW5, and VcRfaH-KOW show a sigmoidal unfolding curve at either pH, indicative of a two-state unfolding process. Analysis of this data by the linear extrapolation model yields transition midpoints ([urea]1/2 values) and ΔGu(H2O) values that confirm the relative order of the stability as determined by thermal denaturation (Figure 3G and H, Table 3, and Figure 2C and D). For MjSpt5-KOW only the native state baseline is observable at both pH values, demonstrating that no denaturation could be achieved and that, consequently, this KOW domain exhibits the highest thermodynamic stability (assuming an m value comparable to that of the other KOW domains, MjSpt5-KOW likely has a ΔGu(H2O) value >30–40 kJ/mol). Notably, we obtained a ΔGu(H2O) value for hSpt5-KOW5 at pH 7, showing that this domain has a stability comparable to that of VcRfaH-KOW at physiological pH (Table 3). As VcRfaH-KOW, in contrast to all other KOW domains in this study, contains a Trp residue an additional fluorescence-based denaturation experiment was performed, and the obtained parameters are in good agreement with the CD data (Table 3 and Figure 3—figure supplement 1A).

**Table 3.**
 Thermodynamic parameters of the six Kyrpides, Ouzounis, Woese (KOW) domains.The values were derived from chemical denaturations monitored by circular dichroism (CD) spectroscopy as well as fluorescence spectroscopy where indicated. Standard deviations result from data fitting.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>EcNusG-KOW</th>
      <th>MtNusG-KOW</th>
      <th>MjSpt5-KOW</th>
      <th>hSpt5-KOW5</th>
      <th>EcRfaH-KOW</th>
      <th>VcRfaH-KOW</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="7">ΔGu(H2O) (25°C) (kJ/mol)</td>
    </tr>
    <tr>
      <td>Urea, pH 4</td>
      <td>19.8±2.21</td>
      <td>22.4±3.46</td>
      <td>–*</td>
      <td>6.24±4.42</td>
      <td>– (native state aggregation)</td>
      <td>10.8±1.66 (10.8±0.90)†</td>
    </tr>
    <tr>
      <td>Urea, pH 7</td>
      <td>27.7±4.21</td>
      <td>26.4±6.16</td>
      <td>–*</td>
      <td>14.3±2.90</td>
      <td>Three-state</td>
      <td>14.0±1.74 (13.9±0.61)†</td>
    </tr>
    <tr>
      <td>GdmCl, pH 7</td>
      <td>11.7±2.07</td>
      <td>15.7±3.99</td>
      <td>45.4±4.83</td>
      <td>7.37±3.16</td>
      <td>Three-state</td>
      <td>2.87±4.92 (2.84±6.55)†</td>
    </tr>
    <tr>
      <td colspan="7">m (25°C) (kJ/(mol M)) ‡</td>
    </tr>
    <tr>
      <td>Urea, pH 4</td>
      <td>2.51±0.453</td>
      <td>4.18±0.660</td>
      <td>–*</td>
      <td>3.25±0.857</td>
      <td>– (native state aggregation)</td>
      <td>2.91±0.396 (2.98±0.22)†</td>
    </tr>
    <tr>
      <td>Urea, pH 7</td>
      <td>3.84±0.681</td>
      <td>5.71±1.32</td>
      <td>–*</td>
      <td>3.83±0.820</td>
      <td>Three-state</td>
      <td>2.98±0.388 (3.13±0.14)†</td>
    </tr>
    <tr>
      <td>GdmCl, pH 7</td>
      <td>5.22±0.809</td>
      <td>8.26±1.87</td>
      <td>9.02±0.984</td>
      <td>4.95±1.31</td>
      <td>Three-state</td>
      <td>7.71±3.68 (7.86±4.29)†</td>
    </tr>
    <tr>
      <td colspan="7">[Denat]1/2 (25°C) (M)</td>
    </tr>
    <tr>
      <td>Urea, pH 4</td>
      <td>7.89</td>
      <td>5.36</td>
      <td>&gt;10*</td>
      <td>1.92</td>
      <td>– (native state aggregation)</td>
      <td>3.71 (3.62)†</td>
    </tr>
    <tr>
      <td>Urea, pH 7</td>
      <td>7.21</td>
      <td>4.62</td>
      <td>&gt;10*</td>
      <td>3.73</td>
      <td>~2.25/~4.25</td>
      <td>4.70 (4.44)†</td>
    </tr>
    <tr>
      <td>GdmCl, pH 7</td>
      <td>2.24</td>
      <td>1.90</td>
      <td>5.03</td>
      <td>1.49</td>
      <td>~0.6/~1.3</td>
      <td>0.37 (0.36)†</td>
    </tr>
  </tbody>
</table>

_*No denaturation possible.†Values were determined by fluorescence-based unfolding experiments.‡The m value is a measure of the broadness of the transition and correlates with the difference in the accessible surface area between N and U, and the transition midpoint._

To complement the analysis, we repeated the unfolding experiments at pH 7 using guanidinium chloride (GdmCl; Figure 3A-F, right, Table 3 and Figure 3—figure supplement 1B). As GdmCl is a more potent denaturant than urea, we were now able to denature even MjSpt5-KOW, giving a [GdmCl]1/2 value of 5.03 M, which is more than twice the value of the next stable protein. In accordance with the urea-based unfolding experiments at pH 7, MjSpt5-KOW, EcNusG-KOW, and MtNusG-KOW exhibit higher ΔGu(H2O) and [denat]1/2 values than VcRfaH-KOW and hSpt5-KOW5, although the relative order of stability of MtNusG-KOW and EcNusG-KOW is swapped. This difference as well as the difference between the absolute ΔGu(H2O) values derived from the urea- and GdmCl-based denaturations is a well-documented phenomenon and may be attributed to the limited applicability of the linear extrapolation model for the analysis of denaturations by GdmCl (see e.g. Gupta et al., 1996; Makhatadze, 1999). Thus, we base our conclusions on the relative comparison of the obtained values. We finally note that chemical unfolding was completely reversible in all cases (Figure 3—figure supplement 2).

Surprisingly, and in contrast to all other domains, EcRfaH-KOW shows a more complex unfolding curve in both urea- and GdmCl-based denaturation experiments at pH 7, with an additional plateau at ≈3 M urea or ≈1 M GdmCl, respectively, between the N and U baselines (Figure 3F; no curve could be obtained at pH 4 due to native state aggregation). This suggests that the unfolding of EcRfaH-KOW may be described via a three-step model including an observable equilibrium intermediate that might play an important role in the fold-switching mechanism of EcRfaH-KOW.

In summary, the poor spectroscopic properties of the analyzed domains limit the precision of the absolute values of the thermodynamic parameters obtained from CD experiments. However, our findings reveal clear differences in the global stability of the six domains and allow a grouping into two classes: MjSpt5-KOW and Ec/MtNusG-KOW are considered as ‘stable domains’, whereas the β-barrel Ec/VcRfaH-KOW as well as hSpt5-KOW5 show a reduced thermodynamic stability.

### Regions that are unfolded in all-α RfaH-KOW are destabilized in the all-β conformation

We next asked whether the less stable KOW domains also exhibit local differences in their stability as compared to the NusG-KOWs and MjSpt5-KOW. Therefore, we identified the backbone H-bond pattern in the six domains and quantified the magnitude of the through H-bond coupling constant, h3JNC’, by long-range HNCO NMR experiments (Table 4). This parameter is inversely proportional to the length of the H-bond and the deviation from its optimum angle, thus reflecting the H-bond strength (Grzesiek et al., 2004). To allow comparison between the six domains, we grouped H-bonds that are located at equivalent positions of the β-barrels and ordered them according to their position in the individual β-sheets (Figure 4A and B).

![Figure 4.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig4-v2.jpg)

**Figure 4.:** (A) Heat map of the magnitude of the h3JNC’ coupling constants of the H-bonds determined by long-range HNCO nuclear magnetic resonance (NMR) experiments. H-bonds that are located at equivalent positions are grouped and ordered according to their location in the respective β-sheet (position within the β-barrel as indicated in (B)), and colored according to their |h3JNC’| value as indicated at the bottom. H-bond numbers highlighted in yellow: H-bonds that have lower |h3JNC’| values for at least two of the domains with reduced thermodynamic stability compared to the stable domains; H-bond numbers highlighted in orange: H-bonds that have higher |h3JNC’| values for at least two of the domains with reduced thermodynamic stability compared to the stable domains. (B) Scheme of the positions of the H-bonds (dashed lines) within the β-barrel. Amino acids are depicted as spheres. White and red circles represent H-bond donors and acceptors, respectively. H-bonds are color-coded as in (A). (C) Cartoon representation of all-β EcRfaH-KOW (PDB-ID: 2LCL, gray). Regions that are unstructured in the all-α conformation are colored in dark red. H-bonds that have lower |h3JNC’| values for at least two of the domains with reduced thermodynamic stability compared to the stable domains are shown as yellow dashed tubes and labeled. The relative orientation of the structures is indicated. The inset shows the all-α EcRfaH-KOW (PDB-ID: 5OND; gray; unstructured regions at the termini are colored in dark red and correspond to the dark red regions in the all-β EcRfaH-KOW).

**Table 4.**
 Quantification of H-bond strengths from LR-HNCO nuclear magnetic resonance (NMR) experiments for all Kyrpides, Ouzounis, Woese (KOW) domains.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="4">EcNusG-KOW</th>
      <th colspan="4">MtNusG-KOW</th>
      <th colspan="4">MjSpt5-KOW</th>
    </tr>
    <tr>
      <th>H-bond #</th>
      <th>β-Sheet</th>
      <th>Donor</th>
      <th>Acceptor</th>
      <th>|h3JNC’| (Hz)</th>
      <th>σ |h3JNC’| (Hz)</th>
      <th>Donor</th>
      <th>Acceptor</th>
      <th>|h3JNC’| (Hz)</th>
      <th>σ |h3JNC’| (Hz)</th>
      <th>Donor</th>
      <th>Acceptor</th>
      <th>|h3JNC’| (Hz)</th>
      <th>σ |h3JNC’| (Hz)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>β1-β2</td>
      <td>131</td>
      <td>148</td>
      <td>0.69</td>
      <td>0.0077</td>
      <td>188</td>
      <td>205</td>
      <td>0.61</td>
      <td>0.0098</td>
      <td>92</td>
      <td>109</td>
      <td>0.70</td>
      <td>0.013</td>
    </tr>
    <tr>
      <td>2</td>
      <td>β1-β2</td>
      <td>148</td>
      <td>132</td>
      <td>0.72</td>
      <td>0.0083</td>
      <td>205</td>
      <td>189</td>
      <td>0.69</td>
      <td>0.0094</td>
      <td>109</td>
      <td>93</td>
      <td>0.79</td>
      <td>0.0088</td>
    </tr>
    <tr>
      <td>3</td>
      <td>β1-β2</td>
      <td>134</td>
      <td>146</td>
      <td>0.67</td>
      <td>0.0081</td>
      <td>191</td>
      <td>203</td>
      <td>0.56</td>
      <td>0.011</td>
      <td>95</td>
      <td>107</td>
      <td>0.77</td>
      <td>0.012</td>
    </tr>
    <tr>
      <td>4</td>
      <td>β1-β2</td>
      <td>146</td>
      <td>134</td>
      <td>0.62</td>
      <td>0.0096</td>
      <td>203</td>
      <td>191</td>
      <td>0.62</td>
      <td>0.0094</td>
      <td>107</td>
      <td>95</td>
      <td>0.67</td>
      <td>0.0095</td>
    </tr>
    <tr>
      <td>5</td>
      <td>β1-β2</td>
      <td>136</td>
      <td>144</td>
      <td>0.65</td>
      <td>0.0073</td>
      <td>193</td>
      <td>201</td>
      <td>0.65</td>
      <td>0.0080</td>
      <td>97</td>
      <td>105</td>
      <td>0.68</td>
      <td>0.048</td>
    </tr>
    <tr>
      <td>6</td>
      <td>β1-β2</td>
      <td>143</td>
      <td>136</td>
      <td>0.65</td>
      <td>0.0088</td>
      <td>200</td>
      <td>193</td>
      <td>0.76</td>
      <td>0.013</td>
      <td>104</td>
      <td>97</td>
      <td>0.82</td>
      <td>0.012</td>
    </tr>
    <tr>
      <td>7</td>
      <td>β2-β3</td>
      <td>147</td>
      <td>161</td>
      <td>0.37</td>
      <td>0.0105</td>
      <td>204</td>
      <td>218</td>
      <td>0.31</td>
      <td>0.015</td>
      <td>108</td>
      <td>122</td>
      <td>0.54</td>
      <td>0.010</td>
    </tr>
    <tr>
      <td>8</td>
      <td>β2-β3</td>
      <td>161</td>
      <td>147</td>
      <td colspan="2">Peak overlap</td>
      <td>218</td>
      <td>204</td>
      <td>0.69</td>
      <td>0.011</td>
      <td>122</td>
      <td>108</td>
      <td>0.65</td>
      <td>0.010</td>
    </tr>
    <tr>
      <td>9</td>
      <td>β2-β3</td>
      <td>149</td>
      <td>159</td>
      <td>0.67</td>
      <td>0.012</td>
      <td>206</td>
      <td>216</td>
      <td>0.53</td>
      <td>0.013</td>
      <td>110</td>
      <td>120</td>
      <td>0.57</td>
      <td>0.030</td>
    </tr>
    <tr>
      <td>10</td>
      <td>β2-β3</td>
      <td>159</td>
      <td>150</td>
      <td>0.50</td>
      <td>0.0086</td>
      <td>216</td>
      <td>207</td>
      <td>0.45</td>
      <td>0.012</td>
      <td>120</td>
      <td>111</td>
      <td>0.60</td>
      <td>0.010</td>
    </tr>
    <tr>
      <td>11</td>
      <td>β2-β3</td>
      <td>152</td>
      <td>157</td>
      <td>0.46</td>
      <td>0.019</td>
      <td>209</td>
      <td>214</td>
      <td colspan="2">Peak overlap</td>
      <td>113</td>
      <td>118</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>12</td>
      <td>β3-β4</td>
      <td>158</td>
      <td>173</td>
      <td>0.78</td>
      <td>0.0077</td>
      <td>215</td>
      <td>230</td>
      <td>0.83</td>
      <td>0.0088</td>
      <td>119</td>
      <td>134</td>
      <td colspan="2">No HNCO peak</td>
    </tr>
    <tr>
      <td>13</td>
      <td>β3-β4</td>
      <td>173</td>
      <td>158</td>
      <td>0.64</td>
      <td>0.010</td>
      <td>230</td>
      <td>215</td>
      <td>0.62</td>
      <td>0.011</td>
      <td>134</td>
      <td>119</td>
      <td>0.62</td>
      <td>0.010</td>
    </tr>
    <tr>
      <td>14</td>
      <td>β3-β4</td>
      <td>160</td>
      <td>171</td>
      <td>0.73</td>
      <td>0.0056</td>
      <td>217</td>
      <td>228</td>
      <td>0.75</td>
      <td>0.0089</td>
      <td>121</td>
      <td>132</td>
      <td>0.88</td>
      <td>0.012</td>
    </tr>
    <tr>
      <td>15</td>
      <td>β3-β4</td>
      <td>171</td>
      <td>161</td>
      <td colspan="2">Peak overlap</td>
      <td>228</td>
      <td>217</td>
      <td>0.73</td>
      <td>0.0062</td>
      <td>132</td>
      <td>121</td>
      <td>0.47</td>
      <td>0.014</td>
    </tr>
    <tr>
      <td>16</td>
      <td>β3-β4</td>
      <td>162</td>
      <td>169</td>
      <td>0.51</td>
      <td>0.0074</td>
      <td>219</td>
      <td>226</td>
      <td>0.50</td>
      <td>0.0090</td>
      <td>123</td>
      <td>130</td>
      <td colspan="2">No H-bond distance</td>
    </tr>
    <tr>
      <td>17</td>
      <td>β3-β4</td>
      <td>169</td>
      <td>162</td>
      <td>0.60</td>
      <td>0.0066</td>
      <td>226</td>
      <td>219</td>
      <td>0.61</td>
      <td>0.0091</td>
      <td colspan="2">No equivalent</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>18</td>
      <td>β3-β4</td>
      <td>167</td>
      <td>164</td>
      <td>–</td>
      <td>–</td>
      <td>224</td>
      <td>221</td>
      <td>0.20</td>
      <td>0.019</td>
      <td colspan="2">No equivalent</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>19</td>
      <td>β5-β1</td>
      <td>137</td>
      <td>177</td>
      <td>0.46</td>
      <td>0.017</td>
      <td>194</td>
      <td>234</td>
      <td>0.52</td>
      <td>0.025</td>
      <td>98</td>
      <td>138</td>
      <td colspan="2">No HNCO peak</td>
    </tr>
    <tr>
      <td>20</td>
      <td>β5-β1</td>
      <td>179</td>
      <td>135</td>
      <td colspan="2">Peak overlap</td>
      <td>236</td>
      <td>192</td>
      <td>0.47</td>
      <td>0.016</td>
      <td>140</td>
      <td>96</td>
      <td colspan="2">Peak overlap</td>
    </tr>
    <tr>
      <td>21</td>
      <td>β5-β1</td>
      <td>135</td>
      <td>179</td>
      <td>0.73</td>
      <td>0.0060</td>
      <td>192</td>
      <td>236</td>
      <td colspan="2">Peak overlap</td>
      <td>96</td>
      <td>140</td>
      <td colspan="2">Peak overlap</td>
    </tr>
    <tr>
      <td>22</td>
      <td>β5-β1</td>
      <td>181</td>
      <td>133</td>
      <td>–</td>
      <td>–</td>
      <td>238</td>
      <td>190</td>
      <td>–</td>
      <td>–</td>
      <td>142</td>
      <td>94</td>
      <td>0.46</td>
      <td>0.023</td>
    </tr>
    <tr>
      <td>23</td>
      <td>β5-β1</td>
      <td colspan="2">No equivalent</td>
      <td>–</td>
      <td>–</td>
      <td colspan="2">No equivalent</td>
      <td>–</td>
      <td>–</td>
      <td>143</td>
      <td>94</td>
      <td>0.27</td>
      <td>0.022</td>
    </tr>
    <tr>
      <td>24</td>
      <td>β5-β1</td>
      <td colspan="2">No equivalent</td>
      <td>–</td>
      <td>–</td>
      <td colspan="2">No equivalent</td>
      <td>–</td>
      <td>–</td>
      <td>94</td>
      <td>143</td>
      <td>0.57</td>
      <td>0.010</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td colspan="4">hSpt5-KOW5</td>
      <td colspan="4">EcRfaH-KOW</td>
      <td colspan="4">VcRfaH-KOW</td>
    </tr>
    <tr>
      <td>H-bond #</td>
      <td>β-Sheet</td>
      <td>Donor</td>
      <td>Acceptor</td>
      <td>|h3JNC’| (Hz)</td>
      <td>σ |h3JNC’| (Hz)</td>
      <td>Donor</td>
      <td>Acceptor</td>
      <td>|h3JNC’| (Hz)</td>
      <td>σ |h3JNC’| (Hz)</td>
      <td>Donor</td>
      <td>Acceptor</td>
      <td>|h3JNC’| (Hz)</td>
      <td>σ |h3JNC’| (Hz)</td>
    </tr>
    <tr>
      <td>1</td>
      <td>β1-β2</td>
      <td>707</td>
      <td>724</td>
      <td>0.60</td>
      <td>0.0074</td>
      <td>113</td>
      <td>130</td>
      <td>0.76</td>
      <td>0.020</td>
      <td>116</td>
      <td>133</td>
      <td>0.87</td>
      <td>0.015</td>
    </tr>
    <tr>
      <td>2</td>
      <td>β1-β2</td>
      <td>724</td>
      <td>708</td>
      <td colspan="2">Peak overlap</td>
      <td>130</td>
      <td>114</td>
      <td>0.53</td>
      <td>0.051</td>
      <td>133</td>
      <td>117</td>
      <td>0.59</td>
      <td>0.024</td>
    </tr>
    <tr>
      <td>3</td>
      <td>β1-β2</td>
      <td>710</td>
      <td>722</td>
      <td>0.70</td>
      <td>0.0077</td>
      <td>116</td>
      <td>128</td>
      <td>0.65</td>
      <td>0.027</td>
      <td>119</td>
      <td>131</td>
      <td colspan="2">Peak overlap</td>
    </tr>
    <tr>
      <td>4</td>
      <td>β1-β2</td>
      <td>722</td>
      <td>710</td>
      <td>0.50</td>
      <td>0.019</td>
      <td>128</td>
      <td>116</td>
      <td colspan="2">Peak overlap</td>
      <td>131</td>
      <td>119</td>
      <td>0.46</td>
      <td>0.020</td>
    </tr>
    <tr>
      <td>5</td>
      <td>β1-β2</td>
      <td>712</td>
      <td>720</td>
      <td colspan="2">No HNCO peak</td>
      <td>118</td>
      <td>126</td>
      <td>0.53</td>
      <td>0.056</td>
      <td>121</td>
      <td>129</td>
      <td>0.57</td>
      <td>0.014</td>
    </tr>
    <tr>
      <td>6</td>
      <td>β1-β2</td>
      <td>719</td>
      <td>713</td>
      <td colspan="2">Peak overlap</td>
      <td>125</td>
      <td>118</td>
      <td>0.66</td>
      <td>0.026</td>
      <td>128</td>
      <td>121</td>
      <td>0.62</td>
      <td>0.017</td>
    </tr>
    <tr>
      <td>7</td>
      <td>β2-β3</td>
      <td>723</td>
      <td>735</td>
      <td colspan="2">H-bond peak present. but too weak to quantify</td>
      <td>129</td>
      <td>142</td>
      <td>0.41</td>
      <td>0.029</td>
      <td>132</td>
      <td>145</td>
      <td>0.42</td>
      <td>0.019</td>
    </tr>
    <tr>
      <td>8</td>
      <td>β2-β3</td>
      <td>735</td>
      <td>723</td>
      <td colspan="2">Peak overlap</td>
      <td>142</td>
      <td>129</td>
      <td>0.70</td>
      <td>0.019</td>
      <td>145</td>
      <td>132</td>
      <td>0.69</td>
      <td>0.027</td>
    </tr>
    <tr>
      <td>9</td>
      <td>β2-β3</td>
      <td>725</td>
      <td>734</td>
      <td>0.71</td>
      <td>0.010</td>
      <td>131</td>
      <td>140</td>
      <td>0.48</td>
      <td>0.032</td>
      <td>134</td>
      <td>143</td>
      <td>0.61</td>
      <td>0.036</td>
    </tr>
    <tr>
      <td>10</td>
      <td>β2-β3</td>
      <td>733</td>
      <td>726</td>
      <td>–</td>
      <td>–</td>
      <td>140</td>
      <td>132</td>
      <td>0.96</td>
      <td>0.021</td>
      <td>143</td>
      <td>135</td>
      <td>1.0</td>
      <td>0.011</td>
    </tr>
    <tr>
      <td>11</td>
      <td>β2-β3</td>
      <td>728</td>
      <td>731</td>
      <td>0.61</td>
      <td>0.012</td>
      <td>134</td>
      <td>138</td>
      <td>–</td>
      <td>–</td>
      <td>137</td>
      <td>141</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>12</td>
      <td>β3-β4</td>
      <td>732</td>
      <td>745</td>
      <td>0.59</td>
      <td>0.009</td>
      <td>139</td>
      <td>154</td>
      <td>0.60</td>
      <td>0.034</td>
      <td>142</td>
      <td>157</td>
      <td colspan="2">Peak overlap</td>
    </tr>
    <tr>
      <td>13</td>
      <td>β3-β4</td>
      <td>745</td>
      <td>732</td>
      <td>0.62</td>
      <td>0.019</td>
      <td>154</td>
      <td>139</td>
      <td colspan="2">No HNCO peak</td>
      <td>157</td>
      <td>142</td>
      <td>0.68</td>
      <td>0.015</td>
    </tr>
    <tr>
      <td>14</td>
      <td>β3-β4</td>
      <td>734</td>
      <td>743</td>
      <td>0.69</td>
      <td>0.039</td>
      <td>141</td>
      <td>152</td>
      <td>0.65</td>
      <td>0.049</td>
      <td>144</td>
      <td>155</td>
      <td>0.58</td>
      <td>0.019</td>
    </tr>
    <tr>
      <td>15</td>
      <td>β3-β4</td>
      <td>743</td>
      <td>734</td>
      <td>0.49</td>
      <td>0.029</td>
      <td>152</td>
      <td>141</td>
      <td>–</td>
      <td>–</td>
      <td>155</td>
      <td>144</td>
      <td>0.72</td>
      <td>0.021</td>
    </tr>
    <tr>
      <td>16</td>
      <td>β3-β4</td>
      <td>736</td>
      <td>741</td>
      <td>0.63</td>
      <td>0.033</td>
      <td>143</td>
      <td>150</td>
      <td>0.75</td>
      <td>0.033</td>
      <td>146</td>
      <td>153</td>
      <td>0.49</td>
      <td>0.024</td>
    </tr>
    <tr>
      <td>17</td>
      <td>β3-β4</td>
      <td>741</td>
      <td>736</td>
      <td colspan="2">No H-bond orientation</td>
      <td>150</td>
      <td>143</td>
      <td>0.47</td>
      <td>0.052</td>
      <td>153</td>
      <td>146</td>
      <td>0.48</td>
      <td>0.015</td>
    </tr>
    <tr>
      <td>18</td>
      <td>β3-β4</td>
      <td colspan="2">No equivalent</td>
      <td>–</td>
      <td>–</td>
      <td>148</td>
      <td>145</td>
      <td colspan="2">No H-bond orientation</td>
      <td>151</td>
      <td>148</td>
      <td colspan="2">No HNCO peak</td>
    </tr>
    <tr>
      <td>19</td>
      <td>β5-β1</td>
      <td>713</td>
      <td>749</td>
      <td colspan="2">No HNCO peak</td>
      <td>119</td>
      <td>158</td>
      <td colspan="2">Peak overlap</td>
      <td>122</td>
      <td>161</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>20</td>
      <td>β5-β1</td>
      <td>751</td>
      <td>711</td>
      <td>–</td>
      <td>–</td>
      <td>160</td>
      <td>117</td>
      <td>0.51</td>
      <td>0.036</td>
      <td>163</td>
      <td>120</td>
      <td>0.57</td>
      <td>0.037</td>
    </tr>
    <tr>
      <td>21</td>
      <td>β5-β1</td>
      <td>711</td>
      <td>751</td>
      <td>0.68</td>
      <td>0.023</td>
      <td>117</td>
      <td>160</td>
      <td>0.68</td>
      <td>0.015</td>
      <td>120</td>
      <td>163</td>
      <td>0.53</td>
      <td>0.016</td>
    </tr>
    <tr>
      <td>22</td>
      <td>β5-β1</td>
      <td>753</td>
      <td>709</td>
      <td>–</td>
      <td>–</td>
      <td>162</td>
      <td>115</td>
      <td>–</td>
      <td>–</td>
      <td>165</td>
      <td>118</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>23</td>
      <td>β5-β1</td>
      <td colspan="2">No equivalent</td>
      <td>–</td>
      <td>–</td>
      <td colspan="2">No equivalent</td>
      <td>–</td>
      <td>–</td>
      <td colspan="2">No equivalent</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>24</td>
      <td>β5-β1</td>
      <td colspan="2">No equivalent</td>
      <td>–</td>
      <td>–</td>
      <td colspan="2">No equivalent</td>
      <td>–</td>
      <td>–</td>
      <td colspan="2">No equivalent</td>
      <td>–</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

Most |h3JNC’| values are in the range of 0.5–0.9 Hz, which is typical for H-bonds of β-sheets (Grzesiek et al., 2004). In line with having the highest Tm, MjSpt5-KOW often exhibits the highest coupling constants, which is indicative of a highly rigid packing of the β-barrel. Strikingly, MjSpt5-KOW has three additional H-bonds between strands β5 and β1 (#22–24), which provides an extra stabilization of the C-terminal β-strand that may contribute to the high thermostability of this protein. The ‘stable’ domains (i.e. Ec/MtNusG-KOW and MjSpt5-KOW) show their strongest H-bonds in two regions, namely between strands β1:β2 and β3:β4. In addition, most of these H-bonds are more stable than corresponding H-bonds in Ec/VcRfaH-KOW and hSpt5-KOW5, implying that the H-bonds in the domains with reduced stability are more dynamic and on average longer or involve a less optimal bonding angle. From this we conclude that in Ec/VcRfaH-KOW and hSpt5-KOW5 strands β1 and parts of β4 are less stably bound to the rest of the β-barrel than in the stable domains. Moreover, together with the fact that β1, the C-terminal half of β4, and β5 are disordered in the all-α state of the Ec/VcRfaH-KOW (Figure 4C), this also reflects the chameleonic folding behavior of these regions in the all-β state.

### hSpt5-KOW5, Ec- and VcRfaH-KOW exchange with a globally unfolded conformer on the ms time scale

To assess the folding mechanism of the KOW domains at the amino acid level, we performed an NMR-based analysis of the structural dynamics of the six β-barrel proteins. As larger structural rearrangements, such as folding events, mostly occur at the μs-ms time scale for small proteins or are even slower (Maxwell et al., 2005), we focused on the analysis of the slow chemical exchange regime. Therefore, we performed amide 15N-based chemical exchange saturation transfer (CEST) experiments (Vallurupalli et al., 2012). This method allows the sensitive detection and characterization of sparsely populated states (=minor species; relative population pB) that exchange with a major species (relative population pA = 1 - pB) with a rate kex of 10–200 s–1. The detection is achieved by frequency-selective saturation along the 15N dimension that is ‘transferred’ from the minor to the major species. This decreases the signal intensity of the major species and then leads to an additional dip in the CEST profile (major species signal intensity versus saturation frequency) next to the large major species minimum if there is a difference in the resonance frequencies of the two species.

None of the CEST profiles of EcNusG-KOW, MtNusG-KOW, and MjSpt5-KOW exhibits an exchange peak (Figure 5A-C), demonstrating that these domains are stable on the ms time scale, in agreement with their high thermodynamic stabilities (see above).

![Figure 5.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig5-v2.jpg)

**Figure 5.:** (A–F) Representative backbone 15N-CEST profiles of the indicated KOW domain measured with one (A–C) or two (D–F) B1 field strengths and an exchange time of 0.5 s. B0 field for (A–C): 21.15T; B0 field for (A–C): 16.45T. The lines in (D–F) are fits to a two-state exchange model. (G–I) Correlation plots showing the high similarity of the chemical shift of the minor CEST species and that of the corresponding random coil value. The latter were obtained by backbone assignment in 8 M urea (EcRfaH-KOW) or are theoretical values (VcRfaH-KOW, hSpt5-KOW5). The squared correlation coefficient and the root mean square deviation (rmsd) between the two corresponding sets of chemical shifts are listed.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Plots of kex versus the population of the minor species (pB) obtained from individual fits (black symbols) or a global fit (red symbol) of the CEST profiles of (A) hSpt5-KOW5, (B) VcRfaH-KOW, and (C) EcRfaH-KOW. Error bars represent the standard deviation of the fits.

In contrast, most CEST traces of hSpt5-KOW5, EcRfaH-KOW, and VcRfaH-KOW have a second dip, indicating exchange with a second, low-populated state (exemplary traces are shown in Figure 5D-F). Using a two-state exchange model, we fitted all CEST traces that showed an exchange signal individually to determine the residue-specific kex and pB values. In all three cases, the kex/pB values appear to cluster in one region, suggesting a global, cooperative process (Figure 5—figure supplement 1A). Thus, we next performed a global fit of all CEST traces for each of the three proteins resulting in global rate constants and populations as well as lifetimes of the two states (Table 5). This analysis yields a relatively high pB value (5.50%) but low kex (15.0 s–1) for EcRfaH-KOW, a much lower pB value (0.43%) but higher kex (75.0 s–1) for VcRfaH-KOW, and pB/kex values of 0.85% and 89.0 s–1 for hSpt5-KOW5.

**Table 5.**
 Exchange parameters derived from global fitting of the chemical exchange saturation transfer (CEST) experiments to a two-state exchange model.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>hSpt5-KOW5</th>
      <th>VcRfaH-KOW</th>
      <th>EcRfaH-KOW</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>pA (%)</td>
      <td>99.15±0.02</td>
      <td>99.57±0.01</td>
      <td>94.47±0.46</td>
    </tr>
    <tr>
      <td>pB (%)</td>
      <td>0.85±0.02</td>
      <td>0.43±0.01</td>
      <td>5.53±0.46</td>
    </tr>
    <tr>
      <td>kAB (s–1)</td>
      <td>0.76±0.03</td>
      <td>0.32±0.02</td>
      <td>0.82±0.10</td>
    </tr>
    <tr>
      <td>kBA (s–1)</td>
      <td>88.62±3.12</td>
      <td>74.24±3.17</td>
      <td>13.98±1.24</td>
    </tr>
    <tr>
      <td>kex (s–1)</td>
      <td>89.38±3.15</td>
      <td>74.57±3.18</td>
      <td>14.80±1.31</td>
    </tr>
    <tr>
      <td>τA (s)</td>
      <td>1.31±0.05</td>
      <td>3.08±0.15</td>
      <td>1.22±0.15</td>
    </tr>
    <tr>
      <td>τB (ms)</td>
      <td>11.28±0.40</td>
      <td>13.47±0.57</td>
      <td>71.52±6.33</td>
    </tr>
    <tr>
      <td>ΔG (kJ/mol)</td>
      <td>11.81±0.05</td>
      <td>13.48±0.07</td>
      <td>7.18±0.21</td>
    </tr>
  </tbody>
</table>

To characterize the exchanging species structurally, we analyzed the chemical shifts of the minor species. In all three cases, the minor species shifts show a very good correlation with those of a completely unfolded conformation (Figure 5G–I; R2 >96%, rmsd <1.04 ppm). Note that the chemical shifts for the unfolded state of EcRfaH-KOW were obtained experimentally by backbone assignment of the protein in 8 M urea, whereas those of VcRfaH-KOW and hSpt5-KOW5 are predicted values (see Materials and methods for details). Determination of the relative populations finally results in the equilibrium constant and the difference in Gibbs free energy, ΔG, separating the energy levels of the two species (Table 5). As expected, these ΔG values are similar to those obtained from the urea-based unfolding experiments at pH 7 (Table 3).

Taken together, the CEST experiments show that the folded all-β state of the isolated RfaH-KOWs and also hSpt5-KOW5 is in equilibrium with a species that resembles an unfolded conformation. As this state is easily accessible from the β-barrel, we conclude that the folding barrier separating the two states cannot be too high as this would prohibit an exchange on the ms time scale.

### The unfolded conformers of Ec- and VcRfaH-KOW contain transient helical structures

Although the chemical shifts of the minor species of EcRfaH-KOW nicely correlate with the chemical shifts of the urea-unfolded protein (Figure 5I), there are some noticeable differences in the 15N chemical shifts (Δδ 15N) of the two data sets (red bars in Figure 6A, top panel). In particular, two regions (region 1: Q127–T131, region 2: E136–I150) show significant deviations of –1 to –3 ppm, indicating local residual structures in these regions. As the type of present (secondary) structure cannot be derived from 15N data, we recorded a CEST experiment on the 13Cα carbons of 13C,15N-EcRfaH-KOW (Figure 6—figure supplement 1) and calculated Δδ 13Cα between the observed minor species values and the random coil values obtained from the urea-unfolded protein (red bars in Figure 6A, bottom panel). The deviations are positive in regions 1 and 2, indicating the presence of helical structures at these sites. This is in agreement with secondary structure predictions, which show that the Leu-rich motif (LLLNL) in region 2, where the deviations of δ 15N and δ 13Cα are most pronounced, has high α-helical propensity (Figure 6—figure supplement 2; see also Balasco et al., 2015). Moreover, the two helical elements are located at the positions of the two α-helices in the all-α form of EcRfaH-KOW (compare Figure 1B). Due to the presence of two dips the CEST profiles can be analyzed using a two-state model (minor versus major species). Interestingly, the resulting 15N transverse relaxation rates (R2 values) of regions 1 and 2 in the minor species are significantly higher than corresponding rates in the β-barrel state (Figure 6A, mid panel). Generally, one would expect that the minor species exhibits lower R2 values as it is more flexible due to its largely unfolded nature (Farrow et al., 1995). The increased relaxation rates thus indicate the presence of additional exchange processes on the intermediate to fast chemical exchange (i.e. μs–ms) time scale. Consequently, the minor species itself seems to be an ensemble of predominantly unfolded, fast interconverting structures with transient helical elements in regions 1 and 2 rather than a static population. As no dips in addition to the ones of the minor and major species can be observed in the CEST profiles, the population of other states is low and beyond the detection limit of CEST experiments.

![Figure 6.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig6-v2.jpg)

**Figure 6.:** (A) Deviations of the minor species of EcRfaH-KOW from the urea-unfolded state. Top row: Sequence-dependent difference between the 15N backbone amide chemical shifts of the minor species and of the values obtained by assignment in 8 M urea. The values for the minor species were either obtained from the chemical exchange saturation transfer (CEST) experiment (red bars, individual fits; ‘CEST – unfolded’) or by tracing back the chemical shift changes from 8 to 0 M urea in the [1H, 15N]-heteronuclear single quantum coherence (HSQC)-based urea titration (gray bars; ‘titration – unfolded’; see panel (B)). Middle row: R2 values of the major species (EcRfaH-KOW β-barrel; blue) and minor species (red), obtained from fitting the CEST profiles (global fit). Regions 1 and 2 of the minor species have R2 values significantly higher than those of their corresponding β-barrel conformation indicating additional exchange processes, whereas N- and C-terminal regions have R2 values lower than those of their corresponding β-barrel conformation, which is typical for random coil structures. Bottom row: Sequence-dependent difference between the 13Cα chemical shifts of the minor species and of the values obtained by assignment in 8 M urea. The values for the minor species were either obtained from the CEST experiment (red bars, individual fits; ‘CEST – unfolded’) or by tracing back the chemical shift changes from 8 to 0 M urea in the [1H, 13C]-ctHSQC-based urea titration (gray bars; ‘titration – unfolded’; see panel (C)). The sequence of EcRfaH-KOW is given above the diagram, the Leu-rich motif is underlined. Regions 1 and 2 are highlighted. Error bars result from data fitting. (B, C) Nuclear magnetic resonance (NMR)-based chemical equilibrium unfolding experiments of EcRfaH-KOW using urea as denaturant. The plots show an overlay of (B) [1H, 15N]-HSQC, and (C) [1H, 13C]-ctHSQC spectra of [15N, 13C]-EcRfaH-KOW, acquired in the presence of varying urea concentrations. The system was buffered by 20 mM Na-phosphate (pH 6.5), 100 mM NaCl, 1 mM ethylenediaminetetraacetic acid (EDTA), 10% (v/v) D2O. Boxed regions mark signals corresponding to the β-barrel state with the signal of S139 being labeled with ‘N’ (‘native’). Arrows and further labels indicate signals of residues that exhibit strong chemical shift changes in the indirect dimension (15N in (B), 13C in (C)). The spectra are colored as indicated.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** The arrows indicate the positions of the minor species dips.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** For each domain two predictions were carried out: (i) By Net-CSSP (Kim et al., 2009), top. The contact-dependent secondary structure propensity (CSSP) of each domain is plotted against die amino acid sequence (red: helices; blue: beta structures; green: random coil). The heat map above each graph displays the propensity of each amino acid to adopt helical (red), beta (blue), or random coil (green) structures using a gradient from dark (high propensity) to light (low propensity) colors. (ii) By Jpred 4 (Drozdetskiy et al., 2015), bottom. The predicted secondary structure elements are shown below the amino acid sequence (red: helices; blue: beta structures). JNetPRED: consensus prediction; JNetCONF: confidence estimate for the prediction (high values correspond to high confidence); JNetHMM: profile prediction based on hidden Markov model (HMM), JNetPSSM: profile prediction based on position-specific scoring matrix (PSSM); JNetJURY: an asterisk indicates significantly different primary predictions.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** (A) Sequence-dependent difference between the 15N backbone amide chemical shifts of the chemical exchange saturation transfer (CEST) minor species of VcRfaH-KOW and the corresponding theoretical random coil value. The sequence of the two protein construct is given above the diagrams. (B) Exemplary traces of CEST experiments recorded on 13Cα carbons of 13C,15N-VcRfaH-KOW. Solid arrows mark the positions of the minor species dips, dashed arrows indicate the predicted random coil values.

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig6-figsupp4-v2.jpg)

**Figure 6—figure supplement 4.:** (A) Sequence-dependent difference between the 15N backbone amide (top) and 13Cα carbons (bottom) chemical shifts of the chemical exchange saturation transfer (CEST) minor species of hSpt5-KOW5 and the corresponding theoretical random coil value. The sequence of the two protein construct is given above the diagrams. (B) Exemplary traces of CEST experiments recorded on 13Cα carbons of 13C,15N-hSpt5-KOW5. Arrows mark the positions of the minor species dips.

![Figure 6—figure supplement 5.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig6-figsupp5-v2.jpg)

**Figure 6—figure supplement 5.:** (A, B) Near-UV circular dichroism (CD) spectra of EcRfaH-KOW during a titration with (A) 10 M urea and (B) 8 M GdmCl. In both cases, the solution was buffered by 10 mM K-phosphate (pH 7.0). The denaturant concentrations at which the spectra were recorded are indicated. (C) 8-Anilino-1-naphthalenesulfonic acid (ANS) binding experiments. The graph shows the ANS fluorescence at 485 nm after over-night incubation of ANS in the presence (filled red circles) or absence (filled blue circles) of EcRfaH-KOW at increasing urea concentrations. The system was buffered by 10 mM K-phosphate (pH 7.0).

![Figure 6—figure supplement 6.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig6-figsupp6-v2.jpg)

**Figure 6—figure supplement 6.:** (A) Relative populations of the minor (filled red circles) and major (filled blue circles) species during the [1H, 13C]-ctHSQC-based urea denaturation of 1H, 13C-EcRfaH-KOW. The populations at a certain urea concentration were calculated from the ratio of volumes of the Hα/Cα correlation peaks of S139 minor or major species signals, respectively, to the sum of both values. The curves were fitted to a two-state model to extract the parameters of the transition from the major species to the minor species. The minor species was treated as a single species neglecting the fact that it is actually an ensemble of at least two subspecies. Fitting to a three-state (or even higher-state) model with an increased number of fitting parameters would not be appropriate due to the limited number of data points. (B) Chemical shift changes of 13Cα signals, Δδ13Cα, of A137, S139, and M140 in the [1H, 13C]-ctHSQC spectra during urea denaturation.

Like EcRfaH-KOW, the minor species of VcRfaH-KOW also seems to contain residual structure (Figure 6—figure supplement 3A). As the unfolded state of this domain was not assigned experimentally, predicted chemical shift values for the random coil structure were used for the correlation plot (Figure 5H). When plotting the Δδ 15N values versus the sequence position (Figure 6—figure supplement 3A), the resulting pattern resembles the one obtained for EcRfaH-KOW (compare Figure 6A, top panel). The regions around residues 103–125 (linker) and 155–165 (C-terminus) show relatively low Δδ 15N values, indicating a random coil structure, whereas the region around residues 140–150 (corresponding to region 2 in EcRfaH-KOW) exhibits significantly increased Δδ 15N values, suggesting residual structure, similar to EcRfaH-KOW. However, only very small minor species dips were observed in some traces of a CEST experiment recorded on the 13Cα carbons of 13C,15N-VcRfaH-KOW (Figure 6—figure supplement 3B), which we attribute to the very low population of the VcRfaH-KOW minor species (0.43%) that is at the detection limit of the Cα-CEST experiment (which is less sensitive than the 15N-CEST). Consequently, we analyzed the CEST profiles only qualitatively. Unambiguous minor species dips could be identified for amino acids predominantly located in the region with residual structure with chemical shifts that are downfield-shifted as compared to random coil values (Figure 6—figure supplement 3B), indicating the presence of helical elements. As for EcRfaH-KOW, this is in full agreement with secondary structure predictions, which suggest that all NusG/Spt5-KOW domains adopt four to five β-strands whereas both RfaH-KOW domains exhibit propensities for both β-strands and α-helices, especially in the regions with residual structure in the CEST minor species (Figure 6—figure supplement 2). Taken together this data suggests that the VcRfaH-KOW minor species also contains transient residual helical structures.

The hSpt5-KOW5 domain is part of an ‘RNA clamp’ during transcription elongation in eukaryotes (Bernecky et al., 2017) and exhibits the typical β-barrel fold in all available structures. Strikingly, hSpt5-KOW5 also exchanges with an unfolded species under non-denaturing conditions (Figure 5G), just as EcRfaH-KOW and VcRfaH-KOW. The magnitude of the differences between the minor species 15N chemical shifts and the predicted random coil values (Figure 6—figure supplement 4A) is similar to that observed for VcRfaH-KOW (Figure 6—figure supplement 3A). Interestingly, the minor species’ chemical shifts of a 13Cα -CEST of 13C,15N-hSpt5-KOW5 clearly indicate the absence of any substantial residual structure (Figure 6—figure supplement 4). In contrast to all other KOW domains in this study, hSpt5-KOW5 is not located at the very C-terminus of full-length hSpt5, but it is just one out of seven KOW domains being flanked by several hundreds of residues at either terminus. Thus, the stability of this domain may be different in its physiological environment. Taken together, this data suggests that hSpt5-KOW5 is a typical monomorphic β-barrel and that its decreased stability, accompanied by the existence of a minor, unfolded species, may be attributed to the absence of the neighboring domains, although we cannot completely rule out that these features are real, intrinsic properties of hSpt5-KOW5 in the full-length protein with (yet unknown) functional relevance.

As the completely unfolded state was only experimentally assigned for EcRfaH-KOW we will focus on this domain in the following analysis. Owing to its population of 5.5% (Table 5), EcRfaH-KOW’s minor species should be detectable in standard HSQC spectra, given a sufficiently high signal-to-noise ratio. As we observed a stable intermediate during the CD-based chemical unfolding of EcRfaH-KOW we aimed at analyzing the role of the minor species during the chemical denaturation of EcRfaH-KOW by recording [1H, 15N]- and [1H, 13C]-correlation spectra of [15N, 13C]-labeled EcRfaH-KOW in the presence of various urea concentrations (0–8 M) (Figure 6B and C). In both spectra series, we observed a decrease in peak intensity/volume of the β-barrel signals with increasing urea concentration (boxed regions in Figure 6B and C), which is completed at ≈ 4 M urea, indicating that the first transition in the far-UV CD-based chemical denaturation of EcRfaH-KOW (Figure 3F) corresponds to the unfolding of its β-barrel (tertiary) structure. This is also corroborated by near-UV CD spectroscopy-based chemical denaturation experiments using urea or GdmCl, respectively, (Figure 6—figure supplement 5A, B), which clearly show that the transition during the titration from 0 to ~3 M urea/~1 M GdmCl is accompanied by a loss in tertiary structure. The possibility that the resulting conformation corresponds to an equilibrium molten globule is, however, excluded due to its inability to bind 8-anilino-1-naphthalenesulfonic acid (ANS, Figure 6—figure supplement 5C).

In order to identify signals corresponding to the minor species in the HSQC spectra of EcRfaH-KOW, we started with the spectrum of the urea-unfolded protein (8 M urea, purple spectra in Figure 6B and C). Most of the corresponding signals shifted linearly with decreasing urea concentration and also lost intensity at urea concentrations <3 M (e.g. signal of S139 in Figure 6B and C). At 0 M urea, finally, only a set of weak signals remained, which we identified as signals of the minor species as these match the chemical shifts of the minor species identified in the CEST experiments (compare red and gray bars in Figure 6A, top/bottom panels). Based on the linear transition between the positions of the (urea) unfolded state toward the positions of the minor species signals, we conclude that addition of urea shifts the minor species’ population toward the completely unfolded state. Although we cannot assess if the minor species samples the completely unfolded state in the absence of any denaturant, the increased 15N R2 values indicate additional exchange processes of the minor species on the µs-ms time scale (Figure 6A, middle panel). Thus, we hypothesize that the minor species can be described as an ensemble of exchanging sub-states, some corresponding to the completely unfolded state ‘U’ and some exhibiting residual helical structure, hereby referred to as α-helical unfolding intermediate ‘Uα’ with the minor species observed in the CEST experiments being the average population under native conditions.

If this is true, the urea-induced chemical shift perturbations experienced by the minor species signals in the [1H, 15N]-HSQCs can be explained by a combination of two effects: (i) change of the chemical environment of the spins due to the presence of urea, which particularly affects δ 1H (see e.g. signal of T157 in Figure 6B), and (ii) change in the relative populations of the minor species’ sub-states toward the unfolded state, which mainly affects Δδ15N. Since the Hα/Cα chemical shifts are relatively independent of the solvent conditions, their perturbations in the urea denaturation series (Figure 6C) even better reflect the change in the ratio of the minor species’ sub-states. The shifting of the minor species’ peaks in Figure 6C is completed at ≈7 M urea, implying that the second transition in the far-UV CD-based unfolding experiment (Figure 3F) corresponds to the denaturation of Uα. Interestingly, the R2 values of residues in region 1 are more than twice as high as those of residues in region 2 (Figure 6A) and, in the [1H, 15N]-HSQC-based denaturation experiment (Figure 6B), the minor species’ signals of residues in region 1 do not shift in a linear manner as it is typical for two exchanging states. Instead, they show a curved transition that is ‘kinked’ at ≈ 2 M urea (see e.g. T131), implying a more complex unfolding process and thus structural heterogeneity of this region. Although our experiments do not allow a precise structural characterization of all states of the minor species, it may be described as an ensemble of largely unfolded, interconverting structures with states U and Uα constituting the extrema.

Due to the fast chemical exchange between the EcRfaH-KOW’s U and Uα states during the chemical denaturation, their relative populations in a certain titration step are encoded in the chemical shift of the minor species signal, whereas the volume of the minor species peak is proportional to the sum of the populations of both states (assuming similar transverse relaxation rates for the species). The chemical shifts of Cα/Hα groups depend to a much lower extent on the urea concentration in the sample than the chemical shifts of amide groups and therefore they provide better measures for the exchange between U and Uα. To first quantify the decay of the all-β conformation and the increase of the minor species during the urea denaturation, we analyzed the peak intensity of both species exemplarily for residue S139 in the [1H, 13C]-ctHSQC-based titration (Figure 6C and Figure 6—figure supplement 6A). The resulting ΔG value of ≈ 7 kJ/mol between the energy levels of major and minor species agrees well with the results from the CEST experiment (7 kJ/mol). Additionally, the m value of 3.4 kJ/(mol M) is very similar to the m values obtained for the other KOW domains by CD spectroscopy (Table 3), indicating that the minor species is indeed close to a completely unfolded state with a small buried surface area.

The complete denaturation of the minor species, that is, the transition of Uα to a fully unfolded state U, can be followed in the [1H, 13C]-ctHSQC-based denaturation experiment by analyzing the change of the minor species’s chemical shifts from the positions in the absence of urea toward those of the completely unfolded state. For example, the Hα/Cα correlation peaks of residues A137, S139, or M140, which are located in region 2, clearly shift from regions typical for α-helical structures (upfield 1H, downfield 13C relative to random coil values) to positions corresponding to an unstructured conformation (downfield 1H, upfield 13C), and finally they localize next to the signals of the Ala, Ser, or Met residues that do not reside in regions with residual helical structure (Figure 6C). Plotting the changes of the 13Cα chemical shifts of A137, S139, and M140 versus the urea concentration (Figure 6—figure supplement 6B) results in curves that resemble the second half of an unfolding transition (Uα ⇋ U) and approach the baseline of the fully unfolded state at ≈6 M urea. The absence of a baseline for Uα precludes a quantitative analysis, but it indicates that the transition mid-point of the curve is probably close to or below 0 M urea. In summary, the data of the NMR-based denaturation experiments (i) strongly support our hypothesis that the minor species identified in the CEST experiments is an ensemble of fast interconverting, mostly unfolded structures with U and Uα being the extrema and (ii) suggest that the minor species might be an important intermediate during the refolding process.

## Discussion

### Fold-switching is conserved among RfaH proteins

Genes coding for RfaH orthologs can be found in many bacterial pathogens, including Salmonella, Klebsiella, Vibrio, and Yersinia spp. (Carter et al., 2004). Despite their divergent evolution, RfaH proteins seem to have a conserved mechanism of action (Carter et al., 2004). To date, only EcRfaH was structurally characterized in detail, revealing that this protein has unique structural features classifying it as transformer protein (Belogurov et al., 2007; Burmann et al., 2012; Zuber et al., 2019). Here, we show that VcRfaH, an evolutionary quite divergent representative sharing 35.8% sequence identity with EcRfaH, exhibits very similar structural properties, that is, VcRfaH-KOW, like EcRfaH-KOW, folds as α-hairpin in the full-length protein, but adopts a NusG-type β-barrel conformation in its isolated form (Figure 1). Interestingly, in VcRfaH helix α3* is 1.5 turns longer as compared to EcRfaH and VcRfaH has a disulfide bridge connecting strand β3* and helix α3*, stabilizing this helix. These two features imply a stabilization of the domain interface and thus an increased affinity between the domains as compared to EcRfaH. This might also explain the increased stability of the isolated VcRfaH-KOW domain (≈14 kJ/mol), which compensates the higher energy gain of the domain interaction. Further, the increased stability of the VcRfaH-KOW domain may be the cause for the sigmoid-shaped CD-based chemical denaturation curves, in agreement with an apparent two-state unfolding process: global unfolding of the folded state occurs at higher denaturant concentrations, where potential partly structured folding intermediates are already largely destabilized and therefore escape detection. This conclusion is supported by the Trp fluorescence-based denaturation data (Figure 3—figure supplement 1), suggesting that the change in the CD signal is almost exclusively caused by the decay of the β-barrel conformation and that the contribution of Uα to the change of the CD signal is negligible. Nevertheless, we conclude that VcRfaH may be regulated by fold-switching just like EcRfaH, and that this metamorphic behavior is conserved in the class of RfaH proteins and may even be found in other NusG paralogs, in agreement with a recent study that predicts that nearly 25% of bacterial NusG proteins might perform α ↔ β transitions similar to EcRfaH (Porter et al., 2022).

### Model for the structural plasticity of RfaH

EcRfaH switches the conformation and function of its KOW domain in a reversible manner to achieve a tight control of gene expression (Zuber et al., 2019). In free EcRfaH, the α-helical hairpin conformation is the preferred state of EcRfaH-KOW, whereas domain separation or isolation of EcRfaH-KOW fosters population of the all-β state in solution (Burmann et al., 2012), suggesting that the all-α conformation is intrinsically unstable, but becomes the thermodynamic minimum in free EcRfaH due to interaction with EcRfaH-NGN.

Interestingly, our thermodynamic analysis (Figures 2 and 3) of the isolated EcRfaH-KOW domain reveals that, although the all-β conformation is the preferred state in isolation, it is only marginally stable, and it is in rapid equilibrium with an ‘unfolded’ state, which is populated to a significant extent, even under physiological conditions. The ‘unfolded’ state is a mixture of random-coil-type unfolded species U and species Uα containing two helical regions.

Based on our results, we suggest a model for the structural transitions of EcRfaH-KOW (Figure 7).

![Figure 7.](https://cdn.elifesciences.org/articles/76630/elife-76630-fig7-v2.jpg)

**Figure 7.:** Qualitative Gibbs free energy level diagram and associated structures for the all-α to all-β transition of EcRfaH-KOW and vice versa. In its ground state, that is, the autoinhibited conformation, the energy of the all-α conformation of EcRfaH-KOW is strongly lowered by the extensive inter-domain contacts with the EcRfaH-NGN domain. Upon recruitment, the domains dissociate, the helical structure of the released KOW domain becomes destabilized in isolation, and rapidly decays toward an ensemble of mainly unfolded sub-states that interconvert on the µs time scale. Some of the sub-states correspond to the completely unfolded state (U) whereas others retain some residual (α-) helical elements (Uα). The scheme displays exemplary structures of these sub-states. Due to their fast structural interconversion, U and Uα may be grouped into a single macro-state/ensemble (as is the case during the chemical exchange saturation transfer [CEST] experiments) that exhibits helical structures for a limited amount of time and is otherwise unfolded. Uα is either marginally stable or even unstable (therefore, its energy level is blurred). The disordered conformation then allows for easy and rapid refolding to the all-β conformation. Due to their low thermodynamic stability, or even instability of all-β and Uα, respectively, the last two steps are reversible, that is, the all-α state can be rapidly regained when the EcRfaH-NGN domain becomes available for re-association after transcription termination.

In the autoinhibited state the all-α conformation of EcRfaH-KOW corresponds to the minimum of the Gibbs free energy as it is stabilized by contacts to the EcRfaH-NGN. During recruitment of EcRfaH to an ops-paused elongation complex, the EcRfaH-NGN:KOW interface is destabilized (most probably via an encounter complex), the domains dissociate and EcRfaH-NGN is sequestered to RNAP (Zuber et al., 2019). The freed all-α EcRfaH-KOW is not stable as G increases due to the loss of EcRfaH-NGN contacts. Consequently, EcRfaH-KOW unfolds, resulting in an ensemble of rapidly interconverting sub-states. Some of these sub-states still contain two residual α-helical regions (intermediate Uα) that correspond to the tip of the α-hairpin in the all-α state, in agreement with hydrogen/deuterium exchange data, which indicate that the hairpin tip is the most stable part of the all-α conformation (Galaz-Davison et al., 2020). Other sub-states represent the completely unfolded protein, which then rapidly refolds into the all-β form. Upon transcription termination EcRfaH is released, and the process is reversed with unfolding of the β-barrel starting, most probably, by detaching β1 and β4/β5 from the central strands as the corresponding H-bonds are the least stable ones (Figure 4). The U state is in equilibrium with Uα, where two α-helical regions that will later constitute the α-hairpin tip are formed transiently and may thus serve both as the nucleation point for the completion of the all-α structure and as starting point for recognition of its cognate binding site on the NGN. This mechanism ensures rapid re-autoinhibition and prevents aggregation of EcRfaH. Although we did not analyze VcRfaH as extensively as EcRfaH, our results suggest that the VcRfaH-KOW domain most likely employs a similar mechanism for its structural transformation, indicating that the presented model is a general scheme for RfaH proteins.

In support of our model, all computational studies on EcRfaH found that the all-α conformation is stable only when in contact with the NGN. Modification of the strength of the EcRfaH-NGN:KOW interface (Ramírez-Sarmiento et al., 2015) or deletion of the linker (Xun et al., 2016) destabilizes the all-α fold and ultimately drives EcRfaH-KOW into the β-barrel state. Moreover, the β-barrel fold is stable and corresponds to or is close to the energy minimum of the energy landscape of EcRfaH-KOW, whereas the all-α fold rapidly unfolds and has a higher G value than the all-β state (Balasco et al., 2015; Bernhardt and Hansmann, 2018; Gc et al., 2014; Joseph et al., 2019; Li et al., 2014; Xiong and Liu, 2015). Apart from these general concepts, most studies differ in several key points, such as the extent to which the all-α state is populated in the isolated EcRfaH-KOW, or the precise folding pathway from all-α to all-β. Strikingly, a recent bioinformatical study very nicely mirrors our data as the authors also observed a significant portion of transiently formed helical structure within the unfolded state ensemble in their simulations (Seifi and Wallin, 2021).

### Requirements for fold-switching proteins

Previous work on designed and naturally occurring fold-switching proteins has identified several specific properties that make fold-switching proteins distinct from others (Bryan and Orban, 2010; Porter and Looger, 2018). In this study, we show that RfaH meets all these requirements and is thus a showcase example for fold-switching proteins:

### Fold-switching is a highly efficient principle of regulation with a steadily increasing importance

To date, about six fold-switching proteins have been studied in detail (summarized in Dishman and Volkman, 2018; Lella and Mahalakshmi, 2017; Zamora-Carreras et al., 2020), but estimates suggest that up to 4% of the proteins in the PDB may have the ability to switch folds (Porter and Looger, 2018). Our study demonstrates which molecular mechanisms confer RfaH its structural plasticity that allows operon-specific regulation without competing with its monomorphic paralog NusG/Spt5. In line with our findings, a recent study on XCL1, another model system for fold-switching proteins, identified very similar principles for the evolution and design of fold-switching proteins (Dishman et al., 2021).

### Importance of a chiefly unfolded state in protein fold-switching

In summary, our results highlight two key features in protein fold-switching: decreased thermodynamic stability and defined local structures in ‘unfolded’ intermediates. Diminished stability is often thought to be detrimental for proteins as it favors non-native contacts and promotes aggregation. However, it is essential to confer fold-switching proteins their conformational plasticity, and, as all transitions from and to the unfolded states are very fast, and the population of these states is rather low, fold-switchers can evade aggregation. Further, the capability of the ‘unfolded’ state to harbor residual defined structures, for example, α-helices, allows to pre-encode a second conformation that could be readily adopted upon a molecular signal.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>strain, strain background</td>
      <td>Escherichia coli BL21(DE3)</td>
      <td>Novagen</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>recombinant DNA reagent</td>
      <td>List of recombinant plasmids used</td>
      <td>Table 7</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>List of primers used</td>
      <td>Table 6, Biolegio</td>
      <td>PCR primers</td>
      <td></td>
    </tr>
    <tr>
      <td>peptide, recombinant protein</td>
      <td>V. cholerae RfaH</td>
      <td>This work</td>
      <td></td>
      <td>See Materials and methods, section ‘Production of recombinant proteins’</td>
    </tr>
    <tr>
      <td>peptide, recombinant protein</td>
      <td>V. cholerae RfaH-KOW</td>
      <td>This work</td>
      <td></td>
      <td>See Materials and methods, section ‘Production of recombinant proteins’</td>
    </tr>
    <tr>
      <td>peptide, recombinant protein</td>
      <td>E. coli RfaH-KOW</td>
      <td>Burmann et al., 2012 doi:10.1016/j.cell.2012.05.042</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>peptide, recombinant protein</td>
      <td>E. coli NusG-KOW</td>
      <td>Burmann et al., 2010 doi: 10.1126/science.1184953</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>peptide, recombinant protein</td>
      <td>M. tuberculosis NusG-KOW</td>
      <td>Strauß et al., 2016 doi: 10.1080/07391102.2015.1031700</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>peptide, recombinant protein</td>
      <td>M. janaschii Spt5-KOW</td>
      <td>This work</td>
      <td></td>
      <td>See Materials and methods, section ‘Production of recombinant proteins’</td>
    </tr>
    <tr>
      <td>peptide, recombinant protein</td>
      <td>Human Spt5-KOW5 (G699-G754)</td>
      <td>This work</td>
      <td></td>
      <td>See Materials and methods, section ‘Production of recombinant proteins’</td>
    </tr>
    <tr>
      <td>commercial assay or kit</td>
      <td>QIAquick Gel Extraction Kit</td>
      <td>Qiagen</td>
      <td>Cat#: 28706</td>
      <td></td>
    </tr>
    <tr>
      <td>commercial assay or kit</td>
      <td>QIAprep Spin Miniprep Kit</td>
      <td>Qiagen</td>
      <td>Cat#: 27106</td>
      <td></td>
    </tr>
    <tr>
      <td>chemical compound, drug</td>
      <td>(15NH)4SO4</td>
      <td>Sigma/Merck KGaA</td>
      <td>Cat#: CS01-185_148</td>
      <td></td>
    </tr>
    <tr>
      <td>chemical compound, drug</td>
      <td>D2O</td>
      <td>Euriso-Top GmbH</td>
      <td>Cat#: 7789-20-0</td>
      <td></td>
    </tr>
    <tr>
      <td>chemical compound, drug</td>
      <td>13C-D-glucose</td>
      <td>Euriso-Top GmbH</td>
      <td>Cat#: CLM-1396–10</td>
      <td></td>
    </tr>
    <tr>
      <td>chemical compound, drug</td>
      <td>Urea</td>
      <td>Carl Roth GmbH &amp; Co. KG</td>
      <td>Cat#: 2317.1</td>
      <td></td>
    </tr>
    <tr>
      <td>chemical compound, drug</td>
      <td>GdmCl</td>
      <td>Carl Roth GmbH &amp; Co. KG</td>
      <td>Cat#: 0037.1</td>
      <td></td>
    </tr>
    <tr>
      <td>chemical compound, drug</td>
      <td>DSS</td>
      <td>Sigma</td>
      <td>Cat#: T-8636</td>
      <td></td>
    </tr>
    <tr>
      <td>chemical compound, drug</td>
      <td>ANS</td>
      <td>Sigma/Merck KGaA</td>
      <td>Cat#: 10417–5G-F</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>Fit-o-Mat v0.752</td>
      <td>Möglich, 2018 doi: 10.1021/acs.jchemed.8b00649</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>PyMol v. 1.7</td>
      <td>The PyMOL Molecular Graphics System, Schrödinger, LLC</td>
      <td>https://pymol.org/2/</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>NMRViewJ</td>
      <td>One Moon Scientific, Inc</td>
      <td>http://www.onemoonscientific.com/nmrviewj</td>
      <td></td>
    </tr>
    <tr>
      <td>software, algorithm</td>
      <td>ChemEx v. 0.6.1</td>
      <td>Vallurupalli et al., 2012 doi:10.1021/ja3001419</td>
      <td>https://github.com/gbouvignies/ChemEx</td>
      <td></td>
    </tr>
    <tr>
      <td>other</td>
      <td>Quartz cuvette for CD spectroscopy, 1 mm</td>
      <td>Hellma GmbH &amp; Co. KG</td>
      <td></td>
      <td>See Materials and methods, section ‘CD spectroscopy’</td>
    </tr>
    <tr>
      <td>other</td>
      <td>Quartz cuvette for CD spectroscopy, 2 mm</td>
      <td>Hellma GmbH &amp; Co. KG</td>
      <td></td>
      <td>See Materials and methods, section ‘CD spectroscopy’</td>
    </tr>
    <tr>
      <td>other</td>
      <td>Quartz cuvette for fluorescence spectroscopy, 1 cm</td>
      <td>Hellma GmbH &amp; Co. KG</td>
      <td></td>
      <td>See Materials and methods, section ‘Fluorescence spectroscopy’</td>
    </tr>
  </tbody>
</table>

**Table 6.**
 Primers used for cloning.


<table>
  <thead>
    <tr>
      <th>Primer</th>
      <th>Sequence (5’ → 3’)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Fw-VcRfaH-KOW</td>
      <td>CAT GCC ATG GGA GAG CAA TTG AAG CAT GCC AC</td>
    </tr>
    <tr>
      <td>Rv-VcRfaH-KOW</td>
      <td>CGC GGA TCC TTA GGT GAC TTC CCA ATC GG</td>
    </tr>
    <tr>
      <td>Fw-hSpt5-KOW5</td>
      <td>CAT GCC ATG GGC CGG AGG GAC AAC GAA CTC ATC GG</td>
    </tr>
    <tr>
      <td>Rv-hSpt5-KOW5</td>
      <td>TAG AAT TCT CAG CCC ACC GTG GTG AGC CGC TG</td>
    </tr>
    <tr>
      <td>Fw-MjSpt5-KOW</td>
      <td>AT GCC ATG GGT AAG AAA ATC ATT GAA AAT ATT GAG AAA GG</td>
    </tr>
    <tr>
      <td>Rv-MjSpt5-KOW</td>
      <td>CGG AAT TCT TAA TCT TTA TGC TTT GAA ACT ATT TTA AC</td>
    </tr>
  </tbody>
</table>

**Table 7.**
 Plasmids.


<table>
  <thead>
    <tr>
      <th>Plasmid</th>
      <th>Description</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>pVS13</td>
      <td>rfaH from V. cholera in pTYB1</td>
      <td>I Artsimovitch</td>
    </tr>
    <tr>
      <td>pHC301</td>
      <td>rfaH from V. cholera in pIA238 (a pET28 derivative) Artsimovitch and Landick, 2002</td>
      <td>Carter et al., 2004</td>
    </tr>
    <tr>
      <td>pETGb1a-VcRfaH-KOW</td>
      <td>rfaH103-165 from V. cholera in pETGb1a</td>
      <td>This work</td>
    </tr>
    <tr>
      <td>pETGb1a-hSpt5-KOW5</td>
      <td>human spt5699-754 in pETGb1a</td>
      <td>This work</td>
    </tr>
    <tr>
      <td>pETGb1a-MjSpt5-KOW</td>
      <td>spt5583-147 from M. janaschii in pETGb1a</td>
      <td>This work</td>
    </tr>
    <tr>
      <td>pOTB7_huSUPT5H</td>
      <td>cDNA plasmid containing human spt5</td>
      <td>Zuber et al., 2018</td>
    </tr>
    <tr>
      <td>pGEX-2TK_MjSpt5-KOW</td>
      <td>spt5583-147 from M. janaschii in pGEX-2TK</td>
      <td>Hirtreiter et al., 2010</td>
    </tr>
    <tr>
      <td>pETGb1a-EcNusG-KOW</td>
      <td>nusG123-181 from E. coli in pETGb1a</td>
      <td>Burmann et al., 2010</td>
    </tr>
    <tr>
      <td>pET101d-MtNusG-KOW</td>
      <td>nusG178-238 from M. tuberculosis in pET101d</td>
      <td>Strauß et al., 2016</td>
    </tr>
    <tr>
      <td>pETGb1a-EcRfaH-KOW</td>
      <td>rfaH101-162 from E. coli in pETGb1a</td>
      <td>Burmann et al., 2012</td>
    </tr>
  </tbody>
</table>

### Cloning

The VcRfaH expression vector pVS13 (V. cholerae rfaH from pHC301 (Carter et al., 2004) in plasmid pTYB1 [NEB]) was a gift from I Artsimovitch, The Ohio State University, Columbus, OH. The C-terminal VcRfaH residue, Thr165, is substituted by an Ala to ensure efficient cleavage of the resulting chitin binding domain (CBD) intein fusion protein (see below). Expression plasmids for VcRfaH-KOW (residues E103-T165), hSpt5-KOW5 (residues G699-G754), and MjSpt5-KOW (residues K83-D147) were created by cloning of the corresponding gene regions into vector pETGb1a (G Stier, EMBL, Heidelberg, Germany) via NcoI and BamHI (VcRfaH-KOW), or NcoI and EcoRI (hSpt5-KOW5 and MjSpt5-KOW) restriction sites, respectively. Templates for PCR amplification were plasmids pHC301 (Carter et al., 2004) for VcRfaH-KOW, pOTB7_huSUPT5H (Zuber et al., 2018) for hSpt5-KOW5, and pGEX-2TK_MjSpt5-KOW (Hirtreiter et al., 2010); kindly provided by F Werner, University College London, UK for MjSpt5-KOW. The primers used for cloning are listed in Table 6. All plasmids used in this study are listed in Table 7.

### Production of recombinant proteins

VcRfaH was obtained from a CBD intein fusion protein encoded in plasmid pVS13, with expression conditions and purification strategy as described for E. coli RfaH (Vassylyeva et al., 2006). EcNusG-KOW and MtNusG-KOW were produced as previously described (Burmann et al., 2010; Strauß et al., 2016). MjSpt5-KOW, hSpt5-KOW5, EcRfaH-KOW, and VcRfaH-KOW were obtained from Gb1 fusions with expression and purification conditions similar to that of EcRfaH-KOW (Burmann et al., 2012).

The quality of all recombinantly produced proteins was ensured according to the guidelines established by ARBRE-MOBIEU and P4EU (https://arbre-mobieu.eu/guidelines-on-protein-quality-control/) (de Marco et al., 2021). In brief, purity was checked by sodium dodecyl sulfate polyacrylamide gel electrophoresis, the absence of nucleic acids by UV spectroscopy, the identity by mass spectrometry and/or NMR spectroscopy, the folding state by CD and/or NMR spectroscopy, and the absence of aggregation by analytical gel filtration or dynamic light scattering.

### Isotopic labeling of proteins

For the production of 15N- and 15N, 13C-labeled proteins, E. coli cells were grown in M9 medium (Green et al., 2012; Meyer and Schlegel, 1983) containing (15NH4)2SO4 (Sigma/Merck KGaA, Darmstadt, Germany) or (15NH4)2SO4 and 13C-D-glucose (Euriso-Top GmbH, Saarbrücken, Germany), respectively, as sole nitrogen or carbon sources. Deuteration was achieved by accustoming cells to M9 medium prepared with increasing concentrations of D2O (0%, 50%, 100% (v/v); Euriso-Top GmbH, Saarbrücken, Germany). Expression and purification protocols were identical to those of the unlabeled proteins.

### NMR spectroscopy

NMR experiments were conducted at Bruker Avance 600, Avance 700, Ascend Aeon 900, and Ascend Aeon 1000 spectrometers, each equipped with room temperature (Avance 600) or cryogenically cooled, inverse 1H, 13C, 15N triple resonance probes (all other spectrometers). All measurements were conducted in 5 mm tubes with a sample volume of 550 µl at 25°C, if not stated otherwise. NMR data was processed using in-house software and analyzed using NMRViewJ (OneMoon Scientific).

Backbone resonance assignments for VcRfaH, VcRfaH-KOW, hSpt5-KOW5, MjSpt5-KOW, and urea-unfolded EcRfaH-KOW were obtained using standard band-selective excitation short transient (Lescop et al., 2007; Schanda et al., 2006) transverse relaxation optimized spectroscopy (TROSY)-based triple resonance experiments (Pervushin et al., 1997; Salzmann et al., 1998). Additionally, carbon-detected CACO, CAN, and NCO experiments (Bermel et al., 2005) were recorded for VcRfaH-KOW. Side chain assignments for VcRfaH-KOW were obtained from CCH- and H(C)CH-TOCSY, HBHA(CO)NH, C(CO)NH, aromatic [1H, 13C]-HSQC, and 13C-edited aromatic nuclear overhauser enhancement spectroscopy (NOESY) experiments (Sattler et al., 1999). Three-dimensional assignment and NOESY experiments were acquired using a non-uniform sampling scheme with a sparsity of 25–50%. Spectra were subsequently reconstructed with in-house written software using the iterative soft thresholding algorithm (Hyberts et al., 2012). The EcRfaH-KOW, VcRfaH-KOW, hSpt5-KOW5, and MjSpt5-KOW samples contained 0.5–1 mM [15N, 13C]-labeled protein in 20 mM Na-phosphate (pH 6.5), 100 mM NaCl, 1 mM ethylenediaminetetraacetic acid (EDTA), 10% (v/v) D2O. The EcRfaH-KOW sample further contained 6 M urea. Due to limited sample stability and poor quality of the initial spectra, VcRfaH (0.3 mM) was [2H, 15N, 13C]-labeled and in an optimized buffer (25 mM Bis-Tris-Propane [pH 6.5], 25 mM Na-Tartrate, 50 mM NaCl, 10% (v/v) D2O) and the measurements were conducted at 20°C. The Cα and CO secondary chemical shift for VcRfaH was calculated as difference between the observed chemical shift and the predicted random coil value (Wishart and Sykes, 1994) using a deuterium correction as given in Venters et al., 1996. Chemical shift assignments for EcNusG-KOW, MtNusG-KOW, and native EcRfaH-KOW were taken from previous studies (Burmann et al., 2012; Mooney et al., 2009; Strauß et al., 2016). The random coil chemical shifts for characterization of the minor species in case of VcRfaH-KOW and hSpt5-KOW were calculated using the Poulsen IDP/IUP random coil chemical shifts calculator tool (https://spin.niddk.nih.gov/bax/nmrserver/Poulsen_rc_CS/).

Distance restraints for the structure calculation of VcRfaH-KOW were obtained from standard 13C- and 15N-edited 3D NOESY experiments (Sattler et al., 1999) with mixing times of 120 ms. NOESY cross-signals were classified according to their intensities and converted to distance restraints with upper limits of 3 Å (strong), 4 Å (medium), 5 Å (weak), and 6 Å (very weak), respectively. Hydrogen bonds were identified from corresponding experiments (see below). Psi/Phi angle restraints were obtained from the geometry dependence of the backbone chemical shifts using TALOS (Cornilescu et al., 1999). The structure calculation was performed with XPLOR-NIH version 2.1.2 using a three-stage simulated annealing protocol with floating assignment of prochiral groups including a conformational database potential (Schwieters et al., 2003). Structures were analyzed with XPLOR-NIH and PROCHECK-NMR (Laskowski et al., 1996).

15N-based CEST experiments were conducted according to Vallurupalli et al., 2012. All samples contained ≈0.7–1 mM 15N-labeled protein. For initial CEST experiments, the domains were in 20 mM HEPES (pH 7.5), 100 mM NaCl, 10% (v/v) D2O, and a single CEST B1 field (ν1=18–25 Hz) during an exchange period of 500 ms was employed. Proteins showing an exchange peak in their CEST profiles were further studied in 20 mM Na-phosphate (pH 6.5), 100 mM NaCl, 1 mM EDTA, 10% (v/v) D2O to decrease amide proton-H2O exchange. CEST experiments were then recorded using two different B1 fields (ν1=13 Hz/26 Hz) and an exchange period of 500 ms. The B1 frequencies were calibrated using a 1D approach on an isolated signal (Guenneugues et al., 1999). The CEST traces obtained at 13/26 Hz were fitted simultaneously according to a two-state exchange model using ChemEx (version 0.6.1, Vallurupalli et al., 2012). Due to the monodisperse distribution of the resulting kex/pB values (Table 5), the CEST traces were then fitted globally, yielding a global kex and pB value. Only those CEST profiles were included in the global fit that showed a Δω>1 ppm. 13Cα-CEST experiments were recorded on [15N, 13C]-labeled protein samples using a [1H, 13C] constant-time (ct) HSQC-based approach (Bouvignies et al., 2014). To maximize the number of analyzable signals, the proteins were in 20 mM Na-phosphate (pH 6.5), 100 mM NaCl, 1 mM EDTA, 99.9% (v/v) D2O (pH uncorrected for D2O). In this case, the chemical shift was referenced via 0.5 mM internal DSS. The experiment was performed at a single B1 field strength (25 Hz) at an exchange period of 500 ms. The CEST traces obtained for [1H, 13C]-EcRfaH-KOW were fitted with ChemEx.

NMR-based chemical denaturation experiments of the KOW domains were done by recording [1H, 15N]-HSQC and [1H, 13C]-ctHSQC spectra of 80 μM [15N, 13C]-EcRfaH-KOW in 20 mM Na-phosphate (pH 6.5), 100 mM NaCl, 1 mM EDTA, 10% (v/v) D2O buffer containing 0–8 M urea. The chemical shifts were referenced to 0.5 mM internal DSS.

For the NMR-based refolding experiment of VcRfaH under reducing conditions a [1H, 15N]-HSQC spectrum of 15N-VcRfaH in refolding buffer (50 mM Na-phosphate [pH 6.5], 50 mM NaCl, 2 mM DTT) was recorded before the protein was incubated in refolding buffer containing 8 M urea for 24 hr. Having recorded another [1H, 15N]-HSQC spectrum urea was removed by stepwise dialysis against 4 l of refolding buffer containing 4, 2, 1, 0.5, and 0 M urea, respectively (2–4 hr for the first four steps and over-night for the last step). Finally, a [1H, 15N]-HSQC spectrum of the refolded protein was recorded.

Hydrogen bonds were identified from 2D or 3D long-range TROSY-based HNCO experiments as previously described (Cordier et al., 2008). All samples contained [15N, 13C]-labeled proteins at 0.7–1 mM in 20 mM Na-phosphate (pH 6.5), 100 mM NaCl, 1 mM EDTA, 10% (v/v) D2O.

### CD spectroscopy

CD data were collected at a Jasco J-1100 spectrometer (Jasco Deutschland GmbH, Pfungstadt, Germany), using quartz cuvettes (Hellma GmbH & Co. KG, Müllheim, Germany). CD spectra were normalized (Equation 1) to obtain the mean residue-weighted ellipticity (ΘMRW):

$$
Θ_{MRW}=\frac{100⋅\theta}{N⋅c⋅d}
$$

θ is the ellipticity in mdeg, N the number of amino acids, c the protein concentration in mM, and d the pathlength of the cuvette in cm.

Thermal unfolding and refolding curves were obtained by measuring the CD signal of 15 μM (≈0.1 mg/ml) protein buffered by either 10 mM K-phosphate (pH 7.0) or 10 mM K-acetate (pH 4.0), respectively, in a 1 cm quartz cuvette upon heating to 95°C and subsequently re-cooling to the initial temperature. The scan speed was 1°C/min, the dwell time 1 min, and the integration time 4 s. Checking the reversibility of thermal unfolding and determination of the wavelength used for temperature transition curves was done by recording far-UV CD spectra at 25°C, then 95°C, and after subsequent re-cooling to 25°C in a 1 mm pathlength cuvette using 25 μM protein solutions in either 10 mM K-phosphate (pH 7.0) or 10 mM K-acetate (pH 4.0). The wavelength to follow a thermal transition corresponds to the wavelength >215 nm with the largest difference in the CD signal between folded and unfolded state and was chosen for each transition individually. Using wavelengths <215 nm led to noisy signals at high temperatures and resulted in non-interpretable data.

Changes in ellipticity (θ) upon thermal unfolding were analyzed with a two-state model using Fit-o-Mat version 0.752 (Möglich, 2018) to obtain the melting temperature (Tm) and enthalpy change at Tm (ΔHu(Tm)) of the transition (both fit parameters) (Equation 2):

$$
\theta=f_{N}⋅(y_{N}+m_{N}⋅(T−T_{m}))+(1−f_{N})⋅(y_{U}+m_{U}⋅(T−T_{m}))
$$

with T being the absolute temperature in K, yN and yU the y-intercepts, and mN and mU the slopes of the N- and U-state baselines, respectively. fN is the fraction of folded molecules, which is related to the equilibrium constant Ku according to Equation 3:

$$
f_{N}=\frac{1}{1+K_{u}}
$$

Finally, Ku is related to the change in Gibbs free energy of the unfolding reaction (ΔGu) and ΔHu(Tm) by Equation 4:

$$
K_{u}=e^{−ΔG_{u}/(RT)}withΔG_{u}=ΔH_{u}(T_{m})−\frac{T}{T_{m}}⋅ΔH_{u}(T_{m})
$$

where R is the ideal gas constant.

CD-based chemical equilibrium unfolding experiments were performed at 25°C. Urea (BioScience Grade; ≈10 M) and GdmCl (≈8 M; both from Carl Roth GmbH & Co. KG, Karlsruhe, Germany) stock solutions were prepared according to Pace et al., 1990. Far-UV CD unfolding experiments were conducted using a 1 mm cuvette. All points of the unfolding curves were obtained from individual samples, each containing 40–60 μM (≈0.25–0.4 mg/ml) protein in either 10 mM K-phosphate (pH 7.0) or 10 mM K-acetate (pH 4.0), respectively. All samples were equilibrated over-night. The denaturant concentration of each sample was determined refractrometrically after CD data acquisition.

As for the thermal transitions, the wavelength to follow a chemical denaturation corresponds to the wavelength >215 nm with the largest difference in the CD signal between folded and unfolded state and was chosen for each transition individually (wavelengths <215 nm led to noisy signals and non-interpretable data at high denaturant concentrations).

Unfolding curves that indicate a two-state transition were analyzed using the linear extrapolation method (Santoro and Bolen, 1988) with Fit-o-Mat version 0.752 (Möglich, 2018) to obtain ΔGu(H2O) and the m value (Equation 5):

$$
S= f_{N}∙y_{N}+m_{N}∙denat+1-f_{N}∙y_{U}+m_{U}∙denat
$$

where S is the signal derived from far-UV CD spectroscopy (i.e. the ΘMRW value), intrinsic Trp fluorescence (for VcRfaH-CTD), or the normalized peak volumes of the [1H, 13C]-ctHSQC major/minor species signals for EcRfaH-KOW residue S139, respectively. [denat] is the denaturant (i.e. urea or GdmCl) concentration in M, yN and yU are the y-intercepts, and mN and mU, the slopes of the N- and U-state baselines, respectively. fN is given by Equation 3. In this case, Ku is defined as (Equation 6):

$$
K_{u}=e^{−ΔG/(RT)}withΔG=ΔH(H_{2}O)−m⋅[denat]
$$

Finally, the [denat]1/2 value is obtained by (Equation 7):

$$
[denat]_{\frac{1}{2}}=\frac{ΔG(H_{2}O)}{m}
$$

Near-UV CD unfolding experiments of EcRfaH-KOW were conducted using a 1 cm quartz cuvette and 0.5 mM protein in 10 mM K-phosphate (pH 7.0). As the exchange between folded and unfolded state is reasonably fast (kex ≈ 15 s–1 at 0 M urea/GdmCl), all points were obtained from a titration of the initial denaturant-free protein sample with a 10 M urea or 8 M GdmCl solution in 10 mM K-phosphate (pH 7.0). The sample was then incubated for 5 min at 25°C to reach equilibrium. Curves were smoothed mathematically using a Savitzky-Golay filter.

To probe reversibility of chemical unfolding and validate incubation times used to reach equilibrium, proteins were dialyzed against 20 mM NH4HCO3 (pH 7.0) buffer, shock-frozen, lyophilized, and subsequently solved in 10 mM K-phosphate (pH 7.0) or 10 mM K-acetate (pH 4.0) with or without 10 M urea/8 M GdmCl, respectively. CD samples containing the identical denaturant concentration (1–2 samples in pre-transition region, 1 at [denat]1/2, 1 in post-transition region) were then prepared from the native or unfolded proteins. All samples were equilibrated over-night; far-UV CD spectra were then recorded using a 1 mm quartz cuvette.

### Fluorescence spectroscopy

Fluorescence spectra were recorded at 25°C using a Peltier-controlled Fluorolog-3 fluorimeter (Horiba Europe GmbH, Oberursel, Germany) equipped with a 1 cm quartz cuvette (Hellma GmbH & Co. KG, Müllheim, Germany). Samples for chemical denaturation of VcRfaH-KOW contained ≈11 μM protein and were prepared as described for the far-UV CD samples. The VcRfaH-KOW Trp residue was excited at 295 nm; emission spectra were then recorded from 300 to 400 nm with slit widths between 2.65/2.65 and 2.8/2.8 nm (excitation/emission) and an integration time of 0.2 s. Analysis of the resulting denaturation curve was performed as described for CD data.

ANS (Sigma/Merck KGaA, Darmstadt, Germany) interaction experiments were conducted by preparing a urea denaturation series of EcRfaH-KOW (final concentration: 5 μM) as described for the CD-based unfolding experiments, equilibrating over-night and adding ANS at a fluorophore:protein ratio of 100:1. Fluorescence spectra were then recorded from 410 to 650 nm following excitation at 395 nm with slit widths of 2.6/2.6 nm (excitation/emission) and 0.1 s integration time. A control experiment was conducted with identical experiment and instrument setup, respectively, but samples lacking protein. The obtained fluorescence at a given wavelength was then plotted against the urea concentration of the respective sample.

### Differential scanning calorimetry

The KOW domains were in either 10 mM K-acetate (pH 4.0; hSpt5-KOW5) or 10 mM K-phosphate (pH 7.0; all other domains), respectively. Given a lack of Trp residues in most domains, the protein concentration was determined via absorption at 205 nm using the molar extinction coefficient (ε205) as calculated by the Protein Calculator tool (Anthis and Clore, 2013).

Initial DSC experiments were carried out on a MicroCal VP-DSC instrument (MicroCal/Malvern Panalytical, Malvern, UK; active volume: 509 µl). The samples were vacuum degassed at room temperature just before the measurements. Prior to the protein-buffer scans, several buffer-buffer scans were performed. All thermograms were recorded at a scan rate of 1.5 K/min under an excess pressure of 30 psi in passive feed-back mode from ≈10°C to 110°C or 130°C (MjSpt5-KOW5), respectively. The unfolding was calometrically reversible for EcNusG-KOW, MtNusG-KOW, MjSpt5-KOW, and EcRfaH-KOW (data not shown). hSpt5-KOW5 aggregated at pH 7.0 upon unfolding at all tested concentrations, whereas VcRfaH-KOW aggregated at concentrations >0.2 mg/ml.

We repeated the measurements for all proteins but MtNusG-KOW using a MicroCal VP-Capillary DSC instrument (Malvern Panalytical, Malvern, UK; active volume 137 µl). The thermograms were obtained at a heating rate of 1.5 K/min with excess pressure (30 psi) and at mid gain feed-back mode. Buffer-buffer runs were done prior to the protein measurements. Thermograms were recorded from ≈5°C to 130°C. The protein concentration was 0.2–1 mg/ml for EcNusG-KOW, 0.25–1 mg/ml for MjSpt5-KOW, 0.15–0.25 mg/ml for hSpt5-KOW5, 0.2–1 mg/ml for EcRfaH-KOW, and 0.1–0.15 mg/ml for VcRfaH-KOW. The measurement for hSpt5-KOW5 was carried out with 10 mM K-acetate (pH 4.0), all other KOW domains were in 10 mM K-phosphate (pH 7.0).

The obtained raw DSC data (VP-DSC data for MtNusG-KOW, VP-Capillary DSC data for all other KOW domains) was scan rate normalized, the corresponding buffer-buffer baseline was subtracted, and the thermograms were then normalized to 1 mol of protein. To extract the thermodynamic parameters, the data was fitted to a two-state unfolding model including a temperature-dependent change in heat capacity from native to unfolded state (Viguera et al., 1994). The temperature dependence of the native state heat capacity (Cp,0) is assumed to be linear (Equation 8; note that Cp,0 contains an instrument-specific offset), whereas the difference in heat capacity to the unfolded state (ΔCp,u(T)) is approximated by a parabolic function (Equation 9):

$$
C_{p,0}=a_{0}+b_{0}∙T
$$



$$
ΔC_{p,u}T=a+b∙T+c∙T^{2}
$$

The value for the pre-factor of the quadratic term, c, was obtained by calculating the theoretical partial molar heat capacity, Cp(T), of the unfolded state for each of the six protein domains at 5°C, 25°C, 50°C, 75°C, 100°C, and 125°C, respectively, according to Makhatadze and Privalov, 1990. Then, the values for Cp(T) were plotted over the temperature and a parabolic function was fitted, yielding c.

The concentration-normalized heat capacity (Cp) then is the sum of Cp,0, the change of the ‘internal’ heat capacity that depends on the fraction of the protein in the folded and unfolded state (i.e. the equilibrium constant Ku), δCpint, and the excess heat absorption of the unfolding reaction δCpexc (Equation 10):

$$
C_{p}=C_{p,0}+\deltaC_{p}^{int}+\deltaC_{p}^{exc}
$$

With δCpint and δCpexc given in Equation 11:

$$
\deltaC_{p}^{int}=ΔC_{p,u}⋅\frac{K_{u}}{1+K_{u}}and\deltaC_{p}^{exc}=\frac{(ΔH_{u}(T))^{2}}{RT^{2}}⋅\frac{K_{u}}{(1+K_{u})^{2}}
$$

Ku is related to the change in Gibbs energy of the unfolding reaction (ΔGu(T)) by (Equation 12):

$$
K_{u}=e^{−ΔG_{u}(T)/(RT)}withΔG_{u}(T)=ΔH_{u}(T)−T⋅ΔS_{u}(T)
$$

The temperature-dependent enthalpy and entropy change (ΔHu(T), and ΔSu(T), respectively) are given by Equations 13 and 14:

$$
ΔH_{u}(T)=ΔH_{u}(T_{m})+a⋅(T−T_{m})+\frac{b}{2}⋅(T^{2}−T_{m}^{2})+\frac{c}{3}⋅(T^{3}−T_{m}^{3})
$$



$$
ΔS_{u}(T)=\frac{ΔH_{u}(T_{m})}{T_{m}}+a⋅ln\frac{T}{T_{m}}+b⋅(T−T_{m})+\frac{c}{2}⋅(T^{2}−T_{m}^{2})
$$

During fitting of Cp, parameters a0, b0, a, b, Tm, and ΔHu(Tm) were allowed to float, while c was kept constant.
