# Peer review - Round 1

Editors:
- Mark Jit, London School of Hygiene & Tropical Medicine, and Public Health England United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29820.028](https://doi.org/10.7554/eLife.29820.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Epidemiological and ecological determinants of Zika virus transmission in an urban setting" for consideration by eLife. Your article has been favorably evaluated by a Senior Editor and three reviewers, one of whom, Mark Jit, is a member of our Board of Reviewing Editors.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work in its current form will not be considered further for publication in eLife.

The three reviewers agreed that this is an interesting paper that has the potential to set a standard for ecological-epidemiological analysis of Zika outbreaks in these settings. However, we had serious misgivings about the model fitting process, interpretation of input data and lack of detail about some outputs. Partly as a result of this, we were not persuaded by the findings either.

If these methodological issues could be addressed, and the results can be used to substantiate a much more compelling and convincing story about Zika in Brazil then we would be willing to consider a revised manuscript as a new submission, which may be sent to the same reviewers. However, at this stage we cannot guarantee that we will review a revised manuscript.

If the technical issues can be addressed but the main hypotheses cannot be sustained, then we still think the manuscript has merit and would encourage submitting it to a more specialised journal.

The specific technical issues that would need to be addressed are the following:

a) Issues around the model fit

- The bimodal posterior distribution for infectious and incubation period in Figures 3C-D suggest there could be an issue with the model fitting. Two possibilities come to mind: either a lack of parameter identifiability in the model itself, or poor mixing of the MCMC chains. We would suggest testing for each of these. What do the pairwise correlations between the posteriors look like? What is the effective sample size of the MCMC outputs for each parameter? According to Table 4, there are 8 parameters estimated – what do the posteriors look like for the other 4?

- In Figure 4, the paper states that a stochastic model was used, but this wasn't mentioned in the Materials and methods. How was stochasticity incorporated? In addition, what time of year were the infections introduced in Figure 3C, and how was this value chosen? It seems to me timing would have a big effect on the number of cases, depending on whether introduction co-coincided with a high value of Re.

- In Figure 5A, we did not understand why the entire region of 0-8 cases was shaded blue, rather than just a line representing 4/1000 infections (or perhaps a boundary region to represent the posterior distribution of the estimate).

- Figure 5B is hard to interpret. The colour gradient seems to have been selected so that the line appears to go through the central microcephaly data point of 27, which makes it difficult to identify which regions produce high and low case numbers. It is also not clear what Figure 5C adds, other than normalising the results by the population size – in which case, should the numbers not be 6.2 times smaller (as the population is 620,000)?

- Why was a Poisson likelihood used for the observation process (equation 19), rather than, say, a binomial distribution?

- Why was the polynomial simplified to a 3rd degree one in equation 20? What effect did this have on the model in practice? Similarly, why was a 3rd degree polynomial used to fit the data in Figure 2—figure supplement 1? What impact could this assumption have had on model results?

- Should the observation rate be time-independent? One would expect that surveillance (and health care seeking) would improve as awareness about Zika increased.

b) Issues around interpretation of data and results

- We would have liked to see more discussion around estimates for the α and rho parameters, which control the extent to which environmental factors influence entomological dynamics. What contribution did humidity and temperature have? What are the implications for analysis in other settings, e.g. with stronger or weaker seasonal effects?

- In the fifth paragraph of the Discussion, it seems a stretch to suggest that the model estimates could be consistent with an autumn 2014 introduction. The lower 95% credible interval in Figure 3 is given as 2nd Jan 2015. What proportion of the posterior density falls within the range of dates implied by phylogenetic data?

- The context of the results is seriously misleading about the epidemiology of ZIKV in the rest of Brazil, specifically comparing 2015 to 2016. The state of Bahia is unique in that substantial surveillance was done in 2015. Zika did not become nationally reportable until January 2016, when reported case numbers increased substantially. From both microcephaly reports and anecdotal information, however, it is clear that massive outbreaks occurred in other states in 2015 (e.g. Pernambuco). This is not a problem with the model per se, but it is a big limitation to the conclusion that FSA was different from the rest of Brazil, (e.g. Figure 1A; Results, second paragraph and fourth paragraphs; Discussion, second paragraph). These sections should be rewritten to specifically address the uncertainty in national reporting (almost complete), remove national versus FSA comparison of the epidemiology, and highlight how this model and other models could tell us something about what likely happened in other places. We see that as one of the strengths of this approach and it is not explored at all.

