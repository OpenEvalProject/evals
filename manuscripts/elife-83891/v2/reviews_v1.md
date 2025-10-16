# Peer review - Round 1

Editors:
- Thorsten Kahnt, National Institute on Drug Abuse Intramural Research Program United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83891.sa0](https://doi.org/10.7554/eLife.83891.sa0)

This important study presents a series of behavioral experiments that test whether value normalization during reinforcement learning follows divisive or range normalization. Behavioral data from probe tests with two alternatives demonstrate convincingly that range normalization provides a better account for choice behavior and value ratings in this setting. These findings will be of interest for readers interested in neuroeconomics and cognitive neuroscience.


---

# Peer review - Round 1

Editors:
- Thorsten Kahnt, National Institute on Drug Abuse Intramural Research Program United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83891.sa1](https://doi.org/10.7554/eLife.83891.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The functional form of value normalization in human reinforcement learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Neil Garrett (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

As you can see in the individual comments there was some confusion about key aspects of your experimental approach and measures. This confusion was resolved during a discussion among reviewers. It would be important that your revised manuscript is more clear about these key aspects. In addition, it would be important to clearly discuss the differences between the predictions made by the different models in choice and learning contexts.

Reviewer #1 (Recommendations for the authors):

1. It would be important to more clearly (and early on) state how 'choice rate' was computed for the transfer phase. This may require describing the transfer phase in more detail.

2. In lines 272 and 299, please don't use 'perfectly' to qualify the match between model predictions and behavior. I agree that the match is pretty close, but perfectly implies an errorless match, which is not the case here. The authors could consider using 'closely captures' and 'closely match' instead.

3. There are several typographical errors throughout the manuscript. I am listing a few below but I'd encourage the authors to proofread the manuscript.

– Line 190: "WB_86 and WT_86", not "NB_86 and NT_86".

– Line 367-368: parenthesis is not closed.

– Line 377-378: parenthesis is not closed.

– Line 382: "that value representations are" not "that values representations are".

Reviewer #2 (Recommendations for the authors):

The main issues with the paper are expositional. Both a clarification of the simulations used to generate the predictions (Figure 1C) and a clarification of the predictions and appropriate setting of each model in previous literature is needed. In particular, DN makes no relevant predictions in a binary choice setting, so in my initial ignorance, I simply assumed the transfer phase was a trinary choice (because otherwise, DM has no bite). I was so confused by these issues that I needed a discussion with the editor after I submitted my initial report. I have left these comments in my report below (points 1-3 below) so the authors are aware of this miscommunication and that it might help them improve Figure 1 and lines 110 – 130. Finally, the statement of the results (and discussion) is rather opinionated. The writing could do with more nuance regarding the predictions of each model, the appropriate setting for those predictions, and the patterns in the data. In particular, there appear to be patterns that also reject a range normalization account, suggesting that we still have much to learn on this topic.

Before discussion with the editor:

1) The choice probabilities do not sum to 1 within condition (for example, in treatment NB, the "50" option seems to be chosen with probability.66 and the "14" with probability <.2. Similar issues arise for DIVISIVE and RANGE. Either I deeply misunderstand the experimental setting, or there is something wrong with the simulation underlying the figure (the simulation uses an argmax, so I do not see how the probabilities can not sum to 1).

2) Why are the unbiased choice probabilities for "50" equal across NB and NT in UNBIASED? Loosely speaking, the Q-learning rule used by the authors will generate a Q_45 that is normally distributed around means [14,50,32,86] (see SuttonandBarto Equation 2.6 and impose a CentralLimitTheorem). Taking the arg-max of these normal random variables will require that P(50) (weakly) decreases as the set size increases. The authors seem to be claiming that it is constant.

3) In an effort to find the causes of these differences, I attempted to simulate the model. Apart from a number of issues with the description of the computational model (see below), the reported simulation size leads to substantial variation between simulation runs (with different RNG seeds).

