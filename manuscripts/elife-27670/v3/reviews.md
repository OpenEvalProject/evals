# Peer review - Round 1

Editors:
- Fred Rieke, Howard Hughes Medical Institute, University of Washington , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27670.024](https://doi.org/10.7554/eLife.27670.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Olfactory receptor neurons use fast dynamic gain control to encode intermittent odorant stimuli" for consideration by eLife. Your article has been favorably evaluated by a Senior Editor and three reviewers, one of whom, Fred Rieke (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Tim Holy (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife, at least without substantial revisions.

Two main points emerged in discussion among the three reviewers about the paper. We highlight these points because we felt they could change how the data is interpreted. All reviewers agreed that these points were important to deal with before we could consider the paper further. Individual reviews, attached below, will both elaborate on these points as well as detail other important issues to consider.

Adaptation vs. saturation.

Adaptation as defined in the paper includes both time-dependent changes in cellular processing as well as static nonlinearities in the response – such as receptor saturation. We felt it was quite important to separate these effects as much as possible. This could, for example, involve fitting NLN models to the responses, providing a "front-end" nonlinearity that could account for receptor saturation. Several related comments in the individual reviews involve how gain is defined and how much the conclusions depend on the definition of gain.

Validity of LN models.

The LN models the form the core analysis tool in the paper are not validated. Several assumptions are central to the analysis. Some of these points may also originate from a lack of clarity in the paper about details of how the LN models were fit. Most importantly, it is not clear in all cases how the linear filter used to project the stimulus was computed. For example, since the standard linear filter calculation assumes symmetry of the stimulus, it is not clear how filters were computed for the naturalistic odor stimuli.

Reviewer #1:

This paper describes adaptation to the mean and variance of odorant stimuli, with a particular focus on adaptation to natural inputs. The question is quite interesting, and for the most part I found the conclusions of the paper well supported by the data presented. Several issues, however, limit my enthusiasm.

How good are LN model fits to the data?

The paper relies extensively on LN models to analyze adaptation. More validation of this approach is needed – e.g. how much of the response variance do LN models describe? Related to this point – are the linear filters used in analysis of responses to naturalistic inputs derived from responses to Gaussian noise inputs (this seems to be the case from the Methods)? If not, how are the filters computed? If the filters are computed for Gaussian noise inputs, are they still valid for naturalistic inputs? Similarly, in Figure 4 – are the low variance and high variance filters assumed to be the same, and is this indeed correct?

LFP as a proxy for transduction.

The LFP is used to estimate properties of odor transduction. It is not clear from the paper how good a proxy the LFP is for transduction, specifically whether it is accurate enough to support the conclusions drawn. More verification of the validity of using the LFP is needed.

Gain definition.

The gain in Figure 2 is defined as the slope of the firing rate vs. projected stimulus curve. But doesn't that mean comparing different firing rates for different whiffs – and hence potentially confounding adaptive effects with static nonlinearities in the responses? This issue also comes up in Figure 3B.

Compensation for slowing of transduction.

The conclusion that speeding of post-transduction processes with adaptation compensate for slowing of transduction is not well developed, especially for a major conclusion of the paper. This relates to the point above about using the LFP as a proxy for transduction.

Reviewer #2:

The submission by Gorur-Shandilya and colleagues examines the dynamics of odorants responses in Drosophila ORNs using both naturalistic (plume-based) stimuli and gaussian stimuli of controlled mean and variance. The authors show that adaptation occurs on rapid time scales in a manner consistent with the well-known Weber-Fechner "law." By measuring both field potentials and spiking, the authors attempt to dissociate transduction dynamics from spiking dynamics, and discover that the two have compensatory kinetic characteristics, so that overall the firing preserves the dynamics of the stimulus.

This study brings the analysis of Drosophila ORN dynamics closer to the standard set in, e.g., phototransduction and several other sensory systems, and for that reason has considerable value. Overall, the results suggest a fair degree of correspondence with the early stages of visual encoding, right down to the magnitude of the relevant time scales. As the authors acknowledge, it is primarily a "phenomenology" study, leaving most questions of mechanism for future work. (The approximate dissociation of spiking vs. transduction is something of an exception, however.) However, the history of other systems argues that quantitative characterization of the phenomenology is an essential step along the path to discovering the underlying machinery.

At a big-picture level, the Introduction sets the stage well, the manuscript as a whole appears scholarly, and the claims seem well-supported by the data and analyses. A key component of this work is the impressive control over stimulus delivery, which is much harder for olfactory stimuli than for visual stimuli, and the authors clearly went to great lengths to achieve this control. Consequently, this study has a lot to recommend it, and little to dislike. My concerns are minor, focusing on the clarity of descriptions, particularly in the Materials and methods section (which is not up to the standard set in the rest of the manuscript). In its current state I suspect that readers will have considerable difficulty understanding exactly what was done at several points in the manuscript. There are some places where I question details of the results, but it seems likely that this is due to a misunderstanding of the precise form of the analysis.

Figure 2D: one oddity is that the tangent of the f-s curve even at 0 appears strongly correlated with the ultimate size of the excursion. Naively, this would appear to violate causality, but of course it could reflect correlations in the stimulus. Nevertheless, it begs the question of how much of this analysis is really dominated by the stimulus correlations; there don't appear to be any examples of a large stimulus that were not preceded by some adaptation, and that leads to concern about the thoroughness of this particular test and analysis.

Reviewer #3:

This paper examines the responses of Drosophila olfactory receptor neurons to dynamic fluctuating stimuli and analyzes their responses predominantly using linear filter methods. Based on these analyses the authors argue that ORNs exhibit fast adaptation that allows them to better encode the properties of odor plumes. The experiments appear to be carefully performed and the data appear to be solid. However, I have concerns about the novelty of the approach and findings, as well as some of the analyses and interpretations.

Linear filter methods have been used for many years to approximate the response of a sensory neuron to a complex time-varying stimuli. A common theme of these studies is the finding that the linear approximation of the response varies as a function of stimulus statistics such as the mean and variance (e.g. Fairhall 2001, Baccus and Meister 2002). In particular, the approximate gain of the neuron generally decreases with increased stimulus variance, a phenomenon known as "gain scaling" or "variance scaling". Following on these studies several groups asked whether single neurons could exhibit this property in response to current injection, and found that it could. Subsequent modeling studies have shown that Hodgkin-Huxley models and other spiking models are capable of producing gain scaling (e.g. Lundstrom et al., 2008). Therefore, the finding that Drosophila ORNs exhibit gain scaling, and that some of this scaling arises at the level of spike generation does not seem novel or surprising.

In the Drosophila olfactory neurons studied here, several papers have examined responses to temporally modulated stimuli (e.g. Kim 2010, Nagel 2011, Martelli 2013, Cafaro, 2016, Cao, 2016). Multiple studies have found that transduction response magnitude (measured intracellularly or by LFP) is well described by a Hill equation, (that is, it rises sigmoidally with log odor concentration), as one would predict from the basic biochemistry of receptor activation (Cao, Cafaro, Nagel). Second, they have found that OR-expressing ORNs exhibit calcium-dependent adaptation that dynamically adjusts sensitivity and gain (Cao, 2016). The approach taken here confounds these two phenomena, as it assumes that responses are a linear function of concentration (here shown to be linearly related to PID voltage). Therefore, the "adaptation" reported by the authors likely contains contributions from the nonlinearity inherent in receptor activation, as well as true dynamical adaptation. This might be addressed by computing filters based on the log concentration, rather than linear concentration, and by comparing "adaptation" (estimated from projections onto linear filters) in OR- and IR expressing ORNs, as IR-expressing ORNs do not exhibit calcium-dependent adaptation, but do show activation nonlinearities.

An issue in the paper is what is meant by "adaptation." The authors seem to argue that adaptation is any change in the linear approximation to the response. For example, in the Introduction they state that they are focusing on phenomenology, which they call "a prerequisite to understanding the mechanisms that implement them." In the Discussion, they say that "'adaptation state is a construction to understand nonlinearities in that response." However, many other parts of the paper imply that these "adaptations" are actively produced by the cell in order to optimize coding. For example, in the title "Olfactory receptor neurons use fast dynamic gain control", Results "small isolated whiffs were amplified…suggesting that ORNs adjusted their gain dynamically", "suggesting that ORNs actively changed their gain." The question of whether certain coding phenomena arise from active adaptation processes, or from unavoidable nonlinearities of receptor-ligand interactions seems germane to the framing of the paper, and the question of whether the phenomena they describe are specializations of insect neurons for encoding odor plumes or general properties of receptor-activated neurons.

A second issue is the characterization of phenomenology versus mechanism. Although the authors claim to focus on phenomenology, a significant part of the paper is devoted to the distinguishing phenomena arising at the level of transduction/LFP, and those arising at the level of spikes- an attempt to place phenomenology in a mechanistic context. Given that multiple stages have been experimentally identified in the transduction process (Cao et al. 2016), and that many models of spike generation are available, it does not seem fair to call this phenomenological characterization a "necessary prerequisite" to mechanistic understanding.

Other comments:

The finding that ORN spikes seem to counteract some of the slowing of transduction responses is interesting and novel but not well-developed.

I am concerned about the linear filter method applied to responses to sparse stimuli in Figure 2. As stated in the Materials and methods, linear filters can be reliably estimated in the presence of an output nonlinearity if the stimuli are Gaussian- however, this is generally not true for stimuli that are strongly skewed, such as the one used here.

In general the authors do not report the goodness of fit of their linear model, making it difficult to interpret whether the observed changes in gain (where gain is the slope of the projected versus real response) are significant.

The authors state: "It remains unclear whether the ORN's ultimate output- the firing rate- follows the same Weber-Fechner scaling." However, Cafaro, 2016 does address this question for ORN spikes, as well as PN membrane potential and spikes.

Introduction, last paragraph: It is unclear at this point in the text why the authors choose to focus on a history of 300ms. This should be better motivated.

Subsection “Fast gain control maintains timing information of naturalistic odor signals”, third paragraph. It would be helpful to at least briefly mention how lags were computed in the Results.

Subsection “Variance gain control in olfaction”. No potential mechanisms for gain scaling of transduction responses are given.

Subsection “Fast gain control could aid in naturalistic odor detection”. The authors state that paradigms that employ conditioning and probe stimuli cannot easily quantify the dynamics of gain change. This does not seem accurate. These paradigms explicitly allow the experimenter to distinguish the stimuli used to generate adaptation from those used to test it. Small combinations of pulses are used to examine the dynamics of gain change in transduction in Cao et al. 2016.

Subsection “Stimulus measurement”. It would be helpful to include a diagram of the odor delivery apparatus along with calibration data.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Olfactory receptor neurons use gain control and complementary kinetics to encode intermittent odorant stimuli" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tim Holy (Reviewer #3).

The reviewers have discussed the reviews with one another all agreed that the revisions have improved the paper substantially. There are a few outstanding issues outlined in the reviews below.

Reviewer #2:

The revised manuscript describes encoding of dynamic stimuli by ORNs. The authors have addressed several of the major concerns cited by all reviewers. First, they find that a static front-end nonlinearity (a Hill function) can account for much of the nonlinearity observed in response to naturalistic odor stimuli, but that a dynamic adaptation component remains. Second, they have expanded their analysis of the dynamics of spiking and transduction, to show that speeding of spiking compensates for slowing of transduction with increased stimulus mean, resulting in spike timing that is independent of stimulus mean- an interesting and novel result. Finally, they have developed a receptor-based model to account for the observed forms of adaptation.

Overall the manuscript is much improved. I think it makes a substantial contribution to the literature. I do have some remaining issues with the manuscript that I think should be resolved prior to publication.

1) The Hill function as a source of nonlinearity.

