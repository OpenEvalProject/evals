# Peer review - Round 1

Editors:
- David C Van Essen, Washington University in St. Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.28728.030](https://doi.org/10.7554/eLife.28728.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article " Efficient and accurate extraction of in vivo calcium signals from microendoscopic video data" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by David Van Essen as the Senior Editor and Reviewing Editor. One of the reviewers was Dr Timothy Holy (Reviewer 2); the other two have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission. With regard to the issue raised with you by email as to whether the new algorithm's success is perhaps more of an accident of initialization than a reflection of good statistical design, the reviewers found your response to be thoughtful and helpful, but not entirely convincing. We therefore plan to ask the original reviewers to take another look at your revised manuscript before making a final decision.

Summary:

This is an excellent paper showing how the CNMF technique has been adapted for use with 1-P calcium imaging in endoscopic data. The paper is for the most part clearly written, and the simulations backed up by the in-vivo imaging data clearly demonstrates that this technique is by far superior to any other currently being used, including ICA/PCA or other variations. It builds on previous work from Pnevmatikakis and colleagues, differing primarily in the statistical model used to describe the background. It will likely be essential to use this technique to obtain the highest quality data, as background fluctuations and cross-talk between neurons can severely impact the data recorded.

However, some aspects of the analysis are difficult to judge, and there are a number of concerns and recommendations raised by the reviewers.

Essential revisions:

1) It is important to discuss carefully to what degree this new algorithm's success reflects more of an accident of initialization than good statistical design. Given that (a) SVD will always produce a lower reconstruction error than NMF for the same number of components, and that (b) having a high background might allow the neural components to "insulate" themselves from the constraints of nonnegativity by offsetting them from zero, it seems possible that the model also admits solutions that are better from the standpoint of the loss function yet worse from the standpoint of biological plausibility. As a consequence, it may only be the initialization causing the algorithm to land in a local (but far from global) minimum that is leading to the kinds of plausible solutions exhibited in the manuscript; the risk is that a more exhaustive optimization algorithm, applied to the same data and model, would prefer solutions that lack this plausibility.

2) The exposition of the CNMF-E algorithm in this paper could stand to be improved substantially. It is extremely hard (or, really, impossible) to make sense of the details of the proposed algorithm as presented in this paper! While the big picture of the algorithm is clear from a quick glance at Equation 8, the details are not clear from the many pages of text that follow.

3) There are concerns about how well the technique would work if the true firing correlations increase. Can the authors do a simulation where they increase pair-wise correlations between the deltaF traces systematically and see at what point segmentation breaks down or cross-talk removal artificially lowers the correlations.

4) Please provide more practical advice about how to implement the software. This method is very computationally intensive, and some direction needs to be given on how to run the software to allow a large number of movies to be analyzed in a reasonable amount of time. There are no benchmarks given (from my reading) on how long the analysis takes per minute of recording and how this can be optimized.

5) Please comment on success of being able to segment the same region over several recordings over days and match up neurons across days?

6) The authors should also present what happens when they iterate their model to full convergence (e.g. square root of the machine precision) and discuss the heuristics they use to choose when to terminate the iteration early.

7) How does the quality of the neuronal reconstruction compare if you just use CNMF on the spatially-filtered (and 0-truncated) image? If it performs similarly, it's not entirely clear that this more complex model represents much of an advance.

8) It is mentioned in subsection “in vivomicroendoscopic imaging and data analysis” that manual interventions were applied in the data analysis shown in this paper. This makes the comparisons shown in this paper unfair to competitors that are fully automated (since of course any method can be improved using manual intervention). Can the authors show results of CNMF-E without manual intervention? Also, how much manual investment (time, numbers of each type of decision, etc.) is necessary, and how much the manual intervention improves the result.

9) How does CNMF-E fare against CNMF when applied to two-photon data? i.e., when the additional flexibility of the model is perhaps not essential, does this extra flexibility degrade the performance in some fashion?

10) It is important to make the data and the scripts available for recreating the figures shown in this paper, for both the simulated and the real data. Otherwise it will be very hard for others to apply CNMF-E and get comparable results, given the many tuning parameters and semi-manual interventions involved.

11) What happens if one passes in the initialization described in subsection “Initialization of model variables” to the CNMF algorithm or to other competitors in the literature?

Reviewer #1:

This is an excellent paper showing how the CNMF technique has been adapted for use with 1-P calcium imaging in endoscopic data. The paper is very clearly written, and the simulations backed up by the in-vivo imaging data clearly demonstrates that this technique is by far superior to any other currently being used, including ICA/PCA or other variations. In fact, it will be essential to use this technique to obtain the highest quality data as background fluctuations and cross-talk between neurons can severely impact the data recorded.

