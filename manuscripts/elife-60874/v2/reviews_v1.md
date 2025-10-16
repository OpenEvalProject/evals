# Peer review - Round 1

Editors:
- Redmond G O'Connell, Trinity College Dublin Ireland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60874.sa1](https://doi.org/10.7554/eLife.60874.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work by HajiHosseini and Hutcherson investigates the self-regulation of choices about whether to accept or reject different varieties of food. Participants made choices either according to their natural preference, with an emphasis on healthiness, or by intentionally decreasing their desire for food. Choice behaviour across these three contexts was modelled via the drift diffusion model, and decision-relevant signals from the model were correlated with frequency-specific signals in scalp EEG data. The study will be of interest to researchers studying value-based decision making, mathematical models of decision making and their electrophysiological correlates.

Decision letter after peer review:

Thank you for submitting your article "Alpha and theta oscillations contribute to attribute regulation in dietary decision making under self-control" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: James Cavanagh (Reviewer #1); Peter R Murphy (Reviewer #2).

The reviewers and reviewing editor have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Both reviewers expressed enthusiasm for the overarching rationale of this paper and agree that it addresses an important topic that would be of considerable interest to the eLife readership. However, as you will see, the two reviewers also identified a number of very substantial issues relating to the general clarity of the manuscript and the informativeness of the analysis approach which may limit the extent to which firm conclusions can really be drawn regarding the mechanisms underlying value-based decision-making. Below you will see that the reviewers have suggested a considerable number of revisions that we would deem necessary before the paper could be considered for publication. If you are willing to complete these revisions, and/or provide a detailed rebuttal where relevant, the paper will be subjected to a further detailed second-round review. As the editors have judged that your manuscript is of interest, but as described below that substantial revisions are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This work by HajiHosseini and Hutcherson investigates the self-regulation of choices about whether to accept or reject different varieties of food. Participants made choices either according to their natural preference, with an emphasis on healthiness, or by intentionally decreasing their desire for food. Choice behaviour across these three contexts was modelled via the drift diffusion model, and decision-relevant signals from the model were correlated with frequency-specific signals in scalp EEG data. The main findings are that suppression of alpha-band power during decision formation was correlated with tastiness and healthiness of food items in contexts where these attributes were most relevant to the choice, which is partially consistent with model-predicted evidence accumulation signals; and, post-stimulus theta power selectively encoded food tastiness in contexts where the influence of this attribute on choice was suppressed

Essential Revisions:

1. Manuscript Clarity and Missing Details

(A) There are major issues with clarity throughout the report. This is primarily due to a lack of description of how the multiple stages of modeling were performed, but there are stylistic deficits as well.

(B) Lines 82-85: This should be a section of stating competing hypotheses, but it is hard to understand how these ideas – as described here – differ from each other and how they could be tested. This is a missed opportunity for providing additional clarity.

(C) The lack of display for things like RT and choice per condition, as well as DDM parameters is another missed opportunity for enhanced clarity (1/2 of pg. 10, most of pg. 11). Figure 2c is particularly frustrating to not know the average RT for each condition. There is currently little information provided by which to judge the quality of the model fits. All that is provided is in Figure S1 – but how the figure should be interpreted is unclear, and from what I can tell it provides no indication as to how well the model fits RT distributions (as opposed to just mean RT and choice percentages).

(D) On line 263, it details how the parameter was the mean of the posterior distribution, but it isn't clear if this individual level distribution is in any way constrained by the group level distribution, which would help protect against over-fitting.

(E) The fitted parameters need to be reported (and ideally, plotted). Of particular importance, currently there is no indication of the signs or magnitudes of the fitted weights given to the tastiness and healthiness attributes, only analyses of differences in weights.

(F) I would welcome a better explanation of how the weights given to different attributes are i) applied to the subject-specific food ratings, and ii) combined to yield a single drift rate for a given stimulus.

(G) It is not clear at all how the DDM params, taste and health params, and EEG are all fit together. Figure 2 caption details how these attribute estimates are "based on DDM structure", but it isn't clear how these boxcars are integrated into the EA signal, or how they are fit together to yield the curves in Figure 2c. The authors note that there were 1000 simulated datasets, but what varied between them?

