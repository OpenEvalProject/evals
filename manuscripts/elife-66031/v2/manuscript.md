# Organ geometry channels reproductive cell fate in the Arabidopsis ovule primordium

## Authors

- Elvira Hernandez-Lagana<sup>1</sup> ([ORCID: 0000-0002-2645-3783](https://orcid.org/0000-0002-2645-3783))
- Gabriella Mosca<sup>2</sup> ([ORCID: 0000-0003-4509-498X](https://orcid.org/0000-0003-4509-498X))
- Ethel Mendocilla-Sato<sup>2</sup> ([ORCID: 0000-0003-0339-3535](https://orcid.org/0000-0003-0339-3535))
- Nuno Pires<sup>2</sup> ([ORCID: 0000-0002-7113-3519](https://orcid.org/0000-0002-7113-3519))
- Anja Frey<sup>2</sup>
- Alejandro Giraldo-Fonseca<sup>2</sup>
- Caroline Michaud<sup>1</sup> ([ORCID: 0000-0002-0620-2442](https://orcid.org/0000-0002-0620-2442))
- Ueli Grossniklaus<sup>2</sup> ([ORCID: 0000-0002-0522-8974](https://orcid.org/0000-0002-0522-8974))
- Olivier Hamant<sup>3</sup> ([ORCID: 0000-0001-6906-6620](https://orcid.org/0000-0001-6906-6620))
- Christophe Godin<sup>3</sup> ([ORCID: 0000-0002-1202-8460](https://orcid.org/0000-0002-1202-8460))
- Arezki Boudaoud<sup>3</sup> ([ORCID: 0000-0002-2780-4717](https://orcid.org/0000-0002-2780-4717))
- Daniel Grimanelli<sup>1</sup> ([ORCID: 0000-0001-5424-114X](https://orcid.org/0000-0001-5424-114X))
- Daphné Autran<sup>1</sup> ([ORCID: 0000-0002-5227-8966](https://orcid.org/0000-0002-5227-8966)) †
- Célia Baroux<sup>2</sup> ([ORCID: 0000-0001-6307-2229](https://orcid.org/0000-0001-6307-2229)) †

### Affiliations

1. DIADE, University of Montpellier, CIRAD, IRD Montpellier France
2. Department of Plant and Microbial Biology and Zurich-Basel Plant Science Center, University of Zürich Zürich Switzerland
3. Laboratoire Reproduction et Développement des Plantes, University of Lyon, ENS Lyon, UCB Lyon 1, CNRS, INRAE, INRIA Lyon France

† Corresponding author

## Abstract

In multicellular organisms, sexual reproduction requires the separation of the germline from the soma. In flowering plants, the female germline precursor differentiates as a single spore mother cell (SMC) as the ovule primordium forms. Here, we explored how organ growth contributes to SMC differentiation. We generated 92 annotated 3D images at cellular resolution in Arabidopsis. We identified the spatio-temporal pattern of cell division that acts in a domain-specific manner as the primordium forms. Tissue growth models uncovered plausible morphogenetic principles involving a spatially confined growth signal, differential mechanical properties, and cell growth anisotropy. Our analysis revealed that SMC characteristics first arise in more than one cell but SMC fate becomes progressively restricted to a single cell during organ growth. Altered primordium geometry coincided with a delay in the fate restriction process in katanin mutants. Altogether, our study suggests that tissue geometry channels reproductive cell fate in the Arabidopsis ovule primordium.

## Introduction

A hallmark of sexual reproduction in multicellular organisms is the separation of the germline from the soma. In animals, primordial germ cells (PGCs) are set-aside during embryogenesis from a mass of pluripotent cells. The number of germ cells depends on the balance between proliferation (self-renewal) and differentiation, a process controlled by both intrinsic factors and signals from the surrounding somatic tissues. In flowering plants, the first cells representing the germline, the spore mother cells (SMCs), differentiate only late in development. SMCs arise multiple times, in each flower during the formation of the reproductive organs. In Arabidopsis, the female SMC differentiates in the nucellus of the ovule primordium, a digit-shaped organ that emerges from the placental tissue of the gynoecium. The SMC is recognizable as a single, large, and elongated subepidermal cell, which is centrally positioned within the nucellus and displays a prominent nucleus and nucleolus (Bajon et al., 1999; Bowman, 1993; Schmidt et al., 2015; Schneitz et al., 1995).

Although SMC singleness may appear to be robust, more than one SMC candidate per primordium is occasionally seen, yet at different frequencies depending on the specific Arabidopsis accession (~5% in Landsberg erecta [Ler], 10% in Columbia [Col-0], 27% in Monterrosso [Mr-0]), (Grossniklaus and Schneitz, 1998; Rodríguez-Leal et al., 2015). Arabidopsis, maize, and rice mutants in which SMC singleness is compromised have unveiled the role of regulatory pathways involving intercellular signaling, small RNAs, as well as DNA and histone methylation (Garcia-Aguilar et al., 2010; Mendes et al., 2020; Nonomura et al., 2003; Olmedo-Monfil et al., 2010; Schmidt et al., 2011; Sheridan et al., 1996; Sheridan et al., 1999; Su et al., 2020; Su et al., 2017; Zhao et al., 2008). As the SMC forms, cell-cycle regulation contributes to the stabilization of its fate in a cell-autonomous manner through cyclin-dependent kinase (CDK) inhibitors and RETINOBLASTOMA-RELATED1 (RBR1) (Cao et al., 2018; Zhao et al., 2017). SMC singleness thus appears to result from a two-step control: first, by restricting differentiation to one cell and second, by preventing self-renewal before meiosis (reviewed in Lora et al., 2019; Pinto et al., 2019).

However, the precise mechanisms underlying the plasticity in the number of SMC candidates and SMC specification are still poorly understood. In principle, SMC singleness may be controlled by successive molecular cues. However, even in that scenario, such cues must be positional, at least to some extent, and thus involve a spatial component. Over the last decade, many different molecular cues defining spatial patterns in the ovule primordium were identified (Pinto et al., 2019; Su et al., 2020); however, their coordination is unknown. Since SMCs emerge at the primordium apex concomitant with its elongation, we hypothesize that geometric constraints during ovule morphogenesis influence SMC singleness and differentiation. Such a hypothesis could explain variation in the number of SMC candidates, ultimately culminating in a single SMC entering meiosis. Answering the questions of whether SMC formation follows a stereotypical or plastic developmental process and whether it is intrinsically linked to or independent of ovule primordium formation would unravel fundamental principles connecting cell fate establishment and organ growth.

Such an analysis requires a high-resolution description of ovule geometry during development. Our current knowledge of ovule primordium growth in Arabidopsis is based on two-dimensional (2D) micrographs from tissue sections or clearing. It is described in discrete developmental stages capturing classes of primordia by their global shape and SMC appearance until meiosis and by the presence of integument layers and ovule curvature later on (Grossniklaus and Schneitz, 1998). In addition, a 3D analysis of average cell volumes during primordium growth was recently provided (Lora et al., 2017), and extensive 3D analysis was carried on for late ovule stages (Vijayan et al., 2021). Yet, we lack a view of the patterning processes regulating early ovule primordium formation and how the dynamics of cell proliferation contributes to the cellular organization during primordium growth. Thus, we described and quantified the growth of the ovule primordium at cellular resolution in 3D. We combined 3D imaging, quantitative analysis of cell and tissue characteristics, reporter gene analyses, and 2D mechanical growth simulations. In addition, using the katanin mutant that affects anisotropic cell growth and division patterns (Luptovčiak et al., 2017a; Ovečka et al., 2020), we show that altered ovule morphology leads to ectopic SMC candidates. We also uncovered that differentiation of SMC candidates initiate earlier than previously thought, and provide evidence for a gradual process of cell fate restriction, channeling the specification of a single SMC prior to meiosis.

## Results

### Building a reference image dataset capturing ovule primordium development at cellular resolution

To generate a reference image dataset describing ovule primordium development in 3D and with cellular resolution, we imaged primordia at consecutive stages in intact carpels by confocal microscopy. Carpels were cleared and stained for cell boundaries using a modified PS-PI staining (Truernit et al., 2008) and mounted using a procedure preserving their 3D integrity (Mendocilla Sato and Baroux, 2017; Figure 1A). We selected high signal-to-noise ratio images and segmented them based on cell boundary signals using Imaris (Bitplane, Switzerland) as described previously (Mendocilla Sato and Baroux, 2017; Figure 1B). We manually curated 92 ovules representing seven consecutive developmental stages (7–21 ovules per stage, Figure 1B, Table 1, Figure 1—source data 1) and classified them according to an extended nomenclature (explained in Materials and methods). The temporal resolution of our analysis led us to subdivide early stages (stage 0-I to stage 0-III) covering primordium emergence prior to the straight digit-shape of the organ set as stage 1-I, where the SMC becomes distinguishable by its apparent larger size in longitudinal views (Grossniklaus and Schneitz, 1998; Figure 1B).

![Figure 1.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig1-v2.jpg)

**Figure 1.:** (A) 3D reconstruction of a whole gynoecium stained with PS-PI (cell wall dye) and visualized by CSLM. The cross-section shows nascent ovule primordia attached to the placenta. (B) Ovule primordium developmental stages (0-I to 2-II) and organ viewpoints (domains) defined for 3D quantitative analyses. All segmented data can be analyzed by an interactive interface named OvuleViz. See also Figure 1—figure supplement 1A–C. n = number of ovules analyzed. Segmented images for all developmental stages are provided in Figure 1—source data 1. See also Figure 1—figure supplement 1D–E, Materials and methods.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) OvuleViz, an interactive interface enabling the analysis of segmented data based on exported cell statistics. The different snapshots display several features of OvuleViz, enabling the generation of plots from chosen cell statistics for chosen ovule primordium stage, genotype, cell labels or groups thereof (viewpoints). (B) Examples of plot types that can be generated by OvuleViz. (C) Possibility to export all or a subset of data as summary table or raw dataframe for further analyses external to OvuleViz. (D) PCA of cell descriptors from the wild-type reference dataset (Arabidopsis Col-0) (see Figure 1—source data 1), for all cell types and all stages. PCA was performed on a dataset containing Sphericity, Ellipticity oblate, Ellipticity prolate, Area, and Volume. Only the first and the second Principal Components (PCs) are shown. The loading plot and table indicate the variables’ contribution to each component. (E) Same as (D) for all cell types grouped by stage: stage 0 (0-I; 0-II), stage 1 (1-I; 1-II), and stage 2 (2-I; 2-II). Variables’ contributions are presented by loading plots for each PC and summary table.

**Table 1.**
 Classification criteria of Arabidopsis ovule primordia.The table summarizes general characteristics of ovule primordia per stage: cell ‘layers’ above the placenta scored as the number of L1 cells in a cell file drawn from the basis to the top, range thereof, total cell number, ovule shape including height, width, aspect ratio. See also Figure 1—source data 1.


<table>
  <tbody>
    <tr>
      <td></td>
      <td colspan="3">0-I</td>
      <td colspan="3">0-II</td>
      <td colspan="3">0-III</td>
    </tr>
    <tr>
      <td>Cells above placenta*</td>
      <td>2.5</td>
      <td>(±3.5)</td>
      <td>(n = 21)</td>
      <td>3.6</td>
      <td>(±0.5)</td>
      <td>(n = 17)</td>
      <td>5.9</td>
      <td>(±1.0)</td>
      <td>(n = 11)</td>
    </tr>
    <tr>
      <td>Range (min-max)</td>
      <td>2</td>
      <td>-</td>
      <td>3</td>
      <td>3</td>
      <td>-</td>
      <td>4</td>
      <td>5</td>
      <td>-</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Total # cells</td>
      <td>28</td>
      <td>(±5.7)</td>
      <td>(n = 21)</td>
      <td>38</td>
      <td>(±8.0)</td>
      <td>(n = 17)</td>
      <td>80</td>
      <td>(±8.4)</td>
      <td>(n = 11)</td>
    </tr>
    <tr>
      <td>Width (µm) (W)</td>
      <td>23</td>
      <td>(±3.5)</td>
      <td></td>
      <td>26.3</td>
      <td>(±2.4)</td>
      <td></td>
      <td>28.0</td>
      <td>(±3.1)</td>
      <td></td>
    </tr>
    <tr>
      <td>Height (µm) (H)</td>
      <td>5.3</td>
      <td>(±1.2)</td>
      <td></td>
      <td>11.9</td>
      <td>(±2.1)</td>
      <td></td>
      <td>22.5</td>
      <td>(±3.6)</td>
      <td></td>
    </tr>
    <tr>
      <td>H:W ratio</td>
      <td>0.2</td>
      <td>(±0.04)</td>
      <td>(n = 13)</td>
      <td>0.45</td>
      <td>(±0.06)</td>
      <td>(n = 14)</td>
      <td>0.8</td>
      <td>(±0.12)</td>
      <td>(n = 8)</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="3">1-I</td>
      <td colspan="3">1-II</td>
      <td rowspan="11" colspan="3">* scoring the length of L1 cell file above placenta</td>
    </tr>
    <tr>
      <td>Cells above placenta*</td>
      <td>7.3</td>
      <td>(±1.3)</td>
      <td>(n = 15)</td>
      <td>9.7</td>
      <td>(±1.0)</td>
      <td>(n = 11)</td>
    </tr>
    <tr>
      <td>Range (min-max)</td>
      <td>6</td>
      <td>-</td>
      <td>10</td>
      <td>8</td>
      <td>-</td>
      <td>11</td>
    </tr>
    <tr>
      <td>Total # cells</td>
      <td>105</td>
      <td>(±10.6)</td>
      <td>(n = 15)</td>
      <td>128</td>
      <td>(±18.0)</td>
      <td>(n = 11)</td>
    </tr>
    <tr>
      <td>Width (µm) (W)</td>
      <td>27</td>
      <td>(±2.0)</td>
      <td></td>
      <td>27.8</td>
      <td>(±3.5)</td>
      <td></td>
    </tr>
    <tr>
      <td>Height (µm) (H)</td>
      <td>30</td>
      <td>(±2.8)</td>
      <td></td>
      <td>39</td>
      <td>(±5.9)</td>
      <td></td>
    </tr>
    <tr>
      <td>H:W ratio</td>
      <td>1.1</td>
      <td>(±0.10)</td>
      <td>(n = 6)</td>
      <td>1.4</td>
      <td>(±0.22)</td>
      <td>(n = 8)</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="3">2-I</td>
      <td colspan="3">2-II</td>
    </tr>
    <tr>
      <td>Cells above placenta*</td>
      <td>10</td>
      <td>(±1.1)</td>
      <td>(n = 10)</td>
      <td>12.6</td>
      <td>(±1.0)</td>
      <td>(n = 7)</td>
    </tr>
    <tr>
      <td>Range (min-max)</td>
      <td>9</td>
      <td>-</td>
      <td>12</td>
      <td>11</td>
      <td>-</td>
      <td>14</td>
    </tr>
    <tr>
      <td>Total # cells</td>
      <td>151</td>
      <td>(±18.9)</td>
      <td>(n = 10)</td>
      <td>165</td>
      <td>(±19.8)</td>
      <td>(n = 7)</td>
    </tr>
  </tbody>
</table>

To evaluate the distinct contribution of domain-, layer-, and cell-specific growth dynamics, we labeled cells depending on their location in different regions of the ovule primordium: apical vs basal domains, L1,L2,L3 layers. In addition, we associated each cell with a cell type: ‘L1 apical’, ‘L1 basal’, ‘L2,L3 apical’, ‘L2,L3 basal’, ‘SMC’, ‘L1 dome’ (for the upmost apical L1 cells in contact with the SMC), ‘CC’ (for companion cells, elongated L2 cells adjacent to the SMC) (Figure 1B, Materials and methods).

To generate a quantitative description of ovule primordia with respect to cell number, size, and shape according to cell labels, layers, domains, ovule stage, and genotype, we developed an interactive, R-based interface named OvuleViz. The interface imports cell descriptors exported from segmented image files and enables multiple plots from a user-based selection of (sub)datasets (Figure 1—figure supplement 1A–C, Materials and methods). This work generated a reference collection of annotated, 3D images capturing ovule primordium development at cellular resolution from emergence until the onset of meiosis. The collection of 92 segmented images, comprising a total of 7763 annotated cells and five morphological cell descriptors (volume, area, sphericity, prolate and oblate ellipticity), provides a unique resource for morphodynamic analyses of ovule primordium growth.

To identify correlations between growth patterns and differentiation, we first performed a principal component analysis (PCA) based on the aforementioned cell descriptors, per cell type and stage, considered together or separately (Figure 1—figure supplement 1D–E). In this global analysis, the SMC appears morphologically distinct at late stages (2-I and 2-II) but not at early stages. This prompted us to investigate in detail the contribution of different layers, domains, and cell types to ovule primordium growth and in relation to SMC differentiation.

### Ovule primordium morphogenesis involves domain-specific cell proliferation and anisotropic cell shape patterns

The ovule primordium emerges from the placenta as a small dome-shaped protrusion and grows into a digit-shaped primordium with nearly cylindrical symmetry (stage 1-I) before enlarging at the base (Figure 1B). Using our segmented images, we first quantified global changes in cell number, cell volume, and ovule primordium shape. Our analysis revealed two distinct phases of morphological events. Phase I (stages 0-I to 0-III) is characterized by a 4.5-fold increase in total cell number together with a moderate increase in mean cell volume (10%, p=0.03). By contrast, Phase II (stages 1-I to 2-II) is characterized by a moderate increase in cell number (50%) and the global mean cell volume is relatively constant (Figure 2A, Figure 2—figure supplement 1A). To quantify the resulting changes in organ shape, we extrapolated a continuous surface mesh of the ovule outline and used it to compute its height and width at the base (Figure 2B–C, Figure 2—figure supplement 1B, Appendix 1). Anisotropic organ growth during Phase I was confirmed by a steady increase in height, while primordium width increased moderately (Figure 2C). This contrast in events between Phase I and II is illustrated by the fold-changes (FCs) in cell number and aspect ratio (Figure 2D), which range between 1.5 and 2.0 in Phase I but drop to 1.4 and 1.2 in Phase II. These observations confirmed that Phase I shows distinct growth dynamics compared to Phase II.

![Figure 2.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig2-v2.jpg)

**Figure 2.:** (A) Mean cell number per ovule increases mainly during stages 0-I to 0-III (Phase I), whereas cell volume per ovule remains constant on average across primordium development (stages 0-I to 2-II). (B) Representative image of a continuous surface of an ovule primordium mesh and its projected median plane. Dashed lines indicate the minimal and maximal curvature points used to measure organ height and width. Color scale: minimal curvature mm-1 (see also Figure 2—figure supplement 1B). (C) Anisotropic organ growth during Phase I and until stage 1-II. Mean width and height were quantified per stage. (D) Phase I shows distinct growth dynamics compared to Phase II. Fold-change of cell number and aspect ratio between stages are plotted. (E) Mean cell number is increased at the L1 vs. L2,L3 layers across developmental stages. (F) Mean cell number is increased in the basal vs. apical domain across developmental stages. (G) Representative images of ovule primordia expressing the M-phase reporter promCYCB1.1::CYCB1.1db-GFP (CYCB1.1db-GFP). White arrows indicate dividing cells. Magenta signal: Renaissance SR2200 cell-wall label. Scale bar: 10 µm. (H) Domain-specific map of mitotic activity during ovule primordium development, scored using the CYCB1.1db-GFP reporter. The frequency of mitoses was calculated per ovule domain at each developmental stage and color-coded as indicated in the bar (right). n: total number of scored ovules. (I) Mean SMC candidate volume (dark blue) is significantly increased as compared to L2,L3 cells (pale blue) from stage 0-III onward, on even at earlier stages as compared to all other cells (inset). (J) Mean cell volume is increased in L2,L3 cells as compared to L1 cells, at the two early developmental stages (0-I, 0-II). (K) The SMC consistently displays anisotropic shape with main axis of elongation aligned with ovule growth axis. The SMC anisotropy index (boxplot, left; stage 0-II, n = 16 ovules) was calculated from the Maximum (dark blue), Minimum (light blue), and Medium (medium blue) covariance matrix eigenvalues, computed from 3D segmented cells (see Figure 2—figure supplement 1G). Image (middle): illustration of the SMC main anisotropy axis (orange arrow) related by an angle ‘alpha’ to the main axis of the ovule primordium (white arrow), stage 0-II. Radar plot (right): ‘alpha’ angle measured on z projections for n = 16 ovule primordia at stage 0-II. See also Materials and methods. Error bars: Standard errors to the mean. Differences between cell types or primordium domains were assessed using a two-tailed Man Whitney U test in (A) and (I); a two-tailed Wilcoxon signed rank test in (J). *p≤0.05, **p≤0.01, ***p≤0.001. See also Figure 2—figure supplement 1, Figure 2—source data 1, Materials and methods.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Average cell number and cell volume in wild-type (Col) ovule primordium during development. Mann Whitney U test was used to assess the difference of each stage relative to the previous stage. Related to Figure 2A. (B) Extraction of overall ovule height and width used in Figure 2B,C. (a) Segmented stack imported in MorphoGraphX, (b) continuous surface mesh created in MorphoGraphX with the minimal curvature projected, the clipping plane is shown (dashed grid), (c) comparison between cell-mesh and continuous mesh, (d) longitudinal section of the mesh showing maximal (1) and minimal (2 and 3) curvature points. Heatmap: minimal curvature mm−1. Related to Figure 2B–C. (C) Box plots and line plot (error bar is standard error of the mean) showing the mean cell volume in each ovule domain during all developmental time points. Mann Whitney U test was used to assess the difference between stages (L1 apical). Related to Figure 2I. (D) Scatter plots comparing the cell volume of SMC (yellow) to the average cell volume of other cells types (same color code as in Figure 1) per ovule primordium, per stage. Related to Figure 2I. The color code follows that of the cell label in panel C. (E) Comparison of cell volume between L1 and L2L3 cells in Phase I ovule primordia (stages 0-I to 0-III). Wilcoxon Signed Rank test was used to assess the difference between domains. Related to Figure 2J. (F) Quantification of cell sphericity and ellipticity (prolate and oblate, see Materials and methods) at all ovule primordium domains during development. (G) Computation of covariance matrix eigenvalues for cell anisotropy analysis: Left: semi-automated cell type classification showing labeled cells along a longitudinal cut of an ovule. L2 SMC neighbors (orange) stands for all L2 cells sharing a portion of their wall with the SMC (yellow). Unlabeled cells (red) are not considered in the analysis. For the inner cells, the main anisotropy axis (the eigenvector of the covariance matrix corresponding to the biggest eigenvalue) is shown with a white line. Right: representation of eigenvectors of the covariance matrix (white lines) used for the PCA analysis on cell anisotropy on a random cell. The eigenvectors are scaled by their own eigenvalue normalized over the sum of the three eigenvalues. The longest eigenvector is aligned with the longest cell axis, the shortest with the shortest cell axis and the mid eigenvector with the cell axis orthogonal to the other two (and of intermediate length). Related to Figure 2K. See also movie in Figure 2—video 1 and Appendix 1. (H) SMC anisotropy index calculated from Maximal (dark blue), Mid (mid blue) and Minimal (pale blue) eigenvalues, normalized by the sum of all, from stage 0-I to stage 2-I. Related to Figure 2K. p values: *p≤0.05, **p≤0.01, ***p≤0.001. See also Figure 2—source data 1.

Next, to capture possible specific patterns of growth, we analyzed cell number, cell size, and cell shape using different viewpoints: one comparing the L1 and L2-L3 layers and one contrasting the apical vs. basal domains. Counting cell number per viewpoint clearly showed a dominant contribution of the epidermis (L1) relative to the subepidermal layers and of the basal relative to the apical domain (Figure 2E and F). To verify these findings with a cellular marker, we analyzed the M-phase-specific promCYCB1.1::CYCB1.1-db-GFP reporter (abbreviated CYCB1.1db-GFP) (Ubeda-Tomás et al., 2009). We scored the number of GFP-expressing cells among 481 ovules and plotted relative mitotic frequencies per cell layer and domain for each ovule stage to generate a cell-based mitotic activity map (Figure 2G–H, Figure 2—source data 1, Materials and methods). In this approach, subepidermal (L2) cells beneath the dome were distinguished from underlying L3 cells to gain resolution in the L2 apical domain where the SMC differentiates. Consistent with our previous observation, in Phase I, a high proliferation activity was scored in L1 cells at the primordium apex (scoring 64% of all mitotic events). By contrast, the L2 apical domain remains relatively quiescent (only 3% of the mitotic events). During Phase II, the majority (60%) of mitotic events is found in the basal domain, consistent with the progressive population of the basal domain with more cells. It is of note that during this phase, few mitotic events are detected in L2 apical cells, with the exception of SMC neighbor cells that show frequent divisions at stage 1-II. Thus, reporter analysis confirmed a biphasic, temporal pattern of cell division with changing regional contributions, suggesting the L1 dome and the basal domain as consecutive sites of proliferation, contributing to the morphological changes in Phase I and II, respectively.

Average cell size analysis, by contrast, did not reveal significant changes during primordium development with the notable exception of the SMC (Figure 2A, Figure 2—figure supplement 1C). The distinct size of the SMC candidate is already detected at stage 0-III when compared to other L2,L3 cells (Figure 2I), or even earlier (stage 0-I) when compared to all other cells (Figure 2I inset). Size differentiation of the SMC is not uniform among ovules, demonstrating plasticity in the process (Figure 2—figure supplement 1D). In addition, cells from the L2 and L3 layers are larger than L1 cells already at stage 0-I (Figure 2J, Figure 2—figure supplement 1E), possibly due to a longer growth phase, consistent with the low division frequency observed previously.

We then investigated cell shape changes during primordium elongation, using ellipticity and sphericity indices computed following segmentation. The analysis did not reveal significant differences between domains or layers (Figure 2—figure supplement 1F). This could indicate either a highly variable cell shape or local, cell-specific differences. We thus more specifically analyzed the subepidermal domain where the SMC differentiates. Companion cells showed an increasing ellipticity (and decreasing sphericity), starting at stage 1-I and culminating at stage 2-I (Figure 2—figure supplement 1F). By contrast, the SMC only showed a moderate decrease in sphericity at late stages and no distinctive ellipticity at early stages (Figure 2—figure supplement 1F) when compared to other cells. To get more information on SMC shape, we compared the maximum, medium, and minimum anisotropy index. For this, we developed an extension for MorphoMechanX (Barbier de Reuille et al., 2015) (http://www.morphomechanx.org), (i) to perform a semi-automatic labeling of cell layers and cell types from a cellularized mesh obtained from segmentation data, and (ii) to compute in each 3D cell the principal axes of shape anisotropy and the corresponding indices (Figure 2—figure supplement 1G, Appendix 1, Figure 2—video 1). The averaged maximum anisotropy shape index of the SMCs was consistently above the medium (and hence above the minimum) anisotropy index (Figure 2K, Figure 2—figure supplement 1H). We measured the degree of alignment of the SMC major axis with the main growth axis of the ovule during early stages (stage 0-II) and found a mean angle of 22° (±11°, n = 16) (Figure 2K). This confirmed that the SMC has a consistent anisotropic shape from early stages onwards, with a distinguishable major axis aligned with the primordium axis.

Taken together, these results suggest that anisotropic primordium growth is linked to a biphasic, domain-specific cell proliferation pattern, alternating between the L1 dome at Phase I and the basal domain at Phase II, combined with localized, anisotropic expansion in the L2 apical domain. In this process, SMC characteristics, such as distinct size, anisotropic shape, and orientation aligned with the growth axis of the primordium, emerge already in Phase I. The pronounced growth and elongation of the SMC in Phase II then occurs concomitant with primordium elongation. While primordium elongation is not explained by anisotropic cell growth alone but also depends on cell proliferation as shown above, the observation that cells are elliptic suggests a potential role for anisotropic cell growth. We explore this property in the next section through an in silico approach.

### 2D mechanical simulations relate ovule primordium growth to SMC shape emergence

Organ shape is determined by the rate and direction of cell growth, which is affected by signaling and the mechanical state and geometry of the tissue. This provides room for multiple regulatory feedback mechanisms and interactions between them (Bassel et al., 2014; Echevin et al., 2019). Mechanical constraints arise from the growth process in form of tensile and compressive forces that, in turn, influence cell and tissue growth (Echevin et al., 2019). To determine the role of ovule primordium growth on SMC differentiation, we sought to understand the contributions of local growth rate and anisotropy, and their relation to signaling and mechanical constraints (Coen et al., 2004; Kennaway et al., 2011).

For this, we developed two complementary 2D models of a longitudinal section of the ovule intersecting its main elongation axis: (i) a finite element method FEM-based mechanical model of the ovule represented as a continuous object (only outlining L1 vs. inner L2,L3 tissue) and (ii) a mass spring MS-based model of the ovule able to represent the mechanical status of each cell wall.

While MS-based models allow the investigation of the connection between organ and individual cell growth, the FEM-based models allow testing the role of material anisotropy. In addition, the two methods represent the cell wall in complementary ways. In FEM models, the cell wall is a continuous material throughout the tissue representation, while in MS models, the cell wall is modeled as a network of connected elasto-plastic wires. The two approaches together allow us to determine the most plausible morphogenetic principles of ovule primordium growth, while addressing the contribution of specific parameters, such as material and cell-based properties in FEM and MS models, respectively.

Growth was implemented in both frameworks using two uncoupled but complementary modalities: (i) growth in which an abstract growth factor captures the cumulative effects of biochemical signals without considering their explicit mode of action (i.e. cell wall loosening, increasing turgor pressure), hereafter referred to as ‘signal-based growth’ (Boudon et al., 2015; Coen et al., 2004); and (ii) passive growth through relaxation of excess of strain inside the tissue, hereafter referred as ‘strain-based growth’ (Boudon et al., 2015; Bozorg et al., 2016).

The mechanical equilibrium is computed to ensure compatibility within the tissue that is locally growing at different rates and orientations. As a consequence, residual internal compressions and tensions arise and this, in turn, affects the mechanical behavior (Boudon et al., 2015; Rodriguez et al., 1994). A polarization field is used to set the direction of anisotropic growth (Coen et al., 2004). The simulation consists of cyclic iterations where the mechanical equilibrium is computed before each growth step is specified by signal-based growth or strain-based growth (Appendix 1). This strategy extends previous tissue growth models (Bassel et al., 2014; Boudon et al., 2015; Bozorg et al., 2016; Kuchen et al., 2012; Mosca et al., 2018). In the case of MS models, a cell will keep growing until it reaches a pre-assigned, user-defined target area, after which it will divide (shortest wall through the centroid rule, see Appendix 1, Figure 3—figure supplement 1D).

We designed a starting template consisting of an L1 layer distinct from the underlying L2,L3 tissue based on different growth and material properties (Table 2, Figure 3—figure supplement 1, Appendix 1). We first set the model components to produce a realistic, elongated, digit-shaped primordium with a narrow dome and an L1 layer of stable thickness during development, fitting experimental observations (Figure 2—figure supplement 1C) (Reference Model, FEM-Model 1, MS-Model 2) (Figure 3A, C and E, Figure 3—figure supplement 1A–D). This model combines the following hypotheses: an initial, narrow domain of anisotropic, signal-based growth with a high concentration in inner layers, a broad domain competent for passive strain-based relaxation, and material anisotropy (for FEM models only). In addition, in the MS-based model, growth was prescribed to occur exclusively along the periclinal direction in the L1, according to our observations.

![Figure 3.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig3-v2.jpg)

**Figure 3.:** (A–B) Schematic representation of the main parameters as described in Table 2 used for the reference model and variation models shown in C and Figure 3—figure supplement 1. The L1 and underlying L2,L3 layers are represented, arrows of different size indicate anisotropy, the bulged dotted lines represent the ability of the tissue to (passively) grow under strain, the gray fields represent the initial domain of the growth signal (pale gray) and the domain of fixed, high concentration (dark gray square), *, for FEM-simulations only. Deviations of these parameters are shown in red. (C–D) Tissue-based FEM simulations of ovule primordium growth. (C) Growth stability is reached at T = 24 in the reference FEM Model 1. (D) Simulations omitting the anisotropic growth parameter (FEM-Model 3) show abnormal ovule dome shape at the same simulation time. The magnitude of accumulated strain is indicated by the background color (according to the heatmap), while the principal strain directions are shown as fine lines (white: positive strain, corresponding to stretch, red: negative strain, corresponding to compression). (E–H) Cell-based MS simulations of ovule primordium growth showing growth signal distribution and anisotropy index at the indicated simulation times (T). (E) Reference Model (MS-Model 2) showing a realistic primordium shape with straight flanks, sharp curvature at the apex, and a narrow base at T = 190. (G) The reference model shows the emergence of a large, anisotropic cell with trapezoidal shape in the L2 at T = 58, confirmed at T = 132. (F) Simulation with isotropic cell growth in inner L2,L3 layers (MS-Model 3) produces a primordium with enlarged apex and basis and flatter dome at the same simulation time as in the Reference Model. (H) L2 cells in MS-Model 3 show reduced anisotropy as compared to the Reference Model. See also Figure 3—figure supplement 1, Table 2, Appendix 1 for modeling hypotheses and methods.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Time series of the FEM reference simulation: FEM-Model 1 and its preparation. Left: reference simulation progression; the lines represent the in-plane principal strains: white for extensive, red for compressive. The heatmap represents the trace of the Green-Lagrange strain tensor. Tables (middle): preparation of the reference template (a–c) and initial parameters (d). (a–c) the starting template is a flat tissue representation distinguishing L1 and inner layers on which anisotropic material (a, Young’s modulus E2), material stiffness (b, Young’s modulus E1E3), and the growth signal (c, Kpar) domain are set. The white lines in the images left indicate the direction of fiber reinforcement for the anisotropic material (a), the intensity of the stiffness in the isotropic component of the material (b), the direction of signal-based growth, which is orthogonal to the fiber reinforcement direction (c). In addition, all lateral boundaries of the simulation template (except the top one) were fixed in all degrees of freedom. The table (d) integrates the visual information with global parameters. See additional explanations in the Materials and Methods. Schematic representation (right) of the main parameters modulated in the models shown in B and compared to the reference model for the L1 and underlying (L2,L3) layers. Arrows of different size indicate anisotropy, the bulged dotted line represent the ability of the tissue to (passively) grow under strain, the gray fields represent the initial domain distribution of the growth signal (pale gray) and the domain of fixed, high concentration (dark gray square). Deviations of these parameters are shown in red in the panel B. (B) Variation of the signal-based growth distribution with respect to the FEM- and MS-based reference models. For all model variations, the result is shown for the continuous FEM-based simulations (top) and the MS-based simulations (middle) at the simulation time point indicated (T), a schematic representation of the altered parameter is shown in red following the scheme template in A (bottom). color scale: same as in panels A and D for FEM- and MS-models, respectively. (a) Model 4: the signal is allowed to diffuse broadly. In both FEM- and MS-based simulations, the primordium is broader and the flanks are not orthogonal to the surface (arrow) as in the reference models. (b) Models 5: L1-driven growth hypothesis (1). Here, the growth-specifying signal is set at a high and fixed (i.e. non-diffusing) concentration only in the L1. In both simulations, these conditions allow the formation of a protrusion but not a realistic primordium. For both simulations, the growth time went beyond the reference time to reach the same final height as in the reference models and to compensate for the prescribed reduced growth intensity. Specific observations are made for the different simulations: FEM-Model 5 shows high compression forces below the L1 (arrow: compressive areas are marked by the blue color and red lines). One interpretation is that these compressions may arise because the L1 ‘collapses’ toward the center in the absence of inner tissue growth. Note the narrower apical, subepidermal domain than in the reference model. Furthermore, in the periclinal direction the L1 experiences significant compressions (indicated by the red lines). MS-Model 5: the growth is not balanced and generated an unstable apex (arrow, winding in different directions during growth, see Figure 3—video 1). (c) Models 6: L1-driven growth hypothesis (2). Here, the growth signal is restricted solely to the L1. In this case, the difference is striking for both FEM- and MS-based simulations: the models are not able to create a significant buckle and, even if strain-based growth is permitted, the inner tissue is not pulled upwards. The growing part of the L1 ends being compressed by the non-growing counterpart (as shown by the compressive strain marked in blue in the image for the FEM-based simulation), causing the simulation to numerically fail earlier than the reference (FEM) or in any case not forming a primordium (MS). (d) Models 7: exclusive inner-tissue growth hypothesis. Here, the growth signal is absent in the L1. The L1 performs exclusively passive strain-based relaxation. In this model, we test whether it is plausible that growth can be entirely initiated by the inner tissues, provided the L1 has a higher ability to relax (compared to the remaining tissue) due to induced strain. In such a scenario, the inner layer, which is prescribed to grow as in the reference model, pushes the L1, causing accumulation of tensile strains in the periclinal direction that get released due to passive strain-based relaxation. Both FEM- and MS-based simulations are able to produce a digit-shaped protrusion, even if, in the FEM-based simulation, it is shorter with less straight flanks (i.e. smoother transition from the placenta to the flanks; dotted arrow). This can be explained by the absence of compressive strains at the base of the ovule (plain arrow) in comparison with the reference model. The MS-based model displays a primordium with increased width at the apex. A possible explanation for this may be the absence of growth constraints generated by the L1. In both cases, the passive strain-based relaxation coefficient of the L1 was higher than in the reference model. Whether this is biologically relevant remains to be addressed experimentally. (C) Models varying passive strain-based relaxation and material properties. Results are shown for the continuous FEM-based simulations (top) and the MS-based simulations (bottom) at the simulation time point indicated (T). (a) Models 8: absence of passive strain-based relaxation in all the tissue. In both simulations, this results in a poorly developed primordium (and numerically the simulation fail earlier than the reference time), likely due to the accumulation of high strains (and stresses), particularly visible in the FEM-based model (high accumulation of compressive and tensile strains near each other in the inner tissue as well as in the L1, arrows). (b) Model 8a: variation of the previous model with absence of passive strain-based relaxation only in the L1. In both simulations, the primordium is shorter than in the reference case, although less severe in the FEM-based simulation. Specifically, in the L1 there is a high accumulation of tensile stresses on the outer walls in the apical portion and in the inner walls at the base (arrows). (c) FEM-Model 2: absence of anisotropic material properties in all tissues. Although the simulation produced a well-shaped primordium, the L1 is slightly thicker (double sided arrow, 1.2-fold compared to reference Model 1) and there is a larger L2,L3 apical domain characterized by a principal strain oriented 90° to that in the reference model (insets). These morphological differences with the reference model can be explained by the fact that passive strain-based relaxation in an isotropic material has an equal effect in the periclinal and the anticlinal direction, producing a thicker L1 and a rounder dome. In (d) FEM-based Model 2b: variation of previous Model 2. Here, only the L1 has anisotropic material properties. This restores the L1 thickness control but the abnormally high intensity and modified direction of compressive strains are similar to that in Model 2. (D) Mass spring reference model and initial template preparation, comparison with data from real ovules. Top left: MS-Model 2 simulation at four different time points. The heatmap indicates the intensity of the growth-specifying signal. Bottom left: reference simulation performed on a template obtained from a real ovule placenta (see also Materials and Methods). Top right: Initial parameters at simulation start. Field values as indicated (a–g) used to set up the reference configuration shown on the placenta at simulation time 0 and MS global parameters (h). More details can be found in the Materials and Methods. Bottom right: comparison between simulation and real primordia. Image: 3D, segmented ovule primordia stage 0-II from the wild-type reference set (see main text), longitudinal view: the SMC (orange) is outlined in a white triangular mesh (color-code refers to cell volume). Its morphology is to be compared to SMC candidates produced in the reference Model MS-Model 2 (e.g. T = 134 for grid-based simulation and T = 108 for real-image template-based simulation): the cell is elongated, centrally located in the apical dome and presents a broader upper periclinal wall surface compared to the bottom one. Plot: comparison of height-width ratio along simulation progression in MS-Model 2 and developmental progression in real (from segmented images of the wild-type reference set, see main text). For the simulation, two equi-distanced time-points between the first (T = 0) and the last simulation time step (T = 190) have been used to compute the values for intermediate phases. (E) Variation of MS-Model 3 - Higher target area in central, L2 apical cell (MS-Model 3a). This model is based on the same hypotheses as in MS-Model 3. The only difference being that the central L2 cell, which in the other models has a target area of 100 um2 , has now a bigger target area prior to division (200 um2). The aim was to test whether longer cell growth influences anisotropy. The heatmap code represents the anisotropy index as defined in Appendix 1 and is scaled up to 1.2, hence with a narrower range than in Figure 3, to allow to appreciate the mild anisotropy level in the candidate SMC (index 1.18, a fully isotropic cell has index equal to 1, the fact that surrounding cells reach the maximum anisotropy index on this limited scale is not informative here). Furthermore, one can qualitatively appreciate that the cell shape is rather trapezoidal. This shows that if the SMC candidate grows longer than neighbouring cells, tissue geometrical constraints can confer cell anisotropy and a trapezoidal shape even in the context of isotropic specified growth, to reach a certain amount of anisotropy. (F) Model lacking cell growth anisotropy specifically in the L1 layer (MS-Model 3b). Strong alterations of ovule dome growth and shape were observed when isotropic cell growth was assigned exclusively to the L1 layer (complementary to growth anisotropy hypothesis in MS-Model 3). The ovule overall shape alterations are likely due to the fact that the same amount of signal-based growth has to be redistributed in the anticlinal and periclinal direction, limiting, though, the amount by which cells are prescribed to elongate. This, in turn, has a constraining effect on the inner layers. By comparing MS-Model 7 (B), where the L1 performs exclusively strain-based growth and MS-Model 3b, where selectively the L1 grows isotropically, it is possible to infer that the anticlinal component of growth in the L1 actively constraints the inner layer expansion. This constriction, in turn, causes a lack of tension build up at the interface between the L1 and L2 which limits then further periclinal strain-based growth in the L1, producing an ovule with a shorter dome and narrower apical domain. (G) Model intervening on SMC division. In the reference MS-Model 2, there is no explicit rule preventing division of the SMC candidate. To analyze the consequence of SMC growth on primordium growth in our models, we prevented the SMC candidate to divide at simulation time T = 110. Under the reference conditions where the turgor pressure is the same among all subepidermal cells, this generates a gigantic cell exerting a considerable tensile stretch on the surrounding cells, deforming the whole domain. This suggests that, in real ovules, SMC growth might be compensated by a reduction in turgor pressure, a hypothesis that needs to be tested. Note that the two direct adjacent cells have an elongated shape reminiscent of companion cells.

**Table 2.**
 Hypotheses used to generate the mass-spring (MS)- and continuous Finite Element Method (FEM)-based simulations.Several growth and mechanical hypotheses were listed at start of modeling. To evaluate their effect on primordium growth, each hypothesis was excluded (-) in at least one scenario. The FEM- and MS-based models presented in Figure 3 and Figure 3—figure supplement 1 are numbered according to scenarios 1–8 in the table. Since it is not possible for MS models to simulate material anisotropy, Model 1 was only tested with FEM models. The hypothesis of growth anisotropy is always active for the L1 layer in the models as reported in the table. Empty dots for ‘material anisotropy’ were considered only for the FEM models. See also Figure 3—figure supplement 1 and Appendix 1 for modeling principles, results, and detailed computational methods.


<table>
  <thead>
    <tr>
      <th rowspan="2" colspan="2">Modeling hypotheses</th>
      <th colspan="8">Models</th>
    </tr>
    <tr>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">Growth anisotropy</td>
      <td>●</td>
      <td>●</td>
      <td>-</td>
      <td>●</td>
      <td>●</td>
      <td>●</td>
      <td>●</td>
      <td>●</td>
    </tr>
    <tr>
      <td colspan="2">Material anisotropy</td>
      <td>●</td>
      <td>-</td>
      <td>○</td>
      <td>○</td>
      <td>○</td>
      <td>○</td>
      <td>○</td>
      <td>○</td>
    </tr>
    <tr>
      <td colspan="2">Strain-based growth</td>
      <td>●</td>
      <td>●</td>
      <td>●</td>
      <td>●</td>
      <td>●</td>
      <td>●</td>
      <td>●</td>
      <td>-</td>
    </tr>
    <tr>
      <td colspan="2">Signal-based growth</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="4">Distribution</td>
      <td>L1 only</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>●</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Inner L2,L3 tissue only (pit-shape)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>●</td>
      <td>-</td>
    </tr>
    <tr>
      <td>L1 + inner L2,L3 tissue (pit-shape)</td>
      <td>●</td>
      <td>●</td>
      <td>●</td>
      <td>-</td>
      <td>●</td>
      <td>-</td>
      <td>-</td>
      <td>●</td>
    </tr>
    <tr>
      <td>L1 + inner L2,L3 tissue (broad distribution)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>●</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td rowspan="3">Fixed high concentration</td>
      <td>L1 only</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>●</td>
      <td>●</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Inner L2,L3 tissue only</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>●</td>
      <td>-</td>
    </tr>
    <tr>
      <td>L1 + inner L2,L3 tissue</td>
      <td>●</td>
      <td>●</td>
      <td>●</td>
      <td>●</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>●</td>
    </tr>
  </tbody>
</table>

Then, using the versatility of the modeling framework to vary initial conditions, we tested the influence of the spatial distribution of the specified growth signal on primordium growth. As first variation, we let the growth signal diffuse broadly in the domain while maintaining the selected initial cells at a prescribed high intensity of the growth signal (FEM-Model 4, MS-Model 4). The emerging primordium is appreciably broader than the Reference Model (Figure 3—figure supplement 1B). We then explored the contribution of the growth signal in the L1 compared to the inner L2,L3 tissue to primordium growth. In FEM-Model 5 and MS-Model 5, the prescribed high growth signal is present only in the L1 but is free to diffuse to the L2,L3 layers. This produced a sharp primordium, narrower and taller than the primordium in the Reference Model, and a thicker L1 layer in the FEM model (Figure 3—figure supplement 1B, Figure 3—video 1). The L2 apical domain is narrower as compared to the Reference Models. When the growth signal is absent in the inner L2,L3 tissue (FEM-Model 6, MS-Model 6), signal growth in the L1 alone is not sufficient to enable primordium growth (Figure 3—figure supplement 1B).

To answer the complementary question whether a growth signal is required in the L1 for primordium growth when it is present in the L2,L3 layers, it was removed in FEM-Model 7 and MS-Model 7 (Table 2; Figure 3—figure supplement 1B). This scenario indeed enables growth of a digit-shaped structure (as long as strain-based growth is permitted), yet the dome appears shallower than in the Reference Model in FEM simulations while it is comparable in MS simulations.

To conclude, both models where a high level of growth signal is selectively present in L1 or in inner L2,L3 layers can produce a digit-shaped primordium. Yet, absence of a growth signal in the inner L2,L3 layers results in drastic shape alterations. This favors a scenario where inner L2,L3 layer-driven growth plays a fundamental role.

Next, through modulation of passive strain-based growth, we determined that a broad tissue domain uniformly competent for strain accommodation is necessary to resolve the high accumulation of stress, which limits primordium elongation (FEM-Model 8, MS-Model 8, Figure 3—figure supplement 1C). We also explored the contribution of material anisotropy for FEM-based simulations (FEM-Model 2 and FEM-Model 2a, Figure 3—figure supplement 1C): even in the case of isotropic material, it is possible to grow a digit-shaped protrusion, yet with a wider dome and increased L1 thickness, contrasting experimental observations. To restore L1 thickness, it is sufficient to prescribe material anisotropy exclusively in the L1 (FEM-Model 2a).

Finally, we asked whether growth anisotropy must be specified in the model or if organ geometry and mechanical constraints are sufficient to specify primordium shape. Removing the growth anisotropy component abolished the digit shape of the primordium and produced a hemi-spherical protrusion in both FEM- and MS-based models (Figure 3B–F, Figure 3—video 2).

In summary, we identified parsimonious growth principles shaping the ovule primordium and suggesting different contributions of the epidermis and inner layers: an active tissue growth, mostly inner L2,L3 layer-driven and requiring a narrow, pit-shaped domain of a growth-signal, complemented by passive tissue growth with a necessary response of the L1 to accommodate the accumulated strain. Furthermore, material anisotropy in the L1 is predicted to play a role in constraining L1 thickness as observed experimentally. The fact that two distinct modeling approaches converge on the same morphogenetic principles suggests that the proposed growth mechanisms are robust. Furthermore, when compared to the growth dynamics of real ovules from phase 0-I to phase 1-I, the cell-based MS model showed a good agreement (Figure 3—figure supplement 1D).

Next, we used cell-based MS simulations to explore the correlation between organ growth and SMC morphological differentiation. In the Reference Model (MS-Model 2), an L2 apical cell with a trapezoidal shape, elongated along the main direction of ovule growth, emerged consistently during simulation (note that these cells still divide in the models as no special rule has been assigned to them) (Figure 3D). These are similar to SMC candidates at stage 0-II in real primordia, in a 2D longitudinal, median section through the ovule (Figure 2K). The elongated-trapezoidal shape of such a cell is not a prescribed feature of the model, but rather emerges from the combination of assigned anisotropic cell growth and geometrical constraints imposed by the surrounding, growing tissues.

Next, we explored the role of cell growth anisotropy in ovule primordium shape and SMC emergence. The MS-Model 3 (Figure 3E–F) corresponds to a virtual mutant where cell growth is isotropic in inner layers (the L1 maintained anisotropic growth to preserve its thickness). This led to an ovule primordium with a wider and flatter dome, comparable to FEM-Model 3. Despite the absence of a specified growth direction in inner L2,L3 tissue, due to geometrical constraints, the primordium still grows mostly vertically. We wanted to assess whether such geometrical constraints enable the formation of an elongated, trapezoidal SMC candidate also in the case of prescribed isotropic growth. As Figure 3G–H shows, the SMC candidate does not display the stereotypical shape and is not even elongated. Yet, mild cell anisotropy can be reached if the SMC candidate is allowed to grow twice more than in the Reference Model (MS-Model 3a, Figure 3—figure supplement 1E).

Altogether, the different simulations suggest that the anisotropy and characteristic shape of the SMC could be an emerging property of ovule primordium growth connected to geometrical constraints, even in the absence of specified anisotropic growth. The complementary model, altering cell growth anisotropy specifically in the L1, further suggested that directional cell growth in the epidermis is necessary to accommodate inner L2,L3 layer-driven growth and permit primordium elongation (MS-Model 3b, Figure 3—figure supplement 1F).

In all simulations, the candidate SMC eventually divided as the models miss a causative rule to differentially regulate cell division. When we prevented the SMC candidate to divide, its enlargement overrode primordium shape control in our simulations, creating an enlarged dome (Figure 3—figure supplement 1G). This suggests that a mechanism may limit SMC growth in real ovule primordia.

Altogether, 2D mechanical simulations in both continuous tissue-based (FEM) or cell-based (MS) approaches confirmed a role for localized cell growth compatible with experimental observations. The simulations also pointed to the importance of a differential role for the epidermis (accommodation) and the inner L2,L3 tissue (major growth component) as well as anisotropic cell growth as necessary for ovule primordium shape. Furthermore, the simulations suggested that SMC formation can be an emerging property of primordium geometry.

### Katanin mutants show a distinct ovule primordium geometry

To experimentally test the prediction of the isotropic growth models, we analyzed ovule primordium growth and SMC fate establishment in katanin (kat) mutants with well-described and -understood geometric defects: in absence of the microtubule-severing protein KATANIN, the self-organization of cortical microtubules in parallel arrays is hindered, thereby decreasing the cellulose-dependent mechanical anisotropy of the cell wall, resulting in more isotropic growth (Bichet et al., 2001; Burk and Ye, 2002). Note that KAT is expressed ubiquitously and, thus, also in the ovule: the KATANIN protein could be detected in both epidermal and internal L2,L3 tissue layers using a GFP reporter (Figure 4—figure supplement 1).

Here, we specifically analyzed the shape and cellular organization of ovule primordia in kat mutants using the botero (bot1-7) (Ws background), lue1, and mad5 alleles (Col background) (Bichet et al., 2001; Bouquin et al., 2003; Brodersen et al., 2008). We generated and analyzed a new dataset of 59 annotated 3D digital kat and corresponding wild-type ovule primordia at stages 0-III, 1-I, and 1-II (Figure 4—source data 1). kat mutant primordia clearly showed an increased size and a more isotropic shape (Figure 4A), being 1.5 times bigger in volume than wild-type primordia (p=0.007, stage 0-III, Figure 4B) with a smaller aspect ratio (p<0.01 stages 1-I, 1-II, Figure 4C). Because the width-to-height ratio does not inform on the shape at the flanks, we derived an equation to estimate the ‘plumpiness’ of the primordia: primordia with rounder flanks will have a higher bounding box occupancy, that is, the volume fraction of a fitting, 3D parallelepiped (bounding box) effectively occupied by the primordium (Figure 4D, left), than straight digit-shaped ovules of the same aspect ratio. Mutant primordia are clearly distinct from wild-type primordia in their relationship between aspect ratio and bounding box occupancy at stage 1-I (Figure 4D, Figure 4—figure supplement 2A), when the primordium normally starts elongating along the major growth axis. These measurements confirmed a marked attenuation of anisotropic growth in kat ovule primordia as was observed in roots, shoot organs, or seeds (Bichet et al., 2001; Hervieux et al., 2016; Luptovčiak et al., 2017b; Ren et al., 2017; Uyttewaal et al., 2012; Wightman et al., 2013; Zhang et al., 2013). Yet, at a global level, the mean cell number, cell volume, and sphericity are not significantly different between kat and wild-type primordia (Figure 4—figure supplement 2B–C). Thus, these global approaches did not resolve the origin of primordia mis-shaping.

![Figure 4.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig4-v2.jpg)

**Figure 4.:** Comparison between wild-type (WT, Ws-4 accession) and katanin (kat, bot1-7 allele) ovule primordia. (A) 3D segmented images at stage 1-II. External organ view (top) and longitudinal sections (bottom) are shown. Scale bar 10 µm. See Figure 4—source data 1 for full datasets. (B–D) Morphological difference between WT and kat primordia measured by their volume (B), the aspect ratio (C), and aspect ratio to bounding box occupancy relationship (D). (D), Left: scheme representing the bounding box capturing the primordium’s 3D surface. See also Figure 4—figure supplement 2A. (E) Quantification of cell number, cell volume, and sphericity in comparisons of L1 vs. L2,L3 and apical vs. basal domains at stage 0-III. See also Figure 4—figure supplement 2C. (F) Mitotic activity domains are altered in kat primordia. Top: Heatmap of Log2 fold change of mitotic activity in the kat mutant (lue1 allele) vs. WT (Col-0) per domain, at two developmental stages. The frequency of mitoses was measured as in Figure 2. Full maps of mitotic activity in different mutant alleles are shown in Figure 4—figure supplement 2E. Bottom: representative images of kat primordia (lue1 allele) expressing CYCB1.1db-GFP. Dashed lines mark L2 apical cells. Magenta signal: Renaissance SR2200 cell wall label. Scale bar 10 µm. (G) Mean cell volume and sphericity are increased in kat L2 apical cells in contact with the SMC. SMC, cells in contact with the SMC, and cells not in direct contact with the SMC, are compared at stage 0-III. Color code in all plots: Dark red: WT; Salmon: kat mutant. Error bars: standard error of the mean. Differences between WT and kat mutants in (B), (C), (E), and (G) were assessed using a Mann Whitney U test; a two-tailed Fischer’s exact test was used in (F). p values: *p≤0.05, **p≤0.01, ***p≤0.001. See also Figure 4—figure supplements 1 and 2; and Figure 4—source data 2.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Localization of GFP:KTN1 (complementing ktn1-2 null mutant background), in the L1 outer wall of ovule primordium, detected by Airyscan super-resolution microscopy. KATANIN protein is detected as small foci frequently aligned with cellulose fibers. Insets are close up of the sectors outlined with white square on the image. GFP channel is displayed in green (two first ovules from the left), or in green and as heatmap (FIRE scale) of fluorescence intensity (third ovule at right). Cell wall cellulose fibers were stained with Renaissance SR2200 (grayscale signal). Scale bars: 10 µm. (B) Localization of GFP:KTN1 in median longitudinal section passing through the SMC (left) or adjacent section passing through the frontal SMC wall (SMC wall plane, right). SMC wall was located thanks to the cellulose dye Renaissance SR2200 (grayscale signal). Ovule primordia at stages 0 (top), 1 (middle) or 2 (bottom) were observed. KATANIN protein is detected more frequently in the L1 layer as indicated by relative fluorescence intensity heatmap visualization (FIRE scale). However, KATANIN signal is present also in internal layers, and notably in the SMC (white arrows) and its neighbors’ cells (yellow arrows). n: number of ovules observed (from nine independent plants). Scale bars: 10 µm.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Ovule size, aspect ratio, bounding box, and bounding box occupancy. Ovule volume was calculated as the sum of cell volumes for individual ovules (OvuleViz data). For each ovule, the volume of their fitting bounding box (represented Figure 4D) was calculated using box side lengths given in Imaris (Bitplane, AG) on ovule primordia treated as Surface objects (see Materials and methods). Bounding box occupancy was calculated as the ratio of the ovule volume relative to its bounding box volume. The aspect ratio was calculated as the height (C length of the bounding box) divided by the mean of the width and depth lengths (A and B lengths of the bounding box). Man Whitney U test was used to assess differences between genotypes. Related to Figure 4B–D. (B) Comparison of cell number, cell volume, and sphericity in wild-type (WT) (Ws-4) and katanin (kat) ovule primordia (bot1-7 allele). Man Whitney U test was used to assess the differences between genotypes. (C) Global PCA analyses of cell characteristics in kat vs. WT ovules (Ws-4). PCA was performed on a dataset containing Sphericity, Ellipticity oblate, Ellipticity prolate, Area, and Volume measurements of WT and kat cells from ovules at the indicated stages (0-III, 1-I, 1-II). Cell types are labeled according to color code indicated. 95% confidence ellipses are indicated (dashed lines). Only the first and the second Principal Components (PCs) are shown. The loading plots indicate the contributions of the variables to each component. Related to Figure 4E. (D) Comparison of mean cell number, volume and sphericity in apical vs. basal domains, and in L1 versus L2,L3 layers between WT (Ws-4) and kat (bot1-7) ovule primordia. Man Whitney U test was used to assess differences between genotypes. Related to Figure 4E. (E) Mitotic activity in distinct domains of the ovule primordium of WT (Col, Ws-4) and kat (lue1, bot1.7) mutant plants. WT Col data are presented also in Figure 2 and shown here for better comparison only. The frequency of mitoses was scored using the CYCB1.1db-GFP reporter. Dark gray regions mark Phase I developmental stages. Two-tailed Fischer’s exact test was used to assess differences between domains in the genotypes. Significant p values (*p≤0.05, **p≤0.01, ***p≤0.001) are indicated for the different domains in colored boxes below the heatmaps (first column: WT; second column: kat). Non-significant differences are not represented. See also Figure 2—source data 1 and Figure 4—source data 1. Related to Figure 4F.

To refine the analysis, we contrasted different layers as done for wild-type primordia and found local alterations that provide an explanation for the formation of broader and more isotropic primordia in kat mutants. Indeed, at stage 0-III, kat ovules display a broader epidermis domain composed of more and larger cells than wild-type ovules (p=0.03 and p<0.001, respectively) (Figure 4E). Mitosis frequency analysis indicated a shift in cell division from the apex toward the basis (2.4 times less mitoses in the L1 dome domain and 2.7 times more in the L1 basal domain, compared to the wild type) (Figure 4F, Figure 4—figure supplement 2E), consistent with the increased cell number observed in L1. Yet increased cell division is not a general characteristic of kat primordia since, overall, the apical and basal domains are not massively overpopulated. By contrast, kat cells are generally larger and slightly more spherical in all domains (Figure 4E, Figure 4—figure supplement 2C–D). When specifically looking at the L2 apical domain, where the SMC differentiates, we noticed an increased relative frequency of CYCB1.1db-GFP expression in kat SMC neighbors at stage 0-II, whereas it decreases at stage 1-II (Figure 4F, Figure 4—figure supplement 2E). This is in stark contrast with SMC neighbors in wild-type primordia displaying first a relative mitotic quiescence at stage 0-II, and then enhanced mitotic activity at stage 1-II. Yet, in the SMC, no mitotic activity increase was observed in kat as compared to wild-type primordia (Figure 4F, Figure 4—figure supplement 2E).

In conclusion, the absence of KAT-mediated cell growth anisotropy is associated with spatio-temporal shifts in cell divisions, leading to an altered primordium geometry including a flatter dome and enlarged basis. Interestingly, these changes coincided with the occurrence of additional large cells in the L2 apical domain of kat primordia (SMC direct neighbor cells, Figure 4G, Materials and methods) similar in size to the SMC. This raises the question of the identity of these ectopic, enlarged neighbor cells.

### Altered ovule primordium geometry in katanin mutants induces ectopic SMC fate

Following the observation of mis-shaped kat primordia that contained larger L2 apical cells, we asked whether this had an impact on cell identity and SMC establishment. As in the wild type, a clear SMC is identifiable in kat primordia, yet it appears slightly bigger and more spherical with some variability over stages (Figure 5A, Figure 5—figure supplement 1). Interestingly, and consistent with the increased mitotic frequency in SMC neighbors observed at earlier stages, at stage 1-II, we scored additional SMC neighbors in kat primordia. On average, these were larger (14%, p=0.006) and slightly more isotropic in shape (~11% less ellipsoid p=0.03, ~2% more spherical, p<0.01) than in the wild type (Figure 5B). At stage 1-II, 34% of the kat primordia (n = 109) showed more than one enlarged, subepidermal cell; decreasing to 14% at stage 2-II (n = 104), in stark contrast with wild-type primordia showing a majority (86% to 96%) of primordia with an unambiguous, single SMC (Figure 5C). The kat phenotype is thus reminiscent of mutants affecting SMC singleness (Pinto et al., 2019) and we hypothesized that these enlarged cells are ectopic SMC candidates.

![Figure 5.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig5-v2.jpg)

**Figure 5.:** (A) SMCs lose their typical pear shape in kat mutants. 3D images of the apical-most cells in top and side view as indicated, showing the SMC (yellow), SMC neighbors (purple), and the L1 dome (transparent red). (B) Differential properties of L2,L3 apical domain cells (SMC and SMC neighbors) in terms of cell number, mean cell volume, ellipticity, and sphericity at stage 1-II. See also Figure 5—figure supplement 1 and Figure 4—source data 2. (C) Representative images of cleared wild-type (WT) and kat ovule primordia. The % indicate the frequency of ovules showing one SMC for WT primordia, or multiple SMC candidates (dashed lines) for kat primordia. (D–E) Representative images and quantification of SMC fate markers in WT and kat primordia: eviction of the H1.1::H1.1-GFP marker (green, D) and ectopic expression of KNU::nls-YFP (yellow, E) in more than one cell per primordia, are increased in kat primordia. See also Figure 5—figure supplement 2A. (F) The meiotic marker AtDMC1::GUS is ectopically expressed in kat ovules. Mutant alleles: bot1-7 (A–B), mad5 (C–E), lue1 (F). Additional kat alleles, stages, markers, and detailed quantifications are presented Figure 5—figure supplement 2 and Figure 5—source data 1. Magenta signal in (B) and (C): Renaissance SR2200 cell wall label. Scale bars for (A): 5 µm; for (C), (D), (E), (F): 10 µm. n: number of ovules scored. Error bar: standard error of the mean. Differences between WT and kat genotypes were assessed using a Mann Whitney U test in (B), and a two-tailed Fischer’s exact test in (C), (D), (E), and (F). p values: *p≤0.05, **p≤0.01, ***p≤0.001. See also Figure 5—figure supplements 1 and 2 and Figure 5—source data 1.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Comparison of volume and sphericity of L2,L3 apical domain cells in wild-type (WT, Ws-4) and katanin (kat, bot1.7 allele). Mann Whitney U test was used to assess the differences between genotypes for the mean cell volume and sphericity visualized by boxplots. Related to Figure 5B.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Representative images and quantification of WT (Ws-4) and kat (bot1-7) ovule primordia expressing pKNU::nls-YFP (yellow signal), specifically expressed in the SMC. kat ovules show ectopic subepidermal cells with YFP signal, confirming SMC fate acquisition. Related to Figure 5E. (B) Representative images of WT (Ws-4) and kat (bot1-7) ovule primordia stained with aniline blue callose dye, and visualized with DIC and epifluorescence microscopy. Callose accumulates specifically in the SMC prior to meiosis (stage 2-IV) and in spore walls of a single tetrad (stage 3-I). In all ovules with callose-positive cells (blue signal), staining was observed in a single cell or tetrad, in both wild-type and katanin background. Representative kat ovules with ectopic enlarged cells which do not display callose are shown (white arrows). Quantification of the proportion of ovules at stages 2-IV and 3-I displaying or lacking callose accumulation, in WT (Col or Ws-4) and kat (lue1 or bot1-7), suggesting altered callose deposition in kat SMC. Related to Figure 5F. (C) Representative images (ca 10 um maximum intensity projections of image stacks) and quantification of WT (Ws-4) and kat (bot1-7) ovule primordia expressing pWOX2:CenH3-GFP (green signal), labeling centromeres from the functional megaspore stage (FG1) onward. Cells ectopically expressing the marker are detected in kat at both early (before centromeres condensation – left panel) and late (after centromeres condensation – middle panel) stages of functional megaspore formation. Ectopic spores were scored based on the presence of a cell wall (white arrows) separating the spores, by contrast to two-nuclei gametophyte stage (right image, shown as an example) where the two nuclei are separated by a vacuole (arrow head). Note that ectopic spores are aligned with the normal, most basal (chalazal) FM, suggesting that they belong to the same tetrad. They also display a similar number of centromeres (5) visible on the projections. Quantification was performed on pooled early and late FG1 stages. Related to Figure 5D–F. (D) Representative images and quantification of WT (Ws-4) and kat (bot1-7) ovule primordia expressing pAKV:H2B-GFP (yellow signal), labeling nucleus from the functional megaspore stage (FG1) to the mature female gametophyte stage (FG7). Spores ectopically expressing the marker are detected in kat at significant levels at FG1 stage (left panel and graph below), and non-significantly at stage FG2 (middle panel and graph below). From stage FG4 to stage FG7, katanin embryo sacs are often abnormal, however conspicuous expression of pAKV:H2B-GFP notably in antipodals cells (arrows, right panel) marked always a single embryo sac in kat ovules (noted as ‘none’ ectopic FG in the graph below). Related to Figure 5D–F. White signal: Renaissance SR2200 cell wall label. Scale bar: 10 µm. n: number of ovules scored. Error bar: standard error of the mean. Two-tailed Fischer’s exact test was used to assess differences between genotypes. p values: *p≤0.05, **p≤0.01, ***p≤0.001. See also Figure 5—source data 1.

To verify this hypothesis, we introgressed several markers of SMC identity in a kat mutant background. The first marker is a GFP-tagged linker histone variant (H1.1-GFP) that marks the somatic-to-reproductive fate transition by its eviction in the SMC at stage 1-I (She et al., 2013). H1.1-GFP eviction occurred in more than one cell in 29% of kat primordia (n = 43, Figure 5D). The second marker reports expression of the KNUCKLES transcription factor (KNU-YFP) in the SMC (Tucker et al., 2012). Detectable as early as stage 1-I in the wild type, it was ectopically expressed in 21% of kat primordia at stage 1-II (n = 43) (Figure 5E, Figure 5—figure supplement 2A). Third, to test whether the ectopic SMC candidates have a meiotic competence, we analyzed the AtDMC1-GUS reporter (Agashe et al., 2002; Klimyuk and Jones, 1997) and, indeed, scored ectopic expression in 57% of kat primordia (n = 56) (Figure 5F). However, using aniline blue staining of callose deposition, which in wild-type SMCs stains the cell wall immediately before meiosis and marks the cells walls of tetrads after meiosis, we never detected ectopic cells accumulating callose or ectopic tetrads in kat ovules (n = 119 and 269 ovules in bot1-7 and lue1, respectively) (Figure 5—figure supplement 2B). We also noted a significant frequency of kat ovules lacking callose in SMCs or tetrads in both kat alleles, suggesting altered cell wall composition in the SMC, consistent with previous reports on kat somatic tissues (Burk and Ye, 2002) We next analyzed the pWOX2-CenH3-GFP marker labeling centromeres starting at the functional megaspore stage (FG1 stage) (De Storme et al., 2016) and found 21% kat primordia (n = 29) with two labeled cells, as compared to 4% (n = 26) in the wild type (Figure 5—figure supplement 2C). These ectopic spores are haploid since they display five centromeres. They may correspond to ectopic surviving spores given their alignment with the basal-most functional megaspore (Figure 5—figure supplement 2C). Using an additional gametophytic reporter, pAKV:H2B-YFP (Schmidt et al., 2011), we confirmed a significant number of ectopic spores at stage FG1 (31% in kat vs. 11% in wild-type ovules) showing a residual signal (Figure 5—figure supplement 2D). However, at later stages (FG2-FG7), we did not find evidence for ectopic embryo sacs (Figure 5—figure supplement 2D). At the FG7 stage, notable alterations in ovule morphology and the number of nuclei in the embryo sac were visible in kat as previously reported (Luptovčiak et al., 2017b).

Taken together, these results show that ectopic, abnormally enlarged SMC neighbors in kat primordia show at least some characteristics of SMC identity, yet they do not complete meiosis and are likely reincorporated into the soma. After meiosis, ectopic surviving spores are observed but do not complete gametogenesis. Hence, reproductive fate establishment is altered in kat ovules but the defects do not persist beyond meiosis suggesting a regulative process.

### SMC singleness is progressively resolved during primordium growth

Based on our analysis of kat primordia, it appeared that the frequency of ectopic SMC candidates was high at early stages but decreased over time (Figure 5C). This is reminiscent of the phenotypic plasticity in SMC differentiation observed, to a lesser degree, in different Arabidopsis accessions (Rodríguez-Leal et al., 2015). To characterize this plasticity during development, we analyzed 1276 wild-type primordia from stage 0-II to 2-II and scored the number of primordia with one or two enlarged, centrally positioned, subepidermal cells (Classes A and B, respectively, Figure 6A–B). In the wild type, the majority of ovules showed a single candidate SMC (Class A) at stage 0-II but 27% of primordia (n = 289) had two SMC candidates (Class B), this frequency decreasing to 3% at stage 2-II (n = 103). This finding is consistent with ~ 5% primordia in wild-type at stage 1-II showing H1.1-GFP eviction (n = 43) and KNU-YFP expression (n = 88) in more than one cell, respectively (Figure 5D–E). Thus, instead of being immediate, SMC singleness can arise from a progressive restriction of fate among several SMC candidates during development. In wild-type primordia, SMC singleness is largely resolved at stage 1-I (Figure 6B).

![Figure 6.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig6-v2.jpg)

**Figure 6.:** (A–B) In wild-type (WT) plants, ovule primordia harbor one (class A) or occasionally two (class B) SMC candidates with the frequency of class B gradually decreasing during development, reminiscent of developmental canalization. Typical images obtained by tissue clearing with SMC candidates highlighted in yellow (A) and plots showing the percentages of classes A and B (B). The frequency of class B ovules is significantly reduced from stage 1-I, suggesting that canalization (represented by the red dashed line) occurs before that stage. The plot coloration is a visual aid only. (C) Developmental canalization is delayed in kat mutants (mad5 allele). The proportion of class B ovules is significantly reduced from stage 2-II only. Quantifications for two additional kat alleles are presented Figure 6—figure supplement 1A. The plot coloration is a visual aid only. (D) The candidate SMCs initially identified as enlarged cells consistently show an enlarged nucleus in both class A and class B primordia. Nuclear area is compared between the candidate SMCs (cSMC) and surrounding L2 and L1 cells (see Figure 6—figure supplement 1D and Materials and methods for further details). Box plots include jittered data points to visualize data variability. Red lines represent the median of cSMC nuclear area for comparison with other cell types. Equivalent quantifications for stage 0-III are presented in Figure 6—figure supplement 1E. (E–F) During Phase I (stages 0-II, 0-III), S-phase is detected in candidate SMCs at higher frequency than in neighbor cells in Class A ovules, and in both SMC candidates in Class B ovules. Representative images of ovule primordia showing the speckled S-phase pattern of the pPCNA1::PCNA1:sGFP reporter (green) (E). Magenta signal: Renaissance SR2200 cell wall label. Scale bar 10 µm. Quantification of speckled S-phase pattern in the SMC candidate and L2 neighbors (class A ovules) or in both SMC candidates (class B) (F). (G–H) During Phase II (stages 1-I to 2-II), in Class A wild-type ovule primordium, SMC exits S-phase, and neighbor cells undergo S-phase; while kat primordia show the opposite pattern. Representative images of Class A ovule primordia primarily showing the nucleoplasmic pattern of pPCNA1::PCNA1:sGFP in SMCs at stages 1-II (left panel) and 2-II (middle panel); and of the speckled S-phase pattern in neighbor cells (right panel). Quantification of speckled S-phase pattern in SMC candidates and neighbors in Phase II wild-type and kat primordia (I). Representative images and quantifications of Phase I kat primordia and of class B primodia are presented in Figure 6—figure supplement 1F–H. See also Figure 2H. (I) Model for the role of KAT in primordium growth and SMC differentiation (graphical abstract). In WT primordia, SMC differentiation follows a developmental canalization process influenced by cell growth anisotropy that shapes the primordium apex. In kat mutants, reduced anisotropy modifies the cell proliferation pattern, enlarges the apex and the L2,L3 apical domain, leading to multiple SMC candidates (delayed canalization). We propose that ovule primordium shape, controlled by anisotropic cell growth, determines SMC singleness. Images: scale bars: 10 um. Graphs: n = total number of ovules. Error bar: standard error of the mean (F, I). Differences between cell types, domains, or genotypes as indicated in the graphs were assessed using Wilcoxon signed rank test in (D), and a two-tailed Fischer’s exact test in B, C, F, and I. p values: *p≤0.05, **p≤0.01, ***p≤0.001. Quantifications for additional alleles and detailed quantifications are provided in Figure 6—figure supplement 1 and Figure 6—source data 1.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/66031/elife-66031-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Canalization of SMC fate in different katanin (kat) alleles (lue1, bot1-7) and respective wild-type (WT) backgrounds (Col, Ws-4). Percentages of classes A and B primordia based on cleared tissue preparations as shown Figure 6A. The proportion of primordia with several SMC candidates at stage 0-II gradually decreases with developmental progression while the proportion of ovules with a single SMC increases, suggesting canalization. A significant delay in canalization (dashed red line) in kat mutants was confirmed by a two-tailed Fischer’s exact test (see also Figure 2—source data 1). Related to Figure 6B–C. (B–C) Ectopic expression of SMC fate in kat primordia (mad5 allele) compared to WT (Col). Percentage of ovule primordia showing H1.1-GFP eviction (B) and KNU-nlsYFP expression (C) in more than one SMC candidate at all developmental stages. Two-tailed Fischer’s exact test was used to assess differences between genotypes. Related to Figure 6B–C and Figure 6D–E. (D–E) Nuclear area as a marker of SMC candidates. Illustration of the cells selected for nuclear area measurements in representative class A and B ovules (D). Nuclei areas were measured in two L1 cells types (L1a, apical position and L1b, closer to the placenta), in cSMC: candidate SMC; L2b: a neighboring L2 cell. Dashed circles mark the nuclei of these cells used in the measurements. Related to Figure 6D. Quantification of nuclear area as shown in (D) for class A and B in WT (Col) and kat (mad5 allele) ovule primordia at stage 0-III (E). Box plot representations include jittered points to visualize data variability. Red lines represent the median of cSMC nuclear area for comparison with the other cells. Wilcoxon signed rank test was used to assess difference between SMC and the other cell types. Related to Figure 6D. (F–H) Frequency of SMCs showing an S-phase pattern in kat and Class B primordia. (F) Representative images; green, PCNA-GFP, magenta: Renaissance SR2200 cell wall label. Scale bar 10 µm. Related to Figure 6F and H. (G) Quantification of S-phase occurrence in SMCs (salmon bars) and neighbor cells (dashed bars) of class A and class B katanin (mad5) ovule primordia in Phase I (stages 0-II and 0-III). (H) Quantification of S-phase occurrence within the L2 apical domain of class B WT (Col) and kat (mad5 allele) ovule primordia in Phase II (stages 1-I to 2-II). The plotted frequencies refer to the number of primordia showing a speckled PCNA-GFP pattern in SMC candidates. Two-tailed Fischer’s exact test was used to assess differences between genotypes. Related to Figure 6H. All graphs: n = number of ovules scored. Error bar: standard error of the mean. p values: *p≤0.05, **p≤0.01, ***p≤0.001. See also Figure 6—source data 1.

Next, we quantified Class A and B primordia in kat mutants by scoring 2587 ovules of three different mutant alleles (Figure 6C, Figure 6—figure supplement 1A). Clearly, plasticity is higher with 42% (n = 202) class B primordia at stage 0-II in kat compared to 26% (n = 289) in the wild type. In addition, the resolution process is delayed in kat mutants as up to 33% Class B primordia persist at stage 1-II (n = 113) compared to 12% in the wild type (n = 281). Consistently, the two SMC markers used previously, clearly identify ectopic SMC candidates in kat primordia at stage 1-I (Figure 6—figure supplement 1B,C), and more significantly at stage 1-II (28.5% ectopic eviction of H1.1-GFP and 21% ectopic expression of KNU-YFP, Figure 5D–E). In addition, at stage 2-II, when 17% of cleared kat primordia (n = 110) showed ectopic SMCs, H1.1-GFP eviction and KNU-YFP expression was only found in 8% (n = 25) and 7% (n = 74) of the primordia, respectively (Figure 6—figure supplement 1B,C). Therefore, molecular events associated with SMC fate are partially uncoupled from cell growth during the resolution of SMC singleness in kat.

Another outcome of this study is the early emergence of SMC candidates, based on cell size mostly and confirming our former 3D cell-based analysis that showed increased cell volume of the L2,L3 apical cells already at stages 0-I/0-II (Figure 2J). To corroborate this finding using a different criterion, we measured the nuclear area, which is a distinctive feature of SMCs (Rodríguez-Leal et al., 2015; She et al., 2013). We compared the nuclear area of SMC candidates to that of surrounding L1 and L2 cells, in both Class A and B primordia, at stages 0-II and 0-III. Wild-type Class A and B primordia showed an enlarged nucleus in the candidate SMCs from stage 0-II onwards, and this correlation was also true in kat primordia (Figure 6D, Figure 6—figure supplement 1D,E).

However, it remains difficult to resolve the precise timing of SMC establishment at these early stages due to the lack of molecular markers. Yet, we reasoned that we may be able to distinguish the SMC candidates from their neighbors by their cell cycle pattern, where cells entering meiosis may engage in a specific S-phase compared to regularly cycling mitotic cells. To this aim, we used a GFP-tagged PCNA variant marking the replication machinery, pPCNA1::PCNA1:sGFP (PCNA-GFP) (Yokoyama et al., 2016). When engaged at active replication forks, PCNA-GFP shows nuclear speckles characteristic of S-phase (Strzalka and Ziemienowicz, 2011). During G1/G2, it remains in the nucleoplasm and in M-phase it is undetectable. We specifically quantified the distribution patterns of PCNA-GFP in cells from the L2 apical domain in wild-type and kat primordia, separately for Class A and B ovules (Figure 6E–H).

In Phase I wild-type primordia, PCNA-GFP was always detectable, in both classes, indicating that L2 apical cells are rarely in M-phase, consistent with the seldom detection of mitoses using CYCB1.1db-GFP. We observed an S-phase pattern consistently in one (Class A) or more (Class B), centrally positioned L2 apical cells, presumably corresponding to SMC candidates (Figure 6E). This pattern was captured in a large proportion of primordia at stage 0-II and 0-III: ~24% (n = 112) and ~40% (n = 79) for Class A, respectively; 30% (n = 41) and 28% (n = 60) for Class B, respectively (Figure 6F). Such high frequencies could be generated either by a slow S-phase in SMC candidates only (the persistence of the marker increasing the probability to score it repeatedly in our sample size), or by a regular (short) mitotic S-phase in a high number of SMC candidates. The low detection frequency of the mitotic marker CYCB1.1db-GFP in SMC candidates is inconsistent with the latter possibility. Thus, the likeliest interpretation is that candidate SMCs enter a slow S-phase from early stages onwards, probably meiotic, although this cannot be assessed with this marker.

In kat primordia at Phase I, Class A ovules showed a wild-type pattern in the SMC at stage 0-II, but a reduction at stage 0-III, suggesting alterations in S-phase entry; and Class B ovules, by contrast, displayed high frequency of S-phase patterns, indicating either a longer S-phase or multiple dividing cells (Figure 6—figure supplement 1G).

In Phase II, SMC candidates showed no S-phase pattern in a large majority of both Class A and B primordia (97% on average, over entire Phase II) (Figure 6G–H, Figure 6—figure supplement 1G–H) in agreement with the presence of newly replicated DNA at stage 1-I (She et al., 2013). In contrast to Phase I, however, S-phase is now detected in SMC neighbors (~21% at stage 1-II) (Figure 6G–H), consistent with the divisions observed in these cells (Figure 2D). Strikingly, in Phase II, kat primordia display a higher frequency of S-phase patterns in SMC candidates (Figure 6H, Figure 6—figure supplement 1F,H), suggesting that S-phase duration or entry is delayed compared to the wild type. SMC neighbors, by contrast, show a lower frequency of S-phase patterns (Class A), consistent with reduced division in these cells (Figure 4F).

Collectively, our data indicate a cellular heterogeneity in terms of size, nuclear size, and S-phase patterns, of the L2 apical domain as compared to L1, which leads to the emergence of one or several SMC candidates as early as stage 0-II. The gradual decrease in the number of primordia with ambiguous SMC candidates demonstrates a developmentally regulated resolution of SMC fate to a single cell. This process is associated with a specific cell cycle progression, cellular elongation, and a robust expression of SMC fate markers. In kat primordia displaying alterations in geometry, SMC singleness is largely compromised: plasticity in SMC emergence is increased and fate resolution to a single SMC is delayed.

## Discussion

Organogenesis involves coordinated cell division and cell expansion, complex growth processes orchestrated by biochemical and mechanical cues (Echevin et al., 2019). How cell differentiation is coordinated in space and time during organ growth, and whether these processes are interrelated, are central aspects for the elucidation of patterning principles (Whitewoods and Coen, 2017). The female germline is initiated with SMC differentiation in the ovule primordium. The SMC emerges as a large, elongated, subepidermal cell that is centrally located at the apex of the primordium, a digit-shaped organ emerging from the placenta. To study how SMC fate relates to ovule organogenesis, we generated a reference collection of images capturing ovule primordium development at cellular resolution in 3D and determined cell division frequencies in the different domains. We observed a biphasic pattern of cell divisions alternating in the epidermis and inner layers, as well as the apical and basal domains, in Phase I (stages 0-I to 0-III) and Phase II (stages 1-I to 2-II).

However, this approach did not allow us to resolve the driving morphogenetic factors. For this reason, we developed continuous tissue-based and cell-based 2D simulations of primordium growth. The different simulations revealed key growth principles shaping the ovule primordium and uncovered differential roles for the epidermis and inner layers. Notably, an inner tissue-driven growth model, where the L1 also contributes to the expansion of the primordium, best described ovule primordium growth. This is reminiscent of a model describing leaf primordium emergence (Peaucelle et al., 2011). In addition, best-fit models produced by both cell- and tissue-based simulations predicted a growth-promoting signal in a confined domain along a vertical stripe at primordium emergence. Candidate growth signals are phytohormones, peptides, and small RNAs known to affect ovule primordium growth (Kawamoto et al., 2020; Pinto et al., 2019; Su et al., 2020). The domains of auxin response restricted in the L1 dome and of cytokinin signaling localized in a region basal to the SMC in Phase II primordia (Bencivenga et al., 2012) also suggest a confined growth signal. Whether the signaling domains are established already in Phase I and play a causative role in primordium patterning remains to be determined. The epidermis, by contrast, is predicted to play a key role in accommodating the constraints generated by inner-tissue growth. In this layer, strain-based growth and anisotropic material properties possibly resolve mechanical conflicts arising between tissue layers that grow at different rates (Hervieux et al., 2017). In line with this hypothesis, we observed frequent divisions in L1 apical cells in vivo that support the expansion of the epidermis while inner tissues develop.

Interestingly, while our models did initially not contain an a priori rule to produce the typical, elongated shape of the SMC, it emerged consistently as a trapezoid-shaped L2 cell in the cell-based reference model. This shape likely emerges from the combination of assigned anisotropic cell growth and geometrical constraints imposed by the surrounding growing tissues. Explicitly blocking SMC division during the simulation, did not only enable its expansion as expected, but also pushed surrounding cells and strongly deformed ovule morphology. Thus, ovule growth homeostasis in vivo likely requires a mechanism to accommodate the differential growth of the SMC. A gradual reduction of SMC turgor pressure is a plausible scenario that would limit SMC size and prevent overriding the constraints provided by surrounding cells, similar to what was suggested for the shoot apical meristem (Long et al., 2020). In turn, a gradient of pressure in a field of cells could provide positional information through the directional movement of water and other molecules, thereby linking organ growth homeostasis, cell growth, and cell fate (Beauzamy et al., 2014; Long et al., 2020). Such a mechanism could also participate in determining the domain of the growth signal predicted by our simulations.

Another prediction of our growth models is the key role of anisotropic cell growth in controlling the geometry of the ovule primordium. Primordia of the kat mutant, deficient in the microtubule severing enzyme KATANIN (Luptovčiak et al., 2017a), resemble virtual mutant primordia generated by models where cell growth is isotropic in the inner layers. kat primordia have a flatter dome and large basis associated with global alterations in the cell proliferation pattern, cell size, and cell shape. Interestingly, kat primordia develop ectopic SMC candidates as early as stage 0-II. The most parsimonious hypothesis is that the altered geometry in kat primordia expands the domain of cells competent to form SMCs. Yet, we cannot exclude a direct effect of the kat mutation on L2 apical cells, disconnected from organ geometry, which would induce de novo SMC fate. However, this scenario is unlikely. First, KATANIN is present throughout ovule primordium cells. Second, we would expect increased cell growth and slower mitoses (Luptovčiak et al., 2017a), resulting in a reduced division frequency of L2 apical cells, which is not the case. Instead, we measured increased cell divisions in L2 SMC neighbors at stage 0-II. Also, the delayed divisions of SMC neighbors in kat at stage 1-II cannot explain the formation of ectopic SMC candidates at stage 0-II.

Therefore, the most parsimonious explanation is that the emergence of several SMC candidates in kat primordia is an effect of ovule primordium geometry. In this scenario, isotropic cell growth and altered mechanical constraints in the tissue acting from primordia emergence onwards, lead to divisions and patterning alterations that expand the domain of cells competent for SMC fate. This working model paves the way to explore the role of epidermal geometry in controlling regulators of the cell cycle and SMC fate in L2 apical cells. This is reminiscent of the epidermis in the shoot apical meristem, affecting the dome shape and acting on stem cell regulators in underlying layers (Gruel et al., 2016; Savaldi-Goldstein et al., 2007). The predicted role of the primordium epidermis to accommodate – and perhaps feedback on – underlying growth constraints is particularly interesting considering the role of mechanical cues on gene regulation (Fal et al., 2017; Landrein et al., 2015). The epidermis of the ovule primordium is also a known source of signaling cues (Kawamoto et al., 2020; Pinto et al., 2019; Su et al., 2020). In addition, phytohormones act themselves on KATANIN-mediated oriented cell growth and cell division (Luptovčiak et al., 2017a). In this context, it is possible that mis-shaping of kat primordia arises from a disrupted feedback altering the distribution pattern of the hypothesized growth signals.

Furthermore, our analyses unveiled new characteristics of the SMC establishment process. We found that SMC candidates emerge from within a mitotically quiescent L2 apical domain, consistent with the finding that the H3.1 histone variant HTR13 is evicted, marking cell cycle exit (Hernandez-Lagana and Autran, 2020). In addition, SMC candidates have a markedly long S-phase compared to surrounding cells. These observations are reminiscent of the animal germline where mitotic quiescence is a prerequisite for meiosis (Kimble, 2011; Reik and Surani, 2015). Also, early SMC candidates already display a typically large cell and nucleus size and an elongated shape aligned with the primordium growth axis. Collectively, we found that SMC characteristics are established much earlier than previously thought, that is, soon after primordium emergence (stages 0-II/0 III). Moreover, these characteristics frequently arise in more than one SMC candidate at Phase I, typically resolving into a single SMC at the onset of Phase II. This clearly documents a developmental sequence of plasticity at SMC fate emergence and progressive resolution of SMC fate to a single cell. This is reminiscent of developmental canalization, which refers to the capacity of an organism to follow a given developmental trajectory in spite of disturbances (Hallgrimsson et al., 2019; Scharloo, 1991; Waddington, 1942). Cell fate canalization is well studied in animal systems where it is modulated by intercellular signal-based feedback mechanisms (Heitzler and Simpson, 1991), epigenetic regulation (Pujadas and Feinberg, 2012), and organ geometry (Huang et al., 2020; Huang and Russell, 1992; Pujadas and Feinberg, 2012; Royer et al., 2020). In plants, canalization is better known in the context of organogenesis during phyllotaxis and developmental robustness (Godin et al., 2020; Lempe et al., 2013). Our study expands the examples of canalization to the level of a cellular domain in the Arabidopsis ovule primordium. While L2 apical cells initially share the competence to form SMC candidates, leading to plasticity at SMC emergence, the progressive restriction of cell fate possibilities in the primordium apex ultimately leads to the specification of only one SMC committed to meiosis. Our results are in line with a formerly proposed canalization process operating during SMC establishment (Grossniklaus and Schneitz, 1998; Rodríguez-Leal et al., 2015). Despite the fact that several mutations (reviewed in Pinto et al., 2019; Mendes et al., 2020), including kat (this study), alter SMC singleness in Arabidopsis, canalization remains a robust process securing the formation of a single embryo sac despite such genetic perturbations. How this developmental mechanism buffers phenotypic inter-individual variations and whether it is evolutionary constrained remains to be determined.

In this study, we quantified plasticity among ovule primordia and progressive fate resolution during primordium growth in wild-type reference accessions. We characterized specific cellular events associated with these processes, notably differential cell growth and cell division. SMC fate emergence is characterized by mitotic quiescence and cellular growth in one or more L2 apical cells. SMC singleness resolution is associated with re-entry into a somatic cell cycle (this study), and re-incorporation of a replicative histone H3.1 (Hernandez-Lagana and Autran, 2020) in candidates neighboring the SMC. How known epigenetic and signaling factors interplay to secure SMC singleness remains to be determined. Similar to mouse and Drosophila, where tissue mechanics and organ geometry were shown to contribute to cell fate canalization (Chan et al., 2017; Huang et al., 2020; Royer et al., 2020), we propose that ovule primordium geometry contributes to channel SMC fate in the apex and the resolution into a single SMC. In this conceptual framework, kat increases plasticity and delays the resolution process toward SMC singleness (working model Figure 6I).

Altogether, our work proposes a conceptual framework linking organ geometry, cell shape, and cell fate acquisition in the ovule primordium, which is potentially of broader relevance in plant patterning. In addition, the image resource published in this study is complementary to others capturing ovule development at later stages (Lora et al., 2017; Vijayan et al., 2021). It also populates a growing number of 3D-segmented images of plant tissues and organs (Wolny et al., 2020), which collectively build the fundament of a developmental atlas integrating morphogenesis with gene expression (Hartmann et al., 2020).

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
      <td>Chemical compound, drug</td>
      <td>Renaissance SR2200</td>
      <td>Renaissance Chemicals</td>
      <td>SCRI Renaissance Stain 2200</td>
      <td>https://www.renchem.co.uk/index.php/specialty-chemicals-division/item/48-selected-fluorescent-dyes-and-brighteners-for-microscopists</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>PI stain</td>
      <td>Sigma- Aldrich</td>
      <td>Catalog # P4170</td>
      <td>Propidium Iodide</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Na-metabisulphite</td>
      <td>Sigma- Aldrich</td>
      <td>Catalog # S9000/PubChem: 329824616</td>
      <td>Sodium metabisulphite</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Aniline Blue</td>
      <td>Sigma- Aldrich</td>
      <td>Catalog # 415049</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>3D digital atlas ovule primordium</td>
      <td>This paper</td>
      <td>https://doi.org/10.5061/dryad.02v6wwq2c</td>
      <td>Data resource. 3D segmented images (.ims files) wild-type (Col-0, Ws-4) and katanin (bot1-7) as shown in Figure 1—source data 1 and Figure 4—source data 1</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>Col-0</td>
      <td>NASC</td>
      <td>NASC (RRID:SCR_004576) Stock ID: N22625</td>
      <td>Wild-type ecotype Col-0</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>Ws-4</td>
      <td>NASC</td>
      <td>NASC (RRID:SCR_004576) stock ID: N5390</td>
      <td>Wild-type ecotype Ws-4</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>bot1-7</td>
      <td>doi:10.1046/j.1365-313x.2001.00946.x</td>
      <td></td>
      <td>bot1-7 mutant. H.Höfte.</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>mad5</td>
      <td>doi:10.1126/science.1159151</td>
      <td></td>
      <td>mad5 mutant. O.Voinnet.</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>lue1</td>
      <td>NASC</td>
      <td>NASC (RRID:SCR_004576) Stock ID: N57954</td>
      <td>lue1 mutant</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>CYCB1db-GFP</td>
      <td>doi:10.1016/j.cub.2009.06.023</td>
      <td></td>
      <td>promCYCB1.1::CYCB1.1db-GFP. M.Bennett.</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>H1.1-GFP</td>
      <td>doi:10.1242/dev.095034</td>
      <td></td>
      <td>promH1.1::H1.1-GFP.</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>KNU-nlsYFP</td>
      <td>doi:10.1242/dev.075390</td>
      <td></td>
      <td>promKNU::nls-YFP. M.Tucker.</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>DMC1-GUS</td>
      <td>doi:10.1046/j.1365-313x.1997.11010001.x</td>
      <td></td>
      <td>promAtDMC1::GUS. I.Siddiqi.</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>pWOX2:CENH3-GFP</td>
      <td>doi:10.1186/s12870-015-0700-5</td>
      <td></td>
      <td>promWOX2::CenH3-GFP. N.DeStorme.</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>PCNA-GFP</td>
      <td>doi:10.1038/srep29657</td>
      <td></td>
      <td>promPCNA1::PCNA1-GFP. S. Matsunaga.</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>pAKV:H2B-GFP</td>
      <td>doi:10.1371/journal.pbio.1001155</td>
      <td></td>
      <td>promAKV::H2B-GFP. W.C. Yang.</td>
    </tr>
    <tr>
      <td>Genetic reagent (Arabidopsis thaliana)</td>
      <td>GFP:KTN1</td>
      <td>doi:10.1126/science.1245533</td>
      <td></td>
      <td>promKTN1::GFP-KTN1. D.W. Ehrhardt.</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>IMARIS</td>
      <td>http://www.bitplane.com/imaris/imaris</td>
      <td>RRID:SCR_007370</td>
      <td>3D image processing software Bitplane AG, Switzerland</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ExportImarisCells,</td>
      <td>This paper.</td>
      <td></td>
      <td>plugin for IMARIS to export segmented cells in meshes for MorphographX. https://github.com/barouxlab/ExportImarisCells (copy archived at swh:1:rev:50badce519f07cf529c3abef765b58972fff70e6); Mosca, 2021a.</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MorphoGraphX</td>
      <td>https://morphographx.org/</td>
      <td></td>
      <td>Software to perform 2D/3D segmentation and image analysis</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MorphoMechanX</td>
      <td>https://morphographx.org/morphomechanx/</td>
      <td></td>
      <td>Software to perform 2D/3D biomechanical simulations</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MassSpring Models_ovuleGrowth2D</td>
      <td>This paper.</td>
      <td>DOI:10.5281/zenodo.4681169</td>
      <td>plugin for MorphoMechanX, 2D MS-models simulation tool. https://github.com/GabriellaMosca/MassSpring_2DovuleGrowthModel (copy archived at swh:1:rev:a66b0496ba51ca7674f0020ace723aa0b850470f); Mosca, 2021b.</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FEM_2DOvule GrowthModel</td>
      <td>This paper.</td>
      <td>DOI:10.5281/zenodo.4681167</td>
      <td>plugin for MorphoMechanX, 2D FEM-models simulation tool. https://github.com/GabriellaMosca/FEM_2DOvuleGrowthModel (copy archived at swh:1:rev:6b6c09f6039ce3e9d55686d6b6e9dadf28b53e2f); Mosca, 2021c.</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>3DAutoLabeling-ShapeQuant</td>
      <td>This paper.</td>
      <td>DOI:10.5281/zenodo.4681165</td>
      <td>plugin for MorphoMechanX, automatic labeling of L1, L2, L3 layers and cell shape quantifier. https://github.com/GabriellaMosca/3DAutoLabeling-ShapeQuant (copy archived at swh:1:rev:3138c3fb10891afbc1d48d35395dc00ee58ce199); Mosca, 2021d.</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>OvuleViz</td>
      <td>This paper.</td>
      <td></td>
      <td>R-based, shiny interface for interactive plotting of Imaris data. https://github.com/barouxlab/OvuleViz (copy archived at swh:1:rev:fd614aa1e80258928ee036191f26c3dd703d3141); Pires, 2021.</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R Project for Statistical Computing/RStudio</td>
      <td>https://www.r-project.org/ http://www.rstudio.com/</td>
      <td>RRID:SCR_001905</td>
      <td>R Core Team, 2013</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>OMERO</td>
      <td>http://www.openmicroscopy.org/site/products/omero</td>
      <td>RRID:SCR_002629</td>
      <td>Besson et al., 2019</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FIJI</td>
      <td>http://fiji.sc</td>
      <td>RRID:SCR_002285</td>
      <td>Rueden et al., 2017</td>
    </tr>
  </tbody>
</table>

### Plant growth and plant material

Arabidopsis thaliana plants were grown under long-day conditions (16 hr light) at 20–23°C in a plant growth room. Columbia (Col-0) and Wassileskija (Ws-4) accessions were used as wild-type controls depending on the mutant background used in the experiment. Three katanin alleles were used: bot1-7 (Bichet et al., 2001) in Ws-4 accession, lue1 (Bouquin et al., 2003) and mad5 (Brodersen et al., 2008) both in the Columbia (Col-0) accession. Homozygous mutant individuals for all the katanin alleles were identified on the basis of their recessive vegetative phenotype. The following published markers were used: pCYCB1.1:db-GFP (Ubeda-Tomás et al., 2009), pKNU:nls:YFP (Tucker et al., 2012), pH1.1:H1.1:GFP (She et al., 2013), AtPCNA1:sGFP (Yokoyama et al., 2016), pAtDMC1:GUS (Agashe et al., 2002; Klimyuk and Jones, 1997), pWOX2:CenH3:GFP (De Storme et al., 2016), pAKV:H2B:GFP (Schmidt et al., 2011), and crossed to kat mutants, and to Ws-4 ecotype for bot1-7 allele comparisons. For KATANIN localization, the published reporter line GFP:KTN1 in a ktn1-2 background (Lindeboom et al., 2013) was used.

### 3D imaging and image processing (segmentation and labeling)

Entire carpels were stained using the pseudo-Schiff propidium iodide (PS-PI) cell wall staining procedure providing excellent optical transparency for 3D imaging in depth in whole-mount. We described previously the manipulation, staining, mounting of the flower carpels and imaging procedures (Mendocilla Sato and Baroux, 2017). Cell-boundary based image segmentation was done using ImarisCell (Bitplane) as described in details previously (Mendocilla Sato and Baroux, 2017). Each ovule was manually labeled in Imaris using customized Cell Labels for the different cell types and domains colored as shown in Figure 1. We defined the labels as follows:

Semi-automated segmentation requiring user input and manual labeling can be error prone. To reduce the error rate, the 92 images were segmented and labeled by one author, but verified and curated by two others. All Imaris files used in the study are available at the DRYAD repository: https://doi.org/10.5061/dryad.02v6wwq2c.

### Ovule stage classification

Ovule development is described according to a well-accepted nomenclature (Schneitz et al., 1995). The first stage, initially defined as stage 1-I, indistinctly grouped primordia from emergence until digit shape. To enable describing early morphogenetic processes, however, we propose to (i) restrict stage 1-I to the final digit shape stage and (ii) subdivide preceding stages as stages 0-I, 0-II, and 0-III, as shown in Figure 1B. These developmental stages are classified according to the approximate number of cell layers protruding above the placenta and overall shape of the ovule as described in Table 1 and Figure 1—source data 1.

### Quantification of cell number, size and shape and interactive plotting using OvuleViz

Several cell descriptors were retrieved using the ImarisCell’ Statistics function and exported as. csv files: cell area, cell volume, cell sphericity, cell ellipticity (oblate and prolate). We developed an interactive R-based data plotting interface, OvuleViz, reading the Imaris-derived data within the exported files ordered by genotype then stages (Figure 1—figure supplement 1). OvuleViz is freely available at https://github.com/barouxlab/OvuleViz (Pires, 2021), and is based on a shiny interface for R. OvuleViz allows plotting selectively one or several of the cell descriptors for chosen stages and genotypes, along different visualization (scatter plots, box plots, histograms). In addition, OvuleViz retrieves the cell number from the number of objects in the. csv file.

### 3D quantification of ovule volume and shape using IMARIS

Ovule volume and shape were quantified on 3D segmentations using IMARIS software, to compare katanin and wild-type genotypes. For each ovule, all segmented labeled cells were duplicated and fused as a single cell object. The ImarisCell’ Statistics function was used to retrieve ‘cell volume’ and ‘bounding box OO’ (object-oriented 3D bounding rectangle, exporting the minimum (A), mid (B) and maximum (C) lengths of the object bounding rectangle). Width to Height ratio was calculated by dividing the maximum (C) length by the mean of mid (B) + minimum (A) lengths. Bounding box occupancy was calculated as the ratio of ovule volume by the bounding box volume.

### Modeling and image analysis with MorphoMechanX

The details of tissue growth models and MorphoMechanX-based processing are described in Appendix 1.

### 2D cytological analysis of cleared ovule primordia and quantifications

For cytological examination of cleared ovule primordia, flower buds from wild-type and mutant plants were harvested and fixed in formalin-acetic acid-alcohol solution (40% formaldehyde, glacial acetic acid, 50% ethanol; in a 5:5:90 vol ratio) for at least 24 hr at room temperature. After fixation, samples were washed two times with 100% ethanol and stored in 70% ethanol. Gynoecia of 0.2–0.6 mm in length were removed from the flowers with fine needles (1 mm insulin syringes), cleared in Herr’s solution (phenol: chloral hydrate: 85% lactic acid: xylene: clove oil in 1:1:1:0,5:1 proportions), and observed by differential interference contrast microscopy using a Zeiss Axioimager Z2 microscope and 40X or 63X oil immersion lenses. Picture acquisition was done with a sCMOS camera (Hamamatsu ORCA Flash V2). Nuclei area measurements were carried out with ImageJ software, using the manual contour tool ‘Oval’.

### Fluorescence microscopy and quantifications

Epifluorescence imaging of callose using aniline blue staining was performed as described (Cao et al., 2018), and observed on a Zeiss Axioimager Z2 microscope with CFP emission filter, DIC, and a 63X oil immersion lens. Image acquisition was done with a sCMOS camera (Hamamatsu ORCA Flash V2).

Imaging of ovule primordia stained in whole-mount for cell boundary was done as described (Mendocilla Sato and Baroux, 2017) using a laser scanning confocal microscope Leica LCS SP8 equipped with a 63X glycerol immersion objective and HyD detectors.

Imaging of the GFP and YFP markers was performed using a laser scanning confocal microscope Leica LCS SP8 equipped with a 63X oil immersion objective, or a Leica SP5 equipped with a 63X glycerol immersion objective and HyD detectors. Samples were mounted in 5% glycerol with the cell wall dye Renaissance 2200 (SR2200) diluted 1/2000 or as described (Musielak et al., 2015). The following wavelengths were used for fluorescence excitation (exc) and detection of emission (em): Renaissance: exc = 405 nm, em = 415–476 nm; GFP: exc = 488 m, em = 493–550 nm; YFP: exc = 514 nm, em = 590–620 nm. For KATANIN localization, GFP:KTN1 ktn1-2 carpels were mounted in gelrite 0.2% supplemented with Renaissance (SR2200) diluted 1/1000 in water, and imaged immediately using a Zeiss LSM880 laser scanning microscope equipped with a 40X long distance water immersion objective and Airyscan detector, in the SR (super-resolution) acquisition mode. Fluorescence was collected using the following filters settings: 405 nm and 488/561/633 nm primary beam splitters for all channels, then BP420−480 + BP495-550 secondary filter for 488 nm excitation channel (GFP) and BP420−480 + LP605 for 405 nm excitation channel (Renaissance). Images were processed using the built-in Airyscan processing tool.

All images were processed using ImageJ (Rueden et al., 2017), OMERO (Besson et al., 2019), or Imaris (Bitplane, Switzerland) for contrast/intensity adjustments and maximum intensity projections where relevant.

The mitotic activity in both wild-type and katanin ovules was quantified by scoring the cells expressing promCYCB1::dbCYCB1-GFP (M phase reporter) on 3D stacks, in each ovule domain at each developmental stage. Only ovules showing at least one cell expressing promCYCB1::dbCYCB1-GFP were included in the analysis. At a given stage, the frequency of mitoses per domain is the ratio between the number of GFP-positive cells within a domain in all observed ovules, to the total number of GFP-positive cells found in all domains in that population of ovules.

To quantify ectopic expression of H1.1-GFP, KNU-nlsYFP, pWOX2:CenH3-GFP and pAKV:H2B-GFP markers, the percentage of ovules presenting expression (or eviction in the case of H1.1-GFP) of the marker in more than one cell (or in more than one embryo sac for pAKV:H2B-GFP) was scored on 3D stacks. To quantify PCNA-GFP patterns, using 3D stacks, cells of the L2 apical domain were classified according to the ‘speckled’ or ‘nucleoplasmic’ patterns, or absence of the marker.

### Histochemical detection of uidA reporter gene product (GUS staining)

Gynoecia of 0.4–0.6 mm in length were removed from the flowers with fine needles and placed in staining solution, using high stringency conditions for ferro- and ferricyanide concentrations to limit GUS product diffusion (0.1% Triton X-100, 10 mM EDTA, 5 mM ferrocyanide, 5 mM ferricyanide and 20 mg/ml 5 -bromo-4-chloro-3-indolyl-beta-d-glucuronic acid cyclohexyl-ammonium salt (X-gluc, Biosynth AG, Staad, CH) in 50 mM phosphate buffer), for 96 hr at 37°C. After staining, the samples were mounted in clearing solution (50% glycerol, 20% lactic acid diluted in water) and observed by differential interference contrast microscopy using a Zeiss Axioimager Z2 microscope. Picture acquisition was done with a color sCMOS camera (Axiocam 506 color Zeiss).

### Statistical analysis

To identify the main cellular descriptors – cell area, cell volume, sphericity, ellipticity oblate, ellipticity prolate – explaining variance of each cell types, at each ovule primordium growth stages and between genotypes, we used principal component analysis (PCA) on a cells' descriptors matrix. PCA was executed using the R software version 3.6.3. In all different subsets of data, PCA was performed by singular value composition of the centred and scaled data matrix. Data entries with missing values were removed before analysis. All Cell data as exported by Imaris were uploaded but only cells with a ‘Cell Label’ as described in the method section ‘3D imaging’ were plotted. For visualization of PCAs, only the first two principal components were represented in both score and loading plots.

To determine if the means between two datasets were significantly different we used two-tailed t-test when the data were normally distributed (n > 30). For all datasets with n < 30, we assume that normality was not possible to assess properly (as small samples most often pass normality tests), thus we used non-parametric tests. Wilcoxon Signed-Rank two-tailed test was used for paired quantifications, and Mann Whitney U two-tailed test was used for unpaired quantifications. Tests were performed in Excel or in R (wilcox.test function). To compare ovule proportions, we used two-tailed Fischer’s Exact test, using https://www.langsrud.com/fisher.html, available online. Variability was assessed using the Standard Error of the mean (SE), indicated in the graphs and/or the supplemental data when applicable. For some datasets, boxplots were used to improve visualization of data distribution. The number of samples and biological replicates for each experiment are indicated in the figure and/or figure legends and/or supplemental data.
