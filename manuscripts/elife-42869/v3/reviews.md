# Peer review - Round 1

Editors:
- Ben Cooper, Mahidol Oxford Tropical Medicine Research Unit Thailand

Reviewers:
- Ben Cooper, Mahidol Oxford Tropical Medicine Research Unit Thailand
- Oliver Brady, London School of Hygiene & Tropical Medicine United Kingdom

## Review text

DOI: [10.7554/eLife.42869.019](https://doi.org/10.7554/eLife.42869.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Nationally-representative serostudies are needed for generalizable burden estimates: dengue in Bangladesh case-study" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ben Cooper as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Neil Ferguson as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Oliver Brady (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Nationally representative serum samples are a valuable tool for understanding disease dynamics and planning vaccination interventions, but outside high income countries such studies are lacking (what seroprevalence studies there are are typically based on convenience samples). The current study, which reports the results of a nationally representative serological study for of Dengue in Bangladesh provides an important insight into the burden of disease and informs public health and future intervention strategies. It also represents an important demonstration of how such a national serological study can be conducted and analysed in a LMIC setting and how it can inform policy.

Essential revisions:

There was a consensus amongst reviewers that the analysis does need a bit more work – certainly in description and possibly also in rigour. At the moment there do seem to be missing some detail as outlined below and it is unclear how the risk factor analysis links to the burden predictions.

1) The title and Abstract of the manuscript are very heavily focused on the need to conduct a large number (> 10) seroprevalence surveys to generate accurate estimates of burden, but this is not tested in detail in the paper. Aside from the numerous other methods of estimating dengue burden which is probably outside of the scope of this paper, the analyses presented here only focus on randomised sampling schemes. WHO guidance on conducting seroprevalence surveys for dengue published only last year (Informing vaccination programs: a guide to the design and conduct of dengue serosurveys, WHO, Geneva, 2017) recommends stratified sampling based on historic dengue incidence as documented by passive surveillance. Passive surveillance data may not be available in Bangladesh, but it is in the vast majority of dengue endemic countries, thus limiting the generalizability of the findings presented here. Using the spatial correlation or risk factor analysis might also give unbiased estimates from < 10 well placed surveys (not tested here). It was also difficult to reconcile these interpretations with statements like: "ultimately our crude estimates of the proportion seropositive in the country (24%) was very close to an estimate adjusted for the age and sex distribution in the country". There is real value in the work that has been done here in its own right, so it is a little confusing why the focus of the paper is so heavily skewed towards a statement that was not so thoroughly tested.

2) Using leave one out cross validation in a dataset of size 70 communities is probably not a particularly stringent test. At a minimum, a CV split of 80% training 20% testing would be more standard. Looking at the model fit (2A-B) even with this small hold-out set there seems to be a fair amount of unexplained variance. Could this be better explained by including other (non-spatial) covariates – ideally those related to the risk factors identified in Table 2? Would this change the conclusions about minimum site sample size for national representativeness?

3) How confident are the authors of the claim made in the second paragraph of the Introduction that nationally representative serum samples are lacking outside high income countries? Can this be backed up by a systematic search of the literature, or is there robust evidence from one or more of the cited papers (Metcalf et al., 2016; Wilson et al., 2012; Osborne, Weinberg and Miller, 1997; Jardine et al., 2010; De Melker and Conyn-van Spaendonck 1998; Ang et al., 2015)?

4) The analysis accounts for clustering at the village level (through a hierarchical model) but not spatial correlation, which in general would be expected to reduce the amount of information in the data. It would be useful if this could be discussed, the decision to ignore such correlation justified, and the situations where it is important to account for spatial correlation in the regression modelling discussed.

5) Results section: "no household level covariates were significantly linked to seropositivity". Following the ASA's report on p-values (and many recommendations before that), it is widely considered unwise to report results according to "bright lines" for p-values (in this case 0.05 presumably). By all means report the p-values, and certainly report the confidence interval, but hopefully we are moving away from the era where we use such arbitrary thresholds to decide whether to report results, while ignoring the magnitude of the effect.

6) It is slightly difficult to read this paper as the Materials and methods are at the end and not enough detail is given in the Results for it be clear what was actually done without referring to the Materials and methods. Note that eLife guidelines say that "A Methods or Model section can appear after the Introduction where it makes sense to do so". I think the authors should either consider moving the Materials and methods to before the Results or at least briefly saying what was done in the Results with a more detailed explanation in the Materials and methods.

7) It's quite unclear how the results were used to derive nationally representatives estimates. The Materials and methods simply say "we also calculated a census-adjusted proportion seropositive by community that adjusted for any sampling bias" but details of how this was done are lacking. Such adjustment also seems to have been using only age and sex distribution from the 2011 census. Why not also use Urban vs. rural (an important predictor according to Table 2 and which should be easily obtained). Other community-level covariates could also be used, potentially. Note there is a literature on multilevel regression and post-stratification to address this type of problem that might be relevant here (see, for example, Zhang et al. Am J Epidemiol 2014, https://academic.oup.com/aje/article/179/8/1025/109078).

8) References to Figure 2B and Figure 2C in the text need to be swapped.

