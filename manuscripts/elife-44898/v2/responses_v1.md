# Author response - Round 1

Authors:
- Yifu Ding ([ORCID: 0000-0002-4629-5858](https://orcid.org/0000-0002-4629-5858))
- Daniel J Vanselow ([ORCID: 0000-0002-9221-8634](https://orcid.org/0000-0002-9221-8634))
- Maksim A Yakovlev ([ORCID: 0000-0003-1846-3751](https://orcid.org/0000-0003-1846-3751))
- Spencer R Katz ([ORCID: 0000-0002-5586-3562](https://orcid.org/0000-0002-5586-3562))
- Alex Y Lin ([ORCID: 0000-0002-1653-4168](https://orcid.org/0000-0002-1653-4168))
- Darin P Clark
- Phillip Vargas
- Xuying Xin
- Jean E Copper
- Victor A Canfield ([ORCID: 0000-0002-4359-1790](https://orcid.org/0000-0002-4359-1790))
- Khai C Ang ([ORCID: 0000-0001-7695-9953](https://orcid.org/0000-0001-7695-9953))
- Yuxin Wang
- Xianghui Xiao
- Francesco De Carlo
- Damian B van Rossum
- Patrick La Riviere ([ORCID: 0000-0003-3415-9864](https://orcid.org/0000-0003-3415-9864))
- Keith C Cheng ([ORCID: 0000-0002-5350-5825](https://orcid.org/0000-0002-5350-5825))

## Response text

DOI: [10.7554/eLife.44898.035](https://doi.org/10.7554/eLife.44898.035)

Reviewer #1:

[…] A minor concern is that two more citations may be appropriate, as only one of the previous papers dealing with soft-tissue imaging by micro-CT in zebrafish is discussed (Babaei, 2016). So that the reader may make comparisons between the data in this manuscript and previous work with zebrafish, it would be helpful to cite Delphine Cheng et al., 2016 for their 3D characterization of the zebrafish GI tract (at lower resolution) in the third paragraph of the Introduction. The 2015 paper by Seo and colleagues in Zebrafish presented work similar in scope to this manuscript and should be discussed. This group imaged whole juvenile zebrafish by synchrotron micro-CT with a pixel size of 0.65 μm (I am unsure of voxel size but the image resolution appears to be lower), using various stains to enhance contrast of soft tissue and blood vessels. (Despite the topics being similar, I think that the image quality in the current manuscript is much better, and the discussion of technique development is much more thorough.)

We agree with including discussion of the suggested articles in context. Resolution is commonly computed as the field-of-view divided by the number of pixels covering that field-of-view, assuming otherwise perfect optics from scintillator to imaging array. Experimental validation of image resolution requires the use of phantoms or other internal controls (in our case, striations of skeletal muscle with previously characterized resolution). It is worth noting that achieved resolution is frequently lower than computed reconstruction resolution.

Reviewer #2:

[…] Remaining questions that are not addressed in this current version of the manuscript involves long-term accessibility of the data and tool. For example, how can the dataset described here be used as a scaffold for a detailed morphological atlas for zebrafish? Despite the tools presented, what does it take for a lab conducting lightsheet imaging (as a use case example) to obtain the subcellular resolution imaged for potential overlay work? For deployment of this work on other mutants (or for other model systems), what will be needed?

Indeed, long-term accessibility of the data and tool is a critical factor needed to promote a broad variety of applications. We have now addressed this issue, in the Discussion of the manuscript.

The pancellular nature of X-ray histotomography makes it ideal for building atlases of normal at the cellular through organ level. A detailed morphological atlas will require full volume representations of fish including larval, juvenile and adult stages. These images will need to be accessible through web-based resources. Fulfilling the long-term goal of unbiased, computational phenotyping will depend on statistical definitions of normal, for both gross and microscopic anatomy. Recognition of “abnormal” phenotypes will be based on comparisons with the statistical normal.

For a lab conducting fluorescence-based imaging – light sheet imaging, for example, there are ways to obtain organismal context at cellular and subcellular resolution. Fluorescent images can be superimposed on a micro-CT atlas by registering one to the other in a region-specific manner. Alternatively, cell-to-cell correlations between fluorescent cells and their histotomographic counterparts in the same fish can be achieved by X-ray histotomography after fixation and metal staining of the fluorescently imaged samples.

Deploying this technology for model organism phenotyping across laboratories will benefit from standardization of sample preparation, imaging parameters, and methods of analysis. Synchrotron-based resources presently appear to be the most suitable for standardization due to their far greater through-put and superior image quality. The applicability of this technology across all tissue types indicates that dedicated synchrotron beamlines for histotomography are justified. Laboratory-based tissue micro-CT using commercial sources will vary in terms of resolution and image quality. For optimal cross-referencing across laboratories, these same samples can be re-imaged at a synchrotron-based resource and shared through a common repository.

To facilitate access to our data, we have uploaded relevant data sets (along with code, supporting data, and descriptions) onto the Dryad Digital Repository, available at https://doi.org/10.5061/dryad.4nb12g2, as suggested by eLife. In the future, we envision a community driven and supported common repository for these types of large imaging data sets, where visualization tools, like ViewTool, are built-in and used for data exploration and evaluation.
