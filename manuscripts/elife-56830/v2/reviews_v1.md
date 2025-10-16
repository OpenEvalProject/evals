# Peer review - Round 1

Editors:
- Molly Przeworski, Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56830.sa1](https://doi.org/10.7554/eLife.56830.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We still know little about how variation in natural levels of radioactivity impact germline mutation rates. By contrasting substitution rates across 14 waterlice species, the study reveals an increase in mutation rates in more radioactive environments; in particular of G>T mutations, consistent with oxidative stress. Thus, this comparative approach identifies the impact of an external mutagen on de novo mutation rates.

Decision letter after peer review:

Thank you for submitting your article "Bedrock radioactivity influences the rate and spectrum of mutation" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Detlef Weigel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Shamil R Sunyaev (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As you can see from the individual reviews below, the reviewers all appreciated the study design and found the results convincing and interesting. Nonetheless, they raised a number of concerns that will need to be addressed in revisions. The most serious set of concerns pertain to the interpretation of the findings. More discussion is needed of possible confounders to the association of bedrock radioactivity levels and substitution rates. Moreover, the assumption that the environmental conditions remain constant in a lineage seems tenuous, which casts doubt on the quantitative estimates provided. This point too merits further discussion. Finally, the interpretation in terms of ROS seems excessively strong. The reviewers also make a number of useful suggestions about statistical analyses, notably in terms of the analysis of the mutation spectrum. In terms of presentation, it was also felt that reviews of the field in the Introduction and Discussion could be improved substantially.

Reviewer #1:

I really liked the idea of comparing synonymous substitution rates and types in closely related species that experience different levels of bedrock radioactivity. I am convinced that there seems to be an association there, and the mutation spectrum results are also interesting, but it was hard to evaluate rival hypotheses for the association without knowing more about the species that live in environments with lower vs higher levels of radioactivity. I was also curious how diverged they are at the nucleotide level. Given that the authors have the data to look at these questions, it would be helpful to know how diversity levels and the allele frequency spectrum differs between different species compare for instance.

I also didn't quite know what to make of the quantitative estimates when I expect the level of bedrock activity likely changed quite a bit over the o(Ne) generations of the species. Could the authors comment on that?

For the mutation spectrum analysis, I think the authors should use a forward variable selection approach, such as the one employed in Harris and Pritchard, 2017.

In terms of presentation, I found the Introduction somewhat unhelpful, in that it lumps references for all sorts of ionizing radiation and UV, on both point mutations and microsatellites. For this reader at least, it would be helpful to overview what types have been studied, and what is known specifically for the type examined here. Also this study should be discussed: https://www.ncbi.nlm.nih.gov/pubmed/25809527. On a related but more minor note, I was unconvinced by the argument that this question cannot be studied experimentally and I don't think the argument is needed to motivate their approach.

In turn, the discussion of life history trait effects on mutation rates in metazoans was both too strong and oddly referenced. As examples, Martin and Palumbi, 1993 is actually an argument for consideration the effect of metabolic rates; Saclier et al., 2018 is only in isopods, when the claim is made for metazoans etc… Similar to my comment on the Introduction, I think a more systematic discussion of the literature is needed.

Finally, I thought the authors could do more to link their findings to studies in other organisms, in particular humans, where there are a number of studies of mutation patterns in populations living in diverse environments (e.g., https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1006581).

Reviewer #2:

This manuscript is proposing an attractive model suggesting that natural radioactivity (even at a low level) affects the mutation rate in waterlice. The authors collected unique biological material in a number of areas with variable radioactivity levels. The data and the proposed model are certainly of great interest. However, I find that the manuscript would benefit from a few additional statistical analyses of the data and from softening the discussion about ROS.

1) The analysis makes a major assumption that the habitat and the corresponding level of radiation remains unchanged after speciation. This assumption warrants a discussion. Overall, I agree that a violation of this assumption would result in a conservative estimate and main results should not be affected.

2) I think that the study lacks a test for robustness of pGLS.

3) The manuscript should discuss potential covariates and confounders. Is it possible that variables other than radioactivity level are responsible for the signal?

4) The conclusions of the manuscript are based on Figure 2 showing non-ulotrametric trees and ratios of synonymous branch lengths. It would be great to show the data for "polymorphic" variants (just terminal branches).

5) In human cells, radiation primarily induces deletions associated with the microhomology repair. If this is also the case in the waterlice system, the authors should be able to find a highly specific and strong signal on top of the results about point mutations. This would dramatically strengthen the conclusions.

6) I do not find that the shift in mutation spectra is a sufficiently strong evidence in favor of ROS. This either requires a much stronger argument, or the discussion about the role of oxidative damage should be softened.

Reviewer #3:

In this study, Saclier et al. explore the effects of natural radioactivity on the germline mutation rate and spectra of subterranean waterlice, aiming to address the question of whether radioactive habitats have long-term evolutionary effects on the genomes of species which inhabit them. The use of this organism to test such a fundamental question in evolutionary biology is very clever, as waterlice are not exposed to confounding effects of UV radiation and have naturally limited dispersal. I found the paper well-written and a fun topic to read, and the arguments that natural radioactivity can have a tangible impact on genome evolution were compelling.

I have a few concerns and suggestions about the regression models and statistical analyses.

Figure 2: This would be easier to follow if points were labeled/colored/shaped to indicate the corresponding species, site, and bedrock formation type.

Table 1: The authors use independent regression models to test for the associations between mutation rate and each three variables of interest: α radioactivity, Received Dose, and λ-15. Why did the authors perform three separate simple regressions rather than a multiple regression using all three of these variables as covariates? Given that λ-15 and Received Dose appear to be stronger predictors of mutation rate than α radioactivity, does this mean the statistically significant association of α radioactivity goes away when adjusting for the other two variables? I expect these three variables to be highly collinear and too many covariates could easily result in overfitting with such a small sample, but the claims drawn from this table would benefit from a more nuanced statistical analysis.

Also, were there any additional environmental covariates that may have been measured when samples were collected or integrated from other data sources (e.g., latitude, distance to nearest industrial activities, etc.)? If possible, it would be interesting to see if other environmental factors can also explain the variation in mutation rates, but I recognize that such data may not be available, and even if it were, this analysis may not be feasible with a small sample.

Table 2: Performing 3 separate regressions for each of 6 mutation types results in some multiple testing issues that must be addressed, at a conservative Bonferroni-corrected α value of.05/18=.0028, only the C:G>A>T mutation class is statistically significant across all 3 explanatory variables, but the A:T>T:A class is not. This multiple testing burden could perhaps be alleviated by using multiple regression as suggested above. Further, the response variables of the 6 regressions are proportions that add to 1, so these are not independent statistical tests, even though they are analyzed and presented as such. Is there a different statistical model that can be used that takes into account the interdependence of the 6 components of the mutation spectrum?

How well-correlated are the nuclear and mitochondrial dS/ra values across samples? A priori, I expect them to be strongly correlated, but it would be interesting and straightforward to investigate if radioactivity levels also affected relative differences in nuclear and mitochondrial mutation rates, e.g., perhaps radioactivity increases nuclear mutation rates in a linear fashion, but mitochondrial mutation rates in a non-linear fashion.
