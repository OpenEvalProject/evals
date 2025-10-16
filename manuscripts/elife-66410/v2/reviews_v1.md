# Peer review - Round 1

Editors:
- Gordon J Berman, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66410.sa1](https://doi.org/10.7554/eLife.66410.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript will be of interest to C. elegans neuroscientists and also biologists interested in methodological innovations in live imaging. The method described in the paper is clever and elegant, and the solution to the neuron correspondence problem is significant because it is another step toward closed-loop neural perturbation experiments in mobile worms.

Decision letter after peer review:

Thank you for submitting your article "Fast deep learning correspondence for neuron tracking and identification in C. elegans using synthetic training" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Gordon J Berman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Many details about the training and characterization are missing. There should be more supplemental info accompanying the manuscript on training the network, characterizations of robustness against noise and errors, verifications – including quantifications like scrambling the data sequence, etc. Not having the information creates a big uncertainty on how to evaluate how close the work is to being usable in a real scenario (i.e., one where segmentation is also available). For whole-brain imaging, there are so many perturbations that can throw off tracking algorithms – segmentation error, cells sometimes "show up" and sometimes "disappear" (the newer version of GCaMPs are really low in baseline), etc. Not seeing these explored systematically concerned the reviews as they didn't have a good sense of whether they have attempted to look at these issues. Thus, we ask the authors to add additional figures and quantifications along these lines to buttress the manuscript's claims.

2) There also was a paucity of details on the network training itself. The methods section mentions, in passing, that some hyper-parameter choices were made on a validation set. Which hyper-parameters were selected in this way, and what ranges of parameters were tried? In this exploration, did the authors observe that network performance was sensitive to some hyper-parameters?

3) Since speed was a crucial criterion for model design, was there any trade-off between network size and running speed, such that future hardware may possibly achieve higher accuracy without further conceptual advances? Similarly, the results all report the performance of one trained network, which the authors report taking half a day to train. This is both a long time and not so long. Were other networks trained and not described, or did they fail to converge? If so, how often do these networks train successfully if using different initial conditions, and do their performances differ?

4) Relatedly, the reviewers also thought that the clarity of the algorithm performance is lacking. For instance, there are no training curves shown for the algorithm. Adding details on the network performance/training into supplementary materials would be beneficial.

5) The majority of the paper uses the authors' own data, which has unique features and structures, leading the reviewers to wonder if the presented results are as generalizable as the authors claim. For example, the authors only accounted for cells that are present in all data sets. What would the numbers look like if they divided by all cells that might show up in any of the animals (a significantly larger number)? The authors do bring up the issue of coverage and accuracy trade-off, but did not really explore this issue at all – the reviewers thought that this point is critical to whole-brain imaging, as the data are rather noisy. So this will have to be addressed using other whole-brain data (maybe published data from another lab, e.g. the Zimmer lab), re-do analysis on the neuron identification part, and more characterization on the coverage-accuracy trade-off. If using the Zimmer data, for example, they should be able to show that they can get the same temporal PCs. If the algorithm is very generalizable and extremely fast and quite accurate as the authors claim, it should be fairly simple to use it on a real whole-brain experiment data set and show that meaningful conclusions can come of it. Without this, one should not make such claims that "The method is fast and predicts correspondence in 10 ms making it suitable for future real-time applications."

6) Related to this point, the reviewers thought that the tracking having an ~80% accuracy is not a meaningful goal. First, this accuracy is an average, and it has no bearing on whether a cell can be *continuously* tracked. The traces may be broken, and worse, wrong cells are linked together. This 80% does not guarantee anything at this point. Having an accuracy on a per-frame basis is not the main goal, and there are existing data from the authors themselves and others where this point could be validated. One would have to show that the traces are similar, and better yet, the temporal PCs are similar. The tracking having 80% accuracy cannot be used for optogenetics at all. It is not meaningful to fire the laser at cells with 20% uncertainty in their identities and carry out any meaningful experiments. Thus, either additional validation on the continuity of the tracked accuracy needs to be provided, or the text on optogenetics needs to be significantly toned down or removed.

