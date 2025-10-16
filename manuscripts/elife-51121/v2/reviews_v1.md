# Peer review - Round 1

Editors:
- Stephanie Palmer, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51121.sa1](https://doi.org/10.7554/eLife.51121.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work addresses how accurate readout in the brain can be maintained despite shifts in neural population tuning and variability. The work reanalyzes previous data from posterior parietal cortex and digs deeper to show that a simple linear readout can, in fact, recover kinematic variables like animal position and speed from this drifting population. While this simple readout works well, it does slowly degrade over days. This work also shows how to ameliorate this degradation: plasticity that operates via a biologically plausible mechanism can maintain accurate readout.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Stable task information from an unstable neural population" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

This is a clearly-presented initial study on how stable readout across days might be achieved despite shifting neural representations. The results have been judged to be sound, analytically, but the potential impact of the work falls short of threshold for a Short Report. Individual reviewer comments are listed below, but the main critiques are summarized here:

1) There are only data on 1 mouse to support the key result, which itself is not surprising given previous work from Driscoll et al., 2017.

2) The present work lacks a null model against which one can properly interpret the success of the concatenated decoder.

Reviewer #1:

This is a well-written, short manuscript about changes in neuronal activity patterns in PPC over days, and how stable readout can be achieved with a simple, linear decoder despite these shifting sands. The idea is that a single, best compromise, linear decoder can be found that is immune to the reconfiguration in the neural population. The work posits, but doesn't prove that the reconfiguration exists in the "null space" of the task.

There are a number of theoretical papers (as nicely referenced in this document) about how accurate decoders might be maintained in changing neural populations, but the upside of this work is that:

a) The results are taken from experimental data with large enough N's and over enough days that decoding accuracy can be traced, and

b) This is the simplest of all possible theories of how performance is maintained, and it's reasonably plausible.

I have some substantive concerns :

1) Given that the consensus decoder had to perform better across days than any single day decoder, it's not clear how surprising these results are.

2) It wasn't clear how well this extrapolates across different mice. In some figures, 3 or 4 individuals are compared, others just 2, others yet, just 1 mouse (mouse 4) is mentioned. This is central to the generality of the paper and should be laid out more clearly. Do the concatenated decoder and LMS decoder results hold for more than one individual?

3) The arguments about the scaling of the biologically plausible weight adjustments seem a little problematic. It's not clear why the results here form an upper bound on the weight changes needed to maintain accurate decoding. Also, it wasn't clear how the interactions between networks, maintaining congruence, is achieved. That final part of the Discussion was a bit vague.

Reviewer #2:

Loback et al. re-analyze data from Driscoll et al., 2017, which had previously shown that PPC representations are unstable over days during a delayed VR T-maze task. Here, using linear decoders, they find that a static decoder can do a reasonable job if trained on data from all days, and that an old model of synaptic weight updates can be applied to maintain decoder performance. The analyses seem to have been done reasonably, but the results strike me as rather shallow and are based on limited data.

The first main result is simply that unstable representations cause single-day (linear) decoders to generalize poorly, but a multi-day decoder to perform somewhat better. I have two issues with this result:

1) Given that activity is sparse and does not have systematic shifts in tuning, this decoding result is very nearly a mathematical necessity. Because of sparsity, the decoder likely ends up built so that different units drive the decoder performance on different sessions. This would not be news. Further, there are no null models analyzed for what would happen under different patterns of tuning shifts, which would be a helpful comparison. It is therefore not clear whether there is anything to be surprised at here.

2) How stable is the behavior within and across sessions? Details of behavior matter all over the brain (Stringer, Pachitariu et al., 2019, Musall, Kaufman et al., 2019), so it is possible that drift in behavioral details could lead to these shifts as well. At least, it should really be shown whether the parameters the authors track are stable over time.

These points said, there is value in this section. The quantifications of instability and of how many neurons are required for good decoder quality are helpful, and the point that only 6% of neurons are even in the top 50% of informativeness is surprising and interesting.

The second major result is the application of the Widrow and Hoff, 1962 model. If I understand correctly, this is primarily a different way of quantifying how fast the tuning changes occur (requiring ~2%/minute weight changes), and secondarily a proof of principle for that model. However, unless I'm missing something, this is a one-mouse result. That would not meet the standard for the field. In addition, comment #2 above applies to this result as well, making it harder to interpret.

Reviewer #3:

In their report, Loback and colleagues reanalyze data from Driscoll et al., 2017. They confirm the finding of that paper, namely that neuronal representations in the parietal cortex of mice reorganize over the time scale of days, while the overall information content is preserved. The authors then more specifically study the dynamics of these changes and relate them to simplified synaptic plasticity rules.

Overall, I find that the paper is clearly written and everything seems technically correct. However, I also find that it lacks scientific novelty. While I find the idea of linking the observed reorganization of neural activity with synaptic plasticity exciting, I find that the paper does not quite achieve that. I think the authors would need to work out some concrete consequences/constraints on plasticity for

this paper to become viable.

Broadly speaking, the current study is divided into two parts. The first part is a re-analysis of the data of Driscoll et al., 2017, which is performed in Figures 1-3. The authors use decoding methods to retrieve task information from the population activity. While some of the details of the population decoding methods are different to those used by the Driscoll et al., the overall conclusions are the same. The strongest point of the re-analysis is that the authors more clearly quantify the strength of the day-to-day changes using decoders that are constrained to change only little over days. That is a nice twist that was not performed in the Driscoll paper.