These are my concerns:

1) I have some concerns about how well the technique would work if the true firing correlations increase. Can the authors do a simulation where they increase pair-wise correlations between the deltaF traces systematically and see at what point segmentation breaks down or cross-talk removal artificially lowers the correlations.

2 I felt that the authors could provide more practical advice about how to implement the software. This method is very computationally intensive, and some direction needs to be given on how to run the software to allow a large number of movies to be analyzed in a reasonable amount of time. There are no benchmarks given (from my reading) on how long the analysis takes per minute of recording and how this can be optimized.

3) Can the authors comment on success of being able to segment the same region over several recordings over days and match up neurons across days?

Reviewer #2:

The manuscript by Zhou and colleagues presents a computational method for extracting calcium signals from neurons in images that are "corrupted" by high background, with a specific interest in microendoscopic recordings. It builds on previous work from Pnevmatikakis and colleagues, differing primarily in the statistical model used to describe the background. The authors present several examples using both simulations and real experimental data to demonstrate the characteristics of their new method. In comparison with their previous method and a PCA/ICA method, the authors show examples where the new method outperforms the previous one.

The manuscript has many strengths, including the application to several different in vivo data sets and the realistic-looking simulated (with available ground truth) data sets. The model also seems thoughtfully designed, and considerable effort was made to ensure that it will be practical at least for data sets of the size of typical endoscopic recordings. The figures are mostly clear except as noted below.

Overall, this may be a worthy addition to the armamentum of methods; however, some aspects of the analysis are difficult to judge, and my overall assessment is that its importance is not yet clear. My major questions/concerns are:

1) First, this reviewer doesn't fully understand why/how the background/foreground separation works. Loosely, the model is of the form `Y ≈ b + a*c`, where `b` is the background and `a` and `c` are the spatial/temporal components of the neurons. In previous work they argued that a non-negativity constraint on `a` and `c` led to substantial improvement over unconstrained methods and effective separation of the neurons from a (small) background. However, in this case `b` is of quite large magnitude, and one might expect this to effectively "relax" the constraint on `a` and `c`: the model could fit a smaller value for `b` in the vicinity of a neuron, allowing `a` and `c` to take on larger positive values and thus "cushioning" them against the impact of the nonnegativity constraint. In a sense, one might imagine that the fully-converged result would not be terribly different from a (sparse, local) singular value decomposition, which is known to not properly segment cells particularly in the presence of temporal correlations among nearby/overlapping cells.

Nevertheless, the temporal traces exhibit the characteristics expected from a "meaningful" nonnegative factorization. So, the question is, why? One possible answer is that the authors are not iterating their model to convergence, and that an intermediate initialization via a "meaningful" nonnegative step still has substantial influence over the final form of the solution. If this is the case, the authors should also present what happens when they iterate their model to full convergence (e.g. square root of the machine precision) and discuss the heuristics they use to choose when to terminate the iteration early.

2) For the real datasets they initialize the neuronal factorization using a high-pass spatial filtering of the raw image, then reintroduce the full image and fit the complete model. But in the end, we're mostly interested in the neurons, and we may not really care that much about an accurate model of the background. How does the quality of the neuronal reconstruction compare if you just use CNMF on the spatially-filtered (and 0-truncated) image? If it performs similarly, it's not entirely clear that this more complex model represents much of an advance.

It's possible that there's a bit of data in the manuscript on this point (Figure 4B, black dots), but to this reviewer it's not clearly described, and this is shown only for simulated data. If you don't know the ground truth, would you care about the difference between 0.99 similarity and 0.999 similarity?

3) The authors describe some manual interventions in the methods, but there does not appear to be much in the way of description of exactly how these interventions were leveraged. It would be helpful to readers to understand what the "raw" output of the unsupervised algorithm really looks like, how much manual investment (time, numbers of each type of decision, etc.) is necessary, and how much the manual intervention improves the result.

Related to these points (particularly the first two), how does CNMF-E fare against CNMF when applied to two-photon data? i.e., when the additional flexibility of the model is perhaps not essential, does this extra flexibility degrade the performance in some fashion?

Reviewer #3:

This paper introduces the CNMF-E algorithm for extraction of neurons from 1-photon calcium imaging data.

1) First and foremost, CNMF-E has quickly become widely-adopted by scientists who are collecting micro-endoscopic video data. Clearly this paper is very high impact and deserves to be published in a prominent journal. I congratulate the authors for an important piece of work, which will surely have a sustained and important impact on the field.

