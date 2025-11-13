# Shank promotes action potential repolarization by recruiting BK channels to calcium microdomains

## Authors

- Luna Gao<sup>1</sup>
- Jian Zhao<sup>1</sup>
- Evan Ardiel<sup>1</sup>
- Qi Hall<sup>1</sup>
- Stephen Nurrish<sup>1</sup> ([ORCID: 0000-0002-2653-9384](https://orcid.org/0000-0002-2653-9384))
- Joshua M Kaplan<sup>1</sup> ([ORCID: 0000-0001-7418-7179](https://orcid.org/0000-0001-7418-7179)) †

### Affiliations

1. Department of Molecular Biology, Massachusetts General Hospital Boston United States ([ROR:002pd6e78](https://ror.org/002pd6e78))
2. Department of Neurobiology, Harvard Medical School Boston United States ([ROR:03vek6s52](https://ror.org/03vek6s52))
3. Program in Neuroscience, Harvard Medical School Boston United States ([ROR:03vek6s52](https://ror.org/03vek6s52))

† Corresponding author

## Abstract

Mutations altering the scaffolding protein Shank are linked to several psychiatric disorders, and to synaptic and behavioral defects in mice. Among its many binding partners, Shank directly binds CaV1 voltage activated calcium channels. Here, we show that the Caenorhabditis elegans SHN-1/Shank promotes CaV1 coupling to calcium activated potassium channels. Mutations inactivating SHN-1, and those preventing SHN-1 binding to EGL-19/CaV1 all increase action potential durations in body muscles. Action potential repolarization is mediated by two classes of potassium channels: SHK-1/KCNA and SLO-1 and SLO-2 BK channels. BK channels are calcium-dependent, and their activation requires tight coupling to EGL-19/CaV1 channels. SHN-1’s effects on AP duration are mediated by changes in BK channels. In shn-1 mutants, SLO-2 currents and channel clustering are significantly decreased in both body muscles and neurons. Finally, increased and decreased shn-1 gene copy number produce similar changes in AP width and SLO-2 current. Collectively, these results suggest that an important function of Shank is to promote microdomain coupling of BK with CaV1.

## Introduction

Shank is a synaptic scaffolding protein (containing SH3, PDZ, proline-rich and SAM domains) (Grabrucker et al., 2011). Mammals have three Shank genes, each encoding multiple isoforms (Jiang and Ehlers, 2013). Several mouse Shank knockouts have been described but these mutants exhibit inconsistent (often contradictory) synaptic and behavioral defects (Jiang and Ehlers, 2013), most likely resulting from differences in the Shank isoforms impacted by each mutation. The biochemical mechanism by which Shank mutations alter synaptic function and behavior has not been determined.

In humans, Shank mutations and CNVs are linked to Autism Spectrum Disorders (ASD), schizophrenia, and mania (Durand et al., 2007; Peça et al., 2011). Haploinsufficiency for 22q13 (which spans the Shank3 locus) occurs in Phelan-McDermid syndrome (PMS), a syndromic form of ASD (Phelan and McDermid, 2012). PMS patients exhibit autistic behaviors accompanied by hypotonia, delayed speech, and intellectual disability (ID) (Bonaglia et al., 2011). Heterozygous inactivating Shank3 mutations are found in sporadic ASD and schizophrenia (Durand et al., 2007; Peça et al., 2011). A parallel set of genetic studies suggest that increased Shank3 function also contributes to psychiatric diseases. 22q13 duplications spanning Shank3 are found in ASD, schizophrenia, ADHD, and bipolar disorder (Durand et al., 2007; Failla et al., 2007; Han et al., 2013). A transgenic mouse that selectively over-expresses Shank3 exhibits hyperactive behavior and susceptibility to seizures (Han et al., 2013). Taken together, these studies suggest that too little or too much Shank3 can contribute to the pathophysiology underlying these psychiatric disorders.

Given its link to psychiatric disorders, there is great interest in determining how Shank regulates circuit development and function. Shank is highly enriched in the post-synaptic densities of excitatory synapses; consequently, most studies have focused on the idea that Shank proteins regulate some aspect of synapse formation or function. Through its various domains, Shank proteins bind many proteins (Lee et al., 2011; Sakai et al., 2011), thereby potentially altering diverse cellular functions. Shank proteins have been implicated in activity induced gene transcription (Perfitt et al., 2020; Pym et al., 2017), synaptic transmission (Zhou et al., 2016), synapse maturation (Harris et al., 2016), synaptic homeostasis (Tatavarty et al., 2020), cytoskeletal remodeling (Lilja et al., 2017), and sleep (Ingiosi et al., 2019). Each of these defects could contribute to the neurodevelopmental and cognitive deficits observed in ASD and schizophrenia.

Several recent studies suggest that an important function of Shank is to regulate the subcellular localization of ion channels. Shank mutations decrease the synaptic localization of NMDA and AMPA type glutamate receptors (Peça et al., 2011; Won et al., 2012). Other studies show that Shank proteins promote delivery of several ion channels to the plasma membrane, including HCN channels (Yi et al., 2016; Zhu et al., 2018), TRPV channels (Han et al., 2016), and CaV1 voltage activated calcium channels (Pym et al., 2017; Wang et al., 2017). Of these potential binding partners, we focus on CaV1 because human CACNA1C (which encodes a CaV1 α-subunit) is mutated in Timothy Syndrome (TS), a rare monogenic form of ASD (Splawski et al., 2005; Splawski et al., 2004), and polymorphisms linked to CACNA1C are associated with multiple psychiatric disorders (Psychiatric Genomics, 2013). For this reason, we asked how Shank regulates the coupling of CaV1 channels to their downstream effectors.

C. elegans has a single Shank gene, shn-1. The SHN-1 protein lacks an SH3 domain but has all other domains found in mammalian Shank proteins. Mammalian Shank proteins directly bind CaV1 channels through both the SH3 and PDZ domains (Zhang et al., 2005). We previously showed that the SHN-1 PDZ domain directly binds to a carboxy-terminal ligand in EGL-19/CaV1 (Pym et al., 2017). CaV1 channels are tightly coupled to multiple downstream calcium activated pathways. C. elegans and mouse Shank proteins have been shown to promote CaV1-mediated activation of the transcription factor CREB (Perfitt et al., 2020; Pym et al., 2017).

Here, we test the idea that SHN-1 regulates CaV1 coupling to a second effector, calcium activated potassium currents (which are mediated by BK channels). BK channels are activated by both membrane depolarization and by cytoplasmic calcium. At resting cytoplasmic calcium levels (~100 nM), BK channels have extremely low open probability. Following depolarization, cytoplasmic calcium rises thereby activating BK channels. BK channels bind calcium with a Kd ranging from 1 to 10 μM (Contreras et al., 2013); consequently, efficient BK channel activation requires tight spatial coupling to voltage activated calcium (CaV) channels. BK channels associate with all classes of CaV channels (Berkefeld et al., 2006). The co-clustering of BK and CaV channels allows rapid activation of hyperpolarizing potassium currents following depolarization. BK channels decrease action potential (AP) durations, promote rapid after hyperpolarization potentials, decrease the duration of calcium entry, and limit secretion of neurotransmitters and hormones in neurons and muscles (Adams et al., 1982; Edgerton and Reinhart, 2003; Petersen and Maruyama, 1984; Storm, 1987). Thus, BK channels have profound effects on circuit activity.

C. elegans has two BK channel subunits (SLO-1 and SLO-2), both of which form calcium and voltage dependent potassium channels when heterologously expressed (Wang et al., 2001; Yuan et al., 2000). SLO-2 channels are also activated by cytoplasmic chloride (Yuan et al., 2000). As in mammals, neuronal SLO-1 and –2 channels inhibit neurotransmitter release (Liu et al., 2014; Liu et al., 2007; Sancar et al., 2011), presumably via their coupling to UNC-2/CaV2 and EGL-19/CaV1. In body muscles, SLO-1 channels are co-localized with EGL-19/CaV1 channels and regulate muscle excitability and behavior (Kim et al., 2009). Here we show that SHN-1 promotes BK coupling to EGL-19/CaV1 channels, thereby decreasing AP duration.

## Results

### SHN-1 acts in muscles to regulate action potential duration

EGL-19/CaV1 channels mediate the primary depolarizing current during body muscle APs (Jospin et al., 2002; Liu et al., 2011). Because SHN-1 directly binds EGL-19 (Pym et al., 2017), we asked if SHN-1 regulates muscle AP firing patterns. In WT animals, body muscles exhibit a pattern of spontaneous AP bursts (~10 APs/burst; burst frequency 0.1 Hz) (Figure 1A). Within a burst, APs became progressively wider (Figure 1B). A similar pattern of progressive AP broadening during burst firing has been reported for many neurons (Geiger and Jonas, 2000; Jackson et al., 1991). Outward potassium currents were progressively decreased during repetitive depolarization (Figure 1C), suggesting that progressive AP broadening most likely results from accumulation of inactivated potassium channels during bursts, as seen in other cell types (Geiger and Jonas, 2000; Kole et al., 2007). Occasionally, WT muscles also exhibited prolonged depolarizations ( > 150ms), which are hereafter designated plateau potentials (PPs). PPs often occur at the end of an AP burst (Figure 1A).

![Figure 1.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig1-v2.jpg)

**Figure 1.:** (A) Representative traces of spontaneous muscle APs are shown for WT and shn-1(nu712 null) mutants. APs occur in bursts of ~10 APs/ burst. Plateau potentials (PPs), defined as transients lasting >150ms, are observed less frequently, often at the end of a burst. (B) APs become progressively longer during bursts. Successive APs taken from a representative burst are shown. (C) Repetitive depolarization to +30 mV leads to a progressive decrease in potassium currents. A representative recording from a WT animal is shown. This likely results from an accumulation of inactivated potassium channels during repetitive stimulation. (D–I) Mean PP rate (D), AP rate (E), AP width (F), RMP (G), AP amplitude (H), and input resistance (Rin, I) are compared in WT and shn-1 null mutants. All shn-1 data were obtained from shn-1(nu712) except for Rin (I), which were from shn-1(tm488). Values that differ significantly from wild type controls are indicated (ns, not significant; *, p < 0.05; **, p < 0.01; ***, p < 0.001). Error bars indicate SEM.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Endogenous SHN-1 is broadly expressed, including in neurons, muscles, skin, and glia. A representative image of reconstituted fluorescence produced by shn-1(nu600 GFP11) and eft-3>GFP1-10 (left) and the corresponding bright field image (right) are shown. Pharyngeal muscles (Ph mm) are indicated in the bright field image. SHN-1(GFP11) expression in body muscles was not detected, consistent with the very low shn-1 mRNA levels reported in body muscles (Cao et al., 2017; Packer et al., 2019). Scale bar indicates 14 μm.

In shn-1 null mutants, PP rate and AP widths were significantly increased, AP amplitudes were decreased, resting membrane potential (RMP) was depolarized, while AP frequency and input resistance were unaltered (Figure 1D–I). Similar increases in AP widths and PP rate were observed in three, independently derived shn-1 null mutants (nu712, nu652, and tm488) (Table 1). Single-cell RNA sequencing studies suggest that SHN-1 is expressed in muscles, neurons, glia, and epithelial cells (Cao et al., 2017; Packer et al., 2019), consistent with the broad expression of split GFP tagged shn-1(nu600 GFP11) (Figure 1—figure supplement 1). To determine if SHN-1 functions in body muscles to control AP duration, we edited the endogenous shn-1 locus to construct alleles that are either inactivated (nu697) or rescued (nu652) by the CRE recombinase (Figure 2A). Using these alleles, we found that AP widths and PP frequency were increased in shn-1(muscle Knockout, KO) and that this defect was eliminated in shn-1(muscle rescue) (Figure 2B–D). By contrast, shn-1(neuron KO) and shn-1(neuron rescue) had no effect on PP rate or AP widths (Figure 2C–D). Because CRE expression in muscles produced opposite changes in AP firing patterns in strains containing the shn-1 nu697 and nu652 alleles, these results are unlikely to be caused by toxicity associated with CRE expression (Speed et al., 2019). The PP rate and AP width defects observed in shn-1(muscle KO) were not significantly different from those in shn-1(null) (Figure 2—figure supplement 2). Collectively, these results suggest that SHN-1 acts in body muscles to control AP duration.

![Figure 2.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig2-v2.jpg)

**Figure 2.:** (A) A schematic of the shn-1 locus is shown. Open boxes indicate UTRs, black boxes indicate coding regions. Recombination sites mediating CRE induced deletions (LoxP) and inversions (FLEX) are indicated. The shn-1(nu697) allele allows CRE-induced shn-1 knockouts while shn-1(nu652) allows CRE-induced shn-1 rescue. In shn-1(nu652), an exon containing in frame stop codons was inserted into the second intron (in the ‘OFF’ orientation). This stop exon is bounded by FLEX sites. (B) Representative traces of spontaneous muscle APs are shown in shn-1(nu697) with and without muscle CRE expression. Mean PP rate (C) and AP width (D) are compared in the indicated shn-1 mutants without (-) and with CRE expression in muscles (m) or neurons (n). Sample sizes are as follows: shn-1(nu697) (17); shn-1(nu697) +muscle CRE (21); shn-1(nu697) +neuron CRE (15); shn-1(nu652) (18); shn-1(nu652) +muscle CRE (30); and shn-1(nu652) +neuron CRE (19). Values that differ significantly from wild-type controls are indicated (ns, not significant; *, p < 0.05; **, p < 0.01; ***, p < 0.001). Error bars indicate SEM. Representative traces for genotypes in panels C and D are shown in Figure 2—figure supplement 1.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Representative traces of spontaneous muscle APs are shown for the indicated genotypes.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Mean PP rate and AP width are compared in the indicated shn-1 mutants. Sample sizes are as follows: shn-1(nu712 null) (21); shn-1(nu697) +muscle CRE (21). Error bars indicate SEM. No significant differences were observed.

**Table 1.**
 Comparison of shn-1 null alleles.


<table>
  <thead>
    <tr>
      <th>Genotype:</th>
      <th>PP rate (Hz):</th>
      <th>AP width (ms):</th>
      <th>AP Amp. (mV):</th>
      <th>RMP (mV):</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>WT</td>
      <td>0.01 ± 0.00</td>
      <td>26.73 ± 1.98</td>
      <td>40.42 ± 0.77</td>
      <td>–12.61 ± 0.96</td>
    </tr>
    <tr>
      <td>shn-1(nu712)</td>
      <td>0.04 ± 0.01**</td>
      <td>42.28 ± 4.17***</td>
      <td>37.63 ± 0.83*</td>
      <td>–8.33 ± 0.72**</td>
    </tr>
    <tr>
      <td>shn-1(nu652)</td>
      <td>0.05 ± 0.02***</td>
      <td>58.06 ± 5.27***</td>
      <td>34.78 ± 0.92***</td>
      <td>–7.19 ± 0.99***</td>
    </tr>
    <tr>
      <td>shn-1(tm488)</td>
      <td>0.05 ± 0.01***</td>
      <td>49.06 ± 7.07***</td>
      <td>41.36 ± 1.64</td>
      <td>–12.06 ± 1.54</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_Mean, SEM, and significant differences from WT controls are indicated (*, P < 0.05; **, P < 0.01; ***, P < 0.001)._

### SHN-1 binding to EGL-19 promotes AP repolarization

Because SHN-1 has multiple binding partners, we sought to confirm that prolonged APs result from decreased SHN-1 binding to EGL-19. To address this question, we recorded APs in strains containing mutations that disrupt this interaction (Figure 3A). PP frequency was significantly increased by a deletion removing the EGL-19 carboxy-terminal PDZ ligand [egl-19(nu496 ΔVTTL)] (Figure 3B). AP widths were significantly increased by a deletion removing the SHN-1 PDZ domain [shn-1(nu542 ΔPDZ)] and by the egl-19(nu496 ΔVTTL) mutation (Figure 3C). Furthermore, the shn-1(nu712 null) and egl-19(nu496 ΔVTTL) mutations did not have additive effects on PP rate and AP widths in double mutants (Figure 3—figure supplement 2). Taken together, these results support the idea that SHN-1 binding to EGL-19/CaV1 accelerates AP repolarization.

![Figure 3.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig3-v2.jpg)

**Figure 3.:** (A) A schematic illustrating the binding interaction between EGL-19’s c-terminus and SHN-1’s PDZ domain is shown. (B–C) Mean PP rate and AP width are compared in the indicated genotypes. Representative traces are shown in Figure 3—figure supplement 1. Mutations deleting the SHN-1 PDZ domain (nu542 ΔPDZ) or those deleting EGL-19’s c-terminal PDZ ligand (nu496 ΔVTTL) were edited into the endogenous genes using CRISPR. These mutations significantly increased AP width, compared to WT controls. Sample sizes are as follows: WT (41), shn-1(nu542) (22), and egl-19(nu496) (22). Values that differ significantly from wild type controls are indicated (ns, not significant; *, p < 0.05; **, p < 0.01; ***, p < 0.001). Error bars indicate SEM.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Representative traces of spontaneous muscle APs are shown for the indicated genotypes.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Mean PP rate and AP width are compared in the indicated genotypes. Sample sizes are as follows: shn-1(nu712 null) (21); shn-1(nu712); egl-19(ΔVTTL) (15). Error bars indicate SEM. No significant differences were observed.

### AP repolarization is controlled by SHK-1 KCNA and SLO-1/2 BK channels

To investigate how SHN-1 controls AP duration, we first asked which potassium channels promote repolarization following APs. Prior studies showed that voltage-activated potassium currents in body muscles are mediated by SHK-1/KCNA and BK channels (Gao and Zhen, 2011; Liu et al., 2011). SHK-1 channel function can be assessed in recordings using an internal solution containing low chloride levels (hereafter IkloCl). IkloCl was nearly eliminated in shk-1 single mutants (Figure 4A–B). BK channel function can be assayed in recordings utilizing internal solutions with high chloride levels (hereafter IkhiCl), which activates SLO-2 channels (Yuan et al., 2000). IkhiCl was ~50% reduced in single mutants lacking either SLO-2 or SHK-1 and was eliminated in slo-2; shk-1 double mutants (Figure 4C–D). These results suggest that SHK-1/KCNA and SLO-2/BK are the primary channels promoting AP repolarization. Consistent with this idea, AP duration was significantly increased in mutants lacking SHK-1/KCNA (Figure 4E–F), as previously reported (Gao and Zhen, 2011; Liu et al., 2011).

![Figure 4.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig4-v2.jpg)

**Figure 4.:** (A–D) Muscle voltage activated potassium currents are mediated by SHK-1 and SLO-2. Voltage activated potassium currents were recorded using pipette solutions containing low (IkloCl, A–B) and high (IkhiCl, C–D) chloride concentrations. Representative traces (A,C) and mean current density (B,D) at +30 mV are shown. IkloCl is mediated by SHK-1 whereas SHK-1 and SLO-2 equally contribute to IkhiCl. (E–F) AP durations are significantly increased in mutants lacking SHK-1, SLO-1, and SLO-2 channels. The AP widths observed in slo-1; slo-2 double mutants were not significantly different from those found in slo-2 single mutants. Representative traces (E and Figure 4—figure supplement 1) and mean AP widths (F) are shown. Alleles used in this figure were: shk-1(ok1581), slo-1(js379), and slo-2(nf100). Sample sizes are as follows: in panel B, WT (5), slo-2 (7), and shk-1 (5); in panel D, WT (10), slo-2 (5), shk-1 (5), shk-1;slo-2 (6); in panel F, WT (16), slo-1 (13), slo-2 (14), slo-1; slo-2 (8), shk-1 (7). Values that differ significantly from wild type controls are indicated (ns, not significant; *, p < 0.05; **, p < 0.01; ***, p < 0.001). Error bars indicate SEM.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Representative traces of spontaneous muscle APs are shown for the indicated genotypes.

Contradictory results have been reported for AP firing patterns in slo-1 and slo-2 BK mutants (Gao and Zhen, 2011; Liu et al., 2011). These studies used intracellular solutions that alter BK channel function. In (Liu et al., 2011), an intracellular solution containing high chloride levels was used, thereby exaggerating SLO-2’s contribution to AP repolarization (Yuan et al., 2000). In (Gao and Zhen, 2011), an intracellular solution containing a fast calcium chelator (BAPTA) was used, which inhibits BK activation thereby minimizing their impact on APs. We re-investigated the effect of SLO channels on APs using intracellular solutions with low chloride and a slow calcium chelator (EGTA), finding that AP durations were increased to a similar extent in slo-1 and slo-2 single mutants (Figure 4E–F). Taken together, these results confirm that SHK-1/KCNA and SLO/BK are the primary channels promoting AP repolarization in body muscles.

### SLO-1 and SLO-2 function together to promote AP repolarization

SLO-1 and SLO-2 subunits are co-expressed in muscles and could potentially co-assemble to form heteromeric channels. To determine if channels containing both SLO-1 and SLO-2 regulate AP repolarization, we analyzed AP widths in slo-1; slo-2 double mutants. AP widths in slo-1; slo-2 double mutants were not significantly different from those found in the single mutants (Figure 4F). Because slo-1 and slo-2 mutations did not have additive effects on AP widths, these results support the idea that heteromeric SLO-1/2 channels mediate rapid repolarization of muscle APs.

We did several experiments to further test the idea that SLO-1 and SLO-2 function together in heteromeric channels. First, we recorded voltage-activated potassium current in body muscles and found that IkhiCl was modestly reduced in slo-1 mutants, was dramatically reduced in slo-2 mutants, and was not further reduced in slo-1; slo-2 double mutants (Figure 5A–B). These results suggest that IkhiCl is mediated by heteromeric channels (containing both SLO-1 and SLO-2 subunits) and by SLO-2 homomers.

![Figure 5.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig5-v2.jpg)

**Figure 5.:** (A–B) IkhiCl was significantly decreased in slo-1(js379) and slo-2(nf100) single mutants but was not further decreased in slo-1; slo-2 double mutants. Representative traces (A) and mean current density (B) at +30 mV are shown. Sample sizes for panel B: WT (15), slo-1 (9), slo-2 (12), slo-1;slo-2 (6). (C–F) Expression of split GFP tagged SLO-2 (C–D) and SLO-1 (E–F) was analyzed in body muscles. CRISPR alleles were constructed adding 7 copies of GFP11 to the endogenous slo-1 and slo-2 genes (Table 2) and fluorescence was reconstituted by expressing GFP1-10 in body muscles. Controls showing that the GFP11 tags had no effect on AP width, RMP, and potassium currents are shown in Figure 5—figure supplement 1. Representative images (C and E) and mean puncta intensity (D and F) are shown. SLO-2 puncta intensity was significantly decreased in slo-1(js379) mutants. SLO-1 puncta intensity was unaltered in slo-2(nf100) mutants. Sample sizes are as follows: in panel D, WT (38) and slo-1 (23); in panel F, WT (34) and slo-2 (19). Values that differ significantly from wild type controls are indicated (ns, not significant; *, p < 0.05; **, p < 0.01; ***, p < 0.001). Error bars indicate SEM. Scale bar indicates 4 μm.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** APs and potassium currents were analyzed in strains containing slo-1(nu678 GFP11) and slo-2(nu725 GFP11) together with the muscle>GFP1-10 transgene. Mean AP width (A), RMP (B), and IkhiCl current density (C) were not significantly different from WT controls. Sample sizes are as follows: in panels A and B, WT (25), slo-1(nu678) (15), and slo-2(nu725) (13); in panel C, WT (10), slo-1(nu678) (12), and slo-2(nu725) (6). Error bars indicate SEM.

As a final test of this idea, we asked if subcellular localization of SLO-1 and SLO-2 subunits requires expression of both subunits. For this analysis, endogenous SLO-1 and SLO-2 subunits were labeled with split GFP. Using CRISPR, we introduced the eleventh β-strand of GFP (GFP11) into the endogenous slo-1 and slo-2 genes and visualized their expression by expressing GFP1-10 in body muscles. Strains containing the GFP11 tagged alleles exhibited wild-type AP widths, RMP, and IkhiCl currents, indicating that the tag did not interfere with SLO channel function (Figure 5—figure supplement 1). Using these alleles, we find that SLO-2 puncta intensity was significantly reduced in slo-1 null mutants, indicating that channels containing SLO-2 subunits require SLO-1 for their trafficking (Figure 5C–D). By contrast, SLO-1 puncta intensity was unaffected in slo-2 mutants, suggesting that BK channels lacking SLO-2 were trafficked normally (Figure 5E–F). Collectively, these results suggest that rapid muscle repolarization following APs is mediated by SLO-1/2 heteromeric channels and by SLO-2 homomers. Two prior studies also suggested that SLO subunits form heteromeric channels when heterologously expressed in Xenopus oocytes. SLO-1 currents were inhibited by a dominant-negative SLO-2 construct (Yuan et al., 2000). Similarly, mammalian SLO2 subunits (KCNT1 and 2) co-assemble to form heteromeric channels (Chen et al., 2009). Our results suggest that endogenously expressed SLO subunits also form heteromeric channels in native tissues.

### SHN-1 controls AP duration through BK channels

SHN-1’s impact on AP duration could be mediated by changes in either SHK-1 or SLO channels. To determine if SHN-1 acts through SLO channels, we asked if slo-2 mutations block SHN-1’s effects on AP widths. Consistent with this idea, AP widths in slo-2 single mutants were not significantly different from those in slo-2 double mutants containing shn-1(nu712 null), shn-1(nu542 ΔPDZ), or egl-19(nu496 ΔVTTL) mutations (Figure 6A). These results suggest that SHN-1 controls AP duration by regulating SLO-2 channels.

![Figure 6.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig6-v2.jpg)

**Figure 6.:** (A) A slo-2 null mutation blocks the effect of SHN-1 on AP width. Mean AP widths in slo-2(nf100) double mutants containing shn-1(nu712 null), shn-1(nu542 ΔPDZ), and egl-19(nu496 ΔVTTL) mutations were not significantly different from those in slo-2 single mutants. Representative traces are shown in Figure 6—figure supplement 1A. Sample sizes: WT (41), slo-2 (14), slo-2;shn-1 (8), slo-2;ΔPDZ (8), and slo-2;ΔVTTL (10). (B–C) IkloCl currents were unaltered in shn-1(nu712 null) mutants. Representative traces (B) and mean current density at +30 mV (C) are shown. Sample sizes: WT (9) and shn-1 (10). These results show that SHK-1 channel function was unaffected in shn-1 mutants. (D–E) IkhiCl currents were significantly smaller in shn-1(nu712 null) and shn-1(nu542 ΔPDZ) mutants but were unaffected in egl-19(nu496 ΔVTTL) mutants. The effect of shn-1 mutations on IkhiCl was eliminated in double mutants lacking SLO-2, indicating that the SHN-1 sensitive potassium current is mediated by SLO-2. IkhiCl currents were recorded from adult body wall muscles of the indicated genotypes at holding potentials of –60 to +60 mV. Representative traces (D and Figure 6—figure supplement 1B) and mean current density at +30 mV (E) are shown. Sample sizes in panel E: WT (12), shn-1 (11), slo-2 (12), ΔPDZ (9), ΔVTTL (8), slo-2;shn-1 (6), slo-2;ΔPDZ (8), and slo-2;ΔVTTL (7). Values that differ significantly from wild type controls are indicated (ns, not significant; *, p < 0.05; **, p < 0.01; ***, p < 0.001). Error bars indicate SEM.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Representative traces of spontaneous muscle APs (A) and IkhiCl currents at +30 mV (B) are shown for the indicated genotypes.

To confirm that SHN-1 regulates SLO-2 channels, we analyzed potassium currents in shn-1 mutants. A shn-1 null mutation had no effect on IkloCl currents, indicating that SHK-1 function was unaffected (Figure 6B–C). By contrast, IkhiCl was ~30% reduced in shn-1 null mutants, ~ 50% reduced in slo-2 mutants, and was not further reduced in shn-1; slo-2 double mutants (Figure 6D–E). Lack of additivity in shn-1; slo-2 double mutants suggests that the SHN-1-sensitive potassium current was mediated by SLO-2. A similar decrease in IkhiCl current was observed in shn-1(nu542 ΔPDZ) mutants (Figure 6E). IkhiCl current was unaltered in egl-19(nu496 ΔVTTL) mutants, implying that SHN-1 binding to EGL-19’s carboxy terminus is not required for SLO-2 current (Figure 6E). Thus, shn-1 inactivation decreased SLO-1/2 BK current but had little or no effect on SHK-1 KCNA current; consequently, SHN-1 regulates AP widths by promoting activation of SLO-1/2 channels.

### SHN-1 promotes microdomain coupling of SLO-2 with EGL-19/CaV1 channels

BK channels bind calcium with affinities ranging from 1 to 10 μM (Contreras et al., 2013). As a result of this calcium dependence, BK channels have very low open probability at resting cytoplasmic calcium levels (~100 nM) and efficient BK activation typically requires close spatial coupling to calcium channels (Barrett et al., 1982). We next asked if body muscle BK channels are functionally coupled to EGL-19/CaV1 channels. Consistent with this idea, IkhiCl current was significantly decreased by nemadipine, an EGL-19/CaV1 antagonist (Figure 7A–B; Kwok et al., 2008). The inhibitory effect of nemadipine on IkhiCl was eliminated in slo-2 mutants (Figure 7A–B), suggesting that the nemadipine-sensitive potassium current was mediated by SLO-2.

![Figure 7.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig7-v2.jpg)

**Figure 7.:** (A–B) SLO-2 activation is functionally coupled to EGL-19. IkhiCl was significantly reduced by nemadipine (an EGL-19 antagonist). This inhibitory effect of nemadipine on IkhiCl was eliminated in slo-2(nf100) mutants, indicating that the nemadipine sensitive current is mediated by SLO-2. IkhiCl currents were recorded from adult body wall muscles of the indicated genotypes at holding potentials of –60 to +60 mV. Representative IkhiCl traces (A) and mean current density as a function of membrane potential (B) are shown. (C) SLO-2 activation requires microdomain coupling to EGL-19. IkhiCl currents recorded in BAPTA are significantly smaller than those in EGTA. The inhibitory effect of BAPTA was reduced in shn-1(nu712 null) mutants and was eliminated in slo-2(nf100) mutants, indicating that the BAPTA sensitive current is mediated by SLO-2. The ratio of IkhiCl current density at +30 mV recorded in BAPTA to the mean current density recorded in EGTA is plotted for the indicated genotypes. Representative traces are shown in Figure 7—figure supplement 1A. Sample sizes for panel C: WT (8), slo-2 (8), and shn-1 (10). (D–E) AP repolarization is mediated by microdomain activation of SLO-2. AP widths recorded in solutions containing BAPTA are wider than those recorded in EGTA. The effect of BAPTA on AP widths was reduced in shn-1(nu712 null) mutants and was eliminated in slo-2(nf100) mutants, indicating that BAPTA’s effect is mediated by SLO-2. Representative traces of WT muscle APs recorded in EGTA and BAPTA are shown (D). The ratio of AP widths recorded in BAPTA to the mean AP widths recorded in EGTA is plotted for the indicated genotypes (E). Representative traces for panel E are shown in Figure 7—figure supplement 1B. Sample sizes for panel E: WT (8), slo-2 (11), and shn-1 (10). (F–H) SLO-2(nu725 GFP11) is partially co-localized with EGL-19(nu722 Cherry11) in body muscles. GFP11 and Cherry11 fluorescence were reconstituted by expressing GFP1-10 and Cherry1-10 in body muscles. SLO-2 puncta intensity was significantly reduced in shn-1(nu712 null) mutants but was unaffected in shn-1(nu542 ΔPDZ) and egl-19(nu496 ΔVTTL) mutants. Representative images (F) and mean puncta intensity for SLO-2 (G) and EGL-19 (H) are shown. Sample sizes for panel G: slo-2(GFP11) single mutants (38), and double mutants containing the shn-1 (35), ΔPDZ (39), and ΔVTTL (18) mutations. Sample sizes for panel H: egl-19(Cherry11) single mutants (34) and shn-1; egl-19(Cherry11) double mutants (31). Values that differ significantly from wild type controls are indicated (ns, not significant; *, p < 0.05; **, p < 0.01; ***, p < 0.001). Error bars indicate SEM. Scale bar indicates 4 μm.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Representative traces of IkhiCl currents at +30 mV (A) and spontaneous muscle APs (B) are shown for the indicated genotypes and recording conditions.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** SLO-1(nu678 GFP11) and UNC-68(nu664 GFP11) puncta intensity in body muscles is compared in WT and shn-1(null) mutants. GFP11 fluorescence was reconstituted by expressing GFP1-10 in body muscles. Representative images (A and C) and mean puncta intensity (B and D) are shown. Sample sizes: slo-1(GFP11) single mutants (23); shn-1(nu712 null);slo-1(GFP11) double mutants (17); unc-68(GFP11) single mutants (20); and shn-1(tm488 null);unc-68(GFP11) double mutants (20). No significant differences were observed. Error bars indicate SEM. Scale bars indicate 4 μm.

Is EGL-19 coupling to SLO-2 mediated by microdomain signaling? To test this idea, we compared IkhiCl and AP widths recorded with intracellular solutions containing fast (BAPTA) and slow (EGTA) calcium chelators (Figure 7C–E). We found that IkhiCl recorded with BAPTA was significantly smaller than that recorded with EGTA (Figure 7C). Similarly, AP widths recorded with BAPTA were significantly longer than those recorded with EGTA (Figure 7D–E). The effect of BAPTA on IkhiCl and AP widths was eliminated in slo-2 mutants (Figure 7C and E), suggesting that the BAPTA sensitive potassium current is mediated by SLO-2. BAPTA’s effect on IkhiCl and AP widths was reduced but not eliminated in shn-1 mutants (Figure 7C and E), consistent with the partial loss of SLO-2 current in these mutants (Figure 6D–E). Taken together, these results suggest that SHN-1 promotes SLO-2 microdomain coupling to EGL-19/CaV1.

If BK channels are functionally coupled to EGL-19/CaV1, these channels should be co-localized. Endogenous SLO-2 channels (tagged with GFP11) were distributed in a punctate pattern on the muscle surface. A subset of the SLO-2 puncta co-localized with EGL-19/CaV1 channels (tagged with Cherry11), suggesting that EGL-19 nanocomplexes are heterogeneous (Figure 7F). SLO-2 puncta intensity was significantly reduced in shn-1 null mutants (Figure 7F–G), consistent with the decreased SLO-2 current observed in these mutants. By contrast, SLO-2 puncta intensity was unaltered in shn-1(nu542 ΔPDZ) and egl-19(nu496 ΔVTTL) mutants (Figure 7G), in which SHN-1 binding to EGL-19’s c-terminus is disrupted (Pym et al., 2017). Next, we asked if inactivating SHN-1 alters the localization of other muscle ion channels. SLO-1 puncta intensity was unaltered in shn-1 null mutants, indicating that BK channels lacking SLO-2 were trafficked normally (Figure 7—figure supplement 2A-B). In body muscles, EGL-19/CaV1 channels are extensively co-localized with calcium channels in the endoplasmic reticulum (ER), UNC-68/Ryanodine Receptors (RYR) (Piggott et al., 2021). However, the puncta intensity of endogenous EGL-19(Cherry11) and UNC-68(GFP11)/RYR in body muscles were unaltered in shn-1(null) mutants (Figure 7H and Figure 7—figure supplement 2C-D), suggesting that SHN-1 does not broadly regulate co-localization of ion channels at ER-plasma membrane junctional contacts. Collectively, these results suggest that SHN-1 stabilizes SLO-2 clusters in the plasma membrane and promotes activation of heteromeric SLO-1/2 channels by nearby calcium channels.

### EGL-19 to SLO-2 coupling is sensitive to shn-1 gene dose

Deletion and duplication of human shank genes are both associated with ASD, schizophrenia, and mania (Bonaglia et al., 2006; Durand et al., 2007; Failla et al., 2007; Gauthier et al., 2010; Han et al., 2013). These results suggest that Shank phenotypes relevant to psychiatric disorders should exhibit a similar sensitivity to Shank copy number. For this reason, we analyzed the effect of shn-1 gene dosage on IkhiCl and AP duration (Figure 8). We analyzed animals with 1 (nu712/+ heterozygotes), 2 (WT), and 4 (WT +2 single copy shn-1 transgenes) copies of shn-1. Compared to wild-type controls, AP duration was significantly increased (Figure 8A and B) while muscle IkhiCl was significantly decreased (Figure 8C and D) in animals containing 1 and 4 copies of shn-1. Thus, increased and decreased shn-1 gene dosage produced similar defects in AP duration and SLO-2 current.

![Figure 8.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig8-v2.jpg)

**Figure 8.:** The effect of shn-1 gene dosage on AP widths (A–B) and IkhiCl current (C–D) was analyzed. IkhiCl was significantly decreased while AP duration was significantly increased in animals containing 1 and 4 copies of shn-1 compared to WT controls (i.e. 2 copies). The following genotypes were analyzed: 1 copy of shn-1 [shn-1(nu712)/ + heterozygotes], 2 copies of shn-1 (WT) and 4 copies of shn-1 (nuSi26 homozygotes in wild-type). IkhiCl currents were recorded from adult body wall muscles of the indicated genotypes at holding potentials of –60 to +60 mV. Representative traces (A,C), mean AP width (B), and mean IkhiCl current density at +30 mV (D) are shown. Sample sizes: for panel B, 1 copy (8), 2 copies (21), and four copies (15); for panel D, 1 copy (8), 2 copies (15), and four copies (7). Significant differences are indicated (ns, not significant; *, p < 0.05; **, p < 0.01; ***, p < 0.001). Error bars indicate SEM.

### SHN-1 regulates BK channel activation in motor neurons

Thus far, our results suggest that SHN-1 promotes EGL-19 to SLO-2 coupling in muscles. We next asked if SHN-1 also promotes coupling in motor neurons. To test this idea, we analyzed IkhiCl in cholinergic motor neurons and found that it was significantly reduced in shn-1 null mutants (Figure 9A–C). The slo-2 and shn-1 mutations did not have additive effects on IkhiCl in double mutants, suggesting that the shn-1 mutation selectively decreases SLO-2 current in motor neurons (Figure 9A–C). Consistent with decreased SLO-2 currents, we observed a corresponding decrease in axonal SLO-2(nu725 GFP11) puncta fluorescence in shn-1 mutant motor neurons (Figure 9D–E). Thus, our results suggest that SHN-1 promotes EGL-19/CaV1 to SLO-2 coupling in both body muscles and cholinergic motor neurons.

![Figure 9.](https://cdn.elifesciences.org/articles/75140/elife-75140-fig9-v2.jpg)

**Figure 9.:** (A–B) IkhiCl currents in cholinergic motor neurons were significantly decreased in shn-1(nu712 null) mutants. IkhiCl currents were recorded from adult cholinergic motor neurons of the indicated genotypes at holding potentials of –60 to +60 mV. Representative traces (A), mean current density as a function of membrane potential (B), and mean current density at +30 mV (C) are shown. Sample sizes for panels B and C: WT (12), shn-1 (10), slo-2 (9), and shn-1; slo-2 (9). (D–E) SLO-2 puncta intensity in motor neuron axons was significantly decreased in shn-1(nu712 null) mutants. Representative images of SLO-2(nu725 GFP11) and a synaptic vesicle marker [UNC-57/Endophilin(mCherry)] in dorsal cord axons of DA/DB motor neurons are shown (D). GFP11 fluorescence was reconstituted with GFP1-10 expressed in DA/DB motor neurons (using the unc-129 promoter). Mean SLO-2 puncta intensity in axons is plotted (E). Sample sizes for panel E: WT (21) and shn-1 (25). Values that differ significantly from wild type controls are indicated (ns, not significant; *, p < 0.05; **, p < 0.01; ***, p < 0.001). Error bars indicate SEM. Scale bar indicates 2 μm.

## Discussion

Our results lead to six principal conclusions. First, we show that SHN-1 acts cell autonomously in muscles to promote rapid repolarization of APs. Second, heteromeric BK channels containing both SLO-1 and SLO-2 subunits promote AP repolarization. Third, SHN-1 limits AP duration by promoting BK channel activation. Fourth, shn-1 mutants have decreased SLO-2 channel clustering and decreased SLO-2 currents. Fifth, increased and decreased SHN-1 gene dosage produce similar defects in AP durations and SLO-2 currents. And sixth, SHN-1 also promotes SLO-2 activation in motor neurons. Below we discuss the significance of these findings.

### Shank as a regulator of ion channel density

Several recent studies suggest that an important function of Shank proteins is to regulate ion channel density and localization. Mutations inactivating Shank have been shown to decrease AMPA and NMDA receptor abundance and post-synaptic currents (Peça et al., 2011; Won et al., 2012), HCN channels (Yi et al., 2016; Zhu et al., 2018), TRPV channels (Han et al., 2016), and voltage-activated CaV1 calcium channels (Pym et al., 2017; Wang et al., 2017). Here, we show that Shank also regulates BK channel densities in C. elegans muscles and motor neurons. Collectively, these studies suggest that Shank proteins have the capacity to control localization of many ion channels, thereby shaping neuron and muscle excitability.

Shank regulation of BK channels could have broad effects on neuron and muscle function. In neurons, BK channels are functionally coupled to CaV channels in the soma and dendrites, thereby regulating AP firing patterns and somatodendritic calcium transients (Golding et al., 1999; Storm, 1987). In pre-synaptic terminals, BK channels limit the duration of calcium influx during APs, thereby decreasing neurotransmitter release (Griguoli et al., 2016; Yazejian et al., 2000). In muscles, BK channels regulate AP firing patterns, calcium influx during APs, and muscle contraction (Dopico et al., 2018; Latorre et al., 2017). Thus, Shank mutations could broadly alter neuron and muscle function via changes in CaV-BK coupling. It will be very interesting to determine if this new function for Shank is conserved in other animals, including humans.

### SHN-1 promotes microdomain coupling of CaV1 and BK channels

BK channel activation requires tight coupling to CaV channels (Berkefeld et al., 2006). Our results suggest that SHN-1 promotes CaV1-BK microdomain coupling. APs were prolonged in shn-1 (null), shn-1(ΔPDZ), and egl-19(ΔVTTL) mutants and in all cases these defects were eliminated in double mutants lacking SLO-2. Interestingly, although all impair SLO-2 mediated AP repolarization, these mutations had distinct effects on SLO-2 channels. SLO-2 currents were reduced in shn-1 (null) and shn-1(ΔPDZ) mutants but were unaffected in egl-19(ΔVTTL) mutants. SLO-2 puncta intensity was decreased in shn-1(null) mutants but was unaffected in shn-1(ΔPDZ) and egl-19(ΔVTTL) mutants. These differences suggest that these mutants comprise an allelic series for EGL-19 to SLO-2 coupling defects in the following hierarchy shn-1 (null) >shn-1(ΔPDZ) > egl-19(ΔVTTL) mutants. Based on these results, we propose that multiple protein interactions progressively tighten CaV-BK coupling. Specifically, we propose that: (1) multiple SHN-1 domains act together to promote SLO-2 coupling to EGL-19, accounting for the distinct phenotypes observed in shn-1(null) and shn-1(ΔPDZ) mutants; (2) SHN-1 promotes formation (or stability) of SLO-2 clusters in the plasma membrane, as indicated by decreased SLO-2 puncta intensity in shn-1(null) mutants; (3) beyond this trafficking function, SHN-1’s PDZ domain tightens SLO-2 coupling to nearby calcium channels, accounting for the smaller SLO-2 current but unaltered SLO-2 puncta intensity in shn-1(ΔPDZ) mutants; (4) SHN-1 PDZ binding to EGL-19’s c-terminus promotes rapid SLO-2 activation during APs, accounting for the increased AP width but unaltered SLO-2 current and puncta intensity in egl-19(ΔVTTL) mutants; and (5) SHN-1’s PDZ must bind multiple proteins (not just EGL-19) to promote SLO-2 activation, accounting for the different phenotypes found in in shn-1(ΔPDZ) and egl-19(ΔVTTL) mutants. Multivalent interactions between scaffolds and their client proteins may represent a general mechanism for promoting microdomain signaling. Although SHN-1 binds EGL-19, SHN-1 may not directly link EGL-19 to SLO/BK channels. Instead, SHN-1 may link EGL-19 to other proteins required for SLO channel localization, for example components of the dystrophin complex (Kim et al., 2009; Sancar et al., 2011).

### Implications for understanding neurodevelopmental disorders

Several studies suggest that Shank3 deletions and duplications are both linked to ASD and schizophrenia, suggesting that opposite changes in Shank3 levels produce similar or overlapping psychiatric phenotypes (Bonaglia et al., 2006; Durand et al., 2007; Failla et al., 2007; Gauthier et al., 2010; Han et al., 2013). It remains possible that more detailed analysis will reveal phenotypic differences between gain and loss of human Shank3. In either case, it is currently unclear how opposite changes in Shank3 levels produce psychiatric phenotypes. Different (potentially opposite) biochemical defects arising from decreased and increased Shank dosage could produce psychiatric traits, perhaps by circuit level mechanisms (Antoine et al., 2019; Peixoto et al., 2016). For example, Shank duplications and hemizygosity could act in different cells or circuits to produce psychiatric traits. Our results provide support for a second possibility. We find that increased and decreased shn-1 gene dosage produce similar cell autonomous CaV1-BK coupling defects. Two prior studies suggest that bidirectional changes in Shank produce similar defects in Wnt signaling and CaV1 current density (Harris et al., 2016; Pym et al., 2017). Collectively, these results suggest that some biochemical functions of Shank exhibit this unusual pattern of dose sensitivity and consequently could contribute to the pathophysiology of human Shankopathies (i.e. Shank3 mutations, CNVs, or PMS).

The role of human Shank in CaV1-BK coupling has not been tested. Nonetheless, it seems plausible that this new physiological function could contribute to neuropsychiatric or co-morbid phenotypes associated with human Shankopathies. Consistent with this idea, PMS and human KCNMA1/BK mutations are associated with several shared phenotypes including: autism, developmental delay, intellectual disability, hypotonia, seizures, and gastrointestinal defects (i.e. vomiting, constipation, or diarrhea) (Bailey et al., 2019; Laumonnier et al., 2006; Phelan and McDermid, 2012; Soorya et al., 2013; Witmer et al., 2019). Moreover, BK channels are regulated by two high confidence ASD genes (UBE3A and hnRNP U). BK channels are degraded by the ubiquitin ligase UBE3A (Sun et al., 2019), mutations in which cause Angelman’s syndrome. The RNA binding protein hnRNP U promotes translation of slo-2 mRNA (Liu et al., 2018). Collectively, these results support the idea that disrupted CaV1-BK channel coupling could play an important role in shankopathies and that BK channels may represent an important therapeutic target for treating these disorders.

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
      <td>Strain, strain background (C. elegans)</td>
      <td>N2 Bristol</td>
      <td>https://cgc.umn.edu/</td>
      <td>N2</td>
      <td>Wild-type reference</td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>slo-1(js379)</td>
      <td>Wang et al., 2001</td>
      <td>NM1968</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>slo-2(nf100)</td>
      <td>Santi et al., 2003</td>
      <td>LY100</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>slo-1(js379);slo-2(nf100)</td>
      <td>This paper</td>
      <td>KP10046</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shk-1(ok1581)</td>
      <td>Liu et al., 2011</td>
      <td>RB1392</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shk-1(ok1581);slo-2(nf100)</td>
      <td>This paper</td>
      <td>KP10879</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(tm488)</td>
      <td>Oh et al., 2011</td>
      <td>KP7032</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu712)</td>
      <td>This paper</td>
      <td>KP10151</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu697)</td>
      <td>This paper</td>
      <td>KP10082</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>nuSi26</td>
      <td>Pym et al., 2017</td>
      <td>KP7493</td>
      <td>Pmyo-3::shn-1A MOSSci</td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>nuSi572</td>
      <td>This paper</td>
      <td>KP10696</td>
      <td>Muscle CRE</td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>nuSi502</td>
      <td>This paper</td>
      <td>KP10497</td>
      <td>Pan neuron CRE</td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu697);nuSi572</td>
      <td>This paper</td>
      <td>KP10767</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu697);nuSi502</td>
      <td>This paper</td>
      <td>KP10768</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>nuSi205</td>
      <td>This paper</td>
      <td>KP9234</td>
      <td>Ubiquitous GFP1-10</td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu604 GFP11)</td>
      <td>This paper</td>
      <td>KP8587</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu652); nuSi205</td>
      <td>This paper</td>
      <td>KP9548</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>nuSi470</td>
      <td>This paper</td>
      <td>KP10393</td>
      <td>Muscle CRE</td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu652);nuSi470</td>
      <td>This paper</td>
      <td>KP10437</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu604);nusi205</td>
      <td>This paper</td>
      <td>KP9232</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu542ΔPDZ)</td>
      <td>This paper</td>
      <td>KP9898</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>egl-19(nu496ΔVTTL)</td>
      <td>Pym et al., 2017</td>
      <td>KP7992</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>egl-19(nu496);shn-1(tm488)</td>
      <td>Pym et al., 2017</td>
      <td>KP8046</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>nuSi144</td>
      <td>This paper</td>
      <td>KP9814</td>
      <td>muscle GFP1-10</td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>slo-2(nu725 GFP11)</td>
      <td>This paper</td>
      <td>KP10285</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>slo-2(nu725);nuSi144</td>
      <td>This paper</td>
      <td>KP10031</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu712); slo-2(nu725);nuSi144</td>
      <td>This paper</td>
      <td>KP10894</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu542); slo-2(nu725);nuSi144</td>
      <td>This paper</td>
      <td>KP10890</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>egl-19(nu496); slo-2(nu725);nuSi144</td>
      <td>This paper</td>
      <td>KP10891</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>slo-1(nu678 GFP11)</td>
      <td>This paper</td>
      <td>KP9826</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>slo-1(nu678);nuSi144</td>
      <td>This paper</td>
      <td>KP10030</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu712); slo-1(nu678);nuSi144</td>
      <td>This paper</td>
      <td>KP10892</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu712);slo-2(nf100)</td>
      <td>This paper</td>
      <td>KP10880</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu542);slo-2(nf100)</td>
      <td>This paper</td>
      <td>KP10881</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>egl-19(nu496);slo-2(nf100)</td>
      <td>This paper</td>
      <td>KP10882</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>nuSi458</td>
      <td>This paper</td>
      <td>KP10374</td>
      <td>muscle Cherry1-10 SL2 GFP1-10</td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>egl-19(nu722 Cherry11)</td>
      <td>This paper</td>
      <td>KP10230</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>slo-2(nu725);egl-19(nu722);nusi458</td>
      <td>This paper</td>
      <td>KP10816</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu712); slo-2(nu725);egl-19(nu722);nusi458</td>
      <td>This paper</td>
      <td>KP10816</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu712);vsIs48</td>
      <td>This paper</td>
      <td>KP10883</td>
      <td>vsIs48 is Punc-17::GFP</td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>slo-2(nf100);vsIs48</td>
      <td>This paper</td>
      <td>KP10884</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu712);slo-2(nf100);vsIs48</td>
      <td>This paper</td>
      <td>KP10885</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>slo-2(nu725);nuSi144</td>
      <td>This paper</td>
      <td>KP10886</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu712);slo-2(nu725);nusi144</td>
      <td>This paper</td>
      <td>KP10887</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>slo-1(nu678); slo-2(nf100); nuSi144</td>
      <td>This paper</td>
      <td>KP10895</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>slo-2(nu725); slo-1(js379);nuSi144</td>
      <td>This paper</td>
      <td>KP10896</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>slo-2(nu725);nuSi250</td>
      <td>This paper</td>
      <td>KP10897</td>
      <td>nuSi250 is Punc-129 GFP1-10</td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu712); slo-2(nu725 GFP11);nuSi250</td>
      <td>This paper</td>
      <td>KP10898</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>egl-19(nu496); shn-1(nu712)</td>
      <td>This paper</td>
      <td>KP10906</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>unc-68(nu664); nuSi144</td>
      <td>This paper</td>
      <td>KP9802</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>unc-68(nu664); shn-1(tm488); nuSi144</td>
      <td>This paper</td>
      <td>KP10040</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>shn-1(nu604,nu652); nuSi502</td>
      <td>This paper</td>
      <td>KP10907</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>OP50</td>
      <td>Brenner, 1974</td>
      <td>OP50</td>
      <td>Worm food</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>egl-19 residue 2</td>
      <td>This paper</td>
      <td>N/A</td>
      <td>TTACCTGACATGATGGACAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>shn-1 ∆PDZ 5'</td>
      <td>This paper</td>
      <td>N/A</td>
      <td>gtgattccacgtggtgtcaa</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>shn-1 ∆PDZ 3'</td>
      <td>This paper</td>
      <td>N/A</td>
      <td>gtagctgatatgagtagggg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>shn-1 intron one loxP insertion</td>
      <td>This paper</td>
      <td>N/A</td>
      <td>tcaatttcagAAGTTCCTTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>shn-1 3' UTR loxP insertion</td>
      <td>This paper</td>
      <td>N/A</td>
      <td>gaaaaggcatagaatcagtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>shn-1 intron two insertion for STOP cassette</td>
      <td>This paper</td>
      <td>N/A</td>
      <td>ggggaaagatatgcatctga</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>shn-1 residue 946 insertion</td>
      <td>This paper</td>
      <td>N/A</td>
      <td>CACATCTTCTCGAACGTCAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>slo-1 residue 1,121 insertion</td>
      <td>This paper</td>
      <td>N/A</td>
      <td>cccggctcgtactccagtcc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>slo-2 residue 1,092 insertion</td>
      <td>This paper</td>
      <td>N/A</td>
      <td>ctgcgtcttagaccccttct</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Pmyo-3::gfp1-10</td>
      <td>This paper</td>
      <td>KP#3,315</td>
      <td>muscle GFP1-10</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Peft-3::gfp1-10</td>
      <td>This paper</td>
      <td>KP#4,524</td>
      <td>ubiquitous GFP1-10</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Punc-129::gfp1-10</td>
      <td>This paper</td>
      <td>KP#4,525</td>
      <td>GFP1-10 in DA/B neurons</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Ppat-10 Cherry1-10 SL2 GFP 1-10</td>
      <td>This paper</td>
      <td>KP#4,526</td>
      <td>Cherry1-10 and GFP1-10 in muscles</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Pmyo-3::CRE</td>
      <td>This paper</td>
      <td>KP#4,527</td>
      <td>muscle CRE</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Psbt-1::CRE</td>
      <td>This paper</td>
      <td>KP#4,528</td>
      <td>Pan neuron CRE</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Peft-3::CRE</td>
      <td>This paper</td>
      <td>KP#4,529</td>
      <td>germline CRE</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Nemadipine-A</td>
      <td>Abcam</td>
      <td>ab145991</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB R2018a</td>
      <td>MATLAB</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji</td>
      <td>https://fiji.sc/</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ClampFit</td>
      <td>Molecular Devices</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism 9</td>
      <td>GraphPad</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Origin 2019</td>
      <td>OriginLab</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Adobe illustrator 2020</td>
      <td>Adobe</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
  </tbody>
