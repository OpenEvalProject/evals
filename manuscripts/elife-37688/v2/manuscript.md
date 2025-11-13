# Germline VRC01 antibody recognition of a modified clade C HIV-1 envelope trimer and a glycosylated HIV-1 gp120 core

## Authors

- Andrew J Borst<sup>1</sup> ([ORCID: 0000-0003-4297-7824](https://orcid.org/0000-0003-4297-7824))
- Connor E Weidle<sup>2</sup>
- Matthew D Gray<sup>2</sup>
- Brandon Frenz<sup>1</sup>
- Joost Snijder<sup>1</sup>
- M Gordon Joyce<sup>3</sup>
- Ivelin S Georgiev<sup>3</sup>
- Guillaume BE Stewart-Jones<sup>3</sup>
- Peter D Kwong<sup>3</sup>
- Andrew T McGuire<sup>2</sup>
- Frank DiMaio<sup>1</sup> ([ORCID: 0000-0002-7524-8938](https://orcid.org/0000-0002-7524-8938))
- Leonidas Stamatatos<sup>2</sup> †
- Marie Pancera<sup>2</sup> †
- David Veesler<sup>1</sup> ([ORCID: 0000-0002-6019-8675](https://orcid.org/0000-0002-6019-8675)) †

### Affiliations

1. Department of Biochemistry University of Washington Seattle United States
2. Vaccine and Infectious Disease Division Fred Hutchinson Cancer Research Center Seattle United States
3. Vaccine Research Center National Institute of Allergy and Infectious Diseases, National Institutes of Health Bethesda United States
4. Department of Global Health University of Washington Seattle United States

† Corresponding author

## Abstract

VRC01 broadly neutralizing antibodies (bnAbs) target the CD4-binding site (CD4BS) of the human immunodeficiency virus-1 (HIV-1) envelope glycoprotein (Env). Unlike mature antibodies, corresponding VRC01 germline precursors poorly bind to Env. Immunogen design has mostly relied on glycan removal from trimeric Env constructs and has had limited success in eliciting mature VRC01 bnAbs. To better understand elicitation of such bnAbs, we characterized the inferred germline precursor of VRC01 in complex with a modified trimeric 426c Env by cryo-electron microscopy and a 426c gp120 core by X-ray crystallography, biolayer interferometry, immunoprecipitation, and glycoproteomics. Our results show VRC01 germline antibodies interacted with a wild-type 426c core lacking variable loops 1–3 in the presence and absence of a glycan at position Asn276, with the latter form binding with higher affinity than the former. Interactions in the presence of an Asn276 oligosaccharide could be enhanced upon carbohydrate shortening, which should be considered for immunogen design.

## Introduction

Despite the tremendous impact of HIV-1 on human health, no efficacious HIV-1 vaccine currently exists. The HIV-1 envelope (Env) glycoprotein is a class-I fusion protein responsible for host attachment and fusion of the viral and cellular membranes (Dalgleish et al., 1984). Following expression, Env trimerizes and undergoes furin-mediated cleavage to yield non-covalent gp120-gp41 pre-fusion trimers anchored in the viral membrane (Haim et al., 2013). As the sole target of neutralizing antibodies, Env is the focus of intense interest for current vaccine design initiatives. However, HIV-1 Env relies on multiple mechanisms of immune evasion – including dense glycosylation, sequence variation, conformational masking, and presentation of decoy epitopes (Burton and Mascola, 2015; Cuevas et al., 2015; Jardine et al., 2015; Kwong et al., 2002; Wei et al., 2003; Zhou et al., 2017). For these reasons, development of an Env-based vaccine capable of eliciting broadly neutralizing antibodies (bnAbs) has proven challenging.

The VRC01-class of bnAbs is of particular interest for HIV-1 vaccine development due to the exceptional potency and breadth of several of its well-characterized members (Huang et al., 2016; Zhou et al., 2015). These bnAbs derive from the VH1-2 variable heavy chain gene (Scheid et al., 2011; Wu et al., 2011), have been isolated from multiple HIV-1-infected patients (Zhou et al., 2013), and putative non-mutated precursors have been identified in naïve individuals (Jardine et al., 2016a). VRC01-class bnAbs are characterized by an unusually short five amino-acid light chain complementary-determining region (CDR) L3 loop (Zhou et al., 2015) and much higher levels of somatic hyper-mutation than antibodies targeting other pathogens (Wu et al., 2015). They bind the CD4-binding site (CD4BS) in a way reminiscent of the interactions formed with the viral receptor CD4, making extensive CDRH2-mediated contacts while also exhibiting multiple amino acid alterations in the CDRL1 loop relative to germline precursors (Wu et al., 2015; Zhou et al., 2013). Although N-linked glycosylation sites (NLGSs) that surround the CD4BS sterically limit recognition by bnAbs (Zhou et al., 2017), particularly those present at position Asn276 in Loop D and along the V5 loop, mature VRC01 bnAbs overcome this barrier and potently neutralize numerous HIV-1 viral clades (Zhou et al., 2017; Huang et al., 2016; Stewart-Jones et al., 2016; Wu et al., 2015). In contrast, the inferred germline precursors of VRC01-class bnAbs lack detectable binding to trimeric Env constructs harboring glycans at these locations (Jardine et al., 2013; McGuire et al., 2016; McGuire et al., 2013; Medina-Ramírez et al., 2017b; Stamatatos et al., 2017).

Whereas most recombinant trimeric Env antigens do not bind germline precursors of VRC01-class bnAbs, a few recently designed constructs have been shown to bind and activate this specific class of B cell receptors (BCRs) (Jardine et al., 2013; McGuire et al., 2016; McGuire et al., 2013; Medina-Ramírez et al., 2017a). We previously engineered a trimeric HIV-1 Env protein able to bind most VRC01-class precursors (McGuire et al., 2013). This construct was a trimeric gp140 protein derived from the clade C 426c virus and lacked variable loops 1, 2, and 3, along with the putative NLGSs at positions Asn276 (loop D), Asn460, and Asn463 (V5 loop) (McGuire et al., 2016). Other constructs have also been engineered to engage the inferred precursors of VRC01-class bnAbs, all of which harbored mutations eliminating the NLGSs in loop D (at position Asn276) and in the V5 loop (Briney et al., 2016; Jardine et al., 2013; McGuire et al., 2016; McGuire et al., 2013; Medina-Ramírez et al., 2017a; Tian et al., 2016). Additionally, a gp120 core derived from the 01dG5 clade virus, which naturally lacks a glycan at position Asn276, was also shown to engage the inferred germline precursor of the VRC01 antibody (VRC01GL) (Wu et al., 2015). Although such glycan-depleted ‘germline-targeting’ immunogens activate B cells expressing germline VRC01-class BCRs in vivo (Briney et al., 2016; Dosenovic et al., 2015; Tian et al., 2016), they largely fail to elicit mature antibodies capable of bypassing the restrictions imposed by the glycan at position Asn276 (Zhou et al., 2017). However, a recent study demonstrated the successful elicitation of CD4BS-targeted antibodies, distinct from the VRC01 lineage, upon immunization of rabbits with an engineered clade C Env trimer (Dubrovskaya et al., 2017).

To better understand the potential avenues of elicitation of VRC01-class bnAbs, we structurally characterized complexes between VRC01GL and two clade C Env constructs using a combination of cryo-electron microscopy (cryoEM) and X-ray crystallography. One of the constructs is a soluble trimeric 426c SOSIP with three NLGSs removed at positions Asn276, Asn460, and Asn463, and is based on our prior work (McGuire et al., 2016; McGuire et al., 2013). The second construct is a monomeric 426c core containing all wild-type NLGSs (including those at positions Asn276, Asn460, and Asn463), but lacks variable loops 1, 2, and 3. The 426c strain naturally lacks NLGSs surrounding the CD4BS at positions Asn234 and Asn362(363), which are present in other clades. Our structural analysis revealed that the absence of these glycans leads to a reduction of local oligosaccharide density in the vicinity of the NLGS at position Asn276. Integrating this data with biolayer interferometry (BLI) assays and glycoproteomics, we demonstrate here that VRC01GL could bind to a 426c core construct in the presence of all naturally occurring NLGSs surrounding the CD4BS, including the NLGS at position Asn276 and with its associated glycan. We also show the affinity of VRC01GL for the 426c core could be modulated by altering protein expression conditions to enrich for longer glycans, and also by shortening glycans via endoglycosidase treatment. These results suggest that priming of VRC01-class bnAbs may be possible using an HIV-1 gp120 derivative containing a glycan at position Asn276. Consequently, future epitope-based vaccine design strategies utilizing a 426c core preserving all NLGSs may be a promising route for guiding elicitation of VRC01-class bnAbs.

## Results

### CryoEM structure of VRC01GL in complex with a modified 426c HIV-1 SOSIP glycoprotein trimer

Based on the known enhanced ability of VRC01GL (and related germline antibodies) to bind 426c constructs lacking putative NLGSs at positions Asn276, Asn460, and Asn463 (McGuire et al., 2013), and the lack of detectable binding to 426c DS-SOSIP (Figure 1A), we engineered a modified 426c DS-SOSIP trimer recapitulating the aforementioned glycan depletion mutations for structural analysis. This construct harbors the S278A, T462A and T465A mutations, abolishing the corresponding NLGSs and enabling binding to VRC01GL (Figure 1B, Figure 1—figure supplement 1). It also contains the SOSIP (Sanders et al., 2002) and the 201C-433C (DS) mutations (Kwon et al., 2015) and is a chimera of 426c gp120 and BG505 gp41 (Joyce et al., 2017). This glycan-depleted protein construct is henceforth referred to as 426c DS-SOSIP D3 (Figure 1—figure supplement 1). The VRC01GL construct comprises the germline VH gene reverted sequences of VH1-2*02, which includes CDRH1 and CDRH2 along with the mature CDRH3 of VRC01 and the germline VK3-11 with the mature CDRL3 of VRC01 (Figure 1—figure supplement 2). Initial complex formation was evaluated using negative-staining EM, which revealed sub-stoichiometric binding of VRC01GL Fab to 426c DS-SOSIP D3 (Figure 1—figure supplement 3A). The VRC01GL Fab appeared to have a much lower affinity for 426c DS-SOSIP D3, compared to the VRC01GL IgG (the latter bound with an apparent equilibrium dissociation constant of 43 nM (Figure 1B), neglecting the effect of avidity). We next attempted to enhance binding of VRC01GL Fab to 426c DS-SOSIP D3 by utilizing a mild glutaraldehyde cross-linking strategy. As expected, we observed significantly increased saturation of 426c DS-SOSIP D3 trimers by VRC01GL Fab, indicating covalent tethering following initial engagement of VRC01GL to the CD4BS was a suitable approach to enrich for and study VRC01GL-bound complexes (Figure 1—figure supplement 3A). We therefore engineered a disulfide bond between G459Cgp120 (426c DS-SOSIP D3†) and the VRC01GL heavy chain A60C (denoted as 426c DS-SOSIP D3†-VRC01GL) (Figure 1—figure supplement 1 and Figure 1—figure supplement 2). This strategy was previously employed to enhance binding of VRC01MAT to SOSIP trimers without altering interface contacts (Stewart-Jones et al., 2016). Using this method, we purified an enriched fraction of Fab-bound trimers and used this sample for structural characterization (Figure 1C, Figure 1—figure supplement 3A–D). This strategy led us to determine two cryoEM reconstructions of the 426c DS-SOSIP D3†-VRC01GL complex (Figure 1D–E, Figure 1—figure supplement 3E–H, Figure 1—figure supplement 4A–D, Figure 1—figure supplement 5): one with three bound Fabs at 3.8 Å resolution (Figure 1D, Table 1, Figure 1—figure supplement 3E, Figure 1—figure supplement 4A–B), and one with two bound Fabs at 4.8 Å resolution (Figure 1E, Figure 1—figure supplement 3H, Figure 1—figure supplement 4C–D).

![Figure 1.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig1-v2.jpg)

**Figure 1.:** (A–B) BLI binding data of immobilized VRC01GL IgGs binding to WT 426c DS-SOSIP (A) or 426c DS-SOSIP D3 trimers. The concentrations of 426c DS-SOSIP trimers injected are indicated on each panel. Fit curves are colored as black dotted lines. A KD could not be determined in (A) due to the weak responses observed. The vertical dotted lines indicate the transition between association and dissociation phases. (C) Size-exclusion chromatogram of the purified 426c DS-SOSIP D3†-VRC01GL complex used for cryoEM structure determination. The pooled fractions used for cryoEM are highlighted in light blue. (D) Two orthogonal views of the 3.8 Å cryoEM reconstruction sharpened with a B-factor of −250 Å2 whereas the glycan density is shown unsharpened. (E) Two orthogonal views of the asymmetric 4.8 Å reconstruction with two bound Fabs. (F) Surface representation of the 426c SOSIP trimer highlighting differences in glycosylation compared to the BG505 SOSIP. Glycans not present in 426c are colored light-gray and outlined. Glycans present in the 426c strain but removed by mutation from the 426c DS-SOSIP D3† construct are colored magenta and outlined. The gp120 surface buried at the interface with VRC01GL is indicated as a dotted outline and is colored yellow. (G) Comparison of the gp120 bridging sheet conformation when VRC01GL-class Fabs are bound to either 426c DS-SOSIP D3† trimer (Top-left) or a previously solved 426c gp120 core lacking selected NLGSs, such as the Asn276 NLGS (PDB: 5IGX) (Top-right). Comparisons of β20β21 loop conformations of each complex are shown below corresponding top panels. (H) Comparison of glycan density and position between VRC01GL-bound and VRC01GL-free protomers in the asymmetric cryoEM reconstruction shown in (E). (Top) Asn197 and Asn386 glycan density is stronger for protomers bound to VRC01GL Fab than for the gp120 protomer not bound to VRC01GL (Bottom). In panels D-H, gp120 protomers are shown in blue, gp41 in red, N-linked glycans in green and VRC01GL in dark and light yellow for the heavy and light chains, respectively.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** HIV-1 constructs derived from the 426c strain used in this study were subjected to multiple sequence alignment using Clustal Omega and rendered using ESPript (Gouet et al., 1999; Sievers and Higgins, 2014). Residues highlighted in red signify identical amino acids conserved across all aligned constructs. Similar residues are highlighted in bold and colored yellow.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** VRC01GL-class antibody and Fab constructs used in this study were subjected to multiple sequence alignment using Clustal Omega and rendered using ESPript (Gouet et al., 1999; Sievers and Higgins, 2014). Residues highlighted in red signify identical amino acids conserved across all aligned constructs. Similar residues are highlighted in bold and colored yellow.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Strategy implemented to increase the occupancy of VRC01GL Fab for structural studies. VRC01GL can engage 426c DS-SOSIP D3, but its low apparent affinity relative to VRC01GL IgG precludes saturation at the concentrations used for negative staining EM imaging (Left). Mild glutaraldehyde (GTA) crosslinking (0.25% GTA for 45 s followed by quenching with 1M Tris) increased VRC01GL saturation of 426c DS-SOSIP D3 (Middle). Engineering a disulfide bond between 426c DS-SOSIP D3 (G459Cgp120) and the heavy chain of VRC01GL (A60CHC) further increased gp120 saturation of the trimer (Right). (B) 3D reconstruction of negatively stained 426c DS-SOSIP D3†-VRC01GL. (C–D) Representative micrograph (E) and 2D class averages (F) of frozen-hydrated 426c DS-SOSIP D3†-VRC01GL. Scale bars represent 200 nm (E) or 200 Å (F). (E) Fourier shell correlation (FSC) curves of the 426c DS-SOSIP D3†-VRC01GL complex with three Fabs bound showing an estimated resolution of 3.8 Å. (F) Fourier shell correlation curves of the 426c DS-SOSIP D3†-VRC01GL complex with two Fabs bound showing an estimated resolution of 4.8 Å. The top and bottom horizontal dashed lines show the 0.5 and 0.143 cutoffs used for resolution estimates for map-to-model or gold-standard FSC, respectively. Both conventional FSC and FSC-part, as reported in Frealign, are shown.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** (A) Local resolution estimates of 426c DS-SOSIP D3† bound to three copies of VRC01GL-A60CHC as determined using ResMap (Kucukelbir et al., 2014). (B) Graphical plot depicting distribution of particle image orientations. (C) Local resolution estimates of 426c DS-SOSIP D3† bound to two copies of VRC01GL-A60CHC as determined using ResMap(Kucukelbir et al., 2014). (D) Graphical plot depicting distribution of particle image orientations.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** Tables highlighting gp120 residues and their associated buried surface area (BSA) which comprise the interface with VRC01-class antibodies, as determined by PISA. BSA values are colored light gray for values ranging between 0.1 and 10.0, light blue for values between 10.1 and 30.0, dark blue for values between 30.1 and 50.0, and red for values > 50.0 Å2. HC: heavy chain; LC: light chain.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** CryoEM density (green semi-transparent surface) and atomic model for glycans at positions Asn230, Asn197, Asn386 and Asn262 are shown.

**Table 1.**
 CryoEM data collection, refinement, and model validation statistics.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data Collection</td>
      <td></td>
    </tr>
    <tr>
      <td>No. of Micrographs</td>
      <td>1993</td>
    </tr>
    <tr>
      <td>No. of Particles</td>
      <td>134,443</td>
    </tr>
    <tr>
      <td>Pixel size, Å</td>
      <td>1.36</td>
    </tr>
    <tr>
      <td>Defocus range, μM</td>
      <td>2.0–3.5</td>
    </tr>
    <tr>
      <td>Voltage, kV</td>
      <td>300</td>
    </tr>
    <tr>
      <td>Dose Rate, counts/pix/sec</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Electron dose, e-/Å2</td>
      <td>43</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
    </tr>
    <tr>
      <td>Resolution, Å</td>
      <td>3.8</td>
    </tr>
    <tr>
      <td>Map-sharpening B factor, Å2</td>
      <td>−230</td>
    </tr>
    <tr>
      <td>Model validation (3 Fab structure)</td>
      <td></td>
    </tr>
    <tr>
      <td>Favored rotamers, %</td>
      <td>98.36%</td>
    </tr>
    <tr>
      <td>Poor rotamers, %</td>
      <td>0.30%</td>
    </tr>
    <tr>
      <td>Ramachandran outliers, %</td>
      <td>0.13%</td>
    </tr>
    <tr>
      <td>Clash Score</td>
      <td>0.99</td>
    </tr>
    <tr>
      <td>Molprobity score EM ringer score</td>
      <td>1.02 1.97</td>
    </tr>
  </tbody>
</table>

Similarly to what was reported for the B41 SOSIP trimer (Ozorowski et al., 2017), the 426c DS-SOSIP D3†-VRC01GL V1/V2 apex is closed under cryoEM conditions (Figure 1D,E,F) whereas it appears open in the conditions we used for negative-staining sample preparation (Ozorowski et al., 2017) (Figure 1—figure supplement 3B). We note that the closed 426c DS-SOSIP D3†-VRC01GL trimeric Env conformation observed in cryoEM lacks a formed gp120 bridging sheet, which is reminiscent of other closed SOSIP trimer structures (Figure 1G) (Julien et al., 2015; Lyumkis et al., 2013b; Pancera et al., 2014; Stewart-Jones et al., 2016). VRC01GL-class antibodies have recently been shown to also bind to core gp120 constructs in the presence of a bridging sheet (Scharf et al., 2016). Our data reveal that VRC01GL could also bind a prefusion closed conformation, which had previously only been reported for its mature counterpart, VRC01MAT (Stewart-Jones et al., 2016) (Figure 1G).

### Structural analysis of the region surrounding the CD4BS in 426c DS-SOSIP D3

Removal of CD4BS-surrounding carbohydrates has been shown to enhance binding of CD4BS-targeted germline VRC01-class antibodies and to increase the antigenicity of this region (McGuire et al., 2016; McGuire et al., 2013; Stamatatos et al., 2017; Zhou et al., 2017). Our structural analysis reveals that the 426c DS-SOSIP naturally lacks an NLGS at position Asn234 near the CD4BS, which is otherwise conserved in 80% of known circulating HIV-1 strains (Crooks et al., 2015). Instead, 426c features a glycan at Asn230 that is more remote from the VRC01 epitope than glycan Asn234 (Jardine et al., 2016b) (Figure 1F). The oligosaccharide at position Asn230 appears to be highly dynamic, since only the two proximal N-acetyl-glucosamine (GlcNAc) moieties are resolved in the reconstruction (Figure 1—figure supplement 6) and does not interact with VRC01GL or other glycans in the complex. Previous structural characterization of clades A and G SOSIP trimers established that glycans at positions Asn276 and Asn234 are in close proximity to each other and likely restrain each others’ conformational freedom (Jardine et al., 2016b; Stewart-Jones et al., 2016; Zhou et al., 2017). The absence of glycan Asn234 in 426c gp120 reduces local carbohydrate crowding near the CD4BS which could increase accessibility of this neutralization supersite (Stewart-Jones et al., 2016) and lead to altered local glycan processing (Behrens et al., 2018; Bonomelli et al., 2011).

The 426c DS-SOSIP also lacks an NLGS at position Asn362(363), which is present in 42% of strains deposited in the HIV database (Gaschen et al., 2001) (Figure 1F). This oligosaccharide is located distally from the viral membrane side of the SOSIP trimer (Figure 1F) and is sandwiched between the VRC01MAT heavy chain and glycan Asn386 in the structure of VRC01MAT bound to the JR-FL SOSIP trimer (clade B) (Stewart-Jones et al., 2016). Analysis of the asymmetric 426c DS-SOSIP D3†-VRC01GL structure, comprising two Fabs, revealed that Fab-bound protomers feature slightly better-resolved density for glycan Asn386 than the free protomer when visualized at the same contour level (Figure 1H). These observations suggest that VRC01GL may stabilize the Asn386 glycan either through reduction of its conformational freedom and/or via direct interactions with the Fab framework region. The absence of glycan Asn362 or other topologically equivalent oligosaccharides in the 426c gp120 sequence likely contributes to increased accessibility of the CD4BS to VRC01GL-class bnAbs due to the close proximity of this glycan to the epitope (Stewart-Jones et al., 2016) (Figure 1F).

Similarly to what is observed in available VRC01MAT/SOSIP complex structures (Stewart-Jones et al., 2016), glycan Asn197 density is also strongest when bound to VRC01GL, but appears weaker in the unbound protomer (Figure 1H), again indicating either Fab-induced stabilization or restriction of movement. The position of glycan Asn197 differs substantially between available structures of monomeric gp120 constructs bound to VRC01GL-class Fabs and the VRC01GL-bound SOSIP trimer reported here (Figure 1G) (Scharf et al., 2016). This variation in Asn197 positioning is guided by the formation of the gp120 bridging sheet in monomeric gp120, which would otherwise only form following CD4 receptor binding in the context of trimeric Env (Figure 1G) (Kwon et al., 2012; Zhou et al., 2010). This conformational difference includes the β20/β21 loop, whose orientation in the 426c DS-SOSIP D3†-VRC01GL complex differs relative to crystal structures of VRC01GL-class antibodies in complex with monomeric gp120 (Figure 1G) (Scharf et al., 2016). Although the β20/β21 loop is close to the VRC01 paratope, VRC01MAT was reported to have minimal preference in the conformation of the bridging sheet or β20/β21 region, as 87% of its contact surface area includes the conformationally invariant outer domain of gp120 (Zhou et al., 2010). Whether or not the conformation of the β20/β21 region directly impacts germline VRC01-class antibody binding affinities remains unclear. However, VRC01GL in complex with gp120 constructs lacking this domain have been determined (eOD-GT6 and eOD-GT8), demonstrating that these germline mAbs do not strictly require this region for CD4BS recognition when glycans surrounding the CD4BS are also removed (Jardine et al., 2013).

### Wild-type V5 loop NLGSs of the 426c core did not hinder binding to VRC01GL Fabs

One of the mechanisms by which HIV-1 Env has evolved to avoid detection by the progenitors of VRC01-class bnAbs is by selection of V5 loop NLGSs (Huang et al., 2016; Li et al., 2011; Zhou et al., 2010) which sterically limit access to the CD4BS. The observation that VRC01GL may accommodate carbohydrates surrounding the CD4BS in our 426c DS-SOSIP D3†-VRC01GL cryoEM structure prompted us to assess the effect on binding of the two V5 loop putative NLGSs mutated in 426c DS-SOSIP D3†-VRC01GL. With 426c Env trimers, we previously found that VRC01GL binding could be detected following removal of glycan Asn276, and was further enhanced following removal of wild-type NLGSs at positions Asn460 and Asn463 (McGuire et al., 2013). We also demonstrated that removing the V1/V2, and V3 loops in gp140 Env trimers further increased binding of multiple VRC01-class germline antibodies relative to trimers only containing glycan-depleting mutations (McGuire et al., 2014; McGuire et al., 2016). However, the effects of V1/V2 and V3 loop deletion on VRC01GL binding to 426c core constructs in the presence of glycans remains unclear. Here we reintroduced the two NLGSs at positions Asn460 and Asn463 (in the V5 loop) and assessed their individual and cumulative effects on VRC01GL engagement of the 426c core construct comprised of gp120 residues 44 to 492, and lacking the V1/V2 and V3 variable loops (Kwon et al., 2012). Expanding on our prior work (McGuire et al., 2016), the following four 426c core glycan-deleted combinations were tested using HEK293F-expressed protein constructs: S278A/T462A/T465A, S278A/T465A, S278A/T462A, and S278A (Figure 1—figure supplement 1, Figure 2A–D, Supplementary file 1).

![Figure 2.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig2-v2.jpg)

**Figure 2.:** (A–D) BLI curves and the corresponding equilibrium dissociation constants for VRC01GL IgG binding to the S278A/T462A/T465A (A), S278A/T462A (B), S278A/T465A (C), and S278A (D) 426c core constructs lacking either one or several glycans in the V5 and D loops. The concentrations of 426c core injected and the color key is indicated on each panel. Fitted curves are colored as black dotted lines. The vertical dashed lines indicate the transition between association and dissociation phases. (E) Ribbon diagram of the 426c core†-VRC01GL complex crystal structure. gp120 is colored blue, VRC01GL Fab is colored yellow (heavy chain: dark yellow; light chain: light yellow), and resolved gp120 glycans are shown in surface representation and colored green. (F) Close-up view of the gp120 Asn460 contacts with the backbone carbonyl and amide groups of the light chain VRC01GL residue Ile02. (G) Close-up view of the (GlcNAc)1 at position Asn463 of gp120. Oligosaccharides are labeled by the corresponding Asn residue they are linked to. Hydrogen bonds are represented as dashed lines. (H–I) Semi-quantitative LC-MS/MS analysis of VRC01GL-based IP experiments depicting the relative signal intensities for identified Asn460 (H) and Asn463 (I) glycoforms in unbound (blue), first binding event (red), and second binding event (yellow) fractions. The ‘unbound’ material indicates 426c core glycoforms that did not bind VRC01GL well following three binding steps. The ‘first’ binding event corresponds to 426c core elution fractions following collection of the sample flow-through and three rigorous wash cycles. The ‘second’ binding event follows a rebinding of the aforementioned flow-through, performing three additional washes, and eluting any residual bound material from the VRC01GL affinity column and collecting this fraction. Colored dots associated with their corresponding histogram bars represent individual values extracted from each experimental replicate, with the bar itself representing the experimental mean signal fraction.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** The top-left ribbon diagram corresponds to the sample analyzed. The LC-MS/MS fragmentation pattern is indicated in the top-right inset. A graphical depiction of the Asn276 residue (dotted white circle) and its associated identified glycan (blue: N-acetyl glucosamine, green: mannose) are represented on the spectrum. Green peak labels correspond to precursor peptides with/without LC-MS/MS fragmentation occurring within the glycan. Red/orange peak labels represent identified x, y, and z fragments. Blue/teal peak labels highlight identified a, b, and c fragments. A) Schematic of possible LC-MS/MS peptide fragmentation patterns. The peptide N- and C-termini are labeled. Possible fragmentation positions are denoted as grey text, with x, y, and z fragments represented as red/orange labels and blue/teal fragments representing a, b, and c fragments. Modified R-groups are denoted in red text. (B–C) Representative LC-MS/MS spectra of detected V5 glycosylation profile of the 426c core†-VRC01GL (GnTI-/--expressed) (B) and a ligand-free 426c core containing a glycan at position Asn460 (GnTI-/--expressed) (C). D–J) Various additional representative LC-MS/MS spectra of an Asn276 glycopeptide containing a (GlcNAc)2-(Man)5 oligosaccharide from ligand-free 426c core (HEK293F-expressed) (D), an Asn276 glycopeptide of the 426c core†-VRC01GL complex with a detectable (GlcNAc)2-(Man)4 sugar (GnTI-/--expressed) (E), an Asn276 peptide from the 426c core†-VRC01GL complex that is unglycosylated at position Asn276 (GnTI-/--expressed) (F), a 426c core Asn276 glycopeptide containing a (GlcNAc)2-(Man)5 oligosaccharide (GnTI-/--expressed) (G), a 426c S278T core Asn276 glycopeptide containing a (GlcNAc)2-(Man)5 oligosaccharide (GnTI-/--expressed) (H), and an Asn276 peptide of a 426c S278T core that is unglycosylated at position Asn276 (GnTI-/--expressed) (I).

Reintroduction of the NLGS at position Asn460 (S278A/T465A) in the 426c core had no detectable impact on VRC01GL binding affinity despite the predicted overlap of a putative carbohydrate at position Asn460 with the bound VRC01GL Fab (Guo et al., 2012) (Figure 2A–B, Supplementary file 1). Indeed, our previous work removing NLGSs at positions Asn460 and Asn463 via the N460D/N463D mutations had only a relatively minor impact on VRC01GL engagement to trimeric 426c constructs compared to the large increase in binding observed following removal of the native Asn276 NLGS (McGuire et al., 2016; McGuire et al., 2013). To better understand the molecular rationale of these observations with the monomeric 426c core construct, we engineered a disulfide-linked 426c core†-VRC01GL complex containing all wild-type NLGSs (426c core†-VRC01GL). We co-expressed these proteins using HEK293 GnTI-/- cells, which lack N-acetyl-glucosaminyltransferase I activity and thus are unable to generate complex N-linked carbohydrates (Wright and Morrison, 1994). We then determined its crystal structure at 2.3 Å resolution after endoglycosidase H (EndoH) treatment to facilitate crystallization (Depetris et al., 2012; Freeze and Kranz, 2010) (Figure 2E, Table 2). Despite harboring an NLGS, no glycan density could be resolved at position Asn460 in either of the two molecules of the asymmetric unit. Instead, the Asn460 side chain is hydrogen bonded to the backbone amide and carbonyl groups of the VRC01GL light-chain residue, Ile02 (Ile02LC) (Kong et al., 2016)(Figure 2F). In support of this observation, we detected only unglycosylated Asn460 peptide fragments when analyzing tryptic digests of this sample with liquid chromatography coupled to electron transfer/high-energy collision-dissociation tandem mass-spectrometry (LC-MS/MS) (Figure 2H, Figure 2—figure supplement 1A,B). Furthermore, only low levels of glycosylation were detected at Asn460 by qualitative LC-MS/MS analysis of unliganded 426c core (lacking the G459C mutation) (Figure 2—figure supplement 1C). Additionally, we performed VRC01GL-based immunoprecipitation (IP) experiments utilizing a VRC01GL affinity column and the same 426c core construct. Semi-quantitative LC-MS/MS comparison of the 426c gp120 core samples from fractions that did not bind to VRC01GL (‘unbound’ flow-through), and those that did (‘bound’ elution), revealed no difference in glycan occupancy of the Asn460 NLGS (Figure 2H). This indicated this sequon is rarely glycosylated in 426c core and explains its negligible impact on VRC01GL binding. The predicted overlap of glycan Asn460 with VRC01GL and the absence of a resolved proximal GlcNAc in the crystal structure of 426c core†-VRC01GL also suggests a likely strict preference for the unglycosylated Asn460 glycoform of the 426c gp120 for binding (Figure 2F).

**Table 2.**
 Crystallographic data collection and refinement statistics


<table>
  <thead>
    <tr>
      <th></th>
      <th>426c core†-VRC01GL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data collection</td>
      <td></td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>C2</td>
    </tr>
    <tr>
      <td>Cell dimensions</td>
      <td></td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>197.082, 109.003, 103.225</td>
    </tr>
    <tr>
      <td>α, β, γ (°)</td>
      <td>90.000, 114.468, 90.000</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>50–2.32 (2.36–2.32)*</td>
    </tr>
    <tr>
      <td>Rsym or Rmerge</td>
      <td>0.076 (0.643)*</td>
    </tr>
    <tr>
      <td>I/sI</td>
      <td>23.4 (1.8)*</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>95.6 (66.8)*</td>
    </tr>
    <tr>
      <td>Redundancy</td>
      <td>7.4 (5.7)*</td>
    </tr>
    <tr>
      <td>CC1/2</td>
      <td>(0.823)*</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>46.98–2.315 (2.398–2.315)*</td>
    </tr>
    <tr>
      <td>No. reflections</td>
      <td>83086</td>
    </tr>
    <tr>
      <td>Rwork/Rfree</td>
      <td>24.38/29.55 (42.67/49.28)</td>
    </tr>
    <tr>
      <td>No. atoms</td>
      <td>12470</td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>11746</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>325</td>
    </tr>
    <tr>
      <td>Ligand</td>
      <td>399</td>
    </tr>
    <tr>
      <td>B-factors (Å2)</td>
      <td>74.22</td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>73.57</td>
    </tr>
    <tr>
      <td>Water</td>
      <td>69.62</td>
    </tr>
    <tr>
      <td>Ligand</td>
      <td>97.10</td>
    </tr>
    <tr>
      <td>R.m.s deviations</td>
      <td></td>
    </tr>
    <tr>
      <td>Bond lengths (Å)</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td>Bond angles (°)</td>
      <td>0.60</td>
    </tr>
    <tr>
      <td>Ramachadran Favored %</td>
      <td>93.39</td>
    </tr>
    <tr>
      <td>Ramachadran Outliers %</td>
      <td>0.13</td>
    </tr>
    <tr>
      <td>MolProbity all-atoms clashscore</td>
      <td>4.05</td>
    </tr>
  </tbody>
</table>

We furthermore observed that reintroduction of the Asn463 NLGS (S278A/T462A or S278A) also did not result in a reduction in VRC01GL binding relative to the 426c S278A/T462A/T465A core (Figure 2A,C,D, Supplementary file 1). This result was unexpected, as V5 glycosylation of Env trimers containing all variable loops have been reported to negatively affect VRC01GL recognition of the CD4BS (Huang et al., 2016; Li et al., 2011; McGuire et al., 2013; Zhou et al., 2010). We observed electron density for the proximal GlcNAc linked to Asn463 in one of the two molecules of the asymmetric unit of the 426c core†-VRC01GL crystal structure and cross-validated the presence of this post-translational modification using LC-MS/MS (Figure 2G). VRC01GL-based IP experiments followed by semi-quantitative LC-MS/MS validated these structural observations by detecting an Asn463 glycosylation profile which was indistinguishable between ‘bound’ elution and ‘unbound’ flow-through fractions (Figure 2I). This supports our BLI data suggesting the Asn463 glycan does not hinder VRC01GL binding in the context of the 426c core and that this site is glycosylated.

### VRC01GL Fab bound to the Asn276 glycan-containing 426c core construct

A hallmark of VRC01-class bnAb maturation is the shortening of the CDRL1 loop length and/or the addition of glycine residues, both of which have been proposed to enable accommodation of the Asn276 glycan near the CD4BS (Jardine et al., 2016a; Scharf et al., 2016; Wu et al., 2015; Zhou et al., 2010). Although VRC01MAT was shown to bind to the trimeric Env CD4BS in the presence of glycan Asn276, its removal significantly increased binding affinity and neutralization potency (Jardine et al., 2013; McGuire et al., 2016; McGuire et al., 2013; Medina-Ramírez et al., 2017a; Stamatatos et al., 2017). Removal of the Asn276 NLGS from certain trimeric SOSIP constructs by either N276D or (S/T)278(A/R) mutations significantly enhanced the antigenicity of the VRC01 epitope (McGuire et al., 2016; McGuire et al., 2013). However, when such glycan-depleted trimeric Env constructs were used as immunogens, the antibodies they elicited failed to overcome the glycan present at position Asn276 of wild-type viruses (Briney et al., 2016; Dosenovic et al., 2015). Removal of glycan Asn276 through N276A substitution abrogated VRC01GL interactions, indicating this amino acid residue was critical for binding (McGuire et al., 2016). These observations suggest that initial engagement of VRC01-class bnAb precursors in infected individuals occurs with an asparagine at position 276 and may also be possible, at low levels, in the presence of a glycan at this NLGS (Scharf et al., 2016).

Considering the reduced glycan shielding of the 426c strain, the deletion of variable loops 1, 2, and 3 in our 426c core constructs, and the minimal impact V5 loop NLGSs had on VRC01GL binding, we tested whether the wild type 426c core construct could interact with VRC01GL in the presence of the Asn276 NLGS (Figure 1—figure supplement 1). BLI analysis revealed VRC01GL bound similarly to both the HEK293F and HEK293 GnTi-/--expressed 426c cores with equilibrium dissociation constants of 11 μM and 15 μM, respectively (Figure 3A,B). The crystal structure of the disulfide engineered 426c core†-VRC01GL complex expressed in GnTi-/- cells further reveals the presence of a resolved glycan at position Asn276 in one of the two molecules of the asymmetric unit, indicating VRC01GL bound to both Asn276 glycosylated and unglycosylated species (Figure 3C–J).

![Figure 3.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig3-v2.jpg)

**Figure 3.:** (A–B) BLI binding data of the immobilized VRC01GL Fab with the 426c core expressed in either HEK293F (A) or HEK293 GnTI-/- cells (B). (C) Crystal structure of 426c core†-VRC01GL highlighting glycan electron density at position Asn276 (grey mesh: 2FO-Fc map contoured at 1.0σ) and amino-acid contacts for one molecule of the asymmetric unit. (D) Structure of VRC01MAT in complex (crosslinked) with the HIV-1 JR-FL SOSIP trimer (PDB ID: 5FYK) (Stewart-Jones et al., 2016) in the same orientation as in panel (C) and focusing on the glycan at position Asn276. (E) CryoEM structure of the 426c DS-SOSIP D3†-VRC01GL complex in the same orientation as in panel (C) and focusing on Asn276. Hydrogen bonds spanning 2.8–3.5 Å are depicted as dashed lines. (F–H) Comparison of VRC01GL CDRL1 conformations in the presence or absence of a glycan at position Asn276. In the three panels, gp120 is shown in blue cartoon representation and VRC01GL light chain in light yellow for our crystal structure of 426c core†-VRC01GL. Residues Gln27 to Tyr32 of VRC01GL light chain are shown as sticks and labeled. (F) VRC01GL bound to eODGT6 (PDB ID: 4JPK)(Jardine et al., 2013) is shown in grey. (G) Chain B of unliganded VRC01GL (PDB ID: 4JPI) (Jardine et al., 2013) is shown in cyan. (H) Chain L of unliganded VRC01GL (PDB ID: 4JPI) (Jardine et al., 2013) is shown in pink. (I) Semi-quantitative LC-MS/MS analysis depicting the relative signal intensities for identified Asn276 glycoforms in unbound (blue), after the first binding event (red), and after the second binding event (yellow) fractions taken from VRC01GL-based IP experiments. The ‘unbound’ material indicates 426c core glycoforms that did not bind VRC01GL following three binding events. Colored dots on corresponding histogram bars represent individual values extracted from each experimental replicate, with the bar itself representing the experimental mean signal fraction. (Inset) SDS-PAGE depicting the average molecular weight difference between wild-type 426c core species in ‘unbound’ flow-through and ‘bound’ elution fractions. (J) Structural comparison of VRC01GL CDRL1 conformations in the presence or absence of a glycan at position Asn276 in each of the molecules present in the asymmetric unit of our 426c core†-VRC01GL crystal structure.

Analysis of this structure highlights distinct sets of interactions observed between the light chains of VRC01GL or VRC01MAT and glycan Asn276, which is rotated ~90˚ when comparing the two structures (Figure 3C–D). In line with our previous observation that Asn276 is important for VRC01GL recognition (McGuire et al., 2016), we observed that Asn276 is hydrogen bonded to the VRC01GL light chain residue Tyr91 in our 426c core†-VRC01GL and 426c DS-SOSIP D3†-VRC01GL structures, but not in the JR-FL SOSIP-VRC01MAT crosslinked complex structure (Figure 3C–E) (PDB: 5FYK) (Stewart-Jones et al., 2016). The CDRL1 of VRC01GL has been shown to adopt multiple conformations both when unliganded and when bound to eOD-GT6; the latter of which lacked a glycan at position Asn276 (Jardine et al., 2013). The CDRL1 loop of NIH45-46GL (a germline VRC01-class antibody) bound to the 426c core TM4 adopts a similar orientation as the one observed for the CDRL1 loop of VRC01GL bound to eOD-GT6 (Scharf et al., 2016) (Jardine et al., 2013) (Supplementary file 2). Comparisons between the structures of our 426c core†-VRC01GL complex, a putatively authentic germline VRC01/eOD-GT6 complex (PDB ID 4JPK [Jardine et al., 2013]) and the unliganded VRC01GL (PDB ID 4JPI) (Jardine et al., 2013), indicate that the CDRL1 of VRC01GL accommodates the Asn276 oligosaccharide in a conformation similar to the CDRL1 of unliganded VRC01GL (chain B) (Supplementary file 2)(Jardine et al., 2013), but differs from a complex with a gp120 core lacking this glycan (Figure 3F–H). This observation supports disulfide crosslinking of 426c core†-VRC01GL did not distort the binding interface into a non-native conformation for the accommodation of glycan Asn276 in our structure (Figure 3C). LC-MS/MS analysis of the sample used for crystallization revealed N-linked carbohydrates at position Asn276 of 426c core†-VRC01GL ranged from (GlcNAc)2-(Man)4 to (GlcNAc)2-(Man)5 (Figure 4A,B, Figure 2—figure supplement 1E). Unglycosylated Asn276 peptides were also identified, corroborating the presence of two populations of molecules in the crystal structure and the ability of VRC01GL to recognize both species (Figure 4A, Figure 2—figure supplement 1F).

![Figure 4.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig4-v2.jpg)

**Figure 4.:** (A) Summary of identifications for 426c Asn276 glycopeptides. 426c core constructs that were subjected to qualitative LC-MS/MS are indicated on the left. Glycopeptide identifications detected using the Byonic software (Bern et al., 2012) are listed in blue and denoted with a check-mark (✓). (B–C) Representative LC-MS/MS spectra from panel (A) of glycan Asn276 identifications from the cross-linked 426c core†-VRC01GL and unliganded 426c core complex following EndoH digestion. The top-left ribbon diagram corresponds to the sample analyzed. The LC-MS/MS fragmentation pattern is indicated in the top-right inset. A graphical depiction of the Asn276 residue (dotted circle) and its associated identified glycan (blue: N-Acetylglucosamine, green : Mannose) are represented on the spectrum. The black line indicates identification of the precursor mass with neutral losses corresponding to the identified glycopeptide. Green peak labels correspond to precursor peptides with/without LC-MS/MS fragmentation occurring within the glycan. Red/orange peak labels represent identified x, y, and z fragments. Blue/teal peak labels highlight identified a, b, and c fragments. After EndoH digestion, a (GlcNAc)2-(Man)5 glycan was the predominant glycoform identified at position Asn276 with the sample used for crystallization (B) whereas a (GlcNAc)1 glycan prevailed with the unliganded 426c core (C).

Despite the EndoH treatment used to promote crystallization of 426c core†-VRC01GL, no (GlcNAc)1 glycopeptides were detected at the Asn276 NLGS by LC-MS/MS (Figure 3A). In contrast, we detected digested glycopeptides containing (GlcNAc)1 moieties for other NLGSs, confirming the efficiency of the EndoH treatment (Figure 2—figure supplement 1B). These observations validated the Asn276 glycan density observed in the crystal structure and suggested that bound VRC01GL protected the glycan Asn276 from enzymatic digestion (Figure 4A,B), but not other oligosaccharides, such as glycan Asn463 (Figure 2E,G and Figure 2—figure supplement 1B). We further corroborated this hypothesis by analyzing EndoH-treated 426c core in the absence of co-expressed VRC01GL and confirmed the presence of (GlcNAc)1 moieties at position Asn276 by LC-MS/MS (Figure 3A,C), supporting that digestion of this glycan was possible if not sterically hindered by the binding of this Fab (Yet et al., 1988).

To probe whether the disulfide cross-link promoted artificial accommodation of glycan Asn276, we performed an additional analysis with samples obtained from IP experiments using the 426c core construct lacking the G459C mutation. 426c core samples from the ‘unbound’ flow-through and ‘bound’ elution fractions had distinct migration profiles by SDS-PAGE (Figure 3I), with the bound fraction exhibiting higher electrophoretic mobility than the unbound species. LC-MS/MS revealed the bound fraction was enriched for unglycosylated Asn276 peptides, suggesting this subspecies was the preferred VRC01GL binder (Figure 3I). This result corroborates reports of VRC01GL binding occurring preferentially in the absence of a glycan at position 276 (Jardine et al., 2013; McGuire et al., 2016; McGuire et al., 2013; Medina-Ramírez et al., 2017a; Scharf et al., 2016; Stamatatos et al., 2017). However, we also detected that the majority of the Asn276 peptide signal was of the (GlcNAc)2-(Man)5 glycoform in bound fractions (approximately twice as much as the unglycosylated Asn276 signal) (Figure 3I), suggesting VRC01GL could indeed bind in the presence of this glycan and in the absence of an engineered cross-link. This experiment, along with our crosslinked 426c core†-VRC01GL crystal structure and qualitative LC-MS/MS, confirm both the glycosylated (Figure 3C,F,G,H,I) and unglycosylated Asn276 glycoforms are present following expression and that VRC01GL could accommodate both. In summary, VRC01GL bound a 426c core with wild-type NLGSs, was sterically compatible with glycans present at positions Asn276 and Asn463, and strictly interacted with a subspecies of gp120 lacking a glycan at position Asn460.

### Modulation of glycan composition altered VRC01GL antibody recognition of the 426c core

Irrespective of the chosen expression system (HEK293F or HEK293 GnTI-/-), our LC-MS/MS analyses showed that 426c core constructs all contained detectable levels of both the unglycosylated and the (GlcNAc)2-(Man)5 oligosaccharide variants at position Asn276 (Figure 4A–B, Figure 3I, Figure 2—figure supplement 1D–G). Since (GlcNAc)2-(Man)5 is a short glycan produced in mammalian cells (Hossler et al., 2009), and was the major detectable glycosylated form in VRC01GL-based IP ‘bound’ elution fractions, we interrogated whether differential expression conditions known to enrich for (GlcNAc)2-(Man)9 glycans could negatively impact the binding of VRC01GL IgGs to 426c core. We thus compared VRC01GL binding to HEK293 GnTI-/--produced 426c core constructs expressed in the absence or presence of 100 µM kifunensine to yield a range of (GlcNAc)2-(Man)5 to (GlcNAc)2-(Man)9 glycans or to enrich for (GlcNAc)2-(Man)9 glycans, respectively (Depetris et al., 2012).

The efficacy of this strategy was confirmed by two orthogonal methods: (1) SDS-PAGE, which demonstrated the two expression conditions yielded samples with distinct migration profiles, and (2) LC-MS/MS, which confirmed enrichment for (GlcNAc)2-(Man)9 glycans in the presence of kifunensine (Figure 5A, Figure 5—figure supplement 1A–C). Importantly, binding affinities for the 426c core were improved by ~10 fold in the context of immobilized full-length VRC01GL IgGs relative to immobilized VRC01 Fabs. The 426c core expressed using HEK293 GnTI-/- in the absence of kifunensine bound VRC01GL IgG with a KD of 2 µM (Figure 5—figure supplement 1B, Supplementary file 3), whereas binding was significantly reduced when the 426c core was expressed in the presence of kifunensine (Figure 5C, Supplementary file 3). The VRC01GL IgG binding affinity to 426c core expressed in GnTI-/- cells in the presence of kifunensine was enhanced following treatment with EndoH (KD = 245 nM, Figure 5D, Supplementary file 3), confirming recognition of gp120 by VRC01GL IgGs can occur in the presence of a proximal GlcNAc at position Asn276. This VRC01GL IgG binding affinity was similar to the HEK293 GnTI-/--expressed 426c S278A core construct (KD = 204 nM), although the kinetics of binding differed for the two samples (Figure 5E).

![Figure 5.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig5-v2.jpg)

**Figure 5.:** (A) Semi-quantitative LC-MS/MS analysis depicting the relative signal intensities for identified Asn276 glycoforms in 426c core (blue), 426c S278T core (yellow), and 426c core expressed in the presence of 100 µM kifunensine (red). (Inset) SDS-PAGE demonstrating the molecular weight difference between the 426c core expressed in the absence (K-) or presence (K+) of 100 µM kifunensine. The molecular weights of the protein standards are indicated on the left. (B–E) BLI binding data and determined equilibrium dissociation constant values of VRC01GL IgG binding to the 426c core expressed using HEK293 GnTI-/- cells (B), the 426c core expressed using HEK293 GnTI-/- cells in the presence of 100 μM kifunensine (C), the 426c core expressed using HEK293 GnTI-/- cells and digested with EndoH (D), and the 426c S278A core expressed using HEK293 GnTI-/- cells (E). The concentrations of 426c core injected are indicated on each panel. Fitted curves are colored as black dotted lines. The vertical dotted lines indicate the transition between association and dissociation phases. N/D: not determined. (F–I) Semi-quantitative LC-MS/MS analysis depicting the relative signal intensities of unbound (blue), first binding event (red), and second binding event (yellow) fractions taken from VRC01GL-based IP experiments. Glycoforms were analyzed for NLGSs Asn197 (G), Asn289 (H), Asn337 (I), and Asn442 (J). Colored dots in panels A and F-I represent individual values extracted from each experimental replicate, with the bar itself representing the experimental mean signal fraction.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Representative LC-MS/MS spectra of glycan Asn276 identifications from the kifunensine-treated 426c core sample used for BLI experiments. The top-left ribbon diagram corresponds to the sample analyzed. The LC-MS/MS fragmentation pattern is indicated in the top-right inset. A graphical depiction of the Asn276 residue (dotted white circle) and its associated identified glycan (blue: N-acetyl glucosamine; green: mannose;) are represented on the spectrum. Green peak labels correspond to precursor peptides with/without LC-MS/MS fragmentation occurring within the glycan. Red/orange peak labels represent identified x, y, and z fragments. Blue/teal peak labels highlight identified a, b, and c fragments. (A–D) Representative LC-MS/MS spectra of an Asn276 glycopeptide with a (GlcNAc)2-(Man)5 oligosaccharide from the 426c core expressed in GnTI-/- cells in the presence of 100 µM kifunensine (A), an Asn276 glycopeptide with a (GlcNAc)2-(Man)8 oligosaccharide (B), an Asn276 glycopeptide with a (GlcNAc)2-(Man)9 oligosaccharide (C), and an unglycosylated Asn276 peptide (D). All these identifications were made from the same kifunensine-treated sample.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Representative LC-MS/MS spectra of glycan Asn276 identifications from the 426c DS-SOSIP. The top-left ribbon diagram corresponds to the sample analyzed. The LC-MS/MS fragmentation pattern is indicated in the top-right inset. A graphical depiction of the Asn276 residue (dotted white circle) and its associated identified glycan (green circle = Mannose; blue = N Acetylglucosamine) are represented on the spectrum. Green peak labels correspond to precursor peptides with/without LC-MS/MS fragmentation occurring within the glycan. Red/orange peak labels represent identified x, y, and z fragments. Blue/teal peak labels highlight identified a, b, and c fragments. (A–D) Representative LC-MS/MS spectrum of an Asn276 glyco-peptide of a detectable (GlcNAc)2-(Man)5 glycan (A), a (GlcNAc)2-(Man)6 glycan (B), a (GlcNAc)2-(Man)7 glycan (C), and a (GlcNAc)2-(Man)8 glycan (D).

Previous studies demonstrated enhanced VRC01MAT binding following glycan Asn276 removal, although VRC01MAT could also accommodate an Asn276 glycan when present (Jardine et al., 2013; McGuire et al., 2013; Medina-Ramírez et al., 2017a); McGuire et al., 2016; Scharf et al., 2016; Stamatatos et al., 2017; Zhou et al., 2017). Similarly to VRC01MAT, VRC01GL binding was previously detected in the absence of the Asn276 glycan (McGuire et al., 2016; McGuire et al., 2013). In this present study, VRC01GL binding was also observed under typical expression conditions with the native Asn276 NLGS retained, but was reduced following expression in the presence of kifunensine (Supplementary file 3, Figure 5A,B,C, Figure 5—figure supplement 1A,B,E,F). This may indicate that kifunensine treatment results in more efficient glycosylation of some NLGSs or that differences in glycan length influence recognition of VRC01GL-class antibodies to the CD4BS, or both (Figure 5A). In line with these hypotheses, the VRC01GL-based IP and subsequent semi-quantitative LC-MS/MS of the 426c core expressed in the absence of kifunensine revealed a consistent preference for short and/or unglycosylated species bound to VRC01GL (Figure 3I, Figure 5F,G,H,I). These findings explain the observed increase in electrophoretic mobility of 426c core species in VRC01GL-based IP fractions that bound this antibody compared to the unbound fraction (Figure 3I).

While many 426c core glycans are likely to be affected by either kifunensine or EndoH treatment, the Asn276 oligosaccharide is expected to have a pronounced negative effect on VRC01GL binding due to its direct overlap with the VRC01GL epitope (Stewart-Jones et al., 2016; Zhou et al., 2017). The 426c core†-VRC01GL crystal structure does not resolve ordered mannose rings at position Asn276, despite their high detected abundance by LC-MS/MS, and thus only the two proximal GlcNAc moieties were modeled in our structure (Figure 4C). This indicates the Asn276 mannose moieties are likely not directly involved in binding to VRC01GL light chain, but rather act as a steric barrier VRC01GL must overcome to interact with the CD4BS. Qualitative LC-MS/MS analyses of the 426c DS-SOSIP trimer, expressed in the absence of kifunensine, revealed longer glycans at the Asn276 NLGS, which correlated with a poorer binding affinity, relative to the 426c core also expressed in the absence of kifunensine (Figure 1A, Figure 5—figure supplement 2). Indeed, interactions with the Asn276-linked mannose moieties might be restricted to VRC01MAT, as these rings are well-resolved in corresponding crystal structures. VRC01GL-specificity and compatibility for proximal GlcNAcs is made evident by the increased affinity of VRC01GL for the 426c core following digestion with EndoH (Figure 5D). These results indicate binding of several germline antibodies to gp120 core constructs could potentially be modulated by tailoring protein expression conditions, oligosaccharide length, and/or by endoglycosidase treatment, as opposed to strict mutations aimed at abolishing NLGSs (Kong et al., 2010).

### The amino acid sequence of an intact 426c core Asn276 NLGS modulated VRC01GL antibody recognition

Considering our prior work demonstrating that amino acid composition of the Asn276 NLGS impacted VRC01GL recognition independently of glycan presence (McGuire et al., 2016), and our observation that VRC01GL could bind to 426c core in the presence of a native NLGS at position Asn276 (with a preferential selection for the unglycosylated variant), we decided to test whether altering the identity of the Asn276 NLGS at the 278 position could impact VRC01GL-class antibody binding. Whereas 82% of sequenced HIV-1 clades harbor a threonine residue at position 278 of gp120, 426c gp120 contains a serine at this position. Since recent reports suggested NXT NLGS sites are more efficiently glycosylated relative to NXS sites (Huang et al., 2017), we compared the binding kinetics of full-length VRC01GL-class IgGs, VRC01GL and 12A21GL, to HEK293 GnTI-/--expressed 426c core and an 426c S278T core mutant (Figure 1—figure supplement 1 and Figure 1—figure supplement 2). BLI experiments demonstrated the S278T mutation reduced the equilibrium dissociation constant by 10-fold relative to the wild type NLGS, mainly by decreasing association kinetics (Figure 6A–D, Figure 5—figure supplement 2A). The S278T mutation did not abrogate VRC01GL-class antibody binding, despite an expected improvement in Asn276 glycosylation efficiency (Huang et al., 2017). Moreover, semi-quantitative LC-MS/MS revealed (GlcNAc)2-(Man)5 oligosaccharides were predominantly detected at position Asn276 in the S278T mutant, though some unglycosylated peptides were still present at low levels (Figure 5A, Figure 2—figure supplement 1H,I).

![Figure 6.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig6-v2.jpg)

**Figure 6.:** (A–D) BLI binding data and associated KD values of 426c core constructs, expressed in HEK293 GnTI-/- cells, with two immobilized VRC01GL-class IgGs. VRC01GL IgG binding was assessed against the 426c core (A) and the 426c S278T core (B). 12A21GL binding to the 426c core (C) and 426c S278T core (D) were also tested. (E–H) BLI binding data and corresponding KD values of 426c core constructs, expressed using HEK293 GnTI-/- cells and treated with EndoH, with VRC01GL-class IgGs. VRC01GL IgG binding was assessed against the EndoH-treated 426c core (E) and the 426c S278T core (F). 12A21GL interactions with the EndoH-treated 426c core (G) and 426c S278T core (H) were also tested. The concentrations of 426c core injected and the color key are indicated on each panel. Fit curves are colored as black dotted lines. The vertical dotted lines indicate the transition between association and dissociation phases.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/37688/elife-37688-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) BLI kinetics parameters determined from panels (B–G) and Figure 6. (B–D) BLI binding data and determined equilibrium dissociation constants for VRC01GL IgG binding to 426c S278A core (A), 426c S278V core (B), and 426c S278R core. (E–G) BLI binding data and determined equilibrium dissociation constants of 12A21GL IgG binding to 426c S278A core (A), 426c S278V core (B), and 426c S278R core. The concentrations of 426c core injected are indicated on each panel. Fit curves are colored black. The vertical dashed lines indicate the transition between association and dissociation phases.

To rule out any potential impact residue identity at position 278 might have on VRC01GL-class antibody binding affinities (irrespective of glycosylation status), we mutated the Asn276 NLGS using substitutions S278A, S278V, and S278R (Figure 1—figure supplement 1). Although the magnitude of binding was improved relative to both 426c core constructs containing a glycan at position Asn276, no appreciable difference in affinities was detected among any of these NLGS-depleted 426c core mutants (Figure 6—figure supplement 1A–F). Since binding was reduced following introduction of the S278T mutation, these results collectively suggest that a significant fraction of the interactions observed by BLI between the 426c core (containing an intact Asn276 NXS NLGS) and VRC01GL occurred with the unglycosylated Asn276 subspecies. This construct is expected to be less-frequently glycosylated at position Asn276 relative to the S278T mutant (Huang et al., 2017). However, VRC01GL-class IgG binding was also detected with the 426c S278T core (Figure 6A–D, Figure 6—figure supplement 1A), and EndoH treatment (which retains core GlcNAcs) of both the S278 and S278T constructs significantly improved IgG binding relative to their untreated counterparts (Figure 6E–H, Figure 6—figure supplement 1A). Although these findings support that VRC01GL-class binding is dampened by the Asn276 mannose moieties , interactions were still possible, as underscored by the presence of this carbohydrate in the crystal structure (Figure 3C), the EndoH protection assay (Figure 4B,C), and VRC01GL-based IP LC-MS/MS analyses of non-crosslinked samples (Figure 3I). The ability of VRC01GL-class antibodies to recognize a CD4BS containing an NLGS at position Asn276 and the linked oligosaccharide is unprecedented, and highlights a potentially unique feature of the 426c core construct containing all native NLGSs for engagement of VRC01GL antibodies.

## Discussion

Broad-spectrum and potent neutralization of HIV-1 by naturally occurring VRC01 bnAbs targeting the CD4BS is possible in humans (Huang et al., 2016). However, mature VRC01-class bnAbs are produced only in a small fraction of infected individuals and only after up to a decade following the initial infection (Wu et al., 2015). Due to the negligible binding of germline VRC01-class antibodies to ‘wild-type’ stabilized prefusion-closed SOSIP trimers, we sought out to understand putative mechanisms of primary engagement of this class of germline antibodies by various HIV-1 immunogens. To this end, we first engineered a disulfide bond between the glycan depleted 426c DS-SOSIP D3 and VRC01GL to promote complex formation. This tethering approach was recently described for VRC01MAT and led to native structures that do not suffer from any distortions (Stewart-Jones et al., 2016). It is unlikely that the engineered disulfide would force the VRC01GL and 426c gp120 to interact in a homogeneous way. Indeed, an engineered disulfide bond would only prevent dissociation of the two proteins (similarly to what we previously described for mature VRC01 [Stewart-Jones et al., 2016]), but will not force them to interact uniformly (Stewart-Jones et al., 2016). Using this crosslinking strategy, we demonstrated that VRC01GL bound to the deglycosylated 426c DS-SOSIP D3† trimer in the absence of a formed bridging sheet and that this binding stabilized surrounding CD4BS carbohydrates at position Asn197 and Asn386. Considering there was a minor enrichment for the unglycosylated Asn197 glycoform in ‘bound’ fractions following VRC01GL-based immunoprecipitation of the 426c core, there could be an entropic cost associated with binding in the presence of this particular oligosaccharide. Additionally, we found that 426c naturally lacks glycans at positions Asn234 and Asn362, which likely enhanced accessibility of the CD4BS to bnAbs and could affect processing of nearby carbohydrates (Behrens et al., 2018), including glycan Asn276. We propose this is one of the reasons explaining the ability of 426c DS-SOSIP D3 and 426c core constructs to bind VRC01GL-class antibodies.

Immunogen design efforts focusing on VRC01-class bnAbs have thus far largely relied on the mutagenic removal of NLGSs during priming followed by their reinsertion during subsequent boosts (McGuire et al., 2013; Medina-Ramírez et al., 2017a; Zhou et al., 2017). This strategy may not recapitulate the conditions of bona fide infections, as several CD4BS NLGSs are conserved amongst circulating HIV-1 strains (Crooks et al., 2015; Lavine et al., 2012; Pritchard et al., 2015; Stewart-Jones et al., 2016). The complete absence of these NLGSs during the priming phase may also remove a selection pressure guiding proper accommodation of these glycans during antibody affinity maturation, and could explain the limited success achieved thus far to elicit VRC01-class bnAbs capable of neutralizing natively glycosylated wild-type viruses. As a result, alternative priming and boost strategies retaining these native NLGSs may need to be considered.

Specifically, HIV-1 gp120 core constructs have previously been shown to have differential processing of NLGSs around the CD4BS relative to their trimeric SOSIP counterparts (Bonomelli et al., 2011). We observed that reintroduction of 426c gp120 V5 loop NLGSs did not negatively impact VRC01GL binding to the 426c core in contrast with what was detected for trimeric 426c gp140 (McGuire et al., 2013). We found that VRC01GL Fabs and IgGs could bind to the 426c core (containing a wild-type Asn276 NLGS) but, as expected, not to a trimeric 426c DS-SOSIP construct containing all wild-type NLGSs (Huang et al., 2016). We put forward this interaction is likely permitted in the 426c core in part due to the absence of variable loops 1, 2, and 3, and could potentially be further augmented by the natural absence of glycans at position Asn234 and Asn362. It is also possible that stabilized trimeric pre-fusion closed SOSIP constructs impart additional negative steric effects not present in the monomeric gp120 core. This is supported by our observation that there is a reduced amount of trimming of the Asn276 glycan in the 426c DS-SOSIP trimer relative to the 426c core monomer. This could arise from steric properties of the trimer which would be absent in soluble monomeric constructs, thereby limiting unfettered access of the glycosylation machinery to this site during expression. It also remains to be determined if the conformation of the gp120 bridging sheet influences the recognition efficacy of this germline antibody.

We found that VRC01GL binding to 426c core constructs preferentially occurred using expression systems allowing for production of short glycans and provided a structural framework for accommodation of the Asn276 oligosaccharide by the VRC01GL CDRL1. As is the case for VRC01MAT (Jardine et al., 2013; McGuire et al., 2016; McGuire et al., 2013; Medina-Ramírez et al., 2017a; Stamatatos et al., 2017), we would like to emphasize that the unglycosylated Asn276 variant is the preferred VRC01GL binding partner and likely had an important contribution to the interactions observed by BLI. However, we detected glycosylation at position Asn276, both structurally and by LC-MS/MS following VRC01GL-based IP experiments, in the VRC01GL-bound fractions, in the presence and absence of cysteine cross-linking, respectively. This indicated accommodation of this oligosaccharide could occur during VRC01GL binding in the absence of CDRL1 loop shortening and/or glycine addition, arguing in favor of its retention in epitope-based constructs derived from the 426c strain of HIV-1.

The structural and biophysical data reported here provide a foundation for understanding how bnAbs targeting the HIV-1 CD4BS may be elicited in humans in the presence of a native Asn276 NLGS. We demonstrated structurally that VRC01GL binding to a 426c core is possible and appears to occur both in the absence and presence of a glycan at position Asn276, supporting recently proposed hypotheses (Jardine et al., 2016b; Scharf et al., 2016). Introduction of an NXS NLGS at position Asn276 of g120 core constructs lacking selected variable loops and in absence of glycans Asn234, Asn362(363), and Asn460 could prove a useful strategy to elicit VRC01-class antibodies during the priming phase of immunization. Additionally, the stark differences in binding observed between VRC01GL and 426c DS-SOSIP or 426c core constructs suggests ‘germline-targeting’ vaccine design strategies starting with a gp120 immunogen may be a promising alternative to current priming strategies focusing on glycan-depleted HIV-1 SOSIP trimers. Indeed, a remarkable success using site-directed epitope-based immunogens targeting other antigenic regions of HIV-1 Env has been recently achieved (Xu et al., 2018). In the context of VRC01GL-targeted immunogens, the use of insect cell expression systems may further benefit recognition of the HIV-1 CD4BS due to the abundance of paucimannose sugars (Altmann et al., 1999). This approach has already been reported to enhance the immunogenicity of the CD4BS for other HIV-1 antibodies, but has yet to be specifically shown for antibodies of the VRC01 lineage (Kong et al., 2010). We highlight here the advantages of using an HIV-1 426c core construct for enhancing VRC01-class germline antibody binding relative to the glycan-depleted 426c trimeric Env SOSIP construct and propose that these observations be considered in future HIV-1 vaccine design efforts.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or Resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Software, algorithm</td>
      <td>Leginon</td>
      <td>doi: 10.1016/ j.jsb.2005.03.010</td>
      <td></td>
      <td>http://emg.nysbc.org/redmine/projects/leginon/wiki/Leginon_Homepage</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RELION-2</td>
      <td>doi: 10.1016/ j.jsb.2012.09.006</td>
      <td>RRID:SCR_016274</td>
      <td>http://www2.mrc-lmb.cam.ac.uk/relion/index.php/Main_Page</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MotionCor2</td>
      <td>doi:10.1038/ nmeth.4193</td>
      <td></td>
      <td>http://emg.nysbc.org/redmine/projects/appion/wiki/Appion_Home</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GCTF</td>
      <td>doi: 10.1016/ j.jsb.2015.11.003</td>
      <td>RRID:SCR_016500</td>
      <td>https://www.mrc-lmb.cam.ac.uk/kzhang/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>CTFFIND4</td>
      <td>doi:10.1016/ j.jsb.2015.08.008</td>
      <td></td>
      <td>http://grigoriefflab.janelia.org/ctffind4</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Frealign</td>
      <td>doi: 10.1016/ bs.mie.2016.04.013</td>
      <td></td>
      <td>http://grigoriefflab.janelia.org/frealign</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Appion Package</td>
      <td>doi: 10.1016/ j.jsb.2009.01.002</td>
      <td></td>
      <td>http://emg.nysbc.org/redmine/projects/appion/wiki/Appion_Home</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DoG Picker</td>
      <td>doi:10.1016/ j.jsb.2009.01.004</td>
      <td></td>
      <td>http://emg.nysbc.org/redmine/projects/appion/wiki/Appion_Home</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Coot</td>
      <td>doi: 10.1107/ S0907444910007493</td>
      <td>RRID:SCR_014222</td>
      <td>http://www2.mrc-lmb.cam.ac.uk/Personal/pemsley/coot/devel/build-info.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Rosetta</td>
      <td>doi: 10.1146/annurev. biochem.77.062906 .171838</td>
      <td>RRID:SCR_015701</td>
      <td>https://www.rosettacommons.org/software</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>UCSF Chimera</td>
      <td>doi: 10.1002/jcc.20084</td>
      <td>RRID:SCR_004097</td>
      <td>http://plato.cgl.ucsf.edu/chimera/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PMI-Byonic</td>
      <td>doi: 10.1002/ 0471250953.bi1320s40</td>
      <td></td>
      <td>https://www.proteinmetrics.com/products/byonic/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Skyline</td>
      <td>doi: 10.1093/ bioinformatics/btq054</td>
      <td>RRID:SCR_014080</td>
      <td>https://skyline.ms/project/home/software/Skyline/begin.view</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Octet Data Acquisition</td>
      <td>Pall ForteBio</td>
      <td>CFR 10.0.3.12d</td>
      <td>https://www.fortebio.com/octet-software.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Octet Data Analysis</td>
      <td>Pall ForteBio</td>
      <td>CFR 10.0.3.1</td>
      <td>https://www.fortebio.com/octet-software.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phaser</td>
      <td>doi:10.1107/ S0021889807021206</td>
      <td></td>
      <td>https://www.phenix-online.org/documentation/reference/phaser.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phenix.refine</td>
      <td>doi:10.1107/ S0907444912001308</td>
      <td></td>
      <td>https://www.phenix-online.org/documentation/reference/refinement.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism</td>
      <td>GraphPad</td>
      <td>RRID:SCR_002798</td>
      <td>https://www.graphpad.com/scientific-software/prism/</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Pymol</td>
      <td>Delano, 2002</td>
      <td></td>
      <td>https://pymol.org/2/</td>
    </tr>
    <tr>
      <td>Cell Line (Homo sapiens)</td>
      <td>HEK293S GnTI-/-</td>
      <td>ATCC</td>
      <td>ATCC: CRL-3022; RRID:CVCL_A785</td>
      <td>https://www.atcc.org/Products/All/CRL-3022.aspx</td>
    </tr>
    <tr>
      <td>Cell Line (Homo sapiens)</td>
      <td>HEK293F</td>
      <td>ThermoFisher Scientifc</td>
      <td>Cat# R79007</td>
      <td>https://www.thermofisher.com/order/catalog/product/R79007</td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>gl VRC01 Igk(3-11)</td>
      <td>doi: 10.1126/ science.1192819</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>gl VRC01 Igg Fab</td>
      <td>doi: 10.1038/ ncomms10618</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>gl VRC01 Igg Fab A60C/C98S</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>gl VRC01 Igg</td>
      <td>10.1126/science.1192819</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>gl 12A21 Igk(1-33)</td>
      <td>10.1084/jem.20122824</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>gl 12A21 Igg Fab</td>
      <td>10.1038/ncomms10618</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>gl 12A21 Igg</td>
      <td>10.1084/jem.20122824</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Human Immunodeficiency Virus-1, Strain: 426 c)</td>
      <td>WT_426 c_DS-SOSIP</td>
      <td>10.1016/j.cell .2016.07.029</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Human Immunodeficiency Virus-1, Strain: 426 c)</td>
      <td>426 c_G459C _DS-SOSIP_D3</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Human Immunodeficiency Virus-1, Strain: 426 c)</td>
      <td>426 c_WT_ gp120c_core</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Human Immunodeficiency Virus-1, Strain: 426 c)</td>
      <td>426 c_G459C _gp120c_core</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Human Immunodeficiency Virus-1, Strain: 426 c)</td>
      <td>426 c_S278A _gp120c_core</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Human Immunodeficiency Virus-1, Strain: 426 c)</td>
      <td>426 c_S278A_T462A _gp120c_core</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Human Immunodeficiency Virus-1, Strain: 426 c)</td>
      <td>426 c_S278A_T465A _gp120c_core</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Human Immunodeficiency Virus-1, Strain: 426 c)</td>
      <td>426 c_S278A_T462A_ T465A_gp120c_core</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Human Immunodeficiency Virus-1, Strain: 426 c)</td>
      <td>426 c_S278T_gp120c</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pTT3</td>
      <td>PMID: 11788735</td>
      <td></td>
      <td>https://biochimie.umontreal.ca/en/department/professors/yves-durocher/</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pVRC8400</td>
      <td>NIH</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Kifunensine</td>
      <td>Sigma-Aldrich</td>
      <td>CAS Number 109944-15-2</td>
      <td>https://www.sigmaaldrich.com/catalog/product/sigma/k1140?lang=en&amp;region=US&amp;gclid=Cj0KCQjwr53OBRCDARIsAL0vKrNtYwTyRzHU65HyVBwdntcP3kGpZ0ElVwYeSK3OcorLn0wf8U1iMQgaAssSEALw_wcB</td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Endoglycosidase-H</td>
      <td>New England Biolabs</td>
      <td>Catalog #P0702S</td>
      <td>https://www.neb.com/products/p0702-endo-h#Product%20Information</td>
    </tr>
  </tbody>