– Note that I did not include heterogeneity in the learning rate in these simulations, since the theoretical setting does not require it (at least the authors don't claim that it does). So α is set to 0.5, which is the mean of the Β(1.1,1.1) distribution the authors use.

After discussion with the editor:

5) Line 123: "It is calculated across all the comparisons involving a given option." This seemingly innocuous sentence needs much more explanation. Does the transfer phase include ALL binary choices between ALL stimuli, including those across conditions? So is the "86" from the WB paired with the "86" from "WT"? If so, presumably this is what is generating the identical choice rates in UNBIASED since they are essentially the same Q_45(86). It is still deeply unsettling that nothing adds up to 1 in Figure 1C, but at least now I understand the source of the differing predictions. However, there still are some issues:

– Why is there a slight increase in the choice proportion for 86 between WT and WB? Shouldn't Q_45 be the same for them because the range doesn't change?

– The number of simulations should be increased (i.e. is it just "10 choose 2" x 50 choices). Given comment 3 above, are we sure there is no noise in the predictions (see points above)? Also, the issue of introducing α heterogeneity into the simulation needs to be addressed, as it seems pointless.

6) The framing in the introduction of the paper needs to be clear about the use of a binary choice transfer phase. DN, as conceptualized by previous work the authors cite, is a model for how valuations are normalized in the choice process (e.g. Webb et al., Mng Sci, 2020, Figure A.4). As such, it is acknowledged that it has limited prediction in binary choice (see Webb et al., Mng Sci, 2020 Proposition 1). Nearly all of its testable implications arise in trinary (or larger) choice sets. For example, the quote in Footnote 1 is the first sentence of the first paragraph of a section titled "Choice Set Size Effects" which describes studies in which there are more than two alternatives in the choice set. There is no choice set size effects in this experiment because it only examines binary choice in the transfer phase, therefore it excludes the types of choice sets in which DN has been previously observed.

As such, the authors write that they opt for a reinforcement learning paradigm "because it has greater potential for translational and cross-species research". It may indeed have translational benefits for cross-species research, and learning settings are important in their own right, but the use of an RL paradigm is not innocuous. There may be critical differences in the form of value coding computations between conditioned learning settings and "descriptive" settings in which valuations are already known (as acknowledged by the authors in an earlier ScienceAdvances paper), not the least of which might be due to the differences between cortical and sub-cortical neural computations (the neural evidence for DN is primarily in cortical regions). There is only one paper I am aware of that applies DN in an RL setting (Louie, PLOSCompBio2022) to account for gain/loss asymmetry in behaviour without the need for different learning rates (though not cited by the authors). This paper should make clear that the application of DN to a conditioned learning phase is a hypothesis raised in this paper, and clarify the distinction between settings in which DN has been previously proposed and examined in other work.

7) Previous studies add alternatives to a choice set and study value normalization. They are important distinctions from this work because they test for choice set size effects explicitly. Exp 2 in Webb et al. 2020 does such an experiment (albeit not in a learning setting) and finds support for DN rather than RN. The key difference is that the additional alternatives are added to the choice set, rather than only in a learning phase. Daviet and Webb also report a double decoy experiment of description-based choice, which follows a similar intuition to this experiment by placing an alternative "inside" two existing alternatives (though again, directly in the choice set rather than a learning phase). The conclusions from that paper are also in favour of DN rather than RN since this interior alternative appears to alter choice behaviour. This latter paper is particularly interesting because it relies on the same intuition for experimental design as in the experiment reported here. The difference is just the learning vs. choice setting, suggesting this distinction is critical for observing predictions consistent with RN vs DN.

8) The experiment tests RN vs DN by expanding the range upward with the "86" option. However, RN would make an equivalent set of predictions if the range were equivalently adjusted downward instead (for example by adding a "68" option to "50" and "86", and then comparing to WB and WT, because it effectively sets the value to "0" or "1" depending only on the range). The predictions of DN would differ however because adding a low-value alternative to the normalization would not change it much. Given the design of the experiment, this would seem like a fairly straightforward prediction to test for RN. Would the behaviour of subjects be symmetric for equivalent ranges, as RN predicts? If so this would be a compelling result, because symmetry is a strong theoretical assumption.

9) There were issues with the reporting of the results that need to be addressed:

line 183, typo NB_50?

lines 182-188 need copy-editing.

line 186; "numerically lower" has no meaning in a statistical comparison. The standard error (t-test) is telling us that there is too much uncertainty to determine if there is a difference between treatments. No more, no less. Arguing for "numerical" significance is equivalent to arguing that there is signal in noise. Statements like this should be removed from the paper.

