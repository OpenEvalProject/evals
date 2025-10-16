# Peer review - Round 1

Editors:
- Mimi Liljeholm, https://ror.org/04gyf1771 University of California, Irvine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85107.sa0](https://doi.org/10.7554/eLife.85107.sa0)

This paper provides a formal analysis of the normative advantage of the opponent pathways of the basal ganglia circuit for cost-benefit decision-making. Specifically, a previously introduced Hebbian nonlinearity is combined with reward-based DA modulation to optimize exploration across lean and rich environments, and across a range of pharmacological and contextual manipulations. The scope of the model, its biological plausibility, and its normative and descriptive aspects are likely to have a significant impact.


---

# Peer review - Round 1

Editors:
- Mimi Liljeholm, https://ror.org/04gyf1771 University of California, Irvine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85107.sa1](https://doi.org/10.7554/eLife.85107.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "On the normative advantages of dopamine and striatal opponency for learning and choice" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Mimi Liljeholm as the Reviewing Editor and Reviewer #, and the evaluation has been overseen by a Senior Editor.

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

Specifically, concerns about the stability and adaptivity of the model, based on actual simulations, were judged serious enough to preclude an invitation to revise. However, if you feel confident that you can compellingly address all issues raised by the reviewers, and the matter of environmental dynamics in particular, we would be happy to consider a resubmission.

Reviewer #1 (Recommendations for the authors):

The authors aim to demonstrate the normative advantage of opponent basal ganglia pathways, using dynamic dopamine (DA) modulation by environmental reward statistics. The finding that well-known neurophysiological and psychopharmacological mechanisms yield rational decision-making in ecologically plausible environments is a major strength of the paper. The methods are rigorous, and the advantage of the model is reliable across a range of parameters and paradigms. More could be done to explain the optimality of certain model predictions, to map the correspondence between model predictions and animal behavior, and to articulate the conceptual relationship between relevant constructs, such as exploration, discrimination, and risk-taking. Nevertheless, the scope of the model, its biological plausibility, and its normative and descriptive aspects suggest that it may have a significant impact.

1. More could be done to detail the, sometimes counterintuitive, optimality of certain model predictions. For example, while it is straightforward that you need to explore to discover better options, the need to sample sub-optimal options so that you know to avoid them makes less sense: if you don't sample them, you are already avoiding them, and when you do choose them, you learn the values – why is it adventitious to do the sampling early in the process as opposed to later? Another example is the claimed optimality of avoiding gambles in lean environments, despite the expected value of the gamble being greater than that of the ST.

2. It would be helpful if there was a description, early in the Introduction, and perhaps again in the Discussion, of how the relevant constructs (i.e., exploration, discrimination, and risk-taking), are related conceptually – note that exploration can be characterized as risk-taking and that the decision to gamble may reflect either exploration or value-based discrimination.

3. In Figure 10a, it is unclear why L-DOPA does not boost G weights and reduce N weights, yielding a greater probability of gambling, on loss trials as it does on gain trials?

4. In Equations 1-3, why not show the updating of Act values, or, if identical to V(a), be explicit about that. Also, Equation 14 is referred to as a prediction error in the text, but the notation indicates an action value [i.e., V(a)].

5. It is argued that OpAL* eliminates the need for a priori knowledge about environmental reward statistics, but DA-modulation depends on confident estimates of the values (i.e., reward probabilities) of all available actions – the implications of this reliance on reward estimates seem under-explored in simulations.

6. It is unclear from the curves in Figure 7 whether the models reach equilibrium by 100 trials. Please show asymptotic performance.

7. Why use only forced-choice simulations? It is hard to imagine a real-world scenario in which "no action" is not an alternative. Failure to include such an option detracts from the ecological validity of the experiments.

Reviewer #2 (Recommendations for the authors):

I really enjoyed this paper that significantly advance our understanding of the basal ganglia circuit. I have some suggestions for additional simulations that can allow establishing to which extent previous findings in reinforcement learning can be accounted for by the OpAL(*) models.

