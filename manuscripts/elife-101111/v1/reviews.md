# Peer review - Round 1

Editors:
- Jesse H Goldberg, Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101111.3.sa0](https://doi.org/10.7554/eLife.101111.3.sa0)

This work introduces a new Python package, Avian Vocalization Analysis (AVN) that provides several key analysis pipelines for birdsong research. This tool is likely to prove useful to researchers in neuroscience and beyond, as demonstrated by convincing experiments using a wide range of publicly available birdsong data.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101111.3.sa1](https://doi.org/10.7554/eLife.101111.3.sa1)

Summary:

In this work, the authors present a new Python software package, Avian Vocalization Network (AVN) aimed at facilitating the analysis of birdsong, especially the song of the zebra finch, the most common songbird model in neuroscience. The package handles some of the most common (and some more advanced) song analyses, including segmentation, syllable classification, featurization of song, calculation of tutor-pupil similarity, and age prediction, with a view toward making the entire process friendlier to experimentalists with limited coding experience working in the field.

For many years, Sound Analysis Pro has served as a standard in the songbird field, the first package to extensively automate songbird analysis and facilitate the computation of acoustic features that have helped define the field. More recently, the increasing popularity of Python as a language, along with the emergence of new machine learning methods, has resulted in a number of new software tools, including the vocalpy ecosystem for audio processing, TweetyNet (for segmentation), t-SNE and UMAP (for visualization), and autoencoder-based approaches for embedding.

As with any software package, this one necessarily makes a number of design choices, which may or may not fit the needs of all users. Those who prefer a more automated pipeline with fewer knobs to turn may appreciate AVN in cases where the existing recipes fit their needs, while those who require more customization and flexibility may require a more bespoke (and thus code-intensive) approach.

Strengths:

The AVN package overlaps several of these earlier efforts, albeit with a focus on more traditional featurization that many experimentalists may find more interpretable than deep learning-based approaches. Among the strengths of the paper are its clarity in explaining the several analyses it facilitates, along with high-quality experiments across multiple public datasets collected from different research groups. As a software package, it is open source, installable via the pip Python package manager, and features high-quality documentation, as well as tutorials. For experimentalists who wish to replicate any of the analyses from the paper, the package is likely to be a useful time saver.

Weaknesses:

I think the potential limitations of the work are predominantly on the software end, with one or two quibbles about the methods.

First, the software: It's important to note that the package is trying to do many things, of which it is likely to do several well and a few comprehensively. Rather than a package that presents a number of new analyses or a new analysis framework, it is more a codification of recipes, some of which are reimplementations of existing work (SAP features), some of which are essentially wrappers around other work (interfacing with WhisperSeg segmentations), and some of which are new (similarity scoring). All of this has value, but in my estimation, it has less value as part of a standalone package and potentially much more as part of an ecosystem like vocalpy that is undergoing continuous development and has long-term support. While the code is well-documented, including web-based documentation for both the core package and the GUI, the latter is available only on Windows, which might limit the scope of adoption.

That is to say, whether AVN is adopted by the field in the medium term will have much more to do with the quality of its maintenance and responsiveness to users than any particular feature, but I believe that many of the analysis recipes that the authors have carefully worked out may find their way into other code and workflows.

In the revised version of the paper, the authors have expanded their case for the design choices made in AVN and remain committed to maintaining the tool. Given the low cost for users in trying new methods and the work the authors have put into further reducing this overhead via documentation, those curious about the package are likely best served by simply downloading it and giving it a try on their own data.

Second, two notes about new analysis approaches:

(1) The authors propose a new means of measuring tutor-pupil similarity based on first learning a latent space of syllables via a self-supervised learning (SSL) scheme and then using the earth mover's distance (EMD) to calculate transport costs between the distributions of tutors' and pupils' syllables. While, to my knowledge, this exact method has not previously been proposed in birdsong, I suspect it is unlikely to differ substantially from the approach of autoencoding followed by MMD used in the Goffinet et al. paper. That is, SSL, like the autoencoder, is a latent space learning approach, and EMD, like MMD, is an integral probability metric that measures discrepancies between two distributions. (Indeed, the two are very closely related: https://stats.stackexchange.com/questions/400180/earth-movers-distance-and-maximum-mean-discrepency) Without further experiments, it is hard to tell whether these two approaches differ meaningfully. Likewise, while the authors have trained on a large corpus of syllables to define their latent space in a way that generalizes to new birds, it is unclear why such an approach would not work with other latent space learning methods.

Update: The authors now provide an extensive comparison with the Goffinet et al. paper and also consider differences between MMD and EMD. This comparison both adds value to the original paper and provides useful benchmarking for others looking to develop latent space comparison methods.

(2) The authors propose a new method for maturity scoring by training a model (a generalized additive model) to predict the age of the bird based on a selected subset of acoustic features. This is distinct from the "predicted age" approach of Brudner, Pearson, and Mooney, which predicts based on a latent representation rather than specific features, and the GAM nicely segregates the contribution of each. As such, this approach may be preferred by many users who appreciate its interpretability.

In summary, my view is that this is a nice paper detailing a well-executed piece of software whose future impact will be determined by the degree of support and maintenance it receives from others over the near and medium term.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101111.3.sa2](https://doi.org/10.7554/eLife.101111.3.sa2)

This paper introduces the Avian Vocalization Network (AVN), a novel birdsong analysis pipeline using deep learning. By automating vocal annotation tasks, the AVN generates interpretable song features and song similarity scores on novel datasets without retraining. The performance of the network is solid and is comparable to that of human annotators.

The authors have improved the manuscript in several aspects, such as the comparison with the Goffinet work. Overall, the AVN feature set could become a useful tool for evaluating birdsongs. But the authors also chose not to address a certain number of criticisms, and some issues remain poorly addressed, and the work is not reproducible at this stage. With a little effort, these issues could get resolved in my view. I will just pick on four issues that I think can be easily addressed:

(1) Limitation of feature set: They claim that AVN satisfies the criteria (line 60) of "creating a common feature space for the comparison of behavioural phenotypes ..."(line 51), but then on LDA analysis, explained on line 910 they say "excluding amplitude and amplitude modulation features as they were found to vary". Since their feature set is not stable and not truly 'common' to all tasks, this limitation needs addressing in the discussion (that some features seem to vary undesirably, and they need exclusion based on some criteria to be defined).

(2) Missing information on classification training loss: The Authors insist that their triplet loss is not related to classification, and they brush off my request for more information. In their rebuttal, they write: 'The loss function is related to the relative distance between embeddings of syllables with the same or different labels, not the classification of syllables as same or different.' Perplexingly, however, in the revised paper, authors speak themselves of 'classes', in Line 1004: this allows the model to begin learning an easier task, of separating syllables of different classes by a smaller margin.' So it seems the authors actually agree with me that there is an underlying classification task. I am therefore going to make it a bit more explicit here what I'm asking for, hoping this will better resonate with them.

In line 984 they define their loss function and in lines 994-996 they define 'hard' and 'semi-hard' triplets. Authors then train a system to minimize the loss with a ratio of 75 percent semi-hard triplets and 25 percent hard triplets and a final weighing parameter value alpha=0.7. What I'm asking for is this 'classification' loss their trained model achieves, or in other words, the fraction of triplets that end up producing a loss, either of the 'hard' or 'semi-hard' type. For example, if their model manages to separate all 'possible triplets' by a margin of at least alpha, then the loss would be zero. If the model achieves to separate all triplets except one, then the loss would correspond to the amount by which the separation differences between the anchor and the positive vs negative samples exceeds alpha. So, an important number to provide in the paper is the fraction of triplets that incur a nonzero loss, i.e., the fraction of semi-hard triplets. And another important quantity is the fraction of hard triplets, i.e. the fraction of triplets that would incur a loss if alpha were set to zero, or, in other words, the triplets for which the negative sample is closer to the anchor than the positive sample. By the way, I assume this latter fraction of hard cases will be zero - that their model does not confuse any positive and negative training samples...

Note: the quantification chosen by the authors termed 'contrast index' is interesting, but it is a derived quantity, it is not the quantity authors chose to optimize during training. If authors were to report both the training loss achieved and the 'contrast index', follow-up work could be benchmarked against both these quantities. If for example, a follow-up model achieves smaller loss but worse contrast, then the loss is not a good placeholder measure for optimizing contrast. Alternatively, follow-up work could focus on the contrast index as training objective, obliterating the need for the triplet loss as an intermediate step (I don't buy the authors' argument that such an optimization would be infeasible).

(3) Reproducibility: they explain the way they train the CNN with triplet loss to produce the embeddings, but we're missing both actual scripts on GitHub to train and inference from scratch, and model weights, or even hyper parameters they used. Authors only provide the architecture, and I don't think that's enough to be considered replicable in today's standards. I would suggest they release complete model checkpoint weights for the result they report, the exact data splits, the hyper parameters they used and training and testing code, so that one can very easily verify their claims and apply their methods to other datasets. Note: for example, the code to extract the embeddings is incomplete (the function definition of single_bird_extract_embeddings cannot be found on GitHub) and the model weights they used are missing.

(4) With regards to the age prediction model, the authors should specify that this model is mainly useful for comparisons across studies but less so for precise evaluation of the effects of a treatment within a study. Namely, the effect on song of a treatment is best assessed by comparison to within-subject past song, and by comparison to age-matched control birds (ideally siblings) raised in identical conditions, rather than to invoke a generic model trained on other birds and from different colonies and breeding conditions as authors propose to do. In other words, to introduce a generic model for evaluation of song maturity introduces measurement noise in terms of the additional birds and their variable conditions, which can hinder precise assessment of treatment effects. Note that to state that in past work such maturity models were used is not a good justification, scientifically speaking.

Finally, the authors write that methods for syllable segmentation have not been systematically compared but the whisperseg work they use did such a comparison. So the authors should revise their novelty claim of being the first to compare syllable segmentation methods.