line 188 – "superficially"? a test either rejects a prediction or doesn't. More specifically, this observation also rejects a prediction of RN and should be stated as such for clarity.

line 183-184 – given that experiments a, b, and c, seem similar and are pooled in later analyses, it would be useful to also pool them to test whether there is an increase in the NT_86 vs NB_86 and WT_86 vs WB_86 choice rates (perhaps using a pooled paired t-test). A tripling of the number of observations might be helpful here for testing whether NB_50<nt_50<wb_86

line 272 – "perfectly" is an overstatement, given the log-likelihood is not zero. Also see the NB_50<nt_50<wb_86

line 299 – perhaps also not "perfect" What is the t-test reported here? And how to interpret this p-value of.13? Is this an argument for accepting the null hypothesis?

Reviewer #3 (Recommendations for the authors):

I have a few comments for the authors to consider:

1) Training performance (Figure 2) seems very close to the ceiling (i.e. accuracy of 100%) for many of the participants. I would be slightly worried that there isn't enough stochasticity for some participants to derive meaningful parameters from the model – did the authors worry about this or run any checks to guard against this possibility at all? Perhaps more interestingly, this pattern (which suggests participants quickly identify the best option and just keep selecting this) also made me wonder whether the unbiased model with a persistence parameter (i.e. which bonuses the most recent choice) would fare as well in terms of log-likelihood scores (Table 2) and/or capture the same pattern of probe (transfer phase) choices as either the divisive or range models. Could the authors refute this possibility?

2) Previous models from this group (e.g., Palminteri 2015 Nature Comms) have conceptualised "contextual value" as an iteratively learned quantity (like the Q values here). But in the normalisation models presented, this aspect is absent. For example, min(R) and max(R) in equation 8 used for the range normalisation model are simply the min/max rewards on that trial (or on the previous trial when full feedback is absent). Similarly, the denominator in equation 9 for the divisive normalisation model. In practice, these could each be updated. For example, instead of min(Ri) in eq. 9, they could use something along the lines of Vmin(i) which updates as:

Vmin(i)t+1 = Vmin(i)t + α*δ t

δt = min(Ri) – Vmin(i)t

Did the authors consider this? Or, another way of asking this, is to ask why the authors assume these key components of the model are not learned quantities that get updated over trial-by-trial experience.

3) Transfer phase – the transfer phase only contains binary combinations. However, during training participants were presented with two binary combination choices and two trinary combination choices (i.e. choices were 50% binary choices and 50% trinary). Could exclusively using binary combinations in the probe phase bias the results at all towards finding stronger evidence for the range model? I'm thinking (and I could be wrong!) that the divisive approach might be better suited to a world where choices are over >2 options. So perhaps participants make choices more consistent with the range model when the probe phase consists of binary choices but might switch to making choices more consistent with the divisive model if this consisted of trinary choices instead. The explicit rating (Figure 5) results do go some way to showing that the results are not just the result of the binary nature of the probe phase (as here ratings are provided one by one I believe). Nonetheless, I'd be interested if the authors had considered this at all or considered this a limitation of the design used. </nt_50<wb_86</nt_50<wb_86

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The functional form of value normalization in human reinforcement learning" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

As you can see, two of the original reviewers were satisfied with your revisions. However, Reviewer #2 does not feel some of their points were fully addressed. Most importantly, there are open issues regarding the contextualization of the current study as well as the important fact that DN was designed to account for choice set effects, rather than normalization during learning, as tested here. Specifically, the binary choice test is only sensitive to value normalization during learning but not whether the form or normalization of these learned values during choice. In other words, while the current experiments test the interesting and worthwhile question of how values are normalized during learning, they do not test whether DN is still applied to RN-learned values at the time of choice. In summary, there is an important distinction between the design of the current study and what has been done to study DN in the past as well as how DN was originally conceptualized. We agree with Reviewer #2 and feel that this distinction should be acknowledged and clarified throughout the paper, most importantly early on in the introduction. Also, the discussion would benefit from revisions that restrict the conclusions of the findings to the appropriate (i.e., learning) context. We are looking forward to receiving a revised version of your interesting and important manuscript.

