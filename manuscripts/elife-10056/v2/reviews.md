# Peer review - Round 1

Reviewers:
- Frances K Skinner, University Health Network , Canada

## Review text

DOI: [10.7554/eLife.10056.022](https://doi.org/10.7554/eLife.10056.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for choosing to send your work entitled "Dendritic nonlinearities are tuned for efficient spike-based computations in cortical circuits" for consideration at eLife. Your full submission has been evaluated by Eve Marder (Senior editor) and three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the decision was reached after very extensive discussions between the reviewers. Based on our discussions and the individual reviews below, we have decided not to consider the present manuscript further at this time. However, we would be willing to consider a significantly revised resubmission (below).

While the reviewers all felt that the work was quite interesting, concern was raised in the ensuing discussions as to the unclear presentation of the essence of the work. In fact, the reviewers spent a considerable time discussing what they thought was the structure of the model, and what it means. The fact that the reviewers went back and forth over these issues indicates a lack of clarity in the Results section. Therefore, it was decided that the work needed significant revisions and significant effort would be required to make the work accessible to the general reader, not only in making the take home message clear, but also in explaining how and why detailed mathematical derivations are needed and used.

Overall, two major aspects require consideration, as summarized below with some suggestions. Additional detailed comments from the reviewers are appended below.

1) A clearer and simpler version of the paper is needed.

A clear line through the reasoning that will allow everyone to see the core of what has been done, and why, needs to be presented. Specifically, the paper needs to be transparent and math that obfuscates should be removed or simplified or explained. The authors are encouraged to present their essential results in a much more straightforward fashion to help elucidate their mathematical derivations.

A suggestion is to use a flow chart of the process/protocol (capturing presynaptic firing statistics, fitting, optimizing etc., and lay bare the limitations/assumptions – e.g., the output computation f(u) is assumed to be a linear function), describe the essential results in words, and point to the mathematical parts in methods/or a mathematical appendix of how and why. We understand and appreciate that you wish to publish the full mathematical treatment, but most eLife readers won't benefit from the math in its present form. The mathematical results could be made complete and readable in an Appendix, while freeing the Results to show the logic of the model and how it works. It looks complicated because of using the most general formulations (multi-state state transitions, and multi-variate normal with arbitrary state-dependent covariance), but the main results are obtained via somewhat simpler formulations. More detailed mathematical derivations could go into a mathematical appendix if necessary.

In this way, people (of diverse backgrounds) would be able to sink their teeth into the contribution, build on it, test it and so on.

2) Take-home message(s) and biological/biophysical intuition needs to be presented.

No biophysical model seems to be included, even simply. Everything seems to be folded into the optimal g(s), so that it is not obvious how best to make a biological/biophysical connection.

The derived 'optimal traces' do, in principle, bring a more stringent test to the theory, but in Figure 4 they have access to the whole pre-synaptic dynamics so the optimal trace can be replaced by the averaged pre-synaptic potential, while in Figure 5 the experimental pattern of stimulation is not sufficiently complex to really probe the detailed temporal structure predicted by the theory. The other figures support qualitative statements. This, for example, could be explicitly stated and rationalized for the reader.

Some aspects came through but because of the first point above, there was not always a clear consensus of what the authors intended as the main message(s) from the work. Could these intents (if appropriate) be better explained?

For example:i) Presynaptic neurons with correlated inputs should target neighboring regions of the dendritic tree so that the inputs can sum nonlinearly while presynaptic neurons with uncorrelated inputs should map onto different portions of the tree and the inputs sum linearly?ii) An optimizing aspect/principle that could ultimately predict the 'location structure' of synapses as a crucial test of their theory.iii) Optimally decoding the information present in the spikes to do the desired computation depends upon the correlationsiv) Addressing the question of why there are nonlinearities in the first place.v) An optimal way to recover the averaged presynaptic potential only from the pre-synaptic spike trains? Can the biophysics approximate this optimal 'decoding' operation?

Reviewer #1:

In this most interesting study, the authors propose a principle that dendritic nonlinearity is optimized to integrate synaptic inputs from the statistics of the presynaptic cells. This principle assumes that communication is mainly via spikes whereas computation is not 'punctate', thus identifying the bottleneck of dendritic processing. They go on to use models (clustered connectivity prediction) and experiment to show that this principle is followed.

