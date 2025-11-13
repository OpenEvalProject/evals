# Nanoscape, a data-driven 3D real-time interactive virtual cell environment

## Authors

- Shereen R Kadir<sup>1</sup> ([ORCID: 0000-0002-3960-988X](https://orcid.org/0000-0002-3960-988X))
- Andrew Lilja<sup>1</sup> ([ORCID: 0000-0001-8311-3702](https://orcid.org/0000-0001-8311-3702))
- Nick Gunn<sup>1</sup>
- Campbell Strong<sup>1</sup>
- Rowan T Hughes<sup>1</sup> ([ORCID: 0000-0001-5618-381X](https://orcid.org/0000-0001-5618-381X))
- Benjamin J Bailey<sup>1</sup>
- James Rae<sup>2</sup>
- Robert G Parton<sup>2</sup> ([ORCID: 0000-0002-7494-5248](https://orcid.org/0000-0002-7494-5248))
- John McGhee<sup>1</sup> ([ORCID: 0000-0002-9264-7535](https://orcid.org/0000-0002-9264-7535)) †

### Affiliations

1. 3D Visualisation Aesthetics Lab, School of Art and Design, and the ARC Centre of Excellence in Convergent Bio-Nano Science and Technology, University of New South Wales Sydney Australia
2. Institute for Molecular Bioscience, ARC Centre of Excellence in Convergent Bio-Nano Science and Technology, and Centre for Microscopy and Microanalysis, University of Queensland Brisbane Australia

† Corresponding author

## Abstract

Our understanding of cellular and structural biology has reached unprecedented levels of detail, and computer visualisation techniques can be used to create three-dimensional (3D) representations of cells and their environment that are useful in both teaching and research. However, extracting and integrating the relevant scientific data, and then presenting them in an effective way, can pose substantial computational and aesthetic challenges. Here we report how computer artists, experts in computer graphics and cell biologists have collaborated to produce a tool called Nanoscape that allows users to explore and interact with 3D representations of cells and their environment that are both scientifically accurate and visually appealing. We believe that using Nanoscape as an immersive learning application will lead to an improved understanding of the complexities of cellular scales, densities and interactions compared with traditional learning modalities.

## Introduction

Since the invention of the microscope in the 16th century and the subsequent discovery of a world concealed from our bare eyes, advances in experimental science and technology have excelled our understanding of cell biology. Modern imaging techniques were central to unravelling the intricacies of the cellular landscape at a molecular level. X-ray crystallography, NMR spectroscopy and cryo-electron microscopy achieve atomic- or near-atomic resolution of individual proteins and cell architecture, while live-cell imaging enables observation of cellular structures, processes and behaviours in real-time. Further, the use of enhanced fluorescent tags and biosensors has shed considerable light on protein kinetics, interactions and diffusion (Wollman et al., 2015; Goodsell et al., 2020).

Three-dimensional (3D) visualisation of scientific concepts and experimental data is nowadays a popular tool to provide insight where traditional, two-dimensional graphical illustrations or descriptive text cannot (Goodsell and Jenkinson, 2018). The educational benefits are numerous, from clarifying complex or abstract concepts to testing hypotheses and generating new ideas (Daly et al., 2016; Jenkinson and McGill, 2012; McClean et al., 2005; Kadir et al., 2020).

However, no single experimental modality is sufficient to elucidate the structure and dynamics of macromolecular assemblies and cellular processes. Therefore, integrative modelling of data from multiple, complementary techniques and scientific disciplines is crucial (Ornes, 2016). Scientific journals and bioinformatics databases contain a wealth of such data, but the extraction, interpretation and consideration of the relevant data is challenging (Conesa and Beck, 2019). Moreover, many biomedical visualisations do not cite journals or databases, meaning that users do not know if a given visualisation has been informed by empirical data, or if it owes more to artistic license (Goodsell and Johnson, 2007; Jantzen et al., 2015).

Biomedical animators often use 3D computer animation and modelling software popular in the games and entertainment industry, such as Autodesk Maya (https://autodesk.com/maya), SideFX Houdini (https://www.sidefx.com/products/houdini/) and Pixologic Zbrush (http://pixologic.com/features/about-zbrush.php). However, the true complexity of the cellular environments is often deliberately diminished to clarify or emphasise features and mechanisms of interest. It may also be reduced for other reasons, such as technical limitations of computer graphics or time constraints (Goodsell and Johnson, 2007).

The last couple of decades have seen an increase in visualisation software tools and accurately scaled, static reconstructions at the molecular level. Notable examples are the HIV-1 virus and Mycoplasma mycoides (created with the packing algorithm CellPACK), and a snapshot of a synaptic bouton obtained through integrating a plethora of imaging techniques, quantitative immunoblotting and mass spectrometry (Johnson et al., 2015; Johnson et al., 2014; Wilhelm et al., 2014). Previously, simulations of Brownian or molecular dynamics have been incorporated into 3D atomic resolution models of bacterial cytoplasmic subsections to examine the effect of the interactions, stability and diffusion of proteins in crowded cellular environments (Feig et al., 2015; Yu et al., 2016; McGuffee and Elcock, 2010).

Furthermore, mathematical and computational modelling platforms such as V-Cell, M-cell, and E-cell are designed to be used by experimental biologists and theoretical biophysicists (Moraru et al., 2008; Stiles and Bartol, 2001; Stiles et al., 1996; Tomita et al., 1999). These platforms can run simulations of cell biological phenomena based on a combination of multiple ‘omics’ technologies and imaging data, thereby enabling scientists to analyse 3D representations of their raw data and test hypotheses with varying degrees of molecular and spatial resolution.

However, many of the existing techniques described above do not fully represent cellular environments, mostly due to sheer complexity but also because of lack of funding or knowledge, or computational limitations. Our previous project (Journey to the Centre of the Cell) already showed significant improvement in the students’ comprehension of cellular structures and processes (Johnston et al., 2018). It provided an immersive, virtual reality educational experience of an entire 3D cell based on serial, block-face scanning electron microscope imaging data. Although the project successfully depicted cellular features from real microscopy data, portrayal of the cell surface environment had to be oversimplified due to various constraints, including working at higher virtual reality frame rates (over 90 fps) and a smaller development team.

Nanoscape is a collaborative follow-up project between computer artists, experts in computer graphics and cell biologists to create an interactive real-time open-world experience that enables a user to navigate a cell terrain within a tumour microenvironment. This first-of-its-kind application distils and integrates a vast archive of scientific data into an interactive immersive experience using a comprehensive library of existing visualisation tools, while employing distinct principles of art and design. Nanoscape is primarily an educational tool for tertiary-level science students, and it is available at https://store.steampowered.com/app/1654050/Nanoscape.

## Using Nanoscape to visualize cell surface proteins and cancer cells

Here, we present some of the challenges and limitations experienced during the data collection process and the conceptualisation of 3D assets, and examine the practicability of visually replicating experimental data. We discuss the implications of gaps in scientific knowledge, modification or simplification of data, and the use of artistic license for visual clarity. Our work raises important questions about whether molecular visualisations can support outcomes beyond the educational field and could help experimentalists to better understand their data.

As part of the pre-production stage, information on the major surface components, extracellular features and processes commonly found in breast cancer scenarios was collated through a comprehensive review of the literature along with analysis of experimental data obtained from scientific collaborators (Figure 1). This cell type was chosen as the focus of the visualisation due to the abundance of protein and structural data available from these sources.

![Figure 1.](https://cdn.elifesciences.org/articles/64047/elife-64047-fig1-v1.jpg)

**Figure 1.:** A 3D model of a breast cancer cell (upper left panel). The region inside the yellow box is shown in more detail in the lower left panel, and region inside the pink box is shown in more detail in the panel on the right. The lower left panel details the components of the extracellular matrix (such as collagen I and proteoglycans), filopodia and macropinocytosis structures (which engulf extracellular material and fluid). The right panel details extracellular vesicles (exosomes), pits in the plasma membrane (caveolae and clathrin coated pits), plasma membrane lipids, surface proteins, components of the extracellular matrix (proteoglycans, collagens I and IV), and a 20 nm nanoparticle. The light red figure in the right panel is 40 nm tall. See Video 1 for animations of some of these processes. ECM: extracellular matrix.

### Cell surface proteins

Cell surface proteins, collectively known as the surfaceome, exhibit a wide range of roles, from playing a vital role in communication between the cell and its environment to signal transduction and transport of ions and other small molecules (Bausch-Fluck et al., 2018). The Cell Surface Protein Atlas (wlab.ethz.ch/cspa) and the in silico human surfaceome (wlab.ethz.ch/surfaceome), which together have classified 2886 entries, were used to first identify different types of surface proteins, such as receptors, soluble and membrane transport proteins (Bausch-Fluck et al., 2015; Bausch-Fluck et al., 2018). Subsequently, over 30 prevalent surface proteins associated with breast cancer that were available from the RSCB Protein Data Bank (PDB) were selected and organised in a cast of characters (see Appendix 1 and Figure 2; Berman et al., 2000). Where possible, any available information on their motion (molecular dynamics, conformational changes and protein interactions), and population densities were interpreted from various published sources.

![Figure 2.](https://cdn.elifesciences.org/articles/64047/elife-64047-fig2-v1.jpg)

**Figure 2.:** Stylized 3D meshes modelled from structures retrieved from the RSCB Protein Data Bank (PDB). Most proteins are depicted as monomers; see Appendix 1 for details.

The structural and dynamic information gathered about the ErbB family of proteins (which consists of 4 receptor tyrosine kinases: EGFR, Her2, Her3, and Her4) and the associated literature references used to create mechanism of action animations for each family member are summarised in Figure 3 and Appendix 2. Molecular Maya (mMaya) modelling and rigging kits (https://clarafi.com/tools/mmaya/), which qualitatively replicate molecular dynamics, were used to simulate ligand binding events and transitions between conformational states (see Materials and methods). These rudimentary mechanism of action animations provided an interpretation of protein movement based on experimental data available and were subsequently used to inform the artistic design team on how best to approach rigging a refined, stylised 3D protein mesh using traditional rigging methods (Figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/64047/elife-64047-fig3-v1.jpg)

**Figure 3.:** (A) Structural and dynamic information about the four proteins in the ErbB family of proteins (EGFR, Her2, Her3, and Her4) and their ligands. Top: Mechanism of action for EFGR which, upon ligand binding, undergoes a conformational change (130° movement) into the active extended conformation; it can also form a dimer with another active EGFR protein. Bottom: PDB structures, ligands and dimer partner combinations for Her2, Her3 and Her4. (B) The creation of stylized protein meshes starts with structures sourced from the PBD (top); the backbone is extruded and the structure is then refined to produce the mesh (bottom). (C) A 3D model of a lipid bilayer in a cancer cell, highlighting an asymmetric distribution of 400 lipids (data adapted from Shahane et al., 2019). The bilayer components include cholesterol (CHOL), 1-palmitoyl-2-oleoyl-sn-glycero-3-phosphocholine (POPC), 1-palmatoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine (POPE), 1-palmitoyl-2-oleoyl-sn-glycero-3-phospho-L-serine (POPS), and palmitoylsphingomyelin (PSM). The proportion of each lipid species within the outer and inner leaflets is shown on the left; the percentage of each species in the bilayer is shown on the right. The two hexagonal shapes are side views of a model cancer plasma membrane with proteins EGFR and GLUT1.

Conformational flexibility plays a crucial role in enabling protein-ligand interactions, multi-specificity and allosteric responses. Unfortunately, most proteins have no reliable, or only partial experimentally determined 3D structures, available. Such limitations may lead to a presentation of a single, ‘native’ structure in visualisations, instead of multiple flexible conformational variations, further perpetuating misconceptions about protein structure, folding, stability and effects of mutations (Robic, 2010). Where possible, Nanoscape used several conformational states of proteins sourced from the PDB as well as conformational changes simulated with mMaya (see Materials and methods). The choice of protein mesh detail and representation will also affect the viewer. A low poly mesh will significantly reduce the computational burden in rendering but may compromise important scientific information, such as the specificity of a ligand binding pocket that may be essential for conveying the mechanism of action. Nanoscape incorporates a level-of-detail feature that reduces the polygon density of proteins as a function of distance to the user, thereby decreasing the computational burden of distant proteins without affecting perceived detail. It also allows more proteins to be displayed on screen simultaneously.

Protein dynamics can range from localised movement in specific residues to large rearrangements in domains and multiple subunits. Representing these broad spatio-temporal scales is a major challenge for biomedical animators. Protein bond vibrations and domain motions can range from femtoseconds to milliseconds respectively, and in turn, many cellular processes occur in the order of seconds to minutes (McGill, 2008; Miao et al., 2019). Multi-scale representations in landscape animations of cells often have constrained computer graphics performances, sacrificing atomic resolution and motion.

Cellular environments are heterogeneous, highly dynamic and densely packed. Up to 20% to 30% of intracellular environments is occupied by macromolecular components (Goodsell et al., 2020). Molecular crowding is known to influence the association and diffusion of proteins, as well as the rates of enzyme-catalysed reactions (Mourão et al., 2014). Yet many visualisations eschew depicting stochastic motion and extreme crowding due to fear of losing focus on the visual narrative or cognitive overload (Goodsell and Johnson, 2007; Jenkinson and McGill, 2012). Furthermore, the computational expense involved with animating and rendering large numbers of meshes is a significant hurdle. However, underrepresentation or oversimplification has been shown to worsen deep rooted misconceptions, particularly amongst students (Garvin-Doxas and Klymkowsky, 2008; Gauthier et al., 2019; Jenkinson et al., 2016; Zhou et al., 2008). Indeed, our inherent ability to picture such numbers in real life is a challenge, and therefore it is useful to perform ‘sanity checks’ (Zoppè, 2017).

We assessed the feasibility of replicating receptor densities based on empirical data, using the 3D computer graphics application Blender (https://www.blender.org/) and the plugin autoPACK (Johnson et al., 2015). The autoPACK algorithm can fill compartmental volumes or surfaces with user defined meshes or protein meshes retrieved from the PDB and has been previously used to generate models of HIV, blood plasma and synaptic vesicles (Johnson et al., 2015; Takamori et al., 2006).

Receptor density values (number per μm2) of six well-known surface biomarkers on MDA-MB-231 cells from flow cytometry data were modelled on 1 μm2 area test patches (Cahall et al., 2015). The packing simulations revealed 12,650 proteins of variable sizes were easily accommodated with moderate molecular crowding (Figure 4). The diversity of surface proteins varies significantly between different cell types, and whilst a fairly equal distribution was modelled for this scenario, proteins are often clustered in functional units or spread unevenly. In addition, the limitations of experimental techniques ought to be scrutinised, for instance, variations in the specificity of antibodies measured with flow cytometry could potentially lead to under- or over exaggeration of numbers. Often, the receptor density data measured is only a snapshot in time, while the receptor population on a cell is highly dynamic and stochastic. Nevertheless, further exploration of experimentally derived population densities using packing algorithms such as autoPACK will improve our understanding of surface protein distribution and organisation.

![Figure 4.](https://cdn.elifesciences.org/articles/64047/elife-64047-fig4-v1.jpg)

**Figure 4.:** (A) PDB meshes of 6 well-known surface biomarkers (CD44, EGFR, EpCAM, Her2, ICAM1 and αVβ3 integrin) on MDA-MB-231 cells from flow cytometry data (Cahall et al., 2015). (B) Scaled receptor meshes were distributed onto a 1 µm2 surface area sphere and plane using the autoPACK plugin in Blender.

A negative consequence of choreographed molecular visualisations is that they can often allude to ‘directed intent’, the most common example being a ligand moving undisturbed towards a receptor, which subsequently leads to immediate binding. A more authentic depiction might be a random walk (constrained by kinetics and thermodynamics) through a packed environment, where the ligand undergoes many non-specific interactions before binding successfully (Jenkinson and McGill, 2012; Robic, 2010). Biomedical artists may be disinclined to animate unsuccessful binding events to save on animation and render time, but this will only deepen superficial understanding or promote misconceptions. Whether visual clutter in crowded molecular environments has a negative impact on audiences is a point of contention. Careful use of graphic devices such as titles or arrows, narration and colour can improve complex visualisations and understanding (Jenkinson et al., 2016; Jenkinson and McGill, 2012; McClean et al., 2005).

### Plasma membrane lipids

All eukaryotic cells are surrounded by a plasma membrane consisting of a ~ 4 nm thick lipid bilayer that acts as a semi-permeable barrier between the cell and its environment. It is also a landscape where many signalling events and biological processes take place. Inside cells, specialised compartments are enclosed by lipid membranes to form discrete organelles, segregating their contents from the cytoplasm (Kobayashi and Menon, 2018; van Meer et al., 2008).

Lipidomics studies have brought great insight into the structure, dynamics and interactions of a variety of lipids within cells (Ingólfsson et al., 2014). Lipid bilayers are densely packed with approximately 5 × 106 molecules per 1 μm2 area and can encompass hundreds of different species (Alberts et al., 2002). The most common structural lipids in eukaryotic membranes are glycerolipids (~65%), sterols (~25%) and sphingolipids (~10%) (Shahane et al., 2019). Whilst cholesterol is generally evenly distributed between the bilayer leaflets, an asymmetric distribution of lipids contributes to their functionality (van Meer et al., 2008). The inner leaflet has a greater proportion of phosphatidylethanolamine, phosphatidylserine, and phosphatidylinositol lipids; in contrast, the outer leaflet is more abundant in phosphatidylcholine and sphingolipids (Kobayashi and Menon, 2018).

In vivo imaging of membranes is experimentally difficult due to their inherent flexibility and highly dynamic fluctuations. Consequently, computational simulations mainly based on in vitro data have been important for understanding the heterogeneity and dynamics of plasma membranes that may exist in distinct phases, and the organisation of protein complexes therein. Near-atomic models of cell membranes composed of numerous lipid constitutions have been created in silico (Ingólfsson et al., 2014). Figure 3C depicts a typical lipid bilayer of a cancer cell, with a representative complement of lipid species visualised using the CHARMM-GUI Membrane Builder to highlight some of the differences between the inner and outer leaflets (Shahane et al., 2019; Jo et al., 2008).

Lipids can move rotationally and laterally within their leaflet and transversely between bilayers. Lateral mobility can be expressed by an experimentally determined diffusion coefficient (D). Many lipids have a D value of ~1 μm2 s−1, which corresponds to a lipid diffusing a distance of 2 μm within 1 s. In contrast, transverse diffusion or ‘flip-flop’ is a far slower process that can take hours and is regulated by flippases and floppases to maintain bilayer asymmetry (Berg et al., 2002).

Replicating lateral diffusion of millions of lipids at speed in whole-cell and environmental molecular visualisations is not only computationally intensive – it is also questionable whether the viewer can fully observe or appreciate such minutiae in a large scene or glean any real insight. To navigate these extensive challenges, the plasma membrane in Nanoscape is instead driven by an animated texture to simulate their form and dynamics.

### Cellular processes

Cellular processes fall within the biological mesoscale, which is an intermediate scale range between nanometre-sized molecular structures and micrometre-sized cellular architecture (Goodsell et al., 2018; Laughlin et al., 2000). An integrative modelling approach was adopted whereby information from multiple sources was combined for depiction of mesoscopic processes on the cell surface. Surface processes of interest were categorised as either protrusion (filopodia), invaginations (caveolae, clathrin-coated pits, or macropinocytosis) or extracellular vesicles (exosomes; see Table 1). Scanning electron microscopy and transmission electron microscopy data were used to calculate the approximate dimensions of typical breast cancer cells, along with sizes and densities of protrusions and invaginations (Figure 5). These measurements were in accordance with published data. Similarly, information on temporal dynamics was taken from research literature (Table 1). Since these data fell within a broad temporal range varying from seconds to minutes, cellular features were modelled and animated using 3D software Zbrush and Maya (Figure 5 and Video 1).

![Figure 5.](https://cdn.elifesciences.org/articles/64047/elife-64047-fig5-v1.jpg)

**Figure 5.:** (A) Representative SEM images of MDA-MB-231 cells. The boxed area shows a higher magnification of filopodia (pseudocoloured blue) and putative pits (caveolae, clathrin coated pits) in red. (B) Representative TEM images of sections of MDA-MB-231 cells. Filopodia are visible in the upper left panel (pseudocoloured blue). Clathrin coated pits are visible in the upper right and lower left panels (red) and right. Caveolae are visible in the lower left panel (green). The lower right panel shows the region inside the red box in the lower left panel at higher magnification. (C) 3D depiction of filopodia, caveolae, clathrin coated pits, and a representative receptor on a 100 µm2 patch on the cell membrane.

**Table 1.**
 Cellular structures and processes in Nanoscape.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Feature</th>
      <th>Examples</th>
      <th>Dimensions</th>
      <th>Density</th>
      <th>Temporal dynamics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">Structures</td>
      <td>Membrane bound receptors1</td>
      <td>EGFR, Integrins, VEGFR</td>
      <td rowspan="2">~5–20 nm length; ~1–5 nm diameter</td>
      <td rowspan="2">Protein specific ~10–104 per µm2</td>
      <td rowspan="2">Protein specific D ~ 10−3–1 µm2/s [see note 10]; Transitions between protein states ~ 1–100µs</td>
    </tr>
    <tr>
      <td>Soluble proteins1</td>
      <td>EGF, TNF, MMPs</td>
    </tr>
    <tr>
      <td>Membrane transport proteins2</td>
      <td>GLUT4, K+ channel, Na+/K+ pump</td>
      <td>~4–10 nm length</td>
      <td>~104 per µm2</td>
      <td>~100–107/s transport rate</td>
    </tr>
    <tr>
      <td>Extracellular matrix3</td>
      <td>Collagens, Fibronectin, Hyaluronic acid</td>
      <td>Variable: from large fibres to smaller glycoproteins</td>
      <td>Variable</td>
      <td>Very low mobility relative to proteins</td>
    </tr>
    <tr>
      <td>Plasma membrane4</td>
      <td>Phospholipids</td>
      <td>~2 nm length;~0.25–0.5 nm2 cross-sectional area</td>
      <td>~5×106 per µm2</td>
      <td>†D ~ 1 µm2/s</td>
    </tr>
    <tr>
      <td rowspan="5">Processes</td>
      <td>Protrusions</td>
      <td>Filopodia5</td>
      <td>~1–5 µm length; ~150–200 nm diameter</td>
      <td>~0.3 per µm2</td>
      <td>~25–50 nm/s protrusion rate</td>
    </tr>
    <tr>
      <td rowspan="3">Endocytosis</td>
      <td>Caveolae6</td>
      <td>~65 nm mean diameter; ~0.0067 µm2 area</td>
      <td>~10 per µm2</td>
      <td>~30 s to minutes</td>
    </tr>
    <tr>
      <td>Clathrin mediated endocytosis7</td>
      <td>~110 nm mean diameter; ~0.0190 µm2 area</td>
      <td>~0.8 per µm2</td>
      <td>~30–60 s</td>
    </tr>
    <tr>
      <td>Macropinocytosis8</td>
      <td>~0.2–5 µm diameter</td>
      <td>?</td>
      <td>~120 s</td>
    </tr>
    <tr>
      <td>Extracellular vesicles</td>
      <td>Exosomes9</td>
      <td>~40–150 nm diameter</td>
      <td>?</td>
      <td>?</td>
    </tr>
  </tbody>
</table>

_* Key features of cellular structures and processes in Nanoscape, with examples detailing properties such as dimensions, densities, temporal dynamics. See Figure 1 for 3D models.Notes: 1 Membrane bound receptors and soluble proteins. Milo et al., 2010. 2 Membrane transport proteins. Milo et al., 2010. Chapter IV in Milo and Phillips, 2015. Page 9 (top paragraph) in Itzhak et al., 2016. Table 8.3 in Gennis, 1989. 3 Extracellular matrix. Frantz et al., 2010. Insua-Rodríguez and Oskarsson, 2016; Früh et al., 2015; Mouw et al., 2014; Pankov and Yamada, 2002. 4 Plasma membrane lipids. Milo et al., 2010. Chapter II in Milo and Phillips, 2015. Chapter 10 in Alberts et al., 2002. Table 1 in Rawicz et al., 2000. Page 2644 (right column, 2nd paragraph) in Brügger et al., 2006. 5 Filopodia density and dimensions. Measured from scanning electron micrographs, see Figure 5 in Mallavarapu and Mitchison, 1999. 6 Caveolae density, dimensions and temporal dynamics. Parton, 1994; Parton et al., 2020a; Parton et al., 2020b; Pelkmans and Zerial, 2005; Boucrot et al., 2011; Richter et al., 2008. 7 Clathrin mediated endocytosis density, dimensions and temporal dynamics. Cocucci et al., 2012; Doherty and McMahon, 2009; Edeling et al., 2006; Kirchhausen, 2009; McMahon and Boucrot, 2011; Merrifield et al., 2002; Parton, 1994; Saffarian and Kirchhausen, 2008; Taylor et al., 2011. 8 Macropinocytosis dimensions. Condon et al., 2018; Lim and Gleeson, 2011. 9 Exosome dimensions. Skotland et al., 2017. 10 Diffusion coefficient. D is microscopically determined by the velocity of the molecule and the mean time between collisions._

![Video 1.](https://cdn.elifesciences.org/articles/64047/elife-64047-video1.mp4.jpg)

**Video 1.:** The human figure shown in some of the models is 40 nm tall. Figure 1 and Figure 5 provide more information about these processes.

### Extracellular matrix

The extracellular matrix (ECM) surrounding cells is an extensive and complex network of structural fibres, adhesion proteins and glycosaminoglycans. It works as a scaffold for the cellular environment and can also influence behaviours, processes and communication of a cell (Frantz et al., 2010; Insua-Rodríguez and Oskarsson, 2016; Mouw et al., 2014). The ECM consists of two biochemically and morphologically distinct forms: the basement membrane, which is a thin layer that forms between epithelial and stromal cells, and the adjacent interstitial matrix, which is a more loosely organised network surrounding cells (Mouw et al., 2014).

Despite its vital role, the ECM is often overlooked in many cellular and molecular visualisations due to several reasons. Firstly, high resolution imaging of the ECM in its native state is inherently difficult in opaque tissue. Whilst optical tissue clearing and decellularisation methods are routinely used to enhance the visibility in stained tissues and organs, they are often harsh treatments that may modify the physical and chemical properties of the ECM (Acuna et al., 2018). In addition, many in vitro models consisting of a limited mix of collagens and matrix proteins, such as cells suspended in 3D gels, may not always be physiologically relevant.

The components within the matrix are often very large macromolecular complexes, and although complete protein sequences are available on Uniprot, many PDB structures are only of truncated or incomplete proteins (UniProt Consortium, 2018). Consequently, it is an arduous task to visualise these large ECM structures in their entirety, and some artistic license may be needed.

To visualise the ECM within a 3D breast tumour microenvironment, we collated information from the literature, including images, and sought advice from experts in the field during the conceptualisation stage (Figure 6A; Table 1). Although there are a multitude of ECM components that make up the tumour microenvironment, for simplicity it was decided the focus would be only on four key ECM players: collagens I and IV, hyaluronic acid and fibronectin (Mouw et al., 2014). In breast cancer, there is usually increased deposition of collagen and fibronectin, and a significant disruption of collagen IV basement membrane networks (Frantz et al., 2010).

![Figure 6.](https://cdn.elifesciences.org/articles/64047/elife-64047-fig6-v1.jpg)

**Figure 6.:** A pre-production sketch (A) and a 3D model (B) of collagen I fibrillar bundles and proteoglycans (such as hyaluronic acid). (C) Collagen IV protomers and dimers. (D) Fibronectin dimers bound to active αVβ3 integrin. (E) Artistic interpretation of the extracellular matrix in a tumour microenvironment. The insert shows the scale of the modelled area (circle) relative to a breast cancer cell model (which has a diameter of ~10 µm).

A stylised artistic approach was adopted to build 3D meshes of the ECM using the modelling program Zbrush. This significantly reduced the polycount of large complex atomic macromolecules, which would otherwise be computationally expensive to render (Figure 6B–D; Materials and methods). Following advice from an ECM expert (S. Kadir personal communication with Dr Thomas Cox, Garvan Institute, July 2019), an artistic impression of a tumour microenvironment niche was built, highlighting interactions between integrin molecules on the cell surface and meshes of the basement membrane and interstitial matrix (Figure 6E).

Due to significant gaps in knowledge, many visualisation challenges were identified early on during the conceptualisation stage. Exactly how ECM proteins interact with one another to eventually form higher order structures such as fibrils, fibres and ultimately matrices, is very unclear. ECM remodelling is a highly dynamic ongoing process, which involves both proteolytic breakdown of existing matrix components by matrix metalloproteases (MMPs) and deposition of new components by cells. This intrinsic activity has significant implications on tissue development, cell migration and pathologies including cancer (Frantz et al., 2010; Insua-Rodríguez and Oskarsson, 2016; Mouw et al., 2014). However, there is not enough discernible data in the literature to reliably inform anyone trying to represent these processes, and as such, much of this detail was omitted from the ECM represented in Nanoscape.

Many molecular visualisations fail to show connections between the cell surface and the ECM (via cell adhesion molecules binding to ECM components) or veer away from even attempting to represent ECM density in vivo. This may be a combination of incomplete information about precise binding interactions, and a reluctance to complicate a scene for fear of cognitive overload. However, its frequent omission or aggressive simplification will only exacerbate a naive view of the ECM in vivo, whereas there is evidence that more complex molecular representations can in fact improve understanding (Jenkinson et al., 2016; Jenkinson and McGill, 2012).

### Tumour microenvironment components

In addition to malignant cells and the ECM, a breast tumour microenvironment is made up of a complex mix of cells (including immune cells, fibroblasts, pericytes and adipocytes), blood vessels, lymphatics and various signalling molecules, and many studies show that cancer cells significantly impact their environment; it has also been shown that interactions with non-transformed cells and the tumour vasculature promote the progression of cancer (Balkwill et al., 2012; Quail and Joyce, 2013; Insua-Rodríguez and Oskarsson, 2016). To build a more comprehensive tumour microenvironment, additional breast cancer cells, cancer-associated fibroblasts and a leaky blood vessel with an animated blood flow were incorporated into the Nanoscape scene (Figure 7; Video 2; Materials and methods).

![Figure 7.](https://cdn.elifesciences.org/articles/64047/elife-64047-fig7-v1.jpg)

**Figure 7.:** (A) Additional neighbouring cancer cells (transparent) surrounding the central or main cancer cell. (B) Cancer-associated fibroblasts (CAFs) entangled in collagen fibres. (C) Leaky blood vessel surrounded by basement membrane mesh (left); snapshot of animation with red blood cells flowing through the vessel (right; see also Video 2).

![Video 2.](https://cdn.elifesciences.org/articles/64047/elife-64047-video2.mp4.jpg)

## The Nanoscape user experience

Nanoscape is distinct from other published molecular and cellular visualisations, being a data-informed artistic innovation that permits user exploration and reflection of a tumour microenvironment. The Nanoscape scene was compiled in the real-time graphics engine Unity3D (https://unity.com/) and can be currently viewed in engine on a desktop gaming PC (with minimum of 1080 GTX GPU). Here, the user is essentially shrunk down to an equivalent height of 40 nm and is able to walk on the surface of a single cancer cell within a discrete play area surrounded by the ECM, neighbouring cancer cells, cancer-associated fibroblasts and a leaky blood vessel to observe surface proteins and cellular processes moving in real-time (Figure 8).

![Figure 8.](https://cdn.elifesciences.org/articles/64047/elife-64047-fig8-v1.jpg)

**Figure 8.:** Vistas from the Nanoscape real-time open-world experience with key cellular features and microenvironment components highlighted. (A–C) Panoramic views showing surface receptors on the plasma membrane along with neighbouring cancer cells, filopodia, collagen I fibres, and blood vessels. Close-up views of surface receptors and lipids (D) and a caveolae (E).

Since the user experience was fundamental to the project, it became clear that true depiction of extreme molecular crowding and the ECM had to be compromised. Extraneous complexity such as the density of soluble molecules present in the extracellular space was significantly diminished, water and ions implicit, lipid meshes were substituted with a texture to mimic their form and dynamics, and the ECM reduced to only collagen I fibres, to enable greater visibility of the landscape.

Similarly, it was computationally demanding and aesthetically unfavourable to replicate the broad temporal ranges of both molecular and cellular processes. Whilst the dynamics of the major cellular processes could be animated accurately, atomic resolution was sacrificed, and protein conformational movement was appreciably slowed down to enable viewers to observe protein-protein interactions more clearly. To partially compensate for these diminutions, some artistic license was applied to evoke the ‘feel’ of a densely packed cancerous milieu through use of colour, lighting, and sound, even if nanoscale cellular entities are below the wavelength of light and devoid of noise.

Nanoscape has significantly surpassed the level of cell surface detail and complexity found in Journey to the Centre of the Cell. And although it is not fully immersive or interactive as the virtual reality experience of Journey to the Centre of the Cell, it has been carefully choreographed to engage the viewer to appreciate the heterogeneity of a tumour microenvironment, without overwhelming them with minutiae and promote understanding of some cell biology fundamentals. Future work involves the development of user-defined control features, which empower the viewer to focus in or out of regions to switch between observing atomic detail to large cellular processes, and adjustable dials for regulating molecular density and temporal dynamics, to experience a more authentic cellular environment.

### Evaluation and broader applications

Though outside the scope of the development stage of the project, formal evaluation of the user experience and objective outcomes is necessary and will inform the practicality of this application as an educational aid. In particular, what effect does increasing the authenticity of the visualisations (with respect to biological densities, scales and interactions) have on users' fundamental understanding of cell biology? In future studies it will be prudent to test several versions of the application varying these parameters and assess the students’ comprehension of core concepts, such as the effect of receptor density on ligand biding.

It is hypothesised that increasing the authenticity of visualisations will improve the comprehension of these advanced topics, as has been observed in similar studies (Jenkinson and McGill, 2012). Both qualitative and quantitative aspects of the user experience, including visual attention (through eye-tracking software), analytics such as time spent in specific locations, and subjective measurements of the users’ visual and mental load, can also be assessed while varying these parameters.

Further analysis might also investigate whether learning outcomes can be influenced by the delivery platform of this application, evaluating the interactive PC experience or virtual reality immersive experience against similar content delivered in a more linear narrative, such as standard video format. Allowing users to control what aspects of the landscape they view and interact with may help them to focus on specific gaps in knowledge. This data is likely to inform science educators on the most appropriate level of detail and delivery platform for each learning objective.

Beyond the didactic purpose of the application, Nanoscape is well-poised to be a valuable public outreach tool. In addition to rich scientific detail, thoughtful consideration was given to key design elements such as colour theory and sound design. These arts-led influences allow Nanoscape to sit alone as a piece of science-based art, inviting the user to wonder at the chaotic molecular landscapes within the body. Whether this type of visualisation offers benefits to the wider scientific research community is yet to be seen. While the artistic and computer graphics-related treatments of proteins and cellular components in Nanoscape is unlikely to make this application suitable for rigorous data interrogation, it may stimulate more holistic reflection of biological systems. Applications that allow multimodal data exploration are promising and may promote broader scientific speculation than each modality examined separately.

### Data collection archiving

Created in 1971, the PDB remains the largest international repository for experimentally determined atomic structures. Considerable progress has been made in recent years to develop platforms and standards for archiving, validating, and disseminating new biological models defined by the PDBx/mmCIF dictionary (Young et al., 2018). Integrative or hybrid modelling structures are, however, not currently included in the PDB because data standards for archiving have not yet been implemented. Hence, the PDB-Dev was established in 2018 as a prototype archiving system (https://pdb-dev.wwpdb.org) (Vallat et al., 2018). This repository contains embedded 3D viewers, links to download structures and related database entries, but also includes citations, input data and software used in the creation of models. Whilst many biomedical animators take models from such sources, clear citation of their molecular visualisation content is often limited.

The information gathered during the pre-production phase of Nanoscape is summarised in Figure 1, Table 1 and Appendix 1 (which includes the PDB IDs for the proteins). Furthermore, Appendixes 2–9 document the methodology behind the creation of mMaya mechanism-of-action animations for the following receptors: EGFR and Her3 (Appendix 2; Kovacs et al., 2015); αVβ3 integrin (Appendix 3; Zhu et al., 2008; Chen et al., 2011); VEGFR1 (Appendix 4; Sarabipour et al., 2016); c-KIT (Appendix 5; Felix et al., 2015); insulin receptor (Appendix 6; Gutmann et al., 2018); Tetraspanin CD81 (Appendix 7); the TNFR superfamily of receptors (Appendix 8; Naismith et al., 1996; Vanamee and Faustman, 2018); and GLUT1 (Appendix 9). These appendixes also include associated references, and information on the artistic approaches taken for modelling assets, along with explanatory comments.

Archiving the information taken from a variety of literature, databases and communication with experts in the field and presenting it in an accessible format will enable others to freely scrutinise or validate the work impartially, and to potentially build new, improved future versions. Selecting and curating vast amounts of information is, however, extremely time consuming, requires an aptitude for interpreting scientific data, and is a constant race to keep abreast of the latest discoveries. Similarly, sustaining up-to-date versions of large-scale complex projects such as Nanoscape whenever new data becomes available, or existing information is proved redundant, is a huge challenge and only reinforces the need for transparent systems of citation in scientific visualisations and comprehensive procedural frameworks to seamlessly implement new models or animations.

## Conclusions

Nanoscape is an innovative collaboration that has produced a multi-scale, explorable 3D environment of a cell. Our work sheds light on some of the technical and creative processes, decisions and sacrifices made in depicting cell surface entities and dynamics as close to experimental data as possible, whilst balancing concerns for the user experience and visual aesthetics. Although initially its main purpose was to be a unique educational and outreach tool to communicate some of the complexities of a tumour microenvironment, the final visualisation experience may also help experimentalists to reflect upon their own data.

Integrative modelling and visualisation of biomolecular systems and multi-scale cell models are becoming increasingly sophisticated, and immersive, virtual field trips to a cell environment such as Nanoscape may provide insights into function and behaviour of a cell. As computer hardware and software continues to evolve to cope with processing enormous amounts of data, improved visual or interactive 3D representations may one day lead the way for scientists to perform in silico experiments and potentially help with the development of new drugs.

Ideally, such a model would fully reflect the spatio-temporal complexities and heterogeneity of the entire cell and its environment and would be capable of continuous iterations and be falsifiable. To accomplish such an ambitious feat, researchers and developers from multiple scientific, computer graphics and design fields must work together.

## Materials and methods

### Software

Commercially available 3D computer graphics software for animation and modelling, Maya (https://autodesk.com/maya), the plugin Molecular Maya (mMaya; https://clarafi.com/tools/mmaya/), and Zbrush (http://pixologic.com/features/about-zbrush.php) were used to build and animate assets. The 3D procedural software Houdini (https://www.sidefx.com/products/houdini/) and the cross-platform game engine Unity3D (https://unity.com/) were used to compile the Nanoscape open-world environment; see ‘Nanoscape open-world compilation’ below for details. Unless stated, all images were rendered in Maya using Arnold at 4K (3840 × 2160).

The Unity3D game engine was used to assemble the various components into a coherent representation of a cell surface environment. Static assets were imported into the engine by standard methods. The animated cellular processes and horde of proteins were integrated and simulated in Houdini and output as custom caches that are streamed into Unity3D at runtime.

### Proteins

Protein structures were retrieved from the RSCB Protein Data Bank (PDB), and mechanism-of-action animations were simulated using the mMaya modelling and rigging kits. Rigged surface or backbone meshes were extracted, and animation playblasts recorded in Maya and composited in After Effects (Adobe CC). See Appendixes 1–9 and ‘Surface protein simulations’ below for details.

For the creation of stylised proteins, polygonal backbone meshes extracted from PDB structures were sculpted and textured in Zbrush, with textures exported for later use as detail maps in the rendering software. Images were rendered in Maya using Arnold at 1400 × 1400.

Receptor density simulations on 1 μm2 surface areas (sphere and plane) based on MDA-MB-231 cells from flow cytometry data were created in Blender 2.78 using the plugin autoPACK (autopack.org) with the spheresBHT packing method (Cahall et al., 2015; Johnson et al., 2015). Low poly PDB meshes of CD44, EGFR, EpCAM, Her2, ICAM1 and αVβ3 integrin were created in mMaya.

### Lipids

A lipid bilayer consisting of 400 lipids was simulated using the CHARMM-GUI Membrane Builder (Jo et al., 2008) based on data from Table 2 in Shahane et al., 2019. UCSF Chimera was used to export lipid meshes to Maya (Pettersen et al., 2004).

### Cells, cellular processes and ECM models

Information on dimensions and temporal dynamics were taken from the literature and data from our collaborators (See Table 1). All 3D assets were modelled in Zbrush or Maya. Cellular processes were animated in Maya.

### Surface protein simulations

Mechanism-of-action (MoA) animations for nine selected receptors were made using the mMaya Modelling and Rigging Kits (https://clarafi.com/tools/mmaya/). mMaya simulations are qualitative and were used to inform the artistic design about general conformational changes and movements that may occur in receptor-ligand binding events. The mMaya Rigging Kit relies on Molecular Mechanics force fields to model molecular structures and their interactions and uses Maya’s particle system and nucleus solver to simulate structural changes and interactions. Molecular Mechanics force fields model how atoms can interact through simplified potentials, and provide a set of spatial restraints (distance, angular, dihedral) to preserve the stereochemistry of each chemical building block imported into the software. By using these force field parameters and molecular topologies, the Rigging Kit builds molecular ‘rigs’ and provides a set of tools for users to apply various external forces interactively. Unlike molecular dynamics simulations, which follow strict thermodynamic laws and make them suited to explore the unsupervised evolution of a molecular system, the mMaya Rigging Kit provides a molecular simulation environment for atomic and coarse-grained molecular models that avoids steric clashes while allowing users to orchestrate complex transitions and large conformational changes.

All rigs were ‘all atom no hydrogen’ constructs and conformational changes were simulated by either target morphing between two endpoint PDB structures (usually inactive and active states), for example EGFR (1NQL → 3NJP) (see Appendix 2, which includes a MoA animation for EGFR), or manually moving handles added to selected regions of the protein rig (e.g., domains). For some proteins where only one PDB structural state was available, as with Her3 (inactive, 1M6B), movement was approximated by targeting protein domains to morph into the conformational state of another known family member (in this case active Her4 3U7U; see Appendix 2, which includes a MoA animation for Her3). In addition, simulations were inferred from MoA hypotheses published in the literature, and rig handles were applied to manipulate the movement of protein rigs to create a ‘hypothetical’ conformation, as in the case of αVβ3 integrin extended form conformation (see Appendix 3, which includes a MoA animation for αVβ3 integrin). When morph targets were set between a rig and a PDB chain, the PDB chain was positioned manually to be near the rig i.e., the C-termini of the chains were aligned as close as possible. Elastic networks were made for protein domains and the strength adjusted, if necessary, to maintain the domain structures. Rig environmental dynamics were adjusted accordingly (e.g., turbulence field magnitude and damping) and simulations tested until the rig moved in a ‘smooth’ manner. Final rig simulations were cached, and receptor surface or backbone meshes extracted. Ligand binding events were added later by key-framing the motion of the meshes manually. In some of the MoA animations, the ligand binding event was omitted and only the resultant conformational change in the protein was shown.

### ECM asset creation

Collagen I is the most abundant structural component of the interstitial membrane. Protein fibrils of varying thicknesses (10 nm–1 μm) were sculpted to highlight striated 67 nm d-space repeats and arranged into bundles to represent fibres. A bespoke insert mesh zBrush tool was created to wrap the proteoglycan hyaluronic acid around collagen I structures (Figure 6B,E).

Similarly, an insert mesh zBrush tool was made for modelling Collagen IV protomers, which consisted of three intertwining α-chains that form a triple helix 400 nm in length. Two collagen IV protomers were joined head-to-head via NC1 dimers (PDB structure 1M3D) at the C-termini, and four collagen N-termini overlaid to form the 7S domain (28 nm overlaps), to create an extensive branched mesh network (Figure 6C,E).

Fibronectin monomers are made up of three repeating units (FN types I, II, III) and usually form dimers linked by a pair of disulphide bonds at their c-termini (Pankov and Yamada, 2002). Fibronectin dimers are long and can form fibrils (ranging from ~133–190 nm) (Früh et al., 2015). However, the precise molecular arrangement and their associations with multiple binding partners is still unclear. Alternative splicing can lead to over 20 protein variants in humans (Pankov and Yamada, 2002). Therefore, a simplified dimer mesh was modelled, which was shown only bound to integrin (Figure 6D,E).

### Cancer cells, cancer-associated fibroblasts and blood vessel

Tumour microenvironment components: additional neighbouring cancer cells (~10 μm diameter), cancer-associated fibroblasts (~20 μm length) and a leaky blood vessel (~10 μm diameter) with red blood cells (~6–8 μm diameter) were modelled in zBrush based on various microscopy images taken from the literature (See Figure 7). The blood flow in the vessel was animated in Maya (Video 2).
