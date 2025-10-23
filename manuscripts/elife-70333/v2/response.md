# Author response - Round 1

Authors:
- Rodrigo M Young ([ORCID: 0000-0001-5765-197X](https://orcid.org/0000-0001-5765-197X))
- Camila J Solis ([ORCID: 0000-0002-7195-523X](https://orcid.org/0000-0002-7195-523X))
- Andres Barriga-Fehrman
- Carlos Abogabir
- Alvaro R Thadani ([ORCID: 0000-0002-2541-1709](https://orcid.org/0000-0002-2541-1709))
- Mariana Labarca ([ORCID: 0000-0001-6455-3569](https://orcid.org/0000-0001-6455-3569))
- Eva Bustamante ([ORCID: 0000-0002-3125-8608](https://orcid.org/0000-0002-3125-8608))
- Cecilia V Tapia ([ORCID: 0000-0001-6234-2100](https://orcid.org/0000-0001-6234-2100))
- Antonia G Sarda
- Francisca Sepulveda ([ORCID: 0000-0002-8144-0096](https://orcid.org/0000-0002-8144-0096))
- Nadia Pozas
- Leslie C Cerpa ([ORCID: 0000-0002-9525-389X](https://orcid.org/0000-0002-9525-389X))
- María A Lavanderos ([ORCID: 0000-0001-6167-0508](https://orcid.org/0000-0001-6167-0508))
- Nelson M Varela ([ORCID: 0000-0002-5229-3007](https://orcid.org/0000-0002-5229-3007))
- Alvaro Santibañez ([ORCID: 0000-0001-9330-2961](https://orcid.org/0000-0001-9330-2961))
- Ana M Sandino ([ORCID: 0000-0002-3862-3743](https://orcid.org/0000-0002-3862-3743))
- Felipe Reyes-Lopez ([ORCID: 0000-0002-5001-457X](https://orcid.org/0000-0002-5001-457X))
- Garth Dixon ([ORCID: 0000-0001-8165-3094](https://orcid.org/0000-0001-8165-3094))
- Luis A Quiñones ([ORCID: 0000-0002-7967-5320](https://orcid.org/0000-0002-7967-5320))

## Response text

DOI: [10.7554/eLife.70333.sa2](https://doi.org/10.7554/eLife.70333.sa2)

[Editors’ note: the authors resubmitted a revised version of the paper for consideration. What follows is the authors’ response to the first round of review.]

All reviewers agreed that the testing of mobile phone screens is highly novel and this study demonstrates that it could be potentially useful to expedite more widespread testing. The major reservations related to the mathematical modeling and the lack of specific consideration about implementation issues. Reviewer two pointed out the these included models are "neither necessary or sufficient to evaluate the possible usefulness of this testing method." It would be necessary to describe the specifics of a screening plan based on smartphone testing how it might interact with other interventions, or possible disadvantages due to displacing other tests that may have higher sensitivity or specificity. Testing smartphones at scale requires a plan, and an assessment of costs, including opportunity costs.

The modeling while robust, does not account for these real world issues and is not specifically calibrated to any specific COVID epidemiology data or parameters. Moreover, the effects in the model are mediated mostly by the quarantine associated with testing, whereas the greatest utility of this testing approach would require linkage to contact tracing.

A final comment on the cell phone testing strategy was that the sample size is small, with only 51 SARS-CoV-2 individuals (by nasopharyngeal swab). Overall, this presents as an extremely promising pilot study which needs further validation in a larger cohort.

We thank the reviewers for their very helpful comments, all of which have been taken on board in this new improved manuscript. Besides removing the computational modelling section from the manuscript, the three main changes in the new version are:

1. In addition to the 51 nasopharyngeal SARS-CoV-2 RT-PCR positive samples, 182 new cases were added to the study.

2. We show that SARS-CoV-2 ‘variants of concern’ can be identified from the samples taken from smartphone screens.

3. We have extensively elaborated on the interpretation and limitations of our results in the Discussion section of the new manuscript.

In the following rebuttal, we have only addressed the comments of reviewers regarding the SARSCoV-2 phone screen testing method. Below, we provide a more detailed description of our responses to the reviewer comments.

Reviewer #1:

[…] My opinion is that the assay portion of the paper alone would do well as a short report. However, the modeling lacks sufficient link to data and details of an implementation plan to truly inform public health policy or practice.

We have removed the modelling data from the manuscript.

Reviewer #2:

[…] The pilot study is very small. The results are certainly promising, but should not be over-interpreted. The authors do not say if the k-means based partitioning was pre-planned.

We took on board this and other reviewers’ comments regarding sample number and, as mentioned above, we have increased the sample number by 182 nasopharyngeal positive RT-PCR results. Also following this and other reviewers’ suggestions we have further elaborated on many aspects in the discussion of this new version and have also removed the k-means portioning as based on the new data, we decided it is no longer necessary.

[…] The authors should avoid post hoc analysis pathways (like using k-means to divide into two clusters). It's probably OK to report that 26/28 high or medium-load samples were positive, but this proportion should be reported with confidence intervals and (unless the authors had a clearly written plan beforehand to not do this) the overall proportion should be reported with confidence intervals as well.

The k-means post hoc analysis has been removed from the manuscript.

[…] What is needed to make this paper convincing is more data (or better scepticism about the existing data) and more discussion about logistics.

We have increased the SARS-CoV-2 Rt-PCR positive sample number four times and also extensively elaborated on the implications and potential of this new method in the discussion.

I don't understand the claim at L123.

This has been removed from the current manuscript.

Not sure if this is in the reviewer's ambit, but I dislike the explanations surrounding the conflict of interest. The authors should state the facts, they don't need to state that they wish to state them, nor to judge their own conflicts.

We agree with the reviewer and have now just stated the facts.

Reviewer #3:

[…] The sample size is small, with only 51 SARS-CoV-2 individuals (by nasopharyngeal swab) so this must be considered a pilot study rather than a large-scale evaluation of the approach. Clearly, if the approach is to gain any traction a much larger study is needed.

As mentioned above, we have significantly increased the sample number of SARS-CoV-2 positive individuals tested by nasal swabbing and RT-PCR. We expect this is enough for the referees to now consider this a validated method.

The claimed advantages over conventional nasopharyngeal screening are lower costs and faster turnaround times, but no attempt to quantify these are given. This information seems crucial for comparison with other testing approaches (e.g. PCR-based tests of nasopharyngeal swabs and lateral flow tests which are now widely used).

We thank the reviewer for pointing this out. Based on these suggestions we have made significant additions to the discussion which now includes arguments and quantification backing up the lowcost and quick turnaround times we claim for the phone screen testing method.

[…] Comments for the authors:

1. Some of the terminology used is non-standard. For example "quarantine" traditionally applies to isolation of those considered at risk of being infected but who have not yet been shown to be infected. "isolation" would be a better term for what the authors are describing.

This comparison was removed from the introduction.

2. I don't think the comparison with influenza in 1918/19 and talk of the "third wave" (as a universal occurrence) is helpful – it's a very different pathogen, and different countries may experience different numbers of "waves" due to the timing of interventions, emerging variants and seasonal factors.

As mentioned above, this has now been included in the discussion.

3. To better make the case for the advantages of the approach over nasopharyngeal screening, some numbers are needed: costs, turnaround times etc.

As the reviewer has noticed, to maximise the number of tested individuals, there was no selection criteria and all the people who arrived at the Davila Clinic (Santiago, Chile) for a SARS-CoV-2 test were recruited for the study.

[…] 5. To make the case for the value of the approach in a specific population information on smartphone ownership in different age groups is needed.

We have included studies for geographical and age distribution of smartphone usage in the discussion.

6. Another potential advantage over nasopharyngeal swabbing is the lack of physical discomfort. This could lead to greater acceptance of the approach. In future work, it would be interesting to explore this.

We agree with the reviewer and the non-invasive advantage of the phone screen testing method was enhanced in this new version of the manuscript.

7. Clearly, if the remarkable findings reported are to translate into a real-world intervention a much larger study with a better characterised population is needed. In future work the authors could also consider exploring RT-PCR versus lateral flow testing of the phone swabs.

We agree with the reviewer and we are currently embarked on a study comparing lateral flow device antigen testing and phone screen testing results. Comparisons between both methods have also been elaborated in the discussion of this current version of the manuscript.

[Editors’ note: what follows is the authors’ response to the second round of review.]

Reviewer #1:

The revised version of this paper does a nice job of adding more samples and clarifying certain analyses. The removal of the mathematical modeling strengthens the manuscript. The paper demonstrates that self-phone sampling for SARS-CoV-2 appears to be a promising diagnostic approach, worthy of more study.

One criticism is that the advantages relative to lateral flow antigen testing are overstated. Antigen tests offer similar sensitivity and specificity with more rapid turnaround time. This should be mentioned.

We agree with the reviewer and when referring to lateral flow antigen testing, we have replaced:

“Lateral flow device antigen testing has become widely used to screen for COVID-19 cases operated by trained staff (Pavelka et al., 2021), and self-administered (Riley et al., 2021).”

For:

“Due to its high sensitivity, specificity, and rapid result turnaround time, lateral flow device antigen testing has become widely used to screen for COVID-19 cases operated by trained staff (Pavelka et al., 2021), and self-administered (Riley et al., 2021).”