7) What is the practical use-case for this cross-individual correspondence, since 65.8% means there are still a lot of errors. Perhaps the authors can discuss (even with some back-of-the-envelope estimates) how much this means for an experiment that compares neural activity between two different worms? What is an experiment that may require doing this fast correspondence estimation between two worms in real-time? Practically speaking, how often would one need to compute correspondences between pairs of frames between two worms? Would the overall correspondence be better if more volumes from each animal were used to find a consensus, or would the authors recommend using NeRVE in that case?

8) "Recording" was used multiple times in the text and it's not clear whether they are time series or single volumes. For instance, it is not clear what exactly are the "12 individual animals" used for generating the training data. Are they single time frames or are they video? If videos, how many frames? It is not clear the NeuroPAL data sets are videos or single volumes.

9) Relatedly, if many time points of 12 individual animals are used to generate training data, this is not fully synthetic. The basis of the training data from many worm heads holds a lot of information. The question is also whether all (any) of the augmentation components are necessary or useful. There should be a full characterization of the differential benefit of the different augmentations from not augmenting at all. Calling it synthetic data (e.g., line 566) may be somewhat of a misnomer.

Reviewer #1:

In this submission, the authors introduce a new methodology for tracking neural correspondences in calcium imaging of freely moving C. elegans using the transformer architecture. The method presents produces state-of-the-art assignment accuracies in a manner that is significantly faster and more robust than existing approaches, potentially allowing for real-time tracking applications once other aspects of the computer vision pipeline become faster. The authors demonstrate the ability of their method on data within and between individuals (using the NeuroPALworm lines), as well as on synthetic control data.

Reviewer #2:

Yu et al. developed a deep neural network model with the goal of solving two challenging problems in live imaging of neural activity in mobile C. elegans. They call their method fast Deep Learning Correspondence (fDLC), and it simultaneously achieves (1) identification of the same neurons within one animal in a movie, and (2) identification of corresponding neurons between two animals. These problems are difficult because worms change poses as they move, including wiggles within a horizontal plane as well as rolls, and there may be developmental variability between individual worms. Many past approaches have relied on computationally `straightening` the worm into a canonical coordinate system, or on generative models that rely on manually curated features. Instead, fDLC takes a neural network approach; the model builds on the transformer architecture, popularized by its success in natural language process (NLP). To circumvent the prohibitively large quantities of data typically required to train such models, the authors used a relatively modest experimental dataset and synthetically augmented the training data, simulating worm-like movements and imaging conditions to generate arbitrarily large training sets. They then tested the trained model on a variety of data not used on the training, reporting good accuracy. The fDLC approach described here is particularly impressive because of its speed -- it computes correspondances among ~100 neurons in 10 msec per volume on relatively standard GPU hardware.

Strengths

The paper is generally clearly written, the methods and results are well presented, and the figures are concise summaries of the results. The introduction gives a thorough and thoughtful review of the related literature and how this work relates to previous methods. I particularly appreciate the authors have made their code publicly available. I believe the paper describes a valuable contribution that will be of significant impact in the study of C. elegans neuroscience, as it solves a series of related technical challenges whose solution will open the door for more bold experiments.

The method described is well suited for the problem, and the performance described is impressive when compared to the closest methods available in the literature. The results are all well demonstrated and justify the conclusions.

Weaknesses

The strengths of the fDLC method are to enable real-time neural perturbations and to allow direct comparisons between different worms. However, as the authors point out, the real-time experiments are currently still intractable because cell segmentation remains slow. Further, direct comparisons between different worms remain to be demonstrated as an application of fDLC.

