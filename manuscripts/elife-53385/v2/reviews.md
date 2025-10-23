# Peer review - Round 1

Editors:
- Thomas Yeo, National University of Singapore Singapore

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53385.sa1](https://doi.org/10.7554/eLife.53385.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper describes NeuroQuery, a new approach to automated meta-analysis of the neuroimaging literature. It is demonstrably superior for many purposes, particularly as a starting point for constraining predictive models and as regions or patterns of interest in new studies. We believe that this will be a very widely used tool. It's also a tremendous amount of work to build and validate, and very few groups have both the skills and motivation to build this and make it accessible to the broad neuroscience/neuroimaging community.

Decision letter after peer review:

Thank you for submitting your article "NeuroQuery: comprehensive meta-analysis of human brain mapping" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Büchel as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Tor D. Wager (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper describes NeuroQuery, a new approach to automated meta-analysis of the neuroimaging literature. It is demonstrably superior for many purposes – particularly as a starting point for constraining predictive models and as regions or patterns of interest in new studies. We believe that this will be a very widely used, and cited, tool. It's also a tremendous amount of work to build and validate, and very few groups have both the skills and motivation to build this and make it accessible to the broad neuroscience/neuroimaging community.

There are a number of exemplary features of this work, including:

– A full implementation that is openly shared on Github, including source code, models, and data

– A fully functional web interface that runs simply and beautifully

– Several types of validation of the model's performance, including (a) stability with rare terms listed in few studies, (b) reproducibility of maps with limited data, (c) better encoding/prediction of brain maps associated with terms.

This work dramatically expands the vocabulary of search terms that can be used in neuroimaging meta-analyses. We believe this is going to be really useful. The model framework is also interesting and motivated by some careful considerations in terms of how the model should be affected by certain classes of rare terms, features included in the model, etc. The bottom line for users is a better set of predictive maps. While there are many potential varieties of such models and one could second-guess some particular choices, the beauty of the authors' approach is that the code is available for others to try out variations and build/validate a different model based on their sensibilities and preferences.

Essential revisions:

1) We believe that the validations are insufficient for some of the claims. The authors should either expand their experiments to validate these claims or tone down their claims.

A) "NeuroQuery, can assemble results from the literature into a brain map based on an arbitrary query." This statement can be mis-interpreted to mean that users can enter any terms they want. My understanding is that the query has to comprise words from the 7547 dictionary words. Words outside the dictionary are ignored.

B) Introduction: "For example, some rare diseases, or a task involving a combination of mental processes that have been studied separately, but never – or rarely – together." This suggests NeuroQuery can do this with precision, but the authors have not experimentally demonstrated that activation maps involving "combination of mental processes that have been studied separately, but never together" can be accurately predicted. To validate this, the authors should consider cases involving compound mental processes (e.g., "auditory working memory") and remove all experiments involving both "auditory" + "working memory". Care has to be taken to also remove experiments using words similar to "auditory" + "working memory", so that experiments such as "auditory n-back" are also removed, even though the experiments did not explicitly use the term "working memory". Note that the entire experiments should be removed, rather than just the specific words. The authors can then re-train their model and show whether the query "auditory working memory" yields activation similar to the removed experiments involving auditory working memory.

C) For subsection “NeuroQuery can map rare or difficult concepts”, it's important to differentiate between a concept that is rarely studied versus a rare word that seldom appears in the literature even though variations of the word might be widely studied. The whole section seems to imply that the NeuroQuery is able to accomplish the former very well, but in the experiment, they chose frequent terms (e.g., language) and progressively delete them from their dataset, thus they are really testing the latter. To really test the former, rather than just deleting the word "language" from the documents, they should delete entire documents containing "language" and/or other terms similar to language (e.g., semantic).

2) Figure 8 (right panel) should be in the main text in addition to (or replacing) Figure 6. While the log likelihood measure is valid, the "absolute" measure is much more helpful to the users of knowing how much to trust the results. Along this note, it is somewhat concerning that the overall accuracy is only 70% – how much should a user trust a tool with a 70% accuracy? However, this is perhaps underselling NeuroQuery because coordinates tend to be sparse, so just based on the reported coordinates, this classification task might simply be very hard. What might be more useful would be for the user to get a sense of how much the NeuroQuery maps actually matches real activation maps. Can the authors perform the same experiment, but using real activation maps from NeuroVault or their own Individual Brain Charting dataset? This is just a suggestion. The authors can choose to just discuss this issue.

3) Results section: some pieces of argumentation presented here are not fully convincing. The authors propose that: "Term co-occurrences, on the other hand, are more consistent and reliable, and capture semantic relationships [Turney and Pantel, 2010]". Most of the brain mapping literature is made of attempts to differentiate cognitive processes inferred from the study of human behaviour such as "proactive control VS retroactive control", "recollection VS familiarity", "face perception VS place perception", "positive emotion VS negative emotion". In that context, it is unclear how terms co-occurrence for example between "face" and "place" would be more consistent and reliable than "face" alone. Term co-occurrence mainly reflects what type of concepts tend to be studied together.