</table>

### Protein purification

HEK293S GnTI-/- and HEK293F cell lines were used for protein expression. Both cells lines were authenticated using STR profiling. Mycoplasma tests were performed using the MycoProbe kit from R and D Systems and the samples were negative for contamination.

#### 426c core†-VRC01GL

426c core†-VRC01GL was expressed using HEK293S GnTI-/- cells . Cells were cultured in suspension and transfected with equal parts of 426c G459C core, VRC01GL-A60CHC, and VRC01GL light chain plasmids (500 µg total/L) using 293 Free Transfection Reagent (Novagen). After 6 days, cells were centrifuged at 4,500 rpm for 20 min and supernatant was filter-sterilized. A His-tag on the Fab heavy chain was utilized for purification by suspending His60 Ni-Superflow Resin (Takata) in the supernatant at 4°C overnight. The Ni resin was washed with a solution of 150 mM NaCl, 20 mM Tris pH 8.0, 20 mM Imidazole pH 7.0 and eluted with a solution of 300 mM NaCl, 50 mM Tris pH 8.0, 250 mM Imidazole pH 7.0. The sample was further purified by Size-exclusion chromatography (SEC) using a HiLoad 16/600 Superdex 200 pg (GE) column removing non-specific proteins and excess Fab. Fractions containing the complex were concentrated and treated with an excess of EndoH for one hour at 37°C. The complex was then rerun over an SEC S200 column and concentrated to ~10 mg/mL for crystallization trials.

