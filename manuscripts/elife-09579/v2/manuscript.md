# Determining composition of micron-scale protein deposits in neurodegenerative disease by spatially targeted optical microproteomics

## Authors

- Kevin C Hadley<sup>1</sup>
- Rishi Rakhit<sup>2</sup>
- Hongbo Guo<sup>3</sup>
- Yulong Sun<sup>1</sup> ([ORCID: 0000-0002-6665-677X](https://orcid.org/0000-0002-6665-677X))
- James EN Jonkman<sup>4</sup>
- Joanne McLaurin<sup>5</sup>
- Lili-Naz Hazrati<sup>6</sup>
- Andrew Emili<sup>3</sup>
- Avijit Chakrabartty<sup>7</sup> †

### Affiliations

1. Department of Medical Biophysics, Princess Margaret Cancer Centre University of Toronto Toronto Canada
2. Department of Chemical and Systems Biology Stanford University Stanford United States
3. The Banting and Best Department of Medical Research, Terrence Donnelly Centre for Cellular & Biomolecular Research, Department of Molecular Genetics University of Toronto Toronto Canada
4. Advanced Optical Microscopy Facility, Princess Margaret Cancer Centre University Health Network Toronto Canada
5. Department of Laboratory Medicine and Pathobiology University of Toronto Toronto Canada
6. Tanz Centre for Research in Neurodegenerative Diseases, Department of Laboratory Medicine and Pathobiology University of Toronto Toronto Canada
7. Departments of Biochemistry and Medical Biophysics, Princess Margaret Cancer Centre University of Toronto Toronto Canada

† Corresponding author

## Abstract

Spatially targeted optical microproteomics (STOMP) is a novel proteomics technique for interrogating micron-scale regions of interest (ROIs) in mammalian tissue, with no requirement for genetic manipulation. Methanol or formalin-fixed specimens are stained with fluorescent dyes or antibodies to visualize ROIs, then soaked in solutions containing the photo-tag: 4-benzoylbenzyl-glycyl-hexahistidine. Confocal imaging along with two photon excitation are used to covalently couple photo-tags to all proteins within each ROI, to a resolution of 0.67 µm in the xy-plane and 1.48 µm axially. After tissue solubilization, photo-tagged proteins are isolated and identified by mass spectrometry. As a test case, we examined amyloid plaques in an Alzheimer's disease (AD) mouse model and a post-mortem AD case, confirming known plaque constituents and discovering new ones. STOMP can be applied to various biological samples including cell lines, primary cell cultures, ex vivo specimens, biopsy samples, and fixed post-mortem tissue.

## Introduction

Pathological protein deposits have a long history as hallmarks of neurodegenerative disease. Early methods used to identify these deposits include the silver stain introduced by Golgi (1873), and Virchow's iodine–sulfuric acid stain for starch (Virchow, 1854) that led to the coining of the term amyloid (Virchow, 1855). More specialized stains and labels have emerged which have begun to probe the structure and composition of pathological protein deposits. The stains Congo red and thioflavin S (ThS) were discovered later and remain in use (reviewed by Westermark (Sipe and Westermark, 2005) and Tanskanen (Tanskanen, 2013)), specifically identifying deposits containing a particular structural motif: amyloid β-pleated sheets. Beyond mere detection lies comprehensive identification of the protein components of these deposits; biochemical analyses of the deposits have produced transformative results in the field of neurodegeneration research. Two classic examples include the discovery of the prion protein and formulation of the protein-only hypothesis of prion disease (Bolton et al., 1982), and the discovery of the Alzheimer amyloid peptide (Aβ) (Glenner and Wong, 1984) and formulation of the amyloid cascade hypothesis of Alzheimer's disease (AD, reviewed by Musiek and Holtzman (Musiek and Holtzman, 2015)). More recently, there was the discovery that the RNA/DNA binding protein TDP-43 (transactive response DNA binding protein 43 kDa) is a significant component of ubiquitin-positive intraneuronal inclusions in certain cases of frontotemporal dementia (FTD) and amyotrophic lateral sclerosis (ALS) (Neumann et al., 2006). This discovery helped establish these diseases as spectrum disorders (Mackenzie, 2007), it led to the identification of TDP-43 mutations that are causative for ALS and FTD (Sreedharan et al., 2008) and established a role for RNA metabolism in ALS/FTD pathogenesis (Lagier-Tourenne and Cleveland, 2009; Mackenzie et al., 2010).

Identification of the protein components of pathological deposits has traditionally involved the partial biochemical purification of detergent-insoluble proteins present in a tissue specimen followed by protein sequencing. Immunohistochemical methods are then used to confirm that the identified proteins are bona fide constituents of the pathological deposits. These methods require large amounts of sometimes-scarce pathological tissue and identification of novel protein components can require increasingly elaborate, time-consuming, and costly protocols. For example, the discovery of TDP-43 in ubiquitin-positive intraneuronal inclusions required the generation of ∼1000 monoclonal antibodies, which were used to screen thousands of tissue sections by immunohistochemistry, to obtain a single monoclonal antibody that specifically labeled ubiquitin-positive intraneuronal inclusions (Neumann et al., 2006). That antibody was used for the proteomic identification of TDP-43 from the detergent-insoluble fraction of pathological tissue homogenates, and confirmatory staining with commercial TDP-43 antibodies was required for validation. In addition to being costly and labor intensive, another major limitation of biochemical purification of protein deposits is that soluble protein components associated with the core aggregates are likely to be lost during fractionation. Identifying deposit-associated soluble proteins could further our understanding of disease mechanisms.

A different strategy that can preserve some of the deposit-associated soluble proteins is laser capture microdissection (LCM), in which protein deposits are lifted intact out of sections of the fixed specimen; their protein compositions are then determined by mass spectrometry (Gozal et al., 2006). The resolution of LCM is ∼10 µm in the horizontal plane and captures the entire thickness of the tissue section along the vertical axis. Thus, for features smaller than ∼10 µm—such as inclusion bodies, small amyloid plaques, narrow fibers, and other irregularly shaped structures—LCM analysis permits enrichment but not complete isolation of target proteins; samples are diluted with extraneous surrounding material. For example, when capturing even a relatively large—3 μm in diameter—inclusion body with a single 10 µm LCM spot, only ∼10% of the recovered protein is from the pathology and 90% from the surrounding cellular milieu. LCM has nevertheless proven useful, however, in the proteomic analysis of systemic amyloidosis, where the amyloid deposits are very large and the feature size is typically ∼50,000 μm2 in area (Sethi et al., 2012, 2013).

Mass spectrometry imaging and its variants can also provide spatially resolved mass spectrometry analysis by directly coupling imaging with laser ablation and achieving 1 mm–10 μm resolution (Stoeckli et al., 2001; Wiseman et al., 2006; Wucher et al., 2007), but it is usually used to look for specific targets rather than in discovery mode.

Recently, proximity labeling techniques such as Bio-ID and APEX have provided high spatial resolution to mass spectrometry, and these techniques have been used to elucidate the composition of several difficult to purify organelles (Roux et al., 2012; Rhee et al., 2013; Firat-Karalar et al., 2014; Hung et al., 2014). However, proximity labeling relies on genetic manipulations to express an exogenous fusion protein to label adjacent components; this protein must be specifically and accurately targeted into a particular biological structure. Imperfect localization, especially in rare structures, results in selective labeling of neighbors outside of the target region yielding false positive associations.

Many of these approaches have been brought to bear on amyloid (senile) plaques in AD brain tissue, in an attempt to identify core components, if any, in addition to Aβ. Early LCM studies utilizing 2D gel electrophoresis coupled with mass spectrometry have detected a modest number of plaque-associated proteins, including an assortment of proteins associated with cell signaling, chaperone function, membrane trafficking, and proteolysis (Liao et al., 2004). A more recent LCM study has suggested that amyloid plaques in AD are highly homogenous structures that are composed almost exclusively of Aβ (Söderberg et al., 2006). The latter study, however, employed sample washing steps with 1% SDS, which may strip away soluble plaque-associated proteins. Finally, a recent attempt to capture more plaque-associated proteins potentially lost to LCM examined the sarkosyl-insoluble fraction of brain samples from patients with AD and appropriate controls (Gozal et al., 2009). Altered levels of eleven specific proteins were identified by this approach but colocalization with amyloid plaques was difficult to validate in many cases—not all insoluble proteins within the brain will necessarily originate from senile plaques. A recent proteomic analysis of fractions obtained from differential centrifugation procedures that yield fractions enriched in post-synaptic proteins have demonstrated that the post-synaptic protein IRSp53 was highly down-regulated in AD (Zhou et al., 2013). While extant LCM and biochemical fractionation studies have identified candidate plaque-associated proteins, significant mechanistic insights have not been produced.

We have developed a semi-automated technique called spatially targeted optical microproteomics (STOMP), which combines two-photon laser scanning microscopy with photochemical affinity labeling and mass spectrometry. While two-photon excitation has previously been used to drive microscopic, 3D-resolved photochemistry (Lee et al., 2008), STOMP represents the first application of this technique to affinity photolabeling, offering single-micron-scale three-dimensional resolution that is an order of magnitude better than the current state of the art LCM. In addition to providing clues to the etiology of neurodegenerative disease, this new proteomic technique also has great potential to advance research in cell biology by yielding the composition of small features that are not amenable to biochemical purification.

We sought to create an unbiased discovery technique that would: (1) have high spatial resolution, (2) target any identifiable or user-defined spatial region in a biological sample, (3) forgo the need for genetic modification, (4) have sufficient sensitivity to detect minor species within the sample, and (5) have sufficient specificity such that most hits can be readily validated as being enriched in the biological structure of interest. Because STOMP does not require genetic manipulation, this technique is applicable to a large variety of biological samples that run the gamut from cell lines, primary cell cultures, ex vivo specimens, human biopsy samples to fixed post-mortem human tissue.

## Results and discussion

### The STOMP technique

In STOMP, laser light from the microscope is used not only to image the fluorescently stained specimen, but also to photochemically crosslink affinity purification ligands to protein components within pathological deposits (Figure 1A). The photo-affinity ligand or photo-tag used here is a peptide of sequence: 4-benzoylbenzyl-Gly-His-His-His-His-His-His-CONH2 (6HisBP) (Figure 1B). Benzoylbenzene is a photoreactive group that forms covalent bonds with C–H and N–H groups upon excitation. The 6HisBP photo-tag molecule (molecular mass, 1105 Da) is of similar size to Congo red (molecular mass, 697 Da) and should have a similar ability to penetrate biological specimens. The specimen is fixed and permeabilized in methanol, then protein deposits in the specimen are selectively stained using antibodies or specific fluorescent dyes. The specimen is then soaked in a solution of 6HisBP to saturate the subcellular compartments with the photo-tag, and imaged using conventional confocal microscopy. The wavelength of the confocal laser is in the visible range and does not excite the UV-absorbing photo-tag. Optical sectioning by confocal microscopy is used to collect a 3D image of the protein deposits in the specimen. This image in turn is used to generate a list of spatial coordinates—a ‘mask’ file—identifying every point in the tissue containing pathological protein deposits (Figure 1C).

![Figure 1.](https://cdn.elifesciences.org/articles/09579/elife-09579-fig1-v2.jpg)

**Figure 1.:** (A) Schematic diagram comparing volumes selected for excision by laser capture microdissection (LCM) (yellow cylinder) and spatially targeted optical microproteomics (STOMP) (blue volume). The STOMP excitation volume is limited approximately to the point spread function of a high numerical aperture lens (<1 µm in the xy plane, ∼1.0 µm axially) compared to ∼10 µm for LCM. (B) Structure of the bifunctional photocrosslinker used in this study; the affinity purification hexahistidine peptide is highlighted in blue, the photocrosslinker benzophenone group is highlighted in yellow. (C) Overview of the STOMP protocol. Tissue sections or cells are first fixed in cold methanol and stained using specific dyes or antibodies. (1) A guide image is acquired at a wavelength that does not activate the photocrosslinker. (2) The guide image is converted to a digital mask that directs the two-photon laser. (3) Two-photon laser selectively illuminates region of interest. The final image shown is anti-His tag immunofluorescence corresponding to areas of photo-tag crosslinking. (D) Silver stain of SDS-PAGE of material retrieved from selective STOMP of CRND8 mouse plaques (left panel) or non-plaque regions of an adjacent brain section (right panel). In each case the control (‘con’) is non-specific binding to Ni2+-NTA agarose beads. Load is 1% of total protein after solubilization of tissue. Note that the predominant protein photo-tagged in the STOMP sample is Aβ (arrow), which is not visible in the non-plaque experiment because of its low overall abundance.

The photo-tagging procedure uses two-photon microscopy (Skoch et al., 2006) rather than conventional confocal microscopy. Two-photon microscopy can excite a small volume (<1 µm3, Figures 1A and Figure 2) anywhere in the specimen, while conventional confocal microscopy excites a continuous cone that spans the entire thickness of the specimen, which would result in the covalent attachment of the photo-tag to off-target regions. A custom software macro was written that reads the mask file and selectively delivers two-photon excitation light to each protein deposit present, while leaving the remainder of the specimen untouched by excitation light (the custom macro is available as Source code 1). The STOMP macro provides a semi-automated tool for photo-tagging proteins in pathological deposits. Importantly, unlike LCM, no manual tracing of features is required with STOMP.

![Figure 2.](https://cdn.elifesciences.org/articles/09579/elife-09579-fig2-v2.jpg)

**Figure 2.:** A single voxel in a TgCRND8 tissue section was photo-tagged. The volume of photo-excitation was measured by confocal fluorescence imaging of the resulting photo-tagged spot. Maximum-intensity projections of the xy- (A, B) and xz- (C) planes are shown. Scale bar 1 µm. Fluorescence profiles of the indicated regions (shaded yellow) are shown (D–F). The width of the peaks is 0.67 µm in x and y, and 1.48 µm along the z axis, corresponding to an ellipsoidal excited volume of 0.38 µm3.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/09579/elife-09579-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Cross correlation of spectral counts for all protein identifications are shown for duplicate runs of STOMP analysis on human amyloid plaque material.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/09579/elife-09579-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Biological replicates of STOMP analysis of amyloid plaque material from TgCRND8 mice show good repeatability. Using our thresholding criteria (at least three spectral counts for each identified protein, at least threefold excess over corresponding dark control) one sample run (P1) identified fewer total proteins than the other (P2), however most proteins identified in P1 were also detected in P2.

We rely on reversible binding of photo-tagged proteins using nickel affinity chromatography. Histidine-rich proteins ubiquitous in all mammalian tissues represent potential contaminants that could bind the nickel affinity beads and confound the STOMP analysis. To circumvent this problem, the first step of the procedure involves limited treatment of the tissue sections with dilute diethyl pyrocarbonate (DEPC). DEPC covalently modifies histidyl residues that abolishes their ability to bind nickel (Wallis and Holbrook, 1973).

After completion of the photo-tagging step, the specimen is solubilized in buffer containing 2% SDS, 8 M urea, and β-mercaptoethanol (β-ME). The photo-tagged proteins are purified using nickel affinity beads that bind the hexahistidyl moiety of 6HisBP. The purified proteins are then analyzed by gel electrophoresis (Figure 1D) and identified by database searching spectra from peptides resulting from digestion and liquid-chromatography and tandem mass spectrometry (LC-MS/MS).

### The resolution of STOMP

To establish the spatial resolution limits of our photo-tagging procedure, we tagged single-voxel spots within sections of methanol-fixed murine brain tissue. By subsequently staining the tissue with an anti-hexahistidine antibody, we were able to use confocal immunofluorescence imaging to directly visualize and measure the extent of the photo-tagged volume.

We measured the diameter (full width at half-maximum, FWHM) of the phototagged volume at 0.67 µm along the x and y axes, and 1.48 µm along the z axis (Figure 2). Taking the excited region to be an ellipsoid, the total volume of a single spot is 0.38 µm3.

### STOMP analysis of amyloid plaques in a transgenic mouse model of AD

We used TgCRND8 mice, a well-characterized transgenic mouse model of AD (Chishti et al., 2001), as a model system for the development of the STOMP technique. These mice express a human form of the amyloid precursor protein carrying two mutations associated with familial AD, and they produce amyloid plaques and exhibit spatial learning impairments by 3 months of age. This study used frozen sections (post-fixed in methanol) of the brains known to contain plaques, from TgCRND8 mice of 8 months of age.

Sets of serial sections on separate slides were treated with DEPC, stained with ThS, and soaked in a solution of 6HisBP. Slides were imaged by confocal microscopy to identify ThS-positive amyloid deposits. Confocal images of ThS-positive amyloid deposits (Figure 1C1) were used to construct individual masks (Figure 1C2). Because our technique hinges on selective photolabeling and purification, we needed to assess the extent of non-specific labeling of 6HisBP in ambient light and under immunofluorescence excitation, as well as non-specific binding to affinity purification beads. Adjacent sections were put aside as ‘dark’ controls used to assess the extent of non-specific labeling of 6HisBP to proteins caused by confocal laser light (488 nm) exposure or other handling, and to assess nonspecific binding of proteins to nickel affinity beads.

The STOMP macro was used to deliver two-photon excitation light to regions of the specimen corresponding to each pixel in the mask image. This excitation light has two effects. First, and most importantly, it photo-activates 6HisBP molecules that are in the amyloid deposits causing photo-tagging of constituent proteins. Second, it serendipitously photo-bleaches the ThS fluorophores present in regions of the specimen targeted by the mask. Immunofluorescence staining of the tissue section with anti-His6 antibody after photo-activation superimposes on the digital mask, thus highlighting the very high accuracy of targeting of the two-photon laser (Figure 1C3). STOMP combines microscopy with selective photo-labeling to accurately resolve, capture, and affinity-label highly irregular shaped micron-scale structures, via a semi-automated procedure.

After solubilization of the specimen, the photo-tagged proteins were bound to nickel affinity beads. Each sample was divided into two portions: one used for mass spectrometry (Table 1) and one for gel electrophoresis and silver staining (Figure 1D). The dark control sample, which—aside from two-photon excitation—was treated identically to the STOMP sample, was run alongside the STOMP sample. It shows very few bands in the silver-stain gel from material bound to the nickel-nitrilotriacetic acid (Ni-NTA) beads compared to the STOMP sample, confirming that nonspecific photo-tagging and nonspecific binding of proteins to the nickel affinity beads is minimal. In addition to a number of proteins ranging in molecular weight from 20 kDa to >250 kDa, the STOMP sample contains large amounts of a low molecular weight protein that was subsequently identified as Aβ (4.5 kDa) (Figure 1D).

**Table 1.**
 Proteins statistically significantly enriched in the amyloid plaques of TgCRND8 mouse brain identified and retrieved by STOMP


<table>
  <thead>
    <tr>
      <th>Protein</th>
      <th>Uniprot ID</th>
      <th>STOMP counts</th>
      <th>SAINT score</th>
      <th>Previous reports of enrichment in plaques (Söderberg et al., 2006)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Amyloid beta A4 protein</td>
      <td>P12023</td>
      <td>378</td>
      <td>0.83</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Synaptosomal-associated protein 25</td>
      <td>P60879</td>
      <td>88</td>
      <td>1.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Cytochrome c1</td>
      <td>Q9D0M3</td>
      <td>70</td>
      <td>0.98</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Excitatory amino acid transporter 2</td>
      <td>P43006</td>
      <td>64</td>
      <td>1.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>V-type proton ATPase subunit B</td>
      <td>P62814</td>
      <td>56</td>
      <td>0.80</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Vesicle-associated membrane protein 2</td>
      <td>P63044</td>
      <td>52</td>
      <td>0.87</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Pyruvate kinase isozymes M1/M2</td>
      <td>P52480</td>
      <td>49</td>
      <td>0.98</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Fructose-bisphosphate aldolase A</td>
      <td>P05064</td>
      <td>47</td>
      <td>1.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Cytochrome b-c1 complex subunit 1</td>
      <td>Q9CZ13</td>
      <td>47</td>
      <td>0.92</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Guanine nucleotide-binding protein G(o) subunit alpha</td>
      <td>P18872</td>
      <td>41</td>
      <td>0.98</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Cytochrome c oxidase subunit 2</td>
      <td>P00405</td>
      <td>40</td>
      <td>0.97</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Tubulin alpha-1B chain</td>
      <td>P05213</td>
      <td>39</td>
      <td>0.98</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>4-aminobutyrate aminotransferase</td>
      <td>P61922</td>
      <td>39</td>
      <td>0.81</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Tubulin beta-3 chain</td>
      <td>Q9ERD7</td>
      <td>38</td>
      <td>1.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>V-type proton ATPase catalytic subunit A</td>
      <td>P50516</td>
      <td>37</td>
      <td>0.99</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Aralar 1</td>
      <td>Q8BH59</td>
      <td>37</td>
      <td>1.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Citrate synthase, mitochondrial</td>
      <td>Q9CZU6</td>
      <td>37</td>
      <td>1.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Clathrin heavy chain 1</td>
      <td>Q68FD5</td>
      <td>35</td>
      <td>1.00</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Alpha-internexin</td>
      <td>P46660</td>
      <td>30</td>
      <td>0.98</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>NADH dehydrogenase 1 alpha subcomplex subunit 9, mitochondrial</td>
      <td>Q9DC69</td>
      <td>30</td>
      <td>0.98</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Fructose-bisphosphate aldolase C</td>
      <td>P05063</td>
      <td>28</td>
      <td>0.91</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Synapsin-2</td>
      <td>Q64332</td>
      <td>27</td>
      <td>0.89</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Dynamin-1</td>
      <td>P39053</td>
      <td>26</td>
      <td>0.99</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>NADH dehydrogenase 1 alpha subcomplex subunit 10, mitochondrial</td>
      <td>Q99LC3</td>
      <td>24</td>
      <td>0.89</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Spectrin alpha chain, brain</td>
      <td>P16546</td>
      <td>22</td>
      <td>1.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Succinate dehydrogenase flavoprotein subunit, mitochondrial</td>
      <td>Q8K2B3</td>
      <td>21</td>
      <td>0.99</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Synapsin-1</td>
      <td>O88935</td>
      <td>20</td>
      <td>0.97</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Rab GDP dissociation inhibitor alpha</td>
      <td>P50396</td>
      <td>20</td>
      <td>0.94</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>V-type proton ATPase 116 kDa subunit a</td>
      <td>Q9Z1G4</td>
      <td>19</td>
      <td>0.98</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Hexokinase-1</td>
      <td>P17710</td>
      <td>18</td>
      <td>1.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Heat shock protein HSP 90-alpha</td>
      <td>P07901</td>
      <td>18</td>
      <td>0.93</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Ubiquitin thioesterase OTUB1</td>
      <td>Q7TQI3</td>
      <td>18</td>
      <td>0.85</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Vesicle-fusing ATPase</td>
      <td>P46460</td>
      <td>17</td>
      <td>0.88</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Spectrin beta chain, brain 1</td>
      <td>Q62261</td>
      <td>17</td>
      <td>1.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>NADH-ubiquinone oxidoreductase 75 kDa subunit, mitochondrial</td>
      <td>Q91VD9</td>
      <td>16</td>
      <td>0.95</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Neurofilament light polypeptide</td>
      <td>P08551</td>
      <td>15</td>
      <td>0.85</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Neurochondrin</td>
      <td>Q9Z0E0</td>
      <td>15</td>
      <td>0.97</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Heat shock protein HSP 90-beta</td>
      <td>P11499</td>
      <td>14</td>
      <td>0.98</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Na/K-transporting ATPase subunit alpha-2</td>
      <td>Q6PIE5</td>
      <td>14</td>
      <td>0.95</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Excitatory amino acid transporter 1</td>
      <td>P56564</td>
      <td>14</td>
      <td>0.93</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Microtubule-associated protein 6</td>
      <td>Q7TSJ2</td>
      <td>13</td>
      <td>0.87</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Serine/threonine-protein phosphatase 2A 65 kDa regulatory subunit A alpha isoform</td>
      <td>Q76MZ3</td>
      <td>11</td>
      <td>0.80</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Catenin beta-1</td>
      <td>Q02248</td>
      <td>11</td>
      <td>0.83</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Tenascin-R</td>
      <td>Q8BYI9</td>
      <td>10</td>
      <td>0.85</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Alpha-actinin-1</td>
      <td>Q7TPR4</td>
      <td>10</td>
      <td>0.98</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Ubiquitin-like modifier-activating enzyme 1</td>
      <td>Q02053</td>
      <td>9</td>
      <td>0.93</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Pyruvate carboxylase, mitochondrial</td>
      <td>Q05920</td>
      <td>9</td>
      <td>0.92</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Ankyrin-2</td>
      <td>Q8C8R3</td>
      <td>2</td>
      <td>0.85</td>
      <td>Detected, not enriched</td>
    </tr>
  </tbody>
</table>

_Table is sorted in descending order of abundance, by normalized spectral counts._

As an additional control, an entire brain section fixed in methanol and soaked with photo-tag was photo-activated by exposure to 365 nm ultraviolet light. Section-wide photo-activation of this specimen caused indiscriminate photo-tagging of proteins in the specimen. Gel electrophoresis of the indiscriminately photo-tagged proteins reveals a very different pattern of protein bands compared to the specimen in which amyloid plaques were specifically targeted for STOMP analysis (Figure 1D).

### Identification of photo-tagged amyloid plaque proteins by mass spectrometry

The total volume of tissue that needs to be photo-tagged to obtain sufficient material for mass spectrometry analysis is a subjective matter and also depends on instrument sensitivity, fixation method used, sample complexity and perhaps other factors. Greater amounts of tissue will increase sensitivity and enable identification of lower abundance proteins, particularly in very complex samples containing a large number of unique proteins. In this study, we were able to identify proteins present in relative abundance in the pathological feature being examined using a total photo-tagged volume of approximately 2 × 106 µm3. (This corresponds to a photo-tagged region of 500 µm × 500 µm in an 8-µm thick tissue section or a cube of photo-tagged tissue 130 μm on a side.) Lowering the stringency will increase the number of hits but may introduce more false positives. Two frozen sections of TgCRND8 brain tissue were sufficient to produce the necessary volume of photo-tagged tissue required for one STOMP experiment, and the process required a total of 12–16 hr of microscope time per sample (6–8 hr per section).

Based on our determination of the resolution of STOMP, regions of interest (ROIs) as small as 0.38 µm can be analyzed (Figure 2). To analyze such small features, however, sufficient numbers of ROIs must be captured, and this may necessitate pooling photo-tagged material from several tissue sections.

Protein identification via mass spectrometry involved on-bead digestion of the photo-tagged proteins with endoproteinase Lys-C followed by trypsin and LC-MS/MS analysis. We performed technical and biological replicates of the proteomic analyses of our STOMP experiment. The technical replicates (Figure 2—figure supplement 1) demonstrate a very high degree of correlation (r2 = 0.98), and the biological replicates demonstrate significant overlap in proteins identified (Figure 2—figure supplement 2). The replicate studies illustrate the high reproducibility of the technique. The list of all identified proteins in amyloid plaques of TgCRND8 mice based on our high stringency criteria is summarized in Table 1.

The aim of STOMP is to provide a compendium of annotated proteins present within the ROI under study—whether or not they are enriched or depleted relative to the surrounding tissue. As regards the quantitative nature of the data, Table 1 collects and summarizes our high-confidence mass spectrometry protein identifications, sorted by molecular-weight-normalized spectral counts: a semi-quantitative proxy for protein abundance. As expected, the most abundant protein found in STOMP from TgCRND8 mouse plaques was Aβ (Figure 1D, Table 1). In addition to Aβ, we identified 454 proteins in at least one of two biological replicates (Supplementary file 1). Combining our biological and technical replicates with our negative controls (‘dark’ samples and replicates), we used the Significance Analysis of INTeractome (SAINT) algorithm (Choi et al., 2011), which uses Bayesian inference to assign a probability of a true interaction, using Aβ as the bait protein. We found 62 proteins with probability >0.8 of being found associated with the plaques, and 146 with probability >0.5 (Supplementary file 1). Among these, synaptosomal proteins were highly enriched, including SNAP25, vesicle-associated membrane protein 2 (VAMP2), vesicular proton pump ATPase (v-ATPase), and synapsins 1 and 2. Apolipoprotein E, which is sometimes associated with senile plaques (Thal et al., 1997), was also detected, albeit at a SAINT score of 0.70 (Supplementary file 1). Certain common synaptic markers—including chromogranin A/C, synaptophysin, synaptogyrin I, synaptoporin, α-synuclein, and VGLUT1 and 2—were not detected in the plaques. Interestingly, the plaques were also devoid of uniquely post-synaptic proteins. We also identified many mitochondrial proteins; although the reason for this is unclear, it may be that the intrinsic hydrophobicity of mitochondrial membrane proteins may predispose them to associate with amyloid plaques. Comparison with proteins found from STOMP analysis of non-plaque areas revealed only limited overlap (Supplementary file 2); VAMP2, synapsin 1, and dynamin 1 are present in both plaque and non-plaque STOMP analysis but are significantly greater enriched in the plaque STOMP samples.

### Validation of the STOMP results in TgCRND8 mice with immunofluorescence and immunohistochemistry

Using confocal microscopy, we examined colocalization of ThS-positive plaques with immunfluorescently labeled Aβ, SNAP25, VAMP2, v-ATPase, synapsin 1, and ApoE. All were found to be present and are apparently genuine components of the amyloid plaque (Figure 3). Optical sectioning demonstrates the presence of each of these proteins in the core of the amyloid plaques suggesting they were incorporated at the earliest stages of plaque formation. Staining of SNAP25, VAMP2, and v-ATPase reveal an immunopositive halo surrounding each of the plaques indicating an accumulation of these proteins not only in the amyloid core but also in the vicinity of the plaques; interestingly, synapsin 1 immunostaining did not have this halo.

![Figure 3.](https://cdn.elifesciences.org/articles/09579/elife-09579-fig3-v2.jpg)

**Figure 3.:** Colocalization of ThS-stained plaques with beta-amyloid positive control (A, G, M) and the synaptic proteins ATP6V1B2 (B, H, N), SNAP25 (C, I, O), VAMP2 (D, J, P), synapsin 1 (E, K, Q), and ApoE (F, L, R). ATP6V1B2, SNAP25, and VAMP2 (N–P) all show a halo of elevated protein concentration in the region surrounding the dense core of the plaque. Scale bar 50 µm, 20 µm in the ApoE panels.

As mentioned above, certain common synaptic markers were not detected by the STOMP analysis. Immunostaining of some of these markers, syntaxin 1, synaptophysin, and α-synuclein, confirmed that these proteins are not concentrated in the amyloid plaques (Figure 4). α-Synuclein has been reported to be associated with senile plaques in human patients with AD; however, TgCRND8 mice are known to not accumulate α-synuclein in their plaques (Xu et al., 2002).

![Figure 4.](https://cdn.elifesciences.org/articles/09579/elife-09579-fig4-v2.jpg)

**Figure 4.:** The SNARE protein syntaxin-1 (A), synaptic marker synaptophysin (B), the neuronal protein alpha-synuclein (C) are absent from ThS-positive plaques (G, H, I, M, N, O). Staining of the glial protein GFAP (D) surrounds the ThS-positive plaques but does not infiltrate the plaque core (J, P). Scale bar 50 µm.

It is not clear why the amyloid deposits contain some pre-synaptic proteins, but not others, and are devoid of post-synaptic proteins. One possibility is that damaged dystrophic neurites that are known to surround the plaques (Chishti et al., 2001) are spilling their contents and the physical properties of certain pre-synaptic proteins cause them to bind with especially high affinity to amyloid plaques. In this regard, it is noteworthy that many of these proteins are membrane proteins with coiled coil domains (Takamori et al., 2006). Another possibility, which is not mutually exclusive and provides an explanation for the presence of pre-synaptic proteins in plaques, is that Aβ fibrils and/or oligomers bind directly to synaptic vesicles and interfere with synaptic function. Evidence for a damaging effect of Aβ on synapses and dendrites has been available for some time (Mattson et al., 1998). Diffusible Aβ oligomers added to cultured primary neurons have been shown to associate with synaptosomes and a concomitant synaptic deterioration is observed (Lacor et al., 2007). In post-mortem AD tissue and in transgenic AD mice, an inverse correlation between levels of Aβ oligomers and levels of synaptic proteins was noted (Pham et al., 2010). The reduction in the levels of detectable synaptic protein in AD tissue may be the result of the aggregation and entrapment of the synaptic proteins in the amyloid plaques. In sum, the STOMP technique has provided clear evidence of interaction of amyloid plaques with pre-synaptic proteins.

### STOMP analysis of senile plaques from post-mortem AD brain

After developing the STOMP method using brain sections of TgCRND8 mice as the test subject, we applied the technique to senile plaques from a case of AD. Human tissue is inherently more difficult to work with than animal tissue because of biochemical changes associated with post-mortem degradation. Furthermore, formalin, the fixative of choice for human tissue, causes covalent modification of proteins and confounds mass spectrometry analysis. These limitations notwithstanding, we find the STOMP technique is suitable for the analysis of formalin-fixed post-mortem human tissue. Senile plaques from brain sections of a severe case of AD were visualized with ThS and photo-tagged using a procedure identical to that used for the TgCRND8 tissue. Mass spectrometry analysis of the protein composition of these senile plaques identified 60 proteins that were statistically significantly enriched, with Aβ being the most abundant protein component (Table 2). Synaptic proteins and proteins involved in synaptic vesicle transport comprised 15% of the abundant protein component of the plaques. For validation of the STOMP analysis of senile plaques, immunofluorescence staining was employed, revealing that GFAP and SNAP25 were detected by both immunofluorescence, while tau and α-synuclein were not detected by either technique (Figure 5).

**Table 2.**
 Proteins statistically significantly enriched in senile plaques from a patient with AD identified and retrieved by STOMP


<table>
  <thead>
    <tr>
      <th>Protein</th>
      <th>Uniprot ID</th>
      <th>STOMP counts</th>
      <th>Dark counts</th>
      <th>Previous reports of enrichment in plaques (Söderberg et al., 2006)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Amyloid beta A4 protein</td>
      <td>P05067</td>
      <td>898</td>
      <td>0.00</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Tubulin alpha-1A chain</td>
      <td>Q71U36</td>
      <td>39.4</td>
      <td>1.99</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Tubulin beta-2A chain</td>
      <td>Q13885</td>
      <td>23.0</td>
      <td>3.51</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Actin, cytoplasmic 1</td>
      <td>P60709</td>
      <td>13.8</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Glial fibrillary acidic protein</td>
      <td>P14136</td>
      <td>11.0</td>
      <td>0.00</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Alpha-internexin</td>
      <td>Q16352</td>
      <td>10.8</td>
      <td>0.90</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Synaptosomal-associated protein 25</td>
      <td>P60880</td>
      <td>9.65</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Carbonyl reductase [NADPH] 1</td>
      <td>P16152</td>
      <td>9.05</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>ATP synthase subunit beta, mitochondrial</td>
      <td>P06576</td>
      <td>9.28</td>
      <td>0.00</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Tubulin polymerization-promoting protein</td>
      <td>O94811</td>
      <td>6.33</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Tubulin beta-3 chain</td>
      <td>Q13509</td>
      <td>5.95</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Cytochrome b-c1 complex subunit 8</td>
      <td>O14949</td>
      <td>5.05</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Calcium/calmodulin-dependent protein kinase type I</td>
      <td>Q9UQM7</td>
      <td>5.08</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Immunoglobulin superfamily member</td>
      <td>Q969P0</td>
      <td>4.23</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>V-type proton ATPase subunit B, kidney isoform</td>
      <td>P15313</td>
      <td>3.96</td>
      <td>0.00</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Vesicle-associated membrane protein 2</td>
      <td>P63027</td>
      <td>3.95</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Pyruvate dehydrogenase E1 component subunit beta</td>
      <td>P11177</td>
      <td>3.82</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Fructose-bisphosphate aldolase C</td>
      <td>P09972</td>
      <td>3.80</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Ferritin light chain</td>
      <td>P02792</td>
      <td>3.75</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Neurofilament heavy polypeptide</td>
      <td>P12036</td>
      <td>3.33</td>
      <td>0.89</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Cytochrome c1, heme protein, mitochondrial</td>
      <td>P08574</td>
      <td>2.82</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Peptidyl-prolyl cis-trans isomerase</td>
      <td>Q13526</td>
      <td>2.74</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Phosphoglycerate mutase 1</td>
      <td>P18669</td>
      <td>2.60</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Beta-actin-like protein 2</td>
      <td>Q562R1</td>
      <td>2.38</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Creatine kinase B-type</td>
      <td>P12277</td>
      <td>2.34</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Transketolase</td>
      <td>P29401</td>
      <td>2.21</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Alpha-enolase</td>
      <td>P06733</td>
      <td>2.12</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Excitatory amino acid transporter 1</td>
      <td>P43003</td>
      <td>2.10</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>40S ribosomal protein S8</td>
      <td>P62241</td>
      <td>2.07</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>60 kDa heat shock protein, mitochondrial</td>
      <td>P10809</td>
      <td>2.05</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Stress-70 protein, mitochondrial</td>
      <td>P38646</td>
      <td>2.04</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Protein SERCA1</td>
      <td>Q96JX3</td>
      <td>2.02</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Spectrin beta chain, brain 1</td>
      <td>Q01082</td>
      <td>1.82</td>
      <td>0.00</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Fascin</td>
      <td>Q16658</td>
      <td>1.83</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>6-phosphogluconolactonase</td>
      <td>O95336</td>
      <td>1.82</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Thioredoxin-dependent peroxide reductase</td>
      <td>P30048</td>
      <td>1.81</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Glutamine synthetase</td>
      <td>P15104</td>
      <td>1.78</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Clathrin heavy chain 1</td>
      <td>Q00610</td>
      <td>1.70</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Elongation factor Tu, mitochondrial</td>
      <td>P49411</td>
      <td>1.51</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Tubulin alpha-4A chain</td>
      <td>P68366</td>
      <td>1.50</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Methionine adenosyltransferase 2 subunit beta</td>
      <td>Q9NZL9</td>
      <td>1.33</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Dihydropyrimidinase-related protein 4 i</td>
      <td>O14531</td>
      <td>1.21</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Tenascin-R</td>
      <td>Q92752</td>
      <td>1.17</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Microtubule-associated protein 6</td>
      <td>Q96JE9</td>
      <td>1.16</td>
      <td>0.29</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Prelamin-A/C</td>
      <td>P02545</td>
      <td>1.01</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Neurofascin</td>
      <td>O94856</td>
      <td>1.00</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Protein kinase C and casein kinase substrate</td>
      <td>Q9BY111</td>
      <td>0.98</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Hexokinase-1</td>
      <td>P19367</td>
      <td>0.98</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>NADH-ubiquinone oxidoreductase 75 kDa subunit</td>
      <td>P283311</td>
      <td>0.94</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Coronin-1C</td>
      <td>Q9ULV4</td>
      <td>0.94</td>
      <td>0.00</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Fumarate hydratase, mitochondrial</td>
      <td>P07954</td>
      <td>0.91</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>Serine/threonine-protein kinase PAK 1</td>
      <td>Q13153</td>
      <td>0.82</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>V-type proton ATPase 116 kDa subunit a isoform 1</td>
      <td>Q93050</td>
      <td>0.78</td>
      <td>0.00</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Contactin-associated protein 1</td>
      <td>P78357</td>
      <td>0.64</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Ubiquitin-like modifier-activating enzyme 1</td>
      <td>P22314</td>
      <td>0.64</td>
      <td>0.00</td>
      <td>Previously unreported</td>
    </tr>
    <tr>
      <td>ATP-citrate synthase</td>
      <td>P53396</td>
      <td>0.62</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Heat shock protein HSP 90-alpha</td>
      <td>P07900</td>
      <td>0.59</td>
      <td>0.00</td>
      <td>Detected, enriched</td>
    </tr>
    <tr>
      <td>Aconitate hydratase, mitochondrial</td>
      <td>Q99798</td>
      <td>0.58</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Spectrin alpha chain, brain</td>
      <td>Q13813</td>
      <td>0.44</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
    <tr>
      <td>Microtubule-associated protein 1B</td>
      <td>P46821</td>
      <td>0.37</td>
      <td>0.00</td>
      <td>Detected, not enriched</td>
    </tr>
  </tbody>
</table>

_Table is sorted in descending order of abundance, by normalized spectral counts._

![Figure 5.](https://cdn.elifesciences.org/articles/09579/elife-09579-fig5-v2.jpg)

**Figure 5.:** Immunofluorescent confirmation of results of STOMP analysis of senile plaques in a case of AD. GFAP (A), a marker of glial cells, surrounds the ThS-positive plaques and partially infiltrates the plaque core (E, I). Tau in dystrophic neurites (B) surrounds the ThS-positive plaques but does not infiltrate the plaque core (F, J). α-synuclein (C) is absent from ThS-positive plaques (G, K). SNAP25 colocalizes with ThS-positive plaques in thiscase of AD (D, H, L). Scale bar is 20 μm.

Gliosis is a well-known feature of AD, and reactive glial cells are often found surrounding amyloid plaques (Mandybur and Chuirazzi, 1990; Sofroniew and Vinters, 2010). Glial proteins, GFAP and excitatory amino acid transporter (EAAT) (Anderson and Swanson, 2000), were both detected in (human) senile plaques (Table 2); however, only EAAT was detected in TgCRND8 amyloid plaques (Table 1). This apparent discrepancy is likely due to astrocytes being more intimately associated with amyloid plaques in human tissue (Figure 5A,E,I) compared to plaques in the TgCRND mouse (Figure 4D,J,P). Tau protein was also not among the abundant plaque proteins. Immunofluorescence staining shows that tau, which is contained in dystrophic neurites that surround the plaques, do not occupy the same physical space as the plaques and were hence not detected in the STOMP analysis (Figure 3B,H,N). SNAP25, on the other hand, was detected in the STOMP analysis and was seen to colocalize with senile plaques (Figure 5D,H,L) and amyloid plaques from TgCRND8 mice (Figure 3C,I,O). α-synuclein is part of the NAC (non-amyloid components) of plaques—with a possible role in fibril formation but not part of the plaque core (Culvenor et al., 1999; Wirths and Bayer, 2003). These proteins were found not to be enriched in the plaques of this case of AD as detected by both STOMP analysis (Table 2) or by immunofluorescent staining (Figure 5C,G,K).

Immunohistochemical staining of pre-synaptic proteins, SNAP25, VAMP2, and synaptophysin in senile plaques from human patients with AD was similar to the immunofluoresence staining in the AD mice, with some notable differences (Figure 6). Senile plaques in the human AD tissue were positive for both SNAP25 and VAMP2. However, synaptophysin staining, which was absent in the amyloid deposits of AD mice, displayed a unique punctate lobular profile that decorated the periphery of the plaque in the human tissue (Figure 6). These STOMP analyses demonstrate the molecular differences of amyloid deposits in AD mice compared to senile plaques in AD patients, but confirm the segregation of these pre-synaptic proteins in and around amyloid plaques and point to their potential importance in AD pathophysiology.

![Figure 6.](https://cdn.elifesciences.org/articles/09579/elife-09579-fig6-v2.jpg)

**Figure 6.:** The amyloid plaques (arrow) are positive for VAMP2 and SNAP25, whereas synaptophysin does not stain the core of the plaques and punctate lobular profiles decorating the plaque are positive for synaptophysin. Scale bar is 30 µm.

### Comparison with previously published data

Some proteins identified by STOMP (including v-ATPase, dynamin, SNAP25, VAMP2, synapsin, clathrin, ankyrin, and so on; see Tables 1, 2 and Supplementary file 3) were detected in previous LCM-based studies; however, with the exception of v-ATPase and dynamin, these proteins were not previously shown to be significantly or sufficiently enriched compared to the control samples (Liao et al., 2004). The highly specific nature of STOMP protein labeling and recovery permits very sensitive detection of proteins present in plaques, even if those proteins are also abundant in the remainder of the brain.

### Conclusions

We have shown that the STOMP technique can be used to determine the proteomic composition of micron-scale microscopic features. The procedure does not require large quantities of tissue and can be completed in a reasonable amount of time. Using amyloid plaques in TgCRND8 mice as a test subject, we demonstrated that STOMP is capable of determining the protein composition of pathological deposits in neurodegenerative disease. Our discovery that there is an accumulation of certain pre-synaptic proteins in AD plaques and in TgCRND8 mice provides direct evidence for an association between amyloid plaque formation and synaptic function. While our initial work in characterizing amyloid deposits in mouse brain used methanol fixed tissues to minimize problems with solubilizing tissue, our experience with human AD pathological tissue shows that STOMP of formalin-fixed archival tissue is possible. The STOMP technique is ideally suited for determination of the compositions of intracellular protein inclusions seen in ALS and FTD. While the principle components of these inclusions, such as TDP-439, FUS (Kwiatkowski et al., 2009; Vance et al., 2009), and dipeptide repeat proteins (Mori et al., 2013) are known, determination of the secondary components of the inclusions could shed light on disease etiology.

In developing the STOMP technique, we have focused on identification of photo-tagged proteins, however, the nonspecific nature of benzophenone photochemistry should cause photo-tagging of nonprotein components as well. In this regard, the STOMP technique can easily be modified to identify the RNA composition of biological features. RNA-containing subcellular structures such as P-bodies and stress granules have been implicated in neurodegenerative disease (Li et al., 2013); these structures are of suitable size for STOMP, and there is a realistic possibility of determining jointly their proteomic and transcriptomic composition with this technique. The application of this technique to many other aspects of cell biology research is also conceivable.

## Materials and methods

Unless otherwise specified, all dry reagents are from Sigma–Aldrich, St. Louis, MO. All organic solvents are from Caledon Laboratories, Georgetown, ON.

### Photo-tag synthesis

The 6HisBP peptide (4-benzoyl-benzamidyl-Gly-His-His-His-His-His-His-amide, Figure 1) was synthesized using FMOC-His(Trt)-OH, FMOC-Gly-OH (Avanced Chemtech, Louisville, KY) and 4-benzoylbenzoic acid; all synthesis steps were carried out in N,N-dimethylformamide (DMF). FMOC cleavage employed 2% 1,8-diazabicyclo[5.4.0]undec-7-ene (DBU); activation and coupling used 0.5 M N,N-diisopropylethylamine (DIPEA) and o-(7-azabenzotriazol-1-yl)-N,N,N′,N′-tetramethyluronium hexafluorophosphate (HATU, Applied Biosystems, Waltham, MA). The peptide was cleaved from the resin by incubating in 5 ml of a solution containing trifluoroacetic acid, thioanisole, ethanedithiol, and anisole in the volume ratio of 90:5:3:2, for 2 hr at room temperature, then precipitated by dropwise addition to 40 ml −70°C diethyl ether. The crude 6HisBP was washed five times with cold diethyl ether to remove residual cleavage reagents, dried under nitrogen, redissolved in ultrapure water, frozen, and lyophilized (Freezone 4.5, Labconco, Kansas City, MO) to remove any remaining volatiles.

The presence of 6HisBP was confirmed by ESI-MS.

### Murine tissue sectioning and preparation

Transgenic CRND8 (TgCRND8) mice express a transgene that encodes human amyloid precursor protein (APP695) harboring both the ‘Swedish’ double mutation KM670/671/NL and the additional ‘Indiana’ point mutation V717F; they develop dense-cored amyloid plaques and neuritic pathology by 5 months of age (Chishti et al., 2001). Animals were sacrificed at 8 months and their brains were embedded in OCT medium for frozen sectioning onto glass slides. Sections were post-fixed by immersion for 10 min in −20°C methanol, air dried at room temperature, and stored at −70°C.

Brain sections were treated with DEPC to covalently modify endogenous histidyl residues and abolish their capacity to bind to nickel. Sections were rehydrated by immersion in DEPC buffer (10 mM NaHCO3, 10 mM NaH2PO4, pH adjusted to 6.0 with hydrochloric acid). An initial working solution of 1 M DEPC in methanol was prepared immediately before use and diluted in DEPC buffer to 10 mM DEPC. Tissue sections were immersed in DEPC solution for 3 hr at room temperature, then washed twice with PBS.

Sections were stained with 1% ThS. Sections were soaked in two changes of 6HisBP working solution (12 mM 6HisBP, 10 mM sodium phosphate, pH 7.6), then coverslipped. For each STOMP sample, a ‘dark’ control was prepared from an adjacent section.

All experiments were performed in accordance with the guidelines imposed by the University of Toronto Animal Care Committee and Canadian Council for Animal Care.

### Microscopy and photoactivation

Microscopy employed Zeiss LSM 510 and LSM 710 confocal microscopes, equipped with two-photon infrared (Coherent Chameleon, tuned to 720 nm) laser sources. ThS fluorescence was excited at 488 nm and imaged confocally through 505 nm longpass or 500–530 nm bandpass filters. The nominal pixel spacing was 0.44 .44× 0.44 µm using a 20× 1.20 NA water immersion objective lens. Masks containing only amyloid plaques were created using the following four-step process in ImageJ (Schneider et al., 2012). High-frequency noise in the ThS fluorescence image was removed using ImageJ's ‘Smooth’ function, and vascular amyloid deposits—if any—were manually excluded from each fluorescence image. Dense-cored plaques were highlighted with the ‘Threshold’ tool. Finally, the ‘Erode’ method was used to trim a single-pixel (0.44 µm) margin from the mask edge, to ensure that only material definitely within the plaque would be photo-tagged. The resulting mask image was saved as a ‘text image’.

Using a custom macro for controlling the two-photon microscope (Pham et al., 2007) each pixel in the mask image was irradiated six times, for 4 ms on each pass. A detailed description of the STOMP macro interface available in Source code 1. The total volume photo-activated was approximately 2 × 106 µm3 per sample (1 × 106 μm3 per section).

### Solubilization and affinity purification

Each section was lifted from the slide using a clean, sterile razor blade and transferred into a 1.5-ml polypropylene microcentrifuge tube. For methanol-fixed murine tissue, 200 μl of solubilization buffer containing 2% sodium dodecyl sulfate (SDS, Bio-Rad, Hercules, CA), 8 M urea, 250 mM NaCl, 10 mM sodium phosphate buffer (pH 8.2), 10% (wt/vol) glycerol, and 2% β-ME was added to each tube. Tubes were immersed in a boiling water bath for 5 min, sonicated for 5 min in a Branson 1210 bath sonicator (Branson Ultrasonic Corporation, Danbury, CT), incubated at room temperature for 45 min, and returned to boiling water for an additional 5 min to fully solubilize the tissue sample.

For solubilization of formalin-fixed human tissue, 400 µl of a modified solubilization buffer containing 200 mM Tris (in addition to the ingredients noted above, as a formaldehyde scavenger) was used. Formalin-fixed sections were held at 90°C for 60 min. Each sample was transferred to a 15-ml polypropylene centrifuge tube and combined with a 20-fold excess of room-temperature dilution buffer (8 M urea, 250 mM NaCl, 10 mM sodium phosphate buffer, 1 mM imidazole) to dilute the SDS, β-ME, and Tris to concentrations compatible with Ni-NTA agarose bead binding. 80 μl of Ni-NTA agarose bead slurry (Qiagen, Valencia, CA) was added, and the mixture was tumbled overnight at room temperature to allow the His-tagged proteins to bind to the beads.

After binding, the beads were pelleted by centrifugation at 500×g for 30 s. The supernatant was discarded, and the beads were resuspended in 1 ml wash buffer (6 M urea, 0.1% SDS, 250 mM NaCl, 10 mM phosphate at pH 8.2, 0.1% β-ME, 1 mM imidazole) and tumbled for 2 min. This wash was repeated three times. During the final wash step, each sample was divided into two portions: one reserved for mass spectrometry, and one for gel electrophoresis and silver staining.

### Mass spectrometry

After recovery, the proteins captured on the surface of the beads for each sample were solubilized in 8 M urea with 50 mM Tris at pH 8, reduced by 5 mM DTT for 1 hr, and alkylated with 10 mM iodoacetamide for 45 min in darkness at room temperature. Proteins were digested at RT with Endoproteinase Lys-C (Roche) for 6 hr first, and then diluted ninefold into ammonium bicarbonate buffer before adding sequencing grade trypsin (Promega) overnight. After acidification to 1% formic acid (FA), mixtures were desalted using disposable Toptip C-18 columns (Glygen) and the eluted peptides lyophilized to dryness.

Peptides were loaded and separated on sequential reverse phase micro-capillary liquid trap and analytical columns using an EASY-nLC nanoflow pump system (Proxeon). The micro-capillary trap column was constructed in a 25 mm × 75 mm silica capillary packed with 5 μm Luna C18 stationary phase (Phenomenex). The analytical column was constructed in a 100 mm × 75 μm silica capillary, with a fine tip pulled with a column puller (Sutter Instruments), packed with 3 μm Luna C18 stationary phase. Separation was performed in 105 min using an organic gradient w consisting of buffer A (5% acetonitrile with 0.1% FA) to buffer B (95% acetonitrile with 0.1% FA) at a flow rate of 300 nl/min starting with a gradient of 2–6% buffer B in 1 min, followed by 6–24% in 74 min, 24–90% in 16 min, then 90% buffer B for 5 min and 90–0% in 1 min and finally 0% buffer B in 8 min. Eluted peptides were electrosprayed from a nanospray ion source (Proxeon) directly into a high-performance Orbitrap Velos hybrid tandem mass spectrometer (ThermoFisher Scientific). 10 data-dependent collision-induced dissociation (CID) ion trap scans (centroid mode) were automatically acquired simultaneously with one high resolution (60,000 FWHM resolution) full scan (profile mode) mass spectra. A dynamic exclusion list was enabled to exclude a maximum of 500 ion targets for 22.5 s.

RAW data files were extracted with the ReAdW program and submitted to database search using SEQUEST (v2.7) against UniProt/SwissProt protein sequence FASTA file containing 22,491 human proteins as well as an equivalent number of reversed decoy proteins (to estimate the empirical false discovery rate). Search parameters were set to allow for one missed cleavage site and one fixed modification (+57 on cysteine) using a precursor tolerance of 3 m/z. Matched peptides were further filtered at the precursor ion mass accuracy level using a 20 ppm cut-off, while protein hits were compiled and filtered using the StatQuest program with a minimum confidence threshold of 99%.

### Gel electrophoresis and silver staining

Silver staining employed an adaptation of the method of Shevchenko et al. (1996). Gels were fixed in 6% formaldehyde and 25% ethanol for 1 hr and washed with water. Gels were sensitized for 45 min in 50 ppm sodium thiosulfate solution, soaked in 0.1% silver nitrate for 45 min, rinsed with ultrapure water, and developed for approximately 1 min in a solution of 2% sodium carbonate with 0.037% formaldehyde. Development was stopped with 50 mM EDTA. Silver-stained gels were photographed with an EOS 550D digital camera (Canon, Tokyo, Japan).

### Immunofluorescence and immunohistochemistry

TgCRND8 brain sections were stained with 1% ThS and blocked overnight with 10% fetal bovine serum (FCS) in PBS. Sections were incubated with primary antibodies against β-amyloid peptide, SNAP25, synapsin 1, synaptophysin, syntaxin 1, α-synuclein, V-type proton ATPase subunit B (ATP6V1B2) or VAMP2 at the dilutions indicated in Supplementary file 4, and then with the appropriate Texas Red-labeled secondary.

Formalin-fixed, paraffin-embedded sections of human brain from deceased AD patients were incubated with synaptophysin, SNAP25, and VAMP2 antibodies at the dilutions indicated in Supplementary file 4. After incubation with secondary antibodies, immunoreactivity was developed using diaminobenzidine and counterstained with hematoxylin.

Tissues from AD cases were collected with patient consent and handled under protocols approved by the University Health Network.

### Photo-tagging volume measurement

TgCRND8 brain sections (frozen sectioned, methanol post-fixed, DEPC treated) were soaked in 6HisBP solution, and a single pixel spot was photo-tagged using the STOMP macro as described above. Unbound photo-tag was then washed out of the section with several changes of PBS. Sections were blocked with 5% bovine serum albumin, incubated with an anti-hexahistidine antibody, and fluorescently labeled with an Alexa 488-conjugated secondary antibody.

A high-resolution confocal z stack of immunofluorescence images was collected using a 63× 1.4 NA oil-immersion objective. Maximum intensity projections through the resulting z stacks were used to quantify the extent of the photo-tagged spot. Fluorescence intensity profiles through the center of the spot in x, y, and z directions were extracted using ImageJ and fitted with a Gaussian curve using OriginPro 8.5.0 (OriginLab, Northampton MA) to determine the width (FWHM) of the spot in each dimension.
