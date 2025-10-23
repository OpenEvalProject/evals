# Peer review - Round 1

Editors:
- Jennifer Flegg, The University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65133.sa1](https://doi.org/10.7554/eLife.65133.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper provides relevant findings of the effects of changing malaria burden on low birth weight using a novel design-based causal inference approach (i.e., a two-step matching procedure as nonparametric data preprocessing in a difference-in-differences design). There are a lot of things to like about this paper, such as its creative design, its extensive data collection effort, and its important results for the policy and health literature. The research topic is well-motivated and of importance to the malaria research community. The statistical methods will be applicable in other contexts.

Decision letter after peer review:

Thank you for submitting your article "Relationship between changing malaria burden and low birth weight in sub-Saharan Africa" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jennifer Flegg (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Summary:

This paper provides relevant findings of the effects of changing malaria burden on low birth weight using a novel design-based causal inference approach (i.e., a two-step matching procedure as nonparametric data preprocessing in a difference-in-differences design). There are a lot of things to like about this paper, such as its creative design, its extensive data collection effort, and its important results for the policy and health literature. The research topic is well-motivated and of importance to the malaria research community. The statistical methods will be applicable in other contexts.

Essential Revisions:

1. To answer the research question, the authors make use of the fact that "while the overall prevalence of malaria has declined in sub-Saharan Africa, the decline has been uneven, with some malaria-endemic areas experiencing sharp drops and others experiencing little change" (page 2). However, they never discuss if that heterogeneity can be explained by hidden variables that could also predict the outcomes. In other words, an unobserved factor u could be explaining both the uneven reduction of malaria in certain areas and birth weight. I understand that it is impossible to provide a final answer to this concern, but I would expect some discussion about it. Probably a sensitivity analysis or the amplification of a sensitivity analysis could help to shed some light on this issue.

2. The authors combine two strategies to answer the research question: difference-in-differences and matching. The authors justify combining both strategies by claiming that matching can make the parallel trend assumption more likely to hold. Even though this point makes sense, it would require a better explanation. The main assumption behind a DID is the outcome in treated and control groups would follow parallel trends in the absence of the treatment. As a result, both observed and unobserved characteristics should also follow a common trajectory across both the control and treated groups before the intervention. Matching can help to address imbalances in terms of observed covariates, however, it will require authors to make assumptions about unobservables that are not discussed in the paper. As in my previous comment, a sensitivity analysis might help to address this concern or at least a discussion to better understand under what conditions matching can credibility enhance a difference-in-differences design.

3. Locations are different across time within the same country because the DHS sample different places when constructing representative samples. This is not a problem per se when implementing a DID. However, it might become problematic if the sampling variability is generating imbalances in only one group and therefore those imbalances are not following a common trajectory, which might produce biased results when implementing the DID. In other words, it is not an issue if sampling variability is changing both the control and treated groups in the same direction, but it is going to be an issue if that is only happening for one of the groups or for both groups but in opposite directions. Matching can provide a direct solution to this problem since now we can attribute the changes in outcomes to the intervention and not to a different group composition. I would recommend authors to discuss how matching can help to improve difference-in-differences design when the units of analysis are not the same across time.

4. DID will be biased if there is an event that is occurring at the same time as the intervention, and therefore that is only affecting the treated group after the treatment (i.e., selective maturation). For example, places experiencing a malaria prevalence decline might also experience other positive health outcomes that can contribute to explaining birth weight. I would encourage authors to discuss this possibility.

5. There has been updated estimates of pf parasite rates that include estimates up to 2017 which I think should be used.

6. The choice of "early" and "late" years was a little arbitrary – is there any justification that can be provided or a sensitivity on these definitions?

7. It wasn't clear how the sociodemographic covariates were chosen – is this list (on page 7) an exhaustive list? If not, how were these covariates chosen?

8. In how the model in Equation (1) is presented, that the mixed effects model was fitted in a frequentist setting? Eg there is a reference later to confidence intervals (not credible intervals). I find the change of using a Bayesian approach in the earlier steps of the methodology to using a Frequentist approach quite strange and would suggest that a consistent approach is used throughout.

9. One of the main findings is about the reduction in the rate of low birth weight, but this is not (at the 95% confidence level) significant based on the modelling. While this is mentioned in the Discussion of the paper, I think this should be more up-front in the abstract/results.

10. Can you share on github or similar?

Reviewer #1:

This paper presents a statistical approach to quantify the relationship between changing pf malaria and the rate of a low-birth weight babies in Africa. A major strength of the work is that the methodology brings together multiple data sources and statistical methods into the one analysis. The authors have achieved their aims and the results support their conclusions. The research topic is well-motivated and of importance to the malaria research community. The statistical methods will be applicable in other contexts.

1. There has been updated estimates of pf parasite rates that include estimates up to 2017 which I think should be used.

2. I thought the choice of "early" and "late" years was a little arbitrary – is there any justification that can be provided or a sensitivity on these definitions?

3. It wasn't clear how the sociodemographic covariates were chosen – is this list (on page 7) an exhaustive list? If not, how were these covariates chosen?

4. It seems to me, in how the model in Equation (1) is presented, that the mixed effects model was fitted in a frequentist setting? Eg there is a reference later to confidence intervals (not credible intervals). I find the change of using a Bayesian approach in the earlier steps of the methodology to using a Frequentist approach quite strange and would suggest that a consistent approach is used throughout.

5. One of the main findings is about the reduction in the rate of low birth weight, but this is not (at the 95% confidence level) significant based on the modelling. While this is mentioned in the Discussion of the paper, I think this should be more up-front in the abstract/results.

Reviewer #2:

The authors study the effects of a malaria prevalence decline on low birth rates. To achieve this goal, they use data from 19 countries in sub-Saharan Africa. This manuscript's main strengths are the data collection efforts (merging annual malaria prevalence, demographic and health surveys, and geographical information) and the use of a novel methodological approach (combining recent developments in optimal matching with a difference-in-differences design). Some weaknesses or aspects that could be improved are the lack of discussion about possible biases such as the presence of unobserved factors that could explain the uneven decline in malaria, the role of sampling variability when using survey data to construct a difference-in-differences design, and the role of selective maturation. Regardless of these previous points, the paper makes clear contributions to the applied causal inference literature by illustrating how it is possible to enhance a traditional difference-in-differences design, and to the health and policy literature by showing the effects of malaria on a crucial development outcome.

I have four main comments/suggestions for the authors:

1. To answer the research question, the authors make use of the fact that "while the overall prevalence of malaria has declined in sub-Saharan Africa, the decline has been uneven, with some malaria-endemic areas experiencing sharp drops and others experiencing little change" (page 2). However, they never discuss if that heterogeneity can be explained by hidden variables that could also predict the outcomes. In other words, an unobserved factor u could be explaining both the uneven reduction of malaria in certain areas and birth weight. I understand that it is impossible to provide a final answer to this concern, but I would expect some discussion about it. Probably a sensitivity analysis or the amplification of a sensitivity analysis could help to shed some light on this issue.

2. The authors combine two strategies to answer the research question: difference-in-differences and matching. The authors justify combining both strategies by claiming that matching can make the parallel trend assumption more likely to hold. Even though this point makes sense, it would require a better explanation. The main assumption behind a DID is the outcome in treated and control groups would follow parallel trends in the absence of the treatment. As a result, both observed and unobserved characteristics should also follow a common trajectory across both the control and treated groups before the intervention. Matching can help to address imbalances in terms of observed covariates, however, it will require authors to make assumptions about unobservables that are not discussed in the paper. As in my previous comment, a sensitivity analysis might help to address this concern or at least a discussion to better understand under what conditions matching can credibility enhance a difference-in-differences design.

3. Locations are different across time within the same country because the DHS sample different places when constructing representative samples. This is not a problem per se when implementing a DID. However, it might become problematic if the sampling variability is generating imbalances in only one group and therefore those imbalances are not following a common trajectory, which might produce biased results when implementing the DID. In other words, it is not an issue if sampling variability is changing both the control and treated groups in the same direction, but it is going to be an issue if that is only happening for one of the groups or for both groups but in opposite directions. Matching can provide a direct solution to this problem since now we can attribute the changes in outcomes to the intervention and not to a different group composition. I would recommend authors to discuss how matching can help to improve difference-in-differences design when the units of analysis are not the same across time.

4. DID will be biased if there is an event that is occurring at the same time as the intervention, and therefore that is only affecting the treated group after the treatment (i.e., selective maturation). For example, places experiencing a malaria prevalence decline might also experience other positive health outcomes that can contribute to explaining birth weight. I would encourage authors to discuss this possibility.