#### 426c DS-SOSIP D3†-VRC01GL

HEK293S GnTI-/- cells were transfected with 426c DS-SOSIP D3†, VRC01GL-A60C heavy chain, VRC01GL light chain and furin plasmids at a ratio of 3:1:1:1, as described above and previously (Stewart-Jones et al., 2016). Complexes were purified by the His-tag on the VRC01GL fragment as described above. Complexes were further purified on SEC as previously described and the peak containing both SOSIP and VRCO1GL were concentrated for cryoEM.

#### 426c DS-SOSIP variants

426c DS-SOSIP D3 (non-crosslinked G459 variant with C-terminal strep-his tag) was expressed using HEK293F cells by co-transfection of 426c DS.SOSIP D3 and furin plasmids at a 5:1 ratio. The cells were not tested for mycoplasma contamination. 426c DS-SOSIP D3 was purified first by Ni-affinity and then by Streptactin-affinity, followed by enzymatic digestion and separation of the cleaved tag from the trimer by SEC using a HiLoad 16/600 Superdex 200 pg (GE).

#### 426c core constructs

All 426c core constructs were expressed by the transfection protocol described above. Agarose Bound Galanthus Nivalis Lectin (Vector) was used to separate the cores from the supernatant. The resin was washed with 20 mM Tris pH 7.5, 100 mM NaCl, 1 mM EDTA and elution used a buffer containing 20 mM Tris pH 7.5, 100 mM NaCl, 1 mM EDTA, and 1M Methyl α-D-mannopyranoside. Samples were further purified by SEC using a HiLoad 16/600 Superdex 200 pg (GE) column.

