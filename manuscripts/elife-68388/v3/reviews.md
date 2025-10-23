# Peer review - Round 1

Editors:
- Armita Nourmohammad, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68388.sa0](https://doi.org/10.7554/eLife.68388.sa0)

By using modern high-throughput sequencing this paper demonstrates that the antibody mediated immune responses that are elicited by vaccination are improved by pre-existing memory CD4 T cell responses. The experimental data are an important contribution and would be useful as a data resource for future research. All reviewers agree that the findings are of great interest to the community.


---

# Peer review - Round 1

Editors:
- Armita Nourmohammad, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68388.sa1](https://doi.org/10.7554/eLife.68388.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Preexisting memory CD4 T cells in naïve individuals confer robust immunity upon hepatitis B vaccination" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Rob J de Boer (Reviewer #2); William S DeWitt III (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Improve the statistical analysis for comparing the early- and late-converters: The authors compare Shannon entropy for day 60 vs. 0 and claim that the difference is more significant in early converters. The p-value however is marginal and does not support such strong claim, especially after taking into account multiple test correction. Please improve this analysis.

2) Develop a randomization test and a null model to show that the expansion of Ag specific T cells from day 0 to 60 is indeed significant.

3) Discuss how the commonality or differences in HLA types may impact the conclusions of the paper.

4) Since you cross validation is done for the ROC curves, please add error bars to the plots as well.

5) Better clarify the procedure for Rhbs measure. What is the distance d? How is the distance cutoff parameter for epitope based classification is chosen? What are the statistics of bystander and non-bystander sequences? How robust are the results to this exact choice?

Ideally the authors should try more suitable TCR distance models like TCRdist by Dash et al. for this analysis.

6) Clarify the language throughout the manuscript as detailed by reviewer #2.

7) Better clarify the mathematical notations in the manuscript.

8) Improve the code in GitHub.

9) Improve the quality and resolution of the figures.

Reviewer #1 (Recommendations for the authors):

1. Please make images properly in pdf – one can't zoom in and sometimes axis labels are unreadable.

2. Since you are doing cross validation in the ROC curves, please add error bars to the plots as well.

3. Figure 5a: I guess you tried to look for significant difference for all possible cell subsets. Have you corrected the p-value for multiple testing?

4. Given that the a central result of the paper derives from the ratio Rhbs measure, more care must be given to properly explain what you are doing:

5. What is the distance d?

6. How do you set the free parameter c?

7. How many bystander and non-bystander sequences you have?

8. What do you get without the bystander normalisation (only numerator)?

9. Could you explain in more detail how do you select these bystander sequences?

10. Is this bystander normalisation already enough to classify early vs late converters or do you get also information from the numerator?

11. line162: can we understand this from the fact that late converters haven't yet built a proper response at day 60?

Reviewer #2 (Recommendations for the authors):

The manuscript is not well written and most of the readers will not easily understand what exactly has been done in the various analysis. Most of my review will therefore asking for clarification.

Generally the language is not very exact. A few examples from page 4:

"Antigen presentation via major histocompatibility complex (MHC) (encoded by HLA genes), together with the right costimulatory and cytokine signals, are responsible for T cell activation (Curtsinger and Mescher, 2010; Esensten et al., 2016)."

– I miss the word proteins after (MHC).

On line 90 you write "the highly degenerate nature of the CD4 T cell recognition" and above you wrote that specificity is imparted.

Line 142: we detected a significant increase in the TCR repertoire Shannon's entropy for early-converters (Figure 2a): this looks like a very minor difference in Figure 2a. Which test was performed and what is the effect size?

Line 143: please explain what you mean by "less clonal".

Line 153: measuring CFSE on day 60 and tracking clones from time point 0 to 60 probably means that you search for the clones that dilute CFSE on day 60 in the day 0 repertoires. This is not explained.

Line 156. "a significant increase in the frequency of unique HBsAg-specific TCR sequences": what is the frequency of a unique sequence? Its abundance? Why then the "unique"? Do you mean "a significant increase in the abundance of TCR sequences specific for HBsAg peptides"?

Line 167: "Thus, although we see a rise in the number of vaccine-specific TCR clonotypes from day 0 to day 60, this cannot be attributed to an expansion of preexisting TCR clonotypes but rather the recruitment of new TCR clonotypes" I don't see how the number of vaccine-specific TCR clonotypes could have increased by an expansion of preexisting TCR clonotypes.

Line 169: "rather the recruitment of new TCRB clonotypes (presumably from the naïve T cell compartment): how about memory clonotypes that were not present in the day 0 sample?

Line 200: Unclear sentence: "These classifications were integrated into a model which outputs a ratio Rhbs for any TCR repertoire representing the amount of HBsAg peptide-specific clonotypes". Is the ratio Rhbs predicting the fraction of HBsAg peptide-specific clonotypes in a repertoire? Note that ratio, amount and fraction would then have the same meaning.

Line 200-215 is poorly written, e.g.,

– This model applied to the memory repertoire at day 60 shows.

– To account for the age variable, a model in which.….

Line 234-237 Hard to read sentence.

Reviewer #3 (Recommendations for the authors):

There are some mathematical notation issues that make it difficult to understand the discriminative ratio R, as defined on line 591 in the methods. The function d(.,.) was previously defined as a hamming distance between sequences, but in this definition it takes arguments trepi and tpep, each of which is defined as a set of sequences. My interpretation is that {trepi | d(trepi, tpep) < c} means something more like {x ∈ trepi | min_(y ∈ tpep) d(x, y) < c}.

The code on GitHub needs substantial improvements to documentation. I was unable to find the part of the code where the c parameter is set for Rhbs, or where the epitope specific clones are held out for the individual being classified in the LOO procedure. I suggest expanding the readme to detail how to use each script, perhaps with example commands, and where various important methodological details are implemented.

Many figure panels are of such low resolution that axis labels and annotations are illegible.

I would expect that HLA type would strongly influence the inter-individual relevance of the peptide specific TCRs, and the performance of this classifier (especially between individuals with different genetic backgrounds). Can the authors comment on why this wasn't an issue in this study?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Preexisting memory CD4 T cells in naïve individuals confer robust immunity upon hepatitis B vaccination" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Giulio Isacchini (Reviewer #1); Rob J de Boer (Reviewer #2); William S DeWitt III (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

By using modern high-throughput sequencing this paper demonstrates the antibody mediated immune responses that are elicited by vaccination are improved by pre-existing memory CD4 T cell responses. The experimental data are an important contribution and would be useful as a data resource for future research. All reviewers agree that the findings are great interest and the revision has addressed all the previous concerns.

Essential revisions:

1) Figure 1—figure supplement 1: early converters subfigure. Comparison between 180 and 365 does not look significant. Is the **** indication in the figure a mistake?

Reviewer #1 (Recommendations for the authors):

The revised manuscript has considerably improved in quality and is ready for publication. The authors have clearly responded to the observations raised by the reviewers. The paper describes an original and important study and is of interest for eLife readers.

Reviewer #2 (Recommendations for the authors):

I have read the rebuttal letter and find that the authors have responded well to my suggestions.

Reviewer #3 (Recommendations for the authors):

The authors' responses to my comments on their initial submission are very thorough, and all of my concerns have been adequately addressed. They have improved the rigor of several statistical analyses, and clarified presentation of technical aspects that had previously been vague or confusing. They have also improved the open source code repository, adding more clear documentation of where key methods from the paper are implemented.

The findings of the manuscript are convincing, and the data is a valuable resource. I have no further concerns.
