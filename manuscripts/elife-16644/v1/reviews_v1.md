# Peer review - Round 1

Editors:
- Mark Jit, London School of Hygiene & Tropical Medicine, and Public Health England , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16644.026](https://doi.org/10.7554/eLife.16644.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Impact of HIV co-infection on the evolution and transmission of multidrug-resistant tuberculosis" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Prabhat Jha as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers and Reviewing Editor were satisfied with the general direction of the analysis and found the work to be sophisticated and to hold an important public health message. However, there were a number of issues around the model and its parameterisation that we felt were inadequate, and which would need to be addressed for the manuscript to be considered further.

Essential revisions:

1) In the first paragraph of the subsection “Effect of HIV co-infection on TB transmission”, you appear to describe a new method for inferring transmission pairs (i.e. person A infected person B), which you have developed. You use a simple SEIR transmission model in determining who infected whom and use an SEIR simulation to help validate the method.

It is important that you further explain this method so that readers can better understand it and researchers will be better able to apply it judiciously in their own work. For example, you conducted a sensitivity analysis on the values used for the latent period and the removal rate but you did not include HIV status in the model, and HIV status could affect each of these parameters. Furthermore, you do not state what mixing assumption you used and likely assumed random mixing. It would be useful if you could explore how the method would perform in the context of non-random mixing (e.g. discuss what the expected effects would be and not necessarily conduct new simulations). You also reported that keeping two-thirds of cases in the second half of the simulated outbreak corresponded to the sampling frame used for the actual genomic data analyses but you need to explain where this number came from (subsection “Simulations and Sensitivity analyses”). If necessary, you should also test the impact of different sampling fractions.

You state "These results conform with our expectation given that there is significant uncertainty about who infected whom based on genomic data alone when accounting for extended periods of within-host evolution" but this high degree of uncertainty does not appear in the conclusions in the main text.

2) In the third paragraph of the subsection “Effect of HIV co-infection on TB transmission”, you tested whether HIV-positive or HIV-negative individuals transmit TB more often conditional on having TB disease. As you suggest, the analysis including all transmissions seems like it would not be very informative since it likely includes many pairs who did not actually transmit between them. While the top X% analyses are affected by the same issue to a lesser extent, there could be another bias in these analyses since enriching for actual transmission pairs would seem to condition on there being at least 1 transmission from the putative source case and thereby eliminates (many of) the instances in which no TB transmission occurred. This would skew the distribution of onward transmissions which could make HIV-positives and negatives appear more similar in terms of their transmission potential than is actually the case.

To provide a simple numerical example of the potential issue, suppose that out of 100 HIV-negative people with active TB 60 of them transmit to 1 other person, while 80 out of 100 TB-HIV coinfected people each transmit TB to 1 person. In this scenario, TB would appear to have the same transmissibility among those who transmitted (i.e. 1 TB transmission per TB transmitter in each HIV group). However, this would give a misleading picture of the actual TB transmission potential of HIV-positive vs. HIV-negative individuals since coinfected people had an 80% probability of transmitting whereas HIV-negative people had a 60% chance of transmitting.

3) In the last paragraph of the subsection “Effect of HIV on progression of Mtb infection to active TB”, you correlate cross-sectional data on HIV and TB prevalences and HIV and MDR-TB prevalences across countries in an effort to determine whether HIV increases TB in general or if it specifically drives the spread of MDR-TB. However, you should explain why this analysis is appropriate in light of the findings of Sergeev et al. (Sci Trans Med 2013, reference 20) who find that the "individual-level association between HIV and drug-resistant forms of TB is dynamic, and therefore, cross-sectional studies that do not report a positive individual-level association will not provide assurance that HIV does not exacerbate the burden of resistant TB in the community."

Also, while the analysis includes HIV and TB/MDR-TB, it's not clear on how it specifically fits in with the rest of paper or if it could be cut without loss of any key information.

You report in Figure 5, the correlation between global patterns of MDR-TB, TB and HIV prevalence. In the Methods you refer to the World Health Organization for the underlying data. This reference should be extended as it now only states "World Health Organization". Data from several countries are known to have limitations in the sense that the prevalence of HIV or TB may not always been known or collected in a rigorous manner. The prevalence of a particular disease can also vary within a single country. Use of these data can therefore also result in biased estimates, as estimates for HIV and TB may be derived from different sites in a single country.

This entire analysis needs to be either strengthened or simply removed from the paper.

4) More explanation is required for key numbers reported in their paper.

In particular, in the Results, you state: "Based on the available data we considered that the sequenced outbreak isolates represented about 35% of the total number of individuals belonging to the outbreak." You should explain how you came up with the figure of 35%. What are you assuming about the fraction of TB cases that are diagnosed and recorded? How, and over what time scale, are you defining the "outbreak" since reactivation TB cases may have been infected decades prior to disease onset?

Again, in the Results, you state: "This left 13 resistance mutations that evolved with high probability during therapy in 11 patients (Table 2). Seven of the patients were HIV negative and four were positive. A χ2 analysis revealed a statistically significant overrepresentation of acquired resistance in HIV-negative cases relative to positives (p = 0.027). This finding strongly suggests that HIV was not a driver of Mtb drug resistance within the outbreak." Given that you indicate that these results strongly back up a key part of your findings, it is important that more information be provided. Specifically, it is unclear exactly which numbers were being compared in the test (e.g. was the null hypothesis that there should be a 50:50 split between HIV-positives and negatives, or was it directly comparing the fraction of mutations found in HIV-infected vs. uninfected individuals [though this would not seem to give the p-value reported]). Also, a Fisher's exact test, not a chi-squared test, would likely be required given that apparently some of the cell sizes were very small.