The authors may have uncovered a fundamental principle, and as they state in the Discussion, "Once patterned dendritic stimulation over a broader and more realistic range of inputs becomes feasible, our theory will provide a principled method for dissecting the roles of presynaptic correlations vs. genuine nonlinear computations in shaping dendritic nonlinearities." Nice I think.

I have a few comments.

1) The authors could state that graded synaptic transmission exists (many examples in invertebrates), so that their principle may not apply there, I assume. Is it definitively known that graded synaptic transmission is not present in cortical circuits?

2) It would be helpful if the authors could expand on the discussion regarding biophysical substrate. That is, to fill in the blanks on how and why "NMDA spikes may provide a general solution". Was some modeling (not shown) done to be able to state this? Please provide some additional discussion/rationale/assumptions for making these statements.

3) Regarding inhibition, the authors discuss potential addition from the perspective of excitatory cells. However, perspectives from inhibitory cells are not expressed. Do the authors expect their principle to hold from the perspective of inhibitory cells (receiving excitatory and/or inhibitory inputs)? The authors should provide some discussion/rationale/assumptions of why this is not included/considered. I do not think it is a given that computation is only from the perspective of excitatory cells? For example, consider the reviews by Klausberger and Somogyi (Science 2008) and Chamberland and Topolnik (Frontiers in Neuroscience 2012).

Reviewer #2:

Nonlinear dendritic integration is often seen as a thorn in the foot. Following in vitro work by Larkum, Magee, Stuart, Hausser and others, it is now clear that dendrites introduce various types of nonlinearity to input integration. Further observations showed physiological patterns that appeared to tune specifically the dendritic nonlinearities. Computations that are carried out in the dendrites (as in Taylor et al. 2000) were then discovered. Thus, it has become increasingly difficult to ignore their computational role. The search for a theoretical role (mainly by Mel and coworkers), on the other hand, was mainly focused on rate-based computations. Yet, rate and spiking descriptions are often qualitatively different (as in plasticity or synfire chains). Understanding the key mechanisms for spike-based dendritic computations remains a fundamental problem, but a very difficult one.

In this article, Ujfalussy and coworkers address the hypothesis that nonlinear dendritic integration serves to decode the correlated pre-synaptic spike trains. They describe mainly three observations that back up this hypothesis. First, they show mathematically that the canonical model of nonlinear integration of Poirazi and Mel (P&M) approximates an optimal decoding of the switching between active and quiescent states. Second, they compared how different biophysically detailed models approximated an optimal decoding strategy. They found that synaptic input clustered on nonlinear dendrites performed better at this task than when the same input was lumped in the soma, or synapses randomly assigned to dendrites. Last, they show that in vitro measurements of dendritic integration in a specific cell type matched the optimal integration strategy expected to decode the input statistics of that particular cell in vivo. These are the three main observations, but a particular strength of this article is that it draws a clear top-down rhetoric and provides general estimates of (bayes) optimal spiking communication.

Although I don't subscribe to all the assumptions described here, they are sensible and worth a careful examination. Ujfalussy and coworkers offer a thorough and elegant treatment of the question relying substantially on most of the state-of-the-art experimental recordings relevant to this problem. The conclusions are well tested, often with very stringent criteria. The relevant literature is properly cited. The article is generally well written.

The main contributions will appeal to researchers coming from different approaches. The mathematical neuroscientist will respect the relation between the P&M model and optimal decoding. Those considering decoding spike train from a bayesian perspective will check the derivations in the supplementary material. Others coming from the literature on noise-correlation will appreciate that, with dendrites, some of the reasonings should be revised. Finally, the new theoretical role for dendritic nonlinearities can clearly be tested with present experimental techniques. For these reasons, I believe that even if the supposed role is later shown to be false or incomplete, the article will have had a strong impact on the community.

Reviewer #2 (Minor Comments):

Generally, confusion arises in the number of models considered. I think that, when a comparison between models is the main result, these different models should be mentioned at the beginning of the section. For instance in the last paragraph of the section “The form of the optimal nonlinearity depends on the statistics of presynaptic inputs” one suddenly learns of the actual comparisons being made.

On a first reading, I could not understand what was done in the first paragraph of the section” Nonlinear integration in cortical neurons is matched to their input statistics”. After reading the supplementary, it is clear, but I think a few sentences should be added to describe in a little more details what was actually compared. For instance, one can read from the first sentence that to test the theory, we need to measure presynaptic statistics and derive the optimal nonlinearity, then measure the nonlinearity in vitro and compare the nonlinearities. That is not what was done, I know now, but I could not rule that out from the paragraph as is. It is also difficult to understand the end of second paragraph of the same section on the first go.