(H) The cross correlations between parameters should be detailed at every level of the model. Co-linearity would be a major issue to avoid, and it seems inevitable in some cases like comparing attribute regressions to EA regressions (where EA is based on some combination of attributes). Without resolution of this issue, Figure panels 3d-e are not interpretable.

2. Analysis Approach

(A) The authors' chosen approach to identify decision signals in the EEG data is indirect and in my opinion of limited value. The issue here is using a correlation of model-estimated (Figure 2c) and observed (Figure 3a,b) signal trajectories to make inferences about the possible functional characteristics of the neural signals in question: When the model-estimated trajectories for both 'decision evidence' and 'evidence accumulation' (EA) signals are themselves highly similar, then they will necessarily yield highly similar correlations with any neural signal (in the case of the alpha suppression signal, both |r|>0.9) and provide very limited insight about what the neural signal might reflect. A more fruitful approach would surely be to exploit the fundamental differences that are predicted of evidence and EA signals: in particular the fact that, in the model at least, the former are expected to be essentially static during decision formation while the latter are expected to exhibit several dynamical properties (in build-up rate scaling with evidence strength, peak latency tracking response time, and stereotyped amplitude at response) that clearly demarcate the two types of signal. Identifying the latter properties in the alpha suppression signal would therefore provide far more compelling support for the proposal that this signal reflects evidence accumulation.

(B) Interpretation of alpha suppression effects. The above point is also relevant when considered in light of existing knowledge about alpha suppression during decision formation. Many studies have reported alpha suppression in the post-stimulus, pre-response period of decision-making tasks, though this response is rarely directly identified with the evidence accumulation process itself; rather, alpha suppression, at least over posterior scalp, tends to be identified with a kind of gating or release from inhibition process (including in papers cited by the authors). If such a process is in some sense sensitive to RT (which has been observed with alpha suppression), then it would perhaps not be surprising if it showed the characteristics observed for alpha suppression presently in Figure 3a,b (assuming RT correlates especially strongly with tastiness in the NATURAL condition and healthiness in the HEALTH condition, both of which are I believe supported by the behavioural modelling). In short, I think the meaning of the alpha suppression findings is currently unclear.

(C) In both Figures 3 and 4, the topographic distributions of the reported effects are by and large quite different between the different experimental conditions. This casts doubt on the notion that the reported signals reflect the same neural processes subject to contextual modulations, and raises further questions as to how the different results should be interpreted.

(D) Modelling. Was the 6-parameter model tested against any other model parameterizations? This can be critical for not over-fitting the data with params that aren't beneficial (e.g. starting point bias), This issue dovetails with the lack of clarity concerns noted above: starting point tends to soak up variance due to asymmetrical thresholds, suggesting both thresholds are enhanced during choice, but the RT distributions aren't shown so this remains unknown. It would be great to see these distributions so the difference between attribute vs. neutral distributions could be visually assessed for skew vs. kurtotic changes. Overall there are quite many free parameters (18) being fit to a relatively low number of trials (540; 180 per condition) per subject, and the model fits may suffer from overfitting. I would encourage the authors to fit more constrained models and identified the most parsimonious fit via model comparison.

(E) What is the purpose of the DECREASE condition? The instructions for this condition struck me as being very much open to interpretation, and indeed it seems to have led to some counterintuitive results (an increase in the weight given to healthiness in this condition, and generally increased decision bounds). Generally, if the instruction is to 'decrease my desire for food', why don't I just refuse every food item I am presented with?

Minor Revisions:

(A) It is surprising that the introduction doesn't include O'Connell's work on P3b slope and drift rate (line 95) (e.g. The classic P300 encodes a build‐to‐threshold decision variable, EJN). With the estimated value attributions peaking around 542 ms, this seems like it might relate to the slope to the P3b. Of course, this is all conjecture since neither the RTs nor the ERPs are shown, but I suggest that the authors utilize the similar correlation strategy with the raw EEG to see if it corresponds with known ERP component activities that have previously been linked to these same DDM constructs.
