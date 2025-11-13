# Computational design of peptides to target NaV1.7 channel with high potency and selectivity for the treatment of pain

## Authors

- Phuong T Nguyen<sup>1</sup> ([ORCID: 0000-0002-9461-7807](https://orcid.org/0000-0002-9461-7807))
- Hai M Nguyen<sup>2</sup> ([ORCID: 0000-0002-1422-7041](https://orcid.org/0000-0002-1422-7041))
- Karen M Wagner<sup>3</sup>
- Robert G Stewart<sup>1</sup>
- Vikrant Singh<sup>2</sup>
- Parashar Thapa<sup>1</sup>
- Yi-Je Chen<sup>2</sup>
- Mark W Lillya<sup>1</sup>
- Anh Tuan Ton<sup>4</sup>
- Richard Kondo<sup>4</sup>
- Andre Ghetti<sup>4</sup>
- Michael W Pennington<sup>5</sup> ([ORCID: 0000-0001-5446-3447](https://orcid.org/0000-0001-5446-3447))
- Bruce Hammock<sup>3</sup> ([ORCID: 0000-0003-1408-8317](https://orcid.org/0000-0003-1408-8317))
- Theanne N Griffith<sup>1</sup> ([ORCID: 0000-0003-0090-6286](https://orcid.org/0000-0003-0090-6286))
- Jon T Sack<sup>1</sup> ([ORCID: 0000-0002-6975-982X](https://orcid.org/0000-0002-6975-982X))
- Heike Wulff<sup>2</sup> ([ORCID: 0000-0003-4437-5763](https://orcid.org/0000-0003-4437-5763)) †
- Vladimir Yarov-Yarovoy<sup>1</sup> ([ORCID: 0000-0002-2325-4834](https://orcid.org/0000-0002-2325-4834)) †

### Affiliations

1. Department of Physiology and Membrane Biology, University of California Davis Davis United States ([ROR:05rrcem69](https://ror.org/05rrcem69))
2. Department of Pharmacology, University of California Davis Davis United States ([ROR:05rrcem69](https://ror.org/05rrcem69))
3. Department of Entomology and Nematology & Comprehensive Cancer Center, University of California Davis Davis United States ([ROR:05rrcem69](https://ror.org/05rrcem69))
4. AnaBios Corporation San Diego United States ([ROR:00yjxga86](https://ror.org/00yjxga86))
5. Ambiopharm Inc North Augusta United States
6. Department of Anesthesiology and Pain Medicine, University of California Davis Davis United States ([ROR:05rrcem69](https://ror.org/05rrcem69))
7. Biophysics Graduate Group, University of California Davis Davis United States ([ROR:05rrcem69](https://ror.org/05rrcem69))

† Corresponding author

## Abstract

The voltage-gated sodium NaV1.7 channel plays a key role as a mediator of action potential propagation in C-fiber nociceptors and is an established molecular target for pain therapy. ProTx-II is a potent and moderately selective peptide toxin from tarantula venom that inhibits human NaV1.7 activation. Here we used available structural and experimental data to guide Rosetta design of potent and selective ProTx-II-based peptide inhibitors of human NaV1.7 channels. Functional testing of designed peptides using electrophysiology identified the PTx2-3127 and PTx2-3258 peptides with IC50s of 7 nM and 4 nM for hNaV1.7 and more than 1000-fold selectivity over human NaV1.1, NaV1.3, NaV1.4, NaV1.5, NaV1.8, and NaV1.9 channels. PTx2-3127 inhibits NaV1.7 currents in mouse and human sensory neurons and shows efficacy in rat models of chronic and thermal pain when administered intrathecally. Rationally designed peptide inhibitors of human NaV1.7 channels have transformative potential to define a new class of biologics to treat pain.

## Introduction

More than 25 million Americans suffer from chronic pain (Nahin, 2015). Chronic pain originates from tissue or nervous system damage and persists longer than three months (Treede et al., 2015). The many causes of chronic pain include surgery, chemotherapy, complex regional pain syndrome, and back pain. People with chronic pain experience higher anxiety, depression, sleep disturbances, and gain weight due to decreased physical activity. Non-opioid treatment options for chronic pain are limited (Seal et al., 2017). Inhibitors of neuronal ion channels are important alternatives that have not demonstrated addiction liability. Non-selective NaV channel inhibitors, including carbamazepine, lacosamide, and lamotrigine are used among initial options to treat patients with chronic pain (Beyreuther et al., 2007; Wiffen et al., 2011; Wiffen et al., 2014). For example, intravenous infusion of the local anesthetic lidocaine, a non-specific NaV channel inhibitor, reduces chronic pain in some patients (Hutson et al., 2015; Iacob et al., 2018; Kandil et al., 2017; van der Wal et al., 2016). However, lidocaine treatments have serious side effects including cardiac arrest, abnormal heartbeat, and seizures. Patients with chronic pain who are not responding to NaV channel inhibitors can be prescribed opioids, but the severe side effects of opioids such as constipation, respiratory depression, and addiction limit their utility. Intrathecal infusion of the voltage-gated calcium channel inhibitor ziconotide is also effective against chronic pain (Bäckryd, 2018; Deer et al., 2018) but accompanied by serious psychiatric side effects (Bäckryd, 2018). Consequently, the treatment of chronic pain remains a major unmet medical need. NaV channels have been thoroughly clinically validated as pharmacological targets for pain treatment, but currently available therapies are limited by incomplete efficacy and significant side effects (Bhattacharya et al., 2009; Dib-Hajj et al., 2010; Kaczorowski et al., 2008; Liu and Wood, 2011; Mulroy, 2002; Walia et al., 2004).

Nociceptive signals originate in peripheral nerve fibers that transduce chemical, mechanical, or thermal stimuli into action potentials that propagate along their axons to the synaptic nerve terminals in the spinal dorsal horn (Basbaum et al., 2009; Dib-Hajj et al., 2010; Dib-Hajj et al., 2013; Waxman and Zamponi, 2014). Voltage-gated sodium (NaV) channels are key molecular determinants of action potential generation and propagation in excitable cells. Of the nine known human NaV (hNaV) channel subtypes (Catterall et al., 2005), genetic and functional studies identified three subtypes as important for pain signaling: NaV1.7, NaV1.8, and NaV1.9, which are predominantly expressed in peripheral neurons (Bennett et al., 2019; Black et al., 2008; Cox et al., 2006; Cummins et al., 2004; Dib-Hajj et al., 2010; Dib-Hajj et al., 2013; Estacion et al., 2009; Fertleman et al., 2006; Goldberg et al., 2012; Nassar et al., 2004; Reimann et al., 2010; Shields et al., 2012; Yang et al., 2012; Yang et al., 2004). NaV1.7 possesses a slow closed-state inactivation compared with other channels (Herzog et al., 2003), making it uniquely important for setting the threshold for action potential firing, and thus the gain in pain signaling neurons (Dib-Hajj et al., 2007; Rush et al., 2007). In accordance with this, loss-of-function mutations in hNaV1.7 have been identified in families with congenital insensitivity to pain (Cox et al., 2006). Gain-of-function mutations in hNaV1.7 lead to inherited pain disorders; families with inherited erythromelalgia have hNaV1.7 mutations that shift its voltage-dependence of activation to hyperpolarized voltages, leading to hyperexcitability in dorsal root ganglion (DRG) neurons and chronic neuropathic pain (Cummins et al., 2004; Yang et al., 2004); patients with paroxysmal extreme pain disorder have defects in hNaV1.7 fast inactivation resulting in persistent sodium currents and episodic burning pain (Fertleman et al., 2006). These and other studies have validated hNaV1.7 as a prime target for the treatment of pain (Dib-Hajj et al., 2010; Dib-Hajj et al., 2013; Waxman and Zamponi, 2014).

Mammalian NaV channels are composed of four homologous domains (I through IV), each containing six transmembrane segments (S1 through S6), with segments S1-S4 of the channel forming the voltage-sensing domain (VSD) and segments S5 and S6 forming the pore (Ahern et al., 2016; Payandeh et al., 2011; Shen et al., 2019; Shen et al., 2017). The binding of local anesthetics to a receptor site formed within the pore inner cavity can directly block ion conduction through the NaV channels (Ragsdale et al., 1994; Yarov-Yarovoy et al., 2001; Yarov-Yarovoy et al., 2002). However, because of the high conservation of residues forming this local anesthetic receptor site among the different isoforms, all currently available therapeutic drugs targeting NaV channels are non-specific.

There is a growing trend in industry and academia to target ion channels with biologics (Bosmans and Swartz, 2010; Neff and Wickenden, 2021; Payandeh and Hackos, 2018; Wulff et al., 2019). More than 10 years ago scientists at Merck demonstrated that a peptide from the venom of the Peruvian green velvet tarantula Thrixopelma pruriens, termed Protoxin-II (ProTx-II), selectively targeted the NaV1.7 channel subtype and blocked action potential propagation in nociceptors (Schmalhofer et al., 2008). Amgen also developed peptide inhibitors of NaV1.7 and identified a novel peptide toxin from the venom of the Chilean tarantula Grammostola porteria, termed GpTx-1, which was a less potent inhibitor of human NaV1.7, compared with ProTx-II, but had 20-fold and 1000-fold selectivity against NaV1.4 (predominantly expressed in muscle) and NaV1.5 (predominantly expressed in the heart) (Murray et al., 2015). Using the GpTx-1 NMR structure as a guide, Amgen scientists created a variant with improved potency and selectivity compared with the wild-type toxin, concluding that GpTx-1 variants can potentially be further developed as peptide therapeutics (Murray et al., 2015). The most advanced reported preclinical development of NaV-selected peptides is from Janssen Biotech, which demonstrated that ProTx-II exerted a strong analgesic effect following intrathecal injection in rat models of thermal and chemical nociception. While efficacious, ProTx-II had a narrow therapeutic window, and induced profound motor effects at moderately higher doses, consistent with inhibition of NaV channel subtypes present on motor neurons (NaV1.1 and NaV1.6) (Flinspach et al., 2017). Janssen Biotech pursued resource-intensive optimization of ProTx-II, but without a structure to guide optimization. This blind optimization process produced 1500 ProTx-II variants, including a peptide, named JNJ63955918, with at least 100-fold selectivity for NaV1.7 over all other NaV channel subtypes tested. However, JNJ63955918 had ~10 fold reduced affinity for NaV1.7 (Flinspach et al., 2017). The in vivo safety window for JNJ63955918 was 7–16-fold, limited by motor deficits and muscle weakness, consistent with insufficient selectivity against off-target NaV channels (Flinspach et al., 2017). More recently, Merck developed ProTx-II analogues with improved selectivity for NaV1.7, reduced ability to cause mast cell degranulation, and enhanced in vivo profile (Adams et al., 2022).

While these prior and ongoing efforts have not succeeded in developing peptides with a sufficiently wide in vivo safety window, the premise that NaV channel blocking peptide affinity and selectivity could be further optimized remains valid (Payandeh and Hackos, 2018). Furthermore, several high-resolution structures of peptide toxins complexes with human NaV channels were solved recently (Clairfeuille et al., 2019; Pan et al., 2019; Shen et al., 2019; Xu et al., 2019), providing essential templates for the structure-guided design of novel therapeutics. These structures revealed key molecular determinants of ProTx-II interaction with the hNaV1.7 channel in both deactivated and activated states (Shen et al., 2019; Xu et al., 2019). To overcome past issues with peptide optimization, we used the Rosetta computational protein redesign approach, available experimental data, and functional testing of designed peptides using electrophysiological assays, mouse and human sensory neurons, stability assays, and efficacy testing in animal models of pain to generate high-affinity, selective inhibitors of human NaV1.7 channels. Our lead peptides have better potency and selectivity than Janssen’s most potent and selective ProTx-II variant. Our lead peptide inhibits sodium current in human and mouse sensory neurons, is stable in artificial cerebrospinal fluid, and is active in rat models of thermal and chronic pain.

## Results

### Design of ProTx-II based peptides targeting hNaV1.7

To optimize potency and selectivity of ProTx-II based peptides to target hNaV1.7, we analyzed x-ray and cryoEM structures of ProTx-II – hNaV1.7 complexes (Shen et al., 2019; Xu et al., 2019), explored available experimental data on hNaV1.7 interactions with ProTx-II and its homologs (Moyer et al., 2018; Murray et al., 2015; Park et al., 2014; Wu et al., 2018; Xu et al., 2019; Zeng et al., 2007), modeled specific interactions of ProTx-II substitutions with hNaV1.7, and designed new ProTx-II variants using Rosetta (Bender et al., 2016; Kuhlman et al., 2003). We learned in each optimization round which particular combination of mutations resulted in the most potent and selective ProTx-II redesign. Mutations that improved the potency and selectivity of ProTx-II-based peptides were kept in the following round(s) of optimization. Our interdisciplinary and iterative peptide optimization approach is described below and outlined in Figure 1.

![Figure 1.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig1-v3.jpg)

**Figure 1.:** Top, transmembrane (left) and extracellular (right) views of the wild-type ProTx-II – hNav1.7 structure in a deactivated state (Xu et al., 2019) Key residues on the wild-type ProTx-II are shown in stick representation and labeled. Bottom, interdisciplinary peptide optimization approach involving Rosetta design, molecular dynamics (MD) simulations, peptide synthesis and folding, electrophysiological testing, peptide stability testing, efficacy in mouse and human DRG neurons, and efficacy in animal models of pain.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** Molecular dynamics simulation of the NavAb/hNav1.7 – ProTx-II complex. (A) A simulation system containing NavAb/hNav1.7 chimeric channel (yellow ribbon), ProTx-II (magenta ribbon), POPC lipid (blue blob), sodium ions (yellow sphere), chloride ion (green sphere), water (transparent surface). (B) Heatmap showing fractional contacts of ProTx-II residues with the surrounding environment categorized as lipid tail, lipid head, VSDII, and water normalized over the time course of the simulation.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig1-figsupp2-v3.jpg)

**Figure 1—figure supplement 2.:** Each peptide toxin sequence name includes 4 letter PDB ID code for the corresponding structure.

#### 1st optimization round

During the first round of optimization, we introduced multiple ProTx-II substitutions guided by available experimental data and insights from the cryoEM structure of the ProTx-II – NaVAb/hNaV1.7 chimera complex in a deactivated state (PDB: 6N4R) (Xu et al., 2019). To improve potency in all of our ProTx-II based peptides, we used the C-terminal amidation based on previously published data (Park et al., 2014). The ProTx-II – NaVAb/hNaV1.7 structure revealed that ProTx-II residues W5 and M6 are positioned in the membrane hydrophobic core and make contact with the unique residue F813 on the S3 segment of hNaV1.7 VSD-II (F812 in the NaVAb/hNaV1.7 structure) (Xu et al., 2019; Figure 1 and Figure 1—figure supplement 1). We introduced the W5A and M6F substitutions in ProTx-II with the insight from an Amgen’s study showing that the double mutant F5A/M6F on GpTx-1 (ProTx-II homolog) improved selectivity for hNaV1.7 over hNaV1.4 (Murray et al., 2015) and reasoning that optimized interactions with F813 may improve ProTx-II based peptide selectivity. In addition, the ProTx-II – NaVAb/hNaV1.7 structure revealed that the hydrophobic residue V20 is positioned in a hydrophilic environment and faces the hNaV1.7 VSD-II S3-S4 loop region (Figure 1 and Figure 1—figure supplement 1). Based on the sequence comparison of ProTx-II to other highly potent peptide toxins targeting the hNaV1.7 VSDII S3-S4 loop region (see Figure 1—figure supplement 2), we noticed that ProTx-III (hNaV1.7 IC50=11.5 nM) has Lysine and JzTx-V (hNaV1.7 IC50=0.6 nM) has Arginine (Cardoso et al., 2015; Moyer et al., 2018) at the position equivalent to the V20 in ProTx-II. Rosetta modeling of the ProTx-II V20R mutant suggested that arginine could form a salt bridge with D816 on the hNaV1.7 VSD-II S3-S4 loop region (Figure 2A and B). Because D816 is only present in the hNaV1.7 and hNaV1.6 subtypes among all human NaV channels (see Figure 2—figure supplement 1), we made the V20R substitution to potentially improve selectivity for hNaV1.7. A Genentech study demonstrated that substituting R22 with nor-arginine (norR) and K26 with arginine improves ProTx-II potency to below IC50=0.1 nM for hNaV1.7 (Xu et al., 2019). Amgen’s study demonstrated that substituting K28 with glutamate improves the selectivity of JzTx-V for hNaV1.7 over NaV1.4 and NaV1.5 (Moyer et al., 2018). Based on these data, we substituted ProTx-II R22 with norR, K26 with arginine, and K28 with glutamate (Figure 2A and B). We also substituted M19 with leucine to improve peptide stability by preventing methionine-dependent oxidation.

![Figure 2.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig2-v3.jpg)

**Figure 2.:** (A) Sequence alignment of the wild-type ProTx-II with PTx2-2954 and PTx2-2955 peptides. (B) Transmembrane (left panel) and extracellular (right panel) views of the PTx2-2955 – hNaV1.7 model. Key residues on the PTx2-2955 and hNaV1.7 are shown in stick representation and labeled. Nitrogen atoms are colored in blue and oxygen atoms are colored in red. Hydrogen bonds between donor and acceptor atoms are shown by blue dash line. (C) Block of whole-cell hNaV1.7 sodium currents by application of increasing concentrations of PTx2-2955 and followed by 1 mM of wild-type ProTx-II as indicated. (D) Inhibition of hNaV1.7 currents was measured as shown in C and plotted as a function of WT ProTx-2 or PTx2-2955 concentration. Fitting the Hill equation to the data yielded IC50 values (95% confidence interval) of 1.7 [0.5, 2.9] nM (n=3) for WT ProTx-II and 185.0 [152.1, 217.9] nM (n=5) for PTx2-2955, respectively.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** Sequence alignment of the extracellular S1-S2 of the VSD-II (top panel) and the extracellular S3-S4 (bottom panel) regions of human Nav channels.

We incorporated these substitutions into two designed ProTx-II variants named PTx2-2954 and PTx2-2955 (Figure 2A). Specifically, PTx2-2954 contains the W5A, M6F, M19L, V20R, R22norR, and K28E substitutions and the PTx2-2955 variant contains the W5A, M6F, M19L, V20R, R22norR, K26R, and K28E substitutions (Figure 2A). The potency of PTx2-2954 and PTx2-2955 for hNaV1.7 was determined using whole-cell voltage-clamp recordings in HEK 293 cells as described in the Methods. PTx2-2955 inhibited hNaV1.7 currents with an IC50 of 185 nM (Figure 2C and D and Table 1). However, PTx2-2954 had no effect on hNaV1.7 currents at 5 µM (Figure 2A). We currently have no explanation for why the PTx2-2954 peptide was not active on hNaV1.7 despite having only an arginine versus lysine difference at position 26. Notably, PTx2-2955 included V20R, K26R, and K28E mutations compared with the wild-type ProTx-II which ultimately benefited the potency and selectivity of our top designs (see 3rd and 4th optimization rounds below). Mutations W5A, M6F, and R22norR did not improve potency and selectivity and were eliminated in the following rounds of optimization. Based on these results, PTx2-2955 peptide was selected as the most potent peptide from the 1st optimization round.

**Table 1.**
 Potency of redesigned ProTx-II peptides.


<table>
  <thead>
    <tr>
      <th>Rank</th>
      <th>Peptide</th>
      <th>IC50 (nM)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>WT ProTx-II</td>
      <td>0.3–1.7</td>
    </tr>
    <tr>
      <td>2</td>
      <td>PTx2-3258</td>
      <td>3.8</td>
    </tr>
    <tr>
      <td>3</td>
      <td>PTx2-3128</td>
      <td>5.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>PTx2-3127</td>
      <td>6.9</td>
    </tr>
    <tr>
      <td>5</td>
      <td>PTx2-3361</td>
      <td>8.6</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Janssen’s (JNJ63955918)</td>
      <td>10.0</td>
    </tr>
    <tr>
      <td>7</td>
      <td>PTx2-3260</td>
      <td>20.8</td>
    </tr>
    <tr>
      <td>8</td>
      <td>PTx2-3066</td>
      <td>30.8</td>
    </tr>
    <tr>
      <td>9</td>
      <td>PTx2-3259</td>
      <td>41.8</td>
    </tr>
    <tr>
      <td>10</td>
      <td>PTx2-3067</td>
      <td>48.3</td>
    </tr>
    <tr>
      <td>11</td>
      <td>PTx2-3064</td>
      <td>52.6</td>
    </tr>
    <tr>
      <td>12</td>
      <td>PTx2-3065</td>
      <td>73.9</td>
    </tr>
    <tr>
      <td>13</td>
      <td>PTx2-3063</td>
      <td>154.0</td>
    </tr>
    <tr>
      <td>14</td>
      <td>PTx2-2955</td>
      <td>185.0</td>
    </tr>
    <tr>
      <td>15</td>
      <td>PTx2-3126</td>
      <td>2300.0</td>
    </tr>
  </tbody>
</table>

#### 2nd optimization round

While the potency of PTx2-2955 was not in the low nanomolar range, the molecular interactions revealed by computational modeling were useful for further rounds of optimization. R26 in PTx2-2955 has extensive contacts with VSD-II and forms a salt bridge with E811 (Figure 3A and B). In addition, a hydrogen-bonding network is formed between residues R20, E28 on PTx2-2955 with D816 on VSD-II, a unique residue in hNaV1.7 and hNaV1.6 (Figure 2—figure supplement 1). We reasoned that such interactions are important for selectivity and given that the ProTx-II – VSD-II protein-protein interface is highly polar, room for further optimization of the molecular interface of ProTx-II and VSD-II may be limited. We preserved these interactions in this round of optimization and explored substitutions at other positions. Specifically, we designed PTx2-3063 based on PTx2-2955 with an extra substitution E12A which was reported to improve the potency of ProTx-II for hNaV1.7 (Park et al., 2014). Notably, in the presence of R26, Norarginine at position 22 does not form a salt bridge with D816 on VSD-II despite being in proximity based on the PTx2-2955 model (Figure 3B). We mutated the Norarginine back to Arginine to promote the hydrogen bond with D816 as it appeared in the wt ProTx-II (Figure 1) and incorporated this into the design of PTx2-3064. In the presence of R22, the hydrogen bond network at the interacting interface is expanded to E28, R20, and R22 on ProTx-II and D816 on VSDII (Figure 3B). We further used Rosetta computational design to explore sequence variants at the non-interface positions of ProTx-II, explicitly looking for substitutions that can stabilize the ProTx-II scaffold or the interface hydrogen bond network while taking into account potential favorable interactions with lipids (see Methods). We also changed the double mutants W5A/M6F back to the wild-type residues in the design process due to the lack of superior engagement with F813 (VSD-II) shown in the PTx2-2955 model. We used Rosetta FastDesign (Maguire et al., 2021) to introduce ProTx-II substitutions and design new peptide variants as described in Methods. Among the ProTx-II based peptide consensus sequences designed by Rosetta (Figure 3—figure supplement 1), we selected the double mutant S11K/E12D and W7Q to introduce in this round. S11K/E12D allows a salt bridge to be formed between K and D while Q7 forms a hydrogen bond with a backbone carbonyl atom on ProTx-II, thus potentially stabilizing the ProTx-II scaffold and the hydrogen bond network between E28, R20, and R22 on ProTx-II and D816 on VSD-II (Figure 3B). We combined these substitutions with other substitutions previously reported to improve potency or selectivity. In particular, the Rosetta suggested substitution W7Q in addition to Y1Q, and W30L was shown to improve selectivity while M19F improved potency for hNaV1.7 (Flinspach et al., 2015; Neff and Wickenden, 2021). To reduce the potential of misfolding due to multiple substitutions, we strategically introduced these changes into three designed variants PTx2-3065, PTx2-3066, and PTx2-3067.

![Figure 3.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig3-v3.jpg)

**Figure 3.:** (A) Sequence alignment of the wild-type ProTx-II with PTx2-2955 and PTx2-2963 - PTx2-2967 peptides. (B) Transmembrane (left panel) and extracellular (right panel) views of the PTx2-3066 – hNaV1.7 model. Key residues on the PTx2-3066 and hNaV1.7 are shown in stick representation and labeled. Nitrogen atoms are colored in blue and oxygen atoms are colored in red. Hydrogen bonds between donor and acceptor atoms are shown by blue dash line. (C) Block of whole-cell hNaV1.7 sodium currents by application of increasing concentrations of PTx2-3066. (D) Inhibition of hNaV1.7 currents was measured as shown in C and plotted as a function concentration of PTx2-2955 or its derivatives. Fitting the Hill equation to the data yielded IC50 values (95% confidence interval) of 185.0 [152.1, 217.9] nM (n=5), 154.0 [39.9, 268.1] nM (n=3), nM, 52.6 [7.0, 98.2] nM (n=3), 73.9 [55.8, 92.0] nM (n=4), 30.8 [27.9, 33.7] nM (n=6), and 48.3 [29.5, 67.1] nM (n=4) for PTx2-2955, PTx2-3063, PTx2-3064, PTx2-3065, PTx2-3066, and PTx2-3067, respectively.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig3-figsupp1-v3.jpg)

**Figure 3—figure supplement 1.:** Computational design of ProTx-II variants. (A) Structural mapping of design restrictions categorized as disulfide positions (yellow), fixed identity positions (black), disallowed acidic identity positions (blue), and free design positions (orange). (B) Rosetta top design sequences and the consensus design sequence (represented as sequence logo) are colored under the design restriction scheme.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig3-figsupp2-v3.jpg)

**Figure 3—figure supplement 2.:** At 10 µM, PTx2-3064 blocked ~92%,~66%, and ~25% of currents conducted by hNaV1.2, hNaV1.4, and hNaV1.5, respectively. At the same concentration, PTx2-3066 blocked ~41%,~34%, and ~1% of currents conducted by hNaV1.2, hNaV1.4, and hNaV1.5, respectively. Data are represented as mean ± standard deviation derived from three individually recorded cells.

PTx2-3063 and PTx2-3064 peptides containing the same W5A and M6F mutations as PTx2-2955 inhibited hNaV1.7 currents with IC50s of 154 and 52.6 nM, respectively (Figure 3C and D and Table 1). PTx2-3065, PTx2-3066, and PTx2-3067 peptides containing the wild-type W5 and M6 residues inhibited hNaV1.7 current with IC50 values equal to 73.9, 30.8, and 48.3 nM, respectively (Figure 3D and Table 1). We further tested the selectivity of PTx2-3064 and PTx2-3066 peptides for hNaV1.7 versus other NaV channels (Figure 3—figure supplement 2). PTx2-3064 and PTx2-3066 peptides blocked hNaV1.2 current by ~92 and~41% at 10 µM, respectively. PTx2-3064 and PTx2-3066 peptides blocked hNaV1.5 current by ~25 and~1% at 10 µM, respectively. PTx2-3064 and PTx2-3066 peptides blocked hNaV1.4 current by ~66% and~34% at 10 µM, respectively (Figure 3—figure supplement 2). Notably, PTx2-3066 included W7Q, S11K, E12D, and W30L mutations compared with PTx2-2955 which ultimately benefited the potency and selectivity of our top designs (see 3rd and 4th optimization rounds below). Mutation M19L did not improve potency and selectivity and was eliminated in the following rounds of optimization. Based on these results, PTx2-3066 peptide was selected as the most potent and selective peptide from the 2nd optimization round.

#### 3rd optimization round

Building on the design of PTx2-3066, we explored other combinations of Rosetta suggested substitutions and the reportedly improved potency/selectivity substitutions. Y1Q and M19F from the design of PTx2-3067 were merged into PTx2-3066 with and without the double mutant W5A/M6F to generate new designs PTx2-3126 and PTx2-3127, respectively. In another design, PTx2-3128, we explored whether the scaffold stabilizing double mutant suggested by Rosetta, S11K/E12D, is indeed important for selectivity by introducing the potency improving substitution E12A, which was used in the previous round (Figure 4A and B).

![Figure 4.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig4-v3.jpg)

**Figure 4.:** (A) Sequence alignment of the wild-type ProTx-II with PTx2-3066 and PTx2-3127 - PTx2-3128 peptides. (B) Transmembrane (left panel) and extracellular (right panel) views of the PTx2-3127 – hNaV1.7 model. Key residues on the PTx2-3127 and hNaV1.7 are shown in stick representation and labeled. Nitrogen atoms are colored in blue and oxygen atoms are colored in red. Hydrogen bonds between donor and acceptor atoms are shown by blue dash line. (C) Block of whole-cell hNaV1.7 sodium currents by application of increasing concentrations of PTx2-3127. (D) Inhibition of hNaV1.7 currents was measured as shown in C and plotted as a function concentration of PTx2-3066 or its derivatives. Fitting the Hill equation to the data yielded the IC50 values (95% confidence interval) of 30.8 [27.9, 33.7] nM (n=6), 2.3 [1.9, 2.7] µM (n=3), 6.9 [6.7, 7.1] nM (n=3), and 5.0 [4.6, 5.4] nM (n=3) for PTx2-3066, PTx2-3126, PTx2-3127, PTx2-3128, respectively.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig4-figsupp1-v3.jpg)

**Figure 4—figure supplement 1.:** Top panel, Data denoted as the mean of individual IC50’s (in nM) derived from recordings of 3 or more cells for each peptide. Bottom panels, Exemplifying current traces before (black traces) and after saturated with 10 µM (purple traces) of PTx2-3127 and PTx2-3128 peptides.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig4-figsupp2-v3.jpg)

**Figure 4—figure supplement 2.:** (A) Plots of current-voltage relationship of normalized hNav1.7 currents measured in control cells (black, n=10) and cells exposed to 50  nM of PTx2-3127 (red, n=8). Cells were stepped in 5 mV increments from –120 mV to +70 mV from a holding potential of –120 mV for 10ms. (B) Voltage-dependent activation curves are derived from the data shown in (A). PTx2-3127 causes a statistically significant depolarized shift in steady-state activation in the depolarizing direction. For control cells, the V1/2 of activation is –28.1±0.9 mV, and the slope factor k is 5.0±0.5 mV; for PTx2-3127-treated cells, the V1/2 of activation is –17.3±3.9 mV, and the slope factor k is 2.4±0.2 mV. (C) Normalized steady-state inactivation curves measured control cells (black, n=12) and cells exposed to 50  nM PTx2-3127 (red, n=6). PTx2-3127 causes a statically significant shift in steady-state inactivation in the hyperpolarized direction. For control cells, the V1/2 of inactivation is –71.2±0.9 mV, and the slope factor k is 5.8±0.1 mV; for PTx2-3127-treated cells, the V1/2 of inactivation is –76.2±2.5 mV, and the slope factor k is 7.3±0.3 mV. Cells were stepped in 10 mV increments from –120 mV to 30 mV for 500ms followed by a test pulse to –10 mV for 30ms. All recordings were performed in a time-matched manner, and normalized conductances and currents were fit to a Boltzmann function, and are shown as means ± SEM.

The PTx2-3126 peptide containing the W5A and M6F mutations from PTx2-2955 and other mutations from PTx2-3066 inhibited hNaV1.7 currents with an IC50=2.3 µM (Figure 4D and Table 1). PTx2-3127 and PTx2-3128 containing the wild-type W5 and M6 residues and other mutations from PTx2-3066 inhibited hNaV1.7 current with IC50s equal to 6.9 and 5.0 nM, respectively (Figure 4D and Table 1). We tested the selectivity of PTx2-3127 and PTx2-3128 for hNaV1.7 versus other NaV channels (see Figure 4—figure supplement 1). PTx2-3127 inhibited other NaV channels with the following IC50 values: 17 µM (hNaV1.1), 5 µM (hNaV1.2), 20 µM (rNaV1.3), 12 µM (hNaV1.4),>137 µM (hNaV1.5), 608 nM (hNaV1.6),>150 µM (hNaV1.8), and 150 µM (hNaV1.9) (see Tables 2 and 3). The data show that PTx2-3127 is at least 1000-fold selective for hNaV1.7 versus hNaV1.1, hNaV1.3, hNaV1.4, hNaV1.5, hNaV1.8, and hNaV1.9. Notably, PTx2-3127 peptide exhibits similar effects on steady-state activation and inactivation on hNav1.7 currents (Figure 4—figure supplement 2), suggesting that it retains a similar mechanism of action as ProTx-II and other published ProTx-II derivatives (Flinspach et al., 2017; Schmalhofer et al., 2008; Smith et al., 2007; Xiao et al., 2010). However, further improvement is needed for the optimized peptide selectivity for hNaV1.7 versus hNaV1.2 and hNaV1.6. PTx2-3128 inhibited other NaV channels with the following IC50 values: 3.3 µM (hNaV1.1), 570 nM (hNaV1.2), 23 µM (rNaV1.3), 22 µM (hNaV1.4), 34 µM (hNaV1.5), 358 nM (hNaV1.6), 10 µM (hNaV1.8), and 8 µM (hNaV1.9). Notably, PTx2-3127 included M19F mutation compared with PTx2-3066 which ultimately benefited the potency and selectivity of our top designs (see 4th optimization round below). Mutation Y1Q did not improve potency and selectivity and was eliminated in the following round of optimization. Based on these results, PTx2-3127 peptide was selected as the most potent and selective peptide from the 3rd optimization round.

**Table 2.**
 Selectivity profile of PTx2-3127 and PTx2-3258 peptides for hNav1.7 versus all other human Nav channels.


<table>
  <thead>
    <tr>
      <th rowspan="2">Nav subtype</th>
      <th colspan="2">PTx2-3258</th>
      <th colspan="2">PTx2-3127</th>
    </tr>
    <tr>
      <th>IC50 (nM)</th>
      <th>Selectivity for hNav1.7 vs hNav1.x (fold)</th>
      <th>IC50 (nM)</th>
      <th>Selectivity for hNav1.7 vs hNav1.x (fold)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>hNav1.1</td>
      <td>5013</td>
      <td>1319</td>
      <td>16,970</td>
      <td>2459</td>
    </tr>
    <tr>
      <td>hNav1.2</td>
      <td>3399</td>
      <td>894</td>
      <td>5040</td>
      <td>730</td>
    </tr>
    <tr>
      <td>rNav1.3</td>
      <td>14,093</td>
      <td>3708</td>
      <td>20,040</td>
      <td>2904</td>
    </tr>
    <tr>
      <td>hNav1.4</td>
      <td>8877</td>
      <td>2336</td>
      <td>11,530</td>
      <td>1671</td>
    </tr>
    <tr>
      <td>hNav1.5</td>
      <td>38,315</td>
      <td>10,082</td>
      <td>137,090</td>
      <td>19,868</td>
    </tr>
    <tr>
      <td>hNav1.6</td>
      <td>382</td>
      <td>100</td>
      <td>608</td>
      <td>88</td>
    </tr>
    <tr>
      <td>hNav1.7</td>
      <td>3.8</td>
      <td>1</td>
      <td>6.9</td>
      <td>1</td>
    </tr>
    <tr>
      <td>hNav1.8</td>
      <td>43,079</td>
      <td>11,336</td>
      <td>&gt;150,000</td>
      <td>&gt;20,000</td>
    </tr>
    <tr>
      <td>hNav1.9</td>
      <td>59,443</td>
      <td>15,642</td>
      <td>&gt;150,000</td>
      <td>&gt;20,000</td>
    </tr>
    <tr>
      <td>hERG</td>
      <td>1861</td>
      <td>496</td>
      <td>1889</td>
      <td>272</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Comparison of selectivity profiles of PTx2-3127 and PTx2-3258 peptides for hNav1.7 versus hNav1.2, hNav1.4, hNav1.5, and hNav1.6 channels.


<table>
  <thead>
    <tr>
      <th>Rank</th>
      <th>Peptide</th>
      <th>Affinity (IC50) for hNav1.7(nM)</th>
      <th>Selectivity for hNav1.7 vs hNav1.2(fold)</th>
      <th>Selectivity for hNav1.7 vs hNav1.4(fold)</th>
      <th>Selectivity for hNav1.7 vs hNav1.5(fold)</th>
      <th>Selectivity for hNav1.7 vs hNav1.6(fold)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>PTx2-3258</td>
      <td>3.8</td>
      <td>894</td>
      <td>2336</td>
      <td>10,082</td>
      <td>100</td>
    </tr>
    <tr>
      <td>2</td>
      <td>PTx2-3127</td>
      <td>6.9</td>
      <td>730</td>
      <td>1671</td>
      <td>19,868</td>
      <td>88</td>
    </tr>
    <tr>
      <td>3</td>
      <td>PTx2-3128</td>
      <td>5.0</td>
      <td>114</td>
      <td>4,500</td>
      <td>6,800</td>
      <td>70</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Janssen’s(JNJ63955918)</td>
      <td>10</td>
      <td>160</td>
      <td>500</td>
      <td>&gt;1000</td>
      <td>100</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Wild-typeProTx-II</td>
      <td>0.3–1</td>
      <td>100–140</td>
      <td>260–380</td>
      <td>300–1000</td>
      <td>86</td>
    </tr>
  </tbody>
</table>

#### 4th optimization round

In the final optimization round, we sought to improve the design of PTx2-3127 by introducing substitution Y1H into the design PTx2-3258 (Figure 5A). Histidine appeared most frequently in the top Rosetta designs at position 1 (see Figure 3—figure supplement 1). The structural model showed a hydrogen bond formed with a backbone carbonyl atom on ProTx-II (Figure 5B) thus potentially stabilizing the ProTx-II scaffold. Building upon PTx2-3258, we replaced Methionine at position 6 by Norleucine to prevent oxidation and incorporated the change in the design of PTx2-3061. All previously tested substitutions selected by Rosetta were hydrogen bond promoting substitutions. In the design of PTx2-3259, we tested if the Q3L substitution suggested by Rosetta (see Figure 3—figure supplement 1) could create an additional stabilizing effect. We selected the third most frequently observed amino acid at this position, Leu based on an experimental design protocol with the membrane scoring function (Alford et al., 2020). Lastly, we attempted to explore non-canonical amino acids at positions 27 and 29 to examine whether the selectivity of PTx2-3258 can be improved further given that these positions are near F813 (VSD-II). This resulted in the design of PTx2-3260 with 2,4-dimethyl-phenylalanine and tert-butyl-cysteine at positions 27 and 29, respectively.

![Figure 5.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig5-v3.jpg)

**Figure 5.:** (A) Sequence alignment of the wild-type ProTx-II with PTx2-3127, PTx2-3258, PTx2-3259, PTx2-3260, and PTx2-3361 peptides. (B) Transmembrane (left panel) and extracellular (right panel) views of the PTx2-3258 – hNaV1.7 model. Key residues on the PTx2-3258 and hNaV1.7 are shown in stick representation and labeled. Nitrogen atoms are colored in blue and oxygen atoms are colored in red. Hydrogen bonds between donor and acceptor atoms are shown by blue dash line. (C) Block of whole-cell hNaV1.7 sodium currents by application of increasing concentrations of PTx2-3258 and followed by 1 mM of wild-type ProTx-II as indicated. (D) Inhibition of hNaV1.7 currents was measured as shown in C and plotted as a function concentration of PTx2-3127 or its derivatives. Fitting the Hill equation to the data yielded the IC50 values (95% confidence interval) of 6.9 [6.7, 7.1] nM (n=3), 3.8 [0.3, 7.3] nM (n=5), 41.8 [16.5, 67.1] nM (n=3), 20.8 [12.4, 29.2] nM (n=3), 8.6 [5.6, 11.6] nM (n=3), nM for PTx2-3127, PTx2-3258, PTx2-3259, PTx2-3260, and PTx2-3361, respectively.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig5-figsupp1-v3.jpg)

**Figure 5—figure supplement 1.:** Top panel, Data denoted as mean of individual IC50’s (in nM) derived from recordings of 3 or more cells for each peptide. Bottom panel, Representative current traces before (black traces) and after saturated with 10 µM (purple traces) of PTx2-3258 peptide.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig5-figsupp2-v3.jpg)

**Figure 5—figure supplement 2.:** The plots of the average area under the curve at 214 nm and 280 nm versus time for the stability of the wild-type ProTx-II (A), PTx2-3127 (B), and PTx2-3258 (C).

Functional characterization of the activity of the peptides PTx2-3258 – PTx2-3260 and PTx2-3361 on the wild-type hNaV1.7 expressed in HEK 293 cells analyzed by whole-cell voltage-clamp was performed as described in Methods. The ProTx-II variants inhibited the hNaV1.7 channel with the following IC50 values: PTx2-3258 (3.8 nM), PTx2-3259 (41.8 nM), PTx2-3260 (21.0 nM), and PTx2-3361 (9.0 nM) (see Figure 5C and D, Figure 5—figure supplement 1, and Tables 1–3). Notably, PTx2-3258 included Y1H mutation compared with PTx2-3127 which ultimately benefited its potency and selectivity.

We tested the broader selectivity of PTx2-3127 and PTx2-3258 on hERG channels. The ProTx-II variants inhibited the hERG channel with the following IC50 values: PTx2-3127 (1.9 µM) and PTx2-3258 (1.9 µM) (see Table 2). Therefore, PTx2-3127 has 272-fold and PTx2-3258 has 496-fold selectivity for hNaV1.7 versus hERG. Notably, while the wild-type ProTx-II did not inhibit KV2.1 channel at 100–300 nM (Bosmans et al., 2008; Bosmans et al., 2011; Schmalhofer et al., 2009), it inhibited Cav3 channels in the micromolar range (Bladen et al., 2014; Middleton et al., 2002). We hypothesize that our lead peptides (PTx2-3127 and PTx2-3258) might also inhibit Cav3 channels in the micromolar range and further optimization of peptide selectivity and potency will be needed.

### Stability of designed peptides in artificial cerebrospinal fluid

To access the biologically relevant stability of the wild-type ProTx-II, PTx2-3127, and PTx2-3258, peptides were incubated in artificial cerebrospinal fluid (aCSF) as described in Methods and their stability was determined by HPLC. Notably, the wild-type ProTx-II, PTx2-3127, and PTx2-3258 were found to be stable in aCSF at 37°C for more than 50 hr (Figure 5—figure supplement 2).

### Efficacy of designed peptides on mouse nociceptor DRG neurons

NaV1.7 is important for pain signaling in mice (Gingras et al., 2014; Nassar et al., 2004). As mice are valuable preclinical models for therapeutic development it is important to know whether mouse endogenous NaV1.7 is responsive to any therapeutic candidate (Beckley et al., 2021; Shiers et al., 2020). We studied the effects of PTx2-3127 on NaV currents of genetically identified mouse nociceptor sensory neurons. Mrgprd+ nonpeptidergic nociceptors were identified by fluorescence in MrgprdGFP mice (Zylka et al., 2005). MrgprdGFP DRG neurons from adult mice have significant expression of mRNA for NaV1.7, NaV1.8 and NaV1.9 with other NaV transcripts in much lower abundance (NaV1.8~NaV1.9>NaV1.7>>NaV1.6>>NaV1.1) (Zheng et al., 2019). Presence of NaV1.7 protein in DRG neurons of the MrgprdGFP mouse line used for electrophysiology was confirmed by observation of anti-NaV1.7 immunofluorescence in MrgprdGFP DRG neuron cell bodies and axonal processes (Figure 6A), consistent with prior reports of NaV1.7 localization to small, unmyelinated neurons (Black et al., 2012). Anti-NaV1.7 immunofluorescence was variable in MrgprdGFP DRG neurons with some exhibiting high and others low density of NaV1.7 protein (Figure 6A, DRG inset arrows and arrowhead, respectively).

![Figure 6.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig6-v3.jpg)

**Figure 6.:** (A) Immunofluorescence from MrgprdGFP labeled NP1 nociceptors (AB_300798, green) and NaV1.7 (AB_2877500, magenta) in a mouse L5 spinal section. Orientation of left DRG was moved during sectioning. Lower panels are zoomed in images to highlight colocalization (white) in dorsal horn nociceptor terminals, dorsal root fibers and DRG cell bodies. NP1 nociceptor DRG cell bodies show both high (arrow) and low (arrowhead) immunofluorescence for NaV1.7. Top image, dorsal horn and DRG zoom images are a z-projection of 3 confocal images spanning 10.06 µm. Zoom in image of dorsal root fibers is a z-projection of 9 airyscan images spanning 3.18 µm. Scale bar in the top image is 500 µm. Scale bars in the dorsal horn, dorsal root and DRG zoom in panels are 100, 20 and 100 µm, respectively. (B) Voltage clamp recordings of NaV currents from dissociated NP1 nociceptors showing impact of PTx2-3127 (red) and subsequent application of TTX (green). Fast-inactivating NaV component revealed by subtraction of 1 µM PTx2-3127 trace from total NaV current. Black dotted line represents 0 pA of current. (C) Left: Mean current density from 0.4 to 1ms of PTx2-3127 sensitive current and vehicle sensitive current. Middle: Mean current density from 0.4 to 1ms of TTX sensitive current after application of PTx2-3127 or vehicle. Right: Peak current density of TTX resistant current after application of PTx2-3127 or vehicle and TTX. Point colors represent the same neuron (N=4 mice). p values calculated by Students T-Test. (D) Peak time of PTx2-3127 sensitive and resistant currents as well as peak time of TTX sensitive and resistant currents. Point colors correspond to the same neurons and is consistent with points shown in C. p values calculated by Students T-Test. (E) Current clamp recording of NP1 action potentials and failures with 3 Hz stimuli in vehicle, 1 µM PTx2-3127 and 1 µM TTX. Dashed line represents 0 mV. (F) Average remaining NP1 action potentials (APs) versus frequency in PTx2-3127 (red points, n=8 neurons, N=4 mice) or in vehicle control (blue points, n=8 neurons, N=4 mice). Average remaining APs after PTx2-3127 or vehicle control in 1 µM TTX (red circle green fill and blue circle green fill, respectively). Neurons with no sensitivity to TTX were excluded from this analysis. (G) Rheobase of NP1 neurons before PTx2-3127, in PTx2-3127 and in TTX (left). Rheobase of NP1 neurons before vehicle, in vehicle and in TTX (right). p values calculated by Students T-test.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig6-figsupp1-v3.jpg)

**Figure 6—figure supplement 1.:** (A) Current clamp recording of TTX-insensitive NP1 action potentials with 3 Hz stimuli in vehicle, 1 µM PTx2-3127 and 1 µM TTX. Dashed line represents 0 mV. (B) Rheobase of TTX insensitive NP1 neurons before PTx2-3127 or vehicle and in TTX. Red points and lines indicate that neurons were in PTx2-3127 before TTX while blue points and lines indicate that neurons were in vehicle before TTX (n=7 neurons, N=3 mice). p values calculated by Students T-test.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig6-figsupp2-v3.jpg)

**Figure 6—figure supplement 2.:** (A) Average remaining NP1 action potentials (APs) versus frequency in PTx2-3127 (red points, n=5 neurons, N=2 mice) or in vehicle control (blue points, n=7 neurons, N=2 mice). Average remaining APs after PTx2-3127 or vehicle control in 1 µM TTX (red circle green fill and blue circle green fill, respectively). Neurons with no sensitivity to TTX were excluded from this analysis. (B) Example of current clamp recording of TTX-insensitive NP1 action potentials with 3 Hz stimuli in vehicle, 1 µM PTx2-3127 and 1 µM TTX. Dashed line represents 0 mV. Insensitivity to TTX was seen in 4 of 16 neurons.

Application of 1 µM PTx2-3127 to dissociated MrgprdGFP neurons under voltage clamp resulted in elimination of a fast-inactivating NaV component (Figure 6B, black trace). Blinded, interleaved experiments with either 1 µM PTx2-3127 or vehicle revealed that PTx2-3127 inhibited 48±17 pA/pF (mean ± SEM) of inward current 0.4–1.0ms after neurons were stepped from –80–0 mV, while vehicle had little effect, inhibiting 2±6 pA/pF (Figure 6C, left). Subsequent application of 1 µM TTX to the vehicle controls inhibited 37±12 pA/pF of inward current, similar to the density inhibited by PTx2-3127. Subsequent application of 1 µM TTX to PTx2-3127 had little effect, 2.1±2.8 pA/pF, showing PTx2-3127 inhibits TTX-sensitive currents in MrgprdGFP neurons (Figure 6C, middle). The density of inhibitor-resistant peak current was similar for TTX ±PTx2-3127 (Figure 6C, right). Comparison of NaV current peak times substantiated the observation that PTx2-3127-sensitive currents were faster than PTx2-3127-resistant currents (Figure 6D). In vehicle controls TTX-sensitive peak currents were faster than TTX-resistant peak currents, consistent with a prior study of MrgprdGFP neurons (Dussor et al., 2008). Overall, the similar effects of either PTx2-3127 or TTX on NaV currents suggests PTx2-3127 targets the TTX-sensitive channels of MrgprdGFP neurons. As MrgprdGFP neurons express NaV1.7, which is TTX-sensitive (Klugbauer et al., 1995), and have much lower transcript abundances of the other TTX-sensitive channels, NaV1.1, 1.2, 1.3, 1.4, 1.6 (Zheng et al., 2019), these results are consistent with PTx2-3127 inhibiting NaV1.7 channels in mouse Mrgprd+ nonpeptidergic nociceptors.

The impact of the designed peptide on action potential firing of dissociated MrgprdGFP neurons was assessed with current-clamp recording. Action potentials were recorded in vehicle, then 1 µM PTx2-3127, then 1 µM TTX. Blinded interleaved controls were conducted with vehicle replacing PTx2-3127. When stimulated with 20ms current injections at 150% of rheobase, the step current required to evoke a single action potential, at 1, 3, and 10 Hz, PTx2-3127 suppressed repetitive firing of most neurons (Figure 6E). In 27% of neurons (7 of 24), no block of action potentials was observed even in TTX (Figure 6—figure supplement 1), and these were not included in further analyses. Injecting current into DRG neurons to lower resting potential can relieve Nav1.7 inactivation and enhance the reliance of action potential generation on Nav1.7 conductance (Shields et al., 2018). However, even when currents were injected to hold MrgprdGFP neurons at less than –80 mV (after liquid junction potential correction), we saw similar results with PTx2-3127 (Figure 6—figure supplement 2), and in 25% of neurons (4 of 16) no block of action potentials was observed in TTX. In all TTX-sensitive neurons, action potentials were blocked by PTx2-3127, and subsequent application of TTX had little additional effect (Figure 6F). Rheobase was also increased by PTx2-3127 (Figure 6G). These data demonstrate that PTx2-3127 can inhibit mouse nociceptor excitability.

### Efficacy of designed peptides on human DRG neurons

We studied the effects of PTx2-3127 on the inhibition of single and multiple action potentials properties generated in adult human DRG neurons isolated from a human organ donor. The DRG neurons in culture were treated for 24 hr with 50 μM oxaliplatin to model chemotherapy-induced neuropathy (Braden et al., 2022; Chang et al., 2018; Li et al., 2018). We chose this model as it has been previously shown that pharmacological targeting of NaV1.7 reduces neuropathic pain in this model (Chang et al., 2018; Dustrude et al., 2016; Li et al., 2018). We found that rheobase increased with increasing concentrations of PTx2-3127 (Figure 7A and Table 4). We then measured action potentials induced by a train of 10–120 individual current steps delivered at 0.1, 1, 3, and 10 Hz, using current injection at 150% of baseline rheobase. The percentage of action potentials remaining was calculated as the number of action potentials in the presence of PTx2-3127 divided by the number of action potentials obtained under control conditions (without drug) at the same frequency. The number of remaining action potentials was reduced in a dose-dependent manner at 0.01, 0.1, and 1 μM PTx2-3127 at different frequencies following 24 hr of incubation with Oxaliplatin (Figure 7B and Table 4). Our data demonstrate that PTx2-3127 is effective at reducing excitability and action potentials firing in human sensory neurons in an in vitro model of chemotherapy-induced neuropathy.

![Figure 7.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig7-v3.jpg)

**Figure 7.:** (A) Efficacy of PTx2-3127 on rheobase in human DRG neurons following 24 h incubation with Oxaliplatin (50 μM). Rheobase after perfusion of the compound is normalized to baseline. (B) Efficacy of PTx2-3127 on action potentials (APs) in human DRG neurons following 24 h incubation with Oxaliplatin (50 μM). Action potential inhibition after perfusion of the compound is normalized to baseline. APs were elicited at 150% of baseline rheobase. Results are presented as mean ± SEM.

**Table 4.**
 Rheobase and number of action potentials following perfusion of PTx2-3127 following 24 h incubation with Oxaliplatin.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2">[Drug] µM</th>
      <th rowspan="2">Rheobase(pA)</th>
      <th colspan="4">Number of APs</th>
      <th>% change</th>
      <th colspan="4">Remaining AP (%)</th>
    </tr>
    <tr>
      <th>0.1 Hz</th>
      <th>1 Hz</th>
      <th>3 Hz</th>
      <th>10 Hz</th>
      <th>Rheobase</th>
      <th>0.1 Hz</th>
      <th>1 Hz</th>
      <th>3 Hz</th>
      <th>10 Hz</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Cell 1</td>
      <td>Baseline</td>
      <td>500</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>62</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <td>0.01</td>
      <td>480</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>61</td>
      <td>–4.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>98.4</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>460</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>60</td>
      <td>–8.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>96.8</td>
    </tr>
    <tr>
      <td>1</td>
      <td>640</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>59</td>
      <td>28.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>95.2</td>
    </tr>
    <tr>
      <td rowspan="4">Cell 2</td>
      <td>Baseline</td>
      <td>300</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <td>0.01</td>
      <td>280</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>47</td>
      <td>–6.7</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>39.2</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>320</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>24</td>
      <td>6.7</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>20.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>600</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td rowspan="4">Cell 3</td>
      <td>Baseline</td>
      <td>360</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>37</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <td>0.01</td>
      <td>460</td>
      <td>10</td>
      <td>120</td>
      <td>96</td>
      <td>28</td>
      <td>27.8</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>80.0</td>
      <td>75.7</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>520</td>
      <td>10</td>
      <td>53</td>
      <td>36</td>
      <td>16</td>
      <td>44.4</td>
      <td>100.0</td>
      <td>44.2</td>
      <td>30.0</td>
      <td>43.2</td>
    </tr>
    <tr>
      <td>1</td>
      <td>700</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>94.4</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td rowspan="4">Cell 4</td>
      <td>Baseline</td>
      <td>1450</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>32</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <td>0.01</td>
      <td>1550</td>
      <td>10</td>
      <td>119</td>
      <td>8</td>
      <td>1</td>
      <td>6.9</td>
      <td>100.0</td>
      <td>99.2</td>
      <td>6.7</td>
      <td>3.1</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>1650</td>
      <td>10</td>
      <td>105</td>
      <td>1</td>
      <td>1</td>
      <td>13.8</td>
      <td>100.0</td>
      <td>87.5</td>
      <td>0.8</td>
      <td>3.1</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1800</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>24.1</td>
      <td>100.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td rowspan="4">Cell 5</td>
      <td>Baseline</td>
      <td>1800</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>48</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <td>0.01</td>
      <td>2000</td>
      <td>10</td>
      <td>120</td>
      <td>105</td>
      <td>28</td>
      <td>11.1</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>87.5</td>
      <td>58.3</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>2000</td>
      <td>10</td>
      <td>120</td>
      <td>90</td>
      <td>27</td>
      <td>11.1</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>75.0</td>
      <td>56.3</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2100</td>
      <td>10</td>
      <td>120</td>
      <td>30</td>
      <td>3</td>
      <td>16.7</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>25.0</td>
      <td>6.3</td>
    </tr>
    <tr>
      <td rowspan="4">Cell 6</td>
      <td>Baseline</td>
      <td>400</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>52</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <td>0.01</td>
      <td>420</td>
      <td>10</td>
      <td>120</td>
      <td>75</td>
      <td>7</td>
      <td>5.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>62.5</td>
      <td>13.5</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>520</td>
      <td>10</td>
      <td>20</td>
      <td>0</td>
      <td>0</td>
      <td>30.0</td>
      <td>100.0</td>
      <td>16.7</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>660</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>65.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td rowspan="4">Cell 7</td>
      <td>Baseline</td>
      <td>420</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>53</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <td>0.01</td>
      <td>460</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>37</td>
      <td>9.5</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>69.8</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>540</td>
      <td>10</td>
      <td>120</td>
      <td>77</td>
      <td>24</td>
      <td>28.6</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>64.2</td>
      <td>45.3</td>
    </tr>
    <tr>
      <td>1</td>
      <td>680</td>
      <td>0</td>
      <td>0</td>
      <td>17</td>
      <td>4</td>
      <td>61.9</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>14.2</td>
      <td>7.5</td>
    </tr>
    <tr>
      <td rowspan="4">Cell 8</td>
      <td>Baseline</td>
      <td>1950</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <td>0.01</td>
      <td>1900</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>–2.6</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>2000</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>2.6</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>3000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>53.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td rowspan="4">Cell 9</td>
      <td>Baseline</td>
      <td>1250</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>57</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <td>0.01</td>
      <td>1250</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>23</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>40.4</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>1300</td>
      <td>10</td>
      <td>120</td>
      <td>93</td>
      <td>18</td>
      <td>4.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>77.5</td>
      <td>31.6</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1250</td>
      <td>10</td>
      <td>120</td>
      <td>81</td>
      <td>7</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>67.5</td>
      <td>12.3</td>
    </tr>
    <tr>
      <td rowspan="4">Cell 10</td>
      <td>Baseline</td>
      <td>3200</td>
      <td>10</td>
      <td>120</td>
      <td>120</td>
      <td>60</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <td>0.01</td>
      <td>3250</td>
      <td>10</td>
      <td>120</td>
      <td>111</td>
      <td>51</td>
      <td>1.6</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>92.5</td>
      <td>85.0</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>3250</td>
      <td>10</td>
      <td>120</td>
      <td>107</td>
      <td>40</td>
      <td>1.6</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>89.2</td>
      <td>66.7</td>
    </tr>
    <tr>
      <td>1</td>
      <td>4700</td>
      <td>10</td>
      <td>59</td>
      <td>43</td>
      <td>34</td>
      <td>46.9</td>
      <td>100.0</td>
      <td>49.2</td>
      <td>35.8</td>
      <td>56.7</td>
    </tr>
    <tr>
      <td rowspan="8"></td>
      <td rowspan="8"></td>
      <td rowspan="8"></td>
      <td rowspan="8"></td>
      <td rowspan="4" colspan="2">Average</td>
      <td>Baseline</td>
      <td>0.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <td>0.01</td>
      <td>4.9</td>
      <td>100.0</td>
      <td>99.9</td>
      <td>82.9</td>
      <td>58.3</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>13.5</td>
      <td>100.0</td>
      <td>84.8</td>
      <td>63.7</td>
      <td>46.3</td>
    </tr>
    <tr>
      <td>1</td>
      <td>49.1</td>
      <td>50.0</td>
      <td>34.9</td>
      <td>24.3</td>
      <td>17.8</td>
    </tr>
    <tr>
      <td rowspan="4" colspan="2">SEM</td>
      <td>Baseline</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>0.01</td>
      <td>3.1</td>
      <td>0.0</td>
      <td>0.1</td>
      <td>9.3</td>
      <td>10.7</td>
    </tr>
    <tr>
      <td>0.1</td>
      <td>5.1</td>
      <td>0.0</td>
      <td>9.4</td>
      <td>12.5</td>
      <td>11.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>10.3</td>
      <td>16.7</td>
      <td>15.0</td>
      <td>10.9</td>
      <td>10.2</td>
    </tr>
  </tbody>
</table>

### Efficacy of designed peptides in animal models of pain

To study the efficacy of PTx2-3127 in animal models of pain, we tested it initially in naïve female and male rats to assess the thermal nociceptive responses and monitor open field activity. Whereas mouse sensory neurons are a useful model in vitro due to their genetic tractability, rats have been proposed to provide more reliable behavioral responses in pain models (Mogil, 2009). Doses were selected referencing the in vivo data available for ProTx-II. Merck’s study found that ProTx-II had a laming effect via intrathecal administration at 2.4 µg but no effect on nociceptive assays at 0.24 µg i.t. (Schmalhofer et al., 2008). Janssen’s study reported that 2 µg of ProTx-II in 10 µL was the maximum tolerated dose in rats (Flinspach et al., 2017). Based on this information we chose a conservative dose of 1.2 and 1.6 µg in 10 µL for intrathecal administration to naïve rats. Intrathecal administration was performed via implanted cannulas which were surgically placed in the subarachnoid space of the spinal cord between L4 and L5. After recovery from surgery (~7 days) the rats were assessed for gait and mobility prior to peptide dosing.

The 1.6 vs 1.2 µg dose resulted in robust analgesia with several rats reaching the cutoff latency (30 s) for a number of hours on a 52.1°C hotplate assessed once per hour (Figure 8A and B) (Two Way Repeated Measures ANOVA, Holm-Sidak method post hoc, p<0.001 PTx2-3127 n=11 vs vehicle n=9). Importantly, this dose did not lame or significantly alter motor activity of the rats. Rats that timed out per the cutoff were immediately ambulatory after being removed from the hot plate. The same dose was administered to a group of rats with oxaliplatin induced neuropathy (Figure 8C). These rats with induced chronic pain were assessed on the 52.1°C hotplate to compare to results from naïve rats. Again the 1.6 µg i.t. dose of PTx2-3127 resulted in robust analgesia, however, with a slightly different time course of action (Two Way Repeated Measures ANOVA, Holm-Sidak method post hoc, p=0.029 PTx2-3127 n=5 vs vehicle n=4).

![Figure 8.](https://cdn.elifesciences.org/articles/81727/elife-81727-fig8-v3.jpg)

**Figure 8.:** PTx2-3127 exhibited dose dependent analgesia on a 52.1°C hotplate increasing the duration of effect as well as number reaching the latency cutoff with doses of 1.2 ug i.t. (A) to 1.6 ug i.t. (B) in naïve female and male rats. The analgesia mediated by PTx2-3127 was significant compared with vehicle controls for both doses (1.2 ug, p≤0.002) and the 1.6 ug dose several rats reached the hotplate latency cutoff (30 s to prevent injury) for several hours’ duration (1.6 ug, p<0.001 and p=0.013 at indicated time points). (C) PTx2-3127 was also effective against oxaliplatin chemotherapy induced neuropathic pain (CIPN) with responses also significant compared with vehicle controls (p<0.001) and reaching the latency cutoff. (A–C, Two Way Repeated Measures ANOVA, Holm-Sidak method post hoc, treated versus control).

## Discussion

Our study provides valuable insights into the development of natural peptide-based therapeutics to treat chronic pain. First, natural peptides, such as ProTx-II, constitute useful starting protein scaffolds for further optimization of selectivity, potency, stability, and bioavailability. Second, high-resolution structures of natural peptide – protein receptor complexes, such as the ProTx-II – hNaV1.7-NaVAb chimera (Xu et al., 2019), and available experimental data on peptide – protein receptor interactions, such as studies by Amgen, Genentech, and Janssen in the case of ProTx-II (Flinspach et al., 2017; Moyer et al., 2018; Xu et al., 2019), provide essential data for the rational design of peptide-based therapeutics. Third, computational structural biology-based protein design using Rosetta allows rational exploration of peptide substitutions in silico guided by high-resolution structures of peptide – protein receptor complexes (Bender et al., 2016; Leman et al., 2020).

The previous state-of-the-art ProTx-II based peptide optimization by Janssen identified a peptide variant (named JNJ63955018) that achieved in vitro selectivity for hNaV1.7 versus other human NaV channels ranging from 100-fold (vs hNaV1.6) to more than 1,000-fold (vs hNaV1.5) (Flinspach et al., 2017). However, the in vivo safety window for JNJ63955018 peptide was only 7–16 fold (Flinspach et al., 2017). Therefore, further improvement of in vitro selectivity for hNaV1.7 versus other human NaV channels to achieve >1000 fold is necessary to expand the in vivo safety window to at least 100-fold (Schmalhofer et al., 2008). Our structure-guided peptide optimization facilitated efficient identification of promising combinations of substitutions and tested only dozens of top candidates compared with the previous comprehensive mutagenesis efforts which synthesized and screened up to 1500 peptide variants (Flinspach et al., 2015; Flinspach et al., 2017; Neff and Wickenden, 2021). Redesign of ProTx-II peptide using Rosetta identified novel and confirmed previously reported substitutions that improved selectivity for hNaV1.7 versus other human NaV channels while preserving low nanomolar potency (see Table 5). Rosetta introduced substitutions of ProTx-II residues facing the membrane environment (Y1H), facing the protein-protein interface environment (M6norLeu), and facing the water-soluble environment (S11K and E12D). Rosetta also confirmed previously reported ProTx-II substitutions facing the membrane environment (Y1Q and W7Q, reported by Janssen Flinspach et al., 2017), facing the protein core environment (M19L, reported by Janssen Flinspach et al., 2015; Neff and Wickenden, 2021), and facing the protein-protein interface environment (K28E, reported by Amgen Moyer et al., 2018). We designed a novel and extensive hydrogen-bonding network at the ProTx-II – hNaV1.7 VSD-II interface involving R20, R22, and E28 (on ProTx-II) and D816 (on hNaV1.7 VSD-II) that contributed to improvements in the lead PTx2-3127 and PTx2-3258 peptide selectivity because Aspartate at position D816 is only present in hNaV1.7 and hNaV1.6 (see Figure 2—figure supplement 1). Our top designed peptides are highly potent, PTx2-3127 (IC50=6.9 nM) and PTx2-3258 (IC50=3.8 nM), and highly selective for hNaV1.7 versus other human NaV channels. PTx2-3127 has 730-, 1671-, and 19,868-fold selectivity for hNaV1.7 versus hNaV1.2, hNaV1.4 and hNaV1.5, respectively. PTx2-3258 has 894-, 2336-, and 10,082-fold selectivity for hNaV1.7 versus hNaV1.2, hNaV1.4, and hNaV1.5, respectively. However, the potency and selectivity of our top peptides, PTx2-3127 and PTx2-3258, are superior to Janssen’s JNJ63955918 peptide (Flinspach et al., 2017), underscoring the power of our structure-guided optimization approach.

**Table 5.**
 Summary of four rounds of ProTx-II peptide optimization.ProTx-II mutations that resulted in the most potent and selective peptide are highlighted in green. ProTx-II mutations that did not result in the most potent and selective peptide are highlighted in yellow. X at residue #22 in PTx2-2955 represents norArg.


<table>
  <thead>
    <tr>
      <th>Residue #</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
      <th>16</th>
      <th>17</th>
      <th>18</th>
      <th>19</th>
      <th>20</th>
      <th>21</th>
      <th>22</th>
      <th>23</th>
      <th>24</th>
      <th>25</th>
      <th>26</th>
      <th>27</th>
      <th>28</th>
      <th>29</th>
      <th>30</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>WT PTx2</td>
      <td>Y</td>
      <td>C</td>
      <td>Q</td>
      <td>K</td>
      <td>W</td>
      <td>M</td>
      <td>W</td>
      <td>T</td>
      <td>C</td>
      <td>D</td>
      <td>S</td>
      <td>E</td>
      <td>R</td>
      <td>K</td>
      <td>C</td>
      <td>C</td>
      <td>E</td>
      <td>G</td>
      <td>M</td>
      <td>V</td>
      <td>C</td>
      <td>R</td>
      <td>L</td>
      <td>W</td>
      <td>C</td>
      <td>K</td>
      <td>K</td>
      <td>K</td>
      <td>L</td>
      <td>W</td>
    </tr>
    <tr>
      <td>PTx2-2955</td>
      <td>Y</td>
      <td>C</td>
      <td>Q</td>
      <td>K</td>
      <td>A</td>
      <td>F</td>
      <td>W</td>
      <td>T</td>
      <td>C</td>
      <td>D</td>
      <td>S</td>
      <td>E</td>
      <td>R</td>
      <td>K</td>
      <td>C</td>
      <td>C</td>
      <td>E</td>
      <td>G</td>
      <td>L</td>
      <td>R</td>
      <td>C</td>
      <td>X</td>
      <td>L</td>
      <td>W</td>
      <td>C</td>
      <td>R</td>
      <td>K</td>
      <td>E</td>
      <td>L</td>
      <td>W</td>
    </tr>
    <tr>
      <td>PTx2-3066</td>
      <td>Y</td>
      <td>C</td>
      <td>Q</td>
      <td>K</td>
      <td>W</td>
      <td>M</td>
      <td>Q</td>
      <td>T</td>
      <td>C</td>
      <td>D</td>
      <td>K</td>
      <td>D</td>
      <td>R</td>
      <td>K</td>
      <td>C</td>
      <td>C</td>
      <td>E</td>
      <td>G</td>
      <td>L</td>
      <td>R</td>
      <td>C</td>
      <td>R</td>
      <td>L</td>
      <td>W</td>
      <td>C</td>
      <td>R</td>
      <td>K</td>
      <td>E</td>
      <td>L</td>
      <td>L</td>
    </tr>
    <tr>
      <td>PTx2-3127</td>
      <td>Q</td>
      <td>C</td>
      <td>Q</td>
      <td>K</td>
      <td>W</td>
      <td>M</td>
      <td>Q</td>
      <td>T</td>
      <td>C</td>
      <td>D</td>
      <td>K</td>
      <td>D</td>
      <td>R</td>
      <td>K</td>
      <td>C</td>
      <td>C</td>
      <td>E</td>
      <td>G</td>
      <td>F</td>
      <td>R</td>
      <td>C</td>
      <td>R</td>
      <td>L</td>
      <td>W</td>
      <td>C</td>
      <td>R</td>
      <td>K</td>
      <td>E</td>
      <td>L</td>
      <td>L</td>
    </tr>
    <tr>
      <td>PTx2-3258</td>
      <td>H</td>
      <td>C</td>
      <td>Q</td>
      <td>K</td>
      <td>W</td>
      <td>M</td>
      <td>Q</td>
      <td>T</td>
      <td>C</td>
      <td>D</td>
      <td>K</td>
      <td>D</td>
      <td>R</td>
      <td>K</td>
      <td>C</td>
      <td>C</td>
      <td>E</td>
      <td>G</td>
      <td>F</td>
      <td>R</td>
      <td>C</td>
      <td>R</td>
      <td>L</td>
      <td>W</td>
      <td>C</td>
      <td>R</td>
      <td>K</td>
      <td>E</td>
      <td>L</td>
      <td>L</td>
    </tr>
  </tbody>
</table>

Endogenous NaV channels do not always share the same pharmacology as recombinantly expressed channels, which could result from differences due to endogenous auxiliary subunits, interacting partners, or posttranslational modifications in native cells absent in heterologous systems (Zhang et al., 2013). Here, we demonstrate the efficacy of PTx2-3127 in targeting endogenous NaV1.7 channels from both mice (Figure 6) and human neurons (Figure 7). Experiments in genetically identified mouse nonpeptidergic nociceptors show that PTx2-3127 inhibits the endogenous fast inward conductance consistent with NaV1.7. PTx2-3127 also inhibits excitability and action potential firing in these neurons. These results suggest that mice have value as a preclinical model for developing PTx2 derivatives as pain therapeutics. Furthermore, in human DRG neurons treated with the chemotherapeutic oxaliplatin, PTx2-3127 also reduced neuronal excitability. Oxaliplatin is a chemotherapeutic agent commonly used to treat colorectal cancers (Graham et al., 2004) and is known to increase sensory neuron excitability to induce both neuropathic mechanical and cold allodynia. However, there is a debate regarding the mechanisms and NaV subtypes through which this occurs. We provide evidence that (1) PTx2-3127 can reduce action potential discharges in an in vitro model of oxaliplatin-induced neuropathy, and (2) NaV1.7 contributes to human neuronal hyperexcitability in this model. This important result is consistent with PTx2-3127 retaining activity against endogenous NaV channels. We note that 1 µM PTx2-3127 partially inhibits hNaV1.6 in HEK cells, and other hNaVs to a lesser extent (Table 1), raising the possibility of off-target Navs contributing to neuronal modulation by 1 µM PTx2-3127. Overall, these results suggest that engineered PTx2 variants have potential to suppress human nociception in the clinic. The dual efficacy of PTx2-3127 in murine and human DRG neurons also demonstrates the value of combining the genetic power of mouse models with the translational relevance of in vitro experiments on human DRG neurons to validate future PTx2 variants during the preclinical optimization (Shiers et al., 2020).

PTx2-3127 demonstrated acute analgesia in keeping with a previous report of NaV channel blockade with ProTx-II and other targeted NaV1.7 blocking approaches (Flinspach et al., 2017). Intrathecal administration of the peptide to otherwise naïve rats blocked pain sensitivity in the suprathreshold hotplate assay over a duration of several hours. After this hotplate assay rats were placed into an open field apparatus where the animals were ambulatory and explorative despite reaching a latency cutoff on the hotplate. The open field was not quantified in this setting because of the supra-stimulation of the hotplate assay directly preceding it. However, our observations correlate with published reports that NaV channel blockade in preclinical models parallels the human genetic mutant phenotype of pain insensitivity without motor function decrements (Gingras et al., 2014). Importantly PTx2-3127 was also effective against CIPN-induced neuropathy with intrathecal administration (Figure 8). The chronic pain of CIPN is often difficult to treat, but using the 52.1°C hotplate we demonstrated potent analgesia using PTx2-3127 in this model. It will be essential to characterize the expression levels and contribution of NaV1.7 versus NaV1.8 to the CIPN pain, as well as the pain modality (i.e. heat/cold, mechanical or chemical stimuli) where this highly selective NaV1.7 blocking peptide is the most potent, however, in this initial investigation, intrathecal PTx2-3127 administration resulted in significant analgesia.

In summary, our interdisciplinary approach demonstrates the power of structure-guided peptide design and represents a major step toward the efficient development of potent and selective natural peptide-based inhibitors of human NaV1.7 channels as prototypes of analgesic drug candidates for treating chronic pain. Additional work will be necessary to address the following limitations of our study and translate NaV1.7 targeted peptides to the clinic. First, a significant improvement in the selectivity of our lead peptides for hNaV1.7 versus hNaV1.6 is needed to avoid affecting the function of motor neurons within a therapeutic concentration range (Schmalhofer et al., 2008). Second, optimization of the duration of peptide efficacy in vivo beyond several hours will be necessary to prolong the therapeutic effect in the clinic, either through increasing stability or continuous administration via an intrathecal pump. Third, the development of peptide formulations will be useful to potentially enable peptide bioavailability through subcutaneous, intranasal or oral administration routes as are already in clinical use for GLP-1 (Glucagon-Like Peptide 1) receptor agonists (Drucker, 2020).

## Methods

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
      <td>Cell line(Homo sapiens)</td>
      <td>HEK 293</td>
      <td>ATCC</td>
      <td>Cat #: CRL-1573</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Rosetta</td>
      <td>Rosetta https://doi.org/10.1038/s41592-020-0848-2https://www.rosettacommons.org/</td>
      <td>Version 3.12</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>IgorPro</td>
      <td>IgorPro https://www.wavemetrics.com/</td>
      <td>Version 8</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSF Chimera</td>
      <td>UCSF Chimera https://www.cgl.ucsf.edu/chimera/</td>
      <td>Version 1.16</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CHARMM-GUI</td>
      <td>CHARMM-GUI https://doi.org/10.1002/jcc.20945http://www.charmm-gui.org</td>
      <td>Version 3.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CHARMM36</td>
      <td>CHARMM36https://doi.org/10.1002/jcc.23354http://mackerell.umaryland.edu/charmm_ff.shtml</td>
      <td>VersionJuly 2019</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Pulse-PulseFit</td>
      <td>Pulse-PulseFit (HEKA Electronik GmbH, Germany) http://www.heka.com/index.html</td>
      <td>Version 8.8</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Origin</td>
      <td>https://www.originlab.com/</td>
      <td>Version 9.0</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Design of ProTx-II based peptides targeting hNav1.7

#### Molecular dynamics simulation of ProTx-II - NavAb/Nav1.7 chimera complex

We ran a molecular dynamics simulation of the cryo-EM structure of NavAb/Nav1.7 in a complex with ProTx-II in a deactivated state (PDB ID: 6N4R) (Xu et al., 2019) to obtain a closer look at the interaction of ProTx-II with lipid membrane at the residue level. CHARMM-GUI (Jo et al., 2008) was used to embed the structure in a lipid bilayer of POPC with explicit TIP3P water molecules at a concentration of 150 mM NaCl. The system contained approximately 90,000 atoms and was parameterized with the CHARMM36 forcefield (Huang and MacKerell, 2013). Neutral pH was used to assign the protonation state as default, and the C-terminal of ProTx-II is in the amidated form. The simulation was run on our local GPU cluster using NAMD version 2.12 (Jiang et al., 2011). After 10,000 steps of steepest descent minimization, 1 fs timestep equilibrations were started with harmonic restraints initially applied to protein-heavy atoms and lipid tail dihedral angles as suggested by CHARMM-GUI (Jo et al., 2008). These restraints were gradually released over 2 ns. Harmonic restraints (0.1 kcal/mol/Å2) were applied only to protein backbone heavy atoms. The systems were equilibrated further for 20 ns using 2 fs timestep with all bonds to hydrogen atoms constrained by the SHAKE algorithm (Ryckaert et al., 1977). The equilibrations were performed in NPT ensemble with semi-isotropic pressure coupling to maintain the correct area per lipid, and a constant temperature of 303.15 K. Particle Mesh Ewald (PME) method was used to compute electrostatic interactions. Non-bonded pair lists were updated every 10 steps with a list cutoff distance of 16 Å and a real space cutoff of 12 Å with energy switching starting at 10 Å. The production run was conducted for 100 ns without applied protein backbone restraints.

We analyzed the 100 ns simulation for interactions of ProTx-II residues with the surrounding environment, categorized into different groups: lipid head, lipid tail, water and VSDII (hNav1.7/NavAb chimera structure (PDB ID: 6N4R) Xu et al., 2019). Fractional contact is defined as the frequency of forming contact (3.5 Å as a cutoff) of heavy atoms belonging to the associated groups normalized over the course of simulation and across interacting chains, A-E, B-F, C-G, D-H of the structure.

#### Computational design of ProTx-II variants

First, the cryo-EM structure of ProTx-II in complex with hNav1.7/NavAb in a deactivated state (PDB ID: 6N4R) was further refined in Rosetta (Leman et al., 2020) using Rosetta cryo-EM refinement protocol (Dustrude et al., 2016) (see the Methods section below entitled 'Rosetta Scripts for refinement of ProTx-II - hNav1.7/NavAb complex'). We generated 1000 refined models and extracted the top 10 scoring models for visual inspection. We carefully examined how well ProTx-II fits into the electron density across multiple interacting chains A-E, B-F, C-G, and D-H of the top models and eventually selected chain A-E for the subsequent modeling.

Rosetta FastDesign (Maguire et al., 2021) was used to introduce ProTx-II substitutions and design new peptide variants. A small deviation of backbone conformation is inherently sampled in FastDesign by ramping cycles of reduced repulsive forces. We seek to sample higher degrees of backbone flexibility during the design process by further incorporating Rosetta Small mover and Roll mover. Small mover performs small random changes in the backbone torsional space while Roll mover invokes small rigid body perturbation between ProTx-II and VSD-II. Both movers were implemented in Rosetta XML scripts prior to the FastDesign mover (see XML scripts in the Methods section below entitled 'Rosetta Scripts for refinement of ProTx-II - hNav1.7/NavAb complex').

FastDesign was used in conjunction with sequence profile constraints to control amino acid identity substitutions. In the computational design step (round 2), fixed identity was applied to positions that reflect empirical knowledge such as R20, R22, E28 for preserving the hydrogen bond network with D816 (VSD-II) and W5, M6, W24, R26, K27, L29 for forming important interactions with the channel as observed from the modeling results of prior designs. On top of that, we disallowed acidic residues for positions that have significant interactions with lipid heads or lipid tails observed from the fractional contacts derived from the MD simulation of the ProTx-II – hNav1.7/NavAb chimera. Other positions, except disulfides, were allowed to freely mutate. However, we used Rosetta FavorSequenceProfile mover to slightly bias new substitutions toward native residues on ProTx-II because of the lack of secondary structure elements for the majority of ProTx-II fold in combination with a higher degree of backbone flexibility could result in highly diverse set of amino acid substitutions with FastDesign. We generated 1000 designs and extracted the 100 top designs by total score followed by selecting the top 20 designs by Rosetta DDG. The consensus designed sequence was constructed from the top 20 designs using sequence logo presentation (see Figure 3—figure supplement 1) and analyzed in combination with available experimental data during each optimization round as described in the main text.

### Peptide synthesis and folding

The ProTx-II variants were produced synthetically using Fmoc automated solid-phase synthesis performed on Liberty Blue peptide synthesizer from CEM Inc using a microwave-assisted synthesis strategy employing diisopropyl carbodiimide and Oxyma for the activation chemistry. Pre-loaded ChemMatrix (Sigma Aldrich) Wang resins were used to produce ProTx-II variants with C-terminal acids. Acidolytic cleavage and deprotection of the completed peptide resins was performed with 9.5 ml trifluoroacetic acid (TFA), 0.5 ml H20, 0.5 ml Anisole, 0.5 ml thioanisole, 0.25 ml of DODT (3,6-dioxa-1,8-octanedithiol), 0.25 ml triisopropyl silane per gram of resin for 2 h at room temperature. Cleaved peptides were precipitated with 5-fold excess of diethyl ether added directly to the pre-filtered cleavage solution, isolated, and re-solubilized in TFA. Linear peptides were purified by preparative HPLC using a Phenomenex Luna C18(2), 100 Å pore size, 10 μ particle size, 250 mm x 21.2 mm column and a 15–48% linear gradient of acetonitrile with 0.05% TFA over 40 min. Molecular weights were confirmed by LC/MS and fractions were pooled for folding. Purified linear fractions were added directly to 20 mM Tris, 2 M Urea, 1:2 oxidized/reduced glutathione, and pH was adjusted to 7.8–8.0 using acetic acid. Final peptide concentration was approximately 0.1–0.2 mg/ml. Solutions were stirred for 24–48 h at room temperature. Folded peptides were purified using a Phenomenex Luna C18(2), 100 Å pore size, 10 μ particle size, 250 mm x 21.2 mm column with a 15–48% linear gradient of acetonitrile with 0.05% TFA over 40 min. Main peak fractions were analyzed by HPLC and LC/MS. Peptide fractions with a purity >95% were pooled, flash-frozen and subsequently lyophilized. Peptide content for each product was determined by absorbance at 280 nm using the calculated extinction coefficient. Percent purity was determined by HPLC using a Phenomenex Luna C18(2) analytical column, 250 mm x 4.6 mm, 100 Å pore size, 5 μ particle size. Peptide mass and oxidation were confirmed by LC/MS using a Waters 2965 separations module coupled to a Waters Micromass ZQ electrospray mass spectrometer.

### Testing of designed peptides potency and selectivity using electrophysiological assays on recombinant channel cell lines

HEK-293 cells stably expressing human NaV1.1, NaV1.4, NaV1.5, NaV1.6, and NaV1.7 were obtained from Dr. Chris Lossin. Rat NaV1.3 expressing HEK-293 cells were from Dr. Stephen Waxman (Yale University, New Haven, CT). These cell lines were cultured in complete DMEM supplemented with 10% FBS, 1% penicillin/streptomycin, and G418. The human NaV1.8 channel (co-expressing with human NaVβ1 and NaVβ2 subunits) and the Nav1.9 channel (co-expressing with human Trkb, NaVβ1, and NaVβ2 subunits) were obtained from Dr. Neil Castle (Icagen, Durham, NC). hNaV1.8 cells cultured with G418 (0.4 mg/mL) and puromycin (0.5 ng/mL) and hNaV1.9 cells were cultured with G418 (0.4 mg/mL), puromycin (0.5 ng/mL), and zeocin (0.05 mg/mL). Human NaV1.2 were expressed transiently by transfection of the hNaV1.2 cDNA (from Dr. Alan L. Goldin, UC Irvine, CA) into HEK-293 cells.

Whole-cell patch-clamp experiments on recombinant channels were conducted manually at room temperature (22–24°C) using an EPC-10 amplifier (HEKA Electronik, Lambrecht/Pfalz, Germany). Cells were trypsinized and plated onto poly-l-lysine–coated coverslips. All recordings were done in normal Ringer external bath solution containing (in mM) 160 NaCl, 4.5 KCl, 2 CaCl2, 1 MgCl2, 10 HEPES (pH 7.4 and 305 mOsm) as. Patch pipettes were pulled from soda lime glass (micro-hematocrit tubes, Kimble Chase, Rochester, NY) and had resistances of 2–3 MΩ when filled with CsF-based internal solution containing (in mM) 10 NaF, 110 CsF, 20 CsCl, 10 HEPES, 2 EGTA, (pH 7.4, 310 mOsm). Data acquisition and analysis were performed with Pulse-PulseFit (HEKA Electronik GmbH, Germany), IgorPro (WaveMetrics, Portland, OR), and Origin 9.0 software (OriginLab Corporation, Northampton, MA). Cells were held at −90 mV and voltage stepped to –120 mV for 200ms before depolarizing to –10 mV for 50 ms to elicit inward currents. Control test currents were monitored for 5–10 min to ensure that the amplitude and kinetics of the response were stable. Series resistance was compensated to 80–90% and linear leak currents and capacitance artefacts were corrected using a P/4 subtraction method. Pulse interval was 0.1 Hz and peptides were applied to individual cells using a glass transfer pipette directly into the recording bath. For measuring inhibition, currents were allowed to saturate with repeated pulsing before addition of subsequent doses. IC50 values were derived from measurements performed on individual cells that were tested with at least three or more concentrations of each peptide. Concentration response curves were fitted with the Hill equation and IC50s are reported with 95% confidence intervals.

### Testing of designed peptides stability in artificial cerebrospinal fluid

Stability In Artificial Cerebrospinal Fluid (aCSF): The stability of the wild-type ProTx-II, PTx2-3127, and PTx2-3258 was conducted in artificial Cerebrospinal Fluid (aCSF). The aCSF was purchased from Tocris Biosciences (Catalog # 3525) and had the following ionic composition (in mM): Na+ 150; K+ 3.0; Ca2+1.4; Mg2+ 0.8; P 1.0; Cl- 155. The wild-type ProTx-II, PTx2-3127, and PTx2-3258 were dissolved in DPBS at 200 μM (1 mg of respective peptides in 1.305 mL, 1.315 mL, and 1.315 mL of DPBS, respectively). 500 μL of dissolved peptide in DPBS and 1.500 mL of aCSF were mixed to get 50 μM peptide solution in aCSF. The samples were incubated at 37°C and aliquots of 100 μL were removed at 0, 1, 2, 4, 8, 12, 24, and 120 hr, respectively. The aliquots were immediately flash frozen and stored at –80°C until further analysis. Peptides dissolved in aCSF were analyzed on a Hewlett Packard 1100 series HPLC system and monitored at 214 nm and 280 nm. The stability at various time points was determined by calculating the average Area under the curve at 214 nm and 280 nm for 2 injections of 20 μL using ChemStation Software. The peptides were run on a BioBasic C18 column (150X4.8 mm, ThermoFisher). The mobile phases were 0.1% Trifluoroacetic Acid in water (mobile phase A) and 100% Acetonitrile (mobile phase B).

### Testing of designed peptides efficacy on mouse sensory neurons

#### Mice

This study was approved by the UC Davis Institutional Animal Care and Use Committee and conforms to guidelines established by the NIH. Mice were maintained on a 12 hr light/dark cycle, and food and water were provided ad libitum. The MrgprdGFPmouse line was a generous gift from David Ginty (Harvard University, Boston MA) (MGI: 3521853).

#### Preparation of DRG sections

This study was approved by the UC Davis Institutional Animal Care and Use Committee and conforms to guidelines established by the NIH. 20-week-old MrgprdGFP mice was briefly anesthetized with 3–5% isoflurane and then decapitated. The spinal column was dissected, and excess muscle tissue removed. The spinal column was then bisected in the middle of the L1 vertebrae identified by the 13th rib and drop fixed for 1 hr in ice cold 4% paraformaldehyde in 0.1 M phosphate buffer (PB) pH adjusted to 7.4. The spine was washed 3× for 10 min each in PB and cryoprotected at 4°C in 30% sucrose diluted in PB for 24 hr. The spine was cut into sections containing two vertebra per sample which were frozen in Optimal Cutting Temperature (OCT) compound (Fisher Cat#4585) and stored at –80°C until sectioning. Vertebrae position relative to the 13th rib was recorded for each frozen sample to determine the specific vertebrae position in the spinal cord. Samples were cut into 30 μm sections on a freezing stage sliding microtome and were collected on Colorfrost Plus microscope slides (Fisher Scientific Cat#12-550-19). Slides were stored at –20°C or immediately used for multiplex immunofluorescence labeling.

#### Multiplex immunofluorescence labeling

A hydrophobic barrier was drawn around tissue sections mounted on slides as described above using a hydrophobic barrier pen (Scientific Device Cat#9804–02). Sections were incubated in 4% milk in PB containing 0.2% Triton X-100 (vehicle) for 1 hr and then incubated in vehicle containing 0.1 mg/mL IgG F(ab) polyclonal IgG antibody (Abcam cat# ab6668) for 1 hr. Sections were washed 3× for 5 min each in vehicle and then incubated in vehicle containing primary Abs. (Supplemental Table Abs) for 1 hr. Sections were washed 3× for 5 min each in vehicle and then incubated in vehicle containing mouse IgG-subclass-specific goat secondary Abs (Table Abs) conjugated to Alexa Fluors (Thermo Fisher). Sections were washed 3× for 5 min each in PB and mounted with Prolong Gold (Thermo Fisher) and Deckglaser cover glass (Cat#NC1776158). All incubations and washes were done at room temperature with gentle rocking.

#### Immunofluorescence imaging

Images were acquired with an inverted scanning imaging system (Zeiss LSM 880, 410900-247-075) run by ZEN black v2.1. Laser lines were 488 nm, 633 nm. Low-magnification images were acquired in confocal mode with a 0.8 NA 20 x objective (Zeiss 420650–9901) and reconstructed as a tiled mosaic using ImageJ. High-magnification images were acquired in airy disk imaging mode with a 1.4 NA 63 x oil objective (Zeiss 420782-9900-799). Linear adjustments to contrast and brightness and average fluorescence intensity z-projections were performed using ImageJ software.

#### Neuron cell culture

Cervical, thoracic and lumbar DRGs were harvested from 4- to 6-week-old MrprD-GFP mice and transferred to Hank’s buffered saline solution (HBSS) (Invitrogen). Ganglia were treated with collagenase (2 mg/ml; Type P, Sigma-Aldrich) in HBSS for 15 min at 37°C followed by 0.05% Trypsin-EDTA (Gibco) for 2.5 min with gentle rotation. Trypsin was neutralized with culture media (MEM, with l-glutamine, Phenol Red, without sodium pyruvate) supplemented with 10% horse serum (heat-inactivated; Gibco), 10 U/ml penicillin, 10 μg/ml streptomycin, MEM vitamin solution (Gibco), and B-27 supplement (Gibco). Serum-containing media was decanted and cells were triturated using a fire-polished Pasteur pipette in MEM culture media containing the supplements listed above. Cells were plated on laminin-treated (0.05 mg/ml, Sigma-Aldrich) 5 mm Deckglaser coverslips, which had previously been washed in 70% ethanol and UV-sterilized. Cells were then incubated at 37°C in 5% CO2. Cells were used for electrophysiological experiments 24–38 hr after plating.

#### Voltage clamp of endogenous neuronal sodium channels

Voltage clamp was achieved with a dPatch amplifier (Sutter Instruments) run by Sutterpatch (Sutter Instruments). Solutions for voltage-clamp recordings: internal (in mM) 15 NaCl, 100 CsCl, 25 CsF, 1 EGTA and 10 HEPES adjusted to pH 7.3 with CsOH, 297 mOsm. Seals and whole-cell configuration were obtained in an external patching solution containing the following (in mM) 145 NaCl, 3.5 KCl, 1.5 CaCl2, 1 MgCl2, 10 HEPES, 10 Glucose adjusted to pH 7.4 with NaOH, 322 mOsm. For voltage-clamp neuronal recordings, the external solution contained (in mM) 44 NaCl, 106 TEA-Cl, 1.5 CaCl2, 1 MgCl2, 0.03 CdCl2 10 HEPES, 10 glucose, pH adjusted to 7.4 with TEA-OH, 315 mOsm. The calculated liquid junction potential for the internal and external recording solutions was 5.82 mV and not accounted for. Osmolality is measured with a vapor pressure osmometer (Wescor, 5520). For voltage-clamp recordings, neurons plated on the cover glass as described in the Neuron Cell Culture section were placed in a recording chamber (Warner Cat#64–0381) and were rinsed with an external patching solution using a gravity-driven perfusion system. Neurons from MrgprdGFP mice showing intracellular GFP were then selected for patching. After the whole-cell voltage clamp was established the external patching solution was exchanged with the external recording solution using a gravity-driven perfusion system. PTx2-3127, vehicle control (external recording solution) and TTX were kept on ice and diluted in room temperature (20–22°C) external recording solution just prior to application to neurons and manually added at a rate of approximately 1 mL/min. Experimenter was blinded to the identity of PTx2-3127 versus vehicle control solutions during recordings. PTx2-3127, vehicle control and TTX were applied to neurons using separate perfusion lines to prevent contamination. After each neuron, perfusion lines were cleared with 1 mL of 70% ethanol followed by 1 mL of milli Q water and were then filled with an external recording solution. Thin-wall borosilicate glass recording pipettes (BF150-110-10, Sutter) were pulled with blunt tips, coated with silicone elastomer (Sylgard 184, Dow Corning), heat cured, and tip fire-polished to resistances less than 3 MΩ. Series resistance of 3–8 MΩ was estimated from the whole-cell parameters circuit. Series resistance compensation between 37 and 77% was used to constrain voltage error to less than 15 mV, lag was 6 µs. Cell capacitances were 13–34 pF. Capacitance and Ohmic leak were subtracted using a P/4 protocol. Output was low-pass filtered at 10 kHz using the amplifier’s built-in Bessel and digitized at 50 kHz. The average current in the initial 0.14 s at holding potential prior to the voltage step was used to zero-subtract each recording. The mean current was the current amplitude between 0.4–1ms into the 0 mV step. Peak current amplitude was the peak current amplitude between 0.4 and 8 ms into the 0 mV step. Experiments were performed on neurons with membrane resistance greater than 1 GΩ assessed prior to running voltage clamp or current clamp protocols while neurons were held at a membrane potential of –80 mV. Data with predicted voltage error, Verror ≥15 mV were excluded from the analysis. Verror was tabulated using estimated series resistance post compensation and peak NaV current.

#### Current clamp

Solutions for current clamp recordings: internal (in mM) 120 K-methylsulfonate, 10 KCl, 10 NaCl, 5 EGTA, 0.5 CaCl2, 10 HEPES, 2.5 MgATP, and adjusted to pH 7.2, 289 mOsm. External solution (in mM) 145 NaCl, 5 KCl, 2 CaCl2, 2 MgCl2, 10 HEPES, 10 Glucose adjusted to pH 7.3 with NaOH, 308 mOsm. The calculated liquid junction potential for these solutions was 9.7 mV which was not accounted for unless noted. Thin-wall borosilicate glass recording pipettes (BF150-110-10, Sutter) were pulled with blunt tips and tip fire-polished to resistances less than 3 MΩ. For current-clamp recordings, neurons plated on the cover glass as described in the Neuron Cell Culture section were placed in a recording chamber (Warner Cat#64–0381) and were rinsed with external solution using a gravity-driven perfusion system. Neurons from MrgprdGFP mice showing intracellular GFP were then selected for patching. The same protocol for application of PTx2-3127, vehicle control (external solution) and TTX described in the Voltage Clamp section was followed. In current clamp experiments data were excluded if the resting membrane potential of a neuron rose above –40 mV. After adjusting for the predicted liquid junction potential offset, the resting membrane potential of neurons in Figure 6 ranged from –57 to –78 mV and the resting membrane potential of TTX-insensitive neurons in Figure 6—figure supplement 1 ranged from –54 to –70 mV.

#### Experimental design and statistical treatment

Independent replicates (n) are individual neurons from multiple mice, details in figure legends. Statistical tests were conducted using Igor 8 (Wavemetrics Inc), details in figure legends.

### Testing of designed peptides efficacy on human sensory neurons

All human tissues that were used for the study were obtained by legal consent from organ donors in the US. AnaBios Corporation’s procurement network includes only US based Organ Procurement Organizations and Hospitals. Policies for donor screening and consent are the ones established by the United Network for Organ Sharing (UNOS). Organizations supplying human tissues to AnaBios follow the standards and procedures established by the US Centers for Disease Control (CDC) and are inspected biannually by the DHHS. Distribution of donor medical information is in compliance with HIPAA regulations to protect donor’s privacy. All transfers of donor tissue to AnaBios are fully traceable and periodically reviewed by US Federal authorities. AnaBios generally obtains donor organs/tissues from adults aged 18–60 years old. Donor DRGs from males and females were harvested using AnaBios’ proprietary surgical techniques and tools and were shipped to AnaBios via dedicated couriers. The DRGs were then further dissected in cold proprietary neuroplegic solution to remove all connective tissue and fat. The ganglia were enzymatically digested, and the isolated neurons put in culture in DMEM F-12 (Gemini Bio-Products CAT#: 900–955. Lot# M96R00J) supplemented with Glutamine 2 mM, Horse Serum 10% (Invitrogen #16050–130), hNGF (25 ng/ml) (Cell Signaling Technology #5221LF), GDNF (25 ng/ml) (ProSpec Protein Specialist #CYT-305) and Penicillin/Streptomycin (Thermo Fischer Scientific #15140–122).

External Current Clamp solution included: 145 mM NaCl, 3 mM KCl, 1 mM MgCl2, 2 mM CaCl2, 10 mM dextrose, 10 mM HEPES, pH = 7.4 (with NaOH), 300±5 mOsm. Internal Current Clamp solution included: 110 mM K+ gluconate, 20 mM KCl, 10 mM EGTA, 8 mM NaCl, 4 mM Mg-ATP, 10 mM HEPES, pH = 7.3 (with KOH), 280±5 mOsm. All of our compounds come from Sigma-Aldrich. PTx2-3127 was stored in 10 mM formulation in DMSO at –20°C. Oxaliplatin was stored in 50 mM formulation in DMSO at 4°C.

DRG recordings were obtained from human DRG in culture (2–7 days). Human DRG neurons were incubated with Oxaliplatin (50 µM) at 37 °C for 24 hr. Whole-cell patch-clamp recordings were conducted under current-clamp mode at room temperature (~23°C) using HEKA EPC-10 amplifier. Data were acquired on a Windows-based computer using the PatchMaster program. Pipettes (1.5–3.0 MΩ) (Warner Instruments #64–0792) were fabricated from 1.5 mm borosilicate capillary glass using a Sutter P-97 puller. Cells on Corning glass coverslips (Thomas Scientific #354086) were transferred to a RC-26GLP recording chamber (Warner Instruments #64–0236) containing 0.5 ml standard external solution. Extracellular solution exchange was performed with rapid exchange perfusion system (flow rate 0.5–1 ml/min) (Warner Instruments #64–0186). Cells for recordings were selected based on smoothness of the membrane. Cells were held at a resting membrane potential. Signals were filtered at 3 kHz, sampled at 10 kHz. Once whole-cell access was obtained the cell was allowed an equilibration time of at least 5 min. Once the cell under recording stabilized, rheobase of single action potentials were assessed. Action potentials were induced by a train of 10 individual current steps 20ms in. duration, delivered at 0.1 Hz and 120 individual current steps delivered at 1, 3, and 10 Hz, using current injection at 150% of rheobase of baseline. Test compound concentrations were washed in for 5 min and step 6 and 7 were repeated for each concentration. Exclusion criteria: series resistance >15 MΩ; unstable recording configuration (15% change of rheobase or access resistance within the same concentration); time frame of drug exposure not respected.

The percentage of action potentials remaining was calculated as the number of action potentials divided by the number of action potentials obtained under control condition at the same frequency. One-way ANOVA (SigmaPlot v14) with Tukey, Bonferroni and Dunnett post-hoc test was used to determine the significance of difference between treatment and control (as specified in the figure and table legends).

### Testing of designed peptides efficacy in animal models of pain

#### Animals

All experiments using live animals were conducted in accordance with protocols approved by the Institutional Animal Care and Use Committee of the University of California and adhered to the National Institutes of Health guide for the care and use of Laboratory animals. Great care was taken to reduce the number and minimize suffering of the animals used. Sprague–Dawley male and female rats (250–300 g; Charles River, Wilmington, MA, USA) were housed with free access to food and water. They were maintained under a 12 h light/dark cycle with controlled temperature and relative humidity. After acclimation, the animals were each assayed for their baseline responses and then a day later received an intrathecal port placement. After recovery from the port surgery, the rats were assessed for post-surgery behavioral testing. For peptide treatments, rats were randomly divided into groups and tested with assays performed between 9:00 a.m. and 5:00 p.m. Scientists running the experiments were blinded to the treatment protocol at the time of the tests.

For the intrathecal cannulation briefly, the rats were anesthetized by isoflurane inhalation and the hair on the back at the surgical site shaved and the skin cleaned with ethyl alcohol and betadine per aseptic technique and incised about 1 cm in length. The muscle on the side of the L4 -L5 vertebrae was incised and retracted to place a catheter into the subarachnoid space. The tissue was incised by the tip of a bent needle, which allows escape of a small amount of cerebral spinal fluid (CSF). The caudal edge of the cut is lifted, and an intrathecal catheter, 32ga (0.8Fr) PU 18 cm, fixed to a stylet with a 27ga luer stub (Instech Laboratories) was gently inserted into the intrathecal space in the midline, dorsal to the spinal cord. The catheter was inserted coinciding with the placement of the distal end of the catheter in proximity to the spinal cord the lumbar vertebrae. The exit end of the catheter is taken out through an opening in the skin and connected to an access port. Rats received 2 mg/kg meloxicam once post surgically and 1 mg/kg daily up to 48 hr post-surgery if needed. The rats were allowed to recover for 7 days and then motor activity of the rats was examined for any sign of alteration. Competent rats were then randomly assigned to groups and tested with experimental compounds and assessed in behavioral assays. At necropsy after the end of the experiments, catheter placements were ensured by injection of colored dye any nonpatent catheters were excluded from the results.

Chemicals: the peptides were stored at –20°C in dry powder. The powder was weighed on an analytical balance and an amount of sterile artificial cerebral spinal fluid (ACSF, Fischer Scientific) was added to formulate concentrations of 1 mg/mL stock which was diluted to the desired concentration for each individual experiment. Stock solutions were aliquoted and stored at –20°C until further use. Peptide solutions were delivered with a Hamilton airtight syringe fit with an autoinjector (Instech laboratories) and 10 μL volume of the selected concentration or ACSF vehicle was injected intrathecally via the cannula and followed by 100 μL ACSF. The treatments were randomized to include different treatments and controls within the same day experimental setting and observers were blinded to the treatments.

Behavioral assays: on the test day animals were first tested for their baseline score in the open field and then hotplate. The open field assay was conducted in an open-field arena (40Wx40 L x 30H cm) of a 16-square grid clear acrylic open top chamber. Behavior and activity were monitored for 2 min. Activity was assessed by the number of lines each animal crosses with both hind paws and number of rears as a function of time. The purpose of the open field was to ensure there was not a significant change in motor skill due to the cannulation surgery. Open field ambulatory activity was assessed after long hotplate latency in some animals, but it was not quantified as a treatment outcome given the high stimulated state after the nociceptive tests and the difference in duration on the hotplate between treatment and control groups. Thermal nociceptive assay: The thermal nociception was assessed with a hotplate plate with the intensity set at a constant 52.1°C. Animals were placed individually on the warm metal surface and timed until their response of hind paw licking or jumping. A cutoff time limit of 30 s was imposed to prevent tissue damage. After paw licking or jump behavior is observed rats were immediately removed from the hotplate. One trial was used for baseline and timepoint assessment in order to not overstimulate or train the animals to the stimulus. Limiting exposure to the hotplate also ensured that no tissue damage occurred with animals that reached the cutoff.

Chronic pain models: Chemotherapy induced neuropathy was induced in rats with oxaliplatin after i.t catheter placement recovery with a single i.p. dose of oxaliplatin 6 mg/kg. The animals were allowed to recover for 3 days and then were assessed in the open field assay to ensure motor function and with a von Frey assay to assess allodynia to verify their pain state. The von Frey assay with an electronic aesthesiometer quantified the average baseline for a group of male and female rats to be 72.9±2.7 grams for the mechanical withdrawal threshold after cannulation but before CIPN model induction which fell to 27.9±2.7 grams indicating allodynia. On the day of treatment rats were assessed for baseline measures and then treated and assayed for thermal nociceptive responses.

### 1. Rosetta scripts for refinement of ProTx-II - hNav1.7/NavAb complex

#### 1.1. Rosetta command lines

~Rosetta/main/source/bin/rosetta_scripts.linuxgccrelease \
  -database~Rosetta/main/database/ \
  -in::file::s $pdb \
  -parser::protocol $xml \
  -ignore_unrecognized_res \
  -edensity::mapreso 4.2 \
  -default_max_cycles 200 \
  -relax:constrain_relax_to_start_coords \
  -edensity::cryoem_scatterers \
  -use_input_sc \
  -beta \
  -missing_density_to_jump \
  -out::prefix EM-relax-density- \
  -crystal_refine \
  -nstruct 5

#### 1.2. Rosetta XML scripts

<ROSETTASCRIPTS>
  <SCOREFXNS>
    <ScoreFunction name="beta" weights="beta_cart"/>
    <ScoreFunction name="dens" weights="beta_cart">
      <Reweight scoretype="elec_dens_fast" weight="35.0"/>
      <Set scale_sc_dens_byres="R:0.76,K:0.76,E:0.76,D:0.76,M:0.76,C:0.81,Q:0.81,H:0.81,N:0.81,T:0.81,S:0.81,Y:0.88,W:0.88,A:0.88,F:0.88,P:0.88,I:0.88,L:0.88,V:0.88"/>
    </ScoreFunction>
  </SCOREFXNS>
  <MOVERS>
    <SetupForDensityScoring name="setupdens"/>
    <LoadDensityMap name="loaddens" mapfile="../6N4R.mrc "/>
    <FastRelax name="relaxcart" ramp_down_constraints="false" scorefxn="dens" repeats="2" cartesian="1"/>
  </MOVERS>
  <PROTOCOLS>
    <Add mover="setupdens"/>
    <Add mover="loaddens"/>
    <Add mover="relaxcart"/>
  </PROTOCOLS>
  <OUTPUT scorefxn="beta"/>
</ROSETTASCRIPTS>

### 2. Rosetta scripts for computational design of ProTx-II variants

#### 2.1. Rosetta command lines

#!/bin/bash
if [ $# -lt 3 ]; then
    echo "USAGE: runDesign.sh <pdb> <xml> <resfile>"
    exit
fi
pdb=$1
xml=$2
resfile=$3
~Rosetta/main/source/bin/rosetta_scripts.macosclangrelease \
    -in:path:databas ~Rosetta/main/database \
    -in:file:fullatom \
    -in:file:s $pdb \
    -parser:protocol $xml \
    -parser:script_vars resfile=$resfile \
    -nstruct 20 \
    -linmem_ig 10 \    -optimization:default_max_cycles 200 \
    -out:file:scorefile score-design-$[resfile].sc \
    -out:prefix design-$[resfile]- \
    -overwrite

#### 2.2. ProTx-II resfile

PIKAA ACDEFGHIKLMNPQRSTVWY
start
24 E NATAA
5 E NATAA
6 E NATAA
22 E NATAA
27 E NATAA
29 E NATAA
20 E PIKAA R
28 E PIKAA E
30 E PIKAA L
1 E NOTAA ED
4 E NOTAA ED
7 E NOTAA ED
8 E NOTAA ED
13 E NOTAA ED

#### 2.3. Rosetta XML file

<ROSETTASCRIPTS>
  <SCOREFXNS>
    <ScoreFunction name="ref2015" weights="ref2015"/>
    <ScoreFunction name="ref2015_cst" weights="ref2015">
      <Reweight scoretype="coordinate_constraint" weight="1"/>
      <Reweight scoretype="atom_pair_constraint" weight="1"/>
      <Reweight scoretype="dihedral_constraint" weight="1"/>
      <Reweight scoretype="angle_constraint" weight="1"/>
      <Reweight scoretype="netcharge" weight="1.0" />
    </ScoreFunction>
    <ScoreFunction name="ref2015_cart" weights="ref2015_cart"/>
  </SCOREFXNS>
  <RESIDUE_SELECTORS>
    <Chain chains="E" name="peptide"/>    <Chain chains="A" name="hNav"/>    <Neighborhood distance="8.0" name="peptide_and_neighbors_8 A" selector="peptide"/>    <Neighborhood distance="8.0" name="interface_hNav" selector="peptide"/>    <And name="interface" selectors="peptide_and_neighbors_8 A,interface_hNav"/>    <Not name="not_peptide_and_neighbors" selector="peptide_and_neighbors_8 A"/>    <Index name="anchors" resnums="5,24"/>
  </RESIDUE_SELECTORS>
  <TASKOPERATIONS>
    <InitializeFromCommandline name="init"/>    <ReadResfile filename="%%resfile%%" name="rrf"/>    <RestrictChainToRepacking chain="2" name="only_repack_chain"/> 
    <DisallowIfNonnative disallow_aas="PCG" name="no_PCG"/>    <OperateOnResidueSubset name="restrict_packing_to_hNav" selector="hNav">
      <RestrictToRepackingRLT/>
    </OperateOnResidueSubset>
    <OperateOnResidueSubset name="prevent_to_not_peptide_and_neighbors" selector="not_peptide_and_neighbors">
      <PreventRepackingRLT/>
    </OperateOnResidueSubset>
    <LimitAromaChi2 name="limchi2"/>
    <IncludeCurrent name="current"/>  </TASKOPERATIONS>
  <FILTERS>
    <Ddg confidence="0" jump="1" name="ddg" repack="1"
repeats="5" scorefxn="ref2015" threshold="–20"/>
    <Ddg confidence="0" jump="1" name="ddg_norepack" repack="0" repeats="1" scorefxn="ref2015" threshold="–20"/>
    <Sasa confidence="0" jump="1" name="interface_buried_sasa"/>
    <Sasa confidence="0" hydrophobic="True" jump="1" name="interface_hydrophobic_sasa"/>
    <Sasa confidence="0" jump="1" name="interface_polar_sasa" polar="True"/>
    <BuriedUnsatHbonds confidence="0" jump_number="1" name="BUH" scorefxn="ref2015"/>
    <BuriedUnsatHbonds confidence="0" cutoff="1" ignore_surface_res="true" name="new_buns_bb_heavy" print_out_info_to_pdb="true" report_bb_heavy_atom_unsats="true" residue_selector="interface" residue_surface_cutoff="20.0" scorefxn="ref2015"/>
    <BuriedUnsatHbonds confidence="0" cutoff="1" ignore_surface_res="true" name="new_buns_sc_heavy" print_out_info_to_pdb="true" report_sc_heavy_atom_unsats="true" residue_selector="interface" residue_surface_cutoff="20.0" scorefxn="ref2015"/>
    <PackStat chain="1" name="Packstat" repeats="5" threshold="0.6"/>
    <InterfaceHbonds jump="1" name="interface_Hbonds" scorefxn="ref2015" threshold="0"/>
  </FILTERS>
  <MOVERS>
    <AddConstraints name="add_hNav_constraints" >
     <CoordinateConstraintGenerator name="gen_csts" sd="0.1" sidechain="false" native="false" residue_selector="hNav" />
    </AddConstraints>
     <ClearConstraintsMover name="clear_all_constraints"/>
     <FastDesign cartesian="0" name="design"
ramp_down_constraints="false" repeats="5" scorefxn="ref2015_cst"
task_operations="init,rrf,prevent_to_not_peptide_and_neighbors,only_repack_chain,no_PCG,limchi2,current">
        <MoveMap bb="0" chi="0" jump="1" name="movemap_design">
          <ResidueSelector bb="1" chi="1" selector="peptide_and_neighbors_8 A"/>
        </MoveMap>
      </FastDesign>
      <RollMover name="roll" start_res="1" stop_res="30"
random_roll="1" random_roll_angle_mag="0.15"
random_roll_trans_mag="0.35" />      <Small name="small" residue_selector="peptide" scorefxn="ref2015_cst" nmoves="20"/>
      <FavorSequenceProfile name="favournative" weight="1.2" use_current="true" matrix="IDENTITY"/>
  </MOVERS>
  <PROTOCOLS>
    <Add mover="add_hNav_constraints"/>
    <Add mover="roll"/>
    <Add mover="small"/>
    <Add mover="favournative"/>
    <Add mover="design"/>
    <Add mover="clear_all_constraints"/>
    <Add filter="ddg"/>
    <Add filter="interface_buried_sasa"/>
    <Add filter="interface_hydrophobic_sasa"/>
    <Add filter="interface_polar_sasa"/>
    <Add filter="new_buns_bb_heavy"/>    <Add filter="new_buns_sc_heavy"/>
    <Add filter="Packstat"/>
    <Add filter="interface_Hbonds"/>
  </PROTOCOLS>
  <OUTPUT scorefxn="ref2015"/>
</ROSETTASCRIPTS>

### Statistical analysis

Results are expressed as means ± SEM. Statistical analysis was performed using Sigmaplot (version 14.0, Systat Software) or Igor Pro 8 (Wavemetrics). Results of in vitro experiments were analyzed using Student’s t test (for differences between two groups). Results of in vivo experiments were analyzed using Two Way Repeated Measures ANOVA with Holm-Sidak post-hoc analysis. Differences between groups with p<0.05 were considered statistically significant. In experiments on mice technical replicates (n) were individual neurons and biological replicates (N) were individual mice. Details on statistical analysis are included in the figure legends. We calculated the sample power for rat behavioral studies with eight animals per group is needed to show significant differences of 20% or more. The acceptable power level was considered to be between 0.8 and 0.9. For the thermal hyperalgesia test we assumed the mean value for the control population is 7.5 s and we want to be able to distinguish a difference of 20% with a common standard deviation of about 10%. To test if the two populations are not equal at a significance level of 0.05, a power of 0.8 gives an n=8. The observed effect size was greater than expected and resulted in significant results with even smaller n. Investigators were blinded to identification of compound components in all studies. In brief, compound doses and vehicles were prepared and dosed on the day of the study by an independent researcher from those conducting the behavioral assessments. All treatment groups were randomized independent of baseline responses and the treatments included vehicle and positive controls were randomized on each day of assessment for blinded observers.
