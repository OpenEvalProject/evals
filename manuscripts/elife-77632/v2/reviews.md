# Peer review - Round 1

Editors:
- Jamie Justice, https://ror.org/0207ad724 Wake Forest School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77632.sa0](https://doi.org/10.7554/eLife.77632.sa0)

The key contribution of this study is to evaluate the longitudinal change in frailty indices by tracking both accumulation of damage and repair of deficits (damage and repair transition rates), using a sophisticated mathematical modeling and a translational approach that spans mice and humans. A second key achievement of this study is to evaluate change in frailty indices and damage and repair transition in interventions that improve health in mice. Collectively this advances progress in translational geroscience by providing new insight regarding how we measure biological age that can aid assessment of aging-relevant interventions. The authors have provided extensive details that support the research frameworks presented in this report.


---

# Peer review - Round 1

Editors:
- Jamie Justice, https://ror.org/0207ad724 Wake Forest School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77632.sa1](https://doi.org/10.7554/eLife.77632.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Measurements of damage and repair in aging mice and humans reveals that robustness and resilience decrease with age, operate over broad timescales, and are affected differently by interventions" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Carlos Isales as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Konstantin Arbeev (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. A key assumption is that an increase in FI is equivalent to a rise in damage, but this relationship is unknown and may ignore a number of important biological processes – including the dynamic interplay between both damage, compensatory processes/feedback, and protection/fitness. There is lingering concern that this may be over-conceptualized, and the true relationship between frailty index and damage is unknown. This should be addressed in the manuscript rationale. Language in discussion and conclusions should be tempered.

2. Additionally, 'repair' assumes a biological process to restore homeostasis, but in this manuscript refers to a switch from out-of-range to a return to in-range for variables and cut-points that are not defined in the manuscript. The issue of measurement error in individual components that switch from out-of-range to in-range or vice versa needs to be addressed. Variables and cutpoints must be detailed. Authors should also distinguish biological processes from mechanical definitions in rationale and discussion.

3. Some variables may represent irreversible processes of deterioration (e.g. loss of whiskers, kyphosis, palpable/visible tumor, etc.), while others may be more dynamic or have cutpoints with unknown validity for in vs out of range. It is anticipated that only a subset of those queried contributes to 'repair' while others irreversibly increase over time. This would challenge the validity of 'repair' models (and interpretation of Figure 5). As above, please include details on specific variables and their cutpoints. Please indicate which of these variables change dynamically over time – with evidence of both 'deficit' and 'repair' – versus those that are irreparable by definition or thresholds.

4. Additional conceptual issues are present in mouse models given typically shorter time scales and acute stress stimulus – in addition to the issues above. Most reviewers have requested additional details to support assumptions made in mouse models.

5. Detailed total follow-up time/time-course in both animal and human data is needed. For example, statistics on total follow-up times in human data. This is important for relative time courses across species and how many times deficits can be damaged/repaired within a given time or relative period of life.

6. Concern over the impact of selection bias/survivor bias in models (especially mice). Please address in the model and discussion.

7. Abstract requires clarity. Data, tests performed, and specific results should be presented as appropriate.

8. Please address specific recommendations and editorial suggestions made by each reviewer below.

Reviewer #1 (Recommendations for the authors):

I commend the authors for their efforts. The modeling of longitudinal data is an important area in aging that needs more attention. I also like the approach at a conceptual level and think the stratification of resilience vs robustness could be quite valuable. I appreciate the idea of making models that are generalizable and think the approach is most appropriate for the human data, but I think more attention needs to be paid to the technical and biological aspects of the variables being modeled for the mouse data.

General comments:

The mouse frailty index is a very useful tool for efficiently measuring the organismal state in large cohorts. A tradeoff for quickly measuring a broad range of health domains is that the individual measurements are low resolution and involve inherent subjectivity (which may be considered measurement error). It is very important to keep this in mind when using individual scores from the index. Some transitions are due to random measurement error and I believe this is especially likely with decreases (or 'resilience' transitions).

While I find the 'robustness' modeling quite interesting, I am skeptical as to how valid the 'resilience' modeling is. The first reason for this is that I do not believe many of the deficits in the mouse index are reversible under normal physiologic conditions. For example, it is exceptionally unlikely for a palpable/visible tumor to resolve in an aged mouse, thus any reversal that was observed must be due to random measurement error. I would conservatively estimate that the following components are not truly reversible in the contexts in which they were studied here: alopecia, loss of fur color, loss of whiskers, tumors, kyphosis, hearing loss, cataracts, corneal capacity, vision loss, rectal prolapse, genital prolapse.

When used as a sum of its components, the mouse frailty index is highly robust to these measurement errors as demonstrated many times in the literature. However, breaking apart the index into its components compromises this robustness, and I am not aware of literature which has validated the use of individual components of the index. How do the authors account for the measurement error which is inherent to the individual components of the mouse frailty index, and how might this error affect their models? I would be particularly concerned with how this would affect the models in figure 5.

Additionally, the authors state that "the observed damage is thought to occur due to natural stochastic transitions." I do not necessarily agree with that characterization for many of the pathologies measured here. For example, I would not consider vision loss a stochastic transition but rather a gradual degenerative process. Stochasticity involves when it crosses a threshold that can be measured/detected by the researcher. The authors state the following assumption: "We assume these time intervals are small so that we use constant rates within each time-interval to approximate these integrals." Small is subjective and the time intervals are up to 2 months which is 7-10% of a mouse lifespan. Can the authors justify this assumption and/or discuss the implications of such an assumption to their models? The time scale should also be considered in the context of the specific measurements being taken.