A key concept of the model is its sensitivity to environmental richness (i.e., whether the agent is in a lean or in a rich environment). The concept behind the "rho" variable is very closely related to that of "state value" or "reference point" as it has been applied to reinforcement learning and valuation since Palminteri et al. (2015). The key demonstration of a crucial role of overall "environmental richness" in learning and valuation came from a task, which, explicitly coupling features of the Frank (2004) and Pessiglione (2006) tasks, showed that transfer learning performance is highly context-dependent (see Palminteri and Lebreton, 2021; Daw and Hunter, 2021 for review of these results). My question here is whether or not the OpAL(*) models are sufficient to generate such context-dependent preferences. Does this (very robust) behavioral effect naturally emerge from the model? Or do we need to specify an additional process to explain this? Can you simulate Palminteri et al. (2015) using the OpAL(*) models and show what are the performance in the learning and transfer phase?

A robust and replicable finding in human (and nonhuman) reinforcement learning is that when fitting the model with two learning rates for positive or negative prediction errors (starting from Frank et al. 2007, supplementary materials, continuing in Lefebvre et al. 2017; Gagne et al. 2020; Farashahi et al. 2019; Ohta et al. 2021; Chambon et al. 2020 – the rare occurrences of the opposite pattern are generally explained by wrongly initializing the Q-values at pessimistic values). The optimality of this bias has been sometimes investigated (see Cazé and Van den Merr 2013; Lefebvre et al. 2022). My question here is whether and/or under which circumstances do the OpAL(*) models explain the ubiquity of this pattern? If you simulate OpAL(*) models and then fit the asymmetric model, would you (quasi-)systematically retrieve the asymmetric pattern?

Finally, the actor prediction errors are normalized. I can see the logic of this. I was nonetheless puzzled by the functional form of the normalization that is not really a range normalization (Lmag is lacking at the numerator). Consider for example Bavard et al. (2021), which propose a full range normalization rule. What is the rationale for this particular form of normalization? Are Lmag and Rmag learned (via δ rule or other, see Bavard et al.) or specified in advance?

Reviewer #3 (Recommendations for the authors):

This manuscript proposes a refined version of the OpAL model, which aims to address the numerical instability problems present in the previous version and demonstrate the normative advantages of the model in learning tasks. Unfortunately, the instability problems still persist in the proposed model, and the normative comparison is unconvincing due to the limited range of scenarios and tasks investigated.

Comments

1. It has been previously pointed out that the OpAL model is numerically unstable: all synaptic weights converge to 0 with learning, and as a result, the model has a tendency to make random choices with practice. The authors claim that the proposed model "addresses limitations of the original OpAL", but in fact, it does not – it just postpones their effect by introducing learning rates that decay with time, which ensures that the weights simply stop changing as learning progresses. Consequently, there are several problems with the proposed argumentation in the paper:

a. The paper does not adequately describe the scale of the stability problem faced by the original OpAL model. A cartoon in Figure 1 falsely suggests that the weights in the OpAL model converge to stable values with learning, by contrast even for this scenario all weights decay to 0. The appendix attached below this review contains Matlab code simulating the OpAL model, and the first figure generated by this code shows OpAL model simulations corresponding to Figure 1. Running the code clearly shows that all weights decay to 0 in this simulation. Therefore, weight evolution in the OpAL model in Figure 1, needs to show the actual simulation of the OpAL model rather than cartoons with qualitatively different behaviour of the weights.

b. Similarly, a reader may get a false impression that the instability problems only occur in the scenario in Figure 13, because the manuscript states in lines 1104-1105 that the OpAL model "in carefully constructed situations, gives rise to unstable actor dynamics". However, as pointed out in my previous comment, these problems are ubiquitous, and in fact, Mikhael and Bogacz (2016) also illustrated this problem in Figure 9 of their paper for randomly generated rewards. The reason why Moeller and Bogacz (2019) considered the scenario in Figure 13 is that for this case one can easily show analytically that the weights in the OpAL model converge to 0.

