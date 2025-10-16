# Peer review - Round 1

Editors:
- Marius V Peelen, https://ror.org/016xsfp80 Radboud University Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74943.sa0](https://doi.org/10.7554/eLife.74943.sa0)

This well-conducted study uses relatively large sample sizes, comprehensive statistical testing, and state-of-the-art modeling to provide novel evidence that human infants generalize shape from single examples on the basis of the "shape skeleton", a structural description of the part structure of the shape. It will be of interest to researchers working on object shape processing and on the development of visual perception.


---

# Peer review - Round 1

Editors:
- Marius V Peelen, https://ror.org/016xsfp80 Radboud University Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74943.sa1](https://doi.org/10.7554/eLife.74943.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "The shape skeleton supports one-shot categorization in human infants: Behavioral and computational evidence" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

Specifically, the reviewers thought that results may be alternatively explained by motion similarity and/or low-level visual similarity between habituation and test stimuli, as explained in more detail below.

Reviewer #1:

This is a very lucidly written article on a fascinating and important topic: how humans are able to learn novel visual categories based on few or even just one single example. This ability can be contrasted with conventional machine learning models which typically require massive data sets with thousands of training examples to learn the ability to categorize novel examples accurately. How humans generalize so well from such sparse training data remains poorly understood and working out how we achieve this is important not only for the psychological sciences, but also has implications for artificial intelligence and machine learning too.

The authors start with a strong premise, which is also likely to be true: a crucial aspect of human one-shot visual learning likely involves the perceptual processes that segment observed shapes into parts and represent them as a hierarchy of limbs, in a representation known in the field as 'shape skeletons'. There is a long history of evidence suggesting the human visual system analyses shape in this way, and such representations naturally lend themselves to abstractions and generalizations that are robust against significant variations in appearance, such as the surface structure and even pose of objects. While this is an excellent starting point for investigating one-shot learning, the idea that such representations might play a role in human visual categorization more generally is rather well accepted in the field, and thus perhaps not so original on its own. The potential novelty and importance of the contribution therefore rests on demonstrating that such representations are central to one-shot learning in particular.

Unfortunately, due to their choice of stimuli, I believe that the experiments the authors perform do not yet provide compelling evidence that the infants' looking times are driven by skeletal representations, or indeed whether one-shot learning is necessarily playing a role in their habituation.

The problem is that the different Surface Forms of each Skeleton are more similar to one another than those of the other Skeletons, in terms of the raw pixel similarity. I took screenshots of the stimuli from the MS and compared them in MATLAB. For 7 out of 10 possible comparisons, the corresponding Surface Forms from the same 'category' are closer in raw pixel terms than to any of the rivals. This leads me to believe that the pattern of results is based on the raw physical (and thus perceptual) similarity between the habituation and test stimuli, rather than based on one-shot generalization per se, or on skeletal representations of the shapes in particular. In my opinion, the fact that sophisticated artificial neural network models don't predict this is not in itself strong evidence against my suggested explanation of the findings.

In future studies, this issue could be addressed by using stimuli for which this confound is not a problem. This could be achieved, for example, by using additional transformations of the objects, such as rotations, that preserve part structure but radically alter the projected image of the objects. This way skeletal structure could be decoupled from straightforward image similarity, and a stronger case for generalization beyond the 'one-shot' training exemplar would be provided.

Reviewer #2:

This is an important paper. The issue of "one-shot" learning---how people can learn categories and concepts from a single example or set of examples---lies at the heart of the current controversies over "deep learning" models. These models are ubiquitous these days and are often promoted as descriptive models of human learning, but they inherently require many trials to learn. But human learners can often learn from single trials, presenting a fundamental challenge to the entire deep learning paradigm. This has been pointed out in broad terms before, but to really advance this debate, a study needs to establish that humans can indeed learn from single examples, simultaneously demonstrate that appropriate deep learning models cannot, and explain something about exactly what why---all of which this paper accomplishes with impressive rigor.

In that context, the paper specifically studies shape category learning by human infants, a particularly interesting case, and establishes a specific pattern: that infants generalize shape categories based on the "shape skeleton," a structural description of the part structure of the shape. That is, infants exposed to a single shape with a particular shape skeleton tend to be "unsurprised" by other shapes with the same skeleton, but more surprised by shapes with different skeletons, indicating that the single example was enough to establish in their minds an apparent shape category.

This generalization is in a sense unsurprising, because the shape skeleton is supposed to define characteristic "invariants" within shape categories, but it is nevertheless novel. Although the tendency for infants to generalize lexical categories based on shape is well established, the precise nature of one-shot shape generalizations has not previously been studied. For researchers in shape this is a very important result, and for anybody interested in how humans learn categories I think is is both fundamental and thought-provoking.

I found the methodology and statistical analysis in the paper comprehensive and rigorous, and the writing clear, so and have only relatively minor comments on the manuscript, which follow. I don't see page numbers, so give quotations to indicate the relevant location.

– "a phenomenon known as 'one-shot categorization'" – The issue of one-shot category learning, and the computational question of what makes it possible for human learners to instantly generalize from some examples but not others, has been studied somewhat more extensively than this very brief introduction lets on. I would point to for example Feldman (1997, J. Math Psych) which explicitly takes it up and argues for a mechanism related to the current paper (namely, that one-shot categorization is possible when the one example implies a highly specific structural model).

