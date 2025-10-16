# Peer review - Round 1

Editors:
- Belinda Nicolau, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66590.sa1](https://doi.org/10.7554/eLife.66590.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Combining a few analytical strategies, this manuscript proposes a new approach to forecast mortality that distinguishes future changes in lifestyle- and non-lifestyle attributable mortality on life expectancy projection. The authors use data from 18 European countries to test their model and the results yield more optimistic forecasts than other well-established forecasting methods; future generations will have an increased life expectancy than previously expected. The proposed methodology could bring significant benefits when applied to other contexts and represents an important contribution to the field of life expectancy forecasting.

Decision letter after peer review:

Thank you for submitting your article "Future life expectancy in Europe taking into account the impact of smoking, obesity and alcohol" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Ugofilippo Basellini (Reviewer #1); Collin Payne (Reviewer #2).

As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential Revisions (for the authors):

1. Line 206: "France, Spain, and Italy". I am unsure why you included Spain in your forerunner population, since you do not have Spain in your results. This seems not very consistent, and it should be better justified and clarified. I suppose that you do not have lifestyle-attributable mortality for Spain? How do your results change if you exclude Spain from the forerunners (I imagine very little)?

2. Line 392-393: "However, in our view, the added value of integrating lifestyle into mortality projections outweighs the uncertainties that come with it." This should, and can, be empirically tested with out-of-sample exercises.

3. SM Methodology: "All our projections are based on 50,000 simulations" and "We obtained, for each sex-specific population, 50,000 simulated matrices". I was not able to understand how you performed these simulations. Are these generated from the forecasts of the time series model? Or do you employ a bootstrap on the deviance residuals of the fitted models? Or both? More details on how you compute variability of your forecasts are needed.

4. The following text is an expanded explanation of the Public Evaluation of Reviewer 2: "My main issue with the paper as written concerns the assumptions built into the Li-Lee projection of non-lifestyle attributable mortality. I wonder how sensitive the results are to the choice of reference populations here--that is, I'm not sure that female populations of France, Spain, and Italy are the best populations to use as reference here.

These populations currently have high life expectancies, but also have histories of substantial mortality shocks and had much higher mortality rates in the near past. My issue here comes down to the essential difference between current mortality rates and current mortality conditions. The low age-specific mortality rates of these populations are a function of both current mortality conditions (e.g. period effects/current conditions in terms of development, medical care, etc) and of the history of cohort mortality selection pressures among those currently in the population. The chosen reference populations all have older cohorts who have experienced fairly severe mortality selection in early life, which may lead to smaller groups of more selected, "hardier" individuals surviving to later life. I worry that choosing these populations may provide an over-optimistic reference point for convergence (indeed, these three countries have among the largest gaps between period e0 and currently attained cohort e0--see https://doi.org/10.1080/00324728.2019.1618480). So I'd be interested in seeing whether results differed by using a set of low-mortality countries that have faced less severe life-course mortality pressures--e.g. Sweden, Norway, and Switzerland. My hunch is that your life expectancy projections will decline a little, though not massively. But I think it's worth pushing on this assumption a bit to see how sensitive it is."

Reviewer #1 (Recommendations for the authors):

The manuscript introduces a new approach to forecast mortality that explicitly considers the role of lifestyle epidemics (smoking, obesity and alcohol) on the dynamics of mortality. Specifically, a four-step projection methodology is proposed, which distinguishes between non-lifestyle-attributable and lifestyle-attributable mortality. The former is forecast using an extrapolative model, the latter is forecast using a data- and theory-driven approach, and the two components are combined to obtain all-cause mortality forecasts.

The model is applied to 18 European countries and compared to three other well-established forecasting methods (Lee-Carter, United Nations and Eurostat). The proposed approach results in more optimistic forecasts than the other methods, suggesting that future individuals will live longer lives than previously expected. Moreover, forecasts of the proposed methodology are more realistic as they do not display implausible crossovers between sexes and countries which characterize the other methods.

For these reasons, the proposed methodology appears to be an important contribution to the mortality forecasting literature. However, the manuscript has some weaknesses that the authors should address to further improve their work.

Weaknesses

While the forecasts of the proposed approach appear to be more realistic than those of the benchmark model of Lee and Carter (1992), the forecast accuracy of the proposed model is not empirically evaluated. In the recent mortality forecasting literature, great attention has been devoted to out-of-sample validation exercises, which are employed to measure the accuracy of the forecasts (see, e.g.,Shang et al. 2011,Bergeron-Boucher et al. 2017). A point and interval forecast accuracy evaluation of the proposed model as compared to the Lee-Carter one would provide concrete evidence of the new model's strengths. Clearly, given the limited time series available to the authors, only a short-term forecast evaluation can be performed (e.g. 5 and 10 years forecasts).

Moreover, the results and discussions of the authors are exclusively based on life expectancy, which is certainly a very important summary measure of mortality, but it does not capture everything. No results are shown or discussed in terms of forecast mortality rates and lifespan inequality. The former are very relevant to understand the plausibility of the forecast mortality age-pattern. The latter is another important summary measure of mortality that complements life expectancy (van Raalte et al., 2018), and it should be considered in mortality forecasting (Bohk-Ewald et al., 2017).

The data employed to fit the model is limited to 25 years (1990--2014) because lifestyle-attributable mortality data is available only for this period of time. Based on this (rather short) fitting period, the authors forecast mortality for a period of time twice as long (up to 2065, that is a 51 year forecast). This seems rather unbalanced. Moreover, forecasts of lifestyle-attributable mortality seem to be driven more by theory/expert opinion rather that by observed time series, especially for females. I think these potential limitations should be more clearly specified in the manuscript.

Finally, the principal added value of the manuscript – the new approach to forecast mortality – is currently not available to the general public: "Because of the large size of the many different underlying simulation matrices, we are restricted in sharing these data. … The R codes can be requested from the author." One simple way to address this problem is to share a much smaller set of simulations (say 100 instead of 50,000) and warn the users to increase the number of simulations when running the codes on their machines. This would directly provide the research community with the routines to employ the proposed methodology.

References

Bergeron-Boucher, M.-P., V. Canudas-Romo, J. Oeppen, and J. W. Vaupel (2017). Coherent forecasts of mortality with compositional data analysis. Demographic Research 37, 527-566.

Bohk-Ewald, C., M. Ebeling, and R. Rau (2017). Lifespan Disparity as an Additional Indicator for Evaluating Mortality Forecasts. Demography 54 (4), 1559-1577.

Lee, R. D. and L. R. Carter (1992). Modeling and forecasting US mortality. Journal of the American Statistical Association 87 (419), 659-671.

Shang, H. L., H. Booth, and R. Hyndman (2011). Point and interval forecasts of mortality rates and life expectancy: A comparison of ten principal component methods. Demographic Research 25, 173-214.

van Raalte, A. A., I. Sasson, and P. Martikainen (2018). The case for monitoring life-span inequality. Science 362 (6418), 1002-1004.

Reviewer #2 (Recommendations for the authors):

The authors have conducted an ambitious projection exercise, drawing together a number of methods and approaches to seek to understand the impacts of future changes in lifestyle- and non-lifestyle attributable mortality on prospects for life expectancy increase in a set of European countries. This focus on the underlying dynamics of mortality change--that is, disaggregating the long-term changes in non-lifestyle attributable mortality patterns from the much more variable lifestyle-attributable mortality patterns--represents a real step forward in life expectancy projection modeling. These methods could have considerable benefits for projections in other contexts.

My main issue with the paper as written concerns the assumptions built into the Li-Lee projection of non-lifestyle attributable mortality, where I would encourage the authors to test the sensitivity of their projections to alternative choices of reference countries (looking beyond Italy, Spain, and France).
