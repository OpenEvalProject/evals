# Peer review - Round 1

Editors:
- Peter Latham, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66526.sa0](https://doi.org/10.7554/eLife.66526.sa0)

The natural gradient has a long and rich history in machine learning. Here, the authors derive a biologically plausible implementation of natural-gradient-based plasticity for spiking neurons, which renders learning invariant under dendritic transformations. This new synaptic learning rule makes several very interesting experimental predictions with respect to the interplay of homo- and heterosynaptic plasticity, and with regard to the scaling of plasticity by the presynaptic variance.


---

# Peer review - Round 1

Editors:
- Peter Latham, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66526.sa1](https://doi.org/10.7554/eLife.66526.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Natural-gradient learning for spiking neurons" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and John Huguenard as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

This paper derives a natural gradient learning rule for a spiking neuron in a supervised setting. Unlike conventional gradients in Euclidean space, the natural gradient is invariant under reparameterization, thus achieving fast convergence regardless of the position of synaptic contacts on the dendritic tree. The authors relate their rule to experimentally observed properties of synaptic plasticity, such as heterosynaptic regularization. We're not aware of any other work that applied natural gradient to a spiking neuron in a formal way, and we believe it is an important contribution.

That said, we do have several comments. All are relatively minor (many have to do with presentation), and, we hope, easy to address. Because this is a combination of three reviews, they're not exactly in order of appearance in the manuscript. But hopefully not too far off.

1. We're slightly concerned with the fact that the weight update scales inversely with the firing rate. First, presumably for small enough firing rates something in the derivation breaks down. Second, this makes a very strong prediction. The only data we know of that relates to this is in Aitchison and Latham, 2014 (now published in Nature Neuroscience vol 24, pgs 565-571, 2021), where they showed, in one experiment, that learning rate scales as 1/sqrt{r} for moderate firing rates (greater than about 1 Hz), and saturates at small firing rates. This is one experiment, so doesn't rule out the theory here, but these points should be discussed.

2. The link to biology is often very cursory. References to experiments are often in the form 'so and so found something a bit similar'. Wherever possible, you should try to make precision comparisons to experiments. And on page 10 you say that the weight dependent heterosynaptic terms explains the central weight distributions found in cortex. However, the weight dependent heterosynaptic term is just one term out of three, and the other terms are not weight-dependent. If you want to argue this, you should be more rigorous (and in particular take into account all three terms).

3. The conclusion of the Zenke and Gerstner paper is, we believe, incorrect: A learning rule with an intrinsic weight dependence, such as Oja's rule, does not need homeostasis. This clearly doesn't affect any of your analysis, but it does mean that the statement "…… (Zenke and Gerstner, 2017), where it was shown that pairing Hebbian terms with heterosynaptic and homeostatic plasticity is crucial for stability" is, we believe, not true.

4. Figure 1B is pretty incomprehensible, and it doesn't help that the equations are small and gray, making them hard to read. We would suggest dropping it, especially since the point is made very well in the text.

Along the same lines (but much later), in Sec. ‘The naive Euclidean gradient is not parametrization-invariant’ we don't see any contradiction between Equations 26 and Equation 27; they are just two different definitions of Δ ws. It might be an inconsistency, but not a contradiction.

5. Figure 3: Considering that several approximations were made in the derivation of the learning rule (even for Equation 7), learning performance should be evaluated a bit more carefully. In particular:

a. Please plot the distance between student weights and teacher weights, on the same timescale as in Figure 3F (either in Euclidean space or in Fisher metric space).

b. Please plot performance versus learning rate, so we can get a sense of robustness. "Performance" could either be asymptotic loss or time to achieve a particular loss. Also, can you speculate how the learning rate of a neuron can be optimized?

c. What's the target output firing rate? It might have been stated somewhere, but we missed it. It would be nice if it were in the figure caption, like it is in Figure 4.

d. In Figure 3, n=2 and n=100 are both used. It should be clear which panel is which.

e. Panels B and C: what's the timescale? There's only one labeled time point (0.1), so it's impossible to tell. And how many trials did it take to learn? We would have expected considerable learning during 2500 trials.

f. The direction of the gradient depends on whether or not there's a spike on the teacher neuron. Which means the path in weight space is noisy, and the weights should not converge -- instead, they should exhibit fluctuations forever. But the trajectories in D and F were very smoothed. Is that because they're averaged over a large number of trials? Or was some extra processing done? Please explain.

6. Figure 4:

a. Can you reproduce experimental results on dendritic position dependent plasticity (eg. Letzkus JJ, Kampa BM, Stuart GJ, 2006; Sjöström PJ, Häusser M, 2006). These experimental results are inconsistent with vanilla Euclidean gradient; hence they would provide support for biological relevance of the proposed learning rule.

b. "the distance from soma was varied between 1 microns to 10 microns". This seems small; the characteristic length of dendritic decay is in order of 100 microns (Williams and Stuart, 2002).

7. Figure 5: Here, you compared three neurons each receiving single excitatory input with different input characteristics. Do you expect the same result to be true for a single neuron receiving three excitatory inputs? We're curious about it because that's a more relevant scenario. Some casual remarks would be helpful.

8. Figure 7:

a. We're somewhat confused that you you can distinguish between the three forms of plasticity in Equations 11-13, at least for the stimulated synapses. Don't all three forms contribute at once? But in panel B you say, "Weight change of stimulated weights (homosynaptic)". And in panel C, you should have seen homosynaptic plasticity (see next comment). Could you explain how you can single out one form of plasticity? Or else drop the comment. Or maybe we misunderstood?

b. In the legend of Figure 7, it is mentioned that the rest of synapses received 0.01Hz input, but in Sec. ‘Comparison of homo- and heterosynaptic plasticity’, that information is omitted. Did you actually stimulate these synapses? If so, we would have expected a big jump in synaptic weight when there was a spike, and in 60 s there should have been 3 spikes (0.01x60x5).

c. 7G: A should be S?

d. Equation 13 is out of the blue. Could you tell us where this comes from? And from the bottom of page 10, we have

"…… is roughly a linear function of the membrane potential (more specifically, its deviation with respect to its baseline)."

What does baseline refer to? We didn't see anything about baseline in Equation 25, which is where Equation 13 comes from.

e. Could you tell us how the colors in panels B-D were computed? Presumably some assumptions were made. If so, what were they?

9. Equation 4: we believe that the right hand side should not have a minus sign. More importantly, we should be told that Y* consists of a sum of δ-functions; the statement "Here, Y* denotes a teacher spike train sampled from p*" was unhelpful. It's also important to tell us exactly how Y* is sampled, which is, presumably from

P(spike from Y* \in [t, t+dt]) = phi(sumj w*j xjε) dt.

If that's not correct, then we're thoroughly confused.

10. The second paragraph on page 4 makes some strong statements, and we're not sure all of them are true. For instance,

"Convergence of learning is therefore harmed by the slow adaptation of distal synapses compared to equally important proximal counterparts."

Presumably, "adaptation" means "learning". If so, why is adaptation necessarily slow at distal synapses? That would seem to depend on the biological learning rule. If not, what does "adaptation" mean in this context?

And,

"With the multiplicative USP term xε in Equation 4 being the only manifestation of presynaptic activity, there is no mechanism by which to take into account input variability, which can, in turn, also impede learning."

This is a bit out of the blue. Why should input variability affect learning? So far the authors have not said anything about this. It comes up later, but right now it's pretty obscure.

11. Last paragraph on page 4: the motivation for using the Fisher information matrix is a bit obscure. (For instance, what does "it is generally the unique metric that remains invariant under sufficient statistics" mean?) We strongly suspect that we won't be only ones who are lost. So it would be good to motivate it in plain language. And in particular, it would be nice to show, at the very least, that using the Fisher information matrix automatically makes the learning rule invariant with respect to a change of variables. (Which is pretty easy to do.)

Along the same lines, after Equation 9 you say

"This represents an unmediated reflection of the philosophy of natural gradient descent, which finds the steepest path for a small change in output, rather than in the numeric value of some parameter."

This has been the theme all along, but was it ever shown? As far as we can tell, you just used the inverse of the Fisher information matrix. Is it obvious that it has the above effect?

12. It would be extremely useful to write down log pw in the main text.

13. The quantities in Equation 7 should be defined immediately -- right now we have to read down half a page to figure out what they are. And you should tell us immediately how γu and γw could be computed locally.

14. In the section "Natural gradient speeds up learning", please tell us exactly what the cost function is (which, presumably, means telling us w* and the filters you use to convert incoming spike trains to x). And it would be good if the firing rates were given in the main text, so one doesn't have to look at the figure.

15. Because of the factor of phi'(V)/phi(V) in Equations 7 and 8, the effective scaling in Equation 9 is, approximately, 1/phi'(V). This doesn't change the point that a shallow slope implies a high learning rate, but thing's aren't quite as bad as Equation 9 implies. This seems worth mentioning.

16. You mention, on the top of page 8, "that the absence of dendritic democracy does not contradict the presence of democratic plasticity". It seems worth mentioning, just for completeness, that dendritic democracy can be achieved without democratic plasticity. In particular, as far as we can tell, the Euclidean gradient is also consistent with dendritic democracy, although convergence to the democratic state might be slower that for the natural gradient.

17. p. 10 "In comparison, input from weak synapses only has……" We couldn't get the logic of this and the following sentences. This non-trivial claim is not explicitly tested in the subsequent paragraph, but reappears in the discussion. You should expand on it, or remove it.

18. p22: "The integral formulas follow from……". It would help if you referred to Equations 20 and 21 (in Sec. ‘Neuron model’) here. We were confused by the sudden appearance of εo and cε. Also, you should mention how they are related to dt.

19. It is somewhat confusing that you set up the problem about dendritic distance, but then first address, in Figure 3, the role of firing rate, before showing the solution to dendritic plasticity. Perhaps starting with Figure 4, contrasting standard gradients to natural gradients would help.

20. Page 7/8, you say "neurons are not symmetrical geometric objects". You should make it clear what this means (presumably it means that they have dendrites, and, therefore, some weights are attenuated). In addition, it's not clear that not being a symmetrical geometric objects implies a non-isotropic cost landscapes, since how isotropic the cost landscape is depends on the input and cost function as well as the attenuation in the dendrites. In principle they former could cancel the latter, producing an isotropic cost landscapes even with strongly attenuating neurons. It seems best to drop this point.

21. A number of studies have recently emphasized that in large networks most machine learning problems have highly degenerate minima (e.g. Belkin et al. et al. PNAS). Does the algorithm generalize to such situations? Your answer may be "we don't know". But whatever the answer, it would be worth mentioning in the paper.

22. Page 7, last paragraph: should the reference to Figure 5 be to Figure 4?

23. The abundance of superscripts, subscripts and decorations in the variables throughout the manuscript make it very hard to read. We would suggest simplifying notation as much as possible. In particular:

a. The superscript on the gradient operator doesn't help, as it requires extra memorization -- which is hard because it's not standard. You would be much better off putting the superscript on the cost function, and not redefining the gradient. It's especially confusing in Equation 6, since at first glance the superscript n means take n derivatives.

b. There are two w's: wd and ws. Except sometimes there's a w without a superscript. It should always be clear which w you're referring to.

c. The notation in Equation 7 may make for easier reading, but it makes it very difficult to figure out what's actually going on, especially since there's no easy way to tell vectors from scalars. We would strongly recommend using components (dwi/dt = ……). It would make it much more clear, with very little cost.

24. Along the same line, the phrase "unweighted synaptic potential (USP) train" is pretty distracting. We would strongly suggest dropping it, since everybody agrees what a spike train is. Plus, we searched, and "weighted dendritic potentials" was used only once, in the sentence before unweighted synaptic potentials were defined. So "unweighted" seems a bit redundant.

25. Important equations should, in our opinion, be displayed. That's because readers (OK, some of these readers) always go back and search for important quantities, and they're easier to see if displayed. (This was triggered by the expression for V, a few lines up from Equation 2.)

26. The setup should be made clear up front: the neuron is receiving a teacher spike train, yt, and using those spike trains to update its synapses. The statement before Equation 3, "Assuming that the neuron strives to reproduce a target firing distribution p*(y|x)" was not helpful (I couldn't really make sense of it, so I kind of ignored it). And so it took me forever to figure out what was going on.

27. Along the same lines, wouldn't it make sense to just say the neuron is trying to maximize the log probability of the teacher spikes? It gives the same cost function, and it's a lot less obscure than saying the cost function is the KL distance. Clearly a matter of taste, but log probability seems more sensible.

28. On the top of page 9, it says that learning rates are inversely correlated to the variance of σ2(xε). It needs to be clear why the equations say that; right now it's pretty much out of the blue.

29. End of discussion (page 12): "error-correcting plasticity rule". Why is it error correcting?

30. Very end of discussion:

"Explicitly and exactly applying natural gradient at the network level does not appear biologically feasible due to the existence of cross-unit terms in the Fisher information matrix G. However, methods such as the unit-wise natural-gradient approach (Ollivier, 2015) could be employed to approximate the natural gradient using a block-diagonal form of G. For spiking networks, this would reduce global natural-gradient descent to our local rule for single neurons."

We didn't understand that -- it should be unpacked.

31. Given that this is eLife, and there's no page limit, we would strongly urge you to get rid of the Appendix and put all the analysis in Methods. We suspect anybody willing to read Methods will want to see the algebra in the Appendix. In any case, all relevant quantities (e.g., g1, ……) should be in Methods; the reader shouldn't have to hunt them down in what will potentially be another document. And certainly, the gradient, which is central to the whole endeavor, should be in Methods. As should Equation S18, so that the reader knows where G(w) comes from.

32. There's a much easier derivation of G(w), Equation 31:

int dx exp(h dot t) N(x; mu, Σ) f(a dot x)

is easy to evaluate (here x is a vector and N(x; mu, Σ) is a Gaussian with mean mu and covariance Σ). Take two derivatives, and, voila, you have.. Same answer, but easier on the reader.

In addition, the derivation of its inverse can be more concise. G(w) is a sum of a diagonal matrix and a rank-2 modulation. Denoting

V = (r w') and C = [[c1 e2, c2 e], [c2 e, c3]],

we may write

G(w) = c1 Σ + V C VT.

Applying the Woodbury identity,

G-1(w) = Σ-1/c1 – V' (C-1 + V Σ-1 VT)-1 V'T,

where

V' = (r'/e w).

Thus,

g = [[g1 g3], [g2 g4]]

is given as

g = – (C-1 + V Σ-1 VT) -1.

33. Aren't Equations S12-13 a repeat of arguments made above, on the same page? Or is this something new? Either way, it should be clear (and if it's a repeat, maybe it can be dropped).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Natural-gradient learning for spiking neurons" for further consideration by eLife. Your revised article has been evaluated by John Huguenard (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The good news: The reviewers are quite positive, and there are no major concerns.

The bad news: Reviewer 1 has many comments requiring clarification. But almost all should be relatively straightforward to address in a timely way.

Reviewer #1:

The manuscript is much improved, although it's still a bit hard to read. Some of which we think could be easily fixed. Specific comments follow.

1. p 1: "It certainly could be the case that evolution has favored one particular parametrization over all others during its gradual tuning of synaptic plasticity, but this would necessarily imply sub-optimal convergence for all but a narrow set of neuron morphologies and connectome configurations."

We found this confusing, since parametrization and learning rules are not directly coupled. Did you mean "evolution has favored one particular parametrization over all others, and updates weights using Euclidean gradient descent ……"?

2. One more attempt to kill USP: why not call xε filtered spike trains, since that's what they are? "Unweighted synaptic potential" is completely unfamiliar, and with a paper this complicated, that's the last thing one needs -- every single time we read that phrase, we had to mentally translate it to filtered spike trains.

3. Technically, xiε should depend on distance to the soma: because of dendritic filtering, the farther a psp travels along a dendrite the more it spreads out (in time). You should mention this, and speculate on whether it will make much difference to your analysis. It seems like it might, since cε scales with the timescale of the psp.

4. In both places where you mention spikes (xi, above Equation 4 and Y*, above Equation 9) you should point out that they are a sum of δ functions. "Spikes" isn't so well defined in this field.

5. If you want anybody besides hard core theorists do understand what you're doing, you'll need to be explicit about what p* is: it's Equation 7 with phi replaced by phi*, the target firing rate as a function of voltage. We strongly suggest you do that. In particular, the description "a target firing distribution p*(y∣xε)" doesn't help much, since a firing rate distribution is usually a distribution over firing rates. What you mean, though, is that p* gives you the true probability of a spike in a time interval.

5. It would be very helpful, in Equation 9, to add

\approx dt[ (phi – phi*) – phi* log(phi/phi*) ]

(and point out that it's exact in the limit dt --> 0). Then Equation 10 is easy -- just say that phi* is replaced by Y*.

6. Starting in Equation 10, you switch to a weight without a superscript. We found this very confusing, since the learning rule you wrote down in Equation 10 is exactly the one for ws. We strongly suggest you never use w. But if there is a reason to do so, you should be crystal clear about what it is. As far as we could tell, this switch to w is completely unsignalled. So maybe it's a typo?

7. p 4: "which is likely to harm the convergence speed towards an optimal weight configuration."

The word "likely" is not all that convincing. Can you be a lot stronger? Are there relevant refs? Or you could point to the simulations in Figure 3.

8. p 4: "In the following, we therefore drop the index from the synaptic weights w to emphasize the parametrization-invariant nature of the natural gradient."

In fact, what's really going on is that you're deriving the natural gradient learning rule (Equation 13) with V given by

V = sumi f(wi) xiε

which is actually very confusing, since f was used previously to relate ws to wd (Equation 4). Is the f in Equation 14 the same as the one in Equation 4? If so, it should be wd on the right hand side of Equation 14. If not, you should use a different symbol for the function.

As you can see, your notation is confusing us. Our suggestion would be to always use superscripts s or d, and never use w by itself.

9. Figure 2:

"(A) During supervised learning, the error between the current and the target state is measured in terms of a cost function defined on the neuron's output space; in our case, this is the manifold formed by the neuronal output distributions p(y, x)."

What does "defined on the neuron's output space" mean? Doesn't the cost function depend only on the weights, since it's an average over the input-output function? Which is more or less what you say in the next sentence,

"As the output of a neuron is determined by the strength of incoming synapses, the cost C is an implicit function of the afferent weight vector w.!

Although we're not sure why you say "implicit" function; isn't it a very explicit function (see point 5 above).

"If, instead, we follow the gradient on the output manifold itself, it becomes independent of the underlying parametrization."

Since we don't know what the output manifold is (presumably the statistical manifold in panel A? not that that helps), this sentence doesn't make sense to us.

"In contrast, natural-gradient learning will locally correct for distortions arising from non-optimal parametrizations."

This is a highly nontrivial statement, and there's nothing in the manuscript so far that makes this obvious. I think a reference is needed here. Or point the reader to Figure 3 for an example?

10. Equation 13: You may not like components, but it would be extremely helpful to put them in Equation 13, or maybe add an equation with components to make it clear. There is a precedent; you use components in Equation 4. And let's face it, anybody who isn't mathematically competent will have been lost long ago, and anybody who is mathematically competent will want to be sure what's going on. And things are actually ambiguous, since it's really hard to tell what's a vector and what's a scalar. In particular, γu should be treated as a vector, even though it's not bold, so it's not immediately clear whether γs should also be treated as a vector. If nothing else, you should use γu {\bf 1}; that would help a little. Also, the convention these days when writing f(w) is for f not to be bold, but instead define it as a pointwise nonlinearity. You don't have to follow conventions, but it does make it easier on the reader.

The same comment applies to Equation 17.

11. In Equation 14, presumably ws on the left hand side should be bold? And why not use indices, as in Equation 4? Much more clear, and fewer symbols.

12. p 6, typo: "inactive inactive".

13. Two questions and one comment about Figure 3F. First, why don't the orange and blue lines start in the same place? Second, the blue line doesn't appear to be saturating. Can the Euclidean gradient do better than the natural gradient? If so, that's important to point out. But maybe it's not true, and is a by-product of your optimization method?

And the comment: presumably the DKL term on the y-axis has a factor of dt. That makes it pretty much impossible to interpret, since we don't know what dt is (probably it's somewhere, but it's not in an obvious place). We suggest removing the factor of dt, and making it clear that when phi is close to phi*, what's being plotted is <(phi-phi*)^2/2 phi*>. That will make the plot much easier to interpret.

14. p 8: "As a result, the effect of synaptic plasticity on the neuron's output is independent of the synapse location, since dendritic attenuation is precisely counterbalanced by weight update amplification."

Because of the term γw wd, this is true only if wd \propto 1/α(d). But, as you point out later, this doesn't have to be the case. So this statement needs to be modified. Maybe it's approximately true?

15. Figure 5, several comments:

In the equation in panel H, r should be in the numerator, not the denominator, and a factor of ε02 is missing. In addition, the term on the right hand side can be simplified:

σ2(xε) = r ε02/2(tau1 + tau2).

Also it would be a good idea to switch to taus and taum here rather than tau1 and tau2, to be consistent with Methods, and to not clash with the tau's in panels A-B.

And in panels A-B, presumably it should be tausi rather than taui?. Also, taum should be reported here.

It would make it a lot easier on the reader if you wrote down an equation for cε, which isn't so complicated: cε/ri = 2 (taum + taus)/ ε02 ri. Equation 19 is a natural place to do that.

Because of the other two terms in Equation 17, it's not true that "Natural-gradient learning scales inversely with input variance." It should be clear that this is approximate.

16. In Equation 19, it should be xiε on the left hand side, not xε.

17. p 10: "Furthermore, it is also consistent with data from Aitchison and Latham (2014) and Aitchison et al.et al. (2021), as well as with their observation of an inverse dependence on presynaptic firing rates, although our interpretation is different from theirs."

There is no justification for this statement: in Aitchison et al.et al. a plot of Δ w/w versus r showed 1/sqrt(r) scaling. That would be consistent with the theory in this paper only if the weight scales as 1/sqrt(r). It might, but without checking, you can't make that claim.

That data is weak, so the fact that you don't fit it is hardly the end of the world. However, what's more important is to point out that the theory here makes very different predictions that the theory in Aitchison et al.et al. That way, experimentalists will have something to do.

Finally, the inverse scaling with firing rate must eventually saturate, since there's a limit to how big weight changes can be. You should comment on this, if briefly.

18. Figure 7, we're pretty lost, for several reasons:

a. Because homosynaptic scales as 1/r, it's not possible to have unstimulated synapses (for which r=0); at least not with the current derivation. If you want to have unstimulated synapses, you need to show that it is indeed possible, by computing G when ri=0 for some of the i's.

b. From the bottom of page 27, γu \approx ε0 cε. Thus, the first two plasticity terms are

cε (xε/r – ε0).

Because = r ε0, these two terms approximately cancel. Which means everything should be driven by the last term, cw V f(w). This doesn't seem consistent with the explanation in Figure 7.

c. Because of the term cw V f(w), shouldn't there be a strong dependence on the unstimulated weights in panels B-D?

All this should be clarified.

19. p 13: "We further note an interesting property of our learning rule, which it inherits directly from the Fisher information metric that underlies natural gradient descent, namely invariance under sufficient statistics (Cencov, 1972)." What does "invariance under sufficient statistics" refer to?

20. p 13: "A further prediction that follows from our plasticity rule is the normalization of weight changes by the presynaptic variance. We would thus anticipate that increasing the jitter in presynaptic spike trains should reduce LTP in standard plasticity induction protocols."

Presumably this statement comes from the fact that the learning rate scales inversely with the variance of the filtered spike train. However, it's not clear that jittering spike trains increases the variance. What would definitely increase the variance, though, is temporal correlations. Maybe this could be swapped in for jittering? Either that, or explain why jittering increases variance. And also, it would be nice to refer the reader to the dependence of the learning rate on variance.

21. You should comment on where you think the teacher spike train comes from. Presumably it's delivered by PSPs at the soma, but those don't propagate back to synapses. How do you envision the teacher spike trains communicating with the synapses? Even if the answer is "we don't know", it's important to inform the reader -- this may simply be an avenue for future research.

22. In Equations 29 and 30, you should explain why you use \approx. Presumably because that's because you assumed a constant firing rate?

23. Equation 31: it would be extremely useful to point out that cε = 2(taum + taus)/ε02, along with a reference (or calculate it yourself somewhere).

24. After Equation 31, "Unless indicated otherwise, simulations were performed with a membrane time constant taum = 10 ms and a synaptic time constant τs = 3 ms. Hence, USPs had an amplitude of 60 mV".

Doesn't the amplitude of the USPs depend on ε0? And 60 mV seems pretty big. Is that a typo?

25. Equation 34: Missing parentheses around ΣUSP ws in the second term in parentheses.

26. Equation 24 and the line above it: should wi be wid? If not, you shouldn't use f, since that was used to translate somatic to dendritic amplitude.

27. Equation 115: Should it be Theta(V-theta)?

28. Equation 117 is identical to Equation 67. Did you mean to drop the term (phi')2/phi?

Also, (phi')2/phi = 1 when V > theta. But presumably it's equal to 0 when V < theta. If so, Equation 117 should be

G(w) = E(dt Theta(V-theta) x xT).

if that's correct, then the integrals I1-I3 do not reduce to the values given in Equations 118-120.

Reviewer #2:

The authors have done a good job in the revision.

A number of small suggestions remaining:

– Equation 13. Wouldn't it be easier to write this for a single component wi)˙=……

– Figure 3 shows temporal structure in the teacher signal but this is nowhere explained in the main text.

– Fig3D+E perhaps the axis or caption can indicate whether w1,2 is 10 or 50Hz.

– Figure 4A: Shouldn't the purple top solid curve (dendritic voltage) be taller than the solid orange curve?

– Fig5D+E+F might look better with the position of the y-axis left instead of right.
