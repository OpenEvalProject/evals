# Peer review - Round 1

Editors:
- Peter Rodgers, eLife United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60586.sa1](https://doi.org/10.7554/eLife.60586.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Task specialization and its effects on research careers" to eLife for consideration as a Feature Article. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by the eLife Features Editor (Peter Rodgers). The following individuals involved in review of your submission have agreed to reveal their identity: Allison Morgan (Reviewer #1).

The reviewers and editors have discussed the reviews and we have drafted this decision letter to help you prepare a revised submission. We hope you will be able to submit the revised version within two months.

Summary:

Using data on over 6M publications and 200K authors, the authors aim to consider how prominent various scientific archetypes are across researchers' careers and whether there are gendered differences in these roles. The main takeaways are: (i) contributions shift over career stages, due to who is performing experiments/analyzing data (junior/early-career) or conceiving experiments/writing (mid/late-career); (ii) researchers who present as leaders in their early-careers are more likely to remain; (iii) women are less likely to appear in the leader archetype across career stages (and more likely to be in specialized/supporting roles with typically lower productivity). However, there are a number of points and concerns about the work that need to be addressed to make the article suitable for publication.

Essential revisions:

1) Title: I worry that the phrase "its effects" implies a causal relationship that is not warranted by the analysis presented in the paper. Possibly something like: "Task specialization across research careers" is a little more accurate.

2) Please explain why Bayesian analysis was used to determine which of the variables in the dataset predict the Contributorship categories: to me the use of machine learning with boosting classification would seem more appropriate.

Also, please explain how various of the criteria used in the analysis were chosen (eg, the definitions of career stage, the number of iterations used in the Bayesian analysis, the ICMJE criteria included in the analysis).

3) I would like to see the analysis of Contributorship and career stages across years, if possible, to see if there is a change in trends over the years, especially for the gender differences and career advancement.

[Note from the Features Editor: Addressing this point is optional]

4) The low error rates in the Bayesian analysis seem very impressive, but to interpret them better I'd appreciate some notion of recall since (I think?) most authors would not fill a given role. I also assume a cutoff value was chosen from the predicted probability, but this was not explicitly said. These suggestions would likely not impact the conclusions of the work, but would aid in reproducibility.

5) I do not understand why authors use Spearman correlation coefficient because you were investigating an association between nominal/categorical variables and ordinal variables. Please use appropriate measures of association for variables of interest or omit this analysis completely.

6) In subsection “Bayesian network model for predicting contributorship”: The strength of the arcs, i.e., relationships between variables, has been investigated using the bootstrap procedure, with 50 repetitions. Only the arcs that were present in 80% of the repetitions have been considered and are depicted in Figure 2B.

Is this standard procedure? If it is, please give a reference, and in case it is not please explain what is the rationale behind choosing those criteria.

There are several places where I believe the authors should provide statistical hypothesis testing and state the actual differences. These are documented below:

7) In subsection “Career paths, productivity and citation impact”: Figure 5B/C doesn't lead me to believe the differences in publications or citations are meaningfully different across career stages, but the text alludes to differences. Mentioning whether these are supported by statistical tests would strengthen your claims. Also, please expand the caption for figure 5 to fully explain what is being plotted in panels B and C.

8) Figure 6: A significance test across the proportions for men and women would be valuable again, since the text draws our attention to them.

9) Figures 6 and 7: Please include confidence intervals so that the reader can assess whether there are differences between groups.

10) You argue that there are differences in proportions between men and women in archetypes, but I wonder whether that is really due to the fact because in the previous paragraph you state that is more likely for researchers who are leaders in early stages to come to the late stages of career. I wonder what the more predictive factor for career advancement is - gender or specialization in early stage - and it would be good if the authors could resolve this issue by using some prediction model.

Also, you state that the shares of leader archetype are consistently lower for women compare to the men. Can you please test this using some kind of test of proportions (chi square for example) and also report the 95% confidence intervals for proportions?

Also, what does the distribution of \alpha (weights on archetypes) look like for most researchers? Is it easy to distinguish which archetype researchers fall into at a given career stage? This seems slightly important to the interpretation of the results.
