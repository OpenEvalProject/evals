# Peer review - Round 1

Editors:
- Jörn Diedrichsen, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76635.sa0](https://doi.org/10.7554/eLife.76635.sa0)

This important article presents a Bayesian model framework for estimating individual perceptual uncertainty from continuous tracking data – a powerful and exciting alternative to traditional binary-choice psychophysical experiments. The model takes into account motor variability, action cost, and possible misestimation of the generative dynamics. The analyses provide compelling evidence for the framework. The article is clearly written and provides a didactic resource for students wishing to implement similar models on continuous action data.


---

# Peer review - Round 1

Editors:
- Jörn Diedrichsen, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76635.sa1](https://doi.org/10.7554/eLife.76635.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Putting perception into action: Inverse optimal control for continuous psychophysics" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jörn Diedrichsen as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Joshua Gold as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. Overall, all reviewers thought that the paper has the potential to become a very valuable contribution to the field. The revisions focus mainly on the clarity of the submission. The extensive original reviews are attached below and should be responded to in detail.

Essential revisions:

1) The assumption of independence of motor noise across observations (reviewer #1, comment #1) is likely problematic in terms of obtaining valid WAIC values – and this problem should be addressed.

2) The technical exposition in the introduction is sometimes confusing and the clarity of the explanations should be improved. The specific comments provide a detailed list of constructive suggestions here.

3) The discussion of the previous literature is not always as balanced and would be ideal (see reviewer #2)

4) For a tools and resource paper, I would hold that the associated code and documentation should be visible to the reviewers at the point of submission, so the quality of the online resource can be reviewed together with the paper. So I would ask you to provide a working link with the revision of the paper.

Reviewer #1: All comments in public review.

Reviewer #2 (Recommendations for the authors):

Specific Remarks:

– There are passages that read like poorly grounded indictments of well-established literature. Supplementary Section A, which functions as support for claims in the main text and the figure 3 caption, references a study by Yeshurun et al., (2008). The authors of the present paper write that Yeshurun et al., 'investigated the validity of the theoretical result (Green and Swets, 1966), that the forced-choice sensitivity d'FC differs from the sensitivity obtained through an equivalent Yes-No task d'YN by a factor of √2, i.e. d'FC = √2d'YN. Apart from running a serious of experiments targeted at evaluating the validity of this theoretical result, the authors reported the actual values of this factor based on extensive literature review involving numerous studies investigating perceptual sensitivities across sensory modalities. Indeed, the literature review collected a broad range of deviations from the theoretical value.'

The authors then go on to specifically reference two of the papers cited by Yeshurun (2008). One of these papers (Jesteadt and Bilger, 1974) reported that d-prime estimated with a forced-choice task was better by a factor of 2.1 than performance in an equivalent yes-no task. The other (Markowitz and Swets, 1967) reported d-prime estimated with a forced-choice task was better by only 1.15. These two studies deviated from the predicted 1.4 improvement by factors of 1.5x and 0.8x, respectively.

The logic of the passage is problematic, and the passage seems only tenuously connected to the aims of the paper. In my view, I think the supplementary passage and the connected threads in the main text are harmful to the paper's messaging and should be removed. Here is why: The theoretical result relating sensitivity in forced-choice and yes-no tasks as reported by Green and Swets (1966) is easy to derive in a few lines and is most certainly valid, presuming that certain assumptions hold. The authors can of course fairly question whether these assumptions hold in certain experiments (as did Yeshurun et al., 2008), but experiments do not, and could not, evaluate the 'validity of this theoretical result'. The theoretical result stands on its own. The authors' writing seems to conflate a lack of empirical variability (e.g. due to measurement error, assumptions not holding) with a lack of theoretical validity. I thought, initially, that this could perhaps be explained away by inattentive writing.

But the authors' then use the range of deviations aforementioned deviations-the 1.5x deviation reported by Jesteadt and Bliger was on auditory frequency and intensity discrimination; the 0.8x deviation reported by Markowitz and Swets, was on sound detection-to suggest that the observed 1.36x deviations between tracking- and forced-choice-based estimates (from Model 4 fits) are within an established range of deviations in the literature. The relevance of these numbers to the present work is dubious at best. Consider, for example, if some other pair of studies on gustatory sodium discrimination or detection had reported deviations ranging from 0.25x to 8x the theoretically predicted values. Would that somehow be relevant to the interpretation of the current work? I am not sure why the authors thought this a valuable addition to the paper. They seem to be using these studies to suggest that because other studies have deviated from predictions (whatever the causes) that discrepancies in the present study should be thought of as small. It all feels forced. After writing out these notes, I was concerned that perhaps I had been making too much of it. But the next issue has a similar flavor.

