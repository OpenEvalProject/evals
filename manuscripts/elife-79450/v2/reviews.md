# Peer review - Round 1

Editors:
- Paul Bays, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79450.sa0](https://doi.org/10.7554/eLife.79450.sa0)

This important study describes a model neural circuit that learns to optimally represent its inputs subject to an information capacity limit. This novel hypothesis provides a bridge between the theoretical frameworks of rate-distortion theory and neural population coding. Convincing evidence is presented that this model can account for a range of empirical phenomena in the visual working memory literature.


---

# Peer review - Round 1

Editors:
- Paul Bays, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79450.sa1](https://doi.org/10.7554/eLife.79450.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Rate-distortion theory of neural coding and its implications for working memory" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Paul Bays as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Joshua Gold as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Expand and clarify the description of the model and how and why it makes the highlighted predictions, to fill in missing steps and make it more comprehensible to readers from a range of backgrounds.

2) Explain to what extent the neural model and its predictions are compatible with neurophysiological observations of stable tuning functions, and the recurrent excitation believed to maintain activity during a delay.

3) Expand the manuscript to better situate the current model in relation to other mechanistic WM models in the literature, and perform quantitative fitting to more concretely evaluate the model's ability to reproduce empirical data. While formal model comparison (e.g. with AIC) may not be necessary, it is important to evaluate the present model's match to data against other models' to understand its relative strengths and weaknesses. As the model is designed to implement an information capacity limit, its ability to reproduce set size effects (on error variability and error distribution) seems worthy of particular attention.

4) Consider and develop the implications of the model's basic principles (e.g. the idea that periods when WM requirement is low can be traded for a boost in information capacity at a later time) for a broader range of WM tasks and observations. This doesn't have to be quantitative fitting but needs to counter the argument that the empirical data currently presented has been selected to fit the model.

Reviewer #1 (Recommendations for the authors):

Some more technical points:

The "simple update rule" of Equation 14 requires knowledge of the information rate R (Equation 13) – is there a plausible method by which this could be computed in the circuit?

WTA, as utilized in the model, is generally a suboptimal decoding method – would predictions change for population vector or ML decoding?

Cosine tuning curves for input neurons lead to von Mises tuning curves for the output neurons – if that's correct it might be worth spelling out as it is the assumed tuning in previous population models of WM.

Excess kurtosis in error distributions has been an important point of debate in WM modelling – it appears to be present in the simulated data, but how does it arise in the model?

How are the smooth "Data" distribution plots generated? Smoothing may be misleading if the shape of the distribution is a question of interest, as it is for set size effects. The smoothing does not appear to take into account the circularity of the response space, based on what happens at π and -pi.

The description of how model predictions are generated needs to be substantially expanded, to explain step-by-step how the data that appears in the "Simulation" panels were produced. How were estimates obtained? How many repetitions/simulated trials were used (the plots are quite noisy)? To what extent were the simulated trials matched to the real ones, in terms of individual stimuli, etc?

What does it mean for the model that the parameter C had to be made ten times smaller for one experiment than the others?

"Spikes contributed to intrinsic synaptic plasticity for 10 timesteps" – what is the implication of this? Is it plausible? Do the results depend on it?

The section on primate data includes results of a model comparison – the methods need to be explained.

Figure 6A axis-label "Relative color of previous trial" – what does this refer to when the set size is three?

The scales in Figure 3B and D don't match.

The variable u_i is in several places (legend of Figure 1, before Equation 15, maybe others) described as the membrane potential instead of excitatory input (which I think is the intended meaning).

Legend of Figure 8B refers to an orientation tuning curve, but I don't believe the task involved oriented stimuli: angular location is probably what is intended.

Figure 1 and elsewhere – using K to indicate set size is going to be very confusing for WM researchers as it has long been used to refer to WM capacity. SS or even N would be preferable.

Reviewer #2 (Recommendations for the authors):

Equation (2): More explanation is needed when moving from the constrained optimization problem to the unconstrained optimization by forming a Lagrangian, especially for some readers of eLife. Add a couple of sentences justifying this step here.

