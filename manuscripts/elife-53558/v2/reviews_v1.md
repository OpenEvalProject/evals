# Peer review - Round 1

Editors:
- Kevin Struhl, Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53558.sa1](https://doi.org/10.7554/eLife.53558.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article “Chromosome organization by one-sided and two-sided loop extrusion” for consideration by eLife. Your article has been reviewed by one peer reviewer, and the evaluation has been overseen by a Senior/Reviewing Editor. The reviewer has opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. The required revision should address the issues raised in the review.

Reviewer #1:

This paper aims to resolve an important issue in the SMC protein field by reconciling conflicting results from in vitro single-molecule experiments that showed 1-sided DNA loop extrusion, while previous loop-extrusion based modelling of in vivo Hi-C data assumed 2-sided extrusion. From the extensive simulations presented in this paper, it is concluded that pure 1-sided motors cannot account for the full range of biological phenomena associated with loop extrusion, but various alternatives are offered that account for both the experimental observation of such motors and the in vivo data. This is interesting and new.

The manuscript is well structured and clearly articulated, and examines biologically relevant cases. The modelling from the Marko/Mirny labs has been instrumental for our understanding of DNA loop extrusion, and this paper again adds valuable new information. The conclusions are well supported by the simulation data and discussed in the context of biology and recent single molecule experiments.

I recommend publication of the work in eLife after the authors address the questions and comments mentioned below.

– In some of the modelling, a fair comparison with the data is obtained with the semi-diffusive 1D LE model. However this is realized for very large values of vdiff, which can as large as (or exceeding) the LE speed v. With v≈ 1 kb/s, it seems entirely unreasonable to assume a vdiff of that same order of magnitude, as this would imply an extremely fast diffusion of the large SMC complexes along DNA. The authors should discuss how (un)reasonable large such values for vdiff are, and comment on this, if these are indeed physically implausible.

– The authors generally appear to conflate 'eukaryotic chromosomes' with 'mammalian chromosomes' (e.g. with statements such as 'Unlooped chromatin from one-sided extrusion hinders eukaryotic chromosome compaction and organization', etc). This seems unwarranted and should be distinguished more precisely. A major motivation for the current modelling work seems to be the in vitro work by Ganji et al., who measured 2D LE for yeast condensin from S. cerevisiae. Hence it would be natural to compare the simulation results with chromosomal compaction and HiC results obtained for yeast condensin. Hi-C results on yeast SMC proteins have yielded quite different behavior from that of metazoan cells (likely because of the relatively small chromosomes), and notably yeast does not have CTCFs which are a major boundary element in vertebrate cells. Indeed, budding yeast condensin seems to organize more stripes pattern than dots in HiC data (Figure 5B of Schalbetter et al., 2017). In addition, yeast cohesin showed different TAD organization patterns (Schalbetter et al., 2017; Tanizawa et al., 2017). The authors do have a brief paragraph describing some yeast compaction data at the end of their paper, but I would advise to include a more explicit modelling of the chromosomal compaction and HiC for yeast throughput the paper, as well as a much more in-depth discussion regarding the associated comparison to the published yeast data.
