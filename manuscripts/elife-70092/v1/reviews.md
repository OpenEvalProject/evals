# Peer review - Round 1

Editors:
- Adrien Peyrache, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70092.sa1](https://doi.org/10.7554/eLife.70092.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper describes an open-source, high accuracy, and easy-to-use toolbox for automatic sleep scoring. The toolbox also includes a set of graphic tools to visualize raw and processed data as well as scoring performance, which will be of great help for the community.

Decision letter after peer review:

Thank you for submitting your article "A universal, open-source, high-performance tool for automated sleep staging" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Büchel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Sophie Bagur (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

This study describes an automatic sleep scoring tool, which classifies features extracted from the EEG signal using state-of-the-art machine learning techniques. The algorithm (YASA) was trained and validated on a large dataset including healthy subjects and patients, from various ethnicities and at different age. The algorithm offers a high level of sensitivity, specificity and accuracy matching or sometimes even exceeding that of typical interscorer agreement. While this open-source tool will certainly benefit the field, the three reviewers have raised major concerns that need to be addressed. The essential revision requirements are listed below, please refer to the reviewer's comments for further details.

1) The study does not cite the work of Stephansen et al., (Stephansen et al., Nature Communications 2018, doi: 10.1038/s41467-018-07229-3) in which several interesting approaches were proposed. As the same public data were used, YASA could (and certainly should) be benchmarked against this work. More generally, a short review of the existing tools, their performance and accessibility would be a welcomed addition to the introduction.

2) The performance of the algorithm (YASA) seems to be reduced when inter-human scorer confidence is low. It would be interesting to the reader to understand the underlying reasons: does it happen when states are stable or during transitions? Is there a relationship between YASA and human confusion matrices? How does the performance vary with human confidence during sleep apnea? For misclassified epochs, is the confidence lower in all stages? In the case of an error, is the second-highest probability typically the correct one?

3) The algorithm performs worse on N1 stage, older individuals and patients presenting sleep disorders (sleep fragmentation). It would be helpful to add a section to the manuscript with some considerations on how accuracy could be improved for these different issues. Finally, would it be possible to determine the origin of the accuracy variability? Do low and high accuracy sessions differ in some aspects?

4) As YASA usually performs poorly on fragmented sleep data (as acknowledged by the authors), it would be interesting to present the results of the validation test separately for the healthy volunteers (N-25) and the patients (N=55).

5) Nights were cropped to 15 minutes before and after sleep to remove irrelevant extra periods of wakefulness or artefacts on both ends of the recording. This represents an issue for the computation of important sleep measures such as sleep efficiency and latency as the onset/offset of sleep might be missed.

6) Using 30s epochs seems unnecessary with current computing resource, and this could potentially affect the resolution of the scoring. Along the same lines, using a 5min long smoothing window is not justified and may affect the resolution of transition times, especially during N1. Finally, smoothing should perhaps be assymetrical and restricted to the preceding period, not the following.

7) The study should provide more detailed regarding how the algorithm was prevented from overfitting. Furthermore, it is unclear which features were used exactly whether the features used by the algorithm can be changed by future users, this would be an interesting addition.

8) The algorithm was trained on nighttime sleep data thus cannot be immediately compared to daytime (nap) sleep scoring. It is therefore unjustified to use the word "universal" in the title.

Reviewer #1 (Recommendations for the authors):

Details of algorithm predictions:

The authors provide some evidence that the YASA algorithm tends to be mistaken and have low confidence when human inter-scorer variability is high but they only focus on transition periods. The readout of the algorithm's confidence is an interesting tool to assess this. It would therefore be useful for the authors to more systematically explore whether it is related to human scored agreement:

– Correlate epoch by epoch confidence with inter-scorer agreement both for transition and stable periods.

– YASA underperforms on sleep apnea patients, is the confidence also lower and human inter-scorer reliability lower?

– How well do YASA confusion matrices match inter-scorer confusion matrices?

The overall performance of the algorithm is well within the range of the state of the art. It would however be useful to provide some insight into why and how the algorithm fails for those data points with lower accuracy (<70%):

