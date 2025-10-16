# Peer review - Round 1

Editors:
- Peter Latham, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79928.sa0](https://doi.org/10.7554/eLife.79928.sa0)

This is an important study of the role of spike timing in the turtle cortex. The authors provide compelling evidence that single spikes evoke motifs via strong connections, and that those motifs can be reliably routed by weaker connections. The work is careful and clear and makes intuitive predictions about how motifs are generated. It will be especially interesting to determine to what extent the results apply to the mammalian cortex.


---

# Peer review - Round 1

Editors:
- Peter Latham, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79928.sa1](https://doi.org/10.7554/eLife.79928.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Single spikes drive sequential propagation and routing of activity in a cortical network" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Abigail Morrison (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

In a surprising display of unanimity, all three reviewers very much liked the paper, and all three reviewers had one main comment, which is related to the exceptionally low firing rates in the ex-vivo turtle cortex. Our question is: would you see repeated patterns if the firing rate were higher? Extrapolation of your simulations suggests not:

In the "Connectivity" section, starting on line 688, you ask the question "could strong connections underlie cortical sequences more generally, and are sequences an ancient feature of cortical computation?" You don't exactly answer that, but doesn't Figure 2F, which shows that the number of followers falls off rapidly with firing rates, tell us that the answer is likely to be no?

We hesitate to ask for more simulations, but without them, we're not sure this work can't be extrapolated beyond the ex-vivo turtle prep, as you appear to have done:

Line 212: "Our simulations further predict that sequences can occur under in vivo levels (high firing rates) of spontaneous activity".

Lines 594-5: "Our model produces reliable sequences from single spikes as experimentally measured ex vivo and predicts their existence in vivo, where firing rates are higher, with marked differences between excitatory and inhibitory neurons."

We looked at your Ref. 30, and Figure 8C of that reference shows firing rates in an awake turtle prep ranging from 0 and 5 spikes/s following a visual stimulus, with a mean of about 2.5 (and a max of 20). This is much higher than the 0.02-0.09 spikes/s you used in your high firing rate simulations (from line 191). We might be misreading Ref. 30, but certainly, your firing rates are 1-2 orders of magnitude lower than what's found in the mammalian cortex.

Along the same lines, on lines 468-73 you say: "In sum, we identified gate neurons in different sub-networks whose activation is critical for the activation of the sub-network. External single spikes can control the state of gate neurons and thus halt or facilitate the activation of individual sub-networks. The effect of these spikes depends on their timing relative to the sequence trigger. Finally, the activation of a sub-network may influence other sub-networks via recurrent connectivity leading to complex and non-reciprocal interactions."

We're not sure this result will be robust in a noisier network at higher rates; that should be clear.

On a secondary note, which relates to clarity, we will admit that there was somewhat of a split. Reviewer 2 found the paper "exceptionally clear and well-written", whereas Reviewer 1 found the paper often confusing. Here is a summary of what Reviewer 1 said:

My number one rule of writing is: that the reader should never have to ask "why am I being told this?". However, I had to ask that question a lot while I was reading the paper. That's because I wasn't told what to expect up front. Instead, the style was "here's an observation; here's what it means". This sounds good on paper, but it means I have to absorb all sorts of information in isolation, and then put it together. There's a simple fix to that: give us the whole story at the beginning. We do get a pretty good summary, but not until lines 316-9:

"In summary, our model suggests that rare but strong and common but weak connections play different roles in the propagation of activity: the former promotes reliable responses to single spikes, while the latter amplify spontaneous network activity and drive recurrent inhibition, effectively modulating the reliability of those responses."

It would help a huge amount to get a summary like that -- but possibly expanded, because that's only part of the story – upfront. That way, for each of the various manipulations you made -- and there were a lot of them! -- it would have been easy to tell why. As it was, for most of them I had a hard time figuring that out, and I ended up getting pretty lost.

For what it's worth, my take on your results is as follows. As you point out on lines 102-4 "each model excitatory neuron connects to other neurons with a majority of weak synapses and about two connections sufficiently strong to bring the postsynaptic neuron from rest to near firing threshold". This implies a rapid growth in the number of spikes (by a factor of 2 per relevant timestep), with saturation caused by inhibition. This is an intrinsic feature of E-I networks (London et al. (your ref 2) showed this in rat barrel cortex). But there are two differences in the turtle cortex relative to the mammalian cortex: 1) about two connections from each excitatory neuron are strong enough so that a single presynaptic spike can trigger a postsynaptic spike, and 2) the firing rate was very low (about 0.1 Hz). The low firing rate is important; as it increased, repeatability dropped, especially for inhibitory neurons (Figure 2F). So maybe we should think of the weak connectivity as controlling the level of noise.

I'm not 100% this is correct, but it is what I extracted!

Of course, my rule isn't everybody's rule, so the extent to which you implement this is up to you. But in my view, the easier a paper is to read, the more impact it has.

Besides that, we have lots of comments, mainly about clarity and figures. They're more or less collated from the three reviewers, so they're not necessarily in a totally sensible order, although we did try. To reduce the trend toward longer and longer replies to reviewers, you do not need to reply to all of these. We'll leave it to your judgment which ones you do reply to. Maybe just the substantive ones you disagree with? They're all pretty minor, so as far as we're concerned you can just implement them (or at least the ones you agree with), and we'll be happy.

1. In Figure 1A, you should be clear about what the percentages mean. We _think_ they refer to connection probabilities, but that's not mentioned in the figure caption. Under that assumption, the connectivity (per neuron) is as follows:

E-E: 93,000 x 0.14 = 13,020

E-I: 7,000 x 0.46 = 3,220

I-E: 93,000 x 0.49 = 45,570

I-I: 7,000 x 0.26 = 1,820

These connectivity numbers should be in the paper since they're relevant. And 45,570 connections per neuron seems high -- is that consistent with experiments? Or are we doing something wrong?

2. Figure 1D: a log scale would, we think, make the figure easier to read.

3. Figure 1H and I: we're guessing blue and red are E and I, respectively (since that was the color coding for the triangles in panel A). But to avoid any possibility of confusion, this should be stated in the figure caption (and/or on the plots).

4. Line 168-9: "In each simulation, we caused the trigger neuron to fire 100 action potentials at long, regular intervals". We suggest that you tell us the interval (which, from Methods, was 400 ms). We wondered what "long, regular intervals" meant when we read that.

5. You use a Poisson process as a null model. Since E-E networks tend to oscillate, we believe (although we're not 100% sure), that a Poisson process will underestimate variability. You might want to address this (assuming it's relevant, which we're not sure it is).

6. In Figure 2C, what's the y-axis? Do slight displacements indicate different spikes? This should be clear.

7. It would be really nice to show spike rasters after a trigger spike. Presumably, they won't show much of anything, but it would be important to know that -- it's possible that one can see a slight increase in firing rate.

8. Please define normalized entropy (line 177) in the main text, at least qualitatively. And in Methods, it should be defined quantitatively (currently the reader is referred to a paper).

9. We don't understand the left panel in Figure 2E.

10. Lines 257-60: "Interestingly, excitatory-to-inhibitory spike transfers are consistently shorter than their excitatory-to-excitatory counterparts, even at higher firing rates (Figure 3B inset), possibly reflecting the more depolarized state of inhibitory neurons (Figure 1H right)."

Did you mean Figure 1I, not Figure 1H?

11. It would be nice to expand on the implications of Figure 3E. If we understand things correctly (a big if), you're showing the connections between any two neurons in which the postsynaptic one fired within 100 ms of the presynaptic one. Is that correct? If so, it means there are a lot of random coincidences -- that could even happen for un-connected neurons. Which makes it hard for us to interpret what the plot means.

12. line 475: "(network and colors as in Figure 4A)". We couldn't figure out all the colors from Figure 4A.

13. Figures 6B and 6D seem inconsistent: Figure 6B shows that a&b together generate very few followers, whereas Figure 6D shows that a&b together generate a lot of followers. What are we missing?

14. lines 636-8: "The response to simultaneous activation of multiple triggers in our model suggests that sequences operate under excitatory/inhibitory balance, where local inhibition cancels excitatory signals (5) (Figure 6D, H)."

Why do Figures 6D and 6H imply that sentence? More explanation would be helpful.

15. In Methods, please include equations. At least somebody (including one of us) would want to know what they are, and the reader shouldn't have to reproduce them from the explanations (especially since the definition of the exponential integrate and fire neuron probably isn't standard). Especially important is the average number of connections/neurons.

16. In table 1 it says that the synaptic conductance time constant is 1.103681 ms. Is it really that short? That seems strange, given the long membrane time constant. And why so many significant figures?

17. The result that strong sparse connections support sequential network activity is not particularly surprising. Perhaps more emphasis could be placed on the result that the weak, dense part of the network is necessary for supporting flexible sequential activation. Could a figure be added that shows the ideal ratio or range of ratios of strong to weak connections? Perhaps this is in the results already and just needs to be brought to the foreground.

18. The matching to the data from the turtle cortex is an excellent foundation for this work and grounds the model. Still, it might be nice to know how the results change as these parameters move around. In particular, it would be nice to know which aspects of the turtle's visual cortical network and cellular properties are necessary and sufficient parameters for the observed reliable sequence generation. All this is optional, so use your best judgment as to whether you want to include any of it. And some of it might simply be a point for the Results or Discussion.

a. If the ratio of E/I in the network is changed, do the results hold?

b. Are there other parameter changes that substantively affect the results? It seems like single-cell adaptation could be an important factor in pattern generation in the network.

c. The connection pattern in the turtle cortex might also be critical for these results. This isn't modeled explicitly in this work, but it could be an important feature for the experimental results that ground the paper. Does turtle cortex "look like" rodent cortex, or are some of the connections sparser, or do they fall off spatially faster or slower? It would be good to see a discussion of this in the paper.

d. In the model, connections are random but have a log-normal distribution. How does changing this affect the results and how well does that fit rodent cortical data?

19. The Results/Discussion seem to be missing a stronger take on what this kind of patterned activity might be useful for. A concrete example of a downstream computation that relies on the reliable combinatorial activation of sub-network sequences would be useful.

20. The gating results seem very exciting! It might be nice to highlight connections to a recent explosion in ML papers on gating and putting that part of the work more front and center in the abstract.

21. Line 183: "the number of excitatory followers far exceeds the number of inhibitory followers". This seems obvious in a network with 93% excitatory neurons. Are we missing something?

22. Line 187: Hz is a unit for oscillations and spiking activity is not oscillatory. Might we suggest spikes/s?

23. Figure 2E: The MEA square is an excellent example of the sort of thing that this reviewer cannot see when printed at the intended size. Please have mercy on older eyes.

24. Line 250-254: We struggled a bit to understand the concept of spike transfers. It seems like this is any link in any sequence where the presynaptic neuron is excitatory. Could you expand this explanation, please?

25. Line 265: "very few motifs lead to the activation of excitatory neurons". This confused us because in Line 183 it says "the number of excitatory followers far exceeds the number of inhibitory followers". We are clearly missing something important; please clarify.

26. Line 305: How strong do the connections have to be? We're guessing strong enough so a single presynaptic spike causes a postsynaptic spike, but this should be stated.

27. Line 316-319: We feel that the role for strong connections is more clearly demonstrated than the role for weak connections. Obviously, if there are only a very few strong connections then the neurons will have a lower mean membrane potential and will be less responsive to spiking input. Is it that simple, or is there more to it?

28. Figure 3H: We lack the visual acuity to interpret this plot. Perhaps an alternative representation would be clearer?

29. Line 366: two "due to"s in this sentence.

30. Figure 4E-G: there are numbers on these plots that we definitely can't read, and the connectivity in 4G is not only tiny but also a very pale grey in places.

31. Figure 4E, F: this is a measured frequency rather than a probability, right?

32. Line 618: landmark -> hallmark.

33. Line 651: it seems to us that your sequence structures have got a lot in common with those reported in your ref 34 (Polychronous groups, Izhikevich), which also depends on very strong synapses. Can you expand this section with some comparison to that study?

34. Line 731: "may not be linked to behavior". Well, it's ex vivo, so we guess certainly not linked to behavior. Perhaps you can rephrase to make your meaning clearer?

35. Line 818: "variable number of connections". It would be nice to know the statistics of this and how it compares with biology

36. Line 822: Nest -> NEST. (And we appreciate you stating and citing the version used!)
