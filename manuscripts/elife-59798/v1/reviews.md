# Peer review - Round 1

Editors:
- Tatiana Pasternak, National Institute of Neurological Disorders and Stroke United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59798.sa1](https://doi.org/10.7554/eLife.59798.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work provides important new insights into the development of visual motion integration in the ferret visual system. By simultaneously following the development of responses to global motion in primary visual cortex (V1) and in the higher order cortical area PSS, the paper demonstrates that responses to complex motion in the two areas depend on mutual and coordinated interactions, documenting the prominent role of feedback during development. The work has important implications for broader understanding of the nature of interactions between processing stages during brain development.

Decision letter after peer review:

Thank you for submitting your article "Development of visual motion integration involves coordination of multiple cortical stages" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Chris Baker as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Robbe Goris (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Both reviewers were impressed with several aspects of the study and felt that it has a potential of providing new insights into the development of mechanisms underlying cortical processing of global motion. However, they raised a number of substantive concerns that must be addressed before the manuscript can be considered for publication in eLife. These concerns are summarized below.

1) The criteria for establishing developmental epochs are inconsistent throughout the manuscript. These should be established ahead time, justified and used consistently for all analyses.

2) Please address the issues with data analysis resulting from inconsistent subsampling of the data, exemplified in Figures 2 and 5 (see comments from reviewer 2)

3) A related problem results from potential sampling bias: firm conclusions are drawn about group differences despite large differences in Ns among the groups. Adding information about how representative the samples are and a more robust analysis approach could allay these concerns.

4) Please address the problem with the current version of the model-based analysis, raised by Reviewer 1. This reviewer suggests fitting the data with the maximum likelihood method and made a number of other suggestions that are likely to improve the analysis and fitting the data.

You may want to consider this reviewer's suggestion to reorganize the paper and start with presenting the data followed by the introduction of the model and its simulations.

5) Please address the issue raised by reviewer 1 concerning the discussion of the results starting on paragraph four of the Results section.

6) Each reviewer provided additional comments and suggestions, highlighting a number of inconsistencies, which I suggest you address directly.

Reviewer #1:

Lempel and Nielsen report a very cool empirical result: the coordinated development of visual motion integration in areas V1 and PSS. The insight that feedback plays a more prominent role in specific phases of visual development is novel and important. That said, the paper offers no helpful computational understanding of this phenomenon, is written in a manner that appears to reflect the "autobiographical" logic of studies more so than what is actually learned from these studies, and contains a number of questionable data-analysis choices that should either be improved or better justified.

Summary of substantive concerns

1) The age-grouping differs throughout the paper. This is very problematic for a developmental study. The authors need to establish the developmental epochs of interest and the criteria to group ages up front and then stick to these conventions throughout the paper.

2) The model-based analysis in its current form is not helpful. There are a number of issues. First, when introducing the model, it would be helpful if you would start by contrasting the model-parameters for the component and pattern cells – is there any meaningful difference? This is not obvious. For example, the width of the excitatory channel appears to be going in the "wrong" direction in light of the root model of Simoncelli and Heeger (1998) – pattern cells ought to have a broader direction of motion bandwidth, see Figure 10 in Zaharia et al., 2019, for empirical evidence in primates. Second, a recovery analysis would build trust in the modeling enterprise and reveal whether this set of empirical measurements actually allows to unambiguously identify the model's parameters (this could go in supplementary information). Third, the use of mean square error as badness-of-fit statistic and grid-search as optimization routine likely introduces a needless amount of bias and variability in the parameter estimates. How about fitting the data using a maximum likelihood method and an explicit model of spike generation, for example a modulated Poisson process as in Zaharia et al. (2010)? That approach better reflects the standard of model-based data-analysis in current systems neuroscience. Fourth, how can you describe the plots in Figure 5C and D as a match? The model obviously fails to reproduce the most prominent features of the data, calling into question whether we can learn anything meaningful from its parameter estimates at all. Models are only useful if they create insight beyond what can be learned from a simpler data-analysis. It's not clear that the current analysis meets that standard.

3) I would consider to reorganize the paper, lead with the cool coordinated development result, and only then turn to the question "Which computational mechanisms might underlie this phenomenon". I would be fine with a model simulation rather than a model-fitting exercise if it provided some insight into how this coordination can come about. I think that a more complex two-stage model with a feedback loop would be appropriate. How would the feedforward and feedback elements of such a model need to change to capture your empirical observations in both areas? Perhaps you can derive an empirically testable prediction from such a simulation?

4) Results paragraph four and following. The developmental changes in PSS neurons' motion integration are described and treated as a number of independent effects. "First, the influence of the component signals decreased with age… Second, the influence of the pattern signal increased with age…" etc. This is based on an analysis in which data are correlated with two competing predictions. Due to the nature of correlation, it typically has to be the case that if one number goes up, the other has to come down. I would consider reducing this to a single clear statement: The fraction of pattern cells changes, as does the average pattern-index of the population.

Reviewer #2:

This paper describes a set of experiments designed to address the question of how global motion sensitivity develops in ferret high order cortical area PSS. Sensitivity to grating and a range of plaid stimuli is tested in ferrets of different – but early – ages to address this question. The findings can apply to questions of brain development more broadly, as they point to a hierarchical developmental profile – one for which there is fairly strong support in the broader development literature. Thus, the data are of value beyond the specific focus of this paper – on development of motion mechanisms in ferret. Strengths include the comparative analysis of multiple processing stages over the same developmental time period, comparison of low-level and higher-level motion mechanisms, and comparison of their data with a model that allows one to draw insights into the neural mechanisms that contribute to the development of plaid motion sensitivity. The main weaknesses are related to a general sense of uneasiness about the data analysis and presentation, that leaves the reader less than convinced about some of the conclusions.

Strengths

Recordings are made from V1 and PSS, although not in the same animals. Simultaneous recordings would be preferred because of interanimal variability but that was not done here. Regardless, some conclusions can be drawn.

Ferret model allows access to a very early time period in visual system development that is not accessible in the primate. Also, ferret has an analogous motion processing hierarchy to the primate suggesting that the data are likely to apply generally.

The authors utilize a modified version of a previously developed model for plaid sensitivity. Direct comparison is made between data and model predictions, with the goal of identifying potential mechanisms driving the developmental changes.

Weaknesses

Throughout the manuscript, different comparisons are made using different poolings of the neural data. It is unclear why this is. It seems as though they have a large data set collected from many ferrets of a range of ages that is then selectively subsampled for different comparisons. This is not a robust or reliable approach and seems arbitrary and ad hoc. For the primary comparisons, Figure 2, 4 groups of animals are described (P37-41, P42-43, P44-47, "adult"). For the model, 2 groups are selected, here – justifiably – to subdivide before by and after Plaid sensitivity development: P37-41, P44->adult. However, in Figure 5, the data are divided into 3 groups: P37-41, P44-47or 48, "adult". Apart from the case of the model, there is no principled reason for changing the age groupings for the animals.

Perhaps related to the above concern, conclusions are drawn with certainty based on often lopsided comparisons across groups with grossly unequal N. For example, the fundamental conclusion regarding the age at which the pattern response matures is based on a small number of observations in the critical age group P42-43 (N=31); the youngest age group has N=154 while the older age groups have moderate although still comparatively small N. According to Table 2, those 31 neurons came from 5 animals. Similarly, some of the supplemental figures are based on very small numbers of units (e.g. S3c, N=11). One has to wonder about sampling bias and individual differences across animals. Are these differences really meaningful? What is the relative proportion of Zc, Zp and pattern index across different animals of the same age/experience? Without this variance information it is hard to know if the conclusions are valid.

Similarly, although the analysis of the effect of visual experience is very clever, one has to wonder why the data are not presented by days. V4 – a single day – group is compared with "5 or more days" range 5-7 days, resulting in a comparison between N=33 and N=105 units. There is no principled reason for this choice given. For this comparison to be meaningful, the individual days with (presumably) more comparable N should be presented.

The muscimol experiment seems to be tacked on the end. It is a critical component of the overall study that shows that there is likely an interaction between the maturation of PSS and V1 plaid responses. The earlier conclusion based on the model that V1 responses change and play a role in maturation of motion responses, could be because of feedback. These points are not connected until later. Better to include them earlier and provide a more coherent narrative.

The main analysis would be more robust if based on a coherent multivariate analysis that accounts for multiple comparisons to any one data set.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Development of visual motion integration involves coordination of multiple cortical stages" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Chris Baker as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Robbe Goris (Reviewer #1); Lynn Kiorpes (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers felt that most of the reservations raised in their reviews have been addressed. However, one last issue remains. It concerns the approach chosen to isolate the role of visual experience. The suggestion is to include all the data in the analysis, rather than just the subset. Specifically, it would be more informative to include a plot (similar to Figure 2A) showing each animal's median pattern index a function of visual experience over a reasonable range (e.g., from V1 to V7+ in steps of 1 day). The reviewers agreed that an ANCOVA analysis would be an appropriate statistical test for the hypothesis that visual experience explains variance in pattern index beyond the effects of gestational age.

Reviewer #1:

The authors addressed most of my concerns. The remaining issues are detailed below.

The paper has improved substantially, and the authors have addressed several of my concerns. One substantial issue remains in my opinion. Just like the grouping in developmental epochs felt a bit ad hoc in the previous submission, so does the grouping in visual-experience epochs in this resubmission. It is not clear what makes V4 and V5 so special that these epochs should be at the center of this analysis. I am not sure that the authors have sufficient data to distinguish experience from gestational age. The gestational age difference between the V4 and V5 group is a bit more than a day, and so seemingly highly correlated with the difference in visual experience. Furthermore, I don't understand the logic behind Figure 3D and 3E: Why is the absence of an age-based difference in pattern-selectivity evidence in favor of the role of visual experience? If the authors wish to attempt to isolate the role of visual experience, it would be better to conduct an analysis that involves all of their data, rather than just this subset. For example, a plot like Figure 2A, whereby each animal's median pattern index is shown as a function of visual experience over a reasonable range (e.g., from V1 to V7+ in steps of 1 day) would be more informative. I think that an ANCOVA analysis provides a suitable statistical test for the hypothesis that visual experience explains variance in pattern index beyond the effects of gestational age (Pattern index of each cell/animal: dependent variable; age group: independent variable; visual experience: covariate).

Reviewer #2:

The authors have substantially revised this manuscript. They have addressed the major issues raised in the reviews and followed the recommendations made. I find the data presentation to be clear and convincing, and the conclusions to be appropriate. My concerns have been addressed.