</table>

### Strains

Strain maintenance and genetic manipulation were performed as described (Brenner, 1974). Animals were cultivated at room temperature (~22 °C) on agar nematode growth media seeded with OP50 bacteria. Alleles used in this study are described in Table 2 and are identified in each figure legend. All strains utilized are listed in the Key Resources Table. Transgenic animals were prepared by microinjection, and integrated transgenes were isolated following UV irradiation, as described (Dittman and Kaplan, 2006). Single copy transgenes were isolated by the MoSCI and miniMoS techniques (Frøkjaer-Jensen et al., 2008; Frøkjær-Jensen et al., 2014).

**Table 2.**
 Alleles used in this study.


<table>
  <thead>
    <tr>
      <th>Allele:</th>
      <th>Description:</th>
      <th>Reference:</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>shn-1(tm488)</td>
      <td>1537 nt deletion, frameshift at codon 118</td>
      <td colspan="2">Oh et al., 2011</td>
    </tr>
    <tr>
      <td>shn-1(nu697)</td>
      <td>LoxP sites in intron 1 and 3'UTR</td>
      <td colspan="2">This study</td>
    </tr>
    <tr>
      <td>shn-1(nu712)</td>
      <td>derived by germline CRE recombination of nu697</td>
      <td colspan="2">This study</td>
    </tr>
    <tr>
      <td>shn-1(nu652)</td>
      <td>stop cassette (flanked by FLEX sites) in intron two in "OFF" orientation</td>
      <td colspan="2">This study</td>
    </tr>
    <tr>
      <td>shn-1(nu600 GFP11)</td>
      <td>seven copies GFP11 inserted at codon 945 of SHN-1A</td>
      <td colspan="2">This study</td>
    </tr>
    <tr>
      <td>shn-1(nu542ΔPDZ)</td>
      <td>deletes aa 446–532 of SHN-1A</td>
      <td colspan="2">This study</td>
    </tr>
    <tr>
      <td>egl-19(nu722 Cherry11)</td>
      <td>six copies sfCherry11 inserted at codon 2</td>
      <td colspan="2">This study</td>
    </tr>
    <tr>
      <td>egl-19(nu496ΔVTTL)</td>
      <td>WT C-term PAENSSRQHDSRGGSQEDLLLVTTL replaced with PMIHAEDHKKSYF</td>
      <td colspan="2">Pym et al., 2017</td>
    </tr>
    <tr>
      <td>unc-68(nu664 GFP11)</td>
      <td>seven copies GFP11 inserted at codon 3,705 of UNC-68A</td>
      <td colspan="2">Piggott et al., 2021</td>
    </tr>
    <tr>
      <td>slo-2(nu725 GFP11)</td>
      <td>seven copies GFP11 inserted at codon 1,092 of SLO-2A</td>
      <td colspan="2">This study</td>
    </tr>
    <tr>
      <td>slo-1(nu678 GFP11)</td>
      <td>seven copies GFP11 inserted at codon 1,130 of SLO-1A</td>
      <td colspan="2">This study</td>
    </tr>
    <tr>
      <td>slo-1(js379)</td>
      <td>Q251stop</td>
      <td colspan="2">Wang et al., 2001</td>
    </tr>
    <tr>
      <td>slo-2(nf100)</td>
      <td>in frame deletion of aa 450–569</td>
      <td colspan="2">Santi et al., 2003</td>
    </tr>
    <tr>
      <td>shk-1(ok1581)</td>
      <td>P253stop</td>
      <td>Liu et al., 2011</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Shn-1 dosage experiments

