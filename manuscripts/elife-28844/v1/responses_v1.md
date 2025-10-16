# Author response - Round 1

Authors:
- Yesseinia I Angleró-Rodríguez
- Octavio AC Talyuli
- Benjamin J Blumberg
- Seokyoung Kang
- Celia Demby
- Alicia Shields
- Jenny Carlson
- Natapong Jupatanakul
- George Dimopoulos ([ORCID: 0000-0001-6755-8111](https://orcid.org/0000-0001-6755-8111))

## Response text

DOI: [10.7554/eLife.28844.023](https://doi.org/10.7554/eLife.28844.023)

[Editors’ note: the author responses to the first round of peer review follow.]

Reviewer #2:

The manuscript describes laboratory experiments that interrogate the impact of a Talaromyces fungus on Aedes aegypti susceptibility to dengue virus. Regretfully, in its current form, the manuscript is too preliminary for publication in eLife.

The title of the manuscript is mis-leading as there is no evidence that gut digestive activity modulates dengue susceptibility. The problem is that the authors used two unrelated systems to address their question; they first fed mosquitoes with fungal spores to examine the effect on dengue susceptibility in the midgut, fungal persistence throughout the duration of the experiment for mosquito survival assays. However, the rest of the manuscript is based on fungal secretome. This is like comparing apples and oranges. There is no evidence that spores develop further or persist as spores in the mosquito midgut. There is no evidence that the spores persist in the midgut as the experiments have been performed with whole mosquitoes.

We don’t agree with the apples and oranges metaphor used by the reviewer; apples and apple juice would have been more accurate. The first observation of the study was that feeding on live fungi resulted in an enhanced DENV infection, next we show that the effect on infection is attributed to fungus secreted factors. Fungi are generally known for their production and secretion of a variety of bioactive secondary metabolites. We proceeded with the remaining experiments using the fungus secretome because it contains the bioactivity of interest and represented a less complex sample than the entire organism, and the effect was stronger (P <0.0001). The probability that the effect on DENV infection exerted by the spores/conidia (which we have shown secreted the bioactive molecule(s) which we call “secretome”) when present the midgut is attributed to something different from that contained in the filtered spore/conidia culture (secretome) is so small, and difficult to address, that we don’t think it deserved further speculation. We have addressed the other concerns regarding spores persistence in the midgut by performing a new set of experiments where fungus persistence up to 25 days after ingestion was monitored. We now show the persistence of the conidia in the mosquito midgut, after a single feeding on conidia, throughout the entire time-course.

Regarding the title of the manuscript; we have now provided functional evidence, through genesilencing assays, linking decreased trypsin transcript abundance to enhanced DENV infection (Figure 7D, 7E, 7F).

Even should the assumption that spores develop as actively as on the fungal medium and secrete all factors, there is no direct evidence that trypsin inhibition underlies the observed susceptibility, there is no functional analyses of the causative effect of trypsin genes or trypsin activity.

In the original manuscript we presented functional assays showing that midguts treated with the fungus secretome display a significantly lower trypsin enzymatic activity (now Figure 7B).

However, to further address the reviewer’s concern, we have now provided functional evidence, through gene-silencing assays, linking decreased trypsin transcript abundance to enhanced DENV infection (Figure 7D, 7E, 7F).

Finally, as described below, the authors do not use appropriate statistical methods to evaluate the significance of their results, and they do not provide their raw data for confirmation.

We have provided a detailed raw data file outlining the statistical analyses.

[Editors' note: the author responses to the re-review follow.]

Essential revisions:

One of the main criticisms of the previous version of the manuscript was that the study did not conclusively link the anti-dengue effect with the disruption of blood digestion. In the revised manuscript, the authors claim that this functional link is now demonstrated by additional data shown in Figures 7D-F.

In the first revision, we did not claim that the anti-dengue effect is linked with the disruption of blood digestion, but with a disruption of trypsin activity. We explained the reduced ovary development as a possible result of impaired blood digestion. We clarify this aspect in the revised manuscript, and included additional data as suggested by the reviewer, showing that mosquitoes treated with fungus secretome weight more than untreated mosquitoes at 48h post-blood meal (now Figure 7B).

Throughout the paper there are statistical issues with the use of ANOVA to analyze virus titers (log PFU/midgut). These analyses include virus-negative mosquitoes and this has two undesirable consequences. First, the residuals of the analysis are typically not normally distributed, which violates one of the fundamental assumptions of ANOVA. Second, the analysis of infection intensity is partially redundant with that of prevalence because it includes the effect of infection status (infected or uninfected).

We eliminated virus-negative mosquitoes from the intensity graphs and only include this information in graphs showing infection prevalence. We sought specialist advice on statistical analyses from the Johns Hopkins School of Public Health Biostatistics department, and they analyzed the data using Generalized Linear Regression (GLM) with experiment-clustered robust variance estimates to account for potential within-experiment correlation of outcomes (Rogers, 1993) see Statistical Analysis in the Materials and methods section for more details.

Figures 2A and B, 3A and B, 5C, 7F. The upper right infection prevalence boxes were not statistically analyzed (or the stats aren't shown) to indicate if a significant difference was observed. Thus, the authors can't technically state that they observed an increase in infection prevalence (e.g., for Figures 2A and B, second paragraph of the Results section).

We performed statistical analysis of the prevalence data, and include this information in the revised manuscript.

Figure 7A. Ovary development is a tangential parameter for quantifying blood meal digestion. Other factors could contribute to the reduced ovary size observed in Tsp_PR secretome treated mosquitoes. For example, Tsp_PR secretome treated mosquitoes house significantly more bacteria in their gut, and this population may include taxa not normally present. This could induce an immune response. The reduced ovary development observed under these circumstances could reflect a competition for resources between the bacteria and the mosquito. A more direct measurement of blood meal digestion is to simply weight the gut (as in Emre Aksoy et al. 2016, PNAS) or better yet, take photos (as in Bryant et al., 2010).

Ovary development is part of the gonotrophic cycle after a mosquito takes a blood meal, and impairment of ovary development can indicate compromised blood digestion or nutrient acquisition (Bryant et al., 2010; Lea et al., 1978). However, as suggested by the reviewer, and used by others (Pimenta de Oliveira et al., 2017), we now present new data on mosquito body weight after blood feeding, showing that mosquitoes treated with fungus secretome are heavier than the non-treated at 48h post-blood meal suggesting a compromised blood degradation process (Figure 7B).

Figure 7E the authors use ANOVA to compare log-transformed virus titers per mosquito, across several trypsin knockdown treatments. They include virus-negative mosquitoes in their analysis, which results in the shortcomings mentioned above. When one performs the ANOVA of virus titers without virus-negative mosquitoes, for T714 and Tmix (the treatments with the strongest effect according to the authors) the residuals meet the normality assumption of ANOVA and there is a statistically significant interaction between experiment and treatment. In fact, the treatment effect is only seen for the first experiment, but not for the other two experiments. This means that the effect is inconsistent and seriously questions the validity of the conclusion.

We eliminated the virus-negative mosquitoes for all graphs and only included this information in the prevalence graphs. We also included a 4th independent experiment to the data set to render it more robust. Data was analyzed using Generalized Linear Regression (GLM) with experiment-clustered robust variance estimates to account for potential within-experiment correlation of outcomes (Rogers, 1993) see Statistical Analysis in the Materials and methods section for more details.

Figure 7F the authors analyze infection prevalence across several trypsin knockdown treatments. In the Results section the authors claim "silencing of T714 resulted in the greatest increase of DENV infection prevalence". This sentence together with the blow-up view of infection percentages (without plotted confidence intervals) in Figure 7F are strongly misleading. Even for T714 there is no statistically significant effect of the treatment on infection prevalence.

For clarity, we decided to show each trypsin silencing graph in an individual panel with its respective prevalence value and confidence intervals error bars.
