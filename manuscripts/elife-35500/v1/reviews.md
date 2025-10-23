# Peer review - Round 1

Editors:
- Eduardo Franco, McGill University Canada

Reviewers:
- Tom Fowler, University of Birmingham United Kingdom
- Patrick Brown, University of Toronto Canada

## Review text

DOI: [10.7554/eLife.35500.062](https://doi.org/10.7554/eLife.35500.062)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "National and regional seasonal dynamics of all-cause and cause-specific mortality in the USA from 1980 to 2013" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Eduardo Franco as a Reviewing Editor and Prabhat Jha as the Senior Editor. The Reviewing Editor has drafted this decision to help you prepare a revised submission. As is common in eLife, decision narratives are an amalgamation of the essential points of the reviewers' critiques after eliminating redundancies in comments and suggestions.

Summary:

This paper examines the seasonality in age- and disease-specific mortality in the US using geocoded data analyzed via wavelet statistical modelling and Poisson regression techniques. The key results indicate mortality increases in adults over 45 years old in winter from cardiorespiratory causes and injuries. Injuries, attributable mainly to road traffic crashes were seen to rise in the summer months among young men. No variation in seasonality was found by climate region, indicating no apparent disparities in adaptation by geographic location. This study provides insights as to whether climate changes could have an impact on the mortality patterns observed in the US as a model. The findings could assist in planning surveillance mechanisms and in projecting workforce requirements in primary and emergency healthcare.

Essential revisions:

1) By choosing only 4 disease groups the authors seem to have missed a key opportunity to investigate seasonal patterns in finer subgroups despite possessing a large sample size (n = 77,771,264), Furthermore, the rationale for choosing the subgroups presented is unclear. For example, the authors chose to group cardiorespiratory diseases into one large outcome when cardiovascular and respiratory outcomes have differing mechanisms in their association with heat or cold exposure. Within respiratory diseases itself, it makes sense to separate acute and chronic causes because the mechanisms vary so starkly and are related to seasonal patterns, i.e. the incidence of pneumonia and acute respiratory outcomes are likely heightened in the winter and this observation may differ to how/why the incidence of chronic respiratory deaths vary seasonally. Furthermore, the mechanisms for how heat is associated with elevated respiratory deaths is understudied and knowing more about seasonal patterns here would be a useful addition to the literature.

I believe it's important to investigate seasonal patterns of deaths from infectious disease, maternal and neonatal causes, endocrine disorders, genitourinary conditions and neuropsychiatric conditions (which are all associated with temperature) to add valuable insight into understudied but important disease groups, but these have been excluded from the present analysis. Considering the tragic opioid epidemic in USA, it would be a valuable contribution to the literature to understand whether seasonal patterns (at least in more recent years) are observed with deaths related to substance use disorders.

2) The authors pointed out in the Introduction that global warming may impact on excess cold weather death rates. Presumably a major part of the rationale for testing the differences in regions over time was to help inform our understanding of what the impact may be. However no conclusions were reached with regard to the implications of the findings. Clearly any such conclusions would need to be appropriately and heavily caveated but as this is a major reason for the analysis. Please expand the Discussion to include these points.

3) Methodology:

A) Wavelet power spectra are not always easy to interpret, and the uncertainty in estimated wavelet coefficients is difficult to quantify. The wavelet analysis makes for an interesting exploratory tool, showing that for the most part cycles have a duration of 12 months and are reasonably stable over time. It does not seem possible to draw firm conclusions about the research hypothesis using wavelets, however. All cause male mortality for 15-24 year olds appears to be less cyclical in recent years, although how to quantify this effect and assign a statistical significance to it is not apparent from the power spectrum shown.

The second analysis is more appropriate, although the details of this analysis are sparse. It appears that the model used is something like the following, where Yit is the count of deaths in age group i at time t.

--------------------- -------------------------------------

Yit∼ Poisson(Nit ⋅ λit)log(λit)= μi + βit + Mit ⋅ [α1i ⋅ cos(2πt/12)

+α2i ⋅ sin(2πt/12)+α3i ⋅ cos(2πt/6)

+α4i ⋅ sin(2πt/6)]

Mit= ρi + γit

--------------------- -------------------------------------

A model of this could answer the following questions, with p-values produced from a likelihood ratio test.

- Is γi negative? If so the seasonal effect is becoming less severe for age group i.

- Does it look like all age groups have the same trend, with γi = γ₀ for all i?

- Do all age groups have the same cycle, with αpi = αp0?

- Does γ vary by region (negative in cold-climate regions?)

- Do the cycles, given by the α, vary by region or is a nation-wide cycle sufficient?

The above model is easier to interpret than the wavelet analysis. The quantity 1 − exp(120γ) is the change per decade in the seasonality effect, which could be reported with a 95% confidence interval.

B) The approach is different to a number of those referenced (particularly the standard measure of excess winter deaths). It would be helpful to have some comment on this, particularly the generalisability to other studies. The focus has been on peak months in this analysis, but the standard assessment of excess winter deaths is to compare December to March months to the rest of the year.

C) Appropriate rationale was given to the regional splits used in the analysis. However no description was given of the characteristics of these regional areas other than subsequent information on temperatures. As pointed out there could be a number of factors that are important. I would expect some reference to their differing characteristics.

4) Interpretation:

A) No table is presented with descriptive statistics, i.e. on the sample size of cases that fall into each disease category.

B) I may be misreading the paper (in which case it would be helpful to clarify so others do not make the same mistake), however the analysis in Figure 6 compares the difference in temperature experienced in those regions between the warmest and coldest months versus the% seasonal difference in death. In the Discussion this in contrasted with findings from Europe where countries with a more temperate winter have, paradoxically, higher rates of excess winter mortality. However this is not an appropriate direct comparison, regional extremes in variation were not looked at when comparisons between countries are made. This does not invalidate the comparison but it would be helpful to explicitly summarise if there are any differences between regions and examine what those are.

C) One option for this paper would be to be admittedly exploratory, avoiding the use of the word 'significant' and simplifying the analysis. Simple monthly averages and testing for the months having the same mean could replace the wavelet analysis. A second option would be to focus on a specific research hypothesis, explain carefully how the model estimates relate to this research hypothesis, and adjust the p-values for multiple testing.
