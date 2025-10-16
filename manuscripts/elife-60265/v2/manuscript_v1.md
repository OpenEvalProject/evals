# The cryo-EM structure of the human uromodulin filament core reveals a unique assembly mechanism

## Authors

- Jessica J Stanisich<sup>1</sup> ([ORCID: 0000-0002-2702-8092](https://orcid.org/0000-0002-2702-8092))
- Dawid S Zyla<sup>1</sup> ([ORCID: 0000-0001-8471-469X](https://orcid.org/0000-0001-8471-469X))
- Pavel Afanasyev<sup>2</sup> ([ORCID: 0000-0002-6353-6895](https://orcid.org/0000-0002-6353-6895))
- Jingwei Xu<sup>1</sup>
- Anne Kipp<sup>3</sup>
- Eric Olinger<sup>4</sup> ([ORCID: 0000-0003-1178-7980](https://orcid.org/0000-0003-1178-7980))
- Olivier Devuyst<sup>3</sup> ([ORCID: 0000-0003-3744-4767](https://orcid.org/0000-0003-3744-4767))
- Martin Pilhofer<sup>1</sup> ([ORCID: 0000-0002-3649-3340](https://orcid.org/0000-0002-3649-3340))
- Daniel Boehringer<sup>2</sup>
- Rudi Glockshuber<sup>1</sup> ([ORCID: 0000-0003-3320-3843](https://orcid.org/0000-0003-3320-3843)) †

### Affiliations

1. Institute of Molecular Biology & Biophysics, ETH Zurich Zurich Switzerland
2. Cryo-​EM Knowledge Hub (CEMK), ETH Zurich Zurich Switzerland
3. Institute of Physiology, University of Zurich Zurich Switzerland
4. Translational and Clinical Research Institute, Faculty of Medical Sciences, Newcastle University, Central Parkway Newcastle upon Tyne United Kingdom
5. Division of Nephrology, UCLouvain Medical School Brussels Belgium

† Corresponding author

## Abstract

The glycoprotein uromodulin (UMOD) is the most abundant protein in human urine and forms filamentous homopolymers that encapsulate and aggregate uropathogens, promoting pathogen clearance by urine excretion. Despite its critical role in the innate immune response against urinary tract infections, the structural basis and mechanism of UMOD polymerization remained unknown. Here, we present the cryo-EM structure of the UMOD filament core at 3.5 Å resolution, comprised of the bipartite zona pellucida (ZP) module in a helical arrangement with a rise of ~65 Å and a twist of ~180°. The immunoglobulin-like ZPN and ZPC subdomains of each monomer are separated by a long linker that interacts with the preceding ZPC and following ZPN subdomains by β-sheet complementation. The unique filament architecture suggests an assembly mechanism in which subunit incorporation could be synchronized with proteolytic cleavage of the C-terminal pro-peptide that anchors assembly-incompetent UMOD precursors to the membrane.

## Materials and methods

## Purification of human UMOD

Human UMOD fibers were purified from a healthy donor as described in Weiss et al., 2020. Briefly, urine was purified using a diatomaceous earth filter, concentrated, and dialyzed overnight against 0.5 mM EDTA-NaOH, pH 8.2 (300 kDa cut-off, Spectrum laboratories). Aliquots were flash-frozen in liquid nitrogen and stored at ‒20°C until further use. Only the second morning micturition was utilized for urine collection. Protein concentrations were determined as previously described (Weiss et al., 2020).

## Cryo-EM data collection

Protein samples (3.5 µL of 2.5 µM UMOD) were applied to glow-discharged lacey carbon grids with an ultrathin carbon coating (Electron Microscopy Sciences) automatically blotted from the back side of the grid for 13.5 s (100% humidity, 9°C) and plunge frozen in liquid-ethane-propane using a Vitrobot Mark IV (Thermo Fisher Scientific). Micrographs were acquired on a Titan Krios microscope (Thermo Fisher Scientific) operated at 300 kV with a Gatan K2 Summit direct electron detector using a slit width of 20 eV on a GIF-Quantum energy filter. A total of 4679 and 4864 movies were recorded over two data collections from two separate grids and subsequently merged. Images were recorded with EPU software (Thermo Fisher Scientific) at 130 000 x nominal magnification in counting mode with a calibrated pixel size of 1.084 Å. The defocus target ranges were −1.2 µm to −3.3 µm and −0.8 µm to −2.0 µm for the first and second data collection, respectively. Each micrograph was dose-fractionated to 40 frames under a dose rate of 7.5 e- / Å / s, with an exposure time of 6 s, resulting in a total dose of approximately 45 e- / Å2.

## Cryo-EM image processing

The collected movies were motion corrected with MotionCor2 (Zheng et al., 2017). The CTF parameters of the micrographs were estimated using Gctf 1.06 (Zhang, 2016). Following steps of image processing were done in cryoSPARC v2.15 (Punjani et al., 2017) and with the in-house written python scripts for data administration and interpretation (https://github.com/dzyla/umod_processing_scripts). Approximately 600 particles were manually picked from a random selection of micrographs and used to train a convolutional neural network picking model for TOPAZ (Bepler et al., 2019). A total of 1.3 million particles were picked via TOPAZ from all micrographs. For the first steps of processing, particles were extracted with 320 px box size and binned to 2.71 Å/px. After several rounds of 2D classification, 723,000 particles, corresponding to well resolved, clear classes, were selected for further processing. Three ab initio initial models were generated and a single best one was used as a 3D-reference for the 3D-heterogeneous refinement. 3D-heterogeneous refinement with 10 classes resulted in multiple distinct 3D class-averages, showing intrinsic flexibility of the specimen. The most populated 3D class-average of 145,000 particles was chosen for further refinements. Particles from the selected class were then re-extracted at the original pixel size and subjected to a 3D-homogenous refinement. A mask was created in UCSF Chimera (Pettersen et al., 2004) for the center segments of 3D-reconstruction and used for several rounds of local refinement using a non-uniform refinement strategy. This pipeline yielded high-resolution 3D-reconstruction of the central asymmetric unit (AU; ZPN, ZPC, and the inset linker) at 3.5 Å. Detailed workflows are shown in Figure 1—figure supplement 1, Supplementary file 1B,C.

To obtain a map focused on several repeat units, an alternative approach was applied using cisTEM for refinement and classification: all micrographs were manually selected, resulting in a total of 8543 movies which were then also motion corrected using MotionCor2, CFT values estimated using Gctf, and 485,000 particles were manually picked as helices from a random selection of 3600 micrographs in RELION v3.0.8 (Zivanov et al., 2018) and extracted at the original pixel size. The particle stack was then subjected to 2D-classification in cisTEM (Grant et al., 2018). 402,000 good particles were selected, and multiple rounds of focused classification was performed with the imported best cryoSPARC 3D class-average as a reference (described above) and a spherical (120 Å radius) mask. Two of the resulting 3D class-averages were merged and another round of 3D-classification with the same spherical mask was undertaken, resulting in a map resolved to 4.7 Å from 330,000 particles. The map was filtered to 4.7 Å and sharpened using cisTEM default settings (pre-cut-off B-Factor −90.0, resolution cut-off 4.7 Å). Reported helical parameters were estimated in real space from the cisTEM map using relion_helix_toolbox (He and Scheres, 2017) with search ranges for rise (60‒67 Å) and twist (175–185°). Schematic workflows and details are shown in Figure 1—figure supplement 1, Supplementary file 1B,D. For comparative purposes, the cisTEM map FSC curves and the local resolution maps were calculated in cryoSPARC for all generated half-maps.

## Model building and structure refinement

The individual ZP subdomains of the UMOD crystal structure (PDB: 4WRN; Bokhove et al., 2016) were used as initial models (ZPN: aa 428–528, ZPC: aa 541–710, according to the 4WRN numbering). First, the individual domains were rigid-body fitted to the map obtained in cryoSPARC using UCSF Chimera, followed by manual building in Coot 0.9 and ISOLDE (Croll, 2018; Emsley et al., 2010). The asymmetric unit (AU, defined as a single ZPN and ZPC and the inset linker) of UMOD was refined using phenix.real_space_refine program (Adams et al., 2010) with the default settings, which apply Ramachandran restraints. To reduce clashes between subunit interfaces, the AU model was used to create a model with four consecutive ZP subdomains and was refined against the cisTEM map. The structure of the UMOD ZP module was then applied to the RosettaCM refinement with the symmetry derived from the cisTEM map (Song et al., 2013), with the ‘auto’ strategy applied in the refinement. The central ZPN/ZPC module in the refined structure was manually adjusted to the high-resolution cryoSPARC map in COOT and was subsequently used to generate the final UMOD model. This updated model was subjected to the next round of RosettaCM refinement, with a higher RMS model restraint applied (r.m.s. = 0.2). Overall, three rounds of interactive manual and RosettaCM refinements were performed and the geometry parameter of the final AU model structure was further improved using phenix.real_space_refine with tight reference restraints (sigma = 0.025). The sidechain residues 462‒473 in the AU model could not be built with confidence and were omitted from the final model.

For the final model of the UMOD filament, a structure was generated with 3 copies of the final AU model by applying the symmetry derived from the cisTEM map. The central ZPN/ZPC subunit of the core part of the structures were subjected to a real space refinement with tight reference restraints (sigma = 0.025) using the cryoSPARC map. The center ZPN/ZPC subunit in the refined model was then used to generate the new UMOD filament structure. Clashes in the subunit interface were further reduced by performing another round of phenix.real_space_refine with tighter reference restraints (sigma = 0.02).

Model validations were performed using the Comprehensive Validation tool in PHENIX. Final model statistics were generated using MolProbity tool via PHENIX (Chen et al., 2010). Figures of the structure were prepared with PyMol v2.4 (The PyMOL Molecular Graphics System, Version 2.4 Schrödinger, LLC) and EM map figures were generated with UCSF ChimeraX 0.93 (Goddard et al., 2018).

## Cryo-EM model 3D flexibility analysis

The well-resolved reconstructions from 3D classifications steps performed independently in cryoSPARC and cisTEM were rigid-body fitted with ZP subdomains derived from the final model. Each subdomain was first placed at the correct position and then fitted by the Fit in Map tool in Chimera 1.13.1. In total, 6 ZP subdomains were fitted into nine maps where the subdomain Coulomb potential was well defined (four classes from cryoSPARC and five classes from cisTEM) and saved with fixed positions to each other as a ‘filament’. Next, using the PyMOL align command, all nine filament structures were aligned to the center ZPN subdomain. In Chimera, the define axis command was used to give each subunit a centroid and a central axis. For subunits at positions ZPC-1 and ZPC, the maximum angle was determined with the angle command.

## 3D variability analysis of UMOD

3D variability analysis (3DVA) was performed in cryoSPARC using ~723,000 particles extracted at the pixel size of 4.34 Å, 10 modes, and filter resolution of 9.2 Å. The 3DVA display job was run in the simple output mode with 20 intermediate frames. From 10 generated components, the first two exhibited the same yaw/pitch movement (Figure 1—video 2), the third showed an artifact at the box edge, and the fourth showed the elongation along the filament axis (Figure 1—video 2). The higher components showed various movements in the arms (not shown).

## Assessing genetic variation using gnomAD

Genome Aggregation Database (GnomAD) v2.1.1 (https://gnomad.broadinstitute.org/) is aligned against the GRCh37 genome build and was released in March 2019. The dataset comprises 125,748 exomes and 15,708 genomes sequenced as part of various disease-specific and population genetic studies, totaling 141,456 unrelated individuals from eight major populations (Karczewski et al., 2020). Results for UMOD were filtered for missense variants and checked for consistency with the UMOD transcript ENST00000302509.8. Missense variants corresponding to a non-canonical transcript were manually removed.

UMOD variants were parsed using an in-house Python script (https://github.com/dzyla/umod_processing_scripts) and plotted on the structure. Residues with no mutations were set to 1.0 and for all non-zero variants the values were normalized between 0 and 1, based on the PAM250 matrix. The structure was visualized by spectrum coloring in PyMOL 2.4. For Supplementary file 1A, all linker residues are shown and the interfaces are defined by atoms that are within 8 Å of one another, as defined by COCOMAPS (Vangone et al., 2011).
