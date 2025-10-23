# Peer review - Round 1

Editors:
- Ben Cooper, Mahidol Oxford Tropical Medicine Research Unit Thailand

Reviewers:
- Ben Cooper, Mahidol Oxford Tropical Medicine Research Unit Thailand
- Nick Ruktanonchai

## Review text

DOI: [10.7554/eLife.47602.026](https://doi.org/10.7554/eLife.47602.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Local human movement patterns and land use impact exposure to zoonotic malaria in Malaysian Borneo" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ben Cooper as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Neil Ferguson as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Nick Ruktanonchai (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study builds on previous work establishing environmental risk factors for human infections with the zoonotic malaria Plasmodium knowlesi and uses human movement data obtained by GPS tracking, spatiotemporal models of mosquito distribution, and spatial land use data to provide a new perspective on P. knowlesi transmission. The analysis predicts that more than 90% of infectious bites will occur in areas surrounding households at forest edges.

Essential revisions:

The reviewers were agreed that this work potentially represents a significant advance to the P. knowlesi literature. However, there were concerns that some aspects of the work were not clearly motivated, and considerable attention to both the Materials and methods and Results is needed to ensure the work is clearly described, accessible to a broad audience and repeatable. Specifically, the following three points were considered essential revisions:

1) Provide a null model for comparison to illustrate added value of data.

Also, clarify the value of the BRB model over simpler approaches such as kernel smoothing or linear interpolation.

2) Fully describe the results about different land use patterns.

3) Clarify multiple aspects of methods and improve reporting.

A detailed list of specific points that need to be clarified can be found in the individual reviews below.

Reviewer #1:

This paper describes some interesting data concerning human movement patterns and there has been some sophisticated statistical modelling. However, I only have a superficial knowledge of the zoonotic malaria literature and, after carefully reading the manuscript, feel that I am not in a position to judge whether or not this work represents a substantial step forward in understanding the epidemiology of P. knowlesi.

1) I couldn't follow the model specification in the subsection “Human space use”:

e.g. these points were not clear

"we randomly sampled equal numbers of absences within the study site". I don't know what this means. Is this sampling from the data? What are the "equal numbers" equal to? These "absences" were sampled, but what was done with the samples? I may be missing something very obvious here, and perhaps this will be familiar to people working with similar models, but I could only begin to guess what is being done here and why.

Is "occurrence" the same thing as "presence" or something else? It hasn't been made clear what "occurrence" means here.

The first equation suggests "occurrence" for individual j in cell i is defined to be 1 if utilisation of that cell by the same individual is greater than 0. How does this relate (if at all) to the earlier statement that "absence" was defined as a grid cell with a UD of less than 0.00001?

I'm confused by the second equation as well, as the zij values are defined in terms of the yij values in the first equation, but the yij values are defined in terms of the zij values.

2) –Subsection “Exposure to infected vectors”, last paragraph. I couldn't make sense of this section. Specific questions:

i) rit, is a risk and so on the interval [0,1]. However, nothing in the first equation of this paragraph bounds the calculated rit to this interval. Is the implicit assumption that rit values will always be much less than 1 so that there is no need to worry about these bounds?

ii) How are ajt and Zj quantified, and how is uncertainty in these quantities accounted for?

Reviewer #2:

In 'Local human movement patterns and land use impact exposure to zoonotic malaria in Malaysian Borneo', the authors analyze a unique set of data to understand the role of human movement and land use patterns on the risk of exposure to P. knowlesi in Malaysia. P. knowlesi has unique ecological and epidemiological characteristics which makes the interdisciplinary approach (by capturing data about different environmental and human behavioral factors) particularly relevant. The authors use statistical models fit to GPS logger data from individuals, mosquito biting data, and geographic data to identify locations with the highest risk of P. knowlesi exposure. The primary result is that the majority of risk is nearby houses or forested areas, a useful finding that would be strengthened if more background about current public health interventions was provided. Given this result, there are points in the text where it appears that the manuscript was written for other results – based on these results it does not appear that the very detailed nature of daily movement patterns (which are quite variable) was not relevant to risk (since night time movement patterns were fairly consistent across groups). This is a useful and valuable finding, but often the text does not appear to emphasize the actual results (which should not be dismissed) presented.

Overall, there are three primary concerns about the current manuscript.

1) The authors do not provide a null model for comparison. Undoubtably, these data were time consuming and expensive to collect and it would not be feasible to collect these data systematically. However, the authors do not provide a reasonable null model as a point of comparison to clearly illustrate the added value of their data. For example, if you assumed that individuals spent 85%, 90%, 95%, etc. percentage of their time at their residence location instead of using the detailed GPS loggers, are the results substantially different? Similarly for the mosquito biting data, if you assumed that biting increased with forest cover, then how different are the results compared to the detailed analysis the authors provided? Since the final results are in terms of where there is the highest risk, it would be useful to see a comparison of where do these additional data and analyses add value by identifying locations of high risk that would have been missed otherwise. Without this type of comparison, which should be within the scope of the current article, it is difficult to assess how these results are different from a simpler model and set of assumptions. In general, it would be helpful if the authors highlighted where it would have been assumed that there was high risk if not for this analysis.

2) The authors do not fully describe their results about different land use patterns. Throughout the manuscript, the authors note that geographic variables about land use may not accurately reflect how individuals actually use the land. This is an important point and a useful topic to study for spatial analyses of infectious diseases that utilize these types of data. However, it is not clear exactly how their results translate to which types of patterns of use actually correspond to the geographic variables. For example, do certain geographic covariates correspond to different travel behavior? And in which instances do the different land use variables seem to better approximate similar travel behavior (within variable heterogeneity of use)?

3) Finally, it is unclear if the authors took into account or adjusted for their sampling scheme and the level of interpolation applied. Are there measures of uncertainty that could be applied to the analysis, perhaps informed by a null model? In addition, the total number of person nights appears to be highly correlated with the placement of the houses – which would suggest a spatial sampling bias, however there are a number of areas in red up to hundreds of kilometers from the houses. To what extent are these areas with a high number of person nights a function of the statistical smoothing or other covariates versus the raw data? It is understandable if the raw GPS coordinates are not made publicly available, but without additional information about the actual data and a more through presentation of these data, it is unclear to what extent these results are reflective of the actual travel patterns.

Reviewer #3:

Overall, this was a very well-written and interesting paper. The authors have done a generally good job writing up a pretty comprehensive set of analyses, and it represents an important step forward for modeling the spatial interaction of human movement patterns and vector borne disease transmission.
