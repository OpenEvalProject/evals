# Unanticipated mechanisms of covalent inhibitor and synthetic ligand cobinding to PPARγ

## Authors

- Jinsai Shang<sup>1</sup> ([ORCID: 0000-0001-8164-1544](https://orcid.org/0000-0001-8164-1544)) †
- Douglas J Kojetin<sup>1</sup> ([ORCID: 0000-0001-8058-6168](https://orcid.org/0000-0001-8058-6168)) †

### Affiliations

1. Department of Integrative Structural and Computational Biology, Scripps Research and The Herbert Wertheim UF Scripps Institute for Biomedical Innovation & Technology Jupiter United States ([ROR:056pdzs28](https://ror.org/056pdzs28))
2. School of Basic Medical Sciences, Guangzhou Laboratory, Guangzhou Medical University Guangzhou China ([ROR:00zat6v61](https://ror.org/00zat6v61))
3. Department of Biochemistry, Vanderbilt University Nashville United States ([ROR:02vm5rt34](https://ror.org/02vm5rt34))
4. Center for Structural Biology, Vanderbilt University Nashville United States ([ROR:02vm5rt34](https://ror.org/02vm5rt34))
5. Vanderbilt Institute of Chemical Biology, Vanderbilt University Nashville United States ([ROR:02vm5rt34](https://ror.org/02vm5rt34))
6. Center for Applied AI in Protein Dynamics, Vanderbilt University Nashville United States ([ROR:02vm5rt34](https://ror.org/02vm5rt34))

† Corresponding author

## Abstract

Peroxisome proliferator-activated receptor gamma (PPARγ) is a nuclear receptor transcription factor that regulates gene expression programs in response to ligand binding. Endogenous and synthetic ligands, including covalent antagonist inhibitors GW9662 and T0070907, are thought to compete for the orthosteric pocket in the ligand-binding domain (LBD). However, we previously showed that synthetic PPARγ ligands can cooperatively cobind with and reposition a bound endogenous orthosteric ligand to an alternate site, synergistically regulating PPARγ structure and function (Shang et al., 2018). Here, we reveal the structural mechanism of cobinding between a synthetic covalent antagonist inhibitor with other synthetic ligands. Biochemical and NMR data show that covalent inhibitors weaken—but do not prevent—the binding of other ligands via an allosteric mechanism, rather than direct ligand clashing, by shifting the LBD ensemble toward a transcriptionally repressive conformation, which structurally clashes with orthosteric ligand binding. Crystal structures reveal different cobinding mechanisms including alternate site binding to unexpectedly adopting an orthosteric binding mode by altering the covalent inhibitor binding pose. Our findings highlight the significant flexibility of the PPARγ orthosteric pocket, its ability to accommodate multiple ligands, and demonstrate that GW9662 and T0070907 should not be used as chemical tools to inhibit ligand binding to PPARγ.

## Introduction

Peroxisome proliferator-activated receptor γ (PPARγ) is a ligand-regulated nuclear receptor transcription factor that regulates gene expression programs controlling adipogenesis and insulin sensitization. Endogenous PPARγ ligands, which include lipids and fatty acids, bind to an orthosteric pocket within the PPARγ ligand-binding domain (LBD) and function as PPARγ agonists that activate gene programs (Itoh et al., 2008; Li et al., 2008; Malapaka et al., 2012; Kliewer et al., 1997; Kliewer et al., 1995; Waku et al., 2009; Shang et al., 2018). Synthetic small molecule PPARγ ligands, which include FDA-approved antidiabetic drugs, also bind to the same orthosteric pocket, most of which function as agonists that activate PPARγ-mediated transcription. Endogenous and synthetic ligands were originally thought to compete for binding to the PPARγ orthosteric pocket. However, we previously showed that endogenous and synthetic ligands can cobind to PPARγ, likely due to the large size and flexibility of the orthosteric pocket, and synergistically influence PPARγ structure and function (Johnson et al., 2000).

The structural mechanism of agonist-induced activation of PPARγ transcription has been revealed by structural biology studies including NMR spectroscopy and crystal structures. In the absence of ligand, the apo (ligand-free) PPARγ LBD dynamically exchanges between two or more structural conformations (Shang et al., 2020). NMR data show that a critical structural element in the LBD called activation function-2 (AF-2) helix (helix 12), which is part of the AF-2 coactivator binding surface, exchanges between active and repressive conformations that can be stabilized upon binding ligand (Hughes et al., 2012). Agonist binding to the orthosteric pocket stabilizes a solvent exposed helix 12 conformation that enables high-affinity binding of coactivators and increases transcription (Shang et al., 2019; Frkic et al., 2023). Transcriptionally neutral antagonists and repressive inverse agonists developed from orthosteric agonist ligand scaffolds bind via a similar mechanism of agonists but stabilize non-active helix 12 conformations (Frkic et al., 2018; Zheng et al., 2018; Marciano et al., 2015; Lee et al., 2002).

GW9662 and T0070907 are covalent ligands originally described as antagonists as they bind via a nucleophilic substitution mechanism to Cys285 located within the orthosteric pocket and were shown to inhibit binding of select reference PPARγ agonists (Leesnitzer et al., 2002; Hughes et al., 2014). These ligands have been used extensively by the field as covalent antagonist inhibitors to block other synthetic ligands from binding PPARγ to test for synthetic ligand specificity in functional experiments. However, we previously showed GW9662 and T0070907 do not block all ligands from binding to PPARγ Johnson et al., 2000; Hughes et al., 2016; Brust et al., 2017; MacTavish et al., 2024 — and moreover, they have distinct pharmacological PPARγ functions as a transcriptionally neutral antagonist (GW9662) and repressive inverse agonist (T0070907) (Irwin et al., 2022). Although these covalent ligands have similar pharmacological functions to orthosteric non-covalent antagonists and inverse agonists, GW9662 and T0070907 function through a different structural mechanism: they slow the rate of exchange between transcriptionally active and repressive conformations natively populated in the apo-LBD, with T0070907 having a more pronounced effect than GW9662 (Hughes et al., 2012; Orsi et al., 2023). In the transcriptionally repressive conformation stabilized by covalent inverse agonists, helix 12 adopts a solvent-occluded conformation within the orthosteric pocket that overlaps with orthosteric ligand binding poses (Figure 1; Hughes et al., 2012; Orsi et al., 2023; Shang and Kojetin, 2021; Arifi et al., 2023). These and other published studies have informed a ligand activation model whereby agonist binding to the orthosteric pocket either displaces helix 12 from a solvent occluded repressive conformation within the orthosteric pocket to a solvent exposed active conformation, or selects for an active helix 12 conformation from the dynamic LBD ensemble (Jang et al., 2017).

![Figure 1.](https://cdn.elifesciences.org/articles/99782/elife-99782-fig1-v1.jpg)

**Figure 1.:** The active LBD (PDB 6ONJ) is stabilized by agonist (rosiglitazone) and coactivator peptide (TRAP220/MED1), whereas the repressive LBD (PDB 6ONI) is stabilized by covalent inverse agonist (T0070907) and corepressor peptide (NCoR1).

What remains unclear is the structural basis of covalent inhibitor and synthetic ligand cobinding. This ligand cobinding mechanism was originally discovered in studies of alternate site ligand binding (Hughes et al., 2016; Brust et al., 2017; MacTavish et al., 2024; Laghezza et al., 2018; Leijten-van de Gevel et al., 2022; Choi et al., 2011; Berger et al., 2003). Structural studies have mapped the alternate ligand-binding site (Hughes et al., 2016; Brust et al., 2017) when two equivalents of a synthetic ligand bind, one to the orthosteric pocket and another to the entrance of the orthosteric pocket (Jang et al., 2017). NMR and biochemical data revealed non-covalent synthetic compounds can still bind to the PPARγ LBD in the presence of a covalent orthosteric inhibitor (Hughes et al., 2016; Brust et al., 2017; MacTavish et al., 2024). While it is presumed that the non-covalent synthetic compound adopts a non-orthosteric binding mode at an alternate site, crystal structures to verify this cobinding mechanism are still needed. Here, using structural biology studies including NMR and crystallography, we confirm that GW9662 and T0070907 do not prevent other synthetic ligands from binding to PPARγ. Furthermore, we demonstrate that certain synthetic ligands can unexpectedly adopt an orthosteric binding pose when cobound with a covalent antagonist inhibitor.

## Results

### Covalent inhibitor and synthetic ligand cobinding influences PPARγ LBD function

We assembled a set of four non-covalent synthetic PPARγ ligands (BVT-13, MRL24, nTZDpa, and SR1664) previously shown to bind the PPARγ LBD via two molar equivalents or bind in the presence of a covalent ligand, GW9662 or T0070907 (Hughes et al., 2016; Figure 2A). In that previous study, we showed that an analog of MRL24, called MRL20, can activate PPARγ-mediated transcription and increase the expression of PPARγ target genes in differentiated mouse 3T3-L1 preadipocytes when cells were correlated with GW9662 or T0070907 covalent inhibitors. Using a time-resolved fluorescence resonance energy transfer (TR-FRET) biochemical ligand displacement assay, we verified the ligands bind PPARγ LBD with Ki values (Figure 2B) consistent with published data (Ostberg et al., 2004; Acton et al., 2005; Ge et al., 2002; Yu et al., 2005). These ligands are generally classified as partial agonists that activate PPARγ transcription with limited or weak efficacy, or non-agonists/antagonists that are transcriptionally neutral.

![Figure 2.](https://cdn.elifesciences.org/articles/99782/elife-99782-fig2-v1.jpg)

**Figure 2.:** (A) Chemical structures of the compounds. (B) TR-FRET ligand displacement data for the compounds (n=3; mean ±s.d.).

We profiled the non-covalent synthetic ligands using TR-FRET coregulator peptide interaction assays (Figure 3A) to determine how the compounds affect interaction between the PPARγ LBD and peptides derived from NCoR1 corepressor and TRAP220/MED1 coactivator proteins, two coregulator proteins that influence PPARγ transcription in cells (Nolte et al., 1998; Bruning et al., 2007). Consistent with their partial agonist and/or antagonist profiles, the compounds did not significantly increase interaction with the TRAP220 coactivator peptide. Only two compounds, nTZDpa and SR1664, caused notable changes in the coactivator TR-FRET assay. Of these, nTZDpa showed a biphasic transition that may be due to the binding of more than one nTZDpa molecule, which is also suggested by 2D [1H,15N]-TROSY-HSQC NMR data where chemical shift perturbations (CSPs) are observed going from 1 to 2 equivalents of added ligand.

![Figure 3.](https://cdn.elifesciences.org/articles/99782/elife-99782-fig3-v1.jpg)

**Figure 3.:** (A) TR-FRET coregulator interaction assays performed using PPARγ LBD protein with or without preincubation of GW9662 or T0070907 to determine how the non-covalent synthetic ligands influence recruitment of peptides derived from NCoR1 corepressor protein and TRAP220/MED1 coactivator protein fit to a sigmoidal dose response equation or biphasic dose response equation for select cases where a biphasic response is observed (n=3; mean ± s.d.). (B) IC50 and EC50 values extracted from the TR-FRET coregulator interaction data. For curves showing a biphasic response, the higher affinity value is displayed; no value is displayed in cases where the dose response is flat. Error bars when present represent the fitted errors; some fits did not converge to a well-fitted error. See Figure 3—source data 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/99782/elife-99782-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** 2D [1H,15N]-TROSY-HSQC NMR data of 15N-labeled PPARγ LBD in the absence or presence of nTZDpa added at the indicated molar equivalents.

We next performed TR-FRET coregulator interaction assays using PPARγ LBD protein that was first pretreated with a covalent ligand, GW9662 or T0070907, followed by titration of the non-covalent synthetic ligands. When bound to GW9662 or T0070907, corepressor peptide binding affinity to the LBD is progressively strengthened upon binding to GW9662 and T0070907 while coactivator peptide affinity is weakened according to their neutral and repressive pharmacological activities, respectively (Orsi et al., 2023). As a result of this change in coregulator affinity, the baseline TR-FRET signal progressively increases in the corepressor assay and decreases in the coactivator assay. Titration of the synthetic ligands shows notable changes in the NCoR1 corepressor TR-FRET assay, where the ligands decrease NCoR1 peptide interaction with IC50 profiles (Figure 3B) with a similar rank-order to ligand Ki values (MRL24 <nTZDpa < SR1664<BVT.13). Relatively minor changes are observed for the ligands in the TRAP220/MED1 coactivator TR-FRET assay except for MRL24, which shows a concentration-dependent increase in coactivator peptide recruitment. Taken together, these data indicate the functional effect of synthetic ligands binding to PPARγ LBD in the presence of a covalent inhibitor is decreased corepressor peptide interaction. Notably, the synthetic ligand IC50 values are weakened (right shifted) more by the inverse agonist T0070907 compared to the neutral antagonist GW9662, suggesting that pharmacological repressive ligand efficacy may be involved in the ligand cobinding inhibitory mechanism.

### NMR studies indicate covalent inhibitors allosterically weaken cobinding of non-covalent synthetic ligands by stabilizing a repressive conformation

Two mechanisms may contribute to the covalent inhibitor mechanism of weakening synthetic ligand cobinding. The covalent ligands could structurally overlap or clash with synthetic ligand orthosteric binding modes, leading to alternate site binding with a reduced binding affinity. In this case, the relatively simple phenyl group (GW9662) to pyridyl group (T0070907) change would somehow lead to a more robust clash between the covalent inhibitor and synthetic ligand. Alternatively, the TR-FRET data suggested a different mechanism that involves the repressive efficacy of the covalent ligand. The pharmacological shift from a neutral covalent antagonist (GW9662) to repressive covalent inverse agonist (T0070907) may allosterically shift the dynamic LBD ensemble towards a transcriptionally repressive conformation, where helix 12 adopts a solvent occluded conformation within the orthosteric pocket that structurally clashes with orthosteric binding of a synthetic ligand. In this case, synthetic ligand binding to T0070907-bound PPARγ LBD would significantly influence the NMR-detected repressive LBD conformation where helix 12 is within the orthosteric pocket more than the active LBD conformation where helix 12 is solvent exposed and not occluding the orthosteric pocket.

To structurally assess the non-covalent cobinding mechanism, we performed protein NMR footprinting by comparing 2D [1H,15N]-TROSY-HSQC NMR data of 15N-labeled PPARγ LBD preincubated with a covalent ligand (GW9662 or T0070907) in the absence or presence of a synthetic ligand. Non-covalent ligand cobinding to GW9662-bound LBD shows NMR CSPs for select peaks (Figure 4A). In contrast, NMR CSPs are more pronounced for non-covalent ligand binding to T0070907-bound LBD (Figure 4B). Focusing on Gly399, a residue near the AF-2 surface that displays two T0070907-bound NMR peaks in slow exchange corresponding to the active or repressive LBD state but only one GW9662-bound active state peak (Hughes et al., 2012; Irwin et al., 2022; Orsi et al., 2023), cobinding of the non-covalent synthetic ligand causes the two NMR peaks in slow exchange to converge to one NMR peak. The NMR peaks corresponding to the repressive T0070907-bound conformation disappear, while the remaining peaks have NMR chemical shift values similar to the T0070907-bound active state but shifted along the active-repressive continuum (i.e. diagonal between the active and repressive T0070907-bound NMR peaks) that correlates with function (Orsi et al., 2023).

![Figure 4.](https://cdn.elifesciences.org/articles/99782/elife-99782-fig4-v1.jpg)

**Figure 4.:** Overlays of 2D [1H,15N]-TROSY-HSQC NMR data of 15N-labeled PPARγ LBD preincubated with covalent inhibitor, (A) GW9662 or (B) T0070907, in the absence or presence of the indicated non-covalent synthetic ligands added at 2 molar equivalents. (C) Overlays of 2D [1H,15N]-TROSY-HSQC NMR data of 15N-labeled PPARγ LBD in the presence of non-covalent synthetic ligands (singly bound state) compared to the cobound states with a covalent inhibitor.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/99782/elife-99782-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** 2D [1H,15N]-TROSY-HSQC NMR data of 15N-labeled PPARγ LBD in the presence of the indicated ligands added at 2 molar equivalents.

Among the synthetic ligands we tested, MRL24 cobinding shows an increase in TRAP220 coactivator peptide recruitment to T0070907-bound PPARγ LBD and the largest shift NMR-detected shift of the LBD conformational ensemble towards an active state. In contrast, nTZDpa cobinding shows an antagonist-like profile in the TR-FRET data, decreasing both NCoR1 corepressor and to a lesser degree TRAP220 coactivator interaction, and shifts the NMR-detected shift of the LBD conformational ensemble towards an intermediate state between the active and repressive T0070907-observed populations.

Taken together, these NMR-detected observations support the mechanism whereby the repressive conformation helix 12 within the orthosteric pocket of T0070907-bound LBD is displaced to a solvent-exposed active conformation. Furthermore, comparison of 2D [1H,15N]-TROSY-HSQC NMR data of 15N-labeled PPARγ LBD bound to the synthetic ligands alone, or cobound with GW9662 or T0070907, show similar spectral profiles with more subtle CSPs (Figure 4C) compared to the larger NMR CSPs observed when comparing 15N-labeled PPARγ LBD bound to each synthetic ligand alone or T0070907-bound LBD relative to GW9662-bound LBD (Figure 4—figure supplement 1; Hughes et al., 2012). This suggests the active conformation of the PPARγ LBD when bound to a synthetic ligand alone vs. cobound to a covalent ligand are similar, which is supported by the TR-FRET data (Figure 3) showing that synthetic ligand cobinding to T0070907-bound PPARγ LBD decreases corepressor peptide interaction.

### Crystal structures reveal disparate alternate site ligand binding poses

To visualize the ligand cobinding poses, we first crystalized complexes of PPARγ LBD covalently bound to GW9662 or T0070907, which produced solvent exposed active (chain A) and inactive (chain B) helix 12 conformations similar to apo-PPARγ LBD (Bae et al., 2016), then we added synthetic ligands to the crystals using soaking methods. We obtained seven crystal structures in total where each synthetic ligand was cobound to either GW9662 or T0070907, except for SR1664 for which we only obtained a structure cobound to T0070907 (Table 1, Figure 5—figure supplement 1). In most structures, electron density was observed for non-covalent and covalent ligands in both chains. However, in the nTZDpa structures, the covalent ligand was not observed in chain A; and nTZDpa was observed in chains A and B when cobound to GW9662, but only chain B when cobound to T0070907. The structures show high structural similarity to the transcriptionally active LBD conformation with rmsd values ranging from 0.77 to 1.03 Å (Table 2).

**Table 1.**
 X-ray crystallography data collection and refinement statistics.


<table>
  <thead>
    <tr>
      <th></th>
      <th>PPARγ LBD bound to GW9662 and BVT.13</th>
      <th>PPARγ LBD bound to GW9662 and MRL24</th>
      <th>PPARγ LBD bound to GW9662 and nTZDpa</th>
      <th>PPARγ LBD bound to T0070907 and BVT.13</th>
      <th>PPARγ LBD bound to T0070907 and MRL24</th>
      <th>PPARγ LBD bound to T0070907 and nTZDpa</th>
      <th>PPARγ LBD bound to T0070907 and SR1664</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data collection*</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>C 1 2 1</td>
      <td>C 1 2 1</td>
      <td>C 1 2 1</td>
      <td>C 1 2 1</td>
      <td>C 1 2 1</td>
      <td>C 1 2 1</td>
      <td>C 1 2 1</td>
    </tr>
    <tr>
      <td>Cell dimensions</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>92.19, 61.99, 118.84</td>
      <td>91.84, 62.22, 119.24</td>
      <td>92.75, 62.22, 119.08</td>
      <td>92.64, 61.78, 119.13</td>
      <td>92.42, 61.63, 119.55</td>
      <td>93.02, 62.16, 119.46</td>
      <td>93.88, 62.68, 121.04</td>
    </tr>
    <tr>
      <td>α, β, γ (°)</td>
      <td>90, 102.38, 90</td>
      <td>90, 102.28, 90</td>
      <td>90, 102.19, 90</td>
      <td>90, 102.38, 90</td>
      <td>90, 102.19, 90</td>
      <td>90, 102.14, 90</td>
      <td>90, 102.46, 90</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>51.06–2.54(2.63–2.54)</td>
      <td>49.06–2.48(2.57–2.48)</td>
      <td>49.16–3.15(3.26–3.15)</td>
      <td>51.02–2.49(2.58–2.49)</td>
      <td>58.43–2.56(2.65–2.56)</td>
      <td>58.39–2.73(2.83–2.73)</td>
      <td>59.09–3.2(3.31–3.2)</td>
    </tr>
    <tr>
      <td>Rmerge</td>
      <td>0.088 (1.159)</td>
      <td>0.132 (1.791)</td>
      <td>0.043 (0.212)</td>
      <td>0.076 (1.083)</td>
      <td>0.087 (1.367)</td>
      <td>0.108 (1.621)</td>
      <td>0.046 (0.263)</td>
    </tr>
    <tr>
      <td>I / σI</td>
      <td>12.06 (1.38)</td>
      <td>8.54 (1.04)</td>
      <td>15.02 (3.63)</td>
      <td>14.71 (1.76)</td>
      <td>12.80 (1.42)</td>
      <td>10.28 (1.21)</td>
      <td>10.70 (2.94)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>98.14 (96.97)</td>
      <td>98.41 (96.93)</td>
      <td>99.59 (100.00)</td>
      <td>99.14 (99.22)</td>
      <td>99.47 (98.55)</td>
      <td>98.79 (98.27)</td>
      <td>99.87 (100.00)</td>
    </tr>
    <tr>
      <td>Redundancy</td>
      <td>6.6 (6.4)</td>
      <td>6.5 (6.5)</td>
      <td>2.0 (2.0)</td>
      <td>6.6 (6.6)</td>
      <td>6.6 (6.4)</td>
      <td>6.6 (6.7)</td>
      <td>2.0 (2.0)</td>
    </tr>
    <tr>
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
      <td>Refinement</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>2.54</td>
      <td>2.48</td>
      <td>3.15</td>
      <td>2.49</td>
      <td>2.56</td>
      <td>2.73</td>
      <td>3.2</td>
    </tr>
    <tr>
      <td>No. unique reflections</td>
      <td>21761</td>
      <td>23546</td>
      <td>11672</td>
      <td>23269</td>
      <td>21415</td>
      <td>17965</td>
      <td>11555</td>
    </tr>
    <tr>
      <td>Rwork / Rfree</td>
      <td>25.2/31.6</td>
      <td>24.2/29.8</td>
      <td>21.6/29.8</td>
      <td>23.6/29.5</td>
      <td>23.7/27.8</td>
      <td>25.0/30.4</td>
      <td>20.6/28.3</td>
    </tr>
    <tr>
      <td>No. atoms</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>4149</td>
      <td>4065</td>
      <td>3921</td>
      <td>4123</td>
      <td>4066</td>
      <td>4096</td>
      <td>4015</td>
    </tr>
    <tr>
      <td>Ligand/ion</td>
      <td>90</td>
      <td>112</td>
      <td>74</td>
      <td>90</td>
      <td>112</td>
      <td>46</td>
      <td>118</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>35</td>
      <td>82</td>
      <td>2</td>
      <td>43</td>
      <td>21</td>
      <td>18</td>
      <td>0</td>
    </tr>
    <tr>
      <td>B-factors</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>65.80</td>
      <td>53.94</td>
      <td>58.48</td>
      <td>64.00</td>
      <td>64.71</td>
      <td>67.70</td>
      <td>79.58</td>
    </tr>
    <tr>
      <td>Ligand/ion</td>
      <td>74.57</td>
      <td>41.56</td>
      <td>77.08</td>
      <td>74.58</td>
      <td>49.66</td>
      <td>83.90</td>
      <td>108.68</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>55.23</td>
      <td>46.34</td>
      <td>46.73</td>
      <td>51.89</td>
      <td>50.58</td>
      <td>55.19</td>
      <td>n/a</td>
    </tr>
    <tr>
      <td>R.m.s. deviations</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bond lengths (Å)</td>
      <td>0.010</td>
      <td>0.011</td>
      <td>0.013</td>
      <td>0.010</td>
      <td>0.010</td>
      <td>0.012</td>
      <td>0.011</td>
    </tr>
    <tr>
      <td>Bond angles (°)</td>
      <td>1.33</td>
      <td>1.45</td>
      <td>1.43</td>
      <td>1.21</td>
      <td>1.38</td>
      <td>1.35</td>
      <td>1.31</td>
    </tr>
    <tr>
      <td>Ramachandran favored (%)</td>
      <td>92.90</td>
      <td>96.77</td>
      <td>94.33</td>
      <td>96.63</td>
      <td>96.57</td>
      <td>95.01</td>
      <td>92.61</td>
    </tr>
    <tr>
      <td>Ramachandran outliers (%)</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.20</td>
      <td>0.20</td>
      <td>0.21</td>
    </tr>
    <tr>
      <td>PDB accession code</td>
      <td>8ZFN</td>
      <td>8ZFP</td>
      <td>8ZFO</td>
      <td>8ZFQ</td>
      <td>8ZFS</td>
      <td>8ZFR</td>
      <td>8ZFT</td>
    </tr>
  </tbody>
</table>

_*Values in parentheses are for highest-resolution shell._

**Table 2.**
 Structural rmsd comparison of ligand cobound structures to the transcriptionally active PPARγ LBD conformation (PDB 6ONJ).


<table>
  <thead>
    <tr>
      <th>PDB ID</th>
      <th>rmsd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>8ZFP</td>
      <td>0.98</td>
    </tr>
    <tr>
      <td>8ZFO</td>
      <td>0.77</td>
    </tr>
    <tr>
      <td>8ZFQ</td>
      <td>0.97</td>
    </tr>
    <tr>
      <td>8ZFS</td>
      <td>0.95</td>
    </tr>
    <tr>
      <td>8ZFR</td>
      <td>0.92</td>
    </tr>
    <tr>
      <td>8ZFT</td>
      <td>1.00</td>
    </tr>
    <tr>
      <td>8ZFN</td>
      <td>1.03</td>
    </tr>
  </tbody>
</table>

We compared our cobound crystal structures to published structures of PPARγ LBD bound to non-covalent ligands—BVT.13 (Chrisman et al., 2018), MRL24 (Chrisman et al., 2018), nTZDpa Chrisman et al., 2018, and SR1664 alone (Lee et al., 2002) or cobound to NCOA1 coactivator peptide Agirre et al., 2023 —and alone to covalent ligands—GW9662 Johnson et al., 2000 and T0070907 (Irwin et al., 2022). Overall, the LBD conformations when bound to a single ligand or cobound two ligands are highly similar, with only relatively minor conformational changes in certain residue side chains. Although this is largely influenced by the crystallized forms used for soaking, these findings are also consistent with the aforedescribed 2D NMR data, which indicates a similar LBD conformation for these different liganded states.

Focusing on the non-covalent synthetic ligand cobinding poses (Figure 5A), most of the structures surprisingly showed that the ligand adopts a cobound conformation similar to orthosteric binding pose observed in crystals structures of PPARγ LBD bound to the synthetic ligand alone (Figure 5B). Slight reorientations of portions of the synthetic ligand occur to accommodate the cobinding mode, as there are clashes between the synthetic orthosteric and covalent orthosteric ligand binding modes (Figure 5C). Of note, below we use ‘orthosteric binding pose’ to refer to the crystallized ligand conformation when PPARγ LBD is bound to a single ligand.

![Figure 5.](https://cdn.elifesciences.org/articles/99782/elife-99782-fig5-v1.jpg)

**Figure 5.:** (A) Ligand cobinding modes in crystal structures of PPARγ LBD. (B) Comparison of the non-covalent synthetic ligand orthosteric binding mode (singly bound) and ligand cobinding mode with a covalent inhibitor (transparent sticks). Differences between these binding modes are indicated with a black arrow. (C) Structural clashes observed between the covalent inhibitor orthosteric binding mode (transparent sticks) and the non-covalent synthetic ligand binding mode. PDB codes for crystal structures used in the overlays are listed in the Materials and methods section.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/99782/elife-99782-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** All densities are shown from chain B of the cobound structures for (A) GW9662 and BVT.13, (B) T0070907 and BVT.13, (C) GW9662 and MRL24, (D) T0070907 and MRL24, (E) GW9662 and nTZDpa, (F) T0070907 and nTZDpa, and (G) T0070907 and SR1664.

The BVT.13 cobinding pose is similar to its orthosteric binding pose located near the β-sheet. However, the 2,4-dichloro group clashes with the orthosteric GW9662 and T0070907 binding poses, specifically the phenyl and pyridyl groups respectively, resulting in a slight reorientation of the 2,4-dichloro group to accommodate the cobound state. The MRL24 cobinding pose is also similar to its orthosteric ligand binding pose, which was surprising given its larger scaffold size significantly clashes with the orthosteric covalent ligand binding pose. The nTZDpa cobinding pose is also similar to its orthosteric binding pose near the β-sheet. However, the 1-chloro group clashes with the orthosteric covalent ligand binding pose, resulting in a minor reorientation in the cobinding pose. Finally, the SR1664 cobinding pose reveals an alternate site binding mode similar to the crystallized binding pose in the presence of NCOA1 peptide, with a slight reorientation of the benzoic acid group that avoids a clash with the orthosteric T0070907 binding pose. Notably, these alternate site binding modes are distinct from the orthosteric SR1664 binding mode obtained without coregulator peptide, which shows a large steric clash with the orthosteric covalent ligand binding pose.

Focusing on the covalent ligand binding poses, previously determined crystal structures (Hughes et al., 2012) show that GW9662 and T0070907, when bound alone, are oriented in different directions within the orthosteric pocket in the active state when soaked into apo-PPARγ LBD or repressive state when cobound to NCoR1 corepressor peptide, pointing towards or away from the β-sheet surface, respectively (Figure 6A). Cobinding of a non-covalent synthetic ligand has different effects on the covalent ligand binding pose (Figure 6B). For BVT.13, the covalent ligand cobinding pose is similar to the orthosteric binding pose. For MRL24, the cobound covalent ligands adopt a similar binding pose that is different from the active and repressive orthosteric binding poses. For nTZDpa, the cobound covalent ligands adopt different orientations, both of which are distinct from the active and repressive covalent ligand only-bound states. For SR1664, the cobinding mode of T0070907 is similar to the orthosteric binding mode. These structures show that the conformation of the covalent ligand can change and adapt to the cobound non-covalent ligand.

![Figure 6.](https://cdn.elifesciences.org/articles/99782/elife-99782-fig6-v1.jpg)

**Figure 6.:** (A) Structural overlay showing the orthosteric binding modes of GW9662 and T0070907 in crystal structures of PPARγ LBD in active and repressive conformations. (B) Comparison of the covalent binding modes when singly bound (orthosteric) and cobound to a non-covalent synthetic ligand. Black arrows indicate the conformational differences between the orthosteric binding modes vs. cobinding modes. PDB codes for crystal structures used in the overlays are listed in the Materials and methods section.

Notably, orthosteric ligand Ki values for the non-covalent compounds (Figure 2B) correlate with the ability of the non-covalent ligand to push the covalent ligand into a cobinding binding mode that is distinct from the active and repressive covalent ligand binding modes (Figure 6B). MRL24 and nTZDa, which are the most potent non-covalent ligands tested, pushed the covalent ligands into different non-natural conformations, whereas BVT.13 and SR1664 do not. Taken together with structural data showing that the covalent ligands naturally exchange between different active and repressive binding poses (Hughes et al., 2012; Irwin et al., 2022), these findings indicate the malleability of the dynamic orthosteric pocket, the natural orthosteric binding mode of the non-covalent ligand, and the relative orthosteric affinity of the non-covalent ligand may determine whether the covalent ligand traps a non-covalent ligand in the entrance to and/or the β-sheet region of the orthosteric pocket.

## Discussion

Crystal structures of PPARγ bound to covalent and non-covalent synthetic ligands have shown overlapping ligand binding modes, indicating the covalent ligands should block binding of the non-covalent ligands. We and others have posited that cobinding of a non-covalent synthetic ligand to the PPARγ LBD prebound to a covalent ligand (GW9662 or T0070907) would reveal an alternate site binding mode, different from the crystallized binding modes. To our surprise, the non-covalent ligand can bind via its native orthosteric binding mode by pushing the covalent ligand aside, or slightly adapt its binding mode within the orthosteric pocket. Our structural analysis of non-covalent ligand cobinding with a covalent ligand reveals several important observations and conclusions.

Each of the non-covalent synthetic ligands utilizes unique mechanisms to cobind with the covalent ligands, as inferred from our crystal structures in which pre-formed crystals of the PPARγ LBD were soaked with non-covalent synthetic ligands BVT.13 cobinds to a region of the orthosteric pocket that only slightly overlaps with the orthosteric covalent ligand binding pose, adopting a cobinding pose that is similar to when soaked into apo-PPARγ LBD crystals. MRL24 and nTZDpa cobinding pushes the covalent orthosteric ligand into a different conformation, allowing these ligands to adopt their orthosteric binding modes in the cobound state. This finding was surprising for MRL24 in particular, as its orthosteric binding mode overlaps considerably with the orthosteric covalent ligand binding mode. In contrast, SR1664 cobinding occurs to the so-called alternate site, located at the entrance to the orthosteric pocket.

In our previous study, we observed synthetic and natural/endogenous ligand co-binding via co-crystallography where preformed crystals of PPARγ LBD bound to unsaturated fatty acids (UFAs) were soaked with a synthetic ligand, which pushed the bound UFA to an alternate site within the orthosteric ligand-binding pocket (Johnson et al., 2000). In the scenario of synthetic ligand cobinding with a covalent inhibitor, it is possible that soaking a covalent inhibitor into preformed crystals where the PPARγ LBD is already bound to a non-covalent ligand may prove to be difficult. The covalent inhibitor would need to flow through solvent channels within the crystal lattice, which may not be a problem. However, upon reaching the entrance surface to the orthosteric ligand-binding pocket, it may be difficult for the covalent inhibitor to gain access to the region of the orthosteric pocket required for covalent modification as the larger non-covalent ligand could block access. This potential order of addition problem may not be a problem for studies in solution or in cells, where the non-covalent ligand can more freely exchange in and out of the orthosteric pocket and over time the covalent reaction would reach full occupancy.

Our data provide support to structural model where in the absence of ligand, the PPARγ LBD exchanges between a transcriptionally repressive conformation where helix 12 is solvent occluded within the orthosteric pocket and a solvent exposed active conformation (Hughes et al., 2012). T0070907 binding slows the rate of exchange between these two conformations, stabilizing a long-lived active and repressive state (Irwin et al., 2022). GW9662-bound PPARγ LBD also samples active and repressive states, as observed by PRE NMR (Hughes et al., 2012), although the active conformation is more abundantly populated (McCoy et al., 2007). Agonist binding occurs via a two-step mechanism involving a fast encounter complex binding step at the entrance to the orthosteric pocket followed by a slow conformational change where the ligand translocates into the orthosteric pocket (Jang et al., 2017). Our NMR data here show that non-covalent ligand cobinding to T0070907-bound PPARγ LBD selects for an active conformation, as the repressive conformation NMR peak disappears. This indicates non-covalent ligand cobinding prevents the LBD from adopting a transcriptionally repressive helix 12 conformation within orthosteric pocket, explaining why non-covalent ligand cobinding of MRL24 and other PPARγ agonists with a covalent ligand activates PPARγ transcription (Hughes et al., 2016; Brust et al., 2017; MacTavish et al., 2024). Another way to test this structural model could be through the use of covalent PPARγ inverse agonist analogs with graded activity (Orsi et al., 2023), where one might posit that covalent inverse agonist analogs that shift the LBD conformational ensemble towards a fully repressive LBD conformation may better inhibit synthetic ligand cobinding.

Our findings may have profound implications as these GW9662 and T0070907 have been used in many published studies as covalent inhibitors to block ligand binding to PPARγ to test for binding and functional specificity in cells. As of May 2024, more than 1900 citations referring to ‘GW9662 or T0070907’ are reported in PubMed. Nearly 1000 of these publications were published in 2015 or later, after the original report that GW9662 and T0070907 are not effective inhibitors of ligand binding (Hughes et al., 2016), yet many in the field continue to use these compounds as covalent inhibitors. Our findings strongly suggest GW9662 and T0070907 should not be used as antagonists to block binding of other synthetic PPARγ ligands. On the other hand, GW9662 and T0070907 display unique pharmacological properties as a transcriptionally neutral antagonist and repressive inverse agonist, respectively Irwin et al., 2022, and thus it would be appropriate to use these compounds as pharmacological ligands. It may be possible to use the crystal structures we obtained to guide structure-informed design of covalent inhibitors that would physically block cobinding of a synthetic ligand. This could be the potential mechanism of a newer generation covalent antagonist inhibitor we developed, SR16832, that more completely inhibit alternate site ligand binding of an analog of MRL20, rosiglitazone and the UFA docosahexaenoic acid (DHA) MacTavish et al., 2024 and thus may be a better choice for the field to use as a covalent ligand inhibitor of PPARγ.

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
      <td>PPARG (Homo sapiens)</td>
      <td>PPARG</td>
      <td>UniPro</td>
      <td>P37231</td>
      <td>Protein sequence</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BL21(DE3)</td>
      <td>Sigma-Aldrich</td>
      <td>CMC0016</td>
      <td>Electrocompetent cells</td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>T0070907</td>
      <td>Cayman Chemical</td>
      <td>10026</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>GW9662</td>
      <td>Cayman Chemical</td>
      <td>70785</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>MRL-24</td>
      <td>MecChem Express</td>
      <td>HY-122235</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>nTZDpa</td>
      <td>Tocris Bioscience</td>
      <td>2150</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>SR1664</td>
      <td>Cayman Chemical</td>
      <td>11086</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound</td>
      <td>BVT-13</td>
      <td>Sigma Aldrich</td>
      <td>B4438</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PPARγ LBD</td>
      <td>Hughes et al., 2012</td>
      <td>Bacterial expression plasmid</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>LanthaScreen Elite Tb-anti-His antibody</td>
      <td>Thermo Fisher</td>
      <td>#PV5895</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>TRAP220/MED1</td>
      <td>LifeTein</td>
      <td>synthesized</td>
      <td>residues 638–656 (NTKNHPMLMNLLKDNPAQD) synthesized with or without a N-terminal FITC label with a six-carbon linker (Ahx) and an amidated C-terminus for stability</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>NCoR1</td>
      <td>LifeTein</td>
      <td>synthesized</td>
      <td>residues 2256–2,278 (DPASNLGLEDIIRKALMGSFDDK) synthesized with or without a N-terminal FITC label with a six-carbon linker (Ahx) and an amidated C-terminus for stability</td>
    </tr>
    <tr>
      <td>Software</td>
      <td>NMRFx</td>
      <td>Norris et al., 2016</td>
      <td>Version 11.4 .x</td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>Topspin</td>
      <td>Bruker</td>
      <td>Version 3 .x</td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>Prism</td>
      <td>GraShPad</td>
      <td>Version 10</td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>CCP4</td>
      <td>Agirre et al., 2023</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>Phaser</td>
      <td>McCoy et al., 2007</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>Phenix</td>
      <td>Adams et al., 2010</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>COOT</td>
      <td>Emsley and Cowtan, 2004</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>PyMOL</td>
      <td>Schrödinger</td>
      <td>Version 3</td>
      <td></td>
    </tr>
    <tr>
      <td>Software</td>
      <td>jFATCAT</td>
      <td>RCSB</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Materials and reagents

All compounds used in this study—GW9662, T0070907, BVT-13, nTZDpa, MRL24, and SR1664—were obtained from commercial sources including Cayman Chemicals, Tocris Bioscience, and Sigma-Aldrich with purity >95%. Peptides of LXXLL-containing motifs from TRAP220/MED1 (residues 638–656; NTKNHPMLMNLLKDNPAQD) and NCoR1 (2256–2278; DPASNLGLEDIIRKALMGSFDDK) with or without a N-terminal FITC label with a six-carbon linker (Ahx) and an amidated C-terminus for stability were synthesized by LifeTein.

### Protein expression and purification

Human PPARγ LBD (residues 203–477, isoform 1 numbering) was expressed in Escherichia coli BL21(DE3) cells using autoinduction ZY media or M9 minimal media supplemented with NMR isotopes (15NH4Cl) as a Tobacco Etch Virus (TEV)-cleavable N-terminal His-tagged fusion protein using a pET46 Ek/LIC vector (Novagen) and purified using Ni-NTA affinity chromatography and gel filtration chromatography. The purified proteins were concentrated to 10 mg/mL in a buffer consisting of 20 mM potassium phosphate (pH 7.4), 50 mM potassium chloride, 5 mM tris(2-carboxyethyl)phosphine (TCEP), and 0.5 mM ethylenediaminetetraacetic acid (EDTA). Purified protein was verified by SDS-PAGE as >95% pure. For studies using a covalent orthosteric antagonist, PPARγ LBD protein was incubated with at least a~1.05 x excess of GW9662 or T0070907 at 4 °C for 24 hr to ensure covalent modification to residue C285, then buffer exchanged the sample to remove excess covalent antagonist and DMSO. Complete attachment of the covalent antagonist occurs within 30–60 min, as detected using an LTQ XL linear Ion trap mass spectrometer with an electrospray ionization source (Thermo Fisher Scientific).

### Crystallization and structure determination

For T0070907- and GW9662-bound PPARγ LBD complexes, protein was incubated at a 1:3 protein/ligand molar ratio in PBS overnight. Proteins were buffer exchanged to remove DMSO and concentrated to 10 mg/mL. All crystals were obtained after 3–8 days at 22 °C by sitting-drop vapor diffusion against 50 μL of well solution using 96-well format crystallization plates. The crystallization drops contained 1 μL of protein complex sample mixed with apo crystal seeds prepared by PTFE seed bead (Hampton research) and 1 μL of reservoir solution containing 0.1 M MOPS (pH 7.6) and 0.8 M sodium citrate for T0070907 or GW9662-PPARγ LBD complexes; 0.1 M MES (pH 6.5), 0.2 M ammonium sulfate. The non-covalent ligands (BVT.13, MRL24, nTZDpa, SR1664) were soaked into T0070907 or GW9662-PPARγ LBD complex crystals by adding 1.5 μL of compound at a concentration of 2 mM suspended in reservoir solution containing 5% DMSO for 5 days. Data were processed, integrated, and scaled with the programs Mosflm and Scala in CCP4 (Adams et al., 2010). The structure was solved by molecular replacement using the program Phaser (Emsley and Cowtan, 2004) implemented in the PHENIX package Johnson, 2018 and used previously published PPARγ LBD structure (PDB code: 1PRG/6ONI; Hughes et al., 2012; Bae et al., 2016) as the search model. The structure was refined using PHENIX with several cycles of interactive model rebuilding in COOT (Williamson, 2013).

### NMR spectroscopy

2D [1H,15N]-TROSY HSQC NMR data of 200 µM 15N-labeled PPARγ LBD, pre-incubated with a 2 x molar excess of covalent ligand overnight at 4 °C, were acquired at 298 K on a Bruker 700 MHz NMR instrument equipped with a QCI cryoprobe in NMR buffer (50 mM potassium phosphate, 20 mM potassium chloride, 1 mM TCEP, pH 7.4, 10% D2O). Data were processed and analyzed using Topspin 3.0 (Bruker Biospin) and NMRViewJ (OneMoon Scientific, Inc; Johnson, 2018), respectively. NMR chemical shift assignments previously transferred from rosiglitazone-bound PPARγ LBD (Shang et al., 2019) to T0070907- and GW9662-bound states (Hughes et al., 2012; Irwin et al., 2022) were used in this study for well-resolved residues with conversed NMR peak positions to the previous ligand-bound forms using the minimum chemical shift perturbation procedure (Williamson, 2013).

### Time-resolved fluorescence resonance energy transfer (TR-FRET) assay

The time-resolved fluorescence resonance energy transfer (TR-FRET) assays were performed in black 384-well plates (Greiner) with 23 µL final well volume containing 4 nM His6-PPARγ LBD with or without covalently modification by GW9662 or T0070907, 1 nM LanthaScreen Elite Tb-anti-His Antibody (Thermo Fisher), and 400 TRAP220 or NCoR peptide in TR-FRET buffer (20 mM KPO4 pH 7.4, 50 mM KCl, 5 mM TCEP, 0.005% Tween 20). Compound stocks were prepared via serial dilution in DMSO, added to wells in triplicate, and plates were read using BioTek Synergy Neo multimode plate reader after incubating at 25 °C for 1 hr. The Tb donor was excited at 340 nm, its emission was measured at 495 nm, and the acceptor FITC emission was measured at 520 nm. Data were plotted using GraphPad Prism as TR-FRET ratio 520 nm/495 nm vs. ligand concentration and fit to sigmoidal dose-response equation — or biphasic or bell shaped dose response equations when appropriate, determined by comparison of fits to both equations and F test where the simpler model is selected if the p value is less than 0.05.

### Structural comparisons to published crystal structures

Structural overlays were compared to crystals structures of PPARγ LBD bound to GW9662 (PDB 3B0R), T0070907 (PDB 6C1I; Irwin et al., 2022), GW9662 and NCoR1 peptide (PDB 8FHE; Orsi et al., 2023), T0070907 and NCoR1 peptide (6ONI) Hughes et al., 2012, BVT.13 (PDB 2Q6S) Chrisman et al., 2018, MRL24 (PDB 2Q5P; Chrisman et al., 2018), nTZDpa (PDB 2Q5S; Chrisman et al., 2018), SR1664 and NCOA1 peptide (PDB 5DWL) Agirre et al., 2023, and SR1664 (PDB 4R2U; Lee et al., 2002). Pairwise structural alignment and rmsd calculations of the cobound structures to the transcriptionally active (PDB 6ONJ) PPARγ LBD conformation was performed via the RCSB webserver (https://www.rcsb.org/alignment/) using the jFATCAT rigid structural alignment algorithm.
