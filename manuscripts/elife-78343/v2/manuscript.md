# Fat2 polarizes the WAVE complex in trans to align cell protrusions for collective migration

## Authors

- Audrey Miller Williams<sup>1</sup> ([ORCID: 0000-0001-6170-3365](https://orcid.org/0000-0001-6170-3365))
- Seth Donoughe<sup>1</sup> ([ORCID: 0000-0002-4773-5739](https://orcid.org/0000-0002-4773-5739))
- Edwin Munro<sup>1</sup>
- Sally Horne-Badovinac<sup>1</sup> ([ORCID: 0000-0002-0473-7451](https://orcid.org/0000-0002-0473-7451)) †

### Affiliations

1. Department of Molecular Genetics and Cell Biology, University of Chicago Chicago United States ([ROR:024mw5h28](https://ror.org/024mw5h28))
2. Committee on Development, Regeneration, and Stem Cell Biology, University of Chicago Chicago United States ([ROR:024mw5h28](https://ror.org/024mw5h28))
3. Institute for Biophysical Dynamics, University of Chicago Chicago United States ([ROR:024mw5h28](https://ror.org/024mw5h28))

† Corresponding author

## Abstract

For a group of cells to migrate together, each cell must couple the polarity of its migratory machinery with that of the other cells in the cohort. Although collective cell migrations are common in animal development, little is known about how protrusions are coherently polarized among groups of migrating epithelial cells. We address this problem in the collective migration of the follicular epithelial cells in Drosophila melanogaster. In this epithelium, the cadherin Fat2 localizes to the trailing edge of each cell and promotes the formation of F-actin-rich protrusions at the leading edge of the cell behind. We show that Fat2 performs this function by acting in trans to concentrate the activity of the WASP family verprolin homolog regulatory complex (WAVE complex) at one long-lived region along each cell’s leading edge. Without Fat2, the WAVE complex distribution expands around the cell perimeter and fluctuates over time, and protrusive activity is reduced and unpolarized. We further show that Fat2’s influence is very local, with sub-micron-scale puncta of Fat2 enriching the WAVE complex in corresponding puncta just across the leading-trailing cell-cell interface. These findings demonstrate that a trans interaction between Fat2 and the WAVE complex creates stable regions of protrusive activity in each cell and aligns the cells’ protrusions across the epithelium for directionally persistent collective migration.

## Introduction

Collective cell migration is essential for a variety of morphogenetic processes in animals (Friedl and Gilmour, 2009; Scarpa and Mayor, 2016; Norden and Lecaudey, 2019; Perez-Vale and Peifer, 2020). As with individual cell migrations, adherent collective migrations are driven by the concerted action of cell protrusions, contractile actomyosin networks, and adhesions to a substrate (Scarpa and Mayor, 2016; Bodor et al., 2020; Buttenschön and Edelstein-Keshet, 2020). To move forward, individual cells polarize these structures along a migratory axis, and to move persistently in one direction, they need to maintain that polarity stably over time (Stock and Pauli, 2021). Collective cell migrations introduce a new challenge: to move together, the group of migrating cells must be polarized in the same direction (Stock and Pauli, 2021). Otherwise, they would exert forces in different directions and move less efficiently, separate, or fail to migrate altogether.

The epithelial follicle cells of the Drosophila melanogaster ovary are a powerful experimental system in which to investigate how local interactions among migrating cells establish and maintain group polarity. Follicle cells are arranged in a continuous, topologically closed monolayer epithelium that forms the outer cell layer of the ellipsoidal egg chamber—the organ-like structure that gives rise to the egg (Duhart et al., 2017; Figure 1A–C). The apical surfaces of follicle cells adhere to a central germ cell cluster, and their basal surfaces face outward and adhere to a surrounding basement membrane extracellular matrix. The follicle cells migrate along this stationary basement membrane, resulting in rotation of the entire cell cluster (Haigo and Bilder, 2011). As the cells migrate, they secrete additional basement membrane proteins (Haigo and Bilder, 2011). The coordination of migration with secretion causes the cells to produce a basement membrane structure that channels tissue growth along one axis (Gutzeit et al., 1991; Haigo and Bilder, 2011; Isabella and Horne-Badovinac, 2016; Crest et al., 2017). Follicle cell migration lasts for roughly 2 days, and the migration direction—and resulting direction of egg chamber rotation—is stable throughout (Chen et al., 2017; Stedden et al., 2019). The edgeless geometry of the epithelium means cells are not partitioned into ‘leader’ and ‘follower’ roles, and there is no open space, chemical gradient, or other external guidance cue to dictate the migration direction. Instead, this feat of stable cell polarization and directed migration is accomplished through local interactions between the migrating cells themselves (Barlan et al., 2017; Stedden et al., 2019).

![Figure 1.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig1-v2.jpg)

**Figure 1.:** (A) Diagram of a stage 6 egg chamber in cross-section. Anterior is left, posterior right. (B) Three-dimensional diagram of an egg chamber with the anterior half shown. Arrows indicate the migration of follicle cells along the basement membrane and the resulting rotation of the egg chamber around its anterior-posterior axis. (C) Diagram of three follicle cells. Their apical surfaces adhere to the germ cells and their basal surfaces adhere to the basement membrane. The dashed line represents the basal imaging plane used throughout this study except where indicated. (D) Images of the leading edges of two cells expressing Ena-GFP and WAVE complex label Abi-mCherry, and with F-actin stained with phalloidin. (E) Diagrams showing the organization of F-actin and its regulators at the leading edge. The WAVE complex builds a lamellipodial actin network, within which Ena builds filopodia. (F) Images of F-actin (phalloidin) and cell interfaces (anti-Discs Large) in control, ena-RNAi, and abi-RNAi backgrounds. Expression of ena-RNAi strongly depletes filopodia, revealing the less-prominent lamellipodial actin network, whereas abi-RNAi expression removes both filopodia and lamellipodia.

Follicle cell migration is driven, in part, by lamellipodial protrusions that extend from the leading edge of each cell (Gutzeit et al., 1991; Cetera et al., 2014). Lamellipodia are built by the WASP family verprolin homolog regulatory complex (WAVE complex) (Miki et al., 1998; Miki et al., 2000), which is a protein assembly composed of five subunits: SCAR/WAVE, Abi, Sra1/Cyfip, Hem/Nap1, and HSPC300 (Chen et al., 2010). The WAVE complex adds branches to actin filaments by activating the Actin-related proteins-2/3 complex (Arp2/3) and elongates existing filaments, building the branched actin network that pushes the leading edge forward (Machesky et al., 1999; Bieling et al., 2018; Mullins et al., 2018). Embedded within the lamellipodia are Enabled (Ena)-dependent filopodia, which are visually prominent with F-actin labeling but dispensable for migration (Cetera et al., 2014; Figure 1D and E). Removal of filopodia reveals the underlying lamellipodial actin network, whereas removal of WAVE complex subunits eliminates all protrusive structures (Cetera et al., 2014; Figure 1F). We use the term ‘protrusions’ to encompass both of these F-actin networks and the membrane deformations they cause.

The follicle cells align their protrusions across the tissue, a form of planar polarity (Gutzeit et al., 1991; Cetera et al., 2014). The atypical cadherin Fat2 is required both for this planar polarity and for collective migration to occur (Viktorinová et al., 2009; Viktorinová and Dahmann, 2013; Horne-Badovinac, 2017). Fat2 is planar-polarized to the trailing edge of each cell (Viktorinová and Dahmann, 2013), where it promotes the formation of protrusions at the leading edge of the cell immediately behind (Barlan et al., 2017). Interestingly, in addition to migration depending on polarized Fat2 activity, Fat2’s planar polarity also depends on epithelial migration (Barlan et al., 2017). It is not known how Fat2 regulates lamellipodia or cell polarity, or how these processes influence one another. We hypothesized that Fat2 acts as a coupler between tissue planar polarity and cell protrusion by polarizing WAVE complex activity to the leading edge of each cell. To test this, we used genetic mosaic analysis and quantitative imaging of fixed and live tissues to dissect Fat2’s contributions to protrusivity and protrusion polarity at cell and tissue scales.

We show that Fat2 signals in trans, entraining WAVE complex activity to one long-lived region along each cell’s leading edge. Without Fat2, the WAVE complex accumulates transiently at different regions around the cell perimeter, and cell protrusivity is reduced and unpolarized. The interaction between Fat2 and the WAVE complex is non-cell-autonomous but very local, with sub-micron-scale puncta of Fat2 along the trailing edge concentrating the WAVE complex just across the cell-cell interface, at the tips of filopodia embedded within the lamellipodium. These findings demonstrate how an intercellular interaction between Fat2 and the WAVE complex promotes cell protrusivity, stabilizes regions of protrusive activity along the cell perimeter, and aligns protrusions across the epithelium by coupling leading and trailing edges. Fat2-WAVE complex interaction thereby stabilizes the planar polarity of protrusions for directionally persistent collective migration.

## Results

### Fat2 increases and polarizes protrusions at the basal surface of the follicular epithelium

Recent work has shown that Fat2 regulates migration of the follicular epithelium by polarizing F-actin-rich protrusions; specifically, Fat2 at the trailing edge of each cell causes protrusions to form at the leading edge of the cell behind it, and without Fat2, protrusions are reduced or lost (Squarr et al., 2016; Barlan et al., 2017). Beyond this qualitative description, it is not known how Fat2 modulates cell protrusion.

We sought to obtain a deeper, time-resolved view of the role of Fat2 in regulating protrusivity and protrusion distribution. To do so, we developed methods to segment cell membrane extensions and measure their lengths and orientations, and applied these methods to timelapse movies of the basal surface of control and fat2N103-2 epithelia (a null allele, hereafter referred to as fat2; Figure 2, Figure 3). A detailed description of the segmentation approach is included in the Materials and Methods. To analyze these data, we first measured the average lengths of membrane extensions from all cell-cell interfaces (Figure 3A and B). The distribution of measured lengths was unimodal, with no natural division between protrusive and non-protrusive interfaces. Therefore, to establish an empirically grounded cutoff between these categories, we recorded timelapse movies of control epithelia treated with the Arp2/3 inhibitor CK-666, which are non-migratory and almost entirely non-protrusive (Cetera et al., 2014). We used measurements from CK-666-treated epithelia to set a cutoff for the minimum length of a protrusion: any edges with membrane extensions longer than the 98th percentile of those in CK-666-treated epithelia were considered protrusive for subsequent analysis (Figure 3B).

![Figure 2.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig2-v2.jpg)

**Figure 2.:** Top row shows an example of a pair of neighboring cells in which one cell is protruding across their shared interface. Bottom row shows a case in which both cells are protruding across the interface. (A) Cell interfaces and protrusions were labeled with a membrane dye and timelapses of the basal surface were collected. (B) Cells were automatically segmented with a watershed-based method, and segmentation errors were hand-corrected. (C) The bright interface region between each pair of neighboring cells was identified using a watershed-based method. This region includes the interface and any membrane protrusions that extend across it. (D) An enlargement of the boxed regions of (C). (E) The interface region was divided into two parts by the shortest path from vertex to vertex within the region, which approximates the true cell-cell interface position. The two resulting regions were then assigned to the cell from which they each extended. The area of these regions and the length of the interface between them were used to define average membrane extension length (as described in Materials and methods). (F) The tip and base of each region were identified, and then used to measure lengths and orientations (see Materials and methods).

![Figure 3.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig3-v2.jpg)

**Figure 3.:** (A) Timelapse frames of control, fat2, and CK-666-treated epithelia labeled with a membrane dye. Middle row shows segmented edges. Protrusive edges, defined as edges with average membrane extension lengths longer than the 98th percentile of those of CK-666-treated epithelia, are shown in red. Non-protrusive edges are white. Bottom row shows arrows indicating the orientation of each protrusion overlaid on labeled cell membrane. Arrows originate at protrusion bases and have lengths proportional to protrusion lengths. See related Figure 3—video 1 and Figure 3—video 3. (B) Histogram showing the distribution of average membrane extension lengths. The 98th percentile length threshold for CK-666-treated epithelia is indicated. (C) Plot showing the ratio of protrusive to total edges. The protrusivity of fat2 epithelia is variable, with a distribution overlapping with control and CK-666-treated epithelia. Welch’s ANOVA (W(2,9.3)=15.89, p=0.0012) with Dunnet’s T3 multiple comparisons test; n.s. p=0.07, *p=0.04, **p=0.004. Bars indicate mean ± SD. Counts of protrusive and total edges are listed in Figure 3—source data 1. See Figure 3—figure supplement 1 for alternate measurements of protrusivity. (D) Polar histograms of the distribution of protrusion orientations in control and fat2 epithelia. Anterior is left, posterior is right, and in control epithelia images were flipped as needed so that migration is always oriented downward. Bar areas scale with the fraction of protrusions. Protrusion counts are listed are in Figure 3—source data 1. Control protrusions point predominantly in the direction of migration, whereas fat2 protrusions are less polarized. Histograms from individual epithelia can be found in Figure 3—figure supplement 1.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Plot showing the ratio of protrusive to total edges, with protrusivity defined in terms of membrane extension longest length (see Methods). In agreement with the average length definition, the protrusivity of fat2 epithelia is variable, with a distribution overlapping with control and CK-666-treated epithelia. Counts of protrusive and total edges are listed in Figure 3—source data 1. Welch’s ANOVA (W(2,9.4)=22.25, p=0.0003) with Dunnet’s T3 multiple comparisons test; n.s. p=0.16, *p=0.011, **p=0.0019. (B) Plot showing the mean membrane extension lengths of control, fat2, and CK-666-treated egg chambers, with membrane extension length defined as average length (see Materials and methods). With this cutoff-independent protrusivity measurement, the protrusivity of fat2 egg chambers is intermediate between control and CK-666, with a wider distribution that overlaps both. Welch’s ANOVA [W(2,9.7)=13.59, p=0.0015] with Dunnet’s T3 multiple comparisons test; n.s. p=0.076, *p=0.042, **p=0.0019. A,B, Bars indicate mean ± SD. (C) Polar histograms showing the distribution of membrane protrusion orientations in individual control and fat2 egg chambers. Anterior is left, posterior is right, and images were flipped as needed so that migration is downward for control epithelia, in which membrane protrusions are biased in the direction of migration. Bar areas scale with the fraction of protrusions. Protrusion counts are listed are in Figure 3—source data 1. In fat2 epithelia, protrusions have varying levels of axial bias and little or no vectorial bias.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Images showing phalloidin staining of F-actin in control, fat2, and abi-RNAi-expressing epithelia. Bottom row shows the same images with displayed brightness increased. (B) Examples of segmented cell-cell interfaces or medial basal surfaces overlayed on F-actin. (C) Plot of the difference in F-actin fluorescence intensity between cell interfaces and medial basal surfaces shows that while fat2 and abi-RNAi epithelia have less F-actin interface enrichment than control epithelia, F-actin interface enrichment remains higher in fat2 epithelia than abi-RNAi epithelia. Welch’s ANOVA [W(2, 19.84)=94.68, p<0.0001] with Dunnet’s T3 multiple comparisons test; *p=0.033, ****p<0.0001. (D) Frames from timelapse movies of control, fat2, and abi-RNAi epithelia with F-actin labeled with F-Tractin-tdTomato. As with phalloidin staining, the protrusivity of fat2 epithelia is intermediate between that of control and abi-RNAi epithelia. Brightness display settings vary between genotypes to correct for variability in F-Tractin-tdTomato expression levels. See related Figure 3—video 2. (E) Plot of F-actin fluorescence intensity at cell interfaces as a function of interface angular distance from horizontal. Bar areas are rescaled so that the mean in each condition is one. (F) Plot of the F-actin fluorescence intensity ratio between near-horizontal (0–10) and near-vertical (80-90) interfaces, corresponding with leading-trailing and side interfaces, respectively, in migratory control epithelia. F-actin is enriched along near-horizontal interfaces in control, but not fat2, egg chambers. Control-fat2 comparisons: unpaired t-test, ****p<0.0001. Comparison between fat2 and one (dashed line, the expectation if there is no enrichment): one sample t-test, n.s. p=0.88. (C,F) Bars indicate mean ± SD.

Using this quantification approach, we first asked how tissue protrusivity was affected by the loss of Fat2. We found that the protrusivity of fat2 epithelia was lower than that of control epithelia on average, but highly variable, with overlap between the protrusivity distributions of both untreated and CK-666-treated epithelia (Figure 3B and C; Figure 3—figure supplement 1A,B; Figure 3—video 1). As a complementary method, we also measured protrusivity via F-actin labeling in fixed and live tissues, using abi-RNAi-expressing epithelia as a nearly non-protrusive benchmark. The results largely paralleled those seen with membrane labeling (Figure 3—figure supplement 2; Figure 3—video 2); however, the disparity in protrusivity between fat2 and control epithelia appeared larger when measured using F-actin labeling than when measured with membrane labeling (Figure 3C; Figure 3—figure supplement 2). Images of follicle cell protrusions visualized by F-actin staining are dominated by fluorescence from filopodia (Figure 1F). The appearance of lower protrusivity of fat2 epithelia as measured with an F-actin label may therefore indicate that filopodia are disproportionately reduced by loss of Fat2. Altogether, these data show that fat2 epithelia are less protrusive than control epithelia, but do retain some protrusive activity.

These results raised an important question—if some fat2 epithelia have levels of membrane protrusivity comparable to that of control epithelia, then why do all fat2 epithelia fail to migrate (Viktorinová and Dahmann, 2013; Chen et al., 2017; Barlan et al., 2017)? We hypothesized that the mispolarization of protrusions across the tissue contributes to fat2 migration failure. In control epithelia, the majority of protrusions were polarized in the direction of migration, orthogonally to the egg chamber’s anterior-posterior axis (Figure 3A and D; Figure 3—figure supplement 1C; Figure 3—video 3). In contrast, in fat2 epithelia, protrusions were fairly uniformly distributed in all directions or biased in two opposite directions (Figure 3A and D; Figure 3—figure supplement 1C; Figure 3—video 3). Where an axial bias was present, the axis was inconsistent between egg chambers. We also confirmed this finding using F-actin labeling of protrusions. To compare the planar polarity of F-actin protrusions between control and fat2 epithelia, we measured F-actin enrichment at cell-cell interfaces as a function of the angle of the interface relative to the egg chamber’s anterior-posterior axis. We again saw that protrusions were planar-polarized in control epithelia and unpolarized in fat2 epithelia (Figure 3—figure supplement 2). These data show that Fat2 is required to polarize protrusions in a common direction across the epithelium.

Because Fat2 regulates both follicle cell migration and planar polarity, and migration and planar polarity are interdependent (Viktorinová et al., 2009; Viktorinová and Dahmann, 2013; Cetera et al., 2014; Barlan et al., 2017), the unpolarized protrusions of fat2 epithelia could be a cause or a consequence of inability of fat2 epithelia to migrate. To distinguish between these possibilities, we exploited the fact that small groups of fat2 cells can be carried along by neighboring non-mutant, migratory cells (Viktorinová and Dahmann, 2013), allowing us to evaluate polarity of protrusions from fat2 cells in a migratory context. We generated fat2 mosaic tissues that had sufficiently small fractions of mutant cells that the tissue as a whole still migrated, and found that fat2 cells in these tissues were often protrusive, but their protrusions were not polarized in the direction of migration (Figure 4; Figure 4—video 1). This demonstrates that Fat2 does not simply polarize protrusions indirectly by maintaining tissue-wide migration. Rather, Fat2 is required at the scale of groups of cells to polarize those cells’ protrusions in alignment with the direction of collective migration.

![Figure 4.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig4-v2.jpg)

**Figure 4.:** (A) Timelapse frame of a fat2 mosaic epithelium with cell membrane labeled, used to evaluate protrusion orientations in control or fat2 cells within a migratory context. Boxes indicate examples of leading-trailing interfaces between neighbor pairs with each possible combination of genotypes. Representative of 9 similar timelapse movies. See related Figure 4—video 1. (B) Larger images of the interfaces boxed in (A) showing that protrusions are misoriented when fat2 cells are ahead of the interface regardless of the genotype of the cell behind the interface. Arrows point in the direction of protrusion.

### Fat2 increases and polarizes the WAVE complex at the basal surface of the follicular epithelium

Follicle cell protrusions are built by the WAVE complex (Cetera et al., 2014), which commonly acts in a circuit with active Rac and PI(3,4,5)P3. We hypothesized that Fat2 polarizes protrusions by polarizing the distribution of one of these circuit components. To visualize their activity, we focused on the WAVE complex, whose localization most closely determines and reports sites of protrusion. Using CRISPR/Cas9, we endogenously tagged the WAVE complex subunit Sra1 with eGFP (hereafter: Sra1-GFP), allowing us to visualize its localization and dynamics at endogenous levels.

We confirmed that Sra1-GFP flies are viable and fertile when the tagged allele is homozygous, Sra1-GFP localizes to follicle cell leading edges like other WAVE complex labels (Cetera et al., 2014; Squarr et al., 2016), its localization depends on WAVE complex subunit Abi, and F-actin protrusions appear normal (Figure 5A and B; Figure 5—figure supplement 1A-C). Migration was slower when Sra1-GFP was present in two copies (Figure 5—figure supplement 1D), so we performed all subsequent experiments with one copy of Sra1-GFP.

![Figure 5.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig5-v2.jpg)

**Figure 5.:** (A) Diagram showing Fat2 localization at the trailing edge and WAVE complex at the leading edge of the basal surface of follicle cells. The WAVE complex subunits referenced in this paper listed. (B) Images of an Sra1-GFP mosaic epithelium with phalloidin-stained F-actin, showing Sra1-GFP enrichment at leading edges (filled arrows) and not trailing edges (open arrows). (C) Images of a fat2 mosaic epithelium with phalloidin-stained F-actin. Filled arrows indicate leading edges of fat2 cells behind control cells, where protrusions are present. Open arrows indicate leading edges of control cells behind fat2 cells, where protrusions are reduced. (D) Images of a fat2 mosaic epithelium expressing Sra1-GFP. Filled arrows indicate leading edges of fat2 cells behind control cells. Open arrows indicate leading edges of control cells behind fat2 cells. (E,F) Quantification of Sra1-GFP mean fluorescence intensity in fat2 mosaic epithelia along leading-trailing interfaces (E) or medial basal surfaces (F) Diagrams to the left of plots show the measured regions with respect to control (cyan) and fat2 (gray) cells. The genotype(s) of cells in each measured category are shown below the x-axis. Lines connect measurements from the same egg chamber. (E) Sra1-GFP is reduced at the leading edge of cells of any genotype behind fat2 cells. Repeated measures ANOVA [F(3,80)=22.77, p<0.0001] with post-hoc Tukey’s test; n.s. (left to right) p=0.99, 0.24, ****p<0.0001. (F) Sra1-GFP is not significantly changed at the medial basal surface of fat2 cells. Paired t-test; n.s. p=0.08.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Images comparing the localization of markers of WAVE complex subunits: Sra1-GFP, Scar antibody, and Abi-mCherry, at the basal surface (top row) and in cross-section (bottom row). (B) Images of Sra1-GFP localization in control and abi-RNAi-expressing epithelia. Sra1-GFP is dispersed in the absence of Abi. (C) Images showing phalloidin-stained F-actin in epithelia with wild-type Sra1, one or two copies of Sra1-GFP, or expressing sra1-RNAi, used to assess the appearance of protrusions in each condition. (D) Plot of migration speed of epithelia with wild-type Sra1 or one or two copies of Sra1-GFP. Migration speed is reduced when both Sra1 copies are GFP-tagged. One-way ANOVA (F(2,49)=18.37, p<0.0001) with post-hoc Tukey’s test; n.s. 0.66, ****p<0.0001. Bars indicate mean ± SD.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Images of Sra1-GFP at the basal surface in control and fat2 epithelia. (B) Examples of segmented cell-cell interfaces or medial basal surfaces overlaid on Sra1-GFP images. (C) Plot of mean Sra1-GFP fluorescence intensity across the entire basal surface (total), at cell-cell interfaces, and at medial basal surfaces in control and fat2 epithelia. One-way ANOVA (F(5,111)=63.22, p<0.0001) with post-hoc Šidák’s test; n.s. (left to right) p=0.67, 0.64, ****p<0.0001. (D) Plot of Sra1-GFP fluorescence at cell-cell interfaces as a function of interface angular distance from horizontal. Bar areas are rescaled so that the mean in each condition is one. (E) Plot of the Sra1-GFP fluorescence intensity ratio between near-horizontal (0–10) and near-vertical (80-90) interfaces, corresponding with leading-trailing and side interfaces, respectively, in migratory control epithelia. Sra1-GFP is enriched along near-horizontal interfaces in control, but not fat2, egg chambers. Control-fat2 comparison: unpaired t-test, ****p<0.0001. Comparison between fat2 and one (dashed line, the expectation if there is no enrichment): one sample t-test, n.s. p=0.052. (C,E) Bars indicate mean ± SD. F,G, Quantification of Sra1-GFP mean fluorescence intensity in fat2 mosaic epithelia along leading-trailing interfaces (F) or medial basal surfaces (G) Diagrams to the left of plots show the measured regions with respect to control (cyan) and fat2 (gray) cells. The genotype(s) of cells in each measured category are shown below the x-axis. Each column shows data from one egg chamber with points from individual cells. Bars indicate mean. Tissue summary plots in Figure 5E and F.

With an endogenous WAVE complex label in hand, we investigated how Fat2 affects WAVE complex localization. Previous work has shown that WAVE complex levels are reduced at the basal surface of follicle cells lacking Fat2 (Squarr et al., 2016). Consistent with this result, we found that Sra1-GFP levels were lower along cell-cell interfaces at the basal surface of fat2 epithelia than of control epithelia (Figure 5—figure supplement 2). Planar polarity of Sra1-GFP across the epithelium was also lost in the absence of Fat2 (Figure 5—figure supplement 2). Fat2 acts non-cell-autonomously to cause protrusions to form at the leading edge of the cell just behind (Barlan et al., 2017; Figure 5C), so we next tested the hypothesis that Fat2 localizes the WAVE complex to the leading edge in the same non-cell-autonomous pattern. We did this using fat2 mosaic epithelia, in which we could measure Sra1-GFP levels at leading-trailing interfaces shared by control and fat2 cells. We found that Sra1-GFP levels were normally enriched along the leading edges of fat2 cells if control cells were present immediately ahead, showing that Sra1 can still localize to the leading edge of cells lacking Fat2. Conversely, Sra1-GFP levels were reduced along the leading edge of control cells if fat2 cells were immediately ahead (Figure 5D and E; Figure 5—figure supplement 2). We also observed a corresponding non-autonomous pattern of membrane protrusion polarity in timelapse movies of fat2 mosaic epithelia (Figure 4; Figure 4—video 1). We conclude that Fat2 acts non-cell-autonomously to localize the WAVE complex to leading edges, resulting in tissue-wide planar polarization of protrusive activity, and thereby in collective cell migration.

We next asked if, by recruiting the WAVE complex to the leading edge, Fat2 was reducing its levels at other membrane sites, and thereby suppressing mispolarized protrusion. To test whether Fat2 was measurably depleting the non-leading-edge WAVE complex pool, we compared the level of Sra1-GFP at the medial basal surfaces of cells in control or fat2 epithelia, or between control and fat2 cells in mosaic epithelia (see diagram in Figure 5F). In both cases, we measured small increases in mean Sra1-GFP in fat2 cells compared to control cells, but these were not statistically significant (Figure 5D and F; Figure 5—figure supplement 2). Our measurements may not be sensitive enough to detect redistribution of Sra1-GFP occurring across a broad membrane area, or the Sra1-GFP population may be redistributing away from the basal surface. It therefore remains to be determined whether by concentrating the WAVE complex at the leading edge, Fat2 also depletes the WAVE complex from other membrane sites, and thereby suppresses mispolarized protrusions.

### Fat2 stabilizes a region of WAVE complex enrichment and protrusivity in trans

In individually migrating cells, the excitable dynamics of the WAVE complex and its regulators enable it to form transient zones of enrichment along the cell perimeter even in the absence of a directional signal (Weiner et al., 2007; Iglesias and Devreotes, 2012; Stock and Pauli, 2021). Although the planar-polarized distribution of the WAVE complex across the epithelium was lost in fat2 mutant tissue, we wondered (1) whether the WAVE complex could still form regions of enrichment in individual cells and (2) whether these WAVE complex-enriched regions were active and responsible for templating unpolarized protrusions. To evaluate the WAVE complex distribution along the edges of individual cells, we generated entirely fat2 mutant epithelia in which patches of cells expressed Sra1-GFP. At cell-cell interfaces along Sra1-GFP expression boundaries, we found that the boundary cells often had cortical regions devoid of Sra1-GFP (Figure 6A). This observation shows that the WAVE complex is not uniformly localized around the cortex and can form regions of enrichment without Fat2. We also saw that Sra1-GFP enrichment coincided with the presence of F-actin protrusions (Figure 6A), indicating that the WAVE complex in these regions is active. To confirm that the WAVE complex builds the protrusions in fat2 epithelia, we co-imaged Sra1-GFP and a membrane label, and found that Sra1-GFP was enriched at the tips of membrane protrusions (Figure 6—figure supplement 1; Figure 6—video 1). These data indicate that the WAVE complex can still accumulate and build protrusions in the absence of Fat2, tissue-wide planar polarity, and collective cell migration.

![Figure 6.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig6-v2.jpg)

**Figure 6.:** (A) Images of phalloidin-stained F-actin and mosaically expressed Sra1-GFP in an entirely fat2 mutant epithelium. Filled and open arrows indicate genotype boundary interfaces with and without Sra1-GFP enrichment, respectively. Sra1-GFP enrichment is heterogeneous, and interfaces with Sra1-GFP enrichment have more F-actin protrusions. (B) Timelapse frames of Sra1-GFP in control and fat2 epithelia. Top row shows Sra1-GFP with arrows indicating regions of Sra1-GFP enrichment; bottom row shows Sra1-GFP and outlines of cell perimeters used to make kymographs. Laser intensity and brightness display settings differ between genotypes. See related Figure 6—video 2. (C) Diagram of cell perimeter unrolling for kymograph generation. Red represents planar-polarized Sra1 as distributed before and after unrolling. (D) Kymographs of Sra1-GFP fluorescence intensity along cell perimeter outlines exemplified in (C). The y-axis length of regions of high Sra1-GFP enrichment reports their stability over time. Control cells have Sra1-GFP regions along leading-trailing interfaces that are stable over 20 minutes. In fat2 cells, Sra1-GFP-enriched regions are less stable. The arrow indicates a transient accumulation of Sra1-GFP at a control cell side. These occur occasionally, and their stability is similar to Sra1-GFP regions in fat2 cells. (E) Timelapse frame of a fat2 mosaic epithelium in which all cells express Sra1-GFP, used to evaluate Sra1-GFP dynamics in control or fat2 cells within a migratory context. Boxes indicate a leading-trailing interface between two control cells (blue) or fat2 cells (green). Representative of 9 similar timelapse movies. See related Figure 6—video 3. (F) Larger images of the interfaces boxed in (E), taken 9.8 min apart. Sra1-GFP is initially enriched along both interfaces. It remains enriched in the control interface throughout, but loses enrichment along the fat2 interface.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Timelapse frames showing pairs of cell interfaces from control or fat2 epithelia expressing Sra1-GFP and labeled with a membrane dye. Arrows indicate membrane protrusions. Sra1-GFP is enriched at protrusion tips in both control and fat2 epithelia. See related Figure 6—video 1.

A striking feature of migrating follicle cells is the stable polarization of their protrusive leading edges. It is not known whether Fat2 contributes to the stabilization of protrusive regions in addition to positioning them. If so, the positions of WAVE complex-enriched, protrusive regions of fat2 epithelia should fluctuate more than those of control epithelia, in addition to being less well-polarized at the tissue level. To see if this is the case, we acquired timelapse movies of Sra1-GFP and monitored its distribution along cell perimeters over time. In control epithelia, Sra1-GFP was strongly enriched along leading-trailing interfaces relative to side interfaces over the 20-min timelapse. Side interfaces were mostly devoid of Sra1-GFP, except for infrequent Sra1-GFP accumulations that persisted for several minutes (Figure 6B–D; Figure 6—video 2). In contrast, in fat2 epithelia, the regions of greatest Sra1-GFP enrichment along the cell perimeter changed substantially over the 20-min timelapse and multiple Sra1-GFP-enriched regions were often present simultaneously in individual fat2 cells. Sra1-GFP accumulated in these regions, typically spreading outward along the membrane as it did so, and then dissipated. These events had a duration that was comparable to the transient accumulations of Sra1-GFP at side interfaces in control cells (Figure 6B–D; Figure 6—video 2). Because all cell-cell interfaces in fat2 epithelia and side interfaces in control epithelia lack Fat2, this suggests a several-minutes timescale over which regions of WAVE complex enrichment can persist without stabilization by Fat2. Live imaging of Sra1-GFP in fat2 mosaic epithelia yielded similar information—Sra1-GFP enrichment fluctuated more at interfaces between fat2 cells than interfaces between control cells despite both being in a migratory tissue (Figure 6E and F; Figure 6—video 3).

To see if Fat2’s role stabilizing the WAVE complex distribution translates to a role stabilizing protrusive regions, we returned to our timelapse movies of membrane protrusions in control and fat2 epithelia, this time focusing on the protrusions’ dynamics rather than their distribution. In control cells, protrusion polarity appeared largely stable over the 20-min duration of our timelapse movies, whereas in fat2 cells it often shifted substantially. In some fat2 epithelia, protrusion positions shifts were largely restricted to two opposite-facing cell edges, whereas in others, protrusions positions shifted seemingly at random (Figure 7A, Figure 7—video 1). To evaluate the stability of protrusion polarity quantitatively, we measured the frequency of interface protrusion polarity ‘switches’, in which first one cell and then its neighbor protruded across their shared interface (Figure 7B). These events were rare in control epithelia, with ∼2% of interfaces switching polarity per hour. In contrast, they were more common in fat2 epithelia, with ∼60% of interfaces switching polarity per hour (Figure 7C). Together, these observations show that, in addition to polarizing the WAVE complex and protrusive activity to the leading edge, Fat2 stabilizes their distributions for repeated cycles of protrusion from one long-lived cell region (Figure 7D).

![Figure 7.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig7-v2.jpg)

**Figure 7.:** (A) Timelapse frames of control and fat2 epithelia labeled with a membrane dye, showing the position of a cell’s protrusions over time. Top row shows the interfaces and protrusions of one cell and its neighbors. Segmented membrane extensions originating from the center cell (red) are overlaid in the bottom row. Arrows indicate sites of membrane protrusion. In the control cell, protrusion position is stable, whereas in fat2 cells it shifts either along a fixed axis (middle) or seemingly at random (right). See related Figure 7—video 1. (B) Example in which one cell and then its neighbor protrudes across a shared interface (a ‘polarity switch’). The row shows timelapse frames of an interface and associated protrusions from a fat2 epithelium labeled with membrane dye. Arrows originate in the protruding cell and point in the direction of protrusion. The bottom row shows corresponding diagrams of the interface with F-actin-rich protrusions illustrated in yellow. (C) Plot showing the frequency of interface protrusion polarity switches (exemplified in B) in timelapse movies of control and fat2 epithelia. Polarity switches occur more frequently at fat2 interfaces than control ones. Unpaired t-test; ***p=0.0002. Bars indicate mean ± SD. (D) Diagram showing the proposed role of Fat2 stabilizing a region of WAVE complex enrichment and protrusivity. Without Fat2, WAVE complex-enriched, protrusive regions are reduced and more transient.

### Fat2 and the WAVE complex colocalize across leading-trailing cell-cell interfaces

Finally, we explored how Fat2 recruits the WAVE complex across the cell-cell interface. To constrain the set of possible mechanisms, we assessed the spatial scale of their interaction. Fat2 has a punctate distribution along each cell’s trailing edge (Viktorinová and Dahmann, 2013; Barlan et al., 2017), so we asked whether Fat2 recruits the WAVE complex locally to these sites, or recruits it more broadly to the entire interface. We evaluated the colocalization between Fat2 and the WAVE complex along leading-trailing interfaces, visualizing Fat2 with an endogenous 3xeGFP tag (Fat2-3xGFP) and the WAVE complex with mCherry-tagged Abi under control of the ubiquitin promoter (Abi-mCherry). Like Fat2-3xGFP, Abi-mCherry formed puncta, and Abi-mCherry and Fat2-3xGFP puncta strongly colocalized (Spearman’s r=0.71 ± 0.04; Figure 8A–E). Abi-mCherry colocalized significantly less strongly with uniformly-distributed E-cadherin-GFP (Spearman’s r=0.49 ± 0.07; Figure 8—figure supplement 1,B), indicating that Fat2-3xGFP-Abi-mCherry colocalization was not simply a byproduct of curved membrane morphology or our measurement approach. In timelapse movies, Fat2-3xGFP and Abi-mCherry puncta moved together through cycles of protrusion extension and retraction (Figure 8B; Figure 8—video 1). Short-lived Abi-mCherry accumulations formed infrequently at cell sides away from Fat2, similar to the Sra1-GFP side accumulations we described earlier (Figure 6D; Figure 8—figure supplement 1; Figure 6—video 2; Figure 8—video 2). Together, these findings suggest that Fat2 recruits the WAVE complex locally, at the scale of individual puncta, with the WAVE complex occasionally ‘escaping’ Fat2-dependent concentration at the leading edge.

![Figure 8.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig8-v2.jpg)

**Figure 8.:** (A) Images of cells expressing Abi-mCherry and endogenous full-length Fat2-3xGFP or endogenous Fat2-3xGFP lacking the intracellular domain (Fat2ΔICD), used to assess colocalization. (B) Timelapse frames showing the leading-trailing interfaces of two cells expressing Fat2-3xGFP and Abi-mCherry, showing their colocalization over time. See related Figure 8—video 1. (C) Image showing the leading-trailing interface region used in (D); it is also an example of a region used in (E). (D) Line scan showing the fluorescence intensity of Fat2-3xGFP, Abi-mCherry, and F-actin (phalloidin) along the leading-trailing interfaces of the two cells in (C) showing their corresponding peaks of enrichment. (E) Plot of Spearman’s correlation coefficients of Fat2-3xGFP or Fat2ΔICD-3xGFP and Abi-mCherry showing no significant difference in colocalization. Bars indicate mean ± SD. One-way ANOVA (F(5,81)=44.86, p=0.0164 with Figure 8—figure supplement 1) with post-hoc Tukey’s test; n.s. p>0.99. (F) Image showing the distribution of Fat2-3xGFP, Abi-mCherry, and F-actin (phalloidin) at the leading-trailing interface and along the boxed filopodium. (G) Plot showing fluorescence intensity of traces of F-actin, Abi-mCherry, and Fat2-3xGFP showing their relative sites of enrichment along the length of filopodia. Lines and shaded regions indicate mean ± SD. n=74 protrusions (used for SD), 18 cells, 1 cell/egg chamber. (H) Diagram of proposed organization of Fat2, the WAVE complex, and F-actin along the leading-trailing interface based on the present data and previously published work (Viktorinová and Dahmann, 2013; Cetera et al., 2014; Barlan et al., 2017). Fat2 puncta at the trailing edge colocalize with WAVE complex puncta at the leading edge, ahead of filopodia embedded within the lamellipodium.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/78343/elife-78343-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** (A) Images of cells expressing Fat2-3xGFP and Abi-mCherry in control, lar, and ena-RNAi backgrounds (top 3 rows) or E-cadherin-GFP and Abi-mCherry (bottom row, negative control for colocalization measurements). (B) Plot of Spearman’s correlation coefficients of Abi-mCherry and Fat2-3xGFP (or Fat2ΔICD-3xGFP) (gray background) or E-cadherin-GFP (white background) along leading-trailing interfaces show that Fat2 and Abi colocalize in all four conditions more strongly than E-cadherin and Abi. One-way ANOVA (F(5,81)=44.86, p=0.0164) with post-hoc Tukey’s test; n.s. (left to right) p>0.99, p=0.41, **p<0.0046, ****p<0.0001. (A,B) Control, Fat2-3xGFP, and Abi-mCherry images and Spearman’s coefficients are also in Figure 8A and E. (C) Timelapse frames of a side-facing cell-cell interface from an epithelium expressing Abi-mCherry and Fat2-3xGFP. Arrows indicate a site of transient Abi-mCherry accumulation, protrusion, and dissipation with no corresponding Fat2-3xGFP enrichment. See related Figure 8—video 2. (D) Line scan of GFP-Ena, Abi-mCherry, and F-actin (phalloidin) fluorescence intensity along a leading-trailing interface region, showing their corresponding peaks of enrichment. (E) Image showing the GFP-Ena, Abi-mCherry, and F-actin (phalloidin) at the leading edge and in the boxed filopodium. (F) Plot of mean fluorescence intensity of F-actin, Abi-mCherry, and GFP-Ena along the length of filopodia showing their relative distribution. Lines and shaded regions indicate mean ± SD. n=54 filopodia (used for SD), 39 cells from 2 egg chambers. (G) Plot of mean fluorescence intensity of Abi-mCherry along leading-trailing interfaces in control epithelia or similarly-oriented interfaces in lar epithelia, some of which are non-migratory. B,F,G, Bars (B,G) or lines and shaded regions (F) indicate mean ± SD.

If Fat2 puncta locally recruit the WAVE complex, changing the distribution of Fat2 puncta should cause corresponding changes to the distribution of the WAVE complex. To test this, we examined follicle cells expressing an endogenous Fat2 truncation that lacks the intracellular domain (Fat2ΔICD-3xGFP), which distributes more broadly around the cell perimeter than wild-type Fat2 (Aurich and Dahmann, 2016; Barlan et al., 2017), but remains punctate. The distribution of Abi-mCherry expanded around the cell perimeter in the Fat2ΔICD-3xGFP background (Figure 8A) as was previously reported for protrusions (Barlan et al., 2017). Despite their altered distributions, Abi-mCherry puncta colocalized just as well with Fat2 $^{Δ⁢ICD}$-3xGFP puncta as with Fat2-3xGFP puncta (Spearman’s r=0.71 ± 0.04 vs 0.71±0.05; Figure 8E; Figure 8—figure supplement 1). From these data we conclude that Fat2 controls the distribution of the WAVE complex by concentrating the WAVE complex in adjacent puncta. These findings also demonstrate that the Fat2 intracellular domain is dispensable for Fat2-WAVE complex interaction in collectively migrating follicle cells.

Ena-dependent filopodia are embedded within and grow from the lamellipodia (Cetera et al., 2014). The WAVE complex interacts with Ena and is required for the filopodia to form (Cetera et al., 2014; Chen et al., 2014b), so we asked whether the distribution of Fat2-WAVE complex puncta is related to the distribution of filopodia. Labeling filopodia tips with a GFP-tagged Ena transgene (GFP-Ena) and comparing the localization of Abi-mCherry and F-actin to either GFP-Ena or to Fat2-3xGFP, we found that the sites of highest Fat2-3xGFP and Abi-mCherry enrichment coincided with filopodia tips (Figure 8C, D and F; Figure 8—figure supplement 1). Fluorescence intensity profiles along filopodia lengths showed that Fat2-3xGFP and Abi-mCherry were enriched just ahead of the F-actin-rich region (Figure 8F and G). Fat2-3xGFP was shifted slightly forward from Abi-mCherry, consistent with the separation of Fat2-3xGFP and Abi-mCherry fluorophores by a cell-cell interface (Figure 8F and G; Figure 8—figure supplement 1). This analysis demonstrates a stereotyped organization in which Fat2 and the WAVE complex are concentrated with Ena near the tips of the filopodia, with Fat2 at the trailing edge across the cell-cell interface from the leading edge components (Figure 8H).

We considered two explanations for the close spatial relationship between Fat2 puncta, WAVE complex puncta, and filopodia. Fat2 could recruit the WAVE complex locally to puncta, and WAVE complex puncta shape the distribution of filopodia. Alternatively, Fat2 could recruit the WAVE complex to the leading edge, but their colocalization in puncta be a secondary effect of the filopodia, perhaps caused by the known interaction between Ena and Abi (Chen et al., 2014b) or by deformation of the leading-trailing interface. To rule out a dependence on filopodia, we measured colocalization between Fat2-3xGFP and Abi-mCherry in ena-RNAi-expressing epithelia, in which filopodia are strongly depleted (Cetera et al., 2014; Figure 1F). Despite the loss of filopodia, both Fat2-3xGFP and Abi-mCherry remained punctate, and their colocalization was only slightly reduced (Spearman’s r=0.71 ± 0.04 vs 0.65±0.03, Figure 8—figure supplement 1,B). We therefore rule out Ena or the filopodia themselves as required mediators of the spatial relationship between Fat2 and the WAVE complex, and infer that Fat2-WAVE complex colocalization is indicative of Fat2 recruitment of the WAVE complex locally to these sites.

Altogether, we propose that Fat2 acts locally, at the scale of individual Fat2 puncta, to concentrate the WAVE complex in adjacent puncta across the cell-cell interface. Because Fat2 puncta are distributed along the trailing edge, this has the broader effect of stabilizing a region of WAVE complex enrichment at the leading edge.

## Discussion

This work demonstrates that a trans interaction between the atypical cadherin Fat2 and the WAVE complex can stabilize WAVE complex polarity for directed cell migration. Fat2, localized to the trailing edge of each cell, recruits the WAVE complex to the leading edge of the cell behind, just across their shared interface. By concentrating WAVE complex activity in a restricted region, Fat2 strongly biases lamellipodia and filopodia to form at these leading edge sites, stably polarizing overall cell protrusive activity to one cell side. Because the Fat2-WAVE complex signaling system is deployed at each leading-trailing interface in a planar-polarized manner, it both polarizes protrusions within individual cells and aligns these individual cell polarities across the epithelium. This allows the cells to exert force in a common direction and achieve a highly coordinated collective cell migration.

While the molecular players differ, local coupling of leading and trailing edges through asymmetric interactions across their shared interface is a recurring motif in studies of epithelial collective cell migrations. In an epithelial cell culture model of collective migration, asymmetric pulling forces across cell-cell interfaces polarize Rac1 activity and cell protrusion (Das et al., 2015). In another model, one cell’s lamellipodium is stabilized by confinement under the trailing edge of the cell ahead, reinforcing interface asymmetry (Jain et al., 2020). In an endothelial collective cell migration model, asymmetric membrane ‘fingers’ containing VE-cadherin extend from the trailing edge and are engulfed by the leading edge of the cell behind, whose movement they help guide (Hayer et al., 2016). These types of leading-trailing edge coupling systems could operate together with longer-range cues to reinforce the planar polarity of cells’ migratory structures. In migrations with a closed topology and no extrinsic directional cues, such as that of the follicle cells, local polarity coupling may be especially critical for collective migration.

Our development of new computational tools to segment and quantify membrane protrusion dynamics in a collectively-migrating epithelium has led to new insights into how Fat2 regulates protrusions. We found that without Fat2, protrusivity was reduced, and the distribution of remaining protrusions expanded around the cell periphery. Therefore, Fat2 not only promotes protrusion at the leading edge, but also restricts protrusion to that edge. Analysis of fat2 mosaic epithelia revealed that Fat2 acts locally to enforce this restriction—even in the context of a globally planar-polarized, migratory epithelium, cells lacking input from Fat2 in the cell ahead were unable to polarize their protrusions in the direction of migration. Although protrusions were no longer biased in one direction without Fat2, the presence of axial orientation bias in a subset of fat2 epithelia indicates that some form of Fat2-independent planar polarity was still present. This could be mediated by undiscovered planar signaling molecules or by a mechanical cue such as tension transmitted between cells. Investigating the cell-cell communication that gives rise to this layer of planar polarity will be an interesting area for future research.

Excitable WAVE complex activity underlies lamellipodial protrusion (Weiner et al., 2007; Xiong et al., 2010; Graziano and Weiner, 2014), and WAVE complex activity is often entrained by directional cues from the environment (Millius et al., 2009; Xiong et al., 2010; Huang et al., 2013; Hayashi et al., 2014). We hypothesize that Fat2 acts as a similar activity-entraining directional cue in follicle cells. Excitable WAVE complex dynamics were especially apparent in our data in contexts where Fat2 was absent from the cell-cell interface—either at interfaces between cells in fat2 epithelia, or at protrusive side interfaces we observed with low frequency in control cells. In both contexts, the WAVE complex accumulated at an edge region, spread laterally along the membrane, and then dissipated. This corresponded with the initiation, growth, and collapse of a protrusion. Where Fat2 was present, the WAVE complex distribution along the cell perimeter stayed more constant and WAVE complex levels fluctuated in place, but did not appear to spread laterally. These findings, along with the loss of cell and tissue-scale WAVE complex polarization in the absence of Fat2, suggest that Fat2 acts by concentrating WAVE complex activity in a narrow region, thereby polarizing protrusions to a single leading edge.

How might Fat2 locally concentrate the WAVE complex? The WAVE complex is activated by recruitment to the plasma membrane (Oikawa et al., 2004; Lebensohn and Kirschner, 2009; Chen et al., 2010). Positive regulators of WAVE complex accumulation include active Rac, phosphatidylinositol (3,4,5)-triphosphate (PIP3), membrane-localized proteins that directly bind the WAVE complex, and the WAVE complex itself (Miki et al., 1998; Steffen et al., 2004; Oikawa et al., 2004; Sossey-Alaoui et al., 2005; Weiner et al., 2006; Nakao et al., 2008; Namekata et al., 2010; Graziano and Weiner, 2014; Chen et al., 2014a). We propose that Fat2 promotes WAVE complex accumulation within a stable region by acting through one or more of these positive regulators, thereby controlling the site where the WAVE complex excitation threshold is crossed and a protrusion is formed. Under this model, in the absence of Fat2, this site selection instead becomes more stochastic and therefore long-lasting protrusive regions cannot form. If part of the WAVE complex circuit is limiting for protrusion formation, this could also account for Fat2’s ability to suppress protrusion formation away from the leading edge. However, there are other possible suppression mechanisms. For example, in neutrophils, protrusions have been shown to increase membrane tension and thereby suppress distant protrusion, enforcing the selection of a single protrusive region (Houk et al., 2012).

Fat2 acts at the trailing edge of each cell to recruit the WAVE complex in trans, so there must be one or more transmembrane proteins at the leading edge of each cell that bridge this interaction. Previous work has shown that the receptor tyrosine phosphatase Lar is part of this bridge—Fat2 recruits Lar to each follicle cell’s leading edge (Barlan et al., 2017), and in Lar’s absence both WAVE complex levels and cell protrusions are reduced (Barlan et al., 2017; Squarr et al., 2016; Figure 8—figure supplement 1). However, the WAVE complex that persists at the leading edges of lar cells still colocalizes with Fat2 (Figure 8—figure supplement 1). Therefore, there must be at least one other transmembrane protein that works alongside Lar to mediate the Fat2-WAVE complex interaction. Identifying the missing leading edge protein(s) will be important to fully understand how Fat2 shapes WAVE complex activity.

Fat2 is localized in puncta along each cell’s trailing edge (Viktorinová and Dahmann, 2013; Barlan et al., 2017), and we show here that these puncta correspond 1:1 with regions of high WAVE complex enrichment just across the leading-trailing cell-cell interface. Fat2’s punctate distribution and its levels along cell-cell interfaces are unaffected by loss of the WAVE complex (Barlan et al., 2017), indicating that Fat2 puncta shape the distribution of the WAVE complex and protrusions, not the reverse. We further show that the puncta sit at the tips of filopodia that form within the lamellipodial actin network. Filopodia are a prominent feature of the long-lived protrusive regions that form in wild-type epithelia, but appear to be disproportionately reduced in the short-lived, fluctuating protrusive regions that form in fat2 epithelia. We therefore propose that by concentrating the WAVE complex and/or stabilizing its distribution, Fat2 also facilitates filopodia formation. It should be noted, however, that the filopodia are dispensable for collective follicle cell migration (Cetera et al., 2014), so the reason these structures form remains to be determined.

Why, and how, is Fat2 localized in puncta? Cadherins commonly form puncta, though the causes and functions of this organization vary (Truong Quang et al., 2013; Rubinstein et al., 2017; Li et al., 2021). For example, Flamingo (or mammalian Celsr1), an atypical cadherin and central component of the core planar cell polarity pathway, is stabilized by clustering, and this clustering is important for its planar polarization (Strutt et al., 2011; Cho et al., 2015; Stahley et al., 2021). In future work, it will be important to determine how Fat2 assembles in puncta, and whether this local clustering is important for its polarization to trailing edges or its effect on the organization of leading edges. More broadly, it will be critical to determine how Fat2 achieves its trailing edge localization, a necessary step in the polarization of the tissue.

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
      <td>Gene (Drosophila melanogaster)</td>
      <td>Abi</td>
      <td>NA</td>
      <td>FLYB:FBgn0020510</td>
      <td>FlyBase Name: Abelson interacting protein</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>Dlg</td>
      <td>NA</td>
      <td>FLYB:FBgn0001624</td>
      <td>FlyBase Name: discs large 1</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>E-cadherin</td>
      <td>NA</td>
      <td>FLYB:FBgn0003391</td>
      <td>FlyBase Name: shotgun</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>Ena</td>
      <td>NA</td>
      <td>FLYB:FBgn0000578</td>
      <td>FlyBase Name: enabled</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>Fat2 (kug)</td>
      <td>NA</td>
      <td>FLYB:FBgn0261574</td>
      <td>FlyBase Name: kugelei</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>Lar</td>
      <td>NA</td>
      <td>FLYB:FBgn0000464</td>
      <td>FlyBase Name: Leukocyte-antigen- related-like</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>Scar</td>
      <td>NA</td>
      <td>FLYB:FBgn0041781</td>
      <td>FlyBase Name: SCAR</td>
    </tr>
    <tr>
      <td>Gene (Drosophila melanogaster)</td>
      <td>Sra1 (CYFIP)</td>
      <td>NA</td>
      <td>FLYB:FBgn0038320</td>
      <td>FlyBase Name: Cytoplasmic FMR1 interacting protein</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Abi-mCherry or ubi &gt;Abi-mCherry</td>
      <td>Bloomington Drosophila Stock Center; FLYB:FBrf0227194 (S. Huelsmann)</td>
      <td>FLYB:FBst0058729; BDSC:58729</td>
      <td>FlyBase Symbol: P{Ubi-mCherry.Abi}3</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>abi-RNAi</td>
      <td>National Institute of Genetics, Japan</td>
      <td>FLYB:FBtp0079430; NIG:9749 R</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>E-cadherin-GFP</td>
      <td>Bloomington Drosophila Stock Center; PMID:19429710</td>
      <td>FLYB:FBst0060584; BDSC:60584</td>
      <td>FlyBase Genotype: y[1] w*; TI{TI}shg[GFP]</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>GFP-Ena or ubi &gt;GFP-Ena</td>
      <td>Bloomington Drosophila Stock Center; FLYB:FBrf0208868 (S. Nowotarski and M. Peiger)</td>
      <td>FLYB:FBst0028798; BDSC:28798</td>
      <td>FlyBase Genotype: w*; P{Ubi-GFP.ena}3</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>ena-RNAi</td>
      <td>Vienna Drosophila Resource Center</td>
      <td>FLYB:FBst0464896; VDRC:43058</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Fat2-3xGFP FRT80B</td>
      <td>Laboratory of S. Horne-Badovinac; PMID:28292425</td>
      <td>FLYB:FBal0326664</td>
      <td>FlyBase Symbol: kug[3xGFP]</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Fat2ΔICD-3xGFP FRT80B</td>
      <td>Laboratory of S. Horne-Badovinac; PMID:28292425</td>
      <td>FLYB:FBal0326665</td>
      <td>FlyBase Symbol: kug[ΔICD.3xGFP]</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>fat2 or fat2N103-2 FRT80B</td>
      <td>Laboratory of Sally Horne-Badovinac; PMID:22413091</td>
      <td>FLYB:FBal0267777</td>
      <td>FlyBase Symbol: kug[N103-2]</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS &gt;Flp</td>
      <td>Bloomington Drosophila Stock Center; PMID:9584125</td>
      <td>FFLYB:FBst0004539; BDSC:4539</td>
      <td>FlyBase Genotype: y[1] w[*]; PUAS-FLP.DJD1</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>FRT80B</td>
      <td>Bloomington Drosophila Stock Center; PMID:8404527</td>
      <td>FLYB:FBti0002073</td>
      <td>FlyBase Symbol: P{neoFRT}80B</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>UAS &gt;F-Tractin-tdTomato</td>
      <td>Bloomington Drosophila Stock Center; FLYB:FBrf0226873 (T. Tootle); PMID:24995797</td>
      <td>FLYB:FBst0058989; BDSC:58989</td>
      <td>FlyBase Genotype: w*; P{UASp-F-Tractin.tdTomato}15 A/SM6b; MKRS/TM2</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>ubi &gt;GFP NLS (3 L) FRT80B</td>
      <td>Bloomington Drosophila Stock Center; FLYB:FBrf0108530 (D. Bilder and N. Perrimon)</td>
      <td>FLYB:FBst0001620; BDSC:1620</td>
      <td>FlyBase Genotype: w*; P{Ubi-GFP.D}61EF P{neoFRT}80B</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>lar13.2 FRT40A</td>
      <td>Bloomington Drosophila Stock Center; PMID:8598047</td>
      <td>FLYB:FBst0008774; BDSC8774</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>larbola1</td>
      <td>Bloomington Drosophila Stock Center; PMID:11688569</td>
      <td>FLYB:FBst0091654; BDSC:91654</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>MKRS hsFLP/TM6b, Cre</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>FLYB:FBst0001501; BDSC:1501</td>
      <td>y[1] w[67c23]; MKRS, P{hsFLP}86E/TM6B, P{Crew}DH2, Tb[1]</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>nanos-Cas9</td>
      <td>Bloomington Drosophila Stock Center; FLYB:FBrf0223952 (F. Port and S. Bullock); PMID:25002478</td>
      <td>FLYB:FBst0054591; BSDC:54591</td>
      <td>FlyBase Genotype: y[1] M{nos-Cas9.P}ZH-2A w*</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>ubi &gt;mRFP NLS (3 L) FRT80B</td>
      <td>Bloomington Drosophila Stock Center; FLYB:FBrf0210705 (J. Lipsick)</td>
      <td>FLYB:FBti0129786; BDSC:30852</td>
      <td>FlyBase Genotype: w1118; P{Ubi-mRFP.nls}3 L P{neoFRT}80B</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>FRT82b ubi &gt;mRFP NLS (3 R)</td>
      <td>Bloomington Drosophila Stock Center; FLYB:FBrf0210705 (J. Lipsick)</td>
      <td>FLYB:FBst0030555; BDSC:30555</td>
      <td>FlyBase Genotype: w1118; P{neoFRT}82B P{Ubi-mRFP.nls}3 R</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Sra1-GFP</td>
      <td>Produced for this study</td>
      <td></td>
      <td>Sra1 endogenously tagged with GFP using CRISPR. Available from Horne-Badovinac Lab upon request to shorne@uchicago.edu</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>Sra1-GFP FRT80B</td>
      <td>Produced for this study</td>
      <td></td>
      <td>Sra1 endogenously tagged with GFP using CRISPR, with FRT80B. Available from Horne-Badovinac Lab upon request to shorne@uchicago.edu</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>sra1-RNAi</td>
      <td>Bloomington Drosophila Stock Center; PMID:21460824</td>
      <td>FLYB:FBst0038294; BDSC:38294</td>
      <td>FlyBase Genotype: y[1] sc* v[1] sev[21]; P{TRiP.HMS01754}attP2</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>tj &gt;Gal4</td>
      <td>National Institute of Genetics, Japan; PMID:12324948</td>
      <td>FLYB:FBtp0089190; DGRC:104055</td>
      <td>FlyBase Symbol: P{tj-GAL4.U}</td>
    </tr>
    <tr>
      <td>Genetic reagent (Drosophila melanogaster)</td>
      <td>w1118</td>
      <td>Bloomington Drosophila Stock Center</td>
      <td>FLYB:FBal0018186</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Discs Large; Dlg (mouse monoclonal)</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>DSHB:4F3; RRID:AB_528203</td>
      <td>(1:20)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Scar (mouse monoclonal)</td>
      <td>Developmental Studies Hybridoma Bank</td>
      <td>AB_2618386</td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Alexa Fluor 647, anti-mouse secondary (donkey polyclonal)</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat:A31571; RRID:AB_162542</td>
      <td>(1:200)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CellMask Orange Plasma Membrane Stain</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat:C10045</td>
      <td>15 min (1:250)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CellMask Deep Red Plasma Membrane Stain</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat:C10046</td>
      <td>15 min (1:250)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>TRITC Phalloidin</td>
      <td>Millipore Sigma</td>
      <td>Cat:1951</td>
      <td>15 min at room temp (1:300)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Alexa Fluor 647 phalloidin</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat:C10045</td>
      <td>2 hr at room temp (1:50)</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CK-666, Arp2/3 complex inhibitor</td>
      <td>Millipore Sigma</td>
      <td>Cat:553502</td>
      <td>750 μM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Formaldehyde, 16%, methanol free, ultra pure</td>
      <td>Polysciences</td>
      <td>Cat:18814–10</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Recombinant human insulin</td>
      <td>Millipore Sigma</td>
      <td>Cat:12643</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>plasmid: pU6-BbsI-chiRNA</td>
      <td>Addgene</td>
      <td>Addgene:45946; RRID:Addgene_45946</td>
      <td>PMID:23709638</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>plasmid: pU6 chiRNA Sra1 C-term</td>
      <td>Produced for this study</td>
      <td></td>
      <td>CRISPR chiRNA construct for generation of Sra1-GFP. available from Horne-Badovinac Lab upon request to shorne@uchicago.edu</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>plasmid: pDsRed-attP</td>
      <td>Addgene</td>
      <td>Addgene:51019; RRID:Addgene_51019</td>
      <td>PMID:24478335. Vector used to make pDsRed-attP Sra1-GFP HR</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>plasmid: pTWG</td>
      <td>Drosophila Genome Resource Center</td>
      <td>DGRC:1076</td>
      <td>source of enhanced GFP for generation of Sra1-GFP</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>plasmid: pDsRed-attP Sra1-GFP HR</td>
      <td>Produced for this study</td>
      <td></td>
      <td>CRISPR homologous recombinaton construct for generation of Sra1-GFP. Available from Horne-Badovinac Lab upon request to shorne@uchicago.edu</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Zen Blue</td>
      <td>Zeiss</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MetaMorph</td>
      <td>Molecular Devices</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FIJI (ImageJ)</td>
      <td>PMID:22743772</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism 9 for Mac</td>
      <td>GraphPad Software</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Microsoft Excel for Mac, version 16.47</td>
      <td>Microsoft</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Python 3</td>
      <td>Python Software Foundation</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>imageio</td>
      <td>imageio contributors</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>matplotlib</td>
      <td>The Matplotlib Development team</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>napari</td>
      <td>napari contributors</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>numpy</td>
      <td>numpy contributors</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>pims</td>
      <td>pims contributors</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>pandas</td>
      <td>pandas contributors</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>scikit-image</td>
      <td>scikit-image development team</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>scikit-ffm</td>
      <td>scikit-fmm contributors</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>scipy</td>
      <td>scipy contributors</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Materials, data, and code availability

The code necessary to reproduce core aspects of data analysis, along with numerical data not included in source data files, are available at https://github.com/a9w/Fat2_polarizes_WAVE (Williams and Donoughe, 2022). Sequences of plasmids generated in this study are also available at https://github.com/a9w/Fat2_polarizes_WAVE (copy archived at swh:1:rev:0e1ee58588365bd3fba0099c6f002993a18ec279, Williams, 2022). We will share the flies or plasmids themselves upon request to the corresponding author. Image and movie data are available from https://doi.org/10.6084/m9.figshare.20759314.v1.

### Drosophila sources, care, and genetics

The sources and references of all stocks used in this study are listed in Key resources table and the genotypes of Drosophila used in each experiment and associated figure panels are listed in Table 1. Drosophila were raised at 25 °C and fed cornmeal molasses agar food. Females 0–3 days post-eclosion were aged on yeast with males prior to dissection. In most cases, they were aged for 2–3 days at 25 °C. Temperatures and yeasting times used for each experiment are reported in Table 2. In all RNAi experiments, traffic jam >Gal4 (tj >Gal4) (Hayashi et al., 2002) was used to drive RNAi expression in follicle cells and not in germ cells. Sra1-GFP and fat2 mosaic epithelia were generated using the Flp/FRT method (Golic and Lindquist, 1989; Golic, 1991), using FRT82B and FRT80B recombination sites, respectively. In both cases, tj >Gal4 was used to drive expression of UAS >Flp recombinase.

**Table 1.**
 Experimental genotypes.


<table>
  <thead>
    <tr>
      <th>Figure</th>
      <th>Panel</th>
      <th>Name</th>
      <th>Genotype</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>D</td>
      <td>F-actin +Ena + Abi</td>
      <td>w; ubi &gt;GFP-EnaBDSC:28798/ubi &gt;Abi-mCherryBDSC:58729</td>
    </tr>
    <tr>
      <td>1</td>
      <td>F</td>
      <td>Control</td>
      <td>w; tj &gt;Gal4DGRC:104055/+</td>
    </tr>
    <tr>
      <td>1</td>
      <td>F</td>
      <td>ena-RNAi</td>
      <td>w; tj &gt;Gal4DGRC:104055/UAS-ena-RNAiVDRC:43058</td>
    </tr>
    <tr>
      <td>1</td>
      <td>F</td>
      <td>abi-RNAi</td>
      <td>w; tj &gt;Gal4DGRC:104055/+; UAS-abi-RNAiNIG:9749R-3</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Top row</td>
      <td>Protrusion in 1 direction</td>
      <td>w1118</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Bottom row</td>
      <td>Protrusion in both directions</td>
      <td>w; fat2N103-2 FRT80B</td>
    </tr>
    <tr>
      <td>3</td>
      <td>A-C</td>
      <td>Control</td>
      <td>w1118</td>
    </tr>
    <tr>
      <td>3</td>
      <td>A-C</td>
      <td>fat2</td>
      <td>w; fat2N103-2 FRT80B</td>
    </tr>
    <tr>
      <td>3</td>
      <td>A-C</td>
      <td>CK-666</td>
      <td>w1118</td>
    </tr>
    <tr>
      <td>3</td>
      <td>D</td>
      <td>Control</td>
      <td>w1118</td>
    </tr>
    <tr>
      <td>3</td>
      <td>D</td>
      <td>fat2</td>
      <td>w; fat2N103-2 FRT80B</td>
    </tr>
    <tr>
      <td>4</td>
      <td>A,B</td>
      <td>fat2 mosaic</td>
      <td>w; tj &gt;Gal4DGRC:104055, UAS &gt;FlpBDSC:4539/+; fat2N103-2 FRT80B/ubi &gt;GFP NLS FRT80BBDSC1620</td>
    </tr>
    <tr>
      <td>5</td>
      <td>B</td>
      <td>Sra1-GFP mosaic</td>
      <td>w; tj &gt;Gal4DGRC:104055, UAS &gt;FlpBDSC:4539/+; FRT82B Sra1-GFP/FRT82B ubi &gt;mRFP-NLSBDSC:30555</td>
    </tr>
    <tr>
      <td>5</td>
      <td>C</td>
      <td>fat2 mosaic</td>
      <td>w; tj &gt;Gal4DGRC:104055, UAS &gt;FlpBDSC:4539/+; fat2N103-2 FRT80B/ubi &gt;GFP NLS FRT80BBDSC1620</td>
    </tr>
    <tr>
      <td>5</td>
      <td>D-F</td>
      <td>Sra1-GFP mosaic</td>
      <td>w; tj &gt;Gal4DGRC:104055, UAS &gt;FlpBDSC:4539/+; fat2N103-2 FRT80B Sra1-GFP/ubi &gt;mRFP NLS FRT80BDSC:30852</td>
    </tr>
    <tr>
      <td>6</td>
      <td>A</td>
      <td>Sra1-GFP mosaic +fat2</td>
      <td>w; tj &gt;Gal4DGRC:104055, UAS &gt;FlpBDSC:4539/+; fat2N103-2 FRT80B Sra1-GFP/fat2N103-2 FRT80B FRT82B</td>
    </tr>
    <tr>
      <td>6</td>
      <td>B,D</td>
      <td>Control</td>
      <td>w;; Sra1-GFP/+</td>
    </tr>
    <tr>
      <td>6</td>
      <td>B,D</td>
      <td>fat2</td>
      <td>w;; fat2N103-2 FRT80B Sra1-GFP/fat2N103-2 FRT80B</td>
    </tr>
    <tr>
      <td>6</td>
      <td>E,F</td>
      <td>fat2 mosaic +Sra1</td>
      <td>w; tj &gt;Gal4DGRC:104055, UAS &gt;FlpBDSC:4539/+; fat2N103-2 FRT80B Sra1-GFP/ubi &gt;mRFP NLS FRT80BDSC:30852</td>
    </tr>
    <tr>
      <td>7</td>
      <td>A,C</td>
      <td>Control</td>
      <td>w1118</td>
    </tr>
    <tr>
      <td>7</td>
      <td>A,C</td>
      <td>fat2</td>
      <td>w;; fat2N103-2 FRT80B</td>
    </tr>
    <tr>
      <td>7</td>
      <td>B</td>
      <td>Example of switch</td>
      <td>w;; fat2N103-2 FRT80B</td>
    </tr>
    <tr>
      <td>8</td>
      <td>A,E</td>
      <td>Fat2 +Abi</td>
      <td>w;; ubi &gt;Abi-mCherryBDSC:58729, Fat2-3xGFP FRT80B/Fat2-3xGFP FRT80B</td>
    </tr>
    <tr>
      <td>8</td>
      <td>A,E</td>
      <td>Fat2ΔICD + Abi</td>
      <td>w;; ubi &gt;Abi-mCherryBDSC:58729, Fat2ΔICD-3xGFP FRT80B/Fat2ΔICD-3xGFP FRT80B</td>
    </tr>
    <tr>
      <td>8</td>
      <td>B</td>
      <td>Fat2 +Abi</td>
      <td>w;; ubi &gt;Abi-mCherryBDSC:58729, Fat2-3xGFP FRT80B/Fat2-3xGFP FRT80B</td>
    </tr>
    <tr>
      <td>8</td>
      <td>C,D,F,G</td>
      <td>Fat2 +Abi + F-actin</td>
      <td>w;; ubi &gt;Abi-mCherryBDSC:58729, Fat2-3xGFP FRT80B/Fat2-3xGFP FRT80B</td>
    </tr>
    <tr>
      <td>3S1</td>
      <td>A</td>
      <td>Control</td>
      <td>w1118</td>
    </tr>
    <tr>
      <td>3S1</td>
      <td>A</td>
      <td>fat2</td>
      <td>w;; fat2N103-2 FRT80B</td>
    </tr>
    <tr>
      <td>3S1</td>
      <td>A</td>
      <td>CK-666</td>
      <td>w1118</td>
    </tr>
    <tr>
      <td>3S1</td>
      <td>B</td>
      <td>Control</td>
      <td>w1118</td>
    </tr>
    <tr>
      <td>3S1</td>
      <td>B</td>
      <td>fat2</td>
      <td>w;; fat2N103-2 FRT80B</td>
    </tr>
    <tr>
      <td>3S2</td>
      <td>A-C</td>
      <td>Control</td>
      <td>w; tj &gt;Gal4DGRC:104055/+</td>
    </tr>
    <tr>
      <td>3S2</td>
      <td>A-C</td>
      <td>fat2</td>
      <td>w; tj &gt;Gal4DGRC:104055/+; fat2N103-2 FRT80B</td>
    </tr>
    <tr>
      <td>3S2</td>
      <td>A-C</td>
      <td>abi-RNAi</td>
      <td>w; tj &gt;Gal4DGRC:104055/+UAS-abi-RNAiNIG:9749R-3/+</td>
    </tr>
    <tr>
      <td>3S2</td>
      <td>D</td>
      <td>Control</td>
      <td>w; tj &gt;Gal4DGRC:104055/UAS &gt;F-Tractin-tdTomatoBDSC:58989</td>
    </tr>
    <tr>
      <td>3S2</td>
      <td>D</td>
      <td>fat2</td>
      <td>w; tj &gt;Gal4DGRC:104055/UAS &gt;F-Tractin-tdTomatoBDSC:58989; fat2N103-2 FRT80B</td>
    </tr>
    <tr>
      <td>3S2</td>
      <td>D</td>
      <td>abi-RNAi</td>
      <td>w; tj &gt;Gal4DGRC:104055/UAS &gt;F-Tractin-tdTomatoBDSC:58989; UAS-abi-RNAiNIG:9749R-3/+</td>
    </tr>
    <tr>
      <td>3S2</td>
      <td>E,F</td>
      <td>Control</td>
      <td>w1118</td>
    </tr>
    <tr>
      <td>3S2</td>
      <td>E,F</td>
      <td>fat2</td>
      <td>w;; fat2N103-2 FRT80B</td>
    </tr>
    <tr>
      <td>5S1</td>
      <td>A</td>
      <td>Sra1-GFP</td>
      <td>w;; Sra1-GFP</td>
    </tr>
    <tr>
      <td>5S1</td>
      <td>A</td>
      <td>anti-SCAR</td>
      <td>w;; Sra1-GFP</td>
    </tr>
    <tr>
      <td>5S1</td>
      <td>A</td>
      <td>ubi &gt;Abi-mCherry</td>
      <td>w;; ubi &gt;Abi-mCherryBDSC:58729/+</td>
    </tr>
    <tr>
      <td>5S1</td>
      <td>B</td>
      <td>Control</td>
      <td>w; tj &gt;Gal4DGRC:104055/+</td>
    </tr>
    <tr>
      <td>5S1</td>
      <td>B</td>
      <td>abi-RNAi</td>
      <td>tj &gt;Gal4DGRC:104055/+; UAS-abi-RNAiNIG:9749R-3/+</td>
    </tr>
    <tr>
      <td>5S1</td>
      <td>C</td>
      <td>Control</td>
      <td>w1118</td>
    </tr>
    <tr>
      <td>5S1</td>
      <td>C</td>
      <td>Sra1-GFP x1</td>
      <td>w;; Sra1-GFP/+</td>
    </tr>
    <tr>
      <td>5S1</td>
      <td>C</td>
      <td>Sra1-GFP x2</td>
      <td>w;; Sra1-GFP</td>
    </tr>
    <tr>
      <td>5S1</td>
      <td>C</td>
      <td>sra1-RNAi</td>
      <td>w; tj &gt;Gal4DGRC:104055/+; UAS &gt;sra1-RNAiBDSC:38294/+</td>
    </tr>
    <tr>
      <td>5S1</td>
      <td>D</td>
      <td>Control</td>
      <td>w1118</td>
    </tr>
    <tr>
      <td>5S1</td>
      <td>D</td>
      <td>Sra1-GFP x1</td>
      <td>w;; Sra1-GFP/+</td>
    </tr>
    <tr>
      <td>5S1</td>
      <td>D</td>
      <td>Sra1-GFP x2</td>
      <td>w;; Sra1-GFP</td>
    </tr>
    <tr>
      <td>5S2</td>
      <td>A, C-E</td>
      <td>Control</td>
      <td>w;; Sra1-GFP/+</td>
    </tr>
    <tr>
      <td>5S2</td>
      <td>A, C-E</td>
      <td>fat2</td>
      <td>w;; fat2N103-2 FRT80B Sra1-GFP/fat2N103-2 FRT80B</td>
    </tr>
    <tr>
      <td>6S1</td>
      <td></td>
      <td>Control</td>
      <td>w;; Sra1-GFP/+</td>
    </tr>
    <tr>
      <td>6S1</td>
      <td></td>
      <td>fat2</td>
      <td>w;; fat2N103-2 FRT80B Sra1-GFP/fat2N103-2 FRT80B</td>
    </tr>
    <tr>
      <td>8S1</td>
      <td>A,B</td>
      <td>Control Fat2 +Abi</td>
      <td>w;; ubi &gt;Abi-mCherryBDSC:58729, Fat2-3xGFP FRT80B/Fat2-3xGFP FRT80B</td>
    </tr>
    <tr>
      <td>8S1</td>
      <td>A,B</td>
      <td>Fat2ΔICD + Abi</td>
      <td>w;; ubi &gt;Abi-mCherryBDSC:58729, Fat2ΔICD-3xGFP FRT80B/Fat2ΔICD-3xGFP FRT80B</td>
    </tr>
    <tr>
      <td>8S1</td>
      <td>A,B</td>
      <td>ena-RNAi, Fat2 +Abi</td>
      <td>w; tj &gt;Gal4DGRC:104055/UAS &gt;ena RNAiVDRC:43058; ubi &gt;Abi-mCherryBDSC:58729, Fat2-3xGFP FRT80B/Fat2-3xGFP FRT80B</td>
    </tr>
    <tr>
      <td>8S1</td>
      <td>A,B</td>
      <td>Control Fat2 +Abi</td>
      <td>w; larbola 1BDSC:91654/lar13.2 BDSC:8774 FRT40A; ubi &gt;Abi-mCherryBDSC:58729, Fat2-3xGFP FRT80B/Fat2-3xGFP FRT80B</td>
    </tr>
    <tr>
      <td>8S1</td>
      <td>C</td>
      <td>Fat2 +Abi</td>
      <td>w;; ubi &gt;Abi-mCherryBDSC:58729, Fat2-3xGFP FRT80B/Fat2-3xGFP FRT80B</td>
    </tr>
    <tr>
      <td>8S1</td>
      <td>D-F</td>
      <td>Ena +Abi + F-actin</td>
      <td>w; ubi &gt;GFP-EnaBDSC:28798/ubi &gt;Abi-mCherryBDSC:58729</td>
    </tr>
    <tr>
      <td>8S1</td>
      <td>G</td>
      <td>Control</td>
      <td>w;; ubi &gt;Abi-mCherryBDSC:58729, Fat2-3xGFP FRT80B/Fat2-3xGFP FRT80B</td>
    </tr>
    <tr>
      <td>8S1</td>
      <td>G</td>
      <td>lar</td>
      <td>w; larbola 1BDSC:91654/lar13.2 BDSC8774 FRT40A; ubi &gt;Abi-mCherryBDSC:58729, Fat2-3xGFP FRT80B/Fat2-3xGFP FRT80B</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Yeasting conditions.


<table>
  <thead>
    <tr>
      <th>Figure</th>
      <th>Panel</th>
      <th>Days on yeast</th>
      <th>Temp. (°C)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>D</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>1</td>
      <td>F</td>
      <td>3</td>
      <td>29</td>
    </tr>
    <tr>
      <td>2</td>
      <td></td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>3</td>
      <td>A-D</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>4</td>
      <td>A,B</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>5</td>
      <td>B</td>
      <td>7</td>
      <td>25</td>
    </tr>
    <tr>
      <td>5</td>
      <td>C</td>
      <td>3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>5</td>
      <td>D-F</td>
      <td>3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>6</td>
      <td>A</td>
      <td>5</td>
      <td>25</td>
    </tr>
    <tr>
      <td>6</td>
      <td>B,D</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>6</td>
      <td>E</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>7</td>
      <td>A-C</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>8</td>
      <td>A,E</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>8</td>
      <td>B</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>8</td>
      <td>C,D,F,G</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>S1</td>
      <td>A-C</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>S2</td>
      <td>A-C,E,F</td>
      <td>2–3</td>
      <td>29</td>
    </tr>
    <tr>
      <td>S2</td>
      <td>D</td>
      <td>2–3</td>
      <td>29</td>
    </tr>
    <tr>
      <td>S3</td>
      <td>A</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>S3</td>
      <td>B</td>
      <td>3</td>
      <td>29</td>
    </tr>
    <tr>
      <td>S3</td>
      <td>C</td>
      <td>3</td>
      <td>29</td>
    </tr>
    <tr>
      <td>S3</td>
      <td>D</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>S4</td>
      <td>A-E</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>S5</td>
      <td></td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>S6</td>
      <td>A,B,F</td>
      <td>3</td>
      <td>29</td>
    </tr>
    <tr>
      <td>S6</td>
      <td>C</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
    <tr>
      <td>S6</td>
      <td>D-F</td>
      <td>2–3</td>
      <td>25</td>
    </tr>
  </tbody>
</table>

### Generation of Sra1-GFP

Endogenous Sra1 was tagged C-terminally with enhanced GFP (GFP) following the general approaches described by Gratz et al., 2013 and Gratz et al., 2014 . The guide RNA target sequence 5’-GCTTAAATGCATCCCTTTCCGGG-3’ was chosen with flyCRISPR Target Finder (Gratz et al., 2014). The underlined sequence was cloned into the pU6-BbsI-chiRNA plasmid, and the bold sequence is the adjacent PAM motif. For homologous recombination, homology arms approximately 2 kb long flanking the insertion target site were amplified from genomic DNA from the y1 M{nos-Cas9.P}ZH-2A w* (nanos >Cas9) (Port et al., 2014) background. GFP was amplified from the pTWG plasmid. A linker with sequence encoding the amino acids ‘GSGGSGGS’ was added to the N-terminal side of GFP. Homology arms, linker, and GFP were inserted into donor plasmid pDsRed-attP, which contains 3xP3 >DsRed flanked by loxP sites for insertion screening and subsequent removal. The linker-GFP insertion was made immediately before the Sra1 stop codon. Guide and homologous recombination plasmids were injected by Genetivision Inc into the nanos >Cas9 background. F1 males were screened for 3xP3 >DsRed and then 3xP3 >DsRed was excised by crossing to Cre-expressing flies (MKRS hsFLP/TM6b Cre).

### Egg chamber dissection

All data come from stage 6–7 egg chambers. To obtain these, ovaries were dissected into live imaging media (Schneider’s Drosophila medium with 15% fetal bovine serum and 200 μg/mL insulin) in a spot plate using 1 set of Dumont #55 forceps and 1 set of Dumont #5 forceps. Ovarioles were removed from the ovary and from ovariole muscle sheathes with forceps. For live imaging, egg chambers older than the egg chamber to be imaged were removed from the ovariole strands by cutting through the stalk with a 27-gauge hypodermic needle. For fixed imaging, egg chambers older than stage 9 were removed prior to fixation. Removal of older egg chambers allows more compression of the imaged egg chamber between the slide and coverslip so that the basal surface of a field of cells can be imaged in a single plane. For a more detailed description and movies of dissection, see Cetera et al., 2016 .

### Live imaging sample preparation

Following dissection, ovarioles were transferred to a fresh well of live imaging media. For membrane staining, CellMask Orange or Deep Red plasma membrane stain (Thermo Fisher Scientific, Waltham, MA, 1:500) was added and ovarioles incubated for 15 min, followed by a wash in live imaging media to remove excess stain before mounting. Ovarioles were then transferred to a glass slide with 20 μL of live imaging media. For CK-666 treatment, following plasma membrane staining, ovarioles were transferred to live imaging media with 750 μM CK-666 (Millipore Sigma, St. Louis, MO) and then mounted in the same media. Glass beads with diameter 51 μm were added to support the 22x22 mm #1.5 coverslip and limit egg chamber compression. Coverslip edges were sealed with melted petroleum jelly to prevent evaporation while imaging. Samples were checked for damage using the membrane stain or other fluorescent markers as indicators, and excluded if damage was observed. Slides were used for no more than 1 hr.

### Immunostaining and F-actin staining

Following dissection, ovarioles were fixed in 4% EM-grade formaldehyde in PBT (phosphate buffered saline +0.1% Triton X-100) and then washed 3x5 min in PBT at room temperature. Egg chambers were incubated with primary antibodies in PBT overnight at 4° C (anti-Scar, 1:200) or for 2 hr at room temperature (anti-Discs Large, 1:20) while rocking. Ovarioles were then washed 3x5 min in PBT and incubated in secondary antibody diluted 1:200 in PBT for 2 hr at room temperature while rocking. F-actin staining was performed using either TRITC phalloidin (Millipore Sigma, 1:250) or Alexa Fluor 647 phalloidin (Thermo Fisher Scientific, 1:50). If TRITC phalloidin was the only stain or antibody used, it was added directly to the fixation media for 15 min of staining concurrent with fixation. Otherwise, TRITC phalloidin was added for 15–30 min at room temperature as the final staining step. Alexa Fluor 647 phalloidin staining was performed for 2 hr at room temperature while the sample was rocking, concurrent with secondary antibody staining where applicable. Ovarioles were then washed 3x5 min in PBT and mounted in 40 μL SlowFade Diamond antifade on a slide using a 22x50 mm #1.5 coverslip, sealed with nail polish, and stored at 4° C until imaged.

### Microscopy

#### Laser scanning confocal microscopy

Laser scanning confocal microscopy was used for all fixed imaging and for live imaging of membrane-dyed egg chambers. Imaging was performed with a Zeiss LSM 800 upright laser scanning confocal with a 40 x/1.3 NA EC Plan-NEOFLUAR oil immersion objective or a 63 x/1.4 NA Plan-APOCHROMAT oil immersion objective, diode lasers (405, 488, 561, and 640 nm), and GaAsP detectors. The system was controlled with Zen 2.3 Blue acquisition software (Zeiss). Imaging was performed at room temperature. All images show the basal surface of stage 6–7 egg chambers except for Figure 5—figure supplement 1A, bottom row, which shows follicle cells in cross-section. Cross-section images were used for egg chamber staging throughout. Laser scanning confocal microscopy was used to acquire the data in Figure 1D and F; Figure 2; Figure 3; Figure 3—figure supplement 1A-C; Figure 3—figure supplement 2; Figure 3—video 1; Figure 3—video 3; Figure 4; Figure 4—video 1; Figure 5B–F; Figure 5—figure supplement 1; Figure 5—figure supplement 2; Figure 6A; Figure 6—figure supplement 1; Figure 6—video 1; Figure 7A–C; Figure 7—video 1; Figure 8A and C–G; Figure 8—figure supplement 1.

#### TIRF microscopy

Near-TIRF microscopy was used to visualize Fat2-GFP, Sra1-GFP, Abi-mCherry, and F-Tractin-tdTomato (Spracklen et al., 2014) dynamics at the basal surface. Near-TIRF imaging was performed with a Nikon ECLIPSE-Ti inverted microscope with Ti-ND6-PFS Perfect Focus Unit, solid-state 50 mW 481 and 561 nm Sapphire lasers (Coherent technology), motorized TIRF illuminator, laser merge module (Spectral Applied Research), Nikon CFI 100 x Apo 1.45 NA oil immersion TIRF objective with 1.5 x intermediate magnification, and Andor iXon3 897 electron-multiplying charged-coupled device (EM-CCD) camera. Image acquisition was controlled using MetaMorph software. For two color imaging, frames were collected for each color consecutively with the TIRF illumination angle adjusted in between. Imaging was performed at room temperature. For display, movies were corrected for bleaching using the histogram matching method in Fiji (ImageJ) (Schindelin et al., 2012; Schindelin et al., 2015). TIRF microscopy was used to acquire the data in Figure 3—figure supplement 2; Figure 3—video 2; Figure 6B and D–F; Figure 6—video 2; Figure 6—video 3; Figure 8B; Figure 8—figure supplement 1; Figure 8—video 1; Figure 8—video 2.

### Cell and protrusion segmentation from timelapses of cell membrane

Protrusions from timelapse datasets of the follicle cell basal surface stained with CellMask Orange (see Live imaging sample preparation) were segmented with the Python scikit-image and scipy libraries (Figure 2; van der Walt et al., 2014; Virtanen et al., 2020). First, each cell was segmented and tracked, with manual corrections to cell-cell interface placements made using napari (napari contributors, 2019 ). Next, a watershed-based approach was used to segment the regions of high fluorescence intensity at the interface of each pair of neighboring cells. This segmented shape encompasses the cell-cell interface and any associated protrusions from either neighboring cell. Last, to assign protrusions to the cell from which they originated, the segmented region was divided in two by the shortest path between its bounding vertices that lay entirely within the region. This approximates the position of the interface between the cells, and in subsequent steps we will call this line ‘the interface’. Each of the two resulting protrusion shapes was assigned as originating from the cell on the opposite side of the interface, because protrusions extend from one cell and overlap the other. Using this approach, all of the protrusive structures that emerge from one cell, and that overlap a single neighboring cell, are grouped together as a single segmented region for subsequent analysis.

### Measurement of membrane protrusivity, protrusion length, and protrusion orientation

After cell edges and associated protrusions were segmented, they were categorized as either protrusive or non-protrusive and their lengths and orientations using Python scikit-fmm, scikit-image, and scipy libraries. We use the term ‘membrane extensions’ to refer to the cell edge shapes before the protrusive ones have been identified. To measure the length of a membrane extension, we used two different metrics, each of which provides a single length value per cell edge. In one, we calculated the ‘average length’ of a membrane extension as the membrane extension’s area divided by the length of the interface it extended across. As an alternate length measurement, we calculated its ‘longest length’. To do so, we first found its ‘tip’, defined as the pixel within the segmented region farthest from any point along the interface. We then found its ‘base’, the pixel along the interface that was closest to the tip. We defined membrane extension longest length as the length of the shortest path between base and tip that lay entirely within the membrane extension. To categorize membrane extensions as protrusive or non-protrusive throughout the study, we used the ‘average length’ metric. We measured the average length distribution in CK-666-treated epithelia, which are nearly non-protrusive and so provided a measure of the width of the cell-cell interface alone. For all conditions, we categorized a membrane extension as protrusive if its average length was greater than the 98th percentile of length of CK-666-treated epithelia. We then defined the protrusivity of an entire epithelium as the ratio of protrusive to total cell edges in the field of view. We also report two alternate measurements of the protrusivity of an epithelium. In one, We calculate epithelial protrusivity as above, but substitute the longest length as our length measurement (Figure 3—figure supplement 1A). In a second, cutoff-independent epithelial protrusivity measurement, we report the epithelium-mean average membrane extension length (Figure 3—figure supplement 1B). Swarm plots of each of these analyses were generated using GraphPad Prism 9 (GraphPad, San Diego, CA), as were all other swarm plots.

For analysis of protrusion orientation, we included only the membrane extensions categorized as protrusive according to the ‘average length’ metric. We defined a protrusion’s orientation as the orientation of the vector from its base to its tip. Polar histograms, generated in Python with matplotlib (Hunter, 2007), show the distribution of protrusion orientations. In these plots, bar area is proportional to the number of protrusions in the corresponding bin. We note that cells of migratory epithelia often have rearward-pointing retraction fibers as well as protrusions, and our protrusion segmentation method does not distinguish these two types of membrane extensions. For this reason, the degree of protrusion polarity we measure for the migratory control epithelia is likely an underestimate.

### Quantification of F-actin and Sra1-GFP cell-cell interface and non-interface basal surface fluorescence

Cells and cell-cell interfaces were segmented as described above. Cells and interfaces in contact with the tissue border or image border were excluded from analysis. For interface fluorescence intensity, interfaces were dilated by 5 pixels, and mean fluorescence intensity calculated from within this region. Non-interface basal surface fluorescence intensity was calculated as the mean of the remaining (non-interface) tissue surface. For F-actin cell-cell interface enrichment measurements, the overall brightness of the phalloidin staining varied between epithelia independent of genotype. To control for this variation we subtracted the mean intensity of the epithelium’s non-interface basal surface from its mean interface intensity measurement. This value, the degree of F-actin interface enrichment, was used as a proxy for F-actin protrusivity.

### Quantification of F-actin and Sra1-GFP planar polarity

As a simple planar polarity measurement, we quantified mean F-actin (phalloidin) or Sra1-GFP fluorescence intensity along each cell-cell interface as a function of the interface’s orientation with respect to the anterior-posterior axis. To do this, cells and cell-cell interfaces were segmented as described above. For interface angle measurements, the angular distance between the line defined by the interface-bounding vertices and the anterior-posterior (horizontal) axis was calculated. For interface fluorescence intensity measurements, interface regions were identified as segmented interfaces dilated by 5 pixels. Vertices, dilated by 10 pixels, were excluded from interface regions. Mean fluorescence intensity was calculated within each interface region, and background (the mean non-interface basal surface fluorescence intensity of all cells in the image) was subtracted. Polar bar plots, generated in Python with matplotlib, show the mean interface intensity as a function of interface angle. In these plots, bar area is proportional to intensity, and Control and fat2 datasets are rescaled separately so that each have a mean value of one. As a summary statistic for the degree of planar polarization of F-actin or Sra1-GFP in each egg chamber, we found the average fluorescence intensities of interfaces with angles between 0° and 10° and between 80° and 90°. These correspond with leading-trailing and side interfaces, respectively, in migratory epithelia. The leading-trailing interface enrichment is the ratio of these numbers.

### Autonomy analysis in mosaic epithelia

Egg chambers were stained with Alexa Fluor 647 phalloidin to mark protrusions, which indicate migration direction, and to determine whether egg chambers were planar-polarized. We analyzed only S6-7 egg chambers with mixtures of control and fat2 cells that had global stress fiber alignment orthogonal to the anterior-posterior axis, indicating global planar polarity. Since migration is required to maintain planar polarity (Cetera et al., 2014), this also indicates that the epithelium was migratory. We then measured the Sra1-GFP fluorescence intensity at leading-trailing interfaces and medial basal surfaces to determine whether changes in Sra1-GFP levels coincided with the genotype of the Sra1-containing cell, or the genotype of the cell ahead. To select leading-trailing interface regions to measure, we drew 10 pixel-wide segmented lines along leading edges of individual cells, assigning them to a condition based on their own genotype and the genotype of the cell just ahead. If a cell had both control and fat2 cells ahead of it, we measured those leading edge segments separately, assigning each to the applicable condition. Lines were drawn along all visible, in-focus fat2-control and control-fat2 boundaries and a similar number of control-control and fat2-fat2 boundaries. Epithelia were excluded if two or more interfaces of each of the four genotype combinations were not present. From these regions, we measured mean Sra1-GFP fluorescence intensity for each cell, and then took the mean of these as the fluorescence intensity per egg chamber. For a diagram of this method, see Barlan et al., 2017, which we have modified here to allow measurement of individual cells. To quantify medial basal surface Sra1-GFP fluorescence intensity, we used the same approach with the following exceptions: we measured polygonal regions of the basal surface of individual cells away from cell-cell interfaces, and cells were excluded if their leading edge contacted both control and fat2 cells.

### Quantification of migration rate

Egg chambers were dissected, dyed with CellMask Orange, and mounted for live imaging as described above. Several ovarioles were mounted on each slide, with each ovariole terminating in a S6-7 egg chamber. Timelapse imaging was performed for 30 min with frames acquired every 30 s. Multi-point acquisition was used to obtain movies of up to 5 egg chambers simultaneously. To generate a kymograph, a line was drawn along the axis of migration at the center of the anterior-posterior egg chamber axis in Fiji. In these kymographs, cell-cell interfaces are visible as lines, and their slope gives a measurement of cell migration rate. Egg chamber migration rates were calculated from the average of four-cell interface slopes from each kymograph. Egg chambers that clearly slowed down over the course of the timelapse, visible as curvature in the interface lines in the kymographs, were excluded. For an illustration of this method, see Barlan et al., 2017.

### Cell perimeter kymograph generation and interpretation

To visualize the distribution of Sra1-GFP along cell-cell interfaces over time, we generated kymographs of cell perimeters from timelapses of Sra1-GFP-expressing epithelia obtained using near-TIRF microscopy. Perimeters were drawn manually in Fiji in each frame with the pencil tool, and then these perimeters were used to generate kymographs in Python. Perimeters were thinned to 1 pixel and then perimeter pixels were sequenced with Python scikit-image and scipy libraries. Kymographs were generated with matplotlib. Kymograph rows were constructed by linearizing the perimeters from each frame, starting with the pixel directly above the cell centroid (the center of the trailing edge in control cells) and continuing counter-clockwise. Each row shows the fluorescence intensity of the perimeter pixels in sequence. Cell perimeter lengths varied between frames, so kymograph row lengths varied and were aligned to their center position.

At the spatial and temporal resolution of the timelapses and corresponding kymographs, we cannot evaluate differences in the dynamics the puncta-scale WAVE complex accumulations highlighted in Figure 8. Instead, we focus on the ‘region’-scale distribution of Sra1-GFP, and the stability of that distribution over time. The regions we refer to here are approximately the length of a cell-cell interface, with variation. Because the kymographs are generated from epithelia in which all cells express Sra1-GFP, we need additional information to identify the cell to which a region of Sra1-GFP enrichment belongs. We infer that Sra1-GFP is predominantly at leading edges in polarized, migratory epithelia based on the Sra1-GFP distribution in epithelia with mosaic Sra1-GFP expression (Figure 5B). Based on consistent correlation between Sra1-GFP enrichment and the presence of protrusions (Figure 6A, Figure 6—figure supplement 1), and its known role building lamellipodia as part of the WAVE complex (Miki et al., 1998; Miki et al., 2000; Steffen et al., 2004), we also infer that regions of Sra1-GFP enrichment belong to the cell that is protruding outward regardless of genotype. Our interpretations of Sra1-GFP enrichment patterns in movies and corresponding kymographs are made with these assumptions.

### Quantification of the stability of interface protrusion polarity

As a measurement of the stability of protrusive regions over time, we quantified the frequency with which the direction of protrusion switched across a cell-cell interface. These switching events occur when one cell and then its neighbor protrude across their shared interface, and they serve as a score-able indicator of a change in the polarity state of the cells that bound the interface. To determine the switching frequency, we counted the number of switching events that occurred in each timelapse, and then determined an interface protrusion polarity switching rate by dividing the number of switches by the number of interfaces identified with cell and protrusion segmentation. We chose a hand-counting method because the protrusion segmentation error rate from the inclusion of retraction fibers and other sources (see Measurement of membrane protrusivity, protrusion length, and protrusion orientation) was sufficiently high that automated measurement of dynamic features of protrusions was unreliable.

### Colocalization of proteins along the leading-trailing interface

Data used for colocalization analysis were collected with 63 x/1.4 NA Plan-APOCHROMAT oil immersion objective to minimize chromatic aberration. Linescans were generated in Fiji by manually drawing a 10 pixel-wide segmented line along rows of leading-trailing interfaces at the follicle cell basal surface. At least 20 leading-trailing interfaces were included per egg chamber. For the Fat2ΔICD condition, in which the distribution of Fat2 expands beyond leading-trailing interfaces, we measured colocalization either along randomly oriented interfaces (Figure 8E) or leading-trailing interfaces (Figure 8—figure supplement 1) and obtained very similar results. Fluorescence intensities along the linescans were obtained with the PlotProfile function, which averages pixel intensities along the width of the line and reports a list of averaged values along the line’s length. Spearman’s correlation coefficients were calculated for each egg chamber in Python with the scipy.stats module. Failure to exactly follow leading-trailing interfaces and cusps in the segmented lines will artificially inflate the measured correlation, so we used correlation between E-cadherin-GFP (Huang et al., 2009) and Abi-mCherry as a negative control that is also subject to this inflation. Abi-mCherry and E-cadherin-GFP are slightly displaced from each other (anticorrelated) along the length of protrusions (the width of the linescans), but averaging across the line width collapses this displacement, resulting in measured intensity signals that are roughly uncorrelated. Spearman’s correlation coefficients ± standard deviation are reported in the text. Linescans of leading-trailing interfaces were plotted using the fluorescence intensities from along the leading-trailing interfaces of two cells. Intensities from each fluorophore were rescaled between 0 and 1 and plotted with matplotlib in Python.

### Protrusion profile generation

Viewing only the F-actin channel in Fiji, we drew 1 pixel-wide lines down the length of F-actin bundles at the leading edge. Fluorescence intensities along these lines were obtained for all fluorophores with the Fiji PlotProfile function. In Python, these traces were aligned to the pixel with highest Fat2-3xGFP or Ena-GFP intensity (Figure 8G, Figure 8—figure supplement 1). To calculate standard deviation, all traces were first rescaled individually so that their values ranged between 0 and 1. To plot ‘protrusion profiles’, the mean fluorescence was determined for each fluorophore at each pixel position, and then average values were rescaled between 0 and 1. Plots of protrusion profiles were generated with matplotlib.

### Movie generation

Migration motion was subtracted from several timelapse movies of migratory cells or epithelia for ease of visualization. Motion subtraction was performed using the Fiji MultiStackReg plugin ‘translation’ transformation [Thévenaz et al., 1998; control condition in Figure 3—video 1; Figure 6—video 1; Figure 6—video 2 (part 1)] or by aligning to the centroid of a tracked cell in each frame using the scikit-image library [Figure 6—video 2 (part 2); Figure 7—video 1]. Labels were added to movies in Fiji and then exported as uncompressed .avi files. These were encoded as 1080 p30 .mp4 files with H.264 (x264) video encoder using HandBrake 1.4.

### Reproducibility and statistical analysis

Visibly damaged egg chambers were excluded from all analyses. At least two biological replicates were performed for each experiment, and results confirmed to be qualitatively consistent. Each biological replicate included egg chambers pooled from multiple flies. Experiments and analysis were not randomized or performed blinded. Sample sizes were not predetermined using a statistical method. The number of biological replicates (n), statistical tests performed, and their significance can be found in figures or figure legends. Based on visual inspection, all data on which statistical tests were performed followed an approximately normal distribution, so tests assuming normalcy were used. Alpha was set to 0.05 for all statistical tests. Paired statistical tests were used for comparisons of cells of different genetic conditions within mosaic epithelia. All t-tests were two-tailed. One-sample t-tests were used when comparing a distribution of ratios to a null expectation of one. A one-way ANOVA was used when more than two conditions were compared. Welch’s corrections were performed for the t-tests or ANOVAs of data plotted in Figure 3C, Figure 7C, Figure 3—figure supplement 1A,B, and Figure 3—figure supplement 2, for which the variance did not appear consistent between conditions. For post-hoc comparison tests, all pairs of conditions present in the corresponding plot were compared using post-hoc Tukey’s multiple comparisons test with the following exceptions: the data plotted in Figure 8E and Figure 8—figure supplement 1 were analyzed together, and all conditions were compared to Fat2-Abi and E-cadherin-Abi only, and in Figure 5—figure supplement 2 only data from the same region (total, interface, or non-interface) was compared. For these, Šidák’s multiple comparisons tests were used. For Welch’s ANOVA, Dunnet’s T3 multiple comparisons tests were used. p-values reported for all post-hoc tests were adjusted for multiple comparisons. All statistical tests except for the calculation of Spearman’s correlation coefficients were performed in GraphPad Prism 9.