On the first application, the true impact of fDLC may have to wait for further development of real-time cell segmentation. This seems like an imminently achievable technology. On the second application, it remains to be shown whether the 65.8% accuracy -- while quite impressive -- is sufficient to allow novel analyses and insights to be gained. For instance, if one were analyzing a dataset of 10 separately imaged worms, the overall accuracy of identifying an individual corresponding neuron among these 10 animals may be significantly lower.

– Perhaps I'm being a bit nit-picky on terminology, but the use of the phrase `transfer learning` in the abstract (also in Figure 1) seems a bit of a stretch. Am I interpreting correctly that the `transfer` is between the train and test sets, without any further refinement? In what way is this `transfer learning` beyond the standard machine learning use of the test/train split?

– The methods sections mentions in passing, that some hyper-parameter choices were made on a validation set. Which hyper-parameters were selected in this way, and what ranges of parameters were tried? In this exploration, did the authors observe that network performance was sensitive to some hyper-parameters?

– In the tracking results of the same worm across time, the fDLC approach treats each set of coordinates as independent measurements and does not explicitly use any temporal information. Nevertheless, I would imagine that segmented neuron positions from adjacent frames of the same movie, when the worm has not moved its pose by much, may be easier to track than pairs of frames picked at random. Is this true? What about frames that are 2, 3, etc. samples apart?

– The acronym `fDLC` may be easily confused with some modification of DeepLabCut. While this work is also a deep learning based tracking software, I think mistaking this method for DeepLabCut may be not desirable.

Reviewer #3:

This manuscript describes a deep learning model for tracking neurons in C. elegans worms; a side utility of the algorithm is described to be for neuron identification. The problems it is trying to address are significant as there is a need for fast neuron tracking in moving C. elegans whole brain imaging; the premise of the work of using synthetic data for training is interesting. The manuscript has several significant deficiencies, including claims not fully supported by evidence and overreaching conclusions.

Major strengths:

1. The idea of using augmentation to real data to generate training sets for ML model is interesting, particularly in situations where data are hard to come by.

2. fDLC's speed is attractive for the use cases.

Major weaknesses:

1. For tracking to have ~80% accuracy is not meaningful. First, this accuracy is an average, and it has no bearing on whether a cell can be *continuously* tracked. The traces may be broken, and worse, wrong cells are linked together. This 80% does not guarantee anything at this point. Having an accuracy on per-frame basis is not useful at all. To actually have an impact on tracking, traces have to be shown, and these traces need to be verified. There are existing data from the authors themselves and others. One would have to show that the traces are similar, and better yet, the temporal PCs are similar. The tracking having 80% accuracy cannot be used for optogenetics at all. It is not meaningful to fire the laser at cells with 20% uncertainty in their identities and carry out any meaningful experiments. This claim does not make sense. The text on optogenetics needs to be significantly toned down, or better yet, removed.

2. What the Transformer network learned with the data is unclear. The paper does not show exactly what the Transformer network has learned – what features of the data are important? This is critical, as it is possible that another form of information is actually being learned from the data. For instance, in training where the hand-curated cells are used, the cells may be entered in a particular order. It is therefore possible that the Transformer network is learning the order of which the cells are entered, rather than the actual spatial relationships. To show that the Transformer network is really learning something meaningful in the data, one would have to scramble the order of the data and show that the results are not different.

3. The authors stressed that the learning does not require users to prescribe what to look for, but the warping, transformation, noises added are in essence adding information in user-defined way. This claim does not make sense. In the text, the authors also use language such as "roughly matched (their) estimate of variability observed by eye". This is not rigorous and seems dangerous. Exact details and rationales of choices for the warping, transformation, noises added, etc need to be included and fully justified.

4. Clarity of algorithm performance is lacking. For instance, there are no training curves shown for the algorithm.

5. Related, importantly, the accuracy of the algorithm must be very much data-dependent. Sources that can perturb a perfect scenario need to be examined. For instance, how would cells' activities in GCaMP recordings affect accuracy? How would segmentation error affect accuracy? It is not possible to evaluate the real-world utility if these issues are not explored. For all we know, it could be the best data that are fed to the algorithm that is used to calculate the accuracies here.

