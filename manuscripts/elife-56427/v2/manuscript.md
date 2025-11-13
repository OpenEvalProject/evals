# Chemical and structural investigation of the paroxetine-human serotonin transporter complex

## Authors

- Jonathan A Coleman<sup>1</sup> ([ORCID: 0000-0003-0001-6195](https://orcid.org/0000-0003-0001-6195))
- Vikas Navratna<sup>1</sup> ([ORCID: 0000-0001-8599-1461](https://orcid.org/0000-0001-8599-1461))
- Daniele Antermite<sup>2</sup>
- Dongxue Yang<sup>1</sup>
- James A Bull<sup>2</sup> ([ORCID: 0000-0003-3993-5818](https://orcid.org/0000-0003-3993-5818))
- Eric Gouaux<sup>1</sup> ([ORCID: 0000-0002-8549-2360](https://orcid.org/0000-0002-8549-2360)) †

### Affiliations

1. Vollum Institute, Oregon Health & Science University Portland United States
2. Department of Chemistry, Imperial College London, Molecular Sciences Research Hub London United Kingdom
3. Howard Hughes Medical Institute, Oregon Health & Science University Portland United States

† Corresponding author

## Abstract

Antidepressants target the serotonin transporter (SERT) by inhibiting serotonin reuptake. Structural and biochemical studies aiming to understand binding of small-molecules to conformationally dynamic transporters like SERT often require thermostabilizing mutations and antibodies to stabilize a specific conformation, leading to questions about relationships of these structures to the bonafide conformation and inhibitor binding poses of wild-type transporter. To address these concerns, we determined the structures of ∆N72/∆C13 and ts2-inactive SERT bound to paroxetine analogues using single-particle cryo-EM and x-ray crystallography, respectively. We synthesized enantiopure analogues of paroxetine containing either bromine or iodine instead of fluorine. We exploited the anomalous scattering of bromine and iodine to define the pose of these inhibitors and investigated inhibitor binding to Asn177 mutants of ts2-active SERT. These studies provide mutually consistent insights into how paroxetine and its analogues bind to the central substrate-binding site of SERT, stabilize the outward-open conformation, and inhibit serotonin transport.

## Introduction

Serotonin or 5-hydroxytryptamine (5-HT) is a chemical messenger which acts on cells throughout the human body, beginning in early development and throughout adulthood (Berger et al., 2009). 5-HT acts as both a neurotransmitter and a hormone that regulates blood vessel constriction and intestinal motility (Berger et al., 2009). In the central nervous system, 5-HT is released from presynaptic neurons where it diffuses across the synaptic space and binds to 5-HT receptors, promoting downstream signaling and activating postsynaptic neurons (Gether et al., 2006; Kristensen et al., 2011). Thus, 5-HT is a master regulator of circuits, physiology and behavioral functions including the sleep/wake cycle, sexual interest, locomotion, thermoregulation, hunger, mood, and pain (Berger et al., 2009). 5-HT is cleared from synapses and taken into presynaptic neurons by the serotonin transporter (SERT), thus terminating serotonergic signaling (Gether et al., 2006; Kristensen et al., 2011; Rudnick et al., 2014). SERT resides in the plasma membrane of neurons and belongs to a family of neurotransmitter sodium symporters (NSSs) which also includes the dopamine (DAT) and norepinephrine transporters (NET) (Gether et al., 2006; Kristensen et al., 2011; Rudnick et al., 2014). NSSs are twelve transmembrane spanning secondary active transporters which utilize sodium and chloride gradients to energize the transport of neurotransmitter across the membrane (Rudnick et al., 2014; Navratna and Gouaux, 2019; Yamashita et al., 2005; Figure 1a).

![Figure 1.](https://cdn.elifesciences.org/articles/56427/elife-56427-fig1-v2.jpg)

**Figure 1.:** (a) The substrate is bound at the central site (sand, triangle), near two sodium ions (purple, spheres +) and a chloride ion (green, sphere -). The light orange and light blue triangles depict pseudo two-fold symmetric helical repeats comprised of TM1-5 and 6–10, respectively. The disulfide bond (purple line) and N-linked glycosylation (red ‘Y’ shapes) in extracellular loop 2, along with sites of thermostable mutations (Tyr110Ala, TM1a; Ile291Ala, TM5; Thr439Ser, TM8) are also shown (cyan-filled circles). Structural elements involved in binding allosteric ligands are depicted as black-filled circles. Epitopes for the 8B6 and 15B8 Fab binding sites are in squiggly dark-blue and orange lines, respectively. (b) Schematic of the ABC pose of paroxetine bound to the central binding site, derived from the previously determined x-ray structures (Coleman and Gouaux, 2018; Coleman et al., 2016a). The transmembrane helices are shown with circles and mutated residues in subsite B are in sticks. c, The ACB pose of paroxetine bound to the central binding site of SERT predicted by molecular dynamics simulations and mutagenesis (Abramyan et al., 2019; Slack et al., 2019).

The function of NSSs is modulated by a spectrum of small-molecule drugs, thus in turn controlling the availability of neurotransmitter at synapses. Selective serotonin reuptake inhibitors (SSRIs) are a class of drugs which inhibit SERT and are used to treat major depression and anxiety disorders (Cipriani et al., 2018). Using x-ray crystallography and cryo-EM, we have determined structures of thermostabilized variants of human SERT complexed with SSRIs, which together explain many of the common features and differences associated with SERT-SSRI interactions (Coleman and Gouaux, 2018; Coleman et al., 2016a). SSRIs are competitive inhibitors that bind with high-affinity and specificity to a central substrate-binding site in SERT, preventing 5-HT binding and arresting SERT in an outward-open conformation (Gether et al., 2006; Kristensen et al., 2011; Coleman et al., 2016a).

The central site in NSSs is composed of three subsites: A, B, and C (Wang et al., 2013; Figure 1b). In all NSS-ligand structures, the amine group of ligands resides in subsite A and interacts with a conserved Asp residue (Asp98 in SERT). The heterocyclic electronegative group of the ligand is positioned in subsite B (Navratna and Gouaux, 2019). For example, the alkoxyphenoxy groups of reboxetine and nisoxetine (Penmatsa et al., 2015) in Drosophila DAT (dDAT) structures, the halophenyl groups of cocaine analogs in dDAT and S-citalopram in SERT, and the catechol derivatives in DCP-dDAT and sertraline-SERT all occupy subsite B (Coleman and Gouaux, 2018; Coleman et al., 2016a; Wang et al., 2015a). In addition to the central binding site, the activity of SERT and NSSs can also be modulated by small-molecules which bind to an allosteric site located in an extracellular vestibule, typically resulting in non-competitive inhibition of transport (Coleman et al., 2016a; Zhong et al., 2009; Wennogle and Meyerson, 1982; Plenge and Mellerup, 1985).

Paroxetine is an SSRI which exhibits the highest known binding affinity for the central site of SERT (70.2 ± 0.6 pM) compared to any other currently prescribed antidepressants (Cool et al., 1990). Despite its high affinity, paroxetine is frequently associated with serious side effects including infertility, birth defects, cognitive impairment, sexual dysfunction, weight gain, suicidality, and cardiovascular issues (Nevels et al., 2016). As a result, the mechanism of paroxetine binding to SERT has been studied extensively in order to design drugs with higher-specificity and less adverse side-effects. Despite these efforts, however, the binding pose of paroxetine remains a subject of debate (Coleman and Gouaux, 2018; Coleman et al., 2016a; Abramyan et al., 2019; Davis et al., 2016; Slack et al., 2019).

Paroxetine is composed of a secondary amine which resides in a piperidine ring, which in turn is connected to benzodioxol and fluorophenyl groups (Figure 1b). X-ray structures of the SERT-paroxetine complex revealed that the piperidine ring binds to subsite A while the benzodioxol and fluorophenyl groups occupy subsite B and C in the central site, respectively (Coleman and Gouaux, 2018; Coleman et al., 2016a) (ABC pose, Figure 1b). However, recent mutagenesis, molecular dynamics, and binding studies with paroxetine analogues suggest that paroxetine might either occupy ABC pose as observed in the crystal structure, or an ACB pose where the benzodioxol and fluorophenyl groups occupy subsite C and B of the central site respectively (Abramyan et al., 2019; Slack et al., 2019; Figure 1c). Paroxetine is also thought to interact with the allosteric site of SERT, albeit with low-affinity (Plenge and Mellerup, 1985). We have, however, been unable to visualize paroxetine binding at the allosteric site using structural methods. Our x-ray maps, by contrast, resolve a density feature at the allosteric site which instead resembles a molecule of detergent (Coleman et al., 2016a).

To resolve the ambiguity of paroxetine binding poses at the central binding site, we turned to paroxetine derivatives whereby the 4-fluoro group is substituted with either a bromine or an iodine group. Using transport and binding assays, anomalous x-ray diffraction, and cryo-EM, we have examined the binding poses of these paroxetine analogs and their interactions at the central site. Our studies provide key insights into the recognition of high-affinity inhibitors by SERT and the rational design of new small-molecule therapeutics.

## Results

To provide a robust molecular basis for the interaction of paroxetine (1) with SERT, we devised synthetic routes for two derivatives of paroxetine where the 4-fluoro moiety is substituted with either bromo (Br-paroxetine, 2) or iodo (I-paroxetine, 3) groups (Figure 2a,b). We envisaged the use of a C–H functionalization strategy to access enantiopure hydroxymethyl intermediates I, from readily available N-Boc (R)-nipecotic acid 4 (Figure 2b, Appendix 1). Transition metal-catalyzed C–H functionalization can promote the reaction of unactivated C(sp3)–H bonds with the aid of a directing group (He et al., 2017; Rej et al., 2020; Antermite and Bull, 2019; O' Donovan et al., 2018; Maetani et al., 2017; Chapman et al., 2016). Here, C–H functionalization enabled installation of the appropriate aryl group on the pre-existing piperidine ring (Antermite et al., 2018), providing an attractive and short route to vary this functionality with inherent control of enantiomeric excess. In contrast, common methods for (–)-paroxetine synthesis can require the aromatic substituent to be introduced before stereoselective steps or ring construction, reducing flexibility of the process (Slack et al., 2019; Johnson et al., 2001; Hughes et al., 2003; Brandau et al., 2006; Krautwald et al., 2014; Wang et al., 2015b; Kubota et al., 2016; Amat et al., 2000). Nevertheless, during the preparation of this work, the synthesis of Br-paroxetine was reported using an asymmetric conjugate addition and its binding to SERT has been extensively studied (Slack et al., 2019; Brandau et al., 2006).

![Figure 2.](https://cdn.elifesciences.org/articles/56427/elife-56427-fig2-v2.jpg)

**Figure 2.:** (a) Structures of (–)-paroxetine (1) and the targeted Br- (2) and I-analogues (3). (b) Retrosynthetic analysis of Br- and I-(–)-paroxetine. (c) Synthesis of Br- and I-(–)-paroxetine 2 and 3. Q = 8 quinolinyl-. Reaction conditions: i) X = Br: (–)−5 (4.0 mmol), 4-bromo iodobenzene (three equiv), Pd(OAc)2 (5 mol %), K2CO3 (one equiv), PivOH (one equiv), Ph-CF3 (2 mL, 2 M), 110°C, 18 hr; ii) X = I: (–)−5 (4.0 mmol), 1,4-diiodobenzene (four equiv), Pd(OAc)2 (5 mol %), K2CO3 (one equiv), PivOH (one equiv), Ph-CF3 (2 mL, 2 M), 110°C, 18 hr; iii) DBU (three equiv), toluene (1 M), 110°C, 24 hr; iv) Boc2O (four equiv), DMAP (20 mol %), CH3CN (0.5 M), 35°C, 22 hr; v) LiAlH4 (two equiv), THF, 20°C, 0.5 hr; vi) MsCl (1.3 equiv), Et3N (1.4 equiv), CH2Cl2, 0 to 25°C, 2 hr; vii) X = Br: sesamol (1.6 equiv), NaH (1.7 equiv), THF, 0°C to 70°C, 18 hr; viii) X = I: sesamol (2.0 equiv), NaH (2.2 equiv), DMF, 0°C to 90°C, 20 hr; ix) 4 N HCl in dioxane (10 equiv), 0°C to 25°C, 18 hr.

Our synthesis commenced with the C–H arylation of piperidine (–)−5 bearing Daugulis’ aminoquinoline amide directing group (Zaitsev et al., 2005) at C(3). Adapting our reported method (Antermite et al., 2018), Pd-catalyzed C–H functionalization was achieved in moderate yields using 4-bromoiodobenzene or 1,4-diiodobenzene in excess to prevent bis-functionalization, with palladium acetate, K2CO3 and pivalic acid (Figure 2c). The cis-arylated derivatives (+)−6a and (+)−6b were obtained with > 98% ee and complete C(4) selectivity. Minor enantiopure trans-functionalized products, formed via a trans-palladacycle (Antermite et al., 2018), were also isolated (Appendix 1). Subsequent treatment with 1,8-diazabicyclo(5.4.0)undec-7-ene (DBU) gave complete C(3)-epimerization affording (+)−7a and (+)−7b with the desired trans-stereochemistry in 94% and 91% yields. The aminoquinoline group was removed through telescoped amide activation and reduction with LiAlH4 at 20°C to give enantiopure hydroxymethyl intermediates (–)−8a and (–)−8b in 77% and 75% yield. Mesylation and nucleophilic substitution with sesamol formed ether derivatives (–)−9a and (–)−9b, which were deprotected to give Br- and I-paroxetine 2 and 3. An overall yield of 12% over 8 steps from commercial material was obtained in both cases. At each stage, the identity of the products and purity was established by acquiring 1H and 13C nuclear magnetic resonance spectra, IR spectra, and by high-resolution mass spectrometry Supplementary files 1 and 2. Enantiopurity was assessed by high-performance liquid chromatography (HPLC) with reference to racemic or scalemic samples (Supplementary file 1).

We also employed several SERT variants and the 8B6 Fab in the biochemical and structural studies described here. The wild-type SERT construct used in transport experiments contains the full-length SERT sequence fused to a C-terminal GFP tag (Table 1). The ts2-active variant contains two thermostabilizing mutations (Ile291Ala, Thr439Ser) which allows for purification of the apo transporter for binding studies and has kinetics of 5-HT transport (Km: 4.5 ± 0.6 μM, Vmax: 21 ± 5 pmol min−1) that are in a similar range as wild-type SERT (Km: 1.9 ± 0.3 μM, Vmax: 23 ± 1 pmol min−1) (Coleman et al., 2016a; Green et al., 2015). The ts2-inactive variant (Tyr110Ala, Ile291Ala) (Coleman and Gouaux, 2018), by contrast, is unable to transport 5-HT but can be crystallized due to the stabilizing Tyr110Ala mutation (Green et al., 2015) and binds SSRIs with high-affinity. The ΔN72/ΔC13 SERT variant used for cryo-EM is otherwise wild-type SERT which has been truncated at the N- and C-termini (Table 1) and yet retains transport and ligand-binding activities (Coleman et al., 2019). Finally, the recombinant 8B6 Fab (Coleman et al., 2016a; Coleman et al., 2016b) was used to produce SERT-Fab complexes which were studied by X-ray crystallography and cryo-EM.

**Table 1.**
 Expression constructs used in this study.


<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Expression construct</th>
      <th>Experiment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Wild-type SERT</td>
      <td>Full-length human SERT with a C-terminal thrombin-GFP-StrepII-His10 tag.</td>
      <td>[3H] 5-HT transport assays</td>
    </tr>
    <tr>
      <td>∆N72/ ∆C13 SERT</td>
      <td>Wild-type SERT modified by deletion of 72 residues on N-term and 13 residues on C-term</td>
      <td>Cryo-electron microscopy</td>
    </tr>
    <tr>
      <td>ts2-inactive</td>
      <td>Full-length SERT with thrombin cleavage sites inserted after Gln76 and Thr618 and carrying the Tyr110Ala, Ile291Ala thermostabilizing mutations with additional mutations of surface-exposed cysteines Cys554, Cys580, and Cys622 to alanine</td>
      <td>X-ray crystallography and [3H] citalopram binding assays</td>
    </tr>
    <tr>
      <td>ts2-active</td>
      <td>Full-length SERT with thrombin cleavage sites inserted after Gln76 and Thr618 and carrying the Ile291Ala, Thr439Ser thermostabilizing mutations with additional mutations of surface-exposed cysteines Cys554, Cys580, and Cys622 to alanine</td>
      <td>[3H] citalopram binding assays</td>
    </tr>
    <tr>
      <td>Asn177 mutants</td>
      <td>Asn177 mutated to either Val, Thr, or Gln in ts2-active background</td>
      <td>[3H] citalopram binding assays</td>
    </tr>
  </tbody>
</table>

We began by assessing the functional effects of paroxetine, Br-paroxetine, and I-paroxetine on SERT activity by measuring their inhibition of 5-HT transport and S-citalopram competition binding. We assayed the ability of the Br- and I-paroxetine derivatives to inhibit 5-HT transport in HEK293 cells expressing wild-type SERT, observing that upon substituting the 4-fluoro group with 4-bromo or 4-iodo groups, the potency of inhibition of 5-HT transport in wild-type SERT decreased significantly from 4 ± 1 for paroxetine to 40 ± 20 for Br-paroxetine and 180 ± 70 nM for I-paroxetine (Figure 3a, Table 2). Next, we measured the binding of paroxetine, Br-paroxetine, and I-paroxetine to ts2-active and ts2-inactive SERT using S-citalopram competition binding assays, finding that the SERT variants employed in this study exhibited high-affinity for paroxetine and its derivatives (Table 3). A decrease in the binding affinity upon substituting the 4-fluoro group of paroxetine with 4-bromo or 4-iodo groups was observed in the competition binding assays. However, the difference in the binding affinities between paroxetine variants measured by the competition binding assay was not as pronounced as the difference in the inhibition potencies observed in the 5-HT transport assays (Tables 2 and 3). For example, the ts2-inactive (Tyr110Ala, Ile291Ala) variant employed in the previous (Coleman and Gouaux, 2018) and present x-ray studies exhibited a Ki of 0.17 ± 0.02 nM for paroxetine, 0.94 ± 0.01 nM for Br-paroxetine, and a further decrease in affinity to I-paroxetine (2.3 ± 0.1 nM). The ts2-active SERT variant binds with similar affinity to paroxetine and Br-paroxetine, and shows a 4–5 fold decrease in affinity to I-paroxetine (Figure 3b, Table 3).

![Figure 3.](https://cdn.elifesciences.org/articles/56427/elife-56427-fig3-v2.jpg)

**Figure 3.:** (a) 5-HT-transport of wild-type SERT and its inhibition by paroxetine, Br-, and I-paroxetine. Data are mean ± s.e.m. (n = 6). (b) Competition binding of paroxetine and its derivatives to ts2-inactive SERT. In panels a and b, paroxetine, Br-paroxetine, and I-paroxetine curves are shown as black, red, and blue lines, respectively. Data are mean ± s.e.m. (n = 6). (c) Competition binding of paroxetine to ts2-active (black), Asn177Val (red), Asn177Thr (green), and Asn177Gln (blue). Data are mean ± s.e.m. (n = 3). (d) Competition binding of Br-paroxetine. Data are mean ± s.e.m. (n = 3). (e) Competition binding of I-paroxetine. Data are mean ± s.e.m. (n = 3). The values associated with these experiments are reported in Tables 2 and 3.

**Table 2.**
 Inhibition of 5-HT transport by paroxetine and its derivatives.


<table>
  <thead>
    <tr>
      <th>Ligand</th>
      <th>IC50</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Paroxetine</td>
      <td>4 ± 1 nM</td>
    </tr>
    <tr>
      <td>Br-paroxetine</td>
      <td>40 ± 20 nM</td>
    </tr>
    <tr>
      <td>I-paroxetine</td>
      <td>0.18 ± 0.07 µM</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Binding of paroxetine and its derivatives to SERT variants used in this study.


<table>
  <thead>
    <tr>
      <th rowspan="2">SERT variant</th>
      <th colspan="3">Ki (nM)</th>
    </tr>
    <tr>
      <th>Paroxetine</th>
      <th>Br-paroxetine</th>
      <th>I-paroxetine</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ts2-inactive</td>
      <td>0.17 ± 0.02</td>
      <td>0.94 ± 0.01</td>
      <td>2.3 ± 0.1</td>
    </tr>
    <tr>
      <td>ts2-active</td>
      <td>0.31 ± 0.07</td>
      <td>0.4 ± 0.2</td>
      <td>1.7 ± 0.3</td>
    </tr>
    <tr>
      <td>Asn177Val</td>
      <td>1.11 ± 0.04</td>
      <td>5 ± 1</td>
      <td>7.3 ± 0.9</td>
    </tr>
    <tr>
      <td>Asn177Thr</td>
      <td>1.0 ± 0.1</td>
      <td>5 ± 2</td>
      <td>4.4 ± 0.4</td>
    </tr>
    <tr>
      <td>Asn177Gln</td>
      <td>0.58 ± 0.07</td>
      <td>4 ± 1</td>
      <td>3.6 ± 0.4</td>
    </tr>
  </tbody>
</table>

In the x-ray structures of SERT, paroxetine was modeled in the ABC pose such that the benzodioxol group is in subsite B (Coleman and Gouaux, 2018; Coleman et al., 2016a). A recent study suggested that binding affinity and potency to inhibit the transport of Br-paroxetine was only moderately affected upon mutating a non-conserved residue Ala169 to Asp in subsite B of SERT (Slack et al., 2019; Figure 1b). We recently also identified a conserved residue, Asn177 in the subsite B, which upon mutation exhibited differential effects on the inhibitory potency of ibogaine and noribogaine (Coleman et al., 2019). To further probe the role of Asn177 in subsite B, we studied the binding of paroxetine and its derivatives to selected Asn177 mutants designed in the ts2-active background (Figure 1b). We observed that the affinity of paroxetine to ts2-active SERT decreased by three-fold when Asn177 is substituted with small non-polar or polar residues such as valine and threonine, while only a 2-fold change in Ki was observed for glutamine (Asn177Gln) (Figure 3c). In the case of Br-paroxetine, the Asn177 variants (Ki between 4 and 5 nM) display up to a 10–13 fold decrease in Ki when compared with ts2-active SERT (0.4 ± 0.2 nM) (Figure 3d, Table 3). The Asn177 variants show 2–4 fold decrease in affinity to I-paroxetine, with ts2-active SERT exhibiting a Ki of 1.7 ± 0.3 nM and the mutants a Ki of 4–7 nM. In the case of all three paroxetine variants, the reduction in affinity was the lowest for glutamine substitution. Irrespective of the SERT variant used, substitution of fluoro group with bromo or iodo group invariably decreased the affinity of paroxetine (Figure 3e, Table 3).

To define the binding poses of paroxetine and its analogues to SERT, we solved the structures of the ΔN72/ΔC13 and the ts2-inactive SERT variants complexed with Br- and I-paroxetine using single particle cryo-EM and X-ray crystallography (Figure 4—figure supplements 1 and 2). We began by collecting cryo-EM data sets for ΔN72/ΔC13 SERT-8B6 Fab complexes with each ligand. The TM densities in all three reconstructions were well-defined and contiguous allowing for clear positioning of the main chain in an outward-open conformation (Figure 4—figure supplements 3 and 4). Large aromatic side-chains were well-resolved for all three complexes, also suggesting that the aromatic moieties of paroxetine and its analogues could be identified and positioned in our cryo-EM maps. In addition, the particle distribution and orientations of SERT-Fab complexes in presence of Br- and I-paroxetine were similar to paroxetine, allowing for uniform comparison between the maps.

The ~ 3.3 Å resolution map of the ΔN72/ΔC13 SERT-8B6 paroxetine complex allowed us to locate a density feature for the inhibitor at the central site (Figure 4a). The resolution of the Br- and I-paroxetine complexes was comparatively lower at ~ 4.1 Å and ~ 3.8 Å, respectively (Table 4, Figure 4—figure supplement 4). Nevertheless, these ligands could also be modeled into the density at the central site with a correlation coefficient (CC) of 0.75 and 0.77, respectively (Figure 4b–e). To compare paroxetine in the ABC vs. the ACB pose, we flexibly modeled paroxetine in both poses at the central site followed by real space refinement. We observed that in the ACB pose, paroxetine could be positioned with a CC of 0.70 compared with 0.84 for the ABC pose suggesting that while ABC pose is clearly preferred under the conditions we tested, the possibility of an ACB pose cannot be excluded (Figure 4—figure supplement 5a,b). Based on the higher CC value, and the binding pose information from the ts2-inactive and ts3 SERT x-ray structures, the density in cryo-EM maps for paroxetine at the central site was interpreted to best accommodate ABC pose (Coleman and Gouaux, 2018; Coleman et al., 2016a). We also compared the reconstructed complexes by calculating difference maps, attempting to identify features associated with the scattering of bromine and iodine at the central and allosteric sites. However, the resulting difference maps did not contain any interpretable difference densities and thus did not further assist in ligand modeling. In the cryo-EM maps, the maltose headgroup of a DDM molecule could also be visualized in the allosteric site with the detergent tail inserted between TMs 10, 11, and 12. In contrast, in the X-ray maps only the head group of the octyl-maltoside detergent could be modeled due to the weak density of the hydrocarbon chain.

![Figure 4.](https://cdn.elifesciences.org/articles/56427/elife-56427-fig4-v2.jpg)

**Figure 4.:** (a) Cryo-EM reconstruction of SERT bound to paroxetine where the shape of the SERT-8B6 Fab complex and detergent micelle is shown in transparent light grey. The density of SERT is shown in dark blue with TM1 and TM6 colored in orange and yellow, respectively, and the density for paroxetine in green. The variable domain of the 8B6 Fab is colored in purple. Inset shows the density features at the central site of paroxetine. (b) Density feature at the central site of paroxetine. (c) Density feature at the central site of Br-paroxetine. (d) Density feature at the central site of I-paroxetine. (e) Comparison of the binding poses of paroxetine (grey), Br-paroxetine (green), and I-paroxetine (orange). (f) Anomalous difference electron density (blue) derived from Br-paroxetine, contoured at 5.2σ. g, Anomalous difference electron density (blue) derived from I-paroxetine, contoured at 4.3σ.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/56427/elife-56427-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** A representative zoomed, motion-corrected micrograph with individual single particles circled in white. Bar equals 20 nm. Motion-correction and CTF estimation was performed using MotionCor2 and Ctffind4. The number of movies/particles collected for each data set are shown in black (paroxetine), red (Br-paroxetine), and blue (I-paroxetine). After particle picking using either DoG picker or the blob picker in cryoSPARC, particles were sorted using heterogeneous refinement in cryoSPARC followed by 2D classification. For the DoG-picked particles, 3D classes containing SERT-Fab features (boxed) were combined and subjected to 2D classification. For cryoSPARC-picked particles, heterogeneous refinement was also used to initially sort particles in cryoSPARC. Classes with similar features (boxed) were combined, subjected to three independent 2D classifications, and 2D classes containing SERT-Fab features were combined. Particles picked by both methods were combined and duplicate particle-picks were removed in RELION (particle picks that are less than 100 Å of one another were considered duplicates).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/56427/elife-56427-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** For the paroxetine complex, 3D refinement was performed in RELION followed by 3D classification without alignment and a mask which isolated SERT and Fab. 3D classification was not performed on the Br-paroxetine and I-paroxetine particles. Particles were further refined using non-uniform refinement in cryoSPARC, followed by local refinement in cisTEM with a mask which isolated SERT and the Fab variable domain and removed the Fab constant domain and micelle (mask is shown overlaid in blue on top of the Br-paroxetine reconstruction). The final reconstructed volume was sharpened using Phenix local sharpening.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/56427/elife-56427-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (a) Reconstruction of SERT-8B6 paroxetine complex. Left panel, FSC curves for cross-validation, the final map (blue), masked SERT-Fv (red), and a mask which isolated SERT (black). The high-resolution limit cutoff for refinement was 4.5 Å. Middle left panel: model vs. half map 1 (working, red), half map 2 (free, black), model vs. final map (blue). Middle right panel: cryo-EM density map colored by local resolution estimation. Right panel: the angular distribution of particles used in the final reconstruction. (b) Reconstruction of the SERT-8B6 Br-paroxetine complex. The high-resolution limit cutoff for refinement was 6.5 Å. (c) Reconstruction of the SERT-8B6 I-paroxetine complex. The high-resolution limit cutoff for refinement was 6.5 Å.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/56427/elife-56427-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** (a) Density of TM1-12 of the paroxetine reconstruction, shown in blue. (b) Density of TM1-12 of the Br-paroxetine reconstruction, shown in yellow. (c) Density of TM1-12 of the I-paroxetine reconstruction, shown in purple.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/56427/elife-56427-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** (a) Shows the fit of paroxetine to the cryo-EM density in the ABC pose. (b) Shows the fit in the ACB pose.

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/56427/elife-56427-fig4-figsupp6-v2.jpg)

**Figure 4—figure supplement 6.:** (a) A negative difference density feature (red mesh, 4σ) was observed in subsite C for the Fo(paroxetine)-Fo(Br-paroxetine) map. (b) A negative difference density feature (red mesh, 3.5σ) was observed in subsite C for the Fo(paroxetine)-Fo(I-paroxetine) map. (c) No significant difference densities for the Fo(Br-paroxetine)-Fo(I-paroxetine) map was observed at 3.5σ (shown).

**Table 4.**
 Cryo-EM data collection, refinement and validation statisticsa.


<table>
  <thead>
    <tr>
      <th></th>
      <th>#1 (EMDB-21368) (PDB 6VRH) (EMPIAR-10380)</th>
      <th>#2 (EMDB-21369) (PDB 6VRK)</th>
      <th>#3 (EMDB-21370) (PDB 6VRL)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data collection and processing</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Magnification</td>
      <td>77,160</td>
      <td>77,160</td>
      <td>77,160</td>
    </tr>
    <tr>
      <td>Voltage (kV)</td>
      <td>300</td>
      <td>300</td>
      <td>300</td>
    </tr>
    <tr>
      <td>Electron exposure (e–/Å2)</td>
      <td>54–60</td>
      <td>54</td>
      <td>54</td>
    </tr>
    <tr>
      <td>Defocus range (μm)</td>
      <td>−0.8 to −2.2</td>
      <td>−0.8 to −2.2</td>
      <td>−0.8 to −2.2</td>
    </tr>
    <tr>
      <td>Pixel size (Å)</td>
      <td>0.648</td>
      <td>0.648</td>
      <td>0.648</td>
    </tr>
    <tr>
      <td>Symmetry imposed</td>
      <td>C1</td>
      <td>C1</td>
      <td>C1</td>
    </tr>
    <tr>
      <td>Initial particle images (no.)</td>
      <td>4,147,084</td>
      <td>4,545,318</td>
      <td>4,470,768</td>
    </tr>
    <tr>
      <td>Final particle images (no.)</td>
      <td>420,373</td>
      <td>503,993</td>
      <td>414,091</td>
    </tr>
    <tr>
      <td>Map resolution (Å) FSC threshold</td>
      <td>3.3 0.143</td>
      <td>4.1 0.143</td>
      <td>3.8 0.143</td>
    </tr>
    <tr>
      <td>Map resolution range (Å)†</td>
      <td>4.25–3.25</td>
      <td>5.75–3.75</td>
      <td>5.50–3.50</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Initial model used (PDB code)</td>
      <td>6AWN</td>
      <td>6VRH</td>
      <td>6VRH</td>
    </tr>
    <tr>
      <td>Initial model CC Model resolution (Å)‡ FSC threshold</td>
      <td>0.64 3.7 0.5</td>
      <td>0.70 4.3 0.5</td>
      <td>0.71 4.1 0.5</td>
    </tr>
    <tr>
      <td>Model resolution range (Å)</td>
      <td>25.9–3.3</td>
      <td>33.0–4.1</td>
      <td>29.6–4.2</td>
    </tr>
    <tr>
      <td>Map sharpening B factor (Å2)</td>
      <td>−85</td>
      <td>−174</td>
      <td>−161</td>
    </tr>
    <tr>
      <td>Model composition Non-hydrogen atoms Protein residues Ligands (atoms)</td>
      <td>6143 764 254</td>
      <td>6142 764 254</td>
      <td>6142 764 254</td>
    </tr>
    <tr>
      <td>B factors (Å2) Protein Ligand</td>
      <td>138 129</td>
      <td>138 113</td>
      <td>122 112</td>
    </tr>
    <tr>
      <td>R.m.s. deviations Bond lengths (Å) Bond angles (°)</td>
      <td>0.002 0.48</td>
      <td>0.002 0.59</td>
      <td>0.002 0.54</td>
    </tr>
    <tr>
      <td>Validation Refined model CC MolProbity score Clashscore Poor rotamers (%)</td>
      <td>0.73 1.86 9.67 0</td>
      <td>0.74 1.96 10.26 0</td>
      <td>0.75 1.88 10.59 0.00</td>
    </tr>
    <tr>
      <td>Ramachandran plot Favored (%) Allowed (%) Disallowed (%)</td>
      <td>94.84 5.16 0</td>
      <td>93.54 6.46 0</td>
      <td>95.12 4.88 0</td>
    </tr>
  </tbody>
</table>

_aData set #1 is the paroxetine reconstruction, #2 is Br-paroxetine, #3 I-paroxetine.†Local resolution range.‡Resolution at which FSC between map and model is 0.5._

We then explored the binding pose of paroxetine by growing crystals and collecting x-ray data of the ts2-inactive SERT-8B6 Fab complex with Br- and I-paroxetine (Table 5). Anomalous difference maps calculated from the previously determined ts2-inactive paroxetine structure (PDB ID: 6AWN) after refinement, showed clear densities for Br- and I- atoms of the paroxetine derivatives in subsite C (Figure 4f,g). No detectable anomalous peaks were observed in either subsite B or in the allosteric site and there were no other peaks in any other location above 2.5σ, suggesting that under these conditions, Br-paroxetine and I-paroxetine do not bind substantially in the ACB orientation or to the allosteric site. Next, we calculated isomorphous difference maps (Fo-Fo) using the ts2-inactive paroxetine dataset (PDB: 6AWN) and either the Br-paroxetine or I-paroxetine datasets. The Fo(paroxetine)-Fo(Br-paroxetine) map also revealed a difference peak in subsite C near the halogenated groups while no significant peaks were detected in subsite B (Figure 4—figure supplement 6a). Similarly, the Fo(paroxetine)-Fo(I-paroxetine) map also contained a difference peak which overlapped with the position of the halogen (Figure 4—figure supplement 6b) while the Fo(Br-paroxetine)-Fo(I-paroxetine) difference map did not contain any interpretable features, likely due to the low resolution of both datasets (Figure 4—figure supplement 6c).

**Table 5.**
 X-ray data collection statistics.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Br-paroxetine (PDB 6W2B)</th>
      <th>I-paroxetine (PDB 6W2C)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data collection</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>C2221</td>
      <td>C2221</td>
    </tr>
    <tr>
      <td>Cell dimensions</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>128.0, 161.9, 139.7</td>
      <td>127.7, 161.9, 140.8</td>
    </tr>
    <tr>
      <td>α, β, γ (°)</td>
      <td>90, 90, 90</td>
      <td>90, 90, 90</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>20.45–4.69 (4.82–4.69)*</td>
      <td>25.98–6.12 (6.30–6.12)*</td>
    </tr>
    <tr>
      <td>Rmerge</td>
      <td>13.60 (339.3)</td>
      <td>7.9 (292.9)</td>
    </tr>
    <tr>
      <td>I / σI CC1/2</td>
      <td>5.51 (0.49) 99.9 (16.5)</td>
      <td>5.01 (0.32) 99.8 (20.0)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>99.2 (100.0)</td>
      <td>92.6 (89.7)</td>
    </tr>
    <tr>
      <td>Redundancy</td>
      <td>6.8 (6.2)</td>
      <td>1.8 (1.7)</td>
    </tr>
  </tbody>
</table>

_*Values in parentheses are for highest-resolution shell._

We next compared the cryo-EM structure of the SERT-paroxetine complex to the X-ray structure of the ts3 SERT paroxetine complex. Overall comparison of the transporter revealed only minor variation between structures solved by each method, with a Cα root-mean-square-deviation (RMSD) of 0.68 Å. The most significant differences between the cryo-EM and the X-ray structures were found at the extracellular and intracellular sites of TM12 and also in EL2, while the core of the transporter (TM1-10) was largely unchanged (Figure 5a). These changes can largely be explained on the basis of a crystal packing interface formed by TM12 and a highly flexible EL2 that is bound to the 8B6 Fab. We also compared central site residues involved in paroxetine binding, finding that the best fit to the cryo-EM density revealed only minor differences in the side-chains of Asp98, Tyr176, and Phe335 when compared to the x-ray structure (all atom RMSD: 0.91 Å) (Figure 5b). Finally, we compared the cryo-EM structures of the SERT 15B8 Fab/8B6 scFv paroxetine complex (PDB: 6DZW) to the SERT 8B6 Fab paroxetine complex to understand if these antibodies induce changes in transporter structure. Here we found that the most significant differences occurred in the extracellular domain and involved localized regions of EL2 and EL4 that interact with the antibody (Figure 5c). The transporter core was largely unchanged, with the only other significant differences being found in EL6, TM12, and IL4.

![Figure 5.](https://cdn.elifesciences.org/articles/56427/elife-56427-fig5-v2.jpg)

**Figure 5.:** (a) Superposition of the x-ray ts3-SERT-8B6 paroxetine structure (PDB: 5I6X) with the SERT-8B6 paroxetine complex determined by cryo-EM. The root-mean-square-deviations (RMSD) for Cα positions were plotted onto the cryo-EM SERT-8B6 paroxetine structure. (b) Comparison of the central binding site of the x-ray (grey) and cryo-EM (green) paroxetine structures. (c) The structure of the ts2-inactive SERT-8B6 scFv/15B8 Fab paroxetine (cryo-EM, 6DZW), ts2-inactive SERT-8B6 Fab paroxetine (x-ray, 6AWN), and the SERT-8B6 paroxetine (cryo-EM, this work) complexes were superposed onto the ts3 SERT-8B6 paroxetine complex (x-ray, 5I6X) as a reference. The RMSD for Cα positions were calculated for each structure in comparison with the reference. Regions with RMSD > 3.0 Å are shown boxed in red.

## Discussion

The binding of paroxetine to SERT has been extensively debated (Coleman and Gouaux, 2018; Coleman et al., 2016a; Abramyan et al., 2019; Davis et al., 2016; Slack et al., 2019). The first X-ray structure of the ts3-SERT variant demonstrated that the binding pose is such that the piperidine, benzodioxol, and fluorophenyl groups occupy subsites A, B, and C respectively, in the ABC pose (Coleman et al., 2016a; Figure 1b). Competition binding experiments using a variant of SERT containing a central binding site that has been genetically engineered to possess photo-cross-linking amino acids corroborated that paroxetine binds in a fashion which is similar to that observed in crystal structure (Coleman and Gouaux, 2018; Coleman et al., 2016a), where the fluorophenyl group is in proximity to Val501 (Rannversson et al., 2017). However, computational docking experiments using wild-type SERT predicted that the position of benzodioxol and fluorophenyl groups of paroxetine are ‘flipped’, with paroxetine occupying an ACB pose (Davis et al., 2016; Figure 1c). Subsequent studies involving wild-type and mutant SERT variants, that include modeling, mutagenesis, and Br-paroxetine docking experiments suggested that paroxetine could bind in both ABC and ACB poses. These studies also suggested that bromination of paroxetine and certain mutations near the central site, such as Ala169Asp, favored ABC pose (Abramyan et al., 2019; Slack et al., 2019). Hence, the authors in these studies hypothesized that the ABC pose observed in the crystal structure could be because of the crystallization conditions and thermostabilizing mutations.

One of the thermostabilizing mutations in ts3-SERT, Thr439Ser, is near the central binding site and Thr439 participates in a hydrogen bonding network in subsite B that, in turn, includes the dioxol group of paroxetine. To probe the role of the Thr439Ser mutation in modulating the binding pose of paroxetine, we solved the X-ray structure of ts2-inactive (Tyr110Ala, Ile291Ala) SERT, wherein the residue at position 439 was the wild-type threonine. Paroxetine could be modeled in the ABC pose in the X-ray structure of ts2-inactive SERT (Coleman and Gouaux, 2018). MD simulations of ts2-inactive SERT suggested that the Thr439Ser mutation weakens the Na2 site. Furthermore, MD simulations and binding and uptake kinetics experiments using wild-type SERT in presence of paroxetine and a variant of paroxetine where in the 4-fluoro group is substituted with 4-bromo group suggested that the paroxetine binding pose in SERT could be ambiguous because of the pseudo symmetry of the paroxetine molecule. It was noted that paroxetine could occupy both ABC and ACB poses with almost equivalent preference. Upon substituting the 4-fluoro with a bulkier 4-bromo group, the ABC pose was favored (Abramyan et al., 2019; Slack et al., 2019).

Structural studies of SERT in complex with paroxetine and its analogues were thus required to resolve the uncertainty in paroxetine binding pose at the central site. Previously, we had demonstrated that cryo-EM can be used to define the position of ligands at the central site of SERT (Coleman et al., 2019). Here, we employed a similar methodology using the ΔN72/ΔC13 SERT variant complexed with 8B6 Fab to study binding of paroxetine at the central site. The density feature of paroxetine in the cryo-EM map at ~ 3.3 Å clearly resolved the larger benzodioxol and smaller fluorophenyl groups in subsite B and C, respectively (Figure 4b). Though this reconstruction suggests that paroxetine binds in the ABC pose, we also considered the possibility that the inhibitor density feature may represent an average of the ABC and ACB poses. We expected that if Br- and I-paroxetine were suitable surrogates for paroxetine, their binding pose would be unaffected by their reduced electronegativity and the size of the halogenated groups and therefore that they would also be associated with a comparable density feature at this site, as demonstrated by our cryo-EM maps. To further explore if there was a fraction of Br- or I-paroxetine in the ACB pose, we examined the position of the Br- or I- atoms at the central site by X-ray crystallography. If Br- and I-paroxetine were to bind in both the ABC or ACB poses, we expected to observe two anomalous peaks in our x-ray maps in subsites B and C; for both ligands, however, only a single detectable peak was observed in subsite C (Figure 4f,g). Thus, our direct biophysical observations reveal that under the conditions that we tested the ABC pose of paroxetine is preferred over the the ACB pose.

Paroxetine is stabilized at the central binding site by aromatic, ionic, non-ionic, hydrogen bonding, and cation-π interactions (Coleman and Gouaux, 2018). In the ABC pose, the amine of the piperidine ring of paroxetine binds with Asp98 (3.5 Å) and also makes a cation-π interaction with Tyr95 of subsite A (Figure 4a). The benzodioxol group of paroxetine, a catechol-like entity, occupies a position in subsite B which is similar to the binding of catechol derivative groups of sertraline and 3,4-dichlorophenethylamine in SERT (Coleman and Gouaux, 2018) and dDAT (Wang et al., 2015a) structures, respectively. In subsite B, the ring of Tyr176 makes an aromatic interaction with the benzodioxol while the hydrogen-bonding network in subsite B formed by Asn177, Thr439, backbone carbonyl oxygens, and amides are likely responsible for stabilization of the dioxol. The side-chain of Ile172 inserts between the benzodioxol and fluorophenyl, while the rings of Phe341 and Phe335 stack on either side of the fluorophenyl, ‘sandwiching’ it within subsite C. The halogen group of paroxetine and its analogues reside adjacent to the side-chain of Thr497 (4.0 Å), which may act to stabilize these groups through hydrogen bonding (Figure 4a). The larger atomic radius, the longer length of the carbon-halogen bond, and the difference in electronegativity of bromine (radius: 1.85 Å, bond-length: 1.92 Å, electronegativity: 2.96) and iodine (radius: 1.98 Å, bond-length: 2.14 Å, electronegativity: 2.66) relative to fluorine (radius: 1.47 Å, bond-length: 1.35 Å, electronegativity: 3.98) would explain why the fluorine analogue binds with greater affinity than Br-paroxetine and I-paroxetine.

We also explored the effect of conservative and non-conservative mutations in subsite B of SERT at Asn177 (Figure 3). Asn177 participates in a hydrogen-bond network with the hydroxyl group of noribogaine and with the dioxol of paroxetine. However, this network of interactions is also important for binding halogenated inhibitors in subsite B, as in the case for S-citalopram, fluvoxamine, and sertraline. All the mutants that we tested at Asn177 resulted in a loss of binding affinity to paroxetine and its analogues. Furthermore, the Ala169Asp mutation in subsite B (Slack et al., 2019; Figure 1b,c) also reduced paroxetine inhibition and binding, likely also disrupting these interactions. Although the effects were less severe when compared to paroxetine, Br-paroxetine binding and inhibition was also reduced for Ala169Asp (Slack et al., 2019). Thus, these mutations highlight the importance of subsite B interactions in paroxetine binding but they cannot be used to demonstrate the inhibitor pose because, in the ABC or ACB poses, either the dioxol or fluorine of paroxetine could act as a hydrogen-bond acceptor in subsite B.

Using a combination of chemical biology, cryo-EM, and X-ray crystallography we observed that under the conditions that we studied, the SSRI paroxetine preferably occupies the ABC pose at the central site, where it is involved in numerous interactions. However, the data presented in the manuscript does not completely exclude the possibility of an ACB pose at the central site. Our studies of the mechanism of paroxetine binding to SERT provide a robust framework for the design of experiments to identify new highly specific small-molecule SERT inhibitors.

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
      <td>Gene (Homo sapiens)</td>
      <td>Human serotonin transporter</td>
      <td>cDNA</td>
      <td>NCBI Reference Sequence: NP_001036.1</td>
      <td>Dr. Randy D. Blakely (Florida Atlantic university brain institute)</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HEK293S GnTI-</td>
      <td>ATCC</td>
      <td>Cat # ATCC CRL-3022</td>
      <td>Used for expression of SERT (PMID:27929454)</td>
    </tr>
    <tr>
      <td>Cell line (Spodoptera frugiperda)</td>
      <td>SF9 cells</td>
      <td>ATCC</td>
      <td>Cat # ATCC CRL-1711</td>
      <td>Used in production of baculovirus for transduction, and SERT antibodies (PMID:27929454)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal. Isotype IgG2a, kappa</td>
      <td>OHSU VGTI, Monoclonal Antibody Core</td>
      <td></td>
      <td>8B6</td>
    </tr>
    <tr>
      <td>Transfected construct (human)</td>
      <td>pEG BacMam</td>
      <td>Gouaux lab</td>
      <td></td>
      <td>PMID:25299155</td>
    </tr>
    <tr>
      <td>Affinity chromatography resin</td>
      <td>Strep-Tactin Superflow high capacity resin</td>
      <td>Iba life sciences</td>
      <td>Cat#2-1208-500</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>n-dodecyl-β-D-maltoside</td>
      <td>Anatrace</td>
      <td>Cat # D310</td>
      <td>Detergent</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>n-octyl β-D-maltoside</td>
      <td>Anatrace</td>
      <td>Cat # O310</td>
      <td>Detergent</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>fluorinated octyl-maltoside</td>
      <td>Anatrace</td>
      <td>Cat # O310F</td>
      <td>Detergent</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cholesteryl Hemisuccinate</td>
      <td>Anatrace</td>
      <td>Cat # CH210</td>
      <td>Lipid</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>1-palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine</td>
      <td>Anatrace</td>
      <td>Cat # P516</td>
      <td>Lipid</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine</td>
      <td>Anatrace</td>
      <td>Cat # P416</td>
      <td>Lipid</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoglycerol</td>
      <td>Anatrace</td>
      <td>Cat # P616</td>
      <td>Lipid</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Paroxetine hydrochloride hemihydrate</td>
      <td>Sigma</td>
      <td>Cat # P9623</td>
      <td>Inhibitor</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[3H]5-HT</td>
      <td>PerkinElmer</td>
      <td>Cat # NET1167250UC</td>
      <td>Radiolabeled substrate</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>[3H]citalopram</td>
      <td>PerkinElmer</td>
      <td>Cat # NET1039250UC</td>
      <td>Radiolabeled inhibitor</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>XDS</td>
      <td>PMID:20124692</td>
      <td>RRID:SCR_015652</td>
      <td>http://xds.mpimf-heidelberg.mpg.de/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phaser</td>
      <td>PMID:24189240</td>
      <td>RRID:SCR_014219</td>
      <td>https://www.phaser.cimr.cam.ac.uk/index.php/Phaser_Crystallographic_Software</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phenix</td>
      <td>PMID:22505256</td>
      <td>RRID:SCR_014224</td>
      <td>https://www.phenix-online.org/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SerialEM</td>
      <td>PMID:16182563</td>
      <td>RRID:SCR_017293</td>
      <td>http://bio3d.colorado.edu/SerialEM</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MotionCor2</td>
      <td>PMID:28250466</td>
      <td>RRID:SCR_016499</td>
      <td>http://msg.ucsf.edu/em/software/motioncor2.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CTFFIND4</td>
      <td>PMID:26278980</td>
      <td>RRID:SCR_016732</td>
      <td>https://grigoriefflab.umassmed.edu/ctffind4</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DoG-Picker</td>
      <td>PMID:19374019</td>
      <td></td>
      <td>http://emg.nysbc.org/redmine/projects/software/wiki/DoGpicker</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>cryoSPARC</td>
      <td>PMID:28165473</td>
      <td>RRID:SCR_016501</td>
      <td>https://cryosparc.com/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RELION</td>
      <td>PMID:23000701</td>
      <td>RRID:SCR_016274</td>
      <td>http://www2.mrc-lmb.cam.ac.uk/relion</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>cisTEM</td>
      <td>PMID:29513216</td>
      <td>RRID:SCR_016502</td>
      <td>https://cistem.org/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSF-Chimera</td>
      <td>PMID:15264254</td>
      <td>RRID:SCR_004097</td>
      <td>https://www.cgl.ucsf.edu/chimera/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Coot</td>
      <td>PMID:15572765</td>
      <td>RRID:SCR_014222</td>
      <td>https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MolProbity</td>
      <td>PMID:20057044</td>
      <td>RRID:SCR_014226</td>
      <td>http://molprobity.biochem.duke.edu/</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>R 2/2 200 mesh Au holey carbon grids</td>
      <td>Electron Microscopy Sciences</td>
      <td>Cat # Q2100AR2</td>
      <td>Cryo-EM grids</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Copper HIS-Tag YSI</td>
      <td>PerkinElmer</td>
      <td>Cat # RPNQ0096</td>
      <td>SPA beads</td>
    </tr>
  </tbody>
</table>

### SERT expression and purification

The human SERT constructs used in this study were the wild-type, the N- and C-terminally truncated wild-type (ΔN72/ΔC13), ts2-inactive (Tyr110Ala, Ile291Ala), and ts2-active (Ile291Ala, Thr439Ser) (Coleman and Gouaux, 2018; Coleman et al., 2016a; Green et al., 2015; Coleman et al., 2019; Coleman et al., 2016b) proteins (Table 1). The Asn177 mutants were generated in the ts2-active background. The expression and purification of SERT was carried out as previously described with minor modifications (Coleman and Gouaux, 2018; Coleman et al., 2016a; Coleman et al., 2019; Coleman et al., 2016b), as described below. All SERT constructs were cloned into BacMam vector system to be expressed as C-terminal GFP fusion using baculovirus-mediated transduction of HEK293S GnTI- cells. Cells were solubilized in 20 mM Tris pH 8 with 150 mM NaCl, containing 20 mM n-dodecyl-β-D-maltoside (DDM) and 2.5 mM cholesteryl hemisuccinate (CHS), followed by purification using Strep-Tactin affinity chromatography in 20 mM Tris pH 8 with 100 mM NaCl (TBS), 1 mM DDM, and 0.2 mM CHS.

For cryo-EM of the ΔN72/ΔC13 SERT, 1 mM 5-HT was added during solubilization and affinity purification to stabilize SERT. GFP was cleaved from SERT by digestion with thrombin and the SERT-8B6 complex was made as described in the previous paragraph. The complex was separated from free Fab and GFP by SEC in TBS containing 1 mM DDM and 0.2 mM CHS, and the peak fractions were concentrated to 4 mg/ml followed by addition of either 200 μM paroxetine, Br-paroxetine or I-paroxetine.

For crystallization, no ligands were added during purification of ts2-inactive SERT, and 5% glycerol and 25 μM lipid (1-palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine, 1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine, and 1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoglycerol at a molar ratio of 1:1:1) were included in all the purification buffers. Following affinity purification, the fusion protein was digested by thrombin and EndoH and combined with recombinant 8B6 Fab at a molar ratio of 1:1.2. The SERT-8B6 complex was isolated by size-exclusion chromatography (SEC) on a Superdex 200 column in TBS containing 40 mM n-octyl β-D-maltoside, 0.5 mM CHS. The SERT-8B6 Fab complex was concentrated to 2 mg/ml and 1 μM 8B6 Fab and 50 μM Br-paroxetine or I-paroxetine was added prior to crystallization.

### Synthesis of Br- and I-paroxetine

All reactions were carried out under an inert atmosphere (argon) with flame-dried glassware using standard techniques, unless otherwise specified. Anhydrous solvents were obtained by filtration through drying columns (THF, MeCN, CH2Cl2 and DMF) or used as supplied (α,α,α-trifluorotoluene). Reactions in sealed tubes were run using Biotage microwave vials (2–5 ml or 10–20 ml recommended volumes). Aluminum caps equipped with molded butyl/PTFE septa were used for reactions in α,α,α-trifluorotoluene and toluene. Simple butyl septa were used for reactions in other solvents. Chromatographic purification was performed using 230–400 mesh silica with the indicated solvent system according to standard techniques. Analytical thin-layer chromatography (TLC) was performed on precoated, glass-backed silica gel plates. Visualization of the developed chromatogram was performed by UV absorbance (254 nm) and/or stained with a ninhydrin solution in ethanol. HPLC analyses were carried out on an Agilent 1260 Infinity Series system, employing Daicel Chiracel columns, under the indicated conditions. The high-resolution mass spectrometry (HRMS) analyses were performed using electrospray ion source (ESI). ESI was performed using a Waters LCT Premier equipped with an ESI source operated either in positive or negative ion mode. The software used was MassLynx 4.1; this software does not account for the electron and all the calibrations/references are calculated accordingly, that is [M+H]+ is detected and the mass is calibrated to output [M+H]. Melting points are uncorrected. Infrared spectra (FTIR) were recorded in reciprocal centimeters (cm–1).

Nuclear magnetic resonance spectra were recorded on 400 or 500 MHz spectrometers. The frequency used to record the NMR spectra is given in each assignment and spectrum (1H NMR at 400 or 500 MHz; 13C NMR at 101 MHz or 126 MHz). Chemical shifts for 1H NMR spectra were recorded in parts per million from tetramethylsilane with the residual protonated solvent resonance as the internal standard (CHCl3: δ 7.27 ppm, (CD2H)2SO: δ 2.50 ppm, CD2HOD: δ 3.31 ppm). Data was reported as follows: chemical shift (multiplicity [s = singlet, d = doublet, t = triplet, m = multiplet and br = broad], coupling constant, integration and assignment). J values are reported in Hz. All multiplet signals were quoted over a chemical shift range. 13C NMR spectra were recorded with complete proton decoupling. Chemical shifts were reported in parts per million from tetramethylsilane with the solvent resonance as the internal standard (13CDCl3: δ 77.0 ppm, (13CD3)2SO: δ 39.5 ppm, 13CD3OD: δ 49.0 ppm). Assignments of 1H and 13C spectra, as well as cis- or trans-configuration, were based upon the analysis of δ and J values, analogy with previously reported compounds (Antermite et al., 2018), as well as DEPT, COSY and HSQC experiments, where appropriate. All Boc containing compounds appeared as a mixture of rotamers in the NMR spectra at room temperature. In some cases, NMR experiments for these compounds were carried out at 373 K to coalesce the signals, which is indicated in parentheses where appropriate. For NMR analysis performed at room temperature, 2D NMR experiments (COSY and HSQC) are also presented when useful for the assignments. Observed optical rotation (α’) was measured at the indicated temperature (T °C) and values were converted to the corresponding specific rotations $\alpha_{D}^{T}$ in deg cm2g–1, concentration (c) in g per 100 mL. Full details of the synthetic route, using enantiopure and racemic substrates are provided in Appendix 1, and NMR spectra of all reaction intermediates, 2 and 3, and HPLC analysis are cataloged in Supplementary files 1 and 2.

### Crystallization

Crystals of ts2-inactive SERT-8B6 Fab complex were grown by hanging-drop vapor diffusion at 4°C at a ratio of 2:1 (v/v) protein:reservoir. Br-paroxetine crystals were grown using reservoir solution containing 50 mM Tris pH 8.5, 20 mM Na2(SO4), 20 mM LiCl2, 36% PEG 400, and 0.5% 6-aminohexanoic acid. I-paroxetine crystals were grown using a reservoir solution containing 100 mM HEPES pH 7.5, 40 mM MgCl2, and 32% PEG 400.

### X-ray data collection

Crystals were harvested and flash cooled in liquid nitrogen. Data was collected at the Advanced Photon Source (Argonne National Laboratory, beamline 24-ID-C). Data for Br-paroxetine was collected at a wavelength of 0.91840 Å and at 1.37760 Å for I-paroxetine.

### Anomalous difference maps

X-ray data sets were processed with XDS (Kabsch, 2010); Friedel pairs were allowed to have different intensities. Molecular replacement was performed with coordinates from the previously determined ts2-inactive SERT-paroxetine structure (Protein Data Bank (PDB) code: 6AWN) (Coleman and Gouaux, 2018) using PHASER (Bunkóczi et al., 2013). B-factors were refined using PHENIX (Afonine et al., 2012) followed by generating anomalous difference maps using the phases derived from the higher resolution structures. To maximize the signal-to-noise ratio of the Br-paroxetine anomalous difference density, the high-resolution phases were blurred with a B-factor of 500 with a high-resolution cutoff of 5.5 Å. Using these optimized parameters for the Fourier analysis of the Br-paroxetine diffraction data, we obtained an anomalous map with the largest difference peak being present at 6.0σ and the noise level estimated at ~ 2.5σ. To maximize the signal-noise-ratio of the I-paroxetine anomalous difference density, a high-resolution and low-resolution cutoff of 6.3 and 30 Å was applied during the generation of the anomalous maps. Using these optimized parameters for the Fourier analysis of the I-paroxetine diffraction data, we obtained an anomalous map with the largest difference peak being present at 4.5σ and the noise level estimated at ~ 2.5σ.

### Fo-Fo isomorphous difference maps

Isomorphous difference (Fo-Fo) maps were calculated in PHENIX by analyzing isomorphous pairs of crystals. Difference maps were calculated using the previously determined ts2-inactive SERT-paroxetine dataset and PDB (6AWN) for phasing. High- and low-resolution cutoffs of 6.0 and 30.0 Å were applied for the Fo(paroxetine)- Fo(Br-paroxetine) map and cutoffs of 6.3 and 30.0 Å were used for the Fo(paroxetine)- Fo(I-paroxetine) and Fo(Br-paroxetine)- Fo(I-paroxetine) maps.

### Cryo-EM grid preparation

To promote the inclusion of particles in thin ice, 100 μM fluorinated octyl-maltoside (final concentration) from a 10 mM stock was added to SERT-8B6 complexes immediately prior to vitrification. Quantifoil holey carbon gold grids, 2.0/2.0 μm, size/hole space, 200 mesh) were glow discharged for 60 s at 15 mA. SERT-8B6 Fab complex (2.5 μl) was applied to the grid followed by blotting for 2 s in the vitrobot and plunging into liquid ethane cooled by liquid N2.

### Cryo-EM data collection and processing

Images were acquired using the automated program SerialEM (Mastronarde, 2005) on a FEI Titan Krios transmission electron microscope, operating at 300 keV and equipped with a Gatan Image Filter with the slit width set to 20 eV. A Gatan K3 direct electron detector was used to record movies in super-resolution counting mode with a binned pixel size of 0.648 Å per pixel. The defocus values ranged from −0.8 to −2.2 μm. Exposures of 1.0–1.5 s were dose fractioned into 40 frames, resulting in a total dose of 54–60 e− Å−2. Movies were corrected for beam-induced motion using MotionCor2 (Zheng et al., 2017) with 5 × 5 patching. The contrast transfer function (CTF) parameters for each micrograph was determined using ctffind4 (Rohou and Grigorieff, 2015) and particles were picked either using DoG-Picker (Voss et al., 2009) or blob-based picking in cryoSPARC (Punjani et al., 2017). DoG or cryoSPARC picked particles were independently subjected to 3D classification against a low-resolution volume of the SERT-8B6 complex. After sorting, the DoG and cryoSPARC picked particles were combined in RELION (Scheres, 2012) and the duplicate picks were removed (particle picks that are less than 100 Å of one another were considered duplicates). Combined particles were further sorted using reference-free 2D classification in cryoSPARC, followed by refinement in RELION and further 3D classification. Particles were then re-extracted (box size 400, 0.648 Å per pixel) and subjected to non-uniform refinement in cryoSPARC. Local refinement was then performed in cisTEM (Grant et al., 2018) with a mask that excludes the micelle and Fab constant domain to remove low-resolution features. The high-resolution refinement limit was incrementally increased while maintaining a correlation of 0.95 or better until no improvement in map quality was observed. The resolution of the reconstructions was accessed using the Fourier shell correlation (FSC) criterion and a threshold of 0.143 (Rosenthal and Henderson, 2003). Map sharpening was performed using local sharpening in PHENIX.

### Cryo-EM model building and refinement

A starting model was generated by fitting the X-ray structure of SERT-8B6 Fab paroxetine complex (PDB code: 6AWN) into the cryo-EM reconstruction in Chimera (Pettersen et al., 2004). Several rounds of manual adjustment and rebuilding were performed in Coot (Emsley and Cowtan, 2004), followed by real space refinement in PHENIX. For cross-validation, the FSC curve between the refined model and half maps was calculated and compared to prevent overfitting. Molprobity was used to evaluate the stereochemistry and geometry of the structures (Chen et al., 2010).

### Radioligand binding and uptake assays

Competition binding experiments were performed using scintillation proximity assays (SPA) (Green et al., 2015; Coleman et al., 2016b). The assays contained ~ 10 nM SERT, 0.5 mg/ml Cu-Ysi beads in TBS with 1 mM DDM, 0.2 mM CHS, and 10 nM [3H]citalopram and 0.01 nM–1 mM of the cold competitors. Experiments were measured in triplicate. The error bars for each data point represent the s.e.m. Ki values were determined with the Cheng–Prusoff equation (Cheng and Prusoff, 1973) in GraphPad Prism. Uptake was measured as described previously in 96-well plates with [3H]5-HT diluted 1:100 with unlabeled 5-HT. After 24 hr, cells were washed into uptake buffer (25 mM HEPES-Tris, pH 7.0, 130 mM NaCl, 5.4 mM KCl, 1.2 mM CaCl2, 1.2 mM MgSO4, 1 mM ascorbic acid and 5 mM glucose) containing 0.001–10,000 nM of the inhibitor. [3H]5-HT was added to the cells and uptake was stopped by washing cells rapidly three times with uptake buffer. Cells were solubilized with 1% Triton-X100, followed by the addition of 200 μl of scintillation fluid to each well. The amount of labelled 5-HT was measured using a MicroBeta scintillation counter. Data were fit to a sigmoidal dose-response curve.