The second part of the paper is an attempt to relate these day-to-day changes to synaptic plasticity (Figures 3, 4). This part is rather brief and quite sketchy. Roughly, the authors simply reformulate the constrained decoder as an adaptive decoder. Conceptually, that is similar to the ideas brought forward by Rokni et al., Ajemian et al., and others. What could make this part interesting, is if this link could be made stronger, i.e., if it could really be a link to synaptic plasticity, rather than a link to a hypothetical readout. But even if the authors limit themselves to a single readout neuron, many questions are left unaddressed, e.g. how to extrapolate the adaptation rules for the decoder to realistic network sizes.

Other comments:

1) It was not clear to me what happens with the decoders within a session and between days. Do decoders 'jump' between days or stay roughly the same? How does that influence the adaptation rules?

2) Legend of Figure 4 and subsection “Biologically plausible weight adjustment can compensate for ongoing reconfiguration of PPC activity”. You repeatedly state that you approach the 'concatenated decoder.' I guess that should be the 'constrained decoder', otherwise it makes no sense to me.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for choosing to send your work entitled "Stable task information from an unstable neural population" for consideration at eLife. Your letter of appeal has been considered by a Senior Editor and a Reviewing editor, and we are prepared to consider a revised submission with no guarantees of acceptance.

Please address the following concerns that were raised in the discussion of your appeal and revised manuscript:

The null model added is a very nice one (Figure 3—figure supplement 2). It seems there has been a good effort to match it to properties of the data while incorporating a random walk. This is a crucial control. In addition, the new analysis of how drift aligns with coding vs. noise vs. chance (Figure 3—figure supplement 3) is also of substantial interest. Both of these new results are for 4 mice, which is excellent. The framing in the new manuscript also makes it somewhat clearer what the point of this paper is.

Points left to address in full:

1) Please go back and consider the more interesting null model in the other analyses and quantifications in this manuscript. This will improve many other parts of the paper. Please also place this new null model result in the main text of the paper.

2) Regarding the new null model:

Past evidence has clearly shown that neural tuning (or population activity) changes both randomly (assumed to be due to plasticity noise) and directionally (assumed to be due to feedback and learning). With the new null model, the analyses attempts to rule out a random walk. This is valuable effort. However, please add commentary on how this null model is useful despite ignoring the influence of the systematic, directional changes which were already demonstrated in the past, including the authors' own data, and which have usually been related to ongoing learning.

3) Please address in full the expanded review comments sent during the initial appeal. That text is reproduced here:

Thank you for sending us your thoughts and questions about the reviewer comments. This is an excellent piece of work, and the rejection is in no way about whether or not this is solid and publishable. The debate amongst the reviewers revolved around whether it was a significant enough advance for eLife. I have consulted with the reviewers in question and have a more thorough explanation of their comments. Please feel free to reach out if you have further questions.

This manuscript does, indeed, have some basic controls / null models. The shuffle control shows that the decoding is better than chance, and the static same-day model gives an idea of how much the weights have to change per session to do as well as freshly retrained decoders. The null models we'd like to see would compare results with more specific models. This is explained below:

The issue that I think all of the reviewers had is that it wasn't clear how much we should be surprised by these results, and we weren't clear on what new beliefs we should have after reading this paper if we've already read Driscoll, 2017.

There are two basic results that are claimed to be original. First: we should be surprised by the success of a concatenated decoder. On reviewer commented:

"Given that activity is sparse and does not have systematic shifts in tuning, this decoding result is very nearly a mathematical necessity. Because of sparsity, the decoder likely ends up built so that different units drive the decoder performance on different sessions. This would not be news."

In other words, to believe that there's something novel here, we would want to see a null model that can recapitulate the changes seen in Driscoll, 2017, with similar sparsity in the responses, where there isn't an ability to obtain a good concatenated decoder. We'd like to see what's required to have a different result. Without that, we would have expected that the concatenated decoder would work well.

Second, as it was understood by the reviewers, the manuscript argues that we should be surprised that updating decoder weights with the Widrow and Hoff model works here. From Driscoll, 2017, we have an idea of how rapidly location selectivity changes, and how rapidly a static decoder decays. Given that we know this, how rapidly would you expect to have to change the decoder? We didn't see much in the paper that wasn't just a different way of quantifying the same tuning changes. One reviewer suggested adding more specific null models because they think this would let the authors answer these deeper questions. For example, are all of the neurons smoothly changing their tuning? Do some change fast and others slow, and is this a continuous distribution? Is there coordination between neurons' tuning changes or are neurons changing independently? The current null models are extremes: the shuffle is related to a model where everything changes instantly (obviously wrong), and the same-day decoder is equivalent to there being no changes ever (which we know is wrong from Driscoll, 2017). So, what new have we learned?

Finally, regarding the result that only 6% of neurons are in the top 50% all 10 days: again, we lack the context to know how surprised we should be. If we suppose that the informative neurons are chosen randomly each day, then we'd expect the number of neurons that are in the top 50% for 10 days to be 0.5 ^ 9 = ~0.2%. In that case, 6% is surprisingly high. Looking at Driscoll's Figure 2B, ~40% of neurons keep their place preference for 10 days. In that case, 6% is surprisingly low. In fact, why is it so low? Could this just mean the decoder is under-regularized?
