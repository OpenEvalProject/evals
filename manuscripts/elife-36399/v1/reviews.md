# Peer review - Round 1

Editors:
- Peter A Rodgers, eLife United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36399.024](https://doi.org/10.7554/eLife.36399.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Disequilibrium in Gender Ratios among Authors who Contributed Equally" to eLife for consideration as a Feature Article. Your article has been reviewed by three peer reviewers, and the following individual involved in review of your submission has agreed to reveal her identity: Sandra Masur (Reviewer #1).

We would like to invite you to submit a revised manuscript that addresses the concerns raised by the reviewers – please see below.

Summary:

The authors assembled a data set of 3035 articles published between 1995 and 2017 in a variety of biomedical journals in which 2 or more authors were indicated as having contributed equally. They assigned genders to authors manually by finding online photos of authors for 97% of papers and compared rates of male first authors versus female first authors in a series of analyses. The authors are to be commended for tackling an important topic. There are, however, concerns about aspects of the study designs and the techniques used to analyse the data (see below). The manuscript also contains a surprising number of simple errors.

Essential revisions:

Study design and methods:

1) The authors refined and changed their hypotheses and analytical plan while examining data. This would be fine if they had treated the preliminary data as a pilot study from which they designed their study. However, they appear to have included the original data in their full data set.

2) The methods for assembling the data set are not well described, and from the available description, they seem far from systematic. Phases 1 and 3 are particularly problematic, especially Phase 3, as this came after the majority of data collection. The authors claim their search methods for Phase 2 were systematic but provide few details of the system used. Such necessary details would include: a) On what basis were journals selected? (The authors note that journals were selected because, "they are widely known in the biomedical sciences." Can they support this statement in any way?)b) Did the authors include all google scholar and journal website search results or only a certain number of articles or pages? c) How did they select included papers? Was this done by a single person (not recommended) or did they use two independent analysts (recommended)? If the latter, what was their kappa score?

The authors may wish to consult standard methods of a systematic review to gain a better understanding of what is typically expected for a search to qualify as systematic. (E.g., see: Cochrane Handbook Chapter 6.4, which is freely available online.)

Inferential statistics:

3) A number of the analyses in the manuscript are, unfortunately, unacceptable. I would suggest that the authors consult with a statistician or epidemiologist to help them consider their analytical options, including relatively simple methods such as logistic regression, or perhaps something like generalized estimating equations, to account for any instances of the same author(s) appearing multiple times. With such analyses, they could then include year of publication in the model. This would allow them to draw much more robust findings and conclusions that would strengthen their paper and the impact of all the work they have clearly put into this manuscript. (In my experience, many researchers in the biomedical sciences are not aware of the statistical services that are available at their own institution, so I include the following links in case that is the case here:https://www.jhsph.edu/research/centers-and-institutes/johns-hopkins-biostatistics-center/services/index.html;https://stat.uconn.edu/consulting-info/)

4) The authors have conducted multiple Chi-squared analyses without accounting for the ensuing inflated potential for Type I error. Also, they do not report the Chi-squared statistic and degrees of freedom, only the p-value.

5) The analyses do not account for overall gender composition of the pool of authors. If we only examine the 2-author papers and assume that each author is unique, there are 2*1000 + 581 + 447 = 3028 male authors compared to 2*377 + 581 + 447 = 1782 female authors. (Please also consult work by Sugimoto and Larivière for systematic analyses of male and female authorship patterns.) Is it really therefore surprising that more papers are led by male authors? The authors refer to the proportion of women trainees (citing reference 19) but provide no citation to support their implication that first authors may reasonably be assumed to be exclusively trainees.

6) The analyses do not account for the same person or people authoring multiple papers. Is this possible in this data set? If yes, this potential clustering effect could have been accounted for had they used a multilevel model for their analyses. See also point 3 above.

7) Changes in authorship credit allocation over time are accounted for in a very crude way by splitting the data set into two sets, dividing at 2007. This is not an appropriate way to account for change over time, and only adds to the problem of multiple hypothesis testing. See also point 3 above.

