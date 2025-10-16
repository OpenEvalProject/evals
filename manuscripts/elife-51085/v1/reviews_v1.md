# Peer review - Round 1

Editors:
- Robert H Singer, Albert Einstein College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51085.sa1](https://doi.org/10.7554/eLife.51085.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Both reviewers feel that the revisions are acceptable and feel that the analysis tool will be helpful to future investigations.

Decision letter after peer review:

Thank you for submitting your article "CytoCensus: mapping cell identity and division in tissues and organs using machine learning" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard White as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Hailstone et al. present CytoCensus, a supervised machine learning-based application for image analysis, which can be used to identify cells with specific attributes in 3-dimensional objects over time. Hailstone et al. first describe a new ex vivo brain culture technique they developed for time-lapse imaging and then use this technique to generate time-lapse data to test the performance of CytoCensus in identifying neuroblasts, compared to other available tools, namely Ilastik, Fiji-WEKA, RACE, and TrackMate. They found that CytoCensus outperforms all of them both in their data and in a neutral challenge dataset consisting of highly clustered synthetic cells. They then use CytoCensus to compare wild-type fly brains with sypRNAi brains, which are larger. They first exclude an increase in the number of neuroblasts and then find that the difference between the two brains is the division rate of the neuroblasts, which has as a result the production of more neurons. They also find a reduction in the cell cycle time of GMCs, which however does not contribute to the increase in size as the GMCs divide only once in both brains. They then use the proximity map output of CytoCensus to track individual NBs and verify the reduction in cell cycle length. Finally, they show that CytoCensus can also be used for developmental studies in other systems as well, testing it in zebrafish retinoids and early mouse embryos.

Essential revisions:

Both reviewers found the method useful but reviewer 2 felt that more unbiased and rigorous testing compared to other approaches were needed for benchmarking. In addition, this reviewer had questions about the novelty of the technique. After discussion, both reviewers were in agreement that improvements to the manuscript were needed.

1) The authors should discuss the novelty of their approach with respect to similar methods (Swiderska-Chadaj et al., 2018; Liang et al., 2019; Höfener et al., 2018).

2) The authors choose to use a Random Forest approach instead of using deep learning, which seems to be the best performing method for similar tasks and justify this choice by the hardware requirements of deep learning. However, it would be important to understand how large the drop in accuracy would be when compared to deep learning.

3) The authors should provide a convincing benchmarking: a) When comparing to image segmentation methods, the authors should provide a state-of-the art postprocessing scheme to make a fair comparison.

b) The authors should compare to the cell counting module available in Ilastik: https://www.ilastik.org/documentation/counting/counting.html

c) The authors should use challenge data to benchmark their results: Data Science Bowl challenge on nuclear segmentation (https://www.kaggle.com/c/data-science-bowl-2018). This challenge is on nuclear segmentation, but the authors could compare their method to the methods of a leading participant with respect to detection accuracy only.

4) The authors chose not to explain their method in the main text, which I find disturbing given that it is the major subject. The authors should describe their method in the main text in sufficient detail.

5) In the manuscript, there is a confusion between tools and methods. A software tool can be the concrete implementation of one method, but in most cases, a single tool (such as Ilastik) contains a range of methods. The authors should refer to both tool and method, in particular when they discuss benchmarking. In particular, they compare detection with segmentation methods, which is not rigorous.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "CytoCensus, mapping cell identity and division in tissues and organs using machine learning" for further consideration by eLife. Your revised article has been evaluated by Richard White as the Senior Editor, a Reviewing Editor and two peer reviewers.

The manuscript has been improved but there are some remaining issues from reviewer 2 that need to be addressed before acceptance, as outlined below. In particular the reviewer feels that the comparison with IIlastik needs to be fair and suggests an approach to represent this comparison more clearly.

Reviewer #2:

The authors have substantially improved the article and added a number of benchmarking results which make the manuscript stronger and the presented tool more convincing. I still believe that the result shown in Figure 3 needs to be replaced, as detailed below.

While the level of novelty remains relatively low, at least from a methodological point of view, I agree that the tool can be of much use to the community, thanks to its capacity of dealing with 3D data.

Detailed comments:

1) As mentioned in my previous review, I still do not agree with the way the results are presented in Figure 3: the authors compare their results to Ilastik. Concretely, they use Ilastik to segment cells (via pixel-classification). In a second step, they calculate the cell centers from this segmentation result as the centers of the connected components. An example of this is shown in Figure 3B' (2 quotes, upper right) and the corresponding statistics in Figure 3B' (4 quotes, bottom left). The problem with this benchmark is that this is not a reasonable approach for cell center detection. For this reason, I feel that the comparison is misleading and should not be published in this way. Normally, one would always try to apply at least some simple postprocessing for object splitting, prior to calculating the centers. The authors did this additional analysis (cited in the text) in the revised version of the manuscript, and achieved 0.88 ± 0.09 vs. 0.98 ± 0.05 with CytoCensus. This is the proper result to be reported. The difference is less striking, but it is also more realistic and will ultimately convince the readers more than the version that is currently in the manuscript. I therefore require that the Figure 3B' (4 quotes, bottom left) and Figure 3B' (2 quotes, upper right) are replaced by the corresponding figures from this more realistic scenario. The comparison to Ilastik pixel classification without post-processing should be removed.

2) Regarding the results presented in Figure 3—figure supplement 2, the authors should also provide the rank of their method (ranked x out of N participants).