#### Antibodies

All antibodies were expressed by the transfection protocol described above using equal ratios of heavy and light chain encoding plasmids. Protein A Agarose (Pierce) resin was used to separate IgG from the supernatant. Protein A beads were washed with phosphate buffer saline (PBS) and elution used a commercially available IgG elution buffer at pH 2.0 (Pierce). Samples were buffer exchanged into PBS.

### Biolayer interferometry

BLI assays were performed with an Octet Red 96 instrument (ForteBio, Inc, Menlo Park, CA) at 29°C with shaking at 500 r.p.m. All measurements were corrected by subtracting the background signal obtained from duplicate traces generated with an irrelevant negative control IgG or Fab. For standard BLI assays, IgGs were immobilized on anti-AHC biosensors (at 20 µg/ml in PBS), or Fabs on anti-human Fab-CH1 (FAB2G, ForteBio) biosensors (at 40 µg/ in PBS), for 240 s. Sensors were then incubated for 1 min in kinetic buffer (KB: 1X PBS, 0.01% BSA, 0.02% Tween 20% and 0.005% NaN3) to establish the baseline signal (nm shift). Antibody-loaded sensors were then immersed into solutions of purified recombinant samples for kinetic analysis. Analyses of DS-SOSIP trimers and 426c core constructs was performed by BLI using VRC01GL IgG and an extensive dilution series to determine accurate KD estimates. Samples expressed in the presence of 100 µM kifunensin and EndoH-digested were first buffer exchanged into PBS prior to dilution and kinetic analyses. Curve fitting to determine relative apparent antibody affinities for the samples was performed using a 1:1 binding model and the ForteBio data analysis software. Mean kon, koff, and KD values were determined by averaging all binding curves within a dilution series having R2 values of greater than 95% confidence level.