Animals with different shn-1 copy numbers were constructed as follows: 0 copies, shn-1(nu712) homozygotes; one copy, unc-17::gfp (LX929) males were crossed with shn-1(nu712) homozygotes and gfp-expressing hermaphrodites were analyzed; two copies, WT were analyzed; four copies, WT animals homozygous for the single copy transgene expressing SHN-1A in body muscles (nuSi26). The nuSi26 transgene was described in our earlier study (Pym et al., 2017).

### CRISPR alleles

CRISPR alleles were isolated as described (Arribere et al., 2014). Briefly, we used unc-58 as a co-CRISPR selection to identify edited animals. Animals were injected with two guide RNAs (gRNAs) and two repair templates, one introducing an unc-58 gain of function mutation and a second modifying a gene of interest. Progeny exhibiting the unc-58(gf) uncoordinated phenotype were screened for successful editing of the second locus by PCR. Split GFP and split sfCherry constructs are described in Feng et al., 2017. MiniMOS inserts in which Pmyo-3 drives expression of either GFP1-10 (nuSi144) or sfCherry1-10 SL2 GFP1-10 (nuSi458) were created.

Tissue specific shn-1 knockout was performed by introducing LoxP sites into intron 1 and the 3’UTR of the endogenous locus, in shn-1(nu697), and expressing CRE in muscles (pat-10 promoter) or neurons (sbt-1 promoter). Tissue-specific shn-1 rescue was performed by introducing a stop cassette into intron 2 of shn-1 using CRISPR, creating the shn-1(nu652) allele. The stop cassette consists of a synthetic exon (containing a consensus splice acceptor sequence and stop codons in all reading frames) followed by a 3’ UTR and transcriptional terminator taken from the flp-28 gene (the 564 bp sequence just 3’ to the flp-28 stop codon). The stop cassette is flanked by FLEX sites (which are modified loxP sites that mediate CRE induced inversions) (Schnütgen and Ghyselinck, 2007). In this manner, orientation of the stop cassette within the shn-1 locus is controlled by CRE expression. Expression of shn-1 is reduced when the stop cassette is in the OFF configuration (i.e. the same orientation as shn-1) but is unaffected in the ON configuration (opposite orientation). The endogenous flp-28 gene is located in an intron of W07E11.1 (in the opposite orientation). Consequently, we reasoned that the flp-28 transcriptional terminator would interfere with shn-1 expression in an orientation selective manner. A similar strategy was previously described for conditional gene knockouts in Drosophila (Fisher et al., 2017).

