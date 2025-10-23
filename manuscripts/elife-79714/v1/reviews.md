# Peer review - Round 1

Editors:
- Christian R Landry, https://ror.org/04sjchr03 Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79714.sa0](https://doi.org/10.7554/eLife.79714.sa0)

This important study provides an impressive dataset containing more than 200 novel ancient human genome sequences and a creative, robust, novel approach for studying human migration across time. The authors' conclusions are well supported by the data, and the methods used are convincing and solid. This paper will be of great interest to population geneticists and other scholars in the field of paleogenomics.


---

# Peer review - Round 1

Editors:
- Christian R Landry, https://ror.org/04sjchr03 Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79714.sa1](https://doi.org/10.7554/eLife.79714.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Stable population structure in Europe since the Iron Age, despite high mobility" for consideration by eLife. I am sorry it took a long time before we could get back to you with a full evaluation. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Landry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Benjamin Marco Peter (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Some technical concerns were raised regarding the statistical analyses. Some may require additional analyses and some need additional details on how the analyses were performed, including presenting the intermediate steps.

2) One reviewer mentioned that the origin of some of the data was difficult to trace.

Reviewer #1 (Recommendations for the authors):

This paper presents an interesting data set from historic Western Eurasia and North Africa. Overall, I commend the authors for presenting a comprehensive paper that focuses the data analysis of a large project on the major points, and that is easy to follow and well-written. Thus, I have no major comments on how the data was generated, or is presented. Paradoxically, historical periods are undersampled for ancient DNA, and so I think this data will be useful. The presentation is clever in that it focuses on a few interesting cases that highlight the breadth of the data.

The analysis is likewise innovative, with a focus on detecting "outliers" that are atypical for the genetic context where they were found. This is mainly achieved by using PCA and qpAdm, established tools, in a novel way. Here I do have some concerns about technical aspects, where I think some additional work could greatly strengthen the major claims made, and lay out if and how the analysis framework presented here could be applied in other work.

Clustering analysis

I have trouble following what exactly is going on here (particularly since the cited Fernandes et al. paper is also very ambiguous about what exactly is done, and doesn't provide a validation of this method). My understanding is the following: the goal is to test whether a pair of individuals (lets call them I1 and I2) are indistinguishable from each other, when we compare them to a set of reference populations. Formally, this is done by testing whether all statistics of the form F4(Ref_i, Ref_j; I1, I2) = 0, i.e. the difference between I1 and I2 is orthogonal to the space of reference populations, or that you test whether I1 and I2 project to the same point in the space of reference populations (which should be a subset of the PCA-space). Is this true? If so, I think it could be very helpful if you added a technical description of what precisely is done, and some validation on how well this framework works.

An independent concern is the transformation from p-values to distances. I am in particular worried about i) biases due to potentially different numbers of SNPs in different samples and ii) whether the resulting matrix is actually a sensible distance matrix (e.g. additive and satisfies the triangle inequality). To me, a summary that doesn't depend on data quality, like the F2-distance in the reference space (i.e. the sum of all F4-statistics, or an orthogonalized version thereof) would be easier to interpret. At the very least, it would be nice to show some intermediate results of this clustering step on at least a subset of the data, so that the reader can verify that the qpWave-statistics and their resulting p-values make sense.

The methodological concerns lead me to some questions about the data analysis. For example, in Figure 2, Supp 2, very commonly outliers lie right on top of a projected cluster. To my understanding, apart from using a different reference set, the approach using qpWave is equivalent to using a PCA-based clustering and so I would expect very high concordance between the approaches. One possibility could be that the differences are only visible on higher PCs, but since that data is not displayed, the reader is left wondering. I think it would be very helpful to present a more detailed analysis for some of these "surprising" clustering where the PCA disagrees with the clustering so that suspicions that e.g. low-coverage samples might be separated out more often could be laid to rest.

One way the presentation could be improved would be to be more consistent in what a suitable reference data set is. The PCAs (Figure 2, S1 and S2, and Fig6) argue that it makes most sense to present ancient data relative to present-day genetic variation, but the qpWave and qpAdm analysis compare the historic data to that of older populations. Granted, this is a common issue with ancient DNA papers, but the advantage of using a consistent reference data set is that the analyses become directly comparable, and the reader wouldn't have to wonder whether any discrepancies in the two ways of presenting the data are just due to the reference set.

PCA over time

It is a very interesting observation that the Fst-vs distance curve does not appear to change after the bronze age. However, I wonder if the comparison of the PCA to the projection could be solidified. In particular, it is not obvious to me how to compare Figure 6 B and C, since the data in C is projected onto that in Figure B, and so we are viewing the historic samples in the context of the present-day ones. Thus, to me, this suggests that ancient samples are most closely related to the folks that contribute to present-day people that roughly live in the same geographic location, at least for the middle east, north Africa and the Baltics, the three regions where the projections are well resolved.