- The finding about infants is notable, but also susceptible to a clear bias. It should be clearly noted that there may be an increased probability of reporting infants for whom care is often prioritized, both by families who would seek it and institutions who would provide it. This likely increased even more after recognition of the association with microcephaly. Furthermore, this dataset may offer a unique opportunity to assess changes in reporting as that became clear. This would be true for both infants and women of reproductive age.

- The information on microcephaly and GBS was insufficient. In the Introduction, it is stated that both were coincident with ZIKV incidence, but that seems unlikely given that both tend to lag behind incidence. These curves should by shown and discussed more specifically as this is a key component to understanding generalizability and the reliability of the data being used.

- There should be a bit more context of other work on ZIKV and climate; it's not accurate to say "the effects of local climate variables, such as temperature and rainfall, have not yet been explored in relation to Zika transmission." That's true in some ways, but not that generalizable. A number of studies are already cited, e.g. Bogoch et al., 2016; Zhang et al., 2016; Perkins et al., 2016; Messina et al., 2016. This manuscript should point out what is unique here.

- The observation rate estimate is very low. Lower than both Yap and French Polynesia. Is there other evidence that supports such a low rate? Limited surveillance? Is it alternatively possible that the epidemic was spatial heterogeneity actually resulted in a smaller epidemic that had a higher reporting rate, lower attack rate, yet nonetheless produced herd immunity effects?

- There should be more discussion about the risk of microcephaly. The comparisons to French Polynesia and Yap are great but there is a lot of other work that has been done, especially clinical studies: https://www.ncbi.nlm.nih.gov/pubmed/26943629 and https://www.ncbi.nlm.nih.gov/pubmed/27960197. It is especially important to understand why the estimates in this manuscript may be on the very low end of what is being reported elsewhere in studies specifically aimed at measuring that risk.

- The analysis suggests that most susceptibles become infected and then immune soon after the first wave of the epidemic in 2015. The second wave in 2016 has a much lower attack rate with a higher proportion of infants. However, there is potential for a new outbreak some years in the future (the exact time is difficult to determine because the x-axes in Figure 4 are incorrectly labelled I think). It would be useful to show the age distribution and predicted microcephaly incidence related to the later outbreaks. If these occur mainly in young children born after 2015 then the public health relevance may be minimal. This has wider implications – does it imply that the long-term public health impact of Zika is minimal once the virus has been established as an endemic childhood infection? These are obviously very large claims that are probably unsustainable from the model in its current state, but without further clarity about results they are obvious extrapolations that readers may make.

c) Issues around reproducibility

- As is normally the rule with eLife modelling papers, the model code, input data and results (including MCMC samples from the converged joint posterior distribution) needed to reproduce the figure should be included as supplementary data files. Public data from cited online sources may be moved, edited or removed in future, so it is important to include everything required to reproduce the descriptive and modelling analysis with the paper itself.

Reviewer #1:

This manuscript fits a model with entomological, epidemiological and climactic variables to data on Zika cases during the 2015/16 outbreaks in one city in Brazil. The model suggests that most susceptibles were infected during the 2015 wave which led to lower incidence in the 2016 wave, and would prevent further epidemics till some years in the future.

Some questions:

1) The analysis suggests that most susceptibles become infected and then immune soon after the first wave of the epidemic in 2015. The second wave in 2016 has a much lower attack rate with a higher proportion of infants. However, there is potential for a new outbreak some years in the future (the exact time is difficult to determine because the x-axes in Figure 4 are incorrectly labelled I think). It would be useful to show the age distribution and predicted microcephaly incidence related to the later outbreaks. If these occur mainly in young children born after 2015 then the public health relevance may be minimal. This has wider implications – does it imply that the long-term public health impact of Zika is minimal once the virus has been established as an endemic childhood infection?

2) However, it is not clear to me exactly how the model fit works, e.g. is the age dependent notification data even used or just the aggregated counts? It would be useful to give the actual likelihood function being used as equation (Cuong et al., 2011) in the appendix is too general (e.g. we aren't told exactly what yi or di are).

3) The relationship between transmission and climactic variables is established via a set of mechanistic equations linking variables governing vector life cycle with climate. While this is sophisticated, it would be useful to see a more conventional multi-variable regression approach, just to ensure that some obvious relationship has not been lost in the detail.