### Fluorescence imaging

Worms were immobilized on 10% agarose pads with 0.3 µl of 0.1 µm diameter polystyrene microspheres (Polysciences 00876–15, 2.5% w/v suspension). Body muscles just anterior to the vulva were imaged. Images were taken with a Nikon A1R confocal, using a 60 X/1.49 NA oil objective, with Nyquist sampling. Image volumes spanning the muscle surface were collected (~10 planes/volume, 0.15 μm between planes, and 0.06 μm /pixel). Maximum intensity projections for each volume were auto-thresholded, and puncta were identified as round fluorescent objects (area >0.1 μm2), using analysis of particles. Mean fluorescent intensity in each punctum was analyzed in the raw images. All image analysis was done using FIJI.

### Electrophysiology

Whole-cell patch-clamp measurements were performed using a Axopatch 200B amplifier with pClamp 10 software (Molecular Devices). The data were sampled at 10 kHz and filtered at 5 kHz. All recordings were performed at room temperature (~19°C–21°C).

Muscle AP recordings- The bath solution contained (in mM): NaCl 140, KCl 5, CaCl2 5, MgCl2 5, dextrose 11 and HEPES 5 (pH 7.2, 320 mOsm). The pipette solution contained (in mM): Kgluconate 120, KOH 20, Tris 5, CaCl2 0.25, MgCl2 4, sucrose 36, EGTA 5 (or BAPTA 5), and Na2ATP 4 (pH 7.2, 323 mOsm). Spontaneous APs were recorded in current-clamp without current injection. Cell resistance (Rin) was measured following a 10 pA pulse injection. AP traces were analyzed in Matlab. APs were defined as depolarizations lasting <150ms. PPs were defined as depolarizations lasting >150ms.

