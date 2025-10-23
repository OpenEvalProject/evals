# Peer review - Round 1

Editors:
- David Kleinfeld, University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34518.014](https://doi.org/10.7554/eLife.34518.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "A spike sorting toolbox for up to thousands of electrodes validated with ground truth recordings in vitro and in vivo" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor.

Your work is of particular interest based on the rarity of ground truth data for spike sorting. Unfortunately, the reviewers had mixed feeling about the depth and clarity of the data and voice some significant concerns that speak against publication. The chief concern is that the ground truth data for the MEA is limited to the 7 cells for sorting errors less than 20% (Figure 2C; see comment by reviewer 1). In fact, the example (presumably one of the seven points) in Figure 2B suggests that a given cell goes not contribute a waveform to many electrodes (as implied in Figure 1; see additional comment by reviewer 1). Thus the necessity as well as utility of the algorithm seems unmotivated as it stands. Another weakness, discussed by reviewers 1 and 2, is that the merging of clusters is "by hand", although there is precedent in the literature (Fee et al. 1997) for automatic merging based on avoiding events at equal time in the autocorrelation of the merged clusters. Finally, all reviewers and the Reviewing Editor find the presentation confusing or lacking. Material is not presented in a logical order, details of the algorithm as glossed over, etc.

All reviewers felt that the topic of the manuscript is timely. We understand that you may wish to take this manuscript elsewhere at this time. On the other hand, if you agree with the reviewers, we would be willing to consider a revised manuscript with a larger useful data set and with a means for automation of the merging of clusters, without assurance that the revision would be successful.

Reviewer #1:

These authors report their method to do classic spike sorting, creation of single neuron spike time records, from multisite recording. They report results on both multielectrode arrays, used to record in vitro from retinal tissue, and Si probes, used to record in vivo, most frequently from rodents. Their method has been previewed on bioRxiv for some time so there is some public information comparing performance of this method to existing and other recently developed packages. While the technical treatment is thorough, I find the paper confusing, in large part because of the bifurcation of the Materials and methods and the remainder of the paper. To begin, the authors say "those snippets are detected, they are projected in a feature space of lower dimension". What feature space. Ten pages later I find out PCA. How many dimensions, either 5 or 6 depending on the parts of the algorithm. Without comment, the templates are 57 sites. This seems exceptionally large, perhaps usual for MEA recording. The choice of size deserves a clear comment.

I commend the authors on their contribution of "ground truth" MEA data. The field is seriously deficient in reference data and this deficiency impairs progress in the computational problem at hand. Figure 2A and B are commendably clear. I find 2C to be puzzling. I would assume only the inset of retina in vitro is of any interest to the practitioners of neural recording. Error rates above 20% are of no practical utility but occupy 95% of the plot. Alternatively only 1 data point in the in vivo plat is useful. This result is not surprising given the traces in 2B. Peak to peak noise is ~10-12 uV. The usual peak threshold is 3.5-5 x RMS or 12-15 uV. As such, one would not expect to sort signal below that amplitude. With the authors template matching routine, it can be argued that smaller signals can be found but they are buried in noise, again as Figure 2C seems to illustrate. I am left wondering what 2C teaches, except, that sorting has failed in most of the conditions plotted. Does this not call into question the success of the strategy of finding template pools at high amplitude then matching those templates to the raw traces? If that is not the lesson, then the authors need to clarify the value of plotting so many failed sorting exercises. I fail to understand the value of a 50% classification error that matches the optimal classification rate. I would conclude the experiment has failed to produce adequate usable data. Further, the authors choose to compare their sorting accuracy to a previously defined metric, Best Ellipsoidal Error Rate. Harris, 2000, the original source defines this measure as "This measure was designed to estimate the optimal clustering performance for a given set of feature vectors by searching over all possible ellipsoidal cluster boundaries." Is not the principal weakness of the methods of Harris reported there and later an assumption that a cluster is well described by ellipsoidal boundaries? The authors should justify this assumption in the reference data sets. I see no a priori reason that their data should be so constrained, although the "ground spikes" may be.

In the Discussion, especially Figure 3, trends are difficult to understand. For 3A, the plot seems to argue a superlinear dependence on processor count, 6 processors taking 1/30th the time of 2 processors. This seems implausible. Would this plot be more informative on a log time scale without a trend-line. The current plot implies that 10 processors would digest the data in negative time! 3B is much more informative, showing 400 channels would take ~20 hours of computation for 1 hour of recording. While an improvement over many current methods, is not the method of Pachatariu et al., reference in this manuscript as a bioRxiv but now also published in Advances In Neural Information Processing Systems 4448-4456 (2016). The GPU based system reported their quotes "First, we timed the algorithm on several large scale datasets. The average run times for 32, 128 and 384 channel recordings were 10, 29 and 140 minutes respectively, on a single GPU-equipped workstation". While they did not quote the duration of the recording or the total number of neuronal event (a better metric of the computation burden) it seems far faster than the ~30 hours in the present manuscript. Both of the packages are available in the public domain so a direct comparison is a reasonable request. In Figure 3E, the authors plot data ranging from 0 to 15% (including error bars) to 50% full scale. Why not use the full plot height for 15%. Same comment for 3F.

Finally, the authors freely admit their strategy over segments but offer a combination of an automated merging tool as well as a "dedicated GUI" for manual merging. This reviewer did not implement that interface so I cannot comment directly on performance or ease of use. In the Materials and methods section, they describe in detail the method for correlation, but they do no show the error rate as a function of the parameters used for that merging.

In summary, I am undecided. The authors use an admirable amount to "ground truth" data, both their own and that available publicly. Unfortunately, all of these data are inadequate to the problem since the known cells are so few and in the experimental data of such low amplitude yield a residual question of performance remains. This manuscript reports a novel combination of strategies but does not appear to exceed in performance or speed other recently published packages. More than one option is probably justified based on different needs of data sets, but that optimum path is difficult to discern from this manuscript of other published data. Reporting the method is a service to the community and justified in journal space, especially for an online journal such as eLife.

Reviewer #2 (General assessment and major comments (Required)):

In this report, the authors present a new approach to spike sorting that they claim is scalable to thousands of electrodes. This a very timely report as there is renewed interest in spike sorting thanks to the new electrode technologies. However, I find this report to be mixed in terms of strength of the proposed solution and clarity with which the underlying claims are made.

The strength of the proposed solution is significantly under-cut by the need for manual cluster merging. This is a really major limitation. Clustering of thousands of electrodes has to be automatic if it is to be genuinely scalable. I can imagine it would take a long time for someone to check thousands of recordings and merge, especially if they are not an expert.

The authors cite several algorithms that are designed to scale and says they are untested. This is a fair point, but why don't they test them with their ground truth data and compare the results? This would seem to be an important issue for the reader to assess the value of the proposed work in the context of the cited literature.

The Introduction implies that the spike sorting problem has been addressed for small numbers of contacts, but does not include any citations to support the point. What forms of the classical approach that the authors are referring to? I would claim that despite a great deal of attention it is not the case that low-density sorting has been solved. The high density electrode case that the authors focus on here presents new challenges but the authors need to acknowledge the known limitations of low-density approaches.

A novelty of the proposed approach is that it claims to address the superposition problem but how well this works is not demonstrated or discussed. I think the work would be strengthened if this aspect received more attention.

Reviewer #3:

This manuscript presents a novel resource for automated spike sorting on data from large-scale multi-electrode recordings. The authors present new strategies for tackling large recordings with hundreds to thousands of electrodes while being able to integrate information from multiple electrodes and to disentangle overlapping spikes from multiple neurons. Thus, the resource addresses fundamental issues of spike sorting. Given the current development of recording systems with hundreds to thousands of electrodes and the paucity of methods targeted to such data sets, the presented method should therefore make a timely and very strong contribution to the field of multi-electrode recordings.

The approach appears to be well thought-through and apparently guided by much practical experience with spike-sorting issues. The manuscript is accompanied by freely available software that can be downloaded from the authors' website, and the software appears to be well documented and versatile in that it can be run on different operating systems, using different hardware configurations, with straightforward parallelization. Moreover, the authors test their spike-sorting approach on ground-truth data by combining their extracellular multi-electrode recordings with the intracellular recording of individual neurons, a laudable effort. They generally find that their automated spike sorting performs nearly as well as an "optimal classifier", obtained by supervised learning of an elliptical decision boundary in the space of raw electrode signals. The authors also make this ground-truth data available, which will be a great asset available to future developments of spike sorting approaches.

My only concerns therefore relate to the presentation of the material. Given that this is a presentation of a spike sorting resource, it seems mandatory that the computational approach and the technical aspects of the algorithm be explained as thoroughly and clearly as possible so that readers and users can fully understand the approach and adjust it to their own needs by tuning the appropriate parameters. In the Results part, the explanation of the algorithm is rather brief, and it would here be useful to provide a bit more of an intuitive description of the approach (see detailed points below). The Materials and methods section, on the other hand, appears to contain some inaccuracies and small omissions of detail that make it hard to follow some of the steps.

1) The Results part is a bit sparse on explaining the approach, although this would be a nice opportunity to lay out concepts without the need for technical details. For example, it might be useful to provide some brief explanations of why limiting the clustering to the search for centroids is less demanding and what the approach in density-based clustering is. Furthermore, some explanation of what is meant by "clustering each group in parallel" would be helpful, including the strategy for finding the right number of clusters and merging templates and units when necessary.

