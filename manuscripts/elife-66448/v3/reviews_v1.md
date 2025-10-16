# Peer review - Round 1

Editors:
- Talía Malagón, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66448.sa1](https://doi.org/10.7554/eLife.66448.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This interesting phylogenetic analysis of a mumps outbreak in Washington will be of interest to a wide audience, especially those working at the intersection of pathogen genomics and public health. An array of classic and novel phylogenetic approaches supports the conclusions that mumps was introduced several times in Washington during the outbreak, and that the Washington Marshallese community was particularly at risk of mumps infection and transmission despite high vaccination coverage. Consultation with a community health advocate from the affected communities helps contextualize the results.

Decision letter after peer review:

Thank you for submitting your article "Repeated introductions and intensive community transmission fueled a mumps virus outbreak in Washington State" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Miles Davenport as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Please rephrase conclusions regarding the role of age and vaccination to indicate the effect is inconclusive given the low power of the study/small sample size.

2. Figure 2 is difficult to read. A different color scheme may make this figure more understandable.

3. Please compare the age distribution of sampled cases vs outbreak cases in either supplementary table 2 or 3, this would help better convince readers that the sample is representative of the outbreak cases.

4. Elaborate on the decision to include tips on an internal node as the measured variable as opposed to tips with a branch length of a certain distance.

5. Rephrase heading on line 338

6. Additional contextualization of the problem of sampling bias and how this approach is different may help strengthen the methodology presented in the paper.

7. There were several other mumps outbreaks in the United States in the same 2016-2017 time period. Some discussion about Washington state particularities that prevented mumps transmission outside of the Marshallese community would be warranted.

Reviewer #1 (Recommendations for the authors):

I cannot comment much on the sequencing and phylogenetic analyses as this is not my area of expertise, but I can comment on the epidemiological analyses:

• There is an overreliance on p-values in the interpretation of the logistic regression in Table 1. There is no consideration of the fact that the study does not have an adequate sample size to assess the effects of variables other than community status. I would recommend the authors do a post-hoc sample size power calculation, not necessarily to put in the article, but to convince themselves of whether they have the statistical power to assess the impact of vaccination and age. Basically, their logistic regression model is suggesting that in fact we cannot exclude the possibility that vaccination status and age may potentially have very strong effects on transmission (point estimate ORs of 2.21, 0.46, or 0.30, in other words over a doubling or a halving of the odds, which would be considered by many to be an important effect size). The only reason that the analysis has enough statistical power for community status is because the odds ratio is enormous and the prevalence of Marshallese samples is very high. Please read Amrhein V, Greenland S, McShane B. Nature. 2019 Mar;567(7748):305-307 for further discussion on this topic. I would suggest addressing this issue by:

– Mentioning low statistical power to assess the effects of age and vaccination as a limitation of this analysis

– When discussing the results for age and vaccination status, I would recommend using the suggestion of Amrhein et al. and to discuss the point estimate and confidence intervals rather than commenting on their non-statistical significance. (e.g. instead of "Neither age nor vaccination status were significantly associated with the presence of downstream tips in the tree", say instead that while those with unknown vaccination status were more likely to have descendants in the tree than those with known up-to-date vaccination, the confidence interval could not exclude a null or positive association between vaccination status and having tree descendants).

– The conclusion the authors should reach in the abstract and discussion is not that "Neither vaccination status nor age were strong determinants of transmission", but rather that while age and vaccination status might be associated with transmission, the authors did not have enough statistical power to estimate their effect (i.e. the confidence intervals are very wide and cannot exclude either no association or inverse associations).

• I find the parameterization of age very unusual, in general what is more often used for continuous variables is centering the variable around the mean or mode rather than normalizing. I am not convinced that age as a continuous variable is the best way to parameterize age for this analysis. There is no reason to believe that age would necessarily have a linear effect on transmission. Social networks and contacts do not change linearly with age but probably in a more segmented manner as individuals age into different life stages (school, workforce, retirement). Waning vaccine immunity is also possibly not linear with age. This is just a suggestion, but I think it would potentially be more fruitful and maybe yield higher statistical power in this case to categorize age dichotomously as either children (<20y) or adults (>=20y) based on different social networks in children vs adults. However, there may be other cutpoints that fit the data better and that could be explored. Otherwise, some justification for the parameterization of age would be nice.

• Please compare the age distribution of sampled cases vs outbreak cases in either supplementary table 2 or 3, this would help better convince readers that the sample is representative of the outbreak cases.

• Figure 2: Please make the data for Washington state more obvious, for example by restricting an entire color shade such as blue. Currently it is very difficult to distinguish between Georgia, Virginia, Manitoba, Washington, Massachusetts, and North Dakota. It is also not clear from the legend what a grey node represents.

Reviewer #2 (Recommendations for the authors):

The input from community health advocates is a strength that could be better highlighted in the discussion. It is unclear which potential causes (possibly all of them) are corroborated by the lived experiences of the individuals in the Marshallese community in WA.

The new test for descendants in the divergence tree is a useful method that is likely to be adopted in other studies. It would be nice if the authors could elaborate very briefly on the decision to include tips on an internal node as the measured variable as opposed to tips with a branch length of a certain distance. Is this decision based on the substitution rate and serial interval of Mumps and if applied by others should it be adjusted based on the pathogen and/or sampling scheme (e.g. Intensely sampling a super spreading event would show a large number of tips of one type at the base of 1 transmission chain which is different than finding many tips with descendants spread throughout the tree)?

The wording in the heading on line 338 is confusing.

Is it known, or suspected from interviews, if members of the Marshallese community are more closely connected through social contacts with each other than they are with the wider public? This seems like an implicit assumption, but very likely given the outbreaks in WA and AR.

Lines 667-668 in the methods mention 27 "states" were used in the phylogeographic reconstruction. The main text and Figure 1 mention 26.