### Crystallization

Crystallization conditions for the 426c core†-VRC01GL were screened using a Mosquito (ttplabtech)-dispensing robot. Screening was done with Rigaku Wizard Precipitant Synergy block no. 2, Molecular Dimensions Proplex screen HT-96, and Hampton Research Crystal Screen HT using the vapor diffusion method. Initial crystals were further optimized with Hampton Research Additive Screen to grow large and well-diffracting crystals. Final crystals were grown in a solution of 0.09M MgCl2, 0.09M Na-Citrate pH 5.0, 13.5% PEG 4000, 0.1M LiCl2. Crystals were cryoprotected in solutions containing 30% molar excess of their original reagents and 20% glycerol. Crystals diffracted to 2.3 Å. Data was collected at ALS 5.0.2 and processed using HKL2000 (Otwinowski and Minor, 1997).

### Structure solution and refinement

The structure of 426c core†-VRC01GL Fab was solved through molecular replacement using Phaser in CCP4 (Collaborative Computational Project, Number 4, 1994). The structure was further refined with COOT (Emsley and Cowtan, 2004) and Phenix (Adams et al., 2010). The refinement statistics are summarized in Table 1.

### Negative-stain EM sample preparation

All 426c DS-SOSIP constructs in this study (3 µL) were negatively stained at a final concentration of 0.008 mg/mL using Gilder Grids overlaid with a thin layer of carbon and 2% uranyl formate as previously described (Veesler et al., 2014).

