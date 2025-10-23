# Peer review - Round 1

Editors:
- Arduino A Mangoni, Flinders Medical Centre Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68015.sa0](https://doi.org/10.7554/eLife.68015.sa0)

The major strengths of this paper are the use of a combination of relatively novel approaches/applications to the identification of important predictors for recovery after spinal cord surgery. These include various data reduction techniques such as dissimilarity matrices and a subject-centered topological network analysis to identify phenotypes.


---

# Peer review - Round 1

Editors:
- Arduino A Mangoni, Flinders Medical Centre Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68015.sa1](https://doi.org/10.7554/eLife.68015.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Topological network analysis of patient similarity for precision management of acute blood pressure in spinal cord injury" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Marcel Kopp (Reviewer #2).

The Reviewers and Editors have discussed the reviews with one another, and this decision letter is to help you prepare a revised submission.

Essential revisions:

1) Please provide information regarding what covariate adjustment was used in the confirmatory logistic regression models.

2) Can the authors provide an explanation of why they chose the specific forms of clustering to identify patient phenotypes? Other, perhaps simpler and more common unsupervised machine learning algorithms could have been used.

3) Are the results sensitive to the defined outcome of improvement of at least one AIS grade? What happens if this is increased to e.g. 2 grades?

4) Two different approaches to analysis were used – i.e. essentially clustering of some form and also logistic regression (using e.g. quadratic and spline functions). Can the authors comment on whether these 2 approaches can be used interchangeably or whether one would be preferred over to the other to answer the research questions of interest. What advantage does the clustering approach have in terms of the research question?

5) Why was a simple accuracy metric used and not e.g. AUC? Does the accuracy metric account for an imbalance in the outcomes?

6) The LOOCV accuracy was not that high suggesting a lot of other factors might influence outcomes. Is the accuracy really high enough to support the use of MAP being used by clinicians for decision making and/or interventions to control MAP during surgery?

7) What variables were used for the LASSO. The prediction accuracy again seems very low for high-dimensional dataset.

8) Only one dataset was used without splitting the data into a training and validation dataset. Are similar results for the topological network analysis obtained if the data is split for training and validation?

9) What was the modularity of the final network and does it suggest significant clustering?

10) Why was days from surgery to discharge used in the logistic regression models? Might it not be considered a mediator rather than a confounder – and how does its exclusion from the model influence the result?

11) The limitations are mentioned but not discussed or justified. This leads to the following questions: a) Why was the lesion level not included in the analysis? and b) Why did the authors only analyze MAD values during surgery? Because the analysis of MAP data from the ICU period published elsewhere showed similar results regarding the lower limit of MAP, wouldn't it be of interest to know how much overlap there is between the populations with critical MAP values during surgery and during stay in the ICU?

12) Introduction: Neither hypertension nor hypotension following acute SCI has been conclusively demonstrated to impact neurological recovery. Instead, guidelines and more recent work are based purely on observations and post-hoc regression analyses. While the purported mechanism for repeated hypotensive episodes is clear, readers may benefit from at least a brief description of why both hypertension and hypotension could plausibly be important (aside from the fact that, again, non-causal observations demonstrated a relationship in the author's prior work).

13) AIS scores: Based on Table 1 most patients were discharged within 2 weeks after injury. The neurological exam is not so reliable at this point. This is a big limitation of the current work. Although a six month follow-up would be ideal to determine whether neurological recovery occurred, the authors should at least mention this.

14) All the analyses seem to have been conducted on an AIS change. The authors should demonstrate that their analysis holds for a more linear measure of recovery (e.g., total motor score).

15) Based on Figure 2 – Supplement 2, it is difficult to ascertain whether clusters contain a higher proportion of individuals that show an AIS improvement, and those individuals tend to have a MAP > 80 and < 100, is due to these clusters having individuals who were less severe to begin with (i.e., C,D,E) and therefore less likely to be hemodynamically unstable. One way to answer this would be to examine AIS A patients in a separate analysis and determine whether these findings hold. Because, the alternative explanation here is that this analysis is effectively finding a proxy for initial injury severity (i.e., more severe, more hemodynamically unstable) – and not that hemodynamic instability per se is the problem. Another analysis that could help complement this work and avoid this confound would be to use total motor score as the outcome instead of AIS conversion.

