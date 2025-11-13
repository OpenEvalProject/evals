# Cryo-EM structures reveal high-resolution mechanism of a DNA polymerase sliding clamp loader

## Authors

- Christl Gaubitz<sup>1</sup> ([ORCID: 0000-0002-6047-9282](https://orcid.org/0000-0002-6047-9282))
- Xingchen Liu<sup>1</sup> ([ORCID: 0000-0002-9089-1761](https://orcid.org/0000-0002-9089-1761))
- Joshua Pajak<sup>1</sup> ([ORCID: 0000-0001-5781-0870](https://orcid.org/0000-0001-5781-0870))
- Nicholas P Stone<sup>1</sup> ([ORCID: 0000-0002-5869-0329](https://orcid.org/0000-0002-5869-0329))
- Janelle A Hayes<sup>1</sup>
- Gabriel Demo<sup>2</sup>
- Brian A Kelch<sup>1</sup> ([ORCID: 0000-0002-1369-6989](https://orcid.org/0000-0002-1369-6989)) †

### Affiliations

1. Department of Biochemistry and Molecular Biotechnology, University of Massachusetts Chan Medical School Worcester United States ([ROR:0464eyp60](https://ror.org/0464eyp60))
2. RNA Therapeutics Institute, University of Massachusetts Chan Medical School, Worcester MA & Central European Institute of Technology, Masaryk University Brno Czech Republic ([ROR:02j46qs45](https://ror.org/02j46qs45))

† Corresponding author

## Abstract

Sliding clamps are ring-shaped protein complexes that are integral to the DNA replication machinery of all life. Sliding clamps are opened and installed onto DNA by clamp loader AAA+ ATPase complexes. However, how a clamp loader opens and closes the sliding clamp around DNA is still unknown. Here, we describe structures of the Saccharomyces cerevisiae clamp loader Replication Factor C (RFC) bound to its cognate sliding clamp Proliferating Cell Nuclear Antigen (PCNA) en route to successful loading. RFC first binds to PCNA in a dynamic, closed conformation that blocks both ATPase activity and DNA binding. RFC then opens the PCNA ring through a large-scale ‘crab-claw’ expansion of both RFC and PCNA that explains how RFC prefers initial binding of PCNA over DNA. Next, the open RFC:PCNA complex binds DNA and interrogates the primer-template junction using a surprising base-flipping mechanism. Our structures indicate that initial PCNA opening and subsequent closure around DNA do not require ATP hydrolysis, but are driven by binding energy. ATP hydrolysis, which is necessary for RFC release, is triggered by interactions with both PCNA and DNA, explaining RFC’s switch-like ATPase activity. Our work reveals how a AAA+ machine undergoes dramatic conformational changes for achieving binding preference and substrate remodeling.

## Introduction

In all known cellular life, DNA replication is coordinated by ring-shaped sliding clamp proteins that wrap around DNA to activate DNA polymerases and other factors (Moldovan et al., 2007). Sliding clamps are regulated by their presence on DNA, which in turn is governed by clamp loaders that open the sliding clamp ring and place it onto DNA (Kelch, 2016). The clamp loader of eukaryotes Replication Factor C (RFC) installs the sliding clamp Proliferating Cell Nuclear Antigen (PCNA) in a coordinated and stepwise fashion (Kelch, 2016). First, RFC binds ATP, which is a prerequisite for tight binding to PCNA (Sakato et al., 2012a). Next, RFC binds to PCNA, and then opens the PCNA ring. This open ternary complex is now competent to bind to primer–template (p/t) DNA (double-stranded DNA with a single-stranded 5′ overhang). Primer–template binding to the ternary complex triggers ATP hydrolysis in the clamp loader, followed by sliding clamp closure and ultimately release of the clamp loader complex (Chen et al., 2009). Therefore, RFC has two macromolecular substrates, PCNA and p/t-DNA, that must bind sequentially. Yet how clamp loaders achieve this strict sequential order remains unknown.

Clamp loaders are members of the ATPases associated with various cellular activities (AAA+) family (Erzberger and Berger, 2006). Most members of this family function as ringed, homohexameric molecular motors that harvest energy from ATP to translocate substrates through their central pore (Jessop et al., 2021). However, clamp loaders are not motors but instead are ATP-dependent remodeling switches (Kelch, 2016). In contrast to typical AAA+ ATPases, clamp loaders are heteropentameric with the five different subunits called A–E (Figure 1A, B). Each subunit features a classic AAA+ ATPase module, which holds the ATP sandwiched between the Rossmann fold and Lid domain at the binding interface with the neighboring subunit. The AAA+ modules of every subunit are extended by collar domains, which tightly associate together into a flat disk, enabling dynamic interactions between the five AAA+ modules.

![Figure 1.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig1-v2.jpg)

**Figure 1.:** (A) RFC is composed of five different subunits (named A–E) that each consist of the AAA+ ATPase module and a collar domain. The nucleotide-binding site is sandwiched between the N-terminal Rossmann fold domain and the Lid domain of the ATPase module at the subunit interface. The ATPase module and a C-terminal extension of the A subunit called the A′-domain form the A-gate. (B) Domain organization of RFC subunits. (C) Clamp loading begins with binding of ATP to RFC, followed by PCNA binding. How PCNA is opened and DNA binds to the open RFC:PCNA complex is not known. DNA-binding triggers ATP hydrolysis, PCNA closure, and RFC ejection. Structures obtained prior for RFC:PCNA complexes are indicated (Bowman et al., 2004; Gaubitz et al., 2020).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Sodium dodecyl sulfate–polyacrylamide gel electrophoresis (SDS–PAGE) gel of purified RFC and PCNA after gel filtration. A fraction with stoichiometric amounts of RFC and PCNA was used for grid preparation. (B) Crosslinking of the RFC:PCNA at a concentration of 1 mM bis(sulfosuccinimidyl)suberate (BS3) led to the identification of intermolecular and intramolecular crosslinks in RFC, and are shown in schematic representation. 88% of the crosslinks mapped to RFC-A and no crosslinks in PCNA were detected, although PCNA was detected in the sample. (C) Local resolution of reconstructions (center) and a representative section of each complex subunit for each reconstruction. (D) Fourier shell correlation (FSC) curves for the two halves of the reconstructions as well as model vs map curves.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) A downfiltered micrograph taken on a Thermo Fisher Scientific Titan Krios with a Gatan K2 detector is displayed. (B) 2D class averages show different side views. (C) The 3D reference for refinement was generated ab initio with cisTEM (Grant et al., 2018). (D) The ab initio model was downfiltered to 50 Å and used as reference for 3D classification. The first round of classification was performed with the 2× binned particle stack. Further rounds of classification with the unbinned stack improved the resolution. 3D classification with local angular search further helped to improve the resolution of the reconstructions representing complexes with closed PCNA (blue).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) A downfiltered micrograph taken on a Thermo Fisher Scientific Titan Krios with a Gatan K3 detector is displayed. (B) 2D class averages show different side views. (C) Class Open1 of the dataset without DNA was downfiltered to 60 Å and used as reference for 3D classification. The first round of classification was performed with the 4× binned particle stack and the second round of classification with the 2× binned stack. Further classification with the unbinned stack with resolution limit and without alignment helped to separate different conformational states and improved the resolution.

In addition to the canonical AAA+ machinery, many clamp loaders contain an A′ domain that bridges the gap between the A and E subunits. The space between the A′ domain and the AAA+ domain of subunit A is the ‘A-gate’ (Figure 1C), which serves as the entry site for p/t-DNA binding. It was initially proposed that ATP-binding triggers the five AAA+ modules to form a spiral with a symmetrical pitch that matches the geometry of DNA and templates the open clamp (Bowman et al., 2004; Simonetta et al., 2009, Table 1). This symmetric, helical arrangement of the subunits results in a cracked interface between the A and E subunits, bridged by the A′ domain. As the A′ domain stretches away from the A subunit to maintain contact, the A-gate opens and permits p/t-DNA binding (Kelch et al., 2011). However, structures of the human and yeast RFC:PCNA complexes bound to ATP analog show a closed PCNA ring bound to RFC in an autoinhibited state, where the closed A-gate blocks the DNA binding (Bowman et al., 2004; Gaubitz et al., 2020, Table 1 ). Additionally, another element called the ‘E-plug’ reaches into RFC’s central chamber and sterically occludes DNA binding. This autoinhibited state of RFC bound to closed PCNA is likely the first intermediate in the clamp loading reaction (Gaubitz et al., 2020; Sakato et al., 2012a; Thompson et al., 2012).

**Table 1.**
 Clamp loader structures previously obtained for the various states in the clamp loading cycle.


<table>
  <thead>
    <tr>
      <th colspan="4">Clamp loader prior to clamp binding</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Species</td>
      <td>Composition</td>
      <td>Reference</td>
      <td>PDB accession number</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>Clamp loader alone</td>
      <td>Jeruzalmi et al., 2001a</td>
      <td>1JR3</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>Clamp loader, ADP</td>
      <td>Kazmirski et al., 2004</td>
      <td>1XXI</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>Clamp loader, ATP analog</td>
      <td>Kazmirski et al., 2004</td>
      <td>1XXH</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>Clamp loader, ATP analog, primer/template DNA</td>
      <td>Simonetta et al., 2009</td>
      <td>3GLF</td>
    </tr>
    <tr>
      <td colspan="4">Encounter complex of clamp loader bound to the closed clamp</td>
    </tr>
    <tr>
      <td>H. sapiens</td>
      <td>Clamp loader bound to the clamp, ATP analog</td>
      <td>Gaubitz et al., 2020</td>
      <td>6VVO</td>
    </tr>
    <tr>
      <td>S. cerevisiae</td>
      <td>Clamp loader bound to the closed clamp, ATP analog</td>
      <td>Bowman et al., 2004</td>
      <td>1SXJ</td>
    </tr>
    <tr>
      <td colspan="4">Clamp loader bound to the clamp and primer/template DNA</td>
    </tr>
    <tr>
      <td>T4 phage</td>
      <td>Clamp loader, open clamp, ATP analog, DNA</td>
      <td>Kelch et al., 2011</td>
      <td>3U60</td>
    </tr>
    <tr>
      <td>T4 phage</td>
      <td>Clamp loader, closed clamp, ATP analog, DNA</td>
      <td>Kelch et al., 2011</td>
      <td>3U5Z</td>
    </tr>
    <tr>
      <td>T4 phage</td>
      <td>Clamp loader, closed clamp, ATP analog, ADP, DNA</td>
      <td>Kelch et al., 2011</td>
      <td>3U61</td>
    </tr>
  </tbody>
</table>

The question remains: How does the clamp loader open the sliding clamp? This is perhaps the most important function of the clamp loader, yet clues as to how this process is achieved remain elusive (Figure 1C). The structure of the T4 phage loader bound to DNA and an open clamp indicated that the clamp adopts a right-handed spiral conformation that matches the helical pitch of DNA (Kelch et al., 2011). However, this structure represents the state after DNA is bound (Table 1), and does not address how the clamp ring is initially opened. Thus, the structure of a clamp loader bound to an open clamp without DNA has been sought after, as it will illuminate the opening process.

## Results

### Structures of RFC:PCNA complexes en route to DNA loading

To understand how RFC opens PCNA and subsequently binds DNA, we used single-particle cryo-EM to determine structures of full-length Saccharomyces cerevisiae RFC bound to PCNA and the slowly hydrolyzing ATP analog ATPγS in the presence and absence of primer–template (p/t) DNA. We reconstituted the complex from purified RFC and PCNA subcomplexes that were separately expressed in E. coli (Figure 1—figure supplement 1A). Full-length RFC is functional, as it has the expected ATPase activity profile (McNally et al., 2010) with PCNA and p/t-DNA synergistically activating ATP hydrolysis (Figure 6F).

To prevent particle denaturation during sample preparation for cryo-EM, we crosslinked DNA-free and DNA-bound complexes using the amine-reactive crosslinker bis(sulfosuccinimidyl)suberate (BS3). Mild crosslinking is frequently used to obtain high-resolution cryo-EM structures of labile complexes (Gerlach et al., 2018; Yoo et al., 2018; Gaubitz et al., 2020). Mass spectrometry of the DNA-free sample reveals that most crosslinks are intramolecular and map to the unresolved N- and C-termini of RFC1, with only a few detectable intermolecular crosslinks between RFC subunits (Figure 1—figure supplement 1B; Table 2). No significant crosslinks were observed between RFC and PCNA.

**Table 2.**
 List of BS3 crosslinks.


<table>
  <thead>
    <tr>
      <th>XlinkX score</th>
      <th>Type</th>
      <th># Crosslink spectral matches</th>
      <th>Sequence A</th>
      <th>Position A</th>
      <th>Sequence B</th>
      <th>Position B</th>
      <th>Protein A</th>
      <th>Protein B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>58,66</td>
      <td>Inter</td>
      <td>1</td>
      <td>[K]LHLPPGK</td>
      <td>100</td>
      <td>[K]LAATR</td>
      <td>274</td>
      <td>RFC4</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>58,64</td>
      <td>Inter</td>
      <td>3</td>
      <td>[K]LELNVVSSPYHLEITPSDMGNNDR</td>
      <td>82</td>
      <td>S[K]TLLNAGVK</td>
      <td>385</td>
      <td>RFC5</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>56,99</td>
      <td>Inter</td>
      <td>3</td>
      <td>[K]YVNTFMK</td>
      <td>285</td>
      <td>DIL[K]R</td>
      <td>220</td>
      <td>RFC2</td>
      <td>RFC5</td>
    </tr>
    <tr>
      <td>56,47</td>
      <td>Inter</td>
      <td>1</td>
      <td>NQI[K]DFASTR</td>
      <td>98</td>
      <td>[K]LAATR</td>
      <td>274</td>
      <td>RFC3</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>52,59</td>
      <td>Inter</td>
      <td>2</td>
      <td>E[K]VKNFAR</td>
      <td>109</td>
      <td>TME[K]YSK</td>
      <td>160</td>
      <td>RFC2</td>
      <td>RFC5</td>
    </tr>
    <tr>
      <td>50,97</td>
      <td>Inter</td>
      <td>1</td>
      <td>NQI[K]DFASTR</td>
      <td>98</td>
      <td>RPDANSI[K]SR</td>
      <td>484</td>
      <td>RFC3</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>48,17</td>
      <td>Inter</td>
      <td>1</td>
      <td>GASEALA[K]R</td>
      <td>182</td>
      <td>[K]IVKER</td>
      <td>269</td>
      <td>RFC1</td>
      <td>RFC5</td>
    </tr>
    <tr>
      <td>45,16</td>
      <td>Inter</td>
      <td>1</td>
      <td>YT[K]NTR</td>
      <td>139</td>
      <td>[K]EEER</td>
      <td>267</td>
      <td>RFC3</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>41,65</td>
      <td>Inter</td>
      <td>1</td>
      <td>[K]LEEQHNIATK</td>
      <td>249</td>
      <td>YT[K]NTR</td>
      <td>139</td>
      <td>RFC1</td>
      <td>RFC3</td>
    </tr>
    <tr>
      <td>91,6</td>
      <td>Intra</td>
      <td>3</td>
      <td>[K]LEEQHNIATK</td>
      <td>249</td>
      <td>RPDANSI[K]SR</td>
      <td>484</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>72,73</td>
      <td>Intra</td>
      <td>4</td>
      <td>EAELLV[K]KEEER</td>
      <td>266</td>
      <td>[K]LAATR</td>
      <td>274</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>71,87</td>
      <td>Intra</td>
      <td>12</td>
      <td>QLIAGMPAEGGDGEAAE[K]AR</td>
      <td>245</td>
      <td>R[K]LEEQHNIATK</td>
      <td>249</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>71,27</td>
      <td>Intra</td>
      <td>2</td>
      <td>E[K]FKLDPNVIDR</td>
      <td>495</td>
      <td>[K]LAATR</td>
      <td>274</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>71,03</td>
      <td>Intra</td>
      <td>1</td>
      <td>F[K]LDPNVIDR</td>
      <td>497</td>
      <td>[K]LAATR</td>
      <td>274</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>71,03</td>
      <td>Intra</td>
      <td>9</td>
      <td>[K]TSTPLILICNER</td>
      <td>446</td>
      <td>S[K]TLLNAGVK</td>
      <td>385</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>64</td>
      <td>Intra</td>
      <td>1</td>
      <td>EAELLV[K]KEEER</td>
      <td>266</td>
      <td>S[K]KLAATR</td>
      <td>273</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>62,71</td>
      <td>Intra</td>
      <td>1</td>
      <td>RPDANSI[K]SR</td>
      <td>484</td>
      <td>SA[K]YYR</td>
      <td>678</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>62,2</td>
      <td>Intra</td>
      <td>2</td>
      <td>YAPTNLQQVCGN[K]GSVMK</td>
      <td>314</td>
      <td>L[K]NWLANWENSKK</td>
      <td>321</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>61,3</td>
      <td>Intra</td>
      <td>4</td>
      <td>EAELLVK[K]EEERSK</td>
      <td>267</td>
      <td>[K]LAATR</td>
      <td>274</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>60,15</td>
      <td>Intra</td>
      <td>1</td>
      <td>FAFACNQSN[K]IIEPLQSR</td>
      <td>149</td>
      <td>VT[K]NLAQVK</td>
      <td>275</td>
      <td>RFC4</td>
      <td>RFC4</td>
    </tr>
    <tr>
      <td>60,15</td>
      <td>Intra</td>
      <td>3</td>
      <td>YS[K]LSDEDVLKR</td>
      <td>165</td>
      <td>VT[K]NLAQVK</td>
      <td>275</td>
      <td>RFC4</td>
      <td>RFC4</td>
    </tr>
    <tr>
      <td>58,98</td>
      <td>Intra</td>
      <td>1</td>
      <td>IPATV[K]SGFTR</td>
      <td>767</td>
      <td>HAG[K]DGSGVFR</td>
      <td>340</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>58,55</td>
      <td>Intra</td>
      <td>4</td>
      <td>GASEALA[K]R</td>
      <td>182</td>
      <td>VT[K]SISSK</td>
      <td>190</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>57,1</td>
      <td>Intra</td>
      <td>3</td>
      <td>RPDANSI[K]SR</td>
      <td>484</td>
      <td>[K]EEER</td>
      <td>267</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>56,99</td>
      <td>Intra</td>
      <td>1</td>
      <td>KLEEQHNIAT[K]EAELLVK</td>
      <td>259</td>
      <td>[K]EEER</td>
      <td>267</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>56,99</td>
      <td>Intra</td>
      <td>1</td>
      <td>DNVVREED[K]LWTVK</td>
      <td>296</td>
      <td>[K]EEER</td>
      <td>267</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>56,41</td>
      <td>Intra</td>
      <td>1</td>
      <td>[K]YNSMTHPVAIYR</td>
      <td>773</td>
      <td>LGTSTD[K]IGLR</td>
      <td>698</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>53,33</td>
      <td>Intra</td>
      <td>1</td>
      <td>Y[K]CVIINEANSLTK</td>
      <td>136</td>
      <td>L[K]IDVR</td>
      <td>69</td>
      <td>RFC5</td>
      <td>RFC5</td>
    </tr>
    <tr>
      <td>52,59</td>
      <td>Intra</td>
      <td>2</td>
      <td>[K]ASSPTVKPASSK</td>
      <td>77</td>
      <td>[K]TKPSSK</td>
      <td>90</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>52,59</td>
      <td>Intra</td>
      <td>2</td>
      <td>HAG[K]DGSGVFR</td>
      <td>340</td>
      <td>GSVM[K]LK</td>
      <td>319</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>52,59</td>
      <td>Intra</td>
      <td>2</td>
      <td>ASSPTV[K]PASSK</td>
      <td>84</td>
      <td>[K]TKPSSK</td>
      <td>90</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>51,79</td>
      <td>Intra</td>
      <td>2</td>
      <td>[K]LEEQHNIATK</td>
      <td>249</td>
      <td>[K]LAATR</td>
      <td>274</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>50,97</td>
      <td>Intra</td>
      <td>1</td>
      <td>[K]TATSKPGGSK</td>
      <td>845</td>
      <td>S[K]TLLNAGVK</td>
      <td>385</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>50,34</td>
      <td>Intra</td>
      <td>1</td>
      <td>KMPVSNVIDVSETPEGE[K]K</td>
      <td>68</td>
      <td>LPLPA[K]R</td>
      <td>75</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>49,59</td>
      <td>Intra</td>
      <td>4</td>
      <td>EKF[K]LDPNVIDR</td>
      <td>497</td>
      <td>RPDANSI[K]SR</td>
      <td>484</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>47,92</td>
      <td>Intra</td>
      <td>1</td>
      <td>LGTSTD[K]IGLR</td>
      <td>698</td>
      <td>[K]LAATR</td>
      <td>274</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>47,92</td>
      <td>Intra</td>
      <td>1</td>
      <td>S[K]TLLNAGVK</td>
      <td>385</td>
      <td>[K]LAATR</td>
      <td>274</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>47,92</td>
      <td>Intra</td>
      <td>1</td>
      <td>GASEALA[K]R</td>
      <td>182</td>
      <td>[K]LAATR</td>
      <td>274</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>47,85</td>
      <td>Intra</td>
      <td>2</td>
      <td>SISS[K]TSVVVLGDEAGPK</td>
      <td>195</td>
      <td>[K]LEEQHNIATK</td>
      <td>249</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>47,85</td>
      <td>Intra</td>
      <td>1</td>
      <td>[K]YNSMTHPVAIYR</td>
      <td>773</td>
      <td>[K]TATSKPGGSK</td>
      <td>845</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>46,57</td>
      <td>Intra</td>
      <td>4</td>
      <td>R[K]LEEQHNIATK</td>
      <td>249</td>
      <td>GASEALA[K]R</td>
      <td>182</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>46,35</td>
      <td>Intra</td>
      <td>1</td>
      <td>[K]ASSPTVKPASSK</td>
      <td>77</td>
      <td>VT[K]SISSK</td>
      <td>190</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>45,16</td>
      <td>Intra</td>
      <td>1</td>
      <td>YAPTNLQQVCGN[K]GSVMK</td>
      <td>314</td>
      <td>[K]EEER</td>
      <td>267</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>45,16</td>
      <td>Intra</td>
      <td>1</td>
      <td>E[K]FKLDPNVIDR</td>
      <td>495</td>
      <td>[K]EEER</td>
      <td>267</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>45,16</td>
      <td>Intra</td>
      <td>2</td>
      <td>[K]LEEQHNIATK</td>
      <td>249</td>
      <td>[K]EEER</td>
      <td>267</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>44,72</td>
      <td>Intra</td>
      <td>1</td>
      <td>E[K]FKLDPNVIDR</td>
      <td>495</td>
      <td>RPDANSI[K]SR</td>
      <td>484</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>44,45</td>
      <td>Intra</td>
      <td>1</td>
      <td>YAPTNLQQVCGN[K]GSVMK</td>
      <td>314</td>
      <td>[K]LEEQHNIATK</td>
      <td>249</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>44,14</td>
      <td>Intra</td>
      <td>2</td>
      <td>NLP[K]MRPFDR</td>
      <td>462</td>
      <td>S[K]TLLNAGVK</td>
      <td>385</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>44,14</td>
      <td>Intra</td>
      <td>1</td>
      <td>RPDANSI[K]SR</td>
      <td>484</td>
      <td>GASEALA[K]R</td>
      <td>182</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>44,12</td>
      <td>Intra</td>
      <td>1</td>
      <td>[K]LEEQHNIATK</td>
      <td>249</td>
      <td>[K]TKPSSK</td>
      <td>90</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>43,7</td>
      <td>Intra</td>
      <td>1</td>
      <td>NLP[K]MRPFDR</td>
      <td>462</td>
      <td>LGTSTD[K]IGLR</td>
      <td>698</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>43,7</td>
      <td>Intra</td>
      <td>1</td>
      <td>[K]YNSMTHPVAIYR</td>
      <td>773</td>
      <td>TATS[K]PGGSK</td>
      <td>850</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>41,98</td>
      <td>Intra</td>
      <td>2</td>
      <td>LGTSTD[K]IGLR</td>
      <td>698</td>
      <td>RPDANSI[K]SR</td>
      <td>484</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>41,98</td>
      <td>Intra</td>
      <td>1</td>
      <td>[K]LEEQHNIATK</td>
      <td>249</td>
      <td>F[K]LDPNVIDR</td>
      <td>497</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>41,98</td>
      <td>Intra</td>
      <td>1</td>
      <td>HAG[K]DGSGVFR</td>
      <td>340</td>
      <td>VT[K]SISSK</td>
      <td>190</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
    <tr>
      <td>41,94</td>
      <td>Intra</td>
      <td>1</td>
      <td>NQI[K]DFASTR</td>
      <td>98</td>
      <td>YT[K]NTR</td>
      <td>139</td>
      <td>RFC3</td>
      <td>RFC3</td>
    </tr>
    <tr>
      <td>40,95</td>
      <td>Intra</td>
      <td>1</td>
      <td>NLAQV[K]ESVR</td>
      <td>281</td>
      <td>IHKLNN[K]A</td>
      <td>322</td>
      <td>RFC4</td>
      <td>RFC4</td>
    </tr>
    <tr>
      <td>40,92</td>
      <td>Intra</td>
      <td>1</td>
      <td>KLPLPA[K]R</td>
      <td>75</td>
      <td>[K]EEER</td>
      <td>267</td>
      <td>RFC1</td>
      <td>RFC1</td>
    </tr>
  </tbody>
</table>

We imaged the RFC:PCNA complex with and without p/t-DNA using a 300 kV Titan Krios microscope (Figure 1—figure supplement 1C, D, Figure 2A. B, and Figure 3A, B; Table 3). 3D classification results in four well-defined reconstructions from the DNA-free sample, with overall resolutions ranging between 3.8 and 4.0 Å (Figure 1—figure supplement 2D). The dataset of the DNA-containing sample yielded several well-defined classes, with overall resolutions ranging between 3.3 and 3.5 Å (Figure 1—figure supplement 3C, Table 3). We focused on classes in which all subunits of RFC and PCNA are visible, although the N- and C-terminal regions of the A subunit lack clear density. The quality of the cryo-EM reconstructions readily permitted model building using the crystal structure as a template (Bowman et al., 2004; Figure 1—figure supplement 1C, D; Table 3).

![Figure 2.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig2-v2.jpg)

**Figure 2.:** (A) Cryo-EM maps of the three Autoinhibited conformations of the RFC:PCNA complex. PCNA tilts closer relative to RFC in Autoinhibited2. The subunit arrangement of the AAA+ module of Autoinhibited3 is changed slightly, which leads to a crack in the A-gate. (B) Top view on the contact sites of PCNA with RFC in the autoinhibited conformation. (C) Principal component analysis of all Autoinhibited particles reveals a rocking motion of PCNA relative to RFC. The Cα displacement of principal component 1 (PC1) is indicated by arrows, scaled down by a factor of 2. (D) Principal component analysis reveals a range of motions within the initial RFC:PCNA complex. Amplitude histogram of the first principal component (PC1) reveals a unimodal distribution of particles, suggesting that this state consists of related particles in continuous motion.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Side views of the atomic models of Autoinhibited1, the RFC:PCNA crystal structure (Bowman et al., 2004), and of the human RFC:PCNA complex show similarity. (B) Closeup of the nucleotide-binding sites. The cryo-EM map is shown in yellow overlaying the atomic model. The catalytically important Walker A lysine, Walker B glutamates, and trans-acting arginine fingers are shown. The arginine fingers are distant within the active sites of RFC-B,C,D in Autoinhibited1 and 2 and in RFC-B,D of Autoinhibited3, rendering these active sites inactive. For comparison, the nucleotide-binding sites in the atomic model of the RFC:PCNA crystal structure (PDB 1SXJ) are shown. Here, the SRC motif arginine fingers were mutated to glutamines. RFC-E is not catalytically competent and has ADP bound. The A′ domain does not donate trans-acting arginine fingers. (C) Top views on the AAA+ spiral of the T4 clamp loader, RFC:PCNA crystal structure and Autoinihibited1–3. The T4 clamp loader, which has DNA bound, is in an active conformation. Here, the rotation axes that relate the subunits are coincident with each other and the central axis of DNA. In contrast, the symmetry of the AAA+ spiral of RFC in the autoinhibited conformation is distorted, and the axes are skewed in all these structures.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Superpositions of Autoinhibited 1 and 2 and 1 and 3 highlight differences in the orientation of PCNA toward RFC as well as the opening of the A-gate. (B) The two masks used for the first multibody refinement define PCNA and RFC as separate rigid bodies. (C) Principal component (PC) analysis revealed the two most dominant motions with RFC and PCNA. (D) Amplitude histogram of PC2 is unimodal. (E) PC2 reveals a swiveling motion. The Cα displacement is indicated by modevector generated arrows, scaled down by a factor of 2. (F) The two masks used for the second multibody refinement were chosen to match domain boundaries determined with the ENM DynOmics server (Li et al., 2017) and to capture motion between the A′ and the AAA+ module of the A-gate. (G) PC analysis revealed two dominant motions. (H) Amplitude histogram of PC1 is unimodal. (I) Multibody refinement two also revealed rocking and swiveling as dominant motions.

![Figure 3.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig3-v2.jpg)

**Figure 3.:** (A) Cryo-EM map of RFC bound to an open PCNA ring. (B) PCNA is held open by contacts with all five subunits of RFC. (C) The Cα displacement from closed to open PCNA is indicated by arrows, scaled up by a factor of 4. (D) The AAA+ modules widen from the Autoinhibited state (gray) to an open spiral conformation. (E) Top view of the AAA+ spiral shows that the E-plug and A-gate block access to RFC’s central DNA-binding chamber in the Autoinhibited conformation but retract in the open conformation. RFC opens wide enough for DNA to directly enter the central chamber. (F) Top view of the Rossmann fold arrangement in the Autoinhibited conformation. The rotation axes that relate neighboring subunits are shown in different colors and are skewed, indicating asymmetric rotations which lead to gaps between the subunits. (G) The rotation axes overlay in the Open2 state of RFC, indicating a symmetric arrangement of the AAA+ spiral. Symmetrization closes the gaps, and results in an increased interaction area between neighboring subunits.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Top and side views of the cryo-EM map of RFC bound to open PCNA, which was obtained from the dataset without DNA. (B) Top and side views of the cryo-EM map of RFC bound to open PCNA obtained from the dataset with DNA. (C) Overlay of the two models for Open1 and Open2 shows that the two models strongly resemble each other. (D) Open1 superposed to Open2. Open2 is colored by RMSD. (E) Closeup of the nucleotide-binding sites in Open1 and in Open2. The cryo-EM map is shown in yellow overlaying the atomic model. Critical catalytic residues are shown as sticks. All active sites are occupied with ATPγS. (F) PCNA intrasubunit distortions that occur for opening. The Cα displacement is indicated by modevector-generated arrows, scaled up by a factor of 4.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Overview of interaction sites of RFC with PCNA in the autoinhibited conformation. The three PCNA subunits and RFC’s AAA + module are shown in a cartoon flattened onto the page. RFC-D and RFC-E are not in contact with PCNA. (B) Cartoon overview of interaction sites of RFC with PCNA in the open conformation. RFC-D and RFC-E now contact PCNA. (C) Closeup views of the RFC–PCNA interaction sites in Autoinhibited1 are shown, the rest is omitted for clarity. The contact between PCNA and RFC-A is mediated by a short helix and adjacent hydrophobic and aromatic residues that insert into PCNA’s hydrophobic pockets. This conformation is commonly seen in binding partners which contain a PCNA-interacting protein (PIP) motif or derived motifs. (D) Contacts of RFC-A and RFC-B with PCNA do not change significantly upon PCNA opening. The interaction of PCNA with RFC-C becomes more extensive, and RFC-D and RFC-E establish new contacts to PCNA. RFC-C and RFC-E insert into PCNA’s hydrophobic pocket but do not employ a PIP motif. The E-plug and A′ domain reinforce the interaction with PCNA.

**Table 3.**
 Cryo-EM data collection, processing, and model statistics.


<table>
  <thead>
    <tr>
      <th>Dataset</th>
      <th colspan="4">No DNA</th>
      <th colspan="3">DNA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Magnification</td>
      <td colspan="4">130,000</td>
      <td colspan="3">81,000</td>
    </tr>
    <tr>
      <td>Voltage (keV)</td>
      <td colspan="4">300</td>
      <td colspan="3">300</td>
    </tr>
    <tr>
      <td>Cumulative exposure(e−/Å 2)</td>
      <td colspan="4">49–51</td>
      <td colspan="3">40</td>
    </tr>
    <tr>
      <td>Detector</td>
      <td colspan="4">K2 Summit</td>
      <td colspan="3">K3</td>
    </tr>
    <tr>
      <td>Pixel size (Å)</td>
      <td colspan="4">1.059</td>
      <td colspan="3">1.06</td>
    </tr>
    <tr>
      <td>Defocus range (μm)</td>
      <td colspan="4">−1.1 to −2.4</td>
      <td colspan="3">−1.2 to −2.3</td>
    </tr>
    <tr>
      <td>Micrographs used (no.)</td>
      <td colspan="4">6109</td>
      <td colspan="3">4499</td>
    </tr>
    <tr>
      <td>Initial particle images (no.)</td>
      <td colspan="4">954,291</td>
      <td colspan="3">1,331,440</td>
    </tr>
    <tr>
      <td>Symmetry</td>
      <td colspan="7">C</td>
    </tr>
    <tr>
      <td>Class name</td>
      <td>Autoinhibited1</td>
      <td>Autoinhibited2</td>
      <td>Autoinhibited3</td>
      <td>Open1</td>
      <td>Open2</td>
      <td>DNA-open</td>
      <td>DNA-closed</td>
    </tr>
    <tr>
      <td>Final refined particles (no.)</td>
      <td>55,308</td>
      <td>68,227</td>
      <td>60,036</td>
      <td>46,069</td>
      <td>63,752</td>
      <td>46,300</td>
      <td>76,270</td>
    </tr>
    <tr>
      <td>Applied B factor (Å2)</td>
      <td>−100</td>
      <td>−159.352</td>
      <td>−163.938</td>
      <td>−100</td>
      <td>−106.457</td>
      <td>−105.857</td>
      <td>−105.313</td>
    </tr>
    <tr>
      <td>Map resolution(Å, FSC 0.143)</td>
      <td>3.8</td>
      <td>3.9</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>3.5</td>
      <td>3.4</td>
      <td>3.3</td>
    </tr>
    <tr>
      <td>Model-Map CC_mask</td>
      <td>0.78</td>
      <td>0.77</td>
      <td>0.77</td>
      <td>0.76</td>
      <td>0.78</td>
      <td>0.79</td>
      <td>0.77</td>
    </tr>
    <tr>
      <td>Bond lengths (Å), angles (°)</td>
      <td>0.002,0.585</td>
      <td>0.002,0.561</td>
      <td>0.002,0.558</td>
      <td>0.002,0.574</td>
      <td>0.002,0.542</td>
      <td>0.002,0.518</td>
      <td>0.002,0.523</td>
    </tr>
    <tr>
      <td>Ramachandran outliers, allowed, favored</td>
      <td>0.00,3.16, 96.84</td>
      <td>0.00,3.11, 96.89</td>
      <td>0.00,2.89, 97.11</td>
      <td>0.00,3.08, 96.92</td>
      <td>0.00,3.38, 96.62</td>
      <td>0.00,2.23, 97.77</td>
      <td>0.00,2.16, 97.84</td>
    </tr>
    <tr>
      <td>Poor rotamers (%),MolProbity score, Clashscore (all atoms)</td>
      <td>0.00,1.68,9.05</td>
      <td>0.00,1.68,9.42</td>
      <td>0.00,1.68,9.95</td>
      <td>0.00,1.67,9.26</td>
      <td>2.01,1.91,8.67</td>
      <td>1.09,1.54,8.44</td>
      <td>1.09,1.55,9.18</td>
    </tr>
    <tr>
      <td>Accession number,EMDB, PDB</td>
      <td>25568,7THJ</td>
      <td>25569,7TIC</td>
      <td>25614,7THV</td>
      <td>25615,7TKU</td>
      <td>25753,7TI8</td>
      <td>25616,7TIB</td>
      <td>25617, 7TID</td>
    </tr>
  </tbody>
</table>

### The initial complex of RFC:PCNA is dynamic

Three of the classes from the DNA-free sample are of RFC bound to closed PCNA in different conformational states (Figure 2). Overall, these structures resemble the previous yeast RFC:PCNA crystal structure and our recent cryo-EM structure of human RFC (hRFC):PCNA (Figure 2—figure supplement 1A; Bowman et al., 2004; Gaubitz et al., 2020). The PCNA ring is closed with only the A, B, and C subunits of RFC contacting PCNA (Figure 2B). The interaction area between clamp loader and clamp averages ~1940 Å2 across the three states. The nucleotide density in each of the four active sites is most consistent with the presence of ATPγS, although the density for the γ-phosphate analog in the D subunit is somewhat ambiguous due to low local resolution throughout this subunit. Nonetheless, the ATPase sites of the B, C, and D subunits are in an inactive state (Figure 2—figure supplement 1B), with the AAA+ spiral in the overtwisted state observed in the hRFC structure and the previous yeast RFC crystal structure (Figure 2—figure supplement 1C; Bowman et al., 2004; Gaubitz et al., 2020). Therefore, all three of these structures represent autoinhibited states of RFC (termed Autoinhibited1, Autoinhibited2, and Autoinhibited3). Because the Autoinhibited1, 2, and 3 states likely represent ATP-saturated configurations, we place these conformational states early in the clamp loading reaction.

The subunits in the AAA + spiral have a different tilt in each of the Autoinhibited states, thereby slightly altering the intersubunit interactions (Figure 2—figure supplement 1C). For instance, the Autoinhibited3 state exhibits a slightly cracked A-gate (but not open enough for DNA to pass through), whereas the A-gate is closed in the Autoinhibited1 and 2 states (Figure 2A, Figure 2—figure supplement 2A). Further, the AAA + modules of subunits C and D change their position into a more symmetric alignment with overlapping rotation axes relative to Autoinhibited1 and 2 (Figure 2—figure supplement 1C). On the other hand, the PCNA ring tilts ~19° relative to the RFC-D in the Autoinhibited2 state relative to the Autoinhibited1 and 3 states (Figure 2A, Figure 2—figure supplement 2A).

Despite these differences, the three Autoinhibited structures are very similar, and so we asked if these conformations represent distinct intermediates or if they are snapshots along a continuum of conformations. Therefore, we characterized the particles that contribute to the Autoinhibited states using multibody refinement (Figure 2—figure supplement 2B–I), a computational tool that allows modeling of macromolecular motion (Nakane et al., 2018). To examine motion between clamp and clamp loader, we defined RFC and PCNA as two independent rigid bodies (Figure 2—figure supplement 2B–E). This analysis revealed that the dominant motion is rocking of PCNA toward RFC, with the linker between the ATPase and collar domains serving as a hinge (Figure 2C, Video 1). Other motions include swiveling of the RFC spiral with RFC-D getting closer to PCNA (Figure 2—figure supplement 2E, Video 2). These results are not dependent on the particular mask used, as similar motions are observed using different masking strategies (Figure 2—figure supplement 2F–I). Principal component analysis of the multibody conformers revealed a unimodal distribution of particles along their eigenvalue (Figure 2D, Figure 2—figure supplement 2D,H). This unimodal distribution indicates that the three different observed cryo-EM class averages do not represent particles in discrete states, but rather snapshots along a continuum of motion. Thus, the autoinhibited state of RFC is conformationally heterogeneous, with the dominant motions driving RFC toward PCNA. We propose these motions represent an early phase of the transition toward opening of the PCNA ring.

![Video 1.](https://cdn.elifesciences.org/articles/74175/elife-74175-video1.mp4.jpg)

![Video 2.](https://cdn.elifesciences.org/articles/74175/elife-74175-video2.mp4.jpg)

### PCNA opening is coupled to large-scale expansion of RFC

Each of the two cryo-EM datasets revealed a class of RFC bound to open PCNA with no DNA bound (Figure 1—figure supplements 2D and 3C). To our knowledge, these are the first high-resolution structures of a clamp loader bound to an open clamp prior to DNA binding. Both reconstructions are highly similar (overall Cα RMSD is 0.74 Å, map to map correlation coefficient is ~0.85) and we refer to these structures as Open1 and Open2 (Figure 3—figure supplement 1A–D). PCNA forms a right-handed spiral with a ~20 Å opening that is wide enough for dsDNA to enter (Figure 3A, B). The PCNA ring opens primarily through in-plane rather than out-of-plane motions (in-plane ~19 Å and out-of-plane ~10 Å for Open2, Figure 3C). Each of the subunits of PCNA twists outward and toward RFC, with the largest distortion in subunit II (Figure 3—figure supplement 1F).

PCNA opens at the A-gate of RFC, disrupting the interaction between the first and third subunits of the PCNA ring (termed PCNA-I and PCNA-III, hereafter). The open PCNA ring is directly held by all five subunits of RFC, burying ~3800 Å2 of surface area, an approximate ~1860 Å2 increase over that of the Autoinhibited states (Figure 3B, Figure 3—figure supplement 2A, B). The RFC-C subunit shifts downward to interact much more tightly with PCNA-II, while PCNA also forms new interactions with RFC-D, RFC-E, and the A′ domain of RFC-A (Figure 3—figure supplement 2C, D). The overall interface is characterized by an alternating pattern of strong and weak interactions (strong: RFC-A, -C, and -E; weak: RFC-B, -D, and A′). The strong interactions are with the main partner binding pocket of PCNA, using a binding region that resembles a common motif for PCNA-interacting partners. Of these strong interfaces, RFC-A is the most substantial and RFC-E weakest; RFC-A contains a true PCNA interaction motif, while RFC-C and RFC-E’s motifs are increasingly degenerate. It is likely that the stronger interactions at the ‘bottom’ of the spiral allows the clamp loader to toggle between the closed and open states of PCNA without releasing RFC.

The AAA+ modules of RFC adopt a right-handed spiral whose periodicity matches that of the six contact sites on PCNA. The symmetry of the ATPase spiral can be visualized by the near perfect alignment of the rotation axes that relate adjacent AAA+ subunits (Figure 3F, G). The interfaces between adjacent AAA+ modules become tighter, bringing the catalytic arginine finger residue closer to the neighboring ATPase site and potentiating ATP hydrolysis. This observation explains the modest boost in ATP activity upon PCNA binding (Johnson et al., 2006; Figure 6F). However, similar to the Autoinhibited structures, all four active sites remain bound to ATP analog (Figure 3—figure supplement 1). Therefore, while opening is necessary to promote ATP hydrolysis by properly positioning the trans-acting arginine finger residues across the intersubunit interface, ATP hydrolysis is not necessary to drive the conformational change from Autoinhibited to Open and opening is likely not sufficient to stimulate ATP hydrolysis on its own.

In order to rupture the PCNA ring, the AAA+ spiral of RFC widens, opening the A-gate. RFC opens using a large hinge motion, pivoting around the B–C and C–D subunit interfaces (Figure 3D, E; Video 3). The RFC-E subunit uses its E-plug to bind PCNA, which pulls the A′ domain and E-plug up to 45 Å away from the AAA+ module. This reveals a large opening of the A-gate (at its most narrow, the A-gate is approximately 20 Å wide) (Figure 3E). p/t-DNA can therefore directly enter the open RFC:PCNA complex.

![Video 3.](https://cdn.elifesciences.org/articles/74175/elife-74175-video3.mp4.jpg)

Opening of the A-gate separates the RFC-A Lid and collar domains, inducing a fold-switching transition in the Lid domain. The majority of the last helix of the Lid (Helix α4; residues 541–546) unravels into a taut β-strand conformation (Figure 4A, B). The remaining residues in helix α4 (residues 536–542) shift forward, causing a major change in the core packing of the Lid domain. This ‘sliding spring’ motion leads to a ~11 Å helix displacement, whereby some residues, such as Leu 549, move up to 22 Å from their original position. The stretching of the RFC-A Lid opens a new pore between the A and B subunits (Figure 4B). We discuss the role of this pore in the next section.

![Figure 4.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig4-v2.jpg)

**Figure 4.:** (A) Helix 4 of the RFC-A subunit in Autoinhibited1 is shown in purple. (B) In the open conformation, Lid Helix four is displaced and partially unravels, whereby the packing arrangement of the hydrophobic core of the lid domain in RFC-A changes. Ile536 and Leu549 move ~13 and ~22 Å from their original position and a pore is formed between the RFC-A and RFC-B subunits.

### Structures of the RFC:PCNA complex bound to primer–template DNA

To reveal how RFC:PCNA binds and responds to DNA, we analyzed two classes that contain DNA-bound RFC:PCNA. One class shows PCNA in an open lock-washer shape, and the other has PCNA in a closed conformation. Therefore, we term these two states DNAPCNA-open and DNAPCNA-closed, respectively (Figure 5A–C). Both classes contain clear density for p/t-DNA: 18 basepairs of duplex DNA are bound inside the central chambers of RFC and PCNA, and 6 nucleotides of the ssDNA template extend through the A-gate, preventing its closure. The AAA+ spiral of RFC tracks the minor groove of dsDNA using a suite of residues that are conserved across all known clamp loaders to match the helical symmetry of DNA (Kelch et al., 2011; Simonetta et al., 2009).

![Figure 5.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig5-v2.jpg)

**Figure 5.:** (A) Schematic representation of the structure of RFC:PCNA bound to primer–template (p/t) DNA. (B) Cryo-EM map of RFC:PCNA bound to p/t-DNA and open PCNA (termed DNAPCNA-open). (C) Cryo-EM map of RFC:PCNA bound to p/t-DNA with closed PCNA (termed DNAPCNA-closed). (D) The E-plug inserts into the major groove and interacts with both strands of the p/t-DNA. (E) Top view of contact sites of RFC with PCNA. PCNA is held open by contacts with all five subunits in DNAPCNA-open. (F) In DNAPCNA-closed, the interaction between RFC-E and PCNA-III is lost.(G) Overview of structure of Open2. (H) Top view of the AAA+ spiral of DNAPCNA-open. Displacement vectors between Open2 and DNAPCNA-open are indicated by arrows, scaled up by a factor of 2. The AAA+ spiral constricts around DNA. (I) The AAA+ spiral of DNAPCNA-closed. Displacement vectors between DNAPCNA-open and DNAPCNA-closed indicate that the AAA+ spiral constricts further around DNA, leading to changes in ATPase sites.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) PCNA constriction in DNAPCNA-open and DNAPCNA-closed. Displacement vectors between Open2 and DNAPCNA-open are shown as green arrows, scaled by a factor of 4 (left). Displacement vectors between DNAPCNA-open and DNAPCNA-closed are shown as green arrows, scaled by a factor of 4 (right). Upon DNA binding, the PCNA lock-washer constricts in DNAPCNA-open, due to a motion at the NTD of PCNA-III. PCNA is closed in a puckered conformation in DNAPCNA-closed through constricting motions of PCNA-I and PCNA-III. (B) The overlay of the rotation axes in the open conformation of RFC is indicative for spiral symmetry. The tilt angles show that in the DNA-bound structures (DNAPCNA-open and DNAPCNA-closed), the rotation axes become more tilted upon PCNA closure, indicating that DNA binding and PCNA closure slightly disrupt the symmetric arrangement of the AAA+ spiral. (C) Closeup of the nucleotide-binding sites in DNAPCNA-open and DNAPCNA-closed. The cryo-EM map is shown in yellow overlaying the atomic model. Critical catalytic residues are shown as sticks. All active sites are occupied with ATPγS.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** In all cases, the active sites were aligned about their Walker A and Walker B motifs. (A) Comparing the active sites of Closed1 to Open2. (B) Comparing the active sites of Open2 to DNAPCNA-open. (C) Comparing the active sites of DNAPCNA-open to DNAPCNA-closed. The most substantial change occurs upon clamp opening (A), which brings the arginine fingers in the RFC B–D active sites close to the γ-phosphate. This change does not occur in RFC-A, whose hydrolysis is dispensable for clamp loading. After opening, DNA binding (B) and then clamp closure (C) do not change the active sites much, indicating that DNA binding does not stimulate hydrolysis by reorganizing the ATPase-binding interface.

The E-plug beta-hairpin slots into the major groove of the duplex region of p/t-DNA (Figure 5D). Conserved basic residues at the tip of the E-plug interact directly with both the template and primer strands. Therefore, the E-plug provides a mechanism for the RFC AAA+ spiral to recognize both strands of DNA, unlike the clamp loaders from E. coli and T4 phage, whose AAA+ spirals only interact with the template strand (Kelch et al., 2011; Simonetta et al., 2009). Moreover, this structure shows that the E-plug changes its role from blocking DNA binding (in the three Autoinhibited states) to one in which it directly supports DNA binding. This explains the nonintuitive effect on DNA binding we observed previously, where hRFC variants with a mutated E-plug bind DNA with equivalent affinity as WT-hRFC (Gaubitz et al., 2020).

In DNAPCNA-open, both RFC and PCNA broadly resemble the conformations seen in Open1 and Open2. The RFC A-gate is open, with all five subunits gripping PCNA in an open lock-washer shape. However, both RFC and PCNA constrict relative to the Open1 and Open2 structures (Figure 5G, H and Figure 5—figure supplement 1A, B). RFC constricts modestly, pivoting the E, D, and C subunits around a hinge at the B–C interface. PCNA constricts ~12 Å upon DNA binding, with most of this constriction occurring in subunit III of PCNA (Figure 5—figure supplement 1A). Subunit III of PCNA is held by the RFC-D and RFC-E subunits, although RFC-E grips PCNA less tightly in DNAPCNA-open (~3800 Å2 total RFC–PCNA interaction area for the Open1 and 2 structures vs ~3400 Å2 for DNAPCNA-open). Overall, the PCNA conformation is similar to that seen for the structure of the T4 phage clamp bound to clamp loader and p/t-DNA (Kelch et al., 2011).

The DNAPCNA-closed structure has a closed PCNA ring that is distorted from planarity. Upon closure, PCNA loses its interaction with the RFC-E subunit, but retains its interfaces with the other four RFC subunits (Figure 5E, F). The distortion of the PCNA ring is most prevalent in subunit III, which puckers to maintain its interaction with the RFC-D subunit (Figure 5—figure supplement 1A, B). Interestingly, the interaction between DNA and PCNA becomes more extensive upon PCNA closure (~50 vs 250 Å2). Conserved basic residues lining the inner pore of PCNA also interact directly with the duplex, as has been hypothesized previously (Liu et al., 2017; McNally et al., 2010). We propose that these interactions help to drive the closure of PCNA around DNA.

DNAPCNA-open and DNAPCNA-closed, just like the other states described herein, are in the fully ATP-bound state: ATPγS in the active sites of the A, B, C, and D subunits, and ADP in the nucleotide-binding site of the E subunit (Figure 5—figure supplement 1C). Therefore, these structures represent reaction intermediates following DNA binding but preceding ATP hydrolysis. Upon binding DNA, the AAA + spiral constricts (Figure 5H), primarily due to a hinge-like motion at the interface between RFC-C and RFC-B. The AAA + spiral constricts around an axis coincident with the DNA axis. Subsequent PCNA closure further exaggerates the constriction of the RFC AAA+ spiral (Figure 5I). Despite these movements, the position of the arginine finger within the ATPase active site does not change substantially (Figure 5—figure supplement 2). Thus, DNA binding likely stimulates ATP hydrolysis through another mode of action. One such proposed mode is repositioning a conserved arginine known as the switch residue, which in turn would activate the Walker B glutamate (Kelch et al., 2011; Kelch et al., 2012). However, we find that this residue is not in the position that was previously predicted to stimulate hydrolysis. Despite this, the active sites appear to be in the fully active state, with all of the catalytic machinery poised to hydrolyze ATP. We discuss the ramifications of this observation on the allosteric activation of RFC below.

### RFC flips the 3′ base of the primer strand

Unexpectedly, we observe that the 3′ nucleotide of the primer strand is melted in both DNA-bound RFC:PCNA structures, with the base flipped away from the rest of the duplex (Figure 6A, B). The basepair is disrupted by a ‘separation pin’ at the base of the RFC-A collar domain that wedges between the DNA strands (Figure 6B). The indole ring of Trp638 replaces the flipped 3′ base to maintain stacking interactions. The 3′ nucleotide is repositioned inside the pore formed by the unraveling of the RFC-A Lid domain upon opening of the A-gate; this site is closed in the Autoinhibited state (Figure 4). The flipped base stacks against the phenyl ring of Phe582. These residues are conserved in eukaryotic clamp loaders but are absent in bacterial, archaeal or phage clamp loaders (Figure 6—figure supplement 5A).

![Figure 6.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig6-v2.jpg)

**Figure 6.:** (A) The last nucleotide in the primer strand is separated from the duplex. (B) The collar of RFC-A contains a ‘separation pin’ with two critical residues (Trp638 and Phe582) that stabilize the flipping of the 3′ primer nucleotide into the pore between RFC-A and RFC-B. The cryo-EM map is shown in red mesh. (C) The primer strand of p/t-DNA contains 3′ nucleotide with a 2-aminopurine (2AP) base, an adenine analog that reports on base-pairing and base-stacking. 2AP fluorescence increases in the presence of ATPγS and RFC:PCNA to a higher level than in the unpaired 2AP-labeled primer strand. (D) The human RFC:PCNA complex also induces an increase in 2AP fluorescence emission, whereas the E. coli clamp loader, which does not flip the 3’ end of the primer (Simonetta et al., 2009), does not increase 2AP fluorescence. (E) Mutation of Phe582 and Trp638 reduces 2-AP fluorescence in the presence of ATPγS. (F) ATPase activity of the ‘separation pin’ mutants.The ATP hydrolysis rate of the RFC-W638G variant is significantly reduced compared to wild type in the presence of PCNA and DNA (p value from one-way ANOVA test: ****p ≤ 0.0001).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Fluorescence intensity traces for 375 nM of p/t APp=1 in the presence of RFC:PCNA with and without nucleotide or primer APp=1. (B) Placement of 2-aminopurine (2AP) at different positions. The fluorescence with p/t APp=1 in the presence of ATPγS and RFC:PCNA increases ~fourfold in relation to the sample without ATPγS, whereas placement of the oligo further away from the 3′OH end reduces the fluorescence increase to ~twofold. (C) Results from (Figure 6B) could be recapitulated using p/t-DNA with 2-AP in the template strand (t = 1). The E. coli clamp loader, which does not have a separation pin, does not change fluorescence in the presence of ATPγS. (D) ATPase activity of the ‘separation pin’ mutants. DNA-binding affinity and maximum ATP hydrolysis rate are reduced in RFCW638G. (E) The steady-state ATP hydrolysis rate of the RFC-W638G variant is significantly reduced compared to wild type (p value = 0.0005). The RFC-F582A variant binds DNA with similar affinity than wild type (p value = 0.0288). DNA-binding affinity for RFC-W638G is slightly reduced (p value <0.0001). Error bars reflect the standard deviation from three replicates. The asterisks correspond to p values from one-way ANOVA tests comparing variants to wild type, ‘ns’ = not significant p > 0.05, *p ≤ 0.05, **p ≤ 0.01, ***p ≤ 0.001, ****p ≤ 0.0001 .

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** (A) Cartoon depiction of different DNA substrates that were used to probe if the separation pin acts to discriminate different moieties at the primer–template junction. (B–D) Similar ATPase activity profiles of the wild type and the two separation pin variants indicate that the separation pin is not critical to discriminate between these DNA substrates. Error bars on these bar graphs reflect the standard deviation from three replicates. The asterisks on these graphs correspond to p values from one-way ANOVA tests comparing different DNA substrates with an unmodified primer–template junction (p/t-DNA): ‘ns’ = not significant p > 0.05, *p ≤ 0.05, **p ≤ 0.01, ***p ≤ 0.001, ****p ≤ 0.0001.

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** To directly assess the physiological role of the separation pin using yeast, we performed spot assays with strains that express either wild type RFC1 or the F582A or the W638G variant. The two variants and the wild type display similar colony sizes across a variety of conditions, including varying temperatures, UV radiation, and treatment with hydroxyurea (HU) or methyl methanesulfonate (MMS), indicating that there is no striking phenotype with the tested conditions.

![Figure 6—figure supplement 4.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig6-figsupp4-v2.jpg)

**Figure 6—figure supplement 4.:** (A) In the T4 and E. coli clamp loaders, the duplex p/t-DNA extends farther into the central chamber, enabling more substantial contacts with the B–E subunits compared to RFC. (B) Contribution of RFC subunits to DNA binding. RFC-A dominates contact with p/t-DNA when compared to other clamp loaders.

![Figure 6—figure supplement 5.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig6-figsupp5-v2.jpg)

**Figure 6—figure supplement 5.:** (A) The separation pin is conserved in RFC1 across eukaryotes. Sequence alignment shows the conservation of the ‘separation pin’ among five eukaryotic species. The conserved sequences are marked by blue boxes. The fully conserved residues are in white with a red background, the highly conserved residues are in red, and the less conserved ones are in black. F582 and W638 are pointed out by the blue arrow. (B) A potential separation pin in the Ctf18 clamp loader. The structure of yeast Ctf18 (blue) predicted by AlphaFold (Jumper et al., 2021; Varadi et al., 2022) is superposed onto collar domain of the DNAPCNA-open structure of yeast RFC (RFC1 in red, primer strand in yellow, and template strand in orange). Key residues of the RFC1 separation pin are highlighted (Phe 582, Gln 636, and Trp 638), as well as their predicted counterparts in Ctf18 (Glu427, Asn477, and Leu481). While the separation pin helical hairpin is likely conserved, the key residues that mediate base-flipping in RFC1 are not conserved.

To characterize base-flipping, we measured binding of DNA substrates containing the adenine analog 2-aminopurine (2AP). Fluorescence of 2AP is dependent on base-pairing (Frey et al., 1995; Jean and Hall, 2001): fluorescence is low when 2AP is base paired, but high in the free state. To monitor melting, we placed 2AP either at the 3′ end of the primer strand (APp=1) or at the corresponding site in the template strand (APt=1). Importantly, we find a dramatic increase in 2AP fluorescence that is dependent on addition of RFC, PCNA and ATP analog (Figure 6C, Figure 6—figure supplement 1A–C). The increase in 2AP fluorescence is not observed in the presence of ADP, which does not support DNA binding (Kelch et al., 2011; McNally et al., 2010). Placement of 2AP at the p = 2 or p = 3 position of the primer yields diminished fluorescence, suggesting that only the 3′ base is flipped (Figure 6—figure supplement 1B). Therefore, our 2AP experiments validate that RFC- and PCNA-dependent 3′ end melting occurs in solution. The human clamp loader, which has a similar separation pin as yeast RFC (Gaubitz et al., 2020), greatly enhances 2AP fluorescence. However, the E. coli clamp loader, which binds p/t-DNA but does not melt the primer strand (Simonetta et al., 2009), does not alter fluorescence (Figure 6D). Thus melting of the 3′ nucleotide is a conserved activity of eukaryotic clamp loaders, but is likely not used by bacterial clamp loaders.

To determine the mechanism and role of primer melting, we modified the p/t-DNA and/or key residues in the separation pin and assessed their effects on base-flipping, ATP hydrolysis, and DNA affinity. The W638G and F582A variants have attenuated base-flipping as measured by 2AP fluorescence (Figure 6E, Figure 6—figure supplement 1C). However, DNA-dependent ATP hydrolysis is minimally affected, particularly in the F582A variant, whose ATPase rate and apparent affinity for DNA are similar to WT (Figure 6F and Figure 6—figure supplement 1D, E). These results indicate that base-flipping requires the separation pin, but base-flipping is not required for DNA binding or ATPase activation.

We hypothesized that the base-flipping mechanism functions to specifically recognize the 3′ end of the primer. By flipping the base, the separation pin could potentially act as a quality control mechanism to verify proper status of the primer end. We tested this hypothesis by measuring how WT-RFC and the W638G and F582A variants respond to various nucleic acid architectures. If our hypothesis were true, we would expect that the W638G and F582A variants would lose the ability to discriminate against ‘incorrect’ nucleic acid substrates. We tested ATPase activity against a series of nucleic acid substrates that include: ssDNA, 3′ phosphate, 3′ abasic sites, a 3′ ribonucleotide, an RNA primer, ssDNA–dsDNA junctions of opposite polarity (i.e. recessed 3′ ends, Figure 6—figure supplement 2A). We performed these assays using nucleic acid concentrations at or near the Kd for the various forms of RFC (Figure 6—figure supplement 1A), so that any deviations in activity or binding would be observable. However, we observe nearly identical ATPase activity profiles for the variants as we do for WT-RFC (Figure 6—figure supplement 2B–D). Therefore, the biochemical characterization of variants with reduced base-flipping does not support our hypothesis that the separation pin acts to discriminate against incorrect substrates.

To directly assess the physiological role of base-flipping in normal RFC function, we measured growth of yeast strains carrying the WT, W638G, or F582A variants as the only copy of RFC1 (Figure 6—figure supplement 3). We tested yeast growth across a wide variety of DNA damaging treatments: ultraviolet radiation (UV), hydroxyurea (HU), or methyl methanesulfonate (MMS). Because base-flipping is thought to have a strong temperature dependence (Yin et al., 2014), we measured yeast growth over a broad temperature range (18–37°C). Surprisingly, we find no obvious growth phenotype across our broad spectrum of conditions (Figure 6—figure supplement 3). Thus, we currently find no obvious role for the separation pin, despite its conservation in RFC complexes across all eukaryotes. Further investigation will be required to discern the functional role, if any, of the base-flipping mechanism of RFC.

## Discussion

### Defining the clamp loading reaction in high resolution

We have determined a series of structures that provide a high-resolution view of the clamp loading process. Our structures correspond to numerous reaction intermediates, allowing us to order the structures into a coherent description of the clamp loading reaction prior to ATP hydrolysis (Figure 7 and Video 4). The Autoinhibited states represent the transient encounter complex that forms early in the clamp loading process before ring opening. The Open1 and 2 states represent the stable intermediate state in which PCNA is opened but DNA has yet to bind. The DNAPCNA-open structure contains p/t-DNA and an open clamp, which is the transient intermediate following DNA binding (Liu et al., 2017; Marzahn et al., 2015; Sakato et al., 2012a). Finally, the DNAPCNA-closed structure represents a possible stable intermediate that forms if ATP hydrolysis were stalled for whatever reason (Marzahn et al., 2015; Sakato et al., 2012b). Therefore, our structures delineate the conformational states that span the entire clamp opening and closing process, the central reaction of the clamp loading cycle.

![Figure 7.](https://cdn.elifesciences.org/articles/74175/elife-74175-fig7-v2.jpg)

**Figure 7.:** Initial binding of RFC to PCNA places the complex in an Autoinhibited state, whereby closed PCNA and the E-plug preclude DNA binding, and an overtightened AAA+ helix inhibits ATPase activity. The Autoinhibited state is dynamic, rocking PCNA relative to RFC as captured by multibody refinement. Upon complete binding to PCNA, RFC uses the crab-claw mechanism to simultaneously open both PCNA and the A-gate, providing an entryway for p/t-DNA. p/t-DNA then binds directly through the A-gate and open PCNA, which are wide enough to accommodate dsDNA entry. The 3′ end of the primer is flipped into the pore that is formed between RFC-A and RFC-B. PCNA closes to form additional contacts with DNA, partially detaching from RFC at the E subunit. Finally, ATPase activity and inorganic phosphate release eject RFC, leaving PCNA bound to p/t-DNA in the correct orientation.

![Video 4.](https://cdn.elifesciences.org/articles/74175/elife-74175-video4.mp4.jpg)

### A crab-claw mechanism for opening the sliding clamp

Our structures show that RFC is in a constricted, autoinhibited conformation upon initial binding to PCNA. This state is highly dynamic, and we captured some of the conformational heterogeneity using multibody refinement. The primary mode of motion pivots PCNA relative to RFC, such that PCNA approaches the D- and E-subunits of RFC. We speculate that this motion is on-pathway toward a direct interaction between PCNA and all five RFC subunits, facilitating the opening of the PCNA ring. Thus, the dynamics of the Autoinhibited complex are important for the opening of PCNA. Future studies will investigate this possibility.

To open PCNA, our structures show that RFC uses the previously hypothesized ‘crab-claw’ mechanism (Jeruzalmi et al., 2001a; Jeruzalmi et al., 2001b; O’Donnell et al., 2001). This contradicts the previous suggestion that the E. coli clamp loader opens the ring with limited conformational changes in the clamp loader (Goedken et al., 2004; Kelch, 2016). In this ‘limited change‘ model, ATP binding places the encounter complex in a conformation that ‘templates’ the open clamp. However, our structures preclude this model for RFC because we observe large conformational changes in the clamp loader upon opening the PCNA ring. Furthermore, the Autoinhibited state of RFC cannot template an open PCNA conformation. One possible reason for the discrepancy between the two studies is that different model systems were used; bacterial clamp loaders lack the A′ domain that constricts the AAA+ spiral of the yeast clamp loader. Without the A′ domain, the bacterial clamp loaders may be free to adopt a conformation that can template the open clamp prior to clamp binding.

The crab-claw motion that we observe is primarily driven by a hinge-like motion that pivots about the RFC-C subunit. This motion allows the A′ domain and E, D, and C subunits to grip PCNA tightly, which is impossible in the Autoinhibited state. Kinetic characterization of RFC variants has predicted a hinge role for this region (Sakato et al., 2012b), highlighting this subunit’s importance in clamp loading. The crab-claw conformational change is remarkable because it requires a fold-switching event in the Lid domain of the RFC-A subunit (Figure 4A, B). At a minimum, this would require that helix-4 of the RFC-A Lid to unfold and refold into a new position. The fact that clamp opening is relatively fast (Liu et al., 2017) and does not require ATP hydrolysis indicates that these conformational rearrangements must have a relatively low energy barrier despite the large-scale motion. How the RFC:PCNA complex couples these motions becomes an important question for future studies.

Why use a ‘crab-claw’ mechanism? We envision two nonmutually exclusive hypotheses. First, we hypothesize that this mechanism allows RFC to bind each of its macromolecular substrates (PCNA and p/t-DNA) in the proper order to ensure efficient clamp loading and to avoid futile cycles of ATP hydrolysis. For proper clamp loading, RFC must bind PCNA first, because initial binding of p/t-DNA would sterically hinder binding of the PCNA ring. Therefore, RFC has evolved high affinity for PCNA and only binds p/t-DNA with high affinity after it has bound PCNA (Cai et al., 1998; Shiomi et al., 2000). The crab-claw mechanism for PCNA opening can explain this hierarchy of binding, as the autoinhibited state blocks the DNA-binding site (Gaubitz et al., 2020 and Figure 3E). The crab-claw mechanism ensures that RFC’s DNA-binding chamber only becomes accessible once the PCNA ring is open. Our second hypothesis is that the crab-claw mechanism enables complex modes of clamp loader regulation. Clamp loader activity could be inhibited by binding partners or post-translational modifications that favor the Autoinhibited state. There are numerous RFC binding partners and post-translational modifications that remain unexplored, and thus are candidates for playing regulatory roles (Dephoure et al., 2008; Kim and Brill, 2001; Ochoa et al., 2020; Olsen et al., 2010; Tomida et al., 2008; Wang et al., 2012; Wang et al., 2013).

### RFC-A subunit drives DNA recognition

To illuminate how RFC recognizes DNA, we measured the relative contribution of each RFC subunit to DNA binding. We find that RFC-A accounts for ~64% of the buried surface area between RFC and DNA. This contrasts with T4 and E. coli clamp loaders, where the A subunits account for ~36% of the binding interface (Figure 6—figure supplement 4B). Much of this proportional increase arises from additional interactions between RFC-A and DNA through the separation pin and the flipped 3′ nucleotide. Furthermore, we find that B, C, D, and E subunits of RFC interact with DNA significantly less (~760 Å2) than the comparable subunits of T4 and E. coli (~1125 Å2). The decrease in DNA interaction from the B, C, D, and E subunits is due to the p/t-DNA duplex region inserting deeper into the AAA+ spiral of the T4 and E. coli clamp loaders than in RFC (Figure 6—figure supplement 4A). Therefore, the large swing in the proportional interaction area is the net result of additional interactions from RFC-A and less from the remaining subunits.

This proportionally large interaction area suggests RFC-A as the subunit primarily responsible for recognizing DNA. This finding provides an attractive explanation for how alternative clamp loaders specifically recognize different DNA structures. RFC-like complexes or RLCs are only found in eukaryotes and share four of RFC’s five subunits (RFC-B through RFC-E); each RLC contains a unique A subunit (Majka and Burgers, 2004). We hypothesize that the diminished role of the B, C, D, and E subunits in DNA recognition allows the A-subunit to assume the role of specifically binding unique structures of DNA. In support of this hypothesis, bacterial and phage clamp loaders do not have alternative forms that recognize different DNA structures, and their clamp loaders have substantially more contact between DNA and the B, C, D, and E subunits. The more pronounced role of the A subunit in eukaryotic clamp loaders allows for dramatically more plasticity in function. Further, the diminished role of the remaining subunits raises the question of how the pivot point at the C subunit contributes to the activity of RLC complexes. Finally, these findings raise the intriguing possibility of engineering RLCs with novel specificity and activity.

Following this reasoning even further, we hypothesized that RFC flips the 3′ nucleotide to specifically recognize the recessed 3′ end of p/t-DNA. We observe flipping of the 3′ nucleotide in both the DNAPCNA-open and DNAPCNA-closed structures, indicating that flipping can occur before ring closure. This observation can explain the ‘DNA repositioning transition’ that occurs quickly (t1/2 ~ 35 ms) after initial DNA binding, but before clamp closure (Liu et al., 2017). We propose that this transition is the flipping of the 3′ nucleotide. However, the flipping mechanism does not appear to be used to discriminate between different DNA architectures. The W638G and F582A variants have a similar DNA discrimination profile as WT-RFC, despite having very different base-flipping activity (Figure 6E, Figure 6—figure supplement 2). Moreover, the physiological role of base-flipping is unclear, as yeast carrying these variants have no obvious cellular defects (Figure 6—figure supplement 3). We still hypothesize that there is likely a role for the flipping activity, as the separation pin is conserved across RFC complexes from yeast to humans. Moreover, this separation pin is not found in the related 9-1-1 clamp loader Rad24-RLC (Castaneda et al., 2021; Zheng et al., 2021). A separation pin extension is found in the related loader Ctf18 (Figure 6—figure supplement 5B) but the flipping amino acids are not conserved. (Predictions for or against a separation pin in the final loader subunit Elg1 are weak due to very limited sequence homology between RFC1 and Elg1.) Future experiments will investigate the role of base-flipping in more detail.

### Forces driving clamp loading

Our structures delineate a conformational pathway that illustrates much of the clamp loading reaction. We reveal how: (1) RFC initially binds PCNA, (2) how PCNA is opened, (3) how DNA is bound, and (4) how PCNA closes around DNA. This unprecedented view into the mechanism of clamp loading allows us to hypothesize on the forces that drive this reaction toward the loading of PCNA. We use the interaction areas between and within PCNA, RFC, and p/t-DNA to approximate these forces.

PCNA is opened through a large conformational change in both PCNA and RFC. In solution the open form is the predominant state (Zhuang et al., 2006), so it is important to understand what interactions drive this opening. Upon opening, PCNA loses the entire interface between subunits I and III. However, the open PCNA ring increases its interaction area with RFC by contacting all five subunits. Moreover, the crab-claw motion of RFC results in tighter association between adjacent AAA+ modules. Altogether, the opening of PCNA and RFC result in an increased interaction area of ~4000 Å2 (Figure 3F). We propose that this is the driving force for stabilizing the open form of PCNA.

Once open, p/t-DNA enters the PCNA:RFC complex through the A-gate. The A-gate is wide enough for dsDNA to directly enter into the RFC:PCNA inner chamber. This finding is in direct contradiction of the ‘filter-and-slide’ model for DNA binding that posited that the opening is large enough for only ssDNA to enter such that the clamp loader filtered out dsDNA to accelerate the search for a p/t-junction (Kelch, 2016; Kelch et al., 2011). The filter-and-slide model was primarily predicated on crystal structures of the T4 phage clamp loader and on FRET data that suggested that initial binding of DNA does not constrict the open clamp (Kelch et al., 2011; Zhuang et al., 2006). While it remains a possibility that other clamp loaders use a filter-and-slide mechanism, our structures clearly indicate that yeast RFC uses the much more simple direct binding model.

Once DNA is bound, PCNA must close around the ring before ejection of the RFC complex. Rapid kinetics studies showed that ATP hydrolysis precedes clamp closure under normal conditions (Liu et al., 2017; Marzahn et al., 2015; Sakato et al., 2012b). Taken together, these two points could lead to the conclusion that ATP hydrolysis provides the energy to actively close the clamp after loading DNA. However, we observe this transition from our DNAPCNA-open and DNAPCNA-closed structures, and neither structure shows evidence of ATP hydrolysis, suggesting that PCNA can close before ATP hydrolyzes. To harmonize all of the available data, we must draw a new conclusion, which is that while ATP hydrolysis typically occurs prior to clamp closure, it is not strictly required, and clamp closure can precede hydrolysis if the hydrolysis step becomes rate limiting, as would likely occur with the slowly hydrolyzable ATPγS. It still remains possible that ATP hydrolysis could make clamp closure easier, by weakening interactions between RFC and PCNA/DNA, but in this view clamp closure is still a spontaneous process and does not require harvesting energy from ATP hydrolysis. Therefore, it is possible that ATP hydrolysis can proceed from either DNAPCNA-open and DNAPCNA-closed states, but most commonly from the DNAPCNA-open state.

This raises the question as to how DNA stimulates ATP hydrolysis and subsequent ejection of the clamp loader. We note that the ATPase active sites do not change much from the Open to DNAPCNA-open or DNAPCNA-closed conformations (Figure 5—figure supplement 2). It is also surprising that the AAA+ modules are already in a symmetrized pose prior to DNA loading, because DNA had been thought to be the driving force for symmetrizing the AAA+ spiral (Kelch et al., 2011; Simonetta et al., 2009), and this symmetry had been thought to favor ATP hydrolysis. Despite this symmetry, the RFC:PCNA complex (corresponding to the Open1 and Open2 structures) has ~five- to tenfold lower ATPase activity than when both PCNA and DNA are bound (Figure 6F, Chen et al., 2009; Gomes et al., 2001; McNally et al., 2010; Sakato et al., 2012a). This implies that, whereas clamp opening is both necessary and sufficient for symmetrizing the AAA+ modules, this symmetry by itself is not sufficient to stimulate ATP hydrolysis.

There remain many possible avenues for DNA to stimulate ATP hydrolysis. In many AAA+ enzymes, it has been shown that certain residues couple ligand binding and ATP hydrolysis by activating the Walker B glutamate residue (Zhang and Wigley, 2008). A set of conserved arginines (termed the arginine switch residues) within the core of the AAA+ module were proposed to play this role in clamp loaders (Kelch et al., 2011). The arginine switch residues had been hypothesized to flip outward to grip DNA, thereby releasing the Walker B catalytic glutamate to activate ATP hydrolysis. However, the lack of flipping of the arginine switch residues in response to DNA binding in our structures argues that the proposed arginine switch mechanism is not critical for sensing and responding to DNA binding. Our observations are in agreement with previous studies that found that the arginine switch residues of RFC do not likely play a direct role in activating ATP hydrolysis, but are important for the synergistic activation by both PCNA- and DNA binding (Liu et al., 2017). An alternative route, involving a different arginine residue interacting with the ATPase active site, has recently been proposed for DnaC and extended to RFC (Puri et al., 2021). However, we again do not see structural evidence supporting this mechanism. We cannot rule out these mechanisms (or a combination of the two), as these types of interactions may occur just before hydrolysis and are not readily apparent in stalled structures. A recent study on the T4 clamp loader suggests that structural rigidity of a ‘central coupler’ that encircles DNA is important for hydrolysis (Subramanian et al., 2021). Thus, tight binding of RFC to DNA could provide rigidity necessary to stimulate ATP hydrolysis.

Lastly, we note that while DNAPCNA-open and DNAPCNA-closed have similar overall interaction areas, PCNA interacts with DNA much more intimately in the DNAPCNA-closed structure, with direct contact to several conserved basic residues lining the PCNA inner pore. Lys20, Arg80, and Arg147 in particular show close interaction with the PCNA ring. These residues have been independently identified as critical for efficient DNA binding, ATP hydrolysis, and clamp loading (McNally et al., 2010; Zhou and Hingorani, 2012). Therefore, PCNA is an allosteric effector in its own loading and its role in stimulating ATPase activity upon DNA binding should not be overlooked. Further studies will be necessary to reveal how RFC integrates binding of both PCNA and p/t-DNA to achieve full activation.

### Comparison with other AAA+ machines

Clamp loaders have long been models for structure and mechanism of AAA+ proteins (Guenther et al., 1997). However, they are unusual in that they are pentameric protein remodeling switches instead of the more typical hexameric rings that act as processive motors (Hanson and Whiteheart, 2005; Kelch, 2016). We note that conformational changes that we observe here in RFC appear to be more dramatic than those typically seen during motor function. This is likely because the constraints imposed by ring closure limits the types of motions that are available. On the other hand, the open nature of the RFC complex is less constrained and so can adopt more dramatic conformational changes. We further note that these types of large conformational changes are more commonplace in other members of the Initiator/Loader class of AAA+ machines. We propose that the open nature of this class provides larger conformational variability that is necessary for the regulation of these switch-like machines.

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
      <td>BL21(DE3)</td>
      <td>Novagen</td>
      <td>69,450</td>
      <td>Chemically competent cells</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET(11a)-RFC[2 + 3 + 4] (plasmid)</td>
      <td>Finkelstein et al., 2003</td>
      <td></td>
      <td>Expression plasmid</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pLANT-2/RIL[1 + 5] (plasmid)</td>
      <td>Finkelstein et al., 2003</td>
      <td></td>
      <td>Expression plasmid</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pRS413-RFC1(plasmid)</td>
      <td>This study</td>
      <td></td>
      <td>Plasmid for yeast expression of Rfc1 from endogenous promotor</td>
    </tr>
    <tr>
      <td>Strain, strain background (S. cerevisiae)</td>
      <td>BY4743his3Δ1/his3Δ1 leu2Δ0/leu2Δ0 LYS2/lys2Δ0 met15Δ0/MET15 ura3Δ0/ura3Δ0 ∆rfc1::KanMX4/RFC1 (YOR217W)</td>
      <td>Dharmacon</td>
      <td>YSC1055 (22473)</td>
      <td>Yeast Heterozygous Collection</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RELION</td>
      <td>doi:10.7554/eLife.42166</td>
      <td>Relion 3.0.2</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>cisTEM</td>
      <td>doi:10.7554/eLife.35383</td>
      <td>cisTEM-1.0.0-beta</td>
      <td>https://cistem.org/software</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Ctffind</td>
      <td>doi:10.1016/j.jsb.2015.08.008</td>
      <td>Ctffind 4.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSF Chimera</td>
      <td>UCSF, doi:10.1002/jcc.20084</td>
      <td></td>
      <td>http://plato.cgl.ucsf.edu/chimera/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ChimeraX</td>
      <td>UCSF, doi:10.1002/pro.3943</td>
      <td>ChimeraX-1.2</td>
      <td>https://www.cgl.ucsf.edu/chimerax/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>COOT</td>
      <td>doi:10.1107/S0907444910007493</td>
      <td>Coot-0.9.4</td>
      <td>http://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phenix</td>
      <td>doi:10.1107/S0907444909052925</td>
      <td>Phenix-dev-3699</td>
      <td>https://phenix-online.org</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PyMOL</td>
      <td>PyMOL Molecular Graphics System, Schrodinger LLC</td>
      <td></td>
      <td>https://www.pymol.org/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad PRISM</td>
      <td>GraphPad</td>
      <td>GraphPad PRISM 9.2.1</td>
      <td>http://www.graphpad.com/</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Pyruvate kinase</td>
      <td>Calzyme</td>
      <td>107A0250</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Lactate Dehydrogenase</td>
      <td>Worthington Biochemical Cooperation</td>
      <td>LS002755</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Phosphoenol-pyruvic acid monopotassium salt</td>
      <td>Alfa Aesar</td>
      <td>B20358</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Protein purification

RFC was purified as described previously with minor modifications (Finkelstein et al., 2003). pET(11a)-RFC[2 + 3 + 4] and pLANT-2/RIL-RFC[1 + 5] were transformed into BL21(DE3) E. coli cells (Millipore). After preculture, transformants were grown in 4 l of prewarmed terrific broth medium supplemented with 50 μg/ml kanamycin and 100 μg/ml ampicillin at 37°C and induced with IPTG at an optical density of 0.8. Protein expression was continued at 18°C for 15 hr. Cells were pelleted and resuspended in 300 ml lysis buffer (30 mM 2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic acid (HEPES)–NaOH pH 7.5, 250 mM NaCl, 0.25 mM Ethylenediaminetetraacetic acid (EDTA), 5% glycerol, 2 mM Dithiothreitol (DTT), 2 μg/ml aprotinin, 0.2 μg/ml pepstatin, 2 μg/ml leupeptin, and 1 mM phenylmethylsulfonyl fluoride (PMSF)). RFC was purified by chromatography over a 10 ml SP-Sepharose column (80 ml gradient of 300–600 mM NaCl in Buffer C) and a 10 ml Q-Sepharose column (40 ml gradient of 150–500 mM NaCl in Buffer C, GEHealthcare). Peak fractions of hRFC were pooled and dialyzed overnight into a buffer with 30 mM HEPES–NaOH pH 7.5, 250 mM NaCl, 5% glycerol, and 2 mM DTT.

PCNA was purified as described previously with modifications (McNally et al., 2010). BL21(DE3) E. coli cells were transformed with a pET-28 vector that encodes PCNA with a Precission protease cleavable N-terminal 6-His tag. After transformation, preculture and induction, 1 l of cells was grown overnight at 18°C in terrific broth medium supplemented with 50 μg/ml kanamycin. Cells were pelleted and resuspended 30 mM HEPES, pH 7.6, 20 mM imidazole, 500 mM NaCl, 10% glycerol, and 5 mM b-mercaptoethanol. The cells were lysed, centrifuged, and the filtered lysate was applied to a 5 ml HisTrap FF column (GE Healthcare). The column was washed with a buffer at 1 M NaCl, and subsequently washed with a buffer at a low salt concentration (50 mM NaCl). PCNA was eluted with a step of 50% with 500 mM imidazole. The eluted protein was cleaved with Precission protease for 2 hr at room temperature and applied to a 5 ml HiTrap Q HP column (GE Healthcare). Protein was eluted from the Q HP column with a 2 M NaCl buffer in a 100 ml gradient. Peak fractions were dialyzed against buffer containing 30 mM Tris, pH 7.5, 100 mM NaCl, and 2 mM DTT. Purified proteins were concentrated with an Amicon concentration device, aliquoted and frozen in liquid nitrogen for storage at −80°C.

### Crosslinking and mass spectrometry

RFC and PCNA were mixed in a 1/1 ratio and gel filtered into 1 mM tris(2-carboxyethyl)phosphine (TCEP), 200 mM NaCl, 25 mM HEPES–NaOH, pH 7.5, and 4 mM MgCl2. The protein complex was diluted to 3 µM and after the addition of 1 mM ATPγS and 3-min incubation, 1 mM of bis(sulfosuccinimidyl)suberate (BS3, Thermo Scientific Pierce) was added for crosslinking. For crosslinking of DNA-bound RFC:PCNA, 1 mM ATPγS was added to the protein complex first and incubated for 2 min. 7 μM primer/template DNA was added and incubated for another 1 min. The primer sequence was 5′-GCAGACACTACGAGTACATA-3′ and the template sequence was 5′-TTTTTTTTTTTATGTACTCGTAGTGTCTGC-3′. Crosslinking was started with 1 mM BS3, incubated for 15 min at room temperature, and neutralized with Tris–HCl.

Sample without DNA was analyzed by mass spectrometry. The sample was reduced, alkylated, and loaded onto sodium dodecyl sulfate–polyacrylamide gel electrophoresis (SDS–PAGE gel). The gel band corresponding to the crosslinked complex >150 kDa was excised, destained, and incubated with trypsin. The digested peptides were extracted and desalted as previously described (Peled et al., 2018) and analyzed with LC–MS coupled to a Thermo Fisher Scientific Q Exactive Mass Spectrometer in data-dependent mode selecting only precursors of 3. The data were searched against the UniProt database, using Byonic and XlinkX of the Proteome Discoverer 2.3 package.

### Electron microscopy

#### Negative-staining EM

100 nM of RFC:PCNA was applied on carbon-coated 400-mesh grids. Excess sample was blotted from the grid surface, the grids were washed twice with 50 mM HEPES, pH 7.5 and stained with 1% uranyl acetate. RFC:PCNA was imaged on a 120 kV Philips CM-120 microscope fitted with a Gatan Orius SC1000 detector.

#### Cryo-EM sample preparation

Quantifoil R 0.6/1 (DNA dataset) grids were washed with ethyl acetate. Quantifoil and C-flat grids (Electron Microscopy Sciences) were glow discharged with Pelco easiGlow for 60 s at 25 mA (negative polarity). 2.8–3 μl sample was applied to grids at 10°C and 95% humidity in a Vitrobot Mark IV (FEI). Samples were blotted with a force of 5 for 5 s after a 2 s wait and plunged into liquid ethane.

#### Cryo-EM data collection

RFC:PCNA was imaged on a Titan Krios operated at 300 kV and equipped with an GIF energy filter at ×130,000 magnification and a pixel size of 0.53 Å using a K2 Summit detector in superresolution counting mode. The data were collected in four sessions with a target defocus range of −1.1 to −2.4 and a total exposure of ~49–51 e−/Å2 per micrograph averaging 50 frames. Image shift was used to record three images per hole with SerialEM (Mastronarde, 2003). Defective micrographs were discarded leaving a total of 6109 micrographs for processing. RFC:PCNA:DNA was imaged on a Titan Krios operated at 300 kV at ×81,000 magnification and a pixel size of 0.53 Å with a K3 detector in super-resolution mode. A total of 4499 micrographs were collected in 1 day with a target defocus of −1.2 to −2.3 and a total exposure of ~40 e−/Å2 per micrograph averaging 30 frames.

#### Data processing

Micrograph frames were aligned in IMOD (Kremer et al., 1996) with 2× binning, resulting in a pixel size of 1.06 Å/pixel. Initial CTF estimation and particle picking were performed using cisTEM (Grant et al., 2018; Rohou and Grigorieff, 2015). Following particle picking, particles were extracted with a box size of 240 pixels and subjected to 2D classification into 100 classes. Particles from classes with well-defined features were selected for processing in Relion (Figure 1—figure supplement 2A, B, Figure 3A, B). Coordinates and combined micrographs were imported into Relion 3.0.2 (Zivanov et al., 2018), CTF parameters were re-estimated with Gctf1.06 (Zhang, 2016) and particles were subjected to several rounds of 3D classification (Figure 1—figure supplements 2D and 3C). For 3D classification of the RFC:PCNA dataset, an ab initio model was generated with cisTEM, downfiltered to 50 Å and used as reference (Figure 1—figure supplement 2C). For 3D classification of the RFC:PCNA:DNA dataset, class Open1 of the RFC:PCNA dataset was downfiltered to 60 Å and used as reference. Selected, well resolved 3D classes were refined with Relion. The cryo-EM density was postprocessed in Relion for estimating the resolution and density modified with PHENIX for model building and refinement (Terwilliger et al., 2020 Table 3). Model information was not used during density modification.

### Model building and refinement

The crystal structure of yeast RFC bound to PCNA (PDB ID: 1SXJ) was used for initial fitting of Autoinhibited1. All subunits were split into globular domains and fitted into the cryo-EM density with UCSF Chimera (Pettersen et al., 2004). The model was adjusted in Coot (Emsley and Cowtan, 2004), and real-space iteratively refined with two macrocycles in PHENIX1.17 (Liebschner et al., 2019). Autoinhibited2,3 cryo-EM densities were rigid body fit with the refined model of Autoinhibited1, manually adjusted in coot and refined.

The refined model of Autoinhibited1 (Figure 1—figure supplement 1C) was fragmented into individual subunit domains and rigid body fitted into the cryo-EM density of Open2. The resulting model was further flexibly fitted and refined with Namdinator (Kidmose et al., 2019). The resulting model was adjusted in Coot, and refined in PHENIX. The model of Open2 was used for fitting the Open1 cryo-EM density. The fitted model was manually adjusted in Coot and refined in PHENIX. The cryo-EM density of DNAPCNA-closed (Figure 1—figure supplement 3C) was fitted using the Autoinhibited1 model and DNA was modeled in Coot. The resulting model was further flexibly fitted and refined with Namdinator (Kidmose et al., 2019). The model was then adjusted in Coot, and refined in PHENIX. The Namdinator output model of DNAPCNA-closed was used for fitting of the DNAPCNA-open cryo-EM density. The fitted model was manually adjusted in Coot and subjected to refinement in PHENIX. Interface areas were analyzed with the PISA server (Krissinel and Henrick, 2007). UCSF Chimera and Pymol were used for figure generation (Delano, 2002; Pettersen et al., 2004).

### ATPase assays

0.3 μM (Figure 6F) or 0.15 μM RFC (Figure 6—figure supplement 1D) was incubated with a master mix (3 U/ml Pyruvate kinase, 3 U/ml lactate dehydrogenase, 1 mM ATP, 670 μM phosphoenol pyruvate, 170 μM NADH, 50 mM Tris (pH 7.5), 0.5 mM TCEP, 5 mM MgCl2, 200 mM potassium glutamate, 40 mM NaCl), 1 µM PCNA, and annealed primer/template DNA (2 µM Figure 6F, varying amounts Figure 6—figure supplement 1D). ATPase activity was measured at 25°C with the 2014 EnVison Multilabel Plate Reader to detect NAD+. Rates were obtained from a linear fit of the slopes using GraphPad Prism. For the ATPase activity measurements shown in Figure 6—figure supplement 2, 0.12 µM RFC was incubated with 1 µM PCNA and 0.03 µM different DNA constructs (as described in Table 4) and the master mix and buffer described above. ATPase activity was measured at room temperature. For each data point three experimental replicates were performed.

**Table 4.**
 DNA sequences.


<table>
  <thead>
    <tr>
      <th>Template name</th>
      <th>Sequence</th>
      <th>Primer name</th>
      <th>Sequence</th>
      <th>Name used in assay</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Template30-20-A</td>
      <td>TTTTTTTTTTAATGTACTCGTAGTGTCTGC</td>
      <td>Primer20-3’abasic</td>
      <td>GCAGACACTACGAGTACAT/3dSp/</td>
      <td>p/t-DNA 3'-abasic</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Primer20-3’-T-phosphate</td>
      <td>GCAGACACTACGAGTACATT/3Phos/</td>
      <td>p/t-DNA 3’ PO4</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Primer20-3’-T-RNA</td>
      <td>rGrCrArGrArCrArCrUrArCrGrArGrUrArCrArUrU</td>
      <td>RNA primer/DNA template</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Primer20-3’-riboT</td>
      <td>GCAGACACTACGAGTACATrU</td>
      <td>p/t-DNA 3’ ribo</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Primer20-3’-T</td>
      <td>GCAGACACTACGAGTACATT</td>
      <td>p/t-DNA</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Primer20-2AP-0</td>
      <td>GCAGACACTACGAGTACAT/32AmPu/</td>
      <td>p/t-AP, P = 1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Primer20-2AP-2</td>
      <td>GCAGACACTACGAGTAC/i2AmPr/TA</td>
      <td>p/t-AP, P = 3</td>
    </tr>
    <tr>
      <td>Template30-T-1</td>
      <td>TTTTTTTTTTTTTGTACTCGTAGTGTCTGC-3’</td>
      <td>Primer20-2AP-1</td>
      <td>GCAGACACTACGAGTACA/i2AmPr/A</td>
      <td>p/t-AP, P = 2</td>
    </tr>
    <tr>
      <td>Template30-20-2AP</td>
      <td>TTTTTTTTTT/i2AmPr/ATGTACTCGTAGTGTCTGC-3’</td>
      <td>Primer20-3’-T</td>
      <td>GCAGACACTACGAGTACATT</td>
      <td>p/t-AP, t = 1</td>
    </tr>
    <tr>
      <td>Template20-5’-A</td>
      <td>AATGTACTCGTAGTGTCTGC</td>
      <td>Primer20-3’-T</td>
      <td>GCAGACACTACGAGTACATT</td>
      <td>Blunt DNA</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Primer 20–3'-T-10ext</td>
      <td>GCAGACACTACGAGTACATTTTTTTTTTTT</td>
      <td>3' overhang DNA</td>
    </tr>
    <tr>
      <td>Template30-20-A-3’T</td>
      <td>AATGTACTCGTAGTGTCTGCTTTTTTTTTT</td>
      <td>Primer 20–3'-T-10ext</td>
      <td>GCAGACACTACGAGTACATTTTTTTTTTTT</td>
      <td>3' overhang dumbbell DNA</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>polyT 20</td>
      <td>TTTTTTTTTTTTTTTTTTTT</td>
      <td>ssDNA (poly T)</td>
    </tr>
  </tbody>
</table>

### 2-AP fluorescence

2AP fluorescent samples were excited at 315 nm (5 mm slit width), and emission was detected at 370 nm (7 mm slit width) with a FluoroMax 4 (Horiba Join Yvon Inc). Reactions contained 150 or 375 nM annealed DNA (Table 4) and 0.5 or 1 µM RFC in a buffer with 50 mM HEPES–NaOH pH 7.5, 200 mM NaCl, 4 mM MgCl2, 1 mM TCEP and were carried out at room temperature. Experiments (Figure 6C) were performed in the presence of 375 nM DNA, 0.5 μM RFC, and 2.5 μM PCNA. Experiments (Figure 6D, E) were performed with 150 nM DNA, 1 μM RFC, and 2.5 μM PCNA.

### Plasmid generation

The separation pin variants were introduced with site-directed mutagenesis in either pLANT-2/RIL-RFC[1 + 5] for protein purification or pRS413-RFC1 for yeast complementation. pRS413-RFC1 contains the entire RFC1 sequence, where RFC1 is expressed under the control of its own promotor.

### Yeast strains and spot assay

The genotype of the S. cerevisiae strain which was used in this study for transformation with the pRS413 plasmids is described in the Key Resources Table. S. cerevisiae culture, transformation, and tetrad dissection, were performed as previously described (Gomes et al., 2000).

For the spot assay, yeast grown on SC-His plate at 30°C for 2 days was inoculated into 3 ml SC-His media and grown for 3–4 hr to an OD of 0.8. Serial tenfold dilutions of the cultures starting from OD of 0.2 were plated as 4 µl drops onto YPD plates with or without chemical additives (0.01% MMS, 100 mM HU). For UV treatment, the spotted yeast was irradiated with 30 or 100 J/m2 using a UVP UV Crosslinker. The plates were imaged after incubating at 18°C for 7 days, or at 30°C, 37°C for 3 days, (duplicates were done for the treatment with MMS, and triplicates for all other treatments).
