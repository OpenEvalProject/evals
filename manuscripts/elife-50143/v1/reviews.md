# Peer review - Round 1

Editors:
- Timothy O'Leary, University of Cambridge United Kingdom

Reviewers:
- Robert Pearce

## Review text

DOI: [10.7554/eLife.50143.sa1](https://doi.org/10.7554/eLife.50143.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study examines intra- and inter-subject variability in anaesthetic efficacy in two animal species, mice and zebrafish. The authors find that in the vicinity of the EC50 for two different anaesthetics, animals exhibit state-dependent fluctuations between putative conscious and unconscious states. Importantly, the analysis separates trial- and individual-level variability in behavioral outcomes, showing that population level measurements of drug efficacy can be very unreliable measures of efficacy at the individual level, and that individual fluctuations are consistent. This has important implications for personalised medicine and anaesthesia in practice.

Decision letter after peer review:

Thank you for submitting your article "Tight control of noise in state transitions revealed by dynamics of fluctuating individual drug responses" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Richard Aldrich as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Robert Pearce (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All reviewers agreed that the work is important and that the manuscript should appeal to a large cross section of life scientists. The reviews highlighted a few essential revisions (in detail below) that will improve the manuscript and facilitate readers. These concern the interpretation of the results, the assumptions, statistical analyses and a few points on presentation.

Reviewer #1:

This study examines intra- and inter-subject variability in anaesthetic efficacy in two animal species, mice and zebrafish. The authors find that in the vicinity of the EC50 for two different anaesthetics, animals exhibit state-dependent fluctuations between putative conscious and unconscious states. The experiments seem to be conducted rigorously and the manuscript is clear.

It is not clear to me that the pharmacological community (or life scientists and clinicians more generally) would be surprised by the results of this study. Nonetheless, there is a temptation to summarise population effects without considering individual variability or time (state dependence). I think the study is valuable because it illustrates both. With minor editing it could be clearer still, and will help members of the community avoid pitfalls of interpreting dose-response relationships naively.

I have only one substantive concern that is easily addressed. The statistical analyses are not reported adequately. It is not sufficient to simply report a p-value; the degrees of freedom in the test should be provided to ensure appropriate units of replication.

Reviewer #2:

McKinstry-Wu et al. report a model of behavior during anesthesia aiming to account for variability within each behavioral state. This paper presents a useful examination of the variable and stochastic nature of behavior during anesthesia, separating trial- and individual-level variability in behavioral outcomes. A concern, which could be addressed with rewriting, is that the authors discuss anesthesia as if it were intrinsically an all-or-none brain state, but their choice of experimental design imposes the binomial structure onto the data.

Results:

- The use of within-session comparisons for the zebrafish condition (Figure 5), as opposed to the cross-session testing in mice, holds the limitation that there will be session-dependent effects included in this analysis.

- For Figure 6, do the same mice exhibit high sensitivity in both conditions? i.e., within an individual does this overlap still hold? This overlap analysis is interesting but it is not clear from the figure whether it is due to variability within the population or within a given concentration.

Comments on the text:

- The paper's Introduction states that anesthesia is a binary state, and that an individual is either anesthetized or not. However, the state of anesthesia is a spectrum with multiple dimensions – for example, a patient can be in a lightly anesthetized state in which they will not react to a simple sensory stimulus, but will still react to a painful stimulus. The Introduction should be written to clarify this distinction. The method the authors propose can be applied to a specific desired behavioral outcome of interest during anesthesia, but it doesn't mean that anesthesia itself is binary.

- While the authors state several times that behavior is thought to be constant during anesthesia, in general it is known that behavior is variable at a given concentration, for example a binomial state-space model of variable behavior during multiple concentrations of anesthesia has been previously developed and should be cited, Wong et al., 2014.

- The discussion of bistable states is a bit misleading, particularly the section comparing sleep and anesthesia, since it seems unlikely this is a bistable switching between sleep and wakefulness. Even a very gradual descent into anesthesia will appear bistable if a single yes/no threshold is applied to define the behavioral state. In this scenario, the bistable nature is imposed by the behavioral reporting scheme used, and a completely different result could be obtained by using a different behavioral paradigm (for example, if using a study measuring reaction time or magnitude of response). The methods point out the thresholding techniques applied to achieve a binomial outcome (a decision as to whether the mouse achieves 2 separate rightings, and a threshold of distance travelled that is applied to the zebrafish). The Figure 2—figure supplement 2 provides an example of this, as while there is bimodality to the behavior, the yes/no behavioral report is imposed by the authors' threshold. It's useful to distinguish between the bistability of the behavioral test (which is useful for clinical purposes) vs. the bistability of the brain state (which is not shown here, since no neural data were acquired, and in general is found to exhibit complex graded dynamics across anesthetic states).

Reviewer #3:

This paper describes experiments that characterize responsiveness of mice (righting reflex) and zebrafish (startle reflex) in the presence of varying concentrations of anesthetics. The investigators find that i) responsiveness does not match expectations of a Bernoulli process, but rather it fluctuates on a time scale slower than their repeated observations; ii) anesthetic sensitivity differs between individuals, both on a short-term and on a long-term basis; and iii) response probability shows a broad distribution for individuals, in contrast to the expected steep dose-response of population responses. Based on similarities between inter-individual transition variability characteristics the authors argue that noise driving transitions is a conserved and tightly constrained value across species.

The study has many strengths. It uses an interestingly different approach to address an old question, one that has been investigated extensively in the past but that remains unanswered and of intense interest. The methodology is sound, and the observations have been carefully and thoroughly documented. The analysis based on probabilistic statistics makes a convincing case for fluctuating responsiveness that differs between individuals, a finding that is novel and important to the field.

One aspect of the paper that I find less convincing, and possibly problematic, is that the Abstract and Discussion focus so strongly on the 'noise' driving transitions, concluding that noise is tightly controlled and conserved across species – all without having made any explicit assessment of the inferred noise nor any attempt to manipulate it. Rather, the conclusion was based on the finding that the joint distributions of transition probabilities lie on a diagonal and are strongly negatively correlated (Figure 4). The interpretation that 'noise' drives the transitions depends on the underlying model. The authors do put forward a possible model, with their suggestion that the consolidated states of 'sleep' and 'wakefulness' may form such a neurophysiological model. In their model, noise is required to overcome a barrier between the states, similar to the barrier between metastable states of a receptor. This is a reasonable, even attractive, model, but it is conceptual rather than quantitative. Thus, it is difficult to understand how this might be applied to state changes in different individuals or species, and whether the amount of noise is the same or not. Perhaps a quantitative model of the depths of wells/heights of barriers could be derived from the data, using the data of Figure 4—figure supplement 1 to derive transition rates, and compare them explicitly between individuals and species.

Another interesting observation that is discussed relatively extensively is the relationship between individual responsiveness, which seems to show a relatively shallow concentration-response, compared to the expected steepness based on previous population data. It would be useful to know whether the aggregated data do indeed show the expected (as quoted) Hill coefficient of 10-40. If this is the case, can the authors explain how dispersed shallow concentration responses add up to steep population response relationships? If it is not the case, this information is worth noting and it will further inform the discussion.
