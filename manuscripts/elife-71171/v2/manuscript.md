# Differential adhesion regulates neurite placement via a retrograde zippering mechanism

## Authors

- Titas Sengupta<sup>1</sup> ([ORCID: 0000-0002-7228-719X](https://orcid.org/0000-0002-7228-719X))
- Noelle L Koonce<sup>1</sup>
- Nabor Vázquez-Martínez<sup>1</sup>
- Mark W Moyle<sup>1</sup>
- Leighton H Duncan<sup>1</sup>
- Sarah E Emerson<sup>1</sup>
- Xiaofei Han<sup>2</sup>
- Lin Shao<sup>1</sup>
- Yicong Wu<sup>2</sup>
- Anthony Santella<sup>3</sup>
- Li Fan<sup>3</sup>
- Zhirong Bao<sup>3</sup> ([ORCID: 0000-0002-2201-2745](https://orcid.org/0000-0002-2201-2745))
- William A Mohler<sup>4</sup>
- Hari Shroff<sup>2</sup>
- Daniel A Colón-Ramos<sup>1</sup> ([ORCID: 0000-0003-0223-7717](https://orcid.org/0000-0003-0223-7717)) †

### Affiliations

1. Department of Neuroscience and Department of Cell Biology, Yale University School of Medicine New Haven United States ([ROR:03v76x132](https://ror.org/03v76x132))
2. Laboratory of High Resolution Optical Imaging, National Institute of Biomedical Imaging and Bioengineering, National Institutes of Health Bethesda United States ([ROR:00372qc85](https://ror.org/00372qc85))
3. Developmental Biology Program, Sloan Kettering Institute New Haven United States ([ROR:02yrq0923](https://ror.org/02yrq0923))
4. Department of Genetics and Genome Sciences and Center for Cell Analysis and Modeling, University of Connecticut Health Center Farmington United States ([ROR:02kzs4y22](https://ror.org/02kzs4y22))
5. MBL Fellows, Marine Biological Laboratory Woods Hole United States ([ROR:046dg4z72](https://ror.org/046dg4z72))
6. Wu Tsai Institute, Yale University New Haven United States ([ROR:03v76x132](https://ror.org/03v76x132))
7. Instituto de Neurobiología, Recinto de Ciencias Médicas, Universidad de Puerto Rico San Juan Puerto Rico

† Corresponding author

## Abstract

During development, neurites and synapses segregate into specific neighborhoods or layers within nerve bundles. The developmental programs guiding placement of neurites in specific layers, and hence their incorporation into specific circuits, are not well understood. We implement novel imaging methods and quantitative models to document the embryonic development of the C. elegans brain neuropil, and discover that differential adhesion mechanisms control precise placement of single neurites onto specific layers. Differential adhesion is orchestrated via developmentally regulated expression of the IgCAM SYG-1, and its partner ligand SYG-2. Changes in SYG-1 expression across neuropil layers result in changes in adhesive forces, which sort SYG-2-expressing neurons. Sorting to layers occurs, not via outgrowth from the neurite tip, but via an alternate mechanism of retrograde zippering, involving interactions between neurite shafts. Our study indicates that biophysical principles from differential adhesion govern neurite placement and synaptic specificity in vivo in developing neuropil bundles.

## Introduction

In brains, neuronal processes or neurites are segregated away from cell bodies into synapse-rich regions termed neuropils: dense structures of nerve cell extensions which commingle to form functional circuits (Maynard, 1962). In both vertebrates and invertebrates, placement of neurites into specific neighborhoods results in a laminar organization of the neuropil (Kolodkin and Hiesinger, 2017; Millard and Pecot, 2018; Nevin et al., 2008; Sanes and Zipursky, 2010; Schurmann, 2016; Soiza-Reilly and Commons, 2014; Xu, 2020; Zheng et al., 2018). The laminar organization segregates specific information streams within co-located circuits and is a major determinant of synaptic specificity and circuit connectivity (Baier, 2013; Gabriel et al., 2012; Missaire and Hindges, 2015; Moyle et al., 2021; Nguyen-Ba-Charvet and Chédotal, 2014; White et al., 1986; Xie et al., 2017). The developmental programs guiding placement of neurites along specific layers, and therefore circuit architecture within neuropils, are not well understood.

The precise placement of neurites within layered structures cannot be exclusively explained by canonical tip-directed outgrowth dynamics seen during developmental axon guidance (Tessier-Lavigne and Goodman, 1996). Instead, ordered placement of neurites resulting in layered patterns appears to occur via local cell-cell recognition events. These local cell-cell recognition events are modulated by the regulated expression of specific cell adhesion molecules (CAMs) that place neurites, and synapses, within nerve bundles (Aurelio et al., 2003; Kim and Emmons, 2017; Lin et al., 1994; Petrovic and Hummel, 2008; Poskanzer et al., 2003; Schwabe et al., 2019). For example, studies in both the mouse and fly visual systems have revealed important roles for the regulated spatio-temporal expression of IgSF proteins, such as Sidekick, Dscam and Contactin, in targeting synaptic partner neurons to distinct layers or sublayers (Duan et al., 2014; Sanes and Zipursky, 2010; Tan et al., 2015; Yamagata and Sanes, 2008; Yamagata and Sanes, 2012). In C. elegans nerve bundles, neurite position is established and maintained via combinatorial, cell-specific expression of CAMs which mediate local neurite interactions and, when altered, lead to defects in neurite order within bundles (Kim and Emmons, 2017; Yip and Heiman, 2018). How these local, CAM-mediated interactions are regulated during development and how they result in the segregation of neurites into distinct layers, are not well understood.

Differential expression of cell adhesion molecules (CAMs) in undifferentiated cells from early embryos can drive their compartmentalization (Foty and Steinberg, 2005; Foty and Steinberg, 2013; Steinberg, 1962; Steinberg, 1963; Steinberg, 1970; Steinberg and Takeichi, 1994). This compartmentalization is in part regulated by biophysical principles of cell adhesion and surface tension which can give rise to tissue-level patterns and boundaries (Canty et al., 2017; Duguay et al., 2003; Erzberger et al., 2020; Foty et al., 1996; Schötz et al., 2008). Morphogenic developmental processes such as the patterning of the Drosophila germline and retina, the germ layer organization in zebrafish, and the sorting of motor neuron cell bodies into discrete nuclei in the ventral spinal cord can be largely explained via differential adhesion mechanisms and cortical contraction forces that contribute to cell sorting (Bao and Cagan, 2005; Bao et al., 2010; Godt and Tepass, 1998; González-Reyes and St Johnston, 1998; Krieg et al., 2008; Price et al., 2002; Schötz et al., 2008). While differential adhesion is best understood in the context of the sorting of cell bodies in early embryogenesis, recent neurodevelopmental work supports that this mechanism influences sorting of neuronal processes in vivo as well. For example, differential expression of N-cadherin in the Drosophila visual system underlies the organization of synaptic-partnered neurites (Schwabe et al., 2019), where changes in the relative levels of N-cadherin are sufficient to determine placement of neurites within nerve bundles. Whether differential adhesion acts as an organizational principle within layered neuropils and how it regulates precise placement of neurites is not known.

Here, we examine the developmental events that lead to placement of the AIB interneurons in the C. elegans nerve ring. The C. elegans nerve ring is a layered neuropil, with specific layers or strata functionally segregating sensory information and motor outputs (Brittin et al., 2021; Moyle et al., 2021; White et al., 1986). A highly interconnected group of neurons referred to as the ‘rich club’ neurons, and which include interneuron AIB, functionally link distinct strata via precise placement of their neurites (Moyle et al., 2021; Sabrin, 2019; Towlson et al., 2013). Each AIB interneuron projects a single neurite, but segments of that single neurite are placed along distinct and specific layers in the C. elegans nerve ring (Figure 1). The sequence of events resulting in the precise placement of AIB along defined nerve ring layers is unexplored, primarily owing to limitations in visualizing these events in vivo during embryonic stages.

![Figure 1.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig1-v2.jpg)

**Figure 1.:** (A) Schematic of an adult/larval C. elegans showing an AIB neuron (cyan) and its posterior (orange) and anterior (magenta) neighborhoods in the head. The AIB neurite has a proximal neurite segment (orange arrow), a posterior-anterior shift at the dorsal midline (dashed line) and a distal neurite segment (magenta arrow; on the other side of the worm, behind the pharynx, which is in gray). The neon-colored outline represents the nerve ring neuropil. The terms ‘proximal’ or ‘distal’ neurite segments refer to the relationship of the neurite segment to the AIB cell body. The neighborhoods in which the ‘proximal’ and ‘distal’ neurite segments are positioned are referred to as the ‘posterior’ or ‘anterior’ neighborhoods, respectively, because of their position along the anterior-posterior axis of the worm. Note that this schematic only shows one neuron of the AIB pair. Cell body is marked with an asterisk. (B) Magnified schematic of AIB and its neighborhoods in (A, C) Representative confocal image showing the lateral view of an AIB neuron labeled with cytoplasmic mCherry (cyan). (D) Representative confocal image showing an AIB neuron labeled with cytoplasmic mCherry (cyan); and RIM motor neuron of the anterior neighborhood labeled with cytoplasmic GFP (magenta) in lateral view. Note the colocalization of the AIB distal neurite (but not the proximal neurite) with the anterior neighborhood marker RIM (compare with E). (E) As (D), but with AIB (cyan) and AWC and ASE sensory neurons of the posterior neighborhood (orange). Note the colocalization of the AIB proximal neurite (but not the distal neurite) with the posterior neighborhood markers AWC and ASE (compare with D). (F–J) Same as A–E but in axial view indicated by the arrow in (F). The worm head is tilted in this view to make the two neurite segments in the two neighborhoods visible. Note shift in H (arrows), corresponding to AIB neurite shifting neighborhoods (compare I and J). (K,L) Volumetric reconstruction from the JSH electron microscopy connectome dataset (White et al., 1986) of AIBL (K), and AIBL overlaid on nerve ring strata (L), in lateral view, with S2 and S3 strata (named as in Moyle et al., 2021), containing anterior and posterior neighborhoods, respectively. (M) Volumetric reconstruction of AIBL and AIBR in axial view (from the JSH dataset White et al., 1986). Note the shift in neighborhoods by AIBL and AIBR, at the dorsal midline (dashed line), forms a chiasm (also see Figure 1—figure supplement 1). (N) Schematic of M highlighting the AIB neighborhoods for context and the dorsal midline with a dashed line (AIB neighborhoods, synaptic polarity and resulting network properties also shown in Figure 1—figure supplement 2). Scale bar = 10 μm for A–J and 3 μm for K–N.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A-C) Pseudo-colored confocal maximum intensity projections showing AIBL (A), AIBR (B) and merge (C). Orange and magenta arrows indicate positions of the proximal and distal neurites, positioned in the posterior and anterior neighborhoods, respectively (see Figure 1). Note that the proximal and distal neurites of AIBL and AIBR completely overlap in the lateral view, consistent with what would be expected based on their positions and projections from the EM reconstructions (in D–I; White et al., 1986). Scale bar = 10 μm applies A-C. (D-F) EM and in vivo fluorescent microscopy views of the AIBL-AIBR neuron pair. (D) Schematic of the AIBL-AIBR neuron pair in the context of the nerve ring (light neon); (E) Pseudo-colored confocal maximum intensity projections of AIBL (cyan) and AIBR (yellow) (3D projection of this dataset shown in Figure 1—video 4); (F) Volumetric reconstructions of AIBL and AIBR from segmented EM datasets (JSH, White et al., 1986). (G–I) As D–F, but axial view. In all images (D–I), arrowheads indicate the posterior-anterior shift of the two neurons crossing each other to form a chiasm. The gray circle in G depicts the pharynx. Scale bars = 10 μm in E,H, and 3 μm in F,I.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Volumetric reconstruction of AIBL (cyan), a posterior neighborhood neuron (ASEL, orange) and an anterior neighborhood neuron (RIMR, magenta) from an L1 (5 hr post hatching) and an adult connectome dataset (45 hr post hatching, Witvliet et al., 2021). Scale bars = 3 μm. Note that ASEL contacts AIBL exclusively in the posterior neighborhood, and RIMR contacts AIBL exclusively in the anterior neighborhood. AIB is similarly positioned into the same neighborhoods in all available connectome datasets examined (which span all larval developmental stages; data not shown; White et al., 1986; Witvliet et al., 2021). The observation that AIB is already positioned in the two neighborhoods in the L1 stage indicates that AIB placement occurs during embryogenesis. (B,C) Axial view of the AIB neurite and neuron-neuron contact areas between AIBL and anterior neighborhood neuron, RIMR (B) and AIBL and posterior neighborhood neuron, ASEL (C) from the segmented EM dataset of the L4 stage animal JSH (Brittin et al., 2018; White et al., 1986). Contacts are colored red (see Methods) and overlaid on 3D volumetric reconstructions of the AIB neurite (cyan). Orange and magenta arrows indicate the posterior and anterior neighborhoods respectively. Scale bar = 3 μm, applies to B,C. (D) Volumetric reconstruction of AIBR from the JSH electron microscopy connectome dataset (White et al., 1986) in lateral view. Postsynaptic (red) and presynaptic (yellow) regions of the neurite, based on synaptic connectivity maps of AIBR, are indicated. Note that the postsynaptic and presynaptic regions coincide with the proximal and distal segment of AIB. Arrowhead points to the chiasm. Scale bar = 1 μm. (E–G) Representative confocal image showing a lateral view of an AIB neuron with postsynaptic sites (red, labeled by GLR-1:GFP, E) and presynaptic sites (yellow, labeled by mCh:RAB-3, F). (G) is a merge of E and F. Note the opposite polarity in the posterior and anterior neighborhoods (indicated by the orange and magenta arrows respectively) Scale bar = 10 μm, applies to E-G. (H) From the available segmented serial section EM and neuron-neuron contact data (Brittin et al., 2021; Moyle et al., 2021; White et al., 1986; Witvliet et al., 2021), neuron-neuron adjacency matrices were generated as depicted in the schematic. (I) Cosine similarity plot for AIBR. The cosine similarity values (Han et al., 2012) of AIB contacts between each pair of connectome datasets (White et al., 1986; Witvliet et al., 2021) are plotted as a heat map with the color bar indicating the values corresponding to the shades. The similarity values are >0.5 for all pairs of connectome datasets, indicating positive correlation between distribution of AIB contacts in different datasets. This suggests that distribution of AIB contacts with other neurons is largely established in early larval stages (L1) and maintained through development. The labels assigned to the connectome datasets comprise of the developmental stage and name of the animal sectioned (all times are measured post hatching) (White et al., 1986; Witvliet et al., 2021). (J) Box plot (10–90 percentile) of betweenness centrality values for an L1 (5 hr post hatching) connectome dataset and an adult connectome dataset (45 hr post hatching, Witvliet et al., 2021). The gray dots represent neurons whose centrality values lie above the 90-percentile mark or below the 10-percentile mark. The betweenness centrality values (see Methods) for AIBL and AIBR (indicated by cyan and yellow stars respectively) lie above the 90-percentile mark in both datasets. High betweenness centrality being a standard property of rich-club neurons (Towlson et al., 2013), this indicates that contacts of AIBL and AIBR exhibit rich-club features from early developmental stages (L1) to adulthood.

We implemented novel imaging methods and deep-learning approaches to yield high-resolution images of AIB during embryonic development. We discovered that placement of the AIB neurite depends on coordinated retrograde zippering mechanisms that align segments of the AIB neurite onto specific neuropil layers and is distinct from canonical tip-directed mechanisms of neurite placement. Quantitative analysis and modeling of our in vivo imaging data revealed that biophysical principles of differential adhesion influence the observed retrograde zippering mechanism that results in the sorting of the AIB neurite shaft onto distinct neuropil strata. We performed genetic screens to identify the molecular mechanisms underpinning these differential adhesion mechanisms, discovering a role for the IgCAM receptor syg-1 and its ligand, syg-2. We determined that syg-2 acts in AIB to instruct neurite placement across strata, while syg-1 is required non-cell autonomously, and at specific layers. Temporally regulated expression of SYG-1 alters adhesive forces during development to sort segments of AIB onto specific layers. Ectopic expression of SYG-1 predictably affects differential adhesion across layers, repositioning the AIB neurite segments in a SYG-2-dependent manner. Our findings indicate that conserved principles of differential adhesion drive placement of neurites, and en passant synaptic specificity, in layered neuropils.

## Results

### Examination of AIB neurite architecture in the context of the nerve ring strata

First, we characterized the precise placement and synaptic distribution of the AIB neurite within the nerve ring neuropil strata. From electron microscopy connectome datasets and in vivo imaging, we observed that the AIB neurite is unipolar, with its single neurite placed along two distinct and specific strata of the nerve ring (Figure 1, Figure 1—videos 1–3).

Connectomic studies have identified AIB as a ‘rich club’ neuron, a connector hub that links nodes in different functional modules of the brain (Sabrin, 2019; Towlson et al., 2013). We observed that AIB’s role as a connector hub was reflected in its architecture within the context of the layered nerve ring (Figure 1K–N, Figure 1—figure supplement 1, Figure 1—figure supplement 2). For example, the AIB neurite segment in the posterior neighborhood is enriched in postsynaptic specializations, enabling it to receive sensory information from the adjacent sensory neurons that reside in that neighborhood (Figure 1—figure supplement 2; White et al., 1983; White et al., 1986). AIB relays this sensory information onto the anterior neighborhood, where the AIB neurite elaborates presynaptic specializations that innervate neighboring motor interneurons (Figure 1D, E1 and J; Figure 1—figure supplement 2A-G, Figure 1—video 5). The architecture of AIB is reminiscent of that of amacrine cells of the inner plexiform layer (Demb and Singer, 2012; Kolb, 1995; Kunzevitzky et al., 2013; Robles et al., 2013; Strettoi et al., 1992; Taylor and Smith, 2012), which serve as hubs by distributing their neurites and synapses across distinct and specific sublaminae of the vertebrate retina (Marc et al., 2014). We set out to examine how this architecture was laid out during development.

### A retrograde zippering mechanism positions the AIB neurites in the anterior neighborhood during embryonic development

Prior to this study, using characterized cell-specific promoters, AIB could be visualized in larvae (Altun and Chen, 2008; Kuramochi and Doi, 2018) but not in embryos, when placement of AIB into the neighborhoods is specified (Figure 1—figure supplement 2A shows that by earliest postembryonic stage, L1, AIB neurite placement is complete, indicating placement occurs in the embryo). Moreover, continuous imaging of neurodevelopmental events in embryos, necessary for documenting AIB development, presents unique challenges regarding phototoxicity, speeds of image acquisition as it relates to embryonic movement, and the spatial resolution necessary to discern multiple closely spaced neurites in the embryonic nerve ring (Wu et al., 2011). These barriers prevented documentation of AIB neurodevelopmental dynamics. To address these challenges, we first adapted a subtractive labeling strategy for sparse labeling and tracking of the AIB neurites in embryos (detailed in Materials and methods, Figure 2—figure supplement 2,Figure 2—video 1, Armenti et al., 2014). We then adapted use of novel imaging methods, including dual-view light-sheet microscopy (diSPIM) (Kumar et al., 2014; Wu et al., 2013) for long-term isotropic imaging, and a triple-view line-scanning confocal imaging and deep-learning framework for enhanced resolution (Figure 2—figure supplement 2D,E; Weigert et al., 2018; Wu et al., 2016; Wu et al., 2021).

Using these methods, we observed that the AIB neurites enter the nerve ring during the early embryonic elongation phase, ~ 400 min post fertilization (m.p.f). The two AIB neurites then circumnavigate the nerve ring at opposite sides of the neuropil - both AIBL and AIBR project dorsally along the posterior neighborhood, on the left and right-hand sides of the worm, respectively (Figure 2A and B). Simultaneous outgrowth of AIBL and AIBR neurons in the posterior neighborhood results in their neurites circumnavigating the ring and meeting at the dorsal midline of the nerve ring (Figure 2C). Therefore, proper placement of the proximal segment of the AIB neurite in the posterior neighborhood occurs by AIB outgrowth along neurons in this neighborhood (Figure 2A–F).

![Figure 2.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig2-v2.jpg)

**Figure 2.:** A, Schematic of axial view of the AIB neuron pair: AIBL (cyan) and AIBR (yellow) in the context of the nerve ring (light neon) and the pharynx (grey), with posterior neighborhood labeled (orange) and the dashed line representing the dorsal midline where the AIB chiasm is present in adults (see Figure 1). Dotted box represents region in B’-F’, and dotted box in G. B,F, Time-lapse showing initial placement of AIBL and AIBR in the posterior neighborhood and their subsequent separation from this neighborhood. Images are deconvolved diSPIM maximum intensity projections obtained from developing embryos. Neurons were individually pseudocolored to distinguish them (see Methods). The dorsal half of the nerve ring (dotted box in A) are magnified in B’-F’. B’’-F’’ are schematic diagrams representing the images in B-F. Dashed vertical lines midline. Note in (B, B’, B’’), the AIBL and AIBR neurites approaching the dorsal midlinerepresent the dorsal in the posterior neighborhood. In (C, C’, C’’), AIBL and AIBR have met at the dorsal midline and continue growing along each other, past the midline. The latter part of the neurite, past the midline, becomes the future distal neurite. (D, D’, D’’) shows the tip of the AIBL future distal neurite moving away from the posterior neighborhood and its counterpart, AIBR. The arrowhead indicates the point of separation of the AIBL distal neurite and the AIBR proximal neurite. (E, E’, E’’) shows further separation of the two neurites and by (F, F’, F”), they have completely separated. The arrowheads in (E, E’, E’’) and (F, F’, F’’) also indicate the junction between the separating AIBL distal neurite and the AIBR proximal neurite. A similar sequence of events is visualized at higher spatial resolution in Figure 2—figure supplement 1 using triple-view line scanning confocal microscopy (Figure 2—figure supplement 1). G, G’, Confocal micrograph of a postembryonic L4 animal (axial view) showing the relationship between AIBL and AIBR. The region in the box represents the dorsal part of the nerve ring, magnified in G’. H, Axial view schematic of one AIB neuron (cyan) in the context of the anterior neighborhood marker, the RIM neuron (magenta), the nerve ring (light neon) and the pharynx (grey). I-K, Time-lapse showing placement of the AIB neurite (cyan) relative to the anterior neighborhood (magenta). As in B-F, images are deconvolved diSPIM maximum intensity projections and the neurons were pseudocolored. The dorsal half of the nerve ring (dotted box in H) are magnified in I’-K’. Dashed line indicates dorsal midline (where the shift, or chiasm, in the adult is positioned, see Figure 1). I’’-K’’ are schematic diagrams representing the images in I-K. Note in (I, I’, I”), the tip of the AIB neurite encounters the RIM neurite in the anterior neighborhood (green arrowhead). In (J, J’, J’’), the AIB distal neurite has partially aligned along the RIM neurites. The green arrowhead now indicates point of initial encounter of the two neurites (same as in I’), and the red arrowhead indicates the retrograde zippering event bringing the AIB and RIM neurons together in the anterior neighborhood. In (K, K’, K”) the two neurites have zippered up to the dorsal midline. Arrow in J’ indicates direction of zippering. L, Confocal micrograph of a postembryonic L4 animal in axial view showing the final position of AIB with respect to the anterior neighborhood. The same image as Figure 1I was used here for reference. The region in the dotted box represents dorsal part of the nerve ring, magnified in (L’). M, Schematic highlights the steps by which the AIB distal neurite is repositioned to a new neighborhood – (i) exit from the posterior neighborhood and (ii) retrograde zippering onto the anterior neighborhood with intermediate partially zippered states and completely zippered states. Scale bar = 10 µm for B-G and I-L. Scale bar = 2 µm for B’-G’ and I’-L’ Times are in m.p.f. (minutes post fertilization).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A-E) diSPIM maximum intensity projections of AIBL and AIBR showing unzippering. The corresponding pseudocolored images (A’-E’) have been used in Figure 2B–F.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A), Schematic of the ZIF-1/1-ZF1 degradation system used for subtractive fluorescent labeling of specific neurons in embryos (Armenti et al., 2014), also see Materials and methods. Briefly we used lim-4p, expressed in sublateral neurons (Santella et al., 2015) to express ZIF-1 and unc-42p, expressed in the sublateral neurons + AIB + ASH (http://promoters.wormguides.org) to express ZF1-tagged PH:GFP. This results in degradation of PH:GFP from the sublateral neurons, resulting in cell-specific labeling of AIB and/or the ASH neurons. (B) diSPIM image showing unc-42p-driven membrane-tethered PH:GFP expression, without ZIF-1/ZF1 mediated degradation, in neurons of the embryonic nerve ring. Distinction of AIB neurite outgrowth dynamics is not possible in this background due to abundant labeling. Scale bar = 10 μm applies to B,C. (C) diSPIM image showing the nerve ring of an embryo expressing the ZIF-1/ZF1 degradation construct strategy outlined in A. The identity of AIB was confirmed by colocalization and lineaging as described (Moyle et al., 2021). (D,E) Imaging methods that we established and implemented for the investigation of neurodevelopmental events in C. elegans embryos. (D) A triple-view line-scanning confocal microscope that provides enhanced (twofold) axial resolution compared to conventional confocal microscopy (Wu et al., 2021). To image AIB in living nematode embryos, we additionally created a two-step deep learning framework that denoises the raw data, enabling us to turn down the illumination intensity ~30 fold, offering more gentle imaging than conventional confocal microscopy. (E) Dual-view inverted selective plane illumination microscopy (diSPIM), a light-sheet microscopy technique for long-term imaging of AIB neurite development (Kumar et al., 2014; Wu et al., 2013). Deconvolution and fusion of images from orthogonal views result in isotropic spatial resolution. ( F–H), Time-lapse showing relative positions of AIBL (pseudo-colored in cyan) and AIBR (pseudocolored in yellow) in the embryonic nerve ring. Images are reconstructions derived from triple-view line-scanning confocal microscopy, which used a deep learning algorithm for denoising and deconvolving all three views. The dashed white lines represent the dorsal midline of the nerve ring. The dotted boxes represent the dorsal half of the nerve ring and are magnified in F’-H’. F’’-H’’ are schematic diagrams representing the images in (F–H). In (F,F’F’’), the neurites are initially positioned in the same neighborhood. In (G,G’,G’’) they have separated partially from the tip up to a point along their lengths (arrow). In (H,H’,H’’) they have separated completely up to the dorsal midline (arrowhead). The high spatial resolution allows us to clearly distinguish the two neurites and determine their relative positions reliably, confirming results in Figure 2 and enabling detailed quantifications. Scale bar = 2 μm in F, applies to G,H, and 1 μm in F’, applies to G’,H’. (I) Schematic showing AIBL and AIBR in the context of the nerve ring (light neon), pharynx (gray) and the anterior and posterior neighborhood (magenta and orange regions). AIBL exits the posterior neighborhood (direction of outgrowth indicated by black arrow) and cuts through the nerve ring to meet the anterior neighborhood. α is the angle of exit. AIBR also exits similarly. We also measured β: the angle between tangents drawn at the point of downward bend of the nerve ring in the posterior neighborhood, as indicated in schematic (from embryos in which posterior neighborhood neurons are labeled by nphp-4p:PH:GFP). (J) Scatter plot of α and β values (n = 6, 3 AIBL and 3 AIBR neurons measured from three embryos for each of α and β). Unpaired two-tailed t test indicates no significant difference (n.s.) between α and β values (P = 0.1368). The AIB distal neurite therefore exits tangentially from the posterior neighborhood, consistent with AIB losing adhesion in this neighborhood, growing straight instead of following the arc of the nerve ring and crossing the nerve ring toward its eventual encounter with the RIM neuron in the anterior neighborhood.

After meeting at the dorsal midline, instead of making a shift to the anterior neighborhood (as expected from the adult AIB neurite morphology – see Figure 1M and N), the AIB neurites, surprisingly, continue growing along the posterior neighborhood (Figure 2C and D; 480 m.p.f.). At approximately 505 m.p.f., each AIB neurite separates from the posterior neighborhood, starting at its growth cone, by growing tangentially to the posterior neighborhood (the posterior neighborhood is marked in Figure 2A–G by its lateral counterpart, that is, the other AIB, also see Figure 2—figure supplement 2I,J). The departure of the AIB growth cone occurs due to the AIB neurite growing in a straight path trajectory instead of following the bending nerve ring arc (Figure 2—figure supplement 2I,J). Because it has been documented that axons tend to ‘grow straight’ on surfaces lacking adhesive forces that instruct turning (Katz, 1985), we hypothesize that the observed exit (via ‘straight outgrowth’) could result from decreased adhesion to the posterior neighborhood (Figure 2—figure supplement 2I,J).

As it grows tangentially to the posterior neighborhood, the AIB neurite cuts orthogonally through the nerve ring and toward the anterior neighborhood (Figure 2—figure supplement 2I,J). Upon intersecting the anterior neighborhood, the AIB neurite reengages with the arc of the nerve ring. At this developmental stage (Figure 2I), only 3.9 % of the AIB distal neurite is placed in the anterior neighborhood, with the remainder still being positioned in the posterior neighborhood and between neighborhoods. Following this, we observed a repositioning of the AIB neurite, but not via expected tip-directed fasciculation. Instead, the entire shaft of the distal AIB neurite was peeled away from the posterior neighborhood and repositioned onto the anterior neighborhood, starting from the tip of the neurite and progressively ‘zippering’ in a retrograde fashion towards the cell body (Figure 2J and K; the overlap of the AIB neurite with the anterior neighborhood increased from 3.9 % at 515 m.p.f. to 30.4 % at 530 m.p.f. and 71.7 % at 545 m.p.f.). Retrograde zippering stopped at the dorsal midline of the nerve ring (~545 m.p.f.), resulting in the AIB architecture observed in postembryonic larval and adult stages (Figure 2L). The progressive zippering of the AIB neurite onto the anterior neighborhood occurs concurrently with its separation from the posterior neighborhood (Figure 2M), a converse process which we refer to as ‘unzippering’. The in vivo developmental dynamics of AIB repositioning, via retrograde zippering onto the anterior neighborhood, are reminiscent of dynamics observed in cultures of vertebrate neurons in which biophysical forces drive ‘zippering’ of neurite shafts, and the bundling of neurons (Smít et al., 2017). This mechanism is distinct from neurite bundling directed by anterograde migration of neurite tips (Bak and Fraser, 2003), and retrograde zippering, until this study, had not been documented during development and in vivo.

### Biophysical modeling of AIB developmental dynamics is consistent with differential adhesion leading to retrograde zippering

Dynamics of neurite shaft zippering have been previously documented (Barry et al., 2010; Voyiadjis et al., 2011), modeled in tissue culture cells (Smít et al., 2017), and described as resulting from two main forces: neurite-neurite adhesion (represented as ‘S’) and mechanical tension (represented as ‘T’). To better understand the mechanisms that act in vivo during AIB neurite placement, we analyzed AIB developmental dynamics in the context of these known forces that affect neurite zippering. In each neighborhood, the developing AIB neurite experiences two forces: (i) adhesion to neurons in that neighborhood and (ii) tension due to mechanical stretch. As the neurite zippers and unzippers, it has a velocity in the anterior neighborhood (a zippering velocity, $v_{zip}$) and a velocity in the posterior neighborhood (an unzippering velocity, $v_{unzip}$) (Figure 3, Appendix 1 and Appendix 1—figure 1). These velocities are related to the forces on the neurite by the following equation:

$$
v_{zip}+v_{unzip}=\frac{(S_{anterior}−S_{posterior})}{η}−\frac{ΔT}{η}(1−cos\theta)
$$

![Figure 3.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig3-v2.jpg)

**Figure 3.:** (A) Axial view schematic of a single AIB neuron during transition of its neurite between the posterior (orange) and anterior (magenta) neighborhoods. (B,B’) Magnified schematic of dotted inset in (A) showing the AIB neurite (cyan) during its transition from the posterior to the anterior neighborhood. The lengths of the neurite positioned in the posterior and anterior neighborhoods are denoted by Lp and La, respectively. The velocity with which the AIB neurite zippers onto the anterior neighborhood is denoted by $v_{zip}$ , and the velocity with which it unzippers from the posterior neighborhood is denoted by $v_{unzip}$ . At the junction between the neurite and the two neighborhoods, that is at the zippering and unzippering forks, tension and adhesion forces act on the neurite (see B’, Appendix 1 and Appendix 1—figure 1). B', Schematic of AIB neurite zippering to the anterior neighborhood. Adhesion Santerior acts in the direction of zippering (and therefore in the direction of the zippering velocity $v_{zip}$) and favors zippering. Tension Tanterior acts in the opposite direction, disfavoring zippering. (C) Plot of position vs. time of the AIB neurite in both neighborhoods in synchronized embryos at the indicated timepoints on the x-axis ( ± 5 mins). Plot shows mean of Lp (n = 4) and La (n = 3) values at different timepoints. Note zippering from the anterior neighborhood and unzippering from the posterior neighborhood take place in the same time window and are inversely related (between 500–545 m.p.f.). Quantifications were done from three embryos for each of La and Lp. See Figure 3—figure supplement 1 for the individual Lp and La values at each timepoint. (D) Plot of zippering velocities vs time (n = 3) for the indicated timepoints on the x-axis ( ± 5 mins). Note a tenfold increase in velocity mid-way through zippering (530 m.p.f.) m.p.f. = minutes post fertilization. Error bars represent standard error of the mean (S.E.M.), The three embryo datasets used for measuring La values in (C) were used to calculate zippering velocities. For C and D, n represents the number of AIB neurites quantified.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A,B) Plots showing individual measurements of Lp (A) and La (B) (see Methods for details). The Lp (A) and La (B) values at each timepoint were averaged to produce the orange and magenta curves (respectively) in the plot in Figure 3C. Each point represents a single AIB neurite. Lp was quantified from four different embryos and La from three different embryos.

where $v_{zip}$ = zippering velocity, $v_{unzip}$ = unzippering velocity, $S_{anterior}-S_{posterior}$ = difference between adhesive forces in the two neighborhoods, $T=T_{anterior}−T_{posterior}$ = difference between tension acting on the AIB neurite in the two neighborhoods, $η$ = friction constant (see Appendix 1 and Appendix 1—figure 1) and $\theta$ = angle of the AIB neurite to the neighborhoods (Figure 3, Appendix 1 and Appendix 1—figure 1). Since the above biophysical equation defines the relationship between velocities and forces, we measured the velocities of the neurite from our time-lapse images to make predictions about the forces on the neurite.

Time lapse images and measurements of the developmental dynamics showed that zippering and unzippering takes place concurrently: zippering on to the anterior neighborhood and unzippering from the posterior one (Figure 3C). Between 505 and 545 m.p.f., the average length of the AIB neurite that is placed in the anterior neighborhood (4.49 μm) by retrograde zippering is similar to the length that is unzippered from the posterior neighborhood (4.13 μm). Assuming, based on previous studies (Smít et al., 2017), that the tension forces are uniformly distributed along the neurite (and therefore $ΔT=T_{anterior}−T_{posterior}=0$) zippering and unzippering velocities arise from a difference in adhesion ($S_{anterior}−S_{posterior}>0$) (see Appendix 1 and Appendix 1—figure 1).

Measurements of in vivo zippering velocities (Figure 3D) support this hypothesis. Examination of our time-lapse images revealed that AIB neurite zippering onto the distal neighborhood takes place at higher velocities at later timepoints (with mean zippering velocity increasing from 0.09 μm/min at 515 min to 0.34 μm/min at 530 min) (Figure 3D). This increased velocity, or acceleration, is a hallmark of force imbalance and consistent with a net increase in adhesive forces in the anterior neighborhood during the period in which zippering takes place. We note that retrograde zippering comes to a stop precisely at the dorsal midline, likely owing to the adhesion and tension forces on the neurite in the two neighborhoods balancing out at this point.

Together, the developmental dynamics observed for AIB neurite placement are consistent with relative changes in adhesive forces between the neighborhoods. This suggests that dynamic mechanisms resulting in differential adhesion might govern AIB neurite repositioning by a process similar to affinity-based sorting of cells within homogenous tissues (Steinberg, 1963; Steinberg, 1970). We show that differential adhesion across nerve ring bundles result in neurite placement by a zipper-like mechanism (Barry et al., 2010; Roberts and Taylor, 1982; Voyiadjis et al., 2011), distinct from the classical paradigm of chemical attraction of the growing neurite tip to pre-existing nerve bundles or guidepost cells (Plachez and Richards, 2005; Sabry et al., 1991).

### SYG-1 and SYG-2 regulate precise placement of the AIB neurite to the anterior neighborhood

To identify the molecular mechanism underpinning differential adhesion for AIB neurodevelopment, we performed forward and reverse genetic screens (see Materials and methods). We discovered that loss-of-function mutant alleles of syg-1 and syg-2, which encode a pair of interacting Ig family cell adhesion molecules (IgCAMs), display significant defects in the placement of the AIB neurite. In wild type animals, we reproducibly observed complete overlap between the AIB distal neurite and neurons in the anterior neighborhood (Figure 4A–D), consistent with EM characterizations (Figure 1—figure supplement 2A,B). In contrast, 76.3 % of syg-1(ky652) animals and 60 % of syg-2(ky671) animals (compared to 1.8 % of wild-type animals) showed regions of AIB detachment from neurons specifically in the anterior neighborhood (Figure 4E–L; we note we did not detect defects in general morphology of the nerve ring, in the length of the AIB distal neurite, or in position of the AIB neurite in the posterior neighborhood for these mutants, Figure 4—figure supplement 1). In the syg-1(ky652) and syg-2(ky671) animals that exhibit defects in AIB neurite placement, we found that 20.9 ± 3.9 and 18.6% ± 4.0% (respectively) of the neurite segment in the anterior neighborhood is detached from the neighborhood (Figure 4M). Our findings indicate that SYG-1 and SYG-2 are required for correct placement of AIB, specifically to the anterior neighborhood.

![Figure 4.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig4-v2.jpg)

**Figure 4.:** (A-D) Representative confocal images of AIB (A) and RIM neurons (B) which mark the anterior neighborhood, in a wild-type animal. (C) is a merge of A and B. The dashed box represents the region of contact of AIB with the anterior neighborhood, magnified in (D). The AIB distal neurite colocalizes extensively with the anterior neighborhood in wild-type animals (Arrow in D and Figure 1—figure supplement 2A,B). Cell bodies are marked with an asterisk. (E–L) As A–D but in the syg-1(ky652) (E–H) and syg-2(ky671) (I–L) mutant background. Note the gaps between the AIB distal neurite and the RIM neurites (H,L, arrows), indicating loss of contact between the AIB and the anterior neighborhood in these mutants. (M) Schematic and scatter plot of quantifications of the loss of contacts between AIB and the anterior neighborhood for wild type (n = 42), syg-1(ky652) mutant (n = 40) and syg-2(ky671) animals (n = 49). ‘n’ represents the number of AIB neurites quantified from 21, 20 and 25 animals, respectively. The extent of detachment of the AIB distal neurite, and hence its deviation from the RIM neighborhood, was quantified using the indicated formula (see also Materials and methods). Error bars indicate standard error of the mean (S.E.M.). ****p < 0.0001, **p = 0.0095 (one-way ANOVA with Dunnett’s multiple comparisons test). n represents the number of AIB neurites quantified. Estimated effect size, d = 1.087 for WT vs. syg-1(ky652) and 0.775 for WT vs. syg-2(ky671). For neurites that do not show visible detachment, the precent detachment values = 0 and therefore these datapoints lie on the x-axis. The mean percent deviations include neurites with 0 percent detachment. (N) Quantification of the penetrance of the AIB neurite placement defect as the percentage of animals with normal AIB distal neurite placement in WT, syg-1(ky652), syg-2(ky671), syg-1(ky652);syg-2(ky671) double mutant, inx-1p:syg-2 rescue, inx-1p:syg-1 rescue and SYG-1 cosmid rescue (also see Figure 4—figure supplement 1G-I'). inx-1p is a cell-specific promoter driving expression in AIB (Altun and Chen, 2008). The green and purple bars represent syg-1(ky652) and syg-2(ky671) mutant backgrounds respectively. Numbers on bars represent number of animals examined. ****p < 0.0001 by two-sided Fisher’s exact test between WT and syg-1(ky652), between WT and syg-2(ky671), and between syg-1(ky652) and SYG-1 cosmid rescue, and **p = 0.0055 between syg-2(ky671) and inx-1p:syg-2 rescue. There is no significant difference (abbreviated by n.s.) in penetrance between the syg-1(ky652) and syg-1(ky652);syg-2(ky671) (p = 0.6000) populations and between syg-1(ky652) and the inx-1p:syg-1 animals (p = 0.3558). Scale bar = 10 μm, applies to (A–L).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Scatter plot of lengths of the dorsal midline shift (that form a chiasm for the neuron pair, see Figure 1 and Figure 1—figure supplement 1) for wild type (n = 18) and syg-1 (ky652) (n = 18). Error bars indicate standard error of the mean (S.E.M.). ***p = 0.0008 (unpaired two-tailed t-test). In wildtype animals, the chiasm is stereotyped and similar in length across L4 stage animals, as measured from confocal micrographs and displayed in this scatter plot (mean length = 2.97 ± 0.05 μm, n = 18), and electron micrographs (dorsal midline shift length in AIBL and AIBR in electron micrographs of an L4 stage animal, JSH, are 3.01 μm and 3.16 μm, respectively). In syg-1(ky652), the mean length of the chiasm is significantly smaller and is = 1.96 ± 0.27 μm (n = 18). n represents the number of AIB neurons measured from nine wild type and nine syg-1(ky652) animals. Effect size estimate, d = 1.233. (B) Scatter plot of distal neurite lengths for wild type (n = 31) and syg-1(ky652) (n = 30). n represents the number of AIB neurons measured from 16 wild type and 15 syg-1(ky652) animals. (C) Scatter plot of nerve ring width as measured from strains expressing a nerve ring marker cnd-1p:PH:GFP (see Materials and methods), in WT (n = 14) and syg-1(ky652) (n = 14) backgrounds. Two values of nerve ring width were obtained from each animal (one from each side). n = number of animals of each genotype from which measurements were done. For B and C, unpaired two-tailed t test indicates no significant (abbreviated by n.s.) difference (p = 0.0793 and 0.3140, respectively). Error bars indicate standard error of the mean (S.E.M.). (D,E) Representative confocal images of a syg-1(ky652) (D) and a syg-2(ky671) (E) animal with AIB labeled with cytoplasmic mCherry (cyan) and the posterior neighborhood markers, the AWC and ASE neurons labeled with cytoplasmic GFP (orange). Note that the placement of the AIB neurite in the posterior neighborhood is unaffected in syg-1(ky652) and syg-2(ky671). The orange and magenta arrows indicate the positions of the posterior and anterior neighborhoods respectively. Scale bar = 10 μm. (F) Quantification of the minimum perpendicular distances between the AIB proximal and distal neurites in WT (n = 19), syg-1(ky652) (n = 29) and syg-2(ky671) (n = 18). ****p < 0.0001; ***p = 0.0007 (one-way ANOVA with Dunnett’s multiple comparisons test). ‘n’ represents the number of AIB neurons measured from 9, 15, and 9 animals from the WT, syg-1(ky652) and syg-2(ky671) populations, respectively. Effect size estimate, d = 2.239 for WT and syg-1(ky652) and 1.148 for WT and syg-2(ky671). G-I’ Representative confocal images of AIB (cyan) and the anterior neighborhood (magenta) in strains with cell-specific SYG-2 expression (G), cell-specific SYG-1 expression (H) and a cosmid containing syg-1 (recapitulating endogenous SYG-1 expression) (I). The dashed boxes in G, H and I represent the region of contact between AIB and the anterior neighborhood, magnified in G’, H’ and I’, respectively. Note complete alignment of the AIB distal neurite with the anterior neighborhood in G’ and I’ and detachment in H’. Scale bar = 10 μm for G,H,I, and 1 μm for G’,H’,I’.

The IgCAMs SYG-1 and SYG-2 are a receptor-ligand pair that has been best characterized in the context of regulation of synaptogenesis in the C. elegans egg-laying circuit (Shen and Bargmann, 2003; Shen et al., 2004). SYG-1 (Rst and Kirre in Drosophila and Kirrel1/2/3 in mammals) and SYG-2 (Sns and Hibris in Drosophila, and Nephrin in mammals) orthologs also act as multipurpose adhesion molecules in varying conserved developmental contexts (Bao and Cagan, 2005; Bao et al., 2010; Chao and Shen, 2008; Garg et al., 2007; Neumann-Haefelin et al., 2010; Ozkan et al., 2014; Oztokatli et al., 2012; Serizawa et al., 2006; Shen and Bargmann, 2003; Shen et al., 2004; Strünkelnberg et al., 2001). In most of the characterized in vivo contexts, SYG-1 has been shown to act heterophilically with SYG-2 (Dworak et al., 2001; Ozkan et al., 2014; Shen et al., 2004). Consistent with SYG-1 and SYG-2 acting jointly for precise placement of the AIB neurite in vivo, we observed that a double mutant of the syg-1(ky652) and syg-2 (ky671) loss-of-function alleles did not enhance the AIB distal neurite placement defects as compared to either single mutant (Figure 4N).

To determine the site of action of these two molecules, we expressed them cell-specifically in varying tissues. We observed that SYG-2 expression in AIB was sufficient to rescue the AIB distal neurite placement defects in the syg-2(ky671) mutants, suggesting that SYG-2 acts cell autonomously in AIB. While expression of wild-type SYG-1 (via a cosmid) rescued AIB neurite placement onto the anterior neighborhood, expression of SYG-1 using an AIB cell-specific promoter did not (Figure 4N), consistent with SYG-1 regulating AIB neurite placement cell non-autonomously.

### Increased local expression of SYG-1 in the anterior neighborhood coincides with zippering of the AIB neurite onto this neighborhood

To understand how SYG-1 coordinates placement of the AIB neurite, we examined the expression of transcriptional and translational reporters of SYG-1 in the nerve ring of wild type animals. In postembryonic, larva-stage animals (L3 and L4), we observed robust expression of the syg-1 transcriptional reporter in a banded pattern in ~20 neurons present in the AIB posterior and anterior neighborhoods, with specific enrichment in the anterior neighborhood (Figure 5A–E). The SYG-1 translational reporter, which allowed us to look at SYG-1 protein accumulation, also showed a similar expression pattern (Figure 5F–I). To understand how SYG-1 regulates placement of the AIB neurite during development, we examined spatiotemporal dynamics of expression of SYG-1 during embryogenesis at the time of AIB neurite placement (400–550 m.p.f.) (Figure 2), using both the transcriptional and translational syg-1 reporters.

![Figure 5.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig5-v2.jpg)

**Figure 5.:** (A-E) Schematic (A) and representative confocal image of a wild-type animal co-expressing (B) a membrane-targeted syg-1 transcriptional reporter (see Materials and methods, Schwarz et al., 2009) and (C) cytoplasmic AIB reporter. Merged image in (D). Since the syg-1 reporter is membrane-targeted, it labels cell body outlines and neurites (B, D). The dashed box or inset in (D) represents the region of overlap between AIB and syg-1-expressing neurites, magnified in (E). Note that the syg-1 reporter shows two bands of expression in the nerve ring (arrows in B and D) which coincide with the posterior and anterior AIB neighborhoods (orange and magenta arrows). Note also that there is no membrane outline corresponding to the AIB cell body (B) we drew a dashed silhouette of the AIB cell body position as determined in (C). Asterisk indicates cell body. (F–I) As B–E, but with a translational SYG-1 reporter. Note the SYG-1 protein shows a similar expression pattern. (J–N) Schematic (J) and time-lapse images (K–N) of SYG-1 translational reporter expression during embryogenesis (460–640 m.p.f.). Images are deconvolved diSPIM maximum intensity projections. The dashed boxes represent the dorsal half of the nerve ring and are magnified in O-R. O’-R’ are schematic diagrams representing the images in (O–R). In (K, O, O’), SYG-1 expression is primarily visible in a single band containing amphid neurites and corresponding to the AIB posterior neighborhood. The magenta dashed line and magenta arrows point to the anterior neighborhood and the orange arrow, to the posterior neighborhood. By 535 m.p.f. (L, P, P’), SYG-1 expression is visible in both the anterior and posterior neighborhoods. In subsequent timepoints (M, Q, Q’, N, R, R’), SYG-1 expression increases in the anterior neighborhood and decreases in the posterior neighborhood, coincident with AIB developmental events that enable its transition from the posterior to the anterior neighborhood (Figure 2B–K). The syg-1 transcriptional reporter shows a similar expression pattern throughout development (Figure 5—figure supplement 1). (S) Plot showing relative enrichment of the syg-1 transcriptional reporter in the anterior neighborhood over time (magenta) overlaid with plot showing percentage of the relocating AIB distal neurite that has zippered onto the anterior neighborhood (blue). Relative enrichment in the anterior neighborhood is defined as the ratio of mean intensity of the syg-1 reporter in the band corresponding to the AIB anterior neighborhood, as compared to that in the posterior neighborhood (see Materials and methods). This value is calculated starting at a timepoint when syg-1 reporter expression becomes visible in the anterior neighborhood and averaged for four embryos. The relative enrichment values plotted represent values calculated at the indicated developmental times on the x-axis ( ± 10 mins). The reported values of ‘% AIB zippered’ are averaged across the three independent embryo datasets used for the plots in Figure 3. Note similar SYG-1 expression dynamics to zippering dynamics in AIB. Error bars represent standard error of the mean (S.E.M.). See Figure 5—figure supplement 5 for the individual values of syg-1 anterior enrichment and ‘% AIB zippered’. Scale bar = 10 μm, applies to B–D, (F–H) and K–N. Scale bar = 2 μm in E, I and O–R. Times are in m.p.f. (minutes post fertilization).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A-D) Time-lapse images of syg-1 reporter expression during embryogenesis (450–630 m.p.f.). Images are deconvolved diSPIM maximum intensity projections. The dashed boxes represent the dorsal half of the nerve ring and are magnified in E-H. E’-H’ are schematic diagrams representing the images in E–H. In (A,E,E’), syg-1 expression is primarily visible in a single band containing amphid neurites, and therefore coincident with the AIB posterior neighborhood (indicated with orange arrow). The magenta dashed line and magenta arrows point to the anterior neighborhood. (B,F,F’) show onset of weak syg-1 expression in the anterior neighborhood (white arrow in F) and ingrowth of syg-1-expressing neurites into this neighborhood (white arrowhead, identified as RIM neurons by colocalization, see Figure 5—figure supplement 3). syg-1 expression increases in the anterior neighborhood and decreases in the posterior neighborhood as embryonic development progresses (C,G,G’,D,H,H’), quantified in Figure 5S and similar to the SYG-1 protein reporter (Figure 5J–R’). Scale bar = 10 μm in A–D. Scale bar = 1 μm in E–H. All times are in m.p.f. (minutes post fertilization).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A,B) Single z-slice of a diSPIM image of an embryo expressing a ubiquitous mCherry histone label (used for lineaging at 430 mpf and as described in Bao et al., 2006) and syg-1p (3.5 kb) driving GFP (A). (B) shows only the syg-1 channel. Scale bar = 10 μm, applies to A and B. (C) Identity of the SYG-1-labeled neurons in the anterior and posterior neighborhoods. Our lineaging analysis are consistent with embryonic transcriptomic dataset previously reported (Packer et al., 2019). Of note, neurons in the posterior neighborhood that exhibit syg-1 expression at the time window (430–550 m.p.f.) (ADLR, ADLL, ASHR, ASHL), coinciding with when lineaging was performed (430 m.p.f.), in the transcriptomic dataset (Packer et al., 2019) show a decrease in syg-1 expression levels at a later developmental window (550–690 m.p.f.), consistent with our observations in Figure 5 and Figure 5—figure supplement 3. The transcriptome analyses also reveal that certain neurons in the anterior neighborhood (e.g. RIB) exhibit a greater than two-fold increase (435.7–1007.8 estimated transcripts per million - Packer et al., 2019) in expression between the earlier (430–550 m.p.f.) and later (550–690 m.p.f.) developmental windows. Other anterior neighborhood neurons, such as RIM, show a decrease in expression levels in the transcriptomic reports (1536.3–1078.2 estimated transcripts per million), but contribute to an increase in SYG-1 in the anterior neighborhood by growing its neurite into the anterior neighborhood at these time windows. (D) EM reconstruction showing areas of contact between AIBL and all its neighboring neurons (blue), and AIBL and SYG-1 expressing neurons (yellow). These data were derived from segmentations of the JSH EM dataset (Brittin et al., 2021; White et al., 1986) (see Materials and methods for how these contact areas or ‘patches’ were created). Inset shows a rotated view to highlight all patches. Note that while SYG-1 is important for placement of the AIB interneuron, not all fasciculating partners of AIB express SYG-1 (we observe that 13 % of AIB fasciculating partners express SYG-1). (E) Similar to D but for AIBR. Scale bar = 2 μm, applies to D and E.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** (A) Schematic of the axial view of an embryo with the red box showing the region in the head containing the nerve ring. (B–D) Deconvolved diSPIM maximum intensity image of (B) membrane-targeted PH:GFP driven by the syg-1 promoter (as in Figure 5—figure supplement 1) and (C) RIM in an embryo. d is a merge of B and C. Note the colocalization of the RIM neurites (arrow) and the RIM cell body (arrowhead) in D with the syg-1 reporter in the anterior neighborhood. (E–I) Expression of the same syg-1 reporter as in B–D but in larval stage three in a lateral view (E). The syg-1 reporter (F) is co-expressed with a cytoplasmic RIM neuron marker (G). (H) is a merge of F and G. The dashed box represents the region of the nerve ring containing the RIM neuron and the syg-1-expressing neurons. Note the RIM neurite colocalizes with the anterior band of syg-1 expression, coincident with the AIB anterior neighborhood (magenta arrow). The white arrowhead in F–H and semi-transparent magenta outline in F indicates colocalization of the RIM cell body with the syg-1 reporter. Scale bar = 10 μm applies to B–I.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** (A) Schematic of the axial view of an embryo where the red box highlights the region in the head where nerve ring neurons are present, and cropped from images of whole embryos, to produce the images in B,C. B,C, diSPIM maximum intensity projections of fluorescently labeled RIM neurons (arrows) in embryos prior to AIB distal neurite placement (~500–550 m.p.f., minutes post fertilization), labeled with inx-19p:GFP (B) or tdc-1p:GFP (C). Scale bar = 10 μm applies to B,C. (D) Schematic showing strategies used for ablation of the RIM neurons in embryos. In strategy 1, a small (p12) and a large (p17) subunit of human Caspase-3 are both expressed by inx-19p, similar to previously described (Chelur and Chalfie, 2007). The inx-19p is expressed in the RIM neurons from 370 m.p.f – the time of their birth. In strategy 2, p12 is expressed by inx-19p and p17 by tdc-1p (tdc-1p is expressed in the RIM neurons ~ 445 m.p.f.). These caspase subunits are therefore expected to reconstitute expression (and induce ablation) in embryonic RIM neurons. (E) Representative confocal image of a wild type L3 animal expressing membrane-targeted PH:GFP in the RIM neurons with RIM-specific promoter gcy-13p. (F,G) As E, but in animals additionally expressing the caspase subunits for (f) ablation strategy one and (G) ablation strategy 2. Note the absence of RIM labeling, indicating successful ablation of the RIM neurons. Scale bar = 10 μm, applies to E-G. H-M, Confocal images showing AIB (labeled with cytoplasmic mCherry; H,K) and RIM neurons (labeled with PH:GFP; I,L) and merged images (J,M) for wild-type animals (H–J) and animals in which RIM was genetically ablated (K–M). RIM ablation was achieved using Strategy 2, see Materials and methods. Magenta dashed line (M) represents the AIB anterior neighborhood. (N) Quantification of the penetrance of the AIB neurite placement defect as the percentage of animals with normal AIB neurite placement in the anterior neighborhood. Strategy one and Strategy two refer to split caspase ablations (Chelur and Chalfie, 2007) using two different combinations of promoters expressed in RIM neurons (see Materials and methods). ****p < 0.0001 (two-sided Fisher’s exact test). Numbers on bars represent number of animals examined. (O) Quantification of the minimum perpendicular distances between the AIB proximal and distal neurites in WT (n = 28) and RIM-ablated populations (n = 10 for strategy one and n = 14 for strategy 2). ****p < 0.0001; **p = 0.0011 (one-way ANOVA with Dunnett’s multiple comparisons test). n represents the number of AIB neurons measured from 14, 5, and 7 animals from the WT, ablation strategy one and ablation strategy two populations respectively. Effect size estimate, d = 2.313 for WT and ablation strategy 1, and 1.19 for WT and ablation strategy 2. (P,Q) Confocal micrographs of animals where AIB (cyan) and the RIM and RIC neurons (magenta) are co-labeled and SYG-1 is expressed specifically in RIM and RIC (see Materials and methods) in a syg-1(ky652) mutant background. The dashed box represents the nerve ring region containing the neurites of AIB, RIM and RIC, and is magnified in P’ and Q’. The AIB distal neurite is positioned along RIM (P’) or along both RIM and RIC (Q’). The yellow arrowheads and yellow arrows point at the RIC neurite and the RIM neurite, respectively. Scale bar = 10 μm for H–M, P,Q and 2 μm for P’ and Q’.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig5-figsupp5-v2.jpg)

**Figure 5—figure supplement 5.:** (A,B) Plots showing individual values of syg-1 anterior enrichment (A), as measured from the syg-1 transcriptional reporter and percent AIB neurite zippered (B) (see Materials and methods for details). Individual values at each timepoint in A and B were averaged to produce the magenta and blue curves respectively in the plot in Figure 5S. Each point in A represents a measurement of syg-1 anterior enrichment from one side of the embryo, two values are therefore obtained from each embryo (see Materials and methods). Each point in B represents a single AIB neurite. The syg-1 anterior enrichment values (A) were quantified from four different embryos and percentages of the AIB neurite zippered (B) were quantified from three different embryos.

![Figure 5—figure supplement 6.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig5-figsupp6-v2.jpg)

**Figure 5—figure supplement 6.:** (A-C) Confocal micrograph of a larval stage four animal showing AIB (cyan, A), a translational fusion marker GFP:SYG-2 (GFP fused to a 16 kb genomic region including 8 kb upstream sequence and the coding region of syg-2 Shen et al., 2004) (yellow, B) and merge (C). Arrowheads in C point to the subset of SYG-2 puncta that colocalize with the AIB distal neurite (co-injection marker odr-1p:RFP labels an amphid neuron in the same channel as AIB (cyan)).

Prior to 470 m.p.f., syg-1 reporter expression in the nerve ring was primarily restricted to a single band corresponding to the AIB posterior neighborhood (Figure 5K, O and O’). This coincides with periods of outgrowth and placement of the AIB neurons in the posterior neighborhood. However, over the subsequent three hours of embryogenesis (470–650 m.p.f.), SYG-1 expression levels progressively increase in the anterior neighborhood while decreasing in the posterior neighborhood (Figure 5L–R’, Figure 5—figure supplement 1, Figure 5—video 1). The change in expression levels of SYG-1 across neighborhoods coincides with the relocation of the AIB neurite, from the posterior to the anterior neighborhood via retrograde zippering (Figure 5S). To identify which neurons in the nerve ring express SYG-1, we performed single-cell lineaging (Murray et al., 2006) of the neurons expressing the syg-1 transcriptional reporter at approximately 430 m.p.f. (Figure 5—figure supplement 2A-C, Figure 5—video 2). The six neurons in the anterior neighborhood, and 10 neurons in the posterior neighborhood which we identified (Figure 5—figure supplement 2C), were consistent with the identity of SYG-1 expressing neurons from embryonic transcriptomics data (Packer et al., 2019). Both our data, and embryonic transcriptomics data, reveal dynamic changes in the expression levels of SYG-1 in these neurons (Figure 5—figure supplement 2). The transcriptomic studies also demonstrate a ten-fold increase in SYG-2 transcript levels in AIB at the time in which the AIB neurite transitions between neighborhoods (and consistent with our findings that SYG-2 acts cell autonomously in AIB). Together with the biophysical analyses, our data suggests that spatiotemporal changes in SYG-1 and SYG-2 expression might result in changes in forces that drive differential adhesion of AIB neurites via retrograde zippering of their axon shafts.

### Ectopic SYG-1 expression is sufficient to alter placement of the AIB distal neurite

To test whether coincident SYG-1 expression in the anterior neighborhood was responsible for repositioning of AIB to that neighborhood, we set to identify and manipulate the sources of SYG-1 expression. We found that increases of SYG-1 in the anterior neighborhood were caused by (i) ingrowth of SYG-1-expressing neurons into the anterior neighborhood and (ii) onset of syg-1 expression in neurons of the anterior neighborhood (Figure 5—figure supplement 1). We observed strong and robust SYG-1 expression in the RIM neurons, as RIM grows into the anterior neighborhood, contributing to increased SYG-1 expression levels in this neighborhood. Since RIM is also one of the major fasciculation partners of AIB, we hypothesized that SYG-1 expression in RIM neurons contributes to AIB neurite placement (Figure 5—figure supplement 3). To test this hypothesis, we ablated RIM neurons. We observed that RIM ablations result in defects in AIB neurite placement which phenocopied those seen for syg-1 loss-of-function mutants (Figure 5—figure supplement 4). We also observed that expression of SYG-1 specifically in RIM and RIC neurons in syg-1(ky652) mutants was sufficient to position the AIB distal neurite along these neurons (Figure 5—figure supplement 4P-Q).

If differences in SYG-1 expression level between the neighborhoods results in differential adhesion, and consequent relocation of the AIB distal neurite from the posterior to the anterior neighborhood, then purposefully altering these differences should predictably alter the position of the AIB neurite. We tested this hypothesis by inverting the adhesion differential through the overexpression of SYG-1 in the posterior neighborhood (see Materials and methods). Unlike wild type and syg-1 mutants (Figure 6A–F, Figure 6—figure supplement 1), animals with ectopic syg-1 expression in the posterior neighborhood displayed a gain-of-function phenotype, in which the AIB distal neurite remained partially positioned in the posterior neighborhood throughout postembryonic larval stages (Figure 6G–J, Figure 6—figure supplement 1). Importantly, these gain-of-function effects caused by ectopic expression of SYG-1 are not observed in a syg-2(ky671) mutant background (Figure 6K), consistent with SYG-2 expression in AIB being required for AIB’s repositioning to the SYG-1 expressing layers. Our findings indicate that inverting the adhesion differential via enrichment of SYG-1 in the ‘wrong’ neighborhood predictably affects relocation of the AIB distal neurite in a way that is consistent with differential adhesion mechanisms.

![Figure 6.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig6-v2.jpg)

**Figure 6.:** (A) Lateral view schematic of a wild-type AIB neuron (cyan) in the context of the posterior (orange) and anterior (magenta) neighborhoods, and the nerve ring (light neon). Higher SYG-1 endogenous expression in the anterior neighborhood represented by yellow arrowhead. (B–C) Confocal image of a wild type animal with AIB (labeled with cytoplasmic mCherry, in cyan) and the posterior neighborhood neurons AWC and ASE (labeled with cytoplasmic GFP, in orange). The dashed box represents the region of contact between AIB and the posterior neighborhood neurons, magnified in (C). Magenta dashed line represents the AIB anterior neighborhood. (D–F) As (A–C), but in the syg-1(ky652) lof (loss of function) mutant background. Note that the distal neurite is positioned away from the posterior neighborhood, as in wild type, although these animals display defects in fasciculation with the anterior neighborhood (as shown in Figure 4). (G–I) As (D–F), but with ectopic overexpression of SYG-1 in the posterior neighborhood neurons. In the schematic (G), expression of SYG-1 in the posterior neighborhood (achieved here using nphp-4p, also see Figure 6—figure supplement 1) is represented by a yellow arrowhead (as in (A), but here in posterior neighborhood). Note that the AIB distal neurite is now abnormally positioned in the posterior neighborhood in which SYG-1 was ectopically expressed (H, I). (J) Schematic (left) and scatter plot quantification (right) of minimum perpendicular distances (dmin, indicated by black double-headed arrow) between the AIB distal neurite and posterior neighborhood neurons in WT (in black, n = 17), syg-1(ky652) (in green, n = 18), and two syg-1(ky652) populations with SYG-1 overexpressed in two different sets of posterior neighborhood neurons via the use of nphp-4p and (in blue) mgl-1bp (in red) (n = 18 and n = 16 respectively). **p = 0.0056 and 0.0070, respectively (one-way ANOVA with Dunnett’s multiple comparisons test). Effect size estimate, d = 1.075 and 1.140, respectively. Error bars indicate standard error of the mean (S.E.M.). n represents the number of AIB neurites quantified. Quantifications were done from nine animals each for WT, syg-1(ky652) and nphp-4p:syg-1; syg-1(ky652) and eight animals for mgl-1bp:syg-1; syg-1(ky652). (K) Quantification of penetrance of the ectopic AIB neurite placement represented as the percentage of animals with the AIB distal neurite partially positioned in the posterior neighborhood in the WT, syg-1(ky652), posterior SYG-1 overexpression strains (colors represent the same strains as in J) and a posterior SYG-1 overexpression strain in syg-2(ky671) background. Numbers on bars represent number of animals examined. ***p = 0.0002 for syg-1(ky652) and nphp-4p expressed SYG-1 and ****p < 0.0001 for syg-1(ky652) and mgl-1bp expressed SYG-1 by two-sided Fisher’s exact test (also see Figure 6—figure supplement 1). Scale bar = 10 μm in B, E and H and 1 μm in C, F, and I. Cell body is marked with an asterisk.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A) Plot showing the percentage of the AIB distal neurite ectopically positioned in the posterior neighborhood in two strains expressing SYG-1 ectopically in the posterior neighborhood. These measurements were done from the same WT, syg-1(ky652), mgl-1bp:syg-1; syg-1(ky652) and nphp-4p:syg-1; syg-1(ky652) as in Figure 6. mgl-1bp and nphp-4p are promoters driving expression specifically in the posterior neighborhood (see Figure 6 and Materials and methods) One-way ANOVA with Dunnett’s multiple comparisons test was performed. **p = 0.0017 for WT and mgl-1bp:syg-1; syg-1(ky652) and for syg-1(ky652) and mgl-1bp:syg-1; syg-1(ky652), and **p = 0.0015 for WT and nphp-4p:syg-1; syg-1(ky652). syg-1(ky652) and nphp-4p:syg-1; syg-1(ky652). Effect size = 1.186 for WT and nphp-4p:syg-1 and nphp-4p:syg-1; syg-1(ky652). Effect size = 1.304 for WT and mgl-1bp:syg-1 and mgl-1bp:syg-1; syg-1(ky652). (B) Schematic of the receptor-ligand pair SYG-1 (green) and SYG-2 (purple). The red dashed box includes the SYG-1 extracellular Ig domains and transmembrane domain (collectively referred to as SYG-1 ecto). The yellow dashed box includes the SYG-1 transmembrane domain and cytoplasmic domains (collectively referred to as the SYG-1 endodomain or SYG-1 endo). (C) Quantification of penetrance of the ectopic AIB neurite placement as the percentage of animals with the AIB distal neurite partially positioned in the posterior neighborhood in the indicated genotypes. ****p < 0.0001 (by two-sided Fisher’s exact test) for syg-1(ky652) and mgl-1bp:syg-1; syg-1(ky652), in which SYG-1 is expressed specifically in the posterior neighborhood (denoted as posterior SYG-1); for mgl-1bp:syg-1; syg-1(ky652) and mgl-1bp:syg-1; syg-1(ky652); syg-2(ky671), and for mgl-1bp:syg-1; syg-1(ky652) and mgl-1bp:syg-1endo; syg-1(ky652) where mgl-1bp:syg-1endo drives expression of the SYG-1 endodomain in the posterior neighborhood. Number on bars represent the number of animals examined. The first four bars are the same as the ones corresponding to these genotypes in Figure 6K. The black, green and purple bars represent WT, syg-1(ky652) and syg-2(ky671) backgrounds, respectively.

We reasoned that if differential adhesion mechanisms were driving zippering of the AIB neurite during development, expression of the SYG-1 ectodomain would be sufficient to drive the ectopic interactions upon misexpression (Chao and Shen, 2008; Galletta et al., 2004; Gerke et al., 2003). Indeed, expression of the SYG-1 ectodomain in the posterior neighborhood resulted in gain-of-function phenotypes for AIB neurite placement, similar to those seen with misexpression of full-length SYG-1 (although penetrance of these effects was lower than that observed with full-length SYG-1). Consistent with the importance of adhesion-based mechanisms in the observed phenotypes, ectopic expression of the SYG-1 endodomain (which lacks the extracellular ectodomain necessary for interaction with SYG-2, see Materials and methods) in the posterior neighborhood did not result in mislocalization of AIB (Figure 6—figure supplement 1).

### AIB neurite placement by retrograde zippering, and presynaptic assembly, are coordinated during development

AIB displays a polarized distribution of pre- and postsynaptic specializations, and these specializations specifically localize to the neurite segments occupying the anterior and posterior neighborhoods, respectively. The placement of the AIB neurite in the anterior and posterior neighborhoods and its synaptic polarity underlies its role as a connector hub across layers (Sabrin, 2019; Towlson et al., 2013). To understand how the distribution of presynaptic specializations relates to the placement of the AIB neurite, we imaged the subcellular localization of presynaptic proteins RAB-3, CLA-1, and SYD-2 during AIB embryonic development. We observed that presynaptic proteins populate the AIB neurite starting from the tip toward the dorsal midline, in a retrograde pattern reminiscent of the retrograde zippering that places the AIB neurite in the anterior neighborhood (Figure 7A–I). The timing of formation of presynaptic sites suggested that that the process of synaptogenesis closely followed the retrograde zippering mechanisms of AIB repositioning (Figure 7J and K, Figure 7—figure supplement 1). Consistent with synaptogenesis occurring after retrograde zippering, we observed that a novel allele of syd-2(ola341) isolated from our screens exhibit synaptic defects, but do not display phenotypes in AIB neurite placement within the anterior neighborhood (Figure 7—figure supplement 1G-K), indicating that molecules that affect synaptogenesis do not necessarily result in fasciculation defects for AIB. Also consistent with the importance of AIB neurite placement in the anterior neighborhood for correct synaptogenesis, we observed that in syg-1(ky652), RAB-3 signal was specifically and consistently reduced in regions of the AIB distal neurite incapable of repositioning to the anterior neighborhood (Figure 7—figure supplement 3). Overall, our study identified a role for differential adhesion in regulating neurite placement via retrograde zippering, which in turn influences synaptic specificity onto target neurons (Figure 7K).

![Figure 7.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig7-v2.jpg)

**Figure 7.:** (A) Axial view schematic of the AIB neurons (cyan) with presynaptic protein RAB-3 (yellow) puncta along the distal neurite. Arrowhead indicates the tip of the distal neurite and arrow/dashed line indicate the dorsal midline. (B–E) Time-lapse imaging of RAB-3 localization in AIB during embryogenesis. (B–E) are merged diSPIM maximum intensity projections of AIB labeled with membrane-tagged mCherry (cyan) and AIB presynaptic sites labeled with GFP:RAB-3 (yellow), at different timepoints during embryogenesis. (B’-E’) represent the GFP:RAB-3 channel for images in B–E). Note in (B, B’) and (C, C’) that the RAB-3 signal in the neurite is localized exclusively near the neurite tip. As development progresses, there is more RAB-3 signal throughout the neurite from the tip up to the midline (in (D, D’) and (E, E’). Therefore, RAB-3 becomes progressively enriched from the tip up to the midline during development, and the timing for this process correlates, with a slight delay, with the developmental timing of AIB zippering (Figure 2I–K). Arrowhead and arrow, as in (A), indicate the tip of the distal neurite and the region of the neurite near the dorsal midline (dashed vertical line) respectively. Scale bar = 10 μm applies (B–E) and (B’-E’). (F–I) Straightened distal neurites from AIB (corresponding to the region in (B–E) which is marked by the arrowhead (AIB tip) and arrows (dorsal midline)). Note presynaptic assembly, as imaged by RAB-3 accumulation, from the tip of the neurite towards the midline of AIB, reminiscent of the zippering event (Figure 2). Scale bar = 1 μm. (J) Plot showing average RAB-3, CLA-1 and SYD-2 intensities along the AIB distal neurite over time (yellow, orange and green, respectively) and percentage of the relocating AIB distal neurite that has zippered onto the anterior neighborhood (blue). See Figure 7—figure supplement 1 for images of CLA-1 developmental dynamics in AIB. The intensities in the plot represent values calculated at the indicated developmental times on the x-axis ( ± 10 min). The reported values of ‘% AIB zippered’ are averaged are the same as in Figure 5S. Note that RAB-3, CLA-1 and SYD-2 intensity start increasing from after completion of zippering (540 m.p.f.). Error bars represent standard error of the mean (S.E.M.). See Figure 7—figure supplement 2 for individual RAB-3, CLA-1 and SYD-2 intensity values. Times are in m.p.f. (minutes post fertilization). (K) Schematic model showing progressive retrograde zippering leading to placement of the AIB neurite along two different layers. This is accompanied by a switch in SYG-1 expression between layers, and synaptic protein localization in a retrograde order along the neurite, resembling the order of zippering.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Schematic of the lateral view of an AIB neuron (cyan) with presynaptic sites labeled with active zone protein CLA-1 (yellow). (B–E) Time-lapse imaging of CLA-1 localization in AIB during embryogenesis. (B–E) are merged diSPIM maximum intensity projections of AIB labeled with membrane-tagged mCherry (cyan) and AIB presynaptic sites labeled with GFP:CLA-1 (yellow), at different timepoints during embryogenesis. As development progresses, there is more CLA-1 signal throughout the neurite from the tip up to the midline, similar to the time-course of RAB-3 localization (Figure 7). Arrowhead and arrow, indicate the tip of the distal neurite and the region of the neurite near the dorsal midline respectively. Scale bar = 10 μm applies (B–E). (F) Straightened distal neurites from AIB (corresponding to the region in (B–E) which is marked by the arrowhead (AIB tip) and arrows (dorsal midline)). Scale bar = 2 μm. Times are in m.p.f. (minutes post fertilization). (G–K) Representative confocal image of a syd-2(ola341) animal co-expressing (H) cytoplasmic mCherry and (I) GFP:RAB-3 in AIB for simultaneous visualization of AIB morphology and presynaptic sites. (J) is a merge of (H) and (I). The region of the AIB neurite bound by the dashed box in (J) is magnified in (K). Note altered distribution of presynaptic protein RAB-3. RAB-3 is enriched near the tip instead of being localized all along the distal neurite. Scale bar = 10 μm in (H–J) and 3 μm in (K).(K) Representative confocal image of a syd-2(ola341) animal with AIB labeled with cytoplasmic mCherry (cyan) and the distal neighborhood neuron, RIM, labeled with cytoplasmic GFP (magenta). Note that although distribution of RAB-3 is altered (H–K), the placement of the AIB neurite in the RIM-containing distal neighborhood is unaltered in syd-2(ola341). Scale bar = 10 μm.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** A-C Plots showing SYD-2 (A), RAB-3 (B), and CLA-1 (C) mean intensities over time from individual neurites. These values were averaged to obtain the intensity plot in Figure 7J. SYD-2, RAB-3 and CLA-1 intensities were calculated from 2, 3, and 4 different embryos, respectively.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig7-figsupp3-v2.jpg)

**Figure 7—figure supplement 3.:** (A-F) Schematic (A) and representative confocal image of the AIB neurite (B), AIB presynaptic sites (C) and neurite of the postsynaptic partner, the RIM neuron in the anterior neighborhood (D). (E) is a merged image. The dashed box represents the region of contact between the AIB and RIM neurites, magnified in F. (G–L) As (A–F) but in the syg-1(ky652) mutant background. Note the gaps between the AIB distal neurite and the RIM neurites (L) and reduced localization of RAB-3 along the AIB neurite in the region where it is detached from RIM (white arrows in L). Scale bar = 10 μm in A-E, G-K and 1 μm in F,L. (M) Line intensity plot showing RAB-3 fluorescence intensity (yellow) and AIB-RIM contact (magenta) along the length of the AIB distal neurite in G-L. Note the peaks in the two line profiles align, indicating higher RAB-3 intensity at points of AIB-RIM contact. (N) Box plot (10–90 percentile) showing mean intensities of RAB-3 in adhered and detached regions in syg-1(ky652) mutant neurites that exhibit detachment between AIB and RIM (n = 12, where n = number of animals). **p = 0.0003 (unpaired two-tailed t-test). Effect size, d = 1.643.

### SYG-1 is required for layer-specific placement of rich-club neuron AVE

We next examined if syg-1 also mediates layer-specific placement of other neurites. We focused on the rich-club AVE neurons, the neurites of which are also placed in two neighborhoods, one of which coincides with the syg-1-enriched AIB distal neighborhood (Figure 8A–D) (White et al., 1986, Towlson et al., 2013, Sabrin, 2019, Moyle et al., 2021). Reconstructions from electron micrographs reveal that the AVE neurons have a morphology similar to AIB, however its neurite is more anteriorly placed (by one stratum) with respect to AIB (Figure 8A; Moyle et al., 2021). Therefore, the proximal neurite of AVE occupies the S2/S3 neighborhood (also occupied by the AIB distal neurite) (Figure 8B–D). Since syg-1 expression is enriched in this ‘AIB anterior/AVE posterior’ neighborhood, we tested, by examining AVE neurite placement relative to the RIM neurons, if placement of the AVE neurite in this neighborhood is also affected in syg-1(ky652) mutants. When we fluorescently labeled RIM and AVE in wildtype animals, we observed that the proximal AVE neurite runs along the RIM neurite, consistent with EM studies (White et al., 1986; Witvliet et al., 2021, Figure 8E, F and F’). By contrast, in syg-1 mutants the AVE proximal neurite frequently deviates from its trajectory along RIM (seen in 50 % of syg-1(ky652)) mutants versus 9.1 % in wild type (Figure 8G, H, H’1). The dorsal midline shift of AVE is also affected in syg-1 mutant animals (mean length = 2.73 μm in syg-1(ky652) and 3.99 μm in wild-type animals; Figure 8J). The detachment of the AVE neurite resembles defects that would arise from defective zippering of the neurite onto this neighborhood. Together with the AIB studies, these observations are consistent with SYG-1 expression in a specific neuropil neighborhood resulting in specific sorting of neurites into the neighborhood by zippering mechanisms.

![Figure 8.](https://cdn.elifesciences.org/articles/71171/elife-71171-fig8-v2.jpg)

**Figure 8.:** (A) Volumetric reconstruction of command interneuron AVER (green) and AIBR (cyan) from the segmented JSH EM dataset (Brittin et al., 2018; White et al., 1986). Note the similarity in morphology of the two neurons. The distal neurite of AIB and the proximal neurite of AVE lie at the same position (indicated by magenta arrow). The arrowheads indicate the dorsal shift that forms the chiasm in AIB and AVE. Scale bar = 5 μm, also applies to B. (B,C) Volumetric reconstruction of the AVE neurons (green) (B) and the AIB neurons (cyan) (C) in the context of the nerve ring strata S2 (purple) and S3 (orange). Note the placement of the AVE proximal neurite along the border of S2 and S3, and the AVE distal neurite at the anterior boundary of S2 (the anterior boundary abuts S1, not shown here). Note the placement of the AIB distal neurite, also at the S2/S3 border, similar to the AVE proximal neurite. The dashed lines indicate the layer borders. The yellow, magenta and orange arrows correspond to the S1/S2, S2/S3, and S3/S4 borders respectively (S4 not shown here). Scale bar in C = 5 μm. (D) Schematic of the lateral view of AVE (green) in the context of its neighborhoods: proximal (magenta) and distal (yellow), with the nerve ring (light brown) and pharynx (gray). Black arrowhead indicates a posterior-anterior chiasm. The magenta and yellow arrows indicate the positions of the AVE proximal and AVE distal neighborhoods, respectively and coincide with the S2/S3 and S1/S2 borders, respectively (see B). Note that while the design principles of AVE are similar to those of rich-club interneuron AIB, their positions in the nerve ring, and the strata they connect, are different – the AVE neurite is placed more anteriorly by one stratum compared to AIB. E,F,F’, Confocal image of wild-type animal with AVE and RIM co-labeled. The magenta and yellow arrows indicate the positions of the AVE proximal and AVE distal neighborhoods, respectively. White arrowhead indicates AVE chiasm, corresponding to its anterior shift. Dashed box shows region of contact of the AVE and RIM neurites, magnified in F. (F’) is a schematic of the image in (F). Scale bar corresponds to 10 μm in E and 1 μm in F. Scale bars in E and F apply to G and H, respectively. Cell bodies are marked with an asterisk. G,H,H’, As E,F,F’ but in syg-1(ky652) mutant background. Note the gap between the AVE proximal neurite and the RIM neurites (G,H,H’) and defect in the dorsal midline shift. (I) Scatter plot showing quantification of the loss of contacts between the AVE and RIM neurites. The extent of detachment of the AVE proximal neurites from RIM, and hence its deviation from the RIM neighborhood, was quantified using the indicated formula in Figure 4M (also see STAR Methods). Scatter plot depicts % detachment values for wild type (n = 22) and syg-1(ky652) (n = 16) calculated from 11 and 8 animals respectively. Error bars indicate standard error of the mean (S.E.M.). **P = 0.002 (unpaired two-tailed t-test). Effect size d = 1.002. (J) Quantification of length of the posterior-anterior shift, quantified for each AVE neurite, for WT (n = 32) and syg-1(ky652) mutants (n = 40) and displayed as a scatter plot. These were calculated from 16 and 20 animals respectively from WT and syg-1(ky652). Error bars indicate standard error of the mean (S.E.M.). ***p = 0.0001 (unpaired two-tailed t-test). Effect size d = 1.003. n represents the number of AIB neurites quantified.

## Discussion

The precise assembly of the cellular architecture of AIB in the context of the layered nerve ring neuropil underwrites its role as a “rich-club” neuron. AIB was identified, through graph theory analyses, as a rich-club neuron (Towlson et al., 2013) - a connector hub with high betweeness centrality, which links nodes of the C. elegans neural networks with high efficiency. We observe that the AIB neurite segments are precisely placed on distinct functional layers of the nerve ring neuropil, and that the placement of these segments, in the context of the pre- and postsynaptic polarity of the neurite, enables AIB to receive inputs from one neighborhood and relay information to the other, thereby linking otherwise modular and functionally distinct layers. Our connectomic analyses and in vivo imaging reveal that these features of AIB architecture are stereotyped across examined C. elegans animals, even as early as the first larval stage, L1 (Witvliet et al., 2021). They are also evolutionarily conserved in nematodes, as examination of AIB in the connectome of the nematode Pristionchus pacificus, which is separated from C. elegans by 100 million years of evolutionary time, revealed similar design principles (Hong et al., 2019). The architecture of AIB is reminiscent to that seen for other ‘nexus neurons’ in layered neuropils, such as AII amacrine cells in the inner plexiform layer of the vertebrate retina (Marc et al., 2014). Like AIB, All amacrine cells receive inputs from one laminar neighborhood (rod bipolar axon terminals in ‘lower sublamina b’) and produce outputs onto a different neighborhood (ganglion cell dendrites in ‘sublamina a’) (Kolb, 1995; Strettoi et al., 1992). For these nexus neurons, as for AIB, the precise placement within neuropil layers is critical for their function and connectivity. We now demonstrate that for AIB, this precise placement is governed via differential adhesion instructed by the layer-specific expression of IgCAM SYG-1. Interestingly, other ‘rich-club’ neurons that emerged from connectomic studies, such as AVE and RIB, are also placed along SYG-1-expressing nerve ring layers, suggesting that similar, SYG-1 dependent and layer-specific mechanisms could underpin placement of these neurons.

Differential adhesion acts via retrograde zippering mechanisms to position AIB across multiple and specific layers. We established new imaging paradigms (Wu et al., 2021; Wu et al., 2013) to document in vivo embryonic development of AIB and observed that the sorting of its distal neurite segment onto the anterior neighborhood occurs, not via tip-directed fasciculation as we had anticipated, but via neurite-shaft retrograde zippering. Zippering mechanisms had been previously documented in tissue culture cells (Barry et al., 2010; Voyiadjis et al., 2011), where they were shown to act via biophysical forces of tension and adhesion (Smít et al., 2017). However, these mechanisms have not been previously reported in vivo. We now demonstrate that retrograde zippering acts in vivo to precisely position neurites in specific neuropil layers. We observe that different segments of the AIB neurite are positioned in different neighborhoods by this mechanism. Zippering of the AIB neurite continues in the anterior neighborhood till adhesion of the neurite to this neighborhood exceeds the opposing action of mechanical tension on the neurite, and stops when adhesion and tension balance each other (Figure 3). Zippering stops at the dorsal midline where several neurites, including those of AIB’s fasciculating partners, stop growing or change trajectories, possibly resulting in a change in adhesion forces on the AIB neurite, and a balance between adhesion and tension. Altogether, our data suggest that the interplay between biophysical forces results in precise placement of segments of the same neurite, allowing it to span two distinct neighborhoods.

Retrograde zippering depends on differential adhesion across layers and is instructed in part by the dynamic expression of SYG-1, and its interaction with the SYG-2 expressing AIB neurons. While we demonstrate that SYG-1 and SYG-2 are important for AIB neurite placement, we hypothesize that other adhesion molecules act redundantly in regulating placement, explaining the partial loss-of-function phenotypes observed in this study, and the gain of function phenotypes upon ectopic expression of SYG-1 in sublayers. Our work also demonstrates that differences in expression levels of IgCAMs such as SYG-1 can result in differential adhesion across whole neuropils. The observed role of SYG-1 in the nerve ring is reminiscent of the role of the SYG-1 and SYG-2 mammalian orthologs, Kirrel2 and Kirrel3, in axon sorting in the olfactory system (Serizawa et al., 2006), and consistent with observations in C. elegans that syg-2 loss of function mutants result in defasciculation defects of the HSNL axon (Shen et al., 2004). Our findings are also consistent with studies on the roles of SYG-1 and SYG-2 Drosophila orthologues, Hibris and Roughest, in tissue morphogenesis of the pupal eye (Bao and Cagan, 2005). In these studies, Hibris and Roughest were shown to instruct complex morphogenic patterns by following simple, adhesion and surface energy-based biophysical principles that contributed to preferential adhesion of specific cell types. We now demonstrate that similar biophysical principles of differential adhesion might help organize neurite placement within heterogeneous tissues, such as neuropils in nervous systems.

SYG-1 and SYG-2 coordinate developmental processes that result in synaptic specificity for the AIB interneurons. Synapses in C. elegans are formed en passant, or along the length of the axon, similar to how they are assembled in the CNS for many circuits (Jontes et al., 2000; Koestinger et al., 2017). Placement of neurites within layers therefore restrict synaptic partner choice. We examined how these events of placement, and synaptogenesis, were coordinated for the AIB interneurons and observed coincidence of presynaptic assembly and retrograde zippering of the AIB neurite. SYG-1 and SYG-2 were identified in C. elegans for their role in synaptic specificity (Shen and Bargmann, 2003; Shen et al., 2004), and the assembly of synaptic specializations can result in changes in the cytoskeletal structure and adhesion junctions (Missler et al., 2012). We observe in our studies that zippering precedes the (detectable) subcellular localization of presynaptic components, suggesting that during AIB development, neurite placement by retrograde zippering constitutes a specificity step distinct from synaptic protein localization and synapse formation. Nonetheless, we hypothesize that coordinated assembly of synaptic sites during the process of retrograde zippering could provide forces that stabilize zippered stretches of the neurite. These could in turn ‘button’ and fasten the AIB neurite onto the anterior layer, securing its relationship with its postsynaptic partner. Consistent with this hypothesis, we observe that ablation of one of its main postsynaptic partners, the RIM neurons, results in defects in AIB placement in the anterior neighborhood. Given the important role of adhesion molecules in coordinating cell-cell interactions and synaptogenesis (Sanes and Zipursky, 2010; Sanes and Zipursky, 2020; Tan et al., 2015; Yamagata and Sanes, 2008; Yamagata and Sanes, 2012), we speculate that adhesion molecules involved in synaptogenesis and neurite placement within layered neuropils might similarly act to coordinate differential adhesion and synaptogenesis onto target neurons.

Zippering mechanisms via affinity-mediated adhesion might help instruct neighborhood coherence while preserving ‘fluid’, or transient interactions among neurites within neuropil structures. Analysis of connectome data and examination of neuronal adjacencies within the nerve ring neuropil revealed that contact profiles for single neurons vary across animals, indicative of fluid or transient interactions during development (Moyle et al., 2021). Yet neuropils have a stereotyped and layered architecture encompassing specific circuits. We hypothesize that dynamic expression of adhesion molecules help preserve tissue organization in tangled neuropils via the creation of affinity relationships of relative strengths. These relationships, in the context of outgrowth decisions of single neurites, would contribute to the sorting of neurites onto specific strata. We propose that sorting of neurite into strata would happen through biophysical interactions not unlike those reported for morphogenic events in early embryos and occurring via differential adhesion (Steinberg, 1962; Steinberg and Gilbert, 2004). Spatiotemporally restricted expression of CAMs in layers, as we observe for SYG-1 and has been observed for other CAMs in layered neuropils (Sanes and Zipursky, 2010; Sanes and Zipursky, 2020; Tan et al., 2015; Yamagata and Sanes, 2008; Yamagata and Sanes, 2012) would then result in dynamic, affinity-mediated relationships that preserve neighborhood coherence in the context of ‘fluid’, or transient interactions among neurites within the neuropil structures.

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
      <td>Strain (C. elegans)</td>
      <td>ujIs113[pie-1p::mCherry::H2B::pie-1 3'UTR+ nhr-2p::his-24::mCherry::let-858 3'UTR+ unc-119(+)];II</td>
      <td>Duncan et al., 2019</td>
      <td>BV276</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>ujIs113;oyIs48[Pceh-36::GFP, lin-15(+)];V</td>
      <td>gift from John Murray</td>
      <td>JIM158</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaIs67[DACR2245 at 40 ng/uL + DACR1412 at 30 ng/uL + DACR218 at 30 ng/uL];X</td>
      <td>This paper</td>
      <td>DCR5516</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex3394[DACR2796 at 60 ng/uL + DACR2651 at 60 ng/uL + DACR218 at 30 ng/uL]</td>
      <td>This paper</td>
      <td>DCR5761</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex3666[DACR199 at 2 ng/uL + DACR218 at 30 ng/uL];olaIs67</td>
      <td>This paper</td>
      <td>DCR6222</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>oyIs48;olaIs67</td>
      <td>This paper</td>
      <td>DCR6301</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex4624[DACR3149 at 10 ng/uL + DACR218 at 30 ng/uL];olaIs67</td>
      <td>This paper</td>
      <td>DCR7648</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaIs68[DACR2245 at 40 ng/uL + DACR1412 at 30 ng/uL + DACR218 at 30 ng/uL]</td>
      <td>This paper</td>
      <td>DCR5517</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaIs68;syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8220</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaIs68;syg-1(ok3640)</td>
      <td>This paper</td>
      <td>DCR8486</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex4624;olaIs68;syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8183</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>kyIs235;kyEx679;syg-1(ky652)</td>
      <td>This paper</td>
      <td>CX5862</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>kyEx679;olaIs68;syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8180</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex4624;kyEx679;olaIs68;syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8489</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain, strain background (C. elegans)</td>
      <td>olaIs68;syg-2(ky671)</td>
      <td>This paper</td>
      <td>DCR6767</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex4624;olaIs68;syg-2(ky671)</td>
      <td>This paper</td>
      <td>DCR8468</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>oyIs48; olaIs68;syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8488</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex5120[DACR3529 at 30 ng/uL + DACR1412 at 30 ng/uL + DACR218 at 30 ng/uL]</td>
      <td>This paper</td>
      <td>DCR8440</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex5063[DACR3492 at 25 ng/uL + DACR3505 at 40 ng/uL + DACR2312 at 25 ng/uL + DACR20 at 25 ng/uL];olaIs67</td>
      <td>This paper</td>
      <td>DCR8365</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex4071[DACR2637 at 15 ng/uL + DACR218 at 30 ng/uL];olaIs67</td>
      <td>This paper</td>
      <td>DCR6814</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex4130[DACR2704 at 100 ng/uL + DACR218 at 50 ng/uL];ujIs113</td>
      <td>This paper</td>
      <td>DCR6920</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex4052[DACR2607 at 100 ng/uL + DACR2609 at 25 ng/uL + DACR218 at 30 ng/uL];olaIs67</td>
      <td>This paper</td>
      <td>DCR6782</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex4054[DACR2607 at 100 ng/uL + DACR2609 at 25 ng/uL + DACR218 at 30 ng/uL];olaIs67</td>
      <td>This paper</td>
      <td>DCR6784</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex3388[DACR2371 at 75 ng/uL + DACR2404 at 30 ng/uL + DACR218 at 30 ng/uL]</td>
      <td>This paper</td>
      <td>DCR5730</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex4618[DACR2607 at 100 ng/uL + DACR2609 at 25 ng/uL + DACR2863 at 25 ng/uL + DACR218 at 30 ng/uL];olaIs67</td>
      <td>This paper</td>
      <td>DCR7642</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex4619[DACR2607 at 100 ng/uL + DACR2609 at 25 ng/uL + DACR2863 at 25 ng/uL + DACR218 at 30 ng/uL];olaIs67</td>
      <td>This paper</td>
      <td>DCR7643</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex3949[DACR2607 at 100 ng/uL + DACR2609 at 25 ng/uL + DACR2351 at 25 ng/uL + DACR218 at 30 ng/uL]</td>
      <td>Moyle et al., 2021</td>
      <td>DCR6633</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex2887[DACR2245 at 100 ng/uL + DACR2404 at 30 ng/uL + DACR218 at 30 ng/uL]</td>
      <td>This paper</td>
      <td>DCR4894</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex3570[DACR2481 at 10 ng/uL + DACR218 at 50 ng/uL];ujIs113</td>
      <td>This paper</td>
      <td>DCR6082</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex5105[DACR3605 at 50 ng/uL + DACR218 at 30 ng/uL]</td>
      <td>This paper</td>
      <td>DCR8421</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaIs117[DACR3502 at 30 ng/uL + DACR20 at 25 ng/uL];olaIs68</td>
      <td>This paper</td>
      <td>DCR8347</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaIs117;olaIs68;syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8350</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex5059[DACR3503 at 10 ng/uL + DACR20 at 25 ng/uL];olaIs68;syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8361</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex5050[DACR3698 at 30 ng/uL + DACR20 at 25 ng/uL];olaIs68;syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8352</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>oyIs48; olaex5059; olaIs68; syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8470</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>oyIs48; olaIs117; olaIs68; syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8472</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex4087[DACR1412 at 30 ng/uL + DACR2618 at 50 ng/uL + DACR218 at 30 ng/uL]</td>
      <td>This paper</td>
      <td>DCR6841</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>oyIs48;olaIs68;syg-2(ky671);</td>
      <td>This paper</td>
      <td>DCR8758</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaEx5279[DACR3527 at 30 ng/uL + DACR20 at 25 ng/uL]; olaIs68; syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8762</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaEx5276 [DACR3780 at 5 ng/ul + DACR1412 at 20 ng/uL + DACR218 at 30 ng/uL]</td>
      <td>This paper</td>
      <td>DCR8759</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaEx5281[DACR3888 at 30 ng/uL + DACR20 at 30 ng/uL]; olaIs68; syg-2(ky671)</td>
      <td>This paper</td>
      <td>DCR8764</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaEx5283[DACR3781 at 30 ng/uL + DACR20 at 25 ng/uL]; olaIs68;syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8766</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaIs117; olaIs68; syg-1(ky652); syg-2(ky671)</td>
      <td>This paper</td>
      <td>DCR8767</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>zbIs3[cnd-1p::PH::GFP]</td>
      <td>Fan et al., 2019</td>
      <td>BV293</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>zbIs3;olaIs68;syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8772</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>kyex684[syg-2:GFP]</td>
      <td>Shen et al., 2004</td>
      <td>TV6006</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex5347[DACR1412 at 30 ng/uL + DACR218 at 30 ng/uL]</td>
      <td>This paper</td>
      <td>DCR8922</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex5332[DACR3901 at 125 ng/uL + DACR2404 at 75 ng/uL + DACR218 at 30 ng/uL]</td>
      <td>This paper</td>
      <td>DCR8894</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex5340[DACR3890 at 100 ng/uL + DACR2404 at 75 ng/uL + DACR218 at 30 ng/uL]</td>
      <td>This paper</td>
      <td>DCR8908</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex5144[DACR3492 at 50 ng/uL + DACR3493 at 50 ng/uL + DACR218 at 30 ng/uL];olaIs67</td>
      <td>This paper</td>
      <td>DCR8469</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex5195[DACR3529 at 30 ng/uL + DACR218 at 30 ng/uL];ujIs113</td>
      <td>This paper</td>
      <td>DCR8626</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaIs67;syd-2(ola341)</td>
      <td>This paper</td>
      <td>DCR6756</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>olaex3666; olaIs67;syd-2(ola341)</td>
      <td>This paper</td>
      <td>DCR6842</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>hdIs32 [glr-1::DsRed2]. gvEx173 [opt-3::GFP+ rol-6(su1006)]</td>
      <td>CGC</td>
      <td>NC1750</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
    <tr>
      <td>Strain (C. elegans)</td>
      <td>gvex173;syg-1(ky652)</td>
      <td>This paper</td>
      <td>DCR8907</td>
      <td>Strain available from D. Colón-Ramos lab</td>
    </tr>
  </tbody>
</table>

### Materials availability

See Supplementary file 1 for plasmids generated and used in this study. See Key Resources Table for C. elegans strains used in this study.

### Code availability

From previously determined adjacencies (Brittin et al., 2018; Brittin et al., 2021; Witvliet et al., 2021), cosine similarities were calculated in Excel, using the formula described in Materials and methods. For computing binary connection matrices for centrality analysis (detailed in Materials and methods below). we used the function “betweenness_bin.m” in the Brain Connectivity Toolbox (Rubinov and Sporns, 2010) of MATLAB2020.

### Maintenance of C. elegans strains

C. elegans strains were raised at 20 °C using OP50 Escherichia coli seeded on NGM plates. N2 Bristol is the wild-type reference strain used.

### Molecular biology and generation of transgenic lines

We used Gibson Assembly (New England Biolabs) or the Gateway system (Invitrogen) to make plasmids (Supplementary file 1) used for generating transgenic C. elegans strains (Key Resources Table). Detailed cloning information or plasmid maps will be provided upon request. Transgenic strains were generated via microinjection with the construct of interest at 2–100 ng/µL by standard techniques (Mello and Fire, 1995). Co-injection markers unc-122p: GFP or unc-122p: RFP were used.

We generated the syg-1 transcriptional reporter (Figure 5, Figure 5—figure supplement 1) by fusing membrane-targeted PH:GFP to a 3.5 kb syg-1 promoter region as described (Schwarz et al., 2009). The translational reporter was generated by fusing a GFP-tagged syg-1b cDNA using the same promoter (Figure 5). For cell-specific SYG-1 expression, full-length SYG-1, SYG-1 ecto (extracellular+ TM domain - amino acids 1–574, Chao and Shen, 2008) or SYG-1 endo (signal peptide+ TM domain+ cytoplasmic domain – amino acids 1–31 + 526-574) were used.

For cell-specific labeling and expression in larvae, we used an inx-1 promoter for AIB (Altun and Chen, 2008), a ceh-36 promoter for AWC and ASE (Kim et al., 2010), tdc-1, gcy-13 and cex-1 promoters for RIM (Greer et al., 2008; Piggott et al., 2011), and an opt-3 promoter for AVE (https://www.wormatlas.org).

### SNP mapping and whole-genome sequencing

We performed a visual forward genetic screen in an integrated wild type transgenic strain (olaIs67) with AIB labeled with cytoplasmic mCherry and AIB presynaptic sites labeled with GFP:RAB-3. Ethyl methanesulfonate (EMS) mutagenesis was performed and animals were screened for defects in placement of the AIB neurite, or presynaptic distribution. We screened for these same phenotypes in our reverse genetic screens as well, where we crossed the marker strain (olaIs67) to characterized mutant alleles. We screened F2 progeny on a Leica DM 5000 B compound microscope with an HCX PL APO 63 x/1.40–0.60 oil objective.

Mutants from forward genetic screens were out-crossed six times to wild type (N2) animals and mapped via single-nucleotide polymorphism (SNP) (Davis et al., 2005) and whole-genome sequencing as previously described (Sarin et al., 2008). We analyzed the results using the Galaxy platform (https://galaxyproject.org/news/cloud-map/, EMS variant density mapping workflow Minevich et al., 2012). Our forward genetic screens uncovered 19 mutants with neurite placement defects and 12 with synaptic defects, including syd-2(ola341) (Figure 7—figure supplement 1).

We also performed a reverse genetic screen with candidate adhesion molecules expressed in AIB and its primary postsynaptic partner, RIM (Schwarz et al., 2009), for defects in AIB neurite placement and presynaptic pattern. Of these mutants syg-1(ky652) and syg-2(ky671) exhibited AIB neurite placement defects.

### Confocal imaging of C. elegans larvae and image processing

We used an UltraView VoX spinning disc confocal microscope with a 60 x CFI Plan Apo VC, NA 1.4, oil objective on a NikonTi-E stand (PerkinElmer) with a Hamamatsu C9100–50 camera. We imaged the following fluorescently tagged fusion proteins, eGFP, GFP, PH:GFP (membrane-tethered), RFP, mTagBFP1, mCherry, mCherry:PH, mScarlet, mScarlet:PH at 405, 488 or 561 nm excitation wavelength. We anesthetized larval stage four animals (unless otherwise mentioned) at room temperature in 10 mM levamisole (Sigma) and mounted them on glass slides for imaging. For Figure 5 and the RIM neuron ablation images in Figure 5—figure supplement 4, larval stage three animals were imaged.

We used the Volocity image acquisition software (Improvision by Perkin Elmer) and processed our images using Fiji (Schindelin et al., 2012). Image processing included maximum intensity projection, 3D projection, rotation, cropping, brightness/contrast, line segment straightening, and pseudo coloring. All quantifications from confocal images were conducted on maximal projections of the raw data. Pseudocoloring of AIBL and AIBR was performed in Fiji. To achieve this, pixels corresponding to the neurite of either AIBL/R were identified and the rest of the pixels in the image were cleared. This was done for both neurons of the pair and the resulting images were merged. For quantifications from confocal images, n = number of neurons quantified, unless otherwise mentioned.

### Embryo labeling, imaging, and image processing

For labeling of neurites in embryos, we used membrane tethered PH:GFP or mScarlet:PH. A subtractive labeling strategy was employed for AIB embryo labeling (Figure 2—figure supplement 2A-C; Armenti et al., 2014; Moyle et al., 2021). Briefly, we generated a strain containing unc-42p::ZF1::PH::GFP and lim-4p::SL2::ZIF-1, which degraded GFP in the sublateral neurons, leaving GFP expression only in the AIB and/or ASH neurons. Onset of twitching was used as a reference to time developmental events. Embryonic twitching is stereotyped and starts at 430 min post fertilization (m.p.f) for our imaging conditions.

Embryonic imaging was performed via dual-view inverted light sheet microscopy (diSPIM) (Kumar et al., 2014; Wu et al., 2013) and a combined triple-view line scanning confocal/DL for denoising (Wu et al., 2021, also described below) described below. Images were processed and quantifications from images were done using CytoSHOW, an open-source image analysis software. CytoSHOW can be downloaded from http://www.cytoshow.org/ as described (Duncan et al., 2019).

### Triple-view line-scanning confocal/DL

We developed a triple-view microscope that can sequentially capture three specimen views, each acquired using line-scanning confocal microscopy (Wu et al., 2021). Multiview registration and deconvolution can be used to fuse the three views (Wu et al., 2016), improving spatial resolution. Much of the hardware for this system is similar to the previously published triple-view system (Wu et al., 2016), that is we used two 0.8 NA water immersion objectives for the top views and a 1.2 NA water immersion lens placed beneath the coverslip for the bottom view. To increase acquisition speed and reduce photobleaching, we applied a deep-learning framework (Weigert et al., 2018) to predict the triple-view result when only using data acquired from the bottom view. The training datasets were established from 50 embryos (anesthetized with 0.3 % sodium azide) in the post-twitching stage, in which the ground truth data were the deconvolved triple view confocal images, and the input data were the raw single view confocal images. These approaches resulted in improved resolution (270nm X 250 nm X 335 nm).

### Cell lineaging

Cell lineaging was performed using StarryNite/AceTree (Bao et al., 2006; Boyle et al., 2006; Murray et al., 2006). Light sheet microscopy and lineaging approaches were integrated to uncover cell identities in pre-twitching embryos (Duncan et al., 2019). Lineaging information for promoters is available at http://promoters.wormguides.org. Our integrated imaging and lineaging approaches enabled us to identify a promoter region of inx-19 which is expressed in the RIM neurons prior to RIM neurite outgrowth (~370 m.p.f.) and in additional neurons in later embryonic stages. The inx-19p was one of the promoters used for embryonic ablation of the RIM neurons (described in the next section).

Our integrated imaging and lineaging approach also enabled us to identify two promoters with expression primarily in neurons located at the AIB posterior neighborhood (nphp-4p and mgl-1bp). 4/4 neuron classes that were identified to have nphp4p expression are in the AIB posterior neighborhood (ADL/R, ASGL/R, ASHL/R, ASJL/R) and 2/3 neuron classes that were identified to have mgl-1bp expression are in the AIB posterior neighborhood (AIAL/R, ADFR) (http://promoters.wormguides.org). We used these promoters to drive ectopic expression of a syg-1 cDNA specifically in the posterior neighborhood.

We also used this imaging and lineaging approach to identify SYG-1 expressing neurons in the anterior and posterior neighborhoods (Figure 5—figure supplement 2). We determined cell identities by lineaging both sides of an embryo expressing the syg-1 transcriptional reporter (see the ‘Molecular Biology and generation of transgenic lines’ section). The cell identities obtained for the left and right sides of the nerve ring were consistent.

### Caspase-mediated ablation of RIM neurons

The RIM neurons were ablated using a split-caspase ablation system (Chelur and Chalfie, 2007). We generated one set of transgenic strains with co-expression of the p12 and p17 subunit of human Caspase-3, both expressed under inx-19p (termed ablation strategy 1), and another set of ablation strains with co-expression of the p12 subunit expressed under inx-19p and p17 under tdc-1p (termed ablation strategy 2) (Figure 5—figure supplement 4). L3 larvae from the RIM-ablated populations were imaged on the spinning-disk confocal microscope (described in the ‘Confocal imaging of C. elegans larvae and image processing’ section).

### Rendering of neurites and contacts in the EM datasets

From available EM datasets (Brittin et al., 2021; Cook et al., 2019; White et al., 1986; Witvliet et al., 2021) we rendered the segmentations of neuron boundaries in 2D using TrakEM2 in Fiji. TrakEM2 segmentations were volumetrically rendered by using the 3D viewer plugin in Fiji (downloaded from https://imagej.net/Fiji#Downloads) and saved as object files (.obj), or by using the 3D viewer in CytoSHOW.

To generate 3D mappings of inter-neurite membrane contact, the entire collection of 76,046 segmented neuron membrane boundaries from the JSH TEM datasets (Brittin et al., 2018; White et al., 1986) were imported from TrakEM2 format into CytoSHOW as 2D cell-name-labelled and uniquely color-coded regions of interest (ROIs). To test for membrane juxtaposition, we dilated each individual cell-specific ROI by nine pixels (40.5 nm) and identified for overlap by comparing with neighboring undilated ROIs from the same EM slice. A collection of 289,012 regions of overlap were recorded as new ROIs, each bearing the color code of the dilated ROI and labeled with both cell-names from the pair of the overlapped ROIs. These ‘contact patch’ ROIs were then grouped by cell-pair-name and rendered via a marching cubes algorithm to yield 3D isosurfaces saved in.obj files. Each of the 8852 rendered.obj files represents all patches of close adjacency between a given pair of neurons, color-coded and labeled by cell-pair name. Selected.obj files were co-displayed in a CytoSHOW3D viewer window to produce views presented in Figure 1, Figure 1—figure supplement 1 and Figure 1—figure supplement 2.

### Schematic representation of larval C. elegans

The schematic representations of larval C. elegans in Figure 1 and Figure 5—figure supplement 3 were made using the 3D worm model in OpenWorm (http://openworm.org - 3D Model by Christian Grove, WormBase, CalTech).

### Quantification and statistical analysis

#### Cosine similarity analysis for comparing AIB contacts across connectomes

We performed cosine similarity analysis (Han et al., 2012) on AIB contacts in available connectome datasets (Brittin et al., 2021; White et al., 1986; Witvliet et al., 2021). For each available adjacency dataset (Brittin et al., 2021; Moyle et al., 2021; Witvliet et al., 2021), we extracted vectors comprising of the weights of AIB contacts with neurons common to all the datasets. We then performed cosine similarity analysis on these vectors using the formula:

$$
\frac{\sum_{i=1}^{n}A_{i}B_{i}}{\sqrt{\sum_{i=1}^{n}A_{i}^{2}}\sqrt{\sum_{i=1}^{n}B_{i}^{2}}}
$$

where A and B are the two vectors under consideration with the symbol ‘‘ denoting the i-th entry of each vector. The similarity values were plotted as a heat map for AIBL and AIBR using Prism. For the datasets L1_0 hr, L1_5 hr, L1_8 hr, L2_23 hr, L3_27 hr, L4_JSH and Adult_N2U, only the neuron-neuron contacts in the EM sections corresponding to the nerve ring were used (as opposed to the whole connectome).

#### Betweenness centrality analysis

We analyzed betweenness centrality for two of the available connectomes of different developmental stages (L1 and adult) (Witvliet et al., 2021). By treating individual components (neurons) of a connectome as the vertices of a graph, we use the following definition of Betweenness Centrality for a vertex $v$,

$$
v_{zip}+v_{unzip}=\frac{S_{anterior}−S_{posterior}}{η}−\frac{T_{anterior}−T_{posterior}}{η}(1−cos\theta)
$$

Here $\lambda_{st}v$ denotes the number of shortest paths between the vertices $s$ and $t$, that include vertex $v$, whereas $\lambda_{st}$ denotes the total number of shortest paths between the vertices $s$ and $t$. We finally divide $BCv$ by $N-1N-2/2$ to normalize it to lie between 0 and 1. For our implementation we use the Brain Connectivity Toolbox (Rubinov and Sporns, 2010) of MATLAB2020, in particular, the function “betweenness_bin.m” in which we input the binary connectivity matrix (threshold = 0) (Fornito et al., 2016) corresponding to the L1 and adult connectomes (Witvliet et al., 2021). We made a Prism box plot (10–90 percentile) of betweenness centrality values of all neurons in each of the two connectomes and highlighted the betweenness centrality values for AIBL and AIBR.

#### Representation of AIB from confocal images

Since we observed that the proximal and distal neurites of AIBL and AIBR completely align and overlap (Figure 1—figure supplement 1) in confocal image stacks where the worms are oriented on their side, for representation purposes we have used the upper 50 % of z-slices in confocal image stacks to make maximum intensity projections. This shows the proximal neurite of AIBL in the context of the distal of AIBR (which has the same anterior-posterior position as the distal neurite of AIBL) (Figure 1—figure supplement 1), or vice versa. We used the same procedure for AVEL and AVER.

### Quantification of penetrance of AIB neurite placement defects and gain-of-function phenotypes

The penetrance of defects in AIB neurite placement in the anterior neighborhood in mutant (or ablation) strains was determined by visualizing the AIB neurite and scoring animals with normal or defective anterior neighborhood placement under the Leica compound microscope described. Animals in which the entire distal neurite was placed at a uniform distance from the proximal neurite, for both AIBL and AIBR, were scored as having normal AIB distal neurite placement.

The penetrance of the gain-of-function effects in ectopic SYG-1 expression strains was determined by scoring the percentage of animals showing ectopic AIB distal neurite placement in the posterior neighborhood. Animals with part (or whole) of the AIB distal neurite overlapping with the posterior neighborhood were considered as having ectopic AIB placement.

### Quantification of minimum perpendicular distance between neurites

Minimum perpendicular distances between neurites (Figure 4—figure supplement 1F, Figure 5—figure supplement 4O) were measured by creating a straight line selection (on Fiji) between the neurites (perpendicular to one of the neurites) in the region where the gap between them is estimated to be the smallest. The measurements were done on maximum intensity projections of raw confocal image stacks where the worms are oriented on their side (z-stacks acquired along left-right axis of the worm, producing a lateral view of the neurons).

### Quantification of percent detachment between neurites

The percent detachment for defasciculated neurites (AIB or AVE and RIM) is calculated by the formula % detachment = detached length (Ld) x 100/ total length (Lt) (also shown in Figure 4M). Ld is calculated by making a freehand line selection along the detached region of the RIM neurite and measuring its length and Lt is calculated by making a freehand selection along the RIM neurite for the entire length over which it contacts AIB or AVE, and measuring the length of the selection. All the measurements were performed on maximum intensity projections of confocal image stacks where the worms are oriented on their side (z-stacks acquired along left right axis of the worm, producing a lateral view of the neurons).

### Quantification of percentage of distal neurite placed in posterior neighborhood

Freehand line selections of the entire distal neurite (Lt) and only the portion of the distal neurite positioned in the posterior neighborhood (Lp) are measured using Fiji. (Lp/Lt)x100 provides the percentage of the distal neurite placed in the posterior neighborhood.

### Quantification of relative enrichment of SYG-1 reporter expression in the anterior neighborhood

Relative (anterior) enrichment of syg-1 reporter expression in embryos (Figure 5S) is calculated using the formula, relative enrichment (syg-1p) = mean anterior neighborhood intensity (Ia)/mean posterior neighborhood intensity (Ip). These measurements were done in transgenic embryos co-expressing the AIB reporter and the syg-1 transcriptional reporter. For calculation of Ip, a freehand line selection was made (using CytoSHOW, http://www.cytoshow.org/, Duncan et al., 2019) along the posterior band of syg-1 expression and mean intensity along the selection was calculated. Same was done for calculation of Ia. The ratios of Ia and Ip were plotted as relative (anterior) enrichment values (Figure 5S). These values were calculated from 3D projections of deconvolved diSPIM images acquired at intensities within dynamic range (not saturated) at timepoints during embryogenesis (485, 515, and 535 min post fertilization), when the AIB neurite grows and is placed into the posterior and anterior neighborhoods. Ia/Ip was calculated from the anterior and posterior syg-1 bands on each side of the embryonic nerve ring per embryo (number of embryos = 4, number of Ia/Ip values = 8).

### Quantification of the dorsal midline shift (chiasm) length of AIB

The dorsal midline shift (chiasm) lengths of AIB and AVE were calculated by making 3D maximum intensity projections of confocal z-stacks and orienting the neuron pair to a dorsal-ventral view. A straight line selection is made along the posterior-anterior shift of each neuron, and each arm of the ‘X’ of the chiasm was measured (using Fiji).

### Quantification of distal neurite length of AIB

The length of the distal neurite of AIB was measured by drawing a freehand line along the neurite segment occupying the distal neighborhood (including the chiasm) in maximum intensity projections of confocal image stacks where the worms are oriented on their side (z-stacks acquired along left-right axis of the worm, producing a lateral view of the neurons).

### Quantification of positions and velocities of the AIB neurite during embryogenesis

The positions of the AIB neurite in the anterior and posterior neighborhoods in Figure 3C are calculated from deconvolved maximum intensity projections of diSPIM images where the neurons are oriented in an axial view. These positions are determined by measuring the lengths along the AIB neurite from the unzippering/zippering forks to the dorsal midline. The distance of the zippering fork from the midline is subtracted from the total length of the neurite at the start of zippering, to obtain the length of the AIB neurite that has already zippered. The fraction of the length of the AIB neurite that has zippered to the initial length of the relocating AIB distal neurite, multiplied by 100, yields the percentage of the AIB neurite that has zippered at each timepoint. The reported values (in Figure 5S) of the percentages of the AIB neurite that has zippered are averages across the three independent embryo datasets (used for the Figure 3 plots). Embryos in which the AIB and RIM neurons were specifically labeled by the subtractive labeling strategy were used for the analysis. Reported measurements represent AIB neurites which were visible through the imaging window. Zippering velocity (Figure 3D) at any timepoint (t1) is defined as the difference between positions of the AIB neurite at that timepoint (t1) and the next timepoint (t2) (for which position was measured), divided by the time interval (t2-t1). These measurements are performed with CytoSHOW. To pseudocolor the neurites for representation, we used the same steps described in ‘Confocal imaging of C. elegans larvae and image processing.’.

### Quantification of the angle of exit of the developing AIB distal neurite with the ventral turn of the nerve ring in the posterior neighborhood

The angle of exit (α) of the developing AIB distal neurite is measured as the angle between straight line tangents drawn along the separating distal segment of AIBL and the proximal neurite of AIBR and vice versa. These measurements are performed on deconvolved maximum intensity projections of diSPIM images where the neurons are oriented in an axial view. The angle of ventral turn of the nerve ring (β) is measured as the angle between straight line tangents drawn along segments of the nerve ring on either side of the ventral bend of the nerve ring in the posterior neighborhood (see Figure 2—figure supplement 2I,J). β is measured from images of embryos with proximal neighborhood labeled with nphp-4 promoter (see Results and http://promoters.wormguides.org). All measurements are performed using CytoSHOW.

### Imaging and representation of synaptic protein RAB-3 in AIB in embryos

Time-lapse imaging of presynaptic proteins RAB-3, CLA-1, and SYD-2 in AIB in embryos was performed using diSPIM (Wu et al., 2013). To visualize the distribution of RAB-3 and CLA-1 along the neurite we straightened the distal neurite of each AIB neuron from maximum intensity projections where the AIB neurons are oriented in the axial (Figure 7) and lateral view (Figure 7—figure supplement 1), respectively.

### Quantification of RAB-3 distribution in Syg-1(ky652) larvae

The line intensity plot in Figure 7—figure supplement 3M was constructed in Fiji by drawing freehand line selections along adhered and detached regions of the AIB neurite and using the Analyze > Plot Profile function. The mean intensities along ‘Adhered’ and ‘Detached’ regions were subtracted from the corresponding mean cell body intensities and plotted in Figure 7—figure supplement 3N.

### Quantification of nerve ring width from larval stage animals

The nerve ring was visualized using a 5.6 kb promoter of cnd-1 (Shah et al., 2017) driving membrane-targeted GFP (PH:GFP) in wildtype and syg-1(ky652) mutant animals. Measurements were done on confocal image stacks where the worms are oriented on their side (z-stacks acquired along left-right axis of the worm, producing a lateral view of the neurons). On each side of the worm, a straight line selection along the anterior-posterior axis from one edge of the labeled nerve ring to the other was defined as the nerve ring width.

### Quantification of length of the dorsal midline shift (chiasm) from EM images

From a segmented EM dataset of the L4 larva JSH (Brittin et al., 2018; White et al., 1986), we calculated the number of z-slices containing segmented regions of the anterior-posterior shift (that forms the chiasm) of AIBL. We multiplied this number with the z-spacing of the dataset (60 nm) to obtain the anterior-posterior distance that the AIBL shift spans (dz). We then calculated the x-y distance between the segmented regions of the AIBL shift in the topmost and bottommost z-slice(dx-y). We calculate the length of the shift in 3D (l) using the formula

$$
l=\sqrt{d_{z}^{2}+d_{x-y}^{2}}
$$

The same measurements were repeated for the length of the dorsal midline shift of AIBR.

### Statistical analyses

Statistical analyses were conducted with PRISM seven software. For each case, the chosen statistical test is described in the figure legend and ‘n’ values are reported. Briefly, for continuous data, comparisons between two groups were determined by unpaired two-tailed t-test and comparisons within multiple groups were performed by ordinary one-way ANOVA. Error bars were reported as standard error of the mean (SEM). For categorical data, groups were compared with two-sided Fisher’s exact test. The range of p-values for significant differences are reported in the figure legend. The Cohen’s d statistic was determined for comparisons between continuous datasets with statistically significant differences, to obtain estimates of effect sizes.
