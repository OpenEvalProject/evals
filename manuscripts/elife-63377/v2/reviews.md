# Peer review - Round 1

Editors:
- Mackenzie W Mathis, EPFL Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63377.sa1](https://doi.org/10.7554/eLife.63377.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

DeepEthogram introduces a new tool to the neuroscience and behavior community that allow direct from-video-to-actions to be automatically identified. The authors comprehensively benchmark and provide data that demonstrates the tool's high utility in many common laboratory scenarios.

Decision letter after peer review:

Thank you for submitting your article "DeepEthogram: a machine learning pipeline for supervised behavior classification from raw pixels" for consideration byeLife. Your article has been reviewed by 3 peer reviewers, including Mackenzie Mathis as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Johannes Bohacek (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Bohnslav et al., present a new toolkit and GUI for using video input to extract behavioral states (ethograms) using a set of established deep neural networks. They show their pipeline works on range of laboratory datasets, and provide metrics comparing network performance to humans. However, the reviewers all agreed there are several key revisions needed in order to support the main claims of the paper. These revolve around benchmarking, datasets, and a more careful handling of related work, limitations of such a software, and clarifying methods. We have collectively decided to send the individual reviews from each reviewer, and ask you address those (and perhaps combine where you see fit), but we urge you to focus in on the following points for your revision.

Datasets:

The reviewers each expressed concern over the simplicity of the datasets and the potentially limited scope of DeepEthogram in relation. For example, the authors claim these are difficult datasets, but in fact we feel they are not representative of the laboratory videos often collected: they have very static backgrounds, no animals have cables or other occluders. We would urge the authors to use other datasets, even those publically available, to more thoroughly benchmark performance in a broader collection of behaviors.

Benchmarking:

While DeepEthogram could be an important tool to the growing toolbox of deep learning tools for behavior, we felt that there are sufficiently other options available that the authors should directly compare performance. While we do appreciate that comparing to the "gold standard" of human-labeled data, the real challenge with such datasets is even humans tend not to agree on a semantic label. Here, the authors only use two humans for ground-truth annotation, but there is a concern of an outlier. Typically, 3 humans are used to overcome a bit of this limitation. Therefore, we suggest carefully benchmarking against humans (i.e., increase the number of ground truth annotations), and please see the individual reviewer comments with specific questions related to other published/available code bases where you can directly compare your pipelines performance.

Methods, Relation to other packages, and Limitations:

The reviewers raised several points where methods are unclear, or how an analysis was performed was not clear. In particular, we ask you to check reviewer #3's comments carefully regarding methods. Moreover, we think a more nuanced discussion about when to do some "pre-processing" (like pose estimation) would be beneficial vs. straight to an ethogram, and visa versa. In particular, it's worth nothing that often times having an intermediate bottleneck such as key points allows the user to more easily assess network performance (keypoints are a defined ground truth vs. semantic action labels).

In total, the reviews are certainly enthusiastic about this work, and do hope you find these suggestions helpful. We look forward to reading your revision.Reviewer #1:

Bohnslav et al., present a new tool to quantify behavior actions directly from video. I think this is a nice addition to the growing body of work using video to analyze behavior. The paper is well written, clear for a general audience, and takes nice innovations in computer vision into life sciences and presents a usable tool for the community. I have a few critical points that I believe need addressed before publication, mostly revolving around benchmarking, but overall I am enthusiastic about this work being ineLife.

In the following sections I highlight areas I believe can be improved upon.

In relation to prior work: The authors should more explicitly state their contribution, and the field's contributions, to action recognition. The introduction mostly highlights limitations of unsupervised methods to perform behavioral analysis (which to note, produces the same outputs as this paper, i.e. an ethogram) and key point estimation alone, which of course is tackling a different problem. What I would like to see is a more careful consideration of the state-of-the-field in computer vision for action recognition, and clearly defining what the contribution is in this paper the cover letter alludes to them developing novel computer vision aspects of the package, but from the code base, etc, it seems they utilize (albeit nicely!) pre-existing works from ~3 years ago, begging the question if this is truly state-of-the-art performance. Moreover, and this does hurt novelty a bit, this is not the first report in life science of such a pipeline, so this should be clearly stated. I don't think it's required to compare this tool to every other tool available, but I do think discussing this in the introduction is of importance (but again, I am still enthusiastic for this being ineLife).

"Our model operates directly on the raw pixel values of videos, and thus it is generally applicable to any case with video data and binary behavior labels and further does not require pre-specification of the body features of interest, such as keypoints on limbs or fitting the body with ellipses." – please include references to the many other papers that do this as well. For example, please see:

Data-driven analyses of motor impairments in animal models of neurological disorders https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000516

LSTM Self-Supervision for Detailed Behavior Analysis https://openaccess.thecvf.com/content_cvpr_2017/html/Brattoli_LSTM_Self-Supervision_for_CVPR_2017_paper.html

Facial expressions of emotion states and their neuronal correlates in mice https://science.sciencemag.org/content/368/6486/89/tab-figures-data (not deep learning, but similar workflow; also extract features as the authors here do, and gets good performance using old CV techniques)

Deep learning improves automated rodent behavior recognition within a specific experimental setup https://www.sciencedirect.com/science/article/pii/S0165027019303930

I think Figure 1A is a bit misleading, it's not clear anymore that manual annotation is the only or most common other alternative pipeline (discussed below in benchmarking)- many tools for automated analysis now exist, and tools like JAABA and MotionMapper have been around for 5+ years; I would rather like to see a comparison workflow to "unsupervised methods," and/or keypoint estimation + classification with supervised or unsupervised means.

Lastly, they do not discuss key papers in life science for automated animal ethogram building, such as Live Mouse Tracker (https://livemousetracker.org/), BORIS and related Behatrix. Not only should these important papers be discussed, they should likely be benchmarked if the authors want to claim SOTA (see below).

Datasets: the authors claim they picked challenging datasets ("Diverse and challenging datasets to test DeepEthogram"), but I don't believe this is the case and they should tone down this statement. In fact, the datasets presented are rather easy to solve (the camera is orthogonal to the animal, i.e. top or bottom, or the animal's position is fixed, and the background is homogeneous, rarely the case even for laboratory experiments). I would urge them to use another more challenging dataset, and/or discuss the limitations of this work. For example, a mouse in a standard home cage with bedding, nests, huts, etc would pose more challenges, or they could report their performance on the Kinect700 dataset, which they pretrain on anyhow.

Benchmarking: The authors don't directly compare their work to that of other tools available in the field. Is their approach better (higher performance) than:

(1) unsupervised learning methods

(2) pose estimation plus classifiers or unsupervised clustering (as done in LEAP, DeepLabCut, B-SOiD, SIMBA, and the ETH DLC-Analyzer)

(3) tools that automate ethogram building, such as JAABA, BORIS/Behatrix.

Therefore, more results should be presented in relation to key works, and/or a more clear introduction on this topic should be presented.

– For example, they claim it's hard to match the resulting clusters from unsupervised learning to their "label:" i.e., "their outputs can be challenging to match up to behaviors of interest in cases in which researchers have strong prior knowledge about the specific behaviors relevant to their experiments". But this is not really a fair statement; one can simply look at the clusters and post-hoc assign a label, which has been nicely done in MotionMapper, for example.

– In pose estimation, one gets an animal-centric lower dimensional representation, which can be mapped onto behavioral states (ethograms), or used for kinematic analysis if desired. However, there is the minimal number of key points needed to make a representation that can still be used for ethogram building. Is the raw-pixel input truly better than this for all behaviors? For example, on the simple datasets with black backgrounds presented in this work, the background pixels are useless, and don't hinder the analysis. However, if the background dynamically changed (camera is moving, or background changes (lighting, bedding etc)), then the classification task from raw pixels becomes much harder than the task of extracted keypoints to classification task. Therefore, I think the authors should do the following: (1) discuss this limitation clearly in the paper, and (2) if they want to claim their method has universally higher performance, they need to show this on both simple and more challenging data.

Moveover, the authors discuss 4 limitations of other approaches, but do not address them in their work, i.e.:

– "First, the user must specify which features are key to the behavior (e.g. body position or limb position), but many behaviors are whole-body activities that could best be classified by full body data." – can they show an example where this is true? It seems from their data each action could be easily defined by kinematic actions of specific body parts a priori.

– "Second, errors that occur in tracking these features in a video will result in poor input data to the classification of behaviors, potentially decreasing the accuracy of labeling." – but is poor video quality not an issue for your classification method? The apple-to-apple comparison here is having corrupted video data as "bad" inputs – of course any method will suffer with bad data input.

– "Third, users might have to perform a pre-processing step between their raw videos and the input to these algorithms, increasing pipeline complexity and researcher time." – can they elaborate here? What preprocessing is needed for pose estimation, that is not needed for this, for example? (Both require manual labor, and given the time estimates, DEG takes longer to label than key point estimation due to the human needing to be able to look at video clips (see their own discussion)).

– "Fourth, the selection of features often needs to be tailored to specific video angles, behaviors (e.g. social behaviors vs. individual mice), species, and maze environments, making the analysis pipelines often specialized to specific experiments." – this is absolutely true, but also a limitation to the authors work, where the classifiers are tailored, the video should be a fixed perspective, background static, etc. So again I don't see this as a major limitation that makes pose estimation a truly invalid option.

Benchmarking and Evaluation:

– "We evaluated how many video frames a user must label to train a reliable model. We selected 1, 2, 4, 8, 12, or 16 random videos for training and used the remaining videos for evaluation. We only required that each training set had at least one frame of each behavior. We trained the feature extractors, extracted the features, and trained the sequence models for each split of the data." – it is not clear how many FRAMES are used here; please state in # of frames in Figure 5 and in the text (not just video #'s).

Related: "Combining all these models together, we found that the model performed with more than 90% accuracy when trained with only 80 example frames" This again is a bit misleading, as the user wants to know the total # of frames needed for your data, i.e. in this case this means that a human needs to annotate at least 80-100 frames per behavior, which for 5 states is ~500 frames; this should be made more explicit.

– "We note that here we used DEG-fast due to the large numbers of splits of the data, and we anticipate that the more complex DEG-medium and DEG-slow models might even require less training data." – this would go against common assumptions in deep learning; the deeper the models, the more prone to overfitting you are with less data. Please revise, or show the data that this statement is true.

– "Human-human performance was calculated by defining one labeler as the "ground truth" and the other labeler as "predictions", and then computing the same performance metrics as for DEG. " – this is a rather unconventional way to measure ground truth performance of humans. Shouldn't the humans be directly compared for % agreement and % disagreement on the behavioral state? (i.e., add a plot to the row that starts with G in figure 3).

To note, this is a limitation of such approaches, compared to pose-estimation, as humans can disagree on what a "behavior" is, whereas key points have a true GT, so I think it's a really important point that the authors address this head on (thanks!), and could be expanded in the discussion. Notably, MARS puts a lot of effort into measuring human performance, and perhaps this could be discussed in the context of this work as well.

Reviewer #2:

It was a pleasure reviewing the methodological manuscript describing DeepEthogram, a software developed for supervised behavioral classification. The software is intended to allow users to automate classification/quantification of complex animal behaviors using a set of supervised deep learning algorithms. The manuscript combines a few state-of-art neural networks into a pipeline to solve the problem of behavior classification in a supervised way. The pipeline uses well-established CNN to extract spatial features from each still frame of the videos that best predicts the user-provided behavior labels. In parallel, optical flow for each frame is estimated through another CNN, providing information about the "instantaneous" movement for each pixel. The optical flow "image" is then passed to another feature extractor that has the same architecture as the spatial feature extractor, and meaningful patterns of pixel-wise movements are extracted. Finally, the spatial feature stream and the optical flow feature stream are combined and fed into a temporal Gaussian mixture CNN, which can pool together information across long periods of time, mimicking human classifiers who can use previous frames to inform classification of behavior in current frame. The resulting pipeline provides a supervised classification algorithm that can directly operate on raw videos, while maintaining a relatively small computational demands on the hardware.

While I think something like DeepEthogram is needed in the field, I think the authors could do substantially more to validate that DeepEthogram is the ticket. In particular, I find the range of datasets validated in the manuscript poorly representative of the range of behavioral tracking circumstances that researchers routinely face. First, in all exemplar datasets, the animals are recorded in a completely empty environment. The animals are not interacting with any objects as they might in routine behavioral tests; there are no cables attached to them (which is routine for optogenetic studies, physiological recording studies, etc); they are alone (Can DeepEthogram classify social behaviors? the github page lists this as a typical use case); there isn't even cage bedding.

The authors also tout the time saving benefits of using deep ethogram. However, with their best performing implementation (DEG slow), with a state of the art computer, with a small video (256 x 256 pixels, width by height), the software runs at 15 frames per second (nearly 1/2 the speed of the raw video). My intuition is that this is on the slow side, given that many behaviors can be scored by human observers in near real time if the observer is using anything but a stopwatch. It would be nice to see benchmarks on larger videos that more accurately reflect the range of acquisition frames. If it is necessary for users to dramatically downsample videos, this should be made clear.

Specific comments:

– It would be nice to see if DeepEthogram is capable of accurately scoring a behavior across a range of backgrounds. For example, if the model is trained on a sideview recording of an animal grooming in its cage, can it accurately score an animal in an open field doing the same from an overhead view, or a side view? If the authors provided guidance on such issues to the reader this would be helpful.

– The authors should highlight that human scoring greatly outperforms DEG on a range of behaviors when comparing the individual F1 scores in Figure 3. Why aren't there any statistics for these comparisons?

– Some of the F1 scores for individual behaviors look very low (~0.5). It would be nice to know what chance performance is in these situations and if the software is performing above chance.

– I find it hard to understand the size of the data sets used in the analyses. For instance, what is 'one split of the data', referenced in Figure 3? Moreover, the authors state "We selected 1, 2, 4, 8, 12, or 16 random videos for training and used the remaining videos for evaluation" I have no idea what this means. What is the length and fps of the video?

– Are overall F1 scores in Figure 3 computed as the mean of the individual scores on each component F1 score, or the combination of all behaviors (such that it weights high frequency behaviors)? It's also difficult to understand what the individual points in Figure 4 (a-c) correspond to.

– The use of the names Mouse-1, Mouse-2 etc for experiments are confusing because it can appear that these experiments are only looking at single mice. I would change the nomenclature to highlight that these reflect experiments with multiple mice.

– It is not clear why the image has to be averaged across RGB channels and then replicated 20 times for the spatial stream. The author mentioned "To leverage ImageNet weights with this new number of channels", and I assume this means the input to the spatial stream has to have same shape (number of weights) as the input to the flow stream. However why this is the case is not clear, especially considering two feature extractor networks are independently trained for spatial and flow streams. Lastly this might raise the question of whether there will be valuable information in the RGB channels separately that will be lost from the averaging operation (for example, certain part of an animal's body has different color than others but is equal-luminous).

– It is not intuitive why simple average pooling is sufficient for fusing the spatial and flow streams. It can be speculated that classification of certain behavior will benefit much more from optical flow features while other behaviors benefits from still image features. I'm curious to see whether an additional layer at the fusing stage that has behavior-specific weights could improve performance.

– Since computational demands is one of the major concern in this article, I'm wondering whether exploiting the sparse nature of the input images would further improve the performance of the algorithm. Often times the animal of interests only occupies a small number of pixels in the raw images, and some simple thresholding of the images, or even user-defined masking of the images, together with use of sparse data backends and operations should in theory significantly reduce the computational demands for both the spatial and flow feature extractor networks.

Reviewer #3:

The paper by Bohnslav et al., presents a software tool that integrates a supervised machine learning algorithm for detecting and quantifying behavior directly from raw video input. The manuscript is well-written, the results are clear. Strengths and weaknesses of the approach are discussed and the work is appropriately placed in the bigger context of ongoing research in the field. The algorithms demonstrate high performance and reach human-level accuracy for behavior recognition. The classifiers are embedded in an excellent user-friendly interface that eliminates the need of any programming skills on the end of the user. Labeled datasets can even be imported. We suggest additional analyses to strengthen the manuscript.

1) Although the presented metrics for accuracy and F1 are state of the art it would be useful to also report absolute numbers for some of the scored behaviors for each trial, because most behavioral neuroscience studies actually report behavior in absolute numbers and/or duration of individual behaviors (rears, face grooms, etc.). Correlation of human and DEG data should also be presented on this level. This will speak to many readers more directly than the accuracy and F1 statistics. For this, we would like to see a leave-one-out cross-validation or a k-fold cross-validation (ensure that each trial ends up exactly once in a cross validation set) that enables a final per-trial readout. This can be done with only one of the DEG types (e.g "fast"). The current randomization approach of 60/20/20% (train/validate/test) with a n of 3 repeats is insufficient, since it a) allows per-trial data for at most 60% of all files and b) is susceptible to artefacts due to random splits (i.e one abnormal trial can be over or under represented in the cross validation sets).

