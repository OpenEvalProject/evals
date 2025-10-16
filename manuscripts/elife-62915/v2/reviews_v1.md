# Peer review - Round 1

Editors:
- Simon Yona, The Hebrew University of Jerusalem Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62915.sa1](https://doi.org/10.7554/eLife.62915.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The revised manuscript now has a clearer analysis workflow. ImmunoCluster is a user-friendly pipeline R package for the analysis of flow and mass cytometry experiments and for imaging mass cytometry. We hope this provides non-computational immunologists with an opportunity to use dimensionality reduction, unsupervised clustering and differential expression/abundance analyses.

Decision letter after peer review:

Thank you for submitting your article "ImmunoCluster: A computational framework for the non-specialist to profile cellular heterogeneity in cytometry datasets" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tadatsugu Taniguchi as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Evan W Newell (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

The authors propose ImmunoCluster, a user-friendly pipeline R package for the analysis of flow and mass cytometry experiments and for imaging mass cytometry. The claim is that this approach and package is easy to use for non-computational immunologists and facilitates dimensionality reduction, unsupervised clustering, and differential expression/abundance analyses.

While this software is useful, the examples provided are good, there is very little/no novelty in the approach provided. The reviewers main concern is that the paper in its current form does not propose any new methodology with regards to clustering, visualization, or differential analysis. It was felt that the paper in its current form combines existing methodology in a user-friendly way that could indeed be important for biologists. In addition, the paper should acknowledge similar packages that already exist (eg CytofKit https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005112).

The combined reviewers' comments can be found below. For this manuscript to merit further consideration at eLife, clearer descriptions of ease of use of Immunocluster compared to other methods and other distinguishing features should be better highlighted and additional benchmarking comparisons.

Summary:

This tool enables advances but other tools already available that are sufficient and therefore the authors will need to convince a large portion of the researcher to use this tool, better comparisons should be provided to help in answering this question and then also better convince readers to use this software.

Essential revisions:

The authors note that several other similar packages influenced the development of ImmunoCluster (Refs 13-16) but it is unclear what makes this package novel. For instance, how does this workflow compare to other packages such as CATALYST (referenced by the authors) for quantifying cell cluster abundances and assessment of differential composition, which has been used in various ways in several publications (Crowell et al. F1000Res. 2020 [this one is new so not yet possible to have referenced], Weber et al., Communications Biology 2019, Nowicka et al., F1000Res. 2017, and related Fonseka et al. Sci. Trans. Med. 2018)? With regards to the differential abundance testing, there has been some excellent work in recent years, including DiffCyt (https://www.nature.com/articles/s42003-019-0415-5) and Cydar (https://pubmed.ncbi.nlm.nih.gov/28504682/). These methods among others seem to be the state-of-the-art in differential abundance analysis. How do your differential analysis results compare to these others, for example? Can you implement these methods in your pipeline?

The authors mention that the pipeline can accommodate millions of cells. Is this the case for all the clustering and visualization steps, or do you require downsampling? It would be helpful to see an analysis of run-time/details of the computer used to analyse the data. It appears the clustering methods implemented here (phenograph for example) might not work well if there are millions of cells across multiple samples.

In the MDS plots of samples (see Figure 3A), it is unclear what features are used to project the samples. Could you please elaborate on this point?

Does this current approach have any means for assessing or correcting for batch effects within the datasets? The authors only mention sample barcoding as an experimental plan to reduce batch effects, but fail to mention of any strategy to assess or correct for batch effects, which is a very important consideration that should be addressed.

Similarly, although channel spillover and differences in cell numbers were mentioned, no means were provided to assess or rectify these effects using the approach described.