8) The authors have split the dataset into articles with 2 equally-contributing authors and those with more than 2. Like the time-based split, this is problematic. Do the authors have any basis for assuming that there is a difference between these types of credit-sharing such that they must be analyzed separately?

9) In the Results section, the authors note that they looked at the possibility for alphabetical order in a subsample of 2109 papers. Why this subsample? How was this selected?

10) The authors report a confidence interval in their methods but do not apply it in any way in their presentation of results. More worrisome is that the authors have not accounted for the fact that confidence intervals rely on the assumption that the sample population (i.e., the data analyzed) was sampled randomly from the population. This was emphatically not the case in this study. For this reason, the confidence interval calculation does not apply. (A minor point in relation: I was able to reproduce their estimate of a confidence interval of 2.38 using the website they used by leaving the default setting of 50%, which was not the result in their study. This suggests a potential lack of understanding of how to use these calculations.)

Descriptive statistics:

11) Four out of six continents lack sufficient sample size for it to be valid to look at distribution of shared authorship even descriptively. In addition, presenting these descriptive statistics in equally-sized pie charts inadvertently conveys that each continent has an equivalently-sized subsample in the data set.

Conclusions:

12) The data presented in this paper suggest that any gender bias in author order (which certainly appears to have been a legitimate issue in papers published 1995-2007) is no longer a problem in more recent papers. If this is true, this is excellent news and should be presented as such.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting the revised version of your manuscript "Disequilibrium in Gender Ratios among Authors who Contributed Equally". The revised manuscript has been reviewed again by the referee who had the most specific concerns about the statistical analyses employed in the original version (Reviewer #2), and while they welcome many of the changes, they still have a number of concerns that you will need to address (please see below). There are also several editorial points I would like you to address (again, please see below). Although this might seem like a long list (24 points), most of them should be straightforward to address.

Reviewer #2:

The authors have nicely addressed some of my concerns (in particular the statistical analyses are improved-the authors are to be commended for their work to improve the robustness of their conclusions) but some concerns remain, and some minor new concerns arose pertaining to the new analyses. My main concerns remaining have to do with how the statistical analyses are presented.

1) First, for their new analyses, the authors have named their primary outcome variable "gender bias" and defined it as follows: "gender bias in first authorship was defined as first male author when all the authors contributed equally." This is problematic and does not align with how gender bias is defined in other literature. In an ideal world, there would be no gender bias, meaning that the optimal value of a variable named "gender bias" would be zero. Yet, presumably, the authors are not arguing that no man should ever be listed first under conditions of shared first authorship. By naming this variable "gender bias," this is what is currently implied. It would be more understandable to readers (and more in keeping with how this is usually done in studies of sex and gender in humans) to define this variable as something like, 'male author listed first' or perhaps 'm* authorship' in keeping with their notation used elsewhere in the paper. This makes it more intuitive to the reader that the ideal level for this variable is 0.5, not 0.0.

2) Second, it is standard practice to provide a table in the results showing odds ratios and confidence intervals (along with p-values, if one believes those are important, which the authors seem to) for each variable in the model. This would help readers who are familiar with these kinds of statistics more rapidly grasp the findings.

I list these two points first and second because being clearer about how the outcome variable is defined and the odds ratios for each variable in the model could help solve some the following problem.

3) In the Results section, the authors state, "The Odds Ratio of Gender Bias in First Authorship (95% Confidence Interval) using year as a continuous variable was 0.958 (0.931-0.986) with p < 0.01, indicating a significant preference for males in the first position considering all publications from 1995-2017." The statistics presented do not support the authors' statement here. Odds ratios under 1 mean that the outcome is less likely than the reference, not more likely. In other words, the odds ratio presented in this sentence indicates that the variable "gender bias" is less likely than the reference. The authors may want to check with their statistical consultants on this, because based on the raw data presented a few lines up (56% male author first vs. 44% female author first in the n=971 mixed-gender subsample) I would not be surprised to see an odds ratio and 95% confidence interval of 0.958 (0.931-0.986) for female first authorship in that subsample.

