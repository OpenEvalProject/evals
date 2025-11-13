# Bright multicolor labeling of neuronal circuits with fluorescent proteins and chemical tags

## Authors

- Richi Sakaguchi<sup>1</sup> ([ORCID: 0000-0002-3988-6385](https://orcid.org/0000-0002-3988-6385))
- Marcus N Leiwe<sup>1</sup> ([ORCID: 0000-0002-3493-7091](https://orcid.org/0000-0002-3493-7091))
- Takeshi Imai<sup>1</sup> ([ORCID: 0000-0002-8449-0080](https://orcid.org/0000-0002-8449-0080)) †

### Affiliations

1. Graduate School of Medical Sciences Kyushu University Fukuoka Japan
2. Graduate School of Biostudies Kyoto University Kyoto Japan
3. Laboratory for Sensory Circuit Formation RIKEN Center for Developmental Biology Kobe Japan

† Corresponding author

## Abstract

The stochastic multicolor labeling method ‘Brainbow’ is a powerful strategy to label multiple neurons differentially with fluorescent proteins; however, the fluorescence levels provided by the original attempts to use this strategy were inadequate. In the present study, we developed a stochastic multicolor labeling method with enhanced expression levels that uses a tetracycline-operator system (Tetbow). We optimized Tetbow for either plasmid or virus vector-mediated multicolor labeling. When combined with tissue clearing, Tetbow was powerful enough to visualize the three-dimensional architecture of individual neurons. Using Tetbow, we were able to visualize the axonal projection patterns of individual mitral/tufted cells along several millimeters in the mouse olfactory system. We also developed a Tetbow system with chemical tags, in which genetically encoded chemical tags were labeled with synthetic fluorophores. This was useful in expanding the repertoire of the fluorescence labels and the applications of the Tetbow system. Together, these new tools facilitate light-microscopy-based neuronal tracing at both a large scale and a high resolution.

## Introduction

Neuronal circuits are the basis for brain function. Therefore, the reconstruction of neuronal wiring diagrams is key to understanding circuit function. Fluorescence imaging has been a powerful approach in visualizing the three-dimensional structure of neuronal morphology. In particular, fluorescent proteins are useful for labeling genetically-defined neuronal populations. In recent years, a number of tissue-clearing methods have been developed, and these have been optimized for use with fluorescent proteins and deep-tissue antibody staining (Hama et al., 2011; Chung et al., 2013; Ke et al., 2013; Susaki et al., 2014; Richardson and Lichtman, 2015). These new tools have expanded the scale of the available technologies for fluorescence imaging to whole-organ and whole-organism levels.

It is still difficult, however, to dissect and trace an individual neuron from a brain sample labeled with a single type of fluorescent protein. One way to overcome this problem is to improve the spatial resolution. Recently, we developed a tissue-clearing agent for high-resolution three-dimensional fluorescence imaging, named SeeDB2 (Ke et al., 2013). SeeDB2 was designed to minimize spherical aberrations, allowing for high-resolution imaging including super-resolution microscopy. In this approach, there was much improvement in the z-resolution, a critical factor for dissection of neuronal fibers crossing over along the z-axis. Similarly, expansion microscopy is also a promising new approach used to improve resolution in three-dimensional fluorescence imaging (Chen et al., 2015; Ku et al., 2016; Tillberg et al., 2016; Chang et al., 2017).

Another approach to the dissection of neuronal circuits is multicolor labeling. To facilitate the dissection of individual neurons, a transgenic multicolor labeling method, Brainbow, has been developed, in which three different fluorescent proteins were expressed in a stochastic manner (Livet et al., 2007; Cai et al., 2013; Loulier et al., 2014). Brainbow used the Cre-loxP system to express one of the three fluorescent protein genes stochastically in a transgene. When multiple copies of the transgene cassette are introduced, stochastic choices will result in a combinatorial expression of these three genes with different copy numbers, producing dozens of color hues.

Although the Brainbow concept is powerful for discriminating between numerous neurons using light microscopy, the existing Brainbow methods are of limited use for neuronal tracing. This is because the stochastic and combinatorial expression of fluorescent proteins is possible only at low copy number ranges for the transgenes, so that the expression levels of the fluorescent proteins were not sufficiently high for bright and high-resolution imaging of axons and dendrites. Therefore, many of the previous studies were forced to use subsequent antibody staining to produce reliable neuronal tracing. In the present study, we utilized the Tet-Off system (Tetbow) to develop a multicolor labeling method with enhanced expression. As vector (plasmid and virus)-mediated gene transfer has become a versatile tool in modern neuroscience, we aimed to perform multicolor labeling using these tools. As a proof-of-concept experiment, we demonstrated the ability to trace axons of individual neurons on the scale of several millimeters in the mouse olfactory system. To improve the stability of the fluorescence labels after harsh tissue-clearing treatment, we also developed a Tetbow system with chemical tags. When combined with the advances in the growing field of tissue-clearing techniques, these new multicolor labeling strategies should facilitate neuronal tracing at higher densities and resolutions.

## Results

### A trade-off between expression levels and color variation

Earlier Brainbow methods utilized transgenic animals for stochastic multicolor labeling. They utilized the Cre-loxP system, in which DNA recombination resulted in a stochastic selection of one fluorescent protein gene out of three (or more) choices. When multiple copies of the Brainbow transgene were introduced into the genome, stochastic recombination produced a variety of color hues based on different copy numbers of expressed fluorescent protein genes (collectively called XFPs) (Livet et al., 2007). In recent years, however, plasmid or virus vector-mediated gene transfer has become a more versatile strategy in neuroscience. We therefore tried to optimize a multicolor labeling method for vector-mediated gene transfer.

Previously, an adeno-associated virus (AAV)-mediated Brainbow method (AAV-Brainbow) has been reported (Cai et al., 2013). However, in the vector-mediated gene transfer, the Cre-loxP system is not essential for the stochastic and combinatorial expression of XFP genes (Kobiler et al., 2010; Weber et al., 2011; Siddiqi et al., 2014). We can easily make color variations by introducing a mixture of three different XFP constructs: as long as the copy number of the introduced genes is small, labeled neurons will still produce a variety of colors irrespective of whether the Cre-loxP system is used or not (Figure 1A–C). It should be noted, however, that color variation reduces as the copy number of the introduced genes increases. We can estimate the optimum copy number of the introduced XFP genes as follows. We considered that the number of introduced genes will follow a Poisson distribution (Kobiler et al., 2010). When three different XFP genes are introduced at 20 copies/cell/color on average, a similar number of copies will be introduced into each neuron, and only a small degree of color variation will be generated (Figure 1C). By contrast, if the copy number is too small, many of the neurons will express just one XFP gene (Figure 1A). When these three genes are introduced at an average 2 copies/cell/color, much larger color variations will be produced (Figure 1B).

![Figure 1.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig1-v1.jpg)

**Figure 1.:** Stochastic representation of the vector-mediated multicolor labeling strategy. Here we assume that the copy numbers of introduced vectors follow a Poisson distribution. In a plasmid or virus-mediated gene transfer method, we do not need to use the Cre-loxP system. Rather, it is important to limit the number of genes introduced into each cell. For example, in theory, an average of 2 copies/cell/color can result in the stochastic expression of three different genes (B). If we introduce a copy number that is too small (e.g. an average of 0.2 copies/cell; A), only one of the three genes will be expressed in most cells. If too many genes are introduced in each cell (e.g. an average of 20 copies/cell; C), color variations will be reduced because many of the neurons will express a similar number of XFP genes. The use of the Cre-loxP system alone cannot solve this problem. Simulations of the expected color variations that are based on the various Poisson distributions (middle) are shown as ternary plots (100 plots/condition, right panel). The numerical data are presented in Figure 1—source data 1. Note that many of the plots are overlapping at the edge of the triangle in (A). Three different XFPs are shown in red (R), green (G), and blue (B). (D) The difference between two colors represented as Euclidean distance in 3D color space. For example, a difference between colors a and b is represented as the distance, d. (E) Box plots of Euclidean distances in all pairs of plots in 3D space in relation to copy number. The horizontal lines within each box represents the median, the box represents the interquartile range, and the whiskers show the minimum and maximum values. (F) A cartoon illustrating the cells inside (X%) and outside the threshold Euclidean distance. The cells outside (100 – X %) are considered to be discernable. (G) The percentage of discernable cells for each threshold d and each copy number. Simulation data used for (E) and (G) are provided in Figure 1—source data 1. (H) The color discrimination abilities of experienced researchers. Tests are explained in Figure 1—figure supplement 1. Mean ± SD are indicated in red. When threshold d is 0.1, the score was 94.5 ± 1.73% (mean ± SD). Score data are in Figure 1—source data 2.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (a) a flowchart describing the generation of the color sets and the user choices. The euclidean distances chosen as threshold values were 0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.1, 0.15, 0.2, and 0.25. To prevent color intensity influencing decisions, the intensity was randomized in the 50–100% range for each trial. (b) a schematic showing either the ‘crossed’ (top) or ‘straight’ (bottom) decisions for the ‘same’ sets of colors that the user has to make. (c) examples showing the choices at various thresholds. White arrows display the correct decisions.

We wanted to determine the optimum copy number of the expressed XFP genes on the basis of this simulation. We plotted the color values for cells in the color-coding space after intensity normalization (total intensity = 1). In this coding space, each dimension represents the intensity of one of the three colors (Red, Green, and Blue in pseudocolor representation). The mean Euclidean distance (d) for two randomly chosen cells was greater when the copy number was lower (Figure 1D,E), but this does not necessarily mean that we can discriminate between many cells, as the two cells are more likely to become the same color when copy number is too low (Figure 1A). We therefore calculated the probability that two randomly chosen cells are discriminated on the basis of a given threshold distance in the color-coding space. Here we considered that cells within the threshold distance (d) from a reference are indiscriminable in the color-coding space; cells outside of the threshold distance were considered discriminable from the reference (Figure 1F). In our simulation, when we assumed a threshold distance of 0.1, 95.3% of cells could be discriminated from a given cell when XFP genes were expressed at 2 copies/color/cell (Figure 1G). We also found that experienced researchers can discriminate two colors separated by 0.1 Euclidean distances in the color-coding space at 94.5 ± 1.73% accuracy (mean ± S.D.; Figure 1H and Figure 1— figure supplement 1). Thus, ~2 copies/color/cell is the optimum when the color hues are judged visually by human experimenters.

We evaluated this prediction using the in utero electroporation of plasmid vectors into layer 2/3 cortical pyramidal neurons (electroporated at embryonic day 15). We introduced a mixture of three separate plasmid vectors encoding mTurquoise2 (blue), EYFP (green), and tdTomato (red) genes under a CAG promoter. When these plasmids were expressed at high copy numbers (CAG High; DNA solution introduced was 1 μg/μL/plasmid; 3 μg/μL in total; see 'Materials and methods' section for details), only small color variations were produced (Figure 2A,C). When the DNA concentrations were reduced (CAG Low; 0.25 μg/μL/plasmid), the color variation increased (Figure 2B), but the overall fluorescence levels were much reduced (Figure 2E). Thus, there is a trade-off between the expression levels of fluorescent proteins and color variations, and this is the reason why the previous Brainbow methods were unable to produce color variations that were bright enough for labeling.

![Figure 2.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig2-v1.jpg)

**Figure 2.:** (A) L2/3 neurons labeled with CAG-Turquoise2, EYFP, and tdTomato (1 or 0.25 μg/μL each). When each plasmid was introduced at 0.25 μg/μL, the color variation was increased, but the fluorescence levels were reduced. Enhanced images are shown on the right. (B) CAG-tTA, TRE- Turquoise2, EYFP, and tdTomato were introduced at 0.25 μg/μL each (Tetbow construct; see Figure 2—figure supplement 1). In utero electroporation was performed at E15 and the mice were analyzed at P21. Experiments were performed in parallel, and image acquisition conditions were the same for (A) and (B). Scale bars represent 50 μm. (C, D) Color variations made by three CAG vectors (C) vs. Tetbow vectors (D) are shown in ternary plots. Fluorescence intensities were vector normalized and the fluorescence intensity ratios were compared. Fluorescence intensities at neuronal somata were used for the quantitative comparison. Note that the color variations are small with high-copy CAG vectors, whereas color variations are high with the Tetbow vectors (n = 249–728 cells per group from three sets of experiments for each of the samples). Fluorescence intensity data used for (C), (D), and (F) are provided in Figure 2—source data 1. (E) Boxplot of median EYFP fluorescence intensities (normalized to the median of CAG (0.25 µg/µl). A D’Agostino and Pearson Normality Test showed that the data were not normally distributed (p<0.0001). EYFP signals in (A) and (B) were compared. The horizontal line in each box represents the median location, the box represents the interquartile range, and the whiskers show the minimum and maximum values. p*<0.05, p***<0.001 (Kruskal-Wallis with Dunn’s post hoc test, n = 104–276 per sample). The data are from one set of experiments performed in parallel. We analyzed three independent sets of experiments and obtained similar results. The fluorescence intensity data used for (E) are in Figure 2—source data 2. (F) Percentage of discernable cells in the condition of each threshold d and each copy number. p***<0.001 (two-way ANOVA with Tukey-Kramer post hoc test, n = 249–728 per sample).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Plasmid maps for CAG-tTA, TRE-mTurquoise2/EYFP/tdTomato. To ensure adequate plasmid yield in Escherichia coli, the TRE expression cassette was transferred to a high-copy plasmid, pBluescriptII (SK+). To enhance the stability of mRNA, a WPRE sequence is added to the 3’’ UTR. We used cytosolic XFPs, because cytosolic XFPs are much brighter than membrane localized XFPs (data not shown).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** In utero electroporation was used to label M/T cells at E12 and mice were analyzed at P8. Whole brains were cleared with SeeDB2G and imaged with confocal microscopy. Low and high magnification images in axons of M/T cells are shown. High magnification images show the axon collaterals in the piriform cortex. (A) Tetbow constructs were introduced. Maximal intensity projection images of confocal images are shown (left: 1330.11 μm thick, right: 23.97 μm thick). (B) CAG-iCre (0.1 μg/μL), EF1a-BbTagBY (0.5 μg/μL), and EF1a-BbChT (0.5 μg/μL) were introduced. In utero electroporation was performed at E15 and mice were analyzed at P21. Experiments were performed in parallel, and image acquisition conditions were the same in (A) and (B). Note, however, that the Brainbow constructs use an EF1a promoter and membrane-bound XFPs, whereas Tetbow uses a TRE promoter and cytosolic XFPs. We also tested the CAG-Brainbow3.0 in the cerebral cortex, but labeling signals were much lower than Tetbow (data not shown). Scale bars are 1 mm (left) and 20 μm (right). Three samples were imaged in the same condition. A representative sample is shown for (A). The brightest sample is shown in (B), as we could not find clear signals at axons in the two remaining samples after clearing. OB, olfactory bulb; OT, olfactory tubercle, PC, piriform cortex.

### Tetbow: multicolor labeling with enhanced expression levels

We therefore wanted to enhance the expression levels of fluorescent proteins while maintaining the required low copy numbers of XFP genes. Recent studies indicated that the tetracycline response element (TRE) promoter ensures much higher expression levels than the CAG promoter when expressed with a tetracycline trans-activator (tTA) (Madisen et al., 2015; Sadakane et al., 2015). We therefore used the tTA-TRE (Tet-Off) system instead of a common CAG promoter. We also introduced a Woodchuck hepatitis virus posttranscriptional regulatory element (WPRE) sequence in the 3’′ UTR of XFP genes to improve their expression levels. Earlier Brainbow techniques used membrane-bound XFPs because unmodified XFPs labeled the somata too brightly and affected the tracing of nearby neurites (Cai et al., 2013). However, this problem can be easily solved by minimizing spherical aberration in microscopy by using an index-matched clearing agent, SeeDB2 (Ke et al., 2016). Furthermore, unmodified XFPs label axons and dendrites much more brightly than the membrane-bound ones (data not shown). We therefore used unmodified XFPs instead of membrane-bound XFPs. These new set of constructs (named Tetbow; Figure 2—figure supplement 1) achieved much higher XFP expression levels when compared with the CAG-promoter plasmids (Figure 2B). When we quantified the expression levels of EYFP, we observed a six-fold increase in fluorescence levels (Figure 2E; CAG 0.25 μg/μL vs. Tetbow 0.25 μg/μL; n = 104 and 260, respectively, p<0.0001, Kruskal Wallis with Dunn’s post hoc test). Tetbow allowed for much more robust multicolor labeling than the Brainbow constructs when introduced by in utero electroporation, allowing more reliable axon tracing (Figure 2—figure supplement 2).

Owing to the enhanced expression, the Tetbow system achieved bright labeling (Figure 2E) while maintaining the color variations produced by low copy numbers of XFP genes. When CAG-XFP genes were introduced at high concentrations (1 μg/μL each), the color variations were small; by contrast, the Tetbow constructs (0.25 μg/μL) produced much larger variations (Figure 2D). In the color discrimination analysis, we confirmed that different cells are better discriminated by Tetbow than in the CAG High condition (Figure 2F).

We further tried to determine the optimum concentration of plasmids for Tetbow when labeled with in utero electroporation. Among the four plasmid concentrations we tested (0.05, 0.1, 0.25, and 0.5 μg/μL each), color discrimination performance was comparable. Paradoxically, however, the expression levels of XFP were the highest at 0.25 μg/μL each, not at 0.5. We therefore considered the possibility that a moderate expression level of tTA is critical for the optimum expression. When 0.1, 0.25, and 0.5 μg/μL of CAG-tTA plasmid was co-introduced with 0.25 μg/μL each of TRE-XFP plasmids, the highest expression level was found with 0.1 μg/μL CAG-tTA (Figure 3D–F). Thus, too high a concentration of tTA leads to the suppression of TRE-XFP genes. Consistent with this assumption, when the WPRE sequence was added to the CAG-tTA plasmid, the expression level of TRE-XFP genes was reduced (Figure 3—figure supplement 1). Thus, the expression level of tTA needs to be moderate to achieve the highest expression of TRE-XFP genes.

![Figure 3.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig3-v1.jpg)

**Figure 3.:** (A–C) Plasmid concentrations for the four Tetbow vectors (CAG-tTA and three TRE-XFP vectors) were tested at 0.05, 0.1, 0.25, and 0.5 μg/μL. (B) Boxplot of median EYFP fluorescence intensities (normalized to the median of Tetbow (0.05 µg/µl)). A D’Agostino and Pearson normality test showed that the data were not normally distributed (p<0.0001). The horizontal bar within each box represents the median fluorescence intensity, the box represents the interquartile range, and the whiskers show the minimum and maximum values. p**<0.01, p***<0.001 (Kruskal Wallis with Dunn’s post hoc test, n = 273–524 per sample). (C) Percentage of discernable cells for each of the threshold d and dilution conditions. There was no significant difference between each d condition (two-way ANOVA with Tukey-Kramer post hoc test) (n = 273–524 per sample). The fluorescence intensity data used for (B) and (C) are available in Figure 3—source data 1. (D–F) L2/3 neurons labeled with Tetbow. Only tTA concentrations were changed (0.1, 0.25, or 0.5 μg/μL). Decrease in tTA concentrations enhanced signal intensities. (E) Boxplot of median EYFP fluorescence intensities (normalized to the median of Tetbow (tTA: 0.5 µg/µl)). A D’Agostino and Pearson normality test showed that the data were not normally distributed (p<0.0001). The horizontal bar within each box represents the median location, the box represents the interquartile range, and the whiskers show the minimum and maximum values. p**<0.01, p***<0.001 (Kruskal Wallis with Dunn’s post hoc test, n = 356–414 per sample). (F) Percentage of discernable cells for each threshold d and each dilution condition. p*<0.05, p***<0.001 (two-way ANOVA with Tukey-Kramer post hoc test, n = 356–414 per sample). The fluorescence intensity data used for (E) and (F) are available in Figure 3—source data 2.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** We tried to enhance the expression levels of XFPs by adding WPRE to the 3’′-UTR of the tTA gene, but the expression levels of XFPs were decreased with WPRE. The imaging conditions were the same as for Figure 2.

### High-resolution 3D imaging with tissue clearing

We described the use of SeeDB2 as a tissue-clearing agent (Ke et al., 2016). SeeDB2 is designed to minimize spherical aberrations for glycerol (SeeDB2G) or oil (SeeDB2S) immersion objective lenses, making high-resolution 3D imaging possible. Furthermore, various fluorescent proteins were best preserved in SeeDB2, much more so than in commercialized mounting media or other tissue-clearing agents (Ke et al., 2016). In high-resolution imaging, we must obtain photons from a limited volume, and thus the fluorescence intensity must be sufficiently high. Therefore, the combination of Tetbow and SeeDB2 is ideal for high-resolution volumetric multicolor imaging.

We introduced Tetbow constructs into Layer 2/3 neurons in the cerebral cortex using in utero electroporation. After clearing with SeeDB2G, the fluorescence levels of XFPs with Tetbow were strong enough to allow visualization of the fine detail of neuronal morphology in 3D (Figure 4A and Video 1). When we analyzed adult brain slices (P70), detailed structures of dendritic spines (Figure 4B, Figure 4—figure supplement 1, and Video 2) and axonal boutons (Figure 4C) were clearly visualized with Tetbow. It should be noted that we obtained these high-resolution images of synaptic structures using solely native fluorescence of XFPs, with no antibody staining.

![Figure 4.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig4-v1.jpg)

**Figure 4.:** Volume rendering of Layer 2/3 cortical pyramidal neurons labeled with Tetbow (P70). In utero electroporation was used to label L2/3 neurons at E15. Brain slices were cleared with SeeDB2G and imaged with confocal microscopy. Different neurons were brightly labeled with different colors. Representative images are shown from four independent experiments. (A) Low- and high-magnification images in Layer 2/3 (45.16 μm thick). The four panels on the right indicate each of the three single channel fluorescence images. See also Video 1. (B) Dendrites and dendritic spines were brightly labeled with various colors with Tetbow. A volume-rendered image (18.65 μm thick) is shown. See also Video 2. (C) Axons and axonal boutons were clearly visualized with Tetbow. A volume rendered image (23.01 μm thick) is shown. Note that the synaptic-scale structures were clearly visualized with the native fluorescence of XFPs, without antibody staining. Scale bars are 20 μm (A, left) and 5 μm (A, right and B, C).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Shallow and deep images of L2/3 cortical pyramidal neurons labeled with Tetbow in a thick brain slice (1 mm). In utero electroporation was used to label L2/3 neurons at E15. Brain slices were cleared with SeeDB2G and imaged with confocal microscopy. Maximal intensity projection images of confocal images are shown (4.96 μm thick). Dendritic spines were visualized in the deep section of thick slices. Scale bars are 5 μm.

![Video 1.](https://cdn.elifesciences.org/articles/40350/elife-40350-video1.mp4.jpg)

**Video 1.:** Tetbow plasmids were introduced at E15 and the cerebral cortex was analyzed at P70. See legends to Figure 4A.

![Video 2.](https://cdn.elifesciences.org/articles/40350/elife-40350-video2.mp4.jpg)

**Video 2.:** Tetbow plasmids were introduced at E15 and the cerebral cortex was analyzed at P70. See legends to Figure 4B.

To evaluate the versatility of Tetbow, we also tested other types of neurons using in utero electroporation. For example, we were able to label brightly mitral and tufted (M/T) cells in the olfactory bulb with Tetbow. It is known that each glomerulus in the olfactory bulb is innervated by 20–50 M/T cells (Ke et al., 2013; Imai, 2014). When we looked at each glomerulus, dendrites from different mitral cells were clearly visualized and were distinguishable by their different colors (Figure 5 and Video 3). Thus, Tetbow can be used to analyze the detailed dendrite wiring diagram of individual M/T cells, including ‘sister’ M/T cells, which are connected to the same glomerulus.

![Figure 5.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig5-v1.jpg)

**Figure 5.:** M/T cells in the olfactory bulb (P7) were labeled with Tetbow. A volume-rendered image is shown (84.07 μm thick). Each mitral cell was labeled with unique colors facilitating the identification of individual neurons at high resolution. Note that dendritic tufts from different neurons are clearly distinguishable with different colors in the high-magnification image (bottom). Representative data from one out of three independent experiments are shown here. See also Video 3. Scale bars are 100 μm (top) and 20 μm (bottom). Fluorescence signals at M/T cell somata are intentionally saturated in this image so that the fine details of dendrites are better visualized.

![Video 3.](https://cdn.elifesciences.org/articles/40350/elife-40350-video3.mp4.jpg)

**Video 3.:** Tetbow plasmids were introduced at E12 and the olfactory bulb samples were analyzed at P7. See legends to Figure 5.

### Tetbow with chemical tags

Aqueous tissue-clearing agents are useful for large-scale three-dimensional imaging with fluorescent proteins. However, to clear lipid-rich myelinated axons completely, harsh clearing treatments, such as the use of detergents, solvents, and heating, are inevitable (Dodt et al., 2007; Chung et al., 2013; Renier et al., 2014; Susaki et al., 2014; Murray et al., 2015). Indeed, there is a trade-off between the transparency of the tissues and damage to the tissues and fluorescent proteins (Ke et al., 2013; Ke et al., 2016). For example, most of the solvent-based clearing methods, such as BABB, quench fluorescent proteins. To overcome this problem, chemical tags could be a promising alternative to fluorescent proteins (Kohl et al., 2014; Sutcliffe et al., 2017). Genetically encoded chemical tags, such as SNAP, Halo, CLIP, and TMP form covalent bonds with their cognate substrate, and fluoresce with synthetic labels. The molecular weights of these ligands are relatively small, allowing easy penetration into thick tissues. Once they form covalent bonds with their substrates, the fluorescence remains stable even under harsh clearing conditions.

We tested Tetbow multicolor labeling with three different chemical tags, SNAP, Halo, and CLIP (Figure 6—figure supplement 1). We introduced these three chemical tag genes into L2/3 cortical pyramidal neurons using in utero electroporation. Brains were fixed, and the three chemical tags were visualized with synthetic fluorescence labels: SNAP-Surface 488, HaloTag TMR Ligand, and CLIP-Surface 647, respectively (Figure 6A). Like fluorescent proteins, chemical tags allowed for the robust multicolor labeling of neurons using the Tetbow system (Figure 6B). Owing to the low molecular weight of the substrates, 1 mm-thick mouse brain samples were efficiently labeled (Figure 6—figure supplement 2). After tissue clearing with solvent-based tissue clearing agents, 3DISCO or BABB, fluorescent proteins were largely quenched (data not shown) (Ke et al., 2013); synthetic fluorophores bound to chemical tags, however, were bright and stable under these clearing conditions (Figure 6B).

![Figure 6.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig6-v1.jpg)

**Figure 6.:** (A) Tetbow labeling with chemical tags. We used SNAP, CLIP, and Halo tags for Tetbow labeling. These chemical tags form covalent bonds with their substrates, which contain chemical fluorophores. These chemical labels are stable even under harsh clearing conditions. See Figure 6—figure supplement 1 for plasmid construction. (B) L2/3 neurons labeled with SNAP, Halo, and CLIP tags were visualized with SNAP-Surface 488, HaloTag TMR Ligand, and CLIP-Surface 647 (P21), respectively. Brain tissue was cleared with SeeDB2G, BABB, or 3DISCO. Note that a fluorescent protein, mTurquoise2, was largely quenched by BABB and 3DISCO whereas chemical tags with synthetic dyes remained stable. Scale bars are 50 μm. Data for each condition were obtained from sections from the same animal. This process was replicated for three animals.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Plasmid maps for a chemical-tag Tetbow. Chemical-tag expression cassettes are basically the same as those for XFPs.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** L2/3 neurons labeled with SNAP, Halo, and CLIP tags were visualized with SNAP-Surface 488, HaloTag TMR Ligand, and CLIP-Surface 647, respectively. Chemical tag genes were introduced by in utero electroporation at E15. A 1-mm-thick brain slice (P21) was cleared with SeeDB2G. Scale bars are 50 μm.

### Tetbow AAVs

AAVs are also becoming a versatile gene delivery tool in neuroscience. However, the size of the conventional Brainbow gene cassettes was too large to allow them to be packaged into an AAV vector (<5 kb). For this reason, a previous study divided the Brainbow cassette into two separate AAVs with two XFP genes each, and employed Cre-loxP recombination (Cai et al., 2013). As described above, however, the Cre-loxP system is not needed to achieve multicolor labeling using AAV-mediated gene expression. Using the Tetbow strategy (i.e. multiple AAV vectors with different XFP genes), we can solve the size problem, and achieve improved multicolor labeling using simplified DNA constructs.

We generated four separate AAV vectors carrying SYN1-tTA, TRE-mTurquoise2, TRE-EYFP, and TRE-tdTomato genes (Figure 7—figure supplement 1). The human SYNI promoter was used to express tTA specifically in neurons. These four AAV vectors (serotype AAV2/1) were injected into the cerebral cortex of adult mice (P56) and analyzed two weeks later. We found a stochastic and combinatorial expression of the encoded fluorescent proteins in Layer five neurons when injected at 4 × 108 gc/mL of AAV-SYN1-tTA and 3 × 1010 gc/mL of AAV-TRE-XFPs (Figure 7A). As expected from our simulation (Figure 1), the virus titer was critical for producing color variations. Higher virus titers led to reduced color variations (Figure 7B, right). In the cerebral cortex, 1–3 × 1010 gc/mL of AAV-TRE-XFPs was found to be optimum on the basis of the resultant expression levels and color variations (Figure 7C and D), but the optimum range may be different for different cell types (Figure 7—figure supplement 2), injection volumes, or virus serotypes. Expression levels were sufficiently high for high-resolution imaging of neuronal morphology, including the visualization of dendritic spines (Video 4). It should be noted, however, that the expression of Tetbow AAVs can lead to toxic effects on cellular functions after a prolonged incubation period, as a result of the extremely high levels of expression. For example, cortical neurons started to show an aggregation of XFPs and displayed morphological abnormalities 4 weeks after virus injection, whereas olfactory bulb neurons were best visualized at 4 weeks. Thus, the optimum incubation time may be different for different cell types.

![Figure 7.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig7-v1.jpg)

**Figure 7.:** (A) Layer five pyramidal neurons in the cerebral cortex labeled with Tetbow AAVs. Tetbow AAVs (serotype AAV2/1) were injected at P56 and analyzed two weeks later. Brain slices were cleared with SeeDB2G. The images display the native fluorescence of XFPs under SeeDB2G clearing. Low- and high-magnification images (89 μm thick, volume rendering) are shown. Scale bars are 100 μm on the left, and 10 μm on the right. (B) The optimization of virus titer conditions. Various titers of TRE-mTurquoise2, TRE-EYFP and TRE-tdTomato (1 × 1010, 3 × 1010, 1 × 1011 gc/mL) were injected at P56 and analyzed two weeks later. The tTA titer was 4 × 108 gc/mL throughout. (C) Boxplots of EYFP fluorescence intensities at the cell bodies (normalized to the median of 1 × 1010 gc/mL). A D’Agostino and Pearson normality test showed that the data were not normally distributed (p<0.0001). The horizontal line within each box represents the median location, the box represents the interquartile range, and the whiskers represent the minimum and maximum values. p*<0.05, p***<0.001 (Kruskal-Wallis with Dunn’s post hoc test, n = 163–220 per sample). (D) The percentage of discernable cells for each threshold d and each titer condition. p*<0.05, p**<0.01, p***<0.001 (two-way ANOVA with Tukey-Kramer post hoc test, n = 163–220 per sample). Fluorescence intensity data used for (B) to (D) are available in Figure 7—source data 1.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** Plasmid maps for the pAAV vectors used in this study. TRE-XFP expression cassettes are basically the same as in in utero electroporation. The tTA gene was expressed under the SYN1 promoter to ensure neuronal expression.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig7-figsupp2-v1.jpg)

**Figure 7—figure supplement 2.:** (A) CA1 neurons in the hippocampus labeled with Tetbow AAVs. See also Video 4. (B) Granule cells in the olfactory bulb labeled with Tetbow AAVs. Tetbow AAVs were injected at P56 and analyzed two weeks later. Brain slices were cleared with SeeDB2G. Note that fine dendritic spines are clearly visualized with different color hues. Images are native fluorescence of XFPs under SeeDB2G clearing. Maximal intensity projection images of confocal images are shown (234.62 μm thick for (A), and 272 μm thick for (B)). Scale bars are 100 μm in the panels on the left, and 5 μm in those on the right. Fluorescence intensity data used for (B)-(D) are available in Figure 7—source data 1.

![Video 4.](https://cdn.elifesciences.org/articles/40350/elife-40350-video4.mp4.jpg)

**Video 4.:** Tetbow AAVs were injected to the hippocampus at P56 and analyzed after two weeks. See legends to Figure 7—figure supplement 2.

### Long-range axon tracing with Tetbow

The bright multicolor labeling method, Tetbow, is particularly useful for the analysis of long-range axonal projection of a population of neurons. To test the utility of Tetbow, we focused on mitral and tufted (M/T) cells in the olfactory bulb, which project axons (up to several millimeters) to the olfactory cortex, including the anterior olfactory nucleus, olfactory tubercle, piriform cortex, cortical amygdala, and lateral entorhinal cortex. Previous studies have performed axon tracing on populations of M/T cells from glomeruli in the olfactory bulb using dye injections (Nagayama, 2010; Sosulski et al., 2011), but these studies could not fully dissect individual axons. Other studies performed single-cell axon tracing using hundreds of serial brain sections, but these analyses were highly laborious and time-consuming (Ghosh et al., 2011; Igarashi et al., 2012). Owing to these limitations, we do not yet understand fully how the odor inputs into individual M/T cells are conveyed to the olfactory cortex.

To examine the axonal projections of M/T cells from the olfactory bulb, we injected Tetbow AAVs into the mouse olfactory bulb. First, Tetbow AAVs were expressed in most of olfactory bulb neurons. When compared to single-color labeling, the stochastic and combinatorial expression of XFPs was helpful in improving tracing performance (Figure 8—figure supplement 1). Efficient axon tracing was further facilitated by the local injection of Tetbow AAVs (Figure 8A,B). In the olfactory bulb, many types of neurons were labeled, but only M/T cells projected their axons to the olfactory cortex. To facilitate high-resolution fluorescence imaging with a limited working distance of the objective lens (20x, NA = 0.75, WD = 0.66 mm), we flattened the olfactory cortical area onto a glass slide (Sosulski et al., 2011). After the fixation and tissue clearing, axons of individual M/T cells were clearly visualized with XFPs in the entire area of the olfactory cortex (Figure 8D and Video 5). The unique color hue was largely preserved at the average level, if not at a single-pixel resolution, from proximal to distal part in each axon (Figure 8E). Across the three image areas, the median Euclidean distance for the same neuron was 0.049 (interquartile range = 0.063, n = 34 pairs). The unique color hues and their consistency facilitated manual reconstruction of individual M/T cell axons in the olfactory cortex (Figure 8F, Figure 8—figure supplement 2, and Video 6). Highly divergent patterns of axonal collaterals were observed among labeled M/T cell axons, complementing earlier findings (Nagayama, 2010; Ghosh et al., 2011; Sosulski et al., 2011).

![Figure 8.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig8-v1.jpg)

**Figure 8.:** (A) M/T cells in the olfactory bulb were labeled with Tetbow AAVs. The Tetbow AAV cocktail (138 nL) was injected into a single location on the dorsal surface of the right olfactory bulb using a glass capillary. The virus was injected at P60 and mice were analyzed four weeks later. AAV titers were 4 × 108 gc/mL for AAV2/1-SYN1-tTA2 and 3 × 1010 gc/mL each for AAV2/1-TRE-mTurquoise2-WPRE, AAV2/1-TRE-EYFP-WPRE, and AAV2/1-TRE-tdTomato-WPRE. (B) In the olfactory bulb, M/T cells and various types of interneurons were densely labeled with Tetbow. (C) In the olfactory cortex, only M/T cell axons were labeled with Tetbow AAVs. The ventral-lateral part of the brain was flattened to 700 μm thickness. After fixation and clearing, confocal images were taken with 20x objective lenses. The labeling density was lower in the olfactory cortex, so we could easily trace individual M/T cell axons. M/T cell axons were found in the all areas of the olfactory cortex, including anterior olfactory nucleus (AON), olfactory tubercle (OT), piriform cortex (anterior (APC) and posterior (PPC)), cortical amygdala (CA), and lateral entorhinal cortex (LEC). Maximal intensity projection images of confocal images are shown (379.89 μm). See also Video 5. (D) High-magnification versions of the images shown in (C). All of the axons that were found in both area (a) and (b) and that could be traced for >1,000 μm were analyzed (14 axons). (E) Ternary plots of color codes in the axons highlighted in (C). Average color codes in each area (a–c) are shown. The color consistency is shown on the right. The color code was largely consistent across the areas except for a few axons (#6, #11 or #12). The copy number may not be optimum in this sample, as the plots are not found in the periphery of the ternary plots. The fluorescence intensity data used for (E) are available in Figure 8—source data 1. (F) Tracing and reconstruction of M/T cell axons. We terminated tracing when the labeled axons were interrupted by unlabeled gaps. Thus, our conservative tracing is most probably showing an underestimate of the entire wiring diagram. All of the axons that could be successfully traced for >1,000 μm are shown. The maximum length of the traced axon was 6852.63 μm. A z-stacked image of the reconstruction is shown. Tracings of individual M/T cells are shown in Figure 8—figure supplement 2. See also Video 6. Scale bars are 1 mm.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** (A) Olfactory bulb neurons were densely labeled with Tetbow AAVs. The majority of M/T cells in the dorsal olfactory bulb were labeled. AON, anterior olfactory nucleus; CA, cortical amygdala; LEC, lateral entorhinal cortex; OB, olfactory bulb; OT, olfactory tubercle; PC, piriform cortex. (B) M/T cell axons were densely labeled in the lateral olfactory tract. An enlarged image of the red boxed area is shown below. A z-stack image of and an image of the x-z section along the orange line are shown. Using this sample, we compared the tracing performance of single-color vs. Tetbow labeling. (C) The definition of successful tracing. In the gray-scale image data, we judged that two axons were successfully dissected when they crossed-over at different z positions (success). We judged that axon tracing failed when the two axons crossed on the same z plane (failure). In Tetbow tracing (full color), we judged that two axons were successfully dissected when the color hues for the two axons were visually discernable (success). We judged that the tracing failed when the two axons crossed on the same z plane and the two colors were visually too alike to discriminate (failure). According to Figure 1H, an experimenter can discriminate between two different colors separated by Euclidean distance 0.1 at >90% accuracy. We did not consider the direction of the crossing axons when we made a decision of success vs. failure. (D) Cumulative plots showing successfully traced axon length. The maximum length of traced axons in the gray-scale image data was 155.229 μm. The maximum length of traced axons in Tetbow (full color) was 318.953 μm. Eight axons out of 100 were fully traced Tetbow (full color), whereas no axons could be fully traced in the gray-scale image. Thus, Tetbow labeling much improves the tracing performance for densely labeled axons. Scale bars are 100 μm (A), 1 mm (B, top), and 50 μm (B, middle and bottom).

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/40350/elife-40350-fig8-figsupp2-v1.jpg)

**Figure 8—figure supplement 2.:** Putative mitral cell axons travel along the distal part of the lateral olfactory tract and send collaterals to the piriform cortex. Putative tufted cell axons terminate in the olfactory tubercle.

![Video 5.](https://cdn.elifesciences.org/articles/40350/elife-40350-video5.mp4.jpg)

**Video 5.:** Tetbow AAVs were injected to the olfactory bulb at P60 and analyzed after four weeks. Volume-rendering images of the olfactory cortex are shown. See legends to Figure 8.

![Video 6.](https://cdn.elifesciences.org/articles/40350/elife-40350-video6.mp4.jpg)

**Video 6.:** Traced M/T cell axons are separately shown. See legends to Figure 8 and Figure 8—figure supplement 1.

## Discussion

### Bright multicolor labeling of neurons using the Tet-Off system

To achieve the stochastic expression of multiple fluorescent proteins, it is important to optimize the number of genes that are introduced per cell. We introduced a limited number of copies of plasmids or virus vectors into neurons to enable the stochastic expression of XFPs based on a Poisson distribution. To enhance the expression levels of XFPs, we utilized a Tet-Off system, in which the tetracycline trans-activator (tTA) binds to the TRE promoter to drive the expression of genes of interest. In this way, we achieved multicolor labeling with much-improved brightness. Previously, the electroporation and virus infection of the Brainbow construct introduced just a small number of genes per cell, and as a result, the fluorescence levels were not sufficiently high for reliable neuronal tracing (Kobiler et al., 2010; Egawa et al., 2013) (see also Figure 2—figure supplement 2). In fact, Brainbow methods often had to employ antibody staining to enhance the fluorescence signals (Cai et al., 2013). However, our Tetbow strategy provides enhanced fluorescence, allowing for high-resolution imaging without the need for antibody staining. As a result, our Tetbow strategy has opened up a new opportunity for large-scale high-resolution neuronal tracing using tissue clearing.

Our Tetbow strategy also overcomes a size-limit problem associated with AAV vectors. As we introduced tTA and TRE-XFP gene cassettes with separate AAV vectors, DNA construction was also simplified. Using our Tetbow AAVs, we could clearly visualize different neurons with different color hues at synaptic resolution. It should be noted, however, that using the correct virus titer is critical for the generation of color variations. If the virus titer is too low, many of the labeled neurons will express just one XFP gene. By contrast, if the virus titer is too high, many of the labeled neurons will express all three genes at similar levels. Recently, another group employed a similar strategy using a Tet-Off system and a newly engineered AAV for intravenous transduction; but the brightness levels that they achieved were not as good as those provided by CAG vectors (Chan et al., 2017). To achieve the highest expression levels of XFPs, the expression level of tTA needs to be optimized (Figure 3). The Tet-Off system is also useful for controling the sparseness of XFP expression; by simply diluting the tTA vector, the expression of XFP can be sparsened without affecting color variations (Chan et al., 2017).

AAV- based Tetbow is useful for a relatively broad set of applications, including use in less genetically tractable model animals. For example, an AAV-based Tet-Off system has already been tested in the marmoset brain (Sadakane et al., 2015). Like mice, these animals demonstrated high expression levels of fluorescent proteins when the Tet-Off system was used. Thus, our Tetbow strategy can be useful for neuronal tracing studies in various species including primates.

### Multicolor labeling with chemical tags

In the present study, we also extended the Tetbow method to include chemical tags. Current tissue clearing methods are intended for the use of fluorescent proteins, but chemical tags can become a good alternative to the fluorescent proteins. First, unlike fluorescent proteins, once labeled with synthetic fluorophores, chemical tags are stable under harsh clearing conditions. This means that we can have a broader choice of clearing methods, particularly for lipid-rich and thick tissues. Chemical tags may also be useful for expansion microscopy, where the stability of fluorescent proteins has been a challenging aspect (Chen et al., 2015; Ku et al., 2016; Tillberg et al., 2016; Chang et al., 2017). The fluorescence labeling of chemical tags is much easier than the antibody staining of XFPs (Kohl et al., 2014). Furthermore, synthetic fluorophores penetrate much deeper than antibodies because of their smaller size. Second, more choices of fluorescence spectrum and photochemical properties are available with chemical tags than with fluorescent proteins. For example, synthetic fluorophores cover the spectrum from UV to near-IR range, expanding the possible spectrum range when imaging. In addition, autonomously blinking fluorophores are very useful for localization-based super-resolution microscopy (Uno et al., 2014). Multicolor 3D PALM/STORM imaging of cleared tissues would be an interesting possibility in the future.

### Single-axon tracing for long-range axonal projections

In recent years, several tissue-clearing methods that are optimized for fluorescence imaging have been developed, expanding the imaging scale in light-microscopy-based neuronal tracing. However, the imaging resolution was not sufficiently high for densely labeled neuronal circuits. Therefore, we could only look at population-level connectivity (Oh et al., 2014) or at a very small subset of neurons (Economo et al., 2016) with light microscopy. To examine the projection diagram of individual neurons, a single-cell barcoding and RNA sequencing approach, MAPseq, has been proposed (Kebschull et al., 2016). Although MAPseq is a promising new tool in the study of area-to-area connectivity for hundreds of neurons (Han et al., 2018), we cannot know the finer details of their neuronal morphology. Currently, saturated connectomics is only possible with electron microscopy (Kasthuri et al., 2015), but the analytical throughput is currently not sufficient for the study of long-range projections. The combination of Tetbow and tissue clearing can become a useful tool to fill the gap, allowing the dissection of densely labeled neurons at a large scale.

### Limitations and future challenges

In the present study, we employed our Tetbow method to analyze axonal projection profiles for M/T cells in the mouse olfactory bulb (Figure 8). We were able to find labeled axons in all the areas of the olfactory cortices that we examined (piriform cortex, cortical amygdala, and lateral entorhinal cortex), but it remains unclear whether we could completely label all the fibers to their termini. In fact, it is extremely difficult to know whether the labeled termini are really termini or are interrupted by small unlabeled gaps. Even if the second scenario is very likely, it is difficult to know which segments are in fact connected to each other, but the variable color hues can help. Single-cell labeling is advantageous to avoid such ambiguity, although the throughput is limited for such analyses (Igarashi et al., 2012). By contrast, multicolor labeling may be useful to compare the projection patterns in the same animals. In our analysis shown in Figure 8F, we traced axons using conservative criteria: we terminated tracing when labeled axons were interrupted by small gaps. Nevertheless, the quality of axonal tracing was comparable to that in earlier studies (Nagayama, 2010; Ghosh et al., 2011). To further improve the tracing performance (including up to the axon termini), it will be important to improve labeling methods in order to fill the thin neuronal fibers completely and evenly.

In this study, we employed manual neuronal tracing to Tetbow data, and were able to trace individual M/T cell axons successfully at the millimeter (>6 mm) scale. Color hues were consistent at a global scale (Figure 8E), but not perfect in high-magnification images (Figure 8D). Chromatic aberration can also be a problem in the high-resolution imaging of thick tissues. Another important challenge will be to improve the color hue consistency throughout a neuron and to develop auto-tracing software that is optimized for the multicolor-labeled neurons.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th colspan="2">Designation</th>
      <th colspan="2">Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gene (Mus musculus)</td>
      <td colspan="2">C57BL/6N</td>
      <td colspan="2">Japan SLC</td>
      <td>RRID: MGI:5658686</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (Mus musculus)</td>
      <td colspan="2">ICR</td>
      <td colspan="2">Japan SLC</td>
      <td>RRID: MGI:5652524</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td colspan="2">AAVpro 293 T Cell Line</td>
      <td colspan="2">Clontech</td>
      <td>cat# 632273</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pTRE-Tight</td>
      <td colspan="2">Clontech</td>
      <td>cat# 631059</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pCAG-CreERT2</td>
      <td colspan="2">PMID: 17209010 (Matsuda and Cepko, 2007)</td>
      <td>Addgene# 14797</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pmTurquoise2-N1</td>
      <td colspan="2">PMID: 22434194 (Goedhart et al., 2012;Matsuda and Cepko, 2007)</td>
      <td>Addgene# 60561</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pBluescript II SK(+) phagemid</td>
      <td colspan="2">Agilent Technologies</td>
      <td>cat# 212205</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">paavCAG-pre- mGRASP-mCerulean</td>
      <td colspan="2">PMID: 22138823 (Kim et al., 2011)</td>
      <td>Addgene# 34910</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pSNAPf</td>
      <td colspan="2">New England Biolabs</td>
      <td>cat# N9183S</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pCLIPf</td>
      <td colspan="2">New England Biolabs</td>
      <td>cat# N9215S</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pFC14K HaloTag CMV Flexi Vector</td>
      <td colspan="2">Promega</td>
      <td>cat# G3780</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pCAG-mTurquoise2</td>
      <td colspan="2">This paper</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pCAG-EYFP</td>
      <td colspan="2">This paper</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pCAG-tdTomato</td>
      <td colspan="2">This paper</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pCAG-tTA</td>
      <td colspan="2">This paper</td>
      <td>Addgene# 104102</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pBS-TRE -mTurquoise2-WPRE</td>
      <td colspan="2">This paper</td>
      <td>Addgene# 104103</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pBS-TRE-EYFP-WPRE</td>
      <td colspan="2">This paper</td>
      <td>Addgene# 104104</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pBS-TRE-td Tomato-WPRE</td>
      <td colspan="2">This paper</td>
      <td>Addgene# 104105</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pBS-TRE-SNAPf-WPRE</td>
      <td colspan="2">This paper</td>
      <td>Addgene# 104106</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pBS-TRE-CLIPf-WPRE</td>
      <td colspan="2">This paper</td>
      <td>Addgene# 104107</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pBS-TRE-HaloTag-WPRE</td>
      <td colspan="2">This paper</td>
      <td>Addgene# 104108</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">AAV2-miniSOG -VAMP2-tTA-mCherry</td>
      <td colspan="2">PMID: 23889931 (Lin et al., 2013)</td>
      <td>Addgene# 50970</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pAAV-SYN1-tTA</td>
      <td colspan="2">This paper</td>
      <td>Addgene# 104109</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pAAV-TRE -mTurquoise2-WPRE</td>
      <td colspan="2">This paper</td>
      <td>Addgene# 104110</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pAAV-TRE -EYFP-WPRE</td>
      <td colspan="2">This paper</td>
      <td>Addgene# 104111</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pAAV-TRE -tdTomato-WPRE</td>
      <td colspan="2">This paper</td>
      <td>Addgene# 104112</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">pCAG-iCre</td>
      <td colspan="2">PMID: 26972009 (Ke et al., 2016)</td>
      <td>N/A</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">AAV-EF1a-BbTagBY</td>
      <td colspan="2">PMID: 23817127 (Cai et al., 2013)</td>
      <td>Addgene# 45185</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td colspan="2">AAV-EF1a-BbChT</td>
      <td colspan="2">PMID: 23817127 (Cai et al., 2013)</td>
      <td>Addgene# 45186</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td colspan="2">AAVpro Helper Free System</td>
      <td colspan="2">Takara</td>
      <td>cat# 6673</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td colspan="2">AAVpro Purification Kit (All Serotypes)</td>
      <td colspan="2">Takara</td>
      <td>cat# 6666</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td colspan="2">AAVpro Titration Kit (for real-time PCR)</td>
      <td colspan="2">Takara</td>
      <td>cat# 6233</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td colspan="2">SNAP-Surface 488</td>
      <td colspan="2">New England Biolabs</td>
      <td>cat# S9124S</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td colspan="2">CLIP-Surface 647</td>
      <td colspan="2">New England Biolabs</td>
      <td>cat# S9234S</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td colspan="2">HaloTag TMR Ligand</td>
      <td colspan="2">Promega</td>
      <td>cat# G8252</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td colspan="2">Saponin</td>
      <td colspan="2">Nakalai-tesque</td>
      <td>cat# 30502–42</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td colspan="2">Omnipaque 350</td>
      <td colspan="2">Daiichi-Sankyo</td>
      <td>cat# 081–106974</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td colspan="2">Urea</td>
      <td colspan="2">Wako</td>
      <td>cat# 219–00175</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td colspan="2">N,N,N',N'-Tetrakis (2-hydroxypropyl) ethylenediamine</td>
      <td colspan="2">TCI</td>
      <td>cat# T0781</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td colspan="2">Triton X-100</td>
      <td colspan="2">Nakalai-tesque</td>
      <td>cat# 12967–45</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td colspan="2">Hexane</td>
      <td colspan="2">Nakalai-tesque</td>
      <td>cat# 17922–65</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td colspan="2">Benzyl alcohol</td>
      <td colspan="2">SIGMA</td>
      <td>cat# 402834–100 ML</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td colspan="2">Benzyl benzoate</td>
      <td colspan="2">Wako</td>
      <td>cat# 025–01336</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td colspan="2">Tetrahydrofuran, super dehydrated, with stabilizer</td>
      <td colspan="2">Wako</td>
      <td>cat# 207–17905</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td colspan="2">Dibenzyl Ether</td>
      <td colspan="2">Wako</td>
      <td>cat# 022–01466</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td colspan="2">ImageJ</td>
      <td colspan="2">NIH</td>
      <td>RRID: SCR_003070</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td colspan="2">GraphPad Prism 7</td>
      <td colspan="2">GraphPad Software</td>
      <td>RRID: SCR_002798</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td colspan="2">MATLAB</td>
      <td colspan="2">MathWorks</td>
      <td>RRID: SCR_001622</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td colspan="2">Leica Application Suite X</td>
      <td colspan="2">Leica Microsystems</td>
      <td>RRID: SCR_013673</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td colspan="2">Imaris</td>
      <td colspan="2">Bitplane AG</td>
      <td>RRID: SCR_007370</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td colspan="2">Neurolucida</td>
      <td colspan="2">MBF Bioscience</td>
      <td>RRID: SCR_001775</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td colspan="2">Adobe Photoshop</td>
      <td colspan="2">Adobe</td>
      <td>RRID: SCR_014199</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td colspan="2">Adobe Illustrator</td>
      <td colspan="2">Adobe</td>
      <td>RRID: SCR_010279</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td colspan="2">Microslicer</td>
      <td colspan="2">Dosaka EM</td>
      <td>PRO7N</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td colspan="2">Electroporator</td>
      <td colspan="2">BEX</td>
      <td>CUY21EX</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td colspan="2">Forceps-type electrodes (5 mm diameter)</td>
      <td colspan="2">BEX</td>
      <td>LF650P5</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td colspan="2">Forceps-type electrodes (3 mm diameter)</td>
      <td colspan="2">BEX</td>
      <td>LF650P3</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td colspan="2">TCS SP8X</td>
      <td colspan="2">Leica Microsystems</td>
      <td>TCS SP8X</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td colspan="2">10x dry lens</td>
      <td colspan="2">Leica Microsystems</td>
      <td>HC PL APO 10x/0.40 CS</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td colspan="2">20x multi-immersion objective lens</td>
      <td colspan="2">Leica Microsystems</td>
      <td>HC PL APO 20x /0.75 IMM CORR CS2</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td colspan="2">40x oil-immersion objective lens</td>
      <td colspan="2">Leica Microsystems</td>
      <td>HC PL APO 40x OIL CS2,</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td colspan="2">63x glycerol-immersion objective lens</td>
      <td colspan="2">Leica Microsystems</td>
      <td>HC PL APO 63x GLYC CORR CS2</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td colspan="2">Raw image data</td>
      <td colspan="2">This paper</td>
      <td>http://ssbd.qbic.riken.jp/set/20180901/</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td colspan="2">Neurolucida reconstruction data</td>
      <td colspan="2">This paper</td>
      <td>http://ssbd.qbic.riken.jp/set/20180901/</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td colspan="2">MATLAB codes</td>
      <td colspan="2">This paper</td>
      <td>https://github.com/mleiwe/TetbowCodes</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Plasmids

pCAG-mTurquoise2/EYFP/tdTomato were assembled by using pCAG-CreERT2 (Addgene #14797, RRID: Addgene_14797, from Dr. Cepko), pmTurquoise2-N1 (Addgene #60561, RRID: Addgene_60561, from Dr. D. Gadella), EYFP (Clontech), and tdTomato (a gift from Dr. R. Tsien). To generate a backbone vector for pTRE-XFP, an Xho-Xho fragment containing TRE-SV40 poly A was transferred from pTRE-Tight (#631059, Clontech) to pBluescript II SK(+) (# 212205, Agilent) to ensure high-copy expression in Escherichia coli. The WPRE sequence was PCR amplified from an aavCAG-pre-mGRASP-mCerulean vector (Addgene #34910, RRID: Addgene_34910, a gift from Dr. J. Kim). The tTA sequence in pCAG-tTA and pAAV2-SYN1-tTA was derived from the tTA2 section of the pTet-Off Advanced vector (Clontech). SNAPf and CLIPf tag genes were obtained from New England Biolabs (#N9183S, #N9215S), and the HaloTag gene was obtained from Promega (#G3780). AAV2-Tetbow vectors were generated by modifying AAV2-miniSOG-VAMP2-tTA-mCherry (Addgene #50970, RRID: Addgene_50970, from Dr. R. Tsien). Maps for the Tetbow plasmids are shown in figure supplements. The Tetbow plasmids and their sequences have been deposited at Addgene (https://www.addgene.org/Takeshi_Imai/) with Addgene #104102–104112. See also SeeDB Resources (https://sites.google.com/site/seedbresources/) for updated information.

As for the Brainbow experiments, we used AAV-EF1a-BbTagBY (Addgene #45185, RRID: Addgene_45185) and AAV-EF1a-BbChT (Addgene #45186, RRID: Addgene_45186) plasmids.

### Mice

All animal experiments were approved by the Institutional Animal Care and Use Committee of the RIKEN Kobe Institute and Kyushu University. ICR mice (Japan SLC, RRID: MGI: 5652524) were used for in utero electroporation and C57BL/6N mice (Japan SLC, RRID: MGI: 5658686) were used for AAV experiments (age, P56-70; male). To obtain brain tissue, mice were i.p. injected with an overdose of nembutal (Dainippon Sumitomo Pharma) or somnopentyl (Kyoritsu Seiyaku) to produce deep anesthesia, followed by an intracardiac perfusion with 4% paraformaldehyde (PFA) in phosphate buffered saline (PBS). Excised brain samples were post-fixed with 4% PFA in PBS at 4°C overnight. Samples were then embedded in 4% agarose and cut into slices of 220, 500, or 1000 μm thick with a microslicer, PRO7N (Dosaka EM).

### In utero electroporation

The in utero electroporation of plasmids to the cerebral cortex and mitral cells was performed as described previously (Saito, 2006; Ke et al., 2013; Muroyama et al., 2016). Pregnant ICR mice were anesthetized with medetomidine (0.3 mg/kg), midazolam (4 mg/kg), and butorphanol (5 mg/kg), or with ketamine (100 mg/kg) and xylazine (10 mg/kg). The uterine horns carrying embryos were exposed through a midline abdominal incision. To label L2/3 neurons in the cortex, 1 μL of plasmid solutions diluted in PBS was injected into the lateral ventricle of the embryos at E15 using a micropipette made from a glass capillary. Electric pulses (single 10 ms poration pulse at 72 V, followed by five 50 ms driving pulses at 40–42 V with 950 ms intervals) were delivered by a CUY21EX electroporator (BEX) and forcep-type electrodes (5 mm diameter, #LF650P5, BEX). To introduce pCAG-XFP vectors, the labels pCAG-mTurquoise2, EYFP, and tdTomato were injected into the lateral ventricle and electroporated at high-copy (1 μg/μL each, 3 μg/μL in total) or low-copy (0.25 μg/μL each, 0.75 μg/μL in total) numbers. pTRE-XFP vectors with pCAG-tTA were injected and electroporated at low-copy numbers (0.25 μg/μL each, 1.0 μg/μL in total) when not specified; in Figure 3, the exact plasmid concentrations are specified. To label mitral cells in the olfactory bulb, in utero electroporation was performed at E12. Electric pulses (single 10 ms poration pulse at 72 V, followed by five 50 ms driving pulses at 36 V with 950 ms intervals) were delivered with forceps-type electrodes (3 mm diameter, #LF650P3, BEX). After the electroporation, the uterine horns were placed back into the abdominal cavity, and the abdominal wall and skin were sutured.

### AAV

AAV vectors were generated using the AAVpro Helper Free System (AAV1, #6673, Takara) from Takara and the AAVpro 293 T cell line (#632273, Clontech) following the manufacturers’ instructions. The backbone pAAV plasmid is for AAV2. Thus, the serotype used in this study is AAV2/1. AAV vectors were generated by AAVpro 293 T cells (#632273, Clontech). AAVpro 293T is a commercialized cell line for production of AAV vectors. We did not test for mycoplasma contamination in our hands. In our experiments, cells within 10 passages were used for virus production. AAV vectors were purified using the AAVpro Purification Kit All Serotypes (#6666, Takara). Virus titers were then determined by qPCR using the AAVpro Titration Kit (#6233, Takara) and the StepOnePlus system (ThermoFisher). To infect the AAV vectors, C57BL/6 mice (P56-70) were anesthetized with ketamine (100 mg/kg) and xylazine (10 mg/kg), and an AAV virus cocktail was injected into the brain using the nanoject II system and glass capillaries (#3-00-203-G/XL, Drummond). The injection volume was 207 nL in Figure 7, 138 nL in Figures 8, and 207 nL ×5 different locations in Figure 8—figure supplement 1. The final concentration of the virus cocktail was 4 × 108 gc/ml for AAV2/1-SYN1-tTA2 and 1 × 1010–1 × 1011 gc/mL each for AAV2/1-TRE-mTurquoise2-WPRE, AAV2/1-TRE-EYFP-WPRE, and AAV2/1-TRE-tdTomato-WPRE. The mice were sacrificed 2 or 4 weeks after viral injection. It should be noted that the expression of Tetbow AAV can lead to toxic effects for cellular functions after prolonged incubation because of the extremely high levels of expression. For example, cortical neurons started to show aggregation of XFPs and morphological abnormality 4 weeks after virus injection. Olfactory bulb neurons were best visualized 4 weeks after virus injection without obvious sign of toxicity. The optimum timing for the analysis may be different for different cell types.

The following stereotaxic coordinates were used for AAV injection. Distance in millimeters from the Bregma for the anterior (A) – posterior (P), and lateral (L) positions, and from the brain surface toward the ventral (V) directions are indicated. Cortical layer five neurons: P=1.5, L = 1.5, V = 0.5; hippocampal CA1 neurons: P=1.5, L = 1.5, V = 1; olfactory bulb granule cells: A = 4.5, L = 0.5, V = 0.5; olfactory bulb M/T cells: A = 4.5, L = 0.5, V = 0.3.

### Staining chemical tags

SNAP, CLIP, and HaloTags were visualized with their substrates, SNAP-Surface 488 (#S9124S, New England Biolabs), HaloTag TMR Ligand (#G8252, Promega), CLIP-Surface 647 (#S9234S, New England Biolabs), respectively. Brain slices of 220 or 1000 μm thickness were incubated with the substrates (2 μM each) in 2 ml 2% saponin in PBS overnight. The slices were then washed with PBS (3 × 30 min).

### Clearing with SeeDB2G

Brain-slice samples were cleared with SeeDB2G for imaging when not specified. SeeDB2G is designed for high-resolution imaging with glycerol-immersion objective lenses (Ke et al., 2016). PFA-fixed brain samples (embedded in agarose, cut at 220, 500, or 1000 μm thick) were cleared at room temperature (25°C) with a 1:2 mixture of Omnipaque 350 (#081–106974, Daiichi-Sankyo) and H2O with 2% saponin (#30502–42, Nakalai-tesque) for 6 hr (3 ml in 5 ml tube), a 1:1 mixture of Omnipaque 350 and H2O with 2% saponin for 6 hr, and finally Omnipaque 350 with 2% saponin overnight. Cleared samples were then mounted in SeeDB2G (Omnipaque 350) on a glass slide using a 0.2 mm thick silicone rubber sheet (AS ONE, #6-9085-13, Togawa rubber) and glass coverslips (#0109030091, Marienfeld, No. 1.5H) (Ke et al., 2016). A detailed step-by-step protocol has been published in bio-protocol (Ke and Imai, 2018).

To quantify the fluorescence intensity of M/T cell axons (Figure 2—figure supplement 2), whole-brain samples were cleared with SeeDB2 and placed on a glass-bottomed dish for imaging and quantification.

To analyze long-rage axonal projection of M/T cells (Figure 8), a right-brain hemisphere was dissected, and the dorsal part and subcortical matter was trimmed away with forceps and a scalpel. The remaining part, containing all of the olfactory cortical areas, was flattened with a 700 mm spacer and fixed with 4% PFA in PBS overnight (Sosulski et al., 2011). Then, the sample was treated with ScaleCUBIC-1 (25% (wt/wt) urea (#219–00175, Wako), 25% (wt/wt) N,N,N’,N’-tetrakis(2-hydroxypropyl)ethylenediamine (#T0781, TCI), and 15% (wt/wt) Triton X-100 (#12967–45, Nakalai-tesque) in H2O) (Susaki et al., 2014) for 24 hr to remove lipids from the lateral olfactory tract, washed with PBS, and then cleared with SeeDB2G as described above.

### BABB

PFA-fixed brain samples were serially incubated in 50%, 80%, and 100% ethanol, each for 8 hr. They were then incubated in 100% ethanol for 12 hr, and then in hexane (#17922–65, Nakalai-tesque) for 12 hr. Samples were cleared (benzyl alcohol (# 402834–100 ML, SIGMA):benzyl benzoate (#025–01336, Wako)=1:2) with gentle shaking for 24 hr.

### 3DISCO

PFA-fixed brain samples were serially incubated in 50%, 70%, 80%, and 100% tetrahydrofuran (THF, # 207–17905, Wako), each for 1 hr. They were then incubated in 100% THF for 12 hr, and then in dibenzyl ether (DBE, #022–01466, Wako) for 3 hr (Ertürk et al., 2012).

### Confocal imaging

Confocal images were acquired using an inverted confocal microscope, TCS SP8X with HyD detectors (Leica Microsystems). Type G immersion (refractive index 1.46, Leica) was used for a 20x multi-immersion objective lens (HC PL APO 20x/0.75 IMM CORR CS2, NA0.75, WD 0.66 mm) and a 63x glycerol-immersion objective lens (HC PL APO 63x GLYC CORR CS2, NA1.3, WD 0.28 mm). Type F immersion (refractive index 1.518, Leica) was used for a 40x oil-immersion objective lens (HC PL APO 40x OIL CS2, NA1.3, WD 0.24 mm). Low-magnification images in Figure 2—figure supplement 2 were taken with a 10x dry lens (HC PL APO 10x/0.40 CS, NA0.4, WD 2.2 mm). Diode lasers of 442 or 448 nm, 488 nm, and 552 nm wavelength were used for mTurquoise2, EYFP, and tdTomato, respectively. In some experiments, a white light laser was used to image mTurquoise2, EYFP, and tdTomato. To image chemical tags, SNAP-Surface 488, HaloTag TMR Ligand, and CLIP-Surface 647 were imaged with diode lasers of 488 nm, 552 nm, and 638 nm wavelength, respectively. Emission light was dispersed by a prism and detected by HyD detectors.

### Image processing and quantification

Microscopy data were processed and visualized with LAS X (RRID: SCR_013673, Leica Microsystems) or Imaris (RRID: SCR_007370, Bitplane). Image data were excluded from further quantitative analyses when the data contained saturated fluorescence signals. For Figures 2 and 3, the fluorescence intensities on somata were quantified with ImageJ at every 2.97 μm thickness. For Figure 7, an image of the soma was taken and analyzed at the focal depth for each cell. For Figure 8, color values at axons were analyzed for maximum intensity projection images, as there may be a slight chromatic aberration along the z axis. After binarization, the average color value ratio was determined for each segment of each axon. Ternary plots, box plots, and statistical analyses were prepared using MATLAB (RRID: SCR_001622, MathWorks). Image data were acquired by RS, to prevent bias when they were subsequently analyzed by MNL. First, the fluorescence intensity in each channel was normalized so that the median intensity was 1. Then, the intensity values were further normalized so that the length of the vector was 1. Raw quantification data (Source Data files) are accompanied with figures. The MATLAB code and processed data for the figure panels have been deposited to GitHub (Leiwe, 2018; copy archived at https://github.com/elifesciences-publications/TetbowCodes).

### Axon tracing

Axon tracing was performed with Neurolucida (RRID: SCR_001775, MBF Bioscience). In Figure 8F, we focused on axons were found within 200 μm of the anterior end of the image. We terminated tracing when labeled axons were interrupted by unlabeled gaps; in such cases, we judged that we cannot be 100% sure whether the interrupted segments are connected. Thus, our tracing was performed using very conservative criteria, and thus most probably provides an underestimate of the entire wiring diagram. Axons that can be traced for >1,000 μm were analyzed (25 axons). Putative mitral and tufted cells were identified on the basis of the projection area (piriform cortex vs. olfactory tubercle) and their axonal trajectories. Brightly-labeled putative mitral and tufted cells were further analyzed in Figure 7D,E. For Figure 8—figure supplement 2, we focused on axons that crossed the anterior plane and within the lateral half. We chose 100 axons in an unbiased manner from the dorsal to ventral direction. The criteria for successful tracing are described in Figure 8D; as these criteria are very strict, the area that is traced may be an underestimate. Color discrimination was performed visually by one experimenter, who also joined the visual color discrimination test.

### Visual color discrimination

Custom MATLAB code (Leiwe, 2018; copy archived at https://github.com/elifesciences-publications/TetbowCodes) was written to quantify the ability of experienced researchers to discriminate three color space (RGB) in terms of 3D Euclidean space. All of the subjects (from the Imai lab) have experience in fluorescence imaging, understand the purpose of the test, and have trichromatic color vision. To prevent the intensity of the color from influencing the decision, the intensity was randomly varied between 50–100% for each square displayed (Figure 1—figure supplement 1). The subject was presented with a choice to discriminate between two colors at a specified Euclidean distance. Specifically, they were asked to determine whether the two columns form a cross or a parallel line. For each Euclidean distance presented, there were 100 trials per subject, with the average success rate stored. Note that this test was not intended to evaluate the color discrimination performance of people in general.

### Modeling

Poisson distributions were calculated in MATLAB, by creating independent distributions for each XFP for each specified copy number. 200 ‘cells’ were selected for each copy number group with associated XFP values derived from the Poisson distributions. The code has been deposited to GitHub (Leiwe, 2018; copy archived at https://github.com/elifesciences-publications/TetbowCodes).

### Imaging data

The raw microscopy data have been deposited to the Systems Science of Biological Dynamics (SSBD) database (http://ssbd.qbic.riken.jp/) with a unique URL (http://ssbd.qbic.riken.jp/set/20180901/). Movies will be posted at SeeDB Resources (https://sites.google.com/site/seedbresources/).

### Step-by-step protocol

Step-by-step protocols has been posted in our website, SeeDB Resources (https://sites.google.com/site/seedbresources/). All of our published clearing methods and technical tips are also posted on this website. A detailed protocol for SeeDB2 was published in bio-protocol (Ke and Imai, 2018).