c. To solve the stability problem, the authors modify the model such that the learning slows with time. However, they admit in l.1130: that the model loses its memory with time, and they propose that the habit system may take over learning and rescue animal bahaviour. However, animals with lesions of dorso-lateral striatum (which is known to underlie habitual behaviour) still can perform learned tasks (Yin HH, Knowlton BJ, Balleine BW. 2004. Lesions of dorsolateral striatum preserve outcome expectancy but disrupt habit formation in instrumental learning. European Journal of Neuroscience 19:181-189.) which is not consistent with the decay of memory of goal directed system.

d. The reduction in learning rate with time introduced in OpAL* only makes sense in stable environments. In changing environments decaying learning rate does not make sense, because the animal would be unable to adapt to changing rewards. However, the second figure generated by the code in the Appendix shows that the weights also decrease to 0 in environments where the reward probability constantly fluctuates according to a random walk (in this simulation the rewards are binary, so the normalization of prediction error introduced in OpAL* does not make any difference). In summary, the learning rules of the OpAL model decay to 0 even if the reward probability is constantly changing, so for this case the model is unable to track reward probability no matter if the decrease of learning rate is introduced or not.

2. The manuscript shows that the OpAL* model can achieve higher rewards than alternative models in simple tasks with constant reward probabilities. However, there are severe problems with the arguments in the paper.

a. All the simulations are run with a small number of trials (i.e. 100). Beyond this number of trials the OpAL model suffers from decay of weights (see my previous comment), so it is questionable whether it would have performance advantages. Therefore, it is critically important that the performance comparison includes simulations with more (e.g. 1000) trials.

b. The simple tasks simulated in the paper has been a focus of much research. There is known optimal learning algorithm (Gittins index) and several well performing ones (e.g. Thomson sampling, Upper confidence bound algorithms). I feel that the normative comparison needs to include a comparison with some of these known solutions.

c. The reason why the OpAL* achieves best performance in the chosen scenario is not well explained. Lines 339-343 present the key of the mechanism: "opponency allows the non-dominant (here, G) actor to contribute early during learning (before N weights accumulate), thereby flattening initial discrimination and enhancing exploration. Second, the Hebbian nonlinearity ensures that negative experiences induce disproportional distortions in N weights for the most suboptimal actions after they have been explored (Figure 6a), thereby allowing the agent to more robustly avoid them (Figures 6b and 6c)." However, the cited figures do not illustrate this mechanism, and to show this, it would be better to show how the weights change during learning.

d. The performance of model is compared in two ways: (i) for the best parameters for each model and (ii) for an average over the range of parameters. I think that method (i) is valid, but method (ii) may introduce a bias if the range is chosen such that the optimal range for one model overlaps with the tested range for one model more than for another. Therefore, I feel that method (ii) should not be included in the manuscript.

3. The manuscript also describes comparison of performance of OpAL* with the model by Moeller and Bogacz (2019), however the manuscript includes incorrect statements about the latter model, and the way it is parameters are chosen does not reflect the conditions in simulated scenarios.

a. The manuscript states in l. 392: "However, in actuality, the convergence to expected payoffs and costs in this model depends on having a constrained relationship between parameters optimized by a priori access to the distributions of rewards in the environment." This is not true. For a given set of parameters, the convergence to payoffs and costs is guaranteed for any reward distribution – derivation of the condition for encoding payoff and costs in Eq 22 and 23 in Moeller and Bogacz does not make any assumptions about knowledge of reward distribution. Please remove this sentence.

b. The condition on parameters derived by Moeller and Bogacz are only necessary to learn payoffs and costs if every trial includes a cost (e.g. an effort to make an action) and a payoff (e.g. the outcome of the action). This is not the case in the presented simulations, so the model parameters do not even need to satisfy the conditions of Moeller and Bogacz.

