# Targeting oncogenic KRasG13C with nucleotide-based covalent inhibitors

## Authors

- Lisa Goebel<sup>1</sup> ([ORCID: 0000-0003-3477-1228](https://orcid.org/0000-0003-3477-1228))
- Tonia Kirschner<sup>1</sup>
- Sandra Koska<sup>1</sup>
- Amrita Rai<sup>2</sup> ([ORCID: 0000-0002-5471-5250](https://orcid.org/0000-0002-5471-5250))
- Petra Janning<sup>3</sup>
- Stefano Maffini<sup>4</sup> ([ORCID: 0000-0001-6380-6560](https://orcid.org/0000-0001-6380-6560))
- Helge Vatheuer<sup>1</sup>
- Paul Czodrowski<sup>1</sup>
- Roger S Goody<sup>2</sup> ([ORCID: 0000-0002-0772-0444](https://orcid.org/0000-0002-0772-0444)) †
- Matthias P Müller<sup>1</sup> ([ORCID: 0000-0002-1529-8933](https://orcid.org/0000-0002-1529-8933)) †
- Daniel Rauh<sup>1</sup> ([ORCID: 0000-0002-1970-7642](https://orcid.org/0000-0002-1970-7642)) †

### Affiliations

1. Department of Chemistry and Chemical Biology, TU Dortmund University Dortmund Germany ([ROR:01k97gp34](https://ror.org/01k97gp34))
2. Department of Structural Biochemistry, Max Planck Institute of Molecular Physiology Dortmund Germany ([ROR:03vpj4s62](https://ror.org/03vpj4s62))
3. Department of Chemical Biology, Max Planck Institute of Molecular Physiology Dortmund Germany ([ROR:03vpj4s62](https://ror.org/03vpj4s62))
4. Department of Mechanistic Cell Biology, Max Planck Institute of Molecular Physiology Dortmund Germany ([ROR:03vpj4s62](https://ror.org/03vpj4s62))

† Corresponding author

## Abstract

Mutations within Ras proteins represent major drivers in human cancer. In this study, we report the structure-based design, synthesis, as well as biochemical and cellular evaluation of nucleotide-based covalent inhibitors for KRasG13C, an important oncogenic mutant of Ras that has not been successfully addressed in the past. Mass spectrometry experiments and kinetic studies reveal promising molecular properties of these covalent inhibitors, and X-ray crystallographic analysis has yielded the first reported crystal structures of KRasG13C covalently locked with these GDP analogues. Importantly, KRasG13C covalently modified with these inhibitors can no longer undergo SOS-catalysed nucleotide exchange. As a final proof-of-concept, we show that in contrast to KRasG13C, the covalently locked protein is unable to induce oncogenic signalling in cells, further highlighting the possibility of using nucleotide-based inhibitors with covalent warheads in KRasG13C-driven cancer.

## Introduction

Ras proteins act as key regulators of many cellular processes by switching between inactive GDP-bound and active GTP-bound states, the latter specifically activating several downstream signalling pathways (Cox et al., 2014). Oncogenic Ras mutations that lead to dysregulation of the switch mechanism are found in about 25% of all human cancers, including three of the most lethal forms (lung, colon, and pancreatic cancer). Among the Ras proteins, KRas is the predominantly mutated isoform (85%), followed by NRas (11%) and HRas (4%), with mutational hotspots at amino acid positions G12, G13, and Q61 (Cox et al., 2014; Hobbs et al., 2016). Although the glycine at position 12 is the most commonly mutated residue, G13 is the second most common mutation (14% of tumors harbor a mutation at this position) and in 6% of these cases, an acquired cysteine is found (Forbes et al., 2015; Visscher et al., 2016). In lung cancer, the prevalence of the G13C mutation is 3%, which is equivalent to approximately 7000 individuals in the US per year (Forbes et al., 2015; Burge and Hobbs, 2022). Because of their prominent role in cancer, Ras oncogenes were identified as attractive targets for cancer therapy since their initial discovery in 1981, but attempts to target Ras have been largely unsuccessful and Ras proteins were long considered undruggable. After decades of failure, new interest has recently arisen from selective targeting of the G12C oncogenic mutant of KRas (Ostrem et al., 2013; Patricelli et al., 2016; Janes et al., 2018; Shin, 2019; Canon et al., 2019; Hong, 2020; Fell et al., 2018; Hallin et al., 2020; Fell, 2020). Inhibitors that bind irreversibly to the G12C mutated cysteine residue within a previously unknown switch-II pocket were originally identified and designed in the Shokat laboratory, and have been further developed within the academic and industrial world to advance candidates into the clinic (clinicaltrials.gov, 2018a; clinicaltrials.gov, 2019a; clinicaltrials.gov, 2018b; clinicaltrials.gov, 2019b; Goebel et al., 2020). In May 2021, the first-in-class KRasG12C inhibitor Sotorasib (Amgen) was approved by the FDA for the treatment of non-small-cell lung cancer (NSCLC), confirming the therapeutic susceptibility of mutant KRas in cancer (Mullard, 2021). A second approach for targeting mutant KRas has been described using nucleotide competitive inhibitors that can covalently bind to KRasG12C (Lim et al., 2014; Xiong et al., 2017). Strategies involving direct competition with nucleotide binding were originally set aside because of the high affinity of GDP/GTP for Ras and high cellular GDP/GTP concentrations. However, the combination of nucleotide competition with covalent binding of the inhibitors to the Ras protein has fuelled new hope. Gray and colleagues developed SML-8-73-1, a GDP derivative harbouring an electrophilic group on the β-phosphate to irreversibly bind to the mutant cysteine at position 12 within the P-loop of Ras (Lim et al., 2014). Unfortunately, the modification of the β-phosphate leads to a dramatic loss of affinity because of the loss of important interactions with the protein and the Mg2+ ion (Müller et al., 2017). In this publication, we demonstrate that GDP/GTP/GppCp analogues with an electrophilic group attached to the ribose interact with the necessary high reversible affinity to KRas and are able to react covalently with KRasG13C.

## Results and discussion

### Selective covalent modification of KRasG13C by 2’,3’-modified nucleotide analogues

Available structural information about the binding of GDP and GTP toward Ras provides a detailed understanding of the underlying high affinity of nucleotides through multiple reversible interactions. Based on published crystal structures of Ras proteins (Figure 1) and a multiple sequence alignment of the Ras small GTPase superfamily (Figure 1—figure supplement 1, Supplementary file 1), we designed and synthesized guanine nucleotide-based inhibitors with an additional Michael acceptor as a covalent warhead for targeting oncogenic KRas variants harboring cysteines in the P-loop (KRasG12C and KRasG13C). Whereas the G12C mutation has been successfully addressed in the past, KRasG13C is a largely unexplored target in cancer therapy. However, based on pKa calculations, we were able to show that the G13C mutation should also be generally addressable by appropriately positioned Michael acceptors (Supplementary file 2). In contrast to Gray and colleagues, we chose the 2’,3’-OH groups of the ribose for attachment of the warhead since modifications at this position do not significantly alter nucleotide affinity (Figure 1A, B; Eberth et al., 2005). Nucleotide derivatives with different linkers (eda: ethylenediamine, pda: propylenediamine, bda: butylenediamine) were synthesised based on published procedures (Method section), including GDP/GTP/GppCp analogues (R=OH), resulting in the formation of mixed 2’ and 3’-isomers, as well as dGTP analogues (R=H) (Eberth et al., 2005; Cremo et al., 1990). In addition to acrylamide-bearing nucleotides that could potentially bind irreversibly to cysteine containing P-loop mutants via Michael addition, we prepared acetamide derivatives as non-reactive control analogues (Figure 1B). The cysteine light-version of KRas constructs lacking other cysteines (C51S, C80L, C118S) were used for initial MS experiments, which indicated that the acrylamide nucleotide derivatives can selectively react with KRasG13C1-169 (Cys-light), but not with KRasG12C1-169 (Cys-light) (Figure 1C, D, E). The eda linker led to the most efficient covalent protein modification (Figure 1C). This tendency is presumably because of a favourable orientation of the reactive warhead and/or a reduced flexibility. Using dGTP analogues, the rate of covalent protein modification was further increased in the case of the eda derivative, indicating that the linker in the 3’-position of the ribose is superior to the 2’-position with respect to targeting KRasG13C. Although, complete modification of KRasG13C was only observed at elevated pH, significant modification of the protein also occurred at a physiological pH within 24 hr. On incubating KRasG13C1-169 (Cys-light) with the GTP analogues, we observed at intermediate stages a mixture of covalently bound GDP and GTP forms of KRasG13C1-169 (Cys-light), but ultimately the reaction yielded only the diphosphate form, indicating that the nucleotides were still hydrolysed after the covalent reaction and were properly positioned in the active site of KRas (Figure 1—figure supplement 2). The time-resolved labelling of KRasG13C1-169 (Cys-light) with either GDP or GTP derivatives led to comparable covalent protein modification rates (Figure 1—figure supplement 3). Additionally, we tested whether the nucleotides were generally able to compete with their natural counterparts and monitored the reaction also in the presence of equimolar concentrations as well as 10 x and 100 x excess of GDP/GTP (Figure 1—figure supplement 4). This shows that although the reaction is slowed down due to the competing nature of GDP and GTP, the modified nucleotides are able to compete. Upon incubating KRasG13C1-169 (Cys-light) with a non-cleavable GppCp derivative, we also observed covalent modification, but without subsequent hydrolysis of the nucleotide (Figure 1—figure supplement 5). To further investigate the specificity of the reaction towards KRasG13C1-169 (Cys-light), we also tested the wild type protein. For KRasWT1-169, very little unspecific labelling was observed at pH 9.5 compared to the G13C mutant (approximately 3% at pH 9, 8% at pH 9.5, whereas under equivalent conditions, KRasG13C modification was ≥90%; Figure 1E, Figure 1—figure supplement 6), thus showing that the warhead reacts preferentially with the cysteine at position 13, but not other cysteines in KRas nor the additional neighboring cysteine in KRasG12C. In addition, the multiple sequence alignment of the Ras small GTPase superfamily revealed that only about 7% of the GTPase members contain cysteines within the P-loop that might potentially be accessible by our linker design and only 3 contain Cys at the position equivalent to residue 13 in Ras (Arl4a, RheBL1, Rab21). Upon incubating Rab21 with edaGDP, we indeed observed similar modification compared to KRasG13C (Figure 1—figure supplement 7). However, since cross-reactivities of covalently binding molecules is well-known and documented also for example in kinase inhibitors such as osimertinib, which modifies a number of off-target kinases (Finlay et al., 2014), we are confident that this will not generally preclude the usage of the nucleotides described. In fact, Rab21 might be an interesting target itself since knock-down of Rab21 has been reported to have beneficial effects in human glioma cells (Ge et al., 2017).

![Figure 1.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig1-v2.jpg)

**Figure 1.:** (A) Structure of KRasWT in the GDP-bound state (grey, P-loop: violet, switch I: red, switch II: blue, NKxD: green, SAK: yellow; PDB 4obe). (B) Model of KRasG13C (model is based on PDB 4obe) showing the distances between the cysteine residue and the OH-groups of the ribose and the general structure of nucleotide derivatives bearing an electrophilic group at the 2’,3’-position of the ribose moiety, showing that position 12 is further remote compared to position 13 and thus explaining the observed specificity of covalent bond formation. (C) Time-dependent analysis of the covalent modification of KRasG13C1-169 (Cys-light) at pH 9.5 using different linker lengths (eda: ethylenediamine, pda: propylenediamine and bda: butylenediamine). (D) Covalent modification of KRasG13C1-169 (Cys-light) proteins at pH 9.5 after 24 hr at room temperature. (E) In contrast, KRasG12C1-169 (Cys-light) mutant was not modified by nucleotide derivatives and for KRasWT1-169 very little unspecific labelling at pH 9.5 was observed compared to the G13C mutant.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Based on the crystal structure of KRasWT (PDB 4obe), aa residues that are potentially accessible via the linker design (eda:~10 Å, bda:~12 Å) are marked (grey, P-loop: violet, switch I: red, NKxD: green, SAK: yellow) and used for multiple sequence alignment of the Ras small GTPase superfamily (Figure 1—figure supplement 1, Supplementary file 1).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Time-resolved labelling of Ras proteins with acryl-edaGTP showing that the GTP derivative binds in the active site of Ras where it is subsequently hydrolysed. (B) Schematic representation of the GDP/GTP hydrolysis. (C) Time-dependent analysis of the covalent modification of KRasG13C proteins with edaGTP at pH 9.5 at room temperature.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** Time-resolved labelling of Ras proteins with acryl-edaGDP (black) or acryl-edaGTP (grey).

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** Labelling of KRasG13C1-169 (Cys-light) with acryl-edaGDP at pH 9.5 and room temperature was monitored after different time points by ESI-MS in the presence of equimolar concentrations and 10 x and 100 x excess of GDP/GTP.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** Labelling of KRasG13C1-169 (Cys-light) with acryl-edaGppCp at pH 9.5 and room temperature was controlled after 24 hr by ESI-MS.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** (A, B, C) pH-dependent labelling of Ras proteins with acryl-edaGDP (black), acryl-pdaGDP (red) and acryl-bdaGDP (blue) after 24 hr. To increase the amount of covalently modified protein, the pH value was gradually increased. For KRasG13C1-169 (Cys-light), a slight labelling could already be observed at pH 7.5, which, however, could be increased to almost 100% by increasing the pH to 9.5. For KRasWT1-169 very little unspecific labelling was observed compared to the G13C mutant.

![Figure 1—figure supplement 7.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig1-figsupp7-v2.jpg)

In summary, since other cysteines that are located within the P-loop or other regions close to the nucleotide are mostly further remote compared to Cys13 and even the directly neighboring residue at position 12 does not become modified as shown above, suitable design and optimization of the linker will likely allow sufficient specificity towards KRasG13C also in vivo (Figure 1—figure supplement 1, Supplementary file 1).

### Reversible affinities of the nucleotide analogues are comparable to those of the unmodified nucleotides

To evaluate the impact of the attached linker on nucleotide binding, we first determined the affinity and kinetics of the interaction of the nucleotide derivatives with Ras compared to unmodified GDP/GTP that have dissociation constants (KD) in the picomolar range (Table 1). For this purpose, we measured the kinetics of the nucleotide association (kon) in a stopped-flow instrument using competition experiments between mantdGDP (2 μM) and increasing amounts of competing nucleotides (1, 2, and 6 μM; Müller et al., 2017). As shown in Table 1—source data 1, the competitive binding of the competing nucleotide and mantdGDP led to a significant decrease in the fluorescence signal because of smaller amounts of mantdGDP binding to KRas. By fitting the data to a previously described model (Müller et al., 2017), we obtained the corresponding kon values, and those for the nucleotide analogues were comparable to those of the unmodified nucleotide (Table 1—source data 2). To further analyse the ability of the modified nucleotides to compete with GDP/GTP, KRasWT:GDP was mixed with equal amounts of the acetamide derivatives and incubated either for 7 days at room temperature in the absence of EDTA, for 24 hr at 4 °C in the presence of EDTA, or for 1 hr at room temperature in the presence of SOS (guanine nucleotide exchange factor) to increase the rate of nucleotide exchange and to allow the reaction to equilibrate. After this equilibration time and buffer exchange, the Ras proteins were concentrated and the nucleotide state was analysed by isocratic HPLC runs. By integrating the corresponding peaks for GDP and the guanosine nucleotide analogues after distinct time points, we observed that the modified nucleotides can indeed compete with GDP (Table 1—source data 3, Table 1—source data 4). Based on the relative abundance of bound nucleotides determined by the HPLC assay, the dissociation constants for the pda and bda derivatives were calculated to be 8.6±1.3 pM and 9.6±0.5 pM, respectively (overlap with the GDP elution peak prevented accurate determination in the case of the eda-derivative; Method section, Table 1). Thus, the attached linker has very little impact on the reversible interaction and the affinity, an important fact that must be considered for the approach of using nucleotide-competitive inhibitors (Müller et al., 2017). In contrast, SML-8-73-1, a GDP derivative harbouring an electrophilic group on the β-phosphate showed a dramatic loss of reversible affinity (KD = ~140 nM) (Jeganathan et al., 2018).

**Table 1.**
 Overview of the calculated kinetic parameters (KD, kon and koff).Table 1—source data 1.Kinetics of the nucleotide association (kon).(A) Competitive binding experiments of GDP and mantdGDP; 1 μM KRas and 2 μM mantdGDP was used in the absence (black curve) or in the presence of 1 µM (red), 2 µM (blue) or 6 µM (green) competing nucleotides in a stopped-flow instrument. (B) The binding curves were globally fit to the indicated model using KinTek Explorer to obtain the corresponding association rates (kon). (C, D, E) Competitive binding experiments between mantdGDP and GDP, GTP, or dGTP analogues. Calculated kon values are shown in Table 1—source data 2.Table 1—source data 2.kon calculation.Overview of kon rate constants obtained from competitive binding experiments with mantdGDP (Table 1—source data 1).Table 1—source data 3.HPLC-based approach for determination of affinities relative to GDP.(A, B, C) Competitive binding experiments of GDP and the acetyl-derivatives of GDP; 50 μM KRasWT:GDP was mixed with 50 µM of edaGDP, pdaGDP or bdaGDP and incubated for 7 days at room temperature in the absence of EDTA, for 24 hr at 4 °C in the presence of 10 mM EDTA or for 1 hr in the presence of SOS (0.5 µM). After buffer exchange for removal of any unbound nucleotides, the resulting mixtures were analyzed by isocratic HPLC runs. (D) Relative amounts of the nucleotides and GDP bound to KRas were compared. It should be noted that the relative affinities mentioned in the method section and shown in Table 1—source data 4 are calculated from these experiments and represent an average affinity of the 2’ isomers, and that of the 3’-isomer seen to be bound in the X-ray structure is presumably actually higher than this, since it can be seen from Figure 2—figure supplement 1 that there is a preference for one of the isomers, presumably the 3’-isomer, so that this species and the derivatives of dGDP/dGTP must have a very similar affinity to that of GDP/GTP.Table 1—source data 4.KD calculations.Overview of the calculated KD values of pdaGDP and edaGDP obtained from an HPLC-based approach (Table 1—source data 3); For reference, the KD values of GDP and the nucleotide analogue SML-8-73-1 are also listed.


<table>
  <thead>
    <tr>
      <th></th>
      <th>KD[pM]</th>
      <th>kon[µM–1s–1]</th>
      <th>koff[s–1]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GDP</td>
      <td>2.5</td>
      <td>4.22</td>
      <td>1.1x10–5</td>
    </tr>
    <tr>
      <td>pdaGDP</td>
      <td>8.6±1.3</td>
      <td>3.34</td>
      <td>2.9x10–5</td>
    </tr>
    <tr>
      <td>bdaGDP</td>
      <td>9.6±0.5</td>
      <td>3.12</td>
      <td>3.0x10–5</td>
    </tr>
    <tr>
      <td>SML-8-73-1</td>
      <td>~140 nM</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

### First crystal structures of the KRasG13C mutant

To gain further insight into the binding mode of the covalently bound nucleotides, we solved the first X-ray crystal structure of the oncogenic KRasG13C mutant, in this case with covalently bound edaGDP (PDB 7ok3) and bdaGDP (PDB 7ok4) (Figure 2, Figure 2—figure supplement 1). The overall structures are very similar to the known structure of KRas:GDP (PDB 4obe), and the nucleotide scaffold, as well as the covalent linkage for both nucleotide analogues with cysteine at position 13 are well resolved in the electron density (Figure 2C, E, Figure 2—figure supplement 1). Interestingly, only the 3’-isomer of the nucleotide analogues was observed in the structures, consistent with results of the MS experiments comparing the efficiency of labelling of the dGTP derivative and the mixed isomers of the GTP derivative and showing a faster reaction for dGTP (Figure 1C). Both structures showed that the nucleotides are bound within the active site in a manner that is comparable to non-covalently bound GDP in other structures of Ras, with similar reversible interactions between the protein and the nucleotide and the additional well-resolved covalent link to Cys13. However, both structures lacked the Mg2+ ions in the active site despite a Mg2+ concentration of 2 mM in the Ras solution. The missing Mg2+-ions are probably a result of the crystallization buffer containing NH4F or NaF, leading to precipitation of poorly soluble MgF2, and this has also been observed in other PDB-deposited structures presumably because of similar effects of the reservoir solutions used in the crystallization process (e.g. PDB 4m1o, 4lyf, 4lyh, 4m21, 4m1s, 4m1t, 4m1t, 4m1y) (Ostrem et al., 2013). In both crystal structures, the eda and bda linker are remote from the Mg2+ binding site and do not directly interfere with Mg2+ binding, suggesting that Mg2+ can generally bind. Thus, the structural analysis verified the nucleotide binding pose and the high reversible affinity comparable to the natural nucleotides and will guide design and optimisation of the linker and the warhead in further studies.

![Figure 2.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig2-v2.jpg)

**Figure 2.:** (A) Comparison of KRasG13C covalently locked with edaGDP (grey, P-loop: violet, switch I: red, switch II: blue, NKxD: green, SAK: yellow, PDB 7ok3) and KRas:GDP (white, PDB 4obe). (B) Comparison of KRasG13C covalently locked with bdaGDP (grey, P-loop: violet, switch I: red, switch II: blue, NKxD: green, SAK: yellow, PDB 7ok4) and KRas:GDP (white, PDB 4obe). (C) Enlarged view of the nucleotide binding pocket in KRasG13C-edaGDP showing the 2Fo-Fc electron density map (countered at 1.0 σ). (D) Structural superposition of KRas:GDP and the covalently locked G13C mutants. (E) Enlarged view of the nucleotide binding pocket in KRasG13C-bdaGDP showing the 2Fo-Fc electron density map (countered at 1.0 σ).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A, B) edaGDP and bdaGDP, respectively, covalently bound to KRasG13C including the FO-FC simulated annealing omit map (green, r.m.s.d.=2.5) and the 2FO-FC map (grey, r.m.s.d.=1.0).

### Inhibition of oncogenic KRasG13C signalling by covalent nucleotide analogues

Finally, we set out to test whether the GDP nucleotide derivatives we are focusing on for cancer therapy were indeed able to inhibit oncogenic signalling by KRasG13C. In a first experiment, we tested and compared the SOS-catalysed nucleotide exchange on Ras. Whereas SOS efficiently catalysed nucleotide exchange on KRasWT, KRasG13C and as a control on KRasG13C:acetyledaGDP, it was unable to do so with the covalently locked G13C-edaGDP mutant, showing that the protein is indeed locked in the inactive state (Figure 3A, Figure 3—figure supplement 1). Interestingly, in these experiments we also observed a drastically increased intrinsic nucleotide exchange rate for KRasG13C compared to KRasWT in the absence of SOS (Figure 3A, blue area), an effect that probably contributes to the increased signalling and oncogenic effect of this mutant, and also this effect is abrogated in the case of covalently locked KRasG13C-edaGDP (Hunter et al., 2015). Similarly, no SOS-catalysed nucleotide exchange was observed in case of covalently modified KRasG13C-edaGppCp, indicating that the protein can also be trapped in the active conformation with the corresponding nucleoside-triphosphates (Figure 3—figure supplement 1B). Thus, the modified GppCp derivatives could also be used as artificial and irreversible activators and generally as tool compounds to further investigate the biological role of KRasG13C in cells. In addition to SOS-catalysed nucleotide exchange, GAP-stimulated GTP hydrolysis was also analysed. While the intrinsic GTP hydrolysis of KRasG13C-edaGTP (t1/2 = 187 min) is comparable to that of KRasWT:GTP (t1/2 = 126 min) and even faster than for the KRasG12C mutant (t1/2 = 300 min) (Li et al., 2021; Figure 3—figure supplement 2), a drastically decreased GAP-stimulated GTP hydrolysis was observed for the G13C mutant as expected (Scheffzek et al., 1997).

![Figure 3.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig3-v2.jpg)

**Figure 3.:** (A) GEF-catalysed nucleotide exchange of KRasWT:GDP, KRasG13C:GDP and KRasG13C-edaGDP (step 1) which were mixed with an excess of mantdGDP (step 2) and subsequently with 0.25 µM (red curve) or 0.5 µM (black curve) of SOS (step 3). The intrinsic nucleotide exchange is depicted in the blue box whereas the SOS-catalysed nucleotide exchange is shown in the grey box. (B) Western blot analysis after electroporation of indicated amounts of full-length KRasWT, KRasG13C, and KRasG13C-edaGDP into HeLa cells. (C) Quantification of protein levels from western blots was performed using Empiria Studio (Li-Cor). The mean fold change was plotted against increasing amounts of protein. Error bars indicate the standard deviation for each measurement (n=3). One-way ANOVA was performed using GraphPad Prism. The uncropped western blots are available as source data (Goebel et al_Source_data_file_WB.xlsx).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** SOS-catalysed nucleotide exchange of (A) KRasG13C:acetyledaGDP and (B) KRasG13C-edaGppCp which were mixed with an excess of mantdGDP and subsequently with 0.25 µM (red curve) or 0.5 µM (black curve) of SOS. The intrinsic nucleotide exchange is depicted in the blue box whereas the SOS-catalysed nucleotide exchange is shown in the grey box.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) The intrinsic (black) and the GAP-stimulated (red) GTP hydrolysis of KRasWT:GTP was measured via HPLC. (B) The intrinsic (black) and the GAP-stimulated (red) GTP hydrolysis of KRasG13C-edaGTP was obtained via ESI-MS. While GAP-stimulated GTP hydrolysis can be observed for KRasWT:GTP already at catalytic amounts of GAP (GAP 1:1000, t1/2 = 16 min), KRasG13C-edaGTP requires equivalent amounts of GAP (GAP 1:1, t1/2 = 35 min). However, the intrinsic GTP hydrolysis of KRasG13C-edaGTP (t1/2 = 187 min) is comparable to that of KRasWT:GTP (t1/2 = 126 min).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Whereas RasG13C:GDP can be pulled down by GST-tagged RafRBD in the presence of GppNHp and GppNHp/SOS, RasG13C-edaGDP cannot become activated and consequently cannot bind to RafRBD, neither in the presence of GppNHp nor GppNHp and SOS.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** (A) Schematic representation of covalent modification of full-length KRasG13C followed by in vitro farnesylation. Nucleotide exchange was performed in the presence of EDTA at pH 7.5 followed by covalent modification of full-length KRasG13C at pH 9.5 to prevent undesired interaction with the cysteine of the CAAX box. To verify the position of the covalent modification, an in vitro farnesylation was afterwards performed, showing complete farnesylation and thus showing that the cysteine of the important CAAX box at the C-terminus of Ras is available for farnesylation and did not react unspecifically with the nucleotide. (B) Schematic representation of in vitro farnesylation of full-length KRasWT as a control experiment.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** (A) Overview of the sequence coverage. The identified regions of the protein are marked in green, and only the C-terminus of the protein cannot be identified due to the multiple lysine side chains present in this region. (B) Comparison of the intensities of all peptides of KRas after tryptic digestion, which were detected in all four replicates of the unmodified protein with an intensity of at least 1E8. Peptide intensities of the unmodified protein and the modified one are comparable from position 16 on, whereas the intensities of the peptides containing the targeted cysteine residue were significantly lower. By calculating the mean values of the intensities for the replicates of the unmodified (s1) and modified proteins (s2) followed by calculating the ratio of the mean values (MW s1/MW s2), we observed that the N terminus up to position 16 in the samples s2 could not be identified or was detected with much lower intensity than the other detectable regions of KRas. Thus, MS/MS analysis suggests that the targeted cysteine residue at position 13 is labelled by the nucleotide-based inhibitor edaGDP. (C, D) Comparison of the intensities of peptide LVVVGAGCVGK (m/z: 529.805+–5 ppm, twofold charged) for KRasG13C and KRasG13C-edaGDP. (D) Ion chromatogram of the peptide for KRasG13C. (D) Ion chromatogram of the peptide for KRasG13C-edaGDP.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig3-figsupp6-v2.jpg)

**Figure 3—figure supplement 6.:** Western blot analysis after electroporation of indicated amounts of full-length (A) KRasWT, (B) KRasG13C and (C) KRasG13C-edaGDP into HeLa cells (n=3 biological replicates). The uncropped western blots are available as source data (Goebel et al_Source_data_file_WB.xlsx).

![Figure 3—figure supplement 7.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig3-figsupp7-v2.jpg)

**Figure 3—figure supplement 7.:** Quantification of (A) KRas and (B) downstream protein levels from western blots after electroporation of indicated amounts of full-length KRasWT, KRasG13C and KRasG13C-edaGDP into HeLa cells using Empiria Studio (Li-Cor). The mean fold change was plotted against increasing amounts of protein. Error bars indicate the standard deviation for each measurement (n=3). Because of the relatively low expression levels of Ras, the contrast needed to be appropriately increased to enable visualisation of the intrinsically expressed KRas protein. The uncropped western blots are available as source data (Goebel et al_Source_data_file_WB.xlsx).

![Figure 3—figure supplement 8.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig3-figsupp8-v2.jpg)

**Figure 3—figure supplement 8.:** (A) Western blot analysis after electroporation of indicated amounts of full-length KRasG13C:acetyledaGDP into HeLa cells (n=3 biological replicates). (B) Quantification of KRas and (C) downstream protein levels from western blots after electroporation of indicated amounts of full-length KRasG13C:acetyledaGDP (blue) into HeLa cells using Empiria Studio (Li-Cor). The mean fold change was plotted against increasing amounts of protein. Error bars indicate the standard deviation for each measurement (n=3). The uncropped western blots are available as source data (Goebel et al_Source_data_file_WB.xlsx).

![Figure 3—figure supplement 9.](https://cdn.elifesciences.org/articles/82184/elife-82184-fig3-figsupp9-v2.jpg)

**Figure 3—figure supplement 9.:** (A) Western blot analysis after electroporation of indicated amounts of full-length KRasG13C-edaGppCp into HeLa cells (n=2 biological replicates). (B) Quantification of KRas and (C) downstream protein levels from western blots after electroporation of indicated amounts of full-length KRasG13C-edaGppCp (green) into HeLa cells using Empiria Studio (Li-Cor). The mean fold change was plotted against increasing amounts of protein. Error bars indicate the standard deviation for each measurement (n=2). The uncropped western blots are available as source data (Goebel et al_Source_data_file_WB.xlsx).

In addition to the effects of GEFs and GAPs, we also investigated whether the covalent modification with edaGDP was sufficient to preclude effector binding. For this, we performed pull-down experiments with GST-tagged RafRBD: Whereas KRasG13C:GDP did not bind to the RafRBD, it was activated in the presence of GppNHp alone or in combination with SOS and was pulled down by RafRBD. This finding again highlights the self-activating nature of this Ras mutant, even in the absence of a stimulus (SOS). In contrast, covalently locked KRasG13C-edaGDP was neither in the presence of GppNHp nor of additional SOS able to bind to the RafRBD (Figure 3—figure supplement 3).

Finally, after the detailed in vitro characterization of the nucleotide analogues, the next experiment was to investigate whether oncogenic signalling could also be inhibited in vivo. Since the nucleotides are unable to cross the cell membrane without loss of the phosphate groups and full labelling of the G13C mutant was only achieved at relatively high pH values within 24 hr, we used electroporation to deliver recombinant full-length KRasWT, KRasG13C and KRasG13C-edaGDP into human cells. Importantly, we confirmed that the covalently locked protein can still be fully farnesylated in vitro (Figure 3—figure supplement 4) and the covalent modification of full-length KRasG13C was further validated through MS/MS‐analysis, which revealed selective labelling of the targeted cysteine residue at position 13 (Figure 3—figure supplement 5). Upon electroporation into HeLa cells, a concentration-dependent increase in abundance of KRas was observed for all variants, indicating successful delivery into cells (Figure 3B, C, Figure 3—figure supplements 6 and 7). However, whereas we observed a concentration-dependent activation of the downstream signalling and upregulation of pcRaf, pAkt, pErk, and pS6 upon delivery of KRasG13C, the covalently locked variant was unable to induce these effects and, similarly to KRasWT, no increase in downstream signalling was observed (Figure 3B, C, Figure 3—figure supplements 6 and 7). In addition, upon electroporation of non-covalently modified KRasG13C:acetyledaGDP or covalently modified KRasG13C-edaGppCP, activation of the Ras pathway comparable to KRasG13C was observed, showing that covalent modification is essential for inhibition of oncogenic signalling and that artificial activation can be induced using non-hydrolysable GTP derivatives, which potentially adds further possibilities of using these nucleotide analogues to study Ras biology (Figure 3—figure supplements 8 and 9). Thus, our cellular data provide an additional proof-of-concept for the use of nucleotide-based covalent inhibitors and activators in KRasG13C-driven cancer.

### Conclusion

In summary, we have successfully developed nucleotide-based covalent inhibitors of oncogenic KRasG13C, a variant of KRas that is largely unexplored as a target even though it is a frequently observed mutation in cancer (Visscher et al., 2016). Thorough biochemical and structural characterization revealed that the nucleotide analogues designed and synthesized in this publication have similar affinities towards Ras compared to their natural counterparts. Since we are currently unable to directly test the nucleotides in cells, we instead extensively tested them in vitro regarding their ability to covalently lock KRasG13C in the inactive state and to effectively inhibit oncogenic signaling. We could show that the nucleotides prohibit (SOS-mediated) nucleotide exchange and lead to an effective interference in the induction of oncogenic effects by KRasG13C in living cells. Thus, after the first successful examples of inhibition of KRasG12C by Shokat and colleagues, our study breaks ground to effectively inhibit another important oncogenic variant of Ras by using small molecules.

Further optimization of the nucleotides to overcome the limitations regarding reactivity at physiological pH, as well as cell-permeability, are necessary and currently ongoing. In this respect, we are focusing on various linker designs based on the determined structure of the adduct, including cyclic linkers, to fine-tune the warhead’s orientation and reactivity towards the cysteine at position 13. Additionally, protective esterification of the diphosphate moiety is currently being investigated to deliver prodrugs of the nucleotides into cells, which subsequently become activated by unspecific esterases (Meier, 2017; Mehellou et al., 2018). We are also investigating whether appropriate modification of the linker length and the electrophilic warhead would also make KRasG12C or other relevant mutants (e.g. HRasG12S in Costello syndrome) (Gripp and Lin, 2012) a possible target in a similar approach.

## Methods

### Sequence alignment

A multiple sequence alignment of the G domain Ras superfamily members was performed using (UniProt Consortium, 2021). The uniport accession codes that were used for the sequence alignment of the GTPases can be taken from Supplementary file 1.

### pKa calculations

For the protein pKa prediction, a program from OpenEye based on the Zap finite difference Poisson–Boltzmann solver was used. Regarding partial charges of the protein, Delphi radii and CHARMM36 All-Hydrogen partial charges were utilized. The linker was removed in the bda/edaGDP structures. The am1bccsym method was used to assign appropriate partial charges to the ligands. An inner dielectric of 10, an ionic strength of 0.05 M and ionization (i.e. pH) of 7.5 was applied. For cysteine, a reference pKa of 8.6 was used. All hydrogen atoms were modeled explicitly, and except for the orientations of the OH and SH protons, which were sampled in 10° steps, the rest of the structure was static. Optimizing ionization state and SH orientation was achieved by applying ten million Monte Carlo steps (Supplementary file 2; Word and Nicholls, 2011).

### Synthesis of nucleotide-based covalent inhibitors

Synthesis of the nucleotide analogues was carried out according to the protocol established by Cremo et al. and described by Eberth et al., 2005; Cremo et al., 1990. A strong cation exchanger (Ion exchanger I, Merck, Darmstadt, Germany) was used to prepare the tributylammonium salts of the nucleotides. The commercially available sodium salt of the nucleotide (0.5 mmol) was dissolved in 3 mL ddH2O and was applied on the column pre-equilibrated with pyridine/H2O (1:1). Nucleotide elution was achieved using methanol/H2O (1:1) and the eluate was dripped into 1 mL TBA. After monitoring the nucleotide elution by spotting samples onto a TLC plate with fluorescent indicator and removing of the methanol/H2O solution the mixture was dried by repeated rotary evaporation from dry DMF (3x20 mL).

### Preparation of 5´-phosphorylimidazolidate 2’,3’-O-carbonate of nucleotides

The remaining solid was dissolved in 20 mL dry DMF and CDI (2.5 mmol) was added under argon atmosphere. After stirring overnight at 4 °C to form the carbonate the reaction was quenched by the addition of absolute methanol (150 µL; Scheme 1).

![Scheme 1.](https://cdn.elifesciences.org/articles/82184/elife-82184-scheme1-v2.jpg)

#### HRMS (ESI-MS)

<table>
  <thead>
    <tr>
      <th>nucleotide</th>
      <th>calculated</th>
      <th>[M-H]-</th>
      <th>found</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GDP</td>
      <td>518.0232</td>
      <td>C14H14O11N7P2</td>
      <td>518.0220</td>
    </tr>
    <tr>
      <td>GTP</td>
      <td>597.9895</td>
      <td>C14H15O14N7P3</td>
      <td>597.9869</td>
    </tr>
    <tr>
      <td>dGTP</td>
      <td>650.0315</td>
      <td>C17H19O13N9P3</td>
      <td>650.0304</td>
    </tr>
    <tr>
      <td>GppCp*</td>
      <td>545.9828</td>
      <td>C12H15O14N5P3</td>
      <td>545.9829</td>
    </tr>
    <tr>
      <td colspan="4">‍*in case of GppCp, the cyclic carbonate was observed with a free terminal phosphate group.</td>
    </tr>
  </tbody>
</table>

### Preparation of the respective 2’,3’-O-carbamates of nucleotides

The primary amine (eda, pda or bda; 2.5 mmol) dissolved in 5 mL dry DMF was slowly added to the carbonate mixture to prepare the phosphoramidate derivative. The resulting precipitate was recovered by centrifugation (10,000 rpm, 10 min) and washed three times with DMF (Scheme 2).

![Scheme 2.](https://cdn.elifesciences.org/articles/82184/elife-82184-scheme2-v2.jpg)

#### LCMS (ESI-MS)

<table>
  <thead>
    <tr>
      <th>nucleotide</th>
      <th>linker</th>
      <th>calculated</th>
      <th>[M-H]-</th>
      <th>found</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">GDP</td>
      <td>eda</td>
      <td>578.1</td>
      <td>C16H22N9O11P2</td>
      <td>578.1</td>
    </tr>
    <tr>
      <td>pda</td>
      <td>592.1</td>
      <td>C17H24N9O11P2</td>
      <td>592.1</td>
    </tr>
    <tr>
      <td>bda</td>
      <td>606.1</td>
      <td>C18H26N9O11P2</td>
      <td>606.1</td>
    </tr>
    <tr>
      <td rowspan="3">GTP</td>
      <td>eda</td>
      <td>658.1</td>
      <td>C16H23N9O14P3</td>
      <td>658.0</td>
    </tr>
    <tr>
      <td>pda</td>
      <td>672.1</td>
      <td>C17H25N9O14P3</td>
      <td>672.1</td>
    </tr>
    <tr>
      <td>bda</td>
      <td>686.1</td>
      <td>C18H27N9O14P3</td>
      <td>686.1</td>
    </tr>
    <tr>
      <td rowspan="3">dGTP</td>
      <td>eda</td>
      <td>634.1</td>
      <td>C15H27N9O13P3</td>
      <td>634.1</td>
    </tr>
    <tr>
      <td>pda</td>
      <td>662.1</td>
      <td>C17H31N9O13P3</td>
      <td>662.1</td>
    </tr>
    <tr>
      <td>bda</td>
      <td>690.2</td>
      <td>C19H35N9O13P3</td>
      <td>690.2</td>
    </tr>
    <tr>
      <td>GppCp</td>
      <td>eda</td>
      <td>648.1</td>
      <td>C16H29N9O13P3</td>
      <td>648.1</td>
    </tr>
  </tbody>
</table>

### Cleavage of the phosphoramidate

The solid was dissolved in 20 mL ddH2O and the pH was adjusted to 1.5 with 0.25 M hydrochloric acid to hydrolyse the phosphoramidate. After stirring at 4 °C for 1–3 d the mixture was then raised to pH 7.5 using 0.25 M NaOH. The nucleotides were purified at 4 °C on a Q-Sepharose column (column volume: 130 mL) preequilibrated with 50 mM triethylammonium bicarbonate buffer (pH 7.6) and eluted by a linear gradient of 50 mM – 1 M TEAB over 600 min with a flow rate of 1 mL/min. The nucleotide containing fractions were analysed by HPLC 50 mM KPi pH 6.6, 10 mM TBAB, 16% ACN; column: ProntoSIL 120–5 C18-AQ, Bischoff, Germany and were lyophilized several times from ddH2O to remove the buffer (Scheme 3).

![Scheme 3.](https://cdn.elifesciences.org/articles/82184/elife-82184-scheme3-v2.jpg)

#### HRMS (ESI-MS)

<table>
  <thead>
    <tr>
      <th>nucleotide</th>
      <th>linker</th>
      <th>calculated</th>
      <th>[M-H]-</th>
      <th>found</th>
      <th>purity (%)</th>
      <th>yield (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">GDP</td>
      <td>eda</td>
      <td>528.0651</td>
      <td>C13H20O12N7P2</td>
      <td>528.0654</td>
      <td>90</td>
      <td>38</td>
    </tr>
    <tr>
      <td>pda</td>
      <td>542.0802</td>
      <td>C14H22O12N7P2</td>
      <td>542.0809</td>
      <td>&gt;95</td>
      <td>65</td>
    </tr>
    <tr>
      <td>bda</td>
      <td>556.0964</td>
      <td>C15H24O12N7P2</td>
      <td>556.0960</td>
      <td>&gt;95</td>
      <td>29</td>
    </tr>
    <tr>
      <td rowspan="3">GTP</td>
      <td>eda</td>
      <td>608.0314</td>
      <td>C13H21O15N7P3</td>
      <td>608.0289</td>
      <td>89</td>
      <td>56</td>
    </tr>
    <tr>
      <td>pda</td>
      <td>662.0471</td>
      <td>C14H23O15N7P3</td>
      <td>662.0471</td>
      <td>87</td>
      <td>83</td>
    </tr>
    <tr>
      <td>bda</td>
      <td>636.0621</td>
      <td>C15H25N7O15P3</td>
      <td>636.0603</td>
      <td>94</td>
      <td>67</td>
    </tr>
    <tr>
      <td rowspan="3">dGTP</td>
      <td>eda</td>
      <td>592.0359</td>
      <td>C13H21O14N7P3</td>
      <td>592.0349</td>
      <td>84</td>
      <td>23</td>
    </tr>
    <tr>
      <td>pda</td>
      <td>606.0516</td>
      <td>C14H23O14N7P3</td>
      <td>606.0521</td>
      <td>93</td>
      <td>11</td>
    </tr>
    <tr>
      <td>bda</td>
      <td>620.0672</td>
      <td>C15H25N7O14P3</td>
      <td>620.0663</td>
      <td>90</td>
      <td>34</td>
    </tr>
    <tr>
      <td>GppCp</td>
      <td>eda</td>
      <td>606.0516</td>
      <td>C14H23N7O14P3</td>
      <td>606.0513</td>
      <td>89</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

### Insertion of the Michael acceptor or non-reactive acetamido derivative

The nucleotide based covalent inhibitors were prepared by dissolving eda, pda or bda nucleotides in a small amount of tetraborate buffer (100 mM, pH 8.5) and adding N-acryloxysuccinimide (1 eq.) dissolved in 25 µL DMSO. The reaction mixture was stirred for 24 h at room temperature and the reaction progress was monitored using HPLC. The covalent nucleotide analogues were purified using Q-Sepharose as described above and were stored at –20 °C as concentrated solutions (~100 mM) in 200 mM HEPES (pH 7.5; Scheme 4).

![Scheme 4.](https://cdn.elifesciences.org/articles/82184/elife-82184-scheme4-v2.jpg)

#### HRMS (ESI-MS)

<table>
  <thead>
    <tr>
      <th>Acrylamides</th>
      <th>linker</th>
      <th>calculated</th>
      <th>[M-H]-</th>
      <th>found</th>
      <th>purity (%)</th>
      <th>yield (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">GDP</td>
      <td>eda</td>
      <td>582.0751</td>
      <td>C16H22N7O13P2</td>
      <td>582.0741</td>
      <td>&gt;95</td>
      <td>57</td>
    </tr>
    <tr>
      <td>pda</td>
      <td>596.0907</td>
      <td>C17H24N7O13P2</td>
      <td>596.0907</td>
      <td>87</td>
      <td>65</td>
    </tr>
    <tr>
      <td>bda</td>
      <td>610.1064</td>
      <td>C18H26N7O13P2</td>
      <td>610.1062</td>
      <td>&gt;95</td>
      <td>78</td>
    </tr>
    <tr>
      <td rowspan="3">GTP</td>
      <td>eda</td>
      <td>662.0414</td>
      <td>C16H23N7O16P3</td>
      <td>662.0394</td>
      <td>93</td>
      <td>54</td>
    </tr>
    <tr>
      <td>pda</td>
      <td>676.0571</td>
      <td>C17H25N7O16P3</td>
      <td>676.0551</td>
      <td>&gt;95</td>
      <td>63</td>
    </tr>
    <tr>
      <td>bda</td>
      <td>690.0727</td>
      <td>C18H27N7O16P3</td>
      <td>690.0705</td>
      <td>86</td>
      <td>75</td>
    </tr>
    <tr>
      <td rowspan="3">dGTP</td>
      <td>eda</td>
      <td>646.0465</td>
      <td>C16H23N7O15P3</td>
      <td>646.0452</td>
      <td>93</td>
      <td>63</td>
    </tr>
    <tr>
      <td>pda</td>
      <td>660.0621</td>
      <td>C17H25N7O15P3</td>
      <td>660.0611</td>
      <td>90</td>
      <td>81</td>
    </tr>
    <tr>
      <td>bda</td>
      <td>674.0778</td>
      <td>C18H27N7O15P3</td>
      <td>674.0771</td>
      <td>93</td>
      <td>74</td>
    </tr>
    <tr>
      <td>GppCp</td>
      <td>eda</td>
      <td>660.0621</td>
      <td>C17H27N7O16P3</td>
      <td>660.0619</td>
      <td>79</td>
      <td>15*</td>
    </tr>
    <tr>
      <td>Acetylamides</td>
      <td>linker</td>
      <td>calculated</td>
      <td>[M-H]-</td>
      <td>found</td>
      <td>purity (%)</td>
      <td>yield (%)</td>
    </tr>
    <tr>
      <td rowspan="3">GDP</td>
      <td>eda</td>
      <td>570.0751</td>
      <td>C15H22N7O13P2</td>
      <td>570.0734</td>
      <td>&gt;95</td>
      <td>57</td>
    </tr>
    <tr>
      <td>pda</td>
      <td>584.0907</td>
      <td>C16H24N7O13P2</td>
      <td>584.0889</td>
      <td>90</td>
      <td>51</td>
    </tr>
    <tr>
      <td>bda</td>
      <td>598.1064</td>
      <td>C17H26N7O13P2</td>
      <td>598.1042</td>
      <td>79</td>
      <td>73</td>
    </tr>
    <tr>
      <td rowspan="3">GTP</td>
      <td>eda</td>
      <td>650.0414</td>
      <td>C15H23N7O16P3</td>
      <td>650.0392</td>
      <td>&gt;95</td>
      <td>23</td>
    </tr>
    <tr>
      <td>pda</td>
      <td>664.0571</td>
      <td>C16H25N7O16P3</td>
      <td>664.0553</td>
      <td>94</td>
      <td>40</td>
    </tr>
    <tr>
      <td>bda</td>
      <td>678.0727</td>
      <td>C17H27N7O16P3</td>
      <td>678.0700</td>
      <td>93</td>
      <td>31</td>
    </tr>
    <tr>
      <td colspan="7">*in case of GppCp, the total yield was calculated over 4 steps.‍</td>
    </tr>
  </tbody>
</table>

### Protein expression and purification

KRasWT1-169 and KRasG13C1-169 Cys-light (C51S C80L C118S) were expressed in BL21 (DE3) E. coli whereas the full-length KRasWT and KRasG13C were expressed in BL21 (DE3) RIL E. coli at 37 °C. Protein expression was induced at A600 nm of 0.5 by addition of 0.2–0.3 mM isopropyl-b-D-thiogalactoside (IPTG), and growth was continued at 19 °C overnight. The bacteria were collected by centrifugation and the obtained pellet resuspended in Ni-NTA buffer (KRas1-169: 50 mM Tris pH 8.0, 250 mM NaCl, 40 mM imidazole, 4 mM MgCl2, 10 µM GDP, 1 mM dithiothreitol (DTT), and 5% glycerol; full-length KRas: 50 mM HEPES pH 7.2, 500 mM LiCl, 2 mM MgCl2, 10 µM GDP, 2 mM β-mercaptoethanol (βME)). The cells were lysed with a microfluidizer, and after addition of protease inhibitor cocktail (Roche complete EDTA free) and 1% CHAPS (w/v) stirring was continued for 1 hr at 4 °C. The lysate was cleared by centrifugation (35,000 x g, 1 h) and the supernatant was loaded onto a Ni-affinity chromatography column (Qiagen Ni-NTA Superflow, 20 mL) pre-equilibrated with Ni-NTA buffer. KRas1-169 proteins were eluted with a linear gradient of imidazole buffer (40 mM – 500 mM), whereas the full-length KRas proteins were collected with a stepwise elution (2, 5, 10, 20, 30, 50, and 100% of Ni-NTA-buffer containing 500 mM imidazole). For cleavage of the N-terminal hexahistidine-tag, TEV protease was added to the pooled elution fractions and dialyzed overnight into dialysis buffer at 4 °C (KRas1-169: 25 mM Tris pH 8.0, 100 mM NaCl, 4 mM MgCl2, 10 µM GDP, 1 mM DTT, and 5% glycerol; full-length KRas: 20 mM HEPES pH 7.2, 200 mM NaCl, 2 mM MgCl2, 10 µM GDP, 2 mM βME and 5% glycerol). The cleaved protein was then applied to a reverse Ni-affinity chromatography column and finally purified by size-exclusion chromatography (GE HiLoad 16/60 Superdex 75 pg) in a final buffer containing 20 mM HEPES pH 7.5, 100 mM NaCl, 2 mM MgCl2, 10 µM GDP, 1 mM TCEP, and 5% glycerol. GST-tagged RafRBD was purified as described previously by affinity chromatography and subsequent size exclusion chromatography in a final buffer containing 20 mM HEPES pH 7.5, 100 mM NaCl, 2 mM MgCl2, 1 mM TCEP, and 5% glycerol (Herrmann et al., 1995).

### Nucleotide exchange

A total of 50 µM Ras protein was incubated with a 10-fold excess of nucleotides in 20 mM HEPES (pH 7.5), 100 mM NaCl, 2 mM MgCl2, 1 mM TCEP, 5% glycerol, and 10 mM EDTA for 3 hr at 4 °C. Nucleotide exchange was terminated by the addition of 20 mM MgCl2 and Ras proteins were washed using centrifugal filter devices to remove any unbound nucleotide. Nucleotide exchange was controlled by isocratic HPLC runs.

### Covalent modification of proteins

To analyse the amount of covalent modification of KRasG13C1-169, 50 µM Ras protein was incubated with a 10-fold excess of the acryl-bearing nucleotides in 100 mM CHES (pH 9.5), 50 mM NaCl, 1 mM TCEP, and 1 mM EDTA. After incubation at room temperature for the appropriate time, the modification of the protein was controlled by ESI-MS. For covalent modification of full-length KRasG13C, a nucleotide exchange with a 10-fold excess of the acryl-bearing nucleotides at pH 7.5 was first performed following incubation at room temperature for 24 h at pH 9.5 for covalent protein modification. Covalent protein modification was controlled by ESI-MS. The MS spectra were recorded on a VelosPro IonTrap (Thermo Scientific) with an EC 50/3 Nucleodur C18 1.8 μm column (Macherey and Nagel) and a gradient of the mobile phase A (0.1% formic acid in water) to B (0.1% formic acid in acetonitrile).

### Stopped-flow experiments

The association kinetics of the nucleotide analogues were analyzed with a SX-20 stopped-flow instrument (Applied Photophysics) at 25 °C in a buffer consisting of 25 mM HEPES (pH 7.5), 100 mM NaCl, 1 mM MgCl2, and 0.5 mM TCEP. 1 µM of nucleotide-free KRas (Müller et al., 2017) in one syringe was mixed rapidly with 2 µM mantdGDP in the other. In subsequent experiments, the second syringe contained competing nucleotides (1, 2, and 6 µM) in addition to 2 µM mantdGDP. The resulting progress curves were globally fit using KinTek Explorer to obtain the corresponding association rate constants as previously described (Table 1—source data 1, Table 1—source data 2 Johnson et al., 2009).

### HPLC-based approach for determination of affinities relative to GDP

The relative affinities of the nucleotide analogues were measured using an HPLC-based approach. 50 µM of KRasWT1-169:GDP was mixed with 50 µM of the acetamide derivatives and incubated either for 7 days at room temperature in the absence of EDTA, for 24 hr at 4 °C in the presence of 10 mM EDTA, or for 1 hr at room temperature in the presence of SOS in a buffer consisting of 20 mM HEPES (pH 7.5), 100 mM NaCl, 2 mM MgCl2, 1 mM TCEP and 5% glycerol. After incubation, the Ras proteins were washed five times with buffer (15 mL) using centrifugal filter devices to remove any unbound nucleotide, concentrated and analysed by isocratic HPLC runs. The resulting curves were analysed by integrating the corresponding peaks for GDP and the guanosine nucleotide analogues after distinct time points using the Agilent ChemStation Software (Table 1—source data 3, Table 1—source data 4).

### Calculation of the KD values of the nucleotide analogues

Based on the percentage distribution determined by the HPLC assay, the relative association constants (KrelA) for pdaGDP and bdaGDP could subsequently be calculated. In contrast, the superposition of the GDP signal prevented an exact determination of the relative association constant for edaGDP. KrelA values of 0.34 and 0.28 relative to GDP were determined for pdaGDP and bdaGDP, respectively. Finally, considering the KD value of 2.5 pM for GDP described by Jeganathan et al. the corresponding dissociation constant KD values could be determined, which are shown in Table 1—source data 4; Jeganathan et al., 2018.

$$
Ras+GDP^{k_{GDP}→}Ras:GDP
$$



$$
Ras+aGDP^{k_{aGDP}→}Ras:aGDP
$$

By rearranging the equilibrium reactions listed in (Equation 1a) and (Equation 1b), the following relationships are obtained for KGDP (Equation 2a) and KaGDP (Equation 2b):

$$
K_{GDP}=\frac{Ras:GDP}{RasGDP}
$$



$$
K_{aGDP}=\frac{Ras:aGDP}{RasaGDP}
$$

Assuming that the concentration for aGDP used in the HPLC assay is 50 µM, the following GDP concentrations for pdaGDP (Equation 3a) and bdaGDP (Equation 3b) can be determined at time t=0 hr using the percentages determined in Table 1—source data 3:

$$
GDP_{total}=\frac{%_{GDP}}{%_{pdaGDP}}=\frac{37%}{63%}\times50\muM=29.4\muM
$$



$$
GDP_{total}=\frac{%_{GDP}}{%_{bdaGDP}}=\frac{43%}{57%}\times50\muM=37.7\muM
$$

The concentrations of the components listed in equation (Equation 2b) can be calculated as follows for pdaGDP (Equation 4a, Equation 4b, Equation 4c, Equation 4d) and bdaGDP (Equation 5a, Equation 5b, Equation 5c, Equation 5d) by considering the total GDP concentrations calculated previously:

$$
[Ras:pdaGDP]=\frac{47}{100}\times29.4\muM=13.8\muM
$$



$$
[Ras:GDP]=\frac{53}{100}\times29.4\muM=15.6\muM
$$



$$
[pdaGDP]=50\muM−13.8\muM=36.2\muM
$$



$$
[GDP]=29.4\muM−15.6\muM=13.8\muM
$$



$$
[Ras:bdaGDP]=\frac{39.5}{100}\times37.7\muM=14.9\muM
$$



$$
[Ras:GDP]=\frac{60.5}{100}\times37.7\muM=22.8\muM
$$



$$
[bdaGDP]=50\muM−14.9\muM=35.1\muM
$$



$$
[GDP]=37.7\muM−22.8\muM=14.9\muM
$$

The relative association constant KrelA can be calculated by the following formula (Equation 6):

$$
K_{relA}=\frac{K_{aGDP}}{K_{GDP}}=\frac{Ras:aGDP\timesGDP}{aGDP\timesRas:GDP}
$$

By inserting the concentrations of each component determined from (Equation 4a, Equation 4b, Equation 4c, Equation 4d) and (Equation 5a, Equation 5b, Equation 5c, Equation 5d) into (Equation 6), the relative association constants KrelA for pdaGDP (Equation 7a) and bdaGDP (Equation 7b) can be calculated:

$$
K_{relA}=\frac{K_{pdaGDP}}{K_{GDP}}=\frac{13.8\muM\times13.8\muM}{36.2\muM\times15.6\muM}=0.34
$$



$$
K_{relA}=\frac{K_{bdaGDP}}{K_{GDP}}=\frac{14.9\muM\times14.9\muM}{35.1\muM\times22.8\muM}=0.28
$$

Based on the relative association constants KrelA, the KA values of the nucleotide analogues can be calculated by multiplication with the association constant of GDP:

$$
K_{A}=K_{A}GDP\timesK_{relA}
$$

The KD value of 2.5 pM described by Jeganathan et al., 2018 was used as the reference value for GDP. By substituting the reference value into KA = 1/KD, a KA value for GDP of 0.4 pM–1 was determined. Accordingly, the KA values for pdaGDP (Equation 9a) and bdaGDP (Equation 9b) are as follows:

$$
K_{A}pdaGDP=0.4pM^{-1}\times0.34=0.136pM^{-1}
$$



$$
K_{A}bdaGDP=0.4pM^{-1}\times0.28=0.112pM^{-1}
$$

By converting the determined KA values into the corresponding KD values using KD = 1/KA, the following dissociation constants could be determined for pdaGDP (Equation 10a) and bdaGDP (Equation 10b):

$$
K_{D}pdaGDP=\frac{1}{0.136pM^{-1}}=7.4pM
$$



$$
K_{D}bdaGDP=\frac{1}{0.112pM^{-1}}=8.9pM
$$

### Crystallization and structure determination

KRasG13C1-169 Cys-light (C51S C80L C118S) was covalently modified by incubating 100 µM KRas with a 10-fold excess of the acryl-bearing nucleotide in 100 mM CHES (pH 9.5), 50 mM NaCl, 1 mM TCEP, and 1 mM EDTA at room temperature for 24 hr. Modification of the protein was monitored by ESI-MS and terminated by the addition of 20 mM MgCl2. The protein was purified by size-exclusion chromatography (GE HiLoad 16/60 Superdex 75 pg) in a final buffer containing 20 mM HEPES pH 7.5, 100 mM NaCl, 2 mM MgCl2, 1 mM TCEP, and 5% glycerol, and subsequently concentrated to 67 mg/mL. To identify the initial crystallization conditions, commercially available protein crystallization screens (JCSG Core I –IV Suites, PEGs and PACT) were used. Using a TTP labtech Mosquito LCP crystal liquid-handling robot, 100 nL of protein solution was mixed with 100 nL reservoir solution in 96-well plates, and crystals were grown using the hanging-drop method at 20 °C. After 1 day of incubation, one successful crystallization condition was obtained for KRasG13C-edaGDP (0.2 M (NH4)F, 20% PEG3350) and KRasG13C-bdaGDP (0.2 M NaF, 20% PEG3350), and the crystals were cryoprotected in mother liquor and flash cooled in liquid nitrogen. The data sets were collected at the PXII X10SA beamline of the Swiss Light Source (Paul Scherrer Institute, Villigen, Switzerland) and indexed and scaled using XDS (Kabsch, 2010). The crystal structures were solved by molecular replacement with PHASER using PDB 4obe as a template (Read, 2001). The manual modification of the molecule of the asymmetric unit was performed using the program COOT (Emsley and Cowtan, 2004), and with the help of the Dundee PRODRG server (Schüttelkopf and van Aalten, 2004), the inhibitor topology file was generated. For multiple cycles of refinement, PHENIX.refine (Adams et al., 2010) was employed, the final structure was evaluated by the PDB_REDOserver (Joosten et al., 2014) and crystal structures were visualized using PyMOL. Data collection, structure refinement statistics, and further details for data collection are provided in Figure 2—figure supplement 1.

### Guanine nucleotide-exchange factor assay

SOS-catalysed nucleotide exchange was monitored at 25 °C in a FluoroMax-3 spectrofluorometer (excitation at 360 nm, emission at 440 nm) in 20 mM HEPES (pH 7.5), 100 mM NaCl, 2 mM MgCl2, and 1 mM TCEP. 5 µM KRas1-169 was mixed with 10 µM mantdGDP and subsequently with different concentrations of SOS (0.25 µM and 0.5 µM) (Figure 3A; Figure 3—figure supplement 1).

### GAP-stimulated GTP hydrolysis

First, for KRasWT1-169, nucleotide exchange with GTP was performed at pH 7.5, and for KRasG13C1-169, covalent modification with a 10-fold excess of acryl-edaGTP at pH 9.5 was done, both in the presence of 50 mM EDTA to block intrinsic GTP hydrolysis. After incubation, the Ras proteins were washed five times with buffer (20 mM HEPES (pH 7.5), 100 mM NaCl, and 1 mM TCEP) using centrifugal filter devices to remove any unbound nucleotide. Nucleotide exchange of KRasWT1-169 was controlled by isocratic HPLC runs, and covalent modification of KRasG13C1-169 was verified by ESI-MS. GTP hydrolysis of Ras proteins was initiated by addition of 2 mM MgCl2 in the absence or presence of Ras-GAP (1:1000 for KRasWT1-169:GTP and 1:1 for KRasG13C1-169-edaGTP). At defined time points (0, 5, 10, 15, 20, 30, 45, 60, 90 and 120 min), samples were taken and immediately snap-frozen in liquid nitrogen. For KRasWT1-169:GTP, samples were thawed and denatured for 5 min at 95 °C. Samples were centrifuged at 14,000 rpm for 10 min at 4 °C and subsequently analysed by isocratic HPLC runs. For KRasG13C1-169-edaGTP, samples were centrifuged and analysed by ESI-MS. The relative amount of each nucleotide was determined by integrating the area of the GTP and GDP peaks using Origin (Figure 3—figure supplement 2; Eberth and Ahmadian, 2009).

### Effector binding (pull-down experiments)

Pull-down experiments were performed in 20 mM HEPES pH 7.5, 50 mM NaCl and 2 mM MgCl2. 10 µg KRasG13C:GDP or the covalently modified KRasG13C-edaGDP and 20 µg GST-tagged cRafRBD (amino acids 51–131) were incubated with/ without 100 µM GppNHp and with/ without 1 µg SOS over night at room temperature. Afterwards, 50 µL glutathione magnetic beads were added to each sample for 30 min. After washing the beads with 500 µL buffer, the beads were settled with a magnet and the supernatant was carefully removed. The beads were resuspended in 50 µL of 4xSDS-loading buffer and visualized via SDS-PAGE (Figure 3—figure supplement 3).

### In vitro farnesylation

50 µM of full-length KRas protein was mixed with 250 µM farnesyl pyrophosphate (FPP) and 10 µM farnesyltransferase (FTase). After incubation at room temperature for 1 hr the mixture was centrifugated at 14,000 rpm for 10 min at 4 °C and analyzed via ESI-MS (Figure 3—figure supplement 4).

### Competition assay

To analyze the amount of covalent modification of KRasG13C1-169 (Cys-light) with the acryl-bearing nucleotide analogue (edaGDP) under competitive conditions with GDP and GTP, four different conditions were tested (buffer: 100 mM CHES pH 9.5., 50 mM NaCl, 1 mM TCEP, 2 mM MgCl2, 5% glycerol). 5 µM KRasG13C (Cys-light) was incubated (1) in the presence of 36 µM edaGDP with and without SOS, (2) in the presence of 305 µM edaGDP, 36 µM GDP and 305 µM GTP with and without SOS, (3) in the presence of 36 µM edaGDP, 36 µM GDP and 305 µM GTP with and without SOS and (4) 36 µM edaGDP, 360 µM GDP, and 3050 µM GTP with and without SOS. After incubation for 1, 2, 3, 4, 5, 22, and 24 hr at room temperature, the covalent protein modification was controlled by ESI-MS.

### MS/MS analysis

For MS/MS analysis, the samples were dissolved in 100 mM TEAB and incubated for 1 hr at 55 °C in the presence of 10 mM TCEP. 17 mM iodoacetamide was added and the samples were incubated in the dark at room temperature for 30 min. Samples were precipitated by adding pre-chilled acetone and stored overnight at –20 °C. After drying the pellets, Trypsin (Roche) was added and the samples were digested at 37 °C with 300 rpm shaking overnight. The digestion was quenched by the addition of 2% TFA and a stage tip purification (Rappsilber et al., 2007) was performed, samples were evaporated to dryness and stored at –20 °C until MS/MS analysis. For nanoHPLC-MS/MS analysis samples were dissolved in 20 μL of 0.1% TFA in water and 3 μL were injected onto an UltiMateTM 3000 RSLCnano system (ThermoFisher Scientific, Germany) online coupled to a Q Exactive Plus Hybrid Quadrupole-Orbitrap Mass Spectrometer equipped with a nanospray source (Nanospray Flex Ion Source, Thermo Scientific). All solvents were LC-MS grade. Samples were injected onto a pre-column cartridge (5 μm, 100 Å, 300 μm ID * 5 mm, Dionex, Germany) using 0.1% TFA in water as eluent with a flow rate of 30 μL/min. Desalting was performed for 5 min with eluent flow to waste followed by back-flushing of the sample during the whole analysis from the pre-column to the PepMap100 RSLC C18 nano-HPLC column (2 μm, 100 Å, 75 μm ID ×50 cm, nanoViper, Dionex, Germany) using a linear gradient starting with 95% solvent A (water containing 0.1% formic acid) / 5% solvent B (acetonitrile containing 0.1% formic acid) and increasing to 30% solvent B in 90 min using a flow rate of 300 nL/min. Afterwards, the column was washed (two steps 60 and 95% solvent B) and re-equilibrated to starting conditions. The nanoHPLC was online coupled to the Quadrupole-Orbitrap Mass Spectrometer using a standard coated SilicaTip (ID 20 μm, Tip-ID 10 μM, New Objective, Woburn, MA, USA). Mass range of m/z 300–1,650 was acquired with a resolution of 70000 for a full scan, followed by up to 10 high energy collision dissociation (HCD) MS / MS scans of the most intense at least doubly charged ions using a resolution of 17500 and a NCE energy of 25%. Data evaluation was performed using MaxQuant software (Cox and Mann, 2008) (v.1.6.3.4) including the Andromeda search algorithm (Cox et al., 2011) and searching the KRas sequence together with a database containing typical contaminants like keratins, trypsin etc., which is included in the MaxQuant software. The search was performed for full enzymatic trypsin cleavages allowing two miscleavages. For database search oxidation of methionine and N-terminal acetylation of proteins, carbamidomethylation of cysteines, and artificial modification of cysteines were defined as variable modifications. The mass accuracy for full mass spectra was set to 20 ppm (first search) and 4.5 ppm (second search), respectively and for MS/MS spectra to 20 ppm. The false discovery rates for peptide and protein identification were set to 1%. For further analysis, the peptide intensities of KRas were compared for modified and unmodified KRas. (Figure 3—figure supplement 5).

### Cell culture

HeLa cells were obtained from the American Type Culture Collection (ATCC) and were cultured in DMEM medium (Gibco) supplemented with 10% fetal bovine serum (FBS) (PAN-Biotech) and 1% penicillin/streptomycin (Gibco). Cells were cultured in a humidified incubator at 37 °C in the presence of 5% CO2. The identity of the cells was validated by STR profiling and the cells were tested negative for mycoplasma contamination.

### Electroporation

Electroporation of full-length KRas constructs (KRasWT, KRasG13C, KRasG13C-edaGDP, KRasG13C:acetyledaGDP and KRasG13C-edaGppCp) was performed based on the protocol described by Alex et al., 2019 using the Neon Transfection System Kit (Thermo Fisher). For electroporation, 3 million cells per experiment were harvested by trypsinization, washed with PBS, and resuspended in 85 µL of the electroporation buffer R (Thermo Fisher). Increasing amounts of recombinant protein samples for each construct (0, 50, 100, 200 and 300 µg) were diluted 1:1 in buffer R followed by the addition of 30 µL of this protein master mix to the cell suspension. This cellular slurry was loaded into a 100 mL Neon Pipette Tip (Thermo Fisher) and electroporated with 2x35 ms pulses at 1000 V. After electroporation, the cells were washed twice with PBS (15 mL) to remove non-internalized extracellular protein and the cell pellet was resuspended in 2 mL complete growth media. Cells were transferred into six-well tissue culture plates (Sarstedt) and incubated for 24 hr at 37 °C and 5% CO2 in a humidified incubator for recovery before being processed for western blotting analysis.

### Western blot analysis

After recovery of the electroporation, cells were washed twice with ice-cold PBS and lysed in 100 µL of phosphatase and protease inhibitor containing RIPA buffer (Cell Signaling Technology). Cells were incubated on ice for 30 min and then harvested by scraping followed by centrifugation at 14,000 rpm for 10 min at 4 °C. Protein concentrations were determined using the Pierce BCA protein assay (Thermo) following the manufacturer’s recommended procedure. Equal amounts of protein (10 µg) were analyzed by SDS-PAGE and transferred to Immobilon-FL PVDF membranes (Merck Millipore) using Pierce 1-step transfer buffer (Thermo) and the Pierce Power Blotter (Thermo). Membranes were washed with ddH2O for 5 min, blocked with OdysseyBlocking Buffer TBS (Li-Cor) for 1 hr at room temperature and then incubated with primary antibodies diluted in OdysseyBlocking Buffer TBS overnight at 4 °C with gentle agitation. KRas (Sigma Aldrich, SAB1404011-100UG), pcRafS338 (CST, 9427), tAkt1 (CST, 2938), pAktS473 (CST, 4060), tErk (CST, 4696), pErkT202/Y204 (CST, 4370), pS6S235/236 (CST, 4858), and β-actin (CST, 4970/Sigma-Aldrich, A5441) antibodies were used to detect the individual proteins. After primary antibody incubation, membranes were washed three times with TBS-T (50 mM Tris, 150 mM NaCl, 0.05% Tween 20, pH 7.4) for 5 min before being incubated with secondary antibodies (anti-mouse IgG (H+L) (DyLight 680 Conjugate) (CST, 5470) / anti-rabbit IgG (H+L) (DyLight 800 4 X PEG Conjugate) (CST, 5151)) diluted in OdysseyBlocking Buffer TBS for 1 hr at room temperature with gentle agitation. After secondary antibody incubation, the membranes were washed three times for 5 min with TBS-T and then scanned using an OdysseyCLx imaging system (Li-Cor). Quantification of protein levels from western blots was performed using Empiria Studio (Li-Cor) (Figure 3B, C, Figure 3—figure supplements 6–9).
