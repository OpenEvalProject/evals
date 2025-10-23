# Enabling X-ray free electron laser crystallography for challenging biological systems from a limited number of crystals

## Authors

- Monarin Uervirojnangkoorn<sup>1</sup>
- Oliver B Zeldin<sup>1</sup>
- Artem Y Lyubimov<sup>1</sup>
- Johan Hattne<sup>2</sup> ([ORCID: 0000-0002-8936-0912](https://orcid.org/0000-0002-8936-0912))
- Aaron S Brewster<sup>3</sup>
- Nicholas K Sauter<sup>3</sup>
- Axel T Brunger<sup>1</sup> ([ORCID: 0000-0001-5121-2036](https://orcid.org/0000-0001-5121-2036)) †
- William I Weis<sup>1</sup> ([ORCID: 0000-0002-5583-6150](https://orcid.org/0000-0002-5583-6150)) †

### Affiliations

1. Department of Molecular and Cellular Physiology Stanford University Stanford United States
2. Janelia Research Campus Ashburn United States
3. Physical Biosciences Division Lawrence Berkeley National Laboratory Berkeley United States
4. Department of Neurology and Neurological Sciences Howard Hughes Medical Institute, Stanford University Stanford United States
5. Department of Photon Science Stanford University Stanford United States
6. Department of Structural Biology Stanford University Stanford United States

† Corresponding author

## Abstract

10.7554/eLife.05421.001 There is considerable potential for X-ray free electron lasers (XFELs) to enable determination of macromolecular crystal structures that are difficult to solve using current synchrotron sources. Prior XFEL studies often involved the collection of thousands to millions of diffraction images, in part due to limitations of data processing methods. We implemented a data processing system based on classical post-refinement techniques, adapted to specific properties of XFEL diffraction data. When applied to XFEL data from three different proteins collected using various sample delivery systems and XFEL beam parameters, our method improved the quality of the diffraction data as well as the resulting refined atomic models and electron density maps. Moreover, the number of observations for a reflection necessary to assemble an accurate data set could be reduced to a few observations. These developments will help expand the applicability of XFEL crystallography to challenging biological systems, including cases where sample is limited. DOI: http://dx.doi.org/10.7554/eLife.05421.001

## Introduction

Radiation damage often limits the resolution and accuracy of macromolecular crystal structures (Garman, 2010; Zeldin et al., 2013). Femtosecond X-ray free electron laser (XFEL) pulses enable the possibility of visualizing molecular structures before the onset of radiation damage, and allow the dynamics of chemical processes to be captured (Solem, 1986; Neutze et al., 2000). Thus, from the first XFEL operation at the Linac Coherent Light Source (LCLS) in 2009, there has been considerable effort dedicated to the development of methods to utilize this rapid succession of bright pulses for macromolecular crystallography, with the aim of obtaining damage-free, chemically accurate structures. Most of the structures reported from XFELs to date use a liquid jet to inject small crystals into the beam (DePonte et al., 2008; Sierra et al., 2012; Weierstall et al., 2014), but diffraction data have also been measured from crystals placed in the beam with a standard goniometer setup (Cohen et al., 2014; Hirata et al., 2014). In both cases, the illuminated volume diffracts before suffering damage by a single XFEL pulse. Because the crystal is effectively stationary during the 10–50 fs exposure, ‘still’ diffraction patterns are obtained, in contrast to standard diffraction data collection where the sample is rotated through a small angle during the exposure.

Extracting accurate Bragg peak intensities from XFEL diffraction data is a substantial challenge. An XFEL data set comprises ‘still’ diffraction patterns generally containing only partially recorded reflections, typically from randomly oriented crystals. The full intensity then has to be estimated from the observed partial intensity observations. Most XFEL diffraction data processing approaches reported to date have approximated the full intensity by the so-called “Monte Carlo” method, in which thousands of partial intensity observations of a given reflection are summed and normalized by the number of observations, which assumes that these observations sample the full 3D Bragg volume. Because a single diffraction image—in which each observed reflection samples only part of each reflection intensity–contains much less information than a small continuous wedge of diffraction data (as used in conventional crystallography), this method requires a very large number of crystals to ensure convergence of the averaged partial reflection intensities to the full intensity value (Kirian et al., 2010). Moreover, shot-to-shot differences in pulse intensity and energy spectrum that arise from the self-amplified stimulated emission (SASE) process (Kondratenko and Saldin, 1979; Bonifacio et al., 1984), along with differences in illuminated crystal volume, mosaicity, and unit-cell dimensions, contribute to intensity variation of the equivalent reflections observed on different images. These differences are assumed to be averaged out by the Monte Carlo method (Hattne et al., 2014). Thus, accurate determination of these parameters for each diffraction image should, in principle, provide more accurate integrated intensities, and converge with fewer measurements. Furthermore, it is desirable to assemble a data set from as few diffraction images as possible, since the potential of XFELs has been limited by the very large amounts of sample required for the Monte Carlo method, compounded by severe limitations in the availability of beamtime.

In the 1970's, the Harrison and Rossmann groups developed ‘post-refinement’ methods (Rossmann et al., 1979; Winkler et al., 1979), in which the parameters that determine the location and volume of the Bragg peaks are ‘post’-refined against a reference set of fully recorded reflections following initial indexing and integration of rotation data. Accurate estimation of these parameters, including the unit-cell lengths and angles, crystal orientation, mosaic spread, and beam divergence enables accurate calculation of what fraction of the reflection intensity was recorded on the image, i.e., its ‘partiality’, which is then used to correct the measurement to its fully recorded equivalent. Applied to virus crystals, for which only a few images can typically be collected before radiation damage becomes significant, post-refinement made it possible to obtain high-quality diffraction data sets collected from many crystals (Rossmann et al., 1979; Winkler et al., 1979).

The implementation of post-refinement for XFEL diffraction data poses unique challenges. Firstly, since XFEL diffraction data generally do not contain fully recorded reflections, the initial scaling and merging of images is difficult. Secondly, since the XFEL diffraction images are stills rather than rotation data, different approaches are required for the correction of measurements to determine the full spot equivalent. Other schemes for implementing post-refinement of XFEL diffraction data have been described previously, but thus far they have been only applied to simulated XFEL data (White, 2014), and to pseudo-still images collected using monochromatic synchrotron radiation (Kabsch, 2014).

We have developed a new post-refinement procedure specifically designed for diffraction data from still images collected from crystals in random orientations. We implemented our method in a new computer program, prime (post-refinement and merging), that post-refines the parameters needed for calculating the partiality of reflections recorded on each still image. We describe here our method and demonstrate that post-refinement greatly improves the quality of the diffraction data from XFEL diffraction experiments with crystals of three different proteins. We show that our post-refinement procedure allows complete data sets to be extracted from a much smaller number of diffraction images than that necessary when using the Monte Carlo method. Thus, this development will help make XFEL crystallography accessible to many challenging problems in biology, including those for which sample quantity is a major limiting factor.

## Results

## Notation

Units are arbitrary unless specified in parenthesis.

Iobs, observed intensity.

Iref, reference intensity.

w, weighting term (inverse variance of the observed intensity).

G, function of linear scale (G0) and resolution-dependent (B) factors that scales the different diffraction images to the reference set.

Eoc, Ewald-offset correction function.

rh, offset reciprocal-space distance from the center of the reflection to the Ewald sphere (Å−1).

rp, radius of the disc of intersection between the reciprocal lattice point and the Ewald sphere (Å−1).

rs, radius of the reciprocal lattice point (Å−1).

![Figure 1.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig1-v2.jpg)

**Figure 1.:** r.h(A) A reciprocal lattice point intersects the Ewald sphere. The inset shows the coordinate system used in cctbx.xfel and prime. The vector S represents the direction of the incident beam (–0z-axis) and forms the radius of the Ewald sphere of length 1/λ. The reciprocal lattice point i is expressed in reciprocal lab coordinates using Equation 5 as represented by the vector x. The Ewald-offset distance, ir, is the difference between the distance from the Ewald-sphere center to the reciprocal lattice point (length of hS) and 1/iλ. The inset shows the definition of the crystal rotation axes; they are applied in the following order: θz, θy, θx. (B) Shown is the volume of a reciprocal lattice point with radius r. The offset sr defines the Ewald-offset correction hEoc, which is the ratio between the area intersecting the Ewald sphere, areaA, and the area at the center of the volume, pA.sDOI: http://dx.doi.org/10.7554/eLife.05421.003

γ0, parameter for Equation 3 (Å−1).

γe, energy spread and unit-cell variation (see Equation 3; Å−1).

γx and γy, beam divergence (see Equation 4; Å−1).

{uc}, unit-cell dimensions (a, b, c (Å), α, β, and γ (°)).

Vc, reciprocal-lattice volume correction function (Å−3).

xobs and xcalc, observed and predicted spot positions on the detector (mm).

x, position of the reciprocal lattice point (Å−1).

S, displacement vector from the center of the Ewald sphere to x (Å−1).

S0, incident beam vector with length 1/wavelength (Å−1).

O, orthogonalization matrix.

R, rotation matrix.

fL and fLN, Lorentzian function and its normalized counterpart.

Γ, full width at half maximum (FWHM) of the Lorentzian function.

## Post-refinement overview

Partiality can be modeled by describing the full reflection as a sphere (Figure 1A). In a still diffraction pattern, assuming a monochromatic photon source, the observed intensity Iobs,h for Miller index h is a thin slice through a three-dimensional reflection. To calculate partiality, we assume that the measurement is an areal (i.e., infinitely thin) sample of the volume (Figure 1B). The maximum partial intensity that can be recorded for a given reflection will occur when its center lies exactly on the Ewald sphere. By definition, the center of the reflection will be offset from the Ewald sphere by rh, and the corresponding disc will have a radius rp. The offset rh is determined by various experimental parameters, including the crystal orientation, unit-cell dimensions, and X-ray photon energy. The offset distance is used to calculate the Ewald offset correction, Eocarea, defined as the ratio between the areas defined by rp and rs (implemented as a smoothed correction function Eoch as defined in ‘Materials and methods’). The Ewald-offset corrected intensity is then converted to the full intensity in 3D by applying a volume correction factor, Vc.

We define the target Tpr for the post-refinement of a partiality and scaling model by:(1)Tpr= ∑hwh(Iobs,h−G(G0,B)Eoch(θx, θy, γ0,γe,γx,γy,{uc})Vc,h−1 × Iref,h)2  ,which minimizes the difference between the observed reflections Iobs and a scaled and Ewald-offset corrected full intensity ‘reference set’ Iref using a least-squares method. The sum is over all observed reflections with Miller indices h.

In alternate refinement cycles, we also minimize the deviations between predicted (xcalc) and observed (xobs) spot positions on the detector using a subset of strong spots as has been suggested previously (Hattne et al., 2014; Kabsch, 2014):(2)Txy=∑h(xobs−xcalc)2.

Sets of parameters associated with each diffraction image, i.e.,

![Figure 2.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig2-v2.jpg)

**Figure 2.:** The flowchart illustrates the iterative post-refinement protocol, broken up into ‘microcycles’ that refine groups of parameters iteratively (blue boxes), and ‘macrocycles’. At the beginning of first macrocycle, a reference diffraction data set is generated. At the end of each macrocycle, the reference diffraction data set is updated. Both the micro- and macrocycles terminate either when the refinement converges or when a user-specified maximum number of cycles is reached.DOI: http://dx.doi.org/10.7554/eLife.05421.004

Procedures for generating the initial reference set Iref(initial) are described below. After convergence of the microcycles, scaled full intensities are calculated from the observed partial intensities Iobs by multiplication of the inverse of the Ewald-offset correction and the scale factor G, along with the volume correction factor Vc. These scaled full reflections are then merged for each unique Miller index, taking into account estimated errors of the observed intensities, σ(Iobs), and propagation of error estimates for the refined parameters. This merged and scaled set of full reflections is then used as the new reference set in the next round of post-refinement using the target functions (Equations 1 and 2, for details see ‘Materials and methods’). These ‘macrocycles’ are repeated until convergence is achieved, after which the merged and scaled set of full intensities is provided to the user.

The prime program controls post-refinement of specified parameters in a particular microcycle (Figure 2). One can refine all parameters together, or selectively refine groups of parameters iteratively, starting from (1) a linear scale factor and a B-factor, (2) crystal orientations, (3) crystal mosaicity, beam divergence, and spectral dispersion, and (4) unit-cell dimensions. Space-group-specific constraints are used to limit the number of free parameters for the unit-cell refinement. A particular microcycle is completed when the target functions converge or when a specified number of iterations is reached; the program then generates the new reference intensity set to replace the current reference set for the next macrocycle. Finally, the program exits and outputs the latest merged reflection set either when the macrocycles converge or when a user-specified maximum number of cycles has been reached.

## Preparation of the observed intensities

The starting point for our post-refinement method is a set of indexed and integrated partial intensities, along with their estimated errors, obtained from still images. For this study, diffraction data and their estimated errors were obtained from the cctbx.xfel package (Sauter et al., 2013; Hattne et al., 2014), although in principle integrated diffraction data from any other program can be used. Observed intensities on the diffraction image were classified as ‘spots’ by the program Spotfinder (Zhang et al., 2006), which identifies Bragg spots by considering connected pixels with area and signal height greater than user-defined thresholds. By trial and error, we accepted reflections larger than 25 pixels with individual-pixel intensity more than 5 σ over background for myoglobin and hydrogenase (collected on a Rayonix MX325HE detector with pixel size of 0.08 mm and beam diameter [FWHM] of 50 μm). For thermolysin (collected on a Cornell-SLAC pixel array detector with pixel size of 0.1 mm and beam size of 2.25 μm2), where reflections are generally smaller, these values were 1 pixel and 5 σ. A full list of parameters is available on the cctbx.xfel wiki (http://cci.lbl.gov/xfel). Separate resolution cutoffs for each image were applied by cctbx.xfel, at resolutions where the average I/σ(I) fell below 0.5 (Hattne et al., 2014).

Prior to post-refinement, the experimentally observed partial intensities need to be corrected by a polarization factor. The primary XFEL beam at LCLS is strongly polarized in the horizontal plane, and we calculate the correction factor as a function of the Bragg angle (θ) and the angle ϕ between the sample reflection and the laboratory horizontal planes (Kahn et al., 1982; see ‘Materials and methods’). For a stationary crystal and a monochromatic beam, a Lorentz factor correction is not applicable; the spectral dispersion of the SASE beam (δE/E ∼ 3 × 10−3 for the data sets studied here) is accounted for by the γe term (see ‘Materials and methods’).

## Generating the initial reference set and initial parameters

An essential step to initiate post-refinement is the generation of the initial reference set Iref (initial). This reference set has to be estimated from the available unmerged and unscaled partial reflection intensities after application of the polarization correction. For the results presented here, linear scale factors for each diffraction image were chosen to make the mean intensities of each diffraction image equal. Since this procedure can be affected by outliers in the observed intensities, we select a subset of reflections with user-specified resolution range and signal-to-noise ratio (I/σ(I)) cutoffs. From this selection, we calculate the mean intensity on each diffraction image and then scale each image to make the mean intensity of all images equal. We correct the scaled observed reflections to their Ewald-offset corrected equivalents using the starting parameters, and then merge the observations, taking into account the experimental σ(Iobs), to generate the initial reference set.

The initial values for crystal orientation, unit-cell dimensions, crystal-to-detector distance, and spot position on the detector were obtained from the refinement of these parameters by cctbx.xfel. The photon energy was that provided by the LCLS endstation system and is not refined. Initial values for the parameters of the reflection width model are described in the ‘Materials and methods’ section.

## Definition and comparison of data processing schemes

In order to separately assess the effects of scaling, the Ewald offset correction (Equation 1), and post-refinement, we refer to three alternative schemes for processing the diffraction data sets: (1) ‘Averaged merged’, in which intensities were generated by averaging all observed partial intensities from equivalent reflections without Ewald-offset correction and scaling; (2) ‘Mean-intensity partiality corrected’, in which intensities were generated by scaling the reflections to the mean intensity and also applying the Ewald-offset correction determined from the initial parameters obtained from the indexing and integration program, followed by merging; and (3) ‘Post-refined’, in which intensities were from the final set of scaled and merged full reflections after the convergence of post-refinement. We note that although the ‘averaged merged’ process is similar to the original Monte Carlo method (Kirian et al., 2010), the integrated, unmerged partial intensities used in our tests were obtained from the program cctbx.xfel (Hattne et al., 2014), which also refines various parameters on an image-by-image basis (Sauter et al., 2014).

## Quality assessment of post-refined data

We tested our post-refinement method on experimental XFEL diffraction data sets from three different crystallized proteins of known structure: myoglobin, hydrogenase, and thermolysin (Table 1). For quality assessment, we performed molecular replacement (MR) with Phaser (McCoy et al., 2007) using models with selected parts of the known structures omitted, followed by atomic model refinement with phenix.refine (Afonine et al., 2012), and inspection of (mFo-DFc) omit maps. We further used three different metrics: CC1/2, and the crystallographic Rwork and Rfree of the fully refined atomic model. We then compared changes in the three quality metrics between merged XFEL diffraction data sets after scaling, partiality correction, and post-refinement. We also investigated the effect of reducing the number of images used by randomly selecting a subset from the full set of diffraction images and repeating the entire post-refinement, merging, MR and refinement processes using this subset.10.7554/eLife.05421.005Table 1.XFEL diffraction data sets used in this studyDOI: http://dx.doi.org/10.7554/eLife.05421.005MyoglobinClostridium pasteurianum hydrogenaseThermolysinSpace groupP6P42212P6122Resolution used (Å)20.0–1.3545.0–1.6050.0–2.10Unit cell dimensions (Å)a = b = 90.8, c = 45.6a = b = 111.2, c = 103.8a = b = 92.7, c = 130.5No. of unique reflections46,55585,27319,995No. of images* indexed75717712,692No. of images with spots to resolution used307751957Average no. of spots on an image (to resolution used)16283640352Energy spectrumSASE†SASE†SASE†DetectorRayonix MX325HERayonix MX325HECSPAD‡Sample delivery methodfixed targetfixed targetElectrospun jet*This is the number of images indexed using cctbx.xfel program, and in the case of thermolysin it is the number of images indexed for one of the two wavelengths.†SASE: self-amplified spontaneous emission.‡CSPAD: Cornell-SLAC pixel array detector.

Diffraction data for both myoglobin and hydrogenase were collected from frozen crystals mounted on a standard goniometer setup (Cohen et al., 2014), whereas the thermolysin data were collected using an electrospun liquid jet to inject nanocystals into a vacuum chamber (Sierra et al., 2012; Bogan, 2013). The completeness of each data set was better than 90% at the limiting resolution used in our tests (Tables 2, 3, 4). Each diffraction data set involved a different number of images due the differing diffraction quality of the crystals.10.7554/eLife.05421.006Table 2.Statistics of post-refinement and atomic model refinement for myoglobinDOI: http://dx.doi.org/10.7554/eLife.05421.006No. images100757Resolutiona (Å)20.0–1.35 (1.40–1.35)20.0–1.35 (1.40–1.35)Completenessa (%)80.0 (22.2)97.7 (79.8)Average no. observations per unique hkla4.0 (1.2)25.7 (2.0)Averaged-mergedMean-scaled partiality correctedPost-refinedAveraged mergedMean-scaled partiality correctedPost-refinedPost-refinement parametersb Linear scale factor G01.00 (0.00)2.79 (5.02)1.00 (1.04)1.00 (0.00)2.19 (3.83)0.89 (1.07) B0.0 (0.0)0.0 (0.0)3.2 (7.8)0.0 (0.0)0.0 (0.0)6.2 (8.3) γ0 (Å−1)NA0.00135 (0.00028)0.00128 (0.00022)NA0.00147 (0.00042)0.00132 (0.00034) γy (Å−1)NA0.00 (0.00)0.00007 (0.00080)NA0.00 (0.00)0.00007 (0.00009) γx (Å−1)NA0.00 (0.00)0.00010 (0.00011)NA0.00 (0.00)0.00008 (0.00010) γe (Å−1)NA0.00200 (0.00)0.00344 (0.00266)NA0.00200 (0.00)0.00423 (0.00323) Unit cell  a (Å):90.4 (0.4)90.4 (0.4)90.5 (0.4)90.4 (0.4)90.4 (0.4)90.5 (0.3)  c (Å)45.3 (0.4)45.3 (0.4)45.3 (0.3)45.3 (0.3)45.3 (0.3)45.3 (0.3) Average Tpr Start/EndNANA19.39 (7.68)/7.17 (3.38)NANA19.83 (7.54)/6.02 (2.59) Average Txy (mm2) Start/EndNANA169.74 (132.56)/132.02 (104.08)NANA170.66 (144.52)/133.42 (109.58) CC1/2 (%)81.379.686.591.895.798.2Molecular replacement scoresc LLG2837.5043.5291.8264.8364.9320. TFZ10.513.013.413.713.814.0Structure-refinement parameters R (%)39.428.023.521.120.317.8 Rfree (%)42.129.424.823.122.519.7 Bond r.m.s.d.0.0060.0060.0040.0060.0060.006 Angle r.m.s.d.1.140.980.791.031.350.86 Ramachandran statistics  Favored (%)98.098.098.098.098.098.0  Outliers (%)0.00.00.00.00.00.0aValues in parentheses correspond to highest resolution shell.bPost-refined parameters are shown as the mean value, with the standard deviation in parentheses.cMolecular replacement scores reported by Phaser (McCoy et al., 2007): log-likelihood gain (LLG) and translation function (TFZ).10.7554/eLife.05421.007Table 3.Statistics of post-refinement and atomic model refinement for hydrogenaseDOI: http://dx.doi.org/10.7554/eLife.05421.007No. images100177Resolutiona (Å)45.0–1.60 (1.66–1.60)45.0–1.60 (1.66–1.60)Completenessa (%)83.0 (47.7)91.2 (63.5)Average no. observations per unique hkla4.4 (1.7)7.13 (2.3)Averaged-mergedPost-refinedAveraged-mergedPost-refinedPost-refinement parametersb Linear scale factor G01.00 (0.00)0.56 (1.27)1.00 (0.00)0.53 (1.22) B0.0 (0.0)10.0 (7.0)0.0 (0.0)10.5 (6.9) γ0 (Å−1)NA0.00132 (0.00042)NA0.00126 (0.00041) γy (Å−1)NA0.00002 (0.00004)NA0.00002 (0.00004) γx (Å−1)NA0.00008 (0.00009)NA0.00008 (0.00011) γe (Å−1)NA0.00269 (0.00138)NA0.00288 (0.00160) Unit cell  a (Å):110.1 (0.4)110.4 (0.3)110.1 (0.4)110.3 (0.4)  c (Å)103.1 (0.4)103.1 (0.2)103.0 (0.4)103.0 (0.2) Average Tpr Start/EndNA28.20 (10.86)/5.92 (2.35)NA26.47 (12.70)/5.22 (2.72) Average Txy (mm2) Start/EndNA623.36 (314.57)/381.23 (198.44)NA564.30 (267.45)/372.28 (202.28) CC1/2 (%)62.077.371.784.8Molecular replacement scoresc LLG53,352.9612.7229.11774. TFZ69.275.975.079.0Structure-refinement parameters R (%)33.425.329.122.0 Rfree (%)36.728.931.325.0 Bond r.m.s.d.0.0060.0070.0070.007 Angle r.m.s.d.1.431.501.681.97 Ramachandran statistics  Favored (%)96.397.097.096.7  Outliers (%)0.00.00.00.0aValues in parentheses correspond to highest resolution shell.bPost-refined parameters are shown as the mean value, with the standard deviation in parentheses.cMolecular replacement scores reported by Phaser (McCoy et al., 2007): log-likelihood gain (LLG) and translation function (TFZ).10.7554/eLife.05421.008Table 4.Statistics of post-refinement and atomic model refinement for thermolysinDOI: http://dx.doi.org/10.7554/eLife.05421.008No. images200012,692Resolutiona (Å)50.0–2.10 (2.18–2.10)50.0–2.10 (2.18–2.10)Completenessa (%)81.3 (24.3)96.5 (74.8)Average no. observations per unique hkla32.8 (1.2)176.6 (2.4)Averaged-mergedPost-refinedAveraged-mergedPost-refinedPost-refinement parametersb Linear scale factor G01.00 (0.00)1.65 (1.66)1.00 (0.00)2.26 (75.12) B0.0 (0.0)23.0 (33.8)0.0 (0.0)30.1 (59.8) γ0 (Å−1)NA0.00052 (0.00040)NA0.00051 (0.00039) γy (Å−1)NA0.00001 (0.00003)NA0.00001 (0.00003) γx (Å−1)NA0.00002 (0.00004)NA0.00002 (0.00004) γe (Å−1)NA0.00110 (0.00129)NA0.00103 (0.00128) Unit cell  a (Å):92.9 (0.3)92.9 (0.2)92.9 (0.3)92.9 (0.3)  c (Å)130.5 (0.5)130.4 (0.4)130.5 (0.5)130.4 (0.4) Average Tpr Start/EndNA1.15 (0.49)/0.55 (0.23)NA1.15 (0.52)/0.28 (0.13) Average Txy (mm2) Start/EndNA168.13 (117.29)/167.72 (106.14)NA169.01 (122.20)/170.00 (122.57) CC1/2 (%)77.793.594.398.8Molecular replacement scoresc LLG3590.4491.5477.6022. TFZ8.99.724.124.6Structure-refinement parameters R (%)25.219.520.718.4 Rfree (%)29.124.023.921.1 Bond r.m.s.d.0.0040.0020.0020.002 Angle r.m.s.d.0.750.580.590.62 Ramachandran statistics  Favored (%)95.994.695.294.9  Outliers (%)0.00.00.00.0 Zinc peak height  Zn(1) (σ)14.016.014.320.9  Zn(2) (σ)3.65.17.77.1 Average peak height for calcium ions (σ)9.711.314.216.1aValues in parentheses correspond to highest resolution shell.bPost-refined parameters are shown as the mean value, with the standard deviation in parentheses.cMolecular replacement scores reported by Phaser (McCoy et al., 2007): log-likelihood gain (LLG) and translation function (TFZ).

## Myoglobin

For myoglobin, we used both an XFEL diffraction data set consisting of 757 diffraction images (Table 1) collected by the SSRL-SMB group using a goniometer-mounted fixed-target grid (Cohen et al., 2014), and a randomly selected subset of 100 diffraction images. The diffraction images were from crystals in random orientations, with a single still image collected from each crystal.

## Convergence of post-refinement

Convergence properties for our post-refinement method for myoglobin are shown in

![Figure 3.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig3-v2.jpg)

**Figure 3.:** Shown are the values of the refined parameters and target functions during the first macrocycle of post-refinement for a representative diffraction image of the myoglobin XFEL diffraction data set. The iterative post-refinement included SF (scale factors), CO (crystal orientation), RR (reflection radius parameters), and UC (unit-cell dimensions) for three microcycles.DOI: http://dx.doi.org/10.7554/eLife.05421.009

![Figure 4.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig4-v2.jpg)

**Figure 4.:** The plots illustrate the convergence of post-refined parameters, target functions, and quality indicators during post-refinement over five macrocycles. A subset of 100 randomly selected diffraction images from the myoglobin XFEL diffraction data was used. For each specified target function and refined parameter, changes are plotted relative to the previous macrocycle, whereas the quality metric CC is shown as absolute numbers. The changes in post-refined parameters and target functions are shown as ‘box plots’. The bottom and top of the blue box are the first (Q1) and third (Q3) quartiles. The red line inside the box is the second quartile (Q2; median). The black horizontal lines extending vertically from the box indicate the range of the particular quantity at a 1.5 interquartile range (Q3–Q1). The plus signs indicate any items beyond this range.1/2DOI: http://dx.doi.org/10.7554/eLife.05421.010

![Figure 5.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig5-v2.jpg)

**Figure 5.:** (A) Percent completeness and (B) average number of observations plotted as a function of resolution for the myoblogin XFEL diffraction data set consisting of all 757 diffraction images (Table 1) and a randomly selected subset of 100 diffraction images. (C) CC for the averaged merged, mean-intensity scaled with partiality correction, and post-refined myoglobin diffraction data sets consisting of 100 and 757 diffraction images.1/2DOI: http://dx.doi.org/10.7554/eLife.05421.011

Inaccuracies in the starting parameters obtained from indexing and integration of still images may limit the radius of convergence and the accuracy of the post-refined parameters. The sources of such errors will be the subject of future improvement in indexing and integration in cctbx.xfel. Nonetheless, for the systems studied here the post-refinements converged within 3–5 cycles.

## Improvements due to post-refinement

For the myoglobin diffraction data set using all 757 images (

![Figure 6.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig6-v2.jpg)

**Figure 6.:** (A) Difference Fourier (mFo-DF) omit maps around the heme group (which was omitted from molecular replacement and atomic model refinement) for the averaged merged, the mean-scaled partiality-corrected merged, and the post-refined myoglobin XFEL diffraction data sets consisting of all 757 diffraction images (cTable 1) and a randomly selected subset of 100 diffraction images. The maps are contoured are at 2.5 σ. (B) A plot of crystallographic R and workR values vs resolution after atomic model refinement using the specified myoglobin diffraction data sets with inclusion of the heme group, SOfree4, and water molecules.DOI: http://dx.doi.org/10.7554/eLife.05421.012

Omit maps were used to compare the quality of the diffraction data processed with the different methods. Specifically, we omitted the heme group from the molecular replacement search model (PDB ID: 3U3E) and in subsequent atomic model refinement, and calculated mFo-DFc difference maps (Figure 6). The real-space correlation coefficient of the heme group to the difference maps calculated from the post-refined diffraction data sets is higher than that calculated from the corresponding averaged merged diffraction data sets using the same set of diffraction images (Figure 6A).

After initial model refinement with the heme group omitted, we included the heme group and well-defined water molecules and completed the atomic model refinement. The post-refined diffraction data set produced the best Rfree and Rwork values, followed by the mean-scaled partiality corrected, with the averaged merged diffraction data sets yielding the poorest refinement statistics.

Overall, comparison of the CC1/2 (Figure 5), omit map quality, and R values (Figure 6B) shows that post-refinement substantially improves scaling and correction of the diffraction data with respect to the mean-scaled partiality-corrected diffraction data set. Thus, post-refinement against the iteratively improved reference set is superior to methods that only consider each diffraction image individually, even when the reflections are scaled and corrected for partiality.

## 100 diffraction images are sufficient for myoglobin structure refinement

Given the significant improvements obtained by post-refining all available images, we tested whether accurate diffraction data and refined atomic models could be obtained using fewer diffraction images by post-refining the randomly selected subset of 100 myoglobin diffraction images. Since this subset is only 80% complete, the CC1/2 is poorer than that of the full diffraction data set consisting of 757 images, but it is nonetheless greatly improved relative to the corresponding non-post-refined diffraction data set (Figure 5). Moreover, the real-space correlation coefficient of the heme group with the difference map obtained with the post-refined 100 diffraction images is better than that calculated from the averaged merged diffraction data set using all the 757 diffraction images (Figure 6A), despite the higher completeness and CC1/2 value of the latter data set (Figure 5C). Thus, post-refinement both improves diffraction data quality for a given set of images and reduces the number of diffraction images required for structure determination and refinement from serial diffraction data.

## Comparison with a synchrotron data set

We also compared the post-refined XFEL difference map (using all 757 diffraction images) with that calculated from an isomorphous synchrotron data set and model (PDB ID: 1JW8, excluding reflections past 1.35 Å resolution to make the resolution of the diffraction data sets equivalent). The omit maps and real-space correlation coefficients for the heme group were of comparable quality (

![Figure 7.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig7-v2.jpg)

**Figure 7.:** Difference Fourier (mFo-DF) omit maps at 1.35 Å around the heme group (which was omitted from molecular replacement and model refinement), generated from (oA) the synchrotron diffraction data and corresponding model with PDB ID 1JW8 (for comparison, all reflections past 1.35 Å resolution were excluded) and (B) the post-refined myoglobin XFEL diffraction data set using all 757 diffraction images (Table 1). The maps are contoured at 2.5 σ.DOI: http://dx.doi.org/10.7554/eLife.05421.013

## Hydrogenase

XFEL diffraction data for Clostridium pasteurianum hydrogenase were measured from eight crystals by the Peters (University of Montana) and SSRL-SMB groups using a goniometer-mounted fixed-target grid (Cohen et al., 2014). This experiment generated 177 diffraction images that could be merged to a completeness of 91%, with more than half of the diffraction images containing reflections to 1.6 Å (each diffraction image typically has approximately 3000 spots). We also used a randomly selected subset of 100 diffraction images to assess the effect of post-refinement on a smaller number of images.

The

![Figure 8.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig8-v2.jpg)

**Figure 8.:** (A) Difference Fourier (mFo-DF) omit maps of one of the four Fe-S clusters (which were omitted in molecular replacement and atomic model refinement) for the averaged merged and the post-refined hydrogenase XFEL diffraction data sets consisting of all 177 diffraction images (cTable 1) and a randomly selected subset of 100 diffraction images. The maps are contoured at 3 σ. (B) Crystallographic R and R values vs resolution after atomic model refinement using the specified diffraction data sets with inclusion of the three Fe-S clusters and water molecules.freeDOI: http://dx.doi.org/10.7554/eLife.05421.014

## Thermolysin

For thermolysin, we tested the entire deposited XFEL diffraction data set consisting of 12,692 diffraction images (Table 1) (Hattne et al., 2014; the diffraction data are publicly archived in the Coherent X-ray Imaging Data Bank, accession ID 23, http://cxidb.org), as well as a randomly selected subset of 2000 diffraction images. In this experiment, the crystal-to-detector distance gave a maximum resolution of 2.6 Å at the edge and 2.1 Å at the corners of the detector. Thus, a large number of diffraction images were required to achieve reasonable completeness of the merged data set for reflections in the 2.1—2.6 Å resolution range.

As in the other two cases, post-refinement significantly improved the CC1/2 value (Table 4). For quality assessment, zinc and calcium ions were omitted from the thermolysin molecular replacement search model (PDB ID: 2TLI) and subsequent atomic model refinement. Post-refinement improved the peak heights of both the zinc and calcium ions (Table 4).

## Anomalous difference Fourier peak heights

The thermolysin diffraction data were collected at a photon energy just above the absorption edge of zinc, so we compared the anomalous signals with and without post-refinement. We used the same four diffraction data sets (i.e., averaged-merged, post-refined, with 2000 and 12,692 diffraction images, respectively), but processed them keeping Friedel mates separate. We refined the atomic model of thermolysin lacking zinc and calcium ions, and calculated anomalous difference Fourier maps (

![Figure 9.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig9-v2.jpg)

**Figure 9.:** Anomalous difference Fourier maps for the averaged merged (A, C) or the post-refined (B, D) thermolysin XFEL diffraction data sets consisting of all 12,692 diffraction images (A, B—Table 1) and a randomly selected subset of 2000 diffraction images (C, D). The anomalous difference Fourier maps were computed using phases from the thermolysin atomic model (but excluding zinc and calcium ions), refined separately against each diffraction data set. All maps are contoured at 3 σ; the peak heights for the two zinc ions are indicated.DOI: http://dx.doi.org/10.7554/eLife.05421.015

## Difference map reveals a bound dipeptide

When the molecular replacement model of thermolysin was refined against the post-refined data, we observed a well-connected electron density feature in the

![Figure 10.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig10-v2.jpg)

**Figure 10.:** (A) Difference Fourier (mFo-DF) maps revealing a Leu–Lys dipeptide near the zinc site for the averaged merged and the post-refined thermolysin XFEL diffraction data sets consisting of all 12,692 diffraction images (cTable 1) and a randomly selected subset of 2000 diffraction images, respectively. The maps are contoured at 3 σ. (B) Crystallographic R and R values vs resolution for the refinements after atomic model refinement using the specified diffraction data sets and with inclusion of two zincs, calcium ions, and the Leu–Lys dipeptide.freeDOI: http://dx.doi.org/10.7554/eLife.05421.016

## Effect of completeness

The completeness of the merged data sets has a direct impact on the overall quality of the diffraction data set (

![Figure 11.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig11-v2.jpg)

**Figure 11.:** (A) Average number of observations per unique hkl. (B) CC for merged subsets using 2000–12,000 images (100% completeness for all subsets). (1/2C) Peak height (σ) in the omit map for the largest peak. (D) R and workR after refining the thermolysin model without zinc and calcium ions against the corresponding post-refined diffraction data sets.freeDOI: http://dx.doi.org/10.7554/eLife.05421.017

## Discussion

Diffraction data collection using conventional x-ray sources typically employs the rotation method, in which a single crystal is rotated through a contiguous set of angles, and the diffraction patterns are recorded on a 2-D detector. If a full data set can be collected from a single crystal without a prohibitive level of radiation damage, diffraction data processing is a well-established and reliable process. In contrast, processing of XFEL diffraction data, which are collected from crystals in random orientations as ‘still’ diffraction images, requires new methods and implementations such as those described here. Improved data collection and processing methods, particularly those that can significantly reduce the amount of sample needed to assemble a complete and accurate diffraction data set, are important for making XFELs useful for certain challenging investigations in structural biology.

We developed a post-refinement method for still diffraction images, such as those obtained at XFELs, and implemented it in new computer program, prime, that applies a least-squares minimization method to refine parameters as defined in our partiality model. Other post-refinement methods for XFEL diffraction data have been described recently (Kabsch, 2014; White, 2014), but our implementation differs from these reports. Kabsch uses a partiality model in which an Ewald offset correction is defined as a Gaussian function of angular distance from the Ewald sphere. White used the intersecting volume between the reflection and the limiting-energy Ewald spheres defined by the energy spectrum for the partiality calculation, and calculates the initial reference data set by averaging all observations without scaling. Neither report describes an application to experimental XFEL diffraction data, so we cannot compare these methods to the results presented here.

We have demonstrated here that our implementation of post-refinement substantially improves the quality of the diffraction data from three different XFEL experiments. Moreover, the resulting structures can be refined to significantly lower Rfree and R values, with electron density maps that reveal novel features more clearly, than those using non-post-refined XFEL data sets. A key feature of our method is that the parameters that define the diffracted spot are iteratively refined against the reference set. This approach is superior to methods that only consider each diffraction image individually. Moreover, our post-refinement procedure allows accurate diffraction data sets to be extracted from a much smaller number of images (average number of observations) than that necessary without post-refinement. Thus, this development will make XFEL crystallography accessible to many challenging problems in biology for which sample quantity is a major limiting factor.

At present, it is difficult to assess the relative quality of post-refined XFEL data studied here with conventional rotation data measured at a synchrotron. The comparison of myoglobin omit maps (Figure 7) suggests that the SR data are perhaps somewhat better, but more systematic studies will be needed to understand the relative merits of the different data sets. We suspect that rotation data would be better due to the ability to directly measure full reflections (at least by summation of partials) without modeling partiality, which is still a relatively crude process (see below). However, a comparison between still data sets measured at a synchrotron and an XFEL is needed to deconvolute the effect of rotation vs other differences between these sources.

Our formulation of post-refinement employs the simplifying assumption that reflections are spherical volumes. More sophisticated models consider crystal mosaicity to have three components, each with a distinct effect on the reciprocal lattice point (Juers et al., 2007; Nave, 1998, 2014). First, the domain size (the average size of the coherently scattering mosaic blocks) produces reciprocal lattice points of constant, finite size: small domains produce large-sized spots, while large domains produce small spots, as there is an inverse (Fourier) relation between spot size and domain size. Second, unit-cell variation among domains produces reflections that are spheres whose radii increase with distance from the origin. In cctbx.xfel, mosaicity (modeled as isotropic parameter) and effective domain size are taken into account when predicting which reflections are in diffracting position prior to integration (Sauter et al., 2014; Sauter, 2015). Third, orientational spread among mosaic domains produces spots shaped like spherical caps. Each cap subtends a solid angle that depends on the magnitude of the spread. In addition, anisotropy in crystal mosaicity is not considered; this would require refining separate parameters along each lattice direction. Finally, the rugged energy spectrum that results from the SASE process of the XFEL is not yet considered in our current model. These issues will require future investigation.

## Materials and methods

## Partiality model

The observed intensity Ih(i) for observation i of Miller index h is a thin slice through a three-dimensional reflection. To calculate partiality, we assume that the measurement is an infinitely thin, circular sample of a spherical volume (Figure 1B). We assume a monochromatic beam as the starting point to define the Ewald offset correction Eocarea. The Eocarea of any reflection centered on the Ewald sphere is defined as 1; this position corresponds to the maximum partial intensity that could be measured for the reflection. The Eocarea for any other position is defined as a function of the normal distance from the Ewald sphere to the center of the reciprocal lattice point (the offset distance, rh), and of the reciprocal-lattice radius of the spot rs, which is a function of the crystal mosaicity and spectral dispersion (Figure 1B). The Eocarea can be described by the ratio of the observed area (Ap) with a radius rp to the Ewald-offset corrected area (As) with a radius rs (Figure 1B).

The SASE spectrum emitted by the XFEL is broad and varies from shot-to-shot (Zhu et al., 2012). To calculate the Ewald sphere, we set the wavelength to be the centroid of the SASE spectrum recorded with each shot. For XFEL data measured with a seeded beam (Amann et al., 2012), the spectrum is narrow and constant from shot-to-shot, and this single value can be used in this case.

In order to model spectral dispersion and the possible effects of asymmetric beam divergence, we adapt the rocking curve model described in Winkler et al. (1979). The four-parameter function used for the rocking curve is rs(γ0, γe,γx, γy)= rs(θ)+ rs(α), where the first term includes the contribution by spectral dispersion and the second term models beam anisotropy. Specifically,(3)rs(θ)=γ0+γe tan θ,where γ0 is a parameter that is initially set to the r.m.s.d. of the Ewald offset calculated for all the reflections on a given image, γe represents the width of the energy spread and the unit-cell variation (the initial value of γe is calculated from the average energy spread), and θ is the Bragg angle. The second term is provided by:(4)rs(α)=[(γy cos α)2+(γx sin α)2]1/2,where α is the azimuthal angle going from meridional (α = 0) to equatorial (α = π/2) . The values of γy and γx are initially set to 0.

The distribution of

![Figure 12.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig12-v2.jpg)

**Figure 12.:** r.hThe histogram shows the distribution of r calculated after post-refinement for myoglobin using 757 diffraction images. The number of observations after applying the reflection selection criteria for merging and outlier rejections for this 1.35 Å data set is 1,136,447 (∼96% of the total observed reflections). The standard deviation is 0.0016 1/Å or approximately 0.12° (when calculated with the mean of the energy distribution).hDOI: http://dx.doi.org/10.7554/eLife.05421.018

## Calculating the reciprocal lattice point offset

The crystal orientation is described in a right-handed coordinate system with the z-axis pointing to the source of the incident beam and the y-axis vertical (Figure 1A). We define the crystal orientation by rotations in the order θz, θy, θx about these axes. For each Miller index h(i), the reciprocal lattice point vector x(i) is obtained by applying orthogonalization and rotation matrixes O and R:(5)x(i)=ROh(i),wherex(i)=(x(i), y(i), z(i)),h(i)=(h(i), k(i), l(i)),O=(a∗b∗ cos γ∗c∗ cos β∗0b∗ sin γ∗c∗(cos α∗− cos γ∗)/sin γ∗00c∗ cos(c∗, c)),R=RθxRθyRθz,where Rθi is the rotation matrix for a rotation around the i-th axis, a∗, b∗, c∗, α∗, β∗, γ∗  are the reciprocal unit-cell parameters, and cos(c∗, c)=(1+2 cos α∗ cos β∗ cos γ∗−cos2α∗−cos2β∗−cos2γ∗)1/2/sin γ∗.

As shown in Figure 1A, the displacement to x(i) from the center of the Ewald sphere is given by:(6)S(i)= x(i)+S0,where S0 = (0, 0, −1/λ). The offset distance is thus the difference between the length of S(i) and the Ewald-sphere radius,(7)rh= |S(i)|−1/λ.

## The Ewald-offset correction function Eoc

We introduce a smooth approximation of the area ratio Eocarea (see ‘Results’) in order to circumvent the undefined first derivative when the ratio is zero. We use a Lorentzian function (fL) to model the radius as function of distance from the Ewald sphere:(8)fL= 1π12Γ(rh)2+(12Γ)2.

The function is normalized so that fL(rh = 0) = 1.0 when the reciprocal-lattice point is centered on the Ewald sphere, so that(9)fLn= πΓ2fL.

We then use the ratio of the observed area (Ap) with a radius rp to the Ewald-offset corrected area (As) with a radius rs (Figure 1B) that corresponds to the full width at half maximum (FWHM), Γ, in the Lorentzian function. Using the Lorentzian function to describe the falloff in radius as we move away from the Ewald sphere makes the Eoc function differentiable at rh = rs. For the reciprocal lattice volume being bound by a sphere of radius rs centered on the reciprocal lattice point, the intersecting area of the volume is given by:(10)Ap=πrp2,whererp=(rs2−rh2)1/2.

The Eoc is then given by the ratio of this intersecting area to the area when this reflection is centered on the Ewald sphere (As),(11)Eocarea=ApAs=πrp2πrs2=1−rh2rs2.

By setting the FWHM of

![Figure 13.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig13-v2.jpg)

**Figure 13.:** (A) Ewald-offset correction Eoc (Equation 14) viewed as a function of the reciprocal-lattice radius (r) and the offset distance (sr). (hB) A slice through Eoc at r = 0.003, comparing sEoc (Equation 14) and Eoc (areaEquation 11).DOI: http://dx.doi.org/10.7554/eLife.05421.019

The use of this Lorentzian approximation to derive the Eoc function vs an actual sphere function, Eocarea, is illustrated in Figure 13B.

## Correction to full intensity

To adjust the observed still intensity to its equivalent at zero offset, we apply the Ewald-offset correction to the observed intensity,(15)IEoc,h(i)=Ih(i)Eoch(i)Gm,where Ih(i) is the observed partial intensity i of Miller index h on image m, Eoch(i) is the Ewald-offset correction, and Gm is a scale function for image m. We then convert this maximum partial intensity to a full intensity estimate by correcting for the volume of the spot, a factor of 43πrs3πrs2 =43rs:(16)Ifull,h(i)=Vc,h(i)IEoc,h(i),whereVc,h(i)=43rs,h(i).

Note that Ifull,h(i) will be on an arbitrary scale, and appropriate scaling methods may be applied to place the data on a quasi-absolute scale prior to structure determination and refinement, as is done for conventional rotation data.

## Refinement of crystal orientation, reflection width, and unit-cell parameters

We refine image m by first minimizing the target function:(17)Tpr=∑h∑iWh(i)(Ih(i)−GmEoch(i)Vc,h−1(i)Ih)2,where1/Wh(i)=σh2(i),and the scale function Gm comprises a linear scale factor G0 and a B-factor:(18)Gm=G0,me−2Bm(sin θh(i)/λm)2.

We apply a spot position restraint as a second target function in subsequent steps during a microcycle using the x, y positions determined by the spot-finding step of data processing (Hattne et al., 2014; Kabsch, 2014).(19)Txy=∑h∑i(xhobs(i)−xhcalc(i))2,where xhobs(i) and xhcalc(i) are the observed and calculated spot centroids, respectively.

The Levenberg–Marquardt (LM) algorithm from the scipy python library (Oliphant, 2007), which is a combination of the gradient descent and the Gauss–Newton iteration, is used to minimize the target function residuals. The refinement of the unit-cell parameters (a, b, c, α, β, γ) takes crystal symmetry constraints into account to make the procedure more robust.

After these iterative refinement cycles are complete, we apply the refined parameters to the reflection intensities of each still, and then merge the same reduced Miller indices (from all stills) to obtain the zero-offset still intensities, which are used for the new reference intensity set (see next section).

## Reflection selection criteria

At each step in a microcycle, the user can select reflections that are used for post-refinement of a parameter group using the following criteria: resolution range, signal strength (I/σ(I)), and the Ewald offset correction value. In addition to these selection criteria, deviations from the target unit-cell dimensions (specified as a fraction of each dimension) can also be used in the merging step so that only diffraction patterns with acceptable unit-cell dimension values are included in the merged reflection set. Each post-refinement parameter group can have its own separate set of reflection selection criteria.

## Merging procedure

Starting from the observed intensities, we obtain the full-volume intensity, Ifull,h(i), from IEoc,h(i) by first applying the Ewald offset correction (Equation 15) and then the full-intensity correction (Equation 16). Prior to merging equivalent observations, we detect outliers using an iterative rejection scheme, discarding reflections with intensity more or less than a user-specified cutoff (3 σ default, where σ is defined as the standard deviation of the distribution of the full reflections Ifull,h). Finally, in order to obtain the merged reflection set, we calculate 〈Ih〉 from the intensity of reflections with the same reduced Miller indices using the sigma-weighted average:(20)〈Ih〉=∑iWh(i)I full,h(i)∑iWh(i),whereWh(i)=1σ2(i)[I full,h(i)],and σ(i)[I full,h(i)] is derived from the calculation of error:(21)(ΔIfull,h(i)Ifull,h(i))2=(ΔIh(i)Ih(i))2+(ΔGG)2+(ΔEocEoc)2.

Since G is a function of G0 and B, and Eoc is a function of crystal orientation, mosaicity, and unit-cell parameters, the error estimates for G can be further calculated as:(22)ΔG2=(∂G∂G0)2ΔG02+(∂G∂B)2ΔB2,and ΔEoc2 can be calculated similarly by summing all over products of partial derivatives and errors estimated for each parameter in the Eoc function (square root of the diagonal elements of the covariance matrix).

We use CC1/2 as a quality indicator for the diffraction data sets (Diederichs and Karplus, 2013). We calculate CC1/2 by randomly partitioning all (partial) intensity observations of a given reflection into two groups. We reject any reflections with fewer than four observations; for all other reflections, we merge the observations in each group using Equation 20. CC1/2 is then calculated as the correlation between these two independently merged diffraction data sets.

## Partial derivatives of the diffraction parameters

Let(23)g=1σ(I−G0e−2B(sin θ/λ)2EocVc−1I),for observed partial intensity i of miller index h.

## Scale factor, G0 and B.

The derivatives of function g with respect to G0:(24)∂g∂G0= −e−2B(sin θ/λ)2EocIσVc.

The derivatives of function g with respect to B:(25)∂g∂B= −G0EocIσVc[2(sin θλ)2e−2B(sin θ/λ)2].

## Crystal rotation angles (θx, θy, θz).

Although three rotation angles θx, θy, θz can be refined, a rotation around the beam direction (z-axis) has no component on the reciprocal-lattice offset (rh) from the Ewald sphere—therefore, the derivative with respect to θz is 0. The partial derivatives with respect to the remaining parameters can be derived in a similar way—here, only the derivatives with respect to are θy given.(26)∂g∂θy=∂g∂Eoc∂Eoc∂rh∂rh∂x∂x∂R∂R∂θy,where∂g∂Eoc= −G0e−2B(sin θ/λ)2IσVc,∂Eoc∂rh=−4rhrs2(2rh2+rs2)2,∂rh∂x=S|S|,∂x∂R=∂R∂θyOh,and R is the rotation matrix of the still image. The derivatives of the g function (Equation 24) with respect to θx and the unit-cell parameters can be calculated by substituting the last partial derivatives of R with the appropriate ones.

## Unit-cell parameters (a, b, c, α, β, γ)

For unit-cell parameters, constraints imposed by crystallographic space groups are applied during the refinement—e.g., tetragonal systems only have two free parameters (a and c) since a = b and α = β = γ = 90. Other restraint conditions, such as allowable refinement limits of the unit-cell dimensions, can also be applied as a ‘penalty terms’ in the least-squares refinement. The partial derivatives with respect to each unit-cell parameter in reciprocal units (here, a∗ is given and a∗=1/a):(27)∂g∂a∗=∂g∂Eoc∂Eoc∂rh∂rh∂x∂x∂O∂O∂a∗,where ∂g∂Eoc, ∂Eoc∂rh, and ∂rh∂x are as derived in (2) and∂x∂O=R∂O∂a∗h.

## Reflection radius, rs

The reflection radius that accommodates effects of crystal mosaicity and spectral dispersion, described by the four parameters, γ0, γy, γx, and γe, has following derivatives:

For γy,(28)∂g∂γy=∂g∂Eoc∂EocVc−1∂rs∂rs∂γy,where ∂g∂Eoc is derived in (Equation 27) and∂EocVc−1∂rs=−3(rs2+2rh2)4(rs2+2rh2)2,∂rs∂γy=γy cos2 α[(γy cos α)2+(γx sin α)2]1/2.

For γx and γe, the ∂g∂p and ∂p∂rs are the same as derived for γy and∂rs∂γx=γx sin2 α[(γy cos α)2+(γx sin α)2]1/2,∂rs∂γ0=1,∂rs∂γe=tan θ.

## Polarization correction

The XFEL beam is nearly 100% polarized in the horizontal direction. The optics at both the LCLS XPP and CXI stations do not introduce additional polarization. To account for the polarization of the primary beam, for a given reflection, we consider the angle

![Figure 14.](https://cdn.elifesciences.org/articles/05421/elife-05421-fig14-v2.jpg)

**Figure 14.:** The diagram shows a reflection on a plane formed by its reciprocal-space vector and the -z-axis at angle . This reflection is affected by the polarization of the incoming primary beam in both the horizontal (ϕx) and vertical (y) directions.DOI: http://dx.doi.org/10.7554/eLife.05421.020

As described in Kahn et al. (1982), the beam I0 incident on the sample crystal can be described in terms of two components, one parallel (σ) and the other perpendicular (π) to the plane of reflection:(29)I0=Iσ+Iπ.

Each of these components is affected by the polarization of the primary beam in both the horizontal (x) and vertical (y) directions. Using fx and fy as the fractions horizontal and vertical in the laboratory frame (fx + fy = 1),(30)Iσ=(fx cos2 ϕ+fy sin2 ϕ)I0,and(31)Iπ=(fx sin2 ϕ+fy cos2 ϕ)I0,where fx and fy are the polarization fractions in the x and y directions.

After reflection, only Iσ is attenuated:(32)I′=I′π+ I′σ= |F|2(Iπ+Iσ cos22θ).

By substituting Iσ and Iπ from Equations 30 and 31 in Equation 32, we arrive at(33)I′=|F|2[fx(sin2 ϕ+cos2 ϕ cos22θ)+fy(cos2 ϕ+sin2 ϕ cos22θ)]I0 ,where the bracketed expression is P (Kahn et al., 1982).

## Molecular replacement and atomic model refinement protocol

To ensure atomic model refinements against the various diffraction data sets were as comparable as possible, we used a standard semi-automated solution and refinement protocol. First, we performed molecular replacement phasing with known structures as search models (PDB ID 3U3E for myoglobin, 3C8Y for hydrogenase, and 2TLI for thermolysin) with all heteroatoms, water molecules, and ligands removed. Molecular replacement was carried out with Phaser (McCoy et al., 2007) using default settings, with r.m.s.d. set to 0.8. The resulting solutions were then refined using phenix.refine (Afonine et al., 2012) in two cycles. In the first cycle, we carried out rigid body refinement, positional (xyz) refinement with automatic correction of Asn, Gln and His sidechain orientations, and atomic displacement parameter (ADP) refinement. We then used the difference density maps for missing ligands and heteroatoms obtained from this cycle to calculate real-space correlation coefficients using phenix.get_cc_mtz_pdb from the PHENIX software suite (Adams et al., 2010) for myoglobin and thermolysin and the program ‘Map Correlation’ from the CCP4 software (Winn et al., 2011) for hydrogenase. These omit difference density maps are shown in Figures 6, 7, 8, 10. In the second cycle, all ligands and heteroatoms were placed in the difference density maps and combined with the refined structure from the first cycle using Coot (Emsley et al., 2010). The second cycle employed positional and ADP refinement with target weights optimization and water update was carried out with these complete models. The structures were validated by MolProbity (Chen et al., 2010). Final refinement statistics (Tables 2, 3, 4) were analyzed with phenix.polygon (Urzhumtseva et al., 2009) and found to be within acceptable range for other structures at similar resolutions. For the thermolysin structure obtained from anomalous diffraction data (processed keeping Friedel pairs separate), only one cycle of atomic model refinement was carried out. All figures were made in PyMOL (The PyMOL Molecular Graphics System, Version 1.5.0.4 Schrödinger, LLC.).

## Computer program

The computer program, prime, is implemented as a part of the cctbx computational crystallography toolbox (Grosse-Kunstleve et al., 2002). Download and installation instructions are available on the cctbx website (http://cctbx.sourceforge.net).

## Note added at proof

Subsequent to acceptance of this article, a paper was published by Ginn et al. (2015) describing an alternative method for orientation refinement as compared to the method of Sauter et al. (2014), and partiality estimation for each individual image, but without post-refinement.