c. The model is simulated with constant "tonic dopamine" level, and by mathematical construction, in this case the models described by Moeller and Bogacz is mathematically equivalent to Q-learning with decay controlled by parameter λ, and will reduce to the standard Q-learning for λ = 0. Since the Authors simulated Q-learning, it is not even clear if it is necessary to simulate Moeller and Bogacz model because by its definition it will have identical (with λ=0) or very similar performance.

d. The manuscript states in l. 415: "Finally, the model in Möller and Bogacz (2019) demonstrated poor across-environment performance, performing only slightly above chance in the rich environment. Results are not shown for this model" – one should not make such statements without actually presenting evidence for them.

Appendix – code simulating OpAL model

function run_OpAL

figure(1)

trials = 2000;

pr = [0.9 0.8 0.7; 0.1 0.2 0.3];

labels = {'rich', 'lean'};

for env = 1:2

subplot (2,1,env);

for action = 1:3

p = zeros (1,trials)+pr(env,action);

[G,N] = opal (p);

plot (G, 'g');

hold on

plot (N, 'r');

end

xlabel ('Trials');

title (labels{env});

legend ('G','N');

end

figure(2)

trials = 1000;

p = zeros (1,trials)+0.1;

for t = 1:trials-1

p(t+1) = p(t) – 0.1*(p(t)-0.5) + 0.1*randn;

if p(t+1) > 1

p(t+1) = 1;

elseif p(t+1) < 0

p(t+1) = 0;

end

end

[G,N] = opal (p);

subplot (2,1,1);

plot (p);

ylabel ('Reward probability')

xlabel ('Trials');

subplot (2,1,2);

plot (G, 'g');

hold on

plot (N, 'r');

legend ('G','N');

xlabel ('Trials');

end

function [G,N] = opal (p)

trials = length(p);

V = zeros (1,trials)+0.5;

G = zeros (1,trials)+0.1;

N = zeros (1,trials)+0.1;

α = 0.2;

for t = 1:trials-1

