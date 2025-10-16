# Peer review - Round 1

Editors:
- Tadatsugu Taniguchi, University of Tokyo Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94899.3.sa0](https://doi.org/10.7554/eLife.94899.3.sa0)

Semenova et al. have studied a large cross-sectional cohort of people living with HIV on suppressive antiretroviral therapy and performed high dimensional flow-cytometry for analysis with data science/machine learning approaches to investigate associations of immunological and clinical parameters and intact/total HIV DNA levels (and categorizations). The study is useful in introducing these new methods and large data set and appears mostly solid, though some of the claims were incompletely supported by the modeling results. The authors have revised the text to fairly reflect their results, yet open questions remain about utility, particularly as to the value of categorical classification (vs continuous measurement) of reservoir size.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94899.3.sa1](https://doi.org/10.7554/eLife.94899.3.sa1)

On responding to the first round of reviews, the authors have nicely adjusted their wording and fairly describe the results of their study. Certain markers were identified for further investigation. Yet, an overall non-obvious relationship between immune markers and HIV reservoirs has been shown previously, and despite the attempt to leverage powerful ML algorithms, they are not magical and cannot reveal strong relationships that fundamentally do not exist. In addition, categorical classification is for now hard to interpret and the more powerful ML algorithms do not seem to outperform more classic regression methods. Therefore, it remains relatively hard to evaluate the utility of this kind of study.

Initial summary:

Semenova et al. have studied a large cross-sectional cohort of people living with HIV on suppressive ART, N=115, and performed high dimensional flow-cytometry to then search for associations between immunological and clinical parameters and intact/total HIV DNA levels.

A number of interesting data science/ML approaches were explored on the data and the project seems a serious undertaking. However, like many other studies that have looked for these kinds of associations, there was not a very strong signal. Of course the goal of unsupervised learning is to find new hypotheses that aren't obvious to human eyes, but I felt in that context, there were (1) results slightly oversold, (2) some questions about methodology in terms mostly of reservoir levels, and (3) results were not sufficiently translated back into meaning in terms of clinical outcomes.

Strengths:

The study is evidently a large and impressive undertaking and combines many cutting edge statistical techniques with a comprehensive experimental cohort of people living with HIV, notably inclusive of populations underrepresented in HIV science. A number of intriguing hypotheses are put forward that could be explored further. Data will be shared and could be a useful repository for more specific analyses.

Weaknesses:

Despite the detailed experiments and methods, there was not a very strong signal for variable(s) predicting HIV reservoir size. The spearman coefficients are ~0.3, (somewhat weak, and acknowledged as such) and predictive models reach 70-80% prediction levels, though of sometimes categorical variables that are challenging to interpret.

There are some questions about methodology, as well as some conclusions that are not completely supported by results, or at minimum not sufficiently contextualized in terms of clinical significance. Edit, authors have substantially revised the text.

On associations: the false discovery rate correction was set at 5%, but data appear underdetermined with fewer observations than variables (144vars > 115ppts), and it isn't always clear if/when variables are related (e.g inverses of one another, for instance %CD4 and %CD8).

The modeling of reservoir size was unusual, typically intact and defective HIV DNA are analyzed on a log10 scale (both for decays and predicting rebound). Also sometimes in this analysis levels are normalized (presumably to max/min?, e.g. S5), and given the large within-host variation of level we see in other works, it is not trivial to predict any downstream impact of normalization across population vs within person. Edit, fixed.

Also, the qualitative characterization of low/high reservoir is not standard, and naturally will split by early/later ART if done as above/below median. Given the continuous nature of these data it seems throughout that predicting above/below median is a little hard to translate into clinical meaning.

Lastly, work is comprehensive and appears solid, but the code was not shared to see how calculations were performed. Edit, fixed.