– The manuscript appears both to misleadingly describe findings in Bonnen et al., (2015), and to self-contradict its own assertions regarding those findings. The authors several times write that Bonnen et al.,'s tracking-based estimates of position uncertainty (i.e. position discrimination thresholds) are an order of magnitude (i.e. ~10x) higher than corresponding forced-choice-based estimates. The authors contrast this discrepancy with their own results, saying that they 'infer values that differ by a factor of 1.36 on average'. It is true that the raw estimates of Bonnen et al., reported tracking-based estimates that were ~10x larger. But that was before Bonnen et al., took several obvious factors into account (e.g. the benefit of integrating across 15 frames of each stimulus presentation, the predicted improvement in sensitivity in 'two-look' forced choice tasks). After taking these factors into account (as it is appropriate to do), the ~10x difference between the tracking- and forced-choice-based was reduced to a ~2x difference. In the supplement, the authors acknowledge that Bonnen et al., took these factors into account, but their writing in the abstract, introduction, and discussion (references to order of magnitude differences) reads as if they are unaware. I am unclear about the reasons for this discrepancy, but it should be corrected.

Further, on page 5, left column the authors report that estimates of perceptual uncertainty of target position from the Kalman Filter model differ from the forced-choice-based estimates by approximately 2x. They write: 'The average factor between the posterior mean perceptual uncertainty in the continuous task and the 2IFC task in the 5 higher contrast conditions is 1.20 for the LQG model, while it is 1.73 for the KF. Only in the lowest contrast condition, it increases to 2.20 and 2.93 arcmin, respectively.'. This difference is in line with the conclusions of Bonnen et al., and does not square with the assertion that tracking-based estimates were off by an order of magnitude (~10x). Given that the current Kalman filter analysis essentially replicates the analysis performed by Bonnen et al., these two assertions (10x differences vs 2x differences) cannot both be correct. Again, in keeping with the first point above, all this seems like a forced attempt to convince the reader that observed deviations are small between the tracking- vs. forced-choice-based estimates of perceptual uncertainty about target position. But it seems unnecessary. Model 4 does a more accurate job of estimating perceptual uncertainty about target position than simpler models (and seems to provide a closer match to forced-choice-based estimates). Let those results stand on their own.

– For a computational paper, in which the primary contribution is to develop methods for data analysis and parameter estimation, there should be substantially more discussion of which parameters have their values trade off of one another. For example, the authors have taken the trouble visualize a posterior distribution over the parameters (Figure 3A). They should help the reader develop an intuition for why the posterior has the structure that it does. All models other than the Kalman filter model include perceptual uncertainty about target position (\σ), perceptual uncertainty about cursor position (\σ_p), and motor variability. All of these quantities affect the reliability with which discrepancies between target and cursor position can be evaluated, and should have similar effects on performance. The figure shows that these parameters trade-off with each other (strong negative correlations in the posterior distributions over the model parameters). The authors should include some discussion of these trade-offs, helping to provide the reader intuition for why these parameters trade-off in the way that they do. Similarly for the positive correlation between motor variability (\σ_m) and perceptual uncertainty about cursor position.

– Regarding their analysis of simulated data, the authors report that attempts to infer the value of the target position uncertainty (\σ) from Model 4 were accurate (Figure 3C). It would be helpful for the authors to describe in more detail the parameters of the simulation. Specifically, in would be useful to explain and provide intuition for how, if the observer had a mistaken belief regarding the drift dynamics, it is possible to accurately infer the value of perceptual uncertainty about target position. A naïve reader might presume that, because there is an infinite number of pairs of position uncertainty (\σ) and presumed drift variance (\σ_s) that determine the Kalman gain, that \σ could not in fact be accurately estimated if \σ_s does not equal the true drift parameter (\σ_rw). Please explain for the reader how this works.

Tone

The current paper describes shortcomings of the Bonnen et al., (2015) data analyses. Many of these shortcomings were explicitly acknowledged by Bonnen et al., It would help the tone and tenor of the manuscript if, when the current authors describe the acknowledged shortcomings, the current authors cite Bonnen et al., (2015).

Examples include:

– "A model, which only considers the perceptual side of the task, will therefore tend to overestimate perceptual uncertainty because these additional factors get lumped into perceptual model parameters, as we will show in simulations."

– "A model without these factors needs to attribute all the experimentally measured behavioral biases and variability to perceptual factors, even when they are potentially caused by additional cognitive and motor processes."

The current paper makes a nice contribution in demonstrating these points quantitatively. But, in places (and in keeping with the flavor of remarks above), the writing seems concerned that readers might not recognize the paper's unique contribution. I think the paper's contribution is clear. And I think that their paper will read better, and leave a better impression, if it looks for ways to portray previous work in a more generous light.

Specific Comments

– Experimentor/Participant distinction

The experimenter has access to the true target position and the true cursor position is available. The experimental participant him/herself has access only to the estimates of target and cursor positions. The article should more explicitly discuss this issue in the main text. Figure 2 and the Supplemental derivations allude to it, but it should be discussed more prominently.

– Explanation of matrix values.

