# Peer review - Round 1

Editors:
- Jan E Carette, Stanford University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64256.sa1](https://doi.org/10.7554/eLife.64256.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this manuscript state of the art techniques are used to systematically mutate the viral genome and measure its effect on viral fitness. This paper provides novel insights in viral pathogenesis and evolution of an important class of viruses.

Decision letter after peer review:

Thank you for submitting your article "Globally defining the effects of mutations in a picornavirus capsid" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Sara Sawyer as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jesse D Bloom (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

This paper will be of interest to scientists studying viral pathogenesis and evolution. The authors use state of the art techniques to systematically mutate the viral genome and measure its effect on viral fitness. The results are robust and support the key claims in the paper.

Summary:

In this manuscript Geller and colleagues describe a deep mutational scan of the coxsackie B3 virus (CV-B3) genome focusing on the structural genes. Comparing the mutations before and after growth of the virus in cell culture allows the authors to derive the mutational fitness effect (MFE) of each mutated residue. After generating this valuable and robust experimental dataset, they compare the MFE with variability observed in strains directly sequenced in nature and observe a correlation suggesting that the experimental fitness in the lab is representative of natural evolutionary processes. They also identify sites under differential selection between the laboratory selection and natural selection, which correspond to known antibody neutralization sites. Using a random forest algorithm the authors show that a combination of evolutionary, sequence and structural information best explains MFE. Finally they focus on the myristoylation and protease cleavage site. The deep mutagenesis allowed for refinement of the 3CDpro cleavage consensus site and allowed for the identification of ~750 cellular proteins that could be substrate. Testing a subset of these, the authors show that 30% indeed could be experimentally verified.

Overall, this well-written manuscript provides an important resource through deep mutagenesis of the picornavirus capsid. The analysis of this dataset and the experimental follow up performed by the authors has generated novel insights in picornavirus structure and function. The study is very nicely done. The data will be of interest to researchers interested in these techniques, as well as researchers interested in picornaviruses themselves. There are also some nice evolutionary and structural analyses, as well as cool use of the deep mutational scanning to identify some new host proteins cut by the viral protease.

1) The authors validate the 3CDpro cleavage sites through expression of 3CDpro outside of the context of viral infection. Looking at the cleavage of the candidate substrates during infection with CV-B3 will be more relevant and perhaps increase the percentage of candidates that can be cleaved by 3CDpro. (Although this would improve the manuscript bolstering the physiological relevance of these candidate substrates, this suggestion is completely optional and not required for acceptance of the manuscript).

2) It would be interesting to extend the analysis to also include the 2A cleavage site. Because only the structural genes are mutated, the analysis can only be done for the site before the protease cleavage residue but might be interesting regardless.

3) Some quite relevant data is now in the supplementary files, which might be missed by the readers. For example the validation with qPCR in Supplementary file 5. Perhaps the result can be also graphed as XY graph showing the correlation in the main figure.

4) The authors refer to "antibody neutralization sites", but they never explain clearly how these were defined. Maybe this is common knowledge in the picornavirus field, but it certainly wasn't obvious to me and would benefit from some explanation. I gather these are sites where mutations escape some antibody?

5) In Figure 2 and some of the surrounding text in the Results (such as the prediction section), it is difficult to tell if the authors are using MFE to refer to the effects of specific mutations, or the mean effects of mutations at each site. This could be better explained for each relevant analysis.

6) Be sure to include adequate text to emphasize these are effects of mutations in cell culture, which might not always mirror effects in nature.

7) The use of the DMS data to make a PSSM to find other proteins cleaved by the protease is cool!

8) Introduction, last paragraph: should be "these data", not "this data".

9) When the authors start using the word "fitness," they should be explicit that this is "fitness" as measured by growth in cell culture, which may not always be precisely the same as fitness in nature.

10) Figure 2A, would be nice if legend is a bit clearer about what "average MFE" (red line) means: I gather average across mutations. Is the average MFE also windowed in 21 amino-acid windows?

11) This is a completely optional suggestion that the authors can feel free to ignore. But we found in our recent DMS that making an interactive heat map (e.g., https://jbloomlab.github.io/SARS-CoV-2-RBD_DMS/) was really useful for enabling people to interrogate the data. These can be made pretty easily using Altair (https://altair-viz.github.io/), and some example code is here (https://github.com/jbloomlab/SARS-CoV-2-RBD_DMS/blob/master/interactive_heatmap.ipynb). Yours would actually be a lot simpler to make as there is just one phenotype shown.