Reviewer #2 (Recommendations for the authors):

The authors have addressed some of my comments from the previous round, though a few remain. In particular, there still seems to be some disagreement over how to describe the study and place it in the context of previous literature. I realize that the authors are addressing (what they interpret) to be overly-strong general statements about the form of normalization in decision-making. This is a useful undertaking. But repeating the same mistake of over-generalizing and not placing the results in context will only serve to continue the confusion.

1) In their reply, the authors write:

"The outcome presentation stage is precisely where (range or divisive) normalization is supposed to happen and affect the values of the options (see also Louie et al., 2022). Once values have been acquired during the learning phase (and affected by a normalization process that may or may not depend on the number of outcomes), it does not matter if they are tested in a binary way."

and:

"First of all, we note that nowhere in the papers proposing and/or defending the DN hypothesis of value-based choices, we could find an explicit disclaimer and/or limitation indicating the authors believe that it should only apply to prospective valuation of described prospects and not to retrospective valuation of obtained outcomes."

I fundamentally disagree on this point. There are various opinions on where normalization is "supposed to happen." Multiple papers have conceptualized DN as a process that occurs during decision and not learning (the citations were provided in the previous round, including some that I feel qualified to interpret). Louie et al., 2022 is the first paper that I am aware of to apply it in learning settings (though an argument can be made that Khaw, Louie, Glimcher (2017, PNAS) has elements of a learning task). That it took 15 years of empirical research to explicitly approach the learning setting should be evidence enough of how its proponents were conceptualizing it. The 2011 review paper that the authors interpret as making this claim simply notes that the matching law implies that "the primary determinant of behaviour is the relative value of rewards." (pg 17). In the immediate sentence following they pose the question: "Does the brain represent action values in absolute terms independent of the other available options, or in relative terms?" to set up the remainder of the paper. The use of the term "action values" by Louie and Glimcher is critical. This is neuro-physiological terminology used to describe the motor/decision stage, where the values that have been learned (by the then-standard RL and RPE circuitry covered in pg 14-16) are used to make decisions (these are the Vs in the 2011 paper, or the Qs in the author's model). It is these Vs that are transformed at the time of decision. See also Webb, Louie, Glimcher (pg 4) for a clear statement of this. Nowhere in these articles is it claimed that the action values in learning settings (again, the Vs!) are formed in a relative manner (like in the authors' Equation 4, 5, and 9 for their Qs).

Of course, this point does not diminish the fact that the authors are testing for DN during the updating step in learning, with some compelling evidence. But we need to be clear on where the DN theory has been largely proposed by previous literature, and where the DN theory has been previously shown to capture behaviour (choice sets with more than two options). This is what I mean when I say it is a hypothesis the authors (or their previous reviewers) are proposing and evaluating in their papers. There are perfectly good reasons to examine DN in this setting (see the normative discussion below) and that should be sufficient to frame the question. I believe these issues need to be framed clearly by the introduction of the paper, rather than as an aside at the end of the Discussion.

line 61: This seems like an ideal spot to clearly state that nearly all empirical applications of DN apply it at the decision stage and address choices with more than two options. In particular, the study by Daviet and Webb implements a protocol similar to the design used here but in a "descriptive" rather than a learning setting (see comment below). The text could then note that "Few recent studies have extended…."

As a final point, if the design included three or more alternatives in their transfer phase, there is some reason to believe that behaviour would depart from the model the authors propose (i.e. we might start to see behaviour influenced by more options at the decision stage). Therefore, contrary to the author's claim, it would "matter if they are tested in a binary way". Therefore the results should only be interpreted as applying to the learning of the valuations, not their use during decision. I agree with the changes to lines 141-145, however, the paper up to this point has still not stated that DN at the decision stage has no strong predictions in binary choice. The reader thus has no context on why that statement of line 141 is true. This needs to be clarified.

