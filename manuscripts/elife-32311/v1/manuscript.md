# A quantitative approach for analyzing the spatio-temporal distribution of 3D intracellular events in fluorescence microscopy

## Authors

- Thierry Pécot<sup>1</sup> ([ORCID: 0000-0003-0772-9753](https://orcid.org/0000-0003-0772-9753))
- Liu Zengzhen<sup>2</sup>
- Jérôme Boulanger<sup>2</sup>
- Jean Salamero<sup>2</sup>
- Charles Kervrann<sup>1</sup> ([ORCID: 0000-0001-6263-0452](https://orcid.org/0000-0001-6263-0452)) †

### Affiliations

1. Serpico Team-Project Inria, Centre Rennes-Bretagne Atlantique Rennes France
2. CNRS UMR 144, Space Time Imaging of Endomembranes Dynamics Team PSL Research University, Institut Curie Paris France
3. Cell and Tissue Imaging Facility IBiSA, Institut Curie Paris France

† Corresponding author

## Abstract

Analysis of the spatial distribution of endomembrane trafficking is fundamental to understand the mechanisms controlling cellular dynamics, cell homeostasy, and cell interaction with its external environment in normal and pathological situations. We present a semi-parametric framework to quantitatively analyze and visualize the spatio-temporal distribution of intracellular events from different conditions. From the spatial coordinates of intracellular features such as segmented subcellular structures or vesicle trajectories, QuantEv automatically estimates weighted densities that are easy to interpret and performs a comprehensive statistical analysis from distribution distances. We apply this approach to study the spatio-temporal distribution of moving Rab6 fluorescently labeled membranes with respect to their direction of movement in crossbow- and disk-shaped cells. We also investigate the position of the generating hub of Rab11-positive membranes and the effect of actin disruption on Rab11 trafficking in coordination with cell shape.

## Introduction

Modern light microscopy associated with fluorescence molecule tagging allows studying the spatial distribution of intracellular events. Unfortunately, fluorescent images are complex to analyze and additional software is needed to evaluate statistical differences between different conditions (Meijering et al., 2016; Tinevez et al., 2017). Automatic methods have the obvious advantage of being quicker and reproducible. However, most computational methods are based on the complex combination of heterogeneous features such as statistical, geometrical, morphological and frequency properties (Peng, 2008), which makes it difficult to draw definitive biological conclusions. Additionally, most experimental designs, especially at single-cell level, pool together data coming from replicated experiments of a given condition (Schauer et al., 2010; Merouane et al., 2015; Biot et al., 2016), neglecting the biological variability between individual cells.

Micro-patterning is now a well-established strategy to reduce morphological variability by imposing constraints on adhesion sites, which has been shown to influence the cytoskeleton geometry and transport carrier localization (Théry et al., 2005; Schauer et al., 2010). This technique opened the way to pairwise comparisons of conditions with a two-sample kernel density-based test by pooling together all data from each condition (Duong et al., 2012). Unfortunately, it does not consider the sample-to-sample variability because all replicated experiments from a given condition are simply merged together. Additionally, the visualization of the kernel density maps enables to average several experiments but fails to identify specific locations of interest in the cell (e.g. docking areas). Finally, assessing the dynamical behavior of labeled membrane structures, a fundamental task for trafficking analysis, remains out of scope in this framework.

In this paper, we describe a method that we call QuantEv dedicated to the analysis of the spatial distribution of intracellular events represented by any static or dynamical descriptor (e.g. detected points, segmented regions, trajectories...) provided that the descriptors are associated with spatial coordinates. QuantEv offers a unifying frame to decipher complex trafficking experiments at the scale of the whole cell. It is typically able to detect subtle global molecular mechanisms when trajectory clustering fails. An overview of the approach is presented in Figure 1. Our approach first computes 3D histograms of descriptors in a cylindrical coordinate system (parameterized by radius $r$, angle $\theta$ and depth $z$) with computational cell shape normalization, enabling comparisons between cells of different shape. Densities are obtained via adaptive kernel density estimation (Silverman, 1986; Taylor, 2008). Visualization through histograms and densities allows giving a clear biological interpretation of the experiments. We use the Earth Mover’s Distance (Rubner et al., 2000) and the Circular Earth Mover’s Distance (Rabin et al., 2011) to measure the dissimilarity between densities associated with different experimental conditions. A statistical analysis of these distances reliably takes into account the biological variability over replicated experiments. By computing weighted densities for each point in the cell as the reference center, QuantEv identifies the point that gives the most uniform angular distribution. This point may coincide with a biological structure of interest that would act as the events emitter or attractor.

![Figure 1.](https://cdn.elifesciences.org/articles/32311/elife-32311-fig1-v1.jpg)

**Figure 1.:** Spatial distribution analysis: QuantEv computes 3D histograms and densities of intracellular descriptors to quantitatively compare different experimental conditions. Uniformity analysis: QuantEv identifies the point that gives the most uniform angular distribution of intracellular descriptors.

In the section Results, we describe the application of QuantEv to detect significant differences between molecular trafficking and phenotypes observed in cells with various shapes. The first application is concerned with the distribution of membranes labeled by GFP-Rab6 as a hallmark of vesicular carriers in unconstrained, crossbow- and disk-shaped cells. Rab6 proteins are transiently anchored to moving transport carriers from the Golgi apparatus located at the cell center to Endoplasmic Reticulum entry sites or to plasma membrane (White et al., 1999; Chavrier and Goud, 1999; Echard et al., 2000; Opdam et al., 2000; Grigoriev et al., 2007; Bardin et al., 2015), both assumed to be located at the cell periphery. Cell shape imposes constraints on the cytoskeleton and consequently influences the spatial distribution of Rab6 transport carriers, as confirmed with kernel density maps (Schauer et al., 2010). We apply QuantEv to visualize and quantify this influence and to localize regions in the cell associated with Rab6 trafficking stages. In addition, Rab6 positive membranes were reported to move from and toward the Golgi in apparent close proportions (Grigoriev et al., 2007, Grigoriev et al., 2011), and yet these membrane associated proteins are believed to traffic in majority from the Golgi located at the cell center to the cell periphery (White et al., 1999; Chavrier and Goud, 1999; Echard et al., 2000; Opdam et al., 2000; Grigoriev et al., 2007) where they should dissociate from membranes and recycle back to the cytosol. To investigate these apparently antagonist statements, we apply QuantEv on Rab6 trajectories to characterize the dynamical behaviors of these transport carriers.

The second application focuses on the dynamics of mCherry-Rab11-positive membranes. Rab11 is known to be primarily localized to the Endosomal Recycling Compartment (ERC), and it organizes spatially and temporally recycling from this compartment (Ullrich et al., 1996; Gidon et al., 2012; Baetz and Goldenring, 2013; Boulanger et al., 2014). Here, we confirm by using QuantEv the hypothesis that the labeled transport intermediates are uniformly distributed around the ERC at the plasma membrane plane. Furthermore, we also investigate the progressive effect of actin disruption induced by Latrunculin A injection on the ERC localization with respect to time. We finally apply QuantEv to analyze the joined influence of actin disruption and cell shape on the radial distribution of Rab11 vesicles trafficking.

## Results

### Visualizing and quantifying the influence of cell shape on the spatial distribution of Rab6 positive membranes

We applied the QuantEv approach to visualize the spatial distribution of Rab6-positive membranes in unconstrained, crossbow- and disk-shaped cells (see Appendix 1—figure 1) and quantify their differences. To test the generic performance of QuantEv, these image sequences were acquired with two different 3D imaging modalities, a multi-point confocal microscopy and a wide field video microscopy. We compared the results obtained with QuantEv to those obtained with the more conventional kernel density (KD) maps (Schauer et al., 2010; Merouane et al., 2015). The KD approach concludes that the distribution of Rab6-positive membranes are clearly different between cells of different shapes (see Figure 2a–c, p value = 0 when considering unconstrained cells versus crossbow-shaped cells, unconstrained cells versus disk-shaped cells, and crossbow-shaped cells versus disk-shaped cells). Unfortunately, it also leads to a significant difference when image sequences with the same cell shape are compared (see Figure 2d). This demonstrates that the KD approach is too sensitive. Instead, QuantEv shows a uniform range of p values when cells with same shape are compared (see Figure 2d) while it leads to significant differences between radial, angular and in-depth distributions of Rab6 proteins from cells with different cell shapes (see Figure 2e–f). The angular distribution of Rab6 proteins is different for the three cell shapes. It ranges from a completely uniform distribution for disk-shaped cells, to a less regular distribution for unconstrained cells and to a distribution oriented toward the three tips of the crossbow for crossbow-shaped cells. In-depth and radial distributions are similar for crossbow- and disk-shaped cells. In contrast, they are different from unconstrained cells. Unconstrained cells show diverse sizes with a strong tendency to spread. This explains why the in-depth distribution is flatter for the unconstrained cells than for the constrained cells. Interestingly, QuantEv is able to reflect these differences. QuantEv also highlights a distribution maximum for a radius at the two-thirds (resp. five-sixth) the distance between the Golgi region border and the cell periphery for both micro-patterns (resp. unconstrained cells) (see Figure 2f–i). These maxima correspond to an accumulation of Rab6-positive membranes and identify the area where they enter a docking phase before switching to a tethering phase. The localization difference for these maxima between constrained and unconstrained cells is explained by a smaller adhesion area without micro-patterns, pushing the docking phase for vesicles closer to the cell periphery. Both radial and angular distributions unraveled by QuantEv represent a measurement of the environment constraints undergone by living cells.

![Figure 2.](https://cdn.elifesciences.org/articles/32311/elife-32311-fig2-v1.jpg)

**Figure 2.:** (a−c) 3D KD maps obtained with kernel density maps when considering all image sequences with unconstrained (a), crossbow- (b) and disk- (c) shaped cells. (d) Box and whisker plots of the p values obtained when comparing randomly 100 times two groups of unconstrained (UCC), crossbow-shaped (CSC) or disk-shaped cells (DSC) with QuantEv and KD maps. (e) Box and whisker plots of the condition differences with respect to radius $r$, angle $\theta$ and depth $z$ over 58 image sequences. p values under conditions of one-sided Wilcoxon signed-rank test when considering the condition differences are indicated below the box and whisker plots. A star (*) indicates that the p value is smaller than 0.05. (f) Histograms (bar plots) and densities (lines) of the spatial distribution of Rab6 positive membranes with respect to radius $r$, angle $\theta$ and depth $z$. These distributions come from 18 image sequences with an unconstrained cell (blue bar plots and lines), 18 image sequences with a crossbow-shaped cell (orange bar plots and lines) and 22 image sequences with a disk-shaped cell (green bar plots and lines). (g−i) Overlay of the average intensity projection map of an image sequence with an unconstrained (g), crossbow- (h) and disk- (i) shaped cell and the radial levels at 0.6 and 0.8. The scale bars correspond to 5 $\mu$m.

### Inwards and outwards Rab6-positive membranes show two distinctive dynamical behaviors

Rab6-positive membranes are trafficking from the Golgi located at the cell center to the cell periphery (White et al., 1999; Chavrier and Goud, 1999; Echard et al., 2000; Opdam et al., 2000; Grigoriev et al., 2007) and at the same time move from and toward the Golgi in comparable proportions (Grigoriev et al., 2007; Grigoriev et al., 2011). To reconcile these two antagonist statements, we applied QuantEv as follows. Rab6 trajectories were classified into two categories (Figure 3a–c): (i) vesicles moving toward the cell periphery; (ii) vesicles moving toward the Golgi. As shown in Figure 3d–f, the proportion of Rab6-positive membranes moving toward the cell periphery and toward the Golgi are close (0.531 versus 0.469 for unconstrained cells, 0.497 versus 0.503 for crossbow-shaped cells, 0.521 versus 0.479 for disk-shaped cells). However, the radial distributions shown in Figure 3d–f display two distinctive modes for vesicles moving toward the cell periphery and those moving toward the Golgi (p value = 0.0002 for unconstrained cells, p value = 0.021 for crossbow-shaped cells, p value = 0.0008 for disk-shaped cells). Between the Golgi and the distribution maxima shown in Figure 2f, Rab6 vesicles are predominantly moving toward the cell periphery. Between these maxima and the cell periphery, they are in majority moving toward the Golgi, indicating that during their docking-tethering phase, the vesicles are predominantly moving toward the cell center. These two distinctive dynamical behaviors are consistent with the aforementioned antagonist statements. To go further in the analysis, we looked at the confinement ratio (Figure 4a), the total path length and the lifetime of Rab6 trajectories, conventional dynamical measures used for particle tracking analysis. The combination of these measures with spatial localization is of high interest (Applegate et al., 2011; Tinevez et al., 2017) and QuantEv provides a good framework to quantitatively analyze and visualize the distribution of these dynamical measures with respect to their intracellular localization. We focus on the radial distribution of Rab6 trajectories from unconstrained and constrained cells as the differences between trajectories moving toward cell periphery and trajectories moving toward Golgi lie in these distributions (see Figure 3d–f). Rab6-positive membranes moving toward the cell periphery have a much more direct path than the ones moving toward the Golgi, except near the cell periphery (see Figure 4b, e). Consistently, Rab6 positive membranes moving toward the Golgi have longer total path length and lifetime than the ones moving toward the cell periphery, especially when approaching the cell periphery (see Figure 4c–e). In summary, this analysis clearly demonstrated that Rab6-positive membranes move predominantly and quite directly from the Golgi to the cell periphery until they enter a docking phase. Then, they mostly go back toward the cell center by following long and indirect trajectories.

![Figure 3.](https://cdn.elifesciences.org/articles/32311/elife-32311-fig3-v1.jpg)

**Figure 3.:** (a–c) Rab6 trajectories moving toward the cell periphery (red trajectories) and toward Golgi (green trajectories) extracted from an image sequence with an unconstrained (a), a crossbow- (b) and a disk- (c) shaped cell. The scale bars correspond to 5 $\mu$m. (d-f) Histograms (bar plots) and densities (lines) of the spatial distribution of Rab6-positive membranes moving toward the cell periphery (green bar plots and lines) or toward the Golgi (pink bar plots and lines) with respect to radius $r$, angle $\theta$ and depth $z$. These distributions come from 18 image sequences with an unconstrained cell (d), 18 image sequences with a crossbow-shaped cell (e) and 22 image sequences with a disk-shaped cell (f). The box and whisker plots of the condition differences of the spatial distribution of moving Rab6-positive membranes with respect to radius $r$, angle $\theta$ and depth $z$ for unconstrained (d), crossbow- (e) and disk- (f) shaped cells are next to the histograms and densities. p values under conditions of one-sided Wilcoxon signed-rank test when considering the condition differences are indicated below the box and whisker plots. A star (*) indicates that the p value is smaller than 0.05.

![Figure 4.](https://cdn.elifesciences.org/articles/32311/elife-32311-fig4-v1.jpg)

**Figure 4.:** (a) Illustration of the displacement distance and the total path length of a trajectory. The confinement ratio is defined as the ratio between the displacement distance and the total path length. (b-d) Histograms (bar plots) and densities (lines) showing the radial distribution of confinement ratio (b), total path length (c) and lifetime (d) for trajectories of Rab6-positive membranes. These distributions come from the grouping of 18 image sequences with unconstrained cells, 18 image sequences with crossbow-shaped cells and 22 image sequences with disk-shaped cells. (e) Box and whisker plots showing the condition differences of the radial distribution of confinement ratio (CR), total path length (TPL) and lifetime (LT) for trajectories of Rab6-positive membranes. p values under conditions of one-sided Wilcoxon signed-rank test when considering the condition differences are indicated below the box and whisker plots. A star (*) indicates that the p value is smaller than 0.05.

### The endosomal recycling compartment organizes Rab11 angular distribution

Rab11-positive recycling membranes originate their journey from the so-called endosomal recycling compartment (ERC). We formulate the assumption that Rab11 positive membranes are uniformly distributed at the membrane plane around the ERC position within the cell, whatever the cell shape is. To test this hypothesis, we used images acquired at the membrane with TIRF microscopy showing Rab11 proteins (see Appendix 1—figure 1 c–d). Most labeled membranes of the ERC are not located near the cell surface. However, for each TIRF sequence, one highly inclined wide field image was also acquired, enabling to visually define its location (red disks in Figure 5a). To test our assumption, the QuantEv uniformity analysis is applied by considering intensity on segmented regions. The results are shown in Figure 5a (blue disks). To have a line of comparison, we also plot the cell centers as green disks in Figure 5a. Interestingly, the blue disk is close to the red disk for all image sequences except one (second line, middle image in Figure 5a). The blue disk is also closer to the red disk than the green disk in seven out of eight image sequences (see Figure 5a–b). Although the point that gives the most uniform angular distribution does not strictly coincide with the manually identified ERC, it is sufficiently close to indicate that the Rab11-positive membranes are quite uniformly distributed around the ERC position at the membrane plane whatever the cell shape is. This indicates that the ERC corresponds to the organizing hub of the Rab11 carrier vesicles.

![Figure 5.](https://cdn.elifesciences.org/articles/32311/elife-32311-fig5-v1.jpg)

**Figure 5.:** (a) The red disks correspond to the manual annotation, the blue disks to the point defining the most uniform angular distribution of Rab11-positive membranes and the green disks correspond to the cell centers. These disks are displayed over the average intensity projections of the image sequences showing Rab11-positive membranes. The scale bar corresponds to 5 $\mu$m. (b) Euclidean distances between the manually annotated ERC and the cell centers (green disks) or the points giving the most uniform angular distribution (blue disks).

### Joint actin disruption and cell shape influence on Rab11 radial distribution

Applying the QuantEv uniformity analysis at each time step of a sequence allows studying the location stability of the particle emitter or attractor. To test if the estimated ERC location is stationary over time, we computed the Euclidean distance between the reference point estimated at time t = 0 and the points estimated for the next frames. In untreated cells, this distance remains stable (see Figure 6 green line). We analyzed cells treated with Latrunculin A, which inhibits actin polymerization (see Appendix 1—figure 1 e–f). We show that the ERC location is moving away as the drug is affecting the cell (see Figure 6 blue and orange lines), enlightening the role of cytoskeleton in stabilizing the cellular localization of the ERC. We then acquired image sequences of unconstrained, crossbow-shaped and disk-shaped cells at 10 and 15 min after Latrunculin A addition, and we extracted Rab11 trajectories. The confinement ratio of Rab11 tracks is decreasing with time (see Figure 7), which is consistent with actin cytoskeleton being involved in Rab11 vesicle trafficking, as already reported (Schafer et al., 2014). The radial distribution of Rab11 vesicles is constantly shifting from the cell periphery to the cell center for unconstrained, crossbow- and disk-shaped cells (see Figure 8a). However, before and at drug injection time, we observe significant differences in radial distributions between the three tested conditions (p value = 0.0023, see Figure 8b). After Latrunculin A treatment, we progressively observe no difference between the radial distributions, as the actin organization is drastically perturbed. Together, these quantifications allow us to conclude that exocytosis/recycling vesicle trafficking is dependent on both cell shape and actin organization.

![Figure 6.](https://cdn.elifesciences.org/articles/32311/elife-32311-fig6-v1.jpg)

**Figure 6.:** Average Euclidean distance between the point giving the most uniform distribution at time t = 0 and the point estimated at further frames for untreated disk-shaped cells (four image sequences) and cells treated with Latrunculin A (six image sequences for each micro-pattern).

![Figure 7.](https://cdn.elifesciences.org/articles/32311/elife-32311-fig7-v1.jpg)

**Figure 7.:** (a-c) Histograms (bar plots) and densities (lines) of the confinement ratio of Rab11 positive membranes on unconstrained (a), crossbow- (b) and disk- (c) shaped cells at Latrunculin A Injection Time, 10 and 15 min after injection. (d) Box and whisker plots of the corresponding condition differences (five image sequences for unconstrained cells, 10 image sequences for crossbow-shaped cells and nine image sequences for disk-shaped cells). p values under conditions of one-sided Wilcoxon signed-rank test when considering the condition differences are indicated below the box and whisker plots. A star (*) indicates that the p value is smaller than 0.05.

![Figure 8.](https://cdn.elifesciences.org/articles/32311/elife-32311-fig8-v1.jpg)

**Figure 8.:** (a) Histograms (bar plots) and densities (lines) of the radial distribution of Rab11-positive membranes on unconstrained, crossbow- and disk-shaped cells at Latrunculin A Injection Time, 10 and 15 min after injection. (b) Box and whisker plots of the condition differences of the radial distribution between unconstrained, crossbow- and disk-shaped cells at Latrunculin A Injection Time, 10 and 15 min after injection. p values under conditions of one-sided Wilcoxon signed-rank test when comparing unconstrained, crossbow- and disk-shaped cells (five image sequences for unconstrained cells, ten image sequences for crossbow-shaped cells and nine image sequences for disk-shaped cells) are indicated below the box and whisker plots.

## Discussion

This article presents a computational framework taking into account cell variability to quantify the distribution of fluorescently labeled proteins. Using dynamical descriptors, detailed insight into dynamical processes is also unraveled and the uniformity analysis allows to localize an organizing region for the observed biological objects.

Additionally to the input image, the user has to define three other inputs that depend on the biological application. First, the user has to decide which coordinate system to use. If the imaged cells are flat as in this study (see Appendix 1—figure 1a–c), a cylindrical coordinate system is well suited while a spherical coordinate system will fit better rounded cells. If the user is not familiar with cylindrical or spherical coordinate systems, a classical Cartesian system is also available, even though less suited to intracellular spatial distribution. Finally, QuantEv also allows to analyze the spatial distribution with respect to a reference point or to membrane borders (Heride et al., 2010). Once the reference coordinate system is chosen, the user has to define a reference point, typically the particle emitter or attractor, and a reference direction in order to fairly compare cells. For example, in this study, the direction between the Golgi and the cell center were used to define a reference direction for unconstrained and disk-shaped cells while the crossbow principal axis was used for crossbow-shaped cells.

As intensity is proportional to the amount of proteins in fluorescence microscopy, using intensity observed in segmented areas is potentially more informative than binary segmentation masks. However, because of phenomena such as photobleaching, phototoxicity, shading, uneven illumination etc., appropriate normalization procedures within and between images need to be applied. If the user is able to correct for these phenomena, it is preferable to use intensity as weights in QuantEv analysis. Otherwise, intensity weights should be avoided.

Given its genericity, QuantEv can easily be applied to any intracellular event and gives useful insights about their spatial distribution across conditions. From these observations, the user can then apply more sophisticated analyses such as mechanistic models of dynamics (Ponti et al., 2004; Jaqaman et al., 2008) or generative models (Li et al., 2012; Johnson et al., 2015a, Johnson et al., 2015b). QuantEv analysis conclusions can also be the starting point of a new modeling.

We demonstrate with the help of QuantEv that the distributions of Rab6-positive membranes from unconstrained, crossbow- and disk-shaped cells are statistically different. QuantEv also enables to identify the locations where Rab6-positive membranes enter their docking phase. By considering the directions of the moving Rab6-positive membranes, QuantEv allows demonstrating that these membranes first move predominantly and directly toward the cell periphery before reaching their docking phase. They then go back to the cell center in an undirected and long fashion. This intriguing result showing statistically bi-directional movements of Rab6 was reported before. The Rab6-positive vesicles generated at the Golgi membranes are predestined to the cell periphery, in order to deliver their exocytic cargo (Grigoriev et al., 2007; Grigoriev et al., 2011), which should favor a centrifuge directionality. Our data reconciles this two apparently opposed observations and show for the first time, that a majority of Rab6 vesicles reverses their movement only toward close docking-fusion sites and only during this ultimate phase of docking-fusion.

QuantEv also demonstrates that Rab11 positive membranes are uniformly distributed around the ERC at the plasma membrane plane. This shows that the ERC represents an organizing hub for the Rab11 carrier vesicles. By applying the QuantEv uniformity analysis along time, we exhibit how the ERC location is affected by actin disruption caused by Latrunculin A injection. The radial distribution analysis of Rab11-positive membranes combined with Latrunculin A injection reveals a dual regulation by cell shape and actin organization on Rab11 trafficking at the plasma membrane, and more generally on the exocytosis/recycling vesicle distribution.

In conclusion, QuantEv has the potential to become a very popular analysis method for dynamics and intracellular event analysis as (i) it is publicly available; (ii) it is fully automated and semi-parametric; (iii) it provides results that are easy to biologically interpret; (iv) it performs a statistical analysis that takes into account the biological variability over the replicated experiments of a same condition and is efficient with small and large amounts of data. On a biological prospective beyond the two particular models presented here, QuantEv will be of great interest for studies where quantitative and statistical analysis of intracellular membrane or particle behaviors are required, depending on physical and external constraints. For instance, in single-cell experiments performed in microfluidics devices, QuantEv will efficiently provide automation and diversity of statistical analyses in ‘one shot’, for a relatively small amount of data. Applying QuantEv in multi-cellular systems, in which cell-cell constraints necessarily affect molecular distribution and particle movements will also be of great interest. Finally, in vivo imaging of single-cell intracellular processes in a very confined and constrained environment will benefit from the generic aspect of the QuantEv sensing and measuring of particle spatial distributions, dynamical measures with respect to intracellular localization and cell to cell variability. An Icy plugin and a tutorial are available at http://icy.bioimageanalysis.org/plugin/QuantEv. A QuantEv analysis module is available on TrackMate and a QuantEv track processor is available in Icy.

## Materials and methods

### Sample preparation

In the first dataset, we use cell lines stably expressing fluorescently tagged proteins in order to minimize the cell-to-cell variability in fluorescence signal. HeLa cells stably expressing fluorescently tagged GFP-RAB6A were previously generated in the Lab at Institut Curie (Teber et al., 2005). They were maintained in DMEM supplemented with 10% fetal bovine serum. Cells were then spread onto fibronectin Cytoo chips (Cytoo Cell Architect) 4 to 5 hr before imaging. Cell adhesion on micro-patterns both constrains the cells in terms of lateral movement and averages their size and shape (disk-shaped and crossbow-shaped, Cytoo Cell Architect, 1100$\mu$ m$^{2}$). As a control of patterning effect, the same cell line was grown under the same culture conditions, and spread on regular glass coverslips, 4 to 5 hr before imaging.

For a second set of experiments, wild-type RPE1 cells (hTERT RPE-1 obtained from ATCC collection) were grown in Dulbecco’s Modified Eagle Medium, Nutrient Mixture F-12 (DMEM/F12) supplemented with 10% (vol/vol) FCS in six-well plates. RPE1 cells were transiently transfected with plasmids coding for Rab11a-GFP, and Langerin-mCherry using the following protocol: 2 $\mu$g of each DNAs, completed to 100 $\mu$L with DMEM/F12 (FCS free) were incubated for 5 min at room temperature. 6 $\mu$L of X-tremeGENE 9 DNA Transfection Reagent (Roche) completed to 100 $\mu$L with DMEM/F12 (FCS free) were added to the mix and incubated for further 15 min at room temperature. The transfection mix was then added to RPE1 cells grown 1 day before and incubated further at 37$^{o}$C overnight. Cells were then spread on regular coverslips or onto fibronectin Cytoo chips (Cytoo Cell Architect) for 4 hr at 37$^{o}$C with F-12 (with 10% (vol/vol) FCS, 10 mM Hepes, 100 units/ml of penicillin and 100 ug/ml of Strep) before imaging. When specified, 2 mM Latrunculin A (Sigma) was dissolved to 0.02 mM in F-12 DMEM. 300 $\mu$L of culture medium with Latrunculin A (600 nM) was added to establish a final Latrunculin A concentration of 3 $\mu$M.

All cell lines were routinely tested for mycoplasma, using PCR or the MycoAlert Mycoplasma Detection Assay.

### Data acquisition

For Rab6-positive membranes in unconstrained cells, videos were recorded with an epifluorescence video automated system composed of a Ti Eclipse inverted microscope equipped with a 100x objective Plan NA (1.4) and a piezo stage for 3D acquisitions (Nikon, S.A, France). The fluorescence was collected using a 512 × 512 EM-CCD (Evolve, Photometric, USA) and driven through the Metamorph software (Molecular Devices). 18 series of 120 Z image stacks of 10 frames were recorded at a rate of about 1 stack/s. The volume rendering of one image from this dataset is shown in Appendix 1—figure 1a.

For Rab6-positive membranes on micro-patterns, the 488 nm laser of a spinning-disk confocal microscope (Ti Eclipse, Nikon, S.A, France equipped with spinning disk system, a 100x/1.4 oil objective and CoolSnap HQ2 CCD, from Roper Scientific S.A.R.L, France) was used to acquire 3D 380 $\times$ 380 $\times$ 8 stacks at a rate of one stack per second. 18 image sequences with crossbow-shaped cells and 22 image sequences with disk-shaped cells were acquired. The system was driven by the Metamorph software (Molecular Devices). The volume rendering of two images from this dataset are shown in Appendix 1—figure 1b–c.

For the Rab11 dataset, live-cell imaging was performed using simultaneous dual color Total Internal Reflection Fluorescence (TIRF) microscopy. All imagings were performed in full conditioned medium at 37$^{o}$C and 5% CO2 unless otherwise indicated. Simultaneous dual color TIRF microscopy sequences were acquired on a Nikon TE2000 inverted microscope equipped with a 100x TIRF objective (NA = 1.49), an azimuthal TIRF module (Ilas2, Roper Scientifc), an image splitter (DV, Roper Scientific) installed in front of an EMCCD camera (Evolve, Photometrics) that can be bypassed or not, depending on the experimental conditions, as indicated in the text, and a temperature controller (LIS). GFP and m-Cherry were excited with a 488 nm and a 561 nm laser, respectively (100 mW). The system was driven by the Metamorph software (Molecular Devices). Four selected image projections from this data set are shown in Appendix 1—figure 1d–g.

### Data availability

We use two datasets in this study that are publicly available on the iMANAGE database at https://cid.curie.fr/iManage/standard/login.html with username public and password Welcome!1 in the project entitled QuantEv-Data.

### Event detection and localization

Before applying QuantEv, the intracellular events have to be identified and localized. The Rab6 proteins are extracted from each image sequence by using the C-CRAFT method (Pécot et al., 2015) with default parameters, except the p value that ranges from 0.0025 to 0.35 depending on the noise level, available on Icy (de Chaumont et al., 2012). The Rab11-positive membranes on micro-patterns are segmented at each time point with the ATLAS algorithm (Basset et al., 2015) with default parameters, except the p value that ranges from 0.05 to 0.45 depending on the noise level. In both cases, a variance stabilization transform (Boulanger et al., 2010) is performed to take into account the Poisson-Gaussian nature of the noise in the CCD sensors. As unconstrained cells are more mobile than cells on micro-patterns, the image sequences showing Rab11-positive membranes in unconstrained cells are not in focus. To correct this phenomenon, a deconvolution method (Lefkimmiatis et al., 2012) is first applied to the image sequences. The Rab11 positive membranes are then segmented at each time point with the Bernsen local thresholding method (Bernsen, 1986) (radius equal to 15 pixels). Finally, Rab6 and Rab11 trajectories are estimated with the multiple hypothesis tracking method developed by Chenouard et al. (2013) with default parameters, available on Icy (de Chaumont et al., 2012), the combinatorial optimization tracking method developed by Sbalzarini and Koumoutsakos (2005) with default parameters, available on ImageJ (Schneider et al., 2012) and the hybrid approach TrackMate (Tinevez et al., 2017) that first connects detected points into short tracks and then links the resulting tracks together, with default parameters, available on Fiji (Schindelin et al., 2012). To identify the trajectories estimated with different methods, we use the gated distance (Chenouard et al., 2014) defined between two trajectories $\theta_{1}$ and $\theta_{2}$ as:

$$
d(\theta_{1},\theta_{2})=\sumt=0T min(||\theta_{1}(t)−\theta_{2}(t)||_{2},ϵ),
$$

where $ϵ$ is the gate. For each image sequence, the gated distance is computed between the trajectories estimated with the three different methods with $ϵ=5$ pixels. Only the trajectories for which the gated distance is inferior to 2 pixels for at least two methods are used for the analysis.

### Weighted density estimation for spatial localization

The localization of events needs to be defined on a common coordinate system to compare the experiments. We propose to use the cylindrical coordinate system where only a reference point such as the event emitter or attractor and a reference direction have to be specified by the user. To fairly compare experiments with different cell shapes, we define appropriate distances to obtain normalized densities, that is independent from the cell shape. We illustrate the importance of shape normalization in Appendix 2.

More formally, let us define $Ω$ the 3D cell support and $\partialΩ$ the 3D cell surface. Let us consider a set of $N$ sample points associated with intracellular events $S={(r_{i},\theta_{i},z_{i},w_{i},d_{\theta_{i}},d_{z_{i}}),i\in[1,N]}$, where $(r_{i},\theta_{i},z_{i})$ denote the spatial cylindrical coordinates. The weight $w_{i}$ enables to take into account features associated to events such as intensity, track length, confinement ratio... $w_{i}$ can typically be a function of fluorescence intensity, proportional to the number of molecules observed at a given location. The distance $d_{\theta_{i}}$ is equal to the Euclidean distance between the coordinate system origin $O\inΩ$ projected on plane $z_{i}$ ($O_{z_{i}}$) and the point $P_{\theta_{i},z_{i}}\in\partialΩ$ with angle $\theta_{i}$ at plane $z_{i}$, such that $d_{\theta_{i}}=||P_{\theta_{i},z_{i}}−O_{z_{i}}||_{2}^{2}$. The distance $d_{z_{i}}$ is equal to the Euclidean distance between the coordinate system origin $O$ and the point $P_{r_{i},\theta_{i}}\in\partialΩ$ with radius $r_{i}$ and angle $\theta_{i}$ such that $d_{z_{i}}=||P_{r_{i},\theta_{i}}−O||$. These two distances allow estimating normalized densities that are independent from cell shapes. We propose to estimate three densities defined as follows:

$$
f(r)=\frac{1}{Z_{r,\theta}}\sumi=1N G_{\sigma^_{r}}(r_{i}−r)\frac{w_{i}}{d_{\theta_{i}}},
$$



$$
f(\theta)=\frac{1}{Z_{r,\theta}}\sumi=1N H_{κ^}(\theta_{i}−\theta)\frac{w_{i}}{d_{\theta_{i}}},
$$



$$
f(z)=\frac{1}{Z_{z}}\sumi=1N G_{\sigma^_{z}}(z_{i}−z)\frac{w_{i}}{d_{z_{i}}},
$$

where $G_{\sigma^}(⋅)$ is a Gaussian kernel with bandwidth $\sigma^$, $H_{κ^}$ is a von Mises kernel with concentration $κ^$ such that $H_{κ^}(\theta)=\frac{e^{κ^cos\theta}}{2\piI_{0}(κ^)}$ and $I_{0}(⋅)$ is the Bessel function of order 0. The bandwidths $\sigma^_{r}$ and $\sigma^_{z}$ are estimated with the Silverman’s rule of thumb (Silverman, 1986) and $κ^$ is estimated using the robust rule of thumb proposed by Taylor (2008). The normalization constants are defined as follows:

$$
Z_{r.\theta}=N\sumi=1N\frac{w_{i}}{d_{\theta_{i}}},Z_{z}=N\sumi=1N\frac{w_{i}}{d_{z_{i}}}.
$$

### Density estimation for dynamical features

In case the distribution of dynamical features such as confinement ratio or lifetime with respect to the track localization is to be studied, the weighted densities are defined differently than in the previous section. In this case, histograms are first computed as the averaged dynamic features for each bin. A density estimation is then estimated from the histograms.

Let us consider a set of $T$ tracks associated with spatial coordinates $T={(r_{i},\theta_{i},z_{i},m_{i}),i\in[1,T]}$, where $(r_{i},\theta_{i},z_{i})$ denote the spatial cylindrical coordinates of the median point of the trajectory $i$ and $m_{i}$ is a dynamic feature associated to track $i$. The histograms corresponding to the averaged dynamic features for each bin are defined as:

$$
h_{r}(b_{r})=\frac{\sumiT𝟙_{b_{r}}[r_{i}]m_{i}}{\sumiT𝟙_{b_{r}}[r_{i}]},
$$



$$
h_{\theta}(b_{\theta})=\frac{\sumiT𝟙_{b_{\theta}}[\theta_{i}]m_{i}}{\sumiT𝟙1_{b_{\theta}}[\theta_{i}]},
$$



$$
h_{z}(b_{z})=\frac{\sumiT𝟙_{b_{z}}[z_{i}]m_{i}}{\sumiT𝟙_{b_{z}}[z_{i}]},
$$

where $b_{r}\in[1,B_{r}]$ is a radius bin and $B_{r}$ is the total number of radius bins, $b_{\theta}\in[1,B_{\theta}]$ is a polar bin and $B_{\theta}$ is the total number of polar bins, $b_{z}\in[1,B_{z}]$ is an in-depth bin and $B_{z}$ is the total number of in-depth bins, and $1_{b_{r}}[r_{i}]$ is equal to $1$ if $r_{i}$ is defined in bin $b_{r}$ and equal to 0$0$ otherwise. Densities are then estimated from the histograms as follows:

$$
f_{d}(r)=\sumi=1B_{r} G_{\sigma^_{r}}(h_{r}(b_{i})−r),
$$



$$
f_{d}(\theta)=\sumi=1B_{\theta} H_{κ^}(h_{\theta}(b_{i})−\theta),
$$



$$
f_{d}(z)=\sumi=1B_{z} G_{\sigma^_{z}}(h_{z}(b_{i})−z),
$$

where $G_{\sigma^}(⋅)$ is a Gaussian kernel with bandwidth $\sigma^$, $H_{κ^}$ is a von Mises kernel with concentration $κ^$. The bandwidths $\sigma^_{r}$ and $\sigma^_{z}$ are estimated with the Silverman’s rule of thumb (Silverman, 1986) and $κ^$ is estimated using the robust rule of thumb proposed by Taylor (2008).

### Statistical procedure

Quantitative comparison between different conditions is mandatory to analyze biological data. In most computational biology studies, data from different experiments corresponding to the same condition are pooled together (Schauer et al., 2010; Merouane et al., 2015). This usual procedure enables to add statistical power when comparing two conditions. Therefore, it is especially useful when few data are available. Unfortunately, pooling data together presents two main drawbacks. First, if large amounts of data are available, the opposite problem arises and the statistical tests may become significant for every comparison (Olivier and Walter, 2015). One solution is to down sample the data, but the amount of down sampling becomes another issue. Second, pooling data together for one condition partially hides the variability between the replicated experiments for this condition. As an example, let us consider a study aimed at analyzing the effects of a drug on a sample of normal individuals. To evaluate the drug efficiency, a comparison between normal individuals and individuals that were administered the drug is conducted. Let us assume that the drug is effective on half the individuals. Consequently, normal individuals are compared to a mix of normal individuals and individuals with the drug effects. This comparison should not be statistically significant as the drug is not efficient on all individuals. However, the effects on the individuals for which the drug is efficient might hide the fact that it is not efficient on all individuals if all the data are pooled together. In what follows, we propose to compute a distance between all experiments instead of a distance between conditions. The idea is demonstrated in Appendix 3 and validated on synthetic image sequences (see Appendix 1—figure 1c–d and Appendix 3).

### Distance between densities

We propose to compute the earth mover’s distance (also known as the Kantorovich-Rubinstein or the first order Wasserstein distance) between every replicate of every condition to apply a statistical test. This transport-based distance demonstrated its efficiency for other studies on cell phenotypes (Wang et al., 2013; Basu et al., 2014). The discrete Earth Mover’s Distance (EMD) between two unidimensional distributions is simply defined as the sum of the absolute differences between their cumulated distribution functions (Rubner et al., 2000):

$$
EMD(f^{1},f^{2})=\sumi=1K |F^{1}(i)−F^{2}(i)|,
$$

where $F^{1}$ and $F^{2}$ are the cumulated distribution functions of $f^{1}$ and $f^{2}$. Although the EMD depends on the number of bins $K$, EMD proportions are kept intact when the number of bins is high enough as shown in Appendix 4. For the angular distribution, the Circular Earth Mover’s Distance (CEMD) (Rabin et al., 2011) is defined as:

$$
CEMD(f^{1},f^{2})=mink\in{1,⋯,K}\sumi=1K |Q_{k}^{1}(i)−Q_{k}^{2}(i)|,
$$

with

$$
Q_{k}(i)={\sumj=ki f(j)ifi\geqk,\sumj=kK f(j)+\sumj=1i f(j)ifi<k.
$$

### Difference between conditions

The EMD and CEMD enable to compute a distance between two single experiments for the radial, angular and in-depth densities. The distances between the replicates of one condition and the replicates of the other condition(s) give an idea about the difference between the conditions. However, a baseline distance is also needed to state if the difference is random or significant. Therefore, two distances are defined for each experiment and each density:

Considering more than two groups does not change the intra-condition distance and only expands the inter-condition distance to more than one group. We define as the condition difference the difference between the inter-condition distance and the intra-condition distance. If the condition difference is high, the conditions are different.

### Statistical test

A statistical test is applied on the difference distance to state if the observed conditions are significantly different. A non-parametric statistical test is better suited as there is no underlying model for the condition difference. In addition, a negative condition difference implies that the current experiment is closer to the replicated experiments of the other condition than the replicated experiments of the same condition. Consequently, the condition difference has to be positive if the conditions are different. For those two reasons, we propose to use the one-sided non-parametric Wilcoxon signed-rank test on the condition differences for all experiments to state if two conditions are statistically different.

### Analysis of uniform distribution of events

In case we focus on the intracellular events assumed to be uniformly distributed around a given biological object, for example the events emitter, QuantEv allows us to estimate a location for this traffic-organizing component. This source location is then defined as the reference point with the most uniform angular distribution. It is established that the maximum entropy corresponds to the most uniform distribution. Consequently, the reference point $O^{∗}$ is defined as the location that maximizes the entropy:

$$
O^{∗}=maxO\inΩ−\sumi=1Nf(\theta_{i})logf(\theta_{i}).
$$

The most straightforward way to find this point is to estimate the entropy map that gives, for each point in $Ω$, the entropy value computed with the current point used as the reference center. We also propose to use the bisection method to speed up the computation (about sixty times faster than the entropy map computation, see Appendix 5—table 1). A uniformity analysis conducted on simulations is presented in Appendix 6. The entropy criterion can be extended to detect multiple organizing components if needed.

### Code availability

The jar file of the QuantEv Icy plugin is available at http://icy.bioimageanalysis.org/plugin/QuantEv. The jar file of the QuantEv track processor is available at http://icy.bioimageanalysis.org/plugin/ QuantEv _(track_processor). The source codes can be extracted from the jar files. The QuantEv analysis module for TrackMate is available on GitHub (Pécot, 2018; copy archived at https://github.com/elifesciences-publications/QuantEvForTrackMate). These codes are released under the GNU Affero General Public License v3.0.