K+ current recordings - The bath solution contained (in mM): NaCl 140, KCl 5, CaCl2 5, MgCl2 5, dextrose 11 and HEPES 5 (pH 7.2, 320 mOsm). For IkloCl recordings, the pipette solution contained (in mM): Kgluconate 120, KOH 20, Tris 5, CaCl2 0.25, MgCl2 4, sucrose 36, EGTA 5, and Na2ATP 4 (pH 7.2, 323 mOsm). For IkhiCl recordings, the pipette solution contained (in mM): KCl 120, KOH 20, Tris 5, CaCl2 0.25, MgCl2 4, sucrose 36, EGTA 5 (or BAPTA 5), and Na2ATP 4 (pH 7.2, 323 mOsm). The voltage-clamp protocol consisted of –60 mV for 50ms, –90 mV for 50ms, test voltage (from –60 mV to +60 mV) 150ms. The repetitive stimulus protocol was –20 mV for 50ms, + 30 mV for 50ms, which was repeated 20 times. In figures, we show outward currents evoked at +30 mV, which corresponds to the peak amplitude of muscle APs. In some recordings, EGL-19 channels were blocked by adding 5 μM nemadipine to the pipette solution. Patch clamp recording of IkhiCl in ACh motor neurons was done using solutions described above for the muscle recordings. ACh neurons were identified for patching by expression of an unc-17 transcriptional reporter (Punc-17::GFP).

### Statistical methods

For normally distributed data, significant differences were assessed with unpaired t tests (for two groups) or one way ANOVA with post-hoc Dunn’s multiple comparisons test (for >2 groups). For non-normal data, differences were assessed by Mann-Whitney (two groups) or Kruskal-Wallis test with post-hoc Dunn’s multiple comparisons test ( > 2 groups). Data graphing and statistics were performed in GraphPad Prism 9. No statistical method was used to select sample sizes. Data shown in each figure represent contemporaneous measurements from mutant and control animals over a period of 1–2 weeks. For electrophysiology, data points represent mean values for individual neuron or muscle recordings (which were considered biological replicates). For imaging studies, data points represent mean puncta fluorescence values in individual animals (which were considered biological replicates). All data obtained in each experiment were analyzed, without any exclusions.