Ideally, it would be nice to have independent PCAs (something F-stats based, or using probabilistic PCA or some other framework that allows for missingness). Alternatively, it could be helpful to quantify the similarity and projection error.

I have the following comments that pertain to the introduction.

Introduction:

I do agree that there is an ancient DNA sampling gap between the end of the Bronze age and the present day, and it is an interesting question to ask how bronze-age folks relate to present-day people. However, I don’t follow why the finding that present-day people are well-modelled as a three-way mixture of bronze-age groups would suggest demographic stability.

Within Western Eurasia, wouldn’t any demographic model with limited outside influences still maintain the principle of three-way mixtures? Do the authors mean to state that they believe that present day geographical genetic variation is mapping to the geographic genetic variation which existed ~6000 years ago? If so, then they should explicitly cite the studies and regions for which this has been established. In any case, this statement should be better motivated. Since this, to me, is an interesting finding of the present work (Figure 6) this might be better moved to the discussion.

Reviewer #2 (Recommendations for the authors):

Antonio, Weiss, Gao, Sawyer, et al. provide new ancient DNA (aDNA) data for 200 individuals from Europe and the Mediterranean from the historical period, including Iron Age, Late Antiquity, Middle Ages, and early modernity. These data are used to characterize population structure in Europe across time and identify first-generation immigrants (roughly speaking, those who present genetic ancestry that is significantly different from others in the same archaeological site). Authors provide an estimate of an average across regions of >8% of individuals being first-generation immigrants. This observation, coupled with the observed genetic heterogeneity across regions, suggests high mobility of individuals during the historical period in Europe. In spite of that, Principal Component Analysis (PCA) indicates that the overall population structure in Europe has been rather stable in the last 3,000 years, i.e., the levels of genetic differentiation across space have been relatively stable. To understand whether population structure stability is compatible with a large number (>8%) of long-distance immigrants, authors use spatially-explicit Wright-Fisher simulations. They conclude these phenomena are incompatible and provide a thoughtful and convincing explanation for that.

Overall I think this manuscript is very well written and provides an exciting take-home message. The dataset with 200+ novel ancient human genomes will be a great resource for population genetics and paleogenomic studies. Methods are robust and well-detailed. Although the methods used are well-known and standard in the field of paleogenomics, the way the authors use these methods is very creative, insightful, and refreshing. Results provide a comprehensive and novel assessment of historical population genetic structure in Europe, including characterizing genetic heterogeneity within populations and interactions/migration across regions. Conclusions are fully supported by the data.

A few of the strengths of this manuscript are its dataset containing a large number of ancient human genomes, the novel insights about human migration provided by the results, the creative approach to characterize migration and population structure across time using aDNA, and the excellent figures describing research results. I see no major issues with this paper.

1) I miss a table with the information regarding the published data, including sample size per region, per period, and source. On a related note, I miss the references to the papers that originally reported the public data being used in this manuscript. The manuscript cites AADR, but as per the AADR website, the individual papers that originally reported the data must be cited when AADR is used. It reads: Researchers who wish to use this compilation as the basis of their publications should cite this website and release version (e.g. "Allen Ancient DNA Resource [website]", version 50.0), while also citing the individual papers that report the data for each of the individuals they analyze. As an author of paper(s) that have originally reported data used in this manuscript, I believe we deserve to have our work acknowledged by users of the AADR compiled dataset and our papers cited. (forgive me if you have already done so and I missed it).

2) Figure 6C depicts the results of a PCA with ancient individuals projected onto present-day ones. Ancient (panel B) and present-day individuals (panel C) present similar spatial structures. I wonder if this is because ancient individuals were projected onto present-day ones. Have you tested whether a PCA with ancient individuals (perhaps a subset with a good breadth of coverage) also recovers the structure observed for present-day individuals? Forgive me if I missed it, but it would be nice to see a PCA plot for the three different historical periods showing the observed population structure is similar across time.

3) I don't see the number of variants observed in the simulations. I see that the simulated chromosome is 1e8 Mb long, but I don't see any mention of the number of observed variants. Perhaps I missed it – please let me know. I strongly suggest that you add this information to Figure 7 caption. I wonder if the different simulation scenarios could result in different numbers of variants being analyzed in each case and therefore different power to detect population structure using PCA (Figure 7).

4) Page 21, line 2: I'm surprised CpG sites are only 15% of the data. I had the impression that CpG sites accounted for ~2/3 of the 1240K dataset, but it's totally possible that you are correct. Please check if these numbers are accurate.