9) "All covariates that were statistically significant at a p-value of <0.1 in the unadjusted analysis were included in a multivariable analysis." Not clear why this was done (except that many other papers do this). There seem to be enough data to include all covariates, and covariates with p-values >0.1 may still have important affects either alone or in combinations. Sometimes covariates have to be selected using some approach as there aren't enough data to use them all, but this doesn't seem to be the case here.

10) "using catalytic models". Given there is no space limit it would be helpful to define the technical details here. Also, a constant force of infection was assumed for all serotypes. Was this assumption of a constant f.o.i. tested (e.g. by comparison with other models)? How consistent are the data with this assumption? The Materials and methods suggest that f.o.i. was allowed to vary by age (is this correct)? Why not also sex given the reported sex differences?

11) "we estimate that 40 million people have been infected with 2.3 million annual infections." (Abstract and Results). 95% CIs are needed for these estimates?

12) Sample size calculations will be useful to others. However, those currently given in the supplementary text use a formula without further justification (or reference to any justification) and condition on the fact that 70 communities are being sampled. To be more useful, I think it would be help if the authors could discuss the sample size implications of sampling more (or fewer) communities for given correlations between village. For example, for the observed within-village correlation how would the required sample size change as a function of the number of communities sampled. What would be the impact of spatial correlation be on these numbers? What about different levels of within village correlation? This would be useful for others planning such studies and think it would also be appropriate to discuss this issue in the Discussion section i.e. what are the resources required for a given precision/resolution and how are the resources required likely affected by study design choices. It would also be useful if the authors could at least discuss the issue of spatial correlation and discuss the merits/demerits of accounting for it in the modelling in general (as well as in this specific example).

13) "Reported having dengue" and "heard of dengue" seem peculiar things to include in the regression, as these might be extended to be a consequence of having dengue rather than a potential risk factor. Perhaps this reflects the fact that the purpose of the regression analysis is not clearly stated. It would be good to have a clear statement about the purpose of the regression and a justification for the choice of variables to include.

14) The supplementary material describes the recruitment strategy: "the study staff identified the house where the most recent wedding had taken place and identified the closest neighbour. They then counted six households in a random direction to identify the first household for the study. To select each additional household for the study, they used the previous household as a starting point and counted six households in a random direction." This seems a little eccentric and not obviously guaranteed to give a random sample. Is there any justification for this choice? Wouldn't numbering households and selecting at random or throwing darts at maps be better? I think this point at least needs to be discussed (with recommendations for future studies) and this aspect of the methods should be move to the Materials and methods section in the main text.

15) "may provide some guidance". Not sure what the intended meaning of this is. What kind of guidance?

16) Was any attempt made at assessing the accuracy of the recorded household data?

17) The entomological approach to determining the presence or absence of Ae. aegypti is quite superficial. The intensity of surveillance (number of BG traps per community) and duration (time in the field) is too short to arrive at a conclusion of presence/absence. In dengue endemic cities, where Ae. aegypti has a well-documented presence, there can be quite marked spatial heterogeneity in the distribution of Ae. aegypti when measured by BG traps, e.g. some houses can be free of this species for consecutive weeks but in a house 50 metres away they can be caught regularly. In regards to Ae. albopictus prevalence, BG traps set indoors are not the optimal method of determining presence/absence- it would have better to set them outdoors or to use outdoor ovitraps. The authors should qualify their conclusions by recognising that trapping method, intensity, duration and seasonality can all influence the likelihood of Aedes detection and this could change the conclusions of the manuscript.

18) Is there any reason uncertainty (in either or all of the data, kriging model and the force of infection model) can't be propagated through to the final burden estimates? Comparing mean estimates with Bhatt et al. to prove that nationally representative surveys are needed probably also needs to consider uncertainty. I think they might have also included tertiary and quaternary infections as well if you want to be comparable.

19) Can code for statistical analysis be made available?

20) "Our findings are in marked contrast to what has been observed with chikungunya in Bangladesh". Can the authors offer any hypothesis as to why this might be the case?

21). Can the authors provide at least one concrete example of such a survey could lead to better decision-making about vaccination?

22) It was felt that some of the statements about findings showing that lack of spread of aegypti is the reason behind heterogeneities in dengue transmission in Bangladesh were not fully justified in light of the known limitations of entomological surveying.

23) The authors correctly point to the possibility that the Panbio-based seroprevalence survey might have reflected past JEV exposure and cite the low case JE incidence to suggest dengue is the primary culprit for the seroloprevalence.. This might be true, but JEV is notoriously difficult to diagnose in the absence of laboratory testing and there would almost certainly be under-reporting of cases in Bangladesh. Having a random subset of samples tested by DENV/JEV PRNT50 assay, regarded as the most specific assay of DENV serostatus, could have helped clarify this point. Can the authors do this readily perhaps on a sample of 100 or so (or use Luminex as a (less preferred) option? Though not essential, it was felt this would improve the quality of the manuscript if it could be done within 2 months. If it can't be done the Discussion needs to be qualified accordingly.

24) Materials and methods: when were interviews conducted in relation to the dengue season? Could this have introduced recall bias of "whether diagnosed with dengue"?

25) Was there any evidence that travel in the last 7 days was a reasonable proxy for long term travel history?

26) "Our finding of a negative correlation between Ae. aegypti and Ae. albopictus presence is consistent with competition between the two species" – or is just evidence that they have different environmental niches?
