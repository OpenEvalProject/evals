# Peer review - Round 1

Editors:
- Peter Rodgers, eLife United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72185.sa1](https://doi.org/10.7554/eLife.72185.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Consensus-based guidance for conducting and reporting multi-analyst studies" to eLife for consideration as a Feature Article. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by the Peter Rogers, eLife Features Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Florian Naudet; Ioana Cristea.

The reviewers and editors have discussed the reviews and we have drafted this decision letter to help you prepare a revised submission.

Summary:

The report describes a consensus-based guideline for multi-analyst studies. Overall, the manuscript provides very helpful suggestions, but I have some doubts about how much such a resource-intensive tool (beyond the rather simple version of independent reproducibility checks) will actually be used by researchers. As it stands now, the audience for such a guideline is both highly select and also I would imagine very limited (at least for now). On the other hand, as demonstrated by several papers the authors cite (such as Botvinik-Nezer et al.), the approach can have profound consequences for the practices of an entire field. However, there are a number of points that need to be addressed to make the article suitable for publication.

Essential revisions:

Section on Methods (for the expert consensus procedure)

1. Line 129: Please provide a reference for the "reactive Delphi" expert consensus procedure. Also, please comment on whether or not you followed any existing guidelines (eg CREDES) for reporting Delphi survey studies.

2. More information is needed on the process of recruiting experts. How was the list of existing many-analyst studies collected (e.g., systematic search, word of mouth)? What was the criteria for selecting "experts on research methodology"? What reasons were given by those experts who declined to get involved? Is there a minimal number of experts required for these kind of Delphi surveys? And what was the rationale for including only experts, and not a wider sample of people who might use the guideline in the future?

3. What was the rationale behind the threshold for expert consensus which was preregistered as IQR <= 2 and median >=6 (https://osf.io/dgrua)? I'm curious about why a minimum level of satisfaction wasn't sought (e.g. items 6 and 8 both have a response of "1", indicating maximum disagreement).

4. I think that more could be said in the text about the results of the consensus panel, and that consensus ratings for each item should at least be described in the main manuscript and not just by referencing a link to OSF.

5. It was a bit surprising to me that so there was so little disagreement between the expert panel on virtually all points of the guideline. This could be due to the fact that all the components of the guideline, with few exceptions, are pretty standard in terms of transparency and thus hard to disagree on (or might reflect that the relatively few multi-analyst studies conducted so far were conducted with an exceptionally high degree of rigor and transparency.) Please comment on this lack of disagreement.

Related to this, I found the section on "Practical Considerations" more nuanced and I assume there could have been some areas of disagreement in assembling this section. It would be interesting if the authors could reflect on some of these disagreements by, for instance, emphasizing points of discussion that were more controversial or where there was a more coagulated minority opinion, if any.

6. Sub-section on "Deciding on the number of co-analysts" (Lines 220-235).

My understanding is that the number of analysts needed may depend on the research question and also on the complexity of the dataset that would be analyzed. I would expect more discussion and guidance here. Currently, I don't think that this sub-section is really useful. Providing some examples would also be very helpful.

Section on Practical considerations

7. This section includes links/references for a couple of tools for any researchers who are considering embarking on their first many-analyst project (eg "instructions for reporting an effect estimate" and tenzing): it would be helpful to includes links/references for more such tools and resources, such as templates for providing the research task to many-analysts, a guide to automating emails, or a tutorial on using container images.

8. Line 271: Please provide examples of the standardized metrics that might be used for reporting results, and comment on how one might select one metric over another.

9. Please add a sub-section on "Providing the Research Questions" to the section "Providing the Dataset, Research Questions, and Research Tasks".

10. Sub-section on "Presenting the methods and results". Please give three or four examples of publications where the authors have done a good job of presenting their methods and results: please also cite the relevant figure(s) and/or table(s) for each example.

Other sections

11. Please add a paragraph to the "Conclusions" section on how you plan to disseminate these guidelines (eg, via the EQUATOR Network?)

12. There are guidelines on developing reporting guidelines for health research (eg Moher et al. 2010 Guidance for developers of health research reporting guidelines. DOI: https://doi.org/10.1371/journal.pmed.1000217). Please comment on whether or not you followed any such guidelines.

Improving the supplementary data

13. These comments are for the supplementary data file https://osf.io/qc7a8/ downloaded on 25 August 2021.

i) The excel formulas to calculate the Median and IQR are missing the rows for experts 45-49 (row 44 is blank, maybe this caused an error?). E.g. the formula in cell B53 is "=MEDIAN(B2:B44)", when it should be "=MEDIAN(B2:B50)". Fixing the formulas doesn't substantially change the results.

ii) There are no data descriptions provided in the excel file. It is not hard to work out what all the numbers and column headings mean by going back to the manuscript, but, given this is a conduct guideline and the last item is about the FAIR principles, it would be nice to lead by example and provide detailed metadata to make the document easy to re-use.

iii) Not all the data has been made publicly available. The registration page (https://osf.io/dgrua) said "All collected raw and processed anonymous data will be publicly shared on the OSF page of the project." Instead, only partial, processed data from the final consensus survey are provided (the free-text comments are not included). It would be great to see two raw files exported from Qualtrics (with names removed/anonymized): one for the preparatory survey, and one for the consensus survey.
