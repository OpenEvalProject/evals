# Peer review - Round 1

Editors:
- Thorsten Kahnt, Northwestern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58809.sa1](https://doi.org/10.7554/eLife.58809.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study shows that the human brain encodes errors in a task-dependent manner. Similar objective errors elicit different neural responses depending on their meaning, defined by the statistics of the task. These results provide novel insights into how the human brain supports adaptive behavior.

Decision letter after peer review:

Thank you for submitting your article "Distinct neural encoding of context-dependent errors and context-dependent changes in behavior during adaptive learning" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This manuscript reports an fMRI study examining error processing in a predictive inference task. The task involves different conditions/contexts defined by their level of noise and volatility. Using MVPA, the authors identified differences in the neural representations of error magnitude and error history in posterior parietal cortex between these conditions. Moreover, behavioral adjustments could be decoded from activity in dorsomedial frontal, anterior cingulate and orbitofrontal cortices.

All reviewers agreed that this is an interesting study addressing a timely question on adaptive behavior, and that the manuscript will be informative to readers interested in decision making, learning, and cognitive control. They further found the experimental design and the general approach convincing, and the results robust. However, there were several concerns regarding analysis and interpretation that need to be addressed prior to publication.

Essential revisions:

1) Results in Figure 6 are interesting as they show that behavioral adjustments can be predicted from brain activity, replicating the findings by Hampton and O'Doherty, 2007. However, it is not clear that they can be considered "context-dependent". This analysis is based on one condition only, and it is therefore not clear whether or not these signals are context-dependent. The reviewers understand that because there are no ambiguous errors in the unstable context the behavioral adjustment analysis is not possible in this context, and thus, no comparisons across contexts can be performed. The authors can choose to keep these results in the paper, but they should not refer to them as "context-dependent" anywhere in the manuscript, including the title and Abstract.

2) The experimental design uses noise level and volatility to define contexts. This is potentially problematic. First, we do not know whether differences between conditions are driven by noise levels, hazard rate, or both. This needs to be discussed. Second, and more importantly, because the noise level is zero in one condition, one context is deterministic whereas the other is probabilistic. This fundamentally changes the meaning of errors and error magnitude between the contexts, such that there is no meaning to error magnitude in the unstable condition (in the sense that larger errors would be any different from smaller errors). Instead, it is a nominal signal that informs subjects of what the new target is, such that an error of 1 carries the same information as an error of 6. Why would such a signal be encoded in a ordinal or linear fashion as in the high-noise condition, where the magnitude of the error is meaningful? Thus, given that contexts are defined by whether or not error magnitude is meaningful, is it really surprising that the brain responds differently to error magnitude? Would the authors expect to find the same results if context was defined by a variable that does not directly affect the meaning of error magnitude (e.g. learning about target locations in different environments)? This boils down to the question of whether these are context-dependent errors, or just fundamentally different errors. Given these issues, reviewers felt that describing the results as "context-dependent" is slightly misleading. To be clear, reviewers feel that the findings are important and interesting, but they agreed that this interpretation needs to be revised throughout the paper (including title and Abstract).

3) There were several methodological/statistical concerns that need to be addressed.

3.1) The low number of subjects (N = 16 – 1 = 15) may call into question the generalizability of the findings. It is relieving that the univariate analysis largely replicates McGuire et al., 2014, but the MVPA analyses are novel and it is hard to assess their generalizability and the potential of false- positive findings. At the very least, this need to be acknowledged in the Discussion.

3.2) The second condition under which trials were removed from analysis is unclear (subsection “Behavior analysis”). What was the exact criterion to identify these trials? Which error magnitude was still acceptable? Did this mean that, after trial removal, large error magnitudes were always and only associated with change points, and does this bias the results in favor of the author's hypothesis?

3.3) The uncorrected threshold of p < 0.005 is prone to false positives (Eklund et al., 2016), and the authors should use p < 0.001 to define clusters, as suggested in that paper.

3.4) Please clearly describe how "balanced accuracy" was computed, and perform random permutations to determine empirical chance levels and use those as baselines.

4) It was unclear why the RB model was used in this study that need to be addressed.

4.1) The two factors in the experimental design do not seem to map directly onto hazard rate (H) and noise level (K). Indeed, H and K appear to be correlated: in a fast change environment, H should be high by definition, K also needs to be high in order to account for frequent changes of reward target.

4.2) Figure 3—figure supplement 1B: The RU values in the unstable condition is lower than those in the high-noise condition. This is opposite to what is shown in Figure 3B. In other words, this result shows a discrepancy between behavioral data-derived model output and output from true model parameters, which may suggest that the model does not account for the behavior as expected.

4.3) The current model-based behavioral results do not support a direct relationship between model parameters and behavior; instead, the authors just show that both model parameters and behavior change as a function of experimental conditions.

4.4) The model-based fMRI results are mostly replications of previous studies and are not linked to the key results (e.g. Figures 4-6). That is, it is unclear what the model really adds to the conclusions of this paper.

4.5) Given these concerns, reviewers suggested to move model-related results to the supplementary materials.
