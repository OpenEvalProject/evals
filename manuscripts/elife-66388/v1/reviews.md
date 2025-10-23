# Peer review - Round 1

Editors:
- Peter Rodgers, eLife United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66388.sa1](https://doi.org/10.7554/eLife.66388.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Meta-Research: Lessons from a catalogue of 6674 brain recordings" to eLife for consideration as a Feature Article. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by the eLife Features Editor (Peter Rodgers). The following individuals involved in review of your submission have agreed to reveal their identity: Peter Kohler (Reviewer #1); Cyril Pernet (Reviewer #3).

The reviewers and editor have discussed the reviews and drafted this decision letter to help you prepare a revised submission. While the reviewers were largely positive about your manuscript, there are quite a few important points that need to be addressed to make the article suitable for publication.

Summary

This manuscript comes from a group in Liverpool who for the last decade have used event-related electroencephalography (EEG) to measure a brain response known as the sustained posterior negativity (SPN). The SPN provides a readout of processing of symmetry and other types of visual regularity. The goal of the current paper is not to offer new information about the role of symmetry in visual perception, but rather to provide a meta-analysis of scientific practice based on the thousands of studies, published and unpublished, accumulated by the authors over the years. The authors use this rare dataset to evaluate their own performance on four key concerns that are known to lead to irreproducible results. The conclusions the authors make about their own scientific practice are largely supported by the data, and the findings offer some recommendations on how to best measure the SPN in future studies. The authors succeed in providing an even-handed estimate of the reproducibility of their research over the last 10 years but are less successful in generalizing their conclusions.

The main strength of the manuscript is the data set, which contains every SPN study ever recorded at the University of Liverpool – more than 6000 recordings of the SPN from more than 2000 participants. The authors have obviously put substantial effort into cleaning up and organizing the data and have made the dataset publicly available along with analysis tools. As such, the data represents a herculean exercise in data sharing and open science and should inspire EEG researchers who are interested in following best practices in those domains. Another strength of the paper are the analyses of publication bias and statistical power, which are quite well-done and fairly unique, at least for EEG research.

The dataset clearly has value in itself, but the potential broader interest of the manuscript depends critically on what the authors do with the data and to what extent their findings can provide general recommendations. The main weakness is that the findings are fairly specific to the measurement modality and brain response (SPN) measured by the authors. In my reading there is generally little attempt to relate the conclusions to other event-related EEG signals, much less to other EEG approaches or other measurement modalities. The sections on Publication Bias and Low Statistical Power are arguably inherently difficult to generalize beyond the SPN. The section on P-hacking, however, is directly limited in impact by analyses that are either very simplistic or missing entirely. The electrode choice section attempts to evaluate the impact of that particular approach to dimensionality reduction, but that is only one of many approaches regularly used in EEG research. The authors discuss that the selection of time window is an important parameter that can influence the results, but there is no actual analysis of the effect of time window selection across the many studies in the dataset. Finally, the analysis of the effect of pre-processing in the same section is also fairly limited in impact, because only one experiment is reanalysed, rather than the whole dataset.

In conclusion, the manuscript will clearly be of interest for the relatively narrow range of researchers who study the SPN using event-related EEG. In addition, the dataset will serve as a useful example of large-scale curated sharing of EEG data. Beyond that, I think the impact and utility of the manuscript in its current from will be relatively limited.

Essential Revisions

1 Data sharing

We encourage the authors to make their data available in a way that is FAIR. As it stands the data are Findable and Accessible, but not much Interoperable or Reusable. For example, using BIDS elecrophysiological derivatives and given the authors experience with EEGLAB, they could use the.set format along with a flat structure and proper metadata (particiants.tsv, data_description.json, channels.tsv, electrodes.tsv, etc.) For more detail, see: https://docs.google.com/document/d/1PmcVs7vg7Th-cGC-UrX8rAhKUHIzOI-uIOh69_mvdlw/edit; Pernet et al., 2019; bids.neuroimaging.io.

Many of these can be done using matlab tools to generate data (https://github.com/bids-standard/bids-starter-kit and https://github.com/sccn/bids-matlab-tools).

https://github.com/bids-standard/bids-matlab could be used to make analysis scripts more general.

Do reach out to the BIDS community and/or myself [Cyril Pernet] if you need help.

A classification of experiments could also be useful (using, say, the cognitive atlas ontology [https://www.cognitiveatlas.org/]).

2 Introduction

a) The introduction needs to better explain the SPN – how it is generated, what it is suppose to reflect/measure, how the potential is summarized in a single mean, etc.

b) Please add a paragraph at the end of the introduction telling readers more about the data, how they can get access to them, how they can reproduce your analyses, and what else it is possible to do with the data.

3 Figures

a) Related to the previous point, figures 1-3 are of limited usefulness to the reader. Please replace them with a single figure that includes a small number of illustrative SPN waves and a small number of illustrative topographic difference maps to clarify the explanation of the SPN (see previous point). Please include no more than four panels in reach row of the figure, and please ensure that the caption for the new figure 1 adequately explains all the panels in the figure.

b) The present figure 1 can then become Figure 1—figure supplement 1, and likewise for the present figures 2 and 3.

c) Please consider grouping the panels within each of these three figure supplements according to, say, a cognitive atlas ontology [https://www.cognitiveatlas.org/] (or similar).

d) Also, for the difference maps, please consider avoiding jet and using instead a linear luminance scale (eg, https://github.com/CPernet/brain_colours).

e) Figure 4b. Please delete the bar graph in the inset and give the three mean values (and confidence intervals) in the figure caption.

f) Figure 6. Please delete the bar graph (panel C) and give the four mean values (and confidence intervals) in the figure caption.

4 More complete reporting