4) Re: the alphabetical subset. The authors have added in the manuscript, "This number differs from the larger data set used in the analysis because we began to record alphabetical ordering after the study had begun when we realized this could be an important variable." I appreciate that they have explained why this happened. However, for this to be a complete, robust study, why don't they just quickly go back and record alphabetical or non-alphabetical ordering for the relatively small proportion of early papers (about one quarter of their sample? The fact that they didn't do it at the time doesn't preclude them from doing it now. This is particularly important given the journal's requirement to support replicability. Nowhere in the materials is it clear which papers in the dataset are part of the 2109 for which alphabetical or non-alphabetical order was recorded and which are part of the 787 for which such data were not collected at first glance.

5) More details are needed regarding the data and analyses to ensure replicability. What statistical software (including version) was used? Typically, when writing about statistical analyses, we include the name of the software (e.g., SAS, Stata, SPSS, etc.) or statistical programming environment (R) and version number. This is because the same analyses run in different software could produce slightly different results.

6) Related to the above, is it possible to provide the script or code as an appendix along with the data? This is good practice for ensuring replicability.

7) Results section: The authors state, "Comparing the expected and observed gender ratios yielded a Chi-square statistic of p <0.00.1" A p-value is not a Chi-squared statistic. A Chi-squared statistic would look something like Chi-squared(degrees of freedom)=number like 2.7 or 0.3 or 34.2 or 976.

8) Results section: "estimated 4%" should say "estimated 4% per year" and "1 to 7% decrease" should read "1 to 7% decrease per year."

9) The source data for Figure 2 doesn't appear to match the Figure. The Figure looks like it was plotted using year of publication as a quasi-continuous variable (i.e., there's one point for each year in the data set) while the source data shows year as a categorized variable (pre-2007 and 2007+) along with country/group of countries as a categorized variable.

10) Point 11 noted, "Four out of six continents lack sufficient sample size for it to be valid to look at distribution of shared authorship even descriptively. In addition, presenting these descriptive statistics in equally-sized pie charts inadvertently conveys that each continent has an equivalently-sized subsample in the data set." The authors responded, "We agree with the reviewer's comment. Therefore, in our new analyses, we looked at the country as a three-category predictor: Europe, US and other. The results for these regions matches are comparable suggesting that the trends we are observing are occurring worldwide." The analysis in the revision has addressed this very well and we now have a very nice Figure 5. However, Figure 4 continues to present 6 continents. This means that Figure 4 continues to have the problem of inadvertently conveying equivalency, and, in addition, it now fails to reflect the analyses conducted. I recommend simply removing Figure 4.

11) The original review stated: "16) If grammatically possible, please refer to 'women' or 'female authors' rather than 'females', and 'men' or 'male authors' rather than 'males.'" The authors' response to this was: "Response: Agree. Done." Yet, there are 22 instances in the manuscript of using 'males' or 'females' when it would be completely grammatically possible to refer to 'male authors,' 'men,' 'female authors,' or 'women.' For example, the second sentence in the revised abstract begins, "For mixed gender pairs males were…" A correct rewording of this line would be, "For mixed-gender pairs, male authors were…" It is acceptable to refer to mice as 'males' and 'females' but it is not acceptable to refer to humans in this way in most English-speaking countries, nor in scientific literature describing studies that involve humans as subjects, objects, or participants (e.g., in clinical medicine, social sciences, etc.). Please correct all 22 uses of 'males' and 'females'.

12) Point 16 in the original review noted that in the original Introduction, the authors stated that, "Analysis of articles in 5 medical journals showed that whereas papers listing equal contributions comprised less than 1% of publications in 2000, by 2009 this trend had increased to 3.6-8.6% depending on the journal (8)." In fact, the paper referenced by Akhabue and Lautenbach reports rates from 1.0-8.6% in 2009 in the top 5 general medicine journals. The 1.0% rate is from the BMJ. This means that the rate of co-first authorship in 2009 was 1.0-8.6%, not 3.6-8.6% as claimed by the authors. The change that they made in their revision (removing the reference to the 5 top general medicine journals) has not fixed the problem that their paper makes a claim unsupported by the citation they are using. They need to change 3.6% to 1.0% in order to be accurate.