p.3: OK, I'm going to be a bit nitpicky here. "The rate-distortion function is monotonically decreasing" – I'm not sure you can be sure of this. Increasing the capacity could yield no decrease in distortion in some cases (like if you're already at D=0), so technically you should say "monotonically non-increasing" I think. You also say this a couple of paragraphs later to justify \β being decreased, but I think you can only ensure it's non-increasing, I think, but maybe you can convince me otherwise.

Equation (4): Are you just integrating the ODE defined by (2) and (3) to get this result? If so, say that, or give a bit more info on how you arrive at this formula.

"We assume that inhibition is strong enough such that only one neuron in the population will be active within an infinitesimally small time window." – I think this statement is unnecessary. As long as you make a time window small enough, the probability of co-occurring spikes in a window will be zero.

p.6: When you talk about recurrent models, I don't really see any semblance of recurrence in your models. They're just feedforward, right? The weights w_i seem to really just to be inputs. r_i does not feedback into all the other u_j's. Admittedly, this would be a trickier optimization problem to solve using a simple learning rule. Do you have an idea how you would do this if you introduced recurrence into the formulation Equation. (10) and (11)? You could punt this to the Discussion or get into more detail here, but not worrying enough about the mechanism of maintenance of the population spiking means you have to artificially dial down the capacity as the delay time is increased when you get to the "Timing" section on p.9.

Figure 2: You're qualitatively replicating the data, but admittedly missing some details. Variance scales up slower in the model and kurtosis drops off slower. Why? Is this just a case of people satisficing? Also, I think if you follow the analysis in the supplement of Sims et al. (2012), you should be able to get a good analytic approximation of 2D assuming an unbounded (rather than periodic) domain. Even if you place the problem on a periodic domain, I think you can solve the rate-distortion problem by hand to find the correctly parameterized von Mises distribution.

"Increasing the intertrial interval reduces the information rate, since no stimuli are being communicated during that time period, and can therefore compensate for longer retention intervals." – I don't agree with this interpretation. I would think that longer ITIs might lead to less serial bias. Mechanistically, I don't see what else would disrupt persistent activity in a neural circuit as a function of ITI.

p.10: Neural firing rate activity from the previous trial seems an unlikely candidate for the primary mechanism for serial dependence given the persistent activity is typically gone between trials (see Barbosa et al. 2020) – e.g., short-term plasticity or something else seems more likely. I know you're aiming at a parsimonious model, but I think this point warrants discussion.

For all your Simulation/Data comparisons, it's not clear exactly how you chose model parameters. Did you do something systematic to try and best replicate the trends in data? Did you pick an arbitrary \β and stick with this throughout? More and clearer information about this would be helpful.

Reviewer #3 (Recommendations for the authors):

It would be informative to formally compare the current model against alternatives [as one example, Matthey, L., Bays, P. M., and Dayan, P. (2015). A probabilistic palimpsest model of visual short-term memory. PLoS computational biology, 11(1), e1004003.]. As it stands, I am not sure if the model is "yet another model" in a fairly large space, or whether it makes unique predictions or outperforms (or perhaps underperforms) existing models.

Absent formal model comparisons, an extended discussion of the current model's strengths, and especially weaknesses, would greatly improve the manuscript.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Rate-distortion theory of neural coding and its implications for working memory" for further consideration by eLife. Your revised article has been evaluated by Joshua Gold (Senior Editor) and a Reviewing Editor.

The manuscript has been improved, and two out of three reviewers are now satisfied, but there are a small number of remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

This revision resolves a number of previous concerns, and the clarity of presentation of the model is much improved. There are two issues remaining that I hope can be dealt with relatively straightforwardly:

1. The revision makes clearer where the empirical data, to which the models are compared and fit, comes from, including that the data in Figure 2A corresponds to Exp 1 in ref [15]. However, if that is the case, why is the data from set size 1 missing? Was it also omitted from model fitting? Please remedy this, as predicting recall performance with a single item is pretty crucial for a working memory model.

2. The problems I noted with data smoothing haven't been dealt with. I checked the plots in the original papers corresponding to Figures2 and 3, and its clear the smoothing is strongly distorting the distribution shapes (which form a key part of the evidence the models are intended to reproduce). Is there a reason you can't just plot histograms, like the original papers did for the data?
