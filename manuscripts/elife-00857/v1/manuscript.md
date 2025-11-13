# Structure-based discovery of fiber-binding compounds that reduce the cytotoxicity of amyloid beta

## Authors

- Lin Jiang<sup>1</sup>
- Cong Liu<sup>1</sup>
- David Leibly<sup>1</sup>
- Meytal Landau<sup>1</sup>
- Minglei Zhao<sup>1</sup>
- Michael P Hughes<sup>1</sup>
- David S Eisenberg<sup>1</sup> †

### Affiliations

1. Departments of Chemistry and Biochemistry and Biological Chemistry Howard Hughes Medical Institute, UCLA–DOE Institute for Genomics and Proteomics, University of California, Los Angeles Los Angeles United States

† Corresponding author

## Abstract

Amyloid protein aggregates are associated with dozens of devastating diseases including Alzheimer’s, Parkinson’s, ALS, and diabetes type 2. While structure-based discovery of compounds has been effective in combating numerous infectious and metabolic diseases, ignorance of amyloid structure has hindered similar approaches to amyloid disease. Here we show that knowledge of the atomic structure of one of the adhesive, steric-zipper segments of the amyloid-beta (Aβ) protein of Alzheimer’s disease, when coupled with computational methods, identifies eight diverse but mainly flat compounds and three compound derivatives that reduce Aβ cytotoxicity against mammalian cells by up to 90%. Although these compounds bind to Aβ fibers, they do not reduce fiber formation of Aβ. Structure-activity relationship studies of the fiber-binding compounds and their derivatives suggest that compound binding increases fiber stability and decreases fiber toxicity, perhaps by shifting the equilibrium of Aβ from oligomers to fibers.

## Introduction

Protein aggregates, both amyloid fibers and smaller amyloid oligomers, have been implicated in the pathology of Alzheimer’s and other neurodegeneration diseases (Chiti and Dobson, 2006; Eisenberg and Jucker, 2012). The increasing prevalence of Alzheimer’s disease in our aging societies, the associated tragedy for patients and their families, and the mounting economic burden for governments have all stimulated intense research into chemical interventions for this condition. Much work has been focused on screening compounds that prevent aggregation and the associated cytotoxicity of the amyloid β-peptide (Aβ) (reviews by Sacchettini and Kelly, 2002; Bartolini and Andrisano, 2010; Hard and Lendel, 2012).

Screens have often focused on natural products from plants and lichens. These include polyphenols, such as epigallocatechin gallate (EGCG) from green tea (Ehrnhoefer et al., 2008) and curcumin from the spice turmeric (Yang et al., 2005). These natural polyphenolic compounds show inhibition on the fibrillation of a variety of amyloid proteins, including Aβ40 as well as α-synuclein, IAPP and PrP (Porat et al., 2006; Dasilva et al., 2010; Ono et al., 2012). Several dyes have also been found to ameliorate amyloid toxicity. Orcein from lichens appears to diminish toxic oligomers and enhance fiber formation (Bieschke et al., 2011). Congo red, thioflavin T and their analogs, commonly used as staining reagents for amyloid detection, exhibit ameliorative effects on neurodegenerative disorders, such as Alzheimer’s, Parkinson’s, Huntington’s, and prion diseases (Frid et al., 2007; Alavez et al., 2011), however their application is limited by significant side effects (Klunk et al., 2004).

Additional screens have identified a variety of molecules, including proteins (Evans et al., 2006), antibodies (Kayed et al., 2003; Ladiwala et al., 2012), synthetic peptide mimetics (Findeis, 2002; Kokkoni et al., 2006; Takahashi and Mihara, 2008; Cheng et al., 2012) and small molecules (Wood et al., 1996; Williams et al., 2005; McLaurin et al., 2006; Necula et al., 2007; Bartolini and Andrisano, 2010; De Felice et al., 2001; Ladiwala et al., 2011; Hard and Lendel, 2012; Kroth et al., 2012), that inhibit Aβ fibrillogenesis and/or Aβ-associated cytotoxicity in vitro. While most efforts have targeted the deposition of Aβ fibers as the hallmark of Alzheimer’s, smaller amyloid oligomers are now receiving greater attention as the possible toxic entities in Alzheimer’s and other neurodegenerative diseases (Hartley et al., 1999; Cleary et al., 2005; Silveira et al., 2005). Furthermore, emerging evidence suggests that mature, end-stage amyloid fibers may serve as a reservoir, prone to releasing toxic oligomer (Xue et al., 2009; Cremades et al., 2012; Krishnan et al., 2012; Shahnawaz and Soto, 2012). Recent screens have identified compounds that reduce Aβ cytotoxicity, without interfering with Aβ fibrillation (Chen et al., 2010) or promoting the formation of stable Aβ aggregates (Bieschke et al., 2011).

Structural information about protein targets often aids drug development, so here we take a structure-based approach, combined with computational screening, to discover amyloid interacting compounds that reduce amyloid toxicity. This approach has been enabled by the determination of atomic structures of the adhesive segments of amyloid fibers, termed steric zippers (Nelson et al., 2005), and of solid state NMR-based structures of amyloid fibers (such as full-length Aβ fibers [Luhrs et al., 2005; Petkova et al., 2005] and the HET-s prion domain complexed with Congo Red [Schutz et al., 2011]). The steric zipper structures reveal a common motif for the spine of amyloid fibers, in which a pair of fibrillar β-sheets is held together by the side-chain interdigitation (Sawaya et al., 2007). We focus on Aβ, a peptide of 39–42 residues cleaved from the Amyloid precursor protein (APP) associated with Alzheimer’s, as a target for inhibitor discovery. The segment Aβ16–21 with the sequence KLVFFA is an amyloid-forming peptide, which packs in a steric zipper form, and has been identified as the spine of the full-length Aβ fiber (Luhrs et al., 2005; Petkova et al., 2006; Colletier et al., 2011). Co-crystal structures have been determined for small molecules in complex with the fibrillar β-sheets of Aβ16–21 (Landau et al., 2011). One of these structures—Aβ16–21 with the dye Orange G—reveals the specific pattern of hydrogen bonds and apolar interactions between orange G and the steric zipper: the negatively charged dye binds specifically to lysine side chains of adjacent sheets, and its planar aromatic portion packs against apolar residues (phenylalanine and valine) of adjacent sheets. By creating a tight, low energy interface across several β-strands within fiber core, this fiber-binding molecule appears to stabilize the fiber structure. With this atomic structure as a basis, we are able to screen for small molecular compounds that bind to amyloid fibers, stabilizing them and possibly reducing amyloid toxicity. Applying our structure-based screening procedure, we screen computationally for compounds that bind to Aβ fibers, termed BAFs (Binders of Amyloid Fibers) and then experimentally test their effects on Aβ aggregation and cytotoxicity.

## Results

### Structure-based screening procedure

We have devised a structure-based procedure for the identification of small molecules that bind to amyloid and affect amyloid toxicity (Figure 1). The procedure starts from a co-crystal structure of a ligand bound to an amyloidogenic segment of Aβ (Landau et al., 2011), the dye orange G bound to the fiber-like crystal structure of KLVFFA(Aβ16–21) segment. This structure reveals the chemical environment or ‘pharmacophore’ presented by the ligand binding site of this Aβ segment, that is, orange G binds to stacked β-sheets of Aβ. Knowledge of the amyloid pharmacophore (Figure 1A) permitted us to screen for compounds that could be expected to bind in this chemical environment, possibly stabilizing amyloid fibers.

![Figure 1.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig1-v1.jpg)