### Negative-Stain EM data collection and processing

Data were collected on an FEI Technai 12 Spirit 120kV electron microscope equipped with a Gatan Ultrascan 4000 CCD camera. A total of 150–300 images were collected per sample by using a random defocus range of 1.1–2.0 µm with a total exposure of 45 e−/A2. Data were automatically acquired using Leginon (Suloway et al., 2005), and data processing was carried out using Appion (Lander et al., 2009). The parameters of the contrast transfer function (CTF) were estimated using CTFFIND4 (Mindell and Grigorieff, 2003), and particles were picked in a reference-free manner using DoG picker (Voss et al., 2009). Particles were extracted with a binning factor of 2 after correcting for the effect of the CTF by flipping the phases of each micrograph with EMAN 1.9 (Ludtke et al., 1999). The 426c DS-SOSIP D3†-VRC01GL stack was pre-processed in RELION/2.1 (Kimanius et al., 2016; Scheres, 2012b; Scheres, 2012a) with an additional binning factor of 2 applied, resulting in a final pixel size of 6.4 Å. Resulting particles were sorted by reference-free 2D classification over 25 iterations. The best particles were chosen for 3D classification into six classes using RELION/2.1 (Kimanius et al., 2016). C3 symmetry was applied for 426c DS-SOSIP D3†-VRC01GL, with the best 3D classes refined further in RELION/2.1 (Kimanius et al., 2016) using the gold-standard approach.