16) Logistic regression – Based on Figure 2p the overall trend looks more to be that higher MAP = > Pr(δ AIS grade > 0). The exception is only 2 data points on the top end. It is difficult to determine how robust the notion is that there is a 'too high' component to this data. Indeed it seems that a linear model does quite well for this analysis as well. Please see my comment below but this should be addressed as the concept of also having a 'top cutoff' is an extremely important clinical feature here.

17) Time outside MAP – The authors use an approach that systematically increases their window in both directions to find their optimal range of 76-104. However, what happens if you then hold 76 and only increase on the upper end? Does this rapidly degrade the relationship? If not, again this would suggest that the evidence for a top end cut-off is not as strong. While I understand the authors briefly looked at this (methods) it seems worth exploring further as this is a critical point for clinical management. I do not see a good reason that the time outside the threshold can not at least be plotted to determine this relationship.

18) Data availability – The code and analysis should be made available to the reviewers. It is impossible to determine the accuracy of this type of analysis without it.

19) Discussion – It seems that the authors should discuss the confound of injury severity being linked with worse hemodynamic instability, and also worse neurological recovery. It would be helpful to include some of the suggested analyses to convince the readers that this confound does not explain the results since it is the most likely alternative explanation.

Reviewer #1:

The major strengths of this paper are the use of a combination of relatively novel approaches/applications to the identification of important predictors for recovery after spinal cord surgery. These include various data reduction techniques such as dissimilarity matrices and a subject-centred topological network analysis to identify phenotypes. The weaknesses include its relatively modest prediction accuracy and the lack of internal and external validation in the primary network analysis.

Reviewer #2:

The major strength of the paper is the statistically highly advanced analysis based on high-resolution data from acute SCI care, i.e. intra-operative mean arterial blood pressure (MAP) and heart rate. The steps of data exploration and analysis and their results are presented transparently. In conjunction with the results of previous studies suggesting that the lower threshold of MAP levels to be avoided in the ICU is about 75 mmHg, the main results of the this study imply that the minimum target MAP may be lower than the currently recommended 85 mmHg also during surgery. The analysis, which combines machine learning algorithms with logistic regression models, may serve as a template for data-driven studies also on other aspects of critical care in the field of SCI.

A weakness of the study is that some of the baseline neurological criteria were not included in the analysis. In particular, the neurological level of injury could be important for the research question, because the degree of blood pressure dysregulation also depends on the lesion level. The authors mention this limitation but do not explain why they accept it. Another limitation is the relatively small sample size of the study. Therefore, the specific results might have limited generalizability. Nevertheless, the study is an essential contribution to the readjustment of MAP threshold recommendations in the very acute stage of SCI and provides key information for the design of future precision medicine studies.

Reviewer #3:

The authors present a nice analysis of the relationship between intraoperative mean arterial pressure and neurological recovery after spinal cord injury, and I appreciate the opportunity to review this work. In general, the results are interesting and largely in line with a growing body of evidence that supports the use of hemodynamic monitoring in the acute phase after injury. There are three primary points with regard to this work that the authors can and should address prior to publication.

First, the exclusive use of AIS conversion as the outcome of neurological improvement is not ideal. Demonstrating that these findings are robust to other more continuous measures of neurological improvement such as motor/sensory scores would go a long way towards demonstrating that this finding is robust.

Second, the authors state in the discussion that MAP management may only be needed for <5 days post-injury. There does not appear to be strong data in the paper to support this point. Either more data should be added that supports this contention or this point should be removed.

Third, although the authors briefly discuss the confound of injury severity being linked to hemodynamic instability, the results are compelling enough at the moment to discount a role of injury severity. Individuals with more severe injuries will necessarily have greater hemodynamic instability, particularly in the hyperacute and acute phase after injury. These same individuals are also less likely to exhibit a conversion of their AIS score (e.g., individuals with AIS A/B). The authors control for this in some of their analyses (e.g., including a coefficient of initial AIS score in their regression models), yet their results seem to indicate that the clusters of individuals they focus on are indeed those with less severe injuries to start with. Demonstrating that injury severity is not a factor would require an analysis of only individuals with AIS A injuries at admission. This would be very compelling and enhance the impact of this work.

Overall, this is an interesting analysis that will be of use to the field.