6. The authors stated that there is a trade-off between accuracy and coverage. This is an important point, but the authors did not fully characterize such trade-off (related to the accuracy comment above); nor was the coverage assumption/definition that went into each part of the work clearly stated. In the tracking part, what would the coverage be? How is it defined? Comparisons to literature algorithm for neuron identification is should not be done when the coverage is also not well defined, i.e. the denominators for the percentages in table 4 are ill-defined.

7. Clarity of the experimental data is lacking. "Recording" was used multiple times in the text and it's not clear whether they are time series or single volumes. For instance, it is not clear what exactly are the "12 individual animals" used for generating the training data. Are they single time frames or are they video? If videos, how many frames? It is not clear the NeuroPAL data sets are videos or single volumes.

8. Related to the issue above, if many time points of 12 individual animals are used to generate training data, this is not at all synthetic. The basis of the training data from many worm heads holds a lot of information. The question is also whether all (any) of the augmentation components are necessary or useful. There should be a full characterization of the differential benefit of the different augmentations from not augmenting at all. Calling it synthetic data in my opinion is a misnomer (e.g. line 566).

9. Generally speaking, if the algorithm is very generalizable and extremely fast, and quite accurate as the authors claim, it should be fairly simple to use it on a real whole-brain experiment data set and show that meaningful conclusions can come of it. Without this, one should not make such claims that "The method is fast and predicts correspondence in 10 ms making it suitable for future real-time applications."

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Fast deep neural correspondence for tracking and identifying neurons in C. elegans using semi-synthetic training" for further consideration by eLife. Your revised article has been evaluated by Ronald Calabrese (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Essential Revisions:

1. The data are from the authors themselves, not peer-reviewed, and not independently validated. The authors did not use, for instance, the Zimmer lab's data; the reason why was unclear to the reviewers. Also, the authors themselves have at least one volume of sensible data from their own previous work (NeRVE, Nguyen et al., 2017) in which they actually performed PCA on the GCaMP data. Applying fDNC to that set of data and showing that PCAs are comparable would make their claim much stronger.

2. The accuracy is a central claim in the paper. It is good that the authors now define what accuracy is in the text, but it is still confusing. A match between the template and the test does not assign a name necessarily -- unless the template neurons already have labels/identities from the ground truth information. From the text, it seems that the template is used as the reference with identities already assigned and that only the neurons common to both the test and template are considered since the denominator of the accuracy is defined as "the total number of ground truth matches". (Another interpretation of the definition would suggest that neurons that both the template and the test got wrong but matches each other would have been counted as accurate?!)

There are two issues – the definition is not applicable for some other methods and that this definition is artificially favorable for fDNC.

a. In Table 2, the authors compare the accuracies of fDNC to that of CPD and CRF (ref 3). This is not appropriate. fDNC and CPD both use template matching, while CRF does not. This is to say that the accuracy definition is not the same for these methods.

b. The accuracy of fDNC is artificially more favorable. NeuroPAL datasets do not reliably identify the same neurons. When using one NeuroPAL dataset as template, and another as the test set, the matches are on the order of 70-80%. The definition of accuracy the authors use, therefore, is artificially high (by some significant percentage). The errors associated in neurons not common to the test and the template are discounted.

c. The coverage and the accuracy discussion should be restored.

3. Implying that fDNC is not "data-privileged" is false (page 13). fDNC is not naive – information from 4000 volumes from 12 animals is there, and fDNC must use a known annotated NeuroPAL dataset as a template, and therefore there is information again (e.g. variability of positions etc). Revising the discussion around this point is important.

Reviewer #1:

I thank the authors for their thoughtful revisions and especially for providing additional methodological details and caveats. I think that it would make a good addition to the literature.