4) Should the observation rate be time-independent? One would expect that surveillance (and health care seeking) would improve as awareness about Zika increased.

5) In Figure 4, it is not clear whether the x-axis in panels A and C are in days or years.

Reviewer #2:

The authors present a transmission modelling analysis of Zika in Feira de Santana, Brazil. I think their broad approach is an important one – combining environmental data in a mechanistic model has the potential to reveal some valuable insights into Zika epidemiology. However, I had some concerns about the robustness of the model estimates, and interpretation of the results.

I have the following comments:

- The bimodal posterior distribution for infectious and incubation period in Figures 3C-D suggest there could be an issue with the model fitting. Two possibilities come to mind: either a lack of parameter identifiability in the model itself, or poor mixing of the MCMC chains. I would suggest testing for each of these. What do the pairwise correlations between the posteriors look like? What is the effective sample size of the MCMC outputs for each parameter? According to Table 4, there are 8 parameters estimated – what do the posteriors look like for the other 4?

- In Figure 4, the authors state they use a stochastic model, but this wasn't mentioned in the Materials and methods. How was stochasticity incorporated? In addition, what time of year were the infections introduced in Figure 3C, and how was this value chosen? It seems to me timing would have a big effect on the number of cases, depending on whether introduction co-coincided with a high value of Re.

- In Figure 5A, I did not understand why the entire region of 0-8 cases was shaded blue, rather than just a line representing 4/1000 infections (or perhaps a boundary region to represent the posterior distribution of the estimate).

- I found Figure 5B hard to interpret. It seems the authors have selected a colour gradient so the line appears to go through the central microcephaly data point of 27, which makes it difficult to identify which regions produce high and low case numbers. It is also not clear to me what Figure 5C adds, other than normalising the results by the population size – in which case, should the numbers not be 6.2 times smaller (as the population is 620,000)?

- I would have liked to see more discussed of estimates for the α and rho parameters, which control the extent to which environmental factors influence entomological dynamics. What contribution did humidity and temperature have? What are the implications for analysis in other settings, e.g. with stronger or weaker seasonal effects?

- In the fifth paragraph of the Discussion, it seems a stretch to suggest that the model estimates could be consistent with an autumn 2014 introduction. The lower 95% credible interval in Figure 3 is given as 2nd Jan 2015. What proportion of the posterior density falls within the range of dates implied by phylogenetic data?

- In the fifth paragraph of the Discussion, the authors suggest they do not have access to spatial data, but Figure 1 indicates they do, at least at some level of resolution. Could they clarify why this is not suitable for exploring heterogeneities to support their discussion point?

- In the subsection “Viral Transmission”, what was the motivation for have density and frequency dependent transmission for vector-human and H-V transmission?

- Why was a Poisson likelihood used for the observation process (equation 19), rather than, say, a binomial distribution?

- Why was the polynomial simplified to a 3rd degree one in equation 20? What effect did this have on the model in practice? Similarly, why was a 3rd degree polynomial used to fit the data in Figure 2—figure supplement 1? What impact could this assumption have had on model results?

Reviewer #3:

The manuscript describes a detailed transmission model of the ZIKV epidemic in the city of Feira de Santa, Brazil. The work is well done and generally interesting, but there were several important shortcomings.

First, the context of the results is seriously misleading about the epidemiology of ZIKV in the rest of Brazil, specifically comparing 2015 to 2016. The state of Bahia is unique in that substantial surveillance was done in 2015. Zika did not become nationally reportable until January 2016, when reported case numbers increased substantially. From both microcephaly reports and anecdotal information, however, it is clear that massive outbreaks occurred in other states in 2015 (e.g. Pernambuco). This is not a problem with the model per se, but it is a big limitation to the conclusion that FSA was different from the rest of Brazil, (e.g. Figure 1A; Results, second and fourth paragraphs; Discussion, second paragraph). These sections should be rewritten to specifically address the uncertainty in national reporting (almost complete), remove national versus FSA comparison of the epidemiology, and highlight how this model and other models could tell us something about what likely happened in other places. I see that as one of the strengths of this approach and it is not explored at all.