r = (rand

δ = r – V(t);

V(t+1) = V(t) + α*δ;

G(t+1) = G(t) + G(t)*α*δ;

N(t+1) = N(t) – N(t)*α*δ;

end

end

Thank you for resubmitting your work entitled "On the normative advantages of dopamine and striatal opponency for learning and choice" for further consideration by eLife. Your revised article has been evaluated by Joshua Gold (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Essential revisions:

Reviewer 3 still has significant concerns about the stability of the model, and about the mechanisms accounting for its superior performance. Please make sure to fully address all requests for clarification detailed below.

Reviewer #1 (Recommendations for the authors):

The authors have successfully addressed my concerns.

Reviewer #2 (Recommendations for the authors):

The authors successfully addressed my suggestions.

Reviewer #3 (Recommendations for the authors):

This manuscript proposes a refined version of the OpAL model, which aims to address the numerical instability problems present in the previous version, and demonstrate normative advantages of the model in tasks involving balancing exploration and exploitation.

I thank the Authors for replying to my review. I feel that the manuscript has been significantly improved, and the comparison of performance with UCB is particularly interesting. Nevertheless, there are still issues that need to be addressed. In particular, it is not clear from the analysis why OpAL* can outperform UCB, and multiple statements about the stability of the model are still misleading.

Comments:

1. It needs to be further clarified why OpAL* outperforms UCB and Q-learning. I have to admit that I am surprised by the higher performance of OpAL* over UCB, because UCB is not an easy algorithm to outperform. Unlike Q-learning, UCB has perfect memory of all rewards and does not forget them. Then I realized that OpAL* also has such perfect memory, as its Bayesian critic counts the rewarded and unrewarded trials for each option. I feel this is the main reason why OpAL* outperform Q-learning. I suggest explaining this important property of OpAL* in the text, and it would be good to test it, e.g. by replacing Bayesian critic by a normal forgetful critic, and testing "Contribution of perfect memory". Please also discuss if such perfect memory is biologically realistic – how could it be implemented in biological neural network?

However, the most surprising result is that OpAL* outperforms UCB. This cannot be explained by most of the discussion of Mechanism section focussing on the gaps between weights for different options, because such gaps are only important if an algorithm choses actions stochastically based on weights, while UCB is practically a deterministic algorithm (beyond initial few trials it will deterministically chose an option). The only mechanism which can explain outperforming UCB is explained in a paragraph starting in line 574. Please investigate further, and provide a clear explanation for how it is possible for OpAL* to outperform UCB.

2. The stability of OpAL* model needs to be honestly presented. The main issue pointed by Mikhael and Bogacz (2016) and then by Moeller and Bogacz (2019) is that the weights in OpAL will asymptotically converge to 0. It is still evident from simulations of the OpAL* in the manuscript and in the response letter that on average the weights decay with trials. There is no demonstration that OpAL* can prevent its weights from converging to 0 eventually, and at the same time can respond to changing rewards. In the revised version, such demonstration has been added in Figures 15c right and 15d right, but it is not possible to understand how these simulations were performed from the paper, and it seems that they are for a model with "weight decay", which is not described in the manuscript. It is not clear if the model with weight decay has the advantages of OpAL* in exploration/exploitation that are the focus of the manuscript. Therefore, I feel that the manuscript has to be modified in one of two ways: The Authors may change the model in the paper to one with weight decay and analyse its performance in exploration/exploitation task. Alternatively, if the current OpAL* model remains the focus of the paper, it needs to be honestly admitted that the OpAL* model suffers from the problem that weights will eventually converge to 0 or the model will stop adapting to changes in the rewards.

Specific comments:

Equation 15 – How is std X estimated? Is it computed from the analytic expression for β distribution? If so, this expression is complex (involving division, square, etc.), so please comment on how such computation could be made by biological networks of neurons.

Equation 22 – Please explain parameter T. As above, please explain how X is computed in the simulation.

Line 293: "These modifications improve the robustness of OpAL* and ensure that the actor weights are well-behaved" – I do not agree with this statement, because in the OpAL* model the weights still converge to 0 unless they are prevented from convergence to 0 by making the model non-adaptive. Please replace "well behaved" in the cited statement, by a more specific description.

Line 499: "Indeed, algorithms like Q-learning and UCB converge well when an option is well-sampled, but the speed and accuracy of this convergence is affected by stochastic sampling". This argument does not apply to UCB, which is deterministic, and hence the sampling in UCB is NOT stochastic.

Line 582 – this again does not seem to apply to UCB, which is deterministic.

Figure 6a is very interesting, but I have a few suggestions to make it more informative. I simulated UCB on the problems in Figure 6a and verified that it indeed gives similar performance to that visualized in this figure, but found that with 1000 iterations there is still substantial variability in the results, and sometimes you get non-monotonic changes in accuracy as shown in blue curve in Figure 6a left, which disappear if the number of iterations is increased. Hence, I suggest to increase the number of iterations (repetitions) in Figure 6a to 10,000 to get less noisy curves.

In Figure 6a the gap between UCB and OpAL* is higher in the right panel but it is not clear if this is due to change in richness or in the number of options. It would be helpful to add two more panels ([0.2 0.3] and [0.8 0.7 0.7 0.7 0.7 0.7]). Also for an easier replicability, it would be good to list the parameters used in simulations of each model.

l. 1478: "Normalizing, therefore, addresses the valid concerns of Möller and Bogacz (2019) while still preserving core OpAL dynamics". I do not agree – the key concern of Möller and Bogacz (2019) was that the weights decay to 0 eventually. The normalization does not fix the problem. In the simulations I did in the previous round of the review, rewards were 0 and 1, so the normalization had no effect.

Equation 30 – I guess the last 2 "cases" were included accidentally (they are a typo), and should be removed.

l.1112: UCB – Please provide the reference for the paper describing UCB. In this algorithm, the model is initialized to selecting each action once before relying on estimated values. Do you do such initial selection? If so, please say this.

Throughout – In many places in the manuscript there are references to appendix, but the appendix is long, and it takes time to find information. Hence whenever you point the reader to the appendix, please point to a specific section or figure.