– Does the overall confidence of the algorithm predict the overall accuracy of a given night of sleep? If so this could allow users to exclude untrustworthy nights from further analysis.

– Since accuracy varies between 90 and 65% could the authors show where this variability occurs? (ie general change in accuracy or specific sleep stages more impacted than others).

– It would be useful if the authors could provide as a supplement example predicted and ground truth hypnograms for high, low and median accuracy levels.

Possible algorithm extensions:

The use of 30s epoch is a historical quirk and a way of lightening the load on human scorers but ceases to be relevant for automated scoring, particularly given the problem arising from epochs at transition periods (ex: sleep apnea patients). The possibility of smaller windows ore sliding 30s epochs could potentially refine sleep analysis. Implementation and investigation of this may be beyond the scope of the manuscript but I feel this advantage should be at least discussed.

Methodological details:

The smoothing window used by the authors (5min) seems quite large. Such a long window could be detrimental in cases of fragmented sleep (ex: sleep apnea patients). The authors claim this allows for an optimal compromise between short and long term dynamics. Could the authors back up this claim from the literature or their own model fitting?

The parameters used for the GBM classifier are said to be chose to prevent overfitting. How was this assessed? Did the authors perform a hyperparameter search by splitting the training data set?

The YASA framework allows for artefact removal, was this step performed on the data before running the sleep staging algorithm?

Please provide a definition of the Shapley value in the methods section.

Reviewer #2 (Recommendations for the authors):

1. As mentioned in the previous section, I am very surprised that the work of Stephansen et al., (Stephansen et al., Nature Communications 2018, doi: 10.1038/s41467-018-07229-3) is not cited. It is extremely relevant as Stephansen et al., also used a large amount of public data to train and test an automated sleep scoring algorithm (based on neural networks). They are very similar ideas developed in this article (for example they also introduced the use of probabilistic scoring with hypnodensities). Some ideas could also be worth implementing with the proposed algorithm such as testing the impact of common sleep disturbances or shortening the epoch window. Finally, most if not all the data used in Stephansen et al., are available on the SleepData.org platform (used by the authors) so the authors could directly benchmark the performance of the two approaches. From my personal experience, Stephansen algorithm has three disadvantages compared to the present algorithm: (i) it is slower and heavier, (ii) it requires python machine-learning packages such as TensorFlow, which are frequently updated, (iii) it is very difficult to modify and understand how it works (black box). I think it would be interesting for the authors to show how their approach could mitigate these issues.

2. The tool would greatly benefit from a graphical interface to install and use the software. Another interesting function could be to process a list of EDF files (for example, all the EDF files in a given folder). From personal experience again, an automated sleep scoring algorithm will not be used in clinical settings at a large scale without a GUI.

3. I think the algorithm will be closer to the current consensus if the smoothing was restricted to preceding and not following epochs. Also, could the authors examine the impact of the duration of the smoothing period on performance? A too large smoothing might decrease the performance for transitory stages such as N1.

4. Since the proposed algorithms can provide a probabilistic score, it would be interesting to explore further the differences between the human gold-standard scores and the algorithm. For example, for misclassified epochs, is the confidence lower in all stages? In the case of an error, is the second-highest probability typically the correct one? Related to the same point, when writing "for epochs ﬂagged by the algorithm as high-conﬁdence ({greater than or equal to}80% conﬁdence) than in epochs with a conﬁdence below 80%", can the authors indicate the % of epochs {greater than or equal to} and < to 80% confidence? Could the authors show the distribution of these confidences per sleep stage?

5. In the "Descriptive Statistics" section, could the authors add a table assessing the difference between the training and test sets for the variables mentioned in the text?

6. How was the AHI obtained? Was it provided for each dataset and individual or computed by the authors?

7. "These results match recently developed deep-learning-based algorithms for automatic sleep staging (Guillot et al., 2020; Perslev et al., 2021)." Citing the Stephansen paper is important here, especially since the authors could apply their algorithms to the same data. Also, the Stephansen studies should be cited when discussing the advantage of a probabilistic scoring (they coined the term hypnodensity).

