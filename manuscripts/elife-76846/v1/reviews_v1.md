# Peer review - Round 1

Editors:
- Grégoire Altan-Bonnet, https://ror.org/040gcmg81 National Cancer Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76846.sa0](https://doi.org/10.7554/eLife.76846.sa0)

In this manuscript, the authors quantitatively analyze the growth curves for E. coli under a large number of growth conditions and use different machine learning methods to tackle the combinatorial complexity of conditions as well as to predict growth parameters from media composition. The large datasets and the use of ML to handle such complex modeling will be of general interest to the biology community.


---

# Peer review - Round 1

Editors:
- Grégoire Altan-Bonnet, https://ror.org/040gcmg81 National Cancer Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76846.sa1](https://doi.org/10.7554/eLife.76846.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Machine learning-assisted discovery of growth decision elements by relating bacterial population dynamics to environmental diversity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Naama Barkai as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Anne Thessen (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) There are concerns about the robustness of the experimental results e.g. because cells were not allowed to adapt and because consumption of nutrients was not accounted for. While redoing all the experiments would be too cumbersome, we would recommend that a few confirmatory experiments (e.g. comparing growth curves for adapted and non-adapted strains) be performed.

2) The strength of the machine learning approach (compared to simpler and easier to interpret methods such as principal component analysis, partial least square regression, etc.) needs to be documented. Please introduce a metric that helps the reader better assess the strength of the statistical analysis

3) A stronger discussion of the approach and/or analysis and/or results will be necessary to highlight the novelty of this study. In its present version, reviewers read underwhelmed by the findings.

Reviewer #1 (Recommendations for the authors):

1) Panels in Fig. 4B would benefit from a violin representation in order to better represent the distribution of parameters. The concentration dependence for the lag time and the growth rates do not look graphically striking while the cor and p values look impressive. The authors should comment on this discrepancy.

Reviewer #2 (Recommendations for the authors):

I have two methodological concerns.

1. Cells adapting to growth media: First test to see if you have this problem by finding out what growth media was used at the culture facility where this strain was acquired. Do your data show any correlations with the conditions similar to that growth media and a short lag phase, high max growth rate, or high max biomass? Is this strain growing better in growth media that more closely resembles the growth media it is already used to? The best solution is to go back and do the experiments again with adapted cultures, but I know that is too much work.

2. Changing chemical concentrations and ratios: The easy fix is to acknowledge and discuss this as a limiting factor in your conclusions or explain how this does not matter for this particular study. The best you can say is that the max growth rate is highest in growth media with high initial sulphate concentrations (or some equivalent statement). Sometimes the ratios of chemicals can be more important than the concentration. You can also be seeing the effects of different metabolites being released into the growth media.

Alternatively, you could make this paper about ML methods and replace the biology-specific claims with a very small literature search that shows your results are biologically plausible.

Keep in mind that even though you are doing a highly controlled experiment, the cells are adapting, the population is evolving, and the amounts and types of chemicals in the media are changing.

Specific Issues

1. I don't see that the data are available.

2. Is the gene expression in Figure 8 actually "differential" gene expression? If so, what is it compared to?

3. Considering the problems with the biology, I'm not convinced you can predict the best growth media for a desired outcome.

4. Please use active voice.

5. Check your results to see if osmotic balance is having any effect (since you are using "highly pure water").

6. Autoclaving can cause media to change in important ways. Make sure you did not have this problem.

7. There are results from simulations present, but no discussion of if they are biologically plausible.

8. I don't think you should be trying to do a prediction task at this point (S3).

Reviewer #3 (Recommendations for the authors):

1) I can't find what the paper is solving that to date was not known. Why should the community care or take home?

2) PCA plot and text show that there is an association between media components and E. coli growth. Isn't that obvious?

3) 6 different off-shelf ML models are used for the regression and one was chosen for interpretation. That's fine but I do not see the innovation here. It say like to say doing PCR to amplify a gene or CRISPR for a deletion. Off-the-shelf ML methods are now established protocols to run classification/regression when the predictor matrix is very big. What is new here? The application to E. coli growth curve inferred parameters?

4) Growth decision-making. Is this term established and defined in the field. Here it is not explained. Also, who is deciding, the bacteria? Bacteria do not decide.

5) Sensitivity analysis section is not clear and I especially do not understand how the authors arrive at the final claim (sentence) in that section.

6) Line 165-167. I do not understand the sentence. Are the authors claiming S (sulphur) to be the most abundant material on earth? What is the relationship with the results of the FBA modeling? I do not find a connection or at least it is not well explained.

7) The paper lacks validation. External validation. The authors make claims about bacteria being able to avoid extinction etc. Prove it. The authors are using E. coli growth curves one of the easiest and quickest experimental systems available. Would be great if they could experimentally validate what they claim. In this shape, it feels a bit of an elaborate way to analyse growth curve data.
