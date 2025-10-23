# Peer review - Round 1

Editors:
- Talía Malagón, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84673.sa0](https://doi.org/10.7554/eLife.84673.sa0)

This paper presents an important effort to develop an open-source software framework for monitoring trends and variations in healthcare over time in England. They demonstrate a compelling example of how this system can track key healthcare indicators over the course of the COVID-19 pandemic. The paper will likely be mainly of interest to stakeholders in England, but could inspire the creation of similar systems in other countries.


---

# Peer review - Round 1

Editors:
- Talía Malagón, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84673.sa1](https://doi.org/10.7554/eLife.84673.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Eleven key measures for monitoring general practice clinical activity during COVID-19: A retrospective cohort study using 48 million adults' primary care records in England through OpenSAFELY" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor.

As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential revisions:

1. Add to the discussion more on the types of future analyses and data needs this platform could be used for.

2. Explain how this work differs from earlier work using the OpenSAFELY platform, as the novelty was not clear to reviewers.

2. Expand on whether the platform can be used to explore trends in specific populations, including vulnerable populations.

3. Comment on the gap in indicators identified by reviewer #3 (mental health, maternal or child health).

4. More thoroughly describe the underlying clinical activity which is intended to be measured by each code.

5. Comment on whether any validation exercise was undertaken to validate whether selected codes identified the target clinical or laboratory measurements.

Reviewer #1 (Recommendations for the authors):

No particular concerns about methodology.

The Results section is a little light, I would have liked to see more analyses of the data, while I admire the extensive work that went into developing this system, currently, it looks like the type of information the system can generate is not extensive. It would be nice to add more to the discussion about the types of future analyses and data needs this platform could be used for.

Reviewer #2 (Recommendations for the authors):

The authors only reported overall trends, without consideration of different (vulnerable) patient groups. It would be meaningful to analyse whether there were (and still are) certain populations that experienced a higher decrease in clinical activity due to the COVID-19 pandemic, in order to issue targeted initiatives.

Reviewer #3 (Recommendations for the authors):

Abstract: the abstract talks about "11 key measures of primary care clinical activity" but there are no examples given, so it is difficult to get a sense of what is actually being measured without reading the full paper. I suggest including some examples of the measures.

Background: as in the abstract, it would be helpful to state some examples of 'clinical activity'.

Key measures of clinical activity: the manuscript talks about CTV3 and SNOMED CT codes but it would be helpful to start off by describing the underlying clinical activity which is intended to be measured. For example, measurement of frequency of diagnosis codes may be a measure of patients seen with a particular condition or diagnosis coding activity (i.e. the proportion of diagnoses that are recorded in coded data rather than free text). Prescribing and laboratory investigation measures are more likely to measure actual clinical activity as these are almost completely recorded electronically.

The authors could also consider the use of the SNOMED CT hierarchy to generate codelists using knowledge of which codes are subtypes of others. This would simplify the description of the codelist and would ensure that future codes are automatically included if they are in an appropriate place in the hierarchy.

Table 1: SNOMED CT coded events can be of a variety of semantic types including records of diagnoses, investigation results, prescriptions etc. The table should state the clinical activity that is intended to be measured, and then the way this is represented and detected in the GP systems (i.e. TPP and EMIS), rather than lumping together as 'SNOMED CT codes'. This is because other (existing or future) GP systems may record such information differently (e.g. in Vision each SNOMED CT coded entry has an 'entity type' which denotes the type of information that is contained within that entry, so there is a distinction between e.g. BP measurements and BP diagnoses). I would expect that validation has occurred to ensure that the SNOMED CT codes used to record common clinical or laboratory measurements are those that would be expected.
