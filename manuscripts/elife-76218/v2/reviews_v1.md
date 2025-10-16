# Peer review - Round 1

Editors:
- Marta Zlatic, https://ror.org/00tw3jy02 MRC Laboratory of Molecular Biology United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76218.sa0](https://doi.org/10.7554/eLife.76218.sa0)

Jia et al., present a valuable machine learning framework, Selfee, based on deep neural networks for analyzing video recordings of animal behavior, which is efficient and runs in an unsupervised fashion, and requires very little pre-processing. Selfee should be of broad interest to researchers studying quantitative animal behavior.


---

# Peer review - Round 1

Editors:
- Marta Zlatic, https://ror.org/00tw3jy02 MRC Laboratory of Molecular Biology United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76218.sa1](https://doi.org/10.7554/eLife.76218.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Selfee: Self-supervised Features Extraction of animal behaviors" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and K VijayRaghavan as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Mason Klein (Reviewer #1); Primoz Ravbar (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The Reviewers agree that the paper presents a really exciting method that could have broad impact on researchers studying quantitative animal behavior. However there are some unresolved issues for establishing the credibility of the method that we would like you to address.

Essential revisions:

1) Chose one or two strong and clean datasets and take them all the way through the analysis pipeline (selfee->anomaly score->AR-HMM->DTW) instead of using different experiments for explaining different points. We suggest removing IR76b data from the story unless the experiment can be somehow justified.

2) Also show Selfee's results on a simpler data set (with Drosophila or some other animal) with single-animal video.

3) Explain the rationale behind the choice of parameters for "Selfee". Please explain why Selfee performs so poorly without the CLD component. Would a simpler architecture, with the addition of CLD, achieve similar performance as the Selfee?

4) Explore the behaviors found in different parts of the t-SNE maps and evaluate the effect of the irrelevant features on their distributions. The t-SNE maps display several clusters representing the same behaviors (Figure 2D) which suggests strong overfitting (weak generalization). The authors should at least show some examples taken from different clusters. This would illustrate why Selfee is separating behaviors that humans perceive as a single category.

5) Provide a formal comparison with one of the pre-existing methods that would in theory work on the same videos (e.g. JAABA) (Posted 6th Apr 2022).

6) Provide a supplementary table showing full genotype of all experimental animals.

Reviewer #1 (Recommendations for the authors):

Overall I like the paper! I will try to give as many specific, detailed comments as possible in this section.

First, to clarify some of the items I listed under "weaknesses" in the public review:

(1) Since the paper feels mainly like a Selfee methods paper, I think spending more time describing what exactly Selfee is and how it works would be appropriate. I would recommend putting an expanded version of the Methods section paragraph (lines 925-933) in the main body of the paper, briefly explaining the techniques and existing software as you go through each step. It would give a reader with little machine learning experience a better understanding of the process.

(2) Efficiency was talked about in the introduction and occasionally brought up when highlighting that Selfee doesn't need large computational/processing power to operate, but I didn't come away with a sense of how much Selfee improves on other approaches in this regard. It would be helpful to be more specific.

(3) The comparisons with DeepLabCut make sense -- if it would be straightforward to compare to other software, that might help highlight unique aspects of Selfee a bit more effectively.

(4) I don't usually recommend new experiments when I review papers, but perhaps showing Selfee's results on a simpler data set (with Drosophila or some other animal), say with single-animal video, before showing the courtship-type results, could ease a reader into the process more effectively.

(5) It would also be great, if possible, to include a small section that could operate like a guide for a novice user to try Selfee on their own data.

A few general comments:

(1) I am not a machine learning expert myself, so I hope another reviewer could evaluate Selfee's uniqueness compared to other methods, as I am taking that at face value in my review. In particular, (line 17-19), is this true that unsupervised analysis has not been used this way before?

(2) A fair amount of grammar/word usage errors, not really a problem and I assume copy editors will address? (e.g. Fast --> Quickly or Rapidly on line 15).

(3) I generally like the figures, but found Figure 2 and Figure 3 pretty difficult to read at that size. Rearranging the panels and/or using larger fonts would help readability considerably.

Reviewer #2 (Recommendations for the authors):

This work is very relevant but has some serious unresolved issues before warranting further consideration. The overall format of the paper will also have to be massively restructured to make it palatable for a wide, life-science research audience.

Major points of concern that need to be addressed:

1) In the way it is presented, the rationale behind choice of several of the parameters for "Selfee" are unclear to me. E.g.

a. Why do the live frames consist of 3 tandem frames? Is 3 somehow a special number that is easy to compute or represent as an RGB image? Why not 4 with CMYK or a higher number with a distinct colormap as is commonly done for representing depth coding.

b. The choice of AR-HMM and DTW as post-processing steps after the Selfee analysis is also a bit unclear to me. Especially because the authors do not discuss any alternatives and moreover, they don't even show great promise in the examples later in the manuscript.