2) In line with comment 1) we propose to update Figure 4, which at the moment uses summed up data from multiple trials. We would rather like to see each trial represented by a single data-point in this figure (#bouts/#frames by behavior). As alternative to individual scatterplots, correlation-matrix-heatmaps could be used to compare different raters.

3) Direct benchmarking against existing datasets is necessary. With many algorithms being published these days, it is important to pick additional (published) datasets and test how well the classifiers perform on those videos. Their software package already allows import of labeled datasets, some are available online. For example, how well can DeepEthogram score…

a. grooming in comparison to Hsu and Yttri (REF #17) or van den Boom et al., (2017, J Neurosci Methods).

b. rearing in comparison to Sturman et al., (REF #21).

c. social interactions compared to (Segalin et al., (REF #7) or Nilsson et al., (REF #19)).

4) In the discussion on page 19 the authors state: "Subsequently, tens to hundreds to thousands of movies could be analyzed, across projects and labs, without additional user-time, which would normally cost additionally hundreds to thousands of hours of time from researchers." This sentence suggests that a network trained on the e.g. the open field test in one lab can be transferred across labs. This key issue of "model transferability" should be tested. E.g. the authors could use the classifier from mouse#3 and test is on another available top-view recording dataset recorded in a different lab with different open-field setup (datasets are available online, e.g. REF #21).

5) Figure 5D/E: Trendline is questionable, we would advise to fit a sigmoid trendline, not an arbitrarily high order polynomial. Linear trend lines (such as shown in Figure 4) should include R2values on the plot or in the legend.

6) In the discussion, the authors do a very good job highlighting the limitations and advantages of their approach. The following limitations should however be expanded:

a. pose-estimation-based approaches (e.g. DLC) are going to be able to track multiple animals at the same time (thus allowing e.g. better read-outs of social interaction). It seems this feature cannot be incorporated in DeepEthogram.

b. Having only 2 human raters is a weakness that should briefly be addressed. Triplicates are useful for assessing outlier values, this could be mentioned in light of the fact that the F1 score of DeepEthogram occasionally outperforms the human raters (e.g. Figure 3C,E).

c. Traditional tracking measures such as time in zone, distance moved and velocity cannot be extracted with this approach. These parameters are still very informative and require a separate analysis with different tools (creating additional work).

d. The authors are correct that the additional time required for behavior analysis (due to the computationally demanding algorithms) is irrelevant for most labs. However, they should add (1) that the current system will not be able to perform behavior recognition in real time (thus preventing the use of closed-loop systems, which packages such as DLC have made possible) and (2) that the speed they discuss on page 16 is based on an advanced computer system (GPU, RAM) and will not be possible with a standard lab computer (or provide an estimate how long training would require if it is possible).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "DeepEthogram, a machine learning pipeline for supervised behavior classification from raw pixels" for further consideration byeLife. Your revised article has been evaluated 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Johannes Bohacek (Reviewer #3).

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The reviewers all felt the manuscript was improved, and thank the authors for the additional datasets and analysis. We would just like to see two items before the publication is accepted fully.

(1) Both reviewer #1 and #2 note the new data is great, but lacks human ground truth. Both for comparison, and releasing the data for others to benchmark on, it would be please include the data. We also understand that obtaining ground truth from 3 persons is a large time commitment, but even if there is one person, this data should be included for all datasets shown in Figure 3.

(2) Please include links for the raw videos used in this work; it is essential for others to benchmark and use to validate the algorithm presented here (see Reviewer 3: "raw videos used in this work (except the ones added during the revision) are – it appears – not accessible online").

Lastly, reviewer 3 notes that perhaps, still, some use-cases are best suited for DeepEthogram, while others more for pose-estimation plus other tools, but this of course cannot be exhaustively demonstrated here; at your discretion you might want to address in the discussion, but we leave that up to your judgement.Reviewer #1:

I thank the authors for the revisions and clarifications, and I think the manuscript is much improved. Plus, the new datasets and comparisons to B-iOD and R-Analyzer (Sturman) are a good additions.

One note is that is not clear which datasets have ground truth data; namely, in the results 5 datasets they use for testing are introduced:

"Mouse-Ventral1"

"Mouse-Ventral2"

"Mouse-Openfield"

"Mouse-Homecage"

"Mouse-Social"

plus three datasets from published work by Sturman et al.,

and "fly"

Then it states that all datasets were labeled; yet, Figure 3 has no ground truth for "Mouse-Ventral2" , "Mouse-Homecage" , "Mouse-Social" or 'Fly" -- please correct and include the ground truth. I do see that is says that only a subset of each of the 2 datasets in Figure 3 are labeled with 3 humans, but minimally then the rest (1 human?) should be included in Figure 3 (and be made open source for future benchmarking).

It appears from the discussion this was done (i.e., at least 1 human, as this is of course required for the supervised algorithm too):

"In our hands, it took approximately 1-3 hours for an expert researcher to label five behaviors in a ten-minute movie from the Mouse-Openfield dataset" and it appears that labeling is defined in the methods.

Reviewer #2:

The authors did a great job addressing our comments, especially with the additional validation work. My only concern is that some of the newly included datasets don't have human-labeled performance for comparison, hence making it hard to judge the actual performance of DeepEthogram. While I understand it is very time-consuming to obtain human labels, I think it will greatly improve the impact of the work if the model comparison can be bench-marked against ground truth. Especially it would be great to see the comparison to human label for the "Mouse-Social" and "Mouse-Homecage" datasets, which presumably represent a large proportion of use cases for DeepEthogram. Otherwise I think it looks good and I would support publication of this manuscript.

Reviewer #3:

The authors present a software solution (DeepEthogram) that performs supervised machine-learning analysis of behavior directly from raw videos files. DeepEthogram comes with a graphical user interface and performs behavior identification and quantification with high accuracy, requires modest amounts of pre-labeled training data, and demands manageable computational resources. It promises to be a versatile addition to the ever-growing compendium of open-source behavior analysis platforms and presents an interesting alternative to pose-estimation-based approaches for supervised behavior classification, under certain conditions.

The authors have generated a large amount of additional data and showcase the power of their approach in a wide variety of datasets including their own data as well as published datasets. DeepEthogram is clearly a powerful tool and the authors do an excellent job describing the advantages and disadvantages of their system and provide a nuanced comparison of point-tracking analyses vs. analyses based on raw videos (pixel data). Also their responses to the reviewers comments are very detailed, thoughtful and clear. The only major issue is that the raw videos used in this work (except the ones added during the revision) are – it appears – not accessible online. This problem must be solved, the videos are essential for reproducibility.

A minor caveat is that in order to compare DeepEthogram to existing supervised and unsupervised approaches, the authors have slightly skewed the odds in their favor by picking conditions that benefit their own algorithm. In the comparison with point-tracking data they use a low resolution top-view recording to label the paws of mice (which are obstructed most of the time from this angle). In the comparison with unsupervised clustering, they use the unsupervised approach for an application that it isn't really designed for (performed in response to reviewers requests). But the authors directly address these points in the text, and the comparisons are still valid and interesting and address the reviewers concerns.