### CryoEM sample preparation

We applied 2 μL of 0.7 mg/mL of DS-SOSIP D3†-VRC01GL in 10 mM HEPES pH 7.5, 50 mM NaCl, 0.085 mM dodecyl-maltoside to glow-discharged C-flat CF-1.2/1.3–4 C-T-grids. Vitrification was performed by using an FEI Vitrobot Mark IV, using a blot time of 6 s at a temperature of 22°C and 100% humidity.

### CryoEM data collection

Data collection was performed automatically using Leginon (Suloway et al., 2005) to control an FEI Titan Krios Electron Microscope equipped with a Gatan Quantum GIF energy filter and a K2 Summit direct electron detector(Li et al., 2013) operating in electron-counting mode spanning a random defocus range between 2.0 and 3.5 μm. Approximately 2000 micrographs were collected with a pixel size of 1.36 Å at a dose rate of 8 counts per pixel per second and 15 s acquisition time (0.2 frame per second), yielding a final measured dose of 43 e−/Å2 per movie.

### CryoEM data processing

Alignment of movie frames was carried out using MotionCor2 (Zheng et al., 2017) with a B-factor of −100 Å2 and an applied dose-weighting scheme of 0.95 electrons/Å2/frame. Omission of low-quality micrographs left a total of 1724 micrographs for downstream data processing. ~567,000 particles were picked in a reference-free manner using DoG picker (Voss et al., 2009). Global defocus and astigmatism were estimated using GCTF (Zhang, 2016) on the non-dose weighted aligned sums. Dose-weighted particles were binned to a final pixel size of 5.44 Å for an initial round of 2D classification using RELION/2.1 (Kimanius et al., 2016). 200,000 selected particles were re-centered, re-extracted, and unbinned to a final pixel size of 1.36 Å and subjected to 3D classification with RELION/2.1 (Kimanius et al., 2016) using the 30 Å low-pass filtered initial model generated from the DS-SOSIP D3†-VRC01GL negative-stain dataset. Out of the eight resulting classes, five classes contained well defined secondary structure elements and three bound Fabs. These classes were low-pass filtered to 20 Å and the best-resolved class was used as an initial model during 3D refinement using C3 symmetry. Refined angles for all particles were subsequently imported into FREALIGN (Grigorieff, 2016; Lyumkis et al., 2013a) and further refined with an applied particle weighting scheme. An additional iteration of refinement was performed by adjusting only the X/Y shifts. This refinement scheme resulted in a final estimated resolution of 3.8 Å for the three-Fab complex. The VRC01GL constant domains of the Fab were masked out during the final rounds of refinement and omitted from the final model due to the inherent flexibility of the elbow region (Stanfield et al., 2006). This same strategy was used for 3D classes of DS-SOSIP D3†-VRC01GL containing only two Fabs (C1 symmetry), leading to a final estimated resolution of 4.8 Å. Reported resolutions are based on the gold-standard FSC = 0.143 criterion. Local resolution estimates were generated using the ResMap software (Kucukelbir et al., 2014).

