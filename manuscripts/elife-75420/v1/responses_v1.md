# Author response - Round 1

Authors:
- Matthias Guggenmos ([ORCID: 0000-0002-0139-4123](https://orcid.org/0000-0002-0139-4123))

## Response text

DOI: [10.7554/eLife.75420.sa2](https://doi.org/10.7554/eLife.75420.sa2)

Reviewer #1 (Recommendations for the authors):

I did not have time to check the toolbox available online but I note that it is an important strength that the authors have shared this resource for other researchers to look at or re-use for their own work.

Regarding the reasoning in paragraph 1.6, it is unclear to me why metacognitive evidence for the chosen option would become zero in case of a sign flip, rather than becoming negative evidence (just flipping sign)? I think it would be best to simply make the assumption that sign flips are impossible.

Indeed, re-reading this paragraph I found my wording to be unnecessarily convoluted. The point I had in mind is quite straightforward: either sign flips are impossible due to the nature of metacognitive noise itself (e.g. lognormal distribution) or they are possible but are not observed because the confidence scale does not include the possibility to report errors (hence confidence=0 in such cases -> censored distributions). I substantially simplified the corresponding paragraphs along these lines (‘Metacognitive noise: noisy-report models’).

Isn't the lack of a reliable recovery of δ_m at low and high type 1 performance levels an issue, because it is exactly at the bounds that δ_m is supposed to have an effect?

Figure 4 (second row) shows that the recovery of δ_m indeed becomes unstable at very low or very high type 1 performance levels. I don’t consider this problematic, however.

Figure 4 investigates parameter recovery in dependence of overall type 1 performance. As outlined above, if overall type 1 performance is close to chance or close to perfect, behavior is random or shows little variance, respectively, which is why parameter recovery is often hampered.

More to the reviewer’s point, in the manuscript I provide an interpretation of δ_m in terms of a confidence threshold (for δ_m < 0), i.e. a minimal level of sensory evidence required to have a nonzero confidence experience. I assume this is what the reviewer was referring to with “exactly at the bounds that δ_m is supposed to have an effect”; please correct me otherwise. This interpretation, however, refers to instances of single trials in which sensory evidence is low (from the perspective of the observer, not necessarily objectively). Critically, the idea of a confidence threshold can be meaningful and impactful even if overall performance is at intermediate or high levels, as subjective sensory evidence will often nevertheless be low in a certain fraction of trials.

More importantly, however, the evidence shift induced through δ_m applies to all levels of internal evidence (after all, it is just the subtraction of a constant); the idea of a confidence threshold at very low levels of evidence is highlighted mainly because it is associated with a prominent feature in the confidence-evidence relationship.

We would like to see more discussion on how this model compares to other proposals of Bayesian confidence signatures (Adler and Ma, 2018, already cited). I also wondered about the possible inclusion of RTs in the model, which is then nicely addressed in the Discussion already.

As the reviewer mentions, I had cited a paper by Adler and Ma from 2018 (Neural Computation), but I now realized that there is a second Adler and Ma (2018; PLOS Comp. Biology), to which the reviewer is likely referring to. I had missed the latter one in my literature review. I now refer to this and related references in a new discussion paragraph on Bayesian confidence models (Line 807ff):

“Finally, how does the present model relate to the recent discussion between Bayesian and Non-Bayesian models of confidence (Aitchison et al., 2015; Sanders et al., 2016; Adler and Ma, 2018b)? A Bayesian observer of the (inner) world is one who maintains a posterior probability density over possible states of that world. In particular, computing confidence for such an observer corresponds to integrating the posterior over all possible states for which the type 1 choice would be correct. In this sense, the model proposed here with the link function provided in Equation 5 corresponds to a Bayesian observer, albeit one that can be susceptible to metacognitive biases and to additional sources of metacognitive noise. Thus, while the observer is Bayesian in nature, it may not be Bayes optimal. At the same time, the framework and the toolbox are flexible to allow for “non-Bayesian” link functions (Figure 3—figure supplement 1) that could represent certain idiosyncratic heuristics and shortcuts inherent to human confidence judgements. Of note, the model proposed here does not consider prior distributions over the stimulus categories (see e.g., Adler and Ma, 2018b). Instead, it is assumed that the observer considers both stimulus categories equally likely which is a reasonable assumption if stimulus categories are balanced.”

I agree that including RTs in a confidence model would be a nice feature, but in my opinion this requires a lot of groundwork that is beyond the scope of this work.

Figure 4, middle panels: I think it is an assumption to simply convert confidence in 0-1 space to 0.5-1 space. Indeed, observers may treat very differently a 0.5-1 scale in which both 'I have purely guessed' and 'I am pretty sure I have made an error' would be reported around 0.5, whereas would be further apart on a 0-1 scale.

In this manuscript I strictly consider confidence as ranging from ‘I have purely guessed’ to ‘I am 100% certain’, i.e. I do not consider the case of realizing errors at the time of the confidence report. This was stated e.g. on Line 330ff (“Unless confidence rating scales include the possibility to indicate errors (which I do not consider here)[.]”). The transformation from 0.5-1 to 0-1 space is thus a purely mathematical one, motivated by certain technical advantages (e.g. the Β noise distribution is naturally bounded between 0 and 1). I now also state this in the relevant paragraph concerning the transformation 0.5-1 -> 0-1 (Line 183ff):

“Note that I do not consider the possibility that type 1 errors can be reported at the time of the confidence report, i.e., confidence cannot be negative.”.

The sensory bias (bias), sensory noise (slope), and sensory threshold (random responses) all capture choice patterns in a logistic function; can you better explain how Equation 2 was developed? But parameterization of Figure 2 seems able to capture all standard effects. Similarly the reasoning leading to the generation of Equation 5 could be better motivated.

Equation 2: The formula in Equation 2 is the logistic distribution. The only change from the standard form is that I converted the conventional parameter s to a standard deviation σ using fact that the variance of the logistic distribution is known as s²π²/3. The nature of the bias parameter in Equation 1 corresponds to a horizontal shift of the resulting psychometric function. The sensory threshold parameter is the mathematical formalization of the notion that a certain degree of sensory stimulation is necessary to drive the system, i.e., below a certain intensity level δs the resulting decision values are zero. I now provide this explanatory information interspersed in ‘Computing decision values’.

Equation 5: I have now added the derivation of the link function in Equation 5 as Appendix Equation A1 and reference to it in ‘The link function: from metacognitive evidence to confidence’.

Figure 3C legend "Higher metacognitive noise flattens the relationship between type 1 decision values and confidence.": this is between metacognitive evidence and confidence instead?

Thanks, corrected!

The behavioral effects shown in Figure 2 and 3 as a function of parameter values are useful, but also confusing because several of the parameters change value from plot to plot. Would it be possible instead to fix all but one parameter, and change the one parameter for 4-5 values instead of 2 values, for instance using a color scale? This way, the reader would be able to appreciate the effect of each parameter in isolation from the others.

I liked this suggestion and implemented it for Figures 2 and 3:

Figure 6A displays an increase in Mratio as type 1 d' increases – the opposite of what is reported in the legend and in the text? at least for d' between 0 and 3, which is the case in most perceptual experiments? Likewise, there is a discrepancy with σ_m from the other module (Figure 6 supp).

Thanks for noting. I replaced it with a more neutral “shows a nonlinear dependency with varying type 1 performance levels” (Line 387). Note that the plots in Figure 6 changed slightly because I now plot proportion correct responses instead of d’ and I use truncated normal distributions for all plots (which is the new default of the toolbox; also, it makes the comparison between noisy-readout and noisy-report models easier).

Reviewer #2 (Recommendations for the authors):

- I found it odd that z was the noisy estimate of z-hat (and c the noisy estimate of c-hat), rather than the other way around given that the -hat operator is typically added to refer to an estimate.

I agree that the notation could be confusing. I now replaced the hat-notation with an asterisk-notation. I did not simply flip the hat and non-hat notation, since noisy versions of the variables are not really an estimate in the traditional sense either (as e.g., the sample mean).

- The current model is restricted to cases in which the sensory evidence is varying. This is opposite to the meta-d' model, in which sensory evidence is assumed to be fixed, or at least varying across a narrow range (eg d' is constant for stimulus repetitions). It might be worth emphasising that the two models can be chosen depending on the data available, rather than ReMeta being universally more suitable than meta-d'.

As I noted also to Reviewer #1, this restriction was unnecessarily imposed in the previous version of the manuscript. The references to this restriction are now removed from the manuscript. In other words, the model also works for constant stimuli.

- I felt the introduction could do with some more emphatic framing, and that the author is selling himself short here. Lines 26-33 outline the rationale for the model. But there are two goals here - one is an incremental one of fixing the biases in current metacognitive efficiency estimates, which is useful, but it doesn't seem to be so debilitating (at least with the standard m-ratio estimates) as to warrant entirely new model machinery. But then later in the paragraph, the fact that this new approach could also accommodate fits of parameters governing different types of metacognitive biases is introduced. This seems much more important given that there is no current framework for modelling such biases.

I agree with this assessment and I now put a stronger emphasis on this methodological gap in the literature (Line 53ff):

“However, currently there is no established framework that allows for unbiased estimates of metacognitive biases. The validity of traditional calibration curve analyses, which is based on a comparison of the subjective and objective probability of being correct, has been debunked repeatedly (Soll, 1996; Merkle, 2009; Drugowitsch, 2016). In particular, the classic hard-easy (Lichtenstein and Fischhoff, 1977), according to which overconfidence is particularly pronounced for difficult tasks, can be explained as a mere statistical artefact of random errors. For this reason, and in view of the potential importance in patient populations, there is a pressing need for unbiased measures of metacognitive biases.”

Towards the end of the introduction, I once again refer to this point (Line 111ff):

“[.] As outlined above, there is currently no established methodology to measure under- and overconfidence, let alone measure different types of such biases. [..]”

In return, I cut down on introductory space taken up by the issue of metacognitive efficiency, in line also with the recommendation of Reviewer #1.