The authors should explain why the B=[0 dt]' parameter takes on the particular values that it does. Is the implication that the control action is best understood as a 'rate of change' so that result matrix-multiplying the control action with B is a position? Please explain. The value of the non-zero element of B trades off perfectly with the square root (?or similar?) of the movement cost parameter 'c'. So it would be valuable for the authors to explain why they chose to set B to have the value it does.

Telegraphic mathematical development.

In the supplement, the mathematics associated with transitioning between Supplemental Equations S16-S18 needs to be expanded. Conditioning the nD Gaussian on x_t and marginalizing out x_hat_t are two separate steps, but the manner in which the passage is written encourages the reader to presume that they are a single step. Too much analytical work is foisted on the reader if he/she wants to carefully follow the derivation along. The derivation is correct (I worked it out myself), but it should be laid out more explicitly. Further, the final expression for the likelihood of the state (x_{t+1}) on time step t+1 should be provided. This likelihood is straightforwardly obtained by marginalizing out the estimate (x^{hat}_{t+1}) of the (2-vector) state, but it would be nice for the reader if the final expression was actually made explicit for the reader.

Subjective model of state dynamics

The authors should make explicit in equation form the fallacious state dynamics that are assumed by the subjective observer. The authors describe it in words, but equations will prevent any uncertainty that the description may produce. Something like:

position walk: p_{t+1} = p_t + eps; where eps ~ N(0, σ_{rw})

velocity walk: v_{t+1} = v_t + eta; where eta ~ N(0, σ_v )

x_{t+1} = p_{t+1} + sum( v_{ 0:(t+1) } ) where the sum goes from 0 to t+1

Subjective model of estimate of velocity

Also, it is not made completely clear how the subjective observer's fallacious estimate of velocity is computed, how it resides in the model, whether the state is expressed as a 2-vector [ x_t x_p ] or a 3-vector [ x_t x_p v_t ], and whether the estimate of the state is expressed as a two-vector [ xhat_t xhat_p ] or a 3-vector [ xhat_t xhat_p vhat_t ]. An expanded discussion of these issues should be included. The expressions are correct but as they stand, but the mathematical development and discussion of these points are a bit too telegraphic.

Typo in the supplementary equation.

I believe that there is a typo in equation S2 of the supplement where the Ricatti equation is laid out. The term with the inverse currently reads ( C*P*C' )^-1 whereas this term in standard expressions for the Ricatti equation should be ( C*P*C' + W*W' )^-1. This term follows the same form as the inverse term in the expression for the Kalman gain (see the line above) which reflects the total covariance ( prior + observation covariances ).

Reviewer #3 (Recommendations for the authors):

The paper is already in a very polished state. I have only a few comments about clarity and completeness.

– I found myself getting confused while reading the paper about what parameters were actually involved in each model (e.g. pg 3: "the KF model has only one parameter: perceptual uncertainty σ". My recommendation to the authors is to move equations 1-4 out of the Methods section and into the main text. Personally I would consider this part of the results (ie. "what are the models we're using"?) and so I would rather see this presented pedagogically within the main paper. Keep implementation details or other technical issues in the Methods, but present the models themselves in the Results section. Just a recommendation, but that's my 2 cents!

– This leads to a related note on clarity: it's not entirely clear to me which parameters are being fit in each model. Presumably you're not fitting the C matrix in equation 2? What about B in equation 1? Come to think of it, I'm not sure where the cursor fits in, allowing for uncertainty in cursor position). (Does that become part of the state vector x_t? Please unpack this more clearly so that we can understand what these equations correspond to for each of the models discussed in the paper!

– "Our implementation will be made available on github" -- I want to note that this should be a requirement for acceptance! (i.e., the code should be posted before the paper is accepted).

– The name "bounded actor" seems like a poor one, since there aren't any bounds on the actor. (There are just costs). Figure 2 C refers to it as "bounded actor with behavioral costs" -- personally I would keep the "with behavioral costs" and drop the "bounded".

– One other point that would be worth making: you could also formulate a "with subjective belief" version of any of the simpler models. Even in the simple KF model, you could allow for mismatch between the true dynamics and the subject's belief about the dynamics. I think it's probably ok to leave the model comparisons as is, since obviously it becomes a bit messy if we have to include "optimal" and "subjective" versions of each of the models, but you should at least mention somewhere in the paper that this can be used to improve the accuracy (in terms of matching observer behavior) for any of the models.

– Can you say anything about the discrete time assumptions of the model? i.e., how would you expect the model parameters (or the accuracy of the fit) to change if you switched to 120 Hz frame rate or 20 Hz frame rate?

– Finally, a small note on grammar/usage: the paper frequently uses "… , which…" in cases where "that" (with no comma). e.g., in the abstract: "recover perceptual thresholds, which are one order of magnitude larger compared to equivalent traditional psychophysical experiments". This makes it sound like you're providing a definition of threshold, rather than describing a property of the recovered thresholds. More correct would be: "We recover perceptual thresholds that are one order of magnitude larger than …". I found this issue repeatedly in the text. You could basically look for nearly every occurrence of ", which" and replace by "that".