What is the experimental stimulus protocol used in the uncaging experiments? How broad is the distribution of ISI? Evenly distributed on Figure 5c and g? Are each burst made of evenly spaced pre-synaptic encaging? Can you really say overfitting is small?

Why exactly the multi-state description in Eq. 11 and 19 if it is never used? Personally, it is only when I saw Eq. S67 that I finally reached the proper mathematical intuitions. Other than the need for simplicity, I am concerned that some of the conclusions would not hold in the multi-state scenario suggested by Eq. 11.

Figure 1: 1B is argued to offer a better fit to optimal than 1C. But there are two differences, correlation and scale. Could it be that in the uncorrelated case, the fit to optimal is not as good when the potential fluctuates on greater amplitudes? In fact, I don't understand why the uncorrelated case should not have a saturating dendritic nonlinearity to counteract the exponential spiking nonlinearity."

Reviewer #3:

The authors present a detailed mathematical analysis, computations and experimental results aimed at supporting the conclusion that dendritic nonlinearities used to integrate synaptic inputs in a neuron are optimized based upon the statistics of that neuron's presynaptic connections. In particular, the suggested result is that if a neuron's presynaptic connections are uncorrelated, sublinear responses are optimal. If, however, the firing of presynaptic neurons are correlated, supralinear responses are optimal for that neuron. If correct, I would find this conclusion to be interesting.

One of the main difficulties with the manuscript is that the details are not easily approachable. There are many pages of complicated mathematics that one must work through, and in many places there hasn't been much attempt to try to explain things in simpler terms to the general reader – I suspect that one will not be able to follow the details here unless one is already an expert.

While the major focus on presynaptic activity is in terms of spikes (and I will grant that a good explanation for this is given), I think it's a concern is that the focus on postsynaptic activity is in terms of subthreshold responses. Granted, the authors say that they can also perform their calculation if the firing rate is substituted for the subthreshold response. This seems like an inconsistency, however – if two or more neurons share synaptic inputs from overlapping sets of presynaptic neurons, and the correlations in the spiking patterns of the presynaptic neurons matter, why is it that correlations in the output spikes of those two or more neurons don't matter? This would seem to be a basic internal inconsistency in the manuscript.

In addition, while there is a huge amount of detail associated with the mathematical calculations, I found the details associated with the experiments to be a bit too sparse. It would have been useful, for example, to see an image of the neocortical pyramidal cell and the specific synapses which are being stimulated.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your work entitled "Dendritic nonlinearities are tuned for efficient spike-based computations in cortical circuits" for peer review at eLife. Your submission has been favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

All of the reviewers are strongly positive about this work but they also want to ensure that the work is accessible, understandable and widely appreciated. They would like all aspects be made as clear as possible. Thus, pending the following revisions, we expect to accept the paper.

Please respond directly to the revisions on a point-by-point basis, revising the paper where needed.

1) Double check all equations in the mathematical appendix – there was some concern given potential sign errors in other equations (see below). Additional explanatory guidance through the mathematical steps should be provided for those readers who may be interested in following these details. The math is still very complicated.

2) Check and correct potential inconsistencies related to the description of the function s(t). In the subsection “Presynaptic statistics” it is still stated that in the limit in which the time step goes to zero the discrete version becomes binary, i.e., zero or 1. In the subsection “Inference and the optimal response”, however it's stated that s(t) is a sum of Dirac-delta functions. The two descriptions can't be consistent, of course, unless there is a division by a time step somewhere. There does not appear to be a careful definition in the manuscript, however.

3) Check the solution of equation (22) given in (23) and (24) for potential sign errors.

4) The additional details about the experiments were appreciated. However, a question arose about the blocking of NMDA channels. It's stated that substantially poorer fits were obtained for this case. Please confirm/clarify whether the postsynaptic filtering parameters were re-fit in this case?

