# Monoubiquitination by the human Fanconi anemia core complex clamps FANCI:FANCD2 on DNA in filamentous arrays

## Authors

- Winnie Tan<sup>1</sup> ([ORCID: 0000-0003-3229-4157](https://orcid.org/0000-0003-3229-4157))
- Sylvie van Twest<sup>1</sup> ([ORCID: 0000-0001-5602-0906](https://orcid.org/0000-0001-5602-0906))
- Andrew Leis<sup>3</sup> ([ORCID: 0000-0003-4905-9401](https://orcid.org/0000-0003-4905-9401))
- Rohan Bythell-Douglas<sup>1</sup> ([ORCID: 0000-0002-3823-8749](https://orcid.org/0000-0002-3823-8749))
- Vincent J Murphy<sup>1</sup>
- Michael Sharp<sup>1</sup> ([ORCID: 0000-0002-1019-3729](https://orcid.org/0000-0002-1019-3729))
- Michael W Parker<sup>3</sup> ([ORCID: 0000-0002-3101-1138](https://orcid.org/0000-0002-3101-1138))
- Wayne Crismani<sup>1</sup> ([ORCID: 0000-0003-0143-8293](https://orcid.org/0000-0003-0143-8293))
- Andrew J Deans<sup>1</sup> ([ORCID: 0000-0002-5271-4422](https://orcid.org/0000-0002-5271-4422)) †

### Affiliations

1. Genome Stability Unit, St. Vincent’s Institute of Medical Research Fitzroy Australia
2. Department of Medicine (St. Vincent’s Health), The University of Melbourne Melbourne Australia
3. Bio21 Institute, University of Melbourne Parkville Australia
4. Structural Biology Unit, St. Vincent’s Institute of Medical Research Fitzroy Australia

† Corresponding author

## Abstract

FANCI:FANCD2 monoubiquitination is a critical event for replication fork stabilization by the Fanconi anemia (FA) DNA repair pathway. It has been proposed that at stalled replication forks, monoubiquitinated-FANCD2 serves to recruit DNA repair proteins that contain ubiquitin-binding motifs. Here, we have reconstituted the FA pathway in vitro to study functional consequences of FANCI:FANCD2 monoubiquitination. We report that monoubiquitination does not promote any specific exogenous protein:protein interactions, but instead stabilizes FANCI:FANCD2 heterodimers on dsDNA. This clamping requires monoubiquitination of only the FANCD2 subunit. We further show using electron microscopy that purified monoubiquitinated FANCI:FANCD2 forms filament-like arrays on long dsDNA. Our results reveal how monoubiquitinated FANCI:FANCD2, defective in many cancer types and all cases of FA, is activated upon DNA binding.

## Introduction

Fanconi anemia (FA) is a devastating childhood syndrome that results in bone marrow failure, leukemia and head and neck cancers (Gillio et al., 1997; Butturini et al., 1994). FA is caused by inheritance of one of 22 dysfunctional FA genes (FANCA-FANCW) (Tan and Deans, 2017). Absence of any one member of the pathway causes genome instability during DNA replication, which results in mutagenic (cancer-causing) DNA damage and hypersensitivity to chemotherapeutic (normal and cancer-killing) DNA damage (Deans and West, 2011). Central to the FA pathway is the conjugation of ubiquitin to FANCI:FANCD2 (ID2) complexes (Walden and Deans, 2014). ID2 monoubiquitination is critical to prevention of bone marrow failure in FA, but it is currently unknown how ID2-ub differs in its function to ID2. Several proteins have been proposed to specifically bind FANCIUb or FANCD2Ub but not the un-ubiquitinated proteins (Smogorzewska et al., 2010; Lachaud et al., 2014). For example, FAN1 nuclease was proposed to interact with FANCD2Ub via its ubiquitin-binding domain (UBZ) (Smogorzewska et al., 2010), whereas recruitment of SLX4 endonuclease to the interstrand crosslink site was shown to be dependent on FANCD2 ubiquitination (Klein Douwel et al., 2014). However, support for these interactions is limited to analysis of ubiquitination-deficient (K > R) mutants, rather than evidence for direct ubiquitin-mediated protein interactions.

The retention of FANCD2 in chromatin foci is dependent on its monoubiquitination by a ‘core complex’ of Fanconi anemia proteins (Walden and Deans, 2014). FANCI and the FA core complex are required to generate FANCD2-foci that mark the location of double strand breaks, stalled replication forks and R-loops (Taniguchi et al., 2002; Schwab et al., 2015; Wienert et al., 2019) in the nucleus, and protect nascent DNA at these sites from degradation by cellular nucleases (Schlacher et al., 2012). The ubiquitinated form of FANCD2, and also its ubiquitinated partner protein FANCI, become resistant to detergent and high-salt extraction from these foci (Smogorzewska et al., 2007; Montes de Oca et al., 2005), leading to speculation about the existence of a chromatin anchor or altered DNA binding specificity post-monoubiquitination (Longerich et al., 2014).

A recent electron microscopy study revealed a DNA interacting domain that is required for FANCI:FANCD2 binding to DNA (Liang et al., 2016). The crystal structure of the non-ubiquitinated FANCI:FANCD2 shows that the monoubiquitination sites of FANCI:FANCD2 are buried and therefore inaccessible in the dimer interface of the complex (Joo et al., 2011), suggesting that DNA binding might be required to expose the ubiquitin binding sites. Based on biochemical analyses, non-ubiquitinated FANCI and FANCD2 preferentially bind to branched DNA molecules which mimic DNA replication and repair intermediates (Longerich et al., 2014; Longerich et al., 2009; Niraj et al., 2017); however, how that activates monoubiquitination of FANCI:FANCD2 remains poorly understood. DNA is a cofactor for maximal ubiquitination (Longerich et al., 2014; van Twest et al., 2017), as is phosphorylation by the ATR kinase (Tan et al., 2020b; Ishiai et al., 2008).

Here, we have reconstituted the FA pathway using recombinant FA core complex and fluorescently labeled DNA oligomer substrates. We show that once monoubiquitinated, FANCI:FANCD2 forms a tight interaction with double-stranded containing DNA. We report the successful purification of monoubiquitinated FANCI:FANCD2 complex bound to DNA using an Avi-ubiquitin construct, and show that the monoubiquitination does not promote any new protein:protein interactions with other factors in vitro. Instead, we reveal a new role of monoubiquitinated FANCI:FANCD2 in forming higher order structures and demonstrate how monoubiquitinated FANCI:FANCD2 interacts with DNA to initiate DNA repair. Our work uncovers the molecular function of the pathogenetic defect in most cases of FA.

## Results

### Monoubiquitination does not promote association of FANCI:FANCD2 with a panel of proteins previously hypothesized to bind the ubiquitinated form

Mono-ubiquitinated FANCI:FANCD2 (henceforth IUbD2Ub) is the active form of the complex in repair of DNA damage. Many previous studies have speculated about the existence of DNA repair proteins that specifically associate with IUbD2Ub. A summary of these proteins is presented in Table 1. Using recombinant ID2 or IUbD2Ub prepared by Avi-ubiquitin purification method (Tan et al., 2020a), we sought to directly compare the binding of this panel of ID2-associated proteins. Each of the partner proteins was expressed using reticulocyte extracts (Figure 1a), and the majority bound to the ID2 complex as predicted based on previously identified associations (Figure 1b). The strongest binding proteins in terms of fraction of protein recovered were SLX4, FAAP20, SMARCAD, FANCJ, PSMD4, SF3B1, MCM5 and BRE. Although SMARCAD and SF3B1 appeared ‘sticky’ in control experiments, recovery of these proteins was still enriched by FANCD2:FANCI beads compared to background. Luciferase protein was used as a control 35S-labeled prey-protein. Surprisingly, our main observation was that none of the proteins showed any increased affinity for IUbD2Ub over ID2 (Figure 1d).

**Table 1.**
 List of proteins containing ubiquitin binding domain that are described or predicted to bind to ubiquitinated FANCD2.


<table>
  <thead>
    <tr>
      <th>Protein</th>
      <th>Function</th>
      <th>Domain</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>FAN1</td>
      <td>Nuclease</td>
      <td>UBZ4</td>
      <td>(Kratz et al., 2010)</td>
    </tr>
    <tr>
      <td>SLX4</td>
      <td>Nuclease</td>
      <td>UBZ1</td>
      <td>(Lachaud et al., 2014)</td>
    </tr>
    <tr>
      <td>FAAP20</td>
      <td>FANCA partner</td>
      <td>UBZ</td>
      <td>(Hein et al., 2015)</td>
    </tr>
    <tr>
      <td>RAP80</td>
      <td>BRCA1 partner</td>
      <td>UIM</td>
      <td>(Castillo et al., 2014)</td>
    </tr>
    <tr>
      <td>SMARCAD1</td>
      <td>Chromatin remodeler</td>
      <td>CUE</td>
      <td>(Densham et al., 2016)</td>
    </tr>
    <tr>
      <td>FANCJ</td>
      <td>Helicase</td>
      <td>-</td>
      <td>(Raghunandan et al., 2015)</td>
    </tr>
    <tr>
      <td>PSMD4</td>
      <td>Protease</td>
      <td>UIM</td>
      <td>(Jacquemont and Taniguchi, 2007)</td>
    </tr>
    <tr>
      <td>SF3B1</td>
      <td>RNA binding protein</td>
      <td>UBZ</td>
      <td>(Moriel-Carretero et al., 2017)</td>
    </tr>
    <tr>
      <td>TRIM25</td>
      <td>E3 ligase</td>
      <td>RING finger</td>
      <td>(Lossaint et al., 2013)</td>
    </tr>
    <tr>
      <td>MCM5</td>
      <td>CMG component</td>
      <td>-</td>
      <td>(Lossaint et al., 2013)</td>
    </tr>
    <tr>
      <td>BRE</td>
      <td>BRCA1 partner</td>
      <td>-</td>
      <td>(Wang, 2007)</td>
    </tr>
    <tr>
      <td>BRCC</td>
      <td>BRCA1 partner</td>
      <td>-</td>
      <td>(Wang, 2007)</td>
    </tr>
    <tr>
      <td>SNM1A</td>
      <td>Nuclease</td>
      <td>UBZ</td>
      <td>(Yang et al., 2010)</td>
    </tr>
    <tr>
      <td>CtIP*</td>
      <td>Nuclease activator</td>
      <td>C2H2 zinc finger</td>
      <td>(Murina et al., 2014)</td>
    </tr>
    <tr>
      <td>Rev1*</td>
      <td>Translesion polymerase</td>
      <td>UBZ3</td>
      <td>(Moldovan et al., 2010)</td>
    </tr>
  </tbody>
</table>

_*Indicates not tested in our experiments, because protein not produced in TnT system._

![Figure 1.](https://cdn.elifesciences.org/articles/54128/elife-54128-fig1-v2.jpg)

**Figure 1.:** (a) 35S-labelled FAN1, SLX4, FAAP20, RAP80, SMARCAD, FANCJ, PSMD4, SF3B1, TRIM25, MCM5, BRE, BRCC, SNM1A or luciferase (control) inputs were expressed using reticulocyte extracts. (b–c) The inputs prepared from (a) were incubated with the indicated FLAG-ID2 (b) or FLAG-IubD2ub (c) followed by FLAG pull-down and elution. The complexes were subjected to SDS-PAGE, and radiolabelled proteins were detected by autoradiography (representative experiment of n = 2). (d) Quantification showing percentage of ID2, IubD2ub or FLAG resin binding to inputs.

### Monoubiquitination clamps FANCI:FANCD2 on DNA

An alternative explanation for the observed increase in association between ID2 and its associated proteins after DNA damage is that IUbD2Ub has an increased affinity for DNA, which brings the protein into closer proximity to these partners. The majority of ID2 associated proteins are chromatin localized. In order to explore the stability of IUbD2Ub on DNA, we performed in vitro monoubiquitination reactions in the presence of IR-dye700 labeled 60 bp double-stranded DNA (dsDNA). As previously characterized (van Twest et al., 2017), we observed DNA-dependent appearance of monoubiquitinated forms of FANCD2 and FANCI when using recombinant FA core complex components (Figure 2a–b). ID2 monoubiquitination readily lead to DNA mobility shifts using EMSA (electromobility shift assay) even at low concentrations, but this was not observed for the unmodified (apo)-ID2 complex in the absence of the enzymatically active FA core complex, or when monoubiquitination-defective K-to-R mutants of ID2 were used in the reaction (Figure 2c, lanes 2–4).

![Figure 2.](https://cdn.elifesciences.org/articles/54128/elife-54128-fig2-v2.jpg)

**Figure 2.:** (a) Schematic of the electrophoretic mobility shift assay (EMSA) using IRDye-700 labeled dsDNA. (b) Coomassie stained SDS-PAGE gel showing monoubiquitination of FANCI:FANCD2 using recombinant FA core complex and IR-dye700 labeled dsDNA. 25, 50 and 100 nM of ID2 or IKRD2KR were incubated with 25 nM of the IR-dye700 dsDNA for 90 min. The respective percentage of FANCI or FANCD2 monoubiquitination were calculated and shown under SDS-PAGE gel. (c) Monoubiquitination reactions from (b) were resolved on 6% native PAGE gel for EMSA analysis. The percentage of ID2 binding to DNA was calculated and shown under native PAGE gel.

Previously, we and others showed that various different dsDNA-containing structures could robustly stimulate ID2 monoubiquitination (Longerich et al., 2014; van Twest et al., 2017; Sareen et al., 2012), but that single-stranded DNA (ssDNA) does not. To determine if monoubiquitinated ID2 had increased affinity for other dsDNA containing structures, we repeated the monoubiquitination reactions in the presence of different IR-dye700 labeled DNA structures. Interestingly, non-ubiquitinated ID2 also exhibited high affinity toward 3’ flap DNA structure (similar to a replication fork stalled on the lagging strand), which has been previously observed (Liang et al., 2016). The 3’-Flap structure, and each of the other dsDNA containing structures, led to increased ID2 monoubiquitination and increased retention of an EMSA shifted band (Figure 3). Conversely, ssDNA, which stimulates monoubiquitination more slowly (van Twest et al., 2017) but to similar levels at the long time point of this assay, did not cause an EMSA shift.

![Figure 3.](https://cdn.elifesciences.org/articles/54128/elife-54128-fig3-v2.jpg)

**Figure 3.:** EMSA gels showing binding of monoubiquitinated or unmodified ID2 complex to different oligo-based DNA substrates. Above each panel, a schematic representing the tested DNA substrate is shown. 25, 50 and 100 nM of ID2 or IKRD2KR were incubated with 25 nM of the indicated DNA substrate and the protein:DNA complexes were resolved on 6% PAGE gels (top). The percentage of DNA binding was calculated and shown under each EMSA gel. Coomassie stained SDS-PAGE gel (bottom) showing the ubiquitination reactions used in the EMSA. The percentage of FANCD2 monoubiquitination was calculated and shown under each SDS-PAGE gel.

### Both FANCIub and FANCD2ub are associated with a ‘clamped’ protein:DNA complex

Previous studies reported that monoubiquitination of ID2 complex may lead to dissociation of the heterodimer to its individual subunits, as measured by loss of co-immunoprecipitation of FANCI with FANCD2 (40, 41). In contrast, we did not observe any Ub-mediated dissociation of ID2 in vitro. First, western blotting of the EMSA gels confirmed that the gel shifted DNA band contains both FANCI and FANCD2 proteins (Figure 4a). Second, FANCIUb still co-immunoprecipitated with FANCD2Ub at the plateau of the in vitro ubiquitination reaction (Figure 4b).

![Figure 4.](https://cdn.elifesciences.org/articles/54128/elife-54128-fig4-v2.jpg)

**Figure 4.:** (a) Western blots of the EMSA gels containing 50, 100 and 200 nM of IubD2ub, ID2 or IKRD2KR in the presence of 25 nM IRDye-700 labeled dsDNA (red). Left panels correspond to anti-FANCI antibody (green) and right panels correspond to anti-FANCD2 antibody (green) (b) StrepII affinity purification of mono-ubiquitinated (+ATP) and non-ubiquitinated ID2 (-ATP). (c) EMSA gels (top) and western blots (bottom) showing the monoubiquitination of 25, 50 and 100 nM IWTD2WT, IKRD2WT, IWTD2KR or IKRD2KR in the presence of 25 nM IRDye-700 labeled dsDNA. (d) Western blots of the EMSA gels showing monoubiquitination of 50, 100 and 200 nM IWTD2WT, IKRD2WT, IWTD2KR or IKRD2KR in the presence of 25 nM IRDye-700 labeled dsDNA. FANCI (left, green) and FANCD2 (right, green) remained bound to IRDye-700 labeled DNA (red) after mono-ubiquitination.

To determine the contribution of each of FANCD2Ub and FANCIUb to the clamping of IUbD2 Ub complex to DNA, we used ubiquitination-deficient (KR) mutants in the ubiquitination reaction. FANCIKR:FANCD2WT or FANCIWT:FANCD2KR mutant results in decrease in EMSA shift, and FANCIKR:FANCD2KR did not bind to DNA (Figure 4c). However, this retention on DNA correlated with the extent of FANCD2 monoubiquitination retained by these mutant complexes. Western blotting the EMSA gels confirmed that both FANCD2 and FANCI are found in the EMSA shifted product, although in higher amounts when both proteins are capable of being monoubiquitinated (Figure 4d).

### Mutant forms of ubiquitin can still clamp ID2 onto DNA

We postulated that the altered affinity for DNA induced by monoubiquitination must result from either a conformational change in the ID2 heterodimer after monoubiquitination, or participation of the conjugated ubiquitin directly in protein:DNA or protein:protein binding. To help distinguish these possibilities, we utilized mutants of ubiquitin that have previously been shown to mediate the known protein:ubiquitin or protein:DNA interactions in other ubiquitinated protein interactions (Figure 5a; Husnjak and Dikic, 2012). Each of these Ub mutants were conjugated to ID2 by the FA core complex with similar efficiency (Figure 5b) and their clamping onto DNA was then measured. Mutations in surface patch 1 (F4A, D58A), surface patch 2 (I44A, V70A), a DNA binding residue (K11R) or a tail mutant (L73P) had no apparent effect on DNA clamping (Figure 5c). This result suggests that no canonical surface or region of ubiquitin is critical for DNA clamping of ID2, and instead ubiquitin conjugation to ID2 probably induces a conformational rearrangement of the heterodimer.

![Figure 5.](https://cdn.elifesciences.org/articles/54128/elife-54128-fig5-v2.jpg)

**Figure 5.:** (a) Crystal structure of ubiquitin with ubiquitin mutant sites depicted (PDB: 1UBQ). Hydrophobic binding pockets are indicated in blue and pink. (b) Western blots showing the time course ubiquitination assays of ID2 using wild-type ubiquitin or ubiquitin F4A, V70A, I44A, D58A, K11R and L73P mutants. (c) EMSA gels showing 25, 50 and 100 nM monoubiquitinated ID2 binding to 25 nM IRDye-700 dsDNA using various ubiquitin mutants (top). Western blots of ID2 ubiquitination products were shown at the bottom and the percentage of FANCI and FANCD2 ubiquitination were shown at the bottom of each western blot panel.

### Purification of monoubiquitinated FANCI:FANCD2 complex bound to dsDNA reveals a filamentous architecture

In order to examine the architecture of purified recombinant IUbD2Ub complex in the presence of dsDNA plasmid, we utilized a recombinant Avi-tag ubiquitin construct containing a 3C protease site between the biotinylated Avi-tag and the N-terminus of ubiquitin (Tan et al., 2020a; Figure 6a). This tagged ubiquitin is incorporated onto FANCI:FANCD2 by the FA core complex, allowing Avidin-Sepharose purification of monoubiquitinated ID2 that is then eluted by 3C protease cleavage. We recovered monoubiquitinated FANCI:FANCD2 complex only when FANCI is monoubiquitinated, suggesting that the N-terminus of D2-attached ubiquitin may be buried within the di-ubiquitinated complex, but the N-terminus of ubiquitin attached to FANCI is accessible for avidin binding (Figure 6b).

![Figure 6.](https://cdn.elifesciences.org/articles/54128/elife-54128-fig6-v2.jpg)

**Figure 6.:** (a) Schematic of purification of monoubiquitinated FANCI:FANCD2 using Avi-ubiquitin. (b) Coomassie stained SDS-PAGE gel (top) and western blots (bottom) showing the purification of monoubiquitinated FANCI:FANCD2 complex eluted using PreScission protease (lanes 1–7) compared to without PreScission protease (lanes 8–14). (c–e) Representative negative-stained EM image of purified FANCIub:FANCD2ub complex bound to 2.7 kb plasmid, unmodified FANCI:FANCD2 incubated with 2.7 kb plasmid and unmodified FANCI:FANCD2 complex. Pseudo-colored regions are shown to highlight particular filament-like arrays in FANCIub:FANCD2ub but not other samples.

Using this purified protein, we compared FANCIub:FANCD2ub to unmodified FANCI:FANCD2 using electron microscopy (EM). Surprisingly, we observed that FANCIub:FANCD2ub forms filament-like arrays when bound to dsDNA plasmid (Figure 6c). Such arrays were not observed in the unmodified FANCI:FANCD2 protein preparation in the absence of presence of plasmid DNA, nor in previous investigations of human or Xenopus FANCI:FANCD2 complexes studied by EM (Figure 6d–e and Swuec et al., 2017; Liang et al., 2016; Lopez-Martinez et al., 2019).

When smaller DNA molecules were used as the substrate for ID2 binding, we either observed no filament-like structures (60 bp, Figure 7a) or shorter filament-like structures (150 bp, Figure 7b) compared to structures that were on average 7-8x longer than the characteristic double saxophone structure of ID2 heterodimer in the non-ubiquitinated state (Figure 7c).

![Figure 7.](https://cdn.elifesciences.org/articles/54128/elife-54128-fig7-v2.jpg)

**Figure 7.:** (a–d) Representative EM image of monoubiquitinated FANCI:FANCD2 bound to (a) 60 bp dsDNA, (b) 150 bp dsDNA, (c) 2.7 kb dsDNA, and (d) 2.7 kb dsDNA and Benzonase-treated. Scale bar, 100 nm. Arrows indicate formation of 1–2 ID2 array; boxes indicate multiple ID2 arrays. (e) Representative 2D class average of ID2. Views of the side and top of ID2 are shown, framed in blue for comparison. (f) Representative 2D class average of IubD2ub bound to 60 bp DNA. Views of the side and top of IubD2ub are shown, framed in red for comparison. (g–h) Example comparison of the length (y) and width (x) of class average images ID2 and IubD2ub (likely an overestimate, because uranyl formate staining increases apparent particle size).

The observation that array length correlated with the size of DNA available for ID2 binding strongly suggested that the association between heterodimer subunits in the array was DNA-mediated. To test whether the array of IubD2ub is also dependent upon binding to the same DNA molecule, we examined the plasmid-stimulated ubiquitination reaction products after treatment with the non-specific endonuclease, Benzonase. It is apparent from EM images that addition of Benzonase breaks the long arrays formed by IubD2ub complex into very short or heterodimer-sized units (Figure 7d). This finding is consistent with Benzonase cleaving exposed DNA between IubD2ub units, leading to destabilization of the filamentous arrays. Together our results show that, in vitro, ubiquitination of ID2 leads to a ubiquitin- and DNA- stabilized filament-like structure.

### Single IubD2ub heterodimers on short 60 bp DNA have an altered architecture

Due to variability in the length and shape of filament-like IubD2ub structures on longer DNA molecules we have not been able to uncover the shape or subunit rearrangement of the individual units of the arrays because attempts to class average arrays failed due to a lack of order. However, examination of IubD2ub purified together with short 60 bp DNA allowed us to collect sufficient images of individual particles for analysis. These particles were similar in size to non-ubiquitinated ID2, but it is clear from individual molecule and class average views that the IubD2ub complex forms a distinct architecture from that of ID2 (Figure 7e–f). In particular, the overall shape of individual particles and their class averages reveal a twisting that repositions the solenoid arms of one or both of the subunits bringing them into closer proximity. The conformational change induced appears to reduce the size of ID2 in one direction (x vs y) but not the other (Figure 7g–h), similar to that predicted in a previously proposed model that placed DNA in a channel between FANCI and FANCD2 post DNA binding (Longerich et al., 2014). These images support the view that monoubiquitination induces a conformational change in the ID2 complex that clamps it upon DNA.

## Discussion

The protection of stalled forks by DNA repair factors is essential for proper DNA replication and the maintenance of genome stability. The primary mechanism of replication fork stabilization at interstrand crosslinks, and other replication blocking damage, utilizes the proteins of the FA-BRCA DNA repair pathway. Monoubiquitination of FANCI:FANCD2 by the FA core complex is the central event in this pathway. Here, we showed that monoubiquitination directly clamps the ID2 complex onto double-stranded DNA, and promotes a filament-like coating of long DNA molecules. This finding answers a long-standing question about the nature of the biochemical reaction that is absent in the majority of patients with FA (Wang and Smogorzewska, 2015; Gregory et al., 2003).

‘Fork protection’ involves (i) exclusion of cellular nucleases such as MRE11 and DNA2 from the stalled DNA replication fork, and (ii) specific recruitment of other factors that are able to restart DNA replication (Schlacher et al., 2012; Tian et al., 2017; Madireddy et al., 2016). The role of nuclease exclusion seems most important because inhibition of either of two nucleases, MRE11 or DNA2, can significantly alleviate the sensitivity of FA-BRCA mutant cells to replication stalling agents (Schlacher et al., 2012; Tian et al., 2017). But in many studies, specific association of various repair factors with IUbD2Ub compared to ID2 have been described. These proteins mostly contain ubiquitin-binding domains, providing an impetus for the recruitment-based hypothesis (summary and references in Table 1). However, because these previous studies focused on use of ubiquitination-deficient mutants, they could not address the underlying question of whether ubiquitin on either FANCI, FANCD2 or both proteins directly mediated the interaction. Now, we have shown that none of these proteins specifically bind recombinant purified IUbD2Ub compared to ID2. This finding was unexpected, and included proteins such as SLX4 (FANCP), MCM5, and FAN1, which have a demonstrated and essential role in the FA-pathway (Walden and Deans, 2014; Lossaint et al., 2013; MacKay et al., 2010).

Instead, our data provide direct evidence that ID2 undergoes a conformational change after monoubiquitination, that leads to it becoming clamped on double-stranded DNA. It is likely that in previous cell-based experiments specific interaction between SLX4 and FAN1 with FANCD2 but not FANCD2K561R was observed because FANCD2K561R does not become clamped on DNA, even in the presence of active FA core complex. This finding is supported by the observation that FANCD2K561R also does not becomes chromatin localized at damage sites even after extensive DNA damage (Matsushita et al., 2005). We propose that IUbD2Ub does not demonstrate restricted interaction with any specific protein partner. None-the-less, its retention in chromatin after ubiquitination would be much more likely to bring the complex into proximity of these other DNA repair factors, where it could still influence their activity.

Clamping onto DNA occurs through a ubiquitin-mediated conformational change in the ID2 complex. A ubiquitin binding-domain (UBD) in FANCD2 has previously been shown necessary for the retention of the protein in the chromatin faction, and for strong binding to FANCI (Rego et al., 2012). This UBD domain sits in the FANCD2 structure opposite to where ubiquitin is likely to reside after its conjugation on to FANCI by the FA core complex, and most likely mediates the clamping function and conformational rearrangement. A high-resolution cryo-EM structure of chicken ID2Ub published by Alcón et al alongside our study (Alcón et al., 2020), also uncovered a conformational rearrangement of ID2 that is then stapled in place by ubiquitin:UBD association. Other DNA-binding proteins such as histone H2A show an increased association with DNA after monoubiquitination (Zhang, 2003) and monoubiquitination also increases the DNA occupancy of transcription factors such as FOXO4 and CIITA (Greer et al., 2003). It is possible that ubiquitin to UBD mediated clamping is a general mechanism of protein:DNA target stabilization.

### IUbD2Ub clamped in nucleoprotein arrays

In addition to a conformational change in ID2 induced by monoubiquitination (that has also been concurrently discovered and reported by the Pavletich, Walden and Passmore labs Alcón et al., 2020; Wang et al., 2020; Rennie et al., 2020) we found that monoubiquitinated IUbD2Ub formed large filament-like arrays when it was purified together with plasmid DNA, but not short 60 bp DNA fragments. Fourier Transformation of the EM images did not reveal clear evidence for layer lines, that are expected for fiber diffraction, so we expect that the IUbD2Ub is not a true filament. On average, the length of plasmid-associated structures is 7-8x (but up to 40x) that of that associated with 60 bp DNA. Larger or longer arrays may potentially be obscured from view because the purification strategy makes elution exponentially more difficult with increasing numbers of conjugated ubiquitin-molecules. Steps to remove ‘aggregates’ may have also inadvertently removed larger arrays. However, as the number of potential plasmid DNA binding sites for ID2 was in large excess the concentration of ID2 used to stimulate reaction, there appears to be some purpose to creation of these filamentous arrays. The modular nature of IUbD2Ub arrays suggests that IUbD2Ub binding to DNA is flexible and can adopt multiple conformations, akin to RPA binding and protecting ssDNA (Yates et al., 2018).

There is evidence that IUbD2Ub clamped in nucleoprotein filaments exist in cells. Antibodies against FANCD2 have long been used as a marker of double strand breaks, stalled replication forks and R-loops because the protein forms large, intensely stained foci during S-phase that are increased after treatment with DNA damaging agents (Taniguchi et al., 2002; Schwab et al., 2015; Deans and West, 2009). We suspect that these intense foci are due to coating of DNA around damaged forks, potentially in filamentous arrays similar to those we observed by EM. Support for the large size and extent of DNA binding reflective of filamentous arrays also comes from chromatin immunoprecipitation and sequencing (ChIP-Seq) using anti-FANCD2 (13). FANCD2, and two other damage markers MRE11 and γH2AX, showed no specific localization in a bulk population of cells, but strongly localized adjacent to a Cas9-induced site-specific DNA break. Both γH2AX and FANCD2 produced a broad peak centered at the target site kilobases (kb) to megabases (mb) in length. In contrast, MRE11 is located within a very tight peak within ~100 bp of the break. Chromatin within 1–2 kb of the DSB showed reduced occupancy by γH2AX, consistent with dechromatinization around break sites (Iacovoni et al., 2010), but FANCD2 was present right up to the DSB. Accumulation of FANCD2 increases at the DSB early after cleavage, and accumulates more distant from the DSB progressively with time post-cleavage. This is suggestive of a polymerization of the FANCD2 signal away from the break site, as we hypothesize would occur for a protein that forms a growing array of molecules at broken DNA (Wienert et al., 2019). The conserved function of FANCD2 as a histone chaperone (Sato et al., 2012; Higgs et al., 2018) may even be directly linked to displacement of nucleosomes as filamentous arrays extend into break-adjacent chromatin.

In this study, we also observed direct association of two ID2 heterodimers by co-immunopurification only after the protein becomes monoubiquitinated. This approach, if performed in cells, could be used to further delineate the mechanism and cellular factors required for the extension of IUbD2Ub arrays during fork protection. Of particular interest will be determining the role of BRCA1 in clamping and/or array extension. BRCA1:BARD1 was initially thought to be the E3 for FANCD2 monoubiquitination, because it co-immunoprecipitates FANCD2, and FANCD2 does not form nuclear foci after damage in BRCA1-deficient cells (Raghunandan et al., 2015). However, in various assays it was later shown that FANCD2 monoubiquitination does occur in BRCA1-deficient cells, but it is uncoupled from FANCD2 foci formation (Jacquemont and Taniguchi, 2007; Moriel-Carretero et al., 2017).

### How would a clamped IUbD2Ub array mediate fork protection?

Filamentous structures on DNA play a genome protective role in prokaryotes: eg DAN protein forms a rigid collaborative filament that reduces accessibility during anoxia (Lim et al., 2013), while the Vibrio cholera protein ParA2 forms protective filamentous structures on DNA during segregation (Hui et al., 2010). Structural characterization has demonstrated how these filaments function and, in the case of ParA2, can be targeted therapeutically (Misra et al., 2018). The coating of ssDNA by RPA in eukaryotes, also protect DNA from the activity of nucleases, and directs the specific activity of others (de Laat et al., 1998; Chen et al., 2013; Nguyen et al., 2017). We propose that a FANCIub:D2ub arrays may have a similar stabilizing role on newly synthesized dsDNA at a stalled replication fork. This property would explain why stalled forks are prone to degradation in FA and BRCA patient cells (Schlacher et al., 2012; Tian et al., 2017). In particular, we hypothesize that filamentous DNA-clamped Iub:D2ub could prevent access to DNA by MRE11 and DNA2 nucleases and prevent aberrant ligation of broken DNA to other parts of the genome by non-homologous end-joining.

Second, the tight binding of FANCIub:D2ub to dsDNA, when localized to stalled replication forks, may also prevent the branch migration of replication forks and inhibit their spontaneous or helicase-mediated reversal (Neelsen and Lopes, 2015). Reversed forks are the substrate for degradation by DNA2 and WRN nuclease activities, providing a hypothetical link between the activities of FANCD2-monoubiquitination and the nuclease activity of DNA2 and WRN (Thangavel et al., 2015; Sidorova et al., 2013).

Third, Iub:D2ub arrays may also locally suppress non-homologous end-joining (NHEJ) factors, and/or delineate the newly synthesized chromatin from unreplicated regions during the promotion of templated repair processes such as homologous recombination. FANCD2, FANCI, and components of the FA core complex were identified amongst relatively few other factors, in a genome-wide screen for genes that promote templated repair over NHEJ (Richardson et al., 2017). Stabilization of RAD51 filaments, required for HR, is also an in vitro property of ID2 (Sato et al., 2016), suggesting Iub:D2ub filamentous arrays may exist adjacent to or coincident with RAD51 filaments in cells, in order to provide a polarity to the homologous recombination reaction without loss or gain of genomic sequences.

### Role of FANCI-monoubiquitination

Fanci and Fancd2 have common and distinct functions in mouse models of Fanconi anemia (Dubois et al., 2019), while the double knockout of FANCI and FANCD2 has an unexpectedly distinct phenotype compared to single knockouts in human cells (Thompson et al., 2017). But FANCIK523R expressing cells are less sensitive to DNA damage than FANCI knockout in human cells (Smogorzewska et al., 2007), so what is the role of FANCI monoubiquitination? Previous studies demonstrated that FANCI monoubiquitination is always subsequent to FANCD2 monoubiquitination, both in cells (Sareen et al., 2012) and in biochemical assays (van Twest et al., 2017). FANCI also likely plays a role in recruiting the FA core complex to the substrate (Castella et al., 2015). In this study, we show that FANCI-monoubiquitination is not necessary for clamping of the ID2 complex onto DNA (Figure 4). However, in vivo it is likely that FANCI monoubiquitination plays a critical role in regulating deubiquitination of the ID2 complex. FANCI recruits the deubiquitinating enzyme USP1:UAF1 (Yang et al., 2011), which prevents trapping of monoubiquitinated FANCD2 at non-productive DNA damage sites, but only ID2Uband not IUbD2Ub is a substrate (van Twest et al., 2017). It is also clear from our EM investigations that FANCI must play an important role in the structural integrity of IUbD2Ub filamentous arrays on DNA, possibly creating an asymmetry necessary for a specific polarity to array assembly.

### Implications for understanding the deficiency of Fanconi anemia

Onset of progressive bone marrow failure occurs at a median age of 7 in children with FA (Butturini et al., 1994). Almost all these patients lack FANCD2 and FANCI monoubiquitination, due to mutation in either FANCD2 or FANCI or one of the nine other FANC proteins required for their monoubiquitination (Walden and Deans, 2014). The importance of the monoubiquitin signal is highlighted by the observation that up to 20% of patients acquire somatic reversion of the inherited mutation in a fraction of blood cells (Soulier et al., 2005). These mutations restore monoubiquitination and prevent bone marrow failure. Our work suggests two potential strategies for treatment of FA: restoration of gene function, such as that which occurs in somatic revertants or, identification of novel mechanisms to stabilize an ID2:DNA-clamped complex for fork protection by ubiquitin-mediated or innovative means. New small molecule activators or inhibitors of ID2:DNA clamping could be therapeutics in FA or cancer-treatment. In vitro biochemistry has proven to be the most powerful tool in uncovering new functions of FANCD2-monoubiquination that had gone undiscovered for nearly 20 years. The approach is likely to be formidable in drugging the FA pathway in future studies.

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
      <td>Recombinant DNA reagent (X. laevis)</td>
      <td>pFastbac1-FLAG-xFANCI</td>
      <td>(Klein Douwel et al., 2014)</td>
      <td></td>
      <td>Gift from Puck Knipscheer</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (X. laevis)</td>
      <td>pFastbac1-StrepII-xFANCD2</td>
      <td>(Klein Douwel et al., 2014)</td>
      <td></td>
      <td>Gift from Puck Knipscheer</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (H. sapiens)</td>
      <td>pFL-EGFP-His-hFANCI</td>
      <td>(Tan et al., 2020a)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (H. sapiens)</td>
      <td>pFastbac1-FLAG-hFANCD2opt</td>
      <td>(Tan et al., 2020a)</td>
      <td>RRID:Addgene_ 134904</td>
      <td>Gift from Angelos Constantinou</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (H. sapiens)</td>
      <td>pFL/pSPL-EGFP-FLAG-B-L-100</td>
      <td>(van Twest et al., 2017)</td>
      <td></td>
      <td>Codon optimized FANCB</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (H. sapiens)</td>
      <td>pFL-MBP-C-E-F</td>
      <td>(van Twest et al., 2017)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (H. sapiens)</td>
      <td>pGEX-KG-GST-UBE2T</td>
      <td>(van Twest et al., 2017)</td>
      <td></td>
      <td>Codon optimized</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (E. coli)</td>
      <td>pet16b-Avi-ubiquitin_rbs_BirA</td>
      <td>(Tan et al., 2020a)</td>
      <td>RRID:Addgene_134897</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (E. coli)</td>
      <td>pSRK2706-GST-HRV-3Cprotease</td>
      <td>(Raran-Kurussi and Waugh, 2016)</td>
      <td>RRID:Addgene_78571</td>
      <td>A gift from David Waugh</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent (E. coli)</td>
      <td>pUC19 plasmid</td>
      <td>New England BioLabs</td>
      <td>N3041S</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (E. coli)</td>
      <td>BL21 (DE3)</td>
      <td>Agilent Technologies</td>
      <td>200131</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Spodoptera frugiperda)</td>
      <td>Sf9</td>
      <td>Thermo Fisher Scientific</td>
      <td>RRID:CVCL_0549</td>
      <td>Maintained in Sf-900 II SFM</td>
    </tr>
    <tr>
      <td>Cell line (Trichoplusia ni)</td>
      <td>High Five</td>
      <td>Thermo Fisher Scientific</td>
      <td>RRID:CVCL_C190</td>
      <td>Maintained in Sf-900 II SFM</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal antibodies against StrepII</td>
      <td>Abcam</td>
      <td>RRID:AB_76949</td>
      <td>one in 3000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal antibodies against FANCI</td>
      <td>Abcam</td>
      <td>RRID:AB_74332</td>
      <td>one in 3000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit polyclonal antibodies against FANCD2</td>
      <td>Abcam</td>
      <td>RRID:AB_10862535</td>
      <td>one in 3000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal antibodies against FLAG</td>
      <td>Aviva Biosciences</td>
      <td>RRID:AB_10884242</td>
      <td>one in 3000 dilution</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>FLAG peptide</td>
      <td>Sigma-Aldrich</td>
      <td>F3290</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Recombinant Human His6-Ubiquitin E1 Enzyme carrier free</td>
      <td>Boston Biochem</td>
      <td>E-304–050</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Ubiquitin and associated mutant variants</td>
      <td>Boston Biochem</td>
      <td>U-110H, UM-I44A, UM-D58A, UM-F4A, UM-L73P, UM-K11R</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TNT T7 Quick Coupled Transcription/Translation System</td>
      <td>Promega Corporation</td>
      <td>L1170</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Anti-FLAG-M2 affinity gel</td>
      <td>Sigma Aldrich</td>
      <td>RRID:AB_10063035</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>EasyTagL-[35S]-Methionine</td>
      <td>PerkinElmer Life Sciences</td>
      <td>NEG709A500UC</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>XMIPP</td>
      <td>(de la Rosa-Trevín et al., 2013)</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Protein purification

Flag-FANCI and StrepII-FANCD2 were expressed using the pFastBac1 vector (Life Technologies). For FANCI:FANCD2 complex, Hi5 cell pellets were resuspended in lysis buffer (50 mM Tris-HCl pH 8.0, 0.1 M NaCl, 1 mM EDTA, 10% glycerol and 1X mammalian protease inhibitor), and sonicated. Lysates were clarified by centrifugation at 20,000 g and the supernatants were incubated with M2 anti-FLAG agarose resin for 2 hr. The resin was washed 5 × 5 min incubation with wash buffer (20 mM Tris-HCl pH 8.0, 0.1 M NaCl, 10% glycerol), and the protein was eluted in the same buffer containing 100 μg/mL FLAG peptide. GST-UBE2T, Flag-BL100, MBP-CEF were purified as described (van Twest et al., 2017). Ubiquitin and His-UBE1 were purchased from Boston Biochem.

### Biotinylated-Avi-ubiquitin purification

His-Avi-ubiquitin was purified as described in Tan et al. (2020a).

### In vitro ubiquitination assay

Standard ubiquitination reactions contained 10 μM recombinant human avidin-biotin-ubiquitin, 50 nM human recombinant UBE1, 100 nM UBE2T, 100 nM PUC19 plasmid, 2 mM ATP, 100 nM FANCI:FANCD2 complex wild type (WT) or ubiquitination-deficient (KR), in reaction buffer (50 mM Tris-HCl pH 7.4, 2.5 mM MgCl2, 150 mM NaCl, 0.01% Triton X-100). 20 μL reactions were set up on ice and incubated at 25°C for 90 min. Reactions were stopped by adding 10 μL NuPage LDS sample buffer and heated at 80°C for 5 min. Reactions were loaded onto 4–12% SDS PAGE and run using NuPAGE MOPS buffer and assessed by western blot analysis using Flag (Aviva Biosciences) or StrepII (Abcam) antibody.

### In vitro transcription/translation pull down of 35S-labeled proteins

Flag-tagged FANCI:FANCD2 and monoubiquitinated FANCI:FANCD2 was prepared by incubating purified FANCI:FANCD2 or monoubiquitinated FANCI:FANCD2 on Flag beads for 2 hr followed by extensive washes in buffer A (20 mM TEA pH 8.0, 150 mM NaCl, 10% glycerol). 35S-labeled proteins containing UBZ or other ubiquitin domains (Table 1) were generated using the TNT Quick Coupled T7 Transcription/Translation System (Promega) and 35S-labeled methionine (Perkin Elmer). 10 μL of TNT product was incubated for 4 hr at 4°C in buffer A with 100 ng Flag-tagged FANCI:FANCD2 or monoubiquitinated FANCI:FANCD2, 20 μL of Flag-beads (Sigma-Aldrich) in a 100 μL reaction. Beads were washed five times with buffer A and resuspended in LDS loading buffer. Proteins were separated by SDS-PAGE and visualized by autoradiography.

### Electrophoretic mobility shift assay

Oligonucleotides used to create fluorescently labeled DNA were IRDYE-700-labeled X0m1 (IDTDNA) and other oligos with the sequences shown in Supplementary file 1. Assembly of the different DNA structures was performed exactly as previously described (Supplementary file 1; van Twest et al., 2017). 25 nM DNA substrates were incubated in 20 μL ubiquitination buffer containing 100 nM FANCI:FANCD2, 100 nM BL100, 100 nM CEF, 10 uM HA-ubiquitin (Boston Biochem), 50 nM UBE1 (Boston Biochem) and 100 nM UBE2T at room temperature for 90 min to initiate ubiquitination. The reaction was resolved by electrophoresis through a 6% non-denaturing polyacrylamide gel in TBE (100 mM Tris, 90 mM boric acid, 1 mM EDTA) buffer and visualized by Licor Odyssey system.

### Purification of monoubiquitinated FANCI:FANCD2 complex

Di-monoubiquitinated FANCI:FANCD2 complex was purified as described (Tan et al., 2020a). DNA molecules of 60 bp or 150 bp (dsDNA from oligonucleotides) or 2.6 kb (circular plasmid DNA) were used to stimulate the reaction for different experiments, as indicated.

### Mass spectrometry analysis of monoubiquitinated FANCI:FANCD2 complex

Gels containing monoubiquitinated FANCI and FANCD2 bands were excised and in-gel digested with trypsin and subjected to LC/MS analysis on ESI-FTICR mass spectrometer at Bio21, The University of Melbourne. The analysis program MASCOT was used to identify ubiquitination sites on FANCI and FANCD2.

### Negative stain electron microscopy

Freshly purified monoubiquitinated or non-ubiquitinated FANCI:FANCD2 complex was applied to glow-discharged, carbon/formvar grids and allowed to adsorb for 60 s. Specimen was then stained with 2% uranyl formate for 60 s. Specimen were imaged at a magnification of 73,000 x on a Ceta camera (corresponding to a pixel size of 1.9 Å) in Talos 120 kV. For FANCI:FANCD2 complex, 20 micrographs were analyzed and 4553 particles were picked for 2D classification. For monoubiquitinated FANCI:FANCD2 complex, 20 micrographs were analyzed and 4698 particles were picked for 2D classification. The length and width of 2D class average were measured using ImageJ.

### Single-particle image processing

Monoubiquitinated or non-ubiquitinated FANCI:FANCD2 particles were semi-automatically picked using XMIPP3 (83). The parameters of the contrast transfer function (CTF) for negative stained data was estimated on each micrograph using CTFFIND3 (Mindell and Grigorieff, 2003). Finally, reference free 2D alignment and averaging were executed using XMIPP3.