8. Out of curiosity, could the list of features used by the algorithms be changed by future users? This could be an interesting feature for future developments.

Reviewer #3 (Recommendations for the authors):

In this study, Vallat and Walker describe a new sleep scoring tool that is based on a classification algorithm using machine-learning approaches in which a set of features is extracted from the EEG signal. The algorithm was trained and validated on a very large number of nocturnal sleep datasets including participants with various ethnicities, age and health status. Results show that the algorithm offers a high level of sensitivity, specificity and accuracy matching or sometimes even exceeding that of typical interscorer agreement. Importantly, a measure of the algorithm's confidence is provided for each scored epoch in order to guide users during their review of the output. The software is described as easy to use, computationally low-demanding, open source and free.

This paper addresses an important need in the field of sleep research. There is indeed a lack of accurate, flexible and open source sleep scoring tools. I would like to commend the authors for their efforts in providing such a tool for the community and for their adherence to the open science framework as the data and codes related to the current manuscript are made available. I predict that this automated tool will be of use for a large number of researchers in the field. I also enjoyed reading the paper that is nicely written. However, I have some concerns listed below that need to be addressed and I also provided comments that might help improving the overall quality of the paper.

– There are some overstatements that need to be toned down.

– In the title, the word "universal" should be removed. The tool was trained and validated on nocturnal sleep data. Sleep characteristics (eg duration and distribution of sleep stages etc.) are different, for example, during diurnal sleep (nap) and the algorithm might not perform as well on nap data. Note that there is a large number of scientific studies in which diurnal, instead of nocturnal, sleep paradigms are used as these paradigms are easier to implement in lab settings. The algorithm being optimized for nocturnal sleep (with eg the definition of specific sleep stage weights that are specific to nocturnal recordings), it is unknown how it would perform on nap data for example.

– In the abstract, the following sentence needs to be altered: "This tool offers high sleep-staging accuracy matching or exceeding human accuracy". Exceeding human accuracy might be misleading as human scores are used as the ground-truth in the validation process. The algorithm exceeds the accuracy of some human scorers and matches the scores of the best scorer.

– Acknowledgement of – and comparisons to – already available tools in the field

There are plenty of automated sleep scoring tools available in the field (most of them are not open source and rather expensive though – as noted by the authors). A short review of the existing tools, their performance and accessibility would be a welcomed addition to the introduction. In line with this comment, other published algorithms were tested on the same set of data used to train and validate the present algorithm. The authors refer to their work for comparison between algorithms but it would be a very nice addition to the paper to provide (and test for) such comparisons. It is currently unclear whether the present algorithm performs any better than algorithms already available in the field.

– Further improvements

The algorithm performs worse on N1 stage, older individuals and patients presenting sleep disorders (sleep fragmentation). It would be helpful to add a section to the manuscript with some considerations on how accuracy could be improved for these different issues. Eg, should one consider training the algorithm on older datasets in order to improve accuracy of scoring when studying aging? Same applies to sleep disorders. It is currently unclear whether the variety of datasets used to train the algorithm is beneficial in these cases.

In the same vein, as algorithms usually perform poorly on fragmented sleep data (as acknowledged by the authors), it would be interesting to present the results of the validation test separately for the healthy volunteers (N-25) and the patients (N=55).

– Justification for some methodological choices

– Nights were cropped to 15 minutes before and after sleep to remove irrelevant extra periods of wakefulness or artefacts on both ends of the recording. This represents an issue for the computation of important sleep measures such as sleep efficiency and latency as the onset/offset of sleep might be missed.

– How were features selected? A description of the features needs to be provided. Which features were Z scored exactly and why not all?

– The custom sleep stage weights procedure is unclear. Why was only a sub-sample used to determine best weights?

– Was the smoothing done with 5min or 15min rolling average? While it is critical to include this temporal window, it looks rather wide. Human scorers usually don't go that far back when scoring but usually just a few epochs (ie 2-3 which is 1min30). What was the rational for choosing such a wide temporal window?

– It is currently unclear when / how the EEG and EMG data were analyzed.
