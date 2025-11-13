# The structure of the endogenous ESX-3 secretion system

## Authors

- Nicole Poweleit<sup>1</sup> ([ORCID: 0000-0002-2700-0241](https://orcid.org/0000-0002-2700-0241))
- Nadine Czudnochowski<sup>1</sup> ([ORCID: 0000-0002-3146-4110](https://orcid.org/0000-0002-3146-4110))
- Rachel Nakagawa<sup>1</sup>
- Donovan D Trinidad<sup>1</sup> ([ORCID: 0000-0002-1439-9927](https://orcid.org/0000-0002-1439-9927))
- Kenan C Murphy<sup>3</sup>
- Christopher M Sassetti<sup>3</sup>
- Oren S Rosenberg<sup>1</sup> ([ORCID: 0000-0002-5736-4388](https://orcid.org/0000-0002-5736-4388)) †

### Affiliations

1. Department of Medicine, Division of Infectious Diseases University of California, San Francisco San Francisco United States
2. Chan-Zuckerberg Biohub University of California, San Francisco San Francisco United States
3. Department of Microbiology and Physiological Systems University of Massachusetts Medical School Worcester United States

† Corresponding author

## Abstract

The ESX (or Type VII) secretion systems are protein export systems in mycobacteria and many Gram-positive bacteria that mediate a broad range of functions including virulence, conjugation, and metabolic regulation. These systems translocate folded dimers of WXG100-superfamily protein substrates across the cytoplasmic membrane. We report the cryo-electron microscopy structure of an ESX-3 system, purified using an epitope tag inserted with recombineering into the chromosome of the model organism Mycobacterium smegmatis. The structure reveals a stacked architecture that extends above and below the inner membrane of the bacterium. The ESX-3 protomer complex is assembled from a single copy of the EccB3, EccC3, and EccE3 and two copies of the EccD3 protein. In the structure, the protomers form a stable dimer that is consistent with assembly into a larger oligomer. The ESX-3 structure provides a framework for further study of these important bacterial transporters.

## Introduction

Mycobacteria use a set of specialized secretion systems called ESX to transport proteins across their complex, diderm cell walls (Gröschel et al., 2016). Originally described as virulence factors in Mycobacteria tuberculosis (Guinn et al., 2004; Hsu et al., 2003; Lewis et al., 2003; Stanley et al., 2003), orthologs of ESX have since been discovered in most Gram-positive bacteria (Bottai et al., 2017), and are more generally referred to as Type VII secretion systems (Bitter et al., 2009). In mycobacteria there are five paralogous ESX operons (ESX 1–5) each of which encodes an inner membrane translocon complex consisting of three conserved Ecc proteins: EccB, EccC, and EccD. A fourth protein, EccE is conserved in all ESX operons except the ancestral ESX-4 operon and is also considered a part of the ESX translocon complex as it copurifies with EccB, EccC, and EccD (Houben et al., 2012). All Type VII secretion systems translocate proteins in the WXG100-superfamily, which share a common two-helix hairpin structure and are found as homo- or heterodimers (Poulsen et al., 2014) and are mutually dependent for secretion with other substrates (Fortune et al., 2005). In contrast to the general secretory apparatus (Sec), ESX substrates have been shown to be secreted in their folded, dimeric state (Sysoeva et al., 2014).

Structural and functional information has been reported for truncated and isolated, soluble domains of the ESX translocon complexes and their homologs (Korotkova et al., 2015; Korotkova et al., 2014; Renshaw et al., 2005; Rosenberg et al., 2015; Strong et al., 2006; Wagner et al., 2016; Wagner et al., 2014; Wagner et al., 2013; Zhang et al., 2015; Zoltner et al., 2016). A low resolution, negative stain electron microscopy structure of ESX-5 shows a translocon complex assembled into a hexamer (Beckham et al., 2017). Structures of other proteins encoded in ESX operons including secreted substrates (Ilghari et al., 2011), substrate chaperons (Ekiert and Cox, 2014), and the protease MycP (Solomonson et al., 2013) have been solved. Despite revealing important functional information about ESX, structures of overexpressed and isolated proteins are insufficient to understand the regulated secretion of fully folded substrates. We therefore undertook structural studies of an endogenously expressed ESX-3 complex from the model organism M. smegmatis using cryo-electron microscopy (cryo-EM). During the preparation of this work for publication, a similar structure of the ESX-3 system expressed from a plasmid was published by another group (Famelis et al., 2019).

The ESX-3 translocon complex is important for iron acquisition (Serafini et al., 2013; Siegrist et al., 2009), cell survival (Tinaztepe et al., 2016), and virulence in pathogenic mycobacteria (Tufariello et al., 2016), and its role in iron homeostasis is conserved in the model system, M. smegmatis (Siegrist et al., 2009). The ESX-3 translocon complex proteins are transcribed in a single operon (Li et al., 2017), and expression of the ESX-3 operon is dependent on the transcriptional regulator IdeR, which controls iron metabolism (Rodriguez et al., 2002) and is required for growth in the human pathogen M. tuberculosis (Pandey and Rodriguez, 2014). The ESX-3 operon is 67% identical between the non-pathogenic model organism M. smegmatis and the pathogen M. tuberculosis over the 4354 amino acids of the ESX-3 operon. This high degree of conservation and essential role in cell growth makes ESX-3 an important candidate for small molecule inhibition (Bottai et al., 2014), as blockade of ESX-3 will both inhibit virulence in M. tuberculosis and kill a broad range of pathogenic mycobacteria.

## Results

A major innovation made possible by the dramatic improvements in cryo-EM (Cheng, 2018) is the ability to examine challenging protein samples at atomic resolution, even when samples are only available at low concentrations. When coupled with recent genetic manipulations that allow for facile insertion of chromosomal epitope and purification tags (Murphy et al., 2018), cryo-EM now holds the promise of routine structural characterization of many endogenously expressed protein complexes not previously tractable by structural techniques. We undertook the purification of the ESX-3 complex from the native host without the need for overexpression. To facilitate purification of the endogenous translocon complex, a cleavable EGFP tag was inserted into the chromosome of M. smegmatis mc(2)155 (wild type) and ΔideR (Dussurget et al., 1996) strains at the C-terminus of EccE3 via the ORBIT method (Murphy et al., 2018) (Figure 1A, Figure 1—figure supplement 1). EccE3 is the final gene in the 11 gene long ESX-3 operon making insertion at this site less likely to disrupt regulation and expression of the operon. Deletion of the gene for the iron acquisition regulator IdeR greatly increases chromosomal expression of ESX-3 from negligible amounts of protein to a yield sufficient for purification and structure determination (Figure 1—figure supplement 2A). Components of ESX-3 were pulled down using an anti-GFP nanobody (Rothbauer et al., 2008) and the EGFP tag was proteolytically cleaved. After size exclusion chromatography, the peak fractions were pooled and analyzed biochemically and by cryo-EM .

### Global structure of the ESX-3 dimer

Four components of the ESX-3 translocon complex EccB3, EccC3, EccD3 and EccE3 were stably affinity-purified as a large molecular weight species of about 900 kDa (Figure 1B and C, Figure 1—figure supplement 2B). The sample was imaged by cryo-EM and reconstructed revealing a dimeric structure, which can be divided into four areas: the flexible periplasmic multimerization domain, the stable transmembrane region, the stable upper cytoplasmic region, and the flexible lower cytoplasmic motor domain (Figure 1D, Table 1). While the peak fraction does not contain particles of a larger size consistent with higher order oligomers, thorough examination of the void volume revealed a small number of particles in a higher oligomeric state (Figure 1—figure supplement 3A–E). The resolution of the ESX-3 dimer varies substantially in different parts of the electron microscopy map and this heterogeneity was partially resolved through data processing (Figure 1—figure supplement 4 and Figure 1—figure supplement 5). Initially, the entire ESX-3 dimer was reconstructed to 4.0 Å resolution (Figure 1—figure supplement 6A). Using symmetry expansion, and focused classification and refinement techniques, the resolutions of targeted regions of the ESX-3 complex were improved to 3.7 Å for the transmembrane region and upper cytoplasmic region (Figure 1—figure supplement 6B–D), 5.8 Å for the periplasmic region (Figure 1—figure supplement 6E), and ~7 Å resolution for the lower cytoplasmic region (Figure 1—figure supplement 6F). The highest resolution maps for each region were combined and filtered to the threshold of the lowest resolution map to form an overall 10 Å combination map for the entire ESX-3 dimer.

![Figure 1.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig1-v2.jpg)

**Figure 1.:** (A) The ESX-3 operon in M. smegmatis and the placement of the purification tag. Genomic deletion of ideR derepresses ESX-3 to boost expression for purification. (B) SDS-PAGE of purified ESX-3 shows four major bands corresponding to EccB3, EccC3, EccD3, and EccE3. (C) Blue native page of the purified ESX-3 complex shows a large molecular weight band around 900 kDa. (D) Merged maps of all focused refinement maps (gray transparency) of the ESX-3 dimer filtered to 10 Å resolution. The transmembrane and upper cytoplasmic focused maps (3.7 Å) are segmented by subunit showing one copy per protomer of EccB3 (pink), EccC3 (blue), EccE3 (orange), EccD3-bent (yellow), and EccD3-extended (green). (E) Atomic models of the transmembrane and upper cytoplasmic regions. (F) A combined map of the full complex filtered to 10 Å resolution (gray transparency) with full models for each protein, EccD3-bent (yellow), EccD3-extended (green), EccE3 (orange), EccC3 (blue), and EccB3 (pink).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Diagram of the ESX-3 operon in M. smegmatis mc(2)155. (B) The targeting oligo used to insert the attP site into the chromosome. (C) The tagging plasmid.(D) Cartoon of the resulting change to the chromosome after ORBIT.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Western blot of solubilized cell material with EccE3 tagged with EGFP. Lane 1, wild type background. Lane 2, ΔideR background. (B) Size exclusion profile for the ESX-3 dimer purified on a Superose 6 10/300column.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Size exclusion profile with void volume and peak fractions indicated. (B) SDS-PAGE of all fractions from the beginning of elution until the end of the peak fraction. (C) BN-PAGE of the void and peak fractions (D) Cryo-EM of the void volume. Scale bar 50 nm (E) 2D class averages of the particles picked from the void volume, some classes reveal possible higher order oligomers. Scale bar 20 nm.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** An initial data set was collected on a Talos Arctica microscope. The final refinement from this data processing was used as the starting model for future data processing.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** Data was collected on a Titan Krios. Particles from the final reconstruction were subsequently used for focused classification and refinement.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** (A) Consensus refinement map and FSC curve for the ESX-3 complex. Focused refinement maps and FSC curves for (B) the left protomer of the ESX-3 complex, (C) the right protomer of the ESX-3 complex, (D) a symmetry expanded protomer, (E) the periplasmic domain of EccB and (F) the lower ATPase domains of EccC. All maps are unsharpened and unmasked.

**Table 1.**
 Data collection and refinement statistics.Collection parameters for initial test data set and void peak analysis on the Talos Arctica and final collection on Titan Krios microscopes. Refinement details for initial model, consensus map, and focused refinements.


<table>
  <thead>
    <tr>
      <th colspan="5">Data Collection</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Collection</td>
      <td>Initial Screening</td>
      <td>Collection 1</td>
      <td>Collection 2</td>
      <td>Void peak</td>
    </tr>
    <tr>
      <td>Microscope</td>
      <td>Talos Arctica</td>
      <td>Titan Krios</td>
      <td>Titan Krios</td>
      <td>Talos Arctica</td>
    </tr>
    <tr>
      <td>Voltage (kV)</td>
      <td>200</td>
      <td>300</td>
      <td>300</td>
      <td>200</td>
    </tr>
    <tr>
      <td>Detector</td>
      <td>Gatan K2</td>
      <td>Gatan K2</td>
      <td>Gatan K2</td>
      <td>Gatan K3</td>
    </tr>
    <tr>
      <td>Pixel size (Å/pixel)</td>
      <td>1.14</td>
      <td>0.82</td>
      <td>0.82</td>
      <td>0.9</td>
    </tr>
    <tr>
      <td>Exposure Time (s)</td>
      <td>9</td>
      <td>10</td>
      <td>10</td>
      <td>11.7</td>
    </tr>
    <tr>
      <td>Electron dose (e-/Å2)</td>
      <td>63</td>
      <td>80</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <td>Defocus range (µm)</td>
      <td>1.5-2.5</td>
      <td>0.4-1.2</td>
      <td>0.6-1.4</td>
      <td>1.5-2.5</td>
    </tr>
    <tr>
      <td>Number of micrographs</td>
      <td>2,499</td>
      <td>2,705</td>
      <td>4,632</td>
      <td>1,215</td>
    </tr>
    <tr>
      <td colspan="5">Consensus Reconstruction</td>
    </tr>
    <tr>
      <td>Data Set</td>
      <td>Initial Screening</td>
      <td>Collection 1 &amp; 2</td>
      <td></td>
      <td>Void peak</td>
    </tr>
    <tr>
      <td>Software</td>
      <td>Relion 2.1, cisTEM, and cryosparc</td>
      <td>Relion 3.0</td>
      <td></td>
      <td>cisTEM</td>
    </tr>
    <tr>
      <td># of particles, picked</td>
      <td>240,000</td>
      <td>778,149</td>
      <td></td>
      <td>259,333</td>
    </tr>
    <tr>
      <td># of particles post, Class2D</td>
      <td>138,000</td>
      <td>554,901</td>
      <td></td>
      <td>640</td>
    </tr>
    <tr>
      <td># of particles post, Class3D</td>
      <td>46,830</td>
      <td>362,438</td>
      <td></td>
      <td>NA</td>
    </tr>
    <tr>
      <td># of particles post, skip align Class3D</td>
      <td>NA</td>
      <td>90,479</td>
      <td></td>
      <td>NA</td>
    </tr>
    <tr>
      <td>Symmetry</td>
      <td>C1</td>
      <td>C1</td>
      <td></td>
      <td>NA</td>
    </tr>
    <tr>
      <td>Map sharpening B-factor (Å2)</td>
      <td>NA</td>
      <td>-160</td>
      <td></td>
      <td>NA</td>
    </tr>
    <tr>
      <td>Final resolution (Å)</td>
      <td>4.7 Å</td>
      <td>4.0 Å</td>
      <td></td>
      <td>NA</td>
    </tr>
    <tr>
      <td colspan="5">Focused Refinements</td>
    </tr>
    <tr>
      <td>Location of focus</td>
      <td># of particles</td>
      <td>Resolution</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protomer i</td>
      <td>76,967</td>
      <td>3.8</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protomer ii</td>
      <td>90,479</td>
      <td>3.8</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Symmetry expanded protomer</td>
      <td>52,067</td>
      <td>3.7</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Periplasmic EccB3</td>
      <td>70,000</td>
      <td>5.8</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ATPase 1, 2, and 3</td>
      <td>30,000</td>
      <td>7</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

The ESX-3 dimer is comprised of ten total proteins, two copies each of EccB3, EccC3, and EccE3 and four copies of EccD3. Two pseudo-symmetric protomers referred to as i and ii, combine to form the ESX-3 dimer. Each protomer contains one copy of EccB3, EccC3, and EccE3 and two conformationally distinct copies of EccD3, referred to as EccD3-bent and EccD3-extended (Figure 1E) based on their highly asymmetric conformations. At 3.7 Å resolution, it was possible to build de novo atomic models for all observable amino acids in the transmembrane and upper cytoplasmic regions, except the two transmembrane helices of EccC3 (Figure 1E and Supplementary file 1). The lower resolution regions of density, the EccC3 transmembrane helices, EccC3 ATPase 1, 2, and 3 domains and the EccB3 periplasmic domain, were flexibly fit using homology models. Using this hybrid approach, a model of the entire ESX-3 dimer has been produced (Figure 1F).

### EccD3 forms a homodimer that encloses a large hydrophobic cavity

There are two copies of EccD3 in each ESX-3 protomer (Figure 2A). The ubiquitin-like N-terminal domain of each EccD3 molecule interacts with EccE3 and EccC3 in the cytoplasm, and a long linker joins the soluble domain of EccD3 to 11 transmembrane helices (Figure 2B and Figure 2—figure supplement 1A–F). The four EccD3 molecules account for 44 of the total 54 transmembrane helices observed in the ESX-3 dimer. A distinct transmembrane cavity is formed by dimerization of the two copies of EccD3 in each protomer with a cross-sectional diameter of ~20×30 Å without significant regions of constriction. Transmembrane helices 1, 9 and 10 interact across the cavity dimer interface in a tight bundle making passive lipid transport into the membrane from the cavity unlikely (Figure 2C). The inner surface of the periplasmic half of the cavity is composed primarily of hydrophobic residues and in our maps, eight extended densities consistent with hydrophobic lipid tails or detergent molecules line the periplasmic inner face of the cavity (Figure 2C). In contrast, the cytoplasmic face of the cavity has several polar residues and ordered hydrophobic densities are not visible.

![Figure 2.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig2-v2.jpg)

**Figure 2.:** (A) EccD3-bent (yellow) and EccD3-extended (green) in the context of the overall ESX-3 dimer (gray transparency). (B) Atomic models of EccD3-bent and EccD3-extended (C) An unsharpened electron microscopy density map of the ESX-3 dimer shows extra densities consistent with lipid or detergent molecules (teal) on the periplasmic face of the EccD3 cavity. (D) EccD3-bent (yellow) and EccD3-extended (green) aligned based on the transmembrane regions shows two distinct conformations of the EccD3 cytoplasmic domains. Amino acids 100–127 of EccD3 adopt a bent (yellow) and an extended (green) conformation.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Map to model fits for EccD3-bent for (A) transmembrane helix 1, amino acids 136–153, (B) transmembrane α-helix 1, amino acids 385–402, and (C) soluble domain β-strands amino acids 10–15 and 90–96. Map to model fits for EccD3-extended for (D) transmembrane helix 1, amino acids 163–181 (E) transmembrane helix 11, amino acids 446–469 (F) soluble loop, amino acids 297–315. (G) Conservation mapping onto the residues of the EccD3 linker, amino acids 100–127. (H) Amino acids 100–127 from EccD3-bent (yellow) interact with EccB3 (pink) and EccC3 (blue). (I) Amino acids 100–127 of EccD3-extended (green), in a distinct conformation, interact with EccE3 (orange) and EccD3-bent (yellow).

In the cytoplasm below the membrane, a stable, upper cytoplasmic region is formed by interactions between the soluble domains of EccD3-bent, EccD3-extended, EccE3, and EccC3. The linker joining the cytoplasmic ubiquitin-like domain to transmembrane helix 1 (residues 100–127) of EccD3 conserves a high sequence identity throughout evolution (Ashkenazy et al., 2016), yet it adopts two distinct secondary structures resulting in the asymmetric placement of the cytoplasmic domains of EccD3 (Figure 2D and Figure 2—figure supplement 1A–G). In EccD3-bent, residues 100–127 are bent, folding into an α-helix and forming a nexus of stabilizing contacts with EccB3 and EccC3 (Figure 2—figure supplement 1H). In EccD3-extended, residues 100–127 are extended and fold into a shorter α-helix that interacts with EccE3 and the cytoplasmic domain of EccD3-bent (Figure 2—figure supplement 1I). This conformational flexibility suggests that if residues 100–127 were released from their associations with EccC3 and EccE3 they could rearrange into the alternative bent or extended conformation with little energetic barrier.

### EccC3 and EccE3 make extensive, stabilizing interactions with the asymmetric, cytoplasmic domains of EccD3

The next component of the stable upper cytoplasmic region is EccE3. EccE3 is positioned at the front of the ESX-3 dimer (Figure 3A), where the conserved transmembrane helix 1 of EccE3 interacts with helix 11 of EccD3-bent in the membrane. Helix 1 is followed by a second EccE3 transmembrane helix, a linker helix, and then extends into the cytoplasm (Figure 3B and C and Figure 3—figure supplement 1A–D). The anti-parallel β-sheets of the cytoplasmic domain of EccE3 have weak structural homology to glycosyl transferase proteins, however, the nucleotide binding pocket is absent in EccE3, leaving it incapable of performing this function (Figure 3—figure supplement 1E and F, Supplementary file 2). EccE3 does not have another obvious ligand or catalytic site. Two conserved helices in the cytoplasmic region of EccE3 between amino acids 133 and 163 form extensive stabilizing interactions with both subunits of EccD3 (Figure 3D, Figure 3—figure supplement 1G). These interactions hold the flexible linker of EccD3-extended in the extended conformation and sterically hinder EccD3-extended from assuming the bent conformation (Figure 3—figure supplement 1H). EccE3 does not form direct protein-protein interactions with either EccB3 or EccC3 suggesting the contacts with EccD3-extended and EccD3-bent are extremely stable as EccE3 was the tagged protein used to immunoprecipitate the ESX-3 dimer.

![Figure 3.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig3-v2.jpg)

**Figure 3.:** (A) The placement of EccE3 in the overall ESX-3 dimer. (B) Atomic model of EccE3 (C) Transmembrane helix 1 of EccE3 interacts with transmembrane helix 11 of EccD3-bent (D) Two soluble helices of EccE3 interact with EccD3-extended and EccD3-bent.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Map and model comparison for transmembrane helix 1, amino acids 1 to 18. (B) Beta strand separation, amino acids amino acids 221 to 240. (C) A single beta strand, amino acids 117 to 126. (D) Conservation mapping onto transmembrane helix1 of EccE3 and transmembrane helix11 of EccD3-bent. (E) Comparison between the structure of EccE3 and the top DALI hit 5FXF-B. (F) Close up on the FADH (cyan) binding pocket of 5fxf-B which is not present in EccE3. (G) Conservation mapping onto the protein-protein interaction soluble helix of EccE3. (H) Residues 133–163 of EccE3 interact substantially with EccD3-bent and EccD3-extended, holding the flexible linker of EccD3-extended in the extended conformation. (H) EccE3 (orange) stabilizes the extended conformation of EccD3-extended (green) and sterically hinders it from adopting the bent conformation (neon green).

The final component of the stable upper cytoplasmic region is the domain of unknown function (DUF) of EccC3. EccC3 extends from the membrane into the upper and lower cytoplasmic regions (Figure 4A). Amino acids 1–33 and 94–403 of EccC3 were built de novo into the higher resolution region of the electron microscopy map revealing the structure of the DUF domain (Figure 4B, Figure 4—figure supplement 1A–C). The de novo model of the DUF has the typical Rossman fold of a nucleotide hydrolysis domain (Figure 4—figure supplement 1D and E) and its closest homolog by Dali search is the ATPase 1 domain of EccC of T. curvata. It is linked to the transmembrane domains by a long helical bundle making extensive contacts with the flexible linker region of EccD3-bent (Figure 4C). The DUF makes additional stabilizing contacts with the ubiquitin-like domains of EccD3-bent and EccD3-extended in the cytoplasm (Figure 4D).

![Figure 4.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig4-v2.jpg)

**Figure 4.:** (A) The placement of EccC3 in the overall ESX-3 dimer. (B) Atomic model of the EccC3 DUF (C) The stalk helices of EccC3 interact with EccB3, EccD3-bent, and EccD3-extended (D) Interactions between EccC3 and the ubiquitin-like domains of EccD3-bent and EccD3-extended in the cytoplasm.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Map and model of the EccC DUF domain, amino acids amino acids 97 to 130. (B) Two beta strands in the EccC DUF domain, amino acids 314 to 319 and 337 to 343. (C) Beta strand in the EccC DUF domain, amino acids 314 to 319. (D) Overlay of the model of the EccC DUF domain with the top DALI hit, 4NH0-A (white). (E) Close up of the ATP binding pocket of 4NH0-A. The ATPase fold remains intact in the DUF domain.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Overlay of the focused refined maps of the transmembrane and upper cytoplasmic regions of protomer i (red) and protomer ii (blue). The two protomers are nearly identical except in the transmembrane domains of EccC3 and the N-terminal tail of EccB3. (B) Density subtraction of the two protomers in A highlights the regions of difference. Specifically, the transmembrane helixes of EccC3 adopt distinct conformations across protomers. (C) In protomer i, 4NH0, the crystal structure of EccC from T. curvata, fits well in the density. In protomer ii, ATPase 2 and 3 fit well into the density but the position of ATPase 1 in the crystal structure, shown by the red dotted circle, does not fit into the density. A density of about the right size for ATPase 1 is shown in yellow. Fitting of ATPase 1 in this density requires the disruption of the interface between ATPase 1 and ATPase 2.

When the transmembrane and upper cytoplasmic regions are compared between protomers, only the transmembrane helices of EccC3 and the N-terminal tail of EccB3 differ (Figure 4—figure supplement 2A and B), otherwise the protomers are superimposable. All four EccC3 transmembrane helices were modeled at 6 Å resolution through a combination of homology modeling and molecular dynamics. In protomer i, transmembrane helix 2 forms lipid mediated hydrophobic interactions with the transmembrane helix of EccB3 in protomer i, and transmembrane helix 1 interacts with transmembrane helix 2 of EccC3 in protomer ii. Transmembrane helix 1 of EccC3 in protomer ii is shifted relative to the protomer i conformation and does not directly interact with other proteins.

### The EccC3 motor domains are flexible and asymmetric across the dimer

The motor domains containing the EccC3 ATPase 1, 2 and 3 hang below the DUF domain in the flexible lower cytoplasmic region. They were resolved at a lower resolution than the upper cytoplasmic domain, but they are clearly asymmetric between protomers i and ii (Figure 4A). Although the EccC3 ATPase 1 domains in both protomers are in a similar location relative to the DUF, the ATPase 2 and 3 domains do not superimpose across protomers even at low resolution (Figure 4—figure supplement 2C) suggesting significant asymmetry between these domains. In protomer i, a homology model based on existing EccC structures fits well into the density; however in protomer ii, the interface between ATPase 1 and 2 is broken relative to the crystal structure with ATPase 2 and ATPase 3 rotated away from the crystal structure interface.

### EccB3 extends into the periplasm and stabilizes dimer formation

The ESX-3 dimer is stabilized by cross-protomer interactions formed by the two EccB3 proteins. EccB3 begins in the cytoplasm with a flexible N-terminal tail leading into a linker helix, followed by a single-pass transmembrane helix, and an extended periplasmic domain (Figure 5A and B, Figure 5—figure supplement 1A and B). The N-terminal tail of EccB3 from protomer i forms extensive cross-protomer contacts with EccB3, EccC3, EccD3-bent and EccD3-extended from protomer ii (Figure 5C, Supplementary file 3). The linker helix of EccB3 forms further protein-protein interactions with EccC3 and EccD3-bent. The transmembrane helix of EccB3 interacts with transmembrane helix 11 of EccD3-extended. Two hydrophobic tails consistent with a lipid or detergent molecules link the transmembrane helix of EccB3 to transmembrane helix 2 of EccC3 (Figure 5D). The two EccB3 periplasmic domains share a large interaction interface across the protomers further stabilizing dimerization. Homology models of two EccB3 proteins can be docked into the periplasmic domain (Figure 5—figure supplement 1C); however, this region is not resolved sufficiently to identify specific interactions. The majority of cross-protomer interactions involve EccB3, suggesting the periplasmic domain is essential for oligomerization.

![Figure 5.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig5-v2.jpg)

**Figure 5.:** (A) EccB3 (pink) in the context of the overall ESX-3 dimer (gray transparency). EccB3 has a single-pass transmembrane domain which extends into a large periplasmic domain which was resolved at 5.8 Å resolution. (B) Atomic models of the EccB3 cytoplasmic and transmembrane domains, amino acids 14–93 and 32–93. (C) The N-terminus of EccB3 forms extensive cross-protomer contacts with EccC3 (blue), EccD3-bent (yellow), and EccD3-extended (green). (D) An unsharpened map of the ESX-3 dimer reveals ordered densities consistent with lipids or detergent molecules mediating the interactions between the EccB3 transmembrane helix (marked with a pink dot) and the EccC3 transmembrane helices.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Fit between map and model in the linker helix, amino acids 34 to 54. (B) Fit between map and model in the transmembrane helix, amino acids 65 to 85. (C) Fit between homology models of the soluble domain of EccB3 and the periplasmic focused refinement map.

### A hexameric model of ESX-3

Previous reports have shown ESX-1 and ESX-5 form hexamers or higher order multimers (Beckham et al., 2017; Houben et al., 2012). We modeled a higher order oligomeric state of ESX-3 based on the low-resolution negative stain structure of ESX-5, which had C6 symmetry imposed during refinement (EMDB 3596). The ESX-3 translocon complex was modeled as a trimer of dimers by low pass filtering the density to 6 Å and docking into the ESX-5 negative stain map (Figure 6—figure supplement 1A). The model of the ESX-3 dimer transmembrane and upper cytoplasmic regions, including the EccC3 transmembrane helices modeled to 6 Å resolution, was fitted into the trimerically positioned ESX-3 density maps (Figure 6—figure supplement 1B). The angle between protomers in the trimer of dimers model alternates between 72° (the angle between protomers i and ii in the ESX-3 dimer map) and 48° and contains both experimentally observed conformations of EccC3. The complete model of the ESX-3 translocon complex was docked into the ESX-5 negative stain map in the same manner revealing major clashes between the low resolution periplasmic and motor domains in a hexameric form (Figure 6—figure supplement 1C). Accommodation of a hexameric complex would require extensive rearrangement of both EccC3 and EccB3.

## Discussion

The ESX-3 structure presented here is purified without the addition of substrates or nucleotide. It is therefore likely to be in a conformation representing the end of the translocation cycle, awaiting either the direct binding of substrates, the binding of nucleotide or both, to reset a substrate-binding competent state. By fitting our dimer structure into a prior low resolution envelope we suggest a model of the oligomeric state of the complex, in close agreement with Famelis et al. However, even allowing for major rearrangements in the more flexible regions of EccC3 and EccB3, a model built by the static trimerization of the experimentally determined dimer structure cannot itself explain the mechanism of action of ESX-3 secretion. The existence of an R-finger catalytic site for ATPase 1 of EccC3 (Rosenberg et al., 2015) requires the R-finger of one protomer to insert into the active site of another protomer. Given the ~65 Å distance we observe between ATPase 1 domains, the completion and activation of the catalytic site of ATPase 1 by an R-finger will necessitate an extremely large rearrangement of the position of the ATPase domains. How might this rearrangement occur? We propose movements in the highly flexible EccD3 linker lead to the release of EccE3 and EccC3 from their rigid positions, thus allowing for a rearrangement of the ATPase domains into an active conformation (Figure 6).

![Figure 6.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig6-v2.jpg)

**Figure 6.:** ATPase activity entails, at a minimum, oligomerization of ATPase 1 to bring the R-finger (R) into proximity of the catalytic site, marked by the Walker A motif (WA). This requires at least 65 Å of movement from the position seen in the structure. (A) The first model of ESX substrate secretion involves trimerization of the ESX-3 dimer followed by multimerization of the EccC ATPase domains into a stack of one to four rings of ATPases (B) The second model shown through the function of a single protomer of the ESX-3 complex. Substrates are selected by interaction with ATPase 3 of EccC and transported via the upper cytoplasmic region to the EccD cavity for secretion.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/52983/elife-52983-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Fit of three copies of the transmembrane and upper cytoplasmic regions of the ESX-3 translocon complex into the ESX-5 hexameric structure (EMDB 3596). The ESX-3 translocon complex was filtered to 6 Å resolution to permit easy visualization of the EccC3 transmembrane helices. (B) The model of the ESX-3 translocon complex for the full transmembrane and upper cytoplasmic domains (including homology models of the EccC3 transmembrane helices accurate to 6 Å resolution) colored by protein. (C) The full model of the ESX-3 translocon complex including homology models for all three EccC3 ATPase domains and the periplasmic domain of EccB3 docked into the ESX-5 negative stain map. Red represents areas were atoms clash substantially.

Once EccC3 assembles into an oligomeric state, the substrate proteins will need to translocate through the inner membrane. We have considered two models for how pore formation and transit might occur: 1) through a pore created by the oligomerization of EccC3 and EccB3 or 2) through the large cavity created by the dimerization of EccD3. In the first model (Figure 6A), the resting state of an ESX translocon complex is a hexamer, with disordered EccC3 ATPase domains free in the cytosol, stabilized by interactions with proteins not seen in the structures presented here (van Winden et al., 2016). It is possible the rare multi-dimer oligomeric state we see in the void volume, and also seen by Famelis et al., represents this state. In a hexamer model, the center of the multimer is formed by the transmembrane helices of EccC3 and EccB3, which create a cavity that could serve as a pore for translocation of substrates. These transmembrane helices are largely hydrophobic and do not contain obvious residues that would allow for the conductance of hydrated substrates. Thus the production of a protein transit channel would require either a large, conformational change in the transmembrane helices, likely facilitated by movements in the cytoplasmic domains of EccC3, EccD3 and EccE3, or a novel mechanism of action for transit through the central pore.

A hexameric pore created by EccC3 agrees well with the documented mechanism of action for motor ATPases in the additional strand catalytic E (ASCE) division of P-loop NTPases (Erzberger and Berger, 2006), which includes EccC3. A hexameric pore also agrees with the proposed mechanism of action for other bacterial secretion systems, such as the Type IV secretion system VirD4 coupling protein (Gomis-Rüth et al., 2001; Hormaeche et al., 2002), which is related evolutionarily to EccC3 (Iyer et al., 2004). The hexamer model is thus firmly grounded in the motor ATPase and bacterial secretion systems literature, although the oligomeric state of VirD4 has recently been called into question (Redzej et al., 2017) and remains controversial (Llosa and Alkorta, 2017).

In a second, more speculative model, EccD3 dimers form a channel for translocation of substrates (Figure 6B). The large cavity found in the EccD3 dimer is striking and by structural homology, is unlike any other membrane protein in the Protein Data Bank. In our density maps, the EccD3 dimer cavity appears capped on the periplasmic side by a dense layer of lipids. In contrast, on the cytoplasmic side the cavity does not exhibit bound lipids due to the polar residues lining the lower half of the cavity. The large cavity is of sufficient diameter to transit a folded EsxG/H dimer, however given the strong hydrophobicity of the cavity the mechanism would not be mediated by water and would require a novel mechanism of secretion that has not been seen in other bacterial secretion systems. It is also possible that the cavity exists to transit a non-protein substrate such as a specific mycobacterial lipid. The ability to transport non-protein substrates could resolve some of the mysteries that remain about the relationships between ESX systems, cell wall stability, lipid content, and nutrient acquisition (Barczak et al., 2017; Bosserman and Champion, 2017; Siegrist et al., 2014; Tufariello et al., 2016).

As each protomer contains an EccD3 cavity, the second model, proposing translocation through EccD3, does not require hexamerization. However, this model is also not incompatible with hexamerization, which would not block a substrate path through EccD3. Further, the role of the hexamer may not be to form a central channel for substrate transit. Rather, hexamerization could serve some other purpose. For example, it may tether functional dimers together, facilitate localization, or increase local concentration and allosteric control of enzymatic activity (Kuriyan and Eisenberg, 2007).

Although the ESX-3 structure presented here allows for mechanistic hypotheses about the transit of substrates across the inner-membrane, it does not provide sufficient information to allow for a structural model of transit across the outer mycomembrane. The EccB3 periplasmic domain (Wagner et al., 2016) has been found to have similarity to the peptidoglycan binding phage protein PlyCB, which forms a ring inside the bacterial cell wall facilitating phage entrance into the cell. A hypothesis is that EccB3 is anchored to a larger outer membrane complex, but the purification conditions we have employed remove proteins required for its stabilization.

The description of ESX-3 presented here agrees in both protein composition and structure with the work recently published by Famelis et al. Given the high sequence conservation among the ESX systems in mycobacteria and related actinobacteria, these structures likely represent an excellent framework for the structural modeling of the other ESX systems. Together, these structures provide a wealth of information about protein-protein interaction interfaces and ESX complex architecture, which can be used to guide structure-based drug design and to generate hypotheses for further mechanistic investigations.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional Information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Biological sample Mycobacterium smegmatis</td>
      <td>mc(2)155</td>
      <td>ATCC</td>
      <td>700084</td>
      <td>Wild type strain</td>
    </tr>
    <tr>
      <td>Biological sample Mycobacterium smegmatis</td>
      <td>mc(2)155 with ideR::mγδ200 (KanR)</td>
      <td>Dussurget et al., 1996, Provided by GM Rodriguez</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Biological sample Mycobacterium smegmatis</td>
      <td>mc(2)155, MSMEG_0626-3C-EGFP</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Biological sample Mycobacterium smegmatis</td>
      <td>mc(2)155 with ideR::mγδ200 (KanR), MSMEG_0626-3C-EGFP</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pKM444</td>
      <td>Murphy et al., 2018</td>
      <td>Addgene Plasmid #108319</td>
      <td>Plasmid encoding for Che9c phage RecT and Bxb1 phage Integrase</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pKM444 - zeo</td>
      <td>This paper</td>
      <td></td>
      <td>Addition of zeocin resistance cassette to pKM444 plasmid</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pKM468-3C-EGFP</td>
      <td>This paper</td>
      <td></td>
      <td>Modified ORBIT tagging plasmid</td>
    </tr>
    <tr>
      <td>Sequenced-based reagent</td>
      <td>ORBIT targeting oligonucleotide</td>
      <td>This paper</td>
      <td>Oligo</td>
      <td>5’ TGTGCGTTCCACTGGTTCCCCGGCAACCACCTGCTGCACGTGAGCCAGCCGGACTACCTAGGTTTGTACCGTACACCACTGAGACCGCGGTGGTTGACCAGACAAACCCGCCGGATGACCCGCTTCCTGCGCGGCTTCATGTTCGACTGAACCCTTCACCGAGGTCCG 3’</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GFP stabilized antibody preparation</td>
      <td>Roche</td>
      <td>Cat. #: 11814460001</td>
      <td>Dilution 1:10000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-mouse IgG HRP-conjugated antibody</td>
      <td>R&amp;D Systems</td>
      <td>Cat. #: HAF007</td>
      <td>Dilution 1:5000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-rabbit IgG antibody HRP</td>
      <td>GenScript</td>
      <td>Cat. #: A00098</td>
      <td>Dilution 1:5000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit anti-GroEL</td>
      <td>Sigma-Aldrich</td>
      <td>Cat. #: G6532-.5ML</td>
      <td>Dilution 1:5000</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Human Rhinovirus (HRV) 3C Protease</td>
      <td>Thermo Scientific Pierce</td>
      <td>Cat. #: 88946</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Superose 6 Increase 10/300 GL</td>
      <td>GE Healthcare</td>
      <td>Cat. #: 29091596</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, detergent</td>
      <td>DDM, n-Dodecyl-β-D-Maltopyranoside</td>
      <td>Inalco</td>
      <td>Cat. #: 1758-1350</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, detergent</td>
      <td>GDN, glyco-diosgenin</td>
      <td>Anatrace</td>
      <td>Cat. #: GDN101</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>NativePAGE 3-12% Bis-Tris Protein Gels, 1.0 mm, 10-well</td>
      <td>ThermoFisher Scientific</td>
      <td>Cat. #: BN1001BOX</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Pierce Silver Stain Kit</td>
      <td>Pierce</td>
      <td>Cat. #: PI24612</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SerialEM</td>
      <td>Mastronarde, 2005</td>
      <td></td>
      <td>https://bio3d.colorado.edu/SerialEM/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MotionCor2</td>
      <td>Zheng et al., 2017</td>
      <td></td>
      <td>http://msg.ucsf.edu/em/software/motioncor2.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CTFfind4</td>
      <td>Rohou and Grigorieff, 2015</td>
      <td></td>
      <td>https://grigoriefflab.umassmed.edu/ctffind4</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RELION</td>
      <td>Scheres, 2012</td>
      <td></td>
      <td>cam.ac.uk/relion/index.php/Download_%26_install</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>cisTEM</td>
      <td>Grant et al., 2018</td>
      <td></td>
      <td>https://cistem.org/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>cryosparc</td>
      <td>Punjani et al., 2017</td>
      <td></td>
      <td>https://cryosparc.com/docs/reference/install/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>pyem</td>
      <td>Asarnow et al., 2019</td>
      <td></td>
      <td>https://github.com/asarnow/pyem</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>coot</td>
      <td>Emsley et al., 2010</td>
      <td></td>
      <td>https://www2.mrc-lmb.cam.</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>raptorX</td>
      <td>Källberg et al., 2012</td>
      <td></td>
      <td>http://raptorx.uchicago.edu/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>phenix real space refine</td>
      <td>Afonine et al., 2018</td>
      <td></td>
      <td>https://www.phenix-online.</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MDFF</td>
      <td>Trabuco et al., 2009</td>
      <td></td>
      <td>org/documentation/reference/refinement.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>namdinator</td>
      <td>Kidmose et al., 2019</td>
      <td></td>
      <td>https://namdinator.au.dk/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>pisa</td>
      <td>Krissinel, 2015</td>
      <td></td>
      <td>http://www.ccp4.ac.uk/pisa/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>chimera</td>
      <td>Pettersen et al., 2004</td>
      <td></td>
      <td>https://www.cgl.ucsf.edu/chimera/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>chimeraX</td>
      <td>Goddard et al., 2018</td>
      <td></td>
      <td>https://www.cgl.ucsf.edu/chimerax/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DALI</td>
      <td>Holm and Laakso, 2016</td>
      <td></td>
      <td>http://ekhidna2.biocenter.helsinki.fi/dali/</td>
    </tr>
  </tbody>
</table>

### Strain construction

Mycobacteria smegmatis mc(2)155 (wild type) and ΔideR cells were chromosomally tagged using the ORBIT protocol (Figure 1—figure supplement 1). For wild type cells, the integrase and annealase expressing plasmid was pKM444. For recombineering in the ΔideR strain, which already contained a kanamycin resistance marker, we created a modified pKM444 plasmid with a zeocin resistance cassette inserted at the EcoIV restriction site. The tagging plasmid was pKM468 with a 3C protease cleavage site added before the EGFP tag. The targeting oligo had the sequence: 5’ TGTGCGTTCCACTGGTTCCCCGGCAACCACCTGCTGCACGTGAGCCAGCCGGACTACCTAGGTTTGTACCGTACACCACTGAGACCGCGGTGGTTGACCAGACAAACCCGCCGGATGACCCGCTTCCTGCGCGGCTTCATGTTCGACTGAACCCTTCACCGAGGTCCG 3’. M. smegmatis cells containing pKM444 were grown in an overnight liquid culture and induced for annealase and integrase expression. Cells were prepared for electroporation and electroporated with the targeting oligo and tagging plasmid. The transformed M. smegmatis were plated on hygromycin (wild type) or hygromycin and kanamycin (ΔideR) containing 7H9 plates and incubated at 37° C for 3 days. Colonies were verified for insertion of the tagging plasmid into the chromosome by PCR.

### Western blotting

100 mL of EccE3 tagged wild type and ΔideR knock out cells were grown overnight to an OD600 of 1.0–1.2. Cells were pelleted and resuspended in 1 mL of buffer (50 mM Tris-HCl pH 8.0, 150 mM NaCl, 1% DDM) and sonicated for 30 s. Cell lysates were run on a 4–20% SDS-PAGE gel (GenScript) and transferred to PVDF membrane (BioRad) using a BioRad Trans-Blot Turbo Transfer System. The blot was washed with PBS and blocked in a 5% milk/PBS-T solution for 1 hr. The blot was incubated with mouse anti-GFP monoclonal antibody (Roche) overnight. After rinsing with PBS-T, the blot was incubated with anti-mouse IgG HRP-conjugated antibody (R&D Systems) for 2 hr. After activation (Amersham) the blot was imaged on a BioRad ChemiDoc. The blot was stripped with stripping buffer (ThermoFisher Scientific) as per the manufacture's instructions, and incubated overnight with rabbit anti-GroEL monoclonal antibody (Sigma-Aldrich). The blot was incubated with goat anti-rabbit IgG antibody HRP (GenScript) for 2 hr, activated (Amersham), and imaged on a BioRad ChemiDoc.

### Protein purification

Purification for high resolution structural determination: M. smegmatis was grown in 6 L of 7H9 supplemented with 0.05% Tween 80 and 20 µg/mL kanamycin to an OD600 of ~0.8. After harvest, cells were washed three times with PBS and frozen in liquid nitrogen before lysis with a cryogenic grinder (SPEX SamplePrep). 24.9 g of powdered cell material was resuspended by adding 56.3 mL 50 mM Tris-HCl pH 8.0, 150 mM NaCl, 1% DDM supplemented with 1X protease inhibitor cocktail (SigmaFast) and 224 units Benzonase endonuclease. The suspension was stirred for 120 min at 4°C. After centrifugation for 30 min at 98,000 g, the supernatant was incubated with 1.4 mL anti-GFP-nanobody resin for 110 min at 4°C. The resin was transferred to a column and washed sequentially with 28 ml of wash buffer (50 mM Tris-HCl pH 8.0, 150 mM NaCl and 0.1% GDN), 14 mL of high salt wash buffer (50 mM Tris-HCl pH 8.0, 400 mM NaCl, and 0.1% GDN), and 14 mL of wash buffer (50 mM Tris-HCl pH 8.0, 150 mM NaCl, and 0.1% GDN). To cleave off the purification tag, the resin was incubated o/n at 4°C with 70 units Pierce HRV 3C protease (Thermo Scientific Pierce) in 2.8 mL wash buffer supplemented with 0.2 mM DTT. This resin was sedimented by gentle centrifugation (300 x g for 3 min), the supernatant collected, and the resin was subsequently washed with 1.4 mL wash buffer. The supernatant and wash fraction were combined and concentrated using an Amicon Ultra-4 centrifugal filter unit with a 100 kDa molecular weight cut-off. The sample was centrifuged at 16,000 g before injection on a Superose 6 10/300 column equilibrated in 50 mM Tris-HCl pH 8.0, 150 mM NaCl and 0.021% GDN. Peak fractions were concentrated using a 0.5 mL centrifugal filter unit (Amicon, 100 kDa cut-off) to an A280 of 5.52 by Nanodrop reading in about ~30 µL . Purification completed for examination of the void fractions was similar except: volumes were scaled for a powder weight of 21.1 g. and the high salt wash was omitted.

### Blue-Native polyacrylamide gel electrophoresis (BN-PAGE)

BN-PAGE experiments were carried out using the Invitrogen NativePAGE Novex Bis-Tris Gel system as recommended by the manufacturer. Samples were prepared in a total volume of 10 µL using 0.5 µL 5% G-250 sample additive. Electrophoresis was performed at a constant voltage of 105-120 V for 2-3.5 hr at 4°C. The gel was fixed and stained using the Pierce silver stain kit.

### Cryo-EM – data acquisition

Samples were frozen for cryo-EM. Quantifoil R1.2/1.3, 400 mesh, copper grids were glow discharged using a Solarus plasma cleaner (Gatan) with an H2/O2 mixture for 30 s. 2 µL of sample were applied per grid and the grids were plunged into liquid ethane using a FEI Vitrobot Mark IV.

Initially, samples were screened, and test data sets were collected on a FEI Talos Arctica 200kV microscope equipped with a Gatan K2 Summit detector. For the initial screen of freezing conditions, 2499 movies were collected at a magnification of 36,000 with a pixel size of 1.14, and a defocus range of −1.5 to −2.5 µm, an exposure time of 9 s, and a dose rate of 7 electrons/Å2/second (Table 1). Data collection for the final structure presented in the main text was collected on a FEI Titan Krios at 300kV with a Gatan K2 Summit detector. Two imaging sessions were used. In the first imaging session, 2705 movies were collected at a magnification of 29,000 with a pixel size of 0.82, and a defocus of −0.4 to −1.2 µm, an exposure time of 10 s to collect 100 total frames, and a dose rate of 8 electrons/Å2/second (Table 1). In the second imaging session, data was collected on the same microscope with the same detector, 4632 movies were collected at a magnification of 29,000 with a pixel size of 0.82, and a defocus range of −0.6 to −1.4 µm, an exposure time of 10 s to collect 80 total frames, and a dose rate of 6.7 electrons/Å2/second. Data used to analyze the void, plateau, and peak regions of the SEC profile were collected on a FEI Talos Arctica at 200kV with a Gatan K3 detector. All micrographs were collected at a magnification of 28,000 with a pixel size of 0.9, and a defocus range of −1.5 to −2.5 µm, an exposure time of 11.7 s to collect 117 total frames at a total dose of 58 electrons/ Å2. For the void region, 1215 micrographs were collected.

### Cryo-EM – data processing

For all data, movies were motion corrected using MotionCor2 (Zheng et al., 2017) and CTF correction was performed using CTFfind4 (Rohou and Grigorieff, 2015). For the Arctica dataset, particles were picked using a gaussian blob in either RELION (Zivanov et al., 2018) or cisTEM (Grant et al., 2018) and initial 2D classification was performed to remove obvious artifactual particles. Initially, a shotgun approach was taken to generate several initial models using RELION, cisTEM, and cryosparc (Punjani et al., 2017). Once an initial model which contained realistic low-resolution features was generated, a user defined descent gradient was performed to improve the model with the goal of achieving accurate secondary structure features. First, all particles selected during 2D classification were refined in 3D against the randomly generated initial model. Second, a round of 3D classification with four classes and default RELION settings was performed and the best class selected. Third, the best class was refined as a single class in 3D classification with increasing Tau2_Fudge and decreasing search angle size. The resulting EM density map had clear transmembrane helix densities and was used as the model for a new 3D reconstruction. This reconstruction was used to back project models for reference-based particle picking in RELION. Two rounds of 2D classification were performed and the best classes selected. One round of 3D classification was performed using the Tau2_Fudge value optimized during the previous run through (T = 12) and the best class selected. A final 3D reconstruction of the Arctica data set yielded a map of about 4.7 Å resolution (Figure 1—figure supplement 4).

After motion correction and CTF determination, the final Titan Krios dataset was processed entirely using RELION. Particles were picked using a gaussian blob, and extracted as 4x binned particles. Two rounds of initial 2D classification were performed with T = 3 on the binned particles and obvious artifactual particles were removed. The final reconstruction from the Arctica dataset was used as the initial model for a 3D reconstruction of the binned particles. 3D classification with four classes and the previously optimized Tau2_Fudge value, T = 12, was performed on the binned particles. The two best classes were selected and re-extracted without binning. A 3D reconstruction was performed. A mask was created for the high-resolution region of the reconstruction and 3D classification without image alignment was performed focused on this region. The best class was selected and the subsequent 4.0 Å reconstruction is the consensus structure for the entire complex (Figure 1—figure supplement 5). Focused classification of each protomer, the periplasmic EccB region, and the ATPase 1, 2, and 3 domains of EccC were performed. To perform focused classification, the center of mass of the region of interest was determined using chimera (Pettersen et al., 2004). Particles were recentered on this area and reextracted. Masks for the region of interest were generated and 3D classification without image alignment was performed. The best class was selected and used for a focused 3D reconstruction without image alignment of the region of interest. A reconstruction was generated and density outside of the region of interest was subtracted. A final reconstruction of the masked and density subtracted particles was then performed. This procedure improved the resolution of the protomer i to 3.75 Å and protomer ii 3.83 Å, 5.8 Å resolution for the EccB3 periplasmic domain, and ~7 Å resolution for the EccC3 lower cytoplasmic region.

To generate the symmetry expanded protomers based on non-point group symmetry (also known as non-crystallographic symmetry or NCS), a transformation matrix between the two protomers was calculated using chimera. Particles were then transformed and aligned using the subparticles.py and star.py utilities in pyem (Asarnow et al., 2019) resulting in a particle stack with twice as many particles as the input file, each focused on protomer i or protomer ii. Density subtraction was performed to remove density outside of the symmetry expanded protomer, and focused classification and refinement were performed as described above. This procedure improved the resolution of the symmetry expanded protomer to 3.69 Å resolution.

### Atomic model building

The cytoplasmic domain from the crystal structure of EccD1 (PDB 4KV2) was docked into the cytoplasmic domains of the two EccD3 molecules and the sequence was mutated. The remaining transmembrane domains of EccD3 and the residues 14–93 of EccB3 were built de novo in Coot (Emsley et al., 2010) using baton building. The alpha helices of EccE3 and EccC3 were initially modeled using the RaptorX (Källberg et al., 2012) homology server. The loops and strands of EccE3 and EccC3 were built in Coot using baton building. All models were subsequently refined individually, as a symmetry expanded protomer, left and right protomers, and as the full model using phenix real space refine (Afonine et al., 2018), Coot, and the MDFF (Trabuco et al., 2009) server, Namdinator (Kidmose et al., 2019; Supplementary file 1).

### Low resolution modeling

The left and right protomer map, periplasmic focused refined map, and lower cytoplasmic focused refined map were all docked into the consensus map and added together using chimera. The combined map was filtered to 10 Å resolution to match the lowest resolution component. Homology models for amino acids 94–516 of EccB3, the transmembrane helixes of EccC3, and 404–1268 of EccC3 were generated using RaptorX. These models were fit into the combined map density using the fit map to model utility in Chimera. The full model was refined using phenix.real_space_refine.

### Model interpretation and display

Buried surface area between subunits was calculated by PISA (Krissinel, 2015). Atomic models for individual proteins were compared against the PDB using the DALI server (Holm and Laakso, 2016). Chimera and ChimeraX (Goddard et al., 2018) were used to display maps and models for figure creation. Consurf (Ashkenazy et al., 2016) was used to produce multisequence alignments and to color structural models by homology.