13) In the file with file name Table 1–source data 1 what does the grey colouring on some rows mean? This should be specified so that anyone aiming to build on or replicate this work can understand the data file.

Editorial points to address:

14) Please consider changing the title to the following:

“Gender Inequalities among Authors who Contributed Equally”

15) Please consider revising the abstract to read as follows:

“We analyzed 2898 scientific papers published in the period 1995-2017 in which two or more authors shared the first author position. For papers in which the first and second authors made equal contributions, mixed gender combinations were most frequent, followed by male-male and then female-female combinations. For the mixed gender combinations, there were more male authors than female authors in the first position, although the disparity was less in the second decade of the period studied. For papers in which three or more authors made equal contributions, there were more male authors than female authors in the first position, and more all-male than all-female combinations. We also show that the disequilibrium in gender ratios among authors who made equal contributions is not consistent with random or alphabetical ordering of these authors. These results raise concerns about female authors not receiving their fair share of credit for scientific papers, and suggest a need for journals to request clarity on the method used to decide author order among those who made equal contributions.”

16a) Please consider replacing the term "disequilibrium in gender ratios" with the term "gender inequalities".

16b) Please consider replacing the terms associations, author associations etc. with the terms combinations, author combinations.

17) Please reword the phrase "the person who does the actual work".

18) Re the sentence that starts: "It is conceivable that some of the disequilibrium in gender ratio in the earlier years…", is it worth mentioning here or somewhere else in the manuscript that, irrespective of the gender breakdown of the science workforce, when considering just those manuscripts with two first authors, one would expect mf to equal fm?

19) Please reword the following sentence to be more precise and/or avoid the word "predominated" (and similar words): "We observed that male-only pairings predominated in author combinations of two or more authors."

20) The sentence "The frequency of multi-author equal contributions dropped rapidly for associations of more than three authors but we observed at least two groupings of 11 authors [Bonham and Stefan, 2017; van den Besselaar and Sandstrom, 2017]." suggest that Bonham and Stefan, 2017 and van den Besselaar and Sandstrom, 2017 have 11 authors, but this is not the case: please clarify.

21) Please move the passage about the limitations caused by the use of Google Scholar ("The approach to search […] in the text of the paper.") to the Materials and methods section, and add a short sentence to the main text stating that this limitation is discussed in the Materials and methods section.

22) Please expand the caption for Figure 2 to better explain to the reader what is shown in this Figure. The revised caption should include a title sentence (in bold). Also, please explain in the caption what the ideal level of this logit function would be. Please also define p(bias).

23) Please expand the caption for Figure 3 to better explain to the reader what is shown in this Figure. The revised caption should include a title sentence (in bold).

24) Please expand the caption for Figure 4 to better explain to the reader what is shown in this Figure. The revised caption should include a title sentence (in bold). Please also explain how these values are predicted.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

I am pleased to inform you that your article, "Gender Inequalities among Authors who Contributed Equally", has been accepted for publication in eLife, subject to addressing a small number of points raised by the referee.

Reviewer #2:

Thank you very much for the opportunity to re-review this paper. The authors have responded extremely well to nearly all my comments, and I believe the paper is substantially improved. There are just a few small corrections remaining:

1. Regarding this passage in the Discussion: “We noted differences between journals in the proportion of pairings…” […]. It's up to the authors, of course, but I think they are underselling their results at this point by calling their findings "preliminary". Also, software for gender identification often uses names as well as, or instead of, images. I would suggest changing, "Hence, our findings should be considered preliminary until confirmed by subsequent studies, which may be able to analyze a larger number of publications across many disciplines through automated searches linked to gender image recognition software," to something like, "Our findings should be complemented by subsequent studies, which may be able to analyze a larger number of publications across many disciplines through automated searches linked to gender recognition software."

2. In discussing their findings in the context of the broader literature, the authors may wish to refer to a similar study published in JAMA, in February 2018, that came across my radar recently: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5838607/