The reviewers previously asked whether many of the nonlinearities described in the data could arise from receptor-ligand interactions, which should give rise to a nonlinear relationship between odor concentration and transduction. The authors have re-analyzed their data and found that responses to natural stimuli are well-described by such a relationship (Figure 1E-F), although context-dependent deviations from this relationship remain (Figure 2). However, it seems that this understanding is not entirely integrated into the text. For example, the title of the first section is "ORN responses to naturalistic odorant stimuli show deviations from linearity that arise from adaptation and saturation" which implies that saturation is the only nonlinearity (not the logarithm implied by the Hill function). Much time is spent on showing that responses deviate from linearity, and then receptor-ligand interactions are suggested as an alternative to output nonlinearities, which seems odd, given that receptor-ligand nonlinearities are an obligate feature of a system composed of odorant receptors that bind and are activated by odorants. A finding that odor concentration is encoded linearly by such a system would be much more surprising. Along these lines, in the Introduction, the authors state that "ORNs employed front-end nonlinearities" which makes it sound like an active choice on the part of ORNs. I think a fairer statement of the findings would be that a front-end nonlinearity, combined with dynamic adaptation that shifts the midpoint of this nonlinearity, can account for ORN responses to a variety of dynamic stimuli.

2) Explanation of Weber-Fechner scaling.

