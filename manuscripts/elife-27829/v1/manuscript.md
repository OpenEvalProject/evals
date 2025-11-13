# Structure-based analysis of CysZ-mediated cellular uptake of sulfate

## Authors

- Zahra Assur Sanghai<sup>1</sup>
- Qun Liu<sup>3</sup>
- Oliver B Clarke<sup>2</sup> ([ORCID: 0000-0003-1876-196X](https://orcid.org/0000-0003-1876-196X))
- Meagan Belcher-Dufrisne<sup>1</sup>
- Pattama Wiriyasermkul<sup>4</sup>
- M Hunter Giese<sup>1</sup>
- Edgar Leal-Pinto<sup>5</sup>
- Brian Kloss<sup>7</sup>
- Shantelle Tabuso<sup>7</sup>
- James Love<sup>7</sup>
- Marco Punta<sup>8</sup>
- Surajit Banerjee<sup>9</sup>
- Kanagalaghatta R Rajashankar<sup>9</sup>
- Burkhard Rost<sup>10</sup>
- Diomedes Logothetis<sup>5</sup>
- Matthias Quick<sup>4</sup>
- Wayne A Hendrickson<sup>1</sup>
- Filippo Mancia<sup>1</sup> ([ORCID: 0000-0003-3293-2200](https://orcid.org/0000-0003-3293-2200)) †

### Affiliations

1. Department of Physiology and Cellular Biophysics Columbia University New York United States
2. Department of Biochemistry and Molecular Biophysics Columbia University New York United States
3. Biology Department Brookhaven National Laboratory Upton United States
4. Center for Molecular Recognition, Department of Psychiatry Columbia University New York United States
5. Department of Physiology and Biophysics Virginia Commonwealth University School of Medicine Richmond United States
6. Department of Pharmaceutical Sciences, School of Pharmacy Bouvé College of Health Sciences, Northeastern University Boston United States
7. New York Structural Biology Center New York United States
8. Centre for Evolution and Cancer The Institute of Cancer Research London United Kingdom
9. Department of Chemistry and Chemical Biology Cornell University, NE-CAT Argonne United States
10. Department of Informatics Technical University of Munich Munich Germany
11. Division of Molecular Therapeutics New York State Psychiatric Institute New York United States

† Corresponding author

## Abstract

Sulfur, most abundantly found in the environment as sulfate (SO42-), is an essential element in metabolites required by all living cells, including amino acids, co-factors and vitamins. However, current understanding of the cellular delivery of SO42- at the molecular level is limited. CysZ has been described as a SO42- permease, but its sequence family is without known structural precedent. Based on crystallographic structure information, SO42- binding and flux experiments, we provide insight into the molecular mechanism of CysZ-mediated translocation of SO42- across membranes. CysZ structures from three different bacterial species display a hitherto unknown fold and have subunits organized with inverted transmembrane topology. CysZ from Pseudomonas denitrificans assembles as a trimer of antiparallel dimers and the CysZ structures from two other species recapitulate dimers from this assembly. Mutational studies highlight the functional relevance of conserved CysZ residues.

## Introduction

Sulfur has a central role in many cellular processes across all kingdoms of life. It is a vital component of several essential compounds, including the sulfur-containing amino acids cysteine and methionine, in prosthetic groups such as the Fe-S clusters, as well as vitamins and micronutrients such as biotin (vitamin H), thiamine (vitamin B1) and lipoic acid, and in coenzymes A and M (Barton, 2005). Whilst mammals obtain the majority of the necessary sulfur-containing metabolites directly from the diet, plants, fungi, and bacteria are able to assimilate and utilize sulfur from organic and inorganic sources (Barton, 2005). Sulfate (SO42-) is the most abundant source of sulfur in the environment and its utilization is contingent upon its entry into the cell (Kertesz, 2000). In certain fungi, and prokaryotes, once internalized, SO42- is first reduced to sulfite (SO32-), and then further to sulfide (S2-), a form that can be used by the cell (Kredich et al., 1979) (Figure 1—figure supplement 1). In Escherichia coli and other gram-negative bacteria, the culmination of the aforementioned sulfate assimilatory (also known as reductive) pathway is the formation of cysteine by the addition of S2- to O-acetylserine by cysteine synthase, followed by the synthesis of methionine from homocysteine (Kredich, 1971) (Figure 1—figure supplement 1).

In prokaryotes, the entry of SO42- into the cell is mediated by four known families of dedicated transport systems: the ABC sulfate transporter complexes SulT or CysTWA, the SulP family of putative SLC13 sodium:sulfate or proton:sulfate symporters or SLC26 solute:sulfate exchangers, the phosphate transporter-like CysP/PitA family, and the CysZ family classified as SO42- permeases (Aguilar-Barajas et al., 2011; Hryniewicz et al., 1990; Kertesz, 2001; Loughlin et al., 2002; Mansilla and de Mendoza, 2000; Sirko et al., 1995). CysZ family members are 28–30 kDa bacterial inner-membrane proteins found exclusively in prokaryotes with no apparent homology to any of the established channel or transporter folds, and are scarcely studied in the literature (Zhang et al., 2014). The cysZ gene owes its name to its presence in the cysteine biosynthesis regulon. In two reports from thirty years ago, an E. coli K-12 strain with a cysZ deletion showed a severe impairment in its ability to accumulate SO42- and was not viable in sulfate-free media without an alternate sulfur source such as thiosulfate (S2O32-) (Britton et al., 1983; Parra et al., 1983). More recently, a third report studying the functional properties of CysZ, concluded that the protein from E. coli functions as a high affinity, highly specific pH-dependent SO42- transporter, directly regulated by the toxic, assimilatory pathway intermediate, SO32- (Zhang et al., 2014).

To investigate the role of CysZ in cellular sulfate uptake at a molecular level, we have undertaken an approach that combines structural and functional studies. To this end, we determined the crystal structures of CysZ from three species, Idiomarina loihiensis (Il; IlCysZ), Pseudomonas fragi (Pf; PfCysZ), and Pseudomonas denitrificans (Pd; PdCysZ), and characterized CysZ function in purified form, predominantly in reconstituted proteoliposomes, but also in cells, and to a lesser extent, in planar lipid bilayers. Combining the structural information from the three orthologs reveals that CysZ features a novel protein fold that assembles as oligomers with an inverted transmembrane topology. This arrangement can be understood as being derived from trimers of dimers akin to the hexameric assembly captured in one of the structures. Interpreting the functional data in a structural context has allowed us to formulate a mechanistic model for CysZ-mediated SO42- translocation across the bacterial cytoplasm membrane.

Both the structures and the functional properties of CysZ proteins are distinct from those of any known membrane transporter or ion channel. Besides not resembling other transporter structures, CysZ mediates sulfate flux into cells or proteoliposomes without coupling to ion gradients, partner proteins, or exogenous energy sources such as ATP. These distinctive properties make CysZ appealing as a model system for studies of biophysical principles of membrane protein biogenesis and transmembrane ion passage.

## Results

### Structure determination of CysZ

Following a structural genomics approach aimed at crystallization for structural analysis, we cloned and screened a total of 63 different bacterial homologs of CysZ for high-level expression and stability in detergents (Love et al., 2010; Mancia and Love, 2011). Crystal structures were determined for CysZ from three organisms. Chronologically, the structure of IlCysZ was the first solved, to 2.3 Å resolution in space group C2 by SAD, initially based on a single selenate ion bound to the protein and subsequently also by selenomethione derivatization (SeMet) SAD, and multi-crystal native SAD (Liu et al., 2012). The structure of PfCysZ was solved second, to 3.5 Å resolution, with crystals also belonging to space group C2. Although PfCysZ and IlCysZ share 42% sequence identity, molecular replacement failed to find a convincing solution, and we instead used SeMet-derivatized PfCysZ to obtain phase information by multi-crystal SeMet SAD. Third, we determined the structure of PdCysZ, which crystallized in multiple forms belonging to space groups P63, P4122 and P212121, revealing the same architecture and oligomeric assembly each time (Figure 1—figure supplement 2b). PdCysZ structures in the P63 and P212121 lattices each contain an entire hexamer in their asymmetric units, whereas a molecular diad coincides with a crystallographic axis in the P4122 lattice. We focused our analysis on the best of these (3.4 Å resolution in P63). The location of the selenium sites was obtained from a SeMet SAD data set, and the structure was solved by combining the resulting SAD phases with those from a molecular replacement solution obtained by positioning the PfCysZ model (75% sequence identity) onto SeMet fiducials in the initial electron density map (Table 1, Figure 1—figure supplement 2a).

**Table 1.**
 Crystallographic data and refinement statistics.


<table>
  <thead>
    <tr>
      <th>Data collection</th>
      <th>Native IlCysZ</th>
      <th>IlCysZ w/SeO42- (SAD)</th>
      <th>SeMet PfCysZ (six crystals, refinement)</th>
      <th>SeMet PfCysZ (15 crystals, SAD)</th>
      <th>Native PdCysZ (MR-SAD)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Beamline</td>
      <td>NSLS X4A</td>
      <td>NSLS X4A/C</td>
      <td>APS 24-ID-E</td>
      <td>APS 24-ID-C</td>
      <td>APS 24-ID-C</td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>C2</td>
      <td>C2</td>
      <td>C2</td>
      <td>C2</td>
      <td>P63</td>
    </tr>
    <tr>
      <td>Cell dimensions:</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>128.9, 82.0, 100.4</td>
      <td>128.9, 81.9, 100.3</td>
      <td>172.29, 56.9, 96.17</td>
      <td>172.35, 56.9, 96.31</td>
      <td>225.13, 225.13, 96.62</td>
    </tr>
    <tr>
      <td>α, β, γ (°)</td>
      <td>90, 125.1, 90</td>
      <td>90, 125.1, 90</td>
      <td>90, 91.43, 90</td>
      <td>90, 91.33, 90</td>
      <td>90, 90, 120</td>
    </tr>
    <tr>
      <td>Za</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Wavelength</td>
      <td>1.7432</td>
      <td>0.96789</td>
      <td>0.97890</td>
      <td>0.97890</td>
      <td>1.0230</td>
    </tr>
    <tr>
      <td>Bragg spacings (Å)</td>
      <td>30–2.30</td>
      <td>50–2.10</td>
      <td>40–3.20</td>
      <td>40–3.50</td>
      <td>86–3.40</td>
    </tr>
    <tr>
      <td>Rmerge</td>
      <td>0.047 (0.257)</td>
      <td>0.046 (0.417)</td>
      <td>0.136 (6.506)</td>
      <td>0.135 (2.13)</td>
      <td>0.095 (2.89)</td>
    </tr>
    <tr>
      <td>I / σI</td>
      <td>29.4 (7.9)</td>
      <td>25.0 (1.9)</td>
      <td>12.3 (0.7)</td>
      <td>24.2 (2.6)</td>
      <td>22.4 (1.2)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>99.9 (99.9)</td>
      <td>99.9 (100.0)</td>
      <td>99.8 (99.3)</td>
      <td>99.9 (100.0)</td>
      <td>100.0 (100.0)</td>
    </tr>
    <tr>
      <td>Multiplicity</td>
      <td>7.3 (7.2)</td>
      <td>7.6 (7.6)</td>
      <td>27.2</td>
      <td>72.8</td>
      <td>19.7</td>
    </tr>
    <tr>
      <td>Refinement:</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>2.30</td>
      <td></td>
      <td>3.50</td>
      <td></td>
      <td>3.40</td>
    </tr>
    <tr>
      <td>No. of reflections</td>
      <td>38075</td>
      <td></td>
      <td>20741</td>
      <td></td>
      <td>37251</td>
    </tr>
    <tr>
      <td>Rwork/Rfree</td>
      <td>0.200/0.238</td>
      <td></td>
      <td>0.297/0.339</td>
      <td></td>
      <td>0.245/0.289</td>
    </tr>
    <tr>
      <td>No. of atoms:</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>3679</td>
      <td></td>
      <td>3428</td>
      <td></td>
      <td>11415</td>
    </tr>
    <tr>
      <td>Ligand/ion</td>
      <td>249</td>
      <td></td>
      <td>0</td>
      <td></td>
      <td>400</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>162</td>
      <td></td>
      <td>0</td>
      <td></td>
      <td>0</td>
    </tr>
    <tr>
      <td>Average B-factors (Å2) Protein Ligand/Ion Water</td>
      <td>49.4 48.4 77.3 45.3</td>
      <td></td>
      <td>198.9 198.9 - -</td>
      <td></td>
      <td>178.58 179.06 164.88 -</td>
    </tr>
    <tr>
      <td>Bond Ideality (r.m.s.d.):</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bond lengths (Å)</td>
      <td>0.006</td>
      <td></td>
      <td>0.006</td>
      <td></td>
      <td>0.010</td>
    </tr>
    <tr>
      <td>Bond angles (°)</td>
      <td>0.894</td>
      <td></td>
      <td>1.133</td>
      <td></td>
      <td>0.96</td>
    </tr>
    <tr>
      <td>Ramachandran Analysis: Favored (%)</td>
      <td>99.0</td>
      <td></td>
      <td>99.2</td>
      <td></td>
      <td>96.27</td>
    </tr>
    <tr>
      <td>PDB accession code</td>
      <td>3TX3</td>
      <td></td>
      <td>6D79</td>
      <td></td>
      <td>6D9Z</td>
    </tr>
  </tbody>
</table>

_Values in parentheses are from the highest resolution shell. Rfree was calculated using 5% of data excluded from refinement._

### The hexameric structure of PdCysZ

The refined structure of PdCysZ comprises an entire hexamer of near-perfect D3 symmetry. Antiparallel pairs of protomers arrange together as a trimer of dimers (Figure 1a), with the three-fold axis oriented perpendicular to the plane of the putative membrane and three two-fold axes between dimers of the hexamer. Both the periplasmic and cytoplasmic faces of the hexamer are essentially identical by symmetry, resulting in a dual-topology assembly for PdCysZ. The hexamer has a triangular face of equal sides measuring approximately 75 Å, with the perpendicular span of about 65 Å. The interaction of the six protomers results in a total buried surface area (Krissinel and Henrick, 2007) of 5,700 Å2. A surface electrostatic representation reveals a hydrophobic belt along the mid-section of the hexamer when viewed from its side, outlining the orientation of CysZ in the lipid bilayer (Czodrowski et al., 2006; Dolinsky et al., 2007; Dolinsky et al., 2004) (Figure 1b). A surface representation of the sequence conservation, calculated by analysis of multiple sequence alignments (MSA) (Ashkenazy et al., 2016; Glaser et al., 2003) highlights the regions of invariance in the sequence and in turn, the areas on the molecule that are most likely to have structural and functional importance (Figure 1c).

![Figure 1.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig1-v1.jpg)

**Figure 1.:** (a) Side and top views of the hexamer as a ribbon diagram with each protomer chain colored differently. The approximate dimensions of the hexamer marked in Å. (b) Side and top views represented by surface electrostatics as calculated by APBS, with negative and positive surface potential represented in red and blue respectively. (c) Side and top views representing conservation of residues as calculated by ConSurf, with maroon being most conserved to cyan being least conserved.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Assimilatory reduction is energetically dispendious as sulfate is extremely stable. In this pathway, sulfate ions enter the cell via a transporter or channel, like CysZ; this is followed by its activation by ATP-sulfurylase, which utilizes ATP to form adensosine phosphosulfate (APS) and inorganic pyrophosphate (PPi) as a by-product. APS is then further activated by the addition of a second phosphate forming phosphoadenosine phosphosulfate (PAPS) and this high-energy intermediate product is poised for sulfur removal to form sulfite (SO32-) by the thioredoxin enzyme, which is then further reduced to sulfide ions (S-). Sulfide, the final reduced sulfur product, can then be used in a variety of ways by the cell, such as the incorporation into O-acetylserine to synthesize cysteine.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (a) Representative electron density in blue mesh for: IlCysZ, contoured at 1 x r.m.s.d., PfCysZ, contoured at 2 x r.m.s.d, with a negative B-factor of −100 Å2 applied to map; PdCysZ, contoured at 1 x r.m.s.d, with a negative B-factor of −100 Å2 applied to map. Final atomic models (Cα trace with side chains depicted) are shown as yellow stick representation. (b) Preliminary molecular replacement analyses of the three different crystal forms obtained for PdCysZ, showing the hexameric assembly of the molecule, seen in each case. The Cα trace of an asymmetric unit in each crystal form is depicted in grey, with their symmetry mates shown in yellow. Space group and unit cell dimensions (in Å) are listed below.

The CysZ protomer is an alpha-helical integral membrane protein with two long transmembrane (TM) helices (H2b and H3a) and two pairs of shorter helices (H4b-H5a and H7-H8) that insert only partially into the membrane (hemi-penetrating), forming a funnel or tripod-like shape within the membrane (Figure 2a,b). The protein has an extra-membranous hydrophilic ‘head’, comprising an iris-like arrangement of the two short helices, H1 and H6, and kinked helices H3b, H4a, and H5b. The amino and carboxyl termini are also located in this region (Figure 2a,b). Helices H4b and H5a lie partly inserted in the membrane, with the turn between the two pointing in towards the three-fold axis at the center of the hexamer. CysZ amino-acid sequences from different organisms are very similar; for example, those of PdCysZ and E. coli CysZ (EcCysZ) are 40.5% identical and those of EcCysZ and our three structures have 30.0% of their residues exactly in common (Figure 2c). Helix boundaries are also essentially the same in the structures of PdCysZ, IlCysZ and PfCysZ (Figure 2c).

![Figure 2.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig2-v1.jpg)

**Figure 2.:** (a) Ribbon representation of the PdCysZ protomer colored in rainbow colors from N (blue) to C terminus (red), viewed from within the plane of the membrane, shown in the same orientation as the protomer drawn in green in Figure 1a. (b) Topology diagram of the PdCysZ protomer with helices marked from 1 to 8. Helices H2b and H3a are transmembrane helices, whereas helices H4-H5 and H7-H8 are hemi-penetrating helical hairpins, only partially inserted into the membrane. (c) Sequence alignment of E. coli CysZ (EcCysZ), P. denitrificans CysZ (PdCysZ), P. fragi CysZ (PfCysZ), and I. loihiensis CysZ (IlCysZ). Residues are colored based on conservation, with maroon being most conserved and cyan least conserved, as calculated by ConSurf using a sequence alignment of 150 non-redundant sequences from the CysZ family as input. Spirals above residues mark the extent of the helical segments based on the atomic structure of PdCysZ with helices numbered H1-H8; letters mark residue identities; black dots above identify every tenth residue (modulo 10) in the PdCysZ sequence and black underlines mark functionally relevant motifs discussed in the text.

### The dimeric assembly of IlCysZ and PfCysZ

Unlike PdCysZ, both IlCysZ and PfCysZ crystallize as dimers (Figure 3a,b), in agreement with their different behavior in detergent-containing solution. Indeed, size-exclusion chromatography runs of the three species of CysZ in the same buffer and detergent conditions, show mono-disperse peaks eluting at 13.42 ml (IlCysZ), 13.95 ml (PfCysZ) and 12.56 ml (PdCysZ) (Figure 3—figure supplement 1). This result is consistent with a different and smaller oligomeric state of IlCysZ and PfCysZ (similar retention volume) compared to PdCysZ (eluting 1 ml ahead).

![Figure 3.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig3-v1.jpg)

**Figure 3.:** (a) Ribbon diagram of the structure of CysZ from I. loihiensis (IlCysZ) at 2.3 Å. Protomers of the dimer are colored in salmon pink and teal blue, arranged in a head-to-tail conformation in the membrane, with helical hairpins H2-H3 and H4-H5 labeled for clarity. The dimer interface of IlCysZ involves helices H2-H3. (b) Ribbon diagram of the structure of CysZ from P. fragi (PfCysZ) at 3.2 Å. The protomers of the dual topology dimer in the membrane are colored gold and purple, with helical hairpins H2-H3 and H4-H5 again labeled. The dimer interface here involves the interaction of helices H4-H5 of each protomer. (c) Side and top views of the superposition of the three different protomers from PdCysZ (green), IlCysZ (pink) and PfCysZ (yellow) after aligning helices H1-H3, with a curved arrow indicating the flexible nature of helices H4-H5. d, e. The same dimer interfaces observed in IlCysZ (a) and PfCysZ (b) observed in the hexameric assembly of PdCysZ, as highlighted in green and blue (d) and green and orange (e). (f) Schematic representation showing how three copies of the dimeric protomers of IlCysZ (green and blue, left) and of PfCysZ (orange and green, center), can coexist in and each recapitulate the hexameric assembly of PdCysZ.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** All three proteins were solubilized from isolated membrane fractions purified in the presence of 0.2% decyl maltopyranoside (DeM) and exchanged into buffer containing 1% β-octyl glucopyranoside (β-OG) on the size-exclusion column (Superdex 200 10/30 HR). Schematic of the oligomeric states observed in the three crystal structures of CysZ are shown below the elution profiles. Crystallization trials were set-up directly after the size-exclusion chromatography step. A shift of ~1 ml was observed for the elution of PdCysZ (peak at 12.56 ml), with respect to PfCysZ and IlCysZ, indicating that the size (volume) and shape of PdCysZ is significantly larger than the other two species. IlCysZ elutes at 13.42 ml, 0.5 ml ahead of PfCysZ, which could be explained by the shape of IlCysZ, occupying more volume as compared to PfCysZ, with its helices (H4–H5) pointing outward, away from the body of the dimer.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (a) A depiction of the surface electrostatic potentials of the IlCysZ dimer with negative surface potential represented in red, and positive potential in blue as calculated by APBS. (b) Surface of IlCysZ rendered by level of hydrophicity, using the Kyte-Doolitle hydrophobicity scale with cyan being most polar, to orange being most hydrophobic, reveals a hydrophobic belt along the center of the dimer, suggesting the orientation of the dimer in the lipid bilayer. (c, d) Single cysteine mutants were designed to be located along the length of helix H4 of CysZ, to gauge the extent of its membrane insertion. The labeled protein was extracted from the membrane and purified after quenching the labeling reaction. Fluorescence intensity was measured and quantified by a Tecan fluorescence plate reader at an excitation of 485 nm and emission of 535 nm the results of which were plotted on the left, with error bars representing the standard deviation from the mean for n = 3. The results show that of all the residues on the helix, only R132C (the top-most residue) was accessible to the fluorophore and hence exposed out of the membrane. (d) Locations of the mutated residues on helix H4 are marked on the model of IlCysZ in green. Crosslinking of L161C-A164C cysteine mutant of PfCysZ and IlCysZ exhibits dimer formation. (e) A depiction of the surface electrostatic potentials of the PfCysZ dimer with negative surface potential represented in red, and positive potential in blue as calculated by APBS, highlights hydrophobic belt marking the orientation of the PfCysZ dimer in the membrane. (f) Membrane orientation of PfCysZ predicted by OPM/PPM server shows its 31-degree tilt to the perpendicular, with a zoomed in view of the location of the cysteine mutants at the dimer interface, used for crosslinking of the dimer. (g, h) Dimer formation by the crosslinking of PfCysZ (g) and of IlCysZ (h) with introduced structure-based cysteine substitution mutations in the helices H4-H5 dimer interface. Analogous pairs of cysteine mutants from each species are shown here: PfCysZ L161C-A164C and IlCysZ L156C-Q163C and V157C-Q163C. Sulfydryl specific Bis-MTS crosslinkers of a certain spacer length (in this case 5.2 Å) were used at 0.5 mM for 1 hr at room temperature to crosslink the protein. Experiment was performed on protein in the membrane, as well as on solubilized protein. WT protein (cysteine-less) was used as a control. Proteins were purified after stopping the reaction, and run on an SDS PAGE with reducing dye, and stained with Coomassie blue.

The protomers of the IlCysZ dimer are arranged in a head-to-tail antiparallel association, with helices H4b-H5a protruding at an angle that is nearly parallel to the putative plane of the membrane (Figure 3a and -figure supplement 2a,b). The PfCysZ dimer is also arranged in an antiparallel orientation but with a different dimer interface (Figure 3b). In the PfCysZ structure, helices H4b-H5a together form a narrower angle with helices H2 and H3, and tuck-in closer to the rest of the molecule (Figure 3b). The resulting dumbbell-shaped PfCysZ dimer is predicted, by OPM/PPM (Orientation of Proteins in Membranes) (Lomize et al., 2012), to lie in the membrane at a 31° tilt to the perpendicular, in agreement with the position of its central hydrophobic belt, as revealed by surface-electrostatics calculations (Figure 3—figure supplement 2e,f). The dimer interfaces of IlCysZ and PfCysZ bury 780 Å2 and 1136 Å2 of surface area respectively (Krissinel and Henrick, 2007)

The individual protomers of CysZ from all three species adopt the same topology and fold, and superpose well with an overall pairwise root mean squared deviation (r.m.s.d) of ~2.5 Å (Figure 3c). The greatest variation between the protomers of each structure is seen in the orientation of helices H4b-H5a with respect to the TM helices H2 and H3 (Figure 3c), which seem to be the most conformationally flexible with respect to the rest of the molecule.

Comparison of the structures of IlCysZ and PfCysZ with that of PdCysZ revealed that these two distinctive dimeric structures are both represented in the hexameric one. Indeed, the IlCysZ dimer (Figure 3a) resembles the vertically arranged pair of protomers in the PdCysZ hexamer (Figure 3d) at each of the vertices of the triangular structure. On the other hand, the PfCysZ dimer (Figure 3b) resembles the transverse pair of protomers lying at a tilt, just as was predicted by OPM (Lomize et al., 2012), along the side of the PdCysZ hexamer when viewed from inside the plane of the membrane (Figure 3e). In essence, the PdCysZ hexamer can be seen as a trimer of either IlCysZ or PfCysZ dimers (Figure 3f).

### Inverted transmembrane assembly of CysZ

To validate the inverted transmembrane assembly of CysZ observed in all our structures, we performed disulfide crosslinking assays on engineered cysteine mutants of CysZ designed to capture the antiparallel dimer, utilizing isolated membranes. Disulfide-trapping experiments of the transverse dimer, performed by crosslinking a pair of mutants (L161C-A164C) on helix H5 of PfCysZ, as well as the corresponding pair in IlCysZ (V157C-Q163C) confirm the dimer interface observed in the structures of PfCysZ and IlCysZ, and, as a consequence, the antiparallel assembly of the two proteins (Figure 3—figure supplement 2f,g,h).

To further validate the orientation of CysZ in the membrane, we performed a cysteine accessibility scan experiment, mapping residues expected to be located outside the lipid bilayer, by fluorescence labeling of the thiol groups of various single cysteine mutants with a membrane-impermeable dye. Membrane fractions isolated from recombinant cultures expressing IlCysZ cysteine mutants introduced at positions along the edge of helix H4 predicted to be solvent accessible based on our structure, were indeed labeled with a membrane-impermeable fluorescent thiol-specific maleimide dye (Figure 3—figure supplement 2c,d).

### Functional characterization of CysZ

To characterize the functional properties of CysZ, we performed (i) radiolabeled [35S]O42- flux measurements in intact E. coli cells and in proteoliposomes containing reconstituted CysZ and (ii) radiolabeled ([35S]O42-) binding assays of purified CysZ in detergent solution. We also used single-channel electrophysiological recordings in planar lipid bilayer reconstituted with CysZ.

First, we compared the time course of SO42- accumulation in an E. coli cysZ knockout strain (E. coli K-12 JW2406-1, CysZ-) (Baba et al., 2006) with that in the wild-type (WT, E. coli K12 BW25113, cysZ+) strain. CysZ- cells, after growth in minimal media and 12 hr of sulfate starvation, showed significantly diminished SO42- uptake when compared to the WT strain (Figure 4a), consistent with previous results (Parra et al., 1983). WT cells showed fast accumulation of 320 μM [35S]O42- that was linear over a period of 3 min, whereas uptake of [35S]O42- by the CysZ- strain started to plateau after about 1 min. This low level of sulfate accumulation by the CysZ- strain could be attributed to the other endogenous sulfate transport systems present in the bacteria (for example ABC transporter and SulP).

![Figure 4.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig4-v1.jpg)

**Figure 4.:** (a) Time course of [35S]O42- uptake (320 μM) by CysZ+ (strain BW25113) or CysZ- (strain JW2406-1)E. coli K-12 cells (n = 3). (b) Time course of [35S]O42- uptake (500 μM) by CysZ-containing proteoliposomes (▲, PdCysZ; ▼, PfCysZ; ◆, IlCysZ) or by control liposomes (š). (c) Kinetics of [35S]O42- uptake by CysZ. Initial rates of [35S]O42- uptake were measured for 5 s with [35S]O42- concentrations ranging from 0.5 to 50 mM. (d) Effect of the membrane potential (ΔΨ) on the initial rate of 1 mM [35S]O42- uptake measured for a period of 5 s. ΔΨ of different polarity was imposed with the K+-ionophore valinomycin in CysZ-containing proteoliposomes that were pre-loaded with different concentrations of KCl and assayed in external buffer of different KCl concentrations (equiosmolar cis/trans conditions) as indicated. The valinomycin-generated K+ flux produced a KCl in/out concentration difference-dependent ΔΨ that was calculated using the Nernst equation ($N_{e}=\frac{RT}{zF}ln\frac{[K^{+}]_{out}}{[K^{+}]_{in}}$). Data in panel (b–d) depict the means ± S.E.M. of 3 independent measurements performed in triplicate. (e, f) Equilibrium binding of [35S]O42- measured with the SPA. (e) Isotopic dilution of 100 μM [35S]O42- with non-labeled SO42- (sodium salt) or (f) competition of 100 μM [35S]O42- with non-labeled SO32- (sodium salt) reveals the EC50 or IC50 (concentration yielding half-maximum displacement or inhibition, respectively). See text for kinetic constants. Data in (e and f) are shown as mean ± S.E.M. of ≥6 measurements and subjected to global fitting in Prism seven and kinetic constants reflect the mean ± S.E.M. of the fit. The use of color for symbols and bars in panel (b–f) is consistent.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (a) Effect of SO32- on [35S]O42- accumulation in CysZ-containing proteoliposomes. Time course of [35S]O42- uptake (500 μM) by CysZ-containing proteoliposomes (▲, PdCysZ; ▼, PfCysZ; ◆, IlCysZ) or by control liposomes (š) in the presence of 500 μM Na2SO3. (b) Inhibition of [35S]O42- by SO32-. Initial rates of 500 μM [35S]O42- uptake were measured for 5 s in the presence of non-labeled SO32- at concentrations ranging from 1 nM – 100 mM. Data (means ± S.E.M. of ≥6 independent measurements) were subjected to nonlinear regression fitting (log inhibitor versus response – variable slope) in Prism 7, revealing an IC50 (SO32- concentration at which [35S]O42- uptake is inhibited by 50%) of 2.73 ± 0.42 mM for PdCysZ, 4.99 ± 0.46 mM for PfCysZ, and 2.31 ± 0.76 mM for IlCysZ. (c) Effect of the sodium motive force (ΔμNa+) or proton motive force (ΔμH+) on CysZ-mediated SO42- uptake. [35S]O42- (1 mM final concentration) uptake was measured for a period of 5 s in CysZ-containing proteoliposomes prepared in 200 mM Tris/Mes, pH 7.5 (inside buffer composition) in assay buffer composed of either (i) 100 mM Tris/Mes, pH 7.5/100 mM NaCl (generation of ΔμNa+; black bars) or (ii) 200 mM Tris/Mes, pH 5.5 (generation of ΔμH+; green bars) in the presence (solid bars) or absence (open bars) of 25 μg gramicidin/mL. Addition of the ionophore gramicidin did not markedly decrease the [35S]O42- uptake activity by CysZ as would be expected for Na+ or H+-coupled SO42- transporters. (d) SO32- binding by CysZ. Saturation binding of SO32- was measured with the MST assay, yielding EC50s of 3.73 ± 0.79 mM for PdCysZ and 8.68 ± 1.88 mM for IlCysZ. (e) Electrophysiology of IlCysZ reconstituted in planar lipid bilayers. Sample traces of IlCysZ under 150 mM symmetrical Na2SO4 solutions at the indicated membrane potentials and pH = 5.4.

To assess direct CysZ-mediated SO42- flux without the potential interference of other native sulfate-transporting systems observed in the bacterial expression host, we henceforth conducted [35S]O42- uptake experiments with purified CysZ reconstituted in proteoliposomes. Consistent with the cell uptake studies, the three orthologs (PdCysZ, PfCysZ and IlCysZ) all mediated the accumulation of 500 μM SO42- into proteoliposomes in a manner virtually indistinguishable from one another. Uptake was time-dependent and occurred rapidly with a peak at about 15 s (Figure 4b).

Testing the previously described inhibitory effect of SO32- (Zhang et al., 2014), we measured uptake of 500 μM [35S]O42- in the presence of 500 μM Na2SO3 (Figure 4—figure supplement 1a). All three species of CysZ displayed SO32- sensitivity and their activity was virtually indistinguishable from the SO42- accumulation observed in control liposomes lacking CysZ (Figure 4—figure supplement 1a). Measuring uptake of 1 mM [35S]O42- in the presence of increasing concentrations of SO32- showed that ~3 mM SO32- resulted in half-maximum inhibition (IC50) of SO42- uptake under those experimental conditions (Figure 4—figure supplement 1b). The further kinetic characterization of the three CysZ isoforms in proteoliposomes (Figure 4c) revealed that the affinity for SO42- transport (Km) by CysZ is about 8 mM (PdCysZ: 8.69 ± 0.35 mM; PfCysZ: 7.86 ± 0.72 mM; IlCysZ: 8.03 ± 0.68 mM), while the maximum velocity of transport (Vmax) is about 90 μmol SO42- x mg CysZ−1 x min−1 (PdCysZ: 100.4 ± 1.4; PfCysZ: 89.7 ± 2.8; IlCysZ: 87.9 ± 2.5; all values in μmol SO42- x mg CysZ−1 x min−1). Taking into account the actual amount of CysZ incorporated into the proteoliposome preparations (determined with the Amidoblack protein assay, [Schaffner and Weissmann, 1973]) revealed catalytic turnover numbers (kcat) of 46.4 ± 0.7 s−1; 42.5 ± 1.3 s−1, and 41.9 ± 1.2 s−1 for PdCysZ, PfCysZ, and IlCysZ, respectively. Whereas this turnover number is well within the range observed for other secondary transporters (Jung et al., 1998; Malinauskaite et al., 2014; Eskandari et al., 1997; Quick et al., 2001), it may also reflect the energetically uncoupled flux of SO42- along its concentration gradient, characteristic for a low-turnover channel phenotype (or passive transport/uniport, or facilitated diffusion) (Ashcroft et al., 2009). In fact, calculations of the SO42- accumulation in the PdCysZ-containing proteoliposomes at the peak of the uptake (at 15 s) shown in Figure 4b reveal that the internal concentration of SO42- is only ~5 fold higher than that of the externally added SO42-, whereas it is ~3 fold elevated at the plateau (120 s), revealing non-concentrative SO42- flux by CysZ that is representative for a channel-like mode of action (see Materials and methods for details). Note that applying the same calculation to the MhsT-mediated Na+-coupled L-tryptophan transport in the identical preparation of MhsT-containing proteoliposomes (Malinauskaite et al., 2014) yields an ~150 fold internal concentration excess of the amino acid. Also, it seems worth noting that while the kcat takes into account the total amount of CysZ in the proteoliposomes, experimental limitations preclude the accurate determination of the actual number of functional CysZ molecules in the proteoliposomes, thus resulting in a potentially underestimated value for the true kcat.

To distinguish between the active and passive SO42- flux phenotypes, we performed uptake studies with CysZ in the reconstituted proteoliposome system in the presence of ionophores that dissipate transmembrane ion gradients that could serve as driving force for SO42- uptake, i.e., co-transport or symport. Performing uptake of 1 mM SO42- using CysZ-containing proteoliposomes preloaded with 200 mM Tris/Mes, pH 7.5 in assay medium composed of 100 mM Tris/Mes, pH 7.5/100 mM NaCl (to generate a sodium motive force, Δ$\mu_{Na^{+}}$) or in 200 mM Tris/Mes, pH 5.5 (to generate a proton motive force, Δ$\mu_{H^{+}}$) revealed activities that were virtually indistinguishable from experiments with the same internal and external buffer composition (200 mM Tris/Mes, pH 7.5) or by adding the ionophore gramicidin (causing the dissipation of ΔμNa+ and ΔμH+; Figure 4 and Figure 4—figure supplement 1c). We then tested the effect of the membrane potential on CysZ activity. For these studies, CysZ-containing proteoliposomes were preloaded with and assayed in a Tris/Mes-based buffer system (at pH 7.5) that allowed for a different KCl inside/outside (Kin/Kout) distribution (Figure 4d). Potassium flux-generated membrane potentials of different polarity were imposed by adding the potassium ionophore valinomycin, revealing that hyperpolarization of the proteoliposomes (inside-negative membrane potentials) did not markedly increase CysZ-mediated SO42- flux into the proteoliposomes. However, depolarization (inside positive) caused about a 40 % increase in the uptake activity of all three CysZ isoforms at a Kin/Kout distribution of 1:100 (producing a theoretical Nernst membrane potential of +118 mV [Figure 4d]).

To further characterize the interaction of CysZ with both SO42- and SO32-, we performed binding experiments with detergent-solubilized and purified CysZ using the scintillation proximity assay (SPA) (Quick and Javitch, 2007) as well as micro-scale thermophoresis (MST) (Seidel et al., 2013). To determine the concentration of half-maximal sulfate binding (EC50), we isotopically diluted [35S]O42- with non-labeled SO42-, obtaining an EC50 of 3.51 ± 1.9 mM for PdCysZ, 2.24 ± 0.85 mM for PfCysZ, and 2.29 ± 1.04 mM for IlCysZ (Figure 4e). Competing binding of [35S]O42- with increasing concentrations of SO32- revealed that CysZ binds SO32- with about 4-fold greater apparent affinity as reflected by a half-maximum inhibition constant (IC50) of 0.74 ± 0.23 mM for PdCysZ, 0.60 ± 0.21 mM for PfCysZ, and 0.56 ± 0.20 mM for IlCysZ (Figure 4f). Whereas the SPA-based binding competition of [35S]O42- binding by SO32- represents an indirect assay, MST-based binding of SO32- revealed apparent affinities for SO32- binding by PdCysZ and IlCysZ of 3.73 ± 0.76 mM and 8.68 ± 1.88 mM, respectively (Figure 4—figure supplement 1d).

Finally, we also employed single-channel electrophysiological current recordings with IlCysZ reconstituted in a planar lipid bilayer. Traces often showed multiple levels of a basic conductance, consistent with the incorporation of more than one reconstituted channel (Figure 4—figure supplement 1e). Recordings were made with varied membrane potentials applied in symmetrical Na2SO4 solutions on both sides of the bilayer, from which a single-channel conductance of ~92 pS was deduced. Measurements made with PdCysZ gave a similar single-channel conductance level. Thus, consistent with our [35S]O42--based flux assays, these electrophysiological measurements showed that reconstituted CysZ exhibits channel-like properties.

### Sulfate binding site

A bound SO42- ion was observed in the structure of IlCysZ. This binding site was confirmed by purifying and crystallizing CysZ in the presence of the heavier SO42--analog selenate (SeO42-). In the SO42- bound structure, each protomer in the dimer showed electron density consistent with a bound sulfate, but only one of the two refined to full occupancy, hence only one is shown in the refined model of IlCysZ (Figure 5a and Figure 5—figure supplement 1). The location of the bound SO42- is on the outer periphery of the CysZ protomer, close to the putative membrane interface where it is coordinated by two arginine residues (R27 and R28 in IlCysZ) and the backbone amides of residues G25 and L26. This SO42--binding site is in the loop between helices H1 and H2, with the motif GLR(R) being well conserved among the CysZ family. Consistent with this observation, crystals of IlCysZ in which R27 and R28 were replaced with alanines did not show interaction with SO42- in that site based on i) the lack of any density in the refined mutant structure at 2.3 Å and ii) functional studies (see below). We could not confirm the presence of SO42- in either of the other structures of PfCysZ and PdCysZ, owing, at least in part, to their lower resolution limit (~3.5 Å). Soaking and co-crystallization attempts on both PfCysZ and PdCysZ with SeO42- resulted in cracking and destabilization of crystals, and loss of measurable diffraction. In this vein, IlCysZ R27A/R28A, and the corresponding PfCysZ R25A and PdCysZ R23A mutants all have severely impaired sulfate uptake capability, as demonstrated in cells and proteoliposomes (Figures 5b and Figure 4—figure supplement 1a), and exhibit dramatically reduced sulfate binding activity (<20% compared of that measured for CysZ-WT, data not shown), consistent with a conserved role for these targeted arginine residues in all CysZ variants.

![Figure 5.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig5-v1.jpg)

**Figure 5.:** (a) Side-view of a ribbon diagram of the PdCysZ hexamer, with one chain rainbow-colored from N- (blue) to C-termini (red). Insets show the sulfate-binding site located at the start of H2a in PdCysZ (left), with conserved residues G21, L22, R23 and L24 labeled, and the corresponding site in IlCysZ (right), with residues G25, L26, R27, and R28 labeled and showing the SO4−2 ion as bound in the crystal structure. (b) Sulfate uptake by sulfate-binding site mutants of PdCysZ. E. coli K-12 CysZ- cells transformed with the listed PdCysZ R23 mutants were used to measure 320 μM [35S]O4−2 uptake (n = 3). Sulfate uptake was abolished for R23A, and rescued to 50% and 40% of the wild type levels for the R23K and R23Q mutants respectively. (c) A top-view of the PdCysZ hexamer, colored as in a. The inset magnifies the central core of CysZ to show the associated network of hydrogen bonds (R129-N184, E106-H185), van der Waals interactions (E103-N184, E106-N184, Q176-E134) and salt bridges (R129-D183, R133-D183, R110-E106) between pairs of highly conserved residues. Interatomic contacts are shown as purple dotted lines with distances (in Å) marked in blue. (d) Sulfate uptake by central-core mutants of PdCysZ. E. coli K-12 CysZ- cells transformed with the listed PdCysZ mutants were used to measure 320 μM [35S]O4−2 uptake (n = 3). N98A and R129E and R129Q showed severely impaired sulfate uptake, whereas more conservative substitutions such as N98D, Q176E and Q176N had less of a negative effect on function. Y177A and Y177F do not show any impaired function.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (a) Apo structure of IlCysZ showing a bound water (H2O) molecule, with no anomalous signal above noise level (collected at Fe edge). (b) IlCysZ in complex with selenate (SeO42-), anomalous Fourier map is shown at 5.0 sigma (collected at Se edge). (c) IlCysZ in complex with sulfate (SO42-), anomalous Fourier map is shown at 2.0 sigma (collected at Fe edge). 2Fo-Fc electron densities are in gray and anomalous Fouriers are in magenta.

### Conserved core in the hydrophilic head

Each apex of the triangular faces of the PdCysZ hexamer comprises an extra-membranous hydrophilic head of a CysZ protomer (Figures 1a and 5c). The central core of this hydrophilic head consists of the ends of helices H3 and H5 and the start of helix H4, with their residues forming an intricate network of hydrogen bonds and salt bridges that hold this helical bundle together (Figure 5c). Two highly conserved motifs in this region, ExVE and QYxDYPxDNHK (Figure 2c), likely play critical roles in this network of interactions. The two aspartates E103 and E106 (PdCysZ) in the first motif interact with R129, N184 and R110, H185, respectively (Figure 5c). The conserved R129 and R133 on helix H4b in turn also interact with D183 and N184 in the DNHK sequence stretch of helix H5b in the second motif. In the second motif, a conserved tyrosine (Y177) lies below the membrane interface towards the core of the molecule, along helix H5.

Mutational studies on a subset of these conserved hydrophilic-head residues highlight their functional relevance (Figure 5d). R129 mutants (R129E or Q) exhibited a severe loss of SO42- binding and uptake, and mutations made to Q176 and Y177 also showed loss in function, albeit to a lesser extent. Charge reversal mutations made to E103 and E106 (to K or R) or the equivalent IlCysZ E107, E110 resulted in very poor expression and stability levels, suggesting that the disruption of the interaction network in this region may destroy the structural integrity of the protein.

### Putative pore and sulfate translocation pathway of CysZ

It was already evident from the initial IlCysZ structure that the hydrophilic head presented an incipient opening into the membrane (Figure 5c-inset, Figure 6a), but it was quite unclear how this opening might relate to transmembrane sulfate translocation. The ‘transverse’ dimer structure of PfCysZ clarified the possibility for ion permeation by showing that openings in its two protomers aligned across the putative membrane; however, the prospective transduction pathway would then be open on one side to the bilayer (Figure 6—figure supplement 1). The PdCysZ structure showed that the open sides of transverse dimers line a central cavity in the PdCysZ hexamers. Thus, plausible transduction pathways became more evident.

![Figure 6.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig6-v1.jpg)

**Figure 6.:** (a) Ribbon diagram colored by conservation with residues in maroon being most conserved to cyan being least conserved (calculated by ConSurf) to highlight the entrance to the putative pore; an asterisk (*) marks the location of the sulfate-binding site (GLR motif) at top of helix H2a. (b) Same view and coloring scheme as in a, but now shown in surface representation. (c) Electrostatic representation of hexameric PdCysZ as viewed from the top, with negative surface potential represented in red, and positive potential in blue as calculated by APBS, with location of the putative pore marked by a dashed circle. (d) Close-up view in electrostatic representation of the putative pore within a PdCysZ protomer, surface and orientation as in b.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (a) The location of the putative sulfate translocation pore in the hydrophilic head of the PfCysZ transverse dimer is marked with an arrow. The cartoon is colored by conservation (maroon- highly conserved, cyan- more variable). (b) A top view (90° rotated) reveals the putative pore going all the way through the PfCysZ dimer. (c) A top view of the PfCysZ dimer in surface depiction, colored by surface electrostatics, shows the negatively charged nature of the entrance to the pore.

The view into a protomer surface along the direct pathway between transverse dimer apices (e.g. green to orange in Figure 3e) displays the pattern of exceptionally high conservation associated with the entrance to a putative pore for sulfate translocation (Figure 6a,b). This putative entrance or ‘pore’ lies in the midst of a tight network of interacting residues, which is seen detailed in the inset of Figure 5c in the very same view as for Figure 6a. These interactions close the incipient pore from ion conduction in this conformation. Intriguingly, this putative pore-entrance lies approximately 17–20 Å (linear distance) away from the observed sulfate binding site. The electrostatic potential surface of PdCysZ (Figure 6c) shows striking and puzzling electronegativity at the conserved pore entrance (Figure 6d compared with Figure 6b). Because of the conservations, similar electrostatics pertain to the two other homologs. Moreover, we observe the same helix dispositions, pore shape and charge interactions in all three structures, evident when the protomers are superimposed (Figure 3c, top view).

Pathway prediction algorithms (namely, PoreWalker [Pellegrini-Calace et al., 2009]) performed on the CysZ protomer revealed a putative ion translocation pathway that begins at the entrance to the putative pore and ends in the large central cavity of the CysZ hexamer that lies within the membrane (Figure 7a,b). In the structure of PdCysZ, the entrance of the putative pore appears to be closed by the network of charge-interactions by conserved residues, R110, E106, N184, H185 and W235 (Figures 6a and 7c–1). These residues interact to tightly restrict access to the putative translocation pathway and constrict the entry of ions, likely selected for size and charge (Figure 7—figure supplement 1a). After the narrow entrance, the putative pathway broadens, surrounded by a ring of conserved asparagine and glutamine residues, N33, N91, N98, Q176, and N220 (Figure 7c-2). Mutations to N98 (N98A, N98D) led to impaired sulfate uptake (Figure 5d). Following this polar environment, the putative pathway widens even further leading into a large, primarily hydrophobic, internal cavity encapsulated by the TM helices of the PdCysZ hexamer, located in the plane of the lipid bilayer (Figure 7b and Figure 7—figure supplement 1c,d). The hydrophobic cavity is enclosed on both the top and bottom by pairs of helices H4-H5, three on each side from the six protomers, pointing in towards the three-fold axis, with each side of the cavity, at its mid-section, measuring ~50 Å, when viewed from above or outside the membrane (Figure 7—figure supplement 1c,d). Given the symmetric, dual topology nature of the CysZ assembly, the ions could then exit the cavity via the same pathway as they entered, but traveling through CysZ protomers located on the opposite side of the membrane.

![Figure 7.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig7-v1.jpg)

**Figure 7.:** (a) A PdCysZ protomer looking into the incipient pore entrance. The polypeptide ribbon is oriented as in Figure 6a and colored by level of sequence conservation (calculated by ConSurf, with maroon being most conserved and cyan least). The putative pore and ion conduction pathway is shown as a yellow tube of 1 Å diameter, calculated by PoreWalker. (b) Surface representation of the PdCysZ hexamer, as side views, both semi-transparent (left) and with surface clipped (right, cut surfaces colored in grey) to allow for the internal visualization of the pathway leading to the central cavity. (c) Side view of a PdCysZ protomer left, viewed as in b and rotated 90° from a. Insets show magnified views of cross-sections along the pathway: At level 1, the entrance to the pore consists of a narrow constriction created by a network of highly conserved polar and charged residues (E106, R110, E134, N184, H185) tightly interacting with one another. At level 2, the pathway broadens and becomes less charged, but yet polar in nature as lined by conserved asparagine, tyrosine and threonine residues (N33, T87, N91, N98, Q176, Y177). From level 3, the pathway widens further and ultimately leads into the large central hydrophobic cavity.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/27829/elife-27829-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** (a) PdCysZ (b) PfCysZ, showing a very narrow constriction of under 2 Å in diameter near the entrance of the pore, which then widens as the ions move past the core of the protomer to the inner central cavity of the hexameric channel (as calculated by PoreWalker, measured at 3 Å steps along the x-axis) (c) Central hydrophobic cavity of PdCysZ hexamer, cross-section of central cavity of the hexameric PdCysZ (top view) and (d) side view, shows a triangular-shaped cavity with each side measuring 49.6 Å in length. The cavity is primarily hydrophobic, as depicted and colored with the Kyte-Doolitle hydrophobicity scale from most polar colored in cyan to most hydrophobic colored in orange.

## Discussion

There are four known families of dedicated SO42- transport systems in prokaryotes6, of which CysZs are the least studied (Zhang et al., 2014). The sequence of CysZ, coding for an integral membrane protein with four predicted TM segments, shows no resemblance to any other known protein. This, and the quest to set the basis for a mechanistic understanding of function, prompted us to investigate the structure of CysZ.

We present here three structures of CysZ from different species, all determined by x-ray crystallography. These structures are all similar, showing a novel fold comprising two extended TM helices and two hemi-penetrating helical hairpins, giving rise to a tripod-like shape within the membrane, and a hydrophilic head (Figures 2a,b and 3c). Two of the structures (IlCysZ and PfCysZ) show dimers in the crystals, albeit with different interfaces (Figure 3a,b), and the third structure (PdCysZ) displays a hexameric assembly in multiple crystal forms (Figure 1a).

All three structures have a dimeric component, each of which is present in the hexameric arrangement present in all the crystal forms of PdCysZ (Figure 3a,b), showing how they are all related. Furthermore, IlCysZ can be crosslinked in membranes to the alternative PfCysZ dimer by engineering of disulfide cysteine mutants (Figure 3—figure supplement 2), which suggests that IlCysZ can adopt both of the dimer assemblies observed in the PdCysZ hexamer. Thus, we hypothesize that CysZ is a hexamer in nature, as observed in PdCysZ, consistent with the fact that all CysZs studied here exhibit essentially the same functional properties. In the case of IlCysZ and PfCysZ, this assembly may have come apart into the subsequently crystallized dimeric components during the process of detergent extraction from the membrane and purification. This could be explained by the unusually labile, and conformationally-flexible, nature of the H4b-H5a helical hairpin of CysZ, with only one pair of stabilizing TM helices per protomer (H2-H3). We presume that the hexamer is maintained with the support and scaffolding of the lipid bilayer.

CysZ shows an inverted transmembrane arrangement, which we confirmed with cross-linking experiments on membranes (Figure 3—figure supplement 2). Antiparallel insertion is fairly uncommon in membrane proteins; however, reported cases include the well-documented EmrE, a multi-drug resistant export protein that inserts into the membrane as an anti-parallel dimer, and the more recently discovered and studied family of double-barreled ‘Fluc’ fluoride channels (Amadi et al., 2010; Korkhov and Tate, 2009; Rapp et al., 2006; Stockbridge et al., 2015; Stockbridge et al., 2013).

Functional characterizations of the three CysZs for which we have obtained structural information show that all three mediate SO42- flux and that this flux is inhibited by SO32-, thus supporting previously reported data on E. coli CysZ (Zhang et al., 2014). However, in contrast to what was observed for E. coli CysZ (Zhang et al., 2014), our data indicate that SO42- flux by PdCysZ, PfCysZ and IlCysZ is not thermodynamically coupled to the proton gradient (i.e., H+/SO42- symport) or the Na+ gradient (i.e., Na+/SO42- symport) but rather reflect the non-concentrative flux of SO42- characteristic of a passive, channel-like translocation mechanism. However, SO42- flux in CysZ-containing proteoliposomes differed from the ohmic I-V relationship indicative of a single ion-selective channel in that it was not affected by hyperpolarization (inside negative), but depolarization of the proteoliposomes (inside positive) led to an increased inward flux of SO42-. Thus, we contemplate that CysZ SO42- flux activity may involve co-permeation of other ions with Na+ being the most likely for our experimental conditions. Our electrophysiological measurements of purified CysZ incorporated into a lipid bilayer did not aim to assess permeability ratios of SO42- and other ions, i.e., for Na+, symmetric Na2SO4 solutions were used in the experiments.

Building on our functional and structural discoveries, our results suggest a fascinating hypothesis for mechanisms of SO42- transfer and regulation. There is a conserved central core (Figure 6a), which is likely to have a structural role. Close to this lies a sulfate-binding site, with functional implications (Figure 5a), and the entrance to a putative pore (Figure 5c). The entrance of this putative pore is delineated by a hydrophilic network of conserved residues that form a tight constriction in our observed conformation. Following this hypothetical route, sulfate ions that might enter through the three separate pores, one per CysZ dimer pair, would converge into a central hydrophobic cavity (Figure 7b and Figure 7—figure supplement 1c,d). Once sulfate ions enter this central cavity, due to the unfavorable environment, these are likely to exit it rather rapidly through one of the three available exit pores on the cytoplasmic side of the hexamer. Hydrophobic cavities and pores are seen commonly in ion channels, with examples ranging from the well documented hydrophobic inner pores of the various potassium channels (Doyle et al., 1998) to the SLAC1 (Chen et al., 2010) and bestrophin anion channels (Yang et al., 2014), and the MscS and MscL mechanosensitive channels (Anishkin et al., 2010; Bass et al., 2002; Birkner et al., 2012; Chen et al., 2010; Doyle et al., 1998), facilitating the rapid passage of ions due to the unfavorable environment, as well as potentially providing a means of ‘hydrophobic gating’ (Aryal et al., 2015).

The surface electrostatics of CysZ (Figures 1b and 6c,d) draw attention to the negative potential of the conserved core of each protomer, which is then surrounded by a more neutral annulus. While this feature seems contradictory to admission of SO42- ions at the extracellular side, it could be advantageous for expulsion into the cytoplasm on the opposite side. In any case, the structures that we have determined are evidently in a closed state, implying that a conformational change would have to occur to allow passage of SO42-, likely modifying the surface electrostatics of the protein. It is tempting to speculate that the regulation of the opening of the pore could be modulated by the binding of sulfate ions to the identified sulfate-binding site, as it is near the entrance of the putative pore. L22 lies in proximity of the entrance of the putative pore, and its backbone amide (along with G21) coordinates the sulfate ion in the GLR motif of the sulfate-binding site. Thus, the binding of sulfate to the GLR motif could trigger a conformational change needed to displace L22, allowing for a wider opening for the sulfate ions to enter the pore. Sulfite could hypothetically exert its inhibitory effect on CysZ function by binding to this site.

There is an overall electropositive region in the center of the hexameric molecule, when viewed from the top (Figures 1b and 6c,d). This central region is lined by conserved residues along helices H4b-H5a, namely, R129, R133 and K137. The hydrophobic tips of helices H4b-H5a of the three protomers on each side of the membrane then converge in the center of the hexamer. A pore through the three-fold axis of the hexamer could provide an alternative passageway for SO42- ions through this assembly.

We observe, in agreement with previous data, that SO32- inhibits CysZ-mediated SO42- flux (Figure 4b,d and Figure 4—figure supplement 1a,f) (Zhang et al., 2014). The antiparallel nature of CysZ could provide a means for internal as well as external regulation. However, experiments in solutions – such as crystallizations – where all molecules are exposed to the same chemical environment, makes capturing such a state in an open or SO32- blocked conformation challenging. Despite this limitation, our CysZ structures and associated functional experiments have allowed us to make substantial progress in the understanding SO42- uptake by these membrane permeases. This work sets the framework for future experiments aimed at unraveling the molecular details of how SO42- is translocated across the membrane by CysZ and how this process is regulated.

## Materials and methods

### Ortholog selection and cloning

A total of 63 cysZ candidate genes were selected by a bioinformatics approach implemented by the New York Consortium of Membrane Protein Structure (NYCOMPS), as previously described (Punta et al., 2009). The majority of the genes (including IlCysZ, uniprot ID: Q5QUJ8) were PCR-amplified from fully sequenced prokaryotic genomic DNA (obtained from ATCC) (Love et al., 2010). CysZ genes from certain species, such as PfCysZ (uniprot ID: A0A0X8F058) and PdCysZ (uniprot ID: M4XKU7) were chemically synthesized by GenScript (Genscript, Piscataway, New Jersey), with codon-optimization for protein expression. All genes were cloned by ligation-independent cloning (LIC) (Aslanidis and de Jong, 1990) into an IPTG (isopropyl β-D-1-thiogalactopyranoside) inducible, kanamycin-resistant pET derived plasmid (Novagen, Madison, Wisconsin), with an N-terminal deca-histidine tag (His10) and a TEV (tobacco etch virus) protease site to allow for tag cleavage upon purification.

### Protein expression and purification

Expression plasmids bearing the cysZ genes were transformed into BL21(DE3)pLysS cells using standard protocols, and grown at 37°C in 2XYT media supplemented with 50 μg/ml kanamycin and 50 μg/ml chloramphenicol in an orbital shaker at 250 rpm. Protein expression was induced for ~16 hr at 22°C with 0.2 mM IPTG once an absorbance (A600 nm) of 0.8–1.0 was reached. Selenomethione (Se-Met)-incorporated proteins were expressed in BL21(DE3)pLysS cells grown using an M9 minimal media kit (Shanghai Medicilon, China) supplemented with the necessary minerals, vitamins and non-inhibitory amino acids. Se-Met was added prior to IPTG induction at an A600 nm of 1.2. The Se-Met-incorporated protein was purified using the same procedures as the native protein. Once harvested, the cells were resuspended at 0.2 g/ml in lysis buffer containing 20 mM Na-Hepes pH 7.5, 200 mM NaCl, 20 mM MgSO4, DNase I and RNase A, 0.5 mM PMSF (phenylmethylsulfonyl fluoride), EDTA-free Complete protease inhibitor cocktail (Roche, Switzerland) and 1 mM TCEP-HCl (Tris (2-carboxyethyl) phosphine hydrochloride) as a reducing agent. Initial small-scale expression and detergent screening was performed on 80 mg of pelleted cells (wet weight), and 7–10 g of cells for large-scale protein purification. Cells were lysed using an Avestin® EmusiFlex-C3 homogenizer, followed by protein solubilization with 1% (w/v) decyl maltopyranoside (DM) (Anatrace, Maumee, Ohio) for 1 hr at 4°C, after-which insoluble material was removed by ultra-centrifugation at 100,000 x g. The solubilized protein was applied to Ni-NTA Sepharose (Qiagen, Germantown, Maryland) in batch, washed with lysis buffer containing 0.2% DM and 40 mM imidazole and eluted in buffer containing 250 mM imidazole. Upon elution, CysZ was dialyzed overnight with His-tagged TEV protease at 4°C, against a buffer containing 20 mM Na-Hepes pH 7.0, 200 mM NaCl, 0.2% DM, 1 mM TCEP-HCl and 20 mM Na2SO4, allowing for the cleavage of the His10 tag and removal of the imidazole. Tagless CysZ was then re-passaged over Ni-NTA sepharose to re-bind of any uncleaved CysZ, TEV protease and the cleaved His10 tag. The protein was then subjected to size-exclusion chromatography (Superdex 200 10/30 HR; GE Healthcare, Chicago, Illinois) in 20 mM Na-Hepes pH 7.0, 200 mM NaCl, 1 mM TCEP-HCl, 20 mM Na2SO4 and appropriate detergent for crystallization, for IlCysZ: 0.06% Lauryl dimethylamine oxide (LDAO) and for PfCysZ and PdCysZ: 1% β-octyl glucopyranoside (β-OG). The choice of detergent was made based on protein yield, stability and mono-disperse gel-filtration peaks obtained in the initial small-scale detergent screening. A yield of ~1.5 mg of purified CysZ was typically obtained from a cell pellet of 7–8 grams (1 liter of culture).

### Protein crystallization

#### IlCysZ

Crystals of IlCysZ in LDAO were obtained by vapor diffusion at a protein concentration of 6–8 mg/ml at 4°C, in a 1:1 v/v ratio against a precipitant of 28–32% PEG400, 0.1M Tris-HCl pH 8.0, with salt additive of 0.1 M NaCl or 0.1 M MgCl2. The crystals appeared overnight, continued to grow in size over the course of 2–4 days after set-up. After optimization, the crystals grew to a maximum size of ~200 μm x 100 μm x 50 μm with a rhomboid or cuboid shape. The crystals were harvested directly without the addition of a cryo-protectant and flash-frozen into liquid nitrogen, for data collection on the X4A/X4C beamlines at National Synchrotron Light Source (NSLS), Brookhaven National Labs (Upton, NY). SeMet derivatized and selenate co-crystals were obtained from the same conditions as the native crystals.

#### PfCysZ

Crystals of PfCysZ in β-OG at 5 mg/ml were initially obtained at 4°C by vapor diffusion, in a 1:1 protein to precipitant ratio, after 1–2 days against 28% PEG400, 0.1 M MES pH 6.0. They were cuboid in shape and grew in clusters of multiple crystals originating from a common locus. The crystals were optimized to a maximal size of ~150–200 μm x 50 μm x 50 μm, with the best diffracting crystals grown under silicone oil (visc. 500) in microbatch Terazaki plates. Crystals were directly flash-frozen into liquid nitrogen without the use of a cryo-protectant and were exposed to X-rays at the NE-CAT (24-IDC and IDE) beamlines at APS, Argonne National Lab (Argonne, IL) for data collection. SeMet crystals were obtained from the same conditions as the native protein.

#### PdCysZ

Crystals of PdCysZ in β-OG at 5–8 mg/ml were initially obtained at 4°C by vapor diffusion, in a 1:1 protein to precipitant ratio, after 2–3 days against 22–30% PEG550MME, 0.1 M Na-Hepes pH 7.0. The rod-like crystals were hexagonal on one face, and grew in clusters originating from a common locus as well as on the edge of the drop. The multiple crystal forms observed were all obtained in the same crystallization conditions. The crystals were optimized to a maximal size of ~200–250 μm x 25 μm x 50 μm. With the addition of 20% glycerol (w/v) as a cryo-protectant, the crystals were flash-frozen into liquid nitrogen and were exposed to X-rays at the NE-CAT (24-IDC and 24-IDE) beamlines at APS, Argonne National Lab (Argonne, IL) for data collection.

### Data collection and structure determination

#### IlCysZ

The structure of CysZ was determined by the single-wavelength anomalous diffraction (SAD) method from anomalous diffraction of a selenate (SeO42-) derivative crystal. The anomalous signals were measured at the Se K-edge peak wavelength, which was determined experimentally from fluorescence scanning of the crystal prior to data collection. All diffraction data were recorded at 100K using an ADSC Q4R CCD detector at the NSLS X4 beamline. Diffraction data were indexed, integrated, scaled, and merged by HKL2000 (Otwinowski and Minor, 1997). Selenate substructure determination was performed with the SHELXD program through HKL2MAP (Pape and Schneider, 2004). A resolution cut-off at 2.6 Å was used for finding Se sites by SHELXD. A strong peak found by SHELXD was used to calculate initial SAD phases, which were improved by density modification by SHELXE (Sheldrick, 2010). With a solvent content of 65% corresponding to two molecules in the asymmetric unit, 50 cycles of density modification resulted in an electron density map of sufficient quality for model building. The initial polypeptide chain was built by Arp/Warp (Langer et al., 2008), at 2.1 Å by using experimental phases. Further cycles of model building were performed manually using COOT (Emsley et al., 2010) and all rounds of refinements were performed with PHENIX (Adams et al., 2010). The native structure of CysZ with bound sulfate was determined both by multi-crystal native SAD (Liu et al., 2012) (final resolution of 2.3 Å) and by molecular replacement with the selenate bound model (final resolution of 2.1 Å). In addition, phase information obtained from Se-Met derivatized protein with 9 Se sites per CysZ molecule, verified our model obtained from the selenate data.

#### PfCysZ

Multi-crystal SeMet-SAD data sets were collected at APS beamline 24-IDC with a Pilatus 6M pixel array detector under a cryogenic temperature of 100 K. To enhance anomalous signals from Se atoms for phasing (Liu et al., 2011), the X-ray wavelength was tuned to the Se-K edge (λ = 0.9789 Å). The orientation of crystals was random without special consideration of crystal alignment, and beam size was adjusted to match the crystal size. A total of 22 data sets were collected, each from a single crystal. An oscillation angle of 1° was used for data collection with a total of 360 frames for each data set. The beam size was adjusted to match the crystal size. The 22 single-crystal data sets were processed individually by using XDS (Kabsch, 2010) and CCP4 packages (Winn et al., 2011). For phasing purposes, the low-resolution anomalous signals were enhanced by increased multiplicity. By rejection of 7 outlier crystals (Liu et al., 2012), anomalous diffraction data from 15 statistically-compatible crystals were scaled and merged for phasing. For outlier rejection, a unit-cell variation of 1.0σ was used. CCP4 program POINTLESS and SCALA (Evans, 2006) were used for data combining; and Bijvoet pairs were kept separately throughout the data flow. For refinement purposes, keeping the high angle data was important, and done by limiting radiation damage as well as by increasing multiplicity. Although most PfCysZ crystals diffracted to only about 3.5 Å spacings or poorer, we intentionally set the detector distance to include higher spacings. Higher resolution data were retained through a data merging procedure that is described as follows: (1) The 22 individually processed data sets were analyzed by diffraction dissimilarity analysis by using only high angle data between 3.5 and 3.0 Å, resulting in three subsets. (2) The data statistics of members in each subset were checked manually and the subset that contained the highest angle data set, e.g. data set 6, was selected for further analyses and data combination. (3) Each data set within the selected subset was compared with data set six by high-angle intensity correlation. Six of the highest resolution data sets were statistically comparable and therefore were selected for merging. For phasing, substructure solutions were found by SHELXD (Sheldrick, 2010) and were further refined and completed by PHASER (McCoy et al., 2007) and then used to compute initial SAD phases at the data limit by SAD phasing with PHENIX (Adams et al., 2010). Phases were density modified with solvent flattening and histogram matching as implemented in CCP4 program DM (Cowtan and Zhang, 1999) to improve phases and also to break phase ambiguity. The estimated solvent contents of 71% were used for density modification. The model was initially built into the experimental electron density map by COOT (Emsley et al., 2010), followed by iterative refinement by PHENIX and model building in COOT. The refined model does not contain solvent molecules at this resolution.

#### PdCysZ

Native crystal data were collected at the APS beamline 24-IDC with a Pilatus 6M pixel array detector at a cryogenic temperature of 100 K at an X-ray wavelength of λ = 1.023 Å. The sample-to-detector distance was set to 500 mm. An oscillation angle of 0.5° was used for data collection. The beam size was adjusted to match the crystal size. Molecular replacement was attempted using a variety of search models (PfCysZ and IlCysZ monomer/dimer models, with various degrees of truncation). Success was achieved by searching for six copies of a search model consisting of the PfCysZ monomer, with residues 36–53 deleted and the sequence adjusted using CHAINSAW (Stein, 2008) (pruning non-conserved residues to the gamma carbon). Density modification of the initial map was performed in PARROT, incorporating solvent flattening, histogram matching and NCS-averaging. An initial round of model building was performed in COOT (Emsley et al., 2010) into this map, followed by further phase improvement and bias-removal using phenix.prime_and_switch (Adams et al., 2010). The improved map was used for a second round of model building, followed by iterative cycles of reciprocal space refinement using phenix.refine, and real-space refinement and correction in COOT.

All graphical representations and figures of our structural models were made in either PyMOL (Schrodinger, 2010) or Chimera (Pettersen et al., 2004).

### [35S]O42- Uptake Experiments

#### In whole cells

The wild-type parental E. coli K-12 strain BW25113 (F-, Δ(araD-araB)567, ΔlacZ4787(::rrnB-3), λ-, rph-1, Δ(rhaD- rhaB)568, hsdR514) and the E. coli K-12 cysZ knockout strain JW2406-1 (F-, Δ(araD-araB)567, ΔlacZ4787(::rrnB-3), λ-, ΔcysZ742::kan,rph-1, Δ(rhaD- rhaB)568, hsdR514) were obtained from the Coli Genetic Stock Center at Yale University (http://cgsc.biology.yale.edu/), originally found in the Keio knockout collection (Baba et al., 2006). Cells were made competent by standard protocols (Hanahan, 1983). The strains were grown in LB (Luria Broth) without any antibiotic (BW25113) or with 50 μg/ml of kanamycin (JW2406-1) at 37°C overnight to stationary phase and the cultures were collected by centrifugation at 3000 x g. Cells were resuspended in Davis-Mingioli (DM) minimal media without sulfate (MgSO4 was replaced with MgCl2 and (NH4)2SO4 was replaced by NH4Cl), supplemented with 0.63 mM L-cysteine and were allowed to grow in the absence of sulfate (Davis and Mingioli, 1950) for a minimum of 9 hr but no longer than 16 hr at 37°C to ensure that the cells were starved of sulfate and the sulfate stores in the cell were depleted to enhance sulfate uptake measurements (F. Parra, personal communication). The cells were collected, washed 3 times in 5 mM Na-Hepes pH 7.0, and resuspended in the same buffer at 0.7 mg cell protein/ml at room temperature. Uptake (performed in triplicate) was initiated by the addition of 320 μM of Na2[35S]O4 to the cell suspension (at a final cell protein concentration of 0.07 mg/mL) and was measured over a time course of typically 0–300 s. The reaction was stopped by diluting the reaction mixture with 1.5 ml of ice-cold 5 mM Na-Hepes, pH 7.0 and immediately filtered through glass-fiber filters (0.75 μm, GF/F). Filters were washed once more with 1.5 ml of buffer, dried, and incubated with EconoSafe scintillation cocktail for >12 hr prior to counting of the radioactivity in a Hidex 300 SL scintillation counter. For the CysZ- cell rescue experiments, a similar protocol was used, transformed with an ampicillin resistant expression vector containing the cysZ gene, mutant or empty vector (as the control). Upon transformation, the cells were grown overnight in a 4 ml starter culture of LB with 50 μg/ml kanamycin and 100 μg/ml ampicillin. The next morning the entire 4 ml was used to inoculate 75 ml of LB (Kan, Amp), and grown at 37°C for 2.5–3 hr until an OD600 of 0.6–0.8 was reached. Protein expression was then induced at 37°C for 4 hr with 0.2 mM IPTG. After 4 hr, the cells were spun down and resuspended in the DM minimal media without sulfate, 0.63 mM cysteine, Amp, Kan and 0.2 mM IPTG, and incubated overnight at 22°C. The next morning the cells were spun down, washed 3 times with 5 mM Na-Hepes 7.0 and resuspended at final concentration of 0.7 mg/ml for uptake.

#### In proteoliposomes

CysZ was purified by the procedure described above, and upon elution from the size-exclusion column concentrated to 1 mg/ml for reconstitution into liposomes at a protein to lipid ratio of 1:100. The liposomes were comprised of a 3:1 ratio of E. coli polar lipids and phosphatidylcholine (PC) (Avanti Polar Lipids, Alabastar, Alabama), prepared by previously described methods (Rigaud et al., 1995). Typically, 4 μl of CysZ-proteoliposomes (corresponding to ~0.2 μg CysZ) and control ‘empty’ liposomes at a concentration of 5 mg/ml, were assayed in 100 μl of reaction buffer containing [35S]O42- (the specific radioactivity was adjusted with Na2SO4) and additions as indicated at the indicated concentrations for the indicated periods of time. Reactions were stopped by the addition of ice-cold 5 mM Na-Hepes, pH 7.0 and filtered through 0.22 μm nitrocellulose filters as described above for whole-cell uptake studies.

#### Calculation of internal substrate concentration in proteoliposomes

The determination of lipid molecules in a proteoliposome was performed according to the following calculation:$N_{totPL}=\frac{4\pir^{2}+(4\pir-m^{2})}{a}$, where NtotPL is the total number of lipid molecules per proteoliposome, r the radius (external; 50 nm in a 100-nm proteoliposome), m the membrane thickness (4 nm), r-m the radius (internal), and a is the area of the lipid headgroups (0.7 nm2) (Lind, 2015). Accordingly, NtotPL = 82866.24. With an average MW of 790.85 of the lipids in the liposome preparation, the lipid concentration in the assay (4 μL of 5 mg/mL proteoliposomes in 100 μL assay volume) is 0.2 g lipid/L or 2.53 x 10−4 M. The number of lipids (Nlipids) per liter is the product of the lipid concentration and Avogadro’s number (NA) to be 2.53 x 10−4 mol/L x 6.022 x 1023 mol−1 = 1.523 x 1023 lipids/L. The number of proteoliposomes in the sample (NPL) can be calculated according to Nlipids/NtotPL, yielding NPL = 1.523 x 1023 lipids/L x 82,866.24 lipids/proteoliposome = 1.838 x 1015 proteoliposomes/L or 1.838 x 1011 proteoliposomes/100 μL. The intraliposomal volume (VPL) in a 100 μL-assay is calculated according to$V_{PL}=\frac{4}{3}\pir-m^{3}xN_{PL}$ = 7.49 x 10−8 L or 0.0749 μL. In Fig. 4b, SO42- accumulation at the 15-s time point for PdCysZ is 0.1869 nmol, yielding a concentration of 2.49 mM SO42-; the SO42- accumulation at the plateau (120-s time point) is 0.1145 nmol, yielding an internal concentration of 1.53 mM. Thus, at an external SO42- concentration of 0.5 mM, this is a ~ 5-fold concentration excess at the peak uptake point (15 s) or a ~ 3-fold excess at the plateau level. For comparison of the CysZ-mediated SO42- accumulation to the concentrative transport of a Na+-coupled secondary transporter, we performed the same calculation for 3H-Trp transport in proteoliposomes containing the multi-hydrophobice substrate transporter, MhsT (Malinauskaite, 2014). The turnover of Trp transport was determined to be 0.8±0.03 s−1. The accumulation of 2.5 μM Trp (about Km) at the 10-s time point was 2.78 x 10−11 mol, yielding an internal concentration of the amino acid of 373.8 μM – a ~150-fold excess of the accumulated amino acid vs the external concentration of 2.5 μM.

### Radioligand binding by Scintillation Proximity Assay (SPA)

CysZ was purified by standard protocols as described above, with the exception of leaving the histidine-tag intact without cleavage by the TEV protease. The imidazole was removed by dialysis and the purified protein was not run over the size exclusion column, and instead was directly concentrated to 2 mg/ml for the SPA experiment. [35S]O42- obtained in the form of sulfuric acid (American Radiolabeled Chemicals (ARC), St. Louis, Missouri) was used asthe radioligand. 200 ng of CysZ was used per assay point, diluted in 100 μl of assay buffer containing 20 mM Hepes pH 7.0, 200 mM NaCl, 0.2% DeM, 20% glycerol, 0.5 mM TCEP, and 125 μg of copper PVT SPA beads (Perkin Elmer, Waltham, Massachusetts). Binding of 100 μM [35S]O42- (at a specific activity of 50 mCi/mmol; mixed with non-labeled Na2SO4) by CysZ was measured in 96-well clear-bottom plates. For isotopic dilutions or competition assays, 10 nM – 100 mM of Na2SO4 or Na2SO3, respectively, were added simultaneously with the radiolabeled substrate. 800 mM imidazole were added to a set of samples (for each individual condition) to determine the non-proximity (background) signal as imidazole competes with His-tagged CysZ for binding to the Cu2+-coated SPA beads. Plates were agitated for a minimum of 30 min or up to 16 hr at 4°C, and measured in the SPA mode of a Wallac MicroBeta1450 scintillation counter (Perkin Elmer, Waltham, Massachusetts). All data were analyzed with GraphPad Prism7 software.

### Microscale thermophoresis (MST)

Direct binding of SO32- by CysZ was measured with microscale thermophoresis using the Monolith NT.LabelFree (NanoTemper Technologies, Germany), which detects the relative change in native tryptophan emission at 336 nm. The binding affinity was determined using 500 nM purified CysZ from either P. denitrificans or I. loihiensis by mixing the protein with a serial dilution of Na2SO3 (0.5–47.5 mM) in buffer containing 20 mM Hepes, pH 6.5, 10% glycerol, 100 mM NaCl, 0.5 mM TCEP and 0.1% n-decyl-β-D-maltopyranoside (DM). The osmolality of all test solutions was maintained by adding appropriate concentrations of NaCl. The mixture was incubated for 20 min at room temperature and then loaded into Monolith NT.LabelFree Zero Background Standard Treated Capillaries. Measurements were carried out at high (60%) MST power and 15% excitation power using the MO.Control v1.4.4 software. The MST data at 19–20 s after IR laser power exposure was collected and the normalized fluorescence was subjected to non-linear regression fitting in Prism seven to obtain the EC50. MST measurements involving PfCysZ were inconclusive.

### Measurement of CysZ single-channel activity in the planar lipid bilayer

A previously described method (Mueller et al., 1962) to insert ion channels incorporated in liposomes into ‘painted’ planar lipid bilayers by vesicle fusion was used to incorporate CysZ into a lipid bilayer created on a small aperture between two aqueous compartments, called the cis and trans compartments (Morera et al., 2007). Phosphatidylethanolamine (PE) and phosphatidylserine (PS) (Avanti Polar Lipids, Alabaster, Alabama), in a ratio of 1:1 were dissolved in chloroform to mix, and dried completely under an argon stream. The mixed and dried lipids were then dissolved in n-decane to a final concentration of 50 μg/ml, and kept at 4°C. The lipids are always prepared fresh, on the same day of the experiment. The purified CysZ proteins were incorporated into PE:PS (1:1) liposomes by brief sonication at 80 kHz for 1 min at 4°C. Since this system is very sensitive to contaminants, CysZ was expressed in and purified from a porin-deficient strain of E. coli cells to prevent any carry through of contaminating porins that could create large conductances and artifacts in the single-channel recordings. However, we cannot rule out that our preparation contained such contaminants that eventually precluded more detailed electrophysiological measurements. The experimental apparatus consisted of two 1 ml buffer chambers separated by a Teflon film that contains a single 20- to 50 μm hole. A lipid bilayer was formed by ‘painting’ the hole with the 1:1 mixture of PE:PS, this results in a seal between the two cups formed by the lipids (Leal-Pinto et al., 1995). For these studies, the cis side was defined as the chamber connected to the voltage-holding electrode and all voltages are referenced to the trans (ground) chamber. Stability of the bilayer was determined by clamping voltage at various levels. If a resistance >100 Ω and noise <0.2 pA were maintained in the patch, the proteoliposomes containing CysZ were added to the trans side of the chamber and stirred for 1 min. The fusion event or insertion of a channel into the bilayer was assessed by the presence of clear transitions from 0 current to an open state.

### Site-specific cysteine labeling experiments

All functional and cysteine mutants of CysZ were generated by site-directed mutagenesis, using the QuikChange site-directed mutagenesis kit (Agilent Technologies, Santa Clara, California). The sequence-verified mutants were then tested for expression in comparison to the WT CysZ. To address the membrane topology of IlCysZ, single cysteine mutants were designed to perform site-directed fluorescence labeling based on the accessibility of the cysteine to the membrane impermeable thiol-directed fluorescent probe (Ye et al., 2001). A set of surface-exposed residues at different positions on the CysZ molecule were selected to be mutated to cysteines, based on the IlCysZ structure. The cysteine mutants were expressed by standard protocols that were used for the WT protein. The membrane fraction of each mutant was pelleted after cell lysis by ultracentrifugation at 100,000 x g and resuspended at 20 mg/ml (Bradford assay) in fresh buffer containing 20 mM Na-Hepes pH 7.0, 200 mM NaCl, protease inhibitors: 0.5 mM PMSF and Complete protease inhibitor cocktail EDTA-free and 1 mM TCEP-HCl. 1 ml of membranes were then incubated with 30 μM membrane-impermeant fluorescein-5-maleimide dye (2 mM stock freshly prepared in water, protected from light) for 30 min in the dark at room temperature. The labeling reaction was stopped by the addition of 6 mM β- mercaptoethanol, and the membranes were spun down and resuspended in fresh buffer to remove any remaining unreacted fluorescent dye. The fluorescently labeled protein was then purified from the membranes by solubilization with 1% DM, using a standard Ni-NTA purification protocol, qualitatively analyzed on an SDS-PAGE, and quantitatively measured by a Tecan fluorescence plate reader at an excitation of 495 nm, emission of 535 nm.

### Crosslinking of cysteine mutant pairs in CysZ

Cysteine mutants of PfCysZ and IlCysZ were designed based on pairs of residues that were in close proximity (within 3–7 Å) of each other in our structure that could have the ability to covalently join the 2 protomers of the dimer. The single and double cysteine mutants were made by site-directed mutagenesis using the QuikChange Site-Directed Mutagenesis Kit (Agilent Technologies, Santa Clara, California). Mutants and WT were expressed using the standard protocols CysZ expression. Isolated membrane fraction was resuspended by homogenization in fresh lysis buffer at a membrane protein concentration of ~25 mg/ml (measured by Bradford Assay). Bis-methanethiosulfonate (Bis-MTS) crosslinkers (Santa Cruz Biotechnologies, Dallas, Texas) of different spacer lengths were used at 0.5 mM (dissolved in DMSO) added to 1 ml of resuspended membranes at RT for 1 hr. Bis-MTS crosslinkers are membrane permeable, highly reactive and specific to sulfhydryl groups, and the covalent linkage is resistant to reducing agents like β-mercaptoethanol (Akabas et al., 1992). The crosslinking lengths used were: 1,1-Methanediyl Bismethanethiosulfonate (3.6 Å), 1,2- Ethanediyl Bismethanethiosulfonate (5.2 Å), 1,4-Butanediyl Bismethanethiosulfonate (7.8 Å) and 1,6-Hexanediyl Bismethanethiosulfonate (10.4 Å). The reaction was quenched by the addition of 10 mM free cysteine, and the protein was then extracted and purified from the membranes with 1% DM followed by Ni-NTA resin. The imidazole is then diluted out in the Ni-elute, and the His-tag is cut with TEV protease in small scale. The cleaved protein is passaged over Ni-NTAresin to remove contaminants and uncleaved protein, and flowthrough is run on a reducing SDS- PAGE and stained with Coomassie blue to analyze dimer formation. The mutants designed were L161C (single mutant), L161C-A164C and N160C-L168C (double mutants) for PfCysZ; and L156C-Q163C and V157C-Q163C (double mutants) for IlCysZ.

### PDB accession codes

Idiomarina loihiensis CysZ: 3TX3, Pseudomonas fragi CysZ: 6D79, Pseudomonas denitrificans CysZ: 6D9Z.
