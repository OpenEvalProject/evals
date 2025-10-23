# Peer review - Round 1

Editors:
- Frances K Skinner, University Health Network Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26724.017](https://doi.org/10.7554/eLife.26724.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Multidimensional imbalances in cortical circuit activity in Fragile-X Syndrome mice" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom, Frances Skinner, is a member of our Board of Reviewing Editors and the evaluation has been overseen by Huda Zoghbi as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Bill Lytton (Reviewer #2); Mark D Humphries (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study combines computational modeling and analysis of two-photon Ca2+ imaging data from in vivo Fragile-X model mice to test the excitatory-inhibitory (E-I) imbalance theory of circuit dysfunction. The microcircuit model highlights the complex non-linear effects of perturbations to cellular components on circuit function, and combined with their logistic response model, indicates that E-I imbalance theory is not sufficient to explain dissociated effects of firing rate and correlations. Analysis of data from Fmr1 knock-out mice demonstrated differences in input-output circuit parameters across development, which could not be captured by examining firing rate and pairwise correlations between neurons alone.

Overall, the model and analysis are able to show relationships between firing statistics and underlying circuit parameters.

The demonstration of capturing network-wide changes in dynamics by a neuron's or population's P(spike) function is innovative, and opens up a range of possible applications in both modelling and data analysis – both of which are demonstrated here. A nice bonus is the characterization of the developmental trajectory of the WT and Fmr1 mice. Collectively, the work attains its goal: to evaluate the relevance of E/I balance, and suggest an alternative.

All of the reviewers found the work to be interesting and felt positive in different ways, but all of the reviewers also felt that extensive rewriting and re-organization was required as several points were confusing and/or unclear along with clarifying various issues. There are three essential aspects that the authors need to address as well as the 5 further comments.

Essential revisions:

A) A re-organization and re-write is required so that the motivation and rationale is clear at various junctures. Some reviewers thought it would be better to present the experiment first (as described at the end of the Introduction, "In this study we compare in vivo….") rather than the model first as it is at present. That is, starting with the problem and working forward rather than starting with some solutions and seeming to look for a problem.

For example, presenting the data first would allow it to be used as a motivator for the model, and make it more accessible to a general neuro audience. However, this then would perhaps seem like P(spike) comes out of the blue. If the order is left as is with the model first, then the motivation needs to be more clearly described and the work should perhaps be presented with less emphasis on Fragile-X and instead a focus on the how models can highlight the simplicity of E-I imbalance theories etc. With this latter option, a title change should be considered.

We leave it to the author to decide how they prefer to re-organize and re-write to present their work in a clear, motivating fashion through the various steps, so that the reader can appreciate and grasp what are the main exciting results. That is, there is a need to bring out the logic of certain choices, details of the analyses, and the motivation for the analyses.

B) Caveats and limitations, as well as advantages and disadvantages of their model should be brought forth in the main text for the reader to appreciate up front, and not only given in the Materials and methods section.

For example, explicitly state why and how a simpler model could/should not be considered, and why they do not expect existing model choices/limitations to not necessarily affect the outcome (e.g., "varying the strength of synapses from 5HT3AR inhibitory neurons to E neurons.… has little effect" might possibly be troublesome given the model setup).

Even within the Materials and methods section, more rationale for model details should be provided. Model equations need to be provided.

For the above points, additional subsections in the Results section could be helpful.

C) Models are only reliably replicable if downloaded. The model (microcircuit, logistic response model) should be made available via ModelDB, GitHub or other repository.

The following comments from the four reviewers also need to be addressed.

1) Explicit equations for population model and circuit model should be provided. Integration scheme and time constant for easy reproduction needed.

Also, several connectivities are fixed or not examined at all (e.g., 'typical cortical value of 0.15?' – what is that based on if there is no data? etc.).

While robustness is tackled via a +/-20% adjustment and found to be 'sloppy', this is essentially because a dynamical systems understanding does not exist (e.g., there would be more sensitivity near a bifurcation) as the authors would know. While it is clearly not possible to do a dynamical systems analyses (and certainly true in general for high-dimensional systems), I wonder if the authors could provide some understanding of the essence of their network I/O in some way to understand the sloppiness and parameter fixing or not including certain connectivities. While this could be challenging, I think this is important to bring forth in some way since the authors go on to analyse their model as if it is 'good enough' to represent the biological situation, so it seems glossed over.

Further, this forms the basis of the linkage they are making here, and it was not clear to me. That is, the interpretation of model (and its parameters) analyses relative to the calcium imaging analyses that was being compared was obscured and/or unclear.

2) I am somewhat perplexed by the decision to lead with the model and then introduce fragile X data late in the paper. In general, I would be more interested if the paper could present some problems with understanding fragile X pathophysiology, likely by interpreting it initially by using various levels of straw-man simplistic single-factor thinking with a simple or 2-stage (I/E) logistic-function explicit model. From there, the paper could demonstrate how the more sophisticated model can at least permit assessment of features which are inaccessible in a logistic model. Granted that this final L2/3 model also does not directly predict treatments fragile X, it at least points in the direction from which future solutions will come.

3) Issues regarding the construction of the microcircuit model. The authors constrained their PV and 5HT3AR model parameters from the experimental work of Avermann et al., 2012. However, this paper identified two GABAergic populations: fast-spiking (shown to be PV-expressing), and non-fast-spiking (NFS; i.e., everything else). Although a large percentage of these NFS cell are likely the heterogeneous 5HT3AR population, they would also include SOM-expressing cells. This assumption that NFS are strictly 5HT3AR has led to some perhaps misleading choices in model construction and choices for intrinsic and synaptic parameters. For example, ~40% 5HT3AR cells are VIP+ in S1 (Lee et al., 2010), and a primary target of VIP+ interneurons are SOM+ (Pfeffer et al., 2013; Dalezios et al., 2002), but the model has no 5HT3AR→ SOM connections. Also, it has 5HT3AR→5HT3AR connections, but not SOM→PV (Pfeffer et al., 2013)?

Overall, these model choices will likely not affect the main results – an overall varied sensitivity to cellular changes. However, it makes the specifics of how distinct populations are affected in Figures 1 and 2 (and the associated text) difficult to interpret from a biological standpoint. Along those lines, Table 1 describes the circuit model variables and could serve as a resource for modelers and experimentalists alike. However, for clarity, readers should be aware of the assumptions made so that they can use with caution.

4) The authors found that the direction of circuit parameters change in young to mature mice is opposite in KO vs WT, which could not be captured by examining neural activity statistics. Given that there is so much redundancy and variability at the cellular level, how does knowing about these circuit properties help us in terms of mechanisms of change?

The logistic response model also fits the threshold s.d., the slope s.d., and the slope-threshold correlation. How were these parameters affected in development/in KO?

5) It is unclear what we learn from the population-level P(spike) model that we could not learn from the single neuron model. Two things it would be good for the authors to address here:

i) The population-level model lacks motivation – I would expect the fourth paragraph of subsection “Firing rates and correlations from the logistic model” to start with something like "In order to characterise the population, we fitted… because…". Why fit a 5-parameter model to the whole population: why not just fit each neuron with a 2-parameter model, and average over their fits? [Just as was done for the model]. Then one would also obtain the population variation in the slope and threshold parameters, and that variation need not conform to a Gaussian model as is enforced by the 5-parameter model. I suspect there is an underlying issue with having enough data per-neuron. Please elaborate.

ii) Having fitted a population model, not much is done with it. It seems plausible that the variation in slope and threshold (quantified by the SD) could change with development, as the underlying parameter ranges contract or expand. So what is the variation over development, and does it differ between WT and Fmr1 mice?