Understanding the origin of Weber-Fechner scaling is a major goal of the paper. Along the lines above I would suggest that Figure 3—figure supplement 2 should be made part of the main text. This shows that the expected front-end nonlinearity, combined with adaptation that shifts the activation curve to the right, is sufficient to account for ORN responses to stimuli with different means. As such a rightward shift with adaptation has been previously reported (Kaissling, 1987, Nagel and Wilson, 2011), this makes for an elegant explanation of the observed responses.

The authors state that the receptor model alone cannot account for Weber-Fechner scaling (response to reviewers 1B). It is true that the receptor model alone does not produce responses that change gain and have similar mean, as in the data. However, it does seem that the receptor model alone (Figure 3—figure supplement 2, panel c) shows a decrease in gain with increased mean. If the output of this simple model were plotted as in Figure 3F what would it look like? Does the change in gain arise from the dynamic adaptation (the shift in half-max) or from the nonlinearity?

3) Receptor-based model.

The authors present a new model, based on a 2-state receptor model, to account for the observed adaptation. As I understand it, their model makes two assumptions: (1) receptor activation/inactivation are the rate limiting steps, and (2) receptor activity feeds back onto these rates, slowing both. The model thus makes specific predictions about what biophysical steps give rise to adaptation.

Given the findings in Figure 3—figure supplement 2, it seems like the main features necessary to explain the results are (1) steady-state output rises as S/S+K, (2) adaptation shifts K to the right, (3) adaptation decreases transition rates, leading to slower responses. The authors should clarify which aspects of their model are essential for reproducing the key features of the data.

4) Use of the LFP as a proxy for transduction.

It is true that it has become somewhat standard in the literature to do this but the LFP should be interpreted with a bit of caution. In Nagel and Wilson 2011, palp LFPs were used because LFPs in this structure were found to more closely reflect activity in a single sensillum (presumably because of the greater spacing between sensilla). A brief caveat noting that LFPs can contain a contribution from nearby sensilla would be welcome.

Reviewer #3:

The revisions thoroughly address my concerns. I am quite satisfied with the revised manuscript.
