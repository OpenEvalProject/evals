# Peer review - Round 1

Editors:
- Hernán A Burbano, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64165.sa1](https://doi.org/10.7554/eLife.64165.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper reconstructs the history of native and invasive tomatoes in the Galápagos Islands-including species that were first collected by Darwin himself. This is a careful and thoughtful study that describes a highly interesting case of phenotypic convergence for fruit color, driven by the exchange of carotenoid loci between endemic and invasive populations. The work provides a beautiful example of natural experiments that advance our understanding of evolution.

Decision letter after peer review:

Thank you for submitting your article "Reconstructing the history and biological consequences of a plant invasion on the Galápagos islands" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Senior Editor and a Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Gregory Owens (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Tomatoes of the Galapagos Islands are a fascinating system for studying the introduction of alien species as well as their hybridization and competition with native congeners. The current work is based on genotype information from native and introduced tomatoes on the islands as well as mainland individuals. The authors infer multiple introductions using demographic modelling and admixture/introgression between introduced and native populations, nicely highlighting that introduction histories are rarely simple.

Essential revisions:

A major concern are the potential biases inherent in the use of RAD-seq data in combination with a single reference genome. If the authors want to include the dadi analysis (which is based on the joint SFS), they must not only clearly discuss the caveats, but additional analyses must be conducted with other models. Currently, only a very limited set of models is used, with a focus on the median results in the main text – with very large CIs. One would expect the optima (reported in the text) as well as the bootstrap medians to be similar. That they are not suggests a poor fit between the data and the model. As the authors are very well aware, in these types of analyses there is always a 'best fit model' but the 'best' model is not particularly informative if it does not fit the data well."

I am including the full reviews, which provide several suggestions for how to improve the analyses / moderate the claims.

Reviewer #1:

Gibson and colleagues use RAD-seq genotyping data from continental and island populations of closely related Solanum species to examine population history and evidence for admixture in the Galapagos islands. This paper combines results from those previously published (Gibson et al., 2020, Molecular Ecology, Gibson et al., 2020, Evolutionary Ecology) and adds in new genotyping and population genetic analyses. The conclusions here are that (i) the wild tomato species S. pimpinellifolium was introduced to the Galapagos in the recent past and has caused a decline in the endemic S. cheesmaniae species and S. galapagense species (which appear not to actually be separate species based on the results here) and that (ii) 'borrowed' alleles from the S. cheesmaniae (CHS) and S. galapagense (GAL) have benefitted S. pimpinellifolium in some way, enhancing its reproductive success.

The results are broadly consistent with the previous findings published earlier this year both in terms of overall population structure (Gibson et al., 2020, Molecular Ecology) and the introgression of the orange fruit locus (Gibson et al., 2020, Evolutionary Ecology) and represent a clear next-step in this series of papers.

For the population genetic analyses presented, I am concerned about the potential biases introduced from RAD-seq data and in particular the strong conclusions and especially the specific time estimates regarding the migration of the S. pimpinellifolium populations. Inherent biases from this type of data and their impacts on basic population genetic parameters have been well-characterized. These were described in Gautier et al., 2013, Arnold et al., 2013, and more recently detailed in Cariou et al., BMC 2016. Arnold et al., 2013 (Mol Ecol) conducted analyses based on simulations and empirical data and found severe biases in genealogical inferences as well as population genetic summary statistics (pi, ThetaW, Tajima's D, FST). Similarly, Gautier et al., (Mol Ecol 2013) showed that allelic dropout in RAD-seq studies biases the inference of genetic variation within and between populations, which was further detailed by Cariou et al., BMC 2016.

Compounded with the issues known for RAD-seq, a single Solanum species is used for alignment of reads, which likely results in a further bias toward apparent lower variation in the diverged island species.

Here, the authors calculate the summary statistics that were already shown to be biased when calculated from RAD-seq data and also go further, using the joint site frequency spectrum for inference via analysis with dadi. Tajima's D is of course a summary statistic based on aspects of the SFS and if it is shown to be biased, I would expect that the numbers of variants assigned to the bins of the JSFS (used in dadi) are problematic.

Even in the best case (i.e., full sequence data), with dadi it is easily possible to find multiple very different demographic models that fit the data equally well (for example earlier migration of fewer individuals vs. more recent migration of a larger number of individuals). Also, in this case, the CIs from the dadi analysis are extremely large, which suggests that the models examined are not very close to reality (or that there are deeper issues with bias due to the nature of the genotype data). For example, in PIM, the bootstrap median estimates for the bottleneck and recovery times are 847 generations ago and 840 generations ago, with confidence intervals of 22-13,591 generations ago for the time to recovery and 0-8000 generations ago for the time to the bottleneck. For the species considered to be island endemics, some estimates were provided but no confidence intervals from that dadi analysis were reported. Even if we are to trust there is no major bias in the RAD-seq genotyping, the dadi do not exlude an ancient natural migration of the S. pimpinellifolium species and even seem to support this possibility.

There seems to be pretty strong evidence presented that the orange locus in PIM is due to introgression from CHS.

Gibson and colleagues use RAD-seq genotyping data from continental and island populations of closely related Solanum species to examine population history and evidence for admixture in the Galapagos islands. This paper combines results from those previously published (Gibson et al., 2020, Molecular Ecology, Gibson et al., 2020, Evolutionary Ecology) and adds in new genotyping and population genetic analyses. The conclusions here are that (i) the wild tomato species S. pimpinellifolium was introduced to the Galapagos in the recent past and has caused a decline in the endemic S. cheesmaniae species and S. galapagense species (which appear not to actually be separate species based on the results here) and that (ii) 'borrowed' alleles from the S. cheesmaniae (CHS) and S. galapagense (GAL) have benefitted S. pimpinellifolium in some way, enhancing its reproductive success.

The results are broadly consistent with the previous findings published earlier this year both in terms of overall population structure (Gibson et al., 2020, Molecular Ecology) and the introgression of the orange fruit locus (Gibson et al., 2020, Evolutionary Ecology) and represent a clear next-step in this series of papers.

For the population genetic analyses presented, I am concerned about the potential biases introduced from RAD-seq data and in particular the strong conclusions and especially the specific time estimates regarding the migration of the S. pimpinellifolium populations. Inherent biases from this type of data and their impacts on basic population genetic parameters have been well-characterized. These were described in Gautier et al., 2013, Arnold et al., 2013, and more recently detailed in Cariou et al., BMC 2016. Arnold et al., 2013 (Mol Ecol) conducted analyses based on simulations and empirical data and found severe biases in genealogical inferences as well as population genetic summary statistics (pi, ThetaW, Tajima's D, FST). Similarly, Gautier et al., (Mol Ecol 2013) showed that allelic dropout in RAD-seq studies biases the inference of genetic variation within and between populations, which was further detailed by Cariou et al., BMC 2016.

Compounded with the issues known for RAD-seq, a single Solanum species is used for alignment of reads, which likely results in a further bias toward apparent lower variation in the diverged island species.

Here, the authors calculate the summary statistics that were already shown to be biased when calculated from RAD-seq data and also go further, using the joint site frequency spectrum for inference via analysis with dadi. Tajima's D is of course a summary statistic based on aspects of the SFS and if it is shown to be biased, I would expect that the numbers of variants assigned to the bins of the JSFS (used in dadi) are problematic.

Even in the best case (i.e., full sequence data), with dadi it is easily possible to find multiple very different demographic models that fit the data equally well (for example earlier migration of fewer individuals vs. more recent migration of a larger number of individuals). Also, in this case, the CIs from the dadi analysis are extremely large, which suggests that the models examined are not very close to reality (or that there are deeper issues with bias due to the nature of the genotype data). For example, in PIM, the bootstrap median estimates for the bottleneck and recovery times are 847 generations ago and 840 generations ago, with confidence intervals of 22-13,591 generations ago for the time to recovery and 0-8000 generations ago for the time to the bottleneck. For the species considered to be island endemics, some estimates were provided but no confidence intervals from that dadi analysis were reported. Even if we are to trust there is no major bias in the RAD-seq genotyping, the dadi do not exlude an ancient natural migration of the S. pimpinellifolium species and even seem to support this possibility.

There seems to be pretty strong evidence presented that the orange locus in S. pimpinellifolium is due to introgression from CHS.

Reviewer #2:

This paper reconstructs the invasion history of wild tomatoes in the Galapagos. The authors genotype multiple samples from four species, including native and invasive tomatoes, and their putative mainland progenitors. They find support for multiple Ecuadorian origins of the invasion using demographic modelling. They also find that there has been introgression in multiple instances between native and invasive species and that a fruit color polymorphism in PIM is likely due to introgression from CHS at fruit color loci.

I really enjoyed this paper. It does a very nice and clean job of testing its hypotheses using modern techniques, like dadi or Locator, but also backing them up with basic pop-gen statistics, e.g., π and dxy. The figures are well-made and thoughtful, and the methods are very well documented. I think the results are worth publishing in eLife, in particular the finding that fruit color has introgressed is an interesting story that will catch people's interests. With this in mind, I wholeheartedly endorse the paper.