4) The authors suggest that "It would require hundreds of studies to detect a peak activation pattern for "aphasia". It is not clear what do the authors mean here. Aphasia is a clinical construct referring to a behavioural disturbance. It is defined as "an inability (or impaired ability) to produce or understand speech". Accordingly, we don't see how one could search for a peak of activation related to aphasia? The line of argumentation could be clarified here by starting with concrete examples. Perhaps an example the authors may refer to is that, starting from a clinical point of view, researchers may want to investigate brain activation related to the processes of language production in order to better understand dysfunctions such those seen in aphasia. Accordingly, the related publication will probably mention "aphasia" "language production" "phonological output lexicon" etc… and this pattern of terms could in turn be linked to similar language related terms in other publications. An alternative guess is that maybe the authors actually refer here to lesion studies that have, for example, searched for correlation between grey matter volume atrophy and aphasia?

5) We have some suggestions for improving the Abstract/Introduction

A) Explaining how a predictive framework allows maps to be generated by generalizing from terms that are well studied ("faces") to those that are less well studied and inaccessible to traditional meta-analyses ("prosopagnosia"). And explaining that this is good for some use cases (generating sensible ROIs/making guesses about where future studies of prosopagnosia might activate), but not good for others (e.g., knowing that a particular area is (de)activated in studies of prosopagnosia).

B) Can you provide a bit more context on previous topic models (e.g., Nielsen/Hansen NNMF "bag of words" work from way back, Poldrack/Yarkoni topic models, GCLDA) and how this approach is different. After reading the Introduction, readers have a sense of what Neuroquery does (its goal), but not how it actually does it (no algorithmic insight). For example, Neuroquery "infers semantic similarities across terms used in the literature", but so does a topic model (which is not mentioned/cited). We recommend including more description early on of what the algorithmic differences are relative to previous work that confer advantages. This is explained later (with some redundancy across sections), but more up front would be helpful.

C) In the Introduction, the authors argue that meta-analyses are limited primarily by performance of in-sample statistical inference (they "model all studies asking the same question") and lack of use of a predictive framework. While there is great value in the current work, we don't think that is strictly true. Other meta-analyses have taken a predictive approach, in a limited way, and also modeled differences across study categories. The Naive Bayes classifier analyses in the Neurosynth paper (Yarkoni, 2011) are an example. And Neurosynth considers topics across tasks and fields of study. Analyzing studies by single search terms is an important limitation (topic models by Poldrack and Yarkoni help; perhaps acknowledge their 2014 paper). Viewing the paper as a whole, we understand why the authors focus on prediction vs. inference in the Introduction, but it's hard to understand how this other work fits in without having gone through the whole paper.

D) Likewise, the emphasis on the ability to interpolate struck us as odd. We understand this as generalizing based on semantic smoothing. This is useful, but we don't think what you meant was really clearly explained in the Introduction.

E) The authors make a compelling case that current meta-analyses are limited. The Pinho 2018 example is very helpful: An automated meta-analysis of all the studies performing the same or a similar contrast is not currently possible, primarily because we have lacked the tools to parse the natural language text in articles well enough to identify an "equivalence class" of functional contrasts.

F) "For example, some rare diseases, or a task involving a combination of mental processes that have been studied separately, but never – or rarely – together." Could the authors provide a concrete example?

6) We have some suggestions for improving the clarity of the Results section:

A) “NeuroQuery relies on a corpus of 13459 full-text neuroimaging publications”

What type of neuroimaging publications? task-based activations experiments? If so, of which type: PET and fMRI or only fMRI-based? does it also include structural MRI studies? does it include all types of populations (healthy adults, elderly, patients studies)?

B) It is not clear how to read Figure 1. What do the length and width of the color and grey lines represent? could this figure be more elaborated to integrate additional aspects of the procedure? e.g. each of the three brain slice has a color that seems to reflect their respective association with the term, how is all that information combine to a single brain pattern?

C) Terminological precision: Results paragraph one: the term "area" is usually reserved for brain territories defined based on microstructure features (e.g. Area 4). Here the authors refer to a spatial location in the brain (or maybe a zone of homogeneity with regards to a specific feature), so they should prefer the term "brain region" for that purpose.

D) Finally, the supplement material provides several quantitative evidence of significant improvement compared to Neurosynth, such as:

– "our method extracted false coordinates from fewer articles: 3 / 40 articles have at least one false location in our dataset, against 20 for NeuroSynth"

– "In terms of raw amount of text, this corpus is 20 times larger than NeuroSynth's"

– "Compared with NeuroSynth, NeuroQuery's extraction method reduced the number of articles with incorrect coordinates (false positives) by a factor of 7, and the number of articles with missing coordinates (false negatives) by a factor of 3 (Table 2)."

