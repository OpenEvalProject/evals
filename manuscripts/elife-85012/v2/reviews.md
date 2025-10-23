# Peer review - Round 1

Editors:
- Andrea E Martin, https://ror.org/00671me87 Max Planck Institute for Psycholinguistics Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85012.sa0](https://doi.org/10.7554/eLife.85012.sa0)

Brodbeck et al. offer a timely and important contribution to how neural signals in response to continuous temporal modulations (as seen in speech and language processing) can be modelled effectively using temporal response functions. They offer a compelling new approach that includes a novel application of a boosting algorithm in addition to an accessible and didactically useful toolbox for analysis. A comparison of boosting and ridge regression via simulation shows the important impact on methods in speech and language neuroscience, as well as in cognitive neuroscience more broadly.


---

# Peer review - Round 1

Editors:
- Andrea E Martin, https://ror.org/00671me87 Max Planck Institute for Psycholinguistics Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85012.sa1](https://doi.org/10.7554/eLife.85012.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Eelbrain: A Python toolkit for time-continuous analysis with temporal response functions" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Barbara Shinn-Cunningham as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Sophie Slaats (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Both Reviewers helpfully point that more clarity is needed regarding the boosting algorithm; its efficacy needs to be directly compared with existing toolboxes (e.g., Crosse et al., 2016, Weissbart/Reichenbach);

2) Reviewer 2's comments about ridge regression need to be addressed – perhaps comparing boosting and ridge regression with regard to collinearity via simulation could better support the conclusions;

3) Reviewer 2 rightly comments on the importance of accessibility and clarity in the documentation. This needs to be fully addressed in order for the work to have the impact it deserves.

4) Please respond to each of the Reviewer's main concerns, and also take care that important details that impact future users of the toolbox are double-checked (e.g., the broken links need to be fixed).

Reviewer #1 (Recommendations for the authors):

This was a great read!

A few questions remain regarding the Boosting algorithm. Firstly, it is not exactly clear how the Sparsity prior is different from the Boosting algorithm, since both appear to favor sparse TRFs (a large number of zeros). Can the boosting algorithm be implemented without a sparsity prior, or is one a logical consequence of the other? It seems like early stopping and assuming an empty mTRF together determine the Sparsity prior. It would be helpful to include this explicitly in section 3.3 (Background: The boosting algorithm), to facilitate the interpretation of (the title of) section 5.2 (Sparsity prior).

Secondly, since the Boosting algorithm sets Eelbrain apart from other TRF implementations, such as the mTRF Toolbox (Crosse et al., 2016) or pyEEG from the Reichenbach lab (https://github.com/Hugo-W/pyEEG), a short comparison of results between two methods would be very informative. Which of the two resulting TRFs is closest to the actual neural response? Why is this the case? Would it be possible that boosting works better in some cases, but not in others?

On page 28 under header 5.4 (Source localization) there is a mention of source localization improving the signal-to-noise ratio of a specific response. While this is undoubtedly true, does this not also lead to the artificial decrease of signal-to-noise ratio for other responses (which might also be relevant, and even modeled)? In other words, is it possible that source localization might lead to an artificial overestimation of the contribution of a given predictor?

The code is easy to use thanks to the wonderful documentation. All the scripts run on the first try. There was only a single error in the scripts as I ran them: in Auditory-TRFs.py, under the header "TRFs", the second cell does not run. The error was the following: [TypeError: 'TTestOneSample' object is not iterable]. All the other cells above it ran to completion. There was a tiny typo under the header "Generate figure" in the same script: the first comment says 'preditive' instead of 'predictive'. Finally, the implementation of the plots yields many warnings if the chosen fonts are not installed (as was the case for me), but this is easy to fix as a user.

The TRFs ran to completion for subjects 1 to 20 – the other ones were omitted due to time constraints. The visual comparison between the newly calculated TRFs and the downloaded ones (for the same subjects, of course) showed minuscule differences in the scalp maps – one or two electrodes were flipped for significance. Unfortunately, the reason for this difference is not clear to me at this point. The other figures were fully identical to the paper.

Reviewer #2 (Recommendations for the authors):

1) The main issue I have is that the current toolbox heavily relies on a single way to solve the TRF estimation problem. This is the boosting algorithm. While there are certainly benefits and downsides to any of the solutions, the toolbox forces a method on the user. As the authors explain, the boosting algorithm could come up with a solution in which fully colinear predictors still end up in the model. This would not happen using other algorithms. Interpreting the added benefit of individual predictors to the model could therefore lead to very different conclusions depending on the toolbox you use. It becomes very difficult for any lay audience to compare results from this algorithm to methods implemented in other toolboxes, for example in the mTRF toolbox introduced by Crosse et al. (2016). I am very positive that the authors are open about this and even provide counterintuitive examples of this problem. However, to make the differences clearer for a lay audience I have two improvements here that could be made:

A) Ideally, the toolbox should provide an easy way to implement different ways to solve the TRF estimation. Now, the boosting methods seem difficult to get around in the current implementation (to me). If the authors could provide at least options to change the solution by provide also other solutions themselves. Personally, adding ridge regression would be beneficial as that has been used e.g. in the Crosse et al., (2016) toolbox lot. But if the toolbox is made in a way that custom-made solutions or future solutions can easily be added and compared that would be a great benefit.

B) In the manuscript these methods should be quantitatively compared rather than only describing some counter-intuitive examples of the boosting algorithm. What would ridge regression do for this collinearity problem? I think the manuscript could benefit from a thorough comparison between the different methods.

2) The provided github code together with the manuscript is not very straightforward. While the installation of the toolbox was very smooth, to actually get to the figures provided in the manuscript required going back and forth within all the folders a couple of times. It was not clear to me that first all the code in the predictor/analysis folders must be run before ending up with the results figures etc. Some more instructions on this could have been helpful.

3) If the code in the github should provide the 'easy' way to do the TRF analysis, to me this was not necessarily extremely straightforward. Besides the order issues as described above, getting to the TRF required many steps that remain unexplained. In the code, the main bulk of work is going into making the predictors themselves. This to me makes sense as that is complicated work, however the manuscript itself they give illustrators how to make predictors and provide the code, but it doesn't seem very integral to eelbrain itself to make the predictors in a straightforward manner. So this is left up to the user. If I am a layperson using the toolbox, I, therefore, need to figure out myself outside of the toolbox (potentially based on the code the authors provide, but this does not seem to be an integral part of eelbrain) to make the predictors before I can continue using the code. Of course, a toolbox that helps with the TRF itself is useful, but a user that never has used a TRF before also needs help potentially making the predictors. I guess this is a choice for the authors, which potentially is not clear in the current version of the manuscript. Is the toolbox for solving the TRF problem using the boosting algorithm or is it also intended to provide a means to generate reasonable predictors? If the former is not solving some of the major issues that a lay audience might have if the latter then the manuscript should have way more explanation on how to generate the predictors using eelbrain. This involves not only showing it in the figure but also providing the relevant code, the current descriptions seem insufficient. It seems that the authors focus on making an easy-to-use TRF tool, but provide tools to make predictors but these are not integral to eelbrain. Thus, if the authors aim to provide a tool to go from data to the TRF (including making the predictors), then the manuscript should explain better how this is done and link this to the code. If they do not intend to do this, then they should more clearly separate what eelbrain can and cannot do.

4) Related to issue 3. The use of trftools. In the code for making the predictors, trftools is used a lot. However, when going to the github page of trftools it seems that the authors are not confident about the stability of the code of trftools ("Tools for data analysis with multivariate temporal response functions (mTRFs). This repository mostly contains tools that extend Eelbrain but are not yet stable enough to be included in the main release."). If the code they provide for a publication refers to a toolbox they themselves don't deem stable I find it difficult to judge the value of the toolbox. A layperson might just go along and use the code provided with a published paper.

5) In general, the paper does not provide any tools or directions to use the toolbox. What is the benefit of this toolbox to what is already available? The overall logic of the toolbox and implementation would have been helpful. Now very often the authors refer to function and class types within the toolbox (e.g. NDVar objects etc.), but without any context, this is very difficult to grasp. I understand the manuscript is not the place to provide a full tutorial, but now the manuscript fails to provide an overall logic of the toolbox and how to approach a problem.

6) Regarding this piece of text: "Because the default implementation of the boosting algorithm constructs 1 the kernel from impulses (each element hi,τ is modified independently), this can lead to temporally discontinuous TRFs. In order to derive smoother TRFs, TRFs can be constructed from a basis of smooth window functions instead. In Eelbrain, the basis shape and window size are controlled by the basis and basis_window parameters in the boosting function." Would it be helpful to demonstrate this and also to show what are the default options in the bases and basis_window and why these are chosen in this way? I think it would be useful for a user to know that these are critical choices that are made for them by the toolbox.
