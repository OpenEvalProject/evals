# Peer review - Round 1

Editors:
- Sacha B Nelson, Brandeis University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.09457.014](https://doi.org/10.7554/eLife.09457.014)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “Unified pre- and postsynaptic long-term plasticity enables reliable and flexible learning” for peer review at eLife. Your submission has been favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All three reviewers found aspects of the improvement in SNR confusing. I think this can be remedied with textual changes not requiring additional experiments or simulations (although if additional simulations – e.g. addressing Reviewer #3's concerns about frequency – will help to clarify, these could presumably be included). All three reviews are included below in the hopes that this will aid in clarifying the manuscript.

Reviewer #1:

This is a carefully done, compact paper with a crisp message that offers a potential solution to an important problem in neuroscience. Although there is now broad agreement that pre- and postsynaptic plasticity mechanisms can coexist at many central synapses, the functional benefit of this is unclear. The authors here adapt prior models of spike-timing-dependent plasticity to take account of the experimentally determined properties of pre- and postsynaptic expression mechanisms for plasticity. They show two functional benefits. First, the two mechanisms better account for observed improvements in sensory discrimination with learning and second, the dual mechanism permits much more rapid relearning when the stimuli being learned change with time.

I have no major concerns.

Reviewer #2:

It is really good to see a model of this detail and rigor combining the pre and post-synaptic aspects of plasticity and to see that we have finally arrived at a point where it is accepted that pre and post-synaptic elements show plasticity. My comments are going to be fairly minor but I hope that the authors will make some effort to tackle them because it will probably help communicate the ideas.

The first point is that the model seeks to explain the advantages of presynaptic plasticity. One of these is the decrease in variance in developing receptive fields another is retained information or savings on reversal of plasticity. Unfortunately, having raked through the formulae a few times, I cannot see where this comes from. In Figure 3, the relearning occurs more quickly because the post-synaptic factor decays slowly. Can the authors explain in more detail why presynaptic plasticity improves relearning? Also, could it not (theoretically) be achieved another way, say by increasing the duration of the post-synaptic factor? I am still missing what is unique about the disposition of the presynaptic plasticity.

I am not disputing the premise, however. It may well be that the slower turnover of presynaptic terminals compared to spines allows faster relearning. I believe that Finnerty and colleagues have done some work on this and they should probably be mentioned in this paper.

The second point is that the main body of the paper seems to be over very quickly. I was left searching for more text. There are several points that could be more fully discussed, including the elements that are explicitly missing from the model and what the impact might be. For example, how does inhibition and plasticity of inhibition impact the outcome and how might the time course of structural plasticity modify the model. On the second point, the Matsuzaki reference deals with structure and synaptic weight post-synaptically but not pre-synaptically. It would also be useful to hear how the model might fit different structures - would more presynaptic plasticity be warranted in layer 5 pyramidal cells than in hippocampus for example?

Reviewer #3:

This paper presents a theoretical model for STDP that incorporates both a pre- and post-synaptic expression locus. To date the vast majority of models have focused on implementations of LTP and LTD that simply scale the value of the synaptic weight, but do not alter short-term synaptic plasticity-thus altering the temporal profile of EPSPs. Importantly the model is based on, and captures, the experimental data which strongly suggests that there are pre- and postsynaptic expression mechanisms. Together the paper is highly novel and provides important data-based insights to our understanding of synaptic plasticity.

It is very interesting that the rule results in better discrimination. What is not clear is why? That is, why does a higher P value provide improve SNR? Yes, the first presynaptic spike generates a large reliable EPSP, but the subsequent spikes are less reliable and depressed. The SNR and ROC analyses were analytical, but I'm struggling to understand how these analyses can capture the true SNR and discriminability without taking into account the firing rate of the presynaptic units. Discriminability must depend in part of on the frequency of the Poisson inputs (and the D and F time constants)-but as it stands the analysis is based on the probabilistic nature of P, that is, essentially only for the first spike. Either I'm missing something, or an analysis based on the actual simulations (which take into account the timing of the spikes) should be performed. This is probably a minor issue, however, as Figure 3C makes it clear the discriminability based on firing rate is excellent.

Based on Figure 3A, P seems to saturate at 1, meaning that there is little or no release for the next 200 ms. This is one reason the SNR calculation may be misleading. It would be useful to show postsynaptic trace segments during stimulation as part of this figure.

I think some readers, particularly, those accustomed to the hippocampal field, will be unfamiliar with the strong evidence that there are presynaptic components to STDP. So I think it is important to strengthen their argument a bit, and perhaps mention that, these studies are based on neocortical data, and that there is likely a difference between hippocampal and neocortical STDP.