2) The authors have surprisingly failed to acknowledge and cite the state of the field that directly translates to their novelty claims (Lines 56-59: "There are no pose estimation paradigms that are designed to handle multi-animal contexts"). Both multi-animal DLC (Lauer et al., 2021) and SLEAP (Perreira et al., 2020) were explicitly designed for this purpose. Not to mention a plethora tools for multi-animal behavioral classification, especially during social interactions that provide pretty much all the extracted information obtained using Selfee in this manuscript. Listing a few Drosophila specific tools:

a. JAABA (Kaabra et al., Nat Methods, 2013)

b. Matebook (Ribeiro et al., Cell 2018)

c. Flytracker (Hoopfer et al., eLife 2015)

3) The authors must provide a sup table showing full genotype of all experimental animals. Wherever possible test and controls should be in the same genetic background (this is especially true for loss of function experiments where vision and locomotion is an integral part of the behavior, like the ones done in this manuscript). Legends for videos should also be provided.

4) Figure 2 demonstrates how good Selfee is at extracting information. To do this, authors have to either look at how data clusters with respect to human annotated labels on a t-sne map or use a k-nn classification step to classify the data. Honestly, the t-sne maps in Figure 2D don't look that promising. K-nn classification looks better with around 70% F1 score. But at this point there should be a formal comparison with one of the pre-exisiting methods that would in theory work on the same videos. I suggest JAABA (or Flytracker+JAABA) since similar labels have been previously extracted using this toolkit. Same holds true for mouse data (2G-I) and especially more important because the F1 scores here are a bit low. Also panels 2F and 2I likely represent cherry picked cases where results are much better than what the scores indicate and hence are not really informative.

5) The rationale for definition of "anomaly score" (Figure 3, lines 230-249) is again poorly defended in the text. Could authors clearly define what "meta-representations of frames" means. Also, why restrict k=1 for IES? How is the +-50 frame window chosen for IAS score. Are these empirically derived values after some trial and error, or based on some priors. Since the anomaly score is quite central to the overall utility of this tool, it needs to be proposed in a much more credible way.

6) The unusual subset of neurotransmitter mutants/silenced lines used in Figure 3 data makes one wonder if the provided data is a cherry-picked subset of the full data to make the story easier. I would really appreciate if all data were shown clearly and rationally. The authors really need to establish credibility for persuading the reader to use their method.

7) Trh mutant phenotype is interesting but interpretations of secondary assays warrant some more thought. Trh neurons directly innervate Drosophila legs (Howard et al., 2019, Curr Biol.) and impact locomotion. Making a claim about social repulsion is a bit too ambitious without further segregating impact on other behaviors like walking that could impact the phenotype observed by the authors.

8) Given that the utility of AR-HMM rests on IR76b experiments which seem to be based on a false premise, it would be best if authors repeat this with one of the myriad of receptors shown to be involved in courtship. Or rather just do AR-HMM on one of the previous datasets.

9) DTW is a cool method but using increased copulation latency of blind flies to show its usability is a bit of a short-sell. It does not in any way increase the credibility of this method and I would rather suggest using DTW to look at longer scale dynamics in previous experiments (e.g. Figure 3 data), provided these are done in the correct genetic background).

Recommendation for improvement: The point of this paper is the method and not the biological findings. But the method loses credibility because there are serious problems with the way the experiments are performed and data is presented. I would recommend the authors chose one strong and clean dataset and take it all the way through their analysis pipeline (selfee->anomaly score->AR-HMM->DTW) instead of using different experiments for explaining different points. Even if the results are less interesting, if the rationale is clear and all data is shown properly this will encourage other people to try out this tool.

Reviewer #3 (Recommendations for the authors):

The figures are in a good shape, except where specifically mentioned (and assuming that the final published figures will have better resolution).

Major concerns (2):

1) Reference [9] is critically important for the understanding of how the CLD is implemented in this architecture, however, I find it difficult to access the reference. The authors should provide for an alternative. Adding more visualization of how the CLD is implemented, in Figure 2, would be helpful. The authors should compare the classification performance of Selfee with and without the CLD (for fly courtship behavior in Figure 2). This way the reader could understand the weight of the CLD in the overall architecture. Next, the authors should discuss alternative architectures with CLD and show why the SimSiam has been chosen.

2) How much of the performance of the classification (and possibly other utilities) is lost to strict end-to-end processing? The authors should show the effects of the following pre-processing steps on the t-SNE maps, the confusion matrices, and the F1 scores: a) use the raw frames instead of live-frames; b) perform simple background subtraction; c) create narrow areas of interest around the animals in each frame. Authors can add other steps such as segmentation. The prediction would be that the classification performance will improve greatly, the t-SNE maps should have fewer yet more distinct clusters, and rare behaviors should be classified better than, for example, in Figure 2—figure supplement 5 F.
