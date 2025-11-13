# Collective forces of tumor spheroids in three-dimensional biopolymer networks

## Authors

- Christoph Mark<sup>1</sup> ([ORCID: 0000-0002-8612-6469](https://orcid.org/0000-0002-8612-6469)) †
- Thomas J Grundy<sup>2</sup>
- Pamela L Strissel<sup>4</sup>
- David Böhringer<sup>1</sup>
- Nadine Grummel<sup>1</sup>
- Richard Gerum<sup>1</sup>
- Julian Steinwachs<sup>1</sup>
- Carolin C Hack<sup>4</sup>
- Matthias W Beckmann<sup>4</sup>
- Markus Eckstein<sup>5</sup>
- Reiner Strick<sup>4</sup>
- Geraldine M O'Neill<sup>2</sup>
- Ben Fabry<sup>1</sup> †

### Affiliations

1. Department of Physics, Friedrich-Alexander University Erlangen-Nürnberg Erlangen Germany
2. Children's Cancer Research Unit, The Children's Hospital at Westmead Sydney Australia
3. School of Medical Sciences and Children’s Hospital at Westmead Clinical School, University of Sydney Sydney Australia
4. Department of Gynecology and Obstetrics, Laboratory for Molecular Medicine, University Hospital Erlangen, Friedrich-Alexander University Erlangen-Nürnberg Erlangen Germany
5. Institute of Pathology, University Hospital Erlangen Erlangen Germany

† Corresponding author

## Abstract

We describe a method for quantifying the contractile forces that tumor spheroids collectively exert on highly nonlinear three-dimensional collagen networks. While three-dimensional traction force microscopy for single cells in a nonlinear matrix is computationally complex due to the variable cell shape, here we exploit the spherical symmetry of tumor spheroids to derive a scale-invariant relationship between spheroid contractility and the surrounding matrix deformations. This relationship allows us to directly translate the magnitude of matrix deformations to the total contractility of arbitrarily sized spheroids. We show that our method is accurate up to strains of 50% and remains valid even for irregularly shaped tissue samples when considering only the deformations in the far field. Finally, we demonstrate that collective forces of tumor spheroids reflect the contractility of individual cells for up to 1 hr after seeding, while collective forces on longer timescales are guided by mechanical feedback from the extracellular matrix.

## Introduction

In the process of tumor invasion, cancer cells leave the primary tumor either individually or collectively (Friedl and Wolf, 2003). This process requires that cells exert physical forces onto the surrounding extracellular matrix (Friedl and Gilmour, 2009; Koch et al., 2012). As cellular force generation and cell-matrix interactions are increasingly recognized as potential therapeutic targets against cancer cell invasion and metastasis (Holle et al., 2018; Chaudhuri et al., 2018), there is a need to quantify the forces that are collectively exerted by invading cancer cells under physiologically relevant conditions. In this work, we introduce a computationally and experimentally simple and reliable method that captures collective effects in tissue remodeling and thus facilitates screenings of potential force-targeting agents.

Numerous biophysical assays have been developed to quantify the traction forces of single cancer cells by measuring the deformations that a cell induces in linear elastic substrates (2D and 3D) with known stiffness (Dembo and Wang, 1999; Butler et al., 2002; Legant et al., 2010). This technique has since been extended to multicellular systems to study collective cell guidance by intercellular stresses in 2D cell monolayers (Tambe et al., 2011; Trepat et al., 2009). Likewise, intercellular stresses within 3D multicellular aggregates (so-called spheroids) have been studied by quantifying the deformation of small elastic beads that are embedded in the spheroids (Dolega et al., 2017).

All methods referenced above are based on linear elastic materials that exhibit a constant stiffness, independent of strain, so that the measured deformation is proportional to the corresponding force. To mimic the physiological condition of cells invading connective tissue in vitro, however, cells are typically cultured in non-linear biopolymer networks such as reconstituted collagen that stiffen significantly when extended (Storm et al., 2005; Münster et al., 2013) but soften when compressed (Steinwachs et al., 2016; Münster et al., 2013). Considering these nonlinear material properties in a finite element approach allows for the quantification of the total contractility (Hall et al., 2016) and the reconstruction of the three-dimensional traction force field around individual cells in a biopolymer network (Steinwachs et al., 2016).

Multicellular tumor spheroids embedded in collagen gels are - depending on cell type - able to contract the collagen fiber network, thereby exerting tensile forces in the matrix that in turn realign fiber bundles and facilitate cell invasion into the matrix (Kopanska et al., 2016; Kopanska et al., 2015; Chen et al., 2019; Han et al., 2016; Lee et al., 2017; Kaufman et al., 2005; Carey et al., 2013). Thus, multicellular tumor spheroids not only replicate the main structural and functional properties of solid tumors (Nunes et al., 2019), but can further serve as a model system for the mechanics of cancer invasion, including collective cellular force generation and tissue remodeling. However, current studies on the force generation of multicellular spheroids all use matrix deformation as a proxy for contractility, to avoid the complex problem of force reconstruction in non-linear materials (Kopanska et al., 2016; Chen et al., 2019; Valencia et al., 2015). This approach poses no problem when comparing spheroids of similar size and cell number. However, in the case of differently sized or differently dense spheroids, or for comparing the collective contractility of a spheroid to that of an individual cell, a more direct measurement in units of force rather than deformation is needed.

Force measurement on a spheroid poses two formidable problems. First, current 3D finite element force reconstruction methods that have been designed for single cells in a non-linear material such as collagen are computationally too slow for analyzing large (∼0.5 mm) tumor spheroids (Steinwachs et al., 2016). Second, measurements typically require a confocal microscope equipped with a high-resolution (NA 1.0 or higher) water dip-in long working distance objective to image the three-dimensional structure of the collagen fiber network using reflection microscopy (Steinwachs et al., 2016). The large scanning volume and associated scanning time would be prohibitive in the case of spheroids.

To overcome these technical challenges, we forgo subcellular force resolution and exploit the approximately spherical symmetry of tumor spheroids. Accordingly, it is sufficient to measure the far-field deformations of the surrounding collagen matrix from a single slice through the equatorial plane of the spheroid, thereby eliminating the need for high-resolution 3D imaging. To quantify matrix deformations over time, image acquisition can be performed with low resolution (4x-10x objective, NA 0.1) brightfield microscopy of micron-sized fiducial markers embedded in the collagen gel.

To relate the measured deformation field surrounding a spheroid to physical forces generated by the cells, we replicate the experiment in silico. Specifically, we simulate a contracting sphere within a bulk of collagen, which can be described by a non-linear material model that takes into account fiber buckling and strain stiffening. We apply this method to spheroids made from glioblastoma cell lines and primary breast cancer cells, as well as to patient-derived breast tumor tissue samples (so-called tumoroids).

## Results

### Collagen contractility assay

We use two model systems to investigate the mechanics of tumor invasion: First, we use in vitro grown tumor spheroids that are generated by culturing suspended cells in non-adhesive U-shaped wells (Figure 1a). Second, we use patient-derived tumor tissue samples (tumoroids) with a size of 200–600 µm, similar to the size of the tumor spheroids in our study. Both spheroids and tumoroids are embedded in a 3D collagen matrix by suspending them in an un-polymerized solution of collagen with 1 µm fiducial marker beads (Figure 1b,c). After the collagen has polymerized, we track the ongoing cell force-induced deformations of the collagen matrix from brightfield time-lapse images (taken every 5–10 min) using particle image velocimetry (Taylor et al., 2010; Figure 1—figure supplements 1 and 2; Video 1). In general, we find that both spheroids and tumoroids induce an approximately radially symmetric, inward-directed deformation field with monotonically increasing absolute deformations over time (Figure 1d–g; Videos 2, 3, 4), in line with a previous report on CT26 colon carcinoma cells (Kopanska et al., 2016). Cells within the spheroids can proliferate after being embedded in the collagen matrix (Figure 1—figure supplement 3). This may lead to spheroid growth and induce a compression of the surrounding matrix (and thus an outward-directed deformation field). However, in none of the spheroids or cell types investigated in this work have we observed such outward-directed matrix deformations.

![Figure 1.](https://cdn.elifesciences.org/articles/51912/elife-51912-fig1-v1.jpg)

**Figure 1.:** (a) Spheroid generation process within non-adhesive U-shaped wells. (b) Spheroid embedding process in collagen gels. The spheroids are suspended in a collagen solution and subsequently pipetted onto a pre-poured layer of collagen (indicated by the dashed line). (c) Exemplary brightfield image of the equatorial plane of a U87 spheroid containing 7,500 cells. The inset shows the edge of the tumor spheroid and the micron-sized fiducial markers (arrows) that are added to the collagen solution. (d-g) Deformation field obtained by particle image velocimetry, 3 h, 6 h, 9 h and 12 h after the collagen gel has polymerized. The spheroid outline is determined by image segmentation and indicated by the red line.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/51912/elife-51912-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Contractile pressure of a spheroid generated from 4000 primary Luminal B breast cancer cells versus time after collagen gel polymerization has been initiated (by increasing the pH of the collagen solution to 10). The orange line indicates the contractile pressure as measured in a regular experiment that starts 60 min after the gel polymerization has been initiated. This waiting time ensures that gel polymerization is complete. As the spheroid may start to contract the surrounding matrix earlier (resulting in displacements that we do not capture in our measurement), our method generally underestimates the spheroid contractility. In an exemplary experiment, we started to record time lapse images of a spheroid using confocal reflection microscopy as soon as the collagen fibers became visible in the reflection channel (30 min after the pH of the collagen solution was increased to 10). From the collagen fiber displacements over the following 30 min of the experiment (60 min after initiation of polymerization), we find a contractile pressure (blue line) of 11 Pa. Given that these spheroids typically reach a contractile pressure of several hundred Pa within 24 h, this systematic error from neglecting the fiber displacements during the first 60 min is small. See also Video 1.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/51912/elife-51912-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (a) Estimated mean pressure value (left) and the corresponding standard error (right) of an exemplary U87 spheroid, 3 h after the experiment started, as a function of the window size and the signal-to-noise threshold used in the PIV-analysis. (b) Mean estimated pressure as a function of the window size, for a signal-to-noise threshold of 1.0, that is without any filtering of the estimated deformations. (c) The 99th percentile of all measured absolute displacements during the first two hours of the experiment, $D_{max}$, for all individual spheroids. The dashed red line represents the upper boundary of $D_{max}$ for a window size of 40 px, according to the one-quarter-rule. The dot-dashed line and the dotted line correspond to the upper boundary for a window size of 30 px and 50 px, respectively.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/51912/elife-51912-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (a) Standard curve for cell number quantification (blue), showing the amount of DNA extracted from different numbers (2000, 4000, 16000, 32000) of U87 glioblastoma cells (n = 3 repeats). We find a linear relationship ($R^{2}=0.997$) between the number of cells and the amount of DNA. The best fit linear function is displayed in orange. (b) U87 glioblastoma cell count at the start of the 24 h spheroid cultivation period within non-adhesive wells ($t=0⁢h$; we use 7500 cells per spheroid), after 24 h of cultivation ($t=24⁢h$; estimated from DNA quantification), and after another 24 h embedded in collagen ($t=48⁢h$; estimated from DNA quantification). We find that during the 24 h cultivation period in non-adhesive wells, the cell count increases by 31%. Within the 24 h period in the collagen matrix, the cell count increases by another 104%. Error bars denote 1 se.

![Video 1.](https://cdn.elifesciences.org/articles/51912/elife-51912-video1.mp4.jpg)

**Video 1.:** Left: Series of confocal reflection microscopy images of collagen fibers at the equatorial plane around a Luminal B breast cancer spheroid embedded in 1.2 mg/ml collagen gel. Time is indicated on the top left and measures time after initiation of collagen polymerization (by increasing the pH of the collagen solution to 10). The video starts once collagen fibers are becoming visible in the reflection channel (∼30 min after initiation of polymerization). The default starting point of a traction force experiment is 60 min after polymerization started. Right: Measured deformation field surrounding the embedded spheroid as indicated by the color-coded arrows. The confocal reflection microscopy images are shown in gray-scale in the background. See Figure 1—figure supplement 1 for a quantitative evaluation of this image series.

![Video 2.](https://cdn.elifesciences.org/articles/51912/elife-51912-video2.mp4.jpg)

**Video 2.:** Time is indicated in the upper-left corner (HH:MM:SS).

![Video 3.](https://cdn.elifesciences.org/articles/51912/elife-51912-video3.mp4.jpg)

**Video 3.:** Time is indicated in the upper-left corner (HH:MM:SS).

![Video 4.](https://cdn.elifesciences.org/articles/51912/elife-51912-video4.mp4.jpg)

**Video 4.:** Time is indicated in the upper-left corner (HH:MM:SS).

### Scale-invariant relation between deformation and contractility

To relate the measured deformation field surrounding a spheroid to physical forces generated by the cells, we use the finite element approach described in Steinwachs et al. (2016). Specifically, we simulate a small spherical inclusion with a negative hydrostatic pressure (that emulates contracting cells within the inclusion) within a large surrounding volume of collagen (Figure 2a,b). This computational analysis predicts that the absolute deformations of the collagen $u⁢(r)$ are largest directly at the boundary of the inclusion and fall off with increasing distance $r$ from the center, depending on the pressure (Figure 2b). For a given pressure, the absolute deformations increase with the radius $r_{0}$ of the inclusion. Importantly, when normalized by the radius of the inclusion $r_{0}$, the deformations $u/r_{0}$ collapse onto a single curve when plotted against the normalized distance $r/r_{0}$ (Figure 2c). This implies that the shape of the simulated deformation field only depends on the pressure but not on the size of the inclusion (i.e. on the spheroid radius $r_{0}$ at the time of seeding).

![Figure 2.](https://cdn.elifesciences.org/articles/51912/elife-51912-fig2-v1.jpg)

**Figure 2.:** (a) Illustration of the tetrahedral mesh used for the material simulation. The spherical volume has a radius of 2 cm, with a spherical inclusion in the center. (b) Enlarged section of the tetrahedral mesh around the spherical inclusion with a radius of $r_{0}$ = 100 µm. c: Simulated absolute deformations $u⁢(r→)$ as a function of the distance $r=|r→|$ from the center of the volume, for an inward-directed pressure of 100 Pa acting on the surface of the inclusion. Different colors indicate different radii $r_{0}$ of the spherical inclusion. d: Same as in (c), but with deformations and distances normalized by $r_{0}$. For a given inbound pressure, all curves collapse onto a single relationship.

### Deformation fields in non-linear biopolymer networks

The collapse of the normalized deformation versus distance relationship furthermore implies that we can estimate the contractile pressure (contractile force per surface area) of a tumor spheroid of arbitrary size from a look-up table. To create this look-up table, we perform 150 simulations with pressures ranging from 0.1 Pa to 10,000 Pa. The simulated deformation fields are normalized by $r_{0}$, binned and interpolated to obtain smooth deformation curves (Figure 3b). For a low pressure of ∼1 Pa, the deformation field as a function of radial distance from the spheroid center falls off with increasing distance according to a power law with an exponent (=slope in a double logarithmic plot) of $\alpha=-2$, as expected for a linear elastic material. With increasing pressure, however, the deformations near the spheroid surface fall off more slowly, with a slope approaching values around $\alpha=-0.2$ for high pressure values > 1000 Pa (Figure 3—figure supplement 1), indicating long-range force transmission due to a stiffening of the collagen fibers. This is in line with reported theoretical models (Xu and Safran, 2015; Grimmer and Notbohm, 2018 and experimental findings (Burkel and Notbohm, 2017; Han et al., 2018).

To evaluate whether measured deformation fields match the predictions from simulation for different strains, we compare simulated and measured matrix deformations around a spheroid grown from 4000 primary triple-negative breast cancer cells over the course of 24 hr after embedding. To avoid tracking artifacts due to invading cells in the direct vicinity of the spheroid, we only use deformations that occur more than two radii away from the spheroid center. We find that triple-negative breast cancer cells deform the collagen matrix by ∼200 µm (corresponding to a strain of over 50%; Video 4) near the spheroid surface after 24 hr of measurement time, resulting in a contractile pressure of 677 ± 68 Pa (median ± st.dev.) and a total contractility (pressure × surface area) of 344 ± 35 µN (median ± st.dev.; Figure 3a,b). At these high strains, collagen may experience plastic deformations and structural changes in addition to purely elastic deformations (Kim et al., 2017). Even though our material model only accounts for elastic deformations, we find excellent agreement between measured and simulated deformation fields (Figure 3b). Importantly, the simulations accurately capture the progressing flattening of the deformation field (deformation versus distance curves) due to strain stiffening of the matrix, which can exceed a 20-fold increase over the linear stiffness of collagen close to the surface of triple-negative breast cancer spheroids (Video 5).

![Figure 3.](https://cdn.elifesciences.org/articles/51912/elife-51912-fig3-v1.jpg)

**Figure 3.:** (a) Brightfield image of a tumor spheroid grown from 4000 primary, triple-negative breast cancer cells, 24 hr after embedding in a 3D collagen gel together with fiducial markers. The initial shape of the spheroid at the beginning of the experiment is indicated by the red shading. Red circles show the trajectory of exemplary fiducial markers over the course of 24 hr measurement time to illustrate the material strain arising within the matrix due to the contractile force of the spheroid. b: Normalized deformations as a function of the normalized distance for material simulations of varying pressure (color coding). Each red marker corresponds to the normalized deformation within an individual image tile analyzed with particle image velocimetry, after 24 hr measurement time. White circles indicate averaged normalized deformations for different time points during the measurement (times and inferred pressure values are noted below each curve). Dashed black lines indicate the corresponding best-fit simulated deformation field.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/51912/elife-51912-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Normalized absolute deformations as a function of the normalized distance, for material simulations with an inbound pressure on the surface of a spherical inclusion ranging from 0.1 Pa to 1000 Pa. The inset shows the power-law exponent $\alpha$ of the deformation field as a function of the inbound pressure (for the near field, $r/r_{0}<2$), illustrating the long-range force transmission in collagen due to strain stiffening.

![Video 5.](https://cdn.elifesciences.org/articles/51912/elife-51912-video5.mp4.jpg)

**Video 5.:** Left: Time-lapse brightfield images of a spheroid generated from 4000 primary triple-negative breast cancer cells embedded in a collagen gel over the time course of 24 h. Time is indicated in the upper-left corner (HH:MM:SS). Right: Local stiffness map of the collagen matrix surrounding the spheroid. Stiffness is displayed on a logarithmic scale and calculated in radial direction relative to the spheroid center. At zero strain, the 1.2 mg/ml collagen gel has a stiffness of 316 Pa. After 24 h measurement time, the maximum local stiffness is 7585 Pa.

### Far-field approximation for non-spherical objects

While spheroids are typically created from only one or two cell types, real tumors are more heterogeneous and contain tumor-generated matrix components as well as a mixture of epithelial and mesenchymal tumor cells that may split into subpopulations with different gene expression levels and gene mutations (Shipitsin et al., 2007). To investigate the interplay of different cell types and matrix components, we extract and isolate small samples from a patient-derived tumor and embed them in a collagen matrix. Due to the preparation process and their inherent heterogeneity, however, these tumoroids generally do not attain a high circularity in culture, but rather have a more elliptical, sometimes irregular shape.

To test whether our method is applicable to non-spherical contracting tissue samples, we apply the collagen contractility assay to tumoroids obtained from a Luminal B breast cancer patient (Figure 4a–c). We find that the tumoroids remain viable within the collagen gel for over 24 h and generate a median contractility of 24.5 µN (with a median effective radius of 149 µm; n = 14; Video 6). We find that for highly elongated tumoroids (Figure 4a), the material simulations overestimate the matrix deformations in the near-field ($r/r_{0}≲4$), due to the oversimplified assumption of spherical geometry (Figure 4d). This may result in local deviations of the inferred pressure of up to 20% close to the spheroid (Figure 4g). Importantly, however, the simulated far-field deformations are still in good agreement with the measured deformations, irrespective of the pronounced eccentricity of the tumoroid (Figure 4d,g). For small tumoroids that only exert small absolute displacements in the matrix (Figure 4b), we sporadically find local deviations in the inferred pressure of up to 20% at the outer rim of the field of view where the matrix deformations approach the resolution limit of the PIV algorithm (Figure 4e,h). Such outliers however do not significantly influence the inferred median pressure that takes into account the complete displacement field. For larger tumoroids with a more circular shape (Figure 4c), the local deviations from the inferred pressure are generally $≲5%$.

![Figure 4.](https://cdn.elifesciences.org/articles/51912/elife-51912-fig4-v1.jpg)

**Figure 4.:** (a-c) Brightfield images of three exemplary tumoroids embedded in a 3D collagen matrix, together with fiducial markers. (d-f) Normalized averaged measured matrix deformations (white circles) of the corresponding tumoroids (a–c) for three time points (1 h, 6 h, and 24 h) after the beginning of the experiment. The dashed lines indicate the corresponding best-fit deformation field from the material simulations. The color-coded background indicates simulated deformations for a range of pressures. g-i: Local relative deviation of the inferred pressure from the best-fit pressure value. Larger values indicate that the measured displacement field deviates stronger from the simulated displacement field.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/51912/elife-51912-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** While we assume spherical geometry of the deformations in the matrix surrounding a spheroid or tumoroid, the measured deformation fields can show deviations from spherical symmetry (see e.g. Figure 1d–g). We evaluate the variations in the reconstructed contractile pressure due to an asymmetric deformation field by subdividing the deformation field around spheroids and tumoroids into narrow 5° angular segments. We then compute the contractile pressure for each segment for a set of Luminal B breast cancer spheroids (n = 5) and Luminal B breast cancer tumoroids (n = 14) after 12 h measurement time. a: In the case of spheroids, the directional heterogeneity of the deformation field results in a directional variability (coefficient of variation, mean/st.dev.) for 5° angular segments of 7% on average. For comparison, the variability between individual spheroids is 6%. b: Despite the very large directional heterogeneity of the deformation field around the usually non-spherical tumoroids, we find that the resulting directional variability (coefficient of variation, mean/st.dev.) in contractile pressure is only 16% on average, compared to 52% variability between individual tumoroids. Thus, the pronounced asymmetry in the deformation field around some spheroids and most tumoroids does not lead to substantial errors.

![Video 6.](https://cdn.elifesciences.org/articles/51912/elife-51912-video6.mp4.jpg)

**Video 6.:** Time is indicated in the upper-left corner (HH:MM:SS).

As highly asymmetric tumoroids (and some spheroids) create asymmetric deformation fields in the surrounding matrix (and thereby an asymmetric stiffening of the matrix; Video 7), we further evaluate the directional contractile pressure by subdividing the deformation field around spheroids and tumoroids into narrow 5° angular segments. We find that the directional variability of the contractile pressure is equal to or smaller than the variability between individual tumoroids or spheroids (Figure 4—figure supplement 1, Videos 8, 9, 10, 11). Thus, our method is applicable to non-spherical samples if we only consider the far-field deformations for force reconstruction.

![Video 7.](https://cdn.elifesciences.org/articles/51912/elife-51912-video7.mp4.jpg)

**Video 7.:** Left: Time-lapse brightfield images of a Luminal B tumoroid embedded in a collagen gel over the time course of 24 h. Time is indicated in the upper-left corner (HH:MM:SS). Right: Local stiffness map of the collagen matrix surrounding the tumoroid. Stiffness is displayed on a linear scale and calculated in radial direction relative to the spheroid center. At zero strain, the 1.2 mg/ml collagen gel has a stiffness of 316 Pa. After 24 h measurement time, the maximum local stiffness is 516 Pa.

![Video 8.](https://cdn.elifesciences.org/articles/51912/elife-51912-video8.mp4.jpg)

**Video 8.:** Left: Angular dependence of contractile pressure of the glioblastoma spheroid shown in Figure 1 d–g. Each point represents the reconstructed contractile pressure from a 5°-segment of the deformation field surrounding the spheroid. The coefficient of variation is defined as mean/st.dev. and denotes the variation of the reconstructed contractile pressure between different directions. Right: Time-lapse images of the equatorial plane of the spheroid. Matrix deformations are shown as arrows, the initial spheroid outline is indicated in red. Images are synchronized to the pressure values shown on the left.

![Video 9.](https://cdn.elifesciences.org/articles/51912/elife-51912-video9.mp4.jpg)

**Video 9.:** Left: Angular dependence of contractile pressure of an exemplary Luminal B breast cancer spheroid. Each point represents the reconstructed contractile pressure from a 5°-segment of the deformation field surrounding the spheroid. The coefficient of variation is defined as mean/st.dev. and denotes the variation of the reconstructed contractile pressure between different directions. Right: Time-lapse images of the equatorial plane of the spheroid. Matrix deformations are shown as arrows, the initial spheroid outline is indicated in red. Images are synchronized to the pressure values shown on the left.

![Video 10.](https://cdn.elifesciences.org/articles/51912/elife-51912-video10.mp4.jpg)

**Video 10.:** Left: Angular dependence of contractile pressure of an exemplary Luminal B tumoroid. Each point represents the reconstructed contractile pressure from a 5°-segment of the deformation field surrounding the tumoroid. The coefficient of variation is defined as mean/st.dev. and denotes the variation of the reconstructed contractile pressure between different directions. Right: Time-lapse images of the equatorial plane of the tumoroid. Matrix deformations are shown as arrows, the initial spheroid outline is indicated in red. Images are synchronized to the pressure values shown on the left.

![Video 11.](https://cdn.elifesciences.org/articles/51912/elife-51912-video11.mp4.jpg)

**Video 11.:** Each point represents the reconstructed contractile pressure from a 5°-segment of the deformation field surrounding the spheroid/tumoroid.

### Mechanical feedback guides collective force generation

We next apply the collagen contractility assay to two glioblastoma cell lines, A172 (15,000 cells per spheroid) and U87 (7,500 cells per spheroid, to match the size of A172 spheroids; Figure 5—figure supplements 1 and 2) as little is known about the traction forces exerted by glioblastoma cells during the invasion of brain tissue. Although collagen is present in only small amounts in the normal human brain, glioblastoma cells readily bind to collagen (Payne and Huang, 2013). Recent studies have shown that fibrillar collagens are an integral part of the locally produced extracellular matrix in glioblastomas (Huijbers et al., 2010; Pointer et al., 2017). Furthermore, collagen is found in the basement membrane surrounding blood vessels, which are a major route of glioblastoma invasion (Payne and Huang, 2013; Cuddapah et al., 2014). Reconstituted collagen gels display a Young’s modulus of 162 ± 25 Pa (Steinwachs et al., 2016) in the linear regime, closely emulating the soft environment of the brain tissue (100–1000 Pa Levental et al., 2007).

To investigate the role of collective effects in cellular force generation, we compare the contractility exerted by individual glioblastoma cells to the contractility of tumor spheroids generated from the respective cell lines. We apply single-cell 3D traction force microscopy as described in Steinwachs et al. (2016). Specifially, we reconstruct the forces exerted by the cells on the collagen gel from the surrounding deformation field (Figure 5a,b). By summing up all force components that point toward the force epicenter, we obtain the total contractility. We find that individual A172 cells are nearly 2-fold stronger compared to U87 cells (91 nN vs. 51 nN; Figure 5c).

![Figure 5.](https://cdn.elifesciences.org/articles/51912/elife-51912-fig5-v1.jpg)

**Figure 5.:** (a) Matrix deformations exerted by an exemplary A172 cell (inset) embedded in a 3D collagen gel. (b) Reconstructed force density field surrounding the A172 cell shown in (a). (c) Median cell contractility as measured by single-cell 3D traction force microscopy (A172: n = 90; U87: n = 86). (d) Mean collective cell contractility of tumor spheroids after 30 min measurement time (A172: n = 17; U87: n = 13). e: Mean collective cell contractility of tumor spheroids after 12 h measurement time (A172: n = 17; U87: n = 13). f: Time course of the mean contractility and corresponding standard error (shaded) for A172 (blue) and U87 (green) spheroids. The 2 h-resting period of the A172 spheroids is marked in red. Error bars denote 1 standard error.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/51912/elife-51912-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (a) Spheroid diameter for A172 containing 15,000 cells at the time of seeding (n = 16) and U87 spheroids with 7,500 cells (n = 17) and with 15,000 cells (n = 15). (b) Spheroid roundness measured as $4⋅Area/(\pi⋅MajorAxis^{2})$. Error bars denote 1 st.dev.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/51912/elife-51912-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (a) Estimated pressure (blue lines) and corresponding standard error (blue shading) of individual A172 tumor spheroids containing 15,000 cells as a function of time, for four separate experiments (left to right). (b) Same as in (a), for three experiments with U87 tumor spheroids containing 15,000 cells. (c) Same as in (a), for three experiments with U87 tumor spheroids containing 7,500 cells.

In the case of spheroids generated from A172 and U87 cells, we find that the collective contractility observed at an early time point (30 min after the beginning of the measurements) closely reflects the differences seen at an individual cell level: A172 spheroids are nearly 2-fold stronger compared to equally sized U87 spheroids (21 µN vs. 11 µN; Figure 5d). During these initial time steps, the induced strains on the collagen matrix are still small, and hence there is no global stiffening of the material which could feed back to cell behavior. By contrast, after 12 h, A172 spheroids and U87 spheroids generate comparable collective contractilities of 140 µN and 149 µN, respectively (Figure 5e). While U87 spheroids keep increasing their contractility over the complete 12 h observation period, A172 spheroids show a 2 h-resting period of after a fast initial increase in contractility (Figure 5f, Figure 5—figure supplement 2). Such a collective resting period requires a synchronized change in cellular force generation across the whole cell population. A likely mediator for this cell-cell coupling is the collagen matrix: as the cells pull on the matrix, collagen exhibits strain stiffening. This change in material stiffness then provides a mechanical feedback to the cells and may thus alter cell behavior at the population level (Morley et al., 2019). This example illustrates that collective contractility is not necessarily related to the respective traction forces of individual cells, especially over longer time scales.

### Collective twitching in tumor spheroids

In a previous study (Steinwachs et al., 2016), we have shown that the contractility of individual breast carcinoma cells varies significantly over time, with alternating phases of low and high contractility that last for 50 min on average and that correlate with the migration process of these cells. By contrast, the data reported above demonstrate that spheroids generated from primary triple-negative breast cancer cells, U87 and A172 glioblastoma cells, and Luminal B breast tumoroids all increase their contractility monotonically over time. However, spheroids made from primary Luminal B breast cancer cells show a different behavior: after 2 h of measurement time, these spheroids begin to show repeated twitches (Figure 6a, Video 12) during which the spheroid relaxes the matrix and subsequently contracts again. These contractile twitches are synchronized across the whole spheroid and thus lead to isotropic, radially symmetric inward-outward movements of the surrounding matrix (Figure 6b,c). An individual twitch is completed after 20 min (Figure 6a inset), indicating a fast-moving signal as a mediator of the effect. The amplitude of individual twitches is in between 2–20 µN around a total contractility of 200–400 µN, demonstrating the ability of our method to measure dynamic force fluctuations with relative changes as small as 1%.

![Figure 6.](https://cdn.elifesciences.org/articles/51912/elife-51912-fig6-v1.jpg)

**Figure 6.:** (a) Median contractility (blue line) and the corresponding standard deviation (blue shading) of an exemplary spheroid grown from 4000 primary Luminal B breast cancer cells. The red box marks the contractility values displayed in the inset, illustrating a single twitch starting at 15:35 hr after the beginning of the measurement. (b) Changes in matrix deformations during the contraction phase of a single twitch that lasts for 15 min and is marked in green in (a). Inward-directed arrows indicate increasing contractility. The spheroid outline and its centroid are marked in red. (c) Changes in matrix deformations during the relaxation phase of a single twitch that lasts for 5 min and is marked in red in (a). Outward-directed arrows indicate decreasing contractility.

![Video 12.](https://cdn.elifesciences.org/articles/51912/elife-51912-video12.mp4.jpg)

**Video 12.:** Time is indicated in the upper-left corner (HH:MM:SS).

## Discussion

In this study, we develop, test and apply a contractility assay for quantifying the collective force generation process in tumor spheroids containing hundreds or thousands of cells. Because the assay takes the pronounced strain stiffening of a collagen matrix into consideration, simulated and measured deformation fields in the collagen matrix surrounding a spheroid show good agreement even for large contractile forces with strains of >50% at the spheroid surface. While our method relies on the assumption of a spherical sample geometry, it remains accurate in the far field (>3–4 sample radii) for elliptical or irregularly shaped tumoroids.

For A172 and U87 glioblastoma cells, we find that the collective forces are proportional to the contractility of individual cells during the initial contraction phase (≤ 1 h), but not on longer time scales. In particular, the large strains induced by the spheroids significantly alter the mechanical environment of the invading cells due to strain stiffening and fiber alignment, and thus affect cellular force generation at a collective level and potentially induce enhanced invasion into the surrounding tissue.

Finally, we report collective twitching of spheroids generated from primary Luminal B cells. While the origin of this effect remains unknown, it demonstrates that these cells are able to synchronize their force generation across an entire spheroid containing several thousands of cells. We note that twitching starts only after the spheroid has already generated appreciable matrix deformations approximately 12 h after the beginning of the measurements, corresponding to a contractility of 200 µN or larger. As cell-matrix interactions and the process of tissue remodelling are increasingly recognized as therapeutic targets (Cox and Erler, 2011), our method provides a reliable and simple in vitro assay to quantify the mechanics behind collective effects in cancer invasion that cannot be measured on a single-cell level.

## Materials and methods

### Primary breast tumoroid and primary cell line isolation

Human tissue collection was approved by the Ethics Committee of the Friedrich-Alexander University Erlangen-Nürnberg, Germany (#99_15Bc) in accordance with the World Medical Association Declaration of Helsinki. Informed consent was obtained from all patients.

The Luminal B tumor was obtained from a patient with Luminal B lymph node positive breast cancer (20% Ki67 positive, hormone receptor positive, but Her2 receptor negative) and no prior chemotherapy. The Triple Negative tumor was obtained from a breast cancer patient (70% Ki67 positive, estrogen receptor, progesterone receptor and Her2 receptor negative; and no prior chemotherapy; Weigand et al., 2016).

Isolation of primary breast tumoroids and primary cell lines are performed as described in Weigand et al. (2016). In brief, all breast tumors are examined by a pathologist, the tumor cores identified, dissected, washed 4x with 1x PBS and then incubated with 1x PBS, penicillin and streptomycin for 1 hr at room temperature. Following tissue mincing and an overnight digestion with collagenase/hyaluronidase (Stem Cell Technologies) in basal culture media, the cell lysate is diluted 1:1 with 1x PBS and centrifuged at 88 g for 30 sec at room temperature. The pellet fraction contains tumoroids, which are either purified further into a single fraction or further fractionated into either epithelial or cancer mesenchymal cells (Weigand et al., 2016). All primary cell lines used in this present study are breast cancer mesenchymal cells. To obtain a purified fraction of tumoroids, the initial pellet is resuspended into 5 ml of 1x PBS then processed 5x with a 1.00 × 60 mm sterile needle, diluted 10x with 1x PBS and filtered through 100 µm nylon filters (10 ml per filter; Falcon) and then washed 2x to separate fibrotic tissue. The final tumoroid size ranges from 200 to 600 µm in diameter.

### Primary breast tumoroids and primary breast cell line culture

Directly following isolation, tumoroids are cultured for 4 days in Epicult basal media and Supplement C (Stem Cell Technologies; Epicult-C human media kit), and L-Glutamine on top of 2% soft agarose beds in 2 cm2 culture dishes. This incubation period promotes tumoroid recovery following the isolation procedure from primary tissue. Established primary breast cancer mesenchymal cells are isolated from two Luminal B (LUB1, LUB25) and a Triple negative (TRIDUC1 Weigand et al., 2016) breast cancer and cultured in Epicult basal media with Supplement C (Stem Cell Technologies, Epicult-C human media kit), L-Glutamine, 10% FCS and then initiated into spheroid formation at an early cell passage number of 3–4.

### Glioblastoma cell line culture

A172 and U-87 MG (referred to as U87 in the main text) glioblastoma cell lines are cultured at 37°C, 95% humidity and 5% CO2 in DMEM (high glucose, pyruvate) with 10% (volume/volume) fetal bovine serum, and 100 Units/ml penicillin/streptomycin (all Thermo Fisher Scientific). Cell lines are short tandem repeat (STR) profiled to confirm identity (CellBank Australia) and are confirmed negative for mycoplasma contamination with Venor GeM Classic detection kit (Minerva biolabs).

### Spheroid culture

Glioblastoma spheroids are created from low-adherent, concave-bottomed surfaces in 96-well dishes (Friedrich et al., 2009). 50 µl of a heated 1.5% (weight/volume) agarose (Thermo Fisher Scientific)/DMEM gel solution is pipetted into the wells of a 96-well dish. Following a 10–15 min interval, the solution cools and forms a non-adherent, concave surface. Subsequently, cells are detached from their tissue culture flasks with 0.05% trypsin solution, counted (15,000 cells per dish for A172 cells and 7,500 cells per dish for U87 cells) and pipetted into wells containing 100 µl cell culture medium. The agarose surface promotes formation of a single spheroid per well. Spheroids take 3 days to fully form while being incubated at standard TC conditions.

Primary breast cancer spheroids are created from cell-repellent, U-bottom, 96-well dishes (Greiner). Cells are detached from their tissue culture flasks with 0.05% trypsin solution, counted (4,000 cells per dish for LUB1, LUB25 and TRIDUC1 cells) and pipetted into wells containing 100 µl cell culture medium. Spheroids take 2 days to fully form while being incubated at standard TC conditions.

### Collagen synthesis

Collagen gels are synthesized as described in Steinwachs et al. (2016) and consist of a 1:1 mixture of rat tail collagen (Collagen R, 2 mg/ml, Matrix Bioscience, Berlin, Germany) and bovine skin collagen (Collagen G, 4 mg/ml, Matrix Bioscience), plus 10% (vol/vol) NaHCO3 (23 mg/ml) and 10% (vol/vol) 10 × DMEM (Gibco). The pH of the solution is adjusted to 10 with 1 M NaOH. For a collagen concentration of 1.2 mg/ml, the solution is diluted with a mixture of 1 vol part NaHCO3, 1 part 10 × DMEM and 8 parts H2O, at a ratio of 1:1.

### Glioblastoma spheroid embedding

FluoSphere polystyrene beads (1 µm diameter, Thermo Fisher Scientific) are carefully suspended, without forming bubbles, in 1.2 mg/ml collagen solution at a concentration of 2·108 beads/ml. 1.5 ml of this mixture is poured into a 35 mm plastic culture dish and is allowed to settle for 2.5 min at room temperature, during which time the spheroids are prepared for embedding. The 2.5 min waiting time is too short for a full polymerization of the collagen solution but is sufficient to ensure that spheroids do not sink to the base of the dish.

After the preparation of the bottom collagen layer, 4 to 5 individual spheroids are removed from their culture plate wells and carefully transferred into a 15 ml centrifuge tube using a P1000 pipette. Once the spheroids have settled to the base of the tube, excess media is aspirated away and spheroids are gently resuspended in 500 µl of the 1.2 mg/ml collagen/bead mixture. The mixture, complete with suspended spheroids, is then transferred from the tube into the 35 mm dish using a P1000 pipette. By pipetting the collagen into the dish drop-by-drop, the positioning of the spheroids within the gel can be controlled. Spheroids are kept separate from each other and away from culture dish margins or air bubbles. After spheroid seeding, the gel is incubated at 37 °C and 5% CO2 for 1 h to fully polymerize. 1.5 ml of pre-warmed cell media is added to the dish, and imaging is started.

### Primary breast cancer spheroid and tumoroid embedding

FluoSphere polystyrene beads (1 µm diameter, Thermo Fisher Scientific) are carefully suspended, without forming bubbles, in 1.2 mg/ml collagen solution at a concentration of 2·108 beads/ml. 650 µl of this mixture is poured into one well of a 6-well plate and is allowed to settle for 10 min in the incubator, during which time the spheroids are prepared for embedding. The 10 min waiting time results in a partially polymerized collagen surface and thus ensures that spheroids/tumoroids do not sink to the base of the dish.

After the preparation of the bottom collagen layer, up to 10 individual spheroids/tumoroids are removed from their culture plate wells and carefully transferred into a 15 ml centrifuge tube using a P200 pipette. Once the spheroids/tumoroids have settled to the base of the tube, excess media is aspirated away and spheroids/tumoroids are resuspended in 650 µl of the 1.2 mg/ml collagen/bead mixture. The mixture, complete with suspended spheroids/tumoroids, is then transferred from the tube into the well using a P1000 pipette. After spheroid seeding, the gel is incubated at 37 °C and 5% CO2 for 1 h to fully polymerize. 2 ml of pre-warmed cell media is added to the well, and imaging is started.

### Time-lapse imaging

The equatorial plane of the embedded glioblastoma spheroids is imaged in brightfield mode with a 5x magnification 0.1 NA objective and a CCD camera (corresponding to a pixel size of 1.29 µm) for at least 12 h, with a time interval of 5 min between consecutive images. Samples are kept in a stage-mounted incubation chamber (37 °C, 5% CO2) during time-lapse imaging. Typically, 3–7 spheroids are imaged in parallel (contained in one dish). In total, we imaged 17 A172 spheroids with 15,000 cells, 14 U87 spheroids with 15,000 cells, and 13 U87 spheroids with 7,500 cells (at least three independent experiments per condition; Figure 5—figure supplement 2).

Primary breast cancer spheroids and tumoroids are imaged using a 4x magnification 0.13 NA objective and a CCD camera (corresponding to a pixel size of 1.02 µm) for 24 h, with a time interval of 10 min between consecutive images (except for the measurement of the pulsing Luminal B spheroid shown in Figure 6, which was recorded at a time interval of 1 min). Samples are imaged at 37 °C and 5% CO2 using a microscope placed inside an incubator. We performed measurements on three primary triple-negative breast cancer spheroids on the same day. From those three measurements, one exemplary data set is shown in Figure 3. We performed measurements on five primary Luminal B breast cancer spheroids (LUB25) on the same day. These data sets are shown in the Supplementary Information. We performed measurements on five primary Luminal B breast cancer spheroids (LUB1) on the same day. From those five measurements, one exemplary data set is shown in Figure 6. We performed measurements on 14 tumoroids from the same patient on the same day. From those 14 measurements, exemplary data sets from three tumoroids are shown in Figure 4.

### Material simulations

We use the semi-affine material model described in Steinwachs et al. (2016) to simulate the non-linear behavior of collagen. In particular, collagen gels exhibit three different mechanical regimes, depending on the applied strain. Individual fibers buckle easily under compression (with exponentially suppressed stiffness) and only attain a constant stiffness for small strains, while they exponentially stiffen under large strains:

$$
κ(\epsilon)=κ_{0}⋅{e^{\epsilon/d_{0}}for\epsilon<0buckling1for0<\epsilon<\epsilon_{s}linearregimee^{(\epsilon−\epsilon_{s})/d_{s}}for\epsilon_{s}<\epsilonstrainstiffening
$$

where $κ_{0}$ denotes the linear stiffness, $d_{0}$ and $d_{s}$ describe the rate of stiffness variation during buckling and stiffening, respectively, and $\epsilon_{s}$ denotes the onset of strain stiffening.

These four parameters can be characterized by shear rheometry and by measuring the vertical contraction of a collagen gel under uniaxial stretch. More specifically, the experimentally obtained stress-strain curve from shear rheometry and the contraction-stretch curve from the uniaxial stretch-experiment are fitted to the semi-affine material model described above. The open-source software saenopy provides ready-to-use fitting routines for this purpose, see https://saenopy.readthedocs.io/.

In this study, we use the material parameters determined in Steinwachs et al. (2016), for a 1.2 mg/ml collagen solution based on a 1:1 mixture of rat tail collagen and bovine skin collagen:

$$
κ_{0}=1645Pa,\epsilon_{s}=0.0075,d_{s}=0.033,d_{0}=0.0008
$$

Note that for different collagen concentrations, only the linear stiffness needs to be adjusted (0.6 mg/ml: $κ_{0}=447⁢Pa$, 2.4 mg/ml: $κ_{0}=5208⁢Pa$), whereas $d_{0}$, $d_{s}$, $\epsilon_{s}$ remain constant.

Deformations in the collagen matrix in response to inward-directed tractions at the spheroid surface are computed using a finite element approach (Steinwachs et al., 2016). In brief, the material volume is divided into finite tetrahedral elements, each of which is assumed to contain a number of isotropically oriented fibers. When such a tetrahedron is deformed, the internal stress is first calculated by taking into account the different deformations of the contained fibers, and subsequently averaged over the faces of the tetrahedron and thus propagated to neighboring elements.

Here, we simulate a spherical bulk of material (with an outer radius of 2 cm) with a small spherical inclusion in its center (with a radius of 100 µm). The finite element mesh for this geometry is created using the open-source software Gmsh (Geuzaine and Remacle, 2009). To emulate the contractile behavior of a spheroid, we assume a constant inbound pressure on the surface of the spherical inclusion and further assume zero deformations on the outer boundary of the bulk. Given these boundary conditions, we use the Python-port of the open-source Semi-Affine Elastic Network Optimizer (Steinwachs et al., 2016) (saenopy) to obtain the corresponding deformation field.

### Particle image velocimetry

Given a series of images through the equatorial plane of the spheroid, we apply the open-source PIV software (OpenPIV Taylor et al., 2010) to each pair of subsequent images. The software subdivides the image recorded at time $t$ into $N$ quadratic tiles (using a tile-size of 40 × 40 pixels for the glioblastoma spheroids and 50×50 pixels for primary breast cancer spheroids and tumoroids) at positions $x→^{(i)}$ with $i=1,2,…,N$ and performs a cross-correlation-based template-matching to determine the most likely offset $Δ⁢u→_{t}^{(i)}$ of all tiles with respect to the previous image. These offsets represent the deformation of the material within the time interval between two subsequent images. To account for a drift of the microscope stage between two images, we subtract the mean value

$$
\mu→_{t}=\frac{1}{N}⁢\sumi=1NΔ⁢u→_{t}^{(i)}
$$

from all offsets for a given time step. To obtain the accumulated deformation $u→_{t}^{(i)}$ at position $x→^{(i)}$ and time step $t$, we sum up the pair-wise deformation fields of all time steps $t^{′}\leqt$:

$$
u→_{t}^{(i)}=\sumt^{′}=1t^{′}=tΔu→_{t^{′}}^{(i)}fori=1,2,...,N
$$

Additionally, we determine the spheroid’s centroid $x→_{t}^{sph}$ for all time steps and its initial radius $r_{0}$ by image segmentation (using Otsu, 1979 method). As we are only interested in the radially aligned deformations towards the contracting spheroid, we compute the absolute deformations $u_{t}^{(i)}$ by projecting the accumulated vectorial deformations $u→_{t}$ in the direction towards the spheroid center, using the relative coordinates $d→_{t}^{(i)}=x→^{(i)}-x→_{t}^{sph}$:

$$
u_{t}^{(i)}=−(u→_{t}^{(i)}.\frac{d→_{t}^{(i)}}{|d→_{t}^{(i)}|}),
$$

where ( . ) denotes the dot product. While we place individual spheroids as far apart as possible within the collagen matrix, other spheroids outside the field-of-view may still affect the measured deformation field, especially in the case of small deformations within the field-of-view. To minimize this systematic bias, we only consider projected deformations that point within a ±20° range towards the spheroid center, by imposing the following condition:

$$
|\frac{u→_{t}^{(i)}}{|u→_{t}^{(i)}|}.\frac{d→_{t}^{(i)}}{|d→_{t}^{(i)}|}|>cos(20^{∘})
$$

Finally, we compute the normalized deformations $u_{t}^{(i)}/r_{0}$ and distances $d_{t}^{(i)}/r_{0}$ so that we can directly compare to experimentally measured and normalized deformation fields.

### Geometrical scaling in nonlinear elastic materials

The scale-invariance of the deformation field of a contracting spherical inclusion within a large body of non-linear elastic material (shown by simulation in Figure 2 in the main text) can be derived analytically. The following derivation is discussed in more detail in Steinwachs (2015).

Given a displacement field $U→⁢(r→)$ of an equilibrium configuration (e.g. induced by a spheroid with a radius of 100 µm and an inbound pressure of 50 Pa), we define the re-scaled displacement field (e.g. induced by a spheroid with a radius of 200 µm and the same pressure of 50 Pa) as

$$
U→^{∗}⁢(r→)=a⋅U→⁢(r→/a)
$$

with $a$ being the scaling factor ($a=2$ for the exemplary spheroid sizes noted above). To check whether the equilibrium state remains unaltered by re-scaling the displacement field in this way, we need to show that the deformation gradient $F¯⁢(r→)$ and thus the strain energy density $W⁢(r→)$ as well as the nominal stress $N¯⁢(r→)$ are not altered by the transformation (at the corresponding points $r→→r→/a$):

$$
F¯^{∗}⁢(r→)=\frac{\partial⁡U→^{∗}⁢(r→)}{\partial⁡r→}+I¯=a⋅\frac{\partial⁡U→⁢(r→/a)}{\partial⁡r→}+I¯=F¯⁢(r→/a)
$$



$$
⟶W^{∗}⁢(r→)=W⁢(r→/a)
$$



$$
⟶N_^{∗}(r→)=N_^{∗}(r→/a)⟶div(N_^{∗}(r→))=\frac{1}{a}⋅div(N_^{∗}(r→/a)),
$$

where $I¯$ denotes the unit tensor. Consequently, the equilibrium equation is fulfilled if the body force $b→⁢(r→)$ is divided by the scaling factor $a$:

$$
ρ_{0}⁢b→^{∗}⁢(r→)+div⁢(N¯^{∗}⁢(r→))=0=\frac{1}{a}⋅(ρ_{0}⁢b→^{∗}⁢(r→/a)+div⁢(N¯^{∗}⁢(r→/a)))
$$

We next consider an infinite continuous body with a spherical hole of radius $R$ at the origin. As a boundary condition, we assume that the spherical inclusion has decreased its radius by $Δ⁢R$, and we denote the displacement field $U→⁢(r→)$ as the equilibrium solution. The total strain energy needed for the inclusion to contract (or dilate) can be determined by integrating the strain energy density:

$$
E⁢(Δ⁢R)=\int_{R}^{∞}W⁢(r→)⁢d^{3}⁢r→
$$

If we now assume that a spherical inclusion with a radius $a⋅R$ contracts by $a⋅Δ⁢R$, we can use the scaling laws noted above to relate the strain energy to that of the un-scaled contracting inclusion:

$$
E^{∗}=\int_{a⋅R}^{∞}W⁢(r→/a)⁢d^{3}⁢r→=a^{3}⋅\int_{R}^{∞}W⁢(r→)⁢d^{3}⁢r→=a^{3}⋅E
$$

In equilibrium, the strain energy of the contracted inclusion depends only on $R$, $Δ⁢R$, and the scaling factor $a$:

$$
E⁢(a⋅R,a⋅Δ⁢R)=a^{3}⋅E⁢(R,Δ⁢R)
$$

Finally, we show that the normal surface pressure $P$ induced by the contraction of the spherical inclusion only depends on the relative contraction $Δ⁢R/R$, but not on the scaling factor $a$:

$$
\frac{\partial⁡E⁢(R,Δ⁢R)}{\partial⁡Δ⁢R}⋅\frac{1}{4⁢\pi⁢R^{2}}=\frac{\frac{\partial⁡E⁢(a⋅R,a⋅Δ⁢R)}{a^{3}}}{\frac{\partial⁡(a⋅Δ⁢R)}{a}}⋅\frac{1}{4⁢\pi⁢R^{2}}=\frac{\partial⁡E⁢(a⋅R,a⋅Δ⁢R)}{\partial⁡(a⋅Δ⁢R)}⋅\frac{1}{4⁢\pi⁢a^{2}⁢R^{2}}=P⁢(Δ⁢R/R)
$$

Given a fixed surface pressure, a simulated displacement field $U→⁢(r→)$ of a spherical inclusion with radius $R$ is thus directly related to the deformation field $U→^{∗}⁢(r→)$ of a spherical inclusion with radius $R^{∗}$ by proper re-scaling with the factor $a=R^{∗}/R$.

### Force reconstruction

To assign a contractility value to a measured deformation field, we first conduct 150 material simulations assuming an inbound pressure on the surface of the spherical inclusion ranging from 0.1 Pa to 10,000 Pa (logarithmically spaced), and interpolate between the resulting deformations fields to create a look-up function that translates any deformation/distance-tuple to a best-fit pressure value. For each measured deformation vector (projected towards the center of the spheroid), we then assign the best-fit pressure value. Finally, we take the median of all assigned pressure values at a given time step to obtain a single pressure value for an individual spheroid.

To obtain the contractility $F$ of an individual spheroid from the contractile pressure $P$, we need to account for the spheroid surface area $A$. As we only have images of the equatorial plane of the spheroid, we approximate the surface area by computing an effective radius $r$ from the top-view projected spheroid area $A_{proj}$:

$$
A=4\pir^{2}withr=\sqrt{\frac{A_{ proj}}{\pi}}
$$

The projected spheroid area is determined at the beginning of the experiment by image segmentation (using Otsu, 1979 method).

We provide the Python package jointforces that implements this force reconstruction method. The package further provides pre-computed look-up functions for different collagen gel concentrations (0.6 mg/ml, 1.2 mg/ml, 2.4 mg/ml) as well as for fibrin gel (4.0 mg/ml) and Matrigel (10 mg/ml). See https://github.com/christophmark/jointforces.

### Local matrix stiffness

To determine the local changes in matrix stiffness (see Videos 5 and 7), we first determine the radial strain $\epsilon$ of the material from the deformation field:

$$
\epsilon(r→)=\frac{u(r→)−u(r→+\delta⋅e→_{r}(r→))}{\delta},
$$

where $u⁢(r→)$ denotes the matrix deformation at position $r→$ that is projected in the direction of the spheroid center, $e→_{r}⁢(r→)$ is the unit vector that points radially away from the spheroid center (at position $r→$), and $\delta$ is the differentiation constant. We choose $\delta$ to be of the same size as the window size used in the PIV method for determining the deformation field.

Using the semi-affine material model as defined above, we calculate the radial uniaxial stress $\sigma⁢(r→)$ from the determined strain $\epsilon⁢(r→)$ (see https://saenopy.readthedocs.io for Python code examples). Finally, we evaluate the local matrix stiffness

$$
k⁢(r→)=\frac{\partial⁡\sigma⁢(r→)}{\partial⁡\epsilon⁢(r→)}
$$

using numerical differentiation.

### Single-cell 3D traction force microscopy

3D traction force microscopy is conducted as explained in Cóndor et al. (2017). In brief, we pipet 1.75 ml of collagen solution into a 35 mm Petri dish and let it set for 2.5 min at room temperature. Subsequently, we add 15,000 cells in another 250 µl of collagen and add this solution on top to obtain a 2 mm-thick layer of collagen. This two-layer approach prevents cells from sinking to the bottom before the gel polymerizes. After waiting for one hour to ensure the complete polymerization of the gel, 2 ml of cell culture medium are added. An additional waiting time of at least two hours before imaging ensures that cells have properly spread into a polarized shape within the collagen gel. In each independent experiment, we image a cubic volume V=(370 µm)3 around up to 40 individual cells using confocal reflection microscopy (20× water dip-in objective with NA 1.0). We subsequently add cytochalasin D (20 µM), wait 30 min to ensure actin fiber depolymerization, and repeat the imaging. Based on the measured deformation fields, we obtain the cell contractility and force polarity of 90 individual A172 cells and 86 individual U87 cells from three independent experiments each.

### DNA isolation and proliferation of U87 cells

To establish a standard curve for cell number quantification, the DNA of 2000, 4000, 16000, 32000 U87 cells are extracted and quantified as described below. To measure cell proliferation during the 24 h spheroid formation process, the DNA of U87 spheroids (n = 7) grown for 24 h from 7500 cells is quantified. To measure cell proliferation during 24 h of culture in collagen, U87 spheroids (n = 7) (grown for 24 h from 7500 cells) are embedded in collagen and incubated for an additional 24 h, followed by DNA extraction. To prepare collagen-embedded spheroids for DNA extraction, single spheroids are pipetted and incubated in basal DMEM media (200 µl) containing 1x collagenase/hyaluronidase (Stem Cell Technologies) for 1 hr at 37°C.

For DNA extraction and quantification, 250 µl of 1x cell lysis buffer (final concentration 20 mM Tris-HCL pH 7.4, 15 mM EDTA pH 8.0, 1 % SDS) is added to U87 cell or spheroids (or 50 µl of 4x cell lysis buffer is added to collagenase/hyaluronidase-treated collagen embedded spheroids). All samples are treated with RNAse A (50 µg/ml) for 30 min at 37°C and with Proteinase K (250 µg/ml) overnight at 37°C. The DNA is extracted with phenol/chloroform/isoamyl alcohol (Sigma), then back extracted with 100 µl TE buffer (10 mM Tris-HCL pH 7.5, 1 mM EDTA pH 8.0) and the DNA is precipitated. All DNA measurements are performed using the QuantiFluor dsDNA System kit with a Quantus Fluorometer (all Promega) according to the manufacturer’s protocol.

### Code availability

The traction force microscopy method introduced in this work is implemented in the Python package jointforces, which provides an interface to the meshing software Gmsh (Geuzaine and Remacle, 2009) and includes particle image velocimetry functions to analyze time-lapse image data. The software is open source (under the MIT License) and is hosted on GitHub (https://github.com/christophmark/jointforces; Böhringer and Mark, 2020). For material simulations and to obtain material parameters from macrorheological measurements, jointforces uses saenopy, a Python-port of the network optimizer SAENO (Steinwachs et al., 2016). saenopy is open source (under the MIT License) and is hosted on GitHub (https://github.com/rgerum/saenopy; Gerum, 2020). The figures in this study have been created using the Python packages (Hunter, 2007 and Gerum, 2019).