2) I'm concerned about the semi-manual "interventions" described in subsection “Interventions”. It is mentioned in subsection “in vivomicroendoscopic imaging and data analysis” that manual interventions were applied in the data analysis shown in this paper. This makes the comparisons shown in this paper unfair to competitors that are fully automated (since of course any method can be improved using manual intervention). Can the authors show results of CNMF-E without manual intervention?

3) The CNMF-E algorithm is just a slight tweak on CNMF, which is itself a pretty standard matrix factorization. This lack of statistical innovation is probably OK, though, since eLife is not looking to publish innovative statistical methodology, but rather an algorithm that works well and has very high impact.

4) I feel very strongly that the exposition of the CNMF-E algorithm in this paper could stand to be improved substantially. It is extremely hard (or, really, impossible) to make sense of the details of the proposed algorithm as presented in this paper! While the big picture of the algorithm is clear from a quick glance at Equation 8, the details are not clear from the many pages of text that follow. When I read a statistical- or computational-focused paper, I wonder "would a statistically/computationally-literate reader of this paper be able to re-implement this algorithm, from scratch, based on the description of this paper?" The answer to that question is definitely "no". More details about this are provided below.

5) It is really wonderful that the authors have easy-to-use code available for the CNMF-E algorithm! However, it is also very important that they post scripts online recreating the figures shown in this paper, for both the simulated and the real data. For instance, I'd like to see a script that one can simply call into matlab that will read in the mouse dorsal striatum data and output exactly the results shown in Figure 5. (A similar request applies to the other figures). This is particularly important in light of the "semi-manual interventions" mentioned in my point 2 above. Furthermore, the actual data used to make the figures (e.g. the calcium recordings for the mouse dorsal striatum area that were used to make Figure 5) should be made available.

Without the availability of the data and a script to get the results shown in the paper, I think it will be very hard for others to apply CNMF-E and get comparable results, given the many tuning parameters and semi-manual interventions involved. It will also be very hard for others to objectively evaluate how well CNMF-E works, and how sensitive the results in this paper are to tuning parameter selection, etc.!

6) I think that most of the benefit of CNMF-E over CNMF comes from the careful initialization of the algorithm described in subsection “Initialization of model variables”, rather than from the details of the optimization problem Equation 8. What happens if one passes in the initialization described in subsection “Initialization of model variables” to the CNMF algorithm or to other competitors in the literature?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Efficient and accurate extraction of in vivo calcium signals from microendoscopic video data" for further consideration at eLife. Your revised article has been favorably evaluated by David Van Essen (Senior Editor and Reviewing Editor), and the original three reviewers.

The manuscript has been improved but there are two small remaining technical points that need to be addressed before acceptance, as outlined below. Both should be easy to address.

1) In subsection “Fitting the CNMF-E model”, the optimization problem (P-All) needs to list s and B^f as optimization variables (i.e. they should appear under 'minimize'). While the reviewer agrees with the authors that "s_i is completely determined by c_i and G^{(i)}, and B^f is not optimized explicitly", nonetheless s_i and B^f are optimization variables. This is actually just a fundamental math issue that has nothing to do with the specifics of the paper at hand!

To understand this point, consider the optimization problem "minimize_{x,y} f(x,y) s.t. x=y". It would NOT be correct to instead write this as "minimize_x f(x,y) s.t. x=y", EVEN THOUGH (to quote the authors), "x is completely determined by y". (Why is "minimize_x f(x,y) s.t. x=y" incorrect? Well, unless y is listed as an optimization variable, then it is treated as a constant in the optimization problem; therefore, the solution to that problem is trivially just x=y, with minimum value attained at f(y,y).)

Thus, (P-All) is simply incorrect as written. The fix is simple: put "s_i" and "B^f" under the "minimize".

2) In a couple of places (e.g. subsections “Fitting the CNMF-E model”and” Ranking seed pixels”) it is mentioned that (P-All) is not jointly convex in the optimization variables. Unfortunately, though this statement is true, it is misleading: when we say that a problem is not "jointly convex", we are implying that it is convex in the individual optimization variables. By contrast, (P-All) isn't even convex in the individual optimization variables. This is because details aren't provided of what (for instance) "is sparse" means. If that means that the l1 norm is penalized, then yes, it is convex in the individual optimization variables. But if it means some other notion of sparsity, e.g. that the l0 norm is penalized, then (P-All) isn't convex in the individual optimization variables.

Therefore, the reviewer feels that stating that (P-All) is "not jointly convex" or "jointly non-convex" is misleading and should be removed from the text where it appears. The authors should instead just say "non-convex" without the word "jointly".
