# Peer review - Round 1

Editors:
- Catherine Emily Carr, University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35587.030](https://doi.org/10.7554/eLife.35587.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Coordinated Neuronal Ensembles in Primary Auditory Cortical Columns" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Shihab Shamma (Reviewer #1).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

All reviewers agree that the paper focuses on an important question, which is how ensembles of synchronized neurons in cortex function and represent stimulus information. Nevertheless, and as set out in the appended reviews, they felt that key elements of this claim were insufficiently supported. For example, with respect to the methods, the reviewers felt it was not clear what assumptions were made, and how the results were affected by grouping criteria. There were also concerns about the criteria for establishing whether or not receptive fields overlapped. This is important for ruling out the possibility that neurons responded to a similar feature of stimulus nonlinearly. The reviewers also felt that the functional consequences of these data remain unclear.

Reviewer #1:

This is a well-written paper that provides solid analysis of an exceptional set of data from primary auditory cortex. On the positive side, the paper advances the concept of cNE in auditory cortex and offers a suite of algorithms and tests to define and identify them. Much of the paper is a solid analysis that deals convincingly with the many possible confounds. For the most part, what is discussed and demonstrated is well-presented, and thus I have little to complain about. All in all, I found the paper enjoyable and informative. What I find less satisfying is what is not in the manuscript, as I will explain:

I found the following sentence very interesting, but is unfortunately undeveloped, and is not addressed in the paper at all:

"If one goal of synchronous firing by groups of neurons is to produce a more efficacious downstream effect than can be accomplished by a single neuron (Buzsáki, 2010), then cNEs may be the functional units that serve to maintain and/or enhance the fidelity of the encoding of relevant sound features".

So what are examples of these features? In other words, the functional significance of these cNE is not addressed at all in this paper except by the general statements in the end. The experiments exploited a broadband complex stimulus, and even showing the STA's measured from the firings of the cNE's would have provided (I believe) really interesting insights into what stimulus features these cNEs are trying to enhance. Such measurements would justify and use the analyses shown, and elevate the paper from a "Methods" paper to something much more, which it deserves to be with a little more analysis of the cNE data. Obviously, many future experiments might engage animals in behaviors or go after the features in speech and music and so on, or to find out if these cNE's remain stable or not, and whether they are somehow related to "Brain States".

Reviewer #2:

The paper "Coordinated Neuronal Ensembles in Primary Auditory Cortical Columns" uses multi electrode recordings to study the synchronized activity of groups of neurons and investigate enhanced information processing by their coordinated activity. The question at the center of this paper is very important, however the paper doesn't really deliver what is promised. The shortcomings of the study are discussed in detail below.

To begin with, how exactly the ensemble of synchronized neurons are identified is unclear. It is mentioned that they apply independent component analysis to the most significant PCA coefficients, but no more detail is provided. While the method is demonstrated using a simulated example, it is unclear what assumptions are being made, what are the limitations of this method, and how the results discussed are affected by this grouping criteria. In short, identifications of neural ensemble in this paper is treated as a trivial, solved problem, which is not the case because the choice of the method can hinder the interpretation of the results.

As an example, the authors show that PWC between CNE members vary from non-members. However, given that the CNEs were chosen based on correlation patterns (PCA/ICA of autocorrelation matrix), this observation is of course expected from the selection criteria.

Another major claim of the study is enhanced information transfer. However, the measure of information used in this study does not really reflect whether CNE carries more information about the stim, the state, or about any other factor as claimed. The measure used is basically an entropy of PSTH, measuring how far from uniform the average spike train is. In other word, it is calculated by averaging the neural responses over 50 repetitions of the same stimulus, and then the entropy of this average is computed. So, this measure only reflects how "bumpy" the average response is. Again, the finding of higher entropy for CNE neurons is expected from the selection criteria of these neurons. If the averaging is done over uncorrelated neurons, the average will be more flat. If they are from a CNE, they by selection have higher correlation and as a result their average will be less uniform (average is indeed what the first PC of the data approximates). Therefore, this finding is not really compelling and informative. I suggest methods such as decoding or "Mutual" information instead of plain entropy. In particular, answering "what" information is more reliably represented and "how" is crucial for the claims of the study.

Moreover, the method used identifies neurons that are co-activated. But obviously if they are fully correlated, then there will be no added information by the ensemble. This issue is ignored, and the authors have only focused on similarity of CNE responses, and not the complementary components encoded by ensemble members.

Finally, the evidence for the claim that the CNEs are not based on overlapping receptive fields is rather weak. The evidence shown is based on STRF, which is a lousy model of neuron's actual receptive field. Therefore, they cannot rule out the possibility that neurons responded to a similar feature of stimulus nonlinearly.

From Discussion "Instead, cNE activity represents important stimulus information embedded in broader network-related contexts". This is indeed a very interesting claim, but I do not believe the author have shown compelling evidence for it.

Reviewer #3:

This is a thorough study identifying cell assemblies in auditory cortex. Spiking events from these cell assemblies carried more information than spikes from single neurons or randomly selected groups of neurons with the same spike/event rate. The authors use a number of controls to demonstrate that the identified cell assemblies could not be solely accounted for by the receptive field similarity.

The analysis in the subsection “Identification of coordinated neuronal ensembles (cNEs)” correlating results obtained full datasets and the first three quarters is somewhat confusing. Some of the overlap in the results will be due to overlap in the data. One possibility is to use bootstrap correction to report the expected correlation that has been compensated for the dataset overlap. A more standard alternative would be to compare cell assemblies identified from different 3/4 of the datasets, and then if they perfectly overlap that would be one answer. If the overlap is less than 100% this can again be corrected using bootstrap formula from the Efron and Tibshirani book "An introduction to the bootstrap".

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Coordinated Neuronal Ensembles in Primary Auditory Cortical Columns" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Andrew King as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We suggest that you make the analyses of the noise correlations more explicit, and test whether the synchrony you observe goes beyond that expected for pairs. To do this, you could compare against surrogate data sampled from a model, e.g. Ising or dichotomized Gaussian, with the same pairwise correlations but no higher-order correlations.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for sending your revised article entitled "Coordinated Neuronal Ensembles in Primary Auditory Cortical Columns" for peer review at eLife. Your article is being evaluated by 3 peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Andrew King as the Senior Editor.

Your article has been favorably reviewed, but there is one remaining reviewer comment that needs to be addressed before a final decision can be made.

Reviewer:

The use of the DG model is appropriate, but I wonder why the authors used a model that matches the pairwise correlations only at zero delay? They point out that this produces simulated spike trains that differ from the real data in two ways: 1) higher-order correlations at all delays and 2) second-order correlations at non-zero delays. If the goal is to quantify the impact of higher-order correlations, this might not the best way to do it. The DG framework can be used to generate spike trains that match the second-order correlations at all delays. Wouldn't that be better for this purpose?