a) Please include a table (as a Supplementary file) that provides information about the electrodes and time windows used in each of the studies. If the electrodes and/or time windows varied across the SPN waves within a study, please explain why.

b) Along similar lines, what stimulus types and tasks were used for what fraction of the SPNs in the dataset? SPNs can be measured for many types of regularity and varies with both stimulus parameters and task (as noted by the authors). This means that the SPN varies across studies not just by neural noise and measurement noise, but also by differences in neural signal. This is not necessarily a weakness of the analyses reported here, but it should be noted, so please include a table (as a Supplementary file) that provides information about the stimulus types and tasks used in the studies.

5 Further analyses

a) The Electrode Choice analysis estimates the effect of a priori selection of electrode ROIs, by comparing three such ROIs, each a smaller subset of the other. Perhaps not surprisingly the responses are highly correlated, and the overall effects change little. I would recommend considering more data-driven approaches to spatial filtering and dimensionality reduction. There are many such approaches, but two that come to mind are reliable components analysis (Dmochowski et al., 2012; Dmochowski et al., 2014; Dmochowski and Norcia, 2015) and non-parametric spatiotemporal clustering (Maris and Oostenveld, 2007). It would be interesting to see if approaches such as these would produce different effect sizes or identified a different set of electrodes across the many studies in the dataset. This could also serve as an assessment of the ability of these methods to identify the same spatial filters / clusters of electrodes across a large dataset. Given that these methods are widely used in the EEG/MEG-community, this would considerably enhance the impact of the manuscript. The spatiotemporal approach could also help address the time window selection issue, as outlined in my next point.

b) The authors acknowledge that the selection of time window is an important parameter that can influence the results, but do not include any analysis of this. Please include an analysis of the effect of time window selection across the many datasets. Also, please comment on how it is possible to measure and separate early and late effects using event-related EEG.

c) The analysis of the effect of pre-processing is also of potential broad interest to researchers doing EEG, but it is limited in impact, because only one study is re-analyzed. I understand that it may be impractical to re-analyze every study in the dataset 12 different ways, but re-analyzing a single dataset seems to have limited utility in the context of the current manuscript. Please either extend this analysis or remove it from the manuscript.

d) Re pre-processing pipelines, please consider discussing some of the recommendations in Pernet et al. [doi.org/10.1038/s41593-020-00709-0]

6 Limitations associated with using data from just one group.

The overall approach to the cumulative research program and the specific suggestions to reduce the experimental bias and improve researchers' self-awareness is indeed helpful but in line with the previously known findings on reproducibility limitations. Furthermore, a re-analysis, which specifically relies on single site single group acquisitions, poses additional issues or specific bias (e.g., data acquisition, methodology, experimental design, data pre-processing, etc.) to the generalizability of the results that the authors should have considered. A comparison with an independent sample of data would make the analysis less autoreferential and methodologically stronger. If possible, please include a comparison with an independent sample of data: if such a comparison is not possible, please discuss the limitations and potential biases associated with using data from just one group.

7 Awarding grades

The authors grading their work does not bring anything to our understanding of reproducibility; please remove.

8 Advice for other researchers

The manuscript currently has a strong focus on SPN research and in places almost reads like a 10-year report on scientific practice within a specific research group. This is undoubtedly valuable, but of limited general interest. So, I hope the authors will forgive an open-ended suggestion. Namely that they carefully consider the ways in which their findings might be valuable to researchers outside their own sphere of interest. I have suggested a few ways above, but perhaps the authors can think of others. What recommendations would the authors make to scientists working in other domains of brain imaging, based on the findings?

9 Publication bias

a) Line 145. "A meta-analysis based on the published SPNs along would overestimate...". It is essential that you perform such a meta-analysis. What you have done is compare the means computed from all vs. published, but not set-up a meta-analysis in which the mean is estimated from the means and variances of published studies alone (I suggest dmetar which is super easy to use even if you never used R / R-studio before; https://bookdown.org/MathiasHarrer/Doing_Meta_Analysis_in_R/). That extra analysis will be very useful because, people do not have access to the data to compute the mean and thus use this meta-analytical approach (how much this will differ from -1.17uV?; in theory it should bring the results closer to -0.94uV)

10 Low statistical power

– Power analysis: You need to explain better the analysis. It is also essential that you demonstrate that a 2nd order polynomial fits better than a 1st order using AIC and RMSE. A second aspect is that you cannot predict effect size from amplitude because the polynome you have was obtained for the entire dataset. This is a typical machine learning regression setting: you need to cross-validate to produce an equation than generalizes -- given the goal is to generalize across experiments, a natural cross validation scheme would be the experimental belonging (fit all data but one experiment, test – iterate to optimize parameters).

– Nonlinearity: to further look into that question you need the complementary plot Cohens'd vs. variance (or 3d plot d, variance, amplitude but sometimes it's hard to see). Given that d = mean/std, the nonlinearity arises because there is a 'spot' where variance behave strangely (likely for the midrange amplitude values). This also relates to your discussion on the number of trials because the number of trials increases precision and in principle reduce between subject variance; depending on expected amplitude the number of trials should therefore be adjusted to reduce variance bias.

11 Miscellaneous

a) Please provide links to the code for the analysis presented in the paper.

b) Please consider making the data-viewing app agnostic wrt operating system.

c) Re the headline effects reported in figure 5: the explanation of these effects in the in the repository needs to be more detailed.

d) Line 148. Please say more about the reasons why 68 SPNs "will likely in the file drawer forever".

e) Line 191 onwards. When talking about pilot studies please add references (for instance Lakens (doi.org/10.1016/j.jesp.2017.09.004). Also, please consider discussing the smallest effect size of interest instead of absolute effect size.