My final high-level comment regards selection bias. As these studies progress and individuals die, the study population drastically changes. How do the authors' models account for this selection bias? Can the results of the modelling tell us anything about the nature of the populations as selection occurs? And finally, would there be value in performing this modeling as a function of "biological age" (ie. time to death) versus chronological age?

Specific comments:

The authors should specify which packages and versions were used for the development of their models. When I ran some of the scripts from Github they threw pandas warnings, leading me to suspect that I am not using the development versions. This is important if the authors expect future use of their models. I would encourage the authors to include package information both in the manuscript and on the Github.

I would recommend the authors be specific when describing their results. Many complex models and statistical tests are generated and it sometimes is unclear what is being referred to. For example, in the section "The acceleration of damage accumulation…" the statement "In mice, this is seen in every dataset and is significant at the indicated ages" is unclear what statistical test is being referred to. I would also recommend the authors be more precise in their result descriptions. For example, in the section "Interventions modify damage…" the statement "This curvature is strongly reduced…" is subjective and would be better supported by a description of specific statistical results.

The authors should be careful with the language used regarding wealth in the human dataset. Wealth is not an intervention. And wealth per se does not influence frailty as worded in methods. In these data wealth is a variable which is often associated with health outcomes including frailty.

In discussion: "…where female live longer but have higher FI scores than males." Female humans live longer but female B6 mice usually live shorter.

The citation the authors use for ELSA points to the database. PMID 23143611 also needs to be cited where the study and data collection procedures are described. It also seems like an omission to not cite PMID 31665163 which explores the relationship between various factors, including wealth, and frailty in the same dataset. I would also recommend the authors include a supplemental table with the specific mouse measurements and human questionnaire items that comprise the respective frailty indices.

The authors should provide more detail on the human frailty variables in the methods. I am assuming the binary responses to questions HEADLA and HEADLB were used, but this should be clarified/explicitly stated in the methods.

Comments on mouse pre-processing methods: In the mouse frailty index, 29 out of 31 parameters are measured on a [0, 0.5, 1] scale, with only weight and temperature using [0, 0.25, 0.5, 0.75, 1] scale, and it looks to me like the Schultz dataset still used [0, 0.5, 1] for these variables. So I don't find the statement "a single repair or damage transition can be interpreted as taking a step of size 0.25 on the fractional deficit scale" to be accurate because 29 out of 31 parameters only have the resolution to move in 0.5 unit increments.

Page 5: Authors state that "in each of the datasets, there is a strong decrease in repair rates and increase in damage rates with age (except in mouse dataset 2 for damage rates)." This doesn't seem to be the case for repair rates in humans entering ELSA study at age 50-70 (CI for p cross 0).

I am also somewhat unclear about the values for the rates in figure 2. In figure S2-1 the authors show that the model fits the data reasonably well. However, when looking at the rates in figure 2, the repair rates appear to be consistently higher than the damage rates. For example, in the Keller dataset males at 22 months, as frailty is consistently increasing, the modeled repair rate appears to be nearly double the modelled damage rate. Overall, the comparative magnitudes of the rates don't seem consistent with the mouse data, where there it is relatively rare to see a "population level" reduction in frailty at a subsequent timepoint (tends to stay the same or increase over time as shown in Figure 2S-2). Same comment for figure 4S2 human data.

Figure S2-1. It is hard to see the bars of the histogram in comparison to the dots. I would recommend making the dots smaller. Quantifying and plotting the deviation of observed vs posterior samples may also make interpretation easier.

The repair rate in the human 70-80 data (2d) appears to have a negative curvature, but this doesn't seem to be reflected in the second derivative plot (3e, teal line centered on zero).

I find the models in figure 5 somewhat difficult to interpret considering the extensive censoring that is occurring. Could the authors attempt a more 'plain language' interpretation of these curves considering the censoring? It seems like the interpretation would be that at 3 months after damage there is only a 75% probability of that damage being repaired? Also, could the authors interpret the drastic reduction in probability occurring in both damage and repair of the Schultz data at ~3 months?

Reviewer #3 (Recommendations for the authors):

I find the result on sex differences in effects of interventions on robustness and resilience very interesting so consider mentioning this in the abstract.

I would like to see more discussion on why deficits can be repaired, especially for some deficits which may seem to represent irreversible processes of deterioration. One example that is not trivial for me to understand (as I am not a specialist in mice) is the repair of the deficit "loss of whiskers." Do they just grow up again after a while? If they do, what constitutes the event of repair (just when they start growing again or when they are fully grown, assuming there is a measure for this)?

Some statistics on the total follow-up times in human data would be helpful. It can help put the estimates of repair/damage scales in the context to provide insight on how many times the deficit can potentially be damaged/repaired in the time period of data collection.

As you indicated in Methods, "The individuals selected from ELSA with wealth data do not have mortality data available, simplifying the model from the joint model used above for mice." In Results, you wrote, "This is a joint longitudinal-survival model, which couples the damage and repair rates together with mortality." This narrative should be changed then to reflect the fact that the joint model was only used in mice data.

Some readers may not be familiar with Bayesian methods so it would help provide in Methods some discussion on the selection of priors – is this a convenience/traditional choice or some other reasons? Also, some narrative on the sensitivity of results to a different choice of priors would be helpful, in my view.