### Model building and refinement

We selected a clade A HIV-1 BG505 SOSIP.664 trimer (Stewart-Jones et al., 2016) and the 426c.TM1deltaV1-V3gp120 in complex with germline NIH46-46 (Scharf et al., 2016) as initial reference models for building 426c DS-SOSIP D3†-VRC01GL. This model was manually trimmed and edited using Coot (Emsley and Cowtan, 2004; Emsley et al., 2010) and RosettaES (Frenz et al., 2017). We then further refined the structure in Rosetta using density-guided protocols (Wang et al., 2016) for the 3.8 Å resolution C3 reconstruction. This process was repeated iteratively until convergence and high agreement with the map was achieved. The Fab constant domains were masked out during refinement and omitted from the final model. Following refinement of protein coordinates, identified N-linked glycans were manually docked into their corresponding density and refined using Rosetta (DiMaio et al., 2011; Frenz et al., 2018). Multiple rounds of minimization were performed on the complete glycoprotein model and manually inspected for errors. Throughout this process, we applied strict non-crystallographic symmetry constraints in Rosetta (DiMaio et al., 2011). The 4.8 Å asymmetric 426c DS-SOSIP D3†-VRC01GL structure bound to only two Fabs was obtained by removing one of the Fabs bound to the aforementioned model and was rigid-body docked into the 2 Fab-bound map using UCSF Chimera.. Mannose rings not supported by density in this map were manually trimmed. Final model quality was analyzed using Molprobity (Chen et al., 2010) and EM ringer (Barad et al., 2015). All figures were generated with UCSF Chimera (Pettersen et al., 2004).

### VRC01GL-based Immunoprecipitation

Purified recombinant VRC01GL IgG was covalently coupled to Dnyabeads MyOne Tosylactivated beads (Life Technologies), and immunoprecipitation using magnetic separation was carried out according to the manufacturer’s protocol. 5 mg of 426c core produced using HEK293S GnTI-/- cells were incubated with 100 μg of VRC01GL-beads for 15 min (first bind), after which the beads were removed and unbound material (flow through) was incubated with a second fresh 100 μg aliquot of VRC01GL-beads for an additional 15 min (second bind). VRC01GL-beads from first and second binding were washed 3x before acidic elution and pH neutralization of affinity-purified samples. Unbound material was further depleted by incubation with a third 100 μg of VRC01GL-beads, which were removed, before analysis. Samples of the original input 426c core, and VRC01GL-bound and unbound fractions were resolved by SDS gel electrophoresis under reducing conditions and the remainder subjected to LC-MS/MS analysis, as described above.

### Mass spectrometry

For analysis of N-linked glycosylation profiles, an estimated 250 pmol of each HIV-1 426c-based construct analyzed in this paper was denatured, reduced, and alkylated by dilution to 5 μM in 50 μL of buffer containing 100 mM Tris (pH 8.5), 10 mM Tris(2-carboxyethylphosphine (TCEP), 40 mM iodoacetamide or 40 mM iodoacetic acid, and 2% (wt/vol) sodium deoxycholate. Samples were first heated to 95°C for 10 min and then incubated for an additional 30 min at room temperature in the dark. The samples were digest with trypsin (Sigma Aldrich), by diluting 20 μL of sample to total volume of 100 μL 50 mM ammonium bicarbonate (pH 8.5). Protease was added to the samples in a ratio of 1:75 by weight and left to incubate at 37°C overnight. After digestion, 2 μL of formic acid was added to the samples to precipitate the sodium deoxycholate from the solution. After centrifugation at 17,000 × g for 25 min, 85 μL of the supernatant was collected and centrifuged again at 17,000 × g for 5 min to ensure removal of any residual precipitated deoxycholate. 80 μL of this supernatant was collected. For each sample, 8 μL was injected on a Thermo Scientific Orbitrap Fusion Tribrid mass spectrometer. A 35 cm analytical column and a 3 cm trap column filled with ReproSil-Pur C18AQ 5 μM (Dr. Maisch) beads were used. Nanospray LC-MS/MS was used to separate peptides over a 90 min gradient from 5% to 30% acetonitrile with 0.1% formic acid. A positive spray voltage of 2100 was used with an ion transfer tube temperature of 350°C. An electron-transfer/higher-energy collision dissociation ion-fragmentation scheme (Frese et al., 2013) was used with calibrated charge-dependent entity-type definition (ETD) parameters and supplemental higher-energy collision dissociation energy of 0.15. A resolution setting of 120,000 with an AGC target of 2 × 105 was used for MS1, and a resolution setting of 30,000 with an AGC target of 1 × 105 was used for MS2. Data were searched with the Protein Metrics Byonic software (Bern et al., 2012), using a small custom database of recombinant protein sequences including the proteases used to prepare the glycopeptides. Reverse decoy sequences were also included in the search. Specificity of the search was set to C-terminal cleavage at R/K (trypsin), allowing up to two missed cleavages, with EthcD fragmentation (b/y- and c/z-type ions). We used a precursor mass and product mass tolerance of 12 ppm and 24 ppm, respectively. Carbamidomethylation of cysteines was set as fixed modification, carbamidomethylation of the lysines and N-terminal amines were set as variable modifications, methionine oxidation as variable modification, pyroglutamate identification was set for both N-terminal glutamines and glutamates as a variable modification, and a concatenated N-linked glycan database (derived from the four software-included databases) was used to identify glycopeptides. All analyzed glycopeptide hits were manually inspected to ensure for quality and accuracy. Semi-quantitative LC-MS/MS of VRC01-based immunoprecipitation experiments were performed using Skyline (MacLean et al., 2010) with peak integration and LC-MS/MS searches imported from Byonic. Missed cleavages and post-translational modifications listed above for qualitative LC-MS/MS searches were included in the quantification of glycopeptides. All MS1 peak areas used for integration were manually inspected to ensure for quality and accuracy. Unbound fractions from two experimental replicates were pooled and injected as two technical replicates, whereas each ‘bound’ fraction (first bind and second bind) were performed as two experimental and two technical replicates each.
