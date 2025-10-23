# Peer review - Round 1

Editors:
- Chris I Baker, National Institute of Mental Health, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72904.sa0](https://doi.org/10.7554/eLife.72904.sa0)

This manuscript is of broad interest to the neuroimaging community. It establishes a detailed reference model of human brain development and lifespan trajectories based on a very large data set, across many cortical and subcortical brain regions. The model not only explains substantial variability on test data, it also successfully uncovers individual differences on a database of psychiatric patients that, in addition to group-level analyses, may be critical for diagnosis, thereby demonstrating high clinical potential. It presents a clear overview of the data resource, including detailed evaluation metrics, and makes code, models and documentation directly available to the community.


---

# Peer review - Round 1

Editors:
- Chris I Baker, National Institute of Mental Health, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72904.sa1](https://doi.org/10.7554/eLife.72904.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Charting Brain Growth and Aging at High Spatial Precision" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Chris Baker as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Bernd Taschler (Reviewer #1); Oscar Esteban (Reviewer #2); Todd Constable (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

As you will see, all three reviewers are very enthusiastic about this work and have some excellent suggestions for strengthening the manuscript that will require some additional analyses.

Essential revisions:

The comments from the three reviewers are highly consistent and identify three main areas where the manuscript can be improved to increase the strength of the results and the utility of the resource.

1) All reviewers noted concerns about the current evidence for generalization of the findings. The authors should include additional cross-validation tests across sites.

2) Related to point (1), the bulk of the data come from the UK Biobank. The implications and potential limitations caused by this should be more fully discussed, although the additional cross-validation analyses will help with this.

3) The manual QC is very impressive, but the whole process could be described in more detail to enable others to reproduce such a QC.

Reviewer #1 (Recommendations for the authors):

This is a highly valuable resource that will hopefully grow further in the future. The manuscript is well written and data and results are presented in a clear and detailed way. I especially commend the authors on making their code easy to run, understandable and truly accessible.

One aspect that, in my opinion, would strengthen the paper is the inclusion of a more comprehensive evaluation on unseen data across sites. With clinical applications in mind where a small, in-house data set is compared to the reference models, it would be useful to understand how much variation is to be expected from scanner/site differences alone. A comparison of the existing evaluation metrics with a scenario in which the models are trained on one set of sites (or even just UKB alone) and tested on a separate set of data that does not include any of the training sites would increase the interpretability of the current results.

Several recent studies have found recruitment and selection bias in the UKB with respect to the general population and even within the imaging cohort compared to the full 500k. Although briefly mentioned in the limitations, this could be expanded further by discussing recent findings.

Reviewer #3 (Recommendations for the authors):

While the numbers are probably sufficient that it doesn't matter – it seems that the train and test sets were only split once – and then the results presented. Proper form might be to randomly split the train/test set multiple times to obtain distributions. It would be much stronger statistically if this was repeated. If this was already repeated then it should be made clearer. The wording refers to train and test set(s) with sets being plural, but I could not find anything explicitly stating how many times this was repeated.

The data shown in Figure 1 might be better served by splitting this into multiple figures. In A it is impossible to read the y-axis. In C and D the caption states that the lines are centiles of variation but it doesn't say what centiles (for example do they match the centiles of pediatric growth charts 0.4th, 2, 9th, 25, 50th etc?) – this should be stated.

Figure 1C shows whole cortex results, while D shows subcortical. It would be nice to show data for some cortical brain regions – or even summarized for lobes instead of just whole brain.

For regions, it would be reassuring to see that the development curves for PFC for example, agree with the previous literature. Or even show that different regions have different temporal growth charts. Similarly, the work could be put in context with the work of Toga et al., Trends Neurosci, 2006 – mapping brain maturation. Or the work of Pigoni et al., Eur Neuropsychopharm, 2021 where they show (in a large sample) that cortical thickness changes in the temporal lobes can be used in classification of first episode psychosis. While the authors state that a thorough analysis of these curves is beyond the scope (and I agree) it would be helpful to have some text that confirms these curves (for healthy or diseased brains) agree with past literature.

Overall I am enthusiastic to see this work published.
