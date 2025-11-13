# Double and triple thermodynamic mutant cycles reveal the basis for specific MsbA-lipid interactions

## Authors

- Jixing Lyu<sup>1</sup>
- Tianqi Zhang<sup>1</sup>
- Michael T Marty<sup>2</sup> ([ORCID: 0000-0001-8115-1772](https://orcid.org/0000-0001-8115-1772))
- David Clemmer<sup>3</sup>
- David H Russell<sup>1</sup>
- Arthur Laganowsky<sup>1</sup> ([ORCID: 0000-0001-5012-5547](https://orcid.org/0000-0001-5012-5547)) †

### Affiliations

1. Department of Chemistry, Texas A&M University College Station United States ([ROR:01f5ytq51](https://ror.org/01f5ytq51))
2. Department of Chemistry and Biochemistry and Bio5 Institute, The University of Arizona Tucson United States ([ROR:023drta67](https://ror.org/023drta67))
3. Department of Chemistry, Indiana University Bloomington United States ([ROR:01kg8sb98](https://ror.org/01kg8sb98))

† Corresponding author

## Abstract

Structural and functional studies of the ATP-binding cassette transporter MsbA have revealed two distinct lipopolysaccharide (LPS) binding sites: one located in the central cavity and the other at a membrane-facing, exterior site. Although these binding sites are known to be important for MsbA function, the thermodynamic basis for these specific MsbA-LPS interactions is not well understood. Here, we use native mass spectrometry to determine the thermodynamics of MsbA interacting with the LPS-precursor 3-deoxy-D-manno-oct-2-ulosonic acid (Kdo)2-lipid A (KDL). The binding of KDL is solely driven by entropy, despite the transporter adopting an inward-facing conformation or trapped in an outward-facing conformation with adenosine 5’-diphosphate and vanadate. An extension of the mutant cycle approach is employed to probe basic residues that interact with KDL. We find the molecular recognition of KDL is driven by a positive coupling entropy (as large as –100 kJ/mol at 298 K) that outweighs unfavorable coupling enthalpy. These findings indicate that alterations in solvent reorganization and conformational entropy can contribute significantly to the free energy of protein-lipid association. The results presented herein showcase the advantage of native MS to obtain thermodynamic insight into protein-lipid interactions that would otherwise be intractable using traditional approaches, and this enabling technology will be instrumental in the life sciences and drug discovery.

## Introduction

Most Gram-negative bacteria contain outer membrane lipopolysaccharide (LPS) that is crucial for maintaining structural integrity and protection from toxins and antibiotics (Simpson and Trent, 2019; Raetz and Whitfield, 2002; Raetz et al., 2007). The ATP-Binding Cassette (ABC) transporter MsbA flips an LPS-precursor, lipooligosaccharide (LOS), from the cytosolic leaflet to the periplasmic leaflet of inner membrane, a process powered by the hydrolysis of adenosine triphosphate (ATP). MsbA functions as a homodimer and each subunit consists of a soluble nucleotide-binding domain (NBD) and a transmembrane domain containing six transmembrane helices (Rees et al., 2009). The proposed mechanism of MsbA-mediated LOS transportation involves the binding of LOS to the interior binding site and a conformational change from an inward-facing conformation (IF) to an outward-facing conformation (OF).

Like other ABC transporters, the ATPase activity of MsbA can be stimulated in the presence of different substrates, particularly hexaacylated lipid A species. (Doerrler and Raetz, 2002; Eckford and Sharom, 2008; Siarheyeva and Sharom, 2009) Recent studies have illuminated the location and importance of several LOS binding sites on MsbA (Mi et al., 2017; Ho et al., 2018; Lyu et al., 2022; Padayatti et al., 2019). The interior binding site is located in the inner cavity, and mutations (R78A, R148A and K299A) engineered to disrupt binding at this site abolish lipid-stimulated ATPase activity and adversely affect cell growth. (Mi et al., 2017; Guo et al., 2021) More recently, the LPS-precursor 3-deoxy-D-manno-oct-2-ulosonic (Kdo)2-lipid A (KDL) was found to bind to an elusive exterior site on MsbA trapped in an OF conformation with adenosine 5’-diphosphate and vanadate (Doerrler and Raetz, 2002; Eckford and Sharom, 2008; Siarheyeva and Sharom, 2009). Similarly, introducing mutations to disrupt binding at the exterior site also abolishes lipid-induced stimulation of ATPase activity (Lyu et al., 2022).

In 1984, Fersht and colleagues introduced the biochemistry community to the application of double mutant cycles as means to quantify the strength of intramolecular and intermolecular interactions. (Carter et al., 1984) The method has proven to be highly effective in examining pairwise interactions, as demonstrated by its notable application in determining the spatial orientation of potassium channel residues in relation to high-affinity toxin binding (Hidalgo and MacKinnon, 1995). More generally, the technique has been used to measure the strength and coupling for residues in protein-protein complexes, protein-ligand complexes, and stability of secondary structure. (Carter et al., 1984; Hidalgo and MacKinnon, 1995; Horovitz, 1996; Pagano et al., 2021; Horovitz et al., 2019; Cockroft and Hunter, 2007; Otzen and Fersht, 1999; Schreiber and Fersht, 1995; Thomas-Tran and Du Bois, 2016) In general, mutant cycles analysis involves measuring the changes in Gibbs free energy for the wild-type protein (P), two single point mutations (PX and PY) and the double mutant protein (PXY) for a given process, such as for protein-protein interactions (for review see Horovitz, 1996). If residue X and Y are independent of each other, then the Gibbs free energy associated with the double mutant protein will be equal to the sum of changes in Gibbs free energy due to the single mutations relative to the wild-type protein. However, if the Gibbs free energy associated with the structural and functional properties of the double mutant protein differs from the sum of single mutant proteins, then the two residues are energetically coupled or co-operative. The coupling free energy (ΔΔGint) is the energy difference between double mutant and two single mutant proteins (see Materials and methods). The ΔΔGint values for pairwise interactions in proteins has revealed the contributions of salt bridges (4–20 kJ/mol), aromatic-aromatic interactions (4 kJ/mol), and charge-aromatic interactions (4 kJ/mol) to protein stability. (Horovitz, 1996; Luisi et al., 2003; Serrano et al., 1991) Prior work on mutant cycles often employed traditional approaches, but such approaches overlook contributions from conformational changes of the reactants as well as potential changes in the hydration of the complex, including the reacting ligand and the solvent (Pagano et al., 2021).

To demonstrate the utility of the mutant cycle approach, we highlight two well-known examples. First, the high-affinity interaction between barnase (an extracellular RNase of Bacillus amyloliquefaciens) and barstar (inhibitor of barnase) has been extensively studied by double mutant cycles. (Schreiber and Fersht, 1995) For example, pairwise interactions between residues that are less than seven angstrom in distance (based on crystal structures) have been shown to be co-operative. These interactions were shown to be important for stability of the barnase-barstar complex with coupling energies reaching as high as 7 kcal/mol. Another classical example involves the application of mutant cycles to guide docking and spatial arrangement of a high-affinity peptide inhibitor (scorpion toxin) binding to the Shaker potassium channel (Hidalgo and MacKinnon, 1995). Of the pairwise interactions that underwent mutant cycle analysis, one pair (R24 from toxin and D431 from channel) in particular displayed an extraordinary coupling energy of 17 kJ/mol. This result indicates the two residues interact in the complex. Despite the absence of a structure of toxin-potassium channel complex, results from the mutant cycle analysis provided a strong constraint positioning the toxin relative to the potassium channel pore-forming region. In summary, these studies demonstrate how mutant cycle analysis can be used to determine the energetics of pairwise interactions, which is important for understanding how these molecular interactions contribute to the overall stability of proteins in complex with other molecules, such as ligands and other proteins.

Native mass spectrometry (MS) is well suited to characterize the interactions between protein and other molecules, especially for membrane proteins (Bolla et al., 2019; Robinson, 2017; Tamara et al., 2022). The technique is capable of maintaining non-covalent interactions and native-like structure in the gas phase (Ruotolo et al., 2005; Laganowsky et al., 2014), essential for studying biochemical interactions with small molecules, such as the binding of drugs, lipids, and nucleotides (Laganowsky et al., 2014; Allison et al., 2015; Barrera et al., 2008; Campuzano et al., 2019; Gupta et al., 2017; Marcoux et al., 2013; Yen et al., 2018; Zhou et al., 2011). In combination with a variable temperature nano electrospray ionization device, native MS has determined the thermodynamics for protein-protein and protein-ligand interactions (Daneshfar et al., 2004; Deng et al., 2013; Raab et al., 2020; Walker et al., 2023; Qiao et al., 2021; McCabe et al., 2021). For example, the molecular interaction between the signaling lipid 4,5-bisphosphate phosphatidylinositol and Kir3.2 is dominated by a large, favorable change in entropy (Qiao et al., 2021). Recently, native MS has been combined with mutant cycles analysis to determine the energetic contribution of pairwise inter-protein interactions for a soluble protein complex (Sokolovski et al., 2017; Cveticanin et al., 2018). Notably, the coupling energies determined by native MS and isothermal calorimetry are in agreement (Sokolovski et al., 2017). Mutant cycle analysis is also being used to study cardiolipin binding to sites on AqpZ with native MS (Jayasekera et al., 2023).

Traditional mutant cycles focus on pairwise interactions, such as two interacting residues in a protein complex (Serrano et al., 1990). Single- and double-point mutations along with characterizing their impact on protein stability/assembly enable assessment of the energetic contribution for the pairwise interaction. If the two residues are independent (non-co-operative) then the change in free energy will be equal to the sum of the two single mutations. In contrast, if the two residues are dependent on each other, then the coupling energy is a measure of their co-operativity. Although mutant cycles are often applied to protein-protein interactions, here we extend mutant cycle principles to study membrane protein-lipid interactions. It is established that MsbA has two high-affinity binding sites for the LPS-precursor KDL. Here, we examine each site independently followed by simultaneously probing both KDL sites. At present, there is limited availability of synthetic KDL derivatives, limiting this study to focus on residues that interact with KDL, such as basic residues coordinating the conserved phosphoglucosamine (P-GlcN) of KDL. Despite the limitation of commercially available KDL derivatives, the studies below demonstrate how residues energetically contribute to specific binding, providing insight into the driving forces underlying essential membrane protein-lipid interactions. Recently, we reported results using native MS that reveal conformation-dependent lipid binding affinities to MsbA (Lyu et al., 2022). As these measurements were performed at a single temperature, we set out to perform a more detailed thermodynamic analysis to better understand the molecular driving forces that underpin specific MsbA-lipid interactions. Here, we report binding thermodynamics (ΔH, ΔS, and ΔG) for KDL binding to MsbA in IF and OF conformations. These results reveal the unique thermodynamic contributions of MsbA residues that engage KDL. We also report coupling energetics (ΔΔGint) for pairwise interactions, including, for the first time, the contributions from coupling enthalpy (ΔΔHint) and coupling entropy (Δ(-TΔSint)), providing rich molecular insight into specific protein-lipid interactions.

## Results

### MsbA residues selected for mutant cycles analyses

MsbA is known to bind KDL either in the inner cavity or at the two exterior sites (Figure 1). For both sites, a series of conserved arginine and lysine residues form specific interactions with the headgroup of KDL. To perform mutant cycles analysis, we introduced single mutations into MsbA to target KDL binding to the interior (MsbAR78A and MsbAR299A) and exterior (MsbAR188A, MsbAR238A, and MsbAK243A) sites. More specifically, R78 coordinates one of the characteristic phosphoglucosamine (P-GlcN) substituents of KDL whereas K299 interacts with a carboxylic acid group in the headgroup of KDL. The two P-GlcN constituents of LOS are coordinated by R238 and R188 +K243, respectively. R188 also forms an additional hydrogen bond with the headgroup of KDL. In addition, we prepared double and triple mutants of MsbA for the various residues that were selected for mutagenesis.

![Figure 1.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig1-v1.jpg)

**Figure 1.:** (a) Two views of LPS bound to the interior site or central cavity of MsbA. The protein shown is also bound to the inhibitor G907 (PDB 6BPL) (Ho et al., 2018). The protein and lipid are shown in cartoon and stick representation, respectively. (b) Molecular details of the residues interacting with LPS at the interior site. Bonds are shown as dashed yellow lines along with residue labels. (c) Two views of the KDL molecules bound to the two exterior binding sites of MsbA that are symmetrically related (PDB 8DMM) (Lyu et al., 2022). Shown as described in panel A. (d) Molecular view of KDL bound to MsbA and shown as described in panel B. The asterisk denotes residues selected for mutant cycle analysis.

### Thermodynamics of MsbA-KDL interactions

We performed titrations to determine the equilibrium binding affinity for MsbA-KDL interactions at four different temperatures (288, 293, 298, and 303 K; Figure 2, Figure 2—figure supplements 1–3). These studies used optimized samples of MsbA that do not contain any co-purified LPS (for details see Lyu et al., 2022). The transporter was stable at the selected temperatures. For example, binding of KDL to MsbA was enhanced at higher temperatures (Figure 2a, Figure 2—figure supplements 1–3), indicating a favorable entropy for the interaction. For a given temperature, the mass spectra from the titration series were deconvoluted and equilibrium dissociation constants (KD) were determined for MsbA binding up to three KDL molecules (Figure 2b, Figure 2—figure supplements 1–3 and Table 1). It is important to note that, unlike traditional approaches that struggle to distinguish between free protein from that bound to ligand, (Jarmoskaite et al., 2020) native MS can resolve different ligand bound states, including the free concentration of protein and free concentration of ligand(s), in a single mass spectrum (Daneshfar et al., 2004; Cong et al., 2016; Cong et al., 2017; Patrick et al., 2018). Notably, the native MS approach has been cross validated using isothermal calorimetry and surface plasmon resonance (Daneshfar et al., 2004; Cong et al., 2016; Cong et al., 2017). Interestingly, van’ t Hoff analysis showed a non-linear trend for three KDL binding reactions (Figure 2c, Figure 2—figure supplements 1–3), indicating that over the selected temperature range, heat capacity is not constant (Prabhu and Sharp, 2005). The nonlinear form of the van't Hoff equation enabled us to determine the ΔH and change in heat capacity (ΔCp) at a reference temperature of 298  K (Figure 2c–d, Figure 2—figure supplements 1–3). In this case, ΔG was calculated directly from KD values, and entropy (ΔS) was back calculated using both ΔH and ΔG. ΔG values for binding KDL1-2 range from –32.0±0.1 to -35.2±0.1 kJ/mol. The binding reaction has a positive ΔCp that alters the thermodynamic parameters at different temperatures. At the lowest temperature, KDL binding is driven by favorable enthalpy (–36±12 to -43±7 kJ/mol) with a small entropically penalty (-TΔS, 2±11–12±7 kJ/mol at 288 K). In contrast, KDL binding at higher temperatures displays a large, favorable entropy (-TΔS, –123±12 to -146±7 kJ/mol at 303 K) that compensates a large enthalpic barrier (86±12–112±7 kJ/mol). These results highlight the role of entropy in KDL binding to MsbA that may stem from solvent reorganization.

![Figure 2.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig2-v1.jpg)

**Figure 2.:** (a) Representative deconvoluted native mass spectra of 0.39 μM wild-type MsbA in C10E5 and in the presence of 0.6 μM KDL recorded at different solution temperatures. (b) Plot of mole fraction of MsbA (KDL)0-3 determined from titration of KDL (dots) at 298 K and resulting fit from a sequential ligand binding model (solid line, R2=0.99). (c) van’ t Hoff plot for MsbA(KDL)1-3 and resulting fit of a nonlinear van’ t Hoff equation. (d) Thermodynamics for MsbA and mutants (MsbAR78A, MsbAK299A and MsbAR78A,K299A) binding KDL at 298 K. (e) Mutant cycles for MsbA and mutants with (from left to right) ΔΔG (mutant minus wild-type), ΔΔH and Δ(-TΔS) values indicated over the respective arrows. Shown are values at 298 K. Reported are the average and standard deviation from repeated measurements (n = 3).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** The temperature is provided in the inset. The concentration of MsbA, MsbAR78A, MsbAR299A and MsbAR78A,K299A is 0.39, 0.36, 0.33, and 0.83 μM, respectively.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Shown are plots of the mole fraction for MsbA and bound to different number of KDL determined from a titration series (dots) and resulting fit from a sequential ligand-binding model (solid lines). The different temperatures and MsbA mutants are labelled. Reported are the mean and standard deviation (n=3).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** van’ t Hoff plots for the transporter binding KDL (dots) and resulting fit from nonlinear Van’t Hoff equation (solid lines). Reference temperature (T0) is 298 K Reported are the mean and standard deviation (n=3).

**Table 1.**
 Equilibrium dissociation constants (KD) for KDL binding MsbA at various temperatures.Reported are the mean and standard deviation (n=3).


<table>
  <thead>
    <tr>
      <th></th>
      <th>Temperature(K)</th>
      <th>KD1(μM)</th>
      <th>KD2(μM)</th>
      <th>KD3(μM)</th>
      <th>R2*</th>
      <th>Χ2*</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">WT</td>
      <td>288</td>
      <td>0.69±0.06</td>
      <td>2.64±0.16</td>
      <td>6.60±0.54</td>
      <td>0.99</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>293</td>
      <td>0.75±0.04</td>
      <td>2.86±0.23</td>
      <td>6.94±0.56</td>
      <td>0.99</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>298</td>
      <td>0.68±0.05</td>
      <td>2.53±0.17</td>
      <td>6.01±0.40</td>
      <td>0.99</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>303</td>
      <td>0.43±0.05</td>
      <td>1.36±0.10</td>
      <td>3.30±0.23</td>
      <td>0.96</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td rowspan="4">R78A</td>
      <td>288</td>
      <td>1.91±0.17</td>
      <td>6.18±0.80</td>
      <td></td>
      <td>0.98</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>293</td>
      <td>1.87±0.18</td>
      <td>6.18±0.37</td>
      <td></td>
      <td>0.98</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>298</td>
      <td>2.00±0.20</td>
      <td>5.23±0.47</td>
      <td></td>
      <td>0.98</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>303</td>
      <td>7.68±0.47</td>
      <td>5.72±0.21</td>
      <td></td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="4">R188A</td>
      <td>288</td>
      <td>2.21±0.17</td>
      <td>11.01±1.95</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>293</td>
      <td>2.28±0.12</td>
      <td>11.62±2.17</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>298</td>
      <td>1.98±0.07</td>
      <td>8.92±0.73</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>303</td>
      <td>1.32±0.05</td>
      <td>4.37±0.13</td>
      <td></td>
      <td>0.95</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td rowspan="4">R238A</td>
      <td>288</td>
      <td>2.48±0.12</td>
      <td>4.74±0.45</td>
      <td></td>
      <td>0.99</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>293</td>
      <td>3.55±0.10</td>
      <td>6.21±0.40</td>
      <td></td>
      <td>1</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>298</td>
      <td>4.70±0.07</td>
      <td>9.66±0.82</td>
      <td></td>
      <td>1</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>303</td>
      <td>4.71±0.20</td>
      <td>9.94±0.40</td>
      <td></td>
      <td>1</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td rowspan="4">K243A</td>
      <td>288</td>
      <td>1.24±0.07</td>
      <td>7.28±0.78</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>293</td>
      <td>1.41±0.09</td>
      <td>7.38±0.53</td>
      <td></td>
      <td>0.99</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>298</td>
      <td>1.28±0.05</td>
      <td>6.65±0.50</td>
      <td></td>
      <td>0.99</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>303</td>
      <td>0.74±0.07</td>
      <td>3.73±0.32</td>
      <td></td>
      <td>0.97</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td rowspan="4">K299A</td>
      <td>288</td>
      <td>2.32±0.06</td>
      <td>6.07±0.33</td>
      <td>17.54±6.77</td>
      <td>1</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>293</td>
      <td>2.35±0.07</td>
      <td>5.75±0.07</td>
      <td>16.03±3.18</td>
      <td>0.99</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>298</td>
      <td>2.12±0.09</td>
      <td>5.07±0.12</td>
      <td>14.01±1.59</td>
      <td>0.99</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>303</td>
      <td>1.38±0.01</td>
      <td>2.91±0.02</td>
      <td>5.91±0.55</td>
      <td>0.97</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td rowspan="4">R78A K299A</td>
      <td>288</td>
      <td>2.56±0.17</td>
      <td>7.77±0.11</td>
      <td></td>
      <td>0.98</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td>293</td>
      <td>3.08±0.13</td>
      <td>8.92±0.39</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>298</td>
      <td>3.17±0.17</td>
      <td>6.78±0.82</td>
      <td></td>
      <td>0.99</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>303</td>
      <td>6.91±0.66</td>
      <td>11.96±2.83</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td rowspan="4">R188A R238A</td>
      <td>288</td>
      <td>5.55±0.87</td>
      <td></td>
      <td></td>
      <td>0.99</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>293</td>
      <td>8.51±0.67</td>
      <td></td>
      <td></td>
      <td>1</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>298</td>
      <td>13.01±0.43</td>
      <td></td>
      <td></td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>303</td>
      <td>11.14±0.23</td>
      <td></td>
      <td></td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="4">R188A K243A</td>
      <td>288</td>
      <td>1.06±0.02</td>
      <td>5.84±0.29</td>
      <td></td>
      <td>0.99</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>293</td>
      <td>1.07±0.02</td>
      <td>6.07±0.13</td>
      <td></td>
      <td>0.99</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>298</td>
      <td>1.05±0.02</td>
      <td>5.82±0.06</td>
      <td></td>
      <td>0.99</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>303</td>
      <td>0.75±0.01</td>
      <td>4.35±0.17</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td rowspan="4">R188A K299A</td>
      <td>288</td>
      <td>13.86±0.85</td>
      <td>13.83±3.23</td>
      <td></td>
      <td>0.99</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>293</td>
      <td>12.55±0.64</td>
      <td>14.29±2.18</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>298</td>
      <td>9.82±0.70</td>
      <td>11.50±1.04</td>
      <td></td>
      <td>0.98</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>303</td>
      <td>4.86±0.44</td>
      <td>8.56±0.20</td>
      <td></td>
      <td>0.99</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td rowspan="4">R238A K243A</td>
      <td>288</td>
      <td>2.79±0.20</td>
      <td>7.93±0.47</td>
      <td></td>
      <td>0.98</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td>293</td>
      <td>3.26±0.09</td>
      <td>7.39±0.50</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>298</td>
      <td>6.53±0.2</td>
      <td>8.97±0.15</td>
      <td></td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>303</td>
      <td>7.63±0.26</td>
      <td>10.78±2.19</td>
      <td></td>
      <td>1</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td rowspan="4">R188A R238A K243A</td>
      <td>288</td>
      <td>20.53±2.25</td>
      <td></td>
      <td></td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>293</td>
      <td>21.09±2.84</td>
      <td></td>
      <td></td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>298</td>
      <td>19.80±1.71</td>
      <td></td>
      <td></td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>303</td>
      <td>13.12±0.81</td>
      <td></td>
      <td></td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

_These values represent the replicates with the poorest fits._

### KDL binding to the interior binding site of MsbA

We next determined the thermodynamics of KDL binding to MsbA containing single and double mutations at the interior binding site (Figure 2d, Figure 2—figure supplements 1–3). R78 of each subunit interacts with one of the P-GlcN moieties of LPS whereas one of the K299 residues interacts with a carboxylic acid group of LPS molecule in the inner cavity. Therefore, introducing the R78A mutation will impact symmetrically equivalent binding sites. MsbAR78A showed a reduction in binding KDL1-2 with ΔG ranging from –30.2±0.2 to -32.5±0.2 kJ/mol. At 298 K, KDL binding is enthalpically and entropically favorable whereas binding of the second KDL is similar to the wild-type protein (Figure 2d, Figure 2—figure supplements 1–3). The binding thermodynamics for MsbAK299A is reminiscent of the wild-type protein with a large, favorable change in entropy (-TΔS, –75±2 to -86±1 kJ/mol at 298 K) and unfavorable enthalpy (43±2–53±1 kJ/mol) (Figure 2d, Figure 2—figure supplements 1–3). The double mutant MsbAR78A,K299A protein shows a reduction in opposing entropic and enthalpic terms leading to an increase in ΔG by ~4 kJ/mol relative to wild-type MsbA (Figure 2d). Mutant cycle analysis indicates a coupling energy (ΔΔGint) of 1.7±0.4 kJ/mol that contributes to the stability of KDL-MsbA complex (Figure 2e, Figure 2—figure supplements 1–3 and Tables 2 and 3). More generally, ΔΔ with a positive sign means favorable cooperation. Interestingly, the coupling enthalpy (ΔΔHint of –26±15 kJ/mol) and coupling entropy (Δ(-TΔS)int of 28±15 kJ/mol at 298 K) indicating that these residues contribute to KDL binding through an entropy driven process that overcomes an enthalpic barrier (Figure 2e, Figure 2—figure supplements 1–3 and Table 3).

**Table 2.**
 Thermodynamic signatures of KDL interacting with wild-type and mutant MsbA.Reported are the mean with standard deviation (n=3), and the subscript denotes the nth KDL binding event.


<table>
  <thead>
    <tr>
      <th></th>
      <th>T(K)</th>
      <th>ΔG1(kJ/mol)</th>
      <th>ΔH1(kJ/mol)</th>
      <th>-TΔS1(kJ/mol)</th>
      <th>ΔCp1(kJ/mol/K)</th>
      <th>ΔG2(kJ/mol)</th>
      <th>ΔH2(kJ/mol)</th>
      <th>-TΔS2(kJ/mol)</th>
      <th>ΔCp2(kJ/mol/K)</th>
      <th>ΔG3(kJ/mol)</th>
      <th>ΔH3(kJ/mol)</th>
      <th>-TΔS3(kJ/mol)</th>
      <th>ΔCp3(kJ/mol/K)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">WT</td>
      <td>288</td>
      <td>–34.0±0.2</td>
      <td>–36.0±11.6</td>
      <td>2.0±11.5</td>
      <td>8.0±1.5</td>
      <td>–30.8±0.1</td>
      <td>–43.2±7.3</td>
      <td>12.4±7.3</td>
      <td>10.1±0.9</td>
      <td>–28.6±0.2</td>
      <td>–36.6±8.1</td>
      <td>8.0±8.0</td>
      <td>9.4±0.9</td>
    </tr>
    <tr>
      <td>293</td>
      <td>–34.4±0.1</td>
      <td>4.3±5.4</td>
      <td>–38.6±5.4</td>
      <td>7.4±1.5</td>
      <td>–31.1±0.2</td>
      <td>7.9±2.7</td>
      <td>–39.0±2.7</td>
      <td>9.1±0.8</td>
      <td>–29.0±0.2</td>
      <td>10.9±3.3</td>
      <td>–39.8±3.3</td>
      <td>8.5±0.6</td>
    </tr>
    <tr>
      <td>298</td>
      <td>–35.2±0.2</td>
      <td>45.0±5.8</td>
      <td>–80.2±5.9</td>
      <td>8.9±1.4</td>
      <td>–32.0±0.2</td>
      <td>59.9±2.3</td>
      <td>–91.8±2.2</td>
      <td>11.7±1.2</td>
      <td>–29.8±0.2</td>
      <td>59.1±1.8</td>
      <td>–88.9±1.7</td>
      <td>10.7±1.5</td>
    </tr>
    <tr>
      <td>303</td>
      <td>–37.0±0.3</td>
      <td>86.1±12.1</td>
      <td>–123.0±12.4</td>
      <td>8.3±1.5</td>
      <td>–34.1±0.2</td>
      <td>112.3±7.1</td>
      <td>–146.4±7.1</td>
      <td>10.6±1.0</td>
      <td>–31.8±0.2</td>
      <td>107.7±7.1</td>
      <td>–139.5±7.1</td>
      <td>9.8±1.1</td>
    </tr>
    <tr>
      <td rowspan="3">R78A</td>
      <td>288</td>
      <td>–31.6±0.2</td>
      <td>9.6±4.5</td>
      <td>–41.2±4.7</td>
      <td>–2.6±1.1</td>
      <td>–28.8±0.3</td>
      <td>–13.0±19.1</td>
      <td>–15.8±18.8</td>
      <td>5.0±1.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>–32.2±0.3</td>
      <td>–3.5±5.1</td>
      <td>–28.6±5.1</td>
      <td>–2.6±1.1</td>
      <td>–29.2±0.1</td>
      <td>12.0±11.1</td>
      <td>–41.3±11.1</td>
      <td>5.0±1.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–32.5±0.2</td>
      <td>–16.7±9.6</td>
      <td>–15.9±9.6</td>
      <td>–2.6±1.1</td>
      <td>–30.2±0.2</td>
      <td>37.1±5.9</td>
      <td>–67.2±6.1</td>
      <td>5.0±1.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R188A</td>
      <td>288</td>
      <td>–31.2±0.2</td>
      <td>–23.0±8.2</td>
      <td>–8.3±8.1</td>
      <td>6.4±1.1</td>
      <td>–27.4±0.4</td>
      <td>–39.1±0.5</td>
      <td>11.8±0.7</td>
      <td>11.2±1.0</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>–31.7±0.1</td>
      <td>9.4±3.6</td>
      <td>–41.1±3.5</td>
      <td>6.1±1.2</td>
      <td>–27.7±0.5</td>
      <td>17.4±4.6</td>
      <td>–45.1±4.2</td>
      <td>10.7±1.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–32.6±0.1</td>
      <td>42.1±3.7</td>
      <td>–74.6±3.7</td>
      <td>6.9±0.9</td>
      <td>–28.8±0.2</td>
      <td>74.4±8.8</td>
      <td>–103.2±8.6</td>
      <td>12.1±0.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–34.1±0.1</td>
      <td>74.9±8.3</td>
      <td>–109.0±8.3</td>
      <td>6.6±1.0</td>
      <td>–31.1±0.1</td>
      <td>131.6±12.8</td>
      <td>–162.7±12.8</td>
      <td>11.5±0.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R238A</td>
      <td>288</td>
      <td>–30.9±0.1</td>
      <td>–66.8±3.4</td>
      <td>35.9±3.3</td>
      <td>4.8±0.3</td>
      <td>–29.4±0.2</td>
      <td>–57.9±17.9</td>
      <td>28.6±17.8</td>
      <td>2.8±2.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>–30.6±0.1</td>
      <td>–42.6±4.0</td>
      <td>12.1±3.9</td>
      <td>4.1±0.3</td>
      <td>–29.2±0.2</td>
      <td>–43.2±6.5</td>
      <td>13.9±6.5</td>
      <td>0.9±2.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–30.4±0.1</td>
      <td>–17.9±4.8</td>
      <td>–12.6±4.8</td>
      <td>5.8±0.3</td>
      <td>–28.6±0.2</td>
      <td>–26.8±7.2</td>
      <td>–1.9±7.0</td>
      <td>5.5±2.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–30.9±0.1</td>
      <td>7.2±5.8</td>
      <td>–38.1±5.9</td>
      <td>5.1±0.3</td>
      <td>–29.0±0.1</td>
      <td>–9.5±18.6</td>
      <td>–19.5±18.7</td>
      <td>3.7±2.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">K243A</td>
      <td>288</td>
      <td>–32.6±0.1</td>
      <td>–48.5±7.3</td>
      <td>15.9±7.2</td>
      <td>9.9±0.9</td>
      <td>–28.4±0.3</td>
      <td>–31.6±7.3</td>
      <td>3.3±7.0</td>
      <td>8.5±0.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>–32.8±0.2</td>
      <td>1.5±3.5</td>
      <td>–34.4±3.5</td>
      <td>9.1±0.8</td>
      <td>–28.8±0.2</td>
      <td>11.7±3.1</td>
      <td>–40.5±3.0</td>
      <td>7.3±1.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–33.6±0.1</td>
      <td>52.2±3.9</td>
      <td>–85.9±4.0</td>
      <td>11.2±1.2</td>
      <td>–29.6±0.2</td>
      <td>56.0±2.0</td>
      <td>–85.5±2.1</td>
      <td>10.3±0.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–35.6±0.2</td>
      <td>103.3±8.0</td>
      <td>–138.9±8.2</td>
      <td>10.3±1.0</td>
      <td>–31.5±0.2</td>
      <td>100.8±5.6</td>
      <td>–132.3±5.8</td>
      <td>9.1±0.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">K299A</td>
      <td>288</td>
      <td>–31.1±0.1</td>
      <td>–22.2±9.5</td>
      <td>–8.9±9.4</td>
      <td>6.4±1.1</td>
      <td>–28.8±0.1</td>
      <td>–18.8±9.6</td>
      <td>–10.0±9.5</td>
      <td>7.3±1.0</td>
      <td>–26.4±0.9</td>
      <td>–35.6±71.5</td>
      <td>9.3±70.7</td>
      <td>11.4±7.1</td>
    </tr>
    <tr>
      <td>293</td>
      <td>–31.6±0.1</td>
      <td>9.9±3.8</td>
      <td>–41.5±3.9</td>
      <td>5.6±1.1</td>
      <td>–29.4±0.1</td>
      <td>18.0±4.6</td>
      <td>–47.4±4.6</td>
      <td>6.0±1.0</td>
      <td>–27.0±0.5</td>
      <td>22.7±37.2</td>
      <td>–49.6±37.5</td>
      <td>9.2±8.6</td>
    </tr>
    <tr>
      <td>298</td>
      <td>–32.4±0.1</td>
      <td>42.7±2.1</td>
      <td>–75.1±1.9</td>
      <td>7.4±1.2</td>
      <td>–30.2±0.1</td>
      <td>55.9±1.7</td>
      <td>–86.1±1.6</td>
      <td>9.0±1.1</td>
      <td>–27.7±0.3</td>
      <td>82.9±7.8</td>
      <td>–110.6±7.9</td>
      <td>14.7±5.1</td>
    </tr>
    <tr>
      <td>303</td>
      <td>–34.0±0.1</td>
      <td>75.8±7.7</td>
      <td>–109.8±7.7</td>
      <td>6.7±1.2</td>
      <td>–32.1±0.1</td>
      <td>94.3±6.3</td>
      <td>–126.4±6.3</td>
      <td>7.8±1.1</td>
      <td>–30.4±0.2</td>
      <td>144.1±30.5</td>
      <td>–174.5±30.3</td>
      <td>12.5±6.4</td>
    </tr>
    <tr>
      <td rowspan="3">R78A K299A</td>
      <td>288</td>
      <td>–30.9±0.2</td>
      <td>–36.8±5.6</td>
      <td>5.9±5.4</td>
      <td>4.4±0.8</td>
      <td>–28.2±0.1</td>
      <td>–49.1±5.7</td>
      <td>20.9±5.7</td>
      <td>12.0±1.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>–30.9±0.1</td>
      <td>–15.0±2.8</td>
      <td>–16.0±2.8</td>
      <td>4.4±0.8</td>
      <td>–28.3±0.1</td>
      <td>10.7±9.6</td>
      <td>–39.1±9.7</td>
      <td>12.0±1.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–31.4±0.1</td>
      <td>6.8±3.8</td>
      <td>–38.2±3.9</td>
      <td>4.4±0.8</td>
      <td>–29.5±0.3</td>
      <td>70.6±15.6</td>
      <td>–100.1±15.9</td>
      <td>12.0±1.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R188A R238A</td>
      <td>288</td>
      <td>–29.0±0.4</td>
      <td>–93.3±15.2</td>
      <td>64.3±14.8</td>
      <td>7.8±1.3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>–28.5±0.2</td>
      <td>–53.3±9.2</td>
      <td>24.8±9.1</td>
      <td>5.9±1.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–27.9±0.1</td>
      <td>–11.6±4.7</td>
      <td>–16.3±4.6</td>
      <td>10.6±1.0</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–28.8±0.1</td>
      <td>30.9±5.9</td>
      <td>–59.7±5.9</td>
      <td>8.7±1.2</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R188A K243A</td>
      <td>288</td>
      <td>–33±0.1</td>
      <td>–20.3±6.0</td>
      <td>–12.6±6.0</td>
      <td>4.9±0.6</td>
      <td>–28.9±0.1</td>
      <td>–21.3±3.4</td>
      <td>–7.6±3.3</td>
      <td>4.8±0.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>–33.5±0.1</td>
      <td>4.5±3.2</td>
      <td>–38.0±3.2</td>
      <td>4.0±0.6</td>
      <td>–29.3±0.1</td>
      <td>2.7±3.4</td>
      <td>–32.0±3.4</td>
      <td>4.2±0.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–34.1±0.1</td>
      <td>30.1±1.9</td>
      <td>–64.3±1.9</td>
      <td>6.2±0.7</td>
      <td>–29.9±0.1</td>
      <td>27.3±5.0</td>
      <td>–57.1±5.0</td>
      <td>5.6±0.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–35.5±0.1</td>
      <td>56.1±4.1</td>
      <td>–91.7±4.1</td>
      <td>5.3±0.6</td>
      <td>–31.1±0.1</td>
      <td>52.0±7.3</td>
      <td>–83.2±7.4</td>
      <td>5.0±0.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R188A K299A</td>
      <td>288</td>
      <td>–26.8±0.1</td>
      <td>–15.4±16.2</td>
      <td>–11.4±16.0</td>
      <td>8.9±2.2</td>
      <td>–26.9±0.6</td>
      <td>–15.7±36.0</td>
      <td>–11.1±35.4</td>
      <td>5.2±3.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>–27.5±0.1</td>
      <td>29.5±5.2</td>
      <td>–57.0±5.2</td>
      <td>7.8±1.3</td>
      <td>–27.2±0.4</td>
      <td>10.1±18.9</td>
      <td>–37.3±18.9</td>
      <td>5.8±6.0</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–28.6±0.2</td>
      <td>75.2±7.6</td>
      <td>–103.8±7.4</td>
      <td>10.4±3.5</td>
      <td>–28.2±0.2</td>
      <td>35.4±6.4</td>
      <td>–63.6±6.3</td>
      <td>4.4±1.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–30.8±0.2</td>
      <td>121.4±19.9</td>
      <td>–152.2±20.0</td>
      <td>9.4±2.6</td>
      <td>–29.4±0.1</td>
      <td>60.5±14.2</td>
      <td>–89.9±14.2</td>
      <td>5.0±2.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R238A K243A</td>
      <td>288</td>
      <td>–30.7±0.2</td>
      <td>–42.4±8.3</td>
      <td>11.8±8.1</td>
      <td>–1.2±0.5</td>
      <td>–28.1±0.1</td>
      <td>13.2±9.6</td>
      <td>–41.4±9.6</td>
      <td>–3.8±2.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>–30.8±0.1</td>
      <td>–46.9±6.0</td>
      <td>16.1±6.0</td>
      <td>–4.7±0.3</td>
      <td>–28.8±0.2</td>
      <td>–5.4±4.5</td>
      <td>–23.4±4.5</td>
      <td>–4.7±1.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–29.6±0.1</td>
      <td>–48.4±4.0</td>
      <td>18.8±4.1</td>
      <td>3.8±0.8</td>
      <td>–28.8±0.1</td>
      <td>–23.3±17.2</td>
      <td>–5.5±17.2</td>
      <td>–2.5±3.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–29.7±0.1</td>
      <td>–48.3±3.4</td>
      <td>18.6±3.4</td>
      <td>0.4±0.6</td>
      <td>–28.9±0.6</td>
      <td>–40.7±31</td>
      <td>11.9±31.5</td>
      <td>–3.4±2.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R188A R238A K243A</td>
      <td>288</td>
      <td>–25.9±0.3</td>
      <td>–25.2±5.7</td>
      <td>–0.7±5.4</td>
      <td>6.2±0.3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>–26.3±0.3</td>
      <td>6.5±3.7</td>
      <td>–32.7±3.4</td>
      <td>5.3±1.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–26.9±0.2</td>
      <td>38.9±0.6</td>
      <td>–65.7±0.7</td>
      <td>7.6±2.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–28.3±0.2</td>
      <td>71.7±3.3</td>
      <td>–100±3.3</td>
      <td>6.7±0.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Double mutant cycle analysis of the first KDL binding to wild-type and mutant MsbA.The ΔΔ values mutant relative to the wild-type protein. Reported are the mean (n=3).


<table>
  <thead>
    <tr>
      <th colspan="2"></th>
      <th>Temperature(K)</th>
      <th>ΔΔG(kJ/mol)</th>
      <th>ΔΔH(kJ/mol)</th>
      <th>Δ(-TΔS)(kJ/mol)</th>
      <th>ΔΔGint(kJ/mol)</th>
      <th>ΔΔHint(kJ/mol)</th>
      <th>Δ(-ΔTS)int(kJ/mol)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3" colspan="2">R78A</td>
      <td>288</td>
      <td>2.4±0.2</td>
      <td>45.6±12.5</td>
      <td>–43.2±12.4</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>2.2±0.2</td>
      <td>–7.8±7.5</td>
      <td>10.0±7.5</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>2.7±0.2</td>
      <td>–61.7±11.3</td>
      <td>64.4±11.3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4" colspan="2">R188A</td>
      <td>288</td>
      <td>2.8±0.2</td>
      <td>13.0±14.2</td>
      <td>–10.2±14.0</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>2.7±0.1</td>
      <td>5.2±6.5</td>
      <td>–2.5±6.5</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>2.7±0.2</td>
      <td>–3.0±6.9</td>
      <td>5.6±7.0</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>2.9±0.4</td>
      <td>–11.2±14.7</td>
      <td>14.1±14.9</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4" colspan="2">R238A</td>
      <td>288</td>
      <td>3.1±0.2</td>
      <td>–30.9±12.1</td>
      <td>33.9±11.9</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>3.8±0.1</td>
      <td>–46.9±6.7</td>
      <td>50.7±6.7</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>4.8±0.1</td>
      <td>–62.9±7.5</td>
      <td>67.7±7.6</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>6.1±0.4</td>
      <td>–78.8±13.5</td>
      <td>84.9±13.7</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4" colspan="2">K243A</td>
      <td>288</td>
      <td>1.4±0.2</td>
      <td>–12.5±13.7</td>
      <td>13.9±13.5</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>1.5±0.2</td>
      <td>–2.7±6.5</td>
      <td>4.3±6.5</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>1.6±0.2</td>
      <td>7.2±7.0</td>
      <td>–5.6±7.1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>1.4±0.4</td>
      <td>17.3±14.5</td>
      <td>–15.9±14.8</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4" colspan="2">K299A</td>
      <td>288</td>
      <td>2.9±0.2</td>
      <td>13.8±15.1</td>
      <td>–10.9±14.8</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>2.8±0.1</td>
      <td>5.7±6.6</td>
      <td>–2.9±6.7</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>2.8±0.2</td>
      <td>–2.4±6.1</td>
      <td>5.2±6.2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>3.0±0.4</td>
      <td>–10.3±14.3</td>
      <td>13.3±14.6</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="3">R78A</td>
      <td rowspan="3">K299A</td>
      <td>288</td>
      <td>3.2±0.2</td>
      <td>–0.8±12.9</td>
      <td>4.0±12.6</td>
      <td>2.2±0.5</td>
      <td>60.2±23.4</td>
      <td>–58.0±23.1</td>
    </tr>
    <tr>
      <td>293</td>
      <td>3.4±0.1</td>
      <td>–19.2±6.1</td>
      <td>22.7±6.1</td>
      <td>1.6±0.4</td>
      <td>17.1±11.6</td>
      <td>–15.6±11.8</td>
    </tr>
    <tr>
      <td>298</td>
      <td>3.8±0.2</td>
      <td>–38.2±6.9</td>
      <td>42.0±7.1</td>
      <td>1.7±0.4</td>
      <td>–25.8±14.6</td>
      <td>27.5±14.7</td>
    </tr>
    <tr>
      <td rowspan="4">R188A</td>
      <td rowspan="4">R238A</td>
      <td>288</td>
      <td>5.0±0.5</td>
      <td>–57.4±19.1</td>
      <td>62.4±18.7</td>
      <td>0.9±0.6</td>
      <td>39.5±26.7</td>
      <td>–38.7±26.2</td>
    </tr>
    <tr>
      <td>293</td>
      <td>5.9±0.2</td>
      <td>–57.5±10.7</td>
      <td>63.5±10.5</td>
      <td>0.6±0.4</td>
      <td>15.8±14.2</td>
      <td>–15.2±14.1</td>
    </tr>
    <tr>
      <td>298</td>
      <td>7.3±0.2</td>
      <td>–56.6±7.5</td>
      <td>64.0±7.5</td>
      <td>0.1±0.4</td>
      <td>–9.2±12.6</td>
      <td>9.3±12.7</td>
    </tr>
    <tr>
      <td>303</td>
      <td>8.2±0.4</td>
      <td>–55.1±13.5</td>
      <td>63.4±13.7</td>
      <td>0.7±0.5</td>
      <td>–34.9±24.0</td>
      <td>35.6±24.5</td>
    </tr>
    <tr>
      <td rowspan="4">R188A</td>
      <td rowspan="4">K243A</td>
      <td>288</td>
      <td>1.0±0.2</td>
      <td>15.7±13.1</td>
      <td>–14.6±12.9</td>
      <td>3.2±0.5</td>
      <td>–15.1±23.8</td>
      <td>18.3±23.4</td>
    </tr>
    <tr>
      <td>293</td>
      <td>0.9±0.1</td>
      <td>0.3±6.2</td>
      <td>0.6±6.2</td>
      <td>3.4±0.2</td>
      <td>2.2±11.1</td>
      <td>1.2±11.1</td>
    </tr>
    <tr>
      <td>298</td>
      <td>1.1±0.2</td>
      <td>–14.9±6.0</td>
      <td>16.0±6.2</td>
      <td>3.2±0.4</td>
      <td>19.1±11.5</td>
      <td>–16.0±11.8</td>
    </tr>
    <tr>
      <td>303</td>
      <td>1.4±0.4</td>
      <td>–29.9±12.7</td>
      <td>31.4±13.0</td>
      <td>2.8±0.6</td>
      <td>36.0±24.2</td>
      <td>–33.2±24.7</td>
    </tr>
    <tr>
      <td rowspan="4">R188A</td>
      <td rowspan="4">K299A</td>
      <td>288</td>
      <td>7.2±0.2</td>
      <td>20.6±20.0</td>
      <td>–13.4±19.7</td>
      <td>–1.5±0.5</td>
      <td>6.2±28.8</td>
      <td>–7.7±28.4</td>
    </tr>
    <tr>
      <td>293</td>
      <td>6.9±0.1</td>
      <td>25.2±7.5</td>
      <td>–18.3±7.5</td>
      <td>–1.4±0.2</td>
      <td>–14.4±11.9</td>
      <td>13.0±11.9</td>
    </tr>
    <tr>
      <td>298</td>
      <td>6.6±0.2</td>
      <td>30.2±9.6</td>
      <td>–23.6±9.6</td>
      <td>–1.1±0.4</td>
      <td>–35.5±13.2</td>
      <td>34.3±13.3</td>
    </tr>
    <tr>
      <td>303</td>
      <td>6.1±0.4</td>
      <td>35.3±23.3</td>
      <td>–29.2±23.5</td>
      <td>–0.3±0.6</td>
      <td>–56.8±31.0</td>
      <td>56.5±31.5</td>
    </tr>
    <tr>
      <td rowspan="4">R238A</td>
      <td rowspan="4">K243A</td>
      <td>288</td>
      <td>3.4±0.2</td>
      <td>–6.4±14.3</td>
      <td>9.8±14.1</td>
      <td>1.1±0.5</td>
      <td>–36.9±23.3</td>
      <td>38.0±22.8</td>
    </tr>
    <tr>
      <td>293</td>
      <td>3.6±0.1</td>
      <td>–51.1±8.1</td>
      <td>54.7±8.1</td>
      <td>1.8±0.2</td>
      <td>1.5±12.4</td>
      <td>0.3±12.4</td>
    </tr>
    <tr>
      <td>298</td>
      <td>5.6±0.2</td>
      <td>–93.4±7.0</td>
      <td>99.0±7.2</td>
      <td>0.8±0.4</td>
      <td>37.7±12.4</td>
      <td>–37.0±12.7</td>
    </tr>
    <tr>
      <td>303</td>
      <td>7.3±0.4</td>
      <td>–134.4±12.5</td>
      <td>141.6±12.9</td>
      <td>0.2±0.6</td>
      <td>72.8±23.4</td>
      <td>–72.6±24.0</td>
    </tr>
  </tbody>
</table>

### KDL binding to the exterior binding site of MsbA

The recently discovered exterior KDL binding site (Lyu et al., 2022) located on the cytosolic leaflet of inner membrane has not been thoroughly investigated, prompting us to characterize this site by a triple mutant cycle (Figure 3, Figure 3—figure supplements 1–6). We first investigated R188 and K243, residues that both interact with one of the P-GlcN moieties of LOS. Like mutants targeting the interior LPS binding site, introducing mutants at the exterior site will impact binding at the two exterior sites. Both MsbAR188A and MsbAK243A single mutants marginally weakened the interaction by about 2 kJ/mol (Figure 3a, Figure 3—figure supplements 1–6). Enthalpy and entropy for KDL binding MsbAR188A and MsbAK243A was largely similar to the wild-type protein (Figure 3a, Figure 3—figure supplements 1–6). However, the R238A mutation significantly weakened the interaction with KDL, increasing ΔG by nearly 5 kJ/mol compared to the wild-type transporter (Figure 3b, Figure 3—figure supplements 1–6 and Table 3) and resulted in an distinct thermodynamic pattern with negative enthalpy changes for both the first and second KDL binding events (Figure 3a, Figure 3—figure supplements 1–6). ΔG for MsbAR188A,K243A was comparable to the K243A single mutant form of the protein (Figure 3a, Figure 3—figure supplements 1–6). The positive coupling energy of 3.2±0.4 kJ/mol with contributions from a coupling enthalpy of 19±11 kJ/mol and a coupling entropy of –16±12 kJ/mol at 298 K (Figure 3b, Figure 3—figure supplements 1–6 and Table 3). Combining mutation R238A with R188A, MsbAR188A,R238A decreased ΔH by 57 kJ/mol at the cost of increasing -TΔS by 64 kJ/mol at 298 K (Figure 3b, Figure 3—figure supplements 1–6 and Table 3). The coupling energy for R188A and R238A is approximately zero as a result of equal coupling enthalpy and entropy of different signs. Compared to the wild-type protein, MsbAR238A,K243A results in an inversion of the thermodynamic signature with binding now being driven by enthalpy. More specifically, this inversion is accompanied by ΔΔH and Δ(-TΔS) of –93±7 kJ/mol and 99±7 kJ/mol at 298 K (Figure 3b, Figure 3—figure supplements 1–6 and Table 3). Again, the coupling enthalpy and entropy (at 298 K) of equal magnitude but opposite signs give rise to a coupling energy of zero for R238A and R243A (Figure 3b, Figure 3—figure supplements 1–6 and Table 3). Introduction of the R188A mutation into MsbAR238A,K243A, results in reversal of the thermodynamic signature to mirror that of MsbAR188A,K243A (Figure 3a, Figure 3—figure supplements 1–6). The coupling energy, coupling enthalpy, and coupling entropy for R188A, R238A, and R243A are 3.4±0.5 kJ/mol, 100±16 kJ/mol, and –97±16 kJ/mol at 298 K (Table 4), respectively. Taken together, these results demonstrate KDL binding to MsbA is sensitive to mutations at both the interior and exterior sites.

![Figure 3.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig3-v1.jpg)

**Figure 3.:** (a) Thermodynamics for MsbA and mutants (MsbAR188A, MsbAR238A, MsbAK243A, MsbAR188A,R243A, MsbAR188A,K243A, MsbAR238A,R243A, and MsbAR188A,R238A,K299A) binding KDL at 298 K. (b) Triple mutant cycles for MsbA and mutants with (from left to right) ΔΔG, ΔΔH and Δ(-TΔS) values indicated over the respective arrows. Shown are values at 298 K. Reported are the average and standard deviation from repeated measurements (n = 3).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** The concentration of MsbAR188A, MsbAR238A, MsbAK243A and MsbAR188A,K299A is 0.56, 0.26, 0.50, and 0.78 μM, respectively. The temperature is provided in the inset.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** The concentration of MsbAR188A,R238A, MsbAR188A,K243A, MsbAR238A,K243A, and MsbAR188A,R238A,K243A is 0.58, 0.27, 0.39, and 0.17 μM, respectively. The temperature is provided in the inset.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** Shown as described in Figure 2—figure supplement 2.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig3-figsupp4-v1.jpg)

**Figure 3—figure supplement 4.:** Shown as described in Figure 2—figure supplement 2.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig3-figsupp5-v1.jpg)

**Figure 3—figure supplement 5.:** Shown as described in Figure 2—figure supplement 3.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig3-figsupp6-v1.jpg)

**Figure 3—figure supplement 6.:** Shown as described in Figure 2—figure supplement 3.

**Table 4.**
 Triple mutant cycle analysis of the first KDL binding to wild-type and mutant MsbA.Shown as described in Table 3.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2"></th>
      <th>Temperature(K)</th>
      <th>ΔΔG(kJ/mol)</th>
      <th>ΔΔH(kJ/mol)</th>
      <th>Δ(-TΔS) (kJ/mol)</th>
      <th>ΔΔGint(kJ/mol)</th>
      <th>ΔΔHint(kJ/mol)</th>
      <th>Δ(-ΔTS)int(kJ/mol)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="12">R188A</td>
      <td rowspan="4" colspan="2">R238A</td>
      <td>288</td>
      <td>2.2±0.2</td>
      <td>–70.4±8.9</td>
      <td>72.6±8.7</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>3.2±0.1</td>
      <td>–62.7±5.4</td>
      <td>65.9±5.3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>4.7±0.1</td>
      <td>–53.7±6.1</td>
      <td>58.3±6.1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>5.4±0.1</td>
      <td>–43.9±10.2</td>
      <td>49.3±10.3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4" colspan="2">K243A</td>
      <td>288</td>
      <td>–1.8±0.2</td>
      <td>2.6±11.0</td>
      <td>19.9±10.8</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>–1.8±0.2</td>
      <td>–4.9±5.0</td>
      <td>–6.4±5.0</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–1.6±0.1</td>
      <td>–11.9±5.4</td>
      <td>10.4±5.4</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–1.4±0.2</td>
      <td>–18.7±11.5</td>
      <td>17.3±11.8</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R238A</td>
      <td rowspan="4">K243A</td>
      <td>288</td>
      <td>5.3±0.4</td>
      <td>–2.2±10.0</td>
      <td>7.5±9.7</td>
      <td>–4.9±0.5</td>
      <td>–65.6±17.4</td>
      <td>85.0±16.9</td>
    </tr>
    <tr>
      <td>293</td>
      <td>5.4±0.4</td>
      <td>–2.9±5.1</td>
      <td>8.4±4.9</td>
      <td>–4.0±0.5</td>
      <td>–64.7±8.9</td>
      <td>51.2±8.8</td>
    </tr>
    <tr>
      <td>298</td>
      <td>5.7±0.2</td>
      <td>–3.2±3.8</td>
      <td>8.9±3.7</td>
      <td>–2.6±0.2</td>
      <td>–62.4±8.9</td>
      <td>59.8±8.9</td>
    </tr>
    <tr>
      <td>303</td>
      <td>5.8±0.2</td>
      <td>–3.2±8.9</td>
      <td>9.0±8.9</td>
      <td>–1.8±0.4</td>
      <td>–59.5±17.8</td>
      <td>57.7±18.0</td>
    </tr>
    <tr>
      <td rowspan="12">R238A</td>
      <td rowspan="4" colspan="2">R188A</td>
      <td>288</td>
      <td>1.9±0.2</td>
      <td>–26.5±8.9</td>
      <td>28.4±8.7</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>2.1±0.1</td>
      <td>–10.6±5.4</td>
      <td>12.8±5.3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>2.5±0.1</td>
      <td>6.3±6.1</td>
      <td>–3.7±6.1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>2.2±0.1</td>
      <td>23.7±10.2</td>
      <td>–21.5±10.3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4" colspan="2">K243A</td>
      <td>288</td>
      <td>0.3±0.2</td>
      <td>24.4±8.0</td>
      <td>–24.1±7.8</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>–0.2±0.1</td>
      <td>–4.2±5.3</td>
      <td>4.0±5.3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>0.8±0.1</td>
      <td>–30.5±6.2</td>
      <td>31.3±6.2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>1.2±0.2</td>
      <td>–55.5±9.9</td>
      <td>56.7±10.2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R188A</td>
      <td rowspan="4">K243A</td>
      <td>288</td>
      <td>5.1±0.2</td>
      <td>41.7±6.6</td>
      <td>–36.6±6.4</td>
      <td>–2.9±0.4</td>
      <td>–43.8±13.7</td>
      <td>40.9±13.3</td>
    </tr>
    <tr>
      <td>293</td>
      <td>4.3±0.4</td>
      <td>49.1±5.4</td>
      <td>–44.8±5.1</td>
      <td>–2.4±0.4</td>
      <td>–64.0±9.3</td>
      <td>61.6±9.1</td>
    </tr>
    <tr>
      <td>298</td>
      <td>3.6±0.2</td>
      <td>56.7±4.9</td>
      <td>–53.2±4.9</td>
      <td>–0.2±0.2</td>
      <td>–81.0±10.0</td>
      <td>80.8±10.0</td>
    </tr>
    <tr>
      <td>303</td>
      <td>2.6±0.2</td>
      <td>64.5±6.7</td>
      <td>–61.9±6.9</td>
      <td>0.8±0.4</td>
      <td>–96.3±15.7</td>
      <td>97.1±16.0</td>
    </tr>
    <tr>
      <td rowspan="12">K243A</td>
      <td rowspan="4" colspan="2">R188A</td>
      <td>288</td>
      <td>–0.4±0.2</td>
      <td>28.1±11.0</td>
      <td>–28.5±10.8</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>–0.7±0.2</td>
      <td>3.0±5.0</td>
      <td>–3.7±5.0</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–0.5±0.1</td>
      <td>–22.1±5.4</td>
      <td>21.6±5.4</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>0.1±0.2</td>
      <td>–47.2±11.5</td>
      <td>47.3±11.8</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4" colspan="2">R238A</td>
      <td>288</td>
      <td>1.9±0.2</td>
      <td>6.1±8.0</td>
      <td>–4.1±7.8</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>293</td>
      <td>2.0±0.1</td>
      <td>–48.4±5.3</td>
      <td>50.4±5.3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>4.0±0.1</td>
      <td>–100.6±6.2</td>
      <td>104.6±6.2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>5.9±0.2</td>
      <td>–151.6±9.9</td>
      <td>157.5±10.2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R188A</td>
      <td rowspan="4">R238A</td>
      <td>288</td>
      <td>6.7±0.2</td>
      <td>23.3±9.2</td>
      <td>–16.6±8.9</td>
      <td>–5.2±0.4</td>
      <td>10.9±16.4</td>
      <td>–16.0±16.0</td>
    </tr>
    <tr>
      <td>293</td>
      <td>6.6±0.4</td>
      <td>5.0±5.1</td>
      <td>1.6±4.9</td>
      <td>–5.2±0.5</td>
      <td>–50.4±8.9</td>
      <td>45.1±8.8</td>
    </tr>
    <tr>
      <td>298</td>
      <td>6.8±0.2</td>
      <td>–13.3±3.9</td>
      <td>20.1±4.0</td>
      <td>–3.3±0.2</td>
      <td>–109.4±9.2</td>
      <td>106.1±9.2</td>
    </tr>
    <tr>
      <td>303</td>
      <td>7.3±0.2</td>
      <td>–31.6±8.7</td>
      <td>38.9±8.9</td>
      <td>–1.3±0.4</td>
      <td>–167.2±17.5</td>
      <td>165.9±17.9</td>
    </tr>
  </tbody>
</table>

### Dissecting KDL binding to the interior and exterior site(s) of MsbA

An open question is if the interior and exterior LOS binding sites of MsbA are allosterically coupled? We focused on the R188A and K299A mutants located at the exterior and interior binding sites, respectively. Results for both single mutants were presented above. MsbA containing the R188A and K299A mutations drastically reduced the binding of KDL (Figure 4a). The ΔG for MsbAR188A,K299A increased by more than 6 kJ/mol compared to the wild-type protein (Figure 4b). This approximately doubles compared to MsbA containing either of the single point mutations. Mutant cycle analysis revealed a negative coupling energy of –1.1±0.4 kJ/mol that partitioned into a coupling enthalpy of –36±13 kJ/mol and coupling entropy of 34±13 kJ/mol at 298 K (Figure 4b and Table 3). In short, mutations at either LOS binding site have a negative impact on binding that is accompanied by a gain in both favorable entropy and unfavorable enthalpy.

![Figure 4.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig4-v1.jpg)

**Figure 4.:** (a) Thermodynamic signatures for MsbA and mutants binding KDL at 298 K. (b–c) Double mutant cycle analysis for R188 and K299. Shown are results for the first (panel b) and second (panel c) KDL binding to MsbA. Shown from left to right is ΔΔG, ΔΔH and Δ(-TΔS) and the values indicated over the respective arrows at 298 K. Reported are the average and standard deviation from repeated measurements (n = 3).

### Mutant cycle analysis of KDL binding to vanadate-trapped MsbA

As MsbA, like other ABC transporters, is highly dynamic, we sought to trap the transporter in an OF conformation using ADP and vanadate to interrogate binding at the exterior lipid binding site. We characterized the binding of KDL to vanadate-trapped MsbA and proteins containing single R188A, R238A, and K243A mutations (Table 5). Here, we focused on the binding of the first and second lipid, since MsbA has two, symmetrically related KDL binding sites in the open, OF conformation. Thermodynamics of MsbA(KDL)1-2 binding is like the non-trapped transporter, wherein entropy (-TΔS ranging from –58±1 to -69±1 kJ/mol at 298 K) is more favorable than a positive enthalpic term (ΔH ranging from 22±1–35±1 kJ/mol) (Figure 5a, Figure 5—figure supplements 1–6 and Table 6). The single mutant proteins (MsbAR188A, MsbAR238A, and MsbAK243A) showed a slight increase in ΔG (at most 5 kJ/mol) (Figure 5a, Figure 5—figure supplements 1–6). Notably, we found MsbAR238A and MsbAK243A had about a four-fold increase in ΔH and favorable entropy was about two-fold higher (Figure 5a, Figure 5—figure supplements 1–6). Double mutant cycle analysis of the pairwise mutants revealed a positive coupling energy of ~2 kJ/mol for MsbA binding one and two KDLs (Figure 5b, Figure 5—figure supplements 1–6 and Table 7). Focusing on the first KDL binding event, the coupling enthalpy and coupling entropy at 298 K for R188 and K238 was 89±7 kJ/mol and –87±7 kJ/mol, respectively (Figure 5b, Figure 5—figure supplements 1–6 and Tables 7 and 8). Likewise, R238 and K243 showed 129±11 kJ/mol of coupling enthalpy and –127±11 kJ/mol of coupling entropy at 298 K (Figure 5b, Figure 5—figure supplements 1–6 and Tables 7 and 8). However, the R188 and K243 pair revealed a relatively low coupling enthalpy and coupling entropy at 298 K of 3.5±7 kJ/mol and 2±7 kJ/mol, respectively (Figure 5b, Figure 5—figure supplements 1–6 and Tables 7 and 8). These results highlight the importance of entropic and enthalpic contributions that underpin specific lipid binding sites.

![Figure 5.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig5-v1.jpg)

**Figure 5.:** (a) Thermodynamic signatures for MsbA and mutants binding KDL at 298 K. (b–c) Double mutant cycle analysis for pairs of R188, R238, and K243 with a total of three combinations. Shown are results for the first (panel b) and second (panel c) KDL binding to MsbA trapped in an open, OF conformation with ADP and vanadate. Within each panel, ΔΔG, ΔΔH and Δ(-TΔS) are shown from left to right and their values at 298 K are indicated over the respective arrows. Reported are the average and standard deviation from repeated measurements (n = 3).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** The concentration of MsbA, MsbAR188A, MsbAR238A, and MsbAK243A is 0.82, 0.86, 0.78, and 0.57 μM, respectively. The temperature in Celsius is provided in the inset.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** The concentration of MsbAR188A,R238A, MsbAR188A,R243A, and MsbAR238A,K243A is 0.44, 0.23, and 0.73 μM, respectively. The temperature is provided in the inset.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** Shown as described in Figure 2—figure supplement 2.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig5-figsupp4-v1.jpg)

**Figure 5—figure supplement 4.:** Shown as described in Figure 2—figure supplement 2.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig5-figsupp5-v1.jpg)

**Figure 5—figure supplement 5.:** Shown as described in Figure 2—figure supplement 3.

![Figure 5—figure supplement 6.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig5-figsupp6-v1.jpg)

**Figure 5—figure supplement 6.:** Shown as described in Figure 2—figure supplement 3.

**Table 5.**
 Equilibrium dissociation constants (KD) for KDL binding MsbA trapped with ADP and vanadate at various temperatures.Reported are the mean and standard deviation (n=3).


<table>
  <thead>
    <tr>
      <th></th>
      <th>Temperature(K)</th>
      <th>KD1(μM)</th>
      <th>KD2(μM)</th>
      <th>KD3(μM)</th>
      <th>R2*</th>
      <th>Χ2*</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">WT</td>
      <td>293</td>
      <td>0.51±0.04</td>
      <td>1.16±0.07</td>
      <td></td>
      <td>0.97</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td>298</td>
      <td>0.44±0.02</td>
      <td>0.93±0.09</td>
      <td></td>
      <td>0.94</td>
      <td>0.17</td>
    </tr>
    <tr>
      <td>303</td>
      <td>0.38±0.02</td>
      <td>0.73±0.05</td>
      <td></td>
      <td>0.94</td>
      <td>0.15</td>
    </tr>
    <tr>
      <td>310</td>
      <td>0.31±0.01</td>
      <td>0.53±0.04</td>
      <td></td>
      <td>0.92</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td rowspan="4">R188A</td>
      <td>293</td>
      <td>1.56±0.09</td>
      <td>3.46±0.15</td>
      <td>10.98±1.15</td>
      <td>0.98</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>298</td>
      <td>1.53±0.11</td>
      <td>3.40±0.21</td>
      <td>10.15±1.62</td>
      <td>0.98</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td>303</td>
      <td>1.35±0.10</td>
      <td>2.90±0.26</td>
      <td>9.02±1.11</td>
      <td>0.98</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>310</td>
      <td>0.93±0.09</td>
      <td>1.89±0.24</td>
      <td>5.50±1.10</td>
      <td>0.97</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td rowspan="4">R238A</td>
      <td>293</td>
      <td>1.67±0.23</td>
      <td>6.71±1.38</td>
      <td></td>
      <td>0.99</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>298</td>
      <td>0.91±0.10</td>
      <td>3.15±0.12</td>
      <td></td>
      <td>0.98</td>
      <td>0.06</td>
    </tr>
    <tr>
      <td>303</td>
      <td>0.34±0.04</td>
      <td>1.09±0.23</td>
      <td>3.75±0.60</td>
      <td>0.95</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>310</td>
      <td>0.10±0.02</td>
      <td>0.33±0.11</td>
      <td>0.92±0.38</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="4">K243A</td>
      <td>293</td>
      <td>2.01±0.06</td>
      <td>5.26±0.85</td>
      <td></td>
      <td>0.99</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>298</td>
      <td>1.46±0.01</td>
      <td>3.90±0.48</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>303</td>
      <td>0.60±0.02</td>
      <td>1.54±0.12</td>
      <td>3.72±0.54</td>
      <td>0.98</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>310</td>
      <td>0.25±0.02</td>
      <td>0.46±0.02</td>
      <td>1.06±0.04</td>
      <td>0.89</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td rowspan="4">R188A R238A</td>
      <td>293</td>
      <td>1.24±0.10</td>
      <td>4.82±0.16</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>298</td>
      <td>1.17±0.11</td>
      <td>4.65±0.92</td>
      <td></td>
      <td>0.99</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>303</td>
      <td>0.87±0.06</td>
      <td>3.05±0.26</td>
      <td></td>
      <td>0.98</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>310</td>
      <td>0.39±0.05</td>
      <td>1.28±0.09</td>
      <td>6.36±1.07</td>
      <td>0.98</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td rowspan="4">R188A K243A</td>
      <td>293</td>
      <td>3.64±0.28</td>
      <td>15.66±4.76</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>298</td>
      <td>2.23±0.07</td>
      <td>6.68±0.17</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>303</td>
      <td>1.06±0.05</td>
      <td>3.10±0.33</td>
      <td>19.33±3.70</td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>310</td>
      <td>0.66±0.02</td>
      <td>1.56±0.04</td>
      <td>5.70±0.93</td>
      <td>0.98</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td rowspan="4">R238A K243A</td>
      <td>293</td>
      <td>1.31±0.04</td>
      <td>4.35±0.07</td>
      <td></td>
      <td>0.99</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>298</td>
      <td>1.03±0.09</td>
      <td>3.65±0.15</td>
      <td></td>
      <td>0.99</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>303</td>
      <td>0.48±0.05</td>
      <td>1.97±0.09</td>
      <td></td>
      <td>0.97</td>
      <td>0.09</td>
    </tr>
    <tr>
      <td>310</td>
      <td>0.10±0.02</td>
      <td>0.58±0.06</td>
      <td></td>
      <td>0.74</td>
      <td>0.93</td>
    </tr>
  </tbody>
</table>

_These values represent the replicates with the poorest fits._

**Table 6.**
 Thermodynamic signatures of KDL interacting with wild-type and mutant MsbA trapped with ADP and vanadate.Reported are the mean with standard deviation (n=3), and the subscript denotes the nth KDL binding event.


<table>
  <thead>
    <tr>
      <th></th>
      <th>T(K)</th>
      <th>ΔG1(kJ/mol)</th>
      <th>ΔH1(kJ/mol)</th>
      <th>-TΔS1(kJ/mol)</th>
      <th>ΔCp1 (kJ/mol/K)</th>
      <th>ΔG2(kJ/mol)</th>
      <th>ΔH2(kJ/mol)</th>
      <th>-TΔS2(kJ/mol)</th>
      <th>ΔCp2 (kJ/mol/K)</th>
      <th>ΔG3(kJ/mol)</th>
      <th>ΔH3(kJ/mol)</th>
      <th>-TΔS3(kJ/mol)</th>
      <th>ΔCp3 (kJ/mol/K)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">WT</td>
      <td>293</td>
      <td>–35.3±0.1</td>
      <td>21.9±1.5</td>
      <td>–57.2±1.3</td>
      <td></td>
      <td>–33.3±0.2</td>
      <td>35.0±0.6</td>
      <td>–68.3±0.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–36.3±0.1</td>
      <td>21.9±1.5</td>
      <td>–58.2±1.3</td>
      <td></td>
      <td>–34.4±0.2</td>
      <td>35.0±0.6</td>
      <td>–69.4±0.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–37.3±0.1</td>
      <td>21.9±1.5</td>
      <td>–59.2±1.3</td>
      <td></td>
      <td>–35.6±0.2</td>
      <td>35.0±0.6</td>
      <td>–70.6±0.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>310</td>
      <td>–38.6±0.1</td>
      <td>21.9±1.5</td>
      <td>–60.5±1.3</td>
      <td></td>
      <td>–37.2±0.2</td>
      <td>35.0±0.6</td>
      <td>–72.2±0.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R188A</td>
      <td>293</td>
      <td>–32.6±0.1</td>
      <td>–6.6±2.6</td>
      <td>–26.0±2.7</td>
      <td>3.6±0.1</td>
      <td>–30.7±0.1</td>
      <td>–7.2±2.4</td>
      <td>–23.4±2.5</td>
      <td>4.1±0.2</td>
      <td>–27.8±0.3</td>
      <td>–3.2±21.3</td>
      <td>–24.7±21.1</td>
      <td>4.1±2.7</td>
    </tr>
    <tr>
      <td>298</td>
      <td>–33.2±0.2</td>
      <td>11.3±2.6</td>
      <td>–44.5±2.7</td>
      <td>3.5±0.1</td>
      <td>–31.2±0.1</td>
      <td>13.4±3.3</td>
      <td>–44.7±3.4</td>
      <td>4.2±0.3</td>
      <td>–28.5±0.4</td>
      <td>17.6±12.4</td>
      <td>–46.1±12.3</td>
      <td>3.6±4.2</td>
    </tr>
    <tr>
      <td>303</td>
      <td>–34.1±0.2</td>
      <td>29.2±2.5</td>
      <td>–63.3±2.6</td>
      <td>3.6±0.1</td>
      <td>–32.2±0.2</td>
      <td>34.1±4.3</td>
      <td>–66.3±4.5</td>
      <td>4.1±0.2</td>
      <td>–29.3±0.3</td>
      <td>37.8±14.8</td>
      <td>–67.1±15.1</td>
      <td>4.9±1.4</td>
    </tr>
    <tr>
      <td>310</td>
      <td>–35.8±0.2</td>
      <td>54.3±2.6</td>
      <td>–90.2±2.8</td>
      <td>3.6±0.1</td>
      <td>–34.0±0.3</td>
      <td>63.0±5.8</td>
      <td>–97.0±6.1</td>
      <td>4.1±0.2</td>
      <td>–31.3±0.5</td>
      <td>67.9±26.1</td>
      <td>–99.2±26.6</td>
      <td>4.3±2.2</td>
    </tr>
    <tr>
      <td rowspan="4">R238A</td>
      <td>293</td>
      <td>–32.1±0.2</td>
      <td>126.8±5.8</td>
      <td>–158.9±5.9</td>
      <td></td>
      <td>–28.9±0.4</td>
      <td>137.7±10.8</td>
      <td>–166.5±10.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–34.8±0.4</td>
      <td>126.8±5.8</td>
      <td>–161.6±6.0</td>
      <td></td>
      <td>–31.7±0.4</td>
      <td>137.7±10.8</td>
      <td>–169.4±11.0</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–37.6±0.4</td>
      <td>126.8±5.8</td>
      <td>–164.3±6.1</td>
      <td></td>
      <td>–34.6±0.5</td>
      <td>137.7±10.8</td>
      <td>–172.2±11.1</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>310</td>
      <td>–41.4±0.5</td>
      <td>126.8±5.8</td>
      <td>–168.1±6.2</td>
      <td></td>
      <td>–38.5±0.7</td>
      <td>137.7±10.8</td>
      <td>–176.2±11.4</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">K243A</td>
      <td>293</td>
      <td>–31.6±0.1</td>
      <td>96.2±5.1</td>
      <td>–127.9±5.1</td>
      <td></td>
      <td>–29.1±0.2</td>
      <td>111.7±6.9</td>
      <td>–140.8±6.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–33.8±0.1</td>
      <td>96.2±5.1</td>
      <td>–130.0±5.1</td>
      <td></td>
      <td>–31.5±0.1</td>
      <td>111.7±6.9</td>
      <td>–143.2±6.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–36.0±0.1</td>
      <td>96.2±5.1</td>
      <td>–132.2±5.3</td>
      <td></td>
      <td>–33.9±0.1</td>
      <td>111.7±6.9</td>
      <td>–145.6±6.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>310</td>
      <td>–39.1±0.2</td>
      <td>96.2±5.1</td>
      <td>–135.3±5.4</td>
      <td></td>
      <td>–37.3±0.2</td>
      <td>111.7±6.9</td>
      <td>–149±7.1</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R188A R238A</td>
      <td>293</td>
      <td>–33.2±0.2</td>
      <td>–10.2±3.0</td>
      <td>–23.0±3.1</td>
      <td>7.5±1.0</td>
      <td>–29.8±0.1</td>
      <td>–8.2±30.4</td>
      <td>–21.7±30.3</td>
      <td>8.1±3.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–33.9±0.2</td>
      <td>27.2±2.5</td>
      <td>–61.0±2.6</td>
      <td>7.5±0.3</td>
      <td>–30.5±0.5</td>
      <td>31.9±13.7</td>
      <td>–62.4±14.2</td>
      <td>8.6±4.6</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–35.2±0.2</td>
      <td>64.5±7.3</td>
      <td>–99.7±7.2</td>
      <td>7.5±2.1</td>
      <td>–32.0±0.2</td>
      <td>72.5±4.9</td>
      <td>–104.5±4.8</td>
      <td>7.4±1.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>310</td>
      <td>–38.1±0.4</td>
      <td>116.9±16.4</td>
      <td>–155.0±16.8</td>
      <td>7.5±1.3</td>
      <td>–35.0±0.2</td>
      <td>127.7±25.9</td>
      <td>–162.7±25.9</td>
      <td>7.9±3.0</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R188A K243A</td>
      <td>293</td>
      <td>–30.5±0.2</td>
      <td>92.4±8.6</td>
      <td>–122.9±8.4</td>
      <td>–1.8±0.9</td>
      <td>–27.0±0.7</td>
      <td>135.4±44.8</td>
      <td>–162.4±44.1</td>
      <td>–4.0±4.0</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–32.3±0.1</td>
      <td>82.1±4.4</td>
      <td>–114.4±4.3</td>
      <td>–0.1±0.9</td>
      <td>–29.5±0.1</td>
      <td>114.7±25.2</td>
      <td>–144.2±25.2</td>
      <td>–3.4±4.5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–34.7±0.1</td>
      <td>73.4±0.1</td>
      <td>–108.0±0.1</td>
      <td>–4.4±0.8</td>
      <td>–32.0±0.3</td>
      <td>94.5±5.7</td>
      <td>–126.5±5.6</td>
      <td>–4.9±3.8</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>310</td>
      <td>–36.7±0.1</td>
      <td>55.6±5.7</td>
      <td>–92.3±5.7</td>
      <td>–2.6±0.8</td>
      <td>–34.5±0.1</td>
      <td>64.4±22.9</td>
      <td>–98.9±22.9</td>
      <td>–4.3±3.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R238A K243A</td>
      <td>293</td>
      <td>–33.0±0.1</td>
      <td>8.9±14.2</td>
      <td>–41.9±14.2</td>
      <td>12.7±2.7</td>
      <td>–30.1±0.1</td>
      <td>6.5±2.2</td>
      <td>–36.6±2.1</td>
      <td>10.0±0.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>–34.2±0.2</td>
      <td>71.8±7.2</td>
      <td>–106.0±7.4</td>
      <td>13.2±2.1</td>
      <td>–31.0±0.1</td>
      <td>56.1±2.1</td>
      <td>–87.1±2.2</td>
      <td>10.5±0.9</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–36.7±0.2</td>
      <td>135.3±16.2</td>
      <td>–171.9±16.3</td>
      <td>11.9±3.5</td>
      <td>–33.1±0.1</td>
      <td>106.2±5.4</td>
      <td>–139.3±5.5</td>
      <td>9.1±1.0</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>310</td>
      <td>–41.6±0.8</td>
      <td>222.4±35.8</td>
      <td>–264.0±36.5</td>
      <td>12.4±2.9</td>
      <td>–37.0±0.3</td>
      <td>174.4±10.5</td>
      <td>–211.4±10.8</td>
      <td>9.7±0.7</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

**Table 7.**
 Double mutant cycle analysis of the first KDL binding to wild-type and mutant MsbA trapped with ADP and vanadate.Shown as described in Table 3.


<table>
  <thead>
    <tr>
      <th colspan="2"></th>
      <th>Temperature(K)</th>
      <th>ΔΔG(kJ/mol)</th>
      <th>ΔΔH(kJ/mol)</th>
      <th>Δ(-TΔS)(kJ/mol)</th>
      <th>ΔΔGint(kJ/mol)</th>
      <th>ΔΔHint(kJ/mol)</th>
      <th>Δ(-ΔTS)int(kJ/mol)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4" colspan="2">R188A</td>
      <td>293</td>
      <td>2.7±0.1</td>
      <td>–28.5±3.1</td>
      <td>31.2±3.1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>3.1±0.2</td>
      <td>–10.6±2.9</td>
      <td>13.7±3.1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>3.2±0.2</td>
      <td>7.3±2.9</td>
      <td>–4.1±2.9</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>310</td>
      <td>2.8±0.2</td>
      <td>32.4±2.9</td>
      <td>–29.7±3.1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4" colspan="2">R238A</td>
      <td>293</td>
      <td>3.2±0.2</td>
      <td>104.9±6.0</td>
      <td>–101.7±6.0</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>1.5±0.4</td>
      <td>104.9±6.0</td>
      <td>–103.4±6.1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>–0.3±0.4</td>
      <td>104.9±6.0</td>
      <td>–105.1±6.2</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>310</td>
      <td>–2.8±0.5</td>
      <td>104.9±6.0</td>
      <td>–107.6±6.4</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4" colspan="2">K243A</td>
      <td>293</td>
      <td>3.7±0.1</td>
      <td>74.3±5.4</td>
      <td>–70.7±5.3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>2.5±0.1</td>
      <td>74.3±5.4</td>
      <td>–71.8±5.3</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>1.3±0.1</td>
      <td>74.3±5.4</td>
      <td>–73.0±5.4</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>310</td>
      <td>–0.5±0.2</td>
      <td>74.3±5.4</td>
      <td>–74.8±5.5</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R188A</td>
      <td rowspan="4">R238A</td>
      <td>293</td>
      <td>2.2±0.2</td>
      <td>–32.1±3.3</td>
      <td>34.2±3.4</td>
      <td>3.8±0.4</td>
      <td>108.5±7.0</td>
      <td>–104.7±7.2</td>
    </tr>
    <tr>
      <td>298</td>
      <td>2.4±0.2</td>
      <td>5.3±2.9</td>
      <td>–2.8±2.9</td>
      <td>2.2±0.5</td>
      <td>89.0±6.9</td>
      <td>–86.9±7.1</td>
    </tr>
    <tr>
      <td>303</td>
      <td>2.1±0.2</td>
      <td>42.6±7.5</td>
      <td>–40.5±7.3</td>
      <td>0.8±0.5</td>
      <td>69.6±9.6</td>
      <td>–68.7±9.8</td>
    </tr>
    <tr>
      <td>310</td>
      <td>0.5±0.4</td>
      <td>95.0±16.5</td>
      <td>–94.5±16.8</td>
      <td>–0.5±0.6</td>
      <td>42.4±17.6</td>
      <td>–42.8±18.1</td>
    </tr>
    <tr>
      <td rowspan="4">R188A</td>
      <td rowspan="4">K243A</td>
      <td>293</td>
      <td>4.8±0.2</td>
      <td>70.5±8.7</td>
      <td>–65.7±8.6</td>
      <td>1.6±0.2</td>
      <td>–24.7±10.4</td>
      <td>26.3±10.3</td>
    </tr>
    <tr>
      <td>298</td>
      <td>4.0±0.1</td>
      <td>60.2±4.7</td>
      <td>–56.2±4.5</td>
      <td>1.6±0.2</td>
      <td>3.5±7.2</td>
      <td>–1.9±7.2</td>
    </tr>
    <tr>
      <td>303</td>
      <td>2.6±0.1</td>
      <td>51.5±1.5</td>
      <td>–48.8±1.3</td>
      <td>1.9±0.2</td>
      <td>30.1±5.8</td>
      <td>–28.2±5.9</td>
    </tr>
    <tr>
      <td>310</td>
      <td>1.9±0.1</td>
      <td>33.7±5.9</td>
      <td>–31.8±5.9</td>
      <td>0.4±0.4</td>
      <td>73.0±8.1</td>
      <td>–72.7±8.3</td>
    </tr>
    <tr>
      <td rowspan="4">R238A</td>
      <td rowspan="4">K243A</td>
      <td>293</td>
      <td>2.3±0.1</td>
      <td>–13.0±14.3</td>
      <td>15.3±14.2</td>
      <td>4.6±0.2</td>
      <td>192.2±16.2</td>
      <td>–187.7±16.2</td>
    </tr>
    <tr>
      <td>298</td>
      <td>2.1±0.2</td>
      <td>49.9±7.3</td>
      <td>–47.8±7.6</td>
      <td>1.9±0.4</td>
      <td>129.3±10.5</td>
      <td>–127.4±10.9</td>
    </tr>
    <tr>
      <td>303</td>
      <td>0.6±0.2</td>
      <td>113.4±16.3</td>
      <td>–112.7±16.4</td>
      <td>0.4±0.5</td>
      <td>65.8±17.9</td>
      <td>–65.4±18.2</td>
    </tr>
    <tr>
      <td>310</td>
      <td>–3.0±0.9</td>
      <td>200.5±35.8</td>
      <td>–203.5±36.5</td>
      <td>–0.4±1.0</td>
      <td>–21.3±36.6</td>
      <td>21.1±37.5</td>
    </tr>
  </tbody>
</table>

**Table 8.**
 Double mutant cycle analysis of the second KDL binding to wild-type and mutant MsbA trapped with ADP and vanadate.Shown as described in Table 3.


<table>
  <thead>
    <tr>
      <th colspan="2"></th>
      <th>Temperature(K)</th>
      <th>ΔΔG(kJ/mol)</th>
      <th>ΔΔH(kJ/mol)</th>
      <th>Δ(-TΔS)(kJ/mol)</th>
      <th>ΔΔGint(kJ/mol)</th>
      <th>ΔΔHint(kJ/mol)</th>
      <th>Δ(-ΔTS)int(kJ/mol)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4" colspan="2">R188A</td>
      <td>293</td>
      <td>2.7±0.2</td>
      <td>–42.2±2.4</td>
      <td>44.9±2.6</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>3.2±0.2</td>
      <td>–21.6±3.3</td>
      <td>24.8±3.4</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>3.5±0.4</td>
      <td>–0.9±4.4</td>
      <td>4.3±4.5</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>310</td>
      <td>3.2±0.4</td>
      <td>28.0±5.9</td>
      <td>–24.8±6.1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4" colspan="2">R238A</td>
      <td>293</td>
      <td>4.4±0.5</td>
      <td>102.7±10.8</td>
      <td>–98.2±10.8</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>2.7±0.5</td>
      <td>102.7±10.8</td>
      <td>–100.0±11.0</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>1.0±0.5</td>
      <td>102.7±10.8</td>
      <td>–101.6±11.1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>310</td>
      <td>–1.3±0.7</td>
      <td>102.7±10.8</td>
      <td>–104.0±11.4</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4" colspan="2">K243A</td>
      <td>293</td>
      <td>4.2±0.4</td>
      <td>76.7±6.9</td>
      <td>–72.5±6.6</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>298</td>
      <td>2.9±0.2</td>
      <td>76.7±6.9</td>
      <td>–73.8±6.7</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>303</td>
      <td>1.7±0.2</td>
      <td>76.7±6.9</td>
      <td>–75.0±6.9</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>310</td>
      <td>–0.1±0.4</td>
      <td>76.7±6.9</td>
      <td>–76.8±7.1</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">R188A</td>
      <td rowspan="4">R238A</td>
      <td>293</td>
      <td>3.5±0.2</td>
      <td>–43.2±30.4</td>
      <td>46.7±30.3</td>
      <td>3.6±0.4</td>
      <td>103.7±32.3</td>
      <td>–100.0±32.2</td>
    </tr>
    <tr>
      <td>298</td>
      <td>3.9±0.5</td>
      <td>–3.1±13.7</td>
      <td>7.0±14.2</td>
      <td>2.0±0.6</td>
      <td>84.2±17.8</td>
      <td>–82.3±18.2</td>
    </tr>
    <tr>
      <td>303</td>
      <td>3.6±0.4</td>
      <td>37.5±4.9</td>
      <td>–33.9±4.8</td>
      <td>0.9±0.6</td>
      <td>64.3±12.6</td>
      <td>–63.3±13.0</td>
    </tr>
    <tr>
      <td>310</td>
      <td>2.2±0.2</td>
      <td>92.7±25.8</td>
      <td>–90.5±25.8</td>
      <td>–0.3±0.9</td>
      <td>38.0±28.7</td>
      <td>–38.3±28.9</td>
    </tr>
    <tr>
      <td rowspan="4">R188A</td>
      <td rowspan="4">K243A</td>
      <td>293</td>
      <td>6.3±0.7</td>
      <td>100.4±44.8</td>
      <td>–94.1±44.1</td>
      <td>0.6±0.7</td>
      <td>–65.9±45.4</td>
      <td>66.5±44.7</td>
    </tr>
    <tr>
      <td>298</td>
      <td>4.9±0.2</td>
      <td>79.7±25.2</td>
      <td>–74.8±25.2</td>
      <td>1.2±0.2</td>
      <td>–24.6±26.3</td>
      <td>25.8±26.3</td>
    </tr>
    <tr>
      <td>303</td>
      <td>3.6±0.4</td>
      <td>59.5±5.8</td>
      <td>–55.9±5.6</td>
      <td>1.5±0.4</td>
      <td>16.3±9.9</td>
      <td>–14.7±9.9</td>
    </tr>
    <tr>
      <td>310</td>
      <td>2.7±0.2</td>
      <td>29.4±22.9</td>
      <td>–26.7±22.9</td>
      <td>0.4±0.4</td>
      <td>75.3±24.6</td>
      <td>–74.9±24.7</td>
    </tr>
    <tr>
      <td rowspan="4">R238A</td>
      <td rowspan="4">K243A</td>
      <td>293</td>
      <td>3.2±0.2</td>
      <td>–28.5±2.2</td>
      <td>31.7±2.2</td>
      <td>5.4±0.5</td>
      <td>207.9±13.0</td>
      <td>–202.4±12.9</td>
    </tr>
    <tr>
      <td>298</td>
      <td>3.4±0.2</td>
      <td>21.1±2.2</td>
      <td>–17.7±2.3</td>
      <td>2.2±0.4</td>
      <td>158.3±13.0</td>
      <td>–156.1±13.1</td>
    </tr>
    <tr>
      <td>303</td>
      <td>2.5±0.2</td>
      <td>71.2±5.4</td>
      <td>–68.7±5.5</td>
      <td>0.2±0.5</td>
      <td>108.2±13.8</td>
      <td>–107.9±14.2</td>
    </tr>
    <tr>
      <td>310</td>
      <td>0.2±0.4</td>
      <td>139.4±10.5</td>
      <td>–139.2±10.8</td>
      <td>–1.6±0.9</td>
      <td>40.0±16.5</td>
      <td>–41.6±17.3</td>
    </tr>
  </tbody>
</table>

## Discussion

Thermodynamics provide unique insight into the molecular forces that drive specific MsbA-KDL interactions. A recurring thermodynamic strategy for specific KDL-MsbA interactions is a large, favorable entropic term that opposes a positive enthalpic value. The human G-protein-gated inward rectifier potassium channel (Kir3.2) also used a similar thermodynamic strategy to engage phosphoinositides (PIPs) (Qiao et al., 2021). The large, positive entropy could stem from solvent reorganization of the lipid with a carbohydrate containing headgroup, and desolvation of hydrated binding pockets on the membrane protein. The release of ordered solvent to the bulk solvent would contribute favorably to entropy. These experiments are performed in detergent and reorganization of detergent may also play a role. Previous work has shown soluble protein-ligand interactions can be driven by a large, positive entropy term that outweighs a large, positive enthalpic penalty (Frederick et al., 2007; Tzeng and Kalodimos, 2009; Tzeng and Kalodimos, 2012; Caro et al., 2017). In these cases, the reaction is mainly driven by conformational entropy originating in enhanced protein motions. However, it is unclear if the conformational dynamics of MsbA are enhanced when bound to KDL.

Most of the van’ t Hoff plots followed non-linear trends, indicating Cp is not constant over the selected temperature range (Prabhu and Sharp, 2005). In nearly all cases, a positive ΔCp was observed that ranged in value from 4 to 12 kJ/mol·K (Tables 2 and 6). Solvation of polar groups in aqueous solvent has been ascribed to positive heat capacities whereas the collapse of apolar residues from their solvated state is accompanied by a negative change in heat capacity (Prabhu and Sharp, 2005; Makhatadze and Privalov, 1995). Reorganization of the hydrated, polar headgroups of KD is consistent with the positive heat capacity observed here. However, change in heat capacity could also be ascribed to temperature-dependent conformational changes in MsbA and/or KDL. Notably, vanadate-trapped MsbA locked in an open, OF conformation should be less conformationally dynamic than the apo protein, which is known to adopt a number of open, IF conformations where the NBDs are separated by different distances. Similar positive heat capacities were observed for the different conformations, suggesting the dynamics of MsbA marginally contribute to the observed non-linear trends. Notably, the headgroup of KDL is nestled in a hydrophilic, basic patch of MsbA in the open, OF conformation. Similarly, the headgroup of PIP binds a hydrophilic, basic pocket in Kir3.2. These hydrophilic patches will be highly solvated, which will be desolvated upon binding lipids contributing favorably to entropy.

Thermodynamics of MsbA-lipid interactions contrast those observed for a different membrane protein. Phospholipid binding to the bacterial ammonia channel (AmtB) were largely driven by enthalpy and, in most cases, entropy was unfavorable (Cong et al., 2016). Another interesting observation for AmtB-lipid interactions was significant enthalpy-entropy compensation for each sequential lipid binding event. Here, enthalpy-entropy compensation is not as pronounced. This result may reflect the much higher affinity and specific MsbA-KDL interactions compared to the weaker AmtB-lipid interactions, sometimes referred to as non-annular lipids (Bolla et al., 2019). Moreover, we have focused the titration here to characterize the binding of the first three KDL molecules to MsbA. While we can’t rule out that the resolved lipid bound states of MsbA represent binding of lipid to one or multiple site(s) on the transporter, the mole fraction plots are suggestive of binding to distinct sites, that is smooth inflections. In a previous study, (Qiao et al., 2021) we observed abnormal binding curves for some PIPs binding to Kir3.2 that we rationalized by the presence of high-affinity binding and low-affinity binding sites. A revised equilibrium binding model including the two-site model dramatically improved the fits, leading to dissection of at least two lipid binding sites. Further studies are warranted to better understand the binding sites of KDL to MsbA in different conformations.

Results of this study begin to draw a connection between LPS binding at the interior and exterior sites of MsbA. It is presently thought that flipping of LOS occurs at interior MsbA site, and the exterior LOS binding site enables feedforward activation, wherein binding of LOS and precursors thereof stimulates ATPase activity (Mi et al., 2017; Ho et al., 2018; Lyu et al., 2022; Gorzelak et al., 2021; Ward et al., 2007; Zou and McHaourab, 2009; Dong et al., 2005). It is also thought that binding of LOS and ATP promotes dimerization of the NBDs. Here, we find mutations at either the interior or exterior sites have a direct impact of KDL binding to MsbA, which under these conditions is presumably adopting an open, IF conformation. Of the mutant proteins, MsbA containing single mutations (MsbAR188A,K299A) at both LOS binding sites resulted in the greatest change in ΔG. This result implies that these sites are allosterically coupled and further investigation is warranted to better understand how the exterior LOS binding sites influence MsbA dynamics.

A defining feature of this work is the use of mutant cycles to not only characterize specific membrane protein-lipid interactions but define the coupling energies of specific residue-lipid interactions in terms of enthalpic and entropic contributions. Traditionally, mutant cycles have been used to understand pairwise interactions of residues, such as in protein-protein complexes, in terms of coupling free energy. Here, we extend mutant cycles to understand how pairs of residues contribute to specific MsbA-KDL interactions. Double mutants targeting the interior site reveal a positive coupling energy of nearly 2 kJ/mol for R78 and K299. These stabilize the MsbA-KDL complex largely through nearly 17 kJ/mol of favorable coupling entropy, which outweighs a negative coupling enthalpy. This phenomenon extends to nearly all mutant cycles investigated in this work, even when the transporter is trapped with vanadate. The largest coupling energy is observed from the triple mutant cycle of R188A, R238A, and R243A, which again stabilization of the complex was achieved via favorable coupling entropy. While we focused on results at 298 K, the coupling energetics among these three residues show 3.4±0.5 kJ/mol. Taken together, mutant cycle analysis reveals that entropy drives high-affinity KDL binding to MsbA and solvent reorganization contributes to KDL binding (Figure 6). There are many factors that contribute to the change in entropy of the system, beyond solvation entropy, and deciphering the entropic contributions of the various components warrants additional studies.

![Figure 6.](https://cdn.elifesciences.org/articles/91094/elife-91094-fig6-v1.jpg)

**Figure 6.:** The lipid headgroup and binding pocket (basic patch illustrated in blue) on the membrane protein are solvated. The ordered solvent (shown in light blue) is then displaced upon lipid binding the membrane protein leading to solvent reorganization. The displacement of ordered solvent (show in light green) contributes to favorable entropy. This process enables the formation of a high affinity, stable membrane protein-lipid complex.

While the use of mutant cycles was prominent a few decades ago, native mass spectrometry opens new opportunities to revisit the classical approach, diving deeper into the energetics of non-covalent interactions, such as dissecting energetics in terms of enthalpic and entropic contributions. Native MS coupled with a variable-temperature nanoelectrospray ionization (nESI) apparatus (McCabe et al., 2021; Cong et al., 2016) has been used to ascertain equilibrium binding constants and thermodynamic properties of protein-protein and protein-ligand interactions. The results obtained align closely with those obtained through other biophysical techniques, such as isothermal titration calorimetry (ITC) and surface plasmon resonance (SPR) (Cong et al., 2017; Daneshfar et al., 2004; Daneshfar et al., 2004; Cong et al., 2016). The approach has also uncovered that specific protein-lipid interactions can allosterically modulate other interactions with protein, lipid, and drug molecules (Marcoux et al., 2013; Yen et al., 2018; Cong et al., 2017; Patrick et al., 2018; Bolla et al., 2018; Gault et al., 2016). More recently, native MS has proved useful in dissecting the thermodynamics of individual nucleotide binding events to GroEL, a 801 kDa tetradecameric chaperonin (Walker et al., 2023). In contrast to traditional approaches, such as ITC and SPR, native MS can resolve and dissect individual binding events enabling the measurement of binding thermodynamics, which is of paramount importance to understanding the molecular driving forces of non-covalent interactions.

In summary, we demonstrate the utility of native MS to determine the thermodynamic origins of specific KDL-MsbA interactions. Combined with the classical mutant cycle approach, (Carter et al., 1984) the thermodynamic contribution of specific interactions with lipids is illuminated. More specifically, MsbA binding KDL is solely driven by entropy, which overcomes an enthalpic penalty. A similar thermodynamic strategy was also observed for Kir3.2-PIP interactions, where entropy plays a central role in the wild-type channel recognizing PIP (Qiao et al., 2021). It is tempting to speculate that favorable entropy is a common theme enabling membrane proteins to specifically engage carbohydrate-containing lipids. We envision thermodynamics and mutant cycles will be invaluable in not only better understanding high-affinity lipid binding sites but also in the development of inhibitors, such as those that may target specific protein-lipid binding site(s). In closing, these studies provide deeper insight into the thermodynamic strategies membrane proteins exploit to achieve high-affinity lipid binding site(s).

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
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BL21-AI</td>
      <td>Invitrogen</td>
      <td>C607003</td>
      <td>Chemically Competent E. coli</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>5-alpha</td>
      <td>NEB</td>
      <td>C2987H</td>
      <td>Chemically Competent E. coli</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCDF-His_TEV_MsbA (plasmid)</td>
      <td>DOI: 10.1038 /s41467-022-34905-2</td>
      <td></td>
      <td>MsbA expression construct</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>MsbA_R78A_F</td>
      <td>This Paper</td>
      <td>PCR primers</td>
      <td>gcgGGTATCACCAGCTATGTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>MsbA_R78A_R</td>
      <td>This Paper</td>
      <td>PCR primers</td>
      <td>CAAAATCATCAGCCCGATC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>MsbA_R188A_F</td>
      <td>DOI: 10.1038 /s41467-022-34905-2</td>
      <td>PCR primers</td>
      <td>gcgTTTCGCAACATCAGTAAAAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>MsbA_R188A_R</td>
      <td>DOI: 10.1038 /s41467-022-34905-2</td>
      <td>PCR primers</td>
      <td>CTTCGATACTACGCGAATC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>MsbA_R238A_F</td>
      <td>DOI: 10.1038 /s41467-022-34905-2</td>
      <td>PCR primers</td>
      <td>gcgCTTCAGGGGATGAAAATG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>MsbA_R238A_R</td>
      <td>DOI: 10.1038 /s41467-022-34905-2</td>
      <td>PCR primers</td>
      <td>CATTCGGTTGCTGACTTTATC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>MsbA_K243A_F</td>
      <td>DOI: 10.1038 /s41467-022-34905-2</td>
      <td>PCR primers</td>
      <td>gcgATGGTTTCAGCCTCTTCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>MsbA_K243A_R</td>
      <td>DOI: 10.1038 /s41467-022-34905-2</td>
      <td>PCR primers</td>
      <td>CATCCCCTGAAGACGCAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>MsbA_K299A_F</td>
      <td>This Paper</td>
      <td>PCR primers</td>
      <td>gcgTCGCTGACTAACGTTAACGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>MsbA_K299A_R</td>
      <td>This Paper</td>
      <td>PCR primers</td>
      <td>CAGCGGACGCATCAGTGC</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>DC Protein Assay</td>
      <td>Bio-Rad</td>
      <td>5000112</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Kdo2-Lipid A (KLA)</td>
      <td>Avanti</td>
      <td>699500</td>
      <td></td>
    </tr>
  </tbody>
</table>

### MsbA expression constructs

MsbA and mutants were essentially expressed and purified as previously described (Lyu et al., 2022). In detail, the MsbA gene (from Escherichia coli genomic DNA) was amplified by polymerase chain reaction (PCR) using Q5 High-Fidelity DNA Polymerase (New England Biolabs, NEB) and subcloned into a modified pCDF-1b plasmid (Novagen) resulting in expression of MsbA with an N-terminal TEV protease cleavable His6 fusion protein. Primers for generating mutations for MsbA were designed using the online tool NEBaseChanger (NEB) and carried out using the KLD enzyme mix (NEB) as described by the manufacturer. All plasmids were transformed into E. coli 5-alpha (NEB) competent cells for plasmids propagation before confirmed by DNA sequencing.

### Protein expression and purification

MsbA expression plasmids were transformed into E. coli (DE3) BL21-AI competent cells (Invitrogen). A single colony was picked and used to inoculate 50 mL LB media to be grown overnight at 37 °C with shaking. The overnight culture was used to inoculate to terrific broth (TB) media and incubated at 37 °C until the OD600nm ≈ 0.6–1.0. After which, the cultures were induced with final concentration of 0.5 mM IPTG (isopropyl β-D-1-thiogalactopryanoside) and 0.2% (w/v) arabinose. After overnight expression at 25 °C, the cultures were harvested at 4000 x g for 10 minutes and the resulting pellet was resuspended in lysis buffer (20 mM Tris, 300 mM NaCl and pH at 7.4 at room temperature). The resuspended cells were centrifuged, and the pellet was then resuspended in lysis buffer. Cells were lysed by four passages through a Microfluidics M-110P microfluidizer operating at 25,000 psi with reaction chamber emersed in an ice bath. The lysate was clarified by centrifugation at 20,000 x g for 25 min and the supernatant was centrifuged at 100,000 x g for 2 hr to pellet membranes. Resuspension buffer (20 mM Tris, 150 mM NaCl, 20% (v/v) glycerol, pH 7.4) was used to homogenize the resulting pellet and 1% (m/v) DDM was added for protein extraction overnight at 4 °C. The extraction was centrifuged at 20,000 x g for 25 min and the resulting supernatant was supplemented with 10 mM imidazole and filtered with a 0.45 µm syringe filter prior to purification by immobilized metal affinity chromatography. The extraction containing solubilized MsbA was loaded onto a column packed with 2.5 mL Ni-NTA resin pre-equilibrated in NHA-DDM buffer (20 mM Tris, 150 mM NaCl, 10 mM imidazole, 10% (v/v) glycerol, pH 7.4 and supplemented with 2 x the critical micelle concentration (CMC) of DDM). After the loading, the column was washed with 5 column volumes (CV) of NHA-DDM buffer, 10 CV of NHA-DDM buffer supplemented with additional 2% (w/v) nonyl-ß-glucoside (NG), and 5 CV of NHA-DDM buffer. The immobilized protein was eluted with the addition of 2 CV of NHB-DDM buffer (20 mM Tris, 150 mM NaCl, 250 mM imidazole, 10% (v/v) glycerol, 2 x CMC of DDM, pH 7.4). The eluted MsbA was pooled and desalted using HiPrep 26/10 desalting column (GE Healthcare) pre-equilibrated in desalting buffer (NHA-DDM with imidazole omitted). TEV protease (expressed and purified in-house) was added to the desalted MsbA sample and incubated overnight at room temperature. The sample was passed over a pre-equilibrated Ni-NTA column and the flow-through containing the cleaved MsbA protein was collected. The pooled protein was concentrated using a centrifugal concentrator (Millipore, 100 kDa) prior to injection onto a Superdex 200 Increase 10/300 GL (GE Healthcare) column equilibrated with 20 mM Tris, 150 mM NaCl, 10% (v/v) glycerol and 2 x CMC C10E5. Peak fractions containing dimeric MsbA were pooled, flash frozen in liquid nitrogen, and stored at –80 °C prior to use.

### Preparation of MsbA for native MS studies

MsbA samples were incubated with 20 µM copper (II) acetate, to saturate the N-terminal metal binding site, (Lyu et al., 2022) prior to buffer exchange using a centrifugal buffere exchange device (Bio-Spin, Bio-Rad) into 200 mM ammonium acetate supplemented with 2 x CMC of C10E5. To prepare vanadate-trapped MsbA, ATP and MgCl2 were added to MsbA at a final concentration of 10 mM. After incubation at room temperature for 10 min, a freshly boiled vanadate solution (pH 10) was added to reach final concentration of 1 mM followed by incubation at 37 °C for an additional 10 min. The sample was then buffer exchanged as described above.

### Native Mass Spectrometry

Samples were loaded into gold-coated glass capillaries made in-house (Laganowsky et al., 2013) and introduced into at a Thermo Fisher Scientific Exactive Plus Orbitrap with Extended Mass Range (EMR) using native electrospray ionization source modified with a variable temperature apparatus (McCabe et al., 2021). For native mass analysis, the instrument was tuned as follow: source DC offset of 10 V, injection flatapole DC to 8.0 V, inter flatapole lens to 4, bent flatapole DC to 3, transfer multipole DC to 3 and C trap entrance lens to 0, trapping gas pressure to 6.0 with the in-source CID to 65.0 eV and CE to 100, spray voltage to 1.70 kV, capillary temperature to 200 °C, maximum inject time to 200ms. Mass spectra were acquired with a setting of 17,500 resolution, microscans set to 1 and averaging set to 100.

### Determination MsbA-lipid equilibrium binding constants

KDL (Avanti) stock solution was prepared by dissolving lipid powder in water. The concentration of MsbA and KDL were determined by a DC protein assay (BioRad) and phosphorus assay, respectively (Chen et al., 1956; Fiske and Subbarow, 1925). MsbA was incubated with varying concentrations of KDL before loading into a glass emitter and mounted on a variable-temperature electrospray ionization (vT-ESI) source (McCabe et al., 2021). Samples were incubated in the source for two minutes at the desired temperature before data acquisition. All titration data were collected in triplicate (n=3), with a 20 min interval between each measurement. Reported are the mean and standard deviation. At a given temperature, the mass spectra were deconvoluted using Unidec (Marty et al., 2015) and the peak intensities for apo and KDL-bound species were determined and converted to mole fraction. The sequential ligand binding model was applied to determine the mole fraction of each species in measurement:

$$
PL_{n−1}+ L ⇔K_{A}PL_{n}
$$

where:

$$
K_{An}=\frac{PL_{n}}{[PL_{n-1}]L}
$$

To calculate the mole fraction of a particular species (Cong et al., 2016):

$$
F_{PLn}=\frac{L_{free}^{n}\prod_{j=1}^{n}K_{Aj}}{1+\sum_{i=1}^{n}L_{free}^{i}\prod_{j=1}^{n}K_{Aj}}
$$

For each titrant in the titration, the free concentration of lipid was computed as follows:

$$
L_{free}=L_{total}-P_{total}\sumi=0niF_{PLi}
$$

The sequential ligand binding model was globally fit to the mole fraction data by minimization of pseudo- $χ^{2}$ function:

$$
χ^{2}= \sum_{j=1}^{m}\sum_{k=1}^{d}(F_{i,j,exp}-F_{i,j,calc})^{2}
$$

where n is the number of bound ligands and d is the number of the experimental mole fraction data points.

Van’t Hoff analysis (van’t Hoff, 1884) was applied to determine the Gibbs free energy change (ΔG), enthalpy change (ΔH) and entropy change (ΔS) based on the equation:

$$
ln⁡K_{A}=−\frac{ΔH}{R}⋅\frac{1}{T}+\frac{ΔS}{R}
$$

For non-linear trends, the non-linear form of the Van’t Hoff equation was applied to determine the thermodynamic parameters (Liu and Sturtevant, 1996):

$$
ln⁡K_{A}=\frac{ΔH_{T_{0}}−T_{0}ΔC_{p}}{R}(\frac{1}{T_{0}}−\frac{1}{T})+\frac{ΔC_{p}}{R}ln⁡(\frac{T}{T_{0}})+ln⁡K_{0}
$$

where KA is the equilibrium association constant, K0 is the equilibrium association constant at the reference temperature (T0), $\DeltaH_{T_{0}}$ is the standard enthalpy at T0, ΔCp is the change in heat capacity at constant pressure, and R is the universal gas constant.

### Mutant cycle analysis

If the two mutated residues are interacting, then the coupling free energy (ΔΔGint) will not be 0 and the value may be positive or negative depending upon whether the interactions between mutated residues enhance or weaken the functional property measured. (Wells, 1990) ΔΔGint can be computed given the change in Gibbs free energy for the wild-type protein (P), two single mutants (PX and PY), and double mutant (PXY) as follows:

$$
\Delta\DeltaG_{int}=\Delta\DeltaG_{PX→P}+\Delta\DeltaG_{PY→P}-\Delta\DeltaG_{PXY→P}
$$

where $\Delta\DeltaG_{PX→P}=\DeltaG_{PX}-\DeltaG_{P}$ , $\Delta\DeltaG_{PY→P}=\DeltaG_{PY}-\DeltaG_{P}$ and $\Delta\DeltaG_{PXY→P}=\DeltaG_{PXY}-\DeltaG_{P}.$ Analogously, the contributions from coupling enthalpy (ΔΔHint) and coupling entropy (Δ(-TΔSint)) can be computed as follows:

$$
\Delta\DeltaH_{int}=\Delta\DeltaH_{PX→P}+\Delta\DeltaH_{PY→P}-\Delta\DeltaH_{PXY→P}
$$



$$
\Delta(-T\DeltaS_{int})=\Delta(-T\DeltaS_{PX→P})+\Delta(-T\DeltaS_{PY→P})-\Delta(-T\DeltaS_{PXY→P})
$$

where T is temperature in K. As an example, $\Delta\DeltaH_{PX→P}=\DeltaH_{PX}-\DeltaH_{P}$ and $\Delta-T\DeltaG_{PX→P}=T\DeltaS_{P}-T\DeltaS_{PX}$ .