**Figure 1.:** In step (A) the crystal structure (Landau et al., 2011) is determined of a complex of an amyloidogenic segment of Aβ (in this case residues 16-KLVFFA-21 of the spine of the Aβ fiber) with an amyloid-binding Ligand X (in this case orange G), revealing aspects of the pharmacophore for Ligand X. Prior to step (B) a large library of available compounds is selected for computational docking (∼18,000 purchasable compounds in this case). In step (B) computational docking is applied to test the compatibility of each member of the library for the pharmacophore of the amyloidogenic segment defined in step (A). In step (C), the top scoring members of the library are tested for compatibility of binding within a full-length Aβ fiber (in this case the 400 top scoring members were tested on a solid state NMR-derived model of an Aβ fiber, pdb entry 2LMO) (Petkova et al., 2006). The representative models from steps B and C are shown in Figure 1—figure supplements 1 and 2. In step (D), the compounds are ranked by tightest binding energy and best shape complementarity for the pharmacophore. In step (E), the top-ranking compounds (25 in this case) are selected for experimental characterization and validation, including NMR assessment of binding, EM assays of their effects on fiber formation, and cell viability assays for their effects on Aβ cytotoxicity. In step (F), new compounds (9 in this case) and compound derivatives (17 in this case) are selected for an additional cycle of computational and experimental testing, based on their similarity to the lead compounds from the initial cycle.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** In step (B) (Figure 1), a large library of ∼18 thousand commercially available compounds were docked onto the Aβ16–21 fiber, and ∼400 top ranking compounds, whose binding energy and shape complementary score are better than the control molecule orange G, were selected for the next docking step. The models of representative BAFs docked on single beta-sheet of Aβ16–21 fiber are compared to that of orange G. (A). A side view of the compound BAF1 (in green sticks) docked on the Aβ16–21 fiber (in a grey color) with a predicted binding energy of −8.4 kcal/mol. (B). A side view of BAF8 (in cyan sticks) docked on the Aβ16–21 fiber with a predicted binding energy of −12 kcal/mol. (C). A side view of orange G (in orange sticks) docked on the Aβ16–21 fiber with a predicted binding energy of −8.0 kcal/mol. The charge interactions between the compounds and Lysine residues of Aβ16–21 fiber are highlighted by black lines.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** In step (C) (Figure 1), the top-ranking compounds after the first docking step were further filtered by docking onto full-length Aβ fiber model (pdb entry 2LMO) (Petkova et al., 2006). The models of representative BAFs docked onto Aβ fiber are compared to that of orange G. (A–C). A top view of the compounds (BAF1, BAF8 and orange G) docked onto Aβ fiber (in a light yellow color). (D–F). A side view of the same compounds docked onto Aβ fiber. (A and D). BAF1 (in a green color) binds to the side of Aβ fiber (in a light yellow color) with a predicted binding energy of −10 kcal/mol. (B and E). BAF8 (in a cyan color) binds to the side of Aβ with a predicted binding energy of −12 kcal/mol. (C and F). Orange G (in an orange color) binds to the side of Aβ fiber with a predicted binding energy of −9 kcal/mol. The charge interactions between the compounds and Lysine residues are highlighted by black lines.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** When identifying BAFs by two steps of computational docking (Figure 2A as well as step B and C in Figure 1), most models of the second docking step (docking to full-length Aβ fiber in step (C) retained their binding modes found in the previous docking step (docking to Aβ16–21 fiber in step (B). Interestingly, docking of BAF1 onto full-length Aβ fiber not only recapitulated the initial binding mode found in previous Aβ16–21 docking step but also revealed the different binding mode with comparable binding energies. Two examples of those alternative binding modes are shown in (A and B). In both modes, BAF1 tends to use its polar (hydroxyl) group to interact with the charged residues Glu22 of Aβ and use its non-polar (aromatic) portion to pack against the hydrophobic residues Phe20 of Aβ full fibers.

### Construction of compound libraries for computational screening

For assembling the compounds in our screening library, we sought three characteristics: (a) commercially available compounds since we intended to follow the in silico screening with experimental validation; (b) compounds with known three-dimensional structures such that our screening would be as realistic as possible; (c) generally flat compounds able to bind to the β-sheets of the steric zipper, as does orange G. Some ∼11,000 compounds having the first two characteristics (CSD-ZINC set) were selected as the intersection of molecules found both in the Cambridge Structure Database (http://www.ccdc.cam.ac.uk) and the Zinc Database of purchasable compounds (http://zinc.docking.org/) (Irwin and Shoichet, 2005). This CSD-ZINC set spans a variety of structural shapes and molecular properties. A second set of ∼7000 compounds, the Flat Compound Set, was gathered from the ZINC database to include molecules expected to bind to the flat surface of a steric zipper. The members of this set contain multiple aromatic rings or one aromatic ring with additional planar groups.

### Computational screening of compounds that bind to Aβ fibers

Computational screening was carried out with the RosettaLigand program (Davis and Baker, 2009), after adapting its docking approach to carry out high-throughput screening (Figure 2). The conformational flexibilities of ligand and protein side chains are in a ‘near-native’ perturbation fashion, meaning that the fine sampling of conformations was restrained to be close to the starting conformation. A balance was achieved between extensive sampling and the speed required for screening a large compound library by fine sampling of side chain and ligand torsion angles only around their starting conformations, as illustrated by sticks in Figure 2C.

![Figure 2.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig2-v1.jpg)

**Figure 2.:** (A). Outline of our procedure for structure-based screening. We prepare two sets of compounds (shown in the upper left) for screening against both types of fibers shown in the upper right. Compound Set 1 is the intersection of the ZINC Database of purchasable compounds with the Cambridge structural database (CSD) of known structures. Set 2 consists of other flat aromatic and multiple conjugated compounds found in the ZINC Database. The full description of each computational step is in ‘Materials and methods’. (B). Distribution of calculated binding energies for the compound libraries of Sets 1 and 2. Those top-ranking compounds have better predicted binding energy than orange G. Structural comparison of docked models of such compound BAF8 and orange-G is discussed in the Figure 2—figure supplement 1. Notice the starred bins which suggest that some members of Set 2, containing flat compounds, tend to be among the top scoring compounds, presumably having the tightest binding to the flat fiber surface. (C). The conformational ensemble of a compound representative shown docked onto the Aβ16–21 fiber structure. (D). A model of BAF8 docked onto an NMR-derived model of full-length Aβ fiber. Notice that the apolar ring structure of the compound binds to the relatively flat apolar (gray) surface of the fiber, and the polar moieties of the compound (red) form hydrogen bonds to the polar groups of the fiber (yellow). The stereo view of BAF8 model is shown in Figure 2—figure supplement 2.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** BAF8 has a chemical structure similar to orange G (top panels). The comparison of the shape complimentary at binding interfaces reveals that BAF8 binds more tightly to the side of fibers than orange G. (A). A top view of the docked model of BAF8 (in a cyan color) with the predicted binding energy of −12 kcal/mol highlights the tight shape complementary at the fiber-ligand interface. (B). A top view of the docked model of orange G (in an orange color) with the predicted binding energy of −8 kcal/mol shows a poorly packed interface with cavities.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** A wall-eyed stereo view of BAF8 (Figure 2D) (in cyan sticks) docked to the side of an Aβ16–21 fiber (light yellow) reveals good non-polar and polar interaction across binding interfaces. The hydrophobic binding site for the aromatic portion of BAF8 is indicated by grey mesh surfaces to highlight the good shape complementary. The polar interaction of hydrogen bonds between the charged residues Lys 16 of Aβ and the polar portion of BAF8 are indicated by black thick lines.

In the screening steps of computational docking (Figure 2A), a library of ∼18,000 purchasable compounds (Sets 1 and 2) was scanned computationally for structural compatibility with the pharmacophore (ligand binding site) presented by a single sheet of the Aβ16–21 steric zipper. Structural compatibility was assessed by a combination of binding energy (Meiler and Baker, 2006) and steric complementarity (Lawrence and Colman, 1993). After computational docking, the distribution of calculated binding energies suggests that, statistically the flat compounds from Set 2 fit more snugly on the flat surfaces of Aβ16–21 fibers than those with diverse shapes in Set 1 (Figure 2B). The best scoring compounds were screened further by requiring that each is also structurally compatible with the solid-state NMR-derived model of the Aβ full-length fiber structure (Petkova et al., 2006) (Figure 1C and Figure 1—figure supplement 3).

### Experimental characterization of BAFs

After in silico screening of a library of ∼18,000 purchasable compounds, twenty-five of the top-ranking compounds all with better scores for binding energy and steric complementarity than orange G (Figure 1D, Figure 2—figure supplement 1), were selected for experimental validation. First these 25 compounds were tested for their ability to protect mammalian cells from Aβ toxicity (Figure 1E, Tables 1 and 2), and five of them were found to reduce the toxic effects of Aβ. These five were tested for binding to both Aβ1–42 and Aβ16–21 fibers by NMR. Two were found to have tighter binding than orange G, and the others gave insufficient NMR signals for detection. To expand this set of the five compounds, a second cycle of inhibitor discovery was performed. From the computed positions of the five compounds, a refined pharmacophore was inferred (Figure 1F), and used in the next cycle of screening. Added to the compound set were nine additional compounds apparently related to the five lead compounds from the initial cycle, plus 17 chemical derivatives of compounds (Tables 1 and 3). The second cycle produced three additional compounds and three compound derivatives that also protected the mammalian cells from Aβ fibers. One of these compounds was confirmed by NMR to bind to Aβ fibers. The detailed description of those experimental results is as follows.

**Table 1.**
 List of all tested BAF compounds


<table>
  <thead>
    <tr>
      <th>Compound</th>
      <th>Molecular formula</th>
      <th>Molecular weight*</th>
      <th>Sources/purchasing</th>
      <th>Rescuing percentage (%)</th>
      <th>ZINC entry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BAF1</td>
      <td>C20H8Br4O5</td>
      <td>648</td>
      <td>Sigma-Aldrich</td>
      <td>44 ± 7</td>
      <td>ZINC04261875</td>
    </tr>
    <tr>
      <td>BAF2</td>
      <td>C19H14O5S</td>
      <td>354</td>
      <td>Sigma-Aldrich</td>
      <td>4 ± 3</td>
      <td>ZINC03860918</td>
    </tr>
    <tr>
      <td>BAF3</td>
      <td>C16H13NO3</td>
      <td>267</td>
      <td>Ryan Scientific</td>
      <td>4 ± 5</td>
      <td>ZINC04289063</td>
    </tr>
    <tr>
      <td>BAF4</td>
      <td>C24H16N2O6</td>
      <td>428</td>
      <td>Aldrich</td>
      <td>88 ± 22</td>
      <td>ZINC13346907</td>
    </tr>
    <tr>
      <td>BAF5</td>
      <td>C16H7Na3O10S3</td>
      <td>524</td>
      <td>Sigma-Aldrich</td>
      <td>11 ± 7</td>
      <td>ZINC03594314</td>
    </tr>
    <tr>
      <td>BAF6</td>
      <td>C26H20N2</td>
      <td>360</td>
      <td>Alfa-Aesar</td>
      <td>5 ± 7</td>
      <td>ZINC08078162</td>
    </tr>
    <tr>
      <td>BAF7</td>
      <td>C18H12N6</td>
      <td>312</td>
      <td>Alfa-Aesar</td>
      <td>2 ± 2</td>
      <td>ZINC00039221</td>
    </tr>
    <tr>
      <td>BAF8</td>
      <td>C17H14N2O5S</td>
      <td>358</td>
      <td>Sigma-Aldrich</td>
      <td>23 ± 11</td>
      <td>ZINC12358966</td>
    </tr>
    <tr>
      <td>BAF9</td>
      <td>C19H13N3O4S</td>
      <td>379</td>
      <td>NCI plated 2007†</td>
      <td>−3 ± 22</td>
      <td>ZINC03954432</td>
    </tr>
    <tr>
      <td>BAF10</td>
      <td>C17H13NO3</td>
      <td>279</td>
      <td>NCI plated 2007</td>
      <td>3 ± 5</td>
      <td>ZINC00105108</td>
    </tr>
    <tr>
      <td>BAF11</td>
      <td>C20H13N2O5S</td>
      <td>393</td>
      <td>NCI plated 2007</td>
      <td>48 ± 12</td>
      <td>ZINC04521479</td>
    </tr>
    <tr>
      <td>BAF12</td>
      <td>C13H8Br3NO</td>
      <td>434</td>
      <td>NCI plated 2007</td>
      <td>38 ± 6</td>
      <td>ZINC12428965</td>
    </tr>
    <tr>
      <td>BAF13</td>
      <td>C19H16ClNO4</td>
      <td>358</td>
      <td>Sigma-Aldrich</td>
      <td>0 ± 2</td>
      <td>ZINC00601283</td>
    </tr>
    <tr>
      <td>BAF14</td>
      <td>C10H6S2O8</td>
      <td>318</td>
      <td>Sigma-Aldrich</td>
      <td>3 ± 3</td>
      <td>ZINC01532215</td>
    </tr>
    <tr>
      <td>BAF15</td>
      <td>C23H28O8</td>
      <td>432</td>
      <td>Sigma-Aldrich</td>
      <td>13 ± 4</td>
      <td>ZINC00630328</td>
    </tr>
    <tr>
      <td>BAF16</td>
      <td>C19H19NO5</td>
      <td>341</td>
      <td>Sigma-Aldrich</td>
      <td>5 ± 8</td>
      <td>ZINC28616347</td>
    </tr>
    <tr>
      <td>BAF17</td>
      <td>C23H25N5O2</td>
      <td>404</td>
      <td>Sigma-Aldrich</td>
      <td>6 ± 3</td>
      <td>ZINC00579168</td>
    </tr>
    <tr>
      <td>BAF18</td>
      <td>C24H16O2</td>
      <td>336</td>
      <td>ChemDiv</td>
      <td>6 ± 2</td>
      <td>ZINC02168932</td>
    </tr>
    <tr>
      <td>BAF19</td>
      <td>C18H14N2O6</td>
      <td>354</td>
      <td>ChemDiv</td>
      <td>3 ± 4</td>
      <td>ZINC01507439</td>
    </tr>
    <tr>
      <td>BAF20</td>
      <td>C25H19N5OS</td>
      <td>438</td>
      <td>ChemDiv</td>
      <td>8 ± 4</td>
      <td>ZINC15859747</td>
    </tr>
    <tr>
      <td>BAF21</td>
      <td>C19H14Br2O</td>
      <td>418</td>
      <td>ChemDiv</td>
      <td>6 ± 3</td>
      <td>ZINC38206526</td>
    </tr>
    <tr>
      <td>BAF22</td>
      <td>C21H16N2O3S2</td>
      <td>408</td>
      <td>Life Chemicals</td>
      <td>3 ± 5</td>
      <td>ZINC04496365</td>
    </tr>
    <tr>
      <td>BAF23</td>
      <td>C16H11ClO5S</td>
      <td>351</td>
      <td>Enamine Ltd</td>
      <td>3 ± 5</td>
      <td>ZINC02649996</td>
    </tr>
    <tr>
      <td>BAF24</td>
      <td>C23H19NO3</td>
      <td>357</td>
      <td>Sigma-Aldrich</td>
      <td>16 ± 5</td>
      <td>ZINC03953119</td>
    </tr>
    <tr>
      <td>BAF25</td>
      <td>C14H8Cl2N4</td>
      <td>303</td>
      <td>Sigma-Aldrich</td>
      <td>4 ± 3</td>
      <td>ZINC00403224</td>
    </tr>
    <tr>
      <td>BAF26</td>
      <td>C17H10O4</td>
      <td>278</td>
      <td>Aldrich</td>
      <td>46 ± 23</td>
      <td>ZINC05770717</td>
    </tr>
    <tr>
      <td>BAF27</td>
      <td>C21H16BrN3O6</td>
      <td>486</td>
      <td>ChemBridge</td>
      <td>4 ± 1</td>
      <td>ZINC01208856</td>
    </tr>
    <tr>
      <td>BAF28</td>
      <td>C17H12N2O3</td>
      <td>292</td>
      <td>ChemBridge</td>
      <td>2 ± 4</td>
      <td>ZINC00061083</td>
    </tr>
    <tr>
      <td>BAF29</td>
      <td>C22H10N4O2</td>
      <td>362</td>
      <td>ChemBridge</td>
      <td>1 ± 5</td>
      <td>ZINC00639061</td>
    </tr>
    <tr>
      <td>BAF30</td>
      <td>C14H8O5</td>
      <td>256</td>
      <td>Aldrich</td>
      <td>18 ± 13</td>
      <td>ZINC03870461</td>
    </tr>
    <tr>
      <td>BAF31</td>
      <td>C19H21NO3</td>
      <td>311</td>
      <td>Sigma</td>
      <td>84 ± 12</td>
      <td>ZINC00011665</td>
    </tr>
    <tr>
      <td>BAF32</td>
      <td>C15H14O7</td>
      <td>306</td>
      <td>Sigma-Aldrich</td>
      <td>15 ± 9</td>
      <td>ZINC03870336</td>
    </tr>
    <tr>
      <td>BAF33</td>
      <td>C27H33N3O8</td>
      <td>528</td>
      <td>Sigma-Aldrich</td>
      <td>7 ± 2</td>
      <td>SIGMA-R2253§</td>
    </tr>
    <tr>
      <td>BAF34</td>
      <td>C30H16N4O14S4</td>
      <td>785</td>
      <td>Aldrich</td>
      <td>‡</td>
      <td>ALDRICH-S432830§</td>
    </tr>
    <tr>
      <td>orange G</td>
      <td>C16H12N2O7S2</td>
      <td>408</td>
      <td>Sigma-Aldrich</td>
      <td>−2 ± 8</td>
      <td>ZINC04261935</td>
    </tr>
  </tbody>
</table>

_The 25 compounds (BAF1-25) are from the first round, and the nine compounds (BAF26-34) are from the second round. Another set of the 17 derivatives of the BAFs are shown in Table 3.*Molecular weight (anhydrous basis) excluding the salt and water molecules.†National Cancer Institute (NCI) free compound library (http://dtp.nci.nih.gov/).‡Toxicity results of BAF34 were not consistent among several independent replica experiments, possibly due to impurity and the high molecular weight of the compound.§ZINC entry of the compound is not applicable, and the catalog number from Sigma-Aldrich is provided._

**Table 2.**
 Detailed list of the active BAF compounds


<table>
  <thead>
    <tr>
      <th rowspan="2">Compound</th>
      <th rowspan="2">Molecular formula</th>
      <th rowspan="2">Molecular weight*</th>
      <th rowspan="2">Sources/companies</th>
      <th rowspan="2">Purity</th>
      <th colspan="2">Rescuing percentage§ (%)</th>
      <th rowspan="2">ZINC entry code¶</th>
      <th rowspan="2">SMILES string</th>
    </tr>
    <tr>
      <th>PC12</th>
      <th>Hela</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BAF1</td>
      <td>C20H8Br4O5</td>
      <td>647.9</td>
      <td>Sigma-Aldrich</td>
      <td>∼99%</td>
      <td>38 ± 11</td>
      <td>44 ± 7</td>
      <td>ZINC04261875</td>
      <td>c1ccc2c(c1)C(=O)OC23c4ccc(c(c4Oc5c3ccc(c5Br)O)Br)O</td>
    </tr>
    <tr>
      <td>BAF4</td>
      <td>C24H16N2O6</td>
      <td>428.4</td>
      <td>Aldrich</td>
      <td>≥95%</td>
      <td>85 ± 18</td>
      <td>88 ± 22</td>
      <td>ZINC13346907</td>
      <td>c1cc(c(cc1O)O)c2cc3c(cc2N)oc-4cc(=O)c(cc4n3)c5ccc(cc5O)O</td>
    </tr>
    <tr>
      <td>BAF8</td>
      <td>C17H14N2O5S</td>
      <td>358.4</td>
      <td>Sigma-Aldrich</td>
      <td>≥90%</td>
      <td>26 ± 12</td>
      <td>23 ± 11</td>
      <td>ZINC12358966</td>
      <td>Cc1ccc(c(c1)/N=N/c2c3ccccc3c(cc2O)S(=O)(=O)[O-])O</td>
    </tr>
    <tr>
      <td>BAF11</td>
      <td>C20H13N2O5S</td>
      <td>393.5</td>
      <td>NCI plated 2007</td>
      <td>†</td>
      <td>51 ± 11</td>
      <td>48 ± 12</td>
      <td>ZINC04521479</td>
      <td>c1ccc2c(c1)ccc(c2O)/N=N/c3c4ccccc4c(cc3O)S(=O)(=O)[O-]</td>
    </tr>
    <tr>
      <td>BAF12</td>
      <td>C13H8Br3NO</td>
      <td>433.9</td>
      <td>NCI plated 2007</td>
      <td>†</td>
      <td>19 ± 6</td>
      <td>38 ± 6</td>
      <td>ZINC12428965</td>
      <td>c1cc(ccc1/N=C/c2cc(cc(c2O)Br)Br)Br</td>
    </tr>
    <tr>
      <td>BAF26</td>
      <td>C17H10O4</td>
      <td>278.3</td>
      <td>Aldrich</td>
      <td>‡</td>
      <td>60 ± 21</td>
      <td>46 ± 23</td>
      <td>ZINC05770717</td>
      <td>c12c(cc(cc1)C(=O)C=O)Cc1c2ccc(c1)C(=O)C=O</td>
    </tr>
    <tr>
      <td>BAF30</td>
      <td>C14H8O5</td>
      <td>256.2</td>
      <td>Aldrich</td>
      <td>‡</td>
      <td>37 ± 18</td>
      <td>18 ± 13</td>
      <td>ZINC03870461</td>
      <td>c1cc2c(cc1O)C(=O)c3c(ccc(c3O)O)C2=O</td>
    </tr>
    <tr>
      <td>BAF31</td>
      <td>C19H21NO3</td>
      <td>311.4</td>
      <td>Sigma</td>
      <td>≥98%</td>
      <td>92 ± 22</td>
      <td>84 ± 12</td>
      <td>ZINC03874841</td>
      <td>CCCN1CCC2=C3C1CC4=C(C3=CC(=C2)O)C(=C(C=C4)O)O</td>
    </tr>
  </tbody>
</table>

_BAFs 1, 4, 8, 11, 12 are from the first round. BAFs 26, 30, 31 are from the second round.*Molecular weight (anhydrous basis) excluding the salt and water molecules.†With the standard of NCI free compound library.‡Analytical data for AldrichCPR products are not available.§Rescue percentage is a scaled cell survival rate.¶Entry code for the ZINC database (http://zinc.docking.org)._

**Table 3.**
 List of the representative BAFs 11, 30, 31 and their derivatives


<table>
  <thead>
    <tr>
      <th>Compound</th>
      <th>Molecular formula</th>
      <th>Molecular weight</th>
      <th>Description</th>
      <th>Toxicity inhibition (%)</th>
      <th>ZINC entry/catalog no.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BAF31</td>
      <td>C19H21NO3</td>
      <td>311</td>
      <td></td>
      <td>84 ± 12</td>
      <td>ZINC03874841</td>
    </tr>
    <tr>
      <td>BAF31ΔOH</td>
      <td>C19H21NO2</td>
      <td>295</td>
      <td>remove one hydroxyl (OH)</td>
      <td>15 ± 2</td>
      <td>ZINC03874841</td>
    </tr>
    <tr>
      <td>BAF30</td>
      <td>C14H8O5</td>
      <td>256</td>
      <td></td>
      <td>18 ± 13</td>
      <td>ZINC03870461</td>
    </tr>
    <tr>
      <td>BAF30αR</td>
      <td>C22H20O13</td>
      <td>492</td>
      <td>add additional R group away from binding interface</td>
      <td>20 ± 10</td>
      <td>ZINC28095922</td>
    </tr>
    <tr>
      <td>BAF30σOHAαOH</td>
      <td>C14H8O6</td>
      <td>272</td>
      <td>change one OH (A) position; add another OH</td>
      <td>9 ± 9</td>
      <td>ZINC03874832</td>
    </tr>
    <tr>
      <td>BAF30σOHAΔOHBαCOO</td>
      <td>C15H8O6</td>
      <td>284</td>
      <td>move one OH (A) position; delete an OH from loc B; add a carboxyl</td>
      <td>9 ± 3</td>
      <td>ZINC04098704</td>
    </tr>
    <tr>
      <td>BAF30σOHABαCH3</td>
      <td>C15H10O5</td>
      <td>270</td>
      <td>move two OH (AB) positions; add a methyl</td>
      <td>6 ± 3</td>
      <td>ZINC03824868</td>
    </tr>
    <tr>
      <td>BAF11</td>
      <td>C20H13N2O5S</td>
      <td>393</td>
      <td></td>
      <td>48 ± 12</td>
      <td>ZINC04521479</td>
    </tr>
    <tr>
      <td>BAF11ISO</td>
      <td>C20H13N2O5S</td>
      <td>393</td>
      <td>isomer form of BAF11</td>
      <td>33 ± 5</td>
      <td>ZINC12405071</td>
    </tr>
    <tr>
      <td>BAF11σR1</td>
      <td>C20H14N4O8S2</td>
      <td>502</td>
      <td>change the aromatic group</td>
      <td>35 ± 9</td>
      <td>ZINC25558261</td>
    </tr>
    <tr>
      <td>BAF11σR2 (BAF8)</td>
      <td>C17H14N2O5S</td>
      <td>358</td>
      <td>change the aromatic group</td>
      <td>22 ± 11</td>
      <td>ZINC12358966</td>
    </tr>
    <tr>
      <td>BAF11σR3</td>
      <td>C16H12N2O6S</td>
      <td>360</td>
      <td>change the aromatic group</td>
      <td>28 ± 4</td>
      <td>ZINC04900892</td>
    </tr>
    <tr>
      <td>BAF11αNO2-</td>
      <td>C20H12N3O7S</td>
      <td>438</td>
      <td>add charged group (nitro)</td>
      <td>15 ± 6</td>
      <td>ZINC16218542</td>
    </tr>
    <tr>
      <td>BAF11ISOαCOO-</td>
      <td>C21H12N2O7S</td>
      <td>436</td>
      <td>BAF11 isomer; add charged group (carboxyl)</td>
      <td>6 ± 5</td>
      <td>ZINC03861030</td>
    </tr>
    <tr>
      <td>BAF11ISOαSO3-</td>
      <td>C20H11N2O11S3</td>
      <td>552</td>
      <td>BAF11 isomer; add charged group (sulfate)</td>
      <td>2 ± 5</td>
      <td>SIGMA-33936</td>
    </tr>
    <tr>
      <td>BAF11ΔOHσR</td>
      <td>C20H14N2O4S</td>
      <td>378</td>
      <td>remove an OH;change the position of the aromatic group</td>
      <td>15 ± 6</td>
      <td>ZINC04803992</td>
    </tr>
    <tr>
      <td>BAF11ΔOHαSO3−</td>
      <td>C20H14N2O7S2</td>
      <td>458</td>
      <td>remove an OH; add sulfate group</td>
      <td>12 ± 3</td>
      <td>ZINC03954029</td>
    </tr>
    <tr>
      <td>BAF11ΔOHαR</td>
      <td>C20H18N4O5S</td>
      <td>426</td>
      <td>remove an OH; add additional group to the aromatic ring</td>
      <td>12 ± 6</td>
      <td>ZINC04416667</td>
    </tr>
    <tr>
      <td>BAF11σOHαR1</td>
      <td>C24H20N4O4S</td>
      <td>461</td>
      <td>swap the position of the OH and aromatics</td>
      <td>5 ± 5</td>
      <td>ZINC04804174</td>
    </tr>
    <tr>
      <td>BAF11σOHαR2</td>
      <td>C16H19N3O5S</td>
      <td>365</td>
      <td>swap the position of the OH and aromatics</td>
      <td>4 ± 6</td>
      <td>ZINC17378758</td>
    </tr>
  </tbody>
</table>

### Inhibition of Aβ1–42 toxicity by BAFs

Having identified compounds that bind Aβ fibers, by a structure-based procedure, we tested their effects on the cytotoxicity of Aβ1–42 fiber against two mammalian cell lines: PC12 and HeLa (Figure 3). Five BAFs—1,4,8,11, and 12—in the initial cycle and three additional BAFs—26, 30, and 31—from the second cycle, with diversified chemical structures shown in Figure 4, significantly increased both PC12 and HeLa cell survival after 24 hr incubation with Aβ1–42 (0.5 µM) at concentration of 2.5 µM, while the BAFs alone had little or no effect on cell survival (Figure 3—figure supplement 1). Three BAFs—11, 26, and 31—showed clear dose-response profiles in their protection of both PC12 and HeLa cells (Figure 3B). Among them, the two best BAFs—26 and 31—were tested and did not affect the cytotoxicity of amyloid fibers other than Aβ (Figure 3—figure supplement 2). Although all of these BAFs provide protection against Aβ toxicity, none diminish the amount of Aβ fibers in electron micrographs (Figure 3C).

![Figure 3.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig3-v1.jpg)

**Figure 3.:** Our newly discovered BAFs diminish Aβ1–42 toxicity without significantly reducing Aβ1–42 fibrillation. (A). Eight BAFs reduce Aβ toxicity in mammalian cell lines (PC12 in orange; HeLa in green). These identified compounds with diversified chemical structures are quite different from orange G, whose co-crystal structure with an amyloid segment is the basis of our approach (Figure 4 and Table 2). For each compound, 2 to 4 repeats of each independent experiment were performed. For each experimental repeat, four replicates per sample per concentration were tested. The symbol * indicates a p<0.1; the symbol ** indicates a p<0.01 and the symbol *** indicates a p<0.001. The student’s t-test and p-value analysis are in Table 4. (B). The representative BAFs—31, 26, and 11—inhibit Aβ cyto-toxicity in a dose-dependent manner. (C). Transmission electron microscopy (TEM) images of Aβ fibers alone and Aβ fibers with the BAFs, the same samples prepared for cell viability assay. All 8 BAFs that diminish Aβ toxicity do not noticeably diminish Aβ fibrillation. Scale bars indicate 200 nm.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Incubating cells with or without BAFs for 24 hours caused little or no change for cell viability of both PC12 and HeLa. The error bars are calculated from four experiment replicates.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** The final concentration of IAPP is 1 µM and α-synuclein is 2 µM. The molar ratio of amyloid fibers and BAFs is 1:1. BAFs (26 and 31), which significantly reduces Aβ toxicity (Figure 3), cannot rescue the toxicity of IAPP and α-synuclein, suggesting that the toxicity alleviating effect of BAFs are specific to the fibers for which they were designed.

**Table 4.**
 Student’s t-test and p value analysis suggests that BAFs reduce the cytotoxicity of Aβ fibers significantly


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2">Average of cell viability (n = 4)</th>
      <th rowspan="2">SD(σ)</th>
      <th colspan="2">Comparison to Aβ fiber alone</th>
    </tr>
    <tr>
      <th>t value</th>
      <th>p value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="5">HeLa cell line</td>
    </tr>
    <tr>
      <td>Aβ fiber alone</td>
      <td>0.40</td>
      <td>0.05</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td>BAF1</td>
      <td>0.66</td>
      <td>0.04</td>
      <td>8.4</td>
      <td>5E-05</td>
    </tr>
    <tr>
      <td>BAF4</td>
      <td>0.93</td>
      <td>0.13</td>
      <td>7.4</td>
      <td>1E-4</td>
    </tr>
    <tr>
      <td>BAF8</td>
      <td>0.54</td>
      <td>0.06</td>
      <td>3.3</td>
      <td>1E-2</td>
    </tr>
    <tr>
      <td>BAF11</td>
      <td>0.69</td>
      <td>0.07</td>
      <td>6.6</td>
      <td>2E-04</td>
    </tr>
    <tr>
      <td>BAF12</td>
      <td>0.63</td>
      <td>0.04</td>
      <td>7.6</td>
      <td>1E-04</td>
    </tr>
    <tr>
      <td>BAF26</td>
      <td>0.68</td>
      <td>0.14</td>
      <td>3.8</td>
      <td>5E-3</td>
    </tr>
    <tr>
      <td>BAF30</td>
      <td>0.51</td>
      <td>0.08</td>
      <td>2.3</td>
      <td>4E-2</td>
    </tr>
    <tr>
      <td>BAF31</td>
      <td>0.91</td>
      <td>0.07</td>
      <td>11.5</td>
      <td>7E-06</td>
    </tr>
    <tr>
      <td colspan="5">PC12 cell line</td>
    </tr>
    <tr>
      <td>Aβ fiber alone</td>
      <td>0.37</td>
      <td>0.07</td>
      <td>/</td>
      <td>/</td>
    </tr>
    <tr>
      <td>BAF1</td>
      <td>0.61</td>
      <td>0.07</td>
      <td>4.9</td>
      <td>1E-3</td>
    </tr>
    <tr>
      <td>BAF4</td>
      <td>0.90</td>
      <td>0.11</td>
      <td>8.0</td>
      <td>7E-05</td>
    </tr>
    <tr>
      <td>BAF8</td>
      <td>0.53</td>
      <td>0.07</td>
      <td>3.2</td>
      <td>1E-2</td>
    </tr>
    <tr>
      <td>BAF11</td>
      <td>0.69</td>
      <td>0.07</td>
      <td>6.5</td>
      <td>2E-4</td>
    </tr>
    <tr>
      <td>BAF12</td>
      <td>0.49</td>
      <td>0.04</td>
      <td>2.9</td>
      <td>2E-2</td>
    </tr>
    <tr>
      <td>BAF26</td>
      <td>0.74</td>
      <td>0.13</td>
      <td>5.0</td>
      <td>1E-3</td>
    </tr>
    <tr>
      <td>BAF30</td>
      <td>0.60</td>
      <td>0.11</td>
      <td>3.5</td>
      <td>8E-3</td>
    </tr>
    <tr>
      <td>BAF31</td>
      <td>0.95</td>
      <td>0.14</td>
      <td>7.4</td>
      <td>1E-4</td>
    </tr>
  </tbody>
</table>

_The Student’s T-test and p-value are based on the comparison to Aβ fiber alone._

![Figure 4.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig4-v1.jpg)

**Figure 4.:** Orange G in an orange box is also displayed for comparison.

### Validation of compound binding by NMR titration

Promising candidate binders from in silico screening and toxicity tests were validated by titration of Aβ fibers into solutions of each compound, as monitored by NMR signals of aromatic protons of the compound (Figure 5). The proton resonances of the freely rotating compounds disappear as the compound binds to the fibers. By increasing the amount of fibers, an apparent Kd for compound binding can be estimated. From in silico screening, all tested BAF compounds are calculated to bind more tightly to Aβ fibers than orange G. In NMR studies, the apparent Kd of orange G binding to Aβ16–21 fibers was found to be 43 ± 21 µM, whereas the apparent Kd of BAF1 binding to Aβ16–21 fibers is 12 ± 7 µM. BAFs were found to bind to both Aβ16–21 fibers and Aβ1–42 fibers. Figure 5F shows a notable correlation between the calculated binding energies and the reduction in NMR peak areas upon Aβ binding. That is, all BAFs with predicted binding energy better than orange G also reduce NMR peak areas more than orange G. On the other hand, BAF31ΔOH, a derivative of BAF31 by removal of a key hydroxyl group essential for binding, exhibits both a worse calculated binding energy and a diminished reduction of NMR peak upon titration of Aβ1–42 fibers.

![Figure 5.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig5-v1.jpg)

**Figure 5.:** NMR binding experiments were performed on BAF compounds and the dye orange G. By monitoring the aromatic regions of the 1H NMR spectra of BAFs 1, 8, and 31, these compounds were shown to bind to both Aβ16–21 and Aβ1–42 fibers more tightly than does orange G. As shown in (A and B), BAF1 binds to Aβ16–21 fibers with affinity stronger than orange G. The determination of binding parameters for Aβ16–21 fibers is detailed in Table 5 and Figure 5—figure supplements 1 and 3. In panel (A), the 1H NMR spectrum of compound BAF1 (at 100 μM) is shown as a function of increasing concentration of Aβ16–21 fibers (0–500 μM, as monomer). The insert shows the area decrease of BAF1 NMR peaks as a function of Aβ16–21 concentration, and the red curve fitting the data defines an apparent Kd of 12 ± 7 µM. In panel (B), the NMR spectrum of orange G (50 μM) is plotted against increasing concentration of Aβ16–21 fibers (0–950 μM), giving an apparent Kd of 43 ± 21 µM. In (C, D and E), BAFs 1 and 8 both bind to Aβ1–42 fibers more strongly than orange G. Notice that the molar ratio of BAFs to Aβ1–42 fibers is comparable to that used in cell toxicity assays (Figure 3). (F). The calculated binding energies of BAFs—1, 8, and 31—to Aβ1–42 fibers are compared to the decreases in NMR peak of these compounds upon their binding to full-length Aβ fibers. These three BAFs have higher affinities and a larger NMR peak reduction than orange G while the ‘knock-out’ derivative with removal of key interactions (BAF31ΔOH) discussed below has a weaker calculated affinity and a smaller NMR peak reduction than orange G. We observe good correlation between computed energies and experimental data from NMR.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** The 1D 1H NMR spectrum shows the aromatic proton regions of BAF1 upon the titration of Aβ16–21 fibers shown in Figure 5A. The insert is the chemical structure of BAF1 with the color-labeled aromatic proton observed in the NMR spectrum. The arrows with different colors indicate the proton assignment for NMR peaks.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** The 1D 1H NMR spectrum shows the aromatic proton regions of orange G against the increasing concentrations of Aβ16–21 fibers shown in Figure 5B. The insert is the chemical structure of orange G with the highlighted label of the aromatic proton shown in the NMR spectrum. The arrows with different colors indicate the proton assignment for NMR peaks.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** To validate our computation methods, NMR titration experiments were performed. (A) One representative peak of aromatic protons of the 1D 1H NMR spectra of the compound BAF8 (at 100µM) upon Aβ16–21 fibers titration (0–500 µM, monomer equivalent). (B) Fitting curve upon the area decrease of BAF8 NMR peaks as a function of fiber concentration. The apparent Kd of BAF8 (24 ± 5 µM) is lower than that of orange-G (Figure 4B), indicating the tighter binding affinity of BAF8 to Aβ16–21 fibers.

**Table 5.**
 Predicted binding energy and experimental measurement of the binding of two BAFs and orange G against both Aβ16–21 (KLVFFA) and full-length Aβ fibers


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th colspan="2">Binding to KLVFFA fiber</th>
      <th colspan="2">Binding to Aβ fiber</th>
    </tr>
    <tr>
      <th>Predicted binding energy (kcal/mol)</th>
      <th>NMR Kd (µM)</th>
      <th>Predicted binding energy (kcal/mol)</th>
      <th>NMR peak reduction (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BAF1</td>
      <td>−8</td>
      <td>12</td>
      <td>−10</td>
      <td>8</td>
    </tr>
    <tr>
      <td>BAF8</td>
      <td>−12</td>
      <td>24</td>
      <td>−12</td>
      <td>13</td>
    </tr>
    <tr>
      <td>orange G</td>
      <td>−8</td>
      <td>43</td>
      <td>−9</td>
      <td>6</td>
    </tr>
  </tbody>
</table>

_The determination of the binding parameters with KLVFFA fiber is detailed in Table 6._

**Table 6.**
 Comparison of the measured binding parameters of the representative BAFs with orange G by NMR titrations


<table>
  <thead>
    <tr>
      <th>Compound</th>
      <th>Predicted binding energy (kcal/mol)</th>
      <th>fmax</th>
      <th>Kd (µM)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BAF1</td>
      <td>−8</td>
      <td>0.47 ± 0.04</td>
      <td>12 ± 7</td>
    </tr>
    <tr>
      <td>BAF8</td>
      <td>−12</td>
      <td>0.82 ± 0.04</td>
      <td>24 ± 5</td>
    </tr>
    <tr>
      <td>Orange-G</td>
      <td>−8</td>
      <td>0.46 ± 0.06</td>
      <td>43 ± 21</td>
    </tr>
  </tbody>
</table>

_The second column lists the predicted binding energy for each top docked model of BAF compounds with KLVFFA fiber, and the binding energy of Orange-G with KLVFFA fiber were also calculated for comparison. Our computational method identified the BAF with better fit to the binding interface than Orange-G. We then used NMR titration to determine the binding affinity. Our previous mass spectrometric analyses of the crystal of the Orange-G with KLVFFA fibers have suggested a binding ratio of compound:fiber with the range of 1:1 to 1:10 (Landau et al., 2011). Together with our structural models and single binding site assumption, we estimated the binding ratio to be 1:3. Accordingly, calculated NMR binding parameters are listed in the table. The third column fmax is the maximum fraction of NMR signal decrease of compound upon binding saturation (‘Materials and methods’)._

### Structure-activity relationship studies of the Aβ pharmacorphore

Based on the lead compounds found in the initial cycle of the procedure, we carried out a second cycle to expand our understanding of the Aβ pharmacorphore. BAF11 (Figure 6A), one of the lead compounds in the initial cycle, was used to perform structure-activity relationship studies. Twelve derivatives of BAF11 were scanned to pinpoint the essential apolar and polar interactions for the pharmacorphore refinement (Figure 6B, Figure 6—figure supplement 1). These derivatives are grouped in five classes, whose effects on Aβ toxicity have been tested (Figure 6C). Classes I and II assess the polar region of BAF11, which makes hydrogen bonds to charged Lys16 ladders of the Aβ fiber: the deletion of the hydroxyl group (Class I) significantly decreased the inhibition of toxicity; the swapping of the hydroxyl group with the aromatic tail (Class II) almost abolished inhibition of toxicity. Classes III, IV, and V focused on the aromatic moieties of BAF11: altering the sizes of aromatic groups (Class III) showed little change in inhibition of toxicity while adding charged or polar groups within aromatic region (Classes IV and V) resulted in a significant decrease of inhibition of toxicity. These differences among BAF11 derivatives in inhibition of toxicity (Figure 6C) further validated our structure-based approach and provided guidelines for the refinement of Aβ pharmacophore.

![Figure 6.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig6-v1.jpg)

**Figure 6.:** (A) Atomic model of BAF11 from the initial cycle docked on the full-length Aβ fiber, viewed in perpendicular to the fiber axis (left panel) and down the fiber axis (right panel). BAF11 is shown as a cyan stick model, whose polar groups form hydrogen bonds (green thick lines) to Lys16 of Aβ. The extensive non-polar interactions arise from the flat aromatic rings of BAF11 packing against the hydrophobic surface formed by Val18 and Phe20 of Aβ. (B) Schematic representation of the polar and nonpolar interactions of BAF11 and its derivatives modeled on the Aβ fiber (in orange and light brown). In the process of the Aβ pharmacophore refinement, five different classes (I–V) of BAF11 derivatives were introduced into the second cycle of screening, to expand the BAF set and to assess the specificity of the compounds identified in the initial cycle. The full description and chemical structure of each derivative are in Table 3 and Figure 5—figure supplement 1. (C) Comparison of the toxicity inhibition (defined in ‘Materials and methods’) among five types of BAF11 derivatives after 24 hr incubation with Aβ (0.5 µM). Notice that all changes to BAF11 which remove binding groups diminish its effectiveness as an inhibitor of toxicity.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** 12 derivatives of the lead compound BAF11 were included to expand the set during the refinement of amyloid pharmacophore (Figure 6C). (A) Chemical structures of BAF11 derivatives. A magenta open circle indicates the deletion of the important hydroxyl group. A green open circle indicates the missing of aromatic atoms in hydrophobic region of BAF11. The red color in chemical structures indicates the addition of atoms or groups to BAF11. The full description of each derivative is in Table 3. (B) Comparison of toxicity inhibition among BAF11 derivatives after 24 hour incubation with Aβ fibers.

In the second cycle, nine new compounds were derived from the refined pharmacophore (Figure 7). Three of them detoxified Aβ in cell survival assay. BAF31, the best inhibitor which protected mammalian cells from Aβ toxicity in the second cycle, increased cell survival from the 40% induced by Aβ alone to >90% (Figure 3). A derivative of BAF31, BAF31ΔOH, lacking the hydroxyl group believed to bind to the Lys residue of the Aβ fiber (shown by the magenta oval in Figure 8B), is calculated no longer to bind to the Aβ fiber. NMR and cell viability assessments indicated that BAF31ΔOH binds much less strongly to Aβ fibers than BAF31 itself and shows significantly reduced power to inhibit toxicity (Figure 8E). Similarly, the detoxifying profile of derivatives of another inhibitor, BAF30, validated the key interactions of BAF30 across the binding interface (Figure 9). Our conclusion is that the NMR binding and toxicity results for the BAF derivatives studied are consistent with our model for the pharmacophore of Aβ (Figure 10).

![Figure 7.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig7-v1.jpg)

**Figure 7.:** (A). Amyloid pharmacophore based on the structural overlay of active BAFs and derivatives. The overlay of the lead compounds from the initial round (BAF4, BAF8, and BAF11) elucidated the consensus of polar and nonpolar interactions at fiber binding interfaces, which sheds light on the amyloid pharmacophore. The amyloid pharmacophore was further refined by iterative approaches of computational docking and experimental testing. The derivatives of those lead compounds were tested to explore the essential role of those consensus interactions, and the differences of binding patterns and toxicity inhibition effects of the BAF derivatives can provide a guideline for the further refinement of amyloid pharmacophore. (B). New BAFs were ‘designed’ based on the refined pharmacophore. One successful example, BAF31 (green sticks) derived from the pharmacophore (grey sticks), showed the enhanced capability of inhibiting Aβ toxicity (Figure 8C). The success of developing enhanced binder from pre-defined pharmacophore highlights the important role of iterative docking/test approach in structure-based drug development.

![Figure 8.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig8-v1.jpg)

**Figure 8.:** (A) Atomic model of the new inhibitor BAF31 (our most tightly binding BAF) derived from the refined pharmacophore (Figure 7, Figure 1F) in the second cycle, viewed perpendicular to the fiber axis on the left and down the fiber axis on the right. In panel (B), one important hydroxyl group forming hydrogen bonds to Lys16 residue of Aβ is highlighted by a magenta circle. (C) A representative NMR band (left panel) of mixture of Aβ fiber with the compound BAF31 compares with that (right panel) of Aβ fiber the derivative BAF31ΔOH which omits that important hydroxyl group. Their full NMR spectrums showing the same trend are shown in Figure 8—figure supplement 1. (D) Cell survival rates after 24 hr incubation with Aβ (0.5 µM), the molar ratio (1:5) of Aβ and the compound is comparable with the ratio in NMR binding experiment (C). (E) Notably, the elimination of one hydrogen bond from BAF31 (the derivative BAF31ΔOH) causes both the marked decrease in inhibition of Aβ toxicity to HeLa cells (D) and the loss of NMR binding to Aβ fibers (C).

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** (A). 1D 1H NMR spectrum of BAF31 (100 µM) without (in black) and with Aβ1–42 fiber (12.5 µM monomer equivalent, in a green color). The magnified peaks are shown in the right panel to highlight the peak differences. (B). NMR spectrum of its derivative BAF31ΔOH (100 µM) when BAF31 is modified by the removal of a key hydroxyl group, without or with Aβ1–42 fiber (0 µM, 12.5 µM). The significant difference in NMR signal reduction between the BAF31 and BAF31ΔOH further validates the model of BAF31docked onto Aβ fibers.

![Figure 9.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig9-v1.jpg)

**Figure 9.:** Structural models of BAF30 (green sticks) docked on Aβ fiber structure (in a light yellow color) are shown in (A and B). The important polar (black hydrogen bonds) interaction between BAF30 and single β-sheet of Aβ fiber, as well as shape complimentary between the aromatic rings of BAF30 and the hydrophobic patches of Aβ fiber are highlighted respectively. Schematic representation of the polar and nonpolar interactions of BAF30 with Aβ fiber is shown in panel (C). The magenta circles highlight two important hydroxyl groups which are absent in BAF30 derivatives. (D). The chemical structure of each derivative is listed. The dark blue open circles indicate the deletion of the important hydroxyl group. The red color in chemical structures indicates the addition of atoms or groups to BAF30. (E). HeLa cell survival rates in the presence of Aβ (0.5 µM monomer equivalent) and BAF30 or the derivatives are compared. The hydrogen bonds between BAF30 and Lys16 residues of Aβ fiber are important for binding of Aβ fiber and inhibition of Aβ toxicity. With additional groups at the opposite side of hydrogen binding sites, the derivative BAF30αR showed little change in toxicity inhibition. However, two BAF30 derivatives (σOHAαOH and σOHAΔOHBαCOO), which alter or delete the two important hydroxyl groups (magenta circles in panel C) of BAF30 that form hydrogen bonds to Lys16, showed a significant decrease in the toxicity inhibition. Furthermore, when BAF30 was modified by shifting both hydroxyl groups (A and B) to their neighboring positions, the derivative BAF30σOHABαCH3 almost lost the inhibition of Aβ toxicity. The rescuing percentage (%) is defined in ‘Materials and methods’.

![Figure 10.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig10-v1.jpg)

**Figure 10.:** The carbonyl group is used to represent the H-bond acceptor (or negative charge) of BAFs, and the naphthalene ring is used to represent the planar aromatic portion of BAFs. Based on the rounds of computing search and experimental test, the detailed description about essential interactions and geometrical parameters are in ‘Materials and methods’.

## Discussion

### Structure-based discovery of compounds that bind amyloid fibers

Amyloid fibers differ fundamentally in structure from the enzymes and signaling proteins that are the traditional targets in structure based design of binding compounds, and thus their pharmacophores might be expected to differ fundamentally as would the types of compounds that bind. In general, the binding sites of the traditional targets are often concave pockets; in contrast, the surfaces of amyloid fibers are flat and repetitive along the fiber axis, without well-defined surface cavities. The widely used ligand-docking software, such as DOCK (Ewing et al., 2001), or AutoDock (Morris et al., 2009), is intended to fit well-defined protein pockets rather than shallow grooves at flat fiber surfaces.

Consequently we have adapted the RosettaLigand program (Davis and Baker, 2009) for docking a library of commercially available compounds onto the flat surface of amyloid fibers. Similarly to other software packages, RosettaLigand scores each candidate compound for its energetic fit to its binding site. The initial site is chosen near that occupied by a bound compound, as determined in a crystal structure. The conformational flexibilities of ligand and protein side chains are modeled in a ‘near-native’ perturbation fashion (‘Materials and methods’), meaning that the fine sampling of conformations was restrained to be close to the starting conformation. To find the position along the flat fibrillar surface of greatest binding energy for each candidate compound, our screening approach leverages the rotamer repacking algorithm (Leaver-Fay et al., 2011) and Rosetta energy function (Kuhlman and Baker, 2000) to account for flexibility of protein side chains and ligand, which is critical in modeling of such shallow grooves on the fiber surface.

Our procedure identified 34 BAF compounds predicted to bind to Aβ fibers, among which eight BAFs diminish the toxicity of the fibers in mammalian cells. We suggest that the same procedure can be used to discover other compounds that reduce the toxicity of Aβ fibers, starting from other co-crystal structures of Aβ segments with other bound ligands. Similarly, the same procedure can be applied to the discovery of compounds that bind to other amyloid proteins, for use as either toxicity inhibitors or imaging agents for amyloid diagnosis.

### Mechanism of inhibition of Aβ toxicity

Our observation is that our tightest binding BAFs all diminish the toxicity of Aβ fibers, and yet do not substantially diminish the amount of fibers. Further study will be required to understand the molecular mechanism underlying the inhibition of Aβ toxicity, but here we offer the following hypothesis.

Emerging evidence suggests that amyloid oligomers, rather than amyloid fibers, are toxic entities (Hartley et al., 1999; Cleary et al., 2005; Silveira et al., 2005), and that perhaps toxic oligomers can be released from amyloid fibers (Xue et al., 2009; Cremades et al., 2012; Krishnan et al., 2012; Shahnawaz and Soto, 2012). By binding to fibers, BAFs stabilize them, thereby shifting the equilibrium of Aβ molecules from smaller, toxic entities towards the fibrillar state. The BAF compounds in their computationally docked sites on Aβ fibers contact several (as few as three and as many as six) adjacent β-strands of the fiber. By creating a low energy binding interface across several fiber strands, the BAFs apparently stabilize the Aβ fibers from breaking into smaller entities.

From previous studies, we expect BAFs to bind to amyloid fibers rather than oligomers. In recent work (Laganowsky et al., 2012; Liu et al., 2012), we proposed that amyloid forming proteins can enter either of two distinct aggregation pathways, which are separated by an energy barrier. One pathway leads to in-register fibers in which every β-strand lies directly above or below an identical strand in the fiber. The other pathway leads to out-of-register oligomers in which antiparallel β-strands are sheared relative to one another and roll into a β-barrel. We found that three out-of-register amyloid-like structures exhibit cytotoxicity (Laganowsky et al., 2012; Liu et al., 2012), which tend to be transient, equilibrating eventually into in-register fibers. In our approach, we search for BAFs based on in-register β-sheets rather than out-of-register β-strands found in toxic oligomeric structures, to which our BAFs are not expected to bind (Figure 11). We speculate that BAFs stabilize the in-register fibers revealed by our steric zippers, relative to out-of-register toxic oligomers, thereby shifting the equilibrium from toxic oligomers towards fibers (Figure 12). Supporting this is our result that diminished toxicity accompanies compound binding.

![Figure 11.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig11-v1.jpg)

**Figure 11.:** As illustrated in (A), BAFs bind to in-register β-sheets. Our structure-based approach searches for BAFs based on in-register β-sheets in Aβ fibers. These BAFs are predicted to bind along the flat hydrophobic surfaces of the fibers and are anchored by polar sidechains of Lysine residues. The Cβ distances between the Lys residues interacting with the BAFs are ∼9.6 Å following the stacked arrangement of in-register β-sheets. Orange G, as well as screened BAFs, favorably interact with the in-register fiber and are compatible with the geometry of the Lys residues aligned in in-register β-sheets. As illustrated in (B), BAFs cannot bind to out-of-register β-sheets. The estimation of Cβ distance between the lysine residues, based on three out-of-register β-sheets structures previously determined (Laganowsky et al., 2012; Liu et al., 2012), ranges from 11 Å to 14 Å, quite different from the ∼9.6 Å measured in in-register β-sheet. We speculate that the BAFs are unable to bind to out-of-register β-sheets, and this difference accounts for the diminished toxicity that accompanies compound binding. Supporting this is our in vitro cell toxicity tests (Table 7 and Figure 11—figure supplement 1).

![Figure 11—figure supplement 1.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig11-figsupp1-v1.jpg)

**Figure 11—figure supplement 1.:** To assess if BAFs inhibit Aβ toxicity by directly interfering with toxic Aβ oligomers, four BAFs —1,11,26,31—, showing the inhibition to Aβ toxicity, were incubated with pre-formed Aβ oligomer and then tested by MTT cell viability assay using HeLa cell line. None of the BAFs significantly reduces toxicity of pre-formed Aβ oligomer. Aβ oligomer was prepared by incubating purified Aβ1–42 in PBS for 4 hr at 37°C at the concentration of 5 µM without agitation. Pre-formed Aβ oligomer was mixed with four different BAFs (Aβ1–42/BAFs = 1:1 molar ratio) and further incubated for 15 min to allow potential binding of BAFs to pre-formed oligomer. The final concentration of Aβ oligomer as monomer is 0.5 µM, the same as what we test Aβ toxicity in MTT cell viability assay.

**Table 7.**
 BAFs reduce Aβ cyto-toxicity by targeting fibers rather than oligomers.


<table>
  <thead>
    <tr>
      <th>Compound</th>
      <th>Inhibition to the cyto-toxicity of Abeta oligomers (%)</th>
      <th>Inhibition to the cyto-toxicity of Abeta fibers (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BAF1</td>
      <td>−4 ± 6</td>
      <td>36 ± 9</td>
    </tr>
    <tr>
      <td>BAF11</td>
      <td>−9 ± 7</td>
      <td>7 ± 7</td>
    </tr>
    <tr>
      <td>BAF26</td>
      <td>−6 ± 6</td>
      <td>26 ± 7</td>
    </tr>
    <tr>
      <td>BAF31</td>
      <td>−17 ± 15</td>
      <td>58 ± 7</td>
    </tr>
  </tbody>
</table>

_The BAF inhibitions of toxicity from either Aβ oligomer or fibers are compared. Four BAFs, which reduce the toxicity of Aβ fibers, show no inhibitory effects to Aβ oligomer toxicity at the equal molar ratio of BAF to Aβ. The inhibition (%) are calculated using the same method defined in ‘Materials and methods’. The toxicity assay of Aβ oligomer is described in Figure 11—figure supplement 1. The toxicity assay of Aβ fiber is the same as that described in Figure 3._

![Figure 12.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig12-v1.jpg)

**Figure 12.:** BAFs (green) bind to the side of amyloid fibers, stabilizing the fiber, and shifting the equilibrium from smaller and more toxic oligomers towards fibers. This shift in equilibrium reduces amyloid toxicity.

### BAFs strengthen the hypothesis that Aβ16–21 fibers reflect essential features of full Aβ fibers

The identification of BAFs starts with the atomic structure of orange G bound within the fiber-like crystals of Aβ16–21, because as yet there is no high-resolution atomic structure available for ligands bound to full-length Aβ fibers. Nevertheless, we found that BAFs diminish toxicity of full-length Aβ fibers. This finding suggests that the steric zipper structure of Aβ16–21 fibers recapitulates some of the essential structural features of full-length Aβ fibers. We are currently attempting cocrystallization of BAFs with Aβ16–21 and other steric zipper structures. We speculate that coupled with computational methods, other steric zipper structures could enable the discovery of the lead compounds for inhibitors of other toxic amyloid entities.

## Materials and methods

### Computational procedures

#### Two choices of compound libraries for structure-based screening

We generated two sets of purchasable compounds to be screened via the computational docking:Cambridge Structure Database (CSD) set. 102,236 organic compounds, whose crystal structures have R-factor better than 0.1, were extracted from the Cambridge Structure Database (version 5.32 November 2010) using ConQuest. The SMILES string of each structure was then used to locate its purchasing information among the ZINC purchasable set (http://zinc.docking.org/) (Irwin and Shoichet, 2005) by OpenBabel package (http://openbabel.org/) (Guha et al., 2006). The fast index table of all SMILES strings of the ZINC purchasable set was generated to allow the fast search of each CSD structure against ZINC purchasable set. CSD structures that failed in locating their purchasing information (i.e., without any hit in searching against ZINC purchasable set) were omitted. A library of 13,918 structures from CSD representing 11,057 compounds were finally compiled, whose purchasing information is annotated by ZINC purchasable database. The complete list of CSD/ZINC entries of these compounds in this CSD set can be found in Supplementary file 1.Flat Compound (FC) set. A library of 6589 compounds containing phenol and less than three freely rotatable bonds were extracted from the ZINC database (http://zinc.docking.org/) (Irwin and Shoichet, 2005). Those compounds have a common feature of planar aromatic ring, resulting in a ‘flat’ compound. The flat compound library includes compounds with similar chemical structures to naturally fiber-binding molecules, for instance, Thioflavin-T (ThT), Congo red, Green tea epigallocatechin-3-gallate (EGCG), and Curcumin. It also includes many natural phenols, such as gallic acid, ferulic acid, coumaric acid, propyl gallate, epicatechin, epigallocatechin, etc. The complete list of ZINC entries of these compounds in this FC set can be found in Supplementary file 2.

### Ligand ensemble preparation with near-‘native’ perturbation

Each molecule in our two compound libraries was prepared for the docking simulations. Hydrogen atoms of each molecule were added for the compounds lacking modeled hydrogens using the program Omega (v. 2.3.2, OpenEye) (Bostrom et al., 2003). Ligand atoms were represented by the most similar Rosetta atom type, their coordinates were re-centered to the origin, and their partial charges were assigned by OpenEye’s AM1-BCC implementation. We then generated the ligand perturbation ensemble near the crystal conformation (CSD set) or starting conformation (FC set) of each molecule. For each rotatable bond of the ligand, a small degree torsion angle deviation (±5°) was applied. K-mean clustering method was used to generate the ligand perturbation ensemble and similar/redundant conformations (rmsd to the selected conformation is less than 0.5 Å) were omitted. Finally, up to 100 conformations for each ligand were generated and made available for Rosetta LigandDock.

### Rosetta LigandDock with additional near ‘native’ perturbation sampling

We adopted the docking algorithm based on the method previously described in the RosettaLigand docking paper (Meiler and Baker, 2006; Davis and Baker, 2009). In general, the algorithm includes three stages: coarse-grained stage, Monte Carlo minimization (MCM) stage and gradient-based minimization stage. Whereas the original RosettaLigand method performed a full sampling of torsional degrees of freedom in the internal ligands and protein side-chains, we made modifications to enable the fast run time required by the screening method. Specially, we sampled the ligand and protein side-chain torsion angles in near-‘native’ perturbation fashion, where only the near-‘native’ conformation of side-chain and ligand rotamers were allowed and any conformation far away from the starting conformation was omitted. For each protein side-chain, the deviations (±0.33, 0.67, 1 SD) around each input torsion were applied based on the standard deviation value of the same torsion bin from the backbone-dependent Dunbrack rotamer library. For each internal torsional angle of the ligand, the deviations (±5°) around the input torsion were applied as described above.

To optimize possible interactions (H-bonding or packing) between compound and fiber, we carried out random perturbations to the TS rigid-body degrees of freedom (5 Å for translational degrees of freedom; 360° for full rotational degrees of freedom) to explore different rigid body arrangements. For each rigid-body perturbation, different conformations of fiber sidechains, and compounds were explored to maximize the binding interactions. We next carried out simultaneous quasi-Newton optimization of the compound rigid body orientation and the sidechain torsion angles, and in some cases, the torsion angles of the compound and the backbone torsion angles in the binding site, using the complete Rosetta energy function.

### Docking of molecules to KLVFFA and Aβ fibrillar structure

The structure of KLVFFA fiber was taken from the co-crystal structure of KLVFFA with orange G (pdb entry: 3OVJ) (Landau et al., 2011). After removing orange G, the sidechain torsion of KLVFFA was optimized to correct any conformational bias from the presence of orange G, and then the optimized structure were inspected to ensure that sidechain torsions are still within the original conformation of the co-crystal structure. The Aβ fibrillar structure was from ssNMR fiber structure of full-length Aβ (pdb entry: 2LMO) 40. The same optimization step was applied before docking. The comparison of docking onto both KLVFFA and Aβ fibrillar structure are discussed in Figure 13.

![Figure 13.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig13-v1.jpg)

**Figure 13.:** A subtlety of our procedure for compound discovery is that it involves both parallel (A) and antiparallel (B) amyloid β-sheets. In the X-ray structure of orange G bound to the segment Aβ16–21(KLVFFA) of Aβ, the sheets are antiparallel (B). The library of compounds is initially selected based on docking to the antiparallel β-sheet of Aβ16–21. In the next step of our procedure, each compound is further screened against the solid-state-NMR-derived model of full-length Aβ fiber, which is a parallel sheet (A). The structure models of orange G docked onto Aβ16–21 structure and full-length Aβ model are shown in Figure 13—figure supplement 1. As simplified here in (A and B), sulfate ions (red) of orange G are respectively hydrogen bonded to two lysine residues (light brown), which keep nearly identical geometry (the same ∼9.6 Å distance between the two lysine residues) in either parallel or antiparallel sheet. Evidence that orange G, as well as BAF compounds identified by our procedure, all bind to both antiparallel and parallel sheets is given by the NMR experiments summarized in Figure 5, where orange G and BAFs are shown to bind to both Aβ16–21 and full-length Aβ fibers. Apparently both parallel and antiparallel amyloid β-sheets are effective in binding to the same compounds.

![Figure 13—figure supplement 1.](https://cdn.elifesciences.org/articles/00857/elife-00857-fig13-figsupp1-v1.jpg)

**Figure 13—figure supplement 1.:** (A). The side view of orange G (in an orange color) docked on the Aβ16–21 fiber (in a grey color) with a predicted binding energy of—8 kcal/mol. (B) side view of orange G (in an orange color) docked on the Aβ full fiber (in a light pink color) with a predicted binding energy of—9 kcal/mol. The charge interactions between the orange G and Lysine 16 are highlighted by dark grey lines.

### Post-docking analysis to rank the compounds

The docked compounds were filtered based on the following criteria: (1) The docking models with a compound-fiber van der Waals attractive energy > −7.0 kcal/mol were removed; (2) The docking models with a compound-fiber hydrogen-binding energy >−0.2 kcal/mol were eliminated. The remaining docked compounds were then ranked according to the energy of binding of compound to fiber. We used not only the total binding energy but also on each of the energy components separately (Lennard-Jones interactions, solvation, hydrogen bonding, and electrostatics) (Lazaridis and Karplus, 1999; Kuhlman and Baker, 2000; Kortemme et al., 2003) for ranking. The compounds ranked in the top 40% according to all of these measures were selected. Finally, the compounds were ranked by tightest binding energy (Meiler and Baker, 2006) and best shape complementarity (Lawrence and Colman, 1993).

### Description of geometrical parameters of the interactions between BAFs and Aβ fiber defined based on structure-based screening of Aβ toxicity inhibitor

Based on the rounds of computing search and experimental test, general rules of the essential interactions of BAF binding to Aβ fibers are summarized here. As illustrated in Figure 10, the geometrical parameters of those key interactions are specified as followings:H-bond acceptor (or negative charge) of the inhibitor makes either hydrogen bond or salt bridge to sidechain nitrogen atoms (NZ) of at least two Lysine residues from adjacent Aβ strands along the fiber axis. Our data suggest that the BAFs need to have good contacts across 2 to 4 adjacent Aβ strands, in order to effectively bind to Aβ fiber and reduce Aβ toxicity.The hydrogen bond or salt bridge described in 1) follows the general rule of H-bond geometry, which are:Distance (d1, as shown in the figure) between the NZ atom of Lys16 and H-bond acceptor atoms of BAFs: 2.8∼3.5 angstrom;Angle (Θ1) at BAF H-bond acceptor atoms:100∼150°;Angle (Θ2) at the NZ atom of Lys16: 130∼180°.Hydrophobic interactions between the apolar residues (phenylalanine18 and valine 20) and the planar aromatic portion of the compounds. The aromatic portion of compounds should be planar or semi-planar to pack against the flat surface of Aβ which spans across at least two adjacent Aβ strands.The hydrophobic interactions described in 3) follow the pi-pi stacking geometry, which are:Distance (d2) between the center of the apolar sidechains and the center of BAF aromatic rings: 4.0∼5.0 angstrom;Dihedral angle (Φ) between the surface plane defined by Phe18 and Val20 and the aromatic ring of the BAFs: 0∼40°.

### Experimental procedures

#### Chemicals and reagents

Chemicals were obtained from a variety of companies (Table 1) and were of the highest purity available.

#### Source of KLVFFA(Aβ16–21) and Aβ1–42 peptide

N-terminal acetylated and C-terminal amidated KLVFFA(Aβ16–21) peptide was synthesized by Celtek Bioscience Peptides (Nashville, TN). Aβ1–42 peptide was overexpressed through Escherichia coli recombinant expression system and was purified as reported previously (Finder et al., 2010). The fusion construct for Aβ1–42 expression contains an N-terminal His tags, followed by 19 repeats of Asn-Ala-Asn-Pro, TEV protease site and the human Aβ1–42 sequence. Briefly, the fusion construct was expressed into inclusion bodies in E.coli BL21(DE3) cells. 8 M urea was used to solubilize the inclusion bodies. Fusion proteins were purified through HisTrap HP Columns, followed by Reversed-phase high-performance liquid chromatography (RP-HPLC). After TEV cleavage, Aβ1–42 peptide was purified from the cleavage solution by RP–HPLC followed by lyophilization. To disrupt preformed aggregation, lyophilized Aβ1–42 was resuspended in 100% Hexafluoroisopropanol (HFIP) which was finally removed by evaporation.

#### Preparation of KLVFFA (Aβ16–21) and Aβ1–42 fiber samples for 1D 1H NMR titration measurement

KLVFFA (Aβ16–21) peptide was dissolved in PBS buffer, pH 7.4 at the concentration of 1 mM and incubated at 37° with continuing shaking for 3 months. Pre-disaggregated Aβ1–42 was dissolved in PBS buffer, pH 7.4 at the concentration of 200 μM and incubated at 37° with continuing shaking for 2 months. For NMR titration samples preparation, KLVFFA (Aβ16–21) or Aβ1–42 fiber stocks were diluted in the PBS buffer solution at the indicated concentrations, followed by adding the small molecules from 100 mM stock solutions in DMSO into fibrillar solution. The final concentration of the small molecule was 50uM or 100 μM. The final volume of NMR samples was 500 μL containing 5% D2O. Prior to NMR spectra collection, samples were incubated at room temperature for 0.5 hr. 500 MHz 1H NMR spectra were collected on a Bruker DRX500 at 283 K with either 256 or 1024 scans collected depending on the intensity of the small molecule signal. H2O resonance was suppressed via excitation sculpting (Hwang and Shaka, 1995); DMSO resonance was suppressed via a frequency shifted presaturation of the DMSO peak. Spectra were processed with XWINNMR 3.6.

#### Dissociation constant (Kd) of small molecules to fibers calculated from NMR data

NMR data were analyzed to estimate the binding constant for the interaction between the BAF compounds and KLVFFA fibers. We monitored the decrease in the 1H aromatic resonance of the compounds as a function of increasing concentrations of KLVFFA fibers. The general equation for deriving the apparent dissociation constant (Kd) is as follows:

For a general reaction of a ligand binding to fibers (containing N monomers):

$$
F(ibril)_{N}+L(igand)↔F_{N}L
$$

.

We estimated the concentration of fibers at any given monomer concentration as:

$$
[F(iber)N]=[Fmomomer]∗(1 fiber/N monomers),
$$

and then we could get:

$[F_{N}]=\frac{[F ]_{T}}{N}−[F_{N}L]$, $[L]=[L]_{T}−[F_{N}L]$, where [F]T is the total monomer concentration, [L]T is the total ligand concentration and [FNL] is the concentration of bound fiber;

$$
K_{d}=\frac{[F_{N}][L]}{[F_{N}L]} and K_{d}=\frac{(\frac{[F ]_{T}}{N}−[F_{N}L])([L]_{T}−[F_{N}L])}{[F_{N}L]},
$$

and thus

$$
[F_{N}L]^{2}−(\frac{[F ]_{T}}{N}+[L]_{T}+K_{d})[F_{N}L]+\frac{[F ]_{T}[L]_{T}}{N}=0.
$$

Finally, we could get the concentration of bound complex [FNL]:

$$
[F_{N}L]=\frac{(\frac{[F ]_{T}}{N}+[L]_{T}+K_{d})−\sqrt{(\frac{[F ]_{T}}{N}+[L]_{T}+K_{d})^{2}−\frac{4[F ]_{T}[L]_{T}}{N}}}{2}
$$

We then applied this equation (1) to our NMR experiments, where we monitored the integrated area of each NMR peak (A) of the compounds over a range of KLVFFA fiber concentrations. Assuming the complex of the BAF compound with fiber is in fast exchange, the peak area is the average of the peak signals for free and bound states, weighted by the fraction of the observed molecule in each state:

$$
A=f_{L}A_{L}+f_{F_{N}L}A_{F_{N}L}.
$$

And the change in NMR peak area (ΔA),

$$
ΔA=A_{L}−A=f_{F_{N}L}(A_{L}−A_{F_{N}L})
$$



$$
\frac{ΔA}{(A_{L}−A_{F_{N}L})}=\frac{ΔA}{ΔA_{max}}=\frac{ΔA/A_{L}}{ΔA_{max}/A_{L}}=\frac{%_{ΔA}}{%_{ΔA_{max}}}=f_{F_{N}L}=\frac{[F_{N}L]}{[L]_{T}}
$$



$$
ΔA/A_{L}=ΔA_{max}/A_{L}\frac{(\frac{[F ]_{T}}{N}+[L]_{T}+K_{d})−\sqrt{(\frac{[F ]_{T}}{N}+[L]_{T}+K_{d})^{2}−\frac{4[F ]_{T}[L]_{T}}{N}}}{2[L]_{T}}.
$$

Hence, the observed fraction of peak area change during the titration of increasing fiber concentration against fixed small compound,

$$
f_{obs}=f_{max}\frac{(\frac{[F ]_{T}}{N}+[L]_{T}+K_{d})−\sqrt{(\frac{[F ]_{T}}{N}+[L]_{T}+K_{d})^{2}−\frac{4[F ]_{T}[L]_{T}}{N}}}{2[L]_{T}}.
$$

Our structural model suggests that one BAF compound binds three fiber monomers. To obtain the Kd, we fit the equation for 1:3 (small molecule:fiber) binding to the NMR titration curve (N = 3), with $f_{obs}$ defined as the fraction of peak area decrease $(\frac{ΔA}{A_{L}})$ for each titration experiment, and $f_{max}$ defined as the fraction maximum of peak area decrease $(\frac{A_{max}}{A_{L}})$ for the saturated complex.

#### MTT cell viability assay

We performed MTT-based cell viability assay to assess the cytotoxicity of Aβ1–42 with or without the addition of BAFs and orange G. A CellTiter 96 aqueous non-radioactive cell proliferation assay kit (MTT) (Promega cat. #G4100, Madison, WI) was used. HeLa and PC-12 (ATCC; cat. # CRL-1721, Manassas, VA) cell lines were used for measuring the toxicity of Aβ1–42. Prior to toxicity test, both HeLa and PC-12 cell lines were plated at 10,000 cells per well in 96-well plates (Costar cat. # 3596, Washington, DC). HeLa cells were cultured in DMEM medium with 10% fetal bovine serum, PC-12 cells were cultured in ATCC-formulated RPMI 1640 medium (ATCC; cat.# 30–2001) with 10% heat-inactivated horse serum and 5% fetal bovine serum. Cells were cultured in 96-well plates for 20 hr at 37°C in 5% CO2. For Aβ1–42 and BAFs samples preparation, purified Aβ1–42 was dissolved in PBS at the final concentration of 5 μM, followed by the addition of BAFs at indicated concentrations. The mixtures were filtered with a 0.2-μm filter and further incubated for 16 hr at 37°C without shaking for fiber formation. To start the MTT assay, 10 μl of pre-incubated mixture was added to each well containing 90 μl medium. After 24 hr incubation at 37°C in 5% CO2, 15 μl Dye solution (Promega cat. #G4102) was added into each well. After incubation for 4 hr at 37°C, 100 μl solubilization Solution/Stop Mix (Promega cat. #G4101) was added to each well. After 12 hr incubation at room temperature, the absorbance was measured at 570 nm with background absorbance recorded at 700 nm. Four replicates were measured for each of the samples. The MTT cell viability assay measured the percentage of survival cell upon the treatment of the mixture of Aβ1–42 and BAFs. The toxicity inhibition (%) or rescuing percentage (%) of each BAF compound was calculated by normalizing the cell survival rate using the PBS buffer-treated cells as 100% and 0.5 μM (final concentration) Aβ1–42 fiber alone-treated cell as 0% viability.

#### Transmission electron microscopy (TEM)

TEM was performed to visualize the fibrillation of Aβ1–42 in presence of BAFs. The samples of Aβ1–42 and BAFs mixture for TEM measurement were the same as those for MTT assay. For specimen preparation, 5 μl solution was spotted onto freshly glow-discharged carbon-coated electron microscopy grids (Ted Pella, Redding, CA). Grids were rinsed twice with 5 μl distilled water after 3 min incubation, followed by staining with 1% uranyl acetate for 1 min. A CM120 electron microscope at an accelerating voltage of 120 kV was used to examine the specimens. Images were recorded digitally by TIETZ F224HD CCD camera.

#### ThT fibrillation assay

Purified Aβ1–42 was dissolved in 10 mM NaOH at the concentration of 200 μM, followed by sonication for further solubilizing Aβ1–42. Aβ1–42 was diluted into PBS buffer at the final concentration of 20 μM, and was mixed with 20 μM Thioflavin T (ThT) and different concentrations of BAFs. The reaction mixture was filtered with a 0.2 μm filter, split into four replicates and placed in a 96-well plate (black with flat optic bottom). The ThT fluorescence signal was measured every 5 min using the Varioskan plate reader (Thermo Fisher Scientific, Inc) with excitation and emission wavelengths of 444 and 484 nm, respectively, at 37°C.