2) I am re-stating here my comment from Round 1: Previous studies add alternatives to a choice set and study value normalization. They are important distinctions from this work because they test for choice set size effects explicitly. Exp 2 in Webb et al. 2020 does such an experiment (albeit not in a learning setting) and finds support for DN rather than RN. The key difference is that the additional alternatives are added to the choice set, rather than only in a learning phase. Daviet and Webb also report a double decoy experiment of description-based choice, which follows a similar intuition to this experiment by placing an alternative "inside" two existing alternatives (though again, directly in the choice set rather than a learning phase). The conclusions from that paper are also in favour of DN rather than RN since this interior alternative appears to alter choice behaviour. This latter paper is particularly interesting because it relies on the same intuition for experimental design as in the experiment reported here. The difference is just the learning vs. choice setting, suggesting this distinction is critical for observing predictions consistent with RN vs DN.

R2.5 We thank the Reviewer for pointing another important reference that we originally missed. The suggested paper is now cited in the relevant part of the discussion (which is copied in R2.4 above).

I'm not sure that the authors interpreted my comment correctly. I don't understand citation #64 in the Discussion or what that paper has to do with risk. I raise the Daviet and Webb study because it implemented a similar design intuition as this study (inserting an option between two options so as not to alter the range), except with "described" alternatives and not learned outcomes. The conclusions in this paper differed from those reported. The manuscript should clearly state this similarity (and important difference in conclusion) between the two as context for the paradigm the authors are using.

3) In Discussion:

a) lines 361-371: This paragraph argues that "We find no evidence for such a [choice set size] effect". As noted in my previous report (and again above), this study is not examining choice set size effects. The size of the choice set in the transfer phase is always binary. Instead, the study is examining the relative coding of learning. This paragraph needs to be re-written so that this is clearly stated. Referring to the results from the transfer task as a "trinary decision context" is confusing.

b) "However, it is worth noting that evidence concerning previous reports of divisive normalization in humans has been recently challenged and alternatively accounts, such as range normalization, have not been properly tested in these datasets 29,65."

The test for Range normalization in the original Louie et al. dataset is in Webb, Louie andGlimcher 2020, Mng Sci and is rejected in favour of DN. It is not clear what the authors mean by "properly."

4) R2.3b In the ex-ante simulations, we randomly sampled both of these parameters from Β(1.1,1.1) distributions, which inherently leads to different predictions in the transfer phase for the binary and trinary contexts, because the choice rate impacts the update of each option. The fact that small differences derive from allowing different learning rates for obtained and forgone outcomes, is confirmed by simulations. We nonetheless kept the original simulations, because they correspond better to the models that we simulated (with two learning rates). The authors are arguing that there is a systematic difference in the predictions for Range WT_86 WB 86 when using two learning rates. This is not an obvious result, but the increase to 500 simulations seems to confirm that it is systematic. This should be clarified in the text. Otherwise, it will be confusing to readers why the predictions change.

5) From Round 1: line 415 – what is meant by "computational advantage" here? The rational inattention literature, which provides the normative foundation of efficient encoding, places emphasis on the frequency of stimuli (which is completely ignored by range normalization) (e.g. Heng, Woodford, Polania, eLife).

Reply: "R2.18 Range and Divisive normalization both provide, to some extent, the computational advantage of being a form of adaptive coding. If the topic interests the Reviewer, we could point to a recent study where their normative status is discussed: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4320894"

The normative argument for relative coding (including both DN and RN) that the authors point to is specific to a learning context (via the exploration/exploitation tradeoff). And even then, it is not an argument that an efficient code should use only the range. Thus it is important to keep in mind that the results reported in the current manuscript may be somewhat specific to the learning setting implemented in the experimental design. Multiple theoretical and empirical papers from across neuroscience and economics have examined the form of normative computation in general settings (Heng et al., cited above; Steverson et al. cited in previous report; Netzer 2009 AER; Robson and Whitehead, Schaffner et al., 2023, NHB) and all have shown that the efficient code adapts to the full distribution of stimuli. It is reasonable to imagine that some physical systems might approximate this with a piecewise linear algorithm based on the range, but this has not been observed in the nervous system (V1, A1, LIP etc.). Of course this can't rule out the possibility that V1, A1 and LIP get it right with a standard cortical computation, but for some reason other areas have to resort to a cruder approximation. But that isn't the obvious hypothesis. Tracking the minimum and maximum – including identifying which is which – seems both unnecessary and complicated in real-world scenarios. Whether (and how much) the results reported in the paper generalize outside this experimental design is an open question.
