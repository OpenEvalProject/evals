# Peer review - Round 1

Editors:
- Cameron Thrash, Louisiana State University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26580.026](https://doi.org/10.7554/eLife.26580.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Microfluidic-based mini-metagenomics enables discovery of novel microbial lineages from complex environmental samples" for consideration by eLife. Your article has been favorably evaluated by Wendy Garrett as the Senior Editor and Cameron Thrash (Reviewer #1) as the Reviewing Editor. The following individuals involved in review of your submission have also agreed to reveal their identity: Brett Baker (Reviewer #2) and Steven Giovannoni (Reviewer #3).

In general the reviewers were favorable towards publication of this work, but the reviewers have a number of concerns that they would like to see addressed first.

Reviewer #1:

The authors present a novel use of microfluidic cell-sorting of microbial communities to facilitate a "mini-metagenomics" approach. I particularly like the combined use of statistics with physical separation in subsamples to refine the binning procedure. While I think this technique was vetted well and has great potential for future application, there are a number of conceptual and technical details I'd like to see fleshed out prior to publication.

Subsection “Microfluidic-based mini-metagenomics enables contig binning based on co-occurrence patterns”, third paragraph: Please detail the criteria for taxonomic lineage assignment. How many genes per contig were required to have the same taxonomic assignment for that contig to be declared part of that group? At what level of taxonomic assignment did that hold (phylum, class, etc.)? What percent ID was required to "trust" the taxonomic assignment for a given gene?

Subsection “Microfluidic-based mini-metagenomics enables contig binning based on co-occurrence patterns”, last paragraph: Did the single copy marker gene tree agree with the CheckM tree? Did the CheckM tree help with taxonomic assignment for those organisms without sufficient gene-based information and/or those without enough genes to be included in the single copy marker tree?

Subsection “Functional analyses reveal dominant energy metabolism in Yellowstone hot spring samples”, first paragraph: How novel are these discoveries for metabolism of the group, and was any additional investigation done? I know nrfA genes need vetting (Welsh et al. 2014 AEM), so these kinds of claims could use more evidence than just blast-ing to KEGG. Why is it interesting that the Euryarchaeota genome has nitrogen fixation genes? Does the genome belong to a subclade where this is unusual?

Subsection “Microfluidic-based mini-metagenomics facilitates assessment of genome abundance and population diversity with single-cell resolution”, first paragraph: How valid is this assumption considering the various shapes and sizes of cells that might be encountered? Please consider and address. Has there been any investigation into whether cell size/morphology biases the microfluidic process?

Subsection “Microfluidic-based mini-metagenomics facilitates assessment of genome abundance and population diversity with single-cell resolution”, first paragraph: Please describe how well the abundance of the organisms in the mini-metagenomics process reflects the abundance of these organisms in the original samples. I believe this should be possible through comparison with the shotgun metagenomics data. This will provide an improved sense of where in the community rank-abundance curve one may hope to explore with the method. It may also reveal if there are biases related to cells from a specific group, which would help answer my preceding questions regarding cell size and morphology in the microfluidics setting.

Subsection “Microfluidic-based mini-metagenomics facilitates assessment of genome abundance and population diversity with single-cell resolution”, last paragraph: How confident are the authors in using SNP determination and dN/dS ratios on genomes that are only binned at the phylum level? In other words, at what level of taxonomic specificity do you believe each genome represents? Species? Strain? Because it seems to me that if the genome represents an amalgamation of data from multiple genetic lineages within a phylum, SNP and dN/dS information could be misleading.

Reviewer #2:

The manuscript is well-written. The methods are sound and the results are justified. I think that this approach might be useful in soils, but given that only 29 genomes were recovered from an YNP hot spring, I personally am not convinced there is a cost advantage or an improvement in genomic reconstruction (based on completeness).

However, I don't see any details about how much sequencing was actually done? This needs to be included, or perhaps I missed it? I would suggest doing an average cost/genome and perhaps do a comparison with output from whole-community assembly and binning. I understand the latter will vary considerably depending on the habitat, so perhaps use a complex community where genomes have been reconstructed like Rifle groundwater (Wrighton et al. 2014)? This might make it more convincing that there is a real advantage to this approach.

As an example, we have been able to obtain 57 genomes (>50%) complete from YNP springs from a modest amount of sequencing, 1 lane of HiSeq and 1 lane of MiSeq. Thus, I'm not particularly impressed with the genome completeness of the bins, as most of them are <50% complete.

Overall, as a test of the approach (testing on mixed cultures and natural communities) this paper does well.

Discussion, first paragraph: – Sure you reduce the cost of sequencing, but you are not getting as much genome by subsampling the community. So this statement is misleading.

Reviewer #3:

This paper describes a useful re-purposing of a commercially available single-cell genomics technology to produce metagenomic data that is roughly equivalent to a library of single-cell assemblies in quality, despite the limitations of the microfluidics preventing the actual sorting of single-cells. Those interested in the use of single-cell genomics (SCG) for the exploration of microbial communities, may consider this to be a viable and possibly much more practical approach than some SCG methods. In this regard, it is a very useful methods paper that addresses a technical deficit in the ability of microbial ecologists with limited funds, space, or personnel who may wish to perform SCG (or SCG-like) analyses in conjunction with metagenomics.