Reviewer #2:

I thank the authors for their careful and detailed responses to comments and concerns. I especially appreciate the additional methodological details on the training of their model and the clarified definition of how performance is evaluated. I think this work is an interesting and valuable contribution to the literature, and another substantial step in achieving real-time manipulations in this popular experimental organism.

Reviewer #3:

The revised manuscript is improved for many of the details, including the data used and how the model was constructed, which are good for reproducibility.

The responses are unsatisfying in a few major places:

1. One of the central concerns from the previous round of review is on whether the algorithm performs well enough for tracking. The revision is unsatisfactory.

a. The authors were asked to apply their tracking to real data to show that the tracking results can generate meaningful data. The authors misunderstood the request as asking for biological insights. The intention is to VALIDATE, not to generate new insights. In fact, that's precisely the reason to apply the algorithm/model to well-curated data that are already peer-reviewed and published.

b. Figure 3 and the supplemental data were a step in the right direction, but are still unsatisfactory. Figure 3E now shows the tracking accuracy; as expected, the errors are sporadic. Some neurons appear to be ok while others not. This is THE reason PCA was asked in the last round. Figure 3 supplement showing AVAL/R traces are not enough to demonstrate the traces are sensible. It is anecdotal. AVA are among the most "obvious" neurons; peaks correlating to reversal behavior made the cells easy to identify and the tracking errors very easily ignored. The question is whether the rest of the neurons (>99% of them) can give sensible traces.

c. The data are from the authors themselves, not peer reviewed and not independently validated. The authors dodged the request to use, for instance, the Zimmer lab's data; the reason is unclear to me. Also, if anything, the authors themselves have at least one volume of sensible data from their own previous work (NeRVE, Nguyen et al., 2017) in which they actually did PCA on the GCaMP data. The least they can do is to apply fDNC to that set of data and show that PCAs are comparable.

d. Tracking is tracking, and should not be confounded with the discussion on neuron identification. The accuracy for tracking purposes should be discussed separately.

2. The authors cited a biorxiv paper (ref 22) and glossed over its contribution. This paper is now published (https://elifesciences.org/articles/59187). The major contribution of 3DeeCellTracker is also a deep learning algorithm for tracking cells, and the paper also dealt with the sort of data this manuscript addresses. There is no discussion and no comparison.

a. In fact, Wen et al. directly compared 3DeeCellTracker performance with other algorithms, including even on the dataset from Nguyen et al. (2017). The accuracies reported in Wen et al., are quite favorable (>90%). This data set should be directly compared.

b. fDNC may be faster, which suggests a trade-off between speed and accuracy. It seems pertinent to include this discussion.

3. The accuracy is a central claim in the paper. It is good that the authors now define what accuracy is in the text, but it is still confusing. A match between the template and the test does not assign a name necessarily, UNLESS the template neurons already have labels/identities from the ground truth information. From the text, it seems that the template IS used as the reference with identities already assigned, and that only the neurons common to both the test and template are considered since the denominator of the accuracy is defined as "the total number of ground truth matches". (Another interpretation of the definition would suggest that neurons that both the template and the test got wrong but matches each other would have been counted as accurate?!)

There are two issues – the definition is not applicable for some other methods and that this definition is artificially favorable for fDNC.

a. In Table 2, the authors compare the accuracies of fDNC to that of CPD and CRF (ref 3). This is not appropriate. fDNC and CPD both use template matching, while CRF does not. This is to say that the accuracy definition is not the same for these methods.

b. The accuracy of fDNC is artificially more favorable. NeuroPAL datasets do not reliably identify the same neurons. When using one NeuroPAL dataset as template, and another as the test set, the matches is on the order of 70-80%. The definition of accuracy the authors use, therefore, is artificially high (by some significant percentage). The errors associated in neurons NOT common to the test and the template are discounted.

c. It seems that the coverage and the accuracy discussion should be restored.