The finding about infants is notable, but also susceptible to a clear bias. It should be clearly noted that there may be an increased probability of reporting infants for whom care is often prioritized, both by families who would seek it and institutions who would provide it. This likely increased even more after recognition of the association with microcephaly. Furthermore, this dataset may offer a unique opportunity to assess changes in reporting as that became clear. This would be true for both infants and women of reproductive age.

I also felt the information on microcephaly and GBS was insufficient. In the Introduction, it is stated that both were coincident with ZIKV incidence, but that seems unlikely given that both tend to lag behind incidence. These curves should by shown and discussed more specifically as this is a key component to understanding generalizability and the reliability of the data being used.

There should be a bit more context of other work on ZIKV and climate; it's not accurate to say "the effects of local climate variables, such as temperature and rainfall, have not yet been explored in relation to Zika transmission." That's true in some ways, but not that generalizable. A number of studies are already cited, e.g. Bogoch et al., 2016; Zhang et al., 2016; Perkins et al., 2016; Messina et al., 2016. This manuscript should point out what is unique here.

The observation rate estimate is very low. Lower than both Yap and French Polynesia. Is there other evidence that supports such a low rate? Limited surveillance? Is it alternatively possible that the epidemic was spatial heterogeneity actually resulted in a smaller epidemic that had a higher reporting rate, lower attack rate, yet nonetheless produced herd immunity effects?

Lastly, there should be more discussion about the risk of microcephaly. The comparisons to French Polynesia and Yap are great but there is a lot of other work that has been done, especially clinical studies: https://www.ncbi.nlm.nih.gov/pubmed/26943629 and https://www.ncbi.nlm.nih.gov/pubmed/27960197. It is especially important to understand why the estimates in this manuscript may be on the very low end of what is being reported elsewhere in studies specifically aimed at measuring that risk.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Epidemiological and ecological determinants of Zika virus transmission in an urban setting" for further consideration at eLife. Your revised article has been favorably evaluated by Prabhat Jha (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The work and manuscript have greatly improved, and the reviewers are satisfied with the approach of the model. However, there are some remaining issues about the way aspects of the model and the results are described that need to be addressed before acceptance, as outlined below:

1) The relationship between the Zika epidemic in FSA vs. the rest of Brazil is still not very clear, although it is improved from before. For example, in the last paragraph of the Introduction it states that Zika peaked elsewhere in the country in 2016. That may be true for some locations, but data suggest otherwise for many of the most affected states. As the authors now note, Zika case surveillance changed substantially in 2016. Clearly higher case numbers are associated with this, but microcephaly numbers were much higher for many states as a result of the 2015 epidemics, so in fact many of the NE states in particular likely had much bigger epidemics in 2015, and FSA may be a very good representation of what happened in those states, not an anomaly as implied in the manuscript. The authors even found evidence of a 4-fold increase in reported FSA between 2015 and 2016. In my view, this is a very important finding and emphasizes how little we know about 2015, even in area with relatively strong surveillance.

While we agree that it is not very helpful to speculate about exactly when the Zika epidemic peaked in different parts of Brazil, we think the overall message is still misleading – it currently appears to suggest that the epidemic in FSA was earlier than the rest of the country when the quality of surveillance in 2015 is probably not good enough to make such conclusions. A more appropriate message could be that detailed analysis of FSA indicated a large epidemic in 2015, which could possibly have occurred in other places although this was not picked up by the limited surveillance at that time.

2) The addition of informative priors is sensible. It would also be helpful to have the posterior outputs so the main figures and analysis can be reproduced. This will enable groups working in other parts of Brazil (or indeed other countries) to make use of the analyses to compare to their findings. References should be given for the priors shown in Figure 2—figure supplement 2 – at the moment only the human incubation and infectious period are given priors.

It would also be helpful to have a brief descriptive file that states what data are used in which figure (if not the actual plotting code itself) – e.g. it is not clear where the age distribution in Figure 1B came from.

3) With regards to the actual code, we take the comment that this would run to many thousands of lines. We actually have facilities to host this on eLife, but we would be happy as an alternative if this was archived e.g. in a suitable GitHub repository.

4) The causal link between ZIKV infection and at least some congenital outcomes (e.g. microcephaly) is now clear from multiple studies in multiple locations. While much is left to be learned, we recommend being more direct in the second paragraph of the Introduction.

5) The term 'herd-immunity' seems a little imprecise as immunity has unlikely reached a level that is truly protective against invasion. Perhaps 'population-level immunity' would be more appropriate?