5) It seems like a bit of an inconsistency that while a big point is made that presynaptic neurons must communicate with spikes, no spiking is considered in the postsynaptic neurons. If spiking is the only way that neurons can communicate (the authors' point), why should one care about the subthreshold response of the postsynaptic neuron? Since so much of the manuscript covers the subthreshold response, something explicit (explanation-wise) should be said about this in the manuscript (and we realize that they consider the case of firing rates).

6) Include a 'toy model' explanation (without math, or if possible, with straightforward enough math equations that most can follow) that summarizes the link between pairwise correlation (temporal) and dendritic integration (spatial) before any specific statistical models are discussed. This would help the reader follow the more detailed case, and avoid confusion in consideration of later statements in the paper. A good place for this might be at the beginning of the Results section.

Specifically, the way the text reads is confusing about when spatial correlations (for lack of a better term) between different presynaptic neurons are being discussed, and when temporal correlations between inputs are being considered. Part of the issue may be that the mathematical formulation in the main text completely hides issues of temporal correlation in the details. Thus one can be left wondering if one of the two types of correlations might be more important and if the theory could shed light on this.

For example, consider these comments from the manuscript:

"However, if presynaptic neurons became correlated the optimal response became nonlinear and the best linear response was unable to accurately follow the fluctuations in the input (Figure 1D)."

"Same as (A-C) but for presynaptic neurons exhibiting synchronized switches between a quiescent and an active state (D, bottom), introducing higher order correlations between the neurons." (Figure 2 caption)

"In particular, sublinear integration was optimal when presynaptic activities exhibited simple Gaussian random walks and thus they could not contain statistical dependencies beyond second order correlations (Figure 2A-C)."

The authors here are trying to provide an intuitive explanation as to why input correlations lead to the observed behavior and this, of course, is good and to be encouraged. In each case, however, what type of correlation is being thought of – spatial or temporal? Further elaboration might provide additional insight.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your work entitled "Dendritic nonlinearities are tuned for efficient spike-based computations in cortical circuits" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Eve Marder as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

The reviewers appreciated the revisions done by the authors, but it was felt that the intuition as provided was incomplete and the mathematical appendix was still not clearly presented. Specifically, it was noted that is unclear how the authors distinguish autocorrelation from cross-correlation (spatial) in the formalism and the text, and as this is a main point of the paper, it should be up front early on in the Discussion (and not just in caption of Figure 1 and later in Methods). Also, eq A91 has an exact solution (separable). In essence, the math appendix should only include what is needed to explain the methods – anything that is more extensive than needed should be either removed or simplified.

In summary, the authors should carefully go through the entire ms to ensure that these aspects are addressed in general. Please also note specific additional comments from the reviewers to address:

1) The manuscript still has trouble delineating spatial vs temporal correlations when it tries to explain different points. For example:

Introduction section: "We pursued this principle in understanding the integrative properties of individual cortical neurons, for which the relevant statistical input patterns are those characterising the dynamically evolving spike trains of their presynaptic partners." This sounds like the manuscript is concerned with temporal issues.

"The optimal response determined by this statistical model, for essentially any setting of parameters, was inherently nonlinear because the additional effect of a presynaptic spike depended on the pattern of spikes that had been previously received from the presynaptic population and thus the integrated effect of multiple spikes could not be computed as a simple linear sum of their individual effects in isolation." This also sounds to me as if a claim that the temporal pattern of inputs is what's leading to nonlinearity.

2) Regarding the errors in the mathematics, we thought that when the authors repaired the solution of Equation 27 they would also fix other instances of this equation in the manuscript. Equation 27 is recapitulated in the mathematical appendix as Equation A91, but the discussion around Equation A91 is clearly wrong. Somehow a different solution from the solution of Equation 27 is obtained; the answer should be equation A92 with Α = 0,Β = B and C = −A. Here’s how the solution goes: we start withζ˙=ζ(1–ζ)[–Α+Βs(t)].

This equation is separable:dζζ(1−ζ)=[–A+Bs(t)]dt.

The left-hand size can be simplified by partial fractions:1ζ(1–ζ)=1ζ+11–ζ,

so that[1ζ+11−ζ]dζ=[−A+Bs(t)]dt.

Both sides of the equation can now be integrated. Assuming 0 < ζ < 1, we getlnζ–ln(1–ζ)=∫​[−A+Bs(t)]dt.

or equivalently,lnζ–ln(1–ζ)=v(t)

wherev˙=–A+Bs(t).

Then solving

ζ1−ζ=ev⇒ζ=ev1+ev+11+e−v.

We don’t know what the authors are trying to do with the rest of Section B.2.2, but it appears to be wrong. We also don’t know to what extent fixing this will affect the rest of the results.