2) One aspect that doesn't become clear in the main part is to what extent merging of units generally needs to be performed and how it was done for the results of Figures 2 and 3. The Materials and methods section states that several templates were used for comparison with ground-truth data. It would be useful to obtain some more information about this. Was this merging done with the GUI described in the Discussion? Was the merging done "blindly", that is, before comparison with the ground-truth data, or retrospectively? Was merging the norm or the exception?

3) A potential issue with automated spike sorting is that it might be difficult to judge the sorting quality of the obtained units, that is, how reliable the units are and to what degree one may expect contamination from other cells or missed spikes. Does the resource provide for any quality control? Useful simple statistics might be the normalized spike amplitude, the distance from other templates, the quality of the fits in the template matching phase, and the variability in the fitting parameters, but maybe the authors could also point out other ways of assessing sorting quality from their own experience of using their software.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your article "A spike sorting toolbox for up to thousands of electrodes validated with ground truth recordings in vitro and in vivo" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The manuscript has been improved but there are some remaining issues that must be addressed before acceptance. This is an important paper that will gain from clarity in the exposition and the correction of numerous typographical errors. Of note:

1) A table of symbols and their definitions will be of great help for the reader.

2) Confusion remains in the implementation of the original clustering process as detailed by the first reviewer. Simply, a clear delineation of the process to create a template and use the template should be completely defined pictorially as well as mathematically.