– "However, one might ask whether these findings are truly indicative of categorization, or simply better discrimination of objects with the different skeletons." I'm not sure these are really different explanations. Learners are better at discriminating objects that appear to be from different categories (categorical perception, etc.).

– "infants' looking times on the first test trial did not differ for within- and between-category test objects" – This claim is followed by a non-significant NHST test, which does not allow an affirmative conclusion of no difference here, and a Bayes Factor, which does. The NHST test really doesn't add anything. I personally think these tests could be omitted throughout the paper in favor of the more informative BFs – but particularly when null results are discussed.

– members from different -> members of different.

– "we tested models by feeding their outputs into an autoencoder and measuring the error signal across habituation and test phases (see Methods)." I didn't quite get this. To evaluate similarity within the network models, can't one use a Euclidean norm or a cosine? Please clarify.

– "but did not differ from one another" – Meaning what? Low BF? If so, please give BF.

– "it has remained unknown whether one-shot categorization is possible within the first year of human life." Has this really never been established, even for simple categories? Anecdotally, infants seem to do one-shot learning all the time.

– "Moreover, V2 and V3 are evolutionarily preserved in primate and non-primate animals" I think the entire discussion of neural analogs here is misleading. I am not a bird expert but I didn't think birds have homologous visual cortical areas to primates. But that doesn't matter, because functional organization is analogous when computational problems are analogous. In other words, birds don't generalize the same way we do because they have V2 areas like us, but because they are solving problems like us.

– "set was comprised of two…" -> "set comprised two…" Use of "comprised of" to mean "composed of" is colloquial. The US comprises states, not the other way around.

Reviewer #3:

This study relates habituation in infants to categorization in neural networks, showing that infants learn (as evidenced by looking times) shape skeletons across surface form, while neural networks that lack an explicit skeletal representation do not show this generalization. A key aspect of the study is that infants are only exposed to one exemplar, suggesting that infants learn shape skeletons using "one-shot categorization". The study is well-conducted, using relatively large sample sizes, comprehensive statistical testing, and careful modelling. The manuscript is well-written and easy to follow. However, results may be alternatively explained by motion similarity and/or low-level visual similarity between habituation and test stimuli.

– The shapes are shown as videos during both habituation and test phases. While I understand that this was preferred for drawing the infants' attention, it complicates the interpretation of the results. First, it becomes hard to disentangle the learning of the shape skeleton from the learning of the motion trajectory. Second, the comparison with neural networks becomes more difficult as these neural networks are not sensitive to motion.

– Because surface form differed for both test objects, the same-skeleton object will be visually more similar to the habituated object than the different-skeleton object. Therefore, it cannot be ruled out that results reflect habituation to lower-level stimulus properties rather than shape skeleton. This is also suggested by recent fMRI results using these stimuli (Ayzenberg et al., Neuropsychologia 2022), showing that the skeletal model correlates with activity patterns throughout the visual system, including V1 (though the cross-surface form results are only shown for V3 and LO, as far as I could tell).

I would recommend the authors to include a discussion of the possible contributions of motion and non-skeletal visual properties to the habituation results.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for choosing to send your work entitled "The shape skeleton supports one-shot categorization in human infants: Behavioral and computational evidence" for consideration at eLife. Your letter of appeal has been considered by a Senior Editor and a Reviewing Editor, and we are prepared to consider a revised submission with no guarantees of acceptance.

In addition to the comments of the previous reviews, during the consultation of the appeal, the following questions came up:

1. What new insight do we gain from the infant study above and beyond what we already know from adults?

2. Why do you think that (dis)habitation is evidence of learning per se, rather than comparisons of perceptual similarity between items?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The shape skeleton supports one-shot categorization in human infants" for further consideration by eLife. Your revised article has been evaluated by Floris de Lange (Senior Editor) and a Reviewing Editor, in consultation with reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The reviewers were not convinced that the experiments convincingly demonstrate “one-shot” categorization. This concern can be addressed by adjusting the headline claim throughout (title, abstract, intro, results and discussion would need some modifications). A suggested alternative title could be: "The shape skeleton supports shape similarity judgments in human infants".

The design involves making a judgment about which objects appear to be more similar. This requires comparing the distances between presented items (in some feature space describing the stimuli). Making such a comparison doesn't involve learning anything on the basis of the experience. It doesn't involve generalization and there is no sense in which it is a 'one-shot' task, except that a given trial presents only a few items. But this is true of practically ANY experiment involving comparing a small number of items.

Here is an analogy: suppose the infants were shown three different (i.e., easily discriminable) patches of gray shades: two patches are relatively light shades of gray and one is a significantly darker shade. A habituation experiment like the one the authors performed would reveal that the infants see the two light grays as more similar than the darker one. But in what sense is this 'one shot categorization'? The infants wouldn't have learned a new category. There is no meaningful generalization. The experiment simply reflects the fact that similar grays look more similar than more different ones.

The same is true in the authors' experiments. The experiments demonstrate that objects with more similar skeletons appear more similar to infants. This is not a trivial result, and is worthy of publication in its own right (although similar findings have already been shown in adults). However not under the title of 'one-shot categorization'. Instead, it should be pitched (correctly) as the shape skeleton contributing substantially to judgments of shape similarity.

To reiterate: I think the authors have performed an elegant study with some interesting findings. I think their interpretation can certainly be discussed in the MS. However, the headline claim about one-shot categorization should be toned down. Otherwise, the term would 'one-shot' would not mean anything anymore.
