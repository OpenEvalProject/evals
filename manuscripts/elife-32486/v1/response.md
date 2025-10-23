# Author response - Round 1

Authors:
- Nick R Parsons ([ORCID: 0000-0001-9975-888X](https://orcid.org/0000-0001-9975-888X))
- M Dawn Teare
- Alice J Sitch ([ORCID: 0000-0001-7727-4497](https://orcid.org/0000-0001-7727-4497))

## Response text

DOI: [10.7554/eLife.32486.015](https://doi.org/10.7554/eLife.32486.015)

Title:

The current title indicates that the paper is going to show that "Unit of analysis issues continue to be a cause of concern in reporting of laboratory-based research", but that is not what the paper does. Rather, the paper provides guidelines on how to understand the concept of "Unit of analysis" and analyse experiments appropriately. The title should be changed to reflect this.

Title changed to “Unit of analysis issues in laboratory based research: a review of concepts and guidance on study design and reporting”.

Essential revisions:

Currently the article contains no guidance on sample size calculation for either the "simple" analyses or the more complex analyses. Nor does it contain any guidance on minimal sample size for the modelling methods suggested. Some comments on sample size and power would be valuable as these are issues that are often neglected by lab scientists. It would also be useful for anyone considering more complex analyses to have an idea of the minimum sample size that can realistically be used to fit the models.

A new subsection has been added, after the ‘Analysis’ subsection, that discusses sample size estimation from initially a very simple design, to more complex GLMMs via simulation.

Subsection “Design”. Different designs. Please include some examples of experiments for each situation, as this would make it easier for lab scientists to recognise their type of sample in this list. The example of groups of subjects seems to refer to situations where interest is in the group itself. A common situation instead is where interest is on the effect of treatment on an individual (the experimental unit), but the individuals happen to be grouped (correlated), and it could be useful to clarify this distinction. For example, in laboratory studies the samples may have been analysed in different batches.

Simple examples have been added to the design types in the subsection “Design”. The ‘Groups of subjects’ example has been expanded to cover the kind of ‘batch-effects’ identified by the reviewer.

Appendix 2 in its current form may not be very helpful or informative to the majority of readers. It does not really explain how to choose among alternative designs, and the equations are likely to be forbidding to non-statisticians. While there are no space limitations in eLife, it should be rewritten to focus on the design issues: when should you get more measurements per subject, vs. more subjects? What good are such within-subject replicates (e.g. small improvements in precision, but particularly to be able to measure assay error). It would also benefit from a box summarising what it is showing in a couple of simple sentences, so people that can't get through the equations can at least understand the point it is making.

Appendix 2 has been modified to discuss fundamental design issues for a putative example experiment. It now focuses more on design issues, and uses less mathematical language that should be more accessible to readers of eLife. The mathematical details of the (incorrect) naïve analysis has been moved to a separate new appendix (Appendix 4).

The code in Appendix 3 is very helpful, but it is difficult to read in its present form. We recommend publishing it in text form using indentation, colours, and explanatory text interspersed with the sections of code to explain it. Ideally, it should be written as a tutorial (with portions of text and code interspersed).

Appendix 3 (R code for examples) has been completely revised and re-written along the lines suggested here. It is now written in the style of a tutorial with code indented and coloured to distinguish it from the main text. R output is also now provided to help those wishing to check exactly what would be produced if the code were pasted directly into R.

It would also be good to show how the data for each of the examples is structured within a database – i.e. with variables representing the individual, clustering, groupings etc. Lab scientists are generally less familiar with how data is entered/stored in databases/stats software, and they may be familiar with GraphPad Prism, which accepts data in very different formats to the standard format required for the analyses presented in this paper. Appendix 3 could be expanded to include the data frames next to the R code (at the start of each example).

We agree that the data entry in the previous example R code was not realistic. Appendix 3 now explicitly shows the format of the data in R. A note is also added to explain how data would normally be entered using the read statement that will import data into R from standard spreadsheets or databases.