3) The reviewers identify other confusing issues, missing references, and the need to avoid "double counting" by using correlation of the same data set for both analysis and verification.

Please address each of the reviewer criticisms in a written reply that addresses each reviewer comment and notes all changes to the text. The revised manuscript will be assessed by the Reviewing editor.

Reviewer #1:

The authors have improved the clarity of the manuscript substantially. My prior concerns have been adequately addressed. In addition to the specific comments below I would ask for additions/clarifications on three subjects.

I) First, on the path of the computation: Figure 1 is clearly the axis for most readers to understand the spike sorting process. Having carefully read the revised text as well as the original, I am still not sure how the original clustering is done. For the step of template collection, the text seems to imply that there are N clustering steps for the N electrodes. If true, one expects that each neuron would be detected on 3-8 electrodes and thus there are 3-8 times more clusters than neurons at least. The content of 1 C implies that these very many clusters are reduced to a template with 57 site "snipets" that make up the template. However, the example of 1C is centered on a maximum amplitude transient. How those maximum amplitude "centers" for templates are found is not clear to me, nor is how the expected variation around that center accommodated. Perhaps it does not need to be, since the template field is large so even is the maximum amplitude site for a given spike is off center, there is still ample information to cluster. A clear delineation of this template creation and use process would be useful, especially if it can be done pictorially as well as mathematically. How are all these redundant units merged?

II) While reading the Materials and methods section especially, but also reading the manuscript, I was constantly looking back through the text for the definition of variables and symbols. Would it be possible for the authors to make a variable definition table so that a reader can have access in one place to be reminded of variable definition for all variables in the paper?

III) The use of BEER is much better explained, but it would be useful to discuss when this assumption of elliptical boundaries is unlikely true, such as bursting cells or electrode-tissue drift.

Reviewer #3:

Let me begin by stating that it is very worthwhile to have a publication that describes SpyKING CIRCUS, since it is one of a handful of tools aimed at the automated analysis of multielectrode data.

Some comments follow:

1) This paper needs significant proofreading/editing to make it more readable.

As an example, the second sentence in the second section (Results) is:

“First, spikes are being detected as threshold crossings (Figure 1A) and isolated the extracellular waveforms for a number of randomly chosen spike times.”

I know what the authors intend, but it is garbled.

2) The Results section contains a description of the algorithm. Is that the format eLife requires? It would be clearer to have sections on the Algorithm, experimental results, validation experiments, etc.

3) A distinguishing feature of the method is the ability to resolve overlapping spikes in large systems in a reasonably automatic fashion and makes this an interesting contribution.

4) Other groups have used artificial template/spike insertion as a way to validate the algorithm and some reference could be given (e.g. Rossant 2016, Chung 2017).

5) The authors use cross-correlograms in order to help automate the merging process. It should be noted that, as a side effect, one can no longer use cross-correlograms as a validation metric.

6) Equation 1 is very confusing. The authors should explain the double sum notation (why index over events and units)? I'm sure they have something in mind but I don't know what it is.
