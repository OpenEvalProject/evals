# Supracellular organization confers directionality and mechanical potency to migrating pairs of cardiopharyngeal progenitor cells

## Authors

- Yelena Y Bernadskaya<sup>1</sup> ([ORCID: 0000-0001-6147-5825](https://orcid.org/0000-0001-6147-5825)) †
- Haicen Yue<sup>2</sup>
- Calina Copos<sup>3</sup>
- Lionel Christiaen<sup>1</sup> ([ORCID: 0000-0001-5930-5667](https://orcid.org/0000-0001-5930-5667)) †
- Alex Mogilner<sup>2</sup> ([ORCID: 0000-0002-9310-3812](https://orcid.org/0000-0002-9310-3812)) †

### Affiliations

1. Center for Developmental Genetics, Department of Biology, New York University New York United States
2. Courant Institute of Mathematical Sciences and Department of Biology, New York University New York United States
3. Mathematics and Computational Medicine, University of North Carolina at Chapel Hill Chapel Hill United States
4. Sars International Centre for Marine Molecular Biology Bergen Norway
5. Department of Heart Disease, Haukeland University Hospital Bergen Norway

† Corresponding author

## Abstract

Physiological and pathological morphogenetic events involve a wide array of collective movements, suggesting that multicellular arrangements confer biochemical and biomechanical properties contributing to tissue-scale organization. The Ciona cardiopharyngeal progenitors provide the simplest model of collective cell migration, with cohesive bilateral cell pairs polarized along the leader-trailer migration path while moving between the ventral epidermis and trunk endoderm. We use the Cellular Potts Model to computationally probe the distributions of forces consistent with shapes and collective polarity of migrating cell pairs. Combining computational modeling, confocal microscopy, and molecular perturbations, we identify cardiopharyngeal progenitors as the simplest cell collective maintaining supracellular polarity with differential distributions of protrusive forces, cell-matrix adhesion, and myosin-based retraction forces along the leader-trailer axis. 4D simulations and experimental observations suggest that cell-cell communication helps establish a hierarchy to align collective polarity with the direction of migration, as observed with three or more cells in silico and in vivo. Our approach reveals emerging properties of the migrating collective: cell pairs are more persistent, migrating longer distances, and presumably with higher accuracy. Simulations suggest that cell pairs can overcome mechanical resistance of the trunk endoderm more effectively when they are polarized collectively. We propose that polarized supracellular organization of cardiopharyngeal progenitors confers emergent physical properties that determine mechanical interactions with their environment during morphogenesis.

## Introduction

Cell migration is a fundamental cellular behavior involved in developmental and physiological processes including germline, craniofacial, and cardiac development, angiogenesis and wound healing, and pathogenesis such as cancer metastasis (Rørth, 2009; Scarpa and Mayor, 2016). In complex dynamic multicellular environments, cells integrate biochemical and mechanical cues to guide their migration. Some migration specialists, like neutrophils, navigate complex environments as single cells (Wang et al., 2020). Conversely, many developmental, homeostatic, and pathogenic morphogenetic events involve the coordinated movements of cellular collectives, as observed during neural crest migration in chick, lateral line migration in zebrafish, and border cell migration in the Drosophila ovary (Piacentino et al., 2020; Olson and Nechiporuk, 2018; Peercy and Starz-Gaiano, 2020). The properties that emerge from collective organization are thought to facilitate biochemical and mechanical integration and foster efficient and accurate tissue morphogenesis in a multicellular context (Malet-Engra et al., 2015; Theveneau et al., 2010; Shellard et al., 2018; van Helvert et al., 2018; Friedl and Mayor, 2017).

Migratory collectives typically exist on a continuum with varying degrees of cell-cell contact and polarity (Capuana et al., 2020; Mayor and Etienne-Manneville, 2016). In minimally differentiated groups, individual cells move as autonomous units, while adjusting directionality and speed relative to their neighbors (Szabó et al., 2006). At the other extreme of collective organization, cells are integrated into supracellular arrangements, with marked front-to-back specialization and continuity of cytoskeletal structures between neighboring cells, ensuring mechanical coupling (reviewed in Shellard and Mayor, 2019). Such collective polarity implies communication between cells to coordinate subcellular processes.

Numerous studies uncovered mechanisms underlying collective organization, such as contact inhibition of locomotion (CIL) (Mayor and Etienne-Manneville, 2016; Ebnet et al., 2018) and leader-mediated inhibition of protrusive activity in follower cells (Cai et al., 2014; Serwane et al., 2017). Ultimately, both biochemical and mechanical properties of migratory collectives contribute to successful tissue morphogenesis. While many biochemical aspects of cell migration have been investigated, measurement of in vivo mechanical forces involved in morphogenetic cell migration has been a challenge (Campàs et al., 2014). To understand the mechanics of collective locomotion, in vitro techniques such as traction force microscopy were developed and used to correlate forces with movement and cytoskeletal dynamics (Danuser and Waterman-Storer, 2003). In more complex embryo settings, the distribution of mechanical forces can be inferred from imaging datasets, combined with available direct measurements of membrane tension (Campàs et al., 2014; Veldhuis et al., 2017; Godard et al., 2020). As a complement to biophysical measurements, computational modeling offers a powerful option to reverse-engineer forces from observed cell shape and enable in silico predictions that can be compared to experimental observations (Godard et al., 2020; Sherrard et al., 2010). There is a rich inventory of modeling approaches, from simple conceptual models of cells as point-like persistent walkers interacting with distance-dependent forces (Méhes and Vicsek, 2014), to detailed continuous or discrete models of interacting cells as distributed mechanical objects with complex rheology and free boundaries (Winkler et al., 2019; Buttenschön and Edelstein-Keshet, 2020; Alert and Trepat, 2020).

We use the cardiogenic lineage of the tunicate Ciona, a simple chordate among the closest relatives of vertebrates (Dehal and Boore, 2006; Putnam et al., 2008), to develop and test a computational model of collective polarity and directed cell migration. During Ciona embryonic development, the cardiopharyngeal precursors are born as two superficially equivalent cells arising from the division of bilateral founders. The resulting cells migrate from their origin in the tail to the ventral trunk, hence their denomination as trunk ventral cells (aka TVCs) (Christiaen et al., 2008; Gline et al., 2015; Bernadskaya et al., 2019). The TVCs migrate as pairs, offering the simplest possible model of polarized collective cell migration. The anterior leader cell extends dynamic lamellipodia-like protrusions, while the posterior trailer terminates in a tapered retractive edge (Christiaen et al., 2008). Under unperturbed conditions, the migrating TVCs remain committed to their leader/trailer positions (Gline et al., 2015; Bernadskaya et al., 2019). TVCs contact multiple tissues during migration, including the posterior mesenchyme, the trunk endoderm, and the ventral epidermis, which serves as substrate (Gline et al., 2015). TVCs maintain polarized organization along the anterior posterior axis and spheroid shapes as they invade the extracellular space between the epidermis and the endoderm. Ciona TVCs thus represent a simple and intriguing model to study the mechanics and polarity of cells migrating in an embryonic context (Figure 1A).

![Figure 1.](https://cdn.elifesciences.org/articles/70977/elife-70977-fig1-v3.jpg)

**Figure 1.:** (A) Diagram of Ciona robusta embryo at the late tailbud stage (embryonic stage 23). Migrating TVCs are shown in green, their non-migratory sister cells, anterior tail muscles (ATMs), in blue. The endoderm is shown in pink. A micrograph of a migratory pair of TVCs is shown with the leader to the right and the trailer to the left. Cell membranes are marked with Mesp>hCD4::GFP. To the right is a surface-rendered image of the migratory TVC pair with leader in blue and trailer in red. Schematic diagram showing the mechanical parameters related to cells’ movement and morphology, reflecting volume conservation (yellow), surface tension (green), cell-cell adhesion (blue), cell-epidermis adhesion (black), and active protrusion/retraction forces (red). The cell pair moves to the right, with the green cell as the leader cell and the gray cell as the trailer cell. Overlying endoderm cells are shown in pink; the underlying epidermis in gray. The shape change (shaded area) is accepted or rejected depending on the energy change $ΔH$ related to it. The equation above shows the effective mechanical energy, H, of the cell pair. The meaning of the parameters is explained in the text. (B) Comparison of cell shape in the experiment and in simulation for single migrating cell and migrating cell pair. Scatter plot shows ratio of leader to trailer sphericity derived from in vivo measurements and in simulations. In vivo data were pooled from two biological replicates. No statistical difference was identified by Student’s t-test between the in vivo and simulated data. Micrographs show dorsal and lateral view of 3D images of TVC. TVC membranes are marked with Mesp>hCD4::GFP, and epidermal cell membranes are marked with Mesp>hCD4::mCherry. (C) Aspect ratios of migrating cell pairs compared to aspect ratios of single migrating cells calculated in Fiji and in simulations. Red lines show length of bounding box width and heights normalized to the width. Scatter plots show mean with standard error of in vivo and simulated data. Statistical analysis was performed using Student’s t-test. No significant difference between conditions in vivo and in simulation. Data are pooled from two biological replicates. (D) Dorsal and sagittal views of force distributions within a single cell (left) and two connected cells (right) in our model for unperturbed cells. Arrow thickness indicates relative strength and direction of force. Cell anterior is in blue and posterior in red. (E) Simulation and in vivo verification of equalized protrusion in leader and trailer. Top panels show results of simulated cell positions at indicated time points and the morphology of an in vivo cell pair when trailer protrusion is upregulated by expression of constitutively active Ras (Rasca). Solid arrows show the direction of migration. Bottom panels show representative positions of migrating cells with respect to the stationary ATMs. Graphs show the cosine of the radian angle of the leader/trailer axis to the axis of migration derived from in vivo and simulations. Inheritance of the perturbing plasmid is followed using the cytoplasmic marker FoxF>mCherry (magenta), and the nuclei of the TVCs and ATMs is marked with Mesp>H2B::GFP histone marker. In vivo data were pooled from two biological replicates. Statistical analysis was performed using Student’s t-test for the experimental data and Student’s t-test with Welch’s correction for the simulation data, ** p<0.01. In simulations here and below, time is measured in units of Monte Carlo step (mcs). (F) Distribution of myosin reporter iMyo-GFP intensity compared to membrane marker Mesp>hCD4::mCherry. Dashed arrows on the merged micrograph indicate the directionality of the line scan, which moves in the direction of the arrow. Mean values with standard error are plotted on the graphs. Data were pooled from two biological replicates.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/70977/elife-70977-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** (A) Typical cell shapes for protrusive and retractive forces distributed within different ranges. (B) Unstable deformation of cell front resulting from focusing the protrusive force in the narrow layer near the flat substrate. (C) Detachment of the trailer from the leader resulting from failure to increase retractive forces in the trailer. (D) Elongation of the leading cell when using the force distribution associated with a single migratory cell. (E) Abnormal cell pair shape produced by loss of protrusive force in trailer and retractive force in leader.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/70977/elife-70977-fig1-figsupp2-v3.jpg)

**Figure 1—figure supplement 2.:** Sphericity is measured using automated Bitplane Imaris function and calculated as the ratio of surface area of sphere with volume equal to that of a cell being analyzed to the actual surface area of the cell. VL, volume of leader cell; VS, volume of sphere that is equivalent to the volume of leader cell; SA, surface area. Table shows individual sphericity values for matched leader/trailer cells.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/70977/elife-70977-fig1-figsupp3-v3.jpg)

**Figure 1—figure supplement 3.:** (A) Micrograph at left shows a dorsal view of a leader/trailer cell pair with leader oriented to the right. Dashed lines show positions of line scans of fluorescence intensity (a.u.) taken in the green (Mesp>iMyo::GFP) and magenta (Mesp>hCD4::mCherry) channels with the center of the line positioned over the cell-cell junction. A total of 19 cell pairs from two biological replicates were analyzed with three line scans per pair. All line scans were of the same length, and fluorescence intensity was averaged per cell pair to represent relative intensity of the two markers. Averages of fluorescence intensities of 19 embryos are shown in the graph with means and SEM. (B) Sagittal slice through a representative trunk ventral cell (TVC) pair with membrane marker Mesp>hCD4::mCherry in magenta and Mesp>iMyo::GFP in green. Images are oriented with leader to the right. Dashed line represents position of cell-cell junction.

Here, we model TVC shape and behavior using the Cellular Potts Model (CPM) (Thüroff et al., 2019; Rens and Edelstein-Keshet, 2019; Fortuna et al., 2020). In the CPM framework, each cell is a shifting shape described by a sum of mechanical energies of cell-substratum and cell-cell adhesions, surface tension and hydrostatic pressure, and protrusion and retraction forces (Figure 1A, bottom panel). These energies effectively correspond to realistic cytoskeleton-generated forces (Rens and Edelstein-Keshet, 2019; Sherrard et al., 2010). The cell boundaries fluctuate, mimicking random force and movement on subcellular scale, and shape changes minimizing the total energy are accepted. This results in evolving, collectively moving cells (Videos 1 and 2). CPM is advantageous in modeling the TVC pair as it allows us to reproduce both the detailed evolving 3D shapes of motile cells and the deformation of tissues surrounding these cells over a reasonable computational time (Thüroff et al., 2019; Rens and Edelstein-Keshet, 2019; Fortuna et al., 2020) – one of the more challenging tasks for detailed force-balance models in 3D (Wu et al., 2018).

![Video 1.](https://cdn.elifesciences.org/articles/70977/elife-70977-video1.mp4.jpg)

![Video 2.](https://cdn.elifesciences.org/articles/70977/elife-70977-video2.mp4.jpg)

By examining the distribution of forces required to recapitulate the shape of migrating TVCs in silico, we first predict the polarized distributions of protrusive activity, cell-matrix adhesion, and actomyosin contractility across cells, and test these predictions using in vivo observations and molecular perturbations. We propose that the leader and trailer cells form the simplest possible supracellular arrangement of a migratory collective. We hypothesize that this arrangement emerges from a leader-trailer mode of migration, which invokes polarized abilities to respond to extracellular guidance and mutual cell-cell attraction. Our model explains the preference for a linear arrangement of cells polarized in the direction of migration as this arrangement improves the persistence of migrating cells, which can presumably better buffer variations in migration cues. Finally, our model predicts that the linear arrangement of cardiopharyngeal progenitors allows them to distribute forces in a way that helps them deform the trunk endoderm and facilitates their migration despite the mechanical resistance exerted by the developing gut primordium.

## Results

### Polarized protrusive and retraction forces are distributed across a supracellular collective

Cell morphology reflects and conditions cellular behavior, inasmuch as both emerge from underlying mechanical forces (Figure 1A; Mogilner and Keren, 2009). From that standpoint, cell shape provides a phenomenological proxy to biophysical forces driving cellular behavior (Campàs et al., 2014; Maitre, 2017). In migrating collectives, leader cells typically adopt splayed morphologies with protrusive activity at the leading edge, while trailing cells display a tapered rear (Nabeshima et al., 1995). This organization is conspicuous in pairs of multipotent cardiopharyngeal progenitor cells (aka TVCs; Figure 1A) in the embryo of the tunicate Ciona. TVC pairs migrate along a stereotypical path, canalized by surrounding tissues, while maintaining cell-cell junctions and polarizing along the direction of migration: the leader cell generates a protrusive edge, while the retracting trailer cell has a tapered rear and higher sphericity (Christiaen et al., 2008; Gline et al., 2015; Bernadskaya et al., 2019; Figures 1A and 2A, Figure 1—figure supplement 2). The Ciona TVCs thus provide the simplest possible example of directional migration of a polarized cell collective.

![Figure 2.](https://cdn.elifesciences.org/articles/70977/elife-70977-fig2-v3.jpg)

**Figure 2.:** (A) Establishment of leader/trailer polarity as measured by the asymmetry that develops between leader and trailer sphericity as cells polarize in the direction of migration. Diagram depicts dorsal view of cells at stages when sphericity was calculated. Migratory cells are highlighted in green. L, leader; T, trailer; ATM, anterior tail muscle. Scatter plots show mean with standard error. Data were pooled from three biological replicates. Statistical significance tested using ANOVA followed by Bonferroni test to compare means. *p<0.05 (B) Simulation of decreasing extracellular matrix (ECM) adhesion in one cell (red) of a migrating cell pair. Cells are migrating to the right starting in a parallel orientation as shown in T = 100 Monte Carlo steps (mcs). Bar graphs show likelihood of either cell assuming the leader or trailer position in either control conditions (50/50 likelihood) or when adhesion in red cell is decreased. Standard error of proportion is shown, and statistical analysis of the proportions is done using Fisher’s exact test. (C) In vivo modulation of ECM adhesion using mosaic inheritance of the Foxf>Intβ1dn, Foxf>Ddrdn, and Foxf>RhoDFca, marked by Foxf>mCherry. Diagram shows a schematic of mosaic inheritance of transgenes and resulting distribution of mCherry fluorescence. Bar graphs show likelihood of cell that inherits the transgenic constrict to be found in either leader or trailer position. Data were pooled from three biological replicates. Error bars are standard error of proportion. Statistical analysis was performed using Fisher’s exact test. (D) Micrographs show distribution of Mesp>Lifeact::GFP in leader and trailer cells. Image on the right shows a representative rendered cell pair surface with spot detection based on 10% highest GFP intensity. Spots are color-coded from smallest (blue) to largest (red). Scatter plot on the right shows number of GFP puncta per cell. Data were pooled from two biological replicates. Statistical analysis was performed using Student’s t-test. *p<0.05.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/70977/elife-70977-fig2-figsupp1-v3.jpg)

**Figure 2—figure supplement 1.:** Micrograph at the bottom right shows trunk ventral cell (TVC) pair expressing Foxf>Intβ1dn with membranes marked by Mesp>hCD4::GFP.

We leveraged the TVCs’ simplicity and experimental tractability, combined with mathematical modeling, to simulate cell shape and behavior from first biophysical principles. We used a previously established experimental perturbation, whereby mosaic expression of a dominant-negative inhibitor of the secretory pathway (Sar1dn) stalls the migration of the transfected TVC while allowing the other cell to migrate on its own, and compare the shapes of single cells to those of cell pairs (Gline et al., 2015). Single migrating TVCs generally display morphologies intermediate to those of either leader or trailer, generating both a leading edge and a retracting rear end, thus producing overall shapes similar to migrating pairs (Figure 1B and C). We further quantified the similarity of cell shapes by comparing the aspect ratios, defined as the ratio between the length and width of the smallest rectangular bounding box that can enclose the cell or cell pair, of single migrating TVCs with TVC pairs. This comparison shows that both maintain similar overall shapes (Figure 1C), leading us to hypothesize that similar force distribution profiles may exist in both conditions.

CPM (Thüroff et al., 2019; Rens and Edelstein-Keshet, 2019; Fortuna et al., 2020) predicts that cell morphologies emerge from the mechanical energies of diverse force-generating processes distributed within each cell (Figure 1A, bottom panel). To explore the cell-autonomous mechanics responsible for the observed shapes of one- and two-cell systems that we can observe in vivo, we selected parameters characterizing the adhesion, cortex tension, and hydrostatic forces from general considerations that apply to most motile cells (see Materials and methods), and investigated the spatial distribution of protrusive and retractive forces that would best recapitulate observed cell shapes as indicated in Figure 1B. We first focused on the spatial-angular distribution of protrusive and retractive forces in single cells. By varying the width of the angular segment for retraction forces at the rear, we observed that narrowly focused retractive forces cause aberrant widening of the leading edge and fail to produce the tapered rear (Figure 1—figure supplement 1A, bottom row), suggesting that a broadly retracting trailing edge better accounts for the observed shapes of single cells.

In contrast, a wide protrusive force distribution widens and flattens the leading edge (Figure 1—figure supplement 1A), recapitulating the observed shapes (Figure 1B). In general, several combinations of protrusive and retractive force distributions produce cell shapes that qualitatively recapitulate observations (Figure 1B, Figure 1—figure supplement 1A). Simulations showed that the single-cell shape is faithfully reproduced if the retraction force is centripetal, radially converging to the cell center along the width and heights of the rear half of the cell. Similarly, protrusion force is centrifugal in the front half of the cell, diverging from the cell center (Figure 1D, Video 1). Other force distributions tested in the cell are discussed in Appendix 1. The polarized distributions of protrusive and retractile forces at the leading edge and trailing rear, respectively, are thus consistent with classic models of single-cell migration on two-dimensional substrates (Ridley et al., 2003).

Empowered by our single-cell simulations, we turned to modeling polarized cell pairs. Although single TVC migration (Gline et al., 2015) suggests that individual TVCs are migration-competent and do not require a cell partner, computationally stitching two identical single-cell models failed to reproduce the polarized morphology of migrating pairs. Specifically, when simulated leader and trailer cells were endowed with equivalent protrusive activity, the width of the trailer front extended beyond the width of the leader posterior, a morphology not observed in control embryos (Figure 1E, yellow two-headed arrow). This also impacted collective polarity, causing the simulated trailer to leave its posterior position and travel side-by-side with the leader (Figure 1E). We quantified this phenomenon by calculating cos(θ) of the angle at which the leader/trailer axis intersects the direction of migration (Figure 1E). The predicted leader-dominated protrusive activity of the cell pair was consistent with previous observations that the typical leader TVC has a wide leading edge with lamellipodia-like protrusions that depend on Rhod/f- and Cdc42-controlled actin networks (Christiaen et al., 2008).

Remarkably, we could reproduce this predicted behavior in vivo by using the TVC-specific minimal Foxf enhancer to misexpress a constitutively active form of Rhod/f mosaically in either the prospective leader, trailer, or both cells, and measure the angle between the TVCs and their stationary sister cells, the anterior tail muscles (Christiaen et al., 2008; Beh et al., 2007) (ATMs) (Figure 1E). Under these conditions, experimentally increasing protrusive activity in one or both migrating cells disrupted their collective polarity, with cells more likely to migrate in parallel as predicted by in silico simulations (Figure 1E). This result suggests that the protrusive activity is suppressed in trailer cells compared to leader and single cells.

Nevertheless, simulations that reduce protrusive activity in the trailer without increasing its retractile forces cause the leader to detach and move forward on its own, overcoming significant mutual adhesion between the two cells (Figure 1—figure supplement 1C). This suggests that some protrusive activity in the trailer is still required, and that, in paired TVCs, the cells exert equivalent forces, while coordinating their activities to distribute protrusive and retractile forces to the leader and trailer cells, respectively (Figure 1—figure supplement 1B–E).

Next, we sought to further probe the supracellular model using phenomenological observations. Notably, the best computational recapitulation of observed shapes was achieved with centripetal retractive forces dominating in the trailer, pulling the cell rear forward and down, while the centrifugal protrusive forces in the leader pushed the front forward (Figure 1B and D, Video 2). The morphology produced by this force distribution also reproduced the measured aspect ratio of the motile TVC pair and single cells (Figure 1C), as well as asymmetries of the leader and trailer as reported by the ratio of their sphericities in vivo compared to simulations (Figure 1B). This is reminiscent of the centripetal character of actomyosin contractility (Yam et al., 2007), which led us to analyze myosin distribution in migrating cell pairs. Consistent with the model’s prediction of a trailer-polarized retractile activity, we observe that iMyo-GFP, an intrabody that recognizes non-muscle myosin II through a conserved epitope (Chaigne et al., 2013; Hashimoto et al., 2015), accumulates at the rear of the trailer cell and is relatively depleted from the leader-trailer junction (Figure 1F, Figure 1—figure supplement 3), implying that the retraction in the trailer is dominant, while the retractive force in the leader is weak, lending further support to the hypothesis that TVC pairs migrate as a supracellular collective.

Taken together, our computational predictions and experimental observations support a model where pairs of multipotent cardiopharyngeal progenitors migrate as a polarized supracellular collective, with protrusive activity and myosin-based retraction distributed across leader and trailer cells, respectively.

### Polarized cell-matrix adhesion contributes to leader/trailer states of migrating cells

Cell-matrix interactions and distribution of protrusive activity to the leading TVC result in the generation of a broad leading edge during the establishment of collective TVC polarity (Bernadskaya et al., 2019). The flattened leading edge of the leader lowers the cell's overall sphericity. Conditions that perturb cell-matrix adhesion often increase the sphericity of leading cells, suggesting that they fail to establish flattened protrusions at the leading edge (Bernadskaya et al., 2019). We compared the sphericity of the leader and trailer cells starting with TVC birth at developmental stage 19 prior to migration (Figure 2A). TVCs’ sphericities did not differ at stage 19, suggesting that they are born with equivalent shapes. Cell sphericities begin to differ significantly during migration, indicating establishment of leader/trailer polarity, adoption of distinct states (Figure 2A), and orientation in direction of migration. Collective TVC polarization is abolished by disruption of cell-matrix adhesion by misexpression of a dominant-negative version of the collagen receptor, Discoidin domain receptor (Ddrdn), which alters integrin-mediated cell-matrix adhesion and disrupts polarized Bmp-Smad signaling (Bernadskaya et al., 2019). This suggests that collective polarity and anisotropy of actin dynamics actively mature in response to extracellular cues and that leader/trailer selection can be biased based on the relative amount of cell-matrix adhesion experienced by the TVCs.

We previously showed that integrin ß1 (Intß1)- and Ddr-mediated signaling and cell-matrix adhesion to the basal lamina of the ventral trunk epidermis promote collective polarity and directional movement of TVC pairs (Bernadskaya et al., 2019; Figure 2A). Here, we harnessed the predictive power of our model to explore the consequences of varying the distribution and strength of cell-matrix adhesion forces across the cell pair in silico. We begin by simulating two cells side-by-side with the same protrusive/retractive force distribution, but with cell-matrix adhesion in one of the cells lower than the other. In order to focus on the cell-autonomous behaviors specific to the TVCs, we performed these simulations without modeling the overlying endoderm under which the cells move in vivo. In these conditions, the cell with reduced adhesion was more likely to assume the trailer position (Figure 2B). We tested this prediction in vivo using mosaic overexpression of the dominant negative forms of Intß1 and Ddr driven by the Foxf minimal TVC enhancer, tracked by co-inheritance of the mCherry marker (Figure 2C). In control mosaic embryos, FoxfTVC-driven fluorescent protein expression marks either the leader or trailer cell in equal proportions, consistent with previously published data (Gline et al., 2015; Figure 2C). In contrast, coexpression of Intß1dn increased the proportion of labeled trailer cells to 57% in mosaic embryos (Figure 2C). Cells that inherited Ddrdn were significantly more likely to be in the trailer position, increasing the proportion of mCherry-labeled cells in the trailer position to 66% (Figure 2C). Mosaic expression of RhoDFca has the opposite, albeit not statistically significant, effect, promoting positioning of the labeled cell anteriorly (Figure 2C), further lending support to our hypothesis of leader cells being more protrusive and less retractive than trailers.

Of note, one simulation of more acute reduction of cell-matrix adhesion in the trailer of leader-trailer polarized cell pairs occasionally caused in silico tumbling behavior (Figure 2—figure supplement 1), where the low-adhesion trailer cell climbs on top of and over the leader cell with normal adhesion. We previously observed this distinctive behavior in vivo (Figure 2—figure supplement 1), following TVC-specific inhibition of cell-matrix adhesion, and reduction of collagen9-a1 secretion from the adjacent trunk endoderm (Gline et al., 2015; Bernadskaya et al., 2019). Taken together, these observations indicate that reduced cell-matrix adhesion promotes positioning of the cell with reduced adhesion posterior to the cell with more adhesion, thereby preferentially adopting the trailer state, which in turn suggests that cell-matrix adhesion is stronger in leader cells.

Our previous work has suggested that leading cells are more adhesive than trailer cells (Bernadskaya et al., 2019). To evaluate the distribution of adhesion-associated actin structure, we assayed the distribution of F-actin in leader/trailer cell pairs using Lifeact::GFP. The F-actin marker localized to the leading edge and an intracellular punctate pattern, suggesting association with adhesion complexed and/or intracellular vesicles (Figure 2D). Quantifications indicated that leader cells consistently contained more ventral Lifeact::GFP+ F-actin puncta than trailer cells, supporting the prediction that F-actin-rich adhesion complexes are enriched in leading cells during TVC migration (Figure 2D). Taken together, these results indicate that increased cell-matrix adhesion and protrusive activity are hallmarks of the leader cell state during collective cell migration.

### Hierarchical guidance orients collective polarity in the direction of migration

From the above sections, a picture emerges whereby the supracellular organization of migrating pairs of cardiopharyngeal progenitors is characterized by leader-polarized protrusive activity and cell-matrix adhesion, and trailer-polarized deadhesion and myosin-driven retraction. Both experimental and simulated disruptions of this supracellular polarity alter directionality, marked by alignment of the leader-trailer axis with the direction of migration. However, the two cells are not arranged in a linear leader-trailer orientation at birth (Figure 3A), and previous observations indicated that either cell can assume a leader position, although single-cell lineage tracing indicates that the leader emerges from the most anterior cell in ~95% of embryos (Gline et al., 2015).

![Figure 3.](https://cdn.elifesciences.org/articles/70977/elife-70977-fig3-v3.jpg)

**Figure 3.:** (A) Evolution of trunk ventral cell (TVC) polarization. Panels show in vivo-rendered images of cells at the indicated embryonic stages. Leader in blue, trailer in red, non-migratory anterior tail muscles (ATMs) in white. Spheres inside cells mark the center of mass, sphere to the right indicates direction of anterior migration. Angle theta between the axis of leader/trailer and direction of migration is indicated. (B) Three hypothesized polarization modes for two-cell migration. Independent: cells polarize independently in the signal direction and move with the same speed. Faster-slower: cells polarize independently in the signal direction, but one cell moves faster than the other. Leader-trailer: one cell (leader) follows the signal direction, while the other (trailer) polarizes in the direction of the leader’s center of mass. L, leader; T, trailer. (C) Establishment of alignment between the leader/trailer axis and direction of migration. Cos(θ) is shown for indicated embryonic stages. Data were pooled from two biological replicates. Statistical analysis was performed using one-way ANOVA and Bonferroni post test. **p<0.01. (D) Left: the simulated evolution of two cells’ geometry, quantified as cosine of the angle between the line connecting the cells centroids and the signal direction, ($cos\theta$), for the three polarization modes shown in (B). Five simulations are run for each mode, and the shaded area shows the standard error. Center: representative snapshots of two cells reaching linear arrangement or at the end of simulation using each mode. The colors of the frames correspond to the dataset on the graph. Right: scatter plot showing the time when $\theta$ reaches $\pi/4$ for two modes with mean and standard error and statistical analysis using Student’s t-test with Welch’s correction. (E) Top: hypothesized polarization modes for three cells. Independent: cells polarize independently in the signal direction and move with equal speeds. Faster-slower: cells polarize independently in the signal direction, in this case, the leader travels the fastest, trailer the slowest, and middle cell travels at an intermediate speed. Leader-trailer: one cell (leader) follows the signal direction, middle cell polarizes towards the leader, and trailer polarizes toward the middle cell. Bottom: simulation of the three-cell group polarization under the three hypothesized polarization modes. Left: the initial cell arrangement in silico (top) and in vivo (bottom). Note that in vivo there are always four cells prior to migration arranged in a rectangular pattern. Center: the polarization of migrating cell clusters over time is quantified by the cosine of the angle between the lines connecting the leader and the two posterior cells separately, as shown in (F). Five simulations were run for each mode, and shaded area shows the standard error. Right: representative snapshots when the three cells reach linear arrangement for the three modes examined (for the independent-same mode, linear arrangement is never reached, snapshot shows cells at the end of a simulation run). The colors of the frames correspond to the datasets on the graph. (F) Three migratory cells are linearly arranged in the direction of migration in vivo. Bar graphs show the proportion of TVCs that migrate as either three or four cells under induced MAPK signaling by Mesp>Rasca and proportion of cell groups that are linearly polarized in each subset. Data were pooled from two biological replicates. Error bars show standard error of proportion. (G) Effects of modulating cell-cell adhesion on the contacting area between the two cells and on their speed, quantified by the percentage of total surface area of the leader cell (top graph, left y-axis, blue symbols), on the ability of the cell pair to polarize in the direction of migration quantified by $cos\theta$ (top graph, right y-axis, red symbols), where $\theta$ is the angle between the line connecting two cells and the moving direction as shown in the top image on the left, and on the total displacement of the leader/trailer pair (bottom graph). x-axis shows the relative energy of the cell-cell junction (the adhesion parameter is rescaled here so that larger value means stronger cell-cell adhesion). Images show cell pairs with either high (top) or low (bottom) cell-cell adhesion. Arrow represents leader/trailer axis.

We analyzed the establishment of leader/trailer polarity from the initial time of TVC birth to full polarization and alignment with the direction of migration over four embryonic stages encompassing TVC migration (Hotta et al., 2007). Tracking cos(θ) to quantify the alignment of cell pairs with direction of migration, with θ defined as the angle between the leader-trailer axis (axis connecting their centers of mass) and the direction of migration (Figure 3A and B), shows that prior to migration at embryonic stage 17 (8.5 hr post fertilization [hpf]), the leader/trailer axis is more orthogonal to the future direction of anterior movement. The cells reach their full polarization and alignment with direction of migration by stage 21, a process that takes approximately 1.5 hr at 18°C, after which they continue to migrate as a fully polarized cell pair for approximately 2 hr (Figure 3A and C).

We sought to explore possible cell-autonomous mechanisms governing the establishment of collective leader-trailer polarity and its alignment with the migration path. We modeled three possible directional modes for the cell pair without including directional noise (Figure 3B): the independent mode, where the two cells have the same distributions of retractive and protrusive forces and their retractive-protrusive axes are aligned to the right, along the net directional signal from the surrounding tissue; the faster-slower mode, where the total retractive-protrusive force in one cell is scaled up compared to the other cell, thus making one cell faster than the other; and the leader-trailer mode, where the prospective leader’s retractive-protrusive axis is aligned with the external signal direction, while the prospective trailer’s retractive-protrusive axis is oriented toward the leader’s center of mass. In simulations, the two cells are initially placed side-by-side, with their retractive-protrusive axes orthogonal to the migration path (i.e., cos(θ) = 0), thus resembling the arrangement observed in vivo prior to the onset of migration. Simulations show that the cells following the independent mode maintain their side-by-side orientation and fail to align with the migration path (Figure 3DVideo 3). By contrast, either the faster-slower or leader-trailer mode led cells to rearrange into a single file aligned with the migration path (i.e., cos(θ) = 1), with the leader-trailer mode allowing faster alignment, with a half-time to alignment reduced compared to the fast-slower mode (Figure 3D, Video 4). This predicted behavior agrees qualitatively with the progressive polarization of TVCs observed in vivo.

![Video 3.](https://cdn.elifesciences.org/articles/70977/elife-70977-video3.mp4.jpg)

![Video 4.](https://cdn.elifesciences.org/articles/70977/elife-70977-video4.mp4.jpg)

The assumption that the basic rule of follower cells polarizing hierarchically towards leader cells predicts that cells should adopt a linear arrangement of leader and follower states even if the number of migrating cells was increased. To test this, we further probed the distinct migration modes by modeling three migrating cells (Figure 3E, diagram at top). In these simulations, each of the three cells adheres equally to the other two. The modes are similar to those for two cells (Figure 3B), with two adaptations: in the faster-slower mode, one cell is the fastest, another – the slowest, and the third moves with an intermediate speed; the leader-trailer mode becomes the leader-middle-trailer mode, in which the polarization axis of the leader is fixed to the external signal direction, the middle cell’s axis orients towards the leader’s center, and the trailer’s axis orients towards the middle cell’s center. To mirror the initial arrangement observed in vivo, we start three-cell simulations with individual cells distributed in a triangular pattern (Figure 3E, Videos 5 and 6). Similar to two-cell simulations, the independent mode failed to produce linear arrangements and the cells remained in triangular formation with no leader emerging, potentially due to the three-cell system minimizing the adhesive energy when each cell maintains contacts with the other two (Figure 3E). Although cells arranged more linearly under the faster-slower mode (Figure 3E, Video 5), they failed to align with the direction of migration for an extended period of time, only achieving the single-file arrangement towards the end of simulations (Figure 3E). The leader-middle-trailer mode was again the most effective at producing full polarization and linear order rapidly (Figure 3E, Video 6), suggesting that basic hierarchical rules of collective polarization can produce linear arrangements of cell groups containing variable numbers of cells. We tested this prediction in vivo, where ectopic FGF/M-Ras/Mek-driven induction within the Mesp+ lineage causes three or four cells to assume a cardiopharyngeal identity and migrate collectively (Christiaen et al., 2008; Davidson et al., 2006; Razy-Krajka et al., 2018). In conditions such as misexpression of a constitutively active form of M-Ras using the Mesp enhancer (Razy-Krajka et al., 2018) (Mesp>M-Rasca), the cells align in the direction of movement in 57% of the experimental embryos, with a single anterior leader, followed by two (13%) or three (87%) cells arranged in a single line (68%, n = 31) (Figure 3F, Videos 7 and 8). This provides experimental support for our leader-trailer polarization model.

![Video 5.](https://cdn.elifesciences.org/articles/70977/elife-70977-video5.mp4.jpg)

![Video 6.](https://cdn.elifesciences.org/articles/70977/elife-70977-video6.mp4.jpg)

![Video 7.](https://cdn.elifesciences.org/articles/70977/elife-70977-video7.mp4.jpg)

**Video 7.:** B7.5 lineage. Nuclei are marked with Mesp>H2B::GFP. Epidermal cells are marked with EphB1>hCD4::mCherry. Epidermal marker is used to orient the embryo.

![Video 8.](https://cdn.elifesciences.org/articles/70977/elife-70977-video8.mp4.jpg)

**Video 8.:** B7.5 lineage. Cell membranes are marked with Mesp>hCD4::GFP. Epidermal cells are marked with EphB1>hCD4::mCherry. Epidermal marker is used to orient the embryo.

Since the ability to organize cell collectives requires maintenance of cell-cell junctions, we also investigated the effect of cell-cell adhesion strength on collective polarization. Multiple simulations varying the cell-cell adhesion energy in our basic model show that cell-cell adhesion strength does not affect the total displacement of cell pairs over long time intervals (Figure 3G, bottom right). However, increasing or decreasing cell-cell adhesion energy causes the cell-cell boundary area to increase or decrease, respectively (Figure 3G, top right, blue plot), which leads to a drastic misalignment of cells with the direction of migration beyond a cell-cell adhesion strength of 10 (relative energy units). This suggests that the extent of cell-cell adhesion may be regulated in vivo and that cells with high cell-cell adhesion will reorient their supracellular polarity away from the direction of migration.

### Collective polarity fosters persistent directionality

Having characterized ground rules that govern collective arrangement of migrating cardiopharyngeal progenitors, we sought to explore the specific properties conferred by this supracellular organization. Unlike specialized motile cells, such as Dictyostelium, fish keratocytes, or neutrophils, which can migrate at ~10 µm/min, 7.5 μm/min, and ~19 μm/min, respectively (Buenemann et al., 2010; Graham et al., 2013; Hoang et al., 2013), TVCs move at ~0.4 µm/min, which is relatively slow, but not unexpected for a developmental migration that contributes to the establishment of accurate cellular patterns in the embryo (Trepat et al., 2012). We reasoned that this behavioral accuracy would be reflected in the cells’ persistence, defined as the ratio of beginning-to-end displacement to trajectory length (Gorelik and Gautreau, 2014; Figure 4A). Directional noise, which counters persistence and accuracy, emerges from inherent stochasticity of motile engines, random fluctuations of external cues, and/or signal transduction (Tang et al., 2014) and can cause meandering trajectories of cells (Wu and Zhang, 2015). We therefore simulate noise by adding directional stochasticity to the model of two cells in the leader-trailer mode and compare the persistence of migrating cell pairs with that of single cells (Figure 4A and B). In simulations, motile cell pairs are always more persistent than single cells when centers of mass are tracked over time for each condition, suggesting that single cells are more sensitive to directional stochasticity. Of note, the total length of the migration path in the simulations was not altered, suggesting that the decreased displacement is a function of the meandering path traveled by the less persistent single cells (Figure 4B).

![Figure 4.](https://cdn.elifesciences.org/articles/70977/elife-70977-fig4-v3.jpg)

**Figure 4.:** (A) Left: simulation of migration persistence over time for single cell and the centroid of the cell pair. The shaded area shows the standard error. In the model, green arrows show the direction of active forces for each cell that is directionally biased but also fluctuates randomly. The leader cell is biased to the right, which is the direction of the external cue, and the trailer cell is biased to the leader cell. $\phi_{L}$ and $\phi_{T}$ are the angles between the green arrows and the right direction, and $\theta$ is the angle between the line connecting two cells and the right direction. The specific stochastic equation for $\phi$ is given in the Materials and methods section using the same angle notations. The diagram on top shows the relationship between displacement and track length and $persistence=\frac{displacement}{track length}$ . (B) Comparison of tracks from simulations of either migrating cell pairs or single cells within the same simulation time. Shaded vertical lines represent mean final displacement. Graphs on the right show mean total displacement and mean total track length with standard error. Statistical analysis was performed using Student’s t-test. *p<0.05. (C) In vivo analysis of total displacement of leader cells in a cell pair and single trunk ventral cells (TVCs) from the anterior tail muscle (ATM). TVC and ATM nuclei are marked with Mesp>H2B::GFP, epidermal cell membranes are marked with EphB1>hCD4::mCherry. Data were pooled from two biological replicates. Scatter plot shows average displacement and standard error. ***p<0.001. (D) In vivo migration of TVC pairs compared to single TVC. Nuclei of the cells are used to track cell migration path in 4D datasets. Paths are color-coded from early (blue) to late (red). Scatter plot shows mean persistence of leader (n = 8), trailer (n = 8), and single TVC (n = 4) with standard error. Statistical analysis was performed using one-way ANOVA with Bonferroni post test. *p<0.05, **p<0.01.

We compared the final displacement of single TVCs in vivo to the total displacement of the leader TVC. In agreement with simulations, TVC pairs migrated further from the anterior ATM than single cells (Gline et al., 2015; Figure 4C). To test if this was due to the loss of persistence, as predicted by the above simulations, we compared the persistence of cell pairs by tracking the nuclei of leader and trailer cells in 4D datasets and compared to the migration paths of single TVCs (Figure 4D, Videos 9 and 10). In control conditions, the leader and trailer migrate with similar persistence; however, the migration paths of single TVCs were significantly less persistent than those of either leader or trailer cells, suggesting that in vivo, collective organization confers robust directionality to the migrating cells.

![Video 9.](https://cdn.elifesciences.org/articles/70977/elife-70977-video9.mp4.jpg)

**Video 9.:** Nuclei are marked with Mesp>H2B::GFP. Epidermal cells are marked with EphB1>hCD4::mCherry. Epidermal marker is used to orient the embryo. Track traces the path of the nucleus centroid during migration.

![Video 10.](https://cdn.elifesciences.org/articles/70977/elife-70977-video10.mp4.jpg)

**Video 10.:** Nuclei are marked with Mesp>H2B::mCherry, and cell membranes are marked with Mesp>hCD4::GFP. Epidermal cells are marked with EphB1>hCD4::mCherry. Epidermal marker is used to orient the embryo. Track traces the path of the nucleus centroid during migration.

In summary, both simulations and in vivo observations suggested that polarized cell pairs migrate with increased robustness to fluctuations in directionality compared to single cells.

### Polarized cell pairs overcome mechanical resistance from the endoderm during migration

The above sections indicate that collective organization endows the TVCs with defined properties (e.g., persistence) that are intrinsic to cell pairs and determine the characteristics of their migration. However, TVCs migrate surrounded by embryonic tissues that canalize their behavior (Christiaen et al., 2008; Gline et al., 2015; Bernadskaya et al., 2019). Specifically, shortly after the onset of migration, the TVCs penetrate the extracellular space between the ventral trunk epidermis, which they use as stiff substrate, and the softer trunk endoderm, which locally deforms as TVCs progress anteriorly (Gline et al., 2015; Figure 5A). We reasoned that the trunk endoderm likely exerts mechanical resistance to the passage of the TVCs and hypothesized that this resistance may be better overcome by polarized cell pairs (Figure 5A and B). We predicted that when two cells migrate in a leader-trailer arrangement, the surface that the leader exposes to mechanical resistance is equivalent to that of a single cell, while the trailer pushes from the rear, therefore adding forward-bearing compression force to overcome endoderm resistance (Figure 5B).

![Figure 5.](https://cdn.elifesciences.org/articles/70977/elife-70977-fig5-v3.jpg)

**Figure 5.:** (A) Micrographs of stage 23 embryos showing the endodermal pocket formed during trunk ventral cell (TVC) migration. Embryos are oriented with anterior to the right. Endodermal cells are marked with Nkx2-1>hCD4::GFP (green), TVCs are marked with Mesp>3xmKate2 (magenta). Yellow arrows point to depression pocket left in the endoderm by migrating TVCs. (B) Proposed model for higher efficiency of supracellular cell pairs in overcoming resistance from the endodermal tissue (pink) during migration: the adhesive cell pair shares the resistance force (yellow arrows), which otherwise each single cell must overcome alone. Pressure from the posterior trailer (purple arrows) can help the cell pair overcome resistance from the endoderm. Size of the arrows below the graphics represents relative strength of the force experienced by the cell in the direction of the arrow. (C) Simulated supracellular cell pair underneath the endoderm. Epidermis is shown in green. The endoderm is rendered transparent. (D) Speed comparison between single cell and differently arranged cell pairs with different profiles and force distributions under the endoderm of varying stiffness. Five simulations are run for each condition; the error bar is the standard error. Statistical analysis is performed using Brown–Forsythe and Welch ANOVA test. *p<0.05, **p<0.01, ****p<0.0001.

To explore this argument, we added deformable endoderm cells to our model and simulated cell migration under varying endoderm stiffness, comparing the effects on migration speed. We simulate migration of one- and two-cell systems, tracking the simulated cells’ centers of mass with five simulations run per condition shown in Figure 5D. When modeling a softer endoderm, by modulating volume preservation and cortical tension parameters relative to those of the TVCs (see Appendix 1), polarized cell pairs perform best, whether in supracellular mode or equivalent force distribution, while side-by-side cells were the slowest, presumably because they expose a greater surface to mechanical resistance (Figure 5B and D). Notably, two equivalent cells moving in single file advanced marginally faster than the supracellular pair, suggesting that cell alignment itself is a key determinant of efficient migration under the soft tissue. When simulating a stiffer endoderm, the advantage of supracellular organization became more apparent. In these simulations, the supracellular collective migrated faster than other arrangements (Figure 5D). Notably, cells migrating side-by-side were slower than single cells with either endoderm stiffness (Figure 5D), which is consistent with the notion that a more extended surface of contact with the endoderm exposes them to greater mechanical resistance, while the smooth teardrop shape of single cells may be near optimal for lowering the resistive deformations of the endoderm. This suggests that the collective shape resulting from supracellular organization optimally minimizes mechanical resistance of the surrounding tissue to migration.

The predicted relative speeds of cells migrating under the endoderm are based on the simplest model, which assumes that the endoderm’s primary effect is mechanical resistance to deformation. In vivo, the interactions between TVCs and endoderm cells are likely more complex, involving indirect cell-cell signaling via extracellular deposition of collagen9-a1 by the endoderm (Bernadskaya et al., 2019). In summary, the combined in silico simulations and in vivo observations indicate that the collective organization of migrating cardiopharyngeal progenitors allows them to overcome mechanical resistance from the deforming endoderm and reach a typically mesodermal position between germ layers for cardiac organogenesis.

## Discussion

Complex multicellular behaviors, including directed collective cell migration, emerge from the context-specific integration of universal dynamic processes, which operate at subcellular scale and are coordinated within and across cells (Bernadskaya and Christiaen, 2016). The sheer complexity of integrated cellular systems constrains direct experimental interrogations, but mathematical models and simulations provide a powerful complement to probe the relative biophysical contributions of subcellular processes to cellular behavior.

In this study, we used a mathematical model, built from first biophysical principles, to generate computational simulations and explore the morphodynamic space of motile cardiopharyngeal progenitor cell pairs of the tunicate Ciona. Qualitative comparisons with experimental data indicated that the shape of cell pairs, similar to that of a single motile cell, emerges from the distribution of higher protrusive activity and cell-matrix adhesion to the leader cell, whereas the rear of the trailer cell is the primary site of myosin-based retraction. The latter prediction is corroborated by in situ patterns of myosin activity and F-actin distribution. This illustrates that a purely mechanical model such as CPM, which assumes that most active stresses are generated at the cellular periphery in addition to hydrostatic pressure in the cytoplasm, can uncover the biomechanical underpinnings of collective cell shape and movement.

The above patterns of protrusive activity, cell-matrix adhesion, and contractility might seem trivial, considering the well-established organization of individual migrating cells. However, in the ‘supracell,’ the distribution of various cytoskeletal activities across all cells in a collective suggests the existence of mechanisms to ensure such ‘division of labor.’ This simple prediction implies multiple roles for the cell-cell contact, in addition to its anticipated low surface tension.

First and foremost, cell-cell adhesion must be strong enough to maintain the integrity of the collective and permit mechanical coupling, lest cells lose contact and migrate disjointly (Figure 1—figure supplement 1C). Conversely, the model predicts that excessive cell-cell adhesion antagonizes cell-matrix adhesion and disrupts collective polarity. Balancing cell-cell and cell-matrix adhesion may result from either mechanical interaction, as suggested by the model, and/or biochemical cross-talks, as observed in other systems (Martinez-Rico et al., 2010; Ramprasad et al., 2007). The coexistence and contributions of both cell-cell and cell-matrix adhesion to supracellular migration emphasize the hybrid nature of such multicellular systems, where cells adopt intermediate states on an epithelial-to-mesenchymal continuum (Friedl and Mayor, 2017; Bernadskaya and Christiaen, 2016; Lecaudey and Gilmour, 2006).

Close cellular contacts probably facilitate propagation of direct mechanical and biochemical interactions that underlie supracellular migration. We tentatively distinguish ‘information flows’ that propagate in either a back-to-front or a front-to-back fashion (Capuana et al., 2020; Mayor and Etienne-Manneville, 2016). For instance, similar to Xenopus cranial neural crest cells and the zebrafish lateral line primordium (Yamaguchi, 2021), Ciona cardiopharyngeal progenitors appear to focus contractility at the back of the trailer cell, thus suggesting that a ‘rear-wheel’ engine may help power their migration. However, in contrast to neural crest cells and Drosophila border cells, we did not observe supracellular actomyosin ‘cables’ extending across cardiopharyngeal progenitors and there is no exchange of cell positions between TVCs. Instead, we surmise that this ‘rear-wheel’ drive represents a back-to-front mechanical input, which propagates as compression force and emerges from rear-localized myosin activity, possibly in response to chemorepulsive inputs integrated by the trailer. It is also conceivable that cell-cell adhesion complexes suppress myosin-based contractility at the back of the leader cell, for example, through recruitment of Rho GAP molecules by cadherin, as is the case in early Caenorhabditis elegans embryos (Klompstra et al., 2015). In neural crest cells, CIL provides such back-to-front signals that polarize the cell collective, in part through cadherins, ephrin receptors, and planar cell polarity (PCP) pathway molecules (Mayor and Etienne-Manneville, 2016). The PCP pathway offers a particularly tantalizing explanation for the spontaneous alignment of three or four adhering cells following ectopic induction of the cardiopharyngeal progenitor fate, and the existence of a ‘leader-trailer’ mode of collective arrangement predicted by the model.

TVCs’ collective polarity is marked by higher protrusive activity and cell-matrix adhesion in the leader, as indicated by experimental observations and model predictions (Christiaen et al., 2008). Mechanically, it is likely that adhesion complexes are established following lamellipodia formation and support traction forces, which complement rear-driven compression to propel the cells forward. It is conceivable that lower protrusive activity in the trailer limits the deployment of cell-matrix adhesion complexes. However, cell-matrix adhesion in the trailer is probably needed to anchor the cell and allow for its hydrostatic pressure to push the leader. Therefore, one must invoke mechanisms whereby the leader suppresses protrusive activity in the trailer, while permitting the establishment of trailer cell-matrix adhesion in its path. In Drosophila border cells, leader-driven suppression of protrusive activity in follower cells is mediated by Rac (Cai et al., 2014) and by Delta-Notch signaling between tip and stalk cells during angiogenesis (Aspalter et al., 2015). It is thus likely that similar ‘front-to-back’ mechanisms govern the collective distribution of protrusions, and by extension cell-matrix adhesion complexes, in cardiopharyngeal progenitors.

While future work combining biophysical modeling, force measurements, and/or inference from quantified cell shapes is needed to elucidate the mechanisms underlying supracellular organization in vivo, our model and experimental investigations uncover important consequences for directed migration: namely, persistence and mechanical interaction with surrounding tissues. Specifically, both computational simulations and live imaging indicated that the instantaneous directionality of single cells fluctuates more than that of cell pairs. In other words, polarized cell pairs are more persistent. It is possible that cell pairs are better at buffering the noise inherent to navigating a complex and changing environment, in part by distributing interactions over greater surfaces, and integrating guidance cues more accurately.

Finally, our observations indicate that supracellular organization determines the outcome of interactions with surrounding tissues during migration. We previously determined that TVC pairs migrate onto the extracellular matrix (ECM) associated with the basal lamina of the ventral trunk epidermis (Bernadskaya et al., 2019), which presumably offers a stiff substrate permitting traction forces. Of note, a specific collagen, col9-a1, secreted from the trunk endoderm is deposited onto the ECM and necessary for TVC-matrix adhesion and collective polarity (Bernadskaya et al., 2019). Here, we find that the trunk endoderm resists deformation by migrating TVCs, which can nonetheless move forward by aligning and joining forces to push against and deform endodermal cells to penetrate the extracellular space. Our combined simulations and experimental observations thus suggest an effect of supracellular organization on the inter-tissue balance of forces that determine morphogenesis in the embryo.

### Resource availability

#### Lead contact

Further information and requests for resources and reagents should be directed to and will be fulfilled by the lead contact: Yelena Bernadskaya (yb372@nyu.edu).

#### Data and code availability

The codes generated during this study are available on GitHub (Yue, 2021; https://github.com/HaicenYue/3D-simulation-of-TVCs.git copy archived at swh:1:rev:c8a79bc7822f295ab72edb8e3f7660c823c3699e).

#### Experimental model and subject details

Wild caught Ciona robusta (formerly Ciona intestinalis type A) were purchased from Marine Research and Educational Products (M-REP, San Diego, CA). As invertebrate chordates, animal care approval was not needed. Prior to use, animals were housed in a recirculating artificial seawater aquarium under constant illumination to prevent spawning.

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
      <td>Software, algorithm</td>
      <td></td>
      <td>https://github.com/HaicenYue/3D-simulation-of-TVCs.git</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (Ciona robusta)</td>
      <td>Wild-caught</td>
      <td>M-Rep, San Diego,CA</td>
      <td>https://www.m-rep.com</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>RhoDFca-F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>TGAAACTTGTATTGCGGCCGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>RhoDFca-R</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>agacgtacgtGAATTCTCACAATAGCAAACAACAGCAGCAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>iMyo::GFP – F</td>
      <td>This paper</td>
      <td>PCR primers</td>
      <td>ACTTGTATTGCGGCCGCAACCATGGCCGAGGTGCAGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>iMyo::GFP – R</td>
      <td>This paper</td>
      <td>PCR Primers</td>
      <td>gctgagcgcGAATTCTTACTTGTACAGCTCGTCCATGC</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCESA: Mesp &gt; hCD4::GFP (plasmid)</td>
      <td>PMID:30610187</td>
      <td></td>
      <td>B7.5 lineage specific GFP membrane marker</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCESA: Mesp &gt; H2B::GFP (plasmid)</td>
      <td>PMID:30610187</td>
      <td></td>
      <td>B7.5 lineage specific GFP histone/nuclear marker</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCESA: Mesp &gt; iMyo::GFP (plasmid)</td>
      <td>This paper</td>
      <td></td>
      <td>B7.5 lineage specific GFP myosin intrabody</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCESA: Foxf &gt; mCherry (plasmid)</td>
      <td>PMID:30610187</td>
      <td></td>
      <td>mCherry TVC-specific marker</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCESA: EfnB &gt; hCD4::mCherry (plasmid)</td>
      <td>PMID:30610187</td>
      <td></td>
      <td>Epidermal mCherry membrane marker</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCESA: Mesp &gt; 3xmKate2 (plasmid)</td>
      <td>PMID:30610187</td>
      <td></td>
      <td>B7.5 lineage specific mKate2 marker</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCESA: Nkx2−1&gt; hCD4::GFP (plasmid)</td>
      <td>PMID:30610187</td>
      <td></td>
      <td>Endoderm specific GFP cell membrane marker</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCESA: Foxf&gt;Sar1dn (plasmid)</td>
      <td>PMID:25564651</td>
      <td></td>
      <td>TVC-specific dominant negative Sar1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCESA: Foxf &gt; Rhodfca (plasmid)</td>
      <td>PMID:18535245</td>
      <td></td>
      <td>TVC-specific constitutively active RhoD/F</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCESA: Mesp &gt; LacZ (plasmid)</td>
      <td>PMID:30610187</td>
      <td></td>
      <td>B7.5 lineage specific LacZ loading control</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCESA: Foxf &gt; Intβ1dn (plasmid)</td>
      <td>PMID:30610187</td>
      <td></td>
      <td>TVC-specific dominant negative Intβ1</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCESA: Foxf &gt; Rasca (plasmid)</td>
      <td>PMID:18535245</td>
      <td></td>
      <td>TVC-Specific constituitivley active Ras</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCESA: Foxf &gt; Ddrdn (plasmid)</td>
      <td>PMID:30610187</td>
      <td></td>
      <td>TVC-specific dominant negative Ddr</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FIJI</td>
      <td>Schindelin et al., 2012 PMID:22743772</td>
      <td>RRID:SCR_002285</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Bitplane Imaris</td>
      <td>Bitplane Imaris</td>
      <td>RRID:SCR_007370</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism 9</td>
      <td>https://www.graphpad.com/</td>
      <td>RRID:SCR_002798</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Electroporation and transgene expression

C. robusta (formerly known as C. intestinalis type A) adults were purchased from M-Rep. Gamete isolation, fertilization, dechorionation, and embryo incubation were performed as previously published (Christiaen et al., 2009a; Christiaen et al., 2009b). The amount of DNA electroporated varied from 10 µg to 90 µg. Animals were reared at 22–24°C. Embryos used for direct visualization of fluorescent markers were fixed in 4% MEM-FA for 30 min, cleared with an PBST-NH4Cl solution (50 mM NH4Cl, 0.15% Triton-X100, 0.05% Tween-20 in 1× PBS), mounted in 50% glycerol supplemented with 2% Dabco 33-LV antifade reagent (Sigma-Aldrich, #290734) and imaged using a Leica SP8 X Confocal microscope.

### Live imaging and TVC tracking

To generate 4D datasets, embryos at 4.5 hpf FABA stage 15 were mounted on glass-bottom microwell Petri dishes (MatTek, part# P35G-1.5–20C) in artificial seawater. Plates were sealed by piping a border of vaseline and 5% (v/v) mineral oil (Sigma, #M841-100ml) and covered with a 22 × 22 Fisherbrand Cover Glass (#12-541-B). Embryos were imaged on a Leica inverted SP8 X Confocal microscope using the 40× water immersion lens at 512 × 512 resolution every 3.5 min for 4–5 hr. B7.5 lineage nuclei and epidermal cell membranes were visualized using Mesp >H2B::GFP and EfnB>hCD4::mCherry, respectively, and TVC migration was tracked using Bitplane Imaris Software Spots module.

### Image acquisition

All images were acquired using the Leica SP8 X WLL confocal microscope using the 63× glycerol immersion lens, NA = 1.44. Z-stacks of fixed embryos were acquired at the system optimized Z-step, 512 × 512 resolution, 600 Hz, and bidirectional scanning. Multiple HyD detectors were used to capture images at various wavelengths.

### Quantification and statistical analysis

#### Morphometrics analysis

The membrane marker Mesp>hCD4::GFP was used to segment the TVCs and derive morphometric measurements such as sphericity, area, and volume in Bitplane Imaris using the Cell function with cell segmentation calculated from cell membranes with an average cell size of 6. Thresholding is adjusted based on individual image properties. Z-steps were normalized to achieve equal voxel size in X, Y, and Z planes. TVCs were then segmented and resulting cells were exported to separate surfaces. For experiments described in Figure 2A, no marker was used to follow transmission of Foxf>Ddrnd and all cells were analyzed. Under these conditions, there is an 80% chance that any given cell has inherited the Ddrdn perturbation. To calculate the distance or angle between cells, a point was placed at the center of mass for each cell using either the nucleus or the cell object using the Bitplane Imaris Measurement module.

#### Image preprocessing

All 3D stacks were imported and converted to Imaris format. Images were reoriented and cropped with the leader cell to the left. An automated Gaussian filter and background subtraction was applied to all images using the Imaris Batch module. Images were projected to 2D using Maximum Intensity Projection to reflect the dorsal view of the cells and exported as TIFFs for analysis in Fiji.

#### Aspect ratio calculation

2D projected images were imported into Fiji and converted to 8-bit format. A threshold was applied to each individual image, and empty spaces were filled using the Binary -> Fill Holes function. Resulting object was used to derive the aspect ratio using the Analyze Particles function. In simulation, black-and-white images were obtained using imbinarize function in MATLAB and then regionprop.BoundingBox function was used to get the minimal rectangle that enclose the object. Aspect ratio is the ratio between the width and length of this rectangle.

#### Myosin intensity analysis

Images were imported into Fiji. Using the freehand line function with a width of 10 units, a scan was performed on the leading edge of the leader cell, the cell-cell junction, and the membrane of the trailer cell using the membrane marker as a guide. The intensity of iMyoGFP and the membrane marker Mesp>hCD4::mCherry along the scan was measured using the Plot Profile function and exported as intensity along the line scan. This was done for each cell pair. Readings along the line scan were aligned based on the starting position of the scan and averages were calculated.

#### Lifeact::GFP distribution analysis

The Cell function was used to segment leader and trailer cells with vesicle detection. The membrane marker Mesp>hCD4::mCherry was used for membrane detection based on membrane signal intensity. Vesicles or spots were detected in each cell object, with the volume growing option to allow for detection of vesicles of varying size. The threshold setting for spot detection in the green channel was set to use the top 10% of GFP signal intensity.

#### Statistical analysis and data representation

For all data comparing two samples of continuous variables, the Wilcoxon rank-sum test (also known as the Mann–Whitney test) was used. Categorical data were analyzed using Fisher’s exact test. Simulation data were analyzed using Student’s t-test with Welch’s correction. For datasets containing more than two conditions and taking into account cell type (leader/trailer), a two-way ANOVA followed by the Bonferroni post test was used. For all datasets containing nominal variables, a chi-square test was used. p-Values are reported as follows: *p<0.05, **p<0.01, ***p<0.001.

#### Model

We use the CPM (Graner and Glazier, 1992) to simulate the movement of one or several cells on the substrate. The model is based on the minimization of the effective energy H, which is a function of the cell shape and areas of contact between adjacent cells and between cells and substrate. It is computationally efficient to study the multiple 3D cells with enough resolution. The model also allows adding protrusive and retractive forces to the cells (Rens and Edelstein-Keshet, 2019; Li and Lowengrub, 2014; Szabó and Merks, 2013).

In the CPM, the space is divided into pixels (in the model, the cell size is about $10∗10∗10$ pixels), and each pixel $i$ is assigned a spin $\sigma_{i}$ . The spin is effectively an index that identifies which cell the pixel belongs to. A stochastic modified Metropolis algorithm (Cipra, 2018) was used to determine how the spin $\sigma$ changes. At each step, the algorithm randomly selects a target site, $i$, and a neighboring source site $j$. If they belong to different cells, or to a cell and neighboring environment, the algorithm sets $\sigma_{i}=\sigma_{j}$ with probability, $P_{\sigma_{i}→\sigma_{j}}$ , which is determined by the Boltzmann acceptance function:

$$
P_{\sigma_{i}→\sigma_{j}}={1,  ΔH\leq0 e^{-\frac{ΔH}{T}},  ΔH§amp;gt;0
$$

where $ΔH$ is the change of the effective energy caused by this change of spin, and $T$ is an effective temperature parameter describing the amplitude of stochastic fluctuations of the cell boundary (Swat, 2012). We use $T=10$ for all the simulations in this paper. The key part of any specific CPM is the effective energy $H$. In our model, we define $H$ as

$$
H=\sum_{\sigma}^{}\lambda_{\sigma}v_{\sigma}-V_{\sigma}^{2}+\sum_{\sigma}^{}κ_{\sigma}a_{\sigma}^{2}     +\sum_{\sigma_{1},\sigma_{2}}^{}J_{\sigma_{1}\sigma_{2}}S_{\sigma_{1}\sigma_{2}}+\sum_{i}^{}(W_{\sigma_{i},p} r→_{i}+W_{\sigma_{i},r} r→_{i}),
$$

Here, the first and the second terms represent the effects of the volume conservation and cell surface (cortex) contraction, respectively. Alternatively, the first term can be thought of as the effect of the hydrostatic pressure of the cytoplasm, and the second term – as the effect of the cell cortex tension. The third term represents the adhesion energy between the neighboring cells and between the cells and the ECM (also called substrate or ECM below). The last term is the effective potential energy related to the protrusive and retractive forces (with subscript $p$ and $r$, respectively). $i$ is the pixel’s index, and $\sigma$ is the cell’s or environment’s spin. Variables $v_{ \sigma}$ and $a_{\sigma}$ are the volume and surface area of the cell $\sigma$, and $V_{\sigma}$ is its target volume. Unlike in some variants of the CPM, we keep the target surface area equal to zero, so effectively the cortex is contractile for any area. The target volume is a parameter that we take to be equal to the volume of the cube of the characteristic cell size. Parameters $\lambda$ and $κ$ are the coefficients determining how tightly the volume is conserved and how great the cortex tension is, respectively. Parameter $J_{\sigma_{1}\sigma_{2}}$ is the adhesion energy per unit area of the boundary between cells $\sigma_{1}$ and $\sigma_{2}$ (or between cell and ECM). Variable $S_{\sigma_{1}\sigma_{2}}$ is the area of the boundary between cells or between one cell and the ECM. Essentially, the model’s first two terms tend to minimize the cell’s area while keeping its volume constant shaping the cell into a sphere. Adhesion terms, however, try to maximize the boundary areas, flattening the cells. The competition between these terms makes individual cell look like a dome on the substrate (this is how we choose relative strengths of the cortex tension and characteristic adhesion), and two cells – like two domes pressed into each other side-by-side. To make the cells move, we must add the forces pushing the cell front and pulling its rear. Note that those forces originate from the cytoskeleton inside the cells, and not in the environment surrounding the cells, so the force balances are implied. Specifically, the force of protrusion that pushes on the cell leading surface forward from inside is balanced by a reactive cytoskeletal pushing directed to the rear and applied to the firm adhesions between the ventral surface of the cell and ECM. Similarly, the force of retraction that pulls the cell rear forward from inside is also balanced by a reactive cytoskeletal pulling directed to the rear and applied to the firm adhesions between the ventral surface of the cell and ECM.

We introduce these forces through effective potential energies as follows. First, we define a polarity for each cell, which is quantified using the angle between the polarization direction and the positive-x direction, $\phi$, as shown in Figure 4A. Then, the respective potential energies can be defined as

$$
W_{p}r→=-Θ\alpha_{p}-\alpha-\phi|r→-r→_{COM}|Pro\alpha-\phi
$$



$$
W_{r}r→=Θ\alpha-\phi-\alpha_{r}|r→-r→_{COM}|Ret
$$

Here, $Θ$ is the Heaviside step function (equal to 1/0 for positive/negative values of argument, respectively). $r→=(x,y,z)$ is the 3D position of a specific pixel. $\alpha$ is the angle of vector $(x-x_{COM},y-y_{COM})$, in which $(x,y)$ is the position of 2D projection of a specific pixel onto the x-y-plane, and $(x_{COM},y_{COM})$ is the 2D position of the centroid of the cell. $\phi$ is the polarity angle mentioned above $. \alpha_{p}$ and $\alpha_{r}$ are the angular ranges of the protrusive and retractive forces, respectively. For example, if the protrusive force exists in the front half of the cell and the retractive force exists in the back half of the cell, then the angles are, $\alpha_{p}=\frac{\pi}{2}$ , $\alpha_{r}=\frac{3\pi}{2}. |r→-r→_{COM}|$ is the 3D distance between a specific pixel and the centroid of the cell and taking a gradient of it, results in the centripetal retractive and centrifugal protrusive forces. $Pro(\alpha-\phi)$ and $Ret$ define the amplitudes of the energy terms that are also strengths of the protrusive and retractive forces, respectively. $Ret$ is a constant parameter, while $Pro$ is constant in some simulations but is a function of angle ($\alpha-\phi$) in others. Their values, as well as the values for $\alpha_{p}$ and $\alpha_{r}$ , and for all other model parameters, are listed in Appendix 1—table 1.

When investigating directionality and persistence of the cells’ trajectories, stochasticity is introduced to the polarity’s dynamics as follows:

$$
d\phi=-\omega_{1}\phi dt-\omega_{2}(\phi-\theta)+\sigma dW_{t}
$$

where $\theta$ is the angle shown in Figure 3B and $dW_{t}$ denotes a Wiener process (stochastic directional noise). The first term shows the tendency of the polarity to align with the external signal’s direction (the positive-x direction), and the second term shows the tendency to follow the other cell. For different polarization modes, $\omega_{1}$ and $\omega_{2}$ take different values. More specifically, for the independent mode and the faster-slower mode shown in Figure 3B (when the cells follow the environmental directional guidance independently), $\omega_{1}\neq0, \omega_{2}=0$ for both cells, while for the leader-trailer mode (when the trailing cell follows the leader instead of following the environmental guidance), $\omega_{1}\neq0, \omega_{2}=0$ for the leader and $\omega_{1}=0, \omega_{2}\neq0$ for the trailer.

It is worth mentioning that the exact absolute values of parameters in the energy function are not important as the dynamics of the system is determined by the ratio $\frac{ΔH}{T}$ in which $T$ is a ‘temperature’ parameter without direct relation to the biological processes, and the ‘Monte Carlo step’ in the simulation is not directly related to an actual time scale. So, we only check whether the ratios of the model parameters are consistent with the experimentally estimated orders of magnitude of the biophysical parameters. Experimental estimates of the force generated over $1\mum$ of the lamellipodial leading edge are $~1000pN$ and the total traction force exerted by the cell is $~10^{4}-10^{5}pN$ (Gline et al., 2015 ; Mogilner and Oster, 2003). As the leading edge of the lamellipodia is only $~0.1-0.2\mum$ thick, while in our model we cannot generate very thin protrusions, we distribute the total forces generated by the lamellipodia almost uniformly to the whole front of the cell and use the protrusive force density $~100pN/\mum^{2}$ assuming the height of the cell is $~10\mum$ (Figure 1A). Similarly, we distribute the total traction force uniformly to the back of the cell resulting in the retractive force density $~10^{2}-10^{3} pN/\mum^{2}$ . Thus, the orders of magnitude of the protrusive and retractive forces are close, and we keep them close in the model. The energy of adhesion between the cell and the substrate is estimated as follows. Each integrin attachment complex has a force $~10-30pN$ (Ananthakrishnan and Ehrlicher, 2007) associated with it. The size of an integrin-based adhesion complexes formed at cell contacts with the ECM is $~1 \mum^{2}$ (Geiger et al., 2001), so we estimate the adhesion force densities as $~10-30 pN/\mum^{2}$ . Then, the ratio between the active forces and the adhesion forces is ˜10. In our model, the force strength parameters, $Pro\alpha-\phi$ and $Ret$, are on the order of 10–100 in dimensionless units, and the adhesion strength parameter $J$ ranges from 0 to 20 in dimensionless units, which is consistent with the force ratios from the experimental measurements.

After the orders of magnitude of the protrusion, retraction and adhesion energies are chosen as described, the rest of the principal model parameters are chosen following the following logic. The cortex contractility parameter $κ$ is chosen so that an individual non-motile cell has a shape close to that of a hemisphere; if this parameter is too small, the cell becomes a ‘pancake’; if too large – a ‘ball.’ The parameter regulating the tightness of the cell volume control, $\lambda$ , is fine-tuned to avoid (1) freezing the cell shape – when this parameter has a value that is too great, most fluctuations of the cell shape get arrested, and (2) loosening the cell shape too much – when this parameter has a value that is too small, cell transiently becomes too small or too large that disagrees with the observations. The values of the parameters for the stochastic directionality experiment are chosen so that the persistence of the single cell predicted trajectories fit that of the observed trajectories. Finally, note that the parameters for the adhesion strength (J) are scaled as follows. We make this parameter a large positive number for the boundary between the two motile cells and endoderm (or for cell-free space boundary in simulations without endoderm); this corresponds to the ‘no adhesion’ regime. Then, the adhesion parameters for cell-cell and cell-ECM boundaries are smaller positive numbers. Thus, the energy in the system decreases when the relative areas of the cell-cell and cell-ECM boundaries increases, so those are the adhesive surfaces.

Note that the dynamics of the simulated cell is determined by the probability function of spin changes, which is defined by the exponential function with a cutoff at 1. This leads to a speed-force relation of an exponential form when the force is too small and is saturated when the force is too large. We avoid this artifact because the parameters we choose restrict our simulations to the regime where the speed-force relation is approximately linear.

Simulations were done using software CompuCell3D 3.7.8 (Swat, 2012). In Appendix 1 tables, we list all model parameters that are varied between different simulations, and in the Supporting information we explain the reasons for the variance. When we simulate the actively migrating cells in the presence of the endoderm that mechanically resists the deformations, we make the endodermal cells mechanically more passive than the migrating cells (their contractile tension is half that of the migrating cells) and vary the endodermal ‘tightness of the volume conservation’ parameter $\lambda$ a few fold less and greater than that of the migrating cells, respectively.