All these aspects could be summarized together with the more qualitative aspects in a table to emphasize the significant improvements over Neurosynth.

7) In the Discussion, it would be very helpful to give readers some intuition for when NeuroQuery will not yield sensible results and when/how exactly it should be used (e.g., even a table of use cases that would be appropriate and inappropriate) – and how to interpret carefully (e.g., look at the semantic loadings, and if there is one anatomical term that dominates, realize that you're essentially getting a map for that brain region). The ADHD example is useful but doesn't really cover the space of principles/use cases. Here are some possible examples we have thought of:

A) Some particular limitations may arise from the predictive nature of neuroquery, which may be less intuitive to many readers. For example, if I put in "aphasia", I will get map for "language", because aphasia is semantically close to language. This is very sensible, but users should not, of course, take this as a map of "aphasia" to be related other terms and used in inference. Users might "discover" that aphasia patterns are very closely related to "language" patterns and make an inference about co-localization of healthy and abnormal function. Of course, it's not your responsibility to control all kinds of potential misuse. But pointers would be helpful to avoid another, e.g., "#cingulategate" (Lieberman et al., 2016 PNAS).

B) For example, let's consider again the case about "combination of mental processes that have been studied separately, but never together". From my understanding of the algorithm, suppose users query "auditory" + "working memory", basically the prediction will be a linear combination of activation maps from "auditory" and "working memory" (+ similar terms due to the smoothing/query expansion). As such, this assumes that compound mental processes yield activations that are linear combination of activation maps of individual mental processes. This should be made clear.

C) Playing around with NeuroQuery, there are some queries that generate obviously wrong results. For example, "autobiographical memory" should probably yield the default network, but we getting hippocampal/retrosplenial activation instead. This presumably happens because NeuroQuery "expanded" the query to become memory because "autobiographical memory" is not one of the 200 keywords? Interesting that NeuroSynth does get it correct (https://neurosynth.org/analyses/terms/autobiographical%20memory/).

D) Perhaps a brief discussion of other limitations would be helpful. We submit that some of the fundamental problems are those not easily solved – that we usually perform meta-analyses based on studies of the same nominal task type (e.g., N-back), and sometimes minor variations in task structure can yield divergent findings. We don't know what all the dimensions are yet. This problem goes far beyond the challenge of establishing a set of consensus labels for task types and relevant cognitive processes. In short, we don't really even know what task features to label yet in many cases, and they don't combine additively. A stop-signal task with one adaptive random walk may be different than one with four, as it allows a different type of cognitive strategy.

E) When to use it: For common terms, meta-analysis (e.g., Neurosynth) does very well (e.g., Figure 4). When would the authors recommend using NeuroQuery over another meta-analytic tool? Maybe they could provide a summary of use cases and conditions (e.g., when few studies of a term/topic are available). Also see point (C).

8) Discussion of other approaches: We submit that the field has become tracked into a relatively narrow space of the possible options and techniques for meta-analysis, based on local analysis of coordinates in MKDA/ALE. Alternatives could be mentioned as potential future directions. For example, early work explored clustering of spatial locations and spatial discriminant tests (e.g., Wager et al., 2002, 2004, 2005), and later work has explored spatial models (e.g., Kang, 2011, Kang, 2014, Wager, 2015) and more advanced co-activation models (Xue, 2014). While this is obviously beyond the scope of the present paper, future work might consider models of spatial co-activation when generating predictions and inferences about meta-analytic maps.

9) The methods are a bit unclear:

A) Significant details about methodologies are missing. How are term frequency and inverse document frequency computed?

B) Equation 5: How is σ^ij computed? Square root of the entries of equation 8?

C) Equation 5: What is the difference between σ^i and σ^ij? σ^i is a column/row of σ^ij?

D) Yj is the j-th column not i-th column of Y?

E) M is a v x n matrix, so equation 8 is a v x v matrix? We are confused how this maps to σ^ij.

F) In Equation 10, is ||U||_1 just the sum of absolute values of all entries in U?

G) What is k set to be in equation 10?

H) "More than 72% of the time, NeuroQuery's output has a higher Pearson correlation with the correct map than with the negative example" – "correct map" refers to the KDE density maps?

10) Subsection “Smoothing: regularization at test time” is hard to read. It would be helpful if the authors explain the intuition behind the different steps and what the different matrices represent. For example, it might be helpful to explain that each row of V can be thought of as the association of words with topic k, so a higher value for row i, column j suggests the j-th dictionary word is more strongly related to the topic k. As another example, the authors should also unpack subsection “Smoothing: regularization at test time”: why do we take V and scale with 𝑛𝑖,𝑖 and then compute C and then l1-normalizing the rows of C to produce T and then finally S. What does each step try to do? We guess roughly speaking VV^T is like a co-occurrence matrix (how likely are two words likely to appear together?), but we are not sure why we have to do the extra normalization with 𝑛𝑖,𝑖, l1-normalization, etc.
